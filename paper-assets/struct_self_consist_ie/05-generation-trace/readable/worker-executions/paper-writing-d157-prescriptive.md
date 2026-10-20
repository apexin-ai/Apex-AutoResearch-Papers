# paper writing d157 prescriptive

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_writing_d157_prescriptive_20260519T022603.log`
- **Structured JSON:** [`d652d8addee28bcb1450.json`](../../sessions/d6/d652d8addee28bcb1450.json)

## Before a recorded user message

14 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "c81a680a-ef91-477f-a664-4c5f1bcd8bca",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1779170400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c311364a-be1c-439e-8b4d-2f740b954c01",
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444"
}
```

---

### Assistant

_source line 4_

I'll read the required files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "aad53046-0346-45e4-9106-32741f874574",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dv9QXM3JE7zeY99vBRjMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14010,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14010
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01WsSHQS2BwqHxhWVbdsgyjC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "cf8d6a73-2b1e-4f07-9f2e-8d2f307852a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dv9QXM3JE7zeY99vBRjMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14010,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14010
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

_source line 6 · 2026-05-19T02:26:18.513Z_

<details><summary>↩ Tool result · `toolu_01WsSHQS2BwqHxhWVbdsgyjC`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\ref{app:epoch_confound}).
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments (ranking stability $\sigma{\leq}0.026$, Table~\ref{tab:multiseed}; sublinear gains beyond $N{=}8$, Appendix~\ref{app:n_scaling}).
18	Inference uses vLLM with constrained decoding \cite{willard2023guided} (seed protocol: Appendix~\ref{app:multiseed}).
19	
20	%% ============================================================
21	\subsection{Quality Estimation Results}
22	\label{sec:qe_results}
23	
24	\begin{table*}[t]
25	\centering
26	\small
27	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
28	\label{tab:quality_estimation}
29	\begin{tabular}{ll cc cc cc}
30	\toprule
31	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
32	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
33	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
34	\midrule
35	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
36	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
37	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
38	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
39	\midrule
40	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
41	\bottomrule
42	\end{tabular}
43	\end{table*}
44	
45	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
46	
47	\paragraph{Signal rankings are difficulty-dependent.}
48	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
49	On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
50	At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
51	
52	%% ============================================================
53	\subsection{The Correlation-Selection Gap}
54	\label{sec:selection_gap}
55	
56	Two factors constrain selection: instance degeneracy collapses the candidate pool for consensus-based approaches, and weak LP-quality alignment prevents exploiting the remaining headroom.
57	Four instance-level signals cannot rank candidates by construction; LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\S\ref{sec:discussion}).
58	
59	\begin{table}[t]
60	\centering
61	\small
62	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Non-tied subset in \S\ref{sec:discussion}; RE in Appendix~\ref{app:re_extension}.}
63	\label{tab:selection}
64	\begin{tabular}{lcc}
65	\toprule
66	Method & NER F1 & $p$ \\
67	\midrule
68	Oracle & $0.775 \pm 0.001$ & --- \\
69	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
70	\midrule
71	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
72	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
73	\midrule
74	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
75	SJ           & $0.646 \pm 0.002$ & .67 \\
76	FK           & $0.646 \pm 0.001$ & .79 \\
77	EM           & $0.637 \pm 0.001$ & --- \\
78	VC           & $0.623 \pm 0.004$ & --- \\
79	\midrule
80	Random           & $0.610 \pm 0.003$ & --- \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	\begin{figure}[t]
86	\centering
87	\includegraphics[width=\columnwidth]{fig_selection_gap}
88	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line: oracle upper bound.}
89	\label{fig:selection_gap}
90	\end{figure}
91	
92	Despite moderate quality estimation, no signal consistently improves selection over greedy (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}).
93	Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed.
94	
95	\paragraph{No significant improvement over greedy.}
96	On SciERC ($n{=}529$, 2-seed sign tests\footnote{MDE${\approx}$1.5~pp at 80\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp).
97	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
98	Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
99	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers} (the sole positive finding, non-tied LP subset $+2.9$~pp $p{=}0.004$, survives Bonferroni correction; \S\ref{sec:discussion}).
100	
101	%% ============================================================
102	\subsection{Cross-Dataset Contrast: Few-NERD}
103	\label{sec:fewnerd}
104	
105	\begin{table}[t]
106	\centering
107	\small
108	\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Instance degeneracy (Degen.\%): fraction where all $N$ samples yield identical F1. $p$: paired bootstrap ($n{=}10{,}000$) vs.\ greedy. Few-NERD and CoNLL $\Delta$ values are 3-seed means; SciERC is single-seed (3-seed mean: $+0.04{\pm}0.48$~pp). Oracle headroom: 5.0~pp (CoNLL), 13.0~pp (SciERC), 12.4~pp (Few-NERD). Minor greedy F1 variations across tables reflect protocol differences (\S\ref{sec:evaluation}). Few-NERD uses 3-epoch checkpoints; SciERC and CoNLL use 5 epochs (Appendix~\ref{app:epoch_confound}).}
109	\label{tab:fewnerd}
110	\resizebox{\columnwidth}{!}{%
111	\begin{tabular}{@{}lrccccr@{}}
112	\toprule
113	Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
114	\midrule
115	CoNLL & 2{,}756 & .908 & 48.4\% & .302 & $-$0.85\,pp & 1.0 \\
116	SciERC & 529 & .644 & 17.8\% & .205 & $+$0.61\,pp & .193 \\
117	Few-NERD & 32{,}565 & .748 & 13.8\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
118	\bottomrule
119	\end{tabular}}
120	\end{table}
121	
122	Few-NERD (Table~\ref{tab:fewnerd}) confirms that LP selection effectiveness is inversely associated with degeneracy.
123	Under standard early stopping (3 epochs for Few-NERD vs.\ 5 for SciERC/CoNLL), Few-NERD degeneracy is 13.8\%, and LP achieves $+1.39$~pp ($p{<}0.001$, seed $\sigma{=}0.04$~pp vs.\ SJ $\sigma{=}2.02$~pp), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).
124	LP selection is 50$\times$ more stable across random seeds than structural selection, making it the only practically reliable signal for deployment scenarios requiring reproducibility.
125	Training convergence modulates degeneracy: a 5-epoch Few-NERD control raises degeneracy to 31\% and halves LP gains, though selection remains positive (Appendix~\ref{app:epoch_confound}).
126	
127	\paragraph{Degeneracy alone does not predict LP selection direction.}
128	Across 23 dataset-model-temperature configurations at $N{=}8$, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}).
129	Counter-examples illustrate: LLaMA CoNLL exhibits 86.5\% degeneracy yet LP is non-negative ($+0.14$~pp), while a 3-epoch SciERC model at 6.4\% degeneracy yields LP $-1.18$~pp.
130	Within fixed settings, however, degeneracy causally modulates LP effectiveness: the SciERC epoch ablation ($-1.18$, $+0.74$, $+0.99$~pp at 3, 5, 10 epochs; Appendix~\ref{app:epoch_confound}) and per-entity-type analysis within Few-NERD ($n{=}8$, $\rho{=}{-}0.881$, $p{=}0.004$; Appendix~\ref{app:per_type_lp}) both show degeneracy effects when dataset and model are held constant.
131	Cross-dataset prediction requires LP signal quality: Few-NERD (within-instance $\rho{\approx}0.5$--$0.7$) shows consistent gains, while SciERC ($\rho{\approx}0.26$) and CoNLL ($\rho{\approx}0.51$, but only 41\% non-degenerate) show mixed results.
132	Even at matched training duration (3 epochs on both datasets), SciERC within-instance $\rho{=}0.319$ remains below Few-NERD's ${\sim}0.5$ (Table~\ref{tab:epoch_scierc}), confirming that LP-quality alignment, not training duration, drives the cross-dataset difference.
133	All five signals achieve positive QE on Few-NERD (VC $\rho{=}0.39$, LP $0.22$), yet only LP translates QE into selection; the gap confirms that strong instance-level QE cannot rank candidates within an instance.
134	Conditional analysis on the favorable subset (non-degenerate instances whose within-instance LP range exceeds the dataset-specific median) yields $+2.47$~pp on SciERC (CI $[+0.30, +4.70]$) and a marginal positive trend on Few-NERD ($+0.63$~pp, CI $[-0.02, +1.30]$); CoNLL remains negative ($-1.78$~pp), consistent with ceiling-regime degeneracy even within the favorable subset (Appendix~\ref{app:conditional_decomp}).
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
139	\caption{Instance degeneracy vs.\ LP selection gain across 23 dataset-model-temperature configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$): degeneracy alone does not predict LP direction across datasets. Within Few-NERD per-entity-type analysis ($n{=}8$; $\rho{=}{-}0.881$, $p{=}0.004$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when LP alignment is held constant. Selection viability depends on LP signal quality and dataset characteristics, not degeneracy alone.}
140	\label{fig:degeneracy_scatter}
141	\end{figure}
142	
143	\paragraph{LP selection scales with sample budget.}
144	Doubling $N$ from 8 to 16 on Few-NERD yields $+0.52$~pp (paired $p{=}0.003$, CI $[+0.17, +0.87]$), driven by reduced degeneracy (14.6\% $\to$ 7.0\%) expanding headroom (12.1 $\to$ 15.4~pp), while LP ranking quality remains stable ($\rho{\approx}0.62$).
145	Structural signals remain uniformly negative at $N{=}16$; the gap persists regardless of sample budget.
146	
147	%% ============================================================
148	\subsection{Robustness}
149	\label{sec:robustness_main}
150	
151	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
152	Signal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; $m{=}3$ raters, interpret with caution given low $m$; exact $p{\approx}0.028$; Table~\ref{tab:ranking-stability}).
153	NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
154	
155	\begin{table}[t]
156	\centering
157	\small
158	\caption{Scale ablation: Qwen3-8B vs.\ 4B NER quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\ref{app:re_extension}.}
159	\label{tab:scale_ablation}
160	\begin{tabular}{@{}ll cc r@{}}
161	\toprule
162	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
163	\midrule
164	CoNLL & SJ & .436 & .422 & $-$.014 \\
165	      & FK & .400 & .418 & $+$.018 \\
166	SciERC & SJ & .360 & .422 & $+$.062 \\
167	       & FK & .267 & .326 & $+$.059 \\
168	\bottomrule
169	\end{tabular}
170	\end{table}
171	
172	\paragraph{Scale robustness.}
173	With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
174	Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
175	
176	\paragraph{LoRA-rank ablation.}
177	Training with LoRA rank${=}8$ (vs.\ 32) lowers degeneracy from 17.8\% to 7.2\% and increases headroom to 16.0~pp, but LP does not improve selection (0.635 vs.\ greedy 0.640).
178	This ablation conflates diversity with model capacity (rank 8 has fewer trainable parameters); within-instance $\rho(\text{LP}, \text{F1}){\approx}0.24$ remains too weak despite wider LP spread (0.057 vs.\ 0.041 nats).
179	Temperature manipulation (\S\ref{sec:discussion}) provides a cleaner test by altering diversity without changing capacity, and yields the same conclusion: both low degeneracy and adequate alignment appear independently associated with selection success.
180	
181	\paragraph{Supervised signal combination.}
182	Supervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).
183	Adding pairwise interaction features does not help (AUROC 0.634 vs.\ 0.638).
184	To test whether richer representations could close the gap, we train a DeBERTa-v3-base verifier that encodes input-output pairs and predicts per-sample F1.
185	DeBERTa achieves $\rho{=}0.329{\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\pm}26.5$\% of the oracle gap (13 of 15 runs negative; vs.\ LP's $+4.2{\pm}10.7$\%); on Few-NERD, DeBERTa recovers only $+3.5$\% (single 80/20 split; vs.\ LP's $+16.3$\%).
186	Cross-dataset transfer fails entirely ($-27$\% to $-72$\% gap closure).
187	Neither handcrafted signal combinations (LR, MLP, RF on 5 scalar signals) nor learned text representations close the selection gap; only model-internal log-probability provides meaningful selection signal, consistent with an information asymmetry between the generating model and external observers.
188	
189	%% ============================================================
190	\subsection{Probing the Information Gap}
191	\label{sec:hidden_probe}
192	
193	The preceding negative results suggest the bottleneck is model-internal rather than a feature engineering problem.
194	We test this directly by training probes on the generating model's hidden representations.
195	
196	\paragraph{Setup.}
197	For each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).
198	
199	\begin{table}[t]
200	\centering
201	\small
202	\caption{Hidden state probes vs.\ LP for sample selection (5-fold CV ${\times}$ 3 seeds). $\rho$: Spearman correlation with per-sample F1. Sel.\ F1: selection F1. Gap\%: oracle gap closure. SciERC greedy${=}0.644$, oracle${=}0.775$.}
203	\label{tab:hidden_probe}
204	\resizebox{\columnwidth}{!}{%
205	\begin{tabular}{@{}l ccc cc@{}}
206	\toprule
207	& \multicolumn{3}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{Few-NERD}} \\
208	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
209	Method & $\rho$ & Sel.\ F1 & Gap\% & $\rho$ & Gap\% \\
210	\midrule
211	LP & .283 & $\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\
212	Hidden Linear & $.179{\pm}.019$ & $.613{\pm}.002$ & $-$23.4 & \multicolumn{2}{c}{---} \\
213	Hidden MLP & $\mathbf{.388{\pm}.013}$ & $.637{\pm}.003$ & $-$5.1 & $\mathbf{.629{\pm}.007}$ & 11.7 \\
214	\bottomrule
215	\end{tabular}}
216	\end{table}
217	
218	\paragraph{Cross-dataset asymmetry.}
219	On SciERC, the MLP probe achieves higher quality correlation than LP ($\rho{=}0.388$ vs.\ $0.283$, $+37$\%); hidden states encode information beyond what LP captures.
220	Yet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\% vs.\ $+4.8$\%; Table~\ref{tab:hidden_probe}).
221	The linear probe performs worse still ($\rho{=}0.179$, gap closure $-23.4$\%).
222	On Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\% vs.\ $12.3$\%).
223	A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\% vs.\ $55.8$\%), confirming that LP's bottleneck is not token aggregation.
224	The correlation-selection gap thus extends to model-internal representations: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\S\ref{sec:discussion}).
225	
226	\phantomsection\label{sec:selection_results}
227	%% Framework validation (DGS) is presented in Discussion §5 to save space
228	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "7f3ae09c-776d-4e5c-8678-ef56bf22bff1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, except Few-NERD models which use 3 epochs (early stopping at the best validation checkpoint; a 5-epoch control confirms LP selection remains positive though gains are halved; Appendix~\\ref{app:epoch_confound}).\nQwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\\ref{app:thinking_token}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments (ranking stability $\\sigma{\\leq}0.026$, Table~\\ref{tab:multiseed}; sublinear gains beyond $N{=}8$, Appendix~\\ref{app:n_scaling}).\nInference uses vLLM with constrained decoding \\cite{willard2023guided} (seed protocol: Appendix~\\ref{app:multiseed}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nTwo factors constrain selection: instance degeneracy collapses the candidate pool for consensus-based approaches, and weak LP-quality alignment prevents exploiting the remaining headroom.\nFour instance-level signals cannot rank candidates by construction; LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & --- \\\\\nVC           & $0.623 \\pm 0.004$ & --- \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.40, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed line: oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nDespite moderate quality estimation, no signal consistently improves selection over greedy (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed.\n\n\\paragraph{No significant improvement over greedy.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp).\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best; closing this gap likely requires trained verifiers \\cite{cobbe2021verifiers} (the sole positive finding, non-tied LP subset $+2.9$~pp $p{=}0.004$, survives Bonferroni correction; \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Instance degeneracy (Degen.\\%): fraction where all $N$ samples yield identical F1. $p$: paired bootstrap ($n{=}10{,}000$) vs.\\ greedy. Few-NERD and CoNLL $\\Delta$ values are 3-seed means; SciERC is single-seed (3-seed mean: $+0.04{\\pm}0.48$~pp). Oracle headroom: 5.0~pp (CoNLL), 13.0~pp (SciERC), 12.4~pp (Few-NERD). Minor greedy F1 variations across tables reflect protocol differences (\\S\\ref{sec:evaluation}). Few-NERD uses 3-epoch checkpoints; SciERC and CoNLL use 5 epochs (Appendix~\\ref{app:epoch_confound}).}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nCoNLL & 2{,}756 & .908 & 48.4\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms that LP selection effectiveness is inversely associated with degeneracy.\nUnder standard early stopping (3 epochs for Few-NERD vs.\\ 5 for SciERC/CoNLL), Few-NERD degeneracy is 13.8\\%, and LP achieves $+1.39$~pp ($p{<}0.001$, seed $\\sigma{=}0.04$~pp vs.\\ SJ $\\sigma{=}2.02$~pp), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp).\nLP selection is 50$\\times$ more stable across random seeds than structural selection, making it the only practically reliable signal for deployment scenarios requiring reproducibility.\nTraining convergence modulates degeneracy: a 5-epoch Few-NERD control raises degeneracy to 31\\% and halves LP gains, though selection remains positive (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 dataset-model-temperature configurations at $N{=}8$, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}).\nCounter-examples illustrate: LLaMA CoNLL exhibits 86.5\\% degeneracy yet LP is non-negative ($+0.14$~pp), while a 3-epoch SciERC model at 6.4\\% degeneracy yields LP $-1.18$~pp.\nWithin fixed settings, however, degeneracy causally modulates LP effectiveness: the SciERC epoch ablation ($-1.18$, $+0.74$, $+0.99$~pp at 3, 5, 10 epochs; Appendix~\\ref{app:epoch_confound}) and per-entity-type analysis within Few-NERD ($n{=}8$, $\\rho{=}{-}0.881$, $p{=}0.004$; Appendix~\\ref{app:per_type_lp}) both show degeneracy effects when dataset and model are held constant.\nCross-dataset prediction requires LP signal quality: Few-NERD (within-instance $\\rho{\\approx}0.5$--$0.7$) shows consistent gains, while SciERC ($\\rho{\\approx}0.26$) and CoNLL ($\\rho{\\approx}0.51$, but only 41\\% non-degenerate) show mixed results.\nEven at matched training duration (3 epochs on both datasets), SciERC within-instance $\\rho{=}0.319$ remains below Few-NERD's ${\\sim}0.5$ (Table~\\ref{tab:epoch_scierc}), confirming that LP-quality alignment, not training duration, drives the cross-dataset difference.\nAll five signals achieve positive QE on Few-NERD (VC $\\rho{=}0.39$, LP $0.22$), yet only LP translates QE into selection; the gap confirms that strong instance-level QE cannot rank candidates within an instance.\nConditional analysis on the favorable subset (non-degenerate instances whose within-instance LP range exceeds the dataset-specific median) yields $+2.47$~pp on SciERC (CI $[+0.30, +4.70]$) and a marginal positive trend on Few-NERD ($+0.63$~pp, CI $[-0.02, +1.30]$); CoNLL remains negative ($-1.78$~pp), consistent with ceiling-regime degeneracy even within the favorable subset (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 dataset-model-temperature configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$): degeneracy alone does not predict LP direction across datasets. Within Few-NERD per-entity-type analysis ($n{=}8$; $\\rho{=}{-}0.881$, $p{=}0.004$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when LP alignment is held constant. Selection viability depends on LP signal quality and dataset characteristics, not degeneracy alone.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\n\\paragraph{LP selection scales with sample budget.}\nDoubling $N$ from 8 to 16 on Few-NERD yields $+0.52$~pp (paired $p{=}0.003$, CI $[+0.17, +0.87]$), driven by reduced degeneracy (14.6\\% $\\to$ 7.0\\%) expanding headroom (12.1 $\\to$ 15.4~pp), while LP ranking quality remains stable ($\\rho{\\approx}0.62$).\nStructural signals remain uniformly negative at $N{=}16$; the gap persists regardless of sample budget.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nSignal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; $m{=}3$ raters, interpret with caution given low $m$; exact $p{\\approx}0.028$; Table~\\ref{tab:ranking-stability}).\nNER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B NER quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nTraining with LoRA rank${=}8$ (vs.\\ 32) lowers degeneracy from 17.8\\% to 7.2\\% and increases headroom to 16.0~pp, but LP does not improve selection (0.635 vs.\\ greedy 0.640).\nThis ablation conflates diversity with model capacity (rank 8 has fewer trainable parameters); within-instance $\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$ remains too weak despite wider LP spread (0.057 vs.\\ 0.041 nats).\nTemperature manipulation (\\S\\ref{sec:discussion}) provides a cleaner test by altering diversity without changing capacity, and yields the same conclusion: both low degeneracy and adequate alignment appear independently associated with selection success.\n\n\\paragraph{Supervised signal combination.}\nSupervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).\nAdding pairwise interaction features does not help (AUROC 0.634 vs.\\ 0.638).\nTo test whether richer representations could close the gap, we train a DeBERTa-v3-base verifier that encodes input-output pairs and predicts per-sample F1.\nDeBERTa achieves $\\rho{=}0.329{\\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\\pm}26.5$\\% of the oracle gap (13 of 15 runs negative; vs.\\ LP's $+4.2{\\pm}10.7$\\%); on Few-NERD, DeBERTa recovers only $+3.5$\\% (single 80/20 split; vs.\\ LP's $+16.3$\\%).\nCross-dataset transfer fails entirely ($-27$\\% to $-72$\\% gap closure).\nNeither handcrafted signal combinations (LR, MLP, RF on 5 scalar signals) nor learned text representations close the selection gap; only model-internal log-probability provides meaningful selection signal, consistent with an information asymmetry between the generating model and external observers.\n\n%% ============================================================\n\\subsection{Probing the Information Gap}\n\\label{sec:hidden_probe}\n\nThe preceding negative results suggest the bottleneck is model-internal rather than a feature engineering problem.\nWe test this directly by training probes on the generating model's hidden representations.\n\n\\paragraph{Setup.}\nFor each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hidden state probes vs.\\ LP for sample selection (5-fold CV ${\\times}$ 3 seeds). $\\rho$: Spearman correlation with per-sample F1. Sel.\\ F1: selection F1. Gap\\%: oracle gap closure. SciERC greedy${=}0.644$, oracle${=}0.775$.}\n\\label{tab:hidden_probe}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l ccc cc@{}}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{Few-NERD}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\nMethod & $\\rho$ & Sel.\\ F1 & Gap\\% & $\\rho$ & Gap\\% \\\\\n\\midrule\nLP & .283 & $\\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\\\\nHidden Linear & $.179{\\pm}.019$ & $.613{\\pm}.002$ & $-$23.4 & \\multicolumn{2}{c}{---} \\\\\nHidden MLP & $\\mathbf{.388{\\pm}.013}$ & $.637{\\pm}.003$ & $-$5.1 & $\\mathbf{.629{\\pm}.007}$ & 11.7 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Cross-dataset asymmetry.}\nOn SciERC, the MLP probe achieves higher quality correlation than LP ($\\rho{=}0.388$ vs.\\ $0.283$, $+37$\\%); hidden states encode information beyond what LP captures.\nYet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\\% vs.\\ $+4.8$\\%; Table~\\ref{tab:hidden_probe}).\nThe linear probe performs worse still ($\\rho{=}0.179$, gap closure $-23.4$\\%).\nOn Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\\% vs.\\ $12.3$\\%).\nA learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\\% vs.\\ $55.8$\\%), confirming that LP's bottleneck is not token aggregation.\nThe correlation-selection gap thus extends to model-internal representations: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\\S\\ref{sec:discussion}).\n\n\\phantomsection\\label{sec:selection_results}\n%% Framework validation (DGS) is presented in Discussion §5 to save space\n",
      "numLines": 228,
      "startLine": 1,
      "totalLines": 228
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01SH5h6c19GTVpdy5ZQLLULF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "c55c9708-df29-4040-9985-ecdd0cf961f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dv9QXM3JE7zeY99vBRjMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14010,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14010
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

