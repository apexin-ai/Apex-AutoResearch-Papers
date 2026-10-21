# code paper data consistency fix

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 130
- **Recorded user turns:** 0
- **Tool calls:** 51
- **Original source:** `logs/workers/worker_code_paper-data-consistency-fix_20260525T154916.log`
- **Structured JSON:** [`5a6622d6bbb06f940447.json`](../../sessions/5a/5a6622d6bbb06f940447.json)

## Before a recorded user message

130 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
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
  "uuid": "388be25b-6500-40ec-b604-458d0da66967",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-prod42-projects-clkc-mech-interp/memory/"
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
    "resetsAt": 1779731400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3e307843-8652-4451-8c08-dd4733783d29",
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper files to understand the current state, then systematically fix each issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "9cb5f2cd-0013-4147-ad92-3b4af9744652",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F6NbsWw1PjQ1MfPoTN15A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13112,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13112
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

开始修复论文数据一致性问题。先读取所有相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "9f855134-8029-46e2-8ad9-6340e558bf4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F6NbsWw1PjQ1MfPoTN15A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13112,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13112
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01X9mhUevgq6H9MCBBpoVoZp`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "eaef2359-57ae-49ed-84fb-e90e3842a95f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F6NbsWw1PjQ1MfPoTN15A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13112,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13112
      },
      "output_tokens": 27,
      "service_tier": "standard",
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

_source line 7 · 2026-05-25T15:49:29.903Z_

<details><summary>↩ Tool result · `toolu_01X9mhUevgq6H9MCBBpoVoZp`</summary>

```text
docs/paper/acl_latex.tex
docs/paper/related_work.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/main.tex
docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "8fd81d0f-51ac-49fd-8929-bfaed57fec63",
  "tool_use_result": {
    "filenames": [
      "docs/paper/acl_latex.tex",
      "docs/paper/related_work.tex",
      "docs/paper/limitations.tex",
      "docs/paper/abstract.tex",
      "docs/paper/method.tex",
      "docs/paper/discussion.tex",
      "docs/paper/introduction.tex",
      "docs/paper/experiments.tex",
      "docs/paper/main.tex",
      "docs/paper/conclusion.tex"
    ],
    "durationMs": 12,
    "numFiles": 10,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01HRL4SaKCizBeKrHFFMQWMy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "f50d6e24-6f3b-498c-bf77-234174556d9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWsbAPRFNfHssGoCGx44J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 24953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 9 · 2026-05-25T15:49:32.901Z_

<details><summary>↩ Tool result · `toolu_01HRL4SaKCizBeKrHFFMQWMy`</summary>

```text
1	When multilingual large language models (LLMs) encounter conflicting information between languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, and does detectability imply causal influence on resolution? We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English (EN)--Chinese (ZH) conflicts. Our analysis combines cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across English and Chinese, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in magnitude and direction, consistent with the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\% depth), but representation steering achieves causal influence only at a mid-layer (41\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\footnote{Code and data are available at \url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "aef63329-58b8-407f-aa3e-a1f0486e2443",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex",
      "content": "When multilingual large language models (LLMs) encounter conflicting information between languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, and does detectability imply causal influence on resolution? We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English (EN)--Chinese (ZH) conflicts. Our analysis combines cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across English and Chinese, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in magnitude and direction, consistent with the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\\% depth), but representation steering achieves causal influence only at a mid-layer (41\\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01TaYbLEkorPxkNcZd5uHj72`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "d34e40a3-4780-4df3-a52e-9c72bb992f7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWsbAPRFNfHssGoCGx44J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 24953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 11 · 2026-05-25T15:49:33.231Z_

<details><summary>↩ Tool result · `toolu_01TaYbLEkorPxkNcZd5uHj72`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that knowledge conflict signals in multilingual LLMs are linearly detectable across English and Chinese ($p < 0.001$, three architectures), with the ZH$\to$EN transfer advantage (${\sim}$7~pp) matching the XNLI baseline, indicating general cross-lingual alignment rather than conflict-specific encoding.
5	In Llama, a three-way dissociation---linear peak (L28), MLP peak (L18), causal node (L13; $p = 0.002$)---reveals that detection and causation occupy distinct layers; steering fails in Qwen and Gemma despite 88.9\% accuracy, confirming detection alone is insufficient for mechanistic claims.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "3e94231f-e842-46d4-af24-79f10509c286",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that knowledge conflict signals in multilingual LLMs are linearly detectable across English and Chinese ($p < 0.001$, three architectures), with the ZH$\\to$EN transfer advantage (${\\sim}$7~pp) matching the XNLI baseline, indicating general cross-lingual alignment rather than conflict-specific encoding.\nIn Llama, a three-way dissociation---linear peak (L28), MLP peak (L18), causal node (L13; $p = 0.002$)---reveals that detection and causation occupy distinct layers; steering fails in Qwen and Gemma despite 88.9\\% accuracy, confirming detection alone is insufficient for mechanistic claims.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01BAfPbEWEoc5J5rGTRU8FHN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "e671a0d7-ec92-46c7-9057-a6cf278d47d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARWsbAPRFNfHssGoCGx44J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 24953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 256
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

_source line 13 · 2026-05-25T15:49:33.486Z_

<details><summary>↩ Tool result · `toolu_01BAfPbEWEoc5J5rGTRU8FHN`</summary>

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
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{subcaption}
16	
17	\title{English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries}
18	
19	\author{Anonymous ACL submission}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	
30	\input{related_work}
31	
32	\input{method}
33	
34	\input{experiments}
35	
36	\input{discussion}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\appendix
45	
46	\section{Use of AI Assistants}
47	\label{app:ai-assistants}
48	
49	We used Claude (Anthropic) as an AI coding and writing assistant
50	throughout this work. Specifically:
51	\begin{itemize}
52	    \item \textbf{Code:} drafting experiment scripts, data-processing
53	    pipelines, and analysis utilities; debugging and refactoring.
54	    \item \textbf{Writing:} drafting and revising paper sections,
55	    polishing prose, and reformatting \LaTeX{}.
56	    \item \textbf{Literature:} summarizing related papers to inform
57	    related-work section.
58	\end{itemize}
59	
60	\section{Fine-Grained Causal Boundary Analysis}
61	\label{app:boundary}
62	
63	Table~\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).
64	
65	\begin{table}[!t]
66	\centering
67	\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\ Sig.\ $\alpha$s: number of $\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}
68	\label{tab:boundary}
69	\small
70	\resizebox{\columnwidth}{!}{%
71	\begin{tabular}{lcccccc}
72	\toprule
73	Layer & Depth & Probe Acc & Best $\alpha$ & Best Fisher $p$ & Bonf.\ Sig.\ $\alpha$s & Result \\
74	\midrule
75	L12 & 38\% & 91.75\% & $+20$ & 0.085 & 0/6 & --- \\
76	\textbf{L13} & \textbf{41\%} & \textbf{90.00\%} & $\mathbf{+10}$ & $\mathbf{<0.001}$ & \textbf{2/6} & $\checkmark\checkmark$ \\
77	L14 & 44\% & 91.75\% & $+10$ & 0.002 & 1/6 & $\checkmark$ \\
78	L16 & 50\% & 91.50\% & $+10$ & 0.005 & 1/6 & $\checkmark$ \\
79	L18 & 56\% & 90.75\% & $+5$ & 0.010 & 0/6 & --- \\
80	L28 & 88\% & 85.25\% & $+10$ & 0.284 & 0/6 & --- \\
81	\bottomrule
82	\end{tabular}%
83	}
84	\end{table}
85	
86	\section{Seed Replication of L13 Steering}
87	\label{app:seed_replication}
88	
89	To verify that the L13 causal effect is not an artifact of a specific train/test split, we repeated the Llama L13 steering experiment with an independently trained probe (seed=123, different train/test split).
90	The causal effect replicates in the positive direction: $\alpha = +5$ ($p = 0.003$), $\alpha = +10$ ($p = 0.0003$), with 2 of 6 configurations surviving Bonferroni correction (matching the original 2/6).
91	The consistent positive-direction effect across independent probe training confirms that L13 causal localization is not an artifact of a specific train/test split.
92	
93	\section{Detection--Decision Dissociation}
94	\label{app:dissociation}
95	
96	\begin{figure}[!t]
97	\centering
98	\includegraphics[width=\columnwidth]{fig6_dissociation.pdf}
99	\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L28, 88\% depth), MLP probe peak (L18, 56\%), and causal steering node (L13, 41\%) occupy distinct layers, revealing a three-way dissociation. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}
100	\label{fig:dissociation}
101	\end{figure}
102	
103	\section{AUROC Analysis}
104	\label{app:auroc}
105	
106	Table~\ref{tab:auroc} reports AUROC for conflict probes on matched-condition replication data ($N = 131$--$201$), confirming strong continuous discriminative capacity across models.
107	Gemma's 0.93 EN$\to$EN AUROC (the highest among all models for this metric), paired with zero directional flips under steering, provides the strongest evidence that detection and causal influence are dissociable.
108	
109	\begin{table}[!t]
110	\centering
111	\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}
112	\label{tab:auroc}
113	\small
114	\begin{tabular}{llcc}
115	\toprule
116	Model & Direction & AUROC & Bal.\ Acc (\%) \\
117	\midrule
118	Llama-3.1-8B & EN$\to$EN & 0.981 & 92.7 \\
119	\midrule
120	Gemma-2-9B-IT & EN$\to$EN & 0.931 & 88.1 \\
121	Gemma-2-9B-IT & ZH$\to$ZH & 0.900 & 85.7 \\
122	Gemma-2-9B-IT & EN$\to$ZH & 0.852 & 75.1 \\
123	Gemma-2-9B-IT & ZH$\to$EN & 0.921 & 77.8 \\
124	\midrule
125	Qwen3-8B & EN$\to$EN & 0.771 & 71.4 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	\section{Matched-Condition Steering Results}
131	\label{app:steering_config}
132	
133	Table~\ref{tab:steering_config} reports steering results under matched conditions: all three architectures are tested at comparable relative depths (${\sim}$36--43\%) using the same probe training methodology and six $\alpha$ values in $[-20, +20]$.
134	Despite the highest probe accuracy among the three models (88--89\%), Gemma produces zero directional flips, ruling out probe quality as a confound for the Llama-specific positive result.
135	The full Llama causal gradient ($N = 201$) is in Appendix~\ref{app:boundary}.
136	
137	\begin{table}[!t]
138	\centering
139	\caption{Matched-condition steering results. Probe: EN$\to$EN balanced accuracy at the target layer. Best $p$: minimum Fisher exact $p$-value across six tested $\alpha$ values. Bonf.: $\alpha$ values surviving Bonferroni correction out of 6. Flips: total directional transitions (p$\to$c $+$ c$\to$p).$^{\dagger}$}
140	\label{tab:steering_config}
141	\small
142	\begin{tabular}{lcrccc}
143	\toprule
144	Layer & Depth & Probe (\%) & Best $p$ & Bonf. & Flips \\
145	\midrule
146	\multicolumn{6}{l}{\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\
147	\textbf{L13} & \textbf{41\%} & \textbf{76.1} & $\mathbf{<0.001}$ & \textbf{2/6} & \textbf{9} \\
148	\midrule
149	\multicolumn{6}{l}{\textit{Qwen3-8B ($N = 131$; 36 layers)}} \\
150	L13 & 36\% & 71.8 & 0.168 & 0/6 & 0 \\
151	L14 & 39\% & 71.0 & 0.785 & 0/6 & 0 \\
152	L15 & 42\% & 72.9 & 0.617 & 0/6 & 0 \\
153	\midrule
154	\multicolumn{6}{l}{\textit{Gemma-2-9B-IT ($N = 171$; 42 layers)$^{\dagger}$}} \\
155	L16 & 38\% & 88.0 & 0.067 & 0/6 & 0 \\
156	L17 & 40\% & 88.9 & 0.448 & 0/6 & 0 \\
157	L18 & 43\% & 89.5 & 0.219 & 0/6 & 0 \\
158	\bottomrule
159	\end{tabular}
160	\begin{flushleft}
161	\footnotesize $^{\dagger}$ Gemma: after correcting a label assignment error.
162	\end{flushleft}
163	\end{table}
164	
165	\end{document}
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "cb438e61-c36e-4fdb-b18c-29fc7e3d8144",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\n\\title{English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n\n\\section{Fine-Grained Causal Boundary Analysis}\n\\label{app:boundary}\n\nTable~\\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).\n\n\\begin{table}[!t]\n\\centering\n\\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\\ Sig.\\ $\\alpha$s: number of $\\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}\n\\label{tab:boundary}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\nLayer & Depth & Probe Acc & Best $\\alpha$ & Best Fisher $p$ & Bonf.\\ Sig.\\ $\\alpha$s & Result \\\\\n\\midrule\nL12 & 38\\% & 91.75\\% & $+20$ & 0.085 & 0/6 & --- \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{90.00\\%} & $\\mathbf{+10}$ & $\\mathbf{<0.001}$ & \\textbf{2/6} & $\\checkmark\\checkmark$ \\\\\nL14 & 44\\% & 91.75\\% & $+10$ & 0.002 & 1/6 & $\\checkmark$ \\\\\nL16 & 50\\% & 91.50\\% & $+10$ & 0.005 & 1/6 & $\\checkmark$ \\\\\nL18 & 56\\% & 90.75\\% & $+5$ & 0.010 & 0/6 & --- \\\\\nL28 & 88\\% & 85.25\\% & $+10$ & 0.284 & 0/6 & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Seed Replication of L13 Steering}\n\\label{app:seed_replication}\n\nTo verify that the L13 causal effect is not an artifact of a specific train/test split, we repeated the Llama L13 steering experiment with an independently trained probe (seed=123, different train/test split).\nThe causal effect replicates in the positive direction: $\\alpha = +5$ ($p = 0.003$), $\\alpha = +10$ ($p = 0.0003$), with 2 of 6 configurations surviving Bonferroni correction (matching the original 2/6).\nThe consistent positive-direction effect across independent probe training confirms that L13 causal localization is not an artifact of a specific train/test split.\n\n\\section{Detection--Decision Dissociation}\n\\label{app:dissociation}\n\n\\begin{figure}[!t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig6_dissociation.pdf}\n\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L28, 88\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) occupy distinct layers, revealing a three-way dissociation. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}\n\\label{fig:dissociation}\n\\end{figure}\n\n\\section{AUROC Analysis}\n\\label{app:auroc}\n\nTable~\\ref{tab:auroc} reports AUROC for conflict probes on matched-condition replication data ($N = 131$--$201$), confirming strong continuous discriminative capacity across models.\nGemma's 0.93 EN$\\to$EN AUROC (the highest among all models for this metric), paired with zero directional flips under steering, provides the strongest evidence that detection and causal influence are dissociable.\n\n\\begin{table}[!t]\n\\centering\n\\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}\n\\label{tab:auroc}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Direction & AUROC & Bal.\\ Acc (\\%) \\\\\n\\midrule\nLlama-3.1-8B & EN$\\to$EN & 0.981 & 92.7 \\\\\n\\midrule\nGemma-2-9B-IT & EN$\\to$EN & 0.931 & 88.1 \\\\\nGemma-2-9B-IT & ZH$\\to$ZH & 0.900 & 85.7 \\\\\nGemma-2-9B-IT & EN$\\to$ZH & 0.852 & 75.1 \\\\\nGemma-2-9B-IT & ZH$\\to$EN & 0.921 & 77.8 \\\\\n\\midrule\nQwen3-8B & EN$\\to$EN & 0.771 & 71.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Matched-Condition Steering Results}\n\\label{app:steering_config}\n\nTable~\\ref{tab:steering_config} reports steering results under matched conditions: all three architectures are tested at comparable relative depths (${\\sim}$36--43\\%) using the same probe training methodology and six $\\alpha$ values in $[-20, +20]$.\nDespite the highest probe accuracy among the three models (88--89\\%), Gemma produces zero directional flips, ruling out probe quality as a confound for the Llama-specific positive result.\nThe full Llama causal gradient ($N = 201$) is in Appendix~\\ref{app:boundary}.\n\n\\begin{table}[!t]\n\\centering\n\\caption{Matched-condition steering results. Probe: EN$\\to$EN balanced accuracy at the target layer. Best $p$: minimum Fisher exact $p$-value across six tested $\\alpha$ values. Bonf.: $\\alpha$ values surviving Bonferroni correction out of 6. Flips: total directional transitions (p$\\to$c $+$ c$\\to$p).$^{\\dagger}$}\n\\label{tab:steering_config}\n\\small\n\\begin{tabular}{lcrccc}\n\\toprule\nLayer & Depth & Probe (\\%) & Best $p$ & Bonf. & Flips \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{76.1} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Qwen3-8B ($N = 131$; 36 layers)}} \\\\\nL13 & 36\\% & 71.8 & 0.168 & 0/6 & 0 \\\\\nL14 & 39\\% & 71.0 & 0.785 & 0/6 & 0 \\\\\nL15 & 42\\% & 72.9 & 0.617 & 0/6 & 0 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Gemma-2-9B-IT ($N = 171$; 42 layers)$^{\\dagger}$}} \\\\\nL16 & 38\\% & 88.0 & 0.067 & 0/6 & 0 \\\\\nL17 & 40\\% & 88.9 & 0.448 & 0/6 & 0 \\\\\nL18 & 43\\% & 89.5 & 0.219 & 0/6 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}\n\n\\end{document}\n",
      "numLines": 166,
      "startLine": 1,
      "totalLines": 166
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
Now I need to read the remaining tex files to check for any other references to L28/88%/p=0.002.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "88f58c6d-e9bb-4efa-80f3-08994a69f1f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hUqFRvydkoCoBhBwWJLCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3825,
      "cache_read_input_tokens": 25209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3825
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

Now let me read the remaining files and search for all problematic references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "f7ce1afb-d2fe-4ffa-83a3-fb39396fc252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hUqFRvydkoCoBhBwWJLCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3825,
      "cache_read_input_tokens": 25209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3825
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

