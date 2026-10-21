# qa consistency audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 2
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_qa_consistency-audit_20260515T212632.log`
- **Structured JSON:** [`de5c2cb9122ea1527167.json`](../../sessions/de/de5c2cb9122ea1527167.json)

## Before a recorded user message

13 recorded events

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
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
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
  "uuid": "aead9186-84a1-46e3-a898-c2df884e1ae1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778889000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2eee4edf-c4e2-40e6-9abd-ef2f10b59176",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a cross-chapter consistency audit of their paper, focusing on Figure 3 vs Table 1 data consistency. Let me start by reading the relevant files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "0aff36e4-f1a1-4093-9e5d-045edb22e194",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fgVfhUvUQ8Bc24WqTMRXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14363,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14363
      },
      "output_tokens": 47,
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

I'll read the key files in parallel to perform the consistency audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "60ed4848-7650-44e5-a98b-fe3cc72a7b1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fgVfhUvUQ8Bc24WqTMRXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14363,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14363
      },
      "output_tokens": 47,
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

<details open><summary>🔧 Tool call — Read · `toolu_01JouZdxmy3eKkQvjWoGHJYa`</summary>

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
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "8efd74cd-a8ff-4c12-b0da-04ec7243d16b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fgVfhUvUQ8Bc24WqTMRXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14363,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14363
      },
      "output_tokens": 47,
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

_source line 7 · 2026-05-15T21:26:46.900Z_

<details><summary>↩ Tool result · `toolu_01JouZdxmy3eKkQvjWoGHJYa`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
10	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
11	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.
12	
13	\subsection{ISR as Diagnostic}
14	\label{sec:diagnostic}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
19	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
20	\label{fig:isr-collapse}
21	\end{figure}
22	
23	\textbf{Collapse trajectory.}
24	Figure~\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
25	PR rises $32\%\to93\%\to96\%$, a trajectory execution-only evaluation would read as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
26	By 500 steps, 87.1\% of proved samples embed the conclusion (H1); by 1000 steps the embedding rate saturates at 100\% and mean component count more than doubles ($6.58\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.
27	Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
28	
29	\textbf{Cross-seed instability.}
30	The three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\ref{app:detailed-results}): s42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{H1}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ via repetition (87\% of rollouts truncated); s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{H7}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
31	The cross-seed PR variance ($\sigma{=}47$\,pp) shows aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).
32	By 1000 steps, all three converge to high PR ($0.95{\pm}0.05$) but $0\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\ref{app:h8} and Table~\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2
33	
34	\textbf{SFT baseline.}
35	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $\text{H7}{=}0$, $\text{H1}{=}7.7\%$, $92.3\%$ non-hacking ($n{=}39$; per-seed range 91--93\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
36	The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.
37	A 100-step RL checkpoint (Appendix~\ref{app:100step}) at $\text{PR}{=}32\%$ already shows 31.2\% hacking (vs.\ SFT's 7.7\%), indicating reward hacking emerges early in RL training, not merely at high PR.
38	
39	\subsection{Meta-Level Goodhart's Law}
40	\label{sec:goodhart}
41	
42	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with a matched random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$, $u\sim\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.
43	The headline finding: ISR-as-reward produces \emph{meta-level} Goodhart~\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\resizebox{\columnwidth}{!}{%
49	\begin{tabular}{lcccccc}
50	\toprule
51	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
52	\midrule
53	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
54	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
55	\midrule
56	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
57	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
58	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
59	\midrule
60	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 12 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)
61	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
62	\bottomrule
63	\end{tabular}}
64	\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random H7 driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}.}
65	\label{tab:goodhart-landscape}
66	\end{table}
67	
68	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-amplified gaming.}
69	H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\sim}5\times$: $70.6\%$ ($163/231$) under ISR vs.\ $13.7\%$ ($36/262$) under random (Fisher $p{=}1.3{\times}10^{-39}$, $\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL
70	Random H7 is highly seed-dependent: $38.3\%$ in seed~43 vs.\ $0\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\%$, Table~\ref{tab:fol-detailed}).
71	H7---a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction (\S\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.
72	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$100\%$ across both conditions, and is in fact \emph{higher} under random (pooled H1 $71\%$ vs.\ $18\%$ under ISR).
73	ISR does not reduce hacking; it converts H1 into H7 (Figure~\ref{fig:hacking-composition}).
74	Random also yields higher and more stable PR ($87{\pm}8\%$ vs.\ $77{\pm}14\%$).
75	
76	\textbf{Premise-count confound.}
77	The one ISR seed not dominated by H7 (s42) has raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ its random control ($0.131$), suggesting genuine improvement.
78	This appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\text{ISR}\geq 0.5$ by definition.
79	Restricting to non-hacking samples with $\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\text{ISR}^{*}{=}0.258$ for ISR vs.\ $0.243$ for random: a $1.06\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis
80	After reclassifying premise-subset gaming (H8; Appendix~\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\ref{app:hacking-modes}), ISR $\beta{=}0.1$ non-hacking rate ($6.06\%$, $14/231$) is numerically lower than random ($9.5\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, two-sided, n.s.; Wilson 95\% CI: ISR $[3.6\%, 9.9\%]$, Random $[6.5\%, 13.7\%]$; Appendix Table~\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test
81	The key asymmetry is not in non-hacking rates but in gaming \emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\geq}97\%$), while random H7 remains seed-dependent and H1-dominated.
82	The raw $3.2\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification
83	
84	\begin{figure}[t]
85	\centering
86	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
87	\caption{Training ISR trajectories across reward conditions. ISR $\beta{=}0.1$ seeds rise rapidly toward $\text{ISR}{\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\text{ISR}{\geq}0.5$ by construction), not genuine structural quality; random $\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}
88	\label{fig:training-isr-curves}
89	\end{figure}
90	
91	\textbf{Temporal collapse under ISR $\beta{=}0.1$.}
92	Figure~\ref{fig:training-isr-curves} traces training ISR across conditions.
93	Extended training (1000 steps) reveals that ISR $\beta{=}0.1$'s genuine rate at 500 steps ($17.3\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\%$ to $96.7\%$ while genuine rate collapses to $2.2\%$ ($n_{\text{comp}}$: $5.58{\to}2.89$).
94	The optimization converges to a fixed point where $\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.
95	This mirrors the exec-only 1000-step trajectory (\S\ref{sec:diagnostic}): both converge to ${\sim}0\%$ genuine proofs despite opposite ISR values ($0.88$ vs.\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
96	
97	\textbf{High-dose ISR ($\beta{=}0.3$): multi-modal Goodhart.}
98	At $\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\text{PR}{=}66{\pm}42\%$, spanning 18--95\%); each seed converges to a distinct pathway (Appendix~\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44
99	Seed~42: \emph{reward collapse} ($\text{PR}{=}18\%$), the classical pattern of~\citep{gao-reward-overoptimization}.
100	Seed~43: \emph{H1 shortcutting} ($\text{PR}{=}86\%$, $\text{H1}{=}69\%$, only $27\%$ non-hacking).
101	Seed~44: \emph{pure H7 meta-Goodhart} ($\text{PR}{=}95\%$, $\text{H7}{=}100\%$, $\text{ISR}^{*}{=}0.742$, $0\%$ non-hacking)---simultaneously gaming \emph{both} execution and structural metrics through the same construction.
102	The random control at $\beta{=}0.3$ is equally unstable ($\text{PR}{=}54{\pm}35\%$, spanning 23--92\%) with near-universal H1 hacking ($91\%$, pooled) and ${\leq}4\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, H7 meta-Goodhart) while random converges to H1-dominated hacking with sporadic H7 ($7\%$ pooled, $0$--$7$ H7a per seed) (Appendix~\ref{app:beta03}).
103	
104	\subsection{Cross-Logic Diagnostic Transfer}
105	\label{sec:crosslogic}
106	
107	\begin{figure}[t]
108	\centering
109	\includegraphics[width=0.95\columnwidth]{figures/fig4_prolog_comparison.pdf}
110	\caption{Cross-logic results. \textbf{Left}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
111	\label{fig:prolog-comparison}
112	\end{figure}
113	
114	We replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce meta-level Goodhart?
115	Detailed per-seed numbers are in Appendix Table~\ref{tab:prolog-detailed}.
116	
117	\textbf{Prolog exec-only: ISR catches redundancy across logics.}
118	Two of three seeds (s42, s43) show $\text{ISR}^{*}{\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3
119	Inspection reveals \emph{redundant coding}: ground facts repeated multiple times (e.g., \texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.
120	This is a different failure semantics from FOL exec-only (conclusion embedding), but $\text{ISR}^{*}$ flags both.
121	We are careful to distinguish: exec-only \emph{low} ISR signals \emph{redundancy}; ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (\S\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.
122	
123	\textbf{Prolog ISR-as-reward: universal Goodhart.}
124	The Prolog result is stronger than FOL: 3/3 seeds reach $0\%$ non-hacking via three distinct mechanisms (Figure~\ref{fig:prolog-comparison}).
125	Seed~42: clean H7 tautologies ($\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42
126	Seed~43: \emph{degenerate uppercase pseudo-Prolog} (e.g., \texttt{MARY\_IS\_AN\_AVA\-DEOTE.}); strict text-match returns $\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43
127	Seed~44: \emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \texttt{is\_the\_dog\_furry.} as both fact and query), with $95/97$ proved samples at $n_{\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44
128	Seed~44 evaded our initial strict classifier (reported $100\%$ genuine); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.
129	We attribute Prolog's stronger collapse to its simpler operational semantics: a broader gaming basin makes the genuine residual disappear---corroborating evidence for Claim 2.
130	
131	\subsection{Hacking Taxonomy}
132	\label{sec:taxonomy}
133	
134	\begin{figure}[t]
135	\centering
136	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
137	\caption{Hacking composition across reward conditions (proved samples; exec-only and SFT: seed~42; ISR and Random bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}
138	\label{fig:hacking-composition}
139	\end{figure}
140	
141	\begin{table}[t]
142	\centering
143	\small
144	\resizebox{\columnwidth}{!}{%
145	\begin{tabular}{lccccc}
146	\toprule
147	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
148	\midrule
149	H1 embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
150	H7 duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
151	H8 prem-subset & 6  & 5  & 8   & 0 & --- \\
152	Tautological   & --- & --- & --- & --- & s42 \\
153	Repetition     & s43 & --- & --- & --- & --- \\
154	Contradiction  & 1k & --- & --- & --- & --- \\
155	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
156	Query-as-fact  & --- & --- & --- & --- & s44 \\
157	\midrule
158	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
159	\bottomrule
160	\end{tabular}}
161	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
162	\label{tab:hacking-taxonomy}
163	\end{table}
164	
165	The eight modes (Table~\ref{tab:hacking-taxonomy}; full definitions in Appendix~\ref{app:hacking-modes}) span the studied conditions.
166	Three are quantifiable across conditions: \textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\%$ regardless of reward type; \textbf{H7} (conclusion duplication) occurs under both ISR and random but ISR amplifies it ${\sim}5\times$ ($70.6\%$ vs.\ $13.7\%$ under random; Fisher $p{=}1.3{\times}10^{-39}$), with random H7 concentrated in a single seed (s43: $38.3\%$; s42, s44: $0\%$); \textbf{H8} (premise-subset gaming) appears under both exec-only ($6\%$) and ISR ($5\%$) conditions (Appendix~\ref{app:h8}).
167	H7 splits into \textbf{H7a} (standard, text-match detectable; $64.5\%$ of ISR proved, $149/231$) and \textbf{H7b} (obfuscated tautology; $6.06\%$, $14/231$): H7b samples use vacuous quantifier wrapping or structural simplification to evade the text-match classifier while remaining logically equivalent (s44: $11/12$ quantifier wrapping, $1/12$ structural; s43: $2$), with $10/12$ (s44) achieving $\text{ISR}{\approx}0.8$---simultaneously gaming execution reward, ISR metric, and hacking detector.
168	The remaining five appear in specific cells: tautological collapse (exec-only s44, Prolog ISR s42), repetition (exec-only s43), contradiction explosion (exec-only at 1000 steps), complexity-without-utility (random $\beta{=}0.1$ residual), and query-as-fact gaming (Prolog ISR s44).
169	
170	The cross-condition pattern is consistent with \S\ref{sec:goodhart}: \emph{reward formulation determines hacking composition but not hacking prevalence.}
171	Exec-only, ISR, and random conditions all show $\geq 80\%$ pooled hacking among proved samples; only SFT shows $92.3\%$ non-hacking.
172	Across 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is random $\beta{=}0.1$ s42 at $\text{PR}{=}79\%$, $22.8\%$ non-hacking, and ISR $\beta{=}0.1$ s42 at $\text{PR}{=}81\%$, $17.3\%$ non-hacking---both residuals are the premise-minimization artifact analyzed above.
173	Query-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "db42b27e-224d-4648-b841-ee2c5fe40224",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\\texttt{eval\\_sta.py}) so training-log ISR is never compared across runs.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory execution-only evaluation would read as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.95{\\pm}0.05$) but $0\\%$ non-hacking (15 samples escape text-match classifiers but are functionally degenerate; see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: H1 saturation; s43: H7 tautology; s44: H1+H8). %% registry: plan016-extended-1000-s42, plan001-exec-only-s43-1000-r2, plan001-exec-only-s44-1000-r2\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; per-seed range 91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific.\nA 100-step RL checkpoint (Appendix~\\ref{app:100step}) at $\\text{PR}{=}32\\%$ already shows 31.2\\% hacking (vs.\\ SFT's 7.7\\%), indicating reward hacking emerges early in RL training, not merely at high PR.\n\n\\subsection{Meta-Level Goodhart's Law}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nThe headline finding: ISR-as-reward produces \\emph{meta-level} Goodhart~\\citep{manheim-goodhart-taxonomy}---the diagnostic itself becomes the target of gaming.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 12 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random H7 driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-amplified gaming.}\nH7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\\sim}5\\times$: $70.6\\%$ ($163/231$) under ISR vs.\\ $13.7\\%$ ($36/262$) under random (Fisher $p{=}1.3{\\times}10^{-39}$, $\\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom H7 is highly seed-dependent: $38.3\\%$ in seed~43 vs.\\ $0\\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\\%$, Table~\\ref{tab:fol-detailed}).\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both conditions, and is in fact \\emph{higher} under random (pooled H1 $71\\%$ vs.\\ $18\\%$ under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$).\n\n\\textbf{Premise-count confound.}\nThe one ISR seed not dominated by H7 (s42) has raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ its random control ($0.131$), suggesting genuine improvement.\nThis appearance is a premise-minimization artifact: ISR-trained models produce shorter formalizations (mean $n{=}5.58$ vs.\\ $8.46$ for random), and ISR rises mechanically as $n$ falls---when $n{=}2$, $\\text{ISR}\\geq 0.5$ by definition.\nRestricting to non-hacking samples with $\\geq{3}$ premises (eliminating the trivial-$n$ regime) gives $\\text{ISR}^{*}{=}0.258$ for ISR vs.\\ $0.243$ for random: a $1.06\\times$ ratio, no meaningful advantage. %% D051 premise-count-matched analysis\nAfter reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:hacking-modes}), ISR $\\beta{=}0.1$ non-hacking rate ($6.06\\%$, $14/231$) is numerically lower than random ($9.5\\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, two-sided, n.s.; Wilson 95\\% CI: ISR $[3.6\\%, 9.9\\%]$, Random $[6.5\\%, 13.7\\%]$; Appendix Table~\\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test\nThe key asymmetry is not in non-hacking rates but in gaming \\emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\\geq}97\\%$), while random H7 remains seed-dependent and H1-dominated.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (meta-Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not genuine structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\textbf{Temporal collapse under ISR $\\beta{=}0.1$.}\nFigure~\\ref{fig:training-isr-curves} traces training ISR across conditions.\nExtended training (1000 steps) reveals that ISR $\\beta{=}0.1$'s genuine rate at 500 steps ($17.3\\%$, seed~42) is transient: by step 1000, H7 gaming escalates from $16.0\\%$ to $96.7\\%$ while genuine rate collapses to $2.2\\%$ ($n_{\\text{comp}}$: $5.58{\\to}2.89$).\nThe optimization converges to a fixed point where $\\text{ISR}^{*}{=}0.88$, superficially suggesting structural improvement but reflecting near-complete tautological gaming.\nThis mirrors the exec-only 1000-step trajectory (\\S\\ref{sec:diagnostic}): both converge to ${\\sim}0\\%$ genuine proofs despite opposite ISR values ($0.88$ vs.\\ $0.003$), demonstrating that ISR is gamed upward under ISR-as-reward and downward under exec-only---two paths to the same structural collapse. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR-as-reward produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$, spanning 18--95\\%); each seed converges to a distinct pathway (Appendix~\\ref{app:detailed-results}). %% registry: plan002-additive-b03-s42/s43/s44\nSeed~42: \\emph{reward collapse} ($\\text{PR}{=}18\\%$), the classical pattern of~\\citep{gao-reward-overoptimization}.\nSeed~43: \\emph{H1 shortcutting} ($\\text{PR}{=}86\\%$, $\\text{H1}{=}69\\%$, only $27\\%$ non-hacking).\nSeed~44: \\emph{pure H7 meta-Goodhart} ($\\text{PR}{=}95\\%$, $\\text{H7}{=}100\\%$, $\\text{ISR}^{*}{=}0.742$, $0\\%$ non-hacking)---simultaneously gaming \\emph{both} execution and structural metrics through the same construction.\nThe random control at $\\beta{=}0.3$ is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$, spanning 23--92\\%) with near-universal H1 hacking ($91\\%$, pooled) and ${\\leq}4\\%$ non-hacking per seed; high-dose proxy weighting destabilizes training regardless of signal source; ISR produces diverse failure modes (reward collapse, H1 shortcutting, H7 meta-Goodhart) while random converges to H1-dominated hacking with sporadic H7 ($7\\%$ pooled, $0$--$7$ H7a per seed) (Appendix~\\ref{app:beta03}).\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Left}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \\textbf{Right}: Prolog ISR-reward gaming-mode composition---all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog: (i) does ISR retain diagnostic value on a structurally different logic; (ii) does ISR-as-reward reproduce meta-level Goodhart?\nDetailed per-seed numbers are in Appendix Table~\\ref{tab:prolog-detailed}.\n\n\\textbf{Prolog exec-only: ISR catches redundancy across logics.}\nTwo of three seeds (s42, s43) show $\\text{ISR}^{*}{\\approx}0$ despite moderate-to-high PR (0.83, 0.56). %% registry: plan006-prolog-exec-s42, plan006-prolog-exec-s43-r3\nInspection reveals \\emph{redundant coding}: ground facts repeated multiple times (e.g., \\texttt{penguin(fido).} appearing three times), so per-clause LOO never breaks the proof.\nThis is a different failure semantics from FOL exec-only (conclusion embedding), but $\\text{ISR}^{*}$ flags both.\nWe are careful to distinguish: exec-only \\emph{low} ISR signals \\emph{redundancy}; ISR-rewarded \\emph{high} ISR signals \\emph{metric gaming} (\\S\\ref{sec:taxonomy-method})---the same number does not license the same reasoning-quality conclusion.\n\n\\textbf{Prolog ISR-as-reward: universal Goodhart.}\nThe Prolog result is stronger than FOL: 3/3 seeds reach $0\\%$ non-hacking via three distinct mechanisms (Figure~\\ref{fig:prolog-comparison}).\nSeed~42: clean H7 tautologies ($\\text{ISR}^{*}{=}1.0$, all $50/100$ proved). %% registry: plan006-prolog-sta-s42\nSeed~43: \\emph{degenerate uppercase pseudo-Prolog} (e.g., \\texttt{MARY\\_IS\\_AN\\_AVA\\-DEOTE.}); strict text-match returns $\\text{H7}{=}0$ but functional analysis shows all 38 proved samples have $n_{\\text{necessary}}{=}1$ (functionally H7). %% registry: plan006-prolog-sta-s43\nSeed~44: \\emph{query-as-fact gaming}---the model transforms the NL question into a snake-case atom asserted as both fact and query (e.g., \\texttt{is\\_the\\_dog\\_furry.} as both fact and query), with $95/97$ proved samples at $n_{\\text{necessary}}{=}1$. %% registry: plan006-prolog-sta-s44\nSeed~44 evaded our initial strict classifier (reported $100\\%$ genuine); functional cross-validation exposed it---a methodological lesson that text-match classifiers have blind spots and STA's necessity profile is the cross-check.\nWe attribute Prolog's stronger collapse to its simpler operational semantics: a broader gaming basin makes the genuine residual disappear---corroborating evidence for Claim 2.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only and SFT: seed~42; ISR and Random bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts H1 into more extreme H7 without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe eight modes (Table~\\ref{tab:hacking-taxonomy}; full definitions in Appendix~\\ref{app:hacking-modes}) span the studied conditions.\nThree are quantifiable across conditions: \\textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\\%$ regardless of reward type; \\textbf{H7} (conclusion duplication) occurs under both ISR and random but ISR amplifies it ${\\sim}5\\times$ ($70.6\\%$ vs.\\ $13.7\\%$ under random; Fisher $p{=}1.3{\\times}10^{-39}$), with random H7 concentrated in a single seed (s43: $38.3\\%$; s42, s44: $0\\%$); \\textbf{H8} (premise-subset gaming) appears under both exec-only ($6\\%$) and ISR ($5\\%$) conditions (Appendix~\\ref{app:h8}).\nH7 splits into \\textbf{H7a} (standard, text-match detectable; $64.5\\%$ of ISR proved, $149/231$) and \\textbf{H7b} (obfuscated tautology; $6.06\\%$, $14/231$): H7b samples use vacuous quantifier wrapping or structural simplification to evade the text-match classifier while remaining logically equivalent (s44: $11/12$ quantifier wrapping, $1/12$ structural; s43: $2$), with $10/12$ (s44) achieving $\\text{ISR}{\\approx}0.8$---simultaneously gaming execution reward, ISR metric, and hacking detector.\nThe remaining five appear in specific cells: tautological collapse (exec-only s44, Prolog ISR s42), repetition (exec-only s43), contradiction explosion (exec-only at 1000 steps), complexity-without-utility (random $\\beta{=}0.1$ residual), and query-as-fact gaming (Prolog ISR s44).\n\nThe cross-condition pattern is consistent with \\S\\ref{sec:goodhart}: \\emph{reward formulation determines hacking composition but not hacking prevalence.}\nExec-only, ISR, and random conditions all show $\\geq 80\\%$ pooled hacking among proved samples; only SFT shows $92.3\\%$ non-hacking.\nAcross 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is random $\\beta{=}0.1$ s42 at $\\text{PR}{=}79\\%$, $22.8\\%$ non-hacking, and ISR $\\beta{=}0.1$ s42 at $\\text{PR}{=}81\\%$, $17.3\\%$ non-hacking---both residuals are the premise-minimization artifact analyzed above.\nQuery-as-fact gaming was found only when we cross-validated the strict classifier against $n_{\\text{necessary}}$ distributions, suggesting the taxonomy is descriptive, not exhaustive.\n",
      "numLines": 174,
      "startLine": 1,
      "totalLines": 174
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_016mLAUkE7m5gSrdrTvwvUSA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/gen_fig3.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "8918ad5e-97b2-48d8-b121-2c3db1d6d8e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fgVfhUvUQ8Bc24WqTMRXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14363,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14363
      },
      "output_tokens": 47,
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

_source line 9 · 2026-05-15T21:26:47.186Z_

<details><summary>↩ Tool result · `toolu_016mLAUkE7m5gSrdrTvwvUSA`</summary>

```text
1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import numpy as np
5	
6	plt.rcParams.update({'pdf.fonttype': 42, 'ps.fonttype': 42})
7	
8	C_H7a = '#D55E00'
9	C_H7b = '#CC79A7'
10	C_H1 = '#E69F00'
11	C_H8 = '#56B4E9'
12	C_GENUINE = '#009E73'
13	
14	conditions = [
15	    'ISR $\\beta$=0.3',
16	    'ISR $\\beta$=0.1',
17	    'Random $\\beta$=0.3',
18	    'Random $\\beta$=0.1',
19	    'Exec-only',
20	    'SFT',
21	]
22	
23	# Order: ISR b0.3, ISR b0.1, Random b0.3, Random b0.1, Exec-only, SFT
24	raw = {
25	    'h7a':     [99, 161,  11,  36,   0,  0],
26	    'h7b':     [ 0,   2,   0,   0,   0,  0],
27	    'h1':      [73,  42, 149, 187,  81,  3],
28	    'h8':      [ 3,  12,   0,  14,   5,  0],
29	    'genuine': [24,  14,   3,  25,   7, 36],
30	}
31	
32	totals = [sum(raw[k][i] for k in raw) for i in range(len(conditions))]
33	# Verify: [199, 231, 163, 262, 93, 39]
34	
35	h7a     = [raw['h7a'][i]     / totals[i] * 100 for i in range(len(conditions))]
36	h7b     = [raw['h7b'][i]     / totals[i] * 100 for i in range(len(conditions))]
37	h1      = [raw['h1'][i]      / totals[i] * 100 for i in range(len(conditions))]
38	h8      = [raw['h8'][i]      / totals[i] * 100 for i in range(len(conditions))]
39	genuine = [raw['genuine'][i] / totals[i] * 100 for i in range(len(conditions))]
40	
41	y = np.arange(len(conditions))
42	bar_h = 0.55
43	
44	fig, ax = plt.subplots(figsize=(8, 4))
45	
46	kw = dict(height=bar_h, edgecolor='white', linewidth=0.5, zorder=3)
47	
48	left = np.zeros(len(conditions))
49	ax.barh(y, h7a, left=left, color=C_H7a, label='H7a (tautological)', **kw)
50	left += h7a
51	ax.barh(y, h7b, left=left, color=C_H7b, label='H7b (ISR-specific)', **kw)
52	left += h7b
53	ax.barh(y, h1, left=left, color=C_H1, label='H1 (shortcut)', **kw)
54	left += h1
55	ax.barh(y, h8, left=left, color=C_H8, label='H8 (conjunction)', **kw)
56	left += h8
57	ax.barh(y, genuine, left=left, color=C_GENUINE, label='Genuine', **kw)
58	left += genuine
59	
60	for i in range(len(conditions)):
61	    ax.text(102, y[i], f'n={totals[i]}', va='center', ha='left', fontsize=9, color='#444444')
62	
63	# ISR β=0.1 H7 vs Random β=0.1 H7
64	isr_h7 = h7a[1] + h7b[1]   # 70.6%
65	rand_h7 = h7a[3] + h7b[3]  # 13.7%
66	ax.annotate(
67	    f'ISR H7: {isr_h7:.1f}%\nvs Random: {rand_h7:.1f}%',
68	    xy=(rand_h7 / 2, y[3]),
69	    xytext=(55, y[2] + 0.6),
70	    fontsize=8.5, fontweight='bold', color=C_H7a,
71	    ha='center',
72	    arrowprops=dict(arrowstyle='->', color=C_H7a, lw=1.5),
73	)
74	
75	ax.set_yticks(y)
76	ax.set_yticklabels(conditions, fontsize=10)
77	ax.set_xlabel('Percentage of proved samples (%)', fontsize=11)
78	ax.set_xlim(0, 116)
79	ax.set_xticks([0, 20, 40, 60, 80, 100])
80	ax.spines['top'].set_visible(False)
81	ax.spines['right'].set_visible(False)
82	ax.tick_params(axis='both', labelsize=10)
83	ax.legend(fontsize=8.5, loc='upper right', frameon=False, ncol=2,
84	          bbox_to_anchor=(0.98, 0.42))
85	
86	fig.subplots_adjust(left=0.22, right=0.95, top=0.95, bottom=0.16)
87	
88	base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig3_hacking_composition'
89	fig.savefig(f'{base}.pdf', dpi=300, bbox_inches='tight', pad_inches=0.15)
90	fig.savefig(f'{base}.png', dpi=300, bbox_inches='tight', pad_inches=0.15)
91	plt.close()
92	print(f'Saved: {base}.pdf')
93	print(f'Saved: {base}.png')
94	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "7b9fc0ea-ff90-4b5c-8bcc-b9bd492c6e83",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/gen_fig3.py",
      "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nplt.rcParams.update({'pdf.fonttype': 42, 'ps.fonttype': 42})\n\nC_H7a = '#D55E00'\nC_H7b = '#CC79A7'\nC_H1 = '#E69F00'\nC_H8 = '#56B4E9'\nC_GENUINE = '#009E73'\n\nconditions = [\n    'ISR $\\\\beta$=0.3',\n    'ISR $\\\\beta$=0.1',\n    'Random $\\\\beta$=0.3',\n    'Random $\\\\beta$=0.1',\n    'Exec-only',\n    'SFT',\n]\n\n# Order: ISR b0.3, ISR b0.1, Random b0.3, Random b0.1, Exec-only, SFT\nraw = {\n    'h7a':     [99, 161,  11,  36,   0,  0],\n    'h7b':     [ 0,   2,   0,   0,   0,  0],\n    'h1':      [73,  42, 149, 187,  81,  3],\n    'h8':      [ 3,  12,   0,  14,   5,  0],\n    'genuine': [24,  14,   3,  25,   7, 36],\n}\n\ntotals = [sum(raw[k][i] for k in raw) for i in range(len(conditions))]\n# Verify: [199, 231, 163, 262, 93, 39]\n\nh7a     = [raw['h7a'][i]     / totals[i] * 100 for i in range(len(conditions))]\nh7b     = [raw['h7b'][i]     / totals[i] * 100 for i in range(len(conditions))]\nh1      = [raw['h1'][i]      / totals[i] * 100 for i in range(len(conditions))]\nh8      = [raw['h8'][i]      / totals[i] * 100 for i in range(len(conditions))]\ngenuine = [raw['genuine'][i] / totals[i] * 100 for i in range(len(conditions))]\n\ny = np.arange(len(conditions))\nbar_h = 0.55\n\nfig, ax = plt.subplots(figsize=(8, 4))\n\nkw = dict(height=bar_h, edgecolor='white', linewidth=0.5, zorder=3)\n\nleft = np.zeros(len(conditions))\nax.barh(y, h7a, left=left, color=C_H7a, label='H7a (tautological)', **kw)\nleft += h7a\nax.barh(y, h7b, left=left, color=C_H7b, label='H7b (ISR-specific)', **kw)\nleft += h7b\nax.barh(y, h1, left=left, color=C_H1, label='H1 (shortcut)', **kw)\nleft += h1\nax.barh(y, h8, left=left, color=C_H8, label='H8 (conjunction)', **kw)\nleft += h8\nax.barh(y, genuine, left=left, color=C_GENUINE, label='Genuine', **kw)\nleft += genuine\n\nfor i in range(len(conditions)):\n    ax.text(102, y[i], f'n={totals[i]}', va='center', ha='left', fontsize=9, color='#444444')\n\n# ISR β=0.1 H7 vs Random β=0.1 H7\nisr_h7 = h7a[1] + h7b[1]   # 70.6%\nrand_h7 = h7a[3] + h7b[3]  # 13.7%\nax.annotate(\n    f'ISR H7: {isr_h7:.1f}%\\nvs Random: {rand_h7:.1f}%',\n    xy=(rand_h7 / 2, y[3]),\n    xytext=(55, y[2] + 0.6),\n    fontsize=8.5, fontweight='bold', color=C_H7a,\n    ha='center',\n    arrowprops=dict(arrowstyle='->', color=C_H7a, lw=1.5),\n)\n\nax.set_yticks(y)\nax.set_yticklabels(conditions, fontsize=10)\nax.set_xlabel('Percentage of proved samples (%)', fontsize=11)\nax.set_xlim(0, 116)\nax.set_xticks([0, 20, 40, 60, 80, 100])\nax.spines['top'].set_visible(False)\nax.spines['right'].set_visible(False)\nax.tick_params(axis='both', labelsize=10)\nax.legend(fontsize=8.5, loc='upper right', frameon=False, ncol=2,\n          bbox_to_anchor=(0.98, 0.42))\n\nfig.subplots_adjust(left=0.22, right=0.95, top=0.95, bottom=0.16)\n\nbase = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures/fig3_hacking_composition'\nfig.savefig(f'{base}.pdf', dpi=300, bbox_inches='tight', pad_inches=0.15)\nfig.savefig(f'{base}.png', dpi=300, bbox_inches='tight', pad_inches=0.15)\nplt.close()\nprint(f'Saved: {base}.pdf')\nprint(f'Saved: {base}.png')\n",
      "numLines": 94,
      "startLine": 1,
      "totalLines": 94
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
Now let me read the abstract, introduction, conclusion, and appendix to check cross-chapter consistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "a39afaa0-58a6-42eb-b4a5-54c90a6a6e7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV7i5dnGeBvErLDnNsjmPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9577,
      "cache_read_input_tokens": 26204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9577
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

