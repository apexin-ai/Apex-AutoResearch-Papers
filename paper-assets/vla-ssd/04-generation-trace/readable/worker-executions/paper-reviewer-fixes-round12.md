# paper reviewer fixes round12

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/workers/worker_paper_reviewer_fixes_round12_20260519T115635.log`
- **Structured JSON:** [`2c5e3a44395bef34431a.json`](../../sessions/2c/2c5e3a44395bef34431a.json)

## Before a recorded user message

78 recorded events

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
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
  "uuid": "48cdde1b-f1ac-478b-a35b-45b1881ecd07",
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
    "resetsAt": 1779198000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "64a0ab92-411a-4a59-a135-eb0c3cadeb88",
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant tex files to understand the current state before making changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "3023f12c-0a65-4fc9-9a33-4a5d31281a89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMkgkujJSNduSmVyjL958M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13405,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13405
      },
      "output_tokens": 26,
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

开始逐项修改。先读取所有相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "16132ecc-be7f-4184-a26c-46f891d36482",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMkgkujJSNduSmVyjL958M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13405,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13405
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — Read · `toolu_01MiSSvGvCAhfXdPKzKSkXvk`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "0a5c6789-6636-4f2f-b09e-fdf340716110",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMkgkujJSNduSmVyjL958M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13405,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13405
      },
      "output_tokens": 26,
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

_source line 7 · 2026-05-19T11:56:47.889Z_

<details><summary>↩ Tool result · `toolu_01MiSSvGvCAhfXdPKzKSkXvk`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
8	\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\ref{tab:counterfactual}).
9	\emph{Supporting}: (3)~attention gradient ($0 \to 9 \to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).
10	\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\times$; Table~\ref{tab:specificity_control}).
11	
12	\paragraph{Mechanistic interpretation.}
13	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; counterfactual ordering follows token novelty ($\rho = 1.0$; \S\ref{sec:learned_routing}).
14	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; Appendix~\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.
15	
16	\paragraph{Functional stages and predictions.}
17	The per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\sim}56\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).
18	The entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\to$ 0 heads), suggesting exit routing serves multi-task flexibility (\S\ref{sec:learned_routing}).
19	Predictions: cross-attention VLAs ($\pi_0$~\cite{black2024_pi0}, Octo~\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.
20	
21	\paragraph{Task-dependent routing.}
22	The routing effect is task-dependent: instruction-discriminative tasks show $2.5\times$ larger $|\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\ref{tab:task_complexity}), rising to $6.5\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\ref{sec:task_complexity}).
23	For deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.
24	
25	\paragraph{Limitations and scope.}
26	We study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
27	Llama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.
28	All analyses are open-loop; our routing analysis (\emph{where}) complements H\"aon et al.'s~\cite{haon2025} (\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "7c4e25e4-0e21-4b88-8de4-7c584721f174",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.\n\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).\n\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).\n\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; counterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), suggesting exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01WLTe1doVQhgUzaTYTRWNge`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "5b5fde65-10db-4816-bf39-19b78e6148c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMkgkujJSNduSmVyjL958M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13405,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13405
      },
      "output_tokens": 26,
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

_source line 9 · 2026-05-19T11:56:48.428Z_

<details><summary>↩ Tool result · `toolu_01WLTe1doVQhgUzaTYTRWNge`</summary>

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
27	The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
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
53	L1 readout attention across three conditions (Table~\ref{tab:routing_gradient}; Figure~\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\%$ text); Llama-2 base 9/32 ($36.5\%$); VLA fine-tuning 24/32 ($57.7\%$), a redistribution beyond inherited priors.
54	Per-token normalization ($38.2\times$ text-to-image ratio; Appendix~\ref{sec:attention_decomp}) corroborates this redistribution.
55	
56	\paragraph{Redistribution of routing across depth.}
57	The 32-layer profile (Figure~\ref{fig:attention_profile}) shows qualitatively distinct patterns.
58	Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).
59	VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\%--70\%; Appendix~\ref{sec:threshold_sensitivity}).
60	
61	\paragraph{Task-specific sharpening.}
62	A fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\ 6--11), sharpening entry-exit routing to entry-only.
63	Probe accuracy is preserved (L1: $99.7\%$; Appendix~\ref{app:finetuned_probe}).
64	
65	\paragraph{Probe robustness corroborates the pattern.}
66	Cross-instruction probes corroborate the three-condition gradient (Appendix Figure~\ref{fig:probe_conditions_appendix}).
67	Training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\_mean changes minimally ($\Delta \leq 1.7\%$; Appendix~\ref{sec:training_effect_summary},~\ref{sec:action_r2_threecond}).
68	
69	\paragraph{Open-loop functional sensitivity.}
70	We ablate attention to instruction tokens at the readout position.
71	Ablating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\footnote{$R^2$ values differ from Table~\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.
72	We compare against 10 random subsets of 24 heads (Appendix~\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \pm 0.013$ ($z = -2.73$, $p = 0.003$).
73	Dominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.
74	In the original extraction pipeline (\S\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\Delta \approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\ref{tab:per_task_r2}).
75	
76	\paragraph{Action trajectory validation.}
77	Ablating 24 instruction-dominant heads alters $72.3\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\%$), concentrated on the gripper dimension (shift $0.291$ vs.\ $< 0.034$; Tables~\ref{tab:attention_decomp},~\ref{tab:per_dim_mae}; Appendix~\ref{sec:action_trajectory}).
78	
79	\paragraph{Dose-response gradient.}
80	Ablating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \to 0.639$; Figure~\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\ref{sec:action_trajectory}).
81	
82	\paragraph{Counterfactual instruction analysis.}
83	Replacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\ref{tab:counterfactual}).
84	Token novelty ($1 - \text{Jaccard}$) predicts the ordering ($\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.
85	L1 ablation ($d = 0.65$) falls within this range (Appendix~\ref{sec:action_trajectory}).
86	
87	\begin{table}[t]
88	\centering
89	\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\% vs.\ 100.0\% in Table~\ref{tab:dense_routing_main}): task-level vs.\ LOOCV splits.}
90	\label{tab:routing_gradient}
91	\small
92	\begin{tabular}{lccccc}
93	\toprule
94	Condition & Heads & Text attn & L1 acc & L31 acc & Mode \\
95	\midrule
96	VLA Trained & 24/32 & 57.7\% & 99.6\% & 100.0\% & immed.+stable \\
97	Llama-2 base & 9/32 & 36.5\% & 80.2\% & 100.0\% & gradual+stable \\
98	Untrained & 0/32 & 11.7\% & 100.0\% & 82.0\% & incid.+forget \\
99	\bottomrule
100	\end{tabular}
101	\end{table}
102	
103	\begin{figure}[t]
104	\centering
105	\includegraphics[width=0.75\columnwidth]{figures/fig_32layer_attention.pdf}
106	\caption{Instruction-dominant heads ($>50\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\ref{fig:probe_conditions_appendix}.}
107	\label{fig:attention_profile}
108	\end{figure}
109	
110	%------------------------------------------------------------------
111	\subsection{Non-Monotonic Refinement of Vision Encoder Output}
112	\label{sec:nonmonotonic}
113	
114	\paragraph{Vision encoder provides geometric foundation.}
115	Table~\ref{tab:rsa_overview} reports RSA $\rho$ and probe $R^2$ between representations and actions.
116	DINOv2 \texttt{cls\_token} achieves the highest RSA ($\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\ref{sec:cka_appendix}).
117	
118	\paragraph{Middle-layer peak (metric-dependent).}
119	Under RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\_mean $\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).
120	The readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\Delta = 0.048$ (Table~\ref{tab:rsa_overview}).
121	Under linear CKA, this pattern disappears (monotonic increase; Appendix~\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.
122	
123	\paragraph{Training primarily enhances readout decodability.}
124	Best-vs-best RSA gain is non-significant on LIBERO-Goal ($\Delta\rho = 0.017$, $3\%$, $N{=}10$ tasks; Appendix Table~\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\Delta = +0.023$, $p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}).
125	The $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.
126	Functional improvements are larger: readout $R^2$ $\Delta = +0.069$ ($p < 0.0001$, 95\% CI $[0.047, 0.090]$), image\_mean $\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.
127	
128	\begin{table}[t]
129	\centering
130	\caption{RSA $\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\ref{sec:cka_appendix}). VLA rows: peak values. \textbf{Bold}: best; \underline{underline}: second.}
131	\label{tab:rsa_overview}
132	\small
133	\begin{tabular}{lcccc}
134	\toprule
135	Source & RSA $\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\
136	\midrule
137	DINOv2 cls\_token & \textbf{0.692} & 0.634 & --- & --- \\
138	VLA Trained readout & \underline{0.643} & \textbf{0.678} & L12 & L13 \\
139	Fused DinoSigLIP & 0.634 & --- & --- & --- \\
140	VLA Trained image\_mean & 0.628 & \underline{0.655} & L12 & L8--L10$^\dagger$ \\
141	DinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\
142	VLA Untrained image\_mean & 0.612 & 0.640 & L0 & L0 \\
143	VLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\
144	CLIP ViT-L/14$^\ddagger$ & 0.557 & 0.587 & --- & --- \\
145	\bottomrule
146	\multicolumn{5}{l}{\footnotesize $^\dagger$$R^2$ peak region across 5 seeds ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).} \\
147	\multicolumn{5}{l}{\footnotesize $^\ddagger$RSA uses \texttt{patch\_mean}; $R^2$ uses \texttt{cls\_token} (each encoder's best aggregation).}
148	\end{tabular}
149	\end{table}
150	
151	\begin{figure}[t]
152	\centering
153	\includegraphics[width=0.92\columnwidth]{figures/fig3.pdf}
154	\caption{Per-layer RSA ($\rho$). Trained image\_mean follows an inverted-U (L0 $0.612 \to$ L12 $0.628 \to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}
155	\label{fig:layer_curves}
156	\end{figure}
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "108b30e7-07fb-4fc8-9501-310afa518d11",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each).\nRepresentations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\nThree LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\nRSA computes Spearman $\\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\\S\\ref{sec:rsa}).\nMLP probes (input $\\to$ 256 $\\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\\S\\ref{sec:probes}).\nThis yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\\text{eff} = 10$) and probes use demo-level train/test splits.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\n%------------------------------------------------------------------\n\\subsection{Framework Validation: Token-Level Specialization}\n\\label{sec:token_specialization}\n\nAs a sanity check on the experimental framework, we train cross-instruction probes (\\S\\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.\n\n\\paragraph{Image tokens are instruction-blind (expected).}\nAs predicted by the causal mask and frozen encoder, image\\_mean instruction classification remains at chance ($10\\%$) across all 32 layers in all conditions (Table~\\ref{tab:dense_routing_main}).\nBoth linear and MLP probes corroborate this, as does standalone DINOv2 ($10\\%$; Appendix~\\ref{sec:instruction_invariance_appendix}).\n\n\\paragraph{Readout token as multimodal hub.}\nTrained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.\nThe readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\\ref{sec:dense_routing}). Image\\_mean remains at chance ($10\\%$) in all conditions; trained readout reaches $100\\%$ at L1 and holds; untrained readout decays from L1 to L31.}\n\\label{tab:dense_routing_main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained readout & Untrained readout & Image\\_mean \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL16 & 100.0\\% & 92.3\\% & 10.0\\% \\\\\nL31 & 100.0\\% & 82.0\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}\n\\label{sec:learned_routing}\n\n\\paragraph{Three-level routing gradient at L1.}\nL1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\nPer-token normalization ($38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}) corroborates this redistribution.\n\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\\%--70\\%; Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), sharpening entry-exit routing to entry-only.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}\nBest-vs-best RSA gain is non-significant on LIBERO-Goal ($\\Delta\\rho = 0.017$, $3\\%$, $N{=}10$ tasks; Appendix Table~\\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\\Delta = +0.023$, $p < 0.001$; Appendix~\\ref{sec:cross_benchmark_appendix}).\nThe $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\nFunctional improvements are larger: readout $R^2$ $\\Delta = +0.069$ ($p < 0.0001$, 95\\% CI $[0.047, 0.090]$), image\\_mean $\\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA $\\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix}). VLA rows: peak values. \\textbf{Bold}: best; \\underline{underline}: second.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & RSA $\\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\\\\n\\midrule\nDINOv2 cls\\_token & \\textbf{0.692} & 0.634 & --- & --- \\\\\nVLA Trained readout & \\underline{0.643} & \\textbf{0.678} & L12 & L13 \\\\\nFused DinoSigLIP & 0.634 & --- & --- & --- \\\\\nVLA Trained image\\_mean & 0.628 & \\underline{0.655} & L12 & L8--L10$^\\dagger$ \\\\\nDinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\\\\nVLA Untrained image\\_mean & 0.612 & 0.640 & L0 & L0 \\\\\nVLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\\\\nCLIP ViT-L/14$^\\ddagger$ & 0.557 & 0.587 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$$R^2$ peak region across 5 seeds ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).} \\\\\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$RSA uses \\texttt{patch\\_mean}; $R^2$ uses \\texttt{cls\\_token} (each encoder's best aggregation).}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$). Trained image\\_mean follows an inverted-U (L0 $0.612 \\to$ L12 $0.628 \\to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n",
      "numLines": 157,
      "startLine": 1,
      "totalLines": 157
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_011LATDf6UotXC1x8fRvHEb2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "cce39a39-a79f-4bae-bdbf-2214655fe702",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMkgkujJSNduSmVyjL958M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13405,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13405
      },
      "output_tokens": 26,
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

_source line 11 · 2026-05-19T11:56:48.763Z_

<details><summary>↩ Tool result · `toolu_011LATDf6UotXC1x8fRvHEb2`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
17	
18	\paragraph{Behavioral and mechanistic analysis of VLAs.}
19	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\cite{grant2026,hou2026,fei2025}.
20	At the mechanistic level, H\"aon et al.~\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.
21	Sparse autoencoder studies have uncovered interpretable features and memorized action sequences~\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\cite{lu2025,molinari2025}.
22	Fang et al.~\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.
23	These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.
24	The closest work to ours is Grant et al.~\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.
25	Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
26	
27	\paragraph{Token-level functional specialization in transformers.}
28	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021}, probing reveals increasingly abstract features across depth~\cite{tenney2019}, the logit lens~\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
29	We extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
30	
31	\paragraph{Representation similarity and probing methodology.}
32	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
33	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
34	We adopt RSA and MLP probes, with CKA in the appendix.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "e78a5b05-3db5-44f4-a36f-f8cb196f98d7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01DB7PQkjiPTD4kLRF6JUpGb`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "af5c7652-6361-429e-b856-244c9d321f5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMkgkujJSNduSmVyjL958M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13405,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13405
      },
      "output_tokens": 26,
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

_source line 13 · 2026-05-19T11:56:49.331Z_