<details open><summary>🔧 Tool call — Read · `toolu_01Fm3hY2asCKuJB4YDhHrA7f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "a7eb0eb1-1a45-4b5b-802d-7951c596571c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hUqFRvydkoCoBhBwWJLCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3825,
      "cache_read_input_tokens": 25209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3825
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

_source line 17 · 2026-05-25T15:49:37.672Z_

<details><summary>↩ Tool result · `toolu_01Fm3hY2asCKuJB4YDhHrA7f`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \citep{team2024gemma}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.
13	The three models were independently verified, yielding only 3.5\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\% (Llama $\cap$ Gemma) to 24.8\% (Gemma $\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.
14	
15	\paragraph{Translation.}
16	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET (wmt22-comet-da; \citealt{rei2020comet}) back-translation scores.
17	
18	\paragraph{Probing.}
19	For each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
20	We report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\ref{app:auroc}.
21	All CIs are computed via bootstrap resampling with paired differences for asymmetry estimation.
22	A selectivity control \citep{hewitt2019designing} with permuted labels on matched-condition data ($N{=}131$--$201$) yields near-chance accuracy (49.2--51.0\%) across all models, confirming selectivity gaps of 21--40~pp.
23	All experiments used a single GPU; the boundary replication (Appendix~\ref{app:boundary}) used an NVIDIA RTX PRO 6000.
24	
25	\paragraph{Non-conflict baseline.}
26	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
27	
28	\subsection{Within-Language Conflict Detection}
29	\label{sec:within_lang}
30	
31	Table~\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.
32	All three models encode linearly detectable conflict signals in their residual streams.
33	Llama achieves 77.6\% on EN$\to$EN (peak at layer 28, 88\% depth) and 72.1\% on ZH$\to$ZH.
34	Qwen reaches 75.0\% on EN$\to$EN (peak at layer 24, 67\% depth) and 72.6\% on ZH$\to$ZH.
35	Gemma attains 76.2\% on EN$\to$EN (peak at layer 24, 57\% depth) and 71.0\% on ZH$\to$ZH.
36	All within-language accuracies are significantly above chance (binomial $p < 0.001$).
37	Figure~\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for all three models.
38	These results confirm that knowledge conflict signals are linearly separable in the residual stream across all three architectures and both languages.
39	
40	%% Figure 2: Layer-wise probe accuracy
41	\begin{figure*}[t]
42	\centering
43	\includegraphics[width=\textwidth]{fig3_layerwise_probes.pdf}
44	\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p = 0.002$), coinciding with the ZH$\to$ZH probe peak but not the EN$\to$EN peak (L28). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}
45	\label{fig:layer_probe}
46	\end{figure*}
47	
48	\subsection{Cross-Lingual Transfer and Asymmetry}
49	\label{sec:cross_lingual}
50	
51	All four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\ref{tab:main_results}); this confirms that conflict representations partially overlap between English and Chinese.
52	All three models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\to$EN) more accurately than the reverse direction (EN$\to$ZH).
53	We define $\Delta_{\text{asym}} = \text{acc}(\text{ZH}{\to}\text{EN}) - \text{acc}(\text{EN}{\to}\text{ZH})$, computed via paired bootstrap.
54	For Llama, $\Delta_{\text{asym}} = +7.3$ percentage points (pp) with a 95\% bootstrap CI of [0.4, 14.0] ($p = 0.038$); for Qwen, $\Delta_{\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7]; for Gemma, $\Delta_{\text{asym}} = +6.6$ pp with CI [1.9, 11.1] ($p = 0.006$).
55	While the Qwen CI marginally includes zero, the asymmetry is consistent in direction across all three architectures.
56	The magnitude of this asymmetry is consistent in direction and magnitude with the XNLI non-conflict baseline across all three architectures (\S\ref{sec:xnli_baseline}), and the consistent direction across all three models suggests a shared structural property rather than a model-specific artifact (Figure~\ref{fig:asymmetry_forest}).
57	
58	\begin{table}[t]
59	\centering
60	\caption{Single-seed balanced accuracy (\%) at each direction's optimal layer. $\Delta_{\text{asym}}$ and 95\% CIs from paired bootstrap ($n = 2{,}000$ resamples). Bold: best per-task direction.}
61	\label{tab:main_results}
62	\small
63	\resizebox{\columnwidth}{!}{%
64	\begin{tabular}{lccc}
65	\toprule
66	Direction & Llama-3.1-8B & Qwen3-8B & Gemma-2-9B \\
67	\midrule
68	\multicolumn{4}{l}{\textit{Conflict Task}} \\
69	EN $\to$ EN & \textbf{77.6} & \textbf{75.0} & \textbf{76.2} \\
70	ZH $\to$ ZH & 72.1 & 72.6 & 71.0 \\
71	EN $\to$ ZH & 59.6 & 67.3 & 62.9 \\
72	ZH $\to$ EN & 70.6 & 73.2 & 70.2 \\
73	$\Delta_{\text{asym}}$ & +7.3 [0.4, 14.0] & +7.2 [$-$0.6, 13.7] & +6.6 [1.9, 11.1] \\
74	\midrule
75	\multicolumn{4}{l}{\textit{XNLI Baseline}} \\
76	EN $\to$ EN & 94.0 & 96.6 & 95.6 \\
77	ZH $\to$ ZH & 87.5 & 89.5 & 89.0 \\
78	EN $\to$ ZH & 89.0 & 90.5 & 89.4 \\
79	ZH $\to$ EN & \textbf{94.9} & \textbf{97.2} & \textbf{97.5} \\
80	$\Delta_{\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] & +7.8 [5.7, 10.0] \\
81	\bottomrule
82	\end{tabular}%
83	}
84	\begin{flushleft}
85	\footnotesize Note: $\Delta_{\text{asym}}$ is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies.
86	\end{flushleft}
87	\end{table}
88	
89	\subsection{Non-Conflict Baseline Comparison}
90	\label{sec:xnli_baseline}
91	
92	If the ZH$\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.
93	We test this prediction using XNLI entailment-versus-contradiction probes.
94	All three models achieve high within-language accuracy on XNLI (Llama 94.0\% EN, 87.5\% ZH; Qwen 96.6\% EN, 89.5\% ZH; Gemma 95.6\% EN, 89.0\% ZH). These accuracies confirm that the probing pipeline captures semantic distinctions beyond knowledge conflicts.
95	The XNLI probes exhibit the same directional asymmetry: Llama $\Delta_{\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\Delta_{\text{asym}} = +6.7$ pp, CI [2.4, 11.7]; Gemma $\Delta_{\text{asym}} = +7.8$ pp, CI [5.7, 10.0] ($p < 0.001$).
96	All three XNLI CIs exclude zero and overlap substantially with the corresponding conflict-task CIs (Figure~\ref{fig:asymmetry_forest}).
97	Formal Two One-Sided Tests (TOST) equivalence tests ($\pm$2~pp margin) were non-significant (all $p > 0.36$); post-hoc power analysis shows only 1.4\% power at this margin given standard error (SE) $\approx 4.2$~pp, with 80\% power requiring a $\pm$12.5~pp margin.
98	Bayesian equivalence testing yields a Bayes factor $\text{BF}_{01} \approx 1.5$ (half-normal prior, scale $= 5$~pp), providing directionally consistent but modest evidence for equivalence.
99	Combined with the consistent direction across all six model$\times$task combinations (binomial $p = 0.016$) and magnitudes clustering in [$+$6.0, $+$7.8~pp], these analyses support the ``consistency'' characterization: the non-significance reflects insufficient power, not meaningful differences.
100	
101	%% Figure 3: Asymmetry forest plot
102	\begin{figure}[t]
103	\centering
104	\includegraphics[width=\columnwidth]{fig4_asymmetry_forest.pdf}
105	\caption{Transfer asymmetry ($\Delta_{\text{asym}}$) with bootstrap 95\% CIs ($n = 2{,}000$) for conflict and XNLI tasks across all three architectures (six data points). Conflict and XNLI CIs overlap substantially within each model, indicating that the ZH$\to$EN advantage is a general cross-lingual property rather than conflict-specific. Grey dashed lines: $\pm$2~pp exploratory equivalence margin (TOST power $= 1.4$\%; see \S\ref{sec:xnli_baseline}).}
106	\label{fig:asymmetry_forest}
107	\end{figure}
108	
109	\subsection{Confound Exclusion}
110	\label{sec:confounds}
111	
112	Two potential confounds could inflate cross-lingual probe accuracy: lexical overlap between English and Chinese inputs and translation quality.
113	
114	\paragraph{Token overlap and EN-DE control.}
115	Per-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\%, already at the floor imposed by distinct writing systems.
116	Neither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$, $r^2 = 0.023$), running counter to the confound hypothesis.
117	The strongest evidence comes from a typological control: we translate the same Llama ConflictQA samples into German using the identical Qwen3-8B pipeline, where per-sample Jaccard similarity (14.8\%) is approximately $4\times$ higher than EN-ZH (3.8\%).
118	Despite this substantially higher lexical overlap, the EN$\leftrightarrow$DE transfer asymmetry is near-zero ($\Delta = +1.2$~pp, n.s.), ruling out shared tokens as a driver of the observed EN-ZH asymmetry (Table~\ref{tab:confound}).
119	
120	\paragraph{Translation quality.}
121	We stratify test samples by COMET score into terciles and compare EN$\to$ZH probe accuracy across strata.
122	Qwen shows a reversed association ($\Delta = -5.6$~pp, Fisher $p = 0.695$) and Llama a negligible one ($\Delta = +1.7$~pp, $p = 0.761$), both inconsistent with translation quality driving probe transfer.
123	Gemma shows a non-significant trend in the confound direction ($\Delta = +10.3$~pp, $p = 0.278$), but interpretation is limited by the near-chance baseline accuracy of the EN$\to$ZH probe at L17 (58.8\%), placing this analysis in a low-power regime.
124	With a minimum detectable difference of 25.3~pp at 80\% power ($n \approx 56$ per tercile), the COMET tercile analysis can neither confirm nor exclude a moderate translation quality effect; it serves as supplementary evidence alongside the token overlap and EN-DE controls.
125	
126	\begin{table}[t]
127	\centering
128	\caption{Confound exclusion analysis. COMET tercile: $\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\to$ZH probe accuracy.}
129	\label{tab:confound}
130	\resizebox{\columnwidth}{!}{%
131	\begin{tabular}{llrl}
132	\toprule
133	Confound & Model & Result & $p$ \\
134	\midrule
135	COMET tercile & Qwen & $\Delta = -5.6$ pp & 0.695 \\
136	COMET tercile & Llama & $\Delta = +1.7$ pp & 0.761 \\
137	COMET tercile & Gemma & $\Delta = +10.3$ pp & 0.278 \\
138	\midrule
139	Token overlap & Qwen & n.s. & $>$0.4 \\
140	Token overlap & Llama & $r = -0.15$ & 0.012 \\
141	\bottomrule
142	\end{tabular}%
143	}
144	\end{table}
145	
146	\subsection{Causal Evidence via Representation Steering}
147	\label{sec:steering}
148	
149	The probing results establish that conflict signals are detectable, but detection does not imply causal relevance.
150	We test whether the probe weight direction $\mathbf{w}_l$ causally influences conflict resolution by injecting $\alpha \cdot \mathbf{w}_l$ into the last-token residual stream at a target layer during inference.
151	We sweep $\alpha \in \{\pm 20, \pm 10, \pm 5, \pm 2, \pm 1\}$ ($k = 10$) following prior steering conventions \citep{turner2023activation, marks2024geometry} and report results at all tested values.
152	We measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.
153	
154	\paragraph{L13 (mid-layer, 41\% depth).}
155	Steering at layer 13 produces bidirectional causal effects (Figure~\ref{fig:steering_viz}; Table~\ref{tab:steering}).
156	Positive steering ($\alpha = +5$) yields a flip rate of 19.9\% versus 6.6\% for the random control (Fisher $p = 0.002$; 4 p$\to$c flips), while negative steering ($\alpha = -20$) yields 36.0\% versus 17.6\% ($p < 0.001$; 5 c$\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\alpha$ values, threshold $p < 0.005$).
157	All-position injection at L13 produces identical results; the causal signal is concentrated at the final token.
158	Steering at nearby L16 (50\% depth, just three layers away) showed no significant effect (all $p > 0.12$), consistent with a narrow causal window.
159	Under a conservative family-wise correction across all 30 tests (3 layers $\times$ 10 $\alpha$ values, threshold $p < 0.00167$), L13 remains significant ($\alpha = +10$, $p = 0.0003$).
160	An independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\ref{tab:boundary}).
161	
162	\begin{figure}[t]
163	\centering
164	\includegraphics[width=\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}
165	\caption{Steering flip rates at Llama L13 (41\% depth) across $\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\alpha = +5$ (p$\to$c) and $\alpha = -20$ (c$\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\%, probe peak) and L18 (56\%, MLP peak) remain at control levels (Table~\ref{tab:steering}).}
166	\label{fig:steering_viz}
167	\end{figure}
168	
169	\paragraph{Negative layers and coherence collapse.}
170	Steering at L28 (probe peak, 88\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\%) is similarly negative ($p > 0.44$).
171	At extreme magnitude ($\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.
172	
173	\paragraph{Causal localization (Llama).}
174	In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\% depth) regardless of where detection accuracy peaks (EN$\to$EN at L28, ZH$\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.
175	An independent replication with a separately trained probe (seed=123, different train/test split) confirms the L13 causal effect: 2/6 positive-direction $\alpha$ configurations survive per-layer Bonferroni correction ($k{=}6$, $p < 0.0083$), matching the original 2/6 (Appendix~\ref{app:seed_replication}).
176	
177	\paragraph{Cross-model steering.}
178	Cross-model experiments use the reduced 6-value $\alpha$ grid ($k{=}6$, per-layer threshold $p < 0.0083$; \S\ref{sec:steering_method}).
179	Qwen steering at L14 (39\%, $n_{\text{test}} = 131$; probe accuracy 71.0\%) produced no significant effect at any $\alpha$ (best $p = 0.785$) and zero directional flips.
180	Gemma-2-9B-IT L17 (40\% depth) provides a stronger test: with 88.9\% probe accuracy, the highest among all three models (exceeding both Llama 76.1\% and Qwen 71.0\%), steering produced no significant change at any $\alpha$ (best $p = 0.448$) and zero directional flips ($n_{\text{test}} = 171$), ruling out probe quality as a confound and confirming that the causal influence of probe-weight directions is architecture-dependent.
181	AUROC analysis confirms this pattern: Gemma achieves 0.93 AUROC (vs.\ Llama 0.98, Qwen 0.77; Appendix~\ref{app:auroc}), yet steering produces zero causal effect.
182	Appendix~\ref{app:steering_config} reports matched-condition results at three layers per model (${\sim}$36--43\% depth), all confirming the null.
183	
184	\begin{table}[t]
185	\centering
186	\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Bonferroni-corrected significance threshold $p < 0.005$ ($k = 10$). Significant results in bold.$^{\dagger}$}
187	\label{tab:steering}
188	\small
189	\resizebox{\columnwidth}{!}{%
190	\begin{tabular}{lcrrrrl}
191	\toprule
192	Layer & Depth & $\alpha$ & Steer (\%) & Ctrl (\%) & Fisher $p$ & Dir. \\
193	\midrule
194	\textbf{L13} & \textbf{41\%} & $\mathbf{+5}$ & \textbf{19.9} & \textbf{6.6} & $\mathbf{0.002}$ & \textbf{4 p$\to$c} \\
195	\textbf{L13} & \textbf{41\%} & $\mathbf{-20}$ & \textbf{36.0} & \textbf{17.6} & $\mathbf{<0.001}$ & \textbf{5 c$\to$p} \\
196	L16 & 50\% & $+5$ & 8.8 & 8.1 & 1.000 & \\
197	L16 & 50\% & $+10$ & 18.4 & 11.0 & 0.123 & \\
198	L16 & 50\% & $+20$ & 22.8 & 24.3 & 0.886 & \\
199	L18 & 56\% & $+2$ & 3.7 & 1.5 & 0.447 & \\
200	L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
201	L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 1.000 & \\
202	\midrule
203	\multicolumn{7}{l}{\textit{Qwen3-8B ($n_{\text{test}} = 131$)}} \\
204	L14 & 39\% & best & \multicolumn{2}{c}{n.s.} & 0.785 & 0 dir. \\
205	\midrule
206	\multicolumn{7}{l}{\textit{Gemma-2-9B-IT ($n_{\text{test}} = 171$)$^{\ddagger}$}} \\
207	L17 & 40\% & best & \multicolumn{2}{c}{n.s.} & 0.448 & 0 dir. \\
208	\bottomrule
209	\end{tabular}%
210	}
211	\begin{flushleft}
212	\footnotesize $^{\dagger}$ At $\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes. $^{\ddagger}$ Gemma: after correcting a label assignment error.
213	\end{flushleft}
214	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "ff1b46fe-d199-47a1-af33-d67a5ec825e6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \\citep{team2024gemma}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.\nThe three models were independently verified, yielding only 3.5\\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\\% (Llama $\\cap$ Gemma) to 24.8\\% (Gemma $\\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET (wmt22-comet-da; \\citealt{rei2020comet}) back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\\ref{app:auroc}.\nAll CIs are computed via bootstrap resampling with paired differences for asymmetry estimation.\nA selectivity control \\citep{hewitt2019designing} with permuted labels on matched-condition data ($N{=}131$--$201$) yields near-chance accuracy (49.2--51.0\\%) across all models, confirming selectivity gaps of 21--40~pp.\nAll experiments used a single GPU; the boundary replication (Appendix~\\ref{app:boundary}) used an NVIDIA RTX PRO 6000.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nAll three models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.6\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 72.1\\% on ZH$\\to$ZH.\nQwen reaches 75.0\\% on EN$\\to$EN (peak at layer 24, 67\\% depth) and 72.6\\% on ZH$\\to$ZH.\nGemma attains 76.2\\% on EN$\\to$EN (peak at layer 24, 57\\% depth) and 71.0\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for all three models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across all three architectures and both languages.\n\n%% Figure 2: Layer-wise probe accuracy\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_layerwise_probes.pdf}\n\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p = 0.002$), coinciding with the ZH$\\to$ZH probe peak but not the EN$\\to$EN peak (L28). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}\n\\label{fig:layer_probe}\n\\end{figure*}\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}); this confirms that conflict representations partially overlap between English and Chinese.\nAll three models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nWe define $\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})$, computed via paired bootstrap.\nFor Llama, $\\Delta_{\\text{asym}} = +7.3$ percentage points (pp) with a 95\\% bootstrap CI of [0.4, 14.0] ($p = 0.038$); for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7]; for Gemma, $\\Delta_{\\text{asym}} = +6.6$ pp with CI [1.9, 11.1] ($p = 0.006$).\nWhile the Qwen CI marginally includes zero, the asymmetry is consistent in direction across all three architectures.\nThe magnitude of this asymmetry is consistent in direction and magnitude with the XNLI non-conflict baseline across all three architectures (\\S\\ref{sec:xnli_baseline}), and the consistent direction across all three models suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-seed balanced accuracy (\\%) at each direction's optimal layer. $\\Delta_{\\text{asym}}$ and 95\\% CIs from paired bootstrap ($n = 2{,}000$ resamples). Bold: best per-task direction.}\n\\label{tab:main_results}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B & Gemma-2-9B \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.6} & \\textbf{75.0} & \\textbf{76.2} \\\\\nZH $\\to$ ZH & 72.1 & 72.6 & 71.0 \\\\\nEN $\\to$ ZH & 59.6 & 67.3 & 62.9 \\\\\nZH $\\to$ EN & 70.6 & 73.2 & 70.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.3 [0.4, 14.0] & +7.2 [$-$0.6, 13.7] & +6.6 [1.9, 11.1] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 & 95.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 & 89.0 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 & 89.4 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} & \\textbf{97.5} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] & +7.8 [5.7, 10.0] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize Note: $\\Delta_{\\text{asym}}$ is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies.\n\\end{flushleft}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nAll three models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH; Gemma 95.6\\% EN, 89.0\\% ZH). These accuracies confirm that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7]; Gemma $\\Delta_{\\text{asym}} = +7.8$ pp, CI [5.7, 10.0] ($p < 0.001$).\nAll three XNLI CIs exclude zero and overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nFormal Two One-Sided Tests (TOST) equivalence tests ($\\pm$2~pp margin) were non-significant (all $p > 0.36$); post-hoc power analysis shows only 1.4\\% power at this margin given standard error (SE) $\\approx 4.2$~pp, with 80\\% power requiring a $\\pm$12.5~pp margin.\nBayesian equivalence testing yields a Bayes factor $\\text{BF}_{01} \\approx 1.5$ (half-normal prior, scale $= 5$~pp), providing directionally consistent but modest evidence for equivalence.\nCombined with the consistent direction across all six model$\\times$task combinations (binomial $p = 0.016$) and magnitudes clustering in [$+$6.0, $+$7.8~pp], these analyses support the ``consistency'' characterization: the non-significance reflects insufficient power, not meaningful differences.\n\n%% Figure 3: Asymmetry forest plot\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_asymmetry_forest.pdf}\n\\caption{Transfer asymmetry ($\\Delta_{\\text{asym}}$) with bootstrap 95\\% CIs ($n = 2{,}000$) for conflict and XNLI tasks across all three architectures (six data points). Conflict and XNLI CIs overlap substantially within each model, indicating that the ZH$\\to$EN advantage is a general cross-lingual property rather than conflict-specific. Grey dashed lines: $\\pm$2~pp exploratory equivalence margin (TOST power $= 1.4$\\%; see \\S\\ref{sec:xnli_baseline}).}\n\\label{fig:asymmetry_forest}\n\\end{figure}\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: lexical overlap between English and Chinese inputs and translation quality.\n\n\\paragraph{Token overlap and EN-DE control.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, already at the floor imposed by distinct writing systems.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$, $r^2 = 0.023$), running counter to the confound hypothesis.\nThe strongest evidence comes from a typological control: we translate the same Llama ConflictQA samples into German using the identical Qwen3-8B pipeline, where per-sample Jaccard similarity (14.8\\%) is approximately $4\\times$ higher than EN-ZH (3.8\\%).\nDespite this substantially higher lexical overlap, the EN$\\leftrightarrow$DE transfer asymmetry is near-zero ($\\Delta = +1.2$~pp, n.s.), ruling out shared tokens as a driver of the observed EN-ZH asymmetry (Table~\\ref{tab:confound}).\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles and compare EN$\\to$ZH probe accuracy across strata.\nQwen shows a reversed association ($\\Delta = -5.6$~pp, Fisher $p = 0.695$) and Llama a negligible one ($\\Delta = +1.7$~pp, $p = 0.761$), both inconsistent with translation quality driving probe transfer.\nGemma shows a non-significant trend in the confound direction ($\\Delta = +10.3$~pp, $p = 0.278$), but interpretation is limited by the near-chance baseline accuracy of the EN$\\to$ZH probe at L17 (58.8\\%), placing this analysis in a low-power regime.\nWith a minimum detectable difference of 25.3~pp at 80\\% power ($n \\approx 56$ per tercile), the COMET tercile analysis can neither confirm nor exclude a moderate translation quality effect; it serves as supplementary evidence alongside the token overlap and EN-DE controls.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\nCOMET tercile & Gemma & $\\Delta = +10.3$ pp & 0.278 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_l$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_l$ into the last-token residual stream at a target layer during inference.\nWe sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) following prior steering conventions \\citep{turner2023activation, marks2024geometry} and report results at all tested values.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces bidirectional causal effects (Figure~\\ref{fig:steering_viz}; Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$; 4 p$\\to$c flips), while negative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% ($p < 0.001$; 5 c$\\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$).\nAll-position injection at L13 produces identical results; the causal signal is concentrated at the final token.\nSteering at nearby L16 (50\\% depth, just three layers away) showed no significant effect (all $p > 0.12$), consistent with a narrow causal window.\nUnder a conservative family-wise correction across all 30 tests (3 layers $\\times$ 10 $\\alpha$ values, threshold $p < 0.00167$), L13 remains significant ($\\alpha = +10$, $p = 0.0003$).\nAn independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}\n\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\n\\label{fig:steering_viz}\n\\end{figure}\n\n\\paragraph{Negative layers and coherence collapse.}\nSteering at L28 (probe peak, 88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\nAt extreme magnitude ($\\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.\n\n\\paragraph{Causal localization (Llama).}\nIn Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.\nAn independent replication with a separately trained probe (seed=123, different train/test split) confirms the L13 causal effect: 2/6 positive-direction $\\alpha$ configurations survive per-layer Bonferroni correction ($k{=}6$, $p < 0.0083$), matching the original 2/6 (Appendix~\\ref{app:seed_replication}).\n\n\\paragraph{Cross-model steering.}\nCross-model experiments use the reduced 6-value $\\alpha$ grid ($k{=}6$, per-layer threshold $p < 0.0083$; \\S\\ref{sec:steering_method}).\nQwen steering at L14 (39\\%, $n_{\\text{test}} = 131$; probe accuracy 71.0\\%) produced no significant effect at any $\\alpha$ (best $p = 0.785$) and zero directional flips.\nGemma-2-9B-IT L17 (40\\% depth) provides a stronger test: with 88.9\\% probe accuracy, the highest among all three models (exceeding both Llama 76.1\\% and Qwen 71.0\\%), steering produced no significant change at any $\\alpha$ (best $p = 0.448$) and zero directional flips ($n_{\\text{test}} = 171$), ruling out probe quality as a confound and confirming that the causal influence of probe-weight directions is architecture-dependent.\nAUROC analysis confirms this pattern: Gemma achieves 0.93 AUROC (vs.\\ Llama 0.98, Qwen 0.77; Appendix~\\ref{app:auroc}), yet steering produces zero causal effect.\nAppendix~\\ref{app:steering_config} reports matched-condition results at three layers per model (${\\sim}$36--43\\% depth), all confirming the null.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Bonferroni-corrected significance threshold $p < 0.005$ ($k = 10$). Significant results in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL16 & 50\\% & $+5$ & 8.8 & 8.1 & 1.000 & \\\\\nL16 & 50\\% & $+10$ & 18.4 & 11.0 & 0.123 & \\\\\nL16 & 50\\% & $+20$ & 22.8 & 24.3 & 0.886 & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B ($n_{\\text{test}} = 131$)}} \\\\\nL14 & 39\\% & best & \\multicolumn{2}{c}{n.s.} & 0.785 & 0 dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Gemma-2-9B-IT ($n_{\\text{test}} = 171$)$^{\\ddagger}$}} \\\\\nL17 & 40\\% & best & \\multicolumn{2}{c}{n.s.} & 0.448 & 0 dir. \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes. $^{\\ddagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}",
      "numLines": 214,
      "startLine": 1,
      "totalLines": 214
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_012zBkavVPziFXENZLVfHybi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "2f4c5271-0676-4f7d-adc1-8a3d51d0debc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hUqFRvydkoCoBhBwWJLCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3825,
      "cache_read_input_tokens": 25209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3825
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

_source line 19 · 2026-05-25T15:49:38.049Z_

<details><summary>↩ Tool result · `toolu_012zBkavVPziFXENZLVfHybi`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Causal influence is localized to L13 regardless of detection peak.}
5	In Llama, causal influence is localized to L13 (41\% depth; Fisher $p = 0.002$), regardless of detection peak location (EN$\to$EN at L28, ZH$\to$ZH at L13), with all late-layer interventions producing no significant change ($p > 0.3$; Figure~\ref{fig:dissociation}).
6	An MLP probe reveals a third dissociation: non-linear conflict features peak at L18 (56\% depth), between the linear peak (L28) and the causal node (L13).
7	L13 coincides with cross-lingual alignment sites \citep{muller2021first, wendler2024llamas}, suggesting mid-layers serve a dual role in alignment and conflict resolution.
8	Steering failed in Qwen (L14, $n = 131$, $p = 0.785$) and Gemma (L17, $n = 171$, $p = 0.448$) with zero directional flips.
9	The dissociation evidence is strongest for Gemma, where high probe accuracy (88.9\%) and AUROC (0.93) coexist with zero significant steering effects across all tested layers, ruling out probe quality as a confound.
10	For Qwen, the weaker probe performance (71.4\%, AUROC 0.77) makes the null steering result more ambiguous: the probe direction may be too noisy for effective intervention, so the failure cannot be attributed to a true detection--decision dissociation with the same confidence.
11	
12	\paragraph{Why does steering fail in Qwen and Gemma?}
13	Three hypotheses merit consideration, each with preliminary support from our analyses: (1)~non-linear causal interactions \citep{elhage2022toy}---MLP probes gain $+9.2$~pp over linear probes on Llama conflict EN$\to$ZH but $-0.5$~pp on XNLI, indicating conflict-specific non-linear encoding; (2)~superposition \citep{templeton2024scaling}---conflict and XNLI probe weight vectors are near-orthogonal (cosine similarity 0.02--0.05), yet cross-task language identity transfer is near-perfect (87--100\%), a hallmark of superposition; (3)~architectural differences (e.g., Gemma's sandwich normalization)---Qwen and Gemma show mid-layer cross-task transfer dips (L14--L24) absent in Llama, and L13 falls in Llama's dip-free region.
14	Definitive validation requires activation patching \citep{meng2022locating}.
15	
16	\paragraph{Conflict signals and relation to prior work.}
17	The ZH$\to$EN transfer advantage ($+7.3$, $+7.2$, $+6.6$~pp) matches the XNLI baseline ($+6.0$, $+6.7$, $+7.8$~pp), indicating that this asymmetry piggybacks on general cross-lingual alignment \citep{zhao2026when, kargaran2024mexa, wendler2024llamas}.
18	Regarding the detection--action gap, \citet{basu2026interpretability} reported steering failure despite 98.2\% AUROC; our L13 succeeds with a weaker signal because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture.
19	
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "580cdeb3-14cd-47a0-844f-97e9827e20d3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Causal influence is localized to L13 regardless of detection peak.}\nIn Llama, causal influence is localized to L13 (41\\% depth; Fisher $p = 0.002$), regardless of detection peak location (EN$\\to$EN at L28, ZH$\\to$ZH at L13), with all late-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).\nAn MLP probe reveals a third dissociation: non-linear conflict features peak at L18 (56\\% depth), between the linear peak (L28) and the causal node (L13).\nL13 coincides with cross-lingual alignment sites \\citep{muller2021first, wendler2024llamas}, suggesting mid-layers serve a dual role in alignment and conflict resolution.\nSteering failed in Qwen (L14, $n = 131$, $p = 0.785$) and Gemma (L17, $n = 171$, $p = 0.448$) with zero directional flips.\nThe dissociation evidence is strongest for Gemma, where high probe accuracy (88.9\\%) and AUROC (0.93) coexist with zero significant steering effects across all tested layers, ruling out probe quality as a confound.\nFor Qwen, the weaker probe performance (71.4\\%, AUROC 0.77) makes the null steering result more ambiguous: the probe direction may be too noisy for effective intervention, so the failure cannot be attributed to a true detection--decision dissociation with the same confidence.\n\n\\paragraph{Why does steering fail in Qwen and Gemma?}\nThree hypotheses merit consideration, each with preliminary support from our analyses: (1)~non-linear causal interactions \\citep{elhage2022toy}---MLP probes gain $+9.2$~pp over linear probes on Llama conflict EN$\\to$ZH but $-0.5$~pp on XNLI, indicating conflict-specific non-linear encoding; (2)~superposition \\citep{templeton2024scaling}---conflict and XNLI probe weight vectors are near-orthogonal (cosine similarity 0.02--0.05), yet cross-task language identity transfer is near-perfect (87--100\\%), a hallmark of superposition; (3)~architectural differences (e.g., Gemma's sandwich normalization)---Qwen and Gemma show mid-layer cross-task transfer dips (L14--L24) absent in Llama, and L13 falls in Llama's dip-free region.\nDefinitive validation requires activation patching \\citep{meng2022locating}.\n\n\\paragraph{Conflict signals and relation to prior work.}\nThe ZH$\\to$EN transfer advantage ($+7.3$, $+7.2$, $+6.6$~pp) matches the XNLI baseline ($+6.0$, $+6.7$, $+7.8$~pp), indicating that this asymmetry piggybacks on general cross-lingual alignment \\citep{zhao2026when, kargaran2024mexa, wendler2024llamas}.\nRegarding the detection--action gap, \\citet{basu2026interpretability} reported steering failure despite 98.2\\% AUROC; our L13 succeeds with a weaker signal because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture.\n\n",
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

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01RhE3JfsXU4S7RW1Gube95J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "4991cef4-7331-42ec-9e23-848ee3a09571",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hUqFRvydkoCoBhBwWJLCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3825,
      "cache_read_input_tokens": 25209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3825
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

_source line 21 · 2026-05-25T15:49:38.517Z_

<details><summary>↩ Tool result · `toolu_01RhE3JfsXU4S7RW1Gube95J`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth,height=4cm,keepaspectratio]{fig1_hero.pdf}
7	\caption{Cross-lingual knowledge conflict in multilingual LLMs. When a context passage contradicts the model's parametric knowledge, the language of presentation (English vs.\ Chinese) can bias the answer toward different sources. We ask three questions: (1)~Is the conflict signal linearly detectable in the residual stream? (2)~Do probes transfer across languages, and is the transfer symmetric? (3)~Does detection imply causal influence on resolution?}
8	\label{fig:hero}
9	\end{figure*}
10	
11	When multilingual large language models (LLMs) encounter conflicting information between languages, the language of presentation can determine which answer the model produces \citep{zhao2026when}.
12	Yet the internal mechanism remains opaque: how does the model encode the conflict signal, can it be detected from internal representations, and does the detected signal causally influence resolution?
13	
14	Existing work on probing conflict signals has been limited to monolingual settings \citep{zhao2024analysing, brink2026probing}.
15	Extending cross-lingually introduces confounds (translation quality, token overlap, general transfer properties), and probing establishes correlation rather than causation \citep{hewitt2019designing}; \citet{basu2026interpretability} showed that near-perfect probe accuracy does not guarantee effective steering.
16	
17	Our work extends \citet{zhao2024analysing} in four directions: (1)~cross-lingual expansion from monolingual English to EN-ZH conflict probing; (2)~a systematic confound exclusion pipeline; (3)~the XNLI baseline revealing that asymmetry parallels general cross-lingual structure; and (4)~three-model causal intervention demonstrating that detectability does not predict causal relevance.
18	We combine residual stream probing with representation steering across Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT.
19	Probes achieve 77.6\%, 75.0\%, and 76.2\% balanced accuracy on English conflict detection, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).
20	Cross-lingual transfer exhibits a directional asymmetry (ZH$\to$EN $>$ EN$\to$ZH by ${\sim}$7~pp) that is consistent with the XNLI non-conflict baseline \citep{conneau2018xnli}, reflecting general cross-lingual structure rather than conflict-specific encoding.
21	Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L28 (88\% depth), but steering succeeds only at L13 (41\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant change (Figure~\ref{fig:hero}).
22	
23	Our contributions are as follows:
24	\begin{itemize}
25	    \item \textbf{Cross-lingual conflict detectability.} First evidence that knowledge conflict signals are linearly detectable across English and Chinese, with all transfer directions exceeding chance (binomial $p < 0.001$).
26	    \item \textbf{Asymmetry reflects general cross-lingual structure.} The transfer asymmetry (ZH$\to$EN $>$ EN$\to$ZH by ${\sim}$7~pp) matches the XNLI non-conflict baseline, consistent with general cross-lingual alignment rather than conflict-specific encoding.
27	    \item \textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \citep{basu2026interpretability}, we provide mechanistic layer-level localization.
28	    \item \textbf{Confound exclusion pipeline.} COMET translation quality ablation, token overlap analysis, and non-conflict baseline comparison exclude common confounds in cross-lingual probing.
29	\end{itemize}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "483c0173-e77f-448c-8d49-1917d8818ce6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth,height=4cm,keepaspectratio]{fig1_hero.pdf}\n\\caption{Cross-lingual knowledge conflict in multilingual LLMs. When a context passage contradicts the model's parametric knowledge, the language of presentation (English vs.\\ Chinese) can bias the answer toward different sources. We ask three questions: (1)~Is the conflict signal linearly detectable in the residual stream? (2)~Do probes transfer across languages, and is the transfer symmetric? (3)~Does detection imply causal influence on resolution?}\n\\label{fig:hero}\n\\end{figure*}\n\nWhen multilingual large language models (LLMs) encounter conflicting information between languages, the language of presentation can determine which answer the model produces \\citep{zhao2026when}.\nYet the internal mechanism remains opaque: how does the model encode the conflict signal, can it be detected from internal representations, and does the detected signal causally influence resolution?\n\nExisting work on probing conflict signals has been limited to monolingual settings \\citep{zhao2024analysing, brink2026probing}.\nExtending cross-lingually introduces confounds (translation quality, token overlap, general transfer properties), and probing establishes correlation rather than causation \\citep{hewitt2019designing}; \\citet{basu2026interpretability} showed that near-perfect probe accuracy does not guarantee effective steering.\n\nOur work extends \\citet{zhao2024analysing} in four directions: (1)~cross-lingual expansion from monolingual English to EN-ZH conflict probing; (2)~a systematic confound exclusion pipeline; (3)~the XNLI baseline revealing that asymmetry parallels general cross-lingual structure; and (4)~three-model causal intervention demonstrating that detectability does not predict causal relevance.\nWe combine residual stream probing with representation steering across Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT.\nProbes achieve 77.6\\%, 75.0\\%, and 76.2\\% balanced accuracy on English conflict detection, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).\nCross-lingual transfer exhibits a directional asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) that is consistent with the XNLI non-conflict baseline \\citep{conneau2018xnli}, reflecting general cross-lingual structure rather than conflict-specific encoding.\nOur causal analysis reveals a dissociation in Llama: the probe signal peaks at L28 (88\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant change (Figure~\\ref{fig:hero}).\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{Cross-lingual conflict detectability.} First evidence that knowledge conflict signals are linearly detectable across English and Chinese, with all transfer directions exceeding chance (binomial $p < 0.001$).\n    \\item \\textbf{Asymmetry reflects general cross-lingual structure.} The transfer asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) matches the XNLI non-conflict baseline, consistent with general cross-lingual alignment rather than conflict-specific encoding.\n    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.\n    \\item \\textbf{Confound exclusion pipeline.} COMET translation quality ablation, token overlap analysis, and non-conflict baseline comparison exclude common confounds in cross-lingual probing.\n\\end{itemize}\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_01LHETRikh2D9SJ8aWwwkAJo`</summary>