Now reading the remaining paper sections for cross-chapter consistency checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "46cbd7e5-c0b4-4f93-a6eb-bc4036059603",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV7i5dnGeBvErLDnNsjmPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9577,
      "cache_read_input_tokens": 26204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9577
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

<details open><summary>🔧 Tool call — Agent · `toolu_01YRtBCJRJs6GuvoLtKk1XGs`</summary>

```json
{
  "description": "Read paper intro/abstract/conclusion",
  "subagent_type": "Explore",
  "prompt": "Read the following files and return their full contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex (look for \\begin{abstract} and \\section{Introduction} and \\section{Conclusion})\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex\n\nI need the exact numbers/percentages mentioned in abstract, introduction, and conclusion sections, plus any data tables in the appendix that correspond to Table 1 or Figure 3 data. Return ALL numerical claims verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "6db8c050-6d45-4c7f-a23f-a645bb2cf54e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV7i5dnGeBvErLDnNsjmPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9577,
      "cache_read_input_tokens": 26204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9577
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

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "abf2cfbc81f6d7f59",
  "tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "description": "Read paper intro/abstract/conclusion",
  "task_type": "local_agent",
  "prompt": "Read the following files and return their full contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex (look for \\begin{abstract} and \\section{Introduction} and \\section{Conclusion})\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex\n\nI need the exact numbers/percentages mentioned in abstract, introduction, and conclusion sections, plus any data tables in the appendix that correspond to Table 1 or Figure 3 data. Return ALL numerical claims verbatim.",
  "uuid": "230ca2ba-346f-4ac1-95f8-97c311d40fce",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

## Round 1

3 recorded events

### User

_source line 14 · 2026-05-15T21:26:54.942Z_

Read the following files and return their full contents:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex (look for \begin{abstract} and \section{Introduction} and \section{Conclusion})
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex

I need the exact numbers/percentages mentioned in abstract, introduction, and conclusion sections, plus any data tables in the appendix that correspond to Table 1 or Figure 3 data. Return ALL numerical claims verbatim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "5563f132-297c-49b4-8fec-517bf098f1d4"
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Agent · `toolu_01RzTjqXsLicXgiiDAPZ9vtw`</summary>

```json
{
  "description": "Read paper method section",
  "subagent_type": "Explore",
  "prompt": "Read the file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex in full. I need to check ISR definition consistency and terminology (H7a/H7b naming, β symbol usage). Return the full content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "80a02f99-6aab-4a9f-8c11-1afbdc7f023b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV7i5dnGeBvErLDnNsjmPM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9577,
      "cache_read_input_tokens": 26204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9577
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

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ab3763a8d522764df",
  "tool_use_id": "toolu_01RzTjqXsLicXgiiDAPZ9vtw",
  "description": "Read paper method section",
  "task_type": "local_agent",
  "prompt": "Read the file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex in full. I need to check ISR definition consistency and terminology (H7a/H7b naming, β symbol usage). Return the full content.",
  "uuid": "ddfa7173-f451-440e-b71b-c1fb06dd8425",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

## Round 2

26 recorded events

### User

_source line 17 · 2026-05-15T21:26:56.539Z_

Read the file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex in full. I need to check ISR definition consistency and terminology (H7a/H7b naming, β symbol usage). Return the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RzTjqXsLicXgiiDAPZ9vtw",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "8a34ae22-e165-4d41-91b0-2364fe264e07"
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
  "task_id": "abf2cfbc81f6d7f59",
  "tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "description": "Reading paper/main.tex",
  "usage": {
    "total_tokens": 23107,
    "tool_uses": 1,
    "duration_ms": 2358
  },
  "last_tool_name": "Read",
  "uuid": "dcba79c2-0b10-4d98-945c-14959868bbfe",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01NN2TUec3vxhE4r4Yrq2Dpf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "7d3c13a0-89bf-4b08-bbed-1135f61bb570",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XayhyzyAaeAQ3Bw9vBH1Ny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23102,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23102,
        "ephemeral_1h_input_tokens": 0
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

_source line 20 · 2026-05-15T21:26:57.337Z_

<details><summary>↩ Tool result · `toolu_01NN2TUec3vxhE4r4Yrq2Dpf`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{limitations}
38	
39	\appendix
40	\input{appendix}
41	
42	\end{document}
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "48161296-88d2-44da-a126-6b978cae4897"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abf2cfbc81f6d7f59",
  "tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "description": "Reading paper/appendix.tex",
  "usage": {
    "total_tokens": 23108,
    "tool_uses": 2,
    "duration_ms": 2488
  },
  "last_tool_name": "Read",
  "uuid": "94445f66-1e67-4f6c-9a4b-16c87080bec0",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01BUiCoHBwYzzA9WrJqPE2B3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "8770535b-301e-4bff-8448-27ee1861a957",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XayhyzyAaeAQ3Bw9vBH1Ny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23102,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23102,
        "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-15T21:26:57.722Z_

<details><summary>↩ Tool result · `toolu_01BUiCoHBwYzzA9WrJqPE2B3`</summary>

```text
1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 8 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
55	
56	
57	\section{STA Algorithm}
58	\label{app:algorithm}
59	
60	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
61	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
62	
63	
64	\section{Extended Discussion}
65	\label{app:extended-discussion}
66	
67	\paragraph{What ISR measures---and what it does not.}
68	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
69	This is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.
70	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
71	ISR and downstream task performance are uncorrelated.
72	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
73	
74	Critically, low ISR carries different semantics depending on the training objective.
75	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
76	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
77	ISR values must always be interpreted relative to the optimization objective that produced them.
78	
79	\paragraph{The premise-count confound.}
80	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
81	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.
82	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
83	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
84	This bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
85	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
86	
87	\begin{table}[h]
88	\centering
89	\caption{Fisher exact tests for genuine rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ genuine rate is corrected for H8 reclassification and H7 false negatives (Appendix~\ref{app:h8}).}
90	\label{tab:bootstrap-ci}
91	\small
92	\begin{tabular}{@{}lcccc@{}}
93	\toprule
94	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
95	\midrule
96	\multicolumn{5}{@{}l}{\textit{Genuine rate (H8+FN corrected)}} \\
97	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
98	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
99	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
100	\midrule
101	\multicolumn{5}{@{}l}{\textit{H7 gaming rate}} \\
102	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
103	\midrule
104	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only genuine rate}} \\
105	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
106	\bottomrule
107	\end{tabular}
108	\\[2pt]
109	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
110	\end{table}
111	
112	\paragraph{Meta-level Goodhart: implications.}
113	The meta-Goodhart finding extends beyond this specific system.
114	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.
115	The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
116	$\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.
117	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
118	
119	\paragraph{Single-seed unreliability.}
120	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
121	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
122	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
123	
124	
125	\section{Hacking Mode Definitions}
126	\label{app:hacking-modes}
127	
128	We identify eight distinct reward hacking modes across all experiments.
129	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
130	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
131	
132	\begin{table}[h]
133	\centering
134	\small
135	\resizebox{\columnwidth}{!}{%
136	\begin{tabular}{@{}llcccc@{}}
137	\toprule
138	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
139	\midrule
140	H1 & Concl.\ in premises & 87 & 18 & 71 & 7 \\
141	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
142	H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
143	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
144	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
145	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
146	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
147	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
148	\bottomrule
149	\end{tabular}}
150	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}12$; ISR s44 only). $^\dagger$Random H7 driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
151	\label{tab:hacking-taxonomy-app}
152	\end{table}
153	
154	\paragraph{Classifier Validation.}
155	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
156	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
157	No training data or manual annotation is used for classification.
158	
159	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
160	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
161	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
162	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
163	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
164	
165	\subsection{H8 --- Premise-Subset Gaming}
166	\label{app:h8}
167	
168	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).
169	We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
170	
171	\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
172	Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
173	
174	\paragraph{Audit scope and limitations.}
175	Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
176	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.
177	Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
178	
179	\paragraph{H7 false-negative correction (H7b obfuscated tautology).}
180	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as genuine by the text matcher.
181	Manual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
182	We classify these as \textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.
183	$10/12$ achieve $\text{ISR}{\approx}0.8$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\S\ref{sec:taxonomy}).
184	After correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.
185	
186	\paragraph{Impact on genuine-rate comparison.}
187	After H8 reclassification and H7 false-negative correction: ISR genuine $= 14/231 = 6.06\%$ vs.\ random genuine $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
188	The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing genuine output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
189	
190	\subsection{H1 --- Conclusion Embedding}
191	
192	\paragraph{Definition.}
193	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
194	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
195	
196	\paragraph{Example (FOL).}
197	{\small\begin{verbatim}
198	Premises:
199	  all x (bird(x) -> flies(x)).
200	  bird(tweety).
201	  flies(tweety).  % conclusion embedded
202	Conclusion: flies(tweety).
203	\end{verbatim}}
204	
205	\paragraph{ISR interaction.}
206	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
207	ISR does not distinguish trivial from substantive necessity.
208	
209	\paragraph{Prevalence.}
210	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
211	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (70.6\% pooled).
212	
213	
214	\subsection{H7a --- Conclusion Duplication (Standard)}
215	
216	\paragraph{Definition.}
217	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
218	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
219	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
220	
221	\paragraph{Example (FOL).}
222	{\small\begin{verbatim}
223	Premises:
224	  all x ((A(x)&B(x))->(C(x)|D(x))).
225	Conclusion:
226	  all x ((A(x)&B(x))->(C(x)|D(x))).
227	\end{verbatim}}
228	
229	\paragraph{ISR interaction.}
230	ISR~$\approx 0.8$--$1.0$.
231	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
232	H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
233	
234	\paragraph{Prevalence.}
235	H7a (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
236	Combined H7 (H7a + H7b): 70.6\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).
237	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all H7a; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
238	
239	
240	\subsection{H7b --- Obfuscated Tautology}
241	
242	\paragraph{Definition.}
243	A single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.
244	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
245	
246	\paragraph{Example (FOL, vacuous quantifier wrapping).}
247	{\small\begin{verbatim}
248	Premises:
249	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
250	Conclusion:
251	  all x ((A(x)&B(x))->(C(x)|D(x))).
252	\end{verbatim}}
253	The premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.
254	
255	\paragraph{ISR interaction.}
256	ISR~$\approx 0.8$ ($10/12$ samples).
257	H7b simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).
258	This triple gaming makes H7b the most complete meta-Goodhart case we observe.
259	
260	\paragraph{Prevalence.}
261	Found exclusively in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).
262	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
263	
264	
265	\subsection{Tautological Collapse}
266	
267	\paragraph{Definition.}
268	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
269	
270	\paragraph{Example (FOL).}
271	\begin{verbatim}
272	Premises: p(a).
273	Conclusion: p(a).
274	\end{verbatim}
275	
276	\paragraph{ISR interaction.}
277	ISR~$=1.0$ (the sole premise is necessary).
278	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
279	
280	\paragraph{Prevalence.}
281	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
282	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
283	
284	
285	\subsection{Repetition Collapse}
286	
287	\paragraph{Definition.}
288	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
289	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
290	
291	\paragraph{Example (Prolog).}
292	\begin{verbatim}
293	penguin(fido).
294	penguin(fido).
295	penguin(fido).
296	... (repeated to 512 tokens)
297	query(penguin(fido)).
298	\end{verbatim}
299	
300	\paragraph{ISR interaction.}
301	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
302	ISR correctly diagnoses this degeneration.
303	
304	\paragraph{Prevalence.}
305	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
306	
307	
308	\subsection{Complexity-without-Utility}
309	
310	\paragraph{Definition.}
311	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
312	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
313	
314	\paragraph{Example (FOL).}
315	{\small\begin{verbatim}
316	Premises:
317	  all x all y (R(x,y) ->
318	    exists z (S(x,z) & T(z,y))).
319	  all x (P(x) -> Q(x)).
320	  P(a).            % only this needed
321	Conclusion: Q(a).
322	\end{verbatim}}
323	
324	\paragraph{ISR interaction.}
325	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
326	This is the mode ISR is best calibrated for.
327	
328	\paragraph{Prevalence.}
329	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
330	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
331	
332	
333	\subsection{Contradiction Explosion}
334	
335	\paragraph{Definition.}
336	The component count grows unboundedly over training.
337	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
338	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
339	
340	\paragraph{Example (FOL, 1000-step exec-only).}
341	{\small\begin{verbatim}
342	Premises:
343	  c1. c2. c3. ... c18. % 18.55 mean
344	  % conclusion embedded among premises
345	Conclusion: Q(a).
346	\end{verbatim}}
347	
348	\paragraph{ISR interaction.}
349	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
350	
351	\paragraph{Prevalence.}
352	Observed in extended exec-only training (seed~42, 1000 steps).
353	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
354	
355	
356	\subsection{Query-as-Fact Gaming}
357	
358	\paragraph{Definition.}
359	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
360	Prolog trivially proves the query by unifying with the fact.
361	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
362	
363	\paragraph{Example (Prolog).}
364	\begin{verbatim}
365	% NL: "Fido is happy."
366	% Model output:
367	fido_is_happy.
368	:- fido_is_happy.     % query = fact
369	\end{verbatim}
370	
371	\paragraph{ISR interaction.}
372	ISR~$\approx 0.9$--$1.0$.
373	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
374	Functionally equivalent to H7 but with a distinct surface mechanism.
375	
376	\paragraph{Prevalence.}
377	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
378	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
379	
380	
381	\section{Per-Seed Detailed Results}
382	\label{app:detailed-results}
383	
384	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
385	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
386	ISR values are proved-only ISR$^*$.
387	
388	\begin{table*}[t]
389	\centering
390	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
391	\label{tab:fol-detailed}
392	\label{tab:fol-beta01-detailed}
393	\footnotesize
394	\setlength{\tabcolsep}{3pt}
395	\begin{tabular}{@{}llccccccl@{}}
396	\toprule
397	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
398	\midrule
399	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
400	Base model (no training)
401	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
402	Ground-truth FOL
403	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
404	SFT
405	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
406	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
407	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
408	\cmidrule(l){2-9}
409	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
410	\midrule
411	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
412	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
413	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\%$ \\
414	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
415	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
416	  & 43 & 1000 & 0.90 & 0.465$^\S$ & 100 & 0 & 0 & H7 dominant \\
417	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
418	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & H8${=}15\%$ \\
419	\cmidrule(l){2-9}
420	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
421	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.95{\pm}0.05$} & & \makebox[0pt][l]{$0.16{\pm}0.27$} & & \makebox[0pt][l]{$0.0{\pm}0.0$} & 1000-step \\
422	\midrule
423	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
424	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
425	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\
426	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\
427	\cmidrule(l){2-9}
428	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
429	\midrule
430	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
431	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
432	\midrule
433	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
434	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
435	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\
436	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\cap$H8: 6) \\
437	\cmidrule(l){2-9}
438	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.87{\pm}0.08$} & & \makebox[0pt][l]{$0.117{\pm}0.042$} & & & H7 seed-dep.: 0/38/0\% \\
439	\midrule
440	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
441	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
442	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{genuine}}{=}3$ \\
443	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
444	\cmidrule(l){2-9}
445	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & & \\
446	\bottomrule
447	\end{tabular}
448	\end{table*}
449	
450	
451	\begin{table*}[t]
452	\centering
453	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
454	\label{tab:prolog-detailed}
455	\small
456	\begin{tabular}{@{}llcccccl@{}}
457	\toprule
458	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
459	\midrule
460	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
461	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
462	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
463	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
464	\cmidrule(l){2-8}
465	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
466	\midrule
467	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
468	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
469	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
470	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
471	\cmidrule(l){2-8}
472	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
473	\bottomrule
474	\end{tabular}
475	
476	\vspace{4pt}
477	{\footnotesize
478	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
479	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
480	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
481	}
482	\end{table*}
483	
484	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
485	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
486	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
487	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
488	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
489	
490	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
491	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
492	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
493	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
494	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
495	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
496	
497	\subsection{Per-Seed Results at $\beta{=}0.3$}
498	\label{app:beta03}
499	
500	Table~\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\beta{=}0.3$.
501	The three ISR seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
502	
503	\begin{table}[h]
504	\centering
505	\caption{Per-seed results at $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}
506	\label{tab:beta03-detailed}
507	\small
508	\begin{tabular}{@{}llcccccl@{}}
509	\toprule
510	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Mode} \\
511	\midrule
512	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
513	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\
514	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\
515	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\
516	\cmidrule(l){2-8}
517	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.66{\pm}0.42$} & & \makebox[0pt][l]{$0.39{\pm}0.31$} & & \\
518	\midrule
519	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
520	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\
521	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{genuine}}{=}3$ \\
522	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
523	\cmidrule(l){2-8}
524	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & \\
525	\bottomrule
526	\end{tabular}
527	\end{table}
528	
529	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
530	\label{app:100step}
531	
532	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%---higher than SFT (13.0\%, 3-seed pooled) but still early in training.
533	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
534	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
535	This demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.
536	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
537	
538	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
539	\label{app:o1-ablation}
540	
541	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
542	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
543	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$---functionally zero---compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
544	
545	\paragraph{ISR signal vs.\ training dynamics.}
546	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
547	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
548	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
549	The result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.
550	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "72398157-3d57-42a3-9f75-3c1faa9ce94e"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab3763a8d522764df",
  "tool_use_id": "toolu_01RzTjqXsLicXgiiDAPZ9vtw",
  "description": "Reading paper/method.tex",
  "usage": {
    "total_tokens": 23025,
    "tool_uses": 1,
    "duration_ms": 1453
  },
  "last_tool_name": "Read",
  "uuid": "3f891d65-2a2b-4cd5-a5b1-e3cabc777c9e",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01PQUeeiFjYyKq7E95m9vCpq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01RzTjqXsLicXgiiDAPZ9vtw",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "2b7190cc-2c51-4ce3-9ed9-0b407fc519c5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Fd5Di6LUC3rZwyfHRqdQm6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5686,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5686,
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

_source line 26 · 2026-05-15T21:26:58.043Z_

<details><summary>↩ Tool result · `toolu_01PQUeeiFjYyKq7E95m9vCpq`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: when the diagnostic becomes the target, meta-level Goodhart's Law emerges.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with GRPO~\citep{deepseekmath} ($K{=}8$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is standard in mutation testing and feature attribution; our novelty is its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
27	
28	\begin{algorithm}[t]
29	\caption{Solver Trace Ablation (STA)}
30	\label{alg:sta}
31	\begin{algorithmic}[1]
32	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
33	\ENSURE $\text{ISR}(x) \in [0, 1]$
34	\STATE $\textit{necessary} \gets 0$
35	\FOR{$i = 1$ to $n$}
36	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
37	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
38	    \ENDIF
39	\ENDFOR
40	\RETURN $\textit{necessary} \,/\, n$
41	\end{algorithmic}
42	\end{algorithm}
43	
44	\paragraph{Intensional Structural Reward.}
45	ISR is the fraction of necessary components:
46	\begin{equation}
47	  \text{ISR}(x) = \frac{1}{n}\sum_{i=1}^{n}\mathbf{1}\bigl[S(x\setminus\{c_i\})=\textit{failed}\bigr]
48	  \label{eq:isr}
49	\end{equation}
50	ISR is defined only for proved formalizations: ISR${=}1$ means every component is necessary; ISR${=}0$ means complete redundancy.
51	We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating structural quality with prove rate.
52	
53	\paragraph{Limitations of ISR.}
54	ISR measures syntactic component necessity, not semantic faithfulness: a formalization can achieve $\text{ISR}{=}1$ while semantically unrelated to the NL input (e.g., a single premise identical to the conclusion).
55	ISR is also sensitive to component count $n$: when $n{=}2$, $\text{ISR}\geq 0.5$ regardless of proof quality.
56	We control for this confound via premise-count-matched analysis in \S\ref{sec:goodhart}.
57	The $O(n)$ per-clause LOO ablation is necessary: a cheaper $O(1)$ binary variant produces near-zero ISR scores ($\text{ISR}^*{=}0.007$) indistinguishable from exec-only, because models generate redundant premise copies whose individual removal never changes the proof outcome.
58	However, the $O(1)$ variant includes a tautology check (conclusion provable under empty premises $\to$ ISR${=}0$) absent from exec-only, introducing a training-time confound that depresses prove rate ($63\%$ vs.\ $93\%$ exec-only); the two conditions are therefore non-equivalent in training dynamics despite producing comparable ISR signals (Appendix~\ref{app:o1-ablation}).
59	
60	\subsection{Reward Conditions and Hacking Modes}
61	\label{sec:rewards}
62	\label{sec:taxonomy-method}
63	
64	We study six conditions: exec-only ($r_{\text{exec}}$), ISR low/high-dose ($r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta\in\{0.1,0.3\}$), matched random controls ($r_{\text{exec}}\cdot(1{+}\beta u)$, $u\sim\mathcal{U}(0,1)$), and an SFT baseline (NLL on gold formalizations).
65	Multiplicative bonuses apply only to proved samples, keeping the prove-rate floor intact.
66	Random isolates ISR-specific signal from generic reward-variance effects; SFT isolates whether structural degeneration arises from RL optimization or data exposure alone.
67	Each RL condition uses seeds $\{42,43,44\}$ and identical training data.
68	An earlier convex formulation ($\alpha r_{\text{exec}} + \beta r_{\text{exec}}\text{ISR}$, $\alpha{+}\beta{=}1$) was discarded because $\text{ISR}{<}1$ always penalized relative to exec-only, collapsing PR (Appendix~\ref{app:setup}).
69	
70	\paragraph{Hacking taxonomy.}
71	Across conditions, seeds, and logic types we identify eight structural-degeneration modes (full definitions in Appendix~\ref{app:hacking-modes}):
72	\textbf{H1} (conclusion embedded among multiple premises),
73	\textbf{H7} (single-premise conclusion duplication, subtypes H7a standard and H7b obfuscated tautology; targets the ISR signal directly, since removing the sole premise forces $\text{ISR}\geq 0.5$),
74	\textbf{H8} (premise-subset gaming: each component is LOO-necessary but the premise set is a strict subset of what the problem requires, inflating ISR without faithful reasoning; Appendix~\ref{app:h8}),
75	\textbf{tautological collapse} (minimal two-component $P{\to}P$ without explicit ISR inflation),
76	\textbf{repetition collapse} (identical clauses repeated to inflate component count),
77	\textbf{complexity-without-utility} (elaborate but vacuous premises),
78	\textbf{contradiction explosion} (contradictory premises trivializing any conclusion via \emph{ex falso}), and
79	\textbf{query-as-fact gaming} (Prolog-specific: emit the NL question as an atom asserted as both fact and query; evades text-match classifiers).
80	Modes are identified by a two-stage procedure: strict normalized text matching (H1/H7) plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution (catches modes evading text matching).
81	We report both classifications in \S\ref{sec:experiments}.
82	
83	In interpreting ISR results we distinguish two failure semantics that share a numerical signature: an exec-only \emph{low} ISR signals \emph{redundancy} (e.g., repeated ground facts in Prolog), whereas an ISR-rewarded \emph{high} ISR signals \emph{metric gaming} (H7-style constructions).
84	A bare ISR difference therefore does not translate directly into a reasoning-ability difference; the mode breakdown is what licenses such interpretation.
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01RzTjqXsLicXgiiDAPZ9vtw",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "a032fd1d-a292-41fd-bcb8-b99f9b7be024"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abf2cfbc81f6d7f59",
  "tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 37813,
    "tool_uses": 3,
    "duration_ms": 5585
  },
  "last_tool_name": "Bash",
  "uuid": "2ea215c8-ce9f-4745-a7d4-16432a0629b3",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01CxP3PxYj8c59L4R6LLC9yk`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "8c7557a2-e5b2-43b7-b021-a85ccd99e576",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019tTW4S8UDGQn8Q79J79ksE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 14699,
      "cache_read_input_tokens": 23102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14699,
        "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-15T21:27:01.058Z_

<details><summary>↩ Tool result · `toolu_01CxP3PxYj8c59L4R6LLC9yk`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "e6ad1ada-b11e-4255-bfe9-16cede21e36c"
}
```

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abf2cfbc81f6d7f59",
  "tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "description": "Reading paper/abstract.tex",
  "usage": {
    "total_tokens": 38256,
    "tool_uses": 4,
    "duration_ms": 7713
  },
  "last_tool_name": "Read",
  "uuid": "c74c6499-7482-4863-a74b-0dfed4dfac1a",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01KvM21SFREL52j7xWqisuym`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "ea54c108-d214-41ad-96a0-4ef71f3ba9d8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DvB8X5TDaCEUVDTbnbPSg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 37801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 442,
        "ephemeral_1h_input_tokens": 0
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

