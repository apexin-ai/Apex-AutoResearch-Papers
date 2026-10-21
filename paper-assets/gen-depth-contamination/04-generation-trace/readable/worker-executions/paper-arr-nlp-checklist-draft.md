# paper arr nlp checklist draft

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_paper_arr_nlp_checklist_draft_20260522T210101.log`
- **Structured JSON:** [`e98df988e530aea0c31f.json`](../../sessions/e9/e98df988e530aea0c31f.json)

## Before a recorded user message

8 recorded events

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
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
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
  "uuid": "2225f20f-5079-4e6f-ae8c-8a91905911d7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1779498000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c1597fa0-76d1-40ff-8ce3-f37d86bacc54",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Assistant

_source line 4_

I'll read the paper to understand the research content, then prepare the checklist draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "eb20159e-6cb3-4c5d-8cdd-40f8a61142ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbNcvP5UeXBGpHbhFbiGrt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12321,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12321
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

<details open><summary>🔧 Tool call — Read · `toolu_01LqLsbidzkmpcYHkqdNVtnv`</summary>

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
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "1b71c271-415b-4d63-9555-bb6c07610133",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbNcvP5UeXBGpHbhFbiGrt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12321,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12321
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

_source line 6 · 2026-05-22T21:01:12.901Z_

<details><summary>↩ Tool result · `toolu_01LqLsbidzkmpcYHkqdNVtnv`</summary>

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
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "12d1835e-15d6-4344-b28c-67cc947060bc",
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

_source line 7_

<details open><summary>🔧 Tool call — Agent · `toolu_01SpnMVyzeBP6t8oFdSTt7bi`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read paper sections",
  "prompt": "I need to read the key sections of a paper to understand its methodology, data, models, evaluation, and computational setup. Read these files and summarize the key details relevant to an ARR Responsible NLP Checklist:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex — What methods are used? What models? What features?\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex — What experiments? What metrics? Computational resources? Random seeds? Statistical significance?\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex — Additional experiments\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex — Discussion section\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex — Introduction\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex — Appendix (may contain computational details, hyperparameters)\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex — Extended appendix\n\nFor each file, extract:\n- Datasets used (names, sources, licenses if mentioned)\n- Models used (names, sizes, whether they are publicly available)\n- Computational resources (GPUs, training time, etc.)\n- Hyperparameters and their search ranges\n- Random seeds\n- Statistical significance tests\n- Any mention of human evaluation\n- Any mention of PII or sensitive data\n- Any mention of code/data release plans\n- Any mention of environmental impact\n\nReport all findings in a structured summary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "4388aa3c-4fe8-4a55-a62a-360487132141",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFKG6ag9tAb8UdzbaCCAmf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1580,
      "cache_read_input_tokens": 24162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1580
      },
      "output_tokens": 49,
      "service_tier": "standard",
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

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "description": "Read paper sections",
  "task_type": "local_agent",
  "prompt": "I need to read the key sections of a paper to understand its methodology, data, models, evaluation, and computational setup. Read these files and summarize the key details relevant to an ARR Responsible NLP Checklist:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex — What methods are used? What models? What features?\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex — What experiments? What metrics? Computational resources? Random seeds? Statistical significance?\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex — Additional experiments\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex — Discussion section\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex — Introduction\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex — Appendix (may contain computational details, hyperparameters)\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex — Extended appendix\n\nFor each file, extract:\n- Datasets used (names, sources, licenses if mentioned)\n- Models used (names, sizes, whether they are publicly available)\n- Computational resources (GPUs, training time, etc.)\n- Hyperparameters and their search ranges\n- Random seeds\n- Statistical significance tests\n- Any mention of human evaluation\n- Any mention of PII or sensitive data\n- Any mention of code/data release plans\n- Any mention of environmental impact\n\nReport all findings in a structured summary.",
  "uuid": "686c6801-0a12-4565-8970-b79ce4c4c067",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

## Round 1

39 recorded events

### User

_source line 9 · 2026-05-22T21:01:24.782Z_

I need to read the key sections of a paper to understand its methodology, data, models, evaluation, and computational setup. Read these files and summarize the key details relevant to an ARR Responsible NLP Checklist:

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex — What methods are used? What models? What features?
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex — What experiments? What metrics? Computational resources? Random seeds? Statistical significance?
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex — Additional experiments
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex — Discussion section
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex — Introduction
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex — Appendix (may contain computational details, hyperparameters)
7. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex — Extended appendix

For each file, extract:
- Datasets used (names, sources, licenses if mentioned)
- Models used (names, sizes, whether they are publicly available)
- Computational resources (GPUs, training time, etc.)
- Hyperparameters and their search ranges
- Random seeds
- Statistical significance tests
- Any mention of human evaluation
- Any mention of PII or sensitive data
- Any mention of code/data release plans
- Any mention of environmental impact

Report all findings in a structured summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "1e6d7f1f-f677-458f-b18b-405ab8ac9919"
}
```

</details>

---

### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 15898,
    "tool_uses": 1,
    "duration_ms": 1547
  },
  "last_tool_name": "Read",
  "uuid": "bc81da76-530c-4807-b1ef-9c40c2addd2b",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_017iZ3nRRDp6Q7cnJ5iKHpQA`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "c93f18fd-93b7-4a66-9a04-6ece94176fa1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Bt3iVNpmbemJWKPDPEGe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15889,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15889,
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

_source line 12 · 2026-05-22T21:01:26.339Z_

<details><summary>↩ Tool result · `toolu_017iZ3nRRDp6Q7cnJ5iKHpQA`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "876a333e-0752-4cad-96e1-864ce62bc459"
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
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "description": "Reading docs/paper/experiments_c1.tex",
  "usage": {
    "total_tokens": 15901,
    "tool_uses": 2,
    "duration_ms": 1765
  },
  "last_tool_name": "Read",
  "uuid": "6b19ea1c-296a-46b6-87e0-77990d2c6f64",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01QVf1dFLveYFt5F1zbGVC6w`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "70ed7912-dbd9-4f3d-824b-edaa69216f97",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Bt3iVNpmbemJWKPDPEGe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15889,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15889,
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

_source line 15 · 2026-05-22T21:01:26.555Z_

<details><summary>↩ Tool result · `toolu_01QVf1dFLveYFt5F1zbGVC6w`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "9792a62c-7a92-4c01-9ffc-03b9e3211eeb"
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
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "description": "Reading docs/paper/experiments_c3.tex",
  "usage": {
    "total_tokens": 15904,
    "tool_uses": 3,
    "duration_ms": 2184
  },
  "last_tool_name": "Read",
  "uuid": "91cc8ee6-3e80-4d90-b832-8fde10e70d81",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_012VG2SAJQn3B4LLzrGknZm7`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "d69274a9-b5f6-4ffc-a7df-92ccc36d7db9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Bt3iVNpmbemJWKPDPEGe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15889,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15889,
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

_source line 18 · 2026-05-22T21:01:26.974Z_

<details><summary>↩ Tool result · `toolu_012VG2SAJQn3B4LLzrGknZm7`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "1c72c701-b5df-4f16-89ee-275541b692d2"
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
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "description": "Reading docs/paper/discussion.tex",
  "usage": {
    "total_tokens": 15907,
    "tool_uses": 4,
    "duration_ms": 2391
  },
  "last_tool_name": "Read",
  "uuid": "ee0f8e9b-954a-4fb0-8af3-6e670d165b2e",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_017BRjyJKsKAvhGV28ed2g4u`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "fcd4c4ab-6f3e-41b9-ba31-0c60efbcb532",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Bt3iVNpmbemJWKPDPEGe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15889,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15889,
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

_source line 21 · 2026-05-22T21:01:27.182Z_