<details><summary>↩ Tool result · `toolu_01DB7PQkjiPTD4kLRF6JUpGb`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "8ef42959-2452-4945-8464-c6fc40e79720",
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01RQt1cX3jF6UTpGVWF884fm`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "26b0c220-6e39-463f-911c-11d967e5012c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMkgkujJSNduSmVyjL958M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13405,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13405
      },
      "output_tokens": 26,
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

_source line 15 · 2026-05-19T11:56:49.856Z_

<details><summary>↩ Tool result · `toolu_01RQt1cX3jF6UTpGVWF884fm`</summary>

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
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter},
38	  journal   = {Frontiers in Systems Neuroscience},
39	  volume    = {2},
40	  pages     = {4},
41	  year      = {2008},
42	  publisher = {Frontiers},
43	}
44	
45	@inproceedings{kornblith2019,
46	  title     = {Similarity of Neural Network Representations Revisited},
47	  author    = {Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},
48	  booktitle = {International Conference on Machine Learning (ICML)},
49	  year      = {2019},
50	}
51	
52	@inproceedings{alain2017,
53	  title     = {Understanding Intermediate Layers Using Linear Classifier Probes},
54	  author    = {Alain, Guillaume and Bengio, Yoshua},
55	  booktitle = {International Conference on Learning Representations (ICLR), Workshop Track},
56	  year      = {2017},
57	}
58	
59	% === Vision Encoders ===
60	
61	@inproceedings{zhai2023_siglip,
62	  title     = {Sigmoid Loss for Language Image Pre-Training},
63	  author    = {Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
64	  booktitle = {International Conference on Computer Vision (ICCV)},
65	  year      = {2023},
66	}
67	
68	@article{oquab2024_dinov2,
69	  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},
70	  author    = {Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and Vo, Huy and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and others},
71	  journal   = {Transactions on Machine Learning Research (TMLR)},
72	  year      = {2024},
73	}
74	
75	@inproceedings{radford2021_clip,
76	  title     = {Learning Transferable Visual Models From Natural Language Supervision},
77	  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},
78	  booktitle = {International Conference on Machine Learning (ICML)},
79	  year      = {2021},
80	}
81	
82	% === Domain-Specific ===
83	
84	@article{grant2026,
85	  title     = {Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models},
86	  author    = {Grant, Bryce and Zhao, Xijia and Wang, Peng},
87	  journal   = {arXiv preprint arXiv:2603.19233},
88	  year      = {2026},
89	}
90	
91	@article{haon2025,
92	  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},
93	  author    = {H{\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},
94	  journal   = {arXiv preprint arXiv:2509.00328},
95	  year      = {2025},
96	}
97	
98	% === Behavioral Analysis of VLAs ===
99	
100	@article{hou2026,
101	  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},
102	  author    = {Hou, Yuchen and Zhao, Lin},
103	  journal   = {arXiv preprint arXiv:2603.00592},
104	  year      = {2026},
105	}
106	
107	@article{fei2025,
108	  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},
109	  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},
110	  journal   = {arXiv preprint arXiv:2510.13626},
111	  year      = {2025},
112	}
113	
114	% === Mechanistic Interpretability of VLAs ===
115	
116	@article{swann2026,
117	  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},
118	  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},
119	  journal   = {arXiv preprint arXiv:2603.19183},
120	  year      = {2026},
121	}
122	
123	@article{buurmeijer2026,
124	  title     = {Observing and Controlling Features in Vision-Language-Action Models},
125	  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},
126	  journal   = {arXiv preprint arXiv:2603.05487},
127	  year      = {2026},
128	}
129	
130	@article{lu2025,
131	  title     = {Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture},
132	  author    = {Lu, Hong and Li, Hengxu and Shahani, Prithviraj Singh and Herbers, Stephanie and Scheutz, Matthias},
133	  journal   = {arXiv preprint arXiv:2502.04558},
134	  year      = {2025},
135	}
136	
137	@article{molinari2025,
138	  title     = {Emergent World Representations in {OpenVLA}},
139	  author    = {Molinari, Marco and Nevali, Leonardo and Navani, Saharsha and Younis, Omar G.},
140	  journal   = {arXiv preprint arXiv:2509.24559},
141	  year      = {2025},
142	}
143	
144	% === Probing Methods ===
145	
146	@article{belinkov2022,
147	  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},
148	  author    = {Belinkov, Yonatan},
149	  journal   = {Computational Linguistics},
150	  volume    = {48},
151	  number    = {1},
152	  pages     = {207--219},
153	  year      = {2022},
154	}
155	
156	% === Causal Tracing and Per-Layer Analysis ===
157	
158	@inproceedings{meng2022_rome,
159	  title     = {Locating and Editing Factual Associations in {GPT}},
160	  author    = {Meng, Kevin and Bau, David and Andonian, Alex and Belinkov, Yonatan},
161	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
162	  year      = {2022},
163	}
164	
165	@article{belrose2023_tunedlens,
166	  title     = {Eliciting Latent Predictions from Transformers with the Tuned Lens},
167	  author    = {Belrose, Nora and Furman, Zach and Smith, Logan and Biderman, Stella and Steinhardt, Jacob and Frankle, Jonathan},
168	  journal   = {arXiv preprint arXiv:2303.08112},
169	  year      = {2023},
170	}
171	
172	% === Mechanistic Interpretability in Transformers ===
173	
174	@article{elhage2021,
175	  title     = {A Mathematical Framework for Transformer Circuits},
176	  author    = {Elhage, Nelson and Nanda, Neel and Olsson, Catherine and Henighan, Tom and Joseph, Nicholas and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and DasSarma, Nova and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},
177	  journal   = {Transformer Circuits Thread},
178	  year      = {2021},
179	  url       = {https://transformer-circuits.pub/2021/framework/index.html},
180	}
181	
182	@article{olsson2022,
183	  title     = {In-context Learning and Induction Heads},
184	  author    = {Olsson, Catherine and Elhage, Nelson and Nanda, Neel and Joseph, Nicholas and DasSarma, Nova and Henighan, Tom and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Johnston, Scott and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},
185	  journal   = {arXiv preprint arXiv:2209.11895},
186	  year      = {2022},
187	}
188	
189	@inproceedings{wang2023_ioi,
190	  title     = {Interpretability in the Wild: a Circuit for Indirect Object Identification in {GPT-2} Small},
191	  author    = {Wang, Kevin and Variengien, Alexandre and Conmy, Arthur and Shlegeris, Buck and Steinhardt, Jacob},
192	  booktitle = {International Conference on Learning Representations (ICLR)},
193	  year      = {2023},
194	}
195	
196	@inproceedings{conmy2023,
197	  title     = {Towards Automated Circuit Discovery for Mechanistic Interpretability},
198	  author    = {Conmy, Arthur and Mavor-Parker, Augustine N. and Lynch, Aengus and Heimersheim, Stefan and Garriga-Alonso, Adri{\`a}},
199	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
200	  year      = {2023},
201	}
202	
203	% === Attention Analysis ===
204	
205	@inproceedings{clark2019,
206	  title     = {What Does {BERT} Look At? {An} Analysis of {BERT}'s Attention},
207	  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},
208	  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},
209	  year      = {2019},
210	}
211	
212	@inproceedings{vig2019,
213	  title     = {Analyzing the Structure of Attention in a Transformer Language Model},
214	  author    = {Vig, Jesse and Belinkov, Yonatan},
215	  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},
216	  year      = {2019},
217	}
218	
219	@inproceedings{voita2019,
220	  title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
221	  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},
222	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
223	  year      = {2019},
224	}
225	
226	% === Token-Level Functional Specialization ===
227	
228	@inproceedings{dosovitskiy2021,
229	  title     = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},
230	  author    = {Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},
231	  booktitle = {International Conference on Learning Representations (ICLR)},
232	  year      = {2021},
233	}
234	
235	@inproceedings{darcet2024,
236	  title     = {Vision Transformers Need Registers},
237	  author    = {Darcet, Timoth{\'e}e and Oquab, Maxime and Mairal, Julien and Bojanowski, Piotr},
238	  booktitle = {International Conference on Learning Representations (ICLR)},
239	  year      = {2024},
240	}
241	
242	@inproceedings{geva2021,
243	  title     = {Transformer Feed-Forward Layers Are Key-Value Memories},
244	  author    = {Geva, Mor and Schuster, Roei and Berant, Jonathan and Levy, Omer},
245	  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
246	  year      = {2021},
247	}
248	
249	@inproceedings{tenney2019,
250	  title     = {{BERT} Rediscovers the Classical {NLP} Pipeline},
251	  author    = {Tenney, Ian and Das, Dipanjan and Pavlick, Ellie},
252	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},
253	  year      = {2019},
254	}
255	
256	% === Representation Similarity Methods ===
257	
258	@inproceedings{raghu2017,
259	  title     = {{SVCCA}: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability},
260	  author    = {Raghu, Maithra and Gilmer, Justin and Yosinski, Jason and Sohl-Dickstein, Jascha},
261	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
262	  year      = {2017},
263	}
264	
265	@inproceedings{morcos2018,
266	  title     = {Insights on Representational Similarity in Neural Networks with Canonical Correlation},
267	  author    = {Morcos, Ari S. and Raghu, Maithra and Bengio, Samy},
268	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
269	  year      = {2018},
270	}
271	
272	@inproceedings{hewitt2019,
273	  title     = {A Structural Probe for Finding Syntax in Word Representations},
274	  author    = {Hewitt, John and Manning, Christopher D.},
275	  booktitle = {Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics (NAACL)},
276	  year      = {2019},
277	}
278	
279	% === VLM Token-Level Analysis ===
280	
281	@inproceedings{neo2025,
282	  title     = {Towards Understanding Multi-Task Learning (Generalization) of {LLMs} via Detecting and Exploring Task-Specific Neurons},
283	  author    = {Neo, Yifan and Wu, Jingcheng and Hooi, Bryan},
284	  booktitle = {International Conference on Learning Representations (ICLR)},
285	  year      = {2025},
286	}
287	
288	% === Representation Similarity (ViT) ===
289	
290	@inproceedings{raghu2021,
291	  title     = {Do Vision Transformers See Like Convolutional Neural Networks?},
292	  author    = {Raghu, Maithra and Unterthiner, Thomas and Kornblith, Simon and Zhang, Chiyuan and Dosovitskiy, Alexey},
293	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
294	  year      = {2021},
295	}
296	
297	% === Probe Methodology ===
298	
299	@inproceedings{hewitt2019control,
300	  title     = {Designing and Interpreting Probes with Control Tasks},
301	  author    = {Hewitt, John and Liang, Percy},
302	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
303	  pages     = {2733--2743},
304	  year      = {2019},
305	  doi       = {10.18653/v1/D19-1275},
306	}
307	
308	% === RSA Toolbox ===
309	
310	@article{nili2014toolbox,
311	  title     = {A Toolbox for Representational Similarity Analysis},
312	  author    = {Nili, Hamed and Wingfield, Cai and Walther, Alexander and Su, Li and Marslen-Wilson, William and Kriegeskorte, Nikolaus},
313	  journal   = {PLoS Computational Biology},
314	  volume    = {10},
315	  number    = {4},
316	  pages     = {e1003553},
317	  year      = {2014},
318	  doi       = {10.1371/journal.pcbi.1003553},
319	}
320	
321	% === Mechanistic Interpretability ===
322	
323	@misc{bills2023language,
324	  title     = {Language Models Can Explain Neurons in Language Models},
325	  author    = {Bills, Steven and Cammarata, Nick and Mossing, Dan and Tillman, Henk and Gao, Leo and Goh, Gabriel and Sutskever, Ilya and Leike, Jan and Wu, Jeff and Saunders, William},
326	  year      = {2023},
327	  howpublished = {OpenAI Blog},
328	  url       = {https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html},
329	}
330	
331	@article{templeton2024scaling,
332	  title     = {Scaling Monosemanticity: Extracting Interpretable Features from {C}laude 3 {S}onnet},
333	  author    = {Templeton, Adly and Conerly, Tom and Marcus, Jonathan and Lindsey, Jack and Bricken, Trenton and Chen, Brian and Pearce, Adam and Citro, Craig and Ameisen, Emmanuel and Jones, Andy and others},
334	  journal   = {Transformer Circuits Thread},
335	  year      = {2024},
336	  url       = {https://transformer-circuits.pub/2024/scaling-monosemanticity/},
337	}
338	
339	% === LLM Internal Probing ===
340	
341	@misc{nostalgebraist2020,
342	  title     = {interpreting {GPT}: the logit lens},
343	  author    = {nostalgebraist},
344	  year      = {2020},
345	  howpublished = {LessWrong blog post},
346	  url       = {https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens},
347	  note      = {Accessed: 2026-05-19},
348	}
349	
350	% === VLA Fine-tuning and Reasoning ===
351	
352	@article{fang2025,
353	  title     = {{DualVLA}: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action},
354	  author    = {Fang, Zhen and Liu, Zhuoyang and Liu, Jiaming and Chen, Hao and Zeng, Yu and Huang, Shiting and Chen, Zehui and Chen, Lin and Zhang, Shanghang and Zhao, Feng},
355	  journal   = {arXiv preprint arXiv:2511.22134},
356	  year      = {2025},
357	}
358	
359	% === LLM Backbone ===
360	
361	@article{touvron2023_llama2,
362	  title     = {{Llama} 2: Open Foundation and Fine-Tuned Chat Models},
363	  author    = {Touvron, Hugo and Martin, Louis and Stone, Kevin and Albert, Peter and Almahairi, Amjad and Babaei, Yasmine and Bashlykov, Nikolay and Batra, Soumya and Bhargava, Prajjwal and Bhosale, Shruti and others},
364	  journal   = {arXiv preprint arXiv:2307.09288},
365	  year      = {2023},
366	}
367	
368	% === Dataset ===
369	
370	@article{padalkar2023_oxe,
371	  title     = {Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},
372	  author    = {Padalkar, Abhishek and Poolber, Acorn and Bewley, Ajinkya and others},
373	  journal   = {arXiv preprint arXiv:2310.08864},
374	  year      = {2023},
375	}
376	
377	% === VLA Foundation Models ===
378	
379	@article{black2024_pi0,
380	  title     = {$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
381	  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and Jakubczak, Szymon and Jones, Tim and Ke, Liyiming and Levine, Sergey and Li-Bell, Adrian and Mothukuri, Mohith and Nair, Suraj and Pertsch, Karl and Shi, Lucy Xiaoyang and Tanner, James and Vuong, Quan and Walling, Anna and Wang, Haohuan and Zhilinsky, Ury},
382	  journal   = {arXiv preprint arXiv:2410.24164},
383	  year      = {2024},
384	}
385	
386	@inproceedings{ghosh2024_octo,
387	  title     = {Octo: An Open-Source Generalist Robot Policy},
388	  author    = {Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and Mees, Oier and Dasari, Sudeep and Hejna, Joey and Kreiman, Tobias and Xu, Charles and You, Jianlan and Wu, Joey and Finn, Chelsea and Kumar, Aviral and Hausman, Karol and Levine, Sergey},
389	  booktitle = {Robotics: Science and Systems},
390	  year      = {2024},
391	}
392	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "473f38e5-6870-44fa-80fa-e9e3bf48177e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
      "content": "% === VLA / Architecture ===\n\n@article{kim2024_openvla,\n  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},\n  journal   = {arXiv preprint arXiv:2406.09246},\n  year      = {2024},\n}\n\n@article{karamcheti2024,\n  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},\n  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},\n  journal   = {arXiv preprint arXiv:2402.07865},\n  year      = {2024},\n}\n\n@article{brohan2023_rt2,\n  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  journal   = {arXiv preprint arXiv:2307.15818},\n  year      = {2023},\n}\n\n% === Benchmark ===\n\n@inproceedings{liu2023_libero,\n  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Representation Analysis Methods ===\n\n@article{kriegeskorte2008,\n  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},\n  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter},\n  journal   = {Frontiers in Systems Neuroscience},\n  volume    = {2},\n  pages     = {4},\n  year      = {2008},\n  publisher = {Frontiers},\n}\n\n@inproceedings{kornblith2019,\n  title     = {Similarity of Neural Network Representations Revisited},\n  author    = {Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2019},\n}\n\n@inproceedings{alain2017,\n  title     = {Understanding Intermediate Layers Using Linear Classifier Probes},\n  author    = {Alain, Guillaume and Bengio, Yoshua},\n  booktitle = {International Conference on Learning Representations (ICLR), Workshop Track},\n  year      = {2017},\n}\n\n% === Vision Encoders ===\n\n@inproceedings{zhai2023_siglip,\n  title     = {Sigmoid Loss for Language Image Pre-Training},\n  author    = {Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle = {International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n}\n\n@article{oquab2024_dinov2,\n  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},\n  author    = {Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and Vo, Huy and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and others},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2024},\n}\n\n@inproceedings{radford2021_clip,\n  title     = {Learning Transferable Visual Models From Natural Language Supervision},\n  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2021},\n}\n\n% === Domain-Specific ===\n\n@article{grant2026,\n  title     = {Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models},\n  author    = {Grant, Bryce and Zhao, Xijia and Wang, Peng},\n  journal   = {arXiv preprint arXiv:2603.19233},\n  year      = {2026},\n}\n\n@article{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {H{\\\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},\n  journal   = {arXiv preprint arXiv:2509.00328},\n  year      = {2025},\n}\n\n% === Behavioral Analysis of VLAs ===\n\n@article{hou2026,\n  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},\n  author    = {Hou, Yuchen and Zhao, Lin},\n  journal   = {arXiv preprint arXiv:2603.00592},\n  year      = {2026},\n}\n\n@article{fei2025,\n  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},\n  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},\n  journal   = {arXiv preprint arXiv:2510.13626},\n  year      = {2025},\n}\n\n% === Mechanistic Interpretability of VLAs ===\n\n@article{swann2026,\n  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},\n  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},\n  journal   = {arXiv preprint arXiv:2603.19183},\n  year      = {2026},\n}\n\n@article{buurmeijer2026,\n  title     = {Observing and Controlling Features in Vision-Language-Action Models},\n  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},\n  journal   = {arXiv preprint arXiv:2603.05487},\n  year      = {2026},\n}\n\n@article{lu2025,\n  title     = {Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture},\n  author    = {Lu, Hong and Li, Hengxu and Shahani, Prithviraj Singh and Herbers, Stephanie and Scheutz, Matthias},\n  journal   = {arXiv preprint arXiv:2502.04558},\n  year      = {2025},\n}\n\n@article{molinari2025,\n  title     = {Emergent World Representations in {OpenVLA}},\n  author    = {Molinari, Marco and Nevali, Leonardo and Navani, Saharsha and Younis, Omar G.},\n  journal   = {arXiv preprint arXiv:2509.24559},\n  year      = {2025},\n}\n\n% === Probing Methods ===\n\n@article{belinkov2022,\n  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},\n  author    = {Belinkov, Yonatan},\n  journal   = {Computational Linguistics},\n  volume    = {48},\n  number    = {1},\n  pages     = {207--219},\n  year      = {2022},\n}\n\n% === Causal Tracing and Per-Layer Analysis ===\n\n@inproceedings{meng2022_rome,\n  title     = {Locating and Editing Factual Associations in {GPT}},\n  author    = {Meng, Kevin and Bau, David and Andonian, Alex and Belinkov, Yonatan},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2022},\n}\n\n@article{belrose2023_tunedlens,\n  title     = {Eliciting Latent Predictions from Transformers with the Tuned Lens},\n  author    = {Belrose, Nora and Furman, Zach and Smith, Logan and Biderman, Stella and Steinhardt, Jacob and Frankle, Jonathan},\n  journal   = {arXiv preprint arXiv:2303.08112},\n  year      = {2023},\n}\n\n% === Mechanistic Interpretability in Transformers ===\n\n@article{elhage2021,\n  title     = {A Mathematical Framework for Transformer Circuits},\n  author    = {Elhage, Nelson and Nanda, Neel and Olsson, Catherine and Henighan, Tom and Joseph, Nicholas and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and DasSarma, Nova and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},\n  journal   = {Transformer Circuits Thread},\n  year      = {2021},\n  url       = {https://transformer-circuits.pub/2021/framework/index.html},\n}\n\n@article{olsson2022,\n  title     = {In-context Learning and Induction Heads},\n  author    = {Olsson, Catherine and Elhage, Nelson and Nanda, Neel and Joseph, Nicholas and DasSarma, Nova and Henighan, Tom and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Johnston, Scott and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},\n  journal   = {arXiv preprint arXiv:2209.11895},\n  year      = {2022},\n}\n\n@inproceedings{wang2023_ioi,\n  title     = {Interpretability in the Wild: a Circuit for Indirect Object Identification in {GPT-2} Small},\n  author    = {Wang, Kevin and Variengien, Alexandre and Conmy, Arthur and Shlegeris, Buck and Steinhardt, Jacob},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2023},\n}\n\n@inproceedings{conmy2023,\n  title     = {Towards Automated Circuit Discovery for Mechanistic Interpretability},\n  author    = {Conmy, Arthur and Mavor-Parker, Augustine N. and Lynch, Aengus and Heimersheim, Stefan and Garriga-Alonso, Adri{\\`a}},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Attention Analysis ===\n\n@inproceedings{clark2019,\n  title     = {What Does {BERT} Look At? {An} Analysis of {BERT}'s Attention},\n  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},\n  year      = {2019},\n}\n\n@inproceedings{vig2019,\n  title     = {Analyzing the Structure of Attention in a Transformer Language Model},\n  author    = {Vig, Jesse and Belinkov, Yonatan},\n  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},\n  year      = {2019},\n}\n\n@inproceedings{voita2019,\n  title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n}\n\n% === Token-Level Functional Specialization ===\n\n@inproceedings{dosovitskiy2021,\n  title     = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},\n  author    = {Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n}\n\n@inproceedings{darcet2024,\n  title     = {Vision Transformers Need Registers},\n  author    = {Darcet, Timoth{\\'e}e and Oquab, Maxime and Mairal, Julien and Bojanowski, Piotr},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n}\n\n@inproceedings{geva2021,\n  title     = {Transformer Feed-Forward Layers Are Key-Value Memories},\n  author    = {Geva, Mor and Schuster, Roei and Berant, Jonathan and Levy, Omer},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2021},\n}\n\n@inproceedings{tenney2019,\n  title     = {{BERT} Rediscovers the Classical {NLP} Pipeline},\n  author    = {Tenney, Ian and Das, Dipanjan and Pavlick, Ellie},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n}\n\n% === Representation Similarity Methods ===\n\n@inproceedings{raghu2017,\n  title     = {{SVCCA}: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability},\n  author    = {Raghu, Maithra and Gilmer, Justin and Yosinski, Jason and Sohl-Dickstein, Jascha},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2017},\n}\n\n@inproceedings{morcos2018,\n  title     = {Insights on Representational Similarity in Neural Networks with Canonical Correlation},\n  author    = {Morcos, Ari S. and Raghu, Maithra and Bengio, Samy},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2018},\n}\n\n@inproceedings{hewitt2019,\n  title     = {A Structural Probe for Finding Syntax in Word Representations},\n  author    = {Hewitt, John and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2019},\n}\n\n% === VLM Token-Level Analysis ===\n\n@inproceedings{neo2025,\n  title     = {Towards Understanding Multi-Task Learning (Generalization) of {LLMs} via Detecting and Exploring Task-Specific Neurons},\n  author    = {Neo, Yifan and Wu, Jingcheng and Hooi, Bryan},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n}\n\n% === Representation Similarity (ViT) ===\n\n@inproceedings{raghu2021,\n  title     = {Do Vision Transformers See Like Convolutional Neural Networks?},\n  author    = {Raghu, Maithra and Unterthiner, Thomas and Kornblith, Simon and Zhang, Chiyuan and Dosovitskiy, Alexey},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2021},\n}\n\n% === Probe Methodology ===\n\n@inproceedings{hewitt2019control,\n  title     = {Designing and Interpreting Probes with Control Tasks},\n  author    = {Hewitt, John and Liang, Percy},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages     = {2733--2743},\n  year      = {2019},\n  doi       = {10.18653/v1/D19-1275},\n}\n\n% === RSA Toolbox ===\n\n@article{nili2014toolbox,\n  title     = {A Toolbox for Representational Similarity Analysis},\n  author    = {Nili, Hamed and Wingfield, Cai and Walther, Alexander and Su, Li and Marslen-Wilson, William and Kriegeskorte, Nikolaus},\n  journal   = {PLoS Computational Biology},\n  volume    = {10},\n  number    = {4},\n  pages     = {e1003553},\n  year      = {2014},\n  doi       = {10.1371/journal.pcbi.1003553},\n}\n\n% === Mechanistic Interpretability ===\n\n@misc{bills2023language,\n  title     = {Language Models Can Explain Neurons in Language Models},\n  author    = {Bills, Steven and Cammarata, Nick and Mossing, Dan and Tillman, Henk and Gao, Leo and Goh, Gabriel and Sutskever, Ilya and Leike, Jan and Wu, Jeff and Saunders, William},\n  year      = {2023},\n  howpublished = {OpenAI Blog},\n  url       = {https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html},\n}\n\n@article{templeton2024scaling,\n  title     = {Scaling Monosemanticity: Extracting Interpretable Features from {C}laude 3 {S}onnet},\n  author    = {Templeton, Adly and Conerly, Tom and Marcus, Jonathan and Lindsey, Jack and Bricken, Trenton and Chen, Brian and Pearce, Adam and Citro, Craig and Ameisen, Emmanuel and Jones, Andy and others},\n  journal   = {Transformer Circuits Thread},\n  year      = {2024},\n  url       = {https://transformer-circuits.pub/2024/scaling-monosemanticity/},\n}\n\n% === LLM Internal Probing ===\n\n@misc{nostalgebraist2020,\n  title     = {interpreting {GPT}: the logit lens},\n  author    = {nostalgebraist},\n  year      = {2020},\n  howpublished = {LessWrong blog post},\n  url       = {https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens},\n  note      = {Accessed: 2026-05-19},\n}\n\n% === VLA Fine-tuning and Reasoning ===\n\n@article{fang2025,\n  title     = {{DualVLA}: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action},\n  author    = {Fang, Zhen and Liu, Zhuoyang and Liu, Jiaming and Chen, Hao and Zeng, Yu and Huang, Shiting and Chen, Zehui and Chen, Lin and Zhang, Shanghang and Zhao, Feng},\n  journal   = {arXiv preprint arXiv:2511.22134},\n  year      = {2025},\n}\n\n% === LLM Backbone ===\n\n@article{touvron2023_llama2,\n  title     = {{Llama} 2: Open Foundation and Fine-Tuned Chat Models},\n  author    = {Touvron, Hugo and Martin, Louis and Stone, Kevin and Albert, Peter and Almahairi, Amjad and Babaei, Yasmine and Bashlykov, Nikolay and Batra, Soumya and Bhargava, Prajjwal and Bhosale, Shruti and others},\n  journal   = {arXiv preprint arXiv:2307.09288},\n  year      = {2023},\n}\n\n% === Dataset ===\n\n@article{padalkar2023_oxe,\n  title     = {Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author    = {Padalkar, Abhishek and Poolber, Acorn and Bewley, Ajinkya and others},\n  journal   = {arXiv preprint arXiv:2310.08864},\n  year      = {2023},\n}\n\n% === VLA Foundation Models ===\n\n@article{black2024_pi0,\n  title     = {$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and Jakubczak, Szymon and Jones, Tim and Ke, Liyiming and Levine, Sergey and Li-Bell, Adrian and Mothukuri, Mohith and Nair, Suraj and Pertsch, Karl and Shi, Lucy Xiaoyang and Tanner, James and Vuong, Quan and Walling, Anna and Wang, Haohuan and Zhilinsky, Ury},\n  journal   = {arXiv preprint arXiv:2410.24164},\n  year      = {2024},\n}\n\n@inproceedings{ghosh2024_octo,\n  title     = {Octo: An Open-Source Generalist Robot Policy},\n  author    = {Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and Mees, Oier and Dasari, Sudeep and Hejna, Joey and Kreiman, Tobias and Xu, Charles and You, Jianlan and Wu, Joey and Finn, Chelsea and Kumar, Aviral and Hausman, Karol and Levine, Sergey},\n  booktitle = {Robotics: Science and Systems},\n  year      = {2024},\n}\n",
      "numLines": 392,
      "startLine": 1,
      "totalLines": 392
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Glob · `toolu_01TjLpwtDTtWAc8yS9ZkRsxj`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "81a53ee7-130b-4242-a98e-cc6b60f69fe2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PMkgkujJSNduSmVyjL958M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13405,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13405
      },
      "output_tokens": 26,
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

_source line 17 · 2026-05-19T11:56:50.287Z_

<details><summary>↩ Tool result · `toolu_01TjLpwtDTtWAc8yS9ZkRsxj`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "63b722d8-e417-49c3-b62b-edb8c833728b",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T222933/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T222933/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T011810/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T011810/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T011810/worst/paper_framing.md",
      "paper_framing.md"
    ],
    "durationMs": 30,
    "numFiles": 7,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files. Let me also check for an appendix.tex file and the paper_framing.md file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "3c406c9f-002e-4d35-88ed-cb6fc9a5f696",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bm2e2BSb9imX69RspDsR3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16429,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16429
      },
      "output_tokens": 8,
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

### Assistant

_source line 19_

