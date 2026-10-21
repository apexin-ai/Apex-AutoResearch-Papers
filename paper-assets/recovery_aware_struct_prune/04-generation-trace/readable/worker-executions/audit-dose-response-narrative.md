# audit dose response narrative

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_audit_dose_response_narrative_20260524T071531.log`
- **Structured JSON:** [`9dadea98f57e1afa95c4.json`](../../sessions/9d/9dadea98f57e1afa95c4.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
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
  "uuid": "e4d6ce98-efff-4cda-824f-b949773acd9e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779616200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4c178dc7-f678-4b3d-9d29-b4413a294877",
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0"
}
```

---

### Assistant

_source line 4_

Let我先读取相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "ee9f9e9b-ee6e-4df9-b5f6-254955991d23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCbETFgvACsfY8pkgJn8uB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12622,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12622
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

<details open><summary>🔧 Tool call — Glob · `toolu_01WQuKCF6zkEp1WV2pCrbsvD`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "965ecfb6-0746-40f9-9c23-b4a91bb7fa05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCbETFgvACsfY8pkgJn8uB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12622,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12622
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

_source line 6 · 2026-05-24T07:15:44.507Z_

<details><summary>↩ Tool result · `toolu_01WQuKCF6zkEp1WV2pCrbsvD`</summary>

```text
docs/paper/backup/experiments.tex
docs/paper/backup/introduction.tex
docs/paper/backup/method.tex
docs/paper/backup/related_work.tex
docs/paper/tables/_deprecated/table2_recovery.tex
docs/paper/tables/tab_cka_stability.tex
docs/paper/main.tex
docs/paper/tables/table3_alpha.tex
docs/paper/tables/_deprecated/table5_inference.tex
docs/paper/tables/tab_mbpp.tex
docs/paper/tables/_deprecated/table1_postprune.tex
docs/paper/limitations.tex
docs/paper/tables/table4_sparsity_cliff.tex
docs/paper/ethics.tex
docs/paper/abstract.tex
docs/paper/method.tex
docs/paper/tables/tab1_recovery_gradient.tex
docs/paper/tables/tab2_decoupling.tex
docs/paper/related_work.tex
docs/paper/tables/tab5_cross_scale.tex
docs/paper/appendix.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/tables/tab_math500.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "fa32712b-2227-4445-bd2b-d0accb8c5da0",
  "tool_use_result": {
    "filenames": [
      "docs/paper/backup/experiments.tex",
      "docs/paper/backup/introduction.tex",
      "docs/paper/backup/method.tex",
      "docs/paper/backup/related_work.tex",
      "docs/paper/tables/_deprecated/table2_recovery.tex",
      "docs/paper/tables/tab_cka_stability.tex",
      "docs/paper/main.tex",
      "docs/paper/tables/table3_alpha.tex",
      "docs/paper/tables/_deprecated/table5_inference.tex",
      "docs/paper/tables/tab_mbpp.tex",
      "docs/paper/tables/_deprecated/table1_postprune.tex",
      "docs/paper/limitations.tex",
      "docs/paper/tables/table4_sparsity_cliff.tex",
      "docs/paper/ethics.tex",
      "docs/paper/abstract.tex",
      "docs/paper/method.tex",
      "docs/paper/tables/tab1_recovery_gradient.tex",
      "docs/paper/tables/tab2_decoupling.tex",
      "docs/paper/related_work.tex",
      "docs/paper/tables/tab5_cross_scale.tex",
      "docs/paper/appendix.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/experiments.tex",
      "docs/paper/tables/tab_math500.tex"
    ],
    "durationMs": 5,
    "numFiles": 25,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_012KQThQCvCvSUSxgFWy4795`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "77c98c05-0209-4827-81af-288eb600b137",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6CNKSYbFdRRCbPQyJEkjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 416,
      "cache_read_input_tokens": 24463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 416
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

_source line 8 · 2026-05-24T07:15:46.805Z_