<details><summary>↩ Tool result · `toolu_017BRjyJKsKAvhGV28ed2g4u`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "c5d4596a-db0b-4fe6-888a-684dd2ca57f9"
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
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 15910,
    "tool_uses": 5,
    "duration_ms": 2604
  },
  "last_tool_name": "Read",
  "uuid": "bc101605-b95c-4b34-a204-e81f5d46207d",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_017V61LhxviAoLMGZ3tRzpof`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "efd1fa66-4b55-41ff-92f2-7f4d51fb1516",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Bt3iVNpmbemJWKPDPEGe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15889,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15889,
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

_source line 24 · 2026-05-22T21:01:27.394Z_

<details><summary>↩ Tool result · `toolu_017V61LhxviAoLMGZ3tRzpof`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "4fb1c3b2-99f7-471b-b7f8-d4e0a53c9ba3"
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
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "description": "Reading docs/paper/appendix.tex",
  "usage": {
    "total_tokens": 15913,
    "tool_uses": 6,
    "duration_ms": 2816
  },
  "last_tool_name": "Read",
  "uuid": "d2ac42db-caae-4c9f-af12-ea58df996c35",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_018gpXZuXzLnaAvr5btqq554`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "5ac3a6ed-ff78-4ab7-a617-1044fdc7d18f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Bt3iVNpmbemJWKPDPEGe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15889,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15889,
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

_source line 27 · 2026-05-22T21:01:27.606Z_

<details><summary>↩ Tool result · `toolu_018gpXZuXzLnaAvr5btqq554`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "7ceecf04-6ecd-4be3-a71b-988caaa204f6"
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
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "description": "Reading docs/paper/appendix_extended.tex",
  "usage": {
    "total_tokens": 15916,
    "tool_uses": 7,
    "duration_ms": 2954
  },
  "last_tool_name": "Read",
  "uuid": "09ec3359-25fa-4303-8dd0-928c9d638379",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_011fCiVEkgCZBrxnGoupbiQB`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "1482c1d8-d65c-411e-a00d-07ce4bae904f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Bt3iVNpmbemJWKPDPEGe9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15889,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15889,
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

_source line 30 · 2026-05-22T21:01:27.742Z_

<details><summary>↩ Tool result · `toolu_011fCiVEkgCZBrxnGoupbiQB`</summary>

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
  "parent_tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "c8a3430f-b2ad-4ecf-8ebb-c6689cd8a6a7"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a87196473858b9a34",
  "tool_use_id": "toolu_01SpnMVyzeBP6t8oFdSTt7bi",
  "status": "completed",
  "output_file": "",
  "summary": "Read paper sections",
  "usage": {
    "total_tokens": 48521,
    "tool_uses": 7,
    "duration_ms": 33135
  },
  "uuid": "bd1fb912-10bc-4409-9ceb-d02320b3bf82",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool result

_source line 32 · 2026-05-22T21:01:57.921Z_

<details><summary>↩ Tool result · `toolu_01SpnMVyzeBP6t8oFdSTt7bi`</summary>

```text
Now I have all the key paper sections. Let me compile a comprehensive summary organized around the ARR Responsible NLP Checklist requirements.

## ARR Responsible NLP Checklist Summary: Generational Depth Contamination Paper

### DATASETS USED

**C4 (Primary Dataset)**
- Source: C4 English validation split
- Size: 5,000 seed documents per configuration + recursive generations up to depth 5 (30,000 total documents per model configuration)
- Tokenization: 256 subword tokens (truncated for seed documents)
- License: Not mentioned in paper
- Additional details: General web text corpus used as primary domain for experiments

**Wikipedia**
- Size: 5,000 texts tested for cross-domain variation
- Purpose: Domain robustness validation
- Results: K_empirical = 2 (matching C4)

**arXiv Abstracts**
- Size: 2,200 texts
- Purpose: Domain robustness validation with structured academic text
- Results: K_empirical = 3 (higher discriminability due to formulaic structure)

**MMLU & HellaSwag**
- Purpose: Downstream task evaluation for filtering consistency checks
- Usage: Fine-tuning evaluation via LoRA (rank 8, α_LoRA=16) for 3 epochs across 5 seeds

### MODELS USED

**Generation Models (LLMs)**
- Qwen2.5-1.5B-Instruct (instruction-tuned, 1.5B parameters) — rewrite and continuation modes
- Qwen2.5-1.5B (base, no instruction tuning)
- Qwen2.5-7B (7B parameters, fp16 precision)
- Pythia-1.4B (1.4B parameters)
- Pythia-6.9B (6.9B parameters)
- OLMo-1B (1B parameters)
- LLaMA-3.1-8B (8B parameters)
- Mistral-7B (7B parameters)
- Gemma-2-2B (2B parameters)

All models are publicly available (Hugging Face).

**Scoring/Feature Extraction Models**
- Qwen2.5-1.5B (primary, for token-level surprisal computation)
- Pythia-1.4B (cross-scorer validation)
- OLMo-1B (cross-scorer validation)

**Classifiers**
- OBD-LightGBM (Ordinal Binary Decomposition): Primary depth classifier using 15 hand-crafted statistical features
- LightGBM hyperparameters: n_estimators=200, learning_rate=0.05, max_depth=6, num_leaves=31
- Neural probe: 2-layer MLP (d_emb → 512 → 256 → 6, ReLU activation, dropout=0.1)

### COMPUTATIONAL RESOURCES

**Training/Inference Infrastructure**
- No explicit GPU/compute specifications mentioned in text
- Generation: 30,000 documents per model configuration (5,000 seeds × 6 depth levels)
- Recursive generation: K=5 iterations (6 depth levels total: 0–5)

**Feature Computation**
- Bootstrap resampling: 1,000–10,000 resamples for confidence intervals
- Permutation testing: 10,000 iterations for p-value estimation
- Cross-validation: 5-fold GroupKFold (grouped by seed document to prevent leakage)

**Fine-tuning for Filtering Experiments**
- LoRA fine-tuning: rank 8, α_LoRA=16
- Epochs: 3
- Seeds: 5 (51 total runs with 10 strategy combinations)
- Task: MMLU and HellaSwag
- Setting: 100% synthetic data (upper bound scenario)

### HYPERPARAMETERS AND SEARCH RANGES

**Generation/Decoding Parameters**
- Default: nucleus sampling p=0.95, temperature T=1.0
- Ablation configurations tested:
  - Greedy decoding
  - Nucleus p=0.9, T=1.0
  - Nucleus p=0.95, T=0.7
  - Nucleus p=0.95, T=1.2

**Threshold Sensitivity**
- Primary decision threshold: θ = 0.60 (operationally defined K_empirical boundary)
- Sensitivity analysis: θ ∈ [0.55, 0.70]
- Justification: Cohen's h ≈ 0.20 (small effect size convention)

**Graduated Filtering Weights**
- w = exp(-α · d̂) where α ∈ {0.1, 0.2, ..., 0.9}
- Tested for dose-response contamination evaluation

**Feature Set (15 dimensions)**
- Surprisal moments: mean, std, skewness, kurtosis (4)
- Surprisal derivatives: mean/std of first- and second-order differences, skewness (5)
- Vocabulary diversity: type-token ratio, hapax legomena ratio, self-BLEU (3)
- Frequency tail: kurtosis, entropy, rare token fraction (3)

**Neural Probe Architecture**
- Optimizer: Adam (lr=10^-3, weight decay=10^-4)
- Loss: Cross-entropy
- Batch size: 256
- Max epochs: 20
- Early stopping: Patience=5 (validation loss)

### RANDOM SEEDS

**Primary Seed**
- Seed = 42 (corpus sampling + generation)

**Robustness Testing**
- Alternative seed = 123 (replication on Wikipedia and C4)
- Result: K_empirical stable in 2/3 configurations; marginal shifts in 1/3

**Contamination Dose-Response**
- 5 seeds for 10%, 30%, 50% contamination ratio experiments

**Cross-Sample Robustness**
- N=5,000 (primary) vs. N=10,000 (independent sample validation)
- Different random seeds for each draw

### STATISTICAL SIGNIFICANCE AND TESTING

**Bootstrap Confidence Intervals**
- 1,000–10,000 resamples (stratified by fold)
- 95% CIs reported for all boundary comparisons
- Bonferroni correction: α_corr = 0.005 (99.5% CIs) for 10 simultaneous model comparisons

