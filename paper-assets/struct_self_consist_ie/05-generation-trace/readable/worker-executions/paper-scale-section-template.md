# paper scale section template

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_scale_section_template_20260519T103054.log`
- **Structured JSON:** [`0aad1f854d4b2a10581b.json`](../../sessions/0a/0aad1f854d4b2a10581b.json)

## Before a recorded user message

26 recorded events

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
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
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
  "uuid": "f9010002-6e9b-4480-9b14-ca9fccb054ef",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1779200400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "45bb05c2-ae74-43c3-b8dc-961a8eb1c3f7",
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9"
}
```

---

### Assistant

_source line 4_

我来执行这个任务。先并行读取当前论文结构和从服务器获取 CoNLL 72B 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "431c440a-4fa0-4da3-9f2c-f57054c623b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jE4SbDB8bDRAuV4vpaFgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13251,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13251
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JSPBRo9PWqLLAytHN5z1g2`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
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
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "54aba8d2-cca0-4cb3-aa91-88e6da3a0cd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jE4SbDB8bDRAuV4vpaFgQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13251,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13251
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

_source line 6 · 2026-05-19T10:31:04.983Z_

<details><summary>↩ Tool result · `toolu_01JSPBRo9PWqLLAytHN5z1g2`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "409918da-a5c7-4f43-884d-8b83b18eb347",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 29
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the experiments.tex file and fetch the CoNLL 72B results in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "c8dd804e-f6f7-4758-9260-256a6643a382",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193bgCWya25ZAX7dK5GALnQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 25092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 710
      },
      "output_tokens": 28,
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_018VRDM1GfKhLJzRMYmhdBoB`</summary>

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
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "d670cd19-d25f-474a-b288-5a882afb8a27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193bgCWya25ZAX7dK5GALnQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 25092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 710
      },
      "output_tokens": 28,
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

_source line 9 · 2026-05-19T10:31:08.544Z_