<details><summary>↩ Tool result · `toolu_012KQThQCvCvSUSxgFWy4795`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model and evaluation.}
9	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (architecture details in Section~\ref{sec:prelim}).
10	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
11	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
12	For rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
13	The original unpruned model achieves 90.83\% on GSM8K (greedy decoding).
14	
15	\paragraph{Pruning methods.}
16	We compare four pruning criteria at 20\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention per layer):
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.
19	    \item \textbf{Random}: uniform random selection among eligible groups.
20	    \item \textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\citep{llmpruner2023}.
21	    \item \textbf{\rasp{}} ($\alpha{=}1.0$): the composite score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}), removing structures that are both low-importance and functionally redundant.
22	\end{enumerate}
23	
24	\paragraph{Recovery pipeline and hardware.}
25	All four methods undergo matched two-stage recovery.
26	Stage~1 (SFT warmup): 2 epochs on 7{,}473 GSM8K chain-of-thought examples with teacher forcing (37 minutes), restoring EOS generation and basic format compliance.
27	Stage~2 (GRPO): Group Relative Policy Optimization~\citep{shao2024grpo} with learning rate $1{\times}10^{-6}$, maximum completion length 1{,}024 tokens, KL penalty coefficient $\beta{=}0.01$, sampling temperature 0.4, DAPO-style clipped loss, and binary reward ($r{=}1$ if correct, $r{=}0$ otherwise), trained for 100 steps on 1{,}000 GSM8K training problems.
28	All methods use identical GRPO configuration with \texttt{max\_completion\_length}{$=$}1{,}024, except Random which uses the TRL default of 512 tokens (Table~\ref{tab:hyperparams}; Appendix~\ref{sec:appendix_training}), making it a conservative comparison point.
29	Seeds vary at the GRPO stage; pruning calibration and SFT use identical configurations across all methods.
30	We repeat GRPO training with 3 random seeds for CKA-only, Standard, and Random (Table~\ref{tab:decoupling}).
31	CKA-only achieves 64.39\% $\pm$ 0.19\,pp (std across seeds), Standard 59.84\% $\pm$ 0.38\,pp; the 4.55\,pp gap is robust across seeds (Welch's $t$-test, $p{=}0.0009$, Cohen's $d{=}11.1$; 95\% CI for mean difference: $[3.62, 5.47]$\,pp), confirming that recovery capacity differences are structural rather than stochastic (per-seed results in Appendix~\ref{sec:appendix_seed}).
32	All experiments run on 2$\times$ NVIDIA RTX PRO 6000 GPUs (94\,GB VRAM each); pruning variants are trained in parallel on separate GPUs under identical wall-clock conditions.
33	
34	
35	\subsection{Recovery Capacity Spectrum}
36	\label{sec:recovery_gradient}
37	
38	\input{tables/tab1_recovery_gradient}
39	
40	\begin{figure*}[t]
41	    \centering
42	    \begin{minipage}[t]{0.38\textwidth}
43	        \centering
44	        \includegraphics[width=\textwidth]{figures/paper/fig2_reward_trajectories.pdf}
45	        \centerline{\small (a) Reward trajectories}
46	    \end{minipage}
47	    \hfill
48	    \begin{minipage}[t]{0.58\textwidth}
49	        \centering
50	        \includegraphics[width=\textwidth]{figures/paper/fig3_collapse_dynamics.pdf}
51	        \centerline{\small (b) $f_0$ and gradient norm diagnostics}
52	    \end{minipage}
53	    \caption{GRPO training dynamics for four pruning criteria (100 steps, $\beta{=}0.01$, $T{=}0.4$). (a)~Reward: CKA-only reaches 0.354 peak; Random oscillates (0.14--0.19); Standard peaks at 0.081; \rasp{} collapses to 0.010. (b)~Left: $f_0$ (zero-variance batch fraction)---CKA-only stays below 0.35 while Standard and \rasp{} remain in the collapse zone ($f_0 > 0.5$). Right: gradient norm---\rasp{} norms near zero throughout; Standard shows a transient minimum at step 90.}
54	    \label{fig:training_dynamics}
55	\end{figure*}
56	
57	Under GRPO training, the four pruning criteria produce a clear recovery capacity spectrum: CKA-only $\gg$ Random $\gg$ Standard $>$ \rasp{} $\alpha{=}1.0$ (Table~\ref{tab:recovery_gradient}, Figure~\ref{fig:training_dynamics}).
58	The pruning criterion, not training configuration, determines whether the model learns, stagnates, or collapses.
59	
60	Among these configurations, only the diversity-maximizing criterion (CKA-only) produces active learning: peak reward 0.354 with $f_0$ as low as 0.125 (Figure~\ref{fig:training_dynamics}b).
61	Random stagnates (reward 0.14--0.19, min $f_0 = 0.300$); Standard exhibits borderline collapse ($f_0 \geq 0.50$, peak reward 0.081); \rasp{} at $\alpha{=}1.0$ collapses ($f_0 \geq 0.675$, reward declining to 0.010, with near-zero KL divergence indicating minimal policy movement; Appendix~\ref{sec:appendix_kl}).
62	The dose-response (\S\ref{sec:sparsity_cliff}) confirms CKA weight as the critical variable: increasing $\alpha$ from 1.0 to 2.0 shifts \rasp{} from collapse to peak recovery (66.11\% vs.\ 64.39\% for CKA-only on GSM8K).
63	
64	
65	\subsection{Reward-Accuracy Decoupling}
66	\label{sec:decoupling}
67	
68	\input{tables/tab2_decoupling}
69	
70	\begin{figure}[t]
71	    \centering
72	    \includegraphics[width=\columnwidth]{figures/paper/fig_sft_grpo_scatter.pdf}
73	    \caption{SFT vs GRPO accuracy across all pruning criteria and sparsity levels on GSM8K ($N{=}1{,}319$). Points near the $y{=}x$ line indicate reward-accuracy decoupling: despite 4.4$\times$ peak reward gaps (Figure~\ref{fig:training_dynamics}a), GRPO barely moves accuracy ($|\Delta| \leq 1$\,pp for all fine-grained methods at 20--25\%).}
74	    \label{fig:sft_grpo_scatter}
75	\end{figure}
76	
77	Despite the 4.4$\times$ peak reward gap, GRPO barely moves accuracy (Figure~\ref{fig:sft_grpo_scatter}): all fine-grained methods at 20\% sparsity change by $|\Delta| < 1$\,pp (CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \rasp{} $-$0.61\,pp; Table~\ref{tab:decoupling}).
78	We term this \emph{reward-accuracy decoupling}: reward trajectory reflects the model's capacity to learn from RL signal, not downstream accuracy.
79	At 20\% sparsity, the four fine-grained criteria show mean $|\Delta| {=} 0.54$\,pp (max $0.61$\,pp); across the full $\alpha$ dose-response spectrum, $|\Delta|$ remains below $1.14$\,pp.
80	
81	The degree of decoupling varies with sparsity: at 15\%, GRPO slightly amplifies the CKA-only advantage (SFT gap 5.69\,pp $\to$ GRPO gap 7.20\,pp); at 20\%, GRPO adds nothing (gap preserved at 4.55\,pp); at 25\%, Standard's peak reward collapses to 0.008 yet accuracy still changes by only $+$0.99\,pp.
82	Across all four fine-grained criteria at 20\% and 25\%, $|\Delta| < 1$\,pp without exception on GSM8K (Tables~\ref{tab:decoupling},~\ref{tab:cross_sparsity}; Appendix~\ref{sec:appendix_cross_sparsity}); dose-response $\alpha$ variations show slightly larger but still small differences (max $1.14$\,pp at $\alpha{=}2.0$; Table~\ref{tab:alpha}; MATH-500 differences within statistical noise, Appendix~\ref{sec:appendix_math500}).
83	
84	These results are robust across seeds (0.37\,pp range; Appendix~\ref{sec:appendix_multiseed}) and extended training (300 steps, accuracy unchanged; \S\ref{sec:extended_analysis}).
85	The endpoints of the spectrum generalize beyond GSM8K: on MATH-500~\citep{hendrycks2021math}, CKA-only and Standard both rank above \rasp{} and Random in SFT accuracy (27.4\%, 23.4\% vs.\ 21.6\%, 14.4\%), though the CKA-only--Standard gap narrows (4.0\,pp vs.\ 4.62\,pp on GSM8K; Appendix~\ref{sec:appendix_math500})---possibly because MATH-500's higher difficulty compresses all pruned methods toward a floor.
86	On MBPP~\citep{austin2021mbpp} all fine-grained GRPO $|\Delta| < 2$\,pp (Appendix~\ref{sec:appendix_mbpp}).
87	\label{sec:ood}
88	ShortGPT~\citep{shortgpt2024} depth pruning is the sole exception: its GRPO delta is task-dependent ($-$1.36\,pp on GSM8K, $+$4.01\,pp on MBPP; Tables~\ref{tab:decoupling},~\ref{tab:mbpp}), unlike fine-grained methods ($|\Delta| \leq 1.34$\,pp).
89	
90	
91	\subsection{Additional Results}
92	\label{sec:additional_results}
93	
94	\paragraph{Post-SFT accuracy does not predict GRPO outcome.}
95	\label{sec:sft_gradient}
96	Under SFT alone, CKA-only (63.91\%) $>$ \rasp{} (61.49\%) $>$ Standard (59.29\%) $>$ Random (51.25\%), yet under GRPO the \rasp{}/Standard ordering reverses and Random outperforms both in peak reward.
97	The spectrum is driven by structural properties of the pruned architecture, not post-SFT accuracy.
98	
99	\paragraph{Dose-response and sparsity limits.}
100	\label{sec:sparsity_cliff}
101	The CKA coefficient $\alpha$ continuously controls recovery capacity.
102	On GSM8K, recovery follows an inverted-U across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$, peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%) with $|\Delta| \leq 1.14$\,pp at every point; $\alpha{=}1.0$ collapses (peak reward 0.061) while $\alpha{=}4.0$ recovers to 62.77\% (Appendix~\ref{sec:appendix_alpha}).\footnote{$\alpha{=}1.0$ uses \texttt{max\_completion\_length}{$=$}1{,}024; other $\alpha$ values use the TRL default of 512. Since $\alpha{=}1.0$ is the curve minimum, this makes the inverted-U a conservative estimate.}
103	The pattern holds on MATH-500: $\alpha{=}2.0$ GRPO (27.4\%) approaches CKA-only (27.6\%) while $\alpha{=}1.0$ lags at 23.0\% (Table~\ref{tab:math500}).
104	All methods collapse at 30\% sparsity (Appendix~\ref{sec:appendix_sparsity_cliff}); pruning reduces parameters by 19\% and memory by ${\sim}$28\% (Appendix~\ref{sec:appendix_inference}).
105	
106	
107	\subsection{Extended Analysis}
108	\label{sec:extended_analysis}
109	
110	\begin{figure}[t]
111	    \centering
112	    \includegraphics[width=\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}
113	    \caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\mu{=}0.62$) yet recovers best; Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} ($\mu{=}0.88$) preserve dense fidelity but collapse under RL.}
114	    \label{fig:cka_heatmap}
115	\end{figure}
116	
117	\paragraph{Representational diversity.}
118	CKA similarity between dense and pruned representations (Figure~\ref{fig:cka_heatmap}) shows CKA-only diverges most from the dense model ($\mu{=}0.62$), while Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} ($\mu{=}0.88$) cluster near 1.0.
119	Preserving dense fidelity through gradient importance appears to retain redundant representations at the expense of the diversity that GRPO exploration requires.
120	CKA-only concentrates pruning in early layers (L0--9, 72.5\% of removed groups) while Standard prunes uniformly, removing late-layer structures that are representationally unique (Appendix~\ref{sec:appendix_overlap},~\ref{sec:appendix_depth_first}).
121	Gradient flow analysis corroborates this: CKA-only models exhibit 2.89$\times$ mean gradient magnitude versus Standard across 55/56 layer groups ($p{<}0.05$, Wilcoxon; Appendix~\ref{sec:appendix_gradient}), consistent with diversity preservation enabling stronger RL training signals.
122	On MATH-500 (Table~\ref{tab:math500}), CKA-only truncates only 22\% of completions (mean 655 tokens) versus Standard's 44\% (mean 1{,}128 tokens), yet achieves equal or higher accuracy---diversity preserves efficient reasoning rather than redundant chains.
123	
124	\begin{figure}[t]
125	    \centering
126	    \includegraphics[width=\columnwidth]{figures/paper/fig5_extended_training.pdf}
127	    \caption{Extended GRPO training (300 steps, 3$\times$ budget). (a)~Standard reward: zero net gain (0.054$\to$0.056); CKA-only sustains a 5.5$\times$ gap. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}
128	    \label{fig:extended_training}
129	\end{figure}
130	
131	\paragraph{Extended training cannot rescue collapse.}
132	Extending GRPO from 100 to 300 steps (Figure~\ref{fig:extended_training}; Appendix~\ref{sec:appendix_extended}), Standard shows zero net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\times$ gap (0.308 vs 0.056 at step 300). The gap is structural, not a matter of training budget.
133	
134	\paragraph{Cross-scale and cross-architecture generalization.}
135	Both findings generalize to 1.5B scale (Table~\ref{tab:cross_scale}; Appendix~\ref{sec:appendix_cross_scale}) and Qwen2.5-Math-7B (Appendix~\ref{sec:appendix_cross_arch}), where CKA-only recovers from 1.0\% post-prune to 51.50\% vs.\ Standard's 21.00\%.
136	
137	
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "cae6ec16-a445-4be7-941c-d19c500e57f9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Base model and evaluation.}\nWe evaluate on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\\citep{qwen2.5} with GQA~\\citep{ainslie2023gqa} (architecture details in Section~\\ref{sec:prelim}).\nOur primary benchmark is GSM8K~\\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.\nWe report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.\nFor rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).\nThe original unpruned model achieves 90.83\\% on GSM8K (greedy decoding).\n\n\\paragraph{Pruning methods.}\nWe compare four pruning criteria at 20\\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\\sim}$1.45B parameters) with identical per-layer capacity floors (${\\ge}$40\\% retention per layer):\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.\n    \\item \\textbf{Random}: uniform random selection among eligible groups.\n    \\item \\textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\\citep{llmpruner2023}.\n    \\item \\textbf{\\rasp{}} ($\\alpha{=}1.0$): the composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ (Eq.~\\ref{eq:score}), removing structures that are both low-importance and functionally redundant.\n\\end{enumerate}\n\n\\paragraph{Recovery pipeline and hardware.}\nAll four methods undergo matched two-stage recovery.\nStage~1 (SFT warmup): 2 epochs on 7{,}473 GSM8K chain-of-thought examples with teacher forcing (37 minutes), restoring EOS generation and basic format compliance.\nStage~2 (GRPO): Group Relative Policy Optimization~\\citep{shao2024grpo} with learning rate $1{\\times}10^{-6}$, maximum completion length 1{,}024 tokens, KL penalty coefficient $\\beta{=}0.01$, sampling temperature 0.4, DAPO-style clipped loss, and binary reward ($r{=}1$ if correct, $r{=}0$ otherwise), trained for 100 steps on 1{,}000 GSM8K training problems.\nAll methods use identical GRPO configuration with \\texttt{max\\_completion\\_length}{$=$}1{,}024, except Random which uses the TRL default of 512 tokens (Table~\\ref{tab:hyperparams}; Appendix~\\ref{sec:appendix_training}), making it a conservative comparison point.\nSeeds vary at the GRPO stage; pruning calibration and SFT use identical configurations across all methods.\nWe repeat GRPO training with 3 random seeds for CKA-only, Standard, and Random (Table~\\ref{tab:decoupling}).\nCKA-only achieves 64.39\\% $\\pm$ 0.19\\,pp (std across seeds), Standard 59.84\\% $\\pm$ 0.38\\,pp; the 4.55\\,pp gap is robust across seeds (Welch's $t$-test, $p{=}0.0009$, Cohen's $d{=}11.1$; 95\\% CI for mean difference: $[3.62, 5.47]$\\,pp), confirming that recovery capacity differences are structural rather than stochastic (per-seed results in Appendix~\\ref{sec:appendix_seed}).\nAll experiments run on 2$\\times$ NVIDIA RTX PRO 6000 GPUs (94\\,GB VRAM each); pruning variants are trained in parallel on separate GPUs under identical wall-clock conditions.\n\n\n\\subsection{Recovery Capacity Spectrum}\n\\label{sec:recovery_gradient}\n\n\\input{tables/tab1_recovery_gradient}\n\n\\begin{figure*}[t]\n    \\centering\n    \\begin{minipage}[t]{0.38\\textwidth}\n        \\centering\n        \\includegraphics[width=\\textwidth]{figures/paper/fig2_reward_trajectories.pdf}\n        \\centerline{\\small (a) Reward trajectories}\n    \\end{minipage}\n    \\hfill\n    \\begin{minipage}[t]{0.58\\textwidth}\n        \\centering\n        \\includegraphics[width=\\textwidth]{figures/paper/fig3_collapse_dynamics.pdf}\n        \\centerline{\\small (b) $f_0$ and gradient norm diagnostics}\n    \\end{minipage}\n    \\caption{GRPO training dynamics for four pruning criteria (100 steps, $\\beta{=}0.01$, $T{=}0.4$). (a)~Reward: CKA-only reaches 0.354 peak; Random oscillates (0.14--0.19); Standard peaks at 0.081; \\rasp{} collapses to 0.010. (b)~Left: $f_0$ (zero-variance batch fraction)---CKA-only stays below 0.35 while Standard and \\rasp{} remain in the collapse zone ($f_0 > 0.5$). Right: gradient norm---\\rasp{} norms near zero throughout; Standard shows a transient minimum at step 90.}\n    \\label{fig:training_dynamics}\n\\end{figure*}\n\nUnder GRPO training, the four pruning criteria produce a clear recovery capacity spectrum: CKA-only $\\gg$ Random $\\gg$ Standard $>$ \\rasp{} $\\alpha{=}1.0$ (Table~\\ref{tab:recovery_gradient}, Figure~\\ref{fig:training_dynamics}).\nThe pruning criterion, not training configuration, determines whether the model learns, stagnates, or collapses.\n\nAmong these configurations, only the diversity-maximizing criterion (CKA-only) produces active learning: peak reward 0.354 with $f_0$ as low as 0.125 (Figure~\\ref{fig:training_dynamics}b).\nRandom stagnates (reward 0.14--0.19, min $f_0 = 0.300$); Standard exhibits borderline collapse ($f_0 \\geq 0.50$, peak reward 0.081); \\rasp{} at $\\alpha{=}1.0$ collapses ($f_0 \\geq 0.675$, reward declining to 0.010, with near-zero KL divergence indicating minimal policy movement; Appendix~\\ref{sec:appendix_kl}).\nThe dose-response (\\S\\ref{sec:sparsity_cliff}) confirms CKA weight as the critical variable: increasing $\\alpha$ from 1.0 to 2.0 shifts \\rasp{} from collapse to peak recovery (66.11\\% vs.\\ 64.39\\% for CKA-only on GSM8K).\n\n\n\\subsection{Reward-Accuracy Decoupling}\n\\label{sec:decoupling}\n\n\\input{tables/tab2_decoupling}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig_sft_grpo_scatter.pdf}\n    \\caption{SFT vs GRPO accuracy across all pruning criteria and sparsity levels on GSM8K ($N{=}1{,}319$). Points near the $y{=}x$ line indicate reward-accuracy decoupling: despite 4.4$\\times$ peak reward gaps (Figure~\\ref{fig:training_dynamics}a), GRPO barely moves accuracy ($|\\Delta| \\leq 1$\\,pp for all fine-grained methods at 20--25\\%).}\n    \\label{fig:sft_grpo_scatter}\n\\end{figure}\n\nDespite the 4.4$\\times$ peak reward gap, GRPO barely moves accuracy (Figure~\\ref{fig:sft_grpo_scatter}): all fine-grained methods at 20\\% sparsity change by $|\\Delta| < 1$\\,pp (CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \\rasp{} $-$0.61\\,pp; Table~\\ref{tab:decoupling}).\nWe term this \\emph{reward-accuracy decoupling}: reward trajectory reflects the model's capacity to learn from RL signal, not downstream accuracy.\nAt 20\\% sparsity, the four fine-grained criteria show mean $|\\Delta| {=} 0.54$\\,pp (max $0.61$\\,pp); across the full $\\alpha$ dose-response spectrum, $|\\Delta|$ remains below $1.14$\\,pp.\n\nThe degree of decoupling varies with sparsity: at 15\\%, GRPO slightly amplifies the CKA-only advantage (SFT gap 5.69\\,pp $\\to$ GRPO gap 7.20\\,pp); at 20\\%, GRPO adds nothing (gap preserved at 4.55\\,pp); at 25\\%, Standard's peak reward collapses to 0.008 yet accuracy still changes by only $+$0.99\\,pp.\nAcross all four fine-grained criteria at 20\\% and 25\\%, $|\\Delta| < 1$\\,pp without exception on GSM8K (Tables~\\ref{tab:decoupling},~\\ref{tab:cross_sparsity}; Appendix~\\ref{sec:appendix_cross_sparsity}); dose-response $\\alpha$ variations show slightly larger but still small differences (max $1.14$\\,pp at $\\alpha{=}2.0$; Table~\\ref{tab:alpha}; MATH-500 differences within statistical noise, Appendix~\\ref{sec:appendix_math500}).\n\nThese results are robust across seeds (0.37\\,pp range; Appendix~\\ref{sec:appendix_multiseed}) and extended training (300 steps, accuracy unchanged; \\S\\ref{sec:extended_analysis}).\nThe endpoints of the spectrum generalize beyond GSM8K: on MATH-500~\\citep{hendrycks2021math}, CKA-only and Standard both rank above \\rasp{} and Random in SFT accuracy (27.4\\%, 23.4\\% vs.\\ 21.6\\%, 14.4\\%), though the CKA-only--Standard gap narrows (4.0\\,pp vs.\\ 4.62\\,pp on GSM8K; Appendix~\\ref{sec:appendix_math500})---possibly because MATH-500's higher difficulty compresses all pruned methods toward a floor.\nOn MBPP~\\citep{austin2021mbpp} all fine-grained GRPO $|\\Delta| < 2$\\,pp (Appendix~\\ref{sec:appendix_mbpp}).\n\\label{sec:ood}\nShortGPT~\\citep{shortgpt2024} depth pruning is the sole exception: its GRPO delta is task-dependent ($-$1.36\\,pp on GSM8K, $+$4.01\\,pp on MBPP; Tables~\\ref{tab:decoupling},~\\ref{tab:mbpp}), unlike fine-grained methods ($|\\Delta| \\leq 1.34$\\,pp).\n\n\n\\subsection{Additional Results}\n\\label{sec:additional_results}\n\n\\paragraph{Post-SFT accuracy does not predict GRPO outcome.}\n\\label{sec:sft_gradient}\nUnder SFT alone, CKA-only (63.91\\%) $>$ \\rasp{} (61.49\\%) $>$ Standard (59.29\\%) $>$ Random (51.25\\%), yet under GRPO the \\rasp{}/Standard ordering reverses and Random outperforms both in peak reward.\nThe spectrum is driven by structural properties of the pruned architecture, not post-SFT accuracy.\n\n\\paragraph{Dose-response and sparsity limits.}\n\\label{sec:sparsity_cliff}\nThe CKA coefficient $\\alpha$ continuously controls recovery capacity.\nOn GSM8K, recovery follows an inverted-U across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$, peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%) with $|\\Delta| \\leq 1.14$\\,pp at every point; $\\alpha{=}1.0$ collapses (peak reward 0.061) while $\\alpha{=}4.0$ recovers to 62.77\\% (Appendix~\\ref{sec:appendix_alpha}).\\footnote{$\\alpha{=}1.0$ uses \\texttt{max\\_completion\\_length}{$=$}1{,}024; other $\\alpha$ values use the TRL default of 512. Since $\\alpha{=}1.0$ is the curve minimum, this makes the inverted-U a conservative estimate.}\nThe pattern holds on MATH-500: $\\alpha{=}2.0$ GRPO (27.4\\%) approaches CKA-only (27.6\\%) while $\\alpha{=}1.0$ lags at 23.0\\% (Table~\\ref{tab:math500}).\nAll methods collapse at 30\\% sparsity (Appendix~\\ref{sec:appendix_sparsity_cliff}); pruning reduces parameters by 19\\% and memory by ${\\sim}$28\\% (Appendix~\\ref{sec:appendix_inference}).\n\n\n\\subsection{Extended Analysis}\n\\label{sec:extended_analysis}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}\n    \\caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\\mu{=}0.62$) yet recovers best; Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} ($\\mu{=}0.88$) preserve dense fidelity but collapse under RL.}\n    \\label{fig:cka_heatmap}\n\\end{figure}\n\n\\paragraph{Representational diversity.}\nCKA similarity between dense and pruned representations (Figure~\\ref{fig:cka_heatmap}) shows CKA-only diverges most from the dense model ($\\mu{=}0.62$), while Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} ($\\mu{=}0.88$) cluster near 1.0.\nPreserving dense fidelity through gradient importance appears to retain redundant representations at the expense of the diversity that GRPO exploration requires.\nCKA-only concentrates pruning in early layers (L0--9, 72.5\\% of removed groups) while Standard prunes uniformly, removing late-layer structures that are representationally unique (Appendix~\\ref{sec:appendix_overlap},~\\ref{sec:appendix_depth_first}).\nGradient flow analysis corroborates this: CKA-only models exhibit 2.89$\\times$ mean gradient magnitude versus Standard across 55/56 layer groups ($p{<}0.05$, Wilcoxon; Appendix~\\ref{sec:appendix_gradient}), consistent with diversity preservation enabling stronger RL training signals.\nOn MATH-500 (Table~\\ref{tab:math500}), CKA-only truncates only 22\\% of completions (mean 655 tokens) versus Standard's 44\\% (mean 1{,}128 tokens), yet achieves equal or higher accuracy---diversity preserves efficient reasoning rather than redundant chains.\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig5_extended_training.pdf}\n    \\caption{Extended GRPO training (300 steps, 3$\\times$ budget). (a)~Standard reward: zero net gain (0.054$\\to$0.056); CKA-only sustains a 5.5$\\times$ gap. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}\n    \\label{fig:extended_training}\n\\end{figure}\n\n\\paragraph{Extended training cannot rescue collapse.}\nExtending GRPO from 100 to 300 steps (Figure~\\ref{fig:extended_training}; Appendix~\\ref{sec:appendix_extended}), Standard shows zero net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\\times$ gap (0.308 vs 0.056 at step 300). The gap is structural, not a matter of training budget.\n\n\\paragraph{Cross-scale and cross-architecture generalization.}\nBoth findings generalize to 1.5B scale (Table~\\ref{tab:cross_scale}; Appendix~\\ref{sec:appendix_cross_scale}) and Qwen2.5-Math-7B (Appendix~\\ref{sec:appendix_cross_arch}), where CKA-only recovers from 1.0\\% post-prune to 51.50\\% vs.\\ Standard's 21.00\\%.\n\n\n",
      "numLines": 138,
      "startLine": 1,
      "totalLines": 138
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01QNqeG4D6sVyjRnyoteP3cH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "ee5e70b2-d061-45c8-a693-0be73c04385c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6CNKSYbFdRRCbPQyJEkjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 416,
      "cache_read_input_tokens": 24463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 416
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