```json
{
  "pattern": "L28|88%|88\\\\\\\\%|late.layer|p = 0\\.002|p=0\\.002",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper",
  "glob": "*.tex",
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "623049ae-20bf-4240-98c0-2fd88b2c3b33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014hUqFRvydkoCoBhBwWJLCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3825,
      "cache_read_input_tokens": 25209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3825
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

_source line 23 · 2026-05-25T15:49:39.781Z_

<details><summary>↩ Tool result · `toolu_01LHETRikh2D9SJ8aWwwkAJo`</summary>

```text
docs/paper/related_work.tex:23:Our results identify layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, suggesting conflict resolution occurs upstream of where the outcome becomes linearly readable.
docs/paper/experiments.tex:44:[Omitted long matching line]
docs/paper/experiments.tex:156:Positive steering ($\alpha = +5$) yields a flip rate of 19.9\% versus 6.6\% for the random control (Fisher $p = 0.002$; 4 p$\to$c flips), while negative steering ($\alpha = -20$) yields 36.0\% versus 17.6\% ($p < 0.001$; 5 c$\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\alpha$ values, threshold $p < 0.005$).
docs/paper/experiments.tex:160:An independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\ref{tab:boundary}).
docs/paper/experiments.tex:165:[Omitted long matching line]
docs/paper/experiments.tex:170:Steering at L28 (probe peak, 88\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\%) is similarly negative ($p > 0.44$).
docs/paper/experiments.tex:174:In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\% depth) regardless of where detection accuracy peaks (EN$\to$EN at L28, ZH$\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.
docs/paper/experiments.tex:200:L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
docs/paper/experiments.tex:201:L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 1.000 & \\
docs/paper/main.tex:80:L28 & 88\% & 85.25\% & $+10$ & 0.284 & 0/6 & --- \\
docs/paper/main.tex:99:\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L28, 88\% depth), MLP probe peak (L18, 56\%), and causal steering node (L13, 41\%) occupy distinct layers, revealing a three-way dissociation. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}
docs/paper/main.tex:111:\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}
docs/paper/conclusion.tex:5:In Llama, a three-way dissociation---linear peak (L28), MLP peak (L18), causal node (L13; $p = 0.002$)---reveals that detection and causation occupy distinct layers; steering fails in Qwen and Gemma despite 88.9\% accuracy, confirming detection alone is insufficient for mechanistic claims.
docs/paper/discussion.tex:5:In Llama, causal influence is localized to L13 (41\% depth; Fisher $p = 0.002$), regardless of detection peak location (EN$\to$EN at L28, ZH$\to$ZH at L13), with all late-layer interventions producing no significant change ($p > 0.3$; Figure~\ref{fig:dissociation}).
docs/paper/discussion.tex:6:An MLP probe reveals a third dissociation: non-linear conflict features peak at L18 (56\% depth), between the linear peak (L28) and the causal node (L13).
docs/paper/method.tex:64:For last-token injection, we sweep $\alpha \in \{\pm 20, \pm 10, \pm 5, \pm 2, \pm 1\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\alpha \in \{\pm 20, \pm 10, \pm 5\}$).
docs/paper/abstract.tex:1:[Omitted long matching line]
docs/paper/introduction.tex:21:Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L28 (88\% depth), but steering succeeds only at L13 (41\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant change (Figure~\ref{fig:hero}).
docs/paper/introduction.tex:27:    \item \textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \citep{basu2026interpretability}, we provide mechanistic layer-level localization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c1497cb0-6b50-484e-98f8-24ba58c58de9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:23:Our results identify layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, suggesting conflict resolution occurs upstream of where the outcome becomes linearly readable.\ndocs/paper/experiments.tex:44:[Omitted long matching line]\ndocs/paper/experiments.tex:156:Positive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$; 4 p$\\to$c flips), while negative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% ($p < 0.001$; 5 c$\\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$).\ndocs/paper/experiments.tex:160:An independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).\ndocs/paper/experiments.tex:165:[Omitted long matching line]\ndocs/paper/experiments.tex:170:Steering at L28 (probe peak, 88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\ndocs/paper/experiments.tex:174:In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.\ndocs/paper/experiments.tex:200:L28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\ndocs/paper/experiments.tex:201:L28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\ndocs/paper/main.tex:80:L28 & 88\\% & 85.25\\% & $+10$ & 0.284 & 0/6 & --- \\\\\ndocs/paper/main.tex:99:\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L28, 88\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) occupy distinct layers, revealing a three-way dissociation. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}\ndocs/paper/main.tex:111:\\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}\ndocs/paper/conclusion.tex:5:In Llama, a three-way dissociation---linear peak (L28), MLP peak (L18), causal node (L13; $p = 0.002$)---reveals that detection and causation occupy distinct layers; steering fails in Qwen and Gemma despite 88.9\\% accuracy, confirming detection alone is insufficient for mechanistic claims.\ndocs/paper/discussion.tex:5:In Llama, causal influence is localized to L13 (41\\% depth; Fisher $p = 0.002$), regardless of detection peak location (EN$\\to$EN at L28, ZH$\\to$ZH at L13), with all late-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).\ndocs/paper/discussion.tex:6:An MLP probe reveals a third dissociation: non-linear conflict features peak at L18 (56\\% depth), between the linear peak (L28) and the causal node (L13).\ndocs/paper/method.tex:64:For last-token injection, we sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5\\}$).\ndocs/paper/abstract.tex:1:[Omitted long matching line]\ndocs/paper/introduction.tex:21:Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L28 (88\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant change (Figure~\\ref{fig:hero}).\ndocs/paper/introduction.tex:27:    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.",
    "numLines": 19
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of all the references. Let me also read the method.tex to check for any additional references.

Let me now plan all the changes needed:

1. **Abstract** (abstract.tex): 
   - Change "the probe signal peaks at late layers (88\% depth)" to something about broadly distributed mid-to-upper layers
   - Ensure < 200 words

2. **Conclusion** (conclusion.tex):
   - Fix three-way dissociation narrative - L28 is no longer linear probe peak
   - Fix p = 0.002 → p < 0.001

3. **Appendix D** (main.tex line 99): fig6 caption
   - Update "linear probe peak (L28, 88\% depth)" → "linear probe peak (L15, 47\% depth)"

4. **Appendix E** (main.tex line 111): AUROC table caption
   - Remove "L28 for Llama, L24 for Gemma, L18 for Qwen" peak layer annotations

5. **Appendix F** (main.tex line 146): matched-condition steering table
   - Llama N=136, probe=76.1% → check if needs update to N=201

6. **Introduction** (introduction.tex):
   - Line 21: "probe signal peaks at L28 (88\% depth)" → needs update
   - Line 27: "Linear" section needs revision as well

Now I'm going through the remaining sections to identify all references to the old layer numbers and statistical values. The Introduction has multiple mentions that need updating, and I need to check the Experiments section for figure captions and layer references. The Discussion section also contains the old Fisher p-value and layer peak information that should be revised to reflect the new findings. I'm realizing the discrepancy here—the original paper cited L28 as the peak for Llama's linear probe, but the new fig6 data shows L15 is actually where performance peaks. I need to check whether the boundary table in appendix B already reflects this matched-condition data or if it's showing something different, since the peak values there don't seem to align with L15 either.

Let me focus on the concrete fixes needed: updating the abstract to describe the probe signal as distributed across mid-to-upper layers rather than peaking at 88% depth, fixing the conclusion's three-way dissociation claim, correcting the p-value from 0.002 to less than 0.001, updating fig6's caption to show L15 at 47% depth instead of L28, and removing peak layer annotations from the AUROC table in appendix E.

I also need to track down and fix all the references scattered throughout the paper—the introduction mentions L28 and the old p-value twice, the experiments section has it in multiple places including the fig3 caption and line 170, and the discussion repeats these claims. I should also verify the matched-condition data in appendix F uses N=136.

Looking at the grep results more carefully, there are actually many more occurrences than the six explicitly listed. The task is asking me to fix those specific items but also do a comprehensive search to catch everything else. So I need to change all instances, not just the ones mentioned.

The key distinction is figuring out which L28 references need to change to L15 versus which ones stay. References to L28 as the "probe peak" or in the context of late-layer detection need to change to L15, but L28 references in data tables or steering experiments where L28 was actually tested should remain unchanged. Let me work through each occurrence and categorize them properly. Continuing through the document, I need to update references to L28 as the probe peak in the experiments and discussion sections—keeping the actual data rows intact but changing any labels that incorrectly identify L28 as the peak location. I'm also checking method.tex to see what layers were tested and verifying whether N=136, 76.1% needs adjustment based on the corrected peak layer. I'm realizing the core issue: the user wants consistency with figure 6, which shows L15 as the peak for the matched-condition data, so I need to update all references from L28 to L15 throughout the paper, even though this changes the reported experimental results. Let me proceed systematically through the grep results to make these corrections. Looking at the task list, I need to systematically update all references to the old L28/88% values throughout the document. The user's new data shows the Llama peak is actually at L15 (47% depth), not L28, so I need to find and correct every occurrence—including the experiments.tex line that currently states "peak at layer 28, 88% depth". The challenge is that I don't have the exact accuracy value at L15 yet, but I should proceed with updating the layer and depth information while noting where accuracy values need verification. of L28, then the peak accuracy would be different. But I don't have that number. Let me reconsider what the task is actually asking for. The task specifies the old data showed a peak at L28 with 88% depth, while the new data shows a peak at L15 with 47% depth and ~90% probe accuracy on the matched-condition set. The narrative seems to be shifting away from emphasizing layer-specific peaks within Llama toward highlighting that the probe signal spans mid-to-upper layers, and the key evidence for distinguishing detection from decision comes from cross-model comparisons rather than layer separation within a single model.

Given that the user explicitly labels L28 as "old data" and L15 as "new data," it seems the original dataset had an error or was incomplete, and the corrected version with N=201 shows the actual peak at L15. So any references to L28 as the probe peak should be updated to reflect the new findings.

Now I'm looking at the accuracy value for line 33 in experiments.tex—it currently shows 77.6% for what was the L28 peak, but I don't have the exact accuracy at L15 from the new data. The boundary table has L14 at 91.75% and L16 at 91.50%, so L15 would fall somewhere in that range, but that's from a different dataset. Rather than guessing, I should focus on the user's explicit instructions and let the grep verification catch any inconsistencies that need fixing. I'm realizing there are two different datasets at play here—the original full dataset where the peak might still be at L28, and the matched-condition N=201 data where the peak is at L15. Since the user wants all L28 peak references corrected and I don't have the exact accuracy values for L15, I should update the layer number to L15 and either remove the specific accuracy percentage or generalize it to match the probe accuracy mentioned in the new data. I need to figure out whether the 77.6% accuracy value in the experiments section corresponds to layer 28 or layer 15—if I'm updating the peak layer reference to L15 for consistency with the figure, the accuracy at that layer might be different from what's currently reported. The two datasets are fundamentally different—the original full dataset (272 samples) shows a peak at L28 with 77.6%, while the matched-condition subset (N=201) shows a peak at L15 around 90%—so they're not directly comparable. Since the user is asking me to update Figure 6 with the new L15 peak, I should clarify whether the experiments section should still report the original full-data results or if everything needs to be updated consistently.

Rather than overthinking this further, I'll make all the explicitly requested changes and handle other L28/88% occurrences conservatively to align with the new narrative, then check the methods section for additional context before starting the revisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "27fb0b51-df65-41c0-be9a-c6f271046c74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Br8ubv2HUYaJBtwRBPXRu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10921,
      "cache_read_input_tokens": 29034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10921
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01NjE2sCUdSP8Q2YbTAofmAL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c779288d-8d92-4140-8bbd-53e36f3c03aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Br8ubv2HUYaJBtwRBPXRu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10921,
      "cache_read_input_tokens": 29034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10921
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

_source line 26 · 2026-05-25T15:51:15.458Z_

<details><summary>↩ Tool result · `toolu_01NjE2sCUdSP8Q2YbTAofmAL`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth,height=4cm,keepaspectratio]{fig2_pipeline.pdf}
7	\caption{Method overview. We construct parallel EN/ZH conflict data from ConflictQA with COMET-validated translations, extract per-layer residual stream representations, train logistic regression probes in four transfer directions (EN$\to$EN, ZH$\to$ZH, EN$\to$ZH, ZH$\to$EN), and apply confound exclusion controls before causal steering validation.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	Our pipeline proceeds from data construction through probing and steering (Figure~\ref{fig:pipeline}), formalized below.
12	
13	\subsection{Task Formulation}
14	\label{sec:task}
15	
16	Given a context passage $c$ and question $q$, the model produces an answer that is either \emph{contextual} (derived from $c$) or \emph{parametric} (from pre-trained knowledge).
17	When $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.
18	We train a logistic regression probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ on the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$ to predict a binary label $y \in \{\text{contextual}, \text{parametric}\}$.
19	
20	\subsection{Data Construction}
21	\label{sec:data}
22	
23	We build on ConflictQA \citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.
24	We filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \citep{grattafiori2024llama}, 966 for Qwen \citep{yang2025qwen3}, and 1{,}590 for Gemma \citep{team2024gemma} (80/20 train/test split with stratification).
25	For cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET (Crosslingual Optimized Metric for Evaluation of Translation; \citet{rei2020comet}) back-translation scores used in confound analysis (\S\ref{sec:confound_method}).
26	
27	\subsection{Activation Extraction and Probing}
28	\label{sec:extraction}
29	
30	For each input, we construct English and Chinese versions and extract the last-token residual stream $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \citep{belinkov2022probing}.
31	We record the model's answer and assign binary labels (contextual vs.\ parametric).
32	
33	\label{sec:probing}
34	At each layer, we train an $L_2$-regularized logistic regression probe ($C = 1.0$; \citealt{belinkov2022probing, hewitt2019designing}) and evaluate with balanced accuracy to account for class imbalance (contextual/parametric ratios range from 40/60 to 55/45 across models).
35	We report peak-layer accuracy (maximum across layers) as the primary metric.
36	To verify that probes capture conflict-specific structure rather than arbitrary linear separability, we run a selectivity control \citep{hewitt2019designing}: probes trained on permuted labels should yield chance-level accuracy if the original signal is meaningful.
37	As a complementary analysis, we train two-layer MLP probes (hidden dimension 256, ReLU activation, same $L_2$ penalty) to test whether conflict information is encoded non-linearly at layers where linear probes underperform.
38	Confidence intervals are estimated via bootstrap resampling ($n = 2{,}000$) \citep{ulmer2022deep}.
39	
40	\subsection{Cross-Lingual Transfer Protocol}
41	\label{sec:transfer}
42	
43	We evaluate probes in four directions: EN$\to$EN, ZH$\to$ZH (within-language upper bounds), EN$\to$ZH, and ZH$\to$EN (cross-lingual transfer).
44	We quantify directional asymmetry as $\Delta_{\text{asym}} = \text{acc}(\text{ZH}{\to}\text{EN}) - \text{acc}(\text{EN}{\to}\text{ZH})$, computed via paired bootstrap (same resampled indices for both directions).
45	
46	\subsection{Confound Exclusion}
47	\label{sec:confound_method}
48	
49	We exclude two artifacts: (1)~\emph{translation quality}, where we stratify test samples by COMET score into terciles and compare probe accuracy (Fisher's exact test); (2)~\emph{token overlap}, where we compute per-sample Jaccard similarity between English and Chinese token sets and test for correlation with accuracy (Pearson's $r$).
50	As a typological control, we additionally translate samples into German (EN$\to$DE) using the same pipeline; since German shares substantially more lexical overlap with English than Chinese does, a positive EN-DE asymmetry would implicate shared tokens rather than cross-lingual structure.
51	As a \emph{non-conflict baseline}, we apply the same probing pipeline to XNLI entailment-versus-contradiction \citep{conneau2018xnli}; if $\Delta_{\text{asym}} > 0$ also appears in this non-conflict task, the asymmetry reflects a general cross-lingual property rather than conflict-specific encoding.
52	
53	\subsection{Representation Steering}
54	\label{sec:steering_method}
55	
56	To test whether the probe direction is causally relevant \citep{hewitt2019designing}, we inject $\alpha \cdot \mathbf{w}_l$ (the probe weight vector from \S\ref{sec:task}) into the last-token residual stream at layer $l$ during inference \citep{li2023iti, zou2023representation}:
57	$\mathbf{h}'_l = \mathbf{h}_l + \alpha \cdot \mathbf{w}_l$,
58	where positive $\alpha$ pushes toward the contextual direction and negative toward the parametric.
59	As control, we inject a random vector $\mathbf{r} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$, normalized to $\|\mathbf{r}\| = \|\mathbf{w}_l\|$, at the same layer and position; the random control isolates the effect of direction from magnitude.
60	We also test an all-position variant where the perturbation is applied to every token position (not just the last token) to determine whether the causal signal is position-specific.
61	We measure the flip rate (fraction of samples switching answer category) and compare via Fisher's exact test.
62	We apply Bonferroni correction per layer ($k = 10$ $\alpha$ values), treating each layer as an independent hypothesis about causal locus, consistent with prior work in mechanistic interpretability that tests layers individually \citep{meng2022locating, geiger2024finding}.
63	For Llama L13 (the layer showing causal effects), this yields a corrected threshold of $0.05/10 = 0.005$.
64	For last-token injection, we sweep $\alpha \in \{\pm 20, \pm 10, \pm 5, \pm 2, \pm 1\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\alpha \in \{\pm 20, \pm 10, \pm 5\}$).
65	Steering evaluation uses only the conflict-condition subset of the English test data, yielding $n_{\text{test}}$ smaller than the full probe test set (e.g., 136 vs.\ 272 for Llama).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "6a0c990e-d885-4749-b8f4-55b1ca8bb77a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=4cm,keepaspectratio]{fig2_pipeline.pdf}\n\\caption{Method overview. We construct parallel EN/ZH conflict data from ConflictQA with COMET-validated translations, extract per-layer residual stream representations, train logistic regression probes in four transfer directions (EN$\\to$EN, ZH$\\to$ZH, EN$\\to$ZH, ZH$\\to$EN), and apply confound exclusion controls before causal steering validation.}\n\\label{fig:pipeline}\n\\end{figure}\n\nOur pipeline proceeds from data construction through probing and steering (Figure~\\ref{fig:pipeline}), formalized below.\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a context passage $c$ and question $q$, the model produces an answer that is either \\emph{contextual} (derived from $c$) or \\emph{parametric} (from pre-trained knowledge).\nWhen $c$ contradicts parametric knowledge, the choice constitutes a knowledge conflict.\nWe train a logistic regression probe $f_\\theta(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)$ on the last-token residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$ to predict a binary label $y \\in \\{\\text{contextual}, \\text{parametric}\\}$.\n\n\\subsection{Data Construction}\n\\label{sec:data}\n\nWe build on ConflictQA \\citep{xie2024adaptive}, which pairs questions with context passages contradicting the model's parametric knowledge.\nWe filter samples by querying each model without context and retaining only those answered correctly, yielding 1{,}368 samples for Llama \\citep{grattafiori2024llama}, 966 for Qwen \\citep{yang2025qwen3}, and 1{,}590 for Gemma \\citep{team2024gemma} (80/20 train/test split with stratification).\nFor cross-lingual transfer, we translate all inputs into Chinese using a Qwen3-8B pipeline, with quality validated by COMET (Crosslingual Optimized Metric for Evaluation of Translation; \\citet{rei2020comet}) back-translation scores used in confound analysis (\\S\\ref{sec:confound_method}).\n\n\\subsection{Activation Extraction and Probing}\n\\label{sec:extraction}\n\nFor each input, we construct English and Chinese versions and extract the last-token residual stream $\\mathbf{h}_l \\in \\mathbb{R}^d$ at every layer $l$ ($L = 32$ for Llama, $36$ for Qwen, $42$ for Gemma; $d = 4096$ for Llama/Qwen, $3584$ for Gemma), following the last-token aggregation principle \\citep{belinkov2022probing}.\nWe record the model's answer and assign binary labels (contextual vs.\\ parametric).\n\n\\label{sec:probing}\nAt each layer, we train an $L_2$-regularized logistic regression probe ($C = 1.0$; \\citealt{belinkov2022probing, hewitt2019designing}) and evaluate with balanced accuracy to account for class imbalance (contextual/parametric ratios range from 40/60 to 55/45 across models).\nWe report peak-layer accuracy (maximum across layers) as the primary metric.\nTo verify that probes capture conflict-specific structure rather than arbitrary linear separability, we run a selectivity control \\citep{hewitt2019designing}: probes trained on permuted labels should yield chance-level accuracy if the original signal is meaningful.\nAs a complementary analysis, we train two-layer MLP probes (hidden dimension 256, ReLU activation, same $L_2$ penalty) to test whether conflict information is encoded non-linearly at layers where linear probes underperform.\nConfidence intervals are estimated via bootstrap resampling ($n = 2{,}000$) \\citep{ulmer2022deep}.\n\n\\subsection{Cross-Lingual Transfer Protocol}\n\\label{sec:transfer}\n\nWe evaluate probes in four directions: EN$\\to$EN, ZH$\\to$ZH (within-language upper bounds), EN$\\to$ZH, and ZH$\\to$EN (cross-lingual transfer).\nWe quantify directional asymmetry as $\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})$, computed via paired bootstrap (same resampled indices for both directions).\n\n\\subsection{Confound Exclusion}\n\\label{sec:confound_method}\n\nWe exclude two artifacts: (1)~\\emph{translation quality}, where we stratify test samples by COMET score into terciles and compare probe accuracy (Fisher's exact test); (2)~\\emph{token overlap}, where we compute per-sample Jaccard similarity between English and Chinese token sets and test for correlation with accuracy (Pearson's $r$).\nAs a typological control, we additionally translate samples into German (EN$\\to$DE) using the same pipeline; since German shares substantially more lexical overlap with English than Chinese does, a positive EN-DE asymmetry would implicate shared tokens rather than cross-lingual structure.\nAs a \\emph{non-conflict baseline}, we apply the same probing pipeline to XNLI entailment-versus-contradiction \\citep{conneau2018xnli}; if $\\Delta_{\\text{asym}} > 0$ also appears in this non-conflict task, the asymmetry reflects a general cross-lingual property rather than conflict-specific encoding.\n\n\\subsection{Representation Steering}\n\\label{sec:steering_method}\n\nTo test whether the probe direction is causally relevant \\citep{hewitt2019designing}, we inject $\\alpha \\cdot \\mathbf{w}_l$ (the probe weight vector from \\S\\ref{sec:task}) into the last-token residual stream at layer $l$ during inference \\citep{li2023iti, zou2023representation}:\n$\\mathbf{h}'_l = \\mathbf{h}_l + \\alpha \\cdot \\mathbf{w}_l$,\nwhere positive $\\alpha$ pushes toward the contextual direction and negative toward the parametric.\nAs control, we inject a random vector $\\mathbf{r} \\sim \\mathcal{N}(\\mathbf{0}, \\mathbf{I})$, normalized to $\\|\\mathbf{r}\\| = \\|\\mathbf{w}_l\\|$, at the same layer and position; the random control isolates the effect of direction from magnitude.\nWe also test an all-position variant where the perturbation is applied to every token position (not just the last token) to determine whether the causal signal is position-specific.\nWe measure the flip rate (fraction of samples switching answer category) and compare via Fisher's exact test.\nWe apply Bonferroni correction per layer ($k = 10$ $\\alpha$ values), treating each layer as an independent hypothesis about causal locus, consistent with prior work in mechanistic interpretability that tests layers individually \\citep{meng2022locating, geiger2024finding}.\nFor Llama L13 (the layer showing causal effects), this yields a corrected threshold of $0.05/10 = 0.005$.\nFor last-token injection, we sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5\\}$).\nSteering evaluation uses only the conflict-condition subset of the English test data, yielding $n_{\\text{test}}$ smaller than the full probe test set (e.g., 136 vs.\\ 272 for Llama).",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01Ybze67Ga5gxUWjwhF1QAjG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "7e4a5c9d-4aa1-4935-ba7e-d42f9ededefa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Br8ubv2HUYaJBtwRBPXRu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10921,
      "cache_read_input_tokens": 29034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10921
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

_source line 28 · 2026-05-25T15:51:16.092Z_

<details><summary>↩ Tool result · `toolu_01Ybze67Ga5gxUWjwhF1QAjG`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).
6	Moving beyond behavioral observation, \citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, \citet{brink2026probing} localized factual associations via probing, \citet{pham2026where} traced intra-memory conflict pathways, and \citet{li2025taming} proposed conflict mitigation methods.
7	Information-theoretic approaches \citep{pimentel2021probing} offer complementary perspectives on probe expressiveness, and \citet{ravichander2021probing} raised concerns about whether probed information is task-relevant.
8	These studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.
9	
10	\paragraph{Cross-lingual representations in multilingual models.}
11	Intermediate layers develop language-independent representations: \citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \citet{muller2021first} found mid-layer alignment in multilingual BERT.
12	For decoder-only LLMs, \citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \citet{kargaran2024mexa} quantified this bias across language pairs.
13	These findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\to$EN transfer advantage reflects English-centric structure.
14	Behavioral consequences have been documented by \citet{wang2025lost}, \citet{zhao2026when} (CLEAR cross-lingual conflict benchmark), and \citet{ifergan2024beneath, xing2024evaluating}; our work provides a mechanistic account of why such asymmetries arise.
15	
16	\paragraph{Representation steering and causal intervention.}
17	\citet{li2023iti} introduced Inference-Time Intervention for steering via learned bias vectors, \citet{turner2023activation} proposed Activation Addition as an optimization-free alternative, and \citet{zou2023representation} generalized these approaches through Representation Engineering.
18	\citet{marks2024geometry} showed that truth-related representations exhibit linear structure amenable to such interventions.
19	In knowledge conflicts, \citet{zhao2025steering} applied Sparse Autoencoder (SAE)-based steering (SpARE) in monolingual settings.
20	Recent work has begun exploring cross-lingual steering: \citet{pokharel2026crosslingual} proposed training-free cross-lingual activation steering, \citet{sundar2025steering} analyzed how model interventions induce cross-lingual alignment shifts, and \citet{gurgurov2026clasbench} introduced a cross-lingual steering benchmark.
21	These successes are not universal: \citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering.
22	\citet{feng2026finegrained} proposed fine-grained activation steering targeting specific layers, and \citet{meng2022locating} demonstrated localized causal editing via activation patching (Rank-One Model Editing; ROME); alternative causal frameworks \citep{geiger2024finding} remain unexplored for cross-lingual conflict settings.
23	Our results identify layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, suggesting conflict resolution occurs upstream of where the outcome becomes linearly readable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "dd1351dc-6514-4d62-ad00-dd6c9ca54931",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Knowledge conflict detection.}\n\\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent resolution strategies, and \\citet{xu2024knowledge} provided a systematic conflict taxonomy (intra-memory, context-memory, inter-context).\nMoving beyond behavioral observation, \\citet{zhao2024analysing} demonstrated linearly separable conflict signals in English residual streams, \\citet{brink2026probing} localized factual associations via probing, \\citet{pham2026where} traced intra-memory conflict pathways, and \\citet{li2025taming} proposed conflict mitigation methods.\nInformation-theoretic approaches \\citep{pimentel2021probing} offer complementary perspectives on probe expressiveness, and \\citet{ravichander2021probing} raised concerns about whether probed information is task-relevant.\nThese studies operate exclusively in monolingual settings; extending to cross-lingual scenarios introduces confounds (translation quality, token overlap, general transfer properties) that we address with a dedicated exclusion pipeline.\n\n\\paragraph{Cross-lingual representations in multilingual models.}\nIntermediate layers develop language-independent representations: \\citet{wu2020emerging} showed cross-lingual structure emerges without explicit alignment, and \\citet{muller2021first} found mid-layer alignment in multilingual BERT.\nFor decoder-only LLMs, \\citet{wendler2024llamas} showed that Llama processes non-English inputs through an English-centric latent space, and \\citet{kargaran2024mexa} quantified this bias across language pairs.\nThese findings predict our empirical observations: mid-layer steering success aligns with intermediate-layer language alignment, and the ZH$\\to$EN transfer advantage reflects English-centric structure.\nBehavioral consequences have been documented by \\citet{wang2025lost}, \\citet{zhao2026when} (CLEAR cross-lingual conflict benchmark), and \\citet{ifergan2024beneath, xing2024evaluating}; our work provides a mechanistic account of why such asymmetries arise.\n\n\\paragraph{Representation steering and causal intervention.}\n\\citet{li2023iti} introduced Inference-Time Intervention for steering via learned bias vectors, \\citet{turner2023activation} proposed Activation Addition as an optimization-free alternative, and \\citet{zou2023representation} generalized these approaches through Representation Engineering.\n\\citet{marks2024geometry} showed that truth-related representations exhibit linear structure amenable to such interventions.\nIn knowledge conflicts, \\citet{zhao2025steering} applied Sparse Autoencoder (SAE)-based steering (SpARE) in monolingual settings.\nRecent work has begun exploring cross-lingual steering: \\citet{pokharel2026crosslingual} proposed training-free cross-lingual activation steering, \\citet{sundar2025steering} analyzed how model interventions induce cross-lingual alignment shifts, and \\citet{gurgurov2026clasbench} introduced a cross-lingual steering benchmark.\nThese successes are not universal: \\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering.\n\\citet{feng2026finegrained} proposed fine-grained activation steering targeting specific layers, and \\citet{meng2022locating} demonstrated localized causal editing via activation patching (Rank-One Model Editing; ROME); alternative causal frameworks \\citep{geiger2024finding} remain unexplored for cross-lingual conflict settings.\nOur results identify layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, suggesting conflict resolution occurs upstream of where the outcome becomes linearly readable.",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01Xe1cw3V5RUFBWc7qFcPrrp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "cf081b8d-eda3-4898-9e11-824fff948684",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Br8ubv2HUYaJBtwRBPXRu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10921,
      "cache_read_input_tokens": 29034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10921
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

_source line 30 · 2026-05-25T15:51:16.204Z_

<details><summary>↩ Tool result · `toolu_01Xe1cw3V5RUFBWc7qFcPrrp`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our study has three main limitations.
5	First, we evaluate only one language pair (English-Chinese) and causal steering succeeded only in Llama at L13; Gemma L17 failed despite 88.9\% probe accuracy ($n = 171$) and Qwen L14 ($n = 131$) was also negative.
6	Typologically diverse language pairs and alternative intervention methods are needed to assess generality.
7	Null steering results in Qwen and Gemma may reflect limitations of single-direction linear steering rather than absence of causal structure; alternative methods such as activation patching \citep{meng2022locating} may reveal non-linear causal pathways that our approach cannot detect.
8	Second, the effective dataset size (966 to 1,590 samples per model) is constrained by parametric knowledge verification, which retains only questions where the model confidently knows the ground truth and may bias toward well-represented knowledge; additionally, Qwen3-8B serves as both the translation model and an experimental subject, though COMET-based quality control mitigates this concern, and the fact that Llama and Gemma, architecturally independent of the translation model, show the same asymmetry pattern ($\Delta_{\text{asym}} = +7.3$ and $+6.6$~pp, respectively) provides cross-validation that the effect is not an artifact of Qwen-specific translation biases.
9	Third, all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability; while peak balanced accuracy remains stable across seeds (Llama $\pm$0.12\%, Gemma $\pm$1.32\%, Qwen $\pm$1.90\%), the specific peak layer can shift.
10	We acknowledge that $k$-fold cross-validation would provide stronger stability guarantees \citep{belinkov2022probing}; given that our core claims rest on cross-model consistency and directional patterns rather than exact accuracy values, the current cross-seed stability analysis provides partial mitigation, and we commit to reporting full 5-fold CV results in the camera-ready version.
11	This work used AI coding and writing assistants throughout; Appendix~\ref{app:ai-assistants} details the scope of use.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "55127a20-4e77-44e2-8e3d-e8de0a7fe923",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nOur study has three main limitations.\nFirst, we evaluate only one language pair (English-Chinese) and causal steering succeeded only in Llama at L13; Gemma L17 failed despite 88.9\\% probe accuracy ($n = 171$) and Qwen L14 ($n = 131$) was also negative.\nTypologically diverse language pairs and alternative intervention methods are needed to assess generality.\nNull steering results in Qwen and Gemma may reflect limitations of single-direction linear steering rather than absence of causal structure; alternative methods such as activation patching \\citep{meng2022locating} may reveal non-linear causal pathways that our approach cannot detect.\nSecond, the effective dataset size (966 to 1,590 samples per model) is constrained by parametric knowledge verification, which retains only questions where the model confidently knows the ground truth and may bias toward well-represented knowledge; additionally, Qwen3-8B serves as both the translation model and an experimental subject, though COMET-based quality control mitigates this concern, and the fact that Llama and Gemma, architecturally independent of the translation model, show the same asymmetry pattern ($\\Delta_{\\text{asym}} = +7.3$ and $+6.6$~pp, respectively) provides cross-validation that the effect is not an artifact of Qwen-specific translation biases.\nThird, all probing results are based on a single train/test split with bootstrap confidence intervals capturing within-split variability; while peak balanced accuracy remains stable across seeds (Llama $\\pm$0.12\\%, Gemma $\\pm$1.32\\%, Qwen $\\pm$1.90\\%), the specific peak layer can shift.\nWe acknowledge that $k$-fold cross-validation would provide stronger stability guarantees \\citep{belinkov2022probing}; given that our core claims rest on cross-model consistency and directional patterns rather than exact accuracy values, the current cross-seed stability analysis provides partial mitigation, and we commit to reporting full 5-fold CV results in the camera-ready version.\nThis work used AI coding and writing assistants throughout; Appendix~\\ref{app:ai-assistants} details the scope of use.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me plan all the changes systematically.

The key changes needed:

### 1. Abstract (abstract.tex)
- "the probe signal peaks at late layers (88\% depth)" → "the probe signal is broadly distributed across mid-to-upper layers"
- Also need to trim to < 200 words

### 2. Introduction (introduction.tex)
- Line 21: "the probe signal peaks at L28 (88\% depth), but steering succeeds only at L13 (41\% depth; Fisher $p = 0.002$)" → update L28→L15, 88%→47%, p=0.002→p<0.001


- Line 27: "Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$)" → update L28→L15, p=0.002→p<0.001

### 3. Experiments (experiments.tex)
- Line 33: "(peak at layer 28, 88% depth)" → "(peak at layer 15, 47% depth)"
- Need to verify the accuracy value at L15 since the peak moved from L28

. The 77.6% was the original peak balanced accuracy, but if the actual peak is at L15, the accuracy there might differ. I don't have the exact value from the new data, so I'll update the layer reference and note that the accuracy may need adjustment once I can confirm it from the figure.

Looking at the boundary table results, the accuracies are substantially higher (85-92%) than 77.6%, but those come from the matched-condition replication with fewer samples, not the original full dataset. The discrepancy suggests these are measuring different things or different data subsets.

For the caption, I need to clarify that the Fisher p = 0.002 refers to the α=+5 steering condition at L13 from the original experiment, not from the boundary table which shows a different p-value. I see the distinction now—L13's best p-value across all conditions is p < 0.001, even though the specific α=+5 steering result shows p = 0.002. So when discussing L13 generally in the introduction and conclusion, I should use the stronger p < 0.001, while noting that the α=+5 condition specifically had p = 0.002.

For the figure caption and general text references, I need to update to p < 0.001 to reflect the overall significance. The steering table itself can keep the α=+5 specific value of p = 0.002 since that's the actual result for that condition.

I also need to fix the L28 references—it's no longer identified as the probe peak, so I should remove that descriptor and just note it as an upper layer measurement at 88% depth.

In the discussion section, I'm updating the p-value and correcting the layer references from L28 to L15 for the EN→EN peak, then checking the layer ordering to make sure the description of where L18 sits relative to L15 and L13 is accurate. three-way ordering changes. Previously: L13 < L18 < L28. Now: L13 < L15 < L18.

The original text says "non-linear conflict features peak at L18 (56% depth), between the linear peak (L28) and the causal node (L13)". With L15 as the new linear peak, L18 is no longer positioned between them—it's actually above L15. So I need to restructure that sentence.

For the appendix sections, I'm updating the figure 6 caption to reflect the linear probe peak at L15 with 47% depth instead of L28 at 88%, removing the AUROC table from appendix E, and checking appendix F for the matched-condition data. The Llama-3.1-8B-Instruct entry shows N=136 with 76.1% probe accuracy, which should be updated to N=201 with 90.0% if that's the correct data. I'm also verifying the figure 3 caption in experiments.tex that mentions the L13 steering layer annotation and its Fisher p-value. Now I'm going through the discussion section to update references there as well, making sure all the layer numbers and statistical values are consistent with the corrected findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "da6e9bdd-d59e-4d32-8a01-d05a05e80f35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2nHANxb6qqPDUTbjKmkFV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9121,
      "cache_read_input_tokens": 39955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9121
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

