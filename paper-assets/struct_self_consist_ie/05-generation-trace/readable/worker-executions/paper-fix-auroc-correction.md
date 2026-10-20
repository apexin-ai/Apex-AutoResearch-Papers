# paper fix auroc correction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_paper-fix_auroc_correction_20260519T141908.log`
- **Structured JSON:** [`36ea8efcfb861d3c974d.json`](../../sessions/36/36ea8efcfb861d3c974d.json)

## Before a recorded user message

40 recorded events

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
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
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
  "uuid": "cbff1a05-8b00-4174-9087-89155673a71d",
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
    "resetsAt": 1779207000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8d22fe3b-f523-4ff0-8fe7-86de482a769c",
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down into tasks:
1. Fix Table 1 AUROC values in experiments.tex
2. Add ρ-AUROC dissociation discussion in experiments.tex
3. Full-text AUROC audit across all tex files
4. Update provenance YAML

Let me start by reading the relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "c6ef0fad-7ddf-4181-b887-77e8325b0b21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

### Assistant

_source line 5_

开始执行。先并行读取所有需要修改和审查的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "579c1653-e55a-4302-a392-67930fb9ba80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_015S1Sk4oDV2oXskYw5JwgPj`</summary>

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
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "60d325f9-cdef-471a-8f09-c9d12ec851f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 7 · 2026-05-19T14:19:20.597Z_

<details><summary>↩ Tool result · `toolu_015S1Sk4oDV2oXskYw5JwgPj`</summary>

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
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
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
49	This collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.
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
103	These factors are consistent with the observed pattern (Table~\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\pm}0.48$\,pp, 3-seed; Table~\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\% of instances yield F1${=}0$.
104	Yet QE remains effective on WNUT-17 (VC $\rho{=}0.724$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
105	This characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\S\ref{sec:fewnerd}, \S\ref{sec:discussion}).
106	
107	%% ============================================================
108	\subsection{Cross-Dataset Contrast: Few-NERD}
109	\label{sec:fewnerd}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap.}
115	\label{tab:fewnerd}
116	\resizebox{\columnwidth}{!}{%
117	\begin{tabular}{@{}lrccccr@{}}
118	\toprule
119	Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
120	\midrule
121	WNUT-17 & 1{,}287 & .452 & 67.9\% & $-$.446 & $-$0.45\,pp & .72 \\
122	CoNLL & 2{,}756 & .908 & 48.4\% & .302 & $-$0.85\,pp & 1.0 \\
123	SciERC & 529 & .644 & 17.8\% & .205 & $+$0.61\,pp & .193 \\
124	Few-NERD & 32{,}565 & .748 & 13.8\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
125	\bottomrule
126	\end{tabular}}
127	\end{table}
128	
129	Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\ref{tab:cross_selection}).
130	Training convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\% and halves LP gains (Appendix~\ref{app:epoch_confound}).
131	
132	\paragraph{Degeneracy alone does not predict LP selection direction.}
133	Across 23 configurations, degeneracy does not predict LP gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}).
134	Cross-dataset prediction requires LP signal quality: Few-NERD ($\rho{\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\rho{\approx}0.26$) does not (Appendix~\ref{app:conditional_decomp}).
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
149	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
150	
151	\begin{table}[t]
152	\centering
153	\small
154	\caption{Scale ablation: 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
155	\label{tab:scale_ablation}
156	\begin{tabular}{@{}ll cc r@{}}
157	\toprule
158	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
159	\midrule
160	CoNLL & SJ & .436 & .422 & $-$.014 \\
161	      & FK & .400 & .418 & $+$.018 \\
162	SciERC & SJ & .360 & .422 & $+$.062 \\
163	       & FK & .267 & .326 & $+$.059 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\paragraph{Scale robustness.}
169	With Qwen3-4B (Table~\ref{tab:scale_ablation}), QE is comparable (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\ref{app:llama3b}).
170	Degeneracy scales with capability: 8B shows 17.8\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
171	
172	\paragraph{LoRA-rank ablation.}
173	LoRA rank${=}8$ (vs.\ 32) lowers degeneracy to 7.2\% but LP remains below greedy ($\rho(\text{LP}, \text{F1}){\approx}0.24$); temperature manipulation ($T{=}1.2$; \S\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.
174	
175	\paragraph{Supervised signal combination and hidden probes.}
176	Supervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\ref{app:supervised_combination}).
177	Hidden state probes improve correlation ($+37$\% on SciERC) but not selection (gap closure $-5.1$\%; Appendix~\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.
178	
179	%% ============================================================
180	\subsection{Scaling Behavior}
181	\label{sec:scaling}
182	
183	We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.
184	
185	\begin{table}[t]
186	\centering
187	\small
188	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp).}
189	\label{tab:scale_comparison}
190	\begin{tabular}{@{}llcccccc@{}}
191	\toprule
192	Dataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\
193	\midrule
194	SciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\
195	       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\
196	\midrule
197	CoNLL  & 8B FT  & .908 & ${\approx}$2 & .424 & .436 & .400 & .302 \\
198	       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	Zero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\ref{tab:scale_comparison}). LP $\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.
204	Structural signals remain positive but reduced (VC $\rho{=}0.277$ on SciERC, SJ $\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\,pp, 41.4\% vs.\ 39.9\% greedy) but not on CoNLL ($-0.37$\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.
205	
206	\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}
207	
208	\begin{figure}[t]
209	\centering
210	% \includegraphics[width=\columnwidth]{figures/fig_scaling_curve.pdf}
211	\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\rho$. Separate lines for fine-tuned vs.\ zero-shot.}
212	\caption{\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}
213	\label{fig:scaling_curve}
214	\end{figure}
215	
216	%% ============================================================
217	\subsection{Prescriptive Results}
218	\label{sec:prescriptive}
219	
220	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
221	
222	\paragraph{Entity-level construction.}
223	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\theta{=}2/N$ (${\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\theta$ stable within $[0.15, 0.35]$; Appendix~\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\,pp, CoNLL $-0.92$\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\,pp; \S\ref{sec:scaling}).
224	
225	\begin{table}[t]
226	\centering
227	\small
228	\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. Best in \textbf{bold}.}
229	\label{tab:entity_construction}
230	\resizebox{\columnwidth}{!}{%
231	\begin{tabular}{@{}llcccc@{}}
232	\toprule
233	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
234	\midrule
235	SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
236	       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
237	\addlinespace
238	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
239	         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
240	\addlinespace
241	CoNLL & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
242	\bottomrule
243	\end{tabular}}
244	\end{table}
245	
246	LP-weighted construction improves over greedy on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$; Table~\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\approx}$8\% (SciERC) and 11\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\ref{app:n_scaling}).
247	
248	\paragraph{LP-alignment gating (preliminary diagnostic).}
249	Construction and LP selection are complementary: construction dominates on SciERC ($+1.02$\,pp vs.\ LP $+0.04{\pm}0.48$\,pp, n.s.; $\rho{\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\ $+1.39$\,pp; $\rho{\approx}0.5$--$0.7$).
250	We estimate within-instance $\rho(\text{LP}, \text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\rho_{\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\approx}0$ (n.s.).
251	The protocol performs three-way routing: (1)~$\rho_{\text{adj}} \geq \tau{=}0.3$: apply LP selection; (2)~$\rho_{\text{adj}} < \tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.
252	This routes Few-NERD to LP selection ($+1.39$\,pp); SciERC, CoNLL, and WNUT-17 fall below $\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\,pp) for protection against negative outcomes (CoNLL $-0.39$\,pp, WNUT-17 n.s.).
253	Routing is stable across $\tau{\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.
254	
255	\paragraph{Selective prediction.}
256	Orthogonal to construction, QE signals support selective prediction: at 80\% coverage, filtering low-confidence instances yields $+5$--$8$\,pp F1 (AUPRC 0.70--0.92; Table~\ref{tab:cross_selection}).
257	
258	\phantomsection\label{sec:selection_results}
259	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "125aa789-55a1-4b2e-b4a7-c54214d8ec9c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.1$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 48.4\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}2$\\,pp vs.\\ SciERC 13.1\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 48.4\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination and hidden probes.}\nSupervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\nHidden state probes improve correlation ($+37$\\% on SciERC) but not selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp).}\n\\label{tab:scale_comparison}\n\\begin{tabular}{@{}llcccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 13.0 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$2 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3  & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nZero-shot 72B produces lower greedy F1 but larger oracle headroom (Table~\\ref{tab:scale_comparison}). LP $\\rho$ drops from $0.205$ to $0.081$ on SciERC and from $0.302$ to near zero on CoNLL; LP selection fails in both datasets (SciERC $-0.1$~pp, CoNLL $-0.4$~pp), confirming that the gap is a structural property of the task rather than a fine-tuning artifact.\nStructural signals remain positive but reduced (VC $\\rho{=}0.277$ on SciERC, SJ $\\rho{=}0.304$ on CoNLL). LP-weighted construction partially compensates on SciERC ($+1.5$\\,pp, 41.4\\% vs.\\ 39.9\\% greedy) but not on CoNLL ($-0.37$\\,pp), where limited headroom (5.3~pp) leaves little room for aggregation.\n\n\\textcolor{red}{TODO: (1) Add 72B fine-tuned results to determine whether fine-tuning at larger scale recovers signal quality. (2) Report degeneracy percentages for 72B zero-shot.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve. X-axis: model scale (4B, 8B, 72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\\theta{=}2/N$ (${\\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\\theta$ stable within $[0.15, 0.35]$; Appendix~\\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\\,pp, CoNLL $-0.92$\\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\\,pp; \\S\\ref{sec:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\\approx}$8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\\ref{app:n_scaling}).\n\n\\paragraph{LP-alignment gating (preliminary diagnostic).}\nConstruction and LP selection are complementary: construction dominates on SciERC ($+1.02$\\,pp vs.\\ LP $+0.04{\\pm}0.48$\\,pp, n.s.; $\\rho{\\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\\ $+1.39$\\,pp; $\\rho{\\approx}0.5$--$0.7$).\nWe estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\nThe protocol performs three-way routing: (1)~$\\rho_{\\text{adj}} \\geq \\tau{=}0.3$: apply LP selection; (2)~$\\rho_{\\text{adj}} < \\tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.\nThis routes Few-NERD to LP selection ($+1.39$\\,pp); SciERC, CoNLL, and WNUT-17 fall below $\\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\\,pp) for protection against negative outcomes (CoNLL $-0.39$\\,pp, WNUT-17 n.s.).\nRouting is stable across $\\tau{\\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, filtering low-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; Table~\\ref{tab:cross_selection}).\n\n\\phantomsection\\label{sec:selection_results}\n",
      "numLines": 259,
      "startLine": 1,
      "totalLines": 259
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_016GPC4h4kcqbSfo4m2MebDB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "f501b8db-7823-4736-90c2-896290344876",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 9 · 2026-05-19T14:19:21.086Z_

<details><summary>↩ Tool result · `toolu_016GPC4h4kcqbSfo4m2MebDB`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\textendash 8B models.
4	All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
5	For instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \textbf{correlation-selection gap}).
6	We identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.
7	The diagnostic naturally motivates entity-level \textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "a5000c02-cd55-4984-8494-8736b11f0b9b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nSelf-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \\textit{sets} of entities with partial overlap, where no majority vote analog exists.\nWe evaluate five confidence signals for quality estimation (QE) and sample selection on four NER benchmarks using fine-tuned 4B\\textendash 8B models.\nAll signals achieve reliable QE ($\\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\\,pp F1 at 80\\% coverage).\nFor instance-level selection, log-probability (LP) succeeds only where LP-quality alignment is strong, and gains are absent elsewhere despite large oracle headroom (the \\textbf{correlation-selection gap}).\nWe identify three qualitative factors: instance degeneracy, oracle headroom, and LP-quality alignment; degeneracy causally modulates LP within fixed settings but does not predict cross-dataset direction.\nThe diagnostic naturally motivates entity-level \\textit{construction}, adapting entity voting to stochastic sampling: LP-weighted aggregation improves F1 by $+1.40$\\,pp on Few-NERD and $+1.02$\\,pp on SciERC (multi-seed mean, $p{<}0.005$). Construction and LP selection are complementary, governed by LP-quality alignment.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01WPi5UFgfBNCJKJHSj9tbLG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "70267763-a210-488e-af04-c82950fc11e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 11 · 2026-05-19T14:19:21.465Z_

<details><summary>↩ Tool result · `toolu_01WPi5UFgfBNCJKJHSj9tbLG`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
13	For selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low instance degeneracy and adequate alignment are present, with gains scaling with $N$.
14	On SciERC, the observed LP gain ($+0.2$~pp, $p{=}0.29$) falls below the minimum detectable effect (${\approx}$1.5~pp at 80\% power, $n{=}529$) despite 13~pp oracle headroom. We term this disparity between quality estimation strength and selection effectiveness the \textbf{correlation-selection gap}.
15	Three factors qualitatively shape this gap: (a)~\textit{instance degeneracy} (13\textendash 87\% across our benchmarks) compresses the candidate space; (b)~\textit{oracle headroom} bounds the achievable gain; (c)~\textit{LP-quality alignment} (within-instance $\rho(\text{LP}, \text{F1})$) determines whether LP can discriminate candidates in non-degenerate instances (\S\ref{sec:selection_gap}).
16	Our diagnosis is complementary to minimum Bayes risk (MBR) utility misalignment \cite{eikema2025structured}: where MBR failures in structured prediction stem from poorly chosen utility functions, we find that degeneracy eliminates candidate diversity before utility alignment matters.
17	Within non-degenerate instances, MBR utility correlates positively with F1 ($\rho{=}0.52$; \S\ref{sec:discussion}).
18	Both mechanisms intensify with model capability: degeneracy rises with scale and training convergence (\S\ref{sec:discussion}). This creates a tension between model quality and test-time improvability.
19	
20	\begin{figure*}[t]
21	\centering
22	\includegraphics[width=\textwidth]{fig_overview}
23	\caption{Overview of the correlation-selection gap and its mitigation. \textbf{Left}: consistency signals reliably estimate instance-level quality ($\rho$ up to 0.45 on CoNLL; Table~\ref{tab:quality_estimation}). \textbf{Center}: instance-level signals assign identical scores to all samples from the same input, so best-of-$N$ selection cannot outperform greedy. \textbf{Right}: entity-level construction aggregates entities across samples via majority vote ($\theta{=}2/N$), bypassing the selection bottleneck ($+1.40$\,pp on Few-NERD, multi-seed mean; \S\ref{sec:prescriptive}).}
24	\label{fig:overview}
25	\end{figure*}
26	
27	We evaluate five signals from three families (structural, surface, and model-internal) on SciERC \cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
28	We vary candidate pool size ($N{\in}\{2,\ldots,32\}$), signal sophistication, and model capacity within the 4B\textendash 8B range; behavior at 70B+ scales remains an open question.
29	An exploratory extension to relation extraction is reported in Appendix~\ref{app:re_extension}.
30	Our contributions:
31	\begin{enumerate}
32	    \item \textbf{Quality estimation framework and selective prediction.}
33	    Five signals from three families evaluated on four NER benchmarks, two model families, and a 4B ablation, achieving reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82).
34	    QE enables selective prediction: filtering low-confidence instances at 80\% coverage yields $+5$--$8$\,pp F1 (area under the precision-recall curve [AUPRC] 0.70--0.92, VC strongest; \S\ref{sec:prescriptive}).
35	
36	    \item \textbf{Diagnostic of the correlation-selection gap.}
37	    For fine-tuned 4B--8B models, LP-quality alignment (within-instance $\rho(\text{LP}, \text{F1})$) is the primary predictor of selection success: LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) where alignment is strong, but not on benchmarks with weak alignment.
38	    Instance degeneracy causally modulates LP within fixed settings (epoch and temperature ablations), but does not predict cross-dataset direction ($\rho{=}0.052$, 23 configurations); structural signals fail by construction; supervised combinations and hidden state probes (Appendix~\ref{app:hidden_probe}) confirm the gap persists.
39	
40	    \item \textbf{Entity-level construction as a diagnostic-motivated mitigation.}
41	    The diagnostic naturally motivates entity-level aggregation, adapting entity voting from ensemble NER \cite{florian2003named} to stochastic sampling: LP-weighted construction yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC (multi-seed mean, $p{<}0.005$; \S\ref{sec:prescriptive}).
42	    Construction and LP selection are complementary on two informative datasets, governed by LP-quality alignment; a simple alignment-based gating protocol correctly routes datasets.
43	\end{enumerate}
44	
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "d954f941-1b63-41e7-830d-4f8118cac6cb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \\citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \\cite{snell2025scaling, brown2024monkeys}.\nBut named entity recognition (NER) poses a structurally different challenge: the output is a \\textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.\n\nPrior work on confidence estimation for LLM-based IE has conflated \\textit{quality estimation} (which inputs does the model handle reliably?) with \\textit{sample selection} (which of $N$ outputs is best?).\nExisting self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.\nUnlike \\citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we provide the first systematic empirical characterization of \\textit{when and why} LP-based selection succeeds or fails for structured prediction, diagnosing degeneracy and compression as the two blocking mechanisms.\nOur experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.\n\nA key distinction structures our analysis: four of five signals (Soft Jaccard, voting confidence, Fleiss' $\\kappa$, exact match) are instance-level aggregates that assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.\nAll signals achieve reliable quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82; Figure~\\ref{fig:overview}), supporting selective prediction.\nFor selection, LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) in settings where both low instance degeneracy and adequate alignment are present, with gains scaling with $N$.\nOn SciERC, the observed LP gain ($+0.2$~pp, $p{=}0.29$) falls below the minimum detectable effect (${\\approx}$1.5~pp at 80\\% power, $n{=}529$) despite 13~pp oracle headroom. We term this disparity between quality estimation strength and selection effectiveness the \\textbf{correlation-selection gap}.\nThree factors qualitatively shape this gap: (a)~\\textit{instance degeneracy} (13\\textendash 87\\% across our benchmarks) compresses the candidate space; (b)~\\textit{oracle headroom} bounds the achievable gain; (c)~\\textit{LP-quality alignment} (within-instance $\\rho(\\text{LP}, \\text{F1})$) determines whether LP can discriminate candidates in non-degenerate instances (\\S\\ref{sec:selection_gap}).\nOur diagnosis is complementary to minimum Bayes risk (MBR) utility misalignment \\cite{eikema2025structured}: where MBR failures in structured prediction stem from poorly chosen utility functions, we find that degeneracy eliminates candidate diversity before utility alignment matters.\nWithin non-degenerate instances, MBR utility correlates positively with F1 ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\nBoth mechanisms intensify with model capability: degeneracy rises with scale and training convergence (\\S\\ref{sec:discussion}). This creates a tension between model quality and test-time improvability.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{Overview of the correlation-selection gap and its mitigation. \\textbf{Left}: consistency signals reliably estimate instance-level quality ($\\rho$ up to 0.45 on CoNLL; Table~\\ref{tab:quality_estimation}). \\textbf{Center}: instance-level signals assign identical scores to all samples from the same input, so best-of-$N$ selection cannot outperform greedy. \\textbf{Right}: entity-level construction aggregates entities across samples via majority vote ($\\theta{=}2/N$), bypassing the selection bottleneck ($+1.40$\\,pp on Few-NERD, multi-seed mean; \\S\\ref{sec:prescriptive}).}\n\\label{fig:overview}\n\\end{figure*}\n\nWe evaluate five signals from three families (structural, surface, and model-internal) on SciERC \\cite{luan2018scierc} as a primary medium-difficulty test bed, with Few-NERD \\cite{ding2021fewnerd} (low-degeneracy contrast), CoNLL-2003 \\cite{tjongkimsang2003conll} (ceiling-effect control), and WNUT-17 \\cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).\nWe vary candidate pool size ($N{\\in}\\{2,\\ldots,32\\}$), signal sophistication, and model capacity within the 4B\\textendash 8B range; behavior at 70B+ scales remains an open question.\nAn exploratory extension to relation extraction is reported in Appendix~\\ref{app:re_extension}.\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Quality estimation framework and selective prediction.}\n    Five signals from three families evaluated on four NER benchmarks, two model families, and a 4B ablation, achieving reliable quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82).\n    QE enables selective prediction: filtering low-confidence instances at 80\\% coverage yields $+5$--$8$\\,pp F1 (area under the precision-recall curve [AUPRC] 0.70--0.92, VC strongest; \\S\\ref{sec:prescriptive}).\n\n    \\item \\textbf{Diagnostic of the correlation-selection gap.}\n    For fine-tuned 4B--8B models, LP-quality alignment (within-instance $\\rho(\\text{LP}, \\text{F1})$) is the primary predictor of selection success: LP achieves $+1.39$~pp on Few-NERD ($p{<}0.001$) where alignment is strong, but not on benchmarks with weak alignment.\n    Instance degeneracy causally modulates LP within fixed settings (epoch and temperature ablations), but does not predict cross-dataset direction ($\\rho{=}0.052$, 23 configurations); structural signals fail by construction; supervised combinations and hidden state probes (Appendix~\\ref{app:hidden_probe}) confirm the gap persists.\n\n    \\item \\textbf{Entity-level construction as a diagnostic-motivated mitigation.}\n    The diagnostic naturally motivates entity-level aggregation, adapting entity voting from ensemble NER \\cite{florian2003named} to stochastic sampling: LP-weighted construction yields $+1.40$\\,pp on Few-NERD and $+1.02$\\,pp on SciERC (multi-seed mean, $p{<}0.005$; \\S\\ref{sec:prescriptive}).\n    Construction and LP selection are complementary on two informative datasets, governed by LP-quality alignment; a simple alignment-based gating protocol correctly routes datasets.\n\\end{enumerate}\n\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01HHHeePZdWRSouN79qKPn6x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "fcea16a8-e1df-49bd-8b51-aab964648679",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 13 · 2026-05-19T14:19:22.126Z_