Now let me read the appendix and paper_framing.md files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "2ed4573a-df72-4188-894b-f306311b30a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bm2e2BSb9imX69RspDsR3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16429,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16429
      },
      "output_tokens": 8,
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

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_015oS7kg7kW8z4J6qYgE68Qp`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "41435d56-85f9-42c3-90df-a5e930dba881",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bm2e2BSb9imX69RspDsR3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16429,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16429
      },
      "output_tokens": 8,
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

_source line 21 · 2026-05-19T11:56:55.919Z_

<details><summary>↩ Tool result · `toolu_015oS7kg7kW8z4J6qYgE68Qp`</summary>

```text
1	# Paper Framing — vla-ssd (Plan B → D060 Reframe)
2	
3	> D048: PI 批准按最大质量重构。A+ 版本保留为 fallback (branch paper-a-plus-backup)。
4	> D060: Round 4 weak reject → C1 降为框架, C2 升为唯一核心 claim, C3 降为 qualified observation。
5	
6	## Target Venue
7	- Primary: CoRL 2026
8	- Deadline: Abstract May 26, Paper May 29
9	- Format: 8 pages + references
10	
11	## Core Insight
12	
13	VLA fine-tuning 的核心贡献是学习 deliberate instruction routing：将 instruction attention 从语言预训练的中层模式（L9-L16）reorganize 到 entry-exit 模式（L0-L1 + L31），实现即时 instruction access。这个三条件梯度（untrained 0/32 → pretrained 9/32 → trained 25/32）是 genuine empirical finding，具有 causal evidence 支撑。Token-level specialization（image-blind, readout-hub）是 causal mask 架构保证的性质，我们通过系统实验 verify 和 quantify 其在实际 VLA 中的表现。
14	
15	## Core Claims (D060 重构：1 核心 + 1 框架 + 1 观察)
16	
17	### C1: Experimental Framework + Architecture-Verified Specialization [方法论贡献，非 empirical finding]
18	**重新定位（D060）**: Token-level specialization 是 causal mask 的数学必然（image tokens 在序列中先于 instruction tokens，无法 attend to instructions）+ frozen encoder 不接收 instruction input。论文贡献不是"发现"这一点，而是：
19	- **(a) 系统实验框架**：factorial design (trained/pretrained/untrained × instruction presence) + 四种互补分析方法（cross-instruction probe + attention + RSA + MLP probe），适用于任何 decoder-only VLA
20	- **(b) 量化验证**：即使 residual stream 理论上可以 leak information，image tokens 在实际模型的全部 32 层均保持 chance（10%）。这不是 trivial——frozen encoder 权重与 LLM 权重共享 residual stream，验证了 no leakage
21	- **(c) 训练差异的量化**：untrained readout L1=100% 但 L31=82%（信号衰减）vs trained 100% 全程稳定——framework 揭示了训练影响 routing robustness 而非 routing existence
22	
23	Key evidence (unchanged):
24	- Cross-instruction probe: same frame × 10 instructions → 10-way classification
25	- Dense L0-L32: image_mean = chance at ALL layers
26	- LOOCV: 100%±0.00 trained, decaying untrained
27	- **承认**: 10-way classification 本身 trivially easy（untrained L1 也 100%），贡献在于 framework + 三条件对比揭示的 routing 差异
28	
29	### C2: Three Qualitatively Different Routing Strategies — VLA Fine-tuning Achieves Immediate Dedicated Routing
30	三条件揭示三种定性不同的 routing 模式：
31	
32	**L1 Attention Routing (heads + attention fraction):**
33	- **Untrained (random init)**: 0/32 heads, 12% text attention
34	- **Llama-2 base (pretrained, no VLA)**: 9/32 heads, 36.5% text attention
35	- **VLA Trained**: 25/32 heads, 58% text attention
36	
37	**Full-Layer Probe Profile (instruction classification accuracy):**
38	- **Trained**: L1=99.6% → 全程 100% — "即时路由 + 完全稳定"
39	- **Llama-2 base**: L1=80.2% → L2=98.7% → L5+=100% — "渐进建立 + 稳定维持"
40	- **Untrained**: L1=100% → L8=98.6% → L31=82% — "偶然路由 + 逐渐遗忘"
41	
42	**VLA Fine-tuning 的独特贡献（精��化）：**
43	1. **即时性**：L1 即达 99.6%（vs pretrained 需 5 层才饱和）
44	2. **头数专用化**：25/32 heads instruction-dominant（vs pretrained 9/32）
45	3. **不是**深层稳定性 — 稳定性来自 pretrained weights（pretrained 也不衰减）
46	
47	**深层���减只发生在 random init**：说明结构化的 pretrained 表示（无论是否经过 VLA 训练）都能维持 instruction signal；random weights 的噪声累积导致信号退化。
48	
49	**Full 32-Layer Attention Profile（D054 升级，dense evidence）：**
50	- **Untrained**: 全 32 层 × 所有 head = 0 instruction-dominant。完全无语言处理能力。
51	- **Llama-2 base**: 倒U型 — L0-L4 低(0-10 heads) → L9-L16 高峰(15-22 heads) → L31 回落(8)。经典 LM pattern：中层做深度语义处理。
52	- **VLA Trained**: 书挡型 — L0-L1 高峰(21-24 heads) → L2-L30 低谷(0-11) → L31 再次高峰(18)。入口获取 instruction + 出口条件化 action output。
53	
54	**C2 Claim（D073 reframe: open-loop functional sensitivity）**: VLA fine-tuning **shifts** instruction attention from mid-layer processing (Llama-2 base: 15-22/32 heads at L10-L17) to entry-layer routing (L0-L1: 21-24/32) and exit-layer re-engagement (L31: 18/32)。Instruction-conditioned action generation operates through **distributed L1 routing** where instruction-attention fraction predicts per-head contribution magnitude (specificity ratio 1.08x at action output)。Routing modulates output direction (d=0.65) without systematic quality degradation (ΔMSE≈0), consistent with an information-computation dissociation (Hewitt & Liang 2019)。不能 claim instruction heads "uniquely responsible" 或 "confirms routing function"——用 "open-loop functional sensitivity" + "support" 而非 "confirm"。可 claim "disproportionate contribution" + "attention-ordered routing"。Section 标题用 "Open-loop functional sensitivity"，正文用 "shifts...from...to..." + "distributed routing"。
55	
56	Key evidence:
57	- **32-layer dense attention profile**: Trained bookend (L0-1: 21-24, L31: 18) vs Llama2base inverted-U (L9-16: 15-22)
58	- Three-condition full-layer probe: trained flat 100%; llama2base saturates L5+100%; untrained decays L1:100%→L31:82%
59	- L1 attention gradient: 0/32 → 9/32 → 25/32 heads
60	- VLA-specific contributions: (1) temporal reorganization from mid-peak to bookend, (2) immediacy (L1: 80.2→99.6%), (3) head dedication (9→25 at L1)
61	- **Per-token normalization**: 38.2x text/image ratio (trained instr-dom) vs 1.5x (untrained) — eliminates token-count confound
62	- **Trajectory-level d**: all conditions d>2.0 (token-level is conservative ~4x underestimate)
63	- **GT error**: ΔMSE≈0 (ablation redirects outputs without degrading GT accuracy) — supports information-computation dissociation
64	- **Token overlap**: Spearman ρ=1.0 between token novelty and d — lexical/positional sensitivity, not semantic distance
65	- **LOO sensitivity**: all leave-one-out p ≤ 0.083, no qualitative reversal; cream cheese reclassification p=0.008
66	- **4-condition training trajectory (D075)**: untrained(0) → llama2(9) → bridge-vla(24) → libero-finetuned(22) at L1。Entry routing 稳定，但 L31 exit engagement 18→0（entry-exit → entry-only sharpening）。Probe accuracy 不变（L31 仍 100%），确认 attention-representation dissociation
67	- **OXE training diversity**: openvla-7b 在 Open X-Embodiment 970K episodes（多平台多任务）上训练，L1 routing 不是 LIBERO-specific
68	
69	### C3: Vision Encoder Geometry Observation [降为 qualified observation，非 core claim]
70	**重新定位（D060）**: RSA inverted-U 的 rise phase 极小（Δρ=0.016, CI 待补），CKA 完全反转 RSA ordering（untrained > trained > DINOv2），"non-monotonic refinement" 仅在 RSA 下成立。DINOv2 ranking 在 CKA 下不成立（CKA 中 DINOv2 排名最低）。
71	
72	**保留为 observation 的理由**：
73	- **Decline phase 也是 RSA-specific**：L12→L32 Δρ=-0.206 远大于 rise phase，但 CKA 单调递增无 decline。不能 claim decline 是 metric-robust。
74	- **R² inverted-U 是 metric-independent 的**：functional probe 确认 L8-L13 peak（0.655-0.678），之后下降。这是 C3 最强的 evidence，不依赖 RSA/CKA 选择。
75	- **Metric divergence 本身是 honest observation**："non-monotonic under RSA, monotonic under CKA"
76	- **DINOv2 RSA ranking**：在 RSA 下 robust，但必须加 "under RSA" qualifier
77	
78	**写法要求**：
79	- Abstract/Intro 中"non-monotonic refinement"加 "under RSA" qualifier
80	- DINOv2 "highest geometric foundation" 加 "as measured by RSA"
81	- best-vs-best Δ=+0.017 明确标 n.s.（CI includes 0）
82	- Discussion 加 metric-dependence caveat（CKA 反转在正文中 qualify，不只在 appendix）
83	
84	Key evidence (unchanged but qualified):
85	- Cross-encoder RSA table — **加 "under RSA" qualifier**
86	- Per-layer RSA + R² profiles — **rise phase CI 待补报**
87	- Cross-benchmark replication — still holds
88	- **CKA divergence** — 必须在正文 acknowledge
89	
90	## Story Spine (D060 Reframe)
91	
92	- **Problem**: VLAs fine-tune LLMs on robot data, but how training reshapes instruction routing and information integration at the token level remains uncharacterized.
93	- **Existing approaches & gaps**: Prior behavioral studies (Grant et al. 2026, Haon et al. 2025) found visual dominance and instruction underutilization, but did not decompose the representational roles of different token positions or explain how training reshapes information flow through the LLM.
94	- **Our framing**: We provide a systematic experimental framework for token-level analysis of VLAs. Using factorial controls (trained/pretrained/untrained) and four complementary methods, we find that VLA fine-tuning's primary contribution is learning a distinctive instruction routing strategy: shifting attention from mid-depth processing (inherited from language pretraining) to an entry-exit pattern, enabling immediate instruction access.
95	- **Headline results**: (1) [Framework] Architecture-expected token specialization is verified and quantified across 32 layers and three conditions. (2) [Core finding] Three qualitatively distinct routing strategies revealed: untrained (0/32 heads, no routing) → pretrained (9/32, mid-depth) → trained (25/32, entry-exit); instruction-conditioned action generation operates through distributed L1 routing where instruction-attention fraction predicts per-head contribution magnitude (dose-response monotonic d=0.48→0.64; counterfactual graduated d=0.63→0.97; size-matched specificity ratio 1.08x). (3) [Observation] Under RSA, vision encoder geometry follows an inverted-U through LLM layers with a substantial decline phase; functional probes confirm peak at L8-L13.
96	- **Practical implications**: (1) Architecture design should optimize instruction-to-readout routing. (2) Under RSA, self-supervised encoders provide the strongest action-relevant geometry (qualified by CKA divergence). (3) L8-L13 functional peak identifies a potential early-exit window.
97	
98	## Key Numerical Benchmarks (unchanged from A+)
99	
100	### Cross-Instruction Probe (C1 + C2 核心实验)
101	
102	| Condition | L0 | L1 | L2 | L5 | L8 | L16 | L24 | L31 |
103	|-----------|----|----|----|----|----|----|-----|-----|
104	| Trained last_preaction | 10% | 99.6% | 100% | 100% | 100% | 100% | 100% | 100% |
105	| **Llama-2 base last_preaction** | **10%** | **80.2%** | **98.7%** | **100%** | **100%** | **100%** | **100%** | **100%** |
106	| Untrained last_preaction | 10% | 100% | 100% | 99.x% | 98.6% | 92.3% | 86.4% | 82.0% |
107	| Trained image_mean | 10% | — | — | — | 10% | 10% | 10% | 9.6% |
108	| DINOv2 | 10% | — | — | — | — | — | — | — |
109	
110	LOOCV (10-fold): Trained 100.00±0.00 (L8-L31), Untrained 96.64±7.07 → 84.76±11.59
111	
112	### L1 Attention Pattern (C2 mechanistic evidence — three-condition)
113	
114	| Metric | Untrained | Llama-2 Base | VLA Trained |
115	|--------|-----------|--------------|-------------|
116	| Attention to text/instruction | 11.7% | 36.5% | 57.7% |
117	| Attention to image | 87.8% | 61.7% | 21.3% |
118	| Instruction-dominant heads (>50%) | 0/32 | 9/32 | 25/32 |
119	
120	### Training Effect Size Summary
121	
122	| Metric | Trained | Untrained | Δ |
123	|--------|---------|-----------|---|
124	| RSA peak (image_mean) | 0.628 (L12) | 0.612 (L0) | +0.017 |
125	| R² peak (last_preaction) | 0.678 (L13) | 0.609 (L32) | +0.069 |
126	| Inst. routing L31 | 100% | 82% | +18pp |
127	| Inst. attention L1 | 58% | 12% | +46pp |
128	| Progress classification | 86.3% (L20) | 85.3% (L4) | +1pp |
129	
130	### Cross-Encoder RSA (C3)
131	
132	| Source | RSA |
133	|--------|-----|
134	| DINO cls_token | 0.692 |
135	| DINO patch_mean | 0.631 |
136	| SigLIP+Projector | 0.615 |
137	| VLA trained peak (L12) | 0.628 |
138	| CLIP ViT-L | 0.557 |
139	
140	## Anticipated Reviewer Concerns (D060 updated — Round 4 已验证)
141	
142	### RC1: "C1 is trivial — causal mask guarantees it" [Round 4 N1, ACCEPTED]
143	**Response**: We accept this. Paper now explicitly acknowledges causal mask as structural source. C1 is repositioned as methodological framework + empirical verification, not novel finding. The framework itself (factorial design + 4 methods) has reusable value for VLA analysis.
144	
145	### RC2: "RSA inverted-U is metric-dependent, CKA reverses" [Round 4 N2, PARTIALLY ACCEPTED]
146	**Response**: Rise phase (Δρ=+0.016) acknowledged as small and qualified with CI. CKA divergence discussed in main text, not just appendix. Decline phase (Δρ=-0.206) is robust across metrics. DINOv2 ranking qualified with "under RSA". C3 downgraded from core claim to observation.
147	
148	### RC3: "Ablation 5 demos underfitting" [Round 4 N3, ACCEPTED + RERUN]
149	**Response**: 50-demo rerun in progress. If effect holds → underfitting confound ruled out. Non-dominant-8 control addresses generic regularization concern. Results TBD.
150	
151	### RC4: "Only tested on one VLA (OpenVLA)"
152	**Response**: Scope explicitly limited. C1 generalizes via causal mask for any decoder-only VLA. C2 routing pattern is testable prediction for other architectures. Future work lists RT-2, π₀.
153	
154	### RC5: "Practical implications speculative / frozen encoder confound" [Round 4 W4]
155	**Response**: Encoder ranking qualified with "under RSA" and "within fixed encoder configuration." Discussion adds explicit caveat that claims about encoder quality require across-encoder experiments. Routing optimization remains well-supported by three-condition gradient.
156	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "22edf023-2138-4649-ab9f-5e085c7053fe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md",
      "content": "# Paper Framing — vla-ssd (Plan B → D060 Reframe)\n\n> D048: PI 批准按最大质量重构。A+ 版本保留为 fallback (branch paper-a-plus-backup)。\n> D060: Round 4 weak reject → C1 降为框架, C2 升为唯一核心 claim, C3 降为 qualified observation。\n\n## Target Venue\n- Primary: CoRL 2026\n- Deadline: Abstract May 26, Paper May 29\n- Format: 8 pages + references\n\n## Core Insight\n\nVLA fine-tuning 的核心贡献是学习 deliberate instruction routing：将 instruction attention 从语言预训练的中层模式（L9-L16）reorganize 到 entry-exit 模式（L0-L1 + L31），实现即时 instruction access。这个三条件梯度（untrained 0/32 → pretrained 9/32 → trained 25/32）是 genuine empirical finding，具有 causal evidence 支撑。Token-level specialization（image-blind, readout-hub）是 causal mask 架构保证的性质，我们通过系统实验 verify 和 quantify 其在实际 VLA 中的表现。\n\n## Core Claims (D060 重构：1 核心 + 1 框架 + 1 观察)\n\n### C1: Experimental Framework + Architecture-Verified Specialization [方法论贡献，非 empirical finding]\n**重新定位（D060）**: Token-level specialization 是 causal mask 的数学必然（image tokens 在序列中先于 instruction tokens，无法 attend to instructions）+ frozen encoder 不接收 instruction input。论文贡献不是\"发现\"这一点，而是：\n- **(a) 系统实验框架**：factorial design (trained/pretrained/untrained × instruction presence) + 四种互补分析方法（cross-instruction probe + attention + RSA + MLP probe），适用于任何 decoder-only VLA\n- **(b) 量化验证**：即使 residual stream 理论上可以 leak information，image tokens 在实际模型的全部 32 层均保持 chance（10%）。这不是 trivial——frozen encoder 权重与 LLM 权重共享 residual stream，验证了 no leakage\n- **(c) 训练差异的量化**：untrained readout L1=100% 但 L31=82%（信号衰减）vs trained 100% 全程稳定——framework 揭示了训练影响 routing robustness 而非 routing existence\n\nKey evidence (unchanged):\n- Cross-instruction probe: same frame × 10 instructions → 10-way classification\n- Dense L0-L32: image_mean = chance at ALL layers\n- LOOCV: 100%±0.00 trained, decaying untrained\n- **承认**: 10-way classification 本身 trivially easy（untrained L1 也 100%），贡献在于 framework + 三条件对比揭示的 routing 差异\n\n### C2: Three Qualitatively Different Routing Strategies — VLA Fine-tuning Achieves Immediate Dedicated Routing\n三条件揭示三种定性不同的 routing 模式：\n\n**L1 Attention Routing (heads + attention fraction):**\n- **Untrained (random init)**: 0/32 heads, 12% text attention\n- **Llama-2 base (pretrained, no VLA)**: 9/32 heads, 36.5% text attention\n- **VLA Trained**: 25/32 heads, 58% text attention\n\n**Full-Layer Probe Profile (instruction classification accuracy):**\n- **Trained**: L1=99.6% → 全程 100% — \"即时路由 + 完全稳定\"\n- **Llama-2 base**: L1=80.2% → L2=98.7% → L5+=100% — \"渐进建立 + 稳定维持\"\n- **Untrained**: L1=100% → L8=98.6% → L31=82% — \"偶然路由 + 逐渐遗忘\"\n\n**VLA Fine-tuning 的独特贡献（精��化）：**\n1. **即时性**：L1 即达 99.6%（vs pretrained 需 5 层才饱和）\n2. **头数专用化**：25/32 heads instruction-dominant（vs pretrained 9/32）\n3. **不是**深层稳定性 — 稳定性来自 pretrained weights（pretrained 也不衰减）\n\n**深层���减只发生在 random init**：说明结构化的 pretrained 表示（无论是否经过 VLA 训练）都能维持 instruction signal；random weights 的噪声累积导致信号退化。\n\n**Full 32-Layer Attention Profile（D054 升级，dense evidence）：**\n- **Untrained**: 全 32 层 × 所有 head = 0 instruction-dominant。完全无语言处理能力。\n- **Llama-2 base**: 倒U型 — L0-L4 低(0-10 heads) → L9-L16 高峰(15-22 heads) → L31 回落(8)。经典 LM pattern：中层做深度语义处理。\n- **VLA Trained**: 书挡型 — L0-L1 高峰(21-24 heads) → L2-L30 低谷(0-11) → L31 再次高峰(18)。入口获取 instruction + 出口条件化 action output。\n\n**C2 Claim（D073 reframe: open-loop functional sensitivity）**: VLA fine-tuning **shifts** instruction attention from mid-layer processing (Llama-2 base: 15-22/32 heads at L10-L17) to entry-layer routing (L0-L1: 21-24/32) and exit-layer re-engagement (L31: 18/32)。Instruction-conditioned action generation operates through **distributed L1 routing** where instruction-attention fraction predicts per-head contribution magnitude (specificity ratio 1.08x at action output)。Routing modulates output direction (d=0.65) without systematic quality degradation (ΔMSE≈0), consistent with an information-computation dissociation (Hewitt & Liang 2019)。不能 claim instruction heads \"uniquely responsible\" 或 \"confirms routing function\"——用 \"open-loop functional sensitivity\" + \"support\" 而非 \"confirm\"。可 claim \"disproportionate contribution\" + \"attention-ordered routing\"。Section 标题用 \"Open-loop functional sensitivity\"，正文用 \"shifts...from...to...\" + \"distributed routing\"。\n\nKey evidence:\n- **32-layer dense attention profile**: Trained bookend (L0-1: 21-24, L31: 18) vs Llama2base inverted-U (L9-16: 15-22)\n- Three-condition full-layer probe: trained flat 100%; llama2base saturates L5+100%; untrained decays L1:100%→L31:82%\n- L1 attention gradient: 0/32 → 9/32 → 25/32 heads\n- VLA-specific contributions: (1) temporal reorganization from mid-peak to bookend, (2) immediacy (L1: 80.2→99.6%), (3) head dedication (9→25 at L1)\n- **Per-token normalization**: 38.2x text/image ratio (trained instr-dom) vs 1.5x (untrained) — eliminates token-count confound\n- **Trajectory-level d**: all conditions d>2.0 (token-level is conservative ~4x underestimate)\n- **GT error**: ΔMSE≈0 (ablation redirects outputs without degrading GT accuracy) — supports information-computation dissociation\n- **Token overlap**: Spearman ρ=1.0 between token novelty and d — lexical/positional sensitivity, not semantic distance\n- **LOO sensitivity**: all leave-one-out p ≤ 0.083, no qualitative reversal; cream cheese reclassification p=0.008\n- **4-condition training trajectory (D075)**: untrained(0) → llama2(9) → bridge-vla(24) → libero-finetuned(22) at L1。Entry routing 稳定，但 L31 exit engagement 18→0（entry-exit → entry-only sharpening）。Probe accuracy 不变（L31 仍 100%），确认 attention-representation dissociation\n- **OXE training diversity**: openvla-7b 在 Open X-Embodiment 970K episodes（多平台多任务）上训练，L1 routing 不是 LIBERO-specific\n\n### C3: Vision Encoder Geometry Observation [降为 qualified observation，非 core claim]\n**重新定位（D060）**: RSA inverted-U 的 rise phase 极小（Δρ=0.016, CI 待补），CKA 完全反转 RSA ordering（untrained > trained > DINOv2），\"non-monotonic refinement\" 仅在 RSA 下成立。DINOv2 ranking 在 CKA 下不成立（CKA 中 DINOv2 排名最低）。\n\n**保留为 observation 的理由**：\n- **Decline phase 也是 RSA-specific**：L12→L32 Δρ=-0.206 远大于 rise phase，但 CKA 单调递增无 decline。不能 claim decline 是 metric-robust。\n- **R² inverted-U 是 metric-independent 的**：functional probe 确认 L8-L13 peak（0.655-0.678），之后下降。这是 C3 最强的 evidence，不依赖 RSA/CKA 选择。\n- **Metric divergence 本身是 honest observation**：\"non-monotonic under RSA, monotonic under CKA\"\n- **DINOv2 RSA ranking**：在 RSA 下 robust，但必须加 \"under RSA\" qualifier\n\n**写法要求**：\n- Abstract/Intro 中\"non-monotonic refinement\"加 \"under RSA\" qualifier\n- DINOv2 \"highest geometric foundation\" 加 \"as measured by RSA\"\n- best-vs-best Δ=+0.017 明确标 n.s.（CI includes 0）\n- Discussion 加 metric-dependence caveat（CKA 反转在正文中 qualify，不只在 appendix）\n\nKey evidence (unchanged but qualified):\n- Cross-encoder RSA table — **加 \"under RSA\" qualifier**\n- Per-layer RSA + R² profiles — **rise phase CI 待补报**\n- Cross-benchmark replication — still holds\n- **CKA divergence** — 必须在正文 acknowledge\n\n## Story Spine (D060 Reframe)\n\n- **Problem**: VLAs fine-tune LLMs on robot data, but how training reshapes instruction routing and information integration at the token level remains uncharacterized.\n- **Existing approaches & gaps**: Prior behavioral studies (Grant et al. 2026, Haon et al. 2025) found visual dominance and instruction underutilization, but did not decompose the representational roles of different token positions or explain how training reshapes information flow through the LLM.\n- **Our framing**: We provide a systematic experimental framework for token-level analysis of VLAs. Using factorial controls (trained/pretrained/untrained) and four complementary methods, we find that VLA fine-tuning's primary contribution is learning a distinctive instruction routing strategy: shifting attention from mid-depth processing (inherited from language pretraining) to an entry-exit pattern, enabling immediate instruction access.\n- **Headline results**: (1) [Framework] Architecture-expected token specialization is verified and quantified across 32 layers and three conditions. (2) [Core finding] Three qualitatively distinct routing strategies revealed: untrained (0/32 heads, no routing) → pretrained (9/32, mid-depth) → trained (25/32, entry-exit); instruction-conditioned action generation operates through distributed L1 routing where instruction-attention fraction predicts per-head contribution magnitude (dose-response monotonic d=0.48→0.64; counterfactual graduated d=0.63→0.97; size-matched specificity ratio 1.08x). (3) [Observation] Under RSA, vision encoder geometry follows an inverted-U through LLM layers with a substantial decline phase; functional probes confirm peak at L8-L13.\n- **Practical implications**: (1) Architecture design should optimize instruction-to-readout routing. (2) Under RSA, self-supervised encoders provide the strongest action-relevant geometry (qualified by CKA divergence). (3) L8-L13 functional peak identifies a potential early-exit window.\n\n## Key Numerical Benchmarks (unchanged from A+)\n\n### Cross-Instruction Probe (C1 + C2 核心实验)\n\n| Condition | L0 | L1 | L2 | L5 | L8 | L16 | L24 | L31 |\n|-----------|----|----|----|----|----|----|-----|-----|\n| Trained last_preaction | 10% | 99.6% | 100% | 100% | 100% | 100% | 100% | 100% |\n| **Llama-2 base last_preaction** | **10%** | **80.2%** | **98.7%** | **100%** | **100%** | **100%** | **100%** | **100%** |\n| Untrained last_preaction | 10% | 100% | 100% | 99.x% | 98.6% | 92.3% | 86.4% | 82.0% |\n| Trained image_mean | 10% | — | — | — | 10% | 10% | 10% | 9.6% |\n| DINOv2 | 10% | — | — | — | — | — | — | — |\n\nLOOCV (10-fold): Trained 100.00±0.00 (L8-L31), Untrained 96.64±7.07 → 84.76±11.59\n\n### L1 Attention Pattern (C2 mechanistic evidence — three-condition)\n\n| Metric | Untrained | Llama-2 Base | VLA Trained |\n|--------|-----------|--------------|-------------|\n| Attention to text/instruction | 11.7% | 36.5% | 57.7% |\n| Attention to image | 87.8% | 61.7% | 21.3% |\n| Instruction-dominant heads (>50%) | 0/32 | 9/32 | 25/32 |\n\n### Training Effect Size Summary\n\n| Metric | Trained | Untrained | Δ |\n|--------|---------|-----------|---|\n| RSA peak (image_mean) | 0.628 (L12) | 0.612 (L0) | +0.017 |\n| R² peak (last_preaction) | 0.678 (L13) | 0.609 (L32) | +0.069 |\n| Inst. routing L31 | 100% | 82% | +18pp |\n| Inst. attention L1 | 58% | 12% | +46pp |\n| Progress classification | 86.3% (L20) | 85.3% (L4) | +1pp |\n\n### Cross-Encoder RSA (C3)\n\n| Source | RSA |\n|--------|-----|\n| DINO cls_token | 0.692 |\n| DINO patch_mean | 0.631 |\n| SigLIP+Projector | 0.615 |\n| VLA trained peak (L12) | 0.628 |\n| CLIP ViT-L | 0.557 |\n\n## Anticipated Reviewer Concerns (D060 updated — Round 4 已验证)\n\n### RC1: \"C1 is trivial — causal mask guarantees it\" [Round 4 N1, ACCEPTED]\n**Response**: We accept this. Paper now explicitly acknowledges causal mask as structural source. C1 is repositioned as methodological framework + empirical verification, not novel finding. The framework itself (factorial design + 4 methods) has reusable value for VLA analysis.\n\n### RC2: \"RSA inverted-U is metric-dependent, CKA reverses\" [Round 4 N2, PARTIALLY ACCEPTED]\n**Response**: Rise phase (Δρ=+0.016) acknowledged as small and qualified with CI. CKA divergence discussed in main text, not just appendix. Decline phase (Δρ=-0.206) is robust across metrics. DINOv2 ranking qualified with \"under RSA\". C3 downgraded from core claim to observation.\n\n### RC3: \"Ablation 5 demos underfitting\" [Round 4 N3, ACCEPTED + RERUN]\n**Response**: 50-demo rerun in progress. If effect holds → underfitting confound ruled out. Non-dominant-8 control addresses generic regularization concern. Results TBD.\n\n### RC4: \"Only tested on one VLA (OpenVLA)\"\n**Response**: Scope explicitly limited. C1 generalizes via causal mask for any decoder-only VLA. C2 routing pattern is testable prediction for other architectures. Future work lists RT-2, π₀.\n\n### RC5: \"Practical implications speculative / frozen encoder confound\" [Round 4 W4]\n**Response**: Encoder ranking qualified with \"under RSA\" and \"within fixed encoder configuration.\" Discussion adds explicit caveat that claims about encoder quality require across-encoder experiments. Routing optimization remains well-supported by three-condition gradient.\n",
      "numLines": 156,
      "startLine": 1,
      "totalLines": 156
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Glob · `toolu_01HhPPu1N9XpHs8DmuTMjV7S`</summary>

```json
{
  "pattern": "**/appendix.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "1c3f6368-8c6d-4d0c-b8ea-92b14962d218",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bm2e2BSb9imX69RspDsR3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16429,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16429
      },
      "output_tokens": 8,
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

_source line 23 · 2026-05-19T11:56:56.277Z_

<details><summary>↩ Tool result · `toolu_01HhPPu1N9XpHs8DmuTMjV7S`</summary>

```text
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "35d77421-5f05-4c19-a654-6eddc699f0e6",
  "tool_use_result": {
    "filenames": [
      "docs/paper/appendix.tex"
    ],
    "durationMs": 5,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the appendix to find where to add the attention profile caveat.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "1be825d5-5e7c-411c-9d5c-4d27ec9720ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ke5b9Wobp4jegTgjQvZ7v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21721,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21721
      },
      "output_tokens": 8,
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

### Assistant

_source line 25_

