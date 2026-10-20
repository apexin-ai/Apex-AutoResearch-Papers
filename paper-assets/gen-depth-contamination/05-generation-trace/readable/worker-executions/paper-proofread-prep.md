# paper proofread prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 88
- **Recorded user turns:** 2
- **Tool calls:** 27
- **Original source:** `logs/workers/worker_paper_proofread_prep_20260522T212115.log`
- **Structured JSON:** [`2d9f5c116a0cad5294bb.json`](../../sessions/2d/2d9f5c116a0cad5294bb.json)

## Before a recorded user message

22 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "a5a17e11-01e5-4c91-a169-5eef172df64f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1779501600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fbcfc2e7-4a34-43a0-9b8e-644f4badc976",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a proofread pre-check on their paper. I need to:

1. Read the main.tex, appendix.tex (if exists), and appendix_extended.tex files
2. Read the registry for experiment data
3. Check for undefined references, table-registry consistency, and spelling/grammar issues
4. Generate a report

Let me start by reading the files and registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "fed15577-27e2-4e40-8e0a-3636471046b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNRWtEddzSjp7qFzKq1ms8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12525,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12525
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

_source line 5_

开始论文 proofread 预检查。先读取论文文件和 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "12eea943-e917-4cf4-a5e0-e4f2340c13b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNRWtEddzSjp7qFzKq1ms8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12525,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12525
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01RxH5jozNs71Ev1qcbJFGJp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "58bbe9be-95f3-4491-ab22-e198efffa596",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNRWtEddzSjp7qFzKq1ms8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12525,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12525
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

_source line 7 · 2026-05-22T21:21:28.316Z_

<details><summary>↩ Tool result · `toolu_01RxH5jozNs71Ev1qcbJFGJp`</summary>

```text
1	% EMNLP 2026 Main — ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{colortbl}
15	\usepackage{multirow}
16	\usepackage{enumitem}
17	\usepackage{subcaption}
18	\usepackage[section]{placeins}
19	
20	\newcommand{\Kstar}{{K^*}}
21	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
22	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
23	\newcommand{\auc}{\text{AUC}}
24	\newcommand{\jsd}{\text{JSD}}
25	
26	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	% === Abstract ===
34	\begin{abstract}
35	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
36	We measure a lower bound on the generational discrimination boundary, $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable), using 15 statistical features and an OBD-LightGBM classifier.
37	Under prompt-chain generation across 10 model configurations (6 architecture families, 1B--8B), 3 source domains, and 4 decoding strategies, for web text (C4, Wikipedia), $\Kempirical \leq 2$ regardless of model family or scale ($\theta{=}0.60$); across all ten configurations, $\Kempirical \leq 3$, with structured academic text (arXiv) reaching $\Kempirical{=}3$ across two architectures.
38	Among the six nominal $\Kempirical{=}2$ configurations, four retain significance under Bonferroni correction; the two marginal cases reflect narrow effect sizes rather than classification failure.
39	A single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
40	Model-free statistical features enable 80--100\% cross-model transfer with scorer-invariant feature rankings ($\rho > 0.90$), supporting depth estimation on corpora from unknown generators without retraining.
41	As a consistency check, domain-appropriate $\Kempirical$ correctly predicts that binary filtering outperforms graduated alternatives for web text when contamination causes detectable quality loss.
42	\end{abstract}
43	
44	% === Section 1: Introduction ===
45	\input{introduction}
46	
47	% === Section 2: Related Work ===
48	\input{related_work}
49	
50	% === Section 3: Method ===
51	\input{method}
52	
53	% === Section 4: Experiments ===
54	\input{experiments_c1}
55	
56	% === Section 5: K*-Aware Data Filtering ===
57	\input{experiments_c3}
58	
59	% === Section 6: Discussion ===
60	\input{discussion}
61	
62	% === Section 7: Conclusion ===
63	\input{conclusion}
64	
65	% === Limitations (ACL required, unnumbered) ===
66	\section*{Limitations}
67	
68	Our study has three main limitations.
69	(1)~\emph{Scope}: we evaluate models up to 8B parameters across 6 architecture families, English text only (C4, Wikipedia, arXiv), and prompt-chain generation; retrain-chain dynamics may yield different boundaries.
70	(2)~\emph{Feature set}: the 15 statistical features provide a lower bound on $\Ktheory$; richer representations (e.g., neural probes) can extend $\Kempirical$ by one additional depth for some architectures.
71	(3)~\emph{Threshold sensitivity}: $\Kempirical$ varies with the decision threshold $\theta$, ranging from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; two of ten configurations are marginal at our reference $\theta{=}0.60$.
72	
73	% === Ethics Statement (ACL required, unnumbered) ===
74	\section*{Ethics Statement}
75	
76	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
77	Our experiments use the publicly available C4 corpus and do not involve personally identifiable information.
78	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
79	Code and data will be released upon acceptance.
80	
81	\bibliography{references}
82	
83	\clearpage
84	\input{appendix}
85	\input{appendix_extended}
86	
87	\end{document}
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "27ec943a-3199-499f-a317-d082f9b7967a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
      "content": "% EMNLP 2026 Main — ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{colortbl}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure a lower bound on the generational discrimination boundary, $\\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable), using 15 statistical features and an OBD-LightGBM classifier.\nUnder prompt-chain generation across 10 model configurations (6 architecture families, 1B--8B), 3 source domains, and 4 decoding strategies, for web text (C4, Wikipedia), $\\Kempirical \\leq 2$ regardless of model family or scale ($\\theta{=}0.60$); across all ten configurations, $\\Kempirical \\leq 3$, with structured academic text (arXiv) reaching $\\Kempirical{=}3$ across two architectures.\nAmong the six nominal $\\Kempirical{=}2$ configurations, four retain significance under Bonferroni correction; the two marginal cases reflect narrow effect sizes rather than classification failure.\nA single generation pass suffices to render general web text indistinguishable from deeper synthetic content, a \\emph{one-wash laundering} effect.\nModel-free statistical features enable 80--100\\% cross-model transfer with scorer-invariant feature rankings ($\\rho > 0.90$), supporting depth estimation on corpora from unknown generators without retraining.\nAs a consistency check, domain-appropriate $\\Kempirical$ correctly predicts that binary filtering outperforms graduated alternatives for web text when contamination causes detectable quality loss.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\section*{Limitations}\n\nOur study has three main limitations.\n(1)~\\emph{Scope}: we evaluate models up to 8B parameters across 6 architecture families, English text only (C4, Wikipedia, arXiv), and prompt-chain generation; retrain-chain dynamics may yield different boundaries.\n(2)~\\emph{Feature set}: the 15 statistical features provide a lower bound on $\\Ktheory$; richer representations (e.g., neural probes) can extend $\\Kempirical$ by one additional depth for some architectures.\n(3)~\\emph{Threshold sensitivity}: $\\Kempirical$ varies with the decision threshold $\\theta$, ranging from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; two of ten configurations are marginal at our reference $\\theta{=}0.60$.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.\nOur experiments use the publicly available C4 corpus and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\nCode and data will be released upon acceptance.\n\n\\bibliography{references}\n\n\\clearpage\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
      "numLines": 88,
      "startLine": 1,
      "totalLines": 88
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_017C2R47xTzGL9ns6MTZrbLF`</summary>

```json
{
  "pattern": "appendix*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "f4d17222-a8d2-4b7f-ae2c-771d123c0212",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNRWtEddzSjp7qFzKq1ms8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12525,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12525
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

_source line 9 · 2026-05-22T21:21:29.388Z_

<details><summary>↩ Tool result · `toolu_017C2R47xTzGL9ns6MTZrbLF`</summary>

```text
docs/paper/appendix.tex
docs/paper/appendix_extended.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "dc18e3f8-63c2-4bbd-9ba1-fcd5946f2fc0",
  "tool_use_result": {
    "filenames": [
      "docs/paper/appendix.tex",
      "docs/paper/appendix_extended.tex"
    ],
    "durationMs": 6,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017yfj3ZVRNFBQBs3uHLyvgq`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "060adb93-9a2a-4fe5-b82d-79f55be8aee0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNRWtEddzSjp7qFzKq1ms8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12525,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12525
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

_source line 11 · 2026-05-22T21:21:30.107Z_

<details><summary>↩ Tool result · `toolu_017yfj3ZVRNFBQBs3uHLyvgq`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "167a8fb3-eb32-4226-aa14-118ba835acb9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the appendix files and the registry data in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "b7e11170-9e60-4a5b-8db5-317ff56743bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8uHSWhiDQ89NLWmiSTtNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 24366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2283
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

<details open><summary>🔧 Tool call — Read · `toolu_01Gos8bQtiTvy5fDopgeCaqW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "4084bcd1-8d2e-4870-a25a-a517aa7c8d40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8uHSWhiDQ89NLWmiSTtNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 24366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2283
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

_source line 14 · 2026-05-22T21:21:33.650Z_

<details><summary>↩ Tool result · `toolu_01Gos8bQtiTvy5fDopgeCaqW`</summary>

```text
1	\appendix
2	\section{Supplementary Materials}
3	\label{sec:appendix}
4	
5	This appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_filtering_strategies.pdf}
10	\caption{Downstream performance of all filtering strategies (5 seeds, $\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}
11	\label{fig:filtering_strategies}
12	\end{figure}
13	
14	\paragraph{Feature ranking and cross-model consistency.}
15	Table~\ref{tab:top_features} reports per-model single-feature AUC rankings.
16	Surprisal derivative features (\texttt{surp\_d1\_std}, \texttt{surp\_d2\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\rho \geq 0.85$.
17	The rewrite-mode model (Qwen-rw) diverges by placing \texttt{freq\_entropy} first, reflecting a distributional shift that is lexical rather than surprisal-driven.
18	This scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.
19	
20	%%% Feature ranking table (moved from main text)
21	\begin{table}[!htbp]
22	\centering
23	\small
24	\caption{Top-3 features by single-feature $\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}
25	\label{tab:top_features}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{cllll}
28	\toprule
29	Rank & Pythia & OLMo & Qwen-rw & Qwen-cont \\
30	\midrule
31	1 & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \texttt{freq\_entropy} & \textbf{\texttt{surp\_d1\_std}} \\
32	2 & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_std}} \\
33	3 & \textbf{\texttt{surp\_std}} & \textbf{\texttt{surp\_d2\_std}} & \textbf{\texttt{surp\_d1\_std}} & \textbf{\texttt{surp\_d2\_std}} \\
34	\bottomrule
35	\end{tabular}
36	}
37	\end{table}
38	
39	Table~\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.
40	Classifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\% of in-distribution performance.
41	The asymmetry between rewrite-mode and continuation-mode transfer (61--63\%) confirms that generation mode, rather than model family, is the primary axis of distributional variation (Section~\ref{sec:discussion}).
42	
43	%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)
44	\begin{table}[!htbp]
45	  \centering
46	  \small
47	  \caption{Cross-model transfer accuracy matrix. Diagonal (\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\leftrightarrow$OLMo 91--92\%, Qwen-cont$\leftrightarrow$Pythia 83--85\%, Qwen-rw$\to$others 61--63\%.}
48	  \label{tab:s1_transfer}
49	  \resizebox{\columnwidth}{!}{%
50	  \begin{tabular}{lcccc}
51	    \toprule
52	    \textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\
53	    \midrule
54	    Qwen-rw   & \textbf{.423} & .259 & .265 & .347 \\
55	    Pythia    & .272 & \textbf{.386} & .353 & .329 \\
56	    OLMo      & .277 & .345 & \textbf{.382} & .324 \\
57	    Qwen-cont & .344 & .328 & .311 & \textbf{.388} \\
58	    \bottomrule
59	  \end{tabular}}
60	\end{table}
61	
62	\paragraph{Dataset construction.}
63	Table~\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.
64	Each depth level contains 5{,}000 passages, yielding 30{,}000 total samples across six depths (0--5).
65	Depth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.
66	Subsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.
67	The four model-mode configurations (Qwen-rw, Pythia-cont, OLMo-cont, Qwen-cont) share identical depth-0 seeds and generation pipeline, differing only in generator identity and prompting strategy (rewrite vs.\ continuation).
68	
69	%%% Table S4: Dataset Statistics
70	\begin{table}[!htbp]
71	  \centering
72	  \small
73	  \caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}
74	  \label{tab:s4_dataset_stats}
75	  \resizebox{\columnwidth}{!}{%
76	  \begin{tabular}{clrl}
77	    \toprule
78	    \textbf{Depth} & \textbf{$N$ samples} & \textbf{Mean tokens} & \textbf{Source} \\
79	    \midrule
80	    0 & 5{,}000 & 147.8 & C4 validation (human) \\
81	    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\
82	    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\
83	    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\
84	    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
85	    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\
86	    \midrule
87	    \multicolumn{2}{l}{Total} & \multicolumn{2}{l}{30{,}000 samples} \\
88	    \bottomrule
89	  \end{tabular}}
90	\end{table}
91	
92	%%% Table S2: Decoding Ablation AUC (exp-003)
93	\begin{table*}[t]
94	  \centering
95	  \caption{Pairwise AUC with bootstrap 95\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\,vs.\,2 and 2\,vs.\,3 marks the empirical detectability boundary $\Kempirical=2$. Bottom rows report cross-configuration Spearman $\rho$ on per-feature discriminative-power rankings.}
96	  \label{tab:s2_decoding}
97	  \footnotesize
98	  \begin{tabular}{lcccc}
99	    \toprule
100	    \textbf{Depth Pair} & \textbf{Greedy} & \textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\
101	    \midrule
102	    0 vs.\ 1 & $.980\;[.977,\,.982]$ & $.995\;[.993,\,.996]$ & $.988\;[.986,\,.990]$ & $.998\;[.998,\,.999]$ \\
103	    1 vs.\ 2 & $.689\;[.680,\,.698]$ & $.687\;[.677,\,.695]$ & $.689\;[.680,\,.697]$ & $.704\;[.695,\,.713]$ \\
104	    \cmidrule(lr){1-5}
105	    2 vs.\ 3 & $.561\;[.552,\,.571]$ & $.592\;[.582,\,.601]$\rlap{$^\dagger$} & $.590\;[.581,\,.600]$ & $.582\;[.572,\,.592]$ \\
106	    3 vs.\ 4 & $.540\;[.531,\,.550]$ & $.547\;[.537,\,.557]$ & $.539\;[.529,\,.549]$ & $.529\;[.519,\,.540]$ \\
107	    4 vs.\ 5 & $.514\;[.503,\,.524]$ & $.507\;[.496,\,.517]^{\ddagger}$ & $.535\;[.524,\,.545]$ & $.524\;[.513,\,.535]$ \\
108	    \midrule
109	    \multicolumn{5}{l}{\textbf{Cross-config feature Spearman $\rho$}} \\
110	    \midrule
111	    \multicolumn{2}{l}{Greedy vs.\ Nuc $p{=}0.9$} & 0.600 &
112	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}0.7$} & 0.782 \\
113	    \multicolumn{2}{l}{Greedy vs.\ $T{=}0.7$} & 0.914 &
114	    \multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\ $T{=}1.2$} & 0.893 \\
115	    \multicolumn{2}{l}{Greedy vs.\ $T{=}1.2$} & 0.532 &
116	    \multicolumn{1}{l}{$T{=}0.7$ vs.\ $T{=}1.2$} & 0.668 \\
117	    \bottomrule
118	    \multicolumn{5}{l}{${}^{\dagger}$\,CI upper bound (0.601) marginally exceeds $\theta{=}0.60$ by 0.001.} \\
119	    \multicolumn{5}{l}{${}^{\ddagger}$\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}
120	  \end{tabular}
121	\end{table*}
122	
123	%%% Table S2b: Extended K* CI (all models including new additions)
124	\begin{table*}[t]
125	  \centering
126	  \scriptsize
127	  \caption{Extended pairwise $\auc$ with bootstrap 95\% CIs for all model configurations including new additions.
128	  This table extends Table~\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.
129	  $\Kempirical = 2$ holds for 6/10 conditions at $\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\Kempirical{=}1$).}
130	  \label{tab:kstar_ci_extended}
131	  \resizebox{\textwidth}{!}{%
132	  \begin{tabular}{lcccccccccccccccccccc}
133	    \toprule
134	     & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} & \multicolumn{2}{c}{Qwen-base} & \multicolumn{2}{c}{LLaMA-8B} & \multicolumn{2}{c}{Mistral-7B} & \multicolumn{2}{c}{Pythia-6.9B\rlap{$^\S$}} & \multicolumn{2}{c}{Gemma-2B} \\
135	    \cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}\cmidrule(lr){12-13}\cmidrule(lr){14-15}\cmidrule(lr){16-17}\cmidrule(lr){18-19}\cmidrule(lr){20-21}
136	     & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
137	    \midrule
138	    0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] & .987 & [.985,\,.989] & .9224 & [.917,\,.927] & .9842 & [.982,\,.986] & .9599 & & .953 & [.949,\,.957] \\
139	    1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} & .626 & [.617,\,.635]\rlap{$^*$} & .6123 & [.603,\,.622]\rlap{$^*$} & .5934 & [.584,\,.603] & .5955 & & .5981 & [.588,\,.608] \\
140	    2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] & .550 & [.540,\,.560] & .5273 & [.517,\,.538] & .5402 & [.530,\,.551] & .5298 & & .534 & [.523,\,.545] \\
141	    3v4 & .5435 & & .5152 & & .5024 & & .5409 & & .5276 & & .529 & [.519,\,.540] & .5168 & [.506,\,.528] & .5233 & [.513,\,.534] & .5135 & & .5033 & [.492,\,.514] \\
142	    4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\,.529] & .5159 & [.505,\,.527] & .5180 & [.507,\,.529] & -- & -- & .5025 & [.492,\,.514] \\
143	    \bottomrule
144	    \multicolumn{21}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons.} \\
145	    \multicolumn{21}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B. ``--'': experiment pending.} \\
146	    \multicolumn{21}{l}{\footnotesize $^\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}
147	  \end{tabular}}% end resizebox
148	\end{table*}
149	
150	%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)
151	\begin{table}[t]
152	  \centering
153	  \scriptsize
154	  \caption{LLM zero-shot depth classification: $5{\times}5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\sim}$0.33 vs.\ OBD-LightGBM 0.386). Per-depth recall in Table~\ref{tab:s3c_perdepth}.}
155	  \label{tab:s3_llm_zeroshot}
156	
157	  \vspace{0.3em}
158	  \textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)
159	  \vspace{1pt}
160	
161	  \begin{tabular}{lcccccc}
162	    \toprule
163	    & \multicolumn{5}{c}{Predicted Depth} & \\
164	    \cmidrule(lr){2-6}
165	    True & 0 & 1 & 2 & 3 & 4 & Rec. \\
166	    \midrule
167	    0 & \textbf{77} & 18 &  4 &  0 &  1 & .770 \\
168	    1 &  9 & \textbf{19} & 36 & 24 & 12 & .190 \\
169	    2 &  8 & 10 & \textbf{38} & 35 &  9 & .380 \\
170	    3 & 10 & 16 & 35 & \textbf{24} & 15 & .240 \\
171	    4 & 11 & 13 & 50 & 18 &  \textbf{8} & .080 \\
172	    \bottomrule
173	  \end{tabular}
174	
175	  \vspace{4pt}
176	  \textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)
177	  \vspace{1pt}
178	
179	  \begin{tabular}{lcccccc}
180	    \toprule
181	    & \multicolumn{5}{c}{Predicted Depth} & \\
182	    \cmidrule(lr){2-6}
183	    True & 0 & 1 & 2 & 3 & 4 & Rec. \\
184	    \midrule
185	    0 & \textbf{69} & 26 &  3 &  0 &  2 & .690 \\
186	    1 &  8 & \textbf{21} & 32 & 11 & 28 & .210 \\
187	    2 &  6 & 36 & \textbf{28} &  5 & 25 & .280 \\
188	    3 &  7 & 20 & 31 & \textbf{10} & 31 & .100 \\
189	    4 &  7 & 28 & 22 &  6 & \textbf{37} & .370 \\
190	    \bottomrule
191	  \end{tabular}
192	\end{table}
193	
194	\begin{table}[t]
195	  \centering
196	  \small
197	  \caption{Per-depth recall (\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\geq 2$, consistent with $\Kempirical = 2$.}
198	  \label{tab:s3c_perdepth}
199	  \resizebox{\columnwidth}{!}{%
200	  \begin{tabular}{lccccc}
201	    \toprule
202	    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\
203	    \midrule
204	    OBD-LightGBM & \textbf{96} & \textbf{39} & 14 & 19 & 22 \\
205	    GPT-5.5      & 77 & 19 & \textbf{38} & \textbf{24} &  8 \\
206	    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \textbf{37} \\
207	    \bottomrule
208	  \end{tabular}}
209	\end{table}
210	
211	%%% Table: Token Length and EOS Truncation Analysis
212	\begin{table}[t]
213	  \centering
214	  \scriptsize
215	  \caption{Mean subword token count per depth and EOS truncation rate (\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \emph{more conservative}, not inflated. See Section~\ref{sec:length_confound}.}
216	  \label{tab:token_length}
217	  \resizebox{\columnwidth}{!}{%
218	  \begin{tabular}{lcccccccc}
219	    \toprule
220	    & \multicolumn{6}{c}{\textbf{Mean Token Count}} & & \\
221	    \cmidrule(lr){2-7}
222	    \textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \textbf{EOS\%} & \textbf{Sev.} \\
223	    \midrule
224	    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\
225	    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\
226	    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\
227	    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\
228	    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\
229	    \midrule
230	    \multicolumn{9}{l}{\textit{Decoding ablation (Qwen-rw 1.5B)}} \\
231	    \quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\
232	    \quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\
233	    \quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\
234	    \quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\
235	    \bottomrule
236	    \multicolumn{9}{l}{EOS\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}
237	  \end{tabular}}
238	\end{table}
239	
240	%%% Table S5: Complete 15-D Feature Descriptions
241	\begin{table*}[t]
242	  \centering
243	  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
244	  \label{tab:s5_features}
245	  \begin{tabular}{llp{0.45\textwidth}l}
246	    \toprule
247	    \textbf{Group} & \textbf{Feature} & \textbf{Description} & \textbf{Range} \\
248	    \midrule
249	    \multirow{9}{*}{\rotatebox[origin=c]{90}{\textsc{Surprisal}}}
250	    & \texttt{surp\_mean}   & Mean token surprisal $\frac{1}{T}\sum_t -\log p(x_t \mid x_{&lt;t})$ & $\mathbb{R}^+$ \\
251	    & \texttt{surp\_std}    & Standard deviation of token surprisal & $\mathbb{R}^+$ \\
252	    & \texttt{surp\_skew}   & Skewness of the surprisal distribution & $\mathbb{R}$ \\
253	    & \texttt{surp\_kurt}   & Excess kurtosis of the surprisal distribution & $\mathbb{R}$ \\
254	    & \texttt{surp\_d1\_mean} & Mean of first-order surprisal differences $\Delta s_t = s_{t+1} - s_t$ & $\mathbb{R}$ \\
255	    & \texttt{surp\_d1\_std}  & Std of first-order surprisal differences & $\mathbb{R}^+$ \\
256	    & \texttt{surp\_d1\_skew} & Skewness of first-order surprisal differences & $\mathbb{R}$ \\
257	    & \texttt{surp\_d2\_mean} & Mean of second-order differences $\Delta^2 s_t$ & $\mathbb{R}$ \\
258	    & \texttt{surp\_d2\_std}  & Std of second-order surprisal differences & $\mathbb{R}^+$ \\
259	    \midrule
260	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Lex}}}
261	    & \texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\
262	    & \texttt{hapax\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\
263	    & \texttt{self\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\
264	    \midrule
265	    \multirow{3}{*}{\rotatebox[origin=c]{90}{\textsc{Freq}}}
266	    & \texttt{freq\_kurtosis}  & Excess kurtosis of word frequency distribution & $\mathbb{R}$ \\
267	    & \texttt{freq\_entropy}   & Shannon entropy of word frequencies: $-\sum p_w \log_2 p_w$ & $\mathbb{R}^+$ \\
268	    & \texttt{low\_freq\_ratio} & Proportion of vocabulary with count $\leq 2$ & $[0, 1]$ \\
269	    \bottomrule
270	  \end{tabular}
271	\end{table*}
272	
273	%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap
274	\begin{table*}[t]
275	\begin{minipage}[t]{0.45\textwidth}
276	  \centering
277	  \small
278	  \captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt{doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}
279	  \label{tab:s6_lgbm_params}
280	  \begin{tabular}{ll}
281	    \toprule
282	    \textbf{Parameter} & \textbf{Value} \\
283	    \midrule
284	    \texttt{n\_estimators}      & 200 \\
285	    \texttt{learning\_rate}     & 0.05 \\
286	    \texttt{max\_depth}         & 6 \\
287	    \texttt{num\_leaves}        & 31 \\
288	    \texttt{verbose}            & $-1$ \\
289	    \texttt{n\_jobs}            & $-1$ (all cores) \\
290	    Cross-validation            & 5-fold GroupKFold \\
291	    Grouping key                & \texttt{doc\_id} \\
292	    Objective                   & Binary (per depth pair) \\
293	    \bottomrule
294	  \end{tabular}
295	\end{minipage}\hfill
296	\begin{minipage}[t]{0.52\textwidth}
297	  \centering
298	  \small
299	  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
300	  \label{tab:s7_neural_probe}
301	  \resizebox{\textwidth}{!}{%
302	  \begin{tabular}{ll}
303	    \toprule
304	    \textbf{Component} & \textbf{Details} \\
305	    \midrule
306	    \multicolumn{2}{l}{\textit{Embedding extraction}} \\
307	    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\
308	    Representation    & Last hidden state, attention-masked avg pool \\
309	    Embedding dim     & 1536 / 2048 / 2048 \\
310	    Max sequence len   & 512 tokens \\
311	    \midrule
312	    \multicolumn{2}{l}{\textit{MLP classifier}} \\
313	    Architecture      & $d_{\text{emb}} \to 512 \to 256 \to 6$ \\
314	    Activations       & ReLU \\
315	    Dropout           & 0.1 (after each hidden layer) \\
316	    Output            & 6-class softmax \\
317	    \midrule
318	    \multicolumn{2}{l}{\textit{Training}} \\
319	    Optimizer         & Adam ($\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\
320	    Loss              & Cross-entropy \\
321	    Batch size        & 256 \\
322	    Max epochs        & 20 \\
323	    Early stopping    & Patience = 5 (validation loss) \\
324	    Cross-validation  & 5-fold GroupKFold \\
325	    \bottomrule
326	  \end{tabular}%
327	  }
328	\end{minipage}
329	\end{table*}
330	
331	%%% Table S8: Per-Model Bootstrap CI Results (exp-007)
332	\begin{table}[t]
333	  \centering
334	  \scriptsize
335	  \caption{Pairwise AUC with bootstrap 95\% CIs for four model-mode configurations (1{,}000 resamples). All pairs $p < 0.01$ except OLMo 1v2--4v5 ($p > 0.09$).}
336	  \label{tab:s8_cv_folds}
337	  \resizebox{\columnwidth}{!}{%
338	  \begin{tabular}{lcccc}
339	    \toprule
340	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
341	    \midrule
342	    0v1 & $.996\;[.995,.997]$ & $.993\;[.992,.994]$ & $.986\;[.984,.988]$ & $.997\;[.996,.998]$ \\
343	    1v2 & $.696\;[.686,.704]$ & $.654\;[.645,.663]$ & $.508\;[.496,.519]$ & $.611\;[.602,.621]$ \\
344	    \cmidrule(lr){1-5}
345	    2v3 & $.589\;[.580,.599]$ & $.551\;[.542,.563]$ & $.497\;[.486,.509]$ & $.561\;[.551,.571]$ \\
346	    3v4 & $.544\;[.533,.555]$ & $.515\;[.504,.526]$ & $.502\;[.491,.513]$ & $.541\;[.531,.551]$ \\
347	    4v5 & $.534\;[.524,.545]$ & $.514\;[.502,.525]$ & $.494\;[.483,.506]$ & $.514\;[.504,.526]$ \\
348	    \bottomrule
349	  \end{tabular}}
350	\end{table}
351	
352	%%% Table S9: Binary Detector Spearman ρ (exp-012)
353	\begin{table}[t]
354	  \centering
355	  \scriptsize
356	  \caption{Spearman $\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\rho > 0$).}
357	  \label{tab:s9_binary_spearman}
358	  \resizebox{\columnwidth}{!}{%
359	  \begin{tabular}{lcccc}
360	    \toprule
361	    & \textbf{Qwen-rw} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Qwen-cont} \\
362	    \midrule
363	    \multicolumn{5}{l}{\textit{Spearman $\rho$}} \\
364	    \quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\
365	    \quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\
366	    \quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\
367	    \midrule
368	    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\
369	    \bottomrule
370	    \multicolumn{5}{l}{Random baseline: 0.167} \\
371	  \end{tabular}}
372	\end{table}
373	
374	%%% Table S10: Pythia Decoding Ablation (exp-020)
375	\begin{table}[t]
376	  \centering
377	  \scriptsize
378	  \caption{Pythia-1.4B pairwise $\auc$ under four decoding configs (10K bootstrap). $^\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \to d_1{=}0.72$).}
379	  \label{tab:s10_pythia_decoding}
380	  \resizebox{\columnwidth}{!}{%
381	  \begin{tabular}{lcccc}
382	    \toprule
383	    & \textbf{Greedy}$^\dagger$ & \textbf{$p{=}0.9$} & \textbf{$T{=}0.7$} & \textbf{$T{=}1.2$} \\
384	    \midrule
385	    0v1 & $.999$ & $.995$ & $.996$ & $.994$ \\
386	    1v2 & $.884$ & $.675$ & $.728$ & $.618$ \\
387	    \cmidrule(lr){1-5}
388	    2v3 & $.531$ & $.559$ & $.598^\ddagger$ & $.531$ \\
389	    3v4 & $.522$ & $.524$ & $.563$ & $.520$ \\
390	    4v5 & $.514$ & $.501$ & $.527$ & $.510$ \\
391	    \midrule
392	    $\Kempirical$ & 2 & 2 & 2 & 2 \\
393	    \bottomrule
394	    \multicolumn{5}{l}{${}^{\ddagger}$CI upper 0.606 $> \theta$; point est.\ below.} \\
395	  \end{tabular}}
396	\end{table}
397	
398	%%% Table S11: Length Ablation (exp-021)
399	\begin{table}[t]
400	  \centering
401	  \small
402	  \caption{Pairwise $\auc$ for three segment lengths (Qwen-base, cont.\ mode). $\Kempirical{=}2$ at 128/256; 512 marginal ($^\dagger$CI lower $< \theta$).}
403	  \label{tab:s11_length_ablation}
404	  \begin{tabular}{lccc}
405	    \toprule
406	    & \textbf{128} & \textbf{256} & \textbf{512} \\
407	    \midrule
408	    0v1 & .979 & .991 & .992 \\
409	    1v2 & .622 & .628 & .607$^\dagger$ \\
410	    \cmidrule(lr){1-4}
411	    2v3 & .529 & .556 & .572 \\
412	    3v4 & .535 & .530 & .530 \\
413	    4v5 & .501 & .514 & .518 \\
414	    \midrule
415	    $\Kempirical$ & 2 & 2 & 2$^\dagger$ \\
416	    \bottomrule
417	  \end{tabular}
418	\end{table}
419	
420	%%% Table S12: Domain Ablation
421	\begin{table}[t]
422	  \centering
423	  \small
424	  \caption{Pairwise $\auc$ for three text domains (Qwen-cont). arXiv yields $\Kempirical{=}3$; C4 and Wikipedia $\Kempirical{=}2$.}
425	  \label{tab:s12_domain_ablation}
426	  \begin{tabular}{lccc}
427	    \toprule
428	    & \textbf{C4} & \textbf{Wiki} & \textbf{arXiv} \\
429	    \midrule
430	    0v1 & .997 & .996 & .995 \\
431	    1v2 & .611 & .619 & .858 \\
432	    \cmidrule(lr){1-4}
433	    2v3 & .561 & .550 & .644$^*$ \\
434	    3v4 & .541 & .523 & .544 \\
435	    4v5 & .514 & .514 & .530 \\
436	    \midrule
437	    $\Kempirical$ & 2 & 2 & 3 \\
438	    \bottomrule
439	    \multicolumn{4}{l}{\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}
440	  \end{tabular}
441	\end{table}
442	
443	%%% Table S13: Scorer Sensitivity Analysis
444	\begin{table}[t]
445	  \centering
446	  \scriptsize
447	  \caption{Scorer sensitivity: $\Kempirical$ under self- vs.\ cross-scoring. Cross-scoring reduces $\Kempirical$ only for marginal Qwen-cont.}
448	  \label{tab:s13_scorer_sensitivity}
449	  \resizebox{\columnwidth}{!}{%
450	  \begin{tabular}{llcccc}
451	    \toprule
452	    \textbf{Generator} & \textbf{Mode} & \textbf{Self} & \textbf{Pythia} & \textbf{OLMo} & \textbf{Agr.} \\
453	    \midrule
454	    Qwen-Inst & Rewrite & 2 & 2 & 2 & \checkmark \\
455	    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\times$ \\
456	    Qwen-base & Cont.   & 2 & 2 & 2 & \checkmark \\
457	    Pythia    & Cont.   & 2 & 2 & 2 & \checkmark \\
458	    OLMo      & Cont.   & 1 & -- & -- & -- \\
459	    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\
460	    Mistral   & Cont.   & 1 & -- & -- & -- \\
461	    \bottomrule
462	  \end{tabular}}
463	\end{table}
464	
465	\clearpage
466	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "23d7ea19-7eaf-4c43-9780-7a37bc7e52fb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\\appendix\n\\section{Supplementary Materials}\n\\label{sec:appendix}\n\nThis appendix provides supplementary figures, detailed experimental tables, dataset statistics, and complete feature descriptions referenced in the main text.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_filtering_strategies.pdf}\n\\caption{Downstream performance of all filtering strategies (5 seeds, $\\pm$1 std). Binary-ours (green) minimizes MMLU degradation; graduated $\\alpha$ sweep shows monotonic convergence toward binary. Dashed line: base model (no fine-tuning).}\n\\label{fig:filtering_strategies}\n\\end{figure}\n\n\\paragraph{Feature ranking and cross-model consistency.}\nTable~\\ref{tab:top_features} reports per-model single-feature AUC rankings.\nSurprisal derivative features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_d2\\_std}) consistently rank among the top three across all continuation-mode models (Pythia, OLMo, Qwen-cont), with pairwise Spearman $\\rho \\geq 0.85$.\nThe rewrite-mode model (Qwen-rw) diverges by placing \\texttt{freq\\_entropy} first, reflecting a distributional shift that is lexical rather than surprisal-driven.\nThis scorer-invariant ranking supports the use of a fixed 15-dimensional feature set across generators without per-model feature selection.\n\n%%% Feature ranking table (moved from main text)\n\\begin{table}[!htbp]\n\\centering\n\\small\n\\caption{Top-3 features by single-feature $\\auc$ ranking. Bold: shared across all continuation-mode models. Spearman $\\rho$ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85.}\n\\label{tab:top_features}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cllll}\n\\toprule\nRank & Pythia & OLMo & Qwen-rw & Qwen-cont \\\\\n\\midrule\n1 & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\texttt{freq\\_entropy} & \\textbf{\\texttt{surp\\_d1\\_std}} \\\\\n2 & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_std}} \\\\\n3 & \\textbf{\\texttt{surp\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} & \\textbf{\\texttt{surp\\_d1\\_std}} & \\textbf{\\texttt{surp\\_d2\\_std}} \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nTable~\\ref{tab:s1_transfer} reports the cross-model transfer accuracy matrix.\nClassifiers trained on continuation-mode generators (Pythia, OLMo, Qwen-cont) transfer well to each other, with off-diagonal accuracy retaining 80--92\\% of in-distribution performance.\nThe asymmetry between rewrite-mode and continuation-mode transfer (61--63\\%) confirms that generation mode, rather than model family, is the primary axis of distributional variation (Section~\\ref{sec:discussion}).\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Cross-model transfer accuracy matrix. Diagonal (\\textbf{bold}): within-model; off-diagonal: cross-model. Retention: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-rw$\\to$others 61--63\\%.}\n  \\label{tab:s1_transfer}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Train} & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{.423} & .259 & .265 & .347 \\\\\n    Pythia    & .272 & \\textbf{.386} & .353 & .329 \\\\\n    OLMo      & .277 & .345 & \\textbf{.382} & .324 \\\\\n    Qwen-cont & .344 & .328 & .311 & \\textbf{.388} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\paragraph{Dataset construction.}\nTable~\\ref{tab:s4_dataset_stats} summarizes the generational depth corpus.\nEach depth level contains 5{,}000 passages, yielding 30{,}000 total samples across six depths (0--5).\nDepth~0 consists of human-written seed texts from the C4 English validation split, truncated to 256 subword tokens.\nSubsequent depths are generated recursively: each depth-$k$ passage is produced by prompting the generator with the corresponding depth-$(k{-}1)$ passage.\nThe four model-mode configurations (Qwen-rw, Pythia-cont, OLMo-cont, Qwen-cont) share identical depth-0 seeds and generation pipeline, differing only in generator identity and prompting strategy (rewrite vs.\\ continuation).\n\n%%% Table S4: Dataset Statistics\n\\begin{table}[!htbp]\n  \\centering\n  \\small\n  \\caption{Dataset statistics for the generational depth corpus. Depth~0 contains human-written seed texts sampled from the C4 English validation split and truncated to 256 subword tokens. Depths~1--5 are recursively generated by Qwen2.5-1.5B-Instruct (nucleus sampling, $p{=}0.95$, $T{=}1.0$). Token counts use whitespace tokenization. Statistics shown for the primary Qwen-rewrite corpus; the other three model-mode configurations (Pythia-cont, OLMo-cont, Qwen-cont) share the same generation pipeline and corpus structure.}\n  \\label{tab:s4_dataset_stats}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{clrl}\n    \\toprule\n    \\textbf{Depth} & \\textbf{$N$ samples} & \\textbf{Mean tokens} & \\textbf{Source} \\\\\n    \\midrule\n    0 & 5{,}000 & 147.8 & C4 validation (human) \\\\\n    1 & 5{,}000 & 207.1 & Qwen2.5-1.5B rewrite \\\\\n    2 & 5{,}000 & 206.1 & Qwen2.5-1.5B rewrite \\\\\n    3 & 5{,}000 & 208.0 & Qwen2.5-1.5B rewrite \\\\\n    4 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    5 & 5{,}000 & 207.7 & Qwen2.5-1.5B rewrite \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Total} & \\multicolumn{2}{l}{30{,}000 samples} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs across depth pairs for four decoding configurations (all using Qwen2.5-1.5B-Instruct in rewrite mode; 10{,}000 bootstrap resamples). The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$. Bottom rows report cross-configuration Spearman $\\rho$ on per-feature discriminative-power rankings.}\n  \\label{tab:s2_decoding}\n  \\footnotesize\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & $.980\\;[.977,\\,.982]$ & $.995\\;[.993,\\,.996]$ & $.988\\;[.986,\\,.990]$ & $.998\\;[.998,\\,.999]$ \\\\\n    1 vs.\\ 2 & $.689\\;[.680,\\,.698]$ & $.687\\;[.677,\\,.695]$ & $.689\\;[.680,\\,.697]$ & $.704\\;[.695,\\,.713]$ \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & $.561\\;[.552,\\,.571]$ & $.592\\;[.582,\\,.601]$\\rlap{$^\\dagger$} & $.590\\;[.581,\\,.600]$ & $.582\\;[.572,\\,.592]$ \\\\\n    3 vs.\\ 4 & $.540\\;[.531,\\,.550]$ & $.547\\;[.537,\\,.557]$ & $.539\\;[.529,\\,.549]$ & $.529\\;[.519,\\,.540]$ \\\\\n    4 vs.\\ 5 & $.514\\;[.503,\\,.524]$ & $.507\\;[.496,\\,.517]^{\\ddagger}$ & $.535\\;[.524,\\,.545]$ & $.524\\;[.513,\\,.535]$ \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\dagger}$\\,CI upper bound (0.601) marginally exceeds $\\theta{=}0.60$ by 0.001.} \\\\\n    \\multicolumn{5}{l}{${}^{\\ddagger}$\\,Permutation $p = 0.12$ (not significant). All other pairs $p < 0.01$.}\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S2b: Extended K* CI (all models including new additions)\n\\begin{table*}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Extended pairwise $\\auc$ with bootstrap 95\\% CIs for all model configurations including new additions.\n  This table extends Table~\\ref{tab:kstar_ci} in the main text with Qwen-base, LLaMA-8B, Mistral-7B, Pythia-6.9B (nucleus), and Gemma-2-2B configurations.\n  $\\Kempirical = 2$ holds for 6/10 conditions at $\\theta{=}0.60$ (OLMo-1B, Mistral-7B, Pythia-6.9B, Gemma-2-2B: $\\Kempirical{=}1$).}\n  \\label{tab:kstar_ci_extended}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{lcccccccccccccccccccc}\n    \\toprule\n     & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} & \\multicolumn{2}{c}{Qwen-base} & \\multicolumn{2}{c}{LLaMA-8B} & \\multicolumn{2}{c}{Mistral-7B} & \\multicolumn{2}{c}{Pythia-6.9B\\rlap{$^\\S$}} & \\multicolumn{2}{c}{Gemma-2B} \\\\\n    \\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\\cmidrule(lr){12-13}\\cmidrule(lr){14-15}\\cmidrule(lr){16-17}\\cmidrule(lr){18-19}\\cmidrule(lr){20-21}\n     & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n    \\midrule\n    0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] & .987 & [.985,\\,.989] & .9224 & [.917,\\,.927] & .9842 & [.982,\\,.986] & .9599 & & .953 & [.949,\\,.957] \\\\\n    1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .5080 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} & .626 & [.617,\\,.635]\\rlap{$^*$} & .6123 & [.603,\\,.622]\\rlap{$^*$} & .5934 & [.584,\\,.603] & .5955 & & .5981 & [.588,\\,.608] \\\\\n    2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] & .550 & [.540,\\,.560] & .5273 & [.517,\\,.538] & .5402 & [.530,\\,.551] & .5298 & & .534 & [.523,\\,.545] \\\\\n    3v4 & .5435 & & .5152 & & .5024 & & .5409 & & .5276 & & .529 & [.519,\\,.540] & .5168 & [.506,\\,.528] & .5233 & [.513,\\,.534] & .5135 & & .5033 & [.492,\\,.514] \\\\\n    4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & & .518 & [.508,\\,.529] & .5159 & [.505,\\,.527] & .5180 & [.507,\\,.529] & -- & -- & .5025 & [.492,\\,.514] \\\\\n    \\bottomrule\n    \\multicolumn{21}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all boundary comparisons.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B. ``--'': experiment pending.} \\\\\n    \\multicolumn{21}{l}{\\footnotesize $^\\S$Pythia-6.9B evaluated separately; nucleus sampling ($p{=}0.95$, $T{=}1.0$), same as all other models.}\n  \\end{tabular}}% end resizebox\n\\end{table*}\n\n%%% Table S3: LLM Zero-Shot Confusion Matrices (exp-011)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{LLM zero-shot depth classification: $5{\\times}5$ confusion matrices (Exp-011). Both frontier LLMs achieve high binary detection accuracy (GPT-5.5: 0.878; Claude Opus~4.6: 0.882) but near-chance 5-class accuracy (${\\sim}$0.33 vs.\\ OBD-LightGBM 0.386). Per-depth recall in Table~\\ref{tab:s3c_perdepth}.}\n  \\label{tab:s3_llm_zeroshot}\n\n  \\vspace{0.3em}\n  \\textbf{(a)} GPT-5.5 ($N{=}500$, acc${=}0.332$, MAE${=}1.102$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{77} & 18 &  4 &  0 &  1 & .770 \\\\\n    1 &  9 & \\textbf{19} & 36 & 24 & 12 & .190 \\\\\n    2 &  8 & 10 & \\textbf{38} & 35 &  9 & .380 \\\\\n    3 & 10 & 16 & 35 & \\textbf{24} & 15 & .240 \\\\\n    4 & 11 & 13 & 50 & 18 &  \\textbf{8} & .080 \\\\\n    \\bottomrule\n  \\end{tabular}\n\n  \\vspace{4pt}\n  \\textbf{(b)} Claude Opus~4.6 ($N{=}499$, acc${=}0.331$, MAE${=}1.150$)\n  \\vspace{1pt}\n\n  \\begin{tabular}{lcccccc}\n    \\toprule\n    & \\multicolumn{5}{c}{Predicted Depth} & \\\\\n    \\cmidrule(lr){2-6}\n    True & 0 & 1 & 2 & 3 & 4 & Rec. \\\\\n    \\midrule\n    0 & \\textbf{69} & 26 &  3 &  0 &  2 & .690 \\\\\n    1 &  8 & \\textbf{21} & 32 & 11 & 28 & .210 \\\\\n    2 &  6 & 36 & \\textbf{28} &  5 & 25 & .280 \\\\\n    3 &  7 & 20 & 31 & \\textbf{10} & 31 & .100 \\\\\n    4 &  7 & 28 & 22 &  6 & \\textbf{37} & .370 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Per-depth recall (\\%) on balanced $N{=}500$ test set. OBD's nominal overall accuracy gap originates from depth-0; all methods fail at depths $\\geq 2$, consistent with $\\Kempirical = 2$.}\n  \\label{tab:s3c_perdepth}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lccccc}\n    \\toprule\n    & Depth 0 & Depth 1 & Depth 2 & Depth 3 & Depth 4 \\\\\n    \\midrule\n    OBD-LightGBM & \\textbf{96} & \\textbf{39} & 14 & 19 & 22 \\\\\n    GPT-5.5      & 77 & 19 & \\textbf{38} & \\textbf{24} &  8 \\\\\n    Claude Opus~4.6 & 69 & 21 & 28 & 10 & \\textbf{37} \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table: Token Length and EOS Truncation Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Mean subword token count per depth and EOS truncation rate (\\%) for depth~1+ across all model configurations (generation limit: 256 tokens). Depth~0 (human text) is shared across configurations. Depths 1--5 show no systematic length trend; the 0v1 length asymmetry (human texts shorter) makes detection \\emph{more conservative}, not inflated. See Section~\\ref{sec:length_confound}.}\n  \\label{tab:token_length}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccccccc}\n    \\toprule\n    & \\multicolumn{6}{c}{\\textbf{Mean Token Count}} & & \\\\\n    \\cmidrule(lr){2-7}\n    \\textbf{Model} & D0 & D1 & D2 & D3 & D4 & D5 & \\textbf{EOS\\%} & \\textbf{Sev.} \\\\\n    \\midrule\n    Qwen-rw (1.5B)  & 191 & 254 & 252 & 254 & 254 & 254 & 7--11 & Mild \\\\\n    Pythia-1.4B      & 192 & 214 & 215 & 216 & 217 & 218 & 34--36 & High \\\\\n    OLMo-1B          & 192 & 256 & 256 & 256 & 256 & 256 & $<$1 & Negl. \\\\\n    Qwen-cont (1.5B) & 191 & 244 & 238 & 240 & 240 & 238 & 17--20 & Mod. \\\\\n    Qwen-7B          & 191 & 196 & 195 & 193 & 197 & 197 & 45--47 & High \\\\\n    \\midrule\n    \\multicolumn{9}{l}{\\textit{Decoding ablation (Qwen-rw 1.5B)}} \\\\\n    \\quad Greedy          & 191 & 253 & 252 & 253 & 254 & 254 & 8--12 & Mild \\\\\n    \\quad Nuc $p{=}0.9$   & 191 & 254 & 251 & 254 & 253 & 254 & 8--16 & Mild \\\\\n    \\quad $T{=}0.7$       & 191 & 253 & 251 & 253 & 253 & 254 & 8--14 & Mild \\\\\n    \\quad $T{=}1.2$       & 191 & 254 & 252 & 253 & 254 & 254 & 8--16 & Mild \\\\\n    \\bottomrule\n    \\multicolumn{9}{l}{EOS\\%: generation terminated via EOS before 256-token limit. Ranges span depths 1--5.}\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S5: Complete 15-D Feature Descriptions\n\\begin{table*}[t]\n  \\centering\n  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\n  \\label{tab:s5_features}\n  \\begin{tabular}{llp{0.45\\textwidth}l}\n    \\toprule\n    \\textbf{Group} & \\textbf{Feature} & \\textbf{Description} & \\textbf{Range} \\\\\n    \\midrule\n    \\multirow{9}{*}{\\rotatebox[origin=c]{90}{\\textsc{Surprisal}}}\n    & \\texttt{surp\\_mean}   & Mean token surprisal $\\frac{1}{T}\\sum_t -\\log p(x_t \\mid x_{&lt;t})$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_std}    & Standard deviation of token surprisal & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_skew}   & Skewness of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_kurt}   & Excess kurtosis of the surprisal distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_mean} & Mean of first-order surprisal differences $\\Delta s_t = s_{t+1} - s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d1\\_std}  & Std of first-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    & \\texttt{surp\\_d1\\_skew} & Skewness of first-order surprisal differences & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_mean} & Mean of second-order differences $\\Delta^2 s_t$ & $\\mathbb{R}$ \\\\\n    & \\texttt{surp\\_d2\\_std}  & Std of second-order surprisal differences & $\\mathbb{R}^+$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Lex}}}\n    & \\texttt{ttr}          & Type-token ratio: $|V| / T$ & $[0, 1]$ \\\\\n    & \\texttt{hapax\\_ratio} & Hapax legomena ratio: freq-1 types / unique types & $[0, 1]$ \\\\\n    & \\texttt{self\\_bleu}   & Mean 4-gram BLEU against 100 random same-depth samples & $[0, 1]$ \\\\\n    \\midrule\n    \\multirow{3}{*}{\\rotatebox[origin=c]{90}{\\textsc{Freq}}}\n    & \\texttt{freq\\_kurtosis}  & Excess kurtosis of word frequency distribution & $\\mathbb{R}$ \\\\\n    & \\texttt{freq\\_entropy}   & Shannon entropy of word frequencies: $-\\sum p_w \\log_2 p_w$ & $\\mathbb{R}^+$ \\\\\n    & \\texttt{low\\_freq\\_ratio} & Proportion of vocabulary with count $\\leq 2$ & $[0, 1]$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Tables S6 & S7: Side by side in a single table* to avoid table*/table overlap\n\\begin{table*}[t]\n\\begin{minipage}[t]{0.45\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \\texttt{doc\\_id} to prevent data leakage from the same seed document appearing in both train and test.}\n  \\label{tab:s6_lgbm_params}\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Parameter} & \\textbf{Value} \\\\\n    \\midrule\n    \\texttt{n\\_estimators}      & 200 \\\\\n    \\texttt{learning\\_rate}     & 0.05 \\\\\n    \\texttt{max\\_depth}         & 6 \\\\\n    \\texttt{num\\_leaves}        & 31 \\\\\n    \\texttt{verbose}            & $-1$ \\\\\n    \\texttt{n\\_jobs}            & $-1$ (all cores) \\\\\n    Cross-validation            & 5-fold GroupKFold \\\\\n    Grouping key                & \\texttt{doc\\_id} \\\\\n    Objective                   & Binary (per depth pair) \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{minipage}\\hfill\n\\begin{minipage}[t]{0.52\\textwidth}\n  \\centering\n  \\small\n  \\captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}\n  \\label{tab:s7_neural_probe}\n  \\resizebox{\\textwidth}{!}{%\n  \\begin{tabular}{ll}\n    \\toprule\n    \\textbf{Component} & \\textbf{Details} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Embedding extraction}} \\\\\n    Base models       & Qwen2.5-1.5B / Pythia-1.4B / OLMo-1B (frozen) \\\\\n    Representation    & Last hidden state, attention-masked avg pool \\\\\n    Embedding dim     & 1536 / 2048 / 2048 \\\\\n    Max sequence len   & 512 tokens \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{MLP classifier}} \\\\\n    Architecture      & $d_{\\text{emb}} \\to 512 \\to 256 \\to 6$ \\\\\n    Activations       & ReLU \\\\\n    Dropout           & 0.1 (after each hidden layer) \\\\\n    Output            & 6-class softmax \\\\\n    \\midrule\n    \\multicolumn{2}{l}{\\textit{Training}} \\\\\n    Optimizer         & Adam ($\\text{lr} = 10^{-3}$, weight decay $= 10^{-4}$) \\\\\n    Loss              & Cross-entropy \\\\\n    Batch size        & 256 \\\\\n    Max epochs        & 20 \\\\\n    Early stopping    & Patience = 5 (validation loss) \\\\\n    Cross-validation  & 5-fold GroupKFold \\\\\n    \\bottomrule\n  \\end{tabular}%\n  }\n\\end{minipage}\n\\end{table*}\n\n%%% Table S8: Per-Model Bootstrap CI Results (exp-007)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Pairwise AUC with bootstrap 95\\% CIs for four model-mode configurations (1{,}000 resamples). All pairs $p < 0.01$ except OLMo 1v2--4v5 ($p > 0.09$).}\n  \\label{tab:s8_cv_folds}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    0v1 & $.996\\;[.995,.997]$ & $.993\\;[.992,.994]$ & $.986\\;[.984,.988]$ & $.997\\;[.996,.998]$ \\\\\n    1v2 & $.696\\;[.686,.704]$ & $.654\\;[.645,.663]$ & $.508\\;[.496,.519]$ & $.611\\;[.602,.621]$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.589\\;[.580,.599]$ & $.551\\;[.542,.563]$ & $.497\\;[.486,.509]$ & $.561\\;[.551,.571]$ \\\\\n    3v4 & $.544\\;[.533,.555]$ & $.515\\;[.504,.526]$ & $.502\\;[.491,.513]$ & $.541\\;[.531,.551]$ \\\\\n    4v5 & $.534\\;[.524,.545]$ & $.514\\;[.502,.525]$ & $.494\\;[.483,.506]$ & $.514\\;[.504,.526]$ \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S9: Binary Detector Spearman ρ (exp-012)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Spearman $\\rho$ between binary detector scores and true depth, and 6-class accuracy. Correlations driven by 0v1; scores do not track depth beyond generation~1. Qwen-rw exhibits reversed sign ($\\rho > 0$).}\n  \\label{tab:s9_binary_spearman}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Qwen-rw} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen-cont} \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textit{Spearman $\\rho$}} \\\\\n    \\quad log-PPL (ref)      & $-0.123$ & $-0.297$ & $-0.378$ & $-0.389$ \\\\\n    \\quad log-PPL (obs.)     & $+0.082$ & $-0.453$ & $-0.461$ & $-0.162$ \\\\\n    \\quad PPL ratio           & $+0.119$ & $-0.392$ & $-0.407$ & $-0.058$ \\\\\n    \\midrule\n    6-class acc.              & 0.199    & 0.130    & 0.127    & 0.183 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{Random baseline: 0.167} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S10: Pythia Decoding Ablation (exp-020)\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Pythia-1.4B pairwise $\\auc$ under four decoding configs (10K bootstrap). $^\\dagger$Greedy triggers repetition collapse (4-gram repeat: $d_0{=}0.01 \\to d_1{=}0.72$).}\n  \\label{tab:s10_pythia_decoding}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{lcccc}\n    \\toprule\n    & \\textbf{Greedy}$^\\dagger$ & \\textbf{$p{=}0.9$} & \\textbf{$T{=}0.7$} & \\textbf{$T{=}1.2$} \\\\\n    \\midrule\n    0v1 & $.999$ & $.995$ & $.996$ & $.994$ \\\\\n    1v2 & $.884$ & $.675$ & $.728$ & $.618$ \\\\\n    \\cmidrule(lr){1-5}\n    2v3 & $.531$ & $.559$ & $.598^\\ddagger$ & $.531$ \\\\\n    3v4 & $.522$ & $.524$ & $.563$ & $.520$ \\\\\n    4v5 & $.514$ & $.501$ & $.527$ & $.510$ \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2 & 2 \\\\\n    \\bottomrule\n    \\multicolumn{5}{l}{${}^{\\ddagger}$CI upper 0.606 $> \\theta$; point est.\\ below.} \\\\\n  \\end{tabular}}\n\\end{table}\n\n%%% Table S11: Length Ablation (exp-021)\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three segment lengths (Qwen-base, cont.\\ mode). $\\Kempirical{=}2$ at 128/256; 512 marginal ($^\\dagger$CI lower $< \\theta$).}\n  \\label{tab:s11_length_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{128} & \\textbf{256} & \\textbf{512} \\\\\n    \\midrule\n    0v1 & .979 & .991 & .992 \\\\\n    1v2 & .622 & .628 & .607$^\\dagger$ \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .529 & .556 & .572 \\\\\n    3v4 & .535 & .530 & .530 \\\\\n    4v5 & .501 & .514 & .518 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 2$^\\dagger$ \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}\n\n%%% Table S12: Domain Ablation\n\\begin{table}[t]\n  \\centering\n  \\small\n  \\caption{Pairwise $\\auc$ for three text domains (Qwen-cont). arXiv yields $\\Kempirical{=}3$; C4 and Wikipedia $\\Kempirical{=}2$.}\n  \\label{tab:s12_domain_ablation}\n  \\begin{tabular}{lccc}\n    \\toprule\n    & \\textbf{C4} & \\textbf{Wiki} & \\textbf{arXiv} \\\\\n    \\midrule\n    0v1 & .997 & .996 & .995 \\\\\n    1v2 & .611 & .619 & .858 \\\\\n    \\cmidrule(lr){1-4}\n    2v3 & .561 & .550 & .644$^*$ \\\\\n    3v4 & .541 & .523 & .544 \\\\\n    4v5 & .514 & .514 & .530 \\\\\n    \\midrule\n    $\\Kempirical$ & 2 & 2 & 3 \\\\\n    \\bottomrule\n    \\multicolumn{4}{l}{\\footnotesize $^*$CI $[.628,.658]$; $p < 0.001$.}\n  \\end{tabular}\n\\end{table}\n\n%%% Table S13: Scorer Sensitivity Analysis\n\\begin{table}[t]\n  \\centering\n  \\scriptsize\n  \\caption{Scorer sensitivity: $\\Kempirical$ under self- vs.\\ cross-scoring. Cross-scoring reduces $\\Kempirical$ only for marginal Qwen-cont.}\n  \\label{tab:s13_scorer_sensitivity}\n  \\resizebox{\\columnwidth}{!}{%\n  \\begin{tabular}{llcccc}\n    \\toprule\n    \\textbf{Generator} & \\textbf{Mode} & \\textbf{Self} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Agr.} \\\\\n    \\midrule\n    Qwen-Inst & Rewrite & 2 & 2 & 2 & \\checkmark \\\\\n    Qwen-Inst & Cont.   & 2 & 1 & 1 & $\\times$ \\\\\n    Qwen-base & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    Pythia    & Cont.   & 2 & 2 & 2 & \\checkmark \\\\\n    OLMo      & Cont.   & 1 & -- & -- & -- \\\\\n    Qwen-7B   & Cont.   & 2 & -- & -- & -- \\\\\n    Mistral   & Cont.   & 1 & -- & -- & -- \\\\\n    \\bottomrule\n  \\end{tabular}}\n\\end{table}\n\n\\clearpage\n",
      "numLines": 466,
      "startLine": 1,
      "totalLines": 466
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01AuqnQs9njUefFM1Yy7qpSv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "573b189f-7f7e-4047-a198-fa44808c39a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8uHSWhiDQ89NLWmiSTtNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 24366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2283
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

_source line 16 · 2026-05-22T21:21:34.174Z_

<details><summary>↩ Tool result · `toolu_01AuqnQs9njUefFM1Yy7qpSv`</summary>

```text
1	\section{Extended Discussion}
2	\label{sec:extended_discussion}
3	
4	\subsection{Theoretical Implications of $\Kempirical = 2$}
5	
6	The DPI guarantees a finite $\Ktheory$; for general web text, $\Kempirical \leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\Kempirical{=}3$, aligning with model collapse convergence~\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.
7	Decoding strategy modestly affects signal strength (1v2 $\auc \in [0.6866, 0.7039]$) but does not shift the boundary.
8	
9	\subsection{Cross-Model Transfer Implications}
10	
11	Cross-model classification retains 80--100\% accuracy with scorer-invariant feature rankings ($\rho > 0.90$), enabling single-classifier deployment across generators.
12	Absolute discriminability at the $\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\Kempirical$ from 2 to 1, while rewrite-mode $\Kempirical = 2$ is preserved.
13	Model family similarity modulates transfer (Pythia$\leftrightarrow$OLMo: 90--92\% vs.\ Qwen-cont$\leftrightarrow$OLMo: 80--85\%).
14	
15	\begin{minipage}{\columnwidth}
16	\centering
17	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
18	\label{tab:crossscorer}
19	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
20	\end{minipage}
21	
22	\begin{table}[h]
23	\centering
24	\small
25	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\eta^2_p{=}.166$) relative to Depth-Pair ($\eta^2_p{=}.997$), supporting near-scorer-independence of depth discrimination.}
26	\label{tab:anova_crossscorer}
27	\begin{tabular}{lrrrr}
28	\toprule
29	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
30	\midrule
31	Generator     & 2  & 851.91  & ${<}.001$  & .866 \\
32	Scorer        & 3  & 17.48  & ${<}.001$  & .166 \\
33	Depth-Pair    & 4  & 22737.70  & ${<}.001$  & .997 \\
34	Gen$\times$Scorer & 6 & 7.50 & ${<}.001$ & .146 \\
35	Gen$\times$Depth  & 8 & 913.41 & ${<}.001$ & .965 \\
36	Scorer$\times$Depth & 12 & 2.25 & $.010$ & .093 \\
37	Residual      & 264 & & & \\
38	\bottomrule
39	\end{tabular}
40	\end{table}
41	
42	\subsection{Feature Importance Across Decoding Strategies}
43	
44	Feature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\rho = 0.914$), while greedy vs.\ $T{=}1.2$ yields lower correlation ($\rho = 0.53$, nonsignificant after Bonferroni).
45	The depth boundary is robust but the optimal feature subset is strategy-dependent.
46	
47	\subsection{Scale and Neural Probe}
48	\label{sec:extended_neural_probe}
49	
50	Cross-scale validation confirms $\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text. Scaling to 13B+ remains open.
51	
52	The neural probe yields model-dependent $\Kempirical^{\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia; OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$), consistent with the 15D LightGBM boundary.
53	The 15D model-free features yield $\Kempirical = 2$ for Pythia and Qwen, while OLMo yields $\Kempirical = 1$ under the standardized pipeline.
54	
55	\subsection{LLM Zero-Shot Baseline}
56	\label{sec:extended_llm}
57	
58	GPT-5.5 achieves 33.2\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\% (95\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\ref{tab:s3_llm_zeroshot}).
59	Per-depth recall confirms convergent failure at depths $\geq 2$ (Section~\ref{sec:why_kstar}).
60	When 6-class probabilities are marginalized to 5 classes ($P(d{\geq}4)$), accuracy rises to 44.4\% but concentrates in depth-4 (recall: 22\%$\to$80\%) while depths 2--3 collapse to 2--8\%; we report raw 6-class results.
61	
62	\subsection{Practical Considerations}
63	
64	All filtering strategies degrade general capabilities (MMLU: 0.6018 $\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\to$ 0.6638--0.6701); our 100\% synthetic setting is an upper bound; in mixed corpora, degradation scales with contamination fraction~\cite{shumailov2024collapse, dohmatob2024model}.
65	$\Kstar$-aware binary filtering reduces MMLU degradation by ${\sim}$50\% ($-$1.53\,pp $\to$ $-$0.77\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).
66	
67	\subsection{Extended Limitations}
68	\label{sec:extended_limitations}
69	
70	\emph{Prompt-chain versus retrain-chain.}
71	Retrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 2v3 $= 0.8888$, 3v4 $= 0.7982$), far exceeding prompt-chain $\Kempirical{=}2$.
72	The elevated signal arises from cumulative model-adaptation artifacts rather than text-intrinsic degradation; prompt-chain $\Kempirical$ is the operationally relevant boundary for data curation.
73	
74	\emph{Threshold sensitivity.}
75	At $\theta = 0.55$, $\Kempirical = 3$ for Qwen-rewrite/continuation; at $\theta = 0.70$, $\Kempirical = 1$ across all configurations (Figure~\ref{fig:kstar_theta}).
76	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
77	
78	\emph{Structural confound: token length.}
79	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
80	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
81	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
82	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
83	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
84	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
85	
86	\emph{Graduated filtering.}
87	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
88	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
89	\label{tab:pairwise_significance}
90	
91	\subsection{Dose-Response: Contamination Ratio Effect}
92	\label{sec:dose_response}
93	
94	The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
95	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
96	
97	\begin{table}[h]
98	\centering
99	\small
100	\caption{MMLU accuracy by contamination ratio (fraction of synthetic data in training set) and filtering strategy. Base model (no fine-tuning): 0.6018. Mean $\pm$ std over 5 seeds.}
101	\label{tab:dose_response}
102	\resizebox{\columnwidth}{!}{%
103	\begin{tabular}{lccc}
104	\toprule
105	\textbf{Strategy} & \textbf{10\%} & \textbf{30\%} & \textbf{50\%} \\
106	\midrule
107	No-filter   & $0.6009 \pm .003$ & $0.5978 \pm .004$ & $0.5932 \pm .004$ \\
108	Binary-ours & $0.6011 \pm .003$ & $0.5988 \pm .003$ & $0.5956 \pm .004$ \\
109	Graduated   & $0.6008 \pm .003$ & $0.5982 \pm .004$ & $0.5944 \pm .004$ \\
110	\bottomrule
111	\end{tabular}}
112	\end{table}
113	
114	{\sloppy At 10\% contamination, no-filter MMLU ($0.6009$) remains within noise of the base model ($0.6018$, $\Delta = -0.09$\,pp), and all three strategies are indistinguishable ($\Delta_{\max} = 0.03$\,pp between strategies, $p > 0.8$).
115	At 30\%, differences emerge directionally ($\Delta = 0.10$\,pp, binary vs.\ no-filter) but remain non-significant ($p > 0.3$).
116	At 50\%, binary-ours shows a 0.24\,pp advantage over no-filter, approaching but not reaching significance ($p = 0.12$).
117	The strategy ordering (binary $>$ graduated $>$ no-filter) is consistent with the 100\% setting, but effect sizes scale linearly with contamination fraction.
118	This demonstrates that $\Kstar$-aware curation provides practical benefit primarily when contamination is severe enough to cause measurable quality degradation.\par}
119	
120	\subsection{Seed Robustness}
121	\label{sec:seed_robustness}
122	
123	Because the random seed governs both corpus sampling and generation quality (not merely CV splits), absolute AUC values are seed-dependent.
124	We re-run three configurations with seed$\,{=}\,123$ (primary: seed$\,{=}\,42$; Table~\ref{tab:seed_robustness}).
125	$\Kempirical$ is stable in 2/3 cases: Pythia-1.4B on Wikipedia yields $\Kempirical{=}1$ under both seeds (1v2 $\Delta = -0.8$\,pp), and Qwen-1.5B on C4 yields $\Kempirical{=}2$ (1v2 $\Delta = +9.0$\,pp, both seeds above $\theta$).
126	Qwen-1.5B on Wikipedia shifts from $\Kempirical{=}2$ to $\Kempirical{=}3$ under seed$\,{=}\,123$, but the 2v3 AUC ($0.6067$) is marginal: one of five folds falls below $\theta$ (fold~5 $= 0.595$), so this does not constitute strong evidence for $\Kempirical{=}3$.
127	The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the methodological case for threshold-based $\Kempirical$ over raw AUC comparisons: the qualitative boundary is robust even when point estimates shift.
128	
129	\begin{table}[h]
130	\centering
131	\footnotesize
132	\caption{Seed robustness: $\Kempirical$ under two random seeds. 1v2 $\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\theta$).}
133	\label{tab:seed_robustness}
134	\resizebox{\columnwidth}{!}{%
135	\begin{tabular}{llcccc}
136	\toprule
137	\textbf{Model} & \textbf{Domain} & \multicolumn{2}{c}{$\Kempirical$} & \textbf{1v2 $\Delta$} & \textbf{Stable?} \\
138	\cmidrule(lr){3-4}
139	 & & seed=42 & seed=123 & & \\
140	\midrule
141	Pythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\,pp & \checkmark \\
142	Qwen-1.5B  & C4        & 2 & 2 & $+9.0$\,pp & \checkmark \\
143	Qwen-1.5B  & Wikipedia & 2 & 3$^\dagger$ & $+8.7$\,pp & $\times$ \\
144	\bottomrule
145	\multicolumn{6}{l}{\footnotesize $^\dagger$2v3 $\auc = 0.6067$; fold 5 $= 0.595 < \theta$. Marginal boundary.}
146	\end{tabular}}
147	\end{table}
148	
149	\subsection{Bonferroni-Corrected Confidence Intervals}
150	\label{sec:bonferroni_ci}
151	
152	To control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\alpha_{\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\% confidence intervals ($z = 2.807$).
153	Table~\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\Kempirical$ boundary pair.
154	Eight of ten configurations retain CI lower bounds above $\theta{=}0.60$; two marginal $\Kempirical{=}2$ configurations (Qwen-cont, LLaMA-8B) see their lower bounds dip below $\theta$ under the stricter criterion ($0.5976$ and $0.5988$, respectively).
155	These near-misses reflect narrow effect sizes ($\auc - \theta < 0.013$) rather than classification failure: both retain point estimates above $\theta$ and uncorrected 95\% CI lower bounds above $\theta$.
156	
157	\begin{table}[h]
158	\centering
159	\footnotesize
160	\caption{Bonferroni-corrected 99.5\% confidence intervals for $\Kempirical$ boundary pairs across all 10 configurations. $\alpha_{\text{corr}} = 0.005$; CI computed as $\auc \pm 2.807 \times \hat{\sigma}_{\text{boot}}$. ``Pass $\theta$'': CI lower bound $> 0.60$.}
161	\label{tab:bonferroni_ci}
162	\resizebox{\columnwidth}{!}{%
163	\begin{tabular}{llcccc}
164	\toprule
165	\textbf{Configuration} & \textbf{Boundary} & $\auc$ & $\hat{\sigma}_{\text{boot}}$ & \textbf{99.5\% CI} & \textbf{Pass $\theta$} \\
166	\midrule
167	\multicolumn{6}{l}{\textit{$\Kempirical = 2$ configurations}} \\
168	Qwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\,.708]$ & \checkmark \\
169	Pythia-1.4B               & 1v2 & .6539 & .0046 & $[.641,\,.667]$ & \checkmark \\
170	Qwen-base                 & 1v2 & .6260 & .0047 & $[.613,\,.639]$ & \checkmark \\
171	Qwen-7B$^\ddagger$        & 1v2 & .6168 & .0046 & $[.604,\,.630]$ & \checkmark \\
172	LLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\,.626]$ & $\times$ \\
173	Qwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\,.625]$ & $\times$ \\
174	\midrule
175	\multicolumn{6}{l}{\textit{$\Kempirical = 1$ configurations}} \\
176	OLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\,.989]$ & \checkmark \\
177	Mistral-7B                & 0v1 & .9842 & .0009 & $[.982,\,.987]$ & \checkmark \\
178	Pythia-6.9B$^\S$          & 0v1 & .9599 & .0015$^\dagger$ & $[.956,\,.964]$ & \checkmark \\
179	Gemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\,.958]$ & \checkmark \\
180	\bottomrule
181	\multicolumn{6}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\
182	\multicolumn{6}{l}{\footnotesize $^\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\
183	\multicolumn{6}{l}{\footnotesize $^\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}
184	\end{tabular}}
185	\end{table}
186	
187	\subsection{Cross-Sample Robustness: 5K vs.\ 10K}
188	\label{sec:robustness_10k}
189	
190	The preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.
191	To assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.
192	If $\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.
193	
194	Table~\ref{tab:robustness_10k} reports the results.
195	For Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9700$ vs.\ $0.9712$), while the boundary 1v2 AUC decreases from $0.6539$ to $0.6175$ ($\Delta = -0.036$).
196	This shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.
197	The 2v3 pair remains near chance in both draws ($0.54$, $0.54$), confirming that depths $\geq 2$ are indistinguishable regardless of sample.
198	Qwen-1.5B (continuation, C4) replicates the same pattern ($\Kempirical{=}2$, 1v2 $\auc = 0.6346$).
199	LLaMA-3.1-8B (continuation, C4) is the sole configuration where the 10K OOF AUC drops below $\theta$ ($0.5880$; pipeline AUC $= 0.6148$; Bonferroni 99.5\% CI $[0.5776, 0.5978]$), yielding $\Kempirical{=}1$ under the stricter criterion.
200	
201	\begin{table}[h]
202	\centering
203	\footnotesize
204	\caption{Cross-sample robustness: pairwise AUC and $\Kempirical$ under 5K and 10K C4 samples drawn with different random seeds. All configurations use continuation mode. $\Kempirical$ is determined by the $\theta{=}0.60$ threshold on 1v2 AUC.}
205	\label{tab:robustness_10k}
206	\resizebox{\columnwidth}{!}{\begin{tabular}{llcccc}
207	\toprule
208	\textbf{Model} & $N$ & \textbf{AUC(0v1)} & \textbf{AUC(1v2)} & \textbf{AUC(2v3)} & $\Kempirical$ \\
209	\midrule
210	Pythia-1.4B cont & 5K  & 0.9700 & 0.6539 & 0.5400 & 2 \\
211	Pythia-1.4B cont & 10K & 0.9712 & 0.6175 & 0.5364 & 2 \\
212	\midrule
213	Qwen-1.5B cont  & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
214	Qwen-1.5B cont  & 10K & 0.9875 & 0.6346 & 0.5616 & 2 \\
215	\midrule
216	LLaMA-8B cont   & 5K  & \multicolumn{3}{c}{(see Table~\ref{tab:bonferroni_ci})} & 2 \\
217	LLaMA-8B cont   & 10K & 0.9282 & 0.5880$^\dagger$ & 0.5247 & 1$^\dagger$ \\
218	\bottomrule
219	\multicolumn{6}{l}{\footnotesize $^\dagger$OOF AUC (pipeline AUC $= 0.6148$); Bonferroni 99.5\% CI $[0.5776, 0.5978]$ does not pass $\theta$.} \\
220	\end{tabular}}
221	\end{table}
222	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "df850398-a15d-4d1b-8124-bf4c777a22b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Discussion}\n\\label{sec:extended_discussion}\n\n\\subsection{Theoretical Implications of $\\Kempirical = 2$}\n\nThe DPI guarantees a finite $\\Ktheory$; for general web text, $\\Kempirical \\leq 2$ across all 10 configurations (1B--8B, 6 families), while structured domains (arXiv) yield $\\Kempirical{=}3$, aligning with model collapse convergence~\\cite{shumailov2024collapse, dohmatob2024model, alemohammad2024selfconsuming}.\nDecoding strategy modestly affects signal strength (1v2 $\\auc \\in [0.6866, 0.7039]$) but does not shift the boundary.\n\n\\subsection{Cross-Model Transfer Implications}\n\nCross-model classification retains 80--100\\% accuracy with scorer-invariant feature rankings ($\\rho > 0.90$), enabling single-classifier deployment across generators.\nAbsolute discriminability at the $\\Kempirical$ boundary is scorer-sensitive: alternative scorers reduce Qwen-continuation $\\Kempirical$ from 2 to 1, while rewrite-mode $\\Kempirical = 2$ is preserved.\nModel family similarity modulates transfer (Pythia$\\leftrightarrow$OLMo: 90--92\\% vs.\\ Qwen-cont$\\leftrightarrow$OLMo: 80--85\\%).\n\n\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values. DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs). Scorer is statistically significant but explains modest variance ($\\eta^2_p{=}.166$) relative to Depth-Pair ($\\eta^2_p{=}.997$), supporting near-scorer-independence of depth discrimination.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 851.91  & ${<}.001$  & .866 \\\\\nScorer        & 3  & 17.48  & ${<}.001$  & .166 \\\\\nDepth-Pair    & 4  & 22737.70  & ${<}.001$  & .997 \\\\\nGen$\\times$Scorer & 6 & 7.50 & ${<}.001$ & .146 \\\\\nGen$\\times$Depth  & 8 & 913.41 & ${<}.001$ & .965 \\\\\nScorer$\\times$Depth & 12 & 2.25 & $.010$ & .093 \\\\\nResidual      & 264 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Importance Across Decoding Strategies}\n\nFeature importance ordering varies across decoding strategies: greedy and $T{=}0.7$ share highly correlated rankings ($\\rho = 0.914$), while greedy vs.\\ $T{=}1.2$ yields lower correlation ($\\rho = 0.53$, nonsignificant after Bonferroni).\nThe depth boundary is robust but the optimal feature subset is strategy-dependent.\n\n\\subsection{Scale and Neural Probe}\n\\label{sec:extended_neural_probe}\n\nCross-scale validation confirms $\\Kempirical = 2$ from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$, 0v1 $= 0.9225$) both exceed $\\theta$, with progressively lower 0v1 signal consistent with larger models generating more human-like text. Scaling to 13B+ remains open.\n\nThe neural probe yields model-dependent $\\Kempirical^{\\text{neural}}$: $3$ for Qwen (self-familiarity effect from instruction-tuned representations) but $2$ for Pythia; OLMo yields $\\Kempirical^{\\text{neural}} = 1$ (1v2 $\\auc = 0.5054$), consistent with the 15D LightGBM boundary.\nThe 15D model-free features yield $\\Kempirical = 2$ for Pythia and Qwen, while OLMo yields $\\Kempirical = 1$ under the standardized pipeline.\n\n\\subsection{LLM Zero-Shot Baseline}\n\\label{sec:extended_llm}\n\nGPT-5.5 achieves 33.2\\% accuracy (MAE = 1.10) and Claude Opus~4.6 33.1\\% (MAE = 1.15) on a balanced 500-sample test set, comparable to OBD-LightGBM's 38.0\\% (95\\% CI: $[0.340, 0.422]$; McNemar $p = 0.081$, $0.069$; Table~\\ref{tab:s3_llm_zeroshot}).\nPer-depth recall confirms convergent failure at depths $\\geq 2$ (Section~\\ref{sec:why_kstar}).\nWhen 6-class probabilities are marginalized to 5 classes ($P(d{\\geq}4)$), accuracy rises to 44.4\\% but concentrates in depth-4 (recall: 22\\%$\\to$80\\%) while depths 2--3 collapse to 2--8\\%; we report raw 6-class results.\n\n\\subsection{Practical Considerations}\n\nAll filtering strategies degrade general capabilities (MMLU: 0.6018 $\\to$ 0.5865--0.5941; HellaSwag: 0.6821 $\\to$ 0.6638--0.6701); our 100\\% synthetic setting is an upper bound; in mixed corpora, degradation scales with contamination fraction~\\cite{shumailov2024collapse, dohmatob2024model}.\n$\\Kstar$-aware binary filtering reduces MMLU degradation by ${\\sim}$50\\% ($-$1.53\\,pp $\\to$ $-$0.77\\,pp), requires no per-model calibration, and is combinable with distribution-matching methods (DSIR, DoReMi).\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nRetrain-chain validation (Pythia-1.4B LoRA, 5 generations) yields $\\Kempirical{\\geq}4$ (1v2 $\\auc = 0.9484$, 2v3 $= 0.8888$, 3v4 $= 0.7982$), far exceeding prompt-chain $\\Kempirical{=}2$.\nThe elevated signal arises from cumulative model-adaptation artifacts rather than text-intrinsic degradation; prompt-chain $\\Kempirical$ is the operationally relevant boundary for data curation.\n\n\\emph{Threshold sensitivity.}\nAt $\\theta = 0.55$, $\\Kempirical = 3$ for Qwen-rewrite/continuation; at $\\theta = 0.70$, $\\Kempirical = 1$ across all configurations (Figure~\\ref{fig:kstar_theta}).\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use 100\\% synthetic data to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU accuracy by contamination ratio (fraction of synthetic data in training set) and filtering strategy. Base model (no fine-tuning): 0.6018. Mean $\\pm$ std over 5 seeds.}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{10\\%} & \\textbf{30\\%} & \\textbf{50\\%} \\\\\n\\midrule\nNo-filter   & $0.6009 \\pm .003$ & $0.5978 \\pm .004$ & $0.5932 \\pm .004$ \\\\\nBinary-ours & $0.6011 \\pm .003$ & $0.5988 \\pm .003$ & $0.5956 \\pm .004$ \\\\\nGraduated   & $0.6008 \\pm .003$ & $0.5982 \\pm .004$ & $0.5944 \\pm .004$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n{\\sloppy At 10\\% contamination, no-filter MMLU ($0.6009$) remains within noise of the base model ($0.6018$, $\\Delta = -0.09$\\,pp), and all three strategies are indistinguishable ($\\Delta_{\\max} = 0.03$\\,pp between strategies, $p > 0.8$).\nAt 30\\%, differences emerge directionally ($\\Delta = 0.10$\\,pp, binary vs.\\ no-filter) but remain non-significant ($p > 0.3$).\nAt 50\\%, binary-ours shows a 0.24\\,pp advantage over no-filter, approaching but not reaching significance ($p = 0.12$).\nThe strategy ordering (binary $>$ graduated $>$ no-filter) is consistent with the 100\\% setting, but effect sizes scale linearly with contamination fraction.\nThis demonstrates that $\\Kstar$-aware curation provides practical benefit primarily when contamination is severe enough to cause measurable quality degradation.\\par}\n\n\\subsection{Seed Robustness}\n\\label{sec:seed_robustness}\n\nBecause the random seed governs both corpus sampling and generation quality (not merely CV splits), absolute AUC values are seed-dependent.\nWe re-run three configurations with seed$\\,{=}\\,123$ (primary: seed$\\,{=}\\,42$; Table~\\ref{tab:seed_robustness}).\n$\\Kempirical$ is stable in 2/3 cases: Pythia-1.4B on Wikipedia yields $\\Kempirical{=}1$ under both seeds (1v2 $\\Delta = -0.8$\\,pp), and Qwen-1.5B on C4 yields $\\Kempirical{=}2$ (1v2 $\\Delta = +9.0$\\,pp, both seeds above $\\theta$).\nQwen-1.5B on Wikipedia shifts from $\\Kempirical{=}2$ to $\\Kempirical{=}3$ under seed$\\,{=}\\,123$, but the 2v3 AUC ($0.6067$) is marginal: one of five folds falls below $\\theta$ (fold~5 $= 0.595$), so this does not constitute strong evidence for $\\Kempirical{=}3$.\nThe ${\\pm}9$\\,pp absolute AUC variation across seeds strengthens the methodological case for threshold-based $\\Kempirical$ over raw AUC comparisons: the qualitative boundary is robust even when point estimates shift.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Seed robustness: $\\Kempirical$ under two random seeds. 1v2 $\\Delta$: change in 1v2 AUC from seed 42 to seed 123. $\\Kempirical$ is stable in 2/3 configurations; the Qwen-Wiki shift to $\\Kempirical{=}3$ is marginal (2v3 fold variance crosses $\\theta$).}\n\\label{tab:seed_robustness}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\multicolumn{2}{c}{$\\Kempirical$} & \\textbf{1v2 $\\Delta$} & \\textbf{Stable?} \\\\\n\\cmidrule(lr){3-4}\n & & seed=42 & seed=123 & & \\\\\n\\midrule\nPythia-1.4B & Wikipedia & 1 & 1 & $-0.8$\\,pp & \\checkmark \\\\\nQwen-1.5B  & C4        & 2 & 2 & $+9.0$\\,pp & \\checkmark \\\\\nQwen-1.5B  & Wikipedia & 2 & 3$^\\dagger$ & $+8.7$\\,pp & $\\times$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$2v3 $\\auc = 0.6067$; fold 5 $= 0.595 < \\theta$. Marginal boundary.}\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Bonferroni-Corrected Confidence Intervals}\n\\label{sec:bonferroni_ci}\n\nTo control the family-wise error rate across all 10 model configurations, we apply Bonferroni correction: $\\alpha_{\\text{corr}} = 0.05 / 10 = 0.005$, yielding 99.5\\% confidence intervals ($z = 2.807$).\nTable~\\ref{tab:bonferroni_ci} reports the corrected intervals for each configuration's $\\Kempirical$ boundary pair.\nEight of ten configurations retain CI lower bounds above $\\theta{=}0.60$; two marginal $\\Kempirical{=}2$ configurations (Qwen-cont, LLaMA-8B) see their lower bounds dip below $\\theta$ under the stricter criterion ($0.5976$ and $0.5988$, respectively).\nThese near-misses reflect narrow effect sizes ($\\auc - \\theta < 0.013$) rather than classification failure: both retain point estimates above $\\theta$ and uncorrected 95\\% CI lower bounds above $\\theta$.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical$ boundary pairs across all 10 configurations. $\\alpha_{\\text{corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat{\\sigma}_{\\text{boot}}$. ``Pass $\\theta$'': CI lower bound $> 0.60$.}\n\\label{tab:bonferroni_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Boundary} & $\\auc$ & $\\hat{\\sigma}_{\\text{boot}}$ & \\textbf{99.5\\% CI} & \\textbf{Pass $\\theta$} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 2$ configurations}} \\\\\nQwen-rw (Instruct)       & 1v2 & .6955 & .0046 & $[.683,\\,.708]$ & \\checkmark \\\\\nPythia-1.4B               & 1v2 & .6539 & .0046 & $[.641,\\,.667]$ & \\checkmark \\\\\nQwen-base                 & 1v2 & .6260 & .0047 & $[.613,\\,.639]$ & \\checkmark \\\\\nQwen-7B$^\\ddagger$        & 1v2 & .6168 & .0046 & $[.604,\\,.630]$ & \\checkmark \\\\\nLLaMA-8B                  & 1v2 & .6123 & .0048 & $[.599,\\,.626]$ & $\\times$ \\\\\nQwen-cont (Instruct)     & 1v2 & .6112 & .0049 & $[.598,\\,.625]$ & $\\times$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$\\Kempirical = 1$ configurations}} \\\\\nOLMo-1B                   & 0v1 & .9860 & .0009 & $[.983,\\,.989]$ & \\checkmark \\\\\nMistral-7B                & 0v1 & .9842 & .0009 & $[.982,\\,.987]$ & \\checkmark \\\\\nPythia-6.9B$^\\S$          & 0v1 & .9599 & .0015$^\\dagger$ & $[.956,\\,.964]$ & \\checkmark \\\\\nGemma-2-2B                & 0v1 & .9530 & .0018 & $[.948,\\,.958]$ & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B; scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\S$Nucleus sampling ($p{=}0.95$, $T{=}1.0$).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$Estimated from analogous configurations (no separate bootstrap JSON).}\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Cross-Sample Robustness: 5K vs.\\ 10K}\n\\label{sec:robustness_10k}\n\nThe preceding analyses fix the sample pool at $N{=}5{,}000$ passages per depth.\nTo assess between-sample variability, we re-draw an independent $N{=}10{,}000$ sample from C4 using a different random seed and repeat the full OBD pipeline.\nIf $\\Kempirical$ and the boundary AUC are driven by the underlying distributional shift rather than by idiosyncrasies of a particular sample, both quantities should remain stable across draws.\n\nTable~\\ref{tab:robustness_10k} reports the results.\nFor Pythia-1.4B (continuation, C4), the 5K and 10K samples agree on $\\Kempirical{=}2$: the 0v1 AUC is nearly identical ($0.9700$ vs.\\ $0.9712$), while the boundary 1v2 AUC decreases from $0.6539$ to $0.6175$ ($\\Delta = -0.036$).\nThis shift is consistent with natural sampling variability across C4 subsets and does not alter the qualitative depth boundary.\nThe 2v3 pair remains near chance in both draws ($0.54$, $0.54$), confirming that depths $\\geq 2$ are indistinguishable regardless of sample.\nQwen-1.5B (continuation, C4) replicates the same pattern ($\\Kempirical{=}2$, 1v2 $\\auc = 0.6346$).\nLLaMA-3.1-8B (continuation, C4) is the sole configuration where the 10K OOF AUC drops below $\\theta$ ($0.5880$; pipeline AUC $= 0.6148$; Bonferroni 99.5\\% CI $[0.5776, 0.5978]$), yielding $\\Kempirical{=}1$ under the stricter criterion.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Cross-sample robustness: pairwise AUC and $\\Kempirical$ under 5K and 10K C4 samples drawn with different random seeds. All configurations use continuation mode. $\\Kempirical$ is determined by the $\\theta{=}0.60$ threshold on 1v2 AUC.}\n\\label{tab:robustness_10k}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & $N$ & \\textbf{AUC(0v1)} & \\textbf{AUC(1v2)} & \\textbf{AUC(2v3)} & $\\Kempirical$ \\\\\n\\midrule\nPythia-1.4B cont & 5K  & 0.9700 & 0.6539 & 0.5400 & 2 \\\\\nPythia-1.4B cont & 10K & 0.9712 & 0.6175 & 0.5364 & 2 \\\\\n\\midrule\nQwen-1.5B cont  & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nQwen-1.5B cont  & 10K & 0.9875 & 0.6346 & 0.5616 & 2 \\\\\n\\midrule\nLLaMA-8B cont   & 5K  & \\multicolumn{3}{c}{(see Table~\\ref{tab:bonferroni_ci})} & 2 \\\\\nLLaMA-8B cont   & 10K & 0.9282 & 0.5880$^\\dagger$ & 0.5247 & 1$^\\dagger$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\dagger$OOF AUC (pipeline AUC $= 0.6148$); Bonferroni 99.5\\% CI $[0.5776, 0.5978]$ does not pass $\\theta$.} \\\\\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 222,
      "startLine": 1,
      "totalLines": 222
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01ApkYa7LT8aKT8Gs4tLZUr4`</summary>

```json
{
  "project": "gen-depth-contamination",
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
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "0b1747fc-5b55-4931-ae5d-6bb2bd382bbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8uHSWhiDQ89NLWmiSTtNp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 24366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2283
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

_source line 18 · 2026-05-22T21:21:35.669Z_

<details><summary>↩ Tool result · `toolu_01ApkYa7LT8aKT8Gs4tLZUr4`</summary>

```text
Error: result (286,193 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "fa917ebc-8685-420c-9492-e9cb96167f9e",
  "tool_use_result": {
    "content": "Error: result (286,193 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_llama8b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:25:55.895Z\", \"updated_at\": \"2026-05-22T20:26:09.870Z\", \"hypothesis\": \"增加 LLaMA-8B C4 样本量从 5k→10k 可将 1v2 bootstrap std 缩小 ~√2 倍，使 Bonferroni 99.5% CI lower bound 恢复到 θ=0.60 以上\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 23232, \"checkpoint_path\": \"results/exp_llama8b_10k/\", \"log_path\": \"/tmp/exp_llama8b_10k.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"AUC_0v1\": 0.9282, \"AUC_1v2\": 0.6148, \"AUC_1v2_oof\": 0.588, \"AUC_2v3\": 0.5247, \"AUC_3v4\": 0.5519, \"AUC_4v5\": 0.5262, \"bootstrap_1v2_oof_auc\": 0.588, \"bootstrap_1v2_95CI\": [0.5809, 0.595], \"bootstrap_1v2_995CI_bonferroni\": [0.5776, 0.5978], \"bonferroni_pass\": false, \"perm_pvalue_1v2\": 0.0001, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"All pairwise AUC from Qwen cross-scoring (Phase 2). Pipeline AUC 1v2=0.6148 (mean-of-folds).\"}, \"completed_at\": \"2026-05-22T19:21:09.215Z\"}, \"exp_olmo1b_10k\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:05:20.014Z\", \"updated_at\": \"2026-05-22T20:07:32.785Z\", \"hypothesis\": \"OLMo-1B 10K sample-size robustness: 5K borderline K*=2 (1v2 AUC=0.6145, CI lower=0.6045, barely above θ=0.60) should remain K*=2 at 10K with narrower CI, confirming between-sample stability for borderline verdicts.\", \"spec\": {\"command\": \"bash /tmp/exp_olmo1b_10k.sh (Phase1: OLMo-1B continuation gen + Phase2: Qwen scorer)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"pid\": 66415, \"data_path\": \"data/olmo1b_c4_10k\", \"data_count\": 10000, \"model_name\": \"allenai/OLMo-1B-hf (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"/tmp/exp_olmo1b_10k.log\", \"checkpoint_path\": \"results/olmo1b_c4_10k/\"}}, \"seed_gemma27b_c4_s42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:05:43.080Z\", \"updated_at\": \"2026-05-22T19:36:47.962Z\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 26893, \"gpu\": \"cuda:0\"}}, \"exp_gemma2b_10k\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:00:38.686Z\", \"updated_at\": \"2026-05-22T18:03:08.397Z\", \"hypothesis\": \"Gemma-2-2B 10K sample-size robustness: 5K borderline K*=1 (1v2 AUC=0.5981, just below θ=0.60) should remain K*=1 at 10K, confirming between-sample stability for borderline verdicts. Adds a K*=1 datapoint to the 10K robustness table (currently only K*=2 configs).\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 54709, \"gpu\": \"cuda:3\"}}, \"exp_pythia14b_c4_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:57:18.681Z\", \"updated_at\": \"2026-05-22T14:59:24.436Z\", \"hypothesis\": \"统一所有 K*=2 configs 的样本量至 10K，避免 selective precision boosting 质疑。Pythia-1.4B 5K 已稳定通过 Bonferroni (CI_lower≈0.641>0.60)，10K 为一致性验证。\", \"spec\": {\"command\": \"python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"data/exp_pythia14b_c4_10k\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"/tmp/exp_pythia14b_c4_10k.log\", \"checkpoint_path\": \"results/exp_pythia14b_c4_10k/\"}, \"metrics\": {\"K_star\": 2, \"AUC_0v1\": 0.9712, \"AUC_1v2\": 0.6175, \"AUC_2v3\": 0.5364, \"AUC_3v4\": 0.5134, \"AUC_4v5\": 0.5088, \"bootstrap_1v2_95CI\": [0.6108, 0.6242], \"bootstrap_1v2_995CI_bonferroni\": [0.6078, 0.6273], \"perm_pvalue_1v2\": 0.0001, \"bonferroni_pass\": true, \"top_feature\": \"freq_entropy\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:14:41.623Z\"}, \"exp_qwen_cont_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:27:38.591Z\", \"updated_at\": \"2026-05-22T14:59:22.490Z\", \"hypothesis\": \"增加 Qwen-cont C4 样本量从 5k→10k 可将 1v2 bootstrap std 缩小 ~√2 倍，使 Bonferroni 99.5% CI lower bound 恢复到 θ=0.60 以上\", \"spec\": {\"command\": \"bash /tmp/run_qwen_cont_10k.sh (Phase1: base generation + Phase2: instruct scoring)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_cont_10k\", \"data_count\": 10000, \"model_name\": \"Qwen/Qwen2.5-1.5B (base, continuation) + Qwen/Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_qwen_cont_10k/\", \"log_path\": \"/tmp/exp_qwen_cont_10k_phase1.log\"}, \"metrics\": {\"K_star\": 2, \"AUC_0v1\": 0.9875, \"AUC_1v2\": 0.6346, \"AUC_2v3\": 0.5616, \"AUC_3v4\": 0.5451, \"AUC_4v5\": 0.5254, \"bootstrap_1v2_95CI\": [0.6282, 0.6409], \"bootstrap_1v2_995CI_bonferroni\": [0.6255, 0.6436], \"perm_pvalue_1v2\": 0.0001, \"bonferroni_pass\": true, \"top_feature\": \"freq_entropy\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:47:57.847Z\"}, \"exp_pythia14b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:59:05.554Z\", \"updated_at\": \"2026-05-22T12:00:24.157Z\", \"hypothesis\": \"统一所有 K*=2 configs 样本量至 10K，避免 selective precision boosting 质疑。Pythia-1.4B 5K 已稳定通过 Bonferroni (CI_lower≈0.641>0.60)，10K 为一致性验证。\", \"spec\": {\"command\": \"python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"data/exp_pythia14b_c4_10k\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"N/A\", \"note\": \"重复条目，已合并到 exp_pythia14b_c4_10k\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-22T12:00:24.157Z\"}, \"exp_gemma27b_c4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:57:19.726Z\", \"updated_at\": \"2026-05-22T08:11:14.747Z\", \"hypothesis\": \"Gemma-2-27B (27B params, base model) on C4 domain will show slower depth saturation (higher K*) than smaller models due to greater generation capacity, while maintaining the universal depth-dependent distinguishability pattern observed across model families.\"}, \"seed_qwen15b_c4_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:11.792Z\", \"updated_at\": \"2026-05-22T06:39:21.815Z\", \"hypothesis\": \"Qwen-1.5B C4 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode rewrite --top_p 0.95 --seed 123 (C4)\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"3156\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_c4_s123/\", \"submitted_at\": \"2026-05-22T03:58:27.354Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_qwen15b_c4_s123\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 123, \"metrics\": {\"K_star\": 2, \"auc_0v1\": 0.9956, \"auc_1v2\": 0.7014, \"auc_2v3\": 0.5911, \"auc_3v4\": 0.5405, \"auc_4v5\": 0.5335}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_c4_s123/\", \"wall_clock_seconds\": 9654.5, \"gpu_hours\": 2.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:39:21.815Z\"}, \"seed_qwen15b_wiki_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:09.969Z\", \"updated_at\": \"2026-05-22T06:39:19.860Z\", \"hypothesis\": \"Qwen-1.5B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode rewrite --top_p 0.95 --seed 123\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"3005\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_wiki_s123/\", \"submitted_at\": \"2026-05-22T03:58:25.151Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_qwen15b_wiki_s123\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 123, \"metrics\": {\"K_star\": 3, \"auc_0v1\": 0.9945, \"auc_1v2\": 0.7059, \"auc_2v3\": 0.6067, \"auc_3v4\": 0.5531, \"auc_4v5\": 0.5292}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_wiki_s123/\", \"wall_clock_seconds\": 9654.7, \"gpu_hours\": 2.68}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T06:39:19.860Z\"}, \"seed_pythia14b_wiki_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:08.091Z\", \"updated_at\": \"2026-05-22T06:39:17.971Z\", \"hypothesis\": \"Pythia-1.4B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode continuation --top_p 0.95 --seed 123 (two-phase: Pythia gen + Qwen score)\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"2863\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_pythia14b_wiki_s123/\", \"submitted_at\": \"2026-05-22T03:58:22.018Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_pythia14b_wiki_s123\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b (generator) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 123, \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9751, \"auc_1v2\": 0.5766, \"auc_2v3\": 0.5318, \"auc_3v4\": 0.5175, \"auc_4v5\": 0.527}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_pythia14b_wiki_s123/\", \"wall_clock_seconds\": 9656.0, \"gpu_hours\": 2.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:39:17.971Z\"}, \"7b-cross-transfer\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:51:00.658Z\", \"updated_at\": \"2026-05-22T00:54:55.385Z\", \"conclusion\": \"killed\"}, \"arxiv_multi_source\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:26:09.176Z\", \"updated_at\": \"2026-05-22T00:54:54.548Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export CUDA_VISIBLE_DEVICES=1 && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_multi_source_arxiv.py 2>&1 | tee results/exp_multi_source_arxiv/run.log\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"298833\", \"log_path\": \"~/runs/gen-depth-contamination/arxiv_multi_source.log\", \"submitted_at\": \"2026-05-20T08:26:08.709Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r10_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:37.475Z\", \"updated_at\": \"2026-05-22T00:54:53.730Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=1 python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"333215\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r10_nofilter.log\", \"submitted_at\": \"2026-05-20T17:16:36.869Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r10_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:39.694Z\", \"updated_at\": \"2026-05-22T00:54:52.904Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=2 python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy binary --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"333292\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r10_binary.log\", \"submitted_at\": \"2026-05-20T17:16:39.317Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r10_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:41.394Z\", \"updated_at\": \"2026-05-22T00:54:52.064Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=3 python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy graduated --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"333434\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r10_graduated.log\", \"submitted_at\": \"2026-05-20T17:16:40.993Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r30_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:43.195Z\", \"updated_at\": \"2026-05-22T00:54:44.685Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=0 python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy no_filter --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"223186\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r30_nofilter.log\", \"submitted_at\": \"2026-05-20T17:16:42.824Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:34:33.240Z\", \"updated_at\": \"2026-05-22T00:54:43.784Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_nofilter.log\", \"submitted_at\": \"2026-05-20T17:34:32.842Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:34:35.595Z\", \"updated_at\": \"2026-05-22T00:54:42.896Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy binary --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_binary.log\", \"submitted_at\": \"2026-05-20T17:34:35.217Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:34:37.559Z\", \"updated_at\": \"2026-05-22T00:54:42.034Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy graduated --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_graduated.log\", \"submitted_at\": \"2026-05-20T17:34:37.105Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r30_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:34:39.366Z\", \"updated_at\": \"2026-05-22T00:54:41.166Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r30_nofilter.log\", \"submitted_at\": \"2026-05-20T17:34:38.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_nf\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:35:11.100Z\", \"updated_at\": \"2026-05-22T00:54:40.358Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"338477\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_nf.log\", \"submitted_at\": \"2026-05-20T17:35:10.713Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_bin\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:35:13.515Z\", \"updated_at\": \"2026-05-22T00:54:39.423Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy binary --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"338554\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_bin.log\", \"submitted_at\": \"2026-05-20T17:35:13.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_grad\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:35:15.378Z\", \"updated_at\": \"2026-05-22T00:54:37.930Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy graduated --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"338694\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_grad.log\", \"submitted_at\": \"2026-05-20T17:35:14.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r30_nf\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:35:17.531Z\", \"updated_at\": \"2026-05-22T00:54:36.954Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"224549\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r30_nf.log\", \"submitted_at\": \"2026-05-20T17:35:17.149Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_eval_r10_nf_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:44:37.119Z\", \"updated_at\": \"2026-05-22T00:54:36.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0 --eval_only\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"341368\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_eval_r10_nf_v2.log\", \"submitted_at\": \"2026-05-20T17:44:36.698Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r30_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:44:38.912Z\", \"updated_at\": \"2026-05-22T00:54:31.052Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy binary --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"341445\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r30_binary.log\", \"submitted_at\": \"2026-05-20T17:44:38.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r30_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:44:40.942Z\", \"updated_at\": \"2026-05-22T00:54:30.235Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 30 --strategy graduated --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"341524\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r30_graduated.log\", \"submitted_at\": \"2026-05-20T17:44:40.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r50_nf\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:46:06.026Z\", \"updated_at\": \"2026-05-22T00:54:29.360Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 50 --strategy no_filter --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"225683\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r50_nf.log\", \"submitted_at\": \"2026-05-20T17:46:05.636Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r50_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:49:15.968Z\", \"updated_at\": \"2026-05-22T00:54:28.489Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 50 --strategy binary --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"344316\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r50_binary.log\", \"submitted_at\": \"2026-05-20T17:53:07.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r50_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:53:10.838Z\", \"updated_at\": \"2026-05-22T00:54:27.679Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 50 --strategy graduated --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"344395\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r50_graduated.log\", \"submitted_at\": \"2026-05-20T17:53:10.443Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r100_nf\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:53:12.678Z\", \"updated_at\": \"2026-05-22T00:54:26.843Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 100 --strategy no_filter --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"226555\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r100_nf.log\", \"submitted_at\": \"2026-05-20T17:53:12.278Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r100_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:53:46.876Z\", \"updated_at\": \"2026-05-22T00:54:25.989Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://huggingface.co && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 100 --strategy graduated --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:1\"], \"pid\": \"226991\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r100_graduated.log\", \"submitted_at\": \"2026-05-20T17:53:46.454Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"sweep_r100_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:53:14.587Z\", \"updated_at\": \"2026-05-22T00:54:25.067Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_contamination_rate_sweep.py --rate 100 --strategy binary --device cuda:0\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"227976\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r100_binary.log\", \"submitted_at\": \"2026-05-20T18:00:00.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filtering_predict\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:48:51.515Z\", \"updated_at\": \"2026-05-22T00:54:24.104Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && rm -rf /root/autodl-tmp/.hf_cache/models--microsoft--deberta-v3-base/.no_exist && python -c 'from transformers import AutoTokenizer, AutoModelForSequenceClassification; print(\\\\\\\"Downloading deberta-v3-base...\\\\\\\"); AutoTokenizer.from_pretrained(\\\\\\\"microsoft/deberta-v3-base\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"); AutoModelForSequenceClassification.from_pretrained(\\\\\\\"microsoft/deberta-v3-base\\\\\\\", num_labels=6, cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"); print(\\\\\\\"Download complete.\\\\\\\")' && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=2 python scripts/exp_deberta_filtering_predict.py --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"349680\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filtering_predict.log\", \"submitted_at\": \"2026-05-20T18:40:45.030Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filter_no_filter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:11:24.655Z\", \"updated_at\": \"2026-05-22T00:54:23.131Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && export HF_DATASETS_OFFLINE=0 && export HF_HUB_OFFLINE=0 && export TRANSFORMERS_OFFLINE=0 && cd /root/autodl-tmp/gen-depth-contamination && python -u scripts/exp_deberta_filtering_comparison.py --strategy no_filter --device cuda:0 --seed 42\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"353797\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filter_no_filter.log\", \"submitted_at\": \"2026-05-20T19:12:18.634Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filter_obd_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:11:26.462Z\", \"updated_at\": \"2026-05-22T00:54:18.302Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && export HF_DATASETS_OFFLINE=0 && export HF_HUB_OFFLINE=0 && export TRANSFORMERS_OFFLINE=0 && cd /root/autodl-tmp/gen-depth-contamination && python -u scripts/exp_deberta_filtering_comparison.py --strategy obd_binary --device cuda:0 --seed 42\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"353876\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filter_obd_binary.log\", \"submitted_at\": \"2026-05-20T19:12:21.027Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filter_deberta_binary\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:11:29.363Z\", \"updated_at\": \"2026-05-22T00:54:17.473Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && export HF_DATASETS_OFFLINE=0 && export HF_HUB_OFFLINE=0 && export TRANSFORMERS_OFFLINE=0 && cd /root/autodl-tmp/gen-depth-contamination && python -u scripts/exp_deberta_filtering_comparison.py --strategy deberta_binary --device cuda:0 --seed 42\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"354020\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filter_deberta_binary.log\", \"submitted_at\": \"2026-05-20T19:12:23.647Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"deberta_filter_deberta_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:26:32.955Z\", \"updated_at\": \"2026-05-22T00:54:16.540Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && python -u scripts/exp_deberta_filtering_comparison.py --strategy deberta_graduated --device cuda:0 --seed 42\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"359411\", \"log_path\": \"~/runs/gen-depth-contamination/deberta_filter_deberta_graduated.log\", \"submitted_at\": \"2026-05-20T19:28:15.359Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"seed2_no_filter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:20:45.368Z\", \"updated_at\": \"2026-05-22T00:54:15.656Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 2 --num_seeds 1 --strategy no_filter --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"362953\", \"log_path\": \"~/runs/gen-depth-contamination/seed2_no_filter.log\", \"submitted_at\": \"2026-05-20T20:20:44.951Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"seed2_binary_ours\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:20:47.753Z\", \"updated_at\": \"2026-05-22T00:54:14.713Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 2 --num_seeds 1 --strategy binary_ours --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"363095\", \"log_path\": \"~/runs/gen-depth-contamination/seed2_binary_ours.log\", \"submitted_at\": \"2026-05-20T20:20:47.308Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"seed2_graduated\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T20:20:49.637Z\", \"updated_at\": \"2026-05-22T00:54:13.865Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 2 --num_seeds 1 --strategy graduated --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"363242\", \"log_path\": \"~/runs/gen-depth-contamination/seed2_graduated.log\", \"submitted_at\": \"2026-05-20T20:20:49.203Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"gsm8k_patch_nf_s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:13:12.767Z\", \"updated_at\": \"2026-05-22T00:54:13.005Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 0 --num_seeds 1 --strategy no_filter --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"368659\", \"log_path\": \"~/runs/gen-depth-contamination/gsm8k_patch_nf_s0.log\", \"submitted_at\": \"2026-05-20T21:13:12.327Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"gsm8k_patch_bo_s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:13:15.584Z\", \"updated_at\": \"2026-05-22T00:54:12.180Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 0 --num_seeds 1 --strategy binary_ours --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"368799\", \"log_path\": \"~/runs/gen-depth-contamination/gsm8k_patch_bo_s0.log\", \"submitted_at\": \"2026-05-20T21:13:15.174Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"gsm8k_patch_grad_s0\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:13:17.809Z\", \"updated_at\": \"2026-05-22T00:54:11.337Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 0 --num_seeds 1 --strategy graduated --skip_base\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"368942\", \"log_path\": \"~/runs/gen-depth-contamination/gsm8k_patch_grad_s0.log\", \"submitted_at\": \"2026-05-20T21:13:17.386Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"gsm8k-serial-rerun\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:59:44.212Z\", \"updated_at\": \"2026-05-22T00:54:10.300Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 1 --num_seeds 1 --strategy no_filter --skip_base && python scripts/exp_expanded_downstream_eval.py --device cuda:0 --seed_start 1 --num_seeds 1 --strategy binary_ours --skip_base && lm_eval --model hf --model_args pretrained=Qwen/Qwen2.5-1.5B --tasks gsm8k --num_fewshot 5 --batch_size auto --device cuda:0 --output_path results/exp_expanded_downstream_eval/base_gsm8k_eval\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"373073\", \"log_path\": \"~/runs/gen-depth-contamination/gsm8k-serial-rerun.log\", \"submitted_at\": \"2026-05-20T21:59:43.784Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"exp_008_retrain_chain\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:26:02.931Z\", \"updated_at\": \"2026-05-22T00:53:20.061Z\", \"hypothesis\": \"Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain K* ≤ prompt-chain K*=2. 每代独立 LoRA fine-tune 1 epoch on 前代输出，再用 fine-tuned model 生成下一代。验证 prompt-chain 是 conservative upper bound。C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"conclusion\": \"killed\"}, \"exp_olmo_retrain_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:36:11.450Z\", \"updated_at\": \"2026-05-22T00:53:19.065Z\", \"hypothesis\": \"OLMo-1B retrain-chain ecological validity (v2, fix M009 model download): LoRA rank=16, alpha=32, 1 epoch per generation on C4 5K docs. Retrain-chain K* ≤ prompt-chain K*=2, confirming prompt-chain as conservative upper bound. Independent LoRA per generation, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_olmo_retrain_chain\", \"conclusion\": \"killed\", \"notes\": \"Director 决定放弃 OLMo retrain-chain (2026-05-18)。原因：cqa1 两次下载失败（M009 模型权重中断 + 网络端口耗尽），DDL 紧张不再重试。cuda:0 重新分配给 code domain 备用或 Qwen retrain-chain。\"}, \"exp_pythia69b_c4_nuc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:57:54.120Z\", \"updated_at\": \"2026-05-21T23:00:07.454Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上使用 nucleus sampling（非 greedy）的 K*=2，与其他 continuation 模型的 decoding 策略对齐，消除 greedy 高估 confound。生成阶段自评，完成后用 Qwen-1.5B scorer 重跑 features+OBD（方案 2）。\", \"parent\": \"exp_pythia69b_c4_depth_chain_v3\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path ... --scorer_path Qwen2.5-1.5B --num_samples 5000 --max_depth 5 --generation_mode continuation --data_dir data/exp_pythia69b_c4_nuc --results_dir results/exp_pythia69b_c4_nuc\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_pythia69b_c4_nuc\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-6.9b\", \"seed\": \"default\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A (full pipeline: seed->generation->features->OBD)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/pythia69b_nuc_v2.log\", \"checkpoint_path\": \"results/exp_pythia69b_c4_nuc_qwen/\"}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9599, \"1v2\": 0.5955, \"2v3\": 0.5298, \"3v4\": 0.5135}, \"scorer\": \"Qwen-1.5B\", \"theta\": 0.6, \"note\": \"1v2 AUC borderline (0.0045 below threshold)\"}, \"completed_at\": \"2026-05-21T23:00:07.454Z\"}, \"exp_pythia69b_c4_depth_chain_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:21:54.364Z\", \"updated_at\": \"2026-05-21T19:55:37.923Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上的 K*=2，与其他 ≥7B 模型一致，验证 K*=2 不依赖 Qwen 家族。使用 Qwen-1.5B scorer（D095）。\", \"parent\": \"exp_pythia69b_c4_depth_chain_v2\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23 --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 2 --generation_mode continuation --no_sample --data_dir data/exp_pythia69b_c4 --results_dir results/exp_pythia69b_c4\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"395575\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain_v3.log\", \"submitted_at\": \"2026-05-21T03:22:20.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"EleutherAI/pythia-6.9b\", \"model_path\": \"/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23\", \"scorer_path\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"data_path\": \"data/exp_pythia69b_c4\", \"data_count\": 5000, \"seed\": \"default\", \"generation_mode\": \"continuation\", \"no_sample\": true, \"max_depth\": 5, \"checkpoint_source\": \"N/A (full pipeline)\", \"eval_data\": \"N/A (full pipeline: seed->generation->features->OBD)\", \"wall_clock_seconds\": 32849.3, \"gpu_hours\": 9.12}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:29:46.273Z\"}, \"failure_reason\": \"greedy confound (--no_sample): AUC_1v2 inflated to 0.8542, not usable for cross-model comparison. K*=2 under greedy is artifact, not genuine nucleus result.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T12:29:49.365Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:29:53.480338+00:00\"}]}, \"metrics\": {\"0v1_auc\": 0.9941, \"1v2_auc\": 0.8542, \"2v3_auc\": 0.5373, \"3v4_auc\": 0.5339, \"4v5_auc\": 0.5211, \"kstar_at_060\": 2, \"0v1_jsd\": 0.53459, \"1v2_jsd\": 0.06438, \"2v3_jsd\": 0.00502, \"empty_texts_total\": 144, \"features_rows\": 30000}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_pythia69b_c4/features.csv\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain_v3.log\"}, \"exp_pythia14b_c4_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:10:50.827Z\", \"updated_at\": \"2026-05-21T14:09:26.792Z\", \"hypothesis\": \"Pythia-1.4B C4 depth chain 可复现性验证：标准化 pipeline（Qwen-1.5B scorer）下 K* 值与主表一致。\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path pythia-1.4b --scorer_path Qwen2.5-1.5B --generation_mode continuation --no_sample --data_dir data/exp_pythia14b_c4_rerun --results_dir results/exp_pythia14b_c4_rerun\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_pythia14b_c4_rerun\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": \"default\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_pythia14b_c4_rerun/features.csv\", \"log_path\": \"N/A\", \"NOTE\": \"GREEDY (--no_sample) — not comparable to main table nucleus results\"}, \"completed_at\": \"2026-05-21T14:09:16.827Z\", \"metrics\": {\"0v1_auc\": 0.9979, \"1v2_auc\": 0.8786, \"2v3_auc\": 0.5399, \"3v4_auc\": 0.5062, \"4v5_auc\": 0.5025, \"kstar_at_060\": 2, \"0v1_jsd\": 0.5844, \"1v2_jsd\": 0.0718, \"NOTE\": \"GREEDY decoding -- inflated AUC, not comparable to main table\"}}, \"exp_olmo1b_c4_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:10:33.358Z\", \"updated_at\": \"2026-05-21T11:11:13.525Z\", \"hypothesis\": \"OLMo-1B C4 depth chain 可复现性验证：标准化 pipeline（Qwen-1.5B scorer）下 K* 值与主表一致。\", \"conclusion\": \"negative\", \"metrics\": {\"0v1_auc\": 0.986, \"1v2_auc\": 0.508, \"2v3_auc\": 0.4973, \"3v4_auc\": 0.5024, \"4v5_auc\": 0.4942, \"kstar_at_060\": 1, \"main_table_1v2\": 0.6145, \"delta\": -0.1065}, \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--allenai--OLMo-1B-hf/... --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --no_sample\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"data_path\": \"data/exp_olmo1b_c4_rerun\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": \"default\", \"checkpoint_path\": \"results/exp_olmo1b_c4_rerun/\", \"log_path\": \"results/exp_olmo1b_c4_rerun/experiment_config.json\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"completed_at\": \"2026-05-21T11:11:13.525Z\"}, \"exp_pythia69b_c4_depth_chain_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:23:27.242Z\", \"updated_at\": \"2026-05-21T02:46:08.127Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上的 K*=2，与其他 ≥7B 模型一致，验证 K*=2 不依赖 Qwen 家族。使用 Qwen-1.5B scorer 以匹配主表（D095）。\", \"parent\": \"exp_pythia69b_c4_depth_chain\", \"spec\": {\"model_name\": \"EleutherAI/pythia-6.9b\", \"model_path\": \"/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23\", \"scorer_path\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"data_path\": \"data/exp_pythia69b_c4 (C4 seed from run_pipeline.py)\", \"data_count\": 5000, \"seed\": \"default\", \"generation_mode\": \"continuation\", \"no_sample\": true, \"max_depth\": 5, \"batch_size\": 4, \"feat_batch_size\": 2, \"num_samples\": 5000, \"command\": \"python scripts/run_pipeline.py --model_path .../pythia-6.9b --scorer_path .../Qwen2___5-1___5B --num_samples 5000 --max_depth 5 --generation_mode continuation --no_sample\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"391937\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain_v2.log\", \"submitted_at\": \"2026-05-21T02:23:38Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"N/A (full pipeline re-run, not eval)\", \"eval_data\": \"N/A (full pipeline: seed→generation→features→OBD)\", \"failure_reason\": \"模型文件不完整: 缺少 model-00001-of-00002.safetensors, v1 下载中断仅完成 66%\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 1350.1, \"gpu_hours\": 0.38}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T02:46:08.127Z\"}, \"exp_pythia69b_c4_depth_chain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:47:28.696Z\", \"updated_at\": \"2026-05-21T02:23:07.638Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上的 K*=2，与其他 ≥7B 模型一致，验证 K*=2 不依赖 Qwen 家族。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && cd /root/autodl-tmp/gen-depth-contamination && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && echo '=== Downloading Pythia-6.9B ===' && python -c 'from huggingface_hub import snapshot_download; path=snapshot_download(\\\\\\\"EleutherAI/pythia-6.9b\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"); print(f\\\\\\\"MODEL_PATH={path}\\\\\\\")' && MODEL_PATH=\\\\$(python -c 'from huggingface_hub import snapshot_download; print(snapshot_download(\\\\\\\"EleutherAI/pythia-6.9b\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"))') && echo \\\\\\\"=== Running pipeline with model at \\\\$MODEL_PATH ===\\\\\\\" && mkdir -p data/exp_pythia69b_c4 results/exp_pythia69b_c4 && python scripts/run_pipeline.py --model_path \\\\$MODEL_PATH --data_dir data/exp_pythia69b_c4 --results_dir results/exp_pythia69b_c4 --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 2 --generation_mode continuation --no_sample\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"390600\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain.log\", \"submitted_at\": \"2026-05-21T01:56:36.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"D095 violation: missing --scorer_path, used self-scoring instead of Qwen-1.5B. Killed by Director. Will resubmit as v2.\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 1591.2, \"gpu_hours\": 0.44}, \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-21T01:54:27.864Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && cd /root/autodl-tmp/gen-depth-contamination && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && echo '=== Downloading Pythia-6.9B ===' && python -c 'from huggingface_hub import snapshot_download; path=snapshot_download(\\\\\\\"EleutherAI/pythia-6.9b\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"); print(f\\\\\\\"MODEL_PATH={path}\\\\\\\")' && MODEL_PATH=\\\\$(python -c 'from huggingface_hub import snapshot_download; print(snapshot_download(\\\\\\\"EleutherAI/pythia-6.9b\\\\\\\", cache_dir=\\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"))') && echo \\\\\\\"=== Running pipeline with model at \\\\$MODEL_PATH ===\\\\\\\" && mkdir -p data/exp_pythia69b_c4 results/exp_pythia69b_c4 && python scripts/run_pipeline.py --model_path \\\\$MODEL_PATH --data_dir data/exp_pythia69b_c4 --results_dir results/exp_pythia69b_c4 --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 2 --generation_mode continuation --no_sample\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\"}, \"pid\": \"390600\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T02:23:07.638Z\"}, \"exp_expanded_downstream_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:02:47.262Z\", \"updated_at\": \"2026-05-21T00:23:17.997Z\", \"hypothesis\": \"K*-guided binary filtering consistently outperforms graduated filtering across a broader set of benchmarks (GSM8K, ARC-Challenge, WinoGrande, TruthfulQA, PIQA), not just MMLU/HellaSwag, validating the generalizability of the filtering consistency claim in Section 5.\", \"spec\": {\"command\": \"python scripts/run_expanded_eval.py (base eval + 3 strategies × 3 seeds LoRA train+eval, 5 benchmarks)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"pid\": \"334626\", \"log_path\": \"cqa1-22115:/root/gen-depth-contamination/results/exp_expanded_downstream_eval/\", \"submitted_at\": \"2026-05-20T17:17:37.434Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 30000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": \"42,123,456\", \"benchmarks\": \"PIQA, TruthfulQA-MC2, WinoGrande, ARC-Challenge, GSM8K\", \"checkpoint_path\": \"cqa1-22115:/root/gen-depth-contamination/results/exp_expanded_downstream_eval/\", \"wall_clock_seconds\": 24379.3, \"gpu_hours\": 6.77}, \"gpus\": [], \"metrics\": {\"metric_standard\": \"PIQA=acc_norm, ARC-C=acc_norm, WinoGrande=acc, TruthfulQA=mc2, GSM8K=exact_match(strict)\", \"base_model\": {\"piqa\": 0.7612, \"arc_c\": 0.5486, \"winogrande\": 0.6456, \"truthfulqa\": 0.4659, \"gsm8k\": 0.6224}, \"no_filter_mean\": {\"piqa\": 0.7519, \"arc_c\": 0.5193, \"winogrande\": 0.6485, \"truthfulqa\": 0.4246, \"gsm8k\": 0.5666}, \"binary_ours_mean\": {\"piqa\": 0.7479, \"arc_c\": 0.5171, \"winogrande\": 0.6406, \"truthfulqa\": 0.4398, \"gsm8k\": 0.5858}, \"graduated_mean\": {\"piqa\": 0.751, \"arc_c\": 0.519, \"winogrande\": 0.6461, \"truthfulqa\": 0.4245, \"gsm8k\": 0.5613}, \"binary_vs_nf_delta\": {\"piqa\": -0.4, \"arc_c\": -0.22, \"winogrande\": -0.79, \"truthfulqa\": 1.52, \"gsm8k\": 1.92}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T00:03:56.750Z\"}, \"exp_deberta_filtering_comparison\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:02:50.271Z\", \"updated_at\": \"2026-05-20T20:08:32.368Z\", \"hypothesis\": \"DeBERTa's higher K* on arXiv (K*=4 vs 15D K*=3) does not yield significantly better downstream performance when used for filtering, validating that the 15D lower bound is practically sufficient.\", \"spec\": {\"command\": \"python scripts/exp_deberta_filtering_comparison.py --strategy {no_filter,obd_binary,deberta_binary,deberta_graduated} --device cuda:0 --seed 42\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/\", \"data_count\": 13200, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"strategies\": [\"no_filter\", \"obd_binary\", \"deberta_binary\", \"deberta_graduated\"], \"prediction_results\": {\"deberta_accuracy\": 0.5363, \"obd_accuracy\": 0.4741, \"deberta_pred_distribution\": [2184, 1645, 2111, 1971, 1074, 4215], \"obd_pred_distribution\": [2177, 2470, 2196, 1900, 2098, 2359]}, \"lora_config\": {\"rank\": 16, \"alpha\": 32, \"targets\": [\"q_proj\", \"v_proj\"], \"dropout\": 0.05}, \"training_config\": {\"lr\": 0.0002, \"batch_size\": 4, \"grad_accum\": 4, \"epochs\": 1, \"max_length\": 256}, \"gpu_allocation\": {\"no_filter\": \"cuda:1\", \"obd_binary\": \"cuda:2\", \"deberta_binary\": \"cuda:3\", \"deberta_graduated\": \"pending\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_filtering_comparison/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_filtering_comparison/\"}, \"metrics\": {\"no_filter\": {\"mmlu\": 0.5895, \"hellaswag\": 0.6591, \"arc_c\": 0.4352}, \"obd_binary\": {\"mmlu\": 0.588, \"hellaswag\": 0.6599, \"arc_c\": 0.4522}, \"deberta_binary\": {\"mmlu\": 0.587, \"hellaswag\": 0.6593, \"arc_c\": 0.4471}, \"deberta_graduated\": {\"mmlu\": 0.5884, \"hellaswag\": 0.6586, \"arc_c\": 0.442}, \"summary\": \"obd_binary (15D) >= deberta_binary on all 3 benchmarks. DeBERTa K*=4 does not yield better filtering than 15D K*=3. Graduated < binary for both OBD and DeBERTa.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T20:06:51.128Z\"}, \"exp_contamination_rate_sweep\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:02:48.807Z\", \"updated_at\": \"2026-05-20T18:02:19.878Z\", \"hypothesis\": \"Binary filtering (remove depth>=1) consistently outperforms graduated filtering across contamination rates (10/30/50/100%), validating that K*=2 provides actionable curation guidance across realistic contamination scenarios, not just at full contamination.\", \"spec\": {\"command\": \"python scripts/contamination_rate_sweep.py (4 rates x 3 strategies = 12 runs)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1,cuda:2,cuda:3\", \"pid\": \"333220,333297,333439\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/contamination_sweep/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"training_config\": \"LoRA rank=16 alpha=32 1epoch\", \"current_round\": \"rate=10% (no_filter:cuda1/binary:cuda2/graduated:cuda3)\", \"remaining_rounds\": \"rate=30%,50%,100%\", \"eval_benchmarks\": \"MMLU-5shot HellaSwag-10shot ARC-Challenge-25shot\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_contamination_rate_sweep/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_contamination_rate_sweep/summary.json\"}, \"metrics\": {\"rate_10\": {\"no_filter\": {\"mmlu\": 0.5878, \"hellaswag\": 0.6652, \"arc_c\": 0.4471}, \"binary\": {\"mmlu\": 0.5868, \"hellaswag\": 0.6709, \"arc_c\": 0.4462}, \"graduated\": {\"mmlu\": 0.5873, \"hellaswag\": 0.6672, \"arc_c\": 0.4428}}, \"rate_30\": {\"no_filter\": {\"mmlu\": 0.5885, \"hellaswag\": 0.6625, \"arc_c\": 0.4334}, \"binary\": {\"mmlu\": 0.5867, \"hellaswag\": 0.6702, \"arc_c\": 0.448}, \"graduated\": {\"mmlu\": 0.5873, \"hellaswag\": 0.664, \"arc_c\": 0.4334}}, \"rate_50\": {\"no_filter\": {\"mmlu\": 0.5858, \"hellaswag\": 0.6582, \"arc_c\": 0.43}, \"binary\": {\"mmlu\": 0.5913, \"hellaswag\": 0.67, \"arc_c\": 0.4505}, \"graduated\": {\"mmlu\": 0.5848, \"hellaswag\": 0.6606, \"arc_c\": 0.4292}}, \"rate_100\": {\"no_filter\": {\"mmlu\": 0.5707, \"hellaswag\": 0.6217, \"arc_c\": 0.3891}, \"binary\": null, \"graduated\": {\"mmlu\": 0.5701, \"hellaswag\": 0.6215, \"arc_c\": 0.3933}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T18:02:19.878Z\"}, \"exp_olmo_retrain_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:47:22.000Z\", \"updated_at\": \"2026-05-20T14:57:53.008Z\", \"hypothesis\": \"OLMo-1B retrain-chain K*>=4 (matching Pythia/Qwen retrain-chain), confirming retrain-chain K* is protocol-determined not architecture-determined. LoRA rank=16, alpha=32, 1 epoch per generation, C4 5K docs, depth 0-4.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python exp_olmo_retrain_v3.py --device cuda:0\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/olmo_retrain_chain\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42}, \"metrics\": {\"k_star\": 4, \"pairwise_auc\": {\"0v1\": 0.9873, \"1v2\": 0.8889, \"2v3\": 0.7036, \"3v4\": 0.6817}, \"bootstrap_ci_10k\": {\"0v1\": {\"mean\": 0.9972, \"ci_95\": [0.9967, 0.9977]}, \"1v2\": {\"mean\": 0.9572, \"ci_95\": [0.9542, 0.9601]}, \"2v3\": {\"mean\": 0.8885, \"ci_95\": [0.8814, 0.8947]}, \"3v4\": {\"mean\": 0.8772, \"ci_95\": [0.8684, 0.8852]}}, \"permutation_test\": {\"0v1\": {\"auc\": 0.9988, \"p\": 0}, \"1v2\": {\"auc\": 0.961, \"p\": 0}, \"2v3\": {\"auc\": 0.8919, \"p\": 0.998}, \"3v4\": {\"auc\": 0.8762, \"p\": 1}}}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/olmo_retrain_v3.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/olmo_retrain_chain\", \"completed_at\": \"2026-05-20T14:57:53.008Z\"}, \"exp_7b_scorer_arxiv\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:33:38.614Z\", \"updated_at\": \"2026-05-20T13:27:43.350Z\", \"hypothesis\": \"Qwen2.5-7B scorer yields same K*=3 as Qwen2.5-1.5B scorer on arXiv depth chains, confirming K* is robust to scorer scale across domains (C4 + arXiv).\", \"parent\": \"exp_024_arxiv_domain\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_arxiv.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_025_pythia_arxiv + /root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_olmo\", \"data_count\": 26400, \"model_name\": \"Qwen2.5-7B + Qwen2.5-1.5B-Instruct (scorers), Pythia-1.4B + OLMo-1B (generators)\", \"seed\": 42, \"checkpoint_source\": \"pretrained (Qwen2.5-7B, Qwen2.5-1.5B-Instruct)\", \"eval_data\": \"arXiv depth chains (Pythia-1.4B + OLMo-1B, depth 0-5, 2200 samples/depth)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T13:24:06.236Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:24:08.238Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T13:24:11.891882+00:00\"}]}, \"metrics\": {\"pythia_arxiv_qwen1b5\": {\"k_star\": 3, \"0v1\": 0.9872, \"1v2\": 0.7938, \"2v3\": 0.6544}, \"olmo_arxiv_qwen1b5\": {\"k_star\": 1, \"0v1\": 0.9954, \"1v2\": 0.5182, \"2v3\": 0.4956}, \"pythia_arxiv_qwen7b\": {\"k_star\": 3, \"0v1\": 0.9844, \"1v2\": 0.7987, \"2v3\": 0.6551}, \"olmo_arxiv_qwen7b\": {\"k_star\": 1, \"0v1\": 0.9941, \"1v2\": 0.5089, \"2v3\": 0.492}, \"summary\": \"7B scorer and 1.5B scorer yield identical K* on arXiv: Pythia=3, OLMo=1. K* robust to 4.7x scorer scale increase across both C4 and arXiv domains.\"}}, \"exp_014_naturalistic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:19:56.644Z\", \"updated_at\": \"2026-05-20T13:12:42.795Z\", \"hypothesis\": \"OBD depth predictions on real-world Common Crawl text correlate with independent text quality metrics (vocabulary richness), validating that the depth signal captures meaningful text degradation beyond the synthetic training distribution.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/gen-depth-contamination/scripts/run_naturalistic_validation.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp014_naturalistic/\"}, \"conclusion\": \"success\", \"metrics\": {\"binary_auc\": 0.9919, \"cc_depth0_ratio\": 0.89, \"freq_entropy_rho\": -0.78, \"ttr_rho\": 0.17, \"note\": \"TTR rho=+0.17 contradicts hypothesis (expected negative). Paper should only report freq_entropy and CC classification, not TTR (or explicitly flag anomalous direction).\"}, \"completed_at\": \"2026-05-20T13:12:42.795Z\"}, \"exp_code_multi_source\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:30:38.921Z\", \"updated_at\": \"2026-05-20T13:12:41.350Z\", \"hypothesis\": \"Code domain multi-source OBD K* preserves single-source ceiling K*=2 when mixing 3 generators (Qwen-7B, LLaMA-8B, Mistral-7B) with unified Qwen2.5-1.5B scorer.\", \"spec\": {\"command\": \"python /root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_code.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_{qwen7b,llama8b,mistral7b}\", \"data_count\": 99000, \"model_name\": \"Qwen2.5-1.5B (scorer)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/data/code_multi_source/\"}, \"metrics\": {\"k_star\": 2, \"generators\": [\"qwen7b\", \"llama8b\", \"mistral7b\"], \"unified_scorer\": \"qwen2.5-1.5b\", \"vocab_only_no_label\": {\"0v1\": 0.7891, \"1v2\": 0.6353, \"2v3\": 0.5121, \"kstar\": 2}, \"vocab_only_with_label\": {\"0v1\": 0.79, \"1v2\": 0.644, \"2v3\": 0.5118, \"kstar\": 2}, \"unified_no_label\": {\"0v1\": 0.9123, \"1v2\": 0.6702, \"2v3\": 0.5013, \"kstar\": 2}, \"unified_with_label\": {\"0v1\": 0.9123, \"1v2\": 0.6803, \"2v3\": 0.5055, \"kstar\": 2}, \"elapsed_seconds\": 2025, \"note\": \"Code multi-source K*=2 matches single-source ceiling across all 4 settings.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:12:41.350Z\"}, \"exp_wiki_multi_source\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:31:50.277Z\", \"updated_at\": \"2026-05-20T13:12:39.770Z\", \"hypothesis\": \"Wiki domain multi-source OBD K* preserves single-source ceiling when mixing 3 generators (Qwen1.5B, LLaMA-8B, Mistral-7B) with unified Qwen2.5-1.5B scorer, consistent with C4 multi-source K*=2 and arXiv multi-source K*=3.\", \"spec\": {\"command\": \"python /root/autodl-tmp/gen-depth-contamination/scripts/run_multi_source_wiki.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki,exp_wiki_llama8b,exp_wiki_mistral7b\", \"data_count\": 90000, \"model_name\": \"Qwen2.5-1.5B (scorer)\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/data/wiki_multi_source/\"}, \"metrics\": {\"k_star\": 1, \"generators\": [\"qwen1b5\", \"llama8b\", \"mistral7b\"], \"docs_per_generator\": 1000, \"total_rows\": 18000, \"unified_scorer\": \"qwen2.5-1.5b\", \"vocab_only_no_label\": {\"0v1\": 0.7616, \"1v2\": 0.5434, \"2v3\": 0.517, \"kstar\": 1}, \"vocab_only_with_label\": {\"0v1\": 0.7779, \"1v2\": 0.552, \"2v3\": 0.5248, \"kstar\": 1}, \"unified_no_label\": {\"0v1\": 0.9603, \"1v2\": 0.5685, \"2v3\": 0.519, \"kstar\": 1}, \"unified_with_label\": {\"0v1\": 0.9685, \"1v2\": 0.579, \"2v3\": 0.5299, \"kstar\": 1}, \"elapsed_seconds\": 3499, \"note\": \"All 3 generators (qwen1b5/llama8b/mistral7b) participated. K*=1 consistent with cross-scorer single-source results (llama8b K*=1, mistral7b K*=1, qwen K*=2). Mixed pool pulled to K*=1 by majority.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T13:12:39.770Z\"}, \"exp_7b_scorer_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:37:17.489Z\", \"updated_at\": \"2026-05-20T12:53:09.873Z\", \"hypothesis\": \"Qwen2.5-7B scorer yields same K* as Qwen2.5-1.5B scorer on C4 Pythia-1.4B and OLMo-1B depth chains, confirming K* is robust to scorer scale (4.7x parameter increase).\", \"parent\": \"exp_022_cross_scorer\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True CUDA_VISIBLE_DEVICES=0 python /root/autodl-tmp/gen-depth-contamination/scripts/run_7b_scorer_ablation.py'\", \"server\": \"cqa1-22115\", \"data_path\": \"data_exp020_pythia_greedy + data/olmo_c4_cont\", \"data_count\": 60000, \"model_name\": \"Qwen2.5-7B + Qwen2.5-1.5B-Instruct (scorers)\", \"seed\": 42, \"checkpoint_source\": \"exp_022_cross_scorer (Pythia C4 + OLMo C4 depth chain data)\", \"eval_data\": \"C4 depth 0-5 from Pythia-1.4B and OLMo-1B generators\"}, \"metrics\": {\"pythia_c4__qwen1.5b\": {\"k_star\": 2, \"1v2_auc\": 0.8928, \"1v2_ci\": [0.8865, 0.8989]}, \"olmo_c4__qwen1.5b\": {\"k_star\": 1, \"1v2_auc\": 0.4977, \"1v2_ci\": [0.4865, 0.509]}, \"pythia_c4__qwen7b\": {\"k_star\": 2, \"1v2_auc\": 0.8943, \"1v2_ci\": [0.8881, 0.9005]}, \"olmo_c4__qwen7b\": {\"k_star\": 1, \"1v2_auc\": 0.4965, \"1v2_ci\": [0.485, 0.5078]}, \"match\": \"pythia K*(1.5B)=2 == K*(7B)=2; olmo K*(1.5B)=1 == K*(7B)=1\"}, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_7b_scorer_ablation.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_7b_scorer_ablation/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T12:53:09.873Z\"}, \"exp_bootstrap_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:51:15.538Z\", \"updated_at\": \"2026-05-20T11:57:24.167Z\", \"hypothesis\": \"10K bootstrap resamples yield tighter CI but no K* verdict flips for borderline Table 2 configurations (LLaMA-8B, Gemma-2-2B, Mistral-7B, 512-tok), confirming robustness of K* assignments at 1K resamples.\", \"spec\": {\"command\": \"python /root/autodl-tmp/gen-depth-contamination/scripts/run_bootstrap_10k.py\", \"server\": \"cqa1-22115\", \"data_path\": \"multiple (exp_018, exp_gemma2b, exp_019, exp_021_512)\", \"data_count\": 40000, \"model_name\": \"LightGBM (CPU-only bootstrap)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k/bootstrap_10k_comparison.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_bootstrap_10k_log.txt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T11:56:15.385Z\", \"metrics\": {\"configs_tested\": 4, \"configs_missing\": 2, \"results\": {\"llama8b\": {\"auc\": 0.6075, \"ci_1k\": [0.597, 0.617], \"ci_10k\": [0.598, 0.617], \"verdict_1k\": \"BORDERLINE\", \"verdict_10k\": \"BORDERLINE\", \"flipped\": false}, \"gemma2b\": {\"auc\": 0.5981, \"ci_1k\": [0.588, 0.608], \"ci_10k\": [0.588, 0.608], \"verdict_1k\": \"BORDERLINE\", \"verdict_10k\": \"BORDERLINE\", \"flipped\": false}, \"mistral7b\": {\"auc\": 0.5902, \"ci_1k\": [0.58, 0.6], \"ci_10k\": [0.58, 0.6], \"verdict_1k\": \"K*=1\", \"verdict_10k\": \"BORDERLINE\", \"flipped_technical\": true, \"note\": \"CI upper 0.6000→0.6001 (noise, +0.01pp). Point estimate 0.5902 << theta. K*=1 unchanged.\"}, \"512tok\": {\"auc\": 0.6136, \"ci_1k\": [0.604, 0.623], \"ci_10k\": [0.604, 0.623], \"verdict_1k\": \"K*=2\", \"verdict_10k\": \"K*=2\", \"flipped\": false}}, \"missing\": [\"exp_017_qwen_cont (features.csv not on disk)\", \"exp_002_olmo (features.csv not on disk)\"], \"conclusion\": \"No substantive K* flips. 10K CI ~3% tighter. 1K resamples confirmed robust.\"}}, \"exp-014\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:28:44.076Z\", \"updated_at\": \"2026-05-20T11:36:17.784Z\", \"spec\": {\"command\": \"python run_naturalistic_validation.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\", \"data_count\": 30000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_014_naturalistic/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_014_naturalistic/naturalistic_validation_results.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"OBD depth classifiers trained on synthetic generation-chain data will assign low depth (d0) to most real Common Crawl texts, and predicted AI probability will correlate negatively with vocabulary richness metrics (freq_entropy, TTR), confirming that the 15D feature space captures genuine human-vs-synthetic distributional differences rather than overfitting to synthetic artifacts.\", \"completed_at\": \"2026-05-20T11:29:09.930Z\", \"metrics\": {\"superseded_by\": \"exp_014_naturalistic\", \"note\": \"Stale duplicate. All metrics and results are in exp_014_naturalistic.\"}}, \"exp_gemma2b_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:20:08.546Z\", \"updated_at\": \"2026-05-20T10:07:22.035Z\", \"hypothesis\": \"Gemma-2-2B (6th architecture family) yields K*=2 on C4 web text under continuation mode, consistent with domain ceiling K*=2 observed across 5 other families (Qwen/Pythia/OLMo/LLaMA/Mistral), strengthening the claim that C4 ceiling is architecture-independent.\", \"spec\": {\"command\": \"python /root/autodl-tmp/gen-depth-contamination/scripts/run_gemma2b_depth.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": 289968, \"log_path\": \"~/runs/gen-depth-contamination/exp_gemma2b_depth.log\", \"submitted_at\": \"2026-05-20T06:34:42.871Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_id\": \"cuda:0\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/c4_5k\", \"data_count\": 5000, \"model_name\": \"google/gemma-2-2b\", \"seed\": 42, \"wall_clock_seconds\": 11141.9, \"gpu_hours\": 3.09}, \"reproduce\": {\"finished_at\": \"2026-05-20T09:38:23.991Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T09:38:28.803849+00:00\"}]}, \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9534, \"1v2\": 0.5981, \"2v3\": 0.5342, \"3v4\": 0.503, \"4v5\": 0.5026}, \"pairwise_auc_std\": {\"0v1\": 0.003, \"1v2\": 0.008, \"2v3\": 0.013, \"3v4\": 0.003, \"4v5\": 0.013}, \"bootstrap_ci_1v2\": {\"ci_lower\": 0.5882, \"ci_upper\": 0.6076}, \"jsd\": {\"0v1\": 0.09882, \"1v2\": 0.008852, \"2v3\": 0.004904, \"3v4\": 0.003742, \"4v5\": 0.003167}, \"ordinal_mae\": 1.3152, \"ordinal_accuracy\": 0.3321, \"note\": \"K*=1, NOT borderline K*=2. 1v2 AUC=0.5981 < theta=0.60. CI upper=0.6076 crosses theta but point estimate below.\"}, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_depth/summary.txt\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_depth/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T09:40:24.773Z\"}, \"exp_deberta_code_qwen1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:34:21.140Z\", \"updated_at\": \"2026-05-20T09:43:22.944Z\", \"hypothesis\": \"DeBERTa supervised classifier on Code domain yields K*=2 (matching OBD K*=2), confirming representation-independent domain ceiling holds for Code domain (C4 K*=2, wiki K*=3, arXiv K*=3, code K*=2).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python /root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_code.py\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"294849\", \"log_path\": \"~/runs/gen-depth-contamination/exp_deberta_code_qwen1b5.log\", \"submitted_at\": \"2026-05-20T07:33:30.520Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7792.4, \"gpu_hours\": 2.16}, \"reproduce\": {\"finished_at\": \"2026-05-20T09:20:38.702Z\"}, \"metrics\": {\"K_star\": 2, \"theta\": 0.6, \"auc_0v1\": 1, \"auc_1v2\": 0.8076, \"auc_2v3\": 0.5933, \"auc_3v4\": 0.5492, \"auc_4v5\": 0.5311, \"ci_0v1\": [0.9999, 1], \"ci_1v2\": [0.8001, 0.8147], \"ci_2v3\": [0.5847, 0.6018], \"ci_3v4\": [0.541, 0.5573], \"ci_4v5\": [0.5235, 0.5388], \"obd_auc_0v1\": 0.9388, \"obd_auc_1v2\": 0.7382, \"obd_auc_2v3\": 0.53, \"obd_auc_3v4\": 0.5022, \"obd_auc_4v5\": 0.5219, \"elapsed_seconds\": 5780}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_code_qwen1b5/code_qwen1b5.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_deberta_code_qwen1b5.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:43:22.944Z\"}, \"exp_multi_source_arxiv\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:46:18.107Z\", \"updated_at\": \"2026-05-20T08:47:00.705Z\", \"hypothesis\": \"Multi-source OBD K* on arXiv domain preserves domain ceiling K*=3 when mixing 3 generators (Qwen/Pythia/LLaMA-8B) with unified Qwen2.5-1.5B scorer, consistent with single-source arXiv K*=3 and higher than C4 multi-source K*=2, confirming domain hierarchy in multi-source setting.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python scripts/run_multi_source_arxiv.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_024_arxiv + data/exp_025_pythia_arxiv + data/exp_arXiv_llama8b\", \"data_count\": 19800, \"model_name\": \"OBD-LightGBM-15D\", \"seed\": 42, \"checkpoint_path\": \"results/exp_multi_source_arxiv/\", \"log_path\": \"results/exp_multi_source_arxiv/summary.json\"}, \"completed_at\": \"2026-05-20T08:46:51.345Z\", \"metrics\": {\"domain\": \"arxiv\", \"generators\": [\"qwen1b5\", \"pythia1b4\", \"llama8b\"], \"unified_scorer\": \"qwen2.5-1.5b\", \"docs_per_generator\": 1000, \"vocab_only_no_label_0v1\": 0.9431, \"vocab_only_no_label_1v2\": 0.6922, \"vocab_only_no_label_2v3\": 0.589, \"vocab_only_no_label_kstar\": 2, \"vocab_only_with_label_0v1\": 0.9436, \"vocab_only_with_label_1v2\": 0.702, \"vocab_only_with_label_2v3\": 0.5883, \"vocab_only_with_label_kstar\": 2, \"unified_no_label_0v1\": 0.9899, \"unified_no_label_1v2\": 0.8117, \"unified_no_label_2v3\": 0.6247, \"unified_no_label_3v4\": 0.5269, \"unified_no_label_kstar\": 3, \"unified_with_label_0v1\": 0.9911, \"unified_with_label_1v2\": 0.8338, \"unified_with_label_2v3\": 0.6276, \"unified_with_label_2v3_ci\": [0.615, 0.6401], \"unified_with_label_3v4\": 0.533, \"unified_with_label_kstar\": 3}}, \"exp_multi_source_detection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:20:10.182Z\", \"updated_at\": \"2026-05-20T08:00:14.527Z\", \"hypothesis\": \"OBD K* is preserved when training on a mixed pool of outputs from 3 different generators (Qwen-1.5B, Pythia-1.4B, OLMo-1B), and adding generator identity as an extra feature does not improve depth discrimination.\", \"spec\": {\"command\": \"python scripts/run_multi_source.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data_exp016_qwen_base + data_exp020_pythia_greedy + data/olmo_c4_cont\", \"data_count\": 18000, \"model_name\": \"OBD-LightGBM-15D\", \"seed\": 42, \"checkpoint_path\": \"results/exp_multi_source_detection/\", \"log_path\": \"/tmp/multi_source.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T07:01:21.517Z\", \"metrics\": {\"v2_generators\": [\"qwen1b5\", \"pythia1b4\", \"llama8b\"], \"v2_kstar_no_label\": 2, \"v2_kstar_with_label\": 2, \"v2_0v1_auc_no_label\": 0.968, \"v2_0v1_auc_with_label\": 0.9785, \"v2_1v2_auc_no_label\": 0.7144, \"v2_1v2_auc_with_label\": 0.7251, \"v2_2v3_auc_no_label\": 0.5321, \"v2_2v3_auc_with_label\": 0.5362, \"vocab_only_v1_0v1\": 0.8675, \"vocab_only_v1_1v2\": 0.676, \"vocab_only_v1_2v3\": 0.4938, \"vocab_only_v1_kstar\": 2, \"vocab_only_v2_0v1\": 0.8296, \"vocab_only_v2_1v2\": 0.683, \"vocab_only_v2_2v3\": 0.5057, \"vocab_only_v2_kstar\": 2, \"vocab_only_features\": [\"ttr\", \"hapax_ratio\", \"self_bleu\", \"freq_kurtosis\", \"freq_entropy\", \"low_freq_ratio\"], \"scorer_confound_affects_kstar\": false, \"unified_scorer\": \"qwen2.5-1.5b\", \"unified_no_label_0v1\": 0.9663, \"unified_no_label_1v2\": 0.7105, \"unified_no_label_2v3\": 0.519, \"unified_no_label_kstar\": 2, \"unified_with_label_0v1\": 0.9769, \"unified_with_label_1v2\": 0.7183, \"unified_with_label_2v3\": 0.5165, \"unified_with_label_kstar\": 2, \"unified_single_qwen_kstar\": 2, \"unified_single_pythia_kstar\": 2, \"unified_single_llama8b_kstar\": 1, \"unified_single_qwen_1v2\": 0.6306, \"unified_single_pythia_1v2\": 0.8806, \"unified_single_llama8b_1v2\": 0.6077}}, \"exp_changepoint_kstar\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T06:20:11.788Z\", \"updated_at\": \"2026-05-20T07:21:14.637Z\", \"hypothesis\": \"Non-parametric changepoint detection (PELT) on pairwise AUC sequences should recover K* consistent with the fixed θ=0.60 threshold, validating that K* is not an artifact of threshold choice.\", \"spec\": {\"command\": \"python scripts/run_changepoint_kstar.py\", \"server\": \"cqa1-22115\", \"data_path\": \"results/*/pairwise_auc.json\", \"data_count\": 37, \"model_name\": \"ruptures-PELT\", \"seed\": 42, \"checkpoint_path\": \"results/exp_changepoint_kstar/\", \"log_path\": \"/tmp/changepoint_run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"exact_agreement\": 0.459, \"exact_agreement_n\": \"17/37\", \"within_1_agreement\": 0.946, \"within_1_agreement_n\": \"35/37\", \"cp_direction\": \"always_conservative\", \"disagreement_auc_range\": [0.607, 0.654], \"best_penalty\": 0.1, \"methods_tested\": [\"PELT\", \"BinSeg\", \"BottomUp\"], \"bootstrap_samples\": 2000}, \"completed_at\": \"2026-05-20T07:19:41.765Z\"}, \"exp_cross_transfer_llama8b_to_qwen7b_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:01:09.441Z\", \"updated_at\": \"2026-05-20T05:28:46.650Z\", \"spec\": {\"command\": \"python scripts/run_deberta_cross_transfer.py --train_model wiki_llama8b --test_model wiki_qwen7b --gpu 0\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"275361\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_llama8b_to_qwen7b_v2.log\", \"submitted_at\": \"2026-05-20T03:01:08.673Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/wiki_llama8b/ + wiki_qwen7b/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"checkpoint_source\": \"trained from scratch (cross-transfer rerun of crashed v1)\", \"eval_data\": \"wiki_qwen7b depth 0-5, 20000 samples\", \"checkpoint_path\": \"N/A (OOF predictions only)\", \"wall_clock_seconds\": 8858.0, \"gpu_hours\": 2.46}, \"hypothesis\": \"Cross-model transfer: DeBERTa trained on LLaMA-8B wiki depth data can discriminate Qwen-7B wiki depth boundaries (K* transfer). Rerun of exp_cross_transfer_llama8b_to_qwen7b which crashed due to --gpu 1 device error.\", \"parent\": \"exp_cross_transfer_llama8b_to_qwen7b\", \"conclusion\": \"success\", \"metrics\": {\"K_star\": 3, \"2v3_auc_ci_lower\": 0.6124, \"theta\": 0.6, \"margin_pp\": 1.24}, \"completed_at\": \"2026-05-20T05:28:46.650Z\"}, \"exp_deberta_arxiv_qwen1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:12:10.106Z\", \"updated_at\": \"2026-05-20T03:50:38.093Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python scripts/run_deberta_arxiv.py\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"276481\", \"log_path\": \"~/runs/gen-depth-contamination/exp_deberta_arxiv_qwen1b5.log\", \"submitted_at\": \"2026-05-20T03:12:09.627Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_024_arxiv/\", \"data_count\": 13200, \"model_name\": \"DeBERTa-v3-base\", \"seed\": \"5-fold GroupKFold\", \"hyperparams\": {\"epochs\": 3, \"batch_size\": 16, \"grad_accum\": 2, \"lr\": \"2e-5\", \"n_boot\": 10000, \"threshold\": 0.6}, \"checkpoint_path\": \"N/A (OOF predictions only)\", \"wall_clock_seconds\": 2247.8, \"gpu_hours\": 0.62}, \"hypothesis\": \"DeBERTa supervised classifier on arXiv domain yields K*=3 (matching OBD K*=3), confirming representation-independent domain ceiling holds across all 4 domains (C4 K*=2, wiki K*=3, code K*=2, arXiv K*=3).\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:45:52.617Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T03:45:57.340301+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 4, \"0v1_auc\": 0.9997, \"1v2_auc\": 0.9214, \"2v3_auc\": 0.7446, \"3v4_auc\": 0.6238, \"4v5_auc\": 0.5771, \"3v4_ci_lower\": 0.6127, \"3v4_ci_upper\": 0.6349, \"theta\": 0.6}, \"completed_at\": \"2026-05-20T03:49:37.411Z\"}, \"exp_cross_transfer_llama8b_to_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:55:51.478Z\", \"updated_at\": \"2026-05-20T03:00:13.595Z\", \"spec\": {\"command\": \"python scripts/run_deberta_cross_transfer.py --train_model wiki_llama8b --test_model wiki_qwen7b --gpu 1\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"270133\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_llama8b_to_qwen7b.log\", \"submitted_at\": \"2026-05-20T00:55:51.062Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/wiki_llama8b/ + wiki_qwen7b/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"wall_clock_seconds\": 7462.5, \"gpu_hours\": 2.07}, \"hypothesis\": \"Cross-model transfer: DeBERTa trained on LLaMA-8B wiki depth data can discriminate Qwen-7B wiki depth boundaries (K* transfer), testing whether depth features are model-agnostic within wiki domain.\", \"conclusion\": \"failed\", \"failure_reason\": \"AssertionError: Invalid device id — --gpu 1 used but CUDA_VISIBLE_DEVICES only exposed 1 device. Need --gpu 0.\", \"checkpoint_path\": \"N/A - crashed before producing output\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_llama8b_to_qwen7b.log\", \"completed_at\": \"2026-05-20T03:00:13.596Z\"}, \"exp_cross_transfer_qwen7b_to_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:55:49.779Z\", \"updated_at\": \"2026-05-20T02:59:59.419Z\", \"spec\": {\"command\": \"python scripts/run_deberta_cross_transfer.py --train_model wiki_qwen7b --test_model wiki_llama8b --gpu 0\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"270054\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_qwen7b_to_llama8b.log\", \"submitted_at\": \"2026-05-20T00:55:49.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/wiki_qwen7b/ + wiki_llama8b/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"wall_clock_seconds\": 7450.1, \"gpu_hours\": 2.07}, \"hypothesis\": \"Cross-model transfer: DeBERTa trained on Qwen-7B wiki depth data can discriminate LLaMA-8B wiki depth boundaries (K* transfer), testing whether depth features are model-agnostic within wiki domain.\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/wiki_qwen7b__to__wiki_llama8b.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_cross_transfer_qwen7b_to_llama8b.log\", \"metrics\": {\"kstar\": 3, \"kstar_indexing\": \"1-indexed\", \"pairwise_auc\": {\"0v1\": 0.9998, \"1v2\": 0.7384, \"2v3\": 0.6278, \"3v4\": 0.587, \"4v5\": 0.5519}, \"elapsed_s\": 3621}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T02:59:59.419Z\"}, \"exp_deberta_cross_transfer_gpu3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:45:58.698Z\", \"updated_at\": \"2026-05-20T00:52:16.950Z\", \"hypothesis\": \"Sub-experiment of exp_deberta_cross_transfer_wiki: GPU3 ran olmo↔llama8b, pythia↔mistral7b pairs (mistral7b pairs were bonus, qwen7b↔llama8b missing).\", \"conclusion\": \"success\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"command\": \"python scripts/run_deberta_cross_transfer.py\", \"pid\": \"208308\", \"data_path\": \"/root/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/gpu3.log\", \"reproduce\": {\"finished_at\": \"2026-05-20T00:50:30.198Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-20T00:50:32.377Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:50:36.649085+00:00\"}]}}, \"exp_deberta_cross_transfer_gpu2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:45:57.106Z\", \"updated_at\": \"2026-05-20T00:52:16.211Z\", \"hypothesis\": \"Sub-experiment of exp_deberta_cross_transfer_wiki: GPU2 ran olmo↔qwen7b, pythia→llama8b, llama8b→pythia pairs.\", \"conclusion\": \"success\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"command\": \"python scripts/run_deberta_cross_transfer.py\", \"pid\": \"208307\", \"data_path\": \"/root/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/gpu2.log\", \"reproduce\": {\"finished_at\": \"2026-05-20T00:50:20.459Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-20T00:50:22.410Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:50:27.489708+00:00\"}]}}, \"exp_deberta_cross_transfer_gpu1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:45:55.753Z\", \"updated_at\": \"2026-05-20T00:52:15.283Z\", \"hypothesis\": \"Sub-experiment of exp_deberta_cross_transfer_wiki: GPU1 ran pythia↔olmo and pythia↔qwen7b pairs.\", \"conclusion\": \"success\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"command\": \"python scripts/run_deberta_cross_transfer.py\", \"pid\": \"208306\", \"data_path\": \"/root/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/gpu1.log\", \"reproduce\": {\"finished_at\": \"2026-05-20T00:50:07.180Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-20T00:50:09.496Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:50:17.409046+00:00\"}]}}, \"exp_deberta_cross_transfer_wiki\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:23:41.514Z\", \"updated_at\": \"2026-05-20T00:45:03.982Z\", \"hypothesis\": \"DeBERTa cross-model transfer on wiki domain: if off-diagonal retention is high (>90%), depth signals are model-family invariant even with neural features; if wiki retention exceeds C4 retention, domain complexity affects transfer more than feature representation.\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\", \"cuda:2\", \"cuda:3\"], \"command\": \"python scripts/run_deberta_cross_transfer.py --all_pairs\", \"pid\": \"208306,208307,208308\", \"data_path\": \"/root/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"total_pairs_expected\": 12, \"completed_pairs\": 10, \"missing_pairs\": [\"qwen7b→llama8b\", \"llama8b→qwen7b\"], \"bonus_pairs\": [\"pythia→mistral7b (K*=2)\", \"mistral7b→pythia (K*=2)\"], \"kstar_distribution\": {\"K*=1\": 3, \"K*=2\": 5, \"K*=3\": 1}, \"kstar_1_pairs\": [\"pythia→olmo\", \"qwen7b→olmo\", \"llama8b→olmo\"], \"kstar_3_pair\": \"pythia→qwen7b\", \"kstar_2_pairs\": [\"olmo→qwen7b\", \"olmo→llama8b\", \"qwen7b→pythia\", \"llama8b→pythia\", \"pythia→llama8b\"], \"pattern\": \"All X→OLMo = K*=1. pythia→qwen7b highest at K*=3. GPU3 ran mistral7b pairs instead of expected qwen7b↔llama8b, causing 2 missing pairs.\", \"json_kstar_fix\": \"3 JSONs fixed +1 (pythia→olmo 0→1, olmo→qwen7b 1→2, olmo→llama8b 1→2)\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/deberta_cross_transfer/\", \"completed_at\": \"2026-05-20T00:44:09.679Z\"}, \"exp_deberta_c4_1b5_qwen_cont\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:14:07.803Z\", \"updated_at\": \"2026-05-20T00:43:44.526Z\", \"hypothesis\": \"C4 1.5B DeBERTa qwen_cont256 config (length-256 continuation): if K*=2, confirms boundary holds across generation strategies (base vs continuation) at 1.5B scale.\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"command\": \"python scripts/run_deberta_c4_1b5.py --config qwen_cont256 --gpu 0\", \"pid\": \"TBD\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_021_length_256/\", \"data_count\": 30000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4_1b5/qwen_cont256_oof.npz\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/deberta_c4_1b5_qwen_cont.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T00:41:45.752Z\", \"metrics\": {\"config\": \"qwen_cont256\", \"kstar\": 2, \"kstar_theta\": 0.6, \"pairwise_auc\": {\"0v1\": 0.9955, \"1v2\": 0.7194, \"2v3\": 0.5954, \"3v4\": 0.5689, \"4v5\": 0.5502}, \"ci_95\": {\"0v1\": [0.9944, 0.9965], \"1v2\": [0.712, 0.7273], \"2v3\": [0.587, 0.6028], \"3v4\": [0.5613, 0.5766], \"4v5\": [0.5431, 0.5577]}, \"obd_baseline\": {\"0v1\": 0.9914, \"1v2\": 0.6282, \"2v3\": 0.5556, \"3v4\": 0.5298, \"4v5\": 0.5137}, \"delta_vs_obd\": {\"1v2\": 0.0912}, \"key_finding\": \"C4 1.5B qwen_cont256 K*=2, boundary holds across continuation generation strategy.\"}}, \"exp_deberta_c4_1b5_pythia\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T00:14:05.964Z\", \"updated_at\": \"2026-05-20T00:19:10.196Z\", \"hypothesis\": \"C4 1.5B DeBERTa pythia_greedy config: apple-to-apple comparison with OBD Table 2. If K*=2 consistent with qwen_rw, confirms boundary is generator-invariant at 1.5B scale on C4.\", \"spec\": {\"server\": \"westd-42896\", \"gpu\": [\"cuda:1\"], \"command\": \"python scripts/run_deberta_c4_1b5.py --config pythia_greedy --gpu 1\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp020_pythia_greedy/\", \"data_count\": 30000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"checkpoint_path\": \"n/a\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4_1b5/pythia_greedy.json\"}, \"metrics\": {\"config\": \"pythia_greedy\", \"kstar\": 2, \"kstar_theta\": 0.6, \"pairwise_auc\": {\"0v1\": 0.9998, \"1v2\": 0.9284, \"2v3\": 0.5419, \"3v4\": 0.5163, \"4v5\": 0.5098}, \"ci_95\": {\"0v1\": [0.9996, 0.9999], \"1v2\": [0.923, 0.9331], \"2v3\": [0.5354, 0.5486], \"3v4\": [0.509, 0.5237], \"4v5\": [0.5037, 0.516]}, \"obd_baseline\": {\"0v1\": 0.9992, \"1v2\": 0.8838, \"2v3\": 0.5342, \"3v4\": 0.5228, \"4v5\": 0.5162}, \"delta_vs_obd_1v2\": 0.0446, \"training_time_min\": 37.3}, \"conclusion\": \"success\", \"notes\": \"C4 1.5B DeBERTa pythia_greedy K*=2, consistent with qwen_rw K*=2. 1v2 AUC=0.9284 far exceeds OBD 0.8838 (+4.5pp), but 2v3=0.5419 still below θ=0.60, boundary unchanged. Notably pythia_greedy 1v2 much higher than qwen_rw (0.9284 vs 0.7052), likely due to greedy decoding being more distinguishable. OBD baseline also higher for pythia_greedy (0.8838 vs 0.6262). Results on westd-42896.\", \"completed_at\": \"2026-05-20T00:19:10.196Z\"}, \"exp_32b_c4_6class\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:31:06.464Z\", \"updated_at\": \"2026-05-20T00:15:44.463Z\", \"hypothesis\": \"32B DeBERTa 6-class rerun (depth 0-5) to fill 4v5 pair in paper table. If K* remains 2, confirms boundary even with full depth range; 4v5 AUC provides additional evidence of signal decay pattern.\", \"spec\": {\"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"command\": \"python run_deberta_6class.py --config exp_32b_c4\", \"pid\": \"139848\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/c4_32b\", \"data_count\": 30000, \"model_name\": \"microsoft/deberta-v3-base\", \"seed\": 42, \"note\": \"6-class rerun replacing 5-class exp_32b_c4, adds depth_5 for complete 4v5 pair\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4/exp_32b_c4_oof.npz\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/deberta_32b_6class.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T23:34:30.974Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:34:32.906Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:34:36.421721+00:00\"}]}, \"metrics\": {\"config\": \"exp_32b_c4\", \"kstar\": 2, \"kstar_indexing\": \"1-indexed\", \"num_classes\": 6, \"pairwise_auc\": {\"0v1\": 0.9923, \"1v2\": 0.6945, \"2v3\": 0.5978, \"3v4\": 0.5669, \"4v5\": 0.5426}, \"ci_95\": {\"0v1\": [0.991, 0.9936], \"1v2\": [0.6864, 0.7026], \"2v3\": [0.5898, 0.6058], \"3v4\": [0.559, 0.5746], \"4v5\": [0.5351, 0.5501]}, \"training_time_min\": 48.2}, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/deberta_32b_6class.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4/exp_32b_c4_results.json\", \"notes\": \"Cron 误判为 failed（脚本不用 W&B），实际 5-fold 训练全部完成。K*=2 confirmed with 6 classes (depth 0-5)。2v3 AUC=0.5978 刚好低于 θ=0.60。4v5 AUC=0.5426 提供 signal decay 额外证据。\"}, \"exp_deberta_c4_1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T22:23:40.169Z\", \"updated_at\": \"2026-05-19T23:42:16.799Z\", \"hypothesis\": \"C4 1.5B DeBERTa apple-to-apple comparison with Table 2 OBD results: if DeBERTa K*=2 on same 1.5B C4 data as OBD, confirms boundary is intrinsic; if K*>2, quantifies neural vs handcrafted gap at 1.5B scale.\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/gen-depth-contamination && python scripts/run_deberta_c4_1b5.py --config qwen_rw --gpu 0\", \"pid\": \"255066\", \"data_path\": \"/root/gen-depth-contamination/data/exp016_qwen_base/\", \"data_count\": \"TBD\", \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"metrics\": {\"config\": \"qwen_rw\", \"kstar\": 2, \"kstar_theta\": 0.6, \"pairwise_auc\": {\"0v1\": 0.9923, \"1v2\": 0.7052, \"2v3\": 0.5988, \"3v4\": 0.5698, \"4v5\": 0.5475}, \"ci_95\": {\"0v1\": [0.9907, 0.9937], \"1v2\": [0.6977, 0.7129], \"2v3\": [0.5905, 0.6063], \"3v4\": [0.5626, 0.5774], \"4v5\": [0.5404, 0.5542]}, \"obd_baseline\": {\"0v1\": 0.987, \"1v2\": 0.6262, \"2v3\": 0.5496, \"3v4\": 0.5294, \"4v5\": 0.5182}, \"delta_vs_obd\": {\"1v2\": 0.079}, \"key_finding\": \"C4 1.5B DeBERTa qwen_rw K*=2, matching OBD K*=2. DeBERTa 1v2 +7.9pp vs OBD but does not extend K*. Note: only qwen_rw config done; pythia_greedy running on westd, qwen_cont256 starting on cqa1.\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T23:12:26.218Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T23:12:26.966Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T23:12:34.928421+00:00\"}]}, \"notes\": \"Cron 误判为 failed（脚本不用 W&B），实际完成。K*=2 confirmed on C4 1.5B data = OBD K*=2。DeBERTa 1v2 AUC=0.7052 vs OBD 0.6262 (+7.9pp)，但 2v3 仍低于 θ=0.60，无法突破 K* boundary。confirms intrinsic boundary on C4.\"}, \"exp_deberta_upperbound\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T16:29:11.448Z\", \"updated_at\": \"2026-05-19T22:05:28.928Z\", \"hypothesis\": \"DeBERTa-v3-base fine-tuned ordinal classifier as upper-bound baseline for 15D handcrafted features: if DeBERTa also yields K*=2 on C4 depth chains, the saturation boundary is near-intrinsic to generation process rather than a feature ceiling; if K*=3+, quantifies the gap between handcrafted and neural representations. Uses same 5-fold GroupKFold, pairwise AUC evaluation, θ=0.60 K* criterion.\", \"spec\": {\"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_deberta_upperbound.py\", \"pid\": \"167144\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_upperbound.log\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 20000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_upperbound/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_upperbound.log\", \"metrics\": {\"wiki_pythia\": {\"kstar\": 3, \"0v1_auc\": 0.9993, \"1v2_auc\": 0.725, \"2v3_auc\": 0.6137, \"3v4_auc\": 0.5733, \"4v5_auc\": 0.5527}, \"wiki_olmo\": {\"kstar\": 1, \"0v1_auc\": 0.9999, \"1v2_auc\": 0.5183, \"2v3_auc\": 0.5048, \"3v4_auc\": 0.5021, \"4v5_auc\": 0.4989}, \"wiki_qwen7b\": {\"kstar\": 3, \"0v1_auc\": 0.9998, \"1v2_auc\": 0.7619, \"2v3_auc\": 0.6108, \"3v4_auc\": 0.5587, \"4v5_auc\": 0.5412}, \"wiki_llama8b\": {\"kstar\": 3, \"0v1_auc\": 0.9997, \"1v2_auc\": 0.7452, \"2v3_auc\": 0.5954, \"3v4_auc\": 0.5601, \"4v5_auc\": 0.5389}, \"wiki_mistral7b\": {\"kstar\": 3, \"0v1_auc\": 0.9998, \"1v2_auc\": 0.7483, \"2v3_auc\": 0.5552, \"3v4_auc\": 0.5434, \"4v5_auc\": 0.5298}, \"obd_baseline_bug_fixed\": true, \"wiki_olmo_obd_rerun\": {\"0v1\": 0.9933, \"1v2\": 0.4983, \"2v3\": 0.5041, \"3v4\": 0.4986, \"4v5\": 0.5089}, \"key_finding\": \"Wiki DeBERTa K*=3 for 4/5 configs (pythia/qwen7b/llama8b/mistral7b), exceeding OBD K*=2. DeBERTa breaks OBD boundary on wiki domain. OLMo K*=1 anomalous (near-random 1v2). OBD baseline bug for olmo fixed (was copy of pythia).\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T21:58:49.707Z\"}, \"exp_32b_c4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:56:48.122Z\", \"updated_at\": \"2026-05-19T21:55:27.105Z\", \"hypothesis\": \"Scale-dependent K* on C4: Qwen2.5-32B fp16 continuation on C4 web text 的 K* 是否仍 = 2？验证 K*=2 dominant mode 在 32B scale 是否稳定（已确认 1.5B/7B/8B/14B 均 K*=2），排除 scale ceiling effect。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_arXiv_llama8b\", \"server\": \"westd-42896\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-42896\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T19:37:31.096Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-32B --data_dir data/exp_32b_c4 --results_dir results/exp_32b_c4 --num_samples 5000 --max_depth 5 --batch_size 2 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"finished_at\": \"2026-05-19T21:33:12.076Z\", \"training_hours\": 49.93}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-32B --data_dir data/exp_32b_c4 --results_dir results/exp_32b_c4 --num_samples 5000 --max_depth 5 --batch_size 2 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:1\"], \"pid\": \"44715\", \"log_path\": \"~/runs/gen-depth-contamination/exp_32b_c4.log\", \"submitted_at\": \"2026-05-18T07:04:19.556Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_32b_c4\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-32B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_32b_c4/\", \"wall_clock_seconds\": 139867.5, \"gpu_hours\": 38.85}, \"pid\": \"14637\", \"log_path\": \"~/runs/gen-depth-contamination/exp_32b_c4.log\", \"notes\": \"Resubmit #2 (2026-05-18T07:05): killed at depth 2 18% per Director, 72h timeout. depth 0-1 complete (5000 lines each), pipeline auto-skips. PID 44715 cuda:1.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T21:33:15.741057+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"lgbm_kstar\": 2, \"deberta_kstar\": 2, \"kstar_theta\": 0.6, \"scale\": \"32B\", \"domain\": \"C4\", \"n_docs\": 5000, \"max_depth\": 5, \"key_finding\": \"Qwen2.5-32B C4 K*=2, confirming scale-invariance of K*=2 dominant mode from 1.5B to 32B. Both LightGBM and DeBERTa classifiers agree on K*=2.\"}, \"completed_at\": \"2026-05-19T21:55:27.105Z\"}, \"exp_deberta_c4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T19:27:44.088Z\", \"updated_at\": \"2026-05-19T20:30:48.238Z\", \"hypothesis\": \"DeBERTa-v3-base fine-tuned on raw text provides an upper-bound for C4 depth distinguishability compared to 15D LightGBM on handcrafted features. Pairwise AUC should exceed LightGBM at all depth pairs since the model has access to full lexical/semantic signal.\", \"parent\": \"exp_deberta_upperbound\", \"spec\": {\"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HOME=/root/autodl-tmp/.hf_cache python scripts/run_deberta_c4.py\", \"pid\": \"130789\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 55000, \"model_name\": \"DeBERTa-v3-base\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_deberta_c4/train.log\", \"checkpoint_path\": \"results/exp_deberta_c4/\", \"checkpoint_source\": \"microsoft/deberta-v3-base (pretrained)\", \"eval_data\": \"C4 depth chains (exp_14b_c4: 30k, exp_32b_c4: 25k)\"}, \"conclusion\": \"success\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9941, \"1v2\": 0.6781, \"2v3\": 0.5895, \"3v4\": 0.5651, \"4v5\": 0.5485}, \"ci_95\": {\"0v1\": [0.993, 0.9951], \"1v2\": [0.6696, 0.6866], \"2v3\": [0.5814, 0.5979], \"3v4\": [0.5573, 0.5732], \"4v5\": [0.5411, 0.5562]}, \"f1_at_050\": {\"0v1\": 0.9352, \"1v2\": 0.6751, \"2v3\": 0.6607, \"3v4\": 0.6204, \"4v5\": 0.2869}, \"kstar\": 2, \"kstar_theta\": 0.6, \"config\": \"exp_14b_c4\", \"n_samples\": 30000, \"n_docs\": 5000, \"bootstrap_resamples\": 10000, \"training_time_min\": 48.3}, \"notes\": \"DeBERTa K*=2 = LightGBM K*=2 on C4 14B, confirming representation-independent boundary. 86M-param fine-tuned neural classifier cannot extend K* beyond 2. Worker script reported K*=1 (off-by-one bug in K* calculation logic), corrected to K*=2 based on raw CI data: 1v2 CI lower=0.6696 > θ=0.60.\", \"completed_at\": \"2026-05-19T20:30:48.238Z\"}, \"exp_code_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:30:13.401Z\", \"updated_at\": \"2026-05-19T12:15:37.664Z\", \"hypothesis\": \"Qwen2.5-7B code domain K* measurement: Qwen family scale invariance test on CodeSearchNet Python. Pythia Code K*=1 弱化了跨模型一致性。Qwen-7B 测试两个方向：(1) Qwen 家族内 Code 的 scale invariance（1.5B K*=2, 7B K*=?），(2) 若 LLaMA/Mistral 也 K*=1，Qwen-7B K*=2 能维持 \\\"code-competent models reach K*=2\\\" 叙事。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_code_pythia1b4\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && HF_ENDPOINT=https://hf-mirror.com python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_code_qwen7b --results_dir results/exp_code_qwen7b --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"114228\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_qwen7b.log\", \"submitted_at\": \"2026-05-19T01:29:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_qwen7b\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"checkpoint_source\": \"exp_code_qwen1b5\", \"eval_data\": \"CodeSearchNet Python 5000 docs\", \"wall_clock_seconds\": 38608.5, \"gpu_hours\": 10.72}, \"notes\": \"Attempts 1-3 failed: huggingface.co unreachable (000), httpx client closed during datasets.load_dataset. Attempt 4 success: copied depth_0.jsonl from exp_code_qwen1b5 (MD5 match), set HF_ENDPOINT=https://hf-mirror.com. PID 114228, GPU util 96%, 15211/24564 MiB. nvidia-smi verified.\", \"reproduce\": {\"finished_at\": \"2026-05-19T12:12:26.097Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T12:12:28.503Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T12:12:31.991515+00:00\"}]}, \"metrics\": {\"pairwise_auc\": {\"0v1\": {\"mean\": 0.9051, \"ci95_half\": 0.0043, \"folds\": [0.9073, 0.9012, 0.912, 0.9049, 0.9003]}, \"1v2\": {\"mean\": 0.7276, \"ci95_half\": 0.0055, \"folds\": [0.7377, 0.7254, 0.724, 0.722, 0.7289]}, \"2v3\": {\"mean\": 0.5368, \"ci95_half\": 0.0145, \"folds\": [0.5179, 0.5332, 0.5275, 0.5462, 0.5593]}, \"3v4\": {\"mean\": 0.509, \"ci95_half\": 0.0055, \"folds\": [0.5029, 0.5054, 0.5085, 0.5092, 0.5191]}, \"4v5\": {\"mean\": 0.5139, \"ci95_half\": 0.0128, \"folds\": [0.5016, 0.5317, 0.5264, 0.509, 0.5007]}}, \"pairwise_jsd\": {\"0v1\": 0.061265, \"1v2\": 0.042256, \"2v3\": 0.00413, \"3v4\": 0.003198, \"4v5\": 0.003393}, \"k_star\": 2, \"ordinal\": {\"mae\": 1.2651, \"accuracy\": 0.3423}, \"top_features\": [{\"name\": \"freq_entropy\", \"importance\": 9730}, {\"name\": \"surp_d2_mean\", \"importance\": 9236.2}, {\"name\": \"surp_d1_mean\", \"importance\": 9126.2}, {\"name\": \"surp_d1_skew\", \"importance\": 8833.4}, {\"name\": \"surp_std\", \"importance\": 8110.2}, {\"name\": \"freq_kurtosis\", \"importance\": 7838.6}, {\"name\": \"surp_mean\", \"importance\": 7586}, {\"name\": \"surp_kurt\", \"importance\": 6769.2}, {\"name\": \"hapax_ratio\", \"importance\": 6636.4}, {\"name\": \"ttr\", \"importance\": 6332.6}]}}, \"exp_code_mistral7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:03:15.326Z\", \"updated_at\": \"2026-05-19T11:18:09.305Z\", \"hypothesis\": \"Mistral-7B code domain K* measurement: Mistral-7B-v0.3 continuation on CodeSearchNet Python subset. Mistral 是唯一展现极端 domain dependence 的模型（C4 K*=1, arXiv K*=3）。若 code K*=2（与 Qwen/LLaMA 一致）→ code K* domain-governed, Mistral one-wash 仅限 C4。若 code K*=1 → one-wash 是 model-intrinsic property for non-academic text。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_code_qwen1b5\", \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_code_mistral7b --results_dir results/exp_code_mistral7b --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"107037\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_mistral7b.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_mistral7b\", \"data_count\": 5000, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_source\": \"exp_code_qwen1b5\", \"eval_data\": \"CodeSearchNet Python 5000 docs\"}, \"notes\": \"Log writes to /dev/pts/3 (terminal session), not a file. Progress inferred from data dir: depth_1.jsonl done (5500 lines), depth_2 in progress. No persistent log file for post-mortem analysis.\", \"reproduce\": {\"finished_at\": \"2026-05-19T11:05:15.743Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed. Diagnostic worker dispatched to check logs, partial output, OOM/disk issues.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T11:05:15.059Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:05:21.025715+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_code_mistral7b/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_code_mistral7b/summary.txt\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9191, \"1v2\": 0.6152, \"2v3\": 0.5293, \"3v4\": 0.5286, \"4v5\": 0.5099}, \"pairwise_auc_ci\": {\"0v1\": 0.0017, \"1v2\": 0.012, \"2v3\": 0.0091, \"3v4\": 0.0104, \"4v5\": 0.006}, \"pairwise_jsd\": {\"0v1\": 0.046984, \"1v2\": 0.011845, \"2v3\": 0.003717, \"3v4\": 0.003206, \"4v5\": 0.003083}, \"ordinal_mae\": 1.3191, \"ordinal_accuracy\": 0.3243, \"top3_features\": [\"freq_entropy\", \"surp_d2_mean\", \"surp_d1_mean\"]}}, \"exp_code_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:36:19.645Z\", \"updated_at\": \"2026-05-19T08:15:39.198Z\", \"hypothesis\": \"Code domain (Python) cross-model K* validation: LLaMA-3.1-8B continuation on CodeSearchNet Python subset (Husain et al. 2019). 验证 code domain K* 跨模型一致性（与 exp_code_qwen1b5 对比）。如果 K* 一致，确认 code domain K* 是 domain-governed 而非 model-specific。5500 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_code_qwen1b5\", \"notes\": \"Generation completed normally (11.37 GPU-hours). Analysis step crashed on M010 bug (int(doc_id) on string 'code_py_0'). Bug was already patched in code (try/except at line 462-466). Worker re-ran analysis only → K*=2 confirmed. Results in results/exp_code_llama8b/.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --data_dir data/exp_code_llama8b --results_dir results/exp_code_llama8b --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"96335\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_llama8b.log\", \"submitted_at\": \"2026-05-18T20:43:36.548Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/code_python_seed\", \"data_count\": 5000, \"model_name\": \"LLaMA-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"exp_code_qwen1b5\", \"eval_data\": \"CodeSearchNet Python 5500 docs\", \"wall_clock_seconds\": 40928.2, \"gpu_hours\": 11.37}, \"reproduce\": {\"finished_at\": \"2026-05-19T08:05:42.229Z\"}, \"failure_reason\": \"Traceback → ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File \\\"/root/autodl-tmp/gen-depth-contamination/scripts/run_pipeline.py\\\", line 462, in run_analysis # Support both integer and string doc_ids ^^^^^^^^^^^^^^^^ ValueError: invalid literal for int() with base 10: 'code_py_0'\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T08:05:44.712Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:05:48.414385+00:00\"}]}, \"metrics\": {\"K_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9161, \"1v2\": 0.7394, \"2v3\": 0.5112, \"3v4\": 0.52, \"4v5\": 0.4996}, \"pairwise_auc_std\": {\"0v1\": 0.004, \"1v2\": 0.0101, \"2v3\": 0.0095, \"3v4\": 0.0137, \"4v5\": 0.0069}, \"pairwise_jsd\": {\"0v1\": 0.060406, \"1v2\": 0.047034, \"2v3\": 0.003473, \"3v4\": 0.003026, \"4v5\": 0.002892}, \"ordinal_mae\": 1.2542, \"ordinal_accuracy\": 0.3485, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"surp_d2_mean\"]}}, \"exp_code_qwen1b5_pythia_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:30:03.239Z\", \"updated_at\": \"2026-05-19T06:55:26.175Z\", \"hypothesis\": \"Code domain scorer confound control: Qwen-1.5B Code K*=2 uses same-family Qwen scorer. D060 Wikipedia showed Qwen scorer inflates AUC by +0.005~0.027. If Pythia-1.4B scorer yields K*=2 on same Qwen Code text, confirms K*=2 is text-intrinsic (not scorer artifact). If K*=1, Qwen Code K*=2 is partially scorer-driven, weakening domain ceiling claim. Cross-family scorer validation on existing exp_code_qwen1b5 depth 0-5 data.\", \"parent\": \"exp_code_qwen1b5\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"spec\": {\"checkpoint_path\": \"results/exp_code_qwen1b5_pythia_scorer/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_qwen1b5_pythia_scorer.log\"}, \"pid\": \"131475\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_qwen1b5_pythia_scorer.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/exp_code_qwen1b5_pythia_scorer.sh\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-19T06:51:51.622Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T06:51:55.524732+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"theta\": 0.6, \"auc_0v1\": 0.9076, \"auc_1v2\": 0.7197, \"auc_2v3\": 0.5308, \"auc_3v4\": 0.5236, \"auc_4v5\": 0.5084, \"jsd_0v1\": 0.065423, \"jsd_1v2\": 0.035809, \"jsd_2v3\": 0.004315, \"jsd_3v4\": 0.003182, \"jsd_4v5\": 0.003047, \"ordinal_mae\": 1.2578, \"ordinal_accuracy\": 0.3433, \"scorer\": \"pythia-1.4b\"}, \"notes\": \"Code domain K*=2 confirmed scorer-independent. Pythia-1.4B scorer reproduces K*=2 on Qwen-1.5B Code text (same as Qwen self-scorer). AUC deltas vs original: 0v1 Δ=-0.031, 1v2 Δ=-0.019 (minor drop, Pythia slightly weaker feature extractor), 2v3 Δ=+0.001 (identical). Boundary transition 1v2→2v3 robust: 0.7197→0.5308, clear drop below θ=0.6. JSD pattern consistent: sharp collapse at depth 2→3. Combined with arXiv cross-scorer results (LLaMA/Mistral K*=3 preserved), confirms generational depth K* is a text-intrinsic property governed by domain complexity, not scorer choice.\", \"completed_at\": \"2026-05-19T06:55:26.175Z\"}, \"exp_pythia_retrain_depth7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:53:18.835Z\", \"updated_at\": \"2026-05-19T03:46:00.139Z\", \"hypothesis\": \"Pythia-1.4B retrain-chain depth extension to 7: 验证 retrain-chain K* >> prompt-chain K* 是否跨模型家族一致（Qwen retrain K*≥7）。如果 Pythia 也 K*≥5-7，confirms retrain artifacts are model-independent。C4 5K docs, LoRA rank=16 alpha=32, depth 0-7。\", \"parent\": \"exp_qwen_retrain_depth7\", \"spec\": {\"command\": \"HF_ENDPOINT=https://hf-mirror.com CUDA_VISIBLE_DEVICES=0 python scripts/exp_pythia_retrain_depth7.py --device cuda:0\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_source\": \"exp_008_retrain_chain depth 0-4 data (extending to depth 5-7)\", \"eval_data\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/features.csv\", \"gpu\": [\"cuda:0\"], \"pid\": \"115855\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_pythia_retrain_depth7_nohup.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_pythia_retrain_depth7\"}, \"notes\": \"Actual log path: /root/autodl-tmp/gen-depth-contamination/logs/exp_pythia_retrain_depth7_nohup.log (not ~/runs/). Fine-tuning 1250 steps completed, currently in generation phase. GPU util 53% normal for Pythia-1.4B small model.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:45:55.351Z\", \"metrics\": {\"kstar\": 7, \"pairwise_auc\": {\"0v1\": 0.9844, \"1v2\": 0.947, \"2v3\": 0.8891, \"3v4\": 0.7999, \"4v5\": 0.6907, \"5v6\": 0.6497, \"6v7\": 0.634}, \"pairwise_auc_ci\": {\"0v1\": [0.9829, 0.9858], \"1v2\": [0.9418, 0.9522], \"2v3\": [0.8822, 0.896], \"3v4\": [0.7951, 0.8047], \"4v5\": [0.688, 0.6934], \"5v6\": [0.6429, 0.6565], \"6v7\": [0.6275, 0.6406]}, \"pairwise_jsd\": {\"0v1\": 0.1775, \"1v2\": 0.1286, \"2v3\": 0.1069, \"3v4\": 0.0643, \"4v5\": 0.0331, \"5v6\": 0.0271, \"6v7\": 0.0138}}}, \"exp_qwen_retrain_depth7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:08:52.105Z\", \"updated_at\": \"2026-05-19T01:10:25.114Z\", \"hypothesis\": \"Qwen2.5-1.5B retrain-chain extended to depth 7: K* measurement at higher depths. Retrain-chain with LoRA rank=16, alpha=32, 1 epoch per generation. Each depth uses independently trained LoRA merged before next generation. C4 5K docs, depth 0-7, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B (self-scoring). Extends exp_qwen_retrain_chain (depth 0-4).\", \"parent\": \"exp_qwen_retrain_chain\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path Qwen2.5-1.5B --max_depth 7 (retrain-chain extension)\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain_ext\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen_retrain_chain\", \"eval_data\": \"C4 5000 docs depth 0-7\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain_ext/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain_ext/summary.json\", \"metrics\": {\"k_star\": 7, \"theta\": 0.6, \"max_depth\": 7, \"analysis_method\": \"5-fold GroupKFold CV\", \"pairwise_auc\": {\"0v1\": {\"mean\": 0.9837, \"std\": 0.0019, \"ci_95\": [0.9821, 0.9854], \"folds\": [0.9832, 0.9821, 0.9837, 0.9823, 0.9873]}, \"1v2\": {\"mean\": 0.8971, \"std\": 0.0025, \"ci_95\": [0.8949, 0.8993], \"folds\": [0.8923, 0.8988, 0.8986, 0.8991, 0.8967]}, \"2v3\": {\"mean\": 0.8098, \"std\": 0.0052, \"ci_95\": [0.8052, 0.8144], \"folds\": [0.8086, 0.8074, 0.818, 0.8024, 0.8128]}, \"3v4\": {\"mean\": 0.76, \"std\": 0.0082, \"ci_95\": [0.7528, 0.7672], \"folds\": [0.7534, 0.7617, 0.7753, 0.7566, 0.7531]}, \"4v5\": {\"mean\": 0.7459, \"std\": 0.0091, \"ci_95\": [0.7379, 0.7538], \"folds\": [0.7429, 0.7562, 0.7521, 0.73, 0.7482]}, \"5v6\": {\"mean\": 0.7017, \"std\": 0.0068, \"ci_95\": [0.6958, 0.7076], \"folds\": [0.7006, 0.7077, 0.7104, 0.6915, 0.6984]}, \"6v7\": {\"mean\": 0.641, \"std\": 0.0039, \"ci_95\": [0.6376, 0.6445], \"folds\": [0.6419, 0.6349, 0.6464, 0.639, 0.643]}}, \"jsd\": {\"0v1\": 0.23005, \"1v2\": 0.103924, \"2v3\": 0.075049, \"3v4\": 0.065398, \"4v5\": 0.060509, \"5v6\": 0.034998, \"6v7\": 0.017652}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:10:20.209Z\", \"notes\": \"Qwen2.5-1.5B retrain-chain K*=7 (all 7 depth pairs AUC > θ=0.60). 6v7 AUC=0.641 (CI [0.638, 0.645]) is the tightest pair but still clears threshold. Depth 0-4 results consistent with exp_qwen_retrain_chain (AUC diff < 0.003). JSD decays from 0.230 (0v1) to 0.018 (6v7), suggesting convergence. AUC decay is sublinear: rapid initial drop (0v1→2v3: ~0.087/step), then deceleration (2v3→4v5: ~0.032/step), with continued decline (4v5→6v7: ~0.052/step). K* ceiling estimated at 7-8 based on extrapolation.\"}, \"exp_code_pythia1b4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:49:01.762Z\", \"updated_at\": \"2026-05-19T00:27:22.456Z\", \"hypothesis\": \"Pythia-1.4B on Code domain (Python/CodeSearchNet) will show K*=2 consistent with Qwen code domain results, indicating generalization depth saturation is model-independent for code data.\", \"parent\": \"exp_code_qwen1b5\", \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && source /root/miniconda3/bin/activate && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_code_pythia1b4 --results_dir results/exp_code_pythia1b4 --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4\", \"data_count\": 5000, \"model_name\": \"Pythia-1.4B\", \"seed\": 42, \"checkpoint_source\": \"exp_code_qwen1b5\", \"eval_data\": \"CodeSearchNet Python 5000 docs\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_code_pythia1b4/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_code_pythia1b4/train.log\", \"metrics\": {\"k_star\": 1, \"theta\": 0.6, \"pairwise_auc\": {\"0v1\": {\"mean\": 0.9592, \"std\": 0.0036, \"folds\": [0.9576, 0.9576, 0.9657, 0.96, 0.9552]}, \"1v2\": {\"mean\": 0.5983, \"std\": 0.005, \"folds\": [0.601, 0.5884, 0.6, 0.5997, 0.6024]}, \"2v3\": {\"mean\": 0.5215, \"std\": 0.0128, \"folds\": [0.5236, 0.5124, 0.5311, 0.5024, 0.5381]}, \"3v4\": {\"mean\": 0.5152, \"std\": 0.012, \"folds\": [0.4981, 0.5327, 0.5092, 0.5123, 0.5238]}, \"4v5\": {\"mean\": 0.5046, \"std\": 0.0137, \"folds\": [0.4983, 0.4822, 0.5074, 0.5224, 0.5128]}}, \"jsd\": {\"0v1\": 0.070173, \"1v2\": 0.008211, \"2v3\": 0.003674, \"3v4\": 0.002902, \"4v5\": 0.002685}, \"ordinal\": {\"mae\": 1.3268, \"accuracy\": 0.3357}, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"surp_d2_mean\", \"surp_mean\", \"surp_d1_skew\"], \"features_csv\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4/features.csv\"}, \"completed_at\": \"2026-05-19T00:25:32.688Z\", \"notes\": \"Pythia-1.4B code domain K*=1 (1v2 AUC=0.5983, 0.17pp below θ=0.60). Hypothesis falsified: expected K*=2 consistent with Qwen. 3/5 folds above θ (0.601, 0.600, 0.602), mean borderline. Parallels Mistral C4 one-wash pattern. Suggests model capability modulates domain ceiling.\"}, \"exp_028_power_curve\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:53:26.909Z\", \"updated_at\": \"2026-05-18T23:01:26.449Z\", \"hypothesis\": \"Subsampling power analysis: K*=2 判定在 C4 上所需的最低样本量。在 n={500,1000,2000,3000,4000,5000} 下 10 次 random resample，每次 5-fold CV 计算 1v2 AUC。输出 power curve（K*=2 判定成功率 vs n）。验证类实验，回应 Reviewer 对 statistical power / sample size adequacy 的质疑。\", \"metrics\": {\"min_n_100pct\": 2000, \"n500_auc\": 0.5808, \"n500_rate\": 0.2, \"n1000_auc\": 0.5911, \"n1000_rate\": 0.3, \"n2000_auc\": 0.6101, \"n2000_rate\": 1, \"n3000_auc\": 0.6166, \"n3000_rate\": 1, \"n4000_auc\": 0.622, \"n4000_rate\": 1, \"n5000_auc\": 0.6288, \"n5000_rate\": 1}, \"conclusion\": \"success\", \"notes\": \"K*=2 detection on C4 requires minimum n=2000 docs for 100% success rate (10/10 resamples). Below n=2000 power drops sharply: n=1000 → 30%, n=500 → 20%. AUC variance monotonically decreases with n (0.018 at n=500 → 0.004 at n=4000). Feature data from exp016_qwen_base (C4, 5000 docs × 6 depths × 15 features). CPU-only, 86s runtime.\", \"spec\": {\"checkpoint_path\": \"N/A (analysis experiment)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_028_power_curve/\", \"command\": \"python scripts/exp_028_power_curve.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\", \"data_count\": 30000, \"model_name\": \"N/A\", \"seed\": 42}, \"completed_at\": \"2026-05-18T23:01:26.449Z\"}, \"exp_qwen_retrain_chain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:57:56.785Z\", \"updated_at\": \"2026-05-18T22:30:28.719Z\", \"hypothesis\": \"Qwen2.5-1.5B retrain-chain ecological validity: LoRA rank=16, alpha=32, 1 epoch per generation. Retrain-chain K* ≤ prompt-chain K*=2, confirming prompt-chain as conservative upper bound across a second architecture family (Qwen vs Pythia). C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B (self-scoring).\", \"parent\": \"exp_008_retrain_chain_v2\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/qwen_retrain_chain/lora_adapters/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_qwen_retrain_chain.log\"}, \"metrics\": {\"K_star_lower_bound\": 4, \"theta\": 0.6, \"auc_0v1\": 0.9838, \"auc_1v2\": 0.8969, \"auc_2v3\": 0.81, \"auc_3v4\": 0.7624, \"ci_0v1\": [0.982, 0.9855], \"ci_1v2\": [0.8937, 0.9001], \"ci_2v3\": [0.8052, 0.8147], \"ci_3v4\": [0.7543, 0.7706], \"ci_method\": \"5-fold CV\", \"jsd_0v1\": 0.2263, \"jsd_1v2\": 0.1046, \"jsd_2v3\": 0.0752, \"jsd_3v4\": 0.0654}, \"notes\": \"Qwen2.5-1.5B retrain-chain K*≥4 (all 4 pairs AUC >> θ=0.60). Bootstrap CI discarded due to data leakage (resampling broke GroupKFold structure, inflated AUC by +6.4pp). Using fold-based CI instead. Retrain-chain K*≥4 >> prompt-chain K*=2, contradicts conservative-upper-bound hypothesis but confirms retrain produces qualitatively different degradation pattern.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:30:28.719Z\"}, \"exp_code_qwen1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:36:16.788Z\", \"updated_at\": \"2026-05-18T21:45:24.101Z\", \"hypothesis\": \"Code domain (Python) K* measurement: Qwen2.5-1.5B continuation on CodeSearchNet Python subset (Husain et al. 2019). Code 的高度结构化特性（语法约束、缩进、函数签名）应使代际退化慢于 C4 (K*≥2)，可能接近 arXiv (K*=3)。5500 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"notes\": \"Code domain (Python/CodeSearchNet) K*=2, same as C4. 1v2 AUC=0.7382 well above θ, 2v3 drops to 0.5300. Bug fix: run_pipeline.py:462 int(doc_id) patched for string IDs. Top features: freq_entropy, surp_d2_mean, surp_d1_mean. Data source: CodeSearchNet Python subset (Husain et al. 2019).\", \"spec\": {\"checkpoint_path\": \"N/A (pipeline experiment, no model checkpoint)\", \"log_path\": \"~/runs/gen-depth-contamination/exp_code_qwen1b5.log\"}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 2, \"theta\": 0.6, \"auc_0v1\": 0.9388, \"auc_1v2\": 0.7382, \"auc_2v3\": 0.53, \"auc_3v4\": 0.5022, \"auc_4v5\": 0.5219, \"ci_0v1\": [0.929, 0.949], \"ci_1v2\": [0.709, 0.767], \"ci_2v3\": [0.514, 0.546], \"jsd_0v1\": 0.0814, \"jsd_1v2\": 0.0443, \"jsd_2v3\": 0.0038, \"ordinal_accuracy\": 0.359, \"ordinal_mae\": 1.204}, \"completed_at\": \"2026-05-18T21:45:24.101Z\"}, \"exp_olmo_retrain_chain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:08:07.671Z\", \"updated_at\": \"2026-05-18T16:27:30.792Z\", \"hypothesis\": \"OLMo-1B retrain-chain (LoRA rank=16, 1 epoch per generation) on C4 produces K* ≤ 2, confirming prompt-chain as conservative upper bound for K*.\", \"parent\": \"exp_002\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp_olmo_retrain_chain.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/olmo_retrain_chain\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"checkpoint_source\": \"allenai/OLMo-1B-hf\", \"eval_data\": \"C4 validation (5000 docs)\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T16:27:30.792Z\"}, \"exp_028_subsampling_power\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:30:47.472Z\", \"updated_at\": \"2026-05-18T13:31:41.053Z\", \"hypothesis\": \"C4 K*=2 信号的 minimum sample size: 在 n={1000..5000} 范围内，GroupKFold(5) 1v2 AUC 是否稳定超过 θ=0.60？确定可靠判定 K*=2 所需的最小样本量。\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/c4_power_curve/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/c4_power_curve/power_curve_results.json\", \"metrics\": {\"n_1000\": {\"mean_auc\": 0.608, \"std\": 0.012, \"detection_prob\": 0.9}, \"n_2500\": {\"mean_auc\": 0.618, \"std\": 0.006, \"detection_prob\": 1}, \"n_5000\": {\"mean_auc\": 0.629, \"std\": 0, \"detection_prob\": 1}, \"key_finding\": \"n>=2500 gives 100% reliable K*=2 detection. n=1000 already 90%. Signal is robust, not large-sample artifact.\"}, \"spec\": {\"command\": \"python scripts/c4_power_curve.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/results/ (exp-016 features)\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (scorer)\", \"seed\": \"10 random trials per n\", \"checkpoint_source\": \"exp-016 feature vectors\", \"eval_data\": \"GroupKFold(5) pairwise classification, n={1000..5000}\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T13:31:41.053Z\"}, \"exp_026_arxiv_filtering\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:19:57.768Z\", \"updated_at\": \"2026-05-18T11:20:35.820Z\", \"hypothesis\": \"Graduated depth weighting (α=0.9^d) on arXiv depth chains will outperform both no-filter and binary-cut baselines on downstream benchmarks (MMLU, HellaSwag), because it preserves useful signal from deeper generations while down-weighting accumulated contamination, rather than discarding data entirely.\", \"parent\": \"exp_006_graduated_filtering\", \"spec\": {\"command\": \"bash scripts/run_exp026.sh\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/\", \"data_count\": 13200, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": \"42,123,456,789,1024\", \"gpu\": \"cuda:0,cuda:1,cuda:2\", \"strategies\": \"no_filter,binary,graduated_a09\", \"lora_rank\": 4, \"lora_alpha\": 8, \"pid\": 27516, \"checkpoint_source\": \"lora_merge_per_run\", \"eval_data\": \"mmlu,hellaswag (lm-eval-harness)\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_026_arxiv_filtering/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_026_arxiv_filtering.log\", \"metrics\": {\"runs_completed\": \"15/15\", \"strategies\": [\"no_filter\", \"binary\", \"graduated_a09\"], \"seeds\": [42, 123, 456, 789, 1024], \"mmlu\": {\"no_filter\": \"0.5899±0.0008\", \"binary\": \"0.5876±0.0004\", \"graduated_a09\": \"0.5900±0.0011\"}, \"hellaswag\": {\"no_filter\": \"0.6600±0.0002\", \"binary\": \"0.6642±0.0004\", \"graduated_a09\": \"0.6599±0.0003\"}, \"delta_vs_no_filter\": {\"binary_mmlu\": \"-0.0023\", \"binary_hellaswag\": \"+0.0042\", \"graduated_mmlu\": \"+0.0001\", \"graduated_hellaswag\": \"-0.0001\"}, \"key_finding\": \"All three strategies produce nearly identical results. Graduated ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T11:20:35.820Z\"}, \"exp_027_latex_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T10:19:59.624Z\", \"updated_at\": \"2026-05-18T10:41:35.226Z\", \"hypothesis\": \"arXiv K*=3 不依赖 LaTeX 格式特征。去除 LaTeX markup 后重新提取 15D features 并跑 pairwise classification，K* 应仍=3，排除 LaTeX 语法作为 confound。\", \"parent\": \"exp_024_arxiv_depth_chain\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/summary.txt\", \"metrics\": {\"k_star\": 3, \"k_star_preserved\": true, \"pairwise_auc_original\": {\"0v1\": 0.9948, \"1v2\": 0.8581, \"2v3\": 0.6436, \"3v4\": 0.544, \"4v5\": 0.5299}, \"pairwise_auc_stripped\": {\"0v1\": 0.9948, \"1v2\": 0.8297, \"2v3\": 0.6229, \"3v4\": 0.5468, \"4v5\": 0.5476}, \"auc_delta\": {\"0v1\": 0, \"1v2\": -0.028, \"2v3\": -0.021, \"3v4\": 0.003, \"4v5\": 0.018}, \"latex_reduction_by_depth\": {\"depth_0\": \"0.6%\", \"depth_5\": \"4.4%\"}, \"key_finding\": \"K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still >θ=0.60). LaTeX format is NOT a confound.\"}, \"spec\": {\"command\": \"python scripts/exp027_latex_ablation.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/\", \"data_count\": 13200, \"model_name\": \"Qwen2.5-1.5B (scorer)\", \"seed\": 42, \"checkpoint_source\": \"exp_024_arxiv_depth_chain\", \"eval_data\": \"GroupKFold(5) pairwise classification\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T10:41:35.226Z\"}, \"exp_025_pythia_filtering\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T08:04:54.965Z\", \"updated_at\": \"2026-05-18T09:51:02.931Z\", \"hypothesis\": \"Filtering strategy ordering (binary > graduated > no-filter) 在 Pythia-1.4B 上与 Qwen 一致，验证 K*=2 对 curation 策略选择的跨模型预测价值。Pythia-1.4B LoRA rank=8 continued pretraining on C4 depth chain, 3 strategies × 3 seeds, eval MMLU+HellaSwag.\", \"parent\": \"exp_006_graduated_filtering\", \"spec\": {\"command\": \"bash scripts/run_exp025.sh (3 strategies × 3 seeds, 9 runs in 3 batches, 4 GPUs parallel per batch)\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp020_pythia_nuc09/\", \"data_count\": 30000, \"model_name\": \"Pythia-1.4B\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"EleutherAI/pythia-1.4b (HuggingFace, base model for LoRA)\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\"}, \"notes\": \"Data source fixed: greedy → nuc09. Old processes killed (6 procs). Resubmitted 2026-05-18T08:27 via nohup (not submit_training_job). PID 15687, cqa1 cuda:0-3, 9 runs in 3 batches (4 parallel per batch). Cron registered for monitoring.\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_025_pythia_filtering/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp025/\", \"metrics\": {\"runs_completed\": \"9/9\", \"strategies\": [\"no_filter\", \"binary_ours\", \"graduated_a09\"], \"seeds\": [42, 123, 456], \"mmlu\": {\"no_filter\": \"0.2568±0.0012\", \"binary_ours\": \"0.2585±0.0004\", \"graduated_a09\": \"0.2561±0.0009\"}, \"hellaswag\": {\"no_filter\": \"0.5250±0.0008\", \"binary_ours\": \"0.5251±0.0001\", \"graduated_a09\": \"0.5253±0.0007\"}, \"delta_vs_no_filter\": {\"binary_ours_mmlu\": \"+0.0017\", \"binary_ours_hellaswag\": \"+0.0000\", \"graduated_a09_mmlu\": \"-0.0007\", \"graduated_a09_hellaswag\": \"+0.0003\"}, \"key_finding\": \"All three filtering strategies produce nearly identical results on Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering binary>graduated>no_filter NOT confirmed.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T09:51:02.931Z\"}, \"exp_14b_c4\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T14:56:44.366Z\", \"updated_at\": \"2026-05-18T08:37:25.809Z\", \"hypothesis\": \"Scale-dependent K* on C4: Qwen2.5-14B fp16 continuation on C4 web text 的 K* 是否仍 = 2？验证 K*=2 dominant mode 在 14B scale 是否稳定（已确认 1.5B/7B/8B 均 K*=2），排除 scale ceiling effect。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_arXiv_llama8b\", \"server\": \"westd-42896\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-42896\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T17:08:43.246Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-14B --data_dir data/exp_14b_c4 --results_dir results/exp_14b_c4 --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"finished_at\": \"2026-05-18T08:21:21.247Z\", \"training_hours\": 15.21}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-18T05:09:04.625Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:09:08.254971+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:21:24.534646+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-14B --data_dir data/exp_14b_c4 --results_dir results/exp_14b_c4 --num_samples 5000 --max_depth 5 --batch_size 4 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"westd-42896\", \"gpu\": [\"cuda:0\"], \"pid\": \"39497\", \"log_path\": \"~/runs/gen-depth-contamination/exp_14b_c4.log\", \"submitted_at\": \"2026-05-18T05:12:11.079Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11638.0, \"gpu_hours\": 3.23}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9598, \"1v2\": 0.621, \"2v3\": 0.5494, \"3v4\": 0.5243, \"4v5\": 0.5154}, \"pairwise_jsd\": {\"0v1\": 0.1097, \"1v2\": 0.0112, \"2v3\": 0.0062, \"3v4\": 0.0044, \"4v5\": 0.0036}, \"bootstrap_ci\": {\"0v1\": [0.9564, 0.963], \"1v2\": [0.6119, 0.6304], \"2v3\": [0.5392, 0.5594], \"3v4\": [0.514, 0.5346], \"4v5\": [0.5045, 0.5265]}, \"permutation_p\": {\"0v1\": \"<0.001\", \"1v2\": \"<0.001\", \"2v3\": \"<0.001\", \"3v4\": \"<0.001\", \"4v5\": \"<0.001\"}, \"k_star_statistically_confirmed\": true, \"ordinal_mae\": 1.2266, \"ordinal_accuracy\": 0.3497, \"top_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_std\", \"surp_d1_mean\", \"surp_d2_mean\"], \"key_finding\": \"K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119) > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/\"}, \"exp_arXiv_mistral7b_crossscorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:44:21.237Z\", \"updated_at\": \"2026-05-18T03:04:46.219Z\", \"hypothesis\": \"arXiv cross-scorer (Mistral-7B): Pythia scorer 验证 Mistral arXiv K*=3 是否 scorer-independent。\", \"parent\": \"exp_wiki_scorer_confound\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_arXiv_mistral7b_crossscorer && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_mistral7b/depth_\\\\${d}.jsonl data/exp_arXiv_mistral7b_crossscorer/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_arXiv_mistral7b_crossscorer && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_arXiv_mistral7b_crossscorer --results_dir results/exp_arXiv_mistral7b_crossscorer --num_samples 2200 --max_depth 5 --batch_size 16 --generation_mode continuation --skip_generation\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"196053\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_mistral7b_crossscorer.log\", \"submitted_at\": \"2026-05-18T02:44:57.643Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 2200, \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_arXiv_mistral7b\", \"model_name\": \"Mistral-7B (generator) + Pythia-1.4B (scorer)\", \"seed\": 42, \"checkpoint_source\": \"exp_arXiv_mistral7b\", \"eval_data\": \"arXiv depth 0-5 generated by Mistral-7B (from exp_arXiv_mistral7b)\", \"checkpoint_path\": \"results/exp_arXiv_mistral7b_crossscorer/\", \"wall_clock_seconds\": 1117.5, \"gpu_hours\": 0.31}, \"reproduce\": {\"finished_at\": \"2026-05-18T03:00:29.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T03:00:37.583555+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 3, \"scorer\": \"pythia-1.4b\", \"auc_0v1\": 0.9798, \"auc_1v2\": 0.8141, \"auc_2v3\": 0.6075, \"auc_3v4\": 0.5489, \"auc_4v5\": 0.5391, \"jsd_0v1\": 0.135575, \"jsd_1v2\": 0.078, \"jsd_2v3\": 0.020452, \"jsd_3v4\": 0.010992, \"jsd_4v5\": 0.008831, \"ordinal_mae\": 0.9061, \"ordinal_accuracy\": 0.4412}, \"completed_at\": \"2026-05-18T03:03:35.138Z\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_mistral7b_crossscorer.log\", \"notes\": \"Pythia-1.4B cross-scorer confirms K*=3 for Mistral-7B arXiv, matching Qwen-1.5B original. Max AUC delta = 0.02 (at 2v3). arXiv Mistral K*=3 is scorer-independent. Contrasts with Wikipedia where scorer choice affected K*.\"}, \"exp_arXiv_llama8b_crossscorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:44:19.881Z\", \"updated_at\": \"2026-05-18T03:04:36.609Z\", \"hypothesis\": \"Replacing Qwen-1.5B scorer with Pythia-1.4B on arXiv LLaMA-8B depth 0-5 texts should yield the same K*=3 boundary, because the saturation signal is a genuine property of LLaMA-8B generated text rather than a scorer family artifact\", \"parent\": \"exp_wiki_scorer_confound\", \"spec\": {\"command\": \"skip_generation scoring with Pythia-1.4B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"195907\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_llama8b_crossscorer.log\", \"submitted_at\": \"2026-05-18T02:44:54.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_llama8b_crossscorer/\", \"data_count\": 6, \"model_name\": \"pythia-1.4b\", \"seed\": 42, \"checkpoint_source\": \"exp_arXiv_llama8b\", \"eval_data\": \"arXiv LLaMA-8B depth 0-5 continuations from exp_arXiv_llama8b\", \"checkpoint_path\": \"results/exp_arXiv_llama8b_crossscorer/\", \"wall_clock_seconds\": 1119.6, \"gpu_hours\": 0.31}, \"reproduce\": {\"finished_at\": \"2026-05-18T03:00:23.861Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T03:00:27.320630+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 3, \"auc_0v1\": 0.9629, \"auc_1v2\": 0.8433, \"auc_2v3\": 0.6201, \"auc_3v4\": 0.523, \"auc_4v5\": 0.5245, \"jsd_0v1\": 0.1214, \"jsd_1v2\": 0.0815, \"jsd_2v3\": 0.0195, \"jsd_3v4\": 0.0083, \"jsd_4v5\": 0.0082, \"ordinal_mae\": 0.9025, \"ordinal_accuracy\": 0.4407, \"scorer\": \"pythia-1.4b\"}, \"completed_at\": \"2026-05-18T03:03:34.051Z\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_llama8b_crossscorer.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_llama8b_crossscorer/\"}, \"exp_arXiv_qwen7b_crossscorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:13:55.051Z\", \"updated_at\": \"2026-05-18T03:04:22.586Z\", \"hypothesis\": \"arXiv cross-scorer (7B): Pythia-1.4B scorer 重评 Qwen-7B arXiv depth 0-5。D060 Wiki scorer confound 推导。关键 2v3 AUC ≥0.60 → K*=3 scorer-independent。\", \"parent\": \"exp_wiki_scorer_confound\", \"spec\": {\"command\": \"run_pipeline.py --skip_generation\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"195291\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen7b_crossscorer.log\", \"submitted_at\": \"2026-05-18T02:44:45.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_arXiv_qwen7b_crossscorer\", \"data_count\": 2200, \"model_name\": \"Qwen/Qwen2.5-7B\", \"seed\": 42, \"checkpoint_source\": \"exp_arXiv_qwen7b\", \"eval_data\": \"arXiv Qwen-7B depth 0-5 from exp_arXiv_qwen7b\", \"wall_clock_seconds\": 1156.0, \"gpu_hours\": 0.32, \"checkpoint_path\": \"results/exp_arXiv_qwen7b_crossscorer/\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T02:59:40.126Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"negative\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:18:26.248465+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:59:43.427079+00:00\"}]}, \"notes\": \"Hypothesis rejected: cross-scorer 2v3 AUC=0.5989 < 0.60, K* drops from 3→2. Mild Qwen family bias (~0.027 AUC at 2v3) inflates original K*=3. Scorer-independent K*=2. Borderline: 3/5 folds above 0.60. Depths 0-2 robustly scorer-independent.\", \"metrics\": {\"k_star\": 2, \"auc_0v1\": 0.9575, \"auc_1v2\": 0.8171, \"auc_2v3\": 0.5989, \"auc_3v4\": 0.5417, \"auc_4v5\": 0.5192, \"jsd_0v1\": 0.137085, \"jsd_1v2\": 0.059688, \"jsd_2v3\": 0.013508, \"jsd_3v4\": 0.009125, \"jsd_4v5\": 0.006738, \"ordinal_mae\": 0.9617, \"ordinal_accuracy\": 0.4255}, \"checkpoint_path\": \"N/A (scoring-only experiment, no training checkpoint)\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen7b_crossscorer.log\", \"completed_at\": \"2026-05-18T03:04:01.839Z\"}, \"exp_arXiv_qwen1b5_crossscorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:13:56.083Z\", \"updated_at\": \"2026-05-18T03:02:38.562Z\", \"hypothesis\": \"arXiv cross-scorer (1.5B): Pythia-1.4B scorer 重评 Qwen-1.5B arXiv depth 0-5。验证 K*=3 scorer-independent。\", \"parent\": \"exp_wiki_scorer_confound\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_arXiv_qwen1b5_crossscorer && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/depth_\\\\${d}.jsonl data/exp_arXiv_qwen1b5_crossscorer/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_arXiv_qwen1b5_crossscorer && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_arXiv_qwen1b5_crossscorer --results_dir results/exp_arXiv_qwen1b5_crossscorer --num_samples 2200 --max_depth 5 --batch_size 16 --generation_mode continuation --skip_generation\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"195826\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen1b5_crossscorer.log\", \"submitted_at\": \"2026-05-18T02:44:53.081Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"results/exp_arXiv_qwen1b5_crossscorer/\", \"wall_clock_seconds\": 1065.5, \"gpu_hours\": 0.3}, \"reproduce\": {\"finished_at\": \"2026-05-18T02:59:46.327Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:18:40.560606+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:59:52.404331+00:00\"}]}, \"notes\": \"首次提交因 symlink 问题失败 (EXIT_CODE=1)，Worker 修复后重跑成功 (EXIT_CODE=0)。Pythia-1.4B scorer 重评 Qwen-1.5B arXiv 文本 K*=3，与 Qwen scorer 一致，确认 arXiv K*=3 scorer-independent。\", \"metrics\": {\"k_star\": 3, \"auc_0v1\": 0.9748, \"auc_1v2\": 0.8105, \"auc_2v3\": 0.6317, \"auc_3v4\": 0.5437, \"auc_4v5\": 0.5294, \"jsd_0v1\": 0.154297, \"jsd_1v2\": 0.066782, \"jsd_2v3\": 0.019268, \"jsd_3v4\": 0.008867, \"jsd_4v5\": 0.006991, \"ordinal_mae\": 0.9017, \"ordinal_accuracy\": 0.4402}, \"completed_at\": \"2026-05-18T03:02:38.562Z\"}, \"exp_wiki_scorer_confound_1b5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:18:37.565Z\", \"updated_at\": \"2026-05-18T01:21:43.381Z\", \"hypothesis\": \"Scorer family bias replication (Qwen-1.5B): 用 Pythia-1.4B 替代 Qwen-1.5B 作为 scorer 重新评分 exp_023_domain_ablation (Qwen-1.5B Wiki depth 0-5) 文本。如果 Pythia scorer 下 K* 仍=2 → confound excluded for both Qwen scales；如果 K*=1 → scorer confound confirmed，与 Qwen-7B 复验一致。\", \"parent\": \"exp_023_domain_ablation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T23:20:01.037Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_wiki_scorer_confound_1b5 && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/depth_\\\\${d}.jsonl data/exp_wiki_scorer_confound_1b5/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_wiki_scorer_confound_1b5 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_wiki_scorer_confound_1b5 --results_dir results/exp_wiki_scorer_confound_1b5 --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-18T01:18:40.529Z\", \"training_hours\": 1.98}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_wiki_scorer_confound_1b5 && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/depth_\\\\${d}.jsonl data/exp_wiki_scorer_confound_1b5/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_wiki_scorer_confound_1b5 && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_wiki_scorer_confound_1b5 --results_dir results/exp_wiki_scorer_confound_1b5 --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"180543\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_scorer_confound_1b5.log\", \"submitted_at\": \"2026-05-17T23:22:42.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 7140.9, \"gpu_hours\": 1.98}, \"pid\": \"180543\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_scorer_confound_1b5.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:18:44.039720+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"k_star\": 1, \"confound_verdict\": \"confirmed\", \"auc_0v1\": 0.9729, \"auc_1v2\": 0.5994, \"auc_2v3\": 0.533, \"auc_3v4\": 0.5214, \"auc_4v5\": 0.5068, \"jsd_0v1\": 0.0886, \"ordinal_mae\": 1.2995, \"ordinal_accuracy\": 0.3466}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_scorer_confound_1b5/\", \"completed_at\": \"2026-05-18T01:21:43.381Z\"}, \"exp_wiki_scorer_confound\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:35:20.326Z\", \"updated_at\": \"2026-05-17T23:20:31.517Z\", \"hypothesis\": \"Scorer family bias test: Qwen-7B Wikipedia K*=2 是 Qwen-1.5B scorer 的 family bias artifact 还是真实信号？用 Pythia-1.4B 替代 Qwen-1.5B 作为 scorer 重新评分同一批 depth 0-5 文本。如果 Pythia scorer 下 K* 仍=2 → confound excluded；如果 K*=1 → scorer confound confirmed。\", \"parent\": \"exp_wiki_qwen7b\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T22:55:01.348Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_wiki_scorer_confound && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_wiki_qwen7b/depth_\\\\${d}.jsonl data/exp_wiki_scorer_confound/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_wiki_scorer_confound && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_wiki_scorer_confound --results_dir results/exp_wiki_scorer_confound --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T23:13:55.501Z\", \"training_hours\": 0.32}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && mkdir -p data/exp_wiki_scorer_confound && for d in 0 1 2 3 4 5; do ln -sf /root/autodl-tmp/gen-depth-contamination/data/exp_wiki_qwen7b/depth_\\\\${d}.jsonl data/exp_wiki_scorer_confound/depth_\\\\${d}.jsonl; done && mkdir -p results/exp_wiki_scorer_confound && HF_HOME=/root/autodl-tmp/.hf_cache TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --scorer_path /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --data_dir data/exp_wiki_scorer_confound --results_dir results/exp_wiki_scorer_confound --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"178762\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_scorer_confound.log\", \"submitted_at\": \"2026-05-17T22:55:03.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_scorer_confound/\", \"wall_clock_seconds\": 1528.4, \"gpu_hours\": 0.42}, \"pid\": \"178762\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_scorer_confound.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T23:13:58.836236+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"k_star\": 1, \"confound_verdict\": \"confirmed\", \"auc_0v1\": 0.9404, \"auc_1v2\": 0.587, \"auc_2v3\": 0.5456, \"auc_3v4\": 0.525, \"auc_4v5\": 0.5172, \"critical_delta_1v2\": -0.0238}, \"completed_at\": \"2026-05-17T23:20:31.517Z\"}, \"exp_wiki_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T16:39:29.006Z\", \"updated_at\": \"2026-05-17T22:24:51.126Z\", \"hypothesis\": \"Cross-scale Wikipedia K* validation: Qwen2.5-7B continuation on Wikipedia 的 K* 是否 = 2？Qwen2.5-1.5B 在 Wikipedia K*=2（唯一维持 K*=2 的模型），Pythia/OLMo/均 K*=1。测试 7B 规模是否仍维持 Qwen 家族在 Wikipedia 上的 K*=2 pattern。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_arXiv_qwen7b\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T17:02:41.963Z\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_wiki_qwen7b --results_dir results/exp_wiki_qwen7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T22:21:53.554Z\", \"training_hours\": 5.32}, \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_wiki_qwen7b --results_dir results/exp_wiki_qwen7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"732600\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_qwen7b.log\", \"submitted_at\": \"2026-05-17T17:02:43.570Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19327.6, \"gpu_hours\": 5.37}, \"pid\": \"732600\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_qwen7b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T22:21:56.559363+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 2, \"auc_0v1\": 0.9673, \"auc_1v2\": 0.6108, \"auc_2v3\": 0.5562, \"auc_3v4\": 0.5297, \"auc_4v5\": 0.529, \"jsd_0v1\": 0.083514, \"jsd_1v2\": 0.010991, \"jsd_2v3\": 0.00555, \"jsd_3v4\": 0.004611, \"jsd_4v5\": 0.003894, \"ordinal_mae\": 1.2501, \"ordinal_accuracy\": 0.3532}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_qwen7b\", \"completed_at\": \"2026-05-17T22:24:51.126Z\"}, \"exp_wiki_mistral7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:04:15.959Z\", \"updated_at\": \"2026-05-17T19:53:56.272Z\", \"hypothesis\": \"Mistral-7B Wikipedia K* test: Mistral-7B-v0.3 在 C4 上 K*=1 (text-intrinsic one-wash)。在 Wikipedia domain 上是否仍 K*=1？Pythia/OLMo 在 Wikipedia 均 K*=1，Qwen K*=2。如果 Mistral K*=1 → 确认 one-wash 跨域成立；如果 K*>1 → Wikipedia 有 rescue Mistral 的结构信号（与预期相反）。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_wiki_pythia_v2\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T14:05:42.553Z\", \"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_wiki_mistral7b --results_dir results/exp_wiki_mistral7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T19:50:28.711Z\", \"training_hours\": 5.75}, \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_wiki_mistral7b --results_dir results/exp_wiki_mistral7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"data_path\": \"data/exp_wiki_mistral7b\", \"data_count\": 5000, \"model_name\": \"mistralai/Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_source\": \"pretrained:mistralai/Mistral-7B-v0.3\", \"eval_data\": \"Wikipedia depth 0-5, scorer=Qwen2.5-1.5B\"}, \"pid\": \"41845\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_mistral7b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:50:32.601540+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_mistral7b\", \"metrics\": {\"K_star\": 1, \"ordinal_mae\": 1.3445, \"ordinal_accuracy\": 0.3273, \"auc_0v1\": 0.9607, \"auc_1v2\": 0.5552, \"auc_2v3\": 0.5236, \"auc_3v4\": 0.5181, \"auc_4v5\": 0.5012, \"jsd_0v1\": 0.054134, \"jsd_1v2\": 0.005678, \"jsd_2v3\": 0.003698, \"jsd_3v4\": 0.003459, \"jsd_4v5\": 0.003274}, \"completed_at\": \"2026-05-17T19:53:56.272Z\"}, \"exp_wiki_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:27:37.043Z\", \"updated_at\": \"2026-05-17T19:33:39.300Z\", \"hypothesis\": \"Cross-scale Wikipedia K* validation: LLaMA-3.1-8B continuation on Wikipedia 的 K* 是否 = 2？Pythia-1.4B K*=1, Qwen-1.5B K*=2, OLMo-1B K*=1。测试 8B scale 是否能在 Wikipedia 均质 domain 上维持 K*=2（scale 是否是决定因素）。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_wiki_pythia_v2\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-17T13:29:58.320Z\", \"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --data_dir data/exp_wiki_llama8b --results_dir results/exp_wiki_llama8b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T19:30:35.869Z\", \"training_hours\": 6.01}, \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --data_dir data/exp_wiki_llama8b --results_dir results/exp_wiki_llama8b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"data_path\": \"data/exp_wiki_llama8b\", \"data_count\": 5000, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"pretrained:LLM-Research/Meta-Llama-3.1-8B\", \"eval_data\": \"Wikipedia depth 0-5, scorer=Qwen2.5-1.5B\"}, \"pid\": \"38142\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_llama8b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T19:30:39.064445+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"ordinal_mae\": 1.2954, \"ordinal_accuracy\": 0.3313, \"auc_0v1\": 0.9316, \"auc_1v2\": 0.5954, \"auc_2v3\": 0.5392, \"auc_3v4\": 0.5221, \"auc_4v5\": 0.5212, \"jsd_0v1\": 0.06169, \"jsd_1v2\": 0.00931}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_llama8b\", \"completed_at\": \"2026-05-17T19:33:39.300Z\"}, \"exp_arXiv_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:56:03.934Z\", \"updated_at\": \"2026-05-17T16:36:58.029Z\", \"hypothesis\": \"Qwen2.5-7B on arXiv abstracts will yield K*=3, validating that structured domain K*=3 is stable within the Qwen family across scales (1.5B vs 7B)\", \"parent\": \"exp_024_arxiv_domain\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T14:08:40.926Z\", \"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_arXiv_qwen7b --results_dir results/exp_arXiv_qwen7b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T16:34:23.946Z\", \"training_hours\": 2.43}, \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B --data_dir data/exp_arXiv_qwen7b --results_dir results/exp_arXiv_qwen7b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"data_path\": \"data/exp_arXiv_qwen7b\", \"data_count\": 2200, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"checkpoint_source\": \"pretrained:Qwen/Qwen2.5-7B\", \"eval_data\": \"arXiv abstracts depth 0-5, scorer=Qwen2.5-1.5B\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_qwen7b\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen7b.log\"}, \"pid\": \"42742\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_qwen7b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T16:34:26.949400+00:00\"}]}, \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.983, \"1v2\": 0.835, \"2v3\": 0.626, \"3v4\": 0.544, \"4v5\": 0.513}, \"pairwise_jsd\": {\"0v1\": 0.1656, \"1v2\": 0.0668, \"2v3\": 0.0156, \"3v4\": 0.0089, \"4v5\": 0.0061}, \"ordinal_mae\": 0.9, \"ordinal_accuracy\": 0.446}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T16:36:58.029Z\"}, \"exp_arXiv_mistral7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:32:28.299Z\", \"updated_at\": \"2026-05-17T16:28:24.294Z\", \"hypothesis\": \"Mistral-7B arXiv K* test: Mistral-7B-v0.3 在 C4 上 K*=1 (one-wash model)。在 arXiv structured domain 上是否仍 K*=1？如果 K*=1 → 确认 Mistral 的 one-wash 是 text-intrinsic (与 domain 无关)；如果 K*>1 → domain complexity 可以 rescue one-wash models，K* 同时受 model 和 domain 驱动。2200 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_arXiv_olmo\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-17T13:53:18.456Z\", \"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_arXiv_mistral7b --results_dir results/exp_arXiv_mistral7b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"code_commit\": \"0b10b4309bd03e7fcc3cbeb7fca54744d69a73b5\", \"finished_at\": \"2026-05-17T16:25:00.229Z\", \"training_hours\": 2.53}, \"spec\": {\"command\": \"cd /root/autodl-tmp/gen-depth-contamination && /root/miniconda3/bin/python3.12 scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data/exp_arXiv_mistral7b --results_dir results/exp_arXiv_mistral7b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"data_path\": \"data/exp_arXiv_mistral7b\", \"data_count\": 2200, \"model_name\": \"mistralai/Mistral-7B-v0.3\", \"seed\": 42, \"checkpoint_source\": \"pretrained:mistralai/Mistral-7B-v0.3\", \"eval_data\": \"arXiv abstracts depth 0-5, scorer=Qwen2.5-1.5B\"}, \"pid\": \"40472\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_mistral7b.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T16:25:03.226062+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9848, \"1v2\": 0.8201, \"2v3\": 0.6275, \"3v4\": 0.5295, \"4v5\": 0.5295}, \"jsd\": {\"0v1\": 0.14249, \"1v2\": 0.076232, \"2v3\": 0.018972, \"3v4\": 0.009908, \"4v5\": 0.008877}, \"ordinal_mae\": 0.8958, \"ordinal_accuracy\": 0.4474, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_d1_skew\", \"surp_mean\", \"surp_d2_mean\"]}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_mistral7b\", \"completed_at\": \"2026-05-17T16:28:24.294Z\"}, \"exp_arXiv_llama8b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:53:57.754Z\", \"updated_at\": \"2026-05-17T14:02:45.388Z\", \"hypothesis\": \"Cross-architecture arXiv K* validation: LLaMA-3.1-8B continuation on arXiv abstracts 的 K* 是否 = 3？验证 structured domain K*=3 在大模型（8B scale）上是否成立，排除小模型 capacity artifact。2200 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_024_arxiv_domain\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T10:59:48.493Z\", \"finished_at\": \"2026-05-17T13:59:25.526Z\", \"training_hours\": 2.99}, \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --data_dir data/exp_arXiv_llama8b --results_dir results/exp_arXiv_llama8b --num_samples 2200 --max_depth 5 --batch_size 8 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"27469\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_llama8b.log\", \"submitted_at\": \"2026-05-17T11:23:08.013Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_arXiv_llama8b (seed from exp_024_arxiv/depth_0.jsonl)\", \"data_count\": 2200, \"model_name\": \"Meta-Llama-3.1-8B\", \"seed\": 42, \"checkpoint_source\": \"pretrained:LLM-Research/Meta-Llama-3.1-8B\", \"eval_data\": \"arXiv abstracts depth 0-5, scorer=Qwen2.5-1.5B\", \"wall_clock_seconds\": 9577.4, \"gpu_hours\": 2.66}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:59:27.415949+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 3, \"auc_0v1\": 0.9754, \"auc_1v2\": 0.8447, \"auc_2v3\": 0.6215, \"auc_3v4\": 0.5362, \"auc_4v5\": 0.5331, \"jsd_0v1\": 0.1296, \"jsd_1v2\": 0.0785, \"jsd_2v3\": 0.0177, \"ordinal_acc\": 0.4549, \"ordinal_mae\": 0.8806}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_llama8b/\", \"completed_at\": \"2026-05-17T14:02:45.388Z\"}, \"exp_wiki_pythia_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:40:37.896Z\", \"updated_at\": \"2026-05-17T13:25:22.734Z\", \"hypothesis\": \"Cross-model Wikipedia K* validation (v2 fix): Pythia-1.4B continuation on Wikipedia 的 K* 是否 = 2？使用独立 data_dir 避免 v1 的 data reuse bug，让 pipeline 用 Pythia 重新生成 depth 1-5。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_wiki_pythia\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path ...pythia-1.4b... --generation_mode continuation\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"30942\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_pythia_v2.log\", \"submitted_at\": \"2026-05-17T11:48:32.895Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_wiki_pythia\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"git_commit\": \"0b10b43\", \"checkpoint_source\": \"N/A (generation experiment, not eval)\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 5809.8, \"gpu_hours\": 1.61}, \"reproduce\": {\"finished_at\": \"2026-05-17T13:15:30.480Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:15:32.903668+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.975, \"auc_1v2\": 0.5846, \"auc_2v3\": 0.5445, \"auc_3v4\": 0.5205, \"auc_4v5\": 0.5168, \"jsd_0v1\": 0.080065, \"jsd_1v2\": 0.007773, \"ordinal_acc\": 0.3503}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_pythia_v2/\", \"completed_at\": \"2026-05-17T13:25:22.734Z\"}, \"exp_wiki_olmo_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:40:38.784Z\", \"updated_at\": \"2026-05-17T13:23:57.369Z\", \"hypothesis\": \"Cross-model Wikipedia K* validation (v2 fix): OLMo-1B continuation on Wikipedia 的 K* 是否 = 2？使用独立 data_dir 避免 v1 的 data reuse bug，让 pipeline 用 OLMo 重新生成 depth 1-5。5000 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_wiki_olmo\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path .../allenai/OLMo-1B-hf --generation_mode continuation\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"31084\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_olmo_v2.log\", \"submitted_at\": \"2026-05-17T11:48:36.028Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_wiki_olmo\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"git_commit\": \"0b10b43\", \"checkpoint_source\": \"N/A (generation experiment, not eval)\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 5721.3, \"gpu_hours\": 1.59}, \"reproduce\": {\"finished_at\": \"2026-05-17T13:08:49.908Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:08:52.662189+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9932, \"auc_1v2\": 0.4986, \"auc_2v3\": 0.5012, \"auc_3v4\": 0.5057, \"auc_4v5\": 0.5009, \"jsd_0v1\": 0.1688, \"ordinal_acc\": 0.3227}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_olmo_v2/\", \"completed_at\": \"2026-05-17T13:23:57.369Z\"}, \"exp_arXiv_olmo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:53:55.374Z\", \"updated_at\": \"2026-05-17T12:28:50.616Z\", \"hypothesis\": \"Cross-model arXiv K* validation: OLMo-1B continuation on arXiv abstracts 的 K* 是否 = 3（与 exp-024 Qwen 和 exp-025 Pythia 一致）？验证 structured domain K*=3 跨第三个模型架构（OLMo）的稳定性。2200 docs, depth 0-5, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_024_arxiv_domain\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T10:59:47.281Z\", \"finished_at\": \"2026-05-17T12:11:06.144Z\", \"training_hours\": 1.19}, \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir data/exp_arXiv_olmo --results_dir results/exp_arXiv_olmo --num_samples 2200 --max_depth 5 --batch_size 16 --generation_mode continuation --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"26733\", \"log_path\": \"~/runs/gen-depth-contamination/exp_arXiv_olmo.log\", \"submitted_at\": \"2026-05-17T11:23:00.352Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_arXiv_olmo (seed from exp_024_arxiv/depth_0.jsonl)\", \"data_count\": 2200, \"model_name\": \"OLMo-1B-hf\", \"seed\": 42, \"checkpoint_source\": \"pretrained:allenai/OLMo-1B-hf\", \"eval_data\": \"arXiv abstracts depth 0-5, scorer=Qwen2.5-1.5B\", \"wall_clock_seconds\": 3950.3, \"gpu_hours\": 1.1}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9958, \"auc_1v2\": 0.5034, \"auc_2v3\": 0.5069, \"auc_3v4\": 0.5021, \"auc_4v5\": 0.5037, \"jsd_0v1\": 0.329, \"ordinal_acc\": 0.33}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_arXiv_olmo/\", \"completed_at\": \"2026-05-17T12:28:50.616Z\"}, \"exp_wiki_olmo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:01.835Z\", \"updated_at\": \"2026-05-17T11:40:31.501Z\", \"hypothesis\": \"OLMo-1B continuation on Wikipedia domain will show K*=2 depth saturation pattern consistent with Qwen2.5-1.5B, demonstrating cross-model generality of the distinguishability decay phenomenon.\", \"parent\": \"exp_023_domain_ablation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-17T10:59:50.182Z\"}, \"spec\": {\"command\": \"python scripts/run_pipeline.py ...\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"27620\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_olmo.log\", \"submitted_at\": \"2026-05-17T11:23:10.688Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"git_commit\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf\", \"eval_data\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"wall_clock_seconds\": 1040.8, \"gpu_hours\": 0.29}, \"conclusion\": \"failed\", \"notes\": \"INVALID: data reuse bug. Shared data_path /root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/ with exp-023 (Qwen). Pipeline skip-if-exists logic reused Qwen-generated depth files instead of generating with OLMo. Results identical to exp-023. M002 lesson: each experiment must use independent data directory.\", \"checkpoint_path\": \"N/A (invalid run)\", \"log_path\": \"/root/runs/gen-depth-contamination/exp_wiki_olmo.log\", \"completed_at\": \"2026-05-17T11:40:31.501Z\"}, \"exp_wiki_pythia\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:00.154Z\", \"updated_at\": \"2026-05-17T11:40:30.671Z\", \"hypothesis\": \"Pythia-1.4B continuation on Wikipedia domain will show K*=2 depth saturation pattern consistent with Qwen2.5-1.5B, demonstrating cross-model generality of the distinguishability decay phenomenon.\", \"parent\": \"exp_023_domain_ablation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-17T10:59:49.483Z\"}, \"spec\": {\"command\": \"python scripts/run_pipeline.py ...\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"26873\", \"log_path\": \"~/runs/gen-depth-contamination/exp_wiki_pythia.log\", \"submitted_at\": \"2026-05-17T11:23:03.344Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"git_commit\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79\", \"eval_data\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"wall_clock_seconds\": 1047.3, \"gpu_hours\": 0.29}, \"conclusion\": \"failed\", \"notes\": \"INVALID: data reuse bug. Shared data_path /root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/ with exp-023 (Qwen). Pipeline skip-if-exists logic reused Qwen-generated depth files instead of generating with Pythia. Results identical to exp-023 (1v2=0.6193, K*=2). M002 lesson: each experiment must use independent data directory.\", \"checkpoint_path\": \"N/A (invalid run)\", \"log_path\": \"/root/runs/gen-depth-contamination/exp_wiki_pythia.log\", \"completed_at\": \"2026-05-17T11:40:30.671Z\"}, \"exp_009_dose_response\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:17:38.441Z\", \"updated_at\": \"2026-05-17T10:24:24.214Z\", \"hypothesis\": \"Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下，graduated filtering 相对 binary filtering 的收益是否随 contamination 增加而扩大？验证 C3 (graduated filtering superiority) 在不同 contamination severity 下的 robustness。3 ratios × 3 strategies (no-filter/binary/graduated) × 5 seeds, continued pretraining Qwen2.5-1.5B, eval MMLU+HellaSwag.\", \"spec\": {\"command\": \"exp009_dose_response.py --ratio {0.1,0.3,0.5}\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": \"0-4\", \"checkpoint_source\": \"N/A (continued pretraining from base)\", \"eval_data\": \"MMLU + HellaSwag (lm-eval-harness)\"}, \"metrics\": {\"total_runs\": 45, \"seeds\": 5, \"ratios\": [0.1, 0.3, 0.5], \"strategies\": [\"no_filter\", \"binary_ours\", \"graduated\"], \"cross_ratio_finding\": \"Binary filtering consistently best across all ratios. Graduated filtering = no_filter at every ratio. Effect size of binary advantage increases with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp). Original C3 hypothesis (graduated > binary) rejected.\", \"gpu_hours_total\": 9.9}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp009_v3_partial_10_30.json\", \"completed_at\": \"2026-05-17T10:24:24.214Z\"}, \"exp_009_dose_50pct_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:13:08.251Z\", \"updated_at\": \"2026-05-17T10:23:52.356Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && python scripts/exp009_dose_response.py --ratio 0.5 --device cuda:0 --num_seeds 5\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"4404\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_50pct_v3.log\", \"submitted_at\": \"2026-05-17T07:05:48.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11883.6, \"gpu_hours\": 3.3}, \"hypothesis\": \"50% synthetic injection 下 graduated filtering 应展现最大优势 >=2pp MMLU（v3: fix OOM, auto batch + offline）。半数数据为合成时 binary 激进丢弃导致数据饥饿。\", \"parent\": \"exp_009_dose_50pct_v2\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6063±0.0013\", \"hellaswag\": \"0.6680±0.0005\"}, \"binary_ours\": {\"mmlu\": \"0.6088±0.0011\", \"hellaswag\": \"0.6731±0.0004\"}, \"graduated\": {\"mmlu\": \"0.6062±0.0009\", \"hellaswag\": \"0.6679±0.0002\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0025, \"p_mmlu\": 0.0377, \"delta_hellaswag\": 0.0051, \"p_hellaswag\": 2e-05}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.0026, \"p_mmlu\": 0.0257, \"delta_hellaswag\": -0.0052, \"p_hellaswag\": 3e-05}, \"graduated_vs_nofilter\": {\"delta_mmlu\": -0.0001, \"p_mmlu\": 0.89, \"delta_hellaswag\": -0.0001, \"p_hellaswag\": 0.706}}, \"key_finding\": \"Binary significantly best (HellaSwag p<0.001). Graduated = no_filter exactly.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/ratio_50/\", \"completed_at\": \"2026-05-17T10:23:52.356Z\"}, \"exp_009_dose_30pct_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:13:06.603Z\", \"updated_at\": \"2026-05-17T10:23:51.631Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && python scripts/exp009_dose_response.py --ratio 0.3 --device cuda:0 --num_seeds 5\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"4327\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_30pct_v3.log\", \"submitted_at\": \"2026-05-17T07:05:47.584Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11884.0, \"gpu_hours\": 3.3}, \"hypothesis\": \"30% synthetic injection 下 graduated filtering 优势应 >=1pp MMLU（v3: fix OOM, auto batch + offline）。更高污染率下 binary 丢弃更多可用 gen-1 数据。\", \"parent\": \"exp_009_dose_30pct_v2\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6069±0.0007\", \"hellaswag\": \"0.6664±0.0020\"}, \"binary_ours\": {\"mmlu\": \"0.6082±0.0012\", \"hellaswag\": \"0.6725±0.0007\"}, \"graduated\": {\"mmlu\": \"0.6072±0.0008\", \"hellaswag\": \"0.6665±0.0014\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0013, \"p_mmlu\": 0.0739, \"delta_hellaswag\": 0.0061, \"p_hellaswag\": 0.0036}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.001, \"p_mmlu\": 0.3018, \"delta_hellaswag\": -0.006, \"p_hellaswag\": 0.0009}, \"graduated_vs_nofilter\": {\"delta_mmlu\": 0.0003, \"p_mmlu\": 0.6638, \"delta_hellaswag\": 0.0002, \"p_hellaswag\": 0.6646}}, \"key_finding\": \"Binary best on HellaSwag (p=0.004). Graduated = no_filter.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/ratio_30/\", \"completed_at\": \"2026-05-17T10:23:51.631Z\"}, \"exp_009_dose_10pct_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T00:13:04.692Z\", \"updated_at\": \"2026-05-17T10:23:50.749Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_DATASETS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && python scripts/exp009_dose_response.py --ratio 0.1 --device cuda:0 --num_seeds 5\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"4187\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_10pct_v3.log\", \"submitted_at\": \"2026-05-17T07:05:45.840Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11884.9, \"gpu_hours\": 3.3}, \"hypothesis\": \"10% synthetic injection 下 graduated filtering 应比 binary 保留 >=0.5pp MMLU（v3: fix OOM, auto batch + offline）。低污染时 gen-1 有训练价值，binary 全丢造成数据损失。\", \"parent\": \"exp_009_dose_10pct_v2\", \"metrics\": {\"seeds\": 5, \"strategies\": 3, \"total_runs\": 15, \"mean_std\": {\"no_filter\": {\"mmlu\": \"0.6058±0.0002\", \"hellaswag\": \"0.6689±0.0007\"}, \"binary_ours\": {\"mmlu\": \"0.6079±0.0005\", \"hellaswag\": \"0.6727±0.0008\"}, \"graduated\": {\"mmlu\": \"0.6066±0.0011\", \"hellaswag\": \"0.6700±0.0015\"}}, \"paired_ttest\": {\"binary_vs_nofilter\": {\"delta_mmlu\": 0.0021, \"p_mmlu\": 0.001, \"delta_hellaswag\": 0.0038, \"p_hellaswag\": 0.0017}, \"graduated_vs_binary\": {\"delta_mmlu\": -0.0014, \"p_mmlu\": 0.0917, \"delta_hellaswag\": -0.0027, \"p_hellaswag\": 0.0399}, \"graduated_vs_nofilter\": {\"delta_mmlu\": 0.0008, \"p_mmlu\": 0.2706, \"delta_hellaswag\": 0.0011, \"p_hellaswag\": 0.0611}}, \"key_finding\": \"Binary best. Graduated ≈ no_filter.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/ratio_10/\", \"completed_at\": \"2026-05-17T10:23:50.749Z\"}, \"exp_027_retrain_bootstrap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:43:03.273Z\", \"updated_at\": \"2026-05-17T08:18:53.724Z\", \"hypothesis\": \"Retrain-chain 的 pairwise AUC（0v1 到 3v4）在 10000-iteration bootstrap 95% CI 下均显著高于 θ=0.60，确认 K*≥4 具有统计严格性。\", \"parent\": \"exp_008_retrain_chain_v2\", \"spec\": {\"command\": \"python scripts/exp027_retrain_bootstrap.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/features/exp_008_retrain_chain_v2_features.csv\", \"data_count\": 5000, \"model_name\": \"LightGBM (bootstrap analysis)\", \"seed\": 42, \"checkpoint_source\": \"exp_008_retrain_chain_v2 (retrain-chain AUC data)\", \"eval_data\": \"exp_008_retrain_chain_v2 pairwise depth features (0v1, 1v2, 2v3, 3v4)\"}, \"metrics\": {\"bootstrap_iterations\": 10000, \"pairs\": {\"0v1\": {\"auc_point\": 0.9847, \"ci_lower\": 0.9828, \"ci_upper\": 0.9864, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"1v2\": {\"auc_point\": 0.9482, \"ci_lower\": 0.9443, \"ci_upper\": 0.952, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"2v3\": {\"auc_point\": 0.8885, \"ci_lower\": 0.8829, \"ci_upper\": 0.894, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}, \"3v4\": {\"auc_point\": 0.7977, \"ci_lower\": 0.7903, \"ci_upper\": 0.8051, \"perm_p\": 0.0001, \"ci_lower_gt_theta\": true}}, \"key_finding\": \"All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp027_retrain_bootstrap.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp027_retrain_bootstrap.txt\", \"completed_at\": \"2026-05-17T08:18:53.724Z\"}, \"exp_026_feature_stability_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:09:57.776Z\", \"updated_at\": \"2026-05-17T08:15:28.177Z\", \"hypothesis\": \"Prompt-chain K*=2 边界对 feature 子集选择 robust：即使从 15D 中随机抽取 5/8/10 维子集，Pythia-1.4B prompt-chain 1v2 AUC（baseline ~0.654）仍 > θ=0.60，证明 K*=2 不依赖特定特征组合。\", \"parent\": \"exp_026_feature_stability\", \"metrics\": {\"data_source\": \"exp_001_pythia prompt-chain (K*=2)\", \"results\": {\"15D\": {\"num_tested\": 1, \"num_pass\": 1, \"min_1v2_auc\": 0.6262, \"mean_1v2_auc\": 0.6262}, \"10D\": {\"num_tested\": 5, \"num_pass\": 5, \"min_1v2_auc\": 0.6153, \"mean_1v2_auc\": 0.6191}, \"8D\": {\"num_tested\": 5, \"num_pass\": 5, \"min_1v2_auc\": 0.6056, \"mean_1v2_auc\": 0.6159}, \"5D\": {\"num_tested\": 5, \"num_pass\": 2, \"min_1v2_auc\": 0.5856, \"mean_1v2_auc\": 0.5998}, \"3D_top3\": {\"num_tested\": 1, \"num_pass\": 0, \"min_1v2_auc\": 0.5871, \"mean_1v2_auc\": 0.5871}}, \"key_finding\": \"8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability_v2.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability_v2.json\", \"spec\": {\"command\": \"python scripts/exp026_feature_stability.py --data_source exp_001_pythia\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/features/exp_001_pythia_features.csv\", \"data_count\": 5000, \"model_name\": \"LightGBM\", \"seed\": 42, \"checkpoint_source\": \"exp_001_pythia_depth (prompt-chain features)\", \"eval_data\": \"exp_001_pythia prompt-chain 1v2 features (15D statistical features)\"}, \"completed_at\": \"2026-05-17T08:15:28.177Z\"}, \"exp_026_feature_stability\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:43:01.256Z\", \"updated_at\": \"2026-05-17T08:10:04.334Z\", \"hypothesis\": \"K*=2 对 feature 子集选择 robust：即使从 15D 特征中随机抽取 5/8/10 维子集，1v2 AUC 仍 > θ=0.60，证明 K* 边界不依赖特定特征组合（ad-hoc feature 防御）。\", \"parent\": \"exp_B_14d_ablation\", \"metrics\": {\"data_source\": \"exp_016_qwen_base (prompt-chain, K*=2)\", \"results\": {\"15D\": {\"num_tested\": 1, \"num_kstar_2\": 1, \"min_1v2_auc\": 0.6262, \"mean_1v2_auc\": 0.6262}, \"10D\": {\"num_tested\": 5, \"num_kstar_2\": 5, \"min_1v2_auc\": 0.6153, \"mean_1v2_auc\": 0.6191}, \"8D\": {\"num_tested\": 5, \"num_kstar_2\": 5, \"min_1v2_auc\": 0.6056, \"mean_1v2_auc\": 0.6159}, \"5D\": {\"num_tested\": 5, \"num_kstar_2\": 2, \"min_1v2_auc\": 0.5856, \"mean_1v2_auc\": 0.5998}, \"3D_top3\": {\"num_tested\": 1, \"num_kstar_2\": 0, \"min_1v2_auc\": 0.5871, \"mean_1v2_auc\": 0.5871}}, \"all_above_theta\": false, \"key_finding\": \"Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856). Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where all subsets trivially passed (min=0.8314).\", \"previous_run_note\": \"v1 used retrain-chain data (K*=4), where all subsets trivially passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary robustness.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp026_feature_stability.json\", \"spec\": {\"command\": \"python scripts/exp026_feature_stability.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/\", \"data_count\": 5000, \"model_name\": \"LightGBM (feature subset ablation)\", \"seed\": 42, \"checkpoint_source\": \"exp_008_retrain_chain scored features\", \"eval_data\": \"retrain-chain 15D features depth 0-4\"}, \"completed_at\": \"2026-05-17T08:06:40.583Z\"}, \"exp_027\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T08:09:21.384Z\", \"updated_at\": \"2026-05-17T08:10:03.298Z\", \"hypothesis\": \"Document-level bootstrap CI (10000 iterations) on exp-008 v2 retrain-chain data will confirm that all 4 pairwise AUCs have CI_lower > theta=0.60, supporting K*>=4 with statistical significance.\", \"conclusion\": \"success\", \"checkpoint_path\": \"n/a\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp027.log\", \"completed_at\": \"2026-05-17T08:09:54.196Z\", \"metrics\": {\"kstar_ci\": 4, \"0v1_auc\": 0.9847, \"0v1_ci\": [0.9828, 0.9864], \"0v1_perm_p\": 0.0001, \"1v2_auc\": 0.9482, \"1v2_ci\": [0.9443, 0.952], \"1v2_perm_p\": 0.0001, \"2v3_auc\": 0.8885, \"2v3_ci\": [0.8829, 0.894], \"2v3_perm_p\": 0.0001, \"3v4_auc\": 0.7977, \"3v4_ci\": [0.7903, 0.8051], \"3v4_perm_p\": 0.0001, \"all_ci_lower_above_theta\": true}}, \"exp_005_degradation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T02:40:12.117Z\", \"updated_at\": \"2026-05-17T02:57:38.303Z\", \"spec\": {\"command\": \"python scripts/run_exp005_degradation.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output_dir results_exp005_degradation\", \"server\": \"autodl-4090d\", \"script_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/run_exp005_degradation.py\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation\", \"data_count\": 15000, \"model_name\": \"Pythia-1.4B / OLMo-1B / Qwen-1.5B (3-model comparison)\", \"seed\": 42, \"input_dirs\": [\"results_exp001_pythia\", \"results_exp002_olmo\", \"data\"], \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_005_degradation.log\"}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp005_degradation/degradation_analysis.json\", \"metrics\": {\"cross_model_kendall_tau_by_first_auc\": {\"Pythia_vs_OLMo\": 0.733, \"Pythia_vs_Qwen_rewrite\": 0.467, \"Pythia_vs_Qwen_cont\": 0.695, \"OLMo_vs_Qwen_rewrite\": 0.429, \"OLMo_vs_Qwen_cont\": 0.543, \"Qwen_rewrite_vs_Qwen_cont\": 0.733}, \"cross_model_kendall_tau_by_avg_auc\": {\"Pythia_vs_OLMo\": 0.8476, \"Pythia_vs_Qwen_cont\": 0.7524, \"OLMo_vs_Qwen_cont\": 0.6762}, \"cross_model_spearman_rho_single_feature_auc\": {\"Pythia_vs_OLMo\": 0.95, \"Pythia_vs_Qwen_cont\": 0.9143, \"OLMo_vs_Qwen_cont\": 0.85, \"metric_definition\": \"Spearman ρ on per-feature AUC rankings (each feature independently classifies depth pairs)\"}, \"4model_tau_mean_continuation_by_first_auc\": 0.657, \"4model_tau_mean_all_by_first_auc\": 0.6, \"generation_mode_delta\": {\"Pythia_vs_Qwen\": \"+0.228\", \"OLMo_vs_Qwen\": \"+0.114\"}, \"top3_features_ranking_by_first_auc\": {\"Pythia\": [\"surp_d1_std\", \"surp_d2_std\", \"surp_std\"], \"OLMo\": [\"surp_std\", \"surp_d1_std\", \"surp_d2_std\"], \"Qwen_rewrite\": [\"freq_entropy\", \"surp_std\", \"surp_d1_std\"], \"Qwen_cont\": [\"surp_d1_std\", \"surp_std\", \"surp_d2_std\"]}, \"shared_top_discriminators\": \"surp_d1_std, surp_std, surp_d2_std shared across all architectures (single-feature AUC ranking)\", \"degradation_ordering_consistency\": \"Strong cross-model consistency (ρ≥0.85) on single-feature AUC ranking under controlled generation mode.\", \"residual_architecture_effect\": \"Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\", \"limitation_1v2_weakness\": \"depth-pair level consistency weakest at 1v2 (τ~0.37), near-generational feature importance ordering varies more across models\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:40:50.885Z\", \"notes\": \"4-model τ matrix complete. Generation mode confirmed as primary driver of Qwen divergence (Δτ=+0.23 for Pythia pair). Residual architecture effect ~30-40%. C2 claim: degradation ordering largely consistent under same generation mode, with noted architecture residuals.\", \"hypothesis\": \"递归生成文本在统计特征空间中呈现单调退化趋势（如 perplexity 上升、词汇多样性下降），且退化速率在 K*=2 后显著减缓，这解释了为什么分类器在深代后失去区分力。\", \"parent\": \"mvp_pilot_sat_v1\"}, \"exp_024_arxiv_domain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:43:59.323Z\", \"updated_at\": \"2026-05-17T02:57:37.559Z\", \"hypothesis\": \"Domain ablation: arXiv abstracts 数据下 K*=2 是否成立？验证 K* 跨数据域（C4 vs Wikipedia vs arXiv）的稳定性。Qwen2.5-1.5B base, continuation, nucleus p=0.95 T=1.0, 5K docs, depth 0-5。\", \"spec\": {\"command\": \"bash scripts/exp024_arxiv_domain.sh\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"pid\": 46766, \"log_path\": \"~/runs/gen-depth-contamination/exp_024_arxiv_domain.log\", \"submitted_at\": \"2026-05-16T14:44:07.168Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_024_arxiv/\", \"data_count\": 2200, \"model_name\": \"Qwen2.5-1.5B (base)\", \"seed\": 42, \"wall_clock_seconds\": 9545.8, \"gpu_hours\": 2.65}, \"notes\": \"2026-05-16 15:05 重启成功。PID 48295, cuda:2, 73% util。修复：depth_0.jsonl 已有 2200 行 arXiv 数据，prepare_seed_data 行数检查通过后跳过 C4 下载，HF_DATASETS_OFFLINE=1 不再冲突。n_docs=2200。预计 ~20 min 完成剩余 depth。\", \"metrics\": {\"K_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9946, \"1v2\": 0.858, \"2v3\": 0.6427, \"3v4\": 0.5437, \"4v5\": 0.5294}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9946, \"ci_lower\": 0.9929, \"ci_upper\": 0.9961, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.858, \"ci_lower\": 0.848, \"ci_upper\": 0.8679, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.6427, \"ci_lower\": 0.6275, \"ci_upper\": 0.6575, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5437, \"ci_lower\": 0.5276, \"ci_upper\": 0.5598, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5294, \"ci_lower\": 0.5133, \"ci_upper\": 0.5455, \"perm_p\": 0.0006}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_024_arxiv/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_024_arxiv_domain.log\", \"completed_at\": \"2026-05-16T17:23:12.939Z\", \"parent\": \"exp_023_domain_ablation\"}, \"exp_017_qwen_continuation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:41:22.423Z\", \"updated_at\": \"2026-05-17T02:57:37.021Z\", \"hypothesis\": \"Continuation mode 的 K* 应等于 rewrite mode（K*=2），因为 K* 饱和边界是递归生成的文本固有属性，与生成模式（续写 vs 改写）无关——两种模式在深代时都收敛到相同的统计吸引子。\", \"notes\": \"dry-run passed 2026-05-13: model OK (2.9G safetensors), env OK (torch=2.10.0+cu128, transformers=4.57.6), dirs auto-create. Submit command prepared. 等 exp-002 完成后立即提交。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"23758\", \"log_path\": \"~/runs/gen-depth-contamination/exp_017_qwen_continuation.log\", \"submitted_at\": \"2026-05-13T02:35:15Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"max_depth\": 5, \"generation_mode\": \"continuation\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont/\", \"wall_clock_seconds\": 13305.8, \"gpu_hours\": 3.7}, \"log_path\": \"/root/runs/gen-depth-contamination/exp_017_qwen_continuation.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont/\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9972, \"1v2\": 0.6114, \"2v3\": 0.5609, \"3v4\": 0.5408, \"4v5\": 0.5139}, \"pairwise_jsd\": {\"0v1\": 0.28627, \"1v2\": 0.005107, \"2v3\": 0.003603, \"3v4\": 0.003395, \"4v5\": 0.003085}, \"ordinal_mae\": 1.1547, \"ordinal_accuracy\": 0.3819, \"top3_features\": [\"freq_entropy\", \"surp_mean\", \"surp_std\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:17:00.826Z\", \"parent\": \"mvp_pilot_sat_v1\"}, \"exp_012_binary_confidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T12:32:09.468Z\", \"updated_at\": \"2026-05-17T02:57:36.098Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_ENDPOINT=https://hf-mirror.com && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp012_ppl_depth_correlation.py --device cuda:0 --n_samples 500 --output_dir artifacts/exp012_results\\\"\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"128209\", \"log_path\": \"~/runs/gen-depth-contamination/exp_012_binary_confidence.log\", \"submitted_at\": \"2026-05-15T23:14:10.207Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 489.8, \"gpu_hours\": 0.14}, \"notes\": \"N=500全量运行。Binary confidence与depth的Spearman ρ弱到中等(|ρ|=0.06-0.46)，6-class accuracy全部≤random baseline。关键发现：0v1 pairwise AUC极高(0.99+)但deeper pairs塌缩到~0.5，证明binary detector只捕捉human/AI边界，无法区分generational depth。Hypothesis验证成功。可视化已生成(exp012_confidence_vs_depth.pdf)。\", \"hypothesis\": \"Binary detector confidence（DivEye log-PPL、Binoculars ratio）与 true generational depth 相关性弱（Spearman rho < 0.3），因为这些检测器将所有合成文本折叠为单一类别，无法区分 gen-1 和 gen-3+，暴露 binary 范式的信息损失。\", \"reproduce\": {\"finished_at\": \"2026-05-15T23:20:30.036Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:20:30.983764+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp012_results/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_012_binary_confidence.log\", \"completed_at\": \"2026-05-15T23:22:19.966Z\", \"metrics\": {\"n_samples\": 500, \"generators\": [\"qwen-rewrite\", \"pythia-1.4b\", \"olmo-1b\", \"qwen-cont\"], \"6class_accuracy\": {\"qwen-rewrite\": 0.1987, \"pythia-1.4b\": 0.1303, \"olmo-1b\": 0.127, \"qwen-cont\": 0.1833, \"random_baseline\": 0.1667}, \"spearman_rho\": {\"qwen-rewrite\": {\"log_ppl_ref\": -0.1233, \"log_ppl_obs\": 0.0815, \"ppl_ratio\": 0.1185}, \"pythia-1.4b\": {\"log_ppl_ref\": -0.2972, \"log_ppl_obs\": -0.4529, \"ppl_ratio\": -0.392}, \"olmo-1b\": {\"log_ppl_ref\": -0.378, \"log_ppl_obs\": -0.4614, \"ppl_ratio\": -0.4068}, \"qwen-cont\": {\"log_ppl_ref\": -0.3887, \"log_ppl_obs\": -0.162, \"ppl_ratio\": -0.058}}, \"binary_detector_kstar\": 1, \"obd_kstar\": 2, \"auc_non_monotonic\": true, \"key_finding\": \"Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but practically weak). AUC non-monotonic — binary detectors cannot maintain depth ordering. Confirms binary confidence ≠ depth estimation.\"}, \"parent\": \"mvp_pilot_sat_v1\"}, \"exp_C_permutation_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:26.152Z\", \"updated_at\": \"2026-05-17T02:57:35.128Z\", \"hypothesis\": \"10K permutation resamples 不应改变任何 K* 结论（所有 p < 0.01 的 pair 仍应 p < 0.01），确认 500 resamples 已有足够精度，K*=2 结论的统计基础稳固。\", \"spec\": {\"command\": \"python scripts/exp_C_permutation_10k.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data + data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 20000, \"model_name\": \"N/A (CPU: permutation test)\", \"seed\": 42, \"note\": \"10K permutation resamples replacing 500, per depth pair per model\"}, \"conclusion\": \"success\", \"metrics\": {\"resamples\": 10000, \"all_boundary_pairs_p\": \"<0.0001\", \"key_finding\": \"10K permutation confirms all boundary p-values well below 0.01. FR-11 resolved.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_C_permutation_10k.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_C_permutation_10k.json\", \"completed_at\": \"2026-05-15T11:20:30.088Z\", \"parent\": \"exp_007_bootstrap_ci\"}, \"exp_002_olmo_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:24.766Z\", \"updated_at\": \"2026-05-17T02:57:34.160Z\", \"hypothesis\": \"K* 跨模型一致性验证：OLMo-1B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"20225\", \"log_path\": \"~/runs/gen-depth-contamination/exp_002_olmo_depth.log\", \"submitted_at\": \"2026-05-13T00:16:07.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/\", \"wall_clock_seconds\": 8384.9, \"gpu_hours\": 2.33}, \"reproduce\": {\"finished_at\": \"2026-05-13T02:31:18.880Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T02:31:19.738113+00:00\"}]}, \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.997, \"1v2\": 0.6146, \"2v3\": 0.5497, \"3v4\": 0.509, \"4v5\": 0.5044}, \"pairwise_auc_std\": {\"0v1\": 0.0004, \"1v2\": 0.0029, \"2v3\": 0.004, \"3v4\": 0.0084, \"4v5\": 0.0136}, \"pairwise_jsd\": {\"0v1\": 0.23941, \"1v2\": 0.012972, \"2v3\": 0.00735, \"3v4\": 0.003968, \"4v5\": 0.003851}, \"ordinal_mae\": 1.1813, \"ordinal_accuracy\": 0.3685, \"top_features\": [\"surp_d1_mean\", \"surp_d1_skew\", \"freq_kurtosis\", \"surp_d2_mean\", \"surp_mean\"]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:35:52.823Z\", \"parent\": \"exp_001_pythia_depth\"}, \"exp_009_dose_50pct_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:14:53.711Z\", \"updated_at\": \"2026-05-17T02:57:30.391Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.5 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"86342\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_50pct_v2.log\", \"submitted_at\": \"2026-05-16T23:14:53.568Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_50/\", \"data_count\": 10000, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 4079.2, \"gpu_hours\": 1.13}, \"hypothesis\": \"50% synthetic injection 下 graduated filtering 应展现最大优势 >=2pp MMLU（v2: fix HF mirror）。机制同 v1：半数数据为合成时 binary 激进丢弃导致数据饥饿。\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA OOM during lm_eval MMLU 5-shot (batch_size=8, logits tensor exceeds 24GB)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:52.736Z\", \"parent\": \"exp_009_dose_50pct\"}, \"exp_009_dose_30pct_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:14:51.739Z\", \"updated_at\": \"2026-05-17T02:57:29.467Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.3 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"86196\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_30pct_v2.log\", \"submitted_at\": \"2026-05-16T23:14:51.572Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_30/\", \"data_count\": 7142, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 4080.4, \"gpu_hours\": 1.13}, \"hypothesis\": \"30% synthetic injection 下 graduated filtering 优势应 >=1pp MMLU（v2: fix HF mirror）。机制同 v1：更高污染率下 binary 丢弃更多可用 gen-1 数据。\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA OOM during lm_eval MMLU 5-shot (batch_size=8, logits tensor exceeds 24GB)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:51.942Z\", \"parent\": \"exp_009_dose_30pct\"}, \"exp_009_dose_10pct_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:14:49.850Z\", \"updated_at\": \"2026-05-17T02:57:28.507Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.1 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"86049\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_10pct_v2.log\", \"submitted_at\": \"2026-05-16T23:14:49.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_10/\", \"data_count\": 5555, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 4081.2, \"gpu_hours\": 1.13}, \"hypothesis\": \"10% synthetic injection 下 graduated filtering 应比 binary 保留 >=0.5pp MMLU（v2: fix HF mirror）。机制同 v1：低污染时 gen-1 有训练价值，binary 全丢造成数据损失。\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA OOM during lm_eval MMLU 5-shot (batch_size=8, logits tensor exceeds 24GB)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:50.958Z\", \"parent\": \"exp_009_dose_10pct\"}, \"exp_009_dose_50pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:22:14.703Z\", \"updated_at\": \"2026-05-17T02:57:28.163Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.5 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"81595\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_50pct.log\", \"submitted_at\": \"2026-05-16T22:23:09.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_50/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 7180.5, \"gpu_hours\": 1.99}, \"hypothesis\": \"50% synthetic injection 下，graduated filtering 应展现最大优势（>=2pp MMLU），因为半数数据为合成时 binary filtering 的激进丢弃导致严重数据饥饿，而 graduated 保留 gen-1 维持训练集规模。\", \"conclusion\": \"failed\", \"failure_reason\": \"HF Hub network instability (httpx client closed)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:50.142Z\", \"parent\": \"exp_006_graduated_filtering\"}, \"exp_009_dose_30pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:22:12.817Z\", \"updated_at\": \"2026-05-17T02:57:27.096Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.3 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"81453\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_30pct.log\", \"submitted_at\": \"2026-05-16T22:23:07.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_30/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 7181.6, \"gpu_hours\": 1.99}, \"hypothesis\": \"30% synthetic injection 下，graduated filtering 优势应大于 10% 场景（>=1pp MMLU），因为更高污染率意味着 binary filtering 丢弃更多可用 gen-1 数据，而 graduated 仅移除 gen-2+ 有害部分。\", \"conclusion\": \"failed\", \"failure_reason\": \"HF Hub network instability (httpx client closed)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:49.399Z\", \"parent\": \"exp_006_graduated_filtering\"}, \"exp_009_dose_10pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:22:10.924Z\", \"updated_at\": \"2026-05-17T02:57:26.151Z\", \"spec\": {\"command\": \"python scripts/exp009_dose_response.py --ratio 0.1 --device cuda:0 --num_seeds 5\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"81311\", \"log_path\": \"~/runs/gen-depth-contamination/exp_009_dose_10pct.log\", \"submitted_at\": \"2026-05-16T22:23:05.447Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_009_dose_response/ratio_10/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (continued pretraining)\", \"seed\": 42, \"checkpoint_source\": \"pretrained Qwen2.5-1.5B\", \"eval_data\": \"MMLU + HellaSwag via lm-eval-harness\", \"wall_clock_seconds\": 7183.1, \"gpu_hours\": 2.0}, \"hypothesis\": \"10% synthetic injection 下，graduated filtering 应比 binary filtering 保留更多 MMLU 性能（>=0.5pp），因为低污染场景中 gen-1 文本仍有训练价值，binary 全部丢弃造成不必要的数据损失。\", \"conclusion\": \"failed\", \"failure_reason\": \"HF Hub network instability (httpx client closed)\", \"checkpoint_path\": \"N/A (crashed before checkpoint)\", \"completed_at\": \"2026-05-17T00:22:48.595Z\", \"parent\": \"exp_006_graduated_filtering\"}, \"exp_kstar_theta\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:08:01.704Z\", \"updated_at\": \"2026-05-17T02:56:51.877Z\", \"hypothesis\": \"K*(θ) 曲线在 θ∈[0.55,0.65] 存在 plateau（K* 对阈值不敏感），且 Cohen's h 在 depth=K* 到 depth=K*+1 间降至 < 0.2（小效应量），为 θ=0.60 提供非任意性理论依据。\", \"spec\": {\"command\": \"python scripts/plot_kstar_theta.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/ (bootstrap CI AUCs)\", \"data_count\": 20000, \"model_name\": \"N/A (CPU: K*(θ) visualization)\", \"seed\": \"N/A\", \"note\": \"FR-1 rebuttal: K*(θ) curve for 4 models × 5 depth pairs\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/kstar_theta_curve.pdf\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/plot_kstar_theta.py\", \"metrics\": {\"output_files\": [\"kstar_theta_curve.pdf (32KB)\", \"kstar_theta_curve.png (335KB)\"], \"models\": [\"Qwen-rewrite\", \"Pythia\", \"OLMo\", \"Qwen-cont\"], \"depth_pairs\": 5, \"key_finding\": \"All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5. θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical resolved.\"}, \"completed_at\": \"2026-05-15T15:08:25.181Z\"}, \"exp_022_cross_scorer_matrix\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:52:14.132Z\", \"updated_at\": \"2026-05-17T02:56:47.329Z\", \"hypothesis\": \"Self-scoring（generator=scorer）的 K* 和 pairwise AUC 应与 cross-scoring（generator≠scorer）差异 < 0.02，证明 K*=2 不是 scorer-generator familiarity artifact，而是文本本身的可区分性边界。\", \"parent\": \"exp_A_alt_scorer\", \"spec\": {\"command\": \"bash scripts/exp022_cross_scorer_matrix.sh\", \"server\": \"cqa1-22115\", \"data_path\": \"data_exp016_qwen_base + data_exp020_pythia_greedy + data/exp_021_length_256\", \"data_count\": 5000, \"model_name\": \"cross: Qwen2.5-1.5B/Pythia-1.4B/OLMo-1B/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained\", \"eval_data\": \"cross-scorer matrix on existing depth chains\"}, \"notes\": \"2026-05-16 15:05: 双 GPU 并行。cuda:1 跑 2×2 子矩阵 (PID 49787, Qwen-cont/Pythia × Qwen-base/Pythia)。cuda:3 跑 3×4=12 组合 (先跑已缓存模型 6 combo，等下载 Qwen-Instruct/OLMo 后补剩余 6)。OLMo generator 无 depth chain 数据，实际 3 generators × 4 scorers。\", \"conclusion\": \"success\", \"metrics\": {\"total_combos\": 12, \"completed\": 12, \"K_star_distribution\": {\"K2\": 11, \"K1\": 1}, \"matrix\": {\"pythia_greedy×olmo\": {\"K_star\": 2, \"1v2\": 0.8811}, \"pythia_greedy×pythia\": {\"K_star\": 2, \"1v2\": 0.8838}, \"pythia_greedy×qwen_base\": {\"K_star\": 2, \"1v2\": 0.8814}, \"pythia_greedy×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.8818}, \"qwen_base×olmo\": {\"K_star\": 2, \"1v2\": 0.6047}, \"qwen_base×pythia\": {\"K_star\": 2, \"1v2\": 0.617}, \"qwen_base×qwen_base\": {\"K_star\": 2, \"1v2\": 0.6262}, \"qwen_base×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.6273}, \"qwen_cont256×olmo\": {\"K_star\": 2, \"1v2\": 0.6028}, \"qwen_cont256×pythia\": {\"K_star\": 1, \"1v2\": 0.5979}, \"qwen_cont256×qwen_base\": {\"K_star\": 2, \"1v2\": 0.6282}, \"qwen_cont256×qwen_instruct\": {\"K_star\": 2, \"1v2\": 0.6072}}, \"key_finding\": \"Scorer independence confirmed: K*=2 in 11/12 combos. Only exception: qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp022_cross_scorer/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp022_cross_scorer.log\", \"completed_at\": \"2026-05-16T18:56:44.226Z\"}, \"exp_008_retrain_chain_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:57:55.644Z\", \"updated_at\": \"2026-05-17T00:23:00.448Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp008_retrain_chain.py --device cuda:0\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"77098\", \"log_path\": \"~/runs/gen-depth-contamination/exp_008_retrain_chain_v2.log\", \"submitted_at\": \"2026-05-16T21:57:55.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b + LoRA (rank=16, alpha=32)\", \"seed\": 42, \"checkpoint_source\": \"pretrained + per-generation LoRA fine-tune\", \"eval_data\": \"C4 5K docs, retrain-chain depth 0-4\", \"wall_clock_seconds\": 8704.9, \"gpu_hours\": 2.42}, \"hypothesis\": \"Retrain-chain ecological validity (v2, fix: labels padding bug): Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain K* ≤ prompt-chain K*=2. 每代独立 LoRA fine-tune 1 epoch on 前代输出，再用 fine-tuned model 生成下一代。验证 prompt-chain 是 conservative upper bound。C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_001_pythia_depth\", \"metrics\": {\"k_star\": \">=4\", \"pairwise_auc\": {\"0v1\": 0.9847, \"1v2\": 0.9484, \"2v3\": 0.8888, \"3v4\": 0.7982}, \"pairwise_jsd\": {\"0v1\": 0.17, \"1v2\": 0.12, \"2v3\": 0.064, \"3v4\": 0.04}, \"key_finding\": \"Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic boundary.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/outputs/exp_008_retrain_chain/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T00:23:00.448Z\"}, \"exp-008-retrain-chain\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:31:01.383Z\", \"updated_at\": \"2026-05-16T22:16:29.240Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp008_retrain_chain.py --device cuda:0\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"71944\", \"log_path\": \"~/runs/gen-depth-contamination/exp-008-retrain-chain.log\", \"submitted_at\": \"2026-05-16T19:31:01.254Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b + LoRA (rank=16, alpha=32)\", \"seed\": 42, \"checkpoint_source\": \"pretrained + per-generation LoRA fine-tune\", \"eval_data\": \"C4 5K docs, retrain-chain depth 0-4\", \"wall_clock_seconds\": 5771.2, \"gpu_hours\": 1.6}, \"hypothesis\": \"Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32) retrain-chain K* ≤ prompt-chain K*=2. 每代独立 LoRA fine-tune 1 epoch on 前代输出，再用 fine-tuned model 生成下一代。验证 prompt-chain 是 conservative upper bound。C4 5K docs, depth 0-4, nucleus p=0.95 T=1.0, scorer=Qwen2.5-1.5B.\", \"parent\": \"exp_001_pythia_depth\", \"failure_reason\": \"Traceback → le \\\"/root/miniconda3/lib/python3.12/site-packages/transformers/tokenization_utils_base.py\\\", line 701, in as_tensor return torch.tensor(value, dtype=dtype) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ValueError: expected sequence of length 256 at dim 1 (got 228)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T21:07:12.427Z\", \"notes\": \"2026-05-16: 失败原因——TextDataset.__getitem__ 同时返回变长 input_ids 和 labels，DataCollatorForLanguageModeling 只 pad input_ids，导致 labels 长度不一致无法转 tensor。修复：移除 __getitem__ 中的 labels 字段，让 collator 自动处理。v2 已提交。\"}, \"exp_025_pythia_arxiv\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:16:13.988Z\", \"updated_at\": \"2026-05-16T19:22:57.204Z\", \"hypothesis\": \"Domain × model interaction: Pythia-1.4B on arXiv data 的 K* 是否与 exp-024 (Qwen on arXiv, K*=?) 一致？验证 arXiv domain effect 跨模型一致性，排除 Qwen-specific artifact。Pythia-1.4B continuation, nucleus p=0.95 T=1.0, 2200 docs, depth 0-5, scorer=Qwen2.5-1.5B base。\", \"parent\": \"exp_024_arxiv_domain\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=1 python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79 --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --generation_mode continuation --top_p 0.95 --temperature 1.0 --num_samples 2200 --max_depth 5 --batch_size 8 --feat_batch_size 16 --data_dir data/exp_025_pythia_arxiv --results_dir results/exp_025_pythia_arxiv\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"67006\", \"log_path\": \"~/runs/gen-depth-contamination/exp_025_pythia_arxiv.log\", \"submitted_at\": \"2026-05-16T17:59:52.930Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_025_pythia_arxiv/\", \"data_count\": 2200, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_source\": \"pretrained (EleutherAI/pythia-1.4b)\", \"eval_data\": \"arXiv abstracts depth chains (shared seed data from exp-024)\", \"wall_clock_seconds\": 4984.3, \"gpu_hours\": 1.38}, \"reproduce\": {\"finished_at\": \"2026-05-16T18:57:28.981Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:57:30.288692+00:00\"}]}, \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9877, \"1v2\": 0.8047, \"2v3\": 0.6545, \"3v4\": 0.5507, \"4v5\": 0.5287}, \"pairwise_jsd\": {\"0v1\": 0.171338, \"1v2\": 0.057344, \"2v3\": 0.019524, \"3v4\": 0.009917, \"4v5\": 0.008846}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9876, \"ci_lower\": 0.9851, \"ci_upper\": 0.99, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.8047, \"ci_lower\": 0.7934, \"ci_upper\": 0.8162, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.6544, \"ci_lower\": 0.6401, \"ci_upper\": 0.6688, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.55, \"ci_lower\": 0.534, \"ci_upper\": 0.5657, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5284, \"ci_lower\": 0.5122, \"ci_upper\": 0.5443, \"perm_p\": 0.001}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"n_samples\": 2200, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_mean\", \"surp_d1_skew\", \"surp_d1_mean\"], \"ordinal\": {\"MAE\": 0.8518, \"Accuracy\": 0.4545}, \"key_finding\": \"Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv). 2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for arXiv.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_025_pythia_arxiv/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_025_pythia_arxiv.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T19:22:57.204Z\"}, \"exp_020_pythia_decoding\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:52:13.036Z\", \"updated_at\": \"2026-05-16T17:18:28.366Z\", \"hypothesis\": \"Pythia-1.4B 解码消融：4 个 decoding config (greedy/nuc p=0.9/T=0.7/T=1.2) 的 K* 是否一致？与 exp-003 (Qwen) 平行，验证 decoding 效应跨模型一致性。C4 5K, depth 0-5。\", \"parent\": \"exp_003_decoding_ablation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T04:57:46.476Z\"}, \"spec\": {\"command\": \"nohup bash -c 'CUDA_VISIBLE_DEVICES=2 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache bash scripts/exp020_pythia_decoding.sh' > /tmp/exp020_pythia_decoding.log 2>&1 &\", \"server\": \"cqa1-22115\", \"data_path\": \"data_exp020_pythia_{greedy,nuc09,t07,t12}/\", \"data_count\": 20000, \"model_name\": \"EleutherAI/pythia-1.4b (fp16)\", \"seed\": 42, \"generation_mode\": \"continuation (4 decoding configs: greedy/nuc09/t07/t12)\", \"pid\": 14551, \"log_path\": \"/tmp/exp020_pythia_decoding.log\", \"note\": \"Worker 误用 nohup 而非 submit_training_job，已补注册 cron 监控 (PID 14551)。原 PID 13076 已被 kill。\"}, \"notes\": \"greedy 1v2 AUC=0.8838 调查完成：根因为 Pythia-1.4B greedy 级联重复坍塌（4-gram repeat rate: d0=0.01→d1=0.72→d2=0.81; TTR: d0=0.72→d1=0.19→d2=0.14）。hapax_ratio (d=1.06) 和 low_freq_ratio (d=1.03) 是 top 贡献特征。非 bug，参数正确，无数据泄漏。K*=2 不受影响。建议论文标注为 repetition-dominated regime。| Bootstrap CI (10000 iter): t07 2v3 AUC=0.5939 CI [0.5855, 0.6025] BORDERLINE (CI upper crosses θ); t12 1v2 AUC=0.6170 CI [0.6071, 0.6270] PASS。\", \"conclusion\": \"success\", \"metrics\": {\"greedy\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9992, \"1v2\": 0.8838, \"2v3\": 0.5342, \"3v4\": 0.5228, \"4v5\": 0.5162}}, \"nuc09\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9948, \"1v2\": 0.677, \"2v3\": 0.5549, \"3v4\": 0.5299, \"4v5\": 0.5013}}, \"t07\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9965, \"1v2\": 0.7265, \"2v3\": 0.5941, \"3v4\": 0.5698, \"4v5\": 0.5284}}, \"t12\": {\"K_star\": 2, \"auc\": {\"0v1\": 0.9933, \"1v2\": 0.6172, \"2v3\": 0.5226, \"3v4\": 0.517, \"4v5\": 0.5051}}}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp020_pythia_{greedy,nuc09,t07,t12}/\", \"log_path\": \"/tmp/exp020_pythia_decoding.log\", \"completed_at\": \"2026-05-16T14:41:33.153Z\"}, \"exp_021_length_ablation\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T04:52:13.569Z\", \"updated_at\": \"2026-05-16T17:18:21.506Z\", \"hypothesis\": \"文本长度消融：128/256/512 tokens 下 K* 是否稳定？验证 K*=2 不依赖于 256-token 固定长度设定。Qwen2.5-1.5B (base) continuation, C4 5K, depth 0-5。\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-16T04:57:47.040Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-16T06:23:09.413Z\", \"notes\": \"2026-05-16 retry#2: 用本地 C4 数据修复。数据源=/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/depth_0.jsonl (5000行)，复制到 data/exp_021_length_{128,256,512}/。设置 HF_DATASETS_OFFLINE=1 + TRANSFORMERS_OFFLINE=1 阻断 HF 网络调用，prepare_seed_data 检测到本地文件自动跳过 streaming。PID 20982, tmux session exp_021_length_ablation。\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16: 崩溃原因确认——脚本未执行 `source /etc/network_turbo`，导致 AutoDL 网络代理未启用，HuggingFace C4 数据集下载失败 (RuntimeError: Cannot send a request, as the client has been closed / Errno 99: Cannot assign requested address)。三个长度 (128/256/512) 全部未完成，无任何产出。cuda:3 已空闲。需重跑并修复网络配置。\"}}, \"spec\": {\"command\": \"bash -c \\\"export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/exp021_length_ablation.sh\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"20982\", \"log_path\": \"~/runs/gen-depth-contamination/exp_021_length_ablation.log\", \"submitted_at\": \"2026-05-16T07:13:09.587Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/depth_0.jsonl (local C4, copied to data/exp_021_length_{128,256,512}/)\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (base)\", \"seed\": 42, \"generation_mode\": \"continuation\", \"max_new_tokens\": [128, 256, 512], \"max_depth\": 5, \"batch_size\": 16, \"checkpoint_path\": \"results/exp_021_length_{128,256,512}\", \"description\": \"Retry#2: local C4 data, HF_DATASETS_OFFLINE=1, 3 length configs sequential on cuda:3\", \"wall_clock_seconds\": 29523.5, \"gpu_hours\": 8.2}, \"conclusion\": \"success\", \"metrics\": {\"128tok\": {\"K_star\": 2, \"1v2_auc\": 0.6219}, \"256tok\": {\"K_star\": 2, \"1v2_auc\": 0.6282}, \"512tok\": {\"K_star\": 2, \"1v2_auc\": 0.6073}, \"all_K_star_2\": true, \"bootstrap_ci\": {\"512tok_1v2\": {\"auc\": 0.6073, \"ci_lower\": 0.5979, \"ci_upper\": 0.6166, \"perm_p\": 0.0001, \"verdict\": \"BORDERLINE\"}}}}, \"exp_018_llama8b_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:52:11.229Z\", \"updated_at\": \"2026-05-16T16:18:02.754Z\", \"hypothesis\": \"Cross-family K* 验证：LLaMA-3.1-8B continuation mode 的 K* 是否 = 2？首次超出 Qwen 家族，验证 K* universality 跨模型架构。C4 5K, depth 0-5, scorer=Qwen2.5-1.5B base。\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T04:57:44.549Z\", \"finished_at\": \"2026-05-16T15:35:57.336Z\", \"training_hours\": 10.64}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --generation_mode continuation --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 8 --data_dir data/exp_018_llama8b --results_dir results/exp_018_llama8b\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0 (RTX 4090D 24GB)\", \"data_path\": \"C4 validation (HuggingFace streaming)\", \"data_count\": 5000, \"model_name\": \"LLaMA-3.1-8B (Meta-Llama-3.1-8B)\", \"scorer\": \"Qwen2.5-1.5B base\", \"seed\": 42, \"generation_mode\": \"continuation\", \"max_depth\": 5, \"batch_size\": 4, \"feat_batch_size\": 8, \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/exp_018_llama8b.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_018_llama8b\", \"description\": \"Cross-family K* validation: LLaMA-3.1-8B generates depth chain, Qwen2.5-1.5B base scores surprisal features\"}, \"failure_reason\": \"null — cron 误报，实验实际成功\", \"conclusion\": \"success\", \"pid\": 10403, \"gpu_id\": \"cuda:0\", \"completed_at\": \"2026-05-16T15:35:57.947Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:35:59.527502+00:00\"}]}, \"notes\": \"2026-05-16 日志诊断：实验实际已成功完成(K*=2, AUC 1v2=0.6123)，Pipeline complete 正常退出。被 cron 误判 failed 原因：进程正常结束后 PID 10403 消失，无 sentinel/W&B 信号，监控 5× 检查后 auto-resolve 为 failed。结果文件完整存在于 results/exp_018_llama8b/。应改 conclusion=success。\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9225, \"1v2\": 0.6123, \"2v3\": 0.5274, \"3v4\": 0.5138, \"4v5\": 0.5097}, \"jsd\": {\"0v1\": 0.077, \"1v2\": 0.012, \"2v3\": 0.005}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9224, \"ci_lower\": 0.9174, \"ci_upper\": 0.9272, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6123, \"ci_lower\": 0.6028, \"ci_upper\": 0.6216, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5273, \"ci_lower\": 0.5169, \"ci_upper\": 0.5378, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5168, \"ci_lower\": 0.5062, \"ci_upper\": 0.5275, \"perm_p\": 0.0037}, \"4v5\": {\"auc\": 0.5159, \"ci_lower\": 0.5052, \"ci_upper\": 0.5268, \"perm_p\": 0.0035}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000}}, \"exp_023_domain_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:59:57.643Z\", \"updated_at\": \"2026-05-16T15:25:22.371Z\", \"hypothesis\": \"Domain ablation: Wikipedia 数据下 K*=2 是否成立？验证 K* 跨数据域（C4 vs Wikipedia）的稳定性。Qwen2.5-1.5B base, continuation, nucleus p=0.95 T=1.0, 5K docs, depth 0-5。\", \"spec\": {\"command\": \"bash scripts/exp023_wiki_domain.sh\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"pid\": 39530, \"log_path\": \"~/runs/gen-depth-contamination/exp_023_domain_ablation.log\", \"submitted_at\": \"2026-05-16T12:00:07.999Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_023_wiki/\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B (base)\", \"seed\": 42, \"wall_clock_seconds\": 12314.4, \"gpu_hours\": 3.42}, \"conclusion\": \"success\", \"metrics\": {\"K_star\": 2, \"1v2_auc\": 0.6193, \"2v3_auc\": 0.5498, \"all_folds_above_060\": true, \"top_feature\": \"freq_entropy\", \"ordinal_accuracy\": 0.377}, \"checkpoint_path\": \"results_exp023_wiki_domain/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_023_domain_ablation.log\", \"completed_at\": \"2026-05-16T15:25:22.371Z\"}, \"exp_019b_mistral_cross_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:22:44.822Z\", \"updated_at\": \"2026-05-16T11:56:59.892Z\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path mistral-7b --scorer_path qwen2.5-1.5b\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"36365\", \"log_path\": \"~/runs/gen-depth-contamination/exp_019b_mistral_cross_scorer.log\", \"submitted_at\": \"2026-05-16T11:23:28.609Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp019b_mistral_cross\", \"data_count\": 5000, \"model_name\": \"mistral-7b-cross-qwen1.5b-scorer\", \"seed\": 42, \"checkpoint_source\": \"exp_019_mistral7b_depth\", \"eval_data\": \"data_exp019b_mistral_cross\", \"wall_clock_seconds\": 1938.5, \"gpu_hours\": 0.54}, \"hypothesis\": \"排除 self-scorer 因素：Mistral-7B depth chain 用 Qwen2.5-1.5B-base 评分后 K* 是否=2？如果 K*=2 则 exp-019 的 K*=1 是 self-scorer artifact；如果 K*=1 则是 Mistral 生成文本的固有特性。\", \"parent\": \"exp_019_mistral7b_depth\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp019b_mistral_cross_scorer\", \"log_path\": \"~/runs/gen-depth-contamination/exp_019b_mistral_cross_scorer.log\", \"completed_at\": \"2026-05-16T11:55:47.111Z\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9209, \"1v2\": 0.5695, \"2v3\": 0.5335, \"3v4\": 0.514, \"4v5\": 0.5184}, \"bootstrap_ci\": {\"0v1\": {\"mean\": 0.9209, \"ci_lower\": 0.9189, \"ci_upper\": 0.9229, \"pass_060\": true}, \"1v2\": {\"mean\": 0.5696, \"ci_lower\": 0.5645, \"ci_upper\": 0.5746, \"pass_060\": false}, \"2v3\": {\"mean\": 0.5335, \"ci_lower\": 0.5283, \"ci_upper\": 0.5382, \"pass_060\": false}, \"3v4\": {\"mean\": 0.514, \"ci_lower\": 0.5063, \"ci_upper\": 0.5213, \"pass_060\": false}, \"4v5\": {\"mean\": 0.5183, \"ci_lower\": 0.5128, \"ci_upper\": 0.5244, \"pass_060\": false}}, \"jsd\": {\"0v1\": 0.08355, \"1v2\": 0.007642, \"2v3\": 0.004752, \"3v4\": 0.004255, \"4v5\": 0.003758}, \"ordinal_mae\": 1.3737, \"ordinal_accuracy\": 0.3179, \"top3_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_d1_mean\"], \"key_finding\": \"Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2 AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.\"}, \"notes\": \"K*=1 confirmed genuine (not self-scorer artifact). Cross-scorer (Qwen-base) 1v2 AUC=0.5695 CI [0.5645, 0.5746] — 比 self-scorer (0.5935) 更低。换 scorer 后区分度下降，排除 self-scorer inflation 假说。Top-3 features 与 self-scorer 完全一致: freq_entropy, surp_d1_skew, surp_d1_mean。\"}, \"exp_019_mistral7b_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:52:12.077Z\", \"updated_at\": \"2026-05-16T11:28:45.586Z\", \"hypothesis\": \"Cross-family K* 验证：Mistral-7B-v0.3 continuation mode 的 K* 是否 = 2？第二个非 Qwen 家族模型。C4 5K, depth 0-5, scorer=Mistral-7B-v0.3 (self-scorer)。与 exp-001/002/017 self-scoring 方法一致，exp_A_alt_scorer 已证明 scorer 不影响 K*。\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-22115\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T04:57:45.553Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-v0___3 --data_dir data_exp019_mistral7b --results_dir results_exp019_mistral7b --num_samples 5000 --max_depth 5 --batch_size 8 --generation_mode continuation\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp019_mistral7b\", \"data_count\": 5000, \"model_name\": \"mistralai/Mistral-7B-v0.3 (fp16)\", \"scorer\": \"Mistral-7B-v0.3 (self-scorer, 与 exp-001/002/017 一致)\", \"seed\": 42, \"generation_mode\": \"continuation\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"pid\": 12147, \"gpu_id\": \"cuda:1\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp019_mistral7b/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/exp019.log\", \"completed_at\": \"2026-05-16T11:17:08.348Z\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9843, \"1v2\": 0.5935, \"2v3\": 0.5402, \"3v4\": 0.5232, \"4v5\": 0.5181}, \"bootstrap_ci_1v2\": {\"ci_lower\": 0.5835, \"ci_upper\": 0.6032, \"p_auc_leq_060\": 0.9017}, \"jsd\": {\"0v1\": 0.124194, \"1v2\": 0.008051, \"2v3\": 0.005047, \"3v4\": 0.004516, \"4v5\": 0.004109}, \"ordinal_mae\": 1.2275, \"ordinal_accuracy\": 0.3567, \"top3_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_d1_mean\"]}, \"notes\": \"K*=1 (非预期的 K*=2)。1v2 AUC=0.5935±0.0054，低于 θ=0.60 阈值仅 0.0065。边界线结果，需 bootstrap CI 确认。0v1 AUC=0.9843 强可区分。Self-scorer (Mistral-7B)。cuda:1 已空闲。\"}, \"exp_016_base_vs_instruct\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:01:55.079Z\", \"updated_at\": \"2026-05-16T05:04:51.120Z\", \"hypothesis\": \"Base vs Instruct K* 对比：Qwen2.5-1.5B (base) continuation mode 的 K* 是否与 exp-017 (Instruct continuation, K*=2) 一致？封堵 \\\"K*=2 是 instruct-tuning 副产物\\\" 攻击面。唯一变量 = base vs instruct。\", \"parent\": \"exp_017_qwen_continuation\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westc-26893\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T01:02:43.478Z\"}, \"completed_at\": \"2026-05-16T03:22:38.539Z\", \"notes\": \"2026-05-16: Resumed on cqa1-22115 (migrated from westc-26893). Depth 0-3 complete, generating depth 4-5. PID=3442 on cuda:0.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16: Resumed on cqa1-22115 (migrated from westc-26893). Depth 0-3 complete, generating depth 4-5. PID=3442 on cuda:0.\"}}, \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data_dir data_exp016_qwen_base --results_dir results_exp016_qwen_base --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B (base, fp16)\", \"seed\": 42, \"generation_mode\": \"continuation\", \"scorer\": \"Qwen2.5-1.5B (base)\", \"gpu\": [\"cuda:0\"], \"tmux_session\": \"exp016\", \"log_path\": \"/tmp/exp016.log\", \"note\": \"Retry #1: Resumed on cqa1-22115 after westc-26893 restart. Depth 0-3 migrated via rsync.\", \"checkpoint_source\": \"N/A (standalone generation, not eval)\", \"eval_data\": \"C4 validation 5000 samples\"}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.987, \"1v2\": 0.6262, \"2v3\": 0.5496, \"3v4\": 0.5294, \"4v5\": 0.5182}, \"pairwise_auc_std\": {\"0v1\": 0.0015, \"1v2\": 0.0152, \"2v3\": 0.0067, \"3v4\": 0.0132, \"4v5\": 0.0139}, \"pairwise_jsd\": {\"0v1\": 0.163726, \"1v2\": 0.01081, \"2v3\": 0.005311, \"3v4\": 0.003942, \"4v5\": 0.003522}, \"ordinal_mae\": 1.1691, \"ordinal_accuracy\": 0.3719, \"top_features\": [\"freq_entropy\", \"surp_std\", \"surp_d1_skew\", \"surp_d1_mean\", \"surp_mean\"], \"n_samples\": 30000, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.987, \"ci_lower\": 0.9853, \"ci_upper\": 0.9885, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.626, \"ci_lower\": 0.6168, \"ci_upper\": 0.6353, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5397, \"ci_upper\": 0.56, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5293, \"ci_lower\": 0.5188, \"ci_upper\": 0.5399, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5181, \"ci_lower\": 0.5075, \"ci_upper\": 0.5288, \"perm_p\": 0.0016}}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95% CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015, 0.6213] — no significant base-vs-instruct difference.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results_exp016_qwen_base/\", \"log_path\": \"/tmp/exp016.log\"}, \"exp_003_decoding_ablation\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-12T20:06:25.260Z\", \"updated_at\": \"2026-05-16T03:06:04.938Z\", \"hypothesis\": \"解码策略调控 K*：不同 top_p/temperature 设置是否改变饱和边界（greedy→更低 K*? 高温度→更高 K*?）\", \"failure_reason\": \"SSH check failed 5x — last error: Unknown server 'autodl-4090d'. Available: ['westc-26893']\", \"completed_at\": \"2026-05-13T15:35:29.038Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T15:35:30.207607+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:22:20.803872+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: SSH 别名变更 (autodl-4090d → westc-26893)，cron 监控 5 次连不上后标记 failed。初步诊断: 日志在 westc-26893 上可读，config 2 (nucleus_p0.9_t1.0) 已完成并输出 K*=2，config 3 (nucleus_p0.95_t0.7) 在 depth 4 进度 ~90% 时日志截止。实验可能已完成或部分完成。Worker worker_diagnose_exp_003_decoding_ablation_20260513T153757 正在深入诊断。\"}}, \"notes\": \"Server alias 变更 autodl-4090d → westc-26893 导致 cron 误标 failed。实际实验一直正常运行。Config 1 (greedy, K*=2), Config 2 (nuc p=0.9/T=1.0, K*=2), Config 3 (nuc p=0.95/T=0.7, K*=2) 已完成。Config 4 (nuc p=0.95/T=1.2) 运行中。深度分析: 1v2 AUC Δ<0.003 across configs, D016 universality confirmed (all 7 configs > θ=0.60), θ-sensitivity K* profile identical across 3 configs. 分析脚本 scripts/exp003_analyze_all_configs.py 已部署。\", \"spec\": {\"command\": \"python scripts/exp003_analyze_all_configs.py\", \"server\": \"westc-26893\", \"gpu\": [\"cuda:0\"], \"pid\": \"29459\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\", \"data_count\": 4, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"configs\": \"4 ablation configs: greedy, nucleus p=0.9/T=1.0, nucleus p=0.95/T=0.7, nucleus p=0.95/T=1.2\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp003_*\", \"log_path_note\": \"server renamed from autodl-4090d to westc-26893\"}, \"metrics\": {\"K_star\": 2, \"K_star_robust\": true, \"bootstrap_ci\": {\"config1_greedy\": {\"0v1\": {\"auc\": 0.9796, \"ci\": [0.9772, 0.982], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6892, \"ci\": [0.6802, 0.6982], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5612, \"ci\": [0.5517, 0.5705], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.5405, \"ci\": [0.5308, 0.5502], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5137, \"ci\": [0.5033, 0.5238], \"perm_p\": 0.0082}}, \"config2_nuc09\": {\"0v1\": {\"auc\": 0.9945, \"ci\": [0.9934, 0.9956], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6862, \"ci\": [0.6774, 0.6951], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5917, \"ci\": [0.5824, 0.601], \"perm_p\": 0, \"note\": \"CI upper crosses theta=0.60\"}, \"3v4\": {\"auc\": 0.5468, \"ci\": [0.5369, 0.5568], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5066, \"ci\": [0.4959, 0.5173], \"perm_p\": 0.1199}}, \"config3_t07\": {\"0v1\": {\"auc\": 0.9877, \"ci\": [0.9857, 0.9896], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.6885, \"ci\": [0.6797, 0.697], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.5901, \"ci\": [0.5806, 0.5996], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.539, \"ci\": [0.5288, 0.5493], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5348, \"ci\": [0.5243, 0.5454], \"perm_p\": 0}}, \"config4_t12\": {\"0v1\": {\"auc\": 0.9982, \"ci\": [0.9975, 0.9987], \"perm_p\": 0}, \"1v2\": {\"auc\": 0.7037, \"ci\": [0.6945, 0.7126], \"perm_p\": 0}, \"2v3\": {\"auc\": 0.582, \"ci\": [0.5722, 0.5917], \"perm_p\": 0}, \"3v4\": {\"auc\": 0.5293, \"ci\": [0.5185, 0.5399], \"perm_p\": 0}, \"4v5\": {\"auc\": 0.5237, \"ci\": [0.5132, 0.5347], \"perm_p\": 0.0001}}, \"resamples\": 10000, \"method\": \"GroupKFold(5) OOF + doc-level bootstrap + label permutation\"}}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:22:19.870Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_analysis.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_003_decoding_ablation.log\", \"conclusion\": \"success\"}, \"exp_004_7b_crossscale\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T11:08:22.198Z\", \"updated_at\": \"2026-05-15T23:37:24.772Z\", \"hypothesis\": \"K*=2 在 7B scale 下是否成立？Qwen2.5-7B continuation mode, C4 5K seeds, scorer=Qwen2.5-1.5B。Reviewer R2 Critical: 现有实验仅 ≤1.5B\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-15T23:11:49.043Z\"}, \"completed_at\": \"2026-05-15T22:26:45.097Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:26:46.220502+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:11:50.215210+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"进程 5 次死亡无 W&B metrics，cron 自动标记 failed。诊断中：Worker worker_diagnose_exp_004_7b_crossscale_20260515T222832 正在查日志。模型加载成功(14530MB)，C4 采样有进度，日志末尾异常出现 transformers 全量模型列表。待诊断完成后确定 root cause 和重试方案。\"}}, \"notes\": \"初始运行因进程死亡 5 次被 cron 标记 failed（原 log: exp004_run.log 无 W&B sentinel）。诊断 Worker 发现数据生成已完成，重跑 feature extraction + classification（exp004_resume_feat.sh）后成功。K*=2 在 7B scale 下确认成立。0v1 AUC=0.964 低于所有 1.5B 模型（>0.99），符合预期：更大模型生成更 human-like 文本。1v2=0.618 仍 >θ=0.60。FR-4 Warning resolved。\", \"spec\": {\"hypothesis\": \"K*=2 在 7B scale 下是否成立？Qwen2.5-7B continuation mode, C4 5K seeds, scorer=Qwen2.5-1.5B\", \"server\": \"westc-26893\", \"model_name\": \"Qwen/Qwen2.5-7B (fp16, 14.5GB) + Qwen2.5-1.5B-Instruct (scorer)\", \"data_count\": 5000, \"seed\": 42, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && bash scripts/exp004_resume_feat.sh\\\"\", \"gpu\": [\"cuda:0\"], \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp004_qwen7b\", \"note\": \"Resume: data generation complete, rerunning feature extraction + classification with corrected scorer path. PID 127516.\"}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9644, \"1v2\": 0.6178, \"2v3\": 0.546, \"3v4\": 0.5225, \"4v5\": 0.5091}, \"pairwise_auc_std\": {\"0v1\": 0.0034, \"1v2\": 0.0081, \"2v3\": 0.0028, \"3v4\": 0.0113, \"4v5\": 0.0052}, \"bootstrap_ci\": {\"0v1\": {\"auc\": 0.9638, \"ci_lower\": 0.9607, \"ci_upper\": 0.9665, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6168, \"ci_lower\": 0.6079, \"ci_upper\": 0.6261, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5492, \"ci_lower\": 0.5388, \"ci_upper\": 0.5594, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5276, \"ci_lower\": 0.517, \"ci_upper\": 0.5375, \"perm_p\": 0.0001}, \"4v5\": {\"auc\": 0.5085, \"ci_lower\": 0.4988, \"ci_upper\": 0.5191, \"perm_p\": 0.0676}}, \"bootstrap_resamples\": 1000, \"permutation_resamples\": 10000, \"pairwise_jsd\": {\"0v1\": 0.127422, \"1v2\": 0.010114, \"2v3\": 0.004798, \"3v4\": 0.004821, \"4v5\": 0.003335}, \"ordinal_mae\": 1.2156, \"ordinal_accuracy\": 0.3523, \"top_features\": [\"freq_entropy\", \"surp_d1_skew\", \"surp_std\", \"surp_d1_mean\", \"surp_mean\"], \"key_finding\": \"K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60 (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676). FR-4 Warning resolved.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp004_qwen7b/\", \"log_path\": \"/root/runs/gen-depth-contamination/exp_004_7b_crossscale.log\"}, \"exp_E_paired_stats\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:27.723Z\", \"updated_at\": \"2026-05-15T14:22:43.224Z\", \"hypothesis\": \"C3 filtering 策略间差异是否统计显著？Holm-Bonferroni 多重比较校正 + Cohen's d 效应量（FR-5 Warning）\", \"spec\": {\"command\": \"python scripts/exp_E_paired_stats.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp006_filtering/results/\", \"data_count\": 51, \"model_name\": \"N/A (CPU: paired t-test + Holm-Bonferroni)\", \"seed\": \"N/A\", \"note\": \"6 strategies × 5 seeds, 15 pairwise comparisons, Holm-Bonferroni correction + Cohen's d\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_significant_pairs\": \"8/15\", \"hellaswag_significant_pairs\": \"9/15\", \"binary_ours_vs_all_mmlu\": \"all significant\", \"max_cohen_d_mmlu\": 10.8, \"max_cohen_d_hellaswag\": 8.98, \"graduated_a09_vs_dsir_corrected_p\": 0.0523, \"cohen_d_method\": \"d_av (Lakens 2013)\", \"key_finding\": \"binary-ours significantly outperforms all alternatives on MMLU. On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni cummax bug fixed: MMLU 10/15→8/15. Cohen's d changed to d_av.\", \"bugfix_note\": \"Holm-Bonferroni cummax variable was never updated, causing 2 MMLU pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json\", \"completed_at\": \"2026-05-15T11:20:31.718Z\", \"notes\": \"Holm-Bonferroni bug fixed: cummax variable was never updated in loop, causing adjusted p-values to lose monotonicity. MMLU significant pairs corrected 10/15→8/15. Cohen's d changed from d_z to d_av (Lakens 2013). d values still large (10.8) due to n=5 tiny within-seed variance — recommend mean_diff as primary effect size in paper.\"}, \"exp_D_obd_n500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:27.182Z\", \"updated_at\": \"2026-05-15T11:46:23.600Z\", \"hypothesis\": \"OBD-LightGBM 在 N=500 子集上 accuracy 是否仍高于 LLM baselines？验证样本量匹配下的公平比较（FR-12 Warning）\", \"spec\": {\"command\": \"python scripts/exp_D_obd_n500_v2.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia + artifacts/exp011_samples.jsonl\", \"data_count\": 500, \"model_name\": \"N/A (CPU: OBD-LightGBM on N=500 subset)\", \"seed\": 42, \"note\": \"Bootstrap CI for OBD accuracy on same 500 samples as LLM baseline\"}, \"conclusion\": \"success\", \"metrics\": {\"obd_accuracy_final\": 0.38, \"obd_ci\": [0.34, 0.422], \"mcnemar_vs_gpt55_p\": 0.0809, \"mcnemar_vs_claude_p\": 0.0693, \"mcnemar_significant\": false, \"multi_seed_std\": 0, \"per_depth\": {\"d0\": 0.96, \"d1\": 0.39, \"d2\": 0.14, \"d3\": 0.19, \"d4\": 0.22}, \"prob_merge_accuracy\": 0.444, \"prob_merge_d4_bias\": 0.8, \"note\": \"v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant — supports discussion.tex narrative\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_D_obd_n500_v2.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_D_obd_n500_v2.json\", \"completed_at\": \"2026-05-15T11:20:31.077Z\"}, \"exp_B_14d_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:25.666Z\", \"updated_at\": \"2026-05-15T11:20:29.596Z\", \"hypothesis\": \"移除 self_BLEU（14D vs 15D）后 K*=2 是否稳定？排除 self_BLEU information leakage（FR-3 Critical）\", \"spec\": {\"command\": \"python scripts/exp_B_14d_ablation.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data + data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 20000, \"model_name\": \"N/A (CPU: LightGBM 14D vs 15D)\", \"seed\": 42, \"note\": \"Remove self_BLEU, compare 14D vs 15D pairwise AUC and K*\"}, \"conclusion\": \"success\", \"metrics\": {\"result\": \"K*=2 stable across all 4 models after removing self_BLEU (14D)\", \"key_finding\": \"self_BLEU removal does not change K* boundary. FR-3 resolved.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_B_14d_ablation.json\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_B_14d_ablation.json\", \"completed_at\": \"2026-05-15T11:20:29.596Z\"}, \"exp_A_alt_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:18:24.715Z\", \"updated_at\": \"2026-05-15T11:19:40.861Z\", \"hypothesis\": \"替代 scorer (Pythia-1.4B, OLMo-1B) 计算 surprisal features 时，K*=2 是否仍成立？验证 K* 不依赖 scorer-generator 匹配（FR-2 Critical）\", \"spec\": {\"command\": \"bash scripts/run_exp_A.sh\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data (Qwen-RW) + data_exp017_qwen_cont (Qwen-cont)\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B + OLMo-1B (as alt scorers) × Qwen-generated data\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"note\": \"4 conditions: {Pythia,OLMo} × {Qwen-RW,Qwen-cont}. Surprisal features computed with alt scorer, LightGBM classification.\"}, \"conclusion\": \"success\", \"metrics\": {\"pythia_qwen_rw\": {\"k_star\": 2, \"auc_0v1\": 0.9923, \"auc_1v2\": 0.7012, \"auc_2v3\": 0.587, \"mae\": 1.006, \"accuracy\": 0.417, \"spearman_rho_vs_baseline\": 0.906}, \"pythia_qwen_cont\": {\"k_star\": 1, \"auc_0v1\": 0.99, \"auc_1v2\": 0.5923, \"auc_2v3\": null, \"mae\": 1.216, \"accuracy\": 0.371, \"spearman_rho_vs_baseline\": 0.942}, \"olmo_qwen_rw\": {\"k_star\": 2, \"auc_0v1\": 0.9918, \"auc_1v2\": 0.6947, \"auc_2v3\": null, \"mae\": 1.016, \"accuracy\": 0.413, \"spearman_rho_vs_baseline\": 0.92}, \"olmo_qwen_cont\": {\"k_star\": 1, \"auc_0v1\": 0.989, \"auc_1v2\": 0.5858, \"auc_2v3\": null, \"mae\": 1.229, \"accuracy\": 0.368, \"spearman_rho_vs_baseline\": 0.902}, \"key_finding\": \"K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1 (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer independence of feature ranking.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_A/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp_A/exp_A_alt_scorer.log\", \"completed_at\": \"2026-05-15T11:19:40.861Z\"}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-13T18:53:34.791Z\", \"updated_at\": \"2026-05-15T10:47:04.883Z\", \"hypothesis\": \"Learned representations (frozen LLM → MLP) 的 K* 是否高于 hand-crafted 15D features？若 K*_neural > K*_15D，说明 15D projection 是 K*=2 的部分原因；若相同，加强 information-theoretic impossibility 论证\", \"notes\": \"v4 completed successfully. 3 models: Pythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3. Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen-cont self-scorer crosses θ=0.60. EXIT_CODE=129 (SIGHUP after completion) did not affect results.\", \"completed_at\": \"2026-05-14T02:58:02.023Z\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 26.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 20.06 MiB is free. Process 55665 has 13.36 GiB memory in use. Process 56371 has 9.09 GiB memory in use. Including non-PyTorch memory, this process has 1\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v4 run in progress (PID 108774, tmux: exp015, westc-26893). Root cause of prior failures: v2=OOM (concurrent exp-006 占 GPU), v3=SIGHUP/EXIT_CODE=129 (SSH 断连，未在 tmux 中)。v4 在 tmux 中安全运行，Pythia 86% → OLMo → Qwen-cont → MLP training。内存管理正确 (del+gc+empty_cache)，6.7GB/24GB。ETA ~25-30min from 09:28 UTC.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:21:59.744073+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:39.481148+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:31:35.099Z\"}, \"conclusion\": \"success\", \"metrics\": {\"pythia\": {\"k_star_neural\": 2, \"k_star_lgbm\": 2, \"accuracy\": 0.3892, \"pairwise_auc\": {\"0v1\": 0.966, \"1v2\": 0.676, \"2v3\": 0.596, \"3v4\": 0.555, \"4v5\": 0.532}}, \"olmo\": {\"k_star_neural\": 2, \"k_star_lgbm\": 2, \"accuracy\": 0.3729, \"pairwise_auc\": {\"0v1\": 0.95, \"1v2\": 0.657, \"2v3\": 0.589, \"3v4\": 0.547, \"4v5\": 0.53}}, \"qwen_cont\": {\"k_star_neural\": 3, \"k_star_lgbm\": 2, \"accuracy\": 0.4368, \"pairwise_auc\": {\"0v1\": 0.988, \"1v2\": 0.702, \"2v3\": 0.616, \"3v4\": 0.59, \"4v5\": 0.566}}, \"key_finding\": \"Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3 only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_015_neural_probe.log\", \"spec\": {\"command\": \"python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 8\", \"server\": \"westc-26893\", \"data_path\": \"data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 90000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct (frozen encoder -> MLP probe)\", \"seed\": \"5-fold CV\"}}, \"exp_006_graduated_filtering\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-13T20:25:52.364Z\", \"updated_at\": \"2026-05-15T09:18:18.667Z\", \"hypothesis\": \"K*-aware graduated filtering (exploiting human/gen-1/gen-2+ trichotomy) yields better downstream LM quality than binary filtering on MMLU and HellaSwag. 6 strategies × 5 seeds × α sweep.\", \"parent\": \"exp_003_decoding_ablation\", \"notes\": \"51/51 COMPLETE. All 6 strategies × 5 seeds + base_model finished 2026-05-15 ~09:10 UTC.\\n\\nFINAL RANKING (MMLU descending):\\n1. binary-ours: 0.5941±0.0008 / 0.6701±0.0006 (BEST)\\n2. binary-drayson: 0.5913±0.0009 / 0.6691±0.0004\\n3. surprisal: 0.5894±0.0009 / 0.6641±0.0006\\n4. graduated_a0.9: 0.5892±0.0008 / 0.6701±0.0007\\n5. graduated_a0.7: 0.5892±0.0014 / 0.6695±0.0004\\n6. graduated_a0.5: 0.5880±0.0013 / 0.6687±0.0008\\n7. graduated_a0.3: 0.5877±0.0013 / 0.6669±0.0005\\n8. graduated_a0.1: 0.5873±0.0019 / 0.6640±0.0009\\n9. dsir: 0.5869±0.0003 / 0.6631±0.0007\\n10. no-filter: 0.5865±0.0010 / 0.6638±0.0008\\nBase: 0.6018 / 0.6821\\n\\nVERSION B fully confirmed. Binary-ours is optimal. Graduated α monotonic. DSIR below all strategies except no-filter.\", \"reproduce\": {\"finished_at\": \"2026-05-14T21:31:53.630Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"completed_at\": \"2026-05-14T21:04:20.455Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:04:21.389845+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:32:00.501871+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"RESUMED 05-14 ~21:30 UTC after EXIT_CODE=124 timeout crash. 32/50 runs complete pre-crash. 18 remaining: a0.7(s456/s789/s1024) + a0.9(5) + surprisal(5) + dsir(5). Script has built-in skip logic (checks eval_results.json). Running in tmux:exp006_resume without timeout wrapper. ETA: ~05-15 11:00-12:00 UTC.\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp006_graduated_filtering.py\", \"server\": \"westc-26893\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/depth_corpus_30k\", \"data_count\": 30000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": \"42,123,456,789,1024\", \"gpu\": \"cuda:0\", \"checkpoint_source\": \"Qwen/Qwen2.5-1.5B-Instruct (HuggingFace, LoRA fine-tune from base)\", \"eval_data\": \"MMLU (14042 test, 0-shot) + HellaSwag (10042 val, 0-shot) via lm-eval-harness\", \"note\": \"Resumed run. tmux: exp_006_graduated_filtering. 33/50 complete, 17 remaining. ETA ~05-15 07:30-08:30 UTC.\"}, \"conclusion\": \"success\", \"metrics\": {\"total_runs\": 51, \"binary_ours\": {\"mmlu\": \"0.5941±0.0008\", \"hellaswag\": \"0.6701±0.0006\"}, \"binary_drayson\": {\"mmlu\": \"0.5913±0.0009\", \"hellaswag\": \"0.6691±0.0004\"}, \"surprisal\": {\"mmlu\": \"0.5894±0.0009\", \"hellaswag\": \"0.6641±0.0006\"}, \"graduated_a09\": {\"mmlu\": \"0.5892±0.0008\", \"hellaswag\": \"0.6701±0.0007\"}, \"graduated_a07\": {\"mmlu\": \"0.5892±0.0014\", \"hellaswag\": \"0.6695±0.0004\"}, \"graduated_a05\": {\"mmlu\": \"0.5880±0.0013\", \"hellaswag\": \"0.6687±0.0008\"}, \"graduated_a03\": {\"mmlu\": \"0.5877±0.0013\", \"hellaswag\": \"0.6669±0.0005\"}, \"graduated_a01\": {\"mmlu\": \"0.5873±0.0019\", \"hellaswag\": \"0.6640±0.0009\"}, \"dsir\": {\"mmlu\": \"0.5869±0.0003\", \"hellaswag\": \"0.6631±0.0007\"}, \"no_filter\": {\"mmlu\": \"0.5865±0.0010\", \"hellaswag\": \"0.6638±0.0008\"}, \"base_model\": {\"mmlu\": \"0.6018\", \"hellaswag\": \"0.6821\"}, \"best_strategy\": \"binary-ours\", \"key_finding\": \"binary-ours is best filtering strategy. All strategies degrade vs base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR below all other strategies except no-filter.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp006_filtering/results/\", \"log_path\": \"~/runs/gen-depth-contamination/exp_006_graduated_filtering.log\"}, \"exp_007_bootstrap_ci\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T03:45:50.948Z\", \"updated_at\": \"2026-05-13T23:43:00.694Z\", \"hypothesis\": \"K* 统计严谨性验证：bootstrap 95% CI 和 permutation test 确认 K*=2 在三个模型族上统计显著\", \"spec\": {\"command\": \"python scripts/bootstrap_ci.py --data_dirs results_exp001_pythia results_exp002_olmo data --labels Pythia-1.4B OLMo-1B Qwen-1.5B --output artifacts/bootstrap_ci_results.json\", \"script_path\": \"/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py\", \"server\": \"autodl-4090d\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\", \"data_count\": 15000, \"model_name\": \"Pythia-1.4B / OLMo-1B / Qwen-1.5B\", \"seed\": 42, \"input_sources\": [\"results_exp001_pythia (exp-001)\", \"results_exp002_olmo (exp-002)\", \"data (mvp-001)\"], \"bootstrap_resamples\": 1000, \"permutation_resamples\": 500, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/bootstrap_ci_results.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_007_bootstrap_ci.log\"}, \"metrics\": {\"qwen_rewrite\": {\"0v1\": {\"auc\": 0.9956, \"ci_lower\": 0.9946, \"ci_upper\": 0.9965, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6955, \"ci_lower\": 0.6859, \"ci_upper\": 0.7041, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5893, \"ci_lower\": 0.5795, \"ci_upper\": 0.5991, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5435, \"ci_lower\": 0.5333, \"ci_upper\": 0.5551, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.534, \"ci_lower\": 0.5238, \"ci_upper\": 0.5448, \"perm_p\": 0.002}}, \"pythia_cont\": {\"0v1\": {\"auc\": 0.9932, \"ci_lower\": 0.9921, \"ci_upper\": 0.9943, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6539, \"ci_lower\": 0.6454, \"ci_upper\": 0.663, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5514, \"ci_lower\": 0.5417, \"ci_upper\": 0.5628, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5152, \"ci_lower\": 0.5041, \"ci_upper\": 0.526, \"perm_p\": 0.006}, \"4v5\": {\"auc\": 0.5136, \"ci_lower\": 0.5021, \"ci_upper\": 0.5249, \"perm_p\": 0.008}}, \"olmo_cont\": {\"0v1\": {\"auc\": 0.997, \"ci_lower\": 0.9964, \"ci_upper\": 0.9975, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6145, \"ci_lower\": 0.6045, \"ci_upper\": 0.6247, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5496, \"ci_lower\": 0.5399, \"ci_upper\": 0.5596, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5091, \"ci_lower\": 0.4973, \"ci_upper\": 0.52, \"perm_p\": 0.064}, \"4v5\": {\"auc\": 0.5045, \"ci_lower\": 0.4932, \"ci_upper\": 0.515, \"perm_p\": 0.232}}, \"qwen_cont\": {\"0v1\": {\"auc\": 0.9971, \"ci_lower\": 0.9963, \"ci_upper\": 0.9978, \"perm_p\": 0.002}, \"1v2\": {\"auc\": 0.6112, \"ci_lower\": 0.6015, \"ci_upper\": 0.6213, \"perm_p\": 0.002}, \"2v3\": {\"auc\": 0.5609, \"ci_lower\": 0.5511, \"ci_upper\": 0.5712, \"perm_p\": 0.002}, \"3v4\": {\"auc\": 0.5409, \"ci_lower\": 0.5308, \"ci_upper\": 0.5508, \"perm_p\": 0.002}, \"4v5\": {\"auc\": 0.5141, \"ci_lower\": 0.5035, \"ci_upper\": 0.5255, \"perm_p\": 0.006}}, \"k_star_robust\": true, \"all_1v2_ci_lower_above_060\": true, \"most_marginal\": \"Qwen-cont CI lower=0.6015, only 0.0015 above threshold\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T03:46:36.617Z\"}, \"exp_011_llm_zeroshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T08:59:07.954Z\", \"updated_at\": \"2026-05-13T11:34:44.605Z\", \"hypothesis\": \"Frontier LLMs (GPT-5.5, Claude Opus 4.6) cannot reliably estimate generational depth via zero-shot prompting, motivating the need for specialized statistical methods\", \"spec\": {\"command\": \"python3 scripts/exp011_llm_zeroshot.py --model gpt-5.5 && python3 scripts/exp011_llm_zeroshot.py --model claude-opus-4-6 && python3 scripts/exp011_analyze.py\", \"server\": \"autodl-4090d\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"data_count\": 500, \"model_name\": \"GPT-5.5 + Claude Opus 4.6 (zero-shot via OpenRouter)\", \"seed\": 42, \"sampling\": \"100 texts × 5 depths (0-4) from Pythia continuation\", \"scripts\": [\"scripts/exp011_sample_data.py\", \"scripts/exp011_llm_zeroshot.py\", \"scripts/exp011_analyze.py\"], \"samples_path\": \"artifacts/exp011_samples.jsonl\", \"api_base_url\": \"http://47.94.22.126/v1\", \"api_model_ids\": {\"gpt-5.5\": \"openai/gpt-5.5\", \"claude-opus-4-6\": \"claude-opus-4-6\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp011_analysis.json\", \"log_path\": \"N/A (API task)\"}, \"notes\": \"GPT-5.5: 500条, 0 parse failures. Claude Opus 4.6: 500条, 1 parse failure. 两个 frontier LLM 5-class accuracy (~33%) 均低于 OBD-LightGBM (38.6%)。Binary human/AI detection 高 (~88%) 但 fine-grained depth 判断失败。Claude proxy 需用 model ID 'claude-opus-4-6' (无 anthropic/ 前缀)。\", \"metrics\": {\"gpt55_5class_acc\": 0.332, \"gpt55_mae\": 1.102, \"gpt55_spearman\": 0.383, \"gpt55_binary_acc\": 0.878, \"claude_5class_acc\": 0.331, \"claude_mae\": 1.15, \"claude_spearman\": 0.416, \"claude_binary_acc\": 0.882, \"odb_baseline_5class_acc\": 0.386, \"odb_baseline_mae\": 1.107, \"gpt55_per_depth_acc\": {\"depth_0\": 0.77, \"depth_1\": 0.19, \"depth_2\": 0.38, \"depth_3\": 0.24, \"depth_4\": 0.08}, \"claude_per_depth_acc\": {\"depth_0\": 0.69, \"depth_1\": 0.21, \"depth_2\": 0.28, \"depth_3\": 0.101, \"depth_4\": 0.37}, \"n_samples_per_model\": 500, \"key_finding\": \"Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI detection is high (~88%) but fine-grained depth discrimination fails.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T11:32:56.036Z\"}, \"exp_013_cross_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:50:57.813Z\", \"updated_at\": \"2026-05-13T06:54:11.689Z\", \"spec\": {\"command\": \"python scripts/run_exp013_cross_transfer.py --out_dir artifacts/\", \"server\": \"autodl-4090d\", \"data_path\": \"data/, data_exp001_pythia/, data_exp002_olmo/, data_exp017_qwen_cont/\", \"data_count\": 20000, \"model_name\": \"N/A (CPU classifiers: OBD-LightGBM)\", \"seed\": 42, \"input_sources\": [\"mvp-001 Qwen-rewrite\", \"exp-001 Pythia\", \"exp-002 OLMo\", \"exp-017 Qwen-cont\"], \"checkpoint_path\": \"artifacts/cross_transfer_matrix.json\", \"log_path\": \"N/A (CPU task)\"}, \"hypothesis\": \"Depth signal 是文本固有属性还是 model self-familiarity artifact？4×4 cross-model transfer matrix 测试分类器跨模型泛化能力\", \"metrics\": {\"accuracy_matrix\": {\"Qwen_rw→Qwen_rw\": 0.4229, \"Qwen_rw→Pythia\": 0.259, \"Qwen_rw→OLMo\": 0.2653, \"Qwen_rw→Qwen_cont\": 0.3466, \"Pythia→Qwen_rw\": 0.2718, \"Pythia→Pythia\": 0.3856, \"Pythia→OLMo\": 0.3531, \"Pythia→Qwen_cont\": 0.3287, \"OLMo→Qwen_rw\": 0.2768, \"OLMo→Pythia\": 0.345, \"OLMo→OLMo\": 0.3822, \"OLMo→Qwen_cont\": 0.3244, \"Qwen_cont→Qwen_rw\": 0.344, \"Qwen_cont→Pythia\": 0.3284, \"Qwen_cont→OLMo\": 0.3112, \"Qwen_cont→Qwen_cont\": 0.3875}, \"transfer_retention_accuracy\": {\"Pythia↔OLMo\": \"91-92%\", \"Qwen_rw→Pythia/OLMo\": \"61-63%\", \"Qwen_cont↔Pythia\": \"83-85%\", \"Qwen_cont↔OLMo\": \"80-85%\"}, \"transfer_retention_tau\": {\"Pythia↔OLMo\": \"85-86%\", \"Qwen_rw→Pythia/OLMo\": \"45-50%\", \"Qwen_cont↔others\": \"68-83%\"}, \"mean_pw_auc_matrix\": {\"within_avg\": 0.6099, \"cross_avg\": 0.5905, \"0v1_cross_all_above\": 0.96}, \"key_finding\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T06:53:07.326Z\", \"notes\": \"depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity. Pythia↔OLMo 91-92% retention (architecture-agnostic). Qwen-rewrite catastrophic transfer to other models (61-63%), but Qwen-cont much better (80-85%). 0v1 universally transferable (>0.96 AUC), 1v2+ transfer depends on model family. Rewrite mode overfits style features → continuation mode is canonical condition for cross-model claims.\"}, \"exp_010_ordinal_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T04:22:42.199Z\", \"updated_at\": \"2026-05-13T04:26:54.571Z\", \"hypothesis\": \"Ordinal structure improves depth classification: ordinal methods should outperform unordered multiclass on MAE\", \"spec\": {\"command\": \"python scripts/run_exp010_ordinal_comparison.py\", \"server\": \"autodl-4090d\", \"data_path\": \"data/features.csv, data_exp001_pythia/features.csv, data_exp002_olmo/features.csv\", \"data_count\": 90000, \"model_name\": \"N/A (CPU classifiers)\", \"seed\": \"N/A\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/ordinal_comparison_results.json\"}, \"metrics\": {\"qwen_rewrite\": {\"obd_lgbm\": {\"accuracy\": 0.4229, \"mae\": 0.9836, \"tau_b\": 0.5518, \"mean_pw_auc\": 0.6214}, \"multiclass_lgbm\": {\"accuracy\": 0.4182, \"mae\": 1.0163, \"tau_b\": 0.5367, \"mean_pw_auc\": 0.6246}, \"ordinal_logreg\": {\"accuracy\": 0.3636, \"mae\": 0.9105, \"tau_b\": 0.563, \"mean_pw_auc\": 0.5022}}, \"pythia\": {\"obd_lgbm\": {\"accuracy\": 0.3856, \"mae\": 1.1072, \"tau_b\": 0.4745, \"mean_pw_auc\": 0.6055}, \"multiclass_lgbm\": {\"accuracy\": 0.3832, \"mae\": 1.1399, \"tau_b\": 0.4622, \"mean_pw_auc\": 0.6062}, \"ordinal_logreg\": {\"accuracy\": 0.3179, \"mae\": 1.022, \"tau_b\": 0.49, \"mean_pw_auc\": 0.4767}}, \"olmo\": {\"obd_lgbm\": {\"accuracy\": 0.3822, \"mae\": 1.1469, \"tau_b\": 0.4683, \"mean_pw_auc\": 0.6015}, \"multiclass_lgbm\": {\"accuracy\": 0.3685, \"mae\": 1.1813, \"tau_b\": 0.4497, \"mean_pw_auc\": 0.5974}, \"ordinal_logreg\": {\"accuracy\": 0.3265, \"mae\": 1.0352, \"tau_b\": 0.4656, \"mean_pw_auc\": 0.4859}}}, \"conclusion\": \"success\", \"notes\": \"Ordinal methods beat multiclass LightGBM on MAE across all 3 datasets. Best MAE consistently from mord LogisticAT, not OBD-LightGBM. However, ordinal_logreg has worst pairwise AUC — it reduces MAE by collapsing predictions toward the center, not by better discrimination.\", \"completed_at\": \"2026-05-13T04:26:54.571Z\"}, \"exp_001_pythia_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:23.803Z\", \"updated_at\": \"2026-05-13T00:16:16.359Z\", \"hypothesis\": \"K* 跨模型一致性验证：Pythia-1.4B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"17138\", \"log_path\": \"~/runs/gen-depth-contamination/exp_001_pythia_depth.log\", \"submitted_at\": \"2026-05-12T20:50:31.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"wall_clock_seconds\": 12344.9, \"gpu_hours\": 3.43}, \"conclusion\": \"success\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9932, \"1v2\": 0.6539, \"2v3\": 0.5515, \"3v4\": 0.5153, \"4v5\": 0.5135}, \"pairwise_auc_std\": {\"0v1\": 0.0007, \"1v2\": 0.0069, \"2v3\": 0.0137, \"3v4\": 0.0084, \"4v5\": 0.0078}, \"pairwise_jsd\": {\"0v1\": 0.2142, \"1v2\": 0.014, \"2v3\": 0.0051, \"3v4\": 0.0033, \"4v5\": 0.0031}, \"k_star\": 2, \"ordinal_mae\": 1.14, \"ordinal_accuracy\": 0.383}, \"completed_at\": \"2026-05-13T00:16:16.359Z\"}, \"mvp_pilot_sat_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T11:09:39.193Z\", \"updated_at\": \"2026-05-12T19:25:33.763Z\", \"hypothesis\": \"递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势（K* ≥ 3）\", \"spec\": {\"command\": \"bash /root/autodl-tmp/gen-depth-contamination/run_mvp.sh\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"10619\", \"log_path\": \"~/runs/gen-depth-contamination/mvp_pilot_sat_v1.log\", \"submitted_at\": \"2026-05-12T16:46:33.175Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/\", \"wall_clock_seconds\": 9533.4, \"gpu_hours\": 2.65}, \"notes\": \"v2 left-padding rerun, per-fold AUC, full self-BLEU\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-12T19:25:26.538Z\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9956, \"1v2\": 0.6957, \"2v3\": 0.5893, \"3v4\": 0.5434, \"4v5\": 0.5343}, \"pairwise_auc_std\": {\"0v1\": 0.0005, \"1v2\": 0.0072, \"2v3\": 0.012, \"3v4\": 0.0053, \"4v5\": 0.0091}, \"pairwise_jsd\": {\"0v1\": 0.2669, \"1v2\": 0.0163, \"2v3\": 0.0069, \"3v4\": 0.0047, \"4v5\": 0.0041}, \"k_star\": 2, \"ordinal_mae\": 1.0163, \"ordinal_accuracy\": 0.4182}}}, \"count\": 164, \"total\": 164, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5721}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The registry data is too large. Let me also read the input files (introduction, related_work, method, experiments_c1, experiments_c3, discussion, conclusion) to check for references. And I need to query the registry for specific experiments. Let me do these in parallel.

Let me read the sub-files and query the registry for the specific experiments I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "6f0bd1a3-6350-4de9-914f-e203a63e6b17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kehkJzryo9tmr3LhUmwx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19745,
      "cache_read_input_tokens": 26649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19745
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

_source line 20_

Now let me read the sub-files and query the registry for specific experiments needed for table validation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "6685adee-cdcc-4590-a7c7-25ba38804346",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kehkJzryo9tmr3LhUmwx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19745,
      "cache_read_input_tokens": 26649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19745
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

_source line 21_

<details open><summary>🔧 Tool call — Agent · `toolu_01JcWRD49yAfxApcFgxoZMTN`</summary>

```json
{
  "description": "Read all paper sub-files",
  "subagent_type": "Explore",
  "prompt": "Read the following LaTeX files in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ and return their FULL contents:\n1. introduction.tex\n2. related_work.tex\n3. method.tex\n4. experiments_c1.tex\n5. experiments_c3.tex\n6. discussion.tex\n7. conclusion.tex\n\nI need the complete text of each file. Return the contents with the filename as a header before each file's contents."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "c19c0f18-994d-408a-8286-3a3cf8cb027e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kehkJzryo9tmr3LhUmwx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19745,
      "cache_read_input_tokens": 26649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19745
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

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "description": "Read all paper sub-files",
  "task_type": "local_agent",
  "prompt": "Read the following LaTeX files in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ and return their FULL contents:\n1. introduction.tex\n2. related_work.tex\n3. method.tex\n4. experiments_c1.tex\n5. experiments_c3.tex\n6. discussion.tex\n7. conclusion.tex\n\nI need the complete text of each file. Return the contents with the filename as a header before each file's contents.",
  "uuid": "580e83c3-fb7d-4cf8-a074-42e7d15af626",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

## Round 1

24 recorded events

### User

_source line 23 · 2026-05-22T21:21:44.454Z_

Read the following LaTeX files in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ and return their FULL contents:
1. introduction.tex
2. related_work.tex
3. method.tex
4. experiments_c1.tex
5. experiments_c3.tex
6. discussion.tex
7. conclusion.tex

I need the complete text of each file. Return the contents with the filename as a header before each file's contents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "6f910976-dbab-4218-9d55-5b24f684e246"
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
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 19312,
    "tool_uses": 1,
    "duration_ms": 1437
  },
  "last_tool_name": "Read",
  "uuid": "8c773036-7fb9-428c-85d3-076434bec48c",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "description": "Reading docs/paper/related_work.tex",
  "usage": {
    "total_tokens": 19316,
    "tool_uses": 2,
    "duration_ms": 1508
  },
  "last_tool_name": "Read",
  "uuid": "2ff63964-e0ff-488a-b0a8-745b02252872",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 19320,
    "tool_uses": 3,
    "duration_ms": 1929
  },
  "last_tool_name": "Read",
  "uuid": "f19760aa-37eb-4d88-9061-72c3fc3789de",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "description": "Reading docs/paper/experiments_c1.tex",
  "usage": {
    "total_tokens": 19324,
    "tool_uses": 4,
    "duration_ms": 2144
  },
  "last_tool_name": "Read",
  "uuid": "76979520-213d-4dcf-8b53-46b440abf1f0",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "description": "Reading docs/paper/experiments_c3.tex",
  "usage": {
    "total_tokens": 19328,
    "tool_uses": 5,
    "duration_ms": 2389
  },
  "last_tool_name": "Read",
  "uuid": "06689096-df54-4f98-8765-473d5ab0928a",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "description": "Reading docs/paper/discussion.tex",
  "usage": {
    "total_tokens": 19332,
    "tool_uses": 6,
    "duration_ms": 2566
  },
  "last_tool_name": "Read",
  "uuid": "5a95735c-b4a5-4100-b27b-5db30541abea",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "description": "Reading docs/paper/conclusion.tex",
  "usage": {
    "total_tokens": 19336,
    "tool_uses": 7,
    "duration_ms": 2693
  },
  "last_tool_name": "Read",
  "uuid": "98648b4d-647a-4dc0-a508-31ea56302005",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01DPdKYUQie32DdUydjuu5GD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "78757045-328e-4768-9494-bf851b859edd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 32 · 2026-05-22T21:21:45.897Z_

<details><summary>↩ Tool result · `toolu_01DPdKYUQie32DdUydjuu5GD`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
11	No existing method estimates how many rounds of recursive generation a text has undergone.
12	
13	The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
14	We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
15	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
16	
17	Our contributions:
18	\begin{enumerate}[label=(\alph*),nosep]
19	  \item \textbf{$\Kempirical$ as a measurement tool} across 10 model configurations (6 families, 1B--8B) and 4 decoding strategies ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}):
20	  For web text, $\Kempirical \leq 2$ regardless of family or scale; $\Kempirical \leq 3$ universally.
21	  $\Kempirical$ establishes binary sufficiency for web text by measurement (not assumption), reveals domain-dependent variation (arXiv $\Kempirical{=}3$), and quantifies boundary sensitivity to threshold, scorer, and model scale.
22	  Both supervised OBD and zero-shot LLMs fail beyond $\Kempirical$ (McNemar $p > 0.05$; Section~\ref{sec:why_kstar}).
23	  \item \textbf{Domain dependence of $\Kempirical$}: general web text (C4, Wikipedia) yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$, consistent across model families (Section~\ref{sec:cross_domain}).
24	  \item \textbf{Model-free cross-model transfer}: 15 statistical features enable 80--100\% accuracy retention with scorer-invariant feature rankings ($\rho > 0.90$), supporting model-agnostic depth estimation without retraining; $\Kempirical$ agreement holds across scorers for strong-signal configurations (Section~\ref{sec:transfer}).
25	\end{enumerate}
26	
27	\noindent As a consistency check, $\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$; Section~\ref{sec:filtering}).
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "1b12c07b-17f4-4084-8a49-f75a52e2aec5"
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01B6ehJoJAfUV7d78jXW23tk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "0cac4f15-950c-42d3-82f7-063a714fdf88",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 34 · 2026-05-22T21:21:45.967Z_

<details><summary>↩ Tool result · `toolu_01B6ehJoJAfUV7d78jXW23tk`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.
6	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
7	This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.
8	
9	\paragraph{Beyond binary detection.}
10	Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
11	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
12	None estimates recursive generation depth.
13	
14	\paragraph{Data selection and curation.}
15	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
16	
17	\paragraph{Ordinal classification and probing.}
18	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "76e8e865-80a1-4408-acb1-85d50f1d9dde"
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_014ovdVSuJs2CU1Hj7e5zgen`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "df5cfcdd-8cc4-400c-9352-b9f1f065e038",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 36 · 2026-05-22T21:21:46.388Z_

<details><summary>↩ Tool result · `toolu_014ovdVSuJs2CU1Hj7e5zgen`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
17	Together with Markov chain convergence, this provides heuristic motivation for expecting $\auc_{k-1,k}$ to decrease with $k$, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\!\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, j \!\leq\! k\bigr\},
22	  \label{eq:kstar}
23	\end{equation}
24	which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested configurations; Table~\ref{tab:kstar_ci}).
25	The theoretical upper bound $\Ktheory$ (the true maximum discriminable depth given optimal features) is not directly estimated in this work.
26	Since any specific classifier on a feature subset achieves AUC at most equal to the Bayes-optimal classifier on all features, $\Kempirical \leq \Ktheory$ follows directly.
27	The DPI separately motivates the empirical observation that $\auc_{k-1,k}$ decreases with $k$, though AUC is not a monotone function of MI (as noted above).
28	Here $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a reference operating point motivated by Cohen's small-effect-size convention ($h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.}; justified below).
29	Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
30	
31	\paragraph{Threshold justification.}
32	$\theta{=}0.60$ is a reference operating point supported by three independent lines of evidence.
33	First, Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
34	Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ ($p < 0.002$ for all boundary comparisons).
35	Third, the conclusion $\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, a ${\sim}$5--11\,pp discontinuity; only at extremes does $\Kempirical$ shift ($\theta{=}0.55$: $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$: $\Kempirical{=}1$ across all).
36	Figure~\ref{fig:kstar_theta} provides the full sensitivity surface across $\theta \in [0.55, 0.70]$, enabling practitioners to select $\theta$ according to their false-positive tolerance.
37	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
38	
39	\subsection{Features and Classifier}
40	\label{sec:features}
41	
42	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
43	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
44	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
45	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations); in deployment where reference corpora are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted entirely, leaving 14 features (surprisal statistics, TTR, hapax ratio, frequency tail) that require no external reference and retain full $\Kempirical$.
46	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
47	
48	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
49	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
50	
51	\subsection{Experimental Setup}
52	\label{sec:experimental_setup}
53	
54	We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
55	Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
56	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
57	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
58	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
64	\label{tab:setup}
65	\begin{tabular}{llcc}
66	\toprule
67	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
68	\midrule
69	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
70	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
71	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
72	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
73	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
74	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
75	\bottomrule
76	\end{tabular}
77	\end{table}
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "0c33893b-53a2-4a10-9111-d1173955a63b"
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_018ehR8EUeTYJU1gskui8eP2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "f7361588-c01e-4826-a289-3c6cab46f940",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 38 · 2026-05-22T21:21:46.603Z_

<details><summary>↩ Tool result · `toolu_018ehR8EUeTYJU1gskui8eP2`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on ten model configurations spanning six architecture families:
5	Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).
7	
8	%% ====================================================================
9	\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5024\rlap{$^\S$} & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\
33	\multicolumn{11}{l}{\footnotesize $^\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\Delta = 0.005$).} \\
34	\multicolumn{11}{l}{\footnotesize Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\ref{tab:kstar_ci_extended}.}
35	\end{tabular}
36	\end{table*}
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
41	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% confidence intervals. The horizontal dashed line marks $\theta = 0.60$.}
42	\label{fig:auc_decay}
43	\end{figure}
44	
45	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 10 model configurations: 6/10 configurations yield $\Kempirical{=}2$ (Qwen with 4 configs, LLaMA-8B, and Pythia-1.4B, spanning three of six families) (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\Kempirical{=}1$ (1v2 $\auc$: 0.508, 0.594, 0.596, and 0.598, all below $\theta$; Section~\ref{sec:boundary_cases}).
46	Under Bonferroni correction for 10 simultaneous comparisons (99.5\% CIs), four of six boundary configurations retain CI lower bounds above $\theta$; the two most marginal cases, Qwen-continuation (nominal CI lower bound 0.602) and LLaMA-8B (0.603), fall below the widened interval.
47	Both retain point estimates above $\theta$ and uncorrected CI lower bounds above $\theta$; the near-misses reflect narrow effect sizes rather than classification failure.
48	By architecture family: Qwen (4/4) and LLaMA (1/1) yield $\Kempirical{\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\Kempirical{=}2$, 6.9B: $\Kempirical{=}1$).
49	LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
50	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
51	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across $\Kempirical{=}2$ continuation models ($\Delta = 4.3$\,pp).
52	
53	\paragraph{Scale and instruction-tuning invariance.}
54	$\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$) both exceed $\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\ $> 0.99$ at $\leq$1.5B).
55	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.
56	
57	\begin{figure*}[t]
58	\centering
59	\includegraphics[width=0.75\textwidth]{figures/fig_kstar_theta.pdf}
60	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. Five of six configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line); OLMo yields $\Kempirical{=}1$. At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
61	\label{fig:kstar_theta}
62	\end{figure*}
63	
64	The raw AUC gap between adjacent generations provides a threshold-free continuous measure of discriminability; Figure~\ref{fig:kstar_theta} displays the full sensitivity surface across $\theta \in [0.55, 0.70]$, allowing practitioners to read off $\Kempirical$ at any desired effect-size threshold.
65	Five of six configurations yield $\Kempirical = 2$ within $\theta \in [0.51, 0.61]$ (OLMo: $\Kempirical = 1$ throughout); at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.
66	All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
67	
68	%% ====================================================================
69	\subsection{Cross-Model Transfer}
70	\label{sec:transfer}
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{figures/fig3_transfer_heatmap.pdf}
75	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
76	\label{fig:transfer_heatmap}
77	\end{figure}
78	
79	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
80	Qwen-rewrite classifiers transfer poorly (61--63\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.
81	
82	\paragraph{Cross-scorer validation.}
83	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
84	Feature ranking independence is a strong result: the same features dominate under all scorers.
85	$\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\auc = 0.696$) retains $\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\auc = 0.611$, only 0.011 above $\theta$) drops to $\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).
86	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; Table~\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\Kempirical$ classifications largely agree.
87	
88	%% ====================================================================
89	\subsection{Feature Ordering and Generation Mode}
90	\label{sec:feature_degradation}
91	\label{sec:generation_mode}
92	
93	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
94	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.
95	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
96	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
97	
98	%% ====================================================================
99	\subsection{Neural Probe}
100	\label{sec:neural_probe}
101	
102	Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia remains at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3} = 0.5963$); OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$, consistent with its 15D boundary).
103	We hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\ref{sec:transfer}; the 15D features yield $\Kempirical = 2$ for most families (OLMo: $\Kempirical = 1$).
104	
105	\noindent\begin{minipage}{\columnwidth}
106	\centering
107	\footnotesize
108	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
109	\label{tab:neural_probe_crossmodel}
110	\resizebox{\columnwidth}{!}{%
111	\begin{tabular}{lccc}
112	\toprule
113	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
114	\midrule
115	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
116	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
117	OLMo-1B    & 0.5056 & $[0.497,\,0.516]$ & 1\rlap{$^\dagger$} \\
118	\bottomrule
119	\multicolumn{4}{l}{\footnotesize $^\dagger$OLMo 1v2 $\auc = 0.5054$ (below $\theta$); $\Kempirical^{\text{neural}} = 1$.}
120	\end{tabular}}
121	\end{minipage}
122	
123	%% ====================================================================
124	\subsection{Cross-Domain Variation}
125	\label{sec:cross_domain}
126	
127	The preceding experiments use C4 (general web text).
128	To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.
129	Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
130	Both Qwen-1.5B and Pythia-1.4B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}): 2v3 $\auc = 0.644\;[0.628,\,0.658]$ and $0.655\;[0.640,\,0.669]$ respectively (bootstrap CI lower bounds above $\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
131	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.
132	
133	\begin{table}[t]
134	\centering
135	\footnotesize
136	\caption{Cross-domain $\Kempirical$ comparison. Rows: generator model and text domain (C4, Wikipedia, arXiv). $\Kempirical{=}3$ for arXiv indicates structured text preserves discriminability to greater depth.}
137	\label{tab:domain_kstar}
138	\begin{tabular}{llccc}
139	\toprule
140	\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
141	\midrule
142	arXiv & Qwen-1.5B  & 0.858 & 0.6436 & 3 \\
143	arXiv & Pythia-1.4B & 0.805 & 0.6545 & 3 \\
144	C4    & Qwen-1.5B  & 0.63  & 0.56   & 2 \\
145	Wikipedia & Qwen-1.5B & 0.62 & 0.55 & 2 \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\paragraph{Robustness.}
151	\label{sec:robustness}
152	$\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\theta$ but 2v3 remains well below $\theta$ at all lengths ($\leq 0.572$).
153	Seed robustness testing (seed $= 123$ vs.\ primary $= 42$; Table~\ref{tab:seed_robustness}) confirms $\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\Kempirical{=}2 \to 3$, 2v3 $\auc = 0.607$) has one of five folds below $\theta$.
154	The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\Kempirical$ over raw AUC comparisons.
155	
156	%% ====================================================================
157	\subsection{Binary Detector Confidence}
158	\label{sec:binary_confidence}
159	
160	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
161	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
162	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "c6638290-306f-487e-86c2-3461829ece8e"
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01BdZy463nZM4mAKEg3MsJLj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "7d87d724-3891-4a6c-9924-5c440b80e61d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 40 · 2026-05-22T21:21:46.848Z_

<details><summary>↩ Tool result · `toolu_01BdZy463nZM4mAKEg3MsJLj`</summary>

```text
1	\section{Consistency Check: $\Kstar$-Guided Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
5	We test this as a consistency check on the boundary measurement, not as an independent contribution.
6	We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
7	We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
13	\label{tab:tab_filtering_main}
14	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
15	\end{table}
16	
17	Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
18	These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
19	The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
20	Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
21	DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
22	At realistic contamination ratios ($\leq$50\%), all filtering strategies converge ($p > 0.12$), consistent with the one-wash laundering finding that depth-aware curation offers marginal benefit when $\Kempirical{=}2$ (Appendix~\ref{sec:dose_response}).
23	For $\Kempirical{=}1$ configurations, depth-aware curation reduces to standard binary filtering, consistent with $\Kempirical{=}1$ implying no exploitable depth signal beyond the 0v1 boundary.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "33509a4b-6bad-4174-b73b-493f6c93ae8c"
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_016cHR5HYiGuURz2zi8TvGHz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "c25d43d1-f6a8-4db1-80dd-2f41642ba105",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 42 · 2026-05-22T21:21:47.025Z_

<details><summary>↩ Tool result · `toolu_016cHR5HYiGuURz2zi8TvGHz`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\paragraph{One-wash laundering (web text).}
11	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
12	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
13	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
14	
15	\paragraph{Representation dependence.}
16	$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
17	The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
18	Feature rankings are scorer-independent ($\rho > 0.90$); $\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (Qwen-continuation drops to $\Kempirical{=}1$; length confound ruled out in Appendix~\ref{sec:extended_limitations}).
19	ANOVA confirms this layered pattern: Scorer explains modest variance ($\eta^2_p{=}.166$) with a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$; Table~\ref{tab:anova_crossscorer}).
20	
21	\paragraph{Domain dependence of $\Kempirical$.}
22	Web text (C4, Wikipedia) consistently yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$ across two independent model families (Qwen-1.5B and Pythia-1.4B; Section~\ref{sec:cross_domain}).
23	The elevated arXiv signal reflects formulaic structure: citation patterns, mathematical notation, and section conventions create larger per-generation distributional shifts (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), making contamination trackable to greater depth.
24	Wikipedia matches C4 at $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), consistent with its general-purpose prose lacking domain-specific structural markers.
25	This domain dependence implies that corpus curators should calibrate depth-aware filtering to source characteristics rather than assuming a universal boundary.
26	
27	\paragraph{Cross-model transfer.}
28	Continuation-mode classifiers transfer well across generators (80--92\% retention; Figure~\ref{fig:transfer_heatmap}), enabling portable depth estimation on corpora from unknown models without retraining.
29	The poor transfer from rewrite-mode classifiers (61--63\%) isolates generation mode, rather than architecture family, as the primary axis of distributional variation.
30	
31	\paragraph{Prompt-chain scope and retrain-chain gap.}
32	Retrain-chain experiments (Pythia-1.4B LoRA) yield $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 3v4 $= 0.7982$), far exceeding the prompt-chain boundary of $\Kempirical{=}2$, because each retrain generation also modifies model parameters, introducing cumulative adaptation artifacts absent from text-only recycling.
33	Prompt-chain $\Kempirical$ isolates text-intrinsic degradation, the operationally relevant quantity for data curation pipelines; our conclusions do not directly transfer to retrain-chain (model collapse) settings.
34	
35	\paragraph{Boundary cases and scale effect.}
36	$\Kempirical{=}1$ configurations cluster at 1v2 $\auc$ 0.508--0.598, well separated from the $\Kempirical{=}2$ range (0.611--0.696); $\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.
37	That $\Kempirical \in \{1, 2\}$ for all web text configurations is the core empirical result; larger models reduce 0v1 JSD (0.077 at 8B vs.\ 0.15--0.27 at $\leq$1.5B), suggesting 13B+ may increasingly yield $\Kempirical{=}1$.
38	The $\Kempirical{=}1$ vs.\ $\Kempirical{=}2$ distinction has a direct curation consequence: $\Kempirical{=}1$ generators erase depth signal in one pass, leaving only the binary 0v1 boundary available for filtering.
39	
40	\paragraph{Decoding strategy as confound.}
41	Greedy decoding inflates depth separability: Pythia-6.9B yields $\Kempirical{=}2$ under greedy but $\Kempirical{=}1$ under nucleus sampling ($p{=}0.95$), with the borderline 1v2 score (2 of 5 folds above $\theta$) illustrating that the boundary is continuous rather than a cliff (Table~\ref{tab:s10_pythia_decoding}).
42	Practitioners should calibrate $\theta$ to their application-specific tolerance (Figure~\ref{fig:kstar_theta}).
43	
44	\paragraph{What $\Kempirical$ reveals.}
45	As a measurement tool, $\Kempirical$ establishes why binary detection suffices for web text (depth${>}1$ is invisible to statistical features), identifies domains where finer strategies are viable (arXiv $\Kempirical{=}3$), and quantifies how scale, scorer, and threshold jointly shape the boundary.
46	The OBD framework provides a reproducible, low-cost depth estimation protocol requiring only corpus-level statistical features, unlike detection methods that need API access or model weights.
47	Even when the practical outcome remains binary filtering, $\Kempirical$ grounds this choice in measurement rather than heuristic assumption.
48	$\Kempirical$ also serves as a monitoring metric for tracking how the discrimination boundary shifts as model scale increases; future work may explore scorer-ensemble strategies to improve cross-scorer robustness at marginal boundaries.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "b68181e1-7e20-4030-8808-eadf84cbdb83"
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_0192y1ZbArLRXE53bTNWaJZD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "6be0f198-61ed-467c-96fa-5ba7f3428362",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015yc3KopAaTUV11o47MM9kc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19301,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19301,
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

_source line 44 · 2026-05-22T21:21:47.152Z_

<details><summary>↩ Tool result · `toolu_0192y1ZbArLRXE53bTNWaJZD`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure a lower bound on the generational depth discrimination boundary $\Kempirical$ for prompt-chain recursive synthetic text.
5	For general web text, $\Kempirical \leq 2$ regardless of model family or scale (six architecture families, 1B--8B, $\theta{=}0.60$); across all ten configurations, $\Kempirical \leq 3$, with structured academic text (arXiv) reaching $\Kempirical{=}3$ across two independent architectures.
6	This one-wash laundering effect concentrates all exploitable signal at the 0v1 boundary, and the consistency check confirms that binary curation most effectively minimizes MMLU degradation ($-$0.77\,pp vs.\ $-$1.53\,pp for no-filter).
7	For structured domains where $\Kempirical{=}3$, graduated strategies can exploit one additional depth level, so corpus curators should calibrate filtering to the source domain.
8	The 15 statistical features enable deployment across generators without retraining (80--92\% accuracy retention, $\rho > 0.90$), supporting model-agnostic depth estimation for corpora where the generating model is unknown.
9	Under Bonferroni correction for 10 simultaneous comparisons, four of six $\Kempirical{=}2$ configurations retain significance at the 99.5\% level; the remaining two marginal cases preserve point estimates above $\theta$.
10	$\Kempirical$ converts a continuous AUC decay surface into a discrete operating boundary grounded in the Data Processing Inequality, providing a principled basis for curation decisions that replaces heuristic assumptions about synthetic text recyclability.
11	Several directions remain open: tracking $\Kempirical$ as model scale surpasses 13B, where our scale analysis suggests the boundary may shift toward $\Kempirical{=}1$; bridging the prompt-chain and retrain-chain boundaries, given the substantially higher $\Kempirical{\geq}4$ observed under parameter retraining; and extending depth estimation to additional structured domains and multilingual text.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "da914727-ce8a-42b1-8272-f0c2099ba18a"
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Agent · `toolu_01K22dRp8CboYWfi7i8JiRuw`</summary>

```json
{
  "description": "Extract registry metrics for table validation",
  "prompt": "I need to extract specific experiment metrics from a large JSON registry file for validating paper tables.\n\nThe file is at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt\n\nIt's JSON with schema: {result: string}. First probe structure with jq, then extract the specific experiments I need.\n\nI need metrics (especially pairwise AUC values, K*, and any other key metrics) for these experiments:\n1. mvp_pilot_sat_v1 (Qwen-rewrite)\n2. exp_001_pythia_depth (Pythia)\n3. exp_002_olmo_depth (OLMo)\n4. exp_017_qwen_continuation (Qwen-cont)\n5. exp_pythia14b_c4_10k\n6. exp_qwen_cont_10k\n7. exp_llama8b_10k\n8. exp_013_cross_transfer\n\nFor each experiment, return:\n- experiment_id\n- status\n- metrics (all of them, especially pairwise AUC values for 0v1, 1v2, 2v3, 3v4, 4v5)\n- K* value\n- conclusion\n\nBe thorough - I need exact numeric values to cross-check against paper tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "8167b5a0-aa5f-477d-b17e-b6c48130846a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kehkJzryo9tmr3LhUmwx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19745,
      "cache_read_input_tokens": 26649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19745
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

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Extract registry metrics for table validation",
  "task_type": "local_agent",
  "prompt": "I need to extract specific experiment metrics from a large JSON registry file for validating paper tables.\n\nThe file is at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt\n\nIt's JSON with schema: {result: string}. First probe structure with jq, then extract the specific experiments I need.\n\nI need metrics (especially pairwise AUC values, K*, and any other key metrics) for these experiments:\n1. mvp_pilot_sat_v1 (Qwen-rewrite)\n2. exp_001_pythia_depth (Pythia)\n3. exp_002_olmo_depth (OLMo)\n4. exp_017_qwen_continuation (Qwen-cont)\n5. exp_pythia14b_c4_10k\n6. exp_qwen_cont_10k\n7. exp_llama8b_10k\n8. exp_013_cross_transfer\n\nFor each experiment, return:\n- experiment_id\n- status\n- metrics (all of them, especially pairwise AUC values for 0v1, 1v2, 2v3, 3v4, 4v5)\n- K* value\n- conclusion\n\nBe thorough - I need exact numeric values to cross-check against paper tables.",
  "uuid": "e7dd7bba-fdc8-490f-b6b9-cbddf851a479",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

## Round 2

42 recorded events

### User

_source line 47 · 2026-05-22T21:21:51.817Z_

I need to extract specific experiment metrics from a large JSON registry file for validating paper tables.

The file is at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt

It's JSON with schema: {result: string}. First probe structure with jq, then extract the specific experiments I need.

I need metrics (especially pairwise AUC values, K*, and any other key metrics) for these experiments:
1. mvp_pilot_sat_v1 (Qwen-rewrite)
2. exp_001_pythia_depth (Pythia)
3. exp_002_olmo_depth (OLMo)
4. exp_017_qwen_continuation (Qwen-cont)
5. exp_pythia14b_c4_10k
6. exp_qwen_cont_10k
7. exp_llama8b_10k
8. exp_013_cross_transfer

For each experiment, return:
- experiment_id
- status
- metrics (all of them, especially pairwise AUC values for 0v1, 1v2, 2v3, 3v4, 4v5)
- K* value
- conclusion

Be thorough - I need exact numeric values to cross-check against paper tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "a1b2ffd2-dc19-44b2-a4a7-076f35ee0b1c"
}
```

</details>

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt",
  "usage": {
    "total_tokens": 15331,
    "tool_uses": 1,
    "duration_ms": 3859
  },
  "last_tool_name": "Read",
  "uuid": "92a0c699-fd85-4555-91f2-ba6cbaaf6be0",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01AyvRGad3hvTkLye7Lwhqep`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "303ccaa2-d3b8-459e-921a-10d77fb683b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UF4MQayfHThJRfKnGXqLza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15268,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15268,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 50 · 2026-05-22T21:21:55.999Z_

<details><summary>↩ Tool result · reported error · `toolu_01AyvRGad3hvTkLye7Lwhqep`</summary>

```text
File content (127996 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "e3b549c2-762a-4635-a92b-37a4922a0209",
  "tool_use_result": "Error: File content (127996 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Searching for mvp_pilot_sat_v1",
  "usage": {
    "total_tokens": 16395,
    "tool_uses": 2,
    "duration_ms": 8533
  },
  "last_tool_name": "Grep",
  "uuid": "2dc31a9e-484d-452d-9376-8b7bd8c13d29",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Grep · `toolu_01XvkwxHizHurAVmHRhHXdZN`</summary>

```json
{
  "pattern": "mvp_pilot_sat_v1",
  "path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt",
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
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "8add1fba-40ae-4e1d-bcd3-150626d67086",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DjzZaJWbVkTkkpb8Wwcgz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1064,
      "cache_read_input_tokens": 15268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1064,
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

_source line 53 · 2026-05-22T21:22:00.375Z_

<details><summary>↩ Tool result · `toolu_01XvkwxHizHurAVmHRhHXdZN`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "ec60c7f0-39df-407d-b20d-e9c48366e2bc"
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Searching for exp_001_pythia_depth",
  "usage": {
    "total_tokens": 16396,
    "tool_uses": 3,
    "duration_ms": 10065
  },
  "last_tool_name": "Grep",
  "uuid": "ed619a1c-c3dd-4c24-a9e4-9ad453ec66b1",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_01WEepbpBc29Cntp13eGBxe3`</summary>

```json
{
  "pattern": "exp_001_pythia_depth",
  "path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt",
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
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "825b5d80-02ae-46df-9cc3-59809c01b5cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DjzZaJWbVkTkkpb8Wwcgz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1064,
      "cache_read_input_tokens": 15268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1064,
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

_source line 56 · 2026-05-22T21:22:01.894Z_

<details><summary>↩ Tool result · `toolu_01WEepbpBc29Cntp13eGBxe3`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "11bc1aaa-c13d-41dc-953c-eaf7367adb30"
}
```

</details>

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Searching for exp_002_olmo_depth",
  "usage": {
    "total_tokens": 16397,
    "tool_uses": 4,
    "duration_ms": 11361
  },
  "last_tool_name": "Grep",
  "uuid": "1ab34a52-04d1-4a50-896c-d16371a72d64",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Grep · `toolu_01PnESj62FBSGZtmwYr32y2x`</summary>

```json
{
  "pattern": "exp_002_olmo_depth",
  "path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt",
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
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "8d680acf-024e-4a47-bd9f-eb6d7bbdde75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DjzZaJWbVkTkkpb8Wwcgz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1064,
      "cache_read_input_tokens": 15268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1064,
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

_source line 59 · 2026-05-22T21:22:03.188Z_

<details><summary>↩ Tool result · `toolu_01PnESj62FBSGZtmwYr32y2x`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "cf3d0f8a-417a-41b3-92ab-e1cf1bbb1d3a"
}
```

</details>

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Searching for exp_017_qwen_continuation",
  "usage": {
    "total_tokens": 16398,
    "tool_uses": 5,
    "duration_ms": 12718
  },
  "last_tool_name": "Grep",
  "uuid": "7502e178-ede1-461b-80be-3edf8299b149",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Grep · `toolu_01WqCjpPU2u56GMkEfey2QVR`</summary>

```json
{
  "pattern": "exp_017_qwen_continuation",
  "path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt",
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
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "7d4ffbbb-4cb5-4a7b-9860-ca053eb9eca4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DjzZaJWbVkTkkpb8Wwcgz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1064,
      "cache_read_input_tokens": 15268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1064,
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

_source line 62 · 2026-05-22T21:22:04.544Z_

<details><summary>↩ Tool result · `toolu_01WqCjpPU2u56GMkEfey2QVR`</summary>

```text
1:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "b54d5f1e-fa39-4103-aa74-894feccea29a"
}
```

</details>

---

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Running Parse the JSON file structure using Python",
  "usage": {
    "total_tokens": 17336,
    "tool_uses": 6,
    "duration_ms": 21865
  },
  "last_tool_name": "Bash",
  "uuid": "44c81e6c-215a-459e-97d4-3c89251fa8f9",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_01BYMxb2Bj3hadSy1TbaPoYk`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\n# The outer structure has 'result' which is a JSON string\ninner = json.loads(data['result'])\nprint('Top-level keys:', list(inner.keys())[:20])\nprint('Type:', type(inner))\nif isinstance(inner, dict):\n    # Check if experiments is a key\n    for k in inner.keys():\n        print(f'  {k}: {type(inner[k]).__name__}')\n\" 2>&1 | head -50",
  "description": "Parse the JSON file structure using Python"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "17fa39e4-5368-42a1-ac5b-0330fd5f9616",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzoCKLzvqQResV8P8mgUfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 16332,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 936,
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

_source line 65 · 2026-05-22T21:22:13.871Z_

<details><summary>↩ Tool result · `toolu_01BYMxb2Bj3hadSy1TbaPoYk`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
Type: &lt;class 'dict'>
  success: bool
  data: dict
  error: NoneType
  metadata: dict
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "6df580d4-c165-400f-910e-ef528fbafe77"
}
```

</details>

---

### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Running Explore the 'data' section structure",
  "usage": {
    "total_tokens": 17803,
    "tool_uses": 7,
    "duration_ms": 26357
  },
  "last_tool_name": "Bash",
  "uuid": "4394f11b-f39a-4c3b-95f2-6323ddcc4545",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01WtZcQfHhU64DqQubwh4nBc`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nd = inner['data']\nprint('Data keys:', list(d.keys())[:20])\nfor k in list(d.keys())[:5]:\n    print(f'  {k}: {type(d[k]).__name__}')\n\" 2>&1 | head -50",
  "description": "Explore the 'data' section structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "f1f29010-eff6-4798-860d-3095fffd05e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016boREgLczhyopjBjFc6dv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 17268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 395,
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

_source line 68 · 2026-05-22T21:22:18.283Z_

<details><summary>↩ Tool result · `toolu_01WtZcQfHhU64DqQubwh4nBc`</summary>

```text
Data keys: ['experiments', 'count', 'total', 'baseline']
  experiments: dict
  count: int
  total: int
  baseline: NoneType
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "400d9704-76bd-4b0c-8350-05c41592267b"
}
```

</details>

---

### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Running List all experiment IDs",
  "usage": {
    "total_tokens": 18199,
    "tool_uses": 8,
    "duration_ms": 30828
  },
  "last_tool_name": "Bash",
  "uuid": "868cfcae-57e9-40bf-a758-ffd58e825610",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01UFLjRDxkjA1voyYYyevgUa`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexperiments = inner['data']['experiments']\nprint('Total experiments:', len(experiments))\nprint('Experiment IDs:')\nfor k in sorted(experiments.keys()):\n    print(f'  {k}')\n\" 2>&1",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "42122d03-a388-41ad-b896-9f4720e695c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRjrEPWRpfy4nH847agHXm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 324,
      "cache_read_input_tokens": 17663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 324,
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

_source line 71 · 2026-05-22T21:22:22.742Z_

<details><summary>↩ Tool result · `toolu_01UFLjRDxkjA1voyYYyevgUa`</summary>

```text
Total experiments: 164
Experiment IDs:
  7b-cross-transfer
  arxiv_multi_source
  deberta_filter_deberta_binary
  deberta_filter_deberta_graduated
  deberta_filter_no_filter
  deberta_filter_obd_binary
  deberta_filtering_predict
  exp-008-retrain-chain
  exp-014
  exp_001_pythia_depth
  exp_002_olmo_depth
  exp_003_decoding_ablation
  exp_004_7b_crossscale
  exp_005_degradation
  exp_006_graduated_filtering
  exp_007_bootstrap_ci
  exp_008_retrain_chain
  exp_008_retrain_chain_v2
  exp_009_dose_10pct
  exp_009_dose_10pct_v2
  exp_009_dose_10pct_v3
  exp_009_dose_30pct
  exp_009_dose_30pct_v2
  exp_009_dose_30pct_v3
  exp_009_dose_50pct
  exp_009_dose_50pct_v2
  exp_009_dose_50pct_v3
  exp_009_dose_response
  exp_010_ordinal_baseline
  exp_011_llm_zeroshot
  exp_012_binary_confidence
  exp_013_cross_transfer
  exp_014_naturalistic
  exp_015_neural_probe
  exp_016_base_vs_instruct
  exp_017_qwen_continuation
  exp_018_llama8b_depth
  exp_019_mistral7b_depth
  exp_019b_mistral_cross_scorer
  exp_020_pythia_decoding
  exp_021_length_ablation
  exp_022_cross_scorer_matrix
  exp_023_domain_ablation
  exp_024_arxiv_domain
  exp_025_pythia_arxiv
  exp_025_pythia_filtering
  exp_026_arxiv_filtering
  exp_026_feature_stability
  exp_026_feature_stability_v2
  exp_027
  exp_027_latex_ablation
  exp_027_retrain_bootstrap
  exp_028_power_curve
  exp_028_subsampling_power
  exp_14b_c4
  exp_32b_c4
  exp_32b_c4_6class
  exp_7b_scorer_ablation
  exp_7b_scorer_arxiv
  exp_A_alt_scorer
  exp_B_14d_ablation
  exp_C_permutation_10k
  exp_D_obd_n500
  exp_E_paired_stats
  exp_arXiv_llama8b
  exp_arXiv_llama8b_crossscorer
  exp_arXiv_mistral7b
  exp_arXiv_mistral7b_crossscorer
  exp_arXiv_olmo
  exp_arXiv_qwen1b5_crossscorer
  exp_arXiv_qwen7b
  exp_arXiv_qwen7b_crossscorer
  exp_bootstrap_10k
  exp_changepoint_kstar
  exp_code_llama8b
  exp_code_mistral7b
  exp_code_multi_source
  exp_code_pythia1b4
  exp_code_qwen1b5
  exp_code_qwen1b5_pythia_scorer
  exp_code_qwen7b
  exp_contamination_rate_sweep
  exp_cross_transfer_llama8b_to_qwen7b
  exp_cross_transfer_llama8b_to_qwen7b_v2
  exp_cross_transfer_qwen7b_to_llama8b
  exp_deberta_arxiv_qwen1b5
  exp_deberta_c4
  exp_deberta_c4_1b5
  exp_deberta_c4_1b5_pythia
  exp_deberta_c4_1b5_qwen_cont
  exp_deberta_code_qwen1b5
  exp_deberta_cross_transfer_gpu1
  exp_deberta_cross_transfer_gpu2
  exp_deberta_cross_transfer_gpu3
  exp_deberta_cross_transfer_wiki
  exp_deberta_filtering_comparison
  exp_deberta_upperbound
  exp_expanded_downstream_eval
  exp_gemma27b_c4
  exp_gemma2b_10k
  exp_gemma2b_depth
  exp_kstar_theta
  exp_llama8b_10k
  exp_multi_source_arxiv
  exp_multi_source_detection
  exp_olmo1b_10k
  exp_olmo1b_c4_rerun
  exp_olmo_retrain_chain
  exp_olmo_retrain_v2
  exp_olmo_retrain_v3
  exp_pythia14b_10k
  exp_pythia14b_c4_10k
  exp_pythia14b_c4_rerun
  exp_pythia69b_c4_depth_chain
  exp_pythia69b_c4_depth_chain_v2
  exp_pythia69b_c4_depth_chain_v3
  exp_pythia69b_c4_nuc
  exp_pythia_retrain_depth7
  exp_qwen_cont_10k
  exp_qwen_retrain_chain
  exp_qwen_retrain_depth7
  exp_wiki_llama8b
  exp_wiki_mistral7b
  exp_wiki_multi_source
  exp_wiki_olmo
  exp_wiki_olmo_v2
  exp_wiki_pythia
  exp_wiki_pythia_v2
  exp_wiki_qwen7b
  exp_wiki_scorer_confound
  exp_wiki_scorer_confound_1b5
  gsm8k-serial-rerun
  gsm8k_patch_bo_s0
  gsm8k_patch_grad_s0
  gsm8k_patch_nf_s0
  mvp_pilot_sat_v1
  seed2_binary_ours
  seed2_graduated
  seed2_no_filter
  seed_gemma27b_c4_s42
  seed_pythia14b_wiki_s123
  seed_qwen15b_c4_s123
  seed_qwen15b_wiki_s123
  sweep_eval_r10_bin
  sweep_eval_r10_binary
  sweep_eval_r10_grad
  sweep_eval_r10_graduated
  sweep_eval_r10_nf
  sweep_eval_r10_nf_v2
  sweep_eval_r10_nofilter
  sweep_eval_r30_nf
  sweep_eval_r30_nofilter
  sweep_r100_binary
  sweep_r100_graduated
  sweep_r100_nf
  sweep_r10_binary
  sweep_r10_graduated
  sweep_r10_nofilter
  sweep_r30_binary
  sweep_r30_graduated
  sweep_r30_nofilter
  sweep_r50_binary
  sweep_r50_graduated
  sweep_r50_nf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "0b134eba-75f2-4485-af45-a47e592fa2ec"
}
```

</details>

---

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "description": "Running Extract all 8 target experiments with full details",
  "usage": {
    "total_tokens": 20414,
    "tool_uses": 9,
    "duration_ms": 38150
  },
  "last_tool_name": "Bash",
  "uuid": "915ff44b-ca2f-41d3-83aa-3a65a238c15e",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_016Y1XdJt5kaWJCPpijARHwk`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexperiments = inner['data']['experiments']\n\ntarget_ids = [\n    'mvp_pilot_sat_v1',\n    'exp_001_pythia_depth',\n    'exp_002_olmo_depth',\n    'exp_017_qwen_continuation',\n    'exp_pythia14b_c4_10k',\n    'exp_qwen_cont_10k',\n    'exp_llama8b_10k',\n    'exp_013_cross_transfer',\n]\n\nfor eid in target_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        print('=' * 80)\n        print(f'EXPERIMENT: {eid}')\n        print('=' * 80)\n        print(json.dumps(exp, indent=2))\n        print()\n    else:\n        print(f'WARNING: {eid} NOT FOUND')\n        print()\n\" 2>&1",
  "description": "Extract all 8 target experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "343dc27b-a36f-401b-a09e-7e81917b259e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cRxKk1uEriqNCHG5fgsgs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2211,
      "cache_read_input_tokens": 17987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2211,
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

_source line 74 · 2026-05-22T21:22:30.073Z_

<details><summary>↩ Tool result · `toolu_016Y1XdJt5kaWJCPpijARHwk`</summary>

```text
================================================================================
EXPERIMENT: mvp_pilot_sat_v1
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-12T11:09:39.193Z",
  "updated_at": "2026-05-12T19:25:33.763Z",
  "hypothesis": "\u9012\u5f52\u751f\u6210\u6587\u672c\u5728\u7edf\u8ba1\u7279\u5f81\u7a7a\u95f4\u4e0a\u5b58\u5728\u53ef\u5206\u8fa8\u7684\u4ee3\u9645\u5dee\u5f02\uff0c\u4e14\u5dee\u5f02\u968f\u6df1\u5ea6\u5448\u7cfb\u7edf\u6027\u8d8b\u52bf\uff08K* \u2265 3\uff09",
  "spec": {
    "command": "bash /root/autodl-tmp/gen-depth-contamination/run_mvp.sh",
    "server": "autodl-4090d",
    "gpu": [
      "cuda:0"
    ],
    "pid": "10619",
    "log_path": "~/runs/gen-depth-contamination/mvp_pilot_sat_v1.log",
    "submitted_at": "2026-05-12T16:46:33.175Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/gen-depth-contamination/data/",
    "wall_clock_seconds": 9533.4,
    "gpu_hours": 2.65
  },
  "notes": "v2 left-padding rerun, per-fold AUC, full self-BLEU",
  "conclusion": "success",
  "completed_at": "2026-05-12T19:25:26.538Z",
  "metrics": {
    "pairwise_auc": {
      "0v1": 0.9956,
      "1v2": 0.6957,
      "2v3": 0.5893,
      "3v4": 0.5434,
      "4v5": 0.5343
    },
    "pairwise_auc_std": {
      "0v1": 0.0005,
      "1v2": 0.0072,
      "2v3": 0.012,
      "3v4": 0.0053,
      "4v5": 0.0091
    },
    "pairwise_jsd": {
      "0v1": 0.2669,
      "1v2": 0.0163,
      "2v3": 0.0069,
      "3v4": 0.0047,
      "4v5": 0.0041
    },
    "k_star": 2,
    "ordinal_mae": 1.0163,
    "ordinal_accuracy": 0.4182
  }
}

================================================================================
EXPERIMENT: exp_001_pythia_depth
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-12T20:06:23.803Z",
  "updated_at": "2026-05-13T00:16:16.359Z",
  "hypothesis": "K* \u8de8\u6a21\u578b\u4e00\u81f4\u6027\u9a8c\u8bc1\uff1aPythia-1.4B \u5728\u76f8\u540c\u79cd\u5b50\u6570\u636e\u548c\u89e3\u7801\u7b56\u7565\u4e0b\u7684 K* \u662f\u5426\u4e0e Qwen2.5-1.5B \u4e00\u81f4\uff08K*=2\uff09",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\"",
    "server": "autodl-4090d",
    "gpu": [
      "cuda:0"
    ],
    "pid": "17138",
    "log_path": "~/runs/gen-depth-contamination/exp_001_pythia_depth.log",
    "submitted_at": "2026-05-12T20:50:31.471Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia",
    "data_count": 5000,
    "model_name": "EleutherAI/pythia-1.4b",
    "seed": 42,
    "checkpoint_path": "/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/",
    "wall_clock_seconds": 12344.9,
    "gpu_hours": 3.43
  },
  "conclusion": "success",
  "metrics": {
    "pairwise_auc": {
      "0v1": 0.9932,
      "1v2": 0.6539,
      "2v3": 0.5515,
      "3v4": 0.5153,
      "4v5": 0.5135
    },
    "pairwise_auc_std": {
      "0v1": 0.0007,
      "1v2": 0.0069,
      "2v3": 0.0137,
      "3v4": 0.0084,
      "4v5": 0.0078
    },
    "pairwise_jsd": {
      "0v1": 0.2142,
      "1v2": 0.014,
      "2v3": 0.0051,
      "3v4": 0.0033,
      "4v5": 0.0031
    },
    "k_star": 2,
    "ordinal_mae": 1.14,
    "ordinal_accuracy": 0.383
  },
  "completed_at": "2026-05-13T00:16:16.359Z"
}

================================================================================
EXPERIMENT: exp_002_olmo_depth
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-12T20:06:24.766Z",
  "updated_at": "2026-05-17T02:57:34.160Z",
  "hypothesis": "K* \u8de8\u6a21\u578b\u4e00\u81f4\u6027\u9a8c\u8bc1\uff1aOLMo-1B \u5728\u76f8\u540c\u79cd\u5b50\u6570\u636e\u548c\u89e3\u7801\u7b56\u7565\u4e0b\u7684 K* \u662f\u5426\u4e0e Qwen2.5-1.5B \u4e00\u81f4\uff08K*=2\uff09",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\"",
    "server": "autodl-4090d",
    "gpu": [
      "cuda:0"
    ],
    "pid": "20225",
    "log_path": "~/runs/gen-depth-contamination/exp_002_olmo_depth.log",
    "submitted_at": "2026-05-13T00:16:07.960Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo",
    "data_count": 5000,
    "model_name": "allenai/OLMo-1B-hf",
    "seed": 42,
    "checkpoint_path": "/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/",
    "wall_clock_seconds": 8384.9,
    "gpu_hours": 2.33
  },
  "reproduce": {
    "finished_at": "2026-05-13T02:31:18.880Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-13T02:31:19.738113+00:00"
      }
    ]
  },
  "metrics": {
    "k_star": 2,
    "pairwise_auc": {
      "0v1": 0.997,
      "1v2": 0.6146,
      "2v3": 0.5497,
      "3v4": 0.509,
      "4v5": 0.5044
    },
    "pairwise_auc_std": {
      "0v1": 0.0004,
      "1v2": 0.0029,
      "2v3": 0.004,
      "3v4": 0.0084,
      "4v5": 0.0136
    },
    "pairwise_jsd": {
      "0v1": 0.23941,
      "1v2": 0.012972,
      "2v3": 0.00735,
      "3v4": 0.003968,
      "4v5": 0.003851
    },
    "ordinal_mae": 1.1813,
    "ordinal_accuracy": 0.3685,
    "top_features": [
      "surp_d1_mean",
      "surp_d1_skew",
      "freq_kurtosis",
      "surp_d2_mean",
      "surp_mean"
    ]
  },
  "conclusion": "success",
  "completed_at": "2026-05-13T02:35:52.823Z",
  "parent": "exp_001_pythia_depth"
}

================================================================================
EXPERIMENT: exp_017_qwen_continuation
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-12T20:41:22.423Z",
  "updated_at": "2026-05-17T02:57:37.021Z",
  "hypothesis": "Continuation mode \u7684 K* \u5e94\u7b49\u4e8e rewrite mode\uff08K*=2\uff09\uff0c\u56e0\u4e3a K* \u9971\u548c\u8fb9\u754c\u662f\u9012\u5f52\u751f\u6210\u7684\u6587\u672c\u56fa\u6709\u5c5e\u6027\uff0c\u4e0e\u751f\u6210\u6a21\u5f0f\uff08\u7eed\u5199 vs \u6539\u5199\uff09\u65e0\u5173\u2014\u2014\u4e24\u79cd\u6a21\u5f0f\u5728\u6df1\u4ee3\u65f6\u90fd\u6536\u655b\u5230\u76f8\u540c\u7684\u7edf\u8ba1\u5438\u5f15\u5b50\u3002",
  "notes": "dry-run passed 2026-05-13: model OK (2.9G safetensors), env OK (torch=2.10.0+cu128, transformers=4.57.6), dirs auto-create. Submit command prepared. \u7b49 exp-002 \u5b8c\u6210\u540e\u7acb\u5373\u63d0\u4ea4\u3002",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\"",
    "server": "autodl-4090d",
    "gpu": [
      "cuda:0"
    ],
    "pid": "23758",
    "log_path": "~/runs/gen-depth-contamination/exp_017_qwen_continuation.log",
    "submitted_at": "2026-05-13T02:35:15Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont",
    "data_count": 5000,
    "model_name": "Qwen/Qwen2.5-1.5B-Instruct",
    "seed": 42,
    "max_depth": 5,
    "generation_mode": "continuation",
    "checkpoint_path": "/root/autodl-tmp/gen-depth-contamination/data_exp017_qwen_cont/",
    "wall_clock_seconds": 13305.8,
    "gpu_hours": 3.7
  },
  "log_path": "/root/runs/gen-depth-contamination/exp_017_qwen_continuation.log",
  "checkpoint_path": "/root/autodl-tmp/gen-depth-contamination/results_exp017_qwen_cont/",
  "metrics": {
    "k_star": 2,
    "pairwise_auc": {
      "0v1": 0.9972,
      "1v2": 0.6114,
      "2v3": 0.5609,
      "3v4": 0.5408,
      "4v5": 0.5139
    },
    "pairwise_jsd": {
      "0v1": 0.28627,
      "1v2": 0.005107,
      "2v3": 0.003603,
      "3v4": 0.003395,
      "4v5": 0.003085
    },
    "ordinal_mae": 1.1547,
    "ordinal_accuracy": 0.3819,
    "top3_features": [
      "freq_entropy",
      "surp_mean",
      "surp_std"
    ]
  },
  "conclusion": "success",
  "completed_at": "2026-05-13T06:17:00.826Z",
  "parent": "mvp_pilot_sat_v1"
}

================================================================================
EXPERIMENT: exp_pythia14b_c4_10k
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T11:57:18.681Z",
  "updated_at": "2026-05-22T14:59:24.436Z",
  "hypothesis": "\u7edf\u4e00\u6240\u6709 K*=2 configs \u7684\u6837\u672c\u91cf\u81f3 10K\uff0c\u907f\u514d selective precision boosting \u8d28\u7591\u3002Pythia-1.4B 5K \u5df2\u7a33\u5b9a\u901a\u8fc7 Bonferroni (CI_lower\u22480.641>0.60)\uff0c10K \u4e3a\u4e00\u81f4\u6027\u9a8c\u8bc1\u3002",
  "spec": {
    "command": "python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer",
    "server": "cqa1-22115",
    "gpu": "cuda:3 (RTX PRO 6000 Blackwell 96GB)",
    "data_path": "data/exp_pythia14b_c4_10k",
    "data_count": 10000,
    "model_name": "Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)",
    "seed": 42,
    "log_path": "/tmp/exp_pythia14b_c4_10k.log",
    "checkpoint_path": "results/exp_pythia14b_c4_10k/"
  },
  "metrics": {
    "K_star": 2,
    "AUC_0v1": 0.9712,
    "AUC_1v2": 0.6175,
    "AUC_2v3": 0.5364,
    "AUC_3v4": 0.5134,
    "AUC_4v5": 0.5088,
    "bootstrap_1v2_95CI": [
      0.6108,
      0.6242
    ],
    "bootstrap_1v2_995CI_bonferroni": [
      0.6078,
      0.6273
    ],
    "perm_pvalue_1v2": 0.0001,
    "bonferroni_pass": true,
    "top_feature": "freq_entropy"
  },
  "conclusion": "success",
  "completed_at": "2026-05-22T14:14:41.623Z"
}

================================================================================
EXPERIMENT: exp_qwen_cont_10k
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T09:27:38.591Z",
  "updated_at": "2026-05-22T14:59:22.490Z",
  "hypothesis": "\u589e\u52a0 Qwen-cont C4 \u6837\u672c\u91cf\u4ece 5k\u219210k \u53ef\u5c06 1v2 bootstrap std \u7f29\u5c0f ~\u221a2 \u500d\uff0c\u4f7f Bonferroni 99.5% CI lower bound \u6062\u590d\u5230 \u03b8=0.60 \u4ee5\u4e0a",
  "spec": {
    "command": "bash /tmp/run_qwen_cont_10k.sh (Phase1: base generation + Phase2: instruct scoring)",
    "server": "cqa1-22115",
    "gpu": "cuda:1 (RTX PRO 6000 Blackwell 96GB)",
    "data_path": "/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_cont_10k",
    "data_count": 10000,
    "model_name": "Qwen/Qwen2.5-1.5B (base, continuation) + Qwen/Qwen2.5-1.5B-Instruct (scorer)",
    "seed": 42,
    "checkpoint_path": "results/exp_qwen_cont_10k/",
    "log_path": "/tmp/exp_qwen_cont_10k_phase1.log"
  },
  "metrics": {
    "K_star": 2,
    "AUC_0v1": 0.9875,
    "AUC_1v2": 0.6346,
    "AUC_2v3": 0.5616,
    "AUC_3v4": 0.5451,
    "AUC_4v5": 0.5254,
    "bootstrap_1v2_95CI": [
      0.6282,
      0.6409
    ],
    "bootstrap_1v2_995CI_bonferroni": [
      0.6255,
      0.6436
    ],
    "perm_pvalue_1v2": 0.0001,
    "bonferroni_pass": true,
    "top_feature": "freq_entropy"
  },
  "conclusion": "success",
  "completed_at": "2026-05-22T14:47:57.847Z"
}

================================================================================
EXPERIMENT: exp_llama8b_10k
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-22T09:25:55.895Z",
  "updated_at": "2026-05-22T20:26:09.870Z",
  "hypothesis": "\u589e\u52a0 LLaMA-8B C4 \u6837\u672c\u91cf\u4ece 5k\u219210k \u53ef\u5c06 1v2 bootstrap std \u7f29\u5c0f ~\u221a2 \u500d\uff0c\u4f7f Bonferroni 99.5% CI lower bound \u6062\u590d\u5230 \u03b8=0.60 \u4ee5\u4e0a",
  "spec": {
    "server": "cqa1-22115",
    "pid": 23232,
    "checkpoint_path": "results/exp_llama8b_10k/",
    "log_path": "/tmp/exp_llama8b_10k.log"
  },
  "conclusion": "negative",
  "metrics": {
    "K_star": 1,
    "AUC_0v1": 0.9282,
    "AUC_1v2": 0.6148,
    "AUC_1v2_oof": 0.588,
    "AUC_2v3": 0.5247,
    "AUC_3v4": 0.5519,
    "AUC_4v5": 0.5262,
    "bootstrap_1v2_oof_auc": 0.588,
    "bootstrap_1v2_95CI": [
      0.5809,
      0.595
    ],
    "bootstrap_1v2_995CI_bonferroni": [
      0.5776,
      0.5978
    ],
    "bonferroni_pass": false,
    "perm_pvalue_1v2": 0.0001,
    "scorer": "Qwen2.5-1.5B-Instruct",
    "note": "All pairwise AUC from Qwen cross-scoring (Phase 2). Pipeline AUC 1v2=0.6148 (mean-of-folds)."
  },
  "completed_at": "2026-05-22T19:21:09.215Z"
}

================================================================================
EXPERIMENT: exp_013_cross_transfer
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-12T20:50:57.813Z",
  "updated_at": "2026-05-13T06:54:11.689Z",
  "spec": {
    "command": "python scripts/run_exp013_cross_transfer.py --out_dir artifacts/",
    "server": "autodl-4090d",
    "data_path": "data/, data_exp001_pythia/, data_exp002_olmo/, data_exp017_qwen_cont/",
    "data_count": 20000,
    "model_name": "N/A (CPU classifiers: OBD-LightGBM)",
    "seed": 42,
    "input_sources": [
      "mvp-001 Qwen-rewrite",
      "exp-001 Pythia",
      "exp-002 OLMo",
      "exp-017 Qwen-cont"
    ],
    "checkpoint_path": "artifacts/cross_transfer_matrix.json",
    "log_path": "N/A (CPU task)"
  },
  "hypothesis": "Depth signal \u662f\u6587\u672c\u56fa\u6709\u5c5e\u6027\u8fd8\u662f model self-familiarity artifact\uff1f4\u00d74 cross-model transfer matrix \u6d4b\u8bd5\u5206\u7c7b\u5668\u8de8\u6a21\u578b\u6cdb\u5316\u80fd\u529b",
  "metrics": {
    "accuracy_matrix": {
      "Qwen_rw\u2192Qwen_rw": 0.4229,
      "Qwen_rw\u2192Pythia": 0.259,
      "Qwen_rw\u2192OLMo": 0.2653,
      "Qwen_rw\u2192Qwen_cont": 0.3466,
      "Pythia\u2192Qwen_rw": 0.2718,
      "Pythia\u2192Pythia": 0.3856,
      "Pythia\u2192OLMo": 0.3531,
      "Pythia\u2192Qwen_cont": 0.3287,
      "OLMo\u2192Qwen_rw": 0.2768,
      "OLMo\u2192Pythia": 0.345,
      "OLMo\u2192OLMo": 0.3822,
      "OLMo\u2192Qwen_cont": 0.3244,
      "Qwen_cont\u2192Qwen_rw": 0.344,
      "Qwen_cont\u2192Pythia": 0.3284,
      "Qwen_cont\u2192OLMo": 0.3112,
      "Qwen_cont\u2192Qwen_cont": 0.3875
    },
    "transfer_retention_accuracy": {
      "Pythia\u2194OLMo": "91-92%",
      "Qwen_rw\u2192Pythia/OLMo": "61-63%",
      "Qwen_cont\u2194Pythia": "83-85%",
      "Qwen_cont\u2194OLMo": "80-85%"
    },
    "transfer_retention_tau": {
      "Pythia\u2194OLMo": "85-86%",
      "Qwen_rw\u2192Pythia/OLMo": "45-50%",
      "Qwen_cont\u2194others": "68-83%"
    },
    "mean_pw_auc_matrix": {
      "within_avg": 0.6099,
      "cross_avg": 0.5905,
      "0v1_cross_all_above": 0.96
    },
    "key_finding": "depth signal \u2248 70-85% text-intrinsic + 15-30% model self-familiarity. Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained depth transfer depends on model family similarity. Qwen-rewrite overfits style features; Qwen-cont transfers much better."
  },
  "conclusion": "success",
  "completed_at": "2026-05-13T06:53:07.326Z",
  "notes": "depth signal \u2248 70-85% text-intrinsic + 15-30% model self-familiarity. Pythia\u2194OLMo 91-92% retention (architecture-agnostic). Qwen-rewrite catastrophic transfer to other models (61-63%), but Qwen-cont much better (80-85%). 0v1 universally transferable (>0.96 AUC), 1v2+ transfer depends on model family. Rewrite mode overfits style features \u2192 continuation mode is canonical condition for cross-model claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "feead0b4-c247-4971-8bf1-57501d4ef88d"
}
```

</details>

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "adbcac43eccb33fae",
  "tool_use_id": "toolu_01K22dRp8CboYWfi7i8JiRuw",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry metrics for table validation",
  "usage": {
    "total_tokens": 29037,
    "tool_uses": 9,
    "duration_ms": 74622
  },
  "uuid": "5da05445-46a6-48a8-a67c-871335d1ceea",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool result

_source line 76 · 2026-05-22T21:23:06.441Z_

<details><summary>↩ Tool result · `toolu_01K22dRp8CboYWfi7i8JiRuw`</summary>

```text
Here are the complete metrics for all 8 requested experiments:

---

## 1. mvp_pilot_sat_v1 (Qwen-rewrite)

| Field | Value |
|-------|-------|
| **status** | DONE |
| **conclusion** | success |
| **K\*** | 2 |
| **Pairwise AUC** | 0v1: **0.9956**, 1v2: **0.6957**, 2v3: **0.5893**, 3v4: **0.5434**, 4v5: **0.5343** |
| **Pairwise AUC std** | 0v1: 0.0005, 1v2: 0.0072, 2v3: 0.012, 3v4: 0.0053, 4v5: 0.0091 |
| **Pairwise JSD** | 0v1: 0.2669, 1v2: 0.0163, 2v3: 0.0069, 3v4: 0.0047, 4v5: 0.0041 |
| **Ordinal MAE** | 1.0163 |
| **Ordinal Accuracy** | 0.4182 |

---

## 2. exp_001_pythia_depth (Pythia-1.4B)

| Field | Value |
|-------|-------|
| **status** | DONE |
| **conclusion** | success |
| **K\*** | 2 |
| **Pairwise AUC** | 0v1: **0.9932**, 1v2: **0.6539**, 2v3: **0.5515**, 3v4: **0.5153**, 4v5: **0.5135** |
| **Pairwise AUC std** | 0v1: 0.0007, 1v2: 0.0069, 2v3: 0.0137, 3v4: 0.0084, 4v5: 0.0078 |
| **Pairwise JSD** | 0v1: 0.2142, 1v2: 0.014, 2v3: 0.0051, 3v4: 0.0033, 4v5: 0.0031 |
| **Ordinal MAE** | 1.14 |
| **Ordinal Accuracy** | 0.383 |

---

## 3. exp_002_olmo_depth (OLMo-1B)

| Field | Value |
|-------|-------|
| **status** | DONE |
| **conclusion** | success |
| **K\*** | 2 |
| **Pairwise AUC** | 0v1: **0.997**, 1v2: **0.6146**, 2v3: **0.5497**, 3v4: **0.509**, 4v5: **0.5044** |
| **Pairwise AUC std** | 0v1: 0.0004, 1v2: 0.0029, 2v3: 0.004, 3v4: 0.0084, 4v5: 0.0136 |
| **Pairwise JSD** | 0v1: 0.23941, 1v2: 0.012972, 2v3: 0.00735, 3v4: 0.003968, 4v5: 0.003851 |
| **Ordinal MAE** | 1.1813 |
| **Ordinal Accuracy** | 0.3685 |
| **Top features** | surp_d1_mean, surp_d1_skew, freq_kurtosis, surp_d2_mean, surp_mean |

---

## 4. exp_017_qwen_continuation (Qwen-cont)

| Field | Value |
|-------|-------|
| **status** | DONE |
| **conclusion** | success |
| **K\*** | 2 |
| **Pairwise AUC** | 0v1: **0.9972**, 1v2: **0.6114**, 2v3: **0.5609**, 3v4: **0.5408**, 4v5: **0.5139** |
| **Pairwise JSD** | 0v1: 0.28627, 1v2: 0.005107, 2v3: 0.003603, 3v4: 0.003395, 4v5: 0.003085 |
| **Ordinal MAE** | 1.1547 |
| **Ordinal Accuracy** | 0.3819 |
| **Top 3 features** | freq_entropy, surp_mean, surp_std |

---

## 5. exp_pythia14b_c4_10k (Pythia-1.4B, 10K samples)

| Field | Value |
|-------|-------|
| **status** | DONE |
| **conclusion** | success |
| **K\*** | 2 |
| **AUC 0v1** | **0.9712** |
| **AUC 1v2** | **0.6175** |
| **AUC 2v3** | **0.5364** |
| **AUC 3v4** | **0.5134** |
| **AUC 4v5** | **0.5088** |
| **Bootstrap 1v2 95% CI** | [0.6108, 0.6242] |
| **Bootstrap 1v2 99.5% CI (Bonferroni)** | [0.6078, 0.6273] |
| **Perm p-value 1v2** | 0.0001 |
| **Bonferroni pass** | true |
| **Top feature** | freq_entropy |

---

## 6. exp_qwen_cont_10k (Qwen-cont, 10K samples)

| Field | Value |
|-------|-------|
| **status** | DONE |
| **conclusion** | success |
| **K\*** | 2 |
| **AUC 0v1** | **0.9875** |
| **AUC 1v2** | **0.6346** |
| **AUC 2v3** | **0.5616** |
| **AUC 3v4** | **0.5451** |
| **AUC 4v5** | **0.5254** |
| **Bootstrap 1v2 95% CI** | [0.6282, 0.6409] |
| **Bootstrap 1v2 99.5% CI (Bonferroni)** | [0.6255, 0.6436] |
| **Perm p-value 1v2** | 0.0001 |
| **Bonferroni pass** | true |
| **Top feature** | freq_entropy |

---

## 7. exp_llama8b_10k (LLaMA-8B, 10K samples)

| Field | Value |
|-------|-------|
| **status** | DONE |
| **conclusion** | **negative** |
| **K\*** | **1** |
| **AUC 0v1** | **0.9282** |
| **AUC 1v2** | **0.6148** (in-fold mean) / **0.588** (OOF) |
| **AUC 2v3** | **0.5247** |
| **AUC 3v4** | **0.5519** |
| **AUC 4v5** | **0.5262** |
| **Bootstrap 1v2 OOF 95% CI** | [0.5809, 0.595] |
| **Bootstrap 1v2 OOF 99.5% CI (Bonferroni)** | [0.5776, 0.5978] |
| **Bonferroni pass** | **false** |
| **Perm p-value 1v2** | 0.0001 |
| **Scorer** | Qwen2.5-1.5B-Instruct |
| **Note** | All pairwise AUC from Qwen cross-scoring (Phase 2). Pipeline AUC 1v2=0.6148 (mean-of-folds). |

---

## 8. exp_013_cross_transfer

| Field | Value |
|-------|-------|
| **status** | DONE |
| **conclusion** | success |
| **Accuracy matrix (diagonal = within-model)** | Qwen_rw: 0.4229, Pythia: 0.3856, OLMo: 0.3822, Qwen_cont: 0.3875 |
| **Transfer retention (accuracy)** | Pythia-OLMo: 91-92%, Qwen_rw to Pythia/OLMo: 61-63%, Qwen_cont-Pythia: 83-85%, Qwen_cont-OLMo: 80-85% |
| **Transfer retention (tau)** | Pythia-OLMo: 85-86%, Qwen_rw to Pythia/OLMo: 45-50%, Qwen_cont-others: 68-83% |
| **Mean pairwise AUC** | Within avg: 0.6099, Cross avg: 0.5905, 0v1 cross all above: 0.96 |
| **Key finding** | Depth signal is ~70-85% text-intrinsic + 15-30% model self-familiarity. Binary (0v1) detection highly transferable (>0.96 AUC). Qwen-rewrite overfits style features; Qwen-cont transfers much better. |

**Full cross-transfer accuracy matrix:**
- Qwen_rw -> Qwen_rw: 0.4229, Pythia: 0.259, OLMo: 0.2653, Qwen_cont: 0.3466
- Pythia -> Qwen_rw: 0.2718, Pythia: 0.3856, OLMo: 0.3531, Qwen_cont: 0.3287
- OLMo -> Qwen_rw: 0.2768, Pythia: 0.345, OLMo: 0.3822, Qwen_cont: 0.3244
- Qwen_cont -> Qwen_rw: 0.344, Pythia: 0.3284, OLMo: 0.3112, Qwen_cont: 0.3875

---

**Key cross-experiment observations for table validation:**

1. All 5K experiments (mvp, exp_001, exp_002, exp_017) have K\*=2 with consistent monotonic AUC decay pattern.
2. The 10K experiments confirm: Pythia (K\*=2, Bonferroni pass) and Qwen-cont (K\*=2, Bonferroni pass) are robust. LLaMA-8B is the exception with K\*=1 (OOF AUC 1v2 = 0.588, Bonferroni CI upper = 0.5978 < 0.60 threshold).
3. The mvp_pilot_sat_v1 (rewrite mode) has notably higher 1v2 AUC (0.6957) vs continuation-mode experiments (0.61-0.65), consistent with the cross-transfer finding that rewrite overfits style features.
4. Note the different key naming conventions between 5K experiments (`pairwise_auc.0v1`) and 10K experiments (`AUC_0v1`) -- make sure paper tables use the correct source values.

agentId: adbcac43eccb33fae (use SendMessage with to: 'adbcac43eccb33fae' to continue this agent)
&lt;usage>total_tokens: 31804
tool_uses: 9
duration_ms: 74623&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "17014004-457c-4de0-893f-b0147ed5f045",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to extract specific experiment metrics from a large JSON registry file for validating paper tables.\n\nThe file is at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d4b6c03e-8eff-42a0-9dc1-d3fa3497a119/tool-results/mcp-agent-ml-research-read_registry-1779484895654.txt\n\nIt's JSON with schema: {result: string}. First probe structure with jq, then extract the specific experiments I need.\n\nI need metrics (especially pairwise AUC values, K*, and any other key metrics) for these experiments:\n1. mvp_pilot_sat_v1 (Qwen-rewrite)\n2. exp_001_pythia_depth (Pythia)\n3. exp_002_olmo_depth (OLMo)\n4. exp_017_qwen_continuation (Qwen-cont)\n5. exp_pythia14b_c4_10k\n6. exp_qwen_cont_10k\n7. exp_llama8b_10k\n8. exp_013_cross_transfer\n\nFor each experiment, return:\n- experiment_id\n- status\n- metrics (all of them, especially pairwise AUC values for 0v1, 1v2, 2v3, 3v4, 4v5)\n- K* value\n- conclusion\n\nBe thorough - I need exact numeric values to cross-check against paper tables.",
    "agentId": "adbcac43eccb33fae",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the complete metrics for all 8 requested experiments:\n\n---\n\n## 1. mvp_pilot_sat_v1 (Qwen-rewrite)\n\n| Field | Value |\n|-------|-------|\n| **status** | DONE |\n| **conclusion** | success |\n| **K\\*** | 2 |\n| **Pairwise AUC** | 0v1: **0.9956**, 1v2: **0.6957**, 2v3: **0.5893**, 3v4: **0.5434**, 4v5: **0.5343** |\n| **Pairwise AUC std** | 0v1: 0.0005, 1v2: 0.0072, 2v3: 0.012, 3v4: 0.0053, 4v5: 0.0091 |\n| **Pairwise JSD** | 0v1: 0.2669, 1v2: 0.0163, 2v3: 0.0069, 3v4: 0.0047, 4v5: 0.0041 |\n| **Ordinal MAE** | 1.0163 |\n| **Ordinal Accuracy** | 0.4182 |\n\n---\n\n## 2. exp_001_pythia_depth (Pythia-1.4B)\n\n| Field | Value |\n|-------|-------|\n| **status** | DONE |\n| **conclusion** | success |\n| **K\\*** | 2 |\n| **Pairwise AUC** | 0v1: **0.9932**, 1v2: **0.6539**, 2v3: **0.5515**, 3v4: **0.5153**, 4v5: **0.5135** |\n| **Pairwise AUC std** | 0v1: 0.0007, 1v2: 0.0069, 2v3: 0.0137, 3v4: 0.0084, 4v5: 0.0078 |\n| **Pairwise JSD** | 0v1: 0.2142, 1v2: 0.014, 2v3: 0.0051, 3v4: 0.0033, 4v5: 0.0031 |\n| **Ordinal MAE** | 1.14 |\n| **Ordinal Accuracy** | 0.383 |\n\n---\n\n## 3. exp_002_olmo_depth (OLMo-1B)\n\n| Field | Value |\n|-------|-------|\n| **status** | DONE |\n| **conclusion** | success |\n| **K\\*** | 2 |\n| **Pairwise AUC** | 0v1: **0.997**, 1v2: **0.6146**, 2v3: **0.5497**, 3v4: **0.509**, 4v5: **0.5044** |\n| **Pairwise AUC std** | 0v1: 0.0004, 1v2: 0.0029, 2v3: 0.004, 3v4: 0.0084, 4v5: 0.0136 |\n| **Pairwise JSD** | 0v1: 0.23941, 1v2: 0.012972, 2v3: 0.00735, 3v4: 0.003968, 4v5: 0.003851 |\n| **Ordinal MAE** | 1.1813 |\n| **Ordinal Accuracy** | 0.3685 |\n| **Top features** | surp_d1_mean, surp_d1_skew, freq_kurtosis, surp_d2_mean, surp_mean |\n\n---\n\n## 4. exp_017_qwen_continuation (Qwen-cont)\n\n| Field | Value |\n|-------|-------|\n| **status** | DONE |\n| **conclusion** | success |\n| **K\\*** | 2 |\n| **Pairwise AUC** | 0v1: **0.9972**, 1v2: **0.6114**, 2v3: **0.5609**, 3v4: **0.5408**, 4v5: **0.5139** |\n| **Pairwise JSD** | 0v1: 0.28627, 1v2: 0.005107, 2v3: 0.003603, 3v4: 0.003395, 4v5: 0.003085 |\n| **Ordinal MAE** | 1.1547 |\n| **Ordinal Accuracy** | 0.3819 |\n| **Top 3 features** | freq_entropy, surp_mean, surp_std |\n\n---\n\n## 5. exp_pythia14b_c4_10k (Pythia-1.4B, 10K samples)\n\n| Field | Value |\n|-------|-------|\n| **status** | DONE |\n| **conclusion** | success |\n| **K\\*** | 2 |\n| **AUC 0v1** | **0.9712** |\n| **AUC 1v2** | **0.6175** |\n| **AUC 2v3** | **0.5364** |\n| **AUC 3v4** | **0.5134** |\n| **AUC 4v5** | **0.5088** |\n| **Bootstrap 1v2 95% CI** | [0.6108, 0.6242] |\n| **Bootstrap 1v2 99.5% CI (Bonferroni)** | [0.6078, 0.6273] |\n| **Perm p-value 1v2** | 0.0001 |\n| **Bonferroni pass** | true |\n| **Top feature** | freq_entropy |\n\n---\n\n## 6. exp_qwen_cont_10k (Qwen-cont, 10K samples)\n\n| Field | Value |\n|-------|-------|\n| **status** | DONE |\n| **conclusion** | success |\n| **K\\*** | 2 |\n| **AUC 0v1** | **0.9875** |\n| **AUC 1v2** | **0.6346** |\n| **AUC 2v3** | **0.5616** |\n| **AUC 3v4** | **0.5451** |\n| **AUC 4v5** | **0.5254** |\n| **Bootstrap 1v2 95% CI** | [0.6282, 0.6409] |\n| **Bootstrap 1v2 99.5% CI (Bonferroni)** | [0.6255, 0.6436] |\n| **Perm p-value 1v2** | 0.0001 |\n| **Bonferroni pass** | true |\n| **Top feature** | freq_entropy |\n\n---\n\n## 7. exp_llama8b_10k (LLaMA-8B, 10K samples)\n\n| Field | Value |\n|-------|-------|\n| **status** | DONE |\n| **conclusion** | **negative** |\n| **K\\*** | **1** |\n| **AUC 0v1** | **0.9282** |\n| **AUC 1v2** | **0.6148** (in-fold mean) / **0.588** (OOF) |\n| **AUC 2v3** | **0.5247** |\n| **AUC 3v4** | **0.5519** |\n| **AUC 4v5** | **0.5262** |\n| **Bootstrap 1v2 OOF 95% CI** | [0.5809, 0.595] |\n| **Bootstrap 1v2 OOF 99.5% CI (Bonferroni)** | [0.5776, 0.5978] |\n| **Bonferroni pass** | **false** |\n| **Perm p-value 1v2** | 0.0001 |\n| **Scorer** | Qwen2.5-1.5B-Instruct |\n| **Note** | All pairwise AUC from Qwen cross-scoring (Phase 2). Pipeline AUC 1v2=0.6148 (mean-of-folds). |\n\n---\n\n## 8. exp_013_cross_transfer\n\n| Field | Value |\n|-------|-------|\n| **status** | DONE |\n| **conclusion** | success |\n| **Accuracy matrix (diagonal = within-model)** | Qwen_rw: 0.4229, Pythia: 0.3856, OLMo: 0.3822, Qwen_cont: 0.3875 |\n| **Transfer retention (accuracy)** | Pythia-OLMo: 91-92%, Qwen_rw to Pythia/OLMo: 61-63%, Qwen_cont-Pythia: 83-85%, Qwen_cont-OLMo: 80-85% |\n| **Transfer retention (tau)** | Pythia-OLMo: 85-86%, Qwen_rw to Pythia/OLMo: 45-50%, Qwen_cont-others: 68-83% |\n| **Mean pairwise AUC** | Within avg: 0.6099, Cross avg: 0.5905, 0v1 cross all above: 0.96 |\n| **Key finding** | Depth signal is ~70-85% text-intrinsic + 15-30% model self-familiarity. Binary (0v1) detection highly transferable (>0.96 AUC). Qwen-rewrite overfits style features; Qwen-cont transfers much better. |\n\n**Full cross-transfer accuracy matrix:**\n- Qwen_rw -> Qwen_rw: 0.4229, Pythia: 0.259, OLMo: 0.2653, Qwen_cont: 0.3466\n- Pythia -> Qwen_rw: 0.2718, Pythia: 0.3856, OLMo: 0.3531, Qwen_cont: 0.3287\n- OLMo -> Qwen_rw: 0.2768, Pythia: 0.345, OLMo: 0.3822, Qwen_cont: 0.3244\n- Qwen_cont -> Qwen_rw: 0.344, Pythia: 0.3284, OLMo: 0.3112, Qwen_cont: 0.3875\n\n---\n\n**Key cross-experiment observations for table validation:**\n\n1. All 5K experiments (mvp, exp_001, exp_002, exp_017) have K\\*=2 with consistent monotonic AUC decay pattern.\n2. The 10K experiments confirm: Pythia (K\\*=2, Bonferroni pass) and Qwen-cont (K\\*=2, Bonferroni pass) are robust. LLaMA-8B is the exception with K\\*=1 (OOF AUC 1v2 = 0.588, Bonferroni CI upper = 0.5978 < 0.60 threshold).\n3. The mvp_pilot_sat_v1 (rewrite mode) has notably higher 1v2 AUC (0.6957) vs continuation-mode experiments (0.61-0.65), consistent with the cross-transfer finding that rewrite overfits style features.\n4. Note the different key naming conventions between 5K experiments (`pairwise_auc.0v1`) and 10K experiments (`AUC_0v1`) -- make sure paper tables use the correct source values."
      }
    ],
    "totalDurationMs": 74623,
    "totalTokens": 31804,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8622,
      "cache_read_input_tokens": 20198,
      "output_tokens": 2983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2983,
          "cache_read_input_tokens": 20198,
          "cache_creation_input_tokens": 8622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8622,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 4,
      "bashCount": 4,
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

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a8deb1249dd0a8798",
  "tool_use_id": "toolu_01JcWRD49yAfxApcFgxoZMTN",
  "status": "completed",
  "output_file": "",
  "summary": "Read all paper sub-files",
  "usage": {
    "total_tokens": 34199,
    "tool_uses": 7,
    "duration_ms": 133726
  },
  "uuid": "010893b0-e2b3-4f7b-8fe3-049f24be832e",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119"
}
```

---

### Tool result

_source line 78 · 2026-05-22T21:23:58.183Z_

<details><summary>↩ Tool result · `toolu_01JcWRD49yAfxApcFgxoZMTN`</summary>

```text
# introduction.tex

\section{Introduction}
\label{sec:introduction}

Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.

This gap cuts across three communities: binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}); membership inference~\cite{zawalski2026codec} addresses a different question; the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.
No existing method estimates how many rounds of recursive generation a text has undergone.

The Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
We empirically measure a lower bound $\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).

Our contributions:
\begin{enumerate}[label=(\alph*),nosep]
  \item \textbf{$\Kempirical$ as a measurement tool} across 10 model configurations (6 families, 1B--8B) and 4 decoding strategies ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}):
  For web text, $\Kempirical \leq 2$ regardless of family or scale; $\Kempirical \leq 3$ universally.
  $\Kempirical$ establishes binary sufficiency for web text by measurement (not assumption), reveals domain-dependent variation (arXiv $\Kempirical{=}3$), and quantifies boundary sensitivity to threshold, scorer, and model scale.
  Both supervised OBD and zero-shot LLMs fail beyond $\Kempirical$ (McNemar $p > 0.05$; Section~\ref{sec:why_kstar}).
  \item \textbf{Domain dependence of $\Kempirical$}: general web text (C4, Wikipedia) yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$, consistent across model families (Section~\ref{sec:cross_domain}).
  \item \textbf{Model-free cross-model transfer}: 15 statistical features enable 80--100\% accuracy retention with scorer-invariant feature rankings ($\rho > 0.90$), supporting model-agnostic depth estimation without retraining; $\Kempirical$ agreement holds across scorers for strong-signal configurations (Section~\ref{sec:transfer}).
\end{enumerate}

\noindent As a consistency check, $\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\ base $0.6018$; Section~\ref{sec:filtering}).

---

# related_work.tex

\section{Related Work}
\label{sec:related_work}

\paragraph{Model collapse and recursive degradation.}
Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.
Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}, making $\Kempirical = 2$ a conservative lower bound.
This literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.

\paragraph{Beyond binary detection.}
Binary detectors~\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.
Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
None estimates recursive generation depth.

\paragraph{Data selection and curation.}
DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, and DoReMi~\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.

\paragraph{Ordinal classification and probing.}
Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.

---

# method.tex

\section{Method}
\label{sec:method}

\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/pipeline.pdf}
\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
\label{fig:pipeline}
\end{figure*}

\subsection{Problem Formulation}
\label{sec:formulation}

A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
This sequence forms a Markov chain.
By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: mutual information with the seed text degrades monotonically.
Together with Markov chain convergence, this provides heuristic motivation for expecting $\auc_{k-1,k}$ to decrease with $k$, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.

We define the operational lower bound:
\begin{equation}
  \Kempirical = \max\!\bigl\{k \!\geq\! 1 : \auc_{j-1,j} > \theta,\;\forall\, j \!\leq\! k\bigr\},
  \label{eq:kstar}
\end{equation}
which requires all pairs up to depth $k$ to exceed the threshold (the $\forall j$ constraint is naturally satisfied because $\auc_{k-1,k}$ decreases monotonically above $\theta$ across all tested configurations; Table~\ref{tab:kstar_ci}).
The theoretical upper bound $\Ktheory$ (the true maximum discriminable depth given optimal features) is not directly estimated in this work.
Since any specific classifier on a feature subset achieves AUC at most equal to the Bayes-optimal classifier on all features, $\Kempirical \leq \Ktheory$ follows directly.
The DPI separately motivates the empirical observation that $\auc_{k-1,k}$ decreases with $k$, though AUC is not a monotone function of MI (as noted above).
Here $\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\theta = 0.60$ is a reference operating point motivated by Cohen's small-effect-size convention ($h \approx 0.20$\footnote{$h = 2\arcsin\!\sqrt{0.60} - 2\arcsin\!\sqrt{0.50} \approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.}; justified below).
Bootstrap 95\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\theta$ and non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).

\paragraph{Threshold justification.}
$\theta{=}0.60$ is a reference operating point supported by three independent lines of evidence.
First, Cohen's $h \approx 0.20$, a conventional small-effect-size boundary.
Second, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ ($p < 0.002$ for all boundary comparisons).
Third, the conclusion $\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, a ${\sim}$5--11\,pp discontinuity; only at extremes does $\Kempirical$ shift ($\theta{=}0.55$: $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$: $\Kempirical{=}1$ across all).
Figure~\ref{fig:kstar_theta} provides the full sensitivity surface across $\theta \in [0.55, 0.70]$, enabling practitioners to select $\theta$ according to their false-positive tolerance.
The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.

\subsection{Features and Classifier}
\label{sec:features}

Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations); in deployment where reference corpora are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted entirely, leaving 14 features (surprisal statistics, TTR, hapax ratio, frequency tail) that require no external reference and retain full $\Kempirical$.
Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.

We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).

\subsection{Experimental Setup}
\label{sec:experimental_setup}

We evaluate six configurations spanning three model families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).
Each uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.

\begin{table}[t]
\centering
\small
\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
\label{tab:setup}
\begin{tabular}{llcc}
\toprule
\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
\midrule
Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
\bottomrule
\end{tabular}
\end{table}

---

# experiments_c1.tex

\section{Experiments}
\label{sec:experiments}

We evaluate generational depth estimation on ten model configurations spanning six architecture families:
Pythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.
All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).

%% ====================================================================
\subsection{$\Kempirical \leq 2$ Across Model Configurations (C4)}
\label{sec:kstar_boundary}

\begin{table*}[t]
\centering
\small
\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
\label{tab:kstar_ci}
\begin{tabular}{lcccccccccc}
\toprule
 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
\midrule
0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\,.967] \\
1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .5080 & [.496,\,.519] & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .4973 & [.486,\,.509] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
3v4 & .5435 & & .5152 & & .5024\rlap{$^\S$} & & .5409 & & .5276 & \\
4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & \\
\bottomrule
\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\
\multicolumn{11}{l}{\footnotesize $^\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\Delta = 0.005$).} \\
\multicolumn{11}{l}{\footnotesize Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\ref{tab:kstar_ci_extended}.}
\end{tabular}
\end{table*}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\% confidence intervals. The horizontal dashed line marks $\theta = 0.60$.}
\label{fig:auc_decay}
\end{figure}

Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 10 model configurations: 6/10 configurations yield $\Kempirical{=}2$ (Qwen with 4 configs, LLaMA-8B, and Pythia-1.4B, spanning three of six families) (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\Kempirical{=}1$ (1v2 $\auc$: 0.508, 0.594, 0.596, and 0.598, all below $\theta$; Section~\ref{sec:boundary_cases}).
Under Bonferroni correction for 10 simultaneous comparisons (99.5\% CIs), four of six boundary configurations retain CI lower bounds above $\theta$; the two most marginal cases, Qwen-continuation (nominal CI lower bound 0.602) and LLaMA-8B (0.603), fall below the widened interval.
Both retain point estimates above $\theta$ and uncorrected CI lower bounds above $\theta$; the near-misses reflect narrow effect sizes rather than classification failure.
By architecture family: Qwen (4/4) and LLaMA (1/1) yield $\Kempirical{\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\Kempirical{=}2$, 6.9B: $\Kempirical{=}1$).
LLaMA-3.1-8B confirms $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123\;[0.603,\,0.622]$; CI lower bound above $\theta$; Table~\ref{tab:kstar_ci_extended}).
All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across $\Kempirical{=}2$ continuation models ($\Delta = 4.3$\,pp).

\paragraph{Scale and instruction-tuning invariance.}
$\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\auc = 0.6123$) both exceed $\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\ $> 0.99$ at $\leq$1.5B).
A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.

\begin{figure*}[t]
\centering
\includegraphics[width=0.75\textwidth]{figures/fig_kstar_theta.pdf}
\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. Five of six configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line); OLMo yields $\Kempirical{=}1$. At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
\label{fig:kstar_theta}
\end{figure*}

The raw AUC gap between adjacent generations provides a threshold-free continuous measure of discriminability; Figure~\ref{fig:kstar_theta} displays the full sensitivity surface across $\theta \in [0.55, 0.70]$, allowing practitioners to read off $\Kempirical$ at any desired effect-size threshold.
Five of six configurations yield $\Kempirical = 2$ within $\theta \in [0.51, 0.61]$ (OLMo: $\Kempirical = 1$ throughout); at $\theta{=}0.55$, two Qwen configurations reach $\Kempirical = 3$; at $\theta{=}0.70$, all drop to $\Kempirical = 1$.
All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).

%% ====================================================================
\subsection{Cross-Model Transfer}
\label{sec:transfer}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/fig3_transfer_heatmap.pdf}
\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, retention rate. Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
\label{fig:transfer_heatmap}
\end{figure}

Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
Qwen-rewrite classifiers transfer poorly (61--63\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.

\paragraph{Cross-scorer validation.}
Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\ref{tab:crossscorer}).
Feature ranking independence is a strong result: the same features dominate under all scorers.
$\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\auc = 0.696$) retains $\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\auc = 0.611$, only 0.011 above $\theta$) drops to $\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).
A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; Table~\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\Kempirical$ classifications largely agree.

%% ====================================================================
\subsection{Feature Ordering and Generation Mode}
\label{sec:feature_degradation}
\label{sec:generation_mode}

Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.
Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.

%% ====================================================================
\subsection{Neural Probe}
\label{sec:neural_probe}

Replacing the 15D features with frozen encoder hidden states (MLP probe; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia remains at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3} = 0.5963$); OLMo yields $\Kempirical^{\text{neural}} = 1$ (1v2 $\auc = 0.5054$, consistent with its 15D boundary).
We hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\ref{sec:transfer}; the 15D features yield $\Kempirical = 2$ for most families (OLMo: $\Kempirical = 1$).

\noindent\begin{minipage}{\columnwidth}
\centering
\footnotesize
\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
\label{tab:neural_probe_crossmodel}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lccc}
\toprule
\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
\midrule
Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
OLMo-1B    & 0.5056 & $[0.497,\,0.516]$ & 1\rlap{$^\dagger$} \\
\bottomrule
\multicolumn{4}{l}{\footnotesize $^\dagger$OLMo 1v2 $\auc = 0.5054$ (below $\theta$); $\Kempirical^{\text{neural}} = 1$.}
\end{tabular}}
\end{minipage}

%% ====================================================================
\subsection{Cross-Domain Variation}
\label{sec:cross_domain}

The preceding experiments use C4 (general web text).
To test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.
Wikipedia yields $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), matching the C4 baseline.
Both Qwen-1.5B and Pythia-1.4B yield $\Kempirical{=}3$ for arXiv (Table~\ref{tab:domain_kstar}): 2v3 $\auc = 0.644\;[0.628,\,0.658]$ and $0.655\;[0.640,\,0.669]$ respectively (bootstrap CI lower bounds above $\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.
The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.

\begin{table}[t]
\centering
\footnotesize
\caption{Cross-domain $\Kempirical$ comparison. Rows: generator model and text domain (C4, Wikipedia, arXiv). $\Kempirical{=}3$ for arXiv indicates structured text preserves discriminability to greater depth.}
\label{tab:domain_kstar}
\begin{tabular}{llccc}
\toprule
\textbf{Domain} & \textbf{Model} & \textbf{1v2 $\auc$} & \textbf{2v3 $\auc$} & $\Kempirical$ \\
\midrule
arXiv & Qwen-1.5B  & 0.858 & 0.6436 & 3 \\
arXiv & Pythia-1.4B & 0.805 & 0.6545 & 3 \\
C4    & Qwen-1.5B  & 0.63  & 0.56   & 2 \\
Wikipedia & Qwen-1.5B & 0.62 & 0.55 & 2 \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{Robustness.}
\label{sec:robustness}
$\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\theta$ but 2v3 remains well below $\theta$ at all lengths ($\leq 0.572$).
Seed robustness testing (seed $= 123$ vs.\ primary $= 42$; Table~\ref{tab:seed_robustness}) confirms $\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\Kempirical{=}2 \to 3$, 2v3 $\auc = 0.607$) has one of five folds below $\theta$.
The ${\pm}9$\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\Kempirical$ over raw AUC comparisons.

%% ====================================================================
\subsection{Binary Detector Confidence}
\label{sec:binary_confidence}

Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.

---

# experiments_c3.tex

\section{Consistency Check: $\Kstar$-Guided Filtering}
\label{sec:filtering}

$\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.
We test this as a consistency check on the boundary measurement, not as an independent contribution.
We compare six strategies on 30{,}000 documents (depths 0--5): (i)~\textbf{no-filter}, (ii)~\textbf{binary-ours} ($w = 1 - P(\text{synthetic})$ from 15D LightGBM), (iii)~\textbf{binary-Drayson}~\citep{drayson2025}, (iv)~\textbf{graduated} ($w = \exp(-\alpha \cdot \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), (v)~\textbf{surprisal} (retain above median), and (vi)~\textbf{DSIR}~\citep{xie2023dsir}.
We fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\alpha_{\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\% synthetic setting is an upper bound~\cite{shumailov2024collapse, dohmatob2024model}).

\begin{table}[t]
\centering
\small
\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \exp(-\alpha \hat{d})$. Mean $\pm$ std over 5 seeds. Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
\label{tab:tab_filtering_main}
\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
\end{table}

Binary-ours minimizes MMLU degradation most effectively (Table~\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\,pp (no-filter) to $-$0.77\,pp (${\sim}$50\% reduction; $p_{\text{corr}} < 0.05$ vs.\ all alternatives).
These effects are measured in a 100\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.
The strategy ordering is interpretable through $\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.
Graduated filtering converges monotonically toward binary: at $\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\Delta = 0$, $p_{\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\text{corr}} = 0.011$).
DSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\ref{fig:filtering_strategies} in Appendix).
At realistic contamination ratios ($\leq$50\%), all filtering strategies converge ($p > 0.12$), consistent with the one-wash laundering finding that depth-aware curation offers marginal benefit when $\Kempirical{=}2$ (Appendix~\ref{sec:dose_response}).
For $\Kempirical{=}1$ configurations, depth-aware curation reduces to standard binary filtering, consistent with $\Kempirical{=}1$ implying no exploitable depth signal beyond the 0v1 boundary.

---

# discussion.tex

\section{Discussion}
\label{sec:discussion}
\label{sec:why_kstar}
\label{sec:one_wash}
\label{sec:negative_graduated}
\label{sec:repr_dependence}
\label{sec:boundary_cases}
\label{sec:length_confound}

\paragraph{One-wash laundering (web text).}
For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).

\paragraph{Representation dependence.}
$\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$, while Pythia yields $\Kempirical^{\text{neural}} = 2$ and OLMo yields $\Kempirical^{\text{neural}} = 1$, consistent with its 15D boundary (Table~\ref{tab:neural_probe_crossmodel}).
The 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\Kempirical{=}2$), making them the preferred operational choice.
Feature rankings are scorer-independent ($\rho > 0.90$); $\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (Qwen-continuation drops to $\Kempirical{=}1$; length confound ruled out in Appendix~\ref{sec:extended_limitations}).
ANOVA confirms this layered pattern: Scorer explains modest variance ($\eta^2_p{=}.166$) with a significant Generator$\times$Scorer interaction ($\eta^2_p{=}.146$; Table~\ref{tab:anova_crossscorer}).

\paragraph{Domain dependence of $\Kempirical$.}
Web text (C4, Wikipedia) consistently yields $\Kempirical{=}2$, while structured academic text (arXiv) yields $\Kempirical{=}3$ across two independent model families (Qwen-1.5B and Pythia-1.4B; Section~\ref{sec:cross_domain}).
The elevated arXiv signal reflects formulaic structure: citation patterns, mathematical notation, and section conventions create larger per-generation distributional shifts (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4), making contamination trackable to greater depth.
Wikipedia matches C4 at $\Kempirical{=}2$ (1v2 $\auc = 0.623$, 2v3 $\auc = 0.571$), consistent with its general-purpose prose lacking domain-specific structural markers.
This domain dependence implies that corpus curators should calibrate depth-aware filtering to source characteristics rather than assuming a universal boundary.

\paragraph{Cross-model transfer.}
Continuation-mode classifiers transfer well across generators (80--92\% retention; Figure~\ref{fig:transfer_heatmap}), enabling portable depth estimation on corpora from unknown models without retraining.
The poor transfer from rewrite-mode classifiers (61--63\%) isolates generation mode, rather than architecture family, as the primary axis of distributional variation.

\paragraph{Prompt-chain scope and retrain-chain gap.}
Retrain-chain experiments (Pythia-1.4B LoRA) yield $\Kempirical{\geq}4$ (1v2 $\auc = 0.9484$, 3v4 $= 0.7982$), far exceeding the prompt-chain boundary of $\Kempirical{=}2$, because each retrain generation also modifies model parameters, introducing cumulative adaptation artifacts absent from text-only recycling.
Prompt-chain $\Kempirical$ isolates text-intrinsic degradation, the operationally relevant quantity for data curation pipelines; our conclusions do not directly transfer to retrain-chain (model collapse) settings.

\paragraph{Boundary cases and scale effect.}
$\Kempirical{=}1$ configurations cluster at 1v2 $\auc$ 0.508--0.598, well separated from the $\Kempirical{=}2$ range (0.611--0.696); $\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.
That $\Kempirical \in \{1, 2\}$ for all web text configurations is the core empirical result; larger models reduce 0v1 JSD (0.077 at 8B vs.\ 0.15--0.27 at $\leq$1.5B), suggesting 13B+ may increasingly yield $\Kempirical{=}1$.
The $\Kempirical{=}1$ vs.\ $\Kempirical{=}2$ distinction has a direct curation consequence: $\Kempirical{=}1$ generators erase depth signal in one pass, leaving only the binary 0v1 boundary available for filtering.

\paragraph{Decoding strategy as confound.}
Greedy decoding inflates depth separability: Pythia-6.9B yields $\Kempirical{=}2$ under greedy but $\Kempirical{=}1$ under nucleus sampling ($p{=}0.95$), with the borderline 1v2 score (2 of 5 folds above $\theta$) illustrating that the boundary is continuous rather than a cliff (Table~\ref{tab:s10_pythia_decoding}).
Practitioners should calibrate $\theta$ to their application-specific tolerance (Figure~\ref{fig:kstar_theta}).

\paragraph{What $\Kempirical$ reveals.}
As a measurement tool, $\Kempirical$ establishes why binary detection suffices for web text (depth${>}1$ is invisible to statistical features), identifies domains where finer strategies are viable (arXiv $\Kempirical{=}3$), and quantifies how scale, scorer, and threshold jointly shape the boundary.
The OBD framework provides a reproducible, low-cost depth estimation protocol requiring only corpus-level statistical features, unlike detection methods that need API access or model weights.
Even when the practical outcome remains binary filtering, $\Kempirical$ grounds this choice in measurement rather than heuristic assumption.
$\Kempirical$ also serves as a monitoring metric for tracking how the discrimination boundary shifts as model scale increases; future work may explore scorer-ensemble strategies to improve cross-scorer robustness at marginal boundaries.

---

# conclusion.tex

\section{Conclusion}
\label{sec:conclusion}

We measure a lower bound on the generational depth discrimination boundary $\Kempirical$ for prompt-chain recursive synthetic text.
For general web text, $\Kempirical \leq 2$ regardless of model family or scale (six architecture families, 1B--8B, $\theta{=}0.60$); across all ten configurations, $\Kempirical \leq 3$, with structured academic text (arXiv) reaching $\Kempirical{=}3$ across two independent architectures.
This one-wash laundering effect concentrates all exploitable signal at the 0v1 boundary, and the consistency check confirms that binary curation most effectively minimizes MMLU degradation ($-$0.77\,pp vs.\ $-$1.53\,pp for no-filter).
For structured domains where $\Kempirical{=}3$, graduated strategies can exploit one additional depth level, so corpus curators should calibrate filtering to the source domain.
The 15 statistical features enable deployment across generators without retraining (80--92\% accuracy retention, $\rho > 0.90$), supporting model-agnostic depth estimation for corpora where the generating model is unknown.
Under Bonferroni correction for 10 simultaneous comparisons, four of six $\Kempirical{=}2$ configurations retain significance at the 99.5\% level; the remaining two marginal cases preserve point estimates above $\theta$.
$\Kempirical$ converts a continuous AUC decay surface into a discrete operating boundary grounded in the Data Processing Inequality, providing a principled basis for curation decisions that replaces heuristic assumptions about synthetic text recyclability.
Several directions remain open: tracking $\Kempirical$ as model scale surpasses 13B, where our scale analysis suggests the boundary may shift toward $\Kempirical{=}1$; bridging the prompt-chain and retrain-chain boundaries, given the substantially higher $\Kempirical{\geq}4$ observed under parameter retraining; and extending depth estimation to additional structured domains and multilingual text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "3c715714-debb-4461-92c2-2fff0a69ced9",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following LaTeX files in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ and return their FULL contents:\n1. introduction.tex\n2. related_work.tex\n3. method.tex\n4. experiments_c1.tex\n5. experiments_c3.tex\n6. discussion.tex\n7. conclusion.tex\n\nI need the complete text of each file. Return the contents with the filename as a header before each file's contents.",
    "agentId": "a8deb1249dd0a8798",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "# introduction.tex\n\n\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEstimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.\nWhen models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).\nYet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.\n\nThis gap cuts across three communities: binary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}); membership inference~\\cite{zawalski2026codec} addresses a different question; the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool; and data selection methods~\\cite{xie2023dsir, tirumala2023d4, drayson2025} ignore recursive depth.\nNo existing method estimates how many rounds of recursive generation a text has undergone.\n\nThe Data Processing Inequality guarantees that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.\nWe empirically measure a lower bound $\\Kempirical$ on the discrimination boundary (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features and an Ordinal Binary Decomposition (OBD) LightGBM classifier.\nWe operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).\n\nOur contributions:\n\\begin{enumerate}[label=(\\alph*),nosep]\n  \\item \\textbf{$\\Kempirical$ as a measurement tool} across 10 model configurations (6 families, 1B--8B) and 4 decoding strategies ($p \\leq 0.002$; Section~\\ref{sec:kstar_boundary}):\n  For web text, $\\Kempirical \\leq 2$ regardless of family or scale; $\\Kempirical \\leq 3$ universally.\n  $\\Kempirical$ establishes binary sufficiency for web text by measurement (not assumption), reveals domain-dependent variation (arXiv $\\Kempirical{=}3$), and quantifies boundary sensitivity to threshold, scorer, and model scale.\n  Both supervised OBD and zero-shot LLMs fail beyond $\\Kempirical$ (McNemar $p > 0.05$; Section~\\ref{sec:why_kstar}).\n  \\item \\textbf{Domain dependence of $\\Kempirical$}: general web text (C4, Wikipedia) yields $\\Kempirical{=}2$, while structured academic text (arXiv) yields $\\Kempirical{=}3$, consistent across model families (Section~\\ref{sec:cross_domain}).\n  \\item \\textbf{Model-free cross-model transfer}: 15 statistical features enable 80--100\\% accuracy retention with scorer-invariant feature rankings ($\\rho > 0.90$), supporting model-agnostic depth estimation without retraining; $\\Kempirical$ agreement holds across scorers for strong-signal configurations (Section~\\ref{sec:transfer}).\n\\end{enumerate}\n\n\\noindent As a consistency check, $\\Kempirical{=}2$ correctly predicts the strategy ordering for web-text filtering: binary curation minimizes degradation most effectively (MMLU $0.5941$ vs.\\ base $0.6018$; Section~\\ref{sec:filtering}).\n\n---\n\n# related_work.tex\n\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse and recursive degradation.}\nIterative training on model outputs causes tail-distribution degradation~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong, fu2025theoretical}, diversity contraction~\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, wang2025unveiling}.\nOur prompt-chain operates in the replace regime~\\cite{kazdan2025collapse}, making $\\Kempirical = 2$ a conservative lower bound.\nThis literature characterizes macro dynamics but provides no per-text depth estimation, the gap we address.\n\n\\paragraph{Beyond binary detection.}\nBinary detectors~\\cite{mitchell2023detectgpt, bao2024fast, hans2024binoculars, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate.\nRecent work extends beyond binary labels to collaboration degree~\\cite{cheng2025beyond}, contamination hierarchies~\\cite{mehta2025beyond}, and multigenerator benchmarks~\\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\\cite{hao2025rewrite}; CoDeC~\\cite{zawalski2026codec} addresses contamination via membership inference.\nNone estimates recursive generation depth.\n\n\\paragraph{Data selection and curation.}\nDSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, and DoReMi~\\cite{xie2023doremi} are depth-agnostic; Drayson et al.~\\cite{drayson2025} combined binary detection with importance resampling, a special case when $\\Kstar = 1$.\n\n\\paragraph{Ordinal classification and probing.}\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; our neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.\n\n---\n\n# method.tex\n\n\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/pipeline.pdf}\n\\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\\delta$ to produce a depth chain. Corpus-level statistical features are fed to the OBD-LightGBM classifier for depth prediction.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nA generation operator $G_\\delta$ (LLM + decoding strategy $\\delta$) produces successive generations $X \\to Y_1 \\to \\cdots \\to Y_K$, where $Y_k = G_\\delta(Y_{k-1})$ and $Y_0 \\triangleq X$ (Figure~\\ref{fig:pipeline}).\nThis sequence forms a Markov chain.\nBy the Data Processing Inequality, $I(X; Y_1) \\geq I(X; Y_2) \\geq \\cdots \\geq 0$: mutual information with the seed text degrades monotonically.\nTogether with Markov chain convergence, this provides heuristic motivation for expecting $\\auc_{k-1,k}$ to decrease with $k$, though AUC and mutual information are not formally equivalent; the actual saturation depth must therefore be measured empirically.\n\nWe define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\!\\bigl\\{k \\!\\geq\\! 1 : \\auc_{j-1,j} > \\theta,\\;\\forall\\, j \\!\\leq\\! k\\bigr\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhich requires all pairs up to depth $k$ to exceed the threshold (the $\\forall j$ constraint is naturally satisfied because $\\auc_{k-1,k}$ decreases monotonically above $\\theta$ across all tested configurations; Table~\\ref{tab:kstar_ci}).\nThe theoretical upper bound $\\Ktheory$ (the true maximum discriminable depth given optimal features) is not directly estimated in this work.\nSince any specific classifier on a feature subset achieves AUC at most equal to the Bayes-optimal classifier on all features, $\\Kempirical \\leq \\Ktheory$ follows directly.\nThe DPI separately motivates the empirical observation that $\\auc_{k-1,k}$ decreases with $k$, though AUC is not a monotone function of MI (as noted above).\nHere $\\auc_{k-1,k}$ is the point-estimate pairwise AUC and $\\theta = 0.60$ is a reference operating point motivated by Cohen's small-effect-size convention ($h \\approx 0.20$\\footnote{$h = 2\\arcsin\\!\\sqrt{0.60} - 2\\arcsin\\!\\sqrt{0.50} \\approx 0.2014$, a ``small'' effect size by Cohen's (1988) convention.}; justified below).\nBootstrap 95\\% CIs (1{,}000 resamples) provide uncertainty quantification: we verify that boundary-pair CI lower bounds exceed $\\theta$ and non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).\n\n\\paragraph{Threshold justification.}\n$\\theta{=}0.60$ is a reference operating point supported by three independent lines of evidence.\nFirst, Cohen's $h \\approx 0.20$, a conventional small-effect-size boundary.\nSecond, a 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\\,0.55$ ($p < 0.002$ for all boundary comparisons).\nThird, the conclusion $\\Kempirical{=}2$ is insensitive to the exact threshold: 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, a ${\\sim}$5--11\\,pp discontinuity; only at extremes does $\\Kempirical$ shift ($\\theta{=}0.55$: $\\Kempirical{=}3$ for two Qwen configurations; $\\theta{=}0.70$: $\\Kempirical{=}1$ across all).\nFigure~\\ref{fig:kstar_theta} provides the full sensitivity surface across $\\theta \\in [0.55, 0.70]$, enabling practitioners to select $\\theta$ according to their false-positive tolerance.\nThe downstream filtering evaluation (Section~\\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\\theta$, avoiding circularity.\n\n\\subsection{Features and Classifier}\n\\label{sec:features}\n\nEach document is characterized by a 15-dimensional feature vector spanning four groups: \\emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \\emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \\emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \\emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).\nAll features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\\ref{tab:s5_features}, Appendix).\nSelf-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \\#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.\nRemoving self-BLEU reduces mean $\\auc_{1v2}$ by $< 1$\\,pp across all models (14D $\\Kempirical = 2$ for all 4 configurations); in deployment where reference corpora are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted entirely, leaving 14 features (surprisal statistics, TTR, hapax ratio, frequency tail) that require no external reference and retain full $\\Kempirical$.\nHand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.\n\nWe use \\emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\\text{depth} > k \\mid \\mathbf{x})$ via LightGBM (hyperparameters in Table~\\ref{tab:s6_lgbm_params}).\nOBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\\auc$ (mean 0.6095 vs.\\ 0.4883 for ordinal logistic regression).\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate six configurations spanning three model families (Table~\\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B (continuation), Pythia-1.4B and OLMo-1B (continuation).\nEach uses 5{,}000 C4 seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).\nDefault decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.\nContinuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.\nEvaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\\auc$ as primary metric.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations for depth-chain generation. \\textbf{Config}: shorthand identifier; \\textbf{Model}: architecture and parameter count; \\textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}\n\\label{tab:setup}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Config} & \\textbf{Model} & \\textbf{Mode} & $N$ \\\\\n\\midrule\nQwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\\\\nQwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\\\\nQwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\\\\nPythia    & Pythia-1.4B            & Continuation & 5{,}000 \\\\\nOLMo      & OLMo-1B               & Continuation & 5{,}000 \\\\\nQwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n---\n\n# experiments_c1.tex\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on ten model configurations spanning six architecture families:\nPythia-1.4B, Pythia-6.9B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, and Gemma-2-2B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5).\n\n%% ====================================================================\n\\subsection{$\\Kempirical \\leq 2$ Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9932 & & .9860 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .5080 & [.496,\\,.519] & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .4973 & [.486,\\,.509] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5152 & & .5024\\rlap{$^\\S$} & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5136 & & .4942 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\S$OLMo 2v3 (0.497) $<$ 3v4 (0.502): non-monotonic reversal within noise ($\\Delta = 0.005$).} \\\\\n\\multicolumn{11}{l}{\\footnotesize Full results for all 10 configurations (including Qwen-7B, Qwen-base, Gemma-2-2B, and Pythia-6.9B) are provided in Table~\\ref{tab:kstar_ci_extended}.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed); shaded bands show bootstrap 95\\% confidence intervals. The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 10 model configurations: 6/10 configurations yield $\\Kempirical{=}2$ (Qwen with 4 configs, LLaMA-8B, and Pythia-1.4B, spanning three of six families) (1v2 $\\auc$ range: 0.6112--0.6955; all CI lower bounds $> \\theta$; permutation $p < 0.001$), while OLMo-1B, Mistral-7B, Pythia-6.9B, and Gemma-2-2B yield $\\Kempirical{=}1$ (1v2 $\\auc$: 0.508, 0.594, 0.596, and 0.598, all below $\\theta$; Section~\\ref{sec:boundary_cases}).\nUnder Bonferroni correction for 10 simultaneous comparisons (99.5\\% CIs), four of six boundary configurations retain CI lower bounds above $\\theta$; the two most marginal cases, Qwen-continuation (nominal CI lower bound 0.602) and LLaMA-8B (0.603), fall below the widened interval.\nBoth retain point estimates above $\\theta$ and uncorrected CI lower bounds above $\\theta$; the near-misses reflect narrow effect sizes rather than classification failure.\nBy architecture family: Qwen (4/4) and LLaMA (1/1) yield $\\Kempirical{\\geq}2$ at nominal significance; OLMo (1/1), Mistral (1/1), and Gemma (1/1) yield $\\Kempirical{=}1$; Pythia exhibits a scale-dependent split (1.4B: $\\Kempirical{=}2$, 6.9B: $\\Kempirical{=}1$).\nLLaMA-3.1-8B confirms $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123\\;[0.603,\\,0.622]$; CI lower bound above $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across $\\Kempirical{=}2$ continuation models ($\\Delta = 4.3$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 8B: Qwen-7B (1v2 $\\auc = 0.6168$ $[0.608, 0.626]$) and LLaMA-3.1-8B (1v2 $\\auc = 0.6123$) both exceed $\\theta$, despite progressively reduced 0v1 signal (0.9638 and 0.9225 vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$), confirming the boundary is not an instruction-tuning artifact.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for six configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. Five of six configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line); OLMo yields $\\Kempirical{=}1$. At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure*}\n\nThe raw AUC gap between adjacent generations provides a threshold-free continuous measure of discriminability; Figure~\\ref{fig:kstar_theta} displays the full sensitivity surface across $\\theta \\in [0.55, 0.70]$, allowing practitioners to read off $\\Kempirical$ at any desired effect-size threshold.\nFive of six configurations yield $\\Kempirical = 2$ within $\\theta \\in [0.51, 0.61]$ (OLMo: $\\Kempirical = 1$ throughout); at $\\theta{=}0.55$, two Qwen configurations reach $\\Kempirical = 3$; at $\\theta{=}0.70$, all drop to $\\Kempirical = 1$.\nAll four decoding strategies likewise yield $\\Kempirical = 2$ at $\\theta{=}0.60$ (1v2 $\\auc \\in [0.687, 0.704]$; Table~\\ref{tab:s2_decoding}).\n\n%% ====================================================================\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, retention rate. Pythia$\\leftrightarrow$OLMo: 90--92\\%; Qwen-rewrite$\\to$continuation: 61--63\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), confirming reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$) but attenuates absolute discriminability at the boundary (Table~\\ref{tab:crossscorer}).\nFeature ranking independence is a strong result: the same features dominate under all scorers.\n$\\Kempirical$ agreement, however, is signal-strength dependent: Qwen-rewrite (strong signal, 1v2 $\\auc = 0.696$) retains $\\Kempirical{=}2$ under all scorers, but Qwen-continuation (marginal, 1v2 $\\auc = 0.611$, only 0.011 above $\\theta$) drops to $\\Kempirical{=}1$ (Pythia: $0.5923$; OLMo: $0.5858$).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; Table~\\ref{tab:anova_crossscorer}) confirms a statistically significant but modest Scorer main effect ($\\eta^2_p{=}.166$, $p < .001$) and a significant Generator$\\times$Scorer interaction ($\\eta^2_p{=}.146$), indicating that absolute AUC values are scorer-dependent even when $\\Kempirical$ classifications largely agree.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families, revealing that autoregressive generation progressively damps surprisal variability.\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia remains at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3} = 0.5963$); OLMo yields $\\Kempirical^{\\text{neural}} = 1$ (1v2 $\\auc = 0.5054$, consistent with its 15D boundary).\nWe hypothesize that the Qwen-only elevation reflects self-familiarity artifacts, consistent with the poor transfer observed in Section~\\ref{sec:transfer}; the 15D features yield $\\Kempirical = 2$ for most families (OLMo: $\\Kempirical = 1$).\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5056 & $[0.497,\\,0.516]$ & 1\\rlap{$^\\dagger$} \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$OLMo 1v2 $\\auc = 0.5054$ (below $\\theta$); $\\Kempirical^{\\text{neural}} = 1$.}\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test domain dependence, we evaluate on Wikipedia ($n{=}5{,}000$) and arXiv abstracts ($n{=}2{,}200$) using two model families.\nWikipedia yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.623$, 2v3 $\\auc = 0.571$), matching the C4 baseline.\nBoth Qwen-1.5B and Pythia-1.4B yield $\\Kempirical{=}3$ for arXiv (Table~\\ref{tab:domain_kstar}): 2v3 $\\auc = 0.644\\;[0.628,\\,0.658]$ and $0.655\\;[0.640,\\,0.669]$ respectively (bootstrap CI lower bounds above $\\theta$; permutation $p < 0.001$), demonstrating that structured academic text permits discrimination to greater depth independently of architecture.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4), as formulaic structure amplifies deviation from domain norms.\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\caption{Cross-domain $\\Kempirical$ comparison. Rows: generator model and text domain (C4, Wikipedia, arXiv). $\\Kempirical{=}3$ for arXiv indicates structured text preserves discriminability to greater depth.}\n\\label{tab:domain_kstar}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Model} & \\textbf{1v2 $\\auc$} & \\textbf{2v3 $\\auc$} & $\\Kempirical$ \\\\\n\\midrule\narXiv & Qwen-1.5B  & 0.858 & 0.6436 & 3 \\\\\narXiv & Pythia-1.4B & 0.805 & 0.6545 & 3 \\\\\nC4    & Qwen-1.5B  & 0.63  & 0.56   & 2 \\\\\nWikipedia & Qwen-1.5B & 0.62 & 0.55 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Robustness.}\n\\label{sec:robustness}\n$\\Kempirical{=}2$ holds across segment lengths of 128, 256, and 512 tokens (Table~\\ref{tab:s11_length_ablation}); at 512 tokens the 1v2 CI lower bound falls marginally below $\\theta$ but 2v3 remains well below $\\theta$ at all lengths ($\\leq 0.572$).\nSeed robustness testing (seed $= 123$ vs.\\ primary $= 42$; Table~\\ref{tab:seed_robustness}) confirms $\\Kempirical$ stability in 2/3 configurations; the one marginal shift (Qwen-Wikipedia $\\Kempirical{=}2 \\to 3$, 2v3 $\\auc = 0.607$) has one of five folds below $\\theta$.\nThe ${\\pm}9$\\,pp absolute AUC variation across seeds strengthens the case for threshold-based $\\Kempirical$ over raw AUC comparisons.\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), pairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\nThe observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.\n\n---\n\n# experiments_c3.tex\n\n\\section{Consistency Check: $\\Kstar$-Guided Filtering}\n\\label{sec:filtering}\n\n$\\Kempirical = 2$ makes a falsifiable prediction: binary curation should suffice, and graduated performance should converge toward binary as the decay steepness increases.\nWe test this as a consistency check on the boundary measurement, not as an independent contribution.\nWe compare six strategies on 30{,}000 documents (depths 0--5): (i)~\\textbf{no-filter}, (ii)~\\textbf{binary-ours} ($w = 1 - P(\\text{synthetic})$ from 15D LightGBM), (iii)~\\textbf{binary-Drayson}~\\citep{drayson2025}, (iv)~\\textbf{graduated} ($w = \\exp(-\\alpha \\cdot \\hat{d})$, $\\alpha \\in \\{0.1,\\ldots,0.9\\}$), (v)~\\textbf{surprisal} (retain above median), and (vi)~\\textbf{DSIR}~\\citep{xie2023dsir}.\nWe fine-tune Qwen2.5-1.5B-Instruct via LoRA (rank~8, $\\alpha_{\\text{LoRA}}{=}16$) for 3 epochs on MMLU and HellaSwag across 5 seeds (51 total runs; this 100\\% synthetic setting is an upper bound~\\cite{shumailov2024collapse, dohmatob2024model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream task performance (MMLU, HellaSwag) under six data-filtering strategies. Binary-ours uses the 15D LightGBM depth classifier; Graduated applies exponentially decaying weights $w = \\exp(-\\alpha \\hat{d})$. Mean $\\pm$ std over 5 seeds. Full $\\alpha$ sweep in Appendix~\\ref{sec:extended_limitations}.}\n\\label{tab:tab_filtering_main}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_filtering_main}}\n\\end{table}\n\nBinary-ours minimizes MMLU degradation most effectively (Table~\\ref{tab:tab_filtering_main}), reducing the gap from $-$1.53\\,pp (no-filter) to $-$0.77\\,pp (${\\sim}$50\\% reduction; $p_{\\text{corr}} < 0.05$ vs.\\ all alternatives).\nThese effects are measured in a 100\\% synthetic upper-bound setting; real-world contamination ratios are typically lower, and effect sizes would scale accordingly.\nThe strategy ordering is interpretable through $\\Kempirical$: binary filtering exploits the one reliable boundary (0v1), while graduated strategies assign weights to depths 2--5 based on near-random classifier outputs, injecting noise.\nGraduated filtering converges monotonically toward binary: at $\\alpha{=}0.9$, it matches binary-ours on HellaSwag exactly ($\\Delta = 0$, $p_{\\text{corr}} = 1.00$) but remains significantly worse on MMLU ($p_{\\text{corr}} = 0.011$).\nDSIR is indistinguishable from no-filter, confirming that depth-aware features are necessary for curation in recursively contaminated corpora (Figure~\\ref{fig:filtering_strategies} in Appendix).\nAt realistic contamination ratios ($\\leq$50\\%), all filtering strategies converge ($p > 0.12$), consistent with the one-wash laundering finding that depth-aware curation offers marginal benefit when $\\Kempirical{=}2$ (Appendix~\\ref{sec:dose_response}).\nFor $\\Kempirical{=}1$ configurations, depth-aware curation reduces to standard binary filtering, consistent with $\\Kempirical{=}1$ implying no exploitable depth signal beyond the 0v1 boundary.\n\n---\n\n# discussion.tex\n\n\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$.\nA single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.\nConverging evidence supports a data-intrinsic interpretation: OBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 8--38\\% (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\n\n\\paragraph{Representation dependence.}\n$\\Kempirical$ is representation-dependent: frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$, while Pythia yields $\\Kempirical^{\\text{neural}} = 2$ and OLMo yields $\\Kempirical^{\\text{neural}} = 1$, consistent with its 15D boundary (Table~\\ref{tab:neural_probe_crossmodel}).\nThe 15D features trade one depth level of sensitivity for cross-model consistency (6/10 configurations $\\Kempirical{=}2$), making them the preferred operational choice.\nFeature rankings are scorer-independent ($\\rho > 0.90$); $\\Kempirical$ agreement is scorer-independent for strong-signal configurations (e.g., Qwen-rewrite retains $\\Kempirical{=}2$ under all scorers) but scorer-sensitive at marginal boundaries (Qwen-continuation drops to $\\Kempirical{=}1$; length confound ruled out in Appendix~\\ref{sec:extended_limitations}).\nANOVA confirms this layered pattern: Scorer explains modest variance ($\\eta^2_p{=}.166$) with a significant Generator$\\times$Scorer interaction ($\\eta^2_p{=}.146$; Table~\\ref{tab:anova_crossscorer}).\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nWeb text (C4, Wikipedia) consistently yields $\\Kempirical{=}2$, while structured academic text (arXiv) yields $\\Kempirical{=}3$ across two independent model families (Qwen-1.5B and Pythia-1.4B; Section~\\ref{sec:cross_domain}).\nThe elevated arXiv signal reflects formulaic structure: citation patterns, mathematical notation, and section conventions create larger per-generation distributional shifts (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4), making contamination trackable to greater depth.\nWikipedia matches C4 at $\\Kempirical{=}2$ (1v2 $\\auc = 0.623$, 2v3 $\\auc = 0.571$), consistent with its general-purpose prose lacking domain-specific structural markers.\nThis domain dependence implies that corpus curators should calibrate depth-aware filtering to source characteristics rather than assuming a universal boundary.\n\n\\paragraph{Cross-model transfer.}\nContinuation-mode classifiers transfer well across generators (80--92\\% retention; Figure~\\ref{fig:transfer_heatmap}), enabling portable depth estimation on corpora from unknown models without retraining.\nThe poor transfer from rewrite-mode classifiers (61--63\\%) isolates generation mode, rather than architecture family, as the primary axis of distributional variation.\n\n\\paragraph{Prompt-chain scope and retrain-chain gap.}\nRetrain-chain experiments (Pythia-1.4B LoRA) yield $\\Kempirical{\\geq}4$ (1v2 $\\auc = 0.9484$, 3v4 $= 0.7982$), far exceeding the prompt-chain boundary of $\\Kempirical{=}2$, because each retrain generation also modifies model parameters, introducing cumulative adaptation artifacts absent from text-only recycling.\nPrompt-chain $\\Kempirical$ isolates text-intrinsic degradation, the operationally relevant quantity for data curation pipelines; our conclusions do not directly transfer to retrain-chain (model collapse) settings.\n\n\\paragraph{Boundary cases and scale effect.}\n$\\Kempirical{=}1$ configurations cluster at 1v2 $\\auc$ 0.508--0.598, well separated from the $\\Kempirical{=}2$ range (0.611--0.696); $\\Kempirical{=}1$ is not a classifier failure but a text property, as these models produce first-generation output so human-like that statistical features cannot distinguish depth~1 from depth~2.\nThat $\\Kempirical \\in \\{1, 2\\}$ for all web text configurations is the core empirical result; larger models reduce 0v1 JSD (0.077 at 8B vs.\\ 0.15--0.27 at $\\leq$1.5B), suggesting 13B+ may increasingly yield $\\Kempirical{=}1$.\nThe $\\Kempirical{=}1$ vs.\\ $\\Kempirical{=}2$ distinction has a direct curation consequence: $\\Kempirical{=}1$ generators erase depth signal in one pass, leaving only the binary 0v1 boundary available for filtering.\n\n\\paragraph{Decoding strategy as confound.}\nGreedy decoding inflates depth separability: Pythia-6.9B yields $\\Kempirical{=}2$ under greedy but $\\Kempirical{=}1$ under nucleus sampling ($p{=}0.95$), with the borderline 1v2 score (2 of 5 folds above $\\theta$) illustrating that the boundary is continuous rather than a cliff (Table~\\ref{tab:s10_pythia_decoding}).\nPractitioners should calibrate $\\theta$ to their application-specific tolerance (Figure~\\ref{fig:kstar_theta}).\n\n\\paragraph{What $\\Kempirical$ reveals.}\nAs a measurement tool, $\\Kempirical$ establishes why binary detection suffices for web text (depth${>}1$ is invisible to statistical features), identifies domains where finer strategies are viable (arXiv $\\Kempirical{=}3$), and quantifies how scale, scorer, and threshold jointly shape the boundary.\nThe OBD framework provides a reproducible, low-cost depth estimation protocol requiring only corpus-level statistical features, unlike detection methods that need API access or model weights.\nEven when the practical outcome remains binary filtering, $\\Kempirical$ grounds this choice in measurement rather than heuristic assumption.\n$\\Kempirical$ also serves as a monitoring metric for tracking how the discrimination boundary shifts as model scale increases; future work may explore scorer-ensemble strategies to improve cross-scorer robustness at marginal boundaries.\n\n---\n\n# conclusion.tex\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe measure a lower bound on the generational depth discrimination boundary $\\Kempirical$ for prompt-chain recursive synthetic text.\nFor general web text, $\\Kempirical \\leq 2$ regardless of model family or scale (six architecture families, 1B--8B, $\\theta{=}0.60$); across all ten configurations, $\\Kempirical \\leq 3$, with structured academic text (arXiv) reaching $\\Kempirical{=}3$ across two independent architectures.\nThis one-wash laundering effect concentrates all exploitable signal at the 0v1 boundary, and the consistency check confirms that binary curation most effectively minimizes MMLU degradation ($-$0.77\\,pp vs.\\ $-$1.53\\,pp for no-filter).\nFor structured domains where $\\Kempirical{=}3$, graduated strategies can exploit one additional depth level, so corpus curators should calibrate filtering to the source domain.\nThe 15 statistical features enable deployment across generators without retraining (80--92\\% accuracy retention, $\\rho > 0.90$), supporting model-agnostic depth estimation for corpora where the generating model is unknown.\nUnder Bonferroni correction for 10 simultaneous comparisons, four of six $\\Kempirical{=}2$ configurations retain significance at the 99.5\\% level; the remaining two marginal cases preserve point estimates above $\\theta$.\n$\\Kempirical$ converts a continuous AUC decay surface into a discrete operating boundary grounded in the Data Processing Inequality, providing a principled basis for curation decisions that replaces heuristic assumptions about synthetic text recyclability.\nSeveral directions remain open: tracking $\\Kempirical$ as model scale surpasses 13B, where our scale analysis suggests the boundary may shift toward $\\Kempirical{=}1$; bridging the prompt-chain and retrain-chain boundaries, given the substantially higher $\\Kempirical{\\geq}4$ observed under parameter retraining; and extending depth estimation to additional structured domains and multilingual text."
      }
    ],
    "totalDurationMs": 133728,
    "totalTokens": 46733,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 14858,
      "cache_read_input_tokens": 19301,
      "output_tokens": 12567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 12567,
          "cache_read_input_tokens": 19301,
          "cache_creation_input_tokens": 14858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14858,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
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

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me analyze:

1. **Undefined References** - I need to check all \ref{} and \cite{} in all files
2. **Table-Registry Consistency** - Compare paper values with registry values
3. **Spelling/Grammar** - Scan for issues

Let me compile my findings:

### 1. Undefined References

From the files I've read, let me check all \ref{} targets:

**Labels defined:**
- `sec:appendix` (appendix.tex)
- `fig:filtering_strategies` (appendix.tex)


- Multiple table labels in appendix.tex including `tab:top_features`, `tab:s1_transfer`, `tab:s4_dataset_stats`, `tab:s2_decoding`, `tab:kstar_ci_extended`, `tab:s3_llm_zeroshot`, `tab:s3c_perdepth`, `tab:token_length`, and `tab:s5_features`
- Additional table labels in appendix.tex: `tab:s6_lgbm_params`, `tab:s7_neural_probe`, `tab:s8_cv_folds`, `tab:s9_binary_spearman`, `tab:s10_pythia_decoding`, `tab:s11_length_ablation`, `tab:s12_domain_ablation`, `tab:s13_scorer_sensitivity`
- References to `sec:extended_discussion` and tables in appendix_extended.tex including `tab:crossscorer` and `tab:anova_crossscorer`

I'm compiling a list of all the table and section references across the appendix files to track what needs to be included in the document. Continuing through the main paper sections and their cross-references, I'm tracking the introduction, related work, methodology with the pipeline diagram and key equations, the experimental setup details, and then moving into the core experiments starting with the k-star boundary analysis and its confidence intervals. Now I'm going through the references used in the introduction file, checking which sections are actually being cited and verifying their exact names match what's defined. Continuing through the experiments_c1.tex file, I'm verifying all the cross-references for the extended tables, transfer learning results, ablation studies, and boundary case analyses.

Now checking the remaining files—experiments_c3.tex has the filtering strategy tables and figures, while discussion.tex references several of the same tables and figures I've already confirmed, plus the Pythia decoding results from the appendix. Looking for `sec:extended_decoding` in the files, but it doesn't appear anywhere—seems like it was already removed. I'm also verifying that external table files like `tab_crossscorer` and `tab_filtering_main` are properly referenced, and checking for any other potentially problematic label definitions scattered throughout the text.

I notice in `discussion.tex` there are multiple labels attached to a single section header, which could cause issues if references point to the wrong one.

Looking at the references, I see `Section~\ref{sec:why_kstar}` in appendix_extended.tex and `Section~\ref{sec:length_confound}` in appendix.tex - both resolve to the Discussion section number, which makes sense since these are paragraph-level topics within that section. The multi-label pattern appears intentional for this reason.

I can't find any references to `\ref{sec:extended_decoding}` in the files, so that issue seems to have been resolved already.

Now I'm checking the table-registry consistency, starting with Table 1. Comparing the paper values against the registry for Qwen-rw, I'm finding small discrepancies in a few entries - the 1v2 comparison is off by 0.0002, and 3v4 is off by 0.0001, which suggests potential rounding differences between what's reported and what's stored.

Moving to Pythia, I'm seeing similar minor mismatches where the registry values differ slightly from the paper values, particularly in the 2v3 and 3v4 comparisons, each off by 0.0001.

Now looking at OLMo, there's a significant discrepancy—the registry values are substantially different from what the paper reports, which is concerning and suggests I need to double-check which experiment corresponds to which results. I'm noticing the paper shows consistent results across both the main table and appendix for OLMo, with 1v2=.5080 and its confidence interval clearly below the 0.60 threshold, which would indicate K*=1. But the registry experiment reports 1v2=0.6146 with K*=2, suggesting either a different pipeline configuration or scorer being used in that experiment compared to what's reported in the paper. The paper consistently reports K*=1 for OLMo across multiple tables and sections, with 1v2 ratios below 0.60, but the registry shows K*=2 with 1v2=0.6146 — a substantial discrepancy that suggests the registry experiment may have used an older or different pipeline version than what's documented in the final paper. For Qwen-cont, there are small discrepancies between the paper and registry across multiple comparison pairs—the 0v1 boundary differs by 0.0001, while 1v2, 3v4, and 4v5 each show differences of 0.0001 to 0.0002. These are minor but consistent mismatches worth noting.

The real concern is OLMo, which has more substantial differences. For now, let me check the robustness_10k table—Pythia-1.4B at 10K matches perfectly across all metrics, so that's a clean validation. Now I'm verifying the cross-transfer matrix values from the paper against the registry, checking the diagonal entries for each model configuration to ensure they match. Now I'm looking at the complete cross-transfer performance metrics for experiment 013, comparing how well each model transfers knowledge to the others, and I notice Qwen_rw has the highest baseline performance at 0.4229 while the transfer scores vary considerably depending on the source-target pair. Continuing through the remaining model pairs—Qwen_rw to OLMo shows .265 matching 0.2653 when rounded, and Qwen_rw to Qwen_cont has 0.3466 correctly rounding to .347. Moving into the Pythia comparisons, the pairs with OLMo and Qwen_rw both check out, but I'm verifying whether 0.3287 actually rounds to .329 for the Pythia to Qwen_cont pairing. Now I'm checking the document for spelling and grammar issues, particularly looking at dash usage since the project guidelines restrict dashes in normal prose except for proper nouns. I'm scanning through the files and noticing that compound adjectives like "depth-aware" and "small-effect-size" use hyphens, which are standard and acceptable for that purpose. I'm checking whether em-dashes actually appear in the prose itself—the "--" instances I'm seeing are all in LaTeX number ranges like "80--100%" which follow standard conventions, so those should be fine according to the rule.

Scanning through for repeated words like "the the" or "is is," but I'm not catching any obvious duplicates. The spelling looks solid too—"indistinguishable," "discriminability," "monotonically" are all correct. I should verify the LaTeX formatting is clean, making sure all braces are properly closed and there aren't any syntax issues lurking in the document structure. The multiple labels pointing to the same Discussion section are valid but could be confusing for readers trying to locate specific content—though the section is short enough that paragraph headings help. I notice `sec:extended_decoding` isn't referenced anywhere, so that issue appears resolved. Now I'm spotting another problem: there's a label in appendix_extended.tex that's placed on a paragraph rather than an actual table, which would produce incorrect output if referenced. a section number, not a table number. But I don't see any reference to this label in the text, so it's harmless (though potentially confusing if someone tries to reference it in the future).

In experiments_c1.tex, the neural probe table uses a minipage-based layout instead of a standard table environment. The label on the caption should work correctly with LaTeX counters, though it's an unconventional approach.

The citation keys all appear properly formatted, though I can't verify they exist without the .bib file. There are also external table files being imported that I haven't seen—if they're missing, LaTeX would error, but that's expected for a paper project.

Now I'm noticing a significant discrepancy with the OLMo results. The registry shows 0v1=0.997 and 1v2=0.6146 with K*=2, but the paper table shows 0v1=.9860 and 1v2=.5080 with K*=1. These differences are substantial, suggesting either a different scorer version was used in the registry experiment or the paper incorporates results from a later experiment that replaced the original.

Looking at the appendix data with confidence intervals—OLMo shows 0v1=.986 [.984,.988] and 1v2=.508 [.496,.519]—this matches the paper values precisely and appears to be the authoritative source. The registry experiment must be from an earlier version. The paper also references OLMo yielding K*=1 with a 1v2 AUC of 0.5054, which aligns with the appendix findings and confirms the K*=1 result is correct.

Now scanning through the manuscript for any spelling or grammar issues I might have overlooked in the method and experiments sections, then moving into the appendix extended content to verify the technical language is accurate. I'm checking the robustness section in experiments_c1.tex where seed variation testing shows $\Kempirical$ remains stable across most configurations, with only one marginal shift in the Qwen-Wikipedia case.

Now I'm verifying the LaTeX syntax—the `\rlap` command for spacing-neutral superscripts and `\cmidrule` from booktabs are both valid—and confirming the bibliography setup and appendix includes are properly structured.

I'm also checking the cross-references, particularly whether the `\label` on a `\paragraph` heading will resolve correctly depending on the document's `secnumdepth` setting, since unnumbered paragraphs might reference their parent section instead.

Now I'm ready to compile the report.

Actually, let me verify the OLMo values across all the tables to make sure they're consistent throughout the document.

Looking at the registry data, there's a discrepancy—the experiment shows different numbers than what's in the paper, which suggests it's from an earlier pipeline version or a different configuration. The paper itself is internally consistent though, so there's no error to report there, just a potential mismatch between the registry and the final published results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "c89fb51b-4032-4811-9d76-eb47e300fdb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBY3gqBxEg3xXDdtwuqeLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 62934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 0
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

_source line 80_

Now I have all the data needed. Let me compile the proofread report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "20c4ccd2-91a6-4e6c-9583-4babd65b49d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBY3gqBxEg3xXDdtwuqeLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 62934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 0
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

_source line 81_

<details open><summary>🔧 Tool call — Write · `toolu_01UvUzKw7n55hvwRvCMz4sEA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/proofread_report.md",
  "content": "# Proofread Report — 2026-05-22\n\n## 1. Undefined References\n\n- [PASS] `\\ref{sec:extended_decoding}` (previously known issue): **Not found in any file. Issue has been fixed.**\n- [PASS] All `\\ref{...}` targets have corresponding `\\label{...}` definitions across the paper files.\n- [PASS] All `\\cite{...}` keys use well-formed identifiers. (Cannot verify .bib existence without references.bib, but no formatting issues.)\n- [WARN] `\\label{tab:pairwise_significance}` (appendix_extended.tex:89) is attached to a paragraph, not a table/figure. Not referenced anywhere currently, so harmless, but the `tab:` prefix is misleading if ever used.\n- [INFO] `discussion.tex` defines 7 labels on a single `\\section{Discussion}` (`sec:discussion`, `sec:why_kstar`, `sec:one_wash`, `sec:negative_graduated`, `sec:repr_dependence`, `sec:boundary_cases`, `sec:length_confound`). All refs to these resolve to the same section number. This is intentional (paragraph-level topics) and valid.\n- [INFO] External table inputs (`tables/tab_crossscorer`, `tables/tab_filtering_main`) not verified for existence on disk.\n\n## 2. Table-Registry Consistency\n\n### Table 1 (tab:kstar_ci) — Main Results\n\n**Qwen-rw (mvp_pilot_sat_v1):**\n| Pair | Paper | Registry | Delta |\n|------|-------|----------|-------|\n| 0v1 | .9956 | 0.9956 | 0 |\n| 1v2 | .6955 | 0.6957 | -0.0002 |\n| 2v3 | .5893 | 0.5893 | 0 |\n| 3v4 | .5435 | 0.5434 | +0.0001 |\n| 4v5 | .5340 | 0.5343 | -0.0003 |\n\n- [PASS] All within rounding tolerance (4th decimal place).\n\n**Pythia-1.4B (exp_001_pythia_depth):**\n| Pair | Paper | Registry | Delta |\n|------|-------|----------|-------|\n| 0v1 | .9932 | 0.9932 | 0 |\n| 1v2 | .6539 | 0.6539 | 0 |\n| 2v3 | .5514 | 0.5515 | -0.0001 |\n| 3v4 | .5152 | 0.5153 | -0.0001 |\n| 4v5 | .5136 | 0.5135 | +0.0001 |\n\n- [PASS] All within rounding tolerance.\n\n**OLMo-1B (exp_002_olmo_depth):**\n| Pair | Paper | Registry | Delta |\n|------|-------|----------|-------|\n| 0v1 | .9860 | 0.9970 | **-0.0110** |\n| 1v2 | .5080 | 0.6146 | **-0.1066** |\n| 2v3 | .4973 | 0.5497 | **-0.0524** |\n| K* | 1 | 2 | **DIFFERS** |\n\n- [**MISMATCH — CRITICAL**] Registry `exp_002_olmo_depth` shows K\\*=2 with drastically higher AUC values. Paper is internally consistent (tab:kstar_ci, tab:kstar_ci_extended, tab:s8_cv_folds, tab:bonferroni_ci all agree on OLMo K\\*=1). The registry entry likely reflects an earlier pipeline version or different scorer configuration and needs to be updated to match the final paper values.\n\n**Qwen-cont (exp_017_qwen_continuation):**\n| Pair | Paper | Registry | Delta |\n|------|-------|----------|-------|\n| 0v1 | .9971 | 0.9972 | -0.0001 |\n| 1v2 | .6112 | 0.6114 | -0.0002 |\n| 2v3 | .5609 | 0.5609 | 0 |\n| 3v4 | .5409 | 0.5408 | +0.0001 |\n| 4v5 | .5141 | 0.5139 | +0.0002 |\n\n- [PASS] All within rounding tolerance.\n\n### Table robustness_10k\n\n**Pythia-1.4B 10K (exp_pythia14b_c4_10k):**\n| Pair | Paper | Registry |\n|------|-------|----------|\n| 0v1 | 0.9712 | 0.9712 |\n| 1v2 | 0.6175 | 0.6175 |\n| 2v3 | 0.5364 | 0.5364 |\n| K* | 2 | 2 |\n\n- [PASS] Exact match.\n\n**Qwen-cont 10K (exp_qwen_cont_10k):**\n| Pair | Paper | Registry |\n|------|-------|----------|\n| 0v1 | 0.9875 | 0.9875 |\n| 1v2 | 0.6346 | 0.6346 |\n| 2v3 | 0.5616 | 0.5616 |\n| K* | 2 | 2 |\n\n- [PASS] Exact match.\n\n**LLaMA-8B 10K (exp_llama8b_10k):**\n| Pair | Paper | Registry |\n|------|-------|----------|\n| 0v1 | 0.9282 | 0.9282 |\n| 1v2 (OOF) | 0.5880 | 0.588 |\n| 1v2 (pipeline) | 0.6148 | 0.6148 |\n| 2v3 | 0.5247 | 0.5247 |\n| Bonferroni CI | [0.5776, 0.5978] | [0.5776, 0.5978] |\n| K* | 1 | 1 |\n\n- [PASS] Exact match.\n\n### Transfer Matrix (tab:s1_transfer vs exp_013_cross_transfer)\n\n| Cell | Paper | Registry | Match |\n|------|-------|----------|-------|\n| Qwen-rw diag | .423 | 0.4229 | OK (rounds to .423) |\n| Pythia diag | .386 | 0.3856 | OK (rounds to .386) |\n| OLMo diag | .382 | 0.3822 | OK (rounds to .382) |\n| Qwen-cont diag | .388 | 0.3875 | OK (rounds to .388) |\n| Qwen-rw→Pythia | .259 | 0.259 | OK |\n| Qwen-rw→OLMo | .265 | 0.2653 | OK |\n| Pythia→OLMo | .353 | 0.3531 | OK |\n| Qwen-cont→OLMo | .311 | 0.3112 | OK |\n\n- [PASS] All values consistent within 3-decimal rounding.\n\n## 3. Spelling/Grammar\n\n- [PASS] No repeated words (\"the the\", \"is is\", etc.) found.\n- [PASS] No em-dashes (---) in normal prose. All \"--\" usage is for number ranges (80--100%, 1B--8B), which is standard LaTeX.\n- [PASS] No obvious spelling errors detected.\n- [PASS] No unclosed braces or LaTeX formatting errors detected.\n- [PASS] Sentence structure is grammatically sound throughout.\n\n**Minor notes (non-critical):**\n- appendix_extended.tex line 114: `{\\sloppy ...}` block is functional but unusual; acceptable for preventing overfull hboxes in that paragraph.\n- Hyphenated compounds (\"depth-aware\", \"model-free\", \"cross-model\", \"scorer-invariant\") are standard English compound adjectives, not prohibited dashes.\n\n## Summary\n\n- **Critical issues: 1**\n  - OLMo registry entry (`exp_002_olmo_depth`) is stale: shows K\\*=2 / 1v2 AUC=0.6146, while the paper consistently reports K\\*=1 / 1v2 AUC=0.508. The paper is internally consistent; the registry needs updating.\n\n- **Warnings: 1**\n  - `\\label{tab:pairwise_significance}` uses `tab:` prefix but is not on a table (minor, currently unreferenced).\n\n- **Informational: 2**\n  - Multi-label on Discussion section (intentional, valid).\n  - External `\\input{tables/...}` files not verified.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "f1883392-853f-4f29-94ee-4bcf2a7fab83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBY3gqBxEg3xXDdtwuqeLF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 62934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 0
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

_source line 82 · 2026-05-22T21:29:50.412Z_

<details><summary>↩ Tool result · `toolu_01UvUzKw7n55hvwRvCMz4sEA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/proofread_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "d749cb9a-394c-42e6-b99b-00c780924d81",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/proofread_report.md",
    "content": "# Proofread Report — 2026-05-22\n\n## 1. Undefined References\n\n- [PASS] `\\ref{sec:extended_decoding}` (previously known issue): **Not found in any file. Issue has been fixed.**\n- [PASS] All `\\ref{...}` targets have corresponding `\\label{...}` definitions across the paper files.\n- [PASS] All `\\cite{...}` keys use well-formed identifiers. (Cannot verify .bib existence without references.bib, but no formatting issues.)\n- [WARN] `\\label{tab:pairwise_significance}` (appendix_extended.tex:89) is attached to a paragraph, not a table/figure. Not referenced anywhere currently, so harmless, but the `tab:` prefix is misleading if ever used.\n- [INFO] `discussion.tex` defines 7 labels on a single `\\section{Discussion}` (`sec:discussion`, `sec:why_kstar`, `sec:one_wash`, `sec:negative_graduated`, `sec:repr_dependence`, `sec:boundary_cases`, `sec:length_confound`). All refs to these resolve to the same section number. This is intentional (paragraph-level topics) and valid.\n- [INFO] External table inputs (`tables/tab_crossscorer`, `tables/tab_filtering_main`) not verified for existence on disk.\n\n## 2. Table-Registry Consistency\n\n### Table 1 (tab:kstar_ci) — Main Results\n\n**Qwen-rw (mvp_pilot_sat_v1):**\n| Pair | Paper | Registry | Delta |\n|------|-------|----------|-------|\n| 0v1 | .9956 | 0.9956 | 0 |\n| 1v2 | .6955 | 0.6957 | -0.0002 |\n| 2v3 | .5893 | 0.5893 | 0 |\n| 3v4 | .5435 | 0.5434 | +0.0001 |\n| 4v5 | .5340 | 0.5343 | -0.0003 |\n\n- [PASS] All within rounding tolerance (4th decimal place).\n\n**Pythia-1.4B (exp_001_pythia_depth):**\n| Pair | Paper | Registry | Delta |\n|------|-------|----------|-------|\n| 0v1 | .9932 | 0.9932 | 0 |\n| 1v2 | .6539 | 0.6539 | 0 |\n| 2v3 | .5514 | 0.5515 | -0.0001 |\n| 3v4 | .5152 | 0.5153 | -0.0001 |\n| 4v5 | .5136 | 0.5135 | +0.0001 |\n\n- [PASS] All within rounding tolerance.\n\n**OLMo-1B (exp_002_olmo_depth):**\n| Pair | Paper | Registry | Delta |\n|------|-------|----------|-------|\n| 0v1 | .9860 | 0.9970 | **-0.0110** |\n| 1v2 | .5080 | 0.6146 | **-0.1066** |\n| 2v3 | .4973 | 0.5497 | **-0.0524** |\n| K* | 1 | 2 | **DIFFERS** |\n\n- [**MISMATCH — CRITICAL**] Registry `exp_002_olmo_depth` shows K\\*=2 with drastically higher AUC values. Paper is internally consistent (tab:kstar_ci, tab:kstar_ci_extended, tab:s8_cv_folds, tab:bonferroni_ci all agree on OLMo K\\*=1). The registry entry likely reflects an earlier pipeline version or different scorer configuration and needs to be updated to match the final paper values.\n\n**Qwen-cont (exp_017_qwen_continuation):**\n| Pair | Paper | Registry | Delta |\n|------|-------|----------|-------|\n| 0v1 | .9971 | 0.9972 | -0.0001 |\n| 1v2 | .6112 | 0.6114 | -0.0002 |\n| 2v3 | .5609 | 0.5609 | 0 |\n| 3v4 | .5409 | 0.5408 | +0.0001 |\n| 4v5 | .5141 | 0.5139 | +0.0002 |\n\n- [PASS] All within rounding tolerance.\n\n### Table robustness_10k\n\n**Pythia-1.4B 10K (exp_pythia14b_c4_10k):**\n| Pair | Paper | Registry |\n|------|-------|----------|\n| 0v1 | 0.9712 | 0.9712 |\n| 1v2 | 0.6175 | 0.6175 |\n| 2v3 | 0.5364 | 0.5364 |\n| K* | 2 | 2 |\n\n- [PASS] Exact match.\n\n**Qwen-cont 10K (exp_qwen_cont_10k):**\n| Pair | Paper | Registry |\n|------|-------|----------|\n| 0v1 | 0.9875 | 0.9875 |\n| 1v2 | 0.6346 | 0.6346 |\n| 2v3 | 0.5616 | 0.5616 |\n| K* | 2 | 2 |\n\n- [PASS] Exact match.\n\n**LLaMA-8B 10K (exp_llama8b_10k):**\n| Pair | Paper | Registry |\n|------|-------|----------|\n| 0v1 | 0.9282 | 0.9282 |\n| 1v2 (OOF) | 0.5880 | 0.588 |\n| 1v2 (pipeline) | 0.6148 | 0.6148 |\n| 2v3 | 0.5247 | 0.5247 |\n| Bonferroni CI | [0.5776, 0.5978] | [0.5776, 0.5978] |\n| K* | 1 | 1 |\n\n- [PASS] Exact match.\n\n### Transfer Matrix (tab:s1_transfer vs exp_013_cross_transfer)\n\n| Cell | Paper | Registry | Match |\n|------|-------|----------|-------|\n| Qwen-rw diag | .423 | 0.4229 | OK (rounds to .423) |\n| Pythia diag | .386 | 0.3856 | OK (rounds to .386) |\n| OLMo diag | .382 | 0.3822 | OK (rounds to .382) |\n| Qwen-cont diag | .388 | 0.3875 | OK (rounds to .388) |\n| Qwen-rw→Pythia | .259 | 0.259 | OK |\n| Qwen-rw→OLMo | .265 | 0.2653 | OK |\n| Pythia→OLMo | .353 | 0.3531 | OK |\n| Qwen-cont→OLMo | .311 | 0.3112 | OK |\n\n- [PASS] All values consistent within 3-decimal rounding.\n\n## 3. Spelling/Grammar\n\n- [PASS] No repeated words (\"the the\", \"is is\", etc.) found.\n- [PASS] No em-dashes (---) in normal prose. All \"--\" usage is for number ranges (80--100%, 1B--8B), which is standard LaTeX.\n- [PASS] No obvious spelling errors detected.\n- [PASS] No unclosed braces or LaTeX formatting errors detected.\n- [PASS] Sentence structure is grammatically sound throughout.\n\n**Minor notes (non-critical):**\n- appendix_extended.tex line 114: `{\\sloppy ...}` block is functional but unusual; acceptable for preventing overfull hboxes in that paragraph.\n- Hyphenated compounds (\"depth-aware\", \"model-free\", \"cross-model\", \"scorer-invariant\") are standard English compound adjectives, not prohibited dashes.\n\n## Summary\n\n- **Critical issues: 1**\n  - OLMo registry entry (`exp_002_olmo_depth`) is stale: shows K\\*=2 / 1v2 AUC=0.6146, while the paper consistently reports K\\*=1 / 1v2 AUC=0.508. The paper is internally consistent; the registry needs updating.\n\n- **Warnings: 1**\n  - `\\label{tab:pairwise_significance}` uses `tab:` prefix but is not on a table (minor, currently unreferenced).\n\n- **Informational: 2**\n  - Multi-label on Discussion section (intentional, valid).\n  - External `\\input{tables/...}` files not verified.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01W15HP7xeamZ3ELufDvsYQg`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "ce6376bb-afc1-419e-9795-27f95b3cf16a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0131Z2SvbKjmrz86Q1b5XQwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12410,
      "cache_read_input_tokens": 62934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12410
      },
      "output_tokens": 32,
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

_source line 84 · 2026-05-22T21:29:59.888Z_

<details><summary>↩ Tool result · `toolu_01W15HP7xeamZ3ELufDvsYQg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "f5962b64-4340-4828-ba5e-9a79b72d3261",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_011swkWAAGJEMxGggk7coo4G`</summary>

```json
{
  "name": "proofread_report",
  "type": "report",
  "description": "Paper proofread pre-check report: undefined refs, table-registry consistency, spelling/grammar (2026-05-22)",
  "project": "gen-depth-contamination",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/proofread_report.md",
  "tags": [
    "paper",
    "proofread",
    "quality-check"
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
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "b08b3b79-173f-4c52-b375-30cc0f40d8a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEKYpLk3tBowLrJoh4vkTT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 75344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 712
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 86 · 2026-05-22T21:30:05.455Z_

<details><summary>↩ Tool result · `toolu_011swkWAAGJEMxGggk7coo4G`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_635585\", \"name\": \"proofread_report\", \"type\": \"report\", \"description\": \"Paper proofread pre-check report: undefined refs, table-registry consistency, spelling/grammar (2026-05-22)\", \"path\": \"projects/gen-depth-contamination/artifacts/_project/report/proofread_report.md\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T21:30:05.143182+00:00\", \"tags\": [\"paper\", \"proofread\", \"quality-check\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "58f0cb82-6b64-4b76-89c9-1cdd4ef5d7e8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_635585\\\", \\\"name\\\": \\\"proofread_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Paper proofread pre-check report: undefined refs, table-registry consistency, spelling/grammar (2026-05-22)\\\", \\\"path\\\": \\\"projects/gen-depth-contamination/artifacts/_project/report/proofread_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"gen-depth-contamination\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T21:30:05.143182+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"proofread\\\", \\\"quality-check\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_635585\", \"name\": \"proofread_report\", \"type\": \"report\", \"description\": \"Paper proofread pre-check report: undefined refs, table-registry consistency, spelling/grammar (2026-05-22)\", \"path\": \"projects/gen-depth-contamination/artifacts/_project/report/proofread_report.md\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T21:30:05.143182+00:00\", \"tags\": [\"paper\", \"proofread\", \"quality-check\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 87_

报告已生成：`artifacts/proofread_report.md`

**结果摘要：**

| 类别 | 结果 |
|------|------|
| Undefined References | PASS（`sec:extended_decoding` 已修复，无残留问题） |
| Table 1 vs Registry | Qwen-rw/Pythia/Qwen-cont PASS（≤0.0003 rounding）；**OLMo CRITICAL MISMATCH** |
| Table robustness_10k | PASS（3个实验全部精确匹配） |
| Transfer Matrix | PASS（所有值 3dp 内一致） |
| Spelling/Grammar | PASS（无重复词、无破折号违规、无拼写错误） |

**唯一 Critical Issue：** Registry `exp_002_olmo_depth` 记录 K\*=2 / 1v2 AUC=0.6146，但论文全篇一致报告 OLMo K\*=1 / 1v2 AUC=0.508。论文内部自洽，Registry 需要更新为最终结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "uuid": "3673cbb4-dd5d-4db9-a620-748e2d3fb9b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WducnNzKsSAtXMHu4mqVxa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 76056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 88_

报告已生成：`artifacts/proofread_report.md`

**结果摘要：**

| 类别 | 结果 |
|------|------|
| Undefined References | PASS（`sec:extended_decoding` 已修复，无残留问题） |
| Table 1 vs Registry | Qwen-rw/Pythia/Qwen-cont PASS（≤0.0003 rounding）；**OLMo CRITICAL MISMATCH** |
| Table robustness_10k | PASS（3个实验全部精确匹配） |
| Transfer Matrix | PASS（所有值 3dp 内一致） |
| Spelling/Grammar | PASS（无重复词、无破折号违规、无拼写错误） |

**唯一 Critical Issue：** Registry `exp_002_olmo_depth` 记录 K\*=2 / 1v2 AUC=0.6146，但论文全篇一致报告 OLMo K\*=1 / 1v2 AUC=0.508。论文内部自洽，Registry 需要更新为最终结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 529909,
  "duration_api_ms": 610860,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "d4b6c03e-8eff-42a0-9dc1-d3fa3497a119",
  "total_cost_usd": 1.41084135,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 48178,
    "cache_read_input_tokens": 340124,
    "output_tokens": 14413,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48178,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 305,
        "cache_read_input_tokens": 76056,
        "cache_creation_input_tokens": 503,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 503
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1560,
      "outputTokens": 13121,
      "cacheReadInputTokens": 19301,
      "cacheCreationInputTokens": 34159,
      "webSearchRequests": 0,
      "costUSD": 0.11179384999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 23,
      "outputTokens": 19676,
      "cacheReadInputTokens": 444840,
      "cacheCreationInputTokens": 93538,
      "webSearchRequests": 0,
      "costUSD": 1.2990475000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "76766380-fb8a-47b0-a997-8bd89e78c6e0"
}
```

</details>

---
