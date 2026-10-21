# paper availability statement

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_paper_availability-statement_20260522T223217.log`
- **Structured JSON:** [`8feb5ddabb1976469359.json`](../../sessions/8f/8feb5ddabb1976469359.json)

## Before a recorded user message

12 recorded events

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
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
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
  "uuid": "231dbc67-0f04-4e32-b5be-09737543366b",
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
    "resetsAt": 1779502800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d33207b8-c698-4f98-904d-518739e5073c",
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22"
}
```

---

### Assistant

_source line 4_

Let me read the paper structure first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "uuid": "561d29df-9a40-4bb7-8706-99249a256af0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5fiT9rVejpCK7hk3LcRnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12272,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12272
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

<details open><summary>🔧 Tool call — Read · `toolu_01ArK4fzqJFyhta9x3rngpVa`</summary>

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
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "uuid": "4e087489-286a-4eaf-a483-dda5f04530e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5fiT9rVejpCK7hk3LcRnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12272,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12272
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

_source line 6 · 2026-05-22T22:32:29.482Z_

<details><summary>↩ Tool result · `toolu_01ArK4fzqJFyhta9x3rngpVa`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb,amsthm}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	
15	\newtheorem{theorem}{Theorem}
16	\newtheorem{definition}{Definition}
17	\newtheorem{proposition}{Proposition}
18	
19	\title{The Weakest Judge Wins: What Really Drives LLM Evaluation\\Panel Vulnerability Under Adversarial Attack}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, drawing on an implicit analogy to Byzantine fault tolerance. We conduct the first large-scale empirical decomposition of panel vulnerability into individual judge weakness ($\eta_{\max}$) and structural diversity ($K_{\mathrm{eff}}$) under adaptive adversarial attack. Across 15 models from 6 families, 455 panels, 6 attack types, and 2 benchmarks, $\eta_{\max}$ is significant in 5 to 8 of 12 conditions depending on non-independence correction method (OLS: 11/12; clustered SE: 8/12; wild cluster bootstrap: 5/12), while $K_{\mathrm{eff}}$'s significance collapses from 8/12 (OLS) to 0--1/12 after correction, yielding a 5:1 dominance ratio under bootstrap inference. Generalized additive model analysis reveals the structure masked by this collapse: diversity is directionally harmful for targeted attacks and protective for shared-bias attacks, a clean 6:6 split by attack mechanism. The choice of aggregation rule fundamentally modulates vulnerability: Bayesian calibration reverses $K_{\mathrm{eff}}$'s direction and weakens $\eta_{\max}$, while threshold voting amplifies both ($R^2{=}0.89$). Panel security under adversarial attack is primarily an individual-judge quality problem; robustness-first selection combined with Bayesian aggregation addresses both vulnerability channels.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{related_work}
32	\input{threat_model}
33	\input{methodology}
34	\input{results}
35	\input{analysis}
36	\input{conclusion}
37	
38	\section*{Limitations}
39	
40	Our study has three principal limitations. First, the combinatorial panel design (455 panels from 15 shared judges) introduces non-independence: each judge appears in 91 panels, inflating OLS standard errors by $\sim$2.5$\times$. We address this with three correction methods (Appendix~\ref{app:robustness_methods}), but these are conservative; the true significance of $K_{\mathrm{eff}}$ likely lies between the OLS upper bound (8/12) and the bootstrap lower bound (1/12). Second, the six local models use AWQ INT4 quantization, which reduces judge accuracy (Table~\ref{tab:models}) and may affect vulnerability patterns in ways that do not transfer to full-precision deployments. Third, the analysis is observational: the $K_{\mathrm{eff}}$--$\eta_{\max}$ correlation ($r = 0.70$) prevents definitive causal attribution, and six attack types do not exhaust the space of possible adversarial interventions. Future work on partial-knowledge adversaries, bootstrapped GAM confidence intervals, and training-based diversity control \citep{kariyappa2019improving,pang2019improving} could address these gaps.
41	
42	\input{appendix}
43	\input{appendix_attacks}
44	
45	\bibliography{references}
46	
47	\end{document}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "uuid": "1125209e-acb8-48d3-a2f1-f0ac1214d8b6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{definition}{Definition}\n\\newtheorem{proposition}{Proposition}\n\n\\title{The Weakest Judge Wins: What Really Drives LLM Evaluation\\\\Panel Vulnerability Under Adversarial Attack}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, drawing on an implicit analogy to Byzantine fault tolerance. We conduct the first large-scale empirical decomposition of panel vulnerability into individual judge weakness ($\\eta_{\\max}$) and structural diversity ($K_{\\mathrm{eff}}$) under adaptive adversarial attack. Across 15 models from 6 families, 455 panels, 6 attack types, and 2 benchmarks, $\\eta_{\\max}$ is significant in 5 to 8 of 12 conditions depending on non-independence correction method (OLS: 11/12; clustered SE: 8/12; wild cluster bootstrap: 5/12), while $K_{\\mathrm{eff}}$'s significance collapses from 8/12 (OLS) to 0--1/12 after correction, yielding a 5:1 dominance ratio under bootstrap inference. Generalized additive model analysis reveals the structure masked by this collapse: diversity is directionally harmful for targeted attacks and protective for shared-bias attacks, a clean 6:6 split by attack mechanism. The choice of aggregation rule fundamentally modulates vulnerability: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction and weakens $\\eta_{\\max}$, while threshold voting amplifies both ($R^2{=}0.89$). Panel security under adversarial attack is primarily an individual-judge quality problem; robustness-first selection combined with Bayesian aggregation addresses both vulnerability channels.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{threat_model}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur study has three principal limitations. First, the combinatorial panel design (455 panels from 15 shared judges) introduces non-independence: each judge appears in 91 panels, inflating OLS standard errors by $\\sim$2.5$\\times$. We address this with three correction methods (Appendix~\\ref{app:robustness_methods}), but these are conservative; the true significance of $K_{\\mathrm{eff}}$ likely lies between the OLS upper bound (8/12) and the bootstrap lower bound (1/12). Second, the six local models use AWQ INT4 quantization, which reduces judge accuracy (Table~\\ref{tab:models}) and may affect vulnerability patterns in ways that do not transfer to full-precision deployments. Third, the analysis is observational: the $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation ($r = 0.70$) prevents definitive causal attribution, and six attack types do not exhaust the space of possible adversarial interventions. Future work on partial-knowledge adversaries, bootstrapped GAM confidence intervals, and training-based diversity control \\citep{kariyappa2019improving,pang2019improving} could address these gaps.\n\n\\input{appendix}\n\\input{appendix_attacks}\n\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
The Limitations section is inline in main.tex (not a separate file). There's no Ethics section. I need to add the availability statement after Limitations but before `\input{appendix}`. I'll add it directly in main.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "uuid": "9e93b48c-d44c-450e-9ab8-6719cea30fb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAbe7nawqD6RuYotqyLY2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 23719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