<details><summary>↩ Tool result · `toolu_018VRDM1GfKhLJzRMYmhdBoB`</summary>

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
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabular}{ll cc cc cc}
28	\toprule
29	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
30	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
31	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
32	\midrule
33	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
34	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
35	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
36	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
37	\midrule
38	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
39	\bottomrule
40	\end{tabular}
41	\end{table*}
42	
43	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
44	
45	\paragraph{Signal rankings are difficulty-dependent.}
46	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
47	On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
48	At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
49	This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
50	
51	%% ============================================================
52	\subsection{The Correlation-Selection Gap}
53	\label{sec:selection_gap}
54	
55	Four of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\S\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.
56	The empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.
57	LP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\S\ref{sec:discussion}).
58	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Non-tied subset in \S\ref{sec:discussion}; RE in Appendix~\ref{app:re_extension}. $^\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}
64	\label{tab:selection}
65	\begin{tabular}{lcc}
66	\toprule
67	Method & NER F1 & $p$ \\
68	\midrule
69	Oracle & $0.775 \pm 0.001$ & --- \\
70	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
71	\midrule
72	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
73	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
74	\midrule
75	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
76	SJ           & $0.646 \pm 0.002$ & .67 \\
77	FK           & $0.646 \pm 0.001$ & .79 \\
78	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
79	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
80	\midrule
81	Random           & $0.610 \pm 0.003$ & --- \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{fig_selection_gap}
89	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\rho$ (seed 42); line with error bars: $\Delta$F1 vs.\ greedy (3-seed mean, seeds 42/123/456). Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}
90	\label{fig:selection_gap}
91	\end{figure}
92	
93	Instance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}).
94	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best.
95	
96	\paragraph{LP: the sole per-sample signal also fails.}
97	On SciERC ($n{=}529$, 2-seed sign tests\footnote{MDE${\approx}$1.5~pp at 80\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.
98	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
99	Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
100	
101	\paragraph{Qualitative factors governing selection effectiveness.}
102	Three factors qualitatively shape LP selection gains: (1)~\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\%, CoNLL 48.4\%; Table~\ref{tab:fewnerd}); (2)~\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\approx}2$\,pp vs.\ SciERC 13.1\,pp); (3)~\textit{LP-quality alignment}, measured as within-instance $\rho(\text{LP}, \text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
103	These factors are consistent with the observed pattern: Few-NERD (low degeneracy, adequate headroom, strong alignment) shows the largest LP gain ($+1.39$\,pp), SciERC (moderate degeneracy, large headroom, weak alignment) shows unreliable gains ($+0.04{\pm}0.48$\,pp, 3-seed mean${\pm}\sigma$; Table~\ref{tab:multiseed}), and CoNLL (high degeneracy, minimal headroom) shows no gain ($-0.85$\,pp).
104	This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\S\ref{sec:fewnerd}, \S\ref{sec:discussion}).
105	
106	%% ============================================================
107	\subsection{Cross-Dataset Contrast: Few-NERD}
108	\label{sec:fewnerd}
109	
110	\begin{table}[t]
111	\centering
112	\small
113	\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Degen.\%: fraction with identical F1 across all samples. $p$: paired bootstrap vs.\ greedy. Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed: $+0.04{\pm}0.48$~pp; Table~\ref{tab:multiseed}). Protocol details in \S\ref{sec:evaluation}; epoch choices in Appendix~\ref{app:epoch_confound}.}
114	\label{tab:fewnerd}
115	\resizebox{\columnwidth}{!}{%
116	\begin{tabular}{@{}lrccccr@{}}
117	\toprule
118	Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
119	\midrule
120	CoNLL & 2{,}756 & .908 & 48.4\% & .302 & $-$0.85\,pp & 1.0 \\
121	SciERC & 529 & .644 & 17.8\% & .205 & $+$0.61\,pp & .193 \\
122	Few-NERD & 32{,}565 & .748 & 13.8\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
123	\bottomrule
124	\end{tabular}}
125	\end{table}
126	
127	Few-NERD (Table~\ref{tab:fewnerd}) confirms that LP selection effectiveness is inversely associated with degeneracy.
128	Under standard early stopping, Few-NERD degeneracy is 13.8\% and LP achieves $+1.39$~pp ($p{<}0.001$), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp); LP is 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\ref{tab:cross_selection}).
129	Training convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\% and halves LP gains (Appendix~\ref{app:epoch_confound}).
130	
131	\paragraph{Degeneracy alone does not predict LP selection direction.}
132	Across 23 configurations, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP (Few-NERD per-entity-type $\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}).
133	Cross-dataset prediction requires LP signal quality: Few-NERD (within-instance $\rho{\approx}0.5$--$0.7$) shows consistent gains, while SciERC ($\rho{\approx}0.26$, even at matched duration $\rho{=}0.319$; Table~\ref{tab:epoch_scierc}) does not.
134	Conditional analysis on the favorable subset yields $+2.47$~pp on SciERC but remains negative on CoNLL (Appendix~\ref{app:conditional_decomp}).
135	
136	\begin{figure}[t]
137	\centering
138	\includegraphics[width=\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}
139	\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
140	\label{fig:degeneracy_scatter}
141	\end{figure}
142	
143	Structural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\ref{app:n_scaling}.
144	
145	%% ============================================================
146	\subsection{Robustness}
147	\label{sec:robustness_main}
148	
149	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
150	Signal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; $m{=}3$ raters, interpret with caution given low $m$; exact $p{\approx}0.028$; Table~\ref{tab:ranking-stability}).
151	NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\caption{Scale ablation: Qwen3-8B vs.\ 4B NER quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\ref{app:re_extension}.}
157	\label{tab:scale_ablation}
158	\begin{tabular}{@{}ll cc r@{}}
159	\toprule
160	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
161	\midrule
162	CoNLL & SJ & .436 & .422 & $-$.014 \\
163	      & FK & .400 & .418 & $+$.018 \\
164	SciERC & SJ & .360 & .422 & $+$.062 \\
165	       & FK & .267 & .326 & $+$.059 \\
166	\bottomrule
167	\end{tabular}
168	\end{table}
169	
170	\paragraph{Scale robustness.}
171	With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
172	Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
173	
174	\paragraph{LoRA-rank ablation.}
175	LoRA rank${=}8$ (vs.\ 32) lowers degeneracy to 7.2\% but LP remains below greedy ($\rho(\text{LP}, \text{F1}){\approx}0.24$); temperature manipulation ($T{=}1.2$; \S\ref{sec:discussion}) provides a cleaner diversity test, confirming that low degeneracy and adequate alignment are independently necessary.
176	
177	\paragraph{Supervised signal combination.}
178	Supervised classifiers (logistic regression, MLP, random forest; 5-fold CV, 3-seed mean, $N{=}16$) and a DeBERTa-v3-base verifier encoding input-output pairs all fail to close the selection gap: selection F1 remains at or below greedy (Appendix~\ref{app:supervised_combination}).
179	
180	Hidden state probes (MLP on final-layer representations) achieve higher quality correlation than LP on SciERC ($\rho{=}0.388$ vs.\ $0.283$, $+37$\%) but do not improve selection (gap closure $-5.1$\% vs.\ $+4.8$\%; Appendix~\ref{app:hidden_probe}). The correlation-selection gap extends to model-internal representations.
181	
182	%% ============================================================
183	\subsection{Prescriptive Results}
184	\label{sec:prescriptive}
185	
186	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
187	
188	\paragraph{Entity-level construction.}
189	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its LP-weighted or uniform frequency across $N$ samples and retain those exceeding a confirmation threshold $\theta{=}2/N$ (an entity is included if it appears in ${\geq}2$ of $N$ samples). This empirically robust default achieves the best or near-best F1 across all datasets, and the optimum is stable within $\theta \in [0.15, 0.35]$ (Appendix~\ref{app:theta_sweep}; $\theta{=}0.5$ majority baseline in Appendix~\ref{app:entity_merge}).
190	
191	\begin{table}[t]
192	\centering
193	\small
194	\caption{Entity-level construction vs.\ greedy decoding ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$: 3 seeds SciERC, 4 seeds Few-NERD). LP: LP-weighted entity aggregation; Unif.: frequency-based. $\theta{=}2/N$ (default heuristic). $p$: seed-42 paired bootstrap vs.\ greedy; LP-weighted positive across all seeds. Best per dataset in \textbf{bold}.}
195	\label{tab:entity_construction}
196	\resizebox{\columnwidth}{!}{%
197	\begin{tabular}{@{}llcccc@{}}
198	\toprule
199	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
200	\midrule
201	SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
202	       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
203	\addlinespace
204	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
205	         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
206	\addlinespace
207	CoNLL & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
208	\bottomrule
209	\end{tabular}}
210	\end{table}
211	
212	LP-weighted construction significantly improves over greedy on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$; Table~\ref{tab:entity_construction}), with LP-weighted gains positive across all 7 seed-dataset combinations, recovering approximately 8\% (SciERC) and 11\% (Few-NERD) of oracle headroom. CoNLL shows no significant gain ($-0.39$\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures.
213	$N$-scaling results are reported in Appendix~\ref{app:n_scaling}.
214	
215	\paragraph{Construction and LP selection are complementary.}
216	Construction dominates on SciERC ($+1.02$\,pp vs.\ LP selection $+0.04{\pm}0.48$\,pp, not significant), where LP-quality alignment is weak (within-instance $\rho{\approx}0.2$).
217	On Few-NERD, both methods yield comparable gains (construction $+1.40$\,pp, LP selection $+1.39$\,pp; Tables~\ref{tab:entity_construction}, \ref{tab:fewnerd}), where alignment is strong ($\rho{\approx}0.5$--$0.7$).
218	The gating criterion is LP-quality alignment: when alignment is weak, construction is the only effective strategy; when alignment is strong, both methods succeed.
219	
220	\paragraph{LP-alignment gating.}
221	We probe 50 held-out validation instances to estimate within-instance $\rho(\text{LP}, \text{F1})$. Above threshold $0.3$, LP selection is applied; below it, entity construction is used instead; when construction yields negative gain (as on CoNLL), the protocol defaults to greedy decoding. Adjusted $\rho$ scores on the dev split (SciERC $0.167$, CoNLL $0.065$, Few-NERD $0.516$) correctly route all three datasets, with dev-set routing matching test-set routing 3/3. This preliminary protocol requires further validation with larger validation sets. Two caveats apply: (a) the protocol is validated on three datasets with large inter-dataset margins; (b) on high-degeneracy datasets (CoNLL, valid ratio 22\%), the adjusted score magnitude is noisy but the routing decision remains robust due to wide margin from the $0.3$ threshold.
222	
223	\paragraph{Selective prediction.}
224	Orthogonal to construction, QE signals support selective prediction: at 80\% coverage, retaining high-confidence instances yields $+5$--$8$\,pp F1 (AUPRC 0.70--0.92; VC strongest on Qwen, model-dependent on LLaMA; Table~\ref{tab:cross_selection}).
225	When selection fails, QE scores route low-confidence instances to human review.
226	
227	\phantomsection\label{sec:selection_results}
228	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "0408aa2e-0a6a-4cf3-8910-6477fb424e03",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern: Few-NERD (low degeneracy, adequate headroom, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (moderate degeneracy, large headroom, weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed mean${\\pm}\\sigma$; Table~\\ref{tab:multiseed}), and CoNLL (high degeneracy, minimal headroom) shows no gain ($-0.85$\\,pp).\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Degen.\\%: fraction with identical F1 across all samples. $p$: paired bootstrap vs.\\ greedy. Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed: $+0.04{\\pm}0.48$~pp; Table~\\ref{tab:multiseed}). Protocol details in \\S\\ref{sec:evaluation}; epoch choices in Appendix~\\ref{app:epoch_confound}.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nCoNLL & 2{,}756 & .908 & 48.4\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms that LP selection effectiveness is inversely associated with degeneracy.\nUnder standard early stopping, Few-NERD degeneracy is 13.8\\% and LP achieves $+1.39$~pp ($p{<}0.001$), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp); LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP (Few-NERD per-entity-type $\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD (within-instance $\\rho{\\approx}0.5$--$0.7$) shows consistent gains, while SciERC ($\\rho{\\approx}0.26$, even at matched duration $\\rho{=}0.319$; Table~\\ref{tab:epoch_scierc}) does not.\nConditional analysis on the favorable subset yields $+2.47$~pp on SciERC but remains negative on CoNLL (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nSignal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; $m{=}3$ raters, interpret with caution given low $m$; exact $p{\\approx}0.028$; Table~\\ref{tab:ranking-stability}).\nNER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B NER quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) provides a cleaner diversity test, confirming that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination.}\nSupervised classifiers (logistic regression, MLP, random forest; 5-fold CV, 3-seed mean, $N{=}16$) and a DeBERTa-v3-base verifier encoding input-output pairs all fail to close the selection gap: selection F1 remains at or below greedy (Appendix~\\ref{app:supervised_combination}).\n\nHidden state probes (MLP on final-layer representations) achieve higher quality correlation than LP on SciERC ($\\rho{=}0.388$ vs.\\ $0.283$, $+37$\\%) but do not improve selection (gap closure $-5.1$\\% vs.\\ $+4.8$\\%; Appendix~\\ref{app:hidden_probe}). The correlation-selection gap extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its LP-weighted or uniform frequency across $N$ samples and retain those exceeding a confirmation threshold $\\theta{=}2/N$ (an entity is included if it appears in ${\\geq}2$ of $N$ samples). This empirically robust default achieves the best or near-best F1 across all datasets, and the optimum is stable within $\\theta \\in [0.15, 0.35]$ (Appendix~\\ref{app:theta_sweep}; $\\theta{=}0.5$ majority baseline in Appendix~\\ref{app:entity_merge}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level construction vs.\\ greedy decoding ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$: 3 seeds SciERC, 4 seeds Few-NERD). LP: LP-weighted entity aggregation; Unif.: frequency-based. $\\theta{=}2/N$ (default heuristic). $p$: seed-42 paired bootstrap vs.\\ greedy; LP-weighted positive across all seeds. Best per dataset in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction significantly improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), with LP-weighted gains positive across all 7 seed-dataset combinations, recovering approximately 8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no significant gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures.\n$N$-scaling results are reported in Appendix~\\ref{app:n_scaling}.\n\n\\paragraph{Construction and LP selection are complementary.}\nConstruction dominates on SciERC ($+1.02$\\,pp vs.\\ LP selection $+0.04{\\pm}0.48$\\,pp, not significant), where LP-quality alignment is weak (within-instance $\\rho{\\approx}0.2$).\nOn Few-NERD, both methods yield comparable gains (construction $+1.40$\\,pp, LP selection $+1.39$\\,pp; Tables~\\ref{tab:entity_construction}, \\ref{tab:fewnerd}), where alignment is strong ($\\rho{\\approx}0.5$--$0.7$).\nThe gating criterion is LP-quality alignment: when alignment is weak, construction is the only effective strategy; when alignment is strong, both methods succeed.\n\n\\paragraph{LP-alignment gating.}\nWe probe 50 held-out validation instances to estimate within-instance $\\rho(\\text{LP}, \\text{F1})$. Above threshold $0.3$, LP selection is applied; below it, entity construction is used instead; when construction yields negative gain (as on CoNLL), the protocol defaults to greedy decoding. Adjusted $\\rho$ scores on the dev split (SciERC $0.167$, CoNLL $0.065$, Few-NERD $0.516$) correctly route all three datasets, with dev-set routing matching test-set routing 3/3. This preliminary protocol requires further validation with larger validation sets. Two caveats apply: (a) the protocol is validated on three datasets with large inter-dataset margins; (b) on high-degeneracy datasets (CoNLL, valid ratio 22\\%), the adjusted score magnitude is noisy but the routing decision remains robust due to wide margin from the $0.3$ threshold.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, retaining high-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; VC strongest on Qwen, model-dependent on LLaMA; Table~\\ref{tab:cross_selection}).\nWhen selection fails, QE scores route low-confidence instances to human review.\n\n\\phantomsection\\label{sec:selection_results}\n",
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019VTBKQFfqVse6Vwj6J6srd`</summary>

```json
{
  "server": "autodl-5090-b",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/72b_zeroshot/conll2003/full_signal_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "b934b885-bd90-48f2-90df-16a50d1b1735",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193bgCWya25ZAX7dK5GALnQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 25092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 710
      },
      "output_tokens": 28,
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