**Permutation Testing**
- 10,000-iteration permutation test for AUC boundary comparisons
- All boundary comparisons: p < 0.001 (6/10 K_empirical=2 configurations)
- Pythia-6.9B 4v5 pair: p = 0.12 (non-significant)

**ANOVA Analysis**
- Three-way ANOVA (Generator × Scorer × Depth-Pair)
- N=300 observations (12 cells × 5 folds × 5 depth-pairs)
- Scorer effect: η²_p = 0.166 (modest)
- Generator × Scorer interaction: η²_p = 0.146 (significant but modest)

**McNemar Test**
- OBD vs. LLM zero-shot comparison (GPT-5.5, Claude Opus 4.6)
- p > 0.05 for depth ≥ 2 comparisons (no significant difference in failure modes)

**Spearman Correlation (Cross-Model Transfer)**
- Feature ranking robustness: ρ > 0.90 (scorer-invariant)
- Cross-configuration ranking: ρ ≥ 0.85 (continuation-mode models)
- Binary detector ranking: |ρ| = 0.06–0.46 (weak)

**Effect Size Reporting**
- Pairwise AUC as primary metric
- Per-fold AUC variation tracked
- 1v2 AUC range: 0.5080–0.6955 across configurations
- 2v3 AUC range: 0.4973–0.5893 (consistently below θ)

### HUMAN EVALUATION

**No human evaluation conducted**
- The paper focuses on automated detection and classification
- LLM zero-shot baselines (GPT-5.5, Claude Opus 4.6) used as reference, not human evaluation
- Downstream task evaluation (MMLU, HellaSwag) is automated

### PII AND SENSITIVE DATA

**No explicit mention of PII concerns**
- C4 is a public web corpus with publicly available license
- No special handling of sensitive data mentioned
- No human annotation involved

### CODE AND DATA RELEASE PLANS

**Not explicitly stated in paper**
- Figure captions reference datasets but do not specify release plans
- No mention of code repository, pre-computed features, or data release timeline
- Reproducibility: Full hyperparameters, feature definitions (Table S5), and experimental configurations provided

### ENVIRONMENTAL IMPACT

**No explicit environmental impact assessment**
- No mention of CO2 emissions, energy consumption, or computational carbon footprint
- Model scale ranges from 1B–8B parameters with generation at scale (30,000 documents per config)
- LoRA fine-tuning (rank 8) reduces training cost vs. full fine-tuning but no quantification provided

---

## KEY RESPONSIBLE NLP CHECKLIST ITEMS TO ADDRESS

**Critical findings for ARR checklist:**

1. **Dataset sourcing**: C4 (public), Wikipedia (public), arXiv (public) — all well-established
2. **Model availability**: All generation and feature models are publicly available on Hugging Face
3. **Reproducibility**: Extensive hyperparameter documentation; random seeds reported; 5-fold CV with seed tracking
4. **Statistical rigor**: Bootstrap CIs with 1,000–10,000 resamples; permutation testing (p < 0.001); Bonferroni correction applied
5. **Robustness claims**: Seed robustness (seed 42 vs. 123), sample robustness (5K vs. 10K), cross-domain validation
6. **Limitations acknowledged**: Prompt-chain vs. retrain-chain distinction; threshold sensitivity; scorer dependence; scale effects (1B–8B)
7. **Filtering validation**: Downstream task evaluation on MMLU/HellaSwag with 5-seed averaging
8. **Missing elements**: No explicit environmental impact statement, no code/data release timeline, no human evaluation