_source line 10 · 2026-05-24T07:15:47.126Z_

<details><summary>↩ Tool result · `toolu_01QNqeG4D6sVyjRnyoteP3cH`</summary>

```text
1	\section{Training Details}
2	\label{sec:appendix_training}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\caption{Hyperparameter details for SFT warmup and GRPO recovery stages. All methods share the same GRPO configuration; Random uses the TRL default generation limit (marked with $^\dagger$).}
8	\label{tab:hyperparams}
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{@{}lll@{}}
11	\toprule
12	Parameter & SFT & GRPO \\
13	\midrule
14	Learning rate & $2 \times 10^{-5}$ & $1 \times 10^{-6}$ \\
15	Batch size & 1 & 1 \\
16	Gradient accumulation & 8 & 1 \\
17	Max sequence length & 2{,}048 & -- \\
18	Max new tokens & -- & 1{,}024\,$^\dagger$512 \\
19	Optimizer & AdamW & AdamW \\
20	Epochs / Steps & 2 epochs & 100 steps \\
21	KL coefficient $\beta$ & -- & 0.01 \\
22	Sampling temperature & -- & 0.4 \\
23	Num generations per prompt & -- & 8 \\
24	Reward & -- & Binary (exact match) \\
25	Loss formulation & Cross-entropy & DAPO-style clipped \\
26	\texttt{reward\_desert\_patience} & -- & 50 \\
27	\bottomrule
28	\multicolumn{3}{l}{\footnotesize $^\dagger$Random uses TRL default of 512 tokens; all other methods use 1{,}024.} \\
29	\end{tabular}}
30	\end{table}
31	
32	\section{Algorithm}
33	\label{sec:appendix_algo}
34	
35	\begin{algorithm}[h]
36	\caption{Controlled Pruning Comparison Framework}
37	\label{alg:rasp}
38	\begin{algorithmic}[1]
39	\Require Model $\mathcal{M}$, calibration data $\mathcal{D}_\text{cal}$, target sparsity $s$, scoring criterion $\mathcal{C} \in \{\text{Std}, \text{RASP}, \text{CKA}, \text{Rand}\}$, layer floor $\tau$
40	\Ensure Pruned and recovered model $\mathcal{M}'$
41	\Statex \textit{\% Stage 1: Shared Structural Analysis}
42	\For{each structure $h \in \mathcal{H}$}
43	    \State Compute importance $I(h)$ via Eq.~\eqref{eq:importance}
44	    \State Collect activations $\mathbf{X}_h$ on $\mathcal{D}_\text{cal}$
45	\EndFor
46	\For{each layer $\ell = 1, \ldots, L$}
47	    \For{each structure $h_i$ in layer $\ell$}
48	        \State $F(h_i) \gets \frac{1}{|\mathcal{H}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{h_i}, \mathbf{X}_{h_j})$
49	    \EndFor
50	\EndFor
51	\Statex \textit{\% Stage 2: Criterion-Specific Scoring}
52	\For{each structure $h \in \mathcal{H}$}
53	    \State $S(h) \gets \mathcal{C}(I(h), F(h))$ \hfill $\triangleright$ Eq.~\ref{eq:standard}, \ref{eq:score}, \ref{eq:cka_only}, or random
54	\EndFor
55	\State Sort $\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\tau$
56	\Statex \textit{\% Stage 3: Two-Stage Recovery}
57	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
58	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ recover reasoning
59	\State \Return $\mathcal{M}'$
60	\end{algorithmic}
61	\end{algorithm}
62	
63	\section{Inference Efficiency}
64	\label{sec:appendix_inference}
65	
66	\begin{table}[h]
67	\centering
68	\small
69	\caption{Inference characteristics at 20\% sparsity (single-GPU, no contention). Pruning reduces parameters by 19\% and memory by ${\sim}$28\%, with TTFT improving 18\%. Per-token throughput decreases 19\% (0.81$\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}
70	\label{tab:inference}
71	\resizebox{\columnwidth}{!}{%
72	\begin{tabular}{@{}lcccc@{}}
73	\toprule
74	Configuration & TPS\,(tok/s) & TTFT\,(ms) & Per-token\,(ms) & Params\,(B) \\
75	\midrule
76	Dense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\
77	CKA-only 20\% & 58.3 & 16.4 & 16.7 & 6.16 \\
78	Standard 20\% & 58.2 & 16.4 & 16.7 & 6.16 \\
79	\bottomrule
80	\end{tabular}}
81	\end{table}
82	
83	All pruned models achieve ${\sim}$28\% memory reduction from structural parameter removal.
84	TTFT (time to first token) improves by 18\% (20.1$\to$16.4\,ms), reflecting faster prefill with fewer parameters.
85	Per-token throughput decreases by 19\% (72.0$\to$58.3 tok/s, or 13.9$\to$16.7\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.
86	CKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.
87	
88	\section{CKA Coefficient $\alpha$ Ablation}
89	\label{sec:appendix_alpha}
90	
91	\input{tables/table3_alpha}
92	
93	On GSM8K, the dose-response curve across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U pattern peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%, $\Delta{=}{+}1.14$\,pp; Table~\ref{tab:alpha}).
94	At $\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\%, GRPO 61.18\%).
95	At $\alpha{=}1.0$ (\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\%, $\Delta{=}{-}0.61$\,pp).
96	$\alpha{=}3.0$ (SFT 64.14\%, GRPO 63.46\%, $\Delta{=}{-}0.68$\,pp) excludes a plateau hypothesis: accuracy drops 2.65\,pp from the $\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.
97	At $\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\% GRPO accuracy (SFT 61.94\%, $\Delta{=}{+}0.83$\,pp) with active GRPO learning (reward 0.146$\to$0.256$\to$0.198).
98	Reward-accuracy decoupling holds at every $\alpha$ value: $|\Delta| \leq 1.14$\,pp across all five points.
99	
100	\section{Extended Training Dynamics}
101	\label{sec:appendix_extended}
102	
103	See Figure~\ref{fig:extended_training} in the main text for the 300-step extended training results.
104	
105	\section{MATH-500 Out-of-Distribution Evaluation}
106	\label{sec:appendix_math500}
107	
108	\input{tables/tab_math500}
109	
110	CKA-only and Standard both outperform \rasp{} and Random on MATH-500 (SFT: 27.4\%, 23.4\% vs.\ 21.6\%, 14.4\%; GRPO: 27.6\%, 27.0\% vs.\ 23.0\%, 13.4\%), consistent with GSM8K.
111	However, the CKA-only--Standard gap narrows substantially: from 4.6\,pp (GSM8K SFT) to 4.0\,pp (MATH-500 SFT) to 0.6\,pp (MATH-500 GRPO).
112	Middle-ranked methods also swap positions (Standard $>$ \rasp{} on MATH-500 vs.\ \rasp{} $>$ Standard on GSM8K).
113	This is consistent with MATH-500's higher difficulty compressing all pruned methods toward a capability floor, reducing inter-method differentiation (\S\ref{sec:ood}).
114	CKA-only also produces more efficient reasoning: only 22\% of completions are truncated at the 2{,}048-token limit (mean 655 tokens) versus Standard's 44\% (mean 1{,}128 tokens), indicating that the preserved structure enables shorter reasoning chains rather than longer ones.
115	The $\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\sim}$8\,pp across $\alpha$ values, but with stderr ${\approx}$2\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.
116	The inverted-U pattern is validated on GSM8K (Table~\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.
117	
118	\section{MBPP Code Generation}
119	\label{sec:appendix_mbpp}
120	
121	\input{tables/tab_mbpp}
122	
123	MBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\approx}1.7$\,pp).
124	This directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.
125	
126	\section{CKA Scoring Stability}
127	\label{sec:appendix_cka_stability}
128	
129	\input{tables/tab_cka_stability}
130	
131	CKA-based structure rankings are highly stable across calibration data volumes: Spearman $\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.
132	
133	\section{Gradient Signal Analysis}
134	\label{sec:appendix_gradient}
135	
136	We compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.
137	
138	\begin{table}[h]
139	\centering
140	\small
141	\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}
142	\label{tab:gradient_flow}
143	\begin{tabular}{@{}lcc@{}}
144	\toprule
145	Comparison & Gradient Ratio & Sig.\ Layers \\
146	\midrule
147	CKA-only vs Standard & 2.89$\times$ & 55\,/\,56 \\
148	CKA-only vs \rasp{} & 2.26$\times$ & 56\,/\,56 \\
149	\rasp{} vs Standard & 1.28$\times$ & 45\,/\,56 \\
150	\bottomrule
151	\end{tabular}
152	\end{table}
153	
154	The gradient magnitude hierarchy (CKA-only $\gg$ \rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\% $>$ 60.88\% $>$ 59.84\%), with bootstrap 95\% CIs for all ratios excluding 1.0.
155	This is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.
156	
157	\section{Seed Reproducibility}
158	\label{sec:appendix_seed}
159	
160	CKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\% (seed 42), 64.22\% (seed 123), 64.59\% (seed 456), yielding mean 64.39\% $\pm$ 0.19\,pp.
161	Standard: mean 59.84\% $\pm$ 0.38\,pp across the same 3 seeds.
162	See Table~\ref{tab:multiseed} for the full summary.
163	
164	\section{Sparsity Cliff at 30\%}
165	\label{sec:appendix_sparsity_cliff}
166	
167	\input{tables/table4_sparsity_cliff}
168	
169	All tested methods collapse at 30\% sparsity: Standard retains 4\% accuracy, CKA-only 1.6\%, and \rasp{} 0\%.
170	This capacity threshold, independent of pruning criterion, validates 20\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.
171	
172	\section{Multi-Seed GRPO Results}
173	\label{sec:appendix_multiseed}
174	
175	\begin{table}[h]
176	\centering
177	\small
178	\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}
179	\label{tab:multiseed}
180	\begin{tabular}{@{}llccc@{}}
181	\toprule
182	Sparsity & Method & Mean Acc.\,(\%) & Std\,(pp) & Seeds \\
183	\midrule
184	\multirow{4}{*}{20\%} & CKA-only & 64.39 & 0.19 & 3 \\
185	 & Standard & 59.84 & 0.38 & 3 \\
186	 & \rasp{} & 60.88 & -- & 1 \\
187	 & Random & 50.72 & 0.15 & 3 \\
188	\midrule
189	\multirow{2}{*}{15\%} & CKA-only & 72.76 & 0.57 & 3 \\
190	 & Standard & 65.56 & 0.50 & 3 \\
191	\bottomrule
192	\end{tabular}
193	\end{table}
194	
195	At 20\% sparsity, the 4.55\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.59\%, Standard: 59.44--60.20\%).
196	Standard shows a wider observed range across seeds (0.76\,pp vs 0.37\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.
197	Random (3 seeds: 50.57\%, 50.72\%, 50.87\%; $\sigma{=}0.15$\,pp, observed range 0.30\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\%.
198	All three seeds satisfy GRPO $\leq$ SFT ($\Delta{=}{-}0.68$, $-$0.53, $-$0.38\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.
199	Note: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\% vs.\ 59.29\% for seeds 123/456; $\Delta = 0.08$\,pp).
200	At 15\% sparsity, the gap widens to 7.20\,pp (72.76\% vs 65.56\%, $t{\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\%, Standard: 65.13--65.43\%).
201	
202	\section{Cross-Sparsity Validation}
203	\label{sec:appendix_cross_sparsity}
204	
205	\begin{table}[h]
206	\centering
207	\small
208	\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\% and 20\% GRPO values are mean over 3 seeds (see Tables~\ref{tab:decoupling},~\ref{tab:multiseed}). $^\ddagger$Single seed. Mean $|\Delta| \leq 1$\,pp across all conditions.}
209	\label{tab:cross_sparsity}
210	\begin{tabular}{@{}llccc@{}}
211	\toprule
212	Sparsity & Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
213	\midrule
214	\multirow{2}{*}{15\%} & CKA-only & 72.18 & \textbf{72.76{\scriptsize$\pm$0.57}} & $+$0.58 \\
215	 & Standard & 66.49 & 65.56{\scriptsize$\pm$0.50} & $-$0.93 \\
216	\midrule
217	\multirow{2}{*}{20\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\
218	 & Standard & 59.29 & 59.84 & $+$0.55 \\
219	\midrule
220	\multirow{2}{*}{25\%$^\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\
221	 & Standard & 50.87 & 51.86 & $+$0.99 \\
222	\midrule
223	30\% & All & \multicolumn{3}{c}{Collapse ($\leq$4\%; Table~\ref{tab:sparsity_cliff})} \\
224	\bottomrule
225	\end{tabular}
226	\end{table}
227	
228	At 15\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\,pp (72.76\% vs 65.56\%), compared to $+$4.55\,pp at 20\%.
229	CKA-only at 15\% (72.76\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\% of original dense model performance (90.83\%).
230	At 25\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\,pp from 15\%$\to$20\%, $-$8.42\,pp from 20\%$\to$25\%), while CKA-only's decline decelerates ($-$8.27\,pp then $-$3.79\,pp).
231	Reward-accuracy decoupling is preserved ($|\Delta| \leq 1$\,pp for both methods) despite Standard's near-zero peak reward (0.008).
232	
233	\section{Cross-Scale Validation}
234	\label{sec:appendix_cross_scale}
235	
236	\input{tables/tab5_cross_scale}
237	
238	On DeepSeek-R1-Distill-Qwen-1.5B at 20\% sparsity, the three-method ordering is preserved (CKA-only 35.48\% $\gg$ \rasp{} 26.16\% $>$ Standard 22.29\%), with reward-accuracy decoupling confirmed at this scale ($|\Delta| < 1$\,pp: CKA-only $-$0.15, Standard $-$0.61\,pp).
239	
240	\section{Cross-Architecture Validation}
241	\label{sec:appendix_cross_arch}
242	
243	\begin{table}[h]
244	\centering
245	\small
246	\caption{Cross-architecture validation on Qwen2.5-Math-7B~\citep{qwen2.5} at 20\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports accuracy $\pm$ binomial standard error ($N{=}200$). EOS rate: fraction of generations that produce a valid end-of-sequence token.}
247	\label{tab:cross_arch}
248	\resizebox{\columnwidth}{!}{%
249	\begin{tabular}{@{}lccc@{}}
250	\toprule
251	Method & Post-Prune\,(\%) & Post-SFT\,(\%) & EOS Rate\,(\%) \\
252	\midrule
253	CKA-only & 1.0 & \textbf{51.50 $\pm$ 3.53} & 27.0 \\
254	Standard & 18.5 & 21.00 $\pm$ 2.88 & 36.5 \\
255	\bottomrule
256	\end{tabular}}
257	\end{table}
258	
259	CKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\% post-prune accuracy vs Standard's 18.5\%), yet SFT recovers CKA-only to 51.50\% while Standard remains at 21.00\%.
260	This post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.
261	EOS rates remain below 40\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\footnote{Preliminary GRPO evaluation yields 48.60\% (243/500), but 83.8\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}
262	
263	\section{Structural Overlap Analysis}
264	\label{sec:appendix_overlap}
265	
266	CKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity.
267	CKA-only concentrates pruning in early layers (L0--9 account for 72.5\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).
268	Standard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).
269	
270	The methods share only partial overlap in which structures they remove.
271	65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.
272	Conversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.
273	
274	This pattern is consistent with the layer-wise CKA similarity analysis (Figure~\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.
275	
276	\section{KL Divergence During GRPO Training}
277	\label{sec:appendix_kl}
278	
279	\begin{figure}[t]
280	    \centering
281	    \includegraphics[width=0.75\columnwidth]{figures/paper/fig_appendix_kl.pdf}
282	    \caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}
283	    \label{fig:kl_divergence}
284	\end{figure}
285	
286	\section{Depth-First Pruning Baseline}
287	\label{sec:appendix_depth_first}
288	
289	As a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\% sparsity.
290	Both SFT (${\sim}$10\%) and GRPO (${\sim}$8\%) accuracy are near chance (early-stopped at $N{\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.
291	This baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.
292	
293	\section{Per-Layer Capacity Floor Ablation}
294	\label{sec:appendix_floor}
295	
296	\begin{table}[h]
297	\centering
298	\small
299	\caption{Effect of per-layer capacity floor $\tau$ on CKA-only pruning at 20\% sparsity. GSM8K accuracy ($N{=}1{,}319$) after GRPO recovery (100 steps). Default $\tau{=}0.4$.}
300	\label{tab:floor_ablation}
301	\begin{tabular}{@{}lcc@{}}
302	\toprule
303	Floor $\tau$ & GRPO Acc.\,(\%) & $\Delta$ vs $\tau{=}0.4$\,(pp) \\
304	\midrule
305	0.3 & 65.05 & $+$0.68 \\
306	0.4 (default) & 64.37 & --- \\
307	0.5 & 61.71 & $-$2.66 \\
308	0.6 & 62.02 & $-$2.35 \\
309	\bottomrule
310	\end{tabular}
311	\end{table}
312	
313	The per-layer capacity floor $\tau$ sets the minimum fraction of MLP channel groups retained in each layer, preventing over-pruning of any single layer regardless of its importance score.
314	We ablate $\tau \in \{0.3, 0.4, 0.5, 0.6\}$ using CKA-only pruning at 20\% sparsity.
315	Lowering $\tau$ to 0.3 slightly improves accuracy ($+$0.68\,pp), while raising it to 0.5 or 0.6 causes a notable drop ($-$2.66 and $-$2.35\,pp respectively; the difference between 0.5 and 0.6 is not significant at 0.31\,pp $\ll$ stderr $\approx$ 1.3\,pp).
316	Over-constraining per-layer retention hurts global pruning quality by forcing removal of important structures in unconstrained layers.
317	
318	\section{Use of AI Assistants}
319	\label{sec:appendix_ai_assistants}
320	
321	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
322	\begin{itemize}[nosep,leftmargin=*]
323	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
324	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
325	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
326	\end{itemize}
327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "2fb4fe51-6f89-4f98-97e2-78db6fd526a3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "content": "\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Hyperparameter details for SFT warmup and GRPO recovery stages. All methods share the same GRPO configuration; Random uses the TRL default generation limit (marked with $^\\dagger$).}\n\\label{tab:hyperparams}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll@{}}\n\\toprule\nParameter & SFT & GRPO \\\\\n\\midrule\nLearning rate & $2 \\times 10^{-5}$ & $1 \\times 10^{-6}$ \\\\\nBatch size & 1 & 1 \\\\\nGradient accumulation & 8 & 1 \\\\\nMax sequence length & 2{,}048 & -- \\\\\nMax new tokens & -- & 1{,}024\\,$^\\dagger$512 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs / Steps & 2 epochs & 100 steps \\\\\nKL coefficient $\\beta$ & -- & 0.01 \\\\\nSampling temperature & -- & 0.4 \\\\\nNum generations per prompt & -- & 8 \\\\\nReward & -- & Binary (exact match) \\\\\nLoss formulation & Cross-entropy & DAPO-style clipped \\\\\n\\texttt{reward\\_desert\\_patience} & -- & 50 \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize $^\\dagger$Random uses TRL default of 512 tokens; all other methods use 1{,}024.} \\\\\n\\end{tabular}}\n\\end{table}\n\n\\section{Algorithm}\n\\label{sec:appendix_algo}\n\n\\begin{algorithm}[h]\n\\caption{Controlled Pruning Comparison Framework}\n\\label{alg:rasp}\n\\begin{algorithmic}[1]\n\\Require Model $\\mathcal{M}$, calibration data $\\mathcal{D}_\\text{cal}$, target sparsity $s$, scoring criterion $\\mathcal{C} \\in \\{\\text{Std}, \\text{RASP}, \\text{CKA}, \\text{Rand}\\}$, layer floor $\\tau$\n\\Ensure Pruned and recovered model $\\mathcal{M}'$\n\\Statex \\textit{\\% Stage 1: Shared Structural Analysis}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State Compute importance $I(h)$ via Eq.~\\eqref{eq:importance}\n    \\State Collect activations $\\mathbf{X}_h$ on $\\mathcal{D}_\\text{cal}$\n\\EndFor\n\\For{each layer $\\ell = 1, \\ldots, L$}\n    \\For{each structure $h_i$ in layer $\\ell$}\n        \\State $F(h_i) \\gets \\frac{1}{|\\mathcal{H}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{h_i}, \\mathbf{X}_{h_j})$\n    \\EndFor\n\\EndFor\n\\Statex \\textit{\\% Stage 2: Criterion-Specific Scoring}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State $S(h) \\gets \\mathcal{C}(I(h), F(h))$ \\hfill $\\triangleright$ Eq.~\\ref{eq:standard}, \\ref{eq:score}, \\ref{eq:cka_only}, or random\n\\EndFor\n\\State Sort $\\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\\tau$\n\\Statex \\textit{\\% Stage 3: Two-Stage Recovery}\n\\State $\\mathcal{M}_\\text{warm} \\gets \\text{SFT}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{sft})$ \\hfill $\\triangleright$ restore EOS \\& format\n\\State $\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{warm}, \\mathcal{D}_\\text{rlvr})$ \\hfill $\\triangleright$ recover reasoning\n\\State \\Return $\\mathcal{M}'$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\section{Inference Efficiency}\n\\label{sec:appendix_inference}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Inference characteristics at 20\\% sparsity (single-GPU, no contention). Pruning reduces parameters by 19\\% and memory by ${\\sim}$28\\%, with TTFT improving 18\\%. Per-token throughput decreases 19\\% (0.81$\\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}\n\\label{tab:inference}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & TPS\\,(tok/s) & TTFT\\,(ms) & Per-token\\,(ms) & Params\\,(B) \\\\\n\\midrule\nDense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\\\\nCKA-only 20\\% & 58.3 & 16.4 & 16.7 & 6.16 \\\\\nStandard 20\\% & 58.2 & 16.4 & 16.7 & 6.16 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll pruned models achieve ${\\sim}$28\\% memory reduction from structural parameter removal.\nTTFT (time to first token) improves by 18\\% (20.1$\\to$16.4\\,ms), reflecting faster prefill with fewer parameters.\nPer-token throughput decreases by 19\\% (72.0$\\to$58.3 tok/s, or 13.9$\\to$16.7\\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.\nCKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.\n\n\\section{CKA Coefficient $\\alpha$ Ablation}\n\\label{sec:appendix_alpha}\n\n\\input{tables/table3_alpha}\n\nOn GSM8K, the dose-response curve across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U pattern peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%, $\\Delta{=}{+}1.14$\\,pp; Table~\\ref{tab:alpha}).\nAt $\\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\\%, GRPO 61.18\\%).\nAt $\\alpha{=}1.0$ (\\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\\%, $\\Delta{=}{-}0.61$\\,pp).\n$\\alpha{=}3.0$ (SFT 64.14\\%, GRPO 63.46\\%, $\\Delta{=}{-}0.68$\\,pp) excludes a plateau hypothesis: accuracy drops 2.65\\,pp from the $\\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.\nAt $\\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\\% GRPO accuracy (SFT 61.94\\%, $\\Delta{=}{+}0.83$\\,pp) with active GRPO learning (reward 0.146$\\to$0.256$\\to$0.198).\nReward-accuracy decoupling holds at every $\\alpha$ value: $|\\Delta| \\leq 1.14$\\,pp across all five points.\n\n\\section{Extended Training Dynamics}\n\\label{sec:appendix_extended}\n\nSee Figure~\\ref{fig:extended_training} in the main text for the 300-step extended training results.\n\n\\section{MATH-500 Out-of-Distribution Evaluation}\n\\label{sec:appendix_math500}\n\n\\input{tables/tab_math500}\n\nCKA-only and Standard both outperform \\rasp{} and Random on MATH-500 (SFT: 27.4\\%, 23.4\\% vs.\\ 21.6\\%, 14.4\\%; GRPO: 27.6\\%, 27.0\\% vs.\\ 23.0\\%, 13.4\\%), consistent with GSM8K.\nHowever, the CKA-only--Standard gap narrows substantially: from 4.6\\,pp (GSM8K SFT) to 4.0\\,pp (MATH-500 SFT) to 0.6\\,pp (MATH-500 GRPO).\nMiddle-ranked methods also swap positions (Standard $>$ \\rasp{} on MATH-500 vs.\\ \\rasp{} $>$ Standard on GSM8K).\nThis is consistent with MATH-500's higher difficulty compressing all pruned methods toward a capability floor, reducing inter-method differentiation (\\S\\ref{sec:ood}).\nCKA-only also produces more efficient reasoning: only 22\\% of completions are truncated at the 2{,}048-token limit (mean 655 tokens) versus Standard's 44\\% (mean 1{,}128 tokens), indicating that the preserved structure enables shorter reasoning chains rather than longer ones.\nThe $\\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\\sim}$8\\,pp across $\\alpha$ values, but with stderr ${\\approx}$2\\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.\nThe inverted-U pattern is validated on GSM8K (Table~\\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.\n\n\\section{MBPP Code Generation}\n\\label{sec:appendix_mbpp}\n\n\\input{tables/tab_mbpp}\n\nMBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\\approx}1.7$\\,pp).\nThis directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.\n\n\\section{CKA Scoring Stability}\n\\label{sec:appendix_cka_stability}\n\n\\input{tables/tab_cka_stability}\n\nCKA-based structure rankings are highly stable across calibration data volumes: Spearman $\\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.\n\n\\section{Gradient Signal Analysis}\n\\label{sec:appendix_gradient}\n\nWe compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}\n\\label{tab:gradient_flow}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nComparison & Gradient Ratio & Sig.\\ Layers \\\\\n\\midrule\nCKA-only vs Standard & 2.89$\\times$ & 55\\,/\\,56 \\\\\nCKA-only vs \\rasp{} & 2.26$\\times$ & 56\\,/\\,56 \\\\\n\\rasp{} vs Standard & 1.28$\\times$ & 45\\,/\\,56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient magnitude hierarchy (CKA-only $\\gg$ \\rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\\% $>$ 60.88\\% $>$ 59.84\\%), with bootstrap 95\\% CIs for all ratios excluding 1.0.\nThis is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.\n\n\\section{Seed Reproducibility}\n\\label{sec:appendix_seed}\n\nCKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\\% (seed 42), 64.22\\% (seed 123), 64.59\\% (seed 456), yielding mean 64.39\\% $\\pm$ 0.19\\,pp.\nStandard: mean 59.84\\% $\\pm$ 0.38\\,pp across the same 3 seeds.\nSee Table~\\ref{tab:multiseed} for the full summary.\n\n\\section{Sparsity Cliff at 30\\%}\n\\label{sec:appendix_sparsity_cliff}\n\n\\input{tables/table4_sparsity_cliff}\n\nAll tested methods collapse at 30\\% sparsity: Standard retains 4\\% accuracy, CKA-only 1.6\\%, and \\rasp{} 0\\%.\nThis capacity threshold, independent of pruning criterion, validates 20\\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.\n\n\\section{Multi-Seed GRPO Results}\n\\label{sec:appendix_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}\n\\label{tab:multiseed}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & Mean Acc.\\,(\\%) & Std\\,(pp) & Seeds \\\\\n\\midrule\n\\multirow{4}{*}{20\\%} & CKA-only & 64.39 & 0.19 & 3 \\\\\n & Standard & 59.84 & 0.38 & 3 \\\\\n & \\rasp{} & 60.88 & -- & 1 \\\\\n & Random & 50.72 & 0.15 & 3 \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.76 & 0.57 & 3 \\\\\n & Standard & 65.56 & 0.50 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 20\\% sparsity, the 4.55\\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.59\\%, Standard: 59.44--60.20\\%).\nStandard shows a wider observed range across seeds (0.76\\,pp vs 0.37\\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.\nRandom (3 seeds: 50.57\\%, 50.72\\%, 50.87\\%; $\\sigma{=}0.15$\\,pp, observed range 0.30\\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\\%.\nAll three seeds satisfy GRPO $\\leq$ SFT ($\\Delta{=}{-}0.68$, $-$0.53, $-$0.38\\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.\nNote: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\\% vs.\\ 59.29\\% for seeds 123/456; $\\Delta = 0.08$\\,pp).\nAt 15\\% sparsity, the gap widens to 7.20\\,pp (72.76\\% vs 65.56\\%, $t{\\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\\%, Standard: 65.13--65.43\\%).\n\n\\section{Cross-Sparsity Validation}\n\\label{sec:appendix_cross_sparsity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\\% and 20\\% GRPO values are mean over 3 seeds (see Tables~\\ref{tab:decoupling},~\\ref{tab:multiseed}). $^\\ddagger$Single seed. Mean $|\\Delta| \\leq 1$\\,pp across all conditions.}\n\\label{tab:cross_sparsity}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.18 & \\textbf{72.76{\\scriptsize$\\pm$0.57}} & $+$0.58 \\\\\n & Standard & 66.49 & 65.56{\\scriptsize$\\pm$0.50} & $-$0.93 \\\\\n\\midrule\n\\multirow{2}{*}{20\\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\\\\n & Standard & 59.29 & 59.84 & $+$0.55 \\\\\n\\midrule\n\\multirow{2}{*}{25\\%$^\\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\\\\n & Standard & 50.87 & 51.86 & $+$0.99 \\\\\n\\midrule\n30\\% & All & \\multicolumn{3}{c}{Collapse ($\\leq$4\\%; Table~\\ref{tab:sparsity_cliff})} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 15\\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\\,pp (72.76\\% vs 65.56\\%), compared to $+$4.55\\,pp at 20\\%.\nCKA-only at 15\\% (72.76\\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\\% of original dense model performance (90.83\\%).\nAt 25\\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\\,pp from 15\\%$\\to$20\\%, $-$8.42\\,pp from 20\\%$\\to$25\\%), while CKA-only's decline decelerates ($-$8.27\\,pp then $-$3.79\\,pp).\nReward-accuracy decoupling is preserved ($|\\Delta| \\leq 1$\\,pp for both methods) despite Standard's near-zero peak reward (0.008).\n\n\\section{Cross-Scale Validation}\n\\label{sec:appendix_cross_scale}\n\n\\input{tables/tab5_cross_scale}\n\nOn DeepSeek-R1-Distill-Qwen-1.5B at 20\\% sparsity, the three-method ordering is preserved (CKA-only 35.48\\% $\\gg$ \\rasp{} 26.16\\% $>$ Standard 22.29\\%), with reward-accuracy decoupling confirmed at this scale ($|\\Delta| < 1$\\,pp: CKA-only $-$0.15, Standard $-$0.61\\,pp).\n\n\\section{Cross-Architecture Validation}\n\\label{sec:appendix_cross_arch}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture validation on Qwen2.5-Math-7B~\\citep{qwen2.5} at 20\\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports accuracy $\\pm$ binomial standard error ($N{=}200$). EOS rate: fraction of generations that produce a valid end-of-sequence token.}\n\\label{tab:cross_arch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Post-Prune\\,(\\%) & Post-SFT\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nCKA-only & 1.0 & \\textbf{51.50 $\\pm$ 3.53} & 27.0 \\\\\nStandard & 18.5 & 21.00 $\\pm$ 2.88 & 36.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nCKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\\% post-prune accuracy vs Standard's 18.5\\%), yet SFT recovers CKA-only to 51.50\\% while Standard remains at 21.00\\%.\nThis post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.\nEOS rates remain below 40\\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\\footnote{Preliminary GRPO evaluation yields 48.60\\% (243/500), but 83.8\\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}\n\n\\section{Structural Overlap Analysis}\n\\label{sec:appendix_overlap}\n\nCKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\\% sparsity.\nCKA-only concentrates pruning in early layers (L0--9 account for 72.5\\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).\nStandard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).\n\nThe methods share only partial overlap in which structures they remove.\n65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.\nConversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.\n\nThis pattern is consistent with the layer-wise CKA similarity analysis (Figure~\\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.\n\n\\section{KL Divergence During GRPO Training}\n\\label{sec:appendix_kl}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=0.75\\columnwidth]{figures/paper/fig_appendix_kl.pdf}\n    \\caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}\n    \\label{fig:kl_divergence}\n\\end{figure}\n\n\\section{Depth-First Pruning Baseline}\n\\label{sec:appendix_depth_first}\n\nAs a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\\% sparsity.\nBoth SFT (${\\sim}$10\\%) and GRPO (${\\sim}$8\\%) accuracy are near chance (early-stopped at $N{\\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.\nThis baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.\n\n\\section{Per-Layer Capacity Floor Ablation}\n\\label{sec:appendix_floor}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of per-layer capacity floor $\\tau$ on CKA-only pruning at 20\\% sparsity. GSM8K accuracy ($N{=}1{,}319$) after GRPO recovery (100 steps). Default $\\tau{=}0.4$.}\n\\label{tab:floor_ablation}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nFloor $\\tau$ & GRPO Acc.\\,(\\%) & $\\Delta$ vs $\\tau{=}0.4$\\,(pp) \\\\\n\\midrule\n0.3 & 65.05 & $+$0.68 \\\\\n0.4 (default) & 64.37 & --- \\\\\n0.5 & 61.71 & $-$2.66 \\\\\n0.6 & 62.02 & $-$2.35 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe per-layer capacity floor $\\tau$ sets the minimum fraction of MLP channel groups retained in each layer, preventing over-pruning of any single layer regardless of its importance score.\nWe ablate $\\tau \\in \\{0.3, 0.4, 0.5, 0.6\\}$ using CKA-only pruning at 20\\% sparsity.\nLowering $\\tau$ to 0.3 slightly improves accuracy ($+$0.68\\,pp), while raising it to 0.5 or 0.6 causes a notable drop ($-$2.66 and $-$2.35\\,pp respectively; the difference between 0.5 and 0.6 is not significant at 0.31\\,pp $\\ll$ stderr $\\approx$ 1.3\\,pp).\nOver-constraining per-layer retention hurts global pruning quality by forcing removal of important structures in unconstrained layers.\n\n\\section{Use of AI Assistants}\n\\label{sec:appendix_ai_assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform the related-work section.\n\\end{itemize}\n",
      "numLines": 327,
      "startLine": 1,
      "totalLines": 327
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01TRrk4Ji2R39VcszBxwTKxz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "56f74d8b-cbd2-4198-9cca-32af90f8e7f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6CNKSYbFdRRCbPQyJEkjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 416,
      "cache_read_input_tokens": 24463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 416
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

_source line 12 · 2026-05-24T07:15:47.596Z_

<details><summary>↩ Tool result · `toolu_01TRrk4Ji2R39VcszBxwTKxz`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	
4	Whether RLVR outperforms SFT for recovering pruned reasoning models depends on how the model was pruned.
5	Under diversity-preserving pruning, the two paradigms produce near-identical accuracy (mean $|\Delta| {=} 0.54$\,pp at 20\%; max $1.34$\,pp), yet the pruning criterion creates a 4.4$\times$ peak reward gap that persists through 300 steps (\S\ref{sec:extended_analysis}).
6	The dose-response across $\alpha$ identifies representational diversity as the causal driver: recovery peaks at $\alpha{=}2.0$ (66.11\%), and CKA similarity tracks the full spectrum ($\mu{=}0.62$ for CKA-only vs.\ $\mu{\geq}0.88$ for collapsing methods).
7	
8	\paragraph{Why does diversity preservation enable RL recovery?}
9	Policy gradient methods require trajectory variation to estimate reward gradients; importance-based pruning collapses the model onto the dense model's dominant reasoning mode, while CKA-only pruning preserves representationally distinct pathways that sustain exploration.
10	Gradient flow evidence supports this: CKA-only exhibits 2.89$\times$ mean gradient magnitude vs.\ Standard (\S\ref{sec:extended_analysis}), consistent with diversity preventing zero-variance batches ($f_0 > 0.5$).
11	Since RL updates only 5--30\% of parameters~\citep{mukherjee2025rlsubnetworks}, CKA-based pruning may preserve precisely this active subnetwork~\citep{frankle2019lth}.
12	
13	\paragraph{Practitioner guidelines.}
14	Use \rasp{} at $\alpha \approx 2.0$, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\ref{fig:dose_response}).
15	Under SFT alone, the criterion still matters (4.62\,pp gap; Table~\ref{tab:decoupling}).
16	Maintain per-layer floors ($\geq$40\%), stay below 25\% sparsity (\S\ref{sec:sparsity_cliff}), and monitor early $f_0$ as a pruning diagnostic.
17	
18	\paragraph{Scope and outlook.}
19	Decoupling holds across sparsity levels (15--25\%), scales (1.5B), and architectures (Qwen2.5-Math-7B); extension to unstructured~\citep{selfhealing2025} or rollout pruning~\citep{xu2026arrol} remains open.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "18ca839e-9785-4107-8ae4-1b8bf30af253",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:conclusion}\n\nWhether RLVR outperforms SFT for recovering pruned reasoning models depends on how the model was pruned.\nUnder diversity-preserving pruning, the two paradigms produce near-identical accuracy (mean $|\\Delta| {=} 0.54$\\,pp at 20\\%; max $1.34$\\,pp), yet the pruning criterion creates a 4.4$\\times$ peak reward gap that persists through 300 steps (\\S\\ref{sec:extended_analysis}).\nThe dose-response across $\\alpha$ identifies representational diversity as the causal driver: recovery peaks at $\\alpha{=}2.0$ (66.11\\%), and CKA similarity tracks the full spectrum ($\\mu{=}0.62$ for CKA-only vs.\\ $\\mu{\\geq}0.88$ for collapsing methods).\n\n\\paragraph{Why does diversity preservation enable RL recovery?}\nPolicy gradient methods require trajectory variation to estimate reward gradients; importance-based pruning collapses the model onto the dense model's dominant reasoning mode, while CKA-only pruning preserves representationally distinct pathways that sustain exploration.\nGradient flow evidence supports this: CKA-only exhibits 2.89$\\times$ mean gradient magnitude vs.\\ Standard (\\S\\ref{sec:extended_analysis}), consistent with diversity preventing zero-variance batches ($f_0 > 0.5$).\nSince RL updates only 5--30\\% of parameters~\\citep{mukherjee2025rlsubnetworks}, CKA-based pruning may preserve precisely this active subnetwork~\\citep{frankle2019lth}.\n\n\\paragraph{Practitioner guidelines.}\nUse \\rasp{} at $\\alpha \\approx 2.0$, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\\ref{fig:dose_response}).\nUnder SFT alone, the criterion still matters (4.62\\,pp gap; Table~\\ref{tab:decoupling}).\nMaintain per-layer floors ($\\geq$40\\%), stay below 25\\% sparsity (\\S\\ref{sec:sparsity_cliff}), and monitor early $f_0$ as a pruning diagnostic.\n\n\\paragraph{Scope and outlook.}\nDecoupling holds across sparsity levels (15--25\\%), scales (1.5B), and architectures (Qwen2.5-Math-7B); extension to unstructured~\\citep{selfhealing2025} or rollout pruning~\\citep{xu2026arrol} remains open.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01RCE7rqiCnwWNrKvqL4GjVq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "c3fc17bd-3f2c-40e6-b3e7-23e87badb67e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6CNKSYbFdRRCbPQyJEkjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 416,
      "cache_read_input_tokens": 24463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 416
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

_source line 14 · 2026-05-24T07:15:48.118Z_

<details><summary>↩ Tool result · `toolu_01RCE7rqiCnwWNrKvqL4GjVq`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dose-response analysis: effect of CKA coefficient $\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha{=}0$ reduces to Standard (importance-only); higher $\alpha$ weights representational diversity. Best in \textbf{bold}.}
5	\label{tab:alpha}
6	\begin{tabular}{@{}cccc@{}}
7	\toprule
8	$\alpha$ & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	0.5 & 60.73 & 61.18 & $+$0.45 \\
11	1.0 & 61.49 & 60.88 & $-$0.61 \\
12	\textbf{2.0} & \textbf{64.97} & \textbf{66.11} & $+$1.14 \\
13	3.0 & 64.14 & 63.46 & $-$0.68 \\
14	4.0 & 61.94 & 62.77 & $+$0.83 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "3a29c149-c1e3-4eb1-9a0f-563d1f296f92",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response analysis: effect of CKA coefficient $\\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\\% MLP channel sparsity. $\\alpha{=}0$ reduces to Standard (importance-only); higher $\\alpha$ weights representational diversity. Best in \\textbf{bold}.}\n\\label{tab:alpha}\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\alpha$ & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n0.5 & 60.73 & 61.18 & $+$0.45 \\\\\n1.0 & 61.49 & 60.88 & $-$0.61 \\\\\n\\textbf{2.0} & \\textbf{64.97} & \\textbf{66.11} & $+$1.14 \\\\\n3.0 & 64.14 & 63.46 & $-$0.68 \\\\\n4.0 & 61.94 & 62.77 & $+$0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the main.tex for the figure references, especially Figure 1 (dose-response sub-figure) and any references to the appendix alpha section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "b92e45ae-b150-4a63-8302-8cee4ada8943",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUtvsnUGWnF6inW1VcpRhR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14307,
      "cache_read_input_tokens": 24879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14307
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

_source line 16_

Now let me check main.tex for figure definitions and references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "ef484777-9568-4595-ae5f-e31bb9ef8b72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUtvsnUGWnF6inW1VcpRhR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14307,
      "cache_read_input_tokens": 24879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14307
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01Qt1rFbyf6RboayCVRrvxig`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "e537bb50-f9b2-44b3-882b-1f10559ad169",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUtvsnUGWnF6inW1VcpRhR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14307,
      "cache_read_input_tokens": 24879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14307
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

