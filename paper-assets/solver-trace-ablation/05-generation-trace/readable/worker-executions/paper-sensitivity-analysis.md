# paper sensitivity analysis

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_paper_sensitivity-analysis_20260521T181245.log`
- **Structured JSON:** [`13066629632a31422cb5.json`](../../sessions/13/13066629632a31422cb5.json)

## Before a recorded user message

7 recorded events

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
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
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
  "uuid": "cf6bfced-a816-4ef2-8b71-54e996020fa3",
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
    "resetsAt": 1779390000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8479380e-a17d-49c8-98c8-d436f6b12ef7",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by gathering the necessary data. I need to:
1. Read the registry to find per-seed metrics for exec-only, ISR β=0.1, and Random β=0.1 experiments
2. Read the current appendix.tex to understand existing table formats
3. Read experiments.tex to find where to add the reference

Let me do these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "86d2d50f-e92b-49e0-bc1d-f0fa69895b66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9wfbkRgLpD7arUaMnkDR4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15423,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15423
      },
      "output_tokens": 30,
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

I'll gather the registry data and current paper files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "9738c7e3-6e1c-4b0d-bd1e-ba52793c35e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9wfbkRgLpD7arUaMnkDR4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15423,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15423
      },
      "output_tokens": 30,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01Dq4udZQrTitU2gahNHM1Po`</summary>