_source line 32 · 2026-05-15T21:27:02.672Z_

<details><summary>↩ Tool result · `toolu_01KvM21SFREL52j7xWqisuym`</summary>

```text
1	\begin{abstract}
2	GRPO-trained neurosymbolic formalizers achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; an SFT baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR improvement reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart: 3/3 seeds gaming via distinct mechanisms, 0\% non-hacking.
9	Across 6 reward conditions, 2 logic types, 3 seeds, we catalog 8 hacking modes---including query-as-fact gaming that bypasses text-match classifiers---documenting ISR's fundamental asymmetry: reliable as a diagnostic, unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "0c8a2dbf-559c-4d72-ad5a-cb0e873ef91d"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abf2cfbc81f6d7f59",
  "tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "description": "Reading paper/introduction.tex",
  "usage": {
    "total_tokens": 38257,
    "tool_uses": 5,
    "duration_ms": 8124
  },
  "last_tool_name": "Read",
  "uuid": "3d4f0b3f-f2d6-46bc-8199-27c585eac700",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01R6FUREAd6uAByB1yoKRTcY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "a0e63687-2b64-4fd3-80de-aa5ea2e58bf3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DvB8X5TDaCEUVDTbnbPSg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 37801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 442,
        "ephemeral_1h_input_tokens": 0
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

_source line 35 · 2026-05-15T21:27:03.075Z_

<details><summary>↩ Tool result · `toolu_01R6FUREAd6uAByB1yoKRTcY`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but gives no gradient on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
17	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
18	ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
19	
20	\paragraph{ISR as diagnostic.}
21	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (99.5\% degradation) while PR rises $32\%{\to}96\%$.
22	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
23	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), localizing the failure to RL optimization, not data or capacity.
24	
25	\paragraph{Meta-level Goodhart.}
26	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR is gamed at its own definition---\emph{meta-level Goodhart's Law}~\citep{manheim-goodhart-taxonomy, karwowski-goodhart-rl, gao-reward-overoptimization}.
27	At $\beta{=}0.1$, 70.6\% of proved samples exhibit conclusion duplication (H7)---versus 13.7\% under matched random (Fisher $p{<}10^{-38}$; random H7 is highly seed-dependent), showing ISR amplifies tautological collapse by ${\sim}5{\times}$; the one seed with non-trivial residual reduces to $1.06\times$ random after controlling for a premise-count confound.
28	At $\beta{=}0.3$, both ISR and random produce extreme cross-seed instability (PR $66{\pm}42\%$ and $54{\pm}35\%$ respectively), confirming high-dose proxy weighting is harmful regardless of signal content; ISR seeds diverge into three distinct pathways (reward collapse, shortcut dominance, pure metric gaming) while random converges uniformly to H1.
29	The effect transfers and intensifies in Prolog: 3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming} that bypasses text-match classifiers.
30	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer.}
31	
32	\paragraph{Contributions.}
33	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 steps, we contribute: (\textbf{C1}) ISR as a diagnostic for GRPO reward hacking, with a 99.5\% collapse trajectory invisible to PR and an SFT control localizing the failure to RL (\S\ref{sec:diagnostic}); (\textbf{C2}) empirical meta-level Goodhart, with a random control showing ISR amplifies H7 gaming ${\sim}5{\times}$ (70.6\% vs.\ 13.7\%, Fisher $p{<}10^{-38}$; random H7 is seed-dependent) and a premise-count-matched analysis showing the sole apparent gain is an LOO artifact (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with universal Goodhart (\S\ref{sec:crosslogic}); (\textbf{C4}) an eight-mode hacking taxonomy including query-as-fact gaming and obfuscated tautology, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
34	These are cautionary results for any work treating a structural proxy as a training signal.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "d903bf77-960f-43e6-b256-5edfbf60c327"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abf2cfbc81f6d7f59",
  "tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "description": "Reading paper/conclusion.tex",
  "usage": {
    "total_tokens": 38258,
    "tool_uses": 6,
    "duration_ms": 8251
  },
  "last_tool_name": "Read",
  "uuid": "861d9448-c732-4342-acb7-8cff63b1e865",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01ANFPrFZ14QNV9zZ9YNrb69`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "29e6efe1-c2d6-4197-abff-a84349dd78fb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DvB8X5TDaCEUVDTbnbPSg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 37801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 442,
        "ephemeral_1h_input_tokens": 0
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