Let me check the appendix for the threshold sensitivity section, and find the specificity ratio 1.08x location in discussion.tex and counterfactual table in experiments.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "e61253eb-4263-426e-bfe7-ad0e00ffeed9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ke5b9Wobp4jegTgjQvZ7v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21721,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21721
      },
      "output_tokens": 8,
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

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_019RAtVTeXnNBoBqnrczs16W`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "fe0b107b-4e2d-4d0f-b28e-7f8b8681a4a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ke5b9Wobp4jegTgjQvZ7v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21721,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21721
      },
      "output_tokens": 8,
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

_source line 27 · 2026-05-19T11:57:01.925Z_

<details><summary>↩ Tool result · `toolu_019RAtVTeXnNBoBqnrczs16W`</summary>

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
182	\caption{Counterfactual instruction analysis. Cohen's $d$, token divergence (\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}
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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "612c317d-0895-4d96-afeb-b4e3b54dbc80",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
      "content": "\\paragraph{Use of Generative AI.}\nGenerative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\n\n\\appendix\n\n\\section{Supplementary Material}\n\\label{sec:appendix}\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}\n\nWe employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA as a complementary perspective.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.\n\n\\subsection{Metric Sensitivity: RSA versus CKA}\n\\label{sec:metric_sensitivity_appendix}\n\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.\n\nAt the per-layer level, linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n\n\\subsection{Branch-Split Detailed Analysis}\n\\label{sec:branch_split_appendix}\n\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\n\n\\subsection{RSA Across Representation Sources}\n\\label{sec:rsa_bar_appendix}\n\nFigure~\\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\\ref{tab:rsa_overview}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n\\subsection{Per-Layer RSA Profiles}\n\\label{sec:rsa_perlayer_appendix}\n\nFigure~\\ref{fig:rsa_perlayer_curve} extends Figure~\\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}\n\\caption{Per-layer RSA ($\\rho$) for trained and untrained models at image\\_mean and readout (last\\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\\_mean diverge: readout $\\rho$ declines gradually ($0.628 \\to 0.584$) while image\\_mean $\\rho$ drops sharply ($0.628 \\to 0.422$), consistent with task-specific conditioning at the readout position.}\n\\label{fig:rsa_perlayer_curve}\n\\end{figure}\n\n\\subsection{Per-Layer Action Decoding Across Training Stages}\n\\label{sec:action_r2_threecond}\n\nFigure~\\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\\pm$ std).\nAll three conditions share L0 representations ($R^2 = 0.645 \\pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.\nThe trained model peaks at L9 ($R^2 = 0.643 \\pm 0.014$), consistent with progressive specialization for action-relevant feature integration.\nLlama-2 base shows a steady decline (L0: $0.645 \\to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.\nThe untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.\nThe three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.\nThe qualitative pattern is consistent across all 3 seeds.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_action_r2_threecond.pdf}\n\\caption{Per-layer action probe $R^2$ (image\\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \\pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\\pm$ std).}\n\\label{fig:action_r2_threecond}\n\\end{figure}\n\n\\subsection{Random-Subset Ablation Details}\n\\label{sec:random_subset_ablation}\n\nTo evaluate whether the ablation effect in \\S\\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).\nDominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \\pm 0.013$ (Figure~\\ref{fig:random_subset_ablation}).\nThe dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_random_subset_ablation.pdf}\n\\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \\pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}\n\\label{fig:random_subset_ablation}\n\\end{figure}\n\n\\subsection{Action Trajectory Analysis Details}\n\\label{sec:action_trajectory}\n\nTable~\\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.\nBoth conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).\nThe gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.\n\nPer-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).\nToken-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.\n\n\\paragraph{Trajectory-level aggregation.}\nAggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\\sim}4\\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).\nInstruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\nAll 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\nCounterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\nFine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n\n\\paragraph{Ground-truth action error.}\nAblation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\\Delta = +0.008$).\nChanges concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.\nPer-task breakdown shows all $|\\Delta\\text{MSE}| < 3\\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.\nThis is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.\n\nTable~\\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).\nIndividual control heads produce ${\\sim}1.9\\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.\nThe 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\\ $0.41$), consistent with collective coordination rather than individual strength.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}\n\\label{tab:perhead_bootstrap}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nGroup & $N$ heads & Collective $d$ & Per-head $d$ [95\\% CI] \\\\\n\\midrule\nInstruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\\\\nControl & 8 & 0.41 & 0.051 [0.048, 0.055] \\\\\n\\midrule\nDifference & --- & --- & 0.024, $p = 0.0018$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis. Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}\n\\label{sec:robustness_appendix}\n\n\\subsubsection{Distance Metric Invariance}\n\\label{sec:metric_invariance}\n\nThe inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\\ref{tab:metric_invariance}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}\n\\label{tab:metric_invariance}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Eucl.\\ Peak & Cos.\\ Peak & Profile $r$ \\\\\n\\midrule\nTrained image\\_mean & L12 & L12 & 0.990 \\\\\nTrained last\\_preaction & L12 & L13 & 0.990 \\\\\nUntrained image\\_mean & L0 & L0 & 0.995 \\\\\nUntrained last\\_preaction & L1 & L1 & 0.992 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Per-DOF Decomposition}\n\\label{sec:perdof}\n\nRSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\\rho = 0.193$), rotation (peak L12, $\\rho = 0.175$), and gripper (peak L13, $\\rho = 0.106$) all exhibit non-monotonic profiles.\nPer-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.\n\n\\subsubsection{Permutation Test}\n\\label{sec:permutation}\n\nPermutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).\n\n\\subsubsection{Probe Seed Sensitivity}\n\\label{sec:seed_sensitivity}\n\nAction probe $R^2$ is highly stable across random seeds.\nOver 5 seeds (trained image\\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\\%$ ($0.655 \\pm 0.002$; Table~\\ref{tab:seed_sensitivity}).\nPeak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.\nSeed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe $R^2$ peak across 5 random seeds (trained image\\_mean).}\n\\label{tab:seed_sensitivity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSeed & Peak Layer & Peak $R^2$ \\\\\n\\midrule\n0 & L9 & 0.654 \\\\\n1 & L16 & 0.656 \\\\\n2 & L9 & 0.653 \\\\\n3 & L10 & 0.655 \\\\\n42 & L9 & 0.655 \\\\\n\\midrule\nMean$\\pm$std & $10.6\\pm2.7$ & $0.655\\pm0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Demonstration Subsample Sensitivity}\n\\label{sec:demo_sensitivity}\n\nTo verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\\ref{tab:demo_sensitivity}).\nThe RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).\nThe probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.\nBoth metrics show reduced absolute values (RSA $-3.6\\%$, $R^2$ $-7.6\\%$) as expected from halved data, but the non-monotonic profile shape is preserved.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inverted-U stability under demonstration subsampling (trained image\\_mean).}\n\\label{tab:demo_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 50 demos & 25 demos & $\\Delta$ \\\\\n\\midrule\nRSA peak layer & L12 & L12 & 0 \\\\\nRSA peak $\\rho$ & 0.628 & 0.606 & $-3.6\\%$ \\\\\n$R^2$ peak layer & L9 & L11 & $+2$ \\\\\n$R^2$ peak value & 0.659 & 0.609 & $-7.6\\%$ \\\\\nRSA profile $r$ & --- & 0.970 & --- \\\\\n$R^2$ profile $r$ & --- & 0.819 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detailed Training Effects}\n\\label{sec:training_effects_appendix}\n\nTable~\\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\\Delta{=}+0.017$, $3\\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{RSA ($\\rho$)}} \\\\\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Probe $R^2$}} \\\\\nBest-vs-best image\\_mean & $+$0.015 & excl.\\ 0 & 0.006 \\\\\n\\quad (trained L8 vs.\\ untrained L0) & & & \\\\\nBest-vs-best readout & $+$0.069 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained L13 vs.\\ untrained L32) & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Training Effect Size Summary}\n\\label{sec:training_effect_summary}\n\nTable~\\ref{tab:training_effect_summary} consolidates training effects across all metrics.\nTraining effects on image\\_mean metrics are modest (RSA $\\Delta = +0.017$, $R^2$ $\\Delta = +0.015$), but effects on last\\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\\Delta = +0.069$).\nThis asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effect sizes across metrics. Image\\_mean effects are modest; last\\_preaction effects are large. Training targets readout-token information integration.}\n\\label{tab:training_effect_summary}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Trained & Untrained & $\\Delta$ \\\\\n\\midrule\nRSA peak (image\\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\\\\n$R^2$ peak (image\\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\\\\n$R^2$ peak (last\\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\\\\nInstruction routing L31 & 100\\% & 82\\% & $+$18pp \\\\\nInstruction attention L1 & 58\\% & 12\\% & $+$46pp \\\\\nProgress classification & 86.3\\% (L20) & 85.3\\% (L4) & $+$1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruction Routing Probes}\n\\label{sec:routing_appendix}\n\n\\subsubsection{Cross-Instruction Classification: Dense Layer Profile}\n\\label{sec:dense_routing}\n\nTable~\\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.\nThe step-function onset between L0 ($10\\%$, chance) and L1 (${\\geq}99.6\\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\\sim}12\\%$) suffices for linear classification at L1.\nBoth pretrained and VLA-trained models sustain $100\\%$ through L31; only random initialization shows progressive decay ($82\\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\\%$ vs.\\ $98.6\\%$).}\n\\label{tab:dense_routing}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained & Untrained & Image\\_mean (trained) \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL2 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL3 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL5 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL6 & 100.0\\% & 97.3\\% & 10.0\\% \\\\\nL7 & 100.0\\% & 96.4\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.6\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction LOOCV Validation}\n\\label{sec:loocv}\n\nLeave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.\nTrained last\\_preaction achieves $100\\% \\pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).\n\n\\subsubsection{QA Probe: Progress and Subtask Classification}\n\\label{sec:qa_probe}\n\nTo test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}\n\\label{tab:qa_probe}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSource & Best Layer & Accuracy \\\\\n\\midrule\nTrained last\\_preaction & L20 & 86.3\\% \\\\\nUntrained last\\_preaction & L20 & 85.3\\% \\\\\nDINOv2 cls\\_token & --- & 82.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction Probe Profiles}\n\\label{sec:probe_profiles}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_probe_conditions.pdf}\n\\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\\%$ at L1, saturating to $100\\%$. Llama-2 base starts at $80.2\\%$, reaching $100\\%$ by L5. Untrained starts at $100\\%$ but decays to $82\\%$ by L31.}\n\\label{fig:probe_conditions_appendix}\n\\end{figure}\n\n\\subsubsection{Four-Condition Cross-Instruction Probe Profile}\n\\label{app:finetuned_probe}\n\nTable~\\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\\to$0 instruction-dominant heads).}\n\\label{tab:finetuned_probe}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 80.2\\% & 99.6\\% & 99.7\\% \\\\\nL8 & 98.6\\% & 99.9\\% & 100.0\\% & 100.0\\% \\\\\nL31 & 82.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{L1 Attention Pattern Analysis}\n\\label{sec:attention_pattern}\n\nFigure~\\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.\nThe three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_l1_stacked_bar.pdf}\n\\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\\%$ text attention). Llama-2 base: 9/32 heads ($36.5\\%$). Untrained: 0/32 heads ($11.7\\%$). See Table~\\ref{tab:routing_gradient} for quantitative comparison.}\n\\label{fig:attention_appendix}\n\\end{figure}\n\n\\subsubsection{Multi-Layer Attention Patterns}\n\\label{sec:multilayer_attention}\n\nTable~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\nThe full profile (Figure~\\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_multi_layer_attn.pdf}\n\\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}\n\\label{fig:multilayer_attention}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\n\\label{tab:multilayer_attention}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{VLA Trained} & \\multicolumn{2}{c}{Llama-2 base} & \\multicolumn{2}{c}{Untrained} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\nLayer & Heads & Text\\% & Heads & Text\\% & Heads & Text\\% \\\\\n\\midrule\nL1 & \\textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\\\\nL8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\\\\nL16 & 10/32 & 48.4 & \\textbf{25/32} & 60.2 & 0/32 & 9.2 \\\\\nL31 & \\textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Threshold Sensitivity Analysis}\n\\label{sec:threshold_sensitivity}\n\nThe main text defines instruction-dominant heads as those allocating $>50\\%$ attention to instruction tokens.\nTable~\\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\\% to 70\\%; the 50\\% threshold is not a boundary-sensitive choice.\n\n\\begin{table}[h]\n\\centering\n\\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}\n\\label{tab:threshold_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nThreshold & VLA Trained & Llama-2 base & Untrained \\\\\n\\midrule\n30\\% & 32 & 13 & 0 \\\\\n40\\% & 31 & 10 & 0 \\\\\n50\\% & 24 & 9 & 0 \\\\\n60\\% & 9 & 4 & 0 \\\\\n70\\% & 5 & 3 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L1 Attention Decomposition by Head Group}\n\\label{sec:attention_decomp}\n\nTable~\\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.\n\n\\begin{table}[h]\n\\centering\n\\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}\n\\label{tab:attention_decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nHead Group & $N$ & Instruction & Vision & BOS/Other \\\\\n\\midrule\nInstruction-dominant & 24 & 62.4\\% & 18.8\\% & 18.8\\% \\\\\nControl & 8 & 44.9\\% & 27.1\\% & 28.0\\% \\\\\n\\midrule\n$\\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHead-level instruction attention entropy reaches $99.5\\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.\n\n\\paragraph{Per-token attention normalization.}\nThe $57.7\\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\\ 256 image tokens).\nPer-token normalization reveals a $38.2\\times$ ratio: each instruction token receives $38.2\\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\\times$ in untrained heads (a $25.5\\times$ increase from training).\nInstruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.\n\n\\subsection{Per-Dimension Action MAE Under Head Ablation}\n\\label{sec:per_dim_mae}\n\nTable~\\ref{tab:per_dim_mae} extends Table~\\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\\times$) falls between the two groups.}\n\\label{tab:per_dim_mae}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Instr.\\ 24h MAE & Control 8h MAE & Ratio \\\\\n\\midrule\n$dx$ & 0.00189 & 0.00037 & 5.09$\\times$ \\\\\n$dy$ & 0.00531 & 0.00125 & 4.26$\\times$ \\\\\n$dz$ & 0.00762 & 0.00243 & 3.14$\\times$ \\\\\n$roll$ & 0.02059 & 0.00785 & 2.62$\\times$ \\\\\n$pitch$ & 0.03071 & 0.01387 & 2.21$\\times$ \\\\\n$yaw$ & 0.03388 & 0.01783 & 1.90$\\times$ \\\\\n$gripper$ & 0.29072 & 0.14072 & 2.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}\n\\label{sec:per_task_r2}\n\nTable~\\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\\Delta R^2 = +0.107$; the 50-demo setting (\\S\\ref{sec:learned_routing}) yields a consistent $+0.059$.}\n\\label{tab:per_task_r2}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & Baseline $R^2$ & Ablated $R^2$ & $\\Delta R^2$ \\\\\n\\midrule\nopen middle drawer & 0.197 & 0.221 & $+$0.024 \\\\\nopen top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\\\\npush plate to stove & 0.190 & 0.197 & $+$0.007 \\\\\nput bowl on plate & 0.375 & 0.474 & $+$0.099 \\\\\nput bowl on stove & 0.235 & 0.395 & $+$0.160 \\\\\nput bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\\\\nput cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\\\\nput wine on rack & 0.189 & 0.424 & $+$0.235 \\\\\nput wine on cabinet & 0.279 & 0.353 & $+$0.074 \\\\\nturn on stove & 0.385 & 0.421 & $+$0.036 \\\\\n\\midrule\nMean $\\pm$ std & $0.256 \\pm 0.070$ & $0.363 \\pm 0.088$ & $+$0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Task Complexity and Routing Dependence}\n\\label{sec:task_complexity}\n\nWe classify tasks as \\emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.\nTable~\\ref{tab:task_complexity} reports per-task $|\\Delta R^2|$ under both groupings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-level L1 ablation effects ($|\\Delta R^2|$) grouped by instruction dependence. \\emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\\times$, $p = 0.033$). \\emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\\times$, $p = 0.008$).}\n\\label{tab:task_complexity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTask & $|\\Delta R^2|$ & Group \\\\\n\\midrule\nput wine on rack & 0.235 & Instr-disc \\\\\nput bowl on cabinet & 0.201 & Instr-disc \\\\\nput bowl on stove & 0.160 & Instr-disc \\\\\nput bowl on plate & 0.099 & Instr-disc \\\\\nopen top drawer + bowl & 0.075 & Instr-disc \\\\\nput wine on cabinet & 0.074 & Instr-disc \\\\\n\\midrule\nput cream cheese in bowl$^\\dagger$ & 0.159 & Vis-suff \\\\\nturn on stove & 0.036 & Vis-suff \\\\\nopen middle drawer & 0.024 & Vis-suff \\\\\npush plate to stove & 0.007 & Vis-suff \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\\\\n\\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\\times$} \\\\\n\\multicolumn{3}{l}{\\textbf{Sensitivity}$^\\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}\n\\label{sec:specificity_control}\n\nTo test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).\n\n\\begin{table}[h]\n\\centering\n\\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}\n\\label{tab:specificity_control}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition (24 heads) & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\nInstruction-dominant & 0.650 & (reference) \\\\\nRandom (5 seeds) & $0.601 \\pm 0.021$ & $[0.568, 0.622]$ \\\\\nImage-dominant & 0.580 & $[0.547, 0.613]$ \\\\\nBottom-24 & 0.565 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.\n",
      "numLines": 776,
      "startLine": 1,
      "totalLines": 776
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

````text
Now I have all the files I need. Let me plan out each edit carefully.

## Item 1: Specificity ratio 1.08x补统计描述 (discussion.tex)
In discussion.tex line 10, the 1.08× is mentioned. I need to add a sentence after it.

Looking at line 10:
```
\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\times$; Table~\ref{tab:specificity_control}).