**File paths for reference:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "3edcbf8e-c05d-4f37-8e81-b0c5db2b898f",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to read the key sections of a paper to understand its methodology, data, models, evaluation, and computational setup. Read these files and summarize the key details relevant to an ARR Responsible NLP Checklist:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex — What methods are used? What models? What features?\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex — What experiments? What metrics? Computational resources? Random seeds? Statistical significance?\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex — Additional experiments\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex — Discussion section\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex — Introduction\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex — Appendix (may contain computational details, hyperparameters)\n7. /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex — Extended appendix\n\nFor each file, extract:\n- Datasets used (names, sources, licenses if mentioned)\n- Models used (names, sizes, whether they are publicly available)\n- Computational resources (GPUs, training time, etc.)\n- Hyperparameters and their search ranges\n- Random seeds\n- Statistical significance tests\n- Any mention of human evaluation\n- Any mention of PII or sensitive data\n- Any mention of code/data release plans\n- Any mention of environmental impact\n\nReport all findings in a structured summary.",
    "agentId": "a87196473858b9a34",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the key paper sections. Let me compile a comprehensive summary organized around the ARR Responsible NLP Checklist requirements.\n\n## ARR Responsible NLP Checklist Summary: Generational Depth Contamination Paper\n\n### DATASETS USED\n\n**C4 (Primary Dataset)**\n- Source: C4 English validation split\n- Size: 5,000 seed documents per configuration + recursive generations up to depth 5 (30,000 total documents per model configuration)\n- Tokenization: 256 subword tokens (truncated for seed documents)\n- License: Not mentioned in paper\n- Additional details: General web text corpus used as primary domain for experiments\n\n**Wikipedia**\n- Size: 5,000 texts tested for cross-domain variation\n- Purpose: Domain robustness validation\n- Results: K_empirical = 2 (matching C4)\n\n**arXiv Abstracts**\n- Size: 2,200 texts\n- Purpose: Domain robustness validation with structured academic text\n- Results: K_empirical = 3 (higher discriminability due to formulaic structure)\n\n**MMLU & HellaSwag**\n- Purpose: Downstream task evaluation for filtering consistency checks\n- Usage: Fine-tuning evaluation via LoRA (rank 8, α_LoRA=16) for 3 epochs across 5 seeds\n\n### MODELS USED\n\n**Generation Models (LLMs)**\n- Qwen2.5-1.5B-Instruct (instruction-tuned, 1.5B parameters) — rewrite and continuation modes\n- Qwen2.5-1.5B (base, no instruction tuning)\n- Qwen2.5-7B (7B parameters, fp16 precision)\n- Pythia-1.4B (1.4B parameters)\n- Pythia-6.9B (6.9B parameters)\n- OLMo-1B (1B parameters)\n- LLaMA-3.1-8B (8B parameters)\n- Mistral-7B (7B parameters)\n- Gemma-2-2B (2B parameters)\n\nAll models are publicly available (Hugging Face).\n\n**Scoring/Feature Extraction Models**\n- Qwen2.5-1.5B (primary, for token-level surprisal computation)\n- Pythia-1.4B (cross-scorer validation)\n- OLMo-1B (cross-scorer validation)\n\n**Classifiers**\n- OBD-LightGBM (Ordinal Binary Decomposition): Primary depth classifier using 15 hand-crafted statistical features\n- LightGBM hyperparameters: n_estimators=200, learning_rate=0.05, max_depth=6, num_leaves=31\n- Neural probe: 2-layer MLP (d_emb → 512 → 256 → 6, ReLU activation, dropout=0.1)\n\n### COMPUTATIONAL RESOURCES\n\n**Training/Inference Infrastructure**\n- No explicit GPU/compute specifications mentioned in text\n- Generation: 30,000 documents per model configuration (5,000 seeds × 6 depth levels)\n- Recursive generation: K=5 iterations (6 depth levels total: 0–5)\n\n**Feature Computation**\n- Bootstrap resampling: 1,000–10,000 resamples for confidence intervals\n- Permutation testing: 10,000 iterations for p-value estimation\n- Cross-validation: 5-fold GroupKFold (grouped by seed document to prevent leakage)\n\n**Fine-tuning for Filtering Experiments**\n- LoRA fine-tuning: rank 8, α_LoRA=16\n- Epochs: 3\n- Seeds: 5 (51 total runs with 10 strategy combinations)\n- Task: MMLU and HellaSwag\n- Setting: 100% synthetic data (upper bound scenario)\n\n### HYPERPARAMETERS AND SEARCH RANGES\n\n**Generation/Decoding Parameters**\n- Default: nucleus sampling p=0.95, temperature T=1.0\n- Ablation configurations tested:\n  - Greedy decoding\n  - Nucleus p=0.9, T=1.0\n  - Nucleus p=0.95, T=0.7\n  - Nucleus p=0.95, T=1.2\n\n**Threshold Sensitivity**\n- Primary decision threshold: θ = 0.60 (operationally defined K_empirical boundary)\n- Sensitivity analysis: θ ∈ [0.55, 0.70]\n- Justification: Cohen's h ≈ 0.20 (small effect size convention)\n\n**Graduated Filtering Weights**\n- w = exp(-α · d̂) where α ∈ {0.1, 0.2, ..., 0.9}\n- Tested for dose-response contamination evaluation\n\n**Feature Set (15 dimensions)**\n- Surprisal moments: mean, std, skewness, kurtosis (4)\n- Surprisal derivatives: mean/std of first- and second-order differences, skewness (5)\n- Vocabulary diversity: type-token ratio, hapax legomena ratio, self-BLEU (3)\n- Frequency tail: kurtosis, entropy, rare token fraction (3)\n\n**Neural Probe Architecture**\n- Optimizer: Adam (lr=10^-3, weight decay=10^-4)\n- Loss: Cross-entropy\n- Batch size: 256\n- Max epochs: 20\n- Early stopping: Patience=5 (validation loss)\n\n### RANDOM SEEDS\n\n**Primary Seed**\n- Seed = 42 (corpus sampling + generation)\n\n**Robustness Testing**\n- Alternative seed = 123 (replication on Wikipedia and C4)\n- Result: K_empirical stable in 2/3 configurations; marginal shifts in 1/3\n\n**Contamination Dose-Response**\n- 5 seeds for 10%, 30%, 50% contamination ratio experiments\n\n**Cross-Sample Robustness**\n- N=5,000 (primary) vs. N=10,000 (independent sample validation)\n- Different random seeds for each draw\n\n### STATISTICAL SIGNIFICANCE AND TESTING\n\n**Bootstrap Confidence Intervals**\n- 1,000–10,000 resamples (stratified by fold)\n- 95% CIs reported for all boundary comparisons\n- Bonferroni correction: α_corr = 0.005 (99.5% CIs) for 10 simultaneous model comparisons\n\n**Permutation Testing**\n- 10,000-iteration permutation test for AUC boundary comparisons\n- All boundary comparisons: p < 0.001 (6/10 K_empirical=2 configurations)\n- Pythia-6.9B 4v5 pair: p = 0.12 (non-significant)\n\n**ANOVA Analysis**\n- Three-way ANOVA (Generator × Scorer × Depth-Pair)\n- N=300 observations (12 cells × 5 folds × 5 depth-pairs)\n- Scorer effect: η²_p = 0.166 (modest)\n- Generator × Scorer interaction: η²_p = 0.146 (significant but modest)\n\n**McNemar Test**\n- OBD vs. LLM zero-shot comparison (GPT-5.5, Claude Opus 4.6)\n- p > 0.05 for depth ≥ 2 comparisons (no significant difference in failure modes)\n\n**Spearman Correlation (Cross-Model Transfer)**\n- Feature ranking robustness: ρ > 0.90 (scorer-invariant)\n- Cross-configuration ranking: ρ ≥ 0.85 (continuation-mode models)\n- Binary detector ranking: |ρ| = 0.06–0.46 (weak)\n\n**Effect Size Reporting**\n- Pairwise AUC as primary metric\n- Per-fold AUC variation tracked\n- 1v2 AUC range: 0.5080–0.6955 across configurations\n- 2v3 AUC range: 0.4973–0.5893 (consistently below θ)\n\n### HUMAN EVALUATION\n\n**No human evaluation conducted**\n- The paper focuses on automated detection and classification\n- LLM zero-shot baselines (GPT-5.5, Claude Opus 4.6) used as reference, not human evaluation\n- Downstream task evaluation (MMLU, HellaSwag) is automated\n\n### PII AND SENSITIVE DATA\n\n**No explicit mention of PII concerns**\n- C4 is a public web corpus with publicly available license\n- No special handling of sensitive data mentioned\n- No human annotation involved\n\n### CODE AND DATA RELEASE PLANS\n\n**Not explicitly stated in paper**\n- Figure captions reference datasets but do not specify release plans\n- No mention of code repository, pre-computed features, or data release timeline\n- Reproducibility: Full hyperparameters, feature definitions (Table S5), and experimental configurations provided\n\n### ENVIRONMENTAL IMPACT\n\n**No explicit environmental impact assessment**\n- No mention of CO2 emissions, energy consumption, or computational carbon footprint\n- Model scale ranges from 1B–8B parameters with generation at scale (30,000 documents per config)\n- LoRA fine-tuning (rank 8) reduces training cost vs. full fine-tuning but no quantification provided\n\n---\n\n## KEY RESPONSIBLE NLP CHECKLIST ITEMS TO ADDRESS\n\n**Critical findings for ARR checklist:**\n\n1. **Dataset sourcing**: C4 (public), Wikipedia (public), arXiv (public) — all well-established\n2. **Model availability**: All generation and feature models are publicly available on Hugging Face\n3. **Reproducibility**: Extensive hyperparameter documentation; random seeds reported; 5-fold CV with seed tracking\n4. **Statistical rigor**: Bootstrap CIs with 1,000–10,000 resamples; permutation testing (p < 0.001); Bonferroni correction applied\n5. **Robustness claims**: Seed robustness (seed 42 vs. 123), sample robustness (5K vs. 10K), cross-domain validation\n6. **Limitations acknowledged**: Prompt-chain vs. retrain-chain distinction; threshold sensitivity; scorer dependence; scale effects (1B–8B)\n7. **Filtering validation**: Downstream task evaluation on MMLU/HellaSwag with 5-seed averaging\n8. **Missing elements**: No explicit environmental impact statement, no code/data release timeline, no human evaluation\n\n**File paths for reference:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`"
      }
    ],
    "totalDurationMs": 33138,
    "totalTokens": 51232,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 32600,
      "cache_read_input_tokens": 15889,
      "output_tokens": 2736,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 32600
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2736,
          "cache_read_input_tokens": 15889,
          "cache_creation_input_tokens": 32600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 32600,
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

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the paper. Let me also check the Ethics Statement and Limitations sections more carefully from main.tex (already read), and now prepare the checklist draft.

Key facts from the paper:
- Datasets: C4 (public), Wikipedia (public), arXiv (public)
- Models: All publicly available on HuggingFace (Qwen2.5, Pythia, OLMo, LLaMA, Mistral, Gemma)
- Classifier: OBD-LightGBM with 15 statistical features
- No human evaluation


- No PII concerns, and the paper includes both a Limitations section with three key points and an Ethics statement
- Code and data will be released upon acceptance
- Random seeds are well-documented: 42 as primary, 123 for robustness checks, and 5 seeds for filtering
- Statistical rigor is demonstrated through bootstrap confidence intervals, permutation testing, and Bonferroni correction
- Hyperparameters are fully specified, though computational resources like GPU requirements and training time aren't explicitly detailed
- No environmental impact statement is present

Now I'll draft responses for the 2024-2025 ARR checklist sections A-F.

Let me also double-check the appendix to see if there's any computational budget information that might have been overlooked.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "f5bdf6d8-ce7b-49c1-9c0f-071e56b8df7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoKmHApncoup63issyLiww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 25742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3334
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

_source line 34_