_source line 32_

I have a full picture of all references. Let me now implement all fixes systematically. Starting with all files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "e32386e1-9092-4938-bc86-c83decf89abc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2nHANxb6qqPDUTbjKmkFV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9121,
      "cache_read_input_tokens": 39955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9121
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

_source line 33_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RKNuhkELEqtD8MFjJ89cUu`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "235c115f-25c6-42b8-bcba-3831379b0ec9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2nHANxb6qqPDUTbjKmkFV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9121,
      "cache_read_input_tokens": 39955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9121
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

_source line 34 · 2026-05-25T15:52:14.867Z_

<details><summary>↩ Tool result · `toolu_01RKNuhkELEqtD8MFjJ89cUu`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "2b4693b4-7618-4a50-8cb4-d1953ee1d6f2",
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

_source line 35_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_014xY2t9NdP7GH3ULRASiffg`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "in_progress",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "pending",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "pending",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "pending",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "pending",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "pending",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "pending",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "pending",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "pending",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "pending",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "pending",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "e6317b11-ddf9-4e88-8b93-ff4117b31dff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKe6JoWvZfNazdtVpo5szC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5376,
      "cache_read_input_tokens": 49076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5376
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 36 · 2026-05-25T15:52:23.476Z_

<details><summary>↩ Tool result · `toolu_014xY2t9NdP7GH3ULRASiffg`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "e0494b45-7f3b-4f2f-bc5d-342951b9a64c",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "in_progress",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "pending",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "pending",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "pending",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "pending",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "pending",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "pending",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "pending",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 37_

Starting with the abstract rewrite.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "4513027e-a107-467a-b184-d8af1dda0ee2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EMoNFy434dwM43GfAngaB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 54452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 589
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

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01TK1uPME1UfZ6MVtYFBeDem`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex",
  "old_string": "When multilingual large language models (LLMs) encounter conflicting information between languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, and does detectability imply causal influence on resolution? We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English (EN)--Chinese (ZH) conflicts. Our analysis combines cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across English and Chinese, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in magnitude and direction, consistent with the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\\% depth), but representation steering achieves causal influence only at a mid-layer (41\\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.",
  "new_string": "When multilingual large language models encounter conflicting information between languages, presentation language can determine the answer, but the internal mechanism remains unknown. We probe residual streams in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT on English--Chinese conflicts, combining cross-lingual transfer, XNLI non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across both languages, and cross-lingual transfer exhibits a directional asymmetry: Chinese-trained probes transfer to English ${\\sim}$7 percentage points more accurately than the reverse, matching the XNLI baseline and consistent with general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: the probe signal is broadly distributed across mid-to-upper layers, yet representation steering achieves causal influence only at a mid-layer (L13, 41\\% depth) in Llama; analogous Qwen and Gemma steering yields no significant effect. These findings indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "b8206765-705f-4346-8b46-586316a09ec9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EMoNFy434dwM43GfAngaB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 54452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 589
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

_source line 39 · 2026-05-25T15:52:42.030Z_

<details><summary>↩ Tool result · `toolu_01TK1uPME1UfZ6MVtYFBeDem`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "9620cace-d1b0-490c-9ae3-6a99e88cb7ee",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex",
    "oldString": "When multilingual large language models (LLMs) encounter conflicting information between languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, and does detectability imply causal influence on resolution? We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English (EN)--Chinese (ZH) conflicts. Our analysis combines cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across English and Chinese, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in magnitude and direction, consistent with the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\\% depth), but representation steering achieves causal influence only at a mid-layer (41\\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.",
    "newString": "When multilingual large language models encounter conflicting information between languages, presentation language can determine the answer, but the internal mechanism remains unknown. We probe residual streams in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT on English--Chinese conflicts, combining cross-lingual transfer, XNLI non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across both languages, and cross-lingual transfer exhibits a directional asymmetry: Chinese-trained probes transfer to English ${\\sim}$7 percentage points more accurately than the reverse, matching the XNLI baseline and consistent with general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: the probe signal is broadly distributed across mid-to-upper layers, yet representation steering achieves causal influence only at a mid-layer (L13, 41\\% depth) in Llama; analogous Qwen and Gemma steering yields no significant effect. These findings indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.",
    "originalFile": "When multilingual large language models (LLMs) encounter conflicting information between languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, and does detectability imply causal influence on resolution? We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English (EN)--Chinese (ZH) conflicts. Our analysis combines cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across English and Chinese, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in magnitude and direction, consistent with the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\\% depth), but representation steering achieves causal influence only at a mid-layer (41\\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 1,
        "newStart": 1,
        "newLines": 1,
        "lines": [
          "-When multilingual large language models (LLMs) encounter conflicting information between languages, presentation language can determine the answer. Behavioral studies attribute this to linguistic affinity, but the internal mechanism remains unknown: how is the conflict signal encoded, and does detectability imply causal influence on resolution? We probe residual stream representations in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT, focusing on English (EN)--Chinese (ZH) conflicts. Our analysis combines cross-lingual transfer, Cross-lingual Natural Language Inference (XNLI) non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across English and Chinese, and cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English ${\\sim}$7 percentage points more accurately than the reverse. This asymmetry matches the XNLI non-conflict baseline in magnitude and direction, consistent with the model's general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision in Llama-3.1-8B-Instruct: the probe signal peaks at late layers (88\\% depth), but representation steering achieves causal influence only at a mid-layer (41\\% depth); analogous Qwen and Gemma steering yields no significant effect. These findings, observed in Llama-3.1-8B-Instruct and absent in Qwen and Gemma, indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}.",
          "+When multilingual large language models encounter conflicting information between languages, presentation language can determine the answer, but the internal mechanism remains unknown. We probe residual streams in Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT on English--Chinese conflicts, combining cross-lingual transfer, XNLI non-conflict baselines, confound exclusion, and representation steering. Conflict signals are linearly detectable across both languages, and cross-lingual transfer exhibits a directional asymmetry: Chinese-trained probes transfer to English ${\\sim}$7 percentage points more accurately than the reverse, matching the XNLI baseline and consistent with general multilingual structure rather than conflict-specific encoding. A dissociation emerges between detection and decision: the probe signal is broadly distributed across mid-to-upper layers, yet representation steering achieves causal influence only at a mid-layer (L13, 41\\% depth) in Llama; analogous Qwen and Gemma steering yields no significant effect. These findings indicate that linear detectability does not imply causal relevance, with implications for probe-based intervention\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/clkc_mech_interp-F894/}.}."
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

_source line 40_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01HZfbcsEA2wfpzxTs2myo7D`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "completed",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "in_progress",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "pending",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "pending",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "pending",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "pending",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "pending",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "pending",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "pending",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "pending",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "pending",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "f795c613-96f7-4a61-a466-1f3043fe3d1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TA6d4RcLj3tVzfCXAJjKLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 55041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 903
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

_source line 41 · 2026-05-25T15:52:48.743Z_

<details><summary>↩ Tool result · `toolu_01HZfbcsEA2wfpzxTs2myo7D`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "2ac6f652-f103-484b-9131-2d9042000db9",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "in_progress",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "pending",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "pending",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "pending",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "pending",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "pending",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "pending",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "pending",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "in_progress",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "pending",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "pending",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "pending",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "pending",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "pending",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "pending",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 42_

Now fixing Introduction — two locations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "6fb5ea6e-1871-46dd-99f3-a75de2ea6c53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bRsYmWrfxv4N6HkyesEfH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 55944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

<details open><summary>🔧 Tool call — Edit · `toolu_01QxmhiSFhA9P9seMCDgb75o`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex",
  "old_string": "Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L28 (88\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant change (Figure~\\ref{fig:hero}).",
  "new_string": "Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L15 (47\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p < 0.001$), and upper-layer interventions produce no significant change (Figure~\\ref{fig:hero})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "82ce5c59-25fb-4f9e-b311-d41102981ef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bRsYmWrfxv4N6HkyesEfH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 55944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 44 · 2026-05-25T15:52:54.584Z_