_source line 38 · 2026-05-15T21:27:03.203Z_

<details><summary>↩ Tool result · `toolu_01ANFPrFZ14QNV9zZ9YNrb69`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	Solver Trace Ablation (STA) exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides; an SFT baseline with 92.3\% non-hacking (3-seed pooled) localizes the failure to RL optimization (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR induces meta-level Goodhart's Law: the diagnostic for gaming becomes itself the target of gaming.
6	At $\beta{=}0.1$, conclusion duplication exploits the LOO definition (70.6\% vs.\ 13.7\% under matched random (Fisher $p{<}10^{-38}$); random H7 is seed-dependent (38.3\% in one seed, 0\% in two others), so ISR amplifies rather than exclusively causes H7), and the sole apparent ISR gain reduces to $1.06\times$ random once a premise-count confound is controlled; at $\beta{=}0.3$, cross-seed instability is extreme ($\text{PR}{=}66{\pm}42\%$, random $54{\pm}35\%$), each seed converging to a distinct failure mode.
7	The pattern transfers to Prolog, where ISR-as-reward yields universal gaming (3/3 seeds, 0\% non-hacking) via three distinct mechanisms including query-as-fact gaming, which bypasses text-match classifiers (\S\ref{sec:taxonomy}).
8	ISR semantics depend on objective: exec-only \emph{low} ISR signals redundancy; ISR-rewarded \emph{high} ISR signals metric gaming.
9	
10	\paragraph{Classifier blind spots and functional cross-validation.}
11	H7b (obfuscated tautology) demonstrates that text-match classifiers have systematic blind spots: the model learns vacuous quantifier wrapping to disguise tautologies, evading detection while simultaneously gaming ISR ($10/12$ samples at $\text{ISR}{\approx}0.8$).
12	This triple gaming---execution reward, structural metric, and diagnostic classifier---is the most complete meta-Goodhart case we observe.
13	Query-as-fact gaming in Prolog (\S\ref{sec:crosslogic}) independently confirms the blind spot: our strict classifier reported $100\%$ genuine before functional LOO analysis revealed $95/97$ samples tautological.
14	Both cases argue for mandatory functional cross-validation of any text-based hacking classifier.
15	
16	\paragraph{H7 dose-response gradient.}
17	H7 tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ H7 ($36/262$, pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
18	The gradient---random $\beta{=}0.1$ ($13.7\%$, pooled) $\to$ random $\beta{=}0.3$ (4--7 H7a per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.
19	
20	\paragraph{Hacking mode switching.}
21	The dominant hacking strategy is not reward-determined: under identical reward configurations, different seeds converge to qualitatively different modes (Appendix Table~\ref{tab:fol-detailed}).
22	Random $\beta{=}0.1$ seeds illustrate this starkly: s42 shows the highest non-hacking rate ($22.8\%$), s43 is H7-dominant ($38.3\%$), and s44 is H8-dominant.
23	ISR $\beta{=}0.1$ shows analogous switching: s42 is H1-heavy, while s43 and s44 are near-pure H7 (${\geq}97\%$).
24	This seed-dependent mode selection implies that GRPO hacking patterns are sensitive to random initialization, and single-seed results can misrepresent the hacking profile of a reward configuration.
25	Multi-seed evaluation with per-mode reporting should be standard practice.
26	
27	The asymmetry---reliable observer, unreliable optimizer---may generalize to other perturbation-based diagnostics; ISR and structurally similar metrics should be used as post-hoc evaluation, with future work targeting gaming-robust rewards and broader logic types.
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "f18982ed-465d-496f-8361-16cbaf41f325"
}
```

</details>

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ab3763a8d522764df",
  "tool_use_id": "toolu_01RzTjqXsLicXgiiDAPZ9vtw",
  "status": "completed",
  "output_file": "",
  "summary": "Read paper method section",
  "usage": {
    "total_tokens": 26329,
    "tool_uses": 1,
    "duration_ms": 8552
  },
  "uuid": "e016892c-817c-4b75-bb4b-150a8f399f8a",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool result

_source line 40 · 2026-05-15T21:27:05.093Z_

<details><summary>↩ Tool result · `toolu_01RzTjqXsLicXgiiDAPZ9vtw`</summary>

```text
Full content of method.tex:

**ISR Definition (Equation 48-51):**
- Defined only for proved formalizations
- ISR(x) = (1/n) × Σ 𝟙[S(x\{cᵢ})=failed] — fraction of necessary components
- ISR=1: all components necessary; ISR=0: complete redundancy
- Notation: ISR* denotes "proved-only ISR" to separate structural quality from prove rate

**H7a/H7b Naming (Line 73):**
- H7: Single-premise conclusion duplication
  - **H7a**: standard (explicit duplication)
  - **H7b**: obfuscated tautology (semantic duplication/obfuscation)
- Both target ISR signal directly — removing sole premise forces ISR≥0.5

**β Symbol Usage (Line 64):**
- Multiplicative reward: r_exec·(1+β·ISR)
- β ∈ {0.1, 0.3} for low/high-dose ISR conditions
- Also used in random control: r_exec·(1+β·u) where u~𝒰(0,1)
- Earlier convex formulation (α·r_exec + β·r_exec·ISR) was discarded

**Consistency Check:**
- ISR terminology is consistent: defined in eq. 47-48, denoted ISR* for proved-only throughout
- H7a/H7b distinction is clearly marked as subtypes
- β usage is uniform as multiplicative weight on ISR/random bonuses
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "96838261-7ca6-416e-a083-8f57407ca8a6",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex in full. I need to check ISR definition consistency and terminology (H7a/H7b naming, β symbol usage). Return the full content.",
    "agentId": "ab3763a8d522764df",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Full content of method.tex:\n\n**ISR Definition (Equation 48-51):**\n- Defined only for proved formalizations\n- ISR(x) = (1/n) × Σ 𝟙[S(x\\{cᵢ})=failed] — fraction of necessary components\n- ISR=1: all components necessary; ISR=0: complete redundancy\n- Notation: ISR* denotes \"proved-only ISR\" to separate structural quality from prove rate\n\n**H7a/H7b Naming (Line 73):**\n- H7: Single-premise conclusion duplication\n  - **H7a**: standard (explicit duplication)\n  - **H7b**: obfuscated tautology (semantic duplication/obfuscation)\n- Both target ISR signal directly — removing sole premise forces ISR≥0.5\n\n**β Symbol Usage (Line 64):**\n- Multiplicative reward: r_exec·(1+β·ISR)\n- β ∈ {0.1, 0.3} for low/high-dose ISR conditions\n- Also used in random control: r_exec·(1+β·u) where u~𝒰(0,1)\n- Earlier convex formulation (α·r_exec + β·r_exec·ISR) was discarded\n\n**Consistency Check:**\n- ISR terminology is consistent: defined in eq. 47-48, denoted ISR* for proved-only throughout\n- H7a/H7b distinction is clearly marked as subtypes\n- β usage is uniform as multiplicative weight on ISR/random bonuses"
      }
    ],
    "totalDurationMs": 8559,
    "totalTokens": 26707,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3301,
      "cache_read_input_tokens": 23016,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3301
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 385,
          "cache_read_input_tokens": 23016,
          "cache_creation_input_tokens": 3301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3301,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
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

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "abf2cfbc81f6d7f59",
  "tool_use_id": "toolu_01YRtBCJRJs6GuvoLtKk1XGs",
  "status": "completed",
  "output_file": "",
  "summary": "Read paper intro/abstract/conclusion",
  "usage": {
    "total_tokens": 42067,
    "tool_uses": 6,
    "duration_ms": 24957
  },
  "uuid": "66c27d31-7c00-4c39-9a99-706464350701",
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a"
}
```

---

### Tool result

_source line 42 · 2026-05-15T21:27:19.905Z_

<details><summary>↩ Tool result · `toolu_01YRtBCJRJs6GuvoLtKk1XGs`</summary>

```text
Perfect. Now I have all the key sections. Let me compile the exact numerical claims from the abstract, introduction, and conclusion sections, along with the relevant data tables from the appendix.

