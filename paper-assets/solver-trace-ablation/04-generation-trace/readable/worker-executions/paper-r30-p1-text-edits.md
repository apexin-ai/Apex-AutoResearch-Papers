# paper r30 p1 text edits

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_paper_r30-p1-text-edits_20260522T154550.log`
- **Structured JSON:** [`a79d1d6c1dc75eb3ba32.json`](../../sessions/a7/a79d1d6c1dc75eb3ba32.json)

## Before a recorded user message

56 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
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
    "mcp__agent-ml-research__clone_repo",
    "mcp__agent-ml-research__list_repo_tree",
    "mcp__agent-ml-research__read_repo_file",
    "mcp__agent-ml-research__search_repo",
    "mcp__agent-ml-research__sync_code_to_remote"
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
  "uuid": "df9ce7b0-07c9-4e8f-92ca-20bde6019b0f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1779478800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4acd1e5b-deee-4e28-9712-fcfa449aa77c",
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down into tasks:

P1-A: Temper causal language in experiments.tex
P1-B: Add ISR* note to Table 1 caption in experiments.tex
P1-C: Add a sentence to limitations.tex
P1-D: Add Wilhelm citation to references.bib and a sentence to related_work.tex

I need to read the files first, then make edits in both docs/paper/ and paper/ directories.

Let me start by reading the relevant files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "0b5e0ed0-4eaf-4802-9e61-d608fd6e2573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116tCZscigAg9K5itxAiwbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15374,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15374
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

_source line 5_

Reading the relevant files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "8e4ec2e9-ed8f-4393-a5a6-928101741714",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116tCZscigAg9K5itxAiwbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15374,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15374
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01CzBFs6SVAH9e8wNngttiAB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "9e9f37ea-3237-49e2-92ed-f063c79ba7d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116tCZscigAg9K5itxAiwbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15374,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15374
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

_source line 7 · 2026-05-22T15:46:02.494Z_

<details><summary>↩ Tool result · `toolu_01CzBFs6SVAH9e8wNngttiAB`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\ref{app:hacking-modes}).
13	
14	\paragraph{Statistical considerations.}
15	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
16	Pooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.
17	At $N{=}3$, seed-level tests achieve 80\% power only for very large effects ($d{\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.
18	An $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\ref{app:n2-sensitivity}).
19	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.
20	
21	\subsection{ISR as Diagnostic}
22	\label{sec:diagnostic}
23	
24	\textbf{Collapse trajectory.}
25	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.
26	As PR climbs from $32\%$ to $96\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\times$, \S\ref{sec:goodhart}) that reveals structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
27	By 500 steps, $87\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.
28	A binary variant testing only collective premise necessity misses the collapse entirely ($\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\ref{app:o1-ablation}).
29	
30	\textbf{Cross-seed instability.}
31	Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\leq}7\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
32	Two additional seeds under identical conditions fail to converge ($\text{PR}{\approx}14\%$; Appendix~\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\ref{app:llama-coldstart}).
33	
34	\textbf{SFT baseline.}
35	SFT on gold formalizations produces $92\%$ non-hacking outputs at $\text{PR}{=}13\%$ ($\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.
36	SFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.
37	Early-training comparison supports this interpretation: at 100 steps ($\text{PR}{=}32\%$), hacking already reaches $31\%$ vs.\ SFT's $8\%$ at comparable PR (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
38	
39	\subsection{Goodhart Effects on ISR-as-Reward}
40	\label{sec:goodhart}
41	
42	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
43	The result is a regressional Goodhart pattern~\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \emph{composition} of failure modes without reducing their aggregate prevalence.
44	ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$ after controlling for premise count.
45	
46	\paragraph{Multiplicative coupling.}
47	The multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.
48	The shuffled-ISR control produces SFT-like outcomes ($87\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).
49	
50	\begin{table*}[t]
51	\centering
52	\small
53	\begin{tabular}{lcccccc}
54	\toprule
55	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
56	\midrule
57	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
58	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
59	\midrule
60	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
61	ISR (3-seed) & 0.1 & 77{\scriptsize$\pm$14} & $1.06\times^\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
62	ISR (5-seed) & 0.1 & 70{\scriptsize$\pm$19} & (0.63)$^\ddagger$ & 54 & 18 & 23 \\ %% registry: plan002-additive-b01-s42--s46 (pooled)
63	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
64	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
65	\midrule
66	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
67	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
68	\bottomrule
69	\end{tabular}
70	\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\times$ is the premise-count-matched value relative to random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random TS driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\S\ref{sec:goodhart}), not an independent reward condition. ISR $\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\sim}55\%$ non-hacking each; Appendix~\ref{app:detailed-results}).}
71	\label{tab:goodhart-landscape}
72	\end{table*}
73	
74	\textbf{Low-dose ISR ($\beta{=}0.1$).}
75	ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random ($\text{OR}_{\text{CMH}}{=}2.46$; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
76	TS is the canonical Goodhart move: a single premise identical to the conclusion yields $\text{ISR}\geq 0.5$ by construction, directly satisfying the LOO metric (\S\ref{sec:taxonomy-method}).
77	Total conclusion embedding ($\text{CE}+\text{TS}$) spans $68$--$100\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\ref{fig:hacking-composition}).
78	
79	\textbf{Premise-count confound.}
80	Raw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.
81	After matching for premise count, the apparent $3.2\times$ advantage shrinks to $1.06\times$ (Appendix~\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test
82	The asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.
83	
84	\textbf{Higher doses and temporal dynamics.}
85	Any genuine reasoning under ISR $\beta{=}0.1$ is transient: non-hacking drops from $17\%$ to $2\%$ by 1000 steps as TS escalates (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
86	Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
87	
88	\textbf{Bimodal seed-dependence (5-seed extension).}
89	Two additional seeds (s45, s46; Appendix~\ref{app:detailed-results}) under the same ISR $\beta{=}0.1$ condition yield ${\sim}55\%$ non-hacking, qualitatively different from the 3-seed average of $6\%$.
90	This bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \S\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46
91	Seeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\times}2$ vs $2{\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\ref{app:detailed-results}).
92	
93	\subsection{Cross-Domain and Cross-Dataset Evidence}
94	\label{sec:crossdomain}
95	\label{sec:crosslogic}
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
100	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
101	\label{fig:prolog-comparison}
102	\end{figure}
103	
104	\textbf{Prolog: universal Goodhart.}
105	Replicating the pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}), exec-only seeds collapse to $\text{ISR}^*{\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.
106	Under ISR-as-reward, all three seeds reach $0\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\ref{tab:prolog-detailed}).
107	Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.
108	
109	\textbf{ProofFOL exec-only: cross-dataset replication.}
110	Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.
111	The dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.
112	
113	\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
114	ISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.
115	
116	\textbf{Mechanism.}
117	The asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.
118	ISR-as-reward inherits the dataset's hacking topology.
119	
120	\paragraph{Cross-scale validation (Qwen3-8B).}
121	Qwen3-8B does not converge under exec-only GRPO ($\text{PR}{=}14\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\ref{app:8b-results}).
122	
123	\subsection{Hacking Taxonomy}
124	\label{sec:taxonomy}
125	
126	\begin{figure}[t]
127	\centering
128	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
129	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}
130	\label{fig:hacking-composition}
131	\end{figure}
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\resizebox{\columnwidth}{!}{%
137	\begin{tabular}{lccccc}
138	\toprule
139	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
140	\midrule
141	CE embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
142	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
143	PG prem-subset & 6  & 5  & 8   & 0 & --- \\
144	Tautological   & --- & --- & --- & --- & s42 \\
145	Repetition     & s43 & --- & --- & --- & --- \\
146	Contradiction  & 1k & --- & --- & --- & --- \\
147	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
148	Query-as-fact  & --- & --- & --- & --- & s44 \\
149	\midrule
150	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
151	\bottomrule
152	\end{tabular}}
153	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}). \texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}
154	\label{tab:hacking-taxonomy}
155	\end{table}
156	
157	Three modes account for the vast majority of hacking (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).
158	The central pattern: \emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\%$ non-hacking.
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "6a6ce772-ce62-46fe-bf76-13b92b95ad75",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) that reveals structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
      "numLines": 159,
      "startLine": 1,
      "totalLines": 159
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01ECQ7gQGJvBCU65hKPeZGt7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "3f199d7e-9ada-453c-8a18-01657c3bb676",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116tCZscigAg9K5itxAiwbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15374,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15374
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

_source line 9 · 2026-05-22T15:46:03.019Z_

<details><summary>↩ Tool result · `toolu_01ECQ7gQGJvBCU65hKPeZGt7`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	Structural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\% genuine; Appendix~\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.
7	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
8	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "e27d2b4f-e247-4726-b68d-a81c3d7b641f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\\ref{app:8b-results},~\\ref{app:llama-coldstart}), leaving cross-scale generalization untested.\nThree to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.\nStructural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\\% genuine; Appendix~\\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.\nOne of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\\ref{app:detailed-results}).\nISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.\n",
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

<details open><summary>🔧 Tool call — Read · `toolu_011E4krCNndeaC2GJGFgjfZd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "6bba01ad-d6d4-4cf5-8c6f-48424fc99d0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116tCZscigAg9K5itxAiwbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15374,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15374
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

_source line 11 · 2026-05-22T15:46:03.363Z_

<details><summary>↩ Tool result · `toolu_011E4krCNndeaC2GJGFgjfZd`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
18	Most closely related, \citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.
19	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.
20	Reward model ensembles~\citep{coste2023reward} and constrained optimization~\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.
21	Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\citep{tarek2025reward, pronesti2026beyond}; \citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.
22	\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.
23	While IPT perturbs \emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.
24	\citet{khalifa2026countdown} provide RLVR hacking testbeds.
25	Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\beta$; its application to a diagnostic designed to \emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.
26	
27	\paragraph{Mutation testing.}
28	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "4d6f93f2-9dee-40eb-bab6-82d356b75111",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.\nIn mathematical reasoning, learned process reward models~\\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\\citep{processbench}.\nA recurring finding is that auxiliary rewards can hurt rather than help: \\citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \\citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.\nAnnotation-free alternatives~\\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\nMost closely related, \\citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.\nReward model ensembles~\\citep{coste2023reward} and constrained optimization~\\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.\nConcurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond}; \\citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.\nWhile IPT perturbs \\emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \\emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nOur Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\\beta$; its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01FQLTuR59PRPKBAk7MF7Ypx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "8693977a-a2e4-430a-96d6-7bac45adc004",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116tCZscigAg9K5itxAiwbh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15374,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15374
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

_source line 13 · 2026-05-22T15:46:03.839Z_

<details><summary>↩ Tool result · `toolu_01FQLTuR59PRPKBAk7MF7Ypx`</summary>