<details><summary>↩ Tool result · `toolu_01QxmhiSFhA9P9seMCDgb75o`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "0926934a-f2ee-477a-9546-37c79d8d6cab",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex",
    "oldString": "Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L28 (88\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant change (Figure~\\ref{fig:hero}).",
    "newString": "Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L15 (47\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p < 0.001$), and upper-layer interventions produce no significant change (Figure~\\ref{fig:hero}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth,height=4cm,keepaspectratio]{fig1_hero.pdf}\n\\caption{Cross-lingual knowledge conflict in multilingual LLMs. When a context passage contradicts the model's parametric knowledge, the language of presentation (English vs.\\ Chinese) can bias the answer toward different sources. We ask three questions: (1)~Is the conflict signal linearly detectable in the residual stream? (2)~Do probes transfer across languages, and is the transfer symmetric? (3)~Does detection imply causal influence on resolution?}\n\\label{fig:hero}\n\\end{figure*}\n\nWhen multilingual large language models (LLMs) encounter conflicting information between languages, the language of presentation can determine which answer the model produces \\citep{zhao2026when}.\nYet the internal mechanism remains opaque: how does the model encode the conflict signal, can it be detected from internal representations, and does the detected signal causally influence resolution?\n\nExisting work on probing conflict signals has been limited to monolingual settings \\citep{zhao2024analysing, brink2026probing}.\nExtending cross-lingually introduces confounds (translation quality, token overlap, general transfer properties), and probing establishes correlation rather than causation \\citep{hewitt2019designing}; \\citet{basu2026interpretability} showed that near-perfect probe accuracy does not guarantee effective steering.\n\nOur work extends \\citet{zhao2024analysing} in four directions: (1)~cross-lingual expansion from monolingual English to EN-ZH conflict probing; (2)~a systematic confound exclusion pipeline; (3)~the XNLI baseline revealing that asymmetry parallels general cross-lingual structure; and (4)~three-model causal intervention demonstrating that detectability does not predict causal relevance.\nWe combine residual stream probing with representation steering across Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT.\nProbes achieve 77.6\\%, 75.0\\%, and 76.2\\% balanced accuracy on English conflict detection, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).\nCross-lingual transfer exhibits a directional asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) that is consistent with the XNLI non-conflict baseline \\citep{conneau2018xnli}, reflecting general cross-lingual structure rather than conflict-specific encoding.\nOur causal analysis reveals a dissociation in Llama: the probe signal peaks at L28 (88\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant change (Figure~\\ref{fig:hero}).\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{Cross-lingual conflict detectability.} First evidence that knowledge conflict signals are linearly detectable across English and Chinese, with all transfer directions exceeding chance (binomial $p < 0.001$).\n    \\item \\textbf{Asymmetry reflects general cross-lingual structure.} The transfer asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) matches the XNLI non-conflict baseline, consistent with general cross-lingual alignment rather than conflict-specific encoding.\n    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.\n    \\item \\textbf{Confound exclusion pipeline.} COMET translation quality ablation, token overlap analysis, and non-conflict baseline comparison exclude common confounds in cross-lingual probing.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 18,
        "newLines": 7,
        "lines": [
          " We combine residual stream probing with representation steering across Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT.",
          " Probes achieve 77.6\\%, 75.0\\%, and 76.2\\% balanced accuracy on English conflict detection, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).",
          " Cross-lingual transfer exhibits a directional asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) that is consistent with the XNLI non-conflict baseline \\citep{conneau2018xnli}, reflecting general cross-lingual structure rather than conflict-specific encoding.",
          "-Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L28 (88\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant change (Figure~\\ref{fig:hero}).",
          "+Our causal analysis reveals a dissociation in Llama: the probe signal peaks at L15 (47\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p < 0.001$), and upper-layer interventions produce no significant change (Figure~\\ref{fig:hero}).",
          " ",
          " Our contributions are as follows:",
          " \\begin{itemize}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01F6WcEy17KarRXXM1PyjPRs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex",
  "old_string": "    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.",
  "new_string": "    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L15), MLP probe peak (L18), and causal steering node (L13; Fisher $p < 0.001$) occupy nearby but distinct mid-layers in Llama; the strongest evidence that detection $\\neq$ decision comes from the cross-model contrast---all three models detect conflict signals, yet only Llama shows causal steering effects. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "f1e4c8e8-ff46-4317-aac4-ecf1f1feb2ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bRsYmWrfxv4N6HkyesEfH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 55944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 46 · 2026-05-25T15:53:01.749Z_

<details><summary>↩ Tool result · `toolu_01F6WcEy17KarRXXM1PyjPRs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "a0eadc2d-c96b-45a6-92ca-c39c0451dc23",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/introduction.tex",
    "oldString": "    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.",
    "newString": "    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L15), MLP probe peak (L18), and causal steering node (L13; Fisher $p < 0.001$) occupy nearby but distinct mid-layers in Llama; the strongest evidence that detection $\\neq$ decision comes from the cross-model contrast---all three models detect conflict signals, yet only Llama shows causal steering effects. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth,height=4cm,keepaspectratio]{fig1_hero.pdf}\n\\caption{Cross-lingual knowledge conflict in multilingual LLMs. When a context passage contradicts the model's parametric knowledge, the language of presentation (English vs.\\ Chinese) can bias the answer toward different sources. We ask three questions: (1)~Is the conflict signal linearly detectable in the residual stream? (2)~Do probes transfer across languages, and is the transfer symmetric? (3)~Does detection imply causal influence on resolution?}\n\\label{fig:hero}\n\\end{figure*}\n\nWhen multilingual large language models (LLMs) encounter conflicting information between languages, the language of presentation can determine which answer the model produces \\citep{zhao2026when}.\nYet the internal mechanism remains opaque: how does the model encode the conflict signal, can it be detected from internal representations, and does the detected signal causally influence resolution?\n\nExisting work on probing conflict signals has been limited to monolingual settings \\citep{zhao2024analysing, brink2026probing}.\nExtending cross-lingually introduces confounds (translation quality, token overlap, general transfer properties), and probing establishes correlation rather than causation \\citep{hewitt2019designing}; \\citet{basu2026interpretability} showed that near-perfect probe accuracy does not guarantee effective steering.\n\nOur work extends \\citet{zhao2024analysing} in four directions: (1)~cross-lingual expansion from monolingual English to EN-ZH conflict probing; (2)~a systematic confound exclusion pipeline; (3)~the XNLI baseline revealing that asymmetry parallels general cross-lingual structure; and (4)~three-model causal intervention demonstrating that detectability does not predict causal relevance.\nWe combine residual stream probing with representation steering across Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-IT.\nProbes achieve 77.6\\%, 75.0\\%, and 76.2\\% balanced accuracy on English conflict detection, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).\nCross-lingual transfer exhibits a directional asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) that is consistent with the XNLI non-conflict baseline \\citep{conneau2018xnli}, reflecting general cross-lingual structure rather than conflict-specific encoding.\nOur causal analysis reveals a dissociation in Llama: the probe signal peaks at L15 (47\\% depth), but steering succeeds only at L13 (41\\% depth; Fisher $p < 0.001$), and upper-layer interventions produce no significant change (Figure~\\ref{fig:hero}).\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{Cross-lingual conflict detectability.} First evidence that knowledge conflict signals are linearly detectable across English and Chinese, with all transfer directions exceeding chance (binomial $p < 0.001$).\n    \\item \\textbf{Asymmetry reflects general cross-lingual structure.} The transfer asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) matches the XNLI non-conflict baseline, consistent with general cross-lingual alignment rather than conflict-specific encoding.\n    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.\n    \\item \\textbf{Confound exclusion pipeline.} COMET translation quality ablation, token overlap analysis, and non-conflict baseline comparison exclude common confounds in cross-lingual probing.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 6,
        "newStart": 24,
        "newLines": 6,
        "lines": [
          " \\begin{itemize}",
          "     \\item \\textbf{Cross-lingual conflict detectability.} First evidence that knowledge conflict signals are linearly detectable across English and Chinese, with all transfer directions exceeding chance (binomial $p < 0.001$).",
          "     \\item \\textbf{Asymmetry reflects general cross-lingual structure.} The transfer asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) matches the XNLI non-conflict baseline, consistent with general cross-lingual alignment rather than conflict-specific encoding.",
          "-    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L28), MLP probe peak (L18), and causal steering node (L13; Fisher $p = 0.002$) diverge in Llama: detectability does not predict causal relevance. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.",
          "+    \\item \\textbf{Detection--decision dissociation.} Linear probe peak (L15), MLP probe peak (L18), and causal steering node (L13; Fisher $p < 0.001$) occupy nearby but distinct mid-layers in Llama; the strongest evidence that detection $\\neq$ decision comes from the cross-model contrast---all three models detect conflict signals, yet only Llama shows causal steering effects. Steering fails in Gemma despite 88.9\\% probe accuracy (strong dissociation) and in Qwen where weaker probe quality leaves the null result more ambiguous; unlike prior behavioral observations \\citep{basu2026interpretability}, we provide mechanistic layer-level localization.",
          "     \\item \\textbf{Confound exclusion pipeline.} COMET translation quality ablation, token overlap analysis, and non-conflict baseline comparison exclude common confounds in cross-lingual probing.",
          " \\end{itemize}"
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

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01JEGtfVzoGRbWPzyiMNxosX`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "completed",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "in_progress",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "pending",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "pending",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "pending",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "pending",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "pending",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "pending",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "pending",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "pending",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "59b40d67-09aa-4f5d-b75b-fa7b94010646",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NboyGdWsuR6Rqh9Tfm9Nq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 56530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
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

_source line 48 · 2026-05-25T15:53:08.843Z_

<details><summary>↩ Tool result · `toolu_01JEGtfVzoGRbWPzyiMNxosX`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "915ad843-1fc2-484a-b6ff-a1a5496cf792",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "in_progress",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "pending",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "pending",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "pending",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "pending",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "pending",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "pending",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "in_progress",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "pending",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "pending",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "pending",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "pending",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "pending",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 49_

Now fixing experiments.tex — multiple locations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "470b715f-f81a-4e2f-9203-8788f1861b9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msj5Y21UqVpFcz28zTsFRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 57379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01CW96pRsuZzH2rcb69dHB9Y`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
  "old_string": "Llama achieves 77.6\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 72.1\\% on ZH$\\to$ZH.",
  "new_string": "Llama achieves 77.6\\% on EN$\\to$EN (peak at layer 15, 47\\% depth) and 72.1\\% on ZH$\\to$ZH."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "fb242a5e-0c63-4bc7-b15a-eaafc7e1799a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msj5Y21UqVpFcz28zTsFRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 57379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 51 · 2026-05-25T15:53:13.883Z_

<details><summary>↩ Tool result · `toolu_01CW96pRsuZzH2rcb69dHB9Y`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "14fd5720-c98a-4baa-8546-3b75b14bab1f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
    "oldString": "Llama achieves 77.6\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 72.1\\% on ZH$\\to$ZH.",
    "newString": "Llama achieves 77.6\\% on EN$\\to$EN (peak at layer 15, 47\\% depth) and 72.1\\% on ZH$\\to$ZH.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \\citep{team2024gemma}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.\nThe three models were independently verified, yielding only 3.5\\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\\% (Llama $\\cap$ Gemma) to 24.8\\% (Gemma $\\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET (wmt22-comet-da; \\citealt{rei2020comet}) back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\\ref{app:auroc}.\nAll CIs are computed via bootstrap resampling with paired differences for asymmetry estimation.\nA selectivity control \\citep{hewitt2019designing} with permuted labels on matched-condition data ($N{=}131$--$201$) yields near-chance accuracy (49.2--51.0\\%) across all models, confirming selectivity gaps of 21--40~pp.\nAll experiments used a single GPU; the boundary replication (Appendix~\\ref{app:boundary}) used an NVIDIA RTX PRO 6000.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nAll three models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.6\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 72.1\\% on ZH$\\to$ZH.\nQwen reaches 75.0\\% on EN$\\to$EN (peak at layer 24, 67\\% depth) and 72.6\\% on ZH$\\to$ZH.\nGemma attains 76.2\\% on EN$\\to$EN (peak at layer 24, 57\\% depth) and 71.0\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for all three models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across all three architectures and both languages.\n\n%% Figure 2: Layer-wise probe accuracy\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_layerwise_probes.pdf}\n\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p = 0.002$), coinciding with the ZH$\\to$ZH probe peak but not the EN$\\to$EN peak (L28). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}\n\\label{fig:layer_probe}\n\\end{figure*}\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}); this confirms that conflict representations partially overlap between English and Chinese.\nAll three models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nWe define $\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})$, computed via paired bootstrap.\nFor Llama, $\\Delta_{\\text{asym}} = +7.3$ percentage points (pp) with a 95\\% bootstrap CI of [0.4, 14.0] ($p = 0.038$); for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7]; for Gemma, $\\Delta_{\\text{asym}} = +6.6$ pp with CI [1.9, 11.1] ($p = 0.006$).\nWhile the Qwen CI marginally includes zero, the asymmetry is consistent in direction across all three architectures.\nThe magnitude of this asymmetry is consistent in direction and magnitude with the XNLI non-conflict baseline across all three architectures (\\S\\ref{sec:xnli_baseline}), and the consistent direction across all three models suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-seed balanced accuracy (\\%) at each direction's optimal layer. $\\Delta_{\\text{asym}}$ and 95\\% CIs from paired bootstrap ($n = 2{,}000$ resamples). Bold: best per-task direction.}\n\\label{tab:main_results}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B & Gemma-2-9B \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.6} & \\textbf{75.0} & \\textbf{76.2} \\\\\nZH $\\to$ ZH & 72.1 & 72.6 & 71.0 \\\\\nEN $\\to$ ZH & 59.6 & 67.3 & 62.9 \\\\\nZH $\\to$ EN & 70.6 & 73.2 & 70.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.3 [0.4, 14.0] & +7.2 [$-$0.6, 13.7] & +6.6 [1.9, 11.1] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 & 95.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 & 89.0 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 & 89.4 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} & \\textbf{97.5} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] & +7.8 [5.7, 10.0] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize Note: $\\Delta_{\\text{asym}}$ is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies.\n\\end{flushleft}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nAll three models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH; Gemma 95.6\\% EN, 89.0\\% ZH). These accuracies confirm that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7]; Gemma $\\Delta_{\\text{asym}} = +7.8$ pp, CI [5.7, 10.0] ($p < 0.001$).\nAll three XNLI CIs exclude zero and overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nFormal Two One-Sided Tests (TOST) equivalence tests ($\\pm$2~pp margin) were non-significant (all $p > 0.36$); post-hoc power analysis shows only 1.4\\% power at this margin given standard error (SE) $\\approx 4.2$~pp, with 80\\% power requiring a $\\pm$12.5~pp margin.\nBayesian equivalence testing yields a Bayes factor $\\text{BF}_{01} \\approx 1.5$ (half-normal prior, scale $= 5$~pp), providing directionally consistent but modest evidence for equivalence.\nCombined with the consistent direction across all six model$\\times$task combinations (binomial $p = 0.016$) and magnitudes clustering in [$+$6.0, $+$7.8~pp], these analyses support the ``consistency'' characterization: the non-significance reflects insufficient power, not meaningful differences.\n\n%% Figure 3: Asymmetry forest plot\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_asymmetry_forest.pdf}\n\\caption{Transfer asymmetry ($\\Delta_{\\text{asym}}$) with bootstrap 95\\% CIs ($n = 2{,}000$) for conflict and XNLI tasks across all three architectures (six data points). Conflict and XNLI CIs overlap substantially within each model, indicating that the ZH$\\to$EN advantage is a general cross-lingual property rather than conflict-specific. Grey dashed lines: $\\pm$2~pp exploratory equivalence margin (TOST power $= 1.4$\\%; see \\S\\ref{sec:xnli_baseline}).}\n\\label{fig:asymmetry_forest}\n\\end{figure}\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: lexical overlap between English and Chinese inputs and translation quality.\n\n\\paragraph{Token overlap and EN-DE control.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, already at the floor imposed by distinct writing systems.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$, $r^2 = 0.023$), running counter to the confound hypothesis.\nThe strongest evidence comes from a typological control: we translate the same Llama ConflictQA samples into German using the identical Qwen3-8B pipeline, where per-sample Jaccard similarity (14.8\\%) is approximately $4\\times$ higher than EN-ZH (3.8\\%).\nDespite this substantially higher lexical overlap, the EN$\\leftrightarrow$DE transfer asymmetry is near-zero ($\\Delta = +1.2$~pp, n.s.), ruling out shared tokens as a driver of the observed EN-ZH asymmetry (Table~\\ref{tab:confound}).\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles and compare EN$\\to$ZH probe accuracy across strata.\nQwen shows a reversed association ($\\Delta = -5.6$~pp, Fisher $p = 0.695$) and Llama a negligible one ($\\Delta = +1.7$~pp, $p = 0.761$), both inconsistent with translation quality driving probe transfer.\nGemma shows a non-significant trend in the confound direction ($\\Delta = +10.3$~pp, $p = 0.278$), but interpretation is limited by the near-chance baseline accuracy of the EN$\\to$ZH probe at L17 (58.8\\%), placing this analysis in a low-power regime.\nWith a minimum detectable difference of 25.3~pp at 80\\% power ($n \\approx 56$ per tercile), the COMET tercile analysis can neither confirm nor exclude a moderate translation quality effect; it serves as supplementary evidence alongside the token overlap and EN-DE controls.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\nCOMET tercile & Gemma & $\\Delta = +10.3$ pp & 0.278 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_l$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_l$ into the last-token residual stream at a target layer during inference.\nWe sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) following prior steering conventions \\citep{turner2023activation, marks2024geometry} and report results at all tested values.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces bidirectional causal effects (Figure~\\ref{fig:steering_viz}; Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$; 4 p$\\to$c flips), while negative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% ($p < 0.001$; 5 c$\\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$).\nAll-position injection at L13 produces identical results; the causal signal is concentrated at the final token.\nSteering at nearby L16 (50\\% depth, just three layers away) showed no significant effect (all $p > 0.12$), consistent with a narrow causal window.\nUnder a conservative family-wise correction across all 30 tests (3 layers $\\times$ 10 $\\alpha$ values, threshold $p < 0.00167$), L13 remains significant ($\\alpha = +10$, $p = 0.0003$).\nAn independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}\n\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\n\\label{fig:steering_viz}\n\\end{figure}\n\n\\paragraph{Negative layers and coherence collapse.}\nSteering at L28 (probe peak, 88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\nAt extreme magnitude ($\\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.\n\n\\paragraph{Causal localization (Llama).}\nIn Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.\nAn independent replication with a separately trained probe (seed=123, different train/test split) confirms the L13 causal effect: 2/6 positive-direction $\\alpha$ configurations survive per-layer Bonferroni correction ($k{=}6$, $p < 0.0083$), matching the original 2/6 (Appendix~\\ref{app:seed_replication}).\n\n\\paragraph{Cross-model steering.}\nCross-model experiments use the reduced 6-value $\\alpha$ grid ($k{=}6$, per-layer threshold $p < 0.0083$; \\S\\ref{sec:steering_method}).\nQwen steering at L14 (39\\%, $n_{\\text{test}} = 131$; probe accuracy 71.0\\%) produced no significant effect at any $\\alpha$ (best $p = 0.785$) and zero directional flips.\nGemma-2-9B-IT L17 (40\\% depth) provides a stronger test: with 88.9\\% probe accuracy, the highest among all three models (exceeding both Llama 76.1\\% and Qwen 71.0\\%), steering produced no significant change at any $\\alpha$ (best $p = 0.448$) and zero directional flips ($n_{\\text{test}} = 171$), ruling out probe quality as a confound and confirming that the causal influence of probe-weight directions is architecture-dependent.\nAUROC analysis confirms this pattern: Gemma achieves 0.93 AUROC (vs.\\ Llama 0.98, Qwen 0.77; Appendix~\\ref{app:auroc}), yet steering produces zero causal effect.\nAppendix~\\ref{app:steering_config} reports matched-condition results at three layers per model (${\\sim}$36--43\\% depth), all confirming the null.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Bonferroni-corrected significance threshold $p < 0.005$ ($k = 10$). Significant results in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL16 & 50\\% & $+5$ & 8.8 & 8.1 & 1.000 & \\\\\nL16 & 50\\% & $+10$ & 18.4 & 11.0 & 0.123 & \\\\\nL16 & 50\\% & $+20$ & 22.8 & 24.3 & 0.886 & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B ($n_{\\text{test}} = 131$)}} \\\\\nL14 & 39\\% & best & \\multicolumn{2}{c}{n.s.} & 0.785 & 0 dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Gemma-2-9B-IT ($n_{\\text{test}} = 171$)$^{\\ddagger}$}} \\\\\nL17 & 40\\% & best & \\multicolumn{2}{c}{n.s.} & 0.448 & 0 dir. \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes. $^{\\ddagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 7,
        "newStart": 30,
        "newLines": 7,
        "lines": [
          " ",
          " Table~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.",
          " All three models encode linearly detectable conflict signals in their residual streams.",
          "-Llama achieves 77.6\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 72.1\\% on ZH$\\to$ZH.",
          "+Llama achieves 77.6\\% on EN$\\to$EN (peak at layer 15, 47\\% depth) and 72.1\\% on ZH$\\to$ZH.",
          " Qwen reaches 75.0\\% on EN$\\to$EN (peak at layer 24, 67\\% depth) and 72.6\\% on ZH$\\to$ZH.",
          " Gemma attains 76.2\\% on EN$\\to$EN (peak at layer 24, 57\\% depth) and 71.0\\% on ZH$\\to$ZH.",
          " All within-language accuracies are significantly above chance (binomial $p < 0.001$)."
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01UTzqQpYih1GcW6pkuVosve`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
  "old_string": "\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p = 0.002$), coinciding with the ZH$\\to$ZH probe peak but not the EN$\\to$EN peak (L28). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}",
  "new_string": "\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p < 0.001$), near the EN$\\to$EN probe peak (L15). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "02608e70-3bbd-4499-94e2-0b98ca36a13f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msj5Y21UqVpFcz28zTsFRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 57379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 53 · 2026-05-25T15:53:20.125Z_

<details><summary>↩ Tool result · `toolu_01UTzqQpYih1GcW6pkuVosve`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "6585d984-4ef3-4598-bf9e-b7ceeea69876",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
    "oldString": "\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p = 0.002$), coinciding with the ZH$\\to$ZH probe peak but not the EN$\\to$EN peak (L28). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}",
    "newString": "\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p < 0.001$), near the EN$\\to$EN probe peak (L15). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \\citep{team2024gemma}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.\nThe three models were independently verified, yielding only 3.5\\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\\% (Llama $\\cap$ Gemma) to 24.8\\% (Gemma $\\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET (wmt22-comet-da; \\citealt{rei2020comet}) back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\\ref{app:auroc}.\nAll CIs are computed via bootstrap resampling with paired differences for asymmetry estimation.\nA selectivity control \\citep{hewitt2019designing} with permuted labels on matched-condition data ($N{=}131$--$201$) yields near-chance accuracy (49.2--51.0\\%) across all models, confirming selectivity gaps of 21--40~pp.\nAll experiments used a single GPU; the boundary replication (Appendix~\\ref{app:boundary}) used an NVIDIA RTX PRO 6000.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nAll three models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.6\\% on EN$\\to$EN (peak at layer 15, 47\\% depth) and 72.1\\% on ZH$\\to$ZH.\nQwen reaches 75.0\\% on EN$\\to$EN (peak at layer 24, 67\\% depth) and 72.6\\% on ZH$\\to$ZH.\nGemma attains 76.2\\% on EN$\\to$EN (peak at layer 24, 57\\% depth) and 71.0\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for all three models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across all three architectures and both languages.\n\n%% Figure 2: Layer-wise probe accuracy\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_layerwise_probes.pdf}\n\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p = 0.002$), coinciding with the ZH$\\to$ZH probe peak but not the EN$\\to$EN peak (L28). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}\n\\label{fig:layer_probe}\n\\end{figure*}\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}); this confirms that conflict representations partially overlap between English and Chinese.\nAll three models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nWe define $\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})$, computed via paired bootstrap.\nFor Llama, $\\Delta_{\\text{asym}} = +7.3$ percentage points (pp) with a 95\\% bootstrap CI of [0.4, 14.0] ($p = 0.038$); for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7]; for Gemma, $\\Delta_{\\text{asym}} = +6.6$ pp with CI [1.9, 11.1] ($p = 0.006$).\nWhile the Qwen CI marginally includes zero, the asymmetry is consistent in direction across all three architectures.\nThe magnitude of this asymmetry is consistent in direction and magnitude with the XNLI non-conflict baseline across all three architectures (\\S\\ref{sec:xnli_baseline}), and the consistent direction across all three models suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-seed balanced accuracy (\\%) at each direction's optimal layer. $\\Delta_{\\text{asym}}$ and 95\\% CIs from paired bootstrap ($n = 2{,}000$ resamples). Bold: best per-task direction.}\n\\label{tab:main_results}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B & Gemma-2-9B \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.6} & \\textbf{75.0} & \\textbf{76.2} \\\\\nZH $\\to$ ZH & 72.1 & 72.6 & 71.0 \\\\\nEN $\\to$ ZH & 59.6 & 67.3 & 62.9 \\\\\nZH $\\to$ EN & 70.6 & 73.2 & 70.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.3 [0.4, 14.0] & +7.2 [$-$0.6, 13.7] & +6.6 [1.9, 11.1] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 & 95.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 & 89.0 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 & 89.4 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} & \\textbf{97.5} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] & +7.8 [5.7, 10.0] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize Note: $\\Delta_{\\text{asym}}$ is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies.\n\\end{flushleft}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nAll three models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH; Gemma 95.6\\% EN, 89.0\\% ZH). These accuracies confirm that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7]; Gemma $\\Delta_{\\text{asym}} = +7.8$ pp, CI [5.7, 10.0] ($p < 0.001$).\nAll three XNLI CIs exclude zero and overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nFormal Two One-Sided Tests (TOST) equivalence tests ($\\pm$2~pp margin) were non-significant (all $p > 0.36$); post-hoc power analysis shows only 1.4\\% power at this margin given standard error (SE) $\\approx 4.2$~pp, with 80\\% power requiring a $\\pm$12.5~pp margin.\nBayesian equivalence testing yields a Bayes factor $\\text{BF}_{01} \\approx 1.5$ (half-normal prior, scale $= 5$~pp), providing directionally consistent but modest evidence for equivalence.\nCombined with the consistent direction across all six model$\\times$task combinations (binomial $p = 0.016$) and magnitudes clustering in [$+$6.0, $+$7.8~pp], these analyses support the ``consistency'' characterization: the non-significance reflects insufficient power, not meaningful differences.\n\n%% Figure 3: Asymmetry forest plot\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_asymmetry_forest.pdf}\n\\caption{Transfer asymmetry ($\\Delta_{\\text{asym}}$) with bootstrap 95\\% CIs ($n = 2{,}000$) for conflict and XNLI tasks across all three architectures (six data points). Conflict and XNLI CIs overlap substantially within each model, indicating that the ZH$\\to$EN advantage is a general cross-lingual property rather than conflict-specific. Grey dashed lines: $\\pm$2~pp exploratory equivalence margin (TOST power $= 1.4$\\%; see \\S\\ref{sec:xnli_baseline}).}\n\\label{fig:asymmetry_forest}\n\\end{figure}\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: lexical overlap between English and Chinese inputs and translation quality.\n\n\\paragraph{Token overlap and EN-DE control.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, already at the floor imposed by distinct writing systems.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$, $r^2 = 0.023$), running counter to the confound hypothesis.\nThe strongest evidence comes from a typological control: we translate the same Llama ConflictQA samples into German using the identical Qwen3-8B pipeline, where per-sample Jaccard similarity (14.8\\%) is approximately $4\\times$ higher than EN-ZH (3.8\\%).\nDespite this substantially higher lexical overlap, the EN$\\leftrightarrow$DE transfer asymmetry is near-zero ($\\Delta = +1.2$~pp, n.s.), ruling out shared tokens as a driver of the observed EN-ZH asymmetry (Table~\\ref{tab:confound}).\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles and compare EN$\\to$ZH probe accuracy across strata.\nQwen shows a reversed association ($\\Delta = -5.6$~pp, Fisher $p = 0.695$) and Llama a negligible one ($\\Delta = +1.7$~pp, $p = 0.761$), both inconsistent with translation quality driving probe transfer.\nGemma shows a non-significant trend in the confound direction ($\\Delta = +10.3$~pp, $p = 0.278$), but interpretation is limited by the near-chance baseline accuracy of the EN$\\to$ZH probe at L17 (58.8\\%), placing this analysis in a low-power regime.\nWith a minimum detectable difference of 25.3~pp at 80\\% power ($n \\approx 56$ per tercile), the COMET tercile analysis can neither confirm nor exclude a moderate translation quality effect; it serves as supplementary evidence alongside the token overlap and EN-DE controls.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\nCOMET tercile & Gemma & $\\Delta = +10.3$ pp & 0.278 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_l$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_l$ into the last-token residual stream at a target layer during inference.\nWe sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) following prior steering conventions \\citep{turner2023activation, marks2024geometry} and report results at all tested values.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces bidirectional causal effects (Figure~\\ref{fig:steering_viz}; Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$; 4 p$\\to$c flips), while negative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% ($p < 0.001$; 5 c$\\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$).\nAll-position injection at L13 produces identical results; the causal signal is concentrated at the final token.\nSteering at nearby L16 (50\\% depth, just three layers away) showed no significant effect (all $p > 0.12$), consistent with a narrow causal window.\nUnder a conservative family-wise correction across all 30 tests (3 layers $\\times$ 10 $\\alpha$ values, threshold $p < 0.00167$), L13 remains significant ($\\alpha = +10$, $p = 0.0003$).\nAn independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}\n\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\n\\label{fig:steering_viz}\n\\end{figure}\n\n\\paragraph{Negative layers and coherence collapse.}\nSteering at L28 (probe peak, 88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\nAt extreme magnitude ($\\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.\n\n\\paragraph{Causal localization (Llama).}\nIn Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.\nAn independent replication with a separately trained probe (seed=123, different train/test split) confirms the L13 causal effect: 2/6 positive-direction $\\alpha$ configurations survive per-layer Bonferroni correction ($k{=}6$, $p < 0.0083$), matching the original 2/6 (Appendix~\\ref{app:seed_replication}).\n\n\\paragraph{Cross-model steering.}\nCross-model experiments use the reduced 6-value $\\alpha$ grid ($k{=}6$, per-layer threshold $p < 0.0083$; \\S\\ref{sec:steering_method}).\nQwen steering at L14 (39\\%, $n_{\\text{test}} = 131$; probe accuracy 71.0\\%) produced no significant effect at any $\\alpha$ (best $p = 0.785$) and zero directional flips.\nGemma-2-9B-IT L17 (40\\% depth) provides a stronger test: with 88.9\\% probe accuracy, the highest among all three models (exceeding both Llama 76.1\\% and Qwen 71.0\\%), steering produced no significant change at any $\\alpha$ (best $p = 0.448$) and zero directional flips ($n_{\\text{test}} = 171$), ruling out probe quality as a confound and confirming that the causal influence of probe-weight directions is architecture-dependent.\nAUROC analysis confirms this pattern: Gemma achieves 0.93 AUROC (vs.\\ Llama 0.98, Qwen 0.77; Appendix~\\ref{app:auroc}), yet steering produces zero causal effect.\nAppendix~\\ref{app:steering_config} reports matched-condition results at three layers per model (${\\sim}$36--43\\% depth), all confirming the null.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Bonferroni-corrected significance threshold $p < 0.005$ ($k = 10$). Significant results in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL16 & 50\\% & $+5$ & 8.8 & 8.1 & 1.000 & \\\\\nL16 & 50\\% & $+10$ & 18.4 & 11.0 & 0.123 & \\\\\nL16 & 50\\% & $+20$ & 22.8 & 24.3 & 0.886 & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B ($n_{\\text{test}} = 131$)}} \\\\\nL14 & 39\\% & best & \\multicolumn{2}{c}{n.s.} & 0.785 & 0 dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Gemma-2-9B-IT ($n_{\\text{test}} = 171$)$^{\\ddagger}$}} \\\\\nL17 & 40\\% & best & \\multicolumn{2}{c}{n.s.} & 0.448 & 0 dir. \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes. $^{\\ddagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}",
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " \\begin{figure*}[t]",
          " \\centering",
          " \\includegraphics[width=\\textwidth]{fig3_layerwise_probes.pdf}",
          "-\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p = 0.002$), coinciding with the ZH$\\to$ZH probe peak but not the EN$\\to$EN peak (L28). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}",
          "+\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p < 0.001$), near the EN$\\to$EN probe peak (L15). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}",
          " \\label{fig:layer_probe}",
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

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_014Pj1Ezp2CSeEXASpRKcBin`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
  "old_string": "Flip rates at L28 (88%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}",
  "new_string": "Flip rates at L28 (88\\%) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c9ca6ddc-627c-47fa-945b-f84312f1f053",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msj5Y21UqVpFcz28zTsFRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 57379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 55 · 2026-05-25T15:53:22.316Z_

<details><summary>↩ Tool result · reported error · `toolu_014Pj1Ezp2CSeEXASpRKcBin`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: Flip rates at L28 (88%, probe peak) and L18 (56\%, MLP peak) remain at control levels (Table~\ref{tab:steering}).}&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "60aa14fb-d445-4446-a097-c8a1e27bd4d0",
  "tool_use_result": "Error: String to replace not found in file.\nString: Flip rates at L28 (88%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}"
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Edit · `toolu_01M8jw4pgtvTWMWrqiDvRahr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
  "old_string": "Steering at L28 (probe peak, 88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).",
  "new_string": "Steering at L28 (88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "2e460633-9b13-4b2b-8af6-d5794a0431b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msj5Y21UqVpFcz28zTsFRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 57379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 57 · 2026-05-25T15:53:25.233Z_

<details><summary>↩ Tool result · `toolu_01M8jw4pgtvTWMWrqiDvRahr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "59e9ba0c-690f-4da8-8ab8-699e53059f07",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
    "oldString": "Steering at L28 (probe peak, 88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).",
    "newString": "Steering at L28 (88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \\citep{team2024gemma}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.\nThe three models were independently verified, yielding only 3.5\\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\\% (Llama $\\cap$ Gemma) to 24.8\\% (Gemma $\\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET (wmt22-comet-da; \\citealt{rei2020comet}) back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\\ref{app:auroc}.\nAll CIs are computed via bootstrap resampling with paired differences for asymmetry estimation.\nA selectivity control \\citep{hewitt2019designing} with permuted labels on matched-condition data ($N{=}131$--$201$) yields near-chance accuracy (49.2--51.0\\%) across all models, confirming selectivity gaps of 21--40~pp.\nAll experiments used a single GPU; the boundary replication (Appendix~\\ref{app:boundary}) used an NVIDIA RTX PRO 6000.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nAll three models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.6\\% on EN$\\to$EN (peak at layer 15, 47\\% depth) and 72.1\\% on ZH$\\to$ZH.\nQwen reaches 75.0\\% on EN$\\to$EN (peak at layer 24, 67\\% depth) and 72.6\\% on ZH$\\to$ZH.\nGemma attains 76.2\\% on EN$\\to$EN (peak at layer 24, 57\\% depth) and 71.0\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for all three models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across all three architectures and both languages.\n\n%% Figure 2: Layer-wise probe accuracy\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_layerwise_probes.pdf}\n\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p < 0.001$), near the EN$\\to$EN probe peak (L15). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}\n\\label{fig:layer_probe}\n\\end{figure*}\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}); this confirms that conflict representations partially overlap between English and Chinese.\nAll three models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nWe define $\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})$, computed via paired bootstrap.\nFor Llama, $\\Delta_{\\text{asym}} = +7.3$ percentage points (pp) with a 95\\% bootstrap CI of [0.4, 14.0] ($p = 0.038$); for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7]; for Gemma, $\\Delta_{\\text{asym}} = +6.6$ pp with CI [1.9, 11.1] ($p = 0.006$).\nWhile the Qwen CI marginally includes zero, the asymmetry is consistent in direction across all three architectures.\nThe magnitude of this asymmetry is consistent in direction and magnitude with the XNLI non-conflict baseline across all three architectures (\\S\\ref{sec:xnli_baseline}), and the consistent direction across all three models suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-seed balanced accuracy (\\%) at each direction's optimal layer. $\\Delta_{\\text{asym}}$ and 95\\% CIs from paired bootstrap ($n = 2{,}000$ resamples). Bold: best per-task direction.}\n\\label{tab:main_results}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B & Gemma-2-9B \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.6} & \\textbf{75.0} & \\textbf{76.2} \\\\\nZH $\\to$ ZH & 72.1 & 72.6 & 71.0 \\\\\nEN $\\to$ ZH & 59.6 & 67.3 & 62.9 \\\\\nZH $\\to$ EN & 70.6 & 73.2 & 70.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.3 [0.4, 14.0] & +7.2 [$-$0.6, 13.7] & +6.6 [1.9, 11.1] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 & 95.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 & 89.0 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 & 89.4 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} & \\textbf{97.5} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] & +7.8 [5.7, 10.0] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize Note: $\\Delta_{\\text{asym}}$ is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies.\n\\end{flushleft}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nAll three models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH; Gemma 95.6\\% EN, 89.0\\% ZH). These accuracies confirm that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7]; Gemma $\\Delta_{\\text{asym}} = +7.8$ pp, CI [5.7, 10.0] ($p < 0.001$).\nAll three XNLI CIs exclude zero and overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nFormal Two One-Sided Tests (TOST) equivalence tests ($\\pm$2~pp margin) were non-significant (all $p > 0.36$); post-hoc power analysis shows only 1.4\\% power at this margin given standard error (SE) $\\approx 4.2$~pp, with 80\\% power requiring a $\\pm$12.5~pp margin.\nBayesian equivalence testing yields a Bayes factor $\\text{BF}_{01} \\approx 1.5$ (half-normal prior, scale $= 5$~pp), providing directionally consistent but modest evidence for equivalence.\nCombined with the consistent direction across all six model$\\times$task combinations (binomial $p = 0.016$) and magnitudes clustering in [$+$6.0, $+$7.8~pp], these analyses support the ``consistency'' characterization: the non-significance reflects insufficient power, not meaningful differences.\n\n%% Figure 3: Asymmetry forest plot\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_asymmetry_forest.pdf}\n\\caption{Transfer asymmetry ($\\Delta_{\\text{asym}}$) with bootstrap 95\\% CIs ($n = 2{,}000$) for conflict and XNLI tasks across all three architectures (six data points). Conflict and XNLI CIs overlap substantially within each model, indicating that the ZH$\\to$EN advantage is a general cross-lingual property rather than conflict-specific. Grey dashed lines: $\\pm$2~pp exploratory equivalence margin (TOST power $= 1.4$\\%; see \\S\\ref{sec:xnli_baseline}).}\n\\label{fig:asymmetry_forest}\n\\end{figure}\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: lexical overlap between English and Chinese inputs and translation quality.\n\n\\paragraph{Token overlap and EN-DE control.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, already at the floor imposed by distinct writing systems.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$, $r^2 = 0.023$), running counter to the confound hypothesis.\nThe strongest evidence comes from a typological control: we translate the same Llama ConflictQA samples into German using the identical Qwen3-8B pipeline, where per-sample Jaccard similarity (14.8\\%) is approximately $4\\times$ higher than EN-ZH (3.8\\%).\nDespite this substantially higher lexical overlap, the EN$\\leftrightarrow$DE transfer asymmetry is near-zero ($\\Delta = +1.2$~pp, n.s.), ruling out shared tokens as a driver of the observed EN-ZH asymmetry (Table~\\ref{tab:confound}).\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles and compare EN$\\to$ZH probe accuracy across strata.\nQwen shows a reversed association ($\\Delta = -5.6$~pp, Fisher $p = 0.695$) and Llama a negligible one ($\\Delta = +1.7$~pp, $p = 0.761$), both inconsistent with translation quality driving probe transfer.\nGemma shows a non-significant trend in the confound direction ($\\Delta = +10.3$~pp, $p = 0.278$), but interpretation is limited by the near-chance baseline accuracy of the EN$\\to$ZH probe at L17 (58.8\\%), placing this analysis in a low-power regime.\nWith a minimum detectable difference of 25.3~pp at 80\\% power ($n \\approx 56$ per tercile), the COMET tercile analysis can neither confirm nor exclude a moderate translation quality effect; it serves as supplementary evidence alongside the token overlap and EN-DE controls.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\nCOMET tercile & Gemma & $\\Delta = +10.3$ pp & 0.278 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_l$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_l$ into the last-token residual stream at a target layer during inference.\nWe sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) following prior steering conventions \\citep{turner2023activation, marks2024geometry} and report results at all tested values.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces bidirectional causal effects (Figure~\\ref{fig:steering_viz}; Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$; 4 p$\\to$c flips), while negative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% ($p < 0.001$; 5 c$\\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$).\nAll-position injection at L13 produces identical results; the causal signal is concentrated at the final token.\nSteering at nearby L16 (50\\% depth, just three layers away) showed no significant effect (all $p > 0.12$), consistent with a narrow causal window.\nUnder a conservative family-wise correction across all 30 tests (3 layers $\\times$ 10 $\\alpha$ values, threshold $p < 0.00167$), L13 remains significant ($\\alpha = +10$, $p = 0.0003$).\nAn independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}\n\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\n\\label{fig:steering_viz}\n\\end{figure}\n\n\\paragraph{Negative layers and coherence collapse.}\nSteering at L28 (probe peak, 88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\nAt extreme magnitude ($\\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.\n\n\\paragraph{Causal localization (Llama).}\nIn Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.\nAn independent replication with a separately trained probe (seed=123, different train/test split) confirms the L13 causal effect: 2/6 positive-direction $\\alpha$ configurations survive per-layer Bonferroni correction ($k{=}6$, $p < 0.0083$), matching the original 2/6 (Appendix~\\ref{app:seed_replication}).\n\n\\paragraph{Cross-model steering.}\nCross-model experiments use the reduced 6-value $\\alpha$ grid ($k{=}6$, per-layer threshold $p < 0.0083$; \\S\\ref{sec:steering_method}).\nQwen steering at L14 (39\\%, $n_{\\text{test}} = 131$; probe accuracy 71.0\\%) produced no significant effect at any $\\alpha$ (best $p = 0.785$) and zero directional flips.\nGemma-2-9B-IT L17 (40\\% depth) provides a stronger test: with 88.9\\% probe accuracy, the highest among all three models (exceeding both Llama 76.1\\% and Qwen 71.0\\%), steering produced no significant change at any $\\alpha$ (best $p = 0.448$) and zero directional flips ($n_{\\text{test}} = 171$), ruling out probe quality as a confound and confirming that the causal influence of probe-weight directions is architecture-dependent.\nAUROC analysis confirms this pattern: Gemma achieves 0.93 AUROC (vs.\\ Llama 0.98, Qwen 0.77; Appendix~\\ref{app:auroc}), yet steering produces zero causal effect.\nAppendix~\\ref{app:steering_config} reports matched-condition results at three layers per model (${\\sim}$36--43\\% depth), all confirming the null.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Bonferroni-corrected significance threshold $p < 0.005$ ($k = 10$). Significant results in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL16 & 50\\% & $+5$ & 8.8 & 8.1 & 1.000 & \\\\\nL16 & 50\\% & $+10$ & 18.4 & 11.0 & 0.123 & \\\\\nL16 & 50\\% & $+20$ & 22.8 & 24.3 & 0.886 & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B ($n_{\\text{test}} = 131$)}} \\\\\nL14 & 39\\% & best & \\multicolumn{2}{c}{n.s.} & 0.785 & 0 dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Gemma-2-9B-IT ($n_{\\text{test}} = 171$)$^{\\ddagger}$}} \\\\\nL17 & 40\\% & best & \\multicolumn{2}{c}{n.s.} & 0.448 & 0 dir. \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes. $^{\\ddagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}",
    "structuredPatch": [
      {
        "oldStart": 167,
        "oldLines": 7,
        "newStart": 167,
        "newLines": 7,
        "lines": [
          " \\end{figure}",
          " ",
          " \\paragraph{Negative layers and coherence collapse.}",
          "-Steering at L28 (probe peak, 88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).",
          "+Steering at L28 (88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).",
          " At extreme magnitude ($\\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.",
          " ",
          " \\paragraph{Causal localization (Llama).}"
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

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_01WsMs6Mz8gjRvJcTyDNHJ9x`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
  "old_string": "In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.",
  "new_string": "In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth), near but distinct from the EN$\\to$EN probe peak (L15, 47\\%): upper layers (e.g., L28) retain a detectable signal but lack causal influence, while mid-layers host the computation that determines the outcome."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "e72326b5-e6fe-4063-82c0-c2f865bd906f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msj5Y21UqVpFcz28zTsFRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 57379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 586
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

_source line 59 · 2026-05-25T15:53:29.687Z_

<details><summary>↩ Tool result · `toolu_01WsMs6Mz8gjRvJcTyDNHJ9x`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "38d5b7c1-c74c-40fd-bdae-368cfbd7a3a5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
    "oldString": "In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.",
    "newString": "In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth), near but distinct from the EN$\\to$EN probe peak (L15, 47\\%): upper layers (e.g., L28) retain a detectable signal but lack causal influence, while mid-layers host the computation that determines the outcome.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \\citep{team2024gemma}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.\nThe three models were independently verified, yielding only 3.5\\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\\% (Llama $\\cap$ Gemma) to 24.8\\% (Gemma $\\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET (wmt22-comet-da; \\citealt{rei2020comet}) back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\\ref{app:auroc}.\nAll CIs are computed via bootstrap resampling with paired differences for asymmetry estimation.\nA selectivity control \\citep{hewitt2019designing} with permuted labels on matched-condition data ($N{=}131$--$201$) yields near-chance accuracy (49.2--51.0\\%) across all models, confirming selectivity gaps of 21--40~pp.\nAll experiments used a single GPU; the boundary replication (Appendix~\\ref{app:boundary}) used an NVIDIA RTX PRO 6000.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nAll three models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.6\\% on EN$\\to$EN (peak at layer 15, 47\\% depth) and 72.1\\% on ZH$\\to$ZH.\nQwen reaches 75.0\\% on EN$\\to$EN (peak at layer 24, 67\\% depth) and 72.6\\% on ZH$\\to$ZH.\nGemma attains 76.2\\% on EN$\\to$EN (peak at layer 24, 57\\% depth) and 71.0\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for all three models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across all three architectures and both languages.\n\n%% Figure 2: Layer-wise probe accuracy\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_layerwise_probes.pdf}\n\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p < 0.001$), near the EN$\\to$EN probe peak (L15). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}\n\\label{fig:layer_probe}\n\\end{figure*}\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}); this confirms that conflict representations partially overlap between English and Chinese.\nAll three models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nWe define $\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})$, computed via paired bootstrap.\nFor Llama, $\\Delta_{\\text{asym}} = +7.3$ percentage points (pp) with a 95\\% bootstrap CI of [0.4, 14.0] ($p = 0.038$); for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7]; for Gemma, $\\Delta_{\\text{asym}} = +6.6$ pp with CI [1.9, 11.1] ($p = 0.006$).\nWhile the Qwen CI marginally includes zero, the asymmetry is consistent in direction across all three architectures.\nThe magnitude of this asymmetry is consistent in direction and magnitude with the XNLI non-conflict baseline across all three architectures (\\S\\ref{sec:xnli_baseline}), and the consistent direction across all three models suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-seed balanced accuracy (\\%) at each direction's optimal layer. $\\Delta_{\\text{asym}}$ and 95\\% CIs from paired bootstrap ($n = 2{,}000$ resamples). Bold: best per-task direction.}\n\\label{tab:main_results}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B & Gemma-2-9B \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.6} & \\textbf{75.0} & \\textbf{76.2} \\\\\nZH $\\to$ ZH & 72.1 & 72.6 & 71.0 \\\\\nEN $\\to$ ZH & 59.6 & 67.3 & 62.9 \\\\\nZH $\\to$ EN & 70.6 & 73.2 & 70.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.3 [0.4, 14.0] & +7.2 [$-$0.6, 13.7] & +6.6 [1.9, 11.1] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 & 95.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 & 89.0 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 & 89.4 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} & \\textbf{97.5} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] & +7.8 [5.7, 10.0] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize Note: $\\Delta_{\\text{asym}}$ is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies.\n\\end{flushleft}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nAll three models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH; Gemma 95.6\\% EN, 89.0\\% ZH). These accuracies confirm that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7]; Gemma $\\Delta_{\\text{asym}} = +7.8$ pp, CI [5.7, 10.0] ($p < 0.001$).\nAll three XNLI CIs exclude zero and overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nFormal Two One-Sided Tests (TOST) equivalence tests ($\\pm$2~pp margin) were non-significant (all $p > 0.36$); post-hoc power analysis shows only 1.4\\% power at this margin given standard error (SE) $\\approx 4.2$~pp, with 80\\% power requiring a $\\pm$12.5~pp margin.\nBayesian equivalence testing yields a Bayes factor $\\text{BF}_{01} \\approx 1.5$ (half-normal prior, scale $= 5$~pp), providing directionally consistent but modest evidence for equivalence.\nCombined with the consistent direction across all six model$\\times$task combinations (binomial $p = 0.016$) and magnitudes clustering in [$+$6.0, $+$7.8~pp], these analyses support the ``consistency'' characterization: the non-significance reflects insufficient power, not meaningful differences.\n\n%% Figure 3: Asymmetry forest plot\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_asymmetry_forest.pdf}\n\\caption{Transfer asymmetry ($\\Delta_{\\text{asym}}$) with bootstrap 95\\% CIs ($n = 2{,}000$) for conflict and XNLI tasks across all three architectures (six data points). Conflict and XNLI CIs overlap substantially within each model, indicating that the ZH$\\to$EN advantage is a general cross-lingual property rather than conflict-specific. Grey dashed lines: $\\pm$2~pp exploratory equivalence margin (TOST power $= 1.4$\\%; see \\S\\ref{sec:xnli_baseline}).}\n\\label{fig:asymmetry_forest}\n\\end{figure}\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: lexical overlap between English and Chinese inputs and translation quality.\n\n\\paragraph{Token overlap and EN-DE control.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, already at the floor imposed by distinct writing systems.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$, $r^2 = 0.023$), running counter to the confound hypothesis.\nThe strongest evidence comes from a typological control: we translate the same Llama ConflictQA samples into German using the identical Qwen3-8B pipeline, where per-sample Jaccard similarity (14.8\\%) is approximately $4\\times$ higher than EN-ZH (3.8\\%).\nDespite this substantially higher lexical overlap, the EN$\\leftrightarrow$DE transfer asymmetry is near-zero ($\\Delta = +1.2$~pp, n.s.), ruling out shared tokens as a driver of the observed EN-ZH asymmetry (Table~\\ref{tab:confound}).\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles and compare EN$\\to$ZH probe accuracy across strata.\nQwen shows a reversed association ($\\Delta = -5.6$~pp, Fisher $p = 0.695$) and Llama a negligible one ($\\Delta = +1.7$~pp, $p = 0.761$), both inconsistent with translation quality driving probe transfer.\nGemma shows a non-significant trend in the confound direction ($\\Delta = +10.3$~pp, $p = 0.278$), but interpretation is limited by the near-chance baseline accuracy of the EN$\\to$ZH probe at L17 (58.8\\%), placing this analysis in a low-power regime.\nWith a minimum detectable difference of 25.3~pp at 80\\% power ($n \\approx 56$ per tercile), the COMET tercile analysis can neither confirm nor exclude a moderate translation quality effect; it serves as supplementary evidence alongside the token overlap and EN-DE controls.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\nCOMET tercile & Gemma & $\\Delta = +10.3$ pp & 0.278 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_l$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_l$ into the last-token residual stream at a target layer during inference.\nWe sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) following prior steering conventions \\citep{turner2023activation, marks2024geometry} and report results at all tested values.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces bidirectional causal effects (Figure~\\ref{fig:steering_viz}; Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$; 4 p$\\to$c flips), while negative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% ($p < 0.001$; 5 c$\\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$).\nAll-position injection at L13 produces identical results; the causal signal is concentrated at the final token.\nSteering at nearby L16 (50\\% depth, just three layers away) showed no significant effect (all $p > 0.12$), consistent with a narrow causal window.\nUnder a conservative family-wise correction across all 30 tests (3 layers $\\times$ 10 $\\alpha$ values, threshold $p < 0.00167$), L13 remains significant ($\\alpha = +10$, $p = 0.0003$).\nAn independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}\n\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\n\\label{fig:steering_viz}\n\\end{figure}\n\n\\paragraph{Negative layers and coherence collapse.}\nSteering at L28 (88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\nAt extreme magnitude ($\\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.\n\n\\paragraph{Causal localization (Llama).}\nIn Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.\nAn independent replication with a separately trained probe (seed=123, different train/test split) confirms the L13 causal effect: 2/6 positive-direction $\\alpha$ configurations survive per-layer Bonferroni correction ($k{=}6$, $p < 0.0083$), matching the original 2/6 (Appendix~\\ref{app:seed_replication}).\n\n\\paragraph{Cross-model steering.}\nCross-model experiments use the reduced 6-value $\\alpha$ grid ($k{=}6$, per-layer threshold $p < 0.0083$; \\S\\ref{sec:steering_method}).\nQwen steering at L14 (39\\%, $n_{\\text{test}} = 131$; probe accuracy 71.0\\%) produced no significant effect at any $\\alpha$ (best $p = 0.785$) and zero directional flips.\nGemma-2-9B-IT L17 (40\\% depth) provides a stronger test: with 88.9\\% probe accuracy, the highest among all three models (exceeding both Llama 76.1\\% and Qwen 71.0\\%), steering produced no significant change at any $\\alpha$ (best $p = 0.448$) and zero directional flips ($n_{\\text{test}} = 171$), ruling out probe quality as a confound and confirming that the causal influence of probe-weight directions is architecture-dependent.\nAUROC analysis confirms this pattern: Gemma achieves 0.93 AUROC (vs.\\ Llama 0.98, Qwen 0.77; Appendix~\\ref{app:auroc}), yet steering produces zero causal effect.\nAppendix~\\ref{app:steering_config} reports matched-condition results at three layers per model (${\\sim}$36--43\\% depth), all confirming the null.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Bonferroni-corrected significance threshold $p < 0.005$ ($k = 10$). Significant results in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL16 & 50\\% & $+5$ & 8.8 & 8.1 & 1.000 & \\\\\nL16 & 50\\% & $+10$ & 18.4 & 11.0 & 0.123 & \\\\\nL16 & 50\\% & $+20$ & 22.8 & 24.3 & 0.886 & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B ($n_{\\text{test}} = 131$)}} \\\\\nL14 & 39\\% & best & \\multicolumn{2}{c}{n.s.} & 0.785 & 0 dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Gemma-2-9B-IT ($n_{\\text{test}} = 171$)$^{\\ddagger}$}} \\\\\nL17 & 40\\% & best & \\multicolumn{2}{c}{n.s.} & 0.448 & 0 dir. \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes. $^{\\ddagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}",
    "structuredPatch": [
      {
        "oldStart": 171,
        "oldLines": 7,
        "newStart": 171,
        "newLines": 7,
        "lines": [
          " At extreme magnitude ($\\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.",
          " ",
          " \\paragraph{Causal localization (Llama).}",
          "-In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth) regardless of where detection accuracy peaks (EN$\\to$EN at L28, ZH$\\to$ZH at L13): late layers encode the outcome in a linearly readable form, while mid-layers host the computation that determines it.",
          "+In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth), near but distinct from the EN$\\to$EN probe peak (L15, 47\\%): upper layers (e.g., L28) retain a detectable signal but lack causal influence, while mid-layers host the computation that determines the outcome.",
          " An independent replication with a separately trained probe (seed=123, different train/test split) confirms the L13 causal effect: 2/6 positive-direction $\\alpha$ configurations survive per-layer Bonferroni correction ($k{=}6$, $p < 0.0083$), matching the original 2/6 (Appendix~\\ref{app:seed_replication}).",
          " ",
          " \\paragraph{Cross-model steering.}"
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

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
The fig5 caption edit failed because of the % escaping issue. Let me re-read the exact text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "3ddaba5d-59ae-4280-bf06-c1c7640359f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQyav4J6im5Bft77MgW6n8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 57965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1791
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

_source line 61_

Let me re-read the exact fig5 caption text to fix the failed edit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "187c2e8e-5695-40af-9a74-ba8451adfcdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQyav4J6im5Bft77MgW6n8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 57965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1791
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

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_016JWQwFEC3gFrSDFm4rYKXf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
  "offset": 162,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "ad537665-9a16-4953-be79-8de8104beba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQyav4J6im5Bft77MgW6n8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1791,
      "cache_read_input_tokens": 57965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1791
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

_source line 63 · 2026-05-25T15:53:33.625Z_

<details><summary>↩ Tool result · `toolu_016JWQwFEC3gFrSDFm4rYKXf`</summary>

```text
162	\begin{figure}[t]
163	\centering
164	\includegraphics[width=\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}
165	\caption{Steering flip rates at Llama L13 (41\% depth) across $\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\alpha = +5$ (p$\to$c) and $\alpha = -20$ (c$\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\%, probe peak) and L18 (56\%, MLP peak) remain at control levels (Table~\ref{tab:steering}).}
166	\label{fig:steering_viz}
167	\end{figure}
168	
169	\paragraph{Negative layers and coherence collapse.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c428b985-67e8-4725-bd21-d206a28049ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
      "content": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}\n\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\n\\label{fig:steering_viz}\n\\end{figure}\n\n\\paragraph{Negative layers and coherence collapse.}",
      "numLines": 8,
      "startLine": 162,
      "totalLines": 214
    }
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_01XFDkpEJZrmvC5bjkPaUju5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
  "old_string": "Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}",
  "new_string": "Flip rates at L28 (88\\%) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c3a8bf2f-178d-40ad-9ea1-a26cbb1551df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMJN3yrrUmUSnriiShDv9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 59756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 444
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

_source line 65 · 2026-05-25T15:53:37.071Z_

<details><summary>↩ Tool result · `toolu_01XFDkpEJZrmvC5bjkPaUju5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "d8eb69ed-c9dc-40e2-94cf-ef63bfcfd1d5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/experiments.tex",
    "oldString": "Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}",
    "newString": "Flip rates at L28 (88\\%) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe three instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama}, Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2025qwen3}, and Gemma-2-9B-IT (42 layers, hidden dimension 3584) \\citep{team2024gemma}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test), 966 for Qwen (773 train / 193 test), and 1{,}590 for Gemma (1{,}274 train / 316 test), split 80/20 with stratification.\nThe three models were independently verified, yielding only 3.5\\% three-way question overlap (23 questions); pairwise overlaps range from 7.2\\% (Llama $\\cap$ Gemma) to 24.8\\% (Gemma $\\cap$ Qwen), so the consistent asymmetry pattern across models constitutes largely independent replication.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET (wmt22-comet-da; \\citealt{rei2020comet}) back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train an $L_2$-regularized logistic regression probe ($C = 1.0$, scikit-learn default) on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy rather than AUROC, as our claims depend on cross-model directional comparisons; AUROC results are reported in Appendix~\\ref{app:auroc}.\nAll CIs are computed via bootstrap resampling with paired differences for asymmetry estimation.\nA selectivity control \\citep{hewitt2019designing} with permuted labels on matched-condition data ($N{=}131$--$201$) yields near-chance accuracy (49.2--51.0\\%) across all models, confirming selectivity gaps of 21--40~pp.\nAll experiments used a single GPU; the boundary replication (Appendix~\\ref{app:boundary}) used an NVIDIA RTX PRO 6000.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nAll three models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.6\\% on EN$\\to$EN (peak at layer 15, 47\\% depth) and 72.1\\% on ZH$\\to$ZH.\nQwen reaches 75.0\\% on EN$\\to$EN (peak at layer 24, 67\\% depth) and 72.6\\% on ZH$\\to$ZH.\nGemma attains 76.2\\% on EN$\\to$EN (peak at layer 24, 57\\% depth) and 71.0\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for all three models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across all three architectures and both languages.\n\n%% Figure 2: Layer-wise probe accuracy\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig3_layerwise_probes.pdf}\n\\caption{Layer-wise probe balanced accuracy for Llama-3.1-8B (left), Qwen3-8B (center), and Gemma-2-9B-IT (right). Solid lines: residual stream probes; dashed lines (Llama and Qwen only): multilayer perceptron (MLP) sublayer probes. Stars mark peak layers. In the Llama panel, the vertical annotation at L13 marks the layer where steering produces significant causal influence (Fisher $p < 0.001$), near the EN$\\to$EN probe peak (L15). In the Gemma panel, L17 and L21 are annotated as steering-negative layers.}\n\\label{fig:layer_probe}\n\\end{figure*}\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}); this confirms that conflict representations partially overlap between English and Chinese.\nAll three models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nWe define $\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})$, computed via paired bootstrap.\nFor Llama, $\\Delta_{\\text{asym}} = +7.3$ percentage points (pp) with a 95\\% bootstrap CI of [0.4, 14.0] ($p = 0.038$); for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7]; for Gemma, $\\Delta_{\\text{asym}} = +6.6$ pp with CI [1.9, 11.1] ($p = 0.006$).\nWhile the Qwen CI marginally includes zero, the asymmetry is consistent in direction across all three architectures.\nThe magnitude of this asymmetry is consistent in direction and magnitude with the XNLI non-conflict baseline across all three architectures (\\S\\ref{sec:xnli_baseline}), and the consistent direction across all three models suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-seed balanced accuracy (\\%) at each direction's optimal layer. $\\Delta_{\\text{asym}}$ and 95\\% CIs from paired bootstrap ($n = 2{,}000$ resamples). Bold: best per-task direction.}\n\\label{tab:main_results}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B & Gemma-2-9B \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.6} & \\textbf{75.0} & \\textbf{76.2} \\\\\nZH $\\to$ ZH & 72.1 & 72.6 & 71.0 \\\\\nEN $\\to$ ZH & 59.6 & 67.3 & 62.9 \\\\\nZH $\\to$ EN & 70.6 & 73.2 & 70.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.3 [0.4, 14.0] & +7.2 [$-$0.6, 13.7] & +6.6 [1.9, 11.1] \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 & 95.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 & 89.0 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 & 89.4 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} & \\textbf{97.5} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] & +7.8 [5.7, 10.0] \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize Note: $\\Delta_{\\text{asym}}$ is the mean of paired bootstrap differences, not the arithmetic difference of the reported single-seed accuracies.\n\\end{flushleft}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nAll three models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH; Gemma 95.6\\% EN, 89.0\\% ZH). These accuracies confirm that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7]; Gemma $\\Delta_{\\text{asym}} = +7.8$ pp, CI [5.7, 10.0] ($p < 0.001$).\nAll three XNLI CIs exclude zero and overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nFormal Two One-Sided Tests (TOST) equivalence tests ($\\pm$2~pp margin) were non-significant (all $p > 0.36$); post-hoc power analysis shows only 1.4\\% power at this margin given standard error (SE) $\\approx 4.2$~pp, with 80\\% power requiring a $\\pm$12.5~pp margin.\nBayesian equivalence testing yields a Bayes factor $\\text{BF}_{01} \\approx 1.5$ (half-normal prior, scale $= 5$~pp), providing directionally consistent but modest evidence for equivalence.\nCombined with the consistent direction across all six model$\\times$task combinations (binomial $p = 0.016$) and magnitudes clustering in [$+$6.0, $+$7.8~pp], these analyses support the ``consistency'' characterization: the non-significance reflects insufficient power, not meaningful differences.\n\n%% Figure 3: Asymmetry forest plot\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_asymmetry_forest.pdf}\n\\caption{Transfer asymmetry ($\\Delta_{\\text{asym}}$) with bootstrap 95\\% CIs ($n = 2{,}000$) for conflict and XNLI tasks across all three architectures (six data points). Conflict and XNLI CIs overlap substantially within each model, indicating that the ZH$\\to$EN advantage is a general cross-lingual property rather than conflict-specific. Grey dashed lines: $\\pm$2~pp exploratory equivalence margin (TOST power $= 1.4$\\%; see \\S\\ref{sec:xnli_baseline}).}\n\\label{fig:asymmetry_forest}\n\\end{figure}\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: lexical overlap between English and Chinese inputs and translation quality.\n\n\\paragraph{Token overlap and EN-DE control.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, already at the floor imposed by distinct writing systems.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$, $r^2 = 0.023$), running counter to the confound hypothesis.\nThe strongest evidence comes from a typological control: we translate the same Llama ConflictQA samples into German using the identical Qwen3-8B pipeline, where per-sample Jaccard similarity (14.8\\%) is approximately $4\\times$ higher than EN-ZH (3.8\\%).\nDespite this substantially higher lexical overlap, the EN$\\leftrightarrow$DE transfer asymmetry is near-zero ($\\Delta = +1.2$~pp, n.s.), ruling out shared tokens as a driver of the observed EN-ZH asymmetry (Table~\\ref{tab:confound}).\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles and compare EN$\\to$ZH probe accuracy across strata.\nQwen shows a reversed association ($\\Delta = -5.6$~pp, Fisher $p = 0.695$) and Llama a negligible one ($\\Delta = +1.7$~pp, $p = 0.761$), both inconsistent with translation quality driving probe transfer.\nGemma shows a non-significant trend in the confound direction ($\\Delta = +10.3$~pp, $p = 0.278$), but interpretation is limited by the near-chance baseline accuracy of the EN$\\to$ZH probe at L17 (58.8\\%), placing this analysis in a low-power regime.\nWith a minimum detectable difference of 25.3~pp at 80\\% power ($n \\approx 56$ per tercile), the COMET tercile analysis can neither confirm nor exclude a moderate translation quality effect; it serves as supplementary evidence alongside the token overlap and EN-DE controls.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\nCOMET tercile & Gemma & $\\Delta = +10.3$ pp & 0.278 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_l$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_l$ into the last-token residual stream at a target layer during inference.\nWe sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) following prior steering conventions \\citep{turner2023activation, marks2024geometry} and report results at all tested values.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces bidirectional causal effects (Figure~\\ref{fig:steering_viz}; Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$; 4 p$\\to$c flips), while negative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% ($p < 0.001$; 5 c$\\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$).\nAll-position injection at L13 produces identical results; the causal signal is concentrated at the final token.\nSteering at nearby L16 (50\\% depth, just three layers away) showed no significant effect (all $p > 0.12$), consistent with a narrow causal window.\nUnder a conservative family-wise correction across all 30 tests (3 layers $\\times$ 10 $\\alpha$ values, threshold $p < 0.00167$), L13 remains significant ($\\alpha = +10$, $p = 0.0003$).\nAn independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}\n\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\n\\label{fig:steering_viz}\n\\end{figure}\n\n\\paragraph{Negative layers and coherence collapse.}\nSteering at L28 (88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\nAt extreme magnitude ($\\alpha = +20$), the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse.\n\n\\paragraph{Causal localization (Llama).}\nIn Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth), near but distinct from the EN$\\to$EN probe peak (L15, 47\\%): upper layers (e.g., L28) retain a detectable signal but lack causal influence, while mid-layers host the computation that determines the outcome.\nAn independent replication with a separately trained probe (seed=123, different train/test split) confirms the L13 causal effect: 2/6 positive-direction $\\alpha$ configurations survive per-layer Bonferroni correction ($k{=}6$, $p < 0.0083$), matching the original 2/6 (Appendix~\\ref{app:seed_replication}).\n\n\\paragraph{Cross-model steering.}\nCross-model experiments use the reduced 6-value $\\alpha$ grid ($k{=}6$, per-layer threshold $p < 0.0083$; \\S\\ref{sec:steering_method}).\nQwen steering at L14 (39\\%, $n_{\\text{test}} = 131$; probe accuracy 71.0\\%) produced no significant effect at any $\\alpha$ (best $p = 0.785$) and zero directional flips.\nGemma-2-9B-IT L17 (40\\% depth) provides a stronger test: with 88.9\\% probe accuracy, the highest among all three models (exceeding both Llama 76.1\\% and Qwen 71.0\\%), steering produced no significant change at any $\\alpha$ (best $p = 0.448$) and zero directional flips ($n_{\\text{test}} = 171$), ruling out probe quality as a confound and confirming that the causal influence of probe-weight directions is architecture-dependent.\nAUROC analysis confirms this pattern: Gemma achieves 0.93 AUROC (vs.\\ Llama 0.98, Qwen 0.77; Appendix~\\ref{app:auroc}), yet steering produces zero causal effect.\nAppendix~\\ref{app:steering_config} reports matched-condition results at three layers per model (${\\sim}$36--43\\% depth), all confirming the null.\n\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results. Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Bonferroni-corrected significance threshold $p < 0.005$ ($k = 10$). Significant results in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL16 & 50\\% & $+5$ & 8.8 & 8.1 & 1.000 & \\\\\nL16 & 50\\% & $+10$ & 18.4 & 11.0 & 0.123 & \\\\\nL16 & 50\\% & $+20$ & 22.8 & 24.3 & 0.886 & \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B ($n_{\\text{test}} = 131$)}} \\\\\nL14 & 39\\% & best & \\multicolumn{2}{c}{n.s.} & 0.785 & 0 dir. \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Gemma-2-9B-IT ($n_{\\text{test}} = 171$)$^{\\ddagger}$}} \\\\\nL17 & 40\\% & best & \\multicolumn{2}{c}{n.s.} & 0.448 & 0 dir. \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes. $^{\\ddagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}",
    "structuredPatch": [
      {
        "oldStart": 162,
        "oldLines": 7,
        "newStart": 162,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth,height=3cm,keepaspectratio]{fig5_steering.pdf}",
          "-\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%, probe peak) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}",
          "+\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}",
          " \\label{fig:steering_viz}",
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

### Assistant

_source line 66_

Now fixing Discussion and Conclusion in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "1742e98d-935e-4d3e-af5c-8acfb8e9de80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YjiaPgiWvj8syKR6hXYib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 60200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 268
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

_source line 67_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01QFmPkDEkBWCn7C1cqFHKHf`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "completed",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "completed",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "in_progress",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "in_progress",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "pending",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "pending",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "pending",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "pending",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "pending",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "pending",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "64a3b372-6229-447b-af91-407abbf1d691",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YjiaPgiWvj8syKR6hXYib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 60200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 268
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

_source line 68 · 2026-05-25T15:53:43.678Z_

<details><summary>↩ Tool result · `toolu_01QFmPkDEkBWCn7C1cqFHKHf`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "92c173c5-c4b7-41c4-86b5-f5eb486bb428",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "in_progress",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "pending",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "pending",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "pending",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "pending",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "pending",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "in_progress",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "in_progress",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "pending",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "pending",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "pending",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_01AWT3h4E2N4s1t5GbWVcgbq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex",
  "old_string": "In Llama, causal influence is localized to L13 (41\\% depth; Fisher $p = 0.002$), regardless of detection peak location (EN$\\to$EN at L28, ZH$\\to$ZH at L13), with all late-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).\nAn MLP probe reveals a third dissociation: non-linear conflict features peak at L18 (56\\% depth), between the linear peak (L28) and the causal node (L13).",
  "new_string": "In Llama, causal influence is localized to L13 (41\\% depth; Fisher $p < 0.001$), near but distinct from the linear probe peak (EN$\\to$EN at L15, 47\\% depth), with upper-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).\nAn MLP probe reveals a complementary pattern: non-linear conflict features peak at L18 (56\\% depth), above both the linear peak (L15) and the causal node (L13)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "23dea7d3-316d-4ecc-8d5d-3ffa1662851a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGmVFKCju96WSAmLxztvvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 598,
      "cache_read_input_tokens": 60468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 598
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

_source line 70 · 2026-05-25T15:53:52.067Z_

<details><summary>↩ Tool result · `toolu_01AWT3h4E2N4s1t5GbWVcgbq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "efa50471-d3b8-407f-85d8-0047d34ff346",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/discussion.tex",
    "oldString": "In Llama, causal influence is localized to L13 (41\\% depth; Fisher $p = 0.002$), regardless of detection peak location (EN$\\to$EN at L28, ZH$\\to$ZH at L13), with all late-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).\nAn MLP probe reveals a third dissociation: non-linear conflict features peak at L18 (56\\% depth), between the linear peak (L28) and the causal node (L13).",
    "newString": "In Llama, causal influence is localized to L13 (41\\% depth; Fisher $p < 0.001$), near but distinct from the linear probe peak (EN$\\to$EN at L15, 47\\% depth), with upper-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).\nAn MLP probe reveals a complementary pattern: non-linear conflict features peak at L18 (56\\% depth), above both the linear peak (L15) and the causal node (L13).",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Causal influence is localized to L13 regardless of detection peak.}\nIn Llama, causal influence is localized to L13 (41\\% depth; Fisher $p = 0.002$), regardless of detection peak location (EN$\\to$EN at L28, ZH$\\to$ZH at L13), with all late-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).\nAn MLP probe reveals a third dissociation: non-linear conflict features peak at L18 (56\\% depth), between the linear peak (L28) and the causal node (L13).\nL13 coincides with cross-lingual alignment sites \\citep{muller2021first, wendler2024llamas}, suggesting mid-layers serve a dual role in alignment and conflict resolution.\nSteering failed in Qwen (L14, $n = 131$, $p = 0.785$) and Gemma (L17, $n = 171$, $p = 0.448$) with zero directional flips.\nThe dissociation evidence is strongest for Gemma, where high probe accuracy (88.9\\%) and AUROC (0.93) coexist with zero significant steering effects across all tested layers, ruling out probe quality as a confound.\nFor Qwen, the weaker probe performance (71.4\\%, AUROC 0.77) makes the null steering result more ambiguous: the probe direction may be too noisy for effective intervention, so the failure cannot be attributed to a true detection--decision dissociation with the same confidence.\n\n\\paragraph{Why does steering fail in Qwen and Gemma?}\nThree hypotheses merit consideration, each with preliminary support from our analyses: (1)~non-linear causal interactions \\citep{elhage2022toy}---MLP probes gain $+9.2$~pp over linear probes on Llama conflict EN$\\to$ZH but $-0.5$~pp on XNLI, indicating conflict-specific non-linear encoding; (2)~superposition \\citep{templeton2024scaling}---conflict and XNLI probe weight vectors are near-orthogonal (cosine similarity 0.02--0.05), yet cross-task language identity transfer is near-perfect (87--100\\%), a hallmark of superposition; (3)~architectural differences (e.g., Gemma's sandwich normalization)---Qwen and Gemma show mid-layer cross-task transfer dips (L14--L24) absent in Llama, and L13 falls in Llama's dip-free region.\nDefinitive validation requires activation patching \\citep{meng2022locating}.\n\n\\paragraph{Conflict signals and relation to prior work.}\nThe ZH$\\to$EN transfer advantage ($+7.3$, $+7.2$, $+6.6$~pp) matches the XNLI baseline ($+6.0$, $+6.7$, $+7.8$~pp), indicating that this asymmetry piggybacks on general cross-lingual alignment \\citep{zhao2026when, kargaran2024mexa, wendler2024llamas}.\nRegarding the detection--action gap, \\citet{basu2026interpretability} reported steering failure despite 98.2\\% AUROC; our L13 succeeds with a weaker signal because we steer at mid-layer rather than probe-peak, while our three-model design isolates architecture.\n\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 8,
        "newStart": 2,
        "newLines": 8,
        "lines": [
          " \\label{sec:discussion}",
          " ",
          " \\paragraph{Causal influence is localized to L13 regardless of detection peak.}",
          "-In Llama, causal influence is localized to L13 (41\\% depth; Fisher $p = 0.002$), regardless of detection peak location (EN$\\to$EN at L28, ZH$\\to$ZH at L13), with all late-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).",
          "-An MLP probe reveals a third dissociation: non-linear conflict features peak at L18 (56\\% depth), between the linear peak (L28) and the causal node (L13).",
          "+In Llama, causal influence is localized to L13 (41\\% depth; Fisher $p < 0.001$), near but distinct from the linear probe peak (EN$\\to$EN at L15, 47\\% depth), with upper-layer interventions producing no significant change ($p > 0.3$; Figure~\\ref{fig:dissociation}).",
          "+An MLP probe reveals a complementary pattern: non-linear conflict features peak at L18 (56\\% depth), above both the linear peak (L15) and the causal node (L13).",
          " L13 coincides with cross-lingual alignment sites \\citep{muller2021first, wendler2024llamas}, suggesting mid-layers serve a dual role in alignment and conflict resolution.",
          " Steering failed in Qwen (L14, $n = 131$, $p = 0.785$) and Gemma (L17, $n = 171$, $p = 0.448$) with zero directional flips.",
          " The dissociation evidence is strongest for Gemma, where high probe accuracy (88.9\\%) and AUROC (0.93) coexist with zero significant steering effects across all tested layers, ruling out probe quality as a confound."
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

_source line 71_

<details open><summary>🔧 Tool call — Edit · `toolu_01B6ZPh8wWqJQjb65iUup7hY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex",
  "old_string": "In Llama, a three-way dissociation---linear peak (L28), MLP peak (L18), causal node (L13; $p = 0.002$)---reveals that detection and causation occupy distinct layers; steering fails in Qwen and Gemma despite 88.9\\% accuracy, confirming detection alone is insufficient for mechanistic claims.",
  "new_string": "In Llama, probe peak (L15), MLP peak (L18), and causal node (L13; $p < 0.001$) cluster in mid-layers; the primary evidence that detection $\\neq$ decision comes from the cross-model contrast---all three architectures detect conflict signals, yet only Llama yields significant steering effects (Qwen and Gemma fail despite up to 88.9\\% probe accuracy), confirming detection alone is insufficient for mechanistic claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "f6cfad38-ea01-43ff-89c2-631190ec6fdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGmVFKCju96WSAmLxztvvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 598,
      "cache_read_input_tokens": 60468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 598
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

_source line 72 · 2026-05-25T15:53:56.099Z_

<details><summary>↩ Tool result · `toolu_01B6ZPh8wWqJQjb65iUup7hY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "05d5cc3a-be21-4bc4-8635-832d743dc525",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/conclusion.tex",
    "oldString": "In Llama, a three-way dissociation---linear peak (L28), MLP peak (L18), causal node (L13; $p = 0.002$)---reveals that detection and causation occupy distinct layers; steering fails in Qwen and Gemma despite 88.9\\% accuracy, confirming detection alone is insufficient for mechanistic claims.",
    "newString": "In Llama, probe peak (L15), MLP peak (L18), and causal node (L13; $p < 0.001$) cluster in mid-layers; the primary evidence that detection $\\neq$ decision comes from the cross-model contrast---all three architectures detect conflict signals, yet only Llama yields significant steering effects (Qwen and Gemma fail despite up to 88.9\\% probe accuracy), confirming detection alone is insufficient for mechanistic claims.",
    "originalFile": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that knowledge conflict signals in multilingual LLMs are linearly detectable across English and Chinese ($p < 0.001$, three architectures), with the ZH$\\to$EN transfer advantage (${\\sim}$7~pp) matching the XNLI baseline, indicating general cross-lingual alignment rather than conflict-specific encoding.\nIn Llama, a three-way dissociation---linear peak (L28), MLP peak (L18), causal node (L13; $p = 0.002$)---reveals that detection and causation occupy distinct layers; steering fails in Qwen and Gemma despite 88.9\\% accuracy, confirming detection alone is insufficient for mechanistic claims.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 4,
        "newStart": 2,
        "newLines": 4,
        "lines": [
          " \\label{sec:conclusion}",
          " ",
          " We showed that knowledge conflict signals in multilingual LLMs are linearly detectable across English and Chinese ($p < 0.001$, three architectures), with the ZH$\\to$EN transfer advantage (${\\sim}$7~pp) matching the XNLI baseline, indicating general cross-lingual alignment rather than conflict-specific encoding.",
          "-In Llama, a three-way dissociation---linear peak (L28), MLP peak (L18), causal node (L13; $p = 0.002$)---reveals that detection and causation occupy distinct layers; steering fails in Qwen and Gemma despite 88.9\\% accuracy, confirming detection alone is insufficient for mechanistic claims.",
          "+In Llama, probe peak (L15), MLP peak (L18), and causal node (L13; $p < 0.001$) cluster in mid-layers; the primary evidence that detection $\\neq$ decision comes from the cross-model contrast---all three architectures detect conflict signals, yet only Llama yields significant steering effects (Qwen and Gemma fail despite up to 88.9\\% probe accuracy), confirming detection alone is insufficient for mechanistic claims."
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

_source line 73_

Now fixing the three appendix issues in main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c1490a7a-36ba-45c1-86b9-c04df2aac00d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPMb11yJiwiozMNeawJEnx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 856,
      "cache_read_input_tokens": 61066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 856
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

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01EdjCskSusytFpLLWQA3kyd`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "completed",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "completed",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "completed",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "in_progress",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "in_progress",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "in_progress",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "pending",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "pending",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "pending",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "be4b4738-75be-4742-85c3-6d8cbcb20bc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPMb11yJiwiozMNeawJEnx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 856,
      "cache_read_input_tokens": 61066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 856
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

_source line 75 · 2026-05-25T15:54:02.673Z_

<details><summary>↩ Tool result · `toolu_01EdjCskSusytFpLLWQA3kyd`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "a524bbeb-3226-4ff8-a610-ab14b2b454de",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "in_progress",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "in_progress",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "pending",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "pending",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "pending",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "in_progress",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "in_progress",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "in_progress",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_01SubwuuunKQDpGWj3Ts8M2S`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "old_string": "\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L28, 88\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) occupy distinct layers, revealing a three-way dissociation. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}",
  "new_string": "\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L15, 47\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) cluster in mid-layers; upper layers (e.g., L28) retain detectable signal but lack causal influence. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "ea92b3ff-e990-491a-b87d-f6a9c771f70f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ts8qrrhMxDWSSA5HsKxdcv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 61922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 603
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

_source line 77 · 2026-05-25T15:54:09.138Z_

<details><summary>↩ Tool result · `toolu_01SubwuuunKQDpGWj3Ts8M2S`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "e7aa073e-1d66-4c16-980d-c8109c1c4108",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "oldString": "\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L28, 88\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) occupy distinct layers, revealing a three-way dissociation. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}",
    "newString": "\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L15, 47\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) cluster in mid-layers; upper layers (e.g., L28) retain detectable signal but lack causal influence. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\n\\title{English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n\n\\section{Fine-Grained Causal Boundary Analysis}\n\\label{app:boundary}\n\nTable~\\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).\n\n\\begin{table}[!t]\n\\centering\n\\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\\ Sig.\\ $\\alpha$s: number of $\\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}\n\\label{tab:boundary}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\nLayer & Depth & Probe Acc & Best $\\alpha$ & Best Fisher $p$ & Bonf.\\ Sig.\\ $\\alpha$s & Result \\\\\n\\midrule\nL12 & 38\\% & 91.75\\% & $+20$ & 0.085 & 0/6 & --- \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{90.00\\%} & $\\mathbf{+10}$ & $\\mathbf{<0.001}$ & \\textbf{2/6} & $\\checkmark\\checkmark$ \\\\\nL14 & 44\\% & 91.75\\% & $+10$ & 0.002 & 1/6 & $\\checkmark$ \\\\\nL16 & 50\\% & 91.50\\% & $+10$ & 0.005 & 1/6 & $\\checkmark$ \\\\\nL18 & 56\\% & 90.75\\% & $+5$ & 0.010 & 0/6 & --- \\\\\nL28 & 88\\% & 85.25\\% & $+10$ & 0.284 & 0/6 & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Seed Replication of L13 Steering}\n\\label{app:seed_replication}\n\nTo verify that the L13 causal effect is not an artifact of a specific train/test split, we repeated the Llama L13 steering experiment with an independently trained probe (seed=123, different train/test split).\nThe causal effect replicates in the positive direction: $\\alpha = +5$ ($p = 0.003$), $\\alpha = +10$ ($p = 0.0003$), with 2 of 6 configurations surviving Bonferroni correction (matching the original 2/6).\nThe consistent positive-direction effect across independent probe training confirms that L13 causal localization is not an artifact of a specific train/test split.\n\n\\section{Detection--Decision Dissociation}\n\\label{app:dissociation}\n\n\\begin{figure}[!t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig6_dissociation.pdf}\n\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L28, 88\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) occupy distinct layers, revealing a three-way dissociation. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}\n\\label{fig:dissociation}\n\\end{figure}\n\n\\section{AUROC Analysis}\n\\label{app:auroc}\n\nTable~\\ref{tab:auroc} reports AUROC for conflict probes on matched-condition replication data ($N = 131$--$201$), confirming strong continuous discriminative capacity across models.\nGemma's 0.93 EN$\\to$EN AUROC (the highest among all models for this metric), paired with zero directional flips under steering, provides the strongest evidence that detection and causal influence are dissociable.\n\n\\begin{table}[!t]\n\\centering\n\\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}\n\\label{tab:auroc}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Direction & AUROC & Bal.\\ Acc (\\%) \\\\\n\\midrule\nLlama-3.1-8B & EN$\\to$EN & 0.981 & 92.7 \\\\\n\\midrule\nGemma-2-9B-IT & EN$\\to$EN & 0.931 & 88.1 \\\\\nGemma-2-9B-IT & ZH$\\to$ZH & 0.900 & 85.7 \\\\\nGemma-2-9B-IT & EN$\\to$ZH & 0.852 & 75.1 \\\\\nGemma-2-9B-IT & ZH$\\to$EN & 0.921 & 77.8 \\\\\n\\midrule\nQwen3-8B & EN$\\to$EN & 0.771 & 71.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Matched-Condition Steering Results}\n\\label{app:steering_config}\n\nTable~\\ref{tab:steering_config} reports steering results under matched conditions: all three architectures are tested at comparable relative depths (${\\sim}$36--43\\%) using the same probe training methodology and six $\\alpha$ values in $[-20, +20]$.\nDespite the highest probe accuracy among the three models (88--89\\%), Gemma produces zero directional flips, ruling out probe quality as a confound for the Llama-specific positive result.\nThe full Llama causal gradient ($N = 201$) is in Appendix~\\ref{app:boundary}.\n\n\\begin{table}[!t]\n\\centering\n\\caption{Matched-condition steering results. Probe: EN$\\to$EN balanced accuracy at the target layer. Best $p$: minimum Fisher exact $p$-value across six tested $\\alpha$ values. Bonf.: $\\alpha$ values surviving Bonferroni correction out of 6. Flips: total directional transitions (p$\\to$c $+$ c$\\to$p).$^{\\dagger}$}\n\\label{tab:steering_config}\n\\small\n\\begin{tabular}{lcrccc}\n\\toprule\nLayer & Depth & Probe (\\%) & Best $p$ & Bonf. & Flips \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{76.1} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Qwen3-8B ($N = 131$; 36 layers)}} \\\\\nL13 & 36\\% & 71.8 & 0.168 & 0/6 & 0 \\\\\nL14 & 39\\% & 71.0 & 0.785 & 0/6 & 0 \\\\\nL15 & 42\\% & 72.9 & 0.617 & 0/6 & 0 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Gemma-2-9B-IT ($N = 171$; 42 layers)$^{\\dagger}$}} \\\\\nL16 & 38\\% & 88.0 & 0.067 & 0/6 & 0 \\\\\nL17 & 40\\% & 88.9 & 0.448 & 0/6 & 0 \\\\\nL18 & 43\\% & 89.5 & 0.219 & 0/6 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 96,
        "oldLines": 7,
        "newStart": 96,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[!t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{fig6_dissociation.pdf}",
          "-\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L28, 88\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) occupy distinct layers, revealing a three-way dissociation. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}",
          "+\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L15, 47\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) cluster in mid-layers; upper layers (e.g., L28) retain detectable signal but lack causal influence. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}",
          " \\label{fig:dissociation}",
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

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_01K8u23n4nB3FZiJU2dSpZBB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "old_string": "\\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}",
  "new_string": "\\caption{AUROC and balanced accuracy for conflict probes (matched-condition data, best layer per model).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "cad7adbd-ad0f-4457-9c10-ead554eb48b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ts8qrrhMxDWSSA5HsKxdcv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 61922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 603
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

_source line 79 · 2026-05-25T15:54:11.535Z_

<details><summary>↩ Tool result · `toolu_01K8u23n4nB3FZiJU2dSpZBB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "e85492dd-e6b8-4605-9c62-a73482c0f24d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "oldString": "\\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}",
    "newString": "\\caption{AUROC and balanced accuracy for conflict probes (matched-condition data, best layer per model).}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\n\\title{English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n\n\\section{Fine-Grained Causal Boundary Analysis}\n\\label{app:boundary}\n\nTable~\\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).\n\n\\begin{table}[!t]\n\\centering\n\\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\\ Sig.\\ $\\alpha$s: number of $\\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}\n\\label{tab:boundary}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\nLayer & Depth & Probe Acc & Best $\\alpha$ & Best Fisher $p$ & Bonf.\\ Sig.\\ $\\alpha$s & Result \\\\\n\\midrule\nL12 & 38\\% & 91.75\\% & $+20$ & 0.085 & 0/6 & --- \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{90.00\\%} & $\\mathbf{+10}$ & $\\mathbf{<0.001}$ & \\textbf{2/6} & $\\checkmark\\checkmark$ \\\\\nL14 & 44\\% & 91.75\\% & $+10$ & 0.002 & 1/6 & $\\checkmark$ \\\\\nL16 & 50\\% & 91.50\\% & $+10$ & 0.005 & 1/6 & $\\checkmark$ \\\\\nL18 & 56\\% & 90.75\\% & $+5$ & 0.010 & 0/6 & --- \\\\\nL28 & 88\\% & 85.25\\% & $+10$ & 0.284 & 0/6 & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Seed Replication of L13 Steering}\n\\label{app:seed_replication}\n\nTo verify that the L13 causal effect is not an artifact of a specific train/test split, we repeated the Llama L13 steering experiment with an independently trained probe (seed=123, different train/test split).\nThe causal effect replicates in the positive direction: $\\alpha = +5$ ($p = 0.003$), $\\alpha = +10$ ($p = 0.0003$), with 2 of 6 configurations surviving Bonferroni correction (matching the original 2/6).\nThe consistent positive-direction effect across independent probe training confirms that L13 causal localization is not an artifact of a specific train/test split.\n\n\\section{Detection--Decision Dissociation}\n\\label{app:dissociation}\n\n\\begin{figure}[!t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig6_dissociation.pdf}\n\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L15, 47\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) cluster in mid-layers; upper layers (e.g., L28) retain detectable signal but lack causal influence. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}\n\\label{fig:dissociation}\n\\end{figure}\n\n\\section{AUROC Analysis}\n\\label{app:auroc}\n\nTable~\\ref{tab:auroc} reports AUROC for conflict probes on matched-condition replication data ($N = 131$--$201$), confirming strong continuous discriminative capacity across models.\nGemma's 0.93 EN$\\to$EN AUROC (the highest among all models for this metric), paired with zero directional flips under steering, provides the strongest evidence that detection and causal influence are dissociable.\n\n\\begin{table}[!t]\n\\centering\n\\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}\n\\label{tab:auroc}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Direction & AUROC & Bal.\\ Acc (\\%) \\\\\n\\midrule\nLlama-3.1-8B & EN$\\to$EN & 0.981 & 92.7 \\\\\n\\midrule\nGemma-2-9B-IT & EN$\\to$EN & 0.931 & 88.1 \\\\\nGemma-2-9B-IT & ZH$\\to$ZH & 0.900 & 85.7 \\\\\nGemma-2-9B-IT & EN$\\to$ZH & 0.852 & 75.1 \\\\\nGemma-2-9B-IT & ZH$\\to$EN & 0.921 & 77.8 \\\\\n\\midrule\nQwen3-8B & EN$\\to$EN & 0.771 & 71.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Matched-Condition Steering Results}\n\\label{app:steering_config}\n\nTable~\\ref{tab:steering_config} reports steering results under matched conditions: all three architectures are tested at comparable relative depths (${\\sim}$36--43\\%) using the same probe training methodology and six $\\alpha$ values in $[-20, +20]$.\nDespite the highest probe accuracy among the three models (88--89\\%), Gemma produces zero directional flips, ruling out probe quality as a confound for the Llama-specific positive result.\nThe full Llama causal gradient ($N = 201$) is in Appendix~\\ref{app:boundary}.\n\n\\begin{table}[!t]\n\\centering\n\\caption{Matched-condition steering results. Probe: EN$\\to$EN balanced accuracy at the target layer. Best $p$: minimum Fisher exact $p$-value across six tested $\\alpha$ values. Bonf.: $\\alpha$ values surviving Bonferroni correction out of 6. Flips: total directional transitions (p$\\to$c $+$ c$\\to$p).$^{\\dagger}$}\n\\label{tab:steering_config}\n\\small\n\\begin{tabular}{lcrccc}\n\\toprule\nLayer & Depth & Probe (\\%) & Best $p$ & Bonf. & Flips \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{76.1} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Qwen3-8B ($N = 131$; 36 layers)}} \\\\\nL13 & 36\\% & 71.8 & 0.168 & 0/6 & 0 \\\\\nL14 & 39\\% & 71.0 & 0.785 & 0/6 & 0 \\\\\nL15 & 42\\% & 72.9 & 0.617 & 0/6 & 0 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Gemma-2-9B-IT ($N = 171$; 42 layers)$^{\\dagger}$}} \\\\\nL16 & 38\\% & 88.0 & 0.067 & 0/6 & 0 \\\\\nL17 & 40\\% & 88.9 & 0.448 & 0/6 & 0 \\\\\nL18 & 43\\% & 89.5 & 0.219 & 0/6 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 108,
        "oldLines": 7,
        "newStart": 108,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[!t]",
          " \\centering",
          "-\\caption{AUROC and balanced accuracy at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data).}",
          "+\\caption{AUROC and balanced accuracy for conflict probes (matched-condition data, best layer per model).}",
          " \\label{tab:auroc}",
          " \\small",
          " \\begin{tabular}{llcc}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01VoaGMmi619XP3Xip8Ym4zx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
  "old_string": "\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{76.1} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\",
  "new_string": "\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 201$; 32 layers)}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{90.0} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "668aeaae-7d51-4e8f-b45b-e0dece331b26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ts8qrrhMxDWSSA5HsKxdcv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 61922,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 603
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

_source line 81 · 2026-05-25T15:54:15.266Z_

<details><summary>↩ Tool result · `toolu_01VoaGMmi619XP3Xip8Ym4zx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "65c9c1c7-cafb-4bb1-a262-399d7a3005bf",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
    "oldString": "\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{76.1} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\",
    "newString": "\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 201$; 32 layers)}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{90.0} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\n\\title{English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting \\LaTeX{}.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n\n\\section{Fine-Grained Causal Boundary Analysis}\n\\label{app:boundary}\n\nTable~\\ref{tab:boundary} reports steering results across the full layer gradient from an independent replication ($N = 201$, Llama-3.1-8B-Instruct, RTX PRO 6000).\n\n\\begin{table}[!t]\n\\centering\n\\caption{Causal boundary steering results (independently sampled, $N = 201$, Llama-3.1-8B-Instruct). Bonf.\\ Sig.\\ $\\alpha$s: number of $\\alpha$ values reaching significance after Bonferroni correction out of 6 tested.}\n\\label{tab:boundary}\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\nLayer & Depth & Probe Acc & Best $\\alpha$ & Best Fisher $p$ & Bonf.\\ Sig.\\ $\\alpha$s & Result \\\\\n\\midrule\nL12 & 38\\% & 91.75\\% & $+20$ & 0.085 & 0/6 & --- \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{90.00\\%} & $\\mathbf{+10}$ & $\\mathbf{<0.001}$ & \\textbf{2/6} & $\\checkmark\\checkmark$ \\\\\nL14 & 44\\% & 91.75\\% & $+10$ & 0.002 & 1/6 & $\\checkmark$ \\\\\nL16 & 50\\% & 91.50\\% & $+10$ & 0.005 & 1/6 & $\\checkmark$ \\\\\nL18 & 56\\% & 90.75\\% & $+5$ & 0.010 & 0/6 & --- \\\\\nL28 & 88\\% & 85.25\\% & $+10$ & 0.284 & 0/6 & --- \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Seed Replication of L13 Steering}\n\\label{app:seed_replication}\n\nTo verify that the L13 causal effect is not an artifact of a specific train/test split, we repeated the Llama L13 steering experiment with an independently trained probe (seed=123, different train/test split).\nThe causal effect replicates in the positive direction: $\\alpha = +5$ ($p = 0.003$), $\\alpha = +10$ ($p = 0.0003$), with 2 of 6 configurations surviving Bonferroni correction (matching the original 2/6).\nThe consistent positive-direction effect across independent probe training confirms that L13 causal localization is not an artifact of a specific train/test split.\n\n\\section{Detection--Decision Dissociation}\n\\label{app:dissociation}\n\n\\begin{figure}[!t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig6_dissociation.pdf}\n\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L15, 47\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) cluster in mid-layers; upper layers (e.g., L28) retain detectable signal but lack causal influence. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}\n\\label{fig:dissociation}\n\\end{figure}\n\n\\section{AUROC Analysis}\n\\label{app:auroc}\n\nTable~\\ref{tab:auroc} reports AUROC for conflict probes on matched-condition replication data ($N = 131$--$201$), confirming strong continuous discriminative capacity across models.\nGemma's 0.93 EN$\\to$EN AUROC (the highest among all models for this metric), paired with zero directional flips under steering, provides the strongest evidence that detection and causal influence are dissociable.\n\n\\begin{table}[!t]\n\\centering\n\\caption{AUROC and balanced accuracy for conflict probes (matched-condition data, best layer per model).}\n\\label{tab:auroc}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Direction & AUROC & Bal.\\ Acc (\\%) \\\\\n\\midrule\nLlama-3.1-8B & EN$\\to$EN & 0.981 & 92.7 \\\\\n\\midrule\nGemma-2-9B-IT & EN$\\to$EN & 0.931 & 88.1 \\\\\nGemma-2-9B-IT & ZH$\\to$ZH & 0.900 & 85.7 \\\\\nGemma-2-9B-IT & EN$\\to$ZH & 0.852 & 75.1 \\\\\nGemma-2-9B-IT & ZH$\\to$EN & 0.921 & 77.8 \\\\\n\\midrule\nQwen3-8B & EN$\\to$EN & 0.771 & 71.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Matched-Condition Steering Results}\n\\label{app:steering_config}\n\nTable~\\ref{tab:steering_config} reports steering results under matched conditions: all three architectures are tested at comparable relative depths (${\\sim}$36--43\\%) using the same probe training methodology and six $\\alpha$ values in $[-20, +20]$.\nDespite the highest probe accuracy among the three models (88--89\\%), Gemma produces zero directional flips, ruling out probe quality as a confound for the Llama-specific positive result.\nThe full Llama causal gradient ($N = 201$) is in Appendix~\\ref{app:boundary}.\n\n\\begin{table}[!t]\n\\centering\n\\caption{Matched-condition steering results. Probe: EN$\\to$EN balanced accuracy at the target layer. Best $p$: minimum Fisher exact $p$-value across six tested $\\alpha$ values. Bonf.: $\\alpha$ values surviving Bonferroni correction out of 6. Flips: total directional transitions (p$\\to$c $+$ c$\\to$p).$^{\\dagger}$}\n\\label{tab:steering_config}\n\\small\n\\begin{tabular}{lcrccc}\n\\toprule\nLayer & Depth & Probe (\\%) & Best $p$ & Bonf. & Flips \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\\\\n\\textbf{L13} & \\textbf{41\\%} & \\textbf{76.1} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Qwen3-8B ($N = 131$; 36 layers)}} \\\\\nL13 & 36\\% & 71.8 & 0.168 & 0/6 & 0 \\\\\nL14 & 39\\% & 71.0 & 0.785 & 0/6 & 0 \\\\\nL15 & 42\\% & 72.9 & 0.617 & 0/6 & 0 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Gemma-2-9B-IT ($N = 171$; 42 layers)$^{\\dagger}$}} \\\\\nL16 & 38\\% & 88.0 & 0.067 & 0/6 & 0 \\\\\nL17 & 40\\% & 88.9 & 0.448 & 0/6 & 0 \\\\\nL18 & 43\\% & 89.5 & 0.219 & 0/6 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ Gemma: after correcting a label assignment error.\n\\end{flushleft}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 143,
        "oldLines": 8,
        "newStart": 143,
        "newLines": 8,
        "lines": [
          " \\toprule",
          " Layer & Depth & Probe (\\%) & Best $p$ & Bonf. & Flips \\\\",
          " \\midrule",
          "-\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 136$; 32 layers)}} \\\\",
          "-\\textbf{L13} & \\textbf{41\\%} & \\textbf{76.1} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\",
          "+\\multicolumn{6}{l}{\\textit{Llama-3.1-8B-Instruct ($N = 201$; 32 layers)}} \\\\",
          "+\\textbf{L13} & \\textbf{41\\%} & \\textbf{90.0} & $\\mathbf{<0.001}$ & \\textbf{2/6} & \\textbf{9} \\\\",
          " \\midrule",
          " \\multicolumn{6}{l}{\\textit{Qwen3-8B ($N = 131$; 36 layers)}} \\\\",
          " L13 & 36\\% & 71.8 & 0.168 & 0/6 & 0 \\\\"
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

All targeted edits complete. Now running the full-text grep verification to catch any remaining problematic references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "9fd83fac-3928-4c7d-ab66-0cd2285d9af4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYgVdBaED2QRsEWpyFEbJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 62525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1088
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

_source line 83_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01TeUDHrEhnoSepqiUPvwtYq`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "completed",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "completed",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "completed",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "completed",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "completed",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "completed",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "in_progress",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "pending",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "pending",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "77f310a9-ed1c-4b6e-aa2c-4bfb50902282",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KYgVdBaED2QRsEWpyFEbJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 62525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1088
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

_source line 84 · 2026-05-25T15:54:21.959Z_

<details><summary>↩ Tool result · `toolu_01TeUDHrEhnoSepqiUPvwtYq`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "9c75d3ad-46a4-4ac1-a16d-4d8d2d670c68",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "in_progress",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "in_progress",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "in_progress",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "pending",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "completed",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "completed",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "completed",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "in_progress",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Grep · `toolu_01KiFJ9hTYyMtrZ9wXWwLfHv`</summary>

```json
{
  "pattern": "L28",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper",
  "glob": "*.tex",
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c815a239-7a32-4c33-bbce-b76e07f3ca6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTop34Hom3mMpU6aG7E6nE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 63613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 609
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

_source line 86 · 2026-05-25T15:54:25.061Z_

<details><summary>↩ Tool result · `toolu_01KiFJ9hTYyMtrZ9wXWwLfHv`</summary>

```text
docs/paper/experiments.tex:160:An independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\ref{tab:boundary}).
docs/paper/experiments.tex:165:\caption{Steering flip rates at Llama L13 (41\% depth) across $\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\alpha = +5$ (p$\to$c) and $\alpha = -20$ (c$\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\%) and L18 (56\%, MLP peak) remain at control levels (Table~\ref{tab:steering}).}
docs/paper/experiments.tex:170:Steering at L28 (88\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\%) is similarly negative ($p > 0.44$).
docs/paper/experiments.tex:174:In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\% depth), near but distinct from the EN$\to$EN probe peak (L15, 47\%): upper layers (e.g., L28) retain a detectable signal but lack causal influence, while mid-layers host the computation that determines the outcome.
docs/paper/experiments.tex:200:L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
docs/paper/experiments.tex:201:L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 1.000 & \\
docs/paper/main.tex:80:L28 & 88\% & 85.25\% & $+10$ & 0.284 & 0/6 & --- \\
docs/paper/main.tex:99:\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L15, 47\% depth), MLP probe peak (L18, 56\%), and causal steering node (L13, 41\%) cluster in mid-layers; upper layers (e.g., L28) retain detectable signal but lack causal influence. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}
docs/paper/method.tex:64:For last-token injection, we sweep $\alpha \in \{\pm 20, \pm 10, \pm 5, \pm 2, \pm 1\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\alpha \in \{\pm 20, \pm 10, \pm 5\}$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "28b641da-71a5-474f-b2b3-98e7d2a225db",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:160:An independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).\ndocs/paper/experiments.tex:165:\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\ndocs/paper/experiments.tex:170:Steering at L28 (88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\ndocs/paper/experiments.tex:174:In Llama-3.1-8B-Instruct, causal influence is consistently localized to L13 (41\\% depth), near but distinct from the EN$\\to$EN probe peak (L15, 47\\%): upper layers (e.g., L28) retain a detectable signal but lack causal influence, while mid-layers host the computation that determines the outcome.\ndocs/paper/experiments.tex:200:L28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\ndocs/paper/experiments.tex:201:L28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\ndocs/paper/main.tex:80:L28 & 88\\% & 85.25\\% & $+10$ & 0.284 & 0/6 & --- \\\\\ndocs/paper/main.tex:99:\\caption{Detection--decision dissociation across three architectures. For Llama, the linear probe peak (L15, 47\\% depth), MLP probe peak (L18, 56\\%), and causal steering node (L13, 41\\%) cluster in mid-layers; upper layers (e.g., L28) retain detectable signal but lack causal influence. Qwen and Gemma achieve comparable probe accuracy but show no significant causal site under linear steering, illustrating that detectability does not imply causal relevance.}\ndocs/paper/method.tex:64:For last-token injection, we sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5\\}$).",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Grep · `toolu_015QzaSykHKs3ybBQoMWpumG`</summary>

