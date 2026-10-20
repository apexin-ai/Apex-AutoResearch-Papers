# paper round7 merged

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 115
- **Recorded user turns:** 0
- **Tool calls:** 43
- **Original source:** `logs/workers/worker_paper_round7-merged_20260517T173708.log`
- **Structured JSON:** [`3260df54519f5333df30.json`](../../sessions/32/3260df54519f5333df30.json)

## Before a recorded user message

115 recorded events

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
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
  "uuid": "2dc9acf4-f2f6-4f4c-a5f4-0d6cb71e766c",
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
    "resetsAt": 1779046200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d6649d09-0502-4991-ac0e-85de74de6120",
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant files to understand the current state before making changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "799a1fe3-7bf7-47b5-9c96-1c048e1f9480",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNJsr6mbd1D33nbZ8N7GMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17863,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17863
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

I'll work through this in two batches. Let me start by reading the relevant files for Batch 1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "21778397-cdd7-4157-80db-1c8fc5c3a2f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNJsr6mbd1D33nbZ8N7GMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17863,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17863
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

<details open><summary>🔧 Tool call — Read · `toolu_013MwWx5kN3ys7U5EcrRYLh9`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "12ef6f87-72d5-439a-b304-e98ea5d26df6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNJsr6mbd1D33nbZ8N7GMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17863,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17863
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

_source line 7 · 2026-05-17T17:37:23.826Z_