```text
1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
51	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
52	  year         = {2023},
53	}
54	
55	% ============================================================
56	% Category 2: Reward shaping for code/formal verification
57	% ============================================================
58	
59	@inproceedings{lightman-verify-step,
60	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
61	  title        = {{Let's Verify Step by Step}},
62	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
63	  year         = {2024},
64	  note         = {arXiv:2305.20050},
65	}
66	
67	@inproceedings{skalse-reward-hacking,
68	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
69	  title        = {{Defining and Characterizing Reward Hacking}},
70	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
71	  year         = {2022},
72	  note         = {arXiv:2209.13085},
73	}
74	
75	% ============================================================
76	% Category 3: Mutation testing in software engineering
77	% ============================================================
78	
79	@article{demillo1978,
80	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
81	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
82	  journal      = {Computer},
83	  volume       = {11},
84	  number       = {4},
85	  pages        = {34--41},
86	  year         = {1978},
87	}
88	
89	@article{jia-harman-survey,
90	  author       = {Yue Jia and Mark Harman},
91	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
92	  journal      = {IEEE Transactions on Software Engineering},
93	  volume       = {37},
94	  number       = {5},
95	  pages        = {649--678},
96	  year         = {2011},
97	}
98	
99	@article{spurious-rewards,
100	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
101	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
102	  journal      = {arXiv preprint arXiv:2506.10947},
103	  year         = {2025},
104	  eprint       = {2506.10947},
105	  archivePrefix = {arXiv},
106	  primaryClass = {cs.AI},
107	}
108	
109	@article{bondarenko-spec-gaming,
110	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
111	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
112	  journal      = {arXiv preprint arXiv:2502.13295},
113	  year         = {2025},
114	  eprint       = {2502.13295},
115	  archivePrefix = {arXiv},
116	  primaryClass = {cs.AI},
117	}
118	
119	@inproceedings{kim-game-formalization,
120	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
121	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
122	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
123	  year         = {2026},
124	  note         = {arXiv:2604.19459},
125	}
126	
127	@inproceedings{gao-reward-overoptimization,
128	  author       = {Leo Gao and John Schulman and Jacob Hilton},
129	  title        = {{Scaling Laws for Reward Model Overoptimization}},
130	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
131	  year         = {2023},
132	  note         = {arXiv:2210.10760},
133	}
134	
135	@inproceedings{karwowski-goodhart-rl,
136	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
137	  title        = {{Goodhart's Law in Reinforcement Learning}},
138	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
139	  year         = {2024},
140	  note         = {arXiv:2310.09144},
141	}
142	
143	% ============================================================
144	% Category 6: FOL/Prolog formalization with LLMs
145	% ============================================================
146	
147	@inproceedings{folio,
148	  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},
149	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
150	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
151	  year         = {2024},
152	  note         = {arXiv:2209.00840},
153	}
154	
155	@inproceedings{logic-lm,
156	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},
157	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
158	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
159	  year         = {2023},
160	}
161	
162	@inproceedings{linc,
163	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},
164	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
165	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
166	  year         = {2023},
167	}
168	
169	@article{fover-pei2025,
170	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
171	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
172	  journal      = {Transactions of the Association for Computational Linguistics},
173	  volume       = {13},
174	  pages        = {1340--1359},
175	  year         = {2025},
176	}
177	
178	@article{lorp,
179	  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},
180	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
181	  journal      = {Knowledge-Based Systems},
182	  year         = {2025},
183	}
184	
185	@article{manheim-goodhart-taxonomy,
186	  author       = {David Manheim and Scott Garrabrant},
187	  title        = {{Categorizing Variants of Goodhart's Law}},
188	  journal      = {arXiv preprint arXiv:1803.04585},
189	  year         = {2019},
190	  eprint       = {1803.04585},
191	  archivePrefix = {arXiv},
192	  primaryClass = {cs.AI},
193	}
194	
195	@inproceedings{math-shepherd,
196	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},
197	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
198	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
199	  year         = {2024},
200	  note         = {arXiv:2312.08935},
201	}
202	
203	% ============================================================
204	% Reward shaping and process supervision
205	% ============================================================
206	
207	@article{rlsf,
208	  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},
209	  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},
210	  journal      = {arXiv preprint arXiv:2405.16661},
211	  year         = {2024},
212	  eprint       = {2405.16661},
213	  archivePrefix = {arXiv},
214	  primaryClass = {cs.AI},
215	}
216	
217	@article{gao-effective-rl-reward,
218	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
219	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
220	  journal      = {arXiv preprint arXiv:2410.15115},
221	  year         = {2024},
222	  eprint       = {2410.15115},
223	  archivePrefix = {arXiv},
224	  primaryClass = {cs.AI},
225	}
226	
227	@inproceedings{kwa-catastrophic-goodhart,
228	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\`{a} Garriga-Alonso},
229	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
230	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
231	  year         = {2024},
232	  note         = {arXiv:2404.18926},
233	}
234	
235	@article{deepseek-prover-v15,
236	  author       = {{DeepSeek AI}},
237	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
238	  journal      = {arXiv preprint arXiv:2408.08152},
239	  year         = {2024},
240	  eprint       = {2408.08152},
241	  archivePrefix = {arXiv},
242	}
243	
244	@article{deepseek-r1,
245	  author       = {{DeepSeek-AI}},
246	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
247	  journal      = {arXiv preprint arXiv:2501.12948},
248	  year         = {2025},
249	  eprint       = {2501.12948},
250	  archivePrefix = {arXiv},
251	}
252	
253	@inproceedings{nlproofs,
254	  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},
255	  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},
256	  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
257	  year         = {2022},
258	  eprint       = {2205.12443},
259	  archivePrefix = {arXiv},
260	}
261	
262	@inproceedings{vstar,
263	  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},
264	  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},
265	  booktitle    = {Conference on Language Modeling (COLM)},
266	  year         = {2024},
267	  eprint       = {2402.06457},
268	  archivePrefix = {arXiv},
269	}
270	
271	@inproceedings{easy-to-hard,
272	  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},
273	  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},
274	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
275	  year         = {2024},
276	  eprint       = {2403.09472},
277	  archivePrefix = {arXiv},
278	}
279	
280	% ============================================================
281	% Additional reward-shaping papers
282	% ============================================================
283	
284	@article{reward-hacking-survey,
285	  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},
286	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
287	  journal      = {arXiv preprint arXiv:2604.13602},
288	  year         = {2026},
289	  eprint       = {2604.13602},
290	  archivePrefix = {arXiv},
291	}
292	
293	@misc{metr-reward-hacking,
294	  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},
295	  title        = {{Recent Frontier Models Are Reward Hacking}},
296	  year         = {2025},
297	  howpublished = {METR Technical Blog},
298	  note         = {\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},
299	}
300	
301	@inproceedings{proofwriter,
302	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
303	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
304	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
305	  year         = {2021},
306	  note         = {arXiv:2012.13048},
307	}
308	
309	@article{prooffol-thatikonda2024,
310	  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},
311	  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},
312	  journal      = {arXiv preprint arXiv:2409.16461},
313	  year         = {2024},
314	  eprint       = {2409.16461},
315	  archivePrefix = {arXiv},
316	}
317	
318	@article{qwen3,
319	  author       = {{Qwen Team}},
320	  title        = {{Qwen3 Technical Report}},
321	  journal      = {arXiv preprint arXiv:2505.09388},
322	  year         = {2025},
323	  eprint       = {2505.09388},
324	  archivePrefix = {arXiv},
325	  primaryClass = {cs.CL},
326	}
327	
328	@article{helff2026gaming,
329	  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},
330	  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},
331	  journal      = {arXiv preprint arXiv:2604.15149},
332	  year         = {2026},
333	  eprint       = {2604.15149},
334	  archivePrefix = {arXiv},
335	}
336	
337	@article{khalifa2026countdown,
338	  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},
339	  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},
340	  journal      = {arXiv preprint arXiv:2603.07084},
341	  year         = {2026},
342	  eprint       = {2603.07084},
343	  archivePrefix = {arXiv},
344	}
345	
346	@inproceedings{uesato2022solving,
347	  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},
348	  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},
349	  booktitle={NeurIPS 2022 Workshop on MATH-AI},
350	  year={2022}
351	}
352	
353	@article{cobbe2021training,
354	  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
355	  title        = {{Training Verifiers to Solve Math Word Problems}},
356	  journal      = {arXiv preprint arXiv:2110.14168},
357	  year         = {2021},
358	}
359	
360	@inproceedings{processbench,
361	  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},
362	  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},
363	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
364	  year         = {2025},
365	  note         = {arXiv:2412.06559},
366	}
367	
368	@article{pronesti2026beyond,
369	  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},
370	  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},
371	  journal      = {arXiv preprint arXiv:2601.17223},
372	  year         = {2026},
373	  eprint       = {2601.17223},
374	  archivePrefix = {arXiv},
375	}
376	
377	@inproceedings{ng1999policy,
378	  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},
379	  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},
380	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
381	  year      = {1999},
382	  pages     = {278--287},
383	}
384	
385	@article{geirhos2020shortcut,
386	  author  = {Robert Geirhos and J{\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},
387	  title   = {Shortcut Learning in Deep Neural Networks},
388	  journal = {Nature Machine Intelligence},
389	  volume  = {2},
390	  pages   = {665--673},
391	  year    = {2020},
392	}
393	
394	@article{dong2026probing,
395	  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},
396	  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},
397	  journal      = {arXiv preprint arXiv:2602.01103},
398	  year         = {2026},
399	  eprint       = {2602.01103},
400	  archivePrefix = {arXiv},
401	}
402	
403	@article{yan2026spurious,
404	  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},
405	  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},
406	  journal      = {arXiv preprint arXiv:2601.11061},
407	  year         = {2026},
408	  eprint       = {2601.11061},
409	  archivePrefix = {arXiv},
410	}
411	
412	@article{tarek2025reward,
413	  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},
414	  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},
415	  journal      = {arXiv preprint arXiv:2509.15557},
416	  year         = {2025},
417	  eprint       = {2509.15557},
418	  archivePrefix = {arXiv},
419	}
420	
421	@inproceedings{yue2025rl-reasoning,
422	  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},
423	  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},
424	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
425	  year         = {2025},
426	  eprint       = {2504.13837},
427	  archivePrefix = {arXiv},
428	}
429	
430	@article{sullivan2025grpo-prm,
431	  author       = {Michael Sullivan and Alexander Koller},
432	  title        = {{GRPO} is Secretly a Process Reward Model},
433	  journal      = {arXiv preprint arXiv:2509.21154},
434	  year         = {2025},
435	  eprint       = {2509.21154},
436	  archivePrefix = {arXiv},
437	}
438	
439	% ============================================================
440	% R19 reviewer-requested references
441	% ============================================================
442	
443	@inproceedings{setlur2025rewarding,
444	  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},
445	  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},
446	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
447	  year         = {2025},
448	  note         = {arXiv:2410.08146},
449	}
450	
451	@article{alphaproof2025,
452	  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},
453	  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},
454	  journal      = {Nature},
455	  year         = {2025},
456	  doi          = {10.1038/s41586-025-09833-y},
457	}
458	
459	% ============================================================
460	% Solvers (Prover9, SWI-Prolog)
461	% ============================================================
462	
463	@article{deepseek-prover-v2,
464	  author       = {{DeepSeek-AI}},
465	  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},
466	  journal      = {arXiv preprint arXiv:2504.21801},
467	  year         = {2025},
468	  eprint       = {2504.21801},
469	  archivePrefix = {arXiv},
470	}
471	
472	@article{cui2025prime,
473	  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},
474	  title        = {{Process Reinforcement through Implicit Rewards}},
475	  journal      = {arXiv preprint arXiv:2502.01456},
476	  year         = {2025},
477	  eprint       = {2502.01456},
478	  archivePrefix = {arXiv},
479	  primaryClass = {cs.CL},
480	}
481	
482	@misc{mccune-prover9,
483	  author       = {William McCune},
484	  title        = {{Prover9 and Mace4}},
485	  year         = {2005--2010},
486	  howpublished = {\url{https://www.cs.unm.edu/~mccune/prover9/}},
487	  note         = {Version 2009-11A},
488	}
489	
490	@inproceedings{lundberg2017unified,
491	  author       = {Scott M. Lundberg and Su-In Lee},
492	  title        = {A Unified Approach to Interpreting Model Predictions},
493	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
494	  year         = {2017},
495	}
496	
497	@inproceedings{coste2023reward,
498	  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},
499	  title        = {Reward Model Ensembles Help Mitigate Overoptimization},
500	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
501	  year         = {2024},
502	  note         = {arXiv:2310.02743},
503	}
504	
505	@inproceedings{moskovitz2023confronting,
506	  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},
507	  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},
508	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
509	  year         = {2024},
510	  note         = {arXiv:2310.04373},
511	}
512	
513	@article{wielemaker2012swi,
514	  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\"o}rn Lager},
515	  title        = {{SWI-Prolog}},
516	  journal      = {Theory and Practice of Logic Programming},
517	  volume       = {12},
518	  number       = {1--2},
519	  pages        = {67--96},
520	  year         = {2012},
521	  doi          = {10.1017/S1471068411000494},
522	}
523	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "1158588a-5a98-4ca9-8a33-a7aeaa58f3be",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
      "content": "% ============================================================\n% LLaMA\n% ============================================================\n\n@article{grattafiori2024llama,\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},\n  title = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n  eprint = {2407.21783},\n  archiveprefix = {arXiv},\n}\n\n% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2404.18926},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2501.12948},\n  year         = {2025},\n  eprint       = {2501.12948},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nlproofs,\n  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},\n  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},\n  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2022},\n  eprint       = {2205.12443},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{vstar,\n  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},\n  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},\n  booktitle    = {Conference on Language Modeling (COLM)},\n  year         = {2024},\n  eprint       = {2402.06457},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{easy-to-hard,\n  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},\n  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  eprint       = {2403.09472},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR Technical Blog},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{prooffol-thatikonda2024,\n  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},\n  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},\n  journal      = {arXiv preprint arXiv:2409.16461},\n  year         = {2024},\n  eprint       = {2409.16461},\n  archivePrefix = {arXiv},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@article{helff2026gaming,\n  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\\\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},\n  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},\n  journal      = {arXiv preprint arXiv:2604.15149},\n  year         = {2026},\n  eprint       = {2604.15149},\n  archivePrefix = {arXiv},\n}\n\n@article{khalifa2026countdown,\n  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},\n  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},\n  journal      = {arXiv preprint arXiv:2603.07084},\n  year         = {2026},\n  eprint       = {2603.07084},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{uesato2022solving,\n  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  booktitle={NeurIPS 2022 Workshop on MATH-AI},\n  year={2022}\n}\n\n@article{cobbe2021training,\n  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},\n  title        = {{Training Verifiers to Solve Math Word Problems}},\n  journal      = {arXiv preprint arXiv:2110.14168},\n  year         = {2021},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{pronesti2026beyond,\n  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},\n  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},\n  journal      = {arXiv preprint arXiv:2601.17223},\n  year         = {2026},\n  eprint       = {2601.17223},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{ng1999policy,\n  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},\n  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {1999},\n  pages     = {278--287},\n}\n\n@article{geirhos2020shortcut,\n  author  = {Robert Geirhos and J{\\\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},\n  title   = {Shortcut Learning in Deep Neural Networks},\n  journal = {Nature Machine Intelligence},\n  volume  = {2},\n  pages   = {665--673},\n  year    = {2020},\n}\n\n@article{dong2026probing,\n  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},\n  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},\n  journal      = {arXiv preprint arXiv:2602.01103},\n  year         = {2026},\n  eprint       = {2602.01103},\n  archivePrefix = {arXiv},\n}\n\n@article{yan2026spurious,\n  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},\n  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},\n  journal      = {arXiv preprint arXiv:2601.11061},\n  year         = {2026},\n  eprint       = {2601.11061},\n  archivePrefix = {arXiv},\n}\n\n@article{tarek2025reward,\n  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},\n  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},\n  journal      = {arXiv preprint arXiv:2509.15557},\n  year         = {2025},\n  eprint       = {2509.15557},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yue2025rl-reasoning,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},\n  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  eprint       = {2504.13837},\n  archivePrefix = {arXiv},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO} is Secretly a Process Reward Model},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% R19 reviewer-requested references\n% ============================================================\n\n@inproceedings{setlur2025rewarding,\n  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},\n  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2410.08146},\n}\n\n@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n% ============================================================\n% Solvers (Prover9, SWI-Prolog)\n% ============================================================\n\n@article{deepseek-prover-v2,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},\n  journal      = {arXiv preprint arXiv:2504.21801},\n  year         = {2025},\n  eprint       = {2504.21801},\n  archivePrefix = {arXiv},\n}\n\n@article{cui2025prime,\n  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},\n  title        = {{Process Reinforcement through Implicit Rewards}},\n  journal      = {arXiv preprint arXiv:2502.01456},\n  year         = {2025},\n  eprint       = {2502.01456},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@misc{mccune-prover9,\n  author       = {William McCune},\n  title        = {{Prover9 and Mace4}},\n  year         = {2005--2010},\n  howpublished = {\\url{https://www.cs.unm.edu/~mccune/prover9/}},\n  note         = {Version 2009-11A},\n}\n\n@inproceedings{lundberg2017unified,\n  author       = {Scott M. Lundberg and Su-In Lee},\n  title        = {A Unified Approach to Interpreting Model Predictions},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2017},\n}\n\n@inproceedings{coste2023reward,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {Reward Model Ensembles Help Mitigate Overoptimization},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.02743},\n}\n\n@inproceedings{moskovitz2023confronting,\n  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},\n  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n",
      "numLines": 523,
      "startLine": 1,
      "totalLines": 523
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper/ versions of these files as well to see their current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "ce579d55-bb1a-48da-854c-af394bac8e35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBvTsangJ4SR7XyyveA1ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17034,
      "cache_read_input_tokens": 27215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17034
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

_source line 15_

Now reading the paper/ directory counterparts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "86a051f5-92da-40e9-bebd-6b0ce2dff39b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBvTsangJ4SR7XyyveA1ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17034,
      "cache_read_input_tokens": 27215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17034
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_017UiKrdx3K5rp49DvsUAsGx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "833b3dd2-3f5a-457a-9045-ed60291b61b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBvTsangJ4SR7XyyveA1ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17034,
      "cache_read_input_tokens": 27215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17034
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

_source line 17 · 2026-05-22T15:46:11.608Z_

<details><summary>↩ Tool result · `toolu_017UiKrdx3K5rp49DvsUAsGx`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\ref{app:hacking-modes}).
13	
14	\paragraph{Statistical considerations.}
15	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
16	Pooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.
17	At $N{=}3$, seed-level tests achieve 80\% power only for very large effects ($d{\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.
18	An $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\ref{app:n2-sensitivity}).
19	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.
20	
21	\subsection{ISR as Diagnostic}
22	\label{sec:diagnostic}
23	
24	\textbf{Collapse trajectory.}
25	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.
26	As PR climbs from $32\%$ to $96\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\times$, \S\ref{sec:goodhart}) that reveals structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
27	By 500 steps, $87\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.
28	A binary variant testing only collective premise necessity misses the collapse entirely ($\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\ref{app:o1-ablation}).
29	
30	\textbf{Cross-seed instability.}
31	Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\leq}7\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
32	Two additional seeds under identical conditions fail to converge ($\text{PR}{\approx}14\%$; Appendix~\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\ref{app:llama-coldstart}).
33	
34	\textbf{SFT baseline.}
35	SFT on gold formalizations produces $92\%$ non-hacking outputs at $\text{PR}{=}13\%$ ($\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.
36	SFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.
37	Early-training comparison supports this interpretation: at 100 steps ($\text{PR}{=}32\%$), hacking already reaches $31\%$ vs.\ SFT's $8\%$ at comparable PR (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
38	
39	\subsection{Goodhart Effects on ISR-as-Reward}
40	\label{sec:goodhart}
41	
42	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
43	The result is a regressional Goodhart pattern~\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \emph{composition} of failure modes without reducing their aggregate prevalence.
44	ISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\times$ to $1.06\times$ after controlling for premise count.
45	
46	\paragraph{Multiplicative coupling.}
47	The multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.
48	The shuffled-ISR control produces SFT-like outcomes ($87\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).
49	
50	\begin{table*}[t]
51	\centering
52	\small
53	\begin{tabular}{lcccccc}
54	\toprule
55	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
56	\midrule
57	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
58	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
59	\midrule
60	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
61	ISR (3-seed) & 0.1 & 77{\scriptsize$\pm$14} & $1.06\times^\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
62	ISR (5-seed) & 0.1 & 70{\scriptsize$\pm$19} & (0.63)$^\ddagger$ & 54 & 18 & 23 \\ %% registry: plan002-additive-b01-s42--s46 (pooled)
63	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
64	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
65	\midrule
66	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
67	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
68	\bottomrule
69	\end{tabular}
70	\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\times$ is the premise-count-matched value relative to random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random TS driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\S\ref{sec:goodhart}), not an independent reward condition. ISR $\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\sim}55\%$ non-hacking each; Appendix~\ref{app:detailed-results}).}
71	\label{tab:goodhart-landscape}
72	\end{table*}
73	
74	\textbf{Low-dose ISR ($\beta{=}0.1$).}
75	ISR reward amplifies TS convergence: $71\%$ of proved samples under ISR exhibit tautological shortcuts vs.\ $14\%$ under random ($\text{OR}_{\text{CMH}}{=}2.46$; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
76	TS is the canonical Goodhart move: a single premise identical to the conclusion yields $\text{ISR}\geq 0.5$ by construction, directly satisfying the LOO metric (\S\ref{sec:taxonomy-method}).
77	Total conclusion embedding ($\text{CE}+\text{TS}$) spans $68$--$100\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\ref{fig:hacking-composition}).
78	
79	\textbf{Premise-count confound.}
80	Raw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.
81	After matching for premise count, the apparent $3.2\times$ advantage shrinks to $1.06\times$ (Appendix~\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test
82	The asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.
83	
84	\textbf{Higher doses and temporal dynamics.}
85	Any genuine reasoning under ISR $\beta{=}0.1$ is transient: non-hacking drops from $17\%$ to $2\%$ by 1000 steps as TS escalates (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
86	Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
87	
88	\textbf{Bimodal seed-dependence (5-seed extension).}
89	Two additional seeds (s45, s46; Appendix~\ref{app:detailed-results}) under the same ISR $\beta{=}0.1$ condition yield ${\sim}55\%$ non-hacking, qualitatively different from the 3-seed average of $6\%$.
90	This bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \S\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46
91	Seeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\times}2$ vs $2{\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\ref{app:detailed-results}).
92	
93	\subsection{Cross-Domain and Cross-Dataset Evidence}
94	\label{sec:crossdomain}
95	\label{sec:crosslogic}
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
100	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
101	\label{fig:prolog-comparison}
102	\end{figure}
103	
104	\textbf{Prolog: universal Goodhart.}
105	Replicating the pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}), exec-only seeds collapse to $\text{ISR}^*{\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.
106	Under ISR-as-reward, all three seeds reach $0\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\ref{tab:prolog-detailed}).
107	Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.
108	
109	\textbf{ProofFOL exec-only: cross-dataset replication.}
110	Converged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.
111	The dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.
112	
113	\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
114	ISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.
115	
116	\textbf{Mechanism.}
117	The asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\text{ISR}{\approx}0$ and rendering ISR reward effectively corrective.
118	ISR-as-reward inherits the dataset's hacking topology.
119	
120	\paragraph{Cross-scale validation (Qwen3-8B).}
121	Qwen3-8B does not converge under exec-only GRPO ($\text{PR}{=}14\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\ref{app:8b-results}).
122	
123	\subsection{Hacking Taxonomy}
124	\label{sec:taxonomy}
125	
126	\begin{figure}[t]
127	\centering
128	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
129	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}
130	\label{fig:hacking-composition}
131	\end{figure}
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\resizebox{\columnwidth}{!}{%
137	\begin{tabular}{lccccc}
138	\toprule
139	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
140	\midrule
141	CE embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
142	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
143	PG prem-subset & 6  & 5  & 8   & 0 & --- \\
144	Tautological   & --- & --- & --- & --- & s42 \\
145	Repetition     & s43 & --- & --- & --- & --- \\
146	Contradiction  & 1k & --- & --- & --- & --- \\
147	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
148	Query-as-fact  & --- & --- & --- & --- & s44 \\
149	\midrule
150	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
151	\bottomrule
152	\end{tabular}}
153	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}). \texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}
154	\label{tab:hacking-taxonomy}
155	\end{table}
156	
157	Three modes account for the vast majority of hacking (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).
158	The central pattern: \emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\%$ non-hacking.
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "42891105-61fb-4ebc-8870-041c8eda32e8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) that reveals structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
      "numLines": 159,
      "startLine": 1,
      "totalLines": 159
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_018TbhFVgmk4dXZmEPuHT9NF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "4d830fb8-7aab-48e5-b83b-dd60775b1123",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBvTsangJ4SR7XyyveA1ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17034,
      "cache_read_input_tokens": 27215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17034
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

_source line 19 · 2026-05-22T15:46:12.572Z_

<details><summary>↩ Tool result · `toolu_018TbhFVgmk4dXZmEPuHT9NF`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	Structural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\% genuine; Appendix~\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.
7	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
8	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "4dc21608-c104-4d36-bde3-61052f91d14c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\\ref{app:8b-results},~\\ref{app:llama-coldstart}), leaving cross-scale generalization untested.\nThree to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.\nStructural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\\% genuine; Appendix~\\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.\nOne of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\\ref{app:detailed-results}).\nISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.\n",
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

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01CY81eEBNQjkhNmxhti9sX2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "b65412c6-fe1f-44bd-b441-71d51dace585",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBvTsangJ4SR7XyyveA1ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17034,
      "cache_read_input_tokens": 27215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17034
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

_source line 21 · 2026-05-22T15:46:12.938Z_

<details><summary>↩ Tool result · `toolu_01CY81eEBNQjkhNmxhti9sX2`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
18	Most closely related, \citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.
19	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.
20	Reward model ensembles~\citep{coste2023reward} and constrained optimization~\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.
21	Concurrent work documents spurious signals in RLVR~\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\citep{tarek2025reward, pronesti2026beyond}; \citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.
22	\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.
23	While IPT perturbs \emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.
24	\citet{khalifa2026countdown} provide RLVR hacking testbeds.
25	Our Goodhart effect follows the regressional pattern~\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\beta$; its application to a diagnostic designed to \emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.
26	
27	\paragraph{Mutation testing.}
28	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "072c133e-c99a-44c8-8b24-39f229d02a84",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.\nIn mathematical reasoning, learned process reward models~\\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\\citep{processbench}.\nA recurring finding is that auxiliary rewards can hurt rather than help: \\citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \\citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.\nAnnotation-free alternatives~\\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\nMost closely related, \\citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.\nReward model ensembles~\\citep{coste2023reward} and constrained optimization~\\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.\nConcurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond}; \\citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.\nWhile IPT perturbs \\emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \\emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nOur Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\\beta$; its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01NWAHF7MfFd88HGAijRpNME`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "47284155-99c7-4b75-9775-998332c839e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBvTsangJ4SR7XyyveA1ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17034,
      "cache_read_input_tokens": 27215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17034
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