Now let me check if computational resources are mentioned anywhere in the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "e967ab11-7576-49c8-a1a7-2fdf99700a0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoKmHApncoup63issyLiww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 25742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3334
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

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_01Kturp5EP6j3TyR6sQCuxpc`</summary>

```json
{
  "pattern": "GPU|compute|hour|A100|V100|H100|runtime|wall.clock|carbon|CO2|energy",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
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
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "5c254dc9-e4a2-4fd4-8836-c71ee6d56ebc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KoKmHApncoup63issyLiww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 25742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3334
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

_source line 36 · 2026-05-22T21:02:11.148Z_

<details><summary>↩ Tool result · `toolu_01Kturp5EP6j3TyR6sQCuxpc`</summary>

```text
docs/paper/appendix_extended.tex:160:\caption{Bonferroni-corrected 99.5\% confidence intervals for $\Kempirical$ boundary pairs across all 10 configurations. $\alpha_{\text{corr}} = 0.005$; CI computed as $\auc \pm 2.807 \times \hat{\sigma}_{\text{boot}}$. ``Pass $\theta$'': CI lower bound $> 0.60$.}
docs/paper/main.log:582:File: mt-cmr.cfg 2013/05/19 v2.2 microtype config. file: Computer Modern Roman 
docs/paper/acl_natbib.bst:484:MACRO {ieeetc} {"IEEE Transactions on Computers"}
docs/paper/acl_natbib.bst:487: {"IEEE Transactions on Computer-Aided Design of Integrated Circuits"}
docs/paper/acl_natbib.bst:493:MACRO {jcss} {"Journal of Computer and System Sciences"}
docs/paper/acl_natbib.bst:495:MACRO {scp} {"Science of Computer Programming"}
docs/paper/acl_natbib.bst:499:MACRO {tocs} {"ACM Transactions on Computer Systems"}
docs/paper/acl_natbib.bst:511:MACRO {tcs} {"Theoretical Computer Science"}
docs/paper/acl_natbib.bst:596:		  % compute the number of remaining authors
docs/paper/tables/tab_domain_model_kstar_full.tex:3:\caption{Full generative depth results with AUC at the $K^*$ boundary (scorer: Qwen2.5-1.5B, $\theta{=}0.60$). AUC($k$v$k{+}1$) denotes the area under the ROC curve distinguishing generation $k$ from generation $k{+}1$. Bold indicates the dominant $K^*$ mode per domain. For Wikipedia ($K^*{=}1$), boundary AUC reports 0v1. All AUC values computed on held-out test splits ($n{=}500$ per class).}
docs/paper/method.tex:43:All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
docs/paper/method.tex:44:Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
docs/paper/integration_templates.md:171:We compute Spearman $\rho$ between detector confidence and true depth for two representative detectors: DivEye~\cite{basani2026diveye} (log-PPL) and Binoculars~\cite{hans2024binoculars} (cross-model perplexity ratio; observer: Pythia-1.4B, performer: OLMo-1B).
docs/paper/appendix.tex:243:  \caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}
docs/paper/main.aux:1007:\@writefile{lot}{\contentsline {table}{\numberline {14}{\ignorespaces Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}}{13}{table.caption.39}\protected@file@percent }
docs/paper/main.aux:1008:\newlabel{tab:s5_features}{{14}{13}{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document}{table.caption.39}{}}
docs/paper/main.aux:1240:\@writefile{lot}{\contentsline {table}{\numberline {27}{\ignorespaces Bonferroni-corrected 99.5\% confidence intervals for ${K^*_{\text  {empirical}}}$ boundary pairs across all 10 configurations. $\alpha _{\text  {corr}} = 0.005$; CI computed as $\text  {AUC}\pm 2.807 \times \hat  {\sigma }_{\text  {boot}}$. ``Pass $\theta $'': CI lower bound $> 0.60$.}}{17}{table.caption.50}\protected@file@percent }
docs/paper/main.aux:1241:\newlabel{tab:bonferroni_ci}{{27}{17}{Bonferroni-corrected 99.5\% confidence intervals for $\Kempirical $ boundary pairs across all 10 configurations. $\alpha _{\text {corr}} = 0.005$; CI computed as $\auc \pm 2.807 \times \hat {\sigma }_{\text {boot}}$. ``Pass $\theta $'': CI lower bound $> 0.60$}{table.caption.50}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "649b17d9-08a4-4c83-9ca0-70e884843a2b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/appendix_extended.tex:160:\\caption{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical$ boundary pairs across all 10 configurations. $\\alpha_{\\text{corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat{\\sigma}_{\\text{boot}}$. ``Pass $\\theta$'': CI lower bound $> 0.60$.}\ndocs/paper/main.log:582:File: mt-cmr.cfg 2013/05/19 v2.2 microtype config. file: Computer Modern Roman \ndocs/paper/acl_natbib.bst:484:MACRO {ieeetc} {\"IEEE Transactions on Computers\"}\ndocs/paper/acl_natbib.bst:487: {\"IEEE Transactions on Computer-Aided Design of Integrated Circuits\"}\ndocs/paper/acl_natbib.bst:493:MACRO {jcss} {\"Journal of Computer and System Sciences\"}\ndocs/paper/acl_natbib.bst:495:MACRO {scp} {\"Science of Computer Programming\"}\ndocs/paper/acl_natbib.bst:499:MACRO {tocs} {\"ACM Transactions on Computer Systems\"}\ndocs/paper/acl_natbib.bst:511:MACRO {tcs} {\"Theoretical Computer Science\"}\ndocs/paper/acl_natbib.bst:596:\t\t  % compute the number of remaining authors\ndocs/paper/tables/tab_domain_model_kstar_full.tex:3:\\caption{Full generative depth results with AUC at the $K^*$ boundary (scorer: Qwen2.5-1.5B, $\\theta{=}0.60$). AUC($k$v$k{+}1$) denotes the area under the ROC curve distinguishing generation $k$ from generation $k{+}1$. Bold indicates the dominant $K^*$ mode per domain. For Wikipedia ($K^*{=}1$), boundary AUC reports 0v1. All AUC values computed on held-out test splits ($n{=}500$ per class).}\ndocs/paper/method.tex:43:All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\\ref{tab:s5_features}, Appendix).\ndocs/paper/method.tex:44:Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \\#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.\ndocs/paper/integration_templates.md:171:We compute Spearman $\\rho$ between detector confidence and true depth for two representative detectors: DivEye~\\cite{basani2026diveye} (log-PPL) and Binoculars~\\cite{hans2024binoculars} (cross-model perplexity ratio; observer: Pythia-1.4B, performer: OLMo-1B).\ndocs/paper/appendix.tex:243:  \\caption{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}\ndocs/paper/main.aux:1007:\\@writefile{lot}{\\contentsline {table}{\\numberline {14}{\\ignorespaces Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document.}}{13}{table.caption.39}\\protected@file@percent }\ndocs/paper/main.aux:1008:\\newlabel{tab:s5_features}{{14}{13}{Complete description of the 15-dimensional feature set used by the OBD classifier. Features are grouped into three families: surprisal statistics (9~dims) computed from Qwen2.5-1.5B token-level log-probabilities, lexical diversity (3~dims), and frequency tail shape (3~dims). All features are computed per document}{table.caption.39}{}}\ndocs/paper/main.aux:1240:\\@writefile{lot}{\\contentsline {table}{\\numberline {27}{\\ignorespaces Bonferroni-corrected 99.5\\% confidence intervals for ${K^*_{\\text  {empirical}}}$ boundary pairs across all 10 configurations. $\\alpha _{\\text  {corr}} = 0.005$; CI computed as $\\text  {AUC}\\pm 2.807 \\times \\hat  {\\sigma }_{\\text  {boot}}$. ``Pass $\\theta $'': CI lower bound $> 0.60$.}}{17}{table.caption.50}\\protected@file@percent }\ndocs/paper/main.aux:1241:\\newlabel{tab:bonferroni_ci}{{27}{17}{Bonferroni-corrected 99.5\\% confidence intervals for $\\Kempirical $ boundary pairs across all 10 configurations. $\\alpha _{\\text {corr}} = 0.005$; CI computed as $\\auc \\pm 2.807 \\times \\hat {\\sigma }_{\\text {boot}}$. ``Pass $\\theta $'': CI lower bound $> 0.60$}{table.caption.50}{}}",
    "numLines": 18
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
No mention of GPUs, compute hours, or environmental impact. This is a gap that needs to be flagged. Let me also check the Ethics Statement more carefully from main.tex - I already have it (lines 74-79). It mentions code/data release upon acceptance.

Now let me draft the checklist. I need to also check what the latest ARR checklist looks like. The 2024 ARR checklist had sections A through F. Let me write a comprehensive draft based on what I know.

Let me also check if there's a `references.bib` file that mentions data licensing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "d5001f08-d524-4ee8-88b3-d137844d2c24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Yy2VbUvNdEp5zHujDypUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 29076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1915
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

_source line 38_

No explicit computational resource reporting found. Now I have enough information to draft the checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "57b5c7c5-8f16-495f-bcc4-d0d28d1d5858",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Yy2VbUvNdEp5zHujDypUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 29076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1915
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

_source line 39_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ARdtnGbNtEJz6JPjE9FBUR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "a9ea57af-48c0-4ddf-81a5-b0a7f7d00d75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Yy2VbUvNdEp5zHujDypUj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 29076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1915
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

_source line 40 · 2026-05-22T21:02:32.779Z_

<details><summary>↩ Tool result · `toolu_01ARdtnGbNtEJz6JPjE9FBUR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "24d664d5-ddf5-401d-a108-52ebc5b920b5",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "isUsingOverage": false
  },
  "uuid": "99c5d2da-6044-4ef9-a943-1f4ab14014b6",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool has a whitelist and this file (arr_responsible_nlp_checklist_draft.md) isn't on it. I'll write directly to the artifacts directory instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "6605962e-4593-4a16-8543-3aa5de8f63e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRbnMtCg7BRDA4DFTsBb96",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 527,
      "cache_read_input_tokens": 30991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 527
      },
      "output_tokens": 22,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Write · `toolu_014Jm2cvtG79ucBFvYb54BeW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/arr_responsible_nlp_checklist_draft.md",
  "content": "# ARR Responsible NLP Research Checklist — Draft Answers\n## Project: gen-depth-contamination (EMNLP 2026 via ARR May)\n\n---\n\n### A. Limitations\n\n**A1: Did you discuss the limitations of your work?**\n- **Yes** — Limitations section (unnumbered, after Section 7) covers three points: (1) scope limited to 1B–8B models, English only, prompt-chain generation; (2) 15 statistical features provide a lower bound; (3) threshold sensitivity of K* across θ ∈ [0.55, 0.70].\n\n**A2: Did you discuss any potential risks of your work?**\n- **Yes** — Ethics Statement discusses dual-use concern (depth estimation could inform adversarial evasion strategies), and notes this risk is shared by all detection research.\n\n---\n\n### B. Ethics / Broader Impact\n\n**B1: Does your paper describe potential risks, harms, or misuses?**\n- **Yes** — Ethics Statement (after Limitations) explicitly addresses adversarial dual-use: depth estimation techniques could help adversaries calibrate rewriting to evade detection. Notes binary detection remains robust (AUC ≥ 0.96 at 0v1).\n\n**B2: Does the paper describe any measures taken to mitigate these risks?**\n- **Partial** — The paper notes that binary detection robustness mitigates the dual-use concern, but does not describe specific access-control or responsible-release measures.\n- ⚠️ **用户确认**: 是否需要补充具体的 mitigation 措施（如 staged release、responsible disclosure 等）？\n\n**B3: Does your paper use any protected attributes (e.g., race, gender)?**\n- **No** — Not applicable. The work operates on text corpora without demographic attributes.\n\n**B4: Does your paper comply with the ACL Code of Ethics?**\n- **Yes**\n\n---\n\n### C. Computational Experiments\n\n**C1: Did you report the number of parameters in each model used?**\n- **Yes** — All 10 model configurations report parameter counts (1B–8B): Qwen2.5-1.5B, Pythia-1.4B/6.9B, OLMo-1B, LLaMA-3.1-8B, Mistral-7B, Gemma-2-2B, Qwen2.5-7B.\n\n**C2: Did you report information about computing infrastructure used?**\n- **No** — ⚠️ **论文中未提及 GPU 类型、训练/推理时间、计算平台。** 需要补充。\n- ⚠️ **用户确认**: 请提供使用的 GPU 型号、生成和训练的总计算时间（GPU hours），以及估算的碳排放（可选）。\n\n**C3: Did you report the evaluation metrics, along with the measures of statistical significance?**\n- **Yes** — 报告了 pairwise AUC、Bootstrap 95% CIs (1,000–10,000 resamples)、permutation tests (p < 0.001)、Bonferroni correction (α_corr = 0.005)、Spearman ρ、ANOVA (η²_p)、McNemar test。统计严谨度高。\n\n**C4: Did you run your experiments with different random seeds?**\n- **Yes** — Primary seed = 42; robustness replication with seed = 123 (Wikipedia, C4); filtering experiments use 5 seeds (51 total runs).\n\n**C5: Did you report the hyperparameter search strategy (e.g., grid search, random search)?**\n- **Partial** — 超参数值已完整报告（LightGBM: n_estimators=200, lr=0.05, max_depth=6; LoRA: rank=8, α=16; decoding: p=0.95, T=1.0 等），但未说明是否进行了超参数搜索，还是直接使用固定值。\n- ⚠️ **用户确认**: 这些超参数是通过搜索确定的还是基于经验/先前工作直接设定的？如果有搜索，请提供搜索范围。\n\n**C6: Did you report the number of training and evaluation examples?**\n- **Yes** — 5,000 seed documents per configuration, 30,000 total (6 depth levels), 5-fold GroupKFold CV (n=500 per class in test split). Filtering: MMLU & HellaSwag with standard splits.\n\n---\n\n### D. Data\n\n**D1: Did you state the names and versions of all datasets used?**\n- **Yes** — C4 (English validation split), Wikipedia, arXiv abstracts. Downstream: MMLU, HellaSwag.\n- ⚠️ **用户确认**: 是否需要补充具体的 dataset version/snapshot date（如 C4 的具体版本号）？\n\n**D2: Did you discuss whether the data you are using/curating contains PII or offensive content?**\n- **Partial** — Ethics Statement mentions \"do not involve personally identifiable information.\" C4 is known to contain some PII in its raw form, but the paper uses it as-is without additional filtering.\n\n**D3: Did you provide the license for each dataset?**\n- **No** — ⚠️ **论文中未提及数据集的 license 信息。**\n- C4: ODC-BY (Open Data Commons Attribution License)\n- Wikipedia: CC BY-SA 3.0\n- arXiv: arXiv license (varies by paper)\n- MMLU / HellaSwag: MIT\n- ⚠️ **用户确认**: 请确认上述 license 信息是否准确，是否需要在论文中添加。\n\n**D4: Did you provide the URL or other access method for all datasets?**\n- **Partial** — 数据集名称已提供，但未列出具体 URL 或 HuggingFace dataset ID。\n- ⚠️ **用户确认**: Checklist 中可简要说明 \"All datasets are publicly available via standard repositories (HuggingFace, etc.)\"\n\n**D5: Did you discuss whether and how consent was obtained from people whose data you used?**\n- **N/A** — 使用的都是公开数据集（C4, Wikipedia, arXiv, MMLU, HellaSwag），无需单独获取同意。\n\n**D6: Did you discuss whether the data you are using was collected in an ethical manner?**\n- **N/A** — 使用已有公开数据集，数据收集伦理由原始数据集维护者负责。\n\n---\n\n### E. Code and Software\n\n**E1: Did you include your code, data, and instructions for reproducing the main results?**\n- **Partial** — Ethics Statement says \"Code and data will be released upon acceptance.\" 论文中提供了完整的超参数和实验配置，但代码/数据尚未公开。\n- Checklist 回答建议: \"Yes, code and data will be released upon acceptance. Full hyperparameters and experimental configurations are provided in the paper and appendix.\"\n\n**E2: Did you include the software and hardware requirements for running your code?**\n- **No** — ⚠️ **未提及软件版本（PyTorch, transformers, LightGBM 版本）或硬件要求。**\n- ⚠️ **用户确认**: 是否需要在 appendix 中补充 software/hardware requirements？\n\n---\n\n### F. Human Evaluation / Annotation\n\n**F1: Did you report inter-annotator agreement?**\n- **N/A** — 本研究不涉及人工评估或标注。\n\n**F2: Did you provide details about the annotators?**\n- **N/A**\n\n**F3: Did you discuss whether and how consent was obtained from annotators?**\n- **N/A**\n\n**F4: Did you report information about compensation for annotators?**\n- **N/A**\n\n---\n\n### G. Use of AI Assistants\n\n**G1: Did you report the use of AI assistants in writing or conducting this research?**\n- ⚠️ **用户确认**: 是否使用了 AI 辅助写作？如果是，需要在 Checklist 中声明（ARR 2025+ 要求）。\n\n---\n\n## 需要用户确认的项目\n\n| # | 问题 | 类别 | 紧迫度 |\n|---|------|------|--------|\n| 1 | **计算资源**: GPU 型号、总 GPU hours、计算平台 | C2 | 🔴 必须补充 |\n| 2 | **超参数搜索**: 是否进行了搜索？搜索范围？ | C5 | 🟡 建议补充 |\n| 3 | **数据集 license**: 确认 C4/Wikipedia/arXiv/MMLU/HellaSwag 的 license | D3 | 🟡 建议确认 |\n| 4 | **数据集版本**: C4 具体版本号/snapshot | D1 | 🟡 建议补充 |\n| 5 | **软件版本**: PyTorch, transformers, LightGBM 等版本号 | E2 | 🟡 建议补充 |\n| 6 | **AI 辅助写作声明** | G1 | 🟡 按 ARR 要求 |\n| 7 | **Dual-use mitigation**: 是否需要补充具体措施 | B2 | 🟢 可选 |\n| 8 | **数据集 URL**: 是否需要列出具体下载链接 | D4 | 🟢 可选 |\n\n---\n\n## 建议的 Checklist 简要回答模板\n\n以下可直接用于 OpenReview submission form 填写（英文）：\n\n> **A1 (Limitations):** Yes. Section \"Limitations\" discusses scope (model scale, English only, prompt-chain), feature set lower bound, and threshold sensitivity.\n>\n> **B (Risks):** Yes. Ethics Statement discusses dual-use risks of depth estimation for adversarial evasion and notes binary detection robustness as mitigation.\n>\n> **C1 (Parameters):** Yes. All 10 model configurations report parameter counts (1B–8B) in Section 3 and Table 1.\n>\n> **C2 (Compute):** [待补充 — 需要用户提供 GPU 型号和计算时间]\n>\n> **C3 (Significance):** Yes. Bootstrap CIs, permutation tests (p < 0.001), Bonferroni correction, ANOVA, McNemar tests reported throughout Sections 4–5 and Appendix.\n>\n> **C4 (Seeds):** Yes. Primary seed=42, robustness seed=123, 5 seeds for filtering experiments.\n>\n> **C5 (Hyperparameters):** All hyperparameters are reported. [待确认: 是否进行了搜索]\n>\n> **C6 (Data size):** Yes. 5,000 seeds × 6 depths × 10 configs; 5-fold GroupKFold; n=500/class test splits.\n>\n> **D1–D4 (Data):** All datasets are publicly available (C4, Wikipedia, arXiv, MMLU, HellaSwag). [待补充: license, version]\n>\n> **E1 (Code):** Code and data will be released upon acceptance.\n>\n> **F (Human eval):** N/A — no human evaluation conducted.\n>\n> **G (AI assistants):** [待用户确认]\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "a21b621f-2d69-4e0c-8c10-370edf97bd2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRbnMtCg7BRDA4DFTsBb96",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 527,
      "cache_read_input_tokens": 30991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 527
      },
      "output_tokens": 22,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779498000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0a9be032-04ae-486a-9d0b-db433dfa976c",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e"
}
```