<details><summary>↩ Tool result · `toolu_01HHHeePZdWRSouN79qKPn6x`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Five confidence signals achieve reliable NER quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage). Instance-level selection fails due to degeneracy and LP compression; entity-level construction yields $+1.40$\,pp on Few-NERD and $+1.02$\,pp on SciERC ($p{<}0.005$), complementary with LP selection and governed by LP-quality alignment. For practitioners: use QE for selective prediction; apply construction when multi-sample generation is feasible; assess LP-alignment to route between strategies. As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \cite{cobbe2021verifiers} may be needed to close the remaining gap.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "19eb9961-2788-4deb-ad4f-4a31a26dd51e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nFive confidence signals achieve reliable NER quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82), enabling selective prediction ($+5$--$8$\\,pp F1 at 80\\% coverage). Instance-level selection fails due to degeneracy and LP compression; entity-level construction yields $+1.40$\\,pp on Few-NERD and $+1.02$\\,pp on SciERC ($p{<}0.005$), complementary with LP selection and governed by LP-quality alignment. For practitioners: use QE for selective prediction; apply construction when multi-sample generation is feasible; assess LP-alignment to route between strategies. As models improve, degeneracy rises and the selection window narrows; content-aware verifiers \\cite{cobbe2021verifiers} may be needed to close the remaining gap.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_0184atZL8nXgpcopihnxTHpb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "58f527e1-dee7-4a77-af64-cc4af7da18b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 15 · 2026-05-19T14:19:22.428Z_

<details><summary>↩ Tool result · `toolu_0184atZL8nXgpcopihnxTHpb`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
4	Three factors qualitatively constrain selection: instance degeneracy (17.8--67.9\%) compresses the candidate space, limited oracle headroom bounds achievable gains, and LP compression (within-instance $\rho$ 0.043--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\rho{=}0.524$) \cite{eikema2022sampling}.
5	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\ref{tab:nontied_main}), but $\varepsilon{=}0.05$ is post-hoc ($p_{\text{adj}}{=}0.14$ after joint correction; Appendix~\ref{app:epsilon_robustness}), so this is exploratory evidence.
6	Temperature disentangles degeneracy from alignment: at $T{=}1.2$, degeneracy drops to 14.9\% yet LP does not improve (median $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}); the selection window narrows as models improve \cite{wang2023selfconsistency, snell2025scaling}.
7	
8	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
9	Entity-level construction bypasses both failure mechanisms (Table~\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\S\ref{sec:prescriptive}).
10	Alternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\ref{app:dals}); our negative results are specific to fine-tuned models with constrained decoding (Appendix~\ref{app:when_selection_works}).
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "e0e39f3c-74d9-4c31-87e8-c07c69a940d2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\nThe decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \\cite{cobbe2021verifiers, venktesh2025trust}.\nThree factors qualitatively constrain selection: instance degeneracy (17.8--67.9\\%) compresses the candidate space, limited oracle headroom bounds achievable gains, and LP compression (within-instance $\\rho$ 0.043--0.667) prevents exploiting the remainder; within non-degenerate instances, MBR utility correlates positively with F1 (SJ median $\\rho{=}0.524$) \\cite{eikema2022sampling}.\nWhere compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP selection yields $+2.9$~pp ($p{=}0.004$; Table~\\ref{tab:nontied_main}), but $\\varepsilon{=}0.05$ is post-hoc ($p_{\\text{adj}}{=}0.14$ after joint correction; Appendix~\\ref{app:epsilon_robustness}), so this is exploratory evidence.\nTemperature disentangles degeneracy from alignment: at $T{=}1.2$, degeneracy drops to 14.9\\% yet LP does not improve (median $\\rho{=}0.225$; Table~\\ref{tab:t_degeneracy}); the selection window narrows as models improve \\cite{wang2023selfconsistency, snell2025scaling}.\n\n\\paragraph{From diagnosis to practice.}\\label{sec:selection_method}\nEntity-level construction bypasses both failure mechanisms (Table~\\ref{tab:entity_construction}), complementary with LP selection and governed by LP-quality alignment (\\S\\ref{sec:prescriptive}).\nAlternative strategies (DALS, MBR, DGS) fail to reliably beat greedy (Appendix~\\ref{app:dals}); our negative results are specific to fine-tuned models with constrained decoding (Appendix~\\ref{app:when_selection_works}).\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_014iNByTErxtxSjXawUd8W1S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "305d0a61-cec2-4c76-91b1-37039c89c410",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 17 · 2026-05-19T14:19:23.404Z_

<details><summary>↩ Tool result · reported error · `toolu_014iNByTErxtxSjXawUd8W1S`</summary>

