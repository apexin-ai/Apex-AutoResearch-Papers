# paper scaling placeholder into experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_scaling-placeholder-into-experiments_20260519T220841.log`
- **Structured JSON:** [`b7223a58217d557a1df3.json`](../../sessions/b7/b7223a58217d557a1df3.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
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
  "uuid": "5c36b13f-440b-4dfd-8829-bcc4b24737dd",
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
    "resetsAt": 1779236400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9c96a928-e667-4c22-990f-9334b71b3caa",
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7"
}
```

---

### Assistant

_source line 4_

I'll read the three source files to understand the current structure and content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "ca77d390-fe7b-4ef1-9940-bbddf333bd9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGCDLief9jYt1W369wZvgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12393,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12393
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

<details open><summary>🔧 Tool call — Read · `toolu_01LnvR23EXkWohqfPvv4xuVr`</summary>

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
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "bdb54b12-23df-44ae-85d5-d526beec4ae1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGCDLief9jYt1W369wZvgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12393,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12393
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

_source line 6 · 2026-05-19T22:08:53.303Z_

<details><summary>↩ Tool result · `toolu_01LnvR23EXkWohqfPvv4xuVr`</summary>

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
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
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
48	At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ at $N{=}16$, but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
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
89	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\rho$ (seed 42); line with error bars: $\Delta$F1 vs.\ greedy (3-seed mean, seeds 42/123/456). Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.0$~pp); dotted gray: random baseline.}
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
102	Three factors qualitatively shape LP selection gains: (1)~\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\%, CoNLL 61.7\%; Table~\ref{tab:fewnerd}); (2)~\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\approx}4$\,pp vs.\ SciERC 13.0\,pp); (3)~\textit{LP-quality alignment}, measured as within-instance $\rho(\text{LP}, \text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
103	These factors are consistent with the observed pattern (Table~\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\pm}0.48$\,pp, 3-seed; Table~\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\% of instances yield F1${=}0$.
104	Yet QE remains effective on WNUT-17 (VC $\rho{=}0.724$, $N{=}16$; Table~\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.
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
122	CoNLL & 2{,}756 & .908 & 61.7\% & .302 & $-$0.85\,pp & 1.0 \\
123	SciERC & 529 & .644 & 17.8\% & .205 & $+$0.61\,pp & .193 \\
124	Few-NERD & 32{,}565 & .748 & 13.0\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
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
188	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%).}
189	\label{tab:scale_comparison}
190	\resizebox{\columnwidth}{!}{%
191	\begin{tabular}{@{}llccccccc@{}}
192	\toprule
193	Dataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\
194	\midrule
195	SciERC & 8B FT  & .644 & 13.0 & 17.8 & .379 & .360 & .267 & .205 \\
196	       & 72B ZS & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\
197	\midrule
198	Few-NERD & 8B FT & .748 & 12.4 & 13.0 & --- & --- & --- & .220 \\
199	         & 72B ZS & .628 & --- & 46.2 & .416 & .345 & --- & .119 \\
200	\midrule
201	CoNLL  & 8B FT  & .908 & ${\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\
202	       & 72B ZS & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\
203	\bottomrule
204	\end{tabular}}
205	\end{table}
206	
207	LP $\rho$ drops sharply without fine-tuning across all three datasets (Table~\ref{tab:scale_comparison}), and LP selection fails on all. Structural signals generalize to zero-shot (Few-NERD VC $\rho{=}0.416$, SJ $0.345$). Degeneracy increases (Few-NERD: $46.2$\% vs.\ $13.0$\%; CoNLL: $67.7$\% vs.\ $61.7$\%).
208	This comparison simultaneously varies model family (Qwen3$\to$Qwen2.5), training regime (fine-tuned$\to$zero-shot), and quantization (FP16$\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.
209	LP-weighted construction yields $+1.53$\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\% of headroom (FT: $7.8$\% SciERC, $11.3$\% Few-NERD). Majority vote also succeeds ($+1.39$\,pp); LP-weighting adds $+0.14$\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\,pp) and CoNLL ($-0.37$\,pp), where degeneracy exceeds $46$\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).
210	
211	%% ============================================================
212	\subsection{Prescriptive Results}
213	\label{sec:prescriptive}
214	
215	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
216	
217	\paragraph{Entity-level construction.}
218	Rather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\theta{=}2/N$ (${\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\theta$ stable within $[0.15, 0.35]$; Appendix~\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\,pp, CoNLL $-0.92$\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\,pp; \S\ref{sec:scaling}).
219	
220	\begin{table}[t]
221	\centering
222	\small
223	\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. Best in \textbf{bold}. $^\ddagger$LP-weighted not computed; uniform only.}
224	\label{tab:entity_construction}
225	\resizebox{\columnwidth}{!}{%
226	\begin{tabular}{@{}llcccc@{}}
227	\toprule
228	Dataset & Wt. & Greedy & Constr. & $\Delta$ & $p$ \\
229	\midrule
230	SciERC & LP & $.646{\pm}.002$ & $\mathbf{.656{\pm}.003}$ & $+1.02{\pm}0.49$\,pp & .004 \\
231	       & Unif. & $.646{\pm}.002$ & $.653{\pm}.006$ & $+0.74{\pm}0.71$\,pp & .023 \\
232	\addlinespace
233	Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001$ \\
234	         & Unif. & $.748$ & $.756{\pm}.006$ & $+0.74{\pm}0.58$\,pp & .003 \\
235	\addlinespace
236	CoNLL$^\ddagger$ & Unif. & .908 & .904 & $-0.39$\,pp & n.s. \\
237	\bottomrule
238	\end{tabular}}
239	\end{table}
240	
241	LP-weighted construction improves over greedy on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$; Table~\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\approx}$8\% (SciERC) and 11\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\ref{app:n_scaling}).
242	
243	\paragraph{LP-alignment gating (preliminary diagnostic).}
244	Construction and LP selection are complementary: construction dominates on SciERC ($+1.02$\,pp vs.\ LP $+0.04{\pm}0.48$\,pp, n.s.; $\rho{\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\ $+1.39$\,pp; $\rho{\approx}0.5$--$0.7$).
245	We estimate within-instance $\rho(\text{LP}, \text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\rho_{\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\approx}0$ (n.s.).
246	The protocol performs three-way routing: (1)~$\rho_{\text{adj}} \geq \tau{=}0.3$: apply LP selection; (2)~$\rho_{\text{adj}} < \tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.
247	This routes Few-NERD to LP selection ($+1.39$\,pp); SciERC, CoNLL, and WNUT-17 fall below $\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\,pp) for protection against negative outcomes (CoNLL $-0.39$\,pp, WNUT-17 n.s.).
248	Routing is stable across $\tau{\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.
249	
250	\paragraph{Selective prediction.}
251	Orthogonal to construction, QE signals support selective prediction: at 80\% coverage, filtering low-confidence instances yields $+5$--$8$\,pp F1 (AUPRC 0.70--0.92; Table~\ref{tab:cross_selection}).
252	
253	\phantomsection\label{sec:selection_results}
254	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "9b8ac825-683f-494e-8477-cf29a63ce061",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \\textbf{bold}. RE in Appendix~\\ref{app:re_extension}; $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ at $N{=}16$, but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.0$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 61.7\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}4$\\,pp vs.\\ SciERC 13.0\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$, $N{=}16$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 61.7\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.0\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination and hidden probes.}\nSupervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\nHidden state probes improve correlation ($+37$\\% on SciERC) but not selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%).}\n\\label{tab:scale_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .644 & 13.0 & 17.8 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nFew-NERD & 8B FT & .748 & 12.4 & 13.0 & --- & --- & --- & .220 \\\\\n         & 72B ZS & .628 & --- & 46.2 & .416 & .345 & --- & .119 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP $\\rho$ drops sharply without fine-tuning across all three datasets (Table~\\ref{tab:scale_comparison}), and LP selection fails on all. Structural signals generalize to zero-shot (Few-NERD VC $\\rho{=}0.416$, SJ $0.345$). Degeneracy increases (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%).\nThis comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\\theta{=}2/N$ (${\\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\\theta$ stable within $[0.15, 0.35]$; Appendix~\\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\\,pp, CoNLL $-0.92$\\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\\,pp; \\S\\ref{sec:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}. $^\\ddagger$LP-weighted not computed; uniform only.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL$^\\ddagger$ & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\\approx}$8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\\ref{app:n_scaling}).\n\n\\paragraph{LP-alignment gating (preliminary diagnostic).}\nConstruction and LP selection are complementary: construction dominates on SciERC ($+1.02$\\,pp vs.\\ LP $+0.04{\\pm}0.48$\\,pp, n.s.; $\\rho{\\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\\ $+1.39$\\,pp; $\\rho{\\approx}0.5$--$0.7$).\nWe estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\nThe protocol performs three-way routing: (1)~$\\rho_{\\text{adj}} \\geq \\tau{=}0.3$: apply LP selection; (2)~$\\rho_{\\text{adj}} < \\tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.\nThis routes Few-NERD to LP selection ($+1.39$\\,pp); SciERC, CoNLL, and WNUT-17 fall below $\\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\\,pp) for protection against negative outcomes (CoNLL $-0.39$\\,pp, WNUT-17 n.s.).\nRouting is stable across $\\tau{\\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, filtering low-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; Table~\\ref{tab:cross_selection}).\n\n\\phantomsection\\label{sec:selection_results}\n",
      "numLines": 254,
      "startLine": 1,
      "totalLines": 254
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01MHHeEorKr8cJmS6SeaGMEX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_A_monotonic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "19baab4c-3844-4189-bea8-d120d7a4c9a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGCDLief9jYt1W369wZvgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12393,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12393
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

_source line 8 · 2026-05-19T22:08:53.810Z_

<details><summary>↩ Tool result · `toolu_01MHHeEorKr8cJmS6SeaGMEX`</summary>

```text
1	%% Version A: Monotonic scaling narrative (7B < 14B < 32B degeneracy)
2	%% Use condition: Qwen2.5 FT results show degeneracy rising monotonically with scale.
3	%% Status: Placeholder framework — fill numbers when exp results arrive.
4	
5	%% ---- Placeholder commands (replace with actual values) ----
6	\newcommand{\scaleSevenDegen}{XX.X}    % 7B degeneracy %
7	\newcommand{\scaleFourteenDegen}{XX.X} % 14B degeneracy %
8	\newcommand{\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %
9	\newcommand{\scaleSevenGreedy}{.XXX}   % 7B greedy F1
10	\newcommand{\scaleFourteenGreedy}{.XXX}% 14B greedy F1
11	\newcommand{\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1
12	\newcommand{\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)
13	\newcommand{\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)
14	\newcommand{\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)
15	\newcommand{\scaleSevenLP}{.XXX}       % 7B LP ρ
16	\newcommand{\scaleFourteenLP}{.XXX}    % 14B LP ρ
17	\newcommand{\scaleThirtytwoLP}{.XXX}   % 32B LP ρ
18	
19	%% ---- Narrative ----
20	
21	\paragraph{Degeneracy rises with scale within a model family.}
22	To examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).
23	Degeneracy increases monotonically with parameter count: $\scaleSevenDegen\%\to\scaleFourteenDegen\%\to\scaleThirtytwoDegen\%$ (Figure~\ref{fig:scaling_curve}a).
24	Greedy F1 also rises ($\scaleSevenGreedy\to\scaleFourteenGreedy\to\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.
25	LP-weighted construction $\Delta$F1 inversely tracks degeneracy ($\scaleSevenConstr\to\scaleFourteenConstr\to\scaleThirtytwoConstr$\,pp), consistent with the gating hypothesis from \S\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.
26	
27	This within-family trend converges with two independent dimensions of evidence.
28	Along the \emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\% to 31.3\% (\S\ref{sec:fewnerd}), mirroring the effect of added parameters.
29	Along the \emph{family} dimension, Qwen3-8B FT (13.0\% degeneracy, $+1.40$\,pp construction) and Qwen2.5-72B ZS (46.2\%, $-0.20$\,pp) bracket the trade-off from opposite ends.
30	Across all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "60ec2bde-7ce5-440e-80fb-50c5a89fbe5e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_A_monotonic.tex",
      "content": "%% Version A: Monotonic scaling narrative (7B < 14B < 32B degeneracy)\n%% Use condition: Qwen2.5 FT results show degeneracy rising monotonically with scale.\n%% Status: Placeholder framework — fill numbers when exp results arrive.\n\n%% ---- Placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ\n\n%% ---- Narrative ----\n\n\\paragraph{Degeneracy rises with scale within a model family.}\nTo examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).\nGreedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.\nLP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.\n\nThis within-family trend converges with two independent dimensions of evidence.\nAlong the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.\nAlong the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.40$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.\nAcross all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01ANMAZDXoGYYG3Te3SEGud4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "48b6e975-8828-40d4-8428-a50b12e330c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGCDLief9jYt1W369wZvgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12393,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12393
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

_source line 10 · 2026-05-19T22:08:54.281Z_

<details><summary>↩ Tool result · `toolu_01ANMAZDXoGYYG3Te3SEGud4`</summary>

```text
1	%% Draft: Zero-shot / Scaling paragraph for \S5.5 (Scaling Behavior)
2	%% Exp ID: exp_qwen25_72b_zeroshot (all 72B ZS numbers)
3	%% Status: Draft for Paper Agent integration. Replaces current \S5.5 content.
4	%% Pending: 7B/14B/32B FT results for full scaling curve; 72B FT for regime disentanglement.
5	
6	\subsection{Scaling Behavior}
7	\label{sec:scaling}
8	
9	To test whether the correlation-selection gap is specific to fine-tuned models, we evaluate Qwen2.5-72B-Instruct (AWQ 4-bit) in a zero-shot setting across all three primary datasets ($N{=}8$, $T{=}1.0$, no task-specific training).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Fine-tuned 8B vs.\ zero-shot 72B: QE correlations and entity construction ($N{=}8$, $T{=}1.0$). Degen.\ = instance degeneracy (\%). Constr.\ = LP-weighted entity construction $\Delta$F1 vs.\ greedy (pp). $^\dagger$Majority voting (uniform weights).}
15	\label{tab:zs_72b}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llcccccr@{}}
18	\toprule
19	Dataset & Regime & Greedy & Degen. & LP $\rho$ & SJ $\rho$ & VC $\rho$ & Constr. \\
20	\midrule
21	SciERC & 8B FT  & .645 & 17.8\% & .205 & .360 & .379 & $+$1.02 \\
22	       & 72B ZS & .399 & 21.0\% & .081 & .217 & .277 & $+$1.53 \\
23	\midrule
24	Few-NERD & 8B FT & .748 & 13.0\% & .220 & .380 & --- & $+$1.40 \\
25	         & 72B ZS & .628 & 46.2\% & .119 & .345 & .416 & $-$0.20 \\
26	\midrule
27	CoNLL  & 8B FT  & .908 & 61.7\% & .302 & .436 & .424 & $-$0.39 \\
28	       & 72B ZS & .712 & 67.7\% & $-$.002 & .304 & .297 & $-$0.37 \\
29	\bottomrule
30	\end{tabular}}
31	\end{table}
32	
33	\paragraph{LP requires fine-tuning calibration.}
34	Table~\ref{tab:zs_72b} compares QE correlations between regimes.
35	LP $\rho$ drops to near zero in the zero-shot setting: from $0.205$ to $0.081$ on SciERC, $0.220$ to $0.119$ on Few-NERD, and $0.302$ to $-0.002$ on CoNLL.
36	Fine-tuning calibrates the model's token-level confidence to task-specific quality gradients; without this calibration, LP provides little discriminative signal for candidate quality.
37	
38	\paragraph{Structural signals generalize beyond fine-tuning.}
39	VC and SJ retain moderate correlations in the zero-shot regime (VC $\rho{=}0.277$--$0.416$, SJ $\rho{=}0.217$--$0.345$), despite the absence of task-specific training.
40	These signals measure inter-sample agreement, a property of output consistency that does not require the model's confidence to be calibrated to a particular task.
41	The divergence between LP and structural signals under zero-shot conditions reflects the correlation-selection gap from a complementary angle: structural signals capture consistency as a task-agnostic distributional property, while LP depends on fine-tuning to align confidence with performance.
42	
43	\paragraph{Degeneracy gates construction effectiveness.}
44	Entity construction (\S\ref{sec:prescriptive}) with LP-weighting yields $+1.53$\,pp on SciERC ($p{=}0.008$, 95\% CI [$+0.25$, $+2.82$]\,pp), where zero-shot degeneracy is lowest (21.0\%).
45	Majority voting also improves SciERC by $+1.39$\,pp; the marginal contribution of LP-weighting over uniform voting is $+0.14$\,pp.
46	On Few-NERD (46.2\% degeneracy, $-0.20$\,pp) and CoNLL (67.7\%, $-0.37$\,pp), construction provides no benefit.
47	This monotonic relationship between degeneracy and construction gain is consistent with the gating hypothesis from \S\ref{sec:fewnerd}: construction recovers value only when candidate diversity is sufficient for recall-driven aggregation.
48	
49	\paragraph{The gap is not a fine-tuning artifact.}
50	Zero-shot LP $\rho$ approaches zero on all three datasets, and LP selection fails on SciERC ($-0.1$\,pp) and CoNLL ($-0.4$\,pp).
51	The same structural factors identified in \S\ref{sec:selection_gap} operate here: weak LP-quality alignment and instance degeneracy compress the effective candidate space.
52	That the gap persists at $9{\times}$ the parameter count, in a zero-shot regime without LoRA fine-tuning, and across three datasets with varying difficulty is consistent with the gap being a structural property of self-consistency applied to structured IE rather than an artifact of a specific training configuration.
53	
54	%% Placeholder: scaling curve figure
55	\begin{figure}[t]
56	\centering
57	% \includegraphics[width=\columnwidth]{figures/fig_scaling_curve.pdf}
58	\textcolor{red}{TODO: Scaling curve (4B/8B/14B/32B/72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\rho$. Separate lines for fine-tuned vs.\ zero-shot.}
59	\caption{\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}
60	\label{fig:scaling_curve}
61	\end{figure}
62	
63	%% TODO: 7B/14B/32B fine-tuned results to complete the scaling curve.
64	%% TODO: 72B fine-tuned results to disentangle scale effect from training regime effect.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "bb851e60-ad98-42a6-b909-d2649add2552",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex",
      "content": "%% Draft: Zero-shot / Scaling paragraph for \\S5.5 (Scaling Behavior)\n%% Exp ID: exp_qwen25_72b_zeroshot (all 72B ZS numbers)\n%% Status: Draft for Paper Agent integration. Replaces current \\S5.5 content.\n%% Pending: 7B/14B/32B FT results for full scaling curve; 72B FT for regime disentanglement.\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTo test whether the correlation-selection gap is specific to fine-tuned models, we evaluate Qwen2.5-72B-Instruct (AWQ 4-bit) in a zero-shot setting across all three primary datasets ($N{=}8$, $T{=}1.0$, no task-specific training).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B: QE correlations and entity construction ($N{=}8$, $T{=}1.0$). Degen.\\ = instance degeneracy (\\%). Constr.\\ = LP-weighted entity construction $\\Delta$F1 vs.\\ greedy (pp). $^\\dagger$Majority voting (uniform weights).}\n\\label{tab:zs_72b}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccccr@{}}\n\\toprule\nDataset & Regime & Greedy & Degen. & LP $\\rho$ & SJ $\\rho$ & VC $\\rho$ & Constr. \\\\\n\\midrule\nSciERC & 8B FT  & .645 & 17.8\\% & .205 & .360 & .379 & $+$1.02 \\\\\n       & 72B ZS & .399 & 21.0\\% & .081 & .217 & .277 & $+$1.53 \\\\\n\\midrule\nFew-NERD & 8B FT & .748 & 13.0\\% & .220 & .380 & --- & $+$1.40 \\\\\n         & 72B ZS & .628 & 46.2\\% & .119 & .345 & .416 & $-$0.20 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & 61.7\\% & .302 & .436 & .424 & $-$0.39 \\\\\n       & 72B ZS & .712 & 67.7\\% & $-$.002 & .304 & .297 & $-$0.37 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{LP requires fine-tuning calibration.}\nTable~\\ref{tab:zs_72b} compares QE correlations between regimes.\nLP $\\rho$ drops to near zero in the zero-shot setting: from $0.205$ to $0.081$ on SciERC, $0.220$ to $0.119$ on Few-NERD, and $0.302$ to $-0.002$ on CoNLL.\nFine-tuning calibrates the model's token-level confidence to task-specific quality gradients; without this calibration, LP provides little discriminative signal for candidate quality.\n\n\\paragraph{Structural signals generalize beyond fine-tuning.}\nVC and SJ retain moderate correlations in the zero-shot regime (VC $\\rho{=}0.277$--$0.416$, SJ $\\rho{=}0.217$--$0.345$), despite the absence of task-specific training.\nThese signals measure inter-sample agreement, a property of output consistency that does not require the model's confidence to be calibrated to a particular task.\nThe divergence between LP and structural signals under zero-shot conditions reflects the correlation-selection gap from a complementary angle: structural signals capture consistency as a task-agnostic distributional property, while LP depends on fine-tuning to align confidence with performance.\n\n\\paragraph{Degeneracy gates construction effectiveness.}\nEntity construction (\\S\\ref{sec:prescriptive}) with LP-weighting yields $+1.53$\\,pp on SciERC ($p{=}0.008$, 95\\% CI [$+0.25$, $+2.82$]\\,pp), where zero-shot degeneracy is lowest (21.0\\%).\nMajority voting also improves SciERC by $+1.39$\\,pp; the marginal contribution of LP-weighting over uniform voting is $+0.14$\\,pp.\nOn Few-NERD (46.2\\% degeneracy, $-0.20$\\,pp) and CoNLL (67.7\\%, $-0.37$\\,pp), construction provides no benefit.\nThis monotonic relationship between degeneracy and construction gain is consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: construction recovers value only when candidate diversity is sufficient for recall-driven aggregation.\n\n\\paragraph{The gap is not a fine-tuning artifact.}\nZero-shot LP $\\rho$ approaches zero on all three datasets, and LP selection fails on SciERC ($-0.1$\\,pp) and CoNLL ($-0.4$\\,pp).\nThe same structural factors identified in \\S\\ref{sec:selection_gap} operate here: weak LP-quality alignment and instance degeneracy compress the effective candidate space.\nThat the gap persists at $9{\\times}$ the parameter count, in a zero-shot regime without LoRA fine-tuning, and across three datasets with varying difficulty is consistent with the gap being a structural property of self-consistency applied to structured IE rather than an artifact of a specific training configuration.\n\n%% Placeholder: scaling curve figure\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\columnwidth]{figures/fig_scaling_curve.pdf}\n\\textcolor{red}{TODO: Scaling curve (4B/8B/14B/32B/72B). Panels: (a) greedy/oracle F1 and headroom, (b) signal $\\rho$. Separate lines for fine-tuned vs.\\ zero-shot.}\n\\caption{\\textcolor{red}{TODO: Signal quality and oracle headroom across model scales.}}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n%% TODO: 7B/14B/32B fine-tuned results to complete the scaling curve.\n%% TODO: 72B fine-tuned results to disentangle scale effect from training regime effect.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the current state:

1. `experiments.tex` already has a `\subsection{Scaling Behavior}` at line 180 (§5.5 / §4.6 depending on numbering) with content about 72B ZS vs 8B FT comparison.
2. Version A has the monotonic scaling narrative with placeholder commands for 7B/14B/32B.
3. The ZS draft has a more detailed version of the scaling section.

The task is to integrate Version A's content into the existing scaling section in experiments.tex. The existing section already covers the 72B ZS comparison. I need to:


- Define the placeholder commands (either at the file start or as comments before the section)
- Insert Version A's narrative about within-family scaling after the existing content
- Add the scaling comparison table and figure placeholders
- Include the Version B note

I'm thinking about placement: the `\newcommand` definitions should probably go near the top of experiments.tex or as comments before the scaling section, then the narrative and table/figure placeholders follow after the current 72B comparison content around line 209. I need to check what labels are already defined in the existing files and avoid duplicates. The ZS draft has a placeholder for `fig:scaling_curve` at line 60, and Version A references it at line 23, so I should use that same label. Now I'm ready to construct the actual edit by inserting the newcommand placeholders before the Scaling Behavior subsection, then adding the Version A content after the existing 72B discussion but before the Prescriptive Results section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "66878327-b6fe-423b-a487-d5326a2bdf03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgHy1LAiSMiv3nJ6BPwMFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11110,
      "cache_read_input_tokens": 24234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11110
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

_source line 12_

The existing `experiments.tex` already has a `\subsection{Scaling Behavior}` at line 180 with 72B ZS content. I'll integrate Version A's within-family scaling narrative and placeholders after the existing content, before `\subsection{Prescriptive Results}`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "e4f87e0b-3183-4211-9146-804048b14bb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgHy1LAiSMiv3nJ6BPwMFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11110,
      "cache_read_input_tokens": 24234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11110
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01T7iXkBEy1zdBemyndvoFVE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}",
  "new_string": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\n%% ---- Scaling placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "63632548-3dec-41bf-8fc9-110070cf15a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgHy1LAiSMiv3nJ6BPwMFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11110,
      "cache_read_input_tokens": 24234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11110
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

_source line 14 · 2026-05-19T22:09:26.658Z_

<details><summary>↩ Tool result · `toolu_01T7iXkBEy1zdBemyndvoFVE`</summary>

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
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "dd9887c3-b323-46f6-ac8e-2e9ffc072df4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}",
    "newString": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\n%% ---- Scaling placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \\textbf{bold}. RE in Appendix~\\ref{app:re_extension}; $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ at $N{=}16$, but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.0$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 61.7\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}4$\\,pp vs.\\ SciERC 13.0\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$, $N{=}16$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 61.7\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.0\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination and hidden probes.}\nSupervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\nHidden state probes improve correlation ($+37$\\% on SciERC) but not selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%).}\n\\label{tab:scale_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .644 & 13.0 & 17.8 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nFew-NERD & 8B FT & .748 & 12.4 & 13.0 & --- & --- & --- & .220 \\\\\n         & 72B ZS & .628 & --- & 46.2 & .416 & .345 & --- & .119 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP $\\rho$ drops sharply without fine-tuning across all three datasets (Table~\\ref{tab:scale_comparison}), and LP selection fails on all. Structural signals generalize to zero-shot (Few-NERD VC $\\rho{=}0.416$, SJ $0.345$). Degeneracy increases (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%).\nThis comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\\theta{=}2/N$ (${\\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\\theta$ stable within $[0.15, 0.35]$; Appendix~\\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\\,pp, CoNLL $-0.92$\\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\\,pp; \\S\\ref{sec:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}. $^\\ddagger$LP-weighted not computed; uniform only.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL$^\\ddagger$ & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\\approx}$8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\\ref{app:n_scaling}).\n\n\\paragraph{LP-alignment gating (preliminary diagnostic).}\nConstruction and LP selection are complementary: construction dominates on SciERC ($+1.02$\\,pp vs.\\ LP $+0.04{\\pm}0.48$\\,pp, n.s.; $\\rho{\\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\\ $+1.39$\\,pp; $\\rho{\\approx}0.5$--$0.7$).\nWe estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\nThe protocol performs three-way routing: (1)~$\\rho_{\\text{adj}} \\geq \\tau{=}0.3$: apply LP selection; (2)~$\\rho_{\\text{adj}} < \\tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.\nThis routes Few-NERD to LP selection ($+1.39$\\,pp); SciERC, CoNLL, and WNUT-17 fall below $\\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\\,pp) for protection against negative outcomes (CoNLL $-0.39$\\,pp, WNUT-17 n.s.).\nRouting is stable across $\\tau{\\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, filtering low-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; Table~\\ref{tab:cross_selection}).\n\n\\phantomsection\\label{sec:selection_results}\n",
    "structuredPatch": [
      {
        "oldStart": 180,
        "oldLines": 6,
        "newStart": 180,
        "newLines": 20,
        "lines": [
          " \\subsection{Scaling Behavior}",
          " \\label{sec:scaling}",
          " ",
          "+%% ---- Scaling placeholder commands (replace with actual values) ----",
          "+\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %",
          "+\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %",
          "+\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %",
          "+\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1",
          "+\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1",
          "+\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1",
          "+\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)",
          "+\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)",
          "+\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)",
          "+\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ",
          "+\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ",
          "+\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ",
          "+",
          " We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.",
          " ",
          " \\begin{table}[t]"
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01Gwfy8oLwQhAuCimCaF7yK5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n%% ============================================================\n\\subsection{Prescriptive Results}",
  "new_string": "This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n\\paragraph{Degeneracy rises with scale within a model family.}\nTo examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).\nGreedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.\nLP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.\n\nThis within-family trend converges with two independent dimensions of evidence.\nAlong the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.\nAlong the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.40$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.\nAcross all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scaling analysis: Qwen2.5 fine-tuned on FewNERD ($N{=}8$, $T{=}1.0$, 3-seed mean). 8B row from Qwen3-8B (Table~\\ref{tab:fewnerd}).}\n\\label{tab:scaling_ft}\n\\begin{tabular}{lcccccc}\n\\toprule\nScale & Degen\\% & LP $\\rho$ & SJ $\\rho$ & Greedy & Constr.\\ $\\Delta$ & $p$ \\\\\n\\midrule\n7B  & \\scaleSevenDegen & \\scaleSevenLP & --- & \\scaleSevenGreedy & \\scaleSevenConstr & --- \\\\\n8B  & 13.0 & .220 & .380 & .748 & $+$1.40 & ${<}.001$ \\\\\n14B & \\scaleFourteenDegen & \\scaleFourteenLP & --- & \\scaleFourteenGreedy & \\scaleFourteenConstr & --- \\\\\n32B & \\scaleThirtytwoDegen & \\scaleThirtytwoLP & --- & \\scaleThirtytwoGreedy & \\scaleThirtytwoConstr & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n%\\includegraphics[width=\\columnwidth]{figures/scaling_curve.pdf}\n\\caption{Degeneracy and LP-weighted construction $\\Delta$F1 across model scales (FewNERD, $N{=}8$). Placeholder --- data pending.}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n% NOTE: Version B (non-monotonic narrative) available at artifacts/scaling_narrative_B_nonmonotonic.tex\n\n%% ============================================================\n\\subsection{Prescriptive Results}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "74655d66-68cf-477f-a923-83419f3f80d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBbStgEVMAXi6KHzDt4MTD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1524,
      "cache_read_input_tokens": 35344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1524
      },
      "output_tokens": 73,
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

_source line 16 · 2026-05-19T22:10:02.166Z_

<details><summary>↩ Tool result · `toolu_01Gwfy8oLwQhAuCimCaF7yK5`</summary>

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
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "d5391cce-587e-4c3c-a985-a4a69c9c8d9e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "oldString": "This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n%% ============================================================\n\\subsection{Prescriptive Results}",
    "newString": "This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n\\paragraph{Degeneracy rises with scale within a model family.}\nTo examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).\nGreedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.\nLP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.\n\nThis within-family trend converges with two independent dimensions of evidence.\nAlong the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.\nAlong the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.40$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.\nAcross all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scaling analysis: Qwen2.5 fine-tuned on FewNERD ($N{=}8$, $T{=}1.0$, 3-seed mean). 8B row from Qwen3-8B (Table~\\ref{tab:fewnerd}).}\n\\label{tab:scaling_ft}\n\\begin{tabular}{lcccccc}\n\\toprule\nScale & Degen\\% & LP $\\rho$ & SJ $\\rho$ & Greedy & Constr.\\ $\\Delta$ & $p$ \\\\\n\\midrule\n7B  & \\scaleSevenDegen & \\scaleSevenLP & --- & \\scaleSevenGreedy & \\scaleSevenConstr & --- \\\\\n8B  & 13.0 & .220 & .380 & .748 & $+$1.40 & ${<}.001$ \\\\\n14B & \\scaleFourteenDegen & \\scaleFourteenLP & --- & \\scaleFourteenGreedy & \\scaleFourteenConstr & --- \\\\\n32B & \\scaleThirtytwoDegen & \\scaleThirtytwoLP & --- & \\scaleThirtytwoGreedy & \\scaleThirtytwoConstr & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n%\\includegraphics[width=\\columnwidth]{figures/scaling_curve.pdf}\n\\caption{Degeneracy and LP-weighted construction $\\Delta$F1 across model scales (FewNERD, $N{=}8$). Placeholder --- data pending.}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n% NOTE: Version B (non-monotonic narrative) available at artifacts/scaling_narrative_B_nonmonotonic.tex\n\n%% ============================================================\n\\subsection{Prescriptive Results}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.\n\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\n\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\n\n\\paragraph{Models and sampling.}\n\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \\textbf{bold}. RE in Appendix~\\ref{app:re_extension}; $N{=}16$ in Table~\\ref{tab:robustness}.}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & \\textbf{.663} & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .650 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & .614 & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\n\\midrule\nLP     & Model      & .205 & .578 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nTable~\\ref{tab:quality_estimation} presents $\\rho$ and AUROC for five signals across tasks and models ($\\varepsilon$-free; $\\varepsilon{=}0.05$ applies to selection only, stable across $[0, 0.2]$, Appendix~\\ref{app:epsilon_robustness}).\n\n\\paragraph{Signal rankings are difficulty-dependent.}\nOn SciERC (medium difficulty), structural signals lead (VC $\\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\\Delta\\rho{=}{+}0.155$; Appendix~\\ref{app:bootstrap_signal}).\nOn CoNLL (single-sample F1${\\approx}$0.91), EM leads both $\\rho$ and AUROC ($0.816$).\nAt the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ at $N{=}16$, but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nThis collapse illustrates a regime where model capability is insufficient to produce meaningful inter-sample variation: 51\\% of instances yield zero F1 across all samples, and consistency signals merely detect this floor rather than discriminating quality among non-trivial outputs.\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\nFour of five signals (SJ, FK, EM, VC) assign identical scores to all candidates from the same input by construction (\\S\\ref{sec:formulation}); they can estimate quality across instances but cannot rank candidates within an instance.\nThe empirical question is whether LP, the sole per-sample signal, can exploit its candidate-discriminative nature for selection.\nLP selection effectiveness is primarily determined by LP-quality alignment rather than degeneracy level (\\S\\ref{sec:discussion}).\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-sample signal}} \\\\\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Instance-level signals (consensus-proximity selection)}} \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\\n\\midrule\nRandom           & $0.610 \\pm 0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.0$~pp); dotted gray: random baseline.}\n\\label{fig:selection_gap}\n\\end{figure}\n\nInstance-level signals assign identical QE scores to all candidates; MBR conversion does not improve over greedy on the primary test bed (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}).\nInstance-level signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} is best.\n\n\\paragraph{LP: the sole per-sample signal also fails.}\nOn SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nThe pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nFew-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\n\n\\paragraph{Qualitative factors governing selection effectiveness.}\nThree factors qualitatively shape LP selection gains: (1)~\\textit{instance degeneracy} compresses the candidate space, leaving fewer instances where any signal can improve over greedy (SciERC 17.8\\%, CoNLL 61.7\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} bounds the maximum achievable gain (CoNLL ${\\approx}4$\\,pp vs.\\ SciERC 13.0\\,pp); (3)~\\textit{LP-quality alignment}, measured as within-instance $\\rho(\\text{LP}, \\text{F1})$, determines whether LP can discriminate candidates in the remaining non-degenerate instances (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nThese factors are consistent with the observed pattern (Table~\\ref{tab:fewnerd}): Few-NERD (low degeneracy, strong alignment) shows the largest LP gain ($+1.39$\\,pp), SciERC (weak alignment) shows unreliable gains ($+0.04{\\pm}0.48$\\,pp, 3-seed; Table~\\ref{tab:multiseed}), CoNLL (high degeneracy, minimal headroom) shows no gain, and WNUT-17 represents the signal-collapse boundary: LP $\\rho{=}{-}0.446$ (the model assigns higher log-probabilities to confidently wrong outputs), within-instance alignment absent ($\\rho{=}0.043$, n.s.), and construction ineffective ($p{>}0.05$, mixed sign) because 51\\% of instances yield F1${=}0$.\nYet QE remains effective on WNUT-17 (VC $\\rho{=}0.724$, $N{=}16$; Table~\\ref{tab:wnut}), confirming QE-selection decoupling at this boundary.\nThis characterization is qualitative: the three factors do not combine into a predictive model ($R^2{<}0$ across 23 configurations), but each factor's role is individually supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\n\n%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\n\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 61.7\\% & .302 & $-$0.85\\,pp & 1.0 \\\\\nSciERC & 529 & .644 & 17.8\\% & .205 & $+$0.61\\,pp & .193 \\\\\nFew-NERD & 32{,}565 & .748 & 13.0\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy: $+1.39$~pp ($p{<}0.001$), while structural signals degrade selection (VC $-1.79$, SJ $-2.14$~pp). LP is 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp) and generalizes to LLaMA-3.1-8B (Table~\\ref{tab:cross_selection}).\nTraining convergence modulates degeneracy: 5-epoch Few-NERD raises degeneracy to 31\\% and halves LP gains (Appendix~\\ref{app:epoch_confound}).\n\n\\paragraph{Degeneracy alone does not predict LP selection direction.}\nAcross 23 configurations, degeneracy does not predict LP gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}), though within fixed settings it causally modulates LP ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}).\nCross-dataset prediction requires LP signal quality: Few-NERD ($\\rho{\\approx}0.5$--$0.7$) shows consistent gains, SciERC ($\\rho{\\approx}0.26$) does not (Appendix~\\ref{app:conditional_decomp}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_degeneracy_lp_scatter.pdf}\n\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\n\\label{fig:degeneracy_scatter}\n\\end{figure}\n\nStructural signals remain negative regardless of sample budget; $N$-scaling analyses are in Appendix~\\ref{app:n_scaling}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency signals are robust across $T{\\in}\\{0.7, 1.0\\}$ with sublinear $N$-scaling gains (Table~\\ref{tab:robustness}); signal rankings are stable across seeds ($W{=}1.0$; Table~\\ref{tab:ranking-stability}). NER calibration is reasonable (ECE 0.069--0.096; Appendix~\\ref{app:calibration}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Scale robustness.}\nWith Qwen3-4B (Table~\\ref{tab:scale_ablation}), QE is comparable (mean $|\\Delta\\rho|{=}0.042$), yet selection remains below greedy despite 13.0~pp headroom. Task difficulty is a stronger predictor than model scale within the 3B--8B range (Appendix~\\ref{app:llama3b}).\nDegeneracy scales with capability: 8B shows 17.8\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{LoRA-rank ablation.}\nLoRA rank${=}8$ (vs.\\ 32) lowers degeneracy to 7.2\\% but LP remains below greedy ($\\rho(\\text{LP}, \\text{F1}){\\approx}0.24$); temperature manipulation ($T{=}1.2$; \\S\\ref{sec:discussion}) confirms that low degeneracy and adequate alignment are independently necessary.\n\n\\paragraph{Supervised signal combination and hidden probes.}\nSupervised classifiers (LR, MLP, RF; 5-fold CV, $N{=}16$) and a DeBERTa-v3-base verifier all fail to close the selection gap (Appendix~\\ref{app:supervised_combination}).\nHidden state probes improve correlation ($+37$\\% on SciERC) but not selection (gap closure $-5.1$\\%; Appendix~\\ref{app:hidden_probe}); the bottleneck extends to model-internal representations.\n\n%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\n%% ---- Scaling placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%).}\n\\label{tab:scale_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .644 & 13.0 & 17.8 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nFew-NERD & 8B FT & .748 & 12.4 & 13.0 & --- & --- & --- & .220 \\\\\n         & 72B ZS & .628 & --- & 46.2 & .416 & .345 & --- & .119 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP $\\rho$ drops sharply without fine-tuning across all three datasets (Table~\\ref{tab:scale_comparison}), and LP selection fails on all. Structural signals generalize to zero-shot (Few-NERD VC $\\rho{=}0.416$, SJ $0.345$). Degeneracy increases (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%).\nThis comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n\n\\paragraph{Entity-level construction.}\nRather than selecting one of $N$ complete outputs, we aggregate entities across all samples, retaining those exceeding a confirmation threshold $\\theta{=}2/N$ (${\\geq}2$ of $N$ samples), with LP-weighted or uniform frequency scoring. Under fine-tuning, this default achieves the best or near-best F1 across all datasets ($\\theta$ stable within $[0.15, 0.35]$; Appendix~\\ref{app:theta_sweep}). In the zero-shot regime, uniform voting degrades (SciERC $-0.52$\\,pp, CoNLL $-0.92$\\,pp) because greater output diversity admits noise entities; LP-weighting is necessary for construction to succeed without fine-tuning (SciERC $+1.5$\\,pp; \\S\\ref{sec:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}. $^\\ddagger$LP-weighted not computed; uniform only.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.646{\\pm}.002$ & $\\mathbf{.656{\\pm}.003}$ & $+1.02{\\pm}0.49$\\,pp & .004 \\\\\n       & Unif. & $.646{\\pm}.002$ & $.653{\\pm}.006$ & $+0.74{\\pm}0.71$\\,pp & .023 \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001$ \\\\\n         & Unif. & $.748$ & $.756{\\pm}.006$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL$^\\ddagger$ & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP-weighted construction improves over greedy on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$; Table~\\ref{tab:entity_construction}), positive across all 7 seed-dataset combinations, recovering ${\\approx}$8\\% (SciERC) and 11\\% (Few-NERD) of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with ceiling-regime degeneracy. The mechanism is recall-driven: aggregating low-frequency correct entities recovers mentions that no single sample captures ($N$-scaling in Appendix~\\ref{app:n_scaling}).\n\n\\paragraph{LP-alignment gating (preliminary diagnostic).}\nConstruction and LP selection are complementary: construction dominates on SciERC ($+1.02$\\,pp vs.\\ LP $+0.04{\\pm}0.48$\\,pp, n.s.; $\\rho{\\approx}0.2$), while on Few-NERD both yield comparable gains ($+1.40$ vs.\\ $+1.39$\\,pp; $\\rho{\\approx}0.5$--$0.7$).\nWe estimate within-instance $\\rho(\\text{LP}, \\text{F1})$ on 50 held-out instances with bootstrap CIs (1000 resamples). Degeneracy-adjusted $\\rho_{\\text{adj}}$: Few-NERD $0.516$ [0.459, 0.759], SciERC $0.167$ [0.146, 0.281], CoNLL $0.065$ [$-$0.061, 0.620], WNUT-17 ${\\approx}0$ (n.s.).\nThe protocol performs three-way routing: (1)~$\\rho_{\\text{adj}} \\geq \\tau{=}0.3$: apply LP selection; (2)~$\\rho_{\\text{adj}} < \\tau$ and construction shows positive dev-set gain: apply construction; (3)~otherwise: retain greedy decoding.\nThis routes Few-NERD to LP selection ($+1.39$\\,pp); SciERC, CoNLL, and WNUT-17 fall below $\\tau$ and route to greedy. The conservative protocol trades SciERC's missed construction gain ($+1.02$\\,pp) for protection against negative outcomes (CoNLL $-0.39$\\,pp, WNUT-17 n.s.).\nRouting is stable across $\\tau{\\in}[0.2, 0.4]$ and matches test-set direction for all four datasets; narrower inter-dataset margins remain untested.\n\n\\paragraph{Selective prediction.}\nOrthogonal to construction, QE signals support selective prediction: at 80\\% coverage, filtering low-confidence instances yields $+5$--$8$\\,pp F1 (AUPRC 0.70--0.92; Table~\\ref{tab:cross_selection}).\n\n\\phantomsection\\label{sec:selection_results}\n",
    "structuredPatch": [
      {
        "oldStart": 222,
        "oldLines": 6,
        "newStart": 222,
        "newLines": 43,
        "lines": [
          " This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.",
          " LP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).",
          " ",
          "+\\paragraph{Degeneracy rises with scale within a model family.}",
          "+To examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).",
          "+Degeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).",
          "+Greedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.",
          "+LP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.",
          "+",
          "+This within-family trend converges with two independent dimensions of evidence.",
          "+Along the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.",
          "+Along the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.40$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.",
          "+Across all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.",
          "+",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\small",
          "+\\caption{Scaling analysis: Qwen2.5 fine-tuned on FewNERD ($N{=}8$, $T{=}1.0$, 3-seed mean). 8B row from Qwen3-8B (Table~\\ref{tab:fewnerd}).}",
          "+\\label{tab:scaling_ft}",
          "+\\begin{tabular}{lcccccc}",
          "+\\toprule",
          "+Scale & Degen\\% & LP $\\rho$ & SJ $\\rho$ & Greedy & Constr.\\ $\\Delta$ & $p$ \\\\",
          "+\\midrule",
          "+7B  & \\scaleSevenDegen & \\scaleSevenLP & --- & \\scaleSevenGreedy & \\scaleSevenConstr & --- \\\\",
          "+8B  & 13.0 & .220 & .380 & .748 & $+$1.40 & ${<}.001$ \\\\",
          "+14B & \\scaleFourteenDegen & \\scaleFourteenLP & --- & \\scaleFourteenGreedy & \\scaleFourteenConstr & --- \\\\",
          "+32B & \\scaleThirtytwoDegen & \\scaleThirtytwoLP & --- & \\scaleThirtytwoGreedy & \\scaleThirtytwoConstr & --- \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          "+\\begin{figure}[t]",
          "+\\centering",
          "+%\\includegraphics[width=\\columnwidth]{figures/scaling_curve.pdf}",
          "+\\caption{Degeneracy and LP-weighted construction $\\Delta$F1 across model scales (FewNERD, $N{=}8$). Placeholder --- data pending.}",
          "+\\label{fig:scaling_curve}",
          "+\\end{figure}",
          "+",
          "+% NOTE: Version B (non-monotonic narrative) available at artifacts/scaling_narrative_B_nonmonotonic.tex",
          "+",
          " %% ============================================================",
          " \\subsection{Prescriptive Results}",
          " \\label{sec:prescriptive}"
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

_source line 17_

验证最终文件结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "ff3edd46-40ea-4bab-9db3-706fd57e47de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJZZZaXJ6tCeQp9HZmqrua",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 36868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1802
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

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01XH4Rwo8KcxFkb4hXRuJ5LX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 179,
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
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "26595850-a51c-4321-960e-97763000f70a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJZZZaXJ6tCeQp9HZmqrua",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 36868,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1802
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

_source line 19 · 2026-05-19T22:10:05.331Z_

<details><summary>↩ Tool result · `toolu_01XH4Rwo8KcxFkb4hXRuJ5LX`</summary>

```text
179	%% ============================================================
180	\subsection{Scaling Behavior}
181	\label{sec:scaling}
182	
183	%% ---- Scaling placeholder commands (replace with actual values) ----
184	\newcommand{\scaleSevenDegen}{XX.X}    % 7B degeneracy %
185	\newcommand{\scaleFourteenDegen}{XX.X} % 14B degeneracy %
186	\newcommand{\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %
187	\newcommand{\scaleSevenGreedy}{.XXX}   % 7B greedy F1
188	\newcommand{\scaleFourteenGreedy}{.XXX}% 14B greedy F1
189	\newcommand{\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1
190	\newcommand{\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)
191	\newcommand{\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)
192	\newcommand{\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)
193	\newcommand{\scaleSevenLP}{.XXX}       % 7B LP ρ
194	\newcommand{\scaleFourteenLP}{.XXX}    % 14B LP ρ
195	\newcommand{\scaleThirtytwoLP}{.XXX}   % 32B LP ρ
196	
197	We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.
198	
199	\begin{table}[t]
200	\centering
201	\small
202	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%).}
203	\label{tab:scale_comparison}
204	\resizebox{\columnwidth}{!}{%
205	\begin{tabular}{@{}llccccccc@{}}
206	\toprule
207	Dataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\
208	\midrule
209	SciERC & 8B FT  & .644 & 13.0 & 17.8 & .379 & .360 & .267 & .205 \\
210	       & 72B ZS & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\
211	\midrule
212	Few-NERD & 8B FT & .748 & 12.4 & 13.0 & --- & --- & --- & .220 \\
213	         & 72B ZS & .628 & --- & 46.2 & .416 & .345 & --- & .119 \\
214	\midrule
215	CoNLL  & 8B FT  & .908 & ${\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\
216	       & 72B ZS & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\
217	\bottomrule
218	\end{tabular}}
219	\end{table}
220	
221	LP $\rho$ drops sharply without fine-tuning across all three datasets (Table~\ref{tab:scale_comparison}), and LP selection fails on all. Structural signals generalize to zero-shot (Few-NERD VC $\rho{=}0.416$, SJ $0.345$). Degeneracy increases (Few-NERD: $46.2$\% vs.\ $13.0$\%; CoNLL: $67.7$\% vs.\ $61.7$\%).
222	This comparison simultaneously varies model family (Qwen3$\to$Qwen2.5), training regime (fine-tuned$\to$zero-shot), and quantization (FP16$\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.
223	LP-weighted construction yields $+1.53$\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\% of headroom (FT: $7.8$\% SciERC, $11.3$\% Few-NERD). Majority vote also succeeds ($+1.39$\,pp); LP-weighting adds $+0.14$\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\,pp) and CoNLL ($-0.37$\,pp), where degeneracy exceeds $46$\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).
224	
225	\paragraph{Degeneracy rises with scale within a model family.}
226	To examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).
227	Degeneracy increases monotonically with parameter count: $\scaleSevenDegen\%\to\scaleFourteenDegen\%\to\scaleThirtytwoDegen\%$ (Figure~\ref{fig:scaling_curve}a).
228	Greedy F1 also rises ($\scaleSevenGreedy\to\scaleFourteenGreedy\to\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.
229	LP-weighted construction $\Delta$F1 inversely tracks degeneracy ($\scaleSevenConstr\to\scaleFourteenConstr\to\scaleThirtytwoConstr$\,pp), consistent with the gating hypothesis from \S\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.
230	
231	This within-family trend converges with two independent dimensions of evidence.
232	Along the \emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\% to 31.3\% (\S\ref{sec:fewnerd}), mirroring the effect of added parameters.
233	Along the \emph{family} dimension, Qwen3-8B FT (13.0\% degeneracy, $+1.40$\,pp construction) and Qwen2.5-72B ZS (46.2\%, $-0.20$\,pp) bracket the trade-off from opposite ends.
234	Across all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.
235	
236	\begin{table}[t]
237	\centering
238	\small
239	\caption{Scaling analysis: Qwen2.5 fine-tuned on FewNERD ($N{=}8$, $T{=}1.0$, 3-seed mean). 8B row from Qwen3-8B (Table~\ref{tab:fewnerd}).}
240	\label{tab:scaling_ft}
241	\begin{tabular}{lcccccc}
242	\toprule
243	Scale & Degen\% & LP $\rho$ & SJ $\rho$ & Greedy & Constr.\ $\Delta$ & $p$ \\
244	\midrule
245	7B  & \scaleSevenDegen & \scaleSevenLP & --- & \scaleSevenGreedy & \scaleSevenConstr & --- \\
246	8B  & 13.0 & .220 & .380 & .748 & $+$1.40 & ${<}.001$ \\
247	14B & \scaleFourteenDegen & \scaleFourteenLP & --- & \scaleFourteenGreedy & \scaleFourteenConstr & --- \\
248	32B & \scaleThirtytwoDegen & \scaleThirtytwoLP & --- & \scaleThirtytwoGreedy & \scaleThirtytwoConstr & --- \\
249	\bottomrule
250	\end{tabular}
251	\end{table}
252	
253	\begin{figure}[t]
254	\centering
255	%\includegraphics[width=\columnwidth]{figures/scaling_curve.pdf}
256	\caption{Degeneracy and LP-weighted construction $\Delta$F1 across model scales (FewNERD, $N{=}8$). Placeholder --- data pending.}
257	\label{fig:scaling_curve}
258	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "6701ab63-1aaa-4a19-87bb-84be21de0caf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\n%% ---- Scaling placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ\n\nWe evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Fine-tuned 8B vs.\\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%).}\n\\label{tab:scale_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .644 & 13.0 & 17.8 & .379 & .360 & .267 & .205 \\\\\n       & 72B ZS & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nFew-NERD & 8B FT & .748 & 12.4 & 13.0 & --- & --- & --- & .220 \\\\\n         & 72B ZS & .628 & --- & 46.2 & .416 & .345 & --- & .119 \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP $\\rho$ drops sharply without fine-tuning across all three datasets (Table~\\ref{tab:scale_comparison}), and LP selection fails on all. Structural signals generalize to zero-shot (Few-NERD VC $\\rho{=}0.416$, SJ $0.345$). Degeneracy increases (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%).\nThis comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n\\paragraph{Degeneracy rises with scale within a model family.}\nTo examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).\nGreedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.\nLP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.\n\nThis within-family trend converges with two independent dimensions of evidence.\nAlong the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.\nAlong the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.40$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.\nAcross all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scaling analysis: Qwen2.5 fine-tuned on FewNERD ($N{=}8$, $T{=}1.0$, 3-seed mean). 8B row from Qwen3-8B (Table~\\ref{tab:fewnerd}).}\n\\label{tab:scaling_ft}\n\\begin{tabular}{lcccccc}\n\\toprule\nScale & Degen\\% & LP $\\rho$ & SJ $\\rho$ & Greedy & Constr.\\ $\\Delta$ & $p$ \\\\\n\\midrule\n7B  & \\scaleSevenDegen & \\scaleSevenLP & --- & \\scaleSevenGreedy & \\scaleSevenConstr & --- \\\\\n8B  & 13.0 & .220 & .380 & .748 & $+$1.40 & ${<}.001$ \\\\\n14B & \\scaleFourteenDegen & \\scaleFourteenLP & --- & \\scaleFourteenGreedy & \\scaleFourteenConstr & --- \\\\\n32B & \\scaleThirtytwoDegen & \\scaleThirtytwoLP & --- & \\scaleThirtytwoGreedy & \\scaleThirtytwoConstr & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n%\\includegraphics[width=\\columnwidth]{figures/scaling_curve.pdf}\n\\caption{Degeneracy and LP-weighted construction $\\Delta$F1 across model scales (FewNERD, $N{=}8$). Placeholder --- data pending.}\n\\label{fig:scaling_curve}\n\\end{figure}",
      "numLines": 80,
      "startLine": 179,
      "totalLines": 305
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01HhfoHSP44j9Bxcp2A3UwGD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": 258,
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
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "773cb2a4-c509-43a9-a928-886272f66674",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdpVfhmreaHYBpdBCCm5qw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2540,
      "cache_read_input_tokens": 38670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2540
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

_source line 21 · 2026-05-19T22:10:09.423Z_

<details><summary>↩ Tool result · `toolu_01HhfoHSP44j9Bxcp2A3UwGD`</summary>

```text
258	\end{figure}
259	
260	% NOTE: Version B (non-monotonic narrative) available at artifacts/scaling_narrative_B_nonmonotonic.tex
261	
262	%% ============================================================
263	\subsection{Prescriptive Results}
264	\label{sec:prescriptive}
265	
266	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
267	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "929c163c-91da-4c9c-b745-d67f81fab3f1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\end{figure}\n\n% NOTE: Version B (non-monotonic narrative) available at artifacts/scaling_narrative_B_nonmonotonic.tex\n\n%% ============================================================\n\\subsection{Prescriptive Results}\n\\label{sec:prescriptive}\n\nThe preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.\n",
      "numLines": 10,
      "startLine": 258,
      "totalLines": 305
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

已完成。experiments.tex 中新增内容位于 §5.5 Scaling Behavior：

**插入位置和内容：**
- **L183–195**: 12 个 `\newcommand` placeholder（7B/14B/32B 的 degen、greedy、constr、LP）
- **L225–234**: Version A 叙事段落 — "Degeneracy rises with scale within a model family"，含三维证据收敛（scale/epoch/family）
- **L236–251**: Table `tab:scaling_ft` — 7B/14B/32B/8B 对比表，8B 行填入已知值
- **L253–258**: Figure `fig:scaling_curve` placeholder（`\includegraphics` 已注释）
- **L260**: Version B 备选注释

**待填 placeholder 清单（12 个）：**

| 命令 | 含义 |
|------|------|
| `\scaleSevenDegen` | 7B degeneracy % |
| `\scaleFourteenDegen` | 14B degeneracy % |
| `\scaleThirtytwoDegen` | 32B degeneracy % |
| `\scaleSevenGreedy` | 7B greedy F1 |
| `\scaleFourteenGreedy` | 14B greedy F1 |
| `\scaleThirtytwoGreedy` | 32B greedy F1 |
| `\scaleSevenConstr` | 7B construction Δ (pp) |
| `\scaleFourteenConstr` | 14B construction Δ (pp) |
| `\scaleThirtytwoConstr` | 32B construction Δ (pp) |
| `\scaleSevenLP` | 7B LP ρ |
| `\scaleFourteenLP` | 14B LP ρ |
| `\scaleThirtytwoLP` | 32B LP ρ |

Table 中 SJ ρ 列 7B/14B/32B 也为 `---`，待实验数据补充。Figure 的 `scaling_curve.pdf` 待生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "uuid": "cca000f3-ccae-4a07-8ba2-c3d4dbba77e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UncMYmhBYAzczQs8ML4fed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 359,
      "cache_read_input_tokens": 41210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 359
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

已完成。experiments.tex 中新增内容位于 §5.5 Scaling Behavior：

**插入位置和内容：**
- **L183–195**: 12 个 `\newcommand` placeholder（7B/14B/32B 的 degen、greedy、constr、LP）
- **L225–234**: Version A 叙事段落 — "Degeneracy rises with scale within a model family"，含三维证据收敛（scale/epoch/family）
- **L236–251**: Table `tab:scaling_ft` — 7B/14B/32B/8B 对比表，8B 行填入已知值
- **L253–258**: Figure `fig:scaling_curve` placeholder（`\includegraphics` 已注释）
- **L260**: Version B 备选注释

**待填 placeholder 清单（12 个）：**

| 命令 | 含义 |
|------|------|
| `\scaleSevenDegen` | 7B degeneracy % |
| `\scaleFourteenDegen` | 14B degeneracy % |
| `\scaleThirtytwoDegen` | 32B degeneracy % |
| `\scaleSevenGreedy` | 7B greedy F1 |
| `\scaleFourteenGreedy` | 14B greedy F1 |
| `\scaleThirtytwoGreedy` | 32B greedy F1 |
| `\scaleSevenConstr` | 7B construction Δ (pp) |
| `\scaleFourteenConstr` | 14B construction Δ (pp) |
| `\scaleThirtytwoConstr` | 32B construction Δ (pp) |
| `\scaleSevenLP` | 7B LP ρ |
| `\scaleFourteenLP` | 14B LP ρ |
| `\scaleThirtytwoLP` | 32B LP ρ |

Table 中 SJ ρ 列 7B/14B/32B 也为 `---`，待实验数据补充。Figure 的 `scaling_curve.pdf` 待生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 92347,
  "duration_api_ms": 93464,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "c91cbb5b-429c-4eea-9564-f1aeaf0980a7",
  "total_cost_usd": 0.3888485,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 29728,
    "cache_read_input_tokens": 188167,
    "output_tokens": 4282,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29728,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 564,
        "cache_read_input_tokens": 41210,
        "cache_creation_input_tokens": 359,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 359
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1790,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001875,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 4282,
      "cacheReadInputTokens": 188167,
      "cacheCreationInputTokens": 29728,
      "webSearchRequests": 0,
      "costUSD": 0.38697349999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b7cad10b-3683-4ca1-8941-43c6d51940bb"
}
```

</details>

---