_source line 8_

Limitations is inline in `main.tex` at line 38-40, followed by appendix inputs. I'll add the availability statement between Limitations and the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "uuid": "792911cd-54b3-4876-9036-5f3f707b7382",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAbe7nawqD6RuYotqyLY2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 23719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01DoCrA44gKUhh65N96Ec9b4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
  "old_string": "Our study has three principal limitations. First, the combinatorial panel design (455 panels from 15 shared judges) introduces non-independence: each judge appears in 91 panels, inflating OLS standard errors by $\\sim$2.5$\\times$. We address this with three correction methods (Appendix~\\ref{app:robustness_methods}), but these are conservative; the true significance of $K_{\\mathrm{eff}}$ likely lies between the OLS upper bound (8/12) and the bootstrap lower bound (1/12). Second, the six local models use AWQ INT4 quantization, which reduces judge accuracy (Table~\\ref{tab:models}) and may affect vulnerability patterns in ways that do not transfer to full-precision deployments. Third, the analysis is observational: the $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation ($r = 0.70$) prevents definitive causal attribution, and six attack types do not exhaust the space of possible adversarial interventions. Future work on partial-knowledge adversaries, bootstrapped GAM confidence intervals, and training-based diversity control \\citep{kariyappa2019improving,pang2019improving} could address these gaps.\n\n\\input{appendix}",
  "new_string": "Our study has three principal limitations. First, the combinatorial panel design (455 panels from 15 shared judges) introduces non-independence: each judge appears in 91 panels, inflating OLS standard errors by $\\sim$2.5$\\times$. We address this with three correction methods (Appendix~\\ref{app:robustness_methods}), but these are conservative; the true significance of $K_{\\mathrm{eff}}$ likely lies between the OLS upper bound (8/12) and the bootstrap lower bound (1/12). Second, the six local models use AWQ INT4 quantization, which reduces judge accuracy (Table~\\ref{tab:models}) and may affect vulnerability patterns in ways that do not transfer to full-precision deployments. Third, the analysis is observational: the $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation ($r = 0.70$) prevents definitive causal attribution, and six attack types do not exhaust the space of possible adversarial interventions. Future work on partial-knowledge adversaries, bootstrapped GAM confidence intervals, and training-based diversity control \\citep{kariyappa2019improving,pang2019improving} could address these gaps.\n\n\\paragraph{Code and Data Availability}\nCode, the evaluation framework, and all panel-level results will be released upon acceptance. All evaluation items are sampled from publicly available benchmarks: MMLU \\citep{hendrycks2021measuring} and ARC-Challenge \\citep{clark2018think}. The nine API-accessed judge models are served through OpenRouter; the six local judges are open-weight models (Qwen 2.5, Llama 3.1, Mistral Large) in AWQ-quantized form. Individual judge scores, panel compositions, and aggregated vulnerability metrics will be included in the release. All experiments use a fixed random seed (42), and all hyperparameters are reported in the methodology section to support reproducibility.\n\n\\input{appendix}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "uuid": "fa9f6ffd-ce13-4b2b-bb04-23a5c3ccbd7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UAbe7nawqD6RuYotqyLY2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 23719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
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