## Exact Numerical Claims from Abstract, Introduction, and Conclusion

### **ABSTRACT**
- **93%** prove rate on FOLIO
- **87%** of proved outputs embed conclusion verbatim among premises
- **-0.049** Spearman ρ (ISR vs NLI accuracy), p = 0.187
- **100-1000 GRPO steps**: ISR collapses from **0.642 → 0.003** while PR rises **32% → 96%**
- **92.3%** non-hacking on identical data (SFT baseline, 3-seed pooled)
- **β=0.1**: **70.6%** conclusion duplication (H7) vs **13.7%** under random (Fisher p = 1.3×10⁻³⁹)
- **~5×** amplification of H7 frequency via ISR vs random
- **1.06×** sole apparent ISR improvement after premise-count control
- **β=0.3**: PR **66±42%** (ISR) and **54±35%** (random)
- **0%** non-hacking in Prolog (3/3 seeds)
- **8** hacking modes catalogued

### **INTRODUCTION**
- **93%** prove rate on first-order logic problems
- **87%** of proved outputs embed conclusion verbatim among premises
- **ISR*: 0.642 → 0.132 → 0.003** over 100-1000 steps (99.5% degradation)
- **32% → 96%** PR rise over same period
- Three seeds diverge with **PR σ = 47 pp** (percentage points)
- **PR = 13.0%** with **92.3%** non-hacking (SFT baseline, 3-seed pooled, 1000 steps)
- **β=0.1**: **70.6%** conclusion duplication vs **13.7%** under random (Fisher p < 10⁻³⁸)
- **~5×** H7 amplification by ISR
- **1.06×** random after premise-count control
- **β=0.3**: PR **66±42%** (ISR) and **54±35%** (random)
- **3/3 seeds** yield **0%** non-hacking in Prolog via distinct mechanisms