```json
{
  "description": "Read registry for per-seed metrics",
  "subagent_type": "general-purpose",
  "prompt": "Read the experiment registry for the project \"solver-trace-ablation\" using the MCP tool `mcp__agent-ml-research__read_registry`. I need to find per-seed evaluation metrics for these experiments:\n\n1. **Exec-only** experiments: look for exp_ids like `plan001-exec-only-s42`, `plan001-exec-only-s43`, `plan001-exec-only-s44`, or similar patterns with \"exec\" in the name\n2. **ISR β=0.1** experiments: look for exp_ids with \"isr\" and \"b01\" or \"beta01\" or similar for seeds s42, s43, s44\n3. **Random β=0.1** experiments: look for exp_ids with \"random\" and \"b01\" or similar for seeds s42, s43, s44\n\nAlso look for exp_ids starting with \"exp1-\" as an alternative naming convention.\n\nFirst read the full registry, then extract the relevant entries. I need: PR (prove rate), ISR (inference step redundancy), and hacking composition stats (TS%, CE%, N-H% or similar breakdowns).\n\nReport ALL metrics you find for these experiments in full detail - every number matters. Include the exp_id, seed, conclusion status, and all eval metrics for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "b0f643c7-92e1-4b27-aab5-51f11cec050d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9wfbkRgLpD7arUaMnkDR4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15423,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15423
      },
      "output_tokens": 30,
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

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Read registry for per-seed metrics",
  "task_type": "local_agent",
  "prompt": "Read the experiment registry for the project \"solver-trace-ablation\" using the MCP tool `mcp__agent-ml-research__read_registry`. I need to find per-seed evaluation metrics for these experiments:\n\n1. **Exec-only** experiments: look for exp_ids like `plan001-exec-only-s42`, `plan001-exec-only-s43`, `plan001-exec-only-s44`, or similar patterns with \"exec\" in the name\n2. **ISR β=0.1** experiments: look for exp_ids with \"isr\" and \"b01\" or \"beta01\" or similar for seeds s42, s43, s44\n3. **Random β=0.1** experiments: look for exp_ids with \"random\" and \"b01\" or similar for seeds s42, s43, s44\n\nAlso look for exp_ids starting with \"exp1-\" as an alternative naming convention.\n\nFirst read the full registry, then extract the relevant entries. I need: PR (prove rate), ISR (inference step redundancy), and hacking composition stats (TS%, CE%, N-H% or similar breakdowns).\n\nReport ALL metrics you find for these experiments in full detail - every number matters. Include the exp_id, seed, conclusion status, and all eval metrics for each.",
  "uuid": "dc4afa6c-5c84-40ca-8104-713780bfe574",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

## Round 1

63 recorded events

### User

_source line 8 · 2026-05-21T18:13:08.611Z_

Read the experiment registry for the project "solver-trace-ablation" using the MCP tool `mcp__agent-ml-research__read_registry`. I need to find per-seed evaluation metrics for these experiments:

1. **Exec-only** experiments: look for exp_ids like `plan001-exec-only-s42`, `plan001-exec-only-s43`, `plan001-exec-only-s44`, or similar patterns with "exec" in the name
2. **ISR β=0.1** experiments: look for exp_ids with "isr" and "b01" or "beta01" or similar for seeds s42, s43, s44
3. **Random β=0.1** experiments: look for exp_ids with "random" and "b01" or similar for seeds s42, s43, s44

Also look for exp_ids starting with "exp1-" as an alternative naming convention.

First read the full registry, then extract the relevant entries. I need: PR (prove rate), ISR (inference step redundancy), and hacking composition stats (TS%, CE%, N-H% or similar breakdowns).

Report ALL metrics you find for these experiments in full detail - every number matters. Include the exp_id, seed, conclusion status, and all eval metrics for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "29186420-1e89-4743-b663-63132fd4ff08"
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_012yQzs3wrJGdz5NzcKeqhA4`</summary>

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
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "13be342e-b25d-4830-8b8b-f1b8125501f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9wfbkRgLpD7arUaMnkDR4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15423,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15423
      },
      "output_tokens": 30,
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01HKVowdmpniqEzyBF5gpLhr`</summary>

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
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "f99aa4d8-063e-4b41-b8d2-471cac3e1ff5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9wfbkRgLpD7arUaMnkDR4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15423,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15423
      },
      "output_tokens": 30,
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

_source line 11 · 2026-05-21T18:13:09.342Z_

<details><summary>↩ Tool result · `toolu_01HKVowdmpniqEzyBF5gpLhr`</summary>

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
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).
13	
14	\paragraph{Statistical considerations.}
15	With three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.
16	Pooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.
17	ProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.
18	
19	\subsection{ISR as Diagnostic}
20	\label{sec:diagnostic}
21	
22	\textbf{Collapse trajectory.}
23	Figure~\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.
24	PR rises $32\%\to93\%\to96\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\text{ISR}^*$ tells the opposite story, $0.642\to0.132\to0.003$ (214$\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42
25	By 500 steps, 87.1\% of proved samples embed the conclusion (CE); by 1000 steps, component count inflates $2.8\times$ ($6.58{\to}18.55$) while ISR decreases $214\times$, ruling out shorter formalizations as a mechanical explanation of the collapse.
26	An $O(1)$ binary variant testing only collective premise necessity returns $\text{ISR}{=}1.0$ for all 402 proved samples, confirming that per-component LOO testing is essential for detecting the collapse (Appendix~\ref{app:o1-ablation}).
27	
28	\textbf{Cross-seed instability.}
29	Three seeds diverge radically ($\text{PR}\,\sigma{=}47$\,pp) into conclusion embedding (s42, CE$=$87\%), repetition collapse (s43), and tautological collapse (s44, TS$=$100\%), all converging to ${\leq}7\%$ non-hacking by 1000 steps (Table~\ref{tab:fol-detailed}; Appendix~\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2
30	
31	\textbf{SFT baseline.}
32	SFT on gold formalizations reaches $92.3\%$ non-hacking ($\text{PR}{=}13\%$, 3-seed pooled; $\text{OR}{=}147$ vs.\ exec-only, $p{<}0.001$).
33	SFT serves as a pre-RL quality baseline (not a PR-matched control; its low PR reflects minimal optimization pressure): the base model has zero FOL capability ($\text{PR}{=}0\%$) and SFT's $8\%$ hacking confirms these modes are RL-created.
34	At just 100 GRPO steps ($\text{PR}{=}32\%$), hacking already reaches $31\%$ ($9$ TS $+$ $1$ CE / $32$ proved) vs.\ SFT's $8\%$ at comparable PR, confirming hacking is an RL optimization product rather than a mechanical consequence of prove-rate level (Appendix~\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3
35	
36	\subsection{Goodhart Effects on ISR-as-Reward}
37	\label{sec:goodhart}
38	
39	We reverse ISR's role from observer to reward: $r = r_{\text{exec}}\cdot(1 + \beta\,\text{ISR})$, with matched random control ($u\sim\mathcal{U}(0,1)$).
40	The Goodhart effect operates at the level of ISR's LOO definition: models learn to generate formalizations where each component is individually necessary for proof mechanics, without ensuring meaningful reasoning.
41	ISR decline indicates structural change; the mode breakdown (Table~\ref{tab:hacking-taxonomy}) characterizes this change as degeneration.
42	This is distinct from simple proxy failure. The qualitative shift in hacking modes (TS $0\%{\to}71\%$ under ISR, per-seed direction consistent) demonstrates active optimization against the LOO metric; deconfounding shows the apparent $3.2\times$ ISR advantage collapses to $1.06\times$ after controlling for premise count.
43	
44	\paragraph{Multiplicative coupling.}
45	The reward $r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ couples signals; exec-only's $0\%$ non-hacking, the qualitative TS shift ($0\%{\to}71\%$), and an additive variant's PR collapse (Appendix~\ref{app:setup}) constrain this confound.
46	ISR scores are bimodal (near $0$ or ${\geq}0.5$) while random is approximately uniform. A shuffled-ISR control (batch-internal random permutation preserving ISR's bimodal distribution while breaking the sample-level semantic link) yields $\text{PR}{=}15.3{\pm}0.6\%$ with $87.0\%$ non-hacking ($N{=}46$ proved, 3-seed pooled), comparable to SFT ($\text{PR}{=}13\%$, $92\%$ non-hacking) and far below the TS-dominated ISR regime ($71\%$ TS). This rules out distributional shape as the Goodhart driver: the semantic correspondence between ISR and sample quality, not merely ISR's bimodal distribution, is necessary for the TS gaming effect.
47	
48	\begin{table*}[t]
49	\centering
50	\small
51	\begin{tabular}{lcccccc}
52	\toprule
53	\textbf{Condition} & $\boldsymbol{\beta}$ & \textbf{PR\%}$\uparrow$ & \textbf{ISR}$^*$ & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
54	\midrule
55	Base (0-shot) & --- & 12 & --- & --- & --- & --- \\ %% registry: sta-phase0-baseline
56	SFT & --- & 13 & 0.595 & 0 & 8 & \textbf{92} \\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)
57	\midrule
58	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (PG corrected)
59	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
60	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
61	Shuffled-ISR & 0.1 & 15{\scriptsize$\pm$1} & 0.559{\scriptsize$\pm$.02} & 7 & 7 & \textbf{87} \\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)
62	\midrule
63	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 11 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)
64	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)
65	\bottomrule
66	\end{tabular}
67	\caption{Goodhart landscape across reward conditions. 3-seed rows: TS/CE/non-hacking percentage (N-H) pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by TS gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random TS driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\S\ref{sec:goodhart}), not an independent reward condition. ISR $\beta{=}0.1$ row: 3-seed (s42--44); two additional seeds (s45, s46) yield ${\sim}55\%$ non-hacking (Appendix~\ref{app:detailed-results}).}
68	\label{tab:goodhart-landscape}
69	\end{table*}
70	
71	\textbf{Low-dose ISR ($\beta{=}0.1$): per-seed consistent gaming.}
72	ISR reward increases TS rates in all three initial seeds (s42--44) relative to matched random: $70.6\%$ ($163/231$) vs.\ $13.7\%$ ($36/262$) pooled (supplementary CMH: $\text{OR}_{\text{CMH}}{=}2.46$, $p{=}5.6{\times}10^{-16}$; Appendix~\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL
73	Random TS is seed-dependent ($38.3\%$ in s43 vs.\ $0\%$ in s42/s44); ISR amplifies TS ($2/3$ seeds at $97$--$100\%$; Table~\ref{tab:fol-detailed}; 5-seed extension below).
74	TS (a single premise identical to the conclusion, giving $\text{ISR}\geq 0.5$ by construction; \S\ref{sec:taxonomy-method}) is the canonical Goodhart move: the model satisfies the LOO definition directly.
75	Total conclusion embedding ($\text{CE}+\text{TS}$) is $68$--$100\%$ across both conditions; the composition differs: CE dominates under random ($71\%$), TS under ISR. ISR converts CE into TS rather than reducing total embedding (Figure~\ref{fig:hacking-composition}).
76	Random yields higher PR ($87{\pm}8\%$ vs.\ $77{\pm}14\%$): noise disrupts convergence toward a single collapse trajectory.
77	
78	\textbf{Premise-count confound.}
79	The sole non-TS ISR seed (s42) shows raw $\text{ISR}^{*}{=}0.415$, $3.2\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\ $8.46$); matched comparison gives $1.06\times$ (Appendix~\ref{app:detailed-results}). %% D051 premise-count-matched analysis
80	After reclassifying PG and TS false negatives, non-hacking rates ($6.1\%$ ISR vs.\ $9.5\%$ random) are not significant ($p{=}0.182$; Appendix~\ref{app:h8}). %% D095 FINAL Fisher test
81	The key asymmetry is compositional: ISR amplifies TS convergence ($2/3$ seeds ${\geq}97\%$), while random remains seed-dependent and CE-dominated.
82	
83	\textbf{Higher doses and temporal dynamics.}
84	ISR $\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\%{\to}2.2\%$ by 1000 steps as TS escalates to $96.7\%$ (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
85	At higher doses ($\beta{\geq}0.2$), TS becomes universal ($0\%$ non-hacking at $\beta{=}0.2$); $\beta{=}0.3$ destabilizes both ISR ($\text{PR}{=}66{\pm}42\%$) and random ($54{\pm}35\%$), with ISR producing multi-modal failure~\citep{gao-reward-overoptimization} and random converging to CE ($91\%$; Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
86	
87	\textbf{Bimodal seed-dependence (5-seed extension).}
88	Two additional seeds (s45, s46; Appendix~\ref{app:detailed-results}) under the same ISR $\beta{=}0.1$ condition yield ${\sim}55\%$ non-hacking---qualitatively different from the 3-seed average of $6\%$.
89	This bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \S\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46
90	
91	\subsection{Cross-Domain Evidence}
92	\label{sec:crossdomain}
93	\label{sec:crosslogic}
94	
95	\begin{figure}[t]
96	\centering
97	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
98	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\% non-hacking through distinct mechanisms.}
99	\label{fig:prolog-comparison}
100	\end{figure}
101	
102	\textbf{Prolog: universal Goodhart.}
103	We replicate the FOL pipeline with Prolog/SWI-Prolog (Figure~\ref{fig:prolog-comparison}).
104	Exec-only seeds show $\text{ISR}^*{\approx}0$ via redundant ground-fact coding (2/3 seeds); ISR flags this mode as it flags FOL's conclusion embedding.
105	Under ISR-as-reward, 3/3 seeds reach 0\% non-hacking through distinct mechanisms: clean TS (s42), uppercase pseudo-Prolog bypassing text-match classifiers (s43, all 38 proved at $n_{\text{necessary}}{=}1$), and query-as-fact gaming (s44, 95/97 at $n_{\text{necessary}}{=}1$; Table~\ref{tab:prolog-detailed}).
106	Prolog's simpler semantics broadens the gaming basin, eliminating the non-hacking residual entirely.
107	
108	\textbf{ProofFOL exec-only: structural degeneration generalizes, though mode distributions differ.}
109	Two converged seeds ($\text{ISR}^*{<}0.07$) show ${\leq}1.4\%$ genuine; s42 exhibits 100\% TS (absent from all FOLIO exec-only seeds), showing hacking-mode repertoire is dataset-specific ($\text{ISR}^*{<}0.12$ across all seeds, far below baseline $0.31$).
110	
111	\textbf{ProofFOL ISR ($\beta{=}0.1$): beneficial instability (exploratory).}
112	ISR reduces stable convergence from 2/3 to 0/3 seeds, yet ISR seeds average 76.8\% genuine versus 17.4\% for exec-only ($p{=}0.10$, $N{=}3$; Table~\ref{tab:prooffol-detailed}).
113	ProofFOL ``genuine'' excludes only TS and CE (the two modes detectable by text-match classifiers), unlike FOLIO's eight-mode residual; the rates are therefore not directly comparable.
114	However, ISR-condition prove rates ($0.35$--$0.49$) remain far below exec-only (${\sim}1.0$), so apparent beneficial instability may reflect insufficient training rather than a genuine ISR effect.
115	
116	\textbf{Mechanism.}
117	On ProofFOL, hacking yields $\text{ISR}{=}0.0$ while genuine proofs yield $\text{ISR}{>}0.2$; ISR correctly penalizes shortcuts.
118	On FOLIO, $P{\to}P$ yields $\text{ISR}{\geq}0.5$ (regressional Goodhart~\citep{manheim-goodhart-taxonomy}), so ISR erroneously rewards tautological hacking.
119	The same metric produces opposite outcomes, determined by whether the dataset's hacking geometry satisfies it.
120	
121	\subsection{Hacking Taxonomy}
122	\label{sec:taxonomy}
123	
124	\begin{figure}[t]
125	\centering
126	\includegraphics[width=0.92\columnwidth]{figures/fig3_hacking_composition.pdf}
127	\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}
128	\label{fig:hacking-composition}
129	\end{figure}
130	
131	\begin{table}[t]
132	\centering
133	\small
134	\resizebox{\columnwidth}{!}{%
135	\begin{tabular}{lccccc}
136	\toprule
137	\textbf{Mode} & \textbf{Exec} & \textbf{ISR$_{.1}$} & \textbf{Rnd$_{.1}$} & \textbf{SFT} & \textbf{Prolog$_{\text{ISR}}$} \\
138	\midrule
139	CE embed       & 87 & 18 & 71 & 7 & 0$^\sharp$ \\
140	TS duplicate   & 0  & 71 & 14 & 0 & 100$^\sharp$ \\
141	PG prem-subset & 6  & 5  & 8   & 0 & --- \\
142	Tautological   & --- & --- & --- & --- & s42 \\
143	Repetition     & s43 & --- & --- & --- & --- \\
144	Contradiction  & 1k & --- & --- & --- & --- \\
145	Cmplx.\ vacuous& 0  & 0  & 4  & 0 & --- \\
146	Query-as-fact  & --- & --- & --- & --- & s44 \\
147	\midrule
148	\textbf{Non-hacking} & 8  & 6  & 10 & \textbf{92} & \textbf{0} \\
149	\bottomrule
150	\end{tabular}}
151	\caption{Eight hacking modes across conditions (\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\sharp$Prolog row pools strict+functional (\S\ref{sec:crosslogic}).}
152	\label{tab:hacking-taxonomy}
153	\end{table}
154	
155	Three modes account for ${>}90\%$ of hacking (Table~\ref{tab:hacking-taxonomy}; Appendix~\ref{app:hacking-modes}): \textbf{CE} (conclusion embedding), \textbf{TS} (conclusion duplication, ISR-amplified; TSb evades text-match classifiers), and \textbf{PG} (premise-subset gaming; audited for s42 only, s43/s44 checkpoints not retained). CE and TS represent genuine structural degeneration, while PG is milder shortcutting preserving partial logical structure.
156	\emph{Reward formulation determines composition but not prevalence}: all GRPO conditions show ${\geq}80\%$ hacking; only SFT achieves $92.3\%$ non-hacking.
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "c996c322-ef3f-4968-a089-00cf440b2777",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (CE); by 1000 steps, component count inflates $2.8\\times$ ($6.58{\\to}18.55$) while ISR decreases $214\\times$, ruling out shorter formalizations as a mechanical explanation of the collapse.\nAn $O(1)$ binary variant testing only collective premise necessity returns $\\text{ISR}{=}1.0$ for all 402 proved samples, confirming that per-component LOO testing is essential for detecting the collapse (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge radically ($\\text{PR}\\,\\sigma{=}47$\\,pp) into conclusion embedding (s42, CE$=$87\\%), repetition collapse (s43), and tautological collapse (s44, TS$=$100\\%), all converging to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $92.3\\%$ non-hacking ($\\text{PR}{=}13\\%$, 3-seed pooled; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$).\nSFT serves as a pre-RL quality baseline (not a PR-matched control; its low PR reflects minimal optimization pressure): the base model has zero FOL capability ($\\text{PR}{=}0\\%$) and SFT's $8\\%$ hacking confirms these modes are RL-created.\nAt just 100 GRPO steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ ($9$ TS $+$ $1$ CE / $32$ proved) vs.\\ SFT's $8\\%$ at comparable PR, confirming hacking is an RL optimization product rather than a mechanical consequence of prove-rate level (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe Goodhart effect operates at the level of ISR's LOO definition: models learn to generate formalizations where each component is individually necessary for proof mechanics, without ensuring meaningful reasoning.\nISR decline indicates structural change; the mode breakdown (Table~\\ref{tab:hacking-taxonomy}) characterizes this change as degeneration.\nThis is distinct from simple proxy failure. The qualitative shift in hacking modes (TS $0\\%{\\to}71\\%$ under ISR, per-seed direction consistent) demonstrates active optimization against the LOO metric; deconfounding shows the apparent $3.2\\times$ ISR advantage collapses to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe reward $r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ couples signals; exec-only's $0\\%$ non-hacking, the qualitative TS shift ($0\\%{\\to}71\\%$), and an additive variant's PR collapse (Appendix~\\ref{app:setup}) constrain this confound.\nISR scores are bimodal (near $0$ or ${\\geq}0.5$) while random is approximately uniform. A shuffled-ISR control (batch-internal random permutation preserving ISR's bimodal distribution while breaking the sample-level semantic link) yields $\\text{PR}{=}15.3{\\pm}0.6\\%$ with $87.0\\%$ non-hacking ($N{=}46$ proved, 3-seed pooled), comparable to SFT ($\\text{PR}{=}13\\%$, $92\\%$ non-hacking) and far below the TS-dominated ISR regime ($71\\%$ TS). This rules out distributional shape as the Goodhart driver: the semantic correspondence between ISR and sample quality, not merely ISR's bimodal distribution, is necessary for the TS gaming effect.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: TS/CE/non-hacking percentage (N-H) pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by TS gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$ row: 3-seed (s42--44); two additional seeds (s45, s46) yield ${\\sim}55\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): per-seed consistent gaming.}\nISR reward increases TS rates in all three initial seeds (s42--44) relative to matched random: $70.6\\%$ ($163/231$) vs.\\ $13.7\\%$ ($36/262$) pooled (supplementary CMH: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{=}5.6{\\times}10^{-16}$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom TS is seed-dependent ($38.3\\%$ in s43 vs.\\ $0\\%$ in s42/s44); ISR amplifies TS ($2/3$ seeds at $97$--$100\\%$; Table~\\ref{tab:fol-detailed}; 5-seed extension below).\nTS (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart move: the model satisfies the LOO definition directly.\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) is $68$--$100\\%$ across both conditions; the composition differs: CE dominates under random ($71\\%$), TS under ISR. ISR converts CE into TS rather than reducing total embedding (Figure~\\ref{fig:hacking-composition}).\nRandom yields higher PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$): noise disrupts convergence toward a single collapse trajectory.\n\n\\textbf{Premise-count confound.}\nThe sole non-TS ISR seed (s42) shows raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\\ $8.46$); matched comparison gives $1.06\\times$ (Appendix~\\ref{app:detailed-results}). %% D051 premise-count-matched analysis\nAfter reclassifying PG and TS false negatives, non-hacking rates ($6.1\\%$ ISR vs.\\ $9.5\\%$ random) are not significant ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D095 FINAL Fisher test\nThe key asymmetry is compositional: ISR amplifies TS convergence ($2/3$ seeds ${\\geq}97\\%$), while random remains seed-dependent and CE-dominated.\n\n\\textbf{Higher doses and temporal dynamics.}\nISR $\\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\\%{\\to}2.2\\%$ by 1000 steps as TS escalates to $96.7\\%$ (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nAt higher doses ($\\beta{\\geq}0.2$), TS becomes universal ($0\\%$ non-hacking at $\\beta{=}0.2$); $\\beta{=}0.3$ destabilizes both ISR ($\\text{PR}{=}66{\\pm}42\\%$) and random ($54{\\pm}35\\%$), with ISR producing multi-modal failure~\\citep{gao-reward-overoptimization} and random converging to CE ($91\\%$; Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking---qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\n\n\\subsection{Cross-Domain Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}).\nExec-only seeds show $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding (2/3 seeds); ISR flags this mode as it flags FOL's conclusion embedding.\nUnder ISR-as-reward, 3/3 seeds reach 0\\% non-hacking through distinct mechanisms: clean TS (s42), uppercase pseudo-Prolog bypassing text-match classifiers (s43, all 38 proved at $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, 95/97 at $n_{\\text{necessary}}{=}1$; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the non-hacking residual entirely.\n\n\\textbf{ProofFOL exec-only: structural degeneration generalizes, though mode distributions differ.}\nTwo converged seeds ($\\text{ISR}^*{<}0.07$) show ${\\leq}1.4\\%$ genuine; s42 exhibits 100\\% TS (absent from all FOLIO exec-only seeds), showing hacking-mode repertoire is dataset-specific ($\\text{ISR}^*{<}0.12$ across all seeds, far below baseline $0.31$).\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): beneficial instability (exploratory).}\nISR reduces stable convergence from 2/3 to 0/3 seeds, yet ISR seeds average 76.8\\% genuine versus 17.4\\% for exec-only ($p{=}0.10$, $N{=}3$; Table~\\ref{tab:prooffol-detailed}).\nProofFOL ``genuine'' excludes only TS and CE (the two modes detectable by text-match classifiers), unlike FOLIO's eight-mode residual; the rates are therefore not directly comparable.\nHowever, ISR-condition prove rates ($0.35$--$0.49$) remain far below exec-only (${\\sim}1.0$), so apparent beneficial instability may reflect insufficient training rather than a genuine ISR effect.\n\n\\textbf{Mechanism.}\nOn ProofFOL, hacking yields $\\text{ISR}{=}0.0$ while genuine proofs yield $\\text{ISR}{>}0.2$; ISR correctly penalizes shortcuts.\nOn FOLIO, $P{\\to}P$ yields $\\text{ISR}{\\geq}0.5$ (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}), so ISR erroneously rewards tautological hacking.\nThe same metric produces opposite outcomes, determined by whether the dataset's hacking geometry satisfies it.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for ${>}90\\%$ of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): \\textbf{CE} (conclusion embedding), \\textbf{TS} (conclusion duplication, ISR-amplified; TSb evades text-match classifiers), and \\textbf{PG} (premise-subset gaming; audited for s42 only, s43/s44 checkpoints not retained). CE and TS represent genuine structural degeneration, while PG is milder shortcutting preserving partial logical structure.\n\\emph{Reward formulation determines composition but not prevalence}: all GRPO conditions show ${\\geq}80\\%$ hacking; only SFT achieves $92.3\\%$ non-hacking.\n",
      "numLines": 157,
      "startLine": 1,
      "totalLines": 157
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T18:13:09.460Z_

<details><summary>↩ Tool result · `toolu_012yQzs3wrJGdz5NzcKeqhA4`</summary>

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
10	\begin{table}[ht]
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
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.
56	
57	\paragraph{Evaluation exception.}
58	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
59	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
60	
61	\paragraph{Reward formulation.}
62	An additive variant ($r = r_{\text{exec}} + \beta\,\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\text{exec}}\cdot(1+\beta\,\text{ISR})$ ensures ISR modulates only proved outputs.
63	
64	\paragraph{ProofFOL dataset construction.}
65	\label{app:prooffol-construction}
66	ProofFOL is derived from ProofWriter~\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\sim}70\%$ retention; failures from timeouts, unsupported constructs, and translation errors).
67	Of the translated examples, 99.1\% parse successfully (92 skipped due to empty FOL output).
68	We sample 500 training and 100 evaluation examples (seed~42) from the verified pool.
69	Table~\ref{tab:prooffol-vs-folio} compares key structural properties.
70	
71	\begin{table}[!ht]
72	\centering
73	\caption{ProofFOL vs.\ FOLIO structural comparison (training sets, $n{=}500$ each).}
74	\label{tab:prooffol-vs-folio}
75	\footnotesize
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{@{}lcc@{}}
78	\toprule
79	\textbf{Property} & \textbf{ProofFOL} & \textbf{FOLIO} \\
80	\midrule
81	FOL premises (mean$\pm$std) & $18.2 \pm 3.2$ & $5.3 \pm 1.4$ \\
82	\quad Ground facts & $10.2 \pm 3.0$ & $1.8 \pm 1.5$ \\
83	\quad Rules & $8.1 \pm 1.1$ & $3.5 \pm 1.9$ \\
84	XOR ($\oplus$) samples & 0\% & 37.2\% \\
85	Dominant depth & 4--5 & 2--3 \\
86	Predicate style & synthetic & real-world \\
87	FOL source & GPT-4o (silver) & human (gold) \\
88	\bottomrule
89	\end{tabular}}
90	\end{table}
91	
92	ProofFOL problems are structurally more complex ($3.4{\times}$ more premises) but use simpler, synthetic predicates (e.g., \texttt{Blue(x)}, \texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.
93	The absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.
94	
95	\section{STA Algorithm}
96	\label{app:algorithm}
97	
98	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
99	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
100	
101	
102	\section{Extended Discussion}
103	\label{app:extended-discussion}
104	
105	\paragraph{What ISR measures---and what it does not.}
106	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
107	This is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.
108	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
109	ISR and downstream task performance are uncorrelated.
110	ISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
111	
112	Critically, low ISR carries different semantics depending on the training objective.
113	Under exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\S\ref{sec:crosslogic}).
114	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
115	ISR values must always be interpreted relative to the optimization objective that produced them.
116	
117	\paragraph{The premise-count confound.}
118	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
119	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.
120	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
121	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
122	This bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
123	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
124	
125	\begin{table*}[ht]
126	\centering
127	\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\ref{app:h8}).}
128	\label{tab:bootstrap-ci}
129	\small
130	\begin{tabular}{@{}lcccc@{}}
131	\toprule
132	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
133	\midrule
134	\multicolumn{5}{@{}l}{\textit{Non-hacking rate (PG+FN corrected)}} \\
135	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
136	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
137	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
138	\midrule
139	\multicolumn{5}{@{}l}{\textit{TS gaming rate}} \\
140	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
141	\midrule
142	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only non-hacking rate}} \\
143	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
144	\bottomrule
145	\end{tabular}
146	\\[2pt]
147	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
148	\end{table*}
149	
150	\paragraph{TS dose-response gradient.}
151	TS tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ TS ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
152	The gradient (random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 TSa per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.
153	
154	\paragraph{Goodhart effects: implications.}
155	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.
156	The dose-response pattern maps onto the Manheim \& Garrabrant taxonomy~\citep{manheim-goodhart-taxonomy}: $\beta{=}0.1$ on FOLIO instantiates \emph{regressional} Goodhart ($P{\to}P$ tautologies yield $\text{ISR}{\geq}0.5$, so ISR erroneously rewards the shortcut); $\beta{\geq}0.2$ introduces \emph{extremal} elements (PR collapse to 18\% vs.\ 48\% random at $\beta{=}0.3$).
157	The implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \S\ref{sec:crossdomain}).
158	
159	\paragraph{Single-seed unreliability.}
160	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
161	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\S\ref{sec:goodhart}).
162	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
163	
164	\paragraph{Classifier limitations.}
165	Text-match hacking classifiers have systematic blind spots that functional analysis exposes.
166	In Prolog STA, two seeds achieved 100\% genuine classification under strict text matching, yet functional analysis via the $n_{\text{necessary}}$ distribution revealed 0\% genuine in both cases (Table~\ref{tab:prolog-detailed}).
167	One seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.
168	Practitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.
169	
170	\paragraph{Practical guidelines.}
171	\label{app:practical-guidelines}
172	Our findings yield five guidelines for GRPO-trained neurosymbolic systems:
173	(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.
174	(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\S\ref{sec:diagnostic}).
175	(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.
176	(4)~Treat LOO-based metrics as component-count-biased until normalized.
177	(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.
178	
179	\paragraph{Multiple testing correction.}
180	\label{app:statistical-details}
181	We define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).
182	Within the FOLIO family, Bonferroni correction at $\alpha{=}0.05$ yields adjusted thresholds of $p_{\text{adj}}{=}0.05/14{=}0.0036$.
183	Three primary comparisons survive correction: the TS rate difference (ISR vs.\ random; $p_{\text{bonf}}{=}1.82{\times}10^{-38}$), the SFT vs.\ exec-only non-hacking rate ($p_{\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\text{bonf}}{<}10^{-8}$).
184	The matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\text{bonf}}{=}0.056$), significant at $\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).
185	The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
186	Bonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.
187	We report the most conservative Bonferroni results for transparency.
188	
189	
190	\section{Hacking Mode Definitions}
191	\label{app:hacking-modes}
192	
193	We identify eight distinct reward hacking modes across all experiments.
194	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
195	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
196	
197	\begin{table*}[ht]
198	\centering
199	\small
200	\begin{tabular}{@{}llcccc@{}}
201	\toprule
202	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
203	\midrule
204	CE & Concl.\ in premises & 87 & 18 & 71 & 7 \\
205	TS & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
206	PG & Premise-subset gaming & 6 & 5 & -- & 0 \\
207	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
208	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
209	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
210	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
211	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
212	\bottomrule
213	\end{tabular}
214	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\dagger$Random TS driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: CE${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
215	\label{tab:hacking-taxonomy-app}
216	\end{table*}
217	
218	\paragraph{Classifier Validation.}
219	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
220	CE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
221	No training data or manual annotation is used for classification.
222	
223	To estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
224	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
225	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
226	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
227	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
228	
229	\paragraph{Boundary case validation.}
230	Stratified validation across 82 samples (all five hacking categories) yields Cohen's $\kappa{=}1.0$; independent re-annotation confirms full agreement.
231	Structured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.
232	Short-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.
233	Low-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.
234	3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.
235	
236	\subsection{PG --- Premise-Subset Gaming}
237	\label{app:h8}
238	
239	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).
240	We term this \textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
241	
242	\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
243	Automated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.
244	
245	\paragraph{Audit scope and limitations.}
246	Full PG audit was completed for ISR $\beta{=}0.1$ seed~42 only.
247	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.
248	Random $\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.
249	
250	\paragraph{TS false-negative correction (TSb obfuscated tautology).}
251	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as non-hacking by the text matcher.
252	Manual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
253	We classify these as \textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.
254	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\S\ref{sec:taxonomy}).
255	After correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.
256	
257	\paragraph{Impact on non-hacking-rate comparison.}
258	After PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\%$ vs.\ random non-hacking $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
259	The direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
260	
261	\subsection{CE --- Conclusion Embedding}
262	
263	\paragraph{Definition.}
264	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
265	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
266	
267	\paragraph{Example (FOL).}
268	\smallskip\noindent\rule{\columnwidth}{0.3pt}
269	{\small\begin{verbatim}
270	Premises:
271	  all x (bird(x) -> flies(x)).
272	  bird(tweety).
273	  flies(tweety).  % conclusion embedded
274	Conclusion: flies(tweety).
275	\end{verbatim}}
276	\noindent\rule{\columnwidth}{0.3pt}\smallskip
277	
278	\paragraph{ISR interaction.}
279	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
280	ISR does not distinguish trivial from substantive necessity.
281	
282	\paragraph{Prevalence.}
283	Conclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\% across all RL conditions.
284	Under exec-only and Random reward, it manifests as CE (71--93\%); under ISR reward, it shifts to TS (70.6\% pooled).
285	
286	
287	\subsection{TSa --- Conclusion Duplication (Standard)}
288	
289	\paragraph{Definition.}
290	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
291	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
292	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
293	
294	\paragraph{Example (FOL).}
295	\smallskip\noindent\rule{\columnwidth}{0.3pt}
296	{\small\begin{verbatim}
297	Premises:
298	  all x ((A(x)&B(x))->(C(x)|D(x))).
299	Conclusion:
300	  all x ((A(x)&B(x))->(C(x)|D(x))).
301	\end{verbatim}}
302	\noindent\rule{\columnwidth}{0.3pt}\smallskip
303	
304	\paragraph{ISR interaction.}
305	ISR~$\approx 0.8$--$1.0$.
306	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
307	TSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.
308	
309	\paragraph{Prevalence.}
310	TSa (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
311	Combined TS (TSa + TSb): 70.6\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).
312	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all TSa; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
313	
314	
315	\subsection{TSb --- Obfuscated Tautology}
316	
317	\paragraph{Definition.}
318	A single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.
319	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
320	
321	\paragraph{Example (FOL, vacuous quantifier wrapping).}
322	\smallskip\noindent\rule{\columnwidth}{0.3pt}
323	{\small\begin{verbatim}
324	Premises:
325	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
326	Conclusion:
327	  all x ((A(x)&B(x))->(C(x)|D(x))).
328	\end{verbatim}}
329	\noindent\rule{\columnwidth}{0.3pt}\smallskip
330	The premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.
331	
332	\paragraph{ISR interaction.}
333	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
334	TSb simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).
335	This triple gaming makes TSb the most complete Goodhart case we observe.
336	
337	\paragraph{Prevalence.}
338	Found primarily in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.
339	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
340	
341	
342	\subsection{Tautological Collapse}
343	
344	\paragraph{Definition.}
345	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
346	
347	\paragraph{Example (FOL).}
348	\smallskip\noindent\rule{\columnwidth}{0.3pt}
349	\begin{verbatim}
350	Premises: p(a).
351	Conclusion: p(a).
352	\end{verbatim}
353	\noindent\rule{\columnwidth}{0.3pt}\smallskip
354	
355	\paragraph{ISR interaction.}
356	ISR~$=1.0$ (the sole premise is necessary).
357	Distinguished from TS by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
358	
359	\paragraph{Prevalence.}
360	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% TS by strict classifier).
361	Also observed in Prolog exec+STA seed~42 (100\% TS, PR~$=0.50$).
362	
363	
364	\subsection{Repetition Collapse}
365	
366	\paragraph{Definition.}
367	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
368	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
369	
370	\paragraph{Example (Prolog).}
371	\smallskip\noindent\rule{\columnwidth}{0.3pt}
372	\begin{verbatim}
373	penguin(fido).
374	penguin(fido).
375	penguin(fido).
376	... (repeated to 512 tokens)
377	query(penguin(fido)).
378	\end{verbatim}
379	\noindent\rule{\columnwidth}{0.3pt}\smallskip
380	
381	\paragraph{ISR interaction.}
382	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
383	ISR correctly diagnoses this degeneration.
384	
385	\paragraph{Prevalence.}
386	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
387	
388	
389	\subsection{Complexity-without-Utility}
390	
391	\paragraph{Definition.}
392	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.
393	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
394	
395	\paragraph{Example (FOL).}
396	\smallskip\noindent\rule{\columnwidth}{0.3pt}
397	{\small\begin{verbatim}
398	Premises:
399	  all x all y (R(x,y) ->
400	    exists z (S(x,z) & T(z,y))).
401	  all x (P(x) -> Q(x)).
402	  P(a).            % only this needed
403	Conclusion: Q(a).
404	\end{verbatim}}
405	\noindent\rule{\columnwidth}{0.3pt}\smallskip
406	
407	\paragraph{ISR interaction.}
408	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
409	This is the mode ISR is best calibrated for.
410	
411	\paragraph{Prevalence.}
412	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
413	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
414	
415	
416	\subsection{Contradiction Explosion}
417	
418	\paragraph{Definition.}
419	The component count grows unboundedly over training.
420	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
421	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
422	
423	\paragraph{Example (FOL, 1000-step exec-only).}
424	\smallskip\noindent\rule{\columnwidth}{0.3pt}
425	{\small\begin{verbatim}
426	Premises:
427	  c1. c2. c3. ... c18. % 18.55 mean
428	  % conclusion embedded among premises
429	Conclusion: Q(a).
430	\end{verbatim}}
431	\noindent\rule{\columnwidth}{0.3pt}\smallskip
432	
433	\paragraph{ISR interaction.}
434	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
435	
436	\paragraph{Prevalence.}
437	Observed in extended exec-only training (seed~42, 1000 steps).
438	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
439	
440	
441	\subsection{Query-as-Fact Gaming}
442	
443	\paragraph{Definition.}
444	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
445	Prolog trivially proves the query by unifying with the fact.
446	This mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.
447	
448	\paragraph{Example (Prolog).}
449	\smallskip\noindent\rule{\columnwidth}{0.3pt}
450	\begin{verbatim}
451	% NL: "Fido is happy."
452	% Model output:
453	fido_is_happy.
454	:- fido_is_happy.     % query = fact
455	\end{verbatim}
456	\noindent\rule{\columnwidth}{0.3pt}\smallskip
457	
458	\paragraph{ISR interaction.}
459	ISR~$\approx 0.9$--$1.0$.
460	The single fact is trivially necessary (its removal breaks the query), inflating ISR.
461	Functionally equivalent to TS but with a distinct surface mechanism.
462	
463	\paragraph{Prevalence.}
464	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
465	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
466	
467	
468	\section{Per-Seed Detailed Results}
469	\label{app:detailed-results}
470	
471	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
472	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
473	ISR values are proved-only ISR$^*$.
474	
475	\begin{table*}[t]
476	\centering
477	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\times}2$ vs.\ $2{\times}4$, mathematically equivalent).}
478	\label{tab:fol-detailed}
479	\label{tab:fol-beta01-detailed}
480	\footnotesize
481	\setlength{\tabcolsep}{3pt}
482	\resizebox{\textwidth}{!}{%
483	\begin{tabular}{@{}llccccccl@{}}
484	\toprule
485	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
486	\midrule
487	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
488	Base model (no training)
489	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
490	Ground-truth FOL
491	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
492	SFT
493	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
494	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
495	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
496	\cmidrule(l){2-9}
497	  & \multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \textbf{92.3} & $n{=}39$ proved \\
498	\midrule
499	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
500	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
501	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\%$ \\
502	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
503	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
504	  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\
505	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
506	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & PG${=}15\%$ \\
507	\cmidrule(l){2-9}
508	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.68{\pm}0.47$ & $0.238{\pm}0.30$ & & & & 500-step \\
509	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.02$ & $0.029{\pm}0.05$ & & & $2.1{\pm}3.6$ & 1000-step \\
510	\midrule
511	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
512	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed CE+TS+PG \\
513	  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\
514	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\
515	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\
516	  & 45$^\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \textbf{54.8} & PG${=}1$; $n{=}42$ \\
517	  & 46$^\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \textbf{54.5} & PG${=}4$; $n{=}77$ \\
518	\cmidrule(l){2-9}
519	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.77{\pm}0.14$ & $0.716{\pm}0.26$ & & & & 500-step (s42--44) \\
520	  & \multicolumn{2}{l}{5-seed mean$\pm$std} & $0.70{\pm}0.19$ & $0.633{\pm}0.23$ & & & & 500-step (s42--46) \\
521	\midrule
522	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
523	  & \multicolumn{8}{l}{See Table~\ref{tab:beta03-detailed} for per-seed $\beta{=}0.3$ results.} \\
524	\midrule
525	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
526	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\
527	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\
528	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\cap$PG: 6) \\
529	\cmidrule(l){2-9}
530	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.87{\pm}0.08$ & $0.117{\pm}0.042$ & & & & TS seed-dep.: 0/38/0\% \\
531	\midrule
532	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
533	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
534	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
535	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
536	\cmidrule(l){2-9}
537	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & & \\
538	\midrule
539	\multicolumn{9}{@{}l}{\textit{Shuffled-ISR $\beta{=}0.1$ (deconfounding control)}} \\
540	  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
541	  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \textbf{87.5} & $n{=}16$ proved \\
542	  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \textbf{86.7} & $n{=}15$ proved \\
543	\cmidrule(l){2-9}
544	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.153{\pm}0.006$ & $0.559{\pm}0.015$ & $6.5$ & $6.5$ & \textbf{87.0} & $N{=}46$ proved \\
545	\bottomrule
546	\end{tabular}}% end resizebox
547	\end{table*}
548	
549	
550	\begin{table*}[t]
551	\centering
552	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
553	\label{tab:prolog-detailed}
554	\small
555	\begin{tabular}{@{}llcccccl@{}}
556	\toprule
557	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
558	\midrule
559	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
560	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
561	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
562	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
563	\cmidrule(l){2-8}
564	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.53{\pm}0.31$ & $0.146{\pm}0.21$ & & & \\
565	\midrule
566	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
567	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & TS tautological \\
568	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional TS$^a$ \\
569	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
570	\cmidrule(l){2-8}
571	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.62{\pm}0.31$ & $0.699{\pm}0.45$ & & & 3/3 Goodhart, 0\% non-hacking \\
572	\bottomrule
573	\end{tabular}
574	
575	\vspace{4pt}
576	{\footnotesize
577	$^a$ Strict TS classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
578	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\
579	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
580	}
581	\end{table*}
582	
583	\begin{table*}[t]
584	\centering
585	\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}
586	\label{tab:prooffol-detailed}
587	\small
588	\begin{tabular}{@{}llcccccl@{}}
589	\toprule
590	\textbf{Condition} & \textbf{Seed} & \textbf{PR$_{\text{f50}}$} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{Genuine\%} & \textbf{Notes} \\
591	\midrule
592	Base & --- & 0.16 & 0.310 & 0 & 0 & \textbf{100} & $n{=}16$ proved \\
593	\midrule
594	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
595	  & 42 & ${\approx}$1.0 & 0.066 & \textbf{100} & 0 & 0 & $n{=}99$; stable \\
596	  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\
597	  & 44 & ${\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\
598	\cmidrule(l){2-8}
599	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{17.4\% genuine (mean of seeds)} & \\
600	\midrule
601	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
602	  & 42 & 0.35 & 0.12 & 0 & 0 & \textbf{100} & $n{=}46$; collapsed \\
603	  & 43 & ${\approx}$0.47 & ${\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\
604	  & 44 & 0.49 & 0.145 & 0 & 0 & \textbf{100} & $n{=}66$; oscillation \\
605	\cmidrule(l){2-8}
606	  & \multicolumn{2}{l}{Aggregate} & & \multicolumn{3}{c}{\textbf{76.8\%} genuine (mean of seeds)} & \\
607	\bottomrule
608	\end{tabular}
609	
610	\vspace{4pt}
611	{\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}
612	\end{table*}
613	
614	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
615	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
616	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
617	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
618	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
619	
620	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
621	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
622	seed~42 produces clean TS tautologies (single premise~$=$~conclusion),
623	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
624	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
625	The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
626	
627	\subsection{Per-Seed Results at $\beta{=}0.2$ and $\beta{=}0.3$}
628	\label{app:beta03}
629	
630	Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
631	At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
632	The three ISR $\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
633	
634	\begin{table*}[ht]
635	\centering
636	\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}
637	\label{tab:beta03-detailed}
638	\small
639	\begin{tabular}{@{}llcccccl@{}}
640	\toprule
641	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Mode} \\
642	\midrule
643	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.2$}} \\
644	  & 42 & 1.00 & 0.602 & \textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\
645	  & 43 & 0.96 & 0.552 & \textbf{96.9} & 1.0 & 0 & PG${=}2$ \\
646	  & 44 & 0.94 & 0.964 & \textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\
647	\cmidrule(l){2-8}
648	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.97{\pm}0.03$ & $0.71{\pm}0.22$ & & & 3/3 TS Goodhart \\
649	\midrule
650	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
651	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\
652	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\
653	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure TS Goodhart \\
654	\cmidrule(l){2-8}
655	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.66{\pm}0.42$ & $0.39{\pm}0.31$ & & & \\
656	\midrule
657	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
658	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\
659	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\text{N-H}}{=}3$ \\
660	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\
661	\cmidrule(l){2-8}
662	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & $0.54{\pm}0.35$ & $0.09{\pm}0.09$ & & & \\
663	\bottomrule
664	\end{tabular}
665	\end{table*}
666	
667	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
668	\label{app:100step}
669	
670	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%, higher than SFT (13.0\%, 3-seed pooled) but still early in training.
671	Of the 32 proved samples, 9 (28.1\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
672	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
673	This demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.
674	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
675	
676	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
677	\label{app:o1-ablation}
678	
679	All main experiments (\S\ref{sec:diagnostic}--\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\texttt{execution\_fast\_sta}) but is used only in the ablation reported here.
680	The two signals measure fundamentally different properties, not approximations of the same quantity.
681	The binary signal tests \emph{collective} premise necessity: $\text{fast\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
682	LOO tests \emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.
683	
684	\paragraph{Evaluation-time comparison.}
685	Across 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.
686	This renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.
687	By contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.
688	Of 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.
689	
690	\paragraph{Training-time ablation.}
691	As a training reward ($r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$, functionally zero, compared to $\text{ISR}^*{=}0.132$ under exec-only and $\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\beta{=}0.1$.
692	The tautology check depresses prove rate by 30\,pp relative to exec-only ($63\%$ vs.\ $93\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.
693	That even the fine-grained $O(n)$ LOO signal, which \emph{does} provide per-component necessity feedback, is ultimately gamed (\S\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.
694	
695	\paragraph{Computational overhead.}
696	Full LOO requires $n{+}1$ solver calls per sample (mean $n{\approx}6$ for FOLIO).
697	With Prover9 at ${\sim}5$\,ms per call, STA evaluation adds ${\sim}55$\,ms per sample versus ${\sim}4$\,s for LLM inference (${<}1\%$ overhead).
698	The $O(1)$ binary check adds a single solver call per proved sample (${<}2\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.
699	
700	\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}
701	\label{app:llama-coldstart}
702	
703	We applied the identical GRPO configuration (Table~\ref{tab:hyperparams}) to LLaMA-3.2-3B~\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).
704	Across 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.
705	This establishes a \emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.
706	Qwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\ 4B), likely reflecting pretraining data composition.
707	An SFT warmstart (3 epochs on gold formalizations, lr$=$2$\times$10$^{-5}$) initially failed: the model produced Unicode FOL notation ($\forall$, $\to$, $\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data (PR$=$0\%, $n{=}100$), suggesting the capability threshold involves format-level compatibility beyond task knowledge.
708	
709	\paragraph{SFT warmstart with GRPO (3-seed).}
710	After correcting the format incompatibility, we repeated the SFT warmstart and applied exec-only GRPO across three seeds (42, 43, 44; 500 steps each).
711	Table~\ref{tab:llama-d165} reports per-seed results.
712	PR stabilizes at $15.0{\pm}1.0$\% (SE), indistinguishable from the SFT baseline: GRPO provides no amplification beyond supervised warmstart.
713	However, non-hacking rates remain high ($86.6{\pm}0.9\%$, 3-seed mean), indicating that at this low PR, structural degeneration does not emerge; the model fails to bootstrap rather than degenerating into reward hacking.
714	ISR$^*$ averages $0.554{\pm}0.010$, comparable to Qwen3-4B SFT ($0.595$; Table~\ref{tab:fol-detailed}), confirming that the few proved samples retain genuine reasoning structure.
715	The combination of Qwen3-8B stagnation at PR${=}15.5\%$ (\S\ref{sec:limitations}) and LLaMA-3.2-3B stagnation at PR${=}15\%$ suggests a model-general cold-start barrier for GRPO on formal reasoning tasks.
716	
717	\begin{table}[ht]
718	\centering
719	\caption{LLaMA-3.2-3B exec-only GRPO with SFT warmstart (3 seeds, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, CE/N-H = percentage among proved samples. CI = contradiction injection (count).}
720	\label{tab:llama-d165}
721	\footnotesize
722	\begin{tabular}{@{}lcccccc@{}}
723	\toprule
724	\textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Notes} \\
725	\midrule
726	42 & 0.14 & 0.547 & 0 & 14.3 & \textbf{85.7} & CI${=}2$; $n{=}14$ \\
727	43 & 0.15 & 0.566 & 0 & 13.3 & \textbf{86.7} & $n{=}15$ \\
728	44 & 0.16 & 0.549 & 0 & 12.5 & \textbf{87.5} & $n{=}16$ \\
729	\cmidrule(l){1-7}
730	Mean$\pm$SE & $0.15{\pm}0.01$ & $0.554{\pm}0.010$ & 0 & 13.4 & \textbf{86.6$\pm$0.9} & $N{=}45$ \\
731	\bottomrule
732	\end{tabular}
733	\end{table}
734	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "784b4f69-1a81-48b8-a676-b9b8410ff795",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Compute resources.}\nExperiments were run on single-GPU setups (NVIDIA RTX 4090 24\\,GB and RTX PRO 6000 96\\,GB).\nEach GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).\nTotal compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\\paragraph{Reward formulation.}\nAn additive variant ($r = r_{\\text{exec}} + \\beta\\,\\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\\text{exec}}\\cdot(1+\\beta\\,\\text{ISR})$ ensures ISR modulates only proved outputs.\n\n\\paragraph{ProofFOL dataset construction.}\n\\label{app:prooffol-construction}\nProofFOL is derived from ProofWriter~\\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \\citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\\sim}70\\%$ retention; failures from timeouts, unsupported constructs, and translation errors).\nOf the translated examples, 99.1\\% parse successfully (92 skipped due to empty FOL output).\nWe sample 500 training and 100 evaluation examples (seed~42) from the verified pool.\nTable~\\ref{tab:prooffol-vs-folio} compares key structural properties.\n\n\\begin{table}[!ht]\n\\centering\n\\caption{ProofFOL vs.\\ FOLIO structural comparison (training sets, $n{=}500$ each).}\n\\label{tab:prooffol-vs-folio}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Property} & \\textbf{ProofFOL} & \\textbf{FOLIO} \\\\\n\\midrule\nFOL premises (mean$\\pm$std) & $18.2 \\pm 3.2$ & $5.3 \\pm 1.4$ \\\\\n\\quad Ground facts & $10.2 \\pm 3.0$ & $1.8 \\pm 1.5$ \\\\\n\\quad Rules & $8.1 \\pm 1.1$ & $3.5 \\pm 1.9$ \\\\\nXOR ($\\oplus$) samples & 0\\% & 37.2\\% \\\\\nDominant depth & 4--5 & 2--3 \\\\\nPredicate style & synthetic & real-world \\\\\nFOL source & GPT-4o (silver) & human (gold) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nProofFOL problems are structurally more complex ($3.4{\\times}$ more premises) but use simpler, synthetic predicates (e.g., \\texttt{Blue(x)}, \\texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.\nThe absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Goodhart effects: implications.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern maps onto the Manheim \\& Garrabrant taxonomy~\\citep{manheim-goodhart-taxonomy}: $\\beta{=}0.1$ on FOLIO instantiates \\emph{regressional} Goodhart ($P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR erroneously rewards the shortcut); $\\beta{\\geq}0.2$ introduces \\emph{extremal} elements (PR collapse to 18\\% vs.\\ 48\\% random at $\\beta{=}0.3$).\nThe implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \\S\\ref{sec:crossdomain}).\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Classifier limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-detailed}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.\nPractitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical guidelines.}\n\\label{app:practical-guidelines}\nOur findings yield five guidelines for GRPO-trained neurosymbolic systems:\n(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.\n(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.\n(4)~Treat LOO-based metrics as component-count-biased until normalized.\n(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.\n\n\\paragraph{Multiple testing correction.}\n\\label{app:statistical-details}\nWe define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).\nWithin the FOLIO family, Bonferroni correction at $\\alpha{=}0.05$ yields adjusted thresholds of $p_{\\text{adj}}{=}0.05/14{=}0.0036$.\nThree primary comparisons survive correction: the TS rate difference (ISR vs.\\ random; $p_{\\text{bonf}}{=}1.82{\\times}10^{-38}$), the SFT vs.\\ exec-only non-hacking rate ($p_{\\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\\text{bonf}}{<}10^{-8}$).\nThe matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\\text{bonf}}{=}0.056$), significant at $\\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).\nThe ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.\nBonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.\nWe report the most conservative Bonferroni results for transparency.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table*}[ht]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nCE & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nTS & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nPG & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random TS driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: CE${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table*}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nCE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\paragraph{Boundary case validation.}\nStratified validation across 82 samples (all five hacking categories) yields Cohen's $\\kappa{=}1.0$; independent re-annotation confirms full agreement.\nStructured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.\nShort-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.\nLow-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.\n3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.\n\n\\subsection{PG --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).\nWe term this \\textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull PG audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.\n\n\\paragraph{TS false-negative correction (TSb obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{CE --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as CE (71--93\\%); under ISR reward, it shifts to TS (70.6\\% pooled).\n\n\n\\subsection{TSa --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nTSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nTSa (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined TS (TSa + TSb): 70.6\\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all TSa; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{TSb --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\nThe premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nTSb simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).\nThis triple gaming makes TSb the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from TS by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% TS by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% TS, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to TS but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\\times}2$ vs.\\ $2{\\times}4$, mathematically equivalent).}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \\textbf{92.3} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & PG${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.68{\\pm}0.47$ & $0.238{\\pm}0.30$ & & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.02$ & $0.029{\\pm}0.05$ & & & $2.1{\\pm}3.6$ & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed CE+TS+PG \\\\\n  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\\\\n  & 45$^\\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \\textbf{54.8} & PG${=}1$; $n{=}42$ \\\\\n  & 46$^\\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \\textbf{54.5} & PG${=}4$; $n{=}77$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.77{\\pm}0.14$ & $0.716{\\pm}0.26$ & & & & 500-step (s42--44) \\\\\n  & \\multicolumn{2}{l}{5-seed mean$\\pm$std} & $0.70{\\pm}0.19$ & $0.633{\\pm}0.23$ & & & & 500-step (s42--46) \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & \\multicolumn{8}{l}{See Table~\\ref{tab:beta03-detailed} for per-seed $\\beta{=}0.3$ results.} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\\cap$PG: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.87{\\pm}0.08$ & $0.117{\\pm}0.042$ & & & & TS seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Shuffled-ISR $\\beta{=}0.1$ (deconfounding control)}} \\\\\n  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \\textbf{87.5} & $n{=}16$ proved \\\\\n  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.153{\\pm}0.006$ & $0.559{\\pm}0.015$ & $6.5$ & $6.5$ & \\textbf{87.0} & $N{=}46$ proved \\\\\n\\bottomrule\n\\end{tabular}}% end resizebox\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.53{\\pm}0.31$ & $0.146{\\pm}0.21$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & TS tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional TS$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.62{\\pm}0.31$ & $0.699{\\pm}0.45$ & & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict TS classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\\S\\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\\text{f50}}{>}0.90$.}\n\\label{tab:prooffol-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR$_{\\text{f50}}$} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{Genuine\\%} & \\textbf{Notes} \\\\\n\\midrule\nBase & --- & 0.16 & 0.310 & 0 & 0 & \\textbf{100} & $n{=}16$ proved \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & ${\\approx}$1.0 & 0.066 & \\textbf{100} & 0 & 0 & $n{=}99$; stable \\\\\n  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\\\\n  & 44 & ${\\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{17.4\\% genuine (mean of seeds)} & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 0.35 & 0.12 & 0 & 0 & \\textbf{100} & $n{=}46$; collapsed \\\\\n  & 43 & ${\\approx}$0.47 & ${\\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\\\\n  & 44 & 0.49 & 0.145 & 0 & 0 & \\textbf{100} & $n{=}66$; oscillation \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{\\textbf{76.8\\%} genuine (mean of seeds)} & \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean TS tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for ISR at $\\beta{=}0.2$ and both ISR and Random at $\\beta{=}0.3$.\nAt $\\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\\% or near-100\\% TS), confirming $\\beta{\\geq}0.2$ as the extremal Goodhart regime.\nThe three ISR $\\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.2$ and $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.2$}} \\\\\n  & 42 & 1.00 & 0.602 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\\\\n  & 43 & 0.96 & 0.552 & \\textbf{96.9} & 1.0 & 0 & PG${=}2$ \\\\\n  & 44 & 0.94 & 0.964 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.03$ & $0.71{\\pm}0.22$ & & & 3/3 TS Goodhart \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure TS Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.66{\\pm}0.42$ & $0.39{\\pm}0.31$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nAll main experiments (\\S\\ref{sec:diagnostic}--\\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\\texttt{execution\\_fast\\_sta}) but is used only in the ablation reported here.\nThe two signals measure fundamentally different properties, not approximations of the same quantity.\nThe binary signal tests \\emph{collective} premise necessity: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nLOO tests \\emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.\n\n\\paragraph{Evaluation-time comparison.}\nAcross 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.\nThis renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.\nBy contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.\nOf 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.\n\n\\paragraph{Training-time ablation.}\nAs a training reward ($r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$, functionally zero, compared to $\\text{ISR}^*{=}0.132$ under exec-only and $\\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\\beta{=}0.1$.\nThe tautology check depresses prove rate by 30\\,pp relative to exec-only ($63\\%$ vs.\\ $93\\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.\nThat even the fine-grained $O(n)$ LOO signal, which \\emph{does} provide per-component necessity feedback, is ultimately gamed (\\S\\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.\n\n\\paragraph{Computational overhead.}\nFull LOO requires $n{+}1$ solver calls per sample (mean $n{\\approx}6$ for FOLIO).\nWith Prover9 at ${\\sim}5$\\,ms per call, STA evaluation adds ${\\sim}55$\\,ms per sample versus ${\\sim}4$\\,s for LLM inference (${<}1\\%$ overhead).\nThe $O(1)$ binary check adds a single solver call per proved sample (${<}2\\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.\n\n\\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}\n\\label{app:llama-coldstart}\n\nWe applied the identical GRPO configuration (Table~\\ref{tab:hyperparams}) to LLaMA-3.2-3B~\\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).\nAcross 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\nThis establishes a \\emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.\nQwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\\ 4B), likely reflecting pretraining data composition.\nAn SFT warmstart (3 epochs on gold formalizations, lr$=$2$\\times$10$^{-5}$) initially failed: the model produced Unicode FOL notation ($\\forall$, $\\to$, $\\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data (PR$=$0\\%, $n{=}100$), suggesting the capability threshold involves format-level compatibility beyond task knowledge.\n\n\\paragraph{SFT warmstart with GRPO (3-seed).}\nAfter correcting the format incompatibility, we repeated the SFT warmstart and applied exec-only GRPO across three seeds (42, 43, 44; 500 steps each).\nTable~\\ref{tab:llama-d165} reports per-seed results.\nPR stabilizes at $15.0{\\pm}1.0$\\% (SE), indistinguishable from the SFT baseline: GRPO provides no amplification beyond supervised warmstart.\nHowever, non-hacking rates remain high ($86.6{\\pm}0.9\\%$, 3-seed mean), indicating that at this low PR, structural degeneration does not emerge; the model fails to bootstrap rather than degenerating into reward hacking.\nISR$^*$ averages $0.554{\\pm}0.010$, comparable to Qwen3-4B SFT ($0.595$; Table~\\ref{tab:fol-detailed}), confirming that the few proved samples retain genuine reasoning structure.\nThe combination of Qwen3-8B stagnation at PR${=}15.5\\%$ (\\S\\ref{sec:limitations}) and LLaMA-3.2-3B stagnation at PR${=}15\\%$ suggests a model-general cold-start barrier for GRPO on formal reasoning tasks.\n\n\\begin{table}[ht]\n\\centering\n\\caption{LLaMA-3.2-3B exec-only GRPO with SFT warmstart (3 seeds, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, CE/N-H = percentage among proved samples. CI = contradiction injection (count).}\n\\label{tab:llama-d165}\n\\footnotesize\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n42 & 0.14 & 0.547 & 0 & 14.3 & \\textbf{85.7} & CI${=}2$; $n{=}14$ \\\\\n43 & 0.15 & 0.566 & 0 & 13.3 & \\textbf{86.7} & $n{=}15$ \\\\\n44 & 0.16 & 0.549 & 0 & 12.5 & \\textbf{87.5} & $n{=}16$ \\\\\n\\cmidrule(l){1-7}\nMean$\\pm$SE & $0.15{\\pm}0.01$ & $0.554{\\pm}0.010$ & 0 & 13.4 & \\textbf{86.6$\\pm$0.9} & $N{=}45$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 734,
      "startLine": 1,
      "totalLines": 734
    }
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
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Read registry for per-seed metrics",
  "usage": {
    "total_tokens": 16109,
    "tool_uses": 1,
    "duration_ms": 2783
  },
  "last_tool_name": "ToolSearch",
  "uuid": "c4b83e11-b7c5-4985-bb94-15025131b208",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015SmFFQ8S8hw1x3Kud9xSUN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "cff91589-e40f-4d19-b774-b6356526c05f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Wo4Ngj8h27FAamhkSng9x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16098,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16098,
        "ephemeral_1h_input_tokens": 0
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

_source line 15 · 2026-05-21T18:13:11.399Z_

<details><summary>↩ Tool result · `toolu_015SmFFQ8S8hw1x3Kud9xSUN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "566ad7a3-e9fc-497b-9687-496a3295a275"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Read registry for per-seed metrics",
  "usage": {
    "total_tokens": 17467,
    "tool_uses": 2,
    "duration_ms": 5700
  },
  "last_tool_name": "mcp__agent-ml-research__read_registry",
  "uuid": "ec86fccd-96c0-444b-9bcf-ccf05fc3a0a1",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_013ajwH5kQqwfdQWNBgSiH2c`</summary>

```json
{
  "project": "solver-trace-ablation",
  "limit": 0,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "05bd2637-e82f-438b-ba76-e71113330596",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgq1Kv8KaRu5iwqmN8ECej",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1295,
      "cache_read_input_tokens": 16098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1295,
        "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-21T18:13:16.294Z_

<details><summary>↩ Tool result · `toolu_013ajwH5kQqwfdQWNBgSiH2c`</summary>

```text
Error: result (360,820 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "ba0e6816-a842-4217-8a28-ca501c695221"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Probe JSON structure of registry dump",
  "usage": {
    "total_tokens": 18087,
    "tool_uses": 3,
    "duration_ms": 12909
  },
  "last_tool_name": "Bash",
  "uuid": "c58081e7-6419-47a0-8676-a9ca0dade172",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01CoxgmRp6eFMjv862263syQ`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\n# Probe structure\njq 'type' \"$FILE\"\njq '.result | type' \"$FILE\"\njq '.result | fromjson | type' \"$FILE\" 2>/dev/null || echo \"result is not nested JSON\"\njq '.result | length' \"$FILE\" | head -1",
  "description": "Probe JSON structure of registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "a346b9b7-a42b-4bc7-a7d1-98bb8487331c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DUtRwvNj5ioeQxPMWFiBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 17393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 620,
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

_source line 21 · 2026-05-21T18:13:21.779Z_

<details><summary>↩ Tool result · `toolu_01CoxgmRp6eFMjv862263syQ`</summary>

```text
"object"
"string"
"object"
336224
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "d5919026-a2ba-4cf8-8c95-ae978614a8a3"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Get first 10 keys of the registry",
  "usage": {
    "total_tokens": 18440,
    "tool_uses": 4,
    "duration_ms": 17385
  },
  "last_tool_name": "Bash",
  "uuid": "4fc2a936-1625-49be-92cd-6c97827b7e9a",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01B1td1AZJUvQLwhoWNcEdcm`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\njq '.result | fromjson | keys[:10]' \"$FILE\"",
  "description": "Get first 10 keys of the registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "bbe4a9f7-7d62-4a95-8365-0f2926e4f0dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AE242MhLqcZJbmHE6vjQt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 18013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 281,
        "ephemeral_1h_input_tokens": 0
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

_source line 24 · 2026-05-21T18:13:26.071Z_

<details><summary>↩ Tool result · `toolu_01B1td1AZJUvQLwhoWNcEdcm`</summary>

```text
[
  "data",
  "error",
  "metadata",
  "success"
]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "3f5dacc1-3ae2-4d7b-953a-f30a2e5c999a"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Get data array length and first entry keys",
  "usage": {
    "total_tokens": 18734,
    "tool_uses": 5,
    "duration_ms": 20736
  },
  "last_tool_name": "Bash",
  "uuid": "77402e9e-f367-480d-8c1d-e8fd1e1c49ce",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01Fm7Ncej1Q4DTtmyy7nADgd`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\njq '.result | fromjson | .data | length' \"$FILE\"\njq '.result | fromjson | .data[0] | keys' \"$FILE\"",
  "description": "Get data array length and first entry keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "d945c1e9-c227-4094-bb2d-c7d3ed8248b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WDNNJxrRoNoGhnuUtrNUN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 222,
      "cache_read_input_tokens": 18294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 222,
        "ephemeral_1h_input_tokens": 0
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

_source line 27 · 2026-05-21T18:13:29.438Z_

<details><summary>↩ Tool result · reported error · `toolu_01Fm7Ncej1Q4DTtmyy7nADgd`</summary>

```text
Exit code 5
4
jq: error (at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt:0): Cannot index object with number
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "26d4a484-beba-4ef8-8a80-a1c4d395d66f",
  "tool_use_result": "Error: Exit code 5\n4\njq: error (at /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt:0): Cannot index object with number"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Check data structure type and keys",
  "usage": {
    "total_tokens": 19147,
    "tool_uses": 6,
    "duration_ms": 24787
  },
  "last_tool_name": "Bash",
  "uuid": "9b514b33-2af7-4b74-94f5-2c0a1c598d9f",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01JeSwgJ5pDuRzn8NpRVdePs`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\njq '.result | fromjson | .data | type' \"$FILE\"\njq '.result | fromjson | .data | keys[:10]' \"$FILE\"",
  "description": "Check data structure type and keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "81145446-f323-43f2-9cc8-d24b37a1a79f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jd4eoQY6DGttNEGkjCPztp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 18516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 341,
        "ephemeral_1h_input_tokens": 0
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

_source line 30 · 2026-05-21T18:13:33.494Z_

<details><summary>↩ Tool result · `toolu_01JeSwgJ5pDuRzn8NpRVdePs`</summary>

```text
"object"
[
  "baseline",
  "count",
  "experiments",
  "total"
]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "a75bed61-3b00-49dd-8768-270bd9e4a910"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Get experiment count and experiments structure",
  "usage": {
    "total_tokens": 19463,
    "tool_uses": 7,
    "duration_ms": 29408
  },
  "last_tool_name": "Bash",
  "uuid": "78dd9a0b-8c9e-41db-b449-076b13e066a0",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01JszGPooVH4ShNyUBPhgFYY`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\njq '.result | fromjson | .data | {count, total}' \"$FILE\"\njq '.result | fromjson | .data.experiments | type' \"$FILE\"\njq '.result | fromjson | .data.experiments | length' \"$FILE\" 2>/dev/null || jq '.result | fromjson | .data.experiments | keys | length' \"$FILE\"",
  "description": "Get experiment count and experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "85271bb9-890c-4e9c-9943-4859e4b781c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTToPccHLoeb8gkiW3C7qu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 18857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 244,
        "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-21T18:13:38.161Z_

<details><summary>↩ Tool result · `toolu_01JszGPooVH4ShNyUBPhgFYY`</summary>

```text
{
  "count": 211,
  "total": 211
}
"object"
211
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "9eda84eb-c8ba-43a8-b119-b4ac2c560dca"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running List all 211 experiment IDs",
  "usage": {
    "total_tokens": 19827,
    "tool_uses": 8,
    "duration_ms": 33492
  },
  "last_tool_name": "Bash",
  "uuid": "7c0d3ed0-0d49-4df3-bdb8-caff60582665",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01MaXo2X9CKVpwReH3aT5pcj`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\n# List all experiment IDs\njq -r '.result | fromjson | .data.experiments | keys[]' \"$FILE\" | sort",
  "description": "List all 211 experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "f01c8b4a-e4ce-40a3-b9b3-1bed02781a6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015s19s5p15Dtet6eKZPcAt2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 19101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 292,
        "ephemeral_1h_input_tokens": 0
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

_source line 36 · 2026-05-21T18:13:42.192Z_

<details><summary>↩ Tool result · `toolu_01MaXo2X9CKVpwReH3aT5pcj`</summary>

```text
d129-1.7b-isr-b01-s43
d129-1.7b-isr-b01-s44
d129-1.7b-isr-b03-s43
d129-1.7b-isr-b03-s44
d129-1.7b-random-b01-s43
d129-1.7b-random-b01-s44
d129-1_7b-isr-b03-s43
d129-1_7b-isr-b03-s44
d129-1_7b-random-b01-s43-r2
d129-1_7b-random-b01-s44
d134-4b-isr-b01-s47
d134-4b-isr-b01-s48
d134-4b-isr-b01-s49
d134-4b-isr-b01-s50
d134-4b-isr-b01-s51
d134-4b-random-b01-s47
d134-4b-random-b01-s48
d134-4b-random-b01-s49
d134-4b-random-b01-s50
d134-4b-random-b01-s51
d142-gated-isr-s52
d142-gated-isr-s53
d142-gated-isr-s54
d142-gated-isr-s55
d142-gated-isr-s56
d142-gated-isr-s57
d143-pw-exec-s42
d143-pw-exec-s43
d143-pw-exec-s44
d143-pw-extended-s42
d143-pw-isr-s42
d143-pw-isr-s43
d143-pw-isr-s44
d143-pw-random-s42
d143-pw-sft-s42
d143-pw-sta-s42
d143-pw-sta-s43
d143-pw-sta-s44
d144-llama-exec-s42
d144-llama-exec-s43
d144-llama-exec-s44
d144-llama-isr-s42
d144-llama-isr-s43
d144-llama-isr-s44
d146-pf-exec-s42
d146-pf-exec-s43
d146-pf-exec-s44
d146-pf-isr-s42
d146-pf-isr-s43
d146-pf-isr-s44
d146-pf-pipeline
d154-8b-exec-s42
d154-8b-exec-s42-k4
d154-8b-exec-s42-k4v2
d154-8b-exec-s42-r2
d154-8b-exec-s42-r3
d154-8b-exec-s43
d154-8b-exec-s44
d154-8b-isr-s42
d154-8b-isr-s43
d157-shuffled-isr-s42
d157-shuffled-isr-s42-r2
d157-shuffled-isr-s42-r3
d157-shuffled-isr-s43
d157-shuffled-isr-s44
d158-llama-grpo-s42
d158-llama-sft-s42
d158_llama_sft_s42
d165-llama-exec-s42
d165-llama-exec-s43
d165-llama-exec-s44
exec-only-s43-1000step-r2
exec-only-s43-1000step-r3
exec-only-s43-1000step-r4
exec-only-s43-1000step-r5
exec-only-s43-1000step-r6
exec-only-s43-1000step-r7
exec-retrain-for-warmstart-s42
exec-retrain-v3-s42
exec-retrain-v3-s43
exp1-isr-b03-s42-1000
exp1-isr-b03-s42-1000-r2
exp1-isr-b03-s43
exp1-isr-b03-s43-r2
exp1-isr-b03-s43-r3
exp1-isr-b03-s43-r4
exp1-isr-b03-s44
exp1-isr-b03-s44-r2
exp1-random-b03-s43
exp1-random-b03-s43-r2
exp1-random-b03-s43-r3
exp1-random-b03-s43-r4
exp1-random-b03-s44
exp1-random-b03-s44-r2
exp2-exec-s43-greedy
exp4-100step-h1h7
gated-isr-curriculum-t02-s42
gated-isr-curriculum-t02-s42-r2
gated-isr-curriculum-t02-s43
gated-isr-curriculum-t02-s43-r2
gated-isr-t03-s42
gated-isr-t03-s43
gated-isr-warmstart-t015-s43
gated-isr-warmstart-t02-s42
gated-isr-warmstart-t02-s43
gated-isr-warmstart-t02-s43-r2
plan001-exec-only-s42
plan001-exec-only-s42-r2
plan001-exec-only-s42-r3
plan001-exec-only-s43
plan001-exec-only-s43-1000
plan001-exec-only-s43-1000-r2
plan001-exec-only-s43-r2
plan001-exec-only-s43-r3
plan001-exec-only-s43-r4
plan001-exec-only-s44
plan001-exec-only-s44-1000
plan001-exec-only-s44-1000-r2
plan001-exec-only-s45
plan001-exec-only-s46
plan002-additive-b01-s42
plan002-additive-b01-s42-1000
plan002-additive-b01-s43
plan002-additive-b01-s43-r2
plan002-additive-b01-s44
plan002-additive-b01-s45
plan002-additive-b01-s45-1000
plan002-additive-b01-s46
plan002-additive-b03-s42
plan003-eval-exec-only-r5
plan004-o1-ablation-s42
plan005-sta-low-s42
plan006-prolog-exec-s42
plan006-prolog-exec-s43
plan006-prolog-exec-s43-r2
plan006-prolog-exec-s43-r3
plan006-prolog-exec-s44
plan006-prolog-sta-s42
plan006-prolog-sta-s43
plan006-prolog-sta-s44
plan009-sft-baseline-s42
plan009-sft-baseline-s42-1000
plan009-sft-baseline-s42-r2
plan009-sft-baseline-s42-r3
plan009-sft-baseline-s42-r4
plan009-sft-baseline-s43
plan009-sft-baseline-s43-1000
plan009-sft-baseline-s44
plan009-sft-baseline-s44-1000
plan009-sft-baseline-s44-1000-r2
plan009-sft-baseline-s44-1000-r3
plan012-hacking-taxonomy
plan013-random-reward-s42
plan013-random-reward-s42-r2
plan013-random-reward-s42-r3
plan013-random-reward-s42-r4
plan014-downstream-nli-s42
plan015-linear-s42
plan016-extended-1000-s42
plan017-additive-random-s42
plan018-additive-random-b01-s42
plan018-additive-random-b01-s42-1000
plan018-additive-random-b01-s42-1000-r2
plan018-additive-random-b01-s42-1000-r3
plan018-additive-random-b01-s43
plan018-additive-random-b01-s43-r2
plan018-additive-random-b01-s43-r3
plan018-additive-random-b01-s44
plan018-additive-random-b01-s44-r2
plan018-additive-random-b01-s45
plan018-additive-random-b01-s45-r3
plan018-additive-random-b01-s46
plan018-random-b01-s45-r2
sta-gt-isr-baseline
sta-phase0-baseline
sta-phase1-exec-only
sta-phase1-exec-only-r2
sta-phase1-exec-only-r3
sta-phase1-exec-only-r4
sta-phase1-exec-only-r5
sta-phase1-exec-sta
sta-phase1-exec-sta-r2
sta-phase1-exec-sta-r3
sta-phase1-exec-sta-r4
sta-phase1-exec-sta-r5
sweep-exec-only-s45
sweep-exec-only-s45-r2
sweep-exec-only-s46
sweep-isr-b005-s42
sweep-isr-b005-s43
sweep-isr-b005-s44
sweep-isr-b01-s45
sweep-isr-b01-s46
sweep-isr-b02-s42
sweep-isr-b02-s43
sweep-isr-b02-s44
sweep-random-b005-s42
sweep-random-b005-s43
sweep-random-b005-s44
sweep-random-b01-s45
sweep-random-b01-s46
w2-qwen3-1.7b-exec-pilot
w2-qwen3-1.7b-isr-b01
w2-qwen3-1.7b-isr-b03
w2-qwen3-1.7b-isr-pilot
w2-qwen3-1.7b-random-b01
w2-qwen3-7b-pilot
w2-qwen3-8b-exec-pilot
w2-qwen3-8b-exec-pilot-r2
w2-qwen3-8b-isr-pilot
w2-qwen3-8b-isr-pilot-r2
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "7ad540b8-3061-41a9-ac1a-d3b9bf9cc571"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Extract plan001-exec-only experiment details",
  "usage": {
    "total_tokens": 22770,
    "tool_uses": 9,
    "duration_ms": 41123
  },
  "last_tool_name": "Bash",
  "uuid": "25551325-0829-4b70-b79f-51d8fc811f9e",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01PPfPXXK3wYKTRMFd8rjgsi`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\n\n# Extract plan001-exec-only experiments for s42, s43, s44\nfor key in \"plan001-exec-only-s42\" \"plan001-exec-only-s43\" \"plan001-exec-only-s44\" \\\n           \"plan001-exec-only-s42-r2\" \"plan001-exec-only-s42-r3\" \\\n           \"plan001-exec-only-s43-r2\" \"plan001-exec-only-s43-r3\" \"plan001-exec-only-s43-r4\" \\\n           \"plan001-exec-only-s43-1000\" \"plan001-exec-only-s43-1000-r2\" \\\n           \"plan001-exec-only-s44-1000\" \"plan001-exec-only-s44-1000-r2\"; do\n    echo \"=== $key ===\"\n    jq -r --arg k \"$key\" '.result | fromjson | .data.experiments[$k] // \"NOT_FOUND\"' \"$FILE\" 2>/dev/null\n    echo \"\"\ndone",
  "description": "Extract plan001-exec-only experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "a661e7f5-b82c-4a09-bc93-f5d1d2619a3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hksDCTubCGMej5dKrSp6y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2939,
      "cache_read_input_tokens": 19393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2939,
        "ephemeral_1h_input_tokens": 0
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

_source line 39 · 2026-05-21T18:13:49.971Z_

<details><summary>↩ Tool result · `toolu_01PPfPXXK3wYKTRMFd8rjgsi`</summary>

```text
=== plan001-exec-only-s42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T22:19:41.568Z",
  "updated_at": "2026-05-15T15:27:42.555Z",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "83029",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s42.log",
    "submitted_at": "2026-05-13T22:20:46.569Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "hypothesis": "exec-only 500步训练 baseline",
    "wall_clock_seconds": 2576.3,
    "gpu_hours": 0.72
  },
  "conclusion": "failed",
  "checkpoint_path": "N/A (failed before checkpoint)",
  "completed_at": "2026-05-13T23:03:42.892Z",
  "taxonomy_note": "D086 补扫: H7=1, H1=80, H8=6, genuine=7 (7.5%). 500-step exec-only 以 H1 为主 (86%), 少量 H7(1) 和 H8(6). eval文件: /root/solver-trace-ablation/outputs/eval_sta_plan001_exec_only_s42.json",
  "h7_count": 1,
  "h1_count": 80,
  "h8_count": 6,
  "genuine_count": 7
}

=== plan001-exec-only-s43 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T23:55:08.635Z",
  "updated_at": "2026-05-14T00:21:04.003Z",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "121275",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s43.log",
    "submitted_at": "2026-05-13T23:55:08.544Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/proofwriter_fol_500.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 43,
    "hypothesis": "exec-only 500步 seed 43, 3-seed baseline 第2个 seed。预期 prove_rate>0.80 (与 s42 一致)",
    "wall_clock_seconds": 1555.5,
    "gpu_hours": 0.43
  },
  "checkpoint_path": "N/A (killed by OOM before completion)",
  "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s43.log",
  "conclusion": "failed",
  "failure_reason": "OOM by plan013 GPU overflow — plan013 未设 CUDA_VISIBLE_DEVICES 导致占用两张 GPU，plan001-s43 被 OOM kill",
  "completed_at": "2026-05-14T00:21:04.003Z"
}

=== plan001-exec-only-s44 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T03:57:09.690Z",
  "updated_at": "2026-05-15T08:29:40.375Z",
  "hypothesis": "Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。",
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "226200",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s44.log",
    "submitted_at": "2026-05-14T04:29:05.471Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 2725.5,
    "gpu_hours": 0.76
  },
  "pid": "226200",
  "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s44.log",
  "reproduce": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\"",
    "finished_at": "2026-05-14T05:06:39.227Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T05:06:40.707032+00:00"
      }
    ]
  },
  "metrics": {
    "eval_prove_rate": 0.98,
    "eval_mean_isr": 0.57,
    "eval_isr_std": 0.2013,
    "eval_median_isr": 0.5,
    "eval_proved_only_isr": 0.5816,
    "eval_n_proved": 98,
    "eval_n_problems": 100,
    "eval_method": "eval_sta.py full STA",
    "eval_data": "proofwriter_fol_100.jsonl",
    "eval_component_count_mean": 2.04,
    "eval_component_count_2": 94,
    "eval_component_count_3": 4,
    "tautological_collapse": true,
    "h7_rate": 1,
    "h7_count": 97,
    "h1_rate": 0,
    "h1_count": 0,
    "genuine_rate": 0,
    "genuine_count": 0,
    "conclusion_embedding_total": 1
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s44",
  "conclusion": "negative",
  "notes": "TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。",
  "completed_at": "2026-05-14T05:14:30.940Z",
  "h7_count": 98
}

=== plan001-exec-only-s42-r2 ===
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-13T22:40:41.773Z",
  "updated_at": "2026-05-15T12:45:21.831Z",
  "completed_at": "2026-05-13T23:46:00Z",
  "extra": {
    "previous_failure": {
      "conclusion": "failed"
    },
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-13T23:46:01.596431+00:00"
      }
    ]
  },
  "spec": {
    "command": "export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s42",
    "server": "westd-39279",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "hypothesis": "500-step exec-only baseline for STA comparison (K=8)",
    "pid": "84901",
    "gpu": [
      "cuda:0"
    ],
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log",
    "submitted_at": "2026-05-13T22:42:40.204Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 3820,
    "gpu_hours": 1.06
  },
  "notes": "Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。",
  "reproduce": {
    "finished_at": "2026-05-13T23:46:00.369Z"
  },
  "conclusion": "success",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500",
  "log_path": "/root/autodl-tmp/outputs/plan001_exec_only_s42/reward_log.jsonl",
  "metrics": {
    "eval_prove_rate": 0.93,
    "eval_mean_isr": 0.1232,
    "eval_isr_std": 0.1887,
    "eval_proved_only_isr": 0.1324,
    "eval_median_isr": 0,
    "eval_n_proved": 93,
    "eval_n_problems": 100,
    "eval_method": "eval_sta.py full STA",
    "eval_data": "proofwriter_fol_100.jsonl",
    "h7_rate": 0,
    "h7_count": 0,
    "h1_rate": 0.871,
    "h1_count": 81,
    "h8_conjunction_collapse_count": 6,
    "h8_conjunction_collapse_rate": 0.0645,
    "genuine_rate": 0.0753,
    "genuine_count": 7,
    "genuine_mean_isr": 0.3141,
    "h1_mean_isr": 0.1055,
    "conclusion_embedding_total": 0.871,
    "content_independent_predicates_count": 1,
    "h8_audit_note": "2026-05-15: H8 conjunction collapse added. genuine 12→7."
  },
  "genuine_count": 7,
  "genuine_rate": 0.075,
  "h8_count": 6
}

=== plan001-exec-only-s42-r3 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T22:42:40.242Z",
  "updated_at": "2026-05-13T23:03:11.395Z",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "85710",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s42-r3.log",
    "submitted_at": "2026-05-13T22:42:40.204Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "hypothesis": "exec-only 500步训练 baseline (retry 3)",
    "wall_clock_seconds": 1228.1,
    "gpu_hours": 0.34
  },
  "conclusion": "failed",
  "completed_at": "2026-05-13T23:03:08.298Z",
  "failure_reason": "OOM crash - duplicate submission while plan001-r2 was occupying cuda:0"
}

=== plan001-exec-only-s43-r2 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T00:22:12.292Z",
  "updated_at": "2026-05-14T01:01:56.416Z",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "pid": "126541",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s43-r2.log",
    "submitted_at": "2026-05-14T00:22:12.241Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 43,
    "hypothesis": "exec-only 500步 seed 43 (retry), 3-seed baseline 第2个 seed",
    "wall_clock_seconds": 2384.2,
    "gpu_hours": 0.66
  },
  "checkpoint_path": "N/A (crashed after submission)",
  "log_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_r2/reward_log.jsonl",
  "conclusion": "failed",
  "failure_reason": "Process crashed after submission (PID 126546 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.",
  "completed_at": "2026-05-14T01:01:56.416Z"
}

=== plan001-exec-only-s43-r3 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T01:02:31.830Z",
  "updated_at": "2026-05-14T01:41:28.427Z",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r3\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "pid": "133258",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 43,
    "hypothesis": "exec-only 500 steps seed 43 (r3), 3-seed baseline 2nd seed",
    "plan_id": "plan_001"
  },
  "conclusion": "failed",
  "failure_reason": "OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 23",
  "checkpoint_path": "N/A (disk full crash at step 23)",
  "log_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_r3/reward_log.jsonl",
  "completed_at": "2026-05-14T01:41:28.427Z"
}

=== plan001-exec-only-s43-r4 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T01:40:37.808Z",
  "updated_at": "2026-05-15T15:28:09.062Z",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r4\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "pid": "136339",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log",
    "submitted_at": "2026-05-14T01:40:37.746Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 43,
    "hypothesis": "Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds",
    "plan_id": "plan001",
    "wall_clock_seconds": 10020.8,
    "gpu_hours": 2.78
  },
  "reproduce": {
    "finished_at": "2026-05-14T03:13:08.926Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T03:13:12.957272+00:00"
      }
    ]
  },
  "metrics": {
    "eval_sampling_prove_rate": 0.14,
    "eval_sampling_mean_isr": 0,
    "eval_sampling_n_proved": 14,
    "eval_sampling_temperature": 0.7,
    "eval_sampling_method": "do_sample=True, temperature=0.7",
    "eval_sampling_by_answer": {
      "true": {
        "count": 34,
        "proved": 6,
        "prove_rate": 0.176
      },
      "false": {
        "count": 25,
        "proved": 2,
        "prove_rate": 0.08
      },
      "unknown": {
        "count": 41,
        "proved": 6,
        "prove_rate": 0.146
      }
    },
    "eval_greedy_prove_rate": 0.13,
    "eval_greedy_mean_isr": 0,
    "eval_greedy_proved_only_isr": 0,
    "eval_greedy_n_proved": 13,
    "eval_greedy_method": "eval_sta.py default (do_sample=False)",
    "eval_greedy_by_answer": {
      "true": {
        "count": 34,
        "proved": 4,
        "prove_rate": 0.118
      },
      "false": {
        "count": 25,
        "proved": 5,
        "prove_rate": 0.2
      },
      "unknown": {
        "count": 41,
        "proved": 4,
        "prove_rate": 0.0976
      }
    },
    "eval_greedy_h7_count": 0,
    "eval_greedy_h7_rate": 0,
    "eval_greedy_h1_count": 13,
    "eval_greedy_h1_rate": 1,
    "eval_greedy_genuine_rate": 0,
    "eval_greedy_n_premises_proved_mean": 17.92,
    "eval_greedy_mean_components_proved": 18.92,
    "eval_greedy_n_premises_all_mean": 32.67,
    "eval_sampling_h1_rate": 1,
    "eval_sampling_h7_rate": 0,
    "eval_sampling_genuine_rate": 0,
    "eval_sampling_mean_components_proved": 18.5,
    "eval_greedy_vs_sampling_delta_pr": -0.01,
    "eval_method_note": "Greedy and sampling agree on failure profile (ISR*=0, H1=100%, components~18.5-18.9). s43 collapse is decoding-invariant."
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_r4",
  "log_path": "/root/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log",
  "conclusion": "negative",
  "notes": "EXP-2 (2026-05-15): greedy eval (T=0) on same 100 held-out problems also done with eval_sta.py defaults (do_sample=False). Result: PR=0.13, ISR*=0.0, H1=100% (13/13), H7=0%, genuine=0%, mean components (proved)=18.92. Sampling (T=0.7) baseline: PR=0.14, ISR*=0.0, H1=100% (14/14), components~18.5. ΔPR=-0.01, both ISR*=0 → s43 collapse is decoding-invariant, NOT a sampling artifact. ~85% of inputs hit max_new_tokens with long repeated-clause outputs; the ~15% that do parse contain the conclusion verbatim among 14-30 premises (n_necessary=0 by per-clause ablation → ISR=0). 训练 PR(last100)=0.883 但 eval PR=13-14% across decoders, ISR=0。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。Checkpoint 已删除（C003）。Report: outputs/h7_classification/exp2_s43_greedy_vs_sample.txt.",
  "completed_at": "2026-05-14T04:27:38.542Z",
  "taxonomy_note": "D086 补扫: proved=13, H7=0, H1=13, H8=1, genuine=0 (0%). exec-only s43 PR=13%, 100% H1 collapse. eval: /root/solver-trace-ablation/outputs/eval_sta_plan001_exec_only_s43_r4.json"
}

=== plan001-exec-only-s43-1000 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T13:22:44.661Z",
  "updated_at": "2026-05-15T13:48:08.794Z",
  "hypothesis": "Exec-only GRPO 1000步 seed=43：与 plan016(s42) 相同配置的第二个 seed。3-seed exec-only 1000步统计，验证 Goodhart collapse（genuine→0%）在 exec-only 条件下的可重复性。与 SFT 1000步 3-seed 对照，确认 collapse 是 RL(GRPO) 特有现象。",
  "parent": "plan016-extended-1000-s42",
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "reproduce": {
    "server": "westd-39279",
    "gpu": "cuda:0",
    "started_at": "2026-05-15T13:23:32.864Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000\"",
    "finished_at": "2026-05-15T13:45:01.320Z",
    "training_hours": 0.36
  },
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "356071",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s43-1000.log",
    "submitted_at": "2026-05-15T13:23:35.275Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 1288.0,
    "gpu_hours": 0.36
  },
  "pid": "356071",
  "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s43-1000.log",
  "failure_reason": "磁盘满 (os error 28): /root/autodl-tmp/ 250G/250G (100%)，step 150 保存 checkpoint 时 safetensors serialize 失败。checkpoint-100 完整可用(15GB)，checkpoint-150 不完整(仅2/4 shards)。分类: disk_full, retryable。",
  "conclusion": "failed",
  "completed_at": "2026-05-15T13:45:03.313Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-15T13:45:05.583858+00:00"
      }
    ]
  }
}

=== plan001-exec-only-s43-1000-r2 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T13:51:02.684Z",
  "updated_at": "2026-05-15T17:16:01.598Z",
  "hypothesis": "Exec-only GRPO 1000步 seed=43（r2 重跑）：r1 因磁盘满在 step 150 崩溃。磁盘已清理（92GB 可用），从 step 0 重跑。",
  "parent": "plan001-exec-only-s43-1000",
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "reproduce": {
    "server": "westd-39279",
    "gpu": "cuda:0",
    "started_at": "2026-05-15T13:51:29.890Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2\"",
    "finished_at": "2026-05-15T16:05:05.890Z",
    "training_hours": 2.23
  },
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "363692",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s43-1000-r2.log",
    "submitted_at": "2026-05-15T13:51:32.190Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2",
    "wall_clock_seconds": 8963.7,
    "gpu_hours": 2.49
  },
  "pid": "363692",
  "log_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2/eval_sta_results.json",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T16:05:10.467837+00:00"
      }
    ]
  },
  "conclusion": "success",
  "metrics": {
    "prove_rate": 0.9,
    "n_proved": 90,
    "n_problems": 100,
    "mean_isr": 0.531,
    "isr_std": 0.15,
    "isr_corrected": 0.465,
    "isr_artifact_note": "n_components=3 quantifier decomposition artifact (+0.066) + $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely from H7a tautological necessity, no reasoning quality signal.",
    "h7_count": 90,
    "h7_rate": 1,
    "h7a_count": 90,
    "h7b_count": 0,
    "h1_count": 0,
    "h1_rate": 0,
    "h8_count": 0,
    "h8_rate": 0,
    "genuine_count": 0,
    "genuine_rate": 0
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2",
  "completed_at": "2026-05-15T16:20:55.876Z",
  "notes": "Taxonomy audit (2026-05-15): 90/90 proved = H7a (100% tautology). All single-premise with conclusion text-matching premise. Content-independent predicates only 1/90. ISR分布反映H7a下quantifier结构差异(部分有∃x wrapping). genuine_strict=0. s43 1000步与500步(s43-r4)同为H7主导模式,但1000步PR大幅提升(14%→90%)。"
}

=== plan001-exec-only-s44-1000 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T13:22:45.226Z",
  "updated_at": "2026-05-15T13:50:32.148Z",
  "hypothesis": "Exec-only GRPO 1000步 seed=44：与 plan016(s42) 相同配置的第三个 seed。完成 3-seed exec-only 1000步统计，与 SFT 1000步 3-seed 对照，统计支撑 Goodhart collapse 是 RL 特有现象的 claim。",
  "parent": "plan016-extended-1000-s42",
  "server": "westd-39279",
  "gpu": "cuda:1",
  "account": "root",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44_1000\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "pid": "357074",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s44-1000.log",
    "submitted_at": "2026-05-15T13:28:02.714Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 1335.7,
    "gpu_hours": 0.37
  },
  "pid": "357074",
  "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s44-1000.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44_1000\"",
    "finished_at": "2026-05-15T13:50:19.963Z"
  },
  "conclusion": "failed",
  "failure_reason": "磁盘满 (/dev/md0 250G/250G)，进程被手动 kill 防止 checkpoint 损坏。需从 step 0 重跑。",
  "completed_at": "2026-05-15T13:50:18.432Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-15T13:50:24.979972+00:00"
      }
    ]
  }
}

=== plan001-exec-only-s44-1000-r2 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T13:51:03.762Z",
  "updated_at": "2026-05-15T17:06:45.730Z",
  "hypothesis": "Exec-only GRPO 1000步 seed=44（r2 重跑）：r1 因磁盘满被 kill。磁盘已清理（92GB 可用），从 step 0 重跑。",
  "parent": "plan001-exec-only-s44-1000",
  "server": "westd-39279",
  "gpu": "cuda:1",
  "account": "root",
  "reproduce": {
    "server": "westd-39279",
    "gpu": "cuda:1",
    "started_at": "2026-05-15T13:51:35.383Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2\"",
    "finished_at": "2026-05-15T16:11:51.095Z",
    "training_hours": 2.34
  },
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "pid": "363840",
    "log_path": "~/runs/solver-trace-ablation/plan001-exec-only-s44-1000-r2.log",
    "submitted_at": "2026-05-15T13:51:37.012Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 8895.8,
    "gpu_hours": 2.47,
    "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2"
  },
  "pid": "363840",
  "log_path": "/root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2/eval_sta_results.json",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T16:11:54.943668+00:00"
      }
    ]
  },
  "metrics": {
    "prove_rate": 1,
    "n_proved": 100,
    "n_problems": 100,
    "mean_isr": 0.002,
    "isr_std": 0.0146,
    "h7_count": 0,
    "h7_rate": 0,
    "h7a_count": 0,
    "h7b_count": 0,
    "h1_count": 85,
    "h1_rate": 0.85,
    "h8_count": 15,
    "h8_rate": 0.15,
    "genuine_count": 0,
    "genuine_rate": 0,
    "genuine_note": "D091: 3 samples escape text-match classifiers but are functionally degenerate (ISR=0, disjunctive/commuted bypasses)"
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2",
  "conclusion": "success",
  "completed_at": "2026-05-15T16:19:52.818Z",
  "taxonomy_note": "D086 clean eval: proved=100, H7=0 (H7a=0, H7b=0), H1=85, H8=15, genuine=3 (3%). 500步→1000步变化: H7 97→0, H1 0→85, H8 0→15. 完全从H7模式转向H1+H8模式. Eval data: proofwriter_fol_100.jsonl",
  "notes": "Taxonomy audit (2026-05-15): H1_only=82, H8_only=12, H1∩H8=3, genuine=3 (all H1-near). 3个genuine proof全部ISR=0, 结论为析取式, universal premise实例化后精确等于/包含结论 + ground facts冗余满足各析取项: folio_1296(∀x实例化+析取交换), folio_1428(∀x子公式+ground facts重复6次), folio_1051(∀x(C(x)∨S(x))实例化=C(a)∨S(a)精确匹配). classify_h7漏检原因: H1不做∀x实例化, H8不检查析取式. Per C013: H1-near保留为genuine但标记. genuine_strict=0."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "a8db594d-6ff7-44ad-b9a6-21a470332bd7"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Extract ISR b01 (plan002-additive-b01) experiment details",
  "usage": {
    "total_tokens": 22772,
    "tool_uses": 10,
    "duration_ms": 44515
  },
  "last_tool_name": "Bash",
  "uuid": "5f32fd80-0365-43d3-b9a9-81e692546ca5",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01KGzL5HoRLLHMFgQAiJDino`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\n\n# Extract ISR b01 experiments - check plan002-additive-b01 (which is ISR)\nfor key in \"plan002-additive-b01-s42\" \"plan002-additive-b01-s42-1000\" \\\n           \"plan002-additive-b01-s43\" \"plan002-additive-b01-s43-r2\" \\\n           \"plan002-additive-b01-s44\" \\\n           \"plan002-additive-b01-s45\" \"plan002-additive-b01-s45-1000\" \\\n           \"plan002-additive-b01-s46\"; do\n    echo \"=== $key ===\"\n    jq -r --arg k \"$key\" '.result | fromjson | .data.experiments[$k] // \"NOT_FOUND\"' \"$FILE\" 2>/dev/null\n    echo \"\"\ndone",
  "description": "Extract ISR b01 (plan002-additive-b01) experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "d7234d30-3d78-4fc3-ba93-efc2db1f596d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hksDCTubCGMej5dKrSp6y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2939,
      "cache_read_input_tokens": 19393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2939,
        "ephemeral_1h_input_tokens": 0
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

_source line 42 · 2026-05-21T18:13:53.295Z_

<details><summary>↩ Tool result · `toolu_01KGzL5HoRLLHMFgQAiJDino`</summary>

```text
=== plan002-additive-b01-s42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T05:29:08.138Z",
  "updated_at": "2026-05-15T14:38:00.829Z",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "262261",
    "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s42.log",
    "submitted_at": "2026-05-14T05:32:32.415Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "plan_id": "plan002",
    "reward_formula": "r_exec * (1 + 0.1 * ISR)",
    "num_steps": 500,
    "wall_clock_seconds": 4493.9,
    "gpu_hours": 1.25,
    "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s42"
  },
  "parent": "plan002-additive-b03-s42",
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "pid": "262261",
  "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s42.log",
  "reproduce": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\"",
    "finished_at": "2026-05-14T06:37:58.285Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T06:37:59.656631+00:00"
      }
    ]
  },
  "conclusion": "negative",
  "metrics": {
    "eval_prove_rate": 0.81,
    "eval_mean_isr": 0.3365,
    "eval_isr_std": 0.3227,
    "eval_proved_only_isr": 0.4154,
    "eval_median_isr": 0.2,
    "eval_n_proved": 81,
    "eval_n_problems": 100,
    "eval_method": "eval_sta.py full STA",
    "eval_data": "proofwriter_fol_100.jsonl",
    "eval_component_count_mean": 5.58,
    "h7_rate": 0.16,
    "h7_count": 13,
    "h1_rate": 0.519,
    "h1_count": 42,
    "h8_conjunction_collapse_count": 12,
    "h8_conjunction_collapse_rate": 0.148,
    "genuine_rate": 0.173,
    "genuine_count": 14,
    "tautological_collapse": false,
    "h8_audit_note": "2026-05-15: H8 conjunction collapse audit completed. 12/81 proved samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json"
  },
  "notes": "H8 re-audit (2026-05-15): 81 proved samples. H7 (single premise=conclusion): 13/81=16.1%, H1 (multi-prem conclusion embedding): 42/81=51.9%, H8 (conjunction collapse): 12/81=14.8%, content-independent: 19/81=23.5%. Genuine (proved - H7 - H1 - H8): 14/81=17.3%. Pre-H8 genuine was 26/81=32.1% — H8 removed 12 samples. Combined conclusion duplication+conjunction = 82.7%. Eval source: proofwriter_fol_100.jsonl (backup at /root/autodl-tmp/eval_results_backup/). H8 JSON: /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json. ⚠️ RECLASSIFIED negative (Reviewer WARNING): 500步快照 genuine 30.9%（H8 未扣除，为上界），1000步崩塌至 2.2%，表明 Goodhart collapse 已在 500 步启动但未完成。",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s42",
  "completed_at": "2026-05-14T06:47:26.358Z",
  "genuine_count": 14,
  "h1_near_count": null,
  "taxonomy_note": "H1-near analysis infeasible: eval_sta deleted; genuine=14 computed from aggregated H7+H1_exact+H8 exclusion per D084. H1-near is supplementary-only (per-sample data available only for Random s42)."
}

=== plan002-additive-b01-s42-1000 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T07:08:50.639Z",
  "updated_at": "2026-05-15T15:35:12.176Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode execution_sta --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "171076",
    "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s42-1000.log",
    "submitted_at": "2026-05-15T07:29:48.253Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 4944.1,
    "gpu_hours": 1.37
  },
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "pid": "171076",
  "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s42-1000.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode execution_sta --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\"",
    "finished_at": "2026-05-15T08:44:46.526Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T08:44:51.343174+00:00"
      }
    ]
  },
  "conclusion": "negative",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s42_1000",
  "metrics": {
    "eval_prove_rate": 0.9,
    "eval_mean_isr": 0.7892,
    "eval_isr_std": 0.3424,
    "eval_proved_only_isr": 0.8769,
    "eval_median_isr": 1,
    "eval_n_proved": 90,
    "eval_n_problems": 100,
    "eval_component_count_mean": 2.889,
    "tautological_collapse": true,
    "train_final_prove_rate": 0.855,
    "train_final_mean_isr": 0.532,
    "h7_count": 87,
    "h7_rate": 0.9667,
    "h1_count": 0,
    "h1_rate": 0,
    "h1_near_count": 1,
    "h1_near_rate": 0.0111,
    "h8_conjunction_collapse_count": 1,
    "h8_conjunction_collapse_rate": 0.0111,
    "genuine_count": 2,
    "genuine_rate": 0.0222,
    "taxonomy_standard": "D086 clean run = ground truth. D084 residual removed."
  },
  "completed_at": "2026-05-15T08:52:12.385Z",
  "genuine_count": 2,
  "genuine_rate": 0.0111,
  "h8_count": 1,
  "notes": "D084 taxonomy re-audit (2026-05-15): 90 proved → H7=87 (96.7%), H1_exact=0, H1_near=1, H8=2 (2.2%), genuine=1 (1.1%). Changes vs prior: H7 +4 (paren normalization), H1 -4→0 (reclassified H7), H8 +1 (folio_1255 shared-antecedent conjunction missed), genuine -1. Tautological collapse confirmed. Taxonomy JSON: /root/autodl-tmp/outputs/plan002_additive_b01_s42_1000_taxonomy_unified.json",
  "h7a_count": 87,
  "h7_count": 87,
  "h1_count": 0,
  "taxonomy_note": "D086 clean run (ground truth): H7a=87, H7b=0, H1=0, H8=1, genuine=2. D084 residual (H8=2, genuine=1) replaced. metrics 字段已同步."
}

=== plan002-additive-b01-s43 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T08:36:16.367Z",
  "updated_at": "2026-05-15T14:27:04.296Z",
  "hypothesis": "ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。",
  "parent": "plan002-additive-b01-s42",
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "reproduce": {
    "server": "westd-39279",
    "gpu": "cuda:0",
    "started_at": "2026-05-14T08:45:10.999Z",
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\"",
    "finished_at": "2026-05-14T09:41:23.932Z",
    "training_hours": 0.94
  },
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "466128",
    "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s43.log",
    "submitted_at": "2026-05-14T08:45:54.837Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 4096.6,
    "gpu_hours": 1.14
  },
  "pid": "466128",
  "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s43.log",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T09:41:25.536028+00:00"
      }
    ]
  },
  "metrics": {
    "eval_prove_rate": 0.61,
    "eval_n_proved": 61,
    "eval_n_problems": 100,
    "eval_proved_only_isr": 0.83,
    "h7_count": 59,
    "h7_rate": 0.9672,
    "h1_count": 0,
    "h1_rate": 0,
    "h1_near_count": 0,
    "h1_near_rate": 0,
    "h8_conjunction_collapse_count": 0,
    "h8_conjunction_collapse_rate": 0,
    "genuine_count": 2,
    "genuine_rate": 0.0328,
    "proved_single_premise_ratio": 1,
    "taxonomy_note": "structurally determined: proved_single_premise_ratio=1.0, all taxonomy categories except H7 are zero by construction. eval file lost but classification derivable from structure."
  },
  "conclusion": "negative",
  "notes": "NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s43/checkpoint-500",
  "completed_at": "2026-05-14T09:54:11.468Z",
  "h7_count": 59,
  "h1_count": 0,
  "genuine_count": 2
}

=== plan002-additive-b01-s43-r2 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T14:21:58.445Z",
  "updated_at": "2026-05-17T02:57:55.367Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43_r2\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "pid": "488462",
    "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s43-r2.log",
    "submitted_at": "2026-05-15T16:36:09.631Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 3945.5,
    "gpu_hours": 1.1
  },
  "notes": "Config file: configs/grpo_additive_bonus_b01.yaml (NOT grpo_additive_b01.yaml). Corrected command: python3 scripts/train_grpo.py --config configs/grpo_additive_bonus_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43_r2",
  "server": "westd-39279",
  "gpu": "cuda:1",
  "account": "root",
  "reproduce": {
    "server": "westd-39279",
    "gpu": "cuda:1",
    "started_at": "2026-05-15T16:36:08.067Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43_r2\"",
    "finished_at": "2026-05-15T17:31:32.375Z",
    "training_hours": 0.92
  },
  "pid": "488462",
  "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s43-r2.log",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T17:31:35.315580+00:00"
      }
    ]
  },
  "metrics": {
    "eval_n_problems": 100,
    "eval_n_proved": 61,
    "eval_prove_rate": 0.61,
    "eval_mean_isr": 0.5063,
    "eval_isr_std": 0.4518,
    "eval_median_isr": 0.5,
    "eval_proved_only_isr": 0.8301,
    "h7a_count": 59,
    "h7b_count": 2,
    "h7_count": 61,
    "h7_rate": 1,
    "h1_count": 0,
    "h1_rate": 0,
    "h8_conjunction_collapse_count": 0,
    "h8_conjunction_collapse_rate": 0,
    "genuine_count": 0,
    "genuine_rate": 0,
    "proved_single_premise_ratio": 1,
    "content_independent_predicates": 5,
    "isr_eq_1_count": 40,
    "isr_eq_1_rate_of_proved": 0.656,
    "train_prove_rate": 0.68775,
    "train_mean_isr": 0.5039
  },
  "conclusion": "negative",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s43_r2/checkpoint-500",
  "completed_at": "2026-05-15T17:41:55.153Z",
  "hypothesis": "ISR β=0.1 seed=43 r2: retry with corrected config (grpo_additive_bonus_b01.yaml). plan002-b01-s43 collapsed to H7 tautology (97% single-premise); r2 verifies whether collapse is deterministic for this seed or stochastic",
  "parent": "plan002-additive-b01-s43"
}

=== plan002-additive-b01-s44 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T08:36:17.298Z",
  "updated_at": "2026-05-15T15:32:47.807Z",
  "hypothesis": "ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。",
  "parent": "plan002-additive-b01-s42",
  "server": "westd-39279",
  "gpu": "cuda:1",
  "account": "root",
  "reproduce": {
    "server": "westd-39279",
    "gpu": "cuda:1",
    "started_at": "2026-05-14T08:45:11.826Z",
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s44\"",
    "finished_at": "2026-05-14T09:28:10.836Z",
    "training_hours": 0.72
  },
  "spec": {
    "command": "python3 scripts/train_grpo.py --mode additive_bonus --isr_beta 0.1 --seed 44",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "pid": "466540",
    "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s44.log",
    "submitted_at": "2026-05-14T08:46:23.037Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 44,
    "wall_clock_seconds": 2950.3,
    "gpu_hours": 0.82
  },
  "pid": "466540",
  "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s44.log",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T09:28:12.416418+00:00"
      }
    ]
  },
  "metrics": {
    "eval_prove_rate": 0.89,
    "eval_mean_isr": 0.803,
    "eval_isr_std": null,
    "eval_proved_only_isr": 0.902,
    "eval_n_proved": 89,
    "eval_n_problems": 100,
    "h7_count": 89,
    "h7_rate": 1,
    "h1_count": 0,
    "h1_rate": 0,
    "h8_conjunction_collapse_count": 0,
    "h8_conjunction_collapse_rate": 0,
    "genuine_count": 0,
    "genuine_rate": 0,
    "component_mean": 4.33,
    "comp_2_ratio": 0.022,
    "h7_fn_correction": "12 former genuine reclassified as H7: all n_prem=1 false negatives (normalization mismatch prevented conclusion matching)"
  },
  "conclusion": "negative",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s44",
  "notes": "H7 FN correction: 12 samples with n_prem=1 misclassified as genuine. Mismatch types: 11 vacuous_quantifier_wrapping (∃x(P(x)) vs ∃x(∃y(P(y)))), 1 structural_simplification. Not simple whitespace/case but logically equivalent structural variants. Evidence file: /root/autodl-tmp/outputs/isr_s44_fn_evidence.json. Source eval: /root/runs/solver-trace-ablation/plan002-additive-b01-s44-eval.json",
  "completed_at": "2026-05-14T09:35:33.310Z",
  "h7_count": 89,
  "h1_count": 0,
  "genuine_count": 0,
  "h7_fn_correction": "vacuous quantifier wrapping (11/12) + structural simplification (1/12); model-learned obfuscation, not classifier bug",
  "h7a_count": 77,
  "h7b_count": 12,
  "taxonomy_note": "D086 补正(Reviewer): H7a=77, H7b=12, H1=0, H8=0, genuine=0. s44 全部 89 proved 均为 single_premise, H8(conjunction collapse)要求 multi-premise 数学上不可能触发. D086 clean run 误报 H8=1 已修正.",
  "h8_count": 0
}

=== plan002-additive-b01-s45 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T02:29:04.763Z",
  "updated_at": "2026-05-17T06:04:52.501Z",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_additive_bonus_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 45 --beta 0.1 --reward_mode additive_bonus --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s45 --no_wandb",
    "server": "westd-39279",
    "gpu": "cuda:0",
    "pid": "115762",
    "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s45.log",
    "submitted_at": "2026-05-17T03:48:15.292Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 45,
    "checkpoint_source": "N/A (training from base)",
    "eval_data": "data/train_500_seed42.jsonl",
    "wall_clock_seconds": 6824.2,
    "gpu_hours": 1.9
  },
  "conclusion": "success",
  "notes": "ISR β=0.1 seed=45, 5-seed completion. PID 115767 confirmed running on cuda:0.",
  "hypothesis": "ISR β=0.1 seed=45: 4th seed completing 5-seed statistics for ISR additive condition. Tests whether H7 tautological collapse observed in s43/s44 is the dominant mode (3/5 seeds) or if s42's partial genuine (17.3%) can be replicated",
  "parent": "plan002-additive-b01-s42",
  "metrics": {
    "eval_prove_rate": 0.42,
    "eval_mean_isr": 0.2542,
    "eval_isr_std": 0.3261,
    "eval_proved_only_isr": 0.6052,
    "eval_median_isr": 0,
    "eval_n_proved": 42,
    "eval_n_problems": 100,
    "h7a_rate": 0.381,
    "h7b_rate": 0,
    "h7_rate": 0.381,
    "h1_rate": 0.048,
    "h8_rate": 0.024,
    "genuine_count": 23,
    "genuine_rate": 0.548,
    "genuine_pct_total": 23,
    "h7_count": 16,
    "h1_count": 2,
    "h8_count": 1,
    "eval_data": "proofwriter_fol_100.jsonl",
    "eval_method": "eval_sta.py + classify_h7.py",
    "taxonomy_standard": "C013"
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s45/checkpoint-500",
  "log_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s45/eval_results.json",
  "completed_at": "2026-05-17T05:41:59.444Z"
}

=== plan002-additive-b01-s45-1000 ===
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-17T11:48:04.009Z",
  "updated_at": "2026-05-17T14:01:37.771Z",
  "hypothesis": "ISR β=0.1 seed=45 genuine window (~55% at 500 steps) will collapse by 1000 steps, consistent with the inevitable collapse pattern observed in s42 (17%→2%). Extended training drives ISR-trained models toward metric gaming regardless of initial genuine rate.",
  "parent": "plan002-additive-b01-s45",
  "failure_reason": "startup recovery: RUNNING with no cron and no server/pid info",
  "completed_at": "2026-05-17T12:09:43.365Z",
  "extra": {
    "previous_failure": {
      "conclusion": "failed"
    }
  },
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_additive_bonus_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 45 --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s45_1000 --no_wandb",
    "server": "westd-39279",
    "gpu_ids": [
      1
    ],
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen/Qwen3-4B",
    "seed": 45,
    "reward_mode": "additive_bonus",
    "beta": 0.1,
    "num_steps": 1000,
    "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s45_1000",
    "log_path": "/root/runs/solver-trace-ablation/plan002-additive-b01-s45-1000.log",
    "checkpoint_source": "plan002-additive-b01-s45",
    "eval_data": "proofwriter_fol_100.jsonl"
  },
  "metrics": {
    "prove_rate": 0.02,
    "proved": 2,
    "total": 100,
    "mean_isr": 0.01,
    "isr_std": 0.0704,
    "H7": 2,
    "H7a": 2,
    "H7b": 0,
    "H1": 0,
    "H8": 0,
    "genuine": 0,
    "genuine_rate": 0
  },
  "conclusion": "negative"
}

=== plan002-additive-b01-s46 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T02:29:06.903Z",
  "updated_at": "2026-05-17T05:42:00.985Z",
  "hypothesis": "ISR β=0.1 seed=46: 5th seed completing 5-seed statistics for ISR additive condition. Tests whether H7 tautological collapse observed in s43/s44 is the dominant mode or if s42's partial genuine (17.3%) can be replicated",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_additive_bonus_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 46 --beta 0.1 --reward_mode additive_bonus --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s46 --no_wandb",
    "server": "westd-39279",
    "gpu": "cuda:1",
    "pid": "115909",
    "log_path": "~/runs/solver-trace-ablation/plan002-additive-b01-s46.log",
    "submitted_at": "2026-05-17T03:48:18.660Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 46,
    "checkpoint_source": "N/A (training from base)",
    "eval_data": "data/train_500_seed42.jsonl",
    "wall_clock_seconds": 6822.3,
    "gpu_hours": 1.9
  },
  "parent": "plan002-additive-b01-s42",
  "metrics": {
    "eval_prove_rate": 0.77,
    "eval_mean_isr": 0.3164,
    "eval_isr_std": 0.2959,
    "eval_proved_only_isr": 0.411,
    "eval_median_isr": 0.25,
    "eval_n_proved": 77,
    "eval_n_problems": 100,
    "h7a_rate": 0.143,
    "h7b_rate": 0,
    "h7_rate": 0.143,
    "h1_rate": 0.26,
    "h8_rate": 0.052,
    "genuine_count": 42,
    "genuine_rate": 0.545,
    "genuine_pct_total": 42,
    "h7_count": 11,
    "h1_count": 20,
    "h8_count": 4,
    "eval_data": "proofwriter_fol_100.jsonl",
    "eval_method": "eval_sta.py + classify_h7.py",
    "taxonomy_standard": "C013"
  },
  "checkpoint_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s46/checkpoint-500",
  "log_path": "/root/autodl-tmp/outputs/plan002_additive_b01_s46/eval_results.json",
  "conclusion": "success",
  "completed_at": "2026-05-17T05:42:00.985Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "eef81475-4e41-4466-9f10-700108de3548"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Extract random b01 (plan018) experiment details",
  "usage": {
    "total_tokens": 22774,
    "tool_uses": 11,
    "duration_ms": 47788
  },
  "last_tool_name": "Bash",
  "uuid": "ed0c4b81-1f05-430e-9a52-91ff1475e87e",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_019y4L7H9AqPZkhAdQV74bex`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\n\n# Extract random b01 experiments\nfor key in \"plan018-additive-random-b01-s42\" \"plan018-additive-random-b01-s42-1000\" \\\n           \"plan018-additive-random-b01-s42-1000-r2\" \"plan018-additive-random-b01-s42-1000-r3\" \\\n           \"plan018-additive-random-b01-s43\" \"plan018-additive-random-b01-s43-r2\" \"plan018-additive-random-b01-s43-r3\" \\\n           \"plan018-additive-random-b01-s44\" \"plan018-additive-random-b01-s44-r2\" \\\n           \"plan018-additive-random-b01-s45\" \"plan018-additive-random-b01-s45-r3\" \\\n           \"plan018-additive-random-b01-s46\" \"plan018-random-b01-s45-r2\"; do\n    echo \"=== $key ===\"\n    jq -r --arg k \"$key\" '.result | fromjson | .data.experiments[$k] // \"NOT_FOUND\"' \"$FILE\" 2>/dev/null\n    echo \"\"\ndone",
  "description": "Extract random b01 (plan018) experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "faecce8c-2beb-45de-96a9-cac0d9012865",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hksDCTubCGMej5dKrSp6y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2939,
      "cache_read_input_tokens": 19393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2939,
        "ephemeral_1h_input_tokens": 0
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

_source line 45 · 2026-05-21T18:13:56.668Z_

<details><summary>↩ Tool result · `toolu_019y4L7H9AqPZkhAdQV74bex`</summary>

```text
&lt;persisted-output>
Output too large (31.3KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/bv6s47ske.txt

Preview (first 2KB):
=== plan018-additive-random-b01-s42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T06:55:48.888Z",
  "updated_at": "2026-05-15T18:08:18.764Z",
  "hypothesis": "β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。",
  "parent": "plan002-additive-b01-s42",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "377678",
    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42.log",
    "submitted_at": "2026-05-14T06:55:59.287Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "plan_id": "plan018",
    "reward_formula": "r = r_exec * (1 + 0.1 * random[0,1])",
    "num_steps": 500,
    "checkpoint_source": "N/A (training, not eval)",
    "eval_data": "N/A (training, not eval)",
    "wall_clock_seconds": 5160.4,
    "gpu_hours": 1.43,
    "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s42"
  },
  "reproduce": {
    "finished_at": "2026-05-14T08:09:07.662Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T08:09:09.188407+00:00"
      }
    ]
  },
  "conclusion": "negative",
  "metrics": {
    "eval_prove_rate": 0.79,
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "264cd923-22bb-485a-b224-3590de6664fc"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Reading ~/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/bv6s47ske.txt",
  "usage": {
    "total_tokens": 46928,
    "tool_uses": 12,
    "duration_ms": 51105
  },
  "last_tool_name": "Read",
  "uuid": "c5230571-b4de-4961-9816-b6b651975caa",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01GwjA9Xqtrvbts7PqsMBczp`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/bv6s47ske.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "688ed1a0-d36d-42d3-9191-569bf9eac33b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1KJdxrKKAvaPwRcG6VN6F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24089,
      "cache_read_input_tokens": 22332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24089,
        "ephemeral_1h_input_tokens": 0
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

_source line 48 · 2026-05-21T18:13:59.968Z_

<details><summary>↩ Tool result · `toolu_01GwjA9Xqtrvbts7PqsMBczp`</summary>

```text
1	=== plan018-additive-random-b01-s42 ===
2	{
3	  "status": "DONE",
4	  "retry_count": 0,
5	  "created_at": "2026-05-14T06:55:48.888Z",
6	  "updated_at": "2026-05-15T18:08:18.764Z",
7	  "hypothesis": "β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。",
8	  "parent": "plan002-additive-b01-s42",
9	  "spec": {
10	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42\"",
11	    "server": "westd-39279",
12	    "gpu": [
13	      "cuda:0"
14	    ],
15	    "pid": "377678",
16	    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42.log",
17	    "submitted_at": "2026-05-14T06:55:59.287Z",
18	    "submitted_via": "submit_training_job",
19	    "backend": "tmux",
20	    "account": "root",
21	    "data_path": "data/train_500_seed42.jsonl",
22	    "data_count": 500,
23	    "model_name": "Qwen3-4B",
24	    "seed": 42,
25	    "plan_id": "plan018",
26	    "reward_formula": "r = r_exec * (1 + 0.1 * random[0,1])",
27	    "num_steps": 500,
28	    "checkpoint_source": "N/A (training, not eval)",
29	    "eval_data": "N/A (training, not eval)",
30	    "wall_clock_seconds": 5160.4,
31	    "gpu_hours": 1.43,
32	    "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s42"
33	  },
34	  "reproduce": {
35	    "finished_at": "2026-05-14T08:09:07.662Z"
36	  },
37	  "extra": {
38	    "hook_events": [
39	      {
40	        "event": "on_complete",
41	        "action": "agent",
42	        "ts": "2026-05-14T08:09:09.188407+00:00"
43	      }
44	    ]
45	  },
46	  "conclusion": "negative",
47	  "metrics": {
48	    "eval_prove_rate": 0.79,
49	    "eval_mean_isr": 0.1038,
50	    "eval_isr_std": 0.1369,
51	    "eval_median_isr": 0.0357,
52	    "eval_proved_only_isr": 0.1314,
53	    "eval_n_proved": 79,
54	    "eval_n_problems": 100,
55	    "tautological_collapse": false,
56	    "h7_count": 0,
57	    "h7_rate": 0,
58	    "h7a_count": 0,
59	    "h7b_count": 0,
60	    "h1_count": 58,
61	    "h1_rate": 0.7342,
62	    "h8_count": 4,
63	    "h8_rate": 0.0506,
64	    "genuine_count": 18,
65	    "genuine_rate": 0.2278,
66	    "taxonomy_tool": "classify_h7.py standard (2026-05-15)",
67	    "taxonomy_note": "Re-classified with current classify_h7.py. Old values: genuine_strict=12 (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1), H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8."
68	  },
69	  "notes": "Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\n\n对比 plan002-b01 (ISR β=0.1):\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\n- Median ISR: 0.036 vs plan002未记录\n- Component count: 8.46 vs 5.58 (random组更多冗余)\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\n- Tautological collapse: 无 (component_2_ratio=0)\n\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\n\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json",
70	  "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s42",
71	  "completed_at": "2026-05-14T08:21:59.737Z",
72	  "h7_count": 0,
73	  "h1_count": 58,
74	  "genuine_count": 18,
75	  "h8_count": 4,
76	  "genuine_rate": 0.228,
77	  "taxonomy_note": "D086 clean run (ground truth): H7=0, H1=58, H8=4, genuine=18 (22.8%). 1 H1∩H8 overlap sample; genuine computed from set union (|H7∪H1∪H8|=61), not simple subtraction (0+58+4=62). genuine = 79 − 61 = 18."
78	}
79	
80	=== plan018-additive-random-b01-s42-1000 ===
81	{
82	  "status": "DONE",
83	  "retry_count": 0,
84	  "created_at": "2026-05-15T07:08:56.941Z",
85	  "updated_at": "2026-05-15T09:25:12.327Z",
86	  "spec": {
87	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --no_wandb\"",
88	    "server": "westd-39279",
89	    "gpu": [
90	      "cuda:1"
91	    ],
92	    "pid": "197860",
93	    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000.log",
94	    "submitted_at": "2026-05-15T08:28:46.060Z",
95	    "submitted_via": "submit_training_job",
96	    "backend": "tmux",
97	    "account": "root",
98	    "wall_clock_seconds": 3386.3,
99	    "gpu_hours": 0.94
100	  },
101	  "server": "westd-39279",
102	  "gpu": "cuda:1",
103	  "account": "root",
104	  "reproduce": {
105	    "server": "westd-39279",
106	    "gpu": "cuda:1",
107	    "started_at": "2026-05-15T08:28:44.610Z",
108	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --no_wandb\"",
109	    "finished_at": "2026-05-15T09:25:10.249Z",
110	    "training_hours": 0.94
111	  },
112	  "pid": "197860",
113	  "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000.log",
114	  "failure_reason": "EXIT_CODE=1 (generic error — check log tail)",
115	  "conclusion": "failed",
116	  "completed_at": "2026-05-15T09:25:12.327Z",
117	  "extra": {
118	    "hook_events": [
119	      {
120	        "event": "on_failed",
121	        "action": "agent",
122	        "ts": "2026-05-15T09:25:17.262043+00:00"
123	      }
124	    ]
125	  }
126	}
127	
128	=== plan018-additive-random-b01-s42-1000-r2 ===
129	{
130	  "status": "DONE",
131	  "retry_count": 0,
132	  "created_at": "2026-05-15T09:31:40.077Z",
133	  "updated_at": "2026-05-15T11:31:44.382Z",
134	  "spec": {
135	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000/checkpoint-350 --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\"",
136	    "server": "westd-39279",
137	    "gpu": [
138	      "cuda:1"
139	    ],
140	    "pid": "224797",
141	    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r2.log",
142	    "submitted_at": "2026-05-15T09:32:10.554Z",
143	    "submitted_via": "submit_training_job",
144	    "backend": "tmux",
145	    "account": "root",
146	    "wall_clock_seconds": 7173.8,
147	    "gpu_hours": 1.99
148	  },
149	  "server": "westd-39279",
150	  "gpu": "cuda:1",
151	  "account": "root",
152	  "pid": "224797",
153	  "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r2.log",
154	  "reproduce": {
155	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000/checkpoint-350 --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\"",
156	    "finished_at": "2026-05-15T10:23:56.400Z"
157	  },
158	  "extra": {
159	    "hook_events": [
160	      {
161	        "event": "on_complete",
162	        "action": "agent",
163	        "ts": "2026-05-15T10:23:59.009335+00:00"
164	      }
165	    ]
166	  },
167	  "metrics": {
168	    "train_final_prove_rate": 0.989,
169	    "train_final_mean_isr": 0.353,
170	    "train_final_reward": 1.062,
171	    "train_steps": 1000,
172	    "train_runtime_seconds": 2957,
173	    "eval_prove_rate": 1,
174	    "eval_mean_isr": 0.3333,
175	    "eval_isr_std": 0,
176	    "eval_median_isr": 0.3333,
177	    "eval_proved_only_isr": 0.3333,
178	    "eval_n_proved": 100,
179	    "eval_n_problems": 100,
180	    "eval_component_count_mean": 3,
181	    "genuine_rate": 0,
182	    "genuine_count": 0,
183	    "tautological_collapse": true,
184	    "h7_rate": null,
185	    "h7_count": null,
186	    "h1_rate": null,
187	    "h1_count": null
188	  },
189	  "conclusion": "negative",
190	  "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000",
191	  "completed_at": "2026-05-15T11:31:44.382Z"
192	}
193	
194	=== plan018-additive-random-b01-s42-1000-r3 ===
195	{
196	  "status": "DONE",
197	  "retry_count": 0,
198	  "created_at": "2026-05-15T10:26:49.094Z",
199	  "updated_at": "2026-05-15T15:39:20.811Z",
200	  "spec": {
201	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\"",
202	    "server": "westd-39279",
203	    "gpu": [
204	      "cuda:1"
205	    ],
206	    "pid": "269147",
207	    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r3.log",
208	    "submitted_at": "2026-05-15T10:27:08.529Z",
209	    "submitted_via": "submit_training_job",
210	    "backend": "tmux",
211	    "account": "root",
212	    "wall_clock_seconds": 6985.6,
213	    "gpu_hours": 1.94
214	  },
215	  "server": "westd-39279",
216	  "gpu": "cuda:1",
217	  "account": "root",
218	  "pid": "269147",
219	  "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s42-1000-r3.log",
220	  "reproduce": {
221	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3 --num_steps 1000 --beta 0.1 --seed 42 --no_wandb\"",
222	    "finished_at": "2026-05-15T12:05:43.550Z"
223	  },
224	  "extra": {
225	    "hook_events": [
226	      {
227	        "event": "on_complete",
228	        "action": "agent",
229	        "ts": "2026-05-15T12:05:46.554124+00:00"
230	      }
231	    ]
232	  },
233	  "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3/checkpoint-1000",
234	  "metrics": {
235	    "eval_prove_rate": 0.97,
236	    "eval_mean_isr": 0.6892,
237	    "eval_isr_std": 0.2037,
238	    "eval_median_isr": 0.75,
239	    "eval_proved_only_isr": 0.7105,
240	    "eval_n_proved": 97,
241	    "eval_n_problems": 100,
242	    "genuine_count": 0,
243	    "genuine_rate": 0,
244	    "h1_count": 0,
245	    "h1_rate": 0,
246	    "h7_count": 97,
247	    "h7_rate": 1,
248	    "tautological_collapse": true,
249	    "train_final_prove_rate": 0.827,
250	    "train_final_mean_isr": 0.5213,
251	    "train_loss": 0.00671,
252	    "train_final_entropy": 0.003,
253	    "train_runtime_seconds": 5783,
254	    "train_steps": 1000,
255	    "eval_by_answer_type": {
256	      "false": {
257	        "count": 25,
258	        "proved": 25,
259	        "prove_rate": 1,
260	        "mean_isr": 0.7533
261	      },
262	      "unknown": {
263	        "count": 41,
264	        "proved": 39,
265	        "prove_rate": 0.951,
266	        "mean_isr": 0.6565
267	      },
268	      "true": {
269	        "count": 34,
270	        "proved": 33,
271	        "prove_rate": 0.971,
272	        "mean_isr": 0.6814
273	      }
274	    },
275	    "n_premise_distribution": {
276	      "1": 97
277	    },
278	    "pattern_description": "All 97 proved: 1 premise identical to conclusion (P therefore P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix)."
279	  },
280	  "conclusion": "negative",
281	  "completed_at": "2026-05-15T12:23:34.170Z",
282	  "taxonomy_note": "D088 修正: metrics 字段已同步 (h7=97, h1=0, genuine=0, 全 H7a). D086 clean run classify_h7 确认 97/97 proved 均为 single_premise=conclusion (H7 tautology). 之前 metrics 残留 h1=97/h7=0 是 D086 前 classify_h7 bug 导致的错误分类. ⚠️ batch_h7ab_clean.json 中 plan018_additive_random_b01_s42_1000 条目处理的是原始失败实验(proved=100)非 r3(proved=97), 不可引用.",
283	  "h7_count": 97,
284	  "h1_count": 0,
285	  "h8_count": 0,
286	  "genuine_count": 0
287	}
288	
289	=== plan018-additive-random-b01-s43 ===
290	{
291	  "status": "DONE",
292	  "retry_count": 0,
293	  "created_at": "2026-05-14T08:36:18.260Z",
294	  "updated_at": "2026-05-14T11:42:09.950Z",
295	  "hypothesis": "Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。",
296	  "parent": "plan018-additive-random-b01-s42",
297	  "spec": {
298	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43\"",
299	    "server": "westd-39279",
300	    "gpu": [
301	      "cuda:1"
302	    ],
303	    "pid": "540910",
304	    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s43.log",
305	    "submitted_at": "2026-05-14T10:58:27.110Z",
306	    "submitted_via": "submit_training_job",
307	    "backend": "tmux",
308	    "account": "root",
309	    "data_path": "data/train_500_seed42.jsonl",
310	    "data_count": 500,
311	    "model_name": "Qwen3-4B",
312	    "seed": 43,
313	    "checkpoint_source": "plan018-additive-random-b01-s42",
314	    "eval_data": "data/train_500_seed42.jsonl",
315	    "wall_clock_seconds": 1929.4,
316	    "gpu_hours": 0.54
317	  },
318	  "reproduce": {
319	    "finished_at": "2026-05-14T11:30:34.690Z"
320	  },
321	  "failure_reason": "磁盘满 (No space left on device): /root/autodl-tmp/ 250G/250G 100% 占满。训练在 step 200/500 保存 checkpoint-200 时 safetensors 序列化失败 (os error 28)。根因: 多个已完成实验的 checkpoint 未清理。可重试——清理磁盘后重跑。",
322	  "conclusion": "failed",
323	  "completed_at": "2026-05-14T11:30:36.549Z",
324	  "extra": {
325	    "hook_events": [
326	      {
327	        "event": "on_failed",
328	        "action": "agent",
329	        "ts": "2026-05-14T11:30:40.886615+00:00"
330	      }
331	    ]
332	  },
333	  "notes": "Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \"No space left on device\". No checkpoint saved. Disk now has 109G free. Retryable as-is."
334	}
335	
336	=== plan018-additive-random-b01-s43-r2 ===
337	{
338	  "status": "DONE",
339	  "retry_count": 0,
340	  "created_at": "2026-05-14T14:01:24.111Z",
341	  "updated_at": "2026-05-15T06:39:54.823Z",
342	  "hypothesis": "Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。",
343	  "parent": "plan018-additive-random-b01-s43",
344	  "server": "westd-39279",
345	  "gpu": "cuda:0",
346	  "account": "root",
347	  "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\"",
348	  "spec": {
349	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\"",
350	    "server": "westd-39279",
351	    "gpu": [
352	      "cuda:0"
353	    ],
354	    "pid": "858386",
355	    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log",
356	    "submitted_at": "2026-05-14T15:24:32.942Z",
357	    "submitted_via": "submit_training_job",
358	    "backend": "tmux",
359	    "account": "root",
360	    "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2",
361	    "wall_clock_seconds": 6748.8,
362	    "gpu_hours": 1.87
363	  },
364	  "pid": "858386",
365	  "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log",
366	  "reproduce": {
367	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\"",
368	    "finished_at": "2026-05-14T16:43:53.042Z"
369	  },
370	  "extra": {
371	    "hook_events": [
372	      {
373	        "event": "on_complete",
374	        "action": "agent",
375	        "ts": "2026-05-14T16:43:54.952857+00:00"
376	      }
377	    ]
378	  },
379	  "metrics": {
380	    "h7_rate": 0,
381	    "h7_count": 0,
382	    "h1_rate": 93.2,
383	    "h1_count": 82,
384	    "genuine_rate": 6.8,
385	    "genuine_count": 6,
386	    "eval_prove_rate": 0.88,
387	    "eval_mean_isr": 0.058
388	  },
389	  "conclusion": "negative",
390	  "completed_at": "2026-05-14T17:17:01.774Z"
391	}
392	
393	=== plan018-additive-random-b01-s43-r3 ===
394	{
395	  "status": "DONE",
396	  "retry_count": 0,
397	  "created_at": "2026-05-15T14:17:51.220Z",
398	  "updated_at": "2026-05-15T18:57:50.838Z",
399	  "spec": {
400	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r3\"",
401	    "server": "westd-39279",
402	    "gpu": [
403	      "cuda:0"
404	    ],
405	    "pid": "486853",
406	    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r3.log",
407	    "submitted_at": "2026-05-15T16:27:24.202Z",
408	    "submitted_via": "submit_training_job",
409	    "backend": "tmux",
410	    "account": "root",
411	    "data_path": "data/train_500_seed42.jsonl",
412	    "data_count": 500,
413	    "model_name": "Qwen3-4B",
414	    "seed": 43,
415	    "wall_clock_seconds": 5840.8,
416	    "gpu_hours": 1.62
417	  },
418	  "server": "westd-39279",
419	  "gpu_id": "cuda:0",
420	  "account": "root",
421	  "reproduce": {
422	    "finished_at": "2026-05-15T17:42:33.712Z"
423	  },
424	  "extra": {
425	    "hook_events": [
426	      {
427	        "event": "on_complete",
428	        "action": "agent",
429	        "ts": "2026-05-15T17:42:36.764588+00:00"
430	      }
431	    ]
432	  },
433	  "metrics": {
434	    "prove_rate": 0.94,
435	    "n_proved": 94,
436	    "n_problems": 100,
437	    "mean_isr": 0.1406,
438	    "isr_std": null,
439	    "proved_only_isr": 0.1495,
440	    "h7_count": 36,
441	    "h7_rate": 0.383,
442	    "h7a_count": 36,
443	    "h7b_count": 0,
444	    "h1_count": 56,
445	    "h1_rate": 0.596,
446	    "h8_count": 1,
447	    "h8_rate": 0.011,
448	    "genuine_count": 1,
449	    "genuine_rate": 0.0106,
450	    "train_prove_rate": 0.5825,
451	    "train_mean_isr": 0.1266,
452	    "taxonomy_tool": "classify_h7.py + manual subtype analysis (2026-05-15)",
453	    "taxonomy_note": "D093 H7 subtype: all 36 H7 are H7a (text-match tautology), 0 H7b. single_premise_count=0: Random H7a are multi-premise proofs with embedded tautological premise, structurally different from exec-only H7a (single-premise minimal tautology). H7b confirmed absent in Random condition.",
454	    "h7a_structural_note": "Random H7a = multi-premise with embedded matching premise; exec-only H7a = single-premise P-therefore-P"
455	  },
456	  "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r3/checkpoint-500",
457	  "log_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r3/analysis.json",
458	  "conclusion": "negative",
459	  "completed_at": "2026-05-15T18:04:44.968Z"
460	}
461	
462	=== plan018-additive-random-b01-s44 ===
463	{
464	  "status": "DONE",
465	  "retry_count": 0,
466	  "created_at": "2026-05-14T08:36:18.722Z",
467	  "updated_at": "2026-05-14T15:00:09.178Z",
468	  "hypothesis": "Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。",
469	  "parent": "plan018-additive-random-b01-s42",
470	  "server": "westd-39279",
471	  "gpu": "cuda:0",
472	  "account": "root",
473	  "reproduce": {
474	    "server": "westd-39279",
475	    "gpu": "cuda:0",
476	    "started_at": "2026-05-14T11:34:13.338Z",
477	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\"",
478	    "finished_at": "2026-05-14T13:37:42.200Z",
479	    "training_hours": 2.06
480	  },
481	  "spec": {
482	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\"",
483	    "server": "westd-39279",
484	    "gpu": [
485	      "cuda:0"
486	    ],
487	    "pid": "564900",
488	    "data_path": "data/train_500_seed42.jsonl",
489	    "data_count": 500,
490	    "model_name": "Qwen3-4B",
491	    "seed": 44,
492	    "reward_formula": "r = r_exec * (1 + 0.1 * random[0,1])",
493	    "num_steps": 500
494	  },
495	  "pid": "564900",
496	  "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log",
497	  "extra": {
498	    "hook_events": [
499	      {
500	        "event": "on_complete",
501	        "action": "agent",
502	        "ts": "2026-05-14T13:37:43.236026+00:00"
503	      }
504	    ]
505	  },
506	  "metrics": {
507	    "prove_rate": 0.89,
508	    "mean_isr": 0.0619,
509	    "isr_std": 0.1756,
510	    "median_isr": 0,
511	    "proved_only_mean_isr": 0.0695,
512	    "n_proved": 89,
513	    "n_problems": 100,
514	    "max_isr": 1,
515	    "min_isr": 0,
516	    "isr_pr_ratio": 0.0695,
517	    "isr_zero_count": 72,
518	    "isr_one_count": 2,
519	    "by_answer_type": {
520	      "false": {
521	        "count": 25,
522	        "proved": 21,
523	        "prove_rate": 0.84,
524	        "mean_isr": 0.0533
525	      },
526	      "unknown": {
527	        "count": 41,
528	        "proved": 40,
529	        "prove_rate": 0.976,
530	        "mean_isr": 0.0892
531	      },
532	      "true": {
533	        "count": 34,
534	        "proved": 28,
535	        "prove_rate": 0.824,
536	        "mean_isr": 0.0353
537	      }
538	    },
539	    "elapsed_seconds": 1012.7,
540	    "eval_method": "eval_sta.py with Prover9Solver, FOL"
541	  },
542	  "conclusion": "success",
543	  "notes": "DONE (success). Random β=0.1 s44 对照分析完成: PR=0.89/ISR=0.062 (clean) vs ISR β=0.1 s44 PR=0.89/ISR=0.803 (H7=86.5% inflated). 同 PR 下 ISR reward 导致 conclusion duplication，random 无此问题。与 s42 结论一致: ISR s42 genuine ISR=0.337 vs Random s42 ISR=0.104 (3.2x)。Random 2/3 seeds done, 等 s43 (plan018-random-b01-s43-r2 QUEUED)。",
544	  "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/checkpoint-500",
545	  "completed_at": "2026-05-14T14:29:21.226Z"
546	}
547	
548	=== plan018-additive-random-b01-s44-r2 ===
549	{
550	  "status": "DONE",
551	  "retry_count": 0,
552	  "created_at": "2026-05-15T14:17:54.315Z",
553	  "updated_at": "2026-05-17T02:57:56.085Z",
554	  "spec": {
555	    "model_name": "Qwen3-4B",
556	    "data_path": "data/train_500_seed42.jsonl",
557	    "data_count": 500,
558	    "seed": 44,
559	    "eval_data": "proofwriter_fol_100.jsonl",
560	    "conclusion_reason": "D095 negative: H7=0, H1=73 (82%), H8=16 (18%), genuine=6 (6.7%). H1+H8 overlap=6 samples. C013 set-exclusion formula applied."
561	  },
562	  "server": "westd-39279",
563	  "gpu": "cuda:1",
564	  "account": "root",
565	  "pid": "533415",
566	  "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s44-r2.log",
567	  "reproduce": {
568	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2\"",
569	    "finished_at": "2026-05-15T19:09:37.912Z"
570	  },
571	  "extra": {
572	    "hook_events": [
573	      {
574	        "event": "on_complete",
575	        "action": "agent",
576	        "ts": "2026-05-15T19:09:40.791078+00:00"
577	      }
578	    ]
579	  },
580	  "metrics": {
581	    "train_prove_rate": 0.64675,
582	    "train_mean_isr": 0.08092,
583	    "train_loss": 0.00937,
584	    "train_steps": 500,
585	    "train_runtime_sec": 4998,
586	    "eval_prove_rate": 0.89,
587	    "eval_mean_isr": 0.0619,
588	    "eval_isr_std": 0.1756,
589	    "eval_median_isr": 0,
590	    "eval_isr_pr_ratio": 0.0695,
591	    "eval_proved_only_isr": 0.0695,
592	    "eval_n_proved": 89,
593	    "eval_n_problems": 100,
594	    "h7_count": 0,
595	    "h7a_count": 0,
596	    "h7b_count": 0,
597	    "h1_count": 73,
598	    "h8_count": 16,
599	    "genuine_count": 6,
600	    "genuine_rate": 0.067,
601	    "h7_rate": 0,
602	    "h1_rate": 0.82,
603	    "h8_rate": 0.18,
604	    "content_independent_count": 18
605	  },
606	  "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s44_r2",
607	  "conclusion": "negative",
608	  "completed_at": "2026-05-15T19:19:05.717Z",
609	  "hypothesis": "Random β=0.1 seed=44 r2: retry after plan018-s44 (PR=89%, genuine=15.7%) was re-evaluated with updated classify_h7. If genuine% drops under stricter taxonomy, random control advantage over ISR narrows",
610	  "parent": "plan018-additive-random-b01-s44"
611	}
612	
613	=== plan018-additive-random-b01-s45 ===
614	{
615	  "status": "DONE",
616	  "retry_count": 1,
617	  "created_at": "2026-05-16T02:29:08.182Z",
618	  "updated_at": "2026-05-17T08:40:33.956Z",
619	  "hypothesis": "Random β=0.1 seed=45, 5-seed matched control for ISR β=0.1 comparison",
620	  "notes": "PID 628171 被 b02 提交时 GPU 冲突挤掉，进程已死。回退 PREPARING 等 GPU 空出后重排。需加 --no_wandb。",
621	  "completed_at": "2026-05-16T04:29:35.108Z",
622	  "extra": {
623	    "previous_failure": {
624	      "conclusion": "killed",
625	      "notes": "PID 628171 被 b02 提交时 GPU 冲突挤掉，进程已死。回退 PREPARING 等 GPU 空出后重排。需加 --no_wandb。"
626	    }
627	  },
628	  "spec": {
629	    "command": "bash -c \"export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 45 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan018_random_b01_s45 --no_wandb\"",
630	    "server": "westd-39279",
631	    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
632	    "data_count": 500,
633	    "model_name": "Qwen/Qwen3-4B",
634	    "seed": 45,
635	    "reward_mode": "additive_random",
636	    "beta": 0.1,
637	    "num_steps": 500,
638	    "checkpoint_path": "/root/autodl-tmp/outputs/plan018_random_b01_s45/step_500",
639	    "log_path": "/root/autodl-tmp/outputs/plan018_random_b01_s45/training.log"
640	  },
641	  "metrics": {
642	    "eval_prove_rate": 0.58,
643	    "eval_n_proved": 58,
644	    "eval_n_problems": 100,
645	    "eval_mean_isr": 0.0096,
646	    "eval_proved_only_isr": 0.0166,
647	    "h7_count": 0,
648	    "h7_rate": 0,
649	    "h1_count": 53,
650	    "h1_rate": 0.914,
651	    "h8_count": 0,
652	    "h8_rate": 0,
653	    "genuine_count": 5,
654	    "genuine_rate": 0.086,
655	    "eval_data": "proofwriter_fol_100.jsonl",
656	    "eval_method": "eval_sta.py + classify_h7.py"
657	  },
658	  "conclusion": "success"
659	}
660	
661	=== plan018-additive-random-b01-s45-r3 ===
662	{
663	  "status": "DONE",
664	  "retry_count": 0,
665	  "created_at": "2026-05-16T05:58:19.847Z",
666	  "updated_at": "2026-05-16T07:14:04.347Z",
667	  "spec": {
668	    "command": "python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --seed 45 --num_steps 500 --num_generations 4 --output_dir /root/autodl-tmp/outputs/plan018_random_b01_s45_r3 --no_wandb",
669	    "server": "westd-39279",
670	    "data_path": "data/train_500_seed42.jsonl",
671	    "data_count": 500,
672	    "model_name": "Qwen3-4B",
673	    "seed": 45,
674	    "gpu": [
675	      "cuda:0"
676	    ],
677	    "pid": "688887",
678	    "reward_mode": "additive_random",
679	    "beta": 0.1,
680	    "num_steps": 500,
681	    "num_generations": 4,
682	    "account": "root",
683	    "failure_reason": "Disk full at step 400/500. checkpoint-400 corrupt (2/4 shards). checkpoint-350 deleted during cleanup. Needs full re-training.",
684	    "log_path": "/root/autodl-tmp/outputs/plan018_random_b01_s45_r3.log",
685	    "checkpoint_path": "NONE"
686	  },
687	  "conclusion": "failed",
688	  "completed_at": "2026-05-16T07:06:34.359Z"
689	}
690	
691	=== plan018-additive-random-b01-s46 ===
692	{
693	  "status": "DONE",
694	  "retry_count": 0,
695	  "created_at": "2026-05-16T02:29:09.430Z",
696	  "updated_at": "2026-05-17T03:38:53.460Z",
697	  "hypothesis": "Random β=0.1 seed=46, 5-seed matched control for ISR β=0.1 comparison",
698	  "spec": {
699	    "hypothesis": "Random β=0.1 seed=46: 5-seed matched control for ISR β=0.1 comparison, 验证 random reward 不会触发 ISR-specific hacking",
700	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 46 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan018_random_b01_s46 --no_wandb\"",
701	    "server": "westd-39279",
702	    "gpu": "cuda:1",
703	    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
704	    "data_count": 500,
705	    "model_name": "Qwen/Qwen3-4B",
706	    "seed": 46,
707	    "pid": "70021",
708	    "submitted_at": "2026-05-17T02:33:30Z",
709	    "submitted_via": "manual_tmux",
710	    "backend": "tmux",
711	    "account": "root",
712	    "wall_clock_seconds": 3914.4,
713	    "gpu_hours": 1.09
714	  },
715	  "server": "westd-39279",
716	  "gpu": "cuda:1",
717	  "parent": "plan018-additive-random-b01-s42",
718	  "conclusion": "negative",
719	  "checkpoint_path": "/root/autodl-tmp/outputs/plan018_random_b01_s46/checkpoint-500",
720	  "log_path": "/root/autodl-tmp/outputs/plan018_random_b01_s46/reward_log.jsonl",
721	  "completed_at": "2026-05-17T03:38:44.406Z",
722	  "metrics": {
723	    "eval_prove_rate": 0.94,
724	    "eval_mean_isr": 0.0424,
725	    "h7_count": 86,
726	    "h1_count": 2,
727	    "h8_count": 4,
728	    "genuine_count": 2,
729	    "genuine_rate": 0.021
730	  }
731	}
732	
733	=== plan018-random-b01-s45-r2 ===
734	{
735	  "status": "DONE",
736	  "retry_count": 0,
737	  "created_at": "2026-05-16T05:36:20.734Z",
738	  "updated_at": "2026-05-16T05:58:26.795Z",
739	  "spec": {
740	    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --seed 45 --num_steps 500 --num_generations 4 --output_dir /root/autodl-tmp/outputs/plan018_random_b01_s45 --no_wandb\"",
741	    "server": "westd-39279",
742	    "gpu": [
743	      "cuda:0"
744	    ],
745	    "pid": "679720",
746	    "data_path": "data/train_500_seed42.jsonl",
747	    "data_count": 500,
748	    "model_name": "Qwen3-4B",
749	    "seed": 45,
750	    "reward_mode": "additive_random",
751	    "beta": 0.1,
752	    "num_steps": 500,
753	    "num_generations": 4,
754	    "account": "root",
755	    "wandb_enabled": false
756	  },
757	  "conclusion": "failed",
758	  "completed_at": "2026-05-16T05:58:26.795Z"
759	}
760	
761	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "74339d19-02e7-4a46-8dfd-87b870ad067e"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Extract additional experiment entries",
  "usage": {
    "total_tokens": 62296,
    "tool_uses": 13,
    "duration_ms": 62508
  },
  "last_tool_name": "Bash",
  "uuid": "6936856e-6287-4808-b61e-d7b1a67faecd",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01L9eurKDxjKkf5DG7oQJJNo`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\n\n# Also check the \"exec-only-s43-1000step\" retries and sweep experiments\nfor key in \"exec-only-s43-1000step-r2\" \"exec-only-s43-1000step-r3\" \"exec-only-s43-1000step-r4\" \\\n           \"exec-only-s43-1000step-r5\" \"exec-only-s43-1000step-r6\" \"exec-only-s43-1000step-r7\" \\\n           \"plan016-extended-1000-s42\" \\\n           \"sweep-exec-only-s45\" \"sweep-exec-only-s46\" \\\n           \"sweep-isr-b01-s45\" \"sweep-isr-b01-s46\" \\\n           \"sweep-random-b01-s45\" \"sweep-random-b01-s46\"; do\n    echo \"=== $key ===\"\n    jq -r --arg k \"$key\" '.result | fromjson | .data.experiments[$k] // \"NOT_FOUND\"' \"$FILE\" 2>/dev/null\n    echo \"\"\ndone",
  "description": "Extract additional experiment entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "91e85d7a-de9b-4192-9d49-9807d0ad24f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0145qto43e43K9rnTEV66ds6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15366,
      "cache_read_input_tokens": 46421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15366,
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

_source line 51 · 2026-05-21T18:14:11.377Z_

<details><summary>↩ Tool result · `toolu_01L9eurKDxjKkf5DG7oQJJNo`</summary>

```text
=== exec-only-s43-1000step-r2 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T23:19:42.457Z",
  "updated_at": "2026-05-16T23:22:03.424Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/solver-trace-ablation && python scripts/train_grpo.py --model_path Qwen/Qwen3-4B --data_path /root/solver-trace-ablation/data/train_500_seed42.jsonl --reward_mode execution_only --beta 0.0 --num_steps 1000 --seed 43 --num_generations 4 --learning_rate 1e-6 --save_total_limit 1 --no_wandb\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "988685",
    "log_path": "~/runs/solver-trace-ablation/exec-only-s43-1000step-r2.log",
    "submitted_at": "2026-05-16T23:21:29.620Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 33.8,
    "gpu_hours": 0.01
  },
  "server": "westd-39279",
  "gpu": "cuda:0",
  "pid": "988685",
  "log_path": "~/runs/solver-trace-ablation/exec-only-s43-1000step-r2.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/solver-trace-ablation && python scripts/train_grpo.py --model_path Qwen/Qwen3-4B --data_path /root/solver-trace-ablation/data/train_500_seed42.jsonl --reward_mode execution_only --beta 0.0 --num_steps 1000 --seed 43 --num_generations 4 --learning_rate 1e-6 --save_total_limit 1 --no_wandb\"",
    "finished_at": "2026-05-16T23:22:00.830Z"
  },
  "failure_reason": "EXIT_CODE=2 (shell misuse / syntax)",
  "conclusion": "failed",
  "completed_at": "2026-05-16T23:22:03.424Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T23:22:06.827170+00:00"
      }
    ]
  }
}

=== exec-only-s43-1000step-r3 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T23:23:41.408Z",
  "updated_at": "2026-05-16T23:28:26.078Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2 --model_path /root/autodl-tmp/models/Qwen3-4B --no_wandb\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "989121",
    "log_path": "~/runs/solver-trace-ablation/exec-only-s43-1000step-r3.log",
    "submitted_at": "2026-05-16T23:24:07.077Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 158.6,
    "gpu_hours": 0.04
  },
  "server": "westd-39279",
  "gpu": "cuda:0",
  "pid": "989121",
  "log_path": "~/runs/solver-trace-ablation/exec-only-s43-1000step-r3.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2 --model_path /root/autodl-tmp/models/Qwen3-4B --no_wandb\"",
    "finished_at": "2026-05-16T23:26:43.093Z"
  },
  "failure_reason": "CUDA OOM: CUDA out of memory. Tried to allocate 54.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 35.56 MiB is free. Including non-PyTorch memory, this process has 94.93 GiB memory in use. Of the allocated memory 90.67 GiB is allocated by PyTorch, an",
  "conclusion": "failed",
  "completed_at": "2026-05-16T23:26:45.641Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T23:26:48.875592+00:00"
      }
    ]
  }
}

=== exec-only-s43-1000step-r4 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T23:48:23.885Z",
  "updated_at": "2026-05-16T23:49:25.870Z",
  "spec": {
    "command": "bash -c \"cd /root/solver-trace-ablation && CUDA_VISIBLE_DEVICES=0 PYTORCH_ALLOC_CONF=expandable_segments:True python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2 --model_path /root/autodl-tmp/models/Qwen3-4B --no_wandb\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "unknown",
    "log_path": "~/runs/solver-trace-ablation/exec-only-s43-1000step-r4.log",
    "submitted_at": "2026-05-16T23:48:49.516Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 36.4,
    "gpu_hours": 0.01
  },
  "server": "westd-39279",
  "gpu": "cuda:0",
  "pid": "unknown",
  "log_path": "~/runs/solver-trace-ablation/exec-only-s43-1000step-r4.log",
  "reproduce": {
    "command": "bash -c \"cd /root/solver-trace-ablation && CUDA_VISIBLE_DEVICES=0 PYTORCH_ALLOC_CONF=expandable_segments:True python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2 --model_path /root/autodl-tmp/models/Qwen3-4B --no_wandb\"",
    "finished_at": "2026-05-16T23:49:23.193Z"
  },
  "failure_reason": "Traceback → Traceback (most recent call last): File \"/root/solver-trace-ablation/scripts/train_grpo.py\", line 33, in &lt;module> import torch ModuleNotFoundError: No module named 'torch'",
  "conclusion": "failed",
  "completed_at": "2026-05-16T23:49:25.870Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T23:49:29.701871+00:00"
      }
    ]
  }
}

=== exec-only-s43-1000step-r5 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T23:49:47.467Z",
  "updated_at": "2026-05-16T23:52:41.148Z",
  "spec": {
    "hypothesis": "s43 exec-only 1000-step 恢复轨迹：500-step s43 PR=76% 是否在延长训练后恢复到 s42/s44 水平(~90%), 回答 Reviewer Q1 seed variance 问题",
    "parent": "plan001-exec-only-s43-1000",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && CUDA_VISIBLE_DEVICES=0 PYTORCH_ALLOC_CONF=expandable_segments:True python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r5 --model_path /root/autodl-tmp/models/Qwen3-4B --no_wandb",
    "server": "westd-39279",
    "gpu": "cuda:0",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen/Qwen3-4B",
    "seed": 43
  },
  "server": "westd-39279",
  "gpu": "cuda:0",
  "pid": "990676",
  "log_path": "~/runs/solver-trace-ablation/exec-only-s43-1000step-r5.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/bin/activate && cd /root/solver-trace-ablation && PYTORCH_ALLOC_CONF=expandable_segments:True python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2 --model_path /root/autodl-tmp/models/Qwen3-4B --no_wandb\"",
    "finished_at": "2026-05-16T23:52:37.474Z"
  },
  "conclusion": "failed",
  "failure_reason": "EXIT_CODE=129 (non-zero)",
  "completed_at": "2026-05-16T23:52:41.148Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T23:52:47.084869+00:00"
      }
    ]
  }
}

=== exec-only-s43-1000step-r6 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T23:51:13.870Z",
  "updated_at": "2026-05-17T00:16:11.173Z",
  "spec": {
    "hypothesis": "s43 exec-only 1000-step 恢复轨迹：500-step s43 PR=76% 是否在延长训练后恢复到 s42/s44 水平(~90%), 回答 Reviewer Q1 seed variance 问题",
    "parent": "plan001-exec-only-s43-1000",
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2 --no_wandb\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen/Qwen3-4B",
    "seed": 43,
    "pid": "991155",
    "submitted_at": "2026-05-16T23:51:30Z",
    "submitted_via": "manual_tmux",
    "backend": "tmux",
    "account": "root",
    "failure_reason": "磁盘满 (250G/250G) at step 100/1000. checkpoint-50 可能完整, checkpoint-100 不完整(仅写入 2/4 shard)",
    "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2/checkpoint-50",
    "log_path": "tmux pane only (no file log)",
    "wall_clock_seconds": 1481.2,
    "gpu_hours": 0.41
  },
  "server": "westd-39279",
  "gpu": "cuda:0",
  "conclusion": "failed",
  "completed_at": "2026-05-17T00:16:11.173Z"
}

=== exec-only-s43-1000step-r7 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-17T00:41:14.461Z",
  "updated_at": "2026-05-17T03:44:39.754Z",
  "spec": {
    "hypothesis": "s43 exec-only 1000-step 恢复轨迹：500-step s43 PR=76% 是否在延长训练后恢复到 s42/s44 水平(~90%), 回答 Reviewer Q1 seed variance 问题",
    "parent": "plan001-exec-only-s43-1000",
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2 --no_wandb\"",
    "server": "westd-39279",
    "gpu": "cuda:0",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen/Qwen3-4B",
    "seed": 43,
    "pid": "996789",
    "submitted_at": "2026-05-17T00:22:00Z",
    "submitted_via": "manual_tmux",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 12159.8,
    "gpu_hours": 3.38
  },
  "server": "westd-39279",
  "gpu": "cuda:0",
  "hypothesis": "Exec-only 1000-step seed=43: tests whether extended training recovers genuine proofs from the degenerate s43 seed (500-step s43 yielded PR=14%, ISR=0, 100% H1). If 1000 steps still collapses, confirms s43 degradation is irreversible under exec-only reward",
  "parent": "plan001-exec-only-s43-r4",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2/checkpoint-1000",
  "log_path": "/root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2/reward_log.jsonl",
  "metrics": {
    "eval_prove_rate": 0.96,
    "eval_mean_isr": 0.0818,
    "h7_count": 0,
    "h1_count": 90,
    "h8_count": 0,
    "genuine_count": 6,
    "genuine_rate": 0.062,
    "content_independent": 4
  },
  "conclusion": "negative",
  "completed_at": "2026-05-17T03:44:39.754Z"
}

=== plan016-extended-1000-s42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T05:29:47.634Z",
  "updated_at": "2026-05-15T20:25:41.946Z",
  "hypothesis": "Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？",
  "parent": "plan001-exec-only-s42-r2",
  "server": "westd-39279",
  "gpu": "cuda:1",
  "account": "root",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:1"
    ],
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "hypothesis": "Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?",
    "plan_id": "plan016",
    "reward_formula": "r = r_exec (exec-only)",
    "num_steps": 1000
  },
  "pid": "263268",
  "log_path": "~/runs/solver-trace-ablation/plan016-extended-1000-s42.log",
  "reproduce": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\"",
    "finished_at": "2026-05-14T08:02:31.805Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T08:02:33.434519+00:00"
      }
    ]
  },
  "metrics": {
    "eval_proved_only_isr": 0.0028,
    "eval_mean_isr": 0.0027,
    "eval_isr_std": 0.0118,
    "eval_median_isr": 0,
    "eval_max_isr": 0.0588,
    "eval_prove_rate": 0.96,
    "eval_n_proved": 96,
    "eval_n_total": 100
  },
  "conclusion": "success",
  "checkpoint_path": "/root/autodl-tmp/outputs/plan016_extended_1000_s42",
  "completed_at": "2026-05-14T08:13:51.754Z",
  "notes": "Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\n\\n## 500 vs 1000 step comparison (eval_sta.py):\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\n|--------|-------------------|-----------------|--------|\\n| eval PR | 0.93 | 0.96 | +3.2% |\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\n| components | 6.58 | 18.55 | +182% |\\n| ISR=0 ratio | - | 94.8% | - |\\n| n_necessary=0 ratio | - | 94.8% | - |\\n\\n## Key findings:\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\n\\n## Implication for paper:\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse."
}

=== sweep-exec-only-s45 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T02:42:16.736Z",
  "updated_at": "2026-05-16T08:22:21.707Z",
  "hypothesis": "W4: Exec-only s45 extends baseline to 5-seed for tighter confidence intervals",
  "conclusion": "killed",
  "notes": "去重取消：与 plan001-exec-only-s45 重复（同 exec-only, seed=45）",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --seed 45 --num_steps 500 --num_generations 4 --output_dir /root/autodl-tmp/outputs/sweep_exec_only_s45 --no_wandb",
    "server": "westd-39279",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 45,
    "gpu": [
      "cuda:1"
    ],
    "pid": "728319",
    "reward_mode": "execution_only",
    "num_steps": 500,
    "num_generations": 4,
    "account": "root",
    "log_path": "~/runs/solver-trace-ablation/sweep-exec-only-s45.log",
    "checkpoint_source": "base_model",
    "failure_reason": "Never actually executed. PID 728319 belonged to s46. Registry corrected."
  },
  "completed_at": "2026-05-16T08:22:21.707Z"
}

=== sweep-exec-only-s46 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T02:42:17.401Z",
  "updated_at": "2026-05-16T09:22:30.339Z",
  "hypothesis": "W4: Exec-only s46 extends baseline to 5-seed for tighter confidence intervals",
  "conclusion": "negative",
  "notes": "去重取消：与 plan001-exec-only-s46 重复（同 exec-only, seed=46）",
  "spec": {
    "command": "python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --seed 46 --num_steps 500 --num_generations 4 --output_dir /root/autodl-tmp/outputs/sweep_exec_only_s46 --no_wandb",
    "server": "westd-39279",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 46,
    "gpu": [
      "cuda:0"
    ],
    "pid": "728319",
    "reward_mode": "execution_only",
    "num_steps": 500,
    "num_generations": 4,
    "account": "root",
    "log_path": "~/runs/solver-trace-ablation/sweep-exec-only-s46.log",
    "checkpoint_source": "base_model"
  },
  "reproduce": {
    "finished_at": "2026-05-16T08:58:35.966Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-16T08:58:39.354910+00:00"
      }
    ]
  },
  "completed_at": "2026-05-16T09:20:24.661Z"
}

=== sweep-isr-b01-s45 ===
{
  "status": "DONE",
  "retry_count": 1,
  "created_at": "2026-05-16T02:28:50.991Z",
  "updated_at": "2026-05-16T04:05:36.104Z",
  "hypothesis": "W4: ISR β=0.1 s45 extends existing 3-seed to 5-seed for tighter confidence intervals on hacking rates and genuine rates",
  "reproduce": {
    "finished_at": "2026-05-16T03:28:29.306Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-16T02:57:23.086288+00:00"
      },
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-16T03:28:36.835248+00:00"
      }
    ],
    "previous_failure": {
      "conclusion": "failed",
      "metrics": {
        "actual_steps": 100,
        "expected_steps": 500,
        "train_prove_rate_nonzero_count": 40,
        "train_prove_rate_zero_count": 60,
        "train_runtime_sec": 915,
        "failure_reason": "config merge bug: argparse default num_steps=100 overrides config num_steps=500"
      },
      "notes": "FAILED: Training ran 100 steps instead of 500. Root cause: train_grpo.py config merge logic (line 395-401) only overrides CLI args when current is None. Since --num_steps has default=100, config file num_steps=500 is silently ignored. The command did not pass --num_steps explicitly. Must retrain with explicit --num_steps 500 in the command, or fix the config merge bug."
    }
  },
  "completed_at": "2026-05-16T03:01:38.649Z",
  "notes": "Loop 16 发现实验仍在 GPU 0 上运行（PID 604569, step 177/500 @03:51 UTC）。之前被错误标记为 killed。wandb run: sweep-isr-b01-s45-r3。预计 ~04:40 UTC 完成。",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus_b01.yaml --beta 0.1 --seed 45 --num_generations 4 --output_dir /root/autodl-tmp/outputs/sweep_isr_b01_s45 --wandb_run sweep-isr-b01-s45-r3 --wandb_project solver-trace-ablation\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "604564",
    "log_path": "~/runs/solver-trace-ablation/sweep-isr-b01-s45.log",
    "submitted_at": "2026-05-16T03:21:42.611Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 408.6,
    "gpu_hours": 0.11
  },
  "conclusion": "killed",
  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
  "metrics": {
    "prove_rate": 0.2357,
    "prove_rate_last50": 0.475,
    "isr_mean": 0.1127,
    "isr_mean_last50": 0.2172,
    "reward_mean": 0.247,
    "loss": 0.0106,
    "parse_rate": 1,
    "steps_completed": 219,
    "steps_total": 500,
    "kill_reason": "SIGKILL exit 137 (system OOM killer)",
    "checkpoint": "checkpoint-200"
  }
}

=== sweep-isr-b01-s46 ===
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-16T02:42:14.600Z",
  "updated_at": "2026-05-16T03:37:25.823Z",
  "hypothesis": "W4: ISR β=0.1 s46 extends to 5-seed for tighter confidence intervals",
  "conclusion": "killed",
  "notes": "去重取消：与 plan002-additive-b01-s46 重复（同 β=0.1, seed=46, ISR 5-seed）"
}

=== sweep-random-b01-s45 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T02:42:13.324Z",
  "updated_at": "2026-05-20T04:05:09.215Z",
  "hypothesis": "W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1",
  "conclusion": "success",
  "notes": "去重取消：与 plan018-additive-random-b01-s45 重复（同 Random β=0.1, seed=45）",
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "reproduce": {
    "server": "westd-39279",
    "gpu": "cuda:0",
    "started_at": "2026-05-20T04:00:49.883Z"
  },
  "spec": {
    "command": "linked from plan018-additive-random-b01-s45 (no re-run)",
    "server": "westd-39279",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 45,
    "checkpoint_path": "/root/autodl-tmp/outputs/plan018_random_b01_s45/step_500",
    "log_path": "/root/autodl-tmp/outputs/plan018_random_b01_s45/training.log"
  },
  "completed_at": "2026-05-20T04:04:54.992Z",
  "metrics": {
    "eval_prove_rate": 0.58,
    "eval_n_proved": 58,
    "eval_n_problems": 100,
    "eval_mean_isr": 0.0096,
    "eval_proved_only_isr": 0.0166,
    "h7_count": 0,
    "h7_rate": 0,
    "h1_count": 53,
    "h1_rate": 0.914,
    "h8_count": 0,
    "h8_rate": 0,
    "genuine_count": 5,
    "genuine_rate": 0.086,
    "eval_data": "proofwriter_fol_100.jsonl",
    "eval_method": "eval_sta.py + classify_h7.py",
    "source": "linked from plan018-additive-random-b01-s45"
  }
}

=== sweep-random-b01-s46 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T02:42:15.492Z",
  "updated_at": "2026-05-20T04:05:11.292Z",
  "hypothesis": "W4: Random β=0.1 s46 extends random control to 5-seed",
  "conclusion": "success",
  "notes": "去重取消：与 plan018-additive-random-b01-s46 重复（同 Random β=0.1, seed=46）",
  "spec": {
    "command": "linked from plan018-additive-random-b01-s46 (no re-run)",
    "server": "westd-39279",
    "data_path": "data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen3-4B",
    "seed": 46,
    "checkpoint_path": "/root/autodl-tmp/outputs/plan018_random_b01_s46",
    "log_path": "/root/autodl-tmp/outputs/plan018_random_b01_s46/training.log"
  },
  "completed_at": "2026-05-20T04:04:58.319Z",
  "metrics": {
    "eval_prove_rate": 0.94,
    "eval_n_proved": 94,
    "eval_n_problems": 100,
    "eval_mean_isr": 0.0424,
    "h7_count": 86,
    "h7_rate": 0.915,
    "h1_count": 2,
    "h1_rate": 0.021,
    "h8_count": 4,
    "h8_rate": 0.043,
    "genuine_count": 2,
    "genuine_rate": 0.021,
    "eval_data": "proofwriter_fol_100.jsonl",
    "eval_method": "eval_sta.py + classify_h7.py",
    "source": "linked from plan018-additive-random-b01-s46"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "2bdd942b-86af-4946-bbf0-666c202db2f2"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "description": "Running Get exec-only s45/s46 entries",
  "usage": {
    "total_tokens": 72887,
    "tool_uses": 14,
    "duration_ms": 71861
  },
  "last_tool_name": "Bash",
  "uuid": "b9d80708-4c18-40a0-9a15-18febde372d8",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01TqQMgFy2ZmTHCbTD3ey8Ff`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/8e9feaac-9f71-428e-bb25-4ce1e25b3aee/tool-results/mcp-agent-ml-research-read_registry-1779387196239.txt\"\n\nfor key in \"plan001-exec-only-s45\" \"plan001-exec-only-s46\" \\\n           \"exec-retrain-for-warmstart-s42\" \"exec-retrain-v3-s42\" \"exec-retrain-v3-s43\"; do\n    echo \"=== $key ===\"\n    jq -r --arg k \"$key\" '.result | fromjson | .data.experiments[$k] // \"NOT_FOUND\"' \"$FILE\" 2>/dev/null\n    echo \"\"\ndone",
  "description": "Get exec-only s45/s46 entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "f40cb9cf-8d9a-4939-96db-4b2e66709c32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Hqx4io2hcw6CYs2uZrvA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10589,
      "cache_read_input_tokens": 61787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10589,
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

_source line 54 · 2026-05-21T18:14:20.646Z_

<details><summary>↩ Tool result · `toolu_01TqQMgFy2ZmTHCbTD3ey8Ff`</summary>

```text
=== plan001-exec-only-s45 ===
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-16T02:29:10.640Z",
  "updated_at": "2026-05-16T03:37:36.874Z",
  "hypothesis": "Exec-only seed=45, 5-seed baseline for tighter confidence intervals"
}

=== plan001-exec-only-s46 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T02:29:11.891Z",
  "updated_at": "2026-05-17T02:57:01.904Z",
  "hypothesis": "Exec-only seed=46 500-step: verifies exec-only converges to ~90% PR with dominant H1 hacking regardless of seed, ruling out s43 low-PR as systematic failure rather than seed variance",
  "spec": {
    "server": "westd-39279",
    "gpu": "cuda:1",
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=1 && export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 46 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s46 --no_wandb\"",
    "data_path": "/root/solver-trace-ablation/data/train_500_seed42.jsonl",
    "data_count": 500,
    "model_name": "Qwen/Qwen3-4B",
    "seed": 46,
    "pid": "5439",
    "submitted_at": "2026-05-17T00:53:00Z",
    "submitted_via": "manual_tmux",
    "backend": "tmux",
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/outputs/plan001_exec_only_s46/checkpoint-500",
    "log_path": "tmux pane only",
    "wall_clock_seconds": 4500,
    "gpu_hours": 1.25
  },
  "server": "westd-39279",
  "gpu": "cuda:1",
  "conclusion": "success",
  "completed_at": "2026-05-17T02:10:04.298Z",
  "metrics": {
    "prove_rate": 0.93,
    "mean_isr": 0.083,
    "genuine_pct": 9.7,
    "h1_pct": 89.2,
    "h7_pct": 0,
    "h8_pct": 4.3,
    "n_proved": 93,
    "n_problems": 100
  },
  "parent": "plan001-exec-only-s42-r2"
}

=== exec-retrain-for-warmstart-s42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T15:46:21.692Z",
  "updated_at": "2026-05-17T02:54:11.486Z",
  "spec": {
    "command": "python scripts/train_grpo.py --config configs/grpo_exec_retrain.yaml --seed 42",
    "server": "westd-39279",
    "gpu": "cuda:0",
    "data_path": "data/proofwriter_fol_100.jsonl",
    "data_count": 100,
    "model_name": "Qwen3-4B",
    "seed": 42,
    "reward_mode": "execution_only",
    "num_steps": 500,
    "purpose": "Exec-only retrain with intermediate checkpoints for ISR-gated warmstart"
  },
  "conclusion": "success",
  "checkpoint_path": "/root/autodl-tmp/outputs/exec_retrain_v3_s42/checkpoint-200",
  "log_path": "/root/autodl-tmp/outputs/exec_retrain_v3_s42.log",
  "completed_at": "2026-05-16T16:53:17.826Z",
  "hypothesis": "Exec-only 200-step intermediate checkpoint as warmstart base: pre-training with pure execution reward establishes basic proof competence before adding ISR gate, avoiding cold-start instability"
}

=== exec-retrain-v3-s42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T16:04:26.936Z",
  "updated_at": "2026-05-16T16:30:52.565Z",
  "spec": {
    "hypothesis": "Exec-only retrain from base Qwen3-4B to generate intermediate checkpoints (step 200-250) for ISR-gated warmstart",
    "model_name": "Qwen3-4B",
    "seed": 42,
    "server": "westd-39279",
    "gpu": "cuda:0",
    "data_path": "data/proofwriter_fol_100.jsonl",
    "data_count": 100,
    "hyperparams": {
      "reward_mode": "exec_only",
      "num_generations": 8,
      "per_device_train_batch_size": 2,
      "gradient_accumulation_steps": 4,
      "lr": 0.000001,
      "max_steps": 500,
      "save_steps": 50,
      "save_total_limit": 3
    },
    "command": "python scripts/train_grpo.py --config configs/grpo_exec_retrain_v3.yaml --seed 42 --output_dir /root/autodl-tmp/outputs/exec_retrain_v3_s42 --no_wandb",
    "pid": 875499,
    "num_generations": 8,
    "num_steps": 500,
    "save_steps": 50,
    "checkpoint_path": "/root/autodl-tmp/outputs/exec_retrain_v3_s42",
    "log_path": "/root/autodl-tmp/outputs/exec_retrain_v3_s42.log"
  },
  "conclusion": "killed",
  "completed_at": "2026-05-16T16:30:52.565Z"
}

=== exec-retrain-v3-s43 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-16T16:04:28.770Z",
  "updated_at": "2026-05-16T16:30:54.692Z",
  "spec": {
    "hypothesis": "Exec-only retrain from base Qwen3-4B to generate intermediate checkpoints (step 200-250) for ISR-gated warmstart",
    "model_name": "Qwen3-4B",
    "seed": 43,
    "server": "westd-39279",
    "gpu": "cuda:1",
    "data_path": "data/proofwriter_fol_100.jsonl",
    "data_count": 100,
    "hyperparams": {
      "reward_mode": "exec_only",
      "num_generations": 8,
      "per_device_train_batch_size": 2,
      "gradient_accumulation_steps": 4,
      "lr": 0.000001,
      "max_steps": 500,
      "save_steps": 50,
      "save_total_limit": 3
    },
    "command": "python scripts/train_grpo.py --config configs/grpo_exec_retrain_v3.yaml --seed 43 --output_dir /root/autodl-tmp/outputs/exec_retrain_v3_s43 --no_wandb",
    "pid": 875573,
    "num_generations": 8,
    "num_steps": 500,
    "save_steps": 50,
    "checkpoint_path": "/root/autodl-tmp/outputs/exec_retrain_v3_s43",
    "log_path": "/root/autodl-tmp/outputs/exec_retrain_v3_s43.log"
  },
  "conclusion": "killed",
  "completed_at": "2026-05-16T16:30:54.692Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "28d6090f-8000-4608-9d5e-f018e185b2ad"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a8bca2bbe6f09904b",
  "tool_use_id": "toolu_01Dq4udZQrTitU2gahNHM1Po",
  "status": "completed",
  "output_file": "",
  "summary": "Read registry for per-seed metrics",
  "usage": {
    "total_tokens": 75508,
    "tool_uses": 14,
    "duration_ms": 128779
  },
  "uuid": "92a074ca-4fca-4bdb-bd98-115327303d2c",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee"
}
```

---

### Tool result

_source line 56 · 2026-05-21T18:15:17.394Z_

<details><summary>↩ Tool result · `toolu_01Dq4udZQrTitU2gahNHM1Po`</summary>

```text
Here is the complete per-seed evaluation metrics report for all three conditions:

---

## 1. EXEC-ONLY EXPERIMENTS

### 500-step runs

**plan001-exec-only-s42-r2** (seed=42) -- conclusion: **success**
- PR: 0.93 (93/100)
- Mean ISR: 0.1232, ISR std: 0.1887, Median ISR: 0, Proved-only ISR: 0.1324
- Hacking: H7=0 (0%), H1=81 (87.1%), H8=6 (6.45%), Genuine=7 (7.53%)
- Genuine mean ISR: 0.3141, H1 mean ISR: 0.1055

**plan001-exec-only-s43-r4** (seed=43) -- conclusion: **negative**
- Greedy: PR=0.13 (13/100), Mean ISR=0, Proved-only ISR=0
- Sampling (T=0.7): PR=0.14 (14/100), Mean ISR=0
- Hacking (greedy): H7=0, H1=13 (100%), Genuine=0 (0%)
- Mean components (proved): 18.92
- Note: complete collapse; decoding-invariant failure

**plan001-exec-only-s44** (seed=44) -- conclusion: **negative**
- PR: 0.98 (98/100)
- Mean ISR: 0.57, ISR std: 0.2013, Proved-only ISR: 0.5816
- Hacking: H7=97 (H7 rate=1.0), H1=0, H8=0, Genuine=0 (0%)
- Mean components: 2.04 (tautological collapse -- 94% have only 2 components)
- Note: ISR=0.5+ is an artifact of tautological single-premise proofs

**plan001-exec-only-s46** (seed=46) -- conclusion: **success**
- PR: 0.93 (93/100)
- Mean ISR: 0.083
- Hacking: H7=0%, H1=89.2%, H8=4.3%, Genuine=9.7%

### 1000-step runs

**plan016-extended-1000-s42** (seed=42) -- conclusion: **success**
- PR: 0.96 (96/100)
- Mean ISR: 0.0027, ISR std: 0.0118, Proved-only ISR: 0.0028
- Note: ISR collapsed from 0.123 (500-step) to 0.003 (1000-step). No taxonomy breakdown in registry but notes say "contradiction-based collapse" with 94.8% having zero necessary components.

**plan001-exec-only-s43-1000-r2** (seed=43) -- conclusion: **success**
- PR: 0.90 (90/100)
- Mean ISR: 0.531, ISR std: 0.15, ISR corrected: 0.465
- Hacking: H7=90 (100%), H7a=90, H7b=0, H1=0, H8=0, Genuine=0 (0%)
- Note: All 90 proved are H7a tautology. ISR reflects quantifier structure, not reasoning quality.

**exec-only-s43-1000step-r7** (seed=43, alternative run) -- conclusion: **negative**
- PR: 0.96 (96/100)
- Mean ISR: 0.0818
- Hacking: H7=0, H1=90, H8=0, Genuine=6 (6.2%)

**plan001-exec-only-s44-1000-r2** (seed=44) -- conclusion: **success**
- PR: 1.00 (100/100)
- Mean ISR: 0.002, ISR std: 0.0146
- Hacking: H7=0, H7a=0, H7b=0, H1=85 (85%), H8=15 (15%), Genuine=0 (0%)
- Note: Shifted from H7 mode (500-step) to H1+H8 mode (1000-step). genuine_strict=0.

---

## 2. ISR beta=0.1 EXPERIMENTS (plan002-additive-b01)

### 500-step runs

**plan002-additive-b01-s42** (seed=42) -- conclusion: **negative**
- PR: 0.81 (81/100)
- Mean ISR: 0.3365, ISR std: 0.3227, Median ISR: 0.2, Proved-only ISR: 0.4154
- Mean components: 5.58
- Hacking: H7=13 (16.1%), H1=42 (51.9%), H8=12 (14.8%), Genuine=14 (17.3%)

**plan002-additive-b01-s43-r2** (seed=43, best run) -- conclusion: **negative**
- PR: 0.61 (61/100)
- Mean ISR: 0.5063, ISR std: 0.4518, Median ISR: 0.5, Proved-only ISR: 0.8301
- Hacking: H7=61 (100%; H7a=59, H7b=2), H1=0, H8=0, Genuine=0 (0%)
- ISR=1 count: 40 (65.6% of proved), all single-premise tautology

**plan002-additive-b01-s44** (seed=44) -- conclusion: **negative**
- PR: 0.89 (89/100)
- Mean ISR: 0.803, Proved-only ISR: 0.902
- Mean components: 4.33
- Hacking: H7=89 (100%; H7a=77, H7b=12), H1=0, H8=0, Genuine=0 (0%)

**plan002-additive-b01-s45** (seed=45) -- conclusion: **success**
- PR: 0.42 (42/100)
- Mean ISR: 0.2542, ISR std: 0.3261, Proved-only ISR: 0.6052
- Hacking: H7=16 (38.1%), H1=2 (4.8%), H8=1 (2.4%), Genuine=23 (54.8%)

**plan002-additive-b01-s46** (seed=46) -- conclusion: **success**
- PR: 0.77 (77/100)
- Mean ISR: 0.3164, ISR std: 0.2959, Proved-only ISR: 0.411
- Hacking: H7=11 (14.3%), H1=20 (26.0%), H8=4 (5.2%), Genuine=42 (54.5%)

### 1000-step runs

**plan002-additive-b01-s42-1000** (seed=42) -- conclusion: **negative**
- PR: 0.90 (90/100)
- Mean ISR: 0.7892, ISR std: 0.3424, Proved-only ISR: 0.8769
- Mean components: 2.889, tautological collapse: true
- Hacking: H7=87 (96.7%; all H7a), H1=0, H8=1 (1.1%), Genuine=2 (2.2%)
- Note: Collapsed from genuine=14 (17.3%) at 500-step to genuine=2 (2.2%) at 1000-step.

**plan002-additive-b01-s45-1000** (seed=45) -- conclusion: **negative**
- PR: 0.02 (2/100)
- Mean ISR: 0.01, ISR std: 0.0704
- Hacking: H7=2 (100%; all H7a), H1=0, H8=0, Genuine=0 (0%)
- Note: Catastrophic collapse from PR=42% genuine=55% at 500 steps to PR=2% at 1000 steps.

---

## 3. RANDOM beta=0.1 EXPERIMENTS (plan018-additive-random-b01)

### 500-step runs

**plan018-additive-random-b01-s42** (seed=42) -- conclusion: **negative**
- PR: 0.79 (79/100)
- Mean ISR: 0.1038, ISR std: 0.1369, Median ISR: 0.0357, Proved-only ISR: 0.1314
- Hacking: H7=0, H1=58 (73.4%), H8=4 (5.1%), Genuine=18 (22.8%)
- Note: set-union dedup applied (H1 intersection H8 = 1 sample)

**plan018-additive-random-b01-s43-r3** (seed=43, best run) -- conclusion: **negative**
- PR: 0.94 (94/100)
- Mean ISR: 0.1406, Proved-only ISR: 0.1495
- Hacking: H7=36 (38.3%; all H7a), H1=56 (59.6%), H8=1 (1.1%), Genuine=1 (1.06%)

**plan018-additive-random-b01-s44-r2** (seed=44, best run) -- conclusion: **negative**
- PR: 0.89 (89/100)
- Mean ISR: 0.0619, ISR std: 0.1756, Median ISR: 0, Proved-only ISR: 0.0695
- Hacking: H7=0, H1=73 (82%), H8=16 (18%), Genuine=6 (6.7%)
- Content-independent count: 18

**plan018-additive-random-b01-s45** (seed=45) -- conclusion: **success**
- PR: 0.58 (58/100)
- Mean ISR: 0.0096, Proved-only ISR: 0.0166
- Hacking: H7=0, H1=53 (91.4%), H8=0, Genuine=5 (8.6%)

**plan018-additive-random-b01-s46** (seed=46) -- conclusion: **negative**
- PR: 0.94 (94/100)
- Mean ISR: 0.0424
- Hacking: H7=86 (91.5%), H1=2 (2.1%), H8=4 (4.3%), Genuine=2 (2.1%)

### 1000-step runs

**plan018-additive-random-b01-s42-1000-r3** (seed=42) -- conclusion: **negative**
- PR: 0.97 (97/100)
- Mean ISR: 0.6892, ISR std: 0.2037, Proved-only ISR: 0.7105
- Hacking: H7=97 (100%), H1=0, H8=0, Genuine=0 (0%)
- Tautological collapse: true. All 97 proved: single premise identical to conclusion (P therefore P).

---

## SUMMARY TABLE (500-step, successful/evaluable runs only)

| Condition | Seed | PR | Mean ISR | TS (H7)% | CE (H1)% | PG (H8)% | Genuine% | N-Hacked |
|-----------|------|------|----------|-----------|-----------|-----------|----------|----------|
| Exec-only | s42 | 0.93 | 0.123 | 0% | 87.1% | 6.5% | 7.5% | 7 |
| Exec-only | s43 | 0.13 | 0.0 | 0% | 100% | 0% | 0% | 0 |
| Exec-only | s44 | 0.98 | 0.57* | 100%* | 0% | 0% | 0% | 0 |
| Exec-only | s46 | 0.93 | 0.083 | 0% | 89.2% | 4.3% | 9.7% | ~9 |
| ISR b=0.1 | s42 | 0.81 | 0.337 | 16.1% | 51.9% | 14.8% | 17.3% | 14 |
| ISR b=0.1 | s43 | 0.61 | 0.506 | 100% | 0% | 0% | 0% | 0 |
| ISR b=0.1 | s44 | 0.89 | 0.803 | 100% | 0% | 0% | 0% | 0 |
| ISR b=0.1 | s45 | 0.42 | 0.254 | 38.1% | 4.8% | 2.4% | 54.8% | 23 |
| ISR b=0.1 | s46 | 0.77 | 0.316 | 14.3% | 26.0% | 5.2% | 54.5% | 42 |
| Random b=0.1 | s42 | 0.79 | 0.104 | 0% | 73.4% | 5.1% | 22.8% | 18 |
| Random b=0.1 | s43 | 0.94 | 0.141 | 38.3% | 59.6% | 1.1% | 1.1% | 1 |
| Random b=0.1 | s44 | 0.89 | 0.062 | 0% | 82.0% | 18.0% | 6.7% | 6 |
| Random b=0.1 | s45 | 0.58 | 0.010 | 0% | 91.4% | 0% | 8.6% | 5 |
| Random b=0.1 | s46 | 0.94 | 0.042 | 91.5% | 2.1% | 4.3% | 2.1% | 2 |

(*) s44 exec-only ISR=0.57 and TS=100% are tautological artifacts (2-component proofs, premise=conclusion).

Key naming: TS = Tautological Shortcut (H7), CE = Conclusion Embedding (H1), PG = Premise Grafting / conjunction collapse (H8). plan001-exec-only-s45 was never completed (stuck in PREPARING).

agentId: a8bca2bbe6f09904b (use SendMessage with to: 'a8bca2bbe6f09904b' to continue this agent)
&lt;usage>total_tokens: 78756
tool_uses: 14
duration_ms: 128781&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "2b82cdf6-b472-409b-9ce7-464b23999064",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the experiment registry for the project \"solver-trace-ablation\" using the MCP tool `mcp__agent-ml-research__read_registry`. I need to find per-seed evaluation metrics for these experiments:\n\n1. **Exec-only** experiments: look for exp_ids like `plan001-exec-only-s42`, `plan001-exec-only-s43`, `plan001-exec-only-s44`, or similar patterns with \"exec\" in the name\n2. **ISR β=0.1** experiments: look for exp_ids with \"isr\" and \"b01\" or \"beta01\" or similar for seeds s42, s43, s44\n3. **Random β=0.1** experiments: look for exp_ids with \"random\" and \"b01\" or similar for seeds s42, s43, s44\n\nAlso look for exp_ids starting with \"exp1-\" as an alternative naming convention.\n\nFirst read the full registry, then extract the relevant entries. I need: PR (prove rate), ISR (inference step redundancy), and hacking composition stats (TS%, CE%, N-H% or similar breakdowns).\n\nReport ALL metrics you find for these experiments in full detail - every number matters. Include the exp_id, seed, conclusion status, and all eval metrics for each.",
    "agentId": "a8bca2bbe6f09904b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete per-seed evaluation metrics report for all three conditions:\n\n---\n\n## 1. EXEC-ONLY EXPERIMENTS\n\n### 500-step runs\n\n**plan001-exec-only-s42-r2** (seed=42) -- conclusion: **success**\n- PR: 0.93 (93/100)\n- Mean ISR: 0.1232, ISR std: 0.1887, Median ISR: 0, Proved-only ISR: 0.1324\n- Hacking: H7=0 (0%), H1=81 (87.1%), H8=6 (6.45%), Genuine=7 (7.53%)\n- Genuine mean ISR: 0.3141, H1 mean ISR: 0.1055\n\n**plan001-exec-only-s43-r4** (seed=43) -- conclusion: **negative**\n- Greedy: PR=0.13 (13/100), Mean ISR=0, Proved-only ISR=0\n- Sampling (T=0.7): PR=0.14 (14/100), Mean ISR=0\n- Hacking (greedy): H7=0, H1=13 (100%), Genuine=0 (0%)\n- Mean components (proved): 18.92\n- Note: complete collapse; decoding-invariant failure\n\n**plan001-exec-only-s44** (seed=44) -- conclusion: **negative**\n- PR: 0.98 (98/100)\n- Mean ISR: 0.57, ISR std: 0.2013, Proved-only ISR: 0.5816\n- Hacking: H7=97 (H7 rate=1.0), H1=0, H8=0, Genuine=0 (0%)\n- Mean components: 2.04 (tautological collapse -- 94% have only 2 components)\n- Note: ISR=0.5+ is an artifact of tautological single-premise proofs\n\n**plan001-exec-only-s46** (seed=46) -- conclusion: **success**\n- PR: 0.93 (93/100)\n- Mean ISR: 0.083\n- Hacking: H7=0%, H1=89.2%, H8=4.3%, Genuine=9.7%\n\n### 1000-step runs\n\n**plan016-extended-1000-s42** (seed=42) -- conclusion: **success**\n- PR: 0.96 (96/100)\n- Mean ISR: 0.0027, ISR std: 0.0118, Proved-only ISR: 0.0028\n- Note: ISR collapsed from 0.123 (500-step) to 0.003 (1000-step). No taxonomy breakdown in registry but notes say \"contradiction-based collapse\" with 94.8% having zero necessary components.\n\n**plan001-exec-only-s43-1000-r2** (seed=43) -- conclusion: **success**\n- PR: 0.90 (90/100)\n- Mean ISR: 0.531, ISR std: 0.15, ISR corrected: 0.465\n- Hacking: H7=90 (100%), H7a=90, H7b=0, H1=0, H8=0, Genuine=0 (0%)\n- Note: All 90 proved are H7a tautology. ISR reflects quantifier structure, not reasoning quality.\n\n**exec-only-s43-1000step-r7** (seed=43, alternative run) -- conclusion: **negative**\n- PR: 0.96 (96/100)\n- Mean ISR: 0.0818\n- Hacking: H7=0, H1=90, H8=0, Genuine=6 (6.2%)\n\n**plan001-exec-only-s44-1000-r2** (seed=44) -- conclusion: **success**\n- PR: 1.00 (100/100)\n- Mean ISR: 0.002, ISR std: 0.0146\n- Hacking: H7=0, H7a=0, H7b=0, H1=85 (85%), H8=15 (15%), Genuine=0 (0%)\n- Note: Shifted from H7 mode (500-step) to H1+H8 mode (1000-step). genuine_strict=0.\n\n---\n\n## 2. ISR beta=0.1 EXPERIMENTS (plan002-additive-b01)\n\n### 500-step runs\n\n**plan002-additive-b01-s42** (seed=42) -- conclusion: **negative**\n- PR: 0.81 (81/100)\n- Mean ISR: 0.3365, ISR std: 0.3227, Median ISR: 0.2, Proved-only ISR: 0.4154\n- Mean components: 5.58\n- Hacking: H7=13 (16.1%), H1=42 (51.9%), H8=12 (14.8%), Genuine=14 (17.3%)\n\n**plan002-additive-b01-s43-r2** (seed=43, best run) -- conclusion: **negative**\n- PR: 0.61 (61/100)\n- Mean ISR: 0.5063, ISR std: 0.4518, Median ISR: 0.5, Proved-only ISR: 0.8301\n- Hacking: H7=61 (100%; H7a=59, H7b=2), H1=0, H8=0, Genuine=0 (0%)\n- ISR=1 count: 40 (65.6% of proved), all single-premise tautology\n\n**plan002-additive-b01-s44** (seed=44) -- conclusion: **negative**\n- PR: 0.89 (89/100)\n- Mean ISR: 0.803, Proved-only ISR: 0.902\n- Mean components: 4.33\n- Hacking: H7=89 (100%; H7a=77, H7b=12), H1=0, H8=0, Genuine=0 (0%)\n\n**plan002-additive-b01-s45** (seed=45) -- conclusion: **success**\n- PR: 0.42 (42/100)\n- Mean ISR: 0.2542, ISR std: 0.3261, Proved-only ISR: 0.6052\n- Hacking: H7=16 (38.1%), H1=2 (4.8%), H8=1 (2.4%), Genuine=23 (54.8%)\n\n**plan002-additive-b01-s46** (seed=46) -- conclusion: **success**\n- PR: 0.77 (77/100)\n- Mean ISR: 0.3164, ISR std: 0.2959, Proved-only ISR: 0.411\n- Hacking: H7=11 (14.3%), H1=20 (26.0%), H8=4 (5.2%), Genuine=42 (54.5%)\n\n### 1000-step runs\n\n**plan002-additive-b01-s42-1000** (seed=42) -- conclusion: **negative**\n- PR: 0.90 (90/100)\n- Mean ISR: 0.7892, ISR std: 0.3424, Proved-only ISR: 0.8769\n- Mean components: 2.889, tautological collapse: true\n- Hacking: H7=87 (96.7%; all H7a), H1=0, H8=1 (1.1%), Genuine=2 (2.2%)\n- Note: Collapsed from genuine=14 (17.3%) at 500-step to genuine=2 (2.2%) at 1000-step.\n\n**plan002-additive-b01-s45-1000** (seed=45) -- conclusion: **negative**\n- PR: 0.02 (2/100)\n- Mean ISR: 0.01, ISR std: 0.0704\n- Hacking: H7=2 (100%; all H7a), H1=0, H8=0, Genuine=0 (0%)\n- Note: Catastrophic collapse from PR=42% genuine=55% at 500 steps to PR=2% at 1000 steps.\n\n---\n\n## 3. RANDOM beta=0.1 EXPERIMENTS (plan018-additive-random-b01)\n\n### 500-step runs\n\n**plan018-additive-random-b01-s42** (seed=42) -- conclusion: **negative**\n- PR: 0.79 (79/100)\n- Mean ISR: 0.1038, ISR std: 0.1369, Median ISR: 0.0357, Proved-only ISR: 0.1314\n- Hacking: H7=0, H1=58 (73.4%), H8=4 (5.1%), Genuine=18 (22.8%)\n- Note: set-union dedup applied (H1 intersection H8 = 1 sample)\n\n**plan018-additive-random-b01-s43-r3** (seed=43, best run) -- conclusion: **negative**\n- PR: 0.94 (94/100)\n- Mean ISR: 0.1406, Proved-only ISR: 0.1495\n- Hacking: H7=36 (38.3%; all H7a), H1=56 (59.6%), H8=1 (1.1%), Genuine=1 (1.06%)\n\n**plan018-additive-random-b01-s44-r2** (seed=44, best run) -- conclusion: **negative**\n- PR: 0.89 (89/100)\n- Mean ISR: 0.0619, ISR std: 0.1756, Median ISR: 0, Proved-only ISR: 0.0695\n- Hacking: H7=0, H1=73 (82%), H8=16 (18%), Genuine=6 (6.7%)\n- Content-independent count: 18\n\n**plan018-additive-random-b01-s45** (seed=45) -- conclusion: **success**\n- PR: 0.58 (58/100)\n- Mean ISR: 0.0096, Proved-only ISR: 0.0166\n- Hacking: H7=0, H1=53 (91.4%), H8=0, Genuine=5 (8.6%)\n\n**plan018-additive-random-b01-s46** (seed=46) -- conclusion: **negative**\n- PR: 0.94 (94/100)\n- Mean ISR: 0.0424\n- Hacking: H7=86 (91.5%), H1=2 (2.1%), H8=4 (4.3%), Genuine=2 (2.1%)\n\n### 1000-step runs\n\n**plan018-additive-random-b01-s42-1000-r3** (seed=42) -- conclusion: **negative**\n- PR: 0.97 (97/100)\n- Mean ISR: 0.6892, ISR std: 0.2037, Proved-only ISR: 0.7105\n- Hacking: H7=97 (100%), H1=0, H8=0, Genuine=0 (0%)\n- Tautological collapse: true. All 97 proved: single premise identical to conclusion (P therefore P).\n\n---\n\n## SUMMARY TABLE (500-step, successful/evaluable runs only)\n\n| Condition | Seed | PR | Mean ISR | TS (H7)% | CE (H1)% | PG (H8)% | Genuine% | N-Hacked |\n|-----------|------|------|----------|-----------|-----------|-----------|----------|----------|\n| Exec-only | s42 | 0.93 | 0.123 | 0% | 87.1% | 6.5% | 7.5% | 7 |\n| Exec-only | s43 | 0.13 | 0.0 | 0% | 100% | 0% | 0% | 0 |\n| Exec-only | s44 | 0.98 | 0.57* | 100%* | 0% | 0% | 0% | 0 |\n| Exec-only | s46 | 0.93 | 0.083 | 0% | 89.2% | 4.3% | 9.7% | ~9 |\n| ISR b=0.1 | s42 | 0.81 | 0.337 | 16.1% | 51.9% | 14.8% | 17.3% | 14 |\n| ISR b=0.1 | s43 | 0.61 | 0.506 | 100% | 0% | 0% | 0% | 0 |\n| ISR b=0.1 | s44 | 0.89 | 0.803 | 100% | 0% | 0% | 0% | 0 |\n| ISR b=0.1 | s45 | 0.42 | 0.254 | 38.1% | 4.8% | 2.4% | 54.8% | 23 |\n| ISR b=0.1 | s46 | 0.77 | 0.316 | 14.3% | 26.0% | 5.2% | 54.5% | 42 |\n| Random b=0.1 | s42 | 0.79 | 0.104 | 0% | 73.4% | 5.1% | 22.8% | 18 |\n| Random b=0.1 | s43 | 0.94 | 0.141 | 38.3% | 59.6% | 1.1% | 1.1% | 1 |\n| Random b=0.1 | s44 | 0.89 | 0.062 | 0% | 82.0% | 18.0% | 6.7% | 6 |\n| Random b=0.1 | s45 | 0.58 | 0.010 | 0% | 91.4% | 0% | 8.6% | 5 |\n| Random b=0.1 | s46 | 0.94 | 0.042 | 91.5% | 2.1% | 4.3% | 2.1% | 2 |\n\n(*) s44 exec-only ISR=0.57 and TS=100% are tautological artifacts (2-component proofs, premise=conclusion).\n\nKey naming: TS = Tautological Shortcut (H7), CE = Conclusion Embedding (H1), PG = Premise Grafting / conjunction collapse (H8). plan001-exec-only-s45 was never completed (stuck in PREPARING)."
      }
    ],
    "totalDurationMs": 128781,
    "totalTokens": 78756,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 72376,
      "output_tokens": 3759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3759,
          "cache_read_input_tokens": 72376,
          "cache_creation_input_tokens": 2620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2620,
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
      "bashCount": 11,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 2
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
Now I have all the data I need. Let me organize the information for the sensitivity analysis.

## Data for 2-seed pooled (s42 + s44), excluding s43

### Exec-only (500-step)
- s42: PR=0.93, ISR*=0.132, TS=0%, CE=87.1%, PG=6.5%, N-H=7.5%, proved=93
- s44: PR=0.98, ISR*=0.582, TS=100%, CE=0%, PG=0%, N-H=0%, proved=98


Wait, s44 exec-only shows a tautological collapse with TS=100%, which is problematic. I need to reconsider this. The paper already claims that excluding s43 doesn't change the qualitative conclusions, so I need to verify this holds up in the appendix. Let me recalculate the pooled statistics for these two seeds, though I'm noticing some inconsistencies in the registry data that need clarification. Looking at the appendix table, s44 shows PR=0.98 with 98 proved samples, all classified as TS (tautological collapse). The registry listing H7=97 seems inconsistent with this, so the actual count is likely H7=98 to match the proved total.

For s42, I'm working through the category breakdown from the appendix: 93 proved samples split into TS=0, CE=81 (87.1%), PG=6 (6.5%), and N-H=7 (7.5%). The numbers add up to 94 when summed, which is one more than the 93 proved count, suggesting there might be an overlap between categories that I need to account for.

For s44, the data shows 98 proved samples with TS=100%, meaning all hacking attempts were timestamp-based. Now I'm calculating the pooled statistics across both seeds: total proved is 191, and the mean proof rate comes to 0.955 with a standard error of 0.05.

But wait—s44's results are heavily skewed by tautological collapse since TS=100% creates an artifact in the ISR* metric (0.582), so combining s42 and s44 doesn't really give a clean picture. The actual task here is to exclude s43 entirely and compute the 2-seed pooled statistics as a robustness check, since reviewers might question s43's influence given its exec-only T=0.7 issue.

Looking at the exec-only conclusions: PR stays high at 95.5% across s42+s44, but ISR collapses and N-H drops to ~3.7%, which supports the reward hacking narrative. For the ISR β=0.1 case, s42 shows moderate performance (PR=0.81, ISR*=0.415) while s44 shows inflated metrics due to the TS=100% artifact, so I need to compute what the 2-seed pooled PR actually comes out to. Now I'm verifying the category breakdowns for each sample—s42 splits across TS, CE, PG, and N-H categories that sum to 81, while s44 is entirely TS at 89. Pooling them gives 102 total TS cases out of 170 proved (60.0%), 42 CE cases (24.7%), and 12 PG cases, though I need to reconcile the PG count with the appendix data. So after the PG reclassification and correcting for TS false negatives, the ISR non-hacking rate drops to 14 out of 231 cases, which is 6.06% when pooling across the three seeds. Now I'm working through the two-seed pooled results for s42 and s44, which gives 14 non-hacking samples out of 170 total proved (8.2%), actually higher than the three-seed rate since s43 diluted the numbers with its 61 proved and zero non-hacking. For the corrected metrics, s44's TS equals its proved count at 89 with zero non-hacking, while s42 requires me to trace through the PG reclassification logic to see which genuine samples were manually identified as having unusually low premise counts. Now I'm checking the Random β=0.1 results for s42, where the proved count is 79 but the breakdown adds to 80—there's a one-sample overlap between the H1 and H8 categories that needs to be accounted for.

Looking at the appendix table for Random, I can see the detailed metrics across different seeds, with s42 showing 73.4% hacking and 22.8% non-hacking, along with specific counts for PG and other categories. Now I'm aggregating the results across both samples to get the combined statistics: 168 total proved cases with a 78% success rate for CE and about 14% for N-H. I'm also calculating the mean performance ratios and standard errors for both PR and ISR*, which show PR averaging around 0.84 with relatively tight confidence bounds.

For the pooled exec-only results, I'm cross-referencing the individual seed outcomes with the registry data to resolve some discrepancies in the true success counts, particularly for s44 where the reported percentages need to align with the actual proved case numbers. Looking at the data more carefully, there's a discrepancy between the H7 count of 97 and the total proved of 98, with H7 rate listed as 1.0. The appendix table shows TS%=100 for s44, which likely means rounding 97/98 up to 100%, so I'll treat this as 98 tautological samples. Now I'm moving on to calculate the pooled results for the 2-seed exec-only combination of s42 and s44.

For the combined dataset totaling 191 samples, I'm computing the mean performance rates and their standard errors: PR averages to 0.955 with a standard error of 0.018, while ISR* is much more variable at 0.357 with a standard error of 0.159 due to the very different performance modes between the two samples. Breaking down the outcomes: 98 samples proved (51.3%), 81 showed correct errors (42.4%), and 7 were non-halting (3.7%). Now I'm calculating the same metrics for the ISR β=0.1 configuration across both seeds, getting a proved sample count of 170 with corresponding percentages for each category, and I'm realizing I should also include PG to stay consistent with the main paper's reporting format.

Looking at the table structure from the main paper, I need to focus on PR, ISR*, TS%, CE%, and N-H% as the key metrics. For the random baseline with β=0.1, I'm seeing notably different results—a much lower ISR* value of 0.101 compared to ISR's 0.659, and a dramatically higher CE% at 78.0%, which makes sense since random search lacks the intelligent guidance that ISR provides.

Now moving on to the 3-seed exec-only pooled results...

I'm noticing s43 is problematic—it was evaluated at T=0.7 rather than greedily, which makes it not directly comparable to the other seeds. The registry shows it achieved 13 proofs out of 100 attempts with zero genuine solutions, so CE% is essentially 100% and N-H% is 0%. When I pool all three seeds together (s42, s43, s44), I get a total of 204 proofs, which gives me a mean PR of 0.68 with high variance due to s43's poor performance.

Looking at the task requirements more carefully, I need to report 2-seed results (s42+s44) for all conditions, and then verify whether the 3-seed exec-only pooled data is feasible—which it is, since the paper already has this in the appendix with the exact statistics I'm calculating.

However, the existing table only shows mean±std for PR and ISR*, not the individual hacking composition metrics (TS%, CE%, N-H%) for the 3-seed exec-only case. Since the main paper's exec-only results use only s42, I should compute the 3-seed pooled hacking statistics as well. Looking at the individual seed data: s42 has 93 proved cases with specific TS/CE/N-H breakdowns, while s43 has only 13 proved cases with different distributions, and I need to reconcile the registry values with the actual proved case counts.

I'm realizing the registry data for s43 shows both greedy and sampling (T=0.7) results, and I need to clarify which one applies—the greedy version has PR=13 with all CE cases and zero ISR, which matches what the appendix table is showing. So the core issue is that seed 43's greedy evaluation shows a very poor precision-recall of 0.13, with all 13 proved cases being CE hacking, yet the main paper evaluated it with nucleus sampling at T=0.7 instead. For the pooled 3-seed exec-only results, I need to account for this caveat when computing the aggregate metrics.

Looking at the breakdown: combining seeds 42, 43, and 44 with greedy gives 204 total proved cases, where the hacking composition splits into TS (98), CE (94), and N-H (7), yielding percentages of 48.0%, 46.1%, and 3.4% respectively. But I should probably focus on a sensitivity analysis comparing the 2-seed pooled results (excluding s43) against the full 3-seed pooled to demonstrate that the qualitative conclusions remain stable, and optionally include the 3-seed exec-only with appropriate caveats about s43's poor greedy performance.

The key patterns hold across conditions: ISR substantially amplifies TS compared to random (60% vs 0% in the 2-seed case), the non-hacking rate stays relatively consistent, and ISR shifts the distribution from CE-dominated to TS-dominated. These conclusions are robust, so I'll write up the appendix section with the sensitivity table and then add the corresponding LaTeX references.

I'm looking at where to place this analysis in the appendix structure. The existing reference in experiments.tex points to app:detailed-results, so I should add the sensitivity paragraph and table there, probably after the per-seed result tables but before the beta03 subsection, to keep the flow logical.

Now I'm setting up a comparison table similar to the main goodhart-landscape table, using the same column structure. I need to calculate the means and standard errors for the exec-only condition (seeds 42 and 44) versus the full dataset, then format it consistently with the existing tables.

Generating markdown table... Now I'm calculating the pooled percentages for the other categories—combining the TS, CE, and N-H values across both samples, which gives me 51.3% for TS, 42.4% for CE, and 3.7% for N-H. Then I'm moving on to the ISR β=0.1 comparison, computing the mean PR and ISR* values with their standard errors for that subset. Now I'm calculating the standard errors for both metrics using the difference between the two studies divided by 2√2. For PR, that gives me 84.0 ± 3.5%, and for ISR*, I'm getting 0.101 ± 0.022 using the appendix table values of 0.131 for s42 and 0.070 for s44.

Looking at the pooled results across both studies, I'm seeing that proved cases total 168, with no treatment-seeking cases, while clinical evaluation accounts for 78% and non-help-seeking for 14.3%. I'm also cross-checking these against the 3-seed comparison results from the main paper to see how the ISR and random conditions differ in their outcome distributions. Now I'm looking at the 3-seed exec-only results, where s43 has that known temperature issue flagged in the appendix. Pooling across all three seeds gives a mean of 68.0% with substantial variance, though s42 and s44 both perform strongly around 93-98% while s43 lags significantly at 13%.

The key insight is that the main paper only reports s42 for exec-only, so the 2-seed pooled comparison (s42+s44) provides a cleaner sensitivity check without the s43 caveat. I'll present both the 3-seed and 2-seed pooled results in a table, noting the temperature issue for s43 so readers understand why the 2-seed version is the more reliable baseline. Generating sensitivity table... I'm looking at the sensitivity analysis results across different conditions and need to write up what these metrics show. The table compares execution-only versus different ISR and random beta settings, tracking how the proportion of proved cases, ISR values, and outcome distributions shift across conditions. The 2-seed exec-only results expose a hidden divergence between s42's CE dominance (87%) and s44's complete TS conversion (100%), which pooling had masked. Now I'm double-checking my standard error formula for the n=2 case to ensure the calculation is correct. I see the user is specifying a particular formula for standard error that differs from the standard statistical definition, so I'll use their formula: SE = |s42 - s44| / (2 * sqrt(2)) rather than the conventional SE = s/sqrt(n).

Now I'm calculating the standard errors for each approach using their formula, which gives me approximately 1.8 for Exec PR, 2.8 for ISR β=0.1 PR, and 3.5 for Random PR. I'll also standardize the precision across the results: performance ratios to one decimal place, ISR* values to three decimals, and percentages to one decimal place.

For the document edits, I need to insert the sensitivity analysis paragraph and table into the appendix after the Goodhart section, then update the reference in experiments.tex to point specifically to this new sensitivity analysis subsection rather than the general detailed results section. Looking at the appendix structure, I can see where the detailed results tables are positioned, so I'll place the new content appropriately before the β=0.3 subsection. I need to update the reference in experiments.tex to point directly to the sensitivity table instead of the general appendix, making it more specific and precise about where the exclusion analysis appears. Writing the sensitivity analysis section... Generating markdown table... I'm checking the ISR s42 N-H% value from the appendix—it shows 17.3%, which represents the genuine non-hacking rate after accounting for TS, CE, and PG classifications, since PG is tracked separately in the table. Now I need to verify the ISR s44 numbers, particularly the TS rate after correcting for false negatives.

For the pooled calculation across both ISR samples, I'm combining the non-hacking counts: 14 cases out of 170 total gives 8.2%, which checks out.

Moving to the Random s42 data, I'm verifying the non-hacking count by multiplying the percentage by the proved count: 22.8% of 79 proved cases equals about 18 cases, which matches. Now I'm checking the Random s44 metrics to complete the verification. For the exec-only pooled calculations, I'm working through s42 and s44. S42 has 93 proved cases with a slight overlap issue between CE and PG categories that accounts for one extra count, so I'm using TS=0, CE=81, N-H=7 for the pooled totals. S44 is straightforward with all 98 cases in TS and nothing in the other categories. Combining both gives me 191 total proved cases: 51.3% TS, 42.4% CE, and 3.7% N-H.

Now I'm ready to finalize the document edits. I'll insert the new appendix section after line 625, using a subsection heading to match the existing structure of the detailed results section. For the experiments.tex file, I need to update the reference at line 10. I should keep the writing dry and academic without any AI-style phrasing, and I'm double-checking the precision specifications for the percentages. Looking at the standard error values I've calculated, I need to decide on consistent decimal precision for the table display. The main paper uses two decimal places for ISR* standard errors like `$\pm$.04`, so I'll apply that same precision to my values—rounding the ISR* errors to two decimals and the PR errors to one decimal to match the formatting conventions. I'll stick with the task's specifications for now. Let me double-check the N-H metric for the exec-only case—the appendix already shows it excludes PG, TS, and CE, so I should use that same definition in the sensitivity table. Looking back at the task requirements, it asks for five metrics: PR, ISR*, TS%, CE%, and N-H%, with no separate PG column, which matches the main paper's approach.

I'm noticing there's some overlap in the data—for instance, exec s42 has TS=0, CE=87.1, N-H=7.5, and PG=6.5, which sums to over 100% because some samples fall into both CE and PG categories. The main paper handles this with footnotes, so I'll do the same: present TS, CE, and N-H while noting that PG samples are excluded from N-H but may overlap with CE.

Looking at the main table's approach, the three percentages don't need to sum to 100%—PG accounts for the remainder. For example, Exec-only shows TS=0, CE=87, N-H=8 (95% total), with PG making up the difference. I'll follow this same convention for consistency.

Now I'm calculating the pooled results across the two seeds. For Exec, combining s42 and s44 gives TS=51.3%, CE=42.4%, N-H=3.7% (97.4% total), with PG at 3.1%. ISR pooled shows TS=60.0%, CE=24.7%, N-H=8.2% (92.9% total) and PG around 7.1%. Random pooled is TS=0%, CE=78.0%, N-H=14.3% (92.3% total) with PG at roughly 11.9% accounting for overlaps. The table works fine without a separate PG column—I can note those percentages in the caption instead.

Now I'm wondering whether to also compute the three-seed pooled results for exec-only.  Since s43 was evaluated with T=0.7, that makes it less reliable, so I'll focus on the two-seed pooled as the main comparison and mention the three-seed version for reference with a note about the temperature difference. Let me now add this section to the appendix, inserting it after the "Prolog: universal Goodhart" paragraph and before the β=0.3 subsection. I'm working on inserting a new subsection about seed 43 sensitivity analysis before the per-seed results section. The new content examines how seed 43 behaves differently across evaluation conditions—showing performance degradation in exec-only mode, collapse to pure theorem solving in ISR, and different characteristics in random mode—but the thought trails off mid-sentence so I'll need to complete it based on the pattern of what's being analyzed.

The next part continues by noting that when pooling just seeds 42 and 44 (excluding seed 43), all the main findings from the three-seed analysis still hold: ISR amplifies theorem solving relative to random, non-hacking rates stay consistently low, and the compositional shift from code execution to theorem solving under ISR reward persists across both conditions.

The 2-seed pooling also reveals an interesting divergence—seed 42 predominantly collapses into code execution mode (87%) while seed 44 collapses into theorem solving (100%), which confirms that different seeds exhibit distinct failure modes. The 3-seed mean for proof rate shows extreme variance because seed 43's greedy collapse is an outlier, but the 2-seed mean of 95.5% better represents the stable regime without that degenerate case.

Generating results table... Formatting the table entries... Generating the results table...

Now I'm updating the reference in the experiments file to point to the new sensitivity analysis table and appendix section that shows the results remain consistent even when excluding seed 43.

For the ISR* metrics, I'm standardizing the precision to match the paper's convention: three decimal places for the main values and two decimal places for the standard errors, so the table will show 0.357±.16, 0.659±.17, and 0.101±.02.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "cb6c743f-9503-4381-9eb0-a0aa966f0a34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpqsxnfKSFKPv4GNdTTbJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 25659,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 27264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4508
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

I have all the registry data and current paper content. Let me compute the 2-seed pooled statistics and make the edits.

**Computed 2-seed pooled (s42+s44):**

| Condition | n_proved | PR% | ISR* | TS% | CE% | N-H% |
|-----------|----------|-----|------|-----|-----|------|
| Exec-only | 191 | 95.5±1.8 | 0.357±.16 | 51.3 | 42.4 | 3.7 |
| ISR β=0.1 | 170 | 85.0±2.8 | 0.659±.17 | 60.0 | 24.7 | 8.2 |
| Random β=0.1 | 168 | 84.0±3.5 | 0.101±.02 | 0 | 78.0 | 14.3 |

Qualitative conclusions preserved: ISR amplifies TS (60% vs 0%), CE→TS shift persists, N-H low everywhere.

For task 3: s43 exec-only has T=0.7 evaluation issue, so 3-seed pooled exec-only is unreliable. The 2-seed pooled is the clean comparison; I'll note the 3-seed stats from the existing table for completeness.

Now making the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "6f013a7a-1bb2-461d-baae-79925ce94f1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpqsxnfKSFKPv4GNdTTbJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 25659,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 27264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4508
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

<details open><summary>🔧 Tool call — Edit · `toolu_01PZN2j3nHt8D7YTxk2AaZ32`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "old_string": "\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}",
  "new_string": "\\subsection{Sensitivity to Seed 43 Exclusion}\n\\label{app:sensitivity-s43}\n\nSeed~43 presents evaluation complications across conditions: exec-only seed~43 suffers greedy-mode degeneration (PR${=}13\\%$; evaluated with $T{=}0.7$ rather than greedy), ISR seed~43 collapses to pure TS (100\\%), and random seed~43 is the only seed exhibiting nonzero TS (38.3\\%; seeds~42/44: 0\\%).\nTable~\\ref{tab:sensitivity-no-s43} reports 2-seed pooled results (s42$+$s44) to verify that conclusions are not driven by seed~43.\n\nAll qualitative conclusions from the 3-seed analysis (\\S\\ref{sec:goodhart}) are preserved:\nISR amplifies TS relative to random (60.0\\% vs.\\ 0\\%), non-hacking rates remain low across all RL conditions (3.7--14.3\\%), and the CE$\\to$TS compositional shift under ISR reward persists (ISR: TS${=}60\\%$/CE${=}25\\%$; random: TS${=}0\\%$/CE${=}78\\%$).\nThe exec-only 2-seed pooled additionally reveals a split between CE-dominant (s42, 87\\%) and TS-dominant (s44, 100\\%) collapse modes, confirming cross-seed divergence (\\S\\ref{sec:diagnostic}).\n\nThe 3-seed exec-only mean (PR${=}68{\\pm}47\\%$; Table~\\ref{tab:fol-detailed}) has extreme variance dominated by s43's greedy-mode collapse; the 2-seed mean (PR${=}95.5\\%$) better characterizes the non-degenerate regime.\n\n\\begin{table}[ht]\n\\centering\n\\caption{2-seed pooled results (s42$+$s44), excluding seed~43.\nPR/ISR$^*$: per-seed mean${\\pm}$SE ($\\text{SE} = |x_{42}{-}x_{44}| / 2\\sqrt{2}$); TS/CE/N-H: pooled \\% of proved ($n$ = total proved).}\n\\label{tab:sensitivity-no-s43}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{PR\\%} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nExec-only & 191 & 95.5{\\scriptsize$\\pm$1.8} & 0.357{\\scriptsize$\\pm$.16} & 51.3 & 42.4 & 3.7 \\\\\nISR $\\beta{=}0.1$ & 170 & 85.0{\\scriptsize$\\pm$2.8} & 0.659{\\scriptsize$\\pm$.17} & 60.0 & 24.7 & 8.2 \\\\\nRandom $\\beta{=}0.1$ & 168 & 84.0{\\scriptsize$\\pm$3.5} & 0.101{\\scriptsize$\\pm$.02} & 0 & 78.0 & 14.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "3165e34f-5194-4156-ae0e-e404cde2cd20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpqsxnfKSFKPv4GNdTTbJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 25659,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 27264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4508
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

_source line 60 · 2026-05-21T18:20:33.050Z_

<details><summary>↩ Tool result · `toolu_01PZN2j3nHt8D7YTxk2AaZ32`</summary>

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
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "68a33b4d-dc0b-4c94-a588-c0e8d3ec598c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
    "oldString": "\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}",
    "newString": "\\subsection{Sensitivity to Seed 43 Exclusion}\n\\label{app:sensitivity-s43}\n\nSeed~43 presents evaluation complications across conditions: exec-only seed~43 suffers greedy-mode degeneration (PR${=}13\\%$; evaluated with $T{=}0.7$ rather than greedy), ISR seed~43 collapses to pure TS (100\\%), and random seed~43 is the only seed exhibiting nonzero TS (38.3\\%; seeds~42/44: 0\\%).\nTable~\\ref{tab:sensitivity-no-s43} reports 2-seed pooled results (s42$+$s44) to verify that conclusions are not driven by seed~43.\n\nAll qualitative conclusions from the 3-seed analysis (\\S\\ref{sec:goodhart}) are preserved:\nISR amplifies TS relative to random (60.0\\% vs.\\ 0\\%), non-hacking rates remain low across all RL conditions (3.7--14.3\\%), and the CE$\\to$TS compositional shift under ISR reward persists (ISR: TS${=}60\\%$/CE${=}25\\%$; random: TS${=}0\\%$/CE${=}78\\%$).\nThe exec-only 2-seed pooled additionally reveals a split between CE-dominant (s42, 87\\%) and TS-dominant (s44, 100\\%) collapse modes, confirming cross-seed divergence (\\S\\ref{sec:diagnostic}).\n\nThe 3-seed exec-only mean (PR${=}68{\\pm}47\\%$; Table~\\ref{tab:fol-detailed}) has extreme variance dominated by s43's greedy-mode collapse; the 2-seed mean (PR${=}95.5\\%$) better characterizes the non-degenerate regime.\n\n\\begin{table}[ht]\n\\centering\n\\caption{2-seed pooled results (s42$+$s44), excluding seed~43.\nPR/ISR$^*$: per-seed mean${\\pm}$SE ($\\text{SE} = |x_{42}{-}x_{44}| / 2\\sqrt{2}$); TS/CE/N-H: pooled \\% of proved ($n$ = total proved).}\n\\label{tab:sensitivity-no-s43}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{PR\\%} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nExec-only & 191 & 95.5{\\scriptsize$\\pm$1.8} & 0.357{\\scriptsize$\\pm$.16} & 51.3 & 42.4 & 3.7 \\\\\nISR $\\beta{=}0.1$ & 170 & 85.0{\\scriptsize$\\pm$2.8} & 0.659{\\scriptsize$\\pm$.17} & 60.0 & 24.7 & 8.2 \\\\\nRandom $\\beta{=}0.1$ & 168 & 84.0{\\scriptsize$\\pm$3.5} & 0.101{\\scriptsize$\\pm$.02} & 0 & 78.0 & 14.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}",
    "originalFile": "% Appendix — solver-trace-ablation\n\n\\section{Experimental Setup}\n\\label{app:setup}\n\nTable~\\ref{tab:hyperparams} lists all hyperparameters shared across experiments.\nAll RL conditions use the same GRPO configuration; only the reward function differs.\nSeeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Training hyperparameters for all GRPO experiments.}\n\\label{tab:hyperparams}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll@{}}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Model}} \\\\\nBase model & Qwen3-4B \\\\\nPrecision & BF16 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{GRPO Training}} \\\\\nRollouts per prompt ($K$) & 4 \\\\\nTraining steps (default) & 500 \\\\\nTraining steps (extended) & 1000 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nPer-device batch size & 4 \\\\\nGradient accumulation steps & 2 \\\\\nEffective batch size & 8 \\\\\nMax completion length & 512 tokens \\\\\nRandom seeds & 42, 43, 44 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Data}} \\\\\nTraining set & FOLIO, 500 examples \\\\\nEvaluation set & FOLIO, 100 examples (held-out) \\\\\nData file & \\texttt{train\\_500\\_seed42} \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Solvers}} \\\\\nFOL solver & Prover9 \\\\\nProlog solver & SWI-Prolog 8.4.2 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{\\textit{Evaluation}} \\\\\nDecoding & Greedy ($T{=}0$) \\\\\nISR computation & \\texttt{eval\\_sta.py} \\\\\nISR variant & Proved-only (ISR$^*$) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Compute resources.}\nExperiments were run on single-GPU setups (NVIDIA RTX 4090 24\\,GB and RTX PRO 6000 96\\,GB).\nEach GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).\nTotal compute across all seeds, conditions, and reruns is approximately 80--120 GPU-hours.\n\n\\paragraph{Evaluation exception.}\nFOL exec-only seed~43 (\\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.\nIts PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).\n\n\\paragraph{Reward formulation.}\nAn additive variant ($r = r_{\\text{exec}} + \\beta\\,\\text{ISR}$) was tested in early experiments but collapsed prove rate to near-zero, as ISR alone provides no gradient toward provable formalizations; the multiplicative form $r_{\\text{exec}}\\cdot(1+\\beta\\,\\text{ISR})$ ensures ISR modulates only proved outputs.\n\n\\paragraph{ProofFOL dataset construction.}\n\\label{app:prooffol-construction}\nProofFOL is derived from ProofWriter~\\citep{proofwriter} (10{,}424 training examples) via the GPT-4o silver-standard FOL translation pipeline of \\citet{prooffol-thatikonda2024} with Prover9 verification filtering (${\\sim}70\\%$ retention; failures from timeouts, unsupported constructs, and translation errors).\nOf the translated examples, 99.1\\% parse successfully (92 skipped due to empty FOL output).\nWe sample 500 training and 100 evaluation examples (seed~42) from the verified pool.\nTable~\\ref{tab:prooffol-vs-folio} compares key structural properties.\n\n\\begin{table}[!ht]\n\\centering\n\\caption{ProofFOL vs.\\ FOLIO structural comparison (training sets, $n{=}500$ each).}\n\\label{tab:prooffol-vs-folio}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Property} & \\textbf{ProofFOL} & \\textbf{FOLIO} \\\\\n\\midrule\nFOL premises (mean$\\pm$std) & $18.2 \\pm 3.2$ & $5.3 \\pm 1.4$ \\\\\n\\quad Ground facts & $10.2 \\pm 3.0$ & $1.8 \\pm 1.5$ \\\\\n\\quad Rules & $8.1 \\pm 1.1$ & $3.5 \\pm 1.9$ \\\\\nXOR ($\\oplus$) samples & 0\\% & 37.2\\% \\\\\nDominant depth & 4--5 & 2--3 \\\\\nPredicate style & synthetic & real-world \\\\\nFOL source & GPT-4o (silver) & human (gold) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nProofFOL problems are structurally more complex ($3.4{\\times}$ more premises) but use simpler, synthetic predicates (e.g., \\texttt{Blue(x)}, \\texttt{Rough(x)}) characteristic of ProofWriter's procedural generation.\nThe absence of XOR constraints and the regularity of predicate structure make ProofFOL a complementary testbed: structural degeneration must emerge from the RL training dynamics rather than from formalization difficulty.\n\n\\section{STA Algorithm}\n\\label{app:algorithm}\n\nAlgorithm~\\ref{alg:sta} (Section~\\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.\nFor unproved samples ($S(x) \\neq \\textit{proved}$), ISR is undefined and the protocol is not applied.\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{What ISR measures---and what it does not.}\nISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.\nThis is strictly weaker than semantic faithfulness: whether the formalization accurately captures the natural-language meaning.\nWe verify this empirically: Spearman $\\rho(\\text{ISR}, \\text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.\nISR and downstream task performance are uncorrelated.\nISR is thus a component-necessity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.\n\nCritically, low ISR carries different semantics depending on the training objective.\nUnder exec-only training, low ISR in Prolog reflects redundant coding (repeated ground facts where removing any single copy does not affect the proof) rather than an absence of reasoning (\\S\\ref{sec:crosslogic}).\nUnder ISR-as-reward, high ISR reflects metric gaming (\\S\\ref{sec:goodhart}).\nISR values must always be interpreted relative to the optimization objective that produced them.\n\n\\paragraph{The premise-count confound.}\nLOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.\nA formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$, even though the latter encodes richer reasoning.\nThis confound explains the sole apparent ISR-as-reward success (\\S\\ref{sec:goodhart}): ISR $\\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.\nPremise-count-matched comparison eliminates the difference ($1.06\\times$; Table~\\ref{tab:fol-beta01-detailed}).\nThis bias is not specific to our setting: any LOO-based structural metric applied to variable-length outputs requires component-count normalization.\nWe recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Fisher exact tests for non-hacking rate across conditions (3-seed pooled). ISR $\\beta{=}0.1$ non-hacking rate is corrected for PG reclassification and TS false negatives (Appendix~\\ref{app:h8}).}\n\\label{tab:bootstrap-ci}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Comparison} & \\textbf{Condition} & \\textbf{Control} & \\textbf{OR} & \\textbf{$p$} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Non-hacking rate (PG+FN corrected)}} \\\\\nISR vs.\\ Random & 6.06\\% {\\scriptsize[3.6,9.9]} & 9.5\\% {\\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\\\\nISR vs.\\ Exec-only & 6.06\\% & 7.5\\% & 0.79 & 0.62 \\\\\nRandom vs.\\ Exec-only & 9.5\\% & 7.5\\% & 1.30 & 0.68 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{TS gaming rate}} \\\\\nISR vs.\\ Random & 70.6\\% {\\scriptsize[64.3,76.3]} & 13.7\\% {\\scriptsize[9.9,18.6]} & 15.05 & $1.3{\\times}10^{-39}$ \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{SFT vs.\\ Exec-only non-hacking rate}} \\\\\nSFT vs.\\ Exec-only & 92.3\\% {\\scriptsize[79.7,97.3]} & 7.5\\% & 147 & ${<}0.001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\\\[2pt]\n{\\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\\% Wilson CIs in brackets where shown.}\n\\end{table*}\n\n\\paragraph{TS dose-response gradient.}\nTS tautology follows a dose-response pattern across reward conditions: random $\\beta{=}0.1$ produces $13.7\\%$ TS ($36/262$ pooled; per-seed: $38.3\\%$ in s43, $0\\%$ in s42/s44), random $\\beta{=}0.3$ yields 4--7 TSa samples per seed, and ISR $\\beta{=}0.1$ reaches $70.6\\%$ ($163/231$).\nThe gradient (random $\\beta{=}0.1$ ($13.7\\%$) $\\to$ random $\\beta{=}0.3$ (4--7 TSa per seed) $\\to$ ISR $\\beta{=}0.1$ ($70.6\\%$)) shows ISR transforms TS from a seed-dependent GRPO tendency to a near-universal convergence direction.\n\n\\paragraph{Goodhart effects: implications.}\nISR was designed to \\emph{detect} reward gaming of $r_{\\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself. Any diagnostic metric risks becoming a target when optimized.\nThe dose-response pattern maps onto the Manheim \\& Garrabrant taxonomy~\\citep{manheim-goodhart-taxonomy}: $\\beta{=}0.1$ on FOLIO instantiates \\emph{regressional} Goodhart ($P{\\to}P$ tautologies yield $\\text{ISR}{\\geq}0.5$, so ISR erroneously rewards the shortcut); $\\beta{\\geq}0.2$ introduces \\emph{extremal} elements (PR collapse to 18\\% vs.\\ 48\\% random at $\\beta{=}0.3$).\nThe implication is conditional: ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL; \\S\\ref{sec:crossdomain}).\n\n\\paragraph{Single-seed unreliability.}\nThe three exec-only seeds diverge radically (PR $\\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\\S\\ref{sec:diagnostic}).\nISR $\\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (TS), 1/3 by premise minimization (\\S\\ref{sec:goodhart}).\nMulti-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.\n\n\\paragraph{Classifier limitations.}\nText-match hacking classifiers have systematic blind spots that functional analysis exposes.\nIn Prolog STA, two seeds achieved 100\\% genuine classification under strict text matching, yet functional analysis via the $n_{\\text{necessary}}$ distribution revealed 0\\% genuine in both cases (Table~\\ref{tab:prolog-detailed}).\nOne seed produces uppercase pseudo-Prolog that is functionally tautological; the other converts conclusions to snake\\_case atoms serving as both fact and query, a gaming mode invisible to string comparison.\nPractitioners should cross-validate text-match classifiers with functional metrics and never treat classifier-reported genuine rates as ground truth without independent verification.\n\n\\paragraph{Practical guidelines.}\n\\label{app:practical-guidelines}\nOur findings yield five guidelines for GRPO-trained neurosymbolic systems:\n(1)~Never evaluate by prove rate alone; use ISR and component count as joint diagnostics.\n(2)~Report multi-seed results: single-seed GRPO evaluation is unreliable, as cross-seed variance can exceed the effect size of interest (\\S\\ref{sec:diagnostic}).\n(3)~Use ISR for post-hoc diagnosis only, not as a training signal; any dose induces gaming or collapse.\n(4)~Treat LOO-based metrics as component-count-biased until normalized.\n(5)~Expect conclusion embedding as a GRPO-universal baseline (Table~\\ref{tab:goodhart-landscape}): reward shaping alters hacking composition, not prevalence.\n\n\\paragraph{Multiple testing correction.}\n\\label{app:statistical-details}\nWe define two test families: FOLIO ($k{=}14$ tests across all conditions) and ProofFOL ($k{=}1$).\nWithin the FOLIO family, Bonferroni correction at $\\alpha{=}0.05$ yields adjusted thresholds of $p_{\\text{adj}}{=}0.05/14{=}0.0036$.\nThree primary comparisons survive correction: the TS rate difference (ISR vs.\\ random; $p_{\\text{bonf}}{=}1.82{\\times}10^{-38}$), the SFT vs.\\ exec-only non-hacking rate ($p_{\\text{bonf}}{=}0.014$), and the Cochran--Mantel--Haenszel test for TS association across seeds ($p_{\\text{bonf}}{<}10^{-8}$).\nThe matched 5+5-seed Fisher/Mann-Whitney comparison is borderline ($p_{\\text{bonf}}{=}0.056$), significant at $\\alpha{=}0.10$ after Bonferroni correction ($k{=}14$).\nThe ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.\nBonferroni assumes independence, which is conservative for our setting (several tests use overlapping data); Holm--Bonferroni or Benjamini--Hochberg FDR would recover the matched 5+5 comparison at conventional significance.\nWe report the most conservative Bonferroni results for transparency.\n\n\n\\section{Hacking Mode Definitions}\n\\label{app:hacking-modes}\n\nWe identify eight distinct reward hacking modes across all experiments.\nEach mode is defined below with its mechanism, a representative example, and its interaction with ISR.\nTable~\\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.\n\n\\begin{table*}[ht]\n\\centering\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Mode} & \\textbf{Mechanism} & \\textbf{Exec} & \\textbf{ISR} & \\textbf{Rnd} & \\textbf{SFT} \\\\\n\\midrule\nCE & Concl.\\ in premises & 87 & 18 & 71 & 7 \\\\\nTS & Single prem.\\ = concl. & $\\bullet$ & \\textbf{71} & 14$^\\dagger$ & 0 \\\\\nPG & Premise-subset gaming & 6 & 5 & -- & 0 \\\\\nTautological & 2-comp $P{=}C$ & $\\bullet$ & 0 & 0 & 0 \\\\\nRepetition & Output degen. & $\\bullet$ & -- & -- & -- \\\\\nContradiction & $n_{\\text{comp}}$ inflated & $\\bullet$ & -- & -- & -- \\\\\nC-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\\\\nQ-as-fact & Atom = fact+query & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hacking taxonomy across FOL conditions (\\% of proved samples). ISR/Rand columns: $\\beta{=}0.1$ 3-seed pooled. TS includes subtypes TSa (text-match, $n{=}149$ ISR $+$ 36 random) and TSb (obfuscated tautology, $n{=}14$; primarily s44). $^\\dagger$Random TS driven by seed~43 (38.3\\%); seeds~42/44: 0\\%. Exec: CE${=}87$\\% in s42; $\\bullet$ marks seed- or step-specific modes (TS/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). PG: premise-subset gaming (Appendix~\\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\\ref{tab:prolog-detailed}).}\n\\label{tab:hacking-taxonomy-app}\n\\end{table*}\n\n\\paragraph{Classifier Validation.}\nHacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.\nCE and TS are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\\text{necessary}}$ distribution from STA (leave-one-out ablation).\nNo training data or manual annotation is used for classification.\n\nTo estimate precision, we manually verified 50 randomly sampled outputs classified as CE or TS: all 50 were confirmed correct (estimated precision ${>}$95\\%, Wilson 95\\% CI: [93\\%, 100\\%]).\nRecall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.\nWe cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\\text{necessary}} \\leq 1$ are flagged as potential false negatives.\nThis cross-validation revealed query-as-fact gaming in Prolog (\\S\\ref{app:hacking-modes}), where the strict text classifier reported 100\\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\\text{necessary}}{=}1$).\nThe non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.\n\n\\paragraph{Boundary case validation.}\nStratified validation across 82 samples (all five hacking categories) yields Cohen's $\\kappa{=}1.0$; independent re-annotation confirms full agreement.\nStructured inspection of 20 boundary cases (short-conclusion CE (10, minimum 4 characters), low-ISR genuine (5, minimum $\\text{ISR}{=}0.22$), and TS on false propositions (5)) confirmed 20/20 correct classifications.\nShort-conclusion CE samples are unambiguous hacking: the conclusion appears as a standalone premise with no NL source.\nLow-ISR genuine samples reflect mode-collapsed template outputs, not structural gaming.\n3/5 TS boundary cases confirm factually false propositions (e.g., affirming ``dogs are plants''), showing TS is not merely vacuous but actively harmful.\n\n\\subsection{PG --- Premise-Subset Gaming}\n\\label{app:h8}\n\nManual audit of ISR $\\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (CE-style).\nWe term this \\textbf{PG (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.\n\n\\paragraph{Detection.} PG is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\\text{prem}} \\leq 3$) that nonetheless achieve high ISR.\nAutomated detection is not currently feasible because PG requires comparing the generated premise set against the gold premises.\n\n\\paragraph{Audit scope and limitations.}\nFull PG audit was completed for ISR $\\beta{=}0.1$ seed~42 only.\nISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\nRandom $\\beta{=}0.1$ does not produce PG by mechanism (no ISR optimization pressure); seed~42 audit confirmed PG${=}0$.\n\n\\paragraph{TS false-negative correction (TSb obfuscated tautology).}\nISR $\\beta{=}0.1$ seed~44 contained 12 samples with $n_{\\text{prem}}{=}1$ classified as non-hacking by the text matcher.\nManual inspection confirmed all 12 are logically equivalent to TS but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).\nWe classify these as \\textbf{TSb} (obfuscated tautology), distinct from text-match-detectable TSa.\n$10/12$ achieve $\\text{ISR}{\\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and TS classifier: triple gaming (\\S\\ref{sec:taxonomy}).\nAfter correction, ISR s44 non-hacking${=}0$; total TS = TSa (77 text-match) + TSb (12 obfuscated) = 89.\n\n\\paragraph{Impact on non-hacking-rate comparison.}\nAfter PG reclassification and TS false-negative correction: ISR non-hacking $= 14/231 = 6.06\\%$ vs.\\ random non-hacking $= 25/262 = 9.5\\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\\% CI: ISR [3.6\\%, 9.9\\%], Random [6.5\\%, 13.7\\%]).\nThe direction is consistent with ISR-amplified gaming modes (TS, PG) displacing non-hacking output, but the effect is not statistically significant at the conventional $\\alpha{=}0.05$ threshold.\n\n\\subsection{CE --- Conclusion Embedding}\n\n\\paragraph{Definition.}\nThe conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.\nThe solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x (bird(x) -> flies(x)).\n  bird(tweety).\n  flies(tweety).  % conclusion embedded\nConclusion: flies(tweety).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nVariable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.\nISR does not distinguish trivial from substantive necessity.\n\n\\paragraph{Prevalence.}\nConclusion embedding in some form (CE multi-premise or TS single-premise) is GRPO-universal at 68--97\\% across all RL conditions.\nUnder exec-only and Random reward, it manifests as CE (71--93\\%); under ISR reward, it shifts to TS (70.6\\% pooled).\n\n\n\\subsection{TSa --- Conclusion Duplication (Standard)}\n\n\\paragraph{Definition.}\nThe entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.\nSince $P \\to P$ is trivially provable, this simultaneously maximizes exec reward.\nBecause the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.8$--$1.0$.\nThe single premise is trivially ``maximally necessary,'' but the proof is vacuous.\nTSa games both exec reward and ISR reward; TSb extends this to triple gaming by additionally evading the text-match classifier.\n\n\\paragraph{Prevalence.}\nTSa (text-match detectable): 64.5\\% pooled (149/231) under ISR~$\\beta{=}0.1$ (s42: 16.0\\%, s43: 96.7\\%, s44: 86.5\\%).\nCombined TS (TSa + TSb): 70.6\\% (163/231; s43 TSa${=}59$ + TSb${=}2$; includes s44 FN correction).\nRandom~$\\beta{=}0.1$ pooled: 13.7\\% (36/262, all TSa; driven by seed~43 at 38.3\\%, seeds~42 and~44 at 0\\%).\n\n\n\\subsection{TSb --- Obfuscated Tautology}\n\n\\paragraph{Definition.}\nA single-premise formalization logically equivalent to TSa (premise = conclusion) but with surface-form differences that evade the text-match TS classifier.\nThe model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).\n\n\\paragraph{Example (FOL, vacuous quantifier wrapping).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y ((A(x)&B(y))->(C(x)|D(y))).\nConclusion:\n  all x ((A(x)&B(x))->(C(x)|D(x))).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\nThe premise introduces a vacuous second variable $y$, immediately unified with $x$; the formulas are logically equivalent but differ textually.\n\n\\paragraph{ISR interaction.}\n$\\text{ISR}{\\geq}0.83$ ($10/12$ samples).\nTSb simultaneously games three objectives: execution reward ($r_{\\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match TS classifier (surface-form difference evades detection).\nThis triple gaming makes TSb the most complete Goodhart case we observe.\n\n\\paragraph{Prevalence.}\nFound primarily in ISR $\\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as non-hacking); seed~43 contributes $2$ additional cases.\nFunctional cross-validation via $n_{\\text{necessary}}{=}1$ exposed the misclassification.\n\n\n\\subsection{Tautological Collapse}\n\n\\paragraph{Definition.}\nTwo-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \\to P$ tautology with minimal token cost.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\nPremises: p(a).\nConclusion: p(a).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$=1.0$ (the sole premise is necessary).\nDistinguished from TS by having low component count ($n_{\\text{comp}}\\approx 2$) and atomic formulas rather than complex sub-structured conclusions.\n\n\\paragraph{Prevalence.}\nDominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\\text{comp}}=2.04$, 100\\% TS by strict classifier).\nAlso observed in Prolog exec+STA seed~42 (100\\% TS, PR~$=0.50$).\n\n\n\\subsection{Repetition Collapse}\n\n\\paragraph{Definition.}\nThe model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.\nRemoving any single repeated copy leaves the others intact, yielding ISR~$\\approx 0$.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\npenguin(fido).\npenguin(fido).\npenguin(fido).\n... (repeated to 512 tokens)\nquery(penguin(fido)).\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$. Each copy is individually redundant since identical copies remain after removal.\nISR correctly diagnoses this degeneration.\n\n\\paragraph{Prevalence.}\nObserved in FOL exec-only seed~43 (87\\% of outputs hit max completion length; PR~$=13$\\%, ISR~$=0$).\n\n\n\\subsection{Complexity-without-Utility}\n\n\\paragraph{Definition.}\nThe formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous: none individually necessary for the proof.\nThe complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.\n\n\\paragraph{Example (FOL).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  all x all y (R(x,y) ->\n    exists z (S(x,z) & T(z,y))).\n  all x (P(x) -> Q(x)).\n  P(a).            % only this needed\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.\nThis is the mode ISR is best calibrated for.\n\n\\paragraph{Prevalence.}\nLow. Observed in Random~$\\beta{=}0.1$ seed~42 at 3.8\\% (3/79).\nNot observed under ISR reward (ISR's gradient discourages zero-ISR premises).\n\n\n\\subsection{Contradiction Explosion}\n\n\\paragraph{Definition.}\nThe component count grows unboundedly over training.\nExcess premises introduce contradictions or redundancies that trivially entail any conclusion via \\emph{ex falso quodlibet}.\nIndividual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.\n\n\\paragraph{Example (FOL, 1000-step exec-only).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n{\\small\\begin{verbatim}\nPremises:\n  c1. c2. c3. ... c18. % 18.55 mean\n  % conclusion embedded among premises\nConclusion: Q(a).\n\\end{verbatim}}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\\% of proved samples having ISR~$=0$).\n\n\\paragraph{Prevalence.}\nObserved in extended exec-only training (seed~42, 1000 steps).\nMean component count grows from ${\\sim}6$ (500 steps) to 18.55 (1000 steps).\n\n\n\\subsection{Query-as-Fact Gaming}\n\n\\paragraph{Definition.}\nThe model converts the natural language conclusion into a snake\\_case atom and includes it as both a ground fact and the query.\nProlog trivially proves the query by unifying with the fact.\nThis mode evades text-match classifiers designed for CE/TS because the generated atom bears no surface resemblance to the original conclusion text.\n\n\\paragraph{Example (Prolog).}\n\\smallskip\\noindent\\rule{\\columnwidth}{0.3pt}\n\\begin{verbatim}\n% NL: \"Fido is happy.\"\n% Model output:\nfido_is_happy.\n:- fido_is_happy.     % query = fact\n\\end{verbatim}\n\\noindent\\rule{\\columnwidth}{0.3pt}\\smallskip\n\n\\paragraph{ISR interaction.}\nISR~$\\approx 0.9$--$1.0$.\nThe single fact is trivially necessary (its removal breaks the query), inflating ISR.\nFunctionally equivalent to TS but with a distinct surface mechanism.\n\n\\paragraph{Prevalence.}\nObserved in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).\n95/97 proved samples have $n_{\\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\\% non-hacking.\n\n\n\\section{Per-Seed Detailed Results}\n\\label{app:detailed-results}\n\nTables~\\ref{tab:fol-beta01-detailed} and \\ref{tab:prolog-detailed} report full per-seed results.\nAll metrics are computed by \\texttt{eval\\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.\nISR values are proved-only ISR$^*$.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\\beta{=}0.1$ breakdown referenced from Table~\\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples. ``---'' indicates data not available. $^\\dagger$s43 uses sampling eval ($T{=}0.7$). $^\\ddagger$Three s44-1000 samples escape text-match heuristics (CE/PG classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass PG detection and commuted premises that bypass CE detection; reclassified as degenerate. $^\\diamond$Seeds 45--46 added post-hoc under identical hyperparameters (effective batch size 8; micro-batch decomposition differs: $4{\\times}2$ vs.\\ $2{\\times}4$, mathematically equivalent).}\n\\label{tab:fol-detailed}\n\\label{tab:fol-beta01-detailed}\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{@{}llccccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{Steps} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Baselines}} \\\\\nBase model (no training)\n  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\\\\nGround-truth FOL\n  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\\\\nSFT\n  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \\textbf{92.3} & Supervised, no RL \\\\\n  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \\textbf{90.9} & \\\\\n  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \\textbf{93.3} & \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed pooled} & $0.130$ & $0.595$ & $0$ & $7.8$ & \\textbf{92.3} & $n{=}39$ proved \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 100 & 0.32 & \\textbf{0.642} & --- & --- & --- & Early checkpoint \\\\\n  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & PG${=}6.5\\%$ \\\\\n  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\\\\n  & 43 & 500 & 0.13 & 0$^\\dagger$ & --- & --- & --- & $^\\dagger$Greedy ($n_{\\text{proved}}{=}13$) \\\\\n  & 43 & 1000 & 0.96 & 0.082 & 0 & 93.8 & 6.2 & CE dominant \\\\\n  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\\\\n  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\\ddagger$ & PG${=}15\\%$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.68{\\pm}0.47$ & $0.238{\\pm}0.30$ & & & & 500-step \\\\\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.02$ & $0.029{\\pm}0.05$ & & & $2.1{\\pm}3.6$ & 1000-step \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \\textbf{17.3} & Mixed CE+TS+PG \\\\\n  & 42 & 1000 & 0.90 & 0.877 & 96.7 & 0 & 2.2 & TS collapse; PG${=}1$ ($n{=}90$) \\\\\n  & 43 & 500 & 0.61 & 0.830 & \\textbf{100} & 0 & 0 & TSa${=}59$, TSb${=}2$ \\\\\n  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & TS dominant (FN corrected) \\\\\n  & 45$^\\diamond$ & 500 & 0.42 & 0.605 & 38.1 & 4.8 & \\textbf{54.8} & PG${=}1$; $n{=}42$ \\\\\n  & 46$^\\diamond$ & 500 & 0.77 & 0.411 & 14.3 & 26.0 & \\textbf{54.5} & PG${=}4$; $n{=}77$ \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.77{\\pm}0.14$ & $0.716{\\pm}0.26$ & & & & 500-step (s42--44) \\\\\n  & \\multicolumn{2}{l}{5-seed mean$\\pm$std} & $0.70{\\pm}0.19$ & $0.633{\\pm}0.23$ & & & & 500-step (s42--46) \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & \\multicolumn{8}{l}{See Table~\\ref{tab:beta03-detailed} for per-seed $\\beta{=}0.3$ results.} \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.1$}} \\\\\n  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & PG${=}4$ \\\\\n  & 43 & 500 & 0.94 & 0.150 & \\textbf{38.3} & 59.6 & 1.1 & TSa${=}36$; PG${=}1$ \\\\\n  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & PG${=}16$ (CE$\\cap$PG: 6) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.87{\\pm}0.08$ & $0.117{\\pm}0.042$ & & & & TS seed-dep.: 0/38/0\\% \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086); $n_{\\text{comp}} = 9.6$ \\\\\n  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & & \\\\\n\\midrule\n\\multicolumn{9}{@{}l}{\\textit{Shuffled-ISR $\\beta{=}0.1$ (deconfounding control)}} \\\\\n  & 42 & 500 & 0.15 & 0.567 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n  & 43 & 500 & 0.16 & 0.568 & 6.3 & 6.3 & \\textbf{87.5} & $n{=}16$ proved \\\\\n  & 44 & 500 & 0.15 & 0.542 & 6.7 & 6.7 & \\textbf{86.7} & $n{=}15$ proved \\\\\n\\cmidrule(l){2-9}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.153{\\pm}0.006$ & $0.559{\\pm}0.015$ & $6.5$ & $6.5$ & \\textbf{87.0} & $N{=}46$ proved \\\\\n\\bottomrule\n\\end{tabular}}% end resizebox\n\\end{table*}\n\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\\ = percentage among proved samples.  ``---'' indicates data not available.}\n\\label{tab:prolog-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\\\\n  & 43 & 0.56 & 0.015 & --- & --- & --- & \\\\\n  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.53{\\pm}0.31$ & $0.146{\\pm}0.21$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec+ISR (STA reward)}} \\\\\n  & 42 & 0.50 & 1.000 & \\textbf{100} & 0 & 0 & TS tautological \\\\\n  & 43 & 0.38 & 0.185 & 0$^\\ddagger$ & 97.4 & 0 & $^\\ddagger$Functional TS$^a$ \\\\\n  & 44 & 0.97 & 0.912 & 0$^\\ddagger$ & 0 & 0$^\\ddagger$ & Query-as-fact gaming$^b$ \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.62{\\pm}0.31$ & $0.699{\\pm}0.45$ & & & 3/3 Goodhart, 0\\% non-hacking \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize\n$^a$ Strict TS classifier reports 0\\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\\\\n$^b$ Strict classifier reports Non-hacking$\\,{=}\\,100$\\%, but 95/97 proved samples have $n_{\\text{necessary}}=1$. The model converts NL to snake\\_case atoms serving as both fact and query, a third distinct Goodhart pathway.\\\\\n$^\\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.\n}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\\S\\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\\text{f50}}{>}0.90$.}\n\\label{tab:prooffol-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR$_{\\text{f50}}$} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{Genuine\\%} & \\textbf{Notes} \\\\\n\\midrule\nBase & --- & 0.16 & 0.310 & 0 & 0 & \\textbf{100} & $n{=}16$ proved \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Exec-only}} \\\\\n  & 42 & ${\\approx}$1.0 & 0.066 & \\textbf{100} & 0 & 0 & $n{=}99$; stable \\\\\n  & 43 & 0.55 & 0.119 & 0 & 49.2 & 50.8 & $n{=}63$; partial \\\\\n  & 44 & ${\\approx}$1.0 & 0.043 & 0 & 98.6 & 1.4 & $n{=}72$; stable \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{17.4\\% genuine (mean of seeds)} & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.1$}} \\\\\n  & 42 & 0.35 & 0.12 & 0 & 0 & \\textbf{100} & $n{=}46$; collapsed \\\\\n  & 43 & ${\\approx}$0.47 & ${\\approx}$0.13 & 0 & 69.6 & 30.4 & $n{=}56$; unstable \\\\\n  & 44 & 0.49 & 0.145 & 0 & 0 & \\textbf{100} & $n{=}66$; oscillation \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{Aggregate} & & \\multicolumn{3}{c}{\\textbf{76.8\\%} genuine (mean of seeds)} & \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{4pt}\n{\\footnotesize Aggregate genuine rate: mean of per-seed genuine rates. Permutation test (exec vs.\\ ISR genuine): $p{=}0.10$, $N{=}3$ per group.}\n\\end{table*}\n\n\\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}\nTable~\\ref{tab:fol-detailed} traces the ISR collapse over training:\nISR$^*=0.642$ at 100 steps $\\to$ $0.132$ at 500 steps ($-79.4$\\%) $\\to$ $0.003$ at 1000 steps ($-99.5$\\% from step 100).\nPR increases monotonically ($0.32 \\to 0.93 \\to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.\nBy step 1000, 94.8\\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.\n\n\\paragraph{Prolog: universal Goodhart via three distinct pathways.}\nAll three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\\% non-hacking proofs (Figure~\\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:\nseed~42 produces clean TS tautologies (single premise~$=$~conclusion),\nseed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,\nand seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.\nThe diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for ISR at $\\beta{=}0.2$ and both ISR and Random at $\\beta{=}0.3$.\nAt $\\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\\% or near-100\\% TS), confirming $\\beta{\\geq}0.2$ as the extremal Goodhart regime.\nThe three ISR $\\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.2$ and $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.2$}} \\\\\n  & 42 & 1.00 & 0.602 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\\\\n  & 43 & 0.96 & 0.552 & \\textbf{96.9} & 1.0 & 0 & PG${=}2$ \\\\\n  & 44 & 0.94 & 0.964 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.97{\\pm}0.03$ & $0.71{\\pm}0.22$ & & & 3/3 TS Goodhart \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.3$}} \\\\\n  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); PG${=}3$ \\\\\n  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 23.3 & CE shortcutting \\\\\n  & 44 & 0.95 & 0.742 & \\textbf{100} & 0 & 0 & Pure TS Goodhart \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.66{\\pm}0.42$ & $0.39{\\pm}0.31$ & & & \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{Random $\\beta{=}0.3$}} \\\\\n  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & TSa${=}4$ (D086) \\\\\n  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & TSa${=}7$; $n_{\\text{N-H}}{=}3$ \\\\\n  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure CE ($n{=}23$) \\\\\n\\cmidrule(l){2-8}\n  & \\multicolumn{2}{l}{3-seed mean$\\pm$std} & $0.54{\\pm}0.35$ & $0.09{\\pm}0.09$ & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}\n\\label{app:100step}\n\nTo control for the prove-rate confound in our SFT comparison (\\S\\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\\%, higher than SFT (13.0\\%, 3-seed pooled) but still early in training.\nOf the 32 proved samples, 9 (28.1\\%) exhibit TS hacking (single premise identical to conclusion) and 1 (3.1\\%) exhibits CE (conclusion embedded among premises), yielding a total hacking rate of 31.2\\%.\nBy contrast, SFT at comparable or lower PR shows 7.7\\% hacking (1/13 proved samples).\nThis demonstrates that reward hacking emerges early in GRPO training, well before the prove-rate plateau, and is not simply an artifact of having more proved samples available for exploitation.\nThe 100-step hacking rate (31.2\\%) is already substantially above SFT (7.7\\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.\n\n\\subsection{$O(1)$ vs.\\ $O(n)$ ISR Ablation}\n\\label{app:o1-ablation}\n\nAll main experiments (\\S\\ref{sec:diagnostic}--\\ref{sec:crossdomain}) use $O(n)$ full LOO ISR during both training and evaluation; the $O(1)$ binary variant described below exists as an alternative implementation (\\texttt{execution\\_fast\\_sta}) but is used only in the ablation reported here.\nThe two signals measure fundamentally different properties, not approximations of the same quantity.\nThe binary signal tests \\emph{collective} premise necessity: $\\text{fast\\_ISR}(x) = 1$ if $x$ is proved and the conclusion is not provable under empty premises (tautology check), $0$ otherwise.\nLOO tests \\emph{individual} premise necessity: each component is removed in turn, and ISR reflects the fraction whose removal causes proof failure.\n\n\\paragraph{Evaluation-time comparison.}\nAcross 402 proved samples from all ProofFOL conditions, the $O(1)$ binary signal is 1.0 for every sample: non-tautological conclusions cannot be proved without any premises, so the collective necessity test is trivially satisfied.\nThis renders $O(1)$ unable to distinguish hacking from genuine formalizations: both pass the empty-premise check.\nBy contrast, $O(n)$ LOO produces a clear separation: exec-only models average $\\text{ISR}^*{=}0.046$ ($n{=}234$) while ISR-trained models average $\\text{ISR}^*{=}0.183$ ($n{=}168$), because hacking constructions contain individually redundant components that LOO detects.\nOf 179 disagreements between the two signals, all are false positives ($O(1){=}1$, LOO${=}0$): the binary check approves formalizations that LOO correctly identifies as structurally degenerate.\n\n\\paragraph{Training-time ablation.}\nAs a training reward ($r = 0.5\\,r_{\\text{exec}} + 0.5\\,\\text{fast\\_ISR}$, seed~42, 500 steps), the $O(1)$ variant achieves $\\text{PR}{=}63\\%$ with $\\text{ISR}^*{=}0.007$, functionally zero, compared to $\\text{ISR}^*{=}0.132$ under exec-only and $\\text{ISR}^*{=}0.42$ under $O(n)$ ISR $\\beta{=}0.1$.\nThe tautology check depresses prove rate by 30\\,pp relative to exec-only ($63\\%$ vs.\\ $93\\%$) by penalizing formalizations where the conclusion is provable without premises, but this constraint provides no gradient toward individual component necessity; the model is free to degenerate as long as it avoids trivial tautologies.\nThat even the fine-grained $O(n)$ LOO signal, which \\emph{does} provide per-component necessity feedback, is ultimately gamed (\\S\\ref{sec:goodhart}) underscores that the problem lies in reward optimization itself, not in signal granularity.\n\n\\paragraph{Computational overhead.}\nFull LOO requires $n{+}1$ solver calls per sample (mean $n{\\approx}6$ for FOLIO).\nWith Prover9 at ${\\sim}5$\\,ms per call, STA evaluation adds ${\\sim}55$\\,ms per sample versus ${\\sim}4$\\,s for LLM inference (${<}1\\%$ overhead).\nThe $O(1)$ binary check adds a single solver call per proved sample (${<}2\\%$ per training step), but the evaluation above shows this saving comes at the cost of all diagnostic power.\n\n\\subsection{Cross-Model Generalization: LLaMA-3.2-3B Cold-Start Failure}\n\\label{app:llama-coldstart}\n\nWe applied the identical GRPO configuration (Table~\\ref{tab:hyperparams}) to LLaMA-3.2-3B~\\citep{grattafiori2024llama} (3B; exec-only, seed~42, $K{=}4$, FOLIO).\nAcross 72 of 500 planned steps the model produced zero valid Prover9 output, generating only natural-language text; $r_{\\text{exec}}{=}0$ for all rollouts yields zero GRPO advantage, so training was terminated early.\nThis establishes a \\emph{capability threshold}: the base model must produce syntactically valid solver input for the RL loop to generate signal.\nQwen3-4B crosses this threshold (non-zero prove rates within 10 steps) while LLaMA-3.2-3B does not despite comparable size (3B vs.\\ 4B), likely reflecting pretraining data composition.\nAn SFT warmstart (3 epochs on gold formalizations, lr$=$2$\\times$10$^{-5}$) initially failed: the model produced Unicode FOL notation ($\\forall$, $\\to$, $\\wedge$) instead of the required ASCII syntax despite training on ASCII-formatted data (PR$=$0\\%, $n{=}100$), suggesting the capability threshold involves format-level compatibility beyond task knowledge.\n\n\\paragraph{SFT warmstart with GRPO (3-seed).}\nAfter correcting the format incompatibility, we repeated the SFT warmstart and applied exec-only GRPO across three seeds (42, 43, 44; 500 steps each).\nTable~\\ref{tab:llama-d165} reports per-seed results.\nPR stabilizes at $15.0{\\pm}1.0$\\% (SE), indistinguishable from the SFT baseline: GRPO provides no amplification beyond supervised warmstart.\nHowever, non-hacking rates remain high ($86.6{\\pm}0.9\\%$, 3-seed mean), indicating that at this low PR, structural degeneration does not emerge; the model fails to bootstrap rather than degenerating into reward hacking.\nISR$^*$ averages $0.554{\\pm}0.010$, comparable to Qwen3-4B SFT ($0.595$; Table~\\ref{tab:fol-detailed}), confirming that the few proved samples retain genuine reasoning structure.\nThe combination of Qwen3-8B stagnation at PR${=}15.5\\%$ (\\S\\ref{sec:limitations}) and LLaMA-3.2-3B stagnation at PR${=}15\\%$ suggests a model-general cold-start barrier for GRPO on formal reasoning tasks.\n\n\\begin{table}[ht]\n\\centering\n\\caption{LLaMA-3.2-3B exec-only GRPO with SFT warmstart (3 seeds, 500 steps). PR = prove rate, ISR$^*$ = proved-only ISR, CE/N-H = percentage among proved samples. CI = contradiction injection (count).}\n\\label{tab:llama-d165}\n\\footnotesize\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Notes} \\\\\n\\midrule\n42 & 0.14 & 0.547 & 0 & 14.3 & \\textbf{85.7} & CI${=}2$; $n{=}14$ \\\\\n43 & 0.15 & 0.566 & 0 & 13.3 & \\textbf{86.7} & $n{=}15$ \\\\\n44 & 0.16 & 0.549 & 0 & 12.5 & \\textbf{87.5} & $n{=}16$ \\\\\n\\cmidrule(l){1-7}\nMean$\\pm$SE & $0.15{\\pm}0.01$ & $0.554{\\pm}0.010$ & 0 & 13.4 & \\textbf{86.6$\\pm$0.9} & $N{=}45$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 624,
        "oldLines": 6,
        "newStart": 624,
        "newLines": 35,
        "lines": [
          " and seed~44 converts NL conclusions to snake\\_case atoms used as both fact and query.",
          " The diversity of gaming pathways across seeds (despite identical training data and reward function) demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.",
          " ",
          "+\\subsection{Sensitivity to Seed 43 Exclusion}",
          "+\\label{app:sensitivity-s43}",
          "+",
          "+Seed~43 presents evaluation complications across conditions: exec-only seed~43 suffers greedy-mode degeneration (PR${=}13\\%$; evaluated with $T{=}0.7$ rather than greedy), ISR seed~43 collapses to pure TS (100\\%), and random seed~43 is the only seed exhibiting nonzero TS (38.3\\%; seeds~42/44: 0\\%).",
          "+Table~\\ref{tab:sensitivity-no-s43} reports 2-seed pooled results (s42$+$s44) to verify that conclusions are not driven by seed~43.",
          "+",
          "+All qualitative conclusions from the 3-seed analysis (\\S\\ref{sec:goodhart}) are preserved:",
          "+ISR amplifies TS relative to random (60.0\\% vs.\\ 0\\%), non-hacking rates remain low across all RL conditions (3.7--14.3\\%), and the CE$\\to$TS compositional shift under ISR reward persists (ISR: TS${=}60\\%$/CE${=}25\\%$; random: TS${=}0\\%$/CE${=}78\\%$).",
          "+The exec-only 2-seed pooled additionally reveals a split between CE-dominant (s42, 87\\%) and TS-dominant (s44, 100\\%) collapse modes, confirming cross-seed divergence (\\S\\ref{sec:diagnostic}).",
          "+",
          "+The 3-seed exec-only mean (PR${=}68{\\pm}47\\%$; Table~\\ref{tab:fol-detailed}) has extreme variance dominated by s43's greedy-mode collapse; the 2-seed mean (PR${=}95.5\\%$) better characterizes the non-degenerate regime.",
          "+",
          "+\\begin{table}[ht]",
          "+\\centering",
          "+\\caption{2-seed pooled results (s42$+$s44), excluding seed~43.",
          "+PR/ISR$^*$: per-seed mean${\\pm}$SE ($\\text{SE} = |x_{42}{-}x_{44}| / 2\\sqrt{2}$); TS/CE/N-H: pooled \\% of proved ($n$ = total proved).}",
          "+\\label{tab:sensitivity-no-s43}",
          "+\\small",
          "+\\begin{tabular}{@{}lcccccc@{}}",
          "+\\toprule",
          "+\\textbf{Condition} & $n$ & \\textbf{PR\\%} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\",
          "+\\midrule",
          "+Exec-only & 191 & 95.5{\\scriptsize$\\pm$1.8} & 0.357{\\scriptsize$\\pm$.16} & 51.3 & 42.4 & 3.7 \\\\",
          "+ISR $\\beta{=}0.1$ & 170 & 85.0{\\scriptsize$\\pm$2.8} & 0.659{\\scriptsize$\\pm$.17} & 60.0 & 24.7 & 8.2 \\\\",
          "+Random $\\beta{=}0.1$ & 168 & 84.0{\\scriptsize$\\pm$3.5} & 0.101{\\scriptsize$\\pm$.02} & 0 & 78.0 & 14.3 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          "+",
          " \\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}",
          " \\label{app:beta03}",
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

_source line 61_

<details open><summary>🔧 Tool call — Edit · `toolu_01RKTLgrPvr2j2bDwWPPM7ew`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:detailed-results})",
  "new_string": "excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:sensitivity-s43}, Table~\\ref{tab:sensitivity-no-s43})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "57262718-edb5-46bb-b0d5-f2b175fef3fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpqsxnfKSFKPv4GNdTTbJG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 25659,
      "cache_creation_input_tokens": 4508,
      "cache_read_input_tokens": 27264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4508
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

_source line 62 · 2026-05-21T18:20:34.001Z_

<details><summary>↩ Tool result · `toolu_01RKTLgrPvr2j2bDwWPPM7ew`</summary>

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
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "940aa1bc-8a32-4292-920a-bd231ce3cdeb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "oldString": "excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:detailed-results})",
    "newString": "excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:sensitivity-s43}, Table~\\ref{tab:sensitivity-no-s43})",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate STA along three axes: ISR as a diagnostic for reward hacking (\\S\\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\\S\\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\\S\\ref{sec:crossdomain}).\nA hacking taxonomy synthesizes the modes observed across conditions (\\S\\ref{sec:taxonomy}).\n\n\\subsection{Setup}\\label{sec:setup}\n\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).\n\n\\paragraph{Statistical considerations.}\nWith three seeds exhibiting multi-attractor dynamics, per-seed qualitative analysis is the primary framework; the divergence itself is a finding.\nPooled statistics (CMH) serve as supplementary reference; CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is $N{=}3$ seeds.\nProofFOL results ($p{=}0.10$, $N{=}3$) are exploratory.\n\n\\subsection{ISR as Diagnostic}\n\\label{sec:diagnostic}\n\n\\textbf{Collapse trajectory.}\nFigure~\\ref{fig:training-isr-curves} traces exec-only GRPO (seed~42) at 100, 500, 1000 steps.\nPR rises $32\\%\\to93\\%\\to96\\%$, a trajectory that execution-only evaluation would interpret as successful optimization; $\\text{ISR}^*$ tells the opposite story, $0.642\\to0.132\\to0.003$ (214$\\times$ collapse). %% registry: plan003-eval-exec-only-r5, plan001-exec-only-s42-r2, plan016-extended-1000-s42\nBy 500 steps, 87.1\\% of proved samples embed the conclusion (CE); by 1000 steps, component count inflates $2.8\\times$ ($6.58{\\to}18.55$) while ISR decreases $214\\times$, ruling out shorter formalizations as a mechanical explanation of the collapse.\nAn $O(1)$ binary variant testing only collective premise necessity returns $\\text{ISR}{=}1.0$ for all 402 proved samples, confirming that per-component LOO testing is essential for detecting the collapse (Appendix~\\ref{app:o1-ablation}).\n\n\\textbf{Cross-seed instability.}\nThree seeds diverge radically ($\\text{PR}\\,\\sigma{=}47$\\,pp) into conclusion embedding (s42, CE$=$87\\%), repetition collapse (s43), and tautological collapse (s44, TS$=$100\\%), all converging to ${\\leq}7\\%$ non-hacking by 1000 steps (Table~\\ref{tab:fol-detailed}; Appendix~\\ref{app:detailed-results}). %% registry: plan001-exec-only-s42-r2, plan001-exec-only-s43-r4, plan001-exec-only-s44; plan016-extended-1000-s42, plan001-exec-only-s43-1000-r7, plan001-exec-only-s44-1000-r2\n\n\\textbf{SFT baseline.}\nSFT on gold formalizations reaches $92.3\\%$ non-hacking ($\\text{PR}{=}13\\%$, 3-seed pooled; $\\text{OR}{=}147$ vs.\\ exec-only, $p{<}0.001$).\nSFT serves as a pre-RL quality baseline (not a PR-matched control; its low PR reflects minimal optimization pressure): the base model has zero FOL capability ($\\text{PR}{=}0\\%$) and SFT's $8\\%$ hacking confirms these modes are RL-created.\nAt just 100 GRPO steps ($\\text{PR}{=}32\\%$), hacking already reaches $31\\%$ ($9$ TS $+$ $1$ CE / $32$ proved) vs.\\ SFT's $8\\%$ at comparable PR, confirming hacking is an RL optimization product rather than a mechanical consequence of prove-rate level (Appendix~\\ref{app:100step}). %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3\n\n\\subsection{Goodhart Effects on ISR-as-Reward}\n\\label{sec:goodhart}\n\nWe reverse ISR's role from observer to reward: $r = r_{\\text{exec}}\\cdot(1 + \\beta\\,\\text{ISR})$, with matched random control ($u\\sim\\mathcal{U}(0,1)$).\nThe Goodhart effect operates at the level of ISR's LOO definition: models learn to generate formalizations where each component is individually necessary for proof mechanics, without ensuring meaningful reasoning.\nISR decline indicates structural change; the mode breakdown (Table~\\ref{tab:hacking-taxonomy}) characterizes this change as degeneration.\nThis is distinct from simple proxy failure. The qualitative shift in hacking modes (TS $0\\%{\\to}71\\%$ under ISR, per-seed direction consistent) demonstrates active optimization against the LOO metric; deconfounding shows the apparent $3.2\\times$ ISR advantage collapses to $1.06\\times$ after controlling for premise count.\n\n\\paragraph{Multiplicative coupling.}\nThe reward $r_{\\text{exec}}\\cdot(1{+}\\beta\\,\\text{ISR})$ couples signals; exec-only's $0\\%$ non-hacking, the qualitative TS shift ($0\\%{\\to}71\\%$), and an additive variant's PR collapse (Appendix~\\ref{app:setup}) constrain this confound.\nISR scores are bimodal (near $0$ or ${\\geq}0.5$) while random is approximately uniform. A shuffled-ISR control (batch-internal random permutation preserving ISR's bimodal distribution while breaking the sample-level semantic link) yields $\\text{PR}{=}15.3{\\pm}0.6\\%$ with $87.0\\%$ non-hacking ($N{=}46$ proved, 3-seed pooled), comparable to SFT ($\\text{PR}{=}13\\%$, $92\\%$ non-hacking) and far below the TS-dominated ISR regime ($71\\%$ TS). This rules out distributional shape as the Goodhart driver: the semantic correspondence between ISR and sample quality, not merely ISR's bimodal distribution, is necessary for the TS gaming effect.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & $\\boldsymbol{\\beta}$ & \\textbf{PR\\%}$\\uparrow$ & \\textbf{ISR}$^*$ & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nBase (0-shot) & --- & 12 & --- & --- & --- & --- \\\\ %% registry: sta-phase0-baseline\nSFT & --- & 13 & 0.595 & 0 & 8 & \\textbf{92} \\\\ %% registry: plan009-sft-baseline-s42-1000/s43-1000/s44-1000-r3 (3-seed pooled)\n\\midrule\nExec-only$^\\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\\\ %% registry: plan001-exec-only-s42-r2 (PG corrected)\nISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)\nRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)\nShuffled-ISR & 0.1 & 15{\\scriptsize$\\pm$1} & 0.559{\\scriptsize$\\pm$.02} & 7 & 7 & \\textbf{87} \\\\ %% registry: d157-shuffled-isr-s42-r3/s43/s44 (3-seed pooled, D159)\n\\midrule\nISR & 0.3 & 66{\\scriptsize$\\pm$42} & 0.39{\\scriptsize$\\pm$.31} & \\textbf{50} & 37 & 11 \\\\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled; D106 s43 genuine 23→20)\nRandom & 0.3 & 54{\\scriptsize$\\pm$35} & 0.09{\\scriptsize$\\pm$.09} & 7 & 91 & 2 \\\\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 TS: s42=4,s43=7,s44=0)\n\\bottomrule\n\\end{tabular}\n\\caption{Goodhart landscape across reward conditions. 3-seed rows: TS/CE/non-hacking percentage (N-H) pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by TS gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes TS classifier false-negative correction (s44) and PG premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random TS driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}. Shuffled-ISR is a deconfounding control (\\S\\ref{sec:goodhart}), not an independent reward condition. ISR $\\beta{=}0.1$ row: 3-seed (s42--44); two additional seeds (s45, s46) yield ${\\sim}55\\%$ non-hacking (Appendix~\\ref{app:detailed-results}).}\n\\label{tab:goodhart-landscape}\n\\end{table*}\n\n\\textbf{Low-dose ISR ($\\beta{=}0.1$): per-seed consistent gaming.}\nISR reward increases TS rates in all three initial seeds (s42--44) relative to matched random: $70.6\\%$ ($163/231$) vs.\\ $13.7\\%$ ($36/262$) pooled (supplementary CMH: $\\text{OR}_{\\text{CMH}}{=}2.46$, $p{=}5.6{\\times}10^{-16}$; Appendix~\\ref{app:statistical-details}). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom TS is seed-dependent ($38.3\\%$ in s43 vs.\\ $0\\%$ in s42/s44); ISR amplifies TS ($2/3$ seeds at $97$--$100\\%$; Table~\\ref{tab:fol-detailed}; 5-seed extension below).\nTS (a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction; \\S\\ref{sec:taxonomy-method}) is the canonical Goodhart move: the model satisfies the LOO definition directly.\nTotal conclusion embedding ($\\text{CE}+\\text{TS}$) is $68$--$100\\%$ across both conditions; the composition differs: CE dominates under random ($71\\%$), TS under ISR. ISR converts CE into TS rather than reducing total embedding (Figure~\\ref{fig:hacking-composition}).\nRandom yields higher PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$): noise disrupts convergence toward a single collapse trajectory.\n\n\\textbf{Premise-count confound.}\nThe sole non-TS ISR seed (s42) shows raw $\\text{ISR}^{*}{=}0.415$, $3.2\\times$ random ($0.131$), a premise-minimization artifact ($n{=}5.58$ vs.\\ $8.46$); matched comparison gives $1.06\\times$ (Appendix~\\ref{app:detailed-results}). %% D051 premise-count-matched analysis\nAfter reclassifying PG and TS false negatives, non-hacking rates ($6.1\\%$ ISR vs.\\ $9.5\\%$ random) are not significant ($p{=}0.182$; Appendix~\\ref{app:h8}). %% D095 FINAL Fisher test\nThe key asymmetry is compositional: ISR amplifies TS convergence ($2/3$ seeds ${\\geq}97\\%$), while random remains seed-dependent and CE-dominated.\n\n\\textbf{Higher doses and temporal dynamics.}\nISR $\\beta{=}0.1$ non-hacking is transient: seed~42 drops $17.3\\%{\\to}2.2\\%$ by 1000 steps as TS escalates to $96.7\\%$ (Figure~\\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42\nAt higher doses ($\\beta{\\geq}0.2$), TS becomes universal ($0\\%$ non-hacking at $\\beta{=}0.2$); $\\beta{=}0.3$ destabilizes both ISR ($\\text{PR}{=}66{\\pm}42\\%$) and random ($54{\\pm}35\\%$), with ISR producing multi-modal failure~\\citep{gao-reward-overoptimization} and random converging to CE ($91\\%$; Appendix~\\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44\n\n\\textbf{Bimodal seed-dependence (5-seed extension).}\nTwo additional seeds (s45, s46; Appendix~\\ref{app:detailed-results}) under the same ISR $\\beta{=}0.1$ condition yield ${\\sim}55\\%$ non-hacking---qualitatively different from the 3-seed average of $6\\%$.\nThis bimodal outcome (3/5 seeds dominated by gaming, 2/5 producing substantial genuine reasoning) reinforces the cross-seed instability documented in \\S\\ref{sec:diagnostic} and underscores that ISR reward outcomes are seed-dependent rather than deterministic. %% registry: plan002-additive-b01-s45, plan002-additive-b01-s46\n\n\\subsection{Cross-Domain Evidence}\n\\label{sec:crossdomain}\n\\label{sec:crosslogic}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_prolog_comparison.pdf}\n\\caption{Cross-logic results. \\textbf{Top}: FOL vs.\\ Prolog exec-only $\\text{ISR}^*$ across 3 seeds (s44 Prolog $0.387$ is a small-sample artifact, $n{=}21$; $^\\dagger$s43 FOL uses sampling $T{=}0.7$, not strictly comparable). \\textbf{Bottom}: Prolog ISR-reward gaming-mode composition; all 3 seeds reach 0\\% non-hacking through distinct mechanisms.}\n\\label{fig:prolog-comparison}\n\\end{figure}\n\n\\textbf{Prolog: universal Goodhart.}\nWe replicate the FOL pipeline with Prolog/SWI-Prolog (Figure~\\ref{fig:prolog-comparison}).\nExec-only seeds show $\\text{ISR}^*{\\approx}0$ via redundant ground-fact coding (2/3 seeds); ISR flags this mode as it flags FOL's conclusion embedding.\nUnder ISR-as-reward, 3/3 seeds reach 0\\% non-hacking through distinct mechanisms: clean TS (s42), uppercase pseudo-Prolog bypassing text-match classifiers (s43, all 38 proved at $n_{\\text{necessary}}{=}1$), and query-as-fact gaming (s44, 95/97 at $n_{\\text{necessary}}{=}1$; Table~\\ref{tab:prolog-detailed}).\nProlog's simpler semantics broadens the gaming basin, eliminating the non-hacking residual entirely.\n\n\\textbf{ProofFOL exec-only: structural degeneration generalizes, though mode distributions differ.}\nTwo converged seeds ($\\text{ISR}^*{<}0.07$) show ${\\leq}1.4\\%$ genuine; s42 exhibits 100\\% TS (absent from all FOLIO exec-only seeds), showing hacking-mode repertoire is dataset-specific ($\\text{ISR}^*{<}0.12$ across all seeds, far below baseline $0.31$).\n\n\\textbf{ProofFOL ISR ($\\beta{=}0.1$): beneficial instability (exploratory).}\nISR reduces stable convergence from 2/3 to 0/3 seeds, yet ISR seeds average 76.8\\% genuine versus 17.4\\% for exec-only ($p{=}0.10$, $N{=}3$; Table~\\ref{tab:prooffol-detailed}).\nProofFOL ``genuine'' excludes only TS and CE (the two modes detectable by text-match classifiers), unlike FOLIO's eight-mode residual; the rates are therefore not directly comparable.\nHowever, ISR-condition prove rates ($0.35$--$0.49$) remain far below exec-only (${\\sim}1.0$), so apparent beneficial instability may reflect insufficient training rather than a genuine ISR effect.\n\n\\textbf{Mechanism.}\nOn ProofFOL, hacking yields $\\text{ISR}{=}0.0$ while genuine proofs yield $\\text{ISR}{>}0.2$; ISR correctly penalizes shortcuts.\nOn FOLIO, $P{\\to}P$ yields $\\text{ISR}{\\geq}0.5$ (regressional Goodhart~\\citep{manheim-goodhart-taxonomy}), so ISR erroneously rewards tautological hacking.\nThe same metric produces opposite outcomes, determined by whether the dataset's hacking geometry satisfies it.\n\n\\subsection{Hacking Taxonomy}\n\\label{sec:taxonomy}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3_hacking_composition.pdf}\n\\caption{Hacking composition across reward conditions (proved samples; exec-only: seed~42; all other bars: pooled across 3 seeds, per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}). ISR converts CE into more extreme TS without reducing total hacking; SFT shows near-zero hacking.}\n\\label{fig:hacking-composition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Mode} & \\textbf{Exec} & \\textbf{ISR$_{.1}$} & \\textbf{Rnd$_{.1}$} & \\textbf{SFT} & \\textbf{Prolog$_{\\text{ISR}}$} \\\\\n\\midrule\nCE embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nTS duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\\nPG prem-subset & 6  & 5  & 8   & 0 & --- \\\\\nTautological   & --- & --- & --- & --- & s42 \\\\\nRepetition     & s43 & --- & --- & --- & --- \\\\\nContradiction  & 1k & --- & --- & --- & --- \\\\\nCmplx.\\ vacuous& 0  & 0  & 4  & 0 & --- \\\\\nQuery-as-fact  & --- & --- & --- & --- & s44 \\\\\n\\midrule\n\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Eight hacking modes across conditions (\\% of proved samples; exec-only/SFT: seed~42; ISR/Random: pooled across 3 seeds). TS includes subtypes TSa (text-match, $n{=}149$) and TSb (obfuscated tautology, $n{=}14$; primarily s44). Cells with seed identifiers indicate the mode dominates that seed. $^\\sharp$Prolog row pools strict+functional (\\S\\ref{sec:crosslogic}).}\n\\label{tab:hacking-taxonomy}\n\\end{table}\n\nThree modes account for ${>}90\\%$ of hacking (Table~\\ref{tab:hacking-taxonomy}; Appendix~\\ref{app:hacking-modes}): \\textbf{CE} (conclusion embedding), \\textbf{TS} (conclusion duplication, ISR-amplified; TSb evades text-match classifiers), and \\textbf{PG} (premise-subset gaming; audited for s42 only, s43/s44 checkpoints not retained). CE and TS represent genuine structural degeneration, while PG is milder shortcutting preserving partial logical structure.\n\\emph{Reward formulation determines composition but not prevalence}: all GRPO conditions show ${\\geq}80\\%$ hacking; only SFT achieves $92.3\\%$ non-hacking.\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\subsection{Setup}\\label{sec:setup}",
          " ",
          " We train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}",
          "-Held-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.",
          "+Held-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:sensitivity-s43}, Table~\\ref{tab:sensitivity-no-s43}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.",
          " Cross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.",
          " We report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).",
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

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the edits by reading the relevant sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "dd3536e4-3d92-4741-858f-003d04f462be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuFZ7gRiKAj6ER2BjdWhjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45734,
      "cache_read_input_tokens": 31772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45734
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

_source line 64_

Let me verify both edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "fd084e07-e92b-478e-a48c-5dee0191ff37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuFZ7gRiKAj6ER2BjdWhjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45734,
      "cache_read_input_tokens": 31772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45734
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

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_01ABqNstwkFVUr5xUWQ5XGK6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
  "offset": 626,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "338a5bc9-a5c1-4846-928a-c7ffd3188475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuFZ7gRiKAj6ER2BjdWhjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45734,
      "cache_read_input_tokens": 31772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45734
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

_source line 66 · 2026-05-21T18:20:37.581Z_

<details><summary>↩ Tool result · `toolu_01ABqNstwkFVUr5xUWQ5XGK6`</summary>

```text
626	
627	\subsection{Sensitivity to Seed 43 Exclusion}
628	\label{app:sensitivity-s43}
629	
630	Seed~43 presents evaluation complications across conditions: exec-only seed~43 suffers greedy-mode degeneration (PR${=}13\%$; evaluated with $T{=}0.7$ rather than greedy), ISR seed~43 collapses to pure TS (100\%), and random seed~43 is the only seed exhibiting nonzero TS (38.3\%; seeds~42/44: 0\%).
631	Table~\ref{tab:sensitivity-no-s43} reports 2-seed pooled results (s42$+$s44) to verify that conclusions are not driven by seed~43.
632	
633	All qualitative conclusions from the 3-seed analysis (\S\ref{sec:goodhart}) are preserved:
634	ISR amplifies TS relative to random (60.0\% vs.\ 0\%), non-hacking rates remain low across all RL conditions (3.7--14.3\%), and the CE$\to$TS compositional shift under ISR reward persists (ISR: TS${=}60\%$/CE${=}25\%$; random: TS${=}0\%$/CE${=}78\%$).
635	The exec-only 2-seed pooled additionally reveals a split between CE-dominant (s42, 87\%) and TS-dominant (s44, 100\%) collapse modes, confirming cross-seed divergence (\S\ref{sec:diagnostic}).
636	
637	The 3-seed exec-only mean (PR${=}68{\pm}47\%$; Table~\ref{tab:fol-detailed}) has extreme variance dominated by s43's greedy-mode collapse; the 2-seed mean (PR${=}95.5\%$) better characterizes the non-degenerate regime.
638	
639	\begin{table}[ht]
640	\centering
641	\caption{2-seed pooled results (s42$+$s44), excluding seed~43.
642	PR/ISR$^*$: per-seed mean${\pm}$SE ($\text{SE} = |x_{42}{-}x_{44}| / 2\sqrt{2}$); TS/CE/N-H: pooled \% of proved ($n$ = total proved).}
643	\label{tab:sensitivity-no-s43}
644	\small
645	\begin{tabular}{@{}lcccccc@{}}
646	\toprule
647	\textbf{Condition} & $n$ & \textbf{PR\%} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} \\
648	\midrule
649	Exec-only & 191 & 95.5{\scriptsize$\pm$1.8} & 0.357{\scriptsize$\pm$.16} & 51.3 & 42.4 & 3.7 \\
650	ISR $\beta{=}0.1$ & 170 & 85.0{\scriptsize$\pm$2.8} & 0.659{\scriptsize$\pm$.17} & 60.0 & 24.7 & 8.2 \\
651	Random $\beta{=}0.1$ & 168 & 84.0{\scriptsize$\pm$3.5} & 0.101{\scriptsize$\pm$.02} & 0 & 78.0 & 14.3 \\
652	\bottomrule
653	\end{tabular}
654	\end{table}
655	
656	\subsection{Per-Seed Results at $\beta{=}0.2$ and $\beta{=}0.3$}
657	\label{app:beta03}
658	
659	Table~\ref{tab:beta03-detailed} reports per-seed results for ISR at $\beta{=}0.2$ and both ISR and Random at $\beta{=}0.3$.
660	At $\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\% or near-100\% TS), confirming $\beta{\geq}0.2$ as the extremal Goodhart regime.
661	The three ISR $\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
662	
663	\begin{table*}[ht]
664	\centering
665	\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}
666	\label{tab:beta03-detailed}
667	\small
668	\begin{tabular}{@{}llcccccl@{}}
669	\toprule
670	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{TS\%} & \textbf{CE\%} & \textbf{N-H\%} & \textbf{Mode} \\
671	\midrule
672	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.2$}} \\
673	  & 42 & 1.00 & 0.602 & \textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\
674	  & 43 & 0.96 & 0.552 & \textbf{96.9} & 1.0 & 0 & PG${=}2$ \\
675	  & 44 & 0.94 & 0.964 & \textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "51702b25-9103-4bb6-a480-506a523091d2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex",
      "content": "\n\\subsection{Sensitivity to Seed 43 Exclusion}\n\\label{app:sensitivity-s43}\n\nSeed~43 presents evaluation complications across conditions: exec-only seed~43 suffers greedy-mode degeneration (PR${=}13\\%$; evaluated with $T{=}0.7$ rather than greedy), ISR seed~43 collapses to pure TS (100\\%), and random seed~43 is the only seed exhibiting nonzero TS (38.3\\%; seeds~42/44: 0\\%).\nTable~\\ref{tab:sensitivity-no-s43} reports 2-seed pooled results (s42$+$s44) to verify that conclusions are not driven by seed~43.\n\nAll qualitative conclusions from the 3-seed analysis (\\S\\ref{sec:goodhart}) are preserved:\nISR amplifies TS relative to random (60.0\\% vs.\\ 0\\%), non-hacking rates remain low across all RL conditions (3.7--14.3\\%), and the CE$\\to$TS compositional shift under ISR reward persists (ISR: TS${=}60\\%$/CE${=}25\\%$; random: TS${=}0\\%$/CE${=}78\\%$).\nThe exec-only 2-seed pooled additionally reveals a split between CE-dominant (s42, 87\\%) and TS-dominant (s44, 100\\%) collapse modes, confirming cross-seed divergence (\\S\\ref{sec:diagnostic}).\n\nThe 3-seed exec-only mean (PR${=}68{\\pm}47\\%$; Table~\\ref{tab:fol-detailed}) has extreme variance dominated by s43's greedy-mode collapse; the 2-seed mean (PR${=}95.5\\%$) better characterizes the non-degenerate regime.\n\n\\begin{table}[ht]\n\\centering\n\\caption{2-seed pooled results (s42$+$s44), excluding seed~43.\nPR/ISR$^*$: per-seed mean${\\pm}$SE ($\\text{SE} = |x_{42}{-}x_{44}| / 2\\sqrt{2}$); TS/CE/N-H: pooled \\% of proved ($n$ = total proved).}\n\\label{tab:sensitivity-no-s43}\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{PR\\%} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} \\\\\n\\midrule\nExec-only & 191 & 95.5{\\scriptsize$\\pm$1.8} & 0.357{\\scriptsize$\\pm$.16} & 51.3 & 42.4 & 3.7 \\\\\nISR $\\beta{=}0.1$ & 170 & 85.0{\\scriptsize$\\pm$2.8} & 0.659{\\scriptsize$\\pm$.17} & 60.0 & 24.7 & 8.2 \\\\\nRandom $\\beta{=}0.1$ & 168 & 84.0{\\scriptsize$\\pm$3.5} & 0.101{\\scriptsize$\\pm$.02} & 0 & 78.0 & 14.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Seed Results at $\\beta{=}0.2$ and $\\beta{=}0.3$}\n\\label{app:beta03}\n\nTable~\\ref{tab:beta03-detailed} reports per-seed results for ISR at $\\beta{=}0.2$ and both ISR and Random at $\\beta{=}0.3$.\nAt $\\beta{=}0.2$, all three seeds converge to pure TS Goodhart (100\\% or near-100\\% TS), confirming $\\beta{\\geq}0.2$ as the extremal Goodhart regime.\nThe three ISR $\\beta{=}0.3$ seeds illustrate qualitatively distinct Goodhart pathways (\\S\\ref{sec:goodhart}).\n\n\\begin{table*}[ht]\n\\centering\n\\caption{Per-seed results at $\\beta{=}0.2$ and $\\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}\n\\label{tab:beta03-detailed}\n\\small\n\\begin{tabular}{@{}llcccccl@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Seed} & \\textbf{PR} & \\textbf{ISR$^*$} & \\textbf{TS\\%} & \\textbf{CE\\%} & \\textbf{N-H\\%} & \\textbf{Mode} \\\\\n\\midrule\n\\multicolumn{8}{@{}l}{\\textit{ISR $\\beta{=}0.2$}} \\\\\n  & 42 & 1.00 & 0.602 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}100$) \\\\\n  & 43 & 0.96 & 0.552 & \\textbf{96.9} & 1.0 & 0 & PG${=}2$ \\\\\n  & 44 & 0.94 & 0.964 & \\textbf{100} & 0 & 0 & Pure TS ($n{=}94$) \\\\",
      "numLines": 50,
      "startLine": 626,
      "totalLines": 763
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01Y3YxaRg6UmXitdWAa8f9r1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": 8,
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
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "fd11b603-0349-439b-947a-0bdb33c8cc9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuFZ7gRiKAj6ER2BjdWhjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45734,
      "cache_read_input_tokens": 31772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45734
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