_source line 11 · 2026-05-19T10:31:10.316Z_

<details><summary>↩ Tool result · `toolu_019VTBKQFfqVse6Vwj6J6srd`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/struct_self_consist_ie/output/72b_zeroshot/conll2003/full_signal_report.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.82}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "d4498cc3-c0f4-4a33-b760-053210f70d74",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"cat: /root/autodl-tmp/struct_self_consist_ie/output/72b_zeroshot/conll2003/full_signal_report.json: No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.82}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/struct_self_consist_ie/output/72b_zeroshot/conll2003/full_signal_report.json: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.82}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The file doesn't exist at that path. Let me find the correct path for the 72B CoNLL results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "b5c307c2-06fc-40f9-8bc2-03998eab7a95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01848NozwUJ73QqoF61J3NAG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 25802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7588
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

_source line 13_

文件路径不对，先找一下 72B CoNLL 结果的实际位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "02665979-6034-4a56-acd1-4b49cd5ce181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01848NozwUJ73QqoF61J3NAG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 25802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7588
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014L8NywjfZSQdFLenFGFLJA`</summary>

```json
{
  "server": "autodl-5090-b",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output -path \"*72b*\" -type f -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "93683142-4ce9-4b04-afcc-a40183227b03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01848NozwUJ73QqoF61J3NAG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7588,
      "cache_read_input_tokens": 25802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7588
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

_source line 15 · 2026-05-19T10:31:16.731Z_

<details><summary>↩ Tool result · `toolu_014L8NywjfZSQdFLenFGFLJA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/72b_zeroshot/full_signal_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "65767c8d-c343-45ff-969a-4c77fc52301e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/output/72b_zeroshot/full_signal_report.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/72b_zeroshot/full_signal_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LGvtjzHHA9TAVRkMLTAWFP`</summary>

```json
{
  "server": "autodl-5090-b",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/72b_zeroshot/full_signal_report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "9074cbfd-98a7-419a-92a4-36fc9ef784c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vFULScqev8e6TnpSHmGvN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 33390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 311
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

_source line 17 · 2026-05-19T10:31:20.064Z_

<details><summary>↩ Tool result · `toolu_01LGvtjzHHA9TAVRkMLTAWFP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"name\\\": \\\"scierc\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"n_samples\\\": 8,\\n    \\\"signals\\\": {\\n      \\\"SJ\\\": {\\n        \\\"rho\\\": 0.21675186319295206\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho\\\": 0.2268643208878706\\n      },\\n      \\\"LP\\\": {\\n        \\\"rho\\\": 0.08105629653698664\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho\\\": 0.18119551565265815\\n      },\\n      \\\"VC\\\": {\\n        \\\"rho\\\": 0.2774474257594968\\n      }\\n    },\\n    \\\"baselines\\\": {\\n      \\\"greedy\\\": {\\n        \\\"mean\\\": 0.3993396070428207,\\n        \\\"ci_lo\\\": 0.37502776576500585,\\n        \\\"ci_hi\\\": 0.42486000661804063\\n      },\\n      \\\"lp_selection\\\": {\\n        \\\"mean\\\": 0.39836297485580263,\\n        \\\"ci_lo\\\": 0.3737535525620703,\\n        \\\"ci_hi\\\": 0.4225968895628631\\n      },\\n      \\\"majority_vote\\\": {\\n        \\\"mean\\\": 0.4132481984238029,\\n        \\\"ci_lo\\\": 0.38694121463497644,\\n        \\\"ci_hi\\\": 0.43869730298443865\\n      },\\n      \\\"oracle\\\": {\\n        \\\"mean\\\": 0.5488904605161693,\\n        \\\"ci_lo\\\": 0.5240391828293529,\\n        \\\"ci_hi\\\": 0.5739669278421642\\n      },\\n      \\\"consensus_theta2n\\\": {\\n        \\\"mean\\\": 0.3941296496146429,\\n        \\\"ci_lo\\\": 0.37087546121195103,\\n        \\\"ci_hi\\\": 0.4162955855512563\\n      },\\n      \\\"consensus_lp_weighted\\\": {\\n        \\\"mean\\\": 0.41463973897533335,\\n        \\\"ci_lo\\\": 0.389058094011947,\\n        \\\"ci_hi\\\": 0.4393016036683333\\n      }\\n    },\\n    \\\"consensus_variants\\\": {\\n      \\\"high=0.5_medium=0.1\\\": {\\n        \\\"mean\\\": 0.39422476137663975,\\n        \\\"ci_lo\\\": 0.3699544254853355,\\n        \\\"ci_hi\\\": 0.4168598469711323\\n      },\\n      \\\"high=0.6_medium=0.2\\\": {\\n        \\\"mean\\\": 0.40482014598440896,\\n        \\\"ci_lo\\\": 0.3800751783977868,\\n        \\\"ci_hi\\\": 0.4289704071951375\\n      },\\n      \\\"high=0.7_medium=0.3\\\": {\\n        \\\"mean\\\": 0.4041807908537587,\\n        \\\"ci_lo\\\": 0.3789660455066882,\\n        \\\"ci_hi\\\": 0.4291235124883518\\n      }\\n    }\\n  },\\n  \\\"conll2003\\\": {\\n    \\\"name\\\": \\\"conll2003\\\",\\n    \\\"n_instances\\\": 2756,\\n    \\\"n_samples\\\": 8,\\n    \\\"signals\\\": {\\n      \\\"SJ\\\": {\\n        \\\"rho\\\": 0.30354061421753875\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho\\\": 0.301887682793874\\n      },\\n      \\\"LP\\\": {\\n        \\\"rho\\\": -0.002157580062126836\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho\\\": 0.2814097853058494\\n      },\\n      \\\"VC\\\": {\\n        \\\"rho\\\": 0.2966588513527752\\n      }\\n    },\\n    \\\"baselines\\\": {\\n      \\\"greedy\\\": {\\n        \\\"mean\\\": 0.7119536566539222,\\n        \\\"ci_lo\\\": 0.697258360251101,\\n        \\\"ci_hi\\\": 0.7270525119037152\\n      },\\n      \\\"lp_selection\\\": {\\n        \\\"mean\\\": 0.708038723230326,\\n        \\\"ci_lo\\\": 0.6938763800051895,\\n        \\\"ci_hi\\\": 0.7230017861592681\\n      },\\n      \\\"majority_vote\\\": {\\n        \\\"mean\\\": 0.7034165516271902,\\n        \\\"ci_lo\\\": 0.6885761129766483,\\n        \\\"ci_hi\\\": 0.718118226053764\\n      },\\n      \\\"oracle\\\": {\\n        \\\"mean\\\": 0.7650894811018455,\\n        \\\"ci_lo\\\": 0.7507759362657187,\\n        \\\"ci_hi\\\": 0.7792039849547808\\n      },\\n      \\\"consensus_theta2n\\\": {\\n        \\\"mean\\\": 0.7027692619428243,\\n        \\\"ci_lo\\\": 0.6887046437369796,\\n        \\\"ci_hi\\\": 0.7175057961115066\\n      },\\n      \\\"consensus_lp_weighted\\\": {\\n        \\\"mean\\\": 0.7082726789317058,\\n        \\\"ci_lo\\\": 0.6936909323750362,\\n        \\\"ci_hi\\\": 0.7230591888468175\\n      }\\n    },\\n    \\\"consensus_variants\\\": {\\n      \\\"high=0.5_medium=0.1\\\": {\\n        \\\"mean\\\": 0.7046208187462513,\\n        \\\"ci_lo\\\": 0.6903098076872617,\\n        \\\"ci_hi\\\": 0.7192922805098889\\n      },\\n      \\\"high=0.6_medium=0.2\\\": {\\n        \\\"mean\\\": 0.7073462347904576,\\n        \\\"ci_lo\\\": 0.6926564367812286,\\n        \\\"ci_hi\\\": 0.7219813980574267\\n      },\\n      \\\"high=0.7_medium=0.3\\\": {\\n        \\\"mean\\\": 0.7088965336492425,\\n        \\\"ci_lo\\\": 0.6944601050831575,\\n        \\\"ci_hi\\\": 0.7236702644433051\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "91699e4f-7450-465c-8408-8af5b8636c2f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc\\\\\\\": {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"scierc\\\\\\\",\\\\n    \\\\\\\"n_instances\\\\\\\": 529,\\\\n    \\\\\\\"n_samples\\\\\\\": 8,\\\\n    \\\\\\\"signals\\\\\\\": {\\\\n      \\\\\\\"SJ\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.21675186319295206\\\\n      },\\\\n      \\\\\\\"FK\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.2268643208878706\\\\n      },\\\\n      \\\\\\\"LP\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.08105629653698664\\\\n      },\\\\n      \\\\\\\"EM\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.18119551565265815\\\\n      },\\\\n      \\\\\\\"VC\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.2774474257594968\\\\n      }\\\\n    },\\\\n    \\\\\\\"baselines\\\\\\\": {\\\\n      \\\\\\\"greedy\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.3993396070428207,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.37502776576500585,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.42486000661804063\\\\n      },\\\\n      \\\\\\\"lp_selection\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.39836297485580263,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.3737535525620703,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.4225968895628631\\\\n      },\\\\n      \\\\\\\"majority_vote\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.4132481984238029,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.38694121463497644,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.43869730298443865\\\\n      },\\\\n      \\\\\\\"oracle\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.5488904605161693,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.5240391828293529,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.5739669278421642\\\\n      },\\\\n      \\\\\\\"consensus_theta2n\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.3941296496146429,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.37087546121195103,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.4162955855512563\\\\n      },\\\\n      \\\\\\\"consensus_lp_weighted\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.41463973897533335,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.389058094011947,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.4393016036683333\\\\n      }\\\\n    },\\\\n    \\\\\\\"consensus_variants\\\\\\\": {\\\\n      \\\\\\\"high=0.5_medium=0.1\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.39422476137663975,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.3699544254853355,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.4168598469711323\\\\n      },\\\\n      \\\\\\\"high=0.6_medium=0.2\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.40482014598440896,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.3800751783977868,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.4289704071951375\\\\n      },\\\\n      \\\\\\\"high=0.7_medium=0.3\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.4041807908537587,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.3789660455066882,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.4291235124883518\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"conll2003\\\\\\\": {\\\\n    \\\\\\\"name\\\\\\\": \\\\\\\"conll2003\\\\\\\",\\\\n    \\\\\\\"n_instances\\\\\\\": 2756,\\\\n    \\\\\\\"n_samples\\\\\\\": 8,\\\\n    \\\\\\\"signals\\\\\\\": {\\\\n      \\\\\\\"SJ\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.30354061421753875\\\\n      },\\\\n      \\\\\\\"FK\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.301887682793874\\\\n      },\\\\n      \\\\\\\"LP\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": -0.002157580062126836\\\\n      },\\\\n      \\\\\\\"EM\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.2814097853058494\\\\n      },\\\\n      \\\\\\\"VC\\\\\\\": {\\\\n        \\\\\\\"rho\\\\\\\": 0.2966588513527752\\\\n      }\\\\n    },\\\\n    \\\\\\\"baselines\\\\\\\": {\\\\n      \\\\\\\"greedy\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.7119536566539222,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.697258360251101,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.7270525119037152\\\\n      },\\\\n      \\\\\\\"lp_selection\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.708038723230326,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.6938763800051895,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.7230017861592681\\\\n      },\\\\n      \\\\\\\"majority_vote\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.7034165516271902,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.6885761129766483,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.718118226053764\\\\n      },\\\\n      \\\\\\\"oracle\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.7650894811018455,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.7507759362657187,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.7792039849547808\\\\n      },\\\\n      \\\\\\\"consensus_theta2n\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.7027692619428243,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.6887046437369796,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.7175057961115066\\\\n      },\\\\n      \\\\\\\"consensus_lp_weighted\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.7082726789317058,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.6936909323750362,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.7230591888468175\\\\n      }\\\\n    },\\\\n    \\\\\\\"consensus_variants\\\\\\\": {\\\\n      \\\\\\\"high=0.5_medium=0.1\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.7046208187462513,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.6903098076872617,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.7192922805098889\\\\n      },\\\\n      \\\\\\\"high=0.6_medium=0.2\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.7073462347904576,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.6926564367812286,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.7219813980574267\\\\n      },\\\\n      \\\\\\\"high=0.7_medium=0.3\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.7088965336492425,\\\\n        \\\\\\\"ci_lo\\\\\\\": 0.6944601050831575,\\\\n        \\\\\\\"ci_hi\\\\\\\": 0.7236702644433051\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.33}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"name\\\": \\\"scierc\\\",\\n    \\\"n_instances\\\": 529,\\n    \\\"n_samples\\\": 8,\\n    \\\"signals\\\": {\\n      \\\"SJ\\\": {\\n        \\\"rho\\\": 0.21675186319295206\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho\\\": 0.2268643208878706\\n      },\\n      \\\"LP\\\": {\\n        \\\"rho\\\": 0.08105629653698664\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho\\\": 0.18119551565265815\\n      },\\n      \\\"VC\\\": {\\n        \\\"rho\\\": 0.2774474257594968\\n      }\\n    },\\n    \\\"baselines\\\": {\\n      \\\"greedy\\\": {\\n        \\\"mean\\\": 0.3993396070428207,\\n        \\\"ci_lo\\\": 0.37502776576500585,\\n        \\\"ci_hi\\\": 0.42486000661804063\\n      },\\n      \\\"lp_selection\\\": {\\n        \\\"mean\\\": 0.39836297485580263,\\n        \\\"ci_lo\\\": 0.3737535525620703,\\n        \\\"ci_hi\\\": 0.4225968895628631\\n      },\\n      \\\"majority_vote\\\": {\\n        \\\"mean\\\": 0.4132481984238029,\\n        \\\"ci_lo\\\": 0.38694121463497644,\\n        \\\"ci_hi\\\": 0.43869730298443865\\n      },\\n      \\\"oracle\\\": {\\n        \\\"mean\\\": 0.5488904605161693,\\n        \\\"ci_lo\\\": 0.5240391828293529,\\n        \\\"ci_hi\\\": 0.5739669278421642\\n      },\\n      \\\"consensus_theta2n\\\": {\\n        \\\"mean\\\": 0.3941296496146429,\\n        \\\"ci_lo\\\": 0.37087546121195103,\\n        \\\"ci_hi\\\": 0.4162955855512563\\n      },\\n      \\\"consensus_lp_weighted\\\": {\\n        \\\"mean\\\": 0.41463973897533335,\\n        \\\"ci_lo\\\": 0.389058094011947,\\n        \\\"ci_hi\\\": 0.4393016036683333\\n      }\\n    },\\n    \\\"consensus_variants\\\": {\\n      \\\"high=0.5_medium=0.1\\\": {\\n        \\\"mean\\\": 0.39422476137663975,\\n        \\\"ci_lo\\\": 0.3699544254853355,\\n        \\\"ci_hi\\\": 0.4168598469711323\\n      },\\n      \\\"high=0.6_medium=0.2\\\": {\\n        \\\"mean\\\": 0.40482014598440896,\\n        \\\"ci_lo\\\": 0.3800751783977868,\\n        \\\"ci_hi\\\": 0.4289704071951375\\n      },\\n      \\\"high=0.7_medium=0.3\\\": {\\n        \\\"mean\\\": 0.4041807908537587,\\n        \\\"ci_lo\\\": 0.3789660455066882,\\n        \\\"ci_hi\\\": 0.4291235124883518\\n      }\\n    }\\n  },\\n  \\\"conll2003\\\": {\\n    \\\"name\\\": \\\"conll2003\\\",\\n    \\\"n_instances\\\": 2756,\\n    \\\"n_samples\\\": 8,\\n    \\\"signals\\\": {\\n      \\\"SJ\\\": {\\n        \\\"rho\\\": 0.30354061421753875\\n      },\\n      \\\"FK\\\": {\\n        \\\"rho\\\": 0.301887682793874\\n      },\\n      \\\"LP\\\": {\\n        \\\"rho\\\": -0.002157580062126836\\n      },\\n      \\\"EM\\\": {\\n        \\\"rho\\\": 0.2814097853058494\\n      },\\n      \\\"VC\\\": {\\n        \\\"rho\\\": 0.2966588513527752\\n      }\\n    },\\n    \\\"baselines\\\": {\\n      \\\"greedy\\\": {\\n        \\\"mean\\\": 0.7119536566539222,\\n        \\\"ci_lo\\\": 0.697258360251101,\\n        \\\"ci_hi\\\": 0.7270525119037152\\n      },\\n      \\\"lp_selection\\\": {\\n        \\\"mean\\\": 0.708038723230326,\\n        \\\"ci_lo\\\": 0.6938763800051895,\\n        \\\"ci_hi\\\": 0.7230017861592681\\n      },\\n      \\\"majority_vote\\\": {\\n        \\\"mean\\\": 0.7034165516271902,\\n        \\\"ci_lo\\\": 0.6885761129766483,\\n        \\\"ci_hi\\\": 0.718118226053764\\n      },\\n      \\\"oracle\\\": {\\n        \\\"mean\\\": 0.7650894811018455,\\n        \\\"ci_lo\\\": 0.7507759362657187,\\n        \\\"ci_hi\\\": 0.7792039849547808\\n      },\\n      \\\"consensus_theta2n\\\": {\\n        \\\"mean\\\": 0.7027692619428243,\\n        \\\"ci_lo\\\": 0.6887046437369796,\\n        \\\"ci_hi\\\": 0.7175057961115066\\n      },\\n      \\\"consensus_lp_weighted\\\": {\\n        \\\"mean\\\": 0.7082726789317058,\\n        \\\"ci_lo\\\": 0.6936909323750362,\\n        \\\"ci_hi\\\": 0.7230591888468175\\n      }\\n    },\\n    \\\"consensus_variants\\\": {\\n      \\\"high=0.5_medium=0.1\\\": {\\n        \\\"mean\\\": 0.7046208187462513,\\n        \\\"ci_lo\\\": 0.6903098076872617,\\n        \\\"ci_hi\\\": 0.7192922805098889\\n      },\\n      \\\"high=0.6_medium=0.2\\\": {\\n        \\\"mean\\\": 0.7073462347904576,\\n        \\\"ci_lo\\\": 0.6926564367812286,\\n        \\\"ci_hi\\\": 0.7219813980574267\\n      },\\n      \\\"high=0.7_medium=0.3\\\": {\\n        \\\"mean\\\": 0.7088965336492425,\\n        \\\"ci_lo\\\": 0.6944601050831575,\\n        \\\"ci_hi\\\": 0.7236702644433051\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"
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
Now I have all the data I need. Let me organize:

**72B Zero-Shot Results:**

**SciERC:**
- greedy = 39.9%, oracle = 54.9%, headroom = 15.0pp
- Signals: VC ρ=0.277, FK ρ=0.227, SJ ρ=0.217, EM ρ=0.181, LP ρ=0.081

**CoNLL:**
- greedy = 71.2%, oracle = 76.5%, headroom = 5.3pp
- Signals: SJ ρ=0.304, FK ρ=0.302, VC ρ=0.297, EM ρ=0.281, LP ρ=-0.002
  
Looking at the experiments.tex structure, I see there are already six main sections covering setup, quality estimation results, the correlation-selection gap, the Few-NERD contrast, robustness analysis, and prescriptive results. There's a scale ablation table in the robustness section comparing 8B and 4B models, and I need to add a new subsection.

The best placement would be after the Robustness section and before Prescriptive Results, since this new subsection on scaling behavior naturally extends the robustness analysis to larger models. The key insight I'm exploring is whether the performance gap between zero-shot and fine-tuned approaches persists when scaling up to 72B, and how degeneracy and signal rankings shift at this larger scale. Looking at the SciERC numbers, the 72B zero-shot results show a substantial gap compared to the 8B fine-tuned baseline, which suggests the scaling behavior is worth examining in detail. Looking at the remaining signal values and thinking through the structure, I need to organize this around how the performance gap and degeneracy patterns shift across model scales, distinguishing between the fine-tuned and zero-shot regimes. I'll set up placeholders for the scaling curve visualization and comparison table, then work through the narrative with the 72B data I have while marking what still needs to be filled in. I'm looking at the performance metrics for 72B zero-shot across both datasets. On SciERC, the model achieves 39.9% greedy accuracy with substantial headroom to oracle at 54.9%, and the uncertainty estimates show varying correlation strengths, with consensus-based methods providing modest improvements over greedy. CoNLL shows much tighter performance at 71.2% greedy with only 5.3pp headroom to oracle, indicating the model is already quite confident on this task.