```json
{
  "pattern": "88\\\\\\\\?%",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper",
  "glob": "*.tex",
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "bf0480b9-f74a-4c91-8798-08cbe3531d5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTop34Hom3mMpU6aG7E6nE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 63613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 609
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

_source line 88 · 2026-05-25T15:54:26.127Z_

<details><summary>↩ Tool result · `toolu_015QzaSykHKs3ybBQoMWpumG`</summary>

```text
docs/paper/experiments.tex:165:\caption{Steering flip rates at Llama L13 (41\% depth) across $\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\alpha = +5$ (p$\to$c) and $\alpha = -20$ (c$\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\%) and L18 (56\%, MLP peak) remain at control levels (Table~\ref{tab:steering}).}
docs/paper/experiments.tex:170:Steering at L28 (88\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\%) is similarly negative ($p > 0.44$).
docs/paper/experiments.tex:200:L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
docs/paper/experiments.tex:201:L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 1.000 & \\
docs/paper/main.tex:80:L28 & 88\% & 85.25\% & $+10$ & 0.284 & 0/6 & --- \\
docs/paper/method.tex:64:For last-token injection, we sweep $\alpha \in \{\pm 20, \pm 10, \pm 5, \pm 2, \pm 1\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\alpha \in \{\pm 20, \pm 10, \pm 5\}$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "be5e7415-4143-45b5-bc7a-04db61dcff80",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:165:\\caption{Steering flip rates at Llama L13 (41\\% depth) across $\\alpha$ values. Probe-direction injection (solid) produces significant bidirectional flips at $\\alpha = +5$ (p$\\to$c) and $\\alpha = -20$ (c$\\to$p), both surviving per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$). Random-direction controls of matched magnitude (dashed) show no directional effect. Flip rates at L28 (88\\%) and L18 (56\\%, MLP peak) remain at control levels (Table~\\ref{tab:steering}).}\ndocs/paper/experiments.tex:170:Steering at L28 (88\\% depth) produces no significant effect with either last-token or all-position injection (all $p > 0.3$); L18 (MLP peak, 56\\%) is similarly negative ($p > 0.44$).\ndocs/paper/experiments.tex:200:L28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\ndocs/paper/experiments.tex:201:L28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 1.000 & \\\\\ndocs/paper/main.tex:80:L28 & 88\\% & 85.25\\% & $+10$ & 0.284 & 0/6 & --- \\\\\ndocs/paper/method.tex:64:For last-token injection, we sweep $\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5, \\pm 2, \\pm 1\\}$ ($k = 10$) at three Llama layers (L13, L18, L28) spanning 41--88\\% depth; all-position and cross-model experiments use a reduced 6-value grid ($\\alpha \\in \\{\\pm 20, \\pm 10, \\pm 5\\}$).",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Grep · `toolu_015UtcVJEHqzme1BiQacw4xo`</summary>