_source line 18 · 2026-05-24T07:15:53.776Z_

<details><summary>↩ Tool result · `toolu_01Qt1rFbyf6RboayCVRrvxig`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{siunitx}
17	\usepackage{algorithm}
18	\usepackage[noend]{algpseudocode}
19	\usepackage{enumitem}
20	\usepackage{xcolor}
21	\usepackage{hyperref}
22	
23	\newcommand{\rasp}{\textsc{Rasp}}
24	
25	\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\begin{abstract}
33	\input{abstract}
34	\end{abstract}
35	
36	\input{introduction}
37	\input{related_work}
38	\input{method}
39	\input{experiments}
40	\input{conclusion}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\section*{Ethics Statement}
46	\input{ethics}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	\end{document}
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "738ceed1-c29e-46a6-8b89-f4fe042daaaa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{siunitx}\n\\usepackage{algorithm}\n\\usepackage[noend]{algpseudocode}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\newcommand{\\rasp}{\\textsc{Rasp}}\n\n\\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\section*{Limitations}\n\\input{limitations}\n\n\\section*{Ethics Statement}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_013o8PTHdSjeMGXCYAxGsH9o`</summary>

```json
{
  "pattern": "dose.response|fig_dose|Figure.*dose|\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "fd4a8a9e-8f24-4026-8ace-b40fa502acde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pi7THg8bD5uHHtcS65HyQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 39186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
      },
      "output_tokens": 35,
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

_source line 20 · 2026-05-24T07:16:02.895Z_

<details><summary>↩ Tool result · `toolu_013o8PTHdSjeMGXCYAxGsH9o`</summary>

```text
docs/paper/main.fls:274:INPUT ../figures/paper/fig1_dose_response.pdf
docs/paper/main.fls:275:INPUT ../figures/paper/fig1_dose_response.pdf
docs/paper/main.fls:276:INPUT ../figures/paper/fig1_dose_response.pdf
docs/paper/main.fls:277:INPUT ../figures/paper/fig1_dose_response.pdf
docs/paper/main.fls:278:INPUT ../figures/paper/fig1_dose_response.pdf
docs/paper/experiments.tex:54:    \label{fig:training_dynamics}
docs/paper/experiments.tex:62:The dose-response (\S\ref{sec:sparsity_cliff}) confirms CKA weight as the critical variable: increasing $\alpha$ from 1.0 to 2.0 shifts \rasp{} from collapse to peak recovery (66.11\% vs.\ 64.39\% for CKA-only on GSM8K).
docs/paper/experiments.tex:74:    \label{fig:sft_grpo_scatter}
docs/paper/experiments.tex:79:At 20\% sparsity, the four fine-grained criteria show mean $|\Delta| {=} 0.54$\,pp (max $0.61$\,pp); across the full $\alpha$ dose-response spectrum, $|\Delta|$ remains below $1.14$\,pp.
docs/paper/experiments.tex:82:Across all four fine-grained criteria at 20\% and 25\%, $|\Delta| < 1$\,pp without exception on GSM8K (Tables~\ref{tab:decoupling},~\ref{tab:cross_sparsity}; Appendix~\ref{sec:appendix_cross_sparsity}); dose-response $\alpha$ variations show slightly larger but still small differences (max $1.14$\,pp at $\alpha{=}2.0$; Table~\ref{tab:alpha}; MATH-500 differences within statistical noise, Appendix~\ref{sec:appendix_math500}).
docs/paper/experiments.tex:99:\paragraph{Dose-response and sparsity limits.}
docs/paper/experiments.tex:114:    \label{fig:cka_heatmap}
docs/paper/experiments.tex:128:    \label{fig:extended_training}
docs/paper/conclusion.tex:6:The dose-response across $\alpha$ identifies representational diversity as the causal driver: recovery peaks at $\alpha{=}2.0$ (66.11\%), and CKA similarity tracks the full spectrum ($\mu{=}0.62$ for CKA-only vs.\ $\mu{\geq}0.88$ for collapsing methods).
docs/paper/conclusion.tex:14:Use \rasp{} at $\alpha \approx 2.0$, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\ref{fig:dose_response}).
docs/paper/main.log:697:<../figures/paper/fig1_dose_response.pdf, id=157, 238.73566pt x 184.32953pt>
docs/paper/main.log:698:File: ../figures/paper/fig1_dose_response.pdf Graphic file (type pdf)
docs/paper/main.log:699:&lt;use ../figures/paper/fig1_dose_response.pdf>
docs/paper/main.log:700:Package pdftex.def Info: ../figures/paper/fig1_dose_response.pdf  used on input
docs/paper/main.log:739:[2 <../figures/paper/fig1_dose_response.pdf>] [3]
docs/paper/tables/table3_alpha.tex:4:\caption{Dose-response analysis: effect of CKA coefficient $\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha{=}0$ reduces to Standard (importance-only); higher $\alpha$ weights representational diversity. Best in \textbf{bold}.}
docs/paper/tables/tab_math500.tex:18:\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
docs/paper/method.tex:89:\label{fig:method_framework}
docs/paper/main.fdb_latexmk:11:  "../figures/paper/fig1_dose_response.pdf" 1779465893.15584 20009 a49e8adef7371aa464c6a43377cfc8ed ""
docs/paper/abstract.tex:5:On DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity, a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at $\alpha{=}2.0$ (66.11\% on GSM8K).
docs/paper/appendix.tex:93:On GSM8K, the dose-response curve across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U pattern peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%, $\Delta{=}{+}1.14$\,pp; Table~\ref{tab:alpha}).
docs/paper/appendix.tex:115:The $\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\sim}$8\,pp across $\alpha$ values, but with stderr ${\approx}$2\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.
docs/paper/appendix.tex:116:The inverted-U pattern is validated on GSM8K (Table~\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.
docs/paper/appendix.tex:283:    \label{fig:kl_divergence}
docs/paper/introduction.tex:7:When pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\% sparsity, mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp across the four fine-grained criteria (max $0.61$\,pp); including dose-response variations and MBPP, the maximum is $1.34$\,pp.
docs/paper/introduction.tex:16:\includegraphics[width=\columnwidth]{../figures/paper/fig1_dose_response.pdf}
docs/paper/introduction.tex:17:\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\alpha{=}2.0$ (66.11\%). SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome.}
docs/paper/introduction.tex:18:\label{fig:dose_response}
docs/paper/introduction.tex:21:We present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\citep{kornblith2019cka} via a coefficient $\alpha$ in the pruning score (Figure~\ref{fig:dose_response}).
docs/paper/introduction.tex:22:The dose-response curve reveals an inverted-U: recovery peaks at $\alpha{=}2.0$ (66.11\% GRPO on GSM8K~\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.
docs/paper/introduction.tex:28:    \item \textbf{Reward-accuracy decoupling.} At 20--25\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria: mean $|\Delta| {=} 0.54$\,pp at 20\% (max $0.61$\,pp; $1.34$\,pp including dose-response variations and MBPP). At 15\%, GRPO can still amplify the CKA-guided advantage ($+$1.51\,pp differential), but this partial exception reinforces the main pattern: the pruning criterion, not the recovery paradigm, determines outcome (\S\ref{sec:decoupling}).
docs/paper/introduction.tex:29:[Omitted long matching line]
docs/paper/main.aux:129:[Omitted long matching line]
docs/paper/main.aux:131:\newlabel{fig:dose_response}{{1}{2}{Dose-response curve for the CKA diversity coefficient $\alpha $ at 20\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\alpha {=}2.0$ (66.11\%). SFT and GRPO curves nearly overlap ($|\Delta | \leq 1.14$\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome}{figure.caption.1}{}}
docs/paper/main.aux:648:\newlabel{sec:sparsity_cliff}{{4.4}{7}{Dose-response and sparsity limits}{section*.27}{}}
docs/paper/main.aux:649:\@writefile{toc}{\contentsline {paragraph}{Dose-response and sparsity limits.}{7}{section*.27}\protected@file@percent }
docs/paper/main.aux:1093:\@writefile{lot}{\contentsline {table}{\numberline {5}{\ignorespaces Dose-response analysis: effect of CKA coefficient $\alpha $ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha {=}0$ reduces to Standard (importance-only); higher $\alpha $ weights representational diversity. Best in \textbf  {bold}.}}{12}{table.caption.44}\protected@file@percent }
docs/paper/main.aux:1094:\newlabel{tab:alpha}{{5}{12}{Dose-response analysis: effect of CKA coefficient $\alpha $ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha {=}0$ reduces to Standard (importance-only); higher $\alpha $ weights representational diversity. Best in \textbf {bold}}{table.caption.44}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "ccd0ee59-29fb-4397-901d-7351087bb15c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.fls:274:INPUT ../figures/paper/fig1_dose_response.pdf\ndocs/paper/main.fls:275:INPUT ../figures/paper/fig1_dose_response.pdf\ndocs/paper/main.fls:276:INPUT ../figures/paper/fig1_dose_response.pdf\ndocs/paper/main.fls:277:INPUT ../figures/paper/fig1_dose_response.pdf\ndocs/paper/main.fls:278:INPUT ../figures/paper/fig1_dose_response.pdf\ndocs/paper/experiments.tex:54:    \\label{fig:training_dynamics}\ndocs/paper/experiments.tex:62:The dose-response (\\S\\ref{sec:sparsity_cliff}) confirms CKA weight as the critical variable: increasing $\\alpha$ from 1.0 to 2.0 shifts \\rasp{} from collapse to peak recovery (66.11\\% vs.\\ 64.39\\% for CKA-only on GSM8K).\ndocs/paper/experiments.tex:74:    \\label{fig:sft_grpo_scatter}\ndocs/paper/experiments.tex:79:At 20\\% sparsity, the four fine-grained criteria show mean $|\\Delta| {=} 0.54$\\,pp (max $0.61$\\,pp); across the full $\\alpha$ dose-response spectrum, $|\\Delta|$ remains below $1.14$\\,pp.\ndocs/paper/experiments.tex:82:Across all four fine-grained criteria at 20\\% and 25\\%, $|\\Delta| < 1$\\,pp without exception on GSM8K (Tables~\\ref{tab:decoupling},~\\ref{tab:cross_sparsity}; Appendix~\\ref{sec:appendix_cross_sparsity}); dose-response $\\alpha$ variations show slightly larger but still small differences (max $1.14$\\,pp at $\\alpha{=}2.0$; Table~\\ref{tab:alpha}; MATH-500 differences within statistical noise, Appendix~\\ref{sec:appendix_math500}).\ndocs/paper/experiments.tex:99:\\paragraph{Dose-response and sparsity limits.}\ndocs/paper/experiments.tex:114:    \\label{fig:cka_heatmap}\ndocs/paper/experiments.tex:128:    \\label{fig:extended_training}\ndocs/paper/conclusion.tex:6:The dose-response across $\\alpha$ identifies representational diversity as the causal driver: recovery peaks at $\\alpha{=}2.0$ (66.11\\%), and CKA similarity tracks the full spectrum ($\\mu{=}0.62$ for CKA-only vs.\\ $\\mu{\\geq}0.88$ for collapsing methods).\ndocs/paper/conclusion.tex:14:Use \\rasp{} at $\\alpha \\approx 2.0$, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\\ref{fig:dose_response}).\ndocs/paper/main.log:697:<../figures/paper/fig1_dose_response.pdf, id=157, 238.73566pt x 184.32953pt>\ndocs/paper/main.log:698:File: ../figures/paper/fig1_dose_response.pdf Graphic file (type pdf)\ndocs/paper/main.log:699:&lt;use ../figures/paper/fig1_dose_response.pdf>\ndocs/paper/main.log:700:Package pdftex.def Info: ../figures/paper/fig1_dose_response.pdf  used on input\ndocs/paper/main.log:739:[2 <../figures/paper/fig1_dose_response.pdf>] [3]\ndocs/paper/tables/table3_alpha.tex:4:\\caption{Dose-response analysis: effect of CKA coefficient $\\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\\% MLP channel sparsity. $\\alpha{=}0$ reduces to Standard (importance-only); higher $\\alpha$ weights representational diversity. Best in \\textbf{bold}.}\ndocs/paper/tables/tab_math500.tex:18:\\multicolumn{4}{l}{\\textit{20\\% sparsity --- $\\alpha$ dose-response}} \\\\\ndocs/paper/method.tex:89:\\label{fig:method_framework}\ndocs/paper/main.fdb_latexmk:11:  \"../figures/paper/fig1_dose_response.pdf\" 1779465893.15584 20009 a49e8adef7371aa464c6a43377cfc8ed \"\"\ndocs/paper/abstract.tex:5:On DeepSeek-R1-Distill-Qwen-7B at 20\\% sparsity, a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at $\\alpha{=}2.0$ (66.11\\% on GSM8K).\ndocs/paper/appendix.tex:93:On GSM8K, the dose-response curve across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U pattern peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%, $\\Delta{=}{+}1.14$\\,pp; Table~\\ref{tab:alpha}).\ndocs/paper/appendix.tex:115:The $\\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\\sim}$8\\,pp across $\\alpha$ values, but with stderr ${\\approx}$2\\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.\ndocs/paper/appendix.tex:116:The inverted-U pattern is validated on GSM8K (Table~\\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.\ndocs/paper/appendix.tex:283:    \\label{fig:kl_divergence}\ndocs/paper/introduction.tex:7:When pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\\% sparsity, mean $|\\Delta(\\text{GRPO}-\\text{SFT})| {=} 0.54$\\,pp across the four fine-grained criteria (max $0.61$\\,pp); including dose-response variations and MBPP, the maximum is $1.34$\\,pp.\ndocs/paper/introduction.tex:16:\\includegraphics[width=\\columnwidth]{../figures/paper/fig1_dose_response.pdf}\ndocs/paper/introduction.tex:17:\\caption{Dose-response curve for the CKA diversity coefficient $\\alpha$ at 20\\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\\alpha{=}2.0$ (66.11\\%). SFT and GRPO curves nearly overlap ($|\\Delta| \\leq 1.14$\\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome.}\ndocs/paper/introduction.tex:18:\\label{fig:dose_response}\ndocs/paper/introduction.tex:21:We present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\\citep{kornblith2019cka} via a coefficient $\\alpha$ in the pruning score (Figure~\\ref{fig:dose_response}).\ndocs/paper/introduction.tex:22:The dose-response curve reveals an inverted-U: recovery peaks at $\\alpha{=}2.0$ (66.11\\% GRPO on GSM8K~\\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.\ndocs/paper/introduction.tex:28:    \\item \\textbf{Reward-accuracy decoupling.} At 20--25\\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria: mean $|\\Delta| {=} 0.54$\\,pp at 20\\% (max $0.61$\\,pp; $1.34$\\,pp including dose-response variations and MBPP). At 15\\%, GRPO can still amplify the CKA-guided advantage ($+$1.51\\,pp differential), but this partial exception reinforces the main pattern: the pruning criterion, not the recovery paradigm, determines outcome (\\S\\ref{sec:decoupling}).\ndocs/paper/introduction.tex:29:[Omitted long matching line]\ndocs/paper/main.aux:129:[Omitted long matching line]\ndocs/paper/main.aux:131:\\newlabel{fig:dose_response}{{1}{2}{Dose-response curve for the CKA diversity coefficient $\\alpha $ at 20\\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\\alpha {=}2.0$ (66.11\\%). SFT and GRPO curves nearly overlap ($|\\Delta | \\leq 1.14$\\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome}{figure.caption.1}{}}\ndocs/paper/main.aux:648:\\newlabel{sec:sparsity_cliff}{{4.4}{7}{Dose-response and sparsity limits}{section*.27}{}}\ndocs/paper/main.aux:649:\\@writefile{toc}{\\contentsline {paragraph}{Dose-response and sparsity limits.}{7}{section*.27}\\protected@file@percent }\ndocs/paper/main.aux:1093:\\@writefile{lot}{\\contentsline {table}{\\numberline {5}{\\ignorespaces Dose-response analysis: effect of CKA coefficient $\\alpha $ on GSM8K accuracy ($N{=}1{,}319$) at 20\\% MLP channel sparsity. $\\alpha {=}0$ reduces to Standard (importance-only); higher $\\alpha $ weights representational diversity. Best in \\textbf  {bold}.}}{12}{table.caption.44}\\protected@file@percent }\ndocs/paper/main.aux:1094:\\newlabel{tab:alpha}{{5}{12}{Dose-response analysis: effect of CKA coefficient $\\alpha $ on GSM8K accuracy ($N{=}1{,}319$) at 20\\% MLP channel sparsity. $\\alpha {=}0$ reduces to Standard (importance-only); higher $\\alpha $ weights representational diversity. Best in \\textbf {bold}}{table.caption.44}{}}",
    "numLines": 43
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_01JGkZ2Rain3TQgreWTk4azG`</summary>

```json
{
  "pattern": "appendix_alpha|sec:appendix_alpha|Appendix.*alpha",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
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
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "b08574bd-1a1c-4a68-9e48-311a49b024da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pi7THg8bD5uHHtcS65HyQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 39186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
      },
      "output_tokens": 35,
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

_source line 22 · 2026-05-24T07:16:04.347Z_

<details><summary>↩ Tool result · `toolu_01JGkZ2Rain3TQgreWTk4azG`</summary>

```text
docs/paper/experiments.tex:82:Across all four fine-grained criteria at 20\% and 25\%, $|\Delta| < 1$\,pp without exception on GSM8K (Tables~\ref{tab:decoupling},~\ref{tab:cross_sparsity}; Appendix~\ref{sec:appendix_cross_sparsity}); dose-response $\alpha$ variations show slightly larger but still small differences (max $1.14$\,pp at $\alpha{=}2.0$; Table~\ref{tab:alpha}; MATH-500 differences within statistical noise, Appendix~\ref{sec:appendix_math500}).
docs/paper/experiments.tex:102:[Omitted long matching line]
docs/paper/appendix.tex:89:\label{sec:appendix_alpha}
docs/paper/main.aux:1084:\newlabel{sec:appendix_alpha}{{D}{11}{CKA Coefficient $\alpha $ Ablation}{appendix.D}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "4a397998-8c1a-4c9e-831c-87e51ccfc107",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:82:Across all four fine-grained criteria at 20\\% and 25\\%, $|\\Delta| < 1$\\,pp without exception on GSM8K (Tables~\\ref{tab:decoupling},~\\ref{tab:cross_sparsity}; Appendix~\\ref{sec:appendix_cross_sparsity}); dose-response $\\alpha$ variations show slightly larger but still small differences (max $1.14$\\,pp at $\\alpha{=}2.0$; Table~\\ref{tab:alpha}; MATH-500 differences within statistical noise, Appendix~\\ref{sec:appendix_math500}).\ndocs/paper/experiments.tex:102:[Omitted long matching line]\ndocs/paper/appendix.tex:89:\\label{sec:appendix_alpha}\ndocs/paper/main.aux:1084:\\newlabel{sec:appendix_alpha}{{D}{11}{CKA Coefficient $\\alpha $ Ablation}{appendix.D}{}}",
    "numLines": 4
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me compile the report.

1. **α=2.0 GRPO 追平 CKA-only 的结论**: 
   - experiments.tex line 62: "increasing $\alpha$ from 1.0 to 2.0 shifts \rasp{} from collapse to peak recovery (66.11\% vs.\ 64.39\% for CKA-only on GSM8K)"
   - So yes, α=2.0 GRPO 66.11% is mentioned, and CKA-only 64.39% is mentioned, and it says it shifts to "peak recovery" exceeding CKA-only. ✅
   
2. **倒 U 型 dose-response 曲线描述**: The paper documents an inverted-U relationship across the α values tested, with performance peaking at α=2.0 where both SFT and GRPO achieve their best results (64.97% and 66.11% respectively), while maintaining tight variance across all tested points. At α=1.0 the model collapses entirely, establishing the critical threshold where the regularization becomes effective.

3. **§4.4 dose-response 段引用**: Now I'm checking whether the dose-response section in §4.4 properly references supporting figures and tables. The text mentions specific performance numbers at α=2.0 but I need to verify if there's an explicit table reference or if it's only implied through the appendix citation. -response section doesn't actually reference the dose-response figure or the alpha table, only the appendix. Figure 1 is mentioned in the conclusion, but the main results section skips those citations entirely. Looking at the §4.4 paragraph more carefully, it references the appendix but is missing the direct citation to Figure 1's dose-response subplot and doesn't explicitly call out Table~\ref{tab:alpha} in that section itself—though Table~\ref{tab:math500} is mentioned. The appendix is being cited correctly in the main text, but the specific figure reference is absent from §4.4.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "759b8e53-64c3-4829-8633-8cda9235d3f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TM8QNG32oZfGp8zXt47B5B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3416,
      "cache_read_input_tokens": 39842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3416
      },
      "output_tokens": 11,
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

_source line 24_

## Dose-Response Narrative 完整性检查报告

### 1. α=2.0 GRPO 追平 CKA-only 的结论
**✅ 已有**

- `experiments.tex:62` — "increasing $\alpha$ from 1.0 to 2.0 shifts RASP from collapse to peak recovery (66.11% vs. 64.39% for CKA-only on GSM8K)"
- `appendix.tex:93` — "inverted-U pattern peaking at α=2.0 (SFT 64.97%, GRPO 66.11%)"
- `conclusion.tex:6` — "recovery peaks at α=2.0 (66.11%)"
- `tables/table3_alpha.tex:12` — 表格中 α=2.0 行加粗，GRPO 66.11%

数值完整，"追平/超过"语义通过 66.11% vs 64.39% 的对比明确传达。

### 2. 倒 U 型 dose-response 曲线描述
**✅ 已有**

- `experiments.tex:101-102` — "recovery follows an inverted-U across α ∈ {0.5, 1.0, 2.0, 3.0, 4.0}, peaking at α=2.0"，并给出 α=1.0 collapse 和 α=4.0 恢复到 62.77% 的完整两侧描述
- `introduction.tex:17,22` — Figure 1 caption 和正文均描述 "inverted-U"
- `abstract.tex:5` — "a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at α=2.0"
- `appendix.tex:93-97` — 完整五点 α 值的逐点描述，包括 α=3.0 排除 plateau 假说

### 3. §4.4 dose-response 段引用
**⚠️ 部分缺失**

`experiments.tex:99-104`（§4.4 Dose-response and sparsity limits）当前引用：
- ✅ `Appendix~\ref{sec:appendix_alpha}` (line 102)
- ✅ `Table~\ref{tab:math500}` (line 103)
- ❌ **未引用 Figure~\ref{fig:dose_response}**（Figure 1，dose-response 曲线图）
- ❌ **未直接引用 Table~\ref{tab:alpha}**（仅通过 Appendix 间接关联）

`Table~\ref{tab:alpha}` 在 §4.3 (line 82) 被引用过，但 §4.4 本身——作为 dose-response 的核心段落——应该直接引用 Figure 1 和 Table 5。

**建议**：在 `experiments.tex:102` 中添加 `(Figure~\ref{fig:dose_response}; Table~\ref{tab:alpha})`，例如改为：
> "...peaking at α=2.0 (SFT 64.97%, GRPO 66.11%; Figure~\ref{fig:dose_response}, Table~\ref{tab:alpha})"

### 4. Appendix D（α ablation）被正文引用
**✅ 已有**

- `experiments.tex:102` — `Appendix~\ref{sec:appendix_alpha}` 直接引用
- `appendix.tex:89` — `\label{sec:appendix_alpha}` 定义（编译后为 Appendix D）

### 5. α=2.0 作为 practitioner guideline
**✅ 已有**

- `conclusion.tex:13-14` — `\paragraph{Practitioner guidelines.} Use RASP at α ≈ 2.0, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\ref{fig:dose_response}).`
- 同段 line 16 还给出配套建议：per-layer floors ≥40%、sparsity <25%、monitor early f₀

---

**总结**：5 项中 4 项完整，1 项部分缺失。§4.4 dose-response 段应直接引用 Figure 1 和 Table 5（tab_alpha），当前仅间接通过 Appendix 关联。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "uuid": "a9c5b429-7352-4c58-ba88-dd789b0e0457",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TM8QNG32oZfGp8zXt47B5B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3416,
      "cache_read_input_tokens": 39842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3416
      },
      "output_tokens": 11,
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

## Dose-Response Narrative 完整性检查报告

### 1. α=2.0 GRPO 追平 CKA-only 的结论
**✅ 已有**

- `experiments.tex:62` — "increasing $\alpha$ from 1.0 to 2.0 shifts RASP from collapse to peak recovery (66.11% vs. 64.39% for CKA-only on GSM8K)"
- `appendix.tex:93` — "inverted-U pattern peaking at α=2.0 (SFT 64.97%, GRPO 66.11%)"
- `conclusion.tex:6` — "recovery peaks at α=2.0 (66.11%)"
- `tables/table3_alpha.tex:12` — 表格中 α=2.0 行加粗，GRPO 66.11%

数值完整，"追平/超过"语义通过 66.11% vs 64.39% 的对比明确传达。

### 2. 倒 U 型 dose-response 曲线描述
**✅ 已有**

- `experiments.tex:101-102` — "recovery follows an inverted-U across α ∈ {0.5, 1.0, 2.0, 3.0, 4.0}, peaking at α=2.0"，并给出 α=1.0 collapse 和 α=4.0 恢复到 62.77% 的完整两侧描述
- `introduction.tex:17,22` — Figure 1 caption 和正文均描述 "inverted-U"
- `abstract.tex:5` — "a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at α=2.0"
- `appendix.tex:93-97` — 完整五点 α 值的逐点描述，包括 α=3.0 排除 plateau 假说

### 3. §4.4 dose-response 段引用
**⚠️ 部分缺失**

`experiments.tex:99-104`（§4.4 Dose-response and sparsity limits）当前引用：
- ✅ `Appendix~\ref{sec:appendix_alpha}` (line 102)
- ✅ `Table~\ref{tab:math500}` (line 103)
- ❌ **未引用 Figure~\ref{fig:dose_response}**（Figure 1，dose-response 曲线图）
- ❌ **未直接引用 Table~\ref{tab:alpha}**（仅通过 Appendix 间接关联）

`Table~\ref{tab:alpha}` 在 §4.3 (line 82) 被引用过，但 §4.4 本身——作为 dose-response 的核心段落——应该直接引用 Figure 1 和 Table 5。

**建议**：在 `experiments.tex:102` 中添加 `(Figure~\ref{fig:dose_response}; Table~\ref{tab:alpha})`，例如改为：
> "...peaking at α=2.0 (SFT 64.97%, GRPO 66.11%; Figure~\ref{fig:dose_response}, Table~\ref{tab:alpha})"

### 4. Appendix D（α ablation）被正文引用
**✅ 已有**

- `experiments.tex:102` — `Appendix~\ref{sec:appendix_alpha}` 直接引用
- `appendix.tex:89` — `\label{sec:appendix_alpha}` 定义（编译后为 Appendix D）

### 5. α=2.0 作为 practitioner guideline
**✅ 已有**

- `conclusion.tex:13-14` — `\paragraph{Practitioner guidelines.} Use RASP at α ≈ 2.0, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\ref{fig:dose_response}).`
- 同段 line 16 还给出配套建议：per-layer floors ≥40%、sparsity <25%、monitor early f₀

---

**总结**：5 项中 4 项完整，1 项部分缺失。§4.4 dose-response 段应直接引用 Figure 1 和 Table 5（tab_alpha），当前仅间接通过 Appendix 关联。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 88288,
  "duration_api_ms": 89251,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "024fcd0c-c71f-439a-831f-707d3fd7e7d0",
  "total_cost_usd": 0.35876275,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 31417,
    "cache_read_input_tokens": 140211,
    "output_tokens": 3621,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31417,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2742,
        "cache_read_input_tokens": 39842,
        "cache_creation_input_tokens": 3416,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3416
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1651,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001741,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 3621,
      "cacheReadInputTokens": 140211,
      "cacheCreationInputTokens": 31417,
      "webSearchRequests": 0,
      "costUSD": 0.35702175,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3827010f-afd0-46ba-9506-410be4f8e041"
}
```

</details>

---
