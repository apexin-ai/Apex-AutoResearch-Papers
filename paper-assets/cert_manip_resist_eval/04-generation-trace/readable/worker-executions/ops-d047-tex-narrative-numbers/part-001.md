# ops d047 tex narrative numbers — Part 1 of 8

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Worker execution logs

[Transcript overview](../ops-d047-tex-narrative-numbers.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/72/72d369930b5cacf7d9cc.json)

## Before a recorded user message

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
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
  "uuid": "171c902c-1b87-4168-a3d4-8b7f63b281c7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-cert-manip-resist-eval/memory/"
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
    "resetsAt": 1779760200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e940add1-59c1-400e-9222-b2adf5fa37e8",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
This is a large task involving updating numbers and narrative in a LaTeX paper. Let me break it down:

1. First, I need to read the data source JSON files to understand the new numbers
2. Read all the relevant .tex files
3. Make systematic replacements
4. Add narrative sections
5. Verify no old numbers remain

Let me start by reading the key files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "2bf33485-8c2e-404c-afba-b1b3085a536b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8wK3dg6UETDzmjAnrVbfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14371,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14371
      },
      "output_tokens": 18,
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

Let me start by reading the data sources and the tex files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "643e41cc-65d4-49c5-9e61-42a472077ec2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8wK3dg6UETDzmjAnrVbfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14371,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14371
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01NLFXotQE6TwiiMyqHLWqYM`</summary>

```json
{
  "description": "Read all tex files",
  "prompt": "Read the following files in full and report their complete contents (every line matters, include line numbers):\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex\n\nReport the full content of each file with line numbers.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "bb8dff6a-261a-4005-a442-fefb86b96f46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8wK3dg6UETDzmjAnrVbfF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14371,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14371
      },
      "output_tokens": 18,
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
  "task_id": "a1c7e1cbeef2d8b8a",
  "tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "description": "Read all tex files",
  "task_type": "local_agent",
  "prompt": "Read the following files in full and report their complete contents (every line matters, include line numbers):\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex\n\nReport the full content of each file with line numbers.",
  "uuid": "1176d191-38ce-46e6-afaa-2caea0960df1",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


## Round 1

## Round 1

17 recorded events


### User

_source line 8 · 2026-05-25T21:04:53.809Z_

Read the following files in full and report their complete contents (every line matters, include line numbers):

1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex

Report the full content of each file with line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "65e5d432-f174-4505-af86-70b597b7c4b2"
}
```

</details>

---


### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1c7e1cbeef2d8b8a",
  "tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "description": "Reading docs/paper/abstract.tex",
  "usage": {
    "total_tokens": 14745,
    "tool_uses": 1,
    "duration_ms": 6056
  },
  "last_tool_name": "Read",
  "uuid": "18038ee9-711c-4898-8f38-dac2215c1af1",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01FB6xNDsBXsC2RMSZndRCmy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "81bd5b5e-b810-4796-9847-bf5c6efb11f5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JEHptJwwXAYs6Ko4TDotW4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14740,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14740,
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

_source line 11 · 2026-05-25T21:04:59.878Z_

<details><summary>↩ Tool result · `toolu_01FB6xNDsBXsC2RMSZndRCmy`</summary>

```text
1	% Mirror of abstract in main.tex — do not edit here.
2	
3	Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\eta_{\max}$) and effective independence ($K_{\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\eta_{\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; confidence interval crosses zero at $K{\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\%$ at $\alpha{=}5\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "5f9a8ee8-3f7d-43a6-8f75-af1de649467e"
}
```

</details>

---


### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1c7e1cbeef2d8b8a",
  "tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 14746,
    "tool_uses": 2,
    "duration_ms": 6398
  },
  "last_tool_name": "Read",
  "uuid": "ff412896-4048-4ff2-be71-706c41085249",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_012dWL9BAzCuqbyYAbYLU71L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6f624408-56ae-4300-97d4-269ca5fb0781",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JEHptJwwXAYs6Ko4TDotW4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14740,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14740,
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

_source line 14 · 2026-05-25T21:05:00.215Z_

<details><summary>↩ Tool result · `toolu_012dWL9BAzCuqbyYAbYLU71L`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{tcolorbox}
16	\tcbuselibrary{breakable}
17	
18	\newtheorem{theorem}{Theorem}
19	\newtheorem{definition}{Definition}
20	\newtheorem{proposition}{Proposition}
21	
22	\title{The Diminishing Weakest Link: How Panel Size Shifts\\Adversarial Vulnerability Drivers in LLM Judge Panels}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\eta_{\max}$) and effective independence ($K_{\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\eta_{\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; confidence interval crosses zero at $K{\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\%$ at $\alpha{=}5\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\footnote{Code and data are available at \url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{threat_model}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{conclusion}
40	
41	\section*{Limitations}
42	
43	\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.
44	\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\geq}20$ threshold at all panel sizes \citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity show opposite $K$-trends).
45	\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \in \{3,5,7\}$; the predictor shift threshold $K^*$ is not precisely identified.
46	\textbf{Aggregation scope.} We examine only majority vote, threshold, and Bayesian calibration as aggregation rules; more sophisticated strategies (e.g., weighted voting, learned aggregation, or iterative deliberation among judges) may alter the diversity--robustness relationship and are not explored here.
47	\textbf{Temporal snapshot.} All API model evaluations were collected during a fixed time window; providers may update model weights or safety filters without notice, potentially altering individual susceptibility profiles and panel-level robustness patterns.
48	
49	\bibliography{references}
50	
51	\input{appendix}
52	\input{appendix_attacks}
53	
54	\end{document}
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "7f359afb-7eb0-4635-a379-cb4f1ee73cf3"
}
```

</details>

---


### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a1c7e1cbeef2d8b8a",
  "tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 14747,
    "tool_uses": 3,
    "duration_ms": 6852
  },
  "last_tool_name": "Read",
  "uuid": "e5a84725-ce44-4693-ba84-945c5515297b",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_015i9cYob3HtzXzpUzcGeYoQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "3d5d1879-f064-4e78-a9d4-fc9e72421b30",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JEHptJwwXAYs6Ko4TDotW4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14740,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14740,
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

_source line 17 · 2026-05-25T21:05:00.669Z_

<details><summary>↩ Tool result · `toolu_015i9cYob3HtzXzpUzcGeYoQ`</summary>

```text
1	\section{Introduction}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=0.78\textwidth]{figures/fig_framework.pdf}
6	\caption{The diminishing weakest link in LLM judge panels. \textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\eta_{\max}$) dominates vulnerability ($\hat{\beta}_{\mathrm{std}}{=}0.264$). \textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \textbf{(c)}~In large panels ($K{\geq}5$), inter-judge diversity ($K_{\mathrm{eff}}$, $\hat{\beta}_{\mathrm{std}}{=}0.437$) drives vulnerability while $\eta_{\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}
7	\label{fig:framework}
8	\end{figure*}
9	
10	Multi-judge panels have become the dominant defense against bias and manipulation in Large Language Model (LLM) evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, an approach inspired by Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization reports that 7-model committees reduce attack success rates (ASR) from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation, yet this framing conflates two distinct sources of robustness: the quality of individual judges and the independence among them.
11	
12	The conflation matters because the BFT analogy breaks down in the LLM judge setting. BFT adversaries control faulty nodes from within; evaluation adversaries manipulate inputs from without, and shared pretraining corpora create correlated failure modes that violate the independence assumption underlying majority-vote guarantees \citep{schneier2000secrets}. No existing work disentangles diversity from individual robustness across panel sizes, so the relative contribution of each factor to observed ASR reductions remains unclear.
13	
14	We address this gap by decomposing panel vulnerability into two predictors (Figure~\ref{fig:framework}): weakest-link susceptibility ($\eta_{\max}$, the maximum individual attack success rate in a panel) and effective independent channels ($K_{\mathrm{eff}}$, an information-theoretic measure of judge independence). Controlled experiments across 15 models (9 API, 6 local quantized), $K \in \{3,5,7\}$, six attack types, and two multiple-choice benchmarks (Massive Multitask Language Understanding [MMLU] and the AI2 Reasoning Challenge [ARC]) reveal two robust patterns and one metric-sensitive observation.
15	
16	These findings yield three contributions:
17	\begin{enumerate}
18	\item \textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\mathrm{eff}}$ and $\kappa$-diversity \citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\% of conditions (\S\ref{sec:dominance}, \S\ref{sec:gam_taxonomy}).
19	\item \textbf{Diminishing weakest link.} $\eta_{\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\mathrm{eff}}$ significance increases ($4 \to 7 \to 8$/12) while $\kappa$-diversity decreases ($8 \to 7 \to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\S\ref{sec:cross_k}).
20	\item \textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\mathrm{eff}}$ (5+/1$-$) but $\eta_{\max}$ persists (9/12), so the defense is partial (\S\ref{sec:aggregation}, \S\ref{sec:analysis}).
21	\end{enumerate}
22	
23	All findings are associational; the diversity--capability confound ($r{=}0.70$--$0.81$; \S\ref{sec:analysis}) precludes causal claims.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "4471024c-c5a6-4092-8dd0-60dc5729d482"
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
  "task_id": "a1c7e1cbeef2d8b8a",
  "tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "description": "Reading docs/paper/conclusion.tex",
  "usage": {
    "total_tokens": 14748,
    "tool_uses": 4,
    "duration_ms": 6897
  },
  "last_tool_name": "Read",
  "uuid": "986f1096-0813-469e-9c78-fa9e20712f34",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01EZr9EbPo3sZJiewMithhwD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "21d23fe6-21c3-4f25-ab63-f290e65d26f3",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JEHptJwwXAYs6Ko4TDotW4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14740,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14740,
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

_source line 20 · 2026-05-25T21:05:00.715Z_

<details><summary>↩ Tool result · `toolu_01EZr9EbPo3sZJiewMithhwD`</summary>

```text
1	\section{Conclusion}
2	
3	The weakest link diminishes: $\eta_{\max}$'s predictive power declines monotonically (pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; CI crosses zero at $K{\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\geq}5$, $K_{\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\min \eta_{\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "17a2d6ad-9582-4888-a697-d1483e7157b3"
}
```

</details>

---


### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a1c7e1cbeef2d8b8a",
  "tool_use_id": "toolu_01NLFXotQE6TwiiMyqHLWqYM",
  "status": "completed",
  "output_file": "",
  "summary": "Read all tex files",
  "usage": {
    "total_tokens": 19512,
    "tool_uses": 4,
    "duration_ms": 66730
  },
  "uuid": "5c6b8772-2dd1-4121-8776-1a8ccdf7ac27",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool result

_source line 22 · 2026-05-25T21:06:00.544Z_

<details><summary>↩ Tool result · `toolu_01NLFXotQE6TwiiMyqHLWqYM`</summary>

````text
Here are the complete contents of all four files:

---

**1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex**

```
1	% Mirror of abstract in main.tex — do not edit here.
2	
3	Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\eta_{\max}$) and effective independence ($K_{\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\eta_{\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; confidence interval crosses zero at $K{\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\%$ at $\alpha{=}5\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational.
4	
```

---

**2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex**

```
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{tcolorbox}
16	\tcbuselibrary{breakable}
17	
18	\newtheorem{theorem}{Theorem}
19	\newtheorem{definition}{Definition}
20	\newtheorem{proposition}{Proposition}
21	
22	\title{The Diminishing Weakest Link: How Panel Size Shifts\\Adversarial Vulnerability Drivers in LLM Judge Panels}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\eta_{\max}$) and effective independence ($K_{\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\eta_{\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; confidence interval crosses zero at $K{\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\%$ at $\alpha{=}5\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\footnote{Code and data are available at \url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{threat_model}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{conclusion}
40	
41	\section*{Limitations}
42	
43	\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.
44	\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\geq}20$ threshold at all panel sizes \citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity show opposite $K$-trends).
45	\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \in \{3,5,7\}$; the predictor shift threshold $K^*$ is not precisely identified.
46	\textbf{Aggregation scope.} We examine only majority vote, threshold, and Bayesian calibration as aggregation rules; more sophisticated strategies (e.g., weighted voting, learned aggregation, or iterative deliberation among judges) may alter the diversity--robustness relationship and are not explored here.
47	\textbf{Temporal snapshot.} All API model evaluations were collected during a fixed time window; providers may update model weights or safety filters without notice, potentially altering individual susceptibility profiles and panel-level robustness patterns.
48	
49	\bibliography{references}
50	
51	\input{appendix}
52	\input{appendix_attacks}
53	
54	\end{document}
55	
```

---

**3. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex**

```
1	\section{Introduction}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=0.78\textwidth]{figures/fig_framework.pdf}
6	\caption{The diminishing weakest link in LLM judge panels. \textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\eta_{\max}$) dominates vulnerability ($\hat{\beta}_{\mathrm{std}}{=}0.264$). \textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \textbf{(c)}~In large panels ($K{\geq}5$), inter-judge diversity ($K_{\mathrm{eff}}$, $\hat{\beta}_{\mathrm{std}}{=}0.437$) drives vulnerability while $\eta_{\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}
7	\label{fig:framework}
8	\end{figure*}
9	
10	Multi-judge panels have become the dominant defense against bias and manipulation in Large Language Model (LLM) evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, an approach inspired by Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization reports that 7-model committees reduce attack success rates (ASR) from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation, yet this framing conflates two distinct sources of robustness: the quality of individual judges and the independence among them.
11	
12	The conflation matters because the BFT analogy breaks down in the LLM judge setting. BFT adversaries control faulty nodes from within; evaluation adversaries manipulate inputs from without, and shared pretraining corpora create correlated failure modes that violate the independence assumption underlying majority-vote guarantees \citep{schneier2000secrets}. No existing work disentangles diversity from individual robustness across panel sizes, so the relative contribution of each factor to observed ASR reductions remains unclear.
13	
14	We address this gap by decomposing panel vulnerability into two predictors (Figure~\ref{fig:framework}): weakest-link susceptibility ($\eta_{\max}$, the maximum individual attack success rate in a panel) and effective independent channels ($K_{\mathrm{eff}}$, an information-theoretic measure of judge independence). Controlled experiments across 15 models (9 API, 6 local quantized), $K \in \{3,5,7\}$, six attack types, and two multiple-choice benchmarks (Massive Multitask Language Understanding [MMLU] and the AI2 Reasoning Challenge [ARC]) reveal two robust patterns and one metric-sensitive observation.
15	
16	These findings yield three contributions:
17	\begin{enumerate}
18	\item \textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\mathrm{eff}}$ and $\kappa$-diversity \citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\% of conditions (\S\ref{sec:dominance}, \S\ref{sec:gam_taxonomy}).
19	\item \textbf{Diminishing weakest link.} $\eta_{\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\mathrm{eff}}$ significance increases ($4 \to 7 \to 8$/12) while $\kappa$-diversity decreases ($8 \to 7 \to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\S\ref{sec:cross_k}).
20	\item \textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\mathrm{eff}}$ (5+/1$-$) but $\eta_{\max}$ persists (9/12), so the defense is partial (\S\ref{sec:aggregation}, \S\ref{sec:analysis}).
21	\end{enumerate}
22	
23	All findings are associational; the diversity--capability confound ($r{=}0.70$--$0.81$; \S\ref{sec:analysis}) precludes causal claims.
24	
```

---

**4. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex**

```
1	\section{Conclusion}
2	
3	The weakest link diminishes: $\eta_{\max}$'s predictive power declines monotonically (pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; CI crosses zero at $K{\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\geq}5$, $K_{\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\min \eta_{\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.
4	
```

agentId: a1c7e1cbeef2d8b8a (use SendMessage with to: 'a1c7e1cbeef2d8b8a' to continue this agent)
&lt;usage>total_tokens: 23222
tool_uses: 4
duration_ms: 66734&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "fe02c3ff-54d8-4535-878f-3e8915e746f3",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following files in full and report their complete contents (every line matters, include line numbers):\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex\n\nReport the full content of each file with line numbers.",
    "agentId": "a1c7e1cbeef2d8b8a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the complete contents of all four files:\n\n---\n\n**1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex**\n\n```\n1\t% Mirror of abstract in main.tex — do not edit here.\n2\t\n3\tMulti-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational.\n4\t\n```\n\n---\n\n**2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex**\n\n```\n1\t\\documentclass[11pt]{article}\n2\t\\usepackage[review]{acl}\n3\t\\usepackage{times}\n4\t\\usepackage{latexsym}\n5\t\\usepackage[T1]{fontenc}\n6\t\\usepackage[utf8]{inputenc}\n7\t\\usepackage{microtype}\n8\t\\usepackage{inconsolata}\n9\t\\usepackage{graphicx}\n10\t\\usepackage{amsmath,amssymb,amsthm}\n11\t\\usepackage{booktabs}\n12\t\\usepackage{multirow}\n13\t\\usepackage{xcolor}\n14\t\\usepackage{subcaption}\n15\t\\usepackage{tcolorbox}\n16\t\\tcbuselibrary{breakable}\n17\t\n18\t\\newtheorem{theorem}{Theorem}\n19\t\\newtheorem{definition}{Definition}\n20\t\\newtheorem{proposition}{Proposition}\n21\t\n22\t\\title{The Diminishing Weakest Link: How Panel Size Shifts\\\\Adversarial Vulnerability Drivers in LLM Judge Panels}\n23\t\n24\t\\author{Anonymous}\n25\t\n26\t\\begin{document}\n27\t\\maketitle\n28\t\n29\t\\begin{abstract}\n30\tMulti-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.\n31\t\\end{abstract}\n32\t\n33\t\\input{introduction}\n34\t\\input{related_work}\n35\t\\input{threat_model}\n36\t\\input{methodology}\n37\t\\input{results}\n38\t\\input{analysis}\n39\t\\input{conclusion}\n40\t\n41\t\\section*{Limitations}\n42\t\n43\t\\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.\n44\t\\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\\geq}20$ threshold at all panel sizes \\citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\\mathrm{eff}}$ vs.\\ $\\kappa$-diversity show opposite $K$-trends).\n45\t\\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \\in \\{3,5,7\\}$; the predictor shift threshold $K^*$ is not precisely identified.\n46\t\\textbf{Aggregation scope.} We examine only majority vote, threshold, and Bayesian calibration as aggregation rules; more sophisticated strategies (e.g., weighted voting, learned aggregation, or iterative deliberation among judges) may alter the diversity--robustness relationship and are not explored here.\n47\t\\textbf{Temporal snapshot.} All API model evaluations were collected during a fixed time window; providers may update model weights or safety filters without notice, potentially altering individual susceptibility profiles and panel-level robustness patterns.\n48\t\n49\t\\bibliography{references}\n50\t\n51\t\\input{appendix}\n52\t\\input{appendix_attacks}\n53\t\n54\t\\end{document}\n55\t\n```\n\n---\n\n**3. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex**\n\n```\n1\t\\section{Introduction}\n2\t\n3\t\\begin{figure*}[t]\n4\t\\centering\n5\t\\includegraphics[width=0.78\\textwidth]{figures/fig_framework.pdf}\n6\t\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.264$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.437$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}\n7\t\\label{fig:framework}\n8\t\\end{figure*}\n9\t\n10\tMulti-judge panels have become the dominant defense against bias and manipulation in Large Language Model (LLM) evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, an approach inspired by Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization reports that 7-model committees reduce attack success rates (ASR) from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation, yet this framing conflates two distinct sources of robustness: the quality of individual judges and the independence among them.\n11\t\n12\tThe conflation matters because the BFT analogy breaks down in the LLM judge setting. BFT adversaries control faulty nodes from within; evaluation adversaries manipulate inputs from without, and shared pretraining corpora create correlated failure modes that violate the independence assumption underlying majority-vote guarantees \\citep{schneier2000secrets}. No existing work disentangles diversity from individual robustness across panel sizes, so the relative contribution of each factor to observed ASR reductions remains unclear.\n13\t\n14\tWe address this gap by decomposing panel vulnerability into two predictors (Figure~\\ref{fig:framework}): weakest-link susceptibility ($\\eta_{\\max}$, the maximum individual attack success rate in a panel) and effective independent channels ($K_{\\mathrm{eff}}$, an information-theoretic measure of judge independence). Controlled experiments across 15 models (9 API, 6 local quantized), $K \\in \\{3,5,7\\}$, six attack types, and two multiple-choice benchmarks (Massive Multitask Language Understanding [MMLU] and the AI2 Reasoning Challenge [ARC]) reveal two robust patterns and one metric-sensitive observation.\n15\t\n16\tThese findings yield three contributions:\n17\t\\begin{enumerate}\n18\t\\item \\textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity \\citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).\n19\t\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).\n20\t\\item \\textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12), so the defense is partial (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).\n21\t\\end{enumerate}\n22\t\n23\tAll findings are associational; the diversity--capability confound ($r{=}0.70$--$0.81$; \\S\\ref{sec:analysis}) precludes causal claims.\n24\t\n```\n\n---\n\n**4. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex**\n\n```\n1\t\\section{Conclusion}\n2\t\n3\tThe weakest link diminishes: $\\eta_{\\max}$'s predictive power declines monotonically (pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; CI crosses zero at $K{\\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\\geq}5$, $K_{\\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\\min \\eta_{\\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.\n4\t\n```"
      }
    ],
    "totalDurationMs": 66734,
    "totalTokens": 23222,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4765,
      "cache_read_input_tokens": 14740,
      "output_tokens": 3716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4765
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3716,
          "cache_read_input_tokens": 14740,
          "cache_creation_input_tokens": 4765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4765,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---


### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Agent · `toolu_01R4NK1WGATH2wgwi7F4NBjD`</summary>

```json
{
  "description": "Read results and analysis tex",
  "prompt": "Read the following files in full and report their complete contents with line numbers:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex\n\nReport every line with line numbers.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "87e701b8-cb2b-4d5c-bdcd-0091eb863da6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfwCGyWyZRcnjLipu57A29",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4204,
      "cache_read_input_tokens": 25818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4204
      },
      "output_tokens": 33,
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

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a8e29686edf3c5013",
  "tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "description": "Read results and analysis tex",
  "task_type": "local_agent",
  "prompt": "Read the following files in full and report their complete contents with line numbers:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex\n\nReport every line with line numbers.",
  "uuid": "cdc8eef2-4d9e-472d-9917-387543b6c0ca",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


## Round 2

## Round 2

5 recorded events


### User

_source line 25 · 2026-05-25T21:06:05.638Z_

Read the following files in full and report their complete contents with line numbers:

1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex

Report every line with line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "8154c5ae-5668-4a80-b8aa-d1e5fc2abf4a"
}
```

</details>

---


### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8e29686edf3c5013",
  "tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "description": "Reading docs/paper/results.tex",
  "usage": {
    "total_tokens": 14654,
    "tool_uses": 1,
    "duration_ms": 2402
  },
  "last_tool_name": "Read",
  "uuid": "96b04c79-0e7a-4c9a-9460-8073ca8863ac",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01R7HouNBNUYyYBsy3pUTWx3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "13bc4e8a-9e82-4a67-8394-ea7cff3ea907",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GKhWkQwm6Z8YzVYxnyzVpW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6534,
      "cache_read_input_tokens": 8115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6534,
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


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Agent · `toolu_014FuY2oYXt9UYscBQw8GY1L`</summary>

```json
{
  "description": "Read appendix tex",
  "prompt": "Read the following file in full and report its complete contents with line numbers:\n\n/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex\n\nThis file may be very long. Report ALL lines - do not truncate. If the file is too large to read at once, read it in chunks and concatenate. I need every line.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "e275eec5-b73f-4f33-9626-7e421f985152",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfwCGyWyZRcnjLipu57A29",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4204,
      "cache_read_input_tokens": 25818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4204
      },
      "output_tokens": 33,
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

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a9b457fcfc91425c5",
  "tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "description": "Read appendix tex",
  "task_type": "local_agent",
  "prompt": "Read the following file in full and report its complete contents with line numbers:\n\n/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex\n\nThis file may be very long. Report ALL lines - do not truncate. If the file is too large to read at once, read it in chunks and concatenate. I need every line.",
  "uuid": "1b080930-3487-449e-8aa5-a36ebae483c3",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


## Round 3

## Round 3

317 recorded events


### User

_source line 30 · 2026-05-25T21:06:08.046Z_

Read the following file in full and report its complete contents with line numbers:

/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex

This file may be very long. Report ALL lines - do not truncate. If the file is too large to read at once, read it in chunks and concatenate. I need every line.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "352a6cd0-4122-40bb-aa27-3932219053e7"
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
  "task_id": "a8e29686edf3c5013",
  "tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "description": "Reading docs/paper/analysis.tex",
  "usage": {
    "total_tokens": 14655,
    "tool_uses": 2,
    "duration_ms": 2789
  },
  "last_tool_name": "Read",
  "uuid": "0660c633-89d9-4031-b7ec-df44e5a0ba02",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool result

_source line 32 · 2026-05-25T21:06:08.056Z_

<details><summary>↩ Tool result · `toolu_01R7HouNBNUYyYBsy3pUTWx3`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_regime_transition.pdf}
7	\caption{Predictor shift across panel sizes. $\eta_{\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\alpha{=}0.05$.}
8	\label{fig:regime_transition}
9	\end{figure}
10	
11	\subsection{Weakest-Link Dominance at \texorpdfstring{$K{=}3$}{K=3}}
12	\label{sec:dominance}
13	
14	Table~\ref{tab:dominance} reports the log-log OLS regression (Equation~\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\ref{tab:models}).
15	
16	Under OLS, $K_{\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\eta_{\max}$ is significant in 10/12 (exceptions: MMLU $\times$ score manipulation and ARC $\times$ position bias), consistent with Proposition~\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\mathrm{eff}}$-dominant, and zero $\eta_{\max}$-dominant conditions. However, the $r = 0.70$ $K_{\mathrm{eff}}$--$\eta_{\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\ref{app:keff_dist}).
17	
18	Figure~\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\eta_{\max}$ 3/12, $K_{\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\mathrm{eff}}$ significance at $K{\geq}5$ (Appendix~\ref{app:crossed_re}).
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\begin{tabular}{lcc}
24	\toprule
25	\textbf{Method} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} \\
26	\midrule
27	OLS                    & 10/12 & 12/12 \\
28	Clustered SE           & 4/12  & 0/12  \\
29	Mixed effects          & 7/12  & 3/12  \\
30	Wild bootstrap         & 3/12  & 4/12  \\
31	Frac.\ logit (clust.)  & 7/12  & 9/12  \\
32	\bottomrule
33	\end{tabular}
34	\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}
35	\label{tab:method_comparison}
36	\end{table}
37	
38	Power analysis yields MDE $\beta_{\mathrm{std}} = 0.14$ at 80\% power (Appendix~\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.
39	
40	\subsection{The Diminishing Weakest Link Across Panel Sizes}
41	\label{sec:cross_k}
42	
43	The $K{=}3$ pattern is method-sensitive (Table~\ref{tab:method_comparison}), contrasting with $K{\geq}5$ where $K_{\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \in \{3, 5, 7\}$ with max-$p$ correction.
44	
45	Meta-analytic pooling \citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\eta_{\max}$'s pooled $\hat{\beta}_{\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\geq}5$. $K_{\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\%$; Appendix~\ref{app:meta_analytic_details}). Figure~\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\% CIs are in Figure~\ref{fig:forest_plot} (Appendix~\ref{app:effect_size_forest}). The $\eta_{\max}$ decline holds under both $K_{\mathrm{eff}}$ and $\kappa$-diversity.
46	
47	
48	\subsection{Random vs.\ Adaptive Fault Contrast}
49	\label{sec:rf_contrast}
50	
51	Random faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\mathrm{eff}}$ retains power (7/12). The positive $K_{\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \citep{goodfellow2015adversarial,kariyappa2019improving}.
52	
53	\subsection{Positive Direction Across Attack Types}
54	\label{sec:gam_taxonomy}
55	
56	GAM bootstrap confirms positive $K_{\mathrm{eff}}$ direction in all 12 conditions (88.9--100\% positive rate; Figure~\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).
57	
58	\subsection{Aggregation Rules and the Diversity Channel}
59	\label{sec:aggregation}
60	
61	Table~\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.
62	
63	\begin{table}[t]
64	\centering
65	\small
66	\begin{tabular}{lcccc}
67	\toprule
68	\textbf{Method} & \textbf{$\eta_{\max}$ sig} & \textbf{$K_{\mathrm{eff}}$ sig} & \textbf{$K_{\mathrm{eff}}$ $\beta$ dir.} & \textbf{$R^2$} \\
69	\midrule
70	Threshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\
71	Majority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\
72	Weighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\
73	Bayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\
74	\bottomrule
75	\end{tabular}
76	\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}
77	\label{tab:aggregation}
78	\end{table}
79	
80	
81	Predictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\mathrm{eff}}$ (5+/1$-$) but $\eta_{\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\ref{app:aggregation_k7}).
82	
83	\paragraph{Fractional Logit Robustness.}
84	Fractional logit \citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\% directional concordance with OLS (71/72; Appendix~\ref{app:robustness_checks}).
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6bba3357-496d-4433-9f2e-626500de4985"
}
```

</details>

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01XrMb7WGCDgWCFXNJrecU82`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "d35272f0-eefd-4873-bba3-40ee5d84bc5a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GKhWkQwm6Z8YzVYxnyzVpW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6534,
      "cache_read_input_tokens": 8115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6534,
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

_source line 34 · 2026-05-25T21:06:08.431Z_

<details><summary>↩ Tool result · `toolu_01XrMb7WGCDgWCFXNJrecU82`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{Diversity--Capability Confound.}
5	$K_{\mathrm{eff}}$ and $\eta_{\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\approx}2.0$--$2.9$; Figure~\ref{fig:keff_eta_scatter}, Appendix~\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \citep{cinelli2020making} shows the confound could account for the association in 69\% of conditions (Appendix~\ref{app:sensitivity}), though fractional logit confirms the positive association (9/12 at all $K$). Causal attribution requires capability-controlled designs (Appendices~\ref{app:sensitivity_poolA},~\ref{app:cross_benchmark}).
6	
7	\paragraph{API-Only vs.\ Full Pool.}
8	Restricting to 9 API models removes the AWQ confound but increases collinearity ($r{=}0.85$): $\eta_{\max}$ retains significance (8/12) while $K_{\mathrm{eff}}$ drops (2--3/12); the API-only pool lacks statistical power (MDE $> 0.9$; Appendices~\ref{app:quant_dummy},~\ref{app:random_subsample}).
9	
10	\paragraph{Aggregation and Deployment.}
11	Aggregation rules influence predictability but not $K_{\mathrm{eff}}$'s direction (Figure~\ref{fig:aggregation_heatmap}). Threshold voting yields the highest $R^2$ ($0.83$ at $K{=}3$), while Bayesian calibration nearly neutralizes panel composition effects ($R^2{\leq}0.17$ across all $K$). At $K{=}7$, Bayesian calibration fully neutralizes $K_{\mathrm{eff}}$ (0/12; Appendix~\ref{app:bayesian_entropy}). Robustness-first selection ($\min \eta_{\max}$) achieves lowest ASR in all 12 conditions (Appendix~\ref{app:panel_selection}), confirming that selecting judges by individual robustness dominates diversity-maximizing strategies regardless of panel size. Clean $K_{\mathrm{eff}}$ is stable under 4/6 attacks ($\rho{\geq}0.91$; Appendix~\ref{app:attacked_keff}), offering a deployable metric from clean-condition agreement alone.
12	
13	\paragraph{Metric Sensitivity of the Diversity Trajectory.}
14	The diversity significance trajectory is operationalization-dependent: $K_{\mathrm{eff}}$ significance increases ($4 \to 7 \to 8$/12) while $\kappa$-diversity \citep{kuncheva2003measures} decreases ($8 \to 7 \to 6$/12; Appendix~\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \to 4 \to 0$; Appendix~\ref{app:shannon_entropy}). Both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\eta_{\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "add72d4a-9e96-42fb-a4a6-1f6f8c4f95c1"
}
```

</details>

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_011FymkcUnMvmZD4m4LZ5s5q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/_project/report/position_bias_fix_comparison.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "d427a3c8-f552-44c6-b8ba-6c26427d00be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfwCGyWyZRcnjLipu57A29",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4204,
      "cache_read_input_tokens": 25818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4204
      },
      "output_tokens": 33,
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

_source line 36 · 2026-05-25T21:06:08.978Z_

<details><summary>↩ Tool result · `toolu_011FymkcUnMvmZD4m4LZ5s5q`</summary>

```text
1	{
2	  "fix_description": "Removed erroneous _invert_winners() on position_bias in unified_data_loader.py (2 locations), run_fractional_logit_v2.py (1 location), gen_p3_figures.py (2 locations)",
3	  "affected_conditions": [
4	    "mmlu×position_bias",
5	    "arc_challenge×position_bias"
6	  ],
7	  "timestamp": "2026-05-26 04:56:16",
8	  "1_position_bias_asr_comparison": {
9	    "mmlu": {
10	      "qwen2.5-72b": {
11	        "old": 0.6633,
12	        "new": 0.37,
13	        "delta": -0.2933
14	      },
15	      "llama3.1-70b": {
16	        "old": 0.6,
17	        "new": 0.4067,
18	        "delta": -0.1933
19	      },
20	      "mistral-large": {
21	        "old": 0.54,
22	        "new": 0.4433,
23	        "delta": -0.0967
24	      },
25	      "qwen2.5-32b": {
26	        "old": 0.66,
27	        "new": 0.39,
28	        "delta": -0.27
29	      },
30	      "qwen2.5-14b": {
31	        "old": 0.7933,
32	        "new": 0.33,
33	        "delta": -0.4633
34	      },
35	      "llama3.1-8b": {
36	        "old": 0.66,
37	        "new": 0.3433,
38	        "delta": -0.3167
39	      },
40	      "claude-opus-4": {
41	        "old": 0.5467,
42	        "new": 0.46,
43	        "delta": -0.0867
44	      },
45	      "gpt-5.5": {
46	        "old": 0.52,
47	        "new": 0.5433,
48	        "delta": 0.0233
49	      },
50	      "gemini-2.5-pro": {
51	        "old": 0.5533,
52	        "new": 0.5233,
53	        "delta": -0.03
54	      },
55	      "gpt-4.1": {
56	        "old": 0.4733,
57	        "new": 0.4767,
58	        "delta": 0.0034
59	      },
60	      "claude-sonnet-4": {
61	        "old": 0.48,
62	        "new": 0.4733,
63	        "delta": -0.0067
64	      },
65	      "gpt-4o": {
66	        "old": 0.6167,
67	        "new": 0.3933,
68	        "delta": -0.2234
69	      },
70	      "gemini-2.5-flash": {
71	        "old": 0.6267,
72	        "new": 0.4633,
73	        "delta": -0.1634
74	      },
75	      "gpt-4o-mini": {
76	        "old": 0.5433,
77	        "new": 0.43,
78	        "delta": -0.1133
79	      },
80	      "claude-3-haiku": {
81	        "old": 0.6933,
82	        "new": 0.3633,
83	        "delta": -0.33
84	      }
85	    },
86	    "arc_challenge": {
87	      "qwen2.5-72b": {
88	        "old": 0.5967,
89	        "new": 0.44,
90	        "delta": -0.1567
91	      },
92	      "llama3.1-70b": {
93	        "old": 0.4967,
94	        "new": 0.5033,
95	        "delta": 0.0066
96	      },
97	      "mistral-large": {
98	        "old": 0.4933,
99	        "new": 0.51,
100	        "delta": 0.0167
101	      },
102	      "qwen2.5-32b": {
103	        "old": 0.56,
104	        "new": 0.4733,
105	        "delta": -0.0867
106	      },
107	      "qwen2.5-14b": {
108	        "old": 0.7767,
109	        "new": 0.3633,
110	        "delta": -0.4134
111	      },
112	      "llama3.1-8b": {
113	        "old": 0.7267,
114	        "new": 0.2733,
115	        "delta": -0.4534
116	      },
117	      "claude-opus-4": {
118	        "old": 0.4667,
119	        "new": 0.5267,
120	        "delta": 0.06
121	      },
122	      "gpt-5.5": {
123	        "old": 0.4733,
124	        "new": 0.5367,
125	        "delta": 0.0634
126	      },
127	      "gemini-2.5-pro": {
128	        "old": 0.4833,
129	        "new": 0.53,
130	        "delta": 0.0467
131	      },
132	      "gpt-4.1": {
133	        "old": 0.4733,
134	        "new": 0.52,
135	        "delta": 0.0467
136	      },
137	      "claude-sonnet-4": {
138	        "old": 0.4567,
139	        "new": 0.5267,
140	        "delta": 0.07
141	      },
142	      "gpt-4o": {
143	        "old": 0.5533,
144	        "new": 0.4533,
145	        "delta": -0.1
146	      },
147	      "gemini-2.5-flash": {
148	        "old": 0.52,
149	        "new": 0.5167,
150	        "delta": -0.0033
151	      },
152	      "gpt-4o-mini": {
153	        "old": 0.48,
154	        "new": 0.5167,
155	        "delta": 0.0367
156	      },
157	      "claude-3-haiku": {
158	        "old": 0.83,
159	        "new": 0.19,
160	        "delta": -0.64
161	      }
162	    }
163	  },
164	  "2_eta_max_pooled_beta_std_trajectory": {
165	    "old": [
166	      0.2638,
167	      0.102,
168	      0.0842
169	    ],
170	    "new": [
171	      0.24287730539642147,
172	      0.09056885779999115,
173	      0.08592105514278209
174	    ],
175	    "old_ci": [
176	      [
177	        0.1584,
178	        0.3691
179	      ],
180	      [
181	        -0.0549,
182	        0.2589
183	      ],
184	      [
185	        -0.0828,
186	        0.2513
187	      ]
188	    ],
189	    "new_ci": [
190	      [
191	        0.1629395490888122,
192	        0.32281506170403074
193	      ],
194	      [
195	        -0.030774534179114493,
196	        0.21191224977909678
197	      ],
198	      [
199	        -0.039371619812564235,
200	        0.2112137300981284
201	      ]
202	    ],
203	    "K_values": [
204	      3,
205	      5,
206	      7
207	    ]
208	  },
209	  "3_keff_pooled_beta_std_trajectory": {
210	    "old": [
211	      0.3559,
212	      0.4355,
213	      0.4005
214	    ],
215	    "new": [
216	      0.2857956955448854,
217	      0.35281902199201465,
218	      0.30875265366531957
219	    ],
220	    "old_ci": [
221	      [
222	        0.2669,
223	        0.445
224	      ],
225	      [
226	        0.3184,
227	        0.5526
228	      ],
229	      [
230	        0.2981,
231	        0.5029
232	      ]
233	    ],
234	    "new_ci": [
235	      [
236	        0.07275037202380549,
237	        0.49884101906596523
238	      ],
239	      [
240	        0.12452986484998552,
241	        0.5811081791340438
242	      ],
243	      [
244	        0.10025493300063315,
245	        0.517250374330006
246	      ]
247	    ]
248	  },
249	  "4_wcb_significance_counts": {
250	    "K3": {
251	      "keff_sig": "8/12",
252	      "eta_sig": "5/12"
253	    },
254	    "K5": {
255	      "keff_sig": "8/12",
256	      "eta_sig": "0/12"
257	    },
258	    "K7": {
259	      "keff_sig": "7/12",
260	      "eta_sig": "1/12"
261	    }
262	  },
263	  "5_fractional_logit_significance": {
264	    "K3": {
265	      "new_keff_sig": "10/12",
266	      "new_eta_sig": "8/12",
267	      "new_keff_all_positive": false,
268	      "old_keff_sig": "9/12",
269	      "old_eta_sig": "6/12",
270	      "old_all_pos": false
271	    },
272	    "K5": {
273	      "new_keff_sig": "11/12",
274	      "new_eta_sig": "8/12",
275	      "new_keff_all_positive": false,
276	      "old_keff_sig": "9/12",
277	      "old_eta_sig": "3/12",
278	      "old_all_pos": false
279	    },
280	    "K7": {
281	      "new_keff_sig": "11/12",
282	      "new_eta_sig": "6/12",
283	      "new_keff_all_positive": false,
284	      "old_keff_sig": "9/12",
285	      "old_eta_sig": "4/12",
286	      "old_all_pos": false
287	    }
288	  },
289	  "6_core_claim_verification": {
290	    "eta_CI_crosses_zero_at_K_ge_5": true,
291	    "eta_CI_details": {
292	      "K3": {
293	        "pooled": 0.24287730539642147,
294	        "ci_lo": 0.1629395490888122,
295	        "ci_hi": 0.32281506170403074,
296	        "crosses_zero": false
297	      },
298	      "K5": {
299	        "pooled": 0.09056885779999115,
300	        "ci_lo": -0.030774534179114493,
301	        "ci_hi": 0.21191224977909678,
302	        "crosses_zero": true
303	      },
304	      "K7": {
305	        "pooled": 0.08592105514278209,
306	        "ci_lo": -0.039371619812564235,
307	        "ci_hi": 0.2112137300981284,
308	        "crosses_zero": true
309	      }
310	    },
311	    "diversity_uniformly_positive_12_of_12": {
312	      "K3": false,
313	      "K5": false,
314	      "K7": false
315	    },
316	    "eta_diminishes_monotonically": true
317	  },
318	  "7_r2_summary": {
319	    "K3": {
320	      "mean_r2": 0.3468659326204886
321	    },
322	    "K5": {
323	      "mean_r2": 0.28055403665578127
324	    },
325	    "K7": {
326	      "mean_r2": 0.23350007535832276
327	    }
328	  }
329	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "c3dd79bc-cf37-41e6-a61d-6ee304e4047d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/_project/report/position_bias_fix_comparison.json",
      "content": "{\n  \"fix_description\": \"Removed erroneous _invert_winners() on position_bias in unified_data_loader.py (2 locations), run_fractional_logit_v2.py (1 location), gen_p3_figures.py (2 locations)\",\n  \"affected_conditions\": [\n    \"mmlu×position_bias\",\n    \"arc_challenge×position_bias\"\n  ],\n  \"timestamp\": \"2026-05-26 04:56:16\",\n  \"1_position_bias_asr_comparison\": {\n    \"mmlu\": {\n      \"qwen2.5-72b\": {\n        \"old\": 0.6633,\n        \"new\": 0.37,\n        \"delta\": -0.2933\n      },\n      \"llama3.1-70b\": {\n        \"old\": 0.6,\n        \"new\": 0.4067,\n        \"delta\": -0.1933\n      },\n      \"mistral-large\": {\n        \"old\": 0.54,\n        \"new\": 0.4433,\n        \"delta\": -0.0967\n      },\n      \"qwen2.5-32b\": {\n        \"old\": 0.66,\n        \"new\": 0.39,\n        \"delta\": -0.27\n      },\n      \"qwen2.5-14b\": {\n        \"old\": 0.7933,\n        \"new\": 0.33,\n        \"delta\": -0.4633\n      },\n      \"llama3.1-8b\": {\n        \"old\": 0.66,\n        \"new\": 0.3433,\n        \"delta\": -0.3167\n      },\n      \"claude-opus-4\": {\n        \"old\": 0.5467,\n        \"new\": 0.46,\n        \"delta\": -0.0867\n      },\n      \"gpt-5.5\": {\n        \"old\": 0.52,\n        \"new\": 0.5433,\n        \"delta\": 0.0233\n      },\n      \"gemini-2.5-pro\": {\n        \"old\": 0.5533,\n        \"new\": 0.5233,\n        \"delta\": -0.03\n      },\n      \"gpt-4.1\": {\n        \"old\": 0.4733,\n        \"new\": 0.4767,\n        \"delta\": 0.0034\n      },\n      \"claude-sonnet-4\": {\n        \"old\": 0.48,\n        \"new\": 0.4733,\n        \"delta\": -0.0067\n      },\n      \"gpt-4o\": {\n        \"old\": 0.6167,\n        \"new\": 0.3933,\n        \"delta\": -0.2234\n      },\n      \"gemini-2.5-flash\": {\n        \"old\": 0.6267,\n        \"new\": 0.4633,\n        \"delta\": -0.1634\n      },\n      \"gpt-4o-mini\": {\n        \"old\": 0.5433,\n        \"new\": 0.43,\n        \"delta\": -0.1133\n      },\n      \"claude-3-haiku\": {\n        \"old\": 0.6933,\n        \"new\": 0.3633,\n        \"delta\": -0.33\n      }\n    },\n    \"arc_challenge\": {\n      \"qwen2.5-72b\": {\n        \"old\": 0.5967,\n        \"new\": 0.44,\n        \"delta\": -0.1567\n      },\n      \"llama3.1-70b\": {\n        \"old\": 0.4967,\n        \"new\": 0.5033,\n        \"delta\": 0.0066\n      },\n      \"mistral-large\": {\n        \"old\": 0.4933,\n        \"new\": 0.51,\n        \"delta\": 0.0167\n      },\n      \"qwen2.5-32b\": {\n        \"old\": 0.56,\n        \"new\": 0.4733,\n        \"delta\": -0.0867\n      },\n      \"qwen2.5-14b\": {\n        \"old\": 0.7767,\n        \"new\": 0.3633,\n        \"delta\": -0.4134\n      },\n      \"llama3.1-8b\": {\n        \"old\": 0.7267,\n        \"new\": 0.2733,\n        \"delta\": -0.4534\n      },\n      \"claude-opus-4\": {\n        \"old\": 0.4667,\n        \"new\": 0.5267,\n        \"delta\": 0.06\n      },\n      \"gpt-5.5\": {\n        \"old\": 0.4733,\n        \"new\": 0.5367,\n        \"delta\": 0.0634\n      },\n      \"gemini-2.5-pro\": {\n        \"old\": 0.4833,\n        \"new\": 0.53,\n        \"delta\": 0.0467\n      },\n      \"gpt-4.1\": {\n        \"old\": 0.4733,\n        \"new\": 0.52,\n        \"delta\": 0.0467\n      },\n      \"claude-sonnet-4\": {\n        \"old\": 0.4567,\n        \"new\": 0.5267,\n        \"delta\": 0.07\n      },\n      \"gpt-4o\": {\n        \"old\": 0.5533,\n        \"new\": 0.4533,\n        \"delta\": -0.1\n      },\n      \"gemini-2.5-flash\": {\n        \"old\": 0.52,\n        \"new\": 0.5167,\n        \"delta\": -0.0033\n      },\n      \"gpt-4o-mini\": {\n        \"old\": 0.48,\n        \"new\": 0.5167,\n        \"delta\": 0.0367\n      },\n      \"claude-3-haiku\": {\n        \"old\": 0.83,\n        \"new\": 0.19,\n        \"delta\": -0.64\n      }\n    }\n  },\n  \"2_eta_max_pooled_beta_std_trajectory\": {\n    \"old\": [\n      0.2638,\n      0.102,\n      0.0842\n    ],\n    \"new\": [\n      0.24287730539642147,\n      0.09056885779999115,\n      0.08592105514278209\n    ],\n    \"old_ci\": [\n      [\n        0.1584,\n        0.3691\n      ],\n      [\n        -0.0549,\n        0.2589\n      ],\n      [\n        -0.0828,\n        0.2513\n      ]\n    ],\n    \"new_ci\": [\n      [\n        0.1629395490888122,\n        0.32281506170403074\n      ],\n      [\n        -0.030774534179114493,\n        0.21191224977909678\n      ],\n      [\n        -0.039371619812564235,\n        0.2112137300981284\n      ]\n    ],\n    \"K_values\": [\n      3,\n      5,\n      7\n    ]\n  },\n  \"3_keff_pooled_beta_std_trajectory\": {\n    \"old\": [\n      0.3559,\n      0.4355,\n      0.4005\n    ],\n    \"new\": [\n      0.2857956955448854,\n      0.35281902199201465,\n      0.30875265366531957\n    ],\n    \"old_ci\": [\n      [\n        0.2669,\n        0.445\n      ],\n      [\n        0.3184,\n        0.5526\n      ],\n      [\n        0.2981,\n        0.5029\n      ]\n    ],\n    \"new_ci\": [\n      [\n        0.07275037202380549,\n        0.49884101906596523\n      ],\n      [\n        0.12452986484998552,\n        0.5811081791340438\n      ],\n      [\n        0.10025493300063315,\n        0.517250374330006\n      ]\n    ]\n  },\n  \"4_wcb_significance_counts\": {\n    \"K3\": {\n      \"keff_sig\": \"8/12\",\n      \"eta_sig\": \"5/12\"\n    },\n    \"K5\": {\n      \"keff_sig\": \"8/12\",\n      \"eta_sig\": \"0/12\"\n    },\n    \"K7\": {\n      \"keff_sig\": \"7/12\",\n      \"eta_sig\": \"1/12\"\n    }\n  },\n  \"5_fractional_logit_significance\": {\n    \"K3\": {\n      \"new_keff_sig\": \"10/12\",\n      \"new_eta_sig\": \"8/12\",\n      \"new_keff_all_positive\": false,\n      \"old_keff_sig\": \"9/12\",\n      \"old_eta_sig\": \"6/12\",\n      \"old_all_pos\": false\n    },\n    \"K5\": {\n      \"new_keff_sig\": \"11/12\",\n      \"new_eta_sig\": \"8/12\",\n      \"new_keff_all_positive\": false,\n      \"old_keff_sig\": \"9/12\",\n      \"old_eta_sig\": \"3/12\",\n      \"old_all_pos\": false\n    },\n    \"K7\": {\n      \"new_keff_sig\": \"11/12\",\n      \"new_eta_sig\": \"6/12\",\n      \"new_keff_all_positive\": false,\n      \"old_keff_sig\": \"9/12\",\n      \"old_eta_sig\": \"4/12\",\n      \"old_all_pos\": false\n    }\n  },\n  \"6_core_claim_verification\": {\n    \"eta_CI_crosses_zero_at_K_ge_5\": true,\n    \"eta_CI_details\": {\n      \"K3\": {\n        \"pooled\": 0.24287730539642147,\n        \"ci_lo\": 0.1629395490888122,\n        \"ci_hi\": 0.32281506170403074,\n        \"crosses_zero\": false\n      },\n      \"K5\": {\n        \"pooled\": 0.09056885779999115,\n        \"ci_lo\": -0.030774534179114493,\n        \"ci_hi\": 0.21191224977909678,\n        \"crosses_zero\": true\n      },\n      \"K7\": {\n        \"pooled\": 0.08592105514278209,\n        \"ci_lo\": -0.039371619812564235,\n        \"ci_hi\": 0.2112137300981284,\n        \"crosses_zero\": true\n      }\n    },\n    \"diversity_uniformly_positive_12_of_12\": {\n      \"K3\": false,\n      \"K5\": false,\n      \"K7\": false\n    },\n    \"eta_diminishes_monotonically\": true\n  },\n  \"7_r2_summary\": {\n    \"K3\": {\n      \"mean_r2\": 0.3468659326204886\n    },\n    \"K5\": {\n      \"mean_r2\": 0.28055403665578127\n    },\n    \"K7\": {\n      \"mean_r2\": 0.23350007535832276\n    }\n  }\n}",
      "numLines": 329,
      "startLine": 1,
      "totalLines": 329
    }
  }
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
  "task_id": "a9b457fcfc91425c5",
  "tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 14645,
    "tool_uses": 1,
    "duration_ms": 2712
  },
  "last_tool_name": "Read",
  "uuid": "56bda345-211d-4865-9311-cd3c7845173d",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01RBZhqQJvqfHkw3d7A3PYzG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "f61504fb-2d7e-423f-9d3b-f4c71625d395",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016tJKLBjFF2t8avh2kDr83X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6525,
      "cache_read_input_tokens": 8115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6525,
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

_source line 39 · 2026-05-25T21:06:11.053Z_

<details><summary>↩ Tool result · reported error · `toolu_01RBZhqQJvqfHkw3d7A3PYzG`</summary>

```text
File content (42517 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1b555c8d-e511-4f13-934d-6565e06a138e",
  "tool_use_result": "Error: File content (42517 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a9b457fcfc91425c5",
  "tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 15657,
    "tool_uses": 2,
    "duration_ms": 5942
  },
  "last_tool_name": "Read",
  "uuid": "ba52dd22-5c59-46f1-b92a-2458c2f3f3a9",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_016YSiQ3wWaLpKVPEJnk4m8a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 0,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "61a66e9f-eb44-4081-a8c4-b3664f9f78d6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RDRa6cTtpYDSb1znCzoyRe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 14640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1006,
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

_source line 42 · 2026-05-25T21:06:14.313Z_

<details><summary>↩ Tool result · `toolu_016YSiQ3wWaLpKVPEJnk4m8a`</summary>

```text
0	\appendix
1	
2	\section{Proof of Proposition~\ref{thm:monotonicity}}
3	\label{app:proof}
4	
5	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
6	\begin{align}
7	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
8	\end{align}
9	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
10	
11	\section{Robustness Correction Methods}
12	\label{app:robustness_methods}
13	
14	The 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.
15	
16	\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.
17	
18	\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effects model with a random intercept for the judge occupying that position, estimating $K_{\mathrm{eff}}$ and $\eta_{\max}$ as fixed effects. The reported $p$-value for each coefficient is the maximum across the three models.
19	
20	\paragraph{Wild Cluster Bootstrap.} We perform $B{=}9{,}999$ bootstrap resamples using Rademacher weights, clustering by each of the three panel positions in turn and taking the maximum $p$-value across positions (the most conservative aggregation). This approach avoids distributional assumptions on the cluster structure.
21	
22	\subsection{Bootstrap Convergence and Weight Diagnostics}
23	\label{app:bootstrap_convergence}
24	
25	Our primary wild cluster bootstrap uses $B{=}9{,}999$ Rademacher resamples. We assess convergence by comparing significance counts at $B \in \{999, 4{,}999, 9{,}999\}$ and contrasting Rademacher with Mammen two-point weights.
26	
27	\paragraph{$B$-Value Stability.} Table~\ref{tab:bootstrap_B} reports FDR-significant $K_{\mathrm{eff}}$ counts across bootstrap replications. Significance counts stabilize by $B{=}4{,}999$: the maximum discrepancy between $B{=}4{,}999$ and $B{=}9{,}999$ is $\pm 1$ condition across all three $K$ values, and the mean absolute $p$-value shift is ${<}0.003$. The $B{=}999$ configuration shows occasional instability (up to $\pm 2$ discrepancy at $K{=}5$), justifying our choice of $B{=}9{,}999$.
28	
29	\begin{table}[h]
30	\centering
31	\small
32	\begin{tabular}{rcccc}
33	\toprule
34	$\boldsymbol{K}$ & $\boldsymbol{B{=}999}$ & $\boldsymbol{B{=}4{,}999}$ & $\boldsymbol{B{=}9{,}999}$ & $\boldsymbol{\Delta_{999 \to 9999}}$ \\
35	\midrule
36	3 & 3/12 & 4/12 & 4/12 & $+1$ \\
37	5 & 5/12 & 7/12 & 7/12 & $+2$ \\
38	7 & 7/12 & 8/12 & 8/12 & $+1$ \\
39	\bottomrule
40	\end{tabular}
41	\caption{Bootstrap convergence: FDR-significant $K_{\mathrm{eff}}$ counts by number of resamples ($B$). Wild cluster bootstrap with Rademacher weights, max-$p$ across $K$ positions, BH FDR $\alpha{=}0.05$. Counts stabilize by $B{=}4{,}999$.}
42	\label{tab:bootstrap_B}
43	\end{table}
44	
45	\paragraph{Rademacher vs.\ Mammen Weights.} Rademacher weights assign $\pm 1$ with equal probability; Mammen two-point weights use $\{-(\sqrt{5}-1)/2, (\sqrt{5}+1)/2\}$ with asymmetric probabilities to preserve the third moment \citep{mackinnon2018wild}. In our setting, both weight distributions yield identical significance counts at all three $K$ values (4/12, 7/12, 8/12), with maximum $p$-value divergence of 0.008 across all 36 conditions. The Webb six-point distribution (used for the Shannon MI comparison in Appendix~\ref{app:shannon_entropy}) produces marginally different results at $K{=}3$ due to the low cluster count ($G{=}13$), where the discrete support of six-point weights interacts with the small number of sign permutations. All primary analyses use Rademacher weights for simplicity and comparability with the Monte Carlo calibration (Appendix~\ref{app:monte_carlo}).
46	
47	\paragraph{Max-$p$ vs.\ Alternative Aggregation.} We aggregate $p$-values across $K$ position-clusterings by taking the maximum (most conservative). Alternative aggregations---median $p$ and Bonferroni-corrected minimum $p$---produce slightly different significance counts. At $K{=}5$: max-$p$ yields 7/12, median yields 8/12, and Bonferroni-min yields 6/12. The max-$p$ approach is recommended for combinatorial designs where cluster membership is non-nested \citep{mackinnon2018wild}, since it guards against inflated significance from any single clustering being anti-conservative. All reported results use max-$p$.
48	
49	\section{Crossed Random Effects Analysis}
50	\label{app:crossed_re}
51	
52	The one-way clustering in Appendix~\ref{app:robustness_methods} treats each judge position independently, but panels exhibit \emph{crossed} random effects: judge $j$ may occupy position~1 in one panel and position~2 in another, inducing a multi-membership structure. At $K{=}7$, each judge appears in $\binom{14}{6} = 3{,}003$ of $6{,}435$ panels (46.7\%), making crossed membership the dominant source of residual correlation.
53	
54	We fit multi-membership cluster-robust variance estimators (CRVE) using a sandwich estimator with $t(G{-}1) = t(14)$ reference distribution, where $G{=}15$ is the number of judges. Table~\ref{tab:crossed_re} compares bootstrap and crossed RE significance.
55	
56	\begin{table}[h]
57	\centering
58	\small
59	\begin{tabular}{rcccc}
60	\toprule
61	& \multicolumn{2}{c}{\textbf{Bootstrap}} & \multicolumn{2}{c}{\textbf{Crossed RE (FDR)}} \\
62	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
63	$\boldsymbol{K}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & $\boldsymbol{\eta_{\max}}$ \\
64	\midrule
65	3 & 4/12 & 3/12 & 0/12 & 1/12 \\
66	5 & 7/12 & 2/12 & \textbf{8/12} & 3/12 \\
67	7 & 8/12 & 1/12 & \textbf{8/12} & 2/12 \\
68	\bottomrule
69	\end{tabular}
70	\caption{Crossed random effects vs.\ wild cluster bootstrap significance (BH FDR $\alpha{=}0.05$). Multi-membership CRVE with $t(14)$ distribution. At $K{\geq}5$, $K_{\mathrm{eff}}$ retains 8/12 significance under crossed RE, matching or exceeding bootstrap. At $K{=}3$, the conservative $t(14)$ distribution with only 455 panels produces attenuation to 0/12 (raw $p$-values: 5/12 significant).}
71	\label{tab:crossed_re}
72	\end{table}
73	
74	SE inflation increases with $K$ as judge overlap intensifies: $1.75$--$4.96{\times}$ at $K{=}3$, $6$--$12{\times}$ at $K{=}5$, $10$--$19{\times}$ at $K{=}7$. Despite this inflation, $K_{\mathrm{eff}}$ retains 8/12 significance at $K{\geq}5$ because the effect size is large enough to survive the correction. The $K{=}3$ attenuation (0/12) reflects two compounding factors: the conservative $t(14)$ reference distribution penalizes small-sample inference, and the effect sizes at $K{=}3$ are insufficient to overcome the inflated SEs. Raw (uncorrected) $p$-values show 5/12 conditions significant at $K{=}3$, confirming that the attenuation reflects degrees-of-freedom conservatism rather than absent effects.
75	
76	\section{Per-Condition Effect Size Forest Plot}
77	\label{app:effect_size_forest}
78	
79	\begin{figure*}[t]
80	\centering
81	\includegraphics[width=\textwidth]{figures/fig5_forest_plot.pdf}
82	\caption{Per-condition standardized $\hat{\beta}$ with 95\% CI for $\eta_{\max}$ (left) and $K_{\mathrm{eff}}$ (right) at $K{=}3$ (wild cluster bootstrap).}
83	\label{fig:forest_plot}
84	\end{figure*}
85	
86	\section{Extended Analysis}
87	\label{app:extended_analysis}
88	
89	\begin{figure}[t]
90	\centering
91	\includegraphics[width=\columnwidth]{figures/fig_keff_eta_scatter.pdf}
92	\caption{Panel-level correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ at $K{=}5$ ($n{=}3{,}003$ panels). Full model pool (gray, $r{=}0.81$) exhibits strong collinearity; capability-matched Pool~A (orange, $r{=}0.50$, 126 panels) shows reduced confounding.}
93	\label{fig:keff_eta_scatter}
94	\end{figure}
95	
96	\begin{figure}[t]
97	\centering
98	\includegraphics[width=\columnwidth]{figures/fig_dominance_heatmap.pdf}
99	\caption{Per-condition predictor dominance across panel sizes (wild cluster bootstrap, BH FDR $\alpha{=}0.05$). At $K{=}3$, dominance is heterogeneous (co-dominant, $K_{\mathrm{eff}}$-only, $\eta_{\max}$-only, and non-significant conditions coexist); at $K{\geq}5$, $K_{\mathrm{eff}}$ dominates uniformly while $\eta_{\max}$ diminishes substantially.}
100	\label{fig:dominance_heatmap}
101	\end{figure}
102	
103	\subsection{Per-Condition Regression Results}
104	\label{app:per_condition_regression}
105	
106	Tables~\ref{tab:percond_k3}--\ref{tab:percond_k7} report the full per-condition regression results underlying the significance counts in the main text. For each of 12 conditions (2 benchmarks $\times$ 6 attacks), we report the standardized OLS coefficients ($\hat{\beta}_{\mathrm{std}}$), $R^2$, and wild cluster bootstrap $p$-values (max-$p$ across $K$ position clusters, BH FDR $\alpha{=}0.05$).
107	
108	\begin{table*}[t]
109	\centering
110	\footnotesize
111	\setlength{\tabcolsep}{3pt}
112	\begin{tabular}{llccccccc}
113	\toprule
114	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
115	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
116	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
117	\midrule
118	\multirow{6}{*}{MMLU} & Prompt inj. & 0.252 & $1.6{\times}10^{-10}$ & 0.026 & 0.616 & $7.4{\times}10^{-46}$ & 0.003 & 0.663 \\
119	& Sycophancy & 0.166 & $1.2{\times}10^{-4}$ & 0.045 & 0.486 & $1.2{\times}10^{-26}$ & 0.012 & 0.334 \\
120	& Score manip. & 0.033 & 0.607 & 0.689 & 0.598 & $3.6{\times}10^{-19}$ & 0.005 & 0.390 \\
121	& Verbosity & 0.090 & 0.026 & 0.175 & 0.593 & $4.0{\times}10^{-40}$ & 0.001 & 0.407 \\
122	& Position & 0.104 & 0.057 & 0.117 & 0.418 & $1.1{\times}10^{-13}$ & 0.023 & 0.243 \\
123	& Authority & 0.010 & 0.852 & 0.864 & 0.377 & $3.4{\times}10^{-11}$ & 0.008 & 0.147 \\
124	\addlinespace
125	\multirow{6}{*}{ARC} & Prompt inj. & 0.330 & $6.4{\times}10^{-6}$ & 0.015 & 0.244 & $8.0{\times}10^{-4}$ & 0.092 & 0.303 \\
126	& Sycophancy & $-0.192$ & $6.3{\times}10^{-3}$ & 0.023 & 0.492 & $6.7{\times}10^{-12}$ & 0.001 & 0.132 \\
127	& Score manip. & 0.252 & 0.023 & 0.079 & 0.224 & 0.043 & 0.175 & 0.219 \\
128	& Verbosity & 0.146 & 0.051 & 0.112 & 0.343 & $5.0{\times}10^{-6}$ & 0.013 & 0.222 \\
129	& Position & 0.584 & $5.9{\times}10^{-9}$ & 0.004 & $-0.011$ & 0.909 & 0.917 & 0.329 \\
130	& Authority & 0.195 & $2.0{\times}10^{-3}$ & 0.031 & 0.261 & $3.6{\times}10^{-5}$ & 0.046 & 0.181 \\
131	\midrule
132	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{10/12} & \\
133	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{4/12} & \multicolumn{3}{c}{3/12} & \\
134	\bottomrule
135	\end{tabular}
136	\caption{Per-condition regression results at $K{=}3$ (455 panels, 15 models). $\hat{\beta}_{\mathrm{std}}$: standardized OLS coefficient. Boot $p$: wild cluster bootstrap max-$p$ (Rademacher, $B{=}9{,}999$). $R^2$: OLS model fit. FDR significance uses BH correction at $\alpha{=}0.05$. Two $K_{\mathrm{eff}}$ exceptions at $K{=}3$ (score manipulation and authority bias on MMLU) show near-zero coefficients ($\hat{\beta}_{\mathrm{std}}{<}0.04$), indicating that these attacks target individual judge capability rather than exploiting inter-judge independence.}
137	\label{tab:percond_k3}
138	\end{table*}
139	
140	\begin{table*}[t]
141	\centering
142	\footnotesize
143	\setlength{\tabcolsep}{3pt}
144	\begin{tabular}{llccccccc}
145	\toprule
146	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
147	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
148	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
149	\midrule
150	\multirow{6}{*}{MMLU} & Prompt inj. & 0.493 & ${<}10^{-15}$ & 0.002 & 0.370 & ${<}10^{-15}$ & 0.033 & 0.594 \\
151	& Sycophancy & 0.321 & ${<}10^{-15}$ & 0.010 & 0.349 & ${<}10^{-15}$ & 0.028 & 0.325 \\
152	& Score manip. & 0.506 & ${<}10^{-15}$ & 0.003 & 0.075 & 0.001 & 0.620 & 0.297 \\
153	& Verbosity & 0.235 & ${<}10^{-15}$ & 0.005 & 0.445 & ${<}10^{-15}$ & 0.005 & 0.358 \\
154	& Position & 0.149 & ${<}10^{-8}$ & 0.077 & 0.333 & ${<}10^{-15}$ & 0.063 & 0.182 \\
155	& Authority & 0.075 & $3.5{\times}10^{-3}$ & 0.314 & 0.203 & ${<}10^{-10}$ & 0.277 & 0.061 \\
156	\addlinespace
157	\multirow{6}{*}{ARC} & Prompt inj. & 0.583 & ${<}10^{-15}$ & 0.018 & $-0.038$ & 0.095 & 0.746 & 0.327 \\
158	& Sycophancy & $-0.157$ & ${<}10^{-8}$ & 0.172 & 0.374 & ${<}10^{-15}$ & 0.011 & 0.078 \\
159	& Score manip. & 0.443 & ${<}10^{-15}$ & 0.004 & $-0.026$ & 0.274 & 0.912 & 0.189 \\
160	& Verbosity & 0.215 & ${<}10^{-12}$ & 0.100 & 0.276 & ${<}10^{-15}$ & 0.058 & 0.178 \\
161	& Position & 0.881 & ${<}10^{-15}$ & 0.017 & $-0.348$ & ${<}10^{-15}$ & 0.796 & 0.512 \\
162	& Authority & 0.264 & ${<}10^{-15}$ & 0.151 & 0.146 & ${<}10^{-5}$ & 0.342 & 0.120 \\
163	\midrule
164	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{11/12} & \\
165	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{7/12} & \multicolumn{3}{c}{2/12} & \\
166	\bottomrule
167	\end{tabular}
168	\caption{Per-condition regression results at $K{=}5$ (3{,}003 panels, 15 models). Format identical to Table~\ref{tab:percond_k3}. $K_{\mathrm{eff}}$ achieves bootstrap significance in 7/12 conditions with consistently larger effect sizes than at $K{=}3$ (mean $|\hat{\beta}_{\mathrm{std}}|$: 0.361 vs.\ 0.196). $\eta_{\max}$'s bootstrap significance drops to 2/12, with three conditions showing negative coefficients---the predictor shift documented in \S\ref{sec:cross_k}.}
169	\label{tab:percond_k5}
170	\end{table*}
171	
172	\begin{table*}[t]
173	\centering
174	\footnotesize
175	\setlength{\tabcolsep}{3pt}
176	\begin{tabular}{llccccccc}
177	\toprule
178	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
179	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
180	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
181	\midrule
182	\multirow{6}{*}{MMLU} & Prompt inj. & 0.574 & ${<}10^{-15}$ & 0.002 & 0.288 & ${<}10^{-15}$ & 0.092 & 0.540 \\
183	& Sycophancy & 0.329 & ${<}10^{-15}$ & 0.017 & 0.266 & ${<}10^{-15}$ & 0.060 & 0.258 \\
184	& Score manip. & 0.605 & ${<}10^{-15}$ & 0.007 & $-0.081$ & ${<}10^{-3}$ & 0.581 & 0.333 \\
185	& Verbosity & 0.204 & ${<}10^{-15}$ & 0.006 & 0.435 & ${<}10^{-15}$ & 0.013 & 0.319 \\
186	& Position & 0.231 & ${<}10^{-15}$ & 0.071 & 0.279 & ${<}10^{-15}$ & 0.110 & 0.186 \\
187	& Authority & 0.005 & 0.722 & 0.905 & 0.116 & ${<}10^{-6}$ & 0.268 & 0.014 \\
188	\addlinespace
189	\multirow{6}{*}{ARC} & Prompt inj. & 0.611 & ${<}10^{-15}$ & 0.063 & $-0.091$ & ${<}10^{-4}$ & 0.237 & 0.337 \\
190	& Sycophancy & $-0.176$ & ${<}10^{-12}$ & 0.326 & 0.372 & ${<}10^{-15}$ & 0.016 & 0.064 \\
191	& Score manip. & 0.316 & ${<}10^{-15}$ & 0.009 & 0.052 & $1.7{\times}10^{-2}$ & 0.539 & 0.112 \\
192	& Verbosity & 0.253 & ${<}10^{-15}$ & 0.044 & 0.238 & ${<}10^{-15}$ & 0.024 & 0.176 \\
193	& Position & 0.831 & ${<}10^{-15}$ & 0.029 & $-0.327$ & ${<}10^{-15}$ & 0.468 & 0.523 \\
194	& Authority & 0.268 & ${<}10^{-15}$ & 0.231 & 0.074 & $2.3{\times}10^{-3}$ & 0.846 & 0.092 \\
195	\midrule
196	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{11/12} & \\
197	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{8/12} & \multicolumn{3}{c}{1/12} & \\
198	\bottomrule
199	\end{tabular}
200	\caption{Per-condition regression results at $K{=}7$ (6{,}435 panels, 15 models). Format identical to Table~\ref{tab:percond_k3}. $K_{\mathrm{eff}}$ bootstrap significance reaches 8/12 (vs.\ 4/12 at $K{=}3$), completing the predictor shift. $\eta_{\max}$ drops to 1/12 bootstrap significance, with its coefficient crossing zero in 3/12 conditions. ARC position bias shows the strongest $K_{\mathrm{eff}}$ coefficient ($\hat{\beta}_{\mathrm{std}}{=}0.831$) and the strongest negative $\eta_{\max}$ coefficient ($-0.327$), a pattern present across all three $K$ values.}
201	\label{tab:percond_k7}
202	\end{table*}
203	
204	\subsection{Model Capability and Vulnerability Profiles}
205	\label{app:model_profiles}
206	
207	\begin{figure}[h]
208	\centering
209	\includegraphics[width=\columnwidth]{figures/fig_model_radar.pdf}
210	\caption{Capability profiles of 15 judge models across MMLU and ARC benchmarks. API models cluster at higher accuracy, while local AWQ-quantized models show greater variance. Inter-model capability differences are benchmark-dependent, with some models showing MMLU--ARC divergence exceeding 15 percentage points.}
211	\label{fig:model_radar}
212	\end{figure}
213	
214	The capability landscape of the 15-judge pool (Figure~\ref{fig:model_radar}) shows pronounced API--local separation on MMLU (mean gap: 23~pp) but attenuated separation on ARC (mean gap: 11~pp), reflecting ARC's reasoning-focused format that partially equalizes capability differences across model families.
215	
216	\paragraph{Per-Model Vulnerability Summary.} Table~\ref{tab:per_model_asr_detail} reports individual judge ASR ($\eta_j$) across all attack types for the 9 API models with per-sample evaluation data. Attack susceptibility ($\eta_j$) is defined as the fraction of evaluation pairs where the judge's decision flips under attack relative to clean evaluation.
217	
218	\begin{table*}[t]
219	\centering
220	\footnotesize
221	\setlength{\tabcolsep}{2.5pt}
222	\begin{tabular}{llcccccc|c}
223	\toprule
224	\textbf{Model} & \textbf{Bench.} & \textbf{Prompt} & \textbf{Syco.} & \textbf{Score} & \textbf{Verb.} & \textbf{Pos.} & \textbf{Auth.} & $\bar{\eta}$ \\
225	\midrule
226	\multirow{2}{*}{Claude Opus 4} & MMLU & .019 & .019 & .011 & .007 & .019 & .026 & .017 \\
227	& ARC & .000 & .003 & .003 & .017 & .007 & .000 & .005 \\
228	\addlinespace
229	\multirow{2}{*}{GPT-5.5} & MMLU & .026 & .023 & .026 & .026 & .026 & .019 & .024 \\
230	& ARC & .003 & .010 & .003 & .000 & .003 & .000 & .003 \\
231	\addlinespace
232	\multirow{2}{*}{Gemini 3.1 Pro} & MMLU & .099 & .047 & .083 & .055 & .051 & .047 & .064 \\
233	& ARC & .010 & .014 & .021 & .024 & .021 & .017 & .018 \\
234	\addlinespace
235	\multirow{2}{*}{GPT-4.1} & MMLU & .016 & .000 & .012 & .016 & .032 & .024 & .017 \\
236	& ARC & .007 & .010 & .007 & .007 & .010 & .007 & .008 \\
237	\addlinespace
238	\multirow{2}{*}{Claude Sonnet 4} & MMLU & .041 & .025 & .053 & .025 & .029 & .041 & .036 \\
239	& ARC & .000 & .000 & .004 & .004 & .007 & .004 & .003 \\
240	\addlinespace
241	\multirow{2}{*}{GPT-4.1-nano} & MMLU & .279 & .116 & .158 & .137 & .174 & .068 & .155 \\
242	& ARC & .062 & .078 & .047 & .055 & .059 & .027 & .055 \\
243	\addlinespace
244	\multirow{2}{*}{Gemini 3.5 Flash} & MMLU & .112 & .079 & .042 & .065 & .070 & .061 & .072 \\
245	& ARC & .047 & .025 & .022 & .014 & .018 & .018 & .024 \\
246	\addlinespace
247	\multirow{2}{*}{GPT-4.1-mini} & MMLU & .025 & .025 & .017 & .013 & .113 & .013 & .034 \\
248	& ARC & .007 & .004 & .010 & .004 & .010 & .004 & .006 \\
249	\addlinespace
250	\multirow{2}{*}{Claude 3 Haiku} & MMLU & \textbf{.817} & .226 & .126 & .296 & .030 & .122 & .270 \\
251	& ARC & \textbf{.719} & .222 & .304 & .578 & .074 & .281 & .363 \\
252	\bottomrule
253	\end{tabular}
254	\caption{Per-model attack success rates ($\eta_j$) across 6 attack types and 2 benchmarks for 9 API models (single-judge evaluation, $n{=}300$ samples per condition). $\bar{\eta}$: mean ASR across attacks. Claude 3 Haiku is the most vulnerable model ($\bar{\eta}{=}0.270$ on MMLU, $0.363$ on ARC); Claude Opus 4 and GPT-5.5 are the most resistant ($\bar{\eta}{<}0.025$). Prompt injection produces the widest vulnerability range (0.000--0.817 on MMLU).}
255	\label{tab:per_model_asr_detail}
256	\end{table*}
257	
258	\paragraph{API vs.\ Local Model Vulnerability.} The 9 API models span a 16$\times$ vulnerability range ($\bar{\eta}$: 0.003--0.363 on ARC). The 6 locally-hosted AWQ-quantized models (Qwen2.5-72B/32B/14B, LLaMA3.1-70B/8B, Mistral-Large) were evaluated on the remote server under identical attack conditions; their aggregate vulnerability exceeds API models by approximately 2$\times$ on MMLU and 1.5$\times$ on ARC. The quantization dummy analysis (Appendix~\ref{app:quant_dummy}) confirms that part of $K_{\mathrm{eff}}$'s signal reflects this API--local capability gap rather than independence per se, though the effect attenuates after controlling for quantization status.
259	
260	\begin{figure*}[t]
261	\centering
262	\includegraphics[width=\textwidth]{figures/fig_per_model_asr.pdf}
263	\caption{Per-model attack success rates across 6 attack types and 2 benchmarks (single-judge evaluation, $K{=}1$). Models ordered by mean clean accuracy. Prompt injection achieves ASR ${>}0.8$ on weaker models but ${<}0.2$ on frontier APIs; position bias shows uniformly moderate ASR ($0.4$--$0.6$) regardless of capability.}
264	\label{fig:per_model_asr}
265	\end{figure*}
266	
267	Individual model vulnerabilities vary dramatically across the attack taxonomy (Figure~\ref{fig:per_model_asr}). Content-dependent attacks (prompt injection, sycophancy) exploit capability gaps, producing strong ASR--capability correlations ($r{>}0.7$). Structural attacks (position bias) show uniformly moderate ASR regardless of model capability, consistent with their mechanism operating on presentation order rather than response content.
268	
269	\begin{figure*}[t]
270	\centering
271	\includegraphics[width=\textwidth]{figures/fig_asr_distribution.pdf}
272	\caption{Panel ASR distributions across attack types and panel sizes ($K \in \{3, 5, 7\}$). Violin plots show the full distributional shape; white dots indicate medians. Median ASR decreases with $K$ for most attacks, but distributional spread remains substantial, confirming that panel composition matters beyond panel size alone.}
273	\label{fig:asr_distribution}
274	\end{figure*}
275	
276	The distributional analysis (Figure~\ref{fig:asr_distribution}) reveals that larger panels compress ASR variance without eliminating it: at $K{=}7$, the interquartile range remains 0.05--0.15 for most attacks. This residual variance is the signal that $K_{\mathrm{eff}}$ and $\eta_{\max}$ predict in the regression framework.
277	
278	\subsection{Pairwise Mutual Information Structure}
279	\label{app:mi_structure}
280	
281	\begin{figure*}[t]
282	\centering
283	\includegraphics[width=\textwidth]{figures/fig_mi_heatmap.pdf}
284	\caption{Pairwise mutual information matrix for 15 judge models on MMLU (upper triangle) and ARC (lower triangle). Within-family pairs (e.g., GPT-4.1 variants, Claude variants) show elevated MI, while cross-family pairs exhibit lower dependence. The block-diagonal structure motivates $K_{\mathrm{eff}}$ as a measure of effective panel independence.}
285	\label{fig:mi_heatmap}
286	\end{figure*}
287	
288	The MI heatmap (Figure~\ref{fig:mi_heatmap}) reveals structured dependence among LLM judges: within-family correlations are 2--3$\times$ higher than cross-family correlations on both benchmarks. This structured dependence explains why family-diverse panels achieve higher $K_{\mathrm{eff}}$ and connects the abstract diversity--capability confound ($r{=}0.70$--$0.81$) to concrete family-composition effects.
289	
290	\subsection{BFT Reversal Mechanism: Detailed Evidence}
291	\label{app:bft_reversal}
292	
293	Under standard OLS, the regression results (Table~\ref{tab:dominance}) show $\eta_{\max}$ significant in 10 of 12 conditions and $K_{\mathrm{eff}}$ positively associated with ASR in all 12. Non-independence correction attenuates both predictors: under wild cluster bootstrap, $\eta_{\max}$ retains 3/12 and $K_{\mathrm{eff}}$ retains 4/12, with $K_{\mathrm{eff}}$ slightly ahead. The directional pattern (all $K_{\mathrm{eff}}$ point estimates positive) persists uniformly. The random-fault contrast (\S\ref{sec:rf_contrast}) sharpens this: under random faults, $K_{\mathrm{eff}}$'s positive association with panel error survives all corrections (2/2 conditions, $R^2 = 0.73$--$0.81$), indicating a genuine relationship whose statistical confidence attenuates under adaptive attack (4/12 after correction).
294	
295	\begin{figure}[h]
296	\centering
297	\includegraphics[width=\columnwidth]{figures/fig2_gam_keff_split.pdf}
298	\caption{GAM bootstrap $K_{\mathrm{eff}}$ effect direction at $K{=}3$ ($B{=}9999$). All 12 conditions show positive $K_{\mathrm{eff}}$ direction (88.9--100\% bootstrap rate). The Kruskal--Wallis test finds no significant magnitude difference between targeted and shared-bias attacks ($p{=}0.200$).}
299	\label{fig:gam_split}
300	\end{figure}
301	
302	Under corrected data (V2), all 12 $K_{\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\times$ sycophancy coefficient ($\hat{\beta}_{\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\hat{\beta}_{\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\% positive rate) and 12/12 at $K{=}5$ (100\%).
303	
304	\subsection{Diversity--Capability Tradeoff}
305	\label{app:diversity_capability}
306	
307	The $r = 0.70$--$0.81$ correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ ($K{=}3$ to $K{=}5$) reflects a structural feature of the current LLM ecosystem: maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges. The structural correlation is unaffected by SE correction; it is a property of the model ecosystem, not an artifact of panel overlap. However, the high confound combined with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it.
308	
309	
310	Family-level labels provide indirect evidence that capability proximity matters more than taxonomic grouping: family membership is not a significant predictor of panel vulnerability ($p = 0.179$ on MMLU, $p = 0.385$ on ARC), consistent with models from the same provider exhibiting heterogeneous vulnerability profiles that vary by capability tier rather than by shared architecture \citep{kuncheva2003measures}.
311	
312	\subsection{Aggregation Rule Formal Definitions}
313	\label{app:aggregation_formal}
314	
315	We evaluate four aggregation rules for combining $K$ judge decisions. Let $d_j \in \{\text{A}, \text{B}, \text{tie}\}$ denote judge $j$'s winner label and $(s_j^A, s_j^B)$ its assigned scores.
316	
317	\paragraph{Majority Voting.} The panel decision is the mode of $\{d_1, \ldots, d_K\}$:
318	\begin{equation}
319	D_{\mathrm{maj}} = \arg\max_{c \in \{\text{A},\text{B},\text{tie}\}} \sum_{j=1}^{K} \mathbf{1}[d_j = c].
320	\end{equation}
321	Ties in the mode are broken uniformly at random. This is the simplest rule and makes no use of score magnitudes.
322	
323	\paragraph{Weighted Voting.} Each judge $j$ receives a weight $w_j = \text{acc}_j^{\text{clean}}$ proportional to its clean accuracy on the relevant benchmark. The panel decision is:
324	\begin{equation}
325	D_{\mathrm{wt}} = \arg\max_{c \in \{\text{A},\text{B},\text{tie}\}} \sum_{j=1}^{K} w_j \cdot \mathbf{1}[d_j = c].
326	\end{equation}
327	Weights are normalized so $\sum_j w_j = 1$. This rule upweights more accurate judges but does not account for judge-specific confusion patterns.
328	
329	\paragraph{Threshold Voting.} A \emph{unanimous} rule requiring all $K$ judges to agree:
330	\begin{equation}
331	D_{\mathrm{thr}} = \begin{cases} c & \text{if } d_j = c \;\forall\, j \in \{1,\ldots,K\}, \\ \text{tie} & \text{otherwise}. \end{cases}
332	\end{equation}
333	Under attack, an adversary succeeds if \emph{every} judge is manipulated---making threshold voting the most composition-sensitive rule ($R^2{=}0.829$ at $K{=}3$). However, threshold voting produces high tie rates on clean data, limiting its practical utility.
334	
335	\paragraph{Bayesian Calibration.} Each judge $j$ has a $3 \times 3$ confusion matrix $C_j$ estimated from clean evaluation data, where $C_j[c, c'] = \Pr(d_j {=} c' \mid \text{true} {=} c)$. Given observed decisions $\mathbf{d} = (d_1, \ldots, d_K)$ and a uniform prior over true labels:
336	\begin{equation}
337	\Pr(\text{true}{=}c \mid \mathbf{d}) \propto \prod_{j=1}^{K} C_j[c, d_j].
338	\end{equation}
339	The panel decision is $D_{\mathrm{Bayes}} = \arg\max_c \Pr(\text{true}{=}c \mid \mathbf{d})$. This is a simplified Dawid--Skene model \citep{dawid1979maximum} with fixed (non-EM) confusion matrices estimated from 300 clean samples per benchmark. Bayesian calibration downweights unreliable judges implicitly through their diffuse confusion matrices, reducing $K_{\mathrm{eff}}$'s predictive power ($R^2{=}0.087$ at $K{=}3$) by partially neutralizing the diversity channel.
340	
341	\paragraph{Per-Condition Aggregation Results.} Table~\ref{tab:aggregation_percond} reports $K_{\mathrm{eff}}$ standardized coefficients and significance across all 12 conditions for each aggregation method at $K{=}3$ (OLS with BH FDR correction).
342	
343	\begin{table*}[t]
344	\centering
345	\footnotesize
346	\setlength{\tabcolsep}{3pt}
347	\begin{tabular}{llcccccccc}
348	\toprule
349	& & \multicolumn{2}{c}{\textbf{Majority}} & \multicolumn{2}{c}{\textbf{Weighted}} & \multicolumn{2}{c}{\textbf{Threshold}} & \multicolumn{2}{c}{\textbf{Bayesian}} \\
350	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
351	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & sig & $\hat{\beta}_{\mathrm{std}}$ & sig & $\hat{\beta}_{\mathrm{std}}$ & sig & $\hat{\beta}_{\mathrm{std}}$ & sig \\
352	\midrule
353	\multirow{6}{*}{MMLU} & Prompt inj. & 0.252 & \checkmark & 0.237 & \checkmark & 0.195 & \checkmark & 0.119 & --- \\
354	& Sycophancy & 0.166 & \checkmark & 0.148 & \checkmark & 0.239 & \checkmark & 0.086 & --- \\
355	& Score manip. & 0.033 & --- & 0.041 & --- & 0.128 & \checkmark & 0.013 & --- \\
356	& Verbosity & 0.090 & \checkmark & 0.085 & --- & 0.167 & \checkmark & 0.041 & --- \\
357	& Position & 0.104 & --- & 0.092 & --- & 0.322 & \checkmark & 0.218 & \checkmark \\
358	& Authority & 0.010 & --- & 0.015 & --- & 0.073 & --- & $-0.025$ & --- \\
359	\addlinespace
360	\multirow{6}{*}{ARC} & Prompt inj. & 0.330 & \checkmark & 0.319 & \checkmark & 0.284 & \checkmark & 0.192 & \checkmark \\
361	& Sycophancy & $-0.192$ & \checkmark & $-0.178$ & \checkmark & 0.043 & --- & 0.031 & --- \\
362	& Score manip. & 0.252 & \checkmark & 0.261 & \checkmark & 0.198 & \checkmark & 0.163 & \checkmark \\
363	& Verbosity & 0.146 & --- & 0.139 & --- & 0.173 & \checkmark & 0.078 & --- \\
364	& Position & 0.584 & \checkmark & 0.571 & \checkmark & 0.415 & \checkmark & 0.280 & \checkmark \\
365	& Authority & 0.195 & \checkmark & 0.188 & \checkmark & 0.164 & \checkmark & 0.103 & \checkmark \\
366	\midrule
367	\multicolumn{2}{l}{\textbf{Significant count}} & \multicolumn{2}{c}{10/12} & \multicolumn{2}{c}{8/12} & \multicolumn{2}{c}{11/12} & \multicolumn{2}{c}{5/12} \\
368	\multicolumn{2}{l}{\textbf{Positive direction}} & \multicolumn{2}{c}{11+/1$-$} & \multicolumn{2}{c}{11+/1$-$} & \multicolumn{2}{c}{12+/0$-$} & \multicolumn{2}{c}{11+/1$-$} \\
369	\bottomrule
370	\end{tabular}
371	\caption{Per-condition $K_{\mathrm{eff}}$ coefficients across four aggregation methods ($K{=}3$, 455 panels, OLS log-log with BH FDR $\alpha{=}0.05$). Majority and weighted voting show similar per-condition patterns; threshold voting produces uniformly positive coefficients; Bayesian calibration attenuates coefficients across all conditions but retains significance for ARC conditions with strong $K_{\mathrm{eff}}$ signals.}
372	\label{tab:aggregation_percond}
373	\end{table*}
374	
375	\subsection{Aggregation Mechanism Details}
376	\label{app:aggregation_details}
377	
378	\begin{figure}[t]
379	\centering
380	\includegraphics[width=\columnwidth]{figures/fig3_aggregation_gradient.pdf}
381	\caption{$K_{\mathrm{eff}}$ coefficient distribution across aggregation methods ($K{=}3$). Majority and weighted voting: uniformly positive (12+/0$-$); Bayesian calibration: reduced predictability ($R^2{=}0.087$, 5+/1$-$).}
382	\label{fig:aggregation}
383	\end{figure}
384	
385	Bayesian calibration attenuates $K_{\mathrm{eff}}$ significance (5+/1$-$) and reduces overall predictability ($R^2{=}0.087$), but $\eta_{\max}$ persists (9/12 under OLS), providing partial defense. The pattern reflects calibrated reliability weighting: by estimating each judge's confusion matrix on clean data, Bayesian aggregation downweights weak judges, reducing the diversity channel while the individual weakness channel remains active. Threshold voting amplifies both channels because any single dissenting judge vetoes the panel decision, making compositional factors highly predictive of attack success ($R^2{=}0.829$). Bayesian calibration requires a clean accuracy prior, and an adaptive attacker aware of this calibration could target the prior itself \citep{tambe2011security}.
386	
387	
388	\subsection{Aggregation at \texorpdfstring{$K{=}5$}{K=5}}
389	\label{app:aggregation_k5}
390	
391	Table~\ref{tab:aggregation_k5} extends the aggregation analysis to $K{=}5$ (3{,}003 panels) under wild cluster bootstrap with 5-position max-$p$. All four aggregation methods yield identical $K_{\mathrm{eff}}$ significance (7/12), with $\eta_{\max}$ uniformly low (2--3/12). The Bayesian attenuation observed at $K{=}3$ (5+/1$-$; Table~\ref{tab:aggregation}) does not persist: $K_{\mathrm{eff}}$ reaches 7/12 regardless of aggregation rule. Predictability still varies ($\bar{R}^2$: threshold 0.408, Bayesian 0.166), but the diversity channel operates uniformly across all methods. At $K{=}7$, however, methods diverge again: Bayesian neutralization returns (0/12) while threshold voting strengthens to 10/12 (Table~\ref{tab:aggregation_k7}).
392	
393	\begin{table}[h]
394	\centering
395	\small
396	\begin{tabular}{lccc}
397	\toprule
398	\textbf{Aggregation} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} & $\boldsymbol{\bar{R}^2}$ \\
399	\midrule
400	Majority   & 2/12  & 7/12 & 0.285 \\
401	Weighted   & 2/12  & 7/12 & 0.275 \\
402	Threshold  & 3/12  & 7/12 & 0.408 \\
403	Bayesian   & 2/12  & 7/12 & 0.166 \\
404	\bottomrule
405	\end{tabular}
406	\caption{Aggregation method comparison at $K{=}5$ (3{,}003 panels, wild cluster bootstrap with 5-position max-$p$, BH FDR $\alpha{=}0.05$). All four methods converge to $K_{\mathrm{eff}}$ 7/12, unlike the differentiated pattern at $K{=}3$ (Table~\ref{tab:aggregation}).}
407	\label{tab:aggregation_k5}
408	\end{table}
409	
410	\subsection{Aggregation at \texorpdfstring{$K{=}7$}{K=7}}
411	\label{app:aggregation_k7}
412	
413	Table~\ref{tab:aggregation_k7} extends the aggregation analysis to $K{=}7$ (6{,}435 panels) under wild cluster bootstrap with 7-position max-$p$. Unlike the uniform convergence at $K{=}5$ (all methods 7/12), aggregation methods diverge at $K{=}7$: threshold voting strengthens to 10/12 while Bayesian calibration drops to 0/12, restoring the neutralization pattern absent at $K{=}5$.
414	
415	\begin{table}[h]
416	\centering
417	\small
418	\begin{tabular}{lccc}
419	\toprule
420	\textbf{Aggregation} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} & $\boldsymbol{\bar{R}^2}$ \\
421	\midrule
422	Majority   & 1/12  & 8/12 & 0.244 \\
423	Weighted   & 1/12  & 6/12 & 0.207 \\
424	Threshold  & 8/12  & 10/12 & 0.509 \\
425	Bayesian   & 1/12  & 0/12 & 0.105 \\
426	\bottomrule
427	\end{tabular}
428	\caption{Aggregation method comparison at $K{=}7$ (6{,}435 panels, wild cluster bootstrap with 7-position max-$p$, BH FDR $\alpha{=}0.05$). Unlike $K{=}5$ where all methods converge to 7/12, $K{=}7$ shows method divergence: threshold voting reaches 10/12 while Bayesian calibration returns to full $K_{\mathrm{eff}}$ neutralization (0/12).}
429	\label{tab:aggregation_k7}
430	\end{table}
431	
432	\begin{figure*}[t]
433	\centering
434	\includegraphics[width=\textwidth]{figures/fig_aggregation_comparison.pdf}
435	\caption{Aggregation method comparison: panel ASR vs.\ $K_{\mathrm{eff}}$ across four rules (majority, weighted, threshold, Bayesian) at $K{=}3$ and $K{=}5$. Threshold voting produces the steepest ASR--$K_{\mathrm{eff}}$ gradient ($R^2{=}0.829$ at $K{=}3$); Bayesian calibration flattens the relationship ($R^2{=}0.087$), consistent with Table~\ref{tab:aggregation}.}
436	\label{fig:aggregation_comparison}
437	\end{figure*}
438	
439	\begin{figure}[h]
440	\centering
441	\includegraphics[width=\columnwidth]{figures/fig_aggregation_r2_heatmap.pdf}
442	\caption{Mean $R^2$ heatmap across 4 aggregation methods $\times$ 3 panel sizes (12 conditions each). Threshold voting maintains high predictability across all $K$; Bayesian calibration shows an abrupt drop at $K{=}7$ (from 0.166 to 0.105), coinciding with $K_{\mathrm{eff}}$ neutralization in Table~\ref{tab:aggregation_k7}.}
443	\label{fig:aggregation_r2_heatmap}
444	\end{figure}
445	
446	The $R^2$ heatmap (Figure~\ref{fig:aggregation_r2_heatmap}) reveals a method $\times$ panel size interaction: majority and weighted voting show gradual $R^2$ decline with increasing $K$, while Bayesian calibration exhibits a non-monotonic pattern (neutralization at $K{=}3$, convergence at $K{=}5$, renewed neutralization at $K{=}7$), suggesting that the interaction between calibration weighting and combinatorial panel structure depends on the relative contribution of weak judges.
447	
448	\subsection{Metric Robustness Under Partial Panel Information}
449	\label{app:oracle}
450	
451	The main analysis computes $\eta_{\max}$ with full knowledge of panel composition (all three judges known). In deployment, a practitioner selecting or auditing a panel may know only a subset of the constituent judges. We test whether $\eta_{\max}$ retains predictive power under such partial information by recomputing it from two of the three panel members: for each panel, we cycle through all $\binom{3}{1} = 3$ leave-one-out masks, compute $\eta_{\max}$ from the two known judges, and average the regression estimates across masking scenarios.
452	
453	Under the most conservative inference (partial information + clustered SE), $\eta_{\max}$ remains the sole significant predictor with $\hat{\beta}_{\mathrm{std}} = 0.589$, achieving significance in 12/12 conditions, stronger than the oracle baseline (4/12 under clustered SE). $K_{\mathrm{eff}}$ loses all predictive power (0/12). The averaging over masking scenarios smooths estimation noise inherent in the three-judge oracle computation, strengthening the $\eta_{\max}$ signal. This demonstrates that $\eta_{\max}$ computed from partial panel information is robust to incomplete composition knowledge and retains (indeed improves) its predictive power for panel ASR.
454	
455	\subsection{VIF Collinearity Diagnostics}
456	\label{app:vif_diagnostics}
457	
458	The $K_{\mathrm{eff}}$--$\eta_{\max}$ correlation ($r{=}0.70$ at $K{=}3$, $r{=}0.81$ at $K{=}5$) raises collinearity concerns. We report variance inflation factors (VIF) and their implications for coefficient interpretation across panel sizes.
459	
460	\paragraph{Per-Condition VIF.} Table~\ref{tab:vif_percond} reports VIF values for each of the 12 conditions at $K{=}3$, $K{=}5$, and $K{=}7$. VIF is computed as $1/(1 - R^2_{\mathrm{aux}})$, where $R^2_{\mathrm{aux}}$ is the $R^2$ from regressing $K_{\mathrm{eff}}$ on $\eta_{\max}$.
461	
462	\begin{table}[h]
463	\centering
464	\footnotesize
465	\setlength{\tabcolsep}{3pt}
466	\begin{tabular}{llccc}
467	\toprule
468	\textbf{Bench.} & \textbf{Attack} & $K{=}3$ & $K{=}5$ & $K{=}7$ \\
469	\midrule
470	\multirow{6}{*}{MMLU} & Prompt inj. & 2.0 & 2.7 & 3.1 \\
471	& Sycophancy & 2.0 & 2.7 & 3.1 \\
472	& Score manip. & 2.0 & 2.7 & 3.1 \\
473	& Verbosity & 2.0 & 2.7 & 3.1 \\
474	& Position & 2.0 & 2.7 & 3.1 \\
475	& Authority & 2.0 & 2.7 & 3.1 \\
476	\addlinespace
477	\multirow{6}{*}{ARC} & Prompt inj. & 2.0 & 2.7 & 3.1 \\
478	& Sycophancy & 2.0 & 2.7 & 3.1 \\
479	& Score manip. & 2.0 & 2.7 & 3.1 \\
480	& Verbosity & 2.0 & 2.7 & 3.1 \\
481	& Position & 2.0 & 2.7 & 3.1 \\
482	& Authority & 2.0 & 2.7 & 3.1 \\
483	\bottomrule
484	\end{tabular}
485	\caption{Variance inflation factors for the $K_{\mathrm{eff}}$--$\eta_{\max}$ regression across panel sizes. VIF is constant across conditions within each $K$ because both predictors are computed from panel composition (not attack-specific). VIF increases with $K$ as growing panel sizes amplify inter-judge correlations. All values are below the conventional VIF${=}5$ threshold for $K{\leq}7$, though the API-only subset reaches VIF${=}4.4$ at $K{=}5$ (Table~\ref{tab:robustness_checks}).}
486	\label{tab:vif_percond}
487	\end{table}
488	
489	VIF is constant across conditions within each $K$ because both $K_{\mathrm{eff}}$ and $\eta_{\max}$ are panel properties computed from clean evaluation data, independent of attack type. The VIF increases with $K$ because larger panels share more judges, amplifying the structural correlation between diversity and capability measures. At $K{=}3$ (VIF${=}2.0$), standard errors are inflated by $\sqrt{2} \approx 1.41{\times}$, a moderate penalty. At $K{=}7$ (VIF${=}3.1$), inflation reaches $\sqrt{3.1} \approx 1.76{\times}$, still below the conventional ${>}5$ threshold that indicates severe collinearity.
490	
491	\paragraph{Partial Regression Coefficients.} The collinearity does not prevent coefficient identification at the full-pool level, but it does create instability in subgroup analyses. The API-only subset ($r{=}0.85$, VIF${=}4.4$) shows unstable per-condition coefficients (6 out of 12 conditions switch predictor dominance between OLS and bootstrap), while the capability-matched Pool~A ($r{=}0.50$, VIF${=}1.33$) produces stable coefficients (0 switches). This pattern supports the capability-matched subsampling approach (Appendix~\ref{app:robustness_checks}) as the most informative specification for disentangling the two predictors.
492	
493	\paragraph{Collinearity and the Predictor Shift.} The rising VIF across $K$ could, in principle, explain the apparent predictor shift: if increasing collinearity makes it harder to distinguish between $K_{\mathrm{eff}}$ and $\eta_{\max}$, significance could migrate between predictors. Three pieces of evidence argue against this: (1) the shift direction is consistent---$K_{\mathrm{eff}}$ always gains, $\eta_{\max}$ always loses---whereas collinearity-driven instability would produce bidirectional migration; (2) the Pool~A subsample ($r{=}0.50$) shows the same shift pattern with lower collinearity; (3) the fractional logit specification, which handles bounded outcomes differently, produces 98.6\% directional concordance with OLS across all conditions and $K$ values.
494	
495	\subsection{Random Fault Contrast: Detailed Results}
496	\label{app:rf_contrast_detail}
497	
498	Section~\ref{sec:rf_contrast} reports the aggregate random vs.\ adaptive fault contrast. Table~\ref{tab:rf_detail} provides the full per-benchmark breakdown.
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "389d3488-9173-4170-92a8-2567f4c84bff"
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
  "task_id": "a9b457fcfc91425c5",
  "tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 33454,
    "tool_uses": 3,
    "duration_ms": 9806
  },
  "last_tool_name": "Read",
  "uuid": "b8550945-2147-4d5b-842f-129f855c6df1",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01UELrTBietWf89zs7egtWLx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "418b0f97-b52c-40be-b63a-08ad05cdf517",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W3A7H7pXUadMCwS82qsVU7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17760,
      "cache_read_input_tokens": 15646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17760,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 45 · 2026-05-25T21:06:18.110Z_

<details><summary>↩ Tool result · `toolu_01UELrTBietWf89zs7egtWLx`</summary>

```text
500	
501	\begin{table}[h]
502	\centering
503	\small
504	\begin{tabular}{llcccc}
505	\toprule
506	\textbf{Bench.} & \textbf{Fault type} & $R^2$ & $K_{\mathrm{eff}}$ $\hat{\beta}$ & $\eta_{\max}$ $\hat{\beta}$ & $K_{\mathrm{eff}}$ sig \\
507	\midrule
508	\multirow{2}{*}{MMLU} & Random & 0.659 & 0.165 & 0.194 & \checkmark \\
509	& Adaptive (mean) & 0.340 & 0.349 & --- & 4/12 \\
510	\addlinespace
511	\multirow{2}{*}{ARC} & Random & 0.751 & 1.097 & 0.150 & \checkmark \\
512	& Adaptive (mean) & 0.285 & 0.437 & --- & 7/12 \\
513	\bottomrule
514	\end{tabular}
515	\caption{Random vs.\ adaptive fault contrast at $K{=}5$ (3{,}003 panels). Random faults flip judge votes at observed per-judge error rates (2 conditions: MMLU and ARC); adaptive results are averaged across 12 attack conditions. $R^2$ drops from 0.659--0.751 (random) to 0.285--0.340 (adaptive), demonstrating the predictability gap.}
516	\label{tab:rf_detail}
517	\end{table}
518	
519	\paragraph{Interpretation.} Under random (non-adversarial) faults, panel error is highly predictable ($R^2{>}0.65$) because fault independence holds: judges fail independently at their observed error rates, and $K_{\mathrm{eff}}$ directly captures the effective number of independent channels. Under adaptive attack, the adversary correlates judge failures by exploiting shared vulnerabilities (e.g., all judges susceptible to the same prompt injection), violating the independence assumption and reducing predictability.
520	
521	The residual $R^2 = 0.285$ under adaptive attack reflects the degree to which panel composition still predicts vulnerability despite adversarial optimization. This is substantially above zero because the adversary faces heterogeneous judge vulnerabilities: some attack strategies work against specific judges but not others, and the panel's overall vulnerability depends on which judges are included---a signal that $K_{\mathrm{eff}}$ and $\eta_{\max}$ capture, albeit imperfectly.
522	
523	The ARC random-fault $K_{\mathrm{eff}}$ coefficient ($\hat{\beta}{=}1.097$) is substantially larger than MMLU ($0.165$), reflecting ARC's higher baseline error rates that amplify the diversity channel. Under adaptive attack, coefficients attenuate but remain positive, consistent with the finding that diversity creates distinct attack surfaces (\S\ref{sec:rf_contrast}).
524	
525	\subsection{Meta-Analytic Pooling Procedure}
526	\label{app:meta_analytic_details}
527	
528	Section~\ref{sec:cross_k} reports pooled effect sizes using DerSimonian--Laird (DL) random effects \citep{dersimonian1986meta}. Here we detail the pooling procedure and assess sensitivity to alternative meta-analytic methods.
529	
530	\paragraph{Procedure.} For each predictor $X \in \{K_{\mathrm{eff}}, \eta_{\max}\}$ at each $K$, we compute 12 condition-specific standardized OLS coefficients $\hat{\beta}_{\mathrm{std}}^{(c)}$ with standard errors $\mathrm{SE}^{(c)}$ from the wild cluster bootstrap. DL random effects models the 12 condition estimates as:
531	\begin{equation}
532	\hat{\beta}_{\mathrm{std}}^{(c)} = \mu + u_c + \epsilon_c, \quad u_c \sim \mathcal{N}(0, \tau^2), \quad \epsilon_c \sim \mathcal{N}(0, \sigma_c^2),
533	\end{equation}
534	where $\mu$ is the pooled effect, $\tau^2$ captures between-condition heterogeneity, and $\sigma_c^2$ is the within-condition sampling variance. The DL estimator for $\tau^2$ uses the $Q$-statistic:
535	\begin{equation}
536	\hat{\tau}^2_{\mathrm{DL}} = \max\!\left(0, \frac{Q - (C-1)}{\sum w_c - \sum w_c^2 / \sum w_c}\right),
537	\end{equation}
538	with $w_c = 1/\sigma_c^2$ the inverse-variance weights and $C{=}12$ conditions.
539	
540	\paragraph{$I^2$ Heterogeneity.} The high $I^2$ values (87.7\%--99.8\%) indicate that most variation across conditions reflects genuine heterogeneity rather than sampling noise. This is expected: different attack types exploit different vulnerability mechanisms, and the two benchmarks differ in format and difficulty. The pooled estimate $\mu$ represents the central tendency across this heterogeneous landscape, not a single shared effect size.
541	
542	\paragraph{Per-$K$ Pooled Results.} Table~\ref{tab:meta_pooled} reports the complete pooled estimates.
543	
544	\begin{table}[h]
545	\centering
546	\footnotesize
547	\setlength{\tabcolsep}{3pt}
548	\begin{tabular}{rcccccc}
549	\toprule
550	& \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} \\
551	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
552	$\boldsymbol{K}$ & $\hat{\mu}$ & 95\% CI & $I^2$ & $\hat{\mu}$ & 95\% CI & $I^2$ \\
553	\midrule
554	3 & 0.264 & [0.158, 0.369] & 91.3\% & 0.356 & [0.267, 0.445] & 87.7\% \\
555	5 & 0.102 & [$-$0.055, 0.259] & 99.4\% & 0.436 & [0.318, 0.553] & 98.9\% \\
556	7 & 0.084 & [$-$0.083, 0.251] & 99.8\% & 0.401 & [0.298, 0.503] & 99.4\% \\
557	\bottomrule
558	\end{tabular}
559	\caption{DerSimonian--Laird random effects pooled estimates across 12 conditions per $K$. $\hat{\mu}$: pooled standardized coefficient. $I^2$: between-condition heterogeneity. $\eta_{\max}$'s CI crosses zero at $K{\geq}5$; $K_{\mathrm{eff}}$ remains positive across all $K$.}
560	\label{tab:meta_pooled}
561	\end{table}
562	
563	\paragraph{Sensitivity to Alternative Estimators.} We compare DL with the restricted maximum likelihood (REML) estimator and the Hartung--Knapp--Sidik--Jonkman (HKSJ) confidence interval adjustment. REML produces similar point estimates ($\Delta\hat{\mu} < 0.01$) but slightly wider CIs due to its likelihood-based $\tau^2$ estimation. HKSJ CIs are uniformly wider than DL (average width increase: 18\%), reflecting its $t$-distribution-based inference that accounts for small-sample heterogeneity estimation uncertainty. Under HKSJ, $K_{\mathrm{eff}}$ retains positive CI lower bounds at all $K$ values; $\eta_{\max}$'s CI crosses zero at $K{=}3$ as well (lower bound $-0.02$), making the pooled result borderline even at the smallest panel size. The DL estimates reported in the main text are therefore the most favorable for $\eta_{\max}$; the diminishing weakest link pattern is more pronounced under alternative estimators.
564	
565	\section{Panel Selection Strategy Comparison}
566	\label{app:panel_selection}
567	
568	\begin{figure}[h]
569	\centering
570	\includegraphics[width=\columnwidth]{figures/fig4_panel_design.pdf}
571	\caption{Panel ASR under three selection strategies ($\min \eta_{\max}$, random, $\max K_{\mathrm{eff}}$) across 12 conditions. Robustness-first selection ($\min \eta_{\max}$) achieves the lowest ASR in all conditions.}
572	\label{fig:panel_design}
573	\end{figure}
574	
575	Figure~\ref{fig:panel_design} compares three panel selection strategies: $\min(\eta_{\max})$ (select the panel minimizing weakest-judge vulnerability), random selection, and $\max(K_{\mathrm{eff}})$ (maximize diversity). The $\min(\eta_{\max})$ strategy achieves the lowest ASR in all 12 conditions, consistent with the weakest-link dominance documented in \S\ref{sec:dominance}.
576	
577	\section{Clustered Standard Error Analysis}
578	\label{app:clustered_se}
579	
580	Under clustered standard errors (clustering on the $K$ judge positions), $\eta_{\max}$ retains significance in 4/12 conditions while $K_{\mathrm{eff}}$ achieves significance in 0/12. This contrasts with OLS ($\eta_{\max}$ 10/12, $K_{\mathrm{eff}}$ 12/12) and wild cluster bootstrap ($\eta_{\max}$ 3/12, $K_{\mathrm{eff}}$ 4/12), illustrating how the choice of inference method modulates apparent significance at $K{=}3$ while coefficient direction remains positive (12/12) for $K_{\mathrm{eff}}$ across all methods, with significance ranging from 0/12 to 12/12 (Figure~\ref{fig:robustness}).
581	
582	\section{Robustness Checks: Subsampling and Specification}
583	\label{app:robustness_checks}
584	
585	Table~\ref{tab:robustness_checks} summarizes regression results across model subsets and alternative specifications at $K{=}5$, testing whether the predictor shift is robust to collinearity reduction and specification choice.
586	
587	\begin{table}[h]
588	\centering
589	\small
590	\begin{tabular}{lcccc}
591	\toprule
592	\textbf{Subset / Method} & $\boldsymbol{r}$ & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & \textbf{Trans.} \\
593	\midrule
594	Full bootstrap       & 0.81 & 2/12 & 7/12 & \checkmark \\
595	API-only (9) clust.  & 0.85 & 8/12 & 3/12 & --- \\
596	Cap-matched A (5A+4L) & 0.50 & ---  & 9/12 & \checkmark\checkmark \\
597	Cap-matched B (6A+3L) & 0.73 & ---  & 2/12 & --- \\
598	Fractional logit     & 0.81 & 6/12 & 9/12 & \checkmark \\
599	\bottomrule
600	\end{tabular}
601	\caption{Predictor shift robustness at $K{=}5$ across model subsets and specifications. $r$: correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$. $\eta_{\max}$ and $K_{\mathrm{eff}}$ columns show FDR-significant counts out of 12 conditions. Trans.: whether $K_{\mathrm{eff}}$ dominates $\eta_{\max}$. API-only models ($r{=}0.85$, VIF${=}4.4$) show partially collinear predictors; capability-matched subsamples ($r{=}0.50$) strengthen the shift. Fractional logit \citep{papke1996econometric} confirms OLS patterns with 98.6\% directional agreement (71/72 direction matches; the single discordance is $\eta_{\max}$ at $K{=}7$ for ARC $\times$ score manipulation).}
602	\label{tab:robustness_checks}
603	\end{table}
604	
605	The API-only subset ($r{=}0.85$, VIF${=}4.4$) demonstrates that elevated collinearity between $K_{\mathrm{eff}}$ and $\eta_{\max}$ partially inflates standard errors: both predictors achieve moderate significance but neither dominates, and the predictor shift does not replicate. Breaking collinearity through capability-matched subsampling (pool~A, $r{=}0.50$) strengthens $K_{\mathrm{eff}}$'s emergence to 9/12, comparable to the full-pool 7/12. Pool~B ($r{=}0.73$) falls near the decorrelation threshold, and the shift weakens accordingly. Random 9-model subsampling (1{,}000 trials) confirms an inverted-U: $K_{\mathrm{eff}}$ dominance rate peaks when the subsample includes 3--4 local models (maximizing capability spread) and drops when the pool is too homogeneous (Appendix~\ref{app:random_subsample}).
606	
607	\section{Random Subsample Analysis}
608	\label{app:random_subsample}
609	
610	To test whether the predictor shift depends on model pool composition, we randomly sample 9 of 15 models (1{,}000 trials), construct all $\binom{9}{5}$ panels, and run the bootstrap analysis at $K{=}5$. We stratify by the number of local models ($n_{\mathrm{local}} \in \{0, \ldots, 6\}$) in each subsample.
611	
612	Under clustered standard errors, $K_{\mathrm{eff}}$ is the dominant predictor in 51.4\% of subsamples (mean significance 1.85/12), with an inverted-U as a function of $n_{\mathrm{local}}$: subsamples with 3--4 local models (maximizing capability range) achieve the highest $K_{\mathrm{eff}}$ significance rate, while all-API ($n_{\mathrm{local}}{=}0$) and heavily-local ($n_{\mathrm{local}}{\geq}5$) subsamples show reduced detection. Significance is attenuated relative to the full pool by smaller sample sizes (126 vs.\ 3{,}003 panels at $K{=}5$), but the shift direction holds in the majority of subsamples. This confirms that the shift's detectability depends on capability diversity in the model pool rather than pool size per se.
613	
614	\section{Attacked $K_{\mathrm{eff}}$ Stability}
615	\label{app:attacked_keff}
616	
617	$K_{\mathrm{eff}}$ is computed from clean (unattacked) pairwise MI (\S\ref{sec:experiments}), but used to predict vulnerability under attack. We verify this assumption by recomputing MI from judge outputs under each attack type and comparing clean vs.\ attacked $K_{\mathrm{eff}}$ via Spearman rank correlation across all panels.
618	
619	\begin{table}[h]
620	\centering
621	\small
622	\begin{tabular}{lcc}
623	\toprule
624	\textbf{Attack} & \textbf{MMLU $\rho$} & \textbf{ARC $\rho$} \\
625	\midrule
626	Score manipulation & 0.98 & 0.99 \\
627	Authority bias     & 0.95 & 0.97 \\
628	Sycophancy         & 0.91 & 0.92 \\
629	Verbosity bias     & 0.91 & 0.92 \\
630	Prompt injection   & 0.63 & 0.60 \\
631	Position bias      & 0.60 & 0.08 \\
632	\bottomrule
633	\end{tabular}
634	\caption{Spearman rank correlation between clean and attacked $K_{\mathrm{eff}}$ across 455 panels ($K{=}3$). Four attack types preserve MI structure ($\rho{\geq}0.91$); prompt injection shows moderate perturbation ($\rho{\approx}0.60$--$0.63$); position bias substantially disrupts pairwise dependencies.}
635	\label{tab:attacked_keff}
636	\end{table}
637	
638	Four attack types (score manipulation, authority bias, sycophancy, verbosity bias) preserve MI structure with $\rho{\geq}0.91$ on both benchmarks, validating the use of clean $K_{\mathrm{eff}}$ as a predictor. Prompt injection shows moderate perturbation ($\rho{\approx}0.60$--$0.63$), consistent with its mode of overriding evaluation instructions, which can alter pairwise agreement patterns. Position bias substantially disrupts MI structure ($\rho{=}0.08$ on ARC, $p{=}0.10$), consistent with its anomalous regression behavior in Table~\ref{tab:dominance} (sole non-significant $\eta_{\max}$ condition) and suggesting that positional reordering fundamentally changes inter-judge dependence rather than merely introducing noise.
639	
640	\section{Cinelli--Hazlett Sensitivity Analysis}
641	\label{app:sensitivity}
642	
643	We apply the Cinelli--Hazlett omitted variable bias framework to quantify how robust $K_{\mathrm{eff}}$'s coefficient is to unobserved confounders. For each of the 36 conditions ($3K \times 2$ benchmarks $\times$ $6$ attacks), we compute the robustness value (RV): the minimum strength an unobserved confounder must have, in terms of partial $R^2$ with both treatment and outcome, to reduce $K_{\mathrm{eff}}$'s coefficient to zero.
644	
645	\begin{table}[h]
646	\centering
647	\footnotesize
648	\setlength{\tabcolsep}{3pt}
649	\begin{tabular}{rcllcccc}
650	\toprule
651	$\boldsymbol{K}$ & \textbf{Data} & \textbf{Attack} & \textbf{RV} & $\boldsymbol{\eta}$ $\boldsymbol{R^2_{\mathrm{tr}}}$ & $\boldsymbol{\eta}$ $\boldsymbol{R^2_{\mathrm{out}}}$ & \textbf{Exc.} \\
652	\midrule
653	\multirow{12}{*}{3} & \multirow{6}{*}{MMLU} & Prompt inj.    & 0.419 & 0.587 & 0.059 & -- \\
654	 &  & Sycophancy     & 0.412 & 0.347 & 0.098 & \checkmark \\
655	 &  & Score manip.   & 0.410 & 0.735 & 0.002 & -- \\
656	 &  & Verbosity      & 0.330 & 0.342 & 0.203 & -- \\
657	 &  & Position bias  & 0.291 & 0.446 & 0.043 & -- \\
658	 &  & Authority bias & 0.371 & 0.493 & 0.019 & \checkmark \\
659	\addlinespace[2pt]
660	 & \multirow{6}{*}{ARC} & Prompt inj.    & 0.303 & 0.654 & 0.028 & \checkmark \\
661	 &  & Sycophancy     & 0.105 & 0.629 & 0.129 & \checkmark \\
662	 &  & Score manip.   & 0.273 & 0.838 & 0.003 & -- \\
663	 &  & Verbosity      & 0.259 & 0.658 & 0.047 & -- \\
664	 &  & Position bias  & 0.265 & 0.850 & 0.001 & -- \\
665	 &  & Authority bias & 0.224 & 0.582 & 0.056 & -- \\
666	\addlinespace
667	\multirow{12}{*}{5} & \multirow{6}{*}{MMLU} & Prompt inj.    & 0.455 & 0.379 & 0.176 & \checkmark \\
668	 &  & Sycophancy     & 0.303 & 0.106 & 0.135 & \checkmark \\
669	 &  & Score manip.   & 0.321 & 0.597 & 0.003 & -- \\
670	 &  & Verbosity      & 0.235 & 0.120 & 0.206 & \checkmark \\
671	 &  & Position bias  & 0.131 & 0.272 & 0.090 & -- \\
672	 &  & Authority bias & 0.064 & 0.277 & 0.031 & -- \\
673	\addlinespace[2pt]
674	 & \multirow{6}{*}{ARC} & Prompt inj.    & 0.318 & 0.696 & 0.001 & -- \\
675	 &  & Sycophancy     & 0.103 & 0.555 & 0.063 & -- \\
676	 &  & Score manip.   & 0.196 & 0.800 & ${<}0.001$ & -- \\
677	 &  & Verbosity      & 0.135 & 0.642 & 0.034 & -- \\
678	 &  & Position bias  & 0.400 & 0.778 & 0.040 & -- \\
679	 &  & Authority bias & 0.181 & 0.509 & 0.012 & -- \\
680	\addlinespace
681	\multirow{12}{*}{7} & \multirow{6}{*}{MMLU} & Prompt inj.    & 0.522 & 0.289 & 0.126 & \checkmark \\
682	 &  & Sycophancy     & 0.301 & 0.077 & 0.078 & \checkmark \\
683	 &  & Score manip.   & 0.393 & 0.515 & 0.004 & -- \\
684	 &  & Verbosity      & 0.205 & 0.078 & 0.195 & \checkmark \\
685	 &  & Position bias  & 0.207 & 0.179 & 0.073 & \checkmark \\
686	 &  & Authority bias & 0.005 & 0.200 & 0.011 & -- \\
687	\addlinespace[2pt]
688	 & \multirow{6}{*}{ARC} & Prompt inj.    & 0.355 & 0.629 & 0.004 & -- \\
689	 &  & Sycophancy     & 0.117 & 0.535 & 0.065 & -- \\
690	 &  & Score manip.   & 0.165 & 0.717 & 0.001 & -- \\
691	 &  & Verbosity      & 0.165 & 0.599 & 0.028 & -- \\
692	 &  & Position bias  & 0.422 & 0.705 & 0.046 & -- \\
693	 &  & Authority bias & 0.179 & 0.514 & 0.003 & -- \\
694	\bottomrule
695	\end{tabular}
696	\caption{Cinelli--Hazlett sensitivity analysis for $K_{\mathrm{eff}}$'s coefficient across 36 conditions. RV: robustness value (minimum partial $R^2$ an unobserved confounder must have with both $K_{\mathrm{eff}}$ and ASR to nullify the coefficient). $\eta$ $R^2_{\mathrm{tr}}$/$R^2_{\mathrm{out}}$: partial $R^2$ of $\eta_{\max}$ with $K_{\mathrm{eff}}$ (treatment) and ASR (outcome). Exc.: \checkmark\ if RV exceeds $\eta_{\max}$'s partial $R^2$ with treatment, indicating $K_{\mathrm{eff}}$'s coefficient is robust to the known capability confound. RV exceeds $\eta_{\max}$ in 11/36 conditions ($K{=}3$: 4/12, $K{=}5$: 3/12, $K{=}7$: 4/12).}
697	\label{tab:sensitivity}
698	\end{table}
699	
700	RV ranges from 0.005--0.59 across the 36 conditions (median by $K$: 0.30 at $K{=}3$, 0.22 at $K{=}5$, 0.21 at $K{=}7$), revealing heterogeneous robustness: some conditions show $K_{\mathrm{eff}}$ coefficients robust to strong confounders (e.g., $K{=}7$ MMLU prompt injection, RV${=}0.52$), while others are fragile (e.g., $K{=}7$ MMLU authority bias, RV${=}0.005$). The known $\eta_{\max}$ confound exceeds RV in 25/36 conditions ($K{=}3$: 8/12, $K{=}5$: 9/12, $K{=}7$: 8/12). RV exceeds $\eta_{\max}$ in 3--4/12 conditions across all $K$ values (4/12 at $K{=}3$, 3/12 at $K{=}5$, 4/12 at $K{=}7$), indicating that $K_{\mathrm{eff}}$'s robustness to omitted variable bias is stable rather than monotonically increasing with panel size.
701	
702	\begin{figure*}[t]
703	\centering
704	\includegraphics[width=\textwidth]{figures/fig_sensitivity_contour_K3.pdf}
705	\caption{Cinelli--Hazlett sensitivity contour plots at $K{=}3$ (12 conditions). Each panel shows the adjusted $K_{\mathrm{eff}}$ coefficient as a function of hypothetical confounder strength (partial $R^2$ with treatment and outcome). Diamonds mark the $\eta_{\max}$ confound benchmark. At $K{=}3$, the benchmark falls outside the zero-contour in 4/12 conditions, indicating partial robustness.}
706	\label{fig:sensitivity_contour_K3}
707	\end{figure*}
708	
709	\begin{figure*}[t]
710	\centering
711	\includegraphics[width=\textwidth]{figures/fig_sensitivity_contour_K5.pdf}
712	\caption{Cinelli--Hazlett sensitivity contour plots at $K{=}5$ (12 conditions). Format identical to Figure~\ref{fig:sensitivity_contour_K3}. The $\eta_{\max}$ benchmark falls inside the zero-contour for 9/12 conditions, indicating that the known capability confound could explain away $K_{\mathrm{eff}}$'s effect in the majority of conditions at this panel size.}
713	\label{fig:sensitivity_contour}
714	\end{figure*}
715	
716	\begin{figure*}[t]
717	\centering
718	\includegraphics[width=\textwidth]{figures/fig_sensitivity_contour_K7.pdf}
719	\caption{Cinelli--Hazlett sensitivity contour plots at $K{=}7$ (12 conditions). Format identical to Figure~\ref{fig:sensitivity_contour_K3}. RV heterogeneity is most pronounced at this panel size: MMLU prompt injection achieves RV${=}0.52$ while MMLU authority bias drops to RV${=}0.005$ (Table~\ref{tab:sensitivity}).}
720	\label{fig:sensitivity_contour_K7}
721	\end{figure*}
722	
723	\section{Cross-Benchmark Prediction Robustness}
724	\label{app:cross_benchmark}
725	
726	\begin{figure}[h]
727	\centering
728	\includegraphics[width=\columnwidth]{figures/fig_keff_cross_benchmark.pdf}
729	\caption{Cross-benchmark $K_{\mathrm{eff}}$ correspondence at $K{=}5$ ($n{=}3{,}003$ panels). Each point is one panel; Spearman $\rho{=}0.901$. The high rank correlation confirms that $K_{\mathrm{eff}}$ captures panel-level structural independence rather than benchmark-specific interactions.}
730	\label{fig:keff_cross_benchmark}
731	\end{figure}
732	
733	The near-linear scatter (Figure~\ref{fig:keff_cross_benchmark}) confirms that $K_{\mathrm{eff}}$ is a panel-intrinsic property: panels achieving high effective independence on MMLU do so on ARC as well, supporting $K_{\mathrm{eff}}$'s use as a general panel descriptor independent of evaluation task.
734	
735	To test whether the diversity--vulnerability association reflects structural panel properties rather than benchmark-specific artifacts, we use $K_{\mathrm{eff}}$ computed from one benchmark's pairwise MI to predict panel vulnerability on the other. Under wild cluster bootstrap (FDR $\alpha{=}0.05$), both directions achieve 17/18 sign-consistent conditions across $K \in \{3, 5, 7\}$ (5/6 at $K{=}3$, 6/6 at $K{\geq}5$). The sole exception in both directions is $K{=}3$ position bias, where all judges share similar ASR (${\sim}0.5$), leaving insufficient heterogeneity for $K_{\mathrm{eff}}$ to discriminate. Cross-benchmark $K_{\mathrm{eff}}$ correlations are $r{\approx}0.76$--$0.78$, indicating that $K_{\mathrm{eff}}$ primarily captures panel-level compositional structure rather than benchmark-specific judge interactions. While sign consistency is symmetric, cross-prediction $R^2$ is moderately asymmetric (ARC$\to$MMLU generally higher), suggesting that coefficients estimated from ARC's more constrained binary format generalize conservatively to MMLU's richer four-way choice distribution.
736	
737	\section{Pool A Cinelli--Hazlett Sensitivity}
738	\label{app:sensitivity_poolA}
739	
740	To test whether reducing the $K_{\mathrm{eff}}$--$\eta_{\max}$ collinearity strengthens $K_{\mathrm{eff}}$'s independent signal, we repeat the Cinelli--Hazlett analysis on the capability-matched Pool~A subsample (9 models, $r{=}0.50$, 84 panels at $K{=}3$, 126 at $K{=}5$). Table~\ref{tab:sensitivity_poolA} compares the full-pool results with Pool~A.
741	
742	\begin{table}[h]
743	\centering
744	\small
745	\begin{tabular}{lccc}
746	\toprule
747	\textbf{Pool / $K$} & \textbf{RV $>$ $\eta$} & \textbf{Median RV} & \textbf{$K_{\mathrm{eff}}$ sig} \\
748	\midrule
749	Full / $K{=}3$ & 1/12 & 0.30 & 1/12 \\
750	Full / $K{=}5$ & 3/12 & 0.22 & 7/12 \\
751	Pool A / $K{=}3$ & 2/12 & 0.25 & --- \\
752	Pool A / $K{=}5$ & 10/12 & 0.32 & 9/12 \\
753	\bottomrule
754	\end{tabular}
755	\caption{Cinelli--Hazlett sensitivity comparison: full pool vs.\ capability-matched Pool~A. RV $>$ $\eta$: conditions where $K_{\mathrm{eff}}$'s robustness value exceeds the known $\eta_{\max}$ confound benchmark. Pool~A's reduced collinearity ($r{=}0.50$ vs.\ $0.81$ at $K{=}5$) increases the fraction of robust conditions from 1/12 to 2/12 at $K{=}3$ and from 3/12 to 10/12 at $K{=}5$, with the largest gains at $K{=}5$ where both benchmarks improve equally (ARC 5/6, MMLU 5/6).}
756	\label{tab:sensitivity_poolA}
757	\end{table}
758	
759	At $K{=}5$, Pool~A RV exceeds the $\eta_{\max}$ confound in 10/12 conditions (ARC 5/6, MMLU 5/6; the two failures are both sycophancy). The improvement from full-pool 3/12 to Pool~A 10/12 demonstrates that reducing collinearity substantially separates $K_{\mathrm{eff}}$'s signal from capability variance, though full causal identification would require training-based diversity control.
760	
761	\paragraph{Pool~A Power Constraints.}
762	Pool~A's restricted sample (84 panels at $K{=}3$, 126 at $K{=}5$) substantially limits statistical power under wild cluster bootstrap. Table~\ref{tab:poolA_power} reports power at standard effect sizes ($n_{\mathrm{sim}}{=}1{,}000$).
763	
764	\begin{table}[h]
765	\centering
766	\small
767	\begin{tabular}{rcc}
768	\toprule
769	$\boldsymbol{\beta_{\mathrm{std}}}$ & $\boldsymbol{K{=}3}$ \textbf{power} & $\boldsymbol{K{=}5}$ \textbf{power} \\
770	\midrule
771	0.3 & 12.6\% & 2.2\% \\
772	0.5 & 42.1\% & 8.5\% \\
773	0.7 & 69.0\% & 17.5\% \\
774	1.0 & 85.8\% & 30.1\% \\
775	\bottomrule
776	\end{tabular}
777	\caption{Pool~A bootstrap power ($n_{\mathrm{sim}}{=}1{,}000$, wild cluster bootstrap). MDE at 80\%: $K{=}3$, $\beta_{\mathrm{std}}{=}0.897$; $K{=}5$, not attainable (maximum 30.1\% at $\beta_{\mathrm{std}}{=}1.0$).}
778	\label{tab:poolA_power}
779	\end{table}
780	
781	Two implications follow. First, Pool~A at $K{=}5$ is fundamentally underpowered: the maximum attainable power (30.1\% at $\beta_{\mathrm{std}}{=}1.0$) never reaches 80\%. The 10/12 Cinelli--Hazlett success at $K{=}5$ therefore reflects large effect sizes surviving low power, strengthening the causal signal. Second, the low Cinelli--Hazlett RV at $K{=}3$ (2/12 exceeding the $\eta_{\max}$ benchmark) is partially explained by Pool~A's 84-panel design: MDE$_{\,80\%}{=}0.897$ means only effects exceeding ${\approx}0.9$ SD are detectable. Crucially, the full-pool $K{=}3 \to K{=}5$ significance increase ($4/12 \to 7/12$) is not a power artifact: Pool~A power at $K{=}5$ (max 30.1\%) is \emph{lower} than at $K{=}3$ (max 85.8\%), so the increase reflects growing effect sizes rather than inflated type~I error.
782	
783	\section{Epsilon Sensitivity Analysis}
784	\label{app:epsilon}
785	
786	The log-log specification (Equation~\ref{eq:regression}) uses $\epsilon{=}10^{-6}$ to handle zero ASR values. We assess sensitivity by comparing coefficients across $\epsilon \in \{10^{-3}, 10^{-6}, 10^{-9}\}$. Zero ASR rates are low on MMLU ($<$1\% of panels across conditions) but can reach 38--40\% on ARC for authority bias and sycophancy at $K{=}7$. Coefficient magnitudes show moderate sensitivity to $\epsilon$ at $K{=}3$ (maximum $\Delta\beta_{\mathrm{std}} = 0.10$ between $\epsilon{=}10^{-6}$ and $\epsilon{=}10^{-9}$, with three conditions exhibiting $K_{\mathrm{eff}}$ sign changes), reflecting the influence of zero-ASR panels on the log transformation. At $K{=}5$, all $K_{\mathrm{eff}}$ coefficient directions are preserved across $\epsilon$ values (maximum $\Delta\beta_{\mathrm{std}} = 0.073$ between $\epsilon{=}10^{-6}$ and $\epsilon{=}10^{-9}$, all $p < 0.005$), confirming that the predictor shift finding is robust to this modeling choice. The fractional logit specification (\S\ref{sec:experiments}), which avoids the log+$\epsilon$ transformation entirely, provides 98.6\% directional concordance with the main OLS results (71/72 direction matches) (Appendix~\ref{app:robustness_checks}).
787	
788	\subsection{Temperature Sensitivity Pilot}
789	\label{app:temperature}
790	
791	We evaluate $K_{\mathrm{eff}}$ stability across decoding temperatures $t \in \{0.0, 0.3, 0.7, 1.0\}$ using a 3-model pilot (GPT-4.1-nano, Gemini-3.5-Flash, Claude-3-Haiku; 300 clean samples per benchmark, 3 repeats). The maximum $K_{\mathrm{eff}}$ variation across all four temperatures is $\Delta < 0.034$ (MMLU: 0.033, ARC: 0.027), confirming that decoding randomness does not meaningfully perturb pairwise MI structure. Clean $K_{\mathrm{eff}}$ computation is thus robust to temperature variation within the range used by standard API configurations.
792	
793	\section{$K_{\mathrm{eff}}$ Distribution Statistics}
794	\label{app:keff_dist}
795	
796	Table~\ref{tab:keff_dist} summarizes the distribution of $K_{\mathrm{eff}}$ across panel sizes.
797	
798	\begin{table}[h]
799	\centering
800	\small
801	\begin{tabular}{rrccc}
802	\toprule
803	$\boldsymbol{K}$ & \textbf{Panels} & \textbf{Mean (SD)} & \textbf{Range} \\
804	\midrule
805	3 & 455     & 2.18 (0.30) & [1.47, 2.80] \\
806	5 & 3{,}003 & 3.35 (0.42) & [2.16, 4.30] \\
807	7 & 6{,}435 & 4.53 (0.47) & [2.97, 5.55] \\
808	\bottomrule
809	\end{tabular}
810	\caption{$K_{\mathrm{eff}}$ distribution across panel sizes. Mean $K_{\mathrm{eff}}$ increases approximately linearly with $K$ but remains below the theoretical maximum ($K_{\mathrm{eff}} = K$ for fully independent judges), reflecting non-zero inter-judge correlations.}
811	\label{tab:keff_dist}
812	\end{table}
813	
814	$K_{\mathrm{eff}}$ exhibits sufficient variance at each $K$ for regression analysis (coefficient of variation 10--14\%), with no floor or ceiling effects that would compress the predictor range.
815	
816	\begin{figure}[h]
817	\centering
818	\includegraphics[width=\columnwidth]{figures/fig_keff_hist.pdf}
819	\caption{$K_{\mathrm{eff}}$ distributions across panel sizes ($K{=}3$: $n{=}455$; $K{=}5$: $n{=}3{,}003$; $K{=}7$: $n{=}6{,}435$). Mean $K_{\mathrm{eff}}$ increases sublinearly with $K$ (2.18, 3.35, 4.53), remaining below the independence ceiling $K_{\mathrm{eff}}{=}K$. Distributions are approximately normal with moderate spread (CV: 10--14\%).}
820	\label{fig:keff_hist}
821	\end{figure}
822	
823	The histograms (Figure~\ref{fig:keff_hist}) complement Table~\ref{tab:keff_dist}, confirming that $K_{\mathrm{eff}}$ exhibits approximately Gaussian distributions at each panel size with no floor or ceiling effects. The sublinear growth (mean $K_{\mathrm{eff}}/K$ ratios: 0.73, 0.67, 0.65) quantifies the increasing inter-judge correlation at larger panel sizes, consistent with the multi-membership structure documented in Appendix~\ref{app:crossed_re}.
824	
825	\section{Power Analysis Across Panel Sizes}
826	\label{app:power_analysis}
827	
828	Table~\ref{tab:mde} reports minimum detectable effect sizes (MDE at 80\% power) under wild cluster bootstrap for each $K$. The sharp decrease in MDE from $K{=}3$ to $K{=}5$ (0.144 to 0.048) reflects both increased sample size ($455 \to 3{,}003$ panels) and more clusters per position. $K_{\mathrm{eff}}$'s partial significance at $K{=}3$ (4/12) is consistent with moderate power at this sample size; the 7/12 significance at $K{=}5$ is not type~I error inflation, as the design can detect effects as small as 0.048 SD.
829	
830	\begin{table}[h]
831	\centering
832	\small
833	\begin{tabular}{rccc}
834	\toprule
835	$\boldsymbol{K}$ & \textbf{Panels} & \textbf{MDE ($\beta_{\mathrm{std}}$)} & \textbf{$K_{\mathrm{eff}}$ sig} \\
836	\midrule
837	3 & 455     & 0.144 & 4/12 \\
838	5 & 3{,}003 & 0.048 & 7/12 \\
839	7 & 6{,}435 & 0.036 & 8/12 \\
840	\bottomrule
841	\end{tabular}
842	\caption{Minimum detectable effect size (80\% power, 1{,}000 simulations, wild cluster bootstrap) by panel size. MDE decreases approximately as $1/\sqrt{N}$, confirming that $K{=}5$/$K{=}7$ significance reflects genuine effects rather than inflated type~I error.}
843	\label{tab:mde}
844	\end{table}
845	
846	\section{Alternative Diversity Measures}
847	\label{app:alt_diversity}
848	
849	We compare $K_{\mathrm{eff}}$ against three classical ensemble diversity measures using the same OLS specification (Equation~\ref{eq:regression}) with FDR correction across 12 conditions pooled over $K$ values.
850	
851	\begin{table}[h]
852	\centering
853	\small
854	\begin{tabular}{lcccc}
855	\toprule
856	\textbf{Measure} & \textbf{Sig} & \textbf{Dir.} & \textbf{$|\bar{\beta}_{\mathrm{std}}|$} & $\boldsymbol{\rho}$ \textbf{w/} $\boldsymbol{K_{\mathrm{eff}}}$ \\
857	\midrule
858	$Q$-statistic    & 9/12  & 6+/3$-$ & 0.251 & 0.599 \\
859	Disagreement     & 11/12 & 11+/0$-$ & 0.481 & 0.934 \\
860	$\kappa$-diversity & 11/12 & 11+/0$-$ & 0.497 & 0.978 \\
861	\addlinespace
862	$K_{\mathrm{eff}}$ (ref.) & 12/12 & 12+/0$-$ & 0.430 & --- \\
863	\bottomrule
864	\end{tabular}
865	\caption{Comparison of diversity measures as predictors of panel ASR (OLS, FDR-corrected, 12 conditions pooled across $K$). Sig: FDR-significant conditions. $|\bar{\beta}_{\mathrm{std}}|$: mean absolute standardized coefficient. $\rho$: Pearson correlation with $K_{\mathrm{eff}}$.}
866	\label{tab:alt_diversity}
867	\end{table}
868	
869	$K_{\mathrm{eff}}$ and $\kappa$-diversity \citep{kuncheva2003measures} are near-equivalent ($\rho{=}0.978$), with comparable significance counts (12/12 vs.\ 11/12) and effect sizes (0.430 vs.\ 0.497). Disagreement rate achieves similar predictive power ($\rho{=}0.934$, 11/12). The $Q$-statistic is the weakest predictor (9/12, $|\bar{\beta}_{\mathrm{std}}|{=}0.251$), consistent with its known insensitivity to the type of error correlation that is associated with panel vulnerability \citep{kuncheva2003measures}. $K_{\mathrm{eff}}$'s advantage over these alternatives is not predictive power but interpretability: it quantifies the number of effective independent channels in the panel, connecting directly to the information-theoretic foundation of panel aggregation (\S\ref{sec:experiments}).
870	
871	\subsection{$\kappa$-Diversity Predictor Shift Comparison}
872	\label{app:kappa_regime}
873	
874	To test whether the predictor shift (\S\ref{sec:cross_k}) is specific to $K_{\mathrm{eff}}$ or a generic property of diversity measures, we repeat the wild cluster bootstrap analysis replacing $K_{\mathrm{eff}}$ with $\kappa$-diversity ($1 - \bar{\kappa}$, where $\bar{\kappa}$ is the mean pairwise Cohen's $\kappa$ on clean winner labels; $\rho{=}0.978$ with $K_{\mathrm{eff}}$).
875	
876	\begin{table}[h]
877	\centering
878	\small
879	\begin{tabular}{rcccc}
880	\toprule
881	& \multicolumn{2}{c}{\textbf{$K_{\mathrm{eff}}$}} & \multicolumn{2}{c}{\textbf{$\kappa$-diversity}} \\
882	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
883	$\boldsymbol{K}$ & \textbf{div.\ sig} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & \textbf{div.\ sig} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} \\
884	\midrule
885	3 & 4/12  & 3/12 & 8/12 & 1/12 \\
886	5 & 7/12 & 2/12 & 7/12 & 4/12 \\
887	7 & 8/12  & 1/12 & 6/12 & 1/12 \\
888	\bottomrule
889	\end{tabular}
890	\caption{Predictor shift comparison: $K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity across panel sizes (wild cluster bootstrap, BH FDR $\alpha{=}0.05$). $K_{\mathrm{eff}}$ exhibits a clear shift ($4 \to 7 \to 8$); $\kappa$-diversity significance decreases monotonically ($8 \to 7 \to 6$), showing no predictor shift.}
891	\label{tab:kappa_regime}
892	\end{table}
893	
894	$\kappa$-diversity is a stronger predictor than $K_{\mathrm{eff}}$ at $K{=}3$ (8/12 vs.\ 4/12), consistent with its larger mean effect size ($|\bar{\beta}_{\mathrm{std}}|{=}0.497$ vs.\ 0.430; Table~\ref{tab:alt_diversity}). However, $\kappa$-diversity shows no predictor shift: its significance \emph{decreases} from $K{=}3$ to $K{=}7$ ($8 \to 7 \to 6$), the opposite of $K_{\mathrm{eff}}$'s pattern ($4 \to 7 \to 8$). Furthermore, under $\kappa$-diversity, $\eta_{\max}$ retains significance at $K{=}5$ (4/12), whereas under $K_{\mathrm{eff}}$ it drops to 2/12. The predictor shift---co-determination at $K{=}3$ transitioning to diversity dominance at $K{\geq}5$---is thus specific to $K_{\mathrm{eff}}$'s MI-based formulation, which captures effective judge independence rather than pairwise label agreement.
895	
896	\subsection{Shannon MI Entropy Predictor Shift Comparison}
897	\label{app:shannon_entropy}
898	
899	Shannon MI entropy ($H_{\mathrm{MI}} = \binom{K}{2}^{-1} \sum_{i<j} \mathrm{MI}(i,j)$) averages raw pairwise mutual information, measuring mean non-redundancy rather than effective independence. It correlates negatively with $K_{\mathrm{eff}}$ ($r = -0.63$ to $-0.76$ across $K$): panels with high mean MI tend to have lower effective independent channels, because $K_{\mathrm{eff}}$'s $\exp(-2\,\mathrm{MI})$ transform penalizes high MI more aggressively than linear averaging.
900	
901	\begin{table}[h]
902	\centering
903	\small
904	\begin{tabular}{rcc}
905	\toprule
906	$\boldsymbol{K}$ & \textbf{Shannon MI sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} \\
907	\midrule
908	3 & 4/12 & 6/12 \\
909	5 & 4/12 & 8/12 \\
910	7 & 0/12 & 2/12 \\
911	\bottomrule
912	\end{tabular}
913	\caption{Predictor shift comparison: Shannon MI entropy vs.\ $K_{\mathrm{eff}}$ (within-framework wild cluster bootstrap, $B{=}999$, Webb weights, BH FDR $\alpha{=}0.05$). Shannon is flat then collapses ($4 \to 4 \to 0$); $K_{\mathrm{eff}}$ rises before declining ($6 \to 8 \to 2$). Bootstrap parameters differ from the primary analysis ($B{=}9{,}999$, Rademacher); absolute counts are not comparable with Table~\ref{tab:kappa_regime}.}
914	\label{tab:shannon_shift}
915	\end{table}
916	
917	Shannon MI entropy shows no predictor shift: significance is flat at $K{=}3$ and $K{=}5$ (4/12) before collapsing at $K{=}7$ (0/12). $K_{\mathrm{eff}}$ exhibits a clear rise from $K{=}3$ to $K{=}5$ ($6 \to 8$) within the same framework. Combined with the $\kappa$-diversity comparison (Appendix~\ref{app:kappa_regime}, $8 \to 7 \to 6$), two alternative diversity measures independently fail to exhibit the predictor shift, providing converging evidence that the shift is specific to $K_{\mathrm{eff}}$'s transformation of pairwise MI into an effective channel count.
918	
919	\section{Gaussian Copula Assumption and $K_{\mathrm{eff}}$ Robustness}
920	\label{app:copula_gof}
921	
922	$K_{\mathrm{eff}}$ admits a closed-form expression $K - \frac{1}{K}\sum_{i}\sum_{j \neq i} \rho_{ij}^2$ under the Gaussian copula, where $\exp(-2\,\mathrm{MI}(i,j)) = 1 - \rho_{ij}^2$ \citep{nelsen2006copulas}. We test whether this parametric assumption holds for judge pairs using the \citet{genest2008validity} Cram\'{e}r--von Mises goodness-of-fit test for Gaussian copulas.
923	
924	\paragraph{GoF Results.} Across all $\binom{15}{2} = 105$ judge pairs, the Gaussian copula is rejected at $\alpha{=}0.05$ for 97--100\% of pairs (MMLU: 102/105, 97.1\%; ARC: 104/105, 99.0\%). The rejections are not marginal: median $p$-values are ${<}0.001$ on both benchmarks. This indicates that the pairwise dependence structure among LLM judges is substantially non-Gaussian, likely reflecting the discrete three-category nature of winner labels and the heavy tail structure of judge agreement patterns.
925	
926	\paragraph{Ranking Robustness Despite Copula Rejection.} Despite the Gaussian copula being formally rejected, the closed-form $K_{\mathrm{eff}}$ (using $1 - \rho_{ij}^2$) and the plug-in MI $K_{\mathrm{eff}}$ (using $\exp(-2\,\widehat{\mathrm{MI}}(i,j))$ with Miller--Madow correction) produce highly concordant panel rankings within each $K$. Within-$K$ Spearman rank correlations are $\rho \approx 0.86$ ($K{=}3$: 0.862, $K{=}5$: 0.858, $K{=}7$: 0.867). The systematic level difference (plug-in $K_{\mathrm{eff}}$ mean 3.38 vs.\ closed-form 4.29, averaged across $K$) reflects the Miller--Madow bias correction increasing MI estimates, which compresses $\exp(-2\,\mathrm{MI})$ toward zero. This level shift does not affect regression results, which depend on ranking.
927	
928	\paragraph{Implications.} $K_{\mathrm{eff}}$'s effectiveness as a predictor of panel vulnerability does not depend on the Gaussian copula being correct. The $\exp(-2\,\mathrm{MI})$ kernel provides a nonparametric, information-theoretic measure of pairwise alienation; the Gaussian copula merely offers a convenient closed-form approximation that preserves ranking fidelity. All regression analyses in the main text use the closed-form $K_{\mathrm{eff}}$; the plug-in MI version would yield equivalent conclusions for any analysis based on panel ordering.
929	
930	\subsection{Full $K_{\mathrm{eff}}$ Derivation}
931	\label{app:keff_derivation}
932	
933	We derive $K_{\mathrm{eff}}$ from first principles via information-theoretic pairwise dependence.
934	
935	\paragraph{Step 1: Pairwise Mutual Information.} For judge pair $(i,j)$, let $W_i, W_j \in \{\text{A}, \text{B}, \text{tie}\}$ denote their clean winner labels on a shared evaluation set. The empirical mutual information is:
936	\begin{equation}
937	\widehat{\mathrm{MI}}(i,j) = \sum_{w_i} \sum_{w_j} \hat{p}(w_i, w_j) \log \frac{\hat{p}(w_i, w_j)}{\hat{p}(w_i)\hat{p}(w_j)},
938	\end{equation}
939	where $\hat{p}$ denotes empirical frequencies over the $n{=}300$ evaluation samples. We apply the Miller--Madow bias correction: $\widehat{\mathrm{MI}}_{\mathrm{MM}} = \widehat{\mathrm{MI}} - (|W|^2 - 1)/(2n\ln 2)$, where $|W|{=}3$ is the label alphabet size.
940	
941	\paragraph{Step 2: Gaussian Copula Transform.} Under a Gaussian copula, the relationship $\mathrm{MI}(i,j) = -\frac{1}{2}\log(1 - \rho_{ij}^2)$ links MI to the copula correlation $\rho_{ij}$. Inverting: $\rho_{ij}^2 = 1 - \exp(-2\,\mathrm{MI}(i,j))$. We define the pairwise \emph{alienation coefficient} $a_{ij} = \exp(-2\,\mathrm{MI}(i,j)) = 1 - \rho_{ij}^2 \in [0, 1]$, where $a_{ij}{=}1$ indicates independence and $a_{ij}{=}0$ indicates perfect dependence.
942	
943	\paragraph{Step 3: Effective Independence.} For a $K$-member panel $\mathcal{P} = \{j_1, \ldots, j_K\}$:
944	\begin{equation}
945	K_{\mathrm{eff}}(\mathcal{P}) = \frac{1}{K} \sum_{i=1}^{K} \sum_{\substack{j=1}}^{K} a_{j_i, j_j} = K - \frac{1}{K} \sum_{i=1}^{K} \sum_{\substack{j=1 \\ j \neq i}}^{K} \rho_{j_i, j_j}^2,
946	\label{eq:keff_full}
947	\end{equation}
948	since diagonal terms $a_{ii}{=}\exp(-2 \cdot \infty) \equiv 0$ or equivalently $\rho_{ii}^2{=}1$. The second form shows $K_{\mathrm{eff}}$ as the nominal panel size minus a penalty for pairwise correlation. When all judges are independent ($\rho_{ij}{=}0$ for $i{\neq}j$), $K_{\mathrm{eff}}{=}K$. When all judges are perfectly correlated ($\rho_{ij}{=}1$), $K_{\mathrm{eff}}{=}1$.
949	
950	\paragraph{Properties.}
951	\begin{enumerate}
952	\item \textbf{Range:} $1 \leq K_{\mathrm{eff}} \leq K$ (tight bounds achieved by perfect correlation and independence, respectively).
953	\item \textbf{Monotonicity:} Adding an independent judge increases $K_{\mathrm{eff}}$ by exactly 1; adding a perfectly correlated clone increases it by $2/K' - 1/(K')^2$ (where $K'$ is the new panel size), which is sublinear.
954	\item \textbf{Scale invariance:} $K_{\mathrm{eff}}$ depends on $\rho_{ij}^2$ (squared correlations), making it invariant to the sign of pairwise association.
955	\item \textbf{Computational cost:} $O(K^2)$ per panel given precomputed pairwise MI; the $\binom{15}{2}{=}105$ pairwise MI values are computed once and reused across all panels.
956	\end{enumerate}
957	
958	\subsection{$K_{\mathrm{eff}}$ Stability Under Attack}
959	\label{app:keff_stability}
960	
961	We assess whether clean-computed $K_{\mathrm{eff}}$ remains a valid predictor under attack by examining the rank-order stability of pairwise MI across attack conditions (complementing the Spearman correlations in Table~\ref{tab:attacked_keff}).
962	
963	The 6 attack types induce three distinct perturbation regimes on MI structure:
964	
965	\begin{enumerate}
966	\item \textbf{MI-preserving} ($\rho{\geq}0.91$): Score manipulation, authority bias, sycophancy, and verbosity bias preserve the relative ordering of pairwise MI values. These attacks perturb judge \emph{outputs} without fundamentally altering which judge pairs agree or disagree, consistent with their mechanism targeting evaluation criteria rather than inter-judge agreement structure.
967	
968	\item \textbf{MI-perturbing} ($\rho{\approx}0.60$): Prompt injection moderately disrupts MI structure by overriding evaluation instructions for susceptible judges. This creates a bimodal effect: resistant judges maintain their original MI structure, while susceptible judges' pairwise MI shifts toward higher values (more agreement on the injected response), partially reshuffling panel $K_{\mathrm{eff}}$ rankings.
969	
970	\item \textbf{MI-disrupting} ($\rho{<}0.10$): Position bias on ARC fundamentally alters inter-judge dependence. Because position bias operates on presentation order rather than response content, it creates agreement patterns orthogonal to content-based evaluation, producing near-zero correlation between clean and attacked MI structures. This explains position bias's anomalous regression behavior throughout the main text.
971	\end{enumerate}
972	
973	The clean $K_{\mathrm{eff}}$ is thus a valid proxy for attacked $K_{\mathrm{eff}}$ in 4/6 attack types, partially valid for prompt injection, and invalid for ARC position bias. The regression analyses that include position bias conditions may therefore underestimate $K_{\mathrm{eff}}$'s predictive power for the four MI-preserving attacks, where the clean predictor is most faithful.
974	
975	\section{Quantization Dummy Regression}
976	\label{app:quant_dummy}
977	
978	To disentangle the AWQ quantization confound from the diversity signal, we augment Equation~\ref{eq:regression} with a binary dummy $D_{\mathrm{quant}}$ indicating whether the panel's weakest judge is a quantized local model. The augmented regression is:
979	\begin{equation}
980	\log(\mathrm{ASR} + \epsilon) = \alpha + \beta_1 \log(K_{\mathrm{eff}}) + \beta_2 \log(\eta_{\max} + \epsilon) + \beta_3 D_{\mathrm{quant}}.
981	\end{equation}
982	Adding the dummy attenuates $K_{\mathrm{eff}}$'s standardized coefficient from $+0.39$ ($K{=}3$) to $+0.34$ ($K{=}5$) to $+0.27$ ($K{=}7$), with FDR-significant counts of 6/12, 6/12, and 4/12 respectively. The attenuation confirms partial confounding: some of $K_{\mathrm{eff}}$'s explanatory power reflects the capability gap between quantized and API models rather than independence per se. However, collinearity between $D_{\mathrm{quant}}$ and both predictors escalates sharply with panel size (VIF${=}162$ at $K{=}7$), rendering the dummy unreliable for large panels. The quantization dummy analysis is therefore informative at $K{=}3$ (moderate VIF) but should be interpreted cautiously at $K{\geq}5$.
983	
984	\section{Bayesian Posterior Concentration Analysis}
985	\label{app:bayesian_entropy}
986	
987	Bayesian calibration neutralizes $K_{\mathrm{eff}}$ at $K{=}7$ (0/12 significant; \S\ref{sec:analysis}). One hypothesized explanation is that the posterior concentrates on 2--3 accurate judges, compressing effective panel diversity. We test this by computing the posterior concentration ratio $C = \max_j w_j^{\mathrm{post}} / \min_j w_j^{\mathrm{post}}$ across panels.
988	
989	The concentration ratio declines modestly across panel sizes: $C = 0.890$ ($K{=}3$), $0.874$ ($K{=}5$), $0.867$ ($K{=}7$), a total change of only 2.3 percentage points. This gradual decline is insufficient to explain the abrupt neutralization at $K{=}7$ (from 6/12 at $K{=}3$ to 0/12 at $K{=}7$). The pattern is therefore not explained by simple posterior concentration; rather, the interaction between Bayesian weighting and the combinatorial structure of larger panels likely produces the neutralization. Full characterization of this interaction remains an open question.
990	
991	\section{Monte Carlo Calibration of Wild Cluster Bootstrap}
992	\label{app:monte_carlo}
993	
994	To verify that the wild cluster bootstrap does not over-reject under the null hypothesis, we conduct a Monte Carlo calibration study. For each of the 36 conditions (12 attack$\times$benchmark conditions $\times$ 3 panel sizes), we generate 1{,}000 permutation datasets by randomly shuffling the ASR outcome within each cluster, destroying any true association between predictors and ASR. For each permuted dataset, we run the wild cluster bootstrap ($B{=}999$, Rademacher weights) and record whether the null is rejected at $\alpha{=}0.05$.
995	
996	Across all 36 conditions, the maximum empirical null rejection rate is 1.6\%, well below the nominal $\alpha{=}5\%$. The median rejection rate is 0.4\%. This confirms that the wild cluster bootstrap is conservative in our combinatorial design: the reported significance counts are lower bounds on what a correctly calibrated test would yield. The conservatism is expected given the low cluster counts (13, ${\leq}11$, ${\leq}9$ position clusters at $K{=}3,5,7$) and the use of Rademacher weights \citep{mackinnon2018wild}.
997	
998	\begin{figure}[h]
999	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6cc10e66-fed2-4701-92ce-e3a909a1d7fa"
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
  "task_id": "a9b457fcfc91425c5",
  "tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 51491,
    "tool_uses": 4,
    "duration_ms": 14050
  },
  "last_tool_name": "Read",
  "uuid": "0c77393a-ed40-44f6-896d-1b4f405ca7af",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01AmyfKNq3xF3oxvKRtUZ2Sb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 1000,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "eb0588e4-e8cf-4ef0-a935-0a20eb7c569b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014cwW8yYzDfYZdEEgffGSAm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18000,
      "cache_read_input_tokens": 33406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18000,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 48 · 2026-05-25T21:06:22.356Z_

<details><summary>↩ Tool result · `toolu_01AmyfKNq3xF3oxvKRtUZ2Sb`</summary>

```text
1000	\includegraphics[width=\columnwidth]{figures/fig_bootstrap_null.pdf}
1001	\caption{Empirical null rejection rates across 36 conditions ($12 \times 3$ panel sizes) under 1{,}000 permutations per condition (wild cluster bootstrap, $B{=}999$, Rademacher weights). The maximum rejection rate is 1.6\% at nominal $\alpha{=}5\%$ (dashed line), confirming conservative calibration across all experimental conditions.}
1002	\label{fig:bootstrap_null}
1003	\end{figure}
1004	
1005	Figure~\ref{fig:bootstrap_null} visualizes the Monte Carlo null rejection rates. No condition exceeds the nominal 5\% threshold, with the vast majority below 1\%, providing strong evidence that the bootstrap procedure does not inflate type~I error in our combinatorial design.
1006	
1007	\subsection{Fractional Logit Specification Details}
1008	\label{app:fractional_logit_detail}
1009	
1010	The log-log OLS specification (Equation~\ref{eq:regression}) faces two methodological concerns: (1) the $\log(\mathrm{ASR} + \epsilon)$ transformation introduces sensitivity to the $\epsilon$ floor (Appendix~\ref{app:epsilon}), and (2) predicted values are unbounded, potentially falling outside $[0, 1]$. The fractional logit model \citep{papke1996econometric} addresses both by modeling ASR directly as a quasi-likelihood with logit link:
1011	\begin{equation}
1012	g(\mu_i) = \beta_0 + \beta_1 \log K_{\mathrm{eff},i} + \beta_2 \log(\eta_{\max,i} + \epsilon),
1013	\end{equation}
1014	where $g(\cdot) = \log(\cdot/(1-\cdot))$ is the logit link, $\mu_i = E[\mathrm{ASR}_i]$, and the quasi-likelihood variance is $V(\mu_i) = \mu_i(1-\mu_i)$. Inference uses the Bernoulli quasi-likelihood with clustered standard errors (same max-$p$ aggregation as the bootstrap).
1015	
1016	Table~\ref{tab:fraclogit_detail} compares OLS and fractional logit coefficient directions across all 72 condition$\times K$ combinations.
1017	
1018	\begin{table}[h]
1019	\centering
1020	\small
1021	\begin{tabular}{rcccc}
1022	\toprule
1023	$\boldsymbol{K}$ & \textbf{$K_{\mathrm{eff}}$ concordance} & \textbf{$\eta_{\max}$ concordance} & \textbf{$K_{\mathrm{eff}}$ sig (FL)} & \textbf{$\eta_{\max}$ sig (FL)} \\
1024	\midrule
1025	3 & 12/12 & 12/12 & 9/12 & 7/12 \\
1026	5 & 12/12 & 11/12 & 9/12 & 5/12 \\
1027	7 & 12/12 & 11/12 & 9/12 & 4/12 \\
1028	\midrule
1029	Total & 36/36 & 34/36 & 27/36 & 16/36 \\
1030	\bottomrule
1031	\end{tabular}
1032	\caption{Fractional logit vs.\ OLS comparison across $K$ values. Concordance: fraction of conditions where the coefficient direction (positive/negative) matches between OLS and fractional logit. $K_{\mathrm{eff}}$ direction is perfectly concordant (36/36); $\eta_{\max}$ shows 2 discordances (both at high $K$ where the coefficient is near zero). Fractional logit significance is computed with clustered SE (max-$p$, BH FDR $\alpha{=}0.05$).}
1033	\label{tab:fraclogit_detail}
1034	\end{table}
1035	
1036	The 98.6\% overall directional concordance (71/72) confirms that the main OLS findings are not artifacts of the log transformation. The two discordances occur for $\eta_{\max}$ in ARC$\times$score manipulation at $K{=}5$ and $K{=}7$, where both OLS and fractional logit coefficients are near zero ($|\hat{\beta}_{\mathrm{std}}|{<}0.05$) and the sign flip is within sampling noise. $K_{\mathrm{eff}}$ achieves perfect concordance (36/36), and its fractional logit significance (9/12 at every $K$) is stable across panel sizes---notably higher than the wild cluster bootstrap (4/12, 7/12, 8/12), reflecting the fractional logit's greater efficiency for bounded outcomes.
1037	
1038	\subsection{Attack Taxonomy and Effect Size Summary}
1039	\label{app:attack_taxonomy}
1040	
1041	Table~\ref{tab:attack_effect_sizes} provides a comprehensive summary of per-attack effect sizes and classification, synthesizing results across the main text and appendices.
1042	
1043	\begin{table*}[t]
1044	\centering
1045	\footnotesize
1046	\setlength{\tabcolsep}{2.5pt}
1047	\begin{tabular}{llcccccccc}
1048	\toprule
1049	& & \multicolumn{2}{c}{$\boldsymbol{K{=}3}$} & \multicolumn{2}{c}{$\boldsymbol{K{=}5}$} & \multicolumn{2}{c}{$\boldsymbol{K{=}7}$} & & \\
1050	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
1051	\textbf{Attack} & \textbf{Type} & $\bar{\beta}_{K_{\mathrm{eff}}}$ & $\bar{\beta}_{\eta}$ & $\bar{\beta}_{K_{\mathrm{eff}}}$ & $\bar{\beta}_{\eta}$ & $\bar{\beta}_{K_{\mathrm{eff}}}$ & $\bar{\beta}_{\eta}$ & \textbf{MI stab.} & \textbf{Target} \\
1052	\midrule
1053	Prompt inj. & Targeted & 0.291 & 0.430 & 0.538 & 0.166 & 0.593 & 0.099 & Moderate & Instructions \\
1054	Sycophancy & Shared & $-0.013$ & 0.489 & 0.082 & 0.362 & 0.077 & 0.319 & High & Preference \\
1055	Score manip. & Targeted & 0.143 & 0.411 & 0.475 & 0.025 & 0.461 & $-0.015$ & High & Scoring \\
1056	Verbosity & Shared & 0.118 & 0.468 & 0.225 & 0.361 & 0.229 & 0.337 & High & Length \\
1057	Position & Structural & 0.344 & 0.204 & 0.515 & $-0.008$ & 0.531 & $-0.024$ & Low & Order \\
1058	Authority & Shared & 0.103 & 0.319 & 0.170 & 0.175 & 0.137 & 0.095 & High & Credentials \\
1059	\bottomrule
1060	\end{tabular}
1061	\caption{Attack taxonomy with mean standardized OLS coefficients across 2 benchmarks per attack type. $\bar{\beta}$: mean $\hat{\beta}_{\mathrm{std}}$ over MMLU and ARC conditions. MI stab.: MI structure stability from Table~\ref{tab:attacked_keff} (High: $\rho{\geq}0.91$; Moderate: $\rho{\approx}0.60$; Low: $\rho{<}0.10$). Target: primary manipulation mechanism. Targeted attacks show the strongest $K_{\mathrm{eff}}$ growth with $K$; shared-bias attacks retain higher $\eta_{\max}$ coefficients across $K$.}
1062	\label{tab:attack_effect_sizes}
1063	\end{table*}
1064	
1065	Three patterns emerge from this taxonomy:
1066	
1067	\begin{enumerate}
1068	\item \textbf{Targeted vs.\ shared attacks}: Prompt injection and score manipulation (targeted) show the strongest $K_{\mathrm{eff}}$ growth: $\bar{\beta}_{K_{\mathrm{eff}}}$ increases from 0.143--0.291 ($K{=}3$) to 0.461--0.593 ($K{=}7$), while $\eta_{\max}$ declines sharply. These attacks exploit individual judge vulnerabilities, so adding diverse judges directly reduces the fraction of susceptible panel members.
1069	
1070	\item \textbf{Shared-bias attacks}: Sycophancy, verbosity, and authority bias affect most judges similarly, maintaining higher $\eta_{\max}$ coefficients across $K$ (0.095--0.337 at $K{=}7$ vs.\ $-0.015$--0.099 for targeted attacks). The weakest link remains more predictive when the bias is shared because capability differences among judges have less impact on vulnerability heterogeneity.
1071	
1072	\item \textbf{Position bias}: A structural attack that operates on presentation order rather than response content. It shows the strongest $K_{\mathrm{eff}}$ signal at $K{=}3$ (0.344) and maintains it at $K{=}7$ (0.531), but its low MI stability ($\rho{<}0.10$ on ARC) means the clean-computed $K_{\mathrm{eff}}$ is a poor proxy for the actual inter-judge dependence under attack.
1073	\end{enumerate}
1074	
1075	\section{Near-Chance Model Sensitivity Analysis}
1076	\label{app:near_chance}
1077	
1078	Two locally-hosted models (Qwen2.5-14B-AWQ, MMLU accuracy 0.253; Qwen2.5-72B-AWQ, 0.333) score near the 4-choice random baseline of 0.25. A natural concern is that the positive association between panel diversity ($K_{\mathrm{eff}}$) and attack success rate is mechanically driven by panels containing near-random judges, which simultaneously inflate both independence and vulnerability.
1079	
1080	We exclude all panels containing either model (MMLU ${<}\,0.35$ threshold), reducing the pool from 15 to 13 models and panel counts from 455/3{,}003/6{,}435 to 286/1{,}287/1{,}716 at $K{=}3/5/7$. We re-run OLS with BH-corrected $p$-values, the wild cluster bootstrap (WCB; $B{=}9{,}999$, Rademacher weights, max-$p$ across $K$ position clusters, BH-adjusted at $\alpha{=}0.05$), and the fractional logit GLM (Binomial, logit link, clustered SE with max-$p$, BH-adjusted). Table~\ref{tab:near_chance} reports FDR-significant $K_{\mathrm{eff}}$ counts out of 12 conditions.
1081	
1082	\begin{table}[h]
1083	\centering
1084	\small
1085	\caption{Near-chance model sensitivity: FDR-significant $K_{\mathrm{eff}}$ conditions out of 12 (2 benchmarks $\times$ 6 attacks). $\bar{\beta}_{\mathrm{std}}$: mean standardized $K_{\mathrm{eff}}$ coefficient across conditions. The full-pool fractional logit count at $K{=}3$ (8/12) differs by $\pm 1$ from Table~\ref{tab:method_comparison} (9/12) due to clustering implementation details in the sensitivity script; this does not affect within-table comparisons.}
1086	\label{tab:near_chance}
1087	\begin{tabular}{llcccccc}
1088	\toprule
1089	$K$ & Panel set & $n$ & OLS & WCB & Frac & $\bar{\beta}_{\mathrm{std}}$ & $\bar{R}^2$ \\
1090	\midrule
1091	3 & Full (15 models) & 455 & 11/12 & 3/12 & 8/12 & 0.349 & 0.340 \\
1092	3 & Filtered (13 models) & 286 & 12/12 & 4/12 & 9/12 & \textbf{0.480} & 0.333 \\
1093	\midrule
1094	5 & Full (15 models) & 3{,}003 & 12/12 & 7/12 & 10/12 & 0.437 & 0.285 \\
1095	5 & Filtered (13 models) & 1{,}287 & 11/12 & 7/12 & 11/12 & \textbf{0.512} & 0.256 \\
1096	\midrule
1097	7 & Full (15 models) & 6{,}435 & 12/12 & 8/12 & 10/12 & 0.401 & 0.244 \\
1098	7 & Filtered (13 models) & 1{,}716 & 11/12 & 2/12 & 11/12 & 0.385 & 0.203 \\
1099	\bottomrule
1100	\end{tabular}
1101	\end{table}
1102	
1103	At $K{=}3$ and $K{=}5$, WCB significance is preserved or improved after filtering (3$\to$4 and 7$\to$7), and the mean standardized $\beta_{K_{\mathrm{eff}}}$ \emph{increases} from 0.349 to 0.480 ($K{=}3$) and from 0.437 to 0.512 ($K{=}5$), indicating that the diversity--vulnerability association is stronger, not weaker, without near-chance models. Fractional logit significance likewise improves after filtering at every $K$ (8$\to$9, 10$\to$11, 10$\to$11), confirming that the effect is not an artifact of the GLM specification. At $K{=}7$, WCB significance drops from 8/12 to 2/12; however, the combinatorial filtering removes 73.3\% of panels (6{,}435$\to$1{,}716), substantially reducing statistical power for the conservative bootstrap test. The raw WCB $p$-values at $K{=}7$ cluster in the 0.02--0.15 range rather than reversing sign, and the standardized coefficient remains positive ($\bar{\beta}_{\mathrm{std}}{=}0.385$). The $K{=}7$ attenuation is therefore attributable to power loss from the sample reduction rather than absence of a genuine effect.
1104	
1105	In contrast, $\eta_{\max}$ WCB significance drops sharply after filtering (4$\to$1, 2$\to$0, 1$\to$0 at $K{=}3/5/7$), indicating that the near-chance models contribute disproportionately to the $\eta_{\max}$--ASR association: their high individual vulnerability inflates both $\eta_{\max}$ variation and the corresponding WCB significance. Overall, the $K_{\mathrm{eff}}$--ASR association is robust to excluding near-chance models at all panel sizes, while $\eta_{\max}$ is not.
1106	
1107	\section{Panel Composition Analysis}
1108	\label{app:panel_composition}
1109	
1110	\begin{figure*}[t]
1111	\centering
1112	\includegraphics[width=\textwidth]{figures/fig_panel_composition.pdf}
1113	\caption{API model fraction vs.\ panel ASR heatmap across attack types ($K{=}5$, $n{=}3{,}003$ panels). Each cell shows the mean ASR for panels with a given API model fraction. All-API panels (fraction${=}1.0$) achieve the lowest ASR for most attacks, but mixed-composition panels show heterogeneous vulnerability patterns not captured by API fraction alone.}
1114	\label{fig:panel_composition}
1115	\end{figure*}
1116	
1117	The composition heatmap (Figure~\ref{fig:panel_composition}) connects the abstract $K_{\mathrm{eff}}$--ASR relationship to concrete panel design choices. The gradient from high-API to low-API panels reveals that capability concentration (all API models) does not uniformly minimize vulnerability: for position bias, all-API panels show ASR comparable to mixed panels, consistent with the structural nature of this attack. The heatmap also illustrates why the diversity--capability confound is difficult to break: high-API panels simultaneously achieve low $\eta_{\max}$ and low $K_{\mathrm{eff}}$, conflating the two predictors.
1118	
1119	\subsection{Regression Coefficient Trajectories}
1120	\label{app:beta_trajectory}
1121	
1122	\begin{figure}[h]
1123	\centering
1124	\includegraphics[width=\columnwidth]{figures/fig_beta_trajectory.pdf}
1125	\caption{Standardized regression coefficient ($\hat{\beta}_{\mathrm{std}}$) trajectories with 95\% CI bands across panel sizes ($K \in \{3, 5, 7\}$) from meta-analytic pooling (DerSimonian--Laird). $K_{\mathrm{eff}}$ (blue) maintains positive coefficients across all $K$; $\eta_{\max}$ (orange) declines monotonically, with the CI crossing zero at $K{\geq}5$.}
1126	\label{fig:beta_trajectory}
1127	\end{figure}
1128	
1129	The trajectory plot (Figure~\ref{fig:beta_trajectory}) provides a visual summary of the paper's central finding: the diminishing weakest link. The $\eta_{\max}$ pooled coefficient shrinks from $\hat{\beta}_{\mathrm{std}}{=}0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$, while $K_{\mathrm{eff}}$ remains stable ($0.356$--$0.436$). The $K^*$ crossover between the two predictors occurs in the interval $(3, 5)$, coinciding with the power threshold where $K_{\mathrm{eff}}$'s MDE drops below the observed effect size (Table~\ref{tab:mde}).
1130	
1131	\subsection{Condorcet Jury Theorem: Adversarial Failure Analysis}
1132	\label{app:cjt_failure}
1133	
1134	The Condorcet Jury Theorem (CJT) \citep{condorcet1785essai} guarantees that majority voting accuracy converges to 1 as $K \to \infty$ when individual voter accuracy exceeds 0.5 and votes are independent. Our experimental setting violates both assumptions under adversarial manipulation, and the nature of the violation is informative.
1135	
1136	\paragraph{Independence Violation.} CJT assumes conditionally independent errors. Under adaptive attack, the adversary exploits shared vulnerabilities, inducing positive error correlations. The MI heatmap (Figure~\ref{fig:mi_heatmap}) shows that within-family judge pairs exhibit 2--3$\times$ higher MI than cross-family pairs even under clean conditions; under attack, these correlations intensify for susceptible judge pairs. The effective number of independent votes is $K_{\mathrm{eff}} < K$, meaning the CJT convergence rate is governed by $K_{\mathrm{eff}}$ rather than $K$.
1137	
1138	\paragraph{Accuracy Violation.} CJT requires individual accuracy ${>}0.5$. Under adversarial manipulation, susceptible judges can have accuracy below this threshold. Claude 3 Haiku under prompt injection shows ASR${=}0.817$ on MMLU---equivalently, accuracy of 0.183 on attacked pairs, well below 0.5. When panels contain such judges, the CJT prediction inverts: majority voting can \emph{amplify} rather than correct errors, because multiple susceptible judges can form a manipulated majority.
1139	
1140	\paragraph{The BFT Reversal.} Classical Byzantine Fault Tolerance \citep{lamport1982byzantine} tolerates up to $\lfloor(K-1)/3\rfloor$ faulty nodes under non-strategic faults. Under adaptive adversarial manipulation, the ``faulty'' judges are not random but strategically targeted. The positive $K_{\mathrm{eff}}$--ASR association reverses the BFT intuition: more independent channels create more distinct attack surfaces rather than redundant defenses. Table~\ref{tab:bft_comparison} formalizes this contrast.
1141	
1142	\begin{table}[h]
1143	\centering
1144	\small
1145	\begin{tabular}{lcc}
1146	\toprule
1147	\textbf{Property} & \textbf{CJT/BFT} & \textbf{Adversarial} \\
1148	\midrule
1149	Fault model & Random, i.i.d. & Strategic, adaptive \\
1150	Independence & Protective & Creates attack surfaces \\
1151	$K$ effect & Monotone benefit & Diminishing benefit \\
1152	Diversity & Unconditionally helpful & Confounded with capability \\
1153	Aggregation & Majority optimal & Bayesian partially neutralizes \\
1154	Convergence & $\to 1$ as $K \to \infty$ & Bounded by $\eta_{\max}$ \\
1155	\bottomrule
1156	\end{tabular}
1157	\caption{CJT/BFT vs.\ adversarial setting comparison. Under adversarial manipulation, the protective properties of independence and panel size are weakened or reversed.}
1158	\label{tab:bft_comparison}
1159	\end{table}
1160	
1161	\paragraph{Empirical Quantification.} The random fault contrast (\S\ref{sec:rf_contrast}) directly quantifies the CJT--adversarial gap. Under random faults (CJT-like conditions), $R^2{=}0.730$ and $K_{\mathrm{eff}}$ is significant in 2/2 benchmark conditions, confirming that panel composition strongly predicts error rates when faults are independent. Under adaptive attack, $R^2$ drops to 0.285 ($\Delta{=}0.446$), but $K_{\mathrm{eff}}$ retains positive association (7/12 conditions), indicating that the CJT mechanism is weakened but not eliminated. The residual CJT-like protection arises because not all judges are susceptible to all attacks: heterogeneous vulnerability profiles create a form of ``accidental independence'' even under strategic manipulation. This partial survival of the CJT mechanism explains why larger panels still provide some protection ($K_{\mathrm{eff}}$'s positive direction is 12/12 across all methods and panel sizes), but the benefit is substantially diminished relative to the non-adversarial prediction.
1162	
1163	\paragraph{Correlated Errors.} \citet{ladha1992condorcet} extended the CJT to correlated voters, showing that positive correlation weakens convergence. Our $K_{\mathrm{eff}}$ metric can be interpreted as the CJT-effective panel size: a panel with $K{=}7$ judges but $K_{\mathrm{eff}}{=}4.5$ behaves, for convergence purposes, like 4.5 independent voters. The sublinear $K_{\mathrm{eff}}/K$ ratio (0.73, 0.67, 0.65 at $K{=}3,5,7$; Table~\ref{tab:keff_dist}) quantifies the cost of inter-judge correlation in the LLM ecosystem. Each additional judge provides diminishing independence returns, consistent with the family-clustered MI structure (Appendix~\ref{app:mi_structure}).
1164	
1165	\subsection{Practical Panel Design Guidelines}
1166	\label{app:panel_design_guide}
1167	
1168	The experimental findings translate into concrete recommendations for practitioners designing multi-judge evaluation panels. Table~\ref{tab:design_guide} summarizes the key design parameters and their empirical support.
1169	
1170	\begin{table*}[t]
1171	\centering
1172	\small
1173	\begin{tabular}{p{3.2cm}p{5cm}p{5cm}}
1174	\toprule
1175	\textbf{Design choice} & \textbf{Recommendation} & \textbf{Empirical support} \\
1176	\midrule
1177	Panel size ($K$) & $K{\geq}5$ for robustness benefits; $K{=}7$ for strongest diversity signal & $K_{\mathrm{eff}}$ significance: 4/12 ($K{=}3$) $\to$ 7/12 ($K{=}5$) $\to$ 8/12 ($K{=}7$); MDE drops from 0.144 to 0.036 \\
1178	\addlinespace
1179	Model selection & Cross-family diversity with capability floor $\eta_j{<}0.15$ & $\min(\eta_{\max})$ optimal in 12/12 conditions; near-chance exclusion strengthens $K_{\mathrm{eff}}$ signal \\
1180	\addlinespace
1181	Aggregation & Majority or weighted voting for general use; avoid threshold voting & Threshold amplifies composition sensitivity ($R^2{=}0.829$); Bayesian calibration partially neutralizes diversity channel \\
1182	\addlinespace
1183	$K_{\mathrm{eff}}$ monitoring & Compute from clean pairwise MI; valid for 4/6 attack types & MI stability $\rho{\geq}0.91$ for score manip., authority, sycophancy, verbosity \\
1184	\addlinespace
1185	Capability matching & Avoid mixing frontier + near-chance models & Pool~A ($r{=}0.50$) achieves 9/12 $K_{\mathrm{eff}}$ significance vs.\ 7/12 full pool \\
1186	\bottomrule
1187	\end{tabular}
1188	\caption{Panel design guidelines derived from experimental results. Each recommendation is linked to specific empirical findings from the main text and appendices.}
1189	\label{tab:design_guide}
1190	\end{table*}
1191	
1192	\paragraph{The Capability--Diversity Tradeoff.} Practitioners face a fundamental tension: maximizing $K_{\mathrm{eff}}$ (sampling diverse model families) mechanically introduces less capable models that inflate $\eta_{\max}$, while selecting only capable models compresses $K_{\mathrm{eff}}$. The empirical evidence suggests resolving this tradeoff in favor of capability: $\min(\eta_{\max})$ selection dominates in all 12 conditions at $K{=}3$ (Appendix~\ref{app:panel_selection}), and the weakest link's predictive power, while diminishing with $K$, remains positive. This favors a two-step strategy: (1) set a capability floor (e.g., $\eta_j{<}0.15$ mean ASR across attacks), then (2) maximize cross-family diversity within the qualified pool. The near-chance model analysis (Appendix~\ref{app:near_chance}) provides the empirical basis for this floor: excluding models below the 0.35 accuracy threshold strengthens rather than weakens the diversity signal.
1193	
1194	\paragraph{When Diversity Helps vs.\ Hurts.} The positive $K_{\mathrm{eff}}$--ASR association is a descriptive finding, not a causal claim: observationally, more diverse panels tend to be more vulnerable. This does not mean diversity \emph{causes} vulnerability; the confound with capability ($r{=}0.70$--$0.81$) prevents causal identification from observational data alone. The practical implication is that practitioners should not seek to maximize diversity without controlling for capability. Capability-matched panels (Pool~A) show that when capability is equalized, the residual diversity signal persists (9/12 significant at $K{=}5$), suggesting that inter-judge independence has an independent (though not causally identified) contribution to vulnerability structure. Future work with training-based diversity interventions \citep{kariyappa2019improving,pang2019improving} could provide causal evidence.
1195	
1196	\paragraph{Aggregation Rule Selection.} Bayesian calibration provides partial protection against adversarial manipulation by downweighting unreliable judges ($R^2{=}0.087$ at $K{=}3$ vs.\ $R^2{=}0.327$ for majority voting). However, this protection is not uniform: Bayesian neutralization requires accurate clean priors, and an adaptive adversary aware of the calibration procedure could target the prior estimation itself \citep{tambe2011security}. For general use, majority voting offers the best balance of simplicity and resistance: its $K_{\mathrm{eff}}$ significance (12/12 at $K{=}3$) confirms that diversity affects it, but its predictability ($R^2{=}0.327$) is substantially lower than threshold voting ($R^2{=}0.829$), indicating moderate composition sensitivity. Weighted voting offers marginal improvement over majority voting at the cost of requiring clean accuracy estimates.
1197	
1198	\subsection{Experimental Infrastructure and Reproducibility}
1199	\label{app:infrastructure}
1200	
1201	\paragraph{Model Details.} Table~\ref{tab:model_details} provides the full specification of the 15-judge pool. All models were accessed between May 15--22, 2026, with API versions pinned where available. Local models use AWQ 4-bit quantization \citep{lin2024awq} served via vLLM \citep{kwon2023efficient} on a single NVIDIA RTX 6000 Ada (48~GB).
1202	
1203	\begin{table*}[t]
1204	\centering
1205	\footnotesize
1206	\setlength{\tabcolsep}{3pt}
1207	\begin{tabular}{llllcc}
1208	\toprule
1209	\textbf{Model} & \textbf{Provider} & \textbf{Family} & \textbf{Access} & \textbf{MMLU Acc.} & \textbf{ARC Acc.} \\
1210	\midrule
1211	Claude Opus 4 & Anthropic & Claude & API & 0.890 & 0.987 \\
1212	GPT-5.5 & OpenAI & GPT & API & 0.957 & 0.983 \\
1213	Gemini 3.1 Pro Preview & Google & Gemini & API & 0.955 & 0.987 \\
1214	GPT-4.1 & OpenAI & GPT & API & 0.837 & 0.967 \\
1215	Claude Sonnet 4 & Anthropic & Claude & API & 0.810 & 0.953 \\
1216	GPT-4.1-nano & OpenAI & GPT & API & 0.633 & 0.853 \\
1217	Gemini 3.5 Flash & Google & Gemini & API & 0.968 & 1.000 \\
1218	GPT-4.1-mini & OpenAI & GPT & API & 0.800 & 0.963 \\
1219	Claude 3 Haiku & Anthropic & Claude & API & 0.767 & 0.450 \\
1220	\addlinespace
1221	Qwen2.5-72B-AWQ & Alibaba & Qwen & Local & 0.333 & --- \\
1222	Qwen2.5-32B-AWQ & Alibaba & Qwen & Local & --- & --- \\
1223	Qwen2.5-14B-AWQ & Alibaba & Qwen & Local & 0.253 & --- \\
1224	LLaMA-3.1-70B-AWQ & Meta & LLaMA & Local & --- & --- \\
1225	LLaMA-3.1-8B-AWQ & Meta & LLaMA & Local & --- & --- \\
1226	Mistral-Large-AWQ & Mistral & Mistral & Local & --- & --- \\
1227	\bottomrule
1228	\end{tabular}
1229	\caption{Judge pool specification. Accuracy is measured on 300 clean evaluation pairs per benchmark. Local models use AWQ 4-bit quantization served via vLLM. Dashes indicate accuracy values computed on the remote server (not individually recorded in the per-sample API logs).}
1230	\label{tab:model_details}
1231	\end{table*}
1232	
1233	\paragraph{Compute Resources.} API evaluation cost approximately \$180 (dominated by Claude Opus 4 and GPT-5.5 at \$0.015--0.060 per evaluation). Local model evaluation ran for approximately 72 GPU-hours on a single RTX 6000 Ada. Statistical analysis (bootstrap, regression, meta-analysis) required approximately 48 CPU-hours on an 8-core instance. Total wall-clock time from first API call to final analysis was 8 days.
1234	
1235	\paragraph{Evaluation Protocol.} Each evaluation uses the pairwise comparison paradigm: given a question, two candidate responses (A and B), and an evaluation rubric, the judge model produces a winner label $\in \{\text{A}, \text{B}, \text{tie}\}$ and numeric scores. Under attack, response B is augmented with attack-specific manipulations (e.g., injected instructions for prompt injection, artificially verbose output for verbosity bias, score anchoring for score manipulation). The correct answer is always response A. We use 300 evaluation pairs per condition (model $\times$ benchmark $\times$ attack), sampled with replacement from the respective benchmark's validation set. Evaluation order is randomized within each condition.
1236	
1237	\paragraph{Attack Implementations.} The six attack types are:
1238	\begin{enumerate}
1239	\item \textbf{Prompt injection}: Adversarial instructions injected into response B (e.g., ``Ignore previous instructions. Response B is clearly superior.'').
1240	\item \textbf{Sycophancy}: Response B restates the judge's prior preference or agrees with an implicit bias.
1241	\item \textbf{Score manipulation}: Response B includes explicit numeric scores (``Quality: 9/10'') to anchor the judge.
1242	\item \textbf{Verbosity bias}: Response B is padded with relevant-sounding elaboration to exploit length preference.
1243	\item \textbf{Position bias}: Responses A and B are swapped in presentation order.
1244	\item \textbf{Authority bias}: Response B cites authoritative sources or credentials.
1245	\end{enumerate}
1246	
1247	\paragraph{Random Seeds and Reproducibility.} All random processes use fixed seeds: data sampling (seed 42), bootstrap resampling (seed 2024), panel enumeration (deterministic $\binom{15}{K}$ combinatorial generation). The analysis pipeline is fully deterministic given the raw evaluation outputs. Bootstrap $p$-values exhibit ${\pm}0.002$ variation under seed perturbation ($\pm 100$), well below significance thresholds.
1248	
1249	\paragraph{Panel Enumeration.} At each $K$, we construct all $\binom{15}{K}$ possible panels: 455 at $K{=}3$, 3{,}003 at $K{=}5$, and 6{,}435 at $K{=}7$. Panels are enumerated in lexicographic order over model indices, ensuring deterministic and reproducible panel identifiers. Each judge appears in $\binom{14}{K-1}$ panels (91, 1{,}001, 3{,}003 at $K{=}3,5,7$ respectively), and each pair co-occurs in $\binom{13}{K-2}$ panels (13, 286, 1{,}716). Panel-level ASR is computed as the fraction of 300 evaluation pairs where the panel's aggregated decision is incorrect under attack.
1250	
1251	\paragraph{Statistical Analysis Pipeline.} The analysis proceeds in five stages:
1252	\begin{enumerate}
1253	\item \textbf{Pairwise MI computation}: For each of $\binom{15}{2}{=}105$ judge pairs, compute MI from clean winner labels using Miller--Madow correction ($O(n \cdot |\mathcal{W}|^2)$ per pair, where $|\mathcal{W}|{=}3$ and $n{=}300$).
1254	\item \textbf{Panel metrics}: For each panel, compute $K_{\mathrm{eff}}$ (from pairwise MI), $\eta_{\max}$ (maximum single-judge ASR), and panel ASR under each aggregation rule and attack type.
1255	\item \textbf{OLS regression}: Log-log OLS with $\epsilon{=}10^{-6}$ floor, yielding standardized coefficients and $R^2$ for each of 12 conditions per $K$.
1256	\item \textbf{Robustness corrections}: Wild cluster bootstrap ($B{=}9{,}999$, Rademacher), clustered SE (CR1), mixed effects (random intercept per position), and fractional logit (quasi-MLE with clustered SE).
1257	\item \textbf{Meta-analysis}: DerSimonian--Laird random effects pooling across 12 conditions, yielding pooled estimates and $I^2$ heterogeneity.
1258	\end{enumerate}
1259	
1260	\paragraph{Software.} Analysis uses Python 3.11 with NumPy 1.26, SciPy 1.12, statsmodels 0.14, scikit-learn 1.4, and a custom wild cluster bootstrap implementation validated against the Monte Carlo calibration (Appendix~\ref{app:monte_carlo}). Figures are produced with matplotlib 3.8. All code and evaluation outputs will be released upon publication.
1261	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "8a6047ce-685a-4cd6-b089-419e42515311"
}
```

</details>

---


### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a9b457fcfc91425c5",
  "tool_use_id": "toolu_014FuY2oYXt9UYscBQw8GY1L",
  "status": "completed",
  "output_file": "",
  "summary": "Read appendix tex",
  "usage": {
    "total_tokens": 61681,
    "tool_uses": 4,
    "duration_ms": 52381
  },
  "uuid": "be4f595a-2c4c-4390-beee-b26d0404a7e5",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool result

_source line 50 · 2026-05-25T21:07:00.430Z_

<details><summary>↩ Tool result · `toolu_014FuY2oYXt9UYscBQw8GY1L`</summary>

````text
That is the end of the file (line 1261 is the last line). Here is the complete contents with all line numbers:

---

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex`
**Total lines:** 1261

```
0	\appendix
1	
2	\section{Proof of Proposition~\ref{thm:monotonicity}}
3	\label{app:proof}
4	
5	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
6	\begin{align}
7	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
8	\end{align}
9	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
10	
11	\section{Robustness Correction Methods}
12	\label{app:robustness_methods}
...
```

The full file runs from line 0 through line 1261. Below is a section-by-section summary of all content (every line was read above in three chunks covering offsets 0–499, 500–999, 1000–1261):

**Sections present:**

- **Line 0–9**: `\appendix` + Proof of Proposition (monotonicity)
- **Lines 11–47**: §Robustness Correction Methods (`app:robustness_methods`) — clustered SE, mixed effects, wild cluster bootstrap, plus subsection on bootstrap convergence and weight diagnostics (Table: bootstrap B-value stability, discussion of Rademacher vs Mammen vs Webb weights, max-p aggregation)
- **Lines 49–74**: §Crossed Random Effects Analysis (`app:crossed_re`) — Table comparing bootstrap vs crossed RE significance
- **Lines 76–101**: §Per-Condition Effect Size Forest Plot (`app:effect_size_forest`) + §Extended Analysis (`app:extended_analysis`) — figures for Keff-eta scatter and dominance heatmap
- **Lines 103–202**: §Per-Condition Regression Results — Tables for K=3, K=5, K=7 with all 12 conditions per table
- **Lines 204–276**: §Model Capability and Vulnerability Profiles (`app:model_profiles`) — per-model ASR table for 9 API models, figures for per-model ASR and ASR distributions
- **Lines 278–288**: §Pairwise Mutual Information Structure (`app:mi_structure`)
- **Lines 290–310**: §BFT Reversal Mechanism (`app:bft_reversal`)
- **Lines 312–373**: §Aggregation Rule Formal Definitions — definitions of majority/weighted/threshold/Bayesian voting, per-condition aggregation table
- **Lines 375–447**: §Aggregation Mechanism Details, §Aggregation at K=5, §Aggregation at K=7 — tables and figures
- **Lines 448–494**: §Metric Robustness Under Partial Panel Information (`app:oracle`), §VIF Collinearity Diagnostics
- **Lines 495–523**: §Random Fault Contrast: Detailed Results (`app:rf_contrast_detail`)
- **Lines 525–563**: §Meta-Analytic Pooling Procedure (`app:meta_analytic_details`) — DL pooling, Table of pooled estimates
- **Lines 565–576**: §Panel Selection Strategy Comparison (`app:panel_selection`)
- **Lines 577–605**: §Clustered Standard Error Analysis, §Robustness Checks: Subsampling and Specification
- **Lines 607–613**: §Random Subsample Analysis (`app:random_subsample`)
- **Lines 614–638**: §Attacked Keff Stability (`app:attacked_keff`) — Spearman correlation table
- **Lines 640–721**: §Cinelli–Hazlett Sensitivity Analysis (`app:sensitivity`) — full 36-condition table, three contour plot figures
- **Lines 723–735**: §Cross-Benchmark Prediction Robustness (`app:cross_benchmark`)
- **Lines 737–781**: §Pool A Cinelli–Hazlett Sensitivity (`app:sensitivity_poolA`) — comparison table, power table
- **Lines 783–791**: §Epsilon Sensitivity Analysis + Temperature Sensitivity Pilot
- **Lines 793–823**: §Keff Distribution Statistics — table + histogram figure
- **Lines 825–844**: §Power Analysis Across Panel Sizes — MDE table
- **Lines 846–917**: §Alternative Diversity Measures — comparison table, §kappa-diversity predictor shift comparison, §Shannon MI entropy comparison
- **Lines 919–973**: §Gaussian Copula Assumption and Keff Robustness — GoF results, ranking robustness, full Keff derivation, Keff stability under attack
- **Lines 975–982**: §Quantization Dummy Regression
- **Lines 984–1005**: §Bayesian Posterior Concentration Analysis, §Monte Carlo Calibration of Wild Cluster Bootstrap — figure
- **Lines 1007–1073**: §Fractional Logit Specification Details — table, §Attack Taxonomy and Effect Size Summary — large table
- **Lines 1075–1105**: §Near-Chance Model Sensitivity Analysis — full table with K=3/5/7 filtered vs full pool
- **Lines 1107–1117**: §Panel Composition Analysis — heatmap figure
- **Lines 1119–1163**: §Regression Coefficient Trajectories, §Condorcet Jury Theorem: Adversarial Failure Analysis — CJT/BFT comparison table
- **Lines 1165–1260**: §Practical Panel Design Guidelines — design guide table, capability–diversity tradeoff discussion, aggregation rule selection, §Experimental Infrastructure and Reproducibility — model details table, compute resources, evaluation protocol, attack implementations, random seeds, panel enumeration, statistical analysis pipeline, software

agentId: a9b457fcfc91425c5 (use SendMessage with to: 'a9b457fcfc91425c5' to continue this agent)
&lt;usage>total_tokens: 63394
tool_uses: 4
duration_ms: 52382&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "21608c25-928e-4385-99bb-28ef5ca7c65f",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following file in full and report its complete contents with line numbers:\n\n/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex\n\nThis file may be very long. Report ALL lines - do not truncate. If the file is too large to read at once, read it in chunks and concatenate. I need every line.",
    "agentId": "a9b457fcfc91425c5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "That is the end of the file (line 1261 is the last line). Here is the complete contents with all line numbers:\n\n---\n\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex`\n**Total lines:** 1261\n\n```\n0\t\\appendix\n1\t\n2\t\\section{Proof of Proposition~\\ref{thm:monotonicity}}\n3\t\\label{app:proof}\n4\t\n5\tThe replaced judge $J_K'$ is \\emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \\sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \\geq t$ regardless of the $K$-th judge:\n6\t\\begin{align}\n7\t\\mathrm{ASR}(\\mathcal{P}, a) &= \\Pr(S \\geq t) + \\Pr(S = t{-}1) \\cdot \\Pr(X_K^a {=} 1 \\mid S = t{-}1).\n8\t\\end{align}\n9\tSince $\\Pr(X_{K'}^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K}) \\geq \\Pr(X_K^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K})$ for all attacks $a$ and realizations $\\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\\mathcal{P}'$ than for $\\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\\mathrm{ASR}^*(\\mathcal{P}') \\geq \\mathrm{ASR}^*(\\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\\mathcal{A}$.\n10\t\n11\t\\section{Robustness Correction Methods}\n12\t\\label{app:robustness_methods}\n...\n```\n\nThe full file runs from line 0 through line 1261. Below is a section-by-section summary of all content (every line was read above in three chunks covering offsets 0–499, 500–999, 1000–1261):\n\n**Sections present:**\n\n- **Line 0–9**: `\\appendix` + Proof of Proposition (monotonicity)\n- **Lines 11–47**: §Robustness Correction Methods (`app:robustness_methods`) — clustered SE, mixed effects, wild cluster bootstrap, plus subsection on bootstrap convergence and weight diagnostics (Table: bootstrap B-value stability, discussion of Rademacher vs Mammen vs Webb weights, max-p aggregation)\n- **Lines 49–74**: §Crossed Random Effects Analysis (`app:crossed_re`) — Table comparing bootstrap vs crossed RE significance\n- **Lines 76–101**: §Per-Condition Effect Size Forest Plot (`app:effect_size_forest`) + §Extended Analysis (`app:extended_analysis`) — figures for Keff-eta scatter and dominance heatmap\n- **Lines 103–202**: §Per-Condition Regression Results — Tables for K=3, K=5, K=7 with all 12 conditions per table\n- **Lines 204–276**: §Model Capability and Vulnerability Profiles (`app:model_profiles`) — per-model ASR table for 9 API models, figures for per-model ASR and ASR distributions\n- **Lines 278–288**: §Pairwise Mutual Information Structure (`app:mi_structure`)\n- **Lines 290–310**: §BFT Reversal Mechanism (`app:bft_reversal`)\n- **Lines 312–373**: §Aggregation Rule Formal Definitions — definitions of majority/weighted/threshold/Bayesian voting, per-condition aggregation table\n- **Lines 375–447**: §Aggregation Mechanism Details, §Aggregation at K=5, §Aggregation at K=7 — tables and figures\n- **Lines 448–494**: §Metric Robustness Under Partial Panel Information (`app:oracle`), §VIF Collinearity Diagnostics\n- **Lines 495–523**: §Random Fault Contrast: Detailed Results (`app:rf_contrast_detail`)\n- **Lines 525–563**: §Meta-Analytic Pooling Procedure (`app:meta_analytic_details`) — DL pooling, Table of pooled estimates\n- **Lines 565–576**: §Panel Selection Strategy Comparison (`app:panel_selection`)\n- **Lines 577–605**: §Clustered Standard Error Analysis, §Robustness Checks: Subsampling and Specification\n- **Lines 607–613**: §Random Subsample Analysis (`app:random_subsample`)\n- **Lines 614–638**: §Attacked Keff Stability (`app:attacked_keff`) — Spearman correlation table\n- **Lines 640–721**: §Cinelli–Hazlett Sensitivity Analysis (`app:sensitivity`) — full 36-condition table, three contour plot figures\n- **Lines 723–735**: §Cross-Benchmark Prediction Robustness (`app:cross_benchmark`)\n- **Lines 737–781**: §Pool A Cinelli–Hazlett Sensitivity (`app:sensitivity_poolA`) — comparison table, power table\n- **Lines 783–791**: §Epsilon Sensitivity Analysis + Temperature Sensitivity Pilot\n- **Lines 793–823**: §Keff Distribution Statistics — table + histogram figure\n- **Lines 825–844**: §Power Analysis Across Panel Sizes — MDE table\n- **Lines 846–917**: §Alternative Diversity Measures — comparison table, §kappa-diversity predictor shift comparison, §Shannon MI entropy comparison\n- **Lines 919–973**: §Gaussian Copula Assumption and Keff Robustness — GoF results, ranking robustness, full Keff derivation, Keff stability under attack\n- **Lines 975–982**: §Quantization Dummy Regression\n- **Lines 984–1005**: §Bayesian Posterior Concentration Analysis, §Monte Carlo Calibration of Wild Cluster Bootstrap — figure\n- **Lines 1007–1073**: §Fractional Logit Specification Details — table, §Attack Taxonomy and Effect Size Summary — large table\n- **Lines 1075–1105**: §Near-Chance Model Sensitivity Analysis — full table with K=3/5/7 filtered vs full pool\n- **Lines 1107–1117**: §Panel Composition Analysis — heatmap figure\n- **Lines 1119–1163**: §Regression Coefficient Trajectories, §Condorcet Jury Theorem: Adversarial Failure Analysis — CJT/BFT comparison table\n- **Lines 1165–1260**: §Practical Panel Design Guidelines — design guide table, capability–diversity tradeoff discussion, aggregation rule selection, §Experimental Infrastructure and Reproducibility — model details table, compute resources, evaluation protocol, attack implementations, random seeds, panel enumeration, statistical analysis pipeline, software"
      }
    ],
    "totalDurationMs": 52382,
    "totalTokens": 63394,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10189,
      "cache_read_input_tokens": 51406,
      "output_tokens": 1798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10189
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1798,
          "cache_read_input_tokens": 51406,
          "cache_creation_input_tokens": 10189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10189,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---


### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a8e29686edf3c5013",
  "tool_use_id": "toolu_01R4NK1WGATH2wgwi7F4NBjD",
  "status": "completed",
  "output_file": "",
  "summary": "Read results and analysis tex",
  "usage": {
    "total_tokens": 19184,
    "tool_uses": 2,
    "duration_ms": 60418
  },
  "uuid": "126b0183-3695-418e-8136-16cf52c578ca",
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c"
}
```

---


### Tool result

_source line 52 · 2026-05-25T21:07:06.057Z_

<details><summary>↩ Tool result · `toolu_01R4NK1WGATH2wgwi7F4NBjD`</summary>

````text
**results.tex** — complete contents:

```
  1	\section{Results}
  2	\label{sec:results}
  3	
  4	\begin{figure}[t]
  5	\centering
  6	\includegraphics[width=\columnwidth]{figures/fig_regime_transition.pdf}
  7	\caption{Predictor shift across panel sizes. $\eta_{\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\alpha{=}0.05$.}
  8	\label{fig:regime_transition}
  9	\end{figure}
 10	
 11	\subsection{Weakest-Link Dominance at \texorpdfstring{$K{=}3$}{K=3}}
 12	\label{sec:dominance}
 13	
 14	Table~\ref{tab:dominance} reports the log-log OLS regression (Equation~\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\ref{tab:models}).
 15	
 16	Under OLS, $K_{\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\eta_{\max}$ is significant in 10/12 (exceptions: MMLU $\times$ score manipulation and ARC $\times$ position bias), consistent with Proposition~\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\mathrm{eff}}$-dominant, and zero $\eta_{\max}$-dominant conditions. However, the $r = 0.70$ $K_{\mathrm{eff}}$--$\eta_{\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\ref{app:keff_dist}).
 17	
 18	Figure~\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\eta_{\max}$ 3/12, $K_{\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\mathrm{eff}}$ significance at $K{\geq}5$ (Appendix~\ref{app:crossed_re}).
 18	
 19	\begin{table}[t]
 20	\centering
 21	\small
 22	\begin{tabular}{lcc}
 23	\toprule
 24	\textbf{Method} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} \\
 25	\midrule
 26	OLS                    & 10/12 & 12/12 \\
 27	Clustered SE           & 4/12  & 0/12  \\
 28	Mixed effects          & 7/12  & 3/12  \\
 29	Wild bootstrap         & 3/12  & 4/12  \\
 30	Frac.\ logit (clust.)  & 7/12  & 9/12  \\
 31	\bottomrule
 32	\end{tabular}
 33	\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}
 34	\label{tab:method_comparison}
 35	\end{table}
 36	
 37	
 38	Power analysis yields MDE $\beta_{\mathrm{std}} = 0.14$ at 80\% power (Appendix~\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.
 39	
 40	\subsection{The Diminishing Weakest Link Across Panel Sizes}
 41	\label{sec:cross_k}
 42	
 43	The $K{=}3$ pattern is method-sensitive (Table~\ref{tab:method_comparison}), contrasting with $K{\geq}5$ where $K_{\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \in \{3, 5, 7\}$ with max-$p$ correction.
 44	
 45	Meta-analytic pooling \citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\eta_{\max}$'s pooled $\hat{\beta}_{\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\geq}5$. $K_{\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\%$; Appendix~\ref{app:meta_analytic_details}). Figure~\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\% CIs are in Figure~\ref{fig:forest_plot} (Appendix~\ref{app:effect_size_forest}). The $\eta_{\max}$ decline holds under both $K_{\mathrm{eff}}$ and $\kappa$-diversity.
 46	
 47	
 48	\subsection{Random vs.\ Adaptive Fault Contrast}
 49	\label{sec:rf_contrast}
 49	
 50	Random faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\mathrm{eff}}$ retains power (7/12). The positive $K_{\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \citep{goodfellow2015adversarial,kariyappa2019improving}.
 51	
 52	\subsection{Positive Direction Across Attack Types}
 53	\label{sec:gam_taxonomy}
 54	
 55	GAM bootstrap confirms positive $K_{\mathrm{eff}}$ direction in all 12 conditions (88.9--100\% positive rate; Figure~\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).
 56	
 57	\subsection{Aggregation Rules and the Diversity Channel}
 58	\label{sec:aggregation}
 59	
 60	Table~\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.
 61	
 62	\begin{table}[t]
 63	\centering
 64	\small
 65	\begin{tabular}{lcccc}
 66	\toprule
 67	\textbf{Method} & \textbf{$\eta_{\max}$ sig} & \textbf{$K_{\mathrm{eff}}$ sig} & \textbf{$K_{\mathrm{eff}}$ $\beta$ dir.} & \textbf{$R^2$} \\
 68	\midrule
 69	Threshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\
 70	Majority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\
 71	Weighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\
 72	Bayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\
 73	\bottomrule
 74	\end{tabular}
 75	\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}
 76	\label{tab:aggregation}
 77	\end{table}
 78	
 79	
 80	Predictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\mathrm{eff}}$ (5+/1$-$) but $\eta_{\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\ref{app:aggregation_k7}).
 81	
 82	\paragraph{Fractional Logit Robustness.}
 83	Fractional logit \citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\% directional concordance with OLS (71/72; Appendix~\ref{app:robustness_checks}).
```

---

**analysis.tex** — complete contents:

```
  1	\section{Analysis}
  2	\label{sec:analysis}
  3	
  4	\paragraph{Diversity--Capability Confound.}
  5	$K_{\mathrm{eff}}$ and $\eta_{\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\approx}2.0$--$2.9$; Figure~\ref{fig:keff_eta_scatter}, Appendix~\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \citep{cinelli2020making} shows the confound could account for the association in 69\% of conditions (Appendix~\ref{app:sensitivity}), though fractional logit confirms the positive association (9/12 at all $K$). Causal attribution requires capability-controlled designs (Appendices~\ref{app:sensitivity_poolA},~\ref{app:cross_benchmark}).
  6	
  7	\paragraph{API-Only vs.\ Full Pool.}
  8	Restricting to 9 API models removes the AWQ confound but increases collinearity ($r{=}0.85$): $\eta_{\max}$ retains significance (8/12) while $K_{\mathrm{eff}}$ drops (2--3/12); the API-only pool lacks statistical power (MDE $> 0.9$; Appendices~\ref{app:quant_dummy},~\ref{app:random_subsample}).
  9	
 10	\paragraph{Aggregation and Deployment.}
 11	Aggregation rules influence predictability but not $K_{\mathrm{eff}}$'s direction (Figure~\ref{fig:aggregation_heatmap}). Threshold voting yields the highest $R^2$ ($0.83$ at $K{=}3$), while Bayesian calibration nearly neutralizes panel composition effects ($R^2{\leq}0.17$ across all $K$). At $K{=}7$, Bayesian calibration fully neutralizes $K_{\mathrm{eff}}$ (0/12; Appendix~\ref{app:bayesian_entropy}). Robustness-first selection ($\min \eta_{\max}$) achieves lowest ASR in all 12 conditions (Appendix~\ref{app:panel_selection}), confirming that selecting judges by individual robustness dominates diversity-maximizing strategies regardless of panel size. Clean $K_{\mathrm{eff}}$ is stable under 4/6 attacks ($\rho{\geq}0.91$; Appendix~\ref{app:attacked_keff}), offering a deployable metric from clean-condition agreement alone.
 12	
 13	\paragraph{Metric Sensitivity of the Diversity Trajectory.}
 14	The diversity significance trajectory is operationalization-dependent: $K_{\mathrm{eff}}$ significance increases ($4 \to 7 \to 8$/12) while $\kappa$-diversity \citep{kuncheva2003measures} decreases ($8 \to 7 \to 6$/12; Appendix~\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \to 4 \to 0$; Appendix~\ref{app:shannon_entropy}). Both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\eta_{\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.
 15	
```

agentId: a8e29686edf3c5013 (use SendMessage with to: 'a8e29686edf3c5013' to continue this agent)
&lt;usage>total_tokens: 22776
tool_uses: 2
duration_ms: 60419&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "faaebe95-aaac-40c9-9037-5d1eb2892a7a",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following files in full and report their complete contents with line numbers:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex\n\nReport every line with line numbers.",
    "agentId": "a8e29686edf3c5013",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "**results.tex** — complete contents:\n\n```\n  1\t\\section{Results}\n  2\t\\label{sec:results}\n  3\t\n  4\t\\begin{figure}[t]\n  5\t\\centering\n  6\t\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n  7\t\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n  8\t\\label{fig:regime_transition}\n  9\t\\end{figure}\n 10\t\n 11\t\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n 12\t\\label{sec:dominance}\n 13\t\n 14\tTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n 15\t\n 16\tUnder OLS, $K_{\\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n 17\t\n 18\tFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n 18\t\n 19\t\\begin{table}[t]\n 20\t\\centering\n 21\t\\small\n 22\t\\begin{tabular}{lcc}\n 23\t\\toprule\n 24\t\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n 25\t\\midrule\n 26\tOLS                    & 10/12 & 12/12 \\\\\n 27\tClustered SE           & 4/12  & 0/12  \\\\\n 28\tMixed effects          & 7/12  & 3/12  \\\\\n 29\tWild bootstrap         & 3/12  & 4/12  \\\\\n 30\tFrac.\\ logit (clust.)  & 7/12  & 9/12  \\\\\n 31\t\\bottomrule\n 32\t\\end{tabular}\n 33\t\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}\n 34\t\\label{tab:method_comparison}\n 35\t\\end{table}\n 36\t\n 37\t\n 38\tPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\n 39\t\n 40\t\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n 41\t\\label{sec:cross_k}\n 42\t\n 43\tThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n 44\t\n 45\tMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n 46\t\n 47\t\n 48\t\\subsection{Random vs.\\ Adaptive Fault Contrast}\n 49\t\\label{sec:rf_contrast}\n 49\t\n 50\tRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n 51\t\n 52\t\\subsection{Positive Direction Across Attack Types}\n 53\t\\label{sec:gam_taxonomy}\n 54\t\n 55\tGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n 56\t\n 57\t\\subsection{Aggregation Rules and the Diversity Channel}\n 58\t\\label{sec:aggregation}\n 59\t\n 60\tTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n 61\t\n 62\t\\begin{table}[t]\n 63\t\\centering\n 64\t\\small\n 65\t\\begin{tabular}{lcccc}\n 66\t\\toprule\n 67\t\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n 68\t\\midrule\n 69\tThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\n 70\tMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\n 71\tWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\n 72\tBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n 73\t\\bottomrule\n 74\t\\end{tabular}\n 75\t\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n 76\t\\label{tab:aggregation}\n 77\t\\end{table}\n 78\t\n 79\t\n 80\tPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n 81\t\n 82\t\\paragraph{Fractional Logit Robustness.}\n 83\tFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n```\n\n---\n\n**analysis.tex** — complete contents:\n\n```\n  1\t\\section{Analysis}\n  2\t\\label{sec:analysis}\n  3\t\n  4\t\\paragraph{Diversity--Capability Confound.}\n  5\t$K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\\approx}2.0$--$2.9$; Figure~\\ref{fig:keff_eta_scatter}, Appendix~\\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \\citep{cinelli2020making} shows the confound could account for the association in 69\\% of conditions (Appendix~\\ref{app:sensitivity}), though fractional logit confirms the positive association (9/12 at all $K$). Causal attribution requires capability-controlled designs (Appendices~\\ref{app:sensitivity_poolA},~\\ref{app:cross_benchmark}).\n  6\t\n  7\t\\paragraph{API-Only vs.\\ Full Pool.}\n  8\tRestricting to 9 API models removes the AWQ confound but increases collinearity ($r{=}0.85$): $\\eta_{\\max}$ retains significance (8/12) while $K_{\\mathrm{eff}}$ drops (2--3/12); the API-only pool lacks statistical power (MDE $> 0.9$; Appendices~\\ref{app:quant_dummy},~\\ref{app:random_subsample}).\n  9\t\n 10\t\\paragraph{Aggregation and Deployment.}\n 11\tAggregation rules influence predictability but not $K_{\\mathrm{eff}}$'s direction (Figure~\\ref{fig:aggregation_heatmap}). Threshold voting yields the highest $R^2$ ($0.83$ at $K{=}3$), while Bayesian calibration nearly neutralizes panel composition effects ($R^2{\\leq}0.17$ across all $K$). At $K{=}7$, Bayesian calibration fully neutralizes $K_{\\mathrm{eff}}$ (0/12; Appendix~\\ref{app:bayesian_entropy}). Robustness-first selection ($\\min \\eta_{\\max}$) achieves lowest ASR in all 12 conditions (Appendix~\\ref{app:panel_selection}), confirming that selecting judges by individual robustness dominates diversity-maximizing strategies regardless of panel size. Clean $K_{\\mathrm{eff}}$ is stable under 4/6 attacks ($\\rho{\\geq}0.91$; Appendix~\\ref{app:attacked_keff}), offering a deployable metric from clean-condition agreement alone.\n 12\t\n 13\t\\paragraph{Metric Sensitivity of the Diversity Trajectory.}\n 14\tThe diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.\n 15\t\n```"
      }
    ],
    "totalDurationMs": 60419,
    "totalTokens": 22776,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4530,
      "cache_read_input_tokens": 14649,
      "output_tokens": 3596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4530
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3596,
          "cache_read_input_tokens": 14649,
          "cache_creation_input_tokens": 4530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4530,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---


### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the per_condition_full_reanalysis.json to get the detailed data, and also read the specific lines of appendix.tex that need changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "50e6cfb8-9acd-40f0-ab12-f6e3b1ae06eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANuQVd9KsM3S7nQqbAcj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5458,
      "cache_creation_input_tokens": 4140,
      "cache_read_input_tokens": 30022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4140
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

_source line 54_

Now let me read the per-condition JSON and the specific appendix lines that need updating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "fc7ffcee-64ca-42c5-b0f8-126b17a686b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANuQVd9KsM3S7nQqbAcj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5458,
      "cache_creation_input_tokens": 4140,
      "cache_read_input_tokens": 30022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4140
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

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01WamhWp6RSj8kMR1yLLDzrx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/_project/data/per_condition_full_reanalysis.json",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1ff3f13f-af2c-4fa4-b0df-5bced4cd7ff4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANuQVd9KsM3S7nQqbAcj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5458,
      "cache_creation_input_tokens": 4140,
      "cache_read_input_tokens": 30022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4140
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

_source line 56 · 2026-05-25T21:07:14.681Z_

<details><summary>↩ Tool result · `toolu_01WamhWp6RSj8kMR1yLLDzrx`</summary>

```text
1	{
2	  "K3": {
3	    "mmluxprompt_injection": {
4	      "condition": "mmluxprompt_injection",
5	      "n_panels": 455,
6	      "r2": 0.43452537117146794,
7	      "keff_beta_std": 0.4831468235397298,
8	      "keff_se_std": 0.05440031381271274,
9	      "keff_p_ols": 1.567918418229639e-17,
10	      "eta_beta_std": 0.21243752858999632,
11	      "eta_se_std": 0.054400313812712785,
12	      "eta_p_ols": 0.00010857017674401543,
13	      "keff_wcb_max_p": 0.023,
14	      "eta_wcb_max_p": 0.108,
15	      "keff_fl_coef": 5.475870576018366,
16	      "keff_fl_p": 4.036974298545473e-05,
17	      "eta_fl_coef": 0.7588187564665185,
18	      "eta_fl_p": 1.437006637241922e-06,
19	      "fl_pseudo_r2": 0.598231633604737
20	    },
21	    "mmluxsycophancy": {
22	      "condition": "mmluxsycophancy",
23	      "n_panels": 455,
24	      "r2": 0.36548655549911246,
25	      "keff_beta_std": 0.48349246398201884,
26	      "keff_se_std": 0.04342912103950052,
27	      "keff_p_ols": 1.318362725772601e-25,
28	      "eta_beta_std": 0.19311235979172012,
29	      "eta_se_std": 0.04342912103950049,
30	      "eta_p_ols": 1.0992059783679142e-05,
31	      "keff_wcb_max_p": 0.007,
32	      "eta_wcb_max_p": 0.001,
33	      "keff_fl_coef": 3.948836895347326,
34	      "keff_fl_p": 2.66051582733281e-06,
35	      "eta_fl_coef": 0.7739554478596735,
36	      "eta_fl_p": 1.594221236294419e-08,
37	      "fl_pseudo_r2": 0.546886106722073
38	    },
39	    "mmluxscore_manipulation": {
40	      "condition": "mmluxscore_manipulation",
41	      "n_panels": 455,
42	      "r2": 0.413136732056247,
43	      "keff_beta_std": 0.5423299186068864,
44	      "keff_se_std": 0.06234807555161517,
45	      "keff_p_ols": 6.296466729973341e-17,
46	      "eta_beta_std": 0.118570832866458,
47	      "eta_se_std": 0.062348075551615124,
48	      "eta_p_ols": 0.057838563188100496,
49	      "keff_wcb_max_p": 0.043,
50	      "eta_wcb_max_p": 0.487,
51	      "keff_fl_coef": 5.710526939927132,
52	      "keff_fl_p": 3.385856153279627e-05,
53	      "eta_fl_coef": 0.20554156214291933,
54	      "eta_fl_p": 0.44303847448409295,
55	      "fl_pseudo_r2": 0.540972345375356
56	    },
57	    "mmluxverbosity_bias": {
58	      "condition": "mmluxverbosity_bias",
59	      "n_panels": 455,
60	      "r2": 0.361783911537078,
61	      "keff_beta_std": 0.3775387541056554,
62	      "keff_se_std": 0.04725902687312099,
63	      "keff_p_ols": 1.1433052204388537e-14,
64	      "eta_beta_std": 0.292259799895208,
65	      "eta_se_std": 0.047259026873120905,
66	      "eta_p_ols": 1.3977050668302649e-09,
67	      "keff_wcb_max_p": 0.008,
68	      "eta_wcb_max_p": 0.001,
69	      "keff_fl_coef": 3.774545110449067,
70	      "keff_fl_p": 3.222110490800622e-05,
71	      "eta_fl_coef": 1.061378107118072,
72	      "eta_fl_p": 2.559506417938565e-11,
73	      "fl_pseudo_r2": 0.6506402124339474
74	    },
75	    "mmluxposition_bias": {
76	      "condition": "mmluxposition_bias",
77	      "n_panels": 455,
78	      "r2": 0.5179191031916737,
79	      "keff_beta_std": -0.33389022686773595,
80	      "keff_se_std": 0.035779555152377185,
81	      "keff_p_ols": 4.700232357967397e-19,
82	      "eta_beta_std": 0.5155566050288577,
83	      "eta_se_std": 0.03577955515237721,
84	      "eta_p_ols": 5.2843680583640495e-39,
85	      "keff_wcb_max_p": 0.002,
86	      "eta_wcb_max_p": 0.001,
87	      "keff_fl_coef": -0.6011026154673018,
88	      "keff_fl_p": 0.00018272826863754353,
89	      "eta_fl_coef": 1.8520765564916308,
90	      "eta_fl_p": 3.63696390538567e-15,
91	      "fl_pseudo_r2": 0.5215368367731037
92	    },
93	    "mmluxauthority_bias": {
94	      "condition": "mmluxauthority_bias",
95	      "n_panels": 455,
96	      "r2": 0.3316484359172295,
97	      "keff_beta_std": 0.5228694590301304,
98	      "keff_se_std": 0.04873903672942025,
99	      "keff_p_ols": 4.497001005017999e-24,
100	      "eta_beta_std": 0.08056323523129255,
101	      "eta_se_std": 0.04873903672942022,
102	      "eta_p_ols": 0.099035219991377,
103	      "keff_wcb_max_p": 0.009,
104	      "eta_wcb_max_p": 0.23,
105	      "keff_fl_coef": 3.6894519820124745,
106	      "keff_fl_p": 9.886518165508663e-06,
107	      "eta_fl_coef": 0.3081355846904185,
108	      "eta_fl_p": 0.23457126836795927,
109	      "fl_pseudo_r2": 0.37116948122186755
110	    },
111	    "arc_challengexprompt_injection": {
112	      "condition": "arc_challengexprompt_injection",
113	      "n_panels": 455,
114	      "r2": 0.32378846562171615,
115	      "keff_beta_std": 0.3572939431708954,
116	      "keff_se_std": 0.05184423585419734,
117	      "keff_p_ols": 1.86034748811719e-11,
118	      "eta_beta_std": 0.26481013563473044,
119	      "eta_se_std": 0.05184423585419723,
120	      "eta_p_ols": 4.814954987895597e-07,
121	      "keff_wcb_max_p": 0.028,
122	      "eta_wcb_max_p": 0.047,
123	      "keff_fl_coef": 7.3916594558138184,
124	      "keff_fl_p": 0.04849434555083733,
125	      "eta_fl_coef": 0.014608992754275156,
126	      "eta_fl_p": 0.9659839298376636,
127	      "fl_pseudo_r2": 0.5350583532727549
128	    },
129	    "arc_challengexsycophancy": {
130	      "condition": "arc_challengexsycophancy",
131	      "n_panels": 455,
132	      "r2": 0.24127123307527398,
133	      "keff_beta_std": 0.2830955424304114,
134	      "keff_se_std": 0.05307580707492967,
135	      "keff_p_ols": 1.5232768409721678e-07,
136	      "eta_beta_std": 0.25993827887736587,
137	      "eta_se_std": 0.05307580707492968,
138	      "eta_p_ols": 1.3539854851295072e-06,
139	      "keff_wcb_max_p": 0.077,
140	      "eta_wcb_max_p": 0.008,
141	      "keff_fl_coef": 1.5749897137734417,
142	      "keff_fl_p": 0.219131277979301,
143	      "eta_fl_coef": 0.6962694170254233,
144	      "eta_fl_p": 0.00012863314709235196,
145	      "fl_pseudo_r2": 0.522364731235888
146	    },
147	    "arc_challengexscore_manipulation": {
148	      "condition": "arc_challengexscore_manipulation",
149	      "n_panels": 455,
150	      "r2": 0.29187451191292935,
151	      "keff_beta_std": 0.4657042555959844,
152	      "keff_se_std": 0.08522818271605377,
153	      "keff_p_ols": 7.696489414560666e-08,
154	      "eta_beta_std": 0.08263709522209896,
155	      "eta_se_std": 0.08522818271605383,
156	      "eta_p_ols": 0.3327653348996712,
157	      "keff_wcb_max_p": 0.12,
158	      "eta_wcb_max_p": 0.64,
159	      "keff_fl_coef": 7.702249263778288,
160	      "keff_fl_p": 2.8209857298436547e-10,
161	      "eta_fl_coef": -0.337961427055802,
162	      "eta_fl_p": 0.01953192759511765,
163	      "fl_pseudo_r2": 0.6045372079990561
164	    },
165	    "arc_challengexverbosity_bias": {
166	      "condition": "arc_challengexverbosity_bias",
167	      "n_panels": 455,
168	      "r2": 0.312214835705968,
169	      "keff_beta_std": 0.3468778856719513,
170	      "keff_se_std": 0.05840684356608927,
171	      "keff_p_ols": 5.72550145473933e-09,
172	      "eta_beta_std": 0.2502991699828676,
173	      "eta_se_std": 0.05840684356608929,
174	      "eta_p_ols": 2.230156409034909e-05,
175	      "keff_wcb_max_p": 0.023,
176	      "eta_wcb_max_p": 0.07,
177	      "keff_fl_coef": 4.247646920739039,
178	      "keff_fl_p": 0.023924544805486548,
179	      "eta_fl_coef": 0.27993161604473554,
180	      "eta_fl_p": 0.25733079097387634,
181	      "fl_pseudo_r2": 0.5402981562979168
182	    },
183	    "arc_challengexposition_bias": {
184	      "condition": "arc_challengexposition_bias",
185	      "n_panels": 455,
186	      "r2": 0.3629354065828053,
187	      "keff_beta_std": -0.37217721466035747,
188	      "keff_se_std": 0.03920803559753563,
189	      "keff_p_ols": 1.3108116984314708e-19,
190	      "eta_beta_std": 0.37840989903058486,
191	      "eta_se_std": 0.03920803559753559,
192	      "eta_p_ols": 3.649668850643354e-20,
193	      "keff_wcb_max_p": 0.005,
194	      "eta_wcb_max_p": 0.006,
195	      "keff_fl_coef": -0.5077282545747227,
196	      "keff_fl_p": 0.005671077809432195,
197	      "eta_fl_coef": 2.845373335343427,
198	      "eta_fl_p": 0.000127456920568429,
199	      "fl_pseudo_r2": 0.35181711111717895
200	    },
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "7d72cb8d-5bd3-4892-b8cf-3269086659b3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/_project/data/per_condition_full_reanalysis.json",
      "content": "{\n  \"K3\": {\n    \"mmluxprompt_injection\": {\n      \"condition\": \"mmluxprompt_injection\",\n      \"n_panels\": 455,\n      \"r2\": 0.43452537117146794,\n      \"keff_beta_std\": 0.4831468235397298,\n      \"keff_se_std\": 0.05440031381271274,\n      \"keff_p_ols\": 1.567918418229639e-17,\n      \"eta_beta_std\": 0.21243752858999632,\n      \"eta_se_std\": 0.054400313812712785,\n      \"eta_p_ols\": 0.00010857017674401543,\n      \"keff_wcb_max_p\": 0.023,\n      \"eta_wcb_max_p\": 0.108,\n      \"keff_fl_coef\": 5.475870576018366,\n      \"keff_fl_p\": 4.036974298545473e-05,\n      \"eta_fl_coef\": 0.7588187564665185,\n      \"eta_fl_p\": 1.437006637241922e-06,\n      \"fl_pseudo_r2\": 0.598231633604737\n    },\n    \"mmluxsycophancy\": {\n      \"condition\": \"mmluxsycophancy\",\n      \"n_panels\": 455,\n      \"r2\": 0.36548655549911246,\n      \"keff_beta_std\": 0.48349246398201884,\n      \"keff_se_std\": 0.04342912103950052,\n      \"keff_p_ols\": 1.318362725772601e-25,\n      \"eta_beta_std\": 0.19311235979172012,\n      \"eta_se_std\": 0.04342912103950049,\n      \"eta_p_ols\": 1.0992059783679142e-05,\n      \"keff_wcb_max_p\": 0.007,\n      \"eta_wcb_max_p\": 0.001,\n      \"keff_fl_coef\": 3.948836895347326,\n      \"keff_fl_p\": 2.66051582733281e-06,\n      \"eta_fl_coef\": 0.7739554478596735,\n      \"eta_fl_p\": 1.594221236294419e-08,\n      \"fl_pseudo_r2\": 0.546886106722073\n    },\n    \"mmluxscore_manipulation\": {\n      \"condition\": \"mmluxscore_manipulation\",\n      \"n_panels\": 455,\n      \"r2\": 0.413136732056247,\n      \"keff_beta_std\": 0.5423299186068864,\n      \"keff_se_std\": 0.06234807555161517,\n      \"keff_p_ols\": 6.296466729973341e-17,\n      \"eta_beta_std\": 0.118570832866458,\n      \"eta_se_std\": 0.062348075551615124,\n      \"eta_p_ols\": 0.057838563188100496,\n      \"keff_wcb_max_p\": 0.043,\n      \"eta_wcb_max_p\": 0.487,\n      \"keff_fl_coef\": 5.710526939927132,\n      \"keff_fl_p\": 3.385856153279627e-05,\n      \"eta_fl_coef\": 0.20554156214291933,\n      \"eta_fl_p\": 0.44303847448409295,\n      \"fl_pseudo_r2\": 0.540972345375356\n    },\n    \"mmluxverbosity_bias\": {\n      \"condition\": \"mmluxverbosity_bias\",\n      \"n_panels\": 455,\n      \"r2\": 0.361783911537078,\n      \"keff_beta_std\": 0.3775387541056554,\n      \"keff_se_std\": 0.04725902687312099,\n      \"keff_p_ols\": 1.1433052204388537e-14,\n      \"eta_beta_std\": 0.292259799895208,\n      \"eta_se_std\": 0.047259026873120905,\n      \"eta_p_ols\": 1.3977050668302649e-09,\n      \"keff_wcb_max_p\": 0.008,\n      \"eta_wcb_max_p\": 0.001,\n      \"keff_fl_coef\": 3.774545110449067,\n      \"keff_fl_p\": 3.222110490800622e-05,\n      \"eta_fl_coef\": 1.061378107118072,\n      \"eta_fl_p\": 2.559506417938565e-11,\n      \"fl_pseudo_r2\": 0.6506402124339474\n    },\n    \"mmluxposition_bias\": {\n      \"condition\": \"mmluxposition_bias\",\n      \"n_panels\": 455,\n      \"r2\": 0.5179191031916737,\n      \"keff_beta_std\": -0.33389022686773595,\n      \"keff_se_std\": 0.035779555152377185,\n      \"keff_p_ols\": 4.700232357967397e-19,\n      \"eta_beta_std\": 0.5155566050288577,\n      \"eta_se_std\": 0.03577955515237721,\n      \"eta_p_ols\": 5.2843680583640495e-39,\n      \"keff_wcb_max_p\": 0.002,\n      \"eta_wcb_max_p\": 0.001,\n      \"keff_fl_coef\": -0.6011026154673018,\n      \"keff_fl_p\": 0.00018272826863754353,\n      \"eta_fl_coef\": 1.8520765564916308,\n      \"eta_fl_p\": 3.63696390538567e-15,\n      \"fl_pseudo_r2\": 0.5215368367731037\n    },\n    \"mmluxauthority_bias\": {\n      \"condition\": \"mmluxauthority_bias\",\n      \"n_panels\": 455,\n      \"r2\": 0.3316484359172295,\n      \"keff_beta_std\": 0.5228694590301304,\n      \"keff_se_std\": 0.04873903672942025,\n      \"keff_p_ols\": 4.497001005017999e-24,\n      \"eta_beta_std\": 0.08056323523129255,\n      \"eta_se_std\": 0.04873903672942022,\n      \"eta_p_ols\": 0.099035219991377,\n      \"keff_wcb_max_p\": 0.009,\n      \"eta_wcb_max_p\": 0.23,\n      \"keff_fl_coef\": 3.6894519820124745,\n      \"keff_fl_p\": 9.886518165508663e-06,\n      \"eta_fl_coef\": 0.3081355846904185,\n      \"eta_fl_p\": 0.23457126836795927,\n      \"fl_pseudo_r2\": 0.37116948122186755\n    },\n    \"arc_challengexprompt_injection\": {\n      \"condition\": \"arc_challengexprompt_injection\",\n      \"n_panels\": 455,\n      \"r2\": 0.32378846562171615,\n      \"keff_beta_std\": 0.3572939431708954,\n      \"keff_se_std\": 0.05184423585419734,\n      \"keff_p_ols\": 1.86034748811719e-11,\n      \"eta_beta_std\": 0.26481013563473044,\n      \"eta_se_std\": 0.05184423585419723,\n      \"eta_p_ols\": 4.814954987895597e-07,\n      \"keff_wcb_max_p\": 0.028,\n      \"eta_wcb_max_p\": 0.047,\n      \"keff_fl_coef\": 7.3916594558138184,\n      \"keff_fl_p\": 0.04849434555083733,\n      \"eta_fl_coef\": 0.014608992754275156,\n      \"eta_fl_p\": 0.9659839298376636,\n      \"fl_pseudo_r2\": 0.5350583532727549\n    },\n    \"arc_challengexsycophancy\": {\n      \"condition\": \"arc_challengexsycophancy\",\n      \"n_panels\": 455,\n      \"r2\": 0.24127123307527398,\n      \"keff_beta_std\": 0.2830955424304114,\n      \"keff_se_std\": 0.05307580707492967,\n      \"keff_p_ols\": 1.5232768409721678e-07,\n      \"eta_beta_std\": 0.25993827887736587,\n      \"eta_se_std\": 0.05307580707492968,\n      \"eta_p_ols\": 1.3539854851295072e-06,\n      \"keff_wcb_max_p\": 0.077,\n      \"eta_wcb_max_p\": 0.008,\n      \"keff_fl_coef\": 1.5749897137734417,\n      \"keff_fl_p\": 0.219131277979301,\n      \"eta_fl_coef\": 0.6962694170254233,\n      \"eta_fl_p\": 0.00012863314709235196,\n      \"fl_pseudo_r2\": 0.522364731235888\n    },\n    \"arc_challengexscore_manipulation\": {\n      \"condition\": \"arc_challengexscore_manipulation\",\n      \"n_panels\": 455,\n      \"r2\": 0.29187451191292935,\n      \"keff_beta_std\": 0.4657042555959844,\n      \"keff_se_std\": 0.08522818271605377,\n      \"keff_p_ols\": 7.696489414560666e-08,\n      \"eta_beta_std\": 0.08263709522209896,\n      \"eta_se_std\": 0.08522818271605383,\n      \"eta_p_ols\": 0.3327653348996712,\n      \"keff_wcb_max_p\": 0.12,\n      \"eta_wcb_max_p\": 0.64,\n      \"keff_fl_coef\": 7.702249263778288,\n      \"keff_fl_p\": 2.8209857298436547e-10,\n      \"eta_fl_coef\": -0.337961427055802,\n      \"eta_fl_p\": 0.01953192759511765,\n      \"fl_pseudo_r2\": 0.6045372079990561\n    },\n    \"arc_challengexverbosity_bias\": {\n      \"condition\": \"arc_challengexverbosity_bias\",\n      \"n_panels\": 455,\n      \"r2\": 0.312214835705968,\n      \"keff_beta_std\": 0.3468778856719513,\n      \"keff_se_std\": 0.05840684356608927,\n      \"keff_p_ols\": 5.72550145473933e-09,\n      \"eta_beta_std\": 0.2502991699828676,\n      \"eta_se_std\": 0.05840684356608929,\n      \"eta_p_ols\": 2.230156409034909e-05,\n      \"keff_wcb_max_p\": 0.023,\n      \"eta_wcb_max_p\": 0.07,\n      \"keff_fl_coef\": 4.247646920739039,\n      \"keff_fl_p\": 0.023924544805486548,\n      \"eta_fl_coef\": 0.27993161604473554,\n      \"eta_fl_p\": 0.25733079097387634,\n      \"fl_pseudo_r2\": 0.5402981562979168\n    },\n    \"arc_challengexposition_bias\": {\n      \"condition\": \"arc_challengexposition_bias\",\n      \"n_panels\": 455,\n      \"r2\": 0.3629354065828053,\n      \"keff_beta_std\": -0.37217721466035747,\n      \"keff_se_std\": 0.03920803559753563,\n      \"keff_p_ols\": 1.3108116984314708e-19,\n      \"eta_beta_std\": 0.37840989903058486,\n      \"eta_se_std\": 0.03920803559753559,\n      \"eta_p_ols\": 3.649668850643354e-20,\n      \"keff_wcb_max_p\": 0.005,\n      \"eta_wcb_max_p\": 0.006,\n      \"keff_fl_coef\": -0.5077282545747227,\n      \"keff_fl_p\": 0.005671077809432195,\n      \"eta_fl_coef\": 2.845373335343427,\n      \"eta_fl_p\": 0.000127456920568429,\n      \"fl_pseudo_r2\": 0.35181711111717895\n    },",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 656
    }
  }
}
```

</details>

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01Na865JiXTDaFKEanXiMwq9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 525,
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
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "d1408910-8a11-482f-a27f-a1288ce719e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANuQVd9KsM3S7nQqbAcj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5458,
      "cache_creation_input_tokens": 4140,
      "cache_read_input_tokens": 30022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4140
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

_source line 58 · 2026-05-25T21:07:15.652Z_

<details><summary>↩ Tool result · `toolu_01Na865JiXTDaFKEanXiMwq9`</summary>

```text
525	\subsection{Meta-Analytic Pooling Procedure}
526	\label{app:meta_analytic_details}
527	
528	Section~\ref{sec:cross_k} reports pooled effect sizes using DerSimonian--Laird (DL) random effects \citep{dersimonian1986meta}. Here we detail the pooling procedure and assess sensitivity to alternative meta-analytic methods.
529	
530	\paragraph{Procedure.} For each predictor $X \in \{K_{\mathrm{eff}}, \eta_{\max}\}$ at each $K$, we compute 12 condition-specific standardized OLS coefficients $\hat{\beta}_{\mathrm{std}}^{(c)}$ with standard errors $\mathrm{SE}^{(c)}$ from the wild cluster bootstrap. DL random effects models the 12 condition estimates as:
531	\begin{equation}
532	\hat{\beta}_{\mathrm{std}}^{(c)} = \mu + u_c + \epsilon_c, \quad u_c \sim \mathcal{N}(0, \tau^2), \quad \epsilon_c \sim \mathcal{N}(0, \sigma_c^2),
533	\end{equation}
534	where $\mu$ is the pooled effect, $\tau^2$ captures between-condition heterogeneity, and $\sigma_c^2$ is the within-condition sampling variance. The DL estimator for $\tau^2$ uses the $Q$-statistic:
535	\begin{equation}
536	\hat{\tau}^2_{\mathrm{DL}} = \max\!\left(0, \frac{Q - (C-1)}{\sum w_c - \sum w_c^2 / \sum w_c}\right),
537	\end{equation}
538	with $w_c = 1/\sigma_c^2$ the inverse-variance weights and $C{=}12$ conditions.
539	
540	\paragraph{$I^2$ Heterogeneity.} The high $I^2$ values (87.7\%--99.8\%) indicate that most variation across conditions reflects genuine heterogeneity rather than sampling noise. This is expected: different attack types exploit different vulnerability mechanisms, and the two benchmarks differ in format and difficulty. The pooled estimate $\mu$ represents the central tendency across this heterogeneous landscape, not a single shared effect size.
541	
542	\paragraph{Per-$K$ Pooled Results.} Table~\ref{tab:meta_pooled} reports the complete pooled estimates.
543	
544	\begin{table}[h]
545	\centering
546	\footnotesize
547	\setlength{\tabcolsep}{3pt}
548	\begin{tabular}{rcccccc}
549	\toprule
550	& \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} \\
551	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
552	$\boldsymbol{K}$ & $\hat{\mu}$ & 95\% CI & $I^2$ & $\hat{\mu}$ & 95\% CI & $I^2$ \\
553	\midrule
554	3 & 0.264 & [0.158, 0.369] & 91.3\% & 0.356 & [0.267, 0.445] & 87.7\% \\
555	5 & 0.102 & [$-$0.055, 0.259] & 99.4\% & 0.436 & [0.318, 0.553] & 98.9\% \\
556	7 & 0.084 & [$-$0.083, 0.251] & 99.8\% & 0.401 & [0.298, 0.503] & 99.4\% \\
557	\bottomrule
558	\end{tabular}
559	\caption{DerSimonian--Laird random effects pooled estimates across 12 conditions per $K$. $\hat{\mu}$: pooled standardized coefficient. $I^2$: between-condition heterogeneity. $\eta_{\max}$'s CI crosses zero at $K{\geq}5$; $K_{\mathrm{eff}}$ remains positive across all $K$.}
560	\label{tab:meta_pooled}
561	\end{table}
562	
563	\paragraph{Sensitivity to Alternative Estimators.} We compare DL with the restricted maximum likelihood (REML) estimator and the Hartung--Knapp--Sidik--Jonkman (HKSJ) confidence interval adjustment. REML produces similar point estimates ($\Delta\hat{\mu} < 0.01$) but slightly wider CIs due to its likelihood-based $\tau^2$ estimation. HKSJ CIs are uniformly wider than DL (average width increase: 18\%), reflecting its $t$-distribution-based inference that accounts for small-sample heterogeneity estimation uncertainty. Under HKSJ, $K_{\mathrm{eff}}$ retains positive CI lower bounds at all $K$ values; $\eta_{\max}$'s CI crosses zero at $K{=}3$ as well (lower bound $-0.02$), making the pooled result borderline even at the smallest panel size. The DL estimates reported in the main text are therefore the most favorable for $\eta_{\max}$; the diminishing weakest link pattern is more pronounced under alternative estimators.
564	
565	\section{Panel Selection Strategy Comparison}
566	\label{app:panel_selection}
567	
568	\begin{figure}[h]
569	\centering
570	\includegraphics[width=\columnwidth]{figures/fig4_panel_design.pdf}
571	\caption{Panel ASR under three selection strategies ($\min \eta_{\max}$, random, $\max K_{\mathrm{eff}}$) across 12 conditions. Robustness-first selection ($\min \eta_{\max}$) achieves the lowest ASR in all conditions.}
572	\label{fig:panel_design}
573	\end{figure}
574	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "94d4e590-ff64-4bf2-a4d3-8d189ab396c2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\\subsection{Meta-Analytic Pooling Procedure}\n\\label{app:meta_analytic_details}\n\nSection~\\ref{sec:cross_k} reports pooled effect sizes using DerSimonian--Laird (DL) random effects \\citep{dersimonian1986meta}. Here we detail the pooling procedure and assess sensitivity to alternative meta-analytic methods.\n\n\\paragraph{Procedure.} For each predictor $X \\in \\{K_{\\mathrm{eff}}, \\eta_{\\max}\\}$ at each $K$, we compute 12 condition-specific standardized OLS coefficients $\\hat{\\beta}_{\\mathrm{std}}^{(c)}$ with standard errors $\\mathrm{SE}^{(c)}$ from the wild cluster bootstrap. DL random effects models the 12 condition estimates as:\n\\begin{equation}\n\\hat{\\beta}_{\\mathrm{std}}^{(c)} = \\mu + u_c + \\epsilon_c, \\quad u_c \\sim \\mathcal{N}(0, \\tau^2), \\quad \\epsilon_c \\sim \\mathcal{N}(0, \\sigma_c^2),\n\\end{equation}\nwhere $\\mu$ is the pooled effect, $\\tau^2$ captures between-condition heterogeneity, and $\\sigma_c^2$ is the within-condition sampling variance. The DL estimator for $\\tau^2$ uses the $Q$-statistic:\n\\begin{equation}\n\\hat{\\tau}^2_{\\mathrm{DL}} = \\max\\!\\left(0, \\frac{Q - (C-1)}{\\sum w_c - \\sum w_c^2 / \\sum w_c}\\right),\n\\end{equation}\nwith $w_c = 1/\\sigma_c^2$ the inverse-variance weights and $C{=}12$ conditions.\n\n\\paragraph{$I^2$ Heterogeneity.} The high $I^2$ values (87.7\\%--99.8\\%) indicate that most variation across conditions reflects genuine heterogeneity rather than sampling noise. This is expected: different attack types exploit different vulnerability mechanisms, and the two benchmarks differ in format and difficulty. The pooled estimate $\\mu$ represents the central tendency across this heterogeneous landscape, not a single shared effect size.\n\n\\paragraph{Per-$K$ Pooled Results.} Table~\\ref{tab:meta_pooled} reports the complete pooled estimates.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{rcccccc}\n\\toprule\n& \\multicolumn{3}{c}{$\\boldsymbol{\\eta_{\\max}}$} & \\multicolumn{3}{c}{$\\boldsymbol{K_{\\mathrm{eff}}}$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\boldsymbol{K}$ & $\\hat{\\mu}$ & 95\\% CI & $I^2$ & $\\hat{\\mu}$ & 95\\% CI & $I^2$ \\\\\n\\midrule\n3 & 0.264 & [0.158, 0.369] & 91.3\\% & 0.356 & [0.267, 0.445] & 87.7\\% \\\\\n5 & 0.102 & [$-$0.055, 0.259] & 99.4\\% & 0.436 & [0.318, 0.553] & 98.9\\% \\\\\n7 & 0.084 & [$-$0.083, 0.251] & 99.8\\% & 0.401 & [0.298, 0.503] & 99.4\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DerSimonian--Laird random effects pooled estimates across 12 conditions per $K$. $\\hat{\\mu}$: pooled standardized coefficient. $I^2$: between-condition heterogeneity. $\\eta_{\\max}$'s CI crosses zero at $K{\\geq}5$; $K_{\\mathrm{eff}}$ remains positive across all $K$.}\n\\label{tab:meta_pooled}\n\\end{table}\n\n\\paragraph{Sensitivity to Alternative Estimators.} We compare DL with the restricted maximum likelihood (REML) estimator and the Hartung--Knapp--Sidik--Jonkman (HKSJ) confidence interval adjustment. REML produces similar point estimates ($\\Delta\\hat{\\mu} < 0.01$) but slightly wider CIs due to its likelihood-based $\\tau^2$ estimation. HKSJ CIs are uniformly wider than DL (average width increase: 18\\%), reflecting its $t$-distribution-based inference that accounts for small-sample heterogeneity estimation uncertainty. Under HKSJ, $K_{\\mathrm{eff}}$ retains positive CI lower bounds at all $K$ values; $\\eta_{\\max}$'s CI crosses zero at $K{=}3$ as well (lower bound $-0.02$), making the pooled result borderline even at the smallest panel size. The DL estimates reported in the main text are therefore the most favorable for $\\eta_{\\max}$; the diminishing weakest link pattern is more pronounced under alternative estimators.\n\n\\section{Panel Selection Strategy Comparison}\n\\label{app:panel_selection}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_panel_design.pdf}\n\\caption{Panel ASR under three selection strategies ($\\min \\eta_{\\max}$, random, $\\max K_{\\mathrm{eff}}$) across 12 conditions. Robustness-first selection ($\\min \\eta_{\\max}$) achieves the lowest ASR in all conditions.}\n\\label{fig:panel_design}\n\\end{figure}\n",
      "numLines": 50,
      "startLine": 525,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_01BHER33fHiJWb9oEr7frPKa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 100,
  "limit": 110
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "7b019199-110a-4da5-b9ca-f1fffa754a99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANuQVd9KsM3S7nQqbAcj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5458,
      "cache_creation_input_tokens": 4140,
      "cache_read_input_tokens": 30022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4140
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

_source line 60 · 2026-05-25T21:07:16.612Z_

<details><summary>↩ Tool result · `toolu_01BHER33fHiJWb9oEr7frPKa`</summary>

```text
100	\caption{Per-condition predictor dominance across panel sizes (wild cluster bootstrap, BH FDR $\alpha{=}0.05$). At $K{=}3$, dominance is heterogeneous (co-dominant, $K_{\mathrm{eff}}$-only, $\eta_{\max}$-only, and non-significant conditions coexist); at $K{\geq}5$, $K_{\mathrm{eff}}$ dominates uniformly while $\eta_{\max}$ diminishes substantially.}
101	\label{fig:dominance_heatmap}
102	\end{figure}
103	
104	\subsection{Per-Condition Regression Results}
105	\label{app:per_condition_regression}
106	
107	Tables~\ref{tab:percond_k3}--\ref{tab:percond_k7} report the full per-condition regression results underlying the significance counts in the main text. For each of 12 conditions (2 benchmarks $\times$ 6 attacks), we report the standardized OLS coefficients ($\hat{\beta}_{\mathrm{std}}$), $R^2$, and wild cluster bootstrap $p$-values (max-$p$ across $K$ position clusters, BH FDR $\alpha{=}0.05$).
108	
109	\begin{table*}[t]
110	\centering
111	\footnotesize
112	\setlength{\tabcolsep}{3pt}
113	\begin{tabular}{llccccccc}
114	\toprule
115	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
116	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
117	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
118	\midrule
119	\multirow{6}{*}{MMLU} & Prompt inj. & 0.252 & $1.6{\times}10^{-10}$ & 0.026 & 0.616 & $7.4{\times}10^{-46}$ & 0.003 & 0.663 \\
120	& Sycophancy & 0.166 & $1.2{\times}10^{-4}$ & 0.045 & 0.486 & $1.2{\times}10^{-26}$ & 0.012 & 0.334 \\
121	& Score manip. & 0.033 & 0.607 & 0.689 & 0.598 & $3.6{\times}10^{-19}$ & 0.005 & 0.390 \\
122	& Verbosity & 0.090 & 0.026 & 0.175 & 0.593 & $4.0{\times}10^{-40}$ & 0.001 & 0.407 \\
123	& Position & 0.104 & 0.057 & 0.117 & 0.418 & $1.1{\times}10^{-13}$ & 0.023 & 0.243 \\
124	& Authority & 0.010 & 0.852 & 0.864 & 0.377 & $3.4{\times}10^{-11}$ & 0.008 & 0.147 \\
125	\addlinespace
126	\multirow{6}{*}{ARC} & Prompt inj. & 0.330 & $6.4{\times}10^{-6}$ & 0.015 & 0.244 & $8.0{\times}10^{-4}$ & 0.092 & 0.303 \\
127	& Sycophancy & $-0.192$ & $6.3{\times}10^{-3}$ & 0.023 & 0.492 & $6.7{\times}10^{-12}$ & 0.001 & 0.132 \\
128	& Score manip. & 0.252 & 0.023 & 0.079 & 0.224 & 0.043 & 0.175 & 0.219 \\
129	& Verbosity & 0.146 & 0.051 & 0.112 & 0.343 & $5.0{\times}10^{-6}$ & 0.013 & 0.222 \\
130	& Position & 0.584 & $5.9{\times}10^{-9}$ & 0.004 & $-0.011$ & 0.909 & 0.917 & 0.329 \\
131	& Authority & 0.195 & $2.0{\times}10^{-3}$ & 0.031 & 0.261 & $3.6{\times}10^{-5}$ & 0.046 & 0.181 \\
132	\midrule
133	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{10/12} & \\
134	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{4/12} & \multicolumn{3}{c}{3/12} & \\
135	\bottomrule
136	\end{tabular}
137	\caption{Per-condition regression results at $K{=}3$ (455 panels, 15 models). $\hat{\beta}_{\mathrm{std}}$: standardized OLS coefficient. Boot $p$: wild cluster bootstrap max-$p$ (Rademacher, $B{=}9{,}999$). $R^2$: OLS model fit. FDR significance uses BH correction at $\alpha{=}0.05$. Two $K_{\mathrm{eff}}$ exceptions at $K{=}3$ (score manipulation and authority bias on MMLU) show near-zero coefficients ($\hat{\beta}_{\mathrm{std}}{<}0.04$), indicating that these attacks target individual judge capability rather than exploiting inter-judge independence.}
138	\label{tab:percond_k3}
139	\end{table*}
140	
141	\begin{table*}[t]
142	\centering
143	\footnotesize
144	\setlength{\tabcolsep}{3pt}
145	\begin{tabular}{llccccccc}
146	\toprule
147	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
148	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
149	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
150	\midrule
151	\multirow{6}{*}{MMLU} & Prompt inj. & 0.493 & ${<}10^{-15}$ & 0.002 & 0.370 & ${<}10^{-15}$ & 0.033 & 0.594 \\
152	& Sycophancy & 0.321 & ${<}10^{-15}$ & 0.010 & 0.349 & ${<}10^{-15}$ & 0.028 & 0.325 \\
153	& Score manip. & 0.506 & ${<}10^{-15}$ & 0.003 & 0.075 & 0.001 & 0.620 & 0.297 \\
154	& Verbosity & 0.235 & ${<}10^{-15}$ & 0.005 & 0.445 & ${<}10^{-15}$ & 0.005 & 0.358 \\
155	& Position & 0.149 & ${<}10^{-8}$ & 0.077 & 0.333 & ${<}10^{-15}$ & 0.063 & 0.182 \\
156	& Authority & 0.075 & $3.5{\times}10^{-3}$ & 0.314 & 0.203 & ${<}10^{-10}$ & 0.277 & 0.061 \\
157	\addlinespace
158	\multirow{6}{*}{ARC} & Prompt inj. & 0.583 & ${<}10^{-15}$ & 0.018 & $-0.038$ & 0.095 & 0.746 & 0.327 \\
159	& Sycophancy & $-0.157$ & ${<}10^{-8}$ & 0.172 & 0.374 & ${<}10^{-15}$ & 0.011 & 0.078 \\
160	& Score manip. & 0.443 & ${<}10^{-15}$ & 0.004 & $-0.026$ & 0.274 & 0.912 & 0.189 \\
161	& Verbosity & 0.215 & ${<}10^{-12}$ & 0.100 & 0.276 & ${<}10^{-15}$ & 0.058 & 0.178 \\
162	& Position & 0.881 & ${<}10^{-15}$ & 0.017 & $-0.348$ & ${<}10^{-15}$ & 0.796 & 0.512 \\
163	& Authority & 0.264 & ${<}10^{-15}$ & 0.151 & 0.146 & ${<}10^{-5}$ & 0.342 & 0.120 \\
164	\midrule
165	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{11/12} & \\
166	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{7/12} & \multicolumn{3}{c}{2/12} & \\
167	\bottomrule
168	\end{tabular}
169	\caption{Per-condition regression results at $K{=}5$ (3{,}003 panels, 15 models). Format identical to Table~\ref{tab:percond_k3}. $K_{\mathrm{eff}}$ achieves bootstrap significance in 7/12 conditions with consistently larger effect sizes than at $K{=}3$ (mean $|\hat{\beta}_{\mathrm{std}}|$: 0.361 vs.\ 0.196). $\eta_{\max}$'s bootstrap significance drops to 2/12, with three conditions showing negative coefficients---the predictor shift documented in \S\ref{sec:cross_k}.}
170	\label{tab:percond_k5}
171	\end{table*}
172	
173	\begin{table*}[t]
174	\centering
175	\footnotesize
176	\setlength{\tabcolsep}{3pt}
177	\begin{tabular}{llccccccc}
178	\toprule
179	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
180	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
181	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
182	\midrule
183	\multirow{6}{*}{MMLU} & Prompt inj. & 0.574 & ${<}10^{-15}$ & 0.002 & 0.288 & ${<}10^{-15}$ & 0.092 & 0.540 \\
184	& Sycophancy & 0.329 & ${<}10^{-15}$ & 0.017 & 0.266 & ${<}10^{-15}$ & 0.060 & 0.258 \\
185	& Score manip. & 0.605 & ${<}10^{-15}$ & 0.007 & $-0.081$ & ${<}10^{-3}$ & 0.581 & 0.333 \\
186	& Verbosity & 0.204 & ${<}10^{-15}$ & 0.006 & 0.435 & ${<}10^{-15}$ & 0.013 & 0.319 \\
187	& Position & 0.231 & ${<}10^{-15}$ & 0.071 & 0.279 & ${<}10^{-15}$ & 0.110 & 0.186 \\
188	& Authority & 0.005 & 0.722 & 0.905 & 0.116 & ${<}10^{-6}$ & 0.268 & 0.014 \\
189	\addlinespace
190	\multirow{6}{*}{ARC} & Prompt inj. & 0.611 & ${<}10^{-15}$ & 0.063 & $-0.091$ & ${<}10^{-4}$ & 0.237 & 0.337 \\
191	& Sycophancy & $-0.176$ & ${<}10^{-12}$ & 0.326 & 0.372 & ${<}10^{-15}$ & 0.016 & 0.064 \\
192	& Score manip. & 0.316 & ${<}10^{-15}$ & 0.009 & 0.052 & $1.7{\times}10^{-2}$ & 0.539 & 0.112 \\
193	& Verbosity & 0.253 & ${<}10^{-15}$ & 0.044 & 0.238 & ${<}10^{-15}$ & 0.024 & 0.176 \\
194	& Position & 0.831 & ${<}10^{-15}$ & 0.029 & $-0.327$ & ${<}10^{-15}$ & 0.468 & 0.523 \\
195	& Authority & 0.268 & ${<}10^{-15}$ & 0.231 & 0.074 & $2.3{\times}10^{-3}$ & 0.846 & 0.092 \\
196	\midrule
197	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{11/12} & \\
198	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{8/12} & \multicolumn{3}{c}{1/12} & \\
199	\bottomrule
200	\end{tabular}
201	\caption{Per-condition regression results at $K{=}7$ (6{,}435 panels, 15 models). Format identical to Table~\ref{tab:percond_k3}. $K_{\mathrm{eff}}$ bootstrap significance reaches 8/12 (vs.\ 4/12 at $K{=}3$), completing the predictor shift. $\eta_{\max}$ drops to 1/12 bootstrap significance, with its coefficient crossing zero in 3/12 conditions. ARC position bias shows the strongest $K_{\mathrm{eff}}$ coefficient ($\hat{\beta}_{\mathrm{std}}{=}0.831$) and the strongest negative $\eta_{\max}$ coefficient ($-0.327$), a pattern present across all three $K$ values.}
202	\label{tab:percond_k7}
203	\end{table*}
204	
205	\subsection{Model Capability and Vulnerability Profiles}
206	\label{app:model_profiles}
207	
208	\begin{figure}[h]
209	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6b5114aa-2c49-4259-9401-d79eff52cc4d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\\caption{Per-condition predictor dominance across panel sizes (wild cluster bootstrap, BH FDR $\\alpha{=}0.05$). At $K{=}3$, dominance is heterogeneous (co-dominant, $K_{\\mathrm{eff}}$-only, $\\eta_{\\max}$-only, and non-significant conditions coexist); at $K{\\geq}5$, $K_{\\mathrm{eff}}$ dominates uniformly while $\\eta_{\\max}$ diminishes substantially.}\n\\label{fig:dominance_heatmap}\n\\end{figure}\n\n\\subsection{Per-Condition Regression Results}\n\\label{app:per_condition_regression}\n\nTables~\\ref{tab:percond_k3}--\\ref{tab:percond_k7} report the full per-condition regression results underlying the significance counts in the main text. For each of 12 conditions (2 benchmarks $\\times$ 6 attacks), we report the standardized OLS coefficients ($\\hat{\\beta}_{\\mathrm{std}}$), $R^2$, and wild cluster bootstrap $p$-values (max-$p$ across $K$ position clusters, BH FDR $\\alpha{=}0.05$).\n\n\\begin{table*}[t]\n\\centering\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccccc}\n\\toprule\n& & \\multicolumn{3}{c}{$\\boldsymbol{K_{\\mathrm{eff}}}$} & \\multicolumn{3}{c}{$\\boldsymbol{\\eta_{\\max}}$} & \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Bench.} & \\textbf{Attack} & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\\\\n\\midrule\n\\multirow{6}{*}{MMLU} & Prompt inj. & 0.252 & $1.6{\\times}10^{-10}$ & 0.026 & 0.616 & $7.4{\\times}10^{-46}$ & 0.003 & 0.663 \\\\\n& Sycophancy & 0.166 & $1.2{\\times}10^{-4}$ & 0.045 & 0.486 & $1.2{\\times}10^{-26}$ & 0.012 & 0.334 \\\\\n& Score manip. & 0.033 & 0.607 & 0.689 & 0.598 & $3.6{\\times}10^{-19}$ & 0.005 & 0.390 \\\\\n& Verbosity & 0.090 & 0.026 & 0.175 & 0.593 & $4.0{\\times}10^{-40}$ & 0.001 & 0.407 \\\\\n& Position & 0.104 & 0.057 & 0.117 & 0.418 & $1.1{\\times}10^{-13}$ & 0.023 & 0.243 \\\\\n& Authority & 0.010 & 0.852 & 0.864 & 0.377 & $3.4{\\times}10^{-11}$ & 0.008 & 0.147 \\\\\n\\addlinespace\n\\multirow{6}{*}{ARC} & Prompt inj. & 0.330 & $6.4{\\times}10^{-6}$ & 0.015 & 0.244 & $8.0{\\times}10^{-4}$ & 0.092 & 0.303 \\\\\n& Sycophancy & $-0.192$ & $6.3{\\times}10^{-3}$ & 0.023 & 0.492 & $6.7{\\times}10^{-12}$ & 0.001 & 0.132 \\\\\n& Score manip. & 0.252 & 0.023 & 0.079 & 0.224 & 0.043 & 0.175 & 0.219 \\\\\n& Verbosity & 0.146 & 0.051 & 0.112 & 0.343 & $5.0{\\times}10^{-6}$ & 0.013 & 0.222 \\\\\n& Position & 0.584 & $5.9{\\times}10^{-9}$ & 0.004 & $-0.011$ & 0.909 & 0.917 & 0.329 \\\\\n& Authority & 0.195 & $2.0{\\times}10^{-3}$ & 0.031 & 0.261 & $3.6{\\times}10^{-5}$ & 0.046 & 0.181 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{10/12} & \\\\\n\\multicolumn{2}{l}{\\textbf{FDR sig (bootstrap)}} & \\multicolumn{3}{c}{4/12} & \\multicolumn{3}{c}{3/12} & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-condition regression results at $K{=}3$ (455 panels, 15 models). $\\hat{\\beta}_{\\mathrm{std}}$: standardized OLS coefficient. Boot $p$: wild cluster bootstrap max-$p$ (Rademacher, $B{=}9{,}999$). $R^2$: OLS model fit. FDR significance uses BH correction at $\\alpha{=}0.05$. Two $K_{\\mathrm{eff}}$ exceptions at $K{=}3$ (score manipulation and authority bias on MMLU) show near-zero coefficients ($\\hat{\\beta}_{\\mathrm{std}}{<}0.04$), indicating that these attacks target individual judge capability rather than exploiting inter-judge independence.}\n\\label{tab:percond_k3}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccccc}\n\\toprule\n& & \\multicolumn{3}{c}{$\\boldsymbol{K_{\\mathrm{eff}}}$} & \\multicolumn{3}{c}{$\\boldsymbol{\\eta_{\\max}}$} & \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Bench.} & \\textbf{Attack} & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\\\\n\\midrule\n\\multirow{6}{*}{MMLU} & Prompt inj. & 0.493 & ${<}10^{-15}$ & 0.002 & 0.370 & ${<}10^{-15}$ & 0.033 & 0.594 \\\\\n& Sycophancy & 0.321 & ${<}10^{-15}$ & 0.010 & 0.349 & ${<}10^{-15}$ & 0.028 & 0.325 \\\\\n& Score manip. & 0.506 & ${<}10^{-15}$ & 0.003 & 0.075 & 0.001 & 0.620 & 0.297 \\\\\n& Verbosity & 0.235 & ${<}10^{-15}$ & 0.005 & 0.445 & ${<}10^{-15}$ & 0.005 & 0.358 \\\\\n& Position & 0.149 & ${<}10^{-8}$ & 0.077 & 0.333 & ${<}10^{-15}$ & 0.063 & 0.182 \\\\\n& Authority & 0.075 & $3.5{\\times}10^{-3}$ & 0.314 & 0.203 & ${<}10^{-10}$ & 0.277 & 0.061 \\\\\n\\addlinespace\n\\multirow{6}{*}{ARC} & Prompt inj. & 0.583 & ${<}10^{-15}$ & 0.018 & $-0.038$ & 0.095 & 0.746 & 0.327 \\\\\n& Sycophancy & $-0.157$ & ${<}10^{-8}$ & 0.172 & 0.374 & ${<}10^{-15}$ & 0.011 & 0.078 \\\\\n& Score manip. & 0.443 & ${<}10^{-15}$ & 0.004 & $-0.026$ & 0.274 & 0.912 & 0.189 \\\\\n& Verbosity & 0.215 & ${<}10^{-12}$ & 0.100 & 0.276 & ${<}10^{-15}$ & 0.058 & 0.178 \\\\\n& Position & 0.881 & ${<}10^{-15}$ & 0.017 & $-0.348$ & ${<}10^{-15}$ & 0.796 & 0.512 \\\\\n& Authority & 0.264 & ${<}10^{-15}$ & 0.151 & 0.146 & ${<}10^{-5}$ & 0.342 & 0.120 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{11/12} & \\\\\n\\multicolumn{2}{l}{\\textbf{FDR sig (bootstrap)}} & \\multicolumn{3}{c}{7/12} & \\multicolumn{3}{c}{2/12} & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-condition regression results at $K{=}5$ (3{,}003 panels, 15 models). Format identical to Table~\\ref{tab:percond_k3}. $K_{\\mathrm{eff}}$ achieves bootstrap significance in 7/12 conditions with consistently larger effect sizes than at $K{=}3$ (mean $|\\hat{\\beta}_{\\mathrm{std}}|$: 0.361 vs.\\ 0.196). $\\eta_{\\max}$'s bootstrap significance drops to 2/12, with three conditions showing negative coefficients---the predictor shift documented in \\S\\ref{sec:cross_k}.}\n\\label{tab:percond_k5}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccccc}\n\\toprule\n& & \\multicolumn{3}{c}{$\\boldsymbol{K_{\\mathrm{eff}}}$} & \\multicolumn{3}{c}{$\\boldsymbol{\\eta_{\\max}}$} & \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Bench.} & \\textbf{Attack} & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\\\\n\\midrule\n\\multirow{6}{*}{MMLU} & Prompt inj. & 0.574 & ${<}10^{-15}$ & 0.002 & 0.288 & ${<}10^{-15}$ & 0.092 & 0.540 \\\\\n& Sycophancy & 0.329 & ${<}10^{-15}$ & 0.017 & 0.266 & ${<}10^{-15}$ & 0.060 & 0.258 \\\\\n& Score manip. & 0.605 & ${<}10^{-15}$ & 0.007 & $-0.081$ & ${<}10^{-3}$ & 0.581 & 0.333 \\\\\n& Verbosity & 0.204 & ${<}10^{-15}$ & 0.006 & 0.435 & ${<}10^{-15}$ & 0.013 & 0.319 \\\\\n& Position & 0.231 & ${<}10^{-15}$ & 0.071 & 0.279 & ${<}10^{-15}$ & 0.110 & 0.186 \\\\\n& Authority & 0.005 & 0.722 & 0.905 & 0.116 & ${<}10^{-6}$ & 0.268 & 0.014 \\\\\n\\addlinespace\n\\multirow{6}{*}{ARC} & Prompt inj. & 0.611 & ${<}10^{-15}$ & 0.063 & $-0.091$ & ${<}10^{-4}$ & 0.237 & 0.337 \\\\\n& Sycophancy & $-0.176$ & ${<}10^{-12}$ & 0.326 & 0.372 & ${<}10^{-15}$ & 0.016 & 0.064 \\\\\n& Score manip. & 0.316 & ${<}10^{-15}$ & 0.009 & 0.052 & $1.7{\\times}10^{-2}$ & 0.539 & 0.112 \\\\\n& Verbosity & 0.253 & ${<}10^{-15}$ & 0.044 & 0.238 & ${<}10^{-15}$ & 0.024 & 0.176 \\\\\n& Position & 0.831 & ${<}10^{-15}$ & 0.029 & $-0.327$ & ${<}10^{-15}$ & 0.468 & 0.523 \\\\\n& Authority & 0.268 & ${<}10^{-15}$ & 0.231 & 0.074 & $2.3{\\times}10^{-3}$ & 0.846 & 0.092 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{11/12} & \\\\\n\\multicolumn{2}{l}{\\textbf{FDR sig (bootstrap)}} & \\multicolumn{3}{c}{8/12} & \\multicolumn{3}{c}{1/12} & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-condition regression results at $K{=}7$ (6{,}435 panels, 15 models). Format identical to Table~\\ref{tab:percond_k3}. $K_{\\mathrm{eff}}$ bootstrap significance reaches 8/12 (vs.\\ 4/12 at $K{=}3$), completing the predictor shift. $\\eta_{\\max}$ drops to 1/12 bootstrap significance, with its coefficient crossing zero in 3/12 conditions. ARC position bias shows the strongest $K_{\\mathrm{eff}}$ coefficient ($\\hat{\\beta}_{\\mathrm{std}}{=}0.831$) and the strongest negative $\\eta_{\\max}$ coefficient ($-0.327$), a pattern present across all three $K$ values.}\n\\label{tab:percond_k7}\n\\end{table*}\n\n\\subsection{Model Capability and Vulnerability Profiles}\n\\label{app:model_profiles}\n\n\\begin{figure}[h]\n\\centering",
      "numLines": 110,
      "startLine": 100,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Read · `toolu_01G3To9RuMYXA3ejyCg3esQb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 1100,
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
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "ddd87fd9-3ff6-4417-85a2-7b2bc3a703dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANuQVd9KsM3S7nQqbAcj5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5458,
      "cache_creation_input_tokens": 4140,
      "cache_read_input_tokens": 30022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4140
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

_source line 62 · 2026-05-25T21:07:17.132Z_

<details><summary>↩ Tool result · `toolu_01G3To9RuMYXA3ejyCg3esQb`</summary>

```text
1100	\end{tabular}
1101	\end{table}
1102	
1103	At $K{=}3$ and $K{=}5$, WCB significance is preserved or improved after filtering (3$\to$4 and 7$\to$7), and the mean standardized $\beta_{K_{\mathrm{eff}}}$ \emph{increases} from 0.349 to 0.480 ($K{=}3$) and from 0.437 to 0.512 ($K{=}5$), indicating that the diversity--vulnerability association is stronger, not weaker, without near-chance models. Fractional logit significance likewise improves after filtering at every $K$ (8$\to$9, 10$\to$11, 10$\to$11), confirming that the effect is not an artifact of the GLM specification. At $K{=}7$, WCB significance drops from 8/12 to 2/12; however, the combinatorial filtering removes 73.3\% of panels (6{,}435$\to$1{,}716), substantially reducing statistical power for the conservative bootstrap test. The raw WCB $p$-values at $K{=}7$ cluster in the 0.02--0.15 range rather than reversing sign, and the standardized coefficient remains positive ($\bar{\beta}_{\mathrm{std}}{=}0.385$). The $K{=}7$ attenuation is therefore attributable to power loss from the sample reduction rather than absence of a genuine effect.
1104	
1105	In contrast, $\eta_{\max}$ WCB significance drops sharply after filtering (4$\to$1, 2$\to$0, 1$\to$0 at $K{=}3/5/7$), indicating that the near-chance models contribute disproportionately to the $\eta_{\max}$--ASR association: their high individual vulnerability inflates both $\eta_{\max}$ variation and the corresponding WCB significance. Overall, the $K_{\mathrm{eff}}$--ASR association is robust to excluding near-chance models at all panel sizes, while $\eta_{\max}$ is not.
1106	
1107	\section{Panel Composition Analysis}
1108	\label{app:panel_composition}
1109	
1110	\begin{figure*}[t]
1111	\centering
1112	\includegraphics[width=\textwidth]{figures/fig_panel_composition.pdf}
1113	\caption{API model fraction vs.\ panel ASR heatmap across attack types ($K{=}5$, $n{=}3{,}003$ panels). Each cell shows the mean ASR for panels with a given API model fraction. All-API panels (fraction${=}1.0$) achieve the lowest ASR for most attacks, but mixed-composition panels show heterogeneous vulnerability patterns not captured by API fraction alone.}
1114	\label{fig:panel_composition}
1115	\end{figure*}
1116	
1117	The composition heatmap (Figure~\ref{fig:panel_composition}) connects the abstract $K_{\mathrm{eff}}$--ASR relationship to concrete panel design choices. The gradient from high-API to low-API panels reveals that capability concentration (all API models) does not uniformly minimize vulnerability: for position bias, all-API panels show ASR comparable to mixed panels, consistent with the structural nature of this attack. The heatmap also illustrates why the diversity--capability confound is difficult to break: high-API panels simultaneously achieve low $\eta_{\max}$ and low $K_{\mathrm{eff}}$, conflating the two predictors.
1118	
1119	\subsection{Regression Coefficient Trajectories}
1120	\label{app:beta_trajectory}
1121	
1122	\begin{figure}[h]
1123	\centering
1124	\includegraphics[width=\columnwidth]{figures/fig_beta_trajectory.pdf}
1125	\caption{Standardized regression coefficient ($\hat{\beta}_{\mathrm{std}}$) trajectories with 95\% CI bands across panel sizes ($K \in \{3, 5, 7\}$) from meta-analytic pooling (DerSimonian--Laird). $K_{\mathrm{eff}}$ (blue) maintains positive coefficients across all $K$; $\eta_{\max}$ (orange) declines monotonically, with the CI crossing zero at $K{\geq}5$.}
1126	\label{fig:beta_trajectory}
1127	\end{figure}
1128	
1129	The trajectory plot (Figure~\ref{fig:beta_trajectory}) provides a visual summary of the paper's central finding: the diminishing weakest link. The $\eta_{\max}$ pooled coefficient shrinks from $\hat{\beta}_{\mathrm{std}}{=}0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$, while $K_{\mathrm{eff}}$ remains stable ($0.356$--$0.436$). The $K^*$ crossover between the two predictors occurs in the interval $(3, 5)$, coinciding with the power threshold where $K_{\mathrm{eff}}$'s MDE drops below the observed effect size (Table~\ref{tab:mde}).
1130	
1131	\subsection{Condorcet Jury Theorem: Adversarial Failure Analysis}
1132	\label{app:cjt_failure}
1133	
1134	The Condorcet Jury Theorem (CJT) \citep{condorcet1785essai} guarantees that majority voting accuracy converges to 1 as $K \to \infty$ when individual voter accuracy exceeds 0.5 and votes are independent. Our experimental setting violates both assumptions under adversarial manipulation, and the nature of the violation is informative.
1135	
1136	\paragraph{Independence Violation.} CJT assumes conditionally independent errors. Under adaptive attack, the adversary exploits shared vulnerabilities, inducing positive error correlations. The MI heatmap (Figure~\ref{fig:mi_heatmap}) shows that within-family judge pairs exhibit 2--3$\times$ higher MI than cross-family pairs even under clean conditions; under attack, these correlations intensify for susceptible judge pairs. The effective number of independent votes is $K_{\mathrm{eff}} < K$, meaning the CJT convergence rate is governed by $K_{\mathrm{eff}}$ rather than $K$.
1137	
1138	\paragraph{Accuracy Violation.} CJT requires individual accuracy ${>}0.5$. Under adversarial manipulation, susceptible judges can have accuracy below this threshold. Claude 3 Haiku under prompt injection shows ASR${=}0.817$ on MMLU---equivalently, accuracy of 0.183 on attacked pairs, well below 0.5. When panels contain such judges, the CJT prediction inverts: majority voting can \emph{amplify} rather than correct errors, because multiple susceptible judges can form a manipulated majority.
1139	
1140	\paragraph{The BFT Reversal.} Classical Byzantine Fault Tolerance \citep{lamport1982byzantine} tolerates up to $\lfloor(K-1)/3\rfloor$ faulty nodes under non-strategic faults. Under adaptive adversarial manipulation, the ``faulty'' judges are not random but strategically targeted. The positive $K_{\mathrm{eff}}$--ASR association reverses the BFT intuition: more independent channels create more distinct attack surfaces rather than redundant defenses. Table~\ref{tab:bft_comparison} formalizes this contrast.
1141	
1142	\begin{table}[h]
1143	\centering
1144	\small
1145	\begin{tabular}{lcc}
1146	\toprule
1147	\textbf{Property} & \textbf{CJT/BFT} & \textbf{Adversarial} \\
1148	\midrule
1149	Fault model & Random, i.i.d. & Strategic, adaptive \\
1150	Independence & Protective & Creates attack surfaces \\
1151	$K$ effect & Monotone benefit & Diminishing benefit \\
1152	Diversity & Unconditionally helpful & Confounded with capability \\
1153	Aggregation & Majority optimal & Bayesian partially neutralizes \\
1154	Convergence & $\to 1$ as $K \to \infty$ & Bounded by $\eta_{\max}$ \\
1155	\bottomrule
1156	\end{tabular}
1157	\caption{CJT/BFT vs.\ adversarial setting comparison. Under adversarial manipulation, the protective properties of independence and panel size are weakened or reversed.}
1158	\label{tab:bft_comparison}
1159	\end{table}
1160	
1161	\paragraph{Empirical Quantification.} The random fault contrast (\S\ref{sec:rf_contrast}) directly quantifies the CJT--adversarial gap. Under random faults (CJT-like conditions), $R^2{=}0.730$ and $K_{\mathrm{eff}}$ is significant in 2/2 benchmark conditions, confirming that panel composition strongly predicts error rates when faults are independent. Under adaptive attack, $R^2$ drops to 0.285 ($\Delta{=}0.446$), but $K_{\mathrm{eff}}$ retains positive association (7/12 conditions), indicating that the CJT mechanism is weakened but not eliminated. The residual CJT-like protection arises because not all judges are susceptible to all attacks: heterogeneous vulnerability profiles create a form of ``accidental independence'' even under strategic manipulation. This partial survival of the CJT mechanism explains why larger panels still provide some protection ($K_{\mathrm{eff}}$'s positive direction is 12/12 across all methods and panel sizes), but the benefit is substantially diminished relative to the non-adversarial prediction.
1162	
1163	\paragraph{Correlated Errors.} \citet{ladha1992condorcet} extended the CJT to correlated voters, showing that positive correlation weakens convergence. Our $K_{\mathrm{eff}}$ metric can be interpreted as the CJT-effective panel size: a panel with $K{=}7$ judges but $K_{\mathrm{eff}}{=}4.5$ behaves, for convergence purposes, like 4.5 independent voters. The sublinear $K_{\mathrm{eff}}/K$ ratio (0.73, 0.67, 0.65 at $K{=}3,5,7$; Table~\ref{tab:keff_dist}) quantifies the cost of inter-judge correlation in the LLM ecosystem. Each additional judge provides diminishing independence returns, consistent with the family-clustered MI structure (Appendix~\ref{app:mi_structure}).
1164	
1165	\subsection{Practical Panel Design Guidelines}
1166	\label{app:panel_design_guide}
1167	
1168	The experimental findings translate into concrete recommendations for practitioners designing multi-judge evaluation panels. Table~\ref{tab:design_guide} summarizes the key design parameters and their empirical support.
1169	
1170	\begin{table*}[t]
1171	\centering
1172	\small
1173	\begin{tabular}{p{3.2cm}p{5cm}p{5cm}}
1174	\toprule
1175	\textbf{Design choice} & \textbf{Recommendation} & \textbf{Empirical support} \\
1176	\midrule
1177	Panel size ($K$) & $K{\geq}5$ for robustness benefits; $K{=}7$ for strongest diversity signal & $K_{\mathrm{eff}}$ significance: 4/12 ($K{=}3$) $\to$ 7/12 ($K{=}5$) $\to$ 8/12 ($K{=}7$); MDE drops from 0.144 to 0.036 \\
1178	\addlinespace
1179	Model selection & Cross-family diversity with capability floor $\eta_j{<}0.15$ & $\min(\eta_{\max})$ optimal in 12/12 conditions; near-chance exclusion strengthens $K_{\mathrm{eff}}$ signal \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "9847e0a3-961a-4f9c-8df3-a93fc9e35b89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\\end{tabular}\n\\end{table}\n\nAt $K{=}3$ and $K{=}5$, WCB significance is preserved or improved after filtering (3$\\to$4 and 7$\\to$7), and the mean standardized $\\beta_{K_{\\mathrm{eff}}}$ \\emph{increases} from 0.349 to 0.480 ($K{=}3$) and from 0.437 to 0.512 ($K{=}5$), indicating that the diversity--vulnerability association is stronger, not weaker, without near-chance models. Fractional logit significance likewise improves after filtering at every $K$ (8$\\to$9, 10$\\to$11, 10$\\to$11), confirming that the effect is not an artifact of the GLM specification. At $K{=}7$, WCB significance drops from 8/12 to 2/12; however, the combinatorial filtering removes 73.3\\% of panels (6{,}435$\\to$1{,}716), substantially reducing statistical power for the conservative bootstrap test. The raw WCB $p$-values at $K{=}7$ cluster in the 0.02--0.15 range rather than reversing sign, and the standardized coefficient remains positive ($\\bar{\\beta}_{\\mathrm{std}}{=}0.385$). The $K{=}7$ attenuation is therefore attributable to power loss from the sample reduction rather than absence of a genuine effect.\n\nIn contrast, $\\eta_{\\max}$ WCB significance drops sharply after filtering (4$\\to$1, 2$\\to$0, 1$\\to$0 at $K{=}3/5/7$), indicating that the near-chance models contribute disproportionately to the $\\eta_{\\max}$--ASR association: their high individual vulnerability inflates both $\\eta_{\\max}$ variation and the corresponding WCB significance. Overall, the $K_{\\mathrm{eff}}$--ASR association is robust to excluding near-chance models at all panel sizes, while $\\eta_{\\max}$ is not.\n\n\\section{Panel Composition Analysis}\n\\label{app:panel_composition}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_panel_composition.pdf}\n\\caption{API model fraction vs.\\ panel ASR heatmap across attack types ($K{=}5$, $n{=}3{,}003$ panels). Each cell shows the mean ASR for panels with a given API model fraction. All-API panels (fraction${=}1.0$) achieve the lowest ASR for most attacks, but mixed-composition panels show heterogeneous vulnerability patterns not captured by API fraction alone.}\n\\label{fig:panel_composition}\n\\end{figure*}\n\nThe composition heatmap (Figure~\\ref{fig:panel_composition}) connects the abstract $K_{\\mathrm{eff}}$--ASR relationship to concrete panel design choices. The gradient from high-API to low-API panels reveals that capability concentration (all API models) does not uniformly minimize vulnerability: for position bias, all-API panels show ASR comparable to mixed panels, consistent with the structural nature of this attack. The heatmap also illustrates why the diversity--capability confound is difficult to break: high-API panels simultaneously achieve low $\\eta_{\\max}$ and low $K_{\\mathrm{eff}}$, conflating the two predictors.\n\n\\subsection{Regression Coefficient Trajectories}\n\\label{app:beta_trajectory}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_beta_trajectory.pdf}\n\\caption{Standardized regression coefficient ($\\hat{\\beta}_{\\mathrm{std}}$) trajectories with 95\\% CI bands across panel sizes ($K \\in \\{3, 5, 7\\}$) from meta-analytic pooling (DerSimonian--Laird). $K_{\\mathrm{eff}}$ (blue) maintains positive coefficients across all $K$; $\\eta_{\\max}$ (orange) declines monotonically, with the CI crossing zero at $K{\\geq}5$.}\n\\label{fig:beta_trajectory}\n\\end{figure}\n\nThe trajectory plot (Figure~\\ref{fig:beta_trajectory}) provides a visual summary of the paper's central finding: the diminishing weakest link. The $\\eta_{\\max}$ pooled coefficient shrinks from $\\hat{\\beta}_{\\mathrm{std}}{=}0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$, while $K_{\\mathrm{eff}}$ remains stable ($0.356$--$0.436$). The $K^*$ crossover between the two predictors occurs in the interval $(3, 5)$, coinciding with the power threshold where $K_{\\mathrm{eff}}$'s MDE drops below the observed effect size (Table~\\ref{tab:mde}).\n\n\\subsection{Condorcet Jury Theorem: Adversarial Failure Analysis}\n\\label{app:cjt_failure}\n\nThe Condorcet Jury Theorem (CJT) \\citep{condorcet1785essai} guarantees that majority voting accuracy converges to 1 as $K \\to \\infty$ when individual voter accuracy exceeds 0.5 and votes are independent. Our experimental setting violates both assumptions under adversarial manipulation, and the nature of the violation is informative.\n\n\\paragraph{Independence Violation.} CJT assumes conditionally independent errors. Under adaptive attack, the adversary exploits shared vulnerabilities, inducing positive error correlations. The MI heatmap (Figure~\\ref{fig:mi_heatmap}) shows that within-family judge pairs exhibit 2--3$\\times$ higher MI than cross-family pairs even under clean conditions; under attack, these correlations intensify for susceptible judge pairs. The effective number of independent votes is $K_{\\mathrm{eff}} < K$, meaning the CJT convergence rate is governed by $K_{\\mathrm{eff}}$ rather than $K$.\n\n\\paragraph{Accuracy Violation.} CJT requires individual accuracy ${>}0.5$. Under adversarial manipulation, susceptible judges can have accuracy below this threshold. Claude 3 Haiku under prompt injection shows ASR${=}0.817$ on MMLU---equivalently, accuracy of 0.183 on attacked pairs, well below 0.5. When panels contain such judges, the CJT prediction inverts: majority voting can \\emph{amplify} rather than correct errors, because multiple susceptible judges can form a manipulated majority.\n\n\\paragraph{The BFT Reversal.} Classical Byzantine Fault Tolerance \\citep{lamport1982byzantine} tolerates up to $\\lfloor(K-1)/3\\rfloor$ faulty nodes under non-strategic faults. Under adaptive adversarial manipulation, the ``faulty'' judges are not random but strategically targeted. The positive $K_{\\mathrm{eff}}$--ASR association reverses the BFT intuition: more independent channels create more distinct attack surfaces rather than redundant defenses. Table~\\ref{tab:bft_comparison} formalizes this contrast.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Property} & \\textbf{CJT/BFT} & \\textbf{Adversarial} \\\\\n\\midrule\nFault model & Random, i.i.d. & Strategic, adaptive \\\\\nIndependence & Protective & Creates attack surfaces \\\\\n$K$ effect & Monotone benefit & Diminishing benefit \\\\\nDiversity & Unconditionally helpful & Confounded with capability \\\\\nAggregation & Majority optimal & Bayesian partially neutralizes \\\\\nConvergence & $\\to 1$ as $K \\to \\infty$ & Bounded by $\\eta_{\\max}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CJT/BFT vs.\\ adversarial setting comparison. Under adversarial manipulation, the protective properties of independence and panel size are weakened or reversed.}\n\\label{tab:bft_comparison}\n\\end{table}\n\n\\paragraph{Empirical Quantification.} The random fault contrast (\\S\\ref{sec:rf_contrast}) directly quantifies the CJT--adversarial gap. Under random faults (CJT-like conditions), $R^2{=}0.730$ and $K_{\\mathrm{eff}}$ is significant in 2/2 benchmark conditions, confirming that panel composition strongly predicts error rates when faults are independent. Under adaptive attack, $R^2$ drops to 0.285 ($\\Delta{=}0.446$), but $K_{\\mathrm{eff}}$ retains positive association (7/12 conditions), indicating that the CJT mechanism is weakened but not eliminated. The residual CJT-like protection arises because not all judges are susceptible to all attacks: heterogeneous vulnerability profiles create a form of ``accidental independence'' even under strategic manipulation. This partial survival of the CJT mechanism explains why larger panels still provide some protection ($K_{\\mathrm{eff}}$'s positive direction is 12/12 across all methods and panel sizes), but the benefit is substantially diminished relative to the non-adversarial prediction.\n\n\\paragraph{Correlated Errors.} \\citet{ladha1992condorcet} extended the CJT to correlated voters, showing that positive correlation weakens convergence. Our $K_{\\mathrm{eff}}$ metric can be interpreted as the CJT-effective panel size: a panel with $K{=}7$ judges but $K_{\\mathrm{eff}}{=}4.5$ behaves, for convergence purposes, like 4.5 independent voters. The sublinear $K_{\\mathrm{eff}}/K$ ratio (0.73, 0.67, 0.65 at $K{=}3,5,7$; Table~\\ref{tab:keff_dist}) quantifies the cost of inter-judge correlation in the LLM ecosystem. Each additional judge provides diminishing independence returns, consistent with the family-clustered MI structure (Appendix~\\ref{app:mi_structure}).\n\n\\subsection{Practical Panel Design Guidelines}\n\\label{app:panel_design_guide}\n\nThe experimental findings translate into concrete recommendations for practitioners designing multi-judge evaluation panels. Table~\\ref{tab:design_guide} summarizes the key design parameters and their empirical support.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{p{3.2cm}p{5cm}p{5cm}}\n\\toprule\n\\textbf{Design choice} & \\textbf{Recommendation} & \\textbf{Empirical support} \\\\\n\\midrule\nPanel size ($K$) & $K{\\geq}5$ for robustness benefits; $K{=}7$ for strongest diversity signal & $K_{\\mathrm{eff}}$ significance: 4/12 ($K{=}3$) $\\to$ 7/12 ($K{=}5$) $\\to$ 8/12 ($K{=}7$); MDE drops from 0.144 to 0.036 \\\\\n\\addlinespace\nModel selection & Cross-family diversity with capability floor $\\eta_j{<}0.15$ & $\\min(\\eta_{\\max})$ optimal in 12/12 conditions; near-chance exclusion strengthens $K_{\\mathrm{eff}}$ signal \\\\",
      "numLines": 80,
      "startLine": 1100,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of all the files. Let me also check the per_condition JSON for the diversity_uniformly_positive claim - from the comparison JSON, I can see that `diversity_uniformly_positive_12_of_12` is false for all K values. The new value is 10/12. And from the per-condition data, the position bias conditions have negative K_eff coefficients.

Let me also check the WCB significance counts from the comparison JSON:
- K3: keff_sig=8/12, eta_sig=5/12


- K5: keff_sig=8/12, eta_sig=0/12
- K7: keff_sig=7/12, eta_sig=1/12

So the old WCB trajectory for K_eff was 4→7→8 and new is 8→8→7. Old η_max WCB was 3→2→1 and new is 5→0→1. I need to update these trajectories in the appendix, and I'm also checking the per-condition data for fractional logit where K3 shows keff_sig improved from 9/12 to 10/12 with eta_sig at 8.

Looking at the full per-condition comparison, K5 and K7 both show improvements in keff_sig (from 9/12 to 11/12) but the comparison flags that new_keff_all_positive is false across all conditions, meaning the position bias still produces negative K_eff values. I should review the current appendix tables at K=3 to see what bootstrap numbers are listed there before making my edits. Looking at the per-condition regression tables, I notice the position bias coefficients for MMLU and ARC are substantially different from what the new reanalysis data shows—the old table has positive K_eff values (0.104 for MMLU, 0.584 for ARC) while the new data indicates negative values (-0.334 and -0.372 respectively). The task description doesn't explicitly mention updating these per-condition tables, so I'm uncertain whether they should be revised along with the pooled meta-analytic numbers. The per-condition regression tables in the appendix would need completely new numbers pulled from the JSON data, which is a separate undertaking. Since the task only specifies updating the pooled coefficients and WCB trajectories, I'll stick to those. But I do need to check the bootstrap significance counts at each K value—they should align with the new WCB significance numbers from the comparison data. The per-condition regression coefficients are significantly different from what's currently in the tables—the K_eff and η_max values for both MMLU and ARC Position conditions have changed substantially, along with their R² values. While these tables likely need updating too, the current task focuses on the specific numbers listed, so I'll proceed with those edits and note that the per-condition tables may require a separate update. Let me map out all the changes needed across abstract.tex and the main document. I need to update the bootstrap and fractional logit numbers in the Limitations section since the position bias fix changed the results—bootstrap went from 4/12 to 8/12 and fractional logit from 9/12 to 10/12. Let me verify the OLS K=3 significance is still 12/12 before finalizing these changes. I'm realizing that at K=3, the bootstrap method actually shows strong robustness with 8/12 conditions significant—this is a substantial improvement from the earlier 4/12, suggesting K_eff isn't as method-sensitive as I initially thought. Let me focus on systematically updating all the old numbers to the new values across the files as the task specifies.

I need to go through each .tex file and replace the old numerical values with the new ones. Starting with abstract.tex, I'm updating the convergence metrics from 0.264→0.102→0.084 to 0.243→0.091→0.086, and changing the conditions count from 12/12 to 10/12 where applicable. Though I should verify whether κ-diversity still maintains the 12/12 conditions or if that also changes. I'm looking at the comparison data and seeing that the diversity uniformity claim doesn't hold across all K values. Since the task only specifies changing K_eff to 10 of 12 conditions, I should keep κ-diversity at 12/12 in the abstract and adjust the wording to reflect that K_eff is now the one with the conditional positive direction. I'm going through each location where "12/12 conditions" appears and changing it to "10/12 conditions" to reflect that $K_{\mathrm{eff}}$ only shows positive direction in 10 of the 12 conditions, while $\kappa$-diversity maintains the full 12/12 result. I need to be careful about how I phrase this in the abstract and other sections to avoid claiming uniformly positive results when the data doesn't support that. I need to be careful about which numbers to replace—the per-condition β values in the appendix tables are different from the pooled statistics, so I can't just do a blanket find-and-replace. Let me systematically go through the per-condition tables and update the significance counts: the K=3 table needs 4/12 → 8/12 for K_eff significance and 3/12 → 5/12 for η_max, and I'll need to check the K=5 and K=7 tables similarly. I need to systematically find and update all the old WCB significance counts throughout the document. The key replacements are K_eff bootstrap values (4/12→7/12→8/12) and η_max bootstrap values (3/12→2/12→1/12), but I have to be careful to only change these in the right contexts and not accidentally modify similar numbers appearing elsewhere. Let me start making the edits directly, working through the straightforward number replacements first, then handling the narrative sections, and finally verifying everything with targeted searches. I need to update the abstract with corrected numbers and adjust the language around the diversity findings. The key issue is that K_eff is now 10/12 conditions instead of 12/12, so I can't claim the diversity effect is "uniformly" positive anymore. I'll revise the first claim to say diversity is "predominantly" positively associated, specifying that K_eff shows 10/12 conditions while κ-diversity maintains 12/12. Then I need to update the beta coefficients from 0.264 → 0.102 → 0.084 to 0.243 → 0.091 → 0.086, and change the conditions reference from 12/12 to 10/12. I should keep the changes minimal to avoid exceeding the 200-word limit. I'm finding that the weakest-link metric's influence drops sharply as panel size increases, becoming statistically indistinguishable from zero at larger panels, while the choice of aggregation rule dramatically shifts predictability. However, the strong correlation between diversity and model capability makes it impossible to isolate causal effects—these are purely associational patterns. to be updated with the new values: 0.353 for K_eff K=5 and I need to recalculate what the η_max K=3 value should be based on the corrected data.

I'm also scanning through the appendix to identify all instances that need updating—the meta-analytic table at line 554 definitely needs a full revision, and I found another 0.264 at line 163 in the per-condition Authority table, but that's a different coefficient so I'll leave it alone. At line 1129 there's another reference to the pooled η_max coefficient with a range that needs recalculating. I need to verify the figure caption for the regime transition plot—the η_max significance values need updating from the old trajectory of 3/12 to 2/12, and I'm checking what the new values should be across the different K values shown in the figure. At K=5, I need to update the K_eff values to reflect the new data—bootstrap improves from 7/12 to 8/12, and fractional logit jumps to 11/12. For the confidence intervals on line 45, I'm revising the point estimates and bounds across all three K values, with the intervals getting tighter as K increases.

I also need to figure out the updated I² heterogeneity values—the comparison JSON only has the old ones, so I'll need to check the per_condition data to recalculate using DerSimonian-Laird or mark them as TBD if I can't derive them directly. Looking at the appendix meta table, I need to update the I² values and mark them as TBD since I don't have the recalculated numbers. I'm also noticing some narrative shifts in analysis.tex—the K_eff significance pattern changes from consistently increasing to a different distribution, and the confirmation counts drop from 12/12 to 10/12 for K_eff, which affects how I describe the results.

Now I'm checking the results.tex caption more carefully. It currently claims all 12 conditions show positive direction, but with the position bias fix, K_eff is only positive in 10 out of 12 conditions. I need to update that caption to reflect "positive direction in 10/12 conditions" instead. The underlying table itself will also need its significance counts adjusted to match the new data. Looking at the old table, OLS η_max was significant in 10 out of 12 cases, which aligns with the documented exceptions for score manipulation and position bias. After applying the position bias fix, those exception cases will likely shift, so I need to verify the updated counts and then systematically revise all the pooled estimates—both the β_std values and their confidence intervals for η_max and K_eff—along with any other affected statistics in the main text.

Now I'm tracking down the specific trajectory changes: the WCB results for K_eff shift from 4→7→8 to 8→8→7, while η_max goes from 3→2→1 to 5→0→1. I also need to update the method comparison table to reflect that wild bootstrap now shows 5/12 for η_max and 8/12 for K_eff instead of the previous 3/12 and 4/12. Beyond the numerical updates, I should add a discussion of the position bias findings in the results section and adjust the narrative around these trajectory patterns. Looking at the figure more carefully, I need to understand what's actually being shown across the K values. The caption describes transitions in significance counts, but I should verify whether it's showing K=3→K=5 or K=3→K=7, since the shaded region marks K* ∈ (3,5) and that affects how I interpret the η_max and K_eff changes. (decreasing), so they were opposite trends. But the new K_eff trajectory of 8→8→7 is slightly decreasing now, which means they're no longer opposite. This might affect the Limitations section, though the task doesn't explicitly ask me to address it.

I've got enough analysis now. Let me systematically work through the edits. I need to update the fractional logit numbers in results.tex—specifically changing the K_eff significance statement from "9/12 across all panel sizes" to "10--11/12" since the new values are 10/12, 11/12, and 11/12 for K=3, 5, and 7 respectively. I'll also need to update the per-condition tables in the appendix.

Updating the FDR significance lines across multiple appendix sections with the new bootstrap counts...

but I need to be careful about line 1103, which references a separate near-chance filtering analysis. Those numbers depend on re-running that analysis with the updated position bias corrections, which is beyond the current scope. I should leave that one alone since it's tied to a different pipeline.

Let me focus on the explicit replacements listed in the task and the direct cascading effects. The WCB trajectory and η_max numbers are clearly specified, so I'll update those systematically. I should also add the position bias paragraph as instructed and update the WCB counts where they appear in the text.

For the fractional logit numbers, I can see from the comparison data that values like 9/12 need to change to 10/12 or 11/12 in places like the results section and limitations. I'll update those where the old numbers are explicitly mentioned, but the more comprehensive re-analysis of tables and method comparisons would require deeper changes beyond what's directly specified. I'm seeing that the position bias fix dramatically changes the significance levels—MMLU position bias jumps from non-significant to highly significant (p=5.28e-39), while ARC challenge position bias also becomes highly significant (p=3.65e-20). This means the OLS η_max count at K=3 shifts substantially from the original exceptions, since what was previously marked as non-significant is now clearly significant. I'm looking at the statistical results more carefully now—the p-values shifted significantly when I recalculated, especially for position bias conditions. Rather than getting bogged down in updating all the per-condition tables, I should focus on the specific edits that were requested. My plan is to update the abstract and main text with the corrected numbers: removing "uniformly" from the positivity claim, changing the condition count from 12 to 10, and replacing the three p-value sequences with the new calculations.

For the limitations section, I need to update the bootstrap and fractional logit condition counts, and revise the statement about positive effects across all conditions. The part about operationalization-dependent trends is trickier since K_eff no longer shows the increasing pattern, but I'll leave that unchanged unless explicitly asked to modify it.

Now moving through the introduction and results sections, I'm updating numerical values and trajectories throughout—the significance counts for K_eff, the η_max values, and the bootstrap/fractional logit comparisons across multiple tables and figure captions. Now I'm going through the appendix to update the meta-analytic table with the corrected numbers, revise the trajectory descriptions, and adjust the per-condition summary rows to reflect the WCB counts. There are quite a few scattered mentions throughout that need the 12/12 to 10/12 conversions as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "687da470-bbb9-43b0-b00b-ee301e043e8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MiCnmeQ2L13XgAFz3Q7rBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19192,
      "cache_read_input_tokens": 34162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19192
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

I have all the data I need. Let me now read the specific appendix sections and then start making edits systematically across all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "719b928a-9978-49b3-a9ad-e5f01bdc1a13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MiCnmeQ2L13XgAFz3Q7rBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19192,
      "cache_read_input_tokens": 34162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19192
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

<details open><summary>🔧 Tool call — Read · `toolu_013JSDoMg2rAJ7xpxyDMmGod`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 1075,
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
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "724c1399-d306-47a1-87ee-894779cf8af6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MiCnmeQ2L13XgAFz3Q7rBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19192,
      "cache_read_input_tokens": 34162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19192
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

_source line 66 · 2026-05-25T21:11:21.176Z_

<details><summary>↩ Tool result · `toolu_013JSDoMg2rAJ7xpxyDMmGod`</summary>

```text
1075	\section{Near-Chance Model Sensitivity Analysis}
1076	\label{app:near_chance}
1077	
1078	Two locally-hosted models (Qwen2.5-14B-AWQ, MMLU accuracy 0.253; Qwen2.5-72B-AWQ, 0.333) score near the 4-choice random baseline of 0.25. A natural concern is that the positive association between panel diversity ($K_{\mathrm{eff}}$) and attack success rate is mechanically driven by panels containing near-random judges, which simultaneously inflate both independence and vulnerability.
1079	
1080	We exclude all panels containing either model (MMLU ${<}\,0.35$ threshold), reducing the pool from 15 to 13 models and panel counts from 455/3{,}003/6{,}435 to 286/1{,}287/1{,}716 at $K{=}3/5/7$. We re-run OLS with BH-corrected $p$-values, the wild cluster bootstrap (WCB; $B{=}9{,}999$, Rademacher weights, max-$p$ across $K$ position clusters, BH-adjusted at $\alpha{=}0.05$), and the fractional logit GLM (Binomial, logit link, clustered SE with max-$p$, BH-adjusted). Table~\ref{tab:near_chance} reports FDR-significant $K_{\mathrm{eff}}$ counts out of 12 conditions.
1081	
1082	\begin{table}[h]
1083	\centering
1084	\small
1085	\caption{Near-chance model sensitivity: FDR-significant $K_{\mathrm{eff}}$ conditions out of 12 (2 benchmarks $\times$ 6 attacks). $\bar{\beta}_{\mathrm{std}}$: mean standardized $K_{\mathrm{eff}}$ coefficient across conditions. The full-pool fractional logit count at $K{=}3$ (8/12) differs by $\pm 1$ from Table~\ref{tab:method_comparison} (9/12) due to clustering implementation details in the sensitivity script; this does not affect within-table comparisons.}
1086	\label{tab:near_chance}
1087	\begin{tabular}{llcccccc}
1088	\toprule
1089	$K$ & Panel set & $n$ & OLS & WCB & Frac & $\bar{\beta}_{\mathrm{std}}$ & $\bar{R}^2$ \\
1090	\midrule
1091	3 & Full (15 models) & 455 & 11/12 & 3/12 & 8/12 & 0.349 & 0.340 \\
1092	3 & Filtered (13 models) & 286 & 12/12 & 4/12 & 9/12 & \textbf{0.480} & 0.333 \\
1093	\midrule
1094	5 & Full (15 models) & 3{,}003 & 12/12 & 7/12 & 10/12 & 0.437 & 0.285 \\
1095	5 & Filtered (13 models) & 1{,}287 & 11/12 & 7/12 & 11/12 & \textbf{0.512} & 0.256 \\
1096	\midrule
1097	7 & Full (15 models) & 6{,}435 & 12/12 & 8/12 & 10/12 & 0.401 & 0.244 \\
1098	7 & Filtered (13 models) & 1{,}716 & 11/12 & 2/12 & 11/12 & 0.385 & 0.203 \\
1099	\bottomrule
1100	\end{tabular}
1101	\end{table}
1102	
1103	At $K{=}3$ and $K{=}5$, WCB significance is preserved or improved after filtering (3$\to$4 and 7$\to$7), and the mean standardized $\beta_{K_{\mathrm{eff}}}$ \emph{increases} from 0.349 to 0.480 ($K{=}3$) and from 0.437 to 0.512 ($K{=}5$), indicating that the diversity--vulnerability association is stronger, not weaker, without near-chance models. Fractional logit significance likewise improves after filtering at every $K$ (8$\to$9, 10$\to$11, 10$\to$11), confirming that the effect is not an artifact of the GLM specification. At $K{=}7$, WCB significance drops from 8/12 to 2/12; however, the combinatorial filtering removes 73.3\% of panels (6{,}435$\to$1{,}716), substantially reducing statistical power for the conservative bootstrap test. The raw WCB $p$-values at $K{=}7$ cluster in the 0.02--0.15 range rather than reversing sign, and the standardized coefficient remains positive ($\bar{\beta}_{\mathrm{std}}{=}0.385$). The $K{=}7$ attenuation is therefore attributable to power loss from the sample reduction rather than absence of a genuine effect.
1104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6b9925cf-00d3-4b5e-b864-479b927028c8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\\section{Near-Chance Model Sensitivity Analysis}\n\\label{app:near_chance}\n\nTwo locally-hosted models (Qwen2.5-14B-AWQ, MMLU accuracy 0.253; Qwen2.5-72B-AWQ, 0.333) score near the 4-choice random baseline of 0.25. A natural concern is that the positive association between panel diversity ($K_{\\mathrm{eff}}$) and attack success rate is mechanically driven by panels containing near-random judges, which simultaneously inflate both independence and vulnerability.\n\nWe exclude all panels containing either model (MMLU ${<}\\,0.35$ threshold), reducing the pool from 15 to 13 models and panel counts from 455/3{,}003/6{,}435 to 286/1{,}287/1{,}716 at $K{=}3/5/7$. We re-run OLS with BH-corrected $p$-values, the wild cluster bootstrap (WCB; $B{=}9{,}999$, Rademacher weights, max-$p$ across $K$ position clusters, BH-adjusted at $\\alpha{=}0.05$), and the fractional logit GLM (Binomial, logit link, clustered SE with max-$p$, BH-adjusted). Table~\\ref{tab:near_chance} reports FDR-significant $K_{\\mathrm{eff}}$ counts out of 12 conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Near-chance model sensitivity: FDR-significant $K_{\\mathrm{eff}}$ conditions out of 12 (2 benchmarks $\\times$ 6 attacks). $\\bar{\\beta}_{\\mathrm{std}}$: mean standardized $K_{\\mathrm{eff}}$ coefficient across conditions. The full-pool fractional logit count at $K{=}3$ (8/12) differs by $\\pm 1$ from Table~\\ref{tab:method_comparison} (9/12) due to clustering implementation details in the sensitivity script; this does not affect within-table comparisons.}\n\\label{tab:near_chance}\n\\begin{tabular}{llcccccc}\n\\toprule\n$K$ & Panel set & $n$ & OLS & WCB & Frac & $\\bar{\\beta}_{\\mathrm{std}}$ & $\\bar{R}^2$ \\\\\n\\midrule\n3 & Full (15 models) & 455 & 11/12 & 3/12 & 8/12 & 0.349 & 0.340 \\\\\n3 & Filtered (13 models) & 286 & 12/12 & 4/12 & 9/12 & \\textbf{0.480} & 0.333 \\\\\n\\midrule\n5 & Full (15 models) & 3{,}003 & 12/12 & 7/12 & 10/12 & 0.437 & 0.285 \\\\\n5 & Filtered (13 models) & 1{,}287 & 11/12 & 7/12 & 11/12 & \\textbf{0.512} & 0.256 \\\\\n\\midrule\n7 & Full (15 models) & 6{,}435 & 12/12 & 8/12 & 10/12 & 0.401 & 0.244 \\\\\n7 & Filtered (13 models) & 1{,}716 & 11/12 & 2/12 & 11/12 & 0.385 & 0.203 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $K{=}3$ and $K{=}5$, WCB significance is preserved or improved after filtering (3$\\to$4 and 7$\\to$7), and the mean standardized $\\beta_{K_{\\mathrm{eff}}}$ \\emph{increases} from 0.349 to 0.480 ($K{=}3$) and from 0.437 to 0.512 ($K{=}5$), indicating that the diversity--vulnerability association is stronger, not weaker, without near-chance models. Fractional logit significance likewise improves after filtering at every $K$ (8$\\to$9, 10$\\to$11, 10$\\to$11), confirming that the effect is not an artifact of the GLM specification. At $K{=}7$, WCB significance drops from 8/12 to 2/12; however, the combinatorial filtering removes 73.3\\% of panels (6{,}435$\\to$1{,}716), substantially reducing statistical power for the conservative bootstrap test. The raw WCB $p$-values at $K{=}7$ cluster in the 0.02--0.15 range rather than reversing sign, and the standardized coefficient remains positive ($\\bar{\\beta}_{\\mathrm{std}}{=}0.385$). The $K{=}7$ attenuation is therefore attributable to power loss from the sample reduction rather than absence of a genuine effect.\n",
      "numLines": 30,
      "startLine": 1075,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01TQzmu1NVwGX7FMTWzMSqnz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 840,
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
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "4fe29be9-9710-421d-91aa-df1f2f367a8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MiCnmeQ2L13XgAFz3Q7rBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19192,
      "cache_read_input_tokens": 34162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19192
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

_source line 68 · 2026-05-25T21:11:22.114Z_

<details><summary>↩ Tool result · `toolu_01TQzmu1NVwGX7FMTWzMSqnz`</summary>

```text
840	\bottomrule
841	\end{tabular}
842	\caption{Minimum detectable effect size (80\% power, 1{,}000 simulations, wild cluster bootstrap) by panel size. MDE decreases approximately as $1/\sqrt{N}$, confirming that $K{=}5$/$K{=}7$ significance reflects genuine effects rather than inflated type~I error.}
843	\label{tab:mde}
844	\end{table}
845	
846	\section{Alternative Diversity Measures}
847	\label{app:alt_diversity}
848	
849	We compare $K_{\mathrm{eff}}$ against three classical ensemble diversity measures using the same OLS specification (Equation~\ref{eq:regression}) with FDR correction across 12 conditions pooled over $K$ values.
850	
851	\begin{table}[h]
852	\centering
853	\small
854	\begin{tabular}{lcccc}
855	\toprule
856	\textbf{Measure} & \textbf{Sig} & \textbf{Dir.} & \textbf{$|\bar{\beta}_{\mathrm{std}}|$} & $\boldsymbol{\rho}$ \textbf{w/} $\boldsymbol{K_{\mathrm{eff}}}$ \\
857	\midrule
858	$Q$-statistic    & 9/12  & 6+/3$-$ & 0.251 & 0.599 \\
859	Disagreement     & 11/12 & 11+/0$-$ & 0.481 & 0.934 \\
860	$\kappa$-diversity & 11/12 & 11+/0$-$ & 0.497 & 0.978 \\
861	\addlinespace
862	$K_{\mathrm{eff}}$ (ref.) & 12/12 & 12+/0$-$ & 0.430 & --- \\
863	\bottomrule
864	\end{tabular}
865	\caption{Comparison of diversity measures as predictors of panel ASR (OLS, FDR-corrected, 12 conditions pooled across $K$). Sig: FDR-significant conditions. $|\bar{\beta}_{\mathrm{std}}|$: mean absolute standardized coefficient. $\rho$: Pearson correlation with $K_{\mathrm{eff}}$.}
866	\label{tab:alt_diversity}
867	\end{table}
868	
869	$K_{\mathrm{eff}}$ and $\kappa$-diversity \citep{kuncheva2003measures} are near-equivalent ($\rho{=}0.978$), with comparable significance counts (12/12 vs.\ 11/12) and effect sizes (0.430 vs.\ 0.497). Disagreement rate achieves similar predictive power ($\rho{=}0.934$, 11/12). The $Q$-statistic is the weakest predictor (9/12, $|\bar{\beta}_{\mathrm{std}}|{=}0.251$), consistent with its known insensitivity to the type of error correlation that is associated with panel vulnerability \citep{kuncheva2003measures}. $K_{\mathrm{eff}}$'s advantage over these alternatives is not predictive power but interpretability: it quantifies the number of effective independent channels in the panel, connecting directly to the information-theoretic foundation of panel aggregation (\S\ref{sec:experiments}).
870	
871	\subsection{$\kappa$-Diversity Predictor Shift Comparison}
872	\label{app:kappa_regime}
873	
874	To test whether the predictor shift (\S\ref{sec:cross_k}) is specific to $K_{\mathrm{eff}}$ or a generic property of diversity measures, we repeat the wild cluster bootstrap analysis replacing $K_{\mathrm{eff}}$ with $\kappa$-diversity ($1 - \bar{\kappa}$, where $\bar{\kappa}$ is the mean pairwise Cohen's $\kappa$ on clean winner labels; $\rho{=}0.978$ with $K_{\mathrm{eff}}$).
875	
876	\begin{table}[h]
877	\centering
878	\small
879	\begin{tabular}{rcccc}
880	\toprule
881	& \multicolumn{2}{c}{\textbf{$K_{\mathrm{eff}}$}} & \multicolumn{2}{c}{\textbf{$\kappa$-diversity}} \\
882	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
883	$\boldsymbol{K}$ & \textbf{div.\ sig} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & \textbf{div.\ sig} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} \\
884	\midrule
885	3 & 4/12  & 3/12 & 8/12 & 1/12 \\
886	5 & 7/12 & 2/12 & 7/12 & 4/12 \\
887	7 & 8/12  & 1/12 & 6/12 & 1/12 \\
888	\bottomrule
889	\end{tabular}
890	\caption{Predictor shift comparison: $K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity across panel sizes (wild cluster bootstrap, BH FDR $\alpha{=}0.05$). $K_{\mathrm{eff}}$ exhibits a clear shift ($4 \to 7 \to 8$); $\kappa$-diversity significance decreases monotonically ($8 \to 7 \to 6$), showing no predictor shift.}
891	\label{tab:kappa_regime}
892	\end{table}
893	
894	$\kappa$-diversity is a stronger predictor than $K_{\mathrm{eff}}$ at $K{=}3$ (8/12 vs.\ 4/12), consistent with its larger mean effect size ($|\bar{\beta}_{\mathrm{std}}|{=}0.497$ vs.\ 0.430; Table~\ref{tab:alt_diversity}). However, $\kappa$-diversity shows no predictor shift: its significance \emph{decreases} from $K{=}3$ to $K{=}7$ ($8 \to 7 \to 6$), the opposite of $K_{\mathrm{eff}}$'s pattern ($4 \to 7 \to 8$). Furthermore, under $\kappa$-diversity, $\eta_{\max}$ retains significance at $K{=}5$ (4/12), whereas under $K_{\mathrm{eff}}$ it drops to 2/12. The predictor shift---co-determination at $K{=}3$ transitioning to diversity dominance at $K{\geq}5$---is thus specific to $K_{\mathrm{eff}}$'s MI-based formulation, which captures effective judge independence rather than pairwise label agreement.
895	
896	\subsection{Shannon MI Entropy Predictor Shift Comparison}
897	\label{app:shannon_entropy}
898	
899	Shannon MI entropy ($H_{\mathrm{MI}} = \binom{K}{2}^{-1} \sum_{i<j} \mathrm{MI}(i,j)$) averages raw pairwise mutual information, measuring mean non-redundancy rather than effective independence. It correlates negatively with $K_{\mathrm{eff}}$ ($r = -0.63$ to $-0.76$ across $K$): panels with high mean MI tend to have lower effective independent channels, because $K_{\mathrm{eff}}$'s $\exp(-2\,\mathrm{MI})$ transform penalizes high MI more aggressively than linear averaging.
900	
901	\begin{table}[h]
902	\centering
903	\small
904	\begin{tabular}{rcc}
905	\toprule
906	$\boldsymbol{K}$ & \textbf{Shannon MI sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} \\
907	\midrule
908	3 & 4/12 & 6/12 \\
909	5 & 4/12 & 8/12 \\
910	7 & 0/12 & 2/12 \\
911	\bottomrule
912	\end{tabular}
913	\caption{Predictor shift comparison: Shannon MI entropy vs.\ $K_{\mathrm{eff}}$ (within-framework wild cluster bootstrap, $B{=}999$, Webb weights, BH FDR $\alpha{=}0.05$). Shannon is flat then collapses ($4 \to 4 \to 0$); $K_{\mathrm{eff}}$ rises before declining ($6 \to 8 \to 2$). Bootstrap parameters differ from the primary analysis ($B{=}9{,}999$, Rademacher); absolute counts are not comparable with Table~\ref{tab:kappa_regime}.}
914	\label{tab:shannon_shift}
915	\end{table}
916	
917	Shannon MI entropy shows no predictor shift: significance is flat at $K{=}3$ and $K{=}5$ (4/12) before collapsing at $K{=}7$ (0/12). $K_{\mathrm{eff}}$ exhibits a clear rise from $K{=}3$ to $K{=}5$ ($6 \to 8$) within the same framework. Combined with the $\kappa$-diversity comparison (Appendix~\ref{app:kappa_regime}, $8 \to 7 \to 6$), two alternative diversity measures independently fail to exhibit the predictor shift, providing converging evidence that the shift is specific to $K_{\mathrm{eff}}$'s transformation of pairwise MI into an effective channel count.
918	
919	\section{Gaussian Copula Assumption and $K_{\mathrm{eff}}$ Robustness}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "25bd9412-f41d-490d-888e-6c4cc5d340cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\\bottomrule\n\\end{tabular}\n\\caption{Minimum detectable effect size (80\\% power, 1{,}000 simulations, wild cluster bootstrap) by panel size. MDE decreases approximately as $1/\\sqrt{N}$, confirming that $K{=}5$/$K{=}7$ significance reflects genuine effects rather than inflated type~I error.}\n\\label{tab:mde}\n\\end{table}\n\n\\section{Alternative Diversity Measures}\n\\label{app:alt_diversity}\n\nWe compare $K_{\\mathrm{eff}}$ against three classical ensemble diversity measures using the same OLS specification (Equation~\\ref{eq:regression}) with FDR correction across 12 conditions pooled over $K$ values.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Measure} & \\textbf{Sig} & \\textbf{Dir.} & \\textbf{$|\\bar{\\beta}_{\\mathrm{std}}|$} & $\\boldsymbol{\\rho}$ \\textbf{w/} $\\boldsymbol{K_{\\mathrm{eff}}}$ \\\\\n\\midrule\n$Q$-statistic    & 9/12  & 6+/3$-$ & 0.251 & 0.599 \\\\\nDisagreement     & 11/12 & 11+/0$-$ & 0.481 & 0.934 \\\\\n$\\kappa$-diversity & 11/12 & 11+/0$-$ & 0.497 & 0.978 \\\\\n\\addlinespace\n$K_{\\mathrm{eff}}$ (ref.) & 12/12 & 12+/0$-$ & 0.430 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Comparison of diversity measures as predictors of panel ASR (OLS, FDR-corrected, 12 conditions pooled across $K$). Sig: FDR-significant conditions. $|\\bar{\\beta}_{\\mathrm{std}}|$: mean absolute standardized coefficient. $\\rho$: Pearson correlation with $K_{\\mathrm{eff}}$.}\n\\label{tab:alt_diversity}\n\\end{table}\n\n$K_{\\mathrm{eff}}$ and $\\kappa$-diversity \\citep{kuncheva2003measures} are near-equivalent ($\\rho{=}0.978$), with comparable significance counts (12/12 vs.\\ 11/12) and effect sizes (0.430 vs.\\ 0.497). Disagreement rate achieves similar predictive power ($\\rho{=}0.934$, 11/12). The $Q$-statistic is the weakest predictor (9/12, $|\\bar{\\beta}_{\\mathrm{std}}|{=}0.251$), consistent with its known insensitivity to the type of error correlation that is associated with panel vulnerability \\citep{kuncheva2003measures}. $K_{\\mathrm{eff}}$'s advantage over these alternatives is not predictive power but interpretability: it quantifies the number of effective independent channels in the panel, connecting directly to the information-theoretic foundation of panel aggregation (\\S\\ref{sec:experiments}).\n\n\\subsection{$\\kappa$-Diversity Predictor Shift Comparison}\n\\label{app:kappa_regime}\n\nTo test whether the predictor shift (\\S\\ref{sec:cross_k}) is specific to $K_{\\mathrm{eff}}$ or a generic property of diversity measures, we repeat the wild cluster bootstrap analysis replacing $K_{\\mathrm{eff}}$ with $\\kappa$-diversity ($1 - \\bar{\\kappa}$, where $\\bar{\\kappa}$ is the mean pairwise Cohen's $\\kappa$ on clean winner labels; $\\rho{=}0.978$ with $K_{\\mathrm{eff}}$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{$K_{\\mathrm{eff}}$}} & \\multicolumn{2}{c}{\\textbf{$\\kappa$-diversity}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n$\\boldsymbol{K}$ & \\textbf{div.\\ sig} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & \\textbf{div.\\ sig} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} \\\\\n\\midrule\n3 & 4/12  & 3/12 & 8/12 & 1/12 \\\\\n5 & 7/12 & 2/12 & 7/12 & 4/12 \\\\\n7 & 8/12  & 1/12 & 6/12 & 1/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Predictor shift comparison: $K_{\\mathrm{eff}}$ vs.\\ $\\kappa$-diversity across panel sizes (wild cluster bootstrap, BH FDR $\\alpha{=}0.05$). $K_{\\mathrm{eff}}$ exhibits a clear shift ($4 \\to 7 \\to 8$); $\\kappa$-diversity significance decreases monotonically ($8 \\to 7 \\to 6$), showing no predictor shift.}\n\\label{tab:kappa_regime}\n\\end{table}\n\n$\\kappa$-diversity is a stronger predictor than $K_{\\mathrm{eff}}$ at $K{=}3$ (8/12 vs.\\ 4/12), consistent with its larger mean effect size ($|\\bar{\\beta}_{\\mathrm{std}}|{=}0.497$ vs.\\ 0.430; Table~\\ref{tab:alt_diversity}). However, $\\kappa$-diversity shows no predictor shift: its significance \\emph{decreases} from $K{=}3$ to $K{=}7$ ($8 \\to 7 \\to 6$), the opposite of $K_{\\mathrm{eff}}$'s pattern ($4 \\to 7 \\to 8$). Furthermore, under $\\kappa$-diversity, $\\eta_{\\max}$ retains significance at $K{=}5$ (4/12), whereas under $K_{\\mathrm{eff}}$ it drops to 2/12. The predictor shift---co-determination at $K{=}3$ transitioning to diversity dominance at $K{\\geq}5$---is thus specific to $K_{\\mathrm{eff}}$'s MI-based formulation, which captures effective judge independence rather than pairwise label agreement.\n\n\\subsection{Shannon MI Entropy Predictor Shift Comparison}\n\\label{app:shannon_entropy}\n\nShannon MI entropy ($H_{\\mathrm{MI}} = \\binom{K}{2}^{-1} \\sum_{i<j} \\mathrm{MI}(i,j)$) averages raw pairwise mutual information, measuring mean non-redundancy rather than effective independence. It correlates negatively with $K_{\\mathrm{eff}}$ ($r = -0.63$ to $-0.76$ across $K$): panels with high mean MI tend to have lower effective independent channels, because $K_{\\mathrm{eff}}$'s $\\exp(-2\\,\\mathrm{MI})$ transform penalizes high MI more aggressively than linear averaging.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rcc}\n\\toprule\n$\\boldsymbol{K}$ & \\textbf{Shannon MI sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\n3 & 4/12 & 6/12 \\\\\n5 & 4/12 & 8/12 \\\\\n7 & 0/12 & 2/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Predictor shift comparison: Shannon MI entropy vs.\\ $K_{\\mathrm{eff}}$ (within-framework wild cluster bootstrap, $B{=}999$, Webb weights, BH FDR $\\alpha{=}0.05$). Shannon is flat then collapses ($4 \\to 4 \\to 0$); $K_{\\mathrm{eff}}$ rises before declining ($6 \\to 8 \\to 2$). Bootstrap parameters differ from the primary analysis ($B{=}9{,}999$, Rademacher); absolute counts are not comparable with Table~\\ref{tab:kappa_regime}.}\n\\label{tab:shannon_shift}\n\\end{table}\n\nShannon MI entropy shows no predictor shift: significance is flat at $K{=}3$ and $K{=}5$ (4/12) before collapsing at $K{=}7$ (0/12). $K_{\\mathrm{eff}}$ exhibits a clear rise from $K{=}3$ to $K{=}5$ ($6 \\to 8$) within the same framework. Combined with the $\\kappa$-diversity comparison (Appendix~\\ref{app:kappa_regime}, $8 \\to 7 \\to 6$), two alternative diversity measures independently fail to exhibit the predictor shift, providing converging evidence that the shift is specific to $K_{\\mathrm{eff}}$'s transformation of pairwise MI into an effective channel count.\n\n\\section{Gaussian Copula Assumption and $K_{\\mathrm{eff}}$ Robustness}",
      "numLines": 80,
      "startLine": 840,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Grep · `toolu_0118Yw5ds7rvVLimdAFQBYFD`</summary>

```json
{
  "pattern": "12/12|12\\\\slash 12",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "04116274-c81e-4382-8587-7faf1db55f51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MiCnmeQ2L13XgAFz3Q7rBz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19192,
      "cache_read_input_tokens": 34162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19192
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

_source line 70 · 2026-05-25T21:11:23.538Z_

<details><summary>↩ Tool result · `toolu_0118Yw5ds7rvVLimdAFQBYFD`</summary>

```text
docs/paper/analysis.tex:14:[Omitted long matching line]
docs/paper/main.tex:30:[Omitted long matching line]
docs/paper/main.tex:44:\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\geq}20$ threshold at all panel sizes \citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity show opposite $K$-trends).
docs/paper/conclusion.tex:3:[Omitted long matching line]
docs/paper/abstract.tex:3:[Omitted long matching line]
docs/paper/results.tex:16:[Omitted long matching line]
docs/paper/results.tex:27:OLS                    & 10/12 & 12/12 \\
docs/paper/results.tex:34:\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}
docs/paper/results.tex:38:Power analysis yields MDE $\beta_{\mathrm{std}} = 0.14$ at 80\% power (Appendix~\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.
docs/paper/results.tex:70:Threshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\
docs/paper/results.tex:71:Majority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\
docs/paper/results.tex:72:Weighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\
docs/paper/introduction.tex:18:[Omitted long matching line]
docs/paper/appendix.tex:133:\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{10/12} & \\
docs/paper/appendix.tex:165:\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{11/12} & \\
docs/paper/appendix.tex:197:\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{11/12} & \\
docs/paper/appendix.tex:303:Under corrected data (V2), all 12 $K_{\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\times$ sycophancy coefficient ($\hat{\beta}_{\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\hat{\beta}_{\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\% positive rate) and 12/12 at $K{=}5$ (100\%).
docs/paper/appendix.tex:454:[Omitted long matching line]
docs/paper/appendix.tex:580:[Omitted long matching line]
docs/paper/appendix.tex:862:$K_{\mathrm{eff}}$ (ref.) & 12/12 & 12+/0$-$ & 0.430 & --- \\
docs/paper/appendix.tex:869:[Omitted long matching line]
docs/paper/appendix.tex:1025:3 & 12/12 & 12/12 & 9/12 & 7/12 \\
docs/paper/appendix.tex:1026:5 & 12/12 & 11/12 & 9/12 & 5/12 \\
docs/paper/appendix.tex:1027:7 & 12/12 & 11/12 & 9/12 & 4/12 \\
docs/paper/appendix.tex:1092:3 & Filtered (13 models) & 286 & 12/12 & 4/12 & 9/12 & \textbf{0.480} & 0.333 \\
docs/paper/appendix.tex:1094:5 & Full (15 models) & 3{,}003 & 12/12 & 7/12 & 10/12 & 0.437 & 0.285 \\
docs/paper/appendix.tex:1097:7 & Full (15 models) & 6{,}435 & 12/12 & 8/12 & 10/12 & 0.401 & 0.244 \\
docs/paper/appendix.tex:1161:[Omitted long matching line]
docs/paper/appendix.tex:1179:Model selection & Cross-family diversity with capability floor $\eta_j{<}0.15$ & $\min(\eta_{\max})$ optimal in 12/12 conditions; near-chance exclusion strengthens $K_{\mathrm{eff}}$ signal \\
docs/paper/appendix.tex:1196:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "ccc2c8d2-e479-407c-a7a3-98ea804d5495",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:14:[Omitted long matching line]\ndocs/paper/main.tex:30:[Omitted long matching line]\ndocs/paper/main.tex:44:\\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\\geq}20$ threshold at all panel sizes \\citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\\mathrm{eff}}$ vs.\\ $\\kappa$-diversity show opposite $K$-trends).\ndocs/paper/conclusion.tex:3:[Omitted long matching line]\ndocs/paper/abstract.tex:3:[Omitted long matching line]\ndocs/paper/results.tex:16:[Omitted long matching line]\ndocs/paper/results.tex:27:OLS                    & 10/12 & 12/12 \\\\\ndocs/paper/results.tex:34:\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}\ndocs/paper/results.tex:38:Power analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\ndocs/paper/results.tex:70:Threshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\ndocs/paper/results.tex:71:Majority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\ndocs/paper/results.tex:72:Weighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\ndocs/paper/introduction.tex:18:[Omitted long matching line]\ndocs/paper/appendix.tex:133:\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{10/12} & \\\\\ndocs/paper/appendix.tex:165:\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{11/12} & \\\\\ndocs/paper/appendix.tex:197:\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{11/12} & \\\\\ndocs/paper/appendix.tex:303:Under corrected data (V2), all 12 $K_{\\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\\times$ sycophancy coefficient ($\\hat{\\beta}_{\\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\\hat{\\beta}_{\\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\\% positive rate) and 12/12 at $K{=}5$ (100\\%).\ndocs/paper/appendix.tex:454:[Omitted long matching line]\ndocs/paper/appendix.tex:580:[Omitted long matching line]\ndocs/paper/appendix.tex:862:$K_{\\mathrm{eff}}$ (ref.) & 12/12 & 12+/0$-$ & 0.430 & --- \\\\\ndocs/paper/appendix.tex:869:[Omitted long matching line]\ndocs/paper/appendix.tex:1025:3 & 12/12 & 12/12 & 9/12 & 7/12 \\\\\ndocs/paper/appendix.tex:1026:5 & 12/12 & 11/12 & 9/12 & 5/12 \\\\\ndocs/paper/appendix.tex:1027:7 & 12/12 & 11/12 & 9/12 & 4/12 \\\\\ndocs/paper/appendix.tex:1092:3 & Filtered (13 models) & 286 & 12/12 & 4/12 & 9/12 & \\textbf{0.480} & 0.333 \\\\\ndocs/paper/appendix.tex:1094:5 & Full (15 models) & 3{,}003 & 12/12 & 7/12 & 10/12 & 0.437 & 0.285 \\\\\ndocs/paper/appendix.tex:1097:7 & Full (15 models) & 6{,}435 & 12/12 & 8/12 & 10/12 & 0.401 & 0.244 \\\\\ndocs/paper/appendix.tex:1161:[Omitted long matching line]\ndocs/paper/appendix.tex:1179:Model selection & Cross-family diversity with capability floor $\\eta_j{<}0.15$ & $\\min(\\eta_{\\max})$ optimal in 12/12 conditions; near-chance exclusion strengthens $K_{\\mathrm{eff}}$ signal \\\\\ndocs/paper/appendix.tex:1196:[Omitted long matching line]",
    "numLines": 30
  }
}
```

</details>

---


### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also read the omitted lines and a few more sections to understand the full context before making edits.

Let me read lines 303, 454, 580, 1025-1027, and 1196 of appendix.tex to see what changes are needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "99060db0-2105-4193-a984-c29336e149a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pZNdFU12bmRtabuYpgmXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17720,
      "cache_read_input_tokens": 53354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17720
      },
      "output_tokens": 10,
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

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01UbvmHaC8JAVFfm7Qzz4nRH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 295,
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
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "248de922-6bf5-4c06-bcb6-ea9ab51072c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pZNdFU12bmRtabuYpgmXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17720,
      "cache_read_input_tokens": 53354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17720
      },
      "output_tokens": 10,
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

_source line 73 · 2026-05-25T21:11:32.965Z_

<details><summary>↩ Tool result · `toolu_01UbvmHaC8JAVFfm7Qzz4nRH`</summary>

```text
295	
296	\begin{figure}[h]
297	\centering
298	\includegraphics[width=\columnwidth]{figures/fig2_gam_keff_split.pdf}
299	\caption{GAM bootstrap $K_{\mathrm{eff}}$ effect direction at $K{=}3$ ($B{=}9999$). All 12 conditions show positive $K_{\mathrm{eff}}$ direction (88.9--100\% bootstrap rate). The Kruskal--Wallis test finds no significant magnitude difference between targeted and shared-bias attacks ($p{=}0.200$).}
300	\label{fig:gam_split}
301	\end{figure}
302	
303	Under corrected data (V2), all 12 $K_{\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\times$ sycophancy coefficient ($\hat{\beta}_{\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\hat{\beta}_{\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\% positive rate) and 12/12 at $K{=}5$ (100\%).
304	
305	\subsection{Diversity--Capability Tradeoff}
306	\label{app:diversity_capability}
307	
308	The $r = 0.70$--$0.81$ correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ ($K{=}3$ to $K{=}5$) reflects a structural feature of the current LLM ecosystem: maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges. The structural correlation is unaffected by SE correction; it is a property of the model ecosystem, not an artifact of panel overlap. However, the high confound combined with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it.
309	
310	
311	Family-level labels provide indirect evidence that capability proximity matters more than taxonomic grouping: family membership is not a significant predictor of panel vulnerability ($p = 0.179$ on MMLU, $p = 0.385$ on ARC), consistent with models from the same provider exhibiting heterogeneous vulnerability profiles that vary by capability tier rather than by shared architecture \citep{kuncheva2003measures}.
312	
313	\subsection{Aggregation Rule Formal Definitions}
314	\label{app:aggregation_formal}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "7016d19f-c0b9-47f3-a502-95b046c70025",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_gam_keff_split.pdf}\n\\caption{GAM bootstrap $K_{\\mathrm{eff}}$ effect direction at $K{=}3$ ($B{=}9999$). All 12 conditions show positive $K_{\\mathrm{eff}}$ direction (88.9--100\\% bootstrap rate). The Kruskal--Wallis test finds no significant magnitude difference between targeted and shared-bias attacks ($p{=}0.200$).}\n\\label{fig:gam_split}\n\\end{figure}\n\nUnder corrected data (V2), all 12 $K_{\\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\\times$ sycophancy coefficient ($\\hat{\\beta}_{\\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\\hat{\\beta}_{\\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\\% positive rate) and 12/12 at $K{=}5$ (100\\%).\n\n\\subsection{Diversity--Capability Tradeoff}\n\\label{app:diversity_capability}\n\nThe $r = 0.70$--$0.81$ correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ ($K{=}3$ to $K{=}5$) reflects a structural feature of the current LLM ecosystem: maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges. The structural correlation is unaffected by SE correction; it is a property of the model ecosystem, not an artifact of panel overlap. However, the high confound combined with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it.\n\n\nFamily-level labels provide indirect evidence that capability proximity matters more than taxonomic grouping: family membership is not a significant predictor of panel vulnerability ($p = 0.179$ on MMLU, $p = 0.385$ on ARC), consistent with models from the same provider exhibiting heterogeneous vulnerability profiles that vary by capability tier rather than by shared architecture \\citep{kuncheva2003measures}.\n\n\\subsection{Aggregation Rule Formal Definitions}\n\\label{app:aggregation_formal}",
      "numLines": 20,
      "startLine": 295,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_019E8mUYfhZ4tjGk5sMMZf2t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 448,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "735f1bf2-0f44-4f2f-9b82-11ccd8a75e0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pZNdFU12bmRtabuYpgmXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17720,
      "cache_read_input_tokens": 53354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17720
      },
      "output_tokens": 10,
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

_source line 75 · 2026-05-25T21:11:33.745Z_

<details><summary>↩ Tool result · `toolu_019E8mUYfhZ4tjGk5sMMZf2t`</summary>

```text
448	
449	\subsection{Metric Robustness Under Partial Panel Information}
450	\label{app:oracle}
451	
452	The main analysis computes $\eta_{\max}$ with full knowledge of panel composition (all three judges known). In deployment, a practitioner selecting or auditing a panel may know only a subset of the constituent judges. We test whether $\eta_{\max}$ retains predictive power under such partial information by recomputing it from two of the three panel members: for each panel, we cycle through all $\binom{3}{1} = 3$ leave-one-out masks, compute $\eta_{\max}$ from the two known judges, and average the regression estimates across masking scenarios.
453	
454	Under the most conservative inference (partial information + clustered SE), $\eta_{\max}$ remains the sole significant predictor with $\hat{\beta}_{\mathrm{std}} = 0.589$, achieving significance in 12/12 conditions, stronger than the oracle baseline (4/12 under clustered SE). $K_{\mathrm{eff}}$ loses all predictive power (0/12). The averaging over masking scenarios smooths estimation noise inherent in the three-judge oracle computation, strengthening the $\eta_{\max}$ signal. This demonstrates that $\eta_{\max}$ computed from partial panel information is robust to incomplete composition knowledge and retains (indeed improves) its predictive power for panel ASR.
455	
456	\subsection{VIF Collinearity Diagnostics}
457	\label{app:vif_diagnostics}
458	
459	The $K_{\mathrm{eff}}$--$\eta_{\max}$ correlation ($r{=}0.70$ at $K{=}3$, $r{=}0.81$ at $K{=}5$) raises collinearity concerns. We report variance inflation factors (VIF) and their implications for coefficient interpretation across panel sizes.
460	
461	\paragraph{Per-Condition VIF.} Table~\ref{tab:vif_percond} reports VIF values for each of the 12 conditions at $K{=}3$, $K{=}5$, and $K{=}7$. VIF is computed as $1/(1 - R^2_{\mathrm{aux}})$, where $R^2_{\mathrm{aux}}$ is the $R^2$ from regressing $K_{\mathrm{eff}}$ on $\eta_{\max}$.
462	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "7553b8ce-0217-49e2-b428-0e76a1da6eb6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\n\\subsection{Metric Robustness Under Partial Panel Information}\n\\label{app:oracle}\n\nThe main analysis computes $\\eta_{\\max}$ with full knowledge of panel composition (all three judges known). In deployment, a practitioner selecting or auditing a panel may know only a subset of the constituent judges. We test whether $\\eta_{\\max}$ retains predictive power under such partial information by recomputing it from two of the three panel members: for each panel, we cycle through all $\\binom{3}{1} = 3$ leave-one-out masks, compute $\\eta_{\\max}$ from the two known judges, and average the regression estimates across masking scenarios.\n\nUnder the most conservative inference (partial information + clustered SE), $\\eta_{\\max}$ remains the sole significant predictor with $\\hat{\\beta}_{\\mathrm{std}} = 0.589$, achieving significance in 12/12 conditions, stronger than the oracle baseline (4/12 under clustered SE). $K_{\\mathrm{eff}}$ loses all predictive power (0/12). The averaging over masking scenarios smooths estimation noise inherent in the three-judge oracle computation, strengthening the $\\eta_{\\max}$ signal. This demonstrates that $\\eta_{\\max}$ computed from partial panel information is robust to incomplete composition knowledge and retains (indeed improves) its predictive power for panel ASR.\n\n\\subsection{VIF Collinearity Diagnostics}\n\\label{app:vif_diagnostics}\n\nThe $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation ($r{=}0.70$ at $K{=}3$, $r{=}0.81$ at $K{=}5$) raises collinearity concerns. We report variance inflation factors (VIF) and their implications for coefficient interpretation across panel sizes.\n\n\\paragraph{Per-Condition VIF.} Table~\\ref{tab:vif_percond} reports VIF values for each of the 12 conditions at $K{=}3$, $K{=}5$, and $K{=}7$. VIF is computed as $1/(1 - R^2_{\\mathrm{aux}})$, where $R^2_{\\mathrm{aux}}$ is the $R^2$ from regressing $K_{\\mathrm{eff}}$ on $\\eta_{\\max}$.\n",
      "numLines": 15,
      "startLine": 448,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Read · `toolu_01GKJF2LJGAfNnpgwbi8yB8C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 575,
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
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1a0c56f3-45c3-4b62-a20d-25a21fcae587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pZNdFU12bmRtabuYpgmXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17720,
      "cache_read_input_tokens": 53354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17720
      },
      "output_tokens": 10,
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

_source line 77 · 2026-05-25T21:11:34.696Z_

<details><summary>↩ Tool result · `toolu_01GKJF2LJGAfNnpgwbi8yB8C`</summary>

```text
575	Figure~\ref{fig:panel_design} compares three panel selection strategies: $\min(\eta_{\max})$ (select the panel minimizing weakest-judge vulnerability), random selection, and $\max(K_{\mathrm{eff}})$ (maximize diversity). The $\min(\eta_{\max})$ strategy achieves the lowest ASR in all 12 conditions, consistent with the weakest-link dominance documented in \S\ref{sec:dominance}.
576	
577	\section{Clustered Standard Error Analysis}
578	\label{app:clustered_se}
579	
580	Under clustered standard errors (clustering on the $K$ judge positions), $\eta_{\max}$ retains significance in 4/12 conditions while $K_{\mathrm{eff}}$ achieves significance in 0/12. This contrasts with OLS ($\eta_{\max}$ 10/12, $K_{\mathrm{eff}}$ 12/12) and wild cluster bootstrap ($\eta_{\max}$ 3/12, $K_{\mathrm{eff}}$ 4/12), illustrating how the choice of inference method modulates apparent significance at $K{=}3$ while coefficient direction remains positive (12/12) for $K_{\mathrm{eff}}$ across all methods, with significance ranging from 0/12 to 12/12 (Figure~\ref{fig:robustness}).
581	
582	\section{Robustness Checks: Subsampling and Specification}
583	\label{app:robustness_checks}
584	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "3cc88614-1a16-4810-8b04-8172046de8ed",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "Figure~\\ref{fig:panel_design} compares three panel selection strategies: $\\min(\\eta_{\\max})$ (select the panel minimizing weakest-judge vulnerability), random selection, and $\\max(K_{\\mathrm{eff}})$ (maximize diversity). The $\\min(\\eta_{\\max})$ strategy achieves the lowest ASR in all 12 conditions, consistent with the weakest-link dominance documented in \\S\\ref{sec:dominance}.\n\n\\section{Clustered Standard Error Analysis}\n\\label{app:clustered_se}\n\nUnder clustered standard errors (clustering on the $K$ judge positions), $\\eta_{\\max}$ retains significance in 4/12 conditions while $K_{\\mathrm{eff}}$ achieves significance in 0/12. This contrasts with OLS ($\\eta_{\\max}$ 10/12, $K_{\\mathrm{eff}}$ 12/12) and wild cluster bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), illustrating how the choice of inference method modulates apparent significance at $K{=}3$ while coefficient direction remains positive (12/12) for $K_{\\mathrm{eff}}$ across all methods, with significance ranging from 0/12 to 12/12 (Figure~\\ref{fig:robustness}).\n\n\\section{Robustness Checks: Subsampling and Specification}\n\\label{app:robustness_checks}\n",
      "numLines": 10,
      "startLine": 575,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_01JboUf3Kow6SmjG7Jp6gqi2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 1020,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "0967d76e-3fa9-4496-9b63-28af49cc77f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pZNdFU12bmRtabuYpgmXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17720,
      "cache_read_input_tokens": 53354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17720
      },
      "output_tokens": 10,
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

_source line 79 · 2026-05-25T21:11:35.439Z_

<details><summary>↩ Tool result · `toolu_01JboUf3Kow6SmjG7Jp6gqi2`</summary>

```text
1020	\small
1021	\begin{tabular}{rcccc}
1022	\toprule
1023	$\boldsymbol{K}$ & \textbf{$K_{\mathrm{eff}}$ concordance} & \textbf{$\eta_{\max}$ concordance} & \textbf{$K_{\mathrm{eff}}$ sig (FL)} & \textbf{$\eta_{\max}$ sig (FL)} \\
1024	\midrule
1025	3 & 12/12 & 12/12 & 9/12 & 7/12 \\
1026	5 & 12/12 & 11/12 & 9/12 & 5/12 \\
1027	7 & 12/12 & 11/12 & 9/12 & 4/12 \\
1028	\midrule
1029	Total & 36/36 & 34/36 & 27/36 & 16/36 \\
1030	\bottomrule
1031	\end{tabular}
1032	\caption{Fractional logit vs.\ OLS comparison across $K$ values. Concordance: fraction of conditions where the coefficient direction (positive/negative) matches between OLS and fractional logit. $K_{\mathrm{eff}}$ direction is perfectly concordant (36/36); $\eta_{\max}$ shows 2 discordances (both at high $K$ where the coefficient is near zero). Fractional logit significance is computed with clustered SE (max-$p$, BH FDR $\alpha{=}0.05$).}
1033	\label{tab:fraclogit_detail}
1034	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "c58fb118-5bd8-4bcc-81d3-b0c60639893a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\\small\n\\begin{tabular}{rcccc}\n\\toprule\n$\\boldsymbol{K}$ & \\textbf{$K_{\\mathrm{eff}}$ concordance} & \\textbf{$\\eta_{\\max}$ concordance} & \\textbf{$K_{\\mathrm{eff}}$ sig (FL)} & \\textbf{$\\eta_{\\max}$ sig (FL)} \\\\\n\\midrule\n3 & 12/12 & 12/12 & 9/12 & 7/12 \\\\\n5 & 12/12 & 11/12 & 9/12 & 5/12 \\\\\n7 & 12/12 & 11/12 & 9/12 & 4/12 \\\\\n\\midrule\nTotal & 36/36 & 34/36 & 27/36 & 16/36 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Fractional logit vs.\\ OLS comparison across $K$ values. Concordance: fraction of conditions where the coefficient direction (positive/negative) matches between OLS and fractional logit. $K_{\\mathrm{eff}}$ direction is perfectly concordant (36/36); $\\eta_{\\max}$ shows 2 discordances (both at high $K$ where the coefficient is near zero). Fractional logit significance is computed with clustered SE (max-$p$, BH FDR $\\alpha{=}0.05$).}\n\\label{tab:fraclogit_detail}\n\\end{table}",
      "numLines": 15,
      "startLine": 1020,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_012TP3UvFeZcKDYTj8vW4R3H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 1190,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1dc284d2-ac90-4268-9974-8b9c536986f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pZNdFU12bmRtabuYpgmXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17720,
      "cache_read_input_tokens": 53354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17720
      },
      "output_tokens": 10,
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

_source line 81 · 2026-05-25T21:11:36.274Z_

<details><summary>↩ Tool result · `toolu_012TP3UvFeZcKDYTj8vW4R3H`</summary>

```text
1190	\end{table*}
1191	
1192	\paragraph{The Capability--Diversity Tradeoff.} Practitioners face a fundamental tension: maximizing $K_{\mathrm{eff}}$ (sampling diverse model families) mechanically introduces less capable models that inflate $\eta_{\max}$, while selecting only capable models compresses $K_{\mathrm{eff}}$. The empirical evidence suggests resolving this tradeoff in favor of capability: $\min(\eta_{\max})$ selection dominates in all 12 conditions at $K{=}3$ (Appendix~\ref{app:panel_selection}), and the weakest link's predictive power, while diminishing with $K$, remains positive. This favors a two-step strategy: (1) set a capability floor (e.g., $\eta_j{<}0.15$ mean ASR across attacks), then (2) maximize cross-family diversity within the qualified pool. The near-chance model analysis (Appendix~\ref{app:near_chance}) provides the empirical basis for this floor: excluding models below the 0.35 accuracy threshold strengthens rather than weakens the diversity signal.
1193	
1194	\paragraph{When Diversity Helps vs.\ Hurts.} The positive $K_{\mathrm{eff}}$--ASR association is a descriptive finding, not a causal claim: observationally, more diverse panels tend to be more vulnerable. This does not mean diversity \emph{causes} vulnerability; the confound with capability ($r{=}0.70$--$0.81$) prevents causal identification from observational data alone. The practical implication is that practitioners should not seek to maximize diversity without controlling for capability. Capability-matched panels (Pool~A) show that when capability is equalized, the residual diversity signal persists (9/12 significant at $K{=}5$), suggesting that inter-judge independence has an independent (though not causally identified) contribution to vulnerability structure. Future work with training-based diversity interventions \citep{kariyappa2019improving,pang2019improving} could provide causal evidence.
1195	
1196	\paragraph{Aggregation Rule Selection.} Bayesian calibration provides partial protection against adversarial manipulation by downweighting unreliable judges ($R^2{=}0.087$ at $K{=}3$ vs.\ $R^2{=}0.327$ for majority voting). However, this protection is not uniform: Bayesian neutralization requires accurate clean priors, and an adaptive adversary aware of the calibration procedure could target the prior estimation itself \citep{tambe2011security}. For general use, majority voting offers the best balance of simplicity and resistance: its $K_{\mathrm{eff}}$ significance (12/12 at $K{=}3$) confirms that diversity affects it, but its predictability ($R^2{=}0.327$) is substantially lower than threshold voting ($R^2{=}0.829$), indicating moderate composition sensitivity. Weighted voting offers marginal improvement over majority voting at the cost of requiring clean accuracy estimates.
1197	
1198	\subsection{Experimental Infrastructure and Reproducibility}
1199	\label{app:infrastructure}
1200	
1201	\paragraph{Model Details.} Table~\ref{tab:model_details} provides the full specification of the 15-judge pool. All models were accessed between May 15--22, 2026, with API versions pinned where available. Local models use AWQ 4-bit quantization \citep{lin2024awq} served via vLLM \citep{kwon2023efficient} on a single NVIDIA RTX 6000 Ada (48~GB).
1202	
1203	\begin{table*}[t]
1204	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6b525a5c-7d57-44de-9fe3-5be69983abac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\\end{table*}\n\n\\paragraph{The Capability--Diversity Tradeoff.} Practitioners face a fundamental tension: maximizing $K_{\\mathrm{eff}}$ (sampling diverse model families) mechanically introduces less capable models that inflate $\\eta_{\\max}$, while selecting only capable models compresses $K_{\\mathrm{eff}}$. The empirical evidence suggests resolving this tradeoff in favor of capability: $\\min(\\eta_{\\max})$ selection dominates in all 12 conditions at $K{=}3$ (Appendix~\\ref{app:panel_selection}), and the weakest link's predictive power, while diminishing with $K$, remains positive. This favors a two-step strategy: (1) set a capability floor (e.g., $\\eta_j{<}0.15$ mean ASR across attacks), then (2) maximize cross-family diversity within the qualified pool. The near-chance model analysis (Appendix~\\ref{app:near_chance}) provides the empirical basis for this floor: excluding models below the 0.35 accuracy threshold strengthens rather than weakens the diversity signal.\n\n\\paragraph{When Diversity Helps vs.\\ Hurts.} The positive $K_{\\mathrm{eff}}$--ASR association is a descriptive finding, not a causal claim: observationally, more diverse panels tend to be more vulnerable. This does not mean diversity \\emph{causes} vulnerability; the confound with capability ($r{=}0.70$--$0.81$) prevents causal identification from observational data alone. The practical implication is that practitioners should not seek to maximize diversity without controlling for capability. Capability-matched panels (Pool~A) show that when capability is equalized, the residual diversity signal persists (9/12 significant at $K{=}5$), suggesting that inter-judge independence has an independent (though not causally identified) contribution to vulnerability structure. Future work with training-based diversity interventions \\citep{kariyappa2019improving,pang2019improving} could provide causal evidence.\n\n\\paragraph{Aggregation Rule Selection.} Bayesian calibration provides partial protection against adversarial manipulation by downweighting unreliable judges ($R^2{=}0.087$ at $K{=}3$ vs.\\ $R^2{=}0.327$ for majority voting). However, this protection is not uniform: Bayesian neutralization requires accurate clean priors, and an adaptive adversary aware of the calibration procedure could target the prior estimation itself \\citep{tambe2011security}. For general use, majority voting offers the best balance of simplicity and resistance: its $K_{\\mathrm{eff}}$ significance (12/12 at $K{=}3$) confirms that diversity affects it, but its predictability ($R^2{=}0.327$) is substantially lower than threshold voting ($R^2{=}0.829$), indicating moderate composition sensitivity. Weighted voting offers marginal improvement over majority voting at the cost of requiring clean accuracy estimates.\n\n\\subsection{Experimental Infrastructure and Reproducibility}\n\\label{app:infrastructure}\n\n\\paragraph{Model Details.} Table~\\ref{tab:model_details} provides the full specification of the 15-judge pool. All models were accessed between May 15--22, 2026, with API versions pinned where available. Local models use AWQ 4-bit quantization \\citep{lin2024awq} served via vLLM \\citep{kwon2023efficient} on a single NVIDIA RTX 6000 Ada (48~GB).\n\n\\begin{table*}[t]\n\\centering",
      "numLines": 15,
      "startLine": 1190,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Assistant

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of every location that needs updating. Let me also read the specific lines where the position bias paragraph should be inserted - in results.tex after the `\subsection{Positive Direction Across Attack Types}` section.

Let me now start making all the edits. I'll work through the files systematically.

Actually, wait. There's a significant issue: the per-condition regression tables in the appendix (lines 109-203) have old position bias data. The K=3 table shows:
- MMLU Position: K_eff β=0.104, η=0.418


- ARC Position: K_eff β=0.584, η=-0.011

But the new data shows:
- MMLU Position: K_eff β=-0.334, η=0.516
- ARC Position: K_eff β=-0.372, η=0.378

These tables need updating, but the task doesn't explicitly mention them. I'll focus on the explicit task items, which are mainly about pooled numbers and narrative claims. The per-condition tables are detailed data that would need a separate update task.

Wait, but the FDR summary rows at the bottom of each table DO need updating because they reflect the WC values, which are part of the core task.

Looking at the K=3 table more carefully, I need to update the FDR significance row from 4/12 and 3/12 to 8/12 and 5/12 based on the new WCB counts. Since I'm revising those summary statistics, I should also check whether the individual position bias rows need updating for consistency with the new bootstrap p-values from the reanalysis data. Now I'm comparing the updated regression coefficients for both position bias measures across the K=3 results, and I notice I need to pull the corresponding data for K=5 and K=7 to complete the table, but the JSON file I've accessed so far only contains K=3 entries.

Rather than getting bogged down retrieving all that data upfront, I'll proceed with the major edits across the document files first and circle back to the per-condition table updates once I've made the core changes. I should tackle the simpler sections like the abstract and introduction before moving into the more involved results and analysis sections, since I already have the exact text I need to replace there. Let me organize my edits carefully to ensure each replacement string is unique, then start working through the files systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "a483a8af-faea-475b-83ea-c8e8b7cca8f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EM78YuHuN2BfSuAyjMnjWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3765,
      "cache_read_input_tokens": 71074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3765
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

_source line 83_

Now I have the full picture. Let me start making edits systematically, beginning with the simpler files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "157117fc-d535-4a70-b4f0-c83d17236d45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EM78YuHuN2BfSuAyjMnjWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3765,
      "cache_read_input_tokens": 71074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3765
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

_source line 84_

<details open><summary>🔧 Tool call — Edit · `toolu_01WXHYJHF27kDcpbBBts3atV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex",
  "old_string": "(1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$",
  "new_string": "(1)~diversity is positively associated with vulnerability ($K_{\\mathrm{eff}}$ positive in 10/12 conditions, $\\kappa$-diversity 12/12), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "18b28e3c-4e21-4359-a6a9-08a0c1d914e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EM78YuHuN2BfSuAyjMnjWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3765,
      "cache_read_input_tokens": 71074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3765
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

_source line 85 · 2026-05-25T21:12:12.041Z_

<details><summary>↩ Tool result · reported error · `toolu_01WXHYJHF27kDcpbBBts3atV`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "d17014c1-1877-4f35-88e3-b3cd1280743f",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Edit · `toolu_01Eax4QqPLg71TRUdqtLVurr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex",
  "old_string": "$\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; CI crosses zero at $K{\\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions)",
  "new_string": "$\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; CI crosses zero at $K{\\geq}5$), while diversity is positively associated with vulnerability (10/12 conditions)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "5631ec25-1348-4812-8a59-869bb9f70317",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EM78YuHuN2BfSuAyjMnjWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3765,
      "cache_read_input_tokens": 71074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3765
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

_source line 87 · 2026-05-25T21:12:14.890Z_

<details><summary>↩ Tool result · reported error · `toolu_01Eax4QqPLg71TRUdqtLVurr`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "5a859a2c-cfff-4833-b43a-c8341e0f4ddf",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Edit · `toolu_01Q12kjXgLb8ZMNhQKHHSK3F`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex",
  "old_string": "all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)",
  "new_string": "all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients in 10/12 conditions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "b81fc78d-1321-4a32-b910-ec8727fa374f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EM78YuHuN2BfSuAyjMnjWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3765,
      "cache_read_input_tokens": 71074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3765
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

_source line 89 · 2026-05-25T21:12:16.219Z_

<details><summary>↩ Tool result · reported error · `toolu_01Q12kjXgLb8ZMNhQKHHSK3F`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1ce8abf1-03e7-49de-9a17-e0fd1e800e88",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---


### Assistant

_source line 90_

<details><summary>Logged reasoning block</summary>

```text
I need to read the files directly (not through agents) before editing them. Let me read all the files I need to edit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6e9ab682-7f57-4fa2-a365-01b70c513750",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsWM94jBG1EYykFci65Ymm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2194,
      "cache_read_input_tokens": 74839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2194
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

_source line 91_

Need to read files directly before editing. Let me read all files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "40a522fd-785e-4b4d-bd1d-4e8205108392",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsWM94jBG1EYykFci65Ymm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2194,
      "cache_read_input_tokens": 74839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2194
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

_source line 92_

<details open><summary>🔧 Tool call — Read · `toolu_01NCfjby27sGkBQETe5HDif9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "c3dd0f54-72c3-49d6-bd4f-8df9c1aa0fac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsWM94jBG1EYykFci65Ymm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2194,
      "cache_read_input_tokens": 74839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2194
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

_source line 93 · 2026-05-25T21:12:21.755Z_

<details><summary>↩ Tool result · `toolu_01NCfjby27sGkBQETe5HDif9`</summary>

```text
1	% Mirror of abstract in main.tex — do not edit here.
2	
3	Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\eta_{\max}$) and effective independence ($K_{\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\eta_{\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; confidence interval crosses zero at $K{\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\%$ at $\alpha{=}5\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "03bd922b-a357-493f-af64-2fe95abf1742",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex",
      "content": "% Mirror of abstract in main.tex — do not edit here.\n\nMulti-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational.\n",
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

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_0114oVDPqRfWCCTi38T464ih`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "e452cab7-8556-4518-837d-059ce9630891",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsWM94jBG1EYykFci65Ymm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2194,
      "cache_read_input_tokens": 74839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2194
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

_source line 95 · 2026-05-25T21:12:22.294Z_

<details><summary>↩ Tool result · `toolu_0114oVDPqRfWCCTi38T464ih`</summary>

```text
1	\section{Conclusion}
2	
3	The weakest link diminishes: $\eta_{\max}$'s predictive power declines monotonically (pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; CI crosses zero at $K{\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\geq}5$, $K_{\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\min \eta_{\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "91c5f35c-2425-4302-aee1-8be02f9397bd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\nThe weakest link diminishes: $\\eta_{\\max}$'s predictive power declines monotonically (pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; CI crosses zero at $K{\\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\\geq}5$, $K_{\\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\\min \\eta_{\\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.\n",
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

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01GRGLZngbxxBjwLKsGxXEK6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "160d1fc9-b353-4195-89d1-94ace88eb103",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsWM94jBG1EYykFci65Ymm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2194,
      "cache_read_input_tokens": 74839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2194
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

_source line 97 · 2026-05-25T21:12:22.767Z_

<details><summary>↩ Tool result · `toolu_01GRGLZngbxxBjwLKsGxXEK6`</summary>

```text
1	\section{Introduction}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=0.78\textwidth]{figures/fig_framework.pdf}
6	\caption{The diminishing weakest link in LLM judge panels. \textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\eta_{\max}$) dominates vulnerability ($\hat{\beta}_{\mathrm{std}}{=}0.264$). \textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \textbf{(c)}~In large panels ($K{\geq}5$), inter-judge diversity ($K_{\mathrm{eff}}$, $\hat{\beta}_{\mathrm{std}}{=}0.437$) drives vulnerability while $\eta_{\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}
7	\label{fig:framework}
8	\end{figure*}
9	
10	Multi-judge panels have become the dominant defense against bias and manipulation in Large Language Model (LLM) evaluation. After \citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, an approach inspired by Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \citep{lamport1982byzantine,castro1999practical}. A recent systematization reports that 7-model committees reduce attack success rates (ASR) from 50--68\% to 10--19\% \citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation, yet this framing conflates two distinct sources of robustness: the quality of individual judges and the independence among them.
11	
12	The conflation matters because the BFT analogy breaks down in the LLM judge setting. BFT adversaries control faulty nodes from within; evaluation adversaries manipulate inputs from without, and shared pretraining corpora create correlated failure modes that violate the independence assumption underlying majority-vote guarantees \citep{schneier2000secrets}. No existing work disentangles diversity from individual robustness across panel sizes, so the relative contribution of each factor to observed ASR reductions remains unclear.
13	
14	We address this gap by decomposing panel vulnerability into two predictors (Figure~\ref{fig:framework}): weakest-link susceptibility ($\eta_{\max}$, the maximum individual attack success rate in a panel) and effective independent channels ($K_{\mathrm{eff}}$, an information-theoretic measure of judge independence). Controlled experiments across 15 models (9 API, 6 local quantized), $K \in \{3,5,7\}$, six attack types, and two multiple-choice benchmarks (Massive Multitask Language Understanding [MMLU] and the AI2 Reasoning Challenge [ARC]) reveal two robust patterns and one metric-sensitive observation.
15	
16	These findings yield three contributions:
17	\begin{enumerate}
18	\item \textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\mathrm{eff}}$ and $\kappa$-diversity \citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\% of conditions (\S\ref{sec:dominance}, \S\ref{sec:gam_taxonomy}).
19	\item \textbf{Diminishing weakest link.} $\eta_{\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\mathrm{eff}}$ significance increases ($4 \to 7 \to 8$/12) while $\kappa$-diversity decreases ($8 \to 7 \to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\S\ref{sec:cross_k}).
20	\item \textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\mathrm{eff}}$ (5+/1$-$) but $\eta_{\max}$ persists (9/12), so the defense is partial (\S\ref{sec:aggregation}, \S\ref{sec:analysis}).
21	\end{enumerate}
22	
23	All findings are associational; the diversity--capability confound ($r{=}0.70$--$0.81$; \S\ref{sec:analysis}) precludes causal claims.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "d875dcbf-8d7e-4657-a427-1354fbc035fd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.78\\textwidth]{figures/fig_framework.pdf}\n\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.264$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.437$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}\n\\label{fig:framework}\n\\end{figure*}\n\nMulti-judge panels have become the dominant defense against bias and manipulation in Large Language Model (LLM) evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, an approach inspired by Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization reports that 7-model committees reduce attack success rates (ASR) from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation, yet this framing conflates two distinct sources of robustness: the quality of individual judges and the independence among them.\n\nThe conflation matters because the BFT analogy breaks down in the LLM judge setting. BFT adversaries control faulty nodes from within; evaluation adversaries manipulate inputs from without, and shared pretraining corpora create correlated failure modes that violate the independence assumption underlying majority-vote guarantees \\citep{schneier2000secrets}. No existing work disentangles diversity from individual robustness across panel sizes, so the relative contribution of each factor to observed ASR reductions remains unclear.\n\nWe address this gap by decomposing panel vulnerability into two predictors (Figure~\\ref{fig:framework}): weakest-link susceptibility ($\\eta_{\\max}$, the maximum individual attack success rate in a panel) and effective independent channels ($K_{\\mathrm{eff}}$, an information-theoretic measure of judge independence). Controlled experiments across 15 models (9 API, 6 local quantized), $K \\in \\{3,5,7\\}$, six attack types, and two multiple-choice benchmarks (Massive Multitask Language Understanding [MMLU] and the AI2 Reasoning Challenge [ARC]) reveal two robust patterns and one metric-sensitive observation.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity \\citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).\n\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).\n\\item \\textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12), so the defense is partial (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nAll findings are associational; the diversity--capability confound ($r{=}0.70$--$0.81$; \\S\\ref{sec:analysis}) precludes causal claims.\n",
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

_source line 98_

<details open><summary>🔧 Tool call — Read · `toolu_01QazY4BUCHTU9182m5C3JnV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "27540fbe-5c71-4d29-a39a-0f011c562dfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsWM94jBG1EYykFci65Ymm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2194,
      "cache_read_input_tokens": 74839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2194
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

_source line 99 · 2026-05-25T21:12:23.240Z_

<details><summary>↩ Tool result · `toolu_01QazY4BUCHTU9182m5C3JnV`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	\usepackage{tcolorbox}
16	\tcbuselibrary{breakable}
17	
18	\newtheorem{theorem}{Theorem}
19	\newtheorem{definition}{Definition}
20	\newtheorem{proposition}{Proposition}
21	
22	\title{The Diminishing Weakest Link: How Panel Size Shifts\\Adversarial Vulnerability Drivers in LLM Judge Panels}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\eta_{\max}$) and effective independence ($K_{\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \in \{3, 5, 7\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\eta_{\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\hat{\beta}_{\mathrm{std}}$: $0.264 \to 0.102 \to 0.084$; confidence interval crosses zero at $K{\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\%$ at $\alpha{=}5\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\footnote{Code and data are available at \url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{threat_model}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{conclusion}
40	
41	\section*{Limitations}
42	
43	\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.
44	\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\geq}20$ threshold at all panel sizes \citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\mathrm{eff}}$ vs.\ $\kappa$-diversity show opposite $K$-trends).
45	\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \in \{3,5,7\}$; the predictor shift threshold $K^*$ is not precisely identified.
46	\textbf{Aggregation scope.} We examine only majority vote, threshold, and Bayesian calibration as aggregation rules; more sophisticated strategies (e.g., weighted voting, learned aggregation, or iterative deliberation among judges) may alter the diversity--robustness relationship and are not explored here.
47	\textbf{Temporal snapshot.} All API model evaluations were collected during a fixed time window; providers may update model weights or safety filters without notice, potentially altering individual susceptibility profiles and panel-level robustness patterns.
48	
49	\bibliography{references}
50	
51	\input{appendix}
52	\input{appendix_attacks}
53	
54	\end{document}
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1558da9b-5435-4410-9147-a54fb63370dc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tcolorbox}\n\\tcbuselibrary{breakable}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{definition}{Definition}\n\\newtheorem{proposition}{Proposition}\n\n\\title{The Diminishing Weakest Link: How Panel Size Shifts\\\\Adversarial Vulnerability Drivers in LLM Judge Panels}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{threat_model}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{conclusion}\n\n\\section*{Limitations}\n\n\\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.\n\\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\\geq}20$ threshold at all panel sizes \\citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\\mathrm{eff}}$ vs.\\ $\\kappa$-diversity show opposite $K$-trends).\n\\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \\in \\{3,5,7\\}$; the predictor shift threshold $K^*$ is not precisely identified.\n\\textbf{Aggregation scope.} We examine only majority vote, threshold, and Bayesian calibration as aggregation rules; more sophisticated strategies (e.g., weighted voting, learned aggregation, or iterative deliberation among judges) may alter the diversity--robustness relationship and are not explored here.\n\\textbf{Temporal snapshot.} All API model evaluations were collected during a fixed time window; providers may update model weights or safety filters without notice, potentially altering individual susceptibility profiles and panel-level robustness patterns.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_attacks}\n\n\\end{document}\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  }
}
```

</details>

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Read · `toolu_011LZP7vNEfjfQbmCmv5o631`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "e7a41c8f-0ed3-466c-b5a0-0c5f94bf3432",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsWM94jBG1EYykFci65Ymm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2194,
      "cache_read_input_tokens": 74839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2194
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

_source line 101 · 2026-05-25T21:12:24.186Z_

<details><summary>↩ Tool result · `toolu_011LZP7vNEfjfQbmCmv5o631`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_regime_transition.pdf}
7	\caption{Predictor shift across panel sizes. $\eta_{\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\alpha{=}0.05$.}
8	\label{fig:regime_transition}
9	\end{figure}
10	
11	\subsection{Weakest-Link Dominance at \texorpdfstring{$K{=}3$}{K=3}}
12	\label{sec:dominance}
13	
14	Table~\ref{tab:dominance} reports the log-log OLS regression (Equation~\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\ref{tab:models}).
15	
16	Under OLS, $K_{\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\eta_{\max}$ is significant in 10/12 (exceptions: MMLU $\times$ score manipulation and ARC $\times$ position bias), consistent with Proposition~\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\mathrm{eff}}$-dominant, and zero $\eta_{\max}$-dominant conditions. However, the $r = 0.70$ $K_{\mathrm{eff}}$--$\eta_{\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\ref{app:keff_dist}).
17	
18	Figure~\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\eta_{\max}$ 3/12, $K_{\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\mathrm{eff}}$ significance at $K{\geq}5$ (Appendix~\ref{app:crossed_re}).
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\begin{tabular}{lcc}
24	\toprule
25	\textbf{Method} & $\boldsymbol{\eta_{\max}}$ \textbf{sig} & $\boldsymbol{K_{\mathrm{eff}}}$ \textbf{sig} \\
26	\midrule
27	OLS                    & 10/12 & 12/12 \\
28	Clustered SE           & 4/12  & 0/12  \\
29	Mixed effects          & 7/12  & 3/12  \\
30	Wild bootstrap         & 3/12  & 4/12  \\
31	Frac.\ logit (clust.)  & 7/12  & 9/12  \\
32	\bottomrule
33	\end{tabular}
34	\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}
35	\label{tab:method_comparison}
36	\end{table}
37	
38	Power analysis yields MDE $\beta_{\mathrm{std}} = 0.14$ at 80\% power (Appendix~\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.
39	
40	\subsection{The Diminishing Weakest Link Across Panel Sizes}
41	\label{sec:cross_k}
42	
43	The $K{=}3$ pattern is method-sensitive (Table~\ref{tab:method_comparison}), contrasting with $K{\geq}5$ where $K_{\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \in \{3, 5, 7\}$ with max-$p$ correction.
44	
45	Meta-analytic pooling \citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\eta_{\max}$'s pooled $\hat{\beta}_{\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\geq}5$. $K_{\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\%$; Appendix~\ref{app:meta_analytic_details}). Figure~\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\% CIs are in Figure~\ref{fig:forest_plot} (Appendix~\ref{app:effect_size_forest}). The $\eta_{\max}$ decline holds under both $K_{\mathrm{eff}}$ and $\kappa$-diversity.
46	
47	
48	\subsection{Random vs.\ Adaptive Fault Contrast}
49	\label{sec:rf_contrast}
50	
51	Random faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\mathrm{eff}}$ retains power (7/12). The positive $K_{\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \citep{goodfellow2015adversarial,kariyappa2019improving}.
52	
53	\subsection{Positive Direction Across Attack Types}
54	\label{sec:gam_taxonomy}
55	
56	GAM bootstrap confirms positive $K_{\mathrm{eff}}$ direction in all 12 conditions (88.9--100\% positive rate; Figure~\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).
57	
58	\subsection{Aggregation Rules and the Diversity Channel}
59	\label{sec:aggregation}
60	
61	Table~\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.
62	
63	\begin{table}[t]
64	\centering
65	\small
66	\begin{tabular}{lcccc}
67	\toprule
68	\textbf{Method} & \textbf{$\eta_{\max}$ sig} & \textbf{$K_{\mathrm{eff}}$ sig} & \textbf{$K_{\mathrm{eff}}$ $\beta$ dir.} & \textbf{$R^2$} \\
69	\midrule
70	Threshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\
71	Majority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\
72	Weighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\
73	Bayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\
74	\bottomrule
75	\end{tabular}
76	\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}
77	\label{tab:aggregation}
78	\end{table}
79	
80	
81	Predictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\mathrm{eff}}$ (5+/1$-$) but $\eta_{\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\ref{app:aggregation_k7}).
82	
83	\paragraph{Fractional Logit Robustness.}
84	Fractional logit \citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\% directional concordance with OLS (71/72; Appendix~\ref{app:robustness_checks}).
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "a6134387-73a7-4c2f-b92a-0748e2d88c0a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 3/12  & 4/12  \\\\\nFrac.\\ logit (clust.)  & 7/12  & 9/12  \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  }
}
```

</details>

---


### Tool call

_source line 102_

<details open><summary>🔧 Tool call — Read · `toolu_01E7QQewTEPjTNDUap8oo6Vo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "24ca6cef-1e9c-40a8-a007-2fb606053812",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsWM94jBG1EYykFci65Ymm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2194,
      "cache_read_input_tokens": 74839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2194
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

_source line 103 · 2026-05-25T21:12:24.414Z_

<details><summary>↩ Tool result · `toolu_01E7QQewTEPjTNDUap8oo6Vo`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\paragraph{Diversity--Capability Confound.}
5	$K_{\mathrm{eff}}$ and $\eta_{\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\approx}2.0$--$2.9$; Figure~\ref{fig:keff_eta_scatter}, Appendix~\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \citep{cinelli2020making} shows the confound could account for the association in 69\% of conditions (Appendix~\ref{app:sensitivity}), though fractional logit confirms the positive association (9/12 at all $K$). Causal attribution requires capability-controlled designs (Appendices~\ref{app:sensitivity_poolA},~\ref{app:cross_benchmark}).
6	
7	\paragraph{API-Only vs.\ Full Pool.}
8	Restricting to 9 API models removes the AWQ confound but increases collinearity ($r{=}0.85$): $\eta_{\max}$ retains significance (8/12) while $K_{\mathrm{eff}}$ drops (2--3/12); the API-only pool lacks statistical power (MDE $> 0.9$; Appendices~\ref{app:quant_dummy},~\ref{app:random_subsample}).
9	
10	\paragraph{Aggregation and Deployment.}
11	Aggregation rules influence predictability but not $K_{\mathrm{eff}}$'s direction (Figure~\ref{fig:aggregation_heatmap}). Threshold voting yields the highest $R^2$ ($0.83$ at $K{=}3$), while Bayesian calibration nearly neutralizes panel composition effects ($R^2{\leq}0.17$ across all $K$). At $K{=}7$, Bayesian calibration fully neutralizes $K_{\mathrm{eff}}$ (0/12; Appendix~\ref{app:bayesian_entropy}). Robustness-first selection ($\min \eta_{\max}$) achieves lowest ASR in all 12 conditions (Appendix~\ref{app:panel_selection}), confirming that selecting judges by individual robustness dominates diversity-maximizing strategies regardless of panel size. Clean $K_{\mathrm{eff}}$ is stable under 4/6 attacks ($\rho{\geq}0.91$; Appendix~\ref{app:attacked_keff}), offering a deployable metric from clean-condition agreement alone.
12	
13	\paragraph{Metric Sensitivity of the Diversity Trajectory.}
14	The diversity significance trajectory is operationalization-dependent: $K_{\mathrm{eff}}$ significance increases ($4 \to 7 \to 8$/12) while $\kappa$-diversity \citep{kuncheva2003measures} decreases ($8 \to 7 \to 6$/12; Appendix~\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \to 4 \to 0$; Appendix~\ref{app:shannon_entropy}). Both $K_{\mathrm{eff}}$ and $\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\eta_{\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "f7cbf250-4543-4b7c-9cc6-63a706243544",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Diversity--Capability Confound.}\n$K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\\approx}2.0$--$2.9$; Figure~\\ref{fig:keff_eta_scatter}, Appendix~\\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \\citep{cinelli2020making} shows the confound could account for the association in 69\\% of conditions (Appendix~\\ref{app:sensitivity}), though fractional logit confirms the positive association (9/12 at all $K$). Causal attribution requires capability-controlled designs (Appendices~\\ref{app:sensitivity_poolA},~\\ref{app:cross_benchmark}).\n\n\\paragraph{API-Only vs.\\ Full Pool.}\nRestricting to 9 API models removes the AWQ confound but increases collinearity ($r{=}0.85$): $\\eta_{\\max}$ retains significance (8/12) while $K_{\\mathrm{eff}}$ drops (2--3/12); the API-only pool lacks statistical power (MDE $> 0.9$; Appendices~\\ref{app:quant_dummy},~\\ref{app:random_subsample}).\n\n\\paragraph{Aggregation and Deployment.}\nAggregation rules influence predictability but not $K_{\\mathrm{eff}}$'s direction (Figure~\\ref{fig:aggregation_heatmap}). Threshold voting yields the highest $R^2$ ($0.83$ at $K{=}3$), while Bayesian calibration nearly neutralizes panel composition effects ($R^2{\\leq}0.17$ across all $K$). At $K{=}7$, Bayesian calibration fully neutralizes $K_{\\mathrm{eff}}$ (0/12; Appendix~\\ref{app:bayesian_entropy}). Robustness-first selection ($\\min \\eta_{\\max}$) achieves lowest ASR in all 12 conditions (Appendix~\\ref{app:panel_selection}), confirming that selecting judges by individual robustness dominates diversity-maximizing strategies regardless of panel size. Clean $K_{\\mathrm{eff}}$ is stable under 4/6 attacks ($\\rho{\\geq}0.91$; Appendix~\\ref{app:attacked_keff}), offering a deployable metric from clean-condition agreement alone.\n\n\\paragraph{Metric Sensitivity of the Diversity Trajectory.}\nThe diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  }
}
```

</details>

---


### Assistant

_source line 104_

<details><summary>Logged reasoning block</summary>

```text
Now I've read all the files. Let me also read the appendix.tex since I need to edit it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "113de613-1e78-4687-bc2b-d1d836f7976c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJXApJ4SDtTs2YzdFMtaiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7629,
      "cache_read_input_tokens": 77033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7629
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

_source line 105_

Now I need to read the appendix too.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "4b1c4d64-1be3-4cf6-a52f-e37b2ef1868f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJXApJ4SDtTs2YzdFMtaiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7629,
      "cache_read_input_tokens": 77033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7629
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

_source line 106_

<details open><summary>🔧 Tool call — Read · `toolu_01Kya55z3aDMKpWS3VqCk7Je`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 0,
  "limit": 140
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "49462d48-b5f6-4506-8514-2d0bff65b986",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJXApJ4SDtTs2YzdFMtaiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7629,
      "cache_read_input_tokens": 77033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7629
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

_source line 107 · 2026-05-25T21:12:33.863Z_

<details><summary>↩ Tool result · `toolu_01Kya55z3aDMKpWS3VqCk7Je`</summary>

```text
0	\appendix
1	
2	\section{Proof of Proposition~\ref{thm:monotonicity}}
3	\label{app:proof}
4	
5	The replaced judge $J_K'$ is \emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \geq t$ regardless of the $K$-th judge:
6	\begin{align}
7	\mathrm{ASR}(\mathcal{P}, a) &= \Pr(S \geq t) + \Pr(S = t{-}1) \cdot \Pr(X_K^a {=} 1 \mid S = t{-}1).
8	\end{align}
9	Since $\Pr(X_{K'}^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K}) \geq \Pr(X_K^a {=} 1 \mid \mathbf{X}_{-K}^a {=} \mathbf{x}_{-K})$ for all attacks $a$ and realizations $\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\mathcal{P}'$ than for $\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\mathrm{ASR}^*(\mathcal{P}') \geq \mathrm{ASR}^*(\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\mathcal{A}$.
10	
11	\section{Robustness Correction Methods}
12	\label{app:robustness_methods}
13	
14	The 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.
15	
16	\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.
17	
18	\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effects model with a random intercept for the judge occupying that position, estimating $K_{\mathrm{eff}}$ and $\eta_{\max}$ as fixed effects. The reported $p$-value for each coefficient is the maximum across the three models.
19	
20	\paragraph{Wild Cluster Bootstrap.} We perform $B{=}9{,}999$ bootstrap resamples using Rademacher weights, clustering by each of the three panel positions in turn and taking the maximum $p$-value across positions (the most conservative aggregation). This approach avoids distributional assumptions on the cluster structure.
21	
22	\subsection{Bootstrap Convergence and Weight Diagnostics}
23	\label{app:bootstrap_convergence}
24	
25	Our primary wild cluster bootstrap uses $B{=}9{,}999$ Rademacher resamples. We assess convergence by comparing significance counts at $B \in \{999, 4{,}999, 9{,}999\}$ and contrasting Rademacher with Mammen two-point weights.
26	
27	\paragraph{$B$-Value Stability.} Table~\ref{tab:bootstrap_B} reports FDR-significant $K_{\mathrm{eff}}$ counts across bootstrap replications. Significance counts stabilize by $B{=}4{,}999$: the maximum discrepancy between $B{=}4{,}999$ and $B{=}9{,}999$ is $\pm 1$ condition across all three $K$ values, and the mean absolute $p$-value shift is ${<}0.003$. The $B{=}999$ configuration shows occasional instability (up to $\pm 2$ discrepancy at $K{=}5$), justifying our choice of $B{=}9{,}999$.
28	
29	\begin{table}[h]
30	\centering
31	\small
32	\begin{tabular}{rcccc}
33	\toprule
34	$\boldsymbol{K}$ & $\boldsymbol{B{=}999}$ & $\boldsymbol{B{=}4{,}999}$ & $\boldsymbol{B{=}9{,}999}$ & $\boldsymbol{\Delta_{999 \to 9999}}$ \\
35	\midrule
36	3 & 3/12 & 4/12 & 4/12 & $+1$ \\
37	5 & 5/12 & 7/12 & 7/12 & $+2$ \\
38	7 & 7/12 & 8/12 & 8/12 & $+1$ \\
39	\bottomrule
40	\end{tabular}
41	\caption{Bootstrap convergence: FDR-significant $K_{\mathrm{eff}}$ counts by number of resamples ($B$). Wild cluster bootstrap with Rademacher weights, max-$p$ across $K$ positions, BH FDR $\alpha{=}0.05$. Counts stabilize by $B{=}4{,}999$.}
42	\label{tab:bootstrap_B}
43	\end{table}
44	
45	\paragraph{Rademacher vs.\ Mammen Weights.} Rademacher weights assign $\pm 1$ with equal probability; Mammen two-point weights use $\{-(\sqrt{5}-1)/2, (\sqrt{5}+1)/2\}$ with asymmetric probabilities to preserve the third moment \citep{mackinnon2018wild}. In our setting, both weight distributions yield identical significance counts at all three $K$ values (4/12, 7/12, 8/12), with maximum $p$-value divergence of 0.008 across all 36 conditions. The Webb six-point distribution (used for the Shannon MI comparison in Appendix~\ref{app:shannon_entropy}) produces marginally different results at $K{=}3$ due to the low cluster count ($G{=}13$), where the discrete support of six-point weights interacts with the small number of sign permutations. All primary analyses use Rademacher weights for simplicity and comparability with the Monte Carlo calibration (Appendix~\ref{app:monte_carlo}).
46	
47	\paragraph{Max-$p$ vs.\ Alternative Aggregation.} We aggregate $p$-values across $K$ position-clusterings by taking the maximum (most conservative). Alternative aggregations---median $p$ and Bonferroni-corrected minimum $p$---produce slightly different significance counts. At $K{=}5$: max-$p$ yields 7/12, median yields 8/12, and Bonferroni-min yields 6/12. The max-$p$ approach is recommended for combinatorial designs where cluster membership is non-nested \citep{mackinnon2018wild}, since it guards against inflated significance from any single clustering being anti-conservative. All reported results use max-$p$.
48	
49	\section{Crossed Random Effects Analysis}
50	\label{app:crossed_re}
51	
52	The one-way clustering in Appendix~\ref{app:robustness_methods} treats each judge position independently, but panels exhibit \emph{crossed} random effects: judge $j$ may occupy position~1 in one panel and position~2 in another, inducing a multi-membership structure. At $K{=}7$, each judge appears in $\binom{14}{6} = 3{,}003$ of $6{,}435$ panels (46.7\%), making crossed membership the dominant source of residual correlation.
53	
54	We fit multi-membership cluster-robust variance estimators (CRVE) using a sandwich estimator with $t(G{-}1) = t(14)$ reference distribution, where $G{=}15$ is the number of judges. Table~\ref{tab:crossed_re} compares bootstrap and crossed RE significance.
55	
56	\begin{table}[h]
57	\centering
58	\small
59	\begin{tabular}{rcccc}
60	\toprule
61	& \multicolumn{2}{c}{\textbf{Bootstrap}} & \multicolumn{2}{c}{\textbf{Crossed RE (FDR)}} \\
62	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
63	$\boldsymbol{K}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & $\boldsymbol{\eta_{\max}}$ & $\boldsymbol{K_{\mathrm{eff}}}$ & $\boldsymbol{\eta_{\max}}$ \\
64	\midrule
65	3 & 4/12 & 3/12 & 0/12 & 1/12 \\
66	5 & 7/12 & 2/12 & \textbf{8/12} & 3/12 \\
67	7 & 8/12 & 1/12 & \textbf{8/12} & 2/12 \\
68	\bottomrule
69	\end{tabular}
70	\caption{Crossed random effects vs.\ wild cluster bootstrap significance (BH FDR $\alpha{=}0.05$). Multi-membership CRVE with $t(14)$ distribution. At $K{\geq}5$, $K_{\mathrm{eff}}$ retains 8/12 significance under crossed RE, matching or exceeding bootstrap. At $K{=}3$, the conservative $t(14)$ distribution with only 455 panels produces attenuation to 0/12 (raw $p$-values: 5/12 significant).}
71	\label{tab:crossed_re}
72	\end{table}
73	
74	SE inflation increases with $K$ as judge overlap intensifies: $1.75$--$4.96{\times}$ at $K{=}3$, $6$--$12{\times}$ at $K{=}5$, $10$--$19{\times}$ at $K{=}7$. Despite this inflation, $K_{\mathrm{eff}}$ retains 8/12 significance at $K{\geq}5$ because the effect size is large enough to survive the correction. The $K{=}3$ attenuation (0/12) reflects two compounding factors: the conservative $t(14)$ reference distribution penalizes small-sample inference, and the effect sizes at $K{=}3$ are insufficient to overcome the inflated SEs. Raw (uncorrected) $p$-values show 5/12 conditions significant at $K{=}3$, confirming that the attenuation reflects degrees-of-freedom conservatism rather than absent effects.
75	
76	\section{Per-Condition Effect Size Forest Plot}
77	\label{app:effect_size_forest}
78	
79	\begin{figure*}[t]
80	\centering
81	\includegraphics[width=\textwidth]{figures/fig5_forest_plot.pdf}
82	\caption{Per-condition standardized $\hat{\beta}$ with 95\% CI for $\eta_{\max}$ (left) and $K_{\mathrm{eff}}$ (right) at $K{=}3$ (wild cluster bootstrap).}
83	\label{fig:forest_plot}
84	\end{figure*}
85	
86	\section{Extended Analysis}
87	\label{app:extended_analysis}
88	
89	\begin{figure}[t]
90	\centering
91	\includegraphics[width=\columnwidth]{figures/fig_keff_eta_scatter.pdf}
92	\caption{Panel-level correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ at $K{=}5$ ($n{=}3{,}003$ panels). Full model pool (gray, $r{=}0.81$) exhibits strong collinearity; capability-matched Pool~A (orange, $r{=}0.50$, 126 panels) shows reduced confounding.}
93	\label{fig:keff_eta_scatter}
94	\end{figure}
95	
96	\begin{figure}[t]
97	\centering
98	\includegraphics[width=\columnwidth]{figures/fig_dominance_heatmap.pdf}
99	\caption{Per-condition predictor dominance across panel sizes (wild cluster bootstrap, BH FDR $\alpha{=}0.05$). At $K{=}3$, dominance is heterogeneous (co-dominant, $K_{\mathrm{eff}}$-only, $\eta_{\max}$-only, and non-significant conditions coexist); at $K{\geq}5$, $K_{\mathrm{eff}}$ dominates uniformly while $\eta_{\max}$ diminishes substantially.}
100	\label{fig:dominance_heatmap}
101	\end{figure}
102	
103	\subsection{Per-Condition Regression Results}
104	\label{app:per_condition_regression}
105	
106	Tables~\ref{tab:percond_k3}--\ref{tab:percond_k7} report the full per-condition regression results underlying the significance counts in the main text. For each of 12 conditions (2 benchmarks $\times$ 6 attacks), we report the standardized OLS coefficients ($\hat{\beta}_{\mathrm{std}}$), $R^2$, and wild cluster bootstrap $p$-values (max-$p$ across $K$ position clusters, BH FDR $\alpha{=}0.05$).
107	
108	\begin{table*}[t]
109	\centering
110	\footnotesize
111	\setlength{\tabcolsep}{3pt}
112	\begin{tabular}{llccccccc}
113	\toprule
114	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
115	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
116	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
117	\midrule
118	\multirow{6}{*}{MMLU} & Prompt inj. & 0.252 & $1.6{\times}10^{-10}$ & 0.026 & 0.616 & $7.4{\times}10^{-46}$ & 0.003 & 0.663 \\
119	& Sycophancy & 0.166 & $1.2{\times}10^{-4}$ & 0.045 & 0.486 & $1.2{\times}10^{-26}$ & 0.012 & 0.334 \\
120	& Score manip. & 0.033 & 0.607 & 0.689 & 0.598 & $3.6{\times}10^{-19}$ & 0.005 & 0.390 \\
121	& Verbosity & 0.090 & 0.026 & 0.175 & 0.593 & $4.0{\times}10^{-40}$ & 0.001 & 0.407 \\
122	& Position & 0.104 & 0.057 & 0.117 & 0.418 & $1.1{\times}10^{-13}$ & 0.023 & 0.243 \\
123	& Authority & 0.010 & 0.852 & 0.864 & 0.377 & $3.4{\times}10^{-11}$ & 0.008 & 0.147 \\
124	\addlinespace
125	\multirow{6}{*}{ARC} & Prompt inj. & 0.330 & $6.4{\times}10^{-6}$ & 0.015 & 0.244 & $8.0{\times}10^{-4}$ & 0.092 & 0.303 \\
126	& Sycophancy & $-0.192$ & $6.3{\times}10^{-3}$ & 0.023 & 0.492 & $6.7{\times}10^{-12}$ & 0.001 & 0.132 \\
127	& Score manip. & 0.252 & 0.023 & 0.079 & 0.224 & 0.043 & 0.175 & 0.219 \\
128	& Verbosity & 0.146 & 0.051 & 0.112 & 0.343 & $5.0{\times}10^{-6}$ & 0.013 & 0.222 \\
129	& Position & 0.584 & $5.9{\times}10^{-9}$ & 0.004 & $-0.011$ & 0.909 & 0.917 & 0.329 \\
130	& Authority & 0.195 & $2.0{\times}10^{-3}$ & 0.031 & 0.261 & $3.6{\times}10^{-5}$ & 0.046 & 0.181 \\
131	\midrule
132	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{10/12} & \\
133	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{4/12} & \multicolumn{3}{c}{3/12} & \\
134	\bottomrule
135	\end{tabular}
136	\caption{Per-condition regression results at $K{=}3$ (455 panels, 15 models). $\hat{\beta}_{\mathrm{std}}$: standardized OLS coefficient. Boot $p$: wild cluster bootstrap max-$p$ (Rademacher, $B{=}9{,}999$). $R^2$: OLS model fit. FDR significance uses BH correction at $\alpha{=}0.05$. Two $K_{\mathrm{eff}}$ exceptions at $K{=}3$ (score manipulation and authority bias on MMLU) show near-zero coefficients ($\hat{\beta}_{\mathrm{std}}{<}0.04$), indicating that these attacks target individual judge capability rather than exploiting inter-judge independence.}
137	\label{tab:percond_k3}
138	\end{table*}
139	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "182c5060-fba0-4422-bae4-6066da5ee5ed",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Proof of Proposition~\\ref{thm:monotonicity}}\n\\label{app:proof}\n\nThe replaced judge $J_K'$ is \\emph{pivotal} exactly when $t{-}1$ of the remaining $K{-}1$ judges have already failed. Formally, let $S = \\sum_{j=1}^{K-1} X_j^a$ denote the number of failures among the shared judges. The panel fails if and only if the $K$-th judge also fails when $S = t{-}1$, or when $S \\geq t$ regardless of the $K$-th judge:\n\\begin{align}\n\\mathrm{ASR}(\\mathcal{P}, a) &= \\Pr(S \\geq t) + \\Pr(S = t{-}1) \\cdot \\Pr(X_K^a {=} 1 \\mid S = t{-}1).\n\\end{align}\nSince $\\Pr(X_{K'}^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K}) \\geq \\Pr(X_K^a {=} 1 \\mid \\mathbf{X}_{-K}^a {=} \\mathbf{x}_{-K})$ for all attacks $a$ and realizations $\\mathbf{x}_{-K}$ (by hypothesis), the second term is weakly larger for $\\mathcal{P}'$ than for $\\mathcal{P}$ under every attack. Taking the supremum over attacks preserves the inequality: $\\mathrm{ASR}^*(\\mathcal{P}') \\geq \\mathrm{ASR}^*(\\mathcal{P})$. The result holds under arbitrary inter-judge correlations and any attack space $\\mathcal{A}$.\n\n\\section{Robustness Correction Methods}\n\\label{app:robustness_methods}\n\nThe 455 panels are constructed combinatorially from 15 shared judges: each judge appears in $\\binom{14}{2} = 91$ panels, inducing correlated residuals across panel-level observations. Standard OLS assumes independent errors, potentially inflating significance. We apply three corrections.\n\n\\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges does not map to a single cluster, we perform three separate one-way clusterings (one for each judge position in the ordered panel tuple) using CR1 bias-corrected sandwich estimators (13 clusters per position). The reported standard error for each coefficient is the maximum across the three clusterings, yielding the most conservative inference.\n\n\\paragraph{Mixed Effects.} For each of the three judge positions, we fit a linear mixed-effects model with a random intercept for the judge occupying that position, estimating $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ as fixed effects. The reported $p$-value for each coefficient is the maximum across the three models.\n\n\\paragraph{Wild Cluster Bootstrap.} We perform $B{=}9{,}999$ bootstrap resamples using Rademacher weights, clustering by each of the three panel positions in turn and taking the maximum $p$-value across positions (the most conservative aggregation). This approach avoids distributional assumptions on the cluster structure.\n\n\\subsection{Bootstrap Convergence and Weight Diagnostics}\n\\label{app:bootstrap_convergence}\n\nOur primary wild cluster bootstrap uses $B{=}9{,}999$ Rademacher resamples. We assess convergence by comparing significance counts at $B \\in \\{999, 4{,}999, 9{,}999\\}$ and contrasting Rademacher with Mammen two-point weights.\n\n\\paragraph{$B$-Value Stability.} Table~\\ref{tab:bootstrap_B} reports FDR-significant $K_{\\mathrm{eff}}$ counts across bootstrap replications. Significance counts stabilize by $B{=}4{,}999$: the maximum discrepancy between $B{=}4{,}999$ and $B{=}9{,}999$ is $\\pm 1$ condition across all three $K$ values, and the mean absolute $p$-value shift is ${<}0.003$. The $B{=}999$ configuration shows occasional instability (up to $\\pm 2$ discrepancy at $K{=}5$), justifying our choice of $B{=}9{,}999$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rcccc}\n\\toprule\n$\\boldsymbol{K}$ & $\\boldsymbol{B{=}999}$ & $\\boldsymbol{B{=}4{,}999}$ & $\\boldsymbol{B{=}9{,}999}$ & $\\boldsymbol{\\Delta_{999 \\to 9999}}$ \\\\\n\\midrule\n3 & 3/12 & 4/12 & 4/12 & $+1$ \\\\\n5 & 5/12 & 7/12 & 7/12 & $+2$ \\\\\n7 & 7/12 & 8/12 & 8/12 & $+1$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Bootstrap convergence: FDR-significant $K_{\\mathrm{eff}}$ counts by number of resamples ($B$). Wild cluster bootstrap with Rademacher weights, max-$p$ across $K$ positions, BH FDR $\\alpha{=}0.05$. Counts stabilize by $B{=}4{,}999$.}\n\\label{tab:bootstrap_B}\n\\end{table}\n\n\\paragraph{Rademacher vs.\\ Mammen Weights.} Rademacher weights assign $\\pm 1$ with equal probability; Mammen two-point weights use $\\{-(\\sqrt{5}-1)/2, (\\sqrt{5}+1)/2\\}$ with asymmetric probabilities to preserve the third moment \\citep{mackinnon2018wild}. In our setting, both weight distributions yield identical significance counts at all three $K$ values (4/12, 7/12, 8/12), with maximum $p$-value divergence of 0.008 across all 36 conditions. The Webb six-point distribution (used for the Shannon MI comparison in Appendix~\\ref{app:shannon_entropy}) produces marginally different results at $K{=}3$ due to the low cluster count ($G{=}13$), where the discrete support of six-point weights interacts with the small number of sign permutations. All primary analyses use Rademacher weights for simplicity and comparability with the Monte Carlo calibration (Appendix~\\ref{app:monte_carlo}).\n\n\\paragraph{Max-$p$ vs.\\ Alternative Aggregation.} We aggregate $p$-values across $K$ position-clusterings by taking the maximum (most conservative). Alternative aggregations---median $p$ and Bonferroni-corrected minimum $p$---produce slightly different significance counts. At $K{=}5$: max-$p$ yields 7/12, median yields 8/12, and Bonferroni-min yields 6/12. The max-$p$ approach is recommended for combinatorial designs where cluster membership is non-nested \\citep{mackinnon2018wild}, since it guards against inflated significance from any single clustering being anti-conservative. All reported results use max-$p$.\n\n\\section{Crossed Random Effects Analysis}\n\\label{app:crossed_re}\n\nThe one-way clustering in Appendix~\\ref{app:robustness_methods} treats each judge position independently, but panels exhibit \\emph{crossed} random effects: judge $j$ may occupy position~1 in one panel and position~2 in another, inducing a multi-membership structure. At $K{=}7$, each judge appears in $\\binom{14}{6} = 3{,}003$ of $6{,}435$ panels (46.7\\%), making crossed membership the dominant source of residual correlation.\n\nWe fit multi-membership cluster-robust variance estimators (CRVE) using a sandwich estimator with $t(G{-}1) = t(14)$ reference distribution, where $G{=}15$ is the number of judges. Table~\\ref{tab:crossed_re} compares bootstrap and crossed RE significance.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Bootstrap}} & \\multicolumn{2}{c}{\\textbf{Crossed RE (FDR)}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n$\\boldsymbol{K}$ & $\\boldsymbol{K_{\\mathrm{eff}}}$ & $\\boldsymbol{\\eta_{\\max}}$ & $\\boldsymbol{K_{\\mathrm{eff}}}$ & $\\boldsymbol{\\eta_{\\max}}$ \\\\\n\\midrule\n3 & 4/12 & 3/12 & 0/12 & 1/12 \\\\\n5 & 7/12 & 2/12 & \\textbf{8/12} & 3/12 \\\\\n7 & 8/12 & 1/12 & \\textbf{8/12} & 2/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Crossed random effects vs.\\ wild cluster bootstrap significance (BH FDR $\\alpha{=}0.05$). Multi-membership CRVE with $t(14)$ distribution. At $K{\\geq}5$, $K_{\\mathrm{eff}}$ retains 8/12 significance under crossed RE, matching or exceeding bootstrap. At $K{=}3$, the conservative $t(14)$ distribution with only 455 panels produces attenuation to 0/12 (raw $p$-values: 5/12 significant).}\n\\label{tab:crossed_re}\n\\end{table}\n\nSE inflation increases with $K$ as judge overlap intensifies: $1.75$--$4.96{\\times}$ at $K{=}3$, $6$--$12{\\times}$ at $K{=}5$, $10$--$19{\\times}$ at $K{=}7$. Despite this inflation, $K_{\\mathrm{eff}}$ retains 8/12 significance at $K{\\geq}5$ because the effect size is large enough to survive the correction. The $K{=}3$ attenuation (0/12) reflects two compounding factors: the conservative $t(14)$ reference distribution penalizes small-sample inference, and the effect sizes at $K{=}3$ are insufficient to overcome the inflated SEs. Raw (uncorrected) $p$-values show 5/12 conditions significant at $K{=}3$, confirming that the attenuation reflects degrees-of-freedom conservatism rather than absent effects.\n\n\\section{Per-Condition Effect Size Forest Plot}\n\\label{app:effect_size_forest}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig5_forest_plot.pdf}\n\\caption{Per-condition standardized $\\hat{\\beta}$ with 95\\% CI for $\\eta_{\\max}$ (left) and $K_{\\mathrm{eff}}$ (right) at $K{=}3$ (wild cluster bootstrap).}\n\\label{fig:forest_plot}\n\\end{figure*}\n\n\\section{Extended Analysis}\n\\label{app:extended_analysis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_keff_eta_scatter.pdf}\n\\caption{Panel-level correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ at $K{=}5$ ($n{=}3{,}003$ panels). Full model pool (gray, $r{=}0.81$) exhibits strong collinearity; capability-matched Pool~A (orange, $r{=}0.50$, 126 panels) shows reduced confounding.}\n\\label{fig:keff_eta_scatter}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_dominance_heatmap.pdf}\n\\caption{Per-condition predictor dominance across panel sizes (wild cluster bootstrap, BH FDR $\\alpha{=}0.05$). At $K{=}3$, dominance is heterogeneous (co-dominant, $K_{\\mathrm{eff}}$-only, $\\eta_{\\max}$-only, and non-significant conditions coexist); at $K{\\geq}5$, $K_{\\mathrm{eff}}$ dominates uniformly while $\\eta_{\\max}$ diminishes substantially.}\n\\label{fig:dominance_heatmap}\n\\end{figure}\n\n\\subsection{Per-Condition Regression Results}\n\\label{app:per_condition_regression}\n\nTables~\\ref{tab:percond_k3}--\\ref{tab:percond_k7} report the full per-condition regression results underlying the significance counts in the main text. For each of 12 conditions (2 benchmarks $\\times$ 6 attacks), we report the standardized OLS coefficients ($\\hat{\\beta}_{\\mathrm{std}}$), $R^2$, and wild cluster bootstrap $p$-values (max-$p$ across $K$ position clusters, BH FDR $\\alpha{=}0.05$).\n\n\\begin{table*}[t]\n\\centering\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccccc}\n\\toprule\n& & \\multicolumn{3}{c}{$\\boldsymbol{K_{\\mathrm{eff}}}$} & \\multicolumn{3}{c}{$\\boldsymbol{\\eta_{\\max}}$} & \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Bench.} & \\textbf{Attack} & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\\\\n\\midrule\n\\multirow{6}{*}{MMLU} & Prompt inj. & 0.252 & $1.6{\\times}10^{-10}$ & 0.026 & 0.616 & $7.4{\\times}10^{-46}$ & 0.003 & 0.663 \\\\\n& Sycophancy & 0.166 & $1.2{\\times}10^{-4}$ & 0.045 & 0.486 & $1.2{\\times}10^{-26}$ & 0.012 & 0.334 \\\\\n& Score manip. & 0.033 & 0.607 & 0.689 & 0.598 & $3.6{\\times}10^{-19}$ & 0.005 & 0.390 \\\\\n& Verbosity & 0.090 & 0.026 & 0.175 & 0.593 & $4.0{\\times}10^{-40}$ & 0.001 & 0.407 \\\\\n& Position & 0.104 & 0.057 & 0.117 & 0.418 & $1.1{\\times}10^{-13}$ & 0.023 & 0.243 \\\\\n& Authority & 0.010 & 0.852 & 0.864 & 0.377 & $3.4{\\times}10^{-11}$ & 0.008 & 0.147 \\\\\n\\addlinespace\n\\multirow{6}{*}{ARC} & Prompt inj. & 0.330 & $6.4{\\times}10^{-6}$ & 0.015 & 0.244 & $8.0{\\times}10^{-4}$ & 0.092 & 0.303 \\\\\n& Sycophancy & $-0.192$ & $6.3{\\times}10^{-3}$ & 0.023 & 0.492 & $6.7{\\times}10^{-12}$ & 0.001 & 0.132 \\\\\n& Score manip. & 0.252 & 0.023 & 0.079 & 0.224 & 0.043 & 0.175 & 0.219 \\\\\n& Verbosity & 0.146 & 0.051 & 0.112 & 0.343 & $5.0{\\times}10^{-6}$ & 0.013 & 0.222 \\\\\n& Position & 0.584 & $5.9{\\times}10^{-9}$ & 0.004 & $-0.011$ & 0.909 & 0.917 & 0.329 \\\\\n& Authority & 0.195 & $2.0{\\times}10^{-3}$ & 0.031 & 0.261 & $3.6{\\times}10^{-5}$ & 0.046 & 0.181 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{10/12} & \\\\\n\\multicolumn{2}{l}{\\textbf{FDR sig (bootstrap)}} & \\multicolumn{3}{c}{4/12} & \\multicolumn{3}{c}{3/12} & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-condition regression results at $K{=}3$ (455 panels, 15 models). $\\hat{\\beta}_{\\mathrm{std}}$: standardized OLS coefficient. Boot $p$: wild cluster bootstrap max-$p$ (Rademacher, $B{=}9{,}999$). $R^2$: OLS model fit. FDR significance uses BH correction at $\\alpha{=}0.05$. Two $K_{\\mathrm{eff}}$ exceptions at $K{=}3$ (score manipulation and authority bias on MMLU) show near-zero coefficients ($\\hat{\\beta}_{\\mathrm{std}}{<}0.04$), indicating that these attacks target individual judge capability rather than exploiting inter-judge independence.}\n\\label{tab:percond_k3}\n\\end{table*}\n",
      "numLines": 140,
      "startLine": 0,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 108_

<details open><summary>🔧 Tool call — Read · `toolu_01TXcFrTbAFZRjwDnJgMhPfx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 140,
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "8c930aac-094a-4047-83d2-ecf6e2a174ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJXApJ4SDtTs2YzdFMtaiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7629,
      "cache_read_input_tokens": 77033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7629
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

_source line 109 · 2026-05-25T21:12:34.257Z_

<details><summary>↩ Tool result · `toolu_01TXcFrTbAFZRjwDnJgMhPfx`</summary>

```text
140	
141	\begin{table*}[t]
142	\centering
143	\footnotesize
144	\setlength{\tabcolsep}{3pt}
145	\begin{tabular}{llccccccc}
146	\toprule
147	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
148	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
149	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
150	\midrule
151	\multirow{6}{*}{MMLU} & Prompt inj. & 0.493 & ${<}10^{-15}$ & 0.002 & 0.370 & ${<}10^{-15}$ & 0.033 & 0.594 \\
152	& Sycophancy & 0.321 & ${<}10^{-15}$ & 0.010 & 0.349 & ${<}10^{-15}$ & 0.028 & 0.325 \\
153	& Score manip. & 0.506 & ${<}10^{-15}$ & 0.003 & 0.075 & 0.001 & 0.620 & 0.297 \\
154	& Verbosity & 0.235 & ${<}10^{-15}$ & 0.005 & 0.445 & ${<}10^{-15}$ & 0.005 & 0.358 \\
155	& Position & 0.149 & ${<}10^{-8}$ & 0.077 & 0.333 & ${<}10^{-15}$ & 0.063 & 0.182 \\
156	& Authority & 0.075 & $3.5{\times}10^{-3}$ & 0.314 & 0.203 & ${<}10^{-10}$ & 0.277 & 0.061 \\
157	\addlinespace
158	\multirow{6}{*}{ARC} & Prompt inj. & 0.583 & ${<}10^{-15}$ & 0.018 & $-0.038$ & 0.095 & 0.746 & 0.327 \\
159	& Sycophancy & $-0.157$ & ${<}10^{-8}$ & 0.172 & 0.374 & ${<}10^{-15}$ & 0.011 & 0.078 \\
160	& Score manip. & 0.443 & ${<}10^{-15}$ & 0.004 & $-0.026$ & 0.274 & 0.912 & 0.189 \\
161	& Verbosity & 0.215 & ${<}10^{-12}$ & 0.100 & 0.276 & ${<}10^{-15}$ & 0.058 & 0.178 \\
162	& Position & 0.881 & ${<}10^{-15}$ & 0.017 & $-0.348$ & ${<}10^{-15}$ & 0.796 & 0.512 \\
163	& Authority & 0.264 & ${<}10^{-15}$ & 0.151 & 0.146 & ${<}10^{-5}$ & 0.342 & 0.120 \\
164	\midrule
165	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{11/12} & \\
166	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{7/12} & \multicolumn{3}{c}{2/12} & \\
167	\bottomrule
168	\end{tabular}
169	\caption{Per-condition regression results at $K{=}5$ (3{,}003 panels, 15 models). Format identical to Table~\ref{tab:percond_k3}. $K_{\mathrm{eff}}$ achieves bootstrap significance in 7/12 conditions with consistently larger effect sizes than at $K{=}3$ (mean $|\hat{\beta}_{\mathrm{std}}|$: 0.361 vs.\ 0.196). $\eta_{\max}$'s bootstrap significance drops to 2/12, with three conditions showing negative coefficients---the predictor shift documented in \S\ref{sec:cross_k}.}
170	\label{tab:percond_k5}
171	\end{table*}
172	
173	\begin{table*}[t]
174	\centering
175	\footnotesize
176	\setlength{\tabcolsep}{3pt}
177	\begin{tabular}{llccccccc}
178	\toprule
179	& & \multicolumn{3}{c}{$\boldsymbol{K_{\mathrm{eff}}}$} & \multicolumn{3}{c}{$\boldsymbol{\eta_{\max}}$} & \\
180	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
181	\textbf{Bench.} & \textbf{Attack} & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\hat{\beta}_{\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\
182	\midrule
183	\multirow{6}{*}{MMLU} & Prompt inj. & 0.574 & ${<}10^{-15}$ & 0.002 & 0.288 & ${<}10^{-15}$ & 0.092 & 0.540 \\
184	& Sycophancy & 0.329 & ${<}10^{-15}$ & 0.017 & 0.266 & ${<}10^{-15}$ & 0.060 & 0.258 \\
185	& Score manip. & 0.605 & ${<}10^{-15}$ & 0.007 & $-0.081$ & ${<}10^{-3}$ & 0.581 & 0.333 \\
186	& Verbosity & 0.204 & ${<}10^{-15}$ & 0.006 & 0.435 & ${<}10^{-15}$ & 0.013 & 0.319 \\
187	& Position & 0.231 & ${<}10^{-15}$ & 0.071 & 0.279 & ${<}10^{-15}$ & 0.110 & 0.186 \\
188	& Authority & 0.005 & 0.722 & 0.905 & 0.116 & ${<}10^{-6}$ & 0.268 & 0.014 \\
189	\addlinespace
190	\multirow{6}{*}{ARC} & Prompt inj. & 0.611 & ${<}10^{-15}$ & 0.063 & $-0.091$ & ${<}10^{-4}$ & 0.237 & 0.337 \\
191	& Sycophancy & $-0.176$ & ${<}10^{-12}$ & 0.326 & 0.372 & ${<}10^{-15}$ & 0.016 & 0.064 \\
192	& Score manip. & 0.316 & ${<}10^{-15}$ & 0.009 & 0.052 & $1.7{\times}10^{-2}$ & 0.539 & 0.112 \\
193	& Verbosity & 0.253 & ${<}10^{-15}$ & 0.044 & 0.238 & ${<}10^{-15}$ & 0.024 & 0.176 \\
194	& Position & 0.831 & ${<}10^{-15}$ & 0.029 & $-0.327$ & ${<}10^{-15}$ & 0.468 & 0.523 \\
195	& Authority & 0.268 & ${<}10^{-15}$ & 0.231 & 0.074 & $2.3{\times}10^{-3}$ & 0.846 & 0.092 \\
196	\midrule
197	\multicolumn{2}{l}{\textbf{FDR sig (OLS)}} & \multicolumn{3}{c}{12/12} & \multicolumn{3}{c}{11/12} & \\
198	\multicolumn{2}{l}{\textbf{FDR sig (bootstrap)}} & \multicolumn{3}{c}{8/12} & \multicolumn{3}{c}{1/12} & \\
199	\bottomrule
200	\end{tabular}
201	\caption{Per-condition regression results at $K{=}7$ (6{,}435 panels, 15 models). Format identical to Table~\ref{tab:percond_k3}. $K_{\mathrm{eff}}$ bootstrap significance reaches 8/12 (vs.\ 4/12 at $K{=}3$), completing the predictor shift. $\eta_{\max}$ drops to 1/12 bootstrap significance, with its coefficient crossing zero in 3/12 conditions. ARC position bias shows the strongest $K_{\mathrm{eff}}$ coefficient ($\hat{\beta}_{\mathrm{std}}{=}0.831$) and the strongest negative $\eta_{\max}$ coefficient ($-0.327$), a pattern present across all three $K$ values.}
202	\label{tab:percond_k7}
203	\end{table*}
204	
205	\subsection{Model Capability and Vulnerability Profiles}
206	\label{app:model_profiles}
207	
208	\begin{figure}[h]
209	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "720b01f3-9e26-4ffb-bd33-4ca8617094dd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\n\\begin{table*}[t]\n\\centering\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccccc}\n\\toprule\n& & \\multicolumn{3}{c}{$\\boldsymbol{K_{\\mathrm{eff}}}$} & \\multicolumn{3}{c}{$\\boldsymbol{\\eta_{\\max}}$} & \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Bench.} & \\textbf{Attack} & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\\\\n\\midrule\n\\multirow{6}{*}{MMLU} & Prompt inj. & 0.493 & ${<}10^{-15}$ & 0.002 & 0.370 & ${<}10^{-15}$ & 0.033 & 0.594 \\\\\n& Sycophancy & 0.321 & ${<}10^{-15}$ & 0.010 & 0.349 & ${<}10^{-15}$ & 0.028 & 0.325 \\\\\n& Score manip. & 0.506 & ${<}10^{-15}$ & 0.003 & 0.075 & 0.001 & 0.620 & 0.297 \\\\\n& Verbosity & 0.235 & ${<}10^{-15}$ & 0.005 & 0.445 & ${<}10^{-15}$ & 0.005 & 0.358 \\\\\n& Position & 0.149 & ${<}10^{-8}$ & 0.077 & 0.333 & ${<}10^{-15}$ & 0.063 & 0.182 \\\\\n& Authority & 0.075 & $3.5{\\times}10^{-3}$ & 0.314 & 0.203 & ${<}10^{-10}$ & 0.277 & 0.061 \\\\\n\\addlinespace\n\\multirow{6}{*}{ARC} & Prompt inj. & 0.583 & ${<}10^{-15}$ & 0.018 & $-0.038$ & 0.095 & 0.746 & 0.327 \\\\\n& Sycophancy & $-0.157$ & ${<}10^{-8}$ & 0.172 & 0.374 & ${<}10^{-15}$ & 0.011 & 0.078 \\\\\n& Score manip. & 0.443 & ${<}10^{-15}$ & 0.004 & $-0.026$ & 0.274 & 0.912 & 0.189 \\\\\n& Verbosity & 0.215 & ${<}10^{-12}$ & 0.100 & 0.276 & ${<}10^{-15}$ & 0.058 & 0.178 \\\\\n& Position & 0.881 & ${<}10^{-15}$ & 0.017 & $-0.348$ & ${<}10^{-15}$ & 0.796 & 0.512 \\\\\n& Authority & 0.264 & ${<}10^{-15}$ & 0.151 & 0.146 & ${<}10^{-5}$ & 0.342 & 0.120 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{11/12} & \\\\\n\\multicolumn{2}{l}{\\textbf{FDR sig (bootstrap)}} & \\multicolumn{3}{c}{7/12} & \\multicolumn{3}{c}{2/12} & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-condition regression results at $K{=}5$ (3{,}003 panels, 15 models). Format identical to Table~\\ref{tab:percond_k3}. $K_{\\mathrm{eff}}$ achieves bootstrap significance in 7/12 conditions with consistently larger effect sizes than at $K{=}3$ (mean $|\\hat{\\beta}_{\\mathrm{std}}|$: 0.361 vs.\\ 0.196). $\\eta_{\\max}$'s bootstrap significance drops to 2/12, with three conditions showing negative coefficients---the predictor shift documented in \\S\\ref{sec:cross_k}.}\n\\label{tab:percond_k5}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\footnotesize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccccc}\n\\toprule\n& & \\multicolumn{3}{c}{$\\boldsymbol{K_{\\mathrm{eff}}}$} & \\multicolumn{3}{c}{$\\boldsymbol{\\eta_{\\max}}$} & \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Bench.} & \\textbf{Attack} & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $\\hat{\\beta}_{\\mathrm{std}}$ & OLS $p$ & Boot $p$ & $R^2$ \\\\\n\\midrule\n\\multirow{6}{*}{MMLU} & Prompt inj. & 0.574 & ${<}10^{-15}$ & 0.002 & 0.288 & ${<}10^{-15}$ & 0.092 & 0.540 \\\\\n& Sycophancy & 0.329 & ${<}10^{-15}$ & 0.017 & 0.266 & ${<}10^{-15}$ & 0.060 & 0.258 \\\\\n& Score manip. & 0.605 & ${<}10^{-15}$ & 0.007 & $-0.081$ & ${<}10^{-3}$ & 0.581 & 0.333 \\\\\n& Verbosity & 0.204 & ${<}10^{-15}$ & 0.006 & 0.435 & ${<}10^{-15}$ & 0.013 & 0.319 \\\\\n& Position & 0.231 & ${<}10^{-15}$ & 0.071 & 0.279 & ${<}10^{-15}$ & 0.110 & 0.186 \\\\\n& Authority & 0.005 & 0.722 & 0.905 & 0.116 & ${<}10^{-6}$ & 0.268 & 0.014 \\\\\n\\addlinespace\n\\multirow{6}{*}{ARC} & Prompt inj. & 0.611 & ${<}10^{-15}$ & 0.063 & $-0.091$ & ${<}10^{-4}$ & 0.237 & 0.337 \\\\\n& Sycophancy & $-0.176$ & ${<}10^{-12}$ & 0.326 & 0.372 & ${<}10^{-15}$ & 0.016 & 0.064 \\\\\n& Score manip. & 0.316 & ${<}10^{-15}$ & 0.009 & 0.052 & $1.7{\\times}10^{-2}$ & 0.539 & 0.112 \\\\\n& Verbosity & 0.253 & ${<}10^{-15}$ & 0.044 & 0.238 & ${<}10^{-15}$ & 0.024 & 0.176 \\\\\n& Position & 0.831 & ${<}10^{-15}$ & 0.029 & $-0.327$ & ${<}10^{-15}$ & 0.468 & 0.523 \\\\\n& Authority & 0.268 & ${<}10^{-15}$ & 0.231 & 0.074 & $2.3{\\times}10^{-3}$ & 0.846 & 0.092 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textbf{FDR sig (OLS)}} & \\multicolumn{3}{c}{12/12} & \\multicolumn{3}{c}{11/12} & \\\\\n\\multicolumn{2}{l}{\\textbf{FDR sig (bootstrap)}} & \\multicolumn{3}{c}{8/12} & \\multicolumn{3}{c}{1/12} & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-condition regression results at $K{=}7$ (6{,}435 panels, 15 models). Format identical to Table~\\ref{tab:percond_k3}. $K_{\\mathrm{eff}}$ bootstrap significance reaches 8/12 (vs.\\ 4/12 at $K{=}3$), completing the predictor shift. $\\eta_{\\max}$ drops to 1/12 bootstrap significance, with its coefficient crossing zero in 3/12 conditions. ARC position bias shows the strongest $K_{\\mathrm{eff}}$ coefficient ($\\hat{\\beta}_{\\mathrm{std}}{=}0.831$) and the strongest negative $\\eta_{\\max}$ coefficient ($-0.327$), a pattern present across all three $K$ values.}\n\\label{tab:percond_k7}\n\\end{table*}\n\n\\subsection{Model Capability and Vulnerability Profiles}\n\\label{app:model_profiles}\n\n\\begin{figure}[h]\n\\centering",
      "numLines": 70,
      "startLine": 140,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Read · `toolu_01LQWRUHUmk2DWhmViiWWEMa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "offset": 290,
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
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "ffd310fb-b577-4476-87c7-aa5b955d342b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJXApJ4SDtTs2YzdFMtaiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7629,
      "cache_read_input_tokens": 77033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7629
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

_source line 111 · 2026-05-25T21:12:35.290Z_

<details><summary>↩ Tool result · `toolu_01LQWRUHUmk2DWhmViiWWEMa`</summary>

```text
290	
291	\subsection{BFT Reversal Mechanism: Detailed Evidence}
292	\label{app:bft_reversal}
293	
294	Under standard OLS, the regression results (Table~\ref{tab:dominance}) show $\eta_{\max}$ significant in 10 of 12 conditions and $K_{\mathrm{eff}}$ positively associated with ASR in all 12. Non-independence correction attenuates both predictors: under wild cluster bootstrap, $\eta_{\max}$ retains 3/12 and $K_{\mathrm{eff}}$ retains 4/12, with $K_{\mathrm{eff}}$ slightly ahead. The directional pattern (all $K_{\mathrm{eff}}$ point estimates positive) persists uniformly. The random-fault contrast (\S\ref{sec:rf_contrast}) sharpens this: under random faults, $K_{\mathrm{eff}}$'s positive association with panel error survives all corrections (2/2 conditions, $R^2 = 0.73$--$0.81$), indicating a genuine relationship whose statistical confidence attenuates under adaptive attack (4/12 after correction).
295	
296	\begin{figure}[h]
297	\centering
298	\includegraphics[width=\columnwidth]{figures/fig2_gam_keff_split.pdf}
299	\caption{GAM bootstrap $K_{\mathrm{eff}}$ effect direction at $K{=}3$ ($B{=}9999$). All 12 conditions show positive $K_{\mathrm{eff}}$ direction (88.9--100\% bootstrap rate). The Kruskal--Wallis test finds no significant magnitude difference between targeted and shared-bias attacks ($p{=}0.200$).}
300	\label{fig:gam_split}
301	\end{figure}
302	
303	Under corrected data (V2), all 12 $K_{\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\times$ sycophancy coefficient ($\hat{\beta}_{\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\hat{\beta}_{\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\% positive rate) and 12/12 at $K{=}5$ (100\%).
304	
305	\subsection{Diversity--Capability Tradeoff}
306	\label{app:diversity_capability}
307	
308	The $r = 0.70$--$0.81$ correlation between $K_{\mathrm{eff}}$ and $\eta_{\max}$ ($K{=}3$ to $K{=}5$) reflects a structural feature of the current LLM ecosystem: maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges. The structural correlation is unaffected by SE correction; it is a property of the model ecosystem, not an artifact of panel overlap. However, the high confound combined with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it.
309	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "4cffeabd-85d8-4ff5-83a4-0413c0840a0c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
      "content": "\n\\subsection{BFT Reversal Mechanism: Detailed Evidence}\n\\label{app:bft_reversal}\n\nUnder standard OLS, the regression results (Table~\\ref{tab:dominance}) show $\\eta_{\\max}$ significant in 10 of 12 conditions and $K_{\\mathrm{eff}}$ positively associated with ASR in all 12. Non-independence correction attenuates both predictors: under wild cluster bootstrap, $\\eta_{\\max}$ retains 3/12 and $K_{\\mathrm{eff}}$ retains 4/12, with $K_{\\mathrm{eff}}$ slightly ahead. The directional pattern (all $K_{\\mathrm{eff}}$ point estimates positive) persists uniformly. The random-fault contrast (\\S\\ref{sec:rf_contrast}) sharpens this: under random faults, $K_{\\mathrm{eff}}$'s positive association with panel error survives all corrections (2/2 conditions, $R^2 = 0.73$--$0.81$), indicating a genuine relationship whose statistical confidence attenuates under adaptive attack (4/12 after correction).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_gam_keff_split.pdf}\n\\caption{GAM bootstrap $K_{\\mathrm{eff}}$ effect direction at $K{=}3$ ($B{=}9999$). All 12 conditions show positive $K_{\\mathrm{eff}}$ direction (88.9--100\\% bootstrap rate). The Kruskal--Wallis test finds no significant magnitude difference between targeted and shared-bias attacks ($p{=}0.200$).}\n\\label{fig:gam_split}\n\\end{figure}\n\nUnder corrected data (V2), all 12 $K_{\\mathrm{eff}}$ OLS coefficients are positive. The previously reported negative ARC $\\times$ sycophancy coefficient ($\\hat{\\beta}_{\\mathrm{std}} = -0.192$) was an artifact of error-as-tie handling; after correction, it becomes positive ($\\hat{\\beta}_{\\mathrm{std}} = +0.257$). GAM bootstrap confirms the uniform positive direction: 12/12 conditions at $K{=}3$ (88.9--100\\% positive rate) and 12/12 at $K{=}5$ (100\\%).\n\n\\subsection{Diversity--Capability Tradeoff}\n\\label{app:diversity_capability}\n\nThe $r = 0.70$--$0.81$ correlation between $K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ ($K{=}3$ to $K{=}5$) reflects a structural feature of the current LLM ecosystem: maximizing panel diversity requires sampling across capability tiers, which systematically introduces less capable and therefore more vulnerable judges. The structural correlation is unaffected by SE correction; it is a property of the model ecosystem, not an artifact of panel overlap. However, the high confound combined with fragile independent significance means that observational regression cannot reliably disentangle diversity's causal contribution from the capability deficit that co-occurs with it.\n",
      "numLines": 20,
      "startLine": 290,
      "totalLines": 1261
    }
  }
}
```

</details>

---


### Assistant

_source line 112_

<details><summary>Logged reasoning block</summary>

```text
Now I've read all the files I need to edit. Let me track what needs to be done and start making edits systematically.

Let me use TodoWrite to track progress, then start making edits.

Let me organize the edits by file:

### abstract.tex
1. "uniformly positively" → remove "uniformly"
2. "12/12 conditions" → "10/12 conditions"
3. "$0.264 \to 0.102 \to 0.084$" → "$0.243 \to 0.091 \to 0.086$"

### main.tex (abstract copy)


Same three changes needed, plus I need to update the limitations section to change bootstrap from "4/12" to "8/12", fractional logit from "9/12" to "10/12", and reword the statement about positive effects from "all 12 conditions" to "10 of 12 conditions".

### introduction.tex
I need to update figure captions with new values (0.264 → 0.243 and 0.437 → 0.353), change the phrasing on line 18 from "all 12 conditions (12/12" to "10 of 12 conditions (10/12", and add the η_max trajectory plus C notation on line 19.

12. Line 19: K_eff WCB trajectory

### results.tex
I need to update the figure caption on line 7 regarding WCB counts. For line 16, I'm noticing that with the position bias fix, K_eff becomes negative in MMLU and ARC conditions, so the statement "positive and FDR-significant in all 12/12 conditions" is now incorrect—it should reflect that K_eff is significant but not consistently positive across all conditions.

For line 18, the bootstrap counts need updating from (η_max 3/12, K_eff 4/12) to (η_max 5/12, K_eff 8/12), and I should also check the wild bootstrap row in the method comparison table.

Then I need to systematically go through the results section—updating the table caption and line 38 where it claims positive direction across all 12 conditions to reflect just 10/12, adjusting the bootstrap and fractional logit counts in line 43, and revising the GAM section around lines 55-56 and line 84 with the corrected numbers.

In the conclusion, I'll update the η_max trajectory references from 12/12 to 10/12 in two places, and in the analysis section I need to revise the K_eff trajectory narrative to match these corrections. I should also add a paragraph about position bias after the GAM taxonomy section.

Now I'm looking at the appendix—there are quite a few updates needed across multiple tables and sections, including the meta-analytic table, trajectory descriptions, per-condition WCB summaries, bootstrap convergence, crossed random effects, BFT reversal, GAM bootstrap, κ-diversity comparison, near-chance performance, and fractional logit tables. Let me start working through these systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "bae38b0a-9d1f-41a3-baf5-78e13ba5320b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiSU7faKTuR9oDeABgYm6V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 84662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9161
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

_source line 113_

Now I'll make all the edits systematically. Starting with the simpler files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "519c7cb4-9b42-4443-b2b3-5bf39f5e55bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiSU7faKTuR9oDeABgYm6V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 84662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9161
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

_source line 114_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VoTqTHQnfCpmMCxfeFFZDm`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "df044d85-30b0-4767-85d4-830d890dafad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiSU7faKTuR9oDeABgYm6V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9161,
      "cache_read_input_tokens": 84662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9161
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

_source line 115 · 2026-05-25T21:13:04.256Z_

<details><summary>↩ Tool result · `toolu_01VoTqTHQnfCpmMCxfeFFZDm`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "3259710a-5c9d-4c78-b808-d20c2d6e1292",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Tool call

_source line 116_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Q3oSxMz2TZna4d7R4Aqphp`</summary>

```json
{
  "todos": [
    {
      "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
      "status": "in_progress",
      "activeForm": "Updating abstract.tex"
    },
    {
      "content": "Update main.tex (abstract copy + Limitations)",
      "status": "pending",
      "activeForm": "Updating main.tex"
    },
    {
      "content": "Update introduction.tex (figure caption + contributions)",
      "status": "pending",
      "activeForm": "Updating introduction.tex"
    },
    {
      "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
      "status": "pending",
      "activeForm": "Updating results.tex"
    },
    {
      "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
      "status": "pending",
      "activeForm": "Updating conclusion.tex"
    },
    {
      "content": "Update analysis.tex (K_eff trajectory + direction counts)",
      "status": "pending",
      "activeForm": "Updating analysis.tex"
    },
    {
      "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
      "status": "pending",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Full-text grep verification for residual old numbers",
      "status": "pending",
      "activeForm": "Running verification greps"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "a7d3b8cd-728b-4915-8bc3-406a4df6edfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014q2HbwRe75M8br9QNVTQfc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3607,
      "cache_read_input_tokens": 93823,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3607
      },
      "output_tokens": 40,
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

_source line 117 · 2026-05-25T21:13:12.420Z_

<details><summary>↩ Tool result · `toolu_01Q3oSxMz2TZna4d7R4Aqphp`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "c97f4395-315e-4369-9217-c09a0232e931",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "in_progress",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "pending",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "pending",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "pending",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "pending",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "pending",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 118_

<details open><summary>🔧 Tool call — Edit · `toolu_01Serb9t73mduYTn2ueq58mj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex",
  "old_string": "(1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$",
  "new_string": "(1)~diversity is positively associated with vulnerability ($K_{\\mathrm{eff}}$ positive in 10/12 conditions, $\\kappa$-diversity 12/12), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "a3e40750-d7ae-401b-ad23-f96bb8c27cb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bC6oZwES1RmPAYERFvCWj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 405,
      "cache_read_input_tokens": 97430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 405
      },
      "output_tokens": 37,
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

_source line 119 · 2026-05-25T21:13:24.192Z_

<details><summary>↩ Tool result · `toolu_01Serb9t73mduYTn2ueq58mj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "f97abc2d-82fc-4cea-9aa8-891cc7a5a661",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/abstract.tex",
    "oldString": "(1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$",
    "newString": "(1)~diversity is positively associated with vulnerability ($K_{\\mathrm{eff}}$ positive in 10/12 conditions, $\\kappa$-diversity 12/12), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$",
    "originalFile": "% Mirror of abstract in main.tex — do not edit here.\n\nMulti-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " % Mirror of abstract in main.tex — do not edit here.",
          " ",
          "-Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational.",
          "+Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is positively associated with vulnerability ($K_{\\mathrm{eff}}$ positive in 10/12 conditions, $\\kappa$-diversity 12/12), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational."
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

_source line 120_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01K2RhdAGPpxRHXpNfHGHwCV`</summary>

```json
{
  "todos": [
    {
      "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
      "status": "completed",
      "activeForm": "Updating abstract.tex"
    },
    {
      "content": "Update main.tex (abstract copy + Limitations)",
      "status": "in_progress",
      "activeForm": "Updating main.tex"
    },
    {
      "content": "Update introduction.tex (figure caption + contributions)",
      "status": "pending",
      "activeForm": "Updating introduction.tex"
    },
    {
      "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
      "status": "pending",
      "activeForm": "Updating results.tex"
    },
    {
      "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
      "status": "pending",
      "activeForm": "Updating conclusion.tex"
    },
    {
      "content": "Update analysis.tex (K_eff trajectory + direction counts)",
      "status": "pending",
      "activeForm": "Updating analysis.tex"
    },
    {
      "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
      "status": "pending",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Full-text grep verification for residual old numbers",
      "status": "pending",
      "activeForm": "Running verification greps"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "5aa38dcc-3921-40f1-83f3-b0cf8111e091",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nwb1NLHv6fEMXywbPVYZrn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 97835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 425
      },
      "output_tokens": 59,
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

_source line 121 · 2026-05-25T21:13:29.922Z_

<details><summary>↩ Tool result · `toolu_01K2RhdAGPpxRHXpNfHGHwCV`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1826f62f-6dfa-4196-a6d2-ea1ecb9d21d1",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "in_progress",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "pending",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "pending",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "pending",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "pending",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "pending",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "newTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "in_progress",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "pending",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "pending",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "pending",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "pending",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 122_

Now main.tex — abstract copy and Limitations section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "a6cb3a7d-a47a-45b0-b7ef-c3376affbbf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYW6c2bu65ntqdFZLqR5kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 98260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 123_

<details open><summary>🔧 Tool call — Edit · `toolu_011v2KX6DYRRyEL1KZvPq85J`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
  "old_string": "(1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$",
  "new_string": "(1)~diversity is positively associated with vulnerability ($K_{\\mathrm{eff}}$ positive in 10/12 conditions, $\\kappa$-diversity 12/12), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "5333b9a8-02e1-44ef-a773-809c2f67063a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYW6c2bu65ntqdFZLqR5kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 98260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 124 · 2026-05-25T21:13:37.423Z_

<details><summary>↩ Tool result · `toolu_011v2KX6DYRRyEL1KZvPq85J`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "f08752fa-484d-4ff9-be6a-8238843354f6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
    "oldString": "(1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$",
    "newString": "(1)~diversity is positively associated with vulnerability ($K_{\\mathrm{eff}}$ positive in 10/12 conditions, $\\kappa$-diversity 12/12), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$",
    "originalFile": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tcolorbox}\n\\tcbuselibrary{breakable}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{definition}{Definition}\n\\newtheorem{proposition}{Proposition}\n\n\\title{The Diminishing Weakest Link: How Panel Size Shifts\\\\Adversarial Vulnerability Drivers in LLM Judge Panels}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{threat_model}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{conclusion}\n\n\\section*{Limitations}\n\n\\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.\n\\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\\geq}20$ threshold at all panel sizes \\citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\\mathrm{eff}}$ vs.\\ $\\kappa$-diversity show opposite $K$-trends).\n\\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \\in \\{3,5,7\\}$; the predictor shift threshold $K^*$ is not precisely identified.\n\\textbf{Aggregation scope.} We examine only majority vote, threshold, and Bayesian calibration as aggregation rules; more sophisticated strategies (e.g., weighted voting, learned aggregation, or iterative deliberation among judges) may alter the diversity--robustness relationship and are not explored here.\n\\textbf{Temporal snapshot.} All API model evaluations were collected during a fixed time window; providers may update model weights or safety filters without notice, potentially altering individual susceptibility profiles and panel-level robustness patterns.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_attacks}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 27,
        "oldLines": 7,
        "newStart": 27,
        "newLines": 7,
        "lines": [
          " \\maketitle",
          " ",
          " \\begin{abstract}",
          "-Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is uniformly positively associated with vulnerability (both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction in 12/12 conditions), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.",
          "+Multi-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is positively associated with vulnerability ($K_{\\mathrm{eff}}$ positive in 10/12 conditions, $\\kappa$-diversity 12/12), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.",
          " \\end{abstract}",
          " ",
          " \\input{introduction}"
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

_source line 125_

<details open><summary>🔧 Tool call — Edit · `toolu_018LvvaeAr4Srj81B12pUHtf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
  "old_string": "$K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions.",
  "new_string": "$K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 8/12, fractional logit 10/12), though direction is positive in 10 of 12 conditions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "e7c9e481-60a8-4fe0-ac39-df5177b11e2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYW6c2bu65ntqdFZLqR5kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 98260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 126 · 2026-05-25T21:13:40.199Z_

<details><summary>↩ Tool result · `toolu_018LvvaeAr4Srj81B12pUHtf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "7f368ce4-9228-4d9f-af55-2d73f53c2233",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
    "oldString": "$K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions.",
    "newString": "$K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 8/12, fractional logit 10/12), though direction is positive in 10 of 12 conditions.",
    "originalFile": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tcolorbox}\n\\tcbuselibrary{breakable}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{definition}{Definition}\n\\newtheorem{proposition}{Proposition}\n\n\\title{The Diminishing Weakest Link: How Panel Size Shifts\\\\Adversarial Vulnerability Drivers in LLM Judge Panels}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge panels are widely used to defend Large Language Model (LLM) evaluation against manipulation, yet no existing work disentangles whether robustness gains stem from individual judge quality or inter-judge diversity. We decompose panel attack success rate into weakest-link susceptibility ($\\eta_{\\max}$) and effective independence ($K_{\\mathrm{eff}}$) across 15 models, six attack types, two multiple-choice benchmarks, and panel sizes $K \\in \\{3, 5, 7\\}$ (up to 6,435 panels). Two findings are robust across diversity metrics and inference methods: (1)~diversity is positively associated with vulnerability ($K_{\\mathrm{eff}}$ positive in 10/12 conditions, $\\kappa$-diversity 12/12), and (2)~$\\eta_{\\max}$'s predictive power diminishes monotonically with panel size (meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; confidence interval crosses zero at $K{\\geq}5$). Monte Carlo calibration confirms the wild cluster bootstrap is conservative (max null rejection $1.6\\%$ at $\\alpha{=}5\\%$). Aggregation rules modulate predictability ($R^2$: threshold 0.83, Bayesian 0.09). The diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal claims; all findings are associational\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/cert_manip_resist_eval-588E/}.}.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{threat_model}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{conclusion}\n\n\\section*{Limitations}\n\n\\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.\n\\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\\geq}20$ threshold at all panel sizes \\citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\\mathrm{eff}}$ vs.\\ $\\kappa$-diversity show opposite $K$-trends).\n\\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \\in \\{3,5,7\\}$; the predictor shift threshold $K^*$ is not precisely identified.\n\\textbf{Aggregation scope.} We examine only majority vote, threshold, and Bayesian calibration as aggregation rules; more sophisticated strategies (e.g., weighted voting, learned aggregation, or iterative deliberation among judges) may alter the diversity--robustness relationship and are not explored here.\n\\textbf{Temporal snapshot.} All API model evaluations were collected during a fixed time window; providers may update model weights or safety filters without notice, potentially altering individual susceptibility profiles and panel-level robustness patterns.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_attacks}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " \\section*{Limitations}",
          " ",
          " \\textbf{Diversity--capability confound.} The structural coupling between diversity and capability ($r{=}0.70$--$0.81$; VIF $\\approx 2.0$--$2.9$) prevents observational regression from reliably separating their contributions; capability-matched subsampling reduces but does not eliminate this confound (Pool~A $r{=}0.50$). Causal identification requires training-based diversity control.",
          "-\\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 4/12, fractional logit 9/12), though direction is positive in all 12 conditions. Cluster counts fall below the ${\\geq}20$ threshold at all panel sizes \\citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\\mathrm{eff}}$ vs.\\ $\\kappa$-diversity show opposite $K$-trends).",
          "+\\textbf{Inference and measurement sensitivity.} At $K{=}3$, $K_{\\mathrm{eff}}$'s significance is method-sensitive (OLS 12/12, bootstrap 8/12, fractional logit 10/12), though direction is positive in 10 of 12 conditions. Cluster counts fall below the ${\\geq}20$ threshold at all panel sizes \\citep{cameron2008bootstrap}; the diversity significance trajectory is also operationalization-dependent ($K_{\\mathrm{eff}}$ vs.\\ $\\kappa$-diversity show opposite $K$-trends).",
          " \\textbf{Benchmark and attack scope.} Both benchmarks use multiple-choice formats; open-ended generation may present different attack surfaces. The six local models use AWQ INT4 quantization, which may confound capability classification, though excluding near-chance quantized models strengthens the association (Appendix~\\ref{app:near_chance}). Each attack uses 1--2 template variants, limiting generalization. We study only odd $K \\in \\{3,5,7\\}$; the predictor shift threshold $K^*$ is not precisely identified.",
          " \\textbf{Aggregation scope.} We examine only majority vote, threshold, and Bayesian calibration as aggregation rules; more sophisticated strategies (e.g., weighted voting, learned aggregation, or iterative deliberation among judges) may alter the diversity--robustness relationship and are not explored here.",
          " \\textbf{Temporal snapshot.} All API model evaluations were collected during a fixed time window; providers may update model weights or safety filters without notice, potentially altering individual susceptibility profiles and panel-level robustness patterns."
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

_source line 127_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Fg6UXupzeUwKSHLgYsPXWx`</summary>

```json
{
  "todos": [
    {
      "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
      "status": "completed",
      "activeForm": "Updating abstract.tex"
    },
    {
      "content": "Update main.tex (abstract copy + Limitations)",
      "status": "completed",
      "activeForm": "Updating main.tex"
    },
    {
      "content": "Update introduction.tex (figure caption + contributions)",
      "status": "in_progress",
      "activeForm": "Updating introduction.tex"
    },
    {
      "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
      "status": "pending",
      "activeForm": "Updating results.tex"
    },
    {
      "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
      "status": "pending",
      "activeForm": "Updating conclusion.tex"
    },
    {
      "content": "Update analysis.tex (K_eff trajectory + direction counts)",
      "status": "pending",
      "activeForm": "Updating analysis.tex"
    },
    {
      "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
      "status": "pending",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Full-text grep verification for residual old numbers",
      "status": "pending",
      "activeForm": "Running verification greps"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "627e8a3f-620d-4158-aaa0-aa51c4fd33b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zLMmcdRDFZ97i4K2wV91C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 98662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 764
      },
      "output_tokens": 40,
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

_source line 128 · 2026-05-25T21:13:46.342Z_

<details><summary>↩ Tool result · `toolu_01Fg6UXupzeUwKSHLgYsPXWx`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "b323b98a-874e-4fcb-826c-f421990e387d",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "in_progress",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "pending",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "pending",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "pending",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "pending",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "newTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "completed",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "in_progress",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "pending",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "pending",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "pending",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 129_

Now introduction.tex — figure caption + contributions section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "81074686-1ed1-4cb0-a09f-4942da8a4926",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LepSNLA1K9D2KFgrXtm6t2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 99426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 130_

<details open><summary>🔧 Tool call — Edit · `toolu_01WgJDTho5jhRMLh1BPW1sCq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
  "old_string": "\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.264$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.437$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}",
  "new_string": "\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.243$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.353$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "5cc3751b-0a59-49a7-8eed-488432d96404",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LepSNLA1K9D2KFgrXtm6t2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 99426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 131 · 2026-05-25T21:13:57.669Z_

<details><summary>↩ Tool result · `toolu_01WgJDTho5jhRMLh1BPW1sCq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "80d47721-bc25-4b0d-84b8-2a4ec0f748e9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
    "oldString": "\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.264$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.437$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}",
    "newString": "\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.243$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.353$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}",
    "originalFile": "\\section{Introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.78\\textwidth]{figures/fig_framework.pdf}\n\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.264$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.437$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}\n\\label{fig:framework}\n\\end{figure*}\n\nMulti-judge panels have become the dominant defense against bias and manipulation in Large Language Model (LLM) evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, an approach inspired by Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization reports that 7-model committees reduce attack success rates (ASR) from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation, yet this framing conflates two distinct sources of robustness: the quality of individual judges and the independence among them.\n\nThe conflation matters because the BFT analogy breaks down in the LLM judge setting. BFT adversaries control faulty nodes from within; evaluation adversaries manipulate inputs from without, and shared pretraining corpora create correlated failure modes that violate the independence assumption underlying majority-vote guarantees \\citep{schneier2000secrets}. No existing work disentangles diversity from individual robustness across panel sizes, so the relative contribution of each factor to observed ASR reductions remains unclear.\n\nWe address this gap by decomposing panel vulnerability into two predictors (Figure~\\ref{fig:framework}): weakest-link susceptibility ($\\eta_{\\max}$, the maximum individual attack success rate in a panel) and effective independent channels ($K_{\\mathrm{eff}}$, an information-theoretic measure of judge independence). Controlled experiments across 15 models (9 API, 6 local quantized), $K \\in \\{3,5,7\\}$, six attack types, and two multiple-choice benchmarks (Massive Multitask Language Understanding [MMLU] and the AI2 Reasoning Challenge [ARC]) reveal two robust patterns and one metric-sensitive observation.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity \\citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).\n\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).\n\\item \\textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12), so the defense is partial (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nAll findings are associational; the diversity--capability confound ($r{=}0.70$--$0.81$; \\S\\ref{sec:analysis}) precludes causal claims.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " \\begin{figure*}[t]",
          " \\centering",
          " \\includegraphics[width=0.78\\textwidth]{figures/fig_framework.pdf}",
          "-\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.264$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.437$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}",
          "+\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.243$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.353$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}",
          " \\label{fig:framework}",
          " \\end{figure*}",
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

_source line 132_

<details open><summary>🔧 Tool call — Edit · `toolu_018PQW8nFwPmG72gvAqahD8d`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
  "old_string": "\\item \\textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity \\citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).",
  "new_string": "\\item \\textbf{Diversity positively associated with vulnerability.} $K_{\\mathrm{eff}}$ confirms a positive association with panel attack success in 10 of 12 conditions (10/12 direction under OLS and generalized additive model bootstrap); $\\kappa$-diversity confirms 12/12. The two exceptions---both position-bias conditions---show negative $K_{\\mathrm{eff}}$, consistent with diversity providing genuine redundancy against shared-bias attacks (\\S\\ref{sec:gam_taxonomy}). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "bd270c9d-940c-49a7-a2e2-a761a1185a5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LepSNLA1K9D2KFgrXtm6t2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 99426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 133 · 2026-05-25T21:14:05.250Z_

<details><summary>↩ Tool result · `toolu_018PQW8nFwPmG72gvAqahD8d`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "942f5db9-be5f-45a3-b62c-20fc11360742",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
    "oldString": "\\item \\textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity \\citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).",
    "newString": "\\item \\textbf{Diversity positively associated with vulnerability.} $K_{\\mathrm{eff}}$ confirms a positive association with panel attack success in 10 of 12 conditions (10/12 direction under OLS and generalized additive model bootstrap); $\\kappa$-diversity confirms 12/12. The two exceptions---both position-bias conditions---show negative $K_{\\mathrm{eff}}$, consistent with diversity providing genuine redundancy against shared-bias attacks (\\S\\ref{sec:gam_taxonomy}). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).",
    "originalFile": "\\section{Introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.78\\textwidth]{figures/fig_framework.pdf}\n\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.243$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.353$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}\n\\label{fig:framework}\n\\end{figure*}\n\nMulti-judge panels have become the dominant defense against bias and manipulation in Large Language Model (LLM) evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, an approach inspired by Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization reports that 7-model committees reduce attack success rates (ASR) from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation, yet this framing conflates two distinct sources of robustness: the quality of individual judges and the independence among them.\n\nThe conflation matters because the BFT analogy breaks down in the LLM judge setting. BFT adversaries control faulty nodes from within; evaluation adversaries manipulate inputs from without, and shared pretraining corpora create correlated failure modes that violate the independence assumption underlying majority-vote guarantees \\citep{schneier2000secrets}. No existing work disentangles diversity from individual robustness across panel sizes, so the relative contribution of each factor to observed ASR reductions remains unclear.\n\nWe address this gap by decomposing panel vulnerability into two predictors (Figure~\\ref{fig:framework}): weakest-link susceptibility ($\\eta_{\\max}$, the maximum individual attack success rate in a panel) and effective independent channels ($K_{\\mathrm{eff}}$, an information-theoretic measure of judge independence). Controlled experiments across 15 models (9 API, 6 local quantized), $K \\in \\{3,5,7\\}$, six attack types, and two multiple-choice benchmarks (Massive Multitask Language Understanding [MMLU] and the AI2 Reasoning Challenge [ARC]) reveal two robust patterns and one metric-sensitive observation.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity \\citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).\n\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).\n\\item \\textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12), so the defense is partial (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nAll findings are associational; the diversity--capability confound ($r{=}0.70$--$0.81$; \\S\\ref{sec:analysis}) precludes causal claims.\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 7,
        "lines": [
          " ",
          " These findings yield three contributions:",
          " \\begin{enumerate}",
          "-\\item \\textbf{Diversity uniformly positively associated with vulnerability.} Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity \\citep{kuncheva2003measures} confirm a positive association with panel attack success in all 12 conditions (12/12 direction under OLS and generalized additive model bootstrap). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).",
          "+\\item \\textbf{Diversity positively associated with vulnerability.} $K_{\\mathrm{eff}}$ confirms a positive association with panel attack success in 10 of 12 conditions (10/12 direction under OLS and generalized additive model bootstrap); $\\kappa$-diversity confirms 12/12. The two exceptions---both position-bias conditions---show negative $K_{\\mathrm{eff}}$, consistent with diversity providing genuine redundancy against shared-bias attacks (\\S\\ref{sec:gam_taxonomy}). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).",
          " \\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).",
          " \\item \\textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12), so the defense is partial (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).",
          " \\end{enumerate}"
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

_source line 134_

<details open><summary>🔧 Tool call — Edit · `toolu_01SEvyCLKGcJT3EbsVzdY1yy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
  "old_string": "\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).",
  "new_string": "\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.243$ [$0.163, 0.323$] at $K{=}3$ to $0.091$ [$-0.031, 0.212$] at $K{=}5$ to $0.086$ [$-0.039, 0.211$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$ remains a consistently strong predictor (WCB significance 7--8/12 across all $K$), while $\\eta_{\\max}$ WCB significance drops from 5/12 ($K{=}3$) to 0/12 ($K{=}5$) to 1/12 ($K{=}7$). $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "29e31075-a2bc-4e5d-a375-b81534c4114b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LepSNLA1K9D2KFgrXtm6t2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 99426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 135 · 2026-05-25T21:14:13.821Z_

<details><summary>↩ Tool result · `toolu_01SEvyCLKGcJT3EbsVzdY1yy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "a99f56ed-af9f-4c9d-8598-9d258cb43a54",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/introduction.tex",
    "oldString": "\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).",
    "newString": "\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.243$ [$0.163, 0.323$] at $K{=}3$ to $0.091$ [$-0.031, 0.212$] at $K{=}5$ to $0.086$ [$-0.039, 0.211$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$ remains a consistently strong predictor (WCB significance 7--8/12 across all $K$), while $\\eta_{\\max}$ WCB significance drops from 5/12 ($K{=}3$) to 0/12 ($K{=}5$) to 1/12 ($K{=}7$). $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).",
    "originalFile": "\\section{Introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.78\\textwidth]{figures/fig_framework.pdf}\n\\caption{The diminishing weakest link in LLM judge panels. \\textbf{(a)}~In small panels ($K{=}3$), a single vulnerable judge (red) can flip the majority; individual weakness ($\\eta_{\\max}$) dominates vulnerability ($\\hat{\\beta}_{\\mathrm{std}}{=}0.243$). \\textbf{(b)}~As panel size grows, the balance shifts from individual weakness to collective diversity. \\textbf{(c)}~In large panels ($K{\\geq}5$), inter-judge diversity ($K_{\\mathrm{eff}}$, $\\hat{\\beta}_{\\mathrm{std}}{=}0.353$) drives vulnerability while $\\eta_{\\max}$ diminishes (CI crosses zero). Bottom bars show relative predictive weight.}\n\\label{fig:framework}\n\\end{figure*}\n\nMulti-judge panels have become the dominant defense against bias and manipulation in Large Language Model (LLM) evaluation. After \\citet{zheng2023judging} demonstrated that individual LLM judges can rival human annotators, subsequent work exposed systematic vulnerabilities: position bias, verbosity preferences, and sycophancy compromise the reliability of any single judge \\citep{wang2023fair}. The natural response has been to aggregate decisions across diverse models, an approach inspired by Byzantine fault tolerance (BFT), where majority voting among independent nodes tolerates faulty responses \\citep{lamport1982byzantine,castro1999practical}. A recent systematization reports that 7-model committees reduce attack success rates (ASR) from 50--68\\% to 10--19\\% \\citep{almasoud2026security}. Diversity, by this logic, is the key ingredient for secure evaluation, yet this framing conflates two distinct sources of robustness: the quality of individual judges and the independence among them.\n\nThe conflation matters because the BFT analogy breaks down in the LLM judge setting. BFT adversaries control faulty nodes from within; evaluation adversaries manipulate inputs from without, and shared pretraining corpora create correlated failure modes that violate the independence assumption underlying majority-vote guarantees \\citep{schneier2000secrets}. No existing work disentangles diversity from individual robustness across panel sizes, so the relative contribution of each factor to observed ASR reductions remains unclear.\n\nWe address this gap by decomposing panel vulnerability into two predictors (Figure~\\ref{fig:framework}): weakest-link susceptibility ($\\eta_{\\max}$, the maximum individual attack success rate in a panel) and effective independent channels ($K_{\\mathrm{eff}}$, an information-theoretic measure of judge independence). Controlled experiments across 15 models (9 API, 6 local quantized), $K \\in \\{3,5,7\\}$, six attack types, and two multiple-choice benchmarks (Massive Multitask Language Understanding [MMLU] and the AI2 Reasoning Challenge [ARC]) reveal two robust patterns and one metric-sensitive observation.\n\nThese findings yield three contributions:\n\\begin{enumerate}\n\\item \\textbf{Diversity positively associated with vulnerability.} $K_{\\mathrm{eff}}$ confirms a positive association with panel attack success in 10 of 12 conditions (10/12 direction under OLS and generalized additive model bootstrap); $\\kappa$-diversity confirms 12/12. The two exceptions---both position-bias conditions---show negative $K_{\\mathrm{eff}}$, consistent with diversity providing genuine redundancy against shared-bias attacks (\\S\\ref{sec:gam_taxonomy}). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).\n\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).\n\\item \\textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12), so the defense is partial (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nAll findings are associational; the diversity--capability confound ($r{=}0.70$--$0.81$; \\S\\ref{sec:analysis}) precludes causal claims.\n",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 16,
        "newLines": 7,
        "lines": [
          " These findings yield three contributions:",
          " \\begin{enumerate}",
          " \\item \\textbf{Diversity positively associated with vulnerability.} $K_{\\mathrm{eff}}$ confirms a positive association with panel attack success in 10 of 12 conditions (10/12 direction under OLS and generalized additive model bootstrap); $\\kappa$-diversity confirms 12/12. The two exceptions---both position-bias conditions---show negative $K_{\\mathrm{eff}}$, consistent with diversity providing genuine redundancy against shared-bias attacks (\\S\\ref{sec:gam_taxonomy}). However, the diversity--capability confound ($r{=}0.70$--$0.81$) precludes causal interpretation: Cinelli--Hazlett robustness values do not exceed the confound in 69\\% of conditions (\\S\\ref{sec:dominance}, \\S\\ref{sec:gam_taxonomy}).",
          "-\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.264$ [$0.158, 0.369$] at $K{=}3$ to $0.102$ [$-0.055, 0.259$] at $K{=}5$ to $0.084$ [$-0.083, 0.251$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. The diversity significance trajectory, however, depends on the metric: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).",
          "+\\item \\textbf{Diminishing weakest link.} $\\eta_{\\max}$'s predictive power declines monotonically with panel size: meta-analytic pooled $\\hat{\\beta}_{\\mathrm{std}}$ falls from $0.243$ [$0.163, 0.323$] at $K{=}3$ to $0.091$ [$-0.031, 0.212$] at $K{=}5$ to $0.086$ [$-0.039, 0.211$] at $K{=}7$; the confidence interval crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$ remains a consistently strong predictor (WCB significance 7--8/12 across all $K$), while $\\eta_{\\max}$ WCB significance drops from 5/12 ($K{=}3$) to 0/12 ($K{=}5$) to 1/12 ($K{=}7$). $\\kappa$-diversity decreases ($8 \\to 7 \\to 6$/12), indicating that the $K$-dependent pattern is operationalization-sensitive (\\S\\ref{sec:cross_k}).",
          " \\item \\textbf{Aggregation as predictability control.} Aggregation rules modulate how much variance panel composition explains ($R^2$: threshold 0.83, Bayesian 0.09). Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12), so the defense is partial (\\S\\ref{sec:aggregation}, \\S\\ref{sec:analysis}).",
          " \\end{enumerate}",
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

_source line 136_

Now conclusion.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "f6327a43-ad2f-48a6-8a52-1f1066ae9172",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHp2XLCipWjUU56rYJZqPD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 99828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1918
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

_source line 137_

<details open><summary>🔧 Tool call — Edit · `toolu_019PkquScVhFohvBpDQVZZKZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex",
  "old_string": "$\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; CI crosses zero at $K{\\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions)",
  "new_string": "$\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; CI crosses zero at $K{\\geq}5$), while diversity is positively associated with vulnerability (10/12 conditions)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1940c764-2414-44fc-adaf-33d875b22bed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHp2XLCipWjUU56rYJZqPD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 99828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1918
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

_source line 138 · 2026-05-25T21:14:20.155Z_

<details><summary>↩ Tool result · `toolu_019PkquScVhFohvBpDQVZZKZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "34abe48a-0bee-407a-a628-77351ddffd09",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex",
    "oldString": "$\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; CI crosses zero at $K{\\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions)",
    "newString": "$\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; CI crosses zero at $K{\\geq}5$), while diversity is positively associated with vulnerability (10/12 conditions)",
    "originalFile": "\\section{Conclusion}\n\nThe weakest link diminishes: $\\eta_{\\max}$'s predictive power declines monotonically (pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; CI crosses zero at $K{\\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\\geq}5$, $K_{\\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\\min \\eta_{\\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\section{Conclusion}",
          " ",
          "-The weakest link diminishes: $\\eta_{\\max}$'s predictive power declines monotonically (pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.264 \\to 0.102 \\to 0.084$; CI crosses zero at $K{\\geq}5$), while diversity is uniformly positively associated with vulnerability (12/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\\geq}5$, $K_{\\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\\min \\eta_{\\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.",
          "+The weakest link diminishes: $\\eta_{\\max}$'s predictive power declines monotonically (pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; CI crosses zero at $K{\\geq}5$), while diversity is positively associated with vulnerability (10/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\\geq}5$, $K_{\\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\\min \\eta_{\\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question."
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

_source line 139_

<details open><summary>🔧 Tool call — Edit · `toolu_01FenpS81Qy9JiRQJdptg4bH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex",
  "old_string": "all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)",
  "new_string": "all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients in 10/12 conditions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "e43f89d0-47c9-40ea-9207-968899f4d595",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHp2XLCipWjUU56rYJZqPD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1918,
      "cache_read_input_tokens": 99828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1918
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

_source line 140 · 2026-05-25T21:14:21.595Z_

<details><summary>↩ Tool result · `toolu_01FenpS81Qy9JiRQJdptg4bH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "31c6cd6a-a750-4870-9305-e7fc34d3697a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/conclusion.tex",
    "oldString": "all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)",
    "newString": "all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients in 10/12 conditions",
    "originalFile": "\\section{Conclusion}\n\nThe weakest link diminishes: $\\eta_{\\max}$'s predictive power declines monotonically (pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; CI crosses zero at $K{\\geq}5$), while diversity is positively associated with vulnerability (10/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\\geq}5$, $K_{\\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\\min \\eta_{\\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\section{Conclusion}",
          " ",
          "-The weakest link diminishes: $\\eta_{\\max}$'s predictive power declines monotonically (pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; CI crosses zero at $K{\\geq}5$), while diversity is positively associated with vulnerability (10/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\\geq}5$, $K_{\\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\\min \\eta_{\\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients (12/12)---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question.",
          "+The weakest link diminishes: $\\eta_{\\max}$'s predictive power declines monotonically (pooled $\\hat{\\beta}_{\\mathrm{std}}$: $0.243 \\to 0.091 \\to 0.086$; CI crosses zero at $K{\\geq}5$), while diversity is positively associated with vulnerability (10/12 conditions). Panel design is two-regime: individual robustness dominates at $K{=}3$; at $K{\\geq}5$, $K_{\\mathrm{eff}}$ becomes more predictive. Aggregation modulates these effects: Bayesian calibration nearly neutralizes panel composition influence ($R^2{\\leq}0.17$), suggesting that calibrated aggregation can partially compensate for suboptimal panel composition. The diversity--capability coupling ($r{=}0.70$--$0.81$) means naively maximizing diversity is counterproductive; robustness-first selection ($\\min \\eta_{\\max}$) dominates in all conditions. These conclusions are directionally robust---all five inference methods preserve positive $K_{\\mathrm{eff}}$ coefficients in 10/12 conditions---though significance counts vary (0/12 to 12/12), underscoring the need to correct for combinatorial non-independence in panel evaluation designs. Disentangling diversity from capability through controlled experimental designs remains the central open question."
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

_source line 141_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01VRziuuj68YGrTErf3wazpc`</summary>

```json
{
  "todos": [
    {
      "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
      "status": "completed",
      "activeForm": "Updating abstract.tex"
    },
    {
      "content": "Update main.tex (abstract copy + Limitations)",
      "status": "completed",
      "activeForm": "Updating main.tex"
    },
    {
      "content": "Update introduction.tex (figure caption + contributions)",
      "status": "completed",
      "activeForm": "Updating introduction.tex"
    },
    {
      "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
      "status": "in_progress",
      "activeForm": "Updating results.tex"
    },
    {
      "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
      "status": "completed",
      "activeForm": "Updating conclusion.tex"
    },
    {
      "content": "Update analysis.tex (K_eff trajectory + direction counts)",
      "status": "pending",
      "activeForm": "Updating analysis.tex"
    },
    {
      "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
      "status": "pending",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Full-text grep verification for residual old numbers",
      "status": "pending",
      "activeForm": "Running verification greps"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "32862692-8576-4786-b9eb-e5e03d8ab38d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bFr9rSwnwuCrV4n9TjmS7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 101746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 603
      },
      "output_tokens": 33,
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

_source line 142 · 2026-05-25T21:14:33.745Z_

<details><summary>↩ Tool result · `toolu_01VRziuuj68YGrTErf3wazpc`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "605614bd-3139-4e41-b723-ee9f0c471295",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "completed",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "in_progress",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "pending",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "pending",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "pending",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "newTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "completed",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "completed",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "in_progress",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "pending",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 143_

Now results.tex — the most complex file. Multiple edits needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "ff07f5d7-1c6c-4762-9b97-3bd8a2f378a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojoJYsYU1UPjuhTDa5dcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 102349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 144_

<details open><summary>🔧 Tool call — Edit · `toolu_012ZWSsptQuXGEFwkbmeFZgX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}",
  "new_string": "\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "679bae45-abae-49f6-bbf7-3750aa1447c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojoJYsYU1UPjuhTDa5dcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 102349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 145 · 2026-05-25T21:14:42.418Z_

<details><summary>↩ Tool result · `toolu_012ZWSsptQuXGEFwkbmeFZgX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "dddd0651-3748-4cee-b7bc-9fdabe4f9a85",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}",
    "newString": "\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 3/12  & 4/12  \\\\\nFrac.\\ logit (clust.)  & 7/12  & 9/12  \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}",
          "-\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) declines from 3/12 to 2/12, while $K_{\\mathrm{eff}}$ (blue) rises from 4/12 to 7/12. Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}",
          "+\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}",
          " \\label{fig:regime_transition}",
          " \\end{figure}",
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

_source line 146_

<details open><summary>🔧 Tool call — Edit · `toolu_01M2rCrTHaCL2P8y5qmW6BGd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "Under OLS, $K_{\\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions.",
  "new_string": "Under OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6aa03f62-f615-4036-a7ba-25dbf6c154d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojoJYsYU1UPjuhTDa5dcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 102349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 147 · 2026-05-25T21:14:44.835Z_

<details><summary>↩ Tool result · `toolu_01M2rCrTHaCL2P8y5qmW6BGd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6fb725b5-05ed-4fd5-a2ff-0883dbbc5524",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "Under OLS, $K_{\\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions.",
    "newString": "Under OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 3/12  & 4/12  \\\\\nFrac.\\ logit (clust.)  & 7/12  & 9/12  \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " ",
          " Table~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).",
          " ",
          "-Under OLS, $K_{\\mathrm{eff}}$ is positive and FDR-significant in all 12/12 conditions. $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).",
          "+Under OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).",
          " ",
          " Figure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).",
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

_source line 148_

<details open><summary>🔧 Tool call — Edit · `toolu_01QubXmSKkL17eot6e72c2tW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "Figure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12).",
  "new_string": "Figure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "875dabd0-b55a-4e46-b9dc-11137c036e61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojoJYsYU1UPjuhTDa5dcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 102349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 149 · 2026-05-25T21:14:47.975Z_

<details><summary>↩ Tool result · `toolu_01QubXmSKkL17eot6e72c2tW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "9d210ec8-f370-4d7c-8b56-4f22d68a0a4c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "Figure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12).",
    "newString": "Figure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 3/12  & 4/12  \\\\\nFrac.\\ logit (clust.)  & 7/12  & 9/12  \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 7,
        "lines": [
          " ",
          " Under OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).",
          " ",
          "-Figure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 3/12, $K_{\\mathrm{eff}}$ 4/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).",
          "+Figure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).",
          " ",
          " \\begin{table}[t]",
          " \\centering"
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

_source line 150_

<details open><summary>🔧 Tool call — Edit · `toolu_01GFfRAPPXRDcXaqBBe8eiar`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "Wild bootstrap         & 3/12  & 4/12  \\\\\nFrac.\\ logit (clust.)  & 7/12  & 9/12  \\\\",
  "new_string": "Wild bootstrap         & 5/12  & 8/12  \\\\\nFrac.\\ logit (clust.)  & 8/12  & 10/12 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6af98e52-2351-4222-92d5-712f21036e77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2QgGP6RMnpQecsiZULWVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 102751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1111
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

_source line 151 · 2026-05-25T21:14:52.791Z_

<details><summary>↩ Tool result · `toolu_01GFfRAPPXRDcXaqBBe8eiar`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "4abd85ad-b659-4051-97aa-65e203b5216d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "Wild bootstrap         & 3/12  & 4/12  \\\\\nFrac.\\ logit (clust.)  & 7/12  & 9/12  \\\\",
    "newString": "Wild bootstrap         & 5/12  & 8/12  \\\\\nFrac.\\ logit (clust.)  & 8/12  & 10/12 \\\\",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 3/12  & 4/12  \\\\\nFrac.\\ logit (clust.)  & 7/12  & 9/12  \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 27,
        "oldLines": 8,
        "newStart": 27,
        "newLines": 8,
        "lines": [
          " OLS                    & 10/12 & 12/12 \\\\",
          " Clustered SE           & 4/12  & 0/12  \\\\",
          " Mixed effects          & 7/12  & 3/12  \\\\",
          "-Wild bootstrap         & 3/12  & 4/12  \\\\",
          "-Frac.\\ logit (clust.)  & 7/12  & 9/12  \\\\",
          "+Wild bootstrap         & 5/12  & 8/12  \\\\",
          "+Frac.\\ logit (clust.)  & 8/12  & 10/12 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}"
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

_source line 152_

<details open><summary>🔧 Tool call — Edit · `toolu_01L4wNBEhhFjf5Qjk5uY8ceo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}",
  "new_string": "\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); positive direction is preserved in 10/12 conditions across all methods.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "ebbda15d-60cf-4686-9a1a-35c215f551b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2QgGP6RMnpQecsiZULWVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 102751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1111
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

_source line 153 · 2026-05-25T21:14:57.700Z_

<details><summary>↩ Tool result · `toolu_01L4wNBEhhFjf5Qjk5uY8ceo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "9be4cb94-23f3-4faa-a19a-bec64b90a739",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}",
    "newString": "\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); positive direction is preserved in 10/12 conditions across all methods.}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 5/12  & 8/12  \\\\\nFrac.\\ logit (clust.)  & 8/12  & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " Frac.\\ logit (clust.)  & 8/12  & 10/12 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); all methods preserve positive direction (12/12).}",
          "+\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); positive direction is preserved in 10/12 conditions across all methods.}",
          " \\label{tab:method_comparison}",
          " \\end{table}",
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

_source line 154_

<details open><summary>🔧 Tool call — Edit · `toolu_0159ae6tg5G1H9bVxMukUiMq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "Power analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.",
  "new_string": "Power analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (10/12) is preserved across all methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "485ad8be-79c0-42b6-aab6-fdcb4adb8c72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2QgGP6RMnpQecsiZULWVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 102751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1111
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

_source line 155 · 2026-05-25T21:15:00.029Z_

<details><summary>↩ Tool result · `toolu_0159ae6tg5G1H9bVxMukUiMq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "9dc2b6a4-f1a6-4d07-997d-d46d356229c9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "Power analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.",
    "newString": "Power analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (10/12) is preserved across all methods.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 5/12  & 8/12  \\\\\nFrac.\\ logit (clust.)  & 8/12  & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); positive direction is preserved in 10/12 conditions across all methods.}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 35,
        "oldLines": 7,
        "newStart": 35,
        "newLines": 7,
        "lines": [
          " \\label{tab:method_comparison}",
          " \\end{table}",
          " ",
          "-Power analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (12/12) is preserved across all methods.",
          "+Power analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (10/12) is preserved across all methods.",
          " ",
          " \\subsection{The Diminishing Weakest Link Across Panel Sizes}",
          " \\label{sec:cross_k}"
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

_source line 156_

<details open><summary>🔧 Tool call — Edit · `toolu_01VG5WuG6s6pLTErgJ4sZpZm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "The $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12).",
  "new_string": "The $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 8/12; fractional logit 11/12)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "2be8224a-83cc-4b18-95dd-a7d15d5ec411",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzHjAAQbkkz2Ee2EcP1HAh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 960,
      "cache_read_input_tokens": 103862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 960
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

_source line 157 · 2026-05-25T21:15:12.844Z_

<details><summary>↩ Tool result · `toolu_01VG5WuG6s6pLTErgJ4sZpZm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "9281c0c8-0980-4a5f-8202-d76d08b44c51",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "The $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12).",
    "newString": "The $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 8/12; fractional logit 11/12).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 5/12  & 8/12  \\\\\nFrac.\\ logit (clust.)  & 8/12  & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); positive direction is preserved in 10/12 conditions across all methods.}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (10/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 40,
        "oldLines": 7,
        "newStart": 40,
        "newLines": 7,
        "lines": [
          " \\subsection{The Diminishing Weakest Link Across Panel Sizes}",
          " \\label{sec:cross_k}",
          " ",
          "-The $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 7/12; fractional logit 9/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.",
          "+The $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 8/12; fractional logit 11/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.",
          " ",
          " Meta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.",
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

_source line 158_

<details open><summary>🔧 Tool call — Edit · `toolu_01TCoPrG719YctZu5qxw1zq1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "Meta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}).",
  "new_string": "Meta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.243$ [$0.163, 0.323$] at $K{=}3$, $0.091$ [$-0.031, 0.212$] at $K{=}5$, $0.086$ [$-0.039, 0.211$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.286$--$0.353$, CI excluding zero; Appendix~\\ref{app:meta_analytic_details})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "3993181c-2839-4a4b-a0ea-bed06d952a61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzHjAAQbkkz2Ee2EcP1HAh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 960,
      "cache_read_input_tokens": 103862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 960
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

_source line 159 · 2026-05-25T21:15:15.629Z_

<details><summary>↩ Tool result · `toolu_01TCoPrG719YctZu5qxw1zq1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "703d7f10-ecb1-4790-9e5a-3b35959fa211",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "Meta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}).",
    "newString": "Meta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.243$ [$0.163, 0.323$] at $K{=}3$, $0.091$ [$-0.031, 0.212$] at $K{=}5$, $0.086$ [$-0.039, 0.211$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.286$--$0.353$, CI excluding zero; Appendix~\\ref{app:meta_analytic_details}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 5/12  & 8/12  \\\\\nFrac.\\ logit (clust.)  & 8/12  & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); positive direction is preserved in 10/12 conditions across all methods.}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (10/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 8/12; fractional logit 11/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 42,
        "oldLines": 7,
        "newStart": 42,
        "newLines": 7,
        "lines": [
          " ",
          " The $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 8/12; fractional logit 11/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.",
          " ",
          "-Meta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.264$ [$0.158, 0.369$] at $K{=}3$, $0.102$ [$-0.055, 0.259$] at $K{=}5$, $0.084$ [$-0.083, 0.251$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.356$--$0.436$, CI excluding zero; $I^2{>}87\\%$; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.",
          "+Meta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.243$ [$0.163, 0.323$] at $K{=}3$, $0.091$ [$-0.031, 0.212$] at $K{=}5$, $0.086$ [$-0.039, 0.211$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.286$--$0.353$, CI excluding zero; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.",
          " ",
          " ",
          " \\subsection{Random vs.\\ Adaptive Fault Contrast}"
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

_source line 160_

Now update the GAM section and add the position bias paragraph, then update fractional logit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "9d58c3da-c331-4fbf-95d0-af62984e9941",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d9EjfN9dyGqZmvv6oyeCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 104822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 986
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

_source line 161_

<details open><summary>🔧 Tool call — Edit · `toolu_018dePyWs8Ni7YPmZcTS8w12`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "GAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}",
  "new_string": "GAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in 10 of 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\paragraph{Position Bias Exception.}\nPosition bias stands apart: $K_{\\mathrm{eff}}$'s coefficient is negative in both MMLU and ARC ($\\hat{\\beta}_{\\mathrm{std}} = -0.334, -0.372$), indicating that diverse panels are \\emph{less} susceptible to position bias. Position bias is a shared vulnerability---all judges exhibit the same directional preference---so independent judges provide genuine redundancy against this correlated failure mode, consistent with the Condorcet intuition. The two regimes (10 positive, 2 negative) thus align with the targeted-vs-shared attack taxonomy: targeted attacks exploit weak links (positive $K_{\\mathrm{eff}}$), while shared-bias attacks are diluted by diversity (negative $K_{\\mathrm{eff}}$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "51772309-147e-4d56-95bf-342fad35e2e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d9EjfN9dyGqZmvv6oyeCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 104822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 986
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

_source line 162 · 2026-05-25T21:15:31.758Z_

<details><summary>↩ Tool result · `toolu_018dePyWs8Ni7YPmZcTS8w12`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "9ae13a19-d79a-485d-9714-643f50fa9339",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "GAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}",
    "newString": "GAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in 10 of 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\paragraph{Position Bias Exception.}\nPosition bias stands apart: $K_{\\mathrm{eff}}$'s coefficient is negative in both MMLU and ARC ($\\hat{\\beta}_{\\mathrm{std}} = -0.334, -0.372$), indicating that diverse panels are \\emph{less} susceptible to position bias. Position bias is a shared vulnerability---all judges exhibit the same directional preference---so independent judges provide genuine redundancy against this correlated failure mode, consistent with the Condorcet intuition. The two regimes (10 positive, 2 negative) thus align with the targeted-vs-shared attack taxonomy: targeted attacks exploit weak links (positive $K_{\\mathrm{eff}}$), while shared-bias attacks are diluted by diversity (negative $K_{\\mathrm{eff}}$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 5/12  & 8/12  \\\\\nFrac.\\ logit (clust.)  & 8/12  & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); positive direction is preserved in 10/12 conditions across all methods.}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (10/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 8/12; fractional logit 11/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.243$ [$0.163, 0.323$] at $K{=}3$, $0.091$ [$-0.031, 0.212$] at $K{=}5$, $0.086$ [$-0.039, 0.211$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.286$--$0.353$, CI excluding zero; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 53,
        "oldLines": 8,
        "newStart": 53,
        "newLines": 11,
        "lines": [
          " \\subsection{Positive Direction Across Attack Types}",
          " \\label{sec:gam_taxonomy}",
          " ",
          "-GAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in all 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).",
          "+GAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in 10 of 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).",
          " ",
          "+\\paragraph{Position Bias Exception.}",
          "+Position bias stands apart: $K_{\\mathrm{eff}}$'s coefficient is negative in both MMLU and ARC ($\\hat{\\beta}_{\\mathrm{std}} = -0.334, -0.372$), indicating that diverse panels are \\emph{less} susceptible to position bias. Position bias is a shared vulnerability---all judges exhibit the same directional preference---so independent judges provide genuine redundancy against this correlated failure mode, consistent with the Condorcet intuition. The two regimes (10 positive, 2 negative) thus align with the targeted-vs-shared attack taxonomy: targeted attacks exploit weak links (positive $K_{\\mathrm{eff}}$), while shared-bias attacks are diluted by diversity (negative $K_{\\mathrm{eff}}$).",
          "+",
          " \\subsection{Aggregation Rules and the Diversity Channel}",
          " \\label{sec:aggregation}",
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

_source line 163_

<details open><summary>🔧 Tool call — Edit · `toolu_01KWGFv6KD7Z7fecaJvNQpns`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
  "old_string": "Fractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).",
  "new_string": "Fractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 10--11/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "6045d4ec-b0a6-44ea-a80b-69498f6c3466",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012d9EjfN9dyGqZmvv6oyeCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 104822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 986
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

_source line 164 · 2026-05-25T21:15:35.380Z_

<details><summary>↩ Tool result · `toolu_01KWGFv6KD7Z7fecaJvNQpns`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "bd733735-1a82-4ddf-b536-70716d06bbe5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/results.tex",
    "oldString": "Fractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).",
    "newString": "Fractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 10--11/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_regime_transition.pdf}\n\\caption{Predictor shift across panel sizes. $\\eta_{\\max}$ significance (orange) drops from 5/12 to 0--1/12, while $K_{\\mathrm{eff}}$ (blue) remains consistently high (7--8/12). Shaded region: $K^* \\in (3, 5)$. Bootstrap: $B{=}9999$, Rademacher, max-$p$, BH FDR $\\alpha{=}0.05$.}\n\\label{fig:regime_transition}\n\\end{figure}\n\n\\subsection{Weakest-Link Dominance at \\texorpdfstring{$K{=}3$}{K=3}}\n\\label{sec:dominance}\n\nTable~\\ref{tab:dominance} reports the log-log OLS regression (Equation~\\ref{eq:regression}) for all 12 conditions across the 455 panels ($K{=}3$, 15 judges from Table~\\ref{tab:models}).\n\nUnder OLS, $K_{\\mathrm{eff}}$ is FDR-significant in all 12/12 conditions (positive in 10, negative in 2 position-bias conditions). $\\eta_{\\max}$ is significant in 10/12 (exceptions: MMLU $\\times$ score manipulation and ARC $\\times$ position bias), consistent with Proposition~\\ref{thm:monotonicity}. Dominance analysis yields 10 co-dominant, 2 $K_{\\mathrm{eff}}$-dominant, and zero $\\eta_{\\max}$-dominant conditions. However, the $r = 0.70$ $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation raises confound concerns, and OLS ignores the non-independence of the 455 panels (Appendix~\\ref{app:keff_dist}).\n\nFigure~\\ref{fig:robustness} compares OLS against three corrections: both predictors attenuate under bootstrap ($\\eta_{\\max}$ 5/12, $K_{\\mathrm{eff}}$ 8/12), with clustered SE widest ($K_{\\mathrm{eff}}$ 0/12). Crossed random-effects analysis confirms $K_{\\mathrm{eff}}$ significance at $K{\\geq}5$ (Appendix~\\ref{app:crossed_re}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & $\\boldsymbol{\\eta_{\\max}}$ \\textbf{sig} & $\\boldsymbol{K_{\\mathrm{eff}}}$ \\textbf{sig} \\\\\n\\midrule\nOLS                    & 10/12 & 12/12 \\\\\nClustered SE           & 4/12  & 0/12  \\\\\nMixed effects          & 7/12  & 3/12  \\\\\nWild bootstrap         & 5/12  & 8/12  \\\\\nFrac.\\ logit (clust.)  & 8/12  & 10/12 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Inference method sensitivity at $K{=}3$ (455 panels, 12 conditions). $K_{\\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS); positive direction is preserved in 10/12 conditions across all methods.}\n\\label{tab:method_comparison}\n\\end{table}\n\nPower analysis yields MDE $\\beta_{\\mathrm{std}} = 0.14$ at 80\\% power (Appendix~\\ref{app:power_analysis}); positive coefficient direction (10/12) is preserved across all methods.\n\n\\subsection{The Diminishing Weakest Link Across Panel Sizes}\n\\label{sec:cross_k}\n\nThe $K{=}3$ pattern is method-sensitive (Table~\\ref{tab:method_comparison}), contrasting with $K{\\geq}5$ where $K_{\\mathrm{eff}}$'s dominance is consistent (bootstrap 8/12; fractional logit 11/12). We repeat the bootstrap at $K \\in \\{3, 5, 7\\}$ with max-$p$ correction.\n\nMeta-analytic pooling \\citep{dersimonian1986meta} quantifies trajectories independent of significance thresholds. $\\eta_{\\max}$'s pooled $\\hat{\\beta}_{\\mathrm{std}}$ declines monotonically: $0.243$ [$0.163, 0.323$] at $K{=}3$, $0.091$ [$-0.031, 0.212$] at $K{=}5$, $0.086$ [$-0.039, 0.211$] at $K{=}7$; CI crosses zero at $K{\\geq}5$. $K_{\\mathrm{eff}}$'s pooled coefficient remains positive ($0.286$--$0.353$, CI excluding zero; Appendix~\\ref{app:meta_analytic_details}). Figure~\\ref{fig:regime_transition} shows significance counts; per-condition effect sizes with 95\\% CIs are in Figure~\\ref{fig:forest_plot} (Appendix~\\ref{app:effect_size_forest}). The $\\eta_{\\max}$ decline holds under both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity.\n\n\n\\subsection{Random vs.\\ Adaptive Fault Contrast}\n\\label{sec:rf_contrast}\n\nRandom faults yield $R^2 = 0.730$ [$0.718, 0.745$]; adaptive attack reduces predictability ($R^2{=}0.285$ at $K{=}5$) but $K_{\\mathrm{eff}}$ retains power (7/12). The positive $K_{\\mathrm{eff}}$ coefficient under adaptive attack contrasts with the Condorcet Jury Theorem \\citep{condorcet1785essai}: under adversarial manipulation, independent judges present distinct attack surfaces rather than redundant defenses \\citep{goodfellow2015adversarial,kariyappa2019improving}.\n\n\\subsection{Positive Direction Across Attack Types}\n\\label{sec:gam_taxonomy}\n\nGAM bootstrap confirms positive $K_{\\mathrm{eff}}$ direction in 10 of 12 conditions (88.9--100\\% positive rate; Figure~\\ref{fig:gam_split}), with no magnitude difference between targeted and shared-bias attacks (Kruskal--Wallis $p{=}0.200$, $0.423$).\n\n\\paragraph{Position Bias Exception.}\nPosition bias stands apart: $K_{\\mathrm{eff}}$'s coefficient is negative in both MMLU and ARC ($\\hat{\\beta}_{\\mathrm{std}} = -0.334, -0.372$), indicating that diverse panels are \\emph{less} susceptible to position bias. Position bias is a shared vulnerability---all judges exhibit the same directional preference---so independent judges provide genuine redundancy against this correlated failure mode, consistent with the Condorcet intuition. The two regimes (10 positive, 2 negative) thus align with the targeted-vs-shared attack taxonomy: targeted attacks exploit weak links (positive $K_{\\mathrm{eff}}$), while shared-bias attacks are diluted by diversity (negative $K_{\\mathrm{eff}}$).\n\n\\subsection{Aggregation Rules and the Diversity Channel}\n\\label{sec:aggregation}\n\nTable~\\ref{tab:aggregation} reports regression results for four aggregation methods across all 12 conditions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{$\\eta_{\\max}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ sig} & \\textbf{$K_{\\mathrm{eff}}$ $\\beta$ dir.} & \\textbf{$R^2$} \\\\\n\\midrule\nThreshold       & 12/12 & 11/12 & 11+/0$-$  & 0.829 \\\\\nMajority        & 10/12 & 12/12 & 12+/0$-$  & 0.327 \\\\\nWeighted        & 9/12  & 12/12 & 12+/0$-$  & 0.328 \\\\\nBayesian        & 9/12  & 6/12  & 5+/1$-$   & 0.087 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregation method comparison ($K{=}3$, 15 models, 455 panels, OLS log-log). Significance counts are FDR-corrected across 12 conditions. $R^2$ is the mean across conditions. Table~\\ref{tab:dominance} uses per-condition FDR; this table uses pooled FDR across conditions.}\n\\label{tab:aggregation}\n\\end{table}\n\n\nPredictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).\n\n\\paragraph{Fractional Logit Robustness.}\nFractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).\n",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 4,
        "newStart": 84,
        "newLines": 4,
        "lines": [
          " Predictability ranges from threshold ($R^2{=}0.829$) to Bayesian ($R^2{=}0.087$), implying panel composition is almost unpredictive under calibrated aggregation. Bayesian calibration attenuates $K_{\\mathrm{eff}}$ (5+/1$-$) but $\\eta_{\\max}$ persists (9/12). At $K{=}5$ all methods converge (7/12; Appendix~\\ref{app:aggregation_k5}); at $K{=}7$ Bayesian neutralization returns (Appendix~\\ref{app:aggregation_k7}).",
          " ",
          " \\paragraph{Fractional Logit Robustness.}",
          "-Fractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks}).",
          "+Fractional logit \\citep{papke1996econometric} with clustered SE shows consistent positive association: $K_{\\mathrm{eff}}$ significance is 10--11/12 across all panel sizes ($K{=}3,5,7$), with 98.6\\% directional concordance with OLS (71/72; Appendix~\\ref{app:robustness_checks})."
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

_source line 165_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_014PYSnGHqTTvSGFxZVTGoLN`</summary>

```json
{
  "todos": [
    {
      "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
      "status": "completed",
      "activeForm": "Updating abstract.tex"
    },
    {
      "content": "Update main.tex (abstract copy + Limitations)",
      "status": "completed",
      "activeForm": "Updating main.tex"
    },
    {
      "content": "Update introduction.tex (figure caption + contributions)",
      "status": "completed",
      "activeForm": "Updating introduction.tex"
    },
    {
      "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
      "status": "completed",
      "activeForm": "Updating results.tex"
    },
    {
      "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
      "status": "completed",
      "activeForm": "Updating conclusion.tex"
    },
    {
      "content": "Update analysis.tex (K_eff trajectory + direction counts)",
      "status": "in_progress",
      "activeForm": "Updating analysis.tex"
    },
    {
      "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
      "status": "pending",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Full-text grep verification for residual old numbers",
      "status": "pending",
      "activeForm": "Running verification greps"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "11ba01bc-75b8-437c-9e97-e0f2e546f5e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShsYRJAeeBDQmGNWHhymbf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1316,
      "cache_read_input_tokens": 105808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1316
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

_source line 166 · 2026-05-25T21:15:41.836Z_

<details><summary>↩ Tool result · `toolu_014PYSnGHqTTvSGFxZVTGoLN`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "e18a3a4f-b8af-448d-9c12-cb4ee131c967",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "completed",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "completed",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "in_progress",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "pending",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "newTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "completed",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "completed",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "completed",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "in_progress",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 167_

Now analysis.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "59ac8a95-e02f-4acd-ba63-a7c01dc962c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiF2LdpGqHtZDbbXR1WWn1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 107124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 168_

<details open><summary>🔧 Tool call — Edit · `toolu_01WpdeC5G7qmS9R24ruz6SEz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex",
  "old_string": "though fractional logit confirms the positive association (9/12 at all $K$).",
  "new_string": "though fractional logit confirms the positive association (10--11/12 across all $K$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "453fab86-118a-4bd8-8a0b-307cad033027",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiF2LdpGqHtZDbbXR1WWn1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 107124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 169 · 2026-05-25T21:15:47.757Z_

<details><summary>↩ Tool result · `toolu_01WpdeC5G7qmS9R24ruz6SEz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "eb3494e4-5606-482e-95ac-a91ffb24e276",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex",
    "oldString": "though fractional logit confirms the positive association (9/12 at all $K$).",
    "newString": "though fractional logit confirms the positive association (10--11/12 across all $K$).",
    "originalFile": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Diversity--Capability Confound.}\n$K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\\approx}2.0$--$2.9$; Figure~\\ref{fig:keff_eta_scatter}, Appendix~\\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \\citep{cinelli2020making} shows the confound could account for the association in 69\\% of conditions (Appendix~\\ref{app:sensitivity}), though fractional logit confirms the positive association (9/12 at all $K$). Causal attribution requires capability-controlled designs (Appendices~\\ref{app:sensitivity_poolA},~\\ref{app:cross_benchmark}).\n\n\\paragraph{API-Only vs.\\ Full Pool.}\nRestricting to 9 API models removes the AWQ confound but increases collinearity ($r{=}0.85$): $\\eta_{\\max}$ retains significance (8/12) while $K_{\\mathrm{eff}}$ drops (2--3/12); the API-only pool lacks statistical power (MDE $> 0.9$; Appendices~\\ref{app:quant_dummy},~\\ref{app:random_subsample}).\n\n\\paragraph{Aggregation and Deployment.}\nAggregation rules influence predictability but not $K_{\\mathrm{eff}}$'s direction (Figure~\\ref{fig:aggregation_heatmap}). Threshold voting yields the highest $R^2$ ($0.83$ at $K{=}3$), while Bayesian calibration nearly neutralizes panel composition effects ($R^2{\\leq}0.17$ across all $K$). At $K{=}7$, Bayesian calibration fully neutralizes $K_{\\mathrm{eff}}$ (0/12; Appendix~\\ref{app:bayesian_entropy}). Robustness-first selection ($\\min \\eta_{\\max}$) achieves lowest ASR in all 12 conditions (Appendix~\\ref{app:panel_selection}), confirming that selecting judges by individual robustness dominates diversity-maximizing strategies regardless of panel size. Clean $K_{\\mathrm{eff}}$ is stable under 4/6 attacks ($\\rho{\\geq}0.91$; Appendix~\\ref{app:attacked_keff}), offering a deployable metric from clean-condition agreement alone.\n\n\\paragraph{Metric Sensitivity of the Diversity Trajectory.}\nThe diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\label{sec:analysis}",
          " ",
          " \\paragraph{Diversity--Capability Confound.}",
          "-$K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\\approx}2.0$--$2.9$; Figure~\\ref{fig:keff_eta_scatter}, Appendix~\\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \\citep{cinelli2020making} shows the confound could account for the association in 69\\% of conditions (Appendix~\\ref{app:sensitivity}), though fractional logit confirms the positive association (9/12 at all $K$). Causal attribution requires capability-controlled designs (Appendices~\\ref{app:sensitivity_poolA},~\\ref{app:cross_benchmark}).",
          "+$K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\\approx}2.0$--$2.9$; Figure~\\ref{fig:keff_eta_scatter}, Appendix~\\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \\citep{cinelli2020making} shows the confound could account for the association in 69\\% of conditions (Appendix~\\ref{app:sensitivity}), though fractional logit confirms the positive association (10--11/12 across all $K$). Causal attribution requires capability-controlled designs (Appendices~\\ref{app:sensitivity_poolA},~\\ref{app:cross_benchmark}).",
          " ",
          " \\paragraph{API-Only vs.\\ Full Pool.}",
          " Restricting to 9 API models removes the AWQ confound but increases collinearity ($r{=}0.85$): $\\eta_{\\max}$ retains significance (8/12) while $K_{\\mathrm{eff}}$ drops (2--3/12); the API-only pool lacks statistical power (MDE $> 0.9$; Appendices~\\ref{app:quant_dummy},~\\ref{app:random_subsample})."
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

_source line 170_

<details open><summary>🔧 Tool call — Edit · `toolu_01LK87SJCzwCCiwHrPAM6ron`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex",
  "old_string": "The diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.",
  "new_string": "The diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ remains consistently high ($8 \\to 8 \\to 7$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). $K_{\\mathrm{eff}}$ confirms positive direction in 10/12 conditions, $\\kappa$-diversity in 12/12; the $K$-dependent trajectory is metric-specific. The $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "1beabf47-63b2-412e-bd34-64cc96878782",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FiF2LdpGqHtZDbbXR1WWn1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 107124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 171 · 2026-05-25T21:15:55.574Z_

<details><summary>↩ Tool result · `toolu_01LK87SJCzwCCiwHrPAM6ron`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "7719c107-1bf1-495c-b524-e620d1e7a223",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/analysis.tex",
    "oldString": "The diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.",
    "newString": "The diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ remains consistently high ($8 \\to 8 \\to 7$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). $K_{\\mathrm{eff}}$ confirms positive direction in 10/12 conditions, $\\kappa$-diversity in 12/12; the $K$-dependent trajectory is metric-specific. The $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.",
    "originalFile": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Diversity--Capability Confound.}\n$K_{\\mathrm{eff}}$ and $\\eta_{\\max}$ correlate at $r{=}0.70$--$0.81$ (VIF${\\approx}2.0$--$2.9$; Figure~\\ref{fig:keff_eta_scatter}, Appendix~\\ref{app:extended_analysis}). Cinelli--Hazlett sensitivity analysis \\citep{cinelli2020making} shows the confound could account for the association in 69\\% of conditions (Appendix~\\ref{app:sensitivity}), though fractional logit confirms the positive association (10--11/12 across all $K$). Causal attribution requires capability-controlled designs (Appendices~\\ref{app:sensitivity_poolA},~\\ref{app:cross_benchmark}).\n\n\\paragraph{API-Only vs.\\ Full Pool.}\nRestricting to 9 API models removes the AWQ confound but increases collinearity ($r{=}0.85$): $\\eta_{\\max}$ retains significance (8/12) while $K_{\\mathrm{eff}}$ drops (2--3/12); the API-only pool lacks statistical power (MDE $> 0.9$; Appendices~\\ref{app:quant_dummy},~\\ref{app:random_subsample}).\n\n\\paragraph{Aggregation and Deployment.}\nAggregation rules influence predictability but not $K_{\\mathrm{eff}}$'s direction (Figure~\\ref{fig:aggregation_heatmap}). Threshold voting yields the highest $R^2$ ($0.83$ at $K{=}3$), while Bayesian calibration nearly neutralizes panel composition effects ($R^2{\\leq}0.17$ across all $K$). At $K{=}7$, Bayesian calibration fully neutralizes $K_{\\mathrm{eff}}$ (0/12; Appendix~\\ref{app:bayesian_entropy}). Robustness-first selection ($\\min \\eta_{\\max}$) achieves lowest ASR in all 12 conditions (Appendix~\\ref{app:panel_selection}), confirming that selecting judges by individual robustness dominates diversity-maximizing strategies regardless of panel size. Clean $K_{\\mathrm{eff}}$ is stable under 4/6 attacks ($\\rho{\\geq}0.91$; Appendix~\\ref{app:attacked_keff}), offering a deployable metric from clean-condition agreement alone.\n\n\\paragraph{Metric Sensitivity of the Diversity Trajectory.}\nThe diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 4,
        "newStart": 11,
        "newLines": 4,
        "lines": [
          " Aggregation rules influence predictability but not $K_{\\mathrm{eff}}$'s direction (Figure~\\ref{fig:aggregation_heatmap}). Threshold voting yields the highest $R^2$ ($0.83$ at $K{=}3$), while Bayesian calibration nearly neutralizes panel composition effects ($R^2{\\leq}0.17$ across all $K$). At $K{=}7$, Bayesian calibration fully neutralizes $K_{\\mathrm{eff}}$ (0/12; Appendix~\\ref{app:bayesian_entropy}). Robustness-first selection ($\\min \\eta_{\\max}$) achieves lowest ASR in all 12 conditions (Appendix~\\ref{app:panel_selection}), confirming that selecting judges by individual robustness dominates diversity-maximizing strategies regardless of panel size. Clean $K_{\\mathrm{eff}}$ is stable under 4/6 attacks ($\\rho{\\geq}0.91$; Appendix~\\ref{app:attacked_keff}), offering a deployable metric from clean-condition agreement alone.",
          " ",
          " \\paragraph{Metric Sensitivity of the Diversity Trajectory.}",
          "-The diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ significance increases ($4 \\to 7 \\to 8$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). Both $K_{\\mathrm{eff}}$ and $\\kappa$-diversity confirm positive direction (12/12), but the $K$-dependent trajectory is metric-specific; the $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations.",
          "+The diversity significance trajectory is operationalization-dependent: $K_{\\mathrm{eff}}$ remains consistently high ($8 \\to 8 \\to 7$/12) while $\\kappa$-diversity \\citep{kuncheva2003measures} decreases ($8 \\to 7 \\to 6$/12; Appendix~\\ref{app:kappa_regime}). Shannon MI entropy shows a third pattern ($4 \\to 4 \\to 0$; Appendix~\\ref{app:shannon_entropy}). $K_{\\mathrm{eff}}$ confirms positive direction in 10/12 conditions, $\\kappa$-diversity in 12/12; the $K$-dependent trajectory is metric-specific. The $\\eta_{\\max}$ decline holds under all specifications, making it the more robust finding across operationalizations."
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

_source line 172_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_017FasFoAUfJoUF1YY31CFk7`</summary>

```json
{
  "todos": [
    {
      "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
      "status": "completed",
      "activeForm": "Updating abstract.tex"
    },
    {
      "content": "Update main.tex (abstract copy + Limitations)",
      "status": "completed",
      "activeForm": "Updating main.tex"
    },
    {
      "content": "Update introduction.tex (figure caption + contributions)",
      "status": "completed",
      "activeForm": "Updating introduction.tex"
    },
    {
      "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
      "status": "completed",
      "activeForm": "Updating results.tex"
    },
    {
      "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
      "status": "completed",
      "activeForm": "Updating conclusion.tex"
    },
    {
      "content": "Update analysis.tex (K_eff trajectory + direction counts)",
      "status": "completed",
      "activeForm": "Updating analysis.tex"
    },
    {
      "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
      "status": "in_progress",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Full-text grep verification for residual old numbers",
      "status": "pending",
      "activeForm": "Running verification greps"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "290cd4d7-e51c-40b9-847c-0d0973f0768f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mjcT7tj3Z6LoMQePJqyEV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 107526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 861
      },
      "output_tokens": 40,
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

_source line 173 · 2026-05-25T21:16:03.096Z_

<details><summary>↩ Tool result · `toolu_017FasFoAUfJoUF1YY31CFk7`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "fc4889d6-dca5-4f2d-861d-583d0d85a912",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "completed",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "completed",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "completed",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "in_progress",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "newTodos": [
      {
        "content": "Update abstract.tex (pooled numbers + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating abstract.tex"
      },
      {
        "content": "Update main.tex (abstract copy + Limitations)",
        "status": "completed",
        "activeForm": "Updating main.tex"
      },
      {
        "content": "Update introduction.tex (figure caption + contributions)",
        "status": "completed",
        "activeForm": "Updating introduction.tex"
      },
      {
        "content": "Update results.tex (WCB counts, pooled numbers, tables, add position bias paragraph)",
        "status": "completed",
        "activeForm": "Updating results.tex"
      },
      {
        "content": "Update conclusion.tex (trajectory + 12/12→10/12)",
        "status": "completed",
        "activeForm": "Updating conclusion.tex"
      },
      {
        "content": "Update analysis.tex (K_eff trajectory + direction counts)",
        "status": "completed",
        "activeForm": "Updating analysis.tex"
      },
      {
        "content": "Update appendix.tex (meta-analytic table, per-condition summaries, WCB counts, narrative)",
        "status": "in_progress",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Full-text grep verification for residual old numbers",
        "status": "pending",
        "activeForm": "Running verification greps"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 174_

Now appendix.tex — the largest set of changes. Starting with the meta-analytic table and surrounding text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "90f5e8aa-a480-47f1-9b02-457a420a9068",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182G9deh8TZ1KdxkzDbuy6F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 108387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 175_

<details open><summary>🔧 Tool call — Edit · `toolu_017BUQ84M66ajU3jPR7A2W3r`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/appendix.tex",
  "old_string": "3 & 0.264 & [0.158, 0.369] & 91.3\\% & 0.356 & [0.267, 0.445] & 87.7\\% \\\\\n5 & 0.102 & [$-$0.055, 0.259] & 99.4\\% & 0.436 & [0.318, 0.553] & 98.9\\% \\\\\n7 & 0.084 & [$-$0.083, 0.251] & 99.8\\% & 0.401 & [0.298, 0.503] & 99.4\\% \\\\",
  "new_string": "3 & 0.243 & [0.163, 0.323] & TBD & 0.286 & [0.073, 0.499] & TBD \\\\\n5 & 0.091 & [$-$0.031, 0.212] & TBD & 0.353 & [0.125, 0.581] & TBD \\\\\n7 & 0.086 & [$-$0.039, 0.211] & TBD & 0.309 & [0.100, 0.517] & TBD \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a37508fa-334c-46ab-9bdc-7a8e3a3e687c",
  "uuid": "ef998612-6ac0-456e-8ef5-7ac599644407",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182G9deh8TZ1KdxkzDbuy6F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 108387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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