Now I'm structuring the LaTeX table to compare 8B fine-tuned versus 72B zero-shot results across both datasets, displaying greedy accuracy, oracle bounds, and the correlation coefficients for different uncertainty signals.

Writing LaTeX table... Generating the comparison table...

I'm noticing the zero-shot performance drops significantly compared to fine-tuned models—the greedy F1 scores are much lower across both datasets, which makes sense without task-specific training. But the interesting part is that the headroom between greedy and constrained decoding is actually larger in zero-shot settings, suggesting there's more room for improvement through better decoding strategies when the model hasn't been fine-tuned.

The signal correlations are weaker in zero-shot too, particularly for LP on CoNLL where it's essentially uninformative. What's consistent though is that LP-weighted construction still manages to help on SciERC even without fine-tuning, which points to entity-level aggregation being more robust across different training regimes.

Writing the subsection... Looking at the performance comparison across model scales, the 8B fine-tuned models substantially outperform the 72B zero-shot variant on SciERC, though the gap narrows on CoNLL where the larger model shows more competitive greedy performance. The correlation patterns remain consistent—all three selection methods show positive correlations with oracle performance—but the magnitudes are notably weaker in the zero-shot setting, suggesting that the signal behavior I observed earlier holds across different scales and training regimes. The 72B zero-shot results show a different pattern: lower absolute performance but larger oracle headroom, yet LP selection still fails to improve over greedy despite this expanded potential. I'm presenting the comparison in Table~\ref{tab:scale_comparison} and noting that the correlation-selection gap persists even at larger scale and in zero-shot settings.

I notice the signal quality degrades significantly in zero-shot—structural signals remain somewhat informative but at reduced magnitude compared to the fine-tuned 8B baseline, with LP correlation dropping to near zero on CoNLL.

Entity-level construction helps partially compensate for this degradation, where LP-weighted aggregation provides a modest improvement on SciERC, though I still need to report the corresponding results for CoNLL at the 72B scale.

Generating comparison table... Completing the results table with the zero-shot CoNLL metrics, then I need to create a scaling curve figure showing how greedy and oracle F1 scores, headroom, and signal quality vary across the different model sizes in both fine-tuned and zero-shot settings. I need to verify the CoNLL 8B oracle value against the existing paper data—the table shows CoNLL greedy at .908 with an LP delta of -0.85pp, and there's mention of roughly 2pp oracle headroom, which would put the 8B FT oracle around .928. I'll keep that as a TODO for now since I don't have the exact figure. Looking at the existing scale ablation table, it already compares 8B versus 4B results, and there's a reference to 8B showing 17.8% versus 4B's 10.4% on SciERC for degeneracy, so my new section should build on that foundation while extending to 72B. For placement, I think this fits best between the Robustness section and Prescriptive Results, since that maintains a logical narrative flow.

Now I'm looking at the exact line numbers to position this correctly—Robustness ends around line 180, and Prescriptive Results begins at line 182, so I'll insert the new subsection between those two points. I'm deciding whether to create a new subsection for scaling behavior focused on the 72B zero-shot results, or integrate it with the existing 4B/8B fine-tuned scale robustness paragraph—I think keeping them separate makes sense since they address different regimes. Now I'm working through the oracle headroom calculations for CoNLL 8B, trying to extract the exact numbers from the paper's tables and existing text to verify my estimates. I should stick with the numbers from the paper rather than chasing down additional sources. Now I'm inserting a new subsection on scaling behavior between the Robustness and Prescriptive Results sections, which will include a table comparing the 8B fine-tuned models against the 72B zero-shot results.