<details><summary>↩ Tool result · `toolu_013MwWx5kN3ys7U5EcrRYLh9`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}) with greedy decoding (Appendix~\ref{app:setup}).
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).
13	
14	\subsection{ISR as Diagnostic}
15	\label{sec:diagnostic}
16	
17	\begin{figure}[t]
18	\centering
19	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
20	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples have $\text{ISR}{=}0$ and mean component count inflates 6.58$\to$18.55 (contradiction explosion).}
21	\label{fig:isr-collapse}
22	\end{figure}
23	
24	\textbf{Collapse trajectory.}
25	Figure~\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
26	PR rises $32\%\to93\%\to96\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
27	By 500 steps, 87.1\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\% and mean component count more than doubles ($6.58\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.
28	Extended training, lacking a structural signal, \emph{worsens} formalization quality while improving the headline number.
29	
30	\textbf{Cross-seed instability.}
31	The three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\ref{app:detailed-results}): s42 reaches $\text{PR}{=}93\%$ via conclusion embedding ($\text{H1}{=}87\%$); s43 collapses to $\text{PR}{=}13\%$ (at 500 steps) via repetition (87\% of rollouts truncated); s44 reaches $\text{PR}{=}98\%$ via tautological collapse ($\text{H7}{=}100\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44
32	The cross-seed PR variance ($\sigma{=}47$\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).
33	By 1000 steps, all three converge to high PR ($0.97{\pm}0.02$) with near-zero genuine output (see Appendix~\ref{app:h8} and Table~\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\%$, genuine $6.2\%$; s44: H1 $85\%$ + H8 $15\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2
34	Notably, s43 recovers from $\text{PR}{=}13\%$ (500 steps) to $\text{PR}{=}96\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.
35	
36	\textbf{SFT baseline.}
37	SFT on gold formalizations reaches $\text{PR}{=}13.0\%$ (3-seed pooled, 1000 steps) with $\text{H7}{=}0$, $\text{H1}{=}7.7\%$, $92.3\%$ non-hacking ($n{=}39$; $\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$; per-seed range ${\sim}$91--93\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
38	The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific; a 100-step checkpoint ($\text{PR}{=}32\%$, hacking${\geq}31\%$) partially controls for the PR-level confound, though the PR gap remains substantial (Appendix~\ref{app:100step}).
39	SFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.
40	Whether SFT would develop similar exploits at higher prove rates remains an open question; this mechanistic argument is plausible but not conclusive.
41	
42	\subsection{ISR as Reward: Goodhart Effects}
43	\label{sec:goodhart}
44	
45	We now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with a matched random control, $r = r_{\text{exec}}\cdot(1 + \beta\,u)$, $u\sim\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.
46	We present $\beta{=}0.1$ first as the focal dose (5 seeds, trajectory analysis), then examine lower and higher doses.
47	The headline finding: ISR contains an inherent Goodhart vulnerability~\citep{manheim-goodhart-taxonomy} observed to produce collapse at all four tested doses ($\beta\in\{0.05, 0.1, 0.2, 0.3\}$).
48	The mechanism is structural: tautological proofs ($P{\to}P$) receive $\text{ISR}{=}0.75$ and single-premise-equals-conclusion constructions receive $\text{ISR}{\geq}0.5$, both by the LOO definition alone.
49	Once sampled during GRPO rollouts, these high-ISR tautologies create a positive feedback loop; $\beta$ controls only the \emph{timing} of collapse, not whether it occurs.
50	
51	\begin{table}[t]
52	\centering
53	\small
54	\resizebox{\columnwidth}{!}{%
55	\begin{tabular}{lcccccc}
56	\toprule
57	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} \\
58	\midrule
59	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
60	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
61	\midrule
62	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
63	Exec-only (1k)$^{\dagger\dagger}$ & --- & 97{\scriptsize$\pm$2} & 0.03{\scriptsize$\pm$.05} & 0 & --- & $\leq$2$^{\dagger\dagger}$ \\
64	ISR$^\ddagger$ & 0.1 & 70{\scriptsize$\pm$19} & --- & \textbf{54} & 18 & 23$^\star$ \\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)
65	Random & 0.1 & \textbf{83}{\scriptsize$\pm$15} & 0.080{\scriptsize$\pm$.06} & 30 & 59 & 8 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)
66	ISR & 0.2 & 97{\scriptsize$\pm$4} & 0.69{\scriptsize$\pm$.24} & \textbf{99} & 0 & 0 \\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\ref{tab:beta02-detail})
67	\midrule
68	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
69	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
70	\midrule
71	\multicolumn{7}{l}{\textit{Qwen3-1.7B (seed~42)}} \\
72	ISR & 0.1 & 100 & 0.600 & 0 & \textbf{100} & 0 \\ %% registry: d113-1.7b-isr-b01-s42
73	Random & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)
74	ISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\ %% registry: d113-1.7b-isr-b03-s42
75	\bottomrule
76	\end{tabular}}
77	\caption{Goodhart landscape. PR/ISR$^*$: mean$\pm$std; H7/H1/N-H: pooled \%. $^\dagger$s42, 500 steps. $^\ddagger$N-H uncorrected upper bound (s43/s44 H8 audit unavailable). $^\star$Transient; collapses at 1000 steps (\S\ref{sec:goodhart-temporal}). $^{\dagger\dagger}$3-seed 1000-step (Appendix Table~\ref{tab:exec-only-1000}).}
78	\label{tab:goodhart-landscape}
79	\end{table}
80	
81	
82	\textbf{Low-dose ISR ($\beta{=}0.1$): stochastic delayed collapse.}
83	At $\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\geq}97\%$ H7, $0\%$ genuine within ${\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.
84	The 5-seed pooled non-hacking rate is ${\sim}23\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\%$ to $55\%$ genuine.
85	This bifurcation is stochastic: all seeds are indistinguishable in the first ${\sim}100$ steps ($\text{ISR}{\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\text{ISR}{\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.
86	Once a seed enters the H7 basin, convergence to saturation takes ${\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46
87	
88	H7 (a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by the LOO definition; \S\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.
89	Total conclusion embedding ($\text{H1}+\text{H7}$) is GRPO-universal at $68$--$100\%$ across both ISR and random conditions (Appendix Figure~\ref{fig:hacking-composition}); the specific mode (H7 vs.\ H1) within a seed is stochastic under both conditions ($\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.
90	Random yields higher PR ($83{\pm}15\%$ vs.\ $70{\pm}19\%$; $n{=}5$ each).
91	Random H7 exhibits extreme seed dependence (per-seed range: $0\%$--$91.5\%$; pooled $30\%$ is dominated by s46 at $91.5\%$ and s43 at $38.3\%$).
92	Both conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\%$ of proved samples in affected seeds: s43${=}61/61$, s44${=}89/89$), while random-induced H7 coexists with other modes ($38$--$92\%$).
93	ISR's reward signal converts H7 from a stochastic possibility into an irreversible attractor once sampled.
94	The reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\beta$ versus ${\sim}1{+}0.26\beta$ for genuine proofs (premise-count-matched), a gap of ${\sim}0.49\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.
95	
96	\textbf{The transient genuine window.}
97	During the transient window, Cochran--Mantel--Haenszel tests stratified by seed show ISR produces more genuine proofs than random controls ($\text{OR}_{\text{CMH}}{=}3.37$, 95\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; uncorrected classification, Appendix Table~\ref{tab:fol-beta01-perseed}).
98	The genuine-rate advantage is sensitive to classification methodology: the 5-seed uncorrected CMH favors ISR, but a 3-seed H8+FN-corrected analysis reverses direction ($\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction and the reduced sample size.
99	The true effect likely lies between these estimates; the transient benefit is suggestive but not robust to stricter classification.
100	This benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\%{\to}2\%$ and $55\%{\to}0\%$ genuine respectively; see below).
101	The same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.
102	Snapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000
103	
104	\textbf{Premise-count confound.}
105	The genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\ref{app:extended-discussion}).
106	
107	\textbf{Trajectory analysis: timing, not destiny.}\label{sec:goodhart-temporal}
108	Extended training (1000 steps; Appendix Figure~\ref{fig:training-isr-curves}) confirms the genuine window is transient across seeds.
109	Seed~42 declines from $17\%$ to $2\%$ genuine via H7 saturation ($16.0\%{\to}96.7\%$ H7, PR stable at ${\sim}96\%$); seed~45, which achieved the highest 500-step genuine rate ($55\%$), collapses to $0\%$ genuine through reward collapse ($\text{PR}: 42\%{\to}2\%$).
110	The two seeds exhibit distinct failure paths (H7 gaming vs.\ output collapse) but converge to the same outcome: zero genuine proofs at extended training. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42, plan002-b01-s45-1000
111	
112	\textbf{Micro-dose ISR ($\beta{=}0.05$): deterministic collapse.}
113	All three ISR seeds reach $\text{PR}{\geq}99\%$ but converge to H7a tautology (H7 $87$--$100\%$, genuine $5.1\%$), while the random control mostly fails to learn (median $\text{PR}{=}7\%$) with zero H7, confirming H7 as specific to ISR's LOO structure.
114	Below a signal-floor, ISR's genuine component is undetectable while its H7 bias remains exploitable (per-seed breakdown in Appendix~\ref{app:beta005}). %% registry: sweep-isr-b005-s42/s43/s44, sweep-random-b005-s42/s43/s44
115	
116	\textbf{Medium-dose ISR ($\beta{=}0.2$): maximum exploitation.}
117	All three seeds converge to pure H7a tautology ($0\%$ non-hacking, $n{=}290$; Appendix Table~\ref{tab:beta02-detail}). %% registry: sweep-isr-b02-s42/s43/s44
118	
119	\textbf{High-dose ISR ($\beta{=}0.3$): multi-modal Goodhart.}
120	At $\beta{=}0.3$, ISR produces extreme cross-seed instability ($\text{PR}{=}66{\pm}42\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\ref{app:beta03}).
121	The random control is equally unstable ($\text{PR}{=}54{\pm}35\%$) with $91\%$ H1 and ${\leq}4\%$ non-hacking; high-dose proxy weighting destabilizes training regardless of signal source. %% registry: plan002-additive-b03-s42/s43/s44
122	ISR vs.\ random H7 at $\beta{=}0.3$: $\text{OR}{=}13.7$, 95\% CI $[7.0, 26.8]$ (Appendix~\ref{app:beta03}).
123	
124	\textbf{Non-monotonic dose-response.}
125	The four $\beta$ levels suggest a non-monotonic pattern: $\beta\in\{0.05, 0.2\}$ converge deterministically to H7 collapse (${\geq}94\%$ H7), $\beta{=}0.3$ triggers multi-modal instability, and only $\beta{=}0.1$ sustains a transient genuine window (3 of 5 seeds).
126	Goodhart collapse is not a simple function of dose; the balance between genuine and exploit reinforcement depends on a threshold interaction between $\beta$ and rollout stochasticity.
127	
128	\subsection{Cross-Logic Diagnostic Transfer}
129	\label{sec:crosslogic}
130	
131	We replicate the FOL pipeline with Prolog/SWI-Prolog (3 seeds, $\beta{=}0.1$).
132	Under exec-only training, 2/3 seeds show $\text{ISR}^{*}{\approx}0$ despite $\text{PR}{\geq}0.56$, reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding; ISR flags both failure semantics.
133	Under ISR reward, 3/3 seeds reach $0\%$ non-hacking through three distinct mechanisms: clean H7 tautology (s42, $\text{ISR}^{*}{=}1.0$), degenerate uppercase pseudo-Prolog evading text-match classifiers (s43, functional $n_{\text{necessary}}{=}1$), and query-as-fact gaming (s44, $95/97$ proved at $n_{\text{necessary}}{=}1$).
134	Seed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.
135	We attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\ref{tab:prolog-detailed} and Figure~\ref{fig:prolog-comparison}).
136	
137	\subsection{Cross-Scale Evidence}
138	\label{sec:crossscale}
139	
140	We train Qwen3-1.7B under ISR $\beta\in\{0.1,0.3\}$ and Random $\beta{=}0.1$ (single seed, 500 steps).
141	All conditions produce $0\%$ non-hacking, but the exploit modes differ qualitatively from 4B: Random discovers H9 (contradiction injection, $\text{PR}{=}93\%$, $100\%$ \emph{ex falso}), ISR $\beta{=}0.1$ collapses to a single fixed template ($\text{ISR}^{*}{=}0.6$ at zero variance, $100\%$ H1), and ISR $\beta{=}0.3$ triggers reward collapse ($\text{PR}{=}17\%$) mirroring the 4B pattern.
142	H9 never appears at 4B scale; fixed-template mode collapse never appears at 4B; different capacities converge to different Goodhart basins under identical rewards.
143	No safe scale was observed in this single-seed comparison (Table~\ref{tab:hacking-taxonomy}).
144	
145	\subsection{Hacking Taxonomy}
146	\label{sec:taxonomy}
147	
148	
149	\begin{table}[t]
150	\centering
151	\small
152	\resizebox{\columnwidth}{!}{%
153	\begin{tabular}{lccccccc}
154	\toprule
155	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} & \textbf{1.7B$_{\text{ISR}}$} & \textbf{1.7B$_{\text{Rnd}}$} \\
156	\midrule
157	H1 embed       & 87 & 18 & 59 & 7 & 0$^\sharp$ & \textbf{100} & 0 \\
158	H7 duplicate   & 0  & \textbf{54} & 30 & 0 & 100$^\sharp$ & 0 & 0 \\
159	H8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 & 0 \\
160	H9 ex falso    & --- & --- & --- & --- & --- & 0 & \textbf{100} \\
161	Tautological   & --- & --- & --- & --- & s42 & --- & --- \\
162	Repetition     & s43 & --- & --- & --- & --- & --- & --- \\
163	Contradiction  & 1k & --- & --- & --- & --- & --- & --- \\
164	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\
165	Query-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\
166	\midrule
167	\textbf{Non-hacking} & 8  & \textbf{23}  & 8 & \textbf{92} & \textbf{0} & \textbf{0} & \textbf{0} \\
168	\bottomrule
169	\end{tabular}}
170	\caption{Nine hacking modes (\% of proved; exec/SFT: s42; ISR/Random 4B: 5-seed pooled; 1.7B: s42). H7a+H7b combined. Seed IDs mark dominant mode. $^\sharp$Prolog: strict+functional pooled. Modes marked with seed identifiers are single-seed observations.}
171	\label{tab:hacking-taxonomy}
172	\end{table}
173	
174	The nine modes (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 conditions.
175	H1, H7, and H8 account for ${>}90\%$ of hacking; H7b ($14/350$) evades text-match classifiers.
176	ISR modestly increases H7 probability ($\text{OR}{=}2.84$, $p{<}5{\times}10^{-12}$; Appendix Table~\ref{tab:bootstrap-ci}), but per-seed variance dominates.
177	All GRPO conditions show ${\geq}80\%$ pooled hacking; only SFT achieves $92.3\%$ non-hacking.
178	CMH tests confirm both effects (H7: $\text{OR}_{\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$).
179	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "f15ffa19-466c-4a70-8540-5db46f7ec284",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nCross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\\S\\ref{sec:crossscale}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}) with greedy decoding (Appendix~\\ref{app:setup}).\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ (at 500 steps) via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.97{\\pm}0.02$) with near-zero genuine output (see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\\%$, genuine $6.2\\%$; s44: H1 $85\\%$ + H8 $15\\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2\nNotably, s43 recovers from $\\text{PR}{=}13\\%$ (500 steps) to $\\text{PR}{=}96\\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$; per-seed range ${\\sim}$91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific; a 100-step checkpoint ($\\text{PR}{=}32\\%$, hacking${\\geq}31\\%$) partially controls for the PR-level confound, though the PR gap remains substantial (Appendix~\\ref{app:100step}).\nSFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.\nWhether SFT would develop similar exploits at higher prove rates remains an open question; this mechanistic argument is plausible but not conclusive.\n\n\\subsection{ISR as Reward: Goodhart Effects}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nWe present $\\beta{=}0.1$ first as the focal dose (5 seeds, trajectory analysis), then examine lower and higher doses.\nThe headline finding: ISR contains an inherent Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy} observed to produce collapse at all four tested doses ($\\beta\\in\\{0.05, 0.1, 0.2, 0.3\\}$).\nThe mechanism is structural: tautological proofs ($P{\\to}P$) receive $\\text{ISR}{=}0.75$ and single-premise-equals-conclusion constructions receive $\\text{ISR}{\\geq}0.5$, both by the LOO definition alone.\nOnce sampled during GRPO rollouts, these high-ISR tautologies create a positive feedback loop; $\\beta$ controls only the \\emph{timing} of collapse, not whether it occurs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nExec-only (1k)$^{\\dagger\\dagger}$ & --- & 97{\\scriptsize$\\pm$2} & 0.03{\\scriptsize$\\pm$.05} & 0 & --- & $\\leq$2$^{\\dagger\\dagger}$ \\\\\nISR$^\\ddagger$ & 0.1 & 70{\\scriptsize$\\pm$19} & --- & \\textbf{54} & 18 & 23$^\\star$ \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)\nRandom & 0.1 & \\textbf{83}{\\scriptsize$\\pm$15} & 0.080{\\scriptsize$\\pm$.06} & 30 & 59 & 8 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)\nISR & 0.2 & 97{\\scriptsize$\\pm$4} & 0.69{\\scriptsize$\\pm$.24} & \\textbf{99} & 0 & 0 \\\\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\\ref{tab:beta02-detail})\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-1.7B (seed~42)}} \\\\\nISR & 0.1 & 100 & 0.600 & 0 & \\textbf{100} & 0 \\\\ %% registry: d113-1.7b-isr-b01-s42\nRandom & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\\\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)\nISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\\\ %% registry: d113-1.7b-isr-b03-s42\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape. PR/ISR$^*$: mean$\\pm$std; H7/H1/N-H: pooled \\%. $^\\dagger$s42, 500 steps. $^\\ddagger$N-H uncorrected upper bound (s43/s44 H8 audit unavailable). $^\\star$Transient; collapses at 1000 steps (\\S\\ref{sec:goodhart-temporal}). $^{\\dagger\\dagger}$3-seed 1000-step (Appendix Table~\\ref{tab:exec-only-1000}).}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): stochastic delayed collapse.}\nAt $\\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\\geq}97\\%$ H7, $0\\%$ genuine within ${\\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.\nThe 5-seed pooled non-hacking rate is ${\\sim}23\\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\\%$ to $55\\%$ genuine.\nThis bifurcation is stochastic: all seeds are indistinguishable in the first ${\\sim}100$ steps ($\\text{ISR}{\\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\\text{ISR}{\\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.\nOnce a seed enters the H7 basin, convergence to saturation takes ${\\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46\n\nH7 (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by the LOO definition; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both ISR and random conditions (Appendix Figure~\\ref{fig:hacking-composition}); the specific mode (H7 vs.\\ H1) within a seed is stochastic under both conditions ($\\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.\nRandom yields higher PR ($83{\\pm}15\\%$ vs.\\ $70{\\pm}19\\%$; $n{=}5$ each).\nRandom H7 exhibits extreme seed dependence (per-seed range: $0\\%$--$91.5\\%$; pooled $30\\%$ is dominated by s46 at $91.5\\%$ and s43 at $38.3\\%$).\nBoth conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\\%$ of proved samples in affected seeds: s43${=}61/61$, s44${=}89/89$), while random-induced H7 coexists with other modes ($38$--$92\\%$).\nISR's reward signal converts H7 from a stochastic possibility into an irreversible attractor once sampled.\nThe reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\\beta$ versus ${\\sim}1{+}0.26\\beta$ for genuine proofs (premise-count-matched), a gap of ${\\sim}0.49\\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.\n\n\\textbf{The transient genuine window.}\nDuring the transient window, Cochran--Mantel--Haenszel tests stratified by seed show ISR produces more genuine proofs than random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, 95\\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; uncorrected classification, Appendix Table~\\ref{tab:fol-beta01-perseed}).\nThe genuine-rate advantage is sensitive to classification methodology: the 5-seed uncorrected CMH favors ISR, but a 3-seed H8+FN-corrected analysis reverses direction ($\\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction and the reduced sample size.\nThe true effect likely lies between these estimates; the transient benefit is suggestive but not robust to stricter classification.\nThis benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine respectively; see below).\nThe same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.\nSnapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000\n\n\\textbf{Premise-count confound.}\nThe genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\\ref{app:extended-discussion}).\n\n\\textbf{Trajectory analysis: timing, not destiny.}\\label{sec:goodhart-temporal}\nExtended training (1000 steps; Appendix Figure~\\ref{fig:training-isr-curves}) confirms the genuine window is transient across seeds.\nSeed~42 declines from $17\\%$ to $2\\%$ genuine via H7 saturation ($16.0\\%{\\to}96.7\\%$ H7, PR stable at ${\\sim}96\\%$); seed~45, which achieved the highest 500-step genuine rate ($55\\%$), collapses to $0\\%$ genuine through reward collapse ($\\text{PR}: 42\\%{\\to}2\\%$).\nThe two seeds exhibit distinct failure paths (H7 gaming vs.\\ output collapse) but converge to the same outcome: zero genuine proofs at extended training. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42, plan002-b01-s45-1000\n\n\\textbf{Micro-dose ISR ($\\beta{=}0.05$): deterministic collapse.}\nAll three ISR seeds reach $\\text{PR}{\\geq}99\\%$ but converge to H7a tautology (H7 $87$--$100\\%$, genuine $5.1\\%$), while the random control mostly fails to learn (median $\\text{PR}{=}7\\%$) with zero H7, confirming H7 as specific to ISR's LOO structure.\nBelow a signal-floor, ISR's genuine component is undetectable while its H7 bias remains exploitable (per-seed breakdown in Appendix~\\ref{app:beta005}). %% registry: sweep-isr-b005-s42/s43/s44, sweep-random-b005-s42/s43/s44\n\n\\textbf{Medium-dose ISR ($\\beta{=}0.2$): maximum exploitation.}\nAll three seeds converge to pure H7a tautology ($0\\%$ non-hacking, $n{=}290$; Appendix Table~\\ref{tab:beta02-detail}). %% registry: sweep-isr-b02-s42/s43/s44\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\\ref{app:beta03}).\nThe random control is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$) with $91\\%$ H1 and ${\\leq}4\\%$ non-hacking; high-dose proxy weighting destabilizes training regardless of signal source. %% registry: plan002-additive-b03-s42/s43/s44\nISR vs.\\ random H7 at $\\beta{=}0.3$: $\\text{OR}{=}13.7$, 95\\% CI $[7.0, 26.8]$ (Appendix~\\ref{app:beta03}).\n\n\\textbf{Non-monotonic dose-response.}\nThe four $\\beta$ levels suggest a non-monotonic pattern: $\\beta\\in\\{0.05, 0.2\\}$ converge deterministically to H7 collapse (${\\geq}94\\%$ H7), $\\beta{=}0.3$ triggers multi-modal instability, and only $\\beta{=}0.1$ sustains a transient genuine window (3 of 5 seeds).\nGoodhart collapse is not a simple function of dose; the balance between genuine and exploit reinforcement depends on a threshold interaction between $\\beta$ and rollout stochasticity.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (3 seeds, $\\beta{=}0.1$).\nUnder exec-only training, 2/3 seeds show $\\text{ISR}^{*}{\\approx}0$ despite $\\text{PR}{\\geq}0.56$, reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding; ISR flags both failure semantics.\nUnder ISR reward, 3/3 seeds reach $0\\%$ non-hacking through three distinct mechanisms: clean H7 tautology (s42, $\\text{ISR}^{*}{=}1.0$), degenerate uppercase pseudo-Prolog evading text-match classifiers (s43, functional $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, $95/97$ proved at $n_{\\text{necessary}}{=}1$).\nSeed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.\nWe attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\\ref{tab:prolog-detailed} and Figure~\\ref{fig:prolog-comparison}).\n\n\\subsection{Cross-Scale Evidence}\n\\label{sec:crossscale}\n\nWe train Qwen3-1.7B under ISR $\\beta\\in\\{0.1,0.3\\}$ and Random $\\beta{=}0.1$ (single seed, 500 steps).\nAll conditions produce $0\\%$ non-hacking, but the exploit modes differ qualitatively from 4B: Random discovers H9 (contradiction injection, $\\text{PR}{=}93\\%$, $100\\%$ \\emph{ex falso}), ISR $\\beta{=}0.1$ collapses to a single fixed template ($\\text{ISR}^{*}{=}0.6$ at zero variance, $100\\%$ H1), and ISR $\\beta{=}0.3$ triggers reward collapse ($\\text{PR}{=}17\\%$) mirroring the 4B pattern.\nH9 never appears at 4B scale; fixed-template mode collapse never appears at 4B; different capacities converge to different Goodhart basins under identical rewards.\nNo safe scale was observed in this single-seed comparison (Table~\\ref{tab:hacking-taxonomy}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{Rnd}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 59 & 7 & 0$^\\sharp$ & \\textbf{100} & 0 \\\\\nH7 duplicate   & 0  & \\textbf{54} & 30 & 0 & 100$^\\sharp$ & 0 & 0 \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 & 0 \\\\\nH9 ex falso    & --- & --- & --- & --- & --- & 0 & \\textbf{100} \\\\\nTautological   & --- & --- & --- & --- & s42 & --- & --- \\\\\nRepetition     & s43 & --- & --- & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & \\textbf{23}  & 8 & \\textbf{92} & \\textbf{0} & \\textbf{0} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Nine hacking modes (\\% of proved; exec/SFT: s42; ISR/Random 4B: 5-seed pooled; 1.7B: s42). H7a+H7b combined. Seed IDs mark dominant mode. $^\\sharp$Prolog: strict+functional pooled. Modes marked with seed identifiers are single-seed observations.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe nine modes (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 conditions.\nH1, H7, and H8 account for ${>}90\\%$ of hacking; H7b ($14/350$) evades text-match classifiers.\nISR modestly increases H7 probability ($\\text{OR}{=}2.84$, $p{<}5{\\times}10^{-12}$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.\nAll GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\nCMH tests confirm both effects (H7: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$).\n",
      "numLines": 179,
      "startLine": 1,
      "totalLines": 179
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01KUqmPxKYYjkRMqn6xeFfe6`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "de106980-67cf-49da-8a8b-4c40c6e5ba1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNJsr6mbd1D33nbZ8N7GMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17863,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17863
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

_source line 9 · 2026-05-17T17:37:24.236Z_

<details><summary>↩ Tool result · `toolu_01KUqmPxKYYjkRMqn6xeFfe6`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$; \S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR increases genuine proofs over random controls ($\text{OR}_{\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.
6	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
7	While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\S\ref{sec:goodhart}), non-monotonic dose-response across four $\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\S\ref{sec:crosslogic}).
8	These details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \emph{that} a metric will be gamed and predicting \emph{how}.
9	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "e5f9ae3c-0609-4fea-a21c-d7a0ab12b0aa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$; \\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\nAt 500 steps, ISR increases genuine proofs over random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\nWhile Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic dose-response across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).\nThese details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}.\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_019Gig2YZ7Lid92YuGfRWaAQ`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "2fe67598-a004-4021-95ea-3d853a779e08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNJsr6mbd1D33nbZ8N7GMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17863,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17863
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

_source line 11 · 2026-05-17T17:37:24.857Z_

<details><summary>↩ Tool result · `toolu_019Gig2YZ7Lid92YuGfRWaAQ`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.
5	ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.
6	A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
7	Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).
8	STA requires solvers supporting component-level input manipulation.
9	
10	\paragraph{Evaluation as temporal snapshot.}
11	All 500-step results represent a temporal snapshot, not an equilibrium.
12	Trajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\sim}23\%$ genuine window observed at 500 steps under ISR $\beta{=}0.1$ is transient (s42: $17\%{\to}2\%$; s45: $55\%{\to}0\%$ genuine).
13	Readers should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.
14	
15	\paragraph{Seed counts per dose.}
16	ISR $\beta{=}0.05$ uses three seeds (all H7-dominated); random $\beta{=}0.05$ uses three seeds with high variance ($\text{PR}{=}0\%$, $7\%$, $62\%$); $\beta{=}0.2$ uses three seeds.
17	The primary $\beta{=}0.1$ comparison uses five seeds per condition.
18	Although all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\S\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.
19	ISR $\beta{=}0.1$ s43 and s44 checkpoints were lost during disk cleanup, preventing retrospective H8 audit on these seeds; the reported 5-seed pooled non-hacking rate (23\%) is an uncorrected upper bound.
20	
21	\paragraph{Cross-scale replication.}
22	Our 1.7B experiments use a single seed.
23	Although different seeds may converge to different exploitation modes (as observed at 4B scale, where three seeds produce three distinct hacking strategies), the qualitative conclusion that hacking dominates with 0\% genuine output is robust: at 4B, all seeds hack regardless of specific mode.
24	The zero-variance mode collapse at 1.7B (100 identical outputs) indicates a sharper convergence basin at smaller scale.
25	Replicating across seeds is a natural next step.
26	
27	\paragraph{Data scale.}
28	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
29	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
30	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "a3fa01f3-8695-4eb1-9487-444278f201e5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.\nA downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nFive seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).\nSTA requires solvers supporting component-level input manipulation.\n\n\\paragraph{Evaluation as temporal snapshot.}\nAll 500-step results represent a temporal snapshot, not an equilibrium.\nTrajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\\sim}23\\%$ genuine window observed at 500 steps under ISR $\\beta{=}0.1$ is transient (s42: $17\\%{\\to}2\\%$; s45: $55\\%{\\to}0\\%$ genuine).\nReaders should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.\n\n\\paragraph{Seed counts per dose.}\nISR $\\beta{=}0.05$ uses three seeds (all H7-dominated); random $\\beta{=}0.05$ uses three seeds with high variance ($\\text{PR}{=}0\\%$, $7\\%$, $62\\%$); $\\beta{=}0.2$ uses three seeds.\nThe primary $\\beta{=}0.1$ comparison uses five seeds per condition.\nAlthough all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\\S\\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.\nISR $\\beta{=}0.1$ s43 and s44 checkpoints were lost during disk cleanup, preventing retrospective H8 audit on these seeds; the reported 5-seed pooled non-hacking rate (23\\%) is an uncorrected upper bound.\n\n\\paragraph{Cross-scale replication.}\nOur 1.7B experiments use a single seed.\nAlthough different seeds may converge to different exploitation modes (as observed at 4B scale, where three seeds produce three distinct hacking strategies), the qualitative conclusion that hacking dominates with 0\\% genuine output is robust: at 4B, all seeds hack regardless of specific mode.\nThe zero-variance mode collapse at 1.7B (100 identical outputs) indicates a sharper convergence basin at smaller scale.\nReplicating across seeds is a natural next step.\n\n\\paragraph{Data scale.}\nOur experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\\citep{folio}.\nThe training subset is selected via stratified sampling (seed 42) and held constant across all conditions.\nWhile our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.\n",
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01G9pEBTDKR2twCfKBu1qTPh`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "43a11125-2985-469a-b046-ea526fb3dc83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNJsr6mbd1D33nbZ8N7GMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17863,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17863
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

_source line 13 · 2026-05-17T17:37:25.507Z_

<details><summary>↩ Tool result · `toolu_01G9pEBTDKR2twCfKBu1qTPh`</summary>

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
25	Rollouts per prompt ($K$) & 4 \\
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
52	\paragraph{Evaluation protocol.}
53	All cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so that training-log ISR is never compared across runs.
54	The evaluation file \texttt{proofwriter\_fol\_100.jsonl} is a legacy filename containing no ProofWriter data.
55	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
56	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
57	
58	
59	\section{STA Algorithm}
60	\label{app:algorithm}
61	
62	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
63	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
64	
65	
66	\section{Extended Discussion}
67	\label{app:extended-discussion}
68	
69	\paragraph{What ISR measures, and what it does not.}
70	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
71	This is strictly weaker than semantic faithfulness (whether the formalization accurately captures the natural-language meaning).
72	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
73	ISR and downstream task performance are uncorrelated.
74	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
75	
76	Critically, low ISR carries different semantics depending on the training objective.
77	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
78	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
79	ISR values must always be interpreted relative to the optimization objective that produced them.
80	
81	\paragraph{The premise-count confound.}
82	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
83	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
84	This confound is central to ISR's Goodhart vulnerability: H7 tautologies (single premise $=$ conclusion) achieve $\text{ISR}{\geq}0.5$ \emph{by construction}, and the shorter formalizations produced by non-collapsed seeds at $\beta{=}0.1$ also inflate ISR mechanically.
85	Premise-count-matched comparison on non-hacking samples yields $\text{ISR}^{*}{=}0.258$ vs.\ $0.243$ for random ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}), confirming that even within the transient genuine window the structural benefit is negligible.
86	This bias is not specific to our setting; any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
87	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
88	
89	\begin{table}[h]
90	\centering
91	\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with H8+FN corrections (sensitivity); H7 comparison at 5-seed (primary) and 3-seed (sensitivity).}
92	\label{tab:bootstrap-ci}
93	\small
94	\resizebox{\columnwidth}{!}{%
95	\begin{tabular}{@{}lcccc@{}}
96	\toprule
97	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
98	\midrule
99	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (5-seed)}} \\
100	ISR vs.\ Random & 22.6\% {\scriptsize[18.2,27.0]} & 7.7\% {\scriptsize[5.5,10.7]} & 3.48 & ${<}10^{-8}$ \\
101	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (3-seed, H8+FN corrected)}} \\
102	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
103	\midrule
104	\multicolumn{5}{@{}l}{\textit{H7 gaming rate (5-seed)}} \\
105	ISR vs.\ Random & 54.3\% {\scriptsize[49.1,59.5]} & 29.5\% {\scriptsize[25.1,33.9]} & 2.84 & $4.82{\times}10^{-12}$ \\
106	\multicolumn{5}{@{}l}{\textit{H7 gaming rate (3-seed sensitivity)}} \\
107	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
108	\midrule
109	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
110	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
111	\bottomrule
112	\end{tabular}}
113	\\[2pt]
114	{\footnotesize 5-seed: ISR $n{=}350$, Random $n{=}414$. 3-seed: ISR $n{=}231$, Random $n{=}262$. Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
115	\end{table}
116	
117	\paragraph{Seed-level statistical analysis.}
118	To address potential inflation from within-seed dependence, we supplement pooled Fisher exact tests with two seed-aware analyses.
119	Cochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: H7 $\text{OR}_{\text{CMH}}{=}2.46$ (95\% CI $[1.85, 3.27]$, $p{=}5.6{\times}10^{-16}$); genuine $\text{OR}_{\text{CMH}}{=}3.37$ (95\% CI $[2.21, 5.13]$, $p{=}4.5{\times}10^{-10}$).
120	Seed-level permutation tests (treating each seed as a single observation, $n{=}5$ per group) yield $p{=}0.28$ (H7) and $p{=}0.26$ (genuine), consistent with the severe power limitation of $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.
121	
122	\begin{table}[h]
123	\centering
124	\caption{Per-seed classification results for ISR and Random at $\beta{=}0.1$ (500 steps, FOL). $n$ = proved samples. ISR$^*$ = proved-only mean ISR. $\dagger$~H8 audit complete; $\ddagger$~checkpoint unavailable before audit, N-H is uncorrected upper bound. Percentages are per-classifier; samples may match multiple modes. N-H uses set-exclusion per the C013 taxonomy standard.}
125	\label{tab:fol-beta01-perseed}
126	\small
127	\begin{tabular}{lrrrrrrrr}
128	\toprule
129	& Seed & PR\% & $n$ & ISR$^*$ & H7\% & H1\% & H8\% & N-H\% \\
130	\midrule
131	\multirow{6}{*}{\rotatebox{90}{ISR}}
132	& s42 & 81 & 81 & 0.415 & 16.0 & 51.9 & 14.8$\dagger$ & 17.3 \\
133	& s43 & 61 & 61 & 0.830 & 100 & 0 & ---$\ddagger$ & 0 \\
134	& s44 & 89 & 89 & 0.902 & 100 & 0 & ---$\ddagger$ & 0 \\
135	& s45 & 42 & 42 & 0.605 & 38.1 & 4.8 & 2.4 & 54.8 \\
136	& s46 & 77 & 77 & 0.411 & 14.3 & 26.0 & 5.2 & 54.5 \\
137	& \textbf{Pool} & \textbf{70$\pm$19} & \textbf{350} & --- & \textbf{54.3} & \textbf{18.0} & --- & \textbf{22.6} \\
138	\midrule
139	\multirow{6}{*}{\rotatebox{90}{Random}}
140	& s42 & 79 & 79 & 0.104 & 0 & 73.4 & 5.1$\dagger$ & 22.8 \\
141	& s43 & 94 & 94 & 0.141 & 38.3 & 59.6 & 1.1 & 1.1 \\
142	& s44 & 89 & 89 & 0.062 & 0 & 82.0 & 18.0 & 6.7 \\
143	& s45 & 58 & 58 & 0.010 & 0 & 91.4 & 0 & 8.6 \\
144	& s46 & 94 & 94 & 0.042 & 91.5 & 2.1 & 4.3 & 2.1 \\
145	& \textbf{Pool} & \textbf{83$\pm$15} & \textbf{414} & --- & \textbf{29.5} & \textbf{55.8} & --- & \textbf{7.7} \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\paragraph{H7 as inevitable exploit.}
151	ISR's LOO definition creates an inherent structural bias: tautological proofs ($P{\to}P$) receive $\text{ISR}{=}0.75$, and single-premise-equals-conclusion constructions receive $\text{ISR}{\geq}0.5$, making H7 the global ISR-maximizing exploit.
152	$\beta$ controls the \emph{timing} of collapse, not whether it occurs.
153	At all four tested doses, H7 dominates: $\beta{=}0.05$ (3 seeds, pooled H7 $93.7\%$, $n{=}253$; random s43 achieves $\text{PR}{=}62\%$ with H1 $77.4\%$ and zero H7, confirming mode specificity); $\beta{=}0.1$ (stochastic bifurcation: 2/5 seeds collapse within ${\sim}150$ steps, remaining 3/5 sustain a transient window that closes under extended training); $\beta{=}0.2$ ($100\%$ H7 across all three seeds, $n{=}290$; Table~\ref{tab:beta02-detail}); $\beta{=}0.3$ (multi-modal, s44 pure H7).
154	The random control produces $29.5\%$ H7 ($122/414$, 5-seed; per-seed: $0\%$--$91.5\%$, dominated by s46 at $91.5\%$ and s43 at $38.3\%$; s42/s44/s45 at $0\%$), random $\beta{=}0.3$ yields 4--7 H7a per seed.
155	Once a seed samples and reinforces the H7 exploit, convergence is irreversible; this absorbing-state property guarantees eventual collapse regardless of dose.
156	
157	\begin{table}[h]
158	\centering
159	\small
160	\caption{ISR $\beta{=}0.2$ per-seed results (maximum exploitation point). All seeds converge to H7a tautology with 0\% genuine.}
161	\label{tab:beta02-detail}
162	\begin{tabular}{lcccc}
163	\toprule
164	\textbf{Seed} & \textbf{PR\%} & \textbf{ISR$^*$} & \textbf{H7a\%} & \textbf{Genuine\%} \\
165	\midrule
166	s42 & 100 & 0.55 & 100 & 0 \\
167	s43 & 97 & 0.96 & 96.9 & 0 \\
168	s44 & 93 & 0.55 & 100 & 0 \\
169	\midrule
170	\textbf{Pooled} & 97$\pm$4 & 0.69$\pm$0.24 & 99.0 & \textbf{0} \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	\paragraph{Goodhart effects: implications.}
176	The finding extends beyond this specific system.
177	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet it contains an inherent structural vulnerability: by its LOO definition, tautological proofs receive artificially high ISR ($P{\to}P$ yields $\text{ISR}{=}0.75$; single-premise-equals-conclusion yields $\text{ISR}{\geq}0.5$), creating a positive feedback loop once sampled during GRPO rollouts~\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.
178	Goodhart collapse~\citep{manheim-goodhart-taxonomy} is observed at all four tested doses ($\beta{=}0.05$: 3 seeds; $\beta\in\{0.1, 0.2, 0.3\}$: 3--5 seeds each).
179	The structural bias predicts universality (H7 tautology is always the global reward-maximizing exploit regardless of $\beta$), and $\beta$ controls only the probability of early sampling and thus the timing of collapse; at $\beta{=}0.05$, three seeds confirm deterministic H7 collapse ($93.7\%$ pooled) while the matched random control at the same $\beta$ produces H1 redundancy instead ($77.4\%$), ruling out dose magnitude as the driver.
180	At moderate doses ($\beta{=}0.1$), collapse is stochastic and delayed (5 seeds bifurcate: 2 collapse rapidly, 3 sustain a transient genuine window that trajectory analysis confirms is temporary); at higher doses ($\beta{=}0.2$), collapse is immediate and universal.
181	$\beta{=}0.3$ adds reward collapse~\citep{gao-reward-overoptimization} as a competing failure mode (PR drops to 18\% in 1/3 seeds), but the underlying Goodhart vulnerability remains the same.
182	The practical implication is that ISR (and structurally similar LOO-based diagnostics) should be used exclusively as post-hoc evaluation tools, never as training rewards.
183	
184	\paragraph{Single-seed unreliability.}
185	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
186	ISR $\beta{=}0.1$ (5 seeds) shows even greater instability: 2/5 seeds collapse to H7 within ${\sim}150$ steps, while 3/5 sustain a transient genuine window.
187	The 5-seed pooled non-hacking rate is ${\sim}23\%$ at 500 steps; trajectory analysis on seeds~42 and~45 (1000 steps) confirms this is temporary ($17\%{\to}2\%$ and $55\%{\to}0\%$ genuine respectively).
188	The dominant hacking mode (H7 vs.\ H1) is stochastic within any treatment condition ($\text{CV}{>}1$).
189	Multi-seed evaluation with trajectory analysis should be standard practice for neurosymbolic RL systems; single-seed or single-checkpoint results can misrepresent a configuration's true hacking profile.
190	
191	
192	\section{Hacking Mode Definitions}
193	\label{app:hacking-modes}
194	
195	We identify nine distinct reward hacking modes across all experiments.
196	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
197	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
198	
199	\begin{figure}[t]
200	\centering
201	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
202	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: 3-seed subset s42/s43/s44, per-seed breakdown in Table~\ref{tab:fol-beta01-perseed}; 5-seed data in Table~\ref{tab:goodhart-landscape}). ISR increases H7 probability without reducing total hacking; the specific mode (H7 vs.\ H1) is seed-dependent within each condition. SFT shows near-zero hacking.}
203	\label{fig:hacking-composition}
204	\end{figure}
205	
206	\begin{table}[h]
207	\centering
208	\small
209	\resizebox{\columnwidth}{!}{%
210	\begin{tabular}{@{}llcccc@{}}
211	\toprule
212	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
213	\midrule
214	H1 & Concl.\ in premises & 87 & 18 & 71 & 7 \\
215	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
216	H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
217	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
218	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
219	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
220	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
221	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
222	\bottomrule
223	\end{tabular}}
224	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed subset (s42/s43/s44); 5-seed totals in Table~\ref{tab:goodhart-landscape}. H7 includes subtypes H7a (text-match) and H7b (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random H7 in 3-seed subset driven by seed~43 (38.3\%); 5-seed pooled: 30\% (dominated by s46 at 91.5\%). Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes. H8: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
225	\label{tab:hacking-taxonomy-app}
226	\end{table}
227	
228	\paragraph{Classifier Validation.}
229	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
230	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
231	No training data or manual annotation is used for classification.
232	
233	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
234	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
235	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
236	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
237	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
238	
239	\subsection{H8 --- Premise-Subset Gaming}
240	\label{app:h8}
241	
242	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).
243	We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
244	
245	\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
246	Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
247	
248	\paragraph{Audit scope and limitations.}
249	Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
250	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
251	Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
252	
253	\paragraph{H7 false-negative correction (H7b obfuscated tautology).}
254	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
255	Manual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
256	We classify these as \textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.
257	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier (triple gaming; \S\ref{sec:taxonomy}).
258	After correction, ISR s44 non-hacking${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.
259	
260	\paragraph{Impact on non-hacking-rate comparison.}
261	After H8 reclassification and H7 false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
262	The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
263	
264	\subsection{H1 --- Conclusion Embedding}
265	
266	\paragraph{Definition.}
267	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
268	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
269	
270	\paragraph{Example (FOL).}
271	{\small\begin{verbatim}
272	Premises:
273	  all x (bird(x) -> flies(x)).
274	  bird(tweety).
275	  flies(tweety).  % conclusion embedded
276	Conclusion: flies(tweety).
277	\end{verbatim}}
278	
279	\paragraph{ISR interaction.}
280	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
281	ISR does not distinguish trivial from substantive necessity.
282	
283	\paragraph{Prevalence.}
284	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
285	Under exec-only and Random reward, it manifests as H1 (59--91\%); under ISR reward, it shifts to H7 (54\% pooled, 5-seed).
286	
287	
288	\subsection{H7a --- Conclusion Duplication (Standard)}
289	
290	\paragraph{Definition.}
291	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
292	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
293	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
294	
295	\paragraph{Example (FOL).}
296	{\small\begin{verbatim}
297	Premises:
298	  all x ((A(x)&B(x))->(C(x)|D(x))).
299	Conclusion:
300	  all x ((A(x)&B(x))->(C(x)|D(x))).
301	\end{verbatim}}
302	
303	\paragraph{ISR interaction.}
304	ISR~$\approx 0.8$--$1.0$.
305	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
306	H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
307	
308	\paragraph{Prevalence.}
309	H7a (text-match detectable): 64.5\% (149/231, 3-seed) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%); 5-seed pooled H7: 54\% (190/350, Table~\ref{tab:goodhart-landscape}).
310	Combined H7 (H7a + H7b, 3-seed): 70.6\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).
311	Random~$\beta{=}0.1$ pooled: 29.5\% (122/414, 5-seed, all H7a; driven by s46 at 91.5\% and s43 at 38.3\%; s42/s44/s45 at 0\%).
312	
313	
314	\subsection{H7b --- Obfuscated Tautology}
315	
316	\paragraph{Definition.}
317	A single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.
318	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
319	
320	\paragraph{Example (FOL, vacuous quantifier wrapping).}
321	{\small\begin{verbatim}
322	Premises:
323	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
324	Conclusion:
325	  all x ((A(x)&B(x))->(C(x)|D(x))).
326	\end{verbatim}}
327	The premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.
328	
329	\paragraph{ISR interaction.}
330	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
331	H7b simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).
332	This triple gaming makes H7b the most complete Goodhart case we observe.
333	
334	\paragraph{Prevalence.}
335	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
336	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
337	
338	
339	\subsection{Tautological Collapse}
340	
341	\paragraph{Definition.}
342	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
343	
344	\paragraph{Example (FOL).}
345	\begin{verbatim}
346	Premises: p(a).
347	Conclusion: p(a).
348	\end{verbatim}
349	
350	\paragraph{ISR interaction.}
351	ISR~$=1.0$ (the sole premise is necessary).
352	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
353	
354	\paragraph{Prevalence.}
355	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
356	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
357	
358	
359	\subsection{Repetition Collapse}
360	
361	\paragraph{Definition.}
362	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
363	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
364	
365	\paragraph{Example (Prolog).}
366	\begin{verbatim}
367	penguin(fido).
368	penguin(fido).
369	penguin(fido).
370	... (repeated to 512 tokens)
371	query(penguin(fido)).
372	\end{verbatim}
373	
374	\paragraph{ISR interaction.}
375	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
376	ISR correctly diagnoses this degeneration.
377	
378	\paragraph{Prevalence.}
379	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
380	
381	
382	\subsection{Complexity-without-Utility}
383	
384	\paragraph{Definition.}
385	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous; none is individually necessary for the proof.
386	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
387	
388	\paragraph{Example (FOL).}
389	{\small\begin{verbatim}
390	Premises:
391	  all x all y (R(x,y) ->
392	    exists z (S(x,z) & T(z,y))).
393	  all x (P(x) -> Q(x)).
394	  P(a).            % only this needed
395	Conclusion: Q(a).
396	\end{verbatim}}
397	
398	\paragraph{ISR interaction.}
399	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
400	This is the mode ISR is best calibrated for.
401	
402	\paragraph{Prevalence.}
403	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
404	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
405	
406	
407	\subsection{Contradiction Explosion}
408	
409	\paragraph{Definition.}
410	The component count grows unboundedly over training.
411	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
412	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
413	
414	\paragraph{Example (FOL, 1000-step exec-only).}
415	{\small\begin{verbatim}
416	Premises:
417	  c1. c2. c3. ... c18. % 18.55 mean
418	  % conclusion embedded among premises
419	Conclusion: Q(a).
420	\end{verbatim}}
421	
422	\paragraph{ISR interaction.}
423	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
424	
425	\paragraph{Prevalence.}
426	Observed in extended exec-only training (seed~42, 1000 steps).
427	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
428	
429	
430	\subsection{Query-as-Fact Gaming}
431	
432	\paragraph{Definition.}
433	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
434	Prolog trivially proves the query by unifying with the fact.
435	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
436	
437	\paragraph{Example (Prolog).}
438	\begin{verbatim}
439	% NL: "Fido is happy."
440	% Model output:
441	fido_is_happy.
442	:- fido_is_happy.     % query = fact
443	\end{verbatim}
444	
445	\paragraph{ISR interaction.}
446	ISR~$\approx 0.9$--$1.0$.
447	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
448	Functionally equivalent to H7 but with a distinct surface mechanism.
449	
450	\paragraph{Prevalence.}
451	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
452	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
453	
454	
455	\subsection{H9 --- Ex Falso Quodlibet (Contradiction Injection)}
456	
457	\paragraph{Definition.}
458	The model generates a premise set containing logically contradictory assertions (e.g., $P(x)$ and $\neg P(x)$).
459	From contradictory premises, any conclusion follows by the \emph{ex falso quodlibet} principle, rendering the proof semantically vacuous regardless of the conclusion's content.
460	Unlike the ``contradiction explosion'' mode observed in 4B exec-only at 1000 steps (where contradictions arise incidentally among inflated premise counts), H9 is a \emph{targeted} strategy: the model constructs minimal contradictory pairs that directly enable the proof.
461	
462	\paragraph{Example (FOL).}
463	{\small\begin{verbatim}
464	Premises:
465	  all x (bird(x) -> flies(x)).
466	  bird(tweety).
467	  -bird(tweety).  % contradicts above
468	Conclusion: happy(tweety).
469	% Proof: bird(tweety) & -bird(tweety) -> False -> anything
470	\end{verbatim}}
471	
472	\paragraph{ISR interaction.}
473	ISR~$>0$ because each side of the contradiction is individually necessary under LOO: removing $P(x)$ leaves $\neg P(x)$ alone, which cannot derive a contradiction; removing $\neg P(x)$ leaves the premises consistent but insufficient to derive an unrelated conclusion.
474	The LOO test thus registers both contradictory premises as ``necessary,'' inflating ISR despite the formalization being semantically vacuous.
475	
476	\paragraph{Prevalence.}
477	Observed exclusively in Qwen3-1.7B under Random $\beta{=}0.1$ (seed~42, 500 steps, proper train/eval separation): 100\% of proved samples ($n{=}93$) exhibit H9.
478	Under ISR $\beta{=}0.1$ with the same model, H9 does not appear; the model instead converges to fixed-template H1 ($\text{ISR}{=}0.6$, zero variance), indicating that ISR reward redirects the hacking pathway from H9 to H1.
479	Not observed in any Qwen3-4B experiment across all conditions and seeds tested. %% registry: d113-1.7b-random-b01-s42
480	
481	
482	\section{Per-Seed Detailed Results}
483	\label{app:detailed-results}
484	
485	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
486	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
487	ISR values are proved-only ISR$^*$.
488	
489	\begin{table*}[t]
490	\centering
491	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\P$Inferred from ISR profile and contradiction-explosion pattern; formal text-match taxonomy not run on this checkpoint.}
492	\label{tab:fol-detailed}
493	\label{tab:fol-beta01-detailed}
494	\footnotesize
495	\setlength{\tabcolsep}{3pt}
496	\begin{tabular}{@{}llccccccl@{}}
497	\toprule
498	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
499	\midrule
500	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
501	Base model (no training)
502	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
503	Ground-truth FOL
504	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
505	SFT
506	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
507	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
508	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
509	\cmidrule(l){2-9}
510	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
511	\midrule
512	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
513	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
514	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\%$ \\
515	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100$^\P$ & 0$^\P$ & Contradiction explosion \\
516	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
517	  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & H1 dominant \\
518	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
519	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & H8${=}15\%$ \\
520	\cmidrule(l){2-9}
521	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
522	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.97{\pm}0.02$} & & \makebox[0pt][l]{$0.03{\pm}0.05$} & & \makebox[0pt][l]{$2.1{\pm}3.6$} & 1000-step \\
523	\midrule
524	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
525	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
526	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\
527	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\
528	\cmidrule(l){2-9}
529	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
530	\midrule
531	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
532	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
533	\midrule
534	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
535	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
536	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\
537	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\cap$H8: 6) \\
538	\cmidrule(l){2-9}
539	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.87{\pm}0.08$} & & \makebox[0pt][l]{$0.117{\pm}0.042$} & & & H7 seed-dep.: 0/38/0\% \\
540	\midrule
541	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
542	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
543	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{N-H}}{=}3$ \\
544	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
545	\cmidrule(l){2-9}
546	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & & \\
547	\bottomrule
548	\end{tabular}
549	\end{table*}
550	
551	\begin{table}[h]
552	\centering
553	\caption{Exec-only baseline at 1000 steps (3 seeds). All seeds converge to high PR with near-zero genuine output. s42 evaluated with ISR metrics only; hacking taxonomy unavailable.}
554	\label{tab:exec-only-1000}
555	\small
556	\begin{tabular}{lrrrrrr}
557	\toprule
558	Seed & PR\% & $n$ & H7\% & H1\% & H8\% & N-H\% \\
559	\midrule
560	s42 & 96 & 96 & 0 & --- & --- & --- \\
561	s43 & 96 & 96 & 0 & 93.8 & 0 & 6.2 \\
562	s44 & 100 & 100 & 0 & 85.0 & 15.0 & 0 \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	
568	\begin{figure}[t]
569	\centering
570	\includegraphics[width=0.95\columnwidth]{figures/fig4_prolog_comparison.pdf}
571	\caption{Cross-logic results. \textbf{Left}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \textbf{Right}: Prolog ISR-reward gaming-mode composition: all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
572	\label{fig:prolog-comparison}
573	\end{figure}
574	
575	\begin{table*}[t]
576	\centering
577	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
578	\label{tab:prolog-detailed}
579	\small
580	\begin{tabular}{@{}llcccccl@{}}
581	\toprule
582	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
583	\midrule
584	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
585	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
586	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
587	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
588	\cmidrule(l){2-8}
589	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
590	\midrule
591	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
592	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
593	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
594	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
595	\cmidrule(l){2-8}
596	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
597	\bottomrule
598	\end{tabular}
599	
600	\vspace{4pt}
601	{\footnotesize
602	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
603	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\
604	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
605	}
606	\end{table*}
607	
608	\begin{figure}[t]
609	\centering
610	\includegraphics[width=0.95\columnwidth]{figures/fig5_training_isr_curves.pdf}
611	\caption{Training ISR trajectories across reward conditions. ISR $\beta{=}0.1$ seeds rise rapidly toward $\text{ISR}{\approx}1$ (Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\text{ISR}{\geq}0.5$ by construction), not genuine structural quality; random $\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}
612	\label{fig:training-isr-curves}
613	\end{figure}
614	
615	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
616	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
617	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
618	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
619	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
620	
621	\paragraph{Prolog: consistent gaming across all seeds via three distinct pathways.}
622	All three Prolog exec+ISR seeds exhibit Goodhart effects with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
623	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
624	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
625	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
626	The diversity of gaming pathways across seeds, despite identical training data and reward function, demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
627	
628	\subsection{Per-Seed Results at $\beta{=}0.3$}
629	\label{app:beta03}
630	
631	Table~\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\beta{=}0.3$.
632	The three ISR seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
633	
634	\begin{table}[h]
635	\centering
636	\caption{Per-seed results at $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}
637	\label{tab:beta03-detailed}
638	\small
639	\resizebox{\columnwidth}{!}{%
640	\begin{tabular}{@{}llcccccl@{}}
641	\toprule
642	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Mode} \\
643	\midrule
644	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
645	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\
646	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & H1 shortcutting \\
647	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure H7 gaming \\
648	\cmidrule(l){2-8}
649	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.66{\pm}0.42$} & & \makebox[0pt][l]{$0.39{\pm}0.31$} & & \\
650	\midrule
651	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
652	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\
653	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{N-H}}{=}3$ \\
654	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
655	\cmidrule(l){2-8}
656	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & \\
657	\bottomrule
658	\end{tabular}}
659	\end{table}
660	
661	\subsection{Per-Seed Results at $\beta{=}0.05$}
662	\label{app:beta005}
663	
664	The 3-seed random control at $\beta{=}0.05$ is highly unstable: s42 fails entirely ($\text{PR}{=}0\%$), s44 barely learns ($\text{PR}{=}7\%$, H1 $71\%$, genuine $0\%$), and only s43 reaches moderate output ($\text{PR}{=}62\%$, H1 $77\%$, genuine $13\%$).
665	The single random seed that learns (s43) shows higher genuine output than ISR ($13\%$ vs.\ $5.1\%$ pooled), consistent with a signal-floor below which ISR's genuine component is undetectable while its H7 bias remains exploitable.
666	
667	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
668	\label{app:100step}
669	
670	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
671	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
672	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
673	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
674	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
675	
676	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
677	\label{app:o1-ablation}
678	
679	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
680	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
681	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$ (functionally zero), compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
682	
683	\paragraph{ISR signal vs.\ training dynamics.}
684	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
685	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
686	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
687	The result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.
688	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "3a3fb578-9cd6-4626-9274-1b471e71793a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nAll cross-run ISR values are recomputed uniformly by a single evaluator (\\texttt{eval\\_sta.py}) so that training-log ISR is never compared across runs.\nThe evaluation file \\texttt{proofwriter\\_fol\\_100.jsonl} is a legacy filename containing no ProofWriter data.\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures, and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness (whether the formalization accurately captures the natural-language meaning).\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound is central to ISR's Goodhart vulnerability: H7 tautologies (single premise $=$ conclusion) achieve $\\text{ISR}{\\geq}0.5$ \\emph{by construction}, and the shorter formalizations produced by non-collapsed seeds at $\\beta{=}0.1$ also inflate ISR mechanically.\nPremise-count-matched comparison on non-hacking samples yields $\\text{ISR}^{*}{=}0.258$ vs.\\ $0.243$ for random ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}), confirming that even within the transient genuine window the structural benefit is negligible.\nThis bias is not specific to our setting; any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table}[h]\n\\centering\n\\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with H8+FN corrections (sensitivity); H7 comparison at 5-seed (primary) and 3-seed (sensitivity).}\n\\label{tab:bootstrap-ci}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (5-seed)}} \\\\\nISR vs.\\ Random & 22.6\\% {\\scriptsize[18.2,27.0]} & 7.7\\% {\\scriptsize[5.5,10.7]} & 3.48 & ${<}10^{-8}$ \\\\\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (3-seed, H8+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{H7 gaming rate (5-seed)}} \\\\\nISR vs.\\ Random & 54.3\\% {\\scriptsize[49.1,59.5]} & 29.5\\% {\\scriptsize[25.1,33.9]} & 2.84 & $4.82{\\times}10^{-12}$ \\\\\n\\multicolumn{5}{@{}l}{\\textit{H7 gaming rate (3-seed sensitivity)}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\\\[2pt]\n{\\footnotesize 5-seed: ISR $n{=}350$, Random $n{=}414$. 3-seed: ISR $n{=}231$, Random $n{=}262$. Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table}\n\n\\paragraph{Seed-level statistical analysis.}\nTo address potential inflation from within-seed dependence, we supplement pooled Fisher exact tests with two seed-aware analyses.\nCochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: H7 $\\text{OR}_{\\text{CMH}}{=}2.46$ (95\\% CI $[1.85, 3.27]$, $p{=}5.6{\\times}10^{-16}$); genuine $\\text{OR}_{\\text{CMH}}{=}3.37$ (95\\% CI $[2.21, 5.13]$, $p{=}4.5{\\times}10^{-10}$).\nSeed-level permutation tests (treating each seed as a single observation, $n{=}5$ per group) yield $p{=}0.28$ (H7) and $p{=}0.26$ (genuine), consistent with the severe power limitation of $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed classification results for ISR and Random at $\\beta{=}0.1$ (500 steps, FOL). $n$ = proved samples. ISR$^*$ = proved-only mean ISR. $\\dagger$~H8 audit complete; $\\ddagger$~checkpoint unavailable before audit, N-H is uncorrected upper bound. Percentages are per-classifier; samples may match multiple modes. N-H uses set-exclusion per the C013 taxonomy standard.}\n\\label{tab:fol-beta01-perseed}\n\\small\n\\begin{tabular}{lrrrrrrrr}\n\\toprule\n& Seed & PR\\% & $n$ & ISR$^*$ & H7\\% & H1\\% & H8\\% & N-H\\% \\\\\n\\midrule\n\\multirow{6}{*}{\\rotatebox{90}{ISR}}\n& s42 & 81 & 81 & 0.415 & 16.0 & 51.9 & 14.8$\\dagger$ & 17.3 \\\\\n& s43 & 61 & 61 & 0.830 & 100 & 0 & ---$\\ddagger$ & 0 \\\\\n& s44 & 89 & 89 & 0.902 & 100 & 0 & ---$\\ddagger$ & 0 \\\\\n& s45 & 42 & 42 & 0.605 & 38.1 & 4.8 & 2.4 & 54.8 \\\\\n& s46 & 77 & 77 & 0.411 & 14.3 & 26.0 & 5.2 & 54.5 \\\\\n& \\textbf{Pool} & \\textbf{70$\\pm$19} & \\textbf{350} & --- & \\textbf{54.3} & \\textbf{18.0} & --- & \\textbf{22.6} \\\\\n\\midrule\n\\multirow{6}{*}{\\rotatebox{90}{Random}}\n& s42 & 79 & 79 & 0.104 & 0 & 73.4 & 5.1$\\dagger$ & 22.8 \\\\\n& s43 & 94 & 94 & 0.141 & 38.3 & 59.6 & 1.1 & 1.1 \\\\\n& s44 & 89 & 89 & 0.062 & 0 & 82.0 & 18.0 & 6.7 \\\\\n& s45 & 58 & 58 & 0.010 & 0 & 91.4 & 0 & 8.6 \\\\\n& s46 & 94 & 94 & 0.042 & 91.5 & 2.1 & 4.3 & 2.1 \\\\\n& \\textbf{Pool} & \\textbf{83$\\pm$15} & \\textbf{414} & --- & \\textbf{29.5} & \\textbf{55.8} & --- & \\textbf{7.7} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{H7 as inevitable exploit.}\nISR's LOO definition creates an inherent structural bias: tautological proofs ($P{\\to}P$) receive $\\text{ISR}{=}0.75$, and single-premise-equals-conclusion constructions receive $\\text{ISR}{\\geq}0.5$, making H7 the global ISR-maximizing exploit.\n$\\beta$ controls the \\emph{timing} of collapse, not whether it occurs.\nAt all four tested doses, H7 dominates: $\\beta{=}0.05$ (3 seeds, pooled H7 $93.7\\%$, $n{=}253$; random s43 achieves $\\text{PR}{=}62\\%$ with H1 $77.4\\%$ and zero H7, confirming mode specificity); $\\beta{=}0.1$ (stochastic bifurcation: 2/5 seeds collapse within ${\\sim}150$ steps, remaining 3/5 sustain a transient window that closes under extended training); $\\beta{=}0.2$ ($100\\%$ H7 across all three seeds, $n{=}290$; Table~\\ref{tab:beta02-detail}); $\\beta{=}0.3$ (multi-modal, s44 pure H7).\nThe random control produces $29.5\\%$ H7 ($122/414$, 5-seed; per-seed: $0\\%$--$91.5\\%$, dominated by s46 at $91.5\\%$ and s43 at $38.3\\%$; s42/s44/s45 at $0\\%$), random $\\beta{=}0.3$ yields 4--7 H7a per seed.\nOnce a seed samples and reinforces the H7 exploit, convergence is irreversible; this absorbing-state property guarantees eventual collapse regardless of dose.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{ISR $\\beta{=}0.2$ per-seed results (maximum exploitation point). All seeds converge to H7a tautology with 0\\% genuine.}\n\\label{tab:beta02-detail}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR$^*$} & \\textbf{H7a\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\ns42 & 100 & 0.55 & 100 & 0 \\\\\ns43 & 97 & 0.96 & 96.9 & 0 \\\\\ns44 & 93 & 0.55 & 100 & 0 \\\\\n\\midrule\n\\textbf{Pooled} & 97$\\pm$4 & 0.69$\\pm$0.24 & 99.0 & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Goodhart effects: implications.}\nThe finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet it contains an inherent structural vulnerability: by its LOO definition, tautological proofs receive artificially high ISR ($P{\\to}P$ yields $\\text{ISR}{=}0.75$; single-premise-equals-conclusion yields $\\text{ISR}{\\geq}0.5$), creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\nGoodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses ($\\beta{=}0.05$: 3 seeds; $\\beta\\in\\{0.1, 0.2, 0.3\\}$: 3--5 seeds each).\nThe structural bias predicts universality (H7 tautology is always the global reward-maximizing exploit regardless of $\\beta$), and $\\beta$ controls only the probability of early sampling and thus the timing of collapse; at $\\beta{=}0.05$, three seeds confirm deterministic H7 collapse ($93.7\\%$ pooled) while the matched random control at the same $\\beta$ produces H1 redundancy instead ($77.4\\%$), ruling out dose magnitude as the driver.\nAt moderate doses ($\\beta{=}0.1$), collapse is stochastic and delayed (5 seeds bifurcate: 2 collapse rapidly, 3 sustain a transient genuine window that trajectory analysis confirms is temporary); at higher doses ($\\beta{=}0.2$), collapse is immediate and universal.\n$\\beta{=}0.3$ adds reward collapse~\\citep{gao-reward-overoptimization} as a competing failure mode (PR drops to 18\\% in 1/3 seeds), but the underlying Goodhart vulnerability remains the same.\nThe practical implication is that ISR (and structurally similar LOO-based diagnostics) should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ (5 seeds) shows even greater instability: 2/5 seeds collapse to H7 within ${\\sim}150$ steps, while 3/5 sustain a transient genuine window.\nThe 5-seed pooled non-hacking rate is ${\\sim}23\\%$ at 500 steps; trajectory analysis on seeds~42 and~45 (1000 steps) confirms this is temporary ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine respectively).\nThe dominant hacking mode (H7 vs.\\ H1) is stochastic within any treatment condition ($\\text{CV}{>}1$).\nMulti-seed evaluation with trajectory analysis should be standard practice for neurosymbolic RL systems; single-seed or single-checkpoint results can misrepresent a configuration's true hacking profile.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify nine distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: 3-seed subset s42/s43/s44, per-seed breakdown in Table~\\ref{tab:fol-beta01-perseed}; 5-seed data in Table~\\ref{tab:goodhart-landscape}). ISR increases H7 probability without reducing total hacking; the specific mode (H7 vs.\\ H1) is seed-dependent within each condition. SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nH8 & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed subset (s42/s43/s44); 5-seed totals in Table~\\ref{tab:goodhart-landscape}. H7 includes subtypes H7a (text-match) and H7b (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random H7 in 3-seed subset driven by seed~43 (38.3\\%); 5-seed pooled: 30\\% (dominated by s46 at 91.5\\%). Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes. H8: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\subsection{H8 --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).\nWe term this \\textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull H8 audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.\n\n\\paragraph{H7 false-negative correction (H7b obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier (triple gaming; \\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter H8 reclassification and H7 false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (H7, H8) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (59--91\\%); under ISR reward, it shifts to H7 (54\\% pooled, 5-seed).\n\n\n\\subsection{H7a --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nH7a (text-match detectable): 64.5\\% (149/231, 3-seed) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%); 5-seed pooled H7: 54\\% (190/350, Table~\\ref{tab:goodhart-landscape}).\nCombined H7 (H7a + H7b, 3-seed): 70.6\\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 29.5\\% (122/414, 5-seed, all H7a; driven by s46 at 91.5\\% and s43 at 38.3\\%; s42/s44/s45 at 0\\%).\n\n\n\\subsection{H7b --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\nThe premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nH7b simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).\nThis triple gaming makes H7b the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% H7, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous; none is individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\subsection{H9 --- Ex Falso Quodlibet (Contradiction Injection)}\n\n\\paragraph{Definition.}\nThe model generates a premise set containing logically contradictory assertions (e.g., $P(x)$ and $\\neg P(x)$).\nFrom contradictory premises, any conclusion follows by the \\emph{ex falso quodlibet} principle, rendering the proof semantically vacuous regardless of the conclusion's content.\nUnlike the ``contradiction explosion'' mode observed in 4B exec-only at 1000 steps (where contradictions arise incidentally among inflated premise counts), H9 is a \\emph{targeted} strategy: the model constructs minimal contradictory pairs that directly enable the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  -bird(tweety).  % contradicts above\nConclusion: happy(tweety).\n% Proof: bird(tweety) & -bird(tweety) -> False -> anything\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$>0$ because each side of the contradiction is individually necessary under LOO: removing $P(x)$ leaves $\\neg P(x)$ alone, which cannot derive a contradiction; removing $\\neg P(x)$ leaves the premises consistent but insufficient to derive an unrelated conclusion.\nThe LOO test thus registers both contradictory premises as ``necessary,'' inflating ISR despite the formalization being semantically vacuous.\n\n\\paragraph{Prevalence.}\nObserved exclusively in Qwen3-1.7B under Random $\\beta{=}0.1$ (seed~42, 500 steps, proper train/eval separation): 100\\% of proved samples ($n{=}93$) exhibit H9.\nUnder ISR $\\beta{=}0.1$ with the same model, H9 does not appear; the model instead converges to fixed-template H1 ($\\text{ISR}{=}0.6$, zero variance), indicating that ISR reward redirects the hacking pathway from H9 to H1.\nNot observed in any Qwen3-4B experiment across all conditions and seeds tested. %% registry: d113-1.7b-random-b01-s42\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\\P$Inferred from ISR profile and contradiction-explosion pattern; formal text-match taxonomy not run on this checkpoint.}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & \\makebox[0pt][l]{$0.130$} & & \\makebox[0pt][l]{$0.595$} & & \\makebox[0pt][l]{\\textbf{92.3}} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100$^\\P$ & 0$^\\P$ & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & H1 dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & H8${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.97{\\pm}0.02$} & & \\makebox[0pt][l]{$0.03{\\pm}0.05$} & & \\makebox[0pt][l]{$2.1{\\pm}3.6$} & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed H1+H7+H8 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\\cap$H8: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.87{\\pm}0.08$} & & \\makebox[0pt][l]{$0.117{\\pm}0.042$} & & & H7 seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Exec-only baseline at 1000 steps (3 seeds). All seeds converge to high PR with near-zero genuine output. s42 evaluated with ISR metrics only; hacking taxonomy unavailable.}\n\\label{tab:exec-only-1000}\n\\small\n\\begin{tabular}{lrrrrrr}\n\\toprule\nSeed & PR\\% & $n$ & H7\\% & H1\\% & H8\\% & N-H\\% \\\\\n\\midrule\ns42 & 96 & 96 & 0 & --- & --- & --- \\\\\ns43 & 96 & 96 & 0 & 93.8 & 0 & 6.2 \\\\\ns44 & 100 & 100 & 0 & 85.0 & 15.0 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Left}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \\textbf{Right}: Prolog ISR-reward gaming-mode composition: all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.699{\\pm}0.45$} & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not genuine structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: consistent gaming across all seeds via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart effects with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds, despite identical training data and reward function, demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\\beta{=}0.3$.\nThe three ISR seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & H1 shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure H7 gaming \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.66{\\pm}0.42$} & & \\makebox[0pt][l]{$0.39{\\pm}0.31$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Per-Seed Results at $\\beta{=}0.05$}\n\\label{app:beta005}\n\nThe 3-seed random control at $\\beta{=}0.05$ is highly unstable: s42 fails entirely ($\\text{PR}{=}0\\%$), s44 barely learns ($\\text{PR}{=}7\\%$, H1 $71\\%$, genuine $0\\%$), and only s43 reaches moderate output ($\\text{PR}{=}62\\%$, H1 $77\\%$, genuine $13\\%$).\nThe single random seed that learns (s43) shows higher genuine output than ISR ($13\\%$ vs.\\ $5.1\\%$ pooled), consistent with a signal-floor below which ISR's genuine component is undetectable while its H7 bias remains exploitable.\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nTo justify the per-clause LOO design (\\S\\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved \\emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nThe reward becomes $r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$.\nAfter 500 steps (seed~42), this variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$ (functionally zero), compared to $\\text{ISR}^*{=}0.132$ under standard exec-only and $\\text{ISR}^*{=}0.42$ under ISR $\\beta{=}0.1$.\n\n\\paragraph{ISR signal vs.\\ training dynamics.}\nAt the \\emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.\nAt the \\emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.\nThis confound depresses prove rate by 30 percentage points ($63\\%$ vs.\\ $93\\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.\nThe result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.\n",
      "numLines": 688,
      "startLine": 1,
      "totalLines": 688
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

Now let me read the introduction and abstract files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "e6590647-7d8a-4f0e-91bf-a36f98ec05fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNfj2sN5VLaGvawRWt4Yju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27097,
      "cache_read_input_tokens": 29704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27097
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01PJLab9kK7pvC95vcdmiKDG`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "f0bc05ca-d0d1-4924-bd35-5169050d4010",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNfj2sN5VLaGvawRWt4Yju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27097,
      "cache_read_input_tokens": 29704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27097
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

_source line 16 · 2026-05-17T17:37:33.021Z_

<details><summary>↩ Tool result · `toolu_01PJLab9kK7pvC95vcdmiKDG`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\pm}2\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Irreducible Solver Rate} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
16	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
17	ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
18	
19	\paragraph{ISR as diagnostic.}
20	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (seed~42; 99.5\% degradation) while PR rises $32\%{\to}96\%$.
21	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
22	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven.
23	
24	\paragraph{ISR as reward: Goodhart collapse at all tested doses.}
25	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR contains an inherent structural vulnerability: tautological proofs (a single premise identical to the conclusion) receive $\text{ISR}{\geq}0.5$ by construction, and implication tautologies ($P{\to}P$) receive $\text{ISR}{=}0.75$, creating a positive feedback loop once sampled during GRPO rollouts~\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.
26	Goodhart collapse~\citep{manheim-goodhart-taxonomy} is observed at all four tested doses (trajectory-confirmed at $\beta{=}0.1$): $\beta$ controls \emph{when} collapse occurs, not \emph{whether}.
27	At moderate doses, collapse is stochastic and delayed: seeds bifurcate between rapid convergence to tautology and a transient genuine window that closes under extended training.
28	Snapshot evaluation would overestimate ISR's benefit; trajectory analysis confirms the window is temporary.
29	The effect transfers to Prolog (3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming}) and is preliminarily observed at 1.7B scale (qualitatively novel gaming modes in single-seed evaluation).
30	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer at any dose.}
31	
32	\paragraph{Contributions.}
33	Across 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, and up to 1000 steps, we contribute: (\textbf{C1}) We empirically demonstrate ISR as a diagnostic for GRPO reward hacking, revealing a 99.5\% collapse trajectory invisible to PR, with an SFT control consistent with RL-specific failure (\S\ref{sec:diagnostic}); (\textbf{C2}) an empirical instance of Goodhart collapse~\citep{manheim-goodhart-taxonomy} at all four tested doses: ISR's structural bias ($\text{ISR}{\geq}0.5$ for tautological proofs) creates a positive feedback loop; the genuine window at moderate $\beta$ is suggestive but non-robust, and $\beta$ controls only timing, not outcome (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\S\ref{sec:crosslogic}); (\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \emph{ex falso} mode, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
34	These are cautionary results: snapshot evaluation of structural rewards can overestimate their benefit; only trajectory analysis reveals the transient nature of apparent improvement.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "0efd35f9-e0fe-42c1-9e24-1b7df005f011",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nGRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\\pm}2\\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.\nEach seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.\n\n\\paragraph{The execution-only blind spot.}\nProve rate, the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), which applies \\emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Irreducible Solver Rate} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (seed~42; 99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven.\n\n\\paragraph{ISR as reward: Goodhart collapse at all tested doses.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR contains an inherent structural vulnerability: tautological proofs (a single premise identical to the conclusion) receive $\\text{ISR}{\\geq}0.5$ by construction, and implication tautologies ($P{\\to}P$) receive $\\text{ISR}{=}0.75$, creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\nGoodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): $\\beta$ controls \\emph{when} collapse occurs, not \\emph{whether}.\nAt moderate doses, collapse is stochastic and delayed: seeds bifurcate between rapid convergence to tautology and a transient genuine window that closes under extended training.\nSnapshot evaluation would overestimate ISR's benefit; trajectory analysis confirms the window is temporary.\nThe effect transfers to Prolog (3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming}) and is preliminarily observed at 1.7B scale (qualitatively novel gaming modes in single-seed evaluation).\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer at any dose.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, and up to 1000 steps, we contribute: (\\textbf{C1}) We empirically demonstrate ISR as a diagnostic for GRPO reward hacking, revealing a 99.5\\% collapse trajectory invisible to PR, with an SFT control consistent with RL-specific failure (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) an empirical instance of Goodhart collapse~\\citep{manheim-goodhart-taxonomy} at all four tested doses: ISR's structural bias ($\\text{ISR}{\\geq}0.5$ for tautological proofs) creates a positive feedback loop; the genuine window at moderate $\\beta$ is suggestive but non-robust, and $\\beta$ controls only timing, not outcome (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \\emph{ex falso} mode, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results: snapshot evaluation of structural rewards can overestimate their benefit; only trajectory analysis reveals the transient nature of apparent improvement.\n",
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01VW1u5iZKfFpBsDMEH1etkt`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "f4f0629d-2476-4ddc-beb6-e7154c981247",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNfj2sN5VLaGvawRWt4Yju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27097,
      "cache_read_input_tokens": 29704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27097
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

_source line 18 · 2026-05-17T17:37:33.480Z_

<details><summary>↩ Tool result · `toolu_01VW1u5iZKfFpBsDMEH1etkt`</summary>

```text
1	\begin{abstract}
2	GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\pm}2\%$, three seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\% non-hacking on identical data, suggesting the failure is RL-specific.
4	Repurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.
5	Across 6 conditions, 2 logic types, and 2 model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
6	\end{abstract}
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "4b0eabfc-69aa-4add-adcc-b5ddc16afb03",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
      "content": "\\begin{abstract}\nGRPO-trained formalizers converge to high prove rates on FOLIO ($97{\\pm}2\\%$, three seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.\nWe propose \\emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\\% non-hacking on identical data, suggesting the failure is RL-specific.\nRepurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.\nAcross 6 conditions, 2 logic types, and 2 model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}\n\\end{abstract}\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_018DFxeeEYdYWPk68Ci1Mwa4`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "013401d9-150d-493a-b04e-6e9cf5837c5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNfj2sN5VLaGvawRWt4Yju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27097,
      "cache_read_input_tokens": 29704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27097
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

_source line 20 · 2026-05-17T17:37:33.756Z_

<details><summary>↩ Tool result · `toolu_018DFxeeEYdYWPk68Ci1Mwa4`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1-2025} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; recent work extends PRMs to multi-domain settings~\citep{zeng2025versaprm} and process-level reasoning~\citep{khalifa2025thinkprm}. \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empirically in RLHF and frontier models~\citep{amodei2016concrete, krakovna2020specification, gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
16	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.
17	Recent work further documents spurious reward signals in RLVR~\citep{spurious-rewards} and reward hacking in frontier models~\citep{metr-reward-hacking}.
18	Our setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \emph{emerges during RL training} rather than at inference time (cf.\ shortcut learning in supervised settings~\citep{geirhos2020shortcut}); and the effect operates at a diagnostic level, where the metric designed to detect gaming becomes gamed when optimized.
19	\citet{pan-reward-misspecification} show that more capable agents exploit reward misspecifications more severely; our cross-scale comparison (4B vs.\ 1.7B) complements this finding by demonstrating that different capacities discover qualitatively different exploits under identical reward formulations.
20	We frame our results as an empirical instance (primarily regressional, with extremal elements) of Goodhart's Law within the \citet{manheim-goodhart-taxonomy} taxonomy: ISR's LOO definition creates an inherent structural bias toward tautology ($P{\to}P$ receives $\text{ISR}{=}0.75$ by construction), with collapse observed at all four tested doses.
21	
22	\paragraph{Mutation testing.}
23	STA adapts the LOO mutation paradigm~\citep{demillo1978, jia-harman-survey} to solver inputs; our contribution lies in the application and empirical findings, not in the perturbation primitive itself.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "61d3ba39-264e-4b09-a743-3e538b35af3d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1-2025} evaluate execution accuracy alone, with no diagnostic for structural quality.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nLearned PRMs~\\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}; recent work extends PRMs to multi-domain settings~\\citep{zeng2025versaprm} and process-level reasoning~\\citep{khalifa2025thinkprm}. \\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.\nSymbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\nRubric-grounded GRPO~\\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.\nThe shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empirically in RLHF and frontier models~\\citep{amodei2016concrete, krakovna2020specification, gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.\nRecent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards} and reward hacking in frontier models~\\citep{metr-reward-hacking}.\nOur setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \\emph{emerges during RL training} rather than at inference time (cf.\\ shortcut learning in supervised settings~\\citep{geirhos2020shortcut}); and the effect operates at a diagnostic level, where the metric designed to detect gaming becomes gamed when optimized.\n\\citet{pan-reward-misspecification} show that more capable agents exploit reward misspecifications more severely; our cross-scale comparison (4B vs.\\ 1.7B) complements this finding by demonstrating that different capacities discover qualitatively different exploits under identical reward formulations.\nWe frame our results as an empirical instance (primarily regressional, with extremal elements) of Goodhart's Law within the \\citet{manheim-goodhart-taxonomy} taxonomy: ISR's LOO definition creates an inherent structural bias toward tautology ($P{\\to}P$ receives $\\text{ISR}{=}0.75$ by construction), with collapse observed at all four tested doses.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; our contribution lies in the application and empirical findings, not in the perturbation primitive itself.\n",
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

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files. Let me start with Batch 1.

### Batch 1 Changes:

1. **experiments.tex L96-102**: Replace the transient genuine window paragraph
2. **experiments.tex L178**: Replace CMH tests sentence
3. **conclusion.tex L4-5**: Replace the OR sentence
4. **limitations.tex L7**: Replace the five seeds sentence
5. **appendix.tex L117-120**: Insert CMH independence caveat

Let me do these changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "ae55cdf5-2e46-459c-b427-6fc2dee81a8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Pp1XNJzugYy7iNHd3RTE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 56801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3368
      },
      "output_tokens": 9,
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