```text
File content (41705 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "92358402-f4dc-4e93-9d0d-9784f95b9931",
  "tool_use_result": "Error: File content (41705 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01UiBuroBLCCiYAazW2qM2rf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "3ee6abb2-8e90-4b1f-b867-9c752ff6af4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 19 · 2026-05-19T14:19:23.870Z_

<details><summary>↩ Tool result · `toolu_01UiBuroBLCCiYAazW2qM2rf`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.
6	Adaptive variants gate on answer agreement \cite{aggarwal2023adaptive}, input difficulty \cite{wang2025make, feng2025optimal}, or response confidence \cite{kim2026reasc}; \citet{chen2025twofailures} diagnose SC failure modes without proposing gating.
7	All target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; \citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.
14	LLM-Blender \cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.
15	Our entity-level construction aggregates across samples from a single fine-tuned model, without requiring model diversity or prompt engineering.
16	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.
17	\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats; \S\ref{sec:discussion}) corroborates this for NER.
18	
19	\paragraph{Uncertainty estimation and MBR decoding.}
20	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic}; semantic uncertainty \cite{kuhn2023semantic, farquhar2024detecting} and P(True) \cite{kadavath2022language} provide model-internal alternatives.
21	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \cite{freitag2022high} and code generation where execution-based MBR improves selection \cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\rho{=}0.52$; \S\ref{sec:discussion}).
22	\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck.
23	Our QE results connect to selective prediction \cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.
24	
25	\paragraph{Best-of-$N$ with learned verifiers.}
26	\citet{gao2023scaling} establish BoN scaling laws and \citet{chen2021evaluating} define the pass@$k$ metric for code generation; our unsupervised signals face a more fundamental limitation than reward overoptimization.
27	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} and self-evaluation guided search \cite{xie2023selfevaluation} learn per-sample scoring.
28	CISC \cite{taubenfeld2025cisc} and Self-Certainty \cite{kang2025selfcertainty} derive per-sample confidence from hidden states rather than output statistics, but require architecture-specific access to intermediate representations; these hidden-state signals remain untested for structured prediction (\S Limitations).
29	Fine-tuning \cite{kirk2024understanding} and constrained decoding \cite{holtzman2020curious, vijayakumar2018diverse} both limit the diversity recoverable for selection.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "447d9792-d1de-486a-b563-ba9b869f938b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency \\cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \\cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.\nTest-time scaling studies \\cite{snell2025scaling, brown2024monkeys} and reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} rely on answer-level agreement.\nAdaptive variants gate on answer agreement \\cite{aggarwal2023adaptive}, input difficulty \\cite{wang2025make, feng2025optimal}, or response confidence \\cite{kim2026reasc}; \\citet{chen2025twofailures} diagnose SC failure modes without proposing gating.\nAll target discrete-answer reasoning; structured prediction requires different gating signals because degeneracy operates at the entity-set level.\n\n\\paragraph{Consistency for structured IE.}\n\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation alone does not ensure selection gains, diagnosing degeneracy and compression as blocking mechanisms.\nCoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\\S\\ref{sec:robustness_main}).\nEarlier work on confidence for structured prediction \\cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.\nEnsemble approaches aggregate predictions from multiple models or prompts \\cite{florian2003named, xiao2025el4ner}; \\citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.\nLLM-Blender \\cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.\nOur entity-level construction aggregates across samples from a single fine-tuned model, without requiring model diversity or prompt engineering.\nOur evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \\cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.\n\\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats; \\S\\ref{sec:discussion}) corroborates this for NER.\n\n\\paragraph{Uncertainty estimation and MBR decoding.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic}; semantic uncertainty \\cite{kuhn2023semantic, farquhar2024detecting} and P(True) \\cite{kadavath2022language} provide model-internal alternatives.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\n\\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck.\nOur QE results connect to selective prediction \\cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.\n\n\\paragraph{Best-of-$N$ with learned verifiers.}\n\\citet{gao2023scaling} establish BoN scaling laws and \\citet{chen2021evaluating} define the pass@$k$ metric for code generation; our unsupervised signals face a more fundamental limitation than reward overoptimization.\nTrained verifiers \\cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} and self-evaluation guided search \\cite{xie2023selfevaluation} learn per-sample scoring.\nCISC \\cite{taubenfeld2025cisc} and Self-Certainty \\cite{kang2025selfcertainty} derive per-sample confidence from hidden states rather than output statistics, but require architecture-specific access to intermediate representations; these hidden-state signals remain untested for structured prediction (\\S Limitations).\nFine-tuning \\cite{kirk2024understanding} and constrained decoding \\cite{holtzman2020curious, vijayakumar2018diverse} both limit the diversity recoverable for selection.\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01CrRVbgZeZ4u9nnAHL8u3sH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "07658118-2d91-4ddc-b275-8428753b5a4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6UTjGitcN2Q5CuhngogVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 21 · 2026-05-19T14:19:24.332Z_

<details><summary>↩ Tool result · `toolu_01CrRVbgZeZ4u9nnAHL8u3sH`</summary>

```text
1	paper:
2	  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence
3	    Signals for Test-Time Scaling in Information Extraction'
4	  version: 169
5	  generated_at: '2026-05-18T15:39:48.035618+00:00'
6	  source: manual provenance build by Paper Agent
7	claims:
8	- id: c001_voting_rho_scierc_ner
9	  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation
10	    artifact)
11	  sections:
12	  - abstract
13	  - introduction
14	  - experiments
15	  - conclusion
16	  - discussion
17	  - related_work
18	  tier: 1
19	  evidence:
20	  - exp_id: exp_012_rerun_1024
21	    metric: ner.voting_rho_full
22	    value: 0.379
23	  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected
24	    via exp_012_rerun_1024 (max_tokens=1024).
25	- id: c002_auroc_dissociation_scierc
26	  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while
27	    Voting leads ρ (NER 0.379, RE 0.422)
28	  sections:
29	  - abstract
30	  - introduction
31	  - experiments
32	  - conclusion
33	  - discussion
34	  tier: 1
35	  evidence:
36	  - exp_id: exp_012_rerun_1024
37	    metric: ner.em_auroc
38	    value: 0.749
39	  - exp_id: exp_012_rerun_1024
40	    metric: re.em_auroc
41	    value: 0.706
42	  - exp_id: exp_012_rerun_1024
43	    metric: ner.voting_auroc
44	    value: 0.684
45	  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected
46	    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline
47	    claim changed from "entity voting achieves ρ=0.38 and AUROC=0.74" to split ρ (Voting
48	    0.38) / AUROC (EM 0.75) claim.
49	- id: c003_sj_rho_scierc_ner
50	  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)
51	  sections:
52	  - experiments
53	  tier: 1
54	  evidence:
55	  - exp_id: exp_012_rerun_1024
56	    metric: ner.sj_rho_full
57	    value: 0.36
58	  - exp_id: exp_004_re_diagnostic
59	    metric: bootstrap_ci_95.ner_sj
60	    value:
61	    - 0.2946
62	    - 0.4586
63	- id: c004_voting_leads_re
64	  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)
65	  sections:
66	  - experiments
67	  tier: 1
68	  evidence:
69	  - exp_id: exp_012_rerun_1024
70	    metric: re.voting_rho_full
71	    value: 0.35
72	  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.
73	- id: c005_fk_beats_sj_re
74	  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER
75	  sections:
76	  - experiments
77	  tier: 1
78	  evidence:
79	  - exp_id: exp_012_rerun_1024
80	    metric: re.fk_rho_full
81	    value: 0.275
82	  - exp_id: exp_012_rerun_1024
83	    metric: re.sj_rho_full
84	    value: 0.25
85	  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.
86	- id: c006_re_40pct_zero_f1
87	  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)
88	  sections:
89	  - experiments
90	  - discussion
91	  tier: 1
92	  evidence:
93	  - exp_id: mvp_pilot_004
94	    metric: re_sample_f1_pct_zero
95	    value: 44.3
96	    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)
97	  - exp_id: exp_008_re_n16_v2
98	    metric: f1_zero_pct
99	    value: 44.3
100	    note: 44.3% at N=16; zero-F1 fraction varies with N and seed
101	- id: c007_em_leads_conll
102	  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816
103	  sections:
104	  - experiments
105	  tier: 1
106	  evidence:
107	  - exp_id: exp_002
108	    metric: em_rho_full
109	    value: 0.4507
110	  - exp_id: exp_002
111	    metric: em_auroc_full
112	    value: 0.8156
113	  - exp_id: exp_015_v2
114	    metric: auroc_best.EM.conll_ner
115	    value: 0.8156
116	- id: c008_cross_model_sj_stability
117	  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'
118	  sections:
119	  - experiments
120	  tier: 1
121	  evidence:
122	  - exp_id: exp_002
123	    metric: sj_rho_full
124	    value: 0.4357
125	  - exp_id: exp_017_llama_conll_infer
126	    metric: full.SJ_rho
127	    value: 0.4314
128	- id: c009_logprob_paradox
129	  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA
130	  sections:
131	  - experiments
132	  - discussion
133	  tier: 1
134	  evidence:
135	  - exp_id: exp_017_llama_conll_infer
136	    metric: full.logprob_AUROC
137	    value: 0.761
138	  - exp_id: exp_017_llama_conll_infer
139	    metric: full.logprob_rho
140	    value: 0.3072
141	- id: c010_conll_oracle_headroom
142	  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'
143	  sections:
144	  - experiments
145	  tier: 1
146	  evidence:
147	  - exp_id: exp_002
148	    metric: oracle_headroom
149	    value: 0.042
150	  - exp_id: exp_017_llama_conll_infer
151	    metric: oracle_headroom
152	    value: 0.0177
153	- id: c011_ner_no_reliable_selection
154	  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed
155	    bootstrap)
156	  sections:
157	  - abstract
158	  - introduction
159	  - experiments
160	  - conclusion
161	  - discussion
162	  - related_work
163	  tier: 1
164	  evidence:
165	  - exp_id: exp_016_rerun_1024_bootstrap
166	    metric: selection_f1_ner
167	    value:
168	      greedy: 0.644
169	      logprob: 0.65
170	      sj: 0.645
171	      voting: 0.634
172	      random: 0.608
173	      oracle: 0.776
174	  - exp_id: exp_016_rerun_1024_bootstrap
175	    metric: bootstrap_selection_test
176	    value:
177	      logprob_vs_greedy_p: 0.39
178	      ci_95:
179	      - -0.03
180	      - 0.042
181	      cohens_d: 0.038
182	      sign_test: 61W/70L
183	  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified
184	    with c012 — no signal reliably helps on either task.
185	- id: c012_re_no_signal_beats_greedy
186	  text: No signal surpasses greedy on RE; logprob drops to −0.9pp
187	  sections:
188	  - abstract
189	  - introduction
190	  - experiments
191	  - conclusion
192	  - discussion
193	  tier: 1
194	  evidence:
195	  - exp_id: exp_016_rerun_1024_bootstrap
196	    metric: selection_f1_re
197	    value:
198	      greedy: 0.404
199	      logprob: 0.395
200	      sj: 0.386
201	      voting: 0.359
202	      random: 0.354
203	      oracle: 0.585
204	  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was "only logprob
205	    helps on RE (+2.3pp)". Corrected via exp_016_rerun_1024_bootstrap.
206	- id: c013_oracle_headroom_ner
207	  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER
208	  sections:
209	  - experiments
210	  - discussion
211	  tier: 1
212	  evidence:
213	  - exp_id: exp_016_rerun_1024_bootstrap
214	    metric: selection_f1_ner.oracle
215	    value: 0.776
216	  - exp_id: exp_016_rerun_1024_bootstrap
217	    metric: selection_f1_ner.greedy
218	    value: 0.644
219	- id: c014_re_oracle_headroom
220	  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'
221	  sections:
222	  - experiments
223	  - discussion
224	  tier: 1
225	  evidence:
226	  - exp_id: exp_016_rerun_1024_bootstrap
227	    metric: selection_f1_re.oracle
228	    value: 0.585
229	  - exp_id: exp_016_rerun_1024_bootstrap
230	    metric: selection_f1_re.greedy
231	    value: 0.404
232	- id: c015_ensemble_auroc
233	  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)
234	  sections:
235	  - discussion
236	  tier: 1
237	  evidence:
238	  - exp_id: exp_016_rerun_1024_bootstrap
239	    metric: ensemble_ner_auroc
240	    value: 0.666
241	  note: Ensemble does NOT improve over best individual. Changed from positive to negative
242	    finding.
243	- id: c016_ece_calibration
244	  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater
245	    miscalibration (ECE 0.109-0.339)
246	  sections:
247	  - experiments
248	  tier: 1
249	  evidence:
250	  - exp_id: exp_016_rerun_1024_bootstrap
251	    metric: calibration_ece
252	    value:
253	      ner_range: 0.069-0.096
254	      re_range: 0.109-0.339
255	  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration
256	    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has
257	    moderate miscalibration. Consistent with fig_reliability_1024.
258	- id: c017_fisher_z_ner_vs_re
259	  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'
260	  sections:
261	  - experiments
262	  tier: 1
263	  evidence:
264	  - exp_id: exp_004_re_diagnostic
265	    metric: fisher_z_ner_vs_re.sj_z
266	    value: 2.31
267	  - exp_id: exp_004_re_diagnostic
268	    metric: fisher_z_ner_vs_re.sj_p
269	    value: 0.0209
270	- id: c018_per_relation_diagnostic
271	  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646
272	  sections:
273	  - experiments
274	  tier: 1
275	  evidence:
276	  - exp_id: exp_004_re_diagnostic
277	    metric: per_relation_type.FEATURE-OF.rho_sj
278	    value: 0.004
279	  - exp_id: exp_004_re_diagnostic
280	    metric: per_relation_type.HYPONYM-OF.rho_fk
281	    value: 0.646
282	- id: c019_entity_span_errors
283	  text: Entity span errors account for 55.5% of RE false negatives
284	  sections:
285	  - experiments
286	  tier: 1
287	  evidence:
288	  - exp_id: exp_004_re_diagnostic
289	    metric: error_propagation
290	    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error
291	      21.7% → entity span errors ~55.5%
292	  note: Computed from error_propagation breakdown in exp_004
293	- id: c020_capability_stratification_ner
294	  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities
295	  sections:
296	  - experiments
297	  tier: 1
298	  evidence:
299	  - exp_id: exp_009_capability_stratification
300	    metric: scierc_ner.by_ent_count.6plus_sj_rho
301	    value: 0.547
302	  - exp_id: exp_009_capability_stratification
303	    metric: scierc_ner.by_ent_count.1_2_sj_rho
304	    value: 0.415
305	- id: c021_wnut_boundary
306	  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'
307	  sections:
308	  - experiments
309	  - conclusion
310	  tier: 1
311	  evidence:
312	  - exp_id: exp_003_wnut17_eval
313	    metric: rho_sj
314	    value: 0.089
315	  - exp_id: exp_003_wnut17_eval
316	    metric: sample_f1_pct_zero
317	    value: 53.7
318	  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered
319	    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'
320	- id: c022_wnut_logprob_negative
321	  text: WNUT logprob shows strong negative correlation
322	  sections:
323	  - experiments
324	  tier: 1
325	  evidence:
326	  - exp_id: exp_003_ner_wnut17
327	    metric: ner.rho_logprob_full
328	    value: -0.414
329	  - exp_id: exp_003_wnut17_eval
330	    metric: rho_logprob_full
331	    value: -0.409
332	- id: c023_re_sent_length_sj
333	  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'
334	  sections:
335	  - experiments
336	  tier: 2
337	  evidence:
338	  - exp_id: exp_009_v2_re_rerun
339	    metric: by_sent_len_quartiles
340	    value:
341	      Q1_sj_rho: 0.11
342	      Q4_sj_rho: 0.473
343	      fisher_z_p: 0.004
344	  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).
345	    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'
346	- id: c024_high_complexity_re_subset
347	  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'
348	  sections:
349	  - experiments
350	  tier: 2
351	  evidence:
352	  - exp_id: exp_009_capability_stratification
353	    metric: scierc_re.by_rel_count
354	    value:
355	      6plus_sj_rho: 0.527
356	  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and
357	    logprob values not in registry summary.
358	- id: c025_temperature_sj_stable
359	  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028
360	  sections:
361	  - experiments
362	  tier: 1
363	  evidence:
364	  - exp_id: exp_005
365	    metric: sj_rho_t07_ner
366	    value: 0.388
367	  - exp_id: exp_012_rerun_1024
368	    metric: ner.sj_rho_full
369	    value: 0.36
370	  note: T=0.7 data from exp_005; T=1.0 from exp_015
371	- id: c026_n_scaling_sj
372	  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen
373	    SciERC NER
374	  sections:
375	  - experiments
376	  tier: 1
377	  evidence:
378	  - exp_id: exp_012_rerun_1024
379	    metric: ner.sj_rho_full
380	    value: 0.36
381	  - exp_id: exp_001_seed42_v2
382	    metric: sj_rho_full
383	    value: 0.428
384	  - exp_id: exp_001_seed123_v2
385	    metric: sj_rho_full
386	    value: 0.424
387	  - exp_id: exp_001_seed456_v2_ner
388	    metric: full.SJ.rho
389	    value: 0.384
390	  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'
391	- id: c027_llama_conll_3seed
392	  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'
393	  sections:
394	  - experiments
395	  tier: 1
396	  evidence:
397	  - exp_id: exp_017_llama_conll_n16
398	    metric: full.SJ_rho
399	    value: 0.4642
400	  - exp_id: exp_017_llama_conll_n16_s123
401	    metric: full.SJ_rho
402	    value: 0.4698
403	  - exp_id: exp_017_llama_conll_n16_s456
404	    metric: full.SJ_rho
405	    value: 0.4552
406	  - exp_id: exp_017_llama_conll_n16
407	    metric: full.logprob_rho
408	    value: 0.3058
409	  - exp_id: exp_017_llama_conll_n16_s123
410	    metric: full.logprob_rho
411	    value: 0.3161
412	  - exp_id: exp_017_llama_conll_n16_s456
413	    metric: full.logprob_rho
414	    value: 0.3078
415	- id: c028_loo_sj_circularity
416	  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible
417	  sections:
418	  - experiments
419	  tier: 1
420	  evidence:
421	  - exp_id: exp_015_v2
422	    metric: loo_sj.max_delta_rho
423	    value: 0.000305
424	  - exp_id: exp_015_v2
425	    metric: loo_sj.all_no_circularity
426	    value: true
427	- id: c029_llama_scierc_cross_model
428	  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;
429	    conditional RE SJ ρ=0.405 > FK ρ=0.259'
430	  sections:
431	  - experiments
432	  tier: 1
433	  evidence:
434	  - exp_id: exp_007_llama_inference
435	    metric: ner.rho_sj
436	    value: 0.363
437	  - exp_id: exp_007_llama_inference
438	    metric: ner.rho_fk
439	    value: 0.327
440	  - exp_id: exp_007_llama_inference
441	    metric: re.sj_rho_cond
442	    value: 0.405
443	  - exp_id: exp_007_llama_inference
444	    metric: re.fk_rho_cond
445	    value: 0.259
446	- id: c030_em_conditional_dominance
447	  text: 'EM ranks #1 on conditional set across all 4 configurations'
448	  sections:
449	  - experiments
450	  tier: 1
451	  evidence:
452	  - exp_id: exp_015_metrics_expansion
453	    metric: ner.em_rho_cond
454	    value: 0.3427
455	  - exp_id: exp_015_metrics_expansion
456	    metric: re.em_rho_cond
457	    value: 0.3607
458	  - exp_id: exp_002_conll_n16
459	    metric: conditional.EM_rho
460	    value: 0.4658
461	  - exp_id: exp_017_llama_conll_n16_s123
462	    metric: conditional.EM_rho
463	    value: 0.4732
464	  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,
465	    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different
466	    seed/N combinations.'
467	- id: c031_em_conditional_scierc
468	  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'
469	  sections:
470	  - experiments
471	  tier: 1
472	  evidence:
473	  - exp_id: exp_001_ner_n16_scierc
474	    metric: ner_cond_em_rho
475	    value: 0.414
476	  - exp_id: exp_001_ner_n16_scierc
477	    metric: re_cond_em_rho
478	    value: 0.475
479	  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'
480	- id: c032_logprob_re_cond_collapse
481	  text: Logprob conditional RE collapses to ρ=0.011
482	  sections:
483	  - experiments
484	  tier: 1
485	  evidence:
486	  - exp_id: exp_012_rerun_1024
487	    metric: re_cond.logprob.rho
488	    value: 0.0112
489	  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).
490	    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text
491	    0.002 was stale and untraceable.'
492	- id: c033_sj_n16_cond_re
493	  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026
494	  sections:
495	  - experiments
496	  - discussion
497	  tier: 1
498	  evidence:
499	  - exp_id: exp_008_re_n16_v2
500	    metric: sj_rho_cond
501	    value: 0.308
502	- id: c034_structural_over_logprob_n16
503	  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124
504	    to +0.175)
505	  sections:
506	  - experiments
507	  - discussion
508	  tier: 1
509	  evidence:
510	  - exp_id: exp_001_ner_n16_scierc
511	    metric: ner_voting_conf_rho
512	    value: 0.399
513	  - exp_id: exp_001_ner_n16_scierc
514	    metric: ner_logprob_rho
515	    value: 0.237
516	  - exp_id: exp_002_conll_n16
517	    metric: full.EM_rho
518	    value: 0.4627
519	  - exp_id: exp_002_conll_n16
520	    metric: full.logprob_rho
521	    value: 0.3146
522	  - exp_id: exp_007_llama_n16
523	    metric: full.voting_conf_rho
524	    value: 0.4515
525	  - exp_id: exp_007_llama_n16
526	    metric: full.logprob_rho
527	    value: 0.2041
528	  - exp_id: exp_017_llama_conll_n16
529	    metric: full.SJ_rho
530	    value: 0.4642
531	  - exp_id: exp_017_llama_conll_n16
532	    metric: full.logprob_rho
533	    value: 0.3058
534	- id: c035_n_scaling_diminishing
535	  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'
536	  sections:
537	  - discussion
538	  tier: 1
539	  evidence:
540	  - exp_id: exp_001_seed42_v2
541	    metric: sj_rho_full
542	    value: 0.428
543	  - exp_id: exp_015_metrics_expansion
544	    metric: ner.sj_rho_full
545	    value: 0.3565
546	  - exp_id: exp_017_llama_conll_n16
547	    metric: full.SJ_rho
548	    value: 0.4642
549	  - exp_id: exp_017_llama_conll_infer
550	    metric: full.SJ_rho
551	    value: 0.4314
552	  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)
553	    - 0.431 = +0.032'
554	- id: c036_sj_ece_calibration
555	  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across
556	    settings)'
557	  sections: []
558	  tier: X
559	  evidence: []
560	  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)
561	    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all
562	    signals ECE 0.27-0.77.
563	- id: C001
564	  location:
565	    section: abstract
566	    paragraph: 0
567	    sentence: 0
568	  text: No signal significantly improves sample selection over greedy decoding despite
569	    13-18pp oracle headroom
570	  type: empirical
571	  evidence:
572	  - exp_012_rerun_1024
573	  decisions:
574	  - D070
575	  - D071
576	  deprecated: false
577	- id: C003
578	  location:
579	    section: abstract
580	    paragraph: 0
581	    sentence: 0
582	  text: LP scores compressed into effective ties for 60% of instances under constrained
583	    decoding
584	  type: empirical
585	  evidence:
586	  - exp_012_rerun_1024
587	  decisions: []
588	  deprecated: false
589	- id: C006
590	  location:
591	    section: abstract
592	    paragraph: 0
593	    sentence: 0
594	  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)
595	  type: empirical
596	  evidence:
597	  - exp_012_rerun_1024
598	  decisions: []
599	  deprecated: false
600	- id: C010
601	  location:
602	    section: abstract
603	    paragraph: 0
604	    sentence: 0
605	  text: Constrained-decoding score compression is the primary bottleneck
606	  type: empirical
607	  evidence:
608	  - exp_012_rerun_1024
609	  decisions: []
610	  deprecated: false
611	- id: C011
612	  location:
613	    section: discussion
614	    paragraph: 0
615	    sentence: 0
616	  text: LP carries useful per-sample quality information; score compression is the
617	    primary bottleneck
618	  type: empirical
619	  evidence:
620	  - exp_012_rerun_1024
621	  decisions:
622	  - D071
623	  deprecated: false
624	- id: C013
625	  location:
626	    section: discussion
627	    paragraph: 0
628	    sentence: 0
629	  text: MBR utility correlates with F1 across instances but not within
630	  type: empirical
631	  evidence:
632	  - exp_012_rerun_1024
633	  decisions: []
634	  deprecated: false
635	- id: C016
636	  location:
637	    section: discussion
638	    paragraph: 0
639	    sentence: 0
640	  text: Free-form ablation would test if bottleneck is decoding-regime-specific
641	  type: planned
642	  evidence: []
643	  decisions:
644	  - D071
645	  deprecated: false
646	- id: C017
647	  location:
648	    section: conclusion
649	    paragraph: 0
650	    sentence: 0
651	  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail
652	    at selection
653	  type: empirical
654	  evidence:
655	  - exp_012_rerun_1024
656	  decisions: []
657	  deprecated: false
658	- id: C019
659	  location:
660	    section: conclusion
661	    paragraph: 0
662	    sentence: 0
663	  text: LP fails due to constrained-decoding score compression
664	  type: empirical
665	  evidence:
666	  - exp_012_rerun_1024
667	  decisions: []
668	  deprecated: false
669	- id: C022
670	  location:
671	    section: conclusion
672	    paragraph: 0
673	    sentence: 0
674	  text: RE findings preliminary, single benchmark
675	  type: scope_limitation
676	  evidence:
677	  - exp_012_rerun_1024
678	  decisions: []
679	  deprecated: false
680	- id: C023
681	  location:
682	    section: sections/discussion
683	    paragraph: 0
684	    sentence: 0
685	  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence
686	    LP on SciERC, but selection performs worse (-2.0pp)
687	  type: quantitative
688	  evidence:
689	  - exp_id: exp_entity_token_lp
690	    metric: scierc_entity_lp_variance_ratio
691	    value: 4.0x
692	  - exp_id: exp_entity_token_lp
693	    metric: scierc_entity_lp_selection_delta
694	    value: -1.68
695	  decisions: []
696	  deprecated: false
697	- id: C024
698	  location:
699	    section: sections/discussion
700	    paragraph: 0
701	    sentence: 0
702	  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with
703	    79% tied
704	  type: quantitative
705	  evidence:
706	  - exp_id: exp_entity_token_lp
707	    metric: conll_entity_lp_variance_median
708	    value: 2e-10
709	  - exp_id: exp_entity_token_lp
710	    metric: conll_entity_lp_tied_fraction
711	    value: 0.794
712	  decisions: []
713	  deprecated: false
714	- id: C025
715	  location:
716	    section: sections/discussion
717	    paragraph: 0
718	    sentence: 0
719	  text: Entity-token LP rules out format-token dilution as primary cause; points to
720	    intrinsic model overconfidence on entity tokens
721	  type: interpretive
722	  evidence:
723	  - exp_id: exp_entity_token_lp
724	  decisions: []
725	  deprecated: false
726	- id: C026
727	  location:
728	    section: sections/limitations
729	    paragraph: 0
730	    sentence: 0
731	  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches
732	    are unexplored
733	  type: scope
734	  evidence:
735	  - exp_id: exp_entity_token_lp
736	  decisions: []
737	  deprecated: false
738	- id: C027
739	  location:
740	    section: sections/introduction
741	    paragraph: 0
742	    sentence: 0
743	  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance
744	    failure are the findings'
745	  type: structural
746	  evidence: []
747	  decisions: []
748	  deprecated: false
749	- id: C028
750	  location:
751	    section: sections/introduction
752	    paragraph: 0
753	    sentence: 0
754	  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous
755	    characterization'
756	  type: structural
757	  evidence: []
758	  decisions: []
759	  deprecated: false
760	- id: C029
761	  location:
762	    section: sections/introduction
763	    paragraph: 0
764	    sentence: 0
765	  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'
766	  type: structural
767	  evidence:
768	  - exp_id: exp_entity_token_lp
769	  decisions: []
770	  deprecated: false
771	- id: C030
772	  location:
773	    section: sections/abstract
774	    paragraph: 0
775	    sentence: 0
776	  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up
777	    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined
778	    from 9 to 6 sentences'
779	  type: structural
780	  evidence: []
781	  decisions: []
782	  deprecated: false
783	- id: C031
784	  location:
785	    section: sections/discussion
786	    paragraph: 0
787	    sentence: 0
788	  text: 21% of SciERC instances produce identical F1 across all N samples
789	  type: quantitative
790	  evidence: Q1 within-instance analysis
791	  decisions: []
792	  deprecated: false
793	- id: C032
794	  location:
795	    section: sections/discussion
796	    paragraph: 0
797	    sentence: 0
798	  text: 58% of CoNLL instances produce identical F1 across all N samples
799	  type: quantitative
800	  evidence: Q1 within-instance analysis
801	  decisions: []
802	  deprecated: false
803	- id: C033
804	  location:
805	    section: sections/discussion
806	    paragraph: 0
807	    sentence: 0
808	  text: 13% of SciERC instances yield constant utility scores
809	  type: quantitative
810	  evidence: Q1 within-instance analysis
811	  decisions: []
812	  deprecated: false
813	- id: C034
814	  location:
815	    section: sections/discussion
816	    paragraph: 0
817	    sentence: 0
818	  text: 49% of CoNLL instances yield constant utility scores
819	  type: quantitative
820	  evidence: Q1 within-instance analysis
821	  decisions: []
822	  deprecated: false
823	- id: C035
824	  location:
825	    section: sections/discussion
826	    paragraph: 0
827	    sentence: 0
828	  text: SJ median within-instance rho = 0.524 on SciERC
829	  type: quantitative
830	  evidence: Q1 within-instance analysis
831	  decisions: []
832	  deprecated: false
833	- id: C036
834	  location:
835	    section: sections/discussion
836	    paragraph: 0
837	    sentence: 0
838	  text: SJ median within-instance rho = 0.994 on CoNLL
839	  type: quantitative
840	  evidence: Q1 within-instance analysis
841	  decisions: []
842	  deprecated: false
843	- id: C037
844	  location:
845	    section: sections/discussion
846	    paragraph: 0
847	    sentence: 0
848	  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances
849	  type: quantitative
850	  evidence: Q1 within-instance analysis
851	  decisions: []
852	  deprecated: false
853	- id: C038
854	  location:
855	    section: sections/discussion
856	    paragraph: 0
857	    sentence: 0
858	  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances
859	  type: quantitative
860	  evidence: Q1 within-instance analysis
861	  decisions: []
862	  deprecated: false
863	- id: C039
864	  location:
865	    section: sections/discussion
866	    paragraph: 0
867	    sentence: 0
868	  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies
869	  type: quantitative
870	  evidence: SF4 greedy data
871	  decisions: []
872	  deprecated: false
873	- id: C040
874	  location:
875	    section: sections/discussion
876	    paragraph: 0
877	    sentence: 0
878	  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp
879	  type: quantitative
880	  evidence: tab:epoch_scierc
881	  decisions: []
882	  deprecated: false
883	- id: C041
884	  location:
885	    section: sections/discussion
886	    paragraph: 0
887	    sentence: 0
888	  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)
889	  type: quantitative
890	  evidence: []
891	  decisions: []
892	  deprecated: false
893	- id: C042
894	  location:
895	    section: sections/discussion
896	    paragraph: 0
897	    sentence: 0
898	  text: Entity-level majority voting yields -0.64pp on CoNLL
899	  type: quantitative
900	  evidence: []
901	  decisions: []
902	  deprecated: false
903	- id: C043
904	  location:
905	    section: sections/discussion
906	    paragraph: 0
907	    sentence: 0
908	  text: Entity-level majority voting yields -3.21pp on Few-NERD
909	  type: quantitative
910	  evidence: []
911	  decisions: []
912	  deprecated: false
913	- id: C044
914	  location:
915	    section: sections/discussion
916	    paragraph: 0
917	    sentence: 0
918	  text: On degenerate subsets, merge is uniformly negative across all three datasets
919	  type: quantitative
920	  evidence: []
921	  decisions: []
922	  deprecated: false
923	- id: C045
924	  location:
925	    section: sections/appendix
926	    paragraph: 0
927	    sentence: 0
928	  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation
929	  type: quantitative
930	  evidence: []
931	  decisions: []
932	  deprecated: false
933	- id: C046
934	  location:
935	    section: sections/appendix
936	    paragraph: 0
937	    sentence: 0
938	  text: Under conservative df=4 adjustment, p=0.033
939	  type: quantitative
940	  evidence: []
941	  decisions: []
942	  deprecated: false
943	- id: C047
944	  location:
945	    section: sections/appendix
946	    paragraph: 0
947	    sentence: 0
948	  text: 3-epoch SciERC mean within-instance rho=0.273
949	  type: quantitative
950	  evidence: []
951	  decisions: []
952	  deprecated: false
953	- id: C048
954	  location:
955	    section: sections/appendix
956	    paragraph: 0
957	    sentence: 0
958	  text: 5-epoch SciERC mean within-instance rho=0.179
959	  type: quantitative
960	  evidence: []
961	  decisions: []
962	  deprecated: false
963	- id: C049
964	  location:
965	    section: sections/appendix
966	    paragraph: 0
967	    sentence: 0
968	  text: 76.4% of instances show positive LP-quality correlation at 3 epochs
969	  type: quantitative
970	  evidence: []
971	  decisions: []
972	  deprecated: false
973	- id: C050
974	  location:
975	    section: sections/appendix
976	    paragraph: 0
977	    sentence: 0
978	  text: 64.1% of instances show positive LP-quality correlation at 5 epochs
979	  type: quantitative
980	  evidence: []
981	  decisions: []
982	  deprecated: false
983	- id: C051
984	  location:
985	    section: sections/appendix
986	    paragraph: 0
987	    sentence: 0
988	  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset
989	    gap
990	  type: quantitative
991	  evidence: []
992	  decisions: []
993	  deprecated: false
994	- id: C052
995	  location:
996	    section: sections/appendix
997	    paragraph: 0
998	    sentence: 0
999	  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL
1000	    0.10'
1001	  type: quantitative
1002	  evidence: []
1003	  decisions: []
1004	  deprecated: false
1005	- id: C053
1006	  location:
1007	    section: sections/appendix
1008	    paragraph: 0
1009	    sentence: 0
1010	  text: LOO regret ranges from 0.51 to 1.21pp
1011	  type: quantitative
1012	  evidence: []
1013	  decisions: []
1014	  deprecated: false
1015	- id: C054
1016	  location:
1017	    section: sections/appendix
1018	    paragraph: 0
1019	    sentence: 0
1020	  text: Even with oracle tau, CoNLL remains at -0.31pp
1021	  type: quantitative
1022	  evidence: []
1023	  decisions: []
1024	  deprecated: false
1025	- id: C055
1026	  location:
1027	    section: sections/appendix
1028	    paragraph: 0
1029	    sentence: 0
1030	  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'
1031	  type: quantitative
1032	  evidence: []
1033	  decisions: []
1034	  deprecated: false
1035	- id: C056
1036	  location:
1037	    section: sections/appendix
1038	    paragraph: 0
1039	    sentence: 0
1040	  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'
1041	  type: quantitative
1042	  evidence: []
1043	  decisions: []
1044	  deprecated: false
1045	- id: C057
1046	  location:
1047	    section: sections/appendix
1048	    paragraph: 0
1049	    sentence: 0
1050	  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'
1051	  type: quantitative
1052	  evidence: []
1053	  decisions: []
1054	  deprecated: false
1055	- id: C058
1056	  location:
1057	    section: sections/experiments
1058	    paragraph: 0
1059	    sentence: 0
1060	  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'
1061	  type: quantitative
1062	  evidence: []
1063	  decisions: []
1064	  deprecated: false
1065	- id: C059
1066	  location:
1067	    section: sections/experiments
1068	    paragraph: 0
1069	    sentence: 0
1070	  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'
1071	  type: quantitative
1072	  evidence: []
1073	  decisions: []
1074	  deprecated: false
1075	- id: C060
1076	  location:
1077	    section: sections/experiments
1078	    paragraph: 0
1079	    sentence: 0
1080	  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'
1081	  type: quantitative
1082	  evidence: []
1083	  decisions: []
1084	  deprecated: false
1085	- id: C061
1086	  location:
1087	    section: sections/appendix
1088	    paragraph: 0
1089	    sentence: 0
1090	  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)
1091	  type: quantitative
1092	  evidence: []
1093	  decisions: []
1094	  deprecated: false
1095	- id: C062
1096	  location:
1097	    section: sections/appendix
1098	    paragraph: 0
1099	    sentence: 0
1100	  text: Entity-token LP rho=0.440 vs full-sequence 0.297
1101	  type: quantitative
1102	  evidence: []
1103	  decisions: []
1104	  deprecated: false
1105	- id: C063
1106	  location:
1107	    section: sections/appendix
1108	    paragraph: 0
1109	    sentence: 0
1110	  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp
1111	  type: quantitative
1112	  evidence: []
1113	  decisions: []
1114	  deprecated: false
1115	tables:
1116	- id: tab:notation
1117	  section: method
1118	  caption: Notation used throughout the paper
1119	  evidence: []
1120	  note: Notation table—no experimental data.
1121	- id: tab:quality_estimation
1122	  section: experiments
1123	  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)
1124	  evidence:
1125	  - exp_id: exp_012_rerun_1024
1126	    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)
1127	  - exp_id: exp_015_metrics_expansion
1128	    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix
1129	  - exp_id: exp_015_v2
1130	    role: AUROC values across settings
1131	  - exp_id: exp_002
1132	    role: CoNLL Qwen N=8 ρ and AUROC
1133	  - exp_id: exp_017_llama_conll_infer
1134	    role: CoNLL LLaMA N=8 ρ and AUROC
1135	  - exp_id: exp_017_llama_conll_n16
1136	    role: LLaMA CoNLL N=16 3-seed (seed=42)
1137	  - exp_id: exp_017_llama_conll_n16_s123
1138	    role: LLaMA CoNLL N=16 3-seed (seed=123)
1139	  - exp_id: exp_017_llama_conll_n16_s456
1140	    role: LLaMA CoNLL N=16 3-seed (seed=456)
1141	- id: tab:selection
1142	  section: experiments
1143	  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)
1144	  evidence:
1145	  - exp_id: exp_016_signal_ensemble
1146	    role: All selection F1 values (NER and RE)
1147	- id: tab:robustness
1148	  section: experiments
1149	  caption: Signal robustness across configurations (Spearman ρ)
1150	  evidence:
1151	  - exp_id: exp_005
1152	    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)
1153	  - exp_id: exp_015_metrics_expansion
1154	    role: N=8 baseline values
1155	  - exp_id: exp_001_seed42_v2
1156	    role: N=16 SJ ρ seed=42
1157	  - exp_id: exp_001_seed123_v2
1158	    role: N=16 SJ ρ seed=123
1159	  - exp_id: exp_001_seed456_v2_ner
1160	    role: N=16 SJ ρ seed=456
1161	  - exp_id: exp_017_llama_conll_n16
1162	    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'
1163	  - exp_id: exp_017_llama_conll_n16_s123
1164	    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'
1165	  - exp_id: exp_017_llama_conll_n16_s456
1166	    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'
1167	figures:
1168	- id: fig:overview
1169	  section: introduction
1170	  caption: The correlation-selection gap conceptual diagram
1171	  evidence:
1172	  - exp_id: exp_015_metrics_expansion
1173	    role: Quality estimation data (ρ, AUROC for left panel)
1174	  - exp_id: exp_016_signal_ensemble
1175	    role: Selection F1 data (right panel)
1176	- id: fig:signal_heatmap
1177	  section: experiments
1178	  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations
1179	  evidence:
1180	  - exp_id: exp_015_metrics_expansion
1181	    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)
1182	  - exp_id: exp_002
1183	    role: CoNLL Qwen full set ρ values
1184	  - exp_id: exp_001_ner_n16_scierc
1185	    role: Conditional set ρ values
1186	- id: fig:selection_gap
1187	  section: experiments
1188	  caption: The correlation-selection gap on SciERC (N=8)
1189	  evidence:
1190	  - exp_id: exp_016_signal_ensemble
1191	    role: Best-of-N selection F1 bars and quality estimation ρ line
1192	- id: fig:temperature_robustness
1193	  section: experiments
1194	  caption: Temperature robustness on SciERC (N=8)
1195	  evidence:
1196	  - exp_id: exp_005
1197	    role: SJ, FK ρ values at T=0.7 and T=1.0
1198	- id: fig:reliability
1199	  section: experiments
1200	  caption: Reliability diagrams on SciERC (N=8, T=1.0)
1201	  evidence:
1202	  - exp_id: exp_015_metrics_expansion
1203	    role: Calibration/ECE data for all signals
1204	  - exp_id: exp_002
1205	    role: ECE values across signals
1206	_completeness:
1207	  coverage: 59/92
1208	  claims: 87
1209	  tables: 4
1210	  figures: 5
1211	  tier_counts:
1212	    tier1: 0
1213	    tier2: 59
1214	    tier3: 33
1215	    tierX: 0
1216	  last_checked: '2026-05-18T15:39:48.035668+00:00'
1217	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "97fbff20-cdb0-4501-aff3-5c560d45b69e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml",
      "content": "paper:\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\n    Signals for Test-Time Scaling in Information Extraction'\n  version: 169\n  generated_at: '2026-05-18T15:39:48.035618+00:00'\n  source: manual provenance build by Paper Agent\nclaims:\n- id: c001_voting_rho_scierc_ner\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\n    artifact)\n  sections:\n  - abstract\n  - introduction\n  - experiments\n  - conclusion\n  - discussion\n  - related_work\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: ner.voting_rho_full\n    value: 0.379\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\n    via exp_012_rerun_1024 (max_tokens=1024).\n- id: c002_auroc_dissociation_scierc\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\n    Voting leads ρ (NER 0.379, RE 0.422)\n  sections:\n  - abstract\n  - introduction\n  - experiments\n  - conclusion\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: ner.em_auroc\n    value: 0.749\n  - exp_id: exp_012_rerun_1024\n    metric: re.em_auroc\n    value: 0.706\n  - exp_id: exp_012_rerun_1024\n    metric: ner.voting_auroc\n    value: 0.684\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\n    claim changed from \"entity voting achieves ρ=0.38 and AUROC=0.74\" to split ρ (Voting\n    0.38) / AUROC (EM 0.75) claim.\n- id: c003_sj_rho_scierc_ner\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: ner.sj_rho_full\n    value: 0.36\n  - exp_id: exp_004_re_diagnostic\n    metric: bootstrap_ci_95.ner_sj\n    value:\n    - 0.2946\n    - 0.4586\n- id: c004_voting_leads_re\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: re.voting_rho_full\n    value: 0.35\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\n- id: c005_fk_beats_sj_re\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: re.fk_rho_full\n    value: 0.275\n  - exp_id: exp_012_rerun_1024\n    metric: re.sj_rho_full\n    value: 0.25\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\n- id: c006_re_40pct_zero_f1\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: mvp_pilot_004\n    metric: re_sample_f1_pct_zero\n    value: 44.3\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\n  - exp_id: exp_008_re_n16_v2\n    metric: f1_zero_pct\n    value: 44.3\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\n- id: c007_em_leads_conll\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_002\n    metric: em_rho_full\n    value: 0.4507\n  - exp_id: exp_002\n    metric: em_auroc_full\n    value: 0.8156\n  - exp_id: exp_015_v2\n    metric: auroc_best.EM.conll_ner\n    value: 0.8156\n- id: c008_cross_model_sj_stability\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_002\n    metric: sj_rho_full\n    value: 0.4357\n  - exp_id: exp_017_llama_conll_infer\n    metric: full.SJ_rho\n    value: 0.4314\n- id: c009_logprob_paradox\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_017_llama_conll_infer\n    metric: full.logprob_AUROC\n    value: 0.761\n  - exp_id: exp_017_llama_conll_infer\n    metric: full.logprob_rho\n    value: 0.3072\n- id: c010_conll_oracle_headroom\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_002\n    metric: oracle_headroom\n    value: 0.042\n  - exp_id: exp_017_llama_conll_infer\n    metric: oracle_headroom\n    value: 0.0177\n- id: c011_ner_no_reliable_selection\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\n    bootstrap)\n  sections:\n  - abstract\n  - introduction\n  - experiments\n  - conclusion\n  - discussion\n  - related_work\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_ner\n    value:\n      greedy: 0.644\n      logprob: 0.65\n      sj: 0.645\n      voting: 0.634\n      random: 0.608\n      oracle: 0.776\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: bootstrap_selection_test\n    value:\n      logprob_vs_greedy_p: 0.39\n      ci_95:\n      - -0.03\n      - 0.042\n      cohens_d: 0.038\n      sign_test: 61W/70L\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\n    with c012 — no signal reliably helps on either task.\n- id: c012_re_no_signal_beats_greedy\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\n  sections:\n  - abstract\n  - introduction\n  - experiments\n  - conclusion\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_re\n    value:\n      greedy: 0.404\n      logprob: 0.395\n      sj: 0.386\n      voting: 0.359\n      random: 0.354\n      oracle: 0.585\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \"only logprob\n    helps on RE (+2.3pp)\". Corrected via exp_016_rerun_1024_bootstrap.\n- id: c013_oracle_headroom_ner\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_ner.oracle\n    value: 0.776\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_ner.greedy\n    value: 0.644\n- id: c014_re_oracle_headroom\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_re.oracle\n    value: 0.585\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: selection_f1_re.greedy\n    value: 0.404\n- id: c015_ensemble_auroc\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\n  sections:\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: ensemble_ner_auroc\n    value: 0.666\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\n    finding.\n- id: c016_ece_calibration\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\n    miscalibration (ECE 0.109-0.339)\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_016_rerun_1024_bootstrap\n    metric: calibration_ece\n    value:\n      ner_range: 0.069-0.096\n      re_range: 0.109-0.339\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\n    moderate miscalibration. Consistent with fig_reliability_1024.\n- id: c017_fisher_z_ner_vs_re\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_004_re_diagnostic\n    metric: fisher_z_ner_vs_re.sj_z\n    value: 2.31\n  - exp_id: exp_004_re_diagnostic\n    metric: fisher_z_ner_vs_re.sj_p\n    value: 0.0209\n- id: c018_per_relation_diagnostic\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_004_re_diagnostic\n    metric: per_relation_type.FEATURE-OF.rho_sj\n    value: 0.004\n  - exp_id: exp_004_re_diagnostic\n    metric: per_relation_type.HYPONYM-OF.rho_fk\n    value: 0.646\n- id: c019_entity_span_errors\n  text: Entity span errors account for 55.5% of RE false negatives\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_004_re_diagnostic\n    metric: error_propagation\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\n      21.7% → entity span errors ~55.5%\n  note: Computed from error_propagation breakdown in exp_004\n- id: c020_capability_stratification_ner\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_009_capability_stratification\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\n    value: 0.547\n  - exp_id: exp_009_capability_stratification\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\n    value: 0.415\n- id: c021_wnut_boundary\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\n  sections:\n  - experiments\n  - conclusion\n  tier: 1\n  evidence:\n  - exp_id: exp_003_wnut17_eval\n    metric: rho_sj\n    value: 0.089\n  - exp_id: exp_003_wnut17_eval\n    metric: sample_f1_pct_zero\n    value: 53.7\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\n- id: c022_wnut_logprob_negative\n  text: WNUT logprob shows strong negative correlation\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_003_ner_wnut17\n    metric: ner.rho_logprob_full\n    value: -0.414\n  - exp_id: exp_003_wnut17_eval\n    metric: rho_logprob_full\n    value: -0.409\n- id: c023_re_sent_length_sj\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\n  sections:\n  - experiments\n  tier: 2\n  evidence:\n  - exp_id: exp_009_v2_re_rerun\n    metric: by_sent_len_quartiles\n    value:\n      Q1_sj_rho: 0.11\n      Q4_sj_rho: 0.473\n      fisher_z_p: 0.004\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\n- id: c024_high_complexity_re_subset\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\n  sections:\n  - experiments\n  tier: 2\n  evidence:\n  - exp_id: exp_009_capability_stratification\n    metric: scierc_re.by_rel_count\n    value:\n      6plus_sj_rho: 0.527\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\n    logprob values not in registry summary.\n- id: c025_temperature_sj_stable\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_005\n    metric: sj_rho_t07_ner\n    value: 0.388\n  - exp_id: exp_012_rerun_1024\n    metric: ner.sj_rho_full\n    value: 0.36\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\n- id: c026_n_scaling_sj\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\n    SciERC NER\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: ner.sj_rho_full\n    value: 0.36\n  - exp_id: exp_001_seed42_v2\n    metric: sj_rho_full\n    value: 0.428\n  - exp_id: exp_001_seed123_v2\n    metric: sj_rho_full\n    value: 0.424\n  - exp_id: exp_001_seed456_v2_ner\n    metric: full.SJ.rho\n    value: 0.384\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\n- id: c027_llama_conll_3seed\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.SJ_rho\n    value: 0.4642\n  - exp_id: exp_017_llama_conll_n16_s123\n    metric: full.SJ_rho\n    value: 0.4698\n  - exp_id: exp_017_llama_conll_n16_s456\n    metric: full.SJ_rho\n    value: 0.4552\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.logprob_rho\n    value: 0.3058\n  - exp_id: exp_017_llama_conll_n16_s123\n    metric: full.logprob_rho\n    value: 0.3161\n  - exp_id: exp_017_llama_conll_n16_s456\n    metric: full.logprob_rho\n    value: 0.3078\n- id: c028_loo_sj_circularity\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_015_v2\n    metric: loo_sj.max_delta_rho\n    value: 0.000305\n  - exp_id: exp_015_v2\n    metric: loo_sj.all_no_circularity\n    value: true\n- id: c029_llama_scierc_cross_model\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_007_llama_inference\n    metric: ner.rho_sj\n    value: 0.363\n  - exp_id: exp_007_llama_inference\n    metric: ner.rho_fk\n    value: 0.327\n  - exp_id: exp_007_llama_inference\n    metric: re.sj_rho_cond\n    value: 0.405\n  - exp_id: exp_007_llama_inference\n    metric: re.fk_rho_cond\n    value: 0.259\n- id: c030_em_conditional_dominance\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_015_metrics_expansion\n    metric: ner.em_rho_cond\n    value: 0.3427\n  - exp_id: exp_015_metrics_expansion\n    metric: re.em_rho_cond\n    value: 0.3607\n  - exp_id: exp_002_conll_n16\n    metric: conditional.EM_rho\n    value: 0.4658\n  - exp_id: exp_017_llama_conll_n16_s123\n    metric: conditional.EM_rho\n    value: 0.4732\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\n    seed/N combinations.'\n- id: c031_em_conditional_scierc\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_001_ner_n16_scierc\n    metric: ner_cond_em_rho\n    value: 0.414\n  - exp_id: exp_001_ner_n16_scierc\n    metric: re_cond_em_rho\n    value: 0.475\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\n- id: c032_logprob_re_cond_collapse\n  text: Logprob conditional RE collapses to ρ=0.011\n  sections:\n  - experiments\n  tier: 1\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    metric: re_cond.logprob.rho\n    value: 0.0112\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\n    0.002 was stale and untraceable.'\n- id: c033_sj_n16_cond_re\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_008_re_n16_v2\n    metric: sj_rho_cond\n    value: 0.308\n- id: c034_structural_over_logprob_n16\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\n    to +0.175)\n  sections:\n  - experiments\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_001_ner_n16_scierc\n    metric: ner_voting_conf_rho\n    value: 0.399\n  - exp_id: exp_001_ner_n16_scierc\n    metric: ner_logprob_rho\n    value: 0.237\n  - exp_id: exp_002_conll_n16\n    metric: full.EM_rho\n    value: 0.4627\n  - exp_id: exp_002_conll_n16\n    metric: full.logprob_rho\n    value: 0.3146\n  - exp_id: exp_007_llama_n16\n    metric: full.voting_conf_rho\n    value: 0.4515\n  - exp_id: exp_007_llama_n16\n    metric: full.logprob_rho\n    value: 0.2041\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.SJ_rho\n    value: 0.4642\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.logprob_rho\n    value: 0.3058\n- id: c035_n_scaling_diminishing\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\n  sections:\n  - discussion\n  tier: 1\n  evidence:\n  - exp_id: exp_001_seed42_v2\n    metric: sj_rho_full\n    value: 0.428\n  - exp_id: exp_015_metrics_expansion\n    metric: ner.sj_rho_full\n    value: 0.3565\n  - exp_id: exp_017_llama_conll_n16\n    metric: full.SJ_rho\n    value: 0.4642\n  - exp_id: exp_017_llama_conll_infer\n    metric: full.SJ_rho\n    value: 0.4314\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\n    - 0.431 = +0.032'\n- id: c036_sj_ece_calibration\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\n    settings)'\n  sections: []\n  tier: X\n  evidence: []\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\n    signals ECE 0.27-0.77.\n- id: C001\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: No signal significantly improves sample selection over greedy decoding despite\n    13-18pp oracle headroom\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions:\n  - D070\n  - D071\n  deprecated: false\n- id: C003\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: LP scores compressed into effective ties for 60% of instances under constrained\n    decoding\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C006\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C010\n  location:\n    section: abstract\n    paragraph: 0\n    sentence: 0\n  text: Constrained-decoding score compression is the primary bottleneck\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C011\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: LP carries useful per-sample quality information; score compression is the\n    primary bottleneck\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions:\n  - D071\n  deprecated: false\n- id: C013\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: MBR utility correlates with F1 across instances but not within\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C016\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\n  type: planned\n  evidence: []\n  decisions:\n  - D071\n  deprecated: false\n- id: C017\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\n    at selection\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C019\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: LP fails due to constrained-decoding score compression\n  type: empirical\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C022\n  location:\n    section: conclusion\n    paragraph: 0\n    sentence: 0\n  text: RE findings preliminary, single benchmark\n  type: scope_limitation\n  evidence:\n  - exp_012_rerun_1024\n  decisions: []\n  deprecated: false\n- id: C023\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\n    LP on SciERC, but selection performs worse (-2.0pp)\n  type: quantitative\n  evidence:\n  - exp_id: exp_entity_token_lp\n    metric: scierc_entity_lp_variance_ratio\n    value: 4.0x\n  - exp_id: exp_entity_token_lp\n    metric: scierc_entity_lp_selection_delta\n    value: -1.68\n  decisions: []\n  deprecated: false\n- id: C024\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\n    79% tied\n  type: quantitative\n  evidence:\n  - exp_id: exp_entity_token_lp\n    metric: conll_entity_lp_variance_median\n    value: 2e-10\n  - exp_id: exp_entity_token_lp\n    metric: conll_entity_lp_tied_fraction\n    value: 0.794\n  decisions: []\n  deprecated: false\n- id: C025\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\n    intrinsic model overconfidence on entity tokens\n  type: interpretive\n  evidence:\n  - exp_id: exp_entity_token_lp\n  decisions: []\n  deprecated: false\n- id: C026\n  location:\n    section: sections/limitations\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\n    are unexplored\n  type: scope\n  evidence:\n  - exp_id: exp_entity_token_lp\n  decisions: []\n  deprecated: false\n- id: C027\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\n    failure are the findings'\n  type: structural\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\n    characterization'\n  type: structural\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C029\n  location:\n    section: sections/introduction\n    paragraph: 0\n    sentence: 0\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\n  type: structural\n  evidence:\n  - exp_id: exp_entity_token_lp\n  decisions: []\n  deprecated: false\n- id: C030\n  location:\n    section: sections/abstract\n    paragraph: 0\n    sentence: 0\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\n    from 9 to 6 sentences'\n  type: structural\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C031\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: 21% of SciERC instances produce identical F1 across all N samples\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C032\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: 58% of CoNLL instances produce identical F1 across all N samples\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C033\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: 13% of SciERC instances yield constant utility scores\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C034\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: 49% of CoNLL instances yield constant utility scores\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C035\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: SJ median within-instance rho = 0.524 on SciERC\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C036\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: SJ median within-instance rho = 0.994 on CoNLL\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C037\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C038\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\n  type: quantitative\n  evidence: Q1 within-instance analysis\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\n  type: quantitative\n  evidence: SF4 greedy data\n  decisions: []\n  deprecated: false\n- id: C040\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: SciERC 3-epoch rho=0.32 vs 5-epoch rho=0.28; LP delta -1.18 vs +0.62 pp\n  type: quantitative\n  evidence: tab:epoch_scierc\n  decisions: []\n  deprecated: false\n- id: C041\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Entity-level majority voting yields +0.76pp on SciERC (5.8% gap recovery)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C042\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Entity-level majority voting yields -0.64pp on CoNLL\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C043\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: Entity-level majority voting yields -3.21pp on Few-NERD\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C044\n  location:\n    section: sections/discussion\n    paragraph: 0\n    sentence: 0\n  text: On degenerate subsets, merge is uniformly negative across all three datasets\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C045\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Exact permutation p=0.005 for per-type degeneracy-headroom correlation\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C046\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Under conservative df=4 adjustment, p=0.033\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C047\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 3-epoch SciERC mean within-instance rho=0.273\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C048\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 5-epoch SciERC mean within-instance rho=0.179\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C049\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 76.4% of instances show positive LP-quality correlation at 3 epochs\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C050\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 64.1% of instances show positive LP-quality correlation at 5 epochs\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C051\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Epoch-to-epoch alignment variation is 0.057 median rho, small vs cross-dataset\n    gap\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C052\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'Optimal DALS tau spans 2 orders of magnitude: FN 0.001, SciERC 0.05, CoNLL\n    0.10'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C053\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: LOO regret ranges from 0.51 to 1.21pp\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C054\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Even with oracle tau, CoNLL remains at -0.31pp\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C055\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'SciERC entity merge best k=3: +1.57pp, 11.9% recovery'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C056\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'CoNLL entity merge best k=3: -0.38pp, -9.0% recovery'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C057\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: 'FewNERD entity merge best k=2: -0.43pp, -3.6% recovery'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C058\n  location:\n    section: sections/experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Conditional decomp SciERC favorable: +2.47pp CI [+0.30, +4.70]'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C059\n  location:\n    section: sections/experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Conditional decomp FewNERD favorable: +0.63pp CI [-0.02, +1.30], marginal'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C060\n  location:\n    section: sections/experiments\n    paragraph: 0\n    sentence: 0\n  text: 'Conditional decomp CoNLL favorable: -1.78pp CI [-2.83, -0.76], negative'\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C061\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP has 4x higher within-instance variance (0.000644 vs 0.000161)\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C062\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP rho=0.440 vs full-sequence 0.297\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\n- id: C063\n  location:\n    section: sections/appendix\n    paragraph: 0\n    sentence: 0\n  text: Entity-token LP selection -0.73pp vs full-sequence +0.35pp\n  type: quantitative\n  evidence: []\n  decisions: []\n  deprecated: false\ntables:\n- id: tab:notation\n  section: method\n  caption: Notation used throughout the paper\n  evidence: []\n  note: Notation table—no experimental data.\n- id: tab:quality_estimation\n  section: experiments\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\n  evidence:\n  - exp_id: exp_012_rerun_1024\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\n  - exp_id: exp_015_metrics_expansion\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\n  - exp_id: exp_015_v2\n    role: AUROC values across settings\n  - exp_id: exp_002\n    role: CoNLL Qwen N=8 ρ and AUROC\n  - exp_id: exp_017_llama_conll_infer\n    role: CoNLL LLaMA N=8 ρ and AUROC\n  - exp_id: exp_017_llama_conll_n16\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\n  - exp_id: exp_017_llama_conll_n16_s123\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\n  - exp_id: exp_017_llama_conll_n16_s456\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\n- id: tab:selection\n  section: experiments\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\n  evidence:\n  - exp_id: exp_016_signal_ensemble\n    role: All selection F1 values (NER and RE)\n- id: tab:robustness\n  section: experiments\n  caption: Signal robustness across configurations (Spearman ρ)\n  evidence:\n  - exp_id: exp_005\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\n  - exp_id: exp_015_metrics_expansion\n    role: N=8 baseline values\n  - exp_id: exp_001_seed42_v2\n    role: N=16 SJ ρ seed=42\n  - exp_id: exp_001_seed123_v2\n    role: N=16 SJ ρ seed=123\n  - exp_id: exp_001_seed456_v2_ner\n    role: N=16 SJ ρ seed=456\n  - exp_id: exp_017_llama_conll_n16\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\n  - exp_id: exp_017_llama_conll_n16_s123\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\n  - exp_id: exp_017_llama_conll_n16_s456\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\nfigures:\n- id: fig:overview\n  section: introduction\n  caption: The correlation-selection gap conceptual diagram\n  evidence:\n  - exp_id: exp_015_metrics_expansion\n    role: Quality estimation data (ρ, AUROC for left panel)\n  - exp_id: exp_016_signal_ensemble\n    role: Selection F1 data (right panel)\n- id: fig:signal_heatmap\n  section: experiments\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\n  evidence:\n  - exp_id: exp_015_metrics_expansion\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\n  - exp_id: exp_002\n    role: CoNLL Qwen full set ρ values\n  - exp_id: exp_001_ner_n16_scierc\n    role: Conditional set ρ values\n- id: fig:selection_gap\n  section: experiments\n  caption: The correlation-selection gap on SciERC (N=8)\n  evidence:\n  - exp_id: exp_016_signal_ensemble\n    role: Best-of-N selection F1 bars and quality estimation ρ line\n- id: fig:temperature_robustness\n  section: experiments\n  caption: Temperature robustness on SciERC (N=8)\n  evidence:\n  - exp_id: exp_005\n    role: SJ, FK ρ values at T=0.7 and T=1.0\n- id: fig:reliability\n  section: experiments\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\n  evidence:\n  - exp_id: exp_015_metrics_expansion\n    role: Calibration/ECE data for all signals\n  - exp_id: exp_002\n    role: ECE values across signals\n_completeness:\n  coverage: 59/92\n  claims: 87\n  tables: 4\n  figures: 5\n  tier_counts:\n    tier1: 0\n    tier2: 59\n    tier3: 33\n    tierX: 0\n  last_checked: '2026-05-18T15:39:48.035668+00:00'\n",
      "numLines": 1217,
      "startLine": 1,
      "totalLines": 1217
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files. Let me also search the appendix for the old AUROC values. The appendix was too large to read in one go. Let me search for the specific values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "aea28546-bca8-48bb-b55e-664df957f202",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JME13qk5DQyh4JksVAMQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28589,
      "cache_read_input_tokens": 25239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28589
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