Writing LaTeX table... Generating markdown table...

The results show that the zero-shot 72B model has significantly lower greedy F1 scores compared to the fine-tuned 8B across both datasets, but interestingly provides more oracle headroom, suggesting it has greater potential for improvement with better decoding strategies.

However, LP selection fails to capitalize on this expanded headroom and actually underperforms greedy decoding on both datasets, with the LP correlation coefficient dropping dramatically in the zero-shot setting. The structural signals like VC and SJ remain positive but weaker without fine-tuning, and the LP signal degrades substantially.

I'm noting that entity-level aggregation does provide some recovery—weighted LP aggregation gains about 1.6 percentage points on SciERC in the zero-shot regime, which is comparable to fine-tuned performance. There are several gaps I need to address: I should run the 72B model with fine-tuning to see if larger scale recovers signal quality, report degeneracy rates for the 72B zero-shot variant, and add the CoNLL results for entity construction at 72B scale. I'm also planning to create a scaling curve visualization showing performance across the different model sizes. Generating the results table... I'm carefully extracting the numerical values from the SciERC results for the 72B zero-shot model and rounding them appropriately for the table. Now I need to construct the exact string replacement to insert this new section right before the Prescriptive Results subsection, making sure the formatting and LaTeX syntax align properly. I'm verifying these numbers against what I cited in the paper. The consensus_lp_weighted score of 0.4146 for SciERC entity construction is indeed 41.5%, which is 1.6pp higher than greedy's 39.9%. For LP selection, SciERC shows a 0.1pp drop, and CoNLL shows a 0.4pp drop compared to greedy. Now I'm checking the oracle performance claim about CoNLL showing approximately 2pp improvement versus SciERC's 13.1pp.

Since the paper explicitly states "≈2pp" for CoNLL, I'll stick with that approximation rather than trying to compute a precise oracle value. I'm reconsidering the table format—instead of showing the oracle F1 directly, I can restructure it to display greedy scores alongside the headroom values, which avoids the awkwardness of approximate oracle numbers.

Reformatting the table... I'm deciding whether to include oracle values in the table or just show headroom instead. The headroom column captures what really matters—the gap between greedy and oracle—so I can drop the oracle column itself and mention specific oracle numbers from the 72B results in the narrative text instead. Now I need to check how this new section fits with the existing Robustness section that already references the scale_ablation table. I'll keep the table focused on the key correlation metrics—VC, SJ, FK, and LP—since those are the main signals the paper discusses, and I can address EM separately in the text or a footnote if needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "5a259066-1a49-42c5-951c-56930f063544",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtUyebqYGCYKh5amanHjp2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 33701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2288
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

数据拿到了。CoNLL 72B zero-shot: greedy=71.2%, oracle=76.5%, headroom=5.3pp; signals: SJ ρ=0.304, FK ρ=0.302, VC ρ=0.297, LP ρ=-0.002。LP selection 完全失效。

现在插入 Scaling Behavior subsection。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "8845b6bf-e31c-4b0b-951e-1d8e8ca67edc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtUyebqYGCYKh5amanHjp2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 33701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2288
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

<details open><summary>🔧 Tool call — Edit · `toolu_019vSQWHLccszdRA32W2iv1e`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "%% ============================================================\n\\subsection{Prescriptive Results}",
  "new_string": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nThe preceding analyses use LoRA fine-tuned 8B models (with 4B ablation in Table~\\ref{tab:scale_ablation}). We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the correlation-selection gap persists when model scale increases by an order of magnitude but task-specific training is removed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Headroom (Hdr.) = oracle $-$ greedy in pp. \\textcolor{red}{TODO: add 72B fine-tuned rows when available.}}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale_comparison} summarizes the comparison. Zero-shot 72B produces substantially lower greedy F1 (SciERC: 39.9\\% vs.\\ 64.5\\%; CoNLL: 71.2\\% vs.\\ 90.8\\%) but larger oracle headroom (SciERC: 15.0~pp vs.\\ 13.0~pp; CoNLL: 5.3~pp vs.\\ ${\\approx}$2~pp). LP selection fails to exceed greedy in either dataset (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), and LP $\\rho$ drops sharply (SciERC: $0.081$ vs.\\ $0.205$; CoNLL: $-0.002$ vs.\\ $0.302$). The correlation-selection gap persists across both scale and training regime.\n\n\\paragraph{Signal quality degrades without fine-tuning.}\nStructural signals remain positive in the zero-shot regime (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL) but at reduced magnitude relative to the fine-tuned 8B baseline. LP, which depends on calibrated token probabilities, is near zero on CoNLL ($\\rho{=}{-}0.002$), consistent with weaker task-specific calibration without fine-tuning. Entity-level construction partially compensates: LP-weighted aggregation yields $+1.6$~pp on SciERC zero-shot (41.5\\% vs.\\ 39.9\\% greedy), comparable to the $+1.0$~pp gain in the fine-tuned regime.\n\n\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot. (3) Add CoNLL 72B entity-construction results.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% ============================================================\n\\subsection{Prescriptive Results}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "e4600f8f-157b-4d0e-8791-edfb4cc64af9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtUyebqYGCYKh5amanHjp2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2288,
      "cache_read_input_tokens": 33701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2288
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

_source line 21 · 2026-05-19T10:33:57.991Z_