_source line 8 · 2026-05-19T02:26:19.093Z_

<details><summary>↩ Tool result · reported error · `toolu_01SH5h6c19GTVpdy5ZQLLULF`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "e6dcbf31-022d-4649-866e-fef3a38ea0a7",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie."
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The skill file doesn't exist, but the paper-writing-norms are already embedded in the CLAUDE.md. I have all the context I need. Let me write the draft subsection.

Let me carefully study the table formatting style from experiments.tex:
- Uses `@{}` column padding
- `\toprule`, `\midrule`, `\bottomrule`
- `\small` font
- `\caption` before the table content
- `\label` right after caption
- Bold best values with `\textbf{}`
- Uses `\,pp` for percentage points


- Uses `resizebox` when needed

Now I'm drafting the prescriptive results subsection, keeping in mind the constraints: no em-dashes or explanatory en-dashes, no -ing phrase endings, no "Furthermore"/"Moreover"/"Additionally" chains, no banned words, every number from the data, self-contained table captions, matching precision and formatting of existing tables, bolding best non-oracle values, and using `\,pp` notation.

Writing the subsection... Generating results table...

The construction approach yields meaningful improvements on SciERC and Few-NERD through better recall of low-frequency entities, though it hits diminishing returns on CoNLL where performance is already near ceiling. When I compare construction against LP selection directly, construction proves more effective on SciERC where the alignment signal is weak, while the two methods show different trade-offs depending on dataset characteristics.