_source line 23_

Now searching the appendix for old SciERC AUROC values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "cd77149f-05a7-49d6-b5a5-d10213876578",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JME13qk5DQyh4JksVAMQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28589,
      "cache_read_input_tokens": 25239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28589
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

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_018RUrzt2uvkmCBdGCzKB5Zb`</summary>

```json
{
  "pattern": "\\.663|\\.650|\\.602|\\.614|0\\.663|0\\.650|0\\.602|0\\.614",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "cf3e3af5-6541-4dc1-9b55-673e4de0625e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JME13qk5DQyh4JksVAMQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28589,
      "cache_read_input_tokens": 25239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28589
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

_source line 25 · 2026-05-19T14:19:30.938Z_

<details><summary>↩ Tool result · `toolu_018RUrzt2uvkmCBdGCzKB5Zb`</summary>

```text
docs/paper/sections/method.tex:62:We report F1 under the protocol matching each experiment's configuration (seed, epoch, $N$). SciERC greedy F1 appears as four values across tables (0.640, 0.644, 0.645, 0.650) due to protocol variants: primary seed vs.\ multi-seed mean, 5-epoch vs.\ 3-epoch checkpoint, and gold-filtered vs.\ full test set. Each table specifies its protocol.
docs/paper/sections/experiments.tex:33:VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
docs/paper/sections/experiments.tex:34:SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
docs/paper/sections/experiments.tex:35:FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
docs/paper/sections/experiments.tex:36:EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
docs/paper/sections/appendix.tex:151:Both proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
docs/paper/sections/appendix.tex:458:LP & .283 & $\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\
docs/paper/sections/appendix.tex:467:Yet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\% vs.\ $+4.8$\%; Table~\ref{tab:hidden_probe}).
docs/paper/sections/appendix.tex:1367:SciERC & .644 & .650 & .639 (.72) & & .260 & .048 \\
docs/paper/sections/appendix.tex:1411:At 10 epochs, the model retains competitive greedy F1 (0.649 vs.\ 0.650 at 3 epochs) yet conditions are unfavorable: 47.8\% degenerate instances and $\rho{=}0.112$.
docs/paper/sections/appendix.tex:1424:Greedy F1 & 0.650 & 0.644 & 0.649 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "c05a0cf7-a84c-4254-90a2-42e7da480a66",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/method.tex:62:We report F1 under the protocol matching each experiment's configuration (seed, epoch, $N$). SciERC greedy F1 appears as four values across tables (0.640, 0.644, 0.645, 0.650) due to protocol variants: primary seed vs.\\ multi-seed mean, 5-epoch vs.\\ 3-epoch checkpoint, and gold-filtered vs.\\ full test set. Each table specifies its protocol.\ndocs/paper/sections/experiments.tex:33:VC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\ndocs/paper/sections/experiments.tex:34:SJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\ndocs/paper/sections/experiments.tex:35:FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\ndocs/paper/sections/experiments.tex:36:EM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\ndocs/paper/sections/appendix.tex:151:Both proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\ndocs/paper/sections/appendix.tex:458:LP & .283 & $\\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\\\\ndocs/paper/sections/appendix.tex:467:Yet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\\% vs.\\ $+4.8$\\%; Table~\\ref{tab:hidden_probe}).\ndocs/paper/sections/appendix.tex:1367:SciERC & .644 & .650 & .639 (.72) & & .260 & .048 \\\\\ndocs/paper/sections/appendix.tex:1411:At 10 epochs, the model retains competitive greedy F1 (0.649 vs.\\ 0.650 at 3 epochs) yet conditions are unfavorable: 47.8\\% degenerate instances and $\\rho{=}0.112$.\ndocs/paper/sections/appendix.tex:1424:Greedy F1 & 0.650 & 0.644 & 0.649 \\\\",
    "numLines": 11
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_018UjRUo9hCcQmzfGgzVFUFy`</summary>

```json
{
  "pattern": "AUROC|AUC",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "25f6bb84-0ee9-44ed-96de-4f2cf6bc5f62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JME13qk5DQyh4JksVAMQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28589,
      "cache_read_input_tokens": 25239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28589
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

_source line 27 · 2026-05-19T14:19:31.945Z_

<details><summary>↩ Tool result · `toolu_018UjRUo9hCcQmzfGgzVFUFy`</summary>

```text
docs/paper/sections/related_work.tex:23:Our QE results connect to selective prediction \cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.
docs/paper/sections/experiments.tex:25:\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
docs/paper/sections/experiments.tex:31:Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
docs/paper/sections/experiments.tex:43:Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models ($\varepsilon$-free; $\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\ref{app:epsilon_robustness}).
docs/paper/sections/experiments.tex:47:On CoNLL (single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$).
docs/paper/sections/conclusion.tex:3:[Omitted long matching line]
docs/paper/sections/discussion.tex:3:The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \cite{cobbe2021verifiers, venktesh2025trust}.
docs/paper/sections/method.tex:55:Spearman $\rho$ between the signal and instance-level F1 (per-instance entity-level F1 counting exact span-and-type matches), and AUROC classifying instances as above/below median F1.
docs/paper/sections/abstract.tex:4:All signals achieve reliable QE ($\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\,pp F1 at 80\% coverage).
docs/paper/sections/appendix.tex:215:Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
docs/paper/sections/appendix.tex:432:Adding pairwise interaction features does not help (AUROC 0.634 vs.\ 0.638).
docs/paper/sections/appendix.tex:496:\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
docs/paper/sections/appendix.tex:1196:AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
docs/paper/sections/appendix.tex:1211:VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
docs/paper/sections/appendix.tex:1213:The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
docs/paper/sections/appendix.tex:1226:Signal & $\rho$ & AUROC & Sel.\ F1 & $\Delta$ vs.\ greedy \\
docs/paper/sections/appendix.tex:1241:AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), consistent with the $\rho$--AUROC dissociation noted in the main text.
docs/paper/sections/appendix.tex:1253:\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
docs/paper/sections/appendix.tex:1257:Signal & $\rho$ & Sample AUROC & Sel.\ $\Delta$ & 95\% CI \\
docs/paper/sections/appendix.tex:1272:(2)~LP is the only signal achieving significant positive selection ($+1.39$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.
docs/paper/sections/appendix.tex:1492:Aggregation & Med.\ var. & $\rho$ & AUROC & $\Delta$ (pp) \\
docs/paper/sections/appendix.tex:1500:Despite stronger correlation ($+$48\%) and higher AUROC, entity-token LP produces worse selection, reinforcing that compression operates at the representation level rather than token aggregation: the correlation-selection gap persists even with a more targeted signal.
docs/paper/sections/introduction.tex:12:All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction.
docs/paper/sections/introduction.tex:33:    Five signals from three families evaluated on four NER benchmarks, two model families, and a 4B ablation, achieving reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "cb5abd28-96fe-4e24-95ac-9661be10f3be",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:23:Our QE results connect to selective prediction \\cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.\ndocs/paper/sections/experiments.tex:25:\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). Best in \\textbf{bold}. RE results in Appendix~\\ref{app:re_extension}. $N{=}16$ in Table~\\ref{tab:robustness}.}\ndocs/paper/sections/experiments.tex:31:Signal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\ndocs/paper/sections/experiments.tex:43:Table~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\ndocs/paper/sections/experiments.tex:47:On CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\ndocs/paper/sections/conclusion.tex:3:[Omitted long matching line]\ndocs/paper/sections/discussion.tex:3:The decoupling of $\\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal; effective selection likely requires content-aware verifiers \\cite{cobbe2021verifiers, venktesh2025trust}.\ndocs/paper/sections/method.tex:55:Spearman $\\rho$ between the signal and instance-level F1 (per-instance entity-level F1 counting exact span-and-type matches), and AUROC classifying instances as above/below median F1.\ndocs/paper/sections/abstract.tex:4:All signals achieve reliable QE ($\\rho$ up to 0.45 on CoNLL-2003, area under the ROC curve [AUROC] up to 0.82), enabling selective prediction ($+5$--$8$\\,pp F1 at 80\\% coverage).\ndocs/paper/sections/appendix.tex:215:Signal & $\\rho$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\ndocs/paper/sections/appendix.tex:432:Adding pairwise interaction features does not help (AUROC 0.634 vs.\\ 0.638).\ndocs/paper/sections/appendix.tex:496:\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\ndocs/paper/sections/appendix.tex:1196:AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\ndocs/paper/sections/appendix.tex:1211:VerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\ndocs/paper/sections/appendix.tex:1213:The AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\ndocs/paper/sections/appendix.tex:1226:Signal & $\\rho$ & AUROC & Sel.\\ F1 & $\\Delta$ vs.\\ greedy \\\\\ndocs/paper/sections/appendix.tex:1241:AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), consistent with the $\\rho$--AUROC dissociation noted in the main text.\ndocs/paper/sections/appendix.tex:1253:\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\ndocs/paper/sections/appendix.tex:1257:Signal & $\\rho$ & Sample AUROC & Sel.\\ $\\Delta$ & 95\\% CI \\\\\ndocs/paper/sections/appendix.tex:1272:(2)~LP is the only signal achieving significant positive selection ($+1.39$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.\ndocs/paper/sections/appendix.tex:1492:Aggregation & Med.\\ var. & $\\rho$ & AUROC & $\\Delta$ (pp) \\\\\ndocs/paper/sections/appendix.tex:1500:Despite stronger correlation ($+$48\\%) and higher AUROC, entity-token LP produces worse selection, reinforcing that compression operates at the representation level rather than token aggregation: the correlation-selection gap persists even with a more targeted signal.\ndocs/paper/sections/introduction.tex:12:All signals achieve reliable quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82; Figure~\\ref{fig:overview}), supporting selective prediction.\ndocs/paper/sections/introduction.tex:33:    Five signals from three families evaluated on four NER benchmarks, two model families, and a 4B ablation, achieving reliable quality estimation ($\\rho$ up to 0.45, AUROC up to 0.82).",
    "numLines": 24
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Grep · `toolu_01924GMbRXyRZvh8R23M2nKF`</summary>