<details><summary>↩ Tool result · `toolu_019vSQWHLccszdRA32W2iv1e`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "94c13503-b0cd-4e9d-b852-7e9299cb313a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "%% ============================================================\n\\subsection{Prescriptive Results}",
    "newString": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nThe preceding analyses use LoRA fine-tuned 8B models (with 4B ablation in Table~\\ref{tab:scale_ablation}). We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the correlation-selection gap persists when model scale increases by an order of magnitude but task-specific training is removed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Headroom (Hdr.) = oracle $-$ greedy in pp. \\textcolor{red}{TODO: add 72B fine-tuned rows when available.}}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale_comparison} summarizes the comparison. Zero-shot 72B produces substantially lower greedy F1 (SciERC: 39.9\\% vs.\\ 64.5\\%; CoNLL: 71.2\\% vs.\\ 90.8\\%) but larger oracle headroom (SciERC: 15.0~pp vs.\\ 13.0~pp; CoNLL: 5.3~pp vs.\\ ${\\approx}$2~pp). LP selection fails to exceed greedy in either dataset (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), and LP $\\rho$ drops sharply (SciERC: $0.081$ vs.\\ $0.205$; CoNLL: $-0.002$ vs.\\ $0.302$). The correlation-selection gap persists across both scale and training regime.\n\n\\paragraph{Signal quality degrades without fine-tuning.}\nStructural signals remain positive in the zero-shot regime (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL) but at reduced magnitude relative to the fine-tuned 8B baseline. LP, which depends on calibrated token probabilities, is near zero on CoNLL ($\\rho{=}{-}0.002$), consistent with weaker task-specific calibration without fine-tuning. Entity-level construction partially compensates: LP-weighted aggregation yields $+1.6$~pp on SciERC zero-shot (41.5\\% vs.\\ 39.9\\% greedy), comparable to the $+1.0$~pp gain in the fine-tuned regime.\n\n\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot. (3) Add CoNLL 72B entity-construction results.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% ============================================================\n\\subsection{Prescriptive Results}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 52\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 52\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern: Few-NERD (low degeneracy, adequate headroom, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (moderate degeneracy, large headroom, weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed mean${\\pm}\\sigma$; Table~\\ref{tab:multiseed}), and CoNLL (high degeneracy, minimal headroom) shows no gain ($-0.85$\\,pp).\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Degen.\\%: fraction with identical F1 across all samples. $p$: paired bootstrap vs.\\ greedy. Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed: $+0.04{\\pm}0.48$~pp; Table~\\ref{tab:multiseed}). Protocol details in \\S\\ref{sec:evaluation}; epoch choices in Appendix~\\ref{app:epoch_confound}.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nCoNLL & 2{,}756 & .908 & 48.4\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms that LP selection effectiveness is inversely associated with degeneracy.\nUnder standard early stopping, Few-NERD degeneracy is 13.8\\% and LP achieves $+1.39$~pp ($p{<}0.001$), while all structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp); LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP (Few-NERD per-entity-type $\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD (within-instance $\\rho{\\approx}0.5$--$0.7$) shows consistent gains, while SciERC ($\\rho{\\approx}0.26$, even at matched duration $\\rho{=}0.319$; Table~\\ref{tab:epoch_scierc}) does not.\nConditional analysis on the favorable subset yields $+2.47$~pp on SciERC but remains negative on CoNLL (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\\Delta\\rho{=}{+}0.044$).\nSignal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; $m{=}3$ raters, interpret with caution given low $m$; exact $p{\\approx}0.028$; Table~\\ref{tab:ranking-stability}).\nNER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3-8B vs.\\ 4B NER quality estimation ($\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) provides a cleaner diversity test, confirming that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination.}\nSupervised classifiers (logistic regression, MLP, random forest; 5-fold CV, 3-seed mean, $N{=}16$) and a DeBERTa-v3-base verifier encoding input-output pairs all fail to close the selection gap: selection F1 remains at or below greedy (Appendix~\\ref{app:supervised_combination}).\n\nHidden state probes (MLP on final-layer representations) achieve higher quality correlation than LP on SciERC ($\\rho{=}0.388$ vs.\\ $0.283$, $+37$\\%) but do not improve selection (gap closure $-5.1$\\% vs.\\ $+4.8$\\%; Appendix~\\ref{app:hidden_probe}). The correlation-selection gap extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its LP-weighted or uniform frequency across $N$ samples and retain those exceeding a confirmation threshold $\\theta{=}2/N$ (an entity is included if it appears in ${\\geq}2$ of $N$ samples). This empirically robust default achieves the best or near-best F1 across all datasets, and the optimum is stable within $\\theta \\in [0.15, 0.35]$ (Appendix~\\ref{app:theta_sweep}; $\\theta{=}0.5$ majority baseline in Appendix~\\ref{app:entity_merge}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level construction vs.\\ greedy decoding ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$: 3 seeds SciERC, 4 seeds Few-NERD). LP: LP-weighted entity aggregation; Unif.: frequency-based. $\\theta{=}2/N$ (default heuristic). $p$: seed-42 paired bootstrap vs.\\ greedy; LP-weighted positive across all seeds. Best per dataset in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction significantly improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), with LP-weighted gains positive across all 7 seed-dataset combinations, recovering approximately 8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no significant gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities across samples recovers mentions that no single sample captures.\n$N$-scaling results are reported in Appendix~\\ref{app:n_scaling}.\n\n\\paragraph{Construction and LP selection are complementary.}\nConstruction dominates on SciERC ($+1.02$\\,pp vs.\\ LP selection $+0.04{\\pm}0.48$\\,pp, not significant), where LP-quality alignment is weak (within-instance $\\rho{\\approx}0.2$).\nOn Few-NERD, both methods yield comparable gains (construction $+1.40$\\,pp, LP selection $+1.39$\\,pp; Tables~\\ref{tab:entity_construction}, \\ref{tab:fewnerd}), where alignment is strong ($\\rho{\\approx}0.5$--$0.7$).\nThe gating criterion is LP-quality alignment: when alignment is weak, construction is the only effective strategy; when alignment is strong, both methods succeed.\n\n\\paragraph{LP-alignment gating.}\nWe probe 50 held-out validation instances to estimate within-instance $\\rho(\\text{LP}, \\text{F1})$. Above threshold $0.3$, LP selection is applied; below it, entity construction is used instead; when construction yields negative gain (as on CoNLL), the protocol defaults to greedy decoding. Adjusted $\\rho$ scores on the dev split (SciERC $0.167$, CoNLL $0.065$, Few-NERD $0.516$) correctly route all three datasets, with dev-set routing matching test-set routing 3/3. This preliminary protocol requires further validation with larger validation sets. Two caveats apply: (a) the protocol is validated on three datasets with large inter-dataset margins; (b) on high-degeneracy datasets (CoNLL, valid ratio 22\\%), the adjusted score magnitude is noisy but the routing decision remains robust due to wide margin from the $0.3$ threshold.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, retaining high-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; VC strongest on Qwen, model-dependent on LLaMA; Table~\\ref{tab:cross_selection}).\nWhen selection fails, QE scores route low-confidence instances to human review.\n\n\\phantomsection\\label{sec:selection_results}\n",
    "structuredPatch": [
      {
        "oldStart": 180,
        "oldLines": 6,
        "newStart": 180,
        "newLines": 45,
        "lines": [
          " Hidden state probes (MLP on final-layer representations) achieve higher quality correlation than LP on SciERC ($\\rho{=}0.388$ vs.\\ $0.283$, $+37$\\%) but do not improve selection (gap closure $-5.1$\\% vs.\\ $+4.8$\\%; Appendix~\\ref{app:hidden_probe}). The correlation-selection gap extends to model-internal representations.",
          " ",
          " %% ============================================================",
          "+\\subsection{Scaling Behavior}",
          "+\\label{sec:scaling}",
          "+",
          "+The preceding analyses use LoRA fine-tuned 8B models (with 4B ablation in Table~\\ref{tab:scale_ablation}). We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the correlation-selection gap persists when model scale increases by an order of magnitude but task-specific training is removed.",
          "+",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\small",
          "+\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Headroom (Hdr.) = oracle $-$ greedy in pp. \\textcolor{red}{TODO: add 72B fine-tuned rows when available.}}",
          "+\\label{tab:scale_comparison}",
          "+\\begin{tabular}{@{}llcccccc@{}}",
          "+\\toprule",
          "+Dataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\",
          "+\\midrule",
          "+SciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\",
          "+       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\",
          "+\\midrule",
          "+CoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\",
          "+       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          "+Table~\\ref{tab:scale_comparison} summarizes the comparison. Zero-shot 72B produces substantially lower greedy F1 (SciERC: 39.9\\% vs.\\ 64.5\\%; CoNLL: 71.2\\% vs.\\ 90.8\\%) but larger oracle headroom (SciERC: 15.0~pp vs.\\ 13.0~pp; CoNLL: 5.3~pp vs.\\ ${\\approx}$2~pp). LP selection fails to exceed greedy in either dataset (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), and LP $\\rho$ drops sharply (SciERC: $0.081$ vs.\\ $0.205$; CoNLL: $-0.002$ vs.\\ $0.302$). The correlation-selection gap persists across both scale and training regime.",
          "+",
          "+\\paragraph{Signal quality degrades without fine-tuning.}",
          "+Structural signals remain positive in the zero-shot regime (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL) but at reduced magnitude relative to the fine-tuned 8B baseline. LP, which depends on calibrated token probabilities, is near zero on CoNLL ($\\rho{=}{-}0.002$), consistent with weaker task-specific calibration without fine-tuning. Entity-level construction partially compensates: LP-weighted aggregation yields $+1.6$~pp on SciERC zero-shot (41.5\\% vs.\\ 39.9\\% greedy), comparable to the $+1.0$~pp gain in the fine-tuned regime.",
          "+",
          "+\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot. (3) Add CoNLL 72B entity-construction results.}",
          "+",
          "+\\begin{figure}[t]",
          "+\\centering",
          "+% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}",
          "+\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}",
          "+\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}",
          "+\\label{fig:scaling_curve}",
          "+\\end{figure}",
          "+",
          "+%% ============================================================",
          " \\subsection{Prescriptive Results}",
          " \\label{sec:prescriptive}",
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

_source line 22_

验证修改后的文件结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "d6a0e8e2-ad36-41b6-a1d5-72538e9809ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhUFuBikCig7APkye7kj8i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10256,
      "cache_read_input_tokens": 35989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10256
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Cy2uj4B4UrtWrwBgMoPUMo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 180,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "420de105-4a11-4193-bbdf-c6c708168d57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhUFuBikCig7APkye7kj8i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10256,
      "cache_read_input_tokens": 35989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10256
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

_source line 24 · 2026-05-19T10:34:01.417Z_

<details><summary>↩ Tool result · `toolu_01Cy2uj4B4UrtWrwBgMoPUMo`</summary>

```text
180	Hidden state probes (MLP on final-layer representations) achieve higher quality correlation than LP on SciERC ($\rho{=}0.388$ vs.\ $0.283$, $+37$\%) but do not improve selection (gap closure $-5.1$\% vs.\ $+4.8$\%; Appendix~\ref{app:hidden_probe}). The correlation-selection gap extends to model-internal representations.
181	
182	%% ============================================================
183	\subsection{Scaling Behavior}
184	\label{sec:scaling}
185	
186	The preceding analyses use LoRA fine-tuned 8B models (with 4B ablation in Table~\ref{tab:scale_ablation}). We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the correlation-selection gap persists when model scale increases by an order of magnitude but task-specific training is removed.
187	
188	\begin{table}[t]
189	\centering
190	\small
191	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Headroom (Hdr.) = oracle $-$ greedy in pp. \textcolor{red}{TODO: add 72B fine-tuned rows when available.}}
192	\label{tab:scale_comparison}
193	\begin{tabular}{@{}llcccccc@{}}
194	\toprule
195	Dataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\
196	\midrule
197	SciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\
198	       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\
199	\midrule
200	CoNLL  & 8B FT  & .908 & ${\approx}$2 & .424 & .436 & .400 & .302 \\
201	       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	Table~\ref{tab:scale_comparison} summarizes the comparison. Zero-shot 72B produces substantially lower greedy F1 (SciERC: 39.9\% vs.\ 64.5\%; CoNLL: 71.2\% vs.\ 90.8\%) but larger oracle headroom (SciERC: 15.0~pp vs.\ 13.0~pp; CoNLL: 5.3~pp vs.\ ${\approx}$2~pp). LP selection fails to exceed greedy in either dataset (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), and LP $\rho$ drops sharply (SciERC: $0.081$ vs.\ $0.205$; CoNLL: $-0.002$ vs.\ $0.302$). The correlation-selection gap persists across both scale and training regime.
207	
208	\paragraph{Signal quality degrades without fine-tuning.}
209	Structural signals remain positive in the zero-shot regime (VC $\rho{=}0.277$ on SciERC, SJ $\rho{=}0.304$ on CoNLL) but at reduced magnitude relative to the fine-tuned 8B baseline. LP, which depends on calibrated token probabilities, is near zero on CoNLL ($\rho{=}{-}0.002$), consistent with weaker task-specific calibration without fine-tuning. Entity-level construction partially compensates: LP-weighted aggregation yields $+1.6$~pp on SciERC zero-shot (41.5\% vs.\ 39.9\% greedy), comparable to the $+1.0$~pp gain in the fine-tuned regime.
210	
211	\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot. (3) Add CoNLL 72B entity-construction results.}
212	
213	\begin{figure}[t]
214	\centering
215	% \includegraphics[width=\columnwidth]{figures/fig_scaling_curve.pdf}
216	\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\rho$. Separate lines for fine-tuned vs.\ zero-shot.}
217	\caption{\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}
218	\label{fig:scaling_curve}
219	\end{figure}
220	
221	%% ============================================================
222	\subsection{Prescriptive Results}
223	\label{sec:prescriptive}
224	
225	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
226	
227	\paragraph{Entity-level construction.}
228	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its LP-weighted or uniform frequency across $N$ samples and retain those exceeding a confirmation threshold $\theta{=}2/N$ (an entity is included if it appears in ${\geq}2$ of $N$ samples). This empirically robust default achieves the best or near-best F1 across all datasets, and the optimum is stable within $\theta \in [0.15, 0.35]$ (Appendix~\ref{app:theta_sweep}; $\theta{=}0.5$ majority baseline in Appendix~\ref{app:entity_merge}).
229	
230	\begin{table}[t]
231	\centering
232	\small
233	\caption{Entity-level construction vs.\ greedy decoding ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$: 3 seeds SciERC, 4 seeds Few-NERD). LP: LP-weighted entity aggregation; Unif.: frequency-based. $\theta{=}2/N$ (default heuristic). $p$: seed-42 paired bootstrap vs.\ greedy; LP-weighted positive across all seeds. Best per dataset in \textbf{bold}.}
234	\label{tab:entity_construction}
235	\resizebox{\columnwidth}{!}{%
236	\begin{tabular}{@{}llcccc@{}}
237	\toprule
238	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
239	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "b82635b6-da3e-491f-8176-1f37238c8348",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "Hidden state probes (MLP on final-layer representations) achieve higher quality correlation than LP on SciERC ($\\rho{=}0.388$ vs.\\ $0.283$, $+37$\\%) but do not improve selection (gap closure $-5.1$\\% vs.\\ $+4.8$\\%; Appendix~\\ref{app:hidden_probe}). The correlation-selection gap extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nThe preceding analyses use LoRA fine-tuned 8B models (with 4B ablation in Table~\\ref{tab:scale_ablation}). We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the correlation-selection gap persists when model scale increases by an order of magnitude but task-specific training is removed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Headroom (Hdr.) = oracle $-$ greedy in pp. \\textcolor{red}{TODO: add 72B fine-tuned rows when available.}}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scale_comparison} summarizes the comparison. Zero-shot 72B produces substantially lower greedy F1 (SciERC: 39.9\\% vs.\\ 64.5\\%; CoNLL: 71.2\\% vs.\\ 90.8\\%) but larger oracle headroom (SciERC: 15.0~pp vs.\\ 13.0~pp; CoNLL: 5.3~pp vs.\\ ${\\approx}$2~pp). LP selection fails to exceed greedy in either dataset (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), and LP $\\rho$ drops sharply (SciERC: $0.081$ vs.\\ $0.205$; CoNLL: $-0.002$ vs.\\ $0.302$). The correlation-selection gap persists across both scale and training regime.\n\n\\paragraph{Signal quality degrades without fine-tuning.}\nStructural signals remain positive in the zero-shot regime (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL) but at reduced magnitude relative to the fine-tuned 8B baseline. LP, which depends on calibrated token probabilities, is near zero on CoNLL ($\\rho{=}{-}0.002$), consistent with weaker task-specific calibration without fine-tuning. Entity-level construction partially compensates: LP-weighted aggregation yields $+1.6$~pp on SciERC zero-shot (41.5\\% vs.\\ 39.9\\% greedy), comparable to the $+1.0$~pp gain in the fine-tuned regime.\n\n\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot. (3) Add CoNLL 72B entity-construction results.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples. For each unique entity mention, we compute its LP-weighted or uniform frequency across $N$ samples and retain those exceeding a confirmation threshold $\\theta{=}2/N$ (an entity is included if it appears in ${\\geq}2$ of $N$ samples). This empirically robust default achieves the best or near-best F1 across all datasets, and the optimum is stable within $\\theta \\in [0.15, 0.35]$ (Appendix~\\ref{app:theta_sweep}; $\\theta{=}0.5$ majority baseline in Appendix~\\ref{app:entity_merge}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level construction vs.\\ greedy decoding ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$: 3 seeds SciERC, 4 seeds Few-NERD). LP: LP-weighted entity aggregation; Unif.: frequency-based. $\\theta{=}2/N$ (default heuristic). $p$: seed-42 paired bootstrap vs.\\ greedy; LP-weighted positive across all seeds. Best per dataset in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule",
      "numLines": 60,
      "startLine": 180,
      "totalLines": 267
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

完成。`\subsection{Scaling Behavior}` 已插入 Robustness 和 Prescriptive Results 之间（L182-219），包含：

- **Table** (`tab:scale_comparison`): 8B FT vs 72B ZS 对比，含 greedy、headroom、四个 signal ρ 值；72B FT 行标 TODO
- **叙事**: 72B ZS headroom 更大但 LP selection 仍失败，signal ρ 全面下降，LP-weighted construction 仍有效 (+1.6pp SciERC)
- **Figure placeholder** (`fig:scaling_curve`): scaling curve 的 TODO 描述
- **TODO 标注**: 72B fine-tuned 结果、degeneracy 分析、CoNLL construction 结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "uuid": "8b301942-e074-40b7-af66-6e5a088caee5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrHoHbzXNiGYvf7X889iZL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 46245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2037
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

### Task result

_source line 26_

完成。`\subsection{Scaling Behavior}` 已插入 Robustness 和 Prescriptive Results 之间（L182-219），包含：

- **Table** (`tab:scale_comparison`): 8B FT vs 72B ZS 对比，含 greedy、headroom、四个 signal ρ 值；72B FT 行标 TODO
- **叙事**: 72B ZS headroom 更大但 LP selection 仍失败，signal ρ 全面下降，LP-weighted construction 仍有效 (+1.6pp SciERC)
- **Figure placeholder** (`fig:scaling_curve`): scaling curve 的 TODO 描述
- **TODO 标注**: 72B fine-tuned 结果、degeneracy 分析、CoNLL construction 结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 187167,
  "duration_api_ms": 187492,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "9eb7d17b-c430-4259-ad04-9f40405b46a9",
  "total_cost_usd": 0.6173672499999999,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 36441,
    "cache_read_input_tokens": 212060,
    "output_tokens": 11279,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36441,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 214,
        "cache_read_input_tokens": 46245,
        "cache_creation_input_tokens": 2037,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2037
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1471,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001556,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 11279,
      "cacheReadInputTokens": 212060,
      "cacheCreationInputTokens": 36441,
      "webSearchRequests": 0,
      "costUSD": 0.6158112499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8d017e7d-2fe2-48dd-8981-a131f1332d5f"
}
```

</details>

---