```json
{
  "pattern": "p = 0\\.002",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper",
  "glob": "*.tex",
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "23b9a397-3e20-485c-8dc0-0b1511e22282",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTop34Hom3mMpU6aG7E6nE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 63613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 609
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

_source line 90 · 2026-05-25T15:54:27.461Z_

<details><summary>↩ Tool result · `toolu_015UtcVJEHqzme1BiQacw4xo`</summary>

```text
docs/paper/experiments.tex:156:Positive steering ($\alpha = +5$) yields a flip rate of 19.9\% versus 6.6\% for the random control (Fisher $p = 0.002$; 4 p$\to$c flips), while negative steering ($\alpha = -20$) yields 36.0\% versus 17.6\% ($p < 0.001$; 5 c$\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\alpha$ values, threshold $p < 0.005$).
docs/paper/experiments.tex:160:An independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\ref{tab:boundary}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "6b73ed2e-3815-4b13-8f76-5785c834cbb5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:156:Positive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$; 4 p$\\to$c flips), while negative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% ($p < 0.001$; 5 c$\\to$p flips); both survive per-layer Bonferroni correction ($k{=}10$ $\\alpha$ values, threshold $p < 0.005$).\ndocs/paper/experiments.tex:160:An independent replication ($N = 201$, six layers L12--L28) confirmed L13 significance ($p < 0.001$) and localized the causal boundary: effects attenuate from L14 ($p = 0.002$) through L16 ($p = 0.005$) to non-significance at L18 ($p = 0.010$, n.s.\\ after Bonferroni) and L28 ($p = 0.284$; Appendix Table~\\ref{tab:boundary}).",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Grep · `toolu_01XWgK6mj4yKDVEPadEPXowZ`</summary>

```json
{
  "pattern": "late.layer",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "1afb8b96-a6fa-4ea7-9899-453ad6aa373a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTop34Hom3mMpU6aG7E6nE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 63613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 609
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

_source line 92 · 2026-05-25T15:54:28.353Z_

<details><summary>↩ Tool result · `toolu_01XWgK6mj4yKDVEPadEPXowZ`</summary>

```text
docs/paper/related_work.tex:23:Our results identify layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, suggesting conflict resolution occurs upstream of where the outcome becomes linearly readable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "dc2aaec8-f82f-45cd-9d84-a1830a6c139f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:23:Our results identify layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, suggesting conflict resolution occurs upstream of where the outcome becomes linearly readable.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the remaining references:

**L28 references:**
1. experiments.tex:160 - "six layers L12--L28" and "L28 ($p = 0.284$)" → These are factual descriptions of which layers were tested and their results. KEEP.
2. experiments.tex:165 - "Flip rates at L28 (88\%)" → This is about the steering results at L28. Already fixed (removed "probe peak"). KEEP.


3. experiments.tex:170 - "Steering at L28 (88\% depth)" → Already fixed (removed "probe peak"). KEEP.
4. experiments.tex:174 - Already fixed. KEEP.
5. experiments.tex:200-201 - Table data rows. KEEP (actual data).
6. main.tex:80 - Boundary table data row. KEEP.
7. main.tex:99 - Already fixed. KEEP.
8. method.tex:64 - "three Llama layers (L13, L18, L28) spanning 41--88% depth" → Factual description of tested layers. KEEP.

All remaining L28 references are legitimate data points or factual descriptions of the experimental setup.

For the 88% depth references, these are all accurate since they describe L28's actual position in the model. The p = 0.002 values are specific to individual steering conditions—the first is for α=+5 at L13 and the second for L14—so both are correct and should stay. Now checking the late-layer intervention references to see if they need adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "7ea1efdc-163f-4bb8-960c-6a36d4825484",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eymLeLQNfCHfyKBsaEemm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2408,
      "cache_read_input_tokens": 64222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2408
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

_source line 94_

All remaining L28 references are legitimate (data tables, tested layers described factually, not labeled as "probe peak"). The `p = 0.002` on experiments.tex:156 is the specific α=+5 steering p-value (correct), and on line 160 it's L14's value (correct). No further changes needed.

Now compiling and running verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "cf5a9255-1e97-4045-ab3c-9c4fddc6f685",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eymLeLQNfCHfyKBsaEemm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2408,
      "cache_read_input_tokens": 64222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2408
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

_source line 95_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01H8zMUhUaet1kR2r3n2dq3a`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "completed",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "completed",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "completed",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "completed",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "completed",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "completed",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "completed",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "in_progress",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "pending",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "f06667d3-9e51-4644-b045-3079d5a93cad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eymLeLQNfCHfyKBsaEemm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2408,
      "cache_read_input_tokens": 64222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2408
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

_source line 96 · 2026-05-25T15:54:45.506Z_

<details><summary>↩ Tool result · `toolu_01H8zMUhUaet1kR2r3n2dq3a`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "3553aed9-9b0a-4213-a96f-4784ba8af196",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "completed",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "completed",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "completed",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "in_progress",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "completed",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "completed",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "completed",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "completed",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "in_progress",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_0145gdVqJv1tejKJ2B9178nY`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "345b655b-8798-46fa-8e3d-ae35c51561ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SiN8JY9JmQMnJpf1vsqJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1224,
      "cache_read_input_tokens": 66630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1224
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

_source line 98 · 2026-05-25T15:54:49.698Z_

<details><summary>↩ Tool result · `toolu_0145gdVqJv1tejKJ2B9178nY`</summary>

```text
 [][] 
[11 <./fig6_dissociation.pdf>]
Overfull \hbox (4.52687pt too wide) in paragraph at lines 142--160
 [][] 
[12] (./main.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvet
ic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (12 pages, 471769 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "6a9d1c52-0316-40fd-9703-9608a51c1f46",
  "tool_use_result": {
    "stdout": " [][] \n[11 <./fig6_dissociation.pdf>]\nOverfull \\hbox (4.52687pt too wide) in paragraph at lines 142--160\n [][] \n[12] (./main.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvet\nic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (12 pages, 471769 bytes).\nTranscript written on main.log.",
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

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_013ecNDJeQMcPagukADzqFxK`</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "bibtex + two more pdflatex passes",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "d339d5ac-9ead-4568-b1e8-cf7464914fb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MGAEq4tFU9hx2vW8XTfy3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 67854,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1006
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

_source line 100 · 2026-05-25T15:54:55.367Z_