```

I also see 1.08× referenced in the mechanistic interpretation section around line 13, where it discusses the matched-size ablation results showing instruction-dominant routing. The user wants me to add a supplementary sentence describing the 1.08× effect at its first mention on line 10. The text should explain that the instruction-dominant group exceeds the random baseline by 2.4 standard deviations.

Looking at the context, this sentence about the modest magnitude supporting distributed routing fits naturally right after the 1.08× is introduced in the synthesis paragraph, before moving into the mechanistic details.

```
Matched-size ablation ($d$: instruction $0.
```

Inserting the sentence after "indicate distributed routing"... I'm looking at where to place the discussion of the 1.08× magnitude in the mechanistic interpretation section, since that's where the matched-size ablation details are covered. I should restructure that paragraph to naturally incorporate the new sentence about what this modest scaling factor tells us about the routing mechanism.

For the second item, I need to find the right location in experiments.tex and discussion.tex to clarify the L31 exit collapse behavior. The current line 62 in experiments.tex describes the OpenVLA-7B condition showing stable L1 entry routing but complete loss of L31 exit re-engagement, with the mid-depth compression details. I should check if there's a "suggesting" phrase nearby that needs rewording to "consistent with the hypothesis that," and then look at discussion.tex line 18 to see where I need to add the alternative explanation and clarify that N=2. I'm noticing the user's instruction references experiments.tex:62, but the "suggesting" text about L31 exit routing actually appears in discussion.tex:18. Let me search through experiments.tex to see if there's another instance of "suggesting" that needs changing, or if the user may have meant discussion.tex instead. Looking at the actual text, I see the "suggesting" language is in discussion.tex:18, not experiments.tex:62. The experiments.tex paragraph about task-specific sharpening doesn't contain that phrasing, so I need to add hedging language there as well to soften the claim about entry-exit routing being eliminated. I should modify both files to be more cautious about the causal interpretation. Now I need to locate the counterfactual table and check if it's properly labeled with the number of tasks. The table appears to be referenced in the appendix, so let me search through the files to find where it's actually defined and see if the caption needs updating. I'm trying to figure out which table is actually Table 5 by counting through the document order. The counterfactual table is in the appendix, but I need to verify its numbering since LaTeX numbers tables sequentially across the entire document. Without compiling, I can't be certain of the exact numbering, but since the user specifically mentions the counterfactual table, I should find its caption in appendix.tex around line 182 and add the n_tasks footnote there.

Looking at the caption, I need to insert "computed on 3 representative tasks (cabinet, bowl, plate)" to clarify the scope of the analysis. I also need to handle the attention profile caveat about single-sample extraction and threshold sensitivity robustness, which should go in section 4.3 of the experiments file.

For the attention profile caveat, the redistribution paragraph already mentions threshold stability across 30%-70%, so I'll add a sentence before that reference explaining that head counts come from single-sample extraction and that the ordering holds across different thresholds.

Now I need to add the Michel et al. citation to related_work.tex. Looking at the mechanistic interpretability section, the paragraph about attention heads and circuits mentions pruning-related work by Voita. The Michel paper on head pruning fits naturally after that line, so I'll insert a sentence connecting their finding about prunable heads to our dose-response analysis of routing in VLAs.

For the second item, I'm identifying where to bridge instruction tuning from NLP to our work on representational mechanisms. The introduction already discusses learned attention routing and how instruction information reaches the action token, so I'll add a sentence contrasting NLP's focus on behavioral compliance with our mechanistic approach to instruction routing. I'm settling on placing this in related_work.tex after the VLA paragraph, since it naturally bridges the discussion of fine-tuning assumptions with how instruction tuning works in NLP before diving into the representational mechanisms we're studying. I'm tracking down all instances of "25/32" in the paper_framing.md file to update them to "24/32" — they appear across multiple lines describing head counts and attention patterns, and I need to make sure I catch every occurrence. I'm identifying all instances of "25/32" in paper_framing.md that refer to VLA Trained L1 heads and need to be corrected to "24/32" to match the paper. I can see there are multiple occurrences across different lines—in the gradient progression description, the table entries, and various explanatory sections. I'll systematically replace each one to ensure consistency with the experiments.tex source. The instruction-dominant group outperforms the random baseline by 2.4 standard deviations across 5 seeds, which supports the distributed routing interpretation rather than a dedicated mechanism. Counterfactual ordering aligns with token novelty at perfect correlation. The entry-exit pattern holds across general VLA training, and task-specific fine-tuning eliminates the L31 re-engagement entirely, suggesting exit routing enables multi-task flexibility—though this comparison is limited to two models. I'm working through edits to the experiments section, adding hedging language around the claims about routing behavior. For the LIBERO fine-tuned model, I need to soften the assertion that exit routing disappears by framing it as consistent with a hypothesis about multi-task flexibility rather than stating it as a definitive finding, especially given the small sample size of just two models being compared. I'm looking at how to integrate the single-extraction caveat into the attention profile discussion. The threshold sensitivity analysis already confirms the ordering is robust across the 30%-70% range, so I can weave in that head counts come from single-sample extraction while noting this robustness holds across classification boundaries.

For the related work additions, I'm planning to cite Michel et al. on attention head pruning and connect it to our dose-response findings showing monotonic rather than threshold effects in VLA instruction routing. Then I'll add a bridge between instruction tuning in NLP—which focuses on behavioral compliance—and our mechanistic study of how instruction information flows through the model's representations.

I also need to update the paper framing metrics from 25/32 to 24/32 across all instances.

Now I'm working through the exact string replacements to ensure they're precise and won't accidentally match unintended text. Let me execute these edits systematically, grouping the independent changes together. I'm realizing there's no "suggesting" language in experiments.tex to change—I need to focus on hedging the causal claim about entry-exit routing instead. The phrase "sharpening entry-exit routing to entry-only" is too strong, so I'm softening it to emphasize this is a hypothesis supported by the model comparison. I'm also adding specificity to the counterfactual analysis caption to note it's based on three representative tasks, clarifying that head counts come from single-sample extraction with threshold robustness confirmed in the appendix, and I'm starting to address the related work section. I'm looking at how to bridge the instruction tuning literature from NLP to the vision-language domain. The key distinction is that NLP instruction tuning emphasizes behavioral compliance, whereas my analysis focuses on how fine-tuning reshapes the internal routing mechanisms—specifically, how 24 of the 32 attention heads become instruction-dominant after training, which I'm studying through functional ablation rather than knowledge editing approaches. I'm verifying that each edit target is unique in its file before applying them. Checking discussion.tex for the routing language, then appendix.tex for the counterfactual analysis text, and confirming the threshold sensitivity reference appears only once. For the bibliography entries, I need to locate the exact passages in the paper where I'm adding the new citations—one about performance subsets and another about the central assumption regarding instruction routing.

Now I'm ready to execute all the edits across the different files, being careful to apply same-file edits sequentially to avoid any overlap issues. I'm checking the split for discussion.tex—the new sentence about the instruction-dominant group fitting between the ablation results and the counterfactual ordering works well. The style checks pass too, so this edit is ready.

For the OpenVLA-7B condition, I need to hedge the conclusion about entry-only routing since this is based on just N=2 observations. Rather than "sharpening entry-exit routing to entry-only," I could say something like "suggesting a shift toward entry-only routing (N=2)" to acknowledge the limited sample while still capturing the pattern. The mid-depth compression pattern (L9-L16 showing 1-7 heads versus the baseline 6-11) combined with the loss of exit re-engagement suggests that exit routing may be more critical for handling task diversity than for optimizing single-task performance, though the training data differences between conditions could also explain some of this variation.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "cef8e050-f97b-4df7-88a6-32396acad21e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

### Assistant

_source line 29_

Now I have all the context. Executing all 7 modifications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "f6bec593-8965-437e-bb1d-74e03a0590bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01ThTTPn3sLyP84zoD3BtN75`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "old_string": "indicate distributed routing; counterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).",
  "new_string": "indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "743e5474-f5cc-44a5-a253-0f1ddc810bdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

_source line 31 · 2026-05-19T11:59:41.328Z_

<details><summary>↩ Tool result · `toolu_01ThTTPn3sLyP84zoD3BtN75`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "8576f2e8-d443-469b-b840-90ae09b5ba9e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "oldString": "indicate distributed routing; counterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).",
    "newString": "indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.\n\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).\n\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).\n\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; counterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), suggesting exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 9,
        "lines": [
          " \\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).",
          " ",
          " \\paragraph{Mechanistic interpretation.}",
          "-Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; counterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).",
          "+Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.",
          "+The instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.",
          "+Counterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).",
          " That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.",
          " ",
          " \\paragraph{Functional stages and predictions.}"
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

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01TMbiJbJVo3LcctvqxJmSgr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "old_string": "suggesting exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).",
  "new_string": "consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "7d861cf4-42d2-4666-836b-ac7a6cf8f109",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

_source line 33 · 2026-05-19T11:59:42.830Z_

<details><summary>↩ Tool result · `toolu_01TMbiJbJVo3LcctvqxJmSgr`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "f7543bfa-3b62-42c6-a13e-f3201d6fb602",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "oldString": "suggesting exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).",
    "newString": "consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.\n\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).\n\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).\n\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), suggesting exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 7,
        "newStart": 17,
        "newLines": 8,
        "lines": [
          " ",
          " \\paragraph{Functional stages and predictions.}",
          " The per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).",
          "-The entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), suggesting exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).",
          "+The entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).",
          "+This is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.",
          " Predictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.",
          " ",
          " \\paragraph{Task-dependent routing.}"
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01V8TAynMcVssp7mgYBbAf1A`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "old_string": "sharpening entry-exit routing to entry-only.",
  "new_string": "an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "7e521d07-6436-4e15-9da5-cf3944ad8107",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

_source line 35 · 2026-05-19T11:59:44.174Z_

<details><summary>↩ Tool result · `toolu_01V8TAynMcVssp7mgYBbAf1A`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "aa703caf-22a0-4fda-bdfc-831338796688",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "oldString": "sharpening entry-exit routing to entry-only.",
    "newString": "an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each).\nRepresentations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\nThree LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\nRSA computes Spearman $\\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\\S\\ref{sec:rsa}).\nMLP probes (input $\\to$ 256 $\\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\\S\\ref{sec:probes}).\nThis yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\\text{eff} = 10$) and probes use demo-level train/test splits.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\n%------------------------------------------------------------------\n\\subsection{Framework Validation: Token-Level Specialization}\n\\label{sec:token_specialization}\n\nAs a sanity check on the experimental framework, we train cross-instruction probes (\\S\\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.\n\n\\paragraph{Image tokens are instruction-blind (expected).}\nAs predicted by the causal mask and frozen encoder, image\\_mean instruction classification remains at chance ($10\\%$) across all 32 layers in all conditions (Table~\\ref{tab:dense_routing_main}).\nBoth linear and MLP probes corroborate this, as does standalone DINOv2 ($10\\%$; Appendix~\\ref{sec:instruction_invariance_appendix}).\n\n\\paragraph{Readout token as multimodal hub.}\nTrained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.\nThe readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\\ref{sec:dense_routing}). Image\\_mean remains at chance ($10\\%$) in all conditions; trained readout reaches $100\\%$ at L1 and holds; untrained readout decays from L1 to L31.}\n\\label{tab:dense_routing_main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained readout & Untrained readout & Image\\_mean \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL16 & 100.0\\% & 92.3\\% & 10.0\\% \\\\\nL31 & 100.0\\% & 82.0\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}\n\\label{sec:learned_routing}\n\n\\paragraph{Three-level routing gradient at L1.}\nL1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\nPer-token normalization ($38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}) corroborates this redistribution.\n\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\\%--70\\%; Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), sharpening entry-exit routing to entry-only.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}\nBest-vs-best RSA gain is non-significant on LIBERO-Goal ($\\Delta\\rho = 0.017$, $3\\%$, $N{=}10$ tasks; Appendix Table~\\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\\Delta = +0.023$, $p < 0.001$; Appendix~\\ref{sec:cross_benchmark_appendix}).\nThe $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\nFunctional improvements are larger: readout $R^2$ $\\Delta = +0.069$ ($p < 0.0001$, 95\\% CI $[0.047, 0.090]$), image\\_mean $\\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA $\\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix}). VLA rows: peak values. \\textbf{Bold}: best; \\underline{underline}: second.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & RSA $\\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\\\\n\\midrule\nDINOv2 cls\\_token & \\textbf{0.692} & 0.634 & --- & --- \\\\\nVLA Trained readout & \\underline{0.643} & \\textbf{0.678} & L12 & L13 \\\\\nFused DinoSigLIP & 0.634 & --- & --- & --- \\\\\nVLA Trained image\\_mean & 0.628 & \\underline{0.655} & L12 & L8--L10$^\\dagger$ \\\\\nDinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\\\\nVLA Untrained image\\_mean & 0.612 & 0.640 & L0 & L0 \\\\\nVLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\\\\nCLIP ViT-L/14$^\\ddagger$ & 0.557 & 0.587 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$$R^2$ peak region across 5 seeds ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).} \\\\\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$RSA uses \\texttt{patch\\_mean}; $R^2$ uses \\texttt{cls\\_token} (each encoder's best aggregation).}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$). Trained image\\_mean follows an inverted-U (L0 $0.612 \\to$ L12 $0.628 \\to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 59,
        "oldLines": 7,
        "newStart": 59,
        "newLines": 7,
        "lines": [
          " VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\\%--70\\%; Appendix~\\ref{sec:threshold_sensitivity}).",
          " ",
          " \\paragraph{Task-specific sharpening.}",
          "-A fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), sharpening entry-exit routing to entry-only.",
          "+A fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.",
          " Probe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).",
          " ",
          " \\paragraph{Probe robustness corroborates the pattern.}"
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01KnL6RdqdqgxjFpcZdxUMLX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "old_string": "; ordering is stable across thresholds (30\\%--70\\%; Appendix~\\ref{sec:threshold_sensitivity}).",
  "new_string": ".\nHead counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "8dbaad40-17d5-47d4-9d8e-1cbe5a720270",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

_source line 37 · 2026-05-19T11:59:45.511Z_

<details><summary>↩ Tool result · `toolu_01KnL6RdqdqgxjFpcZdxUMLX`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "8b220908-1a7f-4d06-80d6-7831c1415a5f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "oldString": "; ordering is stable across thresholds (30\\%--70\\%; Appendix~\\ref{sec:threshold_sensitivity}).",
    "newString": ".\nHead counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity}).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each).\nRepresentations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\nThree LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\nRSA computes Spearman $\\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\\S\\ref{sec:rsa}).\nMLP probes (input $\\to$ 256 $\\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\\S\\ref{sec:probes}).\nThis yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\\text{eff} = 10$) and probes use demo-level train/test splits.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\n%------------------------------------------------------------------\n\\subsection{Framework Validation: Token-Level Specialization}\n\\label{sec:token_specialization}\n\nAs a sanity check on the experimental framework, we train cross-instruction probes (\\S\\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.\n\n\\paragraph{Image tokens are instruction-blind (expected).}\nAs predicted by the causal mask and frozen encoder, image\\_mean instruction classification remains at chance ($10\\%$) across all 32 layers in all conditions (Table~\\ref{tab:dense_routing_main}).\nBoth linear and MLP probes corroborate this, as does standalone DINOv2 ($10\\%$; Appendix~\\ref{sec:instruction_invariance_appendix}).\n\n\\paragraph{Readout token as multimodal hub.}\nTrained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.\nThe readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\\ref{sec:dense_routing}). Image\\_mean remains at chance ($10\\%$) in all conditions; trained readout reaches $100\\%$ at L1 and holds; untrained readout decays from L1 to L31.}\n\\label{tab:dense_routing_main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained readout & Untrained readout & Image\\_mean \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL16 & 100.0\\% & 92.3\\% & 10.0\\% \\\\\nL31 & 100.0\\% & 82.0\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}\n\\label{sec:learned_routing}\n\n\\paragraph{Three-level routing gradient at L1.}\nL1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\nPer-token normalization ($38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}) corroborates this redistribution.\n\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\\%--70\\%; Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}\nBest-vs-best RSA gain is non-significant on LIBERO-Goal ($\\Delta\\rho = 0.017$, $3\\%$, $N{=}10$ tasks; Appendix Table~\\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\\Delta = +0.023$, $p < 0.001$; Appendix~\\ref{sec:cross_benchmark_appendix}).\nThe $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\nFunctional improvements are larger: readout $R^2$ $\\Delta = +0.069$ ($p < 0.0001$, 95\\% CI $[0.047, 0.090]$), image\\_mean $\\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA $\\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix}). VLA rows: peak values. \\textbf{Bold}: best; \\underline{underline}: second.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & RSA $\\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\\\\n\\midrule\nDINOv2 cls\\_token & \\textbf{0.692} & 0.634 & --- & --- \\\\\nVLA Trained readout & \\underline{0.643} & \\textbf{0.678} & L12 & L13 \\\\\nFused DinoSigLIP & 0.634 & --- & --- & --- \\\\\nVLA Trained image\\_mean & 0.628 & \\underline{0.655} & L12 & L8--L10$^\\dagger$ \\\\\nDinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\\\\nVLA Untrained image\\_mean & 0.612 & 0.640 & L0 & L0 \\\\\nVLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\\\\nCLIP ViT-L/14$^\\ddagger$ & 0.557 & 0.587 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$$R^2$ peak region across 5 seeds ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).} \\\\\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$RSA uses \\texttt{patch\\_mean}; $R^2$ uses \\texttt{cls\\_token} (each encoder's best aggregation).}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$). Trained image\\_mean follows an inverted-U (L0 $0.612 \\to$ L12 $0.628 \\to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 56,
        "oldLines": 7,
        "newStart": 56,
        "newLines": 8,
        "lines": [
          " \\paragraph{Redistribution of routing across depth.}",
          " The 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.",
          " Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).",
          "-VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30); ordering is stable across thresholds (30\\%--70\\%; Appendix~\\ref{sec:threshold_sensitivity}).",
          "+VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).",
          "+Head counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity}).",
          " ",
          " \\paragraph{Task-specific sharpening.}",
          " A fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute."
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

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01DJSgvDHj1xiLxFKupy9gfU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "old_string": "Counterfactual instruction analysis. Cohen's $d$",
  "new_string": "Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "f572ae75-cb00-46ea-bd68-1f2b6ee5cb2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

_source line 39 · 2026-05-19T11:59:46.441Z_

<details><summary>↩ Tool result · `toolu_01DJSgvDHj1xiLxFKupy9gfU`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "b4f1866b-c6f0-4894-a180-9dfaca8f8805",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "oldString": "Counterfactual instruction analysis. Cohen's $d$",
    "newString": "Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$",
    "originalFile": "\\paragraph{Use of Generative AI.}\nGenerative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.\n\n\\appendix\n\n\\section{Supplementary Material}\n\\label{sec:appendix}\n\n\\subsection{CKA Analysis Method}\n\\label{sec:cka_appendix}\n\nWe employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA as a complementary perspective.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.\n\n\\subsection{Metric Sensitivity: RSA versus CKA}\n\\label{sec:metric_sensitivity_appendix}\n\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.\n\nAt the per-layer level, linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), with no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n\n\\subsection{Branch-Split Detailed Analysis}\n\\label{sec:branch_split_appendix}\n\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}024-D) and SigLIP branch (1{,}152-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone; concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\n\n\\subsection{RSA Across Representation Sources}\n\\label{sec:rsa_bar_appendix}\n\nFigure~\\ref{fig:rsa_bar} shows RSA with the action space across all representation sources; the ordering matches Table~\\ref{tab:rsa_overview}.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment. CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n\\subsection{Per-Layer RSA Profiles}\n\\label{sec:rsa_perlayer_appendix}\n\nFigure~\\ref{fig:rsa_perlayer_curve} extends Figure~\\ref{fig:layer_curves} (main text) by adding readout and untrained profiles.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_rsa_perlayer_curve.pdf}\n\\caption{Per-layer RSA ($\\rho$) for trained and untrained models at image\\_mean and readout (last\\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\\_mean diverge: readout $\\rho$ declines gradually ($0.628 \\to 0.584$) while image\\_mean $\\rho$ drops sharply ($0.628 \\to 0.422$), consistent with task-specific conditioning at the readout position.}\n\\label{fig:rsa_perlayer_curve}\n\\end{figure}\n\n\\subsection{Per-Layer Action Decoding Across Training Stages}\n\\label{sec:action_r2_threecond}\n\nFigure~\\ref{fig:action_r2_threecond} compares per-layer action probe $R^2$ across three training stages (untrained, Llama-2 base, VLA-trained) using 50 demonstrations per task, averaged over 3 seeds (mean $\\pm$ std).\nAll three conditions share L0 representations ($R^2 = 0.645 \\pm 0.008$); subsequent differences thus arise from Transformer processing rather than input variation.\nThe trained model peaks at L9 ($R^2 = 0.643 \\pm 0.014$), consistent with progressive specialization for action-relevant feature integration.\nLlama-2 base shows a steady decline (L0: $0.645 \\to$ L32: $0.551$, std $0.003$--$0.035$), consistent with stable but unspecialized processing.\nThe untrained model exhibits high cross-seed variance and deep-layer collapse, with negative $R^2$ and bimodal behavior across seeds at late layers; this instability indicates that randomly initialized Transformer layers produce destructive interference on action-relevant structure.\nThe three-condition gradient (trained $>$ Llama-2 base $>$ untrained) holds from L1 through L15, with a reversal at L32 where trained $R^2$ drops below the pretrained baseline.\nThe qualitative pattern is consistent across all 3 seeds.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_action_r2_threecond.pdf}\n\\caption{Per-layer action probe $R^2$ (image\\_mean) across three training conditions: untrained VLA (random weights), Llama-2 base (pretrained, no VLA fine-tuning), and VLA-trained. All conditions share L0 ($0.645 \\pm 0.008$). Trained model peaks at L9; Llama-2 base declines steadily; untrained shows high cross-seed variance and deep-layer collapse. 50 demonstrations per task, 3 seeds (mean $\\pm$ std).}\n\\label{fig:action_r2_threecond}\n\\end{figure}\n\n\\subsection{Random-Subset Ablation Details}\n\\label{sec:random_subset_ablation}\n\nTo evaluate whether the ablation effect in \\S\\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).\nDominant-head ablation increases action $R^2$ by $+0.042$ (within-experiment baseline $0.517$), while random subsets yield a mean increase of $+0.077 \\pm 0.013$ (Figure~\\ref{fig:random_subset_ablation}).\nThe dominant-head effect falls below the random distribution ($z = -2.73$, $p = 0.003$); heads with higher instruction-attention fraction carry more organized routing signals, consistent with graded rather than binary specialization.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_random_subset_ablation.pdf}\n\\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \\pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with graded routing specialization across L1 heads.}\n\\label{fig:random_subset_ablation}\n\\end{figure}\n\n\\subsection{Action Trajectory Analysis Details}\n\\label{sec:action_trajectory}\n\nTable~\\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.\nBoth conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).\nThe gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.\n\nPer-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).\nToken-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.\n\n\\paragraph{Trajectory-level aggregation.}\nAggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\\sim}4\\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).\nInstruction-head ablation ($N = 50$: 5 tasks $\\times$ 10 demos) yields trajectory $d = 2.943$ (95\\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).\nAll 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.\nCounterfactual trajectory-level $d$: empty $3.438$ (CI $[2.921, 4.448]$), wrong $3.798$ ($[3.194, 4.938]$), paraphrased $2.131$ ($[1.740, 2.819]$), shuffled $2.595$ ($[2.028, 3.791]$).\nFine-grained ordering is not reliably distinguished at trajectory level ($N = 30$); token-level comparisons ($N {\\sim} 1{,}500$) provide higher resolution for ordering claims.\n\n\\paragraph{Ground-truth action error.}\nAblation redirects model outputs ($d = 0.65$) but does not systematically increase error relative to expert demonstrations: original MSE $= 0.498$; top-24 instruction-head ablation MSE $= 0.497$ ($\\Delta = -0.001$, Wilcoxon $p = 0.52$, n.s.); bottom-24 non-instruction heads MSE $= 0.506$ ($\\Delta = +0.008$).\nChanges concentrate on the gripper dimension; translation and rotation dimensions are negligibly affected.\nPer-task breakdown shows all $|\\Delta\\text{MSE}| < 3\\%$ of baseline with all $p > 0.27$; the near-zero aggregate $\\Delta$ reflects uniformly small per-task effects rather than cancellation across tasks.\nThis is consistent with the information-computation dissociation: routing heads control instruction-specific direction selection rather than action precision.\n\nTable~\\ref{tab:perhead_bootstrap} reports per-head bootstrap CIs ($10{,}000$ resamples).\nIndividual control heads produce ${\\sim}1.9\\times$ stronger effects ($d = 0.051$) than instruction heads ($d = 0.027$, $p = 0.0018$), consistent across all 5 tasks.\nThe 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\\ $0.41$), consistent with collective coordination rather than individual strength.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}\n\\label{tab:perhead_bootstrap}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nGroup & $N$ heads & Collective $d$ & Per-head $d$ [95\\% CI] \\\\\n\\midrule\nInstruction-dominant & 24 & 0.65 & 0.027 [0.026, 0.029] \\\\\nControl & 8 & 0.41 & 0.051 [0.048, 0.055] \\\\\n\\midrule\nDifference & --- & --- & 0.024, $p = 0.0018$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInstruction-head ablation produces more uniform perturbation across action dimensions (CV${}=1.30$ vs.\\ control CV${}=2.74$, permutation $p = 0.016$), consistent with structured, language-conditioned computation rather than diffuse noise.\n\nTable~\\ref{tab:dose_response} and Figure~\\ref{fig:dose_response} report the dose-response gradient for instruction-head ablation at L1.\nTrajectory divergence increases monotonically from $d = 0.482$ (4 heads) to $d = 0.639$ (32 heads), with steep rise through 12 heads (slope $\\Delta d / \\Delta 4 \\approx 0.026$), a plateau at 16--20 heads ($\\Delta d = 0.001$), and slow increase at 20--32.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{Dose-response gradient: trajectory divergence (Cohen's $d$) as a function of ablated instruction-dominant heads at L1. Error bars: 95\\% bootstrap CIs ($10{,}000$ resamples). Dashed red: control ablation (8 non-instruction heads, $d = 0.41$). Steep rise through 12 heads, plateau at 16--20, diminishing returns beyond.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Dose-response data for L1 instruction-head ablation. Cohen's $d$ vs.\\ original action sequence; 95\\% bootstrap CIs ($10{,}000$ resamples).}\n\\label{tab:dose_response}\n\\small\n\\begin{tabular}{rcc}\n\\toprule\nHeads ablated & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\n4 & 0.482 & [0.449, 0.511] \\\\\n8 & 0.508 & [0.479, 0.541] \\\\\n12 & 0.560 & [0.529, 0.593] \\\\\n16 & 0.592 & [0.559, 0.625] \\\\\n20 & 0.593 & [0.559, 0.627] \\\\\n24 & 0.611 & [0.578, 0.645] \\\\\n28 & 0.619 & [0.587, 0.654] \\\\\n32 & 0.639 & [0.603, 0.671] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Counterfactual instruction analysis. Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Jaccard & Cohen's $d$ & Token div.\\ (\\%) \\\\\n\\midrule\nEmpty (no instruction) & 0.000 & 0.968 & 90.7 \\\\\nWrong (different task) & 0.174 & 0.844 & 89.5 \\\\\nParaphrased & 0.533 & 0.697 & 82.6 \\\\\nShuffled (random order) & 1.000 & 0.625 & 85.7 \\\\\n\\midrule\nL1 ablation (24 heads) & --- & 0.650 & 72.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute action shift per dimension under L1 head ablation. Instruction: 24 dominant heads; Control: 8 remaining heads. Gripper shift dominates both conditions.}\n\\label{tab:action_shift_perdim}\n\\small\n\\begin{tabular}{lccccccc}\n\\toprule\nCondition & $dx$ & $dy$ & $dz$ & $rx$ & $ry$ & $rz$ & Gripper \\\\\n\\midrule\nInstruction (24) & 0.002 & 0.005 & 0.008 & 0.021 & 0.031 & 0.034 & 0.291 \\\\\nControl (8) & 0.000 & 0.001 & 0.002 & 0.008 & 0.014 & 0.018 & 0.141 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pretrained LLM Representation Quality Under Visual Input}\n\\label{sec:ood_diagnostics}\n\nA potential concern with the three-condition comparison (\\S\\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.\nWe evaluate three diagnostics to assess representation quality.\nActivation magnitude grows from $16.5$ (L0) to $90.2$ (L31) for Llama-2 base, compared to $16.5 \\to 51.7$ for the VLA-trained model; the pretrained LLM produces larger but non-exploding activations with no evidence of collapse.\nPer-layer cosine similarity between L0 and deeper layers decreases progressively from $1.0$ to $\\approx 0.28$ at L25, consistent with gradual differentiation rather than catastrophic out-of-distribution behavior.\nTop-10 principal component variance explained remains stable across all layers ($0.59$--$0.74$), with no low-rank collapse.\nThese diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining (Figure~\\ref{fig:ood_diagnostics}). These results support the validity of the three-condition comparison.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_ood_diagnostics.pdf}\n\\caption{Pretrained LLM representation diagnostics under visual input. Left: activation magnitude across layers (Llama-2 base vs.\\ VLA-trained). Center: cosine similarity between L0 and deeper layers. Right: top-10 PC variance explained. All three metrics indicate structured, non-degenerate representations.}\n\\label{fig:ood_diagnostics}\n\\end{figure}\n\n\\subsection{Probe Architecture Sensitivity}\n\\label{sec:linear_probe}\n\nTo rule out that our findings depend on MLP probe capacity ($N/\\text{params} \\approx 0.06$, overparameterized), we replicate the per-layer analysis with a linear probe ($4{,}096 \\to 7$, $N/\\text{params} \\approx 2.2$).\nThe inverted-U pattern reproduces: trained image\\_mean peaks at L14 ($R^2 = 0.565$), while untrained declines monotonically from L0 ($R^2 = 0.517$).\nThe trained--untrained gap is larger under the linear probe (L14: $\\Delta = +0.324$) than the MLP probe (L8: $\\Delta = +0.015$); VLA training thus reorganizes representations to make action information more linearly decodable.\nUntrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.\nFor last\\_preaction tokens, the linear probe also corroborates the inverted-U (peak L13, $R^2 = 0.596$), with the same peak layer as the MLP probe and a trained-vs-untrained gap of $\\Delta = 0.103$ ($p < 0.001$).\nThese results indicate that our qualitative findings reflect representational structure rather than probe capacity artifacts (Figure~\\ref{fig:linear_vs_mlp}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_linear_vs_mlp_probe.pdf}\n\\caption{Per-layer action probe $R^2$ for linear (dashed) and MLP (solid) probes across trained (blue) and untrained (red) conditions. The inverted-U reproduces under both probe architectures; the trained--untrained gap is larger for linear probes.}\n\\label{fig:linear_vs_mlp}\n\\end{figure}\n\n\\subsection{Functional Probe Comparison}\n\\label{sec:probe_bars_appendix}\n\nFigure~\\ref{fig:probe_bars} compares functional probe $R^2$ across representation sources at each source's best layer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\\_mean ($0.655$, L8) exceed the projector baseline ($0.630$); the inverted-U extends to functional capacity.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n\\subsection{Training Effect and Instruction Invariance}\n\\label{sec:instruction_invariance_appendix}\n\nFigure~\\ref{fig:factorial} shows trained vs.\\ untrained RSA profiles and instruction invariance.\nInstruction invariance holds across all conditions: maximum $|\\Delta| < 0.006$, so action geometry is visually grounded and not modulated by language instructions.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$), yielding a modest best-vs-best gain ($\\Delta{=}+0.017$, $3\\%$). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$; action geometry is visually grounded.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Additional RSA Values}\n\\label{sec:additional_rsa}\n\nDINOv2 \\texttt{patch\\_mean} achieves RSA $\\rho = 0.631$, between the \\texttt{cls\\_token} ($0.692$) and the fused DinoSigLIP ($0.634$).\nVLA untrained readout peaks at L1 ($\\rho = 0.626$).\n\n\\subsection{Cross-Benchmark Validation: LIBERO-Spatial}\n\\label{sec:cross_benchmark_appendix}\n\nTo assess generalization beyond in-distribution tasks, we repeat the core RSA and probe analyses on LIBERO-Spatial (10 out-of-distribution tasks requiring spatial reasoning).\nFigure~\\ref{fig:cross_benchmark} shows per-layer RSA and $R^2$ profiles for both LIBERO-Goal and LIBERO-Spatial side by side.\n\nThe inverted-U profile replicates on LIBERO-Spatial: trained image\\_mean RSA peaks at L14 ($\\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.\nTraining produces a significant geometric gain (best-vs-best $\\Delta = +0.023$, 95\\% CI $[0.012, 0.036]$, $p < 0.001$), larger than the LIBERO-Goal effect ($\\Delta = +0.017$, CI includes zero).\n\nTwo notable differences emerge.\nFirst, the absolute RSA values are higher on Spatial ($0.691$ vs.\\ $0.628$), possibly reflecting greater action diversity in spatial tasks that produces a more discriminative action RDM.\nSecond, RSA--$R^2$ peak convergence does not replicate: readout RSA peaks at L15 while $R^2$ peaks at L21 (6-layer gap), contrasting with the near-alignment on Goal ($|\\Delta_\\text{layer}| = 1$).\nThis suggests that peak convergence is benchmark-specific rather than a general consequence of training.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig7.pdf}\n\\caption{Cross-benchmark validation: per-layer RSA and $R^2$ profiles on LIBERO-Goal (left) vs.\\ LIBERO-Spatial (right). The inverted-U replicates on both benchmarks. LIBERO-Spatial shows a significant training effect (RSA best-vs-best $\\Delta = +0.023$, $p < 0.001$) and deeper peak layers (RSA L14, $R^2$ L13), but RSA--$R^2$ peak convergence does not replicate (6-layer gap).}\n\\label{fig:cross_benchmark}\n\\end{figure}\n\n\\subsubsection{Cross-Instruction Probe on LIBERO-Spatial}\n\\label{sec:spatial_cross_instruction}\n\nTable~\\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.\nThe core pattern from LIBERO-Goal replicates: image\\_mean remains at chance (${\\sim}10\\%$) across all layers and conditions, while the trained readout token saturates to $100\\%$ by L4.\nThe untrained readout decays more steeply than on LIBERO-Goal ($75.4\\%$ at L31 vs.\\ $82\\%$), consistent with greater task difficulty.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\\%$ from L4; image\\_mean remains at chance. Untrained readout decays more steeply than on LIBERO-Goal (cf.\\ Table~\\ref{tab:dense_routing_main}).}\n\\label{tab:spatial_cross_instruction}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nToken & Condition & L1 & L4 & L8 & L16 & L31 \\\\\n\\midrule\nlast\\_preaction & Trained & 98.9\\% & 100.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\nlast\\_preaction & Untrained & 99.5\\% & 98.3\\% & 85.7\\% & 68.3\\% & 75.4\\% \\\\\nimage\\_mean & Trained & 10.2\\% & 10.0\\% & 9.9\\% & 10.0\\% & 10.1\\% \\\\\nimage\\_mean & Untrained & 10.1\\% & 10.0\\% & 10.0\\% & 10.0\\% & 10.2\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Robustness Analyses}\n\\label{sec:robustness_appendix}\n\n\\subsubsection{Distance Metric Invariance}\n\\label{sec:metric_invariance}\n\nThe inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\\ref{tab:metric_invariance}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}\n\\label{tab:metric_invariance}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Eucl.\\ Peak & Cos.\\ Peak & Profile $r$ \\\\\n\\midrule\nTrained image\\_mean & L12 & L12 & 0.990 \\\\\nTrained last\\_preaction & L12 & L13 & 0.990 \\\\\nUntrained image\\_mean & L0 & L0 & 0.995 \\\\\nUntrained last\\_preaction & L1 & L1 & 0.992 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Per-DOF Decomposition}\n\\label{sec:perdof}\n\nRSA decomposition by action dimension indicates the inverted-U is not driven by any single degree of freedom: xyz translation (peak L13, $\\rho = 0.193$), rotation (peak L12, $\\rho = 0.175$), and gripper (peak L13, $\\rho = 0.106$) all exhibit non-monotonic profiles.\nPer-DOF RSA values are lower than the 7-D RSA because single-dimension distances carry less discriminative information than the full action space.\n\n\\subsubsection{Permutation Test}\n\\label{sec:permutation}\n\nPermutation testing (1{,}000 shuffles) indicates all observed RSA values are highly significant: observed $\\rho$ ($0.42$--$0.63$) exceeds the null distribution maximum ($0.08$--$0.10$) by $15$--$23$ standard deviations (all $p < 0.001$).\n\n\\subsubsection{Probe Seed Sensitivity}\n\\label{sec:seed_sensitivity}\n\nAction probe $R^2$ is highly stable across random seeds.\nOver 5 seeds (trained image\\_mean, full-layer scan), per-layer $R^2$ standard deviation is uniformly below $0.01$ (mean $0.004$), and the peak $R^2$ varies by less than $0.4\\%$ ($0.655 \\pm 0.002$; Table~\\ref{tab:seed_sensitivity}).\nPeak layer concentrates in the L8--L10 region ($4/5$ seeds); the inverted-U shape is not a seed artifact.\nSeed 1 peaks at L16, but with $R^2$ difference ${<}0.002$. The inverted-U plateau (L8--L16) is sufficiently flat that argmax is sensitive to minor noise while the profile shape is invariant.\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe $R^2$ peak across 5 random seeds (trained image\\_mean).}\n\\label{tab:seed_sensitivity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSeed & Peak Layer & Peak $R^2$ \\\\\n\\midrule\n0 & L9 & 0.654 \\\\\n1 & L16 & 0.656 \\\\\n2 & L9 & 0.653 \\\\\n3 & L10 & 0.655 \\\\\n42 & L9 & 0.655 \\\\\n\\midrule\nMean$\\pm$std & $10.6\\pm2.7$ & $0.655\\pm0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Demonstration Subsample Sensitivity}\n\\label{sec:demo_sensitivity}\n\nTo verify that the inverted-U pattern is not an artifact of sample size, we subsample 25 from 50 demonstrations per task and recompute both RSA and probe profiles (Table~\\ref{tab:demo_sensitivity}).\nThe RSA peak layer remains at L12 with a profile correlation of $r = 0.970$ between 50- and 25-demo conditions (high stability).\nThe probe peak shifts from L9 to L11 (within the L8--L16 plateau) with $r = 0.819$; $R^2$ is more sensitive to training set size than RSA.\nBoth metrics show reduced absolute values (RSA $-3.6\\%$, $R^2$ $-7.6\\%$) as expected from halved data, but the non-monotonic profile shape is preserved.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inverted-U stability under demonstration subsampling (trained image\\_mean).}\n\\label{tab:demo_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 50 demos & 25 demos & $\\Delta$ \\\\\n\\midrule\nRSA peak layer & L12 & L12 & 0 \\\\\nRSA peak $\\rho$ & 0.628 & 0.606 & $-3.6\\%$ \\\\\n$R^2$ peak layer & L9 & L11 & $+2$ \\\\\n$R^2$ peak value & 0.659 & 0.609 & $-7.6\\%$ \\\\\nRSA profile $r$ & --- & 0.970 & --- \\\\\n$R^2$ profile $r$ & --- & 0.819 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detailed Training Effects}\n\\label{sec:training_effects_appendix}\n\nTable~\\ref{tab:training_effects} reports bootstrap-based statistical comparisons of training effects on RSA and probe $R^2$.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effects on action-relevant structure (LIBERO-Goal; bootstrap, 10{,}000 resamples). RSA best-vs-best yields a modest geometric gain ($\\Delta{=}+0.017$, $3\\%$; LIBERO-Spatial: $+0.023$, $p{<}0.001$), while $R^2$ shows substantially larger functional gains.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{RSA ($\\rho$)}} \\\\\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Probe $R^2$}} \\\\\nBest-vs-best image\\_mean & $+$0.015 & excl.\\ 0 & 0.006 \\\\\n\\quad (trained L8 vs.\\ untrained L0) & & & \\\\\nBest-vs-best readout & $+$0.069 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained L13 vs.\\ untrained L32) & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Training Effect Size Summary}\n\\label{sec:training_effect_summary}\n\nTable~\\ref{tab:training_effect_summary} consolidates training effects across all metrics.\nTraining effects on image\\_mean metrics are modest (RSA $\\Delta = +0.017$, $R^2$ $\\Delta = +0.015$), but effects on last\\_preaction metrics are substantial (routing $+18$pp, attention $+46$pp, $R^2$ $\\Delta = +0.069$).\nThis asymmetry indicates that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training effect sizes across metrics. Image\\_mean effects are modest; last\\_preaction effects are large. Training targets readout-token information integration.}\n\\label{tab:training_effect_summary}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Trained & Untrained & $\\Delta$ \\\\\n\\midrule\nRSA peak (image\\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\\\\n$R^2$ peak (image\\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\\\\n$R^2$ peak (last\\_preaction) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\\\\nInstruction routing L31 & 100\\% & 82\\% & $+$18pp \\\\\nInstruction attention L1 & 58\\% & 12\\% & $+$46pp \\\\\nProgress classification & 86.3\\% (L20) & 85.3\\% (L4) & $+$1pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruction Routing Probes}\n\\label{sec:routing_appendix}\n\n\\subsubsection{Cross-Instruction Classification: Dense Layer Profile}\n\\label{sec:dense_routing}\n\nTable~\\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.\nThe step-function onset between L0 ($10\\%$, chance) and L1 (${\\geq}99.6\\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\\sim}12\\%$) suffices for linear classification at L1.\nBoth pretrained and VLA-trained models sustain $100\\%$ through L31; only random initialization shows progressive decay ($82\\%$ at L31). Deep-layer stability thus derives from structured pretrained weights rather than task-specific fine-tuning.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy at readout token, L0--L8. Values reflect dense routing evaluation; main-text Table~\\ref{tab:dense_routing_main} reports sparse single-split results, yielding minor differences (e.g., L8: $98.2\\%$ vs.\\ $98.6\\%$).}\n\\label{tab:dense_routing}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained & Untrained & Image\\_mean (trained) \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL2 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL3 & 100.0\\% & 99.6\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL5 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL6 & 100.0\\% & 97.3\\% & 10.0\\% \\\\\nL7 & 100.0\\% & 96.4\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.6\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction LOOCV Validation}\n\\label{sec:loocv}\n\nLeave-one-out cross-validation over 10 folds (each fold holds out one task's instructions) validates that the cross-instruction probe result is not driven by memorization.\nTrained last\\_preaction achieves $100\\% \\pm 0.00$ across all 10 folds at layers L1--L31 (perfect generalization).\n\n\\subsubsection{QA Probe: Progress and Subtask Classification}\n\\label{sec:qa_probe}\n\nTo test whether LLM layers encode task-relevant semantic information beyond instruction identity, we train probes to classify task progress (early/mid/late) and active subtask from frozen representations (Table~\\ref{tab:qa_probe}).\n\n\\begin{table}[h]\n\\centering\n\\caption{QA probe accuracy (progress + subtask classification, best layer).}\n\\label{tab:qa_probe}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSource & Best Layer & Accuracy \\\\\n\\midrule\nTrained last\\_preaction & L20 & 86.3\\% \\\\\nUntrained last\\_preaction & L20 & 85.3\\% \\\\\nDINOv2 cls\\_token & --- & 82.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Cross-Instruction Probe Profiles}\n\\label{sec:probe_profiles}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_probe_conditions.pdf}\n\\caption{Cross-instruction 10-way classification accuracy at the readout token across all 32 LLM layers. VLA-trained achieves $99.6\\%$ at L1, saturating to $100\\%$. Llama-2 base starts at $80.2\\%$, reaching $100\\%$ by L5. Untrained starts at $100\\%$ but decays to $82\\%$ by L31.}\n\\label{fig:probe_conditions_appendix}\n\\end{figure}\n\n\\subsubsection{Four-Condition Cross-Instruction Probe Profile}\n\\label{app:finetuned_probe}\n\nTable~\\ref{tab:finetuned_probe} extends the three-condition probe comparison (Table~\\ref{tab:dense_routing_main}) with the LIBERO-finetuned checkpoint.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-instruction 10-way classification accuracy across four training conditions. Task-specific fine-tuning (LIBERO) preserves instruction decodability at all layers despite eliminating L31 exit-layer attention engagement (18$\\to$0 instruction-dominant heads).}\n\\label{tab:finetuned_probe}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Untrained & Llama-2 base & OpenVLA-7B & LIBERO-finetuned \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 80.2\\% & 99.6\\% & 99.7\\% \\\\\nL8 & 98.6\\% & 99.9\\% & 100.0\\% & 100.0\\% \\\\\nL31 & 82.0\\% & 100.0\\% & 100.0\\% & 100.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{L1 Attention Pattern Analysis}\n\\label{sec:attention_pattern}\n\nFigure~\\ref{fig:attention_appendix} shows the per-head L1 attention distribution at the readout token.\nThe three-level gradient (untrained 0/32, Llama-2 base 9/32, VLA-trained 24/32 instruction-dominant heads) shows that language pretraining seeds partial instruction routing and VLA fine-tuning shifts it further toward instruction dominance.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_l1_stacked_bar.pdf}\n\\caption{L1 attention from the readout token across three conditions, per head (sorted by instruction attention fraction). VLA-trained: 24/32 instruction-dominant heads ($57.7\\%$ text attention). Llama-2 base: 9/32 heads ($36.5\\%$). Untrained: 0/32 heads ($11.7\\%$). See Table~\\ref{tab:routing_gradient} for quantitative comparison.}\n\\label{fig:attention_appendix}\n\\end{figure}\n\n\\subsubsection{Multi-Layer Attention Patterns}\n\\label{sec:multilayer_attention}\n\nTable~\\ref{tab:multilayer_attention} shows a 4-layer subset of the full 32-layer attention profile (Figure~\\ref{fig:attention_profile}, main text).\nThe full profile (Figure~\\ref{fig:multilayer_attention}) reveals three qualitatively distinct patterns: the untrained model maintains 0 instruction-dominant heads at all 32 layers; Llama-2 base shows a mid-depth peak (L9--L16: 15--22 heads), consistent with typical autoregressive LM processing depth; VLA fine-tuning produces an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads, intermediate layers 0--11).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_multi_layer_attn.pdf}\n\\caption{Instruction-dominant heads and mean text attention fraction across layers for three conditions. VLA-trained shows elevated values at L1 and L31; Llama-2 base peaks at L16; untrained remains near zero throughout.}\n\\label{fig:multilayer_attention}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\\ref{tab:routing_gradient}) due to threshold boundary effects.}\n\\label{tab:multilayer_attention}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{VLA Trained} & \\multicolumn{2}{c}{Llama-2 base} & \\multicolumn{2}{c}{Untrained} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\nLayer & Heads & Text\\% & Heads & Text\\% & Heads & Text\\% \\\\\n\\midrule\nL1 & \\textbf{24/32} & 57.7 & 9/32 & 36.5 & 0/32 & 11.7 \\\\\nL8 & 4/32 & 46.8 & 8/32 & 48.8 & 0/32 & 7.9 \\\\\nL16 & 10/32 & 48.4 & \\textbf{25/32} & 60.2 & 0/32 & 9.2 \\\\\nL31 & \\textbf{18/32} & 56.3 & 8/32 & 34.9 & 0/32 & 7.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsubsection{Threshold Sensitivity Analysis}\n\\label{sec:threshold_sensitivity}\n\nThe main text defines instruction-dominant heads as those allocating $>50\\%$ attention to instruction tokens.\nTable~\\ref{tab:threshold_sensitivity} shows that the three-condition gradient (untrained $<$ Llama-2 base $<$ VLA-trained) holds across all thresholds from 30\\% to 70\\%; the 50\\% threshold is not a boundary-sensitive choice.\n\n\\begin{table}[h]\n\\centering\n\\caption{Number of instruction-dominant heads at L1 under varying attention thresholds. The three-condition ordering is stable across all thresholds.}\n\\label{tab:threshold_sensitivity}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nThreshold & VLA Trained & Llama-2 base & Untrained \\\\\n\\midrule\n30\\% & 32 & 13 & 0 \\\\\n40\\% & 31 & 10 & 0 \\\\\n50\\% & 24 & 9 & 0 \\\\\n60\\% & 9 & 4 & 0 \\\\\n70\\% & 5 & 3 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L1 Attention Decomposition by Head Group}\n\\label{sec:attention_decomp}\n\nTable~\\ref{tab:attention_decomp} decomposes L1 attention mass at the readout token into three token categories for instruction-dominant and control head groups.\n\n\\begin{table}[h]\n\\centering\n\\caption{Attention mass allocation at Layer 1, averaged across 5 samples. Instruction-dominant heads (defined as $>50\\%$ attention to instruction tokens) allocate 17.5 percentage points more attention to instruction tokens than control heads, with corresponding reductions in vision ($-8.3$pp) and BOS/sink ($-9.2$pp) attention.}\n\\label{tab:attention_decomp}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nHead Group & $N$ & Instruction & Vision & BOS/Other \\\\\n\\midrule\nInstruction-dominant & 24 & 62.4\\% & 18.8\\% & 18.8\\% \\\\\nControl & 8 & 44.9\\% & 27.1\\% & 28.0\\% \\\\\n\\midrule\n$\\Delta$ & --- & $+$17.5pp & $-$8.3pp & $-$9.2pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHead-level instruction attention entropy reaches $99.5\\%$ of the uniform maximum; routing is broadly distributed rather than concentrated in a few heads.\n\n\\paragraph{Per-token attention normalization.}\nThe $57.7\\%$ aggregate text attention in instruction-dominant heads partly reflects token-count imbalance (22 instruction vs.\\ 256 image tokens).\nPer-token normalization reveals a $38.2\\times$ ratio: each instruction token receives $38.2\\times$ the attention of each image token in trained instruction-dominant heads, compared to only $1.5\\times$ in untrained heads (a $25.5\\times$ increase from training).\nInstruction-dominant heads also show lower attention entropy ($0.465$) than non-dominant heads ($0.569$), indicating more concentrated attention distributions.\n\n\\subsection{Per-Dimension Action MAE Under Head Ablation}\n\\label{sec:per_dim_mae}\n\nTable~\\ref{tab:per_dim_mae} extends Table~\\ref{tab:action_shift_perdim} with full per-dimension control-head data and instruction-to-control MAE ratios.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean absolute error per action dimension under L1 head ablation. Translation dimensions ($dx$/$dy$/$dz$) show 3--5$\\times$ larger instruction-to-control ratio than rotation dimensions (1.9--2.6$\\times$); instruction-dominant heads have disproportionate influence on positional control. Gripper (2.07$\\times$) falls between the two groups.}\n\\label{tab:per_dim_mae}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nDimension & Instr.\\ 24h MAE & Control 8h MAE & Ratio \\\\\n\\midrule\n$dx$ & 0.00189 & 0.00037 & 5.09$\\times$ \\\\\n$dy$ & 0.00531 & 0.00125 & 4.26$\\times$ \\\\\n$dz$ & 0.00762 & 0.00243 & 3.14$\\times$ \\\\\n$roll$ & 0.02059 & 0.00785 & 2.62$\\times$ \\\\\n$pitch$ & 0.03071 & 0.01387 & 2.21$\\times$ \\\\\n$yaw$ & 0.03388 & 0.01783 & 1.90$\\times$ \\\\\n$gripper$ & 0.29072 & 0.14072 & 2.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Task $R^2$ Distribution Under L1 Ablation}\n\\label{sec:per_task_r2}\n\nTable~\\ref{tab:per_task_r2} reports per-task action probe $R^2$ at L1 under baseline and 24-head ablation conditions (MLP probe, 5 demonstrations per task).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task action probe $R^2$ at L1 (MLP probe, 5 demos/task). All 10 tasks show positive ablation effect ($\\Delta > 0$): instruction-head ablation uniformly increases action decodability at the entry layer. Mean $\\Delta R^2 = +0.107$; the 50-demo setting (\\S\\ref{sec:learned_routing}) yields a consistent $+0.059$.}\n\\label{tab:per_task_r2}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & Baseline $R^2$ & Ablated $R^2$ & $\\Delta R^2$ \\\\\n\\midrule\nopen middle drawer & 0.197 & 0.221 & $+$0.024 \\\\\nopen top drawer + bowl & 0.265 & 0.340 & $+$0.075 \\\\\npush plate to stove & 0.190 & 0.197 & $+$0.007 \\\\\nput bowl on plate & 0.375 & 0.474 & $+$0.099 \\\\\nput bowl on stove & 0.235 & 0.395 & $+$0.160 \\\\\nput bowl on cabinet & 0.256 & 0.457 & $+$0.201 \\\\\nput cream cheese in bowl & 0.186 & 0.345 & $+$0.159 \\\\\nput wine on rack & 0.189 & 0.424 & $+$0.235 \\\\\nput wine on cabinet & 0.279 & 0.353 & $+$0.074 \\\\\nturn on stove & 0.385 & 0.421 & $+$0.036 \\\\\n\\midrule\nMean $\\pm$ std & $0.256 \\pm 0.070$ & $0.363 \\pm 0.088$ & $+$0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Task Complexity and Routing Dependence}\n\\label{sec:task_complexity}\n\nWe classify tasks as \\emph{instruction-discriminative} when multiple tasks share the same manipulated object(s), requiring instruction content to disambiguate the target action (e.g., ``put bowl on plate'' vs.\\ ``put bowl on stove''); remaining tasks involve unique object-action pairings recoverable from visual context alone.\nTable~\\ref{tab:task_complexity} reports per-task $|\\Delta R^2|$ under both groupings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Task-level L1 ablation effects ($|\\Delta R^2|$) grouped by instruction dependence. \\emph{Primary} (conservative): cream cheese in bowl classified as visual-sufficient ($2.5\\times$, $p = 0.033$). \\emph{Sensitivity} (shared-object criterion): cream cheese reclassified as instruction-discriminative ($6.5\\times$, $p = 0.008$).}\n\\label{tab:task_complexity}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nTask & $|\\Delta R^2|$ & Group \\\\\n\\midrule\nput wine on rack & 0.235 & Instr-disc \\\\\nput bowl on cabinet & 0.201 & Instr-disc \\\\\nput bowl on stove & 0.160 & Instr-disc \\\\\nput bowl on plate & 0.099 & Instr-disc \\\\\nopen top drawer + bowl & 0.075 & Instr-disc \\\\\nput wine on cabinet & 0.074 & Instr-disc \\\\\n\\midrule\nput cream cheese in bowl$^\\dagger$ & 0.159 & Vis-suff \\\\\nturn on stove & 0.036 & Vis-suff \\\\\nopen middle drawer & 0.024 & Vis-suff \\\\\npush plate to stove & 0.007 & Vis-suff \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Primary}: Instr-disc mean $0.141$; Vis-suff mean $0.057$} \\\\\n\\multicolumn{3}{l}{Mann-Whitney $U = 21.0$, $p = 0.033$, ratio $= 2.49\\times$} \\\\\n\\multicolumn{3}{l}{\\textbf{Sensitivity}$^\\dagger$: cream cheese as Instr-disc: $p = 0.008$, $6.5\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-out sensitivity.}\nAll leave-one-out $p$-values remain $\\leq 0.083$, with no single task removal causing a qualitative reversal of the effect direction.\nReclassifying the boundary case (cream cheese in bowl) to the instruction-discriminative group strengthens the result ($p = 0.008$).\n\n\\subsection{Specificity Control: Matched-Size Head Ablation}\n\\label{sec:specificity_control}\n\nTo test whether ablation effects are specific to instruction-dominant heads, we ablate four matched-size subsets of 24 heads at L1: instruction-dominant (highest instruction attention fraction), image-dominant (highest image attention fraction), random (5 seeds), and bottom-24 (lowest instruction attention fraction; overlaps 16/24 heads with the instruction-dominant group).\n\n\\begin{table}[h]\n\\centering\n\\caption{Matched-size ablation controls: trajectory disruption ($d$) from ablating 24-head subsets at L1, ranked by instruction attention fraction. Instruction-dominant heads produce the largest effect, but the modest gap ($8\\%$ over random) indicates distributed, attention-graded routing rather than a dedicated subset.}\n\\label{tab:specificity_control}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition (24 heads) & Cohen's $d$ & 95\\% CI \\\\\n\\midrule\nInstruction-dominant & 0.650 & (reference) \\\\\nRandom (5 seeds) & $0.601 \\pm 0.021$ & $[0.568, 0.622]$ \\\\\nImage-dominant & 0.580 & $[0.547, 0.613]$ \\\\\nBottom-24 & 0.565 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll conditions yield comparable ground-truth MSE ($0.487$--$0.504$ vs.\\ baseline $0.497$), consistent with direction-selective rather than precision-degrading effects.\n",
    "structuredPatch": [
      {
        "oldStart": 179,
        "oldLines": 7,
        "newStart": 179,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[h]",
          " \\centering",
          "-\\caption{Counterfactual instruction analysis. Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}",
          "+\\caption{Counterfactual instruction analysis, computed on 3 representative tasks (cabinet, bowl, plate). Cohen's $d$, token divergence (\\%), and Jaccard token overlap with original instruction. Token novelty ($1 - \\text{Jaccard}$) perfectly predicts divergence ordering (Spearman $\\rho = 1.0$, Pearson $r = 0.957$). L1 ablation included for comparison.}",
          " \\label{tab:counterfactual}",
          " \\small",
          " \\begin{tabular}{lccc}"
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

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_018T5Ha9DyXNSfYLhSQjA9Mw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "a small subset accounts for most performance~\\cite{voita2019}.\nOur Layer-1 attention head analysis extends this tradition",
  "new_string": "a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "e29da500-d0c0-463e-bef4-d38d9901ac19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

_source line 41 · 2026-05-19T11:59:47.930Z_

<details><summary>↩ Tool result · `toolu_018T5Ha9DyXNSfYLhSQjA9Mw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "2cd66d8b-f2f0-4eed-b91e-557ea614ec78",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "a small subset accounts for most performance~\\cite{voita2019}.\nOur Layer-1 attention head analysis extends this tradition",
    "newString": "a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 6,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.",
          " Meng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.",
          " Attention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.",
          "+Michel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.",
          " Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.",
          " ",
          " \\paragraph{Behavioral and mechanistic analysis of VLAs.}"
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_017NPH8bmUmo8eAfFq1AKpCL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWe test this assumption at the representational level",
  "new_string": "A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "85197e66-f530-4717-8fae-8888c2c658c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

_source line 43 · 2026-05-19T11:59:51.108Z_

<details><summary>↩ Tool result · `toolu_017NPH8bmUmo8eAfFq1AKpCL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "6ce123a0-b558-48cd-961c-6de9d6d2e3bb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWe test this assumption at the representational level",
    "newString": "A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 6,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.",
          " This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.",
          " A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.",
          "+While instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.",
          " We test this assumption at the representational level through per-layer, per-token-type decomposition.",
          " ",
          " \\paragraph{Mechanistic interpretability in transformers.}"
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

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01G4DW2p5kANcMGNUbNubuF2`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md",
  "old_string": "25/32",
  "new_string": "24/32"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "b1c150fe-4bd4-4d61-99a9-cbb0c9447828",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpWXSWFLQoCwidjJVBB6zR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39338,
      "cache_read_input_tokens": 25246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39338
      },
      "output_tokens": 8,
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

_source line 45 · 2026-05-19T11:59:51.202Z_

<details><summary>↩ Tool result · `toolu_01G4DW2p5kANcMGNUbNubuF2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "ad9c9360-46a0-4191-904a-c3f6456dc317",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md",
    "oldString": "25/32",
    "newString": "24/32",
    "originalFile": "# Paper Framing — vla-ssd (Plan B → D060 Reframe)\n\n> D048: PI 批准按最大质量重构。A+ 版本保留为 fallback (branch paper-a-plus-backup)。\n> D060: Round 4 weak reject → C1 降为框架, C2 升为唯一核心 claim, C3 降为 qualified observation。\n\n## Target Venue\n- Primary: CoRL 2026\n- Deadline: Abstract May 26, Paper May 29\n- Format: 8 pages + references\n\n## Core Insight\n\nVLA fine-tuning 的核心贡献是学习 deliberate instruction routing：将 instruction attention 从语言预训练的中层模式（L9-L16）reorganize 到 entry-exit 模式（L0-L1 + L31），实现即时 instruction access。这个三条件梯度（untrained 0/32 → pretrained 9/32 → trained 25/32）是 genuine empirical finding，具有 causal evidence 支撑。Token-level specialization（image-blind, readout-hub）是 causal mask 架构保证的性质，我们通过系统实验 verify 和 quantify 其在实际 VLA 中的表现。\n\n## Core Claims (D060 重构：1 核心 + 1 框架 + 1 观察)\n\n### C1: Experimental Framework + Architecture-Verified Specialization [方法论贡献，非 empirical finding]\n**重新定位（D060）**: Token-level specialization 是 causal mask 的数学必然（image tokens 在序列中先于 instruction tokens，无法 attend to instructions）+ frozen encoder 不接收 instruction input。论文贡献不是\"发现\"这一点，而是：\n- **(a) 系统实验框架**：factorial design (trained/pretrained/untrained × instruction presence) + 四种互补分析方法（cross-instruction probe + attention + RSA + MLP probe），适用于任何 decoder-only VLA\n- **(b) 量化验证**：即使 residual stream 理论上可以 leak information，image tokens 在实际模型的全部 32 层均保持 chance（10%）。这不是 trivial——frozen encoder 权重与 LLM 权重共享 residual stream，验证了 no leakage\n- **(c) 训练差异的量化**：untrained readout L1=100% 但 L31=82%（信号衰减）vs trained 100% 全程稳定——framework 揭示了训练影响 routing robustness 而非 routing existence\n\nKey evidence (unchanged):\n- Cross-instruction probe: same frame × 10 instructions → 10-way classification\n- Dense L0-L32: image_mean = chance at ALL layers\n- LOOCV: 100%±0.00 trained, decaying untrained\n- **承认**: 10-way classification 本身 trivially easy（untrained L1 也 100%），贡献在于 framework + 三条件对比揭示的 routing 差异\n\n### C2: Three Qualitatively Different Routing Strategies — VLA Fine-tuning Achieves Immediate Dedicated Routing\n三条件揭示三种定性不同的 routing 模式：\n\n**L1 Attention Routing (heads + attention fraction):**\n- **Untrained (random init)**: 0/32 heads, 12% text attention\n- **Llama-2 base (pretrained, no VLA)**: 9/32 heads, 36.5% text attention\n- **VLA Trained**: 25/32 heads, 58% text attention\n\n**Full-Layer Probe Profile (instruction classification accuracy):**\n- **Trained**: L1=99.6% → 全程 100% — \"即时路由 + 完全稳定\"\n- **Llama-2 base**: L1=80.2% → L2=98.7% → L5+=100% — \"渐进建立 + 稳定维持\"\n- **Untrained**: L1=100% → L8=98.6% → L31=82% — \"偶然路由 + 逐渐遗忘\"\n\n**VLA Fine-tuning 的独特贡献（精��化）：**\n1. **即时性**：L1 即达 99.6%（vs pretrained 需 5 层才饱和）\n2. **头数专用化**：25/32 heads instruction-dominant（vs pretrained 9/32）\n3. **不是**深层稳定性 — 稳定性来自 pretrained weights（pretrained 也不衰减）\n\n**深层���减只发生在 random init**：说明结构化的 pretrained 表示（无论是否经过 VLA 训练）都能维持 instruction signal；random weights 的噪声累积导致信号退化。\n\n**Full 32-Layer Attention Profile（D054 升级，dense evidence）：**\n- **Untrained**: 全 32 层 × 所有 head = 0 instruction-dominant。完全无语言处理能力。\n- **Llama-2 base**: 倒U型 — L0-L4 低(0-10 heads) → L9-L16 高峰(15-22 heads) → L31 回落(8)。经典 LM pattern：中层做深度语义处理。\n- **VLA Trained**: 书挡型 — L0-L1 高峰(21-24 heads) → L2-L30 低谷(0-11) → L31 再次高峰(18)。入口获取 instruction + 出口条件化 action output。\n\n**C2 Claim（D073 reframe: open-loop functional sensitivity）**: VLA fine-tuning **shifts** instruction attention from mid-layer processing (Llama-2 base: 15-22/32 heads at L10-L17) to entry-layer routing (L0-L1: 21-24/32) and exit-layer re-engagement (L31: 18/32)。Instruction-conditioned action generation operates through **distributed L1 routing** where instruction-attention fraction predicts per-head contribution magnitude (specificity ratio 1.08x at action output)。Routing modulates output direction (d=0.65) without systematic quality degradation (ΔMSE≈0), consistent with an information-computation dissociation (Hewitt & Liang 2019)。不能 claim instruction heads \"uniquely responsible\" 或 \"confirms routing function\"——用 \"open-loop functional sensitivity\" + \"support\" 而非 \"confirm\"。可 claim \"disproportionate contribution\" + \"attention-ordered routing\"。Section 标题用 \"Open-loop functional sensitivity\"，正文用 \"shifts...from...to...\" + \"distributed routing\"。\n\nKey evidence:\n- **32-layer dense attention profile**: Trained bookend (L0-1: 21-24, L31: 18) vs Llama2base inverted-U (L9-16: 15-22)\n- Three-condition full-layer probe: trained flat 100%; llama2base saturates L5+100%; untrained decays L1:100%→L31:82%\n- L1 attention gradient: 0/32 → 9/32 → 25/32 heads\n- VLA-specific contributions: (1) temporal reorganization from mid-peak to bookend, (2) immediacy (L1: 80.2→99.6%), (3) head dedication (9→25 at L1)\n- **Per-token normalization**: 38.2x text/image ratio (trained instr-dom) vs 1.5x (untrained) — eliminates token-count confound\n- **Trajectory-level d**: all conditions d>2.0 (token-level is conservative ~4x underestimate)\n- **GT error**: ΔMSE≈0 (ablation redirects outputs without degrading GT accuracy) — supports information-computation dissociation\n- **Token overlap**: Spearman ρ=1.0 between token novelty and d — lexical/positional sensitivity, not semantic distance\n- **LOO sensitivity**: all leave-one-out p ≤ 0.083, no qualitative reversal; cream cheese reclassification p=0.008\n- **4-condition training trajectory (D075)**: untrained(0) → llama2(9) → bridge-vla(24) → libero-finetuned(22) at L1。Entry routing 稳定，但 L31 exit engagement 18→0（entry-exit → entry-only sharpening）。Probe accuracy 不变（L31 仍 100%），确认 attention-representation dissociation\n- **OXE training diversity**: openvla-7b 在 Open X-Embodiment 970K episodes（多平台多任务）上训练，L1 routing 不是 LIBERO-specific\n\n### C3: Vision Encoder Geometry Observation [降为 qualified observation，非 core claim]\n**重新定位（D060）**: RSA inverted-U 的 rise phase 极小（Δρ=0.016, CI 待补），CKA 完全反转 RSA ordering（untrained > trained > DINOv2），\"non-monotonic refinement\" 仅在 RSA 下成立。DINOv2 ranking 在 CKA 下不成立（CKA 中 DINOv2 排名最低）。\n\n**保留为 observation 的理由**：\n- **Decline phase 也是 RSA-specific**：L12→L32 Δρ=-0.206 远大于 rise phase，但 CKA 单调递增无 decline。不能 claim decline 是 metric-robust。\n- **R² inverted-U 是 metric-independent 的**：functional probe 确认 L8-L13 peak（0.655-0.678），之后下降。这是 C3 最强的 evidence，不依赖 RSA/CKA 选择。\n- **Metric divergence 本身是 honest observation**：\"non-monotonic under RSA, monotonic under CKA\"\n- **DINOv2 RSA ranking**：在 RSA 下 robust，但必须加 \"under RSA\" qualifier\n\n**写法要求**：\n- Abstract/Intro 中\"non-monotonic refinement\"加 \"under RSA\" qualifier\n- DINOv2 \"highest geometric foundation\" 加 \"as measured by RSA\"\n- best-vs-best Δ=+0.017 明确标 n.s.（CI includes 0）\n- Discussion 加 metric-dependence caveat（CKA 反转在正文中 qualify，不只在 appendix）\n\nKey evidence (unchanged but qualified):\n- Cross-encoder RSA table — **加 \"under RSA\" qualifier**\n- Per-layer RSA + R² profiles — **rise phase CI 待补报**\n- Cross-benchmark replication — still holds\n- **CKA divergence** — 必须在正文 acknowledge\n\n## Story Spine (D060 Reframe)\n\n- **Problem**: VLAs fine-tune LLMs on robot data, but how training reshapes instruction routing and information integration at the token level remains uncharacterized.\n- **Existing approaches & gaps**: Prior behavioral studies (Grant et al. 2026, Haon et al. 2025) found visual dominance and instruction underutilization, but did not decompose the representational roles of different token positions or explain how training reshapes information flow through the LLM.\n- **Our framing**: We provide a systematic experimental framework for token-level analysis of VLAs. Using factorial controls (trained/pretrained/untrained) and four complementary methods, we find that VLA fine-tuning's primary contribution is learning a distinctive instruction routing strategy: shifting attention from mid-depth processing (inherited from language pretraining) to an entry-exit pattern, enabling immediate instruction access.\n- **Headline results**: (1) [Framework] Architecture-expected token specialization is verified and quantified across 32 layers and three conditions. (2) [Core finding] Three qualitatively distinct routing strategies revealed: untrained (0/32 heads, no routing) → pretrained (9/32, mid-depth) → trained (25/32, entry-exit); instruction-conditioned action generation operates through distributed L1 routing where instruction-attention fraction predicts per-head contribution magnitude (dose-response monotonic d=0.48→0.64; counterfactual graduated d=0.63→0.97; size-matched specificity ratio 1.08x). (3) [Observation] Under RSA, vision encoder geometry follows an inverted-U through LLM layers with a substantial decline phase; functional probes confirm peak at L8-L13.\n- **Practical implications**: (1) Architecture design should optimize instruction-to-readout routing. (2) Under RSA, self-supervised encoders provide the strongest action-relevant geometry (qualified by CKA divergence). (3) L8-L13 functional peak identifies a potential early-exit window.\n\n## Key Numerical Benchmarks (unchanged from A+)\n\n### Cross-Instruction Probe (C1 + C2 核心实验)\n\n| Condition | L0 | L1 | L2 | L5 | L8 | L16 | L24 | L31 |\n|-----------|----|----|----|----|----|----|-----|-----|\n| Trained last_preaction | 10% | 99.6% | 100% | 100% | 100% | 100% | 100% | 100% |\n| **Llama-2 base last_preaction** | **10%** | **80.2%** | **98.7%** | **100%** | **100%** | **100%** | **100%** | **100%** |\n| Untrained last_preaction | 10% | 100% | 100% | 99.x% | 98.6% | 92.3% | 86.4% | 82.0% |\n| Trained image_mean | 10% | — | — | — | 10% | 10% | 10% | 9.6% |\n| DINOv2 | 10% | — | — | — | — | — | — | — |\n\nLOOCV (10-fold): Trained 100.00±0.00 (L8-L31), Untrained 96.64±7.07 → 84.76±11.59\n\n### L1 Attention Pattern (C2 mechanistic evidence — three-condition)\n\n| Metric | Untrained | Llama-2 Base | VLA Trained |\n|--------|-----------|--------------|-------------|\n| Attention to text/instruction | 11.7% | 36.5% | 57.7% |\n| Attention to image | 87.8% | 61.7% | 21.3% |\n| Instruction-dominant heads (>50%) | 0/32 | 9/32 | 25/32 |\n\n### Training Effect Size Summary\n\n| Metric | Trained | Untrained | Δ |\n|--------|---------|-----------|---|\n| RSA peak (image_mean) | 0.628 (L12) | 0.612 (L0) | +0.017 |\n| R² peak (last_preaction) | 0.678 (L13) | 0.609 (L32) | +0.069 |\n| Inst. routing L31 | 100% | 82% | +18pp |\n| Inst. attention L1 | 58% | 12% | +46pp |\n| Progress classification | 86.3% (L20) | 85.3% (L4) | +1pp |\n\n### Cross-Encoder RSA (C3)\n\n| Source | RSA |\n|--------|-----|\n| DINO cls_token | 0.692 |\n| DINO patch_mean | 0.631 |\n| SigLIP+Projector | 0.615 |\n| VLA trained peak (L12) | 0.628 |\n| CLIP ViT-L | 0.557 |\n\n## Anticipated Reviewer Concerns (D060 updated — Round 4 已验证)\n\n### RC1: \"C1 is trivial — causal mask guarantees it\" [Round 4 N1, ACCEPTED]\n**Response**: We accept this. Paper now explicitly acknowledges causal mask as structural source. C1 is repositioned as methodological framework + empirical verification, not novel finding. The framework itself (factorial design + 4 methods) has reusable value for VLA analysis.\n\n### RC2: \"RSA inverted-U is metric-dependent, CKA reverses\" [Round 4 N2, PARTIALLY ACCEPTED]\n**Response**: Rise phase (Δρ=+0.016) acknowledged as small and qualified with CI. CKA divergence discussed in main text, not just appendix. Decline phase (Δρ=-0.206) is robust across metrics. DINOv2 ranking qualified with \"under RSA\". C3 downgraded from core claim to observation.\n\n### RC3: \"Ablation 5 demos underfitting\" [Round 4 N3, ACCEPTED + RERUN]\n**Response**: 50-demo rerun in progress. If effect holds → underfitting confound ruled out. Non-dominant-8 control addresses generic regularization concern. Results TBD.\n\n### RC4: \"Only tested on one VLA (OpenVLA)\"\n**Response**: Scope explicitly limited. C1 generalizes via causal mask for any decoder-only VLA. C2 routing pattern is testable prediction for other architectures. Future work lists RT-2, π₀.\n\n### RC5: \"Practical implications speculative / frozen encoder confound\" [Round 4 W4]\n**Response**: Encoder ranking qualified with \"under RSA\" and \"within fixed encoder configuration.\" Discussion adds explicit caveat that claims about encoder quality require across-encoder experiments. Routing optimization remains well-supported by three-condition gradient.\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " ",
          " ## Core Insight",
          " ",
          "-VLA fine-tuning 的核心贡献是学习 deliberate instruction routing：将 instruction attention 从语言预训练的中层模式（L9-L16）reorganize 到 entry-exit 模式（L0-L1 + L31），实现即时 instruction access。这个三条件梯度（untrained 0/32 → pretrained 9/32 → trained 25/32）是 genuine empirical finding，具有 causal evidence 支撑。Token-level specialization（image-blind, readout-hub）是 causal mask 架构保证的性质，我们通过系统实验 verify 和 quantify 其在实际 VLA 中的表现。",
          "+VLA fine-tuning 的核心贡献是学习 deliberate instruction routing：将 instruction attention 从语言预训练的中层模式（L9-L16）reorganize 到 entry-exit 模式（L0-L1 + L31），实现即时 instruction access。这个三条件梯度（untrained 0/32 → pretrained 9/32 → trained 24/32）是 genuine empirical finding，具有 causal evidence 支撑。Token-level specialization（image-blind, readout-hub）是 causal mask 架构保证的性质，我们通过系统实验 verify 和 quantify 其在实际 VLA 中的表现。",
          " ",
          " ## Core Claims (D060 重构：1 核心 + 1 框架 + 1 观察)",
          " "
        ]
      },
      {
        "oldStart": 32,
        "oldLines": 7,
        "newStart": 32,
        "newLines": 7,
        "lines": [
          " **L1 Attention Routing (heads + attention fraction):**",
          " - **Untrained (random init)**: 0/32 heads, 12% text attention",
          " - **Llama-2 base (pretrained, no VLA)**: 9/32 heads, 36.5% text attention",
          "-- **VLA Trained**: 25/32 heads, 58% text attention",
          "+- **VLA Trained**: 24/32 heads, 58% text attention",
          " ",
          " **Full-Layer Probe Profile (instruction classification accuracy):**",
          " - **Trained**: L1=99.6% → 全程 100% — \"即时路由 + 完全稳定\""
        ]
      },
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " ",
          " **VLA Fine-tuning 的独特贡献（精��化）：**",
          " 1. **即时性**：L1 即达 99.6%（vs pretrained 需 5 层才饱和）",
          "-2. **头数专用化**：25/32 heads instruction-dominant（vs pretrained 9/32）",
          "+2. **头数专用化**：24/32 heads instruction-dominant（vs pretrained 9/32）",
          " 3. **不是**深层稳定性 — 稳定性来自 pretrained weights（pretrained 也不衰减）",
          " ",
          " **深层���减只发生在 random init**：说明结构化的 pretrained 表示（无论是否经过 VLA 训练）都能维持 instruction signal；random weights 的噪声累积导致信号退化。"
        ]
      },
      {
        "oldStart": 56,
        "oldLines": 7,
        "newStart": 56,
        "newLines": 7,
        "lines": [
          " Key evidence:",
          " - **32-layer dense attention profile**: Trained bookend (L0-1: 21-24, L31: 18) vs Llama2base inverted-U (L9-16: 15-22)",
          " - Three-condition full-layer probe: trained flat 100%; llama2base saturates L5+100%; untrained decays L1:100%→L31:82%",
          "-- L1 attention gradient: 0/32 → 9/32 → 25/32 heads",
          "+- L1 attention gradient: 0/32 → 9/32 → 24/32 heads",
          " - VLA-specific contributions: (1) temporal reorganization from mid-peak to bookend, (2) immediacy (L1: 80.2→99.6%), (3) head dedication (9→25 at L1)",
          " - **Per-token normalization**: 38.2x text/image ratio (trained instr-dom) vs 1.5x (untrained) — eliminates token-count confound",
          " - **Trajectory-level d**: all conditions d>2.0 (token-level is conservative ~4x underestimate)"
        ]
      },
      {
        "oldStart": 92,
        "oldLines": 7,
        "newStart": 92,
        "newLines": 7,
        "lines": [
          " - **Problem**: VLAs fine-tune LLMs on robot data, but how training reshapes instruction routing and information integration at the token level remains uncharacterized.",
          " - **Existing approaches & gaps**: Prior behavioral studies (Grant et al. 2026, Haon et al. 2025) found visual dominance and instruction underutilization, but did not decompose the representational roles of different token positions or explain how training reshapes information flow through the LLM.",
          " - **Our framing**: We provide a systematic experimental framework for token-level analysis of VLAs. Using factorial controls (trained/pretrained/untrained) and four complementary methods, we find that VLA fine-tuning's primary contribution is learning a distinctive instruction routing strategy: shifting attention from mid-depth processing (inherited from language pretraining) to an entry-exit pattern, enabling immediate instruction access.",
          "-- **Headline results**: (1) [Framework] Architecture-expected token specialization is verified and quantified across 32 layers and three conditions. (2) [Core finding] Three qualitatively distinct routing strategies revealed: untrained (0/32 heads, no routing) → pretrained (9/32, mid-depth) → trained (25/32, entry-exit); instruction-conditioned action generation operates through distributed L1 routing where instruction-attention fraction predicts per-head contribution magnitude (dose-response monotonic d=0.48→0.64; counterfactual graduated d=0.63→0.97; size-matched specificity ratio 1.08x). (3) [Observation] Under RSA, vision encoder geometry follows an inverted-U through LLM layers with a substantial decline phase; functional probes confirm peak at L8-L13.",
          "+- **Headline results**: (1) [Framework] Architecture-expected token specialization is verified and quantified across 32 layers and three conditions. (2) [Core finding] Three qualitatively distinct routing strategies revealed: untrained (0/32 heads, no routing) → pretrained (9/32, mid-depth) → trained (24/32, entry-exit); instruction-conditioned action generation operates through distributed L1 routing where instruction-attention fraction predicts per-head contribution magnitude (dose-response monotonic d=0.48→0.64; counterfactual graduated d=0.63→0.97; size-matched specificity ratio 1.08x). (3) [Observation] Under RSA, vision encoder geometry follows an inverted-U through LLM layers with a substantial decline phase; functional probes confirm peak at L8-L13.",
          " - **Practical implications**: (1) Architecture design should optimize instruction-to-readout routing. (2) Under RSA, self-supervised encoders provide the strongest action-relevant geometry (qualified by CKA divergence). (3) L8-L13 functional peak identifies a potential early-exit window.",
          " ",
          " ## Key Numerical Benchmarks (unchanged from A+)"
        ]
      },
      {
        "oldStart": 115,
        "oldLines": 7,
        "newStart": 115,
        "newLines": 7,
        "lines": [
          " |--------|-----------|--------------|-------------|",
          " | Attention to text/instruction | 11.7% | 36.5% | 57.7% |",
          " | Attention to image | 87.8% | 61.7% | 21.3% |",
          "-| Instruction-dominant heads (>50%) | 0/32 | 9/32 | 25/32 |",
          "+| Instruction-dominant heads (>50%) | 0/32 | 9/32 | 24/32 |",
          " ",
          " ### Training Effect Size Summary",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
All 8 edits succeeded. Now I need to add the bib entries to references.bib. I need to add:
1. michel2019sixteen
2. wei2022finetuned
3. ouyang2022training

Let me add them at the end of the references.bib file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "cd92c9cc-e1d1-43d2-ae11-abd654241f4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pU3mEYqUspKcEsFWbbWT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11933,
      "cache_read_input_tokens": 64584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11933
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

_source line 47_

Now adding the 3 bib entries to references.bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "aa606c66-7001-4e21-be23-56154d45dc89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pU3mEYqUspKcEsFWbbWT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11933,
      "cache_read_input_tokens": 64584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11933
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01AuLbxRddDkosPQmK9gbXi1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "old_string": "@inproceedings{ghosh2024_octo,\n  title     = {Octo: An Open-Source Generalist Robot Policy},\n  author    = {Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and Mees, Oier and Dasari, Sudeep and Hejna, Joey and Kreiman, Tobias and Xu, Charles and You, Jianlan and Wu, Joey and Finn, Chelsea and Kumar, Aviral and Hausman, Karol and Levine, Sergey},\n  booktitle = {Robotics: Science and Systems},\n  year      = {2024},\n}",
  "new_string": "@inproceedings{ghosh2024_octo,\n  title     = {Octo: An Open-Source Generalist Robot Policy},\n  author    = {Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and Mees, Oier and Dasari, Sudeep and Hejna, Joey and Kreiman, Tobias and Xu, Charles and You, Jianlan and Wu, Joey and Finn, Chelsea and Kumar, Aviral and Hausman, Karol and Levine, Sergey},\n  booktitle = {Robotics: Science and Systems},\n  year      = {2024},\n}\n\n% === Attention Head Pruning ===\n\n@inproceedings{michel2019sixteen,\n  title     = {Are Sixteen Heads Really Better than One?},\n  author    = {Michel, Paul and Levy, Omer and Neubig, Graham},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n% === Instruction Tuning ===\n\n@inproceedings{wei2022finetuned,\n  title     = {Finetuned Language Models Are Zero-Shot Learners},\n  author    = {Wei, Jason and Bosma, Maarten and Zhao, Vincent and Guu, Kelvin and Yu, Adams Wei and Lester, Brian and Du, Nan and Dai, Andrew M and Le, Quoc V},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n}\n\n@inproceedings{ouyang2022training,\n  title     = {Training language models to follow instructions with human feedback},\n  author    = {Ouyang, Long and Wu, Jeffrey and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "1b917fa9-5594-4dcb-bec7-79edd8693641",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pU3mEYqUspKcEsFWbbWT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11933,
      "cache_read_input_tokens": 64584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11933
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

_source line 49 · 2026-05-19T12:00:06.295Z_

<details><summary>↩ Tool result · `toolu_01AuLbxRddDkosPQmK9gbXi1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "24346931-4caf-4286-8953-dd9cf0115916",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "oldString": "@inproceedings{ghosh2024_octo,\n  title     = {Octo: An Open-Source Generalist Robot Policy},\n  author    = {Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and Mees, Oier and Dasari, Sudeep and Hejna, Joey and Kreiman, Tobias and Xu, Charles and You, Jianlan and Wu, Joey and Finn, Chelsea and Kumar, Aviral and Hausman, Karol and Levine, Sergey},\n  booktitle = {Robotics: Science and Systems},\n  year      = {2024},\n}",
    "newString": "@inproceedings{ghosh2024_octo,\n  title     = {Octo: An Open-Source Generalist Robot Policy},\n  author    = {Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and Mees, Oier and Dasari, Sudeep and Hejna, Joey and Kreiman, Tobias and Xu, Charles and You, Jianlan and Wu, Joey and Finn, Chelsea and Kumar, Aviral and Hausman, Karol and Levine, Sergey},\n  booktitle = {Robotics: Science and Systems},\n  year      = {2024},\n}\n\n% === Attention Head Pruning ===\n\n@inproceedings{michel2019sixteen,\n  title     = {Are Sixteen Heads Really Better than One?},\n  author    = {Michel, Paul and Levy, Omer and Neubig, Graham},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n% === Instruction Tuning ===\n\n@inproceedings{wei2022finetuned,\n  title     = {Finetuned Language Models Are Zero-Shot Learners},\n  author    = {Wei, Jason and Bosma, Maarten and Zhao, Vincent and Guu, Kelvin and Yu, Adams Wei and Lester, Brian and Du, Nan and Dai, Andrew M and Le, Quoc V},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n}\n\n@inproceedings{ouyang2022training,\n  title     = {Training language models to follow instructions with human feedback},\n  author    = {Ouyang, Long and Wu, Jeffrey and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n}",
    "originalFile": "% === VLA / Architecture ===\n\n@article{kim2024_openvla,\n  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},\n  journal   = {arXiv preprint arXiv:2406.09246},\n  year      = {2024},\n}\n\n@article{karamcheti2024,\n  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},\n  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},\n  journal   = {arXiv preprint arXiv:2402.07865},\n  year      = {2024},\n}\n\n@article{brohan2023_rt2,\n  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  journal   = {arXiv preprint arXiv:2307.15818},\n  year      = {2023},\n}\n\n% === Benchmark ===\n\n@inproceedings{liu2023_libero,\n  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Representation Analysis Methods ===\n\n@article{kriegeskorte2008,\n  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},\n  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter},\n  journal   = {Frontiers in Systems Neuroscience},\n  volume    = {2},\n  pages     = {4},\n  year      = {2008},\n  publisher = {Frontiers},\n}\n\n@inproceedings{kornblith2019,\n  title     = {Similarity of Neural Network Representations Revisited},\n  author    = {Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2019},\n}\n\n@inproceedings{alain2017,\n  title     = {Understanding Intermediate Layers Using Linear Classifier Probes},\n  author    = {Alain, Guillaume and Bengio, Yoshua},\n  booktitle = {International Conference on Learning Representations (ICLR), Workshop Track},\n  year      = {2017},\n}\n\n% === Vision Encoders ===\n\n@inproceedings{zhai2023_siglip,\n  title     = {Sigmoid Loss for Language Image Pre-Training},\n  author    = {Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle = {International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n}\n\n@article{oquab2024_dinov2,\n  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},\n  author    = {Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and Vo, Huy and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and others},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2024},\n}\n\n@inproceedings{radford2021_clip,\n  title     = {Learning Transferable Visual Models From Natural Language Supervision},\n  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2021},\n}\n\n% === Domain-Specific ===\n\n@article{grant2026,\n  title     = {Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models},\n  author    = {Grant, Bryce and Zhao, Xijia and Wang, Peng},\n  journal   = {arXiv preprint arXiv:2603.19233},\n  year      = {2026},\n}\n\n@article{haon2025,\n  title     = {Mechanistic Interpretability for Steering Vision-Language-Action Models},\n  author    = {H{\\\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},\n  journal   = {arXiv preprint arXiv:2509.00328},\n  year      = {2025},\n}\n\n% === Behavioral Analysis of VLAs ===\n\n@article{hou2026,\n  title     = {{LangGap}: Diagnosing and Closing the Language Gap in Vision-Language-Action Models},\n  author    = {Hou, Yuchen and Zhao, Lin},\n  journal   = {arXiv preprint arXiv:2603.00592},\n  year      = {2026},\n}\n\n@article{fei2025,\n  title     = {{LIBERO-Plus}: In-depth Robustness Analysis of Vision-Language-Action Models},\n  author    = {Fei, Senyu and Wang, Siyin and Shi, Junhao and Dai, Zihao and Cai, Jikun and Qian, Pengfang and Ji, Li and He, Xinzhe and Zhang, Shiduo and Fei, Zhaoye and Fu, Jinlan and Gong, Jingjing and Qiu, Xipeng},\n  journal   = {arXiv preprint arXiv:2510.13626},\n  year      = {2025},\n}\n\n% === Mechanistic Interpretability of VLAs ===\n\n@article{swann2026,\n  title     = {Sparse Autoencoders Reveal Interpretable and Steerable Features in {VLA} Models},\n  author    = {Swann, Aiden and McGranahan, Lachlain and Buurmeijer, Hugo and Kennedy, Monroe and Schwager, Mac},\n  journal   = {arXiv preprint arXiv:2603.19183},\n  year      = {2026},\n}\n\n@article{buurmeijer2026,\n  title     = {Observing and Controlling Features in Vision-Language-Action Models},\n  author    = {Buurmeijer, Hugo and Amo Alonso, Carmen and Swann, Aiden and Pavone, Marco},\n  journal   = {arXiv preprint arXiv:2603.05487},\n  year      = {2026},\n}\n\n@article{lu2025,\n  title     = {Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture},\n  author    = {Lu, Hong and Li, Hengxu and Shahani, Prithviraj Singh and Herbers, Stephanie and Scheutz, Matthias},\n  journal   = {arXiv preprint arXiv:2502.04558},\n  year      = {2025},\n}\n\n@article{molinari2025,\n  title     = {Emergent World Representations in {OpenVLA}},\n  author    = {Molinari, Marco and Nevali, Leonardo and Navani, Saharsha and Younis, Omar G.},\n  journal   = {arXiv preprint arXiv:2509.24559},\n  year      = {2025},\n}\n\n% === Probing Methods ===\n\n@article{belinkov2022,\n  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},\n  author    = {Belinkov, Yonatan},\n  journal   = {Computational Linguistics},\n  volume    = {48},\n  number    = {1},\n  pages     = {207--219},\n  year      = {2022},\n}\n\n% === Causal Tracing and Per-Layer Analysis ===\n\n@inproceedings{meng2022_rome,\n  title     = {Locating and Editing Factual Associations in {GPT}},\n  author    = {Meng, Kevin and Bau, David and Andonian, Alex and Belinkov, Yonatan},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2022},\n}\n\n@article{belrose2023_tunedlens,\n  title     = {Eliciting Latent Predictions from Transformers with the Tuned Lens},\n  author    = {Belrose, Nora and Furman, Zach and Smith, Logan and Biderman, Stella and Steinhardt, Jacob and Frankle, Jonathan},\n  journal   = {arXiv preprint arXiv:2303.08112},\n  year      = {2023},\n}\n\n% === Mechanistic Interpretability in Transformers ===\n\n@article{elhage2021,\n  title     = {A Mathematical Framework for Transformer Circuits},\n  author    = {Elhage, Nelson and Nanda, Neel and Olsson, Catherine and Henighan, Tom and Joseph, Nicholas and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and DasSarma, Nova and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},\n  journal   = {Transformer Circuits Thread},\n  year      = {2021},\n  url       = {https://transformer-circuits.pub/2021/framework/index.html},\n}\n\n@article{olsson2022,\n  title     = {In-context Learning and Induction Heads},\n  author    = {Olsson, Catherine and Elhage, Nelson and Nanda, Neel and Joseph, Nicholas and DasSarma, Nova and Henighan, Tom and Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and Conerly, Tom and Drain, Dawn and Ganguli, Deep and Hatfield-Dodds, Zac and Hernandez, Danny and Johnston, Scott and Jones, Andy and Kernion, Jackson and Lovitt, Liane and Ndousse, Kamal and Amodei, Dario and Brown, Tom and Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},\n  journal   = {arXiv preprint arXiv:2209.11895},\n  year      = {2022},\n}\n\n@inproceedings{wang2023_ioi,\n  title     = {Interpretability in the Wild: a Circuit for Indirect Object Identification in {GPT-2} Small},\n  author    = {Wang, Kevin and Variengien, Alexandre and Conmy, Arthur and Shlegeris, Buck and Steinhardt, Jacob},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2023},\n}\n\n@inproceedings{conmy2023,\n  title     = {Towards Automated Circuit Discovery for Mechanistic Interpretability},\n  author    = {Conmy, Arthur and Mavor-Parker, Augustine N. and Lynch, Aengus and Heimersheim, Stefan and Garriga-Alonso, Adri{\\`a}},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Attention Analysis ===\n\n@inproceedings{clark2019,\n  title     = {What Does {BERT} Look At? {An} Analysis of {BERT}'s Attention},\n  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},\n  year      = {2019},\n}\n\n@inproceedings{vig2019,\n  title     = {Analyzing the Structure of Attention in a Transformer Language Model},\n  author    = {Vig, Jesse and Belinkov, Yonatan},\n  booktitle = {Proceedings of the 2019 ACL Workshop BlackboxNLP},\n  year      = {2019},\n}\n\n@inproceedings{voita2019,\n  title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n  author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n}\n\n% === Token-Level Functional Specialization ===\n\n@inproceedings{dosovitskiy2021,\n  title     = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},\n  author    = {Dosovitskiy, Alexey and Beyer, Lucas and Kolesnikov, Alexander and Weissenborn, Dirk and Zhai, Xiaohua and Unterthiner, Thomas and Dehghani, Mostafa and Minderer, Matthias and Heigold, Georg and Gelly, Sylvain and Uszkoreit, Jakob and Houlsby, Neil},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2021},\n}\n\n@inproceedings{darcet2024,\n  title     = {Vision Transformers Need Registers},\n  author    = {Darcet, Timoth{\\'e}e and Oquab, Maxime and Mairal, Julien and Bojanowski, Piotr},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n}\n\n@inproceedings{geva2021,\n  title     = {Transformer Feed-Forward Layers Are Key-Value Memories},\n  author    = {Geva, Mor and Schuster, Roei and Berant, Jonathan and Levy, Omer},\n  booktitle = {Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2021},\n}\n\n@inproceedings{tenney2019,\n  title     = {{BERT} Rediscovers the Classical {NLP} Pipeline},\n  author    = {Tenney, Ian and Das, Dipanjan and Pavlick, Ellie},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2019},\n}\n\n% === Representation Similarity Methods ===\n\n@inproceedings{raghu2017,\n  title     = {{SVCCA}: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability},\n  author    = {Raghu, Maithra and Gilmer, Justin and Yosinski, Jason and Sohl-Dickstein, Jascha},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2017},\n}\n\n@inproceedings{morcos2018,\n  title     = {Insights on Representational Similarity in Neural Networks with Canonical Correlation},\n  author    = {Morcos, Ari S. and Raghu, Maithra and Bengio, Samy},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2018},\n}\n\n@inproceedings{hewitt2019,\n  title     = {A Structural Probe for Finding Syntax in Word Representations},\n  author    = {Hewitt, John and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2019},\n}\n\n% === VLM Token-Level Analysis ===\n\n@inproceedings{neo2025,\n  title     = {Towards Understanding Multi-Task Learning (Generalization) of {LLMs} via Detecting and Exploring Task-Specific Neurons},\n  author    = {Neo, Yifan and Wu, Jingcheng and Hooi, Bryan},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n}\n\n% === Representation Similarity (ViT) ===\n\n@inproceedings{raghu2021,\n  title     = {Do Vision Transformers See Like Convolutional Neural Networks?},\n  author    = {Raghu, Maithra and Unterthiner, Thomas and Kornblith, Simon and Zhang, Chiyuan and Dosovitskiy, Alexey},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2021},\n}\n\n% === Probe Methodology ===\n\n@inproceedings{hewitt2019control,\n  title     = {Designing and Interpreting Probes with Control Tasks},\n  author    = {Hewitt, John and Liang, Percy},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages     = {2733--2743},\n  year      = {2019},\n  doi       = {10.18653/v1/D19-1275},\n}\n\n% === RSA Toolbox ===\n\n@article{nili2014toolbox,\n  title     = {A Toolbox for Representational Similarity Analysis},\n  author    = {Nili, Hamed and Wingfield, Cai and Walther, Alexander and Su, Li and Marslen-Wilson, William and Kriegeskorte, Nikolaus},\n  journal   = {PLoS Computational Biology},\n  volume    = {10},\n  number    = {4},\n  pages     = {e1003553},\n  year      = {2014},\n  doi       = {10.1371/journal.pcbi.1003553},\n}\n\n% === Mechanistic Interpretability ===\n\n@misc{bills2023language,\n  title     = {Language Models Can Explain Neurons in Language Models},\n  author    = {Bills, Steven and Cammarata, Nick and Mossing, Dan and Tillman, Henk and Gao, Leo and Goh, Gabriel and Sutskever, Ilya and Leike, Jan and Wu, Jeff and Saunders, William},\n  year      = {2023},\n  howpublished = {OpenAI Blog},\n  url       = {https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html},\n}\n\n@article{templeton2024scaling,\n  title     = {Scaling Monosemanticity: Extracting Interpretable Features from {C}laude 3 {S}onnet},\n  author    = {Templeton, Adly and Conerly, Tom and Marcus, Jonathan and Lindsey, Jack and Bricken, Trenton and Chen, Brian and Pearce, Adam and Citro, Craig and Ameisen, Emmanuel and Jones, Andy and others},\n  journal   = {Transformer Circuits Thread},\n  year      = {2024},\n  url       = {https://transformer-circuits.pub/2024/scaling-monosemanticity/},\n}\n\n% === LLM Internal Probing ===\n\n@misc{nostalgebraist2020,\n  title     = {interpreting {GPT}: the logit lens},\n  author    = {nostalgebraist},\n  year      = {2020},\n  howpublished = {LessWrong blog post},\n  url       = {https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens},\n  note      = {Accessed: 2026-05-19},\n}\n\n% === VLA Fine-tuning and Reasoning ===\n\n@article{fang2025,\n  title     = {{DualVLA}: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action},\n  author    = {Fang, Zhen and Liu, Zhuoyang and Liu, Jiaming and Chen, Hao and Zeng, Yu and Huang, Shiting and Chen, Zehui and Chen, Lin and Zhang, Shanghang and Zhao, Feng},\n  journal   = {arXiv preprint arXiv:2511.22134},\n  year      = {2025},\n}\n\n% === LLM Backbone ===\n\n@article{touvron2023_llama2,\n  title     = {{Llama} 2: Open Foundation and Fine-Tuned Chat Models},\n  author    = {Touvron, Hugo and Martin, Louis and Stone, Kevin and Albert, Peter and Almahairi, Amjad and Babaei, Yasmine and Bashlykov, Nikolay and Batra, Soumya and Bhargava, Prajjwal and Bhosale, Shruti and others},\n  journal   = {arXiv preprint arXiv:2307.09288},\n  year      = {2023},\n}\n\n% === Dataset ===\n\n@article{padalkar2023_oxe,\n  title     = {Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author    = {Padalkar, Abhishek and Poolber, Acorn and Bewley, Ajinkya and others},\n  journal   = {arXiv preprint arXiv:2310.08864},\n  year      = {2023},\n}\n\n% === VLA Foundation Models ===\n\n@article{black2024_pi0,\n  title     = {$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author    = {Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and Jakubczak, Szymon and Jones, Tim and Ke, Liyiming and Levine, Sergey and Li-Bell, Adrian and Mothukuri, Mohith and Nair, Suraj and Pertsch, Karl and Shi, Lucy Xiaoyang and Tanner, James and Vuong, Quan and Walling, Anna and Wang, Haohuan and Zhilinsky, Ury},\n  journal   = {arXiv preprint arXiv:2410.24164},\n  year      = {2024},\n}\n\n@inproceedings{ghosh2024_octo,\n  title     = {Octo: An Open-Source Generalist Robot Policy},\n  author    = {Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and Mees, Oier and Dasari, Sudeep and Hejna, Joey and Kreiman, Tobias and Xu, Charles and You, Jianlan and Wu, Joey and Finn, Chelsea and Kumar, Aviral and Hausman, Karol and Levine, Sergey},\n  booktitle = {Robotics: Science and Systems},\n  year      = {2024},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 389,
        "oldLines": 3,
        "newStart": 389,
        "newLines": 28,
        "lines": [
          "   booktitle = {Robotics: Science and Systems},",
          "   year      = {2024},",
          " }",
          "+",
          "+% === Attention Head Pruning ===",
          "+",
          "+@inproceedings{michel2019sixteen,",
          "+  title     = {Are Sixteen Heads Really Better than One?},",
          "+  author    = {Michel, Paul and Levy, Omer and Neubig, Graham},",
          "+  booktitle = {Advances in Neural Information Processing Systems},",
          "+  year      = {2019},",
          "+}",
          "+",
          "+% === Instruction Tuning ===",
          "+",
          "+@inproceedings{wei2022finetuned,",
          "+  title     = {Finetuned Language Models Are Zero-Shot Learners},",
          "+  author    = {Wei, Jason and Bosma, Maarten and Zhao, Vincent and Guu, Kelvin and Yu, Adams Wei and Lester, Brian and Du, Nan and Dai, Andrew M and Le, Quoc V},",
          "+  booktitle = {International Conference on Learning Representations},",
          "+  year      = {2022},",
          "+}",
          "+",
          "+@inproceedings{ouyang2022training,",
          "+  title     = {Training language models to follow instructions with human feedback},",
          "+  author    = {Ouyang, Long and Wu, Jeffrey and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and others},",
          "+  booktitle = {Advances in Neural Information Processing Systems},",
          "+  year      = {2022},",
          "+}"
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

_source line 50_

All edits complete. Now verifying the changes and compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "27c5e918-ba80-46cc-9b47-a82c4459f70f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPpfoGZPBb59ahYdoqyaMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 76517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 976
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

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01MnLtB1asH1nbDytT1Fcd9q`</summary>

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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "1683ca3b-7d3b-4954-9ed1-eabe83dd781f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPpfoGZPBb59ahYdoqyaMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 76517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 976
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

_source line 52 · 2026-05-19T12:00:09.791Z_

<details><summary>↩ Tool result · `toolu_01MnLtB1asH1nbDytT1Fcd9q`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
8	\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\ref{tab:counterfactual}).
9	\emph{Supporting}: (3)~attention gradient ($0 \to 9 \to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).
10	\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\times$; Table~\ref{tab:specificity_control}).
11	
12	\paragraph{Mechanistic interpretation.}
13	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.
14	The instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.
15	Counterfactual ordering follows token novelty ($\rho = 1.0$; \S\ref{sec:learned_routing}).
16	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; Appendix~\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.
17	
18	\paragraph{Functional stages and predictions.}
19	The per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\sim}56\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).
20	The entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\S\ref{sec:learned_routing}).
21	This is an $N=2$ comparison (OpenVLA-7B vs.\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\ LIBERO 500 demonstrations) may also contribute to the L31 change.
22	Predictions: cross-attention VLAs ($\pi_0$~\cite{black2024_pi0}, Octo~\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.
23	
24	\paragraph{Task-dependent routing.}
25	The routing effect is task-dependent: instruction-discriminative tasks show $2.5\times$ larger $|\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\ref{tab:task_complexity}), rising to $6.5\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\ref{sec:task_complexity}).
26	For deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.
27	
28	\paragraph{Limitations and scope.}
29	We study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
30	Llama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.
31	All analyses are open-loop; our routing analysis (\emph{where}) complements H\"aon et al.'s~\cite{haon2025} (\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "d391622c-7f82-4e2a-80b0-84b9d71e64e8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.\n\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).\n\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).\n\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_011VAwnF1DD6nHFhxR594qCH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "limit": 70,
  "offset": 55
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "5b95a815-acc6-4219-9f0e-ba2680f379a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPpfoGZPBb59ahYdoqyaMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 76517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 976
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

_source line 54 · 2026-05-19T12:00:10.717Z_

<details><summary>↩ Tool result · `toolu_011VAwnF1DD6nHFhxR594qCH`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "3e247b59-55c6-4d9a-852f-167ca5e93c08",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
      "content": "\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).\nHead counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}",
      "numLines": 70,
      "startLine": 55,
      "totalLines": 158
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01GACVQ5f6QBXFwUtfxN6W9V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "453678a7-94ea-4d80-bc85-585138911e91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPpfoGZPBb59ahYdoqyaMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 76517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 976
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

_source line 56 · 2026-05-19T12:00:11.063Z_

<details><summary>↩ Tool result · `toolu_01GACVQ5f6QBXFwUtfxN6W9V`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	While instruction tuning in NLP focuses on behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.
8	We test this assumption at the representational level through per-layer, per-token-type decomposition.
9	
10	\paragraph{Mechanistic interpretability in transformers.}
11	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
12	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
13	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
14	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
15	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
16	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
17	Michel et al.~\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.
18	Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
19	
20	\paragraph{Behavioral and mechanistic analysis of VLAs.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "e8040f57-ad86-4689-b4b7-a2018a511b8e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 37
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
All edits look correct. Now let me compile the PDF to verify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "3d483935-509f-406f-80b3-cb661a59f480",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6NxxZDN8jg1j8zJYKoS3D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4691,
      "cache_read_input_tokens": 77493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4691
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

_source line 58_

All text edits verified. Now compiling the PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "9e0c46eb-a5aa-4aee-9c22-6069de4e8a09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6NxxZDN8jg1j8zJYKoS3D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4691,
      "cache_read_input_tokens": 77493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4691
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

<details open><summary>🔧 Tool call — Bash · `toolu_01BPwD3FmAGsnAPtsCCERLi1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && latexmk -pdf main.tex 2>&1 | tail -30",
  "description": "Compile LaTeX PDF",
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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "7a23162f-daa6-4d0d-bf3c-046461fa1e3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6NxxZDN8jg1j8zJYKoS3D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4691,
      "cache_read_input_tokens": 77493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4691
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

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bv8um7vf2",
  "tool_use_id": "toolu_01BPwD3FmAGsnAPtsCCERLi1",
  "description": "Compile LaTeX PDF",
  "task_type": "local_bash",
  "uuid": "6f7cd0a4-77a9-480d-9e73-f9af91ef9a2d",
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3"
}
```

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bv8um7vf2",
  "tool_use_id": "toolu_01BPwD3FmAGsnAPtsCCERLi1",
  "status": "completed",
  "output_file": "",
  "summary": "Compile LaTeX PDF",
  "uuid": "c0742080-9bae-44d7-9669-c593d7f0ddbb",
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3"
}
```

---

### Tool result

_source line 62 · 2026-05-19T12:00:21.130Z_

<details><summary>↩ Tool result · `toolu_01BPwD3FmAGsnAPtsCCERLi1`</summary>

```text
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
Output written on main.pdf (28 pages, 566110 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
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
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "b54e6ebb-ee3d-4d19-9130-84b4f91e8ac9",
  "tool_use_result": {
    "stdout": "(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt0900.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on main.pdf (28 pages, 566110 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_014a1YGJHAF7qkyM7efg69Cy`</summary>

```json
{
  "command": "grep -c \"^!\" main.log; echo \"---\"; grep \"Warning.*Citation.*undefined\" main.log | head -5",
  "description": "Check for LaTeX errors and undefined citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "87ec0836-86dc-49d2-bc9f-baa546839741",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TjJcjg2J5u7grB1mT4D8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 82184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 994
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

_source line 64 · 2026-05-19T12:00:25.229Z_

<details><summary>↩ Tool result · `toolu_014a1YGJHAF7qkyM7efg69Cy`</summary>

```text
0
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "f743b917-6ac3-4ef5-9d5c-1b3412a8ccfe",
  "tool_use_result": {
    "stdout": "0\n---",
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

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01L2DjtwSQLE7w8L9hgihrwy`</summary>

```json
{
  "command": "grep -c \"Warning.*Citation.*undefined\" main.log; grep -c \"Warning.*undefined\" main.log; echo \"---page count---\"; pdfinfo main.pdf 2>/dev/null | grep Pages || python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\n# Find where references start\nimport re\npages = text.split('\\x0c')\nprint(f'Total pages: {len(pages)}')\"",
  "description": "Check for undefined citations and page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "1bb71cea-8390-461b-8781-48d9ce260eeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NqK7FjmwkUgS64P2XgFq8D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 119,
      "cache_read_input_tokens": 83178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 119
      },
      "output_tokens": 62,
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

_source line 66 · 2026-05-19T12:00:30.512Z_

<details><summary>↩ Tool result · `toolu_01L2DjtwSQLE7w8L9hgihrwy`</summary>

```text
0
0
---page count---
Pages:           28
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "3970ebb1-e884-44ac-9f67-ca4413d0cc61",
  "tool_use_result": {
    "stdout": "0\n0\n---page count---\nPages:           28",
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

_source line 67_

<details><summary>Logged reasoning block</summary>

```text
28 pages total. I need to check if the main body is within 8 pages. Let me check how the page count breaks down. The main body before references should be within 8 pages for CoRL.

Let me check what the reference page starts at, and appendix page starts at. Let me look at the compiled PDF more carefully.

Actually, I should check if there are any warnings about underfull/overfull boxes, but more importantly I need to verify the main body is ≤ 8 pages. Let me check the main.tex to understand the structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "1d814ed8-11ba-443f-bb07-035f99dbf427",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8MZ7QLcS9mH8KYuWy8DSW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 83178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
      },
      "output_tokens": 8,
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

### Assistant

_source line 68_

0 errors, 0 undefined citations. Let me check the body page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "b644db1a-1e36-4b7e-92a8-703e666e719c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8MZ7QLcS9mH8KYuWy8DSW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 83178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
      },
      "output_tokens": 8,
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

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_01JoQXeUcAaXiB2ueKa6UHP4`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\bibliography\\|\\\\\\\\appendix\\|\\\\\\\\newpage\" main.tex",
  "description": "Find structure markers in main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "38e4cff1-6ac2-4663-acd7-deecba3e4fd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8MZ7QLcS9mH8KYuWy8DSW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 83178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
      },
      "output_tokens": 8,
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

_source line 70 · 2026-05-19T12:00:39.728Z_

<details><summary>↩ Tool result · `toolu_01JoQXeUcAaXiB2ueKa6UHP4`</summary>

```text
35:\bibliography{references}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "bb5d86b2-1742-4378-b536-6cdfe1948dd1",
  "tool_use_result": {
    "stdout": "35:\\bibliography{references}",
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

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01QGib2bXvaMJSdBtKb29g5o`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess, re\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\x0c')\nfor i, page in enumerate(pages[:15], 1):\n    # Look for section headers to identify page content\n    first_lines = page.strip()[:200] if page.strip() else '(empty)'\n    print(f'Page {i}: {first_lines[:120]}')\n\"",
  "description": "Identify page contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "0400b8cf-69c1-4f79-994e-9858ebd1054c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWe9jwi6zzjUQb38pxNgy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 83628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 274
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

_source line 72 · 2026-05-19T12:00:44.773Z_

<details><summary>↩ Tool result · `toolu_01QGib2bXvaMJSdBtKb29g5o`</summary>

```text
Page 1: Vision Encodes, Language Routes:
               Token-Level Functional Specialization in a
                    Vision-La
Page 2: 37   and randomly initialized) crossed with instruction presence, and apply four complementary analy-
38   ses: cross-in
Page 3: 86   generation [3, 27, 28]. At the mechanistic level, Häon et al. [4] identified sparse semantic directions
 87   in VL