_source line 10 · 2026-05-22T22:32:45.940Z_

<details><summary>↩ Tool result · `toolu_01DoCrA44gKUhh65N96Ec9b4`</summary>

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
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "uuid": "8550e752-04ae-4424-856c-0d9c0c44b7ab",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/main.tex",
    "oldString": "Our study has three principal limitations. First, the combinatorial panel design (455 panels from 15 shared judges) introduces non-independence: each judge appears in 91 panels, inflating OLS standard errors by $\\sim$2.5$\\times$. We address this with three correction methods (Appendix~\\ref{app:robustness_methods}), but these are conservative; the true significance of $K_{\\mathrm{eff}}$ likely lies between the OLS upper bound (8/12) and the bootstrap lower bound (1/12). Second, the six local models use AWQ INT4 quantization, which reduces judge accuracy (Table~\\ref{tab:models}) and may affect vulnerability patterns in ways that do not transfer to full-precision deployments. Third, the analysis is observational: the $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation ($r = 0.70$) prevents definitive causal attribution, and six attack types do not exhaust the space of possible adversarial interventions. Future work on partial-knowledge adversaries, bootstrapped GAM confidence intervals, and training-based diversity control \\citep{kariyappa2019improving,pang2019improving} could address these gaps.\n\n\\input{appendix}",
    "newString": "Our study has three principal limitations. First, the combinatorial panel design (455 panels from 15 shared judges) introduces non-independence: each judge appears in 91 panels, inflating OLS standard errors by $\\sim$2.5$\\times$. We address this with three correction methods (Appendix~\\ref{app:robustness_methods}), but these are conservative; the true significance of $K_{\\mathrm{eff}}$ likely lies between the OLS upper bound (8/12) and the bootstrap lower bound (1/12). Second, the six local models use AWQ INT4 quantization, which reduces judge accuracy (Table~\\ref{tab:models}) and may affect vulnerability patterns in ways that do not transfer to full-precision deployments. Third, the analysis is observational: the $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation ($r = 0.70$) prevents definitive causal attribution, and six attack types do not exhaust the space of possible adversarial interventions. Future work on partial-knowledge adversaries, bootstrapped GAM confidence intervals, and training-based diversity control \\citep{kariyappa2019improving,pang2019improving} could address these gaps.\n\n\\paragraph{Code and Data Availability}\nCode, the evaluation framework, and all panel-level results will be released upon acceptance. All evaluation items are sampled from publicly available benchmarks: MMLU \\citep{hendrycks2021measuring} and ARC-Challenge \\citep{clark2018think}. The nine API-accessed judge models are served through OpenRouter; the six local judges are open-weight models (Qwen 2.5, Llama 3.1, Mistral Large) in AWQ-quantized form. Individual judge scores, panel compositions, and aggregated vulnerability metrics will be included in the release. All experiments use a fixed random seed (42), and all hyperparameters are reported in the methodology section to support reproducibility.\n\n\\input{appendix}",
    "originalFile": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb,amsthm}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{definition}{Definition}\n\\newtheorem{proposition}{Proposition}\n\n\\title{The Weakest Judge Wins: What Really Drives LLM Evaluation\\\\Panel Vulnerability Under Adversarial Attack}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nMulti-judge LLM evaluation panels are widely assumed to benefit from judge diversity, drawing on an implicit analogy to Byzantine fault tolerance. We conduct the first large-scale empirical decomposition of panel vulnerability into individual judge weakness ($\\eta_{\\max}$) and structural diversity ($K_{\\mathrm{eff}}$) under adaptive adversarial attack. Across 15 models from 6 families, 455 panels, 6 attack types, and 2 benchmarks, $\\eta_{\\max}$ is significant in 5 to 8 of 12 conditions depending on non-independence correction method (OLS: 11/12; clustered SE: 8/12; wild cluster bootstrap: 5/12), while $K_{\\mathrm{eff}}$'s significance collapses from 8/12 (OLS) to 0--1/12 after correction, yielding a 5:1 dominance ratio under bootstrap inference. Generalized additive model analysis reveals the structure masked by this collapse: diversity is directionally harmful for targeted attacks and protective for shared-bias attacks, a clean 6:6 split by attack mechanism. The choice of aggregation rule fundamentally modulates vulnerability: Bayesian calibration reverses $K_{\\mathrm{eff}}$'s direction and weakens $\\eta_{\\max}$, while threshold voting amplifies both ($R^2{=}0.89$). Panel security under adversarial attack is primarily an individual-judge quality problem; robustness-first selection combined with Bayesian aggregation addresses both vulnerability channels.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{threat_model}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{conclusion}\n\n\\section*{Limitations}\n\nOur study has three principal limitations. First, the combinatorial panel design (455 panels from 15 shared judges) introduces non-independence: each judge appears in 91 panels, inflating OLS standard errors by $\\sim$2.5$\\times$. We address this with three correction methods (Appendix~\\ref{app:robustness_methods}), but these are conservative; the true significance of $K_{\\mathrm{eff}}$ likely lies between the OLS upper bound (8/12) and the bootstrap lower bound (1/12). Second, the six local models use AWQ INT4 quantization, which reduces judge accuracy (Table~\\ref{tab:models}) and may affect vulnerability patterns in ways that do not transfer to full-precision deployments. Third, the analysis is observational: the $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation ($r = 0.70$) prevents definitive causal attribution, and six attack types do not exhaust the space of possible adversarial interventions. Future work on partial-knowledge adversaries, bootstrapped GAM confidence intervals, and training-based diversity control \\citep{kariyappa2019improving,pang2019improving} could address these gaps.\n\n\\input{appendix}\n\\input{appendix_attacks}\n\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 39,
        "oldLines": 6,
        "newStart": 39,
        "newLines": 9,
        "lines": [
          " ",
          " Our study has three principal limitations. First, the combinatorial panel design (455 panels from 15 shared judges) introduces non-independence: each judge appears in 91 panels, inflating OLS standard errors by $\\sim$2.5$\\times$. We address this with three correction methods (Appendix~\\ref{app:robustness_methods}), but these are conservative; the true significance of $K_{\\mathrm{eff}}$ likely lies between the OLS upper bound (8/12) and the bootstrap lower bound (1/12). Second, the six local models use AWQ INT4 quantization, which reduces judge accuracy (Table~\\ref{tab:models}) and may affect vulnerability patterns in ways that do not transfer to full-precision deployments. Third, the analysis is observational: the $K_{\\mathrm{eff}}$--$\\eta_{\\max}$ correlation ($r = 0.70$) prevents definitive causal attribution, and six attack types do not exhaust the space of possible adversarial interventions. Future work on partial-knowledge adversaries, bootstrapped GAM confidence intervals, and training-based diversity control \\citep{kariyappa2019improving,pang2019improving} could address these gaps.",
          " ",
          "+\\paragraph{Code and Data Availability}",
          "+Code, the evaluation framework, and all panel-level results will be released upon acceptance. All evaluation items are sampled from publicly available benchmarks: MMLU \\citep{hendrycks2021measuring} and ARC-Challenge \\citep{clark2018think}. The nine API-accessed judge models are served through OpenRouter; the six local judges are open-weight models (Qwen 2.5, Llama 3.1, Mistral Large) in AWQ-quantized form. Individual judge scores, panel compositions, and aggregated vulnerability metrics will be included in the release. All experiments use a fixed random seed (42), and all hyperparameters are reported in the methodology section to support reproducibility.",
          "+",
          " \\input{appendix}",
          " \\input{appendix_attacks}",
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

_source line 11_

Availability statement 已写入 `main.tex`，位于 Limitations 段落之后、appendix 之前，作为 `\paragraph{Code and Data Availability}`。约 100 words，覆盖 code/data/models/reproducibility 四个方面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "uuid": "556a0ded-d24d-4860-b584-69c1a2188ee9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpcMUgihVMacpkZaHzwD7r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1050
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

### Task result

_source line 12_

Availability statement 已写入 `main.tex`，位于 Limitations 段落之后、appendix 之前，作为 `\paragraph{Code and Data Availability}`。约 100 words，覆盖 code/data/models/reproducibility 四个方面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 23799,
  "duration_api_ms": 24831,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "db2387e1-81b3-4834-bd8f-653c225eef22",
  "total_cost_usd": 0.15060125000000002,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 14501,
    "cache_read_input_tokens": 60064,
    "output_tokens": 1148,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 14501,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 73,
        "cache_read_input_tokens": 24898,
        "cache_creation_input_tokens": 1050,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1050
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1148,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001218,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 1148,
      "cacheReadInputTokens": 60064,
      "cacheCreationInputTokens": 14501,
      "webSearchRequests": 0,
      "costUSD": 0.14938325000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "275e4220-edb8-4809-aee2-7c22fdadb7f0"
}
```

</details>

---