_source line 22_

Starting Batch 1. Let me make the five edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "5a762c7c-8aae-469b-93a8-40a293da8f84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Pp1XNJzugYy7iNHd3RTE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 56801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3368
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01LKzUmu2v4JSQfRzFTFtfgk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\textbf{The transient genuine window.}\nDuring the transient window, Cochran--Mantel--Haenszel tests stratified by seed show ISR produces more genuine proofs than random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, 95\\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; uncorrected classification, Appendix Table~\\ref{tab:fol-beta01-perseed}).\nThe genuine-rate advantage is sensitive to classification methodology: the 5-seed uncorrected CMH favors ISR, but a 3-seed H8+FN-corrected analysis reverses direction ($\\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction and the reduced sample size.\nThe true effect likely lies between these estimates; the transient benefit is suggestive but not robust to stricter classification.\nThis benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine respectively; see below).\nThe same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.\nSnapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000",
  "new_string": "\\textbf{The transient genuine window.}\nAt 500 steps, 3 of 5 ISR seeds sustain genuine output (per-seed range: 2\\%--55\\%) versus 0 of 5 random seeds, a descriptive pattern consistent with ISR temporarily rewarding necessary premises before H7 dominates.\nHowever, statistical inference is limited: Cochran--Mantel--Haenszel tests yield $\\text{OR}_{\\text{CMH}}{=}3.37$ ($p{<}10^{-9}$), but within-seed samples share a checkpoint and use greedy decoding, violating the independence assumption required by CMH; the effective sample size is seeds ($n{=}5$), not samples ($n{=}350$/$414$).\nSeed-level permutation tests, which correctly treat seeds as the unit of observation, yield $p{=}0.26$ (genuine), consistent with the severe power limitation at $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\nUnder stricter classification (H8+FN correction on 3 fully-audited seeds), the direction reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine at 1000 steps).\nThe transient benefit is descriptively observed but statistically underpowered at seed-level ($n{=}5$); it should not be interpreted as evidence that ISR reliably improves structural quality. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "70260322-620b-47ba-9774-9387eb304522",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Pp1XNJzugYy7iNHd3RTE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 56801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3368
      },
      "output_tokens": 9,
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

_source line 24 · 2026-05-17T17:38:02.855Z_