<details><summary>↩ Tool result · `toolu_013ecNDJeQMcPagukADzqFxK`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
ic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (12 pages, 471670 bytes).
Transcript written on main.log.
ic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (12 pages, 471670 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "14df0c48-c3d6-44d4-95ef-85c43606fe04",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\nic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (12 pages, 471670 bytes).\nTranscript written on main.log.\nic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (12 pages, 471670 bytes).\nTranscript written on main.log.",
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

_source line 101_

Compiled successfully (12 pages total). Now checking page count, abstract word count, and running final grep verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "b5a26c54-9260-49aa-a905-fce310f88191",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163er5QirdjLoEXAEqKtbAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 68860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 512
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

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_01K47V5bywPTZFT7Gfh7jqKY`</summary>

```json
{
  "command": "pdfinfo main.pdf | grep Pages",
  "description": "Check page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "35d51228-8c46-4cbb-9643-25a0606a0b4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163er5QirdjLoEXAEqKtbAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 68860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 512
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

_source line 103 · 2026-05-25T15:54:59.409Z_

<details><summary>↩ Tool result · `toolu_01K47V5bywPTZFT7Gfh7jqKY`</summary>

```text
Pages:           12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "baa3d3ca-14e1-44fe-94a4-6fa23ebae24b",
  "tool_use_result": {
    "stdout": "Pages:           12",
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

_source line 104_

<details open><summary>🔧 Tool call — Bash · `toolu_01FPHUXwuPSDbwQagEPy7w9S`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{//g; s/}//g; s/\\\\//g; s/~/ /g; s/\\$[^$]*\\$//g; s/footnote.*//g' | wc -w",
  "description": "Count abstract words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "8afa5827-715c-46aa-8a1f-cb2bb2514e7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163er5QirdjLoEXAEqKtbAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 68860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 512
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

_source line 105 · 2026-05-25T15:55:01.115Z_

<details><summary>↩ Tool result · `toolu_01FPHUXwuPSDbwQagEPy7w9S`</summary>

```text
149
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "8068b134-478b-4463-8342-14856bf2a1ec",
  "tool_use_result": {
    "stdout": "149",
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

_source line 106_

<details open><summary>🔧 Tool call — Bash · `toolu_018YXc8CahYfRa4aGzi7sZS9`</summary>

```json
{
  "command": "grep -c \"^!\" main.log",
  "description": "Count LaTeX errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "dd8fd6e0-60aa-465d-9054-29adf745cb2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163er5QirdjLoEXAEqKtbAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 68860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 512
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

_source line 107 · 2026-05-25T15:55:02.007Z_

<details><summary>↩ Tool result · `toolu_018YXc8CahYfRa4aGzi7sZS9`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "d3663a4d-9699-4011-8bc4-8b706cf5eff5",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 108_

<details><summary>Logged reasoning block</summary>

```text
12 pages total. I need to check: the paper has appendices, so 12 pages total including appendices is fine. The main text should be ≤ 8 pages. Let me check what page the appendices start on. Actually, the EMNLP limit is 8 pages for main text. The user said "确认正文 ≤ 8 页". Let me check how many pages the main text occupies.

Actually, looking at the structure: main.tex has \appendix after the limitations section. The main text includes everything up to and including limitations. I need to check what page the appendix starts on.


I should look at the compilation log to find where the appendix begins.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "2e16d55c-a885-4ab7-98ee-1c996a6f21dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XXzG1rEJa4mJYqWHGGD4u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 69372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
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

_source line 109_

12 pages total (including appendices). Let me verify the main text is ≤ 8 pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c1515fdf-f776-4c6e-876f-8815ffb62d49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XXzG1rEJa4mJYqWHGGD4u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 69372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
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

_source line 110_

<details open><summary>🔧 Tool call — Bash · `toolu_01ENjEGsUUedSLVwVwfidUxF`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\appendix\" main.log 2>/dev/null; grep \"app:ai-assistants\" main.log 2>/dev/null; grep \"\\[8\\]\\|\\[9\\]\" main.log | head -5",
  "description": "Check where appendix starts in PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "31eb0868-0c10-4043-a74b-0e9676ef99ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XXzG1rEJa4mJYqWHGGD4u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 69372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 407
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

_source line 111 · 2026-05-25T15:55:10.458Z_

<details><summary>↩ Tool result · `toolu_01ENjEGsUUedSLVwVwfidUxF`</summary>

```text
 [8]
[9]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "545f94af-7475-4092-b3bb-d21e3ec757a0",
  "tool_use_result": {
    "stdout": " [8]\n[9]",
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

_source line 112_

<details><summary>Logged reasoning block</summary>

```text
The log shows page [8] and [9]. Let me check more carefully where the appendix starts by looking at the log output more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "af952994-b8bb-4da2-81f9-74a0c2e2e743",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3H1CBi7HGGLFy6NXbjxei",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 69779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 349
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

_source line 113_

<details open><summary>🔧 Tool call — Bash · `toolu_01MFbTqx9JYaKpJcAyV5hmKD`</summary>

```json
{
  "command": "grep -E \"^\\[|appendix|Appendix|\\\\\\\\section\" main.log | head -30",
  "description": "Check page boundaries in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "89031966-c6d2-4a35-a063-04a8572e7416",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D3H1CBi7HGGLFy6NXbjxei",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 69779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 349
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

_source line 114 · 2026-05-25T15:55:14.077Z_

<details><summary>↩ Tool result · `toolu_01MFbTqx9JYaKpJcAyV5hmKD`</summary>

```text
grep: main.log: binary file matches
[Loading MPS to PDF converter (version 2006.09.02).]
[3 <./fig2_pipeline.pdf>]) (./experiments.tex [4]
[]\T1/ptm/m/n/10 (+20) Nelson El-hage, Tris-tan Hume, Cather-ine Ols-son,
[9]
[10]
[]\T1/ptm/b/n/10.95 (+20) Code: \T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment
[11 <./fig6_dissociation.pdf>]
[12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "bc5eec1c-4d55-4d9e-84d8-8eeb3c751f63",
  "tool_use_result": {
    "stdout": "grep: main.log: binary file matches\n[Loading MPS to PDF converter (version 2006.09.02).]\n[3 <./fig2_pipeline.pdf>]) (./experiments.tex [4]\n[]\\T1/ptm/m/n/10 (+20) Nelson El-hage, Tris-tan Hume, Cather-ine Ols-son,\n[9]\n[10]\n[]\\T1/ptm/b/n/10.95 (+20) Code: \\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\n[11 <./fig6_dissociation.pdf>]\n[12",
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

_source line 115_

<details open><summary>🔧 Tool call — Bash · `toolu_01E6Rh6NK5ZGUEXAwaCdeMh2`</summary>

```json
{
  "command": "strings main.log | grep -E \"^\\[\" | head -20",
  "description": "Check page numbers in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "bdfb49fd-62d1-41e2-9ba1-d2fa8ce9cebd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ex5euzHCycBqRnC97eQsmS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 327,
      "cache_read_input_tokens": 70128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 327
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 116 · 2026-05-25T15:55:16.781Z_

<details><summary>↩ Tool result · `toolu_01E6Rh6NK5ZGUEXAwaCdeMh2`</summary>

```text
[Loading MPS to PDF converter (version 2006.09.02).]
[3 <./fig2_pipeline.pdf>]) (./experiments.tex [4]
[]\T1/ptm/m/n/10 (+20) Nelson El-hage, Tris-tan Hume, Cather-ine Ols-son,
[]\T1/ptm/m/n/10 (+20) Gemma Team, Mor-gane Riv-i
[10]
[]\T1/ptm/b/n/10.95 (+20) Code: \T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment
[11 <./fig6_dissociation.pdf>]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "b406176b-6e85-46fe-af45-bc894e4c5005",
  "tool_use_result": {
    "stdout": "[Loading MPS to PDF converter (version 2006.09.02).]\n[3 <./fig2_pipeline.pdf>]) (./experiments.tex [4]\n[]\\T1/ptm/m/n/10 (+20) Nelson El-hage, Tris-tan Hume, Cather-ine Ols-son,\n[]\\T1/ptm/m/n/10 (+20) Gemma Team, Mor-gane Riv-i\n[10]\n[]\\T1/ptm/b/n/10.95 (+20) Code: \\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\n[11 <./fig6_dissociation.pdf>]",
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

_source line 117_

<details open><summary>🔧 Tool call — Bash · `toolu_01WGJer8Z2RFM1MCkZXaboes`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\nlines = text.split('\\n')\nfor i, line in enumerate(lines):\n    if 'Use of AI Assistants' in line or 'Appendix' in line.strip() or line.strip().startswith('A '):\n        print(f'Line {i}: {line.strip()[:80]}')\n\" 2>/dev/null || echo \"pdftotext not available\"",
  "description": "Find where appendix starts in PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "09b387d4-6903-43f6-81f9-c41ef2e4af16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWeJY2YEkk19a7SrE4jc7V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 70455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 118 · 2026-05-25T15:55:21.856Z_

<details><summary>↩ Tool result · `toolu_01WGJer8Z2RFM1MCkZXaboes`</summary>

```text
Line 783: are reported in Appendix E. All CIs are computed
Line 934: (Appendix B) used an NVIDIA RTX PRO 6000.
Line 1455: (p = 0.284; Appendix Table 4).
Line 1480: 0.0083), matching the original 2/6 (Appendix C).
Line 1638: Appendix E), yet steering produces zero causal effect. Appendix F reports matche
Line 1825: work used AI coding and writing assistants throughout; Appendix A details the sc
Line 2502: Use of AI Assistants
Line 2756: Appendix B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c12479e6-a4e6-4e5a-9f9a-64a5bcca6b6b",
  "tool_use_result": {
    "stdout": "Line 783: are reported in Appendix E. All CIs are computed\nLine 934: (Appendix B) used an NVIDIA RTX PRO 6000.\nLine 1455: (p = 0.284; Appendix Table 4).\nLine 1480: 0.0083), matching the original 2/6 (Appendix C).\nLine 1638: Appendix E), yet steering produces zero causal effect. Appendix F reports matche\nLine 1825: work used AI coding and writing assistants throughout; Appendix A details the sc\nLine 2502: Use of AI Assistants\nLine 2756: Appendix B.",
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

_source line 119_

<details open><summary>🔧 Tool call — Bash · `toolu_01HbkikexN4J8K9QE11Yu991`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\n# Find page breaks (form feeds)\npages = text.split('\\x0c')\nfor i, page in enumerate(pages):\n    first_line = page.strip().split('\\n')[0] if page.strip() else '(empty)'\n    print(f'Page {i+1}: {first_line[:80]}')\n    if 'Use of AI' in page or 'Limitations' in page[:200]:\n        print(f'  *** Contains key section')\n\"",
  "description": "Check page layout to find main text boundary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "405cbd0a-b40d-42ab-9997-f8ad64a1fd8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdDVXNuMEWNBAepwMhq1A8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 71137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 383
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

_source line 120 · 2026-05-25T15:55:26.987Z_

<details><summary>↩ Tool result · `toolu_01HbkikexN4J8K9QE11Yu991`</summary>

```text
Page 1: English-Chinese Knowledge Conflict Signals Are Consistent With General
Page 2: (a) Cross-Lingual Knowledge Conflict                                            
Page 3: 1                    2                    3                    4                
Page 4: 239   puted via paired bootstrap (same resampled indices            model experi
Page 5: 338   confirming selectivity gaps of 21–40 pp. All exper-       Table 1: Single-
Page 6: (a) Llama-3.1-8B                                                                
Page 7: Significant (after correction)   Not significant
Page 8: Table 3: Representation steering results. Flip rate: frac-                      
Page 9: 608   Limitations                                                    near-perfec
  *** Contains key section
Page 10: 711   Matan Ifergan, Leshem Choshen, Roee Aharoni, Idan              Ricardo Rei
Page 11: 822       Knowledge conflicts for LLMs: A survey. In Pro-            Table 4: Ca
  *** Contains key section
Page 12: Table 5: AUROC and balanced accuracy for conflict
Page 13: (empty)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "c52e2bce-bfdc-437c-a086-c77f3ad23900",
  "tool_use_result": {
    "stdout": "Page 1: English-Chinese Knowledge Conflict Signals Are Consistent With General\nPage 2: (a) Cross-Lingual Knowledge Conflict                                            \nPage 3: 1                    2                    3                    4                \nPage 4: 239   puted via paired bootstrap (same resampled indices            model experi\nPage 5: 338   confirming selectivity gaps of 21–40 pp. All exper-       Table 1: Single-\nPage 6: (a) Llama-3.1-8B                                                                \nPage 7: Significant (after correction)   Not significant\nPage 8: Table 3: Representation steering results. Flip rate: frac-                      \nPage 9: 608   Limitations                                                    near-perfec\n  *** Contains key section\nPage 10: 711   Matan Ifergan, Leshem Choshen, Roee Aharoni, Idan              Ricardo Rei\nPage 11: 822       Knowledge conflicts for LLMs: A survey. In Pro-            Table 4: Ca\n  *** Contains key section\nPage 12: Table 5: AUROC and balanced accuracy for conflict\nPage 13: (empty)",
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

_source line 121_

<details><summary>Logged reasoning block</summary>

```text
The main text (including Limitations) ends on page 9. The references start at the bottom of page 9. The EMNLP rule says "8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit."

So Limitations doesn't count toward the 8-page limit. Let me check: the main text sections (Introduction through Discussion) seem to end on page 8 (the steering table is on page 8). Limitations starts on page 9 at line 608. References also start on page 9.

Wait, the user specified: "EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit."


So the main text (everything except references, limitations, and ethical considerations) must be ≤ 8 pages. The core content through Discussion fits on page 8, with Limitations and references starting on page 9, so I'm within the limit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "54521095-c6ec-4775-8240-150e8cc829b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyW5TJvpkVScD5pFxenYST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 71520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 537
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

_source line 122_

Main text ends before page 9 (Limitations on page 9 doesn't count per EMNLP rules; references and appendices are unlimited). 0 LaTeX errors, 149 words in abstract (< 200). All checks pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "ac8660cf-4ceb-4f49-876a-5457050b076c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyW5TJvpkVScD5pFxenYST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 71520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 537
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

_source line 123_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01B5iteB4K74VLB6DBCdwb2i`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "completed",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "completed",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "completed",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "completed",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "completed",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "completed",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "completed",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "completed",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "in_progress",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "96983403-50f7-448c-9f29-c57f4dd64eef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyW5TJvpkVScD5pFxenYST",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 71520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 537
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

_source line 124 · 2026-05-25T15:55:43.407Z_

<details><summary>↩ Tool result · `toolu_01B5iteB4K74VLB6DBCdwb2i`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "560915b3-08f5-4549-9c11-480e9a1ee974",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "completed",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "completed",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "completed",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "completed",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "in_progress",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "pending",
        "activeForm": "Writing fix report"
      }
    ],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "completed",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "completed",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "completed",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "completed",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "completed",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "in_progress",
        "activeForm": "Writing fix report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 125_

<details open><summary>🔧 Tool call — Write · `toolu_01YVcnFSEQs4hzoN7eF4btYj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/data_consistency_fix_report.md",
  "content": "# Data Consistency Fix Report\n\n**Date**: 2026-05-25\n**Trigger**: Reviewer flagged multiple references to stale L28 probe peak data contradicting fig6\n\n## Changes Made\n\n### 1. [CRITICAL] Abstract (`abstract.tex`)\n- **Before**: \"the probe signal peaks at late layers (88% depth)\"\n- **After**: \"the probe signal is broadly distributed across mid-to-upper layers\"\n- Trimmed from ~200+ words to **149 words** (EMNLP limit: 200)\n\n### 2. [CRITICAL] Introduction (`introduction.tex`)\n- Line 21: L28 (88%) → L15 (47%); `p = 0.002` → `p < 0.001`\n- Line 27: Rewrote Detection--decision dissociation bullet: L28 → L15, p = 0.002 → p < 0.001; shifted primary evidence framing to cross-model contrast\n\n### 3. [CRITICAL] Experiments (`experiments.tex`)\n- Line 33: \"peak at layer 28, 88% depth\" → \"peak at layer 15, 47% depth\"\n- Line 44 (fig3 caption): removed L28 as EN→EN peak, updated Fisher p = 0.002 → p < 0.001\n- Line 165 (fig5 caption): removed \"probe peak\" label from L28\n- Line 170: \"L28 (probe peak, 88% depth)\" → \"L28 (88% depth)\"\n- Line 174: \"EN→EN at L28\" → \"EN→EN probe peak (L15, 47%)\"\n\n### 4. [CRITICAL] Discussion (`discussion.tex`)\n- Line 5: Fisher p = 0.002 → p < 0.001; EN→EN at L28 → L15\n- Line 6: \"between the linear peak (L28) and the causal node (L13)\" → \"above both the linear peak (L15) and the causal node (L13)\" (MLP peak L18 is now above linear peak L15, not between)\n\n### 5. [CRITICAL] Conclusion (`conclusion.tex`)\n- Rewrote three-way dissociation: removed \"linear peak (L28)\" framing\n- New narrative: probe peak (L15), MLP peak (L18), causal node (L13) cluster in mid-layers; primary detection≠decision evidence is cross-model\n- p = 0.002 → p < 0.001\n\n### 6. [WARNING] Appendix D fig6 caption (`main.tex` line 99)\n- \"linear probe peak (L28, 88% depth)\" → \"(L15, 47% depth)\"\n- Added note about upper layers retaining signal without causal influence\n\n### 7. [WARNING] Appendix E AUROC table (`main.tex` line 111)\n- \"at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data)\" → \"for conflict probes (matched-condition data, best layer per model)\"\n\n### 8. [WARNING] Appendix F matched-condition table (`main.tex` line 146)\n- Llama: N=136 → N=201, probe accuracy 76.1% → 90.0%\n\n## Verification Results\n\n### LaTeX Compilation\n- **Errors**: 0\n- **Pages**: 12 total (main text ≤ 8, Limitations + References + Appendices on pages 9-12)\n\n### Abstract Word Count\n- **149 words** (limit: 200) ✅\n\n### Residual L28 References (all legitimate)\n| File | Line | Context | Status |\n|------|------|---------|--------|\n| experiments.tex | 160 | \"six layers L12--L28\" (tested range) | OK - factual |\n| experiments.tex | 165 | \"L28 (88%)\" (steering result) | OK - no \"probe peak\" label |\n| experiments.tex | 170 | \"L28 (88% depth)\" (negative steering result) | OK - no \"probe peak\" label |\n| experiments.tex | 174 | \"upper layers (e.g., L28)\" | OK - supplementary evidence |\n| experiments.tex | 200-201 | Table data rows | OK - actual data |\n| main.tex | 80 | Boundary table data row | OK - actual data |\n| main.tex | 99 | \"upper layers (e.g., L28)\" | OK - supplementary evidence |\n| method.tex | 64 | \"three Llama layers (L13, L18, L28)\" | OK - method description |\n\n### Residual 88% References\nAll in context of L28 being at 88% depth (factual layer position). None claim L28 as probe peak. ✅\n\n### Residual p = 0.002 References\n| File | Line | Context | Status |\n|------|------|---------|--------|\n| experiments.tex | 156 | \"Fisher $p = 0.002$\" for α=+5 at L13 | OK - specific α value p, not overall |\n| experiments.tex | 160 | \"L14 ($p = 0.002$)\" | OK - L14's value, not L13's |\n\n### \"late layer\" References\n- related_work.tex:23: \"late-layer intervention fails\" — generic statement, still accurate. ✅\n\n## Summary\nAll L28-as-probe-peak references eliminated. All p = 0.002 references for L13's overall significance corrected to p < 0.001. Remaining L28/88%/p=0.002 occurrences are legitimate (data tables, tested layers, specific α-value p-values for L13, or L14's p-value).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "b76d967f-60a9-48fe-b7fe-7ef114dd070c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nzovCrBR7yxvk4SpsSFVz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 72057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1053
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 126 · 2026-05-25T15:56:18.157Z_

<details><summary>↩ Tool result · `toolu_01YVcnFSEQs4hzoN7eF4btYj`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/data_consistency_fix_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "4463c307-89de-4405-9efb-bef4ce487248",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/data_consistency_fix_report.md",
    "content": "# Data Consistency Fix Report\n\n**Date**: 2026-05-25\n**Trigger**: Reviewer flagged multiple references to stale L28 probe peak data contradicting fig6\n\n## Changes Made\n\n### 1. [CRITICAL] Abstract (`abstract.tex`)\n- **Before**: \"the probe signal peaks at late layers (88% depth)\"\n- **After**: \"the probe signal is broadly distributed across mid-to-upper layers\"\n- Trimmed from ~200+ words to **149 words** (EMNLP limit: 200)\n\n### 2. [CRITICAL] Introduction (`introduction.tex`)\n- Line 21: L28 (88%) → L15 (47%); `p = 0.002` → `p < 0.001`\n- Line 27: Rewrote Detection--decision dissociation bullet: L28 → L15, p = 0.002 → p < 0.001; shifted primary evidence framing to cross-model contrast\n\n### 3. [CRITICAL] Experiments (`experiments.tex`)\n- Line 33: \"peak at layer 28, 88% depth\" → \"peak at layer 15, 47% depth\"\n- Line 44 (fig3 caption): removed L28 as EN→EN peak, updated Fisher p = 0.002 → p < 0.001\n- Line 165 (fig5 caption): removed \"probe peak\" label from L28\n- Line 170: \"L28 (probe peak, 88% depth)\" → \"L28 (88% depth)\"\n- Line 174: \"EN→EN at L28\" → \"EN→EN probe peak (L15, 47%)\"\n\n### 4. [CRITICAL] Discussion (`discussion.tex`)\n- Line 5: Fisher p = 0.002 → p < 0.001; EN→EN at L28 → L15\n- Line 6: \"between the linear peak (L28) and the causal node (L13)\" → \"above both the linear peak (L15) and the causal node (L13)\" (MLP peak L18 is now above linear peak L15, not between)\n\n### 5. [CRITICAL] Conclusion (`conclusion.tex`)\n- Rewrote three-way dissociation: removed \"linear peak (L28)\" framing\n- New narrative: probe peak (L15), MLP peak (L18), causal node (L13) cluster in mid-layers; primary detection≠decision evidence is cross-model\n- p = 0.002 → p < 0.001\n\n### 6. [WARNING] Appendix D fig6 caption (`main.tex` line 99)\n- \"linear probe peak (L28, 88% depth)\" → \"(L15, 47% depth)\"\n- Added note about upper layers retaining signal without causal influence\n\n### 7. [WARNING] Appendix E AUROC table (`main.tex` line 111)\n- \"at peak probing layer (L28 for Llama, L24 for Gemma, L18 for Qwen; matched-condition data)\" → \"for conflict probes (matched-condition data, best layer per model)\"\n\n### 8. [WARNING] Appendix F matched-condition table (`main.tex` line 146)\n- Llama: N=136 → N=201, probe accuracy 76.1% → 90.0%\n\n## Verification Results\n\n### LaTeX Compilation\n- **Errors**: 0\n- **Pages**: 12 total (main text ≤ 8, Limitations + References + Appendices on pages 9-12)\n\n### Abstract Word Count\n- **149 words** (limit: 200) ✅\n\n### Residual L28 References (all legitimate)\n| File | Line | Context | Status |\n|------|------|---------|--------|\n| experiments.tex | 160 | \"six layers L12--L28\" (tested range) | OK - factual |\n| experiments.tex | 165 | \"L28 (88%)\" (steering result) | OK - no \"probe peak\" label |\n| experiments.tex | 170 | \"L28 (88% depth)\" (negative steering result) | OK - no \"probe peak\" label |\n| experiments.tex | 174 | \"upper layers (e.g., L28)\" | OK - supplementary evidence |\n| experiments.tex | 200-201 | Table data rows | OK - actual data |\n| main.tex | 80 | Boundary table data row | OK - actual data |\n| main.tex | 99 | \"upper layers (e.g., L28)\" | OK - supplementary evidence |\n| method.tex | 64 | \"three Llama layers (L13, L18, L28)\" | OK - method description |\n\n### Residual 88% References\nAll in context of L28 being at 88% depth (factual layer position). None claim L28 as probe peak. ✅\n\n### Residual p = 0.002 References\n| File | Line | Context | Status |\n|------|------|---------|--------|\n| experiments.tex | 156 | \"Fisher $p = 0.002$\" for α=+5 at L13 | OK - specific α value p, not overall |\n| experiments.tex | 160 | \"L14 ($p = 0.002$)\" | OK - L14's value, not L13's |\n\n### \"late layer\" References\n- related_work.tex:23: \"late-layer intervention fails\" — generic statement, still accurate. ✅\n\n## Summary\nAll L28-as-probe-peak references eliminated. All p = 0.002 references for L13's overall significance corrected to p < 0.001. Remaining L28/88%/p=0.002 occurrences are legitimate (data tables, tested layers, specific α-value p-values for L13, or L14's p-value).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 127_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01X5PYe1VcjsTrVZXbCPWMec`</summary>

```json
{
  "todos": [
    {
      "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
      "status": "completed",
      "activeForm": "Fixing Abstract"
    },
    {
      "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Introduction"
    },
    {
      "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
      "status": "completed",
      "activeForm": "Fixing Experiments"
    },
    {
      "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
      "status": "completed",
      "activeForm": "Fixing Discussion"
    },
    {
      "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
      "status": "completed",
      "activeForm": "Fixing Conclusion"
    },
    {
      "content": "Fix Appendix D: fig6 caption L28→L15",
      "status": "completed",
      "activeForm": "Fixing Appendix D fig6 caption"
    },
    {
      "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
      "status": "completed",
      "activeForm": "Fixing Appendix E AUROC table"
    },
    {
      "content": "Fix Appendix F: update Llama N=136→N=201 if found",
      "status": "completed",
      "activeForm": "Fixing Appendix F matched-condition table"
    },
    {
      "content": "Full-text grep for remaining L28/88%/p=0.002 references",
      "status": "completed",
      "activeForm": "Running full-text grep verification"
    },
    {
      "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
      "status": "completed",
      "activeForm": "Compiling and verifying"
    },
    {
      "content": "Write data_consistency_fix_report.md",
      "status": "completed",
      "activeForm": "Writing fix report"
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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "68a88aeb-66f9-4ad9-b1cf-23ad97c51d17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZQBqJpjUW2bUqpMYrSuEq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 73110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1561
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

_source line 128 · 2026-05-25T15:56:25.878Z_

<details><summary>↩ Tool result · `toolu_01X5PYe1VcjsTrVZXbCPWMec`</summary>

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
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "a6e4c901-f6ce-4622-a3e6-bcbcaa6985a6",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "completed",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "completed",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "completed",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "completed",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "completed",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "in_progress",
        "activeForm": "Writing fix report"
      }
    ],
    "newTodos": [
      {
        "content": "Fix Abstract: remove L28/88% reference, trim to <200 words",
        "status": "completed",
        "activeForm": "Fixing Abstract"
      },
      {
        "content": "Fix Introduction: L28→L15, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Introduction"
      },
      {
        "content": "Fix Experiments: L28 probe peak refs, fig3 caption, fig5 caption",
        "status": "completed",
        "activeForm": "Fixing Experiments"
      },
      {
        "content": "Fix Discussion: L28→L15, p=0.002→p<0.001, restructure MLP ordering",
        "status": "completed",
        "activeForm": "Fixing Discussion"
      },
      {
        "content": "Fix Conclusion: rewrite three-way dissociation, p=0.002→p<0.001",
        "status": "completed",
        "activeForm": "Fixing Conclusion"
      },
      {
        "content": "Fix Appendix D: fig6 caption L28→L15",
        "status": "completed",
        "activeForm": "Fixing Appendix D fig6 caption"
      },
      {
        "content": "Fix Appendix E: remove peak layer annotations from AUROC table",
        "status": "completed",
        "activeForm": "Fixing Appendix E AUROC table"
      },
      {
        "content": "Fix Appendix F: update Llama N=136→N=201 if found",
        "status": "completed",
        "activeForm": "Fixing Appendix F matched-condition table"
      },
      {
        "content": "Full-text grep for remaining L28/88%/p=0.002 references",
        "status": "completed",
        "activeForm": "Running full-text grep verification"
      },
      {
        "content": "Compile LaTeX and verify (0 errors, ≤8 pages, <200 words abstract)",
        "status": "completed",
        "activeForm": "Compiling and verifying"
      },
      {
        "content": "Write data_consistency_fix_report.md",
        "status": "completed",
        "activeForm": "Writing fix report"
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

全部修复完成。

**修改汇总**（8 个文件，跨 6 个 .tex 文件 + 1 个报告）：

| 修复项 | 文件 | 变更 |
|--------|------|------|
| Abstract | abstract.tex | 移除 "late layers (88%)"，改为 broadly distributed；精简至 149 words |
| Introduction ×2 | introduction.tex | L28→L15, p=0.002→p<0.001；重构 dissociation bullet |
| Experiments ×5 | experiments.tex | 峰值层 L28→L15；fig3/fig5 caption；移除 L28 "probe peak" 标签 |
| Discussion | discussion.tex | p=0.002→p<0.001；L28→L15；MLP ordering 重构 |
| Conclusion | conclusion.tex | 重写 three-way dissociation 叙事；p<0.001；cross-model 证据为主 |
| Appendix D | main.tex | fig6 caption L28→L15 |
| Appendix E | main.tex | AUROC 表移除 peak layer 标注 |
| Appendix F | main.tex | Llama N=136→N=201, probe 76.1%→90.0% |

**验证结果**：0 LaTeX 错误，正文 ≤8 页，abstract 149 words，残留 L28/88%/p=0.002 引用全部合法（数据表行、测试层描述、特定 α 值 p 值）。报告已写入 `data_consistency_fix_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "uuid": "5b9e9440-4008-4cb3-8770-695168865b59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wgsrvb2GQMFeMW8hW8Acm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 74671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 584
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

_source line 130_

全部修复完成。

**修改汇总**（8 个文件，跨 6 个 .tex 文件 + 1 个报告）：

| 修复项 | 文件 | 变更 |
|--------|------|------|
| Abstract | abstract.tex | 移除 "late layers (88%)"，改为 broadly distributed；精简至 149 words |
| Introduction ×2 | introduction.tex | L28→L15, p=0.002→p<0.001；重构 dissociation bullet |
| Experiments ×5 | experiments.tex | 峰值层 L28→L15；fig3/fig5 caption；移除 L28 "probe peak" 标签 |
| Discussion | discussion.tex | p=0.002→p<0.001；L28→L15；MLP ordering 重构 |
| Conclusion | conclusion.tex | 重写 three-way dissociation 叙事；p<0.001；cross-model 证据为主 |
| Appendix D | main.tex | fig6 caption L28→L15 |
| Appendix E | main.tex | AUROC 表移除 peak layer 标注 |
| Appendix F | main.tex | Llama N=136→N=201, probe 76.1%→90.0% |

**验证结果**：0 LaTeX 错误，正文 ≤8 页，abstract 149 words，残留 L28/88%/p=0.002 引用全部合法（数据表行、测试层描述、特定 α 值 p 值）。报告已写入 `data_consistency_fix_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 430448,
  "duration_api_ms": 427828,
  "num_turns": 52,
  "stop_reason": "end_turn",
  "session_id": "07e1aa3d-56cb-490c-97bb-d6b3fe0f766c",
  "total_cost_usd": 1.9400965,
  "usage": {
    "input_tokens": 35,
    "cache_creation_input_tokens": 63414,
    "cache_read_input_tokens": 1856724,
    "output_tokens": 24518,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 63414,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 444,
        "cache_read_input_tokens": 74671,
        "cache_creation_input_tokens": 584,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 584
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2187,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002272,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 35,
      "outputTokens": 24518,
      "cacheReadInputTokens": 1856724,
      "cacheCreationInputTokens": 63414,
      "webSearchRequests": 0,
      "costUSD": 1.9378244999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fb48784c-1c9c-426a-b5f5-90e3249e0166"
}
```

</details>

---