```json
{
  "pattern": "0\\.75|\\.75|0\\.74|\\.74",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "7809cda8-a2f8-41e3-906a-d88f4dc428db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JME13qk5DQyh4JksVAMQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28589,
      "cache_read_input_tokens": 25239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28589
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

_source line 29 · 2026-05-19T14:19:33.125Z_

<details><summary>↩ Tool result · `toolu_01924GMbRXyRZvh8R23M2nKF`</summary>

```text
docs/paper/sections/experiments.tex:38:LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
docs/paper/sections/experiments.tex:124:Few-NERD & 32{,}565 & .748 & 13.8\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
docs/paper/sections/experiments.tex:236:       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
docs/paper/sections/experiments.tex:238:Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
docs/paper/sections/experiments.tex:239:         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
docs/paper/sections/experiments.tex:250:We estimate within-instance $\rho(\text{LP}, \text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\rho_{\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\approx}0$ (n.s.).
docs/paper/sections/appendix.tex:231:[Omitted long matching line]
docs/paper/sections/appendix.tex:772:Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
docs/paper/sections/appendix.tex:783:Oracle & 0.585 & 0.757 \\
docs/paper/sections/appendix.tex:1054:4 & 21.0\% & $+$10.2 & $+$0.03 & $-$0.31 & $-$0.40 & $-$0.74 & $-$2.16 & $+$0.03 \\
docs/paper/sections/appendix.tex:1082:VC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\
docs/paper/sections/appendix.tex:1134:0.8 & 23.8 & 0.031 & 0.471 & 0.752 \\
docs/paper/sections/appendix.tex:1196:AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
docs/paper/sections/appendix.tex:1211:VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
docs/paper/sections/appendix.tex:1213:The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
docs/paper/sections/appendix.tex:1228:VC & \textbf{.460} & .743 & 0.611 & $-$1.54\,pp \\
docs/paper/sections/appendix.tex:1253:\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
docs/paper/sections/appendix.tex:1265:\multicolumn{3}{l}{Greedy: 0.748 \quad Oracle: 0.872} & \multicolumn{2}{l}{Headroom: 12.4\,pp} \\
docs/paper/sections/appendix.tex:1300:Art & 1{,}277 & 19.8 & .756 & .754 & $-$0.17 & .451 & 9.2\,pp \\
docs/paper/sections/appendix.tex:1378:Extended training increases greedy F1 by $+2.95$~pp (0.748 $\to$ 0.777) but nearly triples instance degeneracy (11.1\% $\to$ 31.3\%), reducing the fraction of instances with non-degenerate outputs from 85.6\% to 68.7\%.
docs/paper/sections/appendix.tex:1395:Greedy F1 & 0.748 & 0.777 \\
docs/paper/sections/appendix.tex:1519:Few-NERD & 0.748 & 0.744 ($k{=}2$) & $-$0.43 & $-$3.6 \\
docs/paper/sections/appendix.tex:1552: & 0.15 & .751 & .751 & $+$0.32 & $+$0.32 \\
docs/paper/sections/appendix.tex:1553: & 0.20 & .751 & .751 & $+$0.32 & $+$0.32 \\
docs/paper/sections/appendix.tex:1554: & 0.25 & .757 & .751 & \textbf{$+$0.88} & $+$0.32 \\
docs/paper/sections/appendix.tex:1555: & 0.30 & .750 & .750 & $+$0.21 & $+$0.21 \\
docs/paper/sections/appendix.tex:1556: & 0.35 & .750 & .750 & $+$0.21 & $+$0.21 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "71cc20e3-8d4e-4a2a-92e9-def030c6ceff",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/experiments.tex:38:LP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\ndocs/paper/sections/experiments.tex:124:Few-NERD & 32{,}565 & .748 & 13.8\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\ndocs/paper/sections/experiments.tex:236:       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\ndocs/paper/sections/experiments.tex:238:Few-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\ndocs/paper/sections/experiments.tex:239:         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\ndocs/paper/sections/experiments.tex:250:We estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\ndocs/paper/sections/appendix.tex:231:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:772:Oracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\ndocs/paper/sections/appendix.tex:783:Oracle & 0.585 & 0.757 \\\\\ndocs/paper/sections/appendix.tex:1054:4 & 21.0\\% & $+$10.2 & $+$0.03 & $-$0.31 & $-$0.40 & $-$0.74 & $-$2.16 & $+$0.03 \\\\\ndocs/paper/sections/appendix.tex:1082:VC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\\\\ndocs/paper/sections/appendix.tex:1134:0.8 & 23.8 & 0.031 & 0.471 & 0.752 \\\\\ndocs/paper/sections/appendix.tex:1196:AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\ndocs/paper/sections/appendix.tex:1211:VerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\ndocs/paper/sections/appendix.tex:1213:The AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\ndocs/paper/sections/appendix.tex:1228:VC & \\textbf{.460} & .743 & 0.611 & $-$1.54\\,pp \\\\\ndocs/paper/sections/appendix.tex:1253:\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\ndocs/paper/sections/appendix.tex:1265:\\multicolumn{3}{l}{Greedy: 0.748 \\quad Oracle: 0.872} & \\multicolumn{2}{l}{Headroom: 12.4\\,pp} \\\\\ndocs/paper/sections/appendix.tex:1300:Art & 1{,}277 & 19.8 & .756 & .754 & $-$0.17 & .451 & 9.2\\,pp \\\\\ndocs/paper/sections/appendix.tex:1378:Extended training increases greedy F1 by $+2.95$~pp (0.748 $\\to$ 0.777) but nearly triples instance degeneracy (11.1\\% $\\to$ 31.3\\%), reducing the fraction of instances with non-degenerate outputs from 85.6\\% to 68.7\\%.\ndocs/paper/sections/appendix.tex:1395:Greedy F1 & 0.748 & 0.777 \\\\\ndocs/paper/sections/appendix.tex:1519:Few-NERD & 0.748 & 0.744 ($k{=}2$) & $-$0.43 & $-$3.6 \\\\\ndocs/paper/sections/appendix.tex:1552: & 0.15 & .751 & .751 & $+$0.32 & $+$0.32 \\\\\ndocs/paper/sections/appendix.tex:1553: & 0.20 & .751 & .751 & $+$0.32 & $+$0.32 \\\\\ndocs/paper/sections/appendix.tex:1554: & 0.25 & .757 & .751 & \\textbf{$+$0.88} & $+$0.32 \\\\\ndocs/paper/sections/appendix.tex:1555: & 0.30 & .750 & .750 & $+$0.21 & $+$0.21 \\\\\ndocs/paper/sections/appendix.tex:1556: & 0.35 & .750 & .750 & $+$0.21 & $+$0.21 \\\\",
    "numLines": 27
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Let me now check the appendix around line 1196 (VerbConf AUROC table) and line 1228 (Few-NERD table) and line 496 (NER AUROC multiseed) since those might reference SciERC AUROC values. Let me also check the "0.82" references - those are CoNLL, should be fine.

Let me also check the appendix for any SciERC-specific AUROC mentions. The key ones from the grep results:

1. **experiments.tex L33-36**: Table 1 - these are the main ones to fix ✓ (identified)


2. **appendix.tex L1196**: Looking at the VerbConf AUROC values (0.681 for SciERC, 0.578, 0.747, 0.753), this appears in the text around line 1211 comparing VerbConf's performance. The 0.681 is VerbConf's SciERC AUROC, which isn't one of the five main signals I need to update.

Now I'm wondering if VerbConf is actually the same as VC (Voting Confidence) or if it's a separate signal entirely. The text mentions VerbConf achieving higher ρ than LP and competitive AUROC scores, but I need to clarify whether this is one of the core signals or something different.

Let me trace through the appendix more carefully—I should look at the full VerbConf table around lines 1190-1245 to understand what's being reported. I also need to check the NER AUROC multiseed table in appendix L496 since the SciERC values there might have the same issue. There's also a VC entry for Few-NERD at L1228 that I should verify, and a statement about AUROC rankings at L1241 that I need to confirm applies to the right dataset.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "e01805e4-3935-4a89-84ab-3491087d8cba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te3Y3kQRwVCBxSA7ybyoqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4744,
      "cache_read_input_tokens": 53828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4744
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

_source line 31_

Let me check specific appendix sections that might contain SciERC AUROC values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "a2feefec-9067-466c-9773-8ac34ca01888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te3Y3kQRwVCBxSA7ybyoqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4744,
      "cache_read_input_tokens": 53828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4744
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

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01DUv5uZnNLGujU53xGu3HFD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 488,
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
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "67e66bb7-fc4b-4d69-ae0b-771659661d1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te3Y3kQRwVCBxSA7ybyoqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4744,
      "cache_read_input_tokens": 53828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4744
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

_source line 33 · 2026-05-19T14:19:53.727Z_

<details><summary>↩ Tool result · `toolu_01DUv5uZnNLGujU53xGu3HFD`</summary>

```text
488	\midrule
489	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
490	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
491	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
492	\midrule
493	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
494	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
495	\midrule
496	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
497	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
498	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
499	\bottomrule
500	\end{tabular}
501	\end{table}
502	
503	\section{Training Configuration}\label{app:training}
504	
505	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
506	
507	\begin{table}[t]
508	\centering
509	\small
510	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
511	\label{tab:training}
512	\begin{tabular}{ll}
513	\toprule
514	Parameter & Value \\
515	\midrule
516	LoRA rank / $\alpha$ & 32 / 64 \\
517	LoRA target & All linear modules \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "e38d0a3b-578d-4aa1-8894-57ae1971bc12",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .579${\\pm}$.008 & .600${\\pm}$.016 & .659${\\pm}$.016 & .677${\\pm}$.011 & .631${\\pm}$.013 \\\\\nLLaMA & .565${\\pm}$.008 & .593${\\pm}$.006 & .632${\\pm}$.012 & .673${\\pm}$.009 & .606${\\pm}$.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\",
      "numLines": 30,
      "startLine": 488,
      "totalLines": 1572
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01C9kuHE8RwQ1jzCXzPE3K4f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 1180,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "88dd77a1-272b-4290-a4dc-022c1ddecada",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te3Y3kQRwVCBxSA7ybyoqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4744,
      "cache_read_input_tokens": 53828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4744
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

_source line 35 · 2026-05-19T14:19:53.783Z_

<details><summary>↩ Tool result · `toolu_01C9kuHE8RwQ1jzCXzPE3K4f`</summary>

```text
1180	
1181	We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \citet{lin2022teaching} and \citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.
1182	Table~\ref{tab:verbconf} reports quality estimation and selection results.
1183	
1184	\begin{table}[t]
1185	\centering
1186	\small
1187	\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
1188	\label{tab:verbconf}
1189	\begin{tabular}{l cc cc}
1190	\toprule
1191	 & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{CoNLL NER}} \\
1192	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1193	Metric & VerbConf & LP & VerbConf & LP \\
1194	\midrule
1195	$\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\
1196	AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
1197	Selection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\
1198	$\Delta$ vs.\ greedy & $-$2.45\,pp & $+$0.2\,pp & $-$1.93\,pp & $-$0.77\,pp \\
1199	\midrule
1200	Mean score & 8.58\,/\,10 & --- & 9.24\,/\,10 & --- \\
1201	Parse fail rate & 0.26\% & --- & 0\% & --- \\
1202	\bottomrule
1203	\end{tabular}
1204	\end{table}
1205	
1206	\paragraph{Severe overconfidence.}
1207	VerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.
1208	This compression is more severe than LP (which spans a 0.041-nat median range); score compression is a general property of model self-assessment, not an artifact of log-probability computation.
1209	
1210	\paragraph{QE--selection decoupling.}
1211	VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
1212	This dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.
1213	The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
1214	
1215	\section{LLaMA-3.2-3B Scale Ablation}\label{app:llama3b}
1216	
1217	To extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\ref{tab:llama3b}).
1218	
1219	\begin{table}[t]
1220	\centering
1221	\small
1222	\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
1223	\label{tab:llama3b}
1224	\begin{tabular}{l cc cc}
1225	\toprule
1226	Signal & $\rho$ & AUROC & Sel.\ F1 & $\Delta$ vs.\ greedy \\
1227	\midrule
1228	VC & \textbf{.460} & .743 & 0.611 & $-$1.54\,pp \\
1229	SJ & .375 & .738 & \textbf{0.633} & $+$0.61\,pp \\
1230	EM & .334 & \textbf{.776} & --- & --- \\
1231	FK & .268 & .671 & 0.630 & $+$0.28\,pp \\
1232	LP & .266 & .633 & 0.628 & $+$0.12\,pp \\
1233	\midrule
1234	Greedy & --- & --- & 0.627 & --- \\
1235	Oracle & --- & --- & 0.763 & --- \\
1236	\bottomrule
1237	\end{tabular}
1238	\end{table}
1239	
1240	The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}); ranking stability holds across two model families spanning 3B--8B.
1241	AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), consistent with the $\rho$--AUROC dissociation noted in the main text.
1242	Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC, the strongest QE signal, yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
1243	
1244	\section{Few-NERD Full Results}\label{app:fewnerd}
1245	
1246	Table~\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).
1247	After gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\% receive zero F1 under greedy decoding.
1248	Instance degeneracy is 13.8\% (vs.\ 17.8\% on SciERC, 48.4\% on CoNLL).
1249	
1250	\begin{table}[t]
1251	\centering
1252	\small
1253	\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
1254	\label{tab:fewnerd_full}
1255	\begin{tabular}{lcccc}
1256	\toprule
1257	Signal & $\rho$ & Sample AUROC & Sel.\ $\Delta$ & 95\% CI \\
1258	\midrule
1259	LP & .220 & .578 & $\mathbf{+1.39}$\,pp & [+1.18, +1.53] \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "8f14e125-e44a-415f-9285-a67071d7acde",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\nWe evaluate verbalized confidence (VerbConf) as a second per-sample signal following \\citet{lin2022teaching} and \\citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.\nTable~\\ref{tab:verbconf} reports quality estimation and selection results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\n\\label{tab:verbconf}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{CoNLL NER}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & VerbConf & LP & VerbConf & LP \\\\\n\\midrule\n$\\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\\\\nAUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\nSelection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\\\\n$\\Delta$ vs.\\ greedy & $-$2.45\\,pp & $+$0.2\\,pp & $-$1.93\\,pp & $-$0.77\\,pp \\\\\n\\midrule\nMean score & 8.58\\,/\\,10 & --- & 9.24\\,/\\,10 & --- \\\\\nParse fail rate & 0.26\\% & --- & 0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Severe overconfidence.}\nVerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.\nThis compression is more severe than LP (which spans a 0.041-nat median range); score compression is a general property of model self-assessment, not an artifact of log-probability computation.\n\n\\paragraph{QE--selection decoupling.}\nVerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\nThis dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.\nThe AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\n\n\\section{LLaMA-3.2-3B Scale Ablation}\\label{app:llama3b}\n\nTo extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\\ref{tab:llama3b}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\n\\label{tab:llama3b}\n\\begin{tabular}{l cc cc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nVC & \\textbf{.460} & .743 & 0.611 & $-$1.54\\,pp \\\\\nSJ & .375 & .738 & \\textbf{0.633} & $+$0.61\\,pp \\\\\nEM & .334 & \\textbf{.776} & --- & --- \\\\\nFK & .268 & .671 & 0.630 & $+$0.28\\,pp \\\\\nLP & .266 & .633 & 0.628 & $+$0.12\\,pp \\\\\n\\midrule\nGreedy & --- & --- & 0.627 & --- \\\\\nOracle & --- & --- & 0.763 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\\ref{tab:quality_estimation}); ranking stability holds across two model families spanning 3B--8B.\nAUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), consistent with the $\\rho$--AUROC dissociation noted in the main text.\nDespite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC, the strongest QE signal, yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.\n\n\\section{Few-NERD Full Results}\\label{app:fewnerd}\n\nTable~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).\nAfter gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\\% receive zero F1 under greedy decoding.\nInstance degeneracy is 13.8\\% (vs.\\ 17.8\\% on SciERC, 48.4\\% on CoNLL).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\n\\label{tab:fewnerd_full}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & Sample AUROC & Sel.\\ $\\Delta$ & 95\\% CI \\\\\n\\midrule\nLP & .220 & .578 & $\\mathbf{+1.39}$\\,pp & [+1.18, +1.53] \\\\",
      "numLines": 80,
      "startLine": 1180,
      "totalLines": 1572
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3MYd8XZwHayphWF2ZYyRA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 205,
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
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "8116bb74-04fb-45cf-b75d-e82f1195f84f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Te3Y3kQRwVCBxSA7ybyoqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4744,
      "cache_read_input_tokens": 53828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4744
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