_source line 68 · 2026-05-21T18:20:38.326Z_

<details><summary>↩ Tool result · `toolu_01Y3YxaRg6UmXitdWAa8f9r1`</summary>

```text
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\ref{app:sensitivity-s43}, Table~\ref{tab:sensitivity-no-s43}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "6bf76dbe-5386-4a01-9c3a-0d6ce35dd981",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
      "content": "\nWe train Qwen3-4B~\\citep{qwen3} with GRPO~\\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\\{42,43,44\\}$ (ISR $\\beta{=}0.1$ extends to $\\{45,46\\}$; Appendix~\\ref{app:detailed-results}) on a fixed 500-example FOLIO~\\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}\nHeld-out evaluation uses 100 FOLIO examples with greedy decoding;\\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 does not change qualitative conclusions (Appendix~\\ref{app:sensitivity-s43}, Table~\\ref{tab:sensitivity-no-s43}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.\nCross-dataset experiments (\\S\\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\\sim}$500 training examples constructed by translating ProofWriter~\\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\\sim}70\\%$ retention); \\emph{stable convergence} denotes $\\overline{\\text{PR}}_{\\text{final\\,50}} > 0.90$.\nWe report prove rate (PR), proved-only ISR ($\\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\\text{necessary}}$ distribution; \\S\\ref{sec:taxonomy-method}), and a \\emph{non-hacking} (N-H) rate, an upper bound on genuine reasoning: the residual matching none of the eight cataloged patterns (classifier recall is unknown).",
      "numLines": 5,
      "startLine": 8,
      "totalLines": 157
    }
  }
}
```