### **CONCLUSION**
- **99.5%** collapse under exec-only GRPO (ISR)
- **92.3%** non-hacking (SFT baseline, 3-seed pooled)
- **β=0.1**: **70.6%** conclusion duplication vs **13.7%** random (Fisher p < 10⁻³⁸)
- Random H7 seed-dependent: **38.3%** in s43, **0%** in s42/s44
- **1.06×** reduction in ISR gain after premise-count control
- **β=0.3**: PR **66±42%**, random **54±35%**
- **3/3 seeds** with **0%** non-hacking in Prolog via three distinct mechanisms
- **10/12** H7b samples at ISR ≈ 0.8
- **95/97** samples tautological in Prolog query-as-fact gaming
- Random **β=0.1**: **13.7%** H7 (pooled); **38.3%** s43, **0%** s42/s44
- **4-7 H7a** samples per seed at random **β=0.3**
- ISR **β=0.1**: **70.6%** H7

---

## Key Data Tables from Appendix

**Table 1 (tab:bootstrap-ci)** — Fisher exact tests for genuine rate:
| Comparison | Condition | Control | OR | p-value |
|---|---|---|---|---|
| ISR vs. Random | 6.06% [3.6,9.9] | 9.5% [6.5,13.7] | 0.61 | 0.182 (n.s.) |
| ISR vs. Exec-only | 6.06% | 7.5% | 0.79 | 0.62 |
| Random vs. Exec-only | 9.5% | 7.5% | 1.30 | 0.68 |
| ISR vs. Random (H7 gaming) | 70.6% [64.3,76.3] | 13.7% [9.9,18.6] | 15.05 | 1.3×10⁻³⁹ |
| SFT vs. Exec-only | 92.3% [79.7,97.3] | 7.5% | 147 | <0.001 |