_source line 37 · 2026-05-19T14:19:53.828Z_

<details><summary>↩ Tool result · `toolu_01Q3MYd8XZwHayphWF2ZYyRA`</summary>

```text
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
212	\label{tab:wnut}
213	\begin{tabular}{lcccc}
214	\toprule
215	Signal & $\rho$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
216	\midrule
217	VC      & .724 & .913 & .038 & .487 \\
218	FK      & .125 & .555 & .169 & .002 \\
219	SJ      & .089 & .517 & .288 & ${<}$1e-7 \\
220	EM      & .050 & .487 & .333 & ${<}$1e-9 \\
221	LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	The full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.
226	VC's high full-set $\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
227	
228	\paragraph{Cross-configuration selection analysis.}
229	Table~\ref{tab:cross_selection} extends the selection analysis to five additional configurations.
230	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
231	On LLaMA FewNERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), confirming LP as the most robust selection signal across model families (Qwen FewNERD: $+1.39$~pp, Table~\ref{tab:fewnerd}). All structural signals degrade selection (VC $-2.39$~pp, SJ $-0.52$~pp), consistent with the Qwen pattern. LLaMA FewNERD degeneracy ($23.4{\pm}4.7$\%, 3 seeds) is higher than Qwen ($12.7$\%), illustrating the capability-diversity tension: LLaMA achieves stronger greedy F1 ($0.784$ vs.\ $0.748$, $+3.6$~pp) but at the cost of higher degeneracy ($+10.7$~pp) and reduced oracle headroom ($10.0$ vs.\ $12.4$~pp).
232	On CoNLL, 48--87\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
233	
234	\begin{table*}[t]
235	\centering
236	\small
237	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
238	\label{tab:cross_selection}
239	\begin{tabular}{llccccccc}
240	\toprule
241	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
242	\midrule
243	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
244	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "7f3b08f2-cbf8-497d-8ef6-f207a5f9ed69",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\\rho$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\n\\label{tab:wnut}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & .913 & .038 & .487 \\\\\nFK      & .125 & .555 & .169 & .002 \\\\\nSJ      & .089 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nThe full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.\nVC's high full-set $\\rho{=}0.724$ is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to five additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn LLaMA FewNERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), confirming LP as the most robust selection signal across model families (Qwen FewNERD: $+1.39$~pp, Table~\\ref{tab:fewnerd}). All structural signals degrade selection (VC $-2.39$~pp, SJ $-0.52$~pp), consistent with the Qwen pattern. LLaMA FewNERD degeneracy ($23.4{\\pm}4.7$\\%, 3 seeds) is higher than Qwen ($12.7$\\%), illustrating the capability-diversity tension: LLaMA achieves stronger greedy F1 ($0.784$ vs.\\ $0.748$, $+3.6$~pp) but at the cost of higher degeneracy ($+10.7$~pp) and reduced oracle headroom ($10.0$ vs.\\ $12.4$~pp).\nOn CoNLL, 48--87\\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\",
      "numLines": 40,
      "startLine": 205,
      "totalLines": 1572
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

````text
Now I have a clear picture. Let me check the multiseed AUROC table around line 496-498. The values there are:

```
\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\