Page 4: 132   DINOv2 (1,024-D) and SigLIP (1,152-D) branches before fusion. Throughout, L0 denotes the em-
133   bedding layer o
Page 5: Table 1: Cross-instruction 10-way classification at selected layers (full profile in Appendix A.18.1).
      Image_mean 
Page 6: Table 2: Instruction routing at L1. Mode: immed./gradual/incid. = acquisition speed; +sta-
      ble/+forget = retention
Page 7: 32
                                                                                                          VLA Trained
Page 8: 0.70                                                         DINOv2 cls (0.692)
                                        
Page 9: 288   Limitations and scope. We study OpenVLA-7B, trained on multi-platform data (OXE, 970K
289   episodes) and evaluate
Page 10: 332   [13] J. Wei, M. Bosma, V. Zhao, K. Guu, A. W. Yu, B. Lester, N. Du, A. M. Dai, and Q. V. Le.
333        Finetuned 
Page 11: 377   [28] S. Fei, S. Wang, J. Shi, Z. Dai, J. Cai, P. Qian, L. Ji, X. He, S. Zhang, Z. Fei, J. Fu, J. Gong, and
378    
Page 12: 421   [44] J. Hewitt and C. D. Manning. A structural probe for finding syntax in word representations.
422        In Pro
Page 13: (a) RSA (Spearman )                    0.11
                                                                            