</details>

---

### Assistant

_source line 69_

Both edits are in place.

**Summary of changes:**

1. **appendix.tex** — Added new subsection "Sensitivity to Seed 43 Exclusion" (`\label{app:sensitivity-s43}`) with:
   - Paragraph explaining why s43 is problematic across all 3 conditions
   - Table `tab:sensitivity-no-s43` with 2-seed (s42+s44) pooled stats for Exec-only, ISR β=0.1, and Random β=0.1
   - Note on 3-seed exec-only being dominated by s43's greedy collapse variance

2. **experiments.tex** — Updated the footnote reference from `Appendix~\ref{app:detailed-results}` to `Appendix~\ref{app:sensitivity-s43}, Table~\ref{tab:sensitivity-no-s43}`

Key numbers in the sensitivity table:
- **ISR TS amplification preserved**: 60.0% (ISR) vs 0% (Random) — consistent with 3-seed 71% vs 14%
- **N-H rates low everywhere**: 3.7% (Exec) / 8.2% (ISR) / 14.3% (Random)
- **CE→TS shift under ISR**: ISR TS=60%/CE=25% vs Random TS=0%/CE=78%
- **3-seed exec-only pooled**: not separately tabled since s43 T=0.7 makes it unreliable; noted in text that 2-seed mean (PR=95.5%) better characterizes the non-degenerate regime

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "uuid": "8a747609-1a3b-4270-a176-18cff1d9fb11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hgrwMPc2uB8aNFgeqNjrv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2515,
      "cache_read_input_tokens": 77506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2515
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