I'm exploring a gating mechanism that measures the correlation between LP scores and entity-level F1 on validation data to automatically select which method to apply—LP selection when alignment is strong, construction when it's weak. This approach successfully identifies the better strategy across all three datasets, with a stable threshold range, though it relies on validation rather than test data and has some practical limitations.

Beyond construction, quality estimation signals also enable selective prediction by filtering to high-confidence instances, achieving substantial F1 gains at 80% coverage with VC as the most reliable signal. For real-world use, this lets practitioners route uncertain predictions to human review instead of generating multiple candidates. the norms allow en-dashes for number ranges, so my usage is consistent with the existing style. For the table width, I'm checking whether to use resizebox—the six columns should fit in a single column without it, and keeping it simple seems better than adding unnecessary formatting.

Looking at how the existing tables handle thousands separators and decimal formatting, I'm matching that style with entries like `32{,}565` and decimal values. Let me verify the column alignment and spacing match the established patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "05afc801-fe42-4370-a0ea-909a53bfefe4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZZW4mMmVLe2HXArXATiv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 25711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7465
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

Now I'll write the draft file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "5b54480c-f438-4e3a-a6df-86b38d32743a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZZW4mMmVLe2HXArXATiv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 25711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7465
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

<details open><summary>🔧 Tool call — Write · `toolu_013gcpZtjftbrpcae4qrdK3j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_draft_prescriptive.tex",
  "content": "%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its frequency across $N$ samples and retain those exceeding a threshold $\\theta$ tuned via 5-fold cross-validation (reporting inner-fold F1 means; $\\theta{=}0.5$ majority baseline in Appendix~\\ref{app:entity_merge}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level construction vs.\\ greedy decoding (macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B). Threshold $\\theta$ tuned via 5-fold CV (inner-fold means). $p$: paired bootstrap vs.\\ greedy ($n{=}10{,}000$).}\n\\label{tab:entity_construction}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nDataset & $n$ & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & 529 & .644 & \\textbf{.658} & $+$1.35\\,pp & .018 \\\\\nFew-NERD & 32{,}565 & .748 & \\textbf{.761} & $+$1.32\\,pp & ${<}.001$ \\\\\nCoNLL & 2{,}756 & .908 & .909 & $+$0.10\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstruction significantly improves on SciERC ($+1.35$\\,pp, $p{=}0.018$) and Few-NERD ($+1.32$\\,pp, $p{<}0.001$). CoNLL shows no significant gain ($+0.10$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures. LP-weighted aggregation shows no advantage over uniform weighting.\n\n\\paragraph{Construction and LP selection are complementary.}\nUnder matched 5-fold CV evaluation, construction dominates on SciERC ($+1.35$\\,pp vs.\\ LP $+0.23$\\,pp), where LP-quality alignment is weak (within-instance $\\rho{\\approx}0.2$).\nOn Few-NERD, where alignment is strong ($\\rho{\\approx}0.5$--$0.7$), LP selection outperforms construction ($+1.88$\\,pp vs.\\ $+1.32$\\,pp).\nThe choice is governed by LP-quality alignment: when LP tracks entity-level F1 within instances, per-sample ranking succeeds; when alignment is weak, entity aggregation bypasses ranking entirely.\n\n\\paragraph{LP-alignment gating.}\nA simple gating protocol probes 50 held-out validation instances to estimate within-instance $\\rho(\\text{LP}, \\text{F1})$. Above a threshold, LP selection is applied; below it, entity construction is used instead. This protocol correctly identifies the better method on all three evaluated datasets, and the threshold is stable across $[0.2, 0.4]$. Three caveats apply: (a) the probe uses validation data, not test data; (b) threshold stability is evaluated on only three datasets; (c) this is a proof of concept that requires broader validation.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: retaining the top-$k$\\% highest-confidence instances. At 80\\% coverage, selective prediction yields $+5$--$8$\\,pp F1 gain (AUPRC 0.70--0.92), with VC as the strongest signal across all datasets. For practitioners, when selection fails, QE scores can route low-confidence instances to human review rather than sample $N$ candidates to identify the best output.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "73e23b1a-3e37-46e3-bce6-4b349bf4de35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZZW4mMmVLe2HXArXATiv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 25711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7465
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

_source line 12 · 2026-05-19T02:27:21.407Z_

<details><summary>↩ Tool result · `toolu_013gcpZtjftbrpcae4qrdK3j`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_draft_prescriptive.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "2568b2a3-ebe6-4354-a6d3-abe4a3f66ed2",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_draft_prescriptive.tex",
    "content": "%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its frequency across $N$ samples and retain those exceeding a threshold $\\theta$ tuned via 5-fold cross-validation (reporting inner-fold F1 means; $\\theta{=}0.5$ majority baseline in Appendix~\\ref{app:entity_merge}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level construction vs.\\ greedy decoding (macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B). Threshold $\\theta$ tuned via 5-fold CV (inner-fold means). $p$: paired bootstrap vs.\\ greedy ($n{=}10{,}000$).}\n\\label{tab:entity_construction}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nDataset & $n$ & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & 529 & .644 & \\textbf{.658} & $+$1.35\\,pp & .018 \\\\\nFew-NERD & 32{,}565 & .748 & \\textbf{.761} & $+$1.32\\,pp & ${<}.001$ \\\\\nCoNLL & 2{,}756 & .908 & .909 & $+$0.10\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConstruction significantly improves on SciERC ($+1.35$\\,pp, $p{=}0.018$) and Few-NERD ($+1.32$\\,pp, $p{<}0.001$). CoNLL shows no significant gain ($+0.10$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures. LP-weighted aggregation shows no advantage over uniform weighting.\n\n\\paragraph{Construction and LP selection are complementary.}\nUnder matched 5-fold CV evaluation, construction dominates on SciERC ($+1.35$\\,pp vs.\\ LP $+0.23$\\,pp), where LP-quality alignment is weak (within-instance $\\rho{\\approx}0.2$).\nOn Few-NERD, where alignment is strong ($\\rho{\\approx}0.5$--$0.7$), LP selection outperforms construction ($+1.88$\\,pp vs.\\ $+1.32$\\,pp).\nThe choice is governed by LP-quality alignment: when LP tracks entity-level F1 within instances, per-sample ranking succeeds; when alignment is weak, entity aggregation bypasses ranking entirely.\n\n\\paragraph{LP-alignment gating.}\nA simple gating protocol probes 50 held-out validation instances to estimate within-instance $\\rho(\\text{LP}, \\text{F1})$. Above a threshold, LP selection is applied; below it, entity construction is used instead. This protocol correctly identifies the better method on all three evaluated datasets, and the threshold is stable across $[0.2, 0.4]$. Three caveats apply: (a) the probe uses validation data, not test data; (b) threshold stability is evaluated on only three datasets; (c) this is a proof of concept that requires broader validation.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: retaining the top-$k$\\% highest-confidence instances. At 80\\% coverage, selective prediction yields $+5$--$8$\\,pp F1 gain (AUPRC 0.70--0.92), with VC as the strongest signal across all datasets. For practitioners, when selection fails, QE scores can route low-confidence instances to human review rather than sample $N$ candidates to identify the best output.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 13_

Draft written to `docs/paper/sections/_draft_prescriptive.tex`. Four paragraphs plus one table, matching the existing `experiments.tex` formatting (column padding, booktabs, `\,pp` notation, bold best values). No em-dashes, no -ing endings, no banned words. All numbers from the provided data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "uuid": "486aee66-d472-498c-81d7-2fc301175163",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtyCEQpte4cLNNyFtFavzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3275,
      "cache_read_input_tokens": 33176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3275
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

_source line 14_

Draft written to `docs/paper/sections/_draft_prescriptive.tex`. Four paragraphs plus one table, matching the existing `experiments.tex` formatting (column padding, booktabs, `\,pp` notation, bold best values). No em-dashes, no -ing endings, no banned words. All numbers from the provided data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 73145,
  "duration_api_ms": 74096,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "fb010a5f-90c5-47fb-af0b-3300b2b99444",
  "total_cost_usd": 0.2791825,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 24750,
    "cache_read_input_tokens": 70588,
    "output_tokens": 3476,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24750,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 79,
        "cache_read_input_tokens": 33176,
        "cache_creation_input_tokens": 3275,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3275
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2196,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002281,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 3476,
      "cacheReadInputTokens": 70588,
      "cacheCreationInputTokens": 24750,
      "webSearchRequests": 0,
      "costUSD": 0.2769015,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d0d99d46-39cd-4238-9607-79f2ab52cb38"
}
```

</details>

---