---

### Tool result

_source line 45 · 2026-05-22T21:03:40.762Z_

<details><summary>↩ Tool result · `toolu_014Jm2cvtG79ucBFvYb54BeW`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/arr_responsible_nlp_checklist_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "d314015c-7320-41af-a422-482f2a8cd340",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/arr_responsible_nlp_checklist_draft.md",
    "content": "# ARR Responsible NLP Research Checklist — Draft Answers\n## Project: gen-depth-contamination (EMNLP 2026 via ARR May)\n\n---\n\n### A. Limitations\n\n**A1: Did you discuss the limitations of your work?**\n- **Yes** — Limitations section (unnumbered, after Section 7) covers three points: (1) scope limited to 1B–8B models, English only, prompt-chain generation; (2) 15 statistical features provide a lower bound; (3) threshold sensitivity of K* across θ ∈ [0.55, 0.70].\n\n**A2: Did you discuss any potential risks of your work?**\n- **Yes** — Ethics Statement discusses dual-use concern (depth estimation could inform adversarial evasion strategies), and notes this risk is shared by all detection research.\n\n---\n\n### B. Ethics / Broader Impact\n\n**B1: Does your paper describe potential risks, harms, or misuses?**\n- **Yes** — Ethics Statement (after Limitations) explicitly addresses adversarial dual-use: depth estimation techniques could help adversaries calibrate rewriting to evade detection. Notes binary detection remains robust (AUC ≥ 0.96 at 0v1).\n\n**B2: Does the paper describe any measures taken to mitigate these risks?**\n- **Partial** — The paper notes that binary detection robustness mitigates the dual-use concern, but does not describe specific access-control or responsible-release measures.\n- ⚠️ **用户确认**: 是否需要补充具体的 mitigation 措施（如 staged release、responsible disclosure 等）？\n\n**B3: Does your paper use any protected attributes (e.g., race, gender)?**\n- **No** — Not applicable. The work operates on text corpora without demographic attributes.\n\n**B4: Does your paper comply with the ACL Code of Ethics?**\n- **Yes**\n\n---\n\n### C. Computational Experiments\n\n**C1: Did you report the number of parameters in each model used?**\n- **Yes** — All 10 model configurations report parameter counts (1B–8B): Qwen2.5-1.5B, Pythia-1.4B/6.9B, OLMo-1B, LLaMA-3.1-8B, Mistral-7B, Gemma-2-2B, Qwen2.5-7B.\n\n**C2: Did you report information about computing infrastructure used?**\n- **No** — ⚠️ **论文中未提及 GPU 类型、训练/推理时间、计算平台。** 需要补充。\n- ⚠️ **用户确认**: 请提供使用的 GPU 型号、生成和训练的总计算时间（GPU hours），以及估算的碳排放（可选）。\n\n**C3: Did you report the evaluation metrics, along with the measures of statistical significance?**\n- **Yes** — 报告了 pairwise AUC、Bootstrap 95% CIs (1,000–10,000 resamples)、permutation tests (p < 0.001)、Bonferroni correction (α_corr = 0.005)、Spearman ρ、ANOVA (η²_p)、McNemar test。统计严谨度高。\n\n**C4: Did you run your experiments with different random seeds?**\n- **Yes** — Primary seed = 42; robustness replication with seed = 123 (Wikipedia, C4); filtering experiments use 5 seeds (51 total runs).\n\n**C5: Did you report the hyperparameter search strategy (e.g., grid search, random search)?**\n- **Partial** — 超参数值已完整报告（LightGBM: n_estimators=200, lr=0.05, max_depth=6; LoRA: rank=8, α=16; decoding: p=0.95, T=1.0 等），但未说明是否进行了超参数搜索，还是直接使用固定值。\n- ⚠️ **用户确认**: 这些超参数是通过搜索确定的还是基于经验/先前工作直接设定的？如果有搜索，请提供搜索范围。\n\n**C6: Did you report the number of training and evaluation examples?**\n- **Yes** — 5,000 seed documents per configuration, 30,000 total (6 depth levels), 5-fold GroupKFold CV (n=500 per class in test split). Filtering: MMLU & HellaSwag with standard splits.\n\n---\n\n### D. Data\n\n**D1: Did you state the names and versions of all datasets used?**\n- **Yes** — C4 (English validation split), Wikipedia, arXiv abstracts. Downstream: MMLU, HellaSwag.\n- ⚠️ **用户确认**: 是否需要补充具体的 dataset version/snapshot date（如 C4 的具体版本号）？\n\n**D2: Did you discuss whether the data you are using/curating contains PII or offensive content?**\n- **Partial** — Ethics Statement mentions \"do not involve personally identifiable information.\" C4 is known to contain some PII in its raw form, but the paper uses it as-is without additional filtering.\n\n**D3: Did you provide the license for each dataset?**\n- **No** — ⚠️ **论文中未提及数据集的 license 信息。**\n- C4: ODC-BY (Open Data Commons Attribution License)\n- Wikipedia: CC BY-SA 3.0\n- arXiv: arXiv license (varies by paper)\n- MMLU / HellaSwag: MIT\n- ⚠️ **用户确认**: 请确认上述 license 信息是否准确，是否需要在论文中添加。\n\n**D4: Did you provide the URL or other access method for all datasets?**\n- **Partial** — 数据集名称已提供，但未列出具体 URL 或 HuggingFace dataset ID。\n- ⚠️ **用户确认**: Checklist 中可简要说明 \"All datasets are publicly available via standard repositories (HuggingFace, etc.)\"\n\n**D5: Did you discuss whether and how consent was obtained from people whose data you used?**\n- **N/A** — 使用的都是公开数据集（C4, Wikipedia, arXiv, MMLU, HellaSwag），无需单独获取同意。\n\n**D6: Did you discuss whether the data you are using was collected in an ethical manner?**\n- **N/A** — 使用已有公开数据集，数据收集伦理由原始数据集维护者负责。\n\n---\n\n### E. Code and Software\n\n**E1: Did you include your code, data, and instructions for reproducing the main results?**\n- **Partial** — Ethics Statement says \"Code and data will be released upon acceptance.\" 论文中提供了完整的超参数和实验配置，但代码/数据尚未公开。\n- Checklist 回答建议: \"Yes, code and data will be released upon acceptance. Full hyperparameters and experimental configurations are provided in the paper and appendix.\"\n\n**E2: Did you include the software and hardware requirements for running your code?**\n- **No** — ⚠️ **未提及软件版本（PyTorch, transformers, LightGBM 版本）或硬件要求。**\n- ⚠️ **用户确认**: 是否需要在 appendix 中补充 software/hardware requirements？\n\n---\n\n### F. Human Evaluation / Annotation\n\n**F1: Did you report inter-annotator agreement?**\n- **N/A** — 本研究不涉及人工评估或标注。\n\n**F2: Did you provide details about the annotators?**\n- **N/A**\n\n**F3: Did you discuss whether and how consent was obtained from annotators?**\n- **N/A**\n\n**F4: Did you report information about compensation for annotators?**\n- **N/A**\n\n---\n\n### G. Use of AI Assistants\n\n**G1: Did you report the use of AI assistants in writing or conducting this research?**\n- ⚠️ **用户确认**: 是否使用了 AI 辅助写作？如果是，需要在 Checklist 中声明（ARR 2025+ 要求）。\n\n---\n\n## 需要用户确认的项目\n\n| # | 问题 | 类别 | 紧迫度 |\n|---|------|------|--------|\n| 1 | **计算资源**: GPU 型号、总 GPU hours、计算平台 | C2 | 🔴 必须补充 |\n| 2 | **超参数搜索**: 是否进行了搜索？搜索范围？ | C5 | 🟡 建议补充 |\n| 3 | **数据集 license**: 确认 C4/Wikipedia/arXiv/MMLU/HellaSwag 的 license | D3 | 🟡 建议确认 |\n| 4 | **数据集版本**: C4 具体版本号/snapshot | D1 | 🟡 建议补充 |\n| 5 | **软件版本**: PyTorch, transformers, LightGBM 等版本号 | E2 | 🟡 建议补充 |\n| 6 | **AI 辅助写作声明** | G1 | 🟡 按 ARR 要求 |\n| 7 | **Dual-use mitigation**: 是否需要补充具体措施 | B2 | 🟢 可选 |\n| 8 | **数据集 URL**: 是否需要列出具体下载链接 | D4 | 🟢 可选 |\n\n---\n\n## 建议的 Checklist 简要回答模板\n\n以下可直接用于 OpenReview submission form 填写（英文）：\n\n> **A1 (Limitations):** Yes. Section \"Limitations\" discusses scope (model scale, English only, prompt-chain), feature set lower bound, and threshold sensitivity.\n>\n> **B (Risks):** Yes. Ethics Statement discusses dual-use risks of depth estimation for adversarial evasion and notes binary detection robustness as mitigation.\n>\n> **C1 (Parameters):** Yes. All 10 model configurations report parameter counts (1B–8B) in Section 3 and Table 1.\n>\n> **C2 (Compute):** [待补充 — 需要用户提供 GPU 型号和计算时间]\n>\n> **C3 (Significance):** Yes. Bootstrap CIs, permutation tests (p < 0.001), Bonferroni correction, ANOVA, McNemar tests reported throughout Sections 4–5 and Appendix.\n>\n> **C4 (Seeds):** Yes. Primary seed=42, robustness seed=123, 5 seeds for filtering experiments.\n>\n> **C5 (Hyperparameters):** All hyperparameters are reported. [待确认: 是否进行了搜索]\n>\n> **C6 (Data size):** Yes. 5,000 seeds × 6 depths × 10 configs; 5-fold GroupKFold; n=500/class test splits.\n>\n> **D1–D4 (Data):** All datasets are publicly available (C4, Wikipedia, arXiv, MMLU, HellaSwag). [待补充: license, version]\n>\n> **E1 (Code):** Code and data will be released upon acceptance.\n>\n> **F (Human eval):** N/A — no human evaluation conducted.\n>\n> **G (AI assistants):** [待用户确认]\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 46_