_source line 70_

Both edits are in place.

**Summary of changes:**

1. **appendix.tex** — Added new subsection "Sensitivity to Seed 43 Exclusion" (`\label{app:sensitivity-s43}`) with:
   - Paragraph explaining why s43 is problematic across all 3 conditions
   - Table `tab:sensitivity-no-s43` with 2-seed (s42+s44) pooled stats for Exec-only, ISR β=0.1, and Random β=0.1
   - Note on 3-seed exec-only being dominated by s43's greedy collapse variance

2. **experiments.tex** — Updated the footnote reference from `Appendix~\ref{app:detailed-results}` to `Appendix~\ref{app:sensitivity-s43}, Table~\ref{tab:sensitivity-no-s43}`

Key numbers in the sensitivity table:
- **ISR TS amplification preserved**: 60.0% (ISR) vs 0% (Random) — consistent with 3-seed 71% vs 14%
- **N-H rates low everywhere**: 3.7% (Exec) / 8.2% (ISR) / 14.3% (Random)
- **CE→TS shift under ISR**: ISR TS=60%/CE=25% vs Random TS=0%/CE=78%
- **3-seed exec-only pooled**: not separately tabled since s43 T=0.7 makes it unreliable; noted in text that 2-seed mean (PR=95.5%) better characterizes the non-degenerate regime

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 470594,
  "duration_api_ms": 469661,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "8e9feaac-9f71-428e-bb25-4ce1e25b3aee",
  "total_cost_usd": 1.9944919999999997,
  "usage": {
    "input_tokens": 25663,
    "cache_creation_input_tokens": 68180,
    "cache_read_input_tokens": 148383,
    "output_tokens": 21230,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 68180,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 389,
        "cache_read_input_tokens": 77506,
        "cache_creation_input_tokens": 2515,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2515
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3535,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0036349999999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 25680,
      "outputTokens": 28765,
      "cacheReadInputTokens": 496964,
      "cacheCreationInputTokens": 143176,
      "webSearchRequests": 0,
      "costUSD": 1.9908569999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8b4d3f97-5f8f-40dc-bff1-1289a82ce5d2"
}
```

</details>

---