Page 14: 476   A.5               Per-Layer RSA Profiles

477   Figure 5 extends Figure 2 (main text) by adding readout and untrai
Page 15: Figure 6: Per-layer action probe R2 (image_mean) across three training conditions: untrained VLA
      (random weights),
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "89fd2562-63c6-4a48-b802-614acb19a0dd",
  "tool_use_result": {
    "stdout": "Page 1: Vision Encodes, Language Routes:\n               Token-Level Functional Specialization in a\n                    Vision-La\nPage 2: 37   and randomly initialized) crossed with instruction presence, and apply four complementary analy-\n38   ses: cross-in\nPage 3: 86   generation [3, 27, 28]. At the mechanistic level, Häon et al. [4] identified sparse semantic directions\n 87   in VL\nPage 4: 132   DINOv2 (1,024-D) and SigLIP (1,152-D) branches before fusion. Throughout, L0 denotes the em-\n133   bedding layer o\nPage 5: Table 1: Cross-instruction 10-way classification at selected layers (full profile in Appendix A.18.1).\n      Image_mean \nPage 6: Table 2: Instruction routing at L1. Mode: immed./gradual/incid. = acquisition speed; +sta-\n      ble/+forget = retention\nPage 7: 32\n                                                                                                          VLA Trained\nPage 8: 0.70                                                         DINOv2 cls (0.692)\n                                        \nPage 9: 288   Limitations and scope. We study OpenVLA-7B, trained on multi-platform data (OXE, 970K\n289   episodes) and evaluate\nPage 10: 332   [13] J. Wei, M. Bosma, V. Zhao, K. Guu, A. W. Yu, B. Lester, N. Du, A. M. Dai, and Q. V. Le.\n333        Finetuned \nPage 11: 377   [28] S. Fei, S. Wang, J. Shi, Z. Dai, J. Cai, P. Qian, L. Ji, X. He, S. Zhang, Z. Fei, J. Fu, J. Gong, and\n378    \nPage 12: 421   [44] J. Hewitt and C. D. Manning. A structural probe for finding syntax in word representations.\n422        In Pro\nPage 13: (a) RSA (Spearman )                    0.11\n                                                                            \nPage 14: 476   A.5               Per-Layer RSA Profiles\n\n477   Figure 5 extends Figure 2 (main text) by adding readout and untrai\nPage 15: Figure 6: Per-layer action probe R2 (image_mean) across three training conditions: untrained VLA\n      (random weights),",
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

_source line 73_

<details><summary>Logged reasoning block</summary>

```text
Looking at the output:
- Pages 1-8: Main body content (page 8 ends with Figure 3/Table 3 area)
- Page 9: Discussion section (still main body!)
- Page 10-12: References
- Page 13+: Appendix

So the main body is 9 pages (through page 9 with the Discussion section). Wait, let me look more carefully.

Page 8 shows "0.70 DINOv2 cls (0.692)" which seems like a figure. Page 9 starts with "Limitations and scope" which is the last paragraph of Discussion.


The main body spans pages 1-9, which means it's 9 pages total. CoRL's limit is 8 pages for the main body excluding references and appendix, so I'm over by 1 page. Let me verify by checking where the references actually begin—page 9 ends with discussion content and page 10 starts with the reference list, confirming the main body is indeed 9 pages.

My recent edits added roughly 10 lines across the discussion, experiments, related work, and appendix files—that's probably 0.2-0.3 pages of content. So either the paper was already close to or at the limit before my changes, or it was already exceeding it. I need to check the original page count to see if this is a new problem or a pre-existing one.

Looking at the line numbers from the PDF text extraction, line 288 appears on page 9, so I should count more carefully what's actually on that final page. Rather than speculate, I'll just report the current page count factually and let the user determine whether this is something they introduced or if it was already an issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "eeafe7a9-4b39-4694-88e5-d11fc728c8b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfV7azKSzDTcfoLPXgn16k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 83902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 833
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

_source line 74_

Main body is 9 pages (pages 1-9), references start on page 10. This exceeds the CoRL 8-page limit by 1 page. This may have been pre-existing; my edits added ~10 lines across the main body. The user may need to trim elsewhere.

Let me also do the writing style compliance check on the new text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "37128d1e-aac9-44c2-b584-b20ef4a512f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfV7azKSzDTcfoLPXgn16k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 83902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 833
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

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_01RuFeUB85BrVchJLdKxmYyY`</summary>

```json
{
  "command": "echo \"=== em-dash check ===\" && grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/{discussion,experiments,related_work,appendix}.tex && echo \"(none found)\" ; echo \"=== explanatory en-dash check ===\" && grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/{discussion,experiments,related_work,appendix}.tex && echo \"(none found)\"",
  "description": "Check for em-dash and explanatory en-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "02ce78dd-d4a2-41ba-8fe2-7f254786aaad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PfV7azKSzDTcfoLPXgn16k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 83902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 833
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

_source line 76 · 2026-05-19T12:01:04.932Z_

<details><summary>↩ Tool result · reported error · `toolu_01RuFeUB85BrVchJLdKxmYyY`</summary>

```text
Exit code 1
=== em-dash check ===
=== explanatory en-dash check ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "fc9752b4-1769-4c6d-a305-db0d5868ad42",
  "tool_use_result": "Error: Exit code 1\n=== em-dash check ===\n=== explanatory en-dash check ==="
}
```

</details>

---

### Assistant

_source line 77_

No em-dashes or explanatory en-dashes found. Summary of all modifications:

| # | File | Location | Change |
|---|------|----------|--------|
| 1 | `discussion.tex:13-14` | Mechanistic interpretation ¶ | Added 2.4 SD statistical description for 1.08x specificity ratio |
| 2a | `discussion.tex:20-21` | Functional stages ¶ | "suggesting" → "consistent with the hypothesis that" + N=2 caveat + alternative explanation (training data diversity) |
| 2b | `experiments.tex:63` | Task-specific sharpening ¶ | "sharpening entry-exit routing to entry-only" → N=2 hedged hypothesis + data diversity caveat |
| 3 | `appendix.tex:182` | Table counterfactual caption | Added "computed on 3 representative tasks (cabinet, bowl, plate)" |
| 4 | `experiments.tex:59-60` | Redistribution of routing ¶ | Added single-sample extraction caveat with threshold sensitivity reference |
| 5 | `related_work.tex:17` + `references.bib` | Mechanistic interp. ¶ | Added Michel et al. 2019 sentence + bib entry |
| 6 | `related_work.tex:7` + `references.bib` | VLA ¶ | Added instruction tuning bridge sentence + Wei 2022 + Ouyang 2022 bib entries |
| 7 | `paper_framing.md` | 6 occurrences | "25/32" → "24/32" |

Compilation: 0 errors, 0 undefined citations, 0 warnings. Body is 9 pages (1 over CoRL limit; may have been pre-existing).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "uuid": "254fbe84-1cc0-441c-acff-3e56777f74cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5vQe56FicMgzUNyLYsigL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 84735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1003
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

_source line 78_

No em-dashes or explanatory en-dashes found. Summary of all modifications:

| # | File | Location | Change |
|---|------|----------|--------|
| 1 | `discussion.tex:13-14` | Mechanistic interpretation ¶ | Added 2.4 SD statistical description for 1.08x specificity ratio |
| 2a | `discussion.tex:20-21` | Functional stages ¶ | "suggesting" → "consistent with the hypothesis that" + N=2 caveat + alternative explanation (training data diversity) |
| 2b | `experiments.tex:63` | Task-specific sharpening ¶ | "sharpening entry-exit routing to entry-only" → N=2 hedged hypothesis + data diversity caveat |
| 3 | `appendix.tex:182` | Table counterfactual caption | Added "computed on 3 representative tasks (cabinet, bowl, plate)" |
| 4 | `experiments.tex:59-60` | Redistribution of routing ¶ | Added single-sample extraction caveat with threshold sensitivity reference |
| 5 | `related_work.tex:17` + `references.bib` | Mechanistic interp. ¶ | Added Michel et al. 2019 sentence + bib entry |
| 6 | `related_work.tex:7` + `references.bib` | VLA ¶ | Added instruction tuning bridge sentence + Wei 2022 + Ouyang 2022 bib entries |
| 7 | `paper_framing.md` | 6 occurrences | "25/32" → "24/32" |

Compilation: 0 errors, 0 undefined citations, 0 warnings. Body is 9 pages (1 over CoRL limit; may have been pre-existing).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 273504,
  "duration_api_ms": 270311,
  "num_turns": 28,
  "stop_reason": "end_turn",
  "session_id": "e2f648de-9000-495d-a3a6-97f7b888b9e3",
  "total_cost_usd": 1.5012604999999997,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 112166,
    "cache_read_input_tokens": 806978,
    "output_tokens": 15781,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 112166,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 443,
        "cache_read_input_tokens": 84735,
        "cache_creation_input_tokens": 1003,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1003
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2024,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002134,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 15781,
      "cacheReadInputTokens": 806978,
      "cacheCreationInputTokens": 112166,
      "webSearchRequests": 0,
      "costUSD": 1.4991264999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "47d49d0b-e8be-4e3a-8b49-87513a7a726b"
}
```

</details>

---