**Table 2 (tab:fol-detailed)** — Detailed per-seed FOL results (selected rows):
| Condition | Seed | Steps | PR | ISR* | H7% | H1% | N-H% |
|---|---|---|---|---|---|---|---|
| SFT | 42 | 1000 | 0.13 | 0.568 | 0 | 7.7 | **92.3** |
| Exec-only | 42 | 500 | 0.93 | 0.132 | 0 | 87.1 | 7.5 |
| Exec-only | 42 | 1000 | 0.96 | 0.003 | 0 | 100 | 0 |
| Exec-only | 44 | 500 | 0.98 | 0.582 | 100 | 0 | 0 |
| ISR β=0.1 | 42 | 500 | 0.81 | 0.415 | 16.0 | 51.9 | **17.3** |
| ISR β=0.1 | 43 | 500 | 0.61 | 0.830 | **100** | 0 | 0 |
| ISR β=0.1 | 44 | 500 | 0.89 | 0.902 | 100 | 0 | 0 |
| Random β=0.1 | 42 | 500 | 0.79 | 0.131 | 0 | 73.4 | 22.8 |
| Random β=0.1 | 43 | 500 | 0.94 | 0.150 | **38.3** | 59.6 | 1.1 |
| ISR β=0.3 | 44 | 500 | 0.95 | 0.742 | **100** | 0 | 0 |