_source line 23 · 2026-05-22T15:46:13.170Z_

<details><summary>↩ Tool result · `toolu_01NWAHF7MfFd88HGAijRpNME`</summary>

```text
1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
51	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
52	  year         = {2023},
53	}
54	
55	% ============================================================
56	% Category 2: Reward shaping for code/formal verification
57	% ============================================================
58	
59	@inproceedings{lightman-verify-step,
60	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
61	  title        = {{Let's Verify Step by Step}},
62	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
63	  year         = {2024},
64	  note         = {arXiv:2305.20050},
65	}
66	
67	@inproceedings{skalse-reward-hacking,
68	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
69	  title        = {{Defining and Characterizing Reward Hacking}},
70	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
71	  year         = {2022},
72	  note         = {arXiv:2209.13085},
73	}
74	
75	% ============================================================
76	% Category 3: Mutation testing in software engineering
77	% ============================================================
78	
79	@article{demillo1978,
80	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
81	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
82	  journal      = {Computer},
83	  volume       = {11},
84	  number       = {4},
85	  pages        = {34--41},
86	  year         = {1978},
87	}
88	
89	@article{jia-harman-survey,
90	  author       = {Yue Jia and Mark Harman},
91	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
92	  journal      = {IEEE Transactions on Software Engineering},
93	  volume       = {37},
94	  number       = {5},
95	  pages        = {649--678},
96	  year         = {2011},
97	}
98	
99	@article{spurious-rewards,
100	  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},
101	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
102	  journal      = {arXiv preprint arXiv:2506.10947},
103	  year         = {2025},
104	  eprint       = {2506.10947},
105	  archivePrefix = {arXiv},
106	  primaryClass = {cs.AI},
107	}
108	
109	@article{bondarenko-spec-gaming,
110	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
111	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
112	  journal      = {arXiv preprint arXiv:2502.13295},
113	  year         = {2025},
114	  eprint       = {2502.13295},
115	  archivePrefix = {arXiv},
116	  primaryClass = {cs.AI},
117	}
118	
119	@inproceedings{kim-game-formalization,
120	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
121	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
122	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
123	  year         = {2026},
124	  note         = {arXiv:2604.19459},
125	}
126	
127	@inproceedings{gao-reward-overoptimization,
128	  author       = {Leo Gao and John Schulman and Jacob Hilton},
129	  title        = {{Scaling Laws for Reward Model Overoptimization}},
130	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
131	  year         = {2023},
132	  note         = {arXiv:2210.10760},
133	}
134	
135	@inproceedings{karwowski-goodhart-rl,
136	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
137	  title        = {{Goodhart's Law in Reinforcement Learning}},
138	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
139	  year         = {2024},
140	  note         = {arXiv:2310.09144},
141	}
142	
143	% ============================================================
144	% Category 6: FOL/Prolog formalization with LLMs
145	% ============================================================
146	
147	@inproceedings{folio,
148	  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},
149	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
150	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
151	  year         = {2024},
152	  note         = {arXiv:2209.00840},
153	}
154	
155	@inproceedings{logic-lm,
156	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},
157	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
158	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
159	  year         = {2023},
160	}
161	
162	@inproceedings{linc,
163	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},
164	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
165	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
166	  year         = {2023},
167	}
168	
169	@article{fover-pei2025,
170	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
171	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
172	  journal      = {Transactions of the Association for Computational Linguistics},
173	  volume       = {13},
174	  pages        = {1340--1359},
175	  year         = {2025},
176	}
177	
178	@article{lorp,
179	  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},
180	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
181	  journal      = {Knowledge-Based Systems},
182	  year         = {2025},
183	}
184	
185	@article{manheim-goodhart-taxonomy,
186	  author       = {David Manheim and Scott Garrabrant},
187	  title        = {{Categorizing Variants of Goodhart's Law}},
188	  journal      = {arXiv preprint arXiv:1803.04585},
189	  year         = {2019},
190	  eprint       = {1803.04585},
191	  archivePrefix = {arXiv},
192	  primaryClass = {cs.AI},
193	}
194	
195	@inproceedings{math-shepherd,
196	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},
197	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
198	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
199	  year         = {2024},
200	  note         = {arXiv:2312.08935},
201	}
202	
203	% ============================================================
204	% Reward shaping and process supervision
205	% ============================================================
206	
207	@article{rlsf,
208	  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},
209	  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},
210	  journal      = {arXiv preprint arXiv:2405.16661},
211	  year         = {2024},
212	  eprint       = {2405.16661},
213	  archivePrefix = {arXiv},
214	  primaryClass = {cs.AI},
215	}
216	
217	@article{gao-effective-rl-reward,
218	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
219	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
220	  journal      = {arXiv preprint arXiv:2410.15115},
221	  year         = {2024},
222	  eprint       = {2410.15115},
223	  archivePrefix = {arXiv},
224	  primaryClass = {cs.AI},
225	}
226	
227	@inproceedings{kwa-catastrophic-goodhart,
228	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\`{a} Garriga-Alonso},
229	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
230	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
231	  year         = {2024},
232	  note         = {arXiv:2404.18926},
233	}
234	
235	@article{deepseek-prover-v15,
236	  author       = {{DeepSeek AI}},
237	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
238	  journal      = {arXiv preprint arXiv:2408.08152},
239	  year         = {2024},
240	  eprint       = {2408.08152},
241	  archivePrefix = {arXiv},
242	}
243	
244	@article{deepseek-r1,
245	  author       = {{DeepSeek-AI}},
246	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
247	  journal      = {arXiv preprint arXiv:2501.12948},
248	  year         = {2025},
249	  eprint       = {2501.12948},
250	  archivePrefix = {arXiv},
251	}
252	
253	@inproceedings{nlproofs,
254	  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},
255	  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},
256	  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
257	  year         = {2022},
258	  eprint       = {2205.12443},
259	  archivePrefix = {arXiv},
260	}
261	
262	@inproceedings{vstar,
263	  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},
264	  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},
265	  booktitle    = {Conference on Language Modeling (COLM)},
266	  year         = {2024},
267	  eprint       = {2402.06457},
268	  archivePrefix = {arXiv},
269	}
270	
271	@inproceedings{easy-to-hard,
272	  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},
273	  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},
274	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
275	  year         = {2024},
276	  eprint       = {2403.09472},
277	  archivePrefix = {arXiv},
278	}
279	
280	% ============================================================
281	% Additional reward-shaping papers
282	% ============================================================
283	
284	@article{reward-hacking-survey,
285	  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},
286	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
287	  journal      = {arXiv preprint arXiv:2604.13602},
288	  year         = {2026},
289	  eprint       = {2604.13602},
290	  archivePrefix = {arXiv},
291	}
292	
293	@misc{metr-reward-hacking,
294	  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},
295	  title        = {{Recent Frontier Models Are Reward Hacking}},
296	  year         = {2025},
297	  howpublished = {METR Technical Blog},
298	  note         = {\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},
299	}
300	
301	@inproceedings{proofwriter,
302	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
303	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
304	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
305	  year         = {2021},
306	  note         = {arXiv:2012.13048},
307	}
308	
309	@article{prooffol-thatikonda2024,
310	  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},
311	  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},
312	  journal      = {arXiv preprint arXiv:2409.16461},
313	  year         = {2024},
314	  eprint       = {2409.16461},
315	  archivePrefix = {arXiv},
316	}
317	
318	@article{qwen3,
319	  author       = {{Qwen Team}},
320	  title        = {{Qwen3 Technical Report}},
321	  journal      = {arXiv preprint arXiv:2505.09388},
322	  year         = {2025},
323	  eprint       = {2505.09388},
324	  archivePrefix = {arXiv},
325	  primaryClass = {cs.CL},
326	}
327	
328	@article{helff2026gaming,
329	  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},
330	  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},
331	  journal      = {arXiv preprint arXiv:2604.15149},
332	  year         = {2026},
333	  eprint       = {2604.15149},
334	  archivePrefix = {arXiv},
335	}
336	
337	@article{khalifa2026countdown,
338	  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},
339	  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},
340	  journal      = {arXiv preprint arXiv:2603.07084},
341	  year         = {2026},
342	  eprint       = {2603.07084},
343	  archivePrefix = {arXiv},
344	}
345	
346	@inproceedings{uesato2022solving,
347	  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},
348	  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},
349	  booktitle={NeurIPS 2022 Workshop on MATH-AI},
350	  year={2022}
351	}
352	
353	@article{cobbe2021training,
354	  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},
355	  title        = {{Training Verifiers to Solve Math Word Problems}},
356	  journal      = {arXiv preprint arXiv:2110.14168},
357	  year         = {2021},
358	}
359	
360	@inproceedings{processbench,
361	  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},
362	  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},
363	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
364	  year         = {2025},
365	  note         = {arXiv:2412.06559},
366	}
367	
368	@article{pronesti2026beyond,
369	  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},
370	  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},
371	  journal      = {arXiv preprint arXiv:2601.17223},
372	  year         = {2026},
373	  eprint       = {2601.17223},
374	  archivePrefix = {arXiv},
375	}
376	
377	@inproceedings{ng1999policy,
378	  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},
379	  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},
380	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
381	  year      = {1999},
382	  pages     = {278--287},
383	}
384	
385	@article{geirhos2020shortcut,
386	  author  = {Robert Geirhos and J{\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},
387	  title   = {Shortcut Learning in Deep Neural Networks},
388	  journal = {Nature Machine Intelligence},
389	  volume  = {2},
390	  pages   = {665--673},
391	  year    = {2020},
392	}
393	
394	@article{dong2026probing,
395	  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},
396	  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},
397	  journal      = {arXiv preprint arXiv:2602.01103},
398	  year         = {2026},
399	  eprint       = {2602.01103},
400	  archivePrefix = {arXiv},
401	}
402	
403	@article{yan2026spurious,
404	  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},
405	  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},
406	  journal      = {arXiv preprint arXiv:2601.11061},
407	  year         = {2026},
408	  eprint       = {2601.11061},
409	  archivePrefix = {arXiv},
410	}
411	
412	@article{tarek2025reward,
413	  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},
414	  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},
415	  journal      = {arXiv preprint arXiv:2509.15557},
416	  year         = {2025},
417	  eprint       = {2509.15557},
418	  archivePrefix = {arXiv},
419	}
420	
421	@inproceedings{yue2025rl-reasoning,
422	  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},
423	  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},
424	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
425	  year         = {2025},
426	  eprint       = {2504.13837},
427	  archivePrefix = {arXiv},
428	}
429	
430	@article{sullivan2025grpo-prm,
431	  author       = {Michael Sullivan and Alexander Koller},
432	  title        = {{GRPO} is Secretly a Process Reward Model},
433	  journal      = {arXiv preprint arXiv:2509.21154},
434	  year         = {2025},
435	  eprint       = {2509.21154},
436	  archivePrefix = {arXiv},
437	}
438	
439	% ============================================================
440	% R19 reviewer-requested references
441	% ============================================================
442	
443	@inproceedings{setlur2025rewarding,
444	  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},
445	  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},
446	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
447	  year         = {2025},
448	  note         = {arXiv:2410.08146},
449	}
450	
451	@article{alphaproof2025,
452	  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},
453	  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},
454	  journal      = {Nature},
455	  year         = {2025},
456	  doi          = {10.1038/s41586-025-09833-y},
457	}
458	
459	% ============================================================
460	% Solvers (Prover9, SWI-Prolog)
461	% ============================================================
462	
463	@article{deepseek-prover-v2,
464	  author       = {{DeepSeek-AI}},
465	  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},
466	  journal      = {arXiv preprint arXiv:2504.21801},
467	  year         = {2025},
468	  eprint       = {2504.21801},
469	  archivePrefix = {arXiv},
470	}
471	
472	@article{cui2025prime,
473	  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},
474	  title        = {{Process Reinforcement through Implicit Rewards}},
475	  journal      = {arXiv preprint arXiv:2502.01456},
476	  year         = {2025},
477	  eprint       = {2502.01456},
478	  archivePrefix = {arXiv},
479	  primaryClass = {cs.CL},
480	}
481	
482	@misc{mccune-prover9,
483	  author       = {William McCune},
484	  title        = {{Prover9 and Mace4}},
485	  year         = {2005--2010},
486	  howpublished = {\url{https://www.cs.unm.edu/~mccune/prover9/}},
487	  note         = {Version 2009-11A},
488	}
489	
490	@inproceedings{lundberg2017unified,
491	  author       = {Scott M. Lundberg and Su-In Lee},
492	  title        = {A Unified Approach to Interpreting Model Predictions},
493	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
494	  year         = {2017},
495	}
496	
497	@inproceedings{coste2023reward,
498	  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},
499	  title        = {Reward Model Ensembles Help Mitigate Overoptimization},
500	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
501	  year         = {2024},
502	  note         = {arXiv:2310.02743},
503	}
504	
505	@inproceedings{moskovitz2023confronting,
506	  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},
507	  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},
508	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
509	  year         = {2024},
510	  note         = {arXiv:2310.04373},
511	}
512	
513	@article{wielemaker2012swi,
514	  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\"o}rn Lager},
515	  title        = {{SWI-Prolog}},
516	  journal      = {Theory and Practice of Logic Programming},
517	  volume       = {12},
518	  number       = {1--2},
519	  pages        = {67--96},
520	  year         = {2012},
521	  doi          = {10.1017/S1471068411000494},
522	}
523	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "ce4ed1a0-5dcb-4935-98c0-ccf140af2a5a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% LLaMA\n% ============================================================\n\n@article{grattafiori2024llama,\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},\n  title = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n  eprint = {2407.21783},\n  archiveprefix = {arXiv},\n}\n\n% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2404.18926},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2501.12948},\n  year         = {2025},\n  eprint       = {2501.12948},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nlproofs,\n  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},\n  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},\n  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2022},\n  eprint       = {2205.12443},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{vstar,\n  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},\n  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},\n  booktitle    = {Conference on Language Modeling (COLM)},\n  year         = {2024},\n  eprint       = {2402.06457},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{easy-to-hard,\n  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},\n  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  eprint       = {2403.09472},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR Technical Blog},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{prooffol-thatikonda2024,\n  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},\n  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},\n  journal      = {arXiv preprint arXiv:2409.16461},\n  year         = {2024},\n  eprint       = {2409.16461},\n  archivePrefix = {arXiv},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@article{helff2026gaming,\n  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\\\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},\n  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},\n  journal      = {arXiv preprint arXiv:2604.15149},\n  year         = {2026},\n  eprint       = {2604.15149},\n  archivePrefix = {arXiv},\n}\n\n@article{khalifa2026countdown,\n  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},\n  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},\n  journal      = {arXiv preprint arXiv:2603.07084},\n  year         = {2026},\n  eprint       = {2603.07084},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{uesato2022solving,\n  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  booktitle={NeurIPS 2022 Workshop on MATH-AI},\n  year={2022}\n}\n\n@article{cobbe2021training,\n  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},\n  title        = {{Training Verifiers to Solve Math Word Problems}},\n  journal      = {arXiv preprint arXiv:2110.14168},\n  year         = {2021},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{pronesti2026beyond,\n  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},\n  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},\n  journal      = {arXiv preprint arXiv:2601.17223},\n  year         = {2026},\n  eprint       = {2601.17223},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{ng1999policy,\n  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},\n  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {1999},\n  pages     = {278--287},\n}\n\n@article{geirhos2020shortcut,\n  author  = {Robert Geirhos and J{\\\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},\n  title   = {Shortcut Learning in Deep Neural Networks},\n  journal = {Nature Machine Intelligence},\n  volume  = {2},\n  pages   = {665--673},\n  year    = {2020},\n}\n\n@article{dong2026probing,\n  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},\n  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},\n  journal      = {arXiv preprint arXiv:2602.01103},\n  year         = {2026},\n  eprint       = {2602.01103},\n  archivePrefix = {arXiv},\n}\n\n@article{yan2026spurious,\n  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},\n  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},\n  journal      = {arXiv preprint arXiv:2601.11061},\n  year         = {2026},\n  eprint       = {2601.11061},\n  archivePrefix = {arXiv},\n}\n\n@article{tarek2025reward,\n  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},\n  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},\n  journal      = {arXiv preprint arXiv:2509.15557},\n  year         = {2025},\n  eprint       = {2509.15557},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yue2025rl-reasoning,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},\n  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  eprint       = {2504.13837},\n  archivePrefix = {arXiv},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO} is Secretly a Process Reward Model},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% R19 reviewer-requested references\n% ============================================================\n\n@inproceedings{setlur2025rewarding,\n  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},\n  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2410.08146},\n}\n\n@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n% ============================================================\n% Solvers (Prover9, SWI-Prolog)\n% ============================================================\n\n@article{deepseek-prover-v2,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},\n  journal      = {arXiv preprint arXiv:2504.21801},\n  year         = {2025},\n  eprint       = {2504.21801},\n  archivePrefix = {arXiv},\n}\n\n@article{cui2025prime,\n  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},\n  title        = {{Process Reinforcement through Implicit Rewards}},\n  journal      = {arXiv preprint arXiv:2502.01456},\n  year         = {2025},\n  eprint       = {2502.01456},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@misc{mccune-prover9,\n  author       = {William McCune},\n  title        = {{Prover9 and Mace4}},\n  year         = {2005--2010},\n  howpublished = {\\url{https://www.cs.unm.edu/~mccune/prover9/}},\n  note         = {Version 2009-11A},\n}\n\n@inproceedings{lundberg2017unified,\n  author       = {Scott M. Lundberg and Su-In Lee},\n  title        = {A Unified Approach to Interpreting Model Predictions},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2017},\n}\n\n@inproceedings{coste2023reward,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {Reward Model Ensembles Help Mitigate Overoptimization},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.02743},\n}\n\n@inproceedings{moskovitz2023confronting,\n  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},\n  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n",
      "numLines": 523,
      "startLine": 1,
      "totalLines": 523
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Both directories have identical content. Now I'll make all the edits. Let me plan:

**P1-A**: Temper causal language in experiments.tex
- L26: "that reveals structural degeneration" → "consistent with structural degeneration"
- L27: "confirming degeneration independent" → "indicating degeneration independent"  
- L35: "confirming that hacking modes are absent" → "indicating that hacking modes are absent"

Wait, let me search more carefully for strong causal words. Let me scan:

L26: "reveals structural degeneration" - YES, change to "consistent with structural degeneration"


L27: "confirming degeneration" - this is OK-ish but could be softened
L32: "confirming that structural degeneration requires" - strong
L35: "confirming that hacking modes are absent" - strong

The user wants only the 2-3 most prominent changes, so I'll focus on the clearest cases: L26 with "reveals," L32 with "confirming that structural degeneration requires," and L105 with "confirming STA's diagnostic transfer" since that's a strong causal claim.

For L26, changing "reveals" to "is consistent with" softens the overreach. For L32 and L105, "suggesting" instead of "confirming" acknowledges the inference is supported but not definitively proven. L32 is actually well-grounded in the data about non-converged seeds, so maybe that one stays. The clearest overreach is L26 "reveals" and L105 "confirming" the diagnostic transfer claim.

Let me settle on the three most prominent: L26 for the explicit user request, L105 because cross-domain claims need more caution, and L32 because the causal mechanism claim is strong. Now I need to check the Table 1 caption.

Looking at the LaTeX file around line 70, I can see the caption ends with a reference to the appendix. I need to insert a note about ISR* being reported for completeness, clarifying that the mode-level analysis is in a specific section. The caption content sits inside the `\caption{}` command, so I'll add the new sentence before the closing brace, right after the appendix reference.

For the limitations section, I'm adding a sentence at the end of the existing paragraph about ISR's diagnostic value. Then I need to update the bibliography files and add a sentence to the related work section about reward hacking, placing it after the Goodhart effect discussion and before the mutation testing paragraph begins.

Now I'm making the three specific edits to experiments.tex in both directories—softening the language from "reveals" to "consistent with," changing "confirming" to "suggesting," and replacing "confirming" with "supporting" in the diagnostic transfer sentence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "6d3000b7-5d9e-4c55-bec8-8d0013637a00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYYy8X7BCw22Uo6PDTfVHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17032,
      "cache_read_input_tokens": 44249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17032
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

_source line 25_

Files are identical across both directories. Applying all edits now.

**P1-A**: experiments.tex — 3 causal language fixes (L26, L32, L105)
**P1-B**: experiments.tex — Table 1 caption ISR* note
**P1-C**: limitations.tex — reward family sentence
**P1-D**: references.bib + related_work.tex — Wilhelm citation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "aa0d85f7-e2ec-4c7a-92f8-fa85e614fee8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYYy8X7BCw22Uo6PDTfVHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17032,
      "cache_read_input_tokens": 44249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17032
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

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_0131kd2Ssa7wQocrSyGWsZUv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "old_string": "that reveals structural degeneration behind apparent success.",
  "new_string": "consistent with structural degeneration behind apparent success."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "65c92424-9d67-4ec6-8cbf-59ce051ba6e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYYy8X7BCw22Uo6PDTfVHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17032,
      "cache_read_input_tokens": 44249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17032
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

_source line 27 · 2026-05-22T15:46:51.329Z_

<details><summary>↩ Tool result · `toolu_0131kd2Ssa7wQocrSyGWsZUv`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "3ce83f5f-9c22-4845-93f8-9904c0a76e94",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "oldString": "that reveals structural degeneration behind apparent success.",
    "newString": "consistent with structural degeneration behind apparent success.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) that reveals structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Collapse trajectory.}",
          " Figure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.",
          "-As PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) that reveals structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42",
          "+As PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42",
          " By 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.",
          " A binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).",
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

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_0195PiAd2XpmAQjq7czg4QXH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "that reveals structural degeneration behind apparent success.",
  "new_string": "consistent with structural degeneration behind apparent success."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "8abc06d0-30d4-4685-a085-6ca1390bfa96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYYy8X7BCw22Uo6PDTfVHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17032,
      "cache_read_input_tokens": 44249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17032
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

_source line 29 · 2026-05-22T15:46:52.262Z_

<details><summary>↩ Tool result · `toolu_0195PiAd2XpmAQjq7czg4QXH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "46e8f8e7-7ba3-4b85-86d1-b2203b2fd7c9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "that reveals structural degeneration behind apparent success.",
    "newString": "consistent with structural degeneration behind apparent success.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) that reveals structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Collapse trajectory.}",
          " Figure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.",
          "-As PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) that reveals structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42",
          "+As PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42",
          " By 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.",
          " A binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).",
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_016HG3P9nvFJ1ajgJgkVtea9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "old_string": "and confirming that structural degeneration requires successful RL optimization as a prerequisite",
  "new_string": "and suggesting that structural degeneration requires successful RL optimization as a prerequisite"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "dbae8bcb-2a8e-425c-9f4d-8b79426cebf7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYYy8X7BCw22Uo6PDTfVHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17032,
      "cache_read_input_tokens": 44249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17032
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