```

I need to look at the surrounding context to figure out what each column represents.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "87556f67-19b6-4dfc-b6a4-7e82b733de28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoP1XdEfuAavJC7pmoCc9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 58572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01Mo79r3mh5zNUvxSH1tAmy5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 470,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "4a6f23cd-15a2-420b-8d2d-cbc73d23b6d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoP1XdEfuAavJC7pmoCc9L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 58572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

_source line 40 · 2026-05-19T14:20:02.040Z_

<details><summary>↩ Tool result · `toolu_01Mo79r3mh5zNUvxSH1tAmy5`</summary>

```text
470	A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\% vs.\ $55.8$\%); LP's bottleneck is not token aggregation.
471	The correlation-selection gap extends to model-internal representations: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\S\ref{sec:discussion}).
472	
473	\section{Multi-Seed Stability}\label{app:multiseed}
474	
475	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
476	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
477	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.
478	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
479	
480	\begin{table}[t]
481	\centering
482	\small
483	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
484	\label{tab:multiseed}
485	\begin{tabular}{lccccc}
486	\toprule
487	& LP & FK & SJ & VC & EM \\
488	\midrule
489	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
490	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
491	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
492	\midrule
493	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
494	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
495	\midrule
496	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
497	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
498	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
499	\bottomrule
500	\end{tabular}
501	\end{table}
502	
503	\section{Training Configuration}\label{app:training}
504	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a38b9630-5c16-4a75-bfda-e198f0df0828",
  "uuid": "be9c1ed1-3593-4303-be73-a606781abc6e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\\% vs.\\ $55.8$\\%); LP's bottleneck is not token aggregation.\nThe correlation-selection gap extends to model-internal representations: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\\S\\ref{sec:discussion}).\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .579${\\pm}$.008 & .600${\\pm}$.016 & .659${\\pm}$.016 & .677${\\pm}$.011 & .631${\\pm}$.013 \\\\\nLLaMA & .565${\\pm}$.008 & .593${\\pm}$.006 & .632${\\pm}$.012 & .673${\\pm}$.009 & .606${\\pm}$.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n",
      "numLines": 35,
      "startLine": 470,
      "totalLines": 1572
    }
  }
}
```

</details>

---