**Table 3 (tab:prolog-detailed)** — Prolog results (SWI-Prolog 8.4.2):
| Condition | Seed | PR | ISR* | H7% | H1% | N-H% | Notes |
|---|---|---|---|---|---|---|---|
| Exec+ISR | 42 | 0.50 | 1.000 | **100** | 0 | 0 | H7 tautological |
| Exec+ISR | 43 | 0.38 | 0.185 | 0 | 97.4 | 0 | Functional H7 |
| Exec+ISR | 44 | 0.97 | 0.912 | 0 | 0 | 0 | Query-as-fact gaming (95/97 n_necessary=1) |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a05e5efe-df59-432c-b1a8-2dd53c56581a",
  "uuid": "92277ae9-84ec-4407-923c-18f24d272ccf",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following files and return their full contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.tex (look for \\begin{abstract} and \\section{Introduction} and \\section{Conclusion})\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex\n\nI need the exact numbers/percentages mentioned in abstract, introduction, and conclusion sections, plus any data tables in the appendix that correspond to Table 1 or Figure 3 data. Return ALL numerical claims verbatim.",
    "agentId": "abf2cfbc81f6d7f59",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have all the key sections. Let me compile the exact numerical claims from the abstract, introduction, and conclusion sections, along with the relevant data tables from the appendix.\n\n## Exact Numerical Claims from Abstract, Introduction, and Conclusion\n\n### **ABSTRACT**\n- **93%** prove rate on FOLIO\n- **87%** of proved outputs embed conclusion verbatim among premises\n- **-0.049** Spearman ρ (ISR vs NLI accuracy), p = 0.187\n- **100-1000 GRPO steps**: ISR collapses from **0.642 → 0.003** while PR rises **32% → 96%**\n- **92.3%** non-hacking on identical data (SFT baseline, 3-seed pooled)\n- **β=0.1**: **70.6%** conclusion duplication (H7) vs **13.7%** under random (Fisher p = 1.3×10⁻³⁹)\n- **~5×** amplification of H7 frequency via ISR vs random\n- **1.06×** sole apparent ISR improvement after premise-count control\n- **β=0.3**: PR **66±42%** (ISR) and **54±35%** (random)\n- **0%** non-hacking in Prolog (3/3 seeds)\n- **8** hacking modes catalogued\n\n### **INTRODUCTION**\n- **93%** prove rate on first-order logic problems\n- **87%** of proved outputs embed conclusion verbatim among premises\n- **ISR*: 0.642 → 0.132 → 0.003** over 100-1000 steps (99.5% degradation)\n- **32% → 96%** PR rise over same period\n- Three seeds diverge with **PR σ = 47 pp** (percentage points)\n- **PR = 13.0%** with **92.3%** non-hacking (SFT baseline, 3-seed pooled, 1000 steps)\n- **β=0.1**: **70.6%** conclusion duplication vs **13.7%** under random (Fisher p < 10⁻³⁸)\n- **~5×** H7 amplification by ISR\n- **1.06×** random after premise-count control\n- **β=0.3**: PR **66±42%** (ISR) and **54±35%** (random)\n- **3/3 seeds** yield **0%** non-hacking in Prolog via distinct mechanisms\n\n### **CONCLUSION**\n- **99.5%** collapse under exec-only GRPO (ISR)\n- **92.3%** non-hacking (SFT baseline, 3-seed pooled)\n- **β=0.1**: **70.6%** conclusion duplication vs **13.7%** random (Fisher p < 10⁻³⁸)\n- Random H7 seed-dependent: **38.3%** in s43, **0%** in s42/s44\n- **1.06×** reduction in ISR gain after premise-count control\n- **β=0.3**: PR **66±42%**, random **54±35%**\n- **3/3 seeds** with **0%** non-hacking in Prolog via three distinct mechanisms\n- **10/12** H7b samples at ISR ≈ 0.8\n- **95/97** samples tautological in Prolog query-as-fact gaming\n- Random **β=0.1**: **13.7%** H7 (pooled); **38.3%** s43, **0%** s42/s44\n- **4-7 H7a** samples per seed at random **β=0.3**\n- ISR **β=0.1**: **70.6%** H7\n\n---\n\n## Key Data Tables from Appendix\n\n**Table 1 (tab:bootstrap-ci)** — Fisher exact tests for genuine rate:\n| Comparison | Condition | Control | OR | p-value |\n|---|---|---|---|---|\n| ISR vs. Random | 6.06% [3.6,9.9] | 9.5% [6.5,13.7] | 0.61 | 0.182 (n.s.) |\n| ISR vs. Exec-only | 6.06% | 7.5% | 0.79 | 0.62 |\n| Random vs. Exec-only | 9.5% | 7.5% | 1.30 | 0.68 |\n| ISR vs. Random (H7 gaming) | 70.6% [64.3,76.3] | 13.7% [9.9,18.6] | 15.05 | 1.3×10⁻³⁹ |\n| SFT vs. Exec-only | 92.3% [79.7,97.3] | 7.5% | 147 | <0.001 |\n\n**Table 2 (tab:fol-detailed)** — Detailed per-seed FOL results (selected rows):\n| Condition | Seed | Steps | PR | ISR* | H7% | H1% | N-H% |\n|---|---|---|---|---|---|---|---|\n| SFT | 42 | 1000 | 0.13 | 0.568 | 0 | 7.7 | **92.3** |\n| Exec-only | 42 | 500 | 0.93 | 0.132 | 0 | 87.1 | 7.5 |\n| Exec-only | 42 | 1000 | 0.96 | 0.003 | 0 | 100 | 0 |\n| Exec-only | 44 | 500 | 0.98 | 0.582 | 100 | 0 | 0 |\n| ISR β=0.1 | 42 | 500 | 0.81 | 0.415 | 16.0 | 51.9 | **17.3** |\n| ISR β=0.1 | 43 | 500 | 0.61 | 0.830 | **100** | 0 | 0 |\n| ISR β=0.1 | 44 | 500 | 0.89 | 0.902 | 100 | 0 | 0 |\n| Random β=0.1 | 42 | 500 | 0.79 | 0.131 | 0 | 73.4 | 22.8 |\n| Random β=0.1 | 43 | 500 | 0.94 | 0.150 | **38.3** | 59.6 | 1.1 |\n| ISR β=0.3 | 44 | 500 | 0.95 | 0.742 | **100** | 0 | 0 |\n\n**Table 3 (tab:prolog-detailed)** — Prolog results (SWI-Prolog 8.4.2):\n| Condition | Seed | PR | ISR* | H7% | H1% | N-H% | Notes |\n|---|---|---|---|---|---|---|---|\n| Exec+ISR | 42 | 0.50 | 1.000 | **100** | 0 | 0 | H7 tautological |\n| Exec+ISR | 43 | 0.38 | 0.185 | 0 | 97.4 | 0 | Functional H7 |\n| Exec+ISR | 44 | 0.97 | 0.912 | 0 | 0 | 0 | Query-as-fact gaming (95/97 n_necessary=1) |"
      }
    ],
    "totalDurationMs": 24962,
    "totalTokens": 43991,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 38243,
      "output_tokens": 1935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1935,
          "cache_read_input_tokens": 38243,
          "cache_creation_input_tokens": 3806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3806,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 0,
      "bashCount": 1,
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