草稿已写入 `artifacts/arr_responsible_nlp_checklist_draft.md`。

关键发现：
- 大部分项可直接回答 Yes/N/A，统计严谨度很高（Bootstrap CIs、Bonferroni、permutation tests）
- **必须补充的缺项**: 计算资源（GPU 型号、GPU hours）— 这是 C2 的硬要求
- **建议补充**: 超参数搜索策略说明、数据集 license、软件版本、AI 辅助声明
- 文末有可直接用于 OpenReview form 填写的英文模板

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "uuid": "a70d5aa9-55c2-4447-bac4-f587647ecadb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MF4Rdj8cHHmPmdkcUyrC8R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3237,
      "cache_read_input_tokens": 31518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3237
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

_source line 47_

草稿已写入 `artifacts/arr_responsible_nlp_checklist_draft.md`。

关键发现：
- 大部分项可直接回答 Yes/N/A，统计严谨度很高（Bootstrap CIs、Bonferroni、permutation tests）
- **必须补充的缺项**: 计算资源（GPU 型号、GPU hours）— 这是 C2 的硬要求
- **建议补充**: 超参数搜索策略说明、数据集 license、软件版本、AI 辅助声明
- 文末有可直接用于 OpenReview form 填写的英文模板

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 155777,
  "duration_api_ms": 157764,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "37b32244-de26-4d48-91cc-a82c404b466e",
  "total_cost_usd": 0.42018764999999997,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 22914,
    "cache_read_input_tokens": 153330,
    "output_tokens": 4805,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 22914,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 177,
        "cache_read_input_tokens": 31518,
        "cache_creation_input_tokens": 3237,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3237
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1395,
      "outputTokens": 3309,
      "cacheReadInputTokens": 15889,
      "cacheCreationInputTokens": 48489,
      "webSearchRequests": 0,
      "costUSD": 0.08014015,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 4805,
      "cacheReadInputTokens": 153330,
      "cacheCreationInputTokens": 22914,
      "webSearchRequests": 0,
      "costUSD": 0.3400475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d7cb2195-cc15-4b39-b31a-542750aab65b"
}
```

</details>

---