<details><summary>↩ Tool result · `toolu_01LKzUmu2v4JSQfRzFTFtfgk`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "7ef26bfc-84ae-41b8-be6e-20c390f08dcd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "\\textbf{The transient genuine window.}\nDuring the transient window, Cochran--Mantel--Haenszel tests stratified by seed show ISR produces more genuine proofs than random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, 95\\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; uncorrected classification, Appendix Table~\\ref{tab:fol-beta01-perseed}).\nThe genuine-rate advantage is sensitive to classification methodology: the 5-seed uncorrected CMH favors ISR, but a 3-seed H8+FN-corrected analysis reverses direction ($\\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction and the reduced sample size.\nThe true effect likely lies between these estimates; the transient benefit is suggestive but not robust to stricter classification.\nThis benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine respectively; see below).\nThe same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.\nSnapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000",
    "newString": "\\textbf{The transient genuine window.}\nAt 500 steps, 3 of 5 ISR seeds sustain genuine output (per-seed range: 2\\%--55\\%) versus 0 of 5 random seeds, a descriptive pattern consistent with ISR temporarily rewarding necessary premises before H7 dominates.\nHowever, statistical inference is limited: Cochran--Mantel--Haenszel tests yield $\\text{OR}_{\\text{CMH}}{=}3.37$ ($p{<}10^{-9}$), but within-seed samples share a checkpoint and use greedy decoding, violating the independence assumption required by CMH; the effective sample size is seeds ($n{=}5$), not samples ($n{=}350$/$414$).\nSeed-level permutation tests, which correctly treat seeds as the unit of observation, yield $p{=}0.26$ (genuine), consistent with the severe power limitation at $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\nUnder stricter classification (H8+FN correction on 3 fully-audited seeds), the direction reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine at 1000 steps).\nThe transient benefit is descriptively observed but statistically underpowered at seed-level ($n{=}5$); it should not be interpreted as evidence that ISR reliably improves structural quality. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nCross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\\S\\ref{sec:crossscale}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}) with greedy decoding (Appendix~\\ref{app:setup}).\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ (at 500 steps) via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.97{\\pm}0.02$) with near-zero genuine output (see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\\%$, genuine $6.2\\%$; s44: H1 $85\\%$ + H8 $15\\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2\nNotably, s43 recovers from $\\text{PR}{=}13\\%$ (500 steps) to $\\text{PR}{=}96\\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$; per-seed range ${\\sim}$91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific; a 100-step checkpoint ($\\text{PR}{=}32\\%$, hacking${\\geq}31\\%$) partially controls for the PR-level confound, though the PR gap remains substantial (Appendix~\\ref{app:100step}).\nSFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.\nWhether SFT would develop similar exploits at higher prove rates remains an open question; this mechanistic argument is plausible but not conclusive.\n\n\\subsection{ISR as Reward: Goodhart Effects}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nWe present $\\beta{=}0.1$ first as the focal dose (5 seeds, trajectory analysis), then examine lower and higher doses.\nThe headline finding: ISR contains an inherent Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy} observed to produce collapse at all four tested doses ($\\beta\\in\\{0.05, 0.1, 0.2, 0.3\\}$).\nThe mechanism is structural: tautological proofs ($P{\\to}P$) receive $\\text{ISR}{=}0.75$ and single-premise-equals-conclusion constructions receive $\\text{ISR}{\\geq}0.5$, both by the LOO definition alone.\nOnce sampled during GRPO rollouts, these high-ISR tautologies create a positive feedback loop; $\\beta$ controls only the \\emph{timing} of collapse, not whether it occurs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nExec-only (1k)$^{\\dagger\\dagger}$ & --- & 97{\\scriptsize$\\pm$2} & 0.03{\\scriptsize$\\pm$.05} & 0 & --- & $\\leq$2$^{\\dagger\\dagger}$ \\\\\nISR$^\\ddagger$ & 0.1 & 70{\\scriptsize$\\pm$19} & --- & \\textbf{54} & 18 & 23$^\\star$ \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)\nRandom & 0.1 & \\textbf{83}{\\scriptsize$\\pm$15} & 0.080{\\scriptsize$\\pm$.06} & 30 & 59 & 8 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)\nISR & 0.2 & 97{\\scriptsize$\\pm$4} & 0.69{\\scriptsize$\\pm$.24} & \\textbf{99} & 0 & 0 \\\\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\\ref{tab:beta02-detail})\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-1.7B (seed~42)}} \\\\\nISR & 0.1 & 100 & 0.600 & 0 & \\textbf{100} & 0 \\\\ %% registry: d113-1.7b-isr-b01-s42\nRandom & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\\\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)\nISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\\\ %% registry: d113-1.7b-isr-b03-s42\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape. PR/ISR$^*$: mean$\\pm$std; H7/H1/N-H: pooled \\%. $^\\dagger$s42, 500 steps. $^\\ddagger$N-H uncorrected upper bound (s43/s44 H8 audit unavailable). $^\\star$Transient; collapses at 1000 steps (\\S\\ref{sec:goodhart-temporal}). $^{\\dagger\\dagger}$3-seed 1000-step (Appendix Table~\\ref{tab:exec-only-1000}).}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): stochastic delayed collapse.}\nAt $\\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\\geq}97\\%$ H7, $0\\%$ genuine within ${\\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.\nThe 5-seed pooled non-hacking rate is ${\\sim}23\\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\\%$ to $55\\%$ genuine.\nThis bifurcation is stochastic: all seeds are indistinguishable in the first ${\\sim}100$ steps ($\\text{ISR}{\\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\\text{ISR}{\\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.\nOnce a seed enters the H7 basin, convergence to saturation takes ${\\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46\n\nH7 (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by the LOO definition; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both ISR and random conditions (Appendix Figure~\\ref{fig:hacking-composition}); the specific mode (H7 vs.\\ H1) within a seed is stochastic under both conditions ($\\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.\nRandom yields higher PR ($83{\\pm}15\\%$ vs.\\ $70{\\pm}19\\%$; $n{=}5$ each).\nRandom H7 exhibits extreme seed dependence (per-seed range: $0\\%$--$91.5\\%$; pooled $30\\%$ is dominated by s46 at $91.5\\%$ and s43 at $38.3\\%$).\nBoth conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\\%$ of proved samples in affected seeds: s43${=}61/61$, s44${=}89/89$), while random-induced H7 coexists with other modes ($38$--$92\\%$).\nISR's reward signal converts H7 from a stochastic possibility into an irreversible attractor once sampled.\nThe reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\\beta$ versus ${\\sim}1{+}0.26\\beta$ for genuine proofs (premise-count-matched), a gap of ${\\sim}0.49\\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.\n\n\\textbf{The transient genuine window.}\nDuring the transient window, Cochran--Mantel--Haenszel tests stratified by seed show ISR produces more genuine proofs than random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, 95\\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; uncorrected classification, Appendix Table~\\ref{tab:fol-beta01-perseed}).\nThe genuine-rate advantage is sensitive to classification methodology: the 5-seed uncorrected CMH favors ISR, but a 3-seed H8+FN-corrected analysis reverses direction ($\\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction and the reduced sample size.\nThe true effect likely lies between these estimates; the transient benefit is suggestive but not robust to stricter classification.\nThis benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine respectively; see below).\nThe same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.\nSnapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000\n\n\\textbf{Premise-count confound.}\nThe genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\\ref{app:extended-discussion}).\n\n\\textbf{Trajectory analysis: timing, not destiny.}\\label{sec:goodhart-temporal}\nExtended training (1000 steps; Appendix Figure~\\ref{fig:training-isr-curves}) confirms the genuine window is transient across seeds.\nSeed~42 declines from $17\\%$ to $2\\%$ genuine via H7 saturation ($16.0\\%{\\to}96.7\\%$ H7, PR stable at ${\\sim}96\\%$); seed~45, which achieved the highest 500-step genuine rate ($55\\%$), collapses to $0\\%$ genuine through reward collapse ($\\text{PR}: 42\\%{\\to}2\\%$).\nThe two seeds exhibit distinct failure paths (H7 gaming vs.\\ output collapse) but converge to the same outcome: zero genuine proofs at extended training. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42, plan002-b01-s45-1000\n\n\\textbf{Micro-dose ISR ($\\beta{=}0.05$): deterministic collapse.}\nAll three ISR seeds reach $\\text{PR}{\\geq}99\\%$ but converge to H7a tautology (H7 $87$--$100\\%$, genuine $5.1\\%$), while the random control mostly fails to learn (median $\\text{PR}{=}7\\%$) with zero H7, confirming H7 as specific to ISR's LOO structure.\nBelow a signal-floor, ISR's genuine component is undetectable while its H7 bias remains exploitable (per-seed breakdown in Appendix~\\ref{app:beta005}). %% registry: sweep-isr-b005-s42/s43/s44, sweep-random-b005-s42/s43/s44\n\n\\textbf{Medium-dose ISR ($\\beta{=}0.2$): maximum exploitation.}\nAll three seeds converge to pure H7a tautology ($0\\%$ non-hacking, $n{=}290$; Appendix Table~\\ref{tab:beta02-detail}). %% registry: sweep-isr-b02-s42/s43/s44\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\\ref{app:beta03}).\nThe random control is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$) with $91\\%$ H1 and ${\\leq}4\\%$ non-hacking; high-dose proxy weighting destabilizes training regardless of signal source. %% registry: plan002-additive-b03-s42/s43/s44\nISR vs.\\ random H7 at $\\beta{=}0.3$: $\\text{OR}{=}13.7$, 95\\% CI $[7.0, 26.8]$ (Appendix~\\ref{app:beta03}).\n\n\\textbf{Non-monotonic dose-response.}\nThe four $\\beta$ levels suggest a non-monotonic pattern: $\\beta\\in\\{0.05, 0.2\\}$ converge deterministically to H7 collapse (${\\geq}94\\%$ H7), $\\beta{=}0.3$ triggers multi-modal instability, and only $\\beta{=}0.1$ sustains a transient genuine window (3 of 5 seeds).\nGoodhart collapse is not a simple function of dose; the balance between genuine and exploit reinforcement depends on a threshold interaction between $\\beta$ and rollout stochasticity.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (3 seeds, $\\beta{=}0.1$).\nUnder exec-only training, 2/3 seeds show $\\text{ISR}^{*}{\\approx}0$ despite $\\text{PR}{\\geq}0.56$, reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding; ISR flags both failure semantics.\nUnder ISR reward, 3/3 seeds reach $0\\%$ non-hacking through three distinct mechanisms: clean H7 tautology (s42, $\\text{ISR}^{*}{=}1.0$), degenerate uppercase pseudo-Prolog evading text-match classifiers (s43, functional $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, $95/97$ proved at $n_{\\text{necessary}}{=}1$).\nSeed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.\nWe attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\\ref{tab:prolog-detailed} and Figure~\\ref{fig:prolog-comparison}).\n\n\\subsection{Cross-Scale Evidence}\n\\label{sec:crossscale}\n\nWe train Qwen3-1.7B under ISR $\\beta\\in\\{0.1,0.3\\}$ and Random $\\beta{=}0.1$ (single seed, 500 steps).\nAll conditions produce $0\\%$ non-hacking, but the exploit modes differ qualitatively from 4B: Random discovers H9 (contradiction injection, $\\text{PR}{=}93\\%$, $100\\%$ \\emph{ex falso}), ISR $\\beta{=}0.1$ collapses to a single fixed template ($\\text{ISR}^{*}{=}0.6$ at zero variance, $100\\%$ H1), and ISR $\\beta{=}0.3$ triggers reward collapse ($\\text{PR}{=}17\\%$) mirroring the 4B pattern.\nH9 never appears at 4B scale; fixed-template mode collapse never appears at 4B; different capacities converge to different Goodhart basins under identical rewards.\nNo safe scale was observed in this single-seed comparison (Table~\\ref{tab:hacking-taxonomy}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{Rnd}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 59 & 7 & 0$^\\sharp$ & \\textbf{100} & 0 \\\\\nH7 duplicate   & 0  & \\textbf{54} & 30 & 0 & 100$^\\sharp$ & 0 & 0 \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 & 0 \\\\\nH9 ex falso    & --- & --- & --- & --- & --- & 0 & \\textbf{100} \\\\\nTautological   & --- & --- & --- & --- & s42 & --- & --- \\\\\nRepetition     & s43 & --- & --- & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & \\textbf{23}  & 8 & \\textbf{92} & \\textbf{0} & \\textbf{0} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Nine hacking modes (\\% of proved; exec/SFT: s42; ISR/Random 4B: 5-seed pooled; 1.7B: s42). H7a+H7b combined. Seed IDs mark dominant mode. $^\\sharp$Prolog: strict+functional pooled. Modes marked with seed identifiers are single-seed observations.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe nine modes (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 conditions.\nH1, H7, and H8 account for ${>}90\\%$ of hacking; H7b ($14/350$) evades text-match classifiers.\nISR modestly increases H7 probability ($\\text{OR}{=}2.84$, $p{<}5{\\times}10^{-12}$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.\nAll GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\nCMH tests confirm both effects (H7: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$).\n",
    "structuredPatch": [
      {
        "oldStart": 94,
        "oldLines": 12,
        "newStart": 94,
        "newLines": 11,
        "lines": [
          " The reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\\beta$ versus ${\\sim}1{+}0.26\\beta$ for genuine proofs (premise-count-matched), a gap of ${\\sim}0.49\\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.",
          " ",
          " \\textbf{The transient genuine window.}",
          "-During the transient window, Cochran--Mantel--Haenszel tests stratified by seed show ISR produces more genuine proofs than random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, 95\\% CI $[2.21, 5.13]$, $p{<}10^{-9}$; uncorrected classification, Appendix Table~\\ref{tab:fol-beta01-perseed}).",
          "-The genuine-rate advantage is sensitive to classification methodology: the 5-seed uncorrected CMH favors ISR, but a 3-seed H8+FN-corrected analysis reverses direction ($\\text{OR}{=}0.61$, n.s.), reflecting both the conservative bias of H8 correction and the reduced sample size.",
          "-The true effect likely lies between these estimates; the transient benefit is suggestive but not robust to stricter classification.",
          "-This benefit is temporary: extended training (1000 steps) on seeds~42 and~45 confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine respectively; see below).",
          "-The same LOO bias that enables genuine improvement (rewarding necessary premises) also creates the Goodhart attractor (rewarding tautological constructions); the genuine window reflects seeds that have not yet sampled the H7 exploit, not seeds that resist it.",
          "-Snapshot evaluation at 500 steps would overestimate ISR's benefit; trajectory analysis is required to distinguish transient from stable improvement. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000",
          "+At 500 steps, 3 of 5 ISR seeds sustain genuine output (per-seed range: 2\\%--55\\%) versus 0 of 5 random seeds, a descriptive pattern consistent with ISR temporarily rewarding necessary premises before H7 dominates.",
          "+However, statistical inference is limited: Cochran--Mantel--Haenszel tests yield $\\text{OR}_{\\text{CMH}}{=}3.37$ ($p{<}10^{-9}$), but within-seed samples share a checkpoint and use greedy decoding, violating the independence assumption required by CMH; the effective sample size is seeds ($n{=}5$), not samples ($n{=}350$/$414$).",
          "+Seed-level permutation tests, which correctly treat seeds as the unit of observation, yield $p{=}0.26$ (genuine), consistent with the severe power limitation at $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.",
          "+Under stricter classification (H8+FN correction on 3 fully-audited seeds), the direction reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine at 1000 steps).",
          "+The transient benefit is descriptively observed but statistically underpowered at seed-level ($n{=}5$); it should not be interpreted as evidence that ISR reliably improves structural quality. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000",
          " ",
          " \\textbf{Premise-count confound.}",
          " The genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\\ref{app:extended-discussion})."
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01CPrgJP6zG4dcqqPbKUUtw7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "CMH tests confirm both effects (H7: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$).",
  "new_string": "CMH tests treating samples as independent yield $\\text{OR}_{\\text{CMH}}{=}2.46$ ($p{<}10^{-15}$) for H7 and $3.37$ ($p{<}10^{-9}$) for genuine output; however, within-seed non-independence inflates these $p$-values (see \\S\\ref{sec:goodhart} for seed-level analysis)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "eaf5734a-9d72-4e7d-bddd-e4ec78d5ac78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Pp1XNJzugYy7iNHd3RTE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 56801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3368
      },
      "output_tokens": 9,
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

_source line 26 · 2026-05-17T17:38:06.537Z_

<details><summary>↩ Tool result · `toolu_01CPrgJP6zG4dcqqPbKUUtw7`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "36ecd277-1a7f-4e7f-9b50-9af96ade0ba6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "CMH tests confirm both effects (H7: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$).",
    "newString": "CMH tests treating samples as independent yield $\\text{OR}_{\\text{CMH}}{=}2.46$ ($p{<}10^{-15}$) for H7 and $3.37$ ($p{<}10^{-9}$) for genuine output; however, within-seed non-independence inflates these $p$-values (see \\S\\ref{sec:goodhart} for seed-level analysis).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nCross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\\S\\ref{sec:crossscale}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}) with greedy decoding (Appendix~\\ref{app:setup}).\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ (at 500 steps) via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.97{\\pm}0.02$) with near-zero genuine output (see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\\%$, genuine $6.2\\%$; s44: H1 $85\\%$ + H8 $15\\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2\nNotably, s43 recovers from $\\text{PR}{=}13\\%$ (500 steps) to $\\text{PR}{=}96\\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$; per-seed range ${\\sim}$91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific; a 100-step checkpoint ($\\text{PR}{=}32\\%$, hacking${\\geq}31\\%$) partially controls for the PR-level confound, though the PR gap remains substantial (Appendix~\\ref{app:100step}).\nSFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.\nWhether SFT would develop similar exploits at higher prove rates remains an open question; this mechanistic argument is plausible but not conclusive.\n\n\\subsection{ISR as Reward: Goodhart Effects}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nWe present $\\beta{=}0.1$ first as the focal dose (5 seeds, trajectory analysis), then examine lower and higher doses.\nThe headline finding: ISR contains an inherent Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy} observed to produce collapse at all four tested doses ($\\beta\\in\\{0.05, 0.1, 0.2, 0.3\\}$).\nThe mechanism is structural: tautological proofs ($P{\\to}P$) receive $\\text{ISR}{=}0.75$ and single-premise-equals-conclusion constructions receive $\\text{ISR}{\\geq}0.5$, both by the LOO definition alone.\nOnce sampled during GRPO rollouts, these high-ISR tautologies create a positive feedback loop; $\\beta$ controls only the \\emph{timing} of collapse, not whether it occurs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nExec-only (1k)$^{\\dagger\\dagger}$ & --- & 97{\\scriptsize$\\pm$2} & 0.03{\\scriptsize$\\pm$.05} & 0 & --- & $\\leq$2$^{\\dagger\\dagger}$ \\\\\nISR$^\\ddagger$ & 0.1 & 70{\\scriptsize$\\pm$19} & --- & \\textbf{54} & 18 & 23$^\\star$ \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)\nRandom & 0.1 & \\textbf{83}{\\scriptsize$\\pm$15} & 0.080{\\scriptsize$\\pm$.06} & 30 & 59 & 8 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)\nISR & 0.2 & 97{\\scriptsize$\\pm$4} & 0.69{\\scriptsize$\\pm$.24} & \\textbf{99} & 0 & 0 \\\\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\\ref{tab:beta02-detail})\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-1.7B (seed~42)}} \\\\\nISR & 0.1 & 100 & 0.600 & 0 & \\textbf{100} & 0 \\\\ %% registry: d113-1.7b-isr-b01-s42\nRandom & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\\\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)\nISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\\\ %% registry: d113-1.7b-isr-b03-s42\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape. PR/ISR$^*$: mean$\\pm$std; H7/H1/N-H: pooled \\%. $^\\dagger$s42, 500 steps. $^\\ddagger$N-H uncorrected upper bound (s43/s44 H8 audit unavailable). $^\\star$Transient; collapses at 1000 steps (\\S\\ref{sec:goodhart-temporal}). $^{\\dagger\\dagger}$3-seed 1000-step (Appendix Table~\\ref{tab:exec-only-1000}).}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): stochastic delayed collapse.}\nAt $\\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\\geq}97\\%$ H7, $0\\%$ genuine within ${\\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.\nThe 5-seed pooled non-hacking rate is ${\\sim}23\\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\\%$ to $55\\%$ genuine.\nThis bifurcation is stochastic: all seeds are indistinguishable in the first ${\\sim}100$ steps ($\\text{ISR}{\\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\\text{ISR}{\\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.\nOnce a seed enters the H7 basin, convergence to saturation takes ${\\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46\n\nH7 (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by the LOO definition; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both ISR and random conditions (Appendix Figure~\\ref{fig:hacking-composition}); the specific mode (H7 vs.\\ H1) within a seed is stochastic under both conditions ($\\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.\nRandom yields higher PR ($83{\\pm}15\\%$ vs.\\ $70{\\pm}19\\%$; $n{=}5$ each).\nRandom H7 exhibits extreme seed dependence (per-seed range: $0\\%$--$91.5\\%$; pooled $30\\%$ is dominated by s46 at $91.5\\%$ and s43 at $38.3\\%$).\nBoth conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\\%$ of proved samples in affected seeds: s43${=}61/61$, s44${=}89/89$), while random-induced H7 coexists with other modes ($38$--$92\\%$).\nISR's reward signal converts H7 from a stochastic possibility into an irreversible attractor once sampled.\nThe reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\\beta$ versus ${\\sim}1{+}0.26\\beta$ for genuine proofs (premise-count-matched), a gap of ${\\sim}0.49\\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.\n\n\\textbf{The transient genuine window.}\nAt 500 steps, 3 of 5 ISR seeds sustain genuine output (per-seed range: 2\\%--55\\%) versus 0 of 5 random seeds, a descriptive pattern consistent with ISR temporarily rewarding necessary premises before H7 dominates.\nHowever, statistical inference is limited: Cochran--Mantel--Haenszel tests yield $\\text{OR}_{\\text{CMH}}{=}3.37$ ($p{<}10^{-9}$), but within-seed samples share a checkpoint and use greedy decoding, violating the independence assumption required by CMH; the effective sample size is seeds ($n{=}5$), not samples ($n{=}350$/$414$).\nSeed-level permutation tests, which correctly treat seeds as the unit of observation, yield $p{=}0.26$ (genuine), consistent with the severe power limitation at $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\nUnder stricter classification (H8+FN correction on 3 fully-audited seeds), the direction reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine at 1000 steps).\nThe transient benefit is descriptively observed but statistically underpowered at seed-level ($n{=}5$); it should not be interpreted as evidence that ISR reliably improves structural quality. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000\n\n\\textbf{Premise-count confound.}\nThe genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\\ref{app:extended-discussion}).\n\n\\textbf{Trajectory analysis: timing, not destiny.}\\label{sec:goodhart-temporal}\nExtended training (1000 steps; Appendix Figure~\\ref{fig:training-isr-curves}) confirms the genuine window is transient across seeds.\nSeed~42 declines from $17\\%$ to $2\\%$ genuine via H7 saturation ($16.0\\%{\\to}96.7\\%$ H7, PR stable at ${\\sim}96\\%$); seed~45, which achieved the highest 500-step genuine rate ($55\\%$), collapses to $0\\%$ genuine through reward collapse ($\\text{PR}: 42\\%{\\to}2\\%$).\nThe two seeds exhibit distinct failure paths (H7 gaming vs.\\ output collapse) but converge to the same outcome: zero genuine proofs at extended training. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42, plan002-b01-s45-1000\n\n\\textbf{Micro-dose ISR ($\\beta{=}0.05$): deterministic collapse.}\nAll three ISR seeds reach $\\text{PR}{\\geq}99\\%$ but converge to H7a tautology (H7 $87$--$100\\%$, genuine $5.1\\%$), while the random control mostly fails to learn (median $\\text{PR}{=}7\\%$) with zero H7, confirming H7 as specific to ISR's LOO structure.\nBelow a signal-floor, ISR's genuine component is undetectable while its H7 bias remains exploitable (per-seed breakdown in Appendix~\\ref{app:beta005}). %% registry: sweep-isr-b005-s42/s43/s44, sweep-random-b005-s42/s43/s44\n\n\\textbf{Medium-dose ISR ($\\beta{=}0.2$): maximum exploitation.}\nAll three seeds converge to pure H7a tautology ($0\\%$ non-hacking, $n{=}290$; Appendix Table~\\ref{tab:beta02-detail}). %% registry: sweep-isr-b02-s42/s43/s44\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\\ref{app:beta03}).\nThe random control is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$) with $91\\%$ H1 and ${\\leq}4\\%$ non-hacking; high-dose proxy weighting destabilizes training regardless of signal source. %% registry: plan002-additive-b03-s42/s43/s44\nISR vs.\\ random H7 at $\\beta{=}0.3$: $\\text{OR}{=}13.7$, 95\\% CI $[7.0, 26.8]$ (Appendix~\\ref{app:beta03}).\n\n\\textbf{Non-monotonic dose-response.}\nThe four $\\beta$ levels suggest a non-monotonic pattern: $\\beta\\in\\{0.05, 0.2\\}$ converge deterministically to H7 collapse (${\\geq}94\\%$ H7), $\\beta{=}0.3$ triggers multi-modal instability, and only $\\beta{=}0.1$ sustains a transient genuine window (3 of 5 seeds).\nGoodhart collapse is not a simple function of dose; the balance between genuine and exploit reinforcement depends on a threshold interaction between $\\beta$ and rollout stochasticity.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (3 seeds, $\\beta{=}0.1$).\nUnder exec-only training, 2/3 seeds show $\\text{ISR}^{*}{\\approx}0$ despite $\\text{PR}{\\geq}0.56$, reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding; ISR flags both failure semantics.\nUnder ISR reward, 3/3 seeds reach $0\\%$ non-hacking through three distinct mechanisms: clean H7 tautology (s42, $\\text{ISR}^{*}{=}1.0$), degenerate uppercase pseudo-Prolog evading text-match classifiers (s43, functional $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, $95/97$ proved at $n_{\\text{necessary}}{=}1$).\nSeed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.\nWe attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\\ref{tab:prolog-detailed} and Figure~\\ref{fig:prolog-comparison}).\n\n\\subsection{Cross-Scale Evidence}\n\\label{sec:crossscale}\n\nWe train Qwen3-1.7B under ISR $\\beta\\in\\{0.1,0.3\\}$ and Random $\\beta{=}0.1$ (single seed, 500 steps).\nAll conditions produce $0\\%$ non-hacking, but the exploit modes differ qualitatively from 4B: Random discovers H9 (contradiction injection, $\\text{PR}{=}93\\%$, $100\\%$ \\emph{ex falso}), ISR $\\beta{=}0.1$ collapses to a single fixed template ($\\text{ISR}^{*}{=}0.6$ at zero variance, $100\\%$ H1), and ISR $\\beta{=}0.3$ triggers reward collapse ($\\text{PR}{=}17\\%$) mirroring the 4B pattern.\nH9 never appears at 4B scale; fixed-template mode collapse never appears at 4B; different capacities converge to different Goodhart basins under identical rewards.\nNo safe scale was observed in this single-seed comparison (Table~\\ref{tab:hacking-taxonomy}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{Rnd}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 59 & 7 & 0$^\\sharp$ & \\textbf{100} & 0 \\\\\nH7 duplicate   & 0  & \\textbf{54} & 30 & 0 & 100$^\\sharp$ & 0 & 0 \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 & 0 \\\\\nH9 ex falso    & --- & --- & --- & --- & --- & 0 & \\textbf{100} \\\\\nTautological   & --- & --- & --- & --- & s42 & --- & --- \\\\\nRepetition     & s43 & --- & --- & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & \\textbf{23}  & 8 & \\textbf{92} & \\textbf{0} & \\textbf{0} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Nine hacking modes (\\% of proved; exec/SFT: s42; ISR/Random 4B: 5-seed pooled; 1.7B: s42). H7a+H7b combined. Seed IDs mark dominant mode. $^\\sharp$Prolog: strict+functional pooled. Modes marked with seed identifiers are single-seed observations.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe nine modes (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 conditions.\nH1, H7, and H8 account for ${>}90\\%$ of hacking; H7b ($14/350$) evades text-match classifiers.\nISR modestly increases H7 probability ($\\text{OR}{=}2.84$, $p{<}5{\\times}10^{-12}$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.\nAll GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\nCMH tests confirm both effects (H7: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$).\n",
    "structuredPatch": [
      {
        "oldStart": 174,
        "oldLines": 4,
        "newStart": 174,
        "newLines": 4,
        "lines": [
          " H1, H7, and H8 account for ${>}90\\%$ of hacking; H7b ($14/350$) evades text-match classifiers.",
          " ISR modestly increases H7 probability ($\\text{OR}{=}2.84$, $p{<}5{\\times}10^{-12}$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.",
          " All GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.",
          "-CMH tests confirm both effects (H7: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{<}10^{-15}$; genuine: $\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$).",
          "+CMH tests treating samples as independent yield $\\text{OR}_{\\text{CMH}}{=}2.46$ ($p{<}10^{-15}$) for H7 and $3.37$ ($p{<}10^{-9}$) for genuine output; however, within-seed non-independence inflates these $p$-values (see \\S\\ref{sec:goodhart} for seed-level analysis)."
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01UmuAb5AhwFwS1XmBDaaZeb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
  "old_string": "At 500 steps, ISR increases genuine proofs over random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.",
  "new_string": "At 500 steps, ISR seeds descriptively sustain more genuine output than random controls (3 of 5 seeds vs.\\ 0 of 5); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.).\nExtended training confirms the window closes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "00924d41-69e6-4426-b66c-8b17b3868a8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Pp1XNJzugYy7iNHd3RTE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 56801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3368
      },
      "output_tokens": 9,
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

_source line 28 · 2026-05-17T17:38:10.316Z_

<details><summary>↩ Tool result · `toolu_01UmuAb5AhwFwS1XmBDaaZeb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "f5e8508a-dc67-4388-882d-8abd08af318e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
    "oldString": "At 500 steps, ISR increases genuine proofs over random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.",
    "newString": "At 500 steps, ISR seeds descriptively sustain more genuine output than random controls (3 of 5 seeds vs.\\ 0 of 5); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.).\nExtended training confirms the window closes.",
    "originalFile": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$; \\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\nAt 500 steps, ISR increases genuine proofs over random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\nWhile Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic dose-response across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).\nThese details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}.\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 8,
        "lines": [
          " \\label{sec:discussion}",
          " ",
          " STA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$; \\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).",
          "-At 500 steps, ISR increases genuine proofs over random controls ($\\text{OR}_{\\text{CMH}}{=}3.37$, $p{<}10^{-9}$); under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes.",
          "+At 500 steps, ISR seeds descriptively sustain more genuine output than random controls (3 of 5 seeds vs.\\ 0 of 5); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.).",
          "+Extended training confirms the window closes.",
          " ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.",
          " While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic dose-response across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).",
          " These details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}."
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01MWWNpCoeD1qRw9sE4y38PN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
  "old_string": "Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).",
  "new_string": "Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$). CMH tests yield $p{<}10^{-9}$ but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy; CMH $p$-values are therefore inflated and should be interpreted as directional indicators, not calibrated significance levels."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "e64c6f32-f07e-4587-a7bf-3a9e2de8c021",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Pp1XNJzugYy7iNHd3RTE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 56801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3368
      },
      "output_tokens": 9,
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

_source line 30 · 2026-05-17T17:38:14.559Z_

<details><summary>↩ Tool result · `toolu_01MWWNpCoeD1qRw9sE4y38PN`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "1f5e685a-0e05-449d-8b04-dceb90497e56",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex",
    "oldString": "Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).",
    "newString": "Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$). CMH tests yield $p{<}10^{-9}$ but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy; CMH $p$-values are therefore inflated and should be interpreted as directional indicators, not calibrated significance levels.",
    "originalFile": "\\section{Limitations}\n\\label{sec:limitations}\n\nExperiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.\nISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.\nA downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).\nFive seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).\nSTA requires solvers supporting component-level input manipulation.\n\n\\paragraph{Evaluation as temporal snapshot.}\nAll 500-step results represent a temporal snapshot, not an equilibrium.\nTrajectory analysis on seeds~42 and~45 (1000 steps) confirms that the ${\\sim}23\\%$ genuine window observed at 500 steps under ISR $\\beta{=}0.1$ is transient (s42: $17\\%{\\to}2\\%$; s45: $55\\%{\\to}0\\%$ genuine).\nReaders should interpret the 500-step non-hacking rates as upper bounds on long-run structural quality under continued training.\n\n\\paragraph{Seed counts per dose.}\nISR $\\beta{=}0.05$ uses three seeds (all H7-dominated); random $\\beta{=}0.05$ uses three seeds with high variance ($\\text{PR}{=}0\\%$, $7\\%$, $62\\%$); $\\beta{=}0.2$ uses three seeds.\nThe primary $\\beta{=}0.1$ comparison uses five seeds per condition.\nAlthough all tested doses produce dominant gaming, the stochastic bifurcation mechanism (\\S\\ref{sec:goodhart}) means that fewer-seed dose points may not capture the full variance of collapse timing.\nISR $\\beta{=}0.1$ s43 and s44 checkpoints were lost during disk cleanup, preventing retrospective H8 audit on these seeds; the reported 5-seed pooled non-hacking rate (23\\%) is an uncorrected upper bound.\n\n\\paragraph{Cross-scale replication.}\nOur 1.7B experiments use a single seed.\nAlthough different seeds may converge to different exploitation modes (as observed at 4B scale, where three seeds produce three distinct hacking strategies), the qualitative conclusion that hacking dominates with 0\\% genuine output is robust: at 4B, all seeds hack regardless of specific mode.\nThe zero-variance mode collapse at 1.7B (100 identical outputs) indicates a sharper convergence basin at smaller scale.\nReplicating across seeds is a natural next step.\n\n\\paragraph{Data scale.}\nOur experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\\citep{folio}.\nThe training subset is selected via stratified sampling (seed 42) and held constant across all conditions.\nWhile our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " Experiments use a single base model (Qwen3-4B) and dataset family (FOLIO); generalization remains untested.",
          " ISR quantifies syntactic component necessity, not semantic faithfulness: a high-ISR proof can still be logically vacuous if its individually necessary premises are collectively inconsistent or semantically ungrounded.",
          " A downstream NLI evaluation confirms this gap, finding ISR and task accuracy uncorrelated (Spearman $\\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\\ref{app:extended-discussion}).",
          "-Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$); CMH tests stratified by seed confirm the pooled associations remain significant ($p{<}10^{-9}$).",
          "+Five seeds demonstrate qualitative divergence but limit statistical power for seed-level permutation tests ($p{\\geq}0.26$; minimum achievable $p{=}0.008$ at $n{=}5$). CMH tests yield $p{<}10^{-9}$ but assume within-stratum independence, which is violated when samples share a checkpoint and decoding strategy; CMH $p$-values are therefore inflated and should be interpreted as directional indicators, not calibrated significance levels.",
          " STA requires solvers supporting component-level input manipulation.",
          " ",
          " \\paragraph{Evaluation as temporal snapshot.}"
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_013rkpPVPXer8CqPcQf8V5mC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "old_string": "Cochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: H7 $\\text{OR}_{\\text{CMH}}{=}2.46$ (95\\% CI $[1.85, 3.27]$, $p{=}5.6{\\times}10^{-16}$); genuine $\\text{OR}_{\\text{CMH}}{=}3.37$ (95\\% CI $[2.21, 5.13]$, $p{=}4.5{\\times}10^{-10}$).\nSeed-level permutation tests",
  "new_string": "Cochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: H7 $\\text{OR}_{\\text{CMH}}{=}2.46$ (95\\% CI $[1.85, 3.27]$, $p{=}5.6{\\times}10^{-16}$); genuine $\\text{OR}_{\\text{CMH}}{=}3.37$ (95\\% CI $[2.21, 5.13]$, $p{=}4.5{\\times}10^{-10}$).\nCMH assumes within-stratum independence, but samples within each seed share a single checkpoint and use greedy decoding; the effective independent units are seeds ($n{=}5$), not samples, and CMH $p$-values are consequently inflated.\nSeed-level permutation tests"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "cb71ecad-f6fc-4e63-bd19-5eb758db017a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Pp1XNJzugYy7iNHd3RTE3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 56801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3368
      },
      "output_tokens": 9,
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

_source line 32 · 2026-05-17T17:38:19.447Z_

<details><summary>↩ Tool result · `toolu_013rkpPVPXer8CqPcQf8V5mC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "2e862447-f140-4335-b449-9526b96d7288",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "oldString": "Cochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: H7 $\\text{OR}_{\\text{CMH}}{=}2.46$ (95\\% CI $[1.85, 3.27]$, $p{=}5.6{\\times}10^{-16}$); genuine $\\text{OR}_{\\text{CMH}}{=}3.37$ (95\\% CI $[2.21, 5.13]$, $p{=}4.5{\\times}10^{-10}$).\nSeed-level permutation tests",
    "newString": "Cochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: H7 $\\text{OR}_{\\text{CMH}}{=}2.46$ (95\\% CI $[1.85, 3.27]$, $p{=}5.6{\\times}10^{-16}$); genuine $\\text{OR}_{\\text{CMH}}{=}3.37$ (95\\% CI $[2.21, 5.13]$, $p{=}4.5{\\times}10^{-10}$).\nCMH assumes within-stratum independence, but samples within each seed share a single checkpoint and use greedy decoding; the effective independent units are seeds ($n{=}5$), not samples, and CMH $p$-values are consequently inflated.\nSeed-level permutation tests",
    "originalFile": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nAll cross-run ISR values are recomputed uniformly by a single evaluator (\\texttt{eval\\_sta.py}) so that training-log ISR is never compared across runs.\nThe evaluation file \\texttt{proofwriter\\_fol\\_100.jsonl} is a legacy filename containing no ProofWriter data.\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures, and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness (whether the formalization accurately captures the natural-language meaning).\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound is central to ISR's Goodhart vulnerability: H7 tautologies (single premise $=$ conclusion) achieve $\\text{ISR}{\\geq}0.5$ \\emph{by construction}, and the shorter formalizations produced by non-collapsed seeds at $\\beta{=}0.1$ also inflate ISR mechanically.\nPremise-count-matched comparison on non-hacking samples yields $\\text{ISR}^{*}{=}0.258$ vs.\\ $0.243$ for random ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}), confirming that even within the transient genuine window the structural benefit is negligible.\nThis bias is not specific to our setting; any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table}[h]\n\\centering\n\\caption{Fisher exact tests across conditions. Non-hacking rate reported at 5-seed (primary) and 3-seed with H8+FN corrections (sensitivity); H7 comparison at 5-seed (primary) and 3-seed (sensitivity).}\n\\label{tab:bootstrap-ci}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (5-seed)}} \\\\\nISR vs.\\ Random & 22.6\\% {\\scriptsize[18.2,27.0]} & 7.7\\% {\\scriptsize[5.5,10.7]} & 3.48 & ${<}10^{-8}$ \\\\\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (3-seed, H8+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{H7 gaming rate (5-seed)}} \\\\\nISR vs.\\ Random & 54.3\\% {\\scriptsize[49.1,59.5]} & 29.5\\% {\\scriptsize[25.1,33.9]} & 2.84 & $4.82{\\times}10^{-12}$ \\\\\n\\multicolumn{5}{@{}l}{\\textit{H7 gaming rate (3-seed sensitivity)}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\\\[2pt]\n{\\footnotesize 5-seed: ISR $n{=}350$, Random $n{=}414$. 3-seed: ISR $n{=}231$, Random $n{=}262$. Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table}\n\n\\paragraph{Seed-level statistical analysis.}\nTo address potential inflation from within-seed dependence, we supplement pooled Fisher exact tests with two seed-aware analyses.\nCochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: H7 $\\text{OR}_{\\text{CMH}}{=}2.46$ (95\\% CI $[1.85, 3.27]$, $p{=}5.6{\\times}10^{-16}$); genuine $\\text{OR}_{\\text{CMH}}{=}3.37$ (95\\% CI $[2.21, 5.13]$, $p{=}4.5{\\times}10^{-10}$).\nSeed-level permutation tests (treating each seed as a single observation, $n{=}5$ per group) yield $p{=}0.28$ (H7) and $p{=}0.26$ (genuine), consistent with the severe power limitation of $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed classification results for ISR and Random at $\\beta{=}0.1$ (500 steps, FOL). $n$ = proved samples. ISR$^*$ = proved-only mean ISR. $\\dagger$~H8 audit complete; $\\ddagger$~checkpoint unavailable before audit, N-H is uncorrected upper bound. Percentages are per-classifier; samples may match multiple modes. N-H uses set-exclusion per the C013 taxonomy standard.}\n\\label{tab:fol-beta01-perseed}\n\\small\n\\begin{tabular}{lrrrrrrrr}\n\\toprule\n& Seed & PR\\% & $n$ & ISR$^*$ & H7\\% & H1\\% & H8\\% & N-H\\% \\\\\n\\midrule\n\\multirow{6}{*}{\\rotatebox{90}{ISR}}\n& s42 & 81 & 81 & 0.415 & 16.0 & 51.9 & 14.8$\\dagger$ & 17.3 \\\\\n& s43 & 61 & 61 & 0.830 & 100 & 0 & ---$\\ddagger$ & 0 \\\\\n& s44 & 89 & 89 & 0.902 & 100 & 0 & ---$\\ddagger$ & 0 \\\\\n& s45 & 42 & 42 & 0.605 & 38.1 & 4.8 & 2.4 & 54.8 \\\\\n& s46 & 77 & 77 & 0.411 & 14.3 & 26.0 & 5.2 & 54.5 \\\\\n& \\textbf{Pool} & \\textbf{70$\\pm$19} & \\textbf{350} & --- & \\textbf{54.3} & \\textbf{18.0} & --- & \\textbf{22.6} \\\\\n\\midrule\n\\multirow{6}{*}{\\rotatebox{90}{Random}}\n& s42 & 79 & 79 & 0.104 & 0 & 73.4 & 5.1$\\dagger$ & 22.8 \\\\\n& s43 & 94 & 94 & 0.141 & 38.3 & 59.6 & 1.1 & 1.1 \\\\\n& s44 & 89 & 89 & 0.062 & 0 & 82.0 & 18.0 & 6.7 \\\\\n& s45 & 58 & 58 & 0.010 & 0 & 91.4 & 0 & 8.6 \\\\\n& s46 & 94 & 94 & 0.042 & 91.5 & 2.1 & 4.3 & 2.1 \\\\\n& \\textbf{Pool} & \\textbf{83$\\pm$15} & \\textbf{414} & --- & \\textbf{29.5} & \\textbf{55.8} & --- & \\textbf{7.7} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{H7 as inevitable exploit.}\nISR's LOO definition creates an inherent structural bias: tautological proofs ($P{\\to}P$) receive $\\text{ISR}{=}0.75$, and single-premise-equals-conclusion constructions receive $\\text{ISR}{\\geq}0.5$, making H7 the global ISR-maximizing exploit.\n$\\beta$ controls the \\emph{timing} of collapse, not whether it occurs.\nAt all four tested doses, H7 dominates: $\\beta{=}0.05$ (3 seeds, pooled H7 $93.7\\%$, $n{=}253$; random s43 achieves $\\text{PR}{=}62\\%$ with H1 $77.4\\%$ and zero H7, confirming mode specificity); $\\beta{=}0.1$ (stochastic bifurcation: 2/5 seeds collapse within ${\\sim}150$ steps, remaining 3/5 sustain a transient window that closes under extended training); $\\beta{=}0.2$ ($100\\%$ H7 across all three seeds, $n{=}290$; Table~\\ref{tab:beta02-detail}); $\\beta{=}0.3$ (multi-modal, s44 pure H7).\nThe random control produces $29.5\\%$ H7 ($122/414$, 5-seed; per-seed: $0\\%$--$91.5\\%$, dominated by s46 at $91.5\\%$ and s43 at $38.3\\%$; s42/s44/s45 at $0\\%$), random $\\beta{=}0.3$ yields 4--7 H7a per seed.\nOnce a seed samples and reinforces the H7 exploit, convergence is irreversible; this absorbing-state property guarantees eventual collapse regardless of dose.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{ISR $\\beta{=}0.2$ per-seed results (maximum exploitation point). All seeds converge to H7a tautology with 0\\% genuine.}\n\\label{tab:beta02-detail}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{PR\\%} & \\textbf{ISR$^*$} & \\textbf{H7a\\%} & \\textbf{Genuine\\%} \\\\\n\\midrule\ns42 & 100 & 0.55 & 100 & 0 \\\\\ns43 & 97 & 0.96 & 96.9 & 0 \\\\\ns44 & 93 & 0.55 & 100 & 0 \\\\\n\\midrule\n\\textbf{Pooled} & 97$\\pm$4 & 0.69$\\pm$0.24 & 99.0 & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Goodhart effects: implications.}\nThe finding extends beyond this specific system.\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet it contains an inherent structural vulnerability: by its LOO definition, tautological proofs receive artificially high ISR ($P{\\to}P$ yields $\\text{ISR}{=}0.75$; single-premise-equals-conclusion yields $\\text{ISR}{\\geq}0.5$), creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\nGoodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses ($\\beta{=}0.05$: 3 seeds; $\\beta\\in\\{0.1, 0.2, 0.3\\}$: 3--5 seeds each).\nThe structural bias predicts universality (H7 tautology is always the global reward-maximizing exploit regardless of $\\beta$), and $\\beta$ controls only the probability of early sampling and thus the timing of collapse; at $\\beta{=}0.05$, three seeds confirm deterministic H7 collapse ($93.7\\%$ pooled) while the matched random control at the same $\\beta$ produces H1 redundancy instead ($77.4\\%$), ruling out dose magnitude as the driver.\nAt moderate doses ($\\beta{=}0.1$), collapse is stochastic and delayed (5 seeds bifurcate: 2 collapse rapidly, 3 sustain a transient genuine window that trajectory analysis confirms is temporary); at higher doses ($\\beta{=}0.2$), collapse is immediate and universal.\n$\\beta{=}0.3$ adds reward collapse~\\citep{gao-reward-overoptimization} as a competing failure mode (PR drops to 18\\% in 1/3 seeds), but the underlying Goodhart vulnerability remains the same.\nThe practical implication is that ISR (and structurally similar LOO-based diagnostics) should be used exclusively as post-hoc evaluation tools, never as training rewards.\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ (5 seeds) shows even greater instability: 2/5 seeds collapse to H7 within ${\\sim}150$ steps, while 3/5 sustain a transient genuine window.\nThe 5-seed pooled non-hacking rate is ${\\sim}23\\%$ at 500 steps; trajectory analysis on seeds~42 and~45 (1000 steps) confirms this is temporary ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine respectively).\nThe dominant hacking mode (H7 vs.\\ H1) is stochastic within any treatment condition ($\\text{CV}{>}1$).\nMulti-seed evaluation with trajectory analysis should be standard practice for neurosymbolic RL systems; single-seed or single-checkpoint results can misrepresent a configuration's true hacking profile.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify nine distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: 3-seed subset s42/s43/s44, per-seed breakdown in Table~\\ref{tab:fol-beta01-perseed}; 5-seed data in Table~\\ref{tab:goodhart-landscape}). ISR increases H7 probability without reducing total hacking; the specific mode (H7 vs.\\ H1) is seed-dependent within each condition. SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nH1 & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nH7 & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nH8 & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed subset (s42/s43/s44); 5-seed totals in Table~\\ref{tab:goodhart-landscape}. H7 includes subtypes H7a (text-match) and H7b (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random H7 in 3-seed subset driven by seed~43 (38.3\\%); 5-seed pooled: 30\\% (dominated by s46 at 91.5\\%). Exec: H1${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes. H8: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nH1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\subsection{H8 --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).\nWe term this \\textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull H8 audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.\n\n\\paragraph{H7 false-negative correction (H7b obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier (triple gaming; \\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter H8 reclassification and H7 false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (H7, H8) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{H1 --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as H1 (59--91\\%); under ISR reward, it shifts to H7 (54\\% pooled, 5-seed).\n\n\n\\subsection{H7a --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nH7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nH7a (text-match detectable): 64.5\\% (149/231, 3-seed) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%); 5-seed pooled H7: 54\\% (190/350, Table~\\ref{tab:goodhart-landscape}).\nCombined H7 (H7a + H7b, 3-seed): 70.6\\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 29.5\\% (122/414, 5-seed, all H7a; driven by s46 at 91.5\\% and s43 at 38.3\\%; s42/s44/s45 at 0\\%).\n\n\n\\subsection{H7b --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\nThe premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nH7b simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).\nThis triple gaming makes H7b the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from H7 by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% H7 by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% H7, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous; none is individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to H7 but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\subsection{H9 --- Ex Falso Quodlibet (Contradiction Injection)}\n\n\\paragraph{Definition.}\nThe model generates a premise set containing logically contradictory assertions (e.g., $P(x)$ and $\\neg P(x)$).\nFrom contradictory premises, any conclusion follows by the \\emph{ex falso quodlibet} principle, rendering the proof semantically vacuous regardless of the conclusion's content.\nUnlike the ``contradiction explosion'' mode observed in 4B exec-only at 1000 steps (where contradictions arise incidentally among inflated premise counts), H9 is a \\emph{targeted} strategy: the model constructs minimal contradictory pairs that directly enable the proof.\n\n\\paragraph{Example (FOL).}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  -bird(tweety).  % contradicts above\nConclusion: happy(tweety).\n% Proof: bird(tweety) & -bird(tweety) -> False -> anything\n\\end{verbatim}}\n\n\\paragraph{ISR interaction.}\nISR~$>0$ because each side of the contradiction is individually necessary under LOO: removing $P(x)$ leaves $\\neg P(x)$ alone, which cannot derive a contradiction; removing $\\neg P(x)$ leaves the premises consistent but insufficient to derive an unrelated conclusion.\nThe LOO test thus registers both contradictory premises as ``necessary,'' inflating ISR despite the formalization being semantically vacuous.\n\n\\paragraph{Prevalence.}\nObserved exclusively in Qwen3-1.7B under Random $\\beta{=}0.1$ (seed~42, 500 steps, proper train/eval separation): 100\\% of proved samples ($n{=}93$) exhibit H9.\nUnder ISR $\\beta{=}0.1$ with the same model, H9 does not appear; the model instead converges to fixed-template H1 ($\\text{ISR}{=}0.6$, zero variance), indicating that ISR reward redirects the hacking pathway from H9 to H1.\nNot observed in any Qwen3-4B experiment across all conditions and seeds tested. %% registry: d113-1.7b-random-b01-s42\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\\P$Inferred from ISR profile and contradiction-explosion pattern; formal text-match taxonomy not run on this checkpoint.}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & \\makebox[0pt][l]{$0.130$} & & \\makebox[0pt][l]{$0.595$} & & \\makebox[0pt][l]{\\textbf{92.3}} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100$^\\P$ & 0$^\\P$ & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & H1 dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & H8${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.68{\\pm}0.47$} & & \\makebox[0pt][l]{$0.238{\\pm}0.30$} & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.97{\\pm}0.02$} & & \\makebox[0pt][l]{$0.03{\\pm}0.05$} & & \\makebox[0pt][l]{$2.1{\\pm}3.6$} & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed H1+H7+H8 \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.77{\\pm}0.14$} & & \\makebox[0pt][l]{$0.716{\\pm}0.26$} & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\\cap$H8: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.87{\\pm}0.08$} & & \\makebox[0pt][l]{$0.117{\\pm}0.042$} & & & H7 seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Exec-only baseline at 1000 steps (3 seeds). All seeds converge to high PR with near-zero genuine output. s42 evaluated with ISR metrics only; hacking taxonomy unavailable.}\n\\label{tab:exec-only-1000}\n\\small\n\\begin{tabular}{lrrrrrr}\n\\toprule\nSeed & PR\\% & $n$ & H7\\% & H1\\% & H8\\% & N-H\\% \\\\\n\\midrule\ns42 & 96 & 96 & 0 & --- & --- & --- \\\\\ns43 & 96 & 96 & 0 & 93.8 & 0 & 6.2 \\\\\ns44 & 100 & 100 & 0 & 85.0 & 15.0 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Left}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$). \\textbf{Right}: Prolog ISR-reward gaming-mode composition: all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.53{\\pm}0.31$} & & \\makebox[0pt][l]{$0.146{\\pm}0.21$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & H7 tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional H7$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.62{\\pm}0.31$} & & \\makebox[0pt][l]{$0.699{\\pm}0.45$} & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict H7 classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig5_training_isr_curves.pdf}\n\\caption{Training ISR trajectories across reward conditions. ISR $\\beta{=}0.1$ seeds rise rapidly toward $\\text{ISR}{\\approx}1$ (Goodhart gaming via H7 tautology); exec-only s44's plateau at ${\\sim}0.5$ is an H7a artifact ($n{=}2$ gives $\\text{ISR}{\\geq}0.5$ by construction), not genuine structural quality; random $\\beta{=}0.1$ remains low. The s42 1k-step trace shows ISR eventually saturates at $0.88$ through the same H7 mechanism.}\n\\label{fig:training-isr-curves}\n\\end{figure}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: consistent gaming across all seeds via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart effects with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean H7 tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds, despite identical training data and reward function, demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\\beta{=}0.3$.\nThe three ISR seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & H1 shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure H7 gaming \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.66{\\pm}0.42$} & & \\makebox[0pt][l]{$0.39{\\pm}0.31$} & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & \\makebox[0pt][l]{$0.54{\\pm}0.35$} & & \\makebox[0pt][l]{$0.09{\\pm}0.09$} & & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Per-Seed Results at $\\beta{=}0.05$}\n\\label{app:beta005}\n\nThe 3-seed random control at $\\beta{=}0.05$ is highly unstable: s42 fails entirely ($\\text{PR}{=}0\\%$), s44 barely learns ($\\text{PR}{=}7\\%$, H1 $71\\%$, genuine $0\\%$), and only s43 reaches moderate output ($\\text{PR}{=}62\\%$, H1 $77\\%$, genuine $13\\%$).\nThe single random seed that learns (s43) shows higher genuine output than ISR ($13\\%$ vs.\\ $5.1\\%$ pooled), consistent with a signal-floor below which ISR's genuine component is undetectable while its H7 bias remains exploitable.\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nTo justify the per-clause LOO design (\\S\\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved \\emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nThe reward becomes $r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$.\nAfter 500 steps (seed~42), this variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$ (functionally zero), compared to $\\text{ISR}^*{=}0.132$ under standard exec-only and $\\text{ISR}^*{=}0.42$ under ISR $\\beta{=}0.1$.\n\n\\paragraph{ISR signal vs.\\ training dynamics.}\nAt the \\emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.\nAt the \\emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.\nThis confound depresses prove rate by 30 percentage points ($63\\%$ vs.\\ $93\\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.\nThe result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.\n",
    "structuredPatch": [
      {
        "oldStart": 117,
        "oldLines": 6,
        "newStart": 117,
        "newLines": 7,
        "lines": [
          " \\paragraph{Seed-level statistical analysis.}",
          " To address potential inflation from within-seed dependence, we supplement pooled Fisher exact tests with two seed-aware analyses.",
          " Cochran--Mantel--Haenszel (CMH) tests stratify by seed while pooling across samples: H7 $\\text{OR}_{\\text{CMH}}{=}2.46$ (95\\% CI $[1.85, 3.27]$, $p{=}5.6{\\times}10^{-16}$); genuine $\\text{OR}_{\\text{CMH}}{=}3.37$ (95\\% CI $[2.21, 5.13]$, $p{=}4.5{\\times}10^{-10}$).",
          "+CMH assumes within-stratum independence, but samples within each seed share a single checkpoint and use greedy decoding; the effective independent units are seeds ($n{=}5$), not samples, and CMH $p$-values are consequently inflated.",
          " Seed-level permutation tests (treating each seed as a single observation, $n{=}5$ per group) yield $p{=}0.28$ (H7) and $p{=}0.26$ (genuine), consistent with the severe power limitation of $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.",
          " ",
          " \\begin{table}[h]"
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

_source line 33_

All 5 Batch 1 edits done. Now checking for em-dashes and compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "c2eff6fa-9382-4893-a599-93d4d90bfb50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGK7DHZKYEt13DKtNnaCQD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2943,
      "cache_read_input_tokens": 60169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2943
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

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_012bgfFows2KDGJCHCcYqAwK`</summary>

```json
{
  "pattern": "—",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "ba5b5397-fa08-476d-9eca-6ba9f0cec103",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGK7DHZKYEt13DKtNnaCQD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2943,
      "cache_read_input_tokens": 60169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2943
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

_source line 35 · 2026-05-17T17:38:26.226Z_

<details><summary>↩ Tool result · `toolu_012bgfFows2KDGJCHCcYqAwK`</summary>

```text
paper/appendix.tex:1:% Appendix — solver-trace-ablation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "100082ff-9fb9-48fd-b88a-b29ff378826a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/appendix.tex:1:% Appendix — solver-trace-ablation",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01NiTADZQpE1VF6unKJa7CnP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX PDF",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "d37a303e-2d4f-4e7c-802f-12fd67ac6b56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGK7DHZKYEt13DKtNnaCQD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2943,
      "cache_read_input_tokens": 60169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2943
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

_source line 37 · 2026-05-17T17:38:29.787Z_

<details><summary>↩ Tool result · `toolu_01NiTADZQpE1VF6unKJa7CnP`</summary>

```text
msy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (22 pages, 604527 bytes).
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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "f34579f2-cfa1-4b26-acea-f1437419954c",
  "tool_use_result": {
    "stdout": "msy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/helvetic/uhvb8a.pfb>\nOutput written on main.pdf (22 pages, 604527 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
The em-dash found is in a comment line at the top of appendix.tex (`% Appendix — solver-trace-ablation`). That's a comment, not visible in the output, so it's fine. No em-dashes in actual content.

PDF compiled successfully with no errors. Let me check for undefined citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "88a61425-71fe-4bd1-9583-5d30f7355ad3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLfSdJ4uxMefuqpVETQybZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 63112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
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

_source line 39_

The only em-dash is in a comment line (not rendered). PDF compiled cleanly. Let me check for undefined citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "0d2190c9-b524-4193-b50c-c790e73622de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLfSdJ4uxMefuqpVETQybZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 63112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_011SPvFVDRV5Wbo7BNM7ZLxh`</summary>

```json
{
  "command": "grep -i \"undefined\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.log | grep -i \"citation\" | head -10",
  "description": "Check for undefined citations in LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "21d07bc2-72a8-457f-9119-eb248286ad32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLfSdJ4uxMefuqpVETQybZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 63112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
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

_source line 41 · 2026-05-17T17:38:36.516Z_

<details><summary>↩ Tool result · `toolu_011SPvFVDRV5Wbo7BNM7ZLxh`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "7f7a99ae-d288-4613-ad2a-d6fc7495ef24",
  "tool_use_result": {
    "stdout": "",
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

_source line 42_

No undefined citations. Now committing Batch 1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "9c77ea31-f2c4-42bb-abbe-528357adb767",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JnuXoJt6wAjeYFc3otwYg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 63932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01RUV2Pum2fDiemjFMmV93Jy`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation && git add paper/experiments.tex paper/conclusion.tex paper/limitations.tex paper/appendix.tex paper/main.pdf paper/main.log && git commit -m \"$(cat <<'EOF'\n[paper] Round 7 Batch 1: CMH non-independence caveat across 5 files, transient window reframed as descriptive\n\nCo-Authored-By: Claude Opus 4.6 &lt;noreply@anthropic.com>\nEOF\n)\"",
  "description": "Commit Batch 1 changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "d777ccf1-0745-4f23-a137-e691cafe7945",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JnuXoJt6wAjeYFc3otwYg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 63932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
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

_source line 44 · 2026-05-17T17:38:44.015Z_

<details><summary>↩ Tool result · `toolu_01RUV2Pum2fDiemjFMmV93Jy`</summary>

```text
[master 37317d3] [paper] Round 7 Batch 1: CMH non-independence caveat across 5 files, transient window reframed as descriptive
 Committer: Ubuntu &lt;ubuntu@ip-172-31-5-208.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 6 files changed, 91 insertions(+), 77 deletions(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "630444e4-ae8c-4b47-8427-5c5a8a01b7ae",
  "tool_use_result": {
    "stdout": "[master 37317d3] [paper] Round 7 Batch 1: CMH non-independence caveat across 5 files, transient window reframed as descriptive\n Committer: Ubuntu &lt;ubuntu@ip-172-31-5-208.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 6 files changed, 91 insertions(+), 77 deletions(-)",
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

_source line 45_

Batch 1 committed. Now starting Batch 2. Let me count citations in introduction.tex before making changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "476413ed-39d1-40cf-a021-678493497591",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015piYLCDtfziAJSU9hoo4bj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 64190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 421
      },
      "output_tokens": 6,
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

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_015gBiduQryFSTpcDQJXtv9P`</summary>

```json
{
  "command": "grep -c \"\\\\\\\\cite\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "description": "Count citations in introduction.tex before changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "45f847cf-fac2-461b-815b-0ca3af76ab52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015piYLCDtfziAJSU9hoo4bj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 64190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 421
      },
      "output_tokens": 6,
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

_source line 47 · 2026-05-17T17:38:49.324Z_

<details><summary>↩ Tool result · `toolu_015gBiduQryFSTpcDQJXtv9P`</summary>

```text
9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "ba59d0cf-2c16-4264-8927-487f039fa2b3",
  "tool_use_result": {
    "stdout": "9",
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

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01VbVaGhN5iNBCnpaUsbiQXL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "edd96cbb-fcc0-4391-a131-b64eb3f54636",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015piYLCDtfziAJSU9hoo4bj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 421,
      "cache_read_input_tokens": 64190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 421
      },
      "output_tokens": 6,
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

_source line 49 · 2026-05-17T17:38:49.621Z_

<details><summary>↩ Tool result · `toolu_01VbVaGhN5iNBCnpaUsbiQXL`</summary>

```text
1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "fd559f51-ebde-470c-bc3d-1d7556a0f662",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 376
    }
  }
}
```

</details>

---

### Assistant

_source line 50_

9 citations before. Now making Batch 2 changes.

**Change 6**: Remove "Notably" AI marker in experiments.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "9f6b590a-58db-48ca-9ffc-e02296032758",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mtiffdGdpr9JACz7uBpyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 64611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 902
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

<details open><summary>🔧 Tool call — Edit · `toolu_01CjFPmQMnNiqmpmM4pBSeph`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "Notably, s43 recovers",
  "new_string": "S43 recovers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "b05ce87b-d570-41fa-bc53-ef739bbec66a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mtiffdGdpr9JACz7uBpyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 64611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 902
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

_source line 52 · 2026-05-17T17:38:55.629Z_

<details><summary>↩ Tool result · `toolu_01CjFPmQMnNiqmpmM4pBSeph`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "42136c24-c4f3-4c8f-b505-0aa2479b2164",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "Notably, s43 recovers",
    "newString": "S43 recovers",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nCross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\\S\\ref{sec:crossscale}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}) with greedy decoding (Appendix~\\ref{app:setup}).\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ (at 500 steps) via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.97{\\pm}0.02$) with near-zero genuine output (see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\\%$, genuine $6.2\\%$; s44: H1 $85\\%$ + H8 $15\\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2\nNotably, s43 recovers from $\\text{PR}{=}13\\%$ (500 steps) to $\\text{PR}{=}96\\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$; per-seed range ${\\sim}$91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific; a 100-step checkpoint ($\\text{PR}{=}32\\%$, hacking${\\geq}31\\%$) partially controls for the PR-level confound, though the PR gap remains substantial (Appendix~\\ref{app:100step}).\nSFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.\nWhether SFT would develop similar exploits at higher prove rates remains an open question; this mechanistic argument is plausible but not conclusive.\n\n\\subsection{ISR as Reward: Goodhart Effects}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nWe present $\\beta{=}0.1$ first as the focal dose (5 seeds, trajectory analysis), then examine lower and higher doses.\nThe headline finding: ISR contains an inherent Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy} observed to produce collapse at all four tested doses ($\\beta\\in\\{0.05, 0.1, 0.2, 0.3\\}$).\nThe mechanism is structural: tautological proofs ($P{\\to}P$) receive $\\text{ISR}{=}0.75$ and single-premise-equals-conclusion constructions receive $\\text{ISR}{\\geq}0.5$, both by the LOO definition alone.\nOnce sampled during GRPO rollouts, these high-ISR tautologies create a positive feedback loop; $\\beta$ controls only the \\emph{timing} of collapse, not whether it occurs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nExec-only (1k)$^{\\dagger\\dagger}$ & --- & 97{\\scriptsize$\\pm$2} & 0.03{\\scriptsize$\\pm$.05} & 0 & --- & $\\leq$2$^{\\dagger\\dagger}$ \\\\\nISR$^\\ddagger$ & 0.1 & 70{\\scriptsize$\\pm$19} & --- & \\textbf{54} & 18 & 23$^\\star$ \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)\nRandom & 0.1 & \\textbf{83}{\\scriptsize$\\pm$15} & 0.080{\\scriptsize$\\pm$.06} & 30 & 59 & 8 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)\nISR & 0.2 & 97{\\scriptsize$\\pm$4} & 0.69{\\scriptsize$\\pm$.24} & \\textbf{99} & 0 & 0 \\\\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\\ref{tab:beta02-detail})\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-1.7B (seed~42)}} \\\\\nISR & 0.1 & 100 & 0.600 & 0 & \\textbf{100} & 0 \\\\ %% registry: d113-1.7b-isr-b01-s42\nRandom & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\\\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)\nISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\\\ %% registry: d113-1.7b-isr-b03-s42\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape. PR/ISR$^*$: mean$\\pm$std; H7/H1/N-H: pooled \\%. $^\\dagger$s42, 500 steps. $^\\ddagger$N-H uncorrected upper bound (s43/s44 H8 audit unavailable). $^\\star$Transient; collapses at 1000 steps (\\S\\ref{sec:goodhart-temporal}). $^{\\dagger\\dagger}$3-seed 1000-step (Appendix Table~\\ref{tab:exec-only-1000}).}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): stochastic delayed collapse.}\nAt $\\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\\geq}97\\%$ H7, $0\\%$ genuine within ${\\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.\nThe 5-seed pooled non-hacking rate is ${\\sim}23\\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\\%$ to $55\\%$ genuine.\nThis bifurcation is stochastic: all seeds are indistinguishable in the first ${\\sim}100$ steps ($\\text{ISR}{\\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\\text{ISR}{\\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.\nOnce a seed enters the H7 basin, convergence to saturation takes ${\\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46\n\nH7 (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by the LOO definition; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both ISR and random conditions (Appendix Figure~\\ref{fig:hacking-composition}); the specific mode (H7 vs.\\ H1) within a seed is stochastic under both conditions ($\\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.\nRandom yields higher PR ($83{\\pm}15\\%$ vs.\\ $70{\\pm}19\\%$; $n{=}5$ each).\nRandom H7 exhibits extreme seed dependence (per-seed range: $0\\%$--$91.5\\%$; pooled $30\\%$ is dominated by s46 at $91.5\\%$ and s43 at $38.3\\%$).\nBoth conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\\%$ of proved samples in affected seeds: s43${=}61/61$, s44${=}89/89$), while random-induced H7 coexists with other modes ($38$--$92\\%$).\nISR's reward signal converts H7 from a stochastic possibility into an irreversible attractor once sampled.\nThe reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\\beta$ versus ${\\sim}1{+}0.26\\beta$ for genuine proofs (premise-count-matched), a gap of ${\\sim}0.49\\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.\n\n\\textbf{The transient genuine window.}\nAt 500 steps, 3 of 5 ISR seeds sustain genuine output (per-seed range: 2\\%--55\\%) versus 0 of 5 random seeds, a descriptive pattern consistent with ISR temporarily rewarding necessary premises before H7 dominates.\nHowever, statistical inference is limited: Cochran--Mantel--Haenszel tests yield $\\text{OR}_{\\text{CMH}}{=}3.37$ ($p{<}10^{-9}$), but within-seed samples share a checkpoint and use greedy decoding, violating the independence assumption required by CMH; the effective sample size is seeds ($n{=}5$), not samples ($n{=}350$/$414$).\nSeed-level permutation tests, which correctly treat seeds as the unit of observation, yield $p{=}0.26$ (genuine), consistent with the severe power limitation at $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\nUnder stricter classification (H8+FN correction on 3 fully-audited seeds), the direction reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine at 1000 steps).\nThe transient benefit is descriptively observed but statistically underpowered at seed-level ($n{=}5$); it should not be interpreted as evidence that ISR reliably improves structural quality. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000\n\n\\textbf{Premise-count confound.}\nThe genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\\ref{app:extended-discussion}).\n\n\\textbf{Trajectory analysis: timing, not destiny.}\\label{sec:goodhart-temporal}\nExtended training (1000 steps; Appendix Figure~\\ref{fig:training-isr-curves}) confirms the genuine window is transient across seeds.\nSeed~42 declines from $17\\%$ to $2\\%$ genuine via H7 saturation ($16.0\\%{\\to}96.7\\%$ H7, PR stable at ${\\sim}96\\%$); seed~45, which achieved the highest 500-step genuine rate ($55\\%$), collapses to $0\\%$ genuine through reward collapse ($\\text{PR}: 42\\%{\\to}2\\%$).\nThe two seeds exhibit distinct failure paths (H7 gaming vs.\\ output collapse) but converge to the same outcome: zero genuine proofs at extended training. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42, plan002-b01-s45-1000\n\n\\textbf{Micro-dose ISR ($\\beta{=}0.05$): deterministic collapse.}\nAll three ISR seeds reach $\\text{PR}{\\geq}99\\%$ but converge to H7a tautology (H7 $87$--$100\\%$, genuine $5.1\\%$), while the random control mostly fails to learn (median $\\text{PR}{=}7\\%$) with zero H7, confirming H7 as specific to ISR's LOO structure.\nBelow a signal-floor, ISR's genuine component is undetectable while its H7 bias remains exploitable (per-seed breakdown in Appendix~\\ref{app:beta005}). %% registry: sweep-isr-b005-s42/s43/s44, sweep-random-b005-s42/s43/s44\n\n\\textbf{Medium-dose ISR ($\\beta{=}0.2$): maximum exploitation.}\nAll three seeds converge to pure H7a tautology ($0\\%$ non-hacking, $n{=}290$; Appendix Table~\\ref{tab:beta02-detail}). %% registry: sweep-isr-b02-s42/s43/s44\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\\ref{app:beta03}).\nThe random control is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$) with $91\\%$ H1 and ${\\leq}4\\%$ non-hacking; high-dose proxy weighting destabilizes training regardless of signal source. %% registry: plan002-additive-b03-s42/s43/s44\nISR vs.\\ random H7 at $\\beta{=}0.3$: $\\text{OR}{=}13.7$, 95\\% CI $[7.0, 26.8]$ (Appendix~\\ref{app:beta03}).\n\n\\textbf{Non-monotonic dose-response.}\nThe four $\\beta$ levels suggest a non-monotonic pattern: $\\beta\\in\\{0.05, 0.2\\}$ converge deterministically to H7 collapse (${\\geq}94\\%$ H7), $\\beta{=}0.3$ triggers multi-modal instability, and only $\\beta{=}0.1$ sustains a transient genuine window (3 of 5 seeds).\nGoodhart collapse is not a simple function of dose; the balance between genuine and exploit reinforcement depends on a threshold interaction between $\\beta$ and rollout stochasticity.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (3 seeds, $\\beta{=}0.1$).\nUnder exec-only training, 2/3 seeds show $\\text{ISR}^{*}{\\approx}0$ despite $\\text{PR}{\\geq}0.56$, reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding; ISR flags both failure semantics.\nUnder ISR reward, 3/3 seeds reach $0\\%$ non-hacking through three distinct mechanisms: clean H7 tautology (s42, $\\text{ISR}^{*}{=}1.0$), degenerate uppercase pseudo-Prolog evading text-match classifiers (s43, functional $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, $95/97$ proved at $n_{\\text{necessary}}{=}1$).\nSeed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.\nWe attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\\ref{tab:prolog-detailed} and Figure~\\ref{fig:prolog-comparison}).\n\n\\subsection{Cross-Scale Evidence}\n\\label{sec:crossscale}\n\nWe train Qwen3-1.7B under ISR $\\beta\\in\\{0.1,0.3\\}$ and Random $\\beta{=}0.1$ (single seed, 500 steps).\nAll conditions produce $0\\%$ non-hacking, but the exploit modes differ qualitatively from 4B: Random discovers H9 (contradiction injection, $\\text{PR}{=}93\\%$, $100\\%$ \\emph{ex falso}), ISR $\\beta{=}0.1$ collapses to a single fixed template ($\\text{ISR}^{*}{=}0.6$ at zero variance, $100\\%$ H1), and ISR $\\beta{=}0.3$ triggers reward collapse ($\\text{PR}{=}17\\%$) mirroring the 4B pattern.\nH9 never appears at 4B scale; fixed-template mode collapse never appears at 4B; different capacities converge to different Goodhart basins under identical rewards.\nNo safe scale was observed in this single-seed comparison (Table~\\ref{tab:hacking-taxonomy}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{Rnd}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 59 & 7 & 0$^\\sharp$ & \\textbf{100} & 0 \\\\\nH7 duplicate   & 0  & \\textbf{54} & 30 & 0 & 100$^\\sharp$ & 0 & 0 \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 & 0 \\\\\nH9 ex falso    & --- & --- & --- & --- & --- & 0 & \\textbf{100} \\\\\nTautological   & --- & --- & --- & --- & s42 & --- & --- \\\\\nRepetition     & s43 & --- & --- & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & \\textbf{23}  & 8 & \\textbf{92} & \\textbf{0} & \\textbf{0} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Nine hacking modes (\\% of proved; exec/SFT: s42; ISR/Random 4B: 5-seed pooled; 1.7B: s42). H7a+H7b combined. Seed IDs mark dominant mode. $^\\sharp$Prolog: strict+functional pooled. Modes marked with seed identifiers are single-seed observations.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe nine modes (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 conditions.\nH1, H7, and H8 account for ${>}90\\%$ of hacking; H7b ($14/350$) evades text-match classifiers.\nISR modestly increases H7 probability ($\\text{OR}{=}2.84$, $p{<}5{\\times}10^{-12}$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.\nAll GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\nCMH tests treating samples as independent yield $\\text{OR}_{\\text{CMH}}{=}2.46$ ($p{<}10^{-15}$) for H7 and $3.37$ ($p{<}10^{-9}$) for genuine output; however, within-seed non-independence inflates these $p$-values (see \\S\\ref{sec:goodhart} for seed-level analysis).\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " The three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ (at 500 steps) via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44",
          " The cross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).",
          " By 1000 steps, all three converge to high PR ($0.97{\\pm}0.02$) with near-zero genuine output (see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\\%$, genuine $6.2\\%$; s44: H1 $85\\%$ + H8 $15\\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2",
          "-Notably, s43 recovers from $\\text{PR}{=}13\\%$ (500 steps) to $\\text{PR}{=}96\\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.",
          "+S43 recovers from $\\text{PR}{=}13\\%$ (500 steps) to $\\text{PR}{=}96\\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.",
          " ",
          " \\textbf{SFT baseline.}",
          " SFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$; per-seed range ${\\sim}$91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3"
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

<details open><summary>🔧 Tool call — Edit · `toolu_018KSNUkJRXyyz6MVZ3CrEsC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\subsection{Cross-Scale Evidence}",
  "new_string": "\\subsection{Preliminary Cross-Scale Evidence}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "441acc36-7f58-4a9a-a2d1-1a0f8173861d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mtiffdGdpr9JACz7uBpyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 64611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 902
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

_source line 54 · 2026-05-17T17:38:57.107Z_

<details><summary>↩ Tool result · `toolu_018KSNUkJRXyyz6MVZ3CrEsC`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "74276338-4371-40b7-84c7-e986b9e5bd5f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "\\subsection{Cross-Scale Evidence}",
    "newString": "\\subsection{Preliminary Cross-Scale Evidence}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and STA as a cross-logic protocol (\\S\\ref{sec:crosslogic}).\nCross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\\S\\ref{sec:crossscale}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\\footnote{All experiments use \\texttt{data/train\\_500\\_seed42.jsonl}; seeds control initialization and rollout sampling only.}\nHeld-out evaluation uses 100 FOLIO examples (\\texttt{proofwriter\\_fol\\_100.jsonl}) with greedy decoding (Appendix~\\ref{app:setup}).\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, defined as the residual of proved samples matching none of the nine cataloged patterns (a necessary but not sufficient condition for semantic correctness).\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/fig2_isr_collapse.pdf}\n\\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\\%$\\to$93\\%$\\to$96\\% while proved-only ISR falls $0.642{\\to}0.132{\\to}0.003$ over 100$\\to$500$\\to$1000 steps. By step 1000, 94.8\\% of proved samples have $\\text{ISR}{=}0$ and mean component count inflates 6.58$\\to$18.55 (contradiction explosion).}\n\\label{fig:isr-collapse}\n\\end{figure}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:isr-collapse} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (H1); by 1000 steps, the embedding rate saturates at 100\\% and mean component count more than doubles ($6.58\\to18.55$) as the model emits contradictory or vacuous premises that trivially derive any conclusion.\nExtended training, lacking a structural signal, \\emph{worsens} formalization quality while improving the headline number.\n\n\\textbf{Cross-seed instability.}\nThe three exec-only seeds diverge into qualitatively different failure modes despite shared data, hyperparameters, and reward (Appendix~\\ref{app:detailed-results}): s42 reaches $\\text{PR}{=}93\\%$ via conclusion embedding ($\\text{H1}{=}87\\%$); s43 collapses to $\\text{PR}{=}13\\%$ (at 500 steps) via repetition (87\\% of rollouts truncated); s44 reaches $\\text{PR}{=}98\\%$ via tautological collapse ($\\text{H7}{=}100\\%$, mean $n{=}2.04$). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44\nThe cross-seed PR variance ($\\sigma{=}47$\\,pp) shows that aggregate metrics obscure qualitatively different failure modes; all three are flagged by $\\text{ISR}^*$ even though one passes the PR check (s44) and one fails it (s43).\nBy 1000 steps, all three converge to high PR ($0.97{\\pm}0.02$) with near-zero genuine output (see Appendix~\\ref{app:h8} and Table~\\ref{tab:fol-detailed}), each through a different dominant mode (s42: $\\text{ISR}^{*}{=}0.003$, taxonomy unavailable; s43: H1 $93.8\\%$, genuine $6.2\\%$; s44: H1 $85\\%$ + H8 $15\\%$). %% registry: plan016-extended-1000-s42, exec-only-s43-1000step-r7, plan001-exec-only-s44-1000-r2\nS43 recovers from $\\text{PR}{=}13\\%$ (500 steps) to $\\text{PR}{=}96\\%$ (1000 steps), but entirely through H1 exploitation: PR recovery does not imply quality recovery, and the repetition-collapse phase is transient rather than terminal.\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $\\text{PR}{=}13.0\\%$ (3-seed pooled, 1000 steps) with $\\text{H7}{=}0$, $\\text{H1}{=}7.7\\%$, $92.3\\%$ non-hacking ($n{=}39$; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$; per-seed range ${\\sim}$91--93\\%). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\nThe near-absence of hacking under identical data exposure is consistent with hacking being RL-specific; a 100-step checkpoint ($\\text{PR}{=}32\\%$, hacking${\\geq}31\\%$) partially controls for the PR-level confound, though the PR gap remains substantial (Appendix~\\ref{app:100step}).\nSFT trains via negative log-likelihood on gold formalizations without exploration-exploitation dynamics; exploit discovery requires the trial-and-error sampling inherent to RL but absent from supervised training.\nWhether SFT would develop similar exploits at higher prove rates remains an open question; this mechanistic argument is plausible but not conclusive.\n\n\\subsection{ISR as Reward: Goodhart Effects}\n\\label{sec:goodhart}\n\nWe now reverse roles: instead of treating ISR as an observer, we use it as a reward augmentation, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with a matched random control, $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,u)$, $u\\sim\\mathcal{U}(0,1)$, to isolate ISR-specific signal from generic reward-variance effects.\nWe present $\\beta{=}0.1$ first as the focal dose (5 seeds, trajectory analysis), then examine lower and higher doses.\nThe headline finding: ISR contains an inherent Goodhart vulnerability~\\citep{manheim-goodhart-taxonomy} observed to produce collapse at all four tested doses ($\\beta\\in\\{0.05, 0.1, 0.2, 0.3\\}$).\nThe mechanism is structural: tautological proofs ($P{\\to}P$) receive $\\text{ISR}{=}0.75$ and single-premise-equals-conclusion constructions receive $\\text{ISR}{\\geq}0.5$, both by the LOO definition alone.\nOnce sampled during GRPO rollouts, these high-ISR tautologies create a positive feedback loop; $\\beta$ controls only the \\emph{timing} of collapse, not whether it occurs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{H7\\%} & \\textbf{H1\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)\nExec-only (1k)$^{\\dagger\\dagger}$ & --- & 97{\\scriptsize$\\pm$2} & 0.03{\\scriptsize$\\pm$.05} & 0 & --- & $\\leq$2$^{\\dagger\\dagger}$ \\\\\nISR$^\\ddagger$ & 0.1 & 70{\\scriptsize$\\pm$19} & --- & \\textbf{54} & 18 & 23$^\\star$ \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46 (5-seed, D124)\nRandom & 0.1 & \\textbf{83}{\\scriptsize$\\pm$15} & 0.080{\\scriptsize$\\pm$.06} & 30 & 59 & 8 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2/s45/s46 (5-seed)\nISR & 0.2 & 97{\\scriptsize$\\pm$4} & 0.69{\\scriptsize$\\pm$.24} & \\textbf{99} & 0 & 0 \\\\ %% registry: sweep-isr-b02-s42/s43/s44 (3-seed; Appendix Table~\\ref{tab:beta02-detail})\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-1.7B (seed~42)}} \\\\\nISR & 0.1 & 100 & 0.600 & 0 & \\textbf{100} & 0 \\\\ %% registry: d113-1.7b-isr-b01-s42\nRandom & 0.1 & 93 & 0.028 & 0 & 0 & 0 \\\\ %% registry: d113-1.7b-random-b01-s42 (H9=100%)\nISR & 0.3 & 17 & 0.031 & 0 & 71 & 29 \\\\ %% registry: d113-1.7b-isr-b03-s42\n\\bottomrule\n\\end{tabular}}\n\\caption{Goodhart landscape. PR/ISR$^*$: mean$\\pm$std; H7/H1/N-H: pooled \\%. $^\\dagger$s42, 500 steps. $^\\ddagger$N-H uncorrected upper bound (s43/s44 H8 audit unavailable). $^\\star$Transient; collapses at 1000 steps (\\S\\ref{sec:goodhart-temporal}). $^{\\dagger\\dagger}$3-seed 1000-step (Appendix Table~\\ref{tab:exec-only-1000}).}\n\\label{tab:goodhart-landscape}\n\\end{table}\n\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): stochastic delayed collapse.}\nAt $\\beta{=}0.1$, 5 seeds exhibit a striking bifurcation: 2 seeds (s43, s44) collapse rapidly to near-pure H7 tautology (${\\geq}97\\%$ H7, $0\\%$ genuine within ${\\sim}150$ steps), while 3 seeds (s42, s45, s46) sustain a transient genuine window.\nThe 5-seed pooled non-hacking rate is ${\\sim}23\\%$ at 500 steps, with the collapsed seeds pulling down the average; the 3 non-collapsed seeds individually range from $17\\%$ to $55\\%$ genuine.\nThis bifurcation is stochastic: all seeds are indistinguishable in the first ${\\sim}100$ steps ($\\text{ISR}{\\approx}0.05$--$0.07$); divergence occurs at steps 150--200 when H7 tautologies, which receive $\\text{ISR}{\\geq}0.5$ by construction, are sampled during rollouts and reinforced via the positive feedback loop.\nOnce a seed enters the H7 basin, convergence to saturation takes ${\\sim}150$ steps and is irreversible. %% registry: plan002-additive-b01-s42/s43-r2/s44/s45/s46\n\nH7 (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by the LOO definition; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart exploit: the model satisfies the structural metric directly rather than producing a genuine derivation.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both ISR and random conditions (Appendix Figure~\\ref{fig:hacking-composition}); the specific mode (H7 vs.\\ H1) within a seed is stochastic under both conditions ($\\text{CV}{>}1$), though ISR modestly increases H7 probability by providing a direct reward pathway.\nRandom yields higher PR ($83{\\pm}15\\%$ vs.\\ $70{\\pm}19\\%$; $n{=}5$ each).\nRandom H7 exhibits extreme seed dependence (per-seed range: $0\\%$--$91.5\\%$; pooled $30\\%$ is dominated by s46 at $91.5\\%$ and s43 at $38.3\\%$).\nBoth conditions produce H7 in 2 of 5 seeds, but the quality differs: ISR-induced H7 is absorbing ($100\\%$ of proved samples in affected seeds: s43${=}61/61$, s44${=}89/89$), while random-induced H7 coexists with other modes ($38$--$92\\%$).\nISR's reward signal converts H7 from a stochastic possibility into an irreversible attractor once sampled.\nThe reward landscape explains H7's attractor strength: H7 tautologies receive expected reward $1{+}0.75\\beta$ versus ${\\sim}1{+}0.26\\beta$ for genuine proofs (premise-count-matched), a gap of ${\\sim}0.49\\beta$ that creates a persistent gradient toward tautological constructions regardless of dose.\n\n\\textbf{The transient genuine window.}\nAt 500 steps, 3 of 5 ISR seeds sustain genuine output (per-seed range: 2\\%--55\\%) versus 0 of 5 random seeds, a descriptive pattern consistent with ISR temporarily rewarding necessary premises before H7 dominates.\nHowever, statistical inference is limited: Cochran--Mantel--Haenszel tests yield $\\text{OR}_{\\text{CMH}}{=}3.37$ ($p{<}10^{-9}$), but within-seed samples share a checkpoint and use greedy decoding, violating the independence assumption required by CMH; the effective sample size is seeds ($n{=}5$), not samples ($n{=}350$/$414$).\nSeed-level permutation tests, which correctly treat seeds as the unit of observation, yield $p{=}0.26$ (genuine), consistent with the severe power limitation at $n{=}5$ (minimum achievable $p{=}0.008$) rather than absence of effect.\nUnder stricter classification (H8+FN correction on 3 fully-audited seeds), the direction reverses ($\\text{OR}{=}0.61$, n.s.), and extended training confirms the window closes completely ($17\\%{\\to}2\\%$ and $55\\%{\\to}0\\%$ genuine at 1000 steps).\nThe transient benefit is descriptively observed but statistically underpowered at seed-level ($n{=}5$); it should not be interpreted as evidence that ISR reliably improves structural quality. %% registry: plan002-b01-s42/s45/s46 (500 step) + plan002-b01-s42-1000\n\n\\textbf{Premise-count confound.}\nThe genuine-rate advantage reflects a selection effect: premise-count-matched comparison yields only $1.06\\times$ ISR difference, confirming indistinguishable per-proof quality once LOO bias toward short outputs is controlled (Appendix~\\ref{app:extended-discussion}).\n\n\\textbf{Trajectory analysis: timing, not destiny.}\\label{sec:goodhart-temporal}\nExtended training (1000 steps; Appendix Figure~\\ref{fig:training-isr-curves}) confirms the genuine window is transient across seeds.\nSeed~42 declines from $17\\%$ to $2\\%$ genuine via H7 saturation ($16.0\\%{\\to}96.7\\%$ H7, PR stable at ${\\sim}96\\%$); seed~45, which achieved the highest 500-step genuine rate ($55\\%$), collapses to $0\\%$ genuine through reward collapse ($\\text{PR}: 42\\%{\\to}2\\%$).\nThe two seeds exhibit distinct failure paths (H7 gaming vs.\\ output collapse) but converge to the same outcome: zero genuine proofs at extended training. %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42, plan002-b01-s45-1000\n\n\\textbf{Micro-dose ISR ($\\beta{=}0.05$): deterministic collapse.}\nAll three ISR seeds reach $\\text{PR}{\\geq}99\\%$ but converge to H7a tautology (H7 $87$--$100\\%$, genuine $5.1\\%$), while the random control mostly fails to learn (median $\\text{PR}{=}7\\%$) with zero H7, confirming H7 as specific to ISR's LOO structure.\nBelow a signal-floor, ISR's genuine component is undetectable while its H7 bias remains exploitable (per-seed breakdown in Appendix~\\ref{app:beta005}). %% registry: sweep-isr-b005-s42/s43/s44, sweep-random-b005-s42/s43/s44\n\n\\textbf{Medium-dose ISR ($\\beta{=}0.2$): maximum exploitation.}\nAll three seeds converge to pure H7a tautology ($0\\%$ non-hacking, $n{=}290$; Appendix Table~\\ref{tab:beta02-detail}). %% registry: sweep-isr-b02-s42/s43/s44\n\n\\textbf{High-dose ISR ($\\beta{=}0.3$): multi-modal Goodhart.}\nAt $\\beta{=}0.3$, ISR produces extreme cross-seed instability ($\\text{PR}{=}66{\\pm}42\\%$): three seeds yield three distinct failure modes (reward collapse, H1 shortcutting, pure H7 gaming; per-seed details in Appendix~\\ref{app:beta03}).\nThe random control is equally unstable ($\\text{PR}{=}54{\\pm}35\\%$) with $91\\%$ H1 and ${\\leq}4\\%$ non-hacking; high-dose proxy weighting destabilizes training regardless of signal source. %% registry: plan002-additive-b03-s42/s43/s44\nISR vs.\\ random H7 at $\\beta{=}0.3$: $\\text{OR}{=}13.7$, 95\\% CI $[7.0, 26.8]$ (Appendix~\\ref{app:beta03}).\n\n\\textbf{Non-monotonic dose-response.}\nThe four $\\beta$ levels suggest a non-monotonic pattern: $\\beta\\in\\{0.05, 0.2\\}$ converge deterministically to H7 collapse (${\\geq}94\\%$ H7), $\\beta{=}0.3$ triggers multi-modal instability, and only $\\beta{=}0.1$ sustains a transient genuine window (3 of 5 seeds).\nGoodhart collapse is not a simple function of dose; the balance between genuine and exploit reinforcement depends on a threshold interaction between $\\beta$ and rollout stochasticity.\n\n\\subsection{Cross-Logic Diagnostic Transfer}\n\\label{sec:crosslogic}\n\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (3 seeds, $\\beta{=}0.1$).\nUnder exec-only training, 2/3 seeds show $\\text{ISR}^{*}{\\approx}0$ despite $\\text{PR}{\\geq}0.56$, reflecting redundant ground-fact repetition rather than FOL-style conclusion embedding; ISR flags both failure semantics.\nUnder ISR reward, 3/3 seeds reach $0\\%$ non-hacking through three distinct mechanisms: clean H7 tautology (s42, $\\text{ISR}^{*}{=}1.0$), degenerate uppercase pseudo-Prolog evading text-match classifiers (s43, functional $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, $95/97$ proved at $n_{\\text{necessary}}{=}1$).\nSeed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.\nWe attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\\ref{tab:prolog-detailed} and Figure~\\ref{fig:prolog-comparison}).\n\n\\subsection{Cross-Scale Evidence}\n\\label{sec:crossscale}\n\nWe train Qwen3-1.7B under ISR $\\beta\\in\\{0.1,0.3\\}$ and Random $\\beta{=}0.1$ (single seed, 500 steps).\nAll conditions produce $0\\%$ non-hacking, but the exploit modes differ qualitatively from 4B: Random discovers H9 (contradiction injection, $\\text{PR}{=}93\\%$, $100\\%$ \\emph{ex falso}), ISR $\\beta{=}0.1$ collapses to a single fixed template ($\\text{ISR}^{*}{=}0.6$ at zero variance, $100\\%$ H1), and ISR $\\beta{=}0.3$ triggers reward collapse ($\\text{PR}{=}17\\%$) mirroring the 4B pattern.\nH9 never appears at 4B scale; fixed-template mode collapse never appears at 4B; different capacities converge to different Goodhart basins under identical rewards.\nNo safe scale was observed in this single-seed comparison (Table~\\ref{tab:hacking-taxonomy}).\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{ISR}}$} & \\textbf{1.7B$_{\\text{Rnd}}$} \\\\\n\\midrule\nH1 embed       & 87 & 18 & 59 & 7 & 0$^\\sharp$ & \\textbf{100} & 0 \\\\\nH7 duplicate   & 0  & \\textbf{54} & 30 & 0 & 100$^\\sharp$ & 0 & 0 \\\\\nH8 prem-subset & 6  & 5  & 8   & 0 & --- & 0 & 0 \\\\\nH9 ex falso    & --- & --- & --- & --- & --- & 0 & \\textbf{100} \\\\\nTautological   & --- & --- & --- & --- & s42 & --- & --- \\\\\nRepetition     & s43 & --- & --- & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- & --- & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 & --- & --- \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & \\textbf{23}  & 8 & \\textbf{92} & \\textbf{0} & \\textbf{0} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Nine hacking modes (\\% of proved; exec/SFT: s42; ISR/Random 4B: 5-seed pooled; 1.7B: s42). H7a+H7b combined. Seed IDs mark dominant mode. $^\\sharp$Prolog: strict+functional pooled. Modes marked with seed identifiers are single-seed observations.}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThe nine modes (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}) span 2 logic types, 2 model scales, and 6 conditions.\nH1, H7, and H8 account for ${>}90\\%$ of hacking; H7b ($14/350$) evades text-match classifiers.\nISR modestly increases H7 probability ($\\text{OR}{=}2.84$, $p{<}5{\\times}10^{-12}$; Appendix Table~\\ref{tab:bootstrap-ci}), but per-seed variance dominates.\nAll GRPO conditions show ${\\geq}80\\%$ pooled hacking; only SFT achieves $92.3\\%$ non-hacking.\nCMH tests treating samples as independent yield $\\text{OR}_{\\text{CMH}}{=}2.46$ ($p{<}10^{-15}$) for H7 and $3.37$ ($p{<}10^{-9}$) for genuine output; however, within-seed non-independence inflates these $p$-values (see \\S\\ref{sec:goodhart} for seed-level analysis).\n",
    "structuredPatch": [
      {
        "oldStart": 133,
        "oldLines": 7,
        "newStart": 133,
        "newLines": 7,
        "lines": [
          " Seed~44 evaded our strict classifier entirely; functional cross-validation was required to expose it.",
          " We attribute complete collapse to Prolog's simpler operational semantics providing a broader gaming basin (detailed results in Appendix Table~\\ref{tab:prolog-detailed} and Figure~\\ref{fig:prolog-comparison}).",
          " ",
          "-\\subsection{Cross-Scale Evidence}",
          "+\\subsection{Preliminary Cross-Scale Evidence}",
          " \\label{sec:crossscale}",
          " ",
          " We train Qwen3-1.7B under ISR $\\beta\\in\\{0.1,0.3\\}$ and Random $\\beta{=}0.1$ (single seed, 500 steps)."
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

_source line 55_

<details open><summary>🔧 Tool call — Edit · `toolu_01WTQdbjU6QvKwpMmZfzB7Qu`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
  "old_string": "($97{\\pm}2\\%$, three seeds)",
  "new_string": "($97{\\pm}2\\%$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "fd7d65ca-1545-470a-aeb6-b45a3fe5d227",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mtiffdGdpr9JACz7uBpyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 64611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 902
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

_source line 56 · 2026-05-17T17:38:58.509Z_

<details><summary>↩ Tool result · `toolu_01WTQdbjU6QvKwpMmZfzB7Qu`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "34d36cb7-9666-4925-a8d5-f21be4801890",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
    "oldString": "($97{\\pm}2\\%$, three seeds)",
    "newString": "($97{\\pm}2\\%$)",
    "originalFile": "\\begin{abstract}\nGRPO-trained formalizers converge to high prove rates on FOLIO ($97{\\pm}2\\%$, three seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.\nWe propose \\emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\\% non-hacking on identical data, suggesting the failure is RL-specific.\nRepurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.\nAcross 6 conditions, 2 logic types, and 2 model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\begin{abstract}",
          "-GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\\pm}2\\%$, three seeds) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.",
          "+GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\\pm}2\\%$) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.",
          " We propose \\emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\\% non-hacking on identical data, suggesting the failure is RL-specific.",
          " Repurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.",
          " Across 6 conditions, 2 logic types, and 2 model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}"
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

_source line 57_

<details open><summary>🔧 Tool call — Edit · `toolu_01KsxAxmC1pdnr4dGgyA7h3H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
  "old_string": "Across 6 conditions, 2 logic types, and 2 model scales",
  "new_string": "Across multiple reward conditions, logic types, and model scales"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "473e3987-e3b7-4b89-af9d-7666788f6135",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mtiffdGdpr9JACz7uBpyp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 64611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 902
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

_source line 58 · 2026-05-17T17:39:00.111Z_

<details><summary>↩ Tool result · `toolu_01KsxAxmC1pdnr4dGgyA7h3H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "8342f461-f35b-46b9-b1fd-21840e2e7f41",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex",
    "oldString": "Across 6 conditions, 2 logic types, and 2 model scales",
    "newString": "Across multiple reward conditions, logic types, and model scales",
    "originalFile": "\\begin{abstract}\nGRPO-trained formalizers converge to high prove rates on FOLIO ($97{\\pm}2\\%$) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.\nWe propose \\emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\\% non-hacking on identical data, suggesting the failure is RL-specific.\nRepurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.\nAcross 6 conditions, 2 logic types, and 2 model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 5,
        "newStart": 2,
        "newLines": 5,
        "lines": [
          " GRPO-trained formalizers converge to high prove rates on FOLIO ($97{\\pm}2\\%$) yet produce effectively zero structurally sound outputs at convergence, a failure invisible to execution-based evaluation.",
          " We propose \\emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs whose derived metric, Irreducible Solver Rate (ISR), exposes a 99.5\\% structural collapse hidden behind rising prove rates; a supervised baseline achieves 92\\% non-hacking on identical data, suggesting the failure is RL-specific.",
          " Repurposed as a reward signal, ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): tautological proofs receive artificially high ISR by construction, and the transient genuine window at moderate doses shows suggestive but non-robust improvement over random controls that disappears under extended training.",
          "-Across 6 conditions, 2 logic types, and 2 model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}",
          "+Across multiple reward conditions, logic types, and model scales, we catalog nine hacking modes and document that ISR is reliable as a diagnostic but unreliable as an optimization target.\\footnote{Code and data: \\url{[anonymized]}}",
          " \\end{abstract}"
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

_source line 59_

**Change 9**: Merge introduction paragraphs. Let me re-read it to see the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "479b70a4-69e2-4a41-bcc1-9117645449c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S44Fd7gYGoUEkkVTrSbKzk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 65513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 894
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

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01ESfWZZhYpm62dw1rnkphCa`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "4609429b-63ba-41b2-9999-3cd12d2b67b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S44Fd7gYGoUEkkVTrSbKzk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 65513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 894
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

_source line 61 · 2026-05-17T17:39:04.565Z_

<details><summary>↩ Tool result · `toolu_01ESfWZZhYpm62dw1rnkphCa`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	GRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\pm}2\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.
5	Each seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.
6	
7	\paragraph{The execution-only blind spot.}
8	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
9	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
11	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
12	
13	\paragraph{Component necessity testing.}
14	We address this gap with \emph{Solver Trace Ablation} (STA), which applies \emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\ref{fig:sta-overview}).
15	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Irreducible Solver Rate} (ISR), with $\text{ISR}{=}1$ indicating full necessity and $\text{ISR}{=}0$ complete redundancy.
16	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
17	ISR captures structural rather than semantic integrity (downstream NLI: $\rho{=}{-}0.049$, $p{=}0.187$).
18	
19	\paragraph{ISR as diagnostic.}
20	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\text{ISR}^{*}{:}\,0.642\to 0.132\to 0.003$ over 100--1000 steps (seed~42; 99.5\% degradation) while PR rises $32\%{\to}96\%$.
21	Three seeds diverge radically (PR $\sigma{=}47$\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.
22	An SFT baseline on identical data reaches $\text{PR}{=}13.0\%$ with 92.3\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven.
23	
24	\paragraph{ISR as reward: Goodhart collapse at all tested doses.}
25	Repurposed as a training signal, $r = r_{\text{exec}} \cdot (1 + \beta\,\text{ISR})$, ISR contains an inherent structural vulnerability: tautological proofs (a single premise identical to the conclusion) receive $\text{ISR}{\geq}0.5$ by construction, and implication tautologies ($P{\to}P$) receive $\text{ISR}{=}0.75$, creating a positive feedback loop once sampled during GRPO rollouts~\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.
26	Goodhart collapse~\citep{manheim-goodhart-taxonomy} is observed at all four tested doses (trajectory-confirmed at $\beta{=}0.1$): $\beta$ controls \emph{when} collapse occurs, not \emph{whether}.
27	At moderate doses, collapse is stochastic and delayed: seeds bifurcate between rapid convergence to tautology and a transient genuine window that closes under extended training.
28	Snapshot evaluation would overestimate ISR's benefit; trajectory analysis confirms the window is temporary.
29	The effect transfers to Prolog (3/3 seeds yield 0\% non-hacking via distinct mechanisms, including \emph{query-as-fact gaming}) and is preliminarily observed at 1.7B scale (qualitatively novel gaming modes in single-seed evaluation).
30	ISR's asymmetry is the central finding: \emph{reliable as observer, unreliable as optimizer at any dose.}
31	
32	\paragraph{Contributions.}
33	Across 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, and up to 1000 steps, we contribute: (\textbf{C1}) We empirically demonstrate ISR as a diagnostic for GRPO reward hacking, revealing a 99.5\% collapse trajectory invisible to PR, with an SFT control consistent with RL-specific failure (\S\ref{sec:diagnostic}); (\textbf{C2}) an empirical instance of Goodhart collapse~\citep{manheim-goodhart-taxonomy} at all four tested doses: ISR's structural bias ($\text{ISR}{\geq}0.5$ for tautological proofs) creates a positive feedback loop; the genuine window at moderate $\beta$ is suggestive but non-robust, and $\beta$ controls only timing, not outcome (\S\ref{sec:goodhart}); (\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\S\ref{sec:crosslogic}); (\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \emph{ex falso} mode, motivating functional cross-validation of diagnostics (\S\ref{sec:taxonomy}).
34	These are cautionary results: snapshot evaluation of structural rewards can overestimate their benefit; only trajectory analysis reveals the transient nature of apparent improvement.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "a3e1c27f-ab6a-4373-b5c3-3e04d5b84ad3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nGRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\\pm}2\\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.\nEach seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.\n\n\\paragraph{The execution-only blind spot.}\nProve rate, the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), which applies \\emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Irreducible Solver Rate} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (seed~42; 99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven.\n\n\\paragraph{ISR as reward: Goodhart collapse at all tested doses.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR contains an inherent structural vulnerability: tautological proofs (a single premise identical to the conclusion) receive $\\text{ISR}{\\geq}0.5$ by construction, and implication tautologies ($P{\\to}P$) receive $\\text{ISR}{=}0.75$, creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\nGoodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): $\\beta$ controls \\emph{when} collapse occurs, not \\emph{whether}.\nAt moderate doses, collapse is stochastic and delayed: seeds bifurcate between rapid convergence to tautology and a transient genuine window that closes under extended training.\nSnapshot evaluation would overestimate ISR's benefit; trajectory analysis confirms the window is temporary.\nThe effect transfers to Prolog (3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming}) and is preliminarily observed at 1.7B scale (qualitatively novel gaming modes in single-seed evaluation).\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer at any dose.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, and up to 1000 steps, we contribute: (\\textbf{C1}) We empirically demonstrate ISR as a diagnostic for GRPO reward hacking, revealing a 99.5\\% collapse trajectory invisible to PR, with an SFT control consistent with RL-specific failure (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) an empirical instance of Goodhart collapse~\\citep{manheim-goodhart-taxonomy} at all four tested doses: ISR's structural bias ($\\text{ISR}{\\geq}0.5$ for tautological proofs) creates a positive feedback loop; the genuine window at moderate $\\beta$ is suggestive but non-robust, and $\\beta$ controls only timing, not outcome (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \\emph{ex falso} mode, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results: snapshot evaluation of structural rewards can overestimate their benefit; only trajectory analysis reveals the transient nature of apparent improvement.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Current paragraph structure:
1. `\paragraph{The execution-only blind spot.}` (L7) - keep
2. `\paragraph{Component necessity testing.}` (L13) - merge into "Solver Trace Ablation"
3. `\paragraph{ISR as diagnostic.}` (L19) - merge into "Solver Trace Ablation"
4. `\paragraph{ISR as reward: Goodhart collapse at all tested doses.}` (L24) - rename to `\paragraph{ISR as reward.}`


5. `\paragraph{Contributions.}` (L32) - keep

Target structure:
1. `\paragraph{The execution-only blind spot.}` - keep unchanged
2. `\paragraph{Solver Trace Ablation.}` - merge ¶2 + ¶3 content
3. `\paragraph{ISR as reward.}` - keep ¶4 content, change title
4. `\paragraph{Contributions.}` - keep unchanged

So I need to:
- Replace `\paragraph{Component necessity testing.}` with `\paragraph{Solver Trace Ablation.}`
- Remove `\paragraph{ISR as diagnostic.}` line (keep its content merged in)
- Rename `\paragraph{ISR as reward: Goodhart collapse at all tested doses.}` to `\paragraph{ISR as reward.}`
- Keep the Contributions section as-is
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "81cfcc3c-5e44-48a0-9d19-e703839bdabe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJR2FJowXCmhtUKFi8g5CZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 66407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1787
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

_source line 63_

Now I need to merge paragraphs 2 and 3, and rename paragraph 4. The changes are:
1. Replace `\paragraph{Component necessity testing.}` with `\paragraph{Solver Trace Ablation.}`
2. Remove the `\paragraph{ISR as diagnostic.}` line
3. Rename `\paragraph{ISR as reward: Goodhart collapse at all tested doses.}` to `\paragraph{ISR as reward.}`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "ca49b332-eadb-46ab-9a09-246811f3bfcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJR2FJowXCmhtUKFi8g5CZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 66407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1787
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

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_012RNsTC7PsAAphxuaciEmLe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "old_string": "\\paragraph{Component necessity testing.}",
  "new_string": "\\paragraph{Solver Trace Ablation.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "4cde2430-5466-47c9-a76b-ca2cc70d786a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJR2FJowXCmhtUKFi8g5CZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 66407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1787
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

_source line 65 · 2026-05-17T17:39:16.605Z_

<details><summary>↩ Tool result · `toolu_012RNsTC7PsAAphxuaciEmLe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "5c7340d9-f41e-4ca4-a2e3-26bcf7330083",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
    "oldString": "\\paragraph{Component necessity testing.}",
    "newString": "\\paragraph{Solver Trace Ablation.}",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nGRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\\pm}2\\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.\nEach seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.\n\n\\paragraph{The execution-only blind spot.}\nProve rate, the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Component necessity testing.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), which applies \\emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Irreducible Solver Rate} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (seed~42; 99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven.\n\n\\paragraph{ISR as reward: Goodhart collapse at all tested doses.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR contains an inherent structural vulnerability: tautological proofs (a single premise identical to the conclusion) receive $\\text{ISR}{\\geq}0.5$ by construction, and implication tautologies ($P{\\to}P$) receive $\\text{ISR}{=}0.75$, creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\nGoodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): $\\beta$ controls \\emph{when} collapse occurs, not \\emph{whether}.\nAt moderate doses, collapse is stochastic and delayed: seeds bifurcate between rapid convergence to tautology and a transient genuine window that closes under extended training.\nSnapshot evaluation would overestimate ISR's benefit; trajectory analysis confirms the window is temporary.\nThe effect transfers to Prolog (3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming}) and is preliminarily observed at 1.7B scale (qualitatively novel gaming modes in single-seed evaluation).\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer at any dose.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, and up to 1000 steps, we contribute: (\\textbf{C1}) We empirically demonstrate ISR as a diagnostic for GRPO reward hacking, revealing a 99.5\\% collapse trajectory invisible to PR, with an SFT control consistent with RL-specific failure (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) an empirical instance of Goodhart collapse~\\citep{manheim-goodhart-taxonomy} at all four tested doses: ISR's structural bias ($\\text{ISR}{\\geq}0.5$ for tautological proofs) creates a positive feedback loop; the genuine window at moderate $\\beta$ is suggestive but non-robust, and $\\beta$ controls only timing, not outcome (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \\emph{ex falso} mode, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results: snapshot evaluation of structural rewards can overestimate their benefit; only trajectory analysis reveals the transient nature of apparent improvement.\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " Process reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.",
          " A separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.",
          " ",
          "-\\paragraph{Component necessity testing.}",
          "+\\paragraph{Solver Trace Ablation.}",
          " We address this gap with \\emph{Solver Trace Ablation} (STA), which applies \\emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\\ref{fig:sta-overview}).",
          " For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Irreducible Solver Rate} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.",
          " LOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces."
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

_source line 66_

<details open><summary>🔧 Tool call — Edit · `toolu_01UwoKDW7M92KgFzyhgsC5tY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "old_string": "ISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic",
  "new_string": "ISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\nAs a post-hoc diagnostic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "35f604c1-a0e0-4144-9b37-4b9c883b5500",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJR2FJowXCmhtUKFi8g5CZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 66407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1787
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

_source line 67 · 2026-05-17T17:39:16.953Z_

<details><summary>↩ Tool result · `toolu_01UwoKDW7M92KgFzyhgsC5tY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "3f044784-0ae3-4b04-81c2-c0d98ca6e817",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
    "oldString": "ISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic",
    "newString": "ISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\nAs a post-hoc diagnostic",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nGRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\\pm}2\\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.\nEach seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.\n\n\\paragraph{The execution-only blind spot.}\nProve rate, the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Solver Trace Ablation.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), which applies \\emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Irreducible Solver Rate} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\n\n\\paragraph{ISR as diagnostic.}\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (seed~42; 99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven.\n\n\\paragraph{ISR as reward: Goodhart collapse at all tested doses.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR contains an inherent structural vulnerability: tautological proofs (a single premise identical to the conclusion) receive $\\text{ISR}{\\geq}0.5$ by construction, and implication tautologies ($P{\\to}P$) receive $\\text{ISR}{=}0.75$, creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\nGoodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): $\\beta$ controls \\emph{when} collapse occurs, not \\emph{whether}.\nAt moderate doses, collapse is stochastic and delayed: seeds bifurcate between rapid convergence to tautology and a transient genuine window that closes under extended training.\nSnapshot evaluation would overestimate ISR's benefit; trajectory analysis confirms the window is temporary.\nThe effect transfers to Prolog (3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming}) and is preliminarily observed at 1.7B scale (qualitatively novel gaming modes in single-seed evaluation).\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer at any dose.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, and up to 1000 steps, we contribute: (\\textbf{C1}) We empirically demonstrate ISR as a diagnostic for GRPO reward hacking, revealing a 99.5\\% collapse trajectory invisible to PR, with an SFT control consistent with RL-specific failure (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) an empirical instance of Goodhart collapse~\\citep{manheim-goodhart-taxonomy} at all four tested doses: ISR's structural bias ($\\text{ISR}{\\geq}0.5$ for tautological proofs) creates a positive feedback loop; the genuine window at moderate $\\beta$ is suggestive but non-robust, and $\\beta$ controls only timing, not outcome (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \\emph{ex falso} mode, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results: snapshot evaluation of structural rewards can overestimate their benefit; only trajectory analysis reveals the transient nature of apparent improvement.\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 8,
        "newStart": 15,
        "newLines": 6,
        "lines": [
          " For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Irreducible Solver Rate} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.",
          " LOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.",
          " ISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).",
          "-",
          "-\\paragraph{ISR as diagnostic.}",
          " As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (seed~42; 99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.",
          " Three seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.",
          " An SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven."
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

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_01PuXFR53CWKf3MdX9ynDJSC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "old_string": "\\paragraph{ISR as reward: Goodhart collapse at all tested doses.}",
  "new_string": "\\paragraph{ISR as reward.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "bd023f6c-cd91-4222-b97f-b5481bdf7106",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJR2FJowXCmhtUKFi8g5CZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 66407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1787
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

_source line 69 · 2026-05-17T17:39:18.196Z_

<details><summary>↩ Tool result · `toolu_01PuXFR53CWKf3MdX9ynDJSC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "001defbc-cf4d-4e51-8828-5fa3d4658251",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
    "oldString": "\\paragraph{ISR as reward: Goodhart collapse at all tested doses.}",
    "newString": "\\paragraph{ISR as reward.}",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nGRPO-trained formalizers converge to high prove rates on first-order logic problems ($97{\\pm}2\\%$ across three seeds, 1000 steps), yet at convergence produce effectively zero structurally sound outputs.\nEach seed develops a distinct degenerate shortcut: conclusion embedding, repetition collapse, or tautological collapse, all invisible to execution-based evaluation, which registers success regardless of whether the proof reflects genuine derivation.\n\n\\paragraph{The execution-only blind spot.}\nProve rate, the dominant evaluation metric for neurosymbolic formalizers~\\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\\citep{skalse-reward-hacking, reward-hacking-survey}.\nRecent work applies GRPO~\\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.\nProcess reward models~\\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.\nA separate line of work documents that LLMs already game logical formalization at inference time~\\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \\emph{diagnostic} for structural integrity in neurosymbolic outputs.\n\n\\paragraph{Solver Trace Ablation.}\nWe address this gap with \\emph{Solver Trace Ablation} (STA), which applies \\emph{component necessity testing} (leave-one-out (LOO) ablation on solver inputs) to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Irreducible Solver Rate} (ISR), with $\\text{ISR}{=}1$ indicating full necessity and $\\text{ISR}{=}0$ complete redundancy.\nLOO ablation itself is standard~\\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.\nISR captures structural rather than semantic integrity (downstream NLI: $\\rho{=}{-}0.049$, $p{=}0.187$).\nAs a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\\citep{folio}, ISR reveals a structural collapse trajectory invisible to PR: $\\text{ISR}^{*}{:}\\,0.642\\to 0.132\\to 0.003$ over 100--1000 steps (seed~42; 99.5\\% degradation) while PR rises $32\\%{\\to}96\\%$.\nThree seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.\nAn SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven.\n\n\\paragraph{ISR as reward: Goodhart collapse at all tested doses.}\nRepurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR contains an inherent structural vulnerability: tautological proofs (a single premise identical to the conclusion) receive $\\text{ISR}{\\geq}0.5$ by construction, and implication tautologies ($P{\\to}P$) receive $\\text{ISR}{=}0.75$, creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.\nGoodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): $\\beta$ controls \\emph{when} collapse occurs, not \\emph{whether}.\nAt moderate doses, collapse is stochastic and delayed: seeds bifurcate between rapid convergence to tautology and a transient genuine window that closes under extended training.\nSnapshot evaluation would overestimate ISR's benefit; trajectory analysis confirms the window is temporary.\nThe effect transfers to Prolog (3/3 seeds yield 0\\% non-hacking via distinct mechanisms, including \\emph{query-as-fact gaming}) and is preliminarily observed at 1.7B scale (qualitatively novel gaming modes in single-seed evaluation).\nISR's asymmetry is the central finding: \\emph{reliable as observer, unreliable as optimizer at any dose.}\n\n\\paragraph{Contributions.}\nAcross 6 reward conditions, 5 seeds, 2 logic types, 2 model scales, and up to 1000 steps, we contribute: (\\textbf{C1}) We empirically demonstrate ISR as a diagnostic for GRPO reward hacking, revealing a 99.5\\% collapse trajectory invisible to PR, with an SFT control consistent with RL-specific failure (\\S\\ref{sec:diagnostic}); (\\textbf{C2}) an empirical instance of Goodhart collapse~\\citep{manheim-goodhart-taxonomy} at all four tested doses: ISR's structural bias ($\\text{ISR}{\\geq}0.5$ for tautological proofs) creates a positive feedback loop; the genuine window at moderate $\\beta$ is suggestive but non-robust, and $\\beta$ controls only timing, not outcome (\\S\\ref{sec:goodhart}); (\\textbf{C3}) cross-logic transfer to Prolog with consistent Goodhart effects across all seeds (\\S\\ref{sec:crosslogic}); (\\textbf{C4}) a nine-mode hacking taxonomy including query-as-fact gaming, obfuscated tautology, and a scale-specific \\emph{ex falso} mode, motivating functional cross-validation of diagnostics (\\S\\ref{sec:taxonomy}).\nThese are cautionary results: snapshot evaluation of structural rewards can overestimate their benefit; only trajectory analysis reveals the transient nature of apparent improvement.\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " Three seeds diverge radically (PR $\\sigma{=}47$\\,pp), each converging to a qualitatively different mode: conclusion embedding, repetition collapse, and tautological collapse.",
          " An SFT baseline on identical data reaches $\\text{PR}{=}13.0\\%$ with 92.3\\% non-hacking (3-seed pooled, 1000 steps), consistent with the failure being RL-specific rather than data- or capacity-driven.",
          " ",
          "-\\paragraph{ISR as reward: Goodhart collapse at all tested doses.}",
          "+\\paragraph{ISR as reward.}",
          " Repurposed as a training signal, $r = r_{\\text{exec}} \\cdot (1 + \\beta\\,\\text{ISR})$, ISR contains an inherent structural vulnerability: tautological proofs (a single premise identical to the conclusion) receive $\\text{ISR}{\\geq}0.5$ by construction, and implication tautologies ($P{\\to}P$) receive $\\text{ISR}{=}0.75$, creating a positive feedback loop once sampled during GRPO rollouts~\\citep{karwowski-goodhart-rl, kwa-catastrophic-goodhart}.",
          " Goodhart collapse~\\citep{manheim-goodhart-taxonomy} is observed at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$): $\\beta$ controls \\emph{when} collapse occurs, not \\emph{whether}.",
          " At moderate doses, collapse is stochastic and delayed: seeds bifurcate between rapid convergence to tautology and a transient genuine window that closes under extended training."
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

_source line 70_

Now **Change 10**: Add Goodhart 1975 reference and cite it. Let me find where "Goodhart's Law" is first mentioned in related_work.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "5ca8d5d3-e906-46f7-9ebc-1c245fee2d0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFScK1eLV4y4w3xipPSPLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 68194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
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

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_01F4E6T5dC19WGWJwMLBhWdE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "offset": 0,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "4d07122c-77cc-4acc-bcd1-269c36d71c5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFScK1eLV4y4w3xipPSPLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 68194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
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

_source line 72 · 2026-05-17T17:39:23.280Z_

<details><summary>↩ Tool result · `toolu_01F4E6T5dC19WGWJwMLBhWdE`</summary>

```text
0	% ============================================================
1	% Category 1: Neurosymbolic reasoning + RL/GRPO
2	% ============================================================
3	
4	@article{deepseekmath,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "800e4594-5cd5-4d0d-9e0b-13cbdcd46997",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,",
      "numLines": 5,
      "startLine": 0,
      "totalLines": 376
    }
  }
}
```

</details>

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_015pbCghVrJL8SwpQi4hjkD8`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "description": "Count lines in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "7281302c-0a83-4162-bd15-2fe4a32d7750",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjFktZ3SFEv7mC2SoSB6ya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 69478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 74 · 2026-05-17T17:39:28.072Z_

<details><summary>↩ Tool result · `toolu_015pbCghVrJL8SwpQi4hjkD8`</summary>

```text
375 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "51afa315-60e5-4f88-b97f-d66b28e186ef",
  "tool_use_result": {
    "stdout": "375 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
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

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_01BR9iJDuS3tEhHt6AvGhPqL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "offset": 370,
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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "8d4b1704-c018-4a76-8bd3-2c79dbdd21bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B4UqhJY4M6THX2HsGLnBd8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 162,
      "cache_read_input_tokens": 69701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 162
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

_source line 76 · 2026-05-17T17:39:34.723Z_

<details><summary>↩ Tool result · `toolu_01BR9iJDuS3tEhHt6AvGhPqL`</summary>

```text
370	@article{deepseek-r1-2025,
371	  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},
372	  author={{DeepSeek-AI}},
373	  journal={arXiv preprint arXiv:2501.12948},
374	  year={2025}
375	}
376	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "3e93a9d7-6677-4f49-9767-b7a7a7f2a131",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "@article{deepseek-r1-2025,\n  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025}\n}\n",
      "numLines": 7,
      "startLine": 370,
      "totalLines": 376
    }
  }
}
```

</details>

---

### Assistant

_source line 77_

Now add the Goodhart 1975 entry at the end of references.bib, and add the citation in related_work.tex where "Goodhart's Law" first appears (L14).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "9ffe4e2b-b5ca-4f59-8008-4fc36b9f1f36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8xE5sUtSh6saoPAJGGbrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 69863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_01RTCo1GijKAswZnA8SW8SGT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "old_string": "@article{deepseek-r1-2025,\n  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025}\n}",
  "new_string": "@article{deepseek-r1-2025,\n  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025}\n}\n\n@incollection{goodhart-1975,\n  author       = {Charles A. E. Goodhart},\n  title        = {{Problems of Monetary Management: The U.K. Experience}},\n  booktitle    = {Monetary Theory and Practice: The U.K. Experience},\n  publisher    = {Macmillan},\n  year         = {1975},\n  pages        = {91--121},\n  address      = {London},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "9209ef08-bcb2-4061-b422-c4ad60895798",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8xE5sUtSh6saoPAJGGbrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 69863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 79 · 2026-05-17T17:39:47.670Z_

<details><summary>↩ Tool result · `toolu_01RTCo1GijKAswZnA8SW8SGT`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "83b5ab6f-1707-4bdb-b09d-239cb7d110f6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
    "oldString": "@article{deepseek-r1-2025,\n  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025}\n}",
    "newString": "@article{deepseek-r1-2025,\n  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025}\n}\n\n@incollection{goodhart-1975,\n  author       = {Charles A. E. Goodhart},\n  title        = {{Problems of Monetary Management: The U.K. Experience}},\n  booktitle    = {Monetary Theory and Practice: The U.K. Experience},\n  publisher    = {Macmillan},\n  year         = {1975},\n  pages        = {91--121},\n  address      = {London},\n}",
    "originalFile": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2025},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n@article{khalifa2025thinkprm,\n  author       = {Muhammad Khalifa and Rishabh Agarwal and Lajanugen Logeswaran and Jaekyeom Kim and Hao Peng and Moontae Lee and Honglak Lee and Lu Wang},\n  title        = {{Process Reward Models That Think}},\n  journal      = {arXiv preprint arXiv:2504.16828},\n  year         = {2025},\n  eprint       = {2504.16828},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@inproceedings{zeng2025versaprm,\n  author       = {Thomas Zeng and Shuibai Zhang and Shutong Wu and Christian Classen and Daewon Chae and Ethan Ewer and Minjae Lee and Heeju Kim and Wonjun Kang and Jackson Kunde and Ying Fan and Jungtaek Kim and Hyung Il Koo and Kannan Ramchandran and Dimitris Papailiopoulos and Kangwook Lee},\n  title        = {{VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2025},\n  note         = {arXiv:2502.06737},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--41},\n  year         = {1978},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@article{spurious-rewards,\n  author       = {Rulin Shao and Shuyue Stella Li and Rui Xin and Scott Geng and Yiping Wang and Sewoong Oh and Simon Shaolei Du and Nathan Lambert and Sewon Min and Ranjay Krishna and Yulia Tsvetkov and Hannaneh Hajishirzi and Pang Wei Koh and Luke Zettlemoyer},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and Hailey Schoelkopf and Yilun Zhao and Zhenting Qi and Martin Riddell and Luke Benson and Lucy Sun and Ekaterina Zubova and Yujie Qiao and Matthew Burtell and David Peng and Jonathan Fan and Yixin Liu and Brian Wong and Malcolm Sailor and Ansong Ni and Linyong Nan and Jungo Kasai and Tao Yu and Rui Zhang and Shafiq Joty and Alexander R. Fabbri and Wojciech Kryscinski and Xi Victoria Lin and Caiming Xiong and Dragomir Radev},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Yang Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and Cedegao E. Zhang and Armando Solar-Lezama and Joshua B. Tenenbaum and Roger Levy},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {Zhengkun Di and Chaoli Zhang and Hongtao Lv and Lizhen Cui and Lei Liu},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and Runxin Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Reward shaping and process supervision\n% ============================================================\n\n@article{rlsf,\n  author       = {Piyush Jha and Prithwish Jana and Pranavkrishna Suresh and Arnav Arora and Vijay Ganesh},\n  title        = {{RLSF: Reinforcement Learning via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rubric-grpo,\n  author       = {Manish Bhattarai and Ismael Boureima and Nishath Rajiv Ranasinghe and Scott Pakin and Dan O'Malley},\n  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},\n  journal      = {arXiv preprint arXiv:2605.08061},\n  year         = {2026},\n  eprint       = {2605.08061},\n  archivePrefix = {arXiv},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Thomas Kwa and Drake Thomas and Adri\\`{a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n  note         = {arXiv:2407.14503},\n}\n\n@article{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  journal      = {arXiv preprint arXiv:2408.08152},\n  year         = {2024},\n  eprint       = {2408.08152},\n  archivePrefix = {arXiv},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@article{reward-hacking-survey,\n  author       = {Xiaohua Wang and Muzhao Tian and Yuqi Zeng and Zisu Huang and others},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n}\n\n@misc{metr-reward-hacking,\n  author       = {{METR}},\n  title        = {{Recent Frontier Models Are Reward Hacking}},\n  year         = {2025},\n  howpublished = {METR blog post},\n  note         = {\\url{https://metr.org/blog/2025-06-05-recent-reward-hacking/}},\n}\n\n\n@article{shapley-1953,\n  author       = {Lloyd S. Shapley},\n  title        = {{A Value for n-Person Games}},\n  journal      = {Contributions to the Theory of Games},\n  volume       = {2},\n  pages        = {307--317},\n  year         = {1953},\n  publisher    = {Princeton University Press},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2021},\n  note         = {arXiv:2012.13048},\n}\n\n@article{qwen3,\n  author       = {{Qwen Team}},\n  title        = {{Qwen3 Technical Report}},\n  journal      = {arXiv preprint arXiv:2505.09388},\n  year         = {2025},\n  eprint       = {2505.09388},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.CL},\n}\n\n@inproceedings{processbench,\n  author       = {Chujie Zheng and Zhenru Zhang and Beichen Zhang and Runji Lin and Keming Lu and Bowen Yu and Dayiheng Liu and Jingren Zhou and Junyang Lin},\n  title        = {{ProcessBench: Identifying Process Errors in Mathematical Reasoning}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2412.06559},\n}\n\n@misc{krakovna2020specification,\n  author       = {Victoria Krakovna and Jonathan Uesato and Vladimir Mikulik and Matthew Rahtz and Tom Everitt and Ramana Kumar and Zac Kenton and Jan Leike and Shane Legg},\n  title        = {Specification gaming: the flip side of {AI} ingenuity},\n  year         = {2020},\n  howpublished = {DeepMind Blog},\n  url          = {https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/},\n}\n\n@article{polu2020generative,\n  author       = {Stanislas Polu and Ilya Sutskever},\n  title        = {{Generative Language Modeling for Automated Theorem Proving}},\n  journal      = {arXiv preprint arXiv:2009.03393},\n  year         = {2020},\n  eprint       = {2009.03393},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.LG},\n}\n\n@article{everitt2021reward,\n  author       = {Tom Everitt and Marcus Hutter and Ramana Kumar and Victoria Krakovna},\n  title        = {{Reward Tampering Problems and Solutions in Reinforcement Learning: A Causal Influence Diagram Perspective}},\n  journal      = {Synthese},\n  volume       = {198},\n  number       = {27},\n  pages        = {6435--6467},\n  year         = {2021},\n  doi          = {10.1007/s11229-021-03141-4},\n}\n\n@inproceedings{pan-reward-misspecification,\n  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},\n  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},\n  booktitle    = {International Conference on Learning Representations (ICLR)},\n  year         = {2022},\n  note         = {arXiv:2201.03544},\n}\n\n@article{amodei2016concrete,\n  title={Concrete Problems in {AI} Safety},\n  author={Amodei, Dario and Olah, Chris and Steinhardt, Jacob and Christiano, Paul and Schulman, John and Man{\\'e}, Dan},\n  journal={arXiv preprint arXiv:1606.06565},\n  year={2016}\n}\n\n@article{geirhos2020shortcut,\n  title={Shortcut Learning in Deep Neural Networks},\n  author={Geirhos, Robert and Jacobsen, J{\\\"o}rn-Henrik and Michaelis, Claudio and Zemel, Richard and Brendel, Wieland and Bethge, Matthias and Wichmann, Felix A.},\n  journal={Nature Machine Intelligence},\n  volume={2},\n  number={11},\n  pages={665--673},\n  year={2020}\n}\n\n@article{deepseek-r1-2025,\n  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 373,
        "oldLines": 3,
        "newStart": 373,
        "newLines": 13,
        "lines": [
          "   journal={arXiv preprint arXiv:2501.12948},",
          "   year={2025}",
          " }",
          "+",
          "+@incollection{goodhart-1975,",
          "+  author       = {Charles A. E. Goodhart},",
          "+  title        = {{Problems of Monetary Management: The U.K. Experience}},",
          "+  booktitle    = {Monetary Theory and Practice: The U.K. Experience},",
          "+  publisher    = {Macmillan},",
          "+  year         = {1975},",
          "+  pages        = {91--121},",
          "+  address      = {London},",
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

_source line 80_

<details open><summary>🔧 Tool call — Edit · `toolu_01KUfzcreZ6ib275ebmNSXjf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "old_string": "\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward}",
  "new_string": "\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law~\\citep{goodhart-1975} is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "188133f7-ac1f-4622-89b2-4c97e8c04756",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8xE5sUtSh6saoPAJGGbrd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 69863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
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

_source line 81 · 2026-05-17T17:39:48.700Z_

<details><summary>↩ Tool result · `toolu_01KUfzcreZ6ib275ebmNSXjf`</summary>

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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "36fa06b5-5136-4ef4-b3cf-a886917e6e5b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "oldString": "\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward}",
    "newString": "\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law~\\citep{goodhart-1975} is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward}",
    "originalFile": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic reasoning.}\nLLM-solver pipelines~\\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\\citep{polu2020generative, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1-2025} evaluate execution accuracy alone, with no diagnostic for structural quality.\nWe use FOLIO~\\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.\n\n\\paragraph{Process rewards and reward shaping.}\nLearned PRMs~\\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\\citep{processbench}; recent work extends PRMs to multi-domain settings~\\citep{zeng2025versaprm} and process-level reasoning~\\citep{khalifa2025thinkprm}. \\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \\emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.\nSymbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\nRubric-grounded GRPO~\\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.\nThe shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.\n\n\\paragraph{Reward hacking and Goodhart's Law.}\nGoodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empirically in RLHF and frontier models~\\citep{amodei2016concrete, krakovna2020specification, gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.\nRecent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards} and reward hacking in frontier models~\\citep{metr-reward-hacking}.\nOur setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \\emph{emerges during RL training} rather than at inference time (cf.\\ shortcut learning in supervised settings~\\citep{geirhos2020shortcut}); and the effect operates at a diagnostic level, where the metric designed to detect gaming becomes gamed when optimized.\n\\citet{pan-reward-misspecification} show that more capable agents exploit reward misspecifications more severely; our cross-scale comparison (4B vs.\\ 1.7B) complements this finding by demonstrating that different capacities discover qualitatively different exploits under identical reward formulations.\nWe frame our results as an empirical instance (primarily regressional, with extremal elements) of Goodhart's Law within the \\citet{manheim-goodhart-taxonomy} taxonomy: ISR's LOO definition creates an inherent structural bias toward tautology ($P{\\to}P$ receives $\\text{ISR}{=}0.75$ by construction), with collapse observed at all four tested doses.\n\n\\paragraph{Mutation testing.}\nSTA adapts the LOO mutation paradigm~\\citep{demillo1978, jia-harman-survey} to solver inputs; our contribution lies in the application and empirical findings, not in the perturbation primitive itself.\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 7,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          " The shared lesson across these approaches is that reward augmentation introduces proxy risk; our contribution is providing an empirical instance of this variant in the neurosymbolic setting, where the diagnostic itself becomes the optimization target.",
          " ",
          " \\paragraph{Reward hacking and Goodhart's Law.}",
          "-Goodhart's Law is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empirically in RLHF and frontier models~\\citep{amodei2016concrete, krakovna2020specification, gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.",
          "+Goodhart's Law~\\citep{goodhart-1975} is established theoretically~\\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl, everitt2021reward} and empirically in RLHF and frontier models~\\citep{amodei2016concrete, krakovna2020specification, gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.",
          " \\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.",
          " Recent work further documents spurious reward signals in RLVR~\\citep{spurious-rewards} and reward hacking in frontier models~\\citep{metr-reward-hacking}.",
          " Our setting differs in three ways: ISR is deterministic and solver-derived rather than learned; gaming \\emph{emerges during RL training} rather than at inference time (cf.\\ shortcut learning in supervised settings~\\citep{geirhos2020shortcut}); and the effect operates at a diagnostic level, where the metric designed to detect gaming becomes gamed when optimized."
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

_source line 82_

Now **Change 11**: conclusion.tex Q5 foreseeability. Let me re-read conclusion.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "05d054cd-0040-458c-a9f7-1a46c1d93b87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnKGgddjfuykaSPmZtQKTD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 70096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
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

_source line 83_

<details open><summary>🔧 Tool call — Read · `toolu_019mr8mbSviPzbfCjvRQinky`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "3745c5d6-25b7-4772-b45d-ef2bb37d0a50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnKGgddjfuykaSPmZtQKTD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 70096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
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

_source line 84 · 2026-05-17T17:39:53.555Z_

<details><summary>↩ Tool result · `toolu_019mr8mbSviPzbfCjvRQinky`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation (\S\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\beta{=}0.1$; \S\ref{sec:goodhart}--\ref{sec:crossscale}).
5	At 500 steps, ISR seeds descriptively sustain more genuine output than random controls (3 of 5 seeds vs.\ 0 of 5); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\text{OR}{=}0.61$, n.s.).
6	Extended training confirms the window closes.
7	ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.
8	While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\S\ref{sec:goodhart}), non-monotonic dose-response across four $\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\S\ref{sec:crosslogic}).
9	These details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \emph{that} a metric will be gamed and predicting \emph{how}.
10	ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "3eba4c7d-55f1-4ff1-970c-3a0456408b80",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$; \\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\nAt 500 steps, ISR seeds descriptively sustain more genuine output than random controls (3 of 5 seeds vs.\\ 0 of 5); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.).\nExtended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\nWhile Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic dose-response across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).\nThese details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}.\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Assistant

_source line 85_

<details><summary>Logged reasoning block</summary>

````text
The instruction says:
- Find the sentence starting with `While Goodhart collapse` (L8)
- Insert before it: `ISR's tautological vulnerability ($\text{ISR}{\geq}0.5$ for single-premise proofs) is predictable from the metric definition; the empirical contribution is not the existence of collapse but the specific phenomena that resist prediction:`
- Then modify the original sentence: delete "While Goodhart collapse under LOO-based metrics is theoretically predictable, several specific phenomena resist simple prediction:" and replace with just the list.

But looking at the current text on L8, it says "While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction:" followed by the list. I need to:


1. Insert the new sentence before L8
2. Replace "While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction:" with just the list items

So the final result should be:
```
ISR's tautological vulnerability ($\text{ISR}{\geq}0.5$ for single-premise proofs) is predictable from the metric definition; the empirical contribution is not the existence of collapse but the specific phenomena that resist prediction:
stochastic bifurcation between collapse and genuine windows (\S\ref{sec:goodhart}), non-monotonic patterns across four $\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\S\ref{sec:crosslogic}).
```

I need to restructure this section by inserting a new sentence that clarifies ISR's tautological vulnerability, then stripping away the redundant framing from the original sentence and keeping just the list of phenomena that actually resist prediction. I need to replace "non-monotonic dose-response" with "non-monotonic patterns" in that list item.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "3e6794f3-def2-4df0-8302-9d766f7362d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UY25Dp5J9ypiDXd3bohsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 70963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 542
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

_source line 86_

<details open><summary>🔧 Tool call — Edit · `toolu_01Q3naU9dirwtnTrq1jtQzef`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
  "old_string": "While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic dose-response across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).\nThese details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}.",
  "new_string": "ISR's tautological vulnerability ($\\text{ISR}{\\geq}0.5$ for single-premise proofs) is predictable from the metric definition; the empirical contribution is not the existence of collapse but the specific phenomena that resist prediction:\nstochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic patterns across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).\nThese details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "70e4afd7-3ef4-48ff-9dbb-38cf331514c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UY25Dp5J9ypiDXd3bohsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 70963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 542
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

_source line 87 · 2026-05-17T17:40:09.400Z_

<details><summary>↩ Tool result · `toolu_01Q3naU9dirwtnTrq1jtQzef`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "108e4e22-03e9-40a9-b0b3-3bb8314cfe8f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex",
    "oldString": "While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic dose-response across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).\nThese details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}.",
    "newString": "ISR's tautological vulnerability ($\\text{ISR}{\\geq}0.5$ for single-premise proofs) is predictable from the metric definition; the empirical contribution is not the existence of collapse but the specific phenomena that resist prediction:\nstochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic patterns across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).\nThese details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}.",
    "originalFile": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nSTA exposes structural degeneration invisible to execution-based evaluation (\\S\\ref{sec:diagnostic}), and ISR exhibits Goodhart collapse at all four tested doses (trajectory-confirmed at $\\beta{=}0.1$; \\S\\ref{sec:goodhart}--\\ref{sec:crossscale}).\nAt 500 steps, ISR seeds descriptively sustain more genuine output than random controls (3 of 5 seeds vs.\\ 0 of 5); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.).\nExtended training confirms the window closes.\nISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.\nWhile Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic dose-response across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).\nThese details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}.\nISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 6,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " At 500 steps, ISR seeds descriptively sustain more genuine output than random controls (3 of 5 seeds vs.\\ 0 of 5); seed-level permutation tests are consistent in direction but underpowered ($p{=}0.26$, $n{=}5$), and under stricter classification the effect reverses ($\\text{OR}{=}0.61$, n.s.).",
          " Extended training confirms the window closes.",
          " ISR is reliable as a diagnostic but unreliable as an optimizer: the same LOO bias that rewards genuine necessity also rewards tautological constructions.",
          "-While Goodhart collapse under LOO-based metrics is theoretically predictable, specific phenomena resist simple prediction: stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic dose-response across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).",
          "+ISR's tautological vulnerability ($\\text{ISR}{\\geq}0.5$ for single-premise proofs) is predictable from the metric definition; the empirical contribution is not the existence of collapse but the specific phenomena that resist prediction:",
          "+stochastic bifurcation between collapse and genuine windows (\\S\\ref{sec:goodhart}), non-monotonic patterns across four $\\beta$ levels, and cross-logic mode divergence where Prolog exhibits gaming pathways absent from FOL (\\S\\ref{sec:crosslogic}).",
          " These details, combined with the sensitivity of genuine-rate estimates to classification methodology, underscore the gap between predicting \\emph{that} a metric will be gamed and predicting \\emph{how}.",
          " ISR and similar perturbation-based metrics should serve as post-hoc evaluation tools, not training signals."
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

_source line 88_

Now let me run the checks: em-dash grep, citation count in intro, and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "f15069ca-779e-4c29-a446-f1ed121776be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8bW4Lg15wQiJbhEPW2F2c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 71505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1201
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

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_014dqQDvXiJJtMASTxjnwMbu`</summary>

```json
{
  "command": "grep -c \"\\\\\\\\cite\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
  "description": "Count citations in introduction.tex after changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "f41d2225-c383-4795-9f14-d6b254141b91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8bW4Lg15wQiJbhEPW2F2c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 71505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1201
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

_source line 90 · 2026-05-17T17:40:16.313Z_

<details><summary>↩ Tool result · `toolu_014dqQDvXiJJtMASTxjnwMbu`</summary>

```text
9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "8140ce39-6f4b-49ed-9ece-30d04c438f26",
  "tool_use_result": {
    "stdout": "9",
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

_source line 91_

<details open><summary>🔧 Tool call — Grep · `toolu_01WDj6s2CNoiBfdch9QKijWb`</summary>

```json
{
  "pattern": "—",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "b2f427ba-a161-4a01-85a8-c1d6153e3fb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8bW4Lg15wQiJbhEPW2F2c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 71505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1201
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

_source line 92 · 2026-05-17T17:40:17.737Z_

<details><summary>↩ Tool result · `toolu_01WDj6s2CNoiBfdch9QKijWb`</summary>

```text
paper/appendix.tex:1:% Appendix — solver-trace-ablation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "e8a6624f-588a-4b53-b7eb-3830fe359ccd",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/appendix.tex:1:% Appendix — solver-trace-ablation",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01Bc1psfWZnvXujUiwaFT9sa`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX PDF",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "eadf08de-adbf-4e63-9c13-0e4cdcd36605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8bW4Lg15wQiJbhEPW2F2c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1201,
      "cache_read_input_tokens": 71505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1201
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

### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bhkxfg4yf",
  "tool_use_id": "toolu_01Bc1psfWZnvXujUiwaFT9sa",
  "description": "Compile LaTeX PDF",
  "task_type": "local_bash",
  "uuid": "00c7c298-1aef-4aa9-9c33-4fa73ad5e242",
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9"
}
```

---

### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bhkxfg4yf",
  "tool_use_id": "toolu_01Bc1psfWZnvXujUiwaFT9sa",
  "status": "completed",
  "output_file": "",
  "summary": "Compile LaTeX PDF",
  "uuid": "47ca777f-fe3a-4cce-abce-68e6ec93ddad",
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9"
}
```

---

### Tool result

_source line 96 · 2026-05-17T17:40:23.487Z_

<details><summary>↩ Tool result · `toolu_01Bc1psfWZnvXujUiwaFT9sa`</summary>

```text
msy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/helvetic/uhvb8a.pfb>
Output written on main.pdf (22 pages, 605066 bytes).
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
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "eb7add8d-b3e2-4593-85bf-786a14df3694",
  "tool_use_result": {
    "stdout": "msy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/helvetic/uhvb8a.pfb>\nOutput written on main.pdf (22 pages, 605066 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 97_

Citation count: 9 before, 9 after (correct, no citations lost). No em-dashes in content. PDF compiled. Let me check for undefined citations and verify page boundary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "a5052de9-07a0-4cb4-8447-7071b43f62cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TT1dg3arYfLHhheeiWz5gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 941,
      "cache_read_input_tokens": 72706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 941
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

_source line 98_

<details open><summary>🔧 Tool call — Bash · `toolu_01XYmtbCtz3uFKKQ9ce3XHFx`</summary>

```json
{
  "command": "grep -i \"undefined\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/main.log | grep -i \"citation\" | head -10",
  "description": "Check for undefined citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "7cc5b57c-f2d3-4849-b153-c37136f84277",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TT1dg3arYfLHhheeiWz5gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 941,
      "cache_read_input_tokens": 72706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 941
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

_source line 99 · 2026-05-17T17:40:29.513Z_

<details><summary>↩ Tool result · `toolu_01XYmtbCtz3uFKKQ9ce3XHFx`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "a16a5dc5-fe54-4cf4-9f78-e296dece7a47",
  "tool_use_result": {
    "stdout": "",
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

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_01KWykHv8A3AsGPHtRiJyKA3`</summary>

```json
{
  "command": "pdftotext main.pdf - 2>/dev/null | head -n 500 | grep -n \"^$\" | tail -20; echo \"---\"; pdftotext -layout main.pdf - 2>/dev/null | grep -n \"^\\f\" | head -10",
  "description": "Check page boundaries in PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "54d90f4c-fe57-4c05-aae6-6495402b22a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TT1dg3arYfLHhheeiWz5gf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 941,
      "cache_read_input_tokens": 72706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 941
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

_source line 101 · 2026-05-17T17:40:31.848Z_

<details><summary>↩ Tool result · `toolu_01KWykHv8A3AsGPHtRiJyKA3`</summary>

```text
269:
280:
331:
336:
376:
383:
387:
402:
428:
431:
433:
435:
438:
454:
456:
458:
472:
478:
480:
499:
---
1418:from Table 1. PR = prove rate, ISR∗ = proved-only ISR, H7/H1/N-H = percentage among proved
1423:formal text-match taxonomy not run on this checkpoint.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "3f2fe312-88ee-4bbb-95b8-6bd32e542ae4",
  "tool_use_result": {
    "stdout": "269:\n280:\n331:\n336:\n376:\n383:\n387:\n402:\n428:\n431:\n433:\n435:\n438:\n454:\n456:\n458:\n472:\n478:\n480:\n499:\n---\n1418:from Table 1. PR = prove rate, ISR∗ = proved-only ISR, H7/H1/N-H = percentage among proved\n1423:formal text-match taxonomy not run on this checkpoint.",
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

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_01XH4Ry82S33UHiJjwoNxAvz`</summary>

```json
{
  "command": "pdftotext -layout main.pdf - 2>/dev/null | awk '/^\\f/{page++} page==8{print NR\": \"$0}' | tail -30",
  "description": "Check what's on page 8 (end)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "a58c7c5f-eaa8-4fd1-a083-e2c7c89b8b54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2FTWzpxdErNZXMtr7tKzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 73647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
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

_source line 103 · 2026-05-17T17:40:36.787Z_

<details><summary>↩ Tool result · `toolu_01XH4Ry82S33UHiJjwoNxAvz`</summary>

```text
632: 720   s45: 55%→0% genuine). Readers should inter-             We release our taxonomy and diagnostic tools         769
633: 721   pret the 500-step non-hacking rates as upper            to help practitioners detect reward hacking          770
634: 722   bounds on long-run structural quality under             in their own systems. All experiments use            771
635: 723   continued training.                                     publicly available datasets (FOLIO) and open-        772
636:                                                               weight models (Qwen3-4B); no human sub-              773
637: 724   Seed counts per dose. ISR β=0.05 uses
638:                                                               jects are involved.                                  774
639: 725   three seeds (all H7-dominated); random
640: 726   β=0.05 uses three seeds with high variance
641: 727   (PR=0%, 7%, 62%); β=0.2 uses three seeds.               References                                           775
642: 728   The primary β=0.1 comparison uses five seeds
643:                                                               Dario Amodei, Chris Olah, Jacob Steinhardt, Paul     776
644: 729   per condition. Although all tested doses pro-             Christiano, John Schulman, and Dan Mané.          777
645: 730   duce dominant gaming, the stochastic bifurca-             2016. Concrete problems in AI safety. arXiv        778
646: 731   tion mechanism (§4.3) means that fewer-seed               preprint arXiv:1606.06565.                         779
647: 732   dose points may not capture the full variance
648:                                                               Manish Bhattarai, Ismael Boureima, Nishath Ra-       780
649: 733   of collapse timing. ISR β=0.1 s43 and s44                jiv Ranasinghe, Scott Pakin, and Dan O’Malley.      781
650: 734   checkpoints were lost during disk cleanup, pre-          2026.       Rubric-Grounded Reinforcement           782
651: 735   venting retrospective H8 audit on these seeds;           Learning:    Structured Judge Rewards for           783
652: 736   the reported 5-seed pooled non-hacking rate              Generalizable Reasoning.       arXiv preprint       784
653:                                                                arXiv:2605.08061.                                   785
654: 737   (23%) is an uncorrected upper bound.
655:                                                               Alexander Bondarenko, Denis Volk, Dmitrii            786
656: 738   Cross-scale replication. Our 1.7B experi-                 Volkov, and Jeffrey Ladish. 2025. Demonstrat-      787
657: 739   ments use a single seed. Although different               ing Specification Gaming in Reasoning Models.      788
658: 740   seeds may converge to different exploitation              arXiv preprint arXiv:2502.13295.                   789
659: 
660: 
661:                                                           9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "ca55351a-0b75-44b9-8be9-074380435225",
  "tool_use_result": {
    "stdout": "632: 720   s45: 55%→0% genuine). Readers should inter-             We release our taxonomy and diagnostic tools         769\n633: 721   pret the 500-step non-hacking rates as upper            to help practitioners detect reward hacking          770\n634: 722   bounds on long-run structural quality under             in their own systems. All experiments use            771\n635: 723   continued training.                                     publicly available datasets (FOLIO) and open-        772\n636:                                                               weight models (Qwen3-4B); no human sub-              773\n637: 724   Seed counts per dose. ISR β=0.05 uses\n638:                                                               jects are involved.                                  774\n639: 725   three seeds (all H7-dominated); random\n640: 726   β=0.05 uses three seeds with high variance\n641: 727   (PR=0%, 7%, 62%); β=0.2 uses three seeds.               References                                           775\n642: 728   The primary β=0.1 comparison uses five seeds\n643:                                                               Dario Amodei, Chris Olah, Jacob Steinhardt, Paul     776\n644: 729   per condition. Although all tested doses pro-             Christiano, John Schulman, and Dan Mané.          777\n645: 730   duce dominant gaming, the stochastic bifurca-             2016. Concrete problems in AI safety. arXiv        778\n646: 731   tion mechanism (§4.3) means that fewer-seed               preprint arXiv:1606.06565.                         779\n647: 732   dose points may not capture the full variance\n648:                                                               Manish Bhattarai, Ismael Boureima, Nishath Ra-       780\n649: 733   of collapse timing. ISR β=0.1 s43 and s44                jiv Ranasinghe, Scott Pakin, and Dan O’Malley.      781\n650: 734   checkpoints were lost during disk cleanup, pre-          2026.       Rubric-Grounded Reinforcement           782\n651: 735   venting retrospective H8 audit on these seeds;           Learning:    Structured Judge Rewards for           783\n652: 736   the reported 5-seed pooled non-hacking rate              Generalizable Reasoning.       arXiv preprint       784\n653:                                                                arXiv:2605.08061.                                   785\n654: 737   (23%) is an uncorrected upper bound.\n655:                                                               Alexander Bondarenko, Denis Volk, Dmitrii            786\n656: 738   Cross-scale replication. Our 1.7B experi-                 Volkov, and Jeffrey Ladish. 2025. Demonstrat-      787\n657: 739   ments use a single seed. Although different               ing Specification Gaming in Reasoning Models.      788\n658: 740   seeds may converge to different exploitation              arXiv preprint arXiv:2502.13295.                   789\n659: \n660: \n661:                                                           9",
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

_source line 104_

<details><summary>Logged reasoning block</summary>

```text
Page 8 has content and ends with page number 9, meaning the content on this physical page is page 9 (0-indexed from pdftotext). Let me check what's on physical pages and where section 5 ends. Let me search for the section content differently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "4cb5e973-3973-4f71-8668-96d1a6df326b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzAwePZp41mYnpTUetmZGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 74113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
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

_source line 105_

<details open><summary>🔧 Tool call — Bash · `toolu_016jToP5RmFc77rYhCRiasEZ`</summary>

```json
{
  "command": "pdftotext -layout main.pdf - 2>/dev/null | awk '/^\\f/{page++} page==7{print NR\": \"$0}' | grep -i \"cross-scale\\|preliminary\\|hacking taxonomy\\|§4\\|4.5\\|4.4\" | head -10",
  "description": "Check where §4.5/§5 appears on pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "1699e48f-5c10-4598-94dc-5598e1a60627",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzAwePZp41mYnpTUetmZGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 74113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 891
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

_source line 106 · 2026-05-17T17:40:45.285Z_

<details><summary>↩ Tool result · `toolu_016jToP5RmFc77rYhCRiasEZ`</summary>

```text
528: 607   4.4   Cross-Logic Diagnostic Transfer                   H9 ex falso       —      —       —      —        —          0         100
551: 620   gaming (s44, 95/97 proved at nnecessary =1).           (see §4.3 for seed-level analysis).                                            657
559: 626   results in Appendix Table 10 and Figure 4).            ble to execution-based evaluation (§4.2), and                                  660
561: 627   4.5   Preliminary Cross-Scale Evidence                 tested doses (trajectory-confirmed at β=0.1;                                   662
562: 628   We train Qwen3-1.7B under ISR β ∈ {0.1, 0.3}           §4.3–4.5). At 500 steps, ISR seeds descrip-                                    663
578: 643   4.6   Hacking Taxonomy                                 furcation between collapse and genuine win-                                    679
579: 644   The nine modes (Table 2; Appendix D) span              dows (§4.3), non-monotonic patterns across                                     680
582: 647   of hacking; H7b (14/350) evades text-match             sent from FOL (§4.4). These details, com-                                      683
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "d29b33b0-c2c8-415c-97c0-751f81d45c44",
  "tool_use_result": {
    "stdout": "528: 607   4.4   Cross-Logic Diagnostic Transfer                   H9 ex falso       —      —       —      —        —          0         100\n551: 620   gaming (s44, 95/97 proved at nnecessary =1).           (see §4.3 for seed-level analysis).                                            657\n559: 626   results in Appendix Table 10 and Figure 4).            ble to execution-based evaluation (§4.2), and                                  660\n561: 627   4.5   Preliminary Cross-Scale Evidence                 tested doses (trajectory-confirmed at β=0.1;                                   662\n562: 628   We train Qwen3-1.7B under ISR β ∈ {0.1, 0.3}           §4.3–4.5). At 500 steps, ISR seeds descrip-                                    663\n578: 643   4.6   Hacking Taxonomy                                 furcation between collapse and genuine win-                                    679\n579: 644   The nine modes (Table 2; Appendix D) span              dows (§4.3), non-monotonic patterns across                                     680\n582: 647   of hacking; H7b (14/350) evades text-match             sent from FOL (§4.4). These details, com-                                      683",
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

_source line 107_

<details open><summary>🔧 Tool call — Bash · `toolu_01BwgXyTrerQ6BsVst1MZKYV`</summary>

```json
{
  "command": "pdftotext -layout main.pdf - 2>/dev/null | awk '/^\\f/{page++} page==7{print NR\": \"$0}' | grep -i \"limitation\\|discussion\\|conclusion\\|section 5\\|§5\" | head -10",
  "description": "Check if §5 starts on page 7 (= page 8 in 1-indexed)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "23678e36-3c6a-4a1a-bb95-9c913f9c4691",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWsRQa9BodvL3UbuUmwRDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 75004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 569
      },
      "output_tokens": 69,
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

_source line 108 · 2026-05-17T17:40:50.226Z_

<details><summary>↩ Tool result · `toolu_01BwgXyTrerQ6BsVst1MZKYV`</summary>

```text
542: 613   conclusion embedding; ISR flags both failure           mark dominant mode. ♯ Prolog: strict+functional
555: 623   expose it. We attribute complete collapse              5       Discussion and Conclusion                                              658
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "d1faa5a5-28c1-4be5-b02b-85122ff912cd",
  "tool_use_result": {
    "stdout": "542: 613   conclusion embedding; ISR flags both failure           mark dominant mode. ♯ Prolog: strict+functional\n555: 623   expose it. We attribute complete collapse              5       Discussion and Conclusion                                              658",
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

_source line 109_

<details open><summary>🔧 Tool call — Bash · `toolu_01SZAorqZ19YUjwwocmrZav6`</summary>

```json
{
  "command": "pdftotext -layout main.pdf - 2>/dev/null | awk '/^\\f/{page++} page==7{print NR\": \"$0}' | tail -10",
  "description": "Check end of page 8 (0-indexed page 7)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "83631518-a304-4249-b059-6ae5cca1a0ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016atyJB4Rikrj4DZdDAwxyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 75573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 321
      },
      "output_tokens": 69,
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

_source line 110 · 2026-05-17T17:40:54.955Z_

<details><summary>↩ Tool result · `toolu_01SZAorqZ19YUjwwocmrZav6`</summary>

```text
583: 648   classifiers. ISR modestly increases H7 prob-           bined with the sensitivity of genuine-rate es-                                 684
584: 649   ability (OR=2.84, p<5×10−12 ; Appendix Ta-             timates to classification methodology, under-                                  685
585: 650   ble 4), but per-seed variance dominates. All           score the gap between predicting that a met-                                   686
586: 651   GRPO conditions show ≥80% pooled hack-                 ric will be gamed and predicting how. ISR                                      687
587: 652   ing; only SFT achieves 92.3% non-hacking.              and similar perturbation-based metrics should                                  688
588: 653   CMH tests treating samples as independent              serve as post-hoc evaluation tools, not training                               689
589: 654   yield ORCMH =2.46 (p<10−15 ) for H7 and 3.37           signals.                                                                       690
590: 
591: 
592:                                                          8
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "dba8ad7e-9d53-401e-8a7c-1096ef98c1f3",
  "tool_use_result": {
    "stdout": "583: 648   classifiers. ISR modestly increases H7 prob-           bined with the sensitivity of genuine-rate es-                                 684\n584: 649   ability (OR=2.84, p<5×10−12 ; Appendix Ta-             timates to classification methodology, under-                                  685\n585: 650   ble 4), but per-seed variance dominates. All           score the gap between predicting that a met-                                   686\n586: 651   GRPO conditions show ≥80% pooled hack-                 ric will be gamed and predicting how. ISR                                      687\n587: 652   ing; only SFT achieves 92.3% non-hacking.              and similar perturbation-based metrics should                                  688\n588: 653   CMH tests treating samples as independent              serve as post-hoc evaluation tools, not training                               689\n589: 654   yield ORCMH =2.46 (p<10−15 ) for H7 and 3.37           signals.                                                                       690\n590: \n591: \n592:                                                          8",
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

_source line 111_

Section 5 (Discussion and Conclusion) starts and ends on page 8 (physical page 8, 1-indexed). The page number printed at the bottom is "8". The content is within the 8-page limit.

No undefined citations, no em-dashes, citation count preserved (9), §5 finishes on page 8. Now commit Batch 2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "bf889821-f8f5-49a4-836d-76269539ba47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NPqCMCNXEeePj8k5jg21Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 409,
      "cache_read_input_tokens": 75894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 409
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

_source line 112_

<details open><summary>🔧 Tool call — Bash · `toolu_012at32mS3NUGb1zyqUXkHwZ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation && git add paper/experiments.tex paper/abstract.tex paper/introduction.tex paper/related_work.tex paper/conclusion.tex paper/references.bib paper/main.pdf paper/main.log && git commit -m \"$(cat <<'EOF'\n[paper] Round 7 Batch 2: Abstract/Intro simplify, Preliminary cross-scale, Goodhart 1975 ref, foreseeability, remove AI markers\n\nCo-Authored-By: Claude Opus 4.6 &lt;noreply@anthropic.com>\nEOF\n)\"",
  "description": "Commit Batch 2 changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "67928df7-b26c-4332-befa-644d9f0d7285",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NPqCMCNXEeePj8k5jg21Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 409,
      "cache_read_input_tokens": 75894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 409
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

_source line 113 · 2026-05-17T17:41:05.073Z_

<details><summary>↩ Tool result · `toolu_012at32mS3NUGb1zyqUXkHwZ`</summary>

```text
[master 4e7052f] [paper] Round 7 Batch 2: Abstract/Intro simplify, Preliminary cross-scale, Goodhart 1975 ref, foreseeability, remove AI markers
 Committer: Ubuntu &lt;ubuntu@ip-172-31-5-208.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 8 files changed, 59 insertions(+), 64 deletions(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "19424531-cae0-47b8-a358-0526744dae2a",
  "tool_use_result": {
    "stdout": "[master 4e7052f] [paper] Round 7 Batch 2: Abstract/Intro simplify, Preliminary cross-scale, Goodhart 1975 ref, foreseeability, remove AI markers\n Committer: Ubuntu &lt;ubuntu@ip-172-31-5-208.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 8 files changed, 59 insertions(+), 64 deletions(-)",
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

_source line 114_

Done. Two commits created:

1. `37317d3` — `[paper] Round 7 Batch 1: CMH non-independence caveat across 5 files, transient window reframed as descriptive`
2. `4e7052f` — `[paper] Round 7 Batch 2: Abstract/Intro simplify, Preliminary cross-scale, Goodhart 1975 ref, foreseeability, remove AI markers`

All checks passed: no em-dashes, no undefined citations, intro citations preserved (9→9), §5 ends on page 8.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "uuid": "d774f86e-c42e-47c8-b5ef-2310aa62cf1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8grFdfNix3oF93wTT3kS7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 76303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 115_

Done. Two commits created:

1. `37317d3` — `[paper] Round 7 Batch 1: CMH non-independence caveat across 5 files, transient window reframed as descriptive`
2. `4e7052f` — `[paper] Round 7 Batch 2: Abstract/Intro simplify, Preliminary cross-scale, Goodhart 1975 ref, foreseeability, remove AI markers`

All checks passed: no em-dashes, no undefined citations, intro citations preserved (9→9), §5 ends on page 8.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 239359,
  "duration_api_ms": 232085,
  "num_turns": 44,
  "stop_reason": "end_turn",
  "session_id": "742c4bba-1172-4bdb-8d32-c37deb04ffa9",
  "total_cost_usd": 1.4375472500000002,
  "usage": {
    "input_tokens": 26,
    "cache_creation_input_tokens": 64985,
    "cache_read_input_tokens": 1559320,
    "output_tokens": 9847,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 64985,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 142,
        "cache_read_input_tokens": 76303,
        "cache_creation_input_tokens": 523,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 523
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 5316,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.005426,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 26,
      "outputTokens": 9847,
      "cacheReadInputTokens": 1559320,
      "cacheCreationInputTokens": 64985,
      "webSearchRequests": 0,
      "costUSD": 1.4321212500000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8a2b3f09-6088-4810-a0db-ab4d6bbf67d9"
}
```

</details>

---