_source line 31 · 2026-05-22T15:46:53.272Z_

<details><summary>↩ Tool result · `toolu_016HG3P9nvFJ1ajgJgkVtea9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "3f52b8d4-c9ff-4e5c-9d2e-6882d6ff01f4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "oldString": "and confirming that structural degeneration requires successful RL optimization as a prerequisite",
    "newString": "and suggesting that structural degeneration requires successful RL optimization as a prerequisite",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 7,
        "newStart": 29,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Cross-seed instability.}",
          " Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2",
          "-Two additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).",
          "+Two additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).",
          " ",
          " \\textbf{SFT baseline.}",
          " SFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization."
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

<details open><summary>🔧 Tool call — Edit · `toolu_01BwgTrVg1BPG3dzWtL1Z4dg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "and confirming that structural degeneration requires successful RL optimization as a prerequisite",
  "new_string": "and suggesting that structural degeneration requires successful RL optimization as a prerequisite"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "e6472998-b23f-4ad4-8d2b-63f4e9325f02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYYy8X7BCw22Uo6PDTfVHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17032,
      "cache_read_input_tokens": 44249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17032
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

_source line 33 · 2026-05-22T15:46:54.690Z_

<details><summary>↩ Tool result · `toolu_01BwgTrVg1BPG3dzWtL1Z4dg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "ca5b061c-f06e-48b8-bd49-aad58d60480d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "and confirming that structural degeneration requires successful RL optimization as a prerequisite",
    "newString": "and suggesting that structural degeneration requires successful RL optimization as a prerequisite",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 7,
        "newStart": 29,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Cross-seed instability.}",
          " Three seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2",
          "-Two additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and confirming that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).",
          "+Two additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).",
          " ",
          " \\textbf{SFT baseline.}",
          " SFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization."
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

<details open><summary>🔧 Tool call — Edit · `toolu_019ZZJ3Woefdrf4RyvdCohes`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "old_string": "confirming STA's diagnostic transfer across logic types.",
  "new_string": "supporting STA's diagnostic transfer across logic types."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "5d834550-cc92-4f1a-8f00-a68b27b31aad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYYy8X7BCw22Uo6PDTfVHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17032,
      "cache_read_input_tokens": 44249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17032
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

_source line 35 · 2026-05-22T15:46:55.579Z_

<details><summary>↩ Tool result · `toolu_019ZZJ3Woefdrf4RyvdCohes`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "fdc51338-1542-40d2-85f4-80ff263ff028",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "oldString": "confirming STA's diagnostic transfer across logic types.",
    "newString": "supporting STA's diagnostic transfer across logic types.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 102,
        "oldLines": 7,
        "newStart": 102,
        "newLines": 7,
        "lines": [
          " \\end{figure}",
          " ",
          " \\textbf{Prolog: universal Goodhart.}",
          "-Replicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.",
          "+Replicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.",
          " Under ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).",
          " Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.",
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01DJzpGQdS3cAxQaoy2936CW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "confirming STA's diagnostic transfer across logic types.",
  "new_string": "supporting STA's diagnostic transfer across logic types."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "c3ace2fe-ebe3-4e5a-8850-5cfdca7e05d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYYy8X7BCw22Uo6PDTfVHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17032,
      "cache_read_input_tokens": 44249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17032
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

_source line 37 · 2026-05-22T15:46:56.213Z_

<details><summary>↩ Tool result · `toolu_01DJzpGQdS3cAxQaoy2936CW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "5926af84-33e6-4225-9ba4-566d83d288ab",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "confirming STA's diagnostic transfer across logic types.",
    "newString": "supporting STA's diagnostic transfer across logic types.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 102,
        "oldLines": 7,
        "newStart": 102,
        "newLines": 7,
        "lines": [
          " \\end{figure}",
          " ",
          " \\textbf{Prolog: universal Goodhart.}",
          "-Replicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, confirming STA's diagnostic transfer across logic types.",
          "+Replicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.",
          " Under ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).",
          " Prolog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.",
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

_source line 38_

P1-A done. Now P1-B (Table 1 caption), P1-C (limitations), P1-D (bib + related_work).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "727c4bfe-c7ba-442e-96bb-68720a959adf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01HRv4UVrK6U2dRT1iH6thW4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "old_string": "(${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}",
  "new_string": "(${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "20db8694-c598-464d-a1be-87052dd23cac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 40 · 2026-05-22T15:47:03.886Z_

<details><summary>↩ Tool result · `toolu_01HRv4UVrK6U2dRT1iH6thW4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "fd0d3d86-394c-420d-b02c-da3efb339f6f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "oldString": "(${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}",
    "newString": "(${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 67,
        "oldLines": 7,
        "newStart": 67,
        "newLines": 7,
        "lines": [
          " Random & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}",
          "+\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}",
          " \\label{tab:goodhart-landscape}",
          " \\end{table*}",
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

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_01SxKf9Him4NVxECDCzFY3FR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "(${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}",
  "new_string": "(${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "992e40a4-c6c9-44ab-b795-956b74f816fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 42 · 2026-05-22T15:47:05.300Z_

<details><summary>↩ Tool result · `toolu_01SxKf9Him4NVxECDCzFY3FR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "3a54b99b-802b-4091-8f8e-0409a2a78932",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "(${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}",
    "newString": "(${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\\leq}7\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall unknown; 152-sample precision audit in Appendix~\\ref{app:hacking-modes}).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nAt $N{=}3$, seed-level tests achieve 80\\% power only for very large effects ($d{\\geq}3.0$); non-significant comparisons (e.g., prevalence $p{=}0.182$) are exploratory.\nAn $N{=}2$ sensitivity analysis excluding s43 confirms consistent patterns (Appendix~\\ref{app:n2-sensitivity}).\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory and underpowered.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) across 1000 training steps.\nAs PR climbs from $32\\%$ to $96\\%$, ISR$^*$ collapses from $0.642$ to $0.003$, a $214\\times$ raw drop (partially attributable to premise-count inflation; matched comparison yields $1.06\\times$, \\S\\ref{sec:goodhart}) consistent with structural degeneration behind apparent success. %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, $87\\%$ of proved samples embed the conclusion verbatim (CE), confirming degeneration independent of the ISR scalar.\nA binary variant testing only collective premise necessity misses the collapse entirely ($\\text{ISR}{=}1.0$ for all proved samples), confirming that per-component LOO testing is essential (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge into qualitatively different failure modes: conclusion embedding (s42), repetition collapse (s43), and tautological collapse (s44), yet all converge to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\nTwo additional seeds under identical conditions fail to converge ($\\text{PR}{\\approx}14\\%$; Appendix~\\ref{app:seed-convergence}), retaining genuine reasoning and suggesting that structural degeneration requires successful RL optimization as a prerequisite (Appendix~\\ref{app:llama-coldstart}).\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations produces $92\\%$ non-hacking outputs at $\\text{PR}{=}13\\%$ ($\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$), confirming that hacking modes are absent before RL optimization.\nSFT serves as a pre-RL reference rather than a PR-matched control; its low PR reflects minimal optimization pressure.\nEarly-training comparison supports this interpretation: at 100 steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ vs.\\ SFT's $8\\%$ at comparable PR (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe result is a regressional Goodhart pattern~\\citep{manheim-goodhart-taxonomy}: optimizing a structural proxy shifts the \\emph{composition} of failure modes without reducing their aggregate prevalence.\nISR converts conclusion embedding (CE) into tautological shortcuts (TS) rather than producing genuine reasoning (Table~\\ref{tab:goodhart-landscape}); the apparent ISR advantage collapses from $3.2\\times$ to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe multiplicative reward formulation conflates ISR signal with interaction effects; three controls constrain this confound: exec-only's convergence to pure hacking, the qualitative TS shift under ISR, and an additive variant that did not converge (Appendix~\\ref{app:setup}); the shuffled-ISR control partially addresses the coupling by preserving ISR's distribution while breaking sample-level semantics.\nThe shuffled-ISR control produces SFT-like outcomes ($87\\%$ non-hacking at low PR), consistent with the Goodhart effect requiring the sample-level ISR signal, not its distributional shape (corroborating rather than definitive given $N{=}46$ proved samples).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR (3-seed) & 0.1 & 77{\\scriptsize$\\pm$14} & $1.06\\times^\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nISR (5-seed) & 0.1 & 70{\\scriptsize$\\pm$19} & (0.63)$^\\ddagger$ & 54 & 18 & 23 \\\\ %% registry: plan002-additive-b01-s42--s46 (pooled)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$).}\nISR reward amplifies TS convergence: $71\\%$ of proved samples under ISR exhibit tautological shortcuts vs.\\ $14\\%$ under random ($\\text{OR}_{\\text{CMH}}{=}2.46$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nTS is the canonical Goodhart move: a single premise identical to the conclusion yields $\\text{ISR}\\geq 0.5$ by construction, directly satisfying the LOO metric (\\S\\ref{sec:taxonomy-method}).\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) spans $68$--$100\\%$ across both conditions; the composition shifts (CE dominates under random, TS under ISR) without reducing aggregate hacking (Figure~\\ref{fig:hacking-composition}).\n\n\\textbf{Premise-count confound.}\nRaw ISR$^*$ comparisons are inflated by premise minimization: ISR-trained models produce shorter formalizations, mechanically boosting the LOO fraction.\nAfter matching for premise count, the apparent $3.2\\times$ advantage shrinks to $1.06\\times$ (Appendix~\\ref{app:detailed-results}); non-hacking rates are indistinguishable ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D051 premise-count-matched analysis; D095 FINAL Fisher test\nThe asymmetry is compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence.\n\n\\textbf{Higher doses and temporal dynamics.}\nAny genuine reasoning under ISR $\\beta{=}0.1$ is transient: non-hacking drops from $17\\%$ to $2\\%$ by 1000 steps as TS escalates (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nHigher doses accelerate collapse: $\\beta{=}0.2$ eliminates all non-hacking; $\\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking, qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\nSeeds 45--46 were added after observing the 3-seed results to test whether the bimodal pattern replicates; the $4{\\times}2$ vs $2{\\times}4$ micro-batch decomposition is mathematically equivalent (Appendix~\\ref{app:detailed-results}).\n\n\\subsection{Cross-Domain and Cross-Dataset Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nReplicating the pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}), exec-only seeds collapse to $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding, supporting STA's diagnostic transfer across logic types.\nUnder ISR-as-reward, all three seeds reach $0\\%$ non-hacking through distinct mechanisms: clean TS (s42), degenerate syntax bypassing text-match classifiers (s43), and query-as-fact gaming (s44; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the residual genuine reasoning seen in FOL.\n\n\\textbf{ProofFOL exec-only: cross-dataset replication.}\nConverged seeds collapse to near-zero genuine reasoning, confirming STA's diagnostic across dataset families.\nThe dominant hacking mode shifts from CE (FOLIO) to TS (ProofFOL), showing that mode repertoire is dataset-specific while the degeneration phenomenon is universal.\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): dataset-dependent asymmetry.}\nISR reward on ProofFOL produces substantially higher genuine rates than exec-only ($p{=}0.10$, exploratory, underpowered; directional only; Table~\\ref{tab:prooffol-detailed}), though at lower PR, possibly reflecting insufficient training.\n\n\\textbf{Mechanism.}\nThe asymmetry follows from hacking geometry: on FOLIO, tautological shortcuts yield high ISR (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}); on ProofFOL, the dominant hacking mode embeds conclusions among many premises, yielding $\\text{ISR}{\\approx}0$ and rendering ISR reward effectively corrective.\nISR-as-reward inherits the dataset's hacking topology.\n\n\\paragraph{Cross-scale validation (Qwen3-8B).}\nQwen3-8B does not converge under exec-only GRPO ($\\text{PR}{=}14\\%$, $K{=}8$; $K{=}4$ produces zero gradient), consistent with degeneration requiring successful convergence (Appendix~\\ref{app:8b-results}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}). \\texttt{1k} denotes a mode observed only at the 1000-step checkpoint.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for the vast majority of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): CE (conclusion embedding), TS (conclusion duplication), and PG (premise-subset gaming).\nThe central pattern: \\emph{reward formulation determines which mode dominates but not whether hacking occurs}; all GRPO conditions produce overwhelming degeneration, while SFT achieves $92\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 67,
        "oldLines": 7,
        "newStart": 67,
        "newLines": 7,
        "lines": [
          " Random & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}).}",
          "+\\caption{Goodhart landscape across reward conditions. PR: prove rate; ISR$^*$: proved-only ISR; TS: tautological shortcut; CE: conclusion embedding; N-H: non-hacking. 3-seed rows: TS/CE/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ raw mean inflated by TS gaming; $1.06\\times$ is the premise-count-matched value relative to random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}); 5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$: 3-seed row uses s42--44; 5-seed row adds s45, s46 (${\\sim}55\\%$ non-hacking each; Appendix~\\ref{app:detailed-results}). ISR* reported for completeness; mode-level analysis (\\S\\ref{sec:goodhart}) provides the primary diagnostic.}",
          " \\label{tab:goodhart-landscape}",
          " \\end{table*}",
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

_source line 43_

<details open><summary>🔧 Tool call — Edit · `toolu_0114eXXqaApL6q9E18KH6W1f`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
  "old_string": "its diagnostic value is realized through the mode breakdown, not the scalar alone.",
  "new_string": "its diagnostic value is realized through the mode breakdown, not the scalar alone.\nAll ISR conditions use a single multiplicative reward family ($r_{\\text{exec}} \\cdot (1+\\beta\\,\\text{ISR})$); alternative formulations remain untested."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "85a02b93-e6e7-48e2-9385-eac603198e06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 44 · 2026-05-22T15:47:09.219Z_

<details><summary>↩ Tool result · `toolu_0114eXXqaApL6q9E18KH6W1f`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "74b517cd-b67f-47dc-837d-461352e8f041",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex",
    "oldString": "its diagnostic value is realized through the mode breakdown, not the scalar alone.",
    "newString": "its diagnostic value is realized through the mode breakdown, not the scalar alone.\nAll ISR conditions use a single multiplicative reward family ($r_{\\text{exec}} \\cdot (1+\\beta\\,\\text{ISR})$); alternative formulations remain untested.",
    "originalFile": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\\ref{app:8b-results},~\\ref{app:llama-coldstart}), leaving cross-scale generalization untested.\nThree to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.\nStructural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\\% genuine; Appendix~\\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.\nOne of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\\ref{app:detailed-results}).\nISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 3,
        "newStart": 6,
        "newLines": 4,
        "lines": [
          " Structural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\\% genuine; Appendix~\\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.",
          " One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\\ref{app:detailed-results}).",
          " ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.",
          "+All ISR conditions use a single multiplicative reward family ($r_{\\text{exec}} \\cdot (1+\\beta\\,\\text{ISR})$); alternative formulations remain untested."
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_011BKw3SxnpjVfAk7LSwSumw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
  "old_string": "its diagnostic value is realized through the mode breakdown, not the scalar alone.",
  "new_string": "its diagnostic value is realized through the mode breakdown, not the scalar alone.\nAll ISR conditions use a single multiplicative reward family ($r_{\\text{exec}} \\cdot (1+\\beta\\,\\text{ISR})$); alternative formulations remain untested."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "1ac019e9-f612-421a-a5ed-d74a8033e315",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 46 · 2026-05-22T15:47:10.474Z_

<details><summary>↩ Tool result · `toolu_011BKw3SxnpjVfAk7LSwSumw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "7b46f7ed-a78c-48a7-bc77-7c9d35db3bad",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
    "oldString": "its diagnostic value is realized through the mode breakdown, not the scalar alone.",
    "newString": "its diagnostic value is realized through the mode breakdown, not the scalar alone.\nAll ISR conditions use a single multiplicative reward family ($r_{\\text{exec}} \\cdot (1+\\beta\\,\\text{ISR})$); alternative formulations remain untested.",
    "originalFile": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\\ref{app:8b-results},~\\ref{app:llama-coldstart}), leaving cross-scale generalization untested.\nThree to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.\nStructural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\\% genuine; Appendix~\\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.\nOne of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\\ref{app:detailed-results}).\nISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 3,
        "newStart": 6,
        "newLines": 4,
        "lines": [
          " Structural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\\% genuine; Appendix~\\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.",
          " One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\\ref{app:detailed-results}).",
          " ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.",
          "+All ISR conditions use a single multiplicative reward family ($r_{\\text{exec}} \\cdot (1+\\beta\\,\\text{ISR})$); alternative formulations remain untested."
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

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_01C39Qj22jjTZyxbLyttUU4L`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "old_string": "@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}",
  "new_string": "@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n\n@article{wilhelm2026monitoring,\n  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},\n  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},\n  journal={arXiv preprint arXiv:2603.04069},\n  year={2026}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "a0e7abb4-9a67-4de1-a4a3-bbec74ff64c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 48 · 2026-05-22T15:47:16.297Z_

<details><summary>↩ Tool result · `toolu_01C39Qj22jjTZyxbLyttUU4L`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "1d60618b-5a49-42b6-92f1-51bfeff00d96",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "oldString": "@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}",
    "newString": "@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n\n@article{wilhelm2026monitoring,\n  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},\n  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},\n  journal={arXiv preprint arXiv:2603.04069},\n  year={2026}\n}",
    "originalFile": "% ============================================================\n% LLaMA\n% ============================================================\n\n@article{grattafiori2024llama,\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},\n  title = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n  eprint = {2407.21783},\n  archiveprefix = {arXiv},\n}\n\n% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2404.18926},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2501.12948},\n  year         = {2025},\n  eprint       = {2501.12948},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nlproofs,\n  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},\n  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},\n  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2022},\n  eprint       = {2205.12443},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{vstar,\n  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},\n  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},\n  booktitle    = {Conference on Language Modeling (COLM)},\n  year         = {2024},\n  eprint       = {2402.06457},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{easy-to-hard,\n  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},\n  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  eprint       = {2403.09472},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR Technical Blog},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{prooffol-thatikonda2024,\n  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},\n  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},\n  journal      = {arXiv preprint arXiv:2409.16461},\n  year         = {2024},\n  eprint       = {2409.16461},\n  archivePrefix = {arXiv},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@article{helff2026gaming,\n  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\\\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},\n  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},\n  journal      = {arXiv preprint arXiv:2604.15149},\n  year         = {2026},\n  eprint       = {2604.15149},\n  archivePrefix = {arXiv},\n}\n\n@article{khalifa2026countdown,\n  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},\n  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},\n  journal      = {arXiv preprint arXiv:2603.07084},\n  year         = {2026},\n  eprint       = {2603.07084},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{uesato2022solving,\n  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  booktitle={NeurIPS 2022 Workshop on MATH-AI},\n  year={2022}\n}\n\n@article{cobbe2021training,\n  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},\n  title        = {{Training Verifiers to Solve Math Word Problems}},\n  journal      = {arXiv preprint arXiv:2110.14168},\n  year         = {2021},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{pronesti2026beyond,\n  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},\n  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},\n  journal      = {arXiv preprint arXiv:2601.17223},\n  year         = {2026},\n  eprint       = {2601.17223},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{ng1999policy,\n  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},\n  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {1999},\n  pages     = {278--287},\n}\n\n@article{geirhos2020shortcut,\n  author  = {Robert Geirhos and J{\\\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},\n  title   = {Shortcut Learning in Deep Neural Networks},\n  journal = {Nature Machine Intelligence},\n  volume  = {2},\n  pages   = {665--673},\n  year    = {2020},\n}\n\n@article{dong2026probing,\n  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},\n  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},\n  journal      = {arXiv preprint arXiv:2602.01103},\n  year         = {2026},\n  eprint       = {2602.01103},\n  archivePrefix = {arXiv},\n}\n\n@article{yan2026spurious,\n  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},\n  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},\n  journal      = {arXiv preprint arXiv:2601.11061},\n  year         = {2026},\n  eprint       = {2601.11061},\n  archivePrefix = {arXiv},\n}\n\n@article{tarek2025reward,\n  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},\n  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},\n  journal      = {arXiv preprint arXiv:2509.15557},\n  year         = {2025},\n  eprint       = {2509.15557},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yue2025rl-reasoning,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},\n  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  eprint       = {2504.13837},\n  archivePrefix = {arXiv},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO} is Secretly a Process Reward Model},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% R19 reviewer-requested references\n% ============================================================\n\n@inproceedings{setlur2025rewarding,\n  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},\n  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2410.08146},\n}\n\n@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n% ============================================================\n% Solvers (Prover9, SWI-Prolog)\n% ============================================================\n\n@article{deepseek-prover-v2,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},\n  journal      = {arXiv preprint arXiv:2504.21801},\n  year         = {2025},\n  eprint       = {2504.21801},\n  archivePrefix = {arXiv},\n}\n\n@article{cui2025prime,\n  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},\n  title        = {{Process Reinforcement through Implicit Rewards}},\n  journal      = {arXiv preprint arXiv:2502.01456},\n  year         = {2025},\n  eprint       = {2502.01456},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@misc{mccune-prover9,\n  author       = {William McCune},\n  title        = {{Prover9 and Mace4}},\n  year         = {2005--2010},\n  howpublished = {\\url{https://www.cs.unm.edu/~mccune/prover9/}},\n  note         = {Version 2009-11A},\n}\n\n@inproceedings{lundberg2017unified,\n  author       = {Scott M. Lundberg and Su-In Lee},\n  title        = {A Unified Approach to Interpreting Model Predictions},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2017},\n}\n\n@inproceedings{coste2023reward,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {Reward Model Ensembles Help Mitigate Overoptimization},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.02743},\n}\n\n@inproceedings{moskovitz2023confronting,\n  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},\n  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 520,
        "oldLines": 3,
        "newStart": 520,
        "newLines": 10,
        "lines": [
          "   year         = {2012},",
          "   doi          = {10.1017/S1471068411000494},",
          " }",
          "+",
          "+@article{wilhelm2026monitoring,",
          "+  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},",
          "+  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},",
          "+  journal={arXiv preprint arXiv:2603.04069},",
          "+  year={2026}",
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

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_0115an8uHrXnGB4du9boWdsG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "old_string": "@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}",
  "new_string": "@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n\n@article{wilhelm2026monitoring,\n  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},\n  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},\n  journal={arXiv preprint arXiv:2603.04069},\n  year={2026}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "81470f12-9690-4335-9d6c-dc166aabbb84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 50 · 2026-05-22T15:47:19.959Z_

<details><summary>↩ Tool result · `toolu_0115an8uHrXnGB4du9boWdsG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "781c8826-ee47-4d67-bd9d-3382c54afa1d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
    "oldString": "@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}",
    "newString": "@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n\n@article{wilhelm2026monitoring,\n  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},\n  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},\n  journal={arXiv preprint arXiv:2603.04069},\n  year={2026}\n}",
    "originalFile": "% ============================================================\n% LLaMA\n% ============================================================\n\n@article{grattafiori2024llama,\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},\n  title = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n  eprint = {2407.21783},\n  archiveprefix = {arXiv},\n}\n\n% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Fine-tuning LLMs via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2404.18926},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2501.12948},\n  year         = {2025},\n  eprint       = {2501.12948},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nlproofs,\n  author       = {Kaiyu Yang and Jia Deng and Danqi Chen},\n  title        = {{Generating Natural Language Proofs with Verifier-Guided Search}},\n  booktitle    = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2022},\n  eprint       = {2205.12443},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{vstar,\n  author       = {Arian Hosseini and Xingdi Yuan and Nikolay Malkin and Aaron Courville and Alessandro Sordoni and Rishabh Agarwal},\n  title        = {{V-STaR: Training Verifiers for Self-Taught Reasoners}},\n  booktitle    = {Conference on Language Modeling (COLM)},\n  year         = {2024},\n  eprint       = {2402.06457},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{easy-to-hard,\n  author       = {Zhiqing Sun and Longhui Yu and Yikang Shen and Weiyang Liu and Yiming Yang and Sean Welleck and Chuang Gan},\n  title        = {{Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  eprint       = {2403.09472},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {Sydney {Von Arx} and Lawrence Chan and Beth Barnes},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR Technical Blog},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{prooffol-thatikonda2024,\n  author       = {Ramya Keerthy Thatikonda and Jiuzhou Han and Wray Buntine and Ehsan Shareghi},\n  title        = {{Strategies for Improving NL-to-FOL Translation with LLMs: Data Generation, Incremental Fine-Tuning, and Verification}},\n  journal      = {arXiv preprint arXiv:2409.16461},\n  year         = {2024},\n  eprint       = {2409.16461},\n  archivePrefix = {arXiv},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@article{helff2026gaming,\n  author       = {Lukas Helff and Quentin Delfosse and David Steinmann and Ruben H{\\\"a}rle and Hikaru Shindo and Patrick Schramowski and Wolfgang Stammer and Kristian Kersting and Felix Friedrich},\n  title        = {{LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking}},\n  journal      = {arXiv preprint arXiv:2604.15149},\n  year         = {2026},\n  eprint       = {2604.15149},\n  archivePrefix = {arXiv},\n}\n\n@article{khalifa2026countdown,\n  author       = {Muhammad Khalifa and Zohaib Khan and Omer Tafveez and Hao Peng and Lu Wang},\n  title        = {{Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR}},\n  journal      = {arXiv preprint arXiv:2603.07084},\n  year         = {2026},\n  eprint       = {2603.07084},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{uesato2022solving,\n  title={{Solving Math Word Problems with Process- and Outcome-Based Feedback}},\n  author={Uesato, Jonathan and Kushman, Nate and Kumar, Ramana and Song, Francis and Siegel, Noah and Wang, Lisa and Creswell, Antonia and Irving, Geoffrey and Higgins, Irina},\n  booktitle={NeurIPS 2022 Workshop on MATH-AI},\n  year={2022}\n}\n\n@article{cobbe2021training,\n  author       = {Karl Cobbe and Vineet Kosaraju and Mohammad Bavarian and Mark Chen and Heewoo Jun and Lukasz Kaiser and Matthias Plappert and Jerry Tworek and Jacob Hilton and Reiichiro Nakano and Christopher Hesse and John Schulman},\n  title        = {{Training Verifiers to Solve Math Word Problems}},\n  journal      = {arXiv preprint arXiv:2110.14168},\n  year         = {2021},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@article{pronesti2026beyond,\n  author       = {Massimiliano Pronesti and Anya Belz and Yufang Hou},\n  title        = {{Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning}},\n  journal      = {arXiv preprint arXiv:2601.17223},\n  year         = {2026},\n  eprint       = {2601.17223},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{ng1999policy,\n  author    = {Andrew Y. Ng and Daishi Harada and Stuart Russell},\n  title     = {Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year      = {1999},\n  pages     = {278--287},\n}\n\n@article{geirhos2020shortcut,\n  author  = {Robert Geirhos and J{\\\"o}rn-Henrik Jacobsen and Claudio Michaelis and Richard Zemel and Wieland Brendel and Matthias Bethge and Felix A. Wichmann},\n  title   = {Shortcut Learning in Deep Neural Networks},\n  journal = {Nature Machine Intelligence},\n  volume  = {2},\n  pages   = {665--673},\n  year    = {2020},\n}\n\n@article{dong2026probing,\n  author       = {Yiming Dong and Kun Fu and Haoyu Li and Xinyuan Zhu and Yurou Liu and Lijing Shao and Jieping Ye and Zheng Wang},\n  title        = {{Probing RLVR Training Instability Through the Lens of Objective-Level Hacking}},\n  journal      = {arXiv preprint arXiv:2602.01103},\n  year         = {2026},\n  eprint       = {2602.01103},\n  archivePrefix = {arXiv},\n}\n\n@article{yan2026spurious,\n  author       = {Lecheng Yan and Ruizhe Li and Guanhua Chen and Qing Li and Jiahui Geng and Wenxi Li and Vincent Wang and Chris Lee},\n  title        = {{Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs}},\n  journal      = {arXiv preprint arXiv:2601.11061},\n  year         = {2026},\n  eprint       = {2601.11061},\n  archivePrefix = {arXiv},\n}\n\n@article{tarek2025reward,\n  author       = {Mirza Farhan Bin Tarek and Rahmatollah Beheshti},\n  title        = {{Reward Hacking Mitigation using Verifiable Composite Rewards}},\n  journal      = {arXiv preprint arXiv:2509.15557},\n  year         = {2025},\n  eprint       = {2509.15557},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yue2025rl-reasoning,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Shiji Song and Gao Huang},\n  title        = {Does Reinforcement Learning Really Incentivize Reasoning Capacity in {LLMs} Beyond the Base Model?},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  eprint       = {2504.13837},\n  archivePrefix = {arXiv},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO} is Secretly a Process Reward Model},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% R19 reviewer-requested references\n% ============================================================\n\n@inproceedings{setlur2025rewarding,\n  author       = {Amrith Setlur and Chirag Nagpal and Adam Fisch and Xinyang Geng and Jacob Eisenstein and Rishabh Agarwal and Alekh Agarwal and Jonathan Berant and Aviral Kumar},\n  title        = {{Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2410.08146},\n}\n\n@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n% ============================================================\n% Solvers (Prover9, SWI-Prolog)\n% ============================================================\n\n@article{deepseek-prover-v2,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition}},\n  journal      = {arXiv preprint arXiv:2504.21801},\n  year         = {2025},\n  eprint       = {2504.21801},\n  archivePrefix = {arXiv},\n}\n\n@article{cui2025prime,\n  author       = {Ganqu Cui and Lifan Yuan and Zefan Wang and Hanbin Wang and Yuchen Zhang and Jiacheng Chen and Wendi Li and Bingxiang He and Yuchen Fan and Tianyu Yu and Qixin Xu and Weize Chen and Jiarui Yuan and Huayu Chen and Kaiyan Zhang and Xingtai Lv and Shuo Wang and Yuan Yao and Xu Han and Hao Peng and Yu Cheng and Zhiyuan Liu and Maosong Sun and Bowen Zhou and Ning Ding},\n  title        = {{Process Reinforcement through Implicit Rewards}},\n  journal      = {arXiv preprint arXiv:2502.01456},\n  year         = {2025},\n  eprint       = {2502.01456},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@misc{mccune-prover9,\n  author       = {William McCune},\n  title        = {{Prover9 and Mace4}},\n  year         = {2005--2010},\n  howpublished = {\\url{https://www.cs.unm.edu/~mccune/prover9/}},\n  note         = {Version 2009-11A},\n}\n\n@inproceedings{lundberg2017unified,\n  author       = {Scott M. Lundberg and Su-In Lee},\n  title        = {A Unified Approach to Interpreting Model Predictions},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2017},\n}\n\n@inproceedings{coste2023reward,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {Reward Model Ensembles Help Mitigate Overoptimization},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.02743},\n}\n\n@inproceedings{moskovitz2023confronting,\n  author       = {Ted Moskovitz and Aldo Pacchiano and Parker Lund and Jakob Foerster},\n  title        = {Confronting Reward Model Overoptimization with Constrained {RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@article{wielemaker2012swi,\n  author       = {Jan Wielemaker and Tom Schrijvers and Markus Triska and Torbj{\\\"o}rn Lager},\n  title        = {{SWI-Prolog}},\n  journal      = {Theory and Practice of Logic Programming},\n  volume       = {12},\n  number       = {1--2},\n  pages        = {67--96},\n  year         = {2012},\n  doi          = {10.1017/S1471068411000494},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 520,
        "oldLines": 3,
        "newStart": 520,
        "newLines": 10,
        "lines": [
          "   year         = {2012},",
          "   doi          = {10.1017/S1471068411000494},",
          " }",
          "+",
          "+@article{wilhelm2026monitoring,",
          "+  title={Monitoring Emergent Reward Hacking During Generation via Internal Activations},",
          "+  author={Wilhelm, Patrick and Wittkopp, Thorsten and Kao, Odej},",
          "+  journal={arXiv preprint arXiv:2603.04069},",
          "+  year={2026}",
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

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Edit · `toolu_01FtRJxxpjXSEhtqHgtLCEVq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
  "old_string": "its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.",
  "new_string": "its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\nComplementarily, \\citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "14ccf253-96bd-41ad-9c44-dd16d88c4926",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 52 · 2026-05-22T15:47:23.251Z_

<details><summary>↩ Tool result · `toolu_01FtRJxxpjXSEhtqHgtLCEVq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "caa88e76-4d61-403d-acd1-44aba9cab063",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
    "oldString": "its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.",
    "newString": "its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\nComplementarily, \\citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.\nIn mathematical reasoning, learned process reward models~\\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\\citep{processbench}.\nA recurring finding is that auxiliary rewards can hurt rather than help: \\citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \\citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.\nAnnotation-free alternatives~\\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\nMost closely related, \\citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.\nReward model ensembles~\\citep{coste2023reward} and constrained optimization~\\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.\nConcurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond}; \\citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.\nWhile IPT perturbs \\emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \\emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nOur Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\\beta$; its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 6,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          " While IPT perturbs \\emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \\emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.",
          " \\citet{khalifa2026countdown} provide RLVR hacking testbeds.",
          " Our Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\\beta$; its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.",
          "+Complementarily, \\citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.",
          " ",
          " \\paragraph{Mutation testing.}",
          " STA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive."
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

_source line 53_

<details open><summary>🔧 Tool call — Edit · `toolu_01HddQxv2xyuMB7f7skRq4kE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "old_string": "its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.",
  "new_string": "its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\nComplementarily, \\citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "3ed1d9dd-31d0-4bc3-aa80-4d2765aa1029",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBdRy7oZe6BWnkF5BLAiSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2687,
      "cache_read_input_tokens": 61281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2687
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

_source line 54 · 2026-05-22T15:47:24.593Z_

<details><summary>↩ Tool result · `toolu_01HddQxv2xyuMB7f7skRq4kE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "9d79587c-264c-4113-9b27-535f9e6279d6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "oldString": "its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.",
    "newString": "its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\nComplementarily, \\citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.\nAlphaProof~\\citep{alphaproof2025} and DeepSeek-Prover-V2~\\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nReward shaping theory~\\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.\nIn mathematical reasoning, learned process reward models~\\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\\citep{processbench}.\nA recurring finding is that auxiliary rewards can hurt rather than help: \\citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \\citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.\nAnnotation-free alternatives~\\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.\n\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF~\\citep{gao-reward-overoptimization} and logical formalization~\\citep{bondarenko-spec-gaming, kim-game-formalization}.\nMost closely related, \\citet{kim-game-formalization} document inference-time gaming on FOLIO with frontier models and Lean~4; our work is complementary in studying training-time degeneration with component necessity rather than faithfulness, and combining STA with inference-time detection would provide full gaming coverage.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes catastrophic Goodhart where KL regularization provably fails, a theoretical lens for why GRPO's KL penalty does not prevent our observed collapse.\nReward model ensembles~\\citep{coste2023reward} and constrained optimization~\\citep{moskovitz2023confronting} address overoptimization at the reward level; STA instead diagnoses structural consequences at the output level.\nConcurrent work documents spurious signals in RLVR~\\citep{spurious-rewards, yan2026spurious, dong2026probing, metr-reward-hacking} and proposes composite rewards as mitigations~\\citep{tarek2025reward, pronesti2026beyond}; \\citet{yue2025rl-reasoning} show RLVR redistributes base-model probability mass rather than creating new reasoning, consistent with our finding that GRPO exploits existing shortcuts.\n\\citet{helff2026gaming} propose Input Perturbation Testing (IPT) for gaming detection; STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training.\nWhile IPT perturbs \\emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \\emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.\n\\citet{khalifa2026countdown} provide RLVR hacking testbeds.\nOur Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\\beta$; its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive.\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 6,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          " While IPT perturbs \\emph{inputs} to detect inference-time gaming, STA performs leave-one-out ablation on \\emph{solver-input components} to diagnose training-time structural degeneration, operating at component-level rather than input-level granularity and targeting the training process rather than deployment behavior.",
          " \\citet{khalifa2026countdown} provide RLVR hacking testbeds.",
          " Our Goodhart effect follows the regressional pattern~\\citep{manheim-goodhart-taxonomy} on FOLIO, with extremal dynamics at high $\\beta$; its application to a diagnostic designed to \\emph{detect} gaming, and the dataset-dependent asymmetry it reveals, are to our knowledge novel.",
          "+Complementarily, \\citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.",
          " ",
          " \\paragraph{Mutation testing.}",
          " STA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; novelty lies in application and findings, not in the perturbation primitive."
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

_source line 55_

全部完成。修改汇总：

### P1-A: 因果语言（experiments.tex, 两个目录）
| 位置 | before | after |
|------|--------|-------|
| L26 | `that reveals structural degeneration` | `consistent with structural degeneration` |
| L32 | `and confirming that structural degeneration requires` | `and suggesting that structural degeneration requires` |
| L105 | `confirming STA's diagnostic transfer` | `supporting STA's diagnostic transfer` |

### P1-B: Table 1 caption（experiments.tex:L70, 两个目录）
caption 末尾增加：`ISR* reported for completeness; mode-level analysis (\S\ref{sec:goodhart}) provides the primary diagnostic.`

### P1-C: Limitations（limitations.tex:L9, 两个目录）
末尾新增一句：`All ISR conditions use a single multiplicative reward family ($r_{\text{exec}} \cdot (1+\beta\,\text{ISR})$); alternative formulations remain untested.`

### P1-D: Wilhelm 引用（两个目录）
- **references.bib**: 末尾添加 `wilhelm2026monitoring` 条目
- **related_work.tex:L26**: Reward hacking 段尾新增：`Complementarily, \citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "uuid": "b13f715d-d704-49c5-a3dd-68fd7e9d9d07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E46phbWYywhAPU8zY8gDHf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2910,
      "cache_read_input_tokens": 63968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2910
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

_source line 56_

全部完成。修改汇总：

### P1-A: 因果语言（experiments.tex, 两个目录）
| 位置 | before | after |
|------|--------|-------|
| L26 | `that reveals structural degeneration` | `consistent with structural degeneration` |
| L32 | `and confirming that structural degeneration requires` | `and suggesting that structural degeneration requires` |
| L105 | `confirming STA's diagnostic transfer` | `supporting STA's diagnostic transfer` |

### P1-B: Table 1 caption（experiments.tex:L70, 两个目录）
caption 末尾增加：`ISR* reported for completeness; mode-level analysis (\S\ref{sec:goodhart}) provides the primary diagnostic.`

### P1-C: Limitations（limitations.tex:L9, 两个目录）
末尾新增一句：`All ISR conditions use a single multiplicative reward family ($r_{\text{exec}} \cdot (1+\beta\,\text{ISR})$); alternative formulations remain untested.`

### P1-D: Wilhelm 引用（两个目录）
- **references.bib**: 末尾添加 `wilhelm2026monitoring` 条目
- **related_work.tex:L26**: Reward hacking 段尾新增：`Complementarily, \citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 97950,
  "duration_api_ms": 98923,
  "num_turns": 23,
  "stop_reason": "end_turn",
  "session_id": "759fd123-8c37-4b16-ae7f-2821db2c96ab",
  "total_cost_usd": 0.59226525,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 55037,
    "cache_read_input_tokens": 208554,
    "output_tokens": 5621,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 55037,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 379,
        "cache_read_input_tokens": 63968,
        "cache_creation_input_tokens": 2910,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2910
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3357,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003447,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 5621,
      "cacheReadInputTokens": 208554,
      "cacheCreationInputTokens": 55037,
      "webSearchRequests": 0,
      "costUSD": 0.5888182499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "83eecef4-f4aa-4c56-8f16-df739f91b9ea"
}
```

</details>

---
