# paper emnlp submission prep

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 36
- **Original source:** `logs/workers/worker_paper_emnlp-submission-prep_20260516T030521.log`
- **Structured JSON:** [`b632179cad40bceccba9.json`](../../sessions/b6/b632179cad40bceccba9.json)

## Before a recorded user message

89 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "02d545fd-6aaf-446d-9553-a9a6d76da4c1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1778905200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f5b2d9f4-92b1-4419-a9c3-3dbff873a41c",
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the .tex files in the paper directory to perform the EMNLP submission checklist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "1c7713db-38d1-460e-ac3a-7e4f5b64dcc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpeX3WUawZvgH5cAdLrLY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12410,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12410
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

I'll read all the paper files in parallel to perform the checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "023c1868-b2e2-40d9-a0c2-c43e37805a2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpeX3WUawZvgH5cAdLrLY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12410,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12410
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Glob · `toolu_016rT7QXX4E6yWb5ArENB9XQ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "90155bcf-fbff-4467-8899-4414977d3959",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpeX3WUawZvgH5cAdLrLY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12410,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12410
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 7 · 2026-05-16T03:05:30.558Z_

<details><summary>↩ Tool result · `toolu_016rT7QXX4E6yWb5ArENB9XQ`</summary>

```text
artifacts/_project/paper/_backup/method_01fe38.tex
artifacts/_project/paper/_backup/ethics_7f2659.tex
artifacts/_project/paper/_backup/table1.tex
artifacts/_project/paper/_backup/table1_329527.tex
artifacts/_project/paper/_backup/table2.tex
artifacts/_project/paper/_backup/table2_373612.tex
artifacts/_project/paper/_backup/table3.tex
artifacts/_project/paper/_backup/table3_fc4017.tex
artifacts/_project/paper/_backup/discussion_d3a579.tex
artifacts/_project/paper/_backup/table4.tex
artifacts/_project/paper/_backup/table4_49aebb.tex
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/_backup/ethics_25b81b.tex
artifacts/_project/paper/_backup/related_work_2ce9dd.tex
artifacts/_project/paper/_backup/main_53f11a.tex
artifacts/_project/paper/_backup/conclusion_b5f10d.tex
artifacts/_project/paper/_backup/introduction_4bbcfd.tex
artifacts/_project/paper/_backup/conclusion_70534e.tex
artifacts/_project/paper/_backup/discussion_c98572.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/_backup/abstract_014854.tex
artifacts/_project/paper/_backup/results_b30771.tex
artifacts/_project/paper/_backup/limitations_69ebec.tex
artifacts/_project/paper/_backup/limitations_b3d194.tex
artifacts/_project/paper/_backup/method_e59d28.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/appendix_classifier.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/appendix_qlora.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/appendix_finer_depth.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "ad3d73eb-1a66-4223-8207-b10e0b31f110",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/_backup/method_01fe38.tex",
      "artifacts/_project/paper/_backup/ethics_7f2659.tex",
      "artifacts/_project/paper/_backup/table1.tex",
      "artifacts/_project/paper/_backup/table1_329527.tex",
      "artifacts/_project/paper/_backup/table2.tex",
      "artifacts/_project/paper/_backup/table2_373612.tex",
      "artifacts/_project/paper/_backup/table3.tex",
      "artifacts/_project/paper/_backup/table3_fc4017.tex",
      "artifacts/_project/paper/_backup/discussion_d3a579.tex",
      "artifacts/_project/paper/_backup/table4.tex",
      "artifacts/_project/paper/_backup/table4_49aebb.tex",
      "artifacts/_project/paper/ethics.tex",
      "artifacts/_project/paper/_backup/ethics_25b81b.tex",
      "artifacts/_project/paper/_backup/related_work_2ce9dd.tex",
      "artifacts/_project/paper/_backup/main_53f11a.tex",
      "artifacts/_project/paper/_backup/conclusion_b5f10d.tex",
      "artifacts/_project/paper/_backup/introduction_4bbcfd.tex",
      "artifacts/_project/paper/_backup/conclusion_70534e.tex",
      "artifacts/_project/paper/_backup/discussion_c98572.tex",
      "artifacts/_project/paper/appendix_length.tex",
      "artifacts/_project/paper/_backup/abstract_014854.tex",
      "artifacts/_project/paper/_backup/results_b30771.tex",
      "artifacts/_project/paper/_backup/limitations_69ebec.tex",
      "artifacts/_project/paper/_backup/limitations_b3d194.tex",
      "artifacts/_project/paper/_backup/method_e59d28.tex",
      "artifacts/_project/paper/appendix_prompt_type.tex",
      "artifacts/_project/paper/appendix_confusion_matrix.tex",
      "artifacts/_project/paper/appendix_lofo.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/appendix_human_edit.tex",
      "artifacts/_project/paper/appendix_classifier.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/table4.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/appendix_qlora.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/appendix_finer_depth.tex"
    ],
    "durationMs": 10,
    "numFiles": 42,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_017TF7cRhaHpatmCkn6qUbDM`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "f9f09837-5789-49c1-91fc-819a0374af63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpeX3WUawZvgH5cAdLrLY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12410,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12410
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 9 · 2026-05-16T03:05:31.613Z_

<details><summary>↩ Tool result · `toolu_017TF7cRhaHpatmCkn6qUbDM`</summary>

```text
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "5490f3fa-ed66-43c5-8b38-d54286732d52",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 5,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_016kV5itBigReq6LUjCDJzJu`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "d5cc2756-3bc1-4f0c-aead-e0c0ec973e39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpeX3WUawZvgH5cAdLrLY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12410,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12410
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 11 · 2026-05-16T03:05:31.776Z_

<details><summary>↩ Tool result · `toolu_016kV5itBigReq6LUjCDJzJu`</summary>

```text
docs/paper/appendix_confusion_matrix.tex
docs/paper/appendix_length.tex
docs/paper/appendix_lofo.tex
docs/paper/appendix_prompt_type.tex
docs/paper/ethics.tex
docs/paper/table3.tex
docs/paper/table4.tex
docs/paper/related_work.tex
docs/paper/appendix_classifier.tex
docs/paper/appendix_human_edit.tex
docs/paper/table1.tex
docs/paper/table2.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/results.tex
docs/paper/method.tex
docs/paper/appendix_qlora.tex
docs/paper/main.tex
docs/paper/appendix_finer_depth.tex
docs/paper/discussion.tex
docs/paper/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "17e37a8c-49ad-489c-9404-f7edf80b0a67",
  "tool_use_result": {
    "filenames": [
      "docs/paper/appendix_confusion_matrix.tex",
      "docs/paper/appendix_length.tex",
      "docs/paper/appendix_lofo.tex",
      "docs/paper/appendix_prompt_type.tex",
      "docs/paper/ethics.tex",
      "docs/paper/table3.tex",
      "docs/paper/table4.tex",
      "docs/paper/related_work.tex",
      "docs/paper/appendix_classifier.tex",
      "docs/paper/appendix_human_edit.tex",
      "docs/paper/table1.tex",
      "docs/paper/table2.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/results.tex",
      "docs/paper/method.tex",
      "docs/paper/appendix_qlora.tex",
      "docs/paper/main.tex",
      "docs/paper/appendix_finer_depth.tex",
      "docs/paper/discussion.tex",
      "docs/paper/limitations.tex"
    ],
    "durationMs": 5,
    "numFiles": 22,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 12_

Now let me read all the main .tex files (excluding backups) in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "bb667846-843f-4f0a-964e-2f2c0d95fb08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_014SxCX4iTu7a3yQVnZpndnT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "6e68469b-b148-494f-acfc-d4c549191ca8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 14 · 2026-05-16T03:05:35.706Z_

<details><summary>↩ Tool result · `toolu_014SxCX4iTu7a3yQVnZpndnT`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	
11	\graphicspath{{../chart/}}
12	
13	\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\in Non-Paraphrastic LLM Text Chains}
14	
15	\author{Anonymous}
16	
17	\begin{document}
18	\maketitle
19	
20	\input{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{results}
26	
27	\input{discussion}
28	\input{conclusion}
29	\input{limitations}
30	\input{ethics}
31	
32	\bibliography{references}
33	
34	\appendix
35	\section{Length Confound Analysis}
36	\label{app:length}
37	\input{appendix_length}
38	
39	\section{Prompt Type Generalization}
40	\label{app:prompt-type}
41	\input{appendix_prompt_type}
42	
43	\section{Finer-Grained Depth Classification}
44	\label{app:finer-depth}
45	\input{appendix_finer_depth}
46	
47	\section{End-to-End Depth Classification (QLoRA)}
48	\label{app:qlora}
49	\input{appendix_qlora}
50	
51	\section{Leave-One-Feature-Out Analysis}
52	\label{app:lofo}
53	\input{appendix_lofo}
54	
55	\section{Confusion Matrix}
56	\label{app:confusion}
57	\input{appendix_confusion_matrix}
58	
59	\section{Classifier Sensitivity}
60	\label{app:classifier}
61	\input{appendix_classifier}
62	
63	\section{Human-Edit Robustness}
64	\label{app:human-edit}
65	\input{appendix_human_edit}
66	
67	\end{document}
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "29688d1c-fbd9-4abb-9e21-e48db32d2118",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
      "content": "% EMNLP 2026 ARR Submission — ACL 2023 Template\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{amsmath}\n\n\\graphicspath{{../chart/}}\n\n\\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\\\in Non-Paraphrastic LLM Text Chains}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{results}\n\n\\input{discussion}\n\\input{conclusion}\n\\input{limitations}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\\section{Length Confound Analysis}\n\\label{app:length}\n\\input{appendix_length}\n\n\\section{Prompt Type Generalization}\n\\label{app:prompt-type}\n\\input{appendix_prompt_type}\n\n\\section{Finer-Grained Depth Classification}\n\\label{app:finer-depth}\n\\input{appendix_finer_depth}\n\n\\section{End-to-End Depth Classification (QLoRA)}\n\\label{app:qlora}\n\\input{appendix_qlora}\n\n\\section{Leave-One-Feature-Out Analysis}\n\\label{app:lofo}\n\\input{appendix_lofo}\n\n\\section{Confusion Matrix}\n\\label{app:confusion}\n\\input{appendix_confusion_matrix}\n\n\\section{Classifier Sensitivity}\n\\label{app:classifier}\n\\input{appendix_classifier}\n\n\\section{Human-Edit Robustness}\n\\label{app:human-edit}\n\\input{appendix_human_edit}\n\n\\end{document}\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01M238nuLyhVGL2gRTcSoqhJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "76c45802-0164-4c11-801e-698a61483d0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 16 · 2026-05-16T03:05:36.592Z_

<details><summary>↩ Tool result · `toolu_01M238nuLyhVGL2gRTcSoqhJ`</summary>

```text
1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	As LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
4	We formulate \emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.
5	We characterize a \emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for gen-1 vs.\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\,=\,0.051).
7	In our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "02571397-fce8-4d08-a4b7-a047df614e84",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
      "content": "% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains\n\\begin{abstract}\nAs LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.\nA 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination---excluding gen-0 to avoid shared-seed overlap---($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).\nIn our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.\n\\end{abstract}\n",
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01Skm4Rt9LdG1M8s6Kv4vum4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "0f6d23aa-06d8-445d-9493-28c2619fb563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 18 · 2026-05-16T03:05:37.093Z_

<details><summary>↩ Tool result · `toolu_01Skm4Rt9LdG1M8s6Kv4vum4`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.
5	Estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.
6	The result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.
7	
8	Existing detectors \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.
9	This conflates qualitatively different material.
10	A first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.
11	A third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.
12	Treating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.
13	
14	We argue that a finer-grained characterization is needed: \emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label.
15	We refer to the overall framework---features, classifier, and evaluation protocol---as \emph{depth fingerprinting}, distinguishing the method from the task it addresses.
16	No existing method addresses this task directly in non-paraphrastic continuation chains.
17	When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\S\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.
18	Concurrent work on iterative paraphrasing chains \cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.
19	These results do not extend to \emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.
20	We focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).
21	
22	We study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).
23	We characterize a \emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.
24	This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.
25	The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\ gen-2+), with per-generator consistency (std\,=\,0.051).
26	
27	We also report a negative finding.
28	Depth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\ 2.387 depth-stratified).
29	In our experimental setting, depth fingerprinting is an effective \emph{diagnostic} tool for characterizing text provenance, not a \emph{curative} tool for data selection.
30	
31	Our contributions are:
32	\begin{enumerate}[nosep,leftmargin=*]
33	    \item \textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.
34	    \item \textbf{Empirical characterization.} We characterize differential depth response across six base-model generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\,=\,0.723 (95\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\,=\,0.051).
35	    \item \textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.
36	\end{enumerate}
37	
38	The remainder of this paper is organized as follows.
39	\S\ref{sec:related} surveys related work on text detection, model collapse, and data quality.
40	\S\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.
41	\S\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.
42	\S\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "e1de6854-e168-427c-be0d-77baaef4a634",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six base-model generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01D3c5GKJzYZKRjurmQKPSAv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "349baabd-2706-4897-b517-55bbef5d16de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 20 · 2026-05-16T03:05:37.630Z_

<details><summary>↩ Tool result · `toolu_01D3c5GKJzYZKRjurmQKPSAv`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	Methods for distinguishing human-written from machine-generated text have evolved from statistical tests on token-level distributions \cite{gltr,grover,release_strategies} to zero-shot approaches exploiting reference-model likelihoods \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers over linguistic features \cite{feat_aug_transformer,reliable_detection,ld_score}.
8	Recent work has pursued diverse detection signals: \citet{intrinsic_dimension} use intrinsic dimensionality estimates, \citet{diveye} propose surprisal diversity features directly comparable to our distributional features, and \citet{generator_barrier} characterize the distributional gap between human and model outputs.
9	\citet{wu_survey_2025} provide the most comprehensive recent survey; see also \citet{jawahar_survey} for an earlier overview.
10	Commercial systems such as GPTZero provide trained-classifier detection but are non-reproducible due to proprietary model access, precluding controlled baseline comparison; we restrict evaluation to open methods.
11	A persistent limitation is that all these methods produce binary (real vs.\ synthetic) decisions.
12	Recent efforts extend detection to multi-class settings: \citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.
13	These approaches discriminate among different \emph{sources} (human vs.\ specific models) rather than recursive generation \emph{depth} within a single generator's chain.
14	Even when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently.
15	\citet{paraphrase_evades} and \citet{detection_possibilities} further demonstrate that detection robustness degrades under distributional shift.
16	Our reference-model entropy features are functionally NLL-based out-of-distribution scores \cite{ood_baseline}; the contribution is not a new detection method but the task formulation (ordinal depth estimation) and the empirical finding that combining drifting and stationary features yields consistent cross-generator performance.
17	
18	\paragraph{Source attribution vs.\ depth estimation.}
19	A related but distinct task is \emph{source attribution}: identifying \emph{which} model generated a given text.
20	\citet{uchendu_attribution} train multi-class classifiers over stylometric features to distinguish outputs of different generators, and \citet{munir_looking_glass} learn attribution models that generalize across unseen language models.
21	These methods answer \emph{who} generated the text; depth estimation answers \emph{how many recursive steps} produced it.
22	The two tasks are orthogonal: a single generator can produce text at any depth, and texts at the same depth may originate from different generators.
23	Our LOGO evaluation explicitly decouples generator identity from depth by holding out entire generators, ensuring that the classifier learns depth signal rather than generator fingerprints.
24	
25	\subsection{Model Collapse and Iterative Generation}
26	\label{sec:related-collapse}
27	
28	A growing body of work studies quality degradation when models are trained on their own outputs.
29	\citet{self_consuming_mad} demonstrate that self-consuming generative models progressively lose distributional coverage, and \citet{curse_of_recursion} show that model collapse is inevitable in successive fine-tuning rounds without fresh human data, though \citet{model_collapse_avoidable} identify conditions under which careful data mixing can mitigate this effect.
30	\citet{strong_model_collapse} extend these results to larger-scale settings.
31	These studies focus on \emph{training-loop} degradation, where model weights are updated on recursive data.
32	Our setting is different: we study \emph{inference chains}, where a fixed model generates text conditioned on its own prior output without retraining.
33	
34	Two concurrent lines of work are most directly relevant.
35	\citet{broken_telephone} analyze paraphrasing and translation chains, showing progressive information loss analogous to the telephone game.
36	\citet{markovian_chains} provide a theoretical framework for convergence in iterative text transformations, demonstrating that semantic-preservation constraints induce attractor dynamics that bound distinguishable depth to approximately three classes.
37	Our work differs in two respects: we study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal beyond the attractor bound; and we focus on \emph{estimating} depth from text features rather than characterizing convergence behavior.
38	
39	\subsection{Vocabulary Diversity and Stylometry}
40	\label{sec:related-diversity}
41	
42	Declining lexical diversity in LLM-generated text is documented in both training \cite{curious_decline} and deployment \cite{writing_diversity} settings.
43	Our surface features---type-token ratio and hapax ratio---instantiate this observation for inference chains, where we show monotonic diversity decline across generation depths without any model retraining.
44	
45	These features are classical stylometric measures with a long history in authorship attribution \cite{stamatatos_survey,koppel_authorship}.
46	\citet{uchendu_attribution} extend stylometric and neural methods to multi-class attribution of text to specific generators.
47	We push beyond generator identity to the \emph{depth} dimension: text from the same generator at different depths exhibits systematically different feature profiles, and these profiles generalize across generators.
48	Sampling strategies also affect diversity; \citet{nucleus_sampling} show that top-$p$ sampling mitigates some degeneration, but our results demonstrate that diversity still declines monotonically across recursive application of the same sampling procedure.
49	
50	\subsection{Data Quality and Provenance}
51	\label{sec:related-provenance}
52	
53	Scalable data curation relies on quality signals to filter web-crawled corpora.
54	\citet{dsir} select pretraining data to match a target distribution, \citet{qurating} learn quality scores from LLM judgments, and \citet{ccnet} filter Common Crawl via perplexity-based heuristics.
55	Generation depth is a complementary provenance signal: it characterizes \emph{how many steps removed} text is from a human source, orthogonal to content quality per se.
56	
57	An alternative approach is proactive provenance through watermarking \cite{watermark_llm,synthid_text,aaronson_watermark}, where identifiable patterns are embedded during generation.
58	However, \citet{chainwash} demonstrate that watermark strength decays across multi-step generation chains, motivating passive post-hoc methods that do not require generator cooperation.
59	Our depth fingerprinting is such a method: it operates on text alone without assuming access to the generating model or an embedded watermark.
60	At the feature level, our reference-model NLL analysis connects to \citet{min_k_percent}, who use the probability distribution's lower tail for membership inference; we analyze the full NLL distribution for a different purpose---ordinal depth estimation rather than training-set membership.
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "0df4e353-a0b1-4cf7-956c-e85b29ec7927",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{AI-Generated Text Detection}\n\\label{sec:related-detection}\n\nMethods for distinguishing human-written from machine-generated text have evolved from statistical tests on token-level distributions \\cite{gltr,grover,release_strategies} to zero-shot approaches exploiting reference-model likelihoods \\cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers over linguistic features \\cite{feat_aug_transformer,reliable_detection,ld_score}.\nRecent work has pursued diverse detection signals: \\citet{intrinsic_dimension} use intrinsic dimensionality estimates, \\citet{diveye} propose surprisal diversity features directly comparable to our distributional features, and \\citet{generator_barrier} characterize the distributional gap between human and model outputs.\n\\citet{wu_survey_2025} provide the most comprehensive recent survey; see also \\citet{jawahar_survey} for an earlier overview.\nCommercial systems such as GPTZero provide trained-classifier detection but are non-reproducible due to proprietary model access, precluding controlled baseline comparison; we restrict evaluation to open methods.\nA persistent limitation is that all these methods produce binary (real vs.\\ synthetic) decisions.\nRecent efforts extend detection to multi-class settings: \\citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \\cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.\nThese approaches discriminate among different \\emph{sources} (human vs.\\ specific models) rather than recursive generation \\emph{depth} within a single generator's chain.\nEven when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently.\n\\citet{paraphrase_evades} and \\citet{detection_possibilities} further demonstrate that detection robustness degrades under distributional shift.\nOur reference-model entropy features are functionally NLL-based out-of-distribution scores \\cite{ood_baseline}; the contribution is not a new detection method but the task formulation (ordinal depth estimation) and the empirical finding that combining drifting and stationary features yields consistent cross-generator performance.\n\n\\paragraph{Source attribution vs.\\ depth estimation.}\nA related but distinct task is \\emph{source attribution}: identifying \\emph{which} model generated a given text.\n\\citet{uchendu_attribution} train multi-class classifiers over stylometric features to distinguish outputs of different generators, and \\citet{munir_looking_glass} learn attribution models that generalize across unseen language models.\nThese methods answer \\emph{who} generated the text; depth estimation answers \\emph{how many recursive steps} produced it.\nThe two tasks are orthogonal: a single generator can produce text at any depth, and texts at the same depth may originate from different generators.\nOur LOGO evaluation explicitly decouples generator identity from depth by holding out entire generators, ensuring that the classifier learns depth signal rather than generator fingerprints.\n\n\\subsection{Model Collapse and Iterative Generation}\n\\label{sec:related-collapse}\n\nA growing body of work studies quality degradation when models are trained on their own outputs.\n\\citet{self_consuming_mad} demonstrate that self-consuming generative models progressively lose distributional coverage, and \\citet{curse_of_recursion} show that model collapse is inevitable in successive fine-tuning rounds without fresh human data, though \\citet{model_collapse_avoidable} identify conditions under which careful data mixing can mitigate this effect.\n\\citet{strong_model_collapse} extend these results to larger-scale settings.\nThese studies focus on \\emph{training-loop} degradation, where model weights are updated on recursive data.\nOur setting is different: we study \\emph{inference chains}, where a fixed model generates text conditioned on its own prior output without retraining.\n\nTwo concurrent lines of work are most directly relevant.\n\\citet{broken_telephone} analyze paraphrasing and translation chains, showing progressive information loss analogous to the telephone game.\n\\citet{markovian_chains} provide a theoretical framework for convergence in iterative text transformations, demonstrating that semantic-preservation constraints induce attractor dynamics that bound distinguishable depth to approximately three classes.\nOur work differs in two respects: we study \\emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal beyond the attractor bound; and we focus on \\emph{estimating} depth from text features rather than characterizing convergence behavior.\n\n\\subsection{Vocabulary Diversity and Stylometry}\n\\label{sec:related-diversity}\n\nDeclining lexical diversity in LLM-generated text is documented in both training \\cite{curious_decline} and deployment \\cite{writing_diversity} settings.\nOur surface features---type-token ratio and hapax ratio---instantiate this observation for inference chains, where we show monotonic diversity decline across generation depths without any model retraining.\n\nThese features are classical stylometric measures with a long history in authorship attribution \\cite{stamatatos_survey,koppel_authorship}.\n\\citet{uchendu_attribution} extend stylometric and neural methods to multi-class attribution of text to specific generators.\nWe push beyond generator identity to the \\emph{depth} dimension: text from the same generator at different depths exhibits systematically different feature profiles, and these profiles generalize across generators.\nSampling strategies also affect diversity; \\citet{nucleus_sampling} show that top-$p$ sampling mitigates some degeneration, but our results demonstrate that diversity still declines monotonically across recursive application of the same sampling procedure.\n\n\\subsection{Data Quality and Provenance}\n\\label{sec:related-provenance}\n\nScalable data curation relies on quality signals to filter web-crawled corpora.\n\\citet{dsir} select pretraining data to match a target distribution, \\citet{qurating} learn quality scores from LLM judgments, and \\citet{ccnet} filter Common Crawl via perplexity-based heuristics.\nGeneration depth is a complementary provenance signal: it characterizes \\emph{how many steps removed} text is from a human source, orthogonal to content quality per se.\n\nAn alternative approach is proactive provenance through watermarking \\cite{watermark_llm,synthid_text,aaronson_watermark}, where identifiable patterns are embedded during generation.\nHowever, \\citet{chainwash} demonstrate that watermark strength decays across multi-step generation chains, motivating passive post-hoc methods that do not require generator cooperation.\nOur depth fingerprinting is such a method: it operates on text alone without assuming access to the generating model or an embedded watermark.\nAt the feature level, our reference-model NLL analysis connects to \\citet{min_k_percent}, who use the probability distribution's lower tail for membership inference; we analyze the full NLL distribution for a different purpose---ordinal depth estimation rather than training-set membership.\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01SsJtGsHD3HcoG9JCsAUiaR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "4d2a913f-ffef-41cc-a3d1-f45d1e383d19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 22 · 2026-05-16T03:05:38.039Z_

<details><summary>↩ Tool result · `toolu_01SsJtGsHD3HcoG9JCsAUiaR`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using six generators spanning three model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, and \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}.
17	This selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	The same pool of seed passages serves as gen-0 for all generators.
21	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
22	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
23	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
24	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
25	The resulting dataset contains approximately 27{,}000 texts across all generators and depths.
26	For classification, depths 2--4 are collapsed into the $2{+}$ class.
27	
28	\subsection{Feature Extraction}
29	\label{sec:features}
30	
31	The seven features are motivated by two complementary views of distributional drift.
32	Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.
33	Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).
34	This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\S\ref{sec:results-differential}).
35	
36	We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.
37	
38	\paragraph{Reference-model features.}
39	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
40	Although Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).
41	From the resulting NLL sequence, we extract five statistics:
42	\begin{itemize}[nosep,leftmargin=*]
43	    \item \textbf{entropy\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;
44	    \item \textbf{entropy\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;
45	    \item \textbf{entropy\_max}: maximum token-level NLL, capturing the most surprising token;
46	    \item \textbf{entropy\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.
47	    Although entropy\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\Delta$F1\,=\,+0.01\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;
48	    \item \textbf{tail\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.
49	    The 90th percentile threshold follows standard practice in heavy-tail analysis \cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\,pp) across thresholds from the 85th to 95th percentile.
50	\end{itemize}
51	
52	\paragraph{Surface features.}
53	Two features capture lexical diversity without requiring a reference model:
54	\begin{itemize}[nosep,leftmargin=*]
55	    \item \textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);
56	    \item \textbf{hapax\_ratio}: proportion of words appearing exactly once (\emph{hapax legomena}).
57	\end{itemize}
58	
59	\paragraph{Feature complementarity.}
60	The grouping reflects an empirical pattern we term \emph{differential depth response}: central-tendency and diversity features (entropy\_mean, TTR, hapax\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\_std, tail\_decay) remain near-stationary.
61	This differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.
62	As shown in \S\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.
63	
64	\subsection{Evaluation Protocol}
65	\label{sec:evaluation}
66	
67	\paragraph{Cross-validation.}
68	To evaluate generalization to unseen generators, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.
69	We additionally report \textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.
70	
71	\paragraph{Classifier.}
72	We use XGBoost \cite{xgboost} as the classifier throughout.
73	Gradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.
74	We use $n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.
75	Baseline detectors (\S\ref{sec:results-baselines}) use the same XGBoost framework with $n\_\text{estimators}{=}100$ and $\max\_\text{depth}{=}3$ to avoid overfitting their single-feature input.
76	LOGO F1 is stable across random seeds (mean\,=\,0.789, std\,=\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.
77	Alternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.
78	We evaluated two ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall ordinal ensemble \cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.
79	
80	\paragraph{Metrics and statistical testing.}
81	The primary metric is \textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.
82	We report per-class F1 scores and 95\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).
83	For pairwise model comparisons (e.g., full features vs.\ ablated subsets), we use the \textbf{McNemar test} on disagreement tables.
84	For comparisons against detection baselines, we use \textbf{paired bootstrap} significance tests.
85	All reported $p$-values are two-sided.
86	We report six pairwise comparisons in \S\ref{sec:results-baselines}; applying Bonferroni correction ($\alpha_{\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.
87	Feature--depth correlations (\S\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.
88	
89	\paragraph{Baselines.}
90	We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
91	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.
92	
93	\paragraph{Length confound control.}
94	Since TTR and hapax\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.
95	We conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.
96	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "e45cb740-f052-4aee-837e-5944dcf0768a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe resulting dataset contains approximately 27{,}000 texts across all generators and depths.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs.\n    Although entropy\\_min shows near-zero marginal impact in leave-one-feature-out analysis ($\\Delta$F1\\,=\\,+0.01\\,pp), we retain it for completeness of the NLL summary statistics (mean, std, max, min) and because removing it does not improve performance;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n    The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ for the 7-feature ensemble.\nBaseline detectors (\\S\\ref{sec:results-baselines}) use the same XGBoost framework with $n\\_\\text{estimators}{=}100$ and $\\max\\_\\text{depth}{=}3$ to avoid overfitting their single-feature input.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\nWe evaluated two ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall ordinal ensemble \\cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\nWe report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
      "numLines": 96,
      "startLine": 1,
      "totalLines": 96
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01D12U3JS2FscmQHPdC43aeR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "71dcd000-4bd9-48c0-9a73-a8e0ac752fe3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 24 · 2026-05-16T03:05:38.595Z_

<details><summary>↩ Tool result · `toolu_01D12U3JS2FscmQHPdC43aeR`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate depth fingerprinting along four axes: cross-generator classification (\S\ref{sec:results-classification}), differential depth response of individual features (\S\ref{sec:results-differential}), comparison with existing detection baselines (\S\ref{sec:results-baselines}), and downstream utility for data curation (\S\ref{sec:results-downstream}).
5	
6	\subsection{Depth Classification Performance}
7	\label{sec:results-classification}
8	
9	Table~\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\,/\,gen-1\,/\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.
10	
11	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.789 (Table~\ref{tab:logo-results}). Because gen-0 seed texts are shared across generators (\S\ref{sec:generation}), the gen-0 class F1 (0.94) may be inflated; we therefore report a leak-free binary evaluation (gen-1 vs.\ gen-2+, F1\,=\,0.723) as the primary metric in \S\ref{sec:results-baselines}.
12	Per-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).
13	Per-class F1 varies by depth: gen-0\,=\,0.94, gen-2+\,=\,0.80, gen-1\,=\,0.64; the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.
14	
15	\paragraph{Cross-scale transfer.}
16	The six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\leq$2.8B training generators.
17	However, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\,=\,0.683 (CI [0.668, 0.694]), compared to 0.76--0.86 for $\leq$2.8B generators.
18	Text generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.
19	Notably, adding Qwen3-8B data \emph{improves} classification on the original five generators (+0.8\,pp to 0.810), indicating that cross-scale diversity benefits rather than dilutes the training signal.
20	A volume-matched control confirms this gain is driven by generator diversity, not data quantity: upsampling the 4-generator training set to match the 5-generator count yields only +0.05\,pp, while the remaining +0.78\,pp (94\% of the total improvement) is attributable to the additional generator's distributional diversity.
21	We note that this gap may narrow with scale-matched training data; our current dataset contains $\sim$1{,}000 samples per generator regardless of scale.
22	
23	\paragraph{Cross-family generalization.}
24	Leave-one-family-out (LOFO) evaluation---holding out an entire model family and training on the remaining two---yields macro-F1 of 0.772 (Pythia held out), 0.762 (OLMo held out), and 0.754 (Qwen held out), confirming that depth features transfer across architectural families with only modest degradation (average $\Delta$\,=\,$-$2.6\,pp vs.\ LOGO).
25	
26	\paragraph{Cross-model chains.}
27	Real-world contamination involves diverse generators at each depth step.
28	We construct cross-model chains where each generation step uses a randomly selected generator and evaluate under 5-fold stratified cross-validation.
29	Cross-model chains yield 3-class macro-F1\,=\,0.809 and binary F1\,=\,0.764, confirming that depth signal is maintained when chain provenance is heterogeneous.
30	Cross-model 3-class F1 (0.809) falls below the best single-model ceiling (Pythia-1B, 0.862) but demonstrates that depth fingerprinting remains effective in multi-generator scenarios that better approximate real-world web contamination.
31	
32	\paragraph{Length confound control.}
33	Text length correlates weakly with depth (Spearman $|\rho| < 0.14$).
34	Length-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\Delta$\,=\,+0.041), ruling out length as a confound (Appendix~\ref{app:length}).
35	
36	
37	\begin{table}[t]
38	\centering
39	\small
40	\begin{tabular}{llccc}
41	\toprule
42	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{Held-out F1} & \textbf{95\% CI} \\
43	\midrule
44	Pythia-1B       & Pythia & 1.0B & 0.856 & [0.843, 0.863] \\
45	Pythia-2.8B     & Pythia & 2.8B & 0.804 & [0.793, 0.813] \\
46	OLMo-2-1B      & OLMo   & 1.5B & 0.764 & [0.754, 0.776] \\
47	Qwen3-0.6B     & Qwen   & 0.6B & 0.824 & [0.813, 0.834] \\
48	Qwen3-1.7B     & Qwen   & 1.7B & 0.806 & [0.796, 0.817] \\
49	Qwen3-8B       & Qwen   & 8.2B & 0.683 & [0.668, 0.694] \\
50	\midrule
51	\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 & --- \\
52	\multicolumn{3}{l}{5-gen LOGO (excl.\ Qwen3-8B)} & 0.802 & --- \\
53	\bottomrule
54	\end{tabular}
55	\caption{Leave-one-generator-out macro-F1 with bootstrap 95\% confidence intervals ($n$\,=\,1000) for 3-class depth estimation using the 7-feature ensemble. Each row holds out one generator for testing and trains on the remaining five.}
56	\label{tab:logo-results}
57	\end{table}
58	
59	\paragraph{Ordinal regression comparison.}
60	To test whether the ordinal structure of the 3-class depth label provides additional discriminative power, we compare CORAL ordinal regression \cite{coral_ordinal} and Frank-Hall ordinal reduction \cite{frank_hall_ordinal} against the standard multiclass XGBoost classifier under the same LOGO protocol.
61	On 3-class F1, CORAL achieves 0.771, Frank-Hall 0.793, and XGBoost 0.789; all three confidence intervals overlap.
62	Binary F1 (gen-1 vs.\ gen-2+) similarly shows no separation: XGBoost 0.721, CORAL 0.728.
63	Concordance index---an ordinal-specific metric rewarding correct ranking---yields XGBoost 0.821, CORAL 0.810, Frank-Hall 0.825; again, all CIs overlap.
64	The standard multiclass classifier already captures the depth-discriminative signal, and explicitly encoding ordinal structure does not yield a measurable gain, likely because the 3-class granularity provides insufficient ordinal resolution for ranking-aware losses to exploit.
65	
66	
67	\subsection{Differential Depth Response}
68	\label{sec:results-differential}
69	
70	Features exhibit \emph{differential depth response}: central-tendency and diversity measures drift monotonically with depth, while distributional shape measures remain near-stationary.
71	This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution---the text becomes progressively more predictable (mean shifts), while the functional form of the distribution is preserved (shape is invariant).
72	
73	\begin{figure}[t]
74	\centering
75	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
76	\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show strong monotonic drift, while shape features (entropy std, tail decay) remain near-stationary.}
77	\label{fig:feature-drift}
78	\end{figure}
79	
80	Individual-level Spearman correlations with depth confirm the split (Figure~\ref{fig:feature-drift}):
81	drifting features show strong monotonic trends (hapax ratio $\rho = -0.558$, TTR $\rho = -0.542$, entropy mean $\rho = -0.475$),
82	while shape features show weak or negligible correlations (entropy std $|\rho| = 0.076$, tail decay $|\rho| = 0.089$).
83	
84	\paragraph{Feature complementarity.}
85	Table~\ref{tab:ablation} reports ablation results.
86	The full 7-feature set (F1\,=\,0.789) significantly outperforms both surface-only features (TTR, hapax\_ratio; F1\,=\,0.729) and reference-only features (entropy mean/std/max/min, tail\_decay; F1\,=\,0.745; McNemar $p \approx 0$).
87	Permutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).
88	Surface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.
89	
90	\paragraph{Cross-family reference models.}
91	To confirm that differential depth response is not an artifact of the Pythia-410M reference model, we recompute all features using two cross-family references: OLMo-2-1B (1.5B) and Qwen3-0.6B.
92	All three reference models achieve comparable LOGO F1: Pythia-410M\,=\,0.803, OLMo-2-1B\,=\,0.807, Qwen3-0.6B\,=\,0.816 (spread 0.013; Table~\ref{tab:cross-ref}).
93	Entropy drift direction is consistently negative across all reference models (Table~\ref{tab:cross-ref}), confirming that the differential depth response is a property of recursive generation, not of the specific reference model used.
94	
95	\input{table4}
96	
97	
98	\begin{table}[t]
99	\centering
100	\small
101	\begin{tabular}{lcc}
102	\toprule
103	\textbf{Feature set} & \textbf{LOGO F1} & \textbf{Top feature (importance)} \\
104	\midrule
105	Full (7 features)     & 0.789 & hapax\_ratio (0.269) \\
106	Surface only (2)      & 0.729 & hapax\_ratio (0.320) \\
107	Reference only (5)    & 0.745 & entropy\_mean (0.218) \\
108	\bottomrule
109	\end{tabular}
110	\caption{Feature ablation (6-gen LOGO). Full $>$ surface = reference confirms complementarity between surface diversity features and reference-model distributional features.}
111	\label{tab:ablation}
112	\end{table}
113	
114	Leave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\_max showing the largest marginal impact despite modest split frequency (Appendix~\ref{app:lofo}).
115	
116	
117	\subsection{Comparison with Detection Baselines}
118	\label{sec:results-baselines}
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.png}
123	\caption{LOGO macro-F1 with 95\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Per-generator held-out F1 varies more for single detectors than for the ensemble.}
124	\label{fig:baseline-ci}
125	\end{figure}
126	
127	We repurpose four existing detection scores as ordinal depth predictors by training the same classifier on each score as a single feature, using identical LOGO evaluation.
128	Because gen-0 seed texts are shared across generators (\S\ref{sec:generation}), 3-class LOGO evaluation creates a train--test overlap for the gen-0 class.
129	We therefore report both 3-class and binary (gen-1 vs.\ gen-2+) results; the binary metric is the primary measure of depth discrimination (Table~\ref{tab:baselines}).
130	
131	\begin{table}[t]
132	\centering
133	\small
134	\begin{tabular}{lccc}
135	\toprule
136	\textbf{Method} & \textbf{3-class F1} & \textbf{Binary F1} & \textbf{Per-gen std} \\
137	\midrule
138	7-feature ensemble    & 0.789 & \textbf{0.723} & 0.051 \\
139	4-det.\ + surface     & \textbf{0.805} & 0.724 & 0.049 \\
140	4-detector ens.\      & 0.796 & 0.712 & 0.044 \\
141	Avg-LogProb           & 0.737 & 0.712 & 0.044 \\
142	LD-Score              & 0.655 & 0.701 & 0.045 \\
143	FastDetectGPT         & 0.688 & 0.616 & 0.056 \\
144	Binoculars            & 0.417 & 0.524 & 0.022 \\
145	\bottomrule
146	\end{tabular}
147	\caption{Depth classification under unified 6-gen LOGO evaluation. \textbf{3-class}: gen-0/gen-1/gen-2+ (gen-0 samples shared across generators; see \S\ref{sec:generation}). \textbf{Binary}: gen-1 vs.\ gen-2+ only, eliminating the gen-0 train--test overlap. Per-gen std measures cross-generator consistency of the binary metric. The 7-feature ensemble is the strongest single-model method on both metrics and matches the best multi-detector ensemble on binary F1.}
148	\label{tab:baselines}
149	\end{table}
150	
151	The 7-feature ensemble achieves binary F1\,=\,0.723, outperforming every individual detection baseline: +1.1\,pp over Avg-LogProb, +2.2\,pp over LD-Score, +10.7\,pp over FastDetectGPT, and +19.9\,pp over Binoculars ($p < 0.001$ for all comparisons).
152	On the 3-class metric, the ensemble (0.789) similarly outperforms all single baselines, though the margins are inflated by the gen-0 overlap.
153	
154	\paragraph{Multi-detector ensembles.}
155	Combining all four detection scores into a 4-detector ensemble yields binary F1\,=\,0.712---below the 7-feature ensemble (0.723).
156	The multi-detector advantage seen in 3-class evaluation (0.796 vs.\ 0.789) is driven entirely by superior gen-0 classification; existing detectors excel at human-vs-machine discrimination but do not capture the finer depth signal between gen-1 and gen-2+.
157	Adding our surface features (TTR, hapax ratio) to the 4-detector ensemble raises binary F1 to 0.724, matching the 7-feature ensemble and confirming that surface diversity features capture signal complementary to detection scores.
158	Baseline results are stable across classifier hyperparameters: using the ensemble's settings ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$) instead of the default ($100$/$3$) changes baseline F1 by less than 0.002\,pp, confirming that performance differences reflect feature informativeness rather than classifier capacity.
159	
160	\paragraph{Binoculars: a non-transferable signal.}
161	Binoculars achieves near-random performance on the depth task (3-class F1\,=\,0.417, binary F1\,=\,0.524), confirming that cross-model perplexity ratios---the core signal in Binoculars---do not transfer to depth discrimination.
162	
163	
164	\subsection{Downstream Utility: A Negative Finding}
165	\label{sec:results-downstream}
166	
167	Can depth-aware data curation improve downstream language model quality?
168	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
169	
170	\begin{table}[t]
171	\centering
172	\small
173	\begin{tabular}{lrc}
174	\toprule
175	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
176	\midrule
177	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
178	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
179	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
180	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
181	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
182	\bottomrule
183	\end{tabular}
184	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
185	\label{tab:downstream}
186	\end{table}
187	
188	The results are unambiguous: data quantity dominates depth composition.
189	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
190	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
191	Cross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.
192	
193	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
194	
195	We report this negative finding transparently: depth fingerprinting is an effective \emph{diagnostic} tool for characterizing text provenance, not a \emph{curative} tool for data curation.
196	Knowing the generation depth of a document does not, by itself, make it more or less useful for training.
197	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "05f9e8fc-fe26-42e2-9976-537ac32cbf98",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate depth fingerprinting along four axes: cross-generator classification (\\S\\ref{sec:results-classification}), differential depth response of individual features (\\S\\ref{sec:results-differential}), comparison with existing detection baselines (\\S\\ref{sec:results-baselines}), and downstream utility for data curation (\\S\\ref{sec:results-downstream}).\n\n\\subsection{Depth Classification Performance}\n\\label{sec:results-classification}\n\nTable~\\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.\n\nThe 7-feature ensemble achieves 3-class LOGO F1\\,=\\,0.789 (Table~\\ref{tab:logo-results}). Because gen-0 seed texts are shared across generators (\\S\\ref{sec:generation}), the gen-0 class F1 (0.94) may be inflated; we therefore report a leak-free binary evaluation (gen-1 vs.\\ gen-2+, F1\\,=\\,0.723) as the primary metric in \\S\\ref{sec:results-baselines}.\nPer-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).\nPer-class F1 varies by depth: gen-0\\,=\\,0.94, gen-2+\\,=\\,0.80, gen-1\\,=\\,0.64; the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.\n\n\\paragraph{Cross-scale transfer.}\nThe six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\\leq$2.8B training generators.\nHowever, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\\,=\\,0.683 (CI [0.668, 0.694]), compared to 0.76--0.86 for $\\leq$2.8B generators.\nText generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.\nNotably, adding Qwen3-8B data \\emph{improves} classification on the original five generators (+0.8\\,pp to 0.810), indicating that cross-scale diversity benefits rather than dilutes the training signal.\nA volume-matched control confirms this gain is driven by generator diversity, not data quantity: upsampling the 4-generator training set to match the 5-generator count yields only +0.05\\,pp, while the remaining +0.78\\,pp (94\\% of the total improvement) is attributable to the additional generator's distributional diversity.\nWe note that this gap may narrow with scale-matched training data; our current dataset contains $\\sim$1{,}000 samples per generator regardless of scale.\n\n\\paragraph{Cross-family generalization.}\nLeave-one-family-out (LOFO) evaluation---holding out an entire model family and training on the remaining two---yields macro-F1 of 0.772 (Pythia held out), 0.762 (OLMo held out), and 0.754 (Qwen held out), confirming that depth features transfer across architectural families with only modest degradation (average $\\Delta$\\,=\\,$-$2.6\\,pp vs.\\ LOGO).\n\n\\paragraph{Cross-model chains.}\nReal-world contamination involves diverse generators at each depth step.\nWe construct cross-model chains where each generation step uses a randomly selected generator and evaluate under 5-fold stratified cross-validation.\nCross-model chains yield 3-class macro-F1\\,=\\,0.809 and binary F1\\,=\\,0.764, confirming that depth signal is maintained when chain provenance is heterogeneous.\nCross-model 3-class F1 (0.809) falls below the best single-model ceiling (Pythia-1B, 0.862) but demonstrates that depth fingerprinting remains effective in multi-generator scenarios that better approximate real-world web contamination.\n\n\\paragraph{Length confound control.}\nText length correlates weakly with depth (Spearman $|\\rho| < 0.14$).\nLength-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\\Delta$\\,=\\,+0.041), ruling out length as a confound (Appendix~\\ref{app:length}).\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Family} & \\textbf{Params} & \\textbf{Held-out F1} & \\textbf{95\\% CI} \\\\\n\\midrule\nPythia-1B       & Pythia & 1.0B & 0.856 & [0.843, 0.863] \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 & [0.793, 0.813] \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.764 & [0.754, 0.776] \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.824 & [0.813, 0.834] \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.806 & [0.796, 0.817] \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.683 & [0.668, 0.694] \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 & --- \\\\\n\\multicolumn{3}{l}{5-gen LOGO (excl.\\ Qwen3-8B)} & 0.802 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-generator-out macro-F1 with bootstrap 95\\% confidence intervals ($n$\\,=\\,1000) for 3-class depth estimation using the 7-feature ensemble. Each row holds out one generator for testing and trains on the remaining five.}\n\\label{tab:logo-results}\n\\end{table}\n\n\\paragraph{Ordinal regression comparison.}\nTo test whether the ordinal structure of the 3-class depth label provides additional discriminative power, we compare CORAL ordinal regression \\cite{coral_ordinal} and Frank-Hall ordinal reduction \\cite{frank_hall_ordinal} against the standard multiclass XGBoost classifier under the same LOGO protocol.\nOn 3-class F1, CORAL achieves 0.771, Frank-Hall 0.793, and XGBoost 0.789; all three confidence intervals overlap.\nBinary F1 (gen-1 vs.\\ gen-2+) similarly shows no separation: XGBoost 0.721, CORAL 0.728.\nConcordance index---an ordinal-specific metric rewarding correct ranking---yields XGBoost 0.821, CORAL 0.810, Frank-Hall 0.825; again, all CIs overlap.\nThe standard multiclass classifier already captures the depth-discriminative signal, and explicitly encoding ordinal structure does not yield a measurable gain, likely because the 3-class granularity provides insufficient ordinal resolution for ranking-aware losses to exploit.\n\n\n\\subsection{Differential Depth Response}\n\\label{sec:results-differential}\n\nFeatures exhibit \\emph{differential depth response}: central-tendency and diversity measures drift monotonically with depth, while distributional shape measures remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution---the text becomes progressively more predictable (mean shifts), while the functional form of the distribution is preserved (shape is invariant).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show strong monotonic drift, while shape features (entropy std, tail decay) remain near-stationary.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nIndividual-level Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):\ndrifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.542$, entropy mean $\\rho = -0.475$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.089$).\n\n\\paragraph{Feature complementarity.}\nTable~\\ref{tab:ablation} reports ablation results.\nThe full 7-feature set (F1\\,=\\,0.789) significantly outperforms both surface-only features (TTR, hapax\\_ratio; F1\\,=\\,0.729) and reference-only features (entropy mean/std/max/min, tail\\_decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).\nSurface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.\n\n\\paragraph{Cross-family reference models.}\nTo confirm that differential depth response is not an artifact of the Pythia-410M reference model, we recompute all features using two cross-family references: OLMo-2-1B (1.5B) and Qwen3-0.6B.\nAll three reference models achieve comparable LOGO F1: Pythia-410M\\,=\\,0.803, OLMo-2-1B\\,=\\,0.807, Qwen3-0.6B\\,=\\,0.816 (spread 0.013; Table~\\ref{tab:cross-ref}).\nEntropy drift direction is consistently negative across all reference models (Table~\\ref{tab:cross-ref}), confirming that the differential depth response is a property of recursive generation, not of the specific reference model used.\n\n\\input{table4}\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature set} & \\textbf{LOGO F1} & \\textbf{Top feature (importance)} \\\\\n\\midrule\nFull (7 features)     & 0.789 & hapax\\_ratio (0.269) \\\\\nSurface only (2)      & 0.729 & hapax\\_ratio (0.320) \\\\\nReference only (5)    & 0.745 & entropy\\_mean (0.218) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (6-gen LOGO). Full $>$ surface = reference confirms complementarity between surface diversity features and reference-model distributional features.}\n\\label{tab:ablation}\n\\end{table}\n\nLeave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\\_max showing the largest marginal impact despite modest split frequency (Appendix~\\ref{app:lofo}).\n\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:results-baselines}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.png}\n\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Per-generator held-out F1 varies more for single detectors than for the ensemble.}\n\\label{fig:baseline-ci}\n\\end{figure}\n\nWe repurpose four existing detection scores as ordinal depth predictors by training the same classifier on each score as a single feature, using identical LOGO evaluation.\nBecause gen-0 seed texts are shared across generators (\\S\\ref{sec:generation}), 3-class LOGO evaluation creates a train--test overlap for the gen-0 class.\nWe therefore report both 3-class and binary (gen-1 vs.\\ gen-2+) results; the binary metric is the primary measure of depth discrimination (Table~\\ref{tab:baselines}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{3-class F1} & \\textbf{Binary F1} & \\textbf{Per-gen std} \\\\\n\\midrule\n7-feature ensemble    & 0.789 & \\textbf{0.723} & 0.051 \\\\\n4-det.\\ + surface     & \\textbf{0.805} & 0.724 & 0.049 \\\\\n4-detector ens.\\      & 0.796 & 0.712 & 0.044 \\\\\nAvg-LogProb           & 0.737 & 0.712 & 0.044 \\\\\nLD-Score              & 0.655 & 0.701 & 0.045 \\\\\nFastDetectGPT         & 0.688 & 0.616 & 0.056 \\\\\nBinoculars            & 0.417 & 0.524 & 0.022 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Depth classification under unified 6-gen LOGO evaluation. \\textbf{3-class}: gen-0/gen-1/gen-2+ (gen-0 samples shared across generators; see \\S\\ref{sec:generation}). \\textbf{Binary}: gen-1 vs.\\ gen-2+ only, eliminating the gen-0 train--test overlap. Per-gen std measures cross-generator consistency of the binary metric. The 7-feature ensemble is the strongest single-model method on both metrics and matches the best multi-detector ensemble on binary F1.}\n\\label{tab:baselines}\n\\end{table}\n\nThe 7-feature ensemble achieves binary F1\\,=\\,0.723, outperforming every individual detection baseline: +1.1\\,pp over Avg-LogProb, +2.2\\,pp over LD-Score, +10.7\\,pp over FastDetectGPT, and +19.9\\,pp over Binoculars ($p < 0.001$ for all comparisons).\nOn the 3-class metric, the ensemble (0.789) similarly outperforms all single baselines, though the margins are inflated by the gen-0 overlap.\n\n\\paragraph{Multi-detector ensembles.}\nCombining all four detection scores into a 4-detector ensemble yields binary F1\\,=\\,0.712---below the 7-feature ensemble (0.723).\nThe multi-detector advantage seen in 3-class evaluation (0.796 vs.\\ 0.789) is driven entirely by superior gen-0 classification; existing detectors excel at human-vs-machine discrimination but do not capture the finer depth signal between gen-1 and gen-2+.\nAdding our surface features (TTR, hapax ratio) to the 4-detector ensemble raises binary F1 to 0.724, matching the 7-feature ensemble and confirming that surface diversity features capture signal complementary to detection scores.\nBaseline results are stable across classifier hyperparameters: using the ensemble's settings ($n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$) instead of the default ($100$/$3$) changes baseline F1 by less than 0.002\\,pp, confirming that performance differences reflect feature informativeness rather than classifier capacity.\n\n\\paragraph{Binoculars: a non-transferable signal.}\nBinoculars achieves near-random performance on the depth task (3-class F1\\,=\\,0.417, binary F1\\,=\\,0.524), confirming that cross-model perplexity ratios---the core signal in Binoculars---do not transfer to depth discrimination.\n\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:results-downstream}\n\nCan depth-aware data curation improve downstream language model quality?\nWe fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{Test PPL} \\\\\n\\midrule\nAll depths            & 12{,}299 & 2.335 $\\pm$ 0.000 \\\\\nSize-matched (random) & 3{,}951  & 2.367 $\\pm$ 0.000 \\\\\nDepth 0--1 only       & 3{,}951  & 2.387 $\\pm$ 0.001 \\\\\nBinary-filtered       & 3{,}951  & 2.389 $\\pm$ 0.000 \\\\\nDepth 0 only          & 797      & 2.681 $\\pm$ 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}\n\\label{tab:downstream}\n\\end{table}\n\nThe results are unambiguous: data quantity dominates depth composition.\nTraining on all 12{,}299 samples yields the lowest perplexity (2.335).\nAt equal sample count ($n$\\,=\\,3{,}951), random subsampling (2.367) \\emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).\nCross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.\n\nRestricting training to human-only text (depth 0, $n$\\,=\\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\\times$ reduction in data volume rather than depth composition per se.\n\nWe report this negative finding transparently: depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data curation.\nKnowing the generation depth of a document does not, by itself, make it more or less useful for training.\n",
      "numLines": 197,
      "startLine": 1,
      "totalLines": 197
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01NtsNctefnqSkPxznmCvGKS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "2483fc2d-362f-465e-aa6b-817d720bfe20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 26 · 2026-05-16T03:05:39.116Z_

<details><summary>↩ Tool result · `toolu_01NtsNctefnqSkPxznmCvGKS`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why are shape features stationary?}
5	Distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\S\ref{sec:results-differential}).
6	One \emph{speculative} explanation is that shape is primarily determined by the sampling mechanism (temperature, top-$p$ truncation) and the model's architecture-level output distribution, both of which are fixed across generation steps.
7	Recursive generation shifts \emph{what} the model talks about---steering toward higher-probability vocabulary regions---but does not alter \emph{how} the model distributes probability mass around its predictions.
8	If this account is correct, shape features should remain stationary even at much greater depths and across different prompt types, while level features should continue to drift until reaching a fixed point.
9	Sampling ablation supports this account: depth signal is robust to moderate sampling variation (F1 range ${\leq}0.3$\,pp for $t \in [0.5, 0.7]$) but degrades at extreme temperatures ($t = 1.0$, $-6$\,pp), consistent with shape features being determined by the sampling mechanism (Appendix~\ref{app:sampling-sensitivity}).
10	We flag this as a hypothesis for future investigation, not a conclusion supported by our current experiments.
11	
12	\paragraph{Relation to OOD detection.}
13	Reference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \cite{detectgpt}, GLTR \cite{gltr}, and Binoculars \cite{binoculars}.
14	Our contribution is not these features per se, but the \emph{ordinal} depth formulation and the empirical finding that they exhibit differential depth response under recursive generation.
15	This connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \cite{ood_baseline}.
16	Recursive generation chains produce an analogous effect---progressive drift away from human text that manifests primarily as a location shift in the NLL distribution.
17	
18	\paragraph{Practical implications.}
19	The differential depth response enables provenance characterization of text corpora.
20	Rather than binary keep-or-discard filtering, practitioners can use depth estimates to understand the composition of their data.
21	Whether this understanding translates to improved curation outcomes remains an open question (\S\ref{sec:results-downstream}).
22	Cross-model chain evaluation (\S\ref{sec:results-classification}) confirms that depth signal persists even when chains involve heterogeneous generators, supporting applicability to realistic web-contamination scenarios.
23	Three-class granularity separates human text from moderate-drift first-generation content and from deeper text with compounding distributional shift---the distinction most relevant to provenance analysis.
24	\paragraph{Granularity ceiling.}
25	Extending to 5-class depth estimation (gen-0 through gen-4) reduces LOGO macro F1 from 0.789 to 0.501, a drop of 0.288 (Appendix~\ref{app:finer-depth}).
26	The degradation is concentrated in middle depths: gen-2 and gen-3 are effectively inseparable (per-class F1 of 0.268 and 0.259, respectively), with adjacent-depth confusions accounting for the majority of errors.
27	Alternative classifiers---random forest (0.476), logistic regression (0.447), Frank-Hall ordinal reduction (0.451)---all perform comparably, confirming that the bottleneck is feature separability, not classifier choice.
28	These results establish three classes as the practical granularity ceiling for the current feature set.
29	Unlike paraphrastic chains, which converge within ${\sim}$3 steps \cite{broken_telephone}, non-paraphrastic continuation chains retain some signal at gen-4 (F1\,=\,0.423), but the gen-2/gen-3 boundary remains unresolvable with surface and entropy features alone.
30	End-to-end fine-tuning (QLoRA on Qwen3-0.6B) raises the 3-class ceiling to F1\,=\,0.905 (+11.6\,pp over handcrafted features; Appendix~\ref{app:qlora}), confirming that raw embeddings contain exploitable depth signal beyond summary statistics.
31	
32	\paragraph{Paraphrastic contamination control.}
33	Initial paraphrastic chain experiments exhibited reversed entropy--depth correlations ($\rho = +0.394$), raising concern that depth signal might be confounded by data contamination from continuation-style seeds leaking into paraphrastic chains.
34	After removing contaminated samples, paraphrastic entropy correlations align with continuation chains ($\rho = -0.533$), confirming the reversal was an artifact.
35	On clean data, paraphrastic chains achieve binary F1\,=\,0.671 (vs.\ 0.749 for continuation), consistent with the faster convergence predicted by \citet{broken_telephone}.
36	Cross-transfer remains effective: a classifier trained on paraphrastic chains achieves binary F1\,=\,0.770 on continuation data, and the reverse transfer yields 0.743, indicating that depth features capture a shared distributional signal across chain types despite differing convergence rates.
37	
38	\paragraph{Robustness to post-generation editing.}
39	Depth features degrade gracefully under simulated human editing: random token replacement at 20\% reduces 3-class F1 by only 6.0\,pp while binary F1 (gen-1 vs.\ gen-2+) remains nearly unchanged ($\Delta \leq 0.8$\,pp).
40	LLM rephrasing presents a different challenge---3-class degradation is modest ($-3.4$\,pp), but binary F1 drops 6.3\,pp, indicating that systematic distributional manipulation erodes depth signal more effectively than surface noise (Appendix~\ref{app:human-edit}).
41	This asymmetry has practical implications: depth fingerprinting is robust to casual editing but more vulnerable in settings where LLM-assisted rewriting is prevalent.
42	
43	\paragraph{Information value of the negative finding.}
44	Depth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\S\ref{sec:results-downstream}).
45	This negative result carries positive information value: it rules out depth-based filtering as a data selection strategy, sparing practitioners from building depth-conditional pipelines that would not yield quality gains.
46	The dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \cite{self_consuming_mad}.
47	
48	\paragraph{Connection to model collapse.}
49	Our results relate to, but are distinct from, model collapse \cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.
50	Model collapse describes distributional degradation when models are \emph{retrained} on their own outputs across generations.
51	We observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \emph{inference chains} without any parameter updates.
52	This suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.
53	The shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.
54	
55	\paragraph{Topic drift as mediator, not confounder.}
56	Recursive generation narrows topic diversity: cosine similarity between adjacent depths increases monotonically from 0.62 (depth 0$\to$1) to 0.86 (depth 3$\to$4), consistent with regression toward high-probability modes.
57	However, topic narrowing accounts for less than 9\% of feature variance (maximum: entropy\_mean, $\rho = -0.286$, $R^2 = 0.082$).
58	Shape features are near-independent of semantic drift (tail\_decay $|\rho| = 0.068$, $R^2 = 0.005$).
59	Topic drift is best understood as a \emph{mediator}---one mechanism through which depth manifests---rather than a confound that invalidates depth features.
60	The depth signal primarily reflects sampling-induced distributional compression, not topic narrowing per se.
61	
62	\paragraph{Depth features vs.\ multi-detector ensembles.}
63	In 3-class evaluation, multi-detector ensembles achieve marginally higher F1 (0.805 with surface features added vs.\ 0.789).
64	However, this advantage is driven entirely by gen-0 classification, where detection scores excel at human-vs-machine discrimination.
65	In the leak-free binary evaluation (gen-1 vs.\ gen-2+), the 7-feature ensemble matches the best multi-detector configuration (0.723 vs.\ 0.724), demonstrating that depth features capture the gen-1/gen-2+ distinction as effectively as four detection pipelines combined.
66	Depth features additionally offer interpretability---they reveal the differential depth response pattern---and computational efficiency, requiring only a single lightweight reference model.
67	
68	\paragraph{Reference-model independence.}
69	The depth signal is not an artifact of reference-model choice.
70	Overall LOGO F1 varies by only 0.013 across three cross-family reference models (0.803--0.816; Table~\ref{tab:cross-ref}), and entropy drift direction is consistently negative for all three, confirming that the differential depth response is a property of recursive generation itself.
71	At the per-generator level, Pythia-1B achieves the highest held-out F1 (0.856) despite using a same-family reference model (Pythia-410M); cross-family references yield nearly identical Pythia-1B F1 (0.845--0.848), ruling out family bias as an explanation for its high detectability.
72	
73	\paragraph{Instruct tuning degrades depth signal through multiple mechanisms.}
74	Preliminary experiments with instruction-tuned models show substantially weaker depth fingerprints: OLMo-2-1B-Instruct achieves 3-class LOGO F1\,=\,0.338 (vs.\ 0.764 for base OLMo-2-1B), and Qwen3-0.6B with chat template yields F1\,=\,0.667 (vs.\ 0.816 for the base model under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\ref{tab:logo-results}).
75	Length-controlled analysis reveals a consistent pattern.
76	Entropy-based features reverse sign across all three instruct models (partial $\rho$ = +0.103, +0.161, +0.364 for Qwen3-0.6B, Qwen3-1.7B, and OLMo-Instruct respectively), though the interpretation is complicated by severe length confounds.
77	Qwen3-0.6B exhibits the weakest residual (+0.103), and a stricter length-matched robustness check yields near-zero correlations (all length-matched $|\rho| < 0.02$), consistent with the depth--feature association being largely mediated by the extreme length disparity across depths (252 vs.\ 23 tokens for gen-0 vs.\ gen-2+).
78	Qwen3-1.7B partial correlations are also substantially reduced after length matching (surface features by 53--60\%, entropy by 91\%), and gen-1 vs.\ gen-2+ binary classification is near chance for both models (F1 $\approx$ 0.5), indicating that depth signal is not operationally detectable in instruct chains.
79	OLMo-Instruct's substantially larger residual ($+0.364$) likely reflects differences in alignment recipe rather than parameter count alone.
80	Surface features (TTR, hapax ratio) show model-dependent behavior: Qwen3-1.7B retains weakly positive partial correlations with depth (TTR partial $\rho$ = +0.130; hapax partial $\rho$ = +0.166), while OLMo-Instruct exhibits negative correlations similar to base models (TTR partial $\rho = -0.241$; hapax partial $\rho = -0.198$).
81	This divergence cautions against treating surface feature reversal as a universal consequence of instruction tuning; the effect is architecture- or training-recipe-dependent.
82	
83	OLMo-Instruct presents a paradox: it exhibits the strongest entropy--depth partial correlation (+0.364) yet the worst classification performance (LOGO F1\,=\,0.338).
84	A likely explanation is that its surface features retain base-model polarity (negative partial $\rho$) while entropy reverses to positive, creating contradictory signals for a classifier trained on base-model patterns---where entropy and surface features are jointly negative at greater depths.
85	OLMo-Instruct breaks this joint structure, and the resulting signal conflict may account for the classification collapse.
86	Disentangling these mechanisms across a broader set of instruct models is a priority for future work; the current findings justify restricting our scope to base models where such confounds are minimal.
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "a25ef33a-892b-4879-9dc6-f3adc41b1d58",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why are shape features stationary?}\nDistributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\\S\\ref{sec:results-differential}).\nOne \\emph{speculative} explanation is that shape is primarily determined by the sampling mechanism (temperature, top-$p$ truncation) and the model's architecture-level output distribution, both of which are fixed across generation steps.\nRecursive generation shifts \\emph{what} the model talks about---steering toward higher-probability vocabulary regions---but does not alter \\emph{how} the model distributes probability mass around its predictions.\nIf this account is correct, shape features should remain stationary even at much greater depths and across different prompt types, while level features should continue to drift until reaching a fixed point.\nSampling ablation supports this account: depth signal is robust to moderate sampling variation (F1 range ${\\leq}0.3$\\,pp for $t \\in [0.5, 0.7]$) but degrades at extreme temperatures ($t = 1.0$, $-6$\\,pp), consistent with shape features being determined by the sampling mechanism (Appendix~\\ref{app:sampling-sensitivity}).\nWe flag this as a hypothesis for future investigation, not a conclusion supported by our current experiments.\n\n\\paragraph{Relation to OOD detection.}\nReference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \\cite{detectgpt}, GLTR \\cite{gltr}, and Binoculars \\cite{binoculars}.\nOur contribution is not these features per se, but the \\emph{ordinal} depth formulation and the empirical finding that they exhibit differential depth response under recursive generation.\nThis connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \\cite{ood_baseline}.\nRecursive generation chains produce an analogous effect---progressive drift away from human text that manifests primarily as a location shift in the NLL distribution.\n\n\\paragraph{Practical implications.}\nThe differential depth response enables provenance characterization of text corpora.\nRather than binary keep-or-discard filtering, practitioners can use depth estimates to understand the composition of their data.\nWhether this understanding translates to improved curation outcomes remains an open question (\\S\\ref{sec:results-downstream}).\nCross-model chain evaluation (\\S\\ref{sec:results-classification}) confirms that depth signal persists even when chains involve heterogeneous generators, supporting applicability to realistic web-contamination scenarios.\nThree-class granularity separates human text from moderate-drift first-generation content and from deeper text with compounding distributional shift---the distinction most relevant to provenance analysis.\n\\paragraph{Granularity ceiling.}\nExtending to 5-class depth estimation (gen-0 through gen-4) reduces LOGO macro F1 from 0.789 to 0.501, a drop of 0.288 (Appendix~\\ref{app:finer-depth}).\nThe degradation is concentrated in middle depths: gen-2 and gen-3 are effectively inseparable (per-class F1 of 0.268 and 0.259, respectively), with adjacent-depth confusions accounting for the majority of errors.\nAlternative classifiers---random forest (0.476), logistic regression (0.447), Frank-Hall ordinal reduction (0.451)---all perform comparably, confirming that the bottleneck is feature separability, not classifier choice.\nThese results establish three classes as the practical granularity ceiling for the current feature set.\nUnlike paraphrastic chains, which converge within ${\\sim}$3 steps \\cite{broken_telephone}, non-paraphrastic continuation chains retain some signal at gen-4 (F1\\,=\\,0.423), but the gen-2/gen-3 boundary remains unresolvable with surface and entropy features alone.\nEnd-to-end fine-tuning (QLoRA on Qwen3-0.6B) raises the 3-class ceiling to F1\\,=\\,0.905 (+11.6\\,pp over handcrafted features; Appendix~\\ref{app:qlora}), confirming that raw embeddings contain exploitable depth signal beyond summary statistics.\n\n\\paragraph{Paraphrastic contamination control.}\nInitial paraphrastic chain experiments exhibited reversed entropy--depth correlations ($\\rho = +0.394$), raising concern that depth signal might be confounded by data contamination from continuation-style seeds leaking into paraphrastic chains.\nAfter removing contaminated samples, paraphrastic entropy correlations align with continuation chains ($\\rho = -0.533$), confirming the reversal was an artifact.\nOn clean data, paraphrastic chains achieve binary F1\\,=\\,0.671 (vs.\\ 0.749 for continuation), consistent with the faster convergence predicted by \\citet{broken_telephone}.\nCross-transfer remains effective: a classifier trained on paraphrastic chains achieves binary F1\\,=\\,0.770 on continuation data, and the reverse transfer yields 0.743, indicating that depth features capture a shared distributional signal across chain types despite differing convergence rates.\n\n\\paragraph{Robustness to post-generation editing.}\nDepth features degrade gracefully under simulated human editing: random token replacement at 20\\% reduces 3-class F1 by only 6.0\\,pp while binary F1 (gen-1 vs.\\ gen-2+) remains nearly unchanged ($\\Delta \\leq 0.8$\\,pp).\nLLM rephrasing presents a different challenge---3-class degradation is modest ($-3.4$\\,pp), but binary F1 drops 6.3\\,pp, indicating that systematic distributional manipulation erodes depth signal more effectively than surface noise (Appendix~\\ref{app:human-edit}).\nThis asymmetry has practical implications: depth fingerprinting is robust to casual editing but more vulnerable in settings where LLM-assisted rewriting is prevalent.\n\n\\paragraph{Information value of the negative finding.}\nDepth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\\S\\ref{sec:results-downstream}).\nThis negative result carries positive information value: it rules out depth-based filtering as a data selection strategy, sparing practitioners from building depth-conditional pipelines that would not yield quality gains.\nThe dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \\cite{self_consuming_mad}.\n\n\\paragraph{Connection to model collapse.}\nOur results relate to, but are distinct from, model collapse \\cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.\nModel collapse describes distributional degradation when models are \\emph{retrained} on their own outputs across generations.\nWe observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \\emph{inference chains} without any parameter updates.\nThis suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.\nThe shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.\n\n\\paragraph{Topic drift as mediator, not confounder.}\nRecursive generation narrows topic diversity: cosine similarity between adjacent depths increases monotonically from 0.62 (depth 0$\\to$1) to 0.86 (depth 3$\\to$4), consistent with regression toward high-probability modes.\nHowever, topic narrowing accounts for less than 9\\% of feature variance (maximum: entropy\\_mean, $\\rho = -0.286$, $R^2 = 0.082$).\nShape features are near-independent of semantic drift (tail\\_decay $|\\rho| = 0.068$, $R^2 = 0.005$).\nTopic drift is best understood as a \\emph{mediator}---one mechanism through which depth manifests---rather than a confound that invalidates depth features.\nThe depth signal primarily reflects sampling-induced distributional compression, not topic narrowing per se.\n\n\\paragraph{Depth features vs.\\ multi-detector ensembles.}\nIn 3-class evaluation, multi-detector ensembles achieve marginally higher F1 (0.805 with surface features added vs.\\ 0.789).\nHowever, this advantage is driven entirely by gen-0 classification, where detection scores excel at human-vs-machine discrimination.\nIn the leak-free binary evaluation (gen-1 vs.\\ gen-2+), the 7-feature ensemble matches the best multi-detector configuration (0.723 vs.\\ 0.724), demonstrating that depth features capture the gen-1/gen-2+ distinction as effectively as four detection pipelines combined.\nDepth features additionally offer interpretability---they reveal the differential depth response pattern---and computational efficiency, requiring only a single lightweight reference model.\n\n\\paragraph{Reference-model independence.}\nThe depth signal is not an artifact of reference-model choice.\nOverall LOGO F1 varies by only 0.013 across three cross-family reference models (0.803--0.816; Table~\\ref{tab:cross-ref}), and entropy drift direction is consistently negative for all three, confirming that the differential depth response is a property of recursive generation itself.\nAt the per-generator level, Pythia-1B achieves the highest held-out F1 (0.856) despite using a same-family reference model (Pythia-410M); cross-family references yield nearly identical Pythia-1B F1 (0.845--0.848), ruling out family bias as an explanation for its high detectability.\n\n\\paragraph{Instruct tuning degrades depth signal through multiple mechanisms.}\nPreliminary experiments with instruction-tuned models show substantially weaker depth fingerprints: OLMo-2-1B-Instruct achieves 3-class LOGO F1\\,=\\,0.338 (vs.\\ 0.764 for base OLMo-2-1B), and Qwen3-0.6B with chat template yields F1\\,=\\,0.667 (vs.\\ 0.816 for the base model under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\\ref{tab:logo-results}).\nLength-controlled analysis reveals a consistent pattern.\nEntropy-based features reverse sign across all three instruct models (partial $\\rho$ = +0.103, +0.161, +0.364 for Qwen3-0.6B, Qwen3-1.7B, and OLMo-Instruct respectively), though the interpretation is complicated by severe length confounds.\nQwen3-0.6B exhibits the weakest residual (+0.103), and a stricter length-matched robustness check yields near-zero correlations (all length-matched $|\\rho| < 0.02$), consistent with the depth--feature association being largely mediated by the extreme length disparity across depths (252 vs.\\ 23 tokens for gen-0 vs.\\ gen-2+).\nQwen3-1.7B partial correlations are also substantially reduced after length matching (surface features by 53--60\\%, entropy by 91\\%), and gen-1 vs.\\ gen-2+ binary classification is near chance for both models (F1 $\\approx$ 0.5), indicating that depth signal is not operationally detectable in instruct chains.\nOLMo-Instruct's substantially larger residual ($+0.364$) likely reflects differences in alignment recipe rather than parameter count alone.\nSurface features (TTR, hapax ratio) show model-dependent behavior: Qwen3-1.7B retains weakly positive partial correlations with depth (TTR partial $\\rho$ = +0.130; hapax partial $\\rho$ = +0.166), while OLMo-Instruct exhibits negative correlations similar to base models (TTR partial $\\rho = -0.241$; hapax partial $\\rho = -0.198$).\nThis divergence cautions against treating surface feature reversal as a universal consequence of instruction tuning; the effect is architecture- or training-recipe-dependent.\n\nOLMo-Instruct presents a paradox: it exhibits the strongest entropy--depth partial correlation (+0.364) yet the worst classification performance (LOGO F1\\,=\\,0.338).\nA likely explanation is that its surface features retain base-model polarity (negative partial $\\rho$) while entropy reverses to positive, creating contradictory signals for a classifier trained on base-model patterns---where entropy and surface features are jointly negative at greater depths.\nOLMo-Instruct breaks this joint structure, and the resulting signal conflict may account for the classification collapse.\nDisentangling these mechanisms across a broader set of instruct models is a priority for future work; the current findings justify restricting our scope to base models where such confounds are minimal.\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_015U1SuYtfj7Y5oMJMdYANgK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "8ff59f4c-3952-41c9-be33-6f515df8a0e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 28 · 2026-05-16T03:05:39.416Z_

<details><summary>↩ Tool result · `toolu_015U1SuYtfj7Y5oMJMdYANgK`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced ordinal generation depth estimation as a task beyond binary synthetic text detection, providing a framework for characterizing the provenance of web-crawled text at finer granularity.
5	Across six generators from three model families (0.6B--8.2B parameters), we documented differential depth response: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble combining both feature types achieves binary macro-F1 of 0.723 (95\% CI: [0.717, 0.729]) for leak-free depth discrimination across six base-model generators, with per-generator std of 0.051.
7	Cross-model chains---where each generation step uses a different generator---yield comparable performance (3-class F1\,=\,0.809, binary F1\,=\,0.764), confirming that depth signal persists under the generator heterogeneity typical of real-world contamination.
8	We also reported that depth-aware data curation does not improve downstream language model quality over random subsampling, establishing that, in our experimental setting, depth fingerprinting functions as a diagnostic tool for provenance characterization rather than a curative tool for data selection.
9	
10	Future work should extend evaluation to instruction-tuned and RLHF models, frontier-scale generators (70B+), and multilingual settings.
11	All code, data, and trained models will be released upon publication to facilitate reproducibility.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "97c401e2-4652-45a9-b25a-4e23dd23d36c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced ordinal generation depth estimation as a task beyond binary synthetic text detection, providing a framework for characterizing the provenance of web-crawled text at finer granularity.\nAcross six generators from three model families (0.6B--8.2B parameters), we documented differential depth response: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.\nA 7-feature ensemble combining both feature types achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination across six base-model generators, with per-generator std of 0.051.\nCross-model chains---where each generation step uses a different generator---yield comparable performance (3-class F1\\,=\\,0.809, binary F1\\,=\\,0.764), confirming that depth signal persists under the generator heterogeneity typical of real-world contamination.\nWe also reported that depth-aware data curation does not improve downstream language model quality over random subsampling, establishing that, in our experimental setting, depth fingerprinting functions as a diagnostic tool for provenance characterization rather than a curative tool for data selection.\n\nFuture work should extend evaluation to instruction-tuned and RLHF models, frontier-scale generators (70B+), and multilingual settings.\nAll code, data, and trained models will be released upon publication to facilitate reproducibility.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_017G35Vm4VY26pThUkoneUX2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "6bb4d533-251e-49ac-84c5-acd5cb503573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 30 · 2026-05-16T03:05:40.374Z_

<details><summary>↩ Tool result · `toolu_017G35Vm4VY26pThUkoneUX2`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All six generators are base (pretrained) models.
5	Web text is predominantly produced by instruction-tuned and RLHF-aligned models, whose generation distributions differ from base model continuations.
6	Preliminary instruct experiments show substantial depth-signal degradation: OLMo-2-1B-Instruct drops to 3-class LOGO F1\,=\,0.338 (vs.\ 0.764 for base OLMo-2-1B) and Qwen3-0.6B with chat template to F1\,=\,0.667 (vs.\ 0.816 base under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\ref{tab:logo-results}).
7	Length-controlled analysis reveals that the effect of instruct tuning on surface features is model-dependent: Qwen models retain weakly positive TTR and hapax partial correlations with depth, while OLMo-Instruct exhibits negative correlations similar to base models.
8	Entropy-based depth signals show reversed partial correlations across all three instruct models (partial $\rho$ ranging from +0.103 to +0.364), though length-matched analysis for the smallest model yields near-zero correlations ($|\rho| < 0.02$) and binary classification is near chance (F1 $\approx$ 0.5), leaving the interpretation of these residuals ambiguous.
9	Disentangling architecture-dependent surface effects from the residual entropy sign change in instruct-tuned generation is a critical direction for future work.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale, but cross-scale classifier transfer incurs a moderate gap (held-out F1\,=\,0.683 vs.\ 0.76--0.86 for $\leq$2.8B generators).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	We evaluate three prompt types (continuation, elaboration, rewriting; Appendix~\ref{app:prompt-type}) but all share the same Pythia-2.8B generator.
16	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms the depth signal generalizes, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
17	
18	Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm that depth signal persists under generator heterogeneity (3-class F1\,=\,0.809, binary F1\,=\,0.764), though the six generators tested represent a controlled laboratory setting rather than the full diversity of web-scale contamination.
19	Simulated human editing (\S\ref{sec:discussion}) suggests graceful degradation under casual editing, but the gap between simulated token replacement and real-world human post-processing remains untested.
20	
21	The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\S\ref{sec:results-differential}) suggest the phenomenon is not reference-specific.
22	All seed texts are English Wikipedia excerpts; generalization to other languages and domains remains untested.
23	
24	The negative downstream result (\S\ref{sec:results-downstream}) is evaluated on causal language modeling only.
25	Other downstream tasks (classification, summarization, instruction following) may respond differently to depth composition.
26	
27	Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \in [0.5, 0.7]$, F1 range ${\leq}0.3$\,pp) but substantial degradation at $t{=}1.0$ ($-6$\,pp), indicating that depth fingerprinting assumes standard decoding regimes.
28	
29	We use 3-class granularity (gen-0\,/\,gen-1\,/\,gen-2+). A 5-class evaluation (Appendix~\ref{app:finer-depth}) yields LOGO F1\,$\approx$\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "bdd0b9ee-047a-452d-bddc-0fc33fde24c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nAll six generators are base (pretrained) models.\nWeb text is predominantly produced by instruction-tuned and RLHF-aligned models, whose generation distributions differ from base model continuations.\nPreliminary instruct experiments show substantial depth-signal degradation: OLMo-2-1B-Instruct drops to 3-class LOGO F1\\,=\\,0.338 (vs.\\ 0.764 for base OLMo-2-1B) and Qwen3-0.6B with chat template to F1\\,=\\,0.667 (vs.\\ 0.816 base under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\\ref{tab:logo-results}).\nLength-controlled analysis reveals that the effect of instruct tuning on surface features is model-dependent: Qwen models retain weakly positive TTR and hapax partial correlations with depth, while OLMo-Instruct exhibits negative correlations similar to base models.\nEntropy-based depth signals show reversed partial correlations across all three instruct models (partial $\\rho$ ranging from +0.103 to +0.364), though length-matched analysis for the smallest model yields near-zero correlations ($|\\rho| < 0.02$) and binary classification is near chance (F1 $\\approx$ 0.5), leaving the interpretation of these residuals ambiguous.\nDisentangling architecture-dependent surface effects from the residual entropy sign change in instruct-tuned generation is a critical direction for future work.\n\nOur experiments include generators up to 8.2B parameters (Qwen3-8B).\nDepth signal persists at this scale, but cross-scale classifier transfer incurs a moderate gap (held-out F1\\,=\\,0.683 vs.\\ 0.76--0.86 for $\\leq$2.8B generators).\nFrontier models (70B+) remain untested; their higher fluency may further compress feature margins.\n\nWe evaluate three prompt types (continuation, elaboration, rewriting; Appendix~\\ref{app:prompt-type}) but all share the same Pythia-2.8B generator.\nCross-prompt-type transfer (LOPTO F1\\,=\\,0.753) confirms the depth signal generalizes, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\\times$ cross-prompt interactions remain untested.\n\nOur primary evaluation uses single-generator chains; cross-model chains (\\S\\ref{sec:results-classification}) confirm that depth signal persists under generator heterogeneity (3-class F1\\,=\\,0.809, binary F1\\,=\\,0.764), though the six generators tested represent a controlled laboratory setting rather than the full diversity of web-scale contamination.\nSimulated human editing (\\S\\ref{sec:discussion}) suggests graceful degradation under casual editing, but the gap between simulated token replacement and real-world human post-processing remains untested.\n\nThe reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\\S\\ref{sec:results-differential}) suggest the phenomenon is not reference-specific.\nAll seed texts are English Wikipedia excerpts; generalization to other languages and domains remains untested.\n\nThe negative downstream result (\\S\\ref{sec:results-downstream}) is evaluated on causal language modeling only.\nOther downstream tasks (classification, summarization, instruction following) may respond differently to depth composition.\n\nOur default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \\in [0.5, 0.7]$, F1 range ${\\leq}0.3$\\,pp) but substantial degradation at $t{=}1.0$ ($-6$\\,pp), indicating that depth fingerprinting assumes standard decoding regimes.\n\nWe use 3-class granularity (gen-0\\,/\\,gen-1\\,/\\,gen-2+). A 5-class evaluation (Appendix~\\ref{app:finer-depth}) yields LOGO F1\\,$\\approx$\\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.\n",
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01G3uy17o6AzchJcKdCwRXuo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "b8be0425-c97a-46f1-8159-a29f513339be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 32 · 2026-05-16T03:05:40.914Z_

<details><summary>↩ Tool result · `toolu_01G3uy17o6AzchJcKdCwRXuo`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage---how many recursive generation steps it has undergone---not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency---rather than content removal---is the objective.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "9a48eec8-0ff1-4727-a113-0a7f8ef22af9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ethics.tex",
      "content": "\\section*{Ethics Statement}\n\\label{sec:ethics}\n\nAll texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.\nOur method estimates the generation depth of a text passage---how many recursive generation steps it has undergone---not the identity of its author.\nIndividual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.\nWe acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).\nWe encourage deployment in data governance pipelines where provenance transparency---rather than content removal---is the objective.\n",
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

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01DPLNUxkDYihicmqRSCmSt6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "7e451fba-fcc1-4f3d-a7f5-11a779c02004",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 34 · 2026-05-16T03:05:41.575Z_

<details><summary>↩ Tool result · `toolu_01DPLNUxkDYihicmqRSCmSt6`</summary>

```text
1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
40	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
41	  journal = {arXiv preprint arXiv:2605.01647},
42	  year = {2026},
43	}
44	
45	@inproceedings{intrinsic_dimension,
46	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
47	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  year = {2023},
50	}
51	
52	@article{diveye,
53	  title = {{Diversity Boosts AI-Generated Text Detection}},
54	  author = {Basani, Advik Raj and Chen, Pin-Yu},
55	  journal = {Transactions on Machine Learning Research},
56	  year = {2026},
57	}
58	
59	@article{generator_barrier,
60	  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
61	  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
62	  journal = {arXiv preprint arXiv:2604.13692},
63	  year = {2026},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{grover,
96	  title = {{Defending Against Neural Fake News}},
97	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2019},
100	}
101	
102	@article{release_strategies,
103	  title = {{Release Strategies and the Social Impacts of Language Models}},
104	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
105	  journal = {arXiv preprint arXiv:1908.09203},
106	  year = {2019},
107	}
108	
109	@inproceedings{beyond_binary,
110	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
111	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
112	  booktitle = {Proceedings of the ACM Web Conference},
113	  year = {2025},
114	}
115	
116	@inproceedings{semeval2024_task8,
117	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
118	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
119	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
120	  year = {2024},
121	}
122	
123	% ===== Model Collapse =====
124	
125	@inproceedings{self_consuming_mad,
126	  title = {{Self-Consuming Generative Models Go MAD}},
127	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
128	  booktitle = {Proceedings of the International Conference on Learning Representations},
129	  year = {2024},
130	}
131	
132	@article{curse_of_recursion,
133	  title = {{AI models collapse when trained on recursively generated data}},
134	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
135	  journal = {Nature},
136	  volume = {631},
137	  pages = {755--759},
138	  year = {2024},
139	  doi = {10.1038/s41586-024-07566-y},
140	}
141	
142	@inproceedings{strong_model_collapse,
143	  title = {{Strong Model Collapse}},
144	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
145	  booktitle = {Proceedings of the International Conference on Learning Representations},
146	  year = {2025},
147	}
148	
149	@inproceedings{model_collapse_avoidable,
150	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
151	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
152	  booktitle = {Proceedings of the Conference on Language Modeling},
153	  year = {2024},
154	}
155	
156	% ===== Fine-tuning =====
157	
158	@inproceedings{qlora,
159	  title = {{QLoRA: Efficient Finetuning of Quantized Language Models}},
160	  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
161	  booktitle = {Advances in Neural Information Processing Systems},
162	  year = {2023},
163	}
164	
165	% ===== OOD Detection =====
166	
167	@inproceedings{ood_baseline,
168	  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},
169	  author = {Hendrycks, Dan and Gimpel, Kevin},
170	  booktitle = {Proceedings of the International Conference on Learning Representations},
171	  year = {2017},
172	}
173	
174	% ===== Data Quality =====
175	
176	@inproceedings{dsir,
177	  title = {{Data Selection for Language Models via Importance Resampling}},
178	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
179	  booktitle = {Advances in Neural Information Processing Systems},
180	  year = {2023},
181	}
182	
183	@inproceedings{qurating,
184	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
185	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
186	  booktitle = {Proceedings of the International Conference on Machine Learning},
187	  year = {2024},
188	}
189	
190	@inproceedings{ccnet,
191	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
192	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
193	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
194	  year = {2020},
195	}
196	
197	% ===== Watermarking =====
198	
199	@inproceedings{watermark_llm,
200	  title = {{A Watermark for Large Language Models}},
201	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
202	  booktitle = {Proceedings of the International Conference on Machine Learning},
203	  year = {2023},
204	}
205	
206	@article{synthid_text,
207	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
208	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
209	  journal = {Nature},
210	  volume = {634},
211	  pages = {818--823},
212	  year = {2024},
213	  doi = {10.1038/s41586-024-08025-4},
214	}
215	
216	@misc{aaronson_watermark,
217	  title = {{Watermarking GPT Outputs}},
218	  author = {Aaronson, Scott and Kirchner, Hendrik},
219	  year = {2022},
220	  howpublished = {Technical Talk},
221	  url = {https://scottaaronson.blog/?p=6823},
222	}
223	
224	@article{chainwash,
225	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
226	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
227	  journal = {arXiv preprint arXiv:2605.05503},
228	  year = {2026},
229	}
230	
231	% ===== Vocabulary Diversity =====
232	
233	@inproceedings{curious_decline,
234	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
235	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
236	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
237	  year = {2024},
238	}
239	
240	@inproceedings{writing_diversity,
241	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
242	  author = {Padmakumar, Vishakh and He, He},
243	  booktitle = {Proceedings of the International Conference on Learning Representations},
244	  year = {2024},
245	}
246	
247	@inproceedings{nucleus_sampling,
248	  title = {{The Curious Case of Neural Text Degeneration}},
249	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
250	  booktitle = {Proceedings of the International Conference on Learning Representations},
251	  year = {2020},
252	}
253	
254	@inproceedings{mapping_llm_science,
255	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
256	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
257	  booktitle = {Proceedings of the Conference on Language Modeling},
258	  year = {2024},
259	}
260	
261	@inproceedings{monitoring_ai_review,
262	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
263	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
264	  booktitle = {Proceedings of the International Conference on Machine Learning},
265	  year = {2024},
266	}
267	
268	% ===== Stylometry =====
269	
270	@article{stamatatos_survey,
271	  title = {{A Survey of Modern Authorship Attribution Methods}},
272	  author = {Stamatatos, Efstathios},
273	  journal = {Journal of the American Society for Information Science and Technology},
274	  year = {2009},
275	}
276	
277	@article{koppel_authorship,
278	  title = {{Computational Methods in Authorship Attribution}},
279	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
280	  journal = {Journal of the American Society for Information Science and Technology},
281	  year = {2009},
282	}
283	
284	@inproceedings{uchendu_attribution,
285	  title = {{Authorship Attribution for Neural Text Generation}},
286	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
287	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
288	  year = {2020},
289	}
290	
291	@inproceedings{munir_looking_glass,
292	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
293	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
294	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
295	  pages = {1811--1822},
296	  year = {2021},
297	  doi = {10.18653/v1/2021.eacl-main.155},
298	}
299	
300	% ===== Iterative Generation =====
301	
302	@inproceedings{broken_telephone,
303	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
304	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
305	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
306	  year = {2025},
307	}
308	
309	@article{markovian_chains,
310	  title = {{Markovian Generation Chains in Large Language Models}},
311	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
312	  journal = {arXiv preprint arXiv:2603.11228},
313	  year = {2026},
314	}
315	
316	% ===== Membership Inference =====
317	
318	@inproceedings{min_k_percent,
319	  title = {{Detecting Pretraining Data from Large Language Models}},
320	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
321	  booktitle = {Proceedings of the International Conference on Learning Representations},
322	  year = {2024},
323	}
324	
325	% ===== Survey =====
326	
327	@article{wu_survey_2025,
328	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
329	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
330	  journal = {Computational Linguistics},
331	  publisher = {MIT Press},
332	  volume = {51},
333	  number = {1},
334	  pages = {275--338},
335	  year = {2025},
336	  doi = {10.1162/coli_a_00549},
337	}
338	
339	@inproceedings{jawahar_survey,
340	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
341	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
342	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
343	  year = {2020},
344	}
345	
346	% ===== Models =====
347	
348	@inproceedings{pythia,
349	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
350	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
351	  booktitle = {Proceedings of the International Conference on Machine Learning},
352	  year = {2023},
353	}
354	
355	@inproceedings{olmo,
356	  title = {{OLMo: Accelerating the Science of Language Models}},
357	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
358	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
359	  year = {2024},
360	}
361	
362	@article{qwen3,
363	  title = {{Qwen3 Technical Report}},
364	  author = {{Qwen Team}},
365	  journal = {arXiv preprint arXiv:2505.09388},
366	  year = {2025},
367	}
368	
369	% ===== Machine Learning =====
370	
371	@article{coral_ordinal,
372	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
373	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
374	  journal = {Pattern Recognition Letters},
375	  volume = {140},
376	  pages = {325--331},
377	  year = {2020},
378	}
379	
380	@inproceedings{frank_hall_ordinal,
381	  title = {{A Simple Approach to Ordinal Classification}},
382	  author = {Frank, Eibe and Hall, Mark},
383	  booktitle = {Proceedings of the European Conference on Machine Learning},
384	  year = {2001},
385	}
386	
387	@inproceedings{xgboost,
388	  title = {{XGBoost: A Scalable Tree Boosting System}},
389	  author = {Chen, Tianqi and Guestrin, Carlos},
390	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
391	  year = {2016},
392	}
393	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "1b13010d-027c-4c82-bbd2-b52b622d7d90",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
      "content": "% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{intrinsic_dimension,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@article{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani, Advik Raj and Chen, Pin-Yu},\n  journal = {Transactions on Machine Learning Research},\n  year = {2026},\n}\n\n@article{generator_barrier,\n  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  journal = {arXiv preprint arXiv:2604.13692},\n  year = {2026},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@article{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},\n  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal = {Transactions on Machine Learning Research},\n  year = {2025},\n  url = {https://openreview.net/forum?id=OOgsAZdFOt},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n@inproceedings{beyond_binary,\n  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},\n  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle = {Proceedings of the ACM Web Conference},\n  year = {2025},\n}\n\n@inproceedings{semeval2024_task8,\n  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},\n  year = {2024},\n}\n\n% ===== Model Collapse =====\n\n@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{curse_of_recursion,\n  title = {{AI models collapse when trained on recursively generated data}},\n  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal = {Nature},\n  volume = {631},\n  pages = {755--759},\n  year = {2024},\n  doi = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2025},\n}\n\n@inproceedings{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n% ===== Fine-tuning =====\n\n@inproceedings{qlora,\n  title = {{QLoRA: Efficient Finetuning of Quantized Language Models}},\n  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n% ===== OOD Detection =====\n\n@inproceedings{ood_baseline,\n  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},\n  author = {Hendrycks, Dan and Gimpel, Kevin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2017},\n}\n\n% ===== Data Quality =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},\n  journal = {Nature},\n  volume = {634},\n  pages = {818--823},\n  year = {2024},\n  doi = {10.1038/s41586-024-08025-4},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Hendrik},\n  year = {2022},\n  howpublished = {Technical Talk},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar, Vishakh and He, He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n@inproceedings{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos, Efstathios},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n@inproceedings{munir_looking_glass,\n  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},\n  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},\n  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},\n  pages = {1811--1822},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.155},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n% ===== Survey =====\n\n@article{wu_survey_2025,\n  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  journal = {Computational Linguistics},\n  publisher = {MIT Press},\n  volume = {51},\n  number = {1},\n  pages = {275--338},\n  year = {2025},\n  doi = {10.1162/coli_a_00549},\n}\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n\n% ===== Models =====\n\n@inproceedings{pythia,\n  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},\n  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{olmo,\n  title = {{OLMo: Accelerating the Science of Language Models}},\n  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{qwen3,\n  title = {{Qwen3 Technical Report}},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n}\n\n% ===== Machine Learning =====\n\n@article{coral_ordinal,\n  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal = {Pattern Recognition Letters},\n  volume = {140},\n  pages = {325--331},\n  year = {2020},\n}\n\n@inproceedings{frank_hall_ordinal,\n  title = {{A Simple Approach to Ordinal Classification}},\n  author = {Frank, Eibe and Hall, Mark},\n  booktitle = {Proceedings of the European Conference on Machine Learning},\n  year = {2001},\n}\n\n@inproceedings{xgboost,\n  title = {{XGBoost: A Scalable Tree Boosting System}},\n  author = {Chen, Tianqi and Guestrin, Carlos},\n  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},\n  year = {2016},\n}\n",
      "numLines": 393,
      "startLine": 1,
      "totalLines": 393
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01JfHSEhG3KLVpJXk566k8oF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "c202285d-c516-43c7-81a4-ae19332b649c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPLDZHEF93jkmMvjGUScDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 24251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

_source line 36 · 2026-05-16T03:05:41.753Z_

<details><summary>↩ Tool result · `toolu_01JfHSEhG3KLVpJXk566k8oF`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\begin{tabular}{llccc}
5	\toprule
6	\textbf{Reference Model} & \textbf{Family} & \textbf{Params} & \textbf{LOGO F1} & \textbf{Entropy Drift Range} \\
7	\midrule
8	Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
9	OLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\
10	Qwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\
11	\bottomrule
12	\end{tabular}
13	\caption{Cross-family reference model validation.
14	Drift direction is consistent (negative) across all three reference models;
15	magnitude varies with reference model capacity.}
16	\label{tab:cross-ref}
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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "1c36e3a9-3f05-48b0-9540-5df37bd99bd1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/table4.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Reference Model} & \\textbf{Family} & \\textbf{Params} & \\textbf{LOGO F1} & \\textbf{Entropy Drift Range} \\\\\n\\midrule\nPythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\\\\nOLMo-2-1B  & OLMo   & 1.5B & 0.807 & [$-$0.61, $-$0.91] \\\\\nQwen3-0.6B & Qwen   & 0.6B & 0.816 & [$-$0.96, $-$1.35] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-family reference model validation.\nDrift direction is consistent (negative) across all three reference models;\nmagnitude varies with reference model capacity.}\n\\label{tab:cross-ref}\n\\end{table}\n",
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

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the appendix files to complete the check. Let me also search for any anonymization issues and check the references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "ca46ac7a-ed9d-425b-bc50-221fd53095db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 38_

Now let me read the appendix files and perform the anonymization/reference checks in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "6b607875-bae3-4d27-9f58-08b48e1f7cf4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01EoG9FZJwV9JJ2saf4ooRyb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "449a5015-5077-4298-b161-23a777c61ef0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 40 · 2026-05-16T03:05:47.459Z_

<details><summary>↩ Tool result · `toolu_01EoG9FZJwV9JJ2saf4ooRyb`</summary>

```text
1	% Appendix A — Length Confound Analysis
2	% Data source: plan-013 (23,032 samples, 5 generators)
3	
4	Surface diversity features (TTR, hapax ratio) mechanically depend on text length:
5	shorter texts yield higher type-token ratios by construction.
6	If generation depth systematically shortens text, observed depth trends could be length artifacts rather than genuine distributional shifts.
7	We rule this out with three complementary analyses.
8	
9	\paragraph{(a) Length--depth correlation.}
10	We compute Spearman rank correlation between word count and depth across all five generators.
11	Correlations are weak and inconsistent in sign:
12	$\rho$ ranges from $-0.066$ (Pythia-1B) to $+0.134$ (OLMo-2-1B), with $|\rho| < 0.14$ in every case.
13	One generator (Qwen3-0.6B) shows no significant correlation ($\rho = 0.012$, $p = 0.43$).
14	Length and depth are thus near-independent in our corpus.
15	
16	\paragraph{(b) Length-normalized feature trends.}
17	To eliminate residual length effects, we recompute TTR and hapax ratio on fixed 200-word windows.
18	After normalization, monotonic depth trends are fully preserved for all generators; moreover, Spearman correlations between normalized features and depth \emph{increase} in absolute value (e.g., Pythia-2.8B TTR: $\rho = -0.633 \to -0.715$).
19	Length removal sharpens the depth signal rather than diminishing it, confirming that the signal is not a length artifact.
20	
21	\paragraph{(c) Length-matched classification.}
22	We subsample the dataset so that word-count distributions are equalized across depth classes, then retrain the 3-class XGBoost classifier (\S\ref{sec:results-classification}).
23	Macro-F1 changes by $\Delta = +0.041$ relative to the unmatched baseline---performance \emph{improves} when length variance is removed.
24	This is consistent with length acting as noise rather than signal.
25	
26	\paragraph{Conclusion.}
27	We observe a dropout bias: shorter texts are more likely to fall below the minimum-length threshold at deeper generation stages.
28	However, this bias does not drive the depth fingerprint.
29	All three analyses converge on the same conclusion: the depth signal captured by our feature ensemble is independent of text-length variation.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "13cf654c-e52c-4c5f-be26-ad03ee9dbdf1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_length.tex",
      "content": "% Appendix A — Length Confound Analysis\n% Data source: plan-013 (23,032 samples, 5 generators)\n\nSurface diversity features (TTR, hapax ratio) mechanically depend on text length:\nshorter texts yield higher type-token ratios by construction.\nIf generation depth systematically shortens text, observed depth trends could be length artifacts rather than genuine distributional shifts.\nWe rule this out with three complementary analyses.\n\n\\paragraph{(a) Length--depth correlation.}\nWe compute Spearman rank correlation between word count and depth across all five generators.\nCorrelations are weak and inconsistent in sign:\n$\\rho$ ranges from $-0.066$ (Pythia-1B) to $+0.134$ (OLMo-2-1B), with $|\\rho| < 0.14$ in every case.\nOne generator (Qwen3-0.6B) shows no significant correlation ($\\rho = 0.012$, $p = 0.43$).\nLength and depth are thus near-independent in our corpus.\n\n\\paragraph{(b) Length-normalized feature trends.}\nTo eliminate residual length effects, we recompute TTR and hapax ratio on fixed 200-word windows.\nAfter normalization, monotonic depth trends are fully preserved for all generators; moreover, Spearman correlations between normalized features and depth \\emph{increase} in absolute value (e.g., Pythia-2.8B TTR: $\\rho = -0.633 \\to -0.715$).\nLength removal sharpens the depth signal rather than diminishing it, confirming that the signal is not a length artifact.\n\n\\paragraph{(c) Length-matched classification.}\nWe subsample the dataset so that word-count distributions are equalized across depth classes, then retrain the 3-class XGBoost classifier (\\S\\ref{sec:results-classification}).\nMacro-F1 changes by $\\Delta = +0.041$ relative to the unmatched baseline---performance \\emph{improves} when length variance is removed.\nThis is consistent with length acting as noise rather than signal.\n\n\\paragraph{Conclusion.}\nWe observe a dropout bias: shorter texts are more likely to fall below the minimum-length threshold at deeper generation stages.\nHowever, this bias does not drive the depth fingerprint.\nAll three analyses converge on the same conclusion: the depth signal captured by our feature ensemble is independent of text-length variation.\n",
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

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01CPLbiaRPsP1Pn9HDHrgFAk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "a0ad6b11-691e-4ac7-b54c-dca880c138be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 42 · 2026-05-16T03:05:47.868Z_

<details><summary>↩ Tool result · `toolu_01CPLbiaRPsP1Pn9HDHrgFAk`</summary>

```text
1	We evaluate depth fingerprinting under three prompt types using Pythia-2.8B: \emph{continuation} (``Continue the following text''), \emph{elaboration} (``Elaborate on the following text''), and \emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\times$ 5 depths.
2	
3	\paragraph{Within-prompt-type classification.}
4	5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while stationary features (entropy std, tail decay) change by less than 5\%.
5	
6	\paragraph{Cross-prompt-type transfer (LOPTO).}
7	Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "ebc1db8f-46aa-4974-9db7-b682df2a36f2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_prompt_type.tex",
      "content": "We evaluate depth fingerprinting under three prompt types using Pythia-2.8B: \\emph{continuation} (``Continue the following text''), \\emph{elaboration} (``Elaborate on the following text''), and \\emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\\times$ 5 depths.\n\n\\paragraph{Within-prompt-type classification.}\n5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while stationary features (entropy std, tail decay) change by less than 5\\%.\n\n\\paragraph{Cross-prompt-type transfer (LOPTO).}\nLeave-one-prompt-type-out evaluation yields average F1\\,=\\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\\% per depth step), followed by rewriting (6.1\\%) and elaboration (1.4\\%), consistent with continuation chains applying less semantic constraint on the output.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_011Rk54s4nzx6ZfyAbzZrFNE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "81055a45-2dae-493e-98cd-e9f46de3335d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 44 · 2026-05-16T03:05:48.861Z_

<details><summary>↩ Tool result · `toolu_011Rk54s4nzx6ZfyAbzZrFNE`</summary>

```text
1	We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \S\ref{sec:method}.
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lcccc}
7	\toprule
8	\textbf{Held-out Generator} & \textbf{Macro F1} & \textbf{Weighted F1} & \textbf{Accuracy} \\
9	\midrule
10	OLMo-2-1B       & 0.484 & 0.506 & 0.524 \\
11	Pythia-1B        & 0.543 & 0.568 & 0.575 \\
12	Pythia-2.8B      & 0.523 & 0.540 & 0.560 \\
13	Qwen3-0.6B      & 0.513 & 0.521 & 0.546 \\
14	Qwen3-1.7B      & 0.510 & 0.536 & 0.548 \\
15	Qwen3-8B        & 0.434 & 0.455 & 0.493 \\
16	\midrule
17	\textbf{Average} & \textbf{0.501 $\pm$ 0.038} & \textbf{0.521} & \textbf{0.541} \\
18	\bottomrule
19	\end{tabular}
20	\caption{5-class LOGO evaluation. Each row holds out one generator for testing, training on the remaining five.}
21	\label{tab:5class-logo}
22	\end{table}
23	
24	\begin{table}[h]
25	\centering
26	\small
27	\begin{tabular}{lccccc}
28	\toprule
29	\textbf{Metric} & \textbf{Gen-0} & \textbf{Gen-1} & \textbf{Gen-2} & \textbf{Gen-3} & \textbf{Gen-4} \\
30	\midrule
31	Avg F1      & 0.921 & 0.634 & 0.268 & 0.259 & 0.423 \\
32	\bottomrule
33	\end{tabular}
34	\caption{Per-class F1 averaged across all six LOGO folds.}
35	\label{tab:5class-perclass}
36	\end{table}
37	
38	\paragraph{Analysis.}
39	Moving from 3-class (gen-0 / gen-1 / gen-2+) to 5-class classification reduces LOGO macro F1 from 0.789 to 0.501, a drop of 0.288.
40	The degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.268 and 0.259 F1, respectively.
41	The aggregated confusion matrix reveals that 36.5\% of true gen-2 samples are misclassified as gen-1, while 37.8\% of true gen-3 samples are predicted as gen-4.
42	Adjacent depths (gen-2$\leftrightarrow$gen-3, gen-3$\leftrightarrow$gen-4) account for the majority of errors, consistent with the intuition that deeper recursive generations converge in surface-level statistical fingerprints.
43	Gen-0 (human text) remains highly distinguishable (F1 = 0.921), and gen-1 retains moderate separability (F1 = 0.634).
44	Notably, shape features that are near-stationary in the 3-class setting become substantially more important under 5-class evaluation: permutation importance of entropy\_std increases by 93\% and tail\_decay by 400\% relative to 3-class, yet these gains are insufficient to resolve adjacent depths.
45	These results support the 3-class grouping adopted in the main paper: collapsing gen-2+ preserves the most informative boundary (human vs.\ first-generation vs.\ deeper recursion) while avoiding the noise introduced by near-identical adjacent depths.
46	
47	\paragraph{Classifier comparison.}
48	To verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we evaluate four alternatives under the same protocol: HistGradientBoosting (macro F1\,=\,0.501, 95\% bootstrap CI [0.496, 0.506]), random forest (0.476), logistic regression (0.447), and Frank-Hall ordinal reduction (0.451).
49	All classifiers perform comparably to the default XGBoost ensemble (0.501), ruling out classifier capacity as the bottleneck.
50	The gen-2/gen-3 boundary is the primary failure mode across all methods: these two classes are effectively inseparable with the current feature set, establishing 3-class granularity as the practical ceiling for surface and entropy features.
51	At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), confirming that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "f9dae0b6-1a71-4ed6-9cbc-fee5cacc52fa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_finer_depth.tex",
      "content": "We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \\S\\ref{sec:method}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Held-out Generator} & \\textbf{Macro F1} & \\textbf{Weighted F1} & \\textbf{Accuracy} \\\\\n\\midrule\nOLMo-2-1B       & 0.484 & 0.506 & 0.524 \\\\\nPythia-1B        & 0.543 & 0.568 & 0.575 \\\\\nPythia-2.8B      & 0.523 & 0.540 & 0.560 \\\\\nQwen3-0.6B      & 0.513 & 0.521 & 0.546 \\\\\nQwen3-1.7B      & 0.510 & 0.536 & 0.548 \\\\\nQwen3-8B        & 0.434 & 0.455 & 0.493 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.501 $\\pm$ 0.038} & \\textbf{0.521} & \\textbf{0.541} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{5-class LOGO evaluation. Each row holds out one generator for testing, training on the remaining five.}\n\\label{tab:5class-logo}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Gen-0} & \\textbf{Gen-1} & \\textbf{Gen-2} & \\textbf{Gen-3} & \\textbf{Gen-4} \\\\\n\\midrule\nAvg F1      & 0.921 & 0.634 & 0.268 & 0.259 & 0.423 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-class F1 averaged across all six LOGO folds.}\n\\label{tab:5class-perclass}\n\\end{table}\n\n\\paragraph{Analysis.}\nMoving from 3-class (gen-0 / gen-1 / gen-2+) to 5-class classification reduces LOGO macro F1 from 0.789 to 0.501, a drop of 0.288.\nThe degradation is concentrated in the middle depths: gen-2 and gen-3 achieve only 0.268 and 0.259 F1, respectively.\nThe aggregated confusion matrix reveals that 36.5\\% of true gen-2 samples are misclassified as gen-1, while 37.8\\% of true gen-3 samples are predicted as gen-4.\nAdjacent depths (gen-2$\\leftrightarrow$gen-3, gen-3$\\leftrightarrow$gen-4) account for the majority of errors, consistent with the intuition that deeper recursive generations converge in surface-level statistical fingerprints.\nGen-0 (human text) remains highly distinguishable (F1 = 0.921), and gen-1 retains moderate separability (F1 = 0.634).\nNotably, shape features that are near-stationary in the 3-class setting become substantially more important under 5-class evaluation: permutation importance of entropy\\_std increases by 93\\% and tail\\_decay by 400\\% relative to 3-class, yet these gains are insufficient to resolve adjacent depths.\nThese results support the 3-class grouping adopted in the main paper: collapsing gen-2+ preserves the most informative boundary (human vs.\\ first-generation vs.\\ deeper recursion) while avoiding the noise introduced by near-identical adjacent depths.\n\n\\paragraph{Classifier comparison.}\nTo verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we evaluate four alternatives under the same protocol: HistGradientBoosting (macro F1\\,=\\,0.501, 95\\% bootstrap CI [0.496, 0.506]), random forest (0.476), logistic regression (0.447), and Frank-Hall ordinal reduction (0.451).\nAll classifiers perform comparably to the default XGBoost ensemble (0.501), ruling out classifier capacity as the bottleneck.\nThe gen-2/gen-3 boundary is the primary failure mode across all methods: these two classes are effectively inseparable with the current feature set, establishing 3-class granularity as the practical ceiling for surface and entropy features.\nAt the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\\S\\ref{sec:results}), confirming that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01BwYkoKWUpvjHMb1Aen5yhi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "513e22d3-715c-4631-86e0-f0058293dbdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 46 · 2026-05-16T03:05:49.299Z_

<details><summary>↩ Tool result · `toolu_01BwYkoKWUpvjHMb1Aen5yhi`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs on the same 6-generator dataset used throughout, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use the same LOGO protocol as the main experiments.
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
12	\label{tab:qlora}
13	\begin{tabular}{lccc}
14	\toprule
15	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
16	\midrule
17	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
18	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	\paragraph{Results.}
24	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003), a +11.6\,pp improvement over the XGBoost baseline (0.789).
25	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
26	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
27	
28	\paragraph{Hyperparameter robustness.}
29	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), confirming stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
30	
31	\paragraph{Implications.}
32	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture---the seven handcrafted features are a strong but lossy compression of the full distributional information.
33	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
34	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "c1659684-4a7c-46bd-b97f-95eefb2b45d0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_qlora.tex",
      "content": "To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \\cite{qlora}.\n\n\\paragraph{Setup.}\nWe fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \\times 10^{-4}$, and 3 epochs on the same 6-generator dataset used throughout, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\nFor 3-class evaluation, we collapse predictions into gen-0\\,/\\,gen-1\\,/\\,gen-2+ post hoc.\nAll results use the same LOGO protocol as the main experiments.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{QLoRA end-to-end depth classification vs.\\ XGBoost on handcrafted features, under LOGO evaluation.}\n\\label{tab:qlora}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{5-class F1} & \\textbf{3-class F1} & \\textbf{Per-class F1 (5-class)} \\\\\n\\midrule\nXGBoost (7 features) & 0.501 $\\pm$ 0.038 & 0.789 & --- \\\\\nQLoRA (Qwen3-0.6B)   & 0.583 $\\pm$ 0.010 & 0.905 $\\pm$ 0.003 & 0.999\\,/\\,0.796\\,/\\,0.413\\,/\\,0.259\\,/\\,0.447 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nQLoRA achieves 3-class LOGO F1\\,=\\,0.905 ($\\pm$0.003), a +11.6\\,pp improvement over the XGBoost baseline (0.789).\nOn 5-class evaluation, QLoRA reaches F1\\,=\\,0.583 ($\\pm$0.010) vs.\\ 0.501 for XGBoost (+8.2\\,pp), with the largest gains at gen-1 (0.796 vs.\\ 0.634) and gen-2 (0.413 vs.\\ 0.268).\nThe gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\\,=\\,0.259), consistent with the feature-level analysis in \\S\\ref{sec:discussion}.\n\n\\paragraph{Hyperparameter robustness.}\nA second run with LoRA rank 32 and seed 123 yields 5-class F1\\,=\\,0.587 ($\\pm$0.005) and 3-class F1\\,=\\,0.905 ($\\pm$0.004), confirming stability across hyperparameter and seed variation ($\\Delta < 1$\\,pp on both metrics).\n\n\\paragraph{Implications.}\nThe substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture---the seven handcrafted features are a strong but lossy compression of the full distributional information.\nEnd-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.\nThis confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.\n",
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

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01NkR96oPn7o5KL4SpyhA5Zp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "2ce99be7-732f-474c-960e-7ed10fa84748",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 48 · 2026-05-16T03:05:50.335Z_

<details><summary>↩ Tool result · `toolu_01NkR96oPn7o5KL4SpyhA5Zp`</summary>

```text
1	We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lcc}
7	\toprule
8	\textbf{Dropped feature} & \textbf{LOGO F1} & $\boldsymbol{\Delta}$ \textbf{vs Full} \\
9	\midrule
10	entropy\_max    & 0.774 & $-$1.50\,pp \\
11	entropy\_mean   & 0.783 & $-$0.63\,pp \\
12	ttr             & 0.784 & $-$0.55\,pp \\
13	hapax\_ratio    & 0.785 & $-$0.42\,pp \\
14	tail\_decay     & 0.786 & $-$0.33\,pp \\
15	entropy\_std    & 0.786 & $-$0.29\,pp \\
16	entropy\_min    & 0.789 & $+$0.01\,pp \\
17	\midrule
18	Full (7 features) & 0.789 & --- \\
19	\bottomrule
20	\end{tabular}
21	\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
22	\label{tab:lofo}
23	\end{table}
24	
25	\paragraph{Analysis.}
26	Entropy\_max causes the largest degradation when removed ($-$1.5\,pp), despite ranking only fourth in permutation importance (split frequency 0.063). This indicates that entropy\_max provides unique signal---capturing the most surprising token under the reference model---that is not redundant with other features.
27	Conversely, entropy\_min is fully redundant ($\Delta$\,=\,+0.01\,pp), consistent with its near-zero permutation importance (0.015).
28	Six of seven features contribute positively to the ensemble, confirming that the 7-feature design is not over-specified.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "69bb9e65-23ff-4a97-8d38-36c9d45d4fba",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_lofo.tex",
      "content": "We complement the permutation importance analysis (\\S\\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\\Delta$ is the change relative to the full 7-feature ensemble (F1\\,=\\,0.789).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Dropped feature} & \\textbf{LOGO F1} & $\\boldsymbol{\\Delta}$ \\textbf{vs Full} \\\\\n\\midrule\nentropy\\_max    & 0.774 & $-$1.50\\,pp \\\\\nentropy\\_mean   & 0.783 & $-$0.63\\,pp \\\\\nttr             & 0.784 & $-$0.55\\,pp \\\\\nhapax\\_ratio    & 0.785 & $-$0.42\\,pp \\\\\ntail\\_decay     & 0.786 & $-$0.33\\,pp \\\\\nentropy\\_std    & 0.786 & $-$0.29\\,pp \\\\\nentropy\\_min    & 0.789 & $+$0.01\\,pp \\\\\n\\midrule\nFull (7 features) & 0.789 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}\n\\label{tab:lofo}\n\\end{table}\n\n\\paragraph{Analysis.}\nEntropy\\_max causes the largest degradation when removed ($-$1.5\\,pp), despite ranking only fourth in permutation importance (split frequency 0.063). This indicates that entropy\\_max provides unique signal---capturing the most surprising token under the reference model---that is not redundant with other features.\nConversely, entropy\\_min is fully redundant ($\\Delta$\\,=\\,+0.01\\,pp), consistent with its near-zero permutation importance (0.015).\nSix of seven features contribute positively to the ensemble, confirming that the 7-feature design is not over-specified.\n",
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01SdnMkt2cvaTCfEyWfVxNDT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "95e37f9c-3117-40a0-b584-ba42b9e38a0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 50 · 2026-05-16T03:05:50.726Z_

<details><summary>↩ Tool result · `toolu_01SdnMkt2cvaTCfEyWfVxNDT`</summary>

```text
1	Table~\ref{tab:confusion} reports the aggregated confusion matrix from 6-generator leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
2	
3	\begin{table}[h]
4	\centering
5	\small
6	\begin{tabular}{lccc}
7	\toprule
8	& \textbf{Pred gen-0} & \textbf{Pred gen-1} & \textbf{Pred gen-2+} \\
9	\midrule
10	\textbf{True gen-0} & 5{,}937 (99.4\%) & 35 (0.6\%) & 0 (0.0\%) \\
11	\textbf{True gen-1} & 368 (6.2\%) & 4{,}437 (75.0\%) & 1{,}113 (18.8\%) \\
12	\textbf{True gen-2+} & 464 (3.0\%) & 3{,}646 (23.3\%) & 11{,}529 (73.7\%) \\
13	\bottomrule
14	\end{tabular}
15	\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%), indicating that gen-1 text already carries detectable recursive distortion.}
16	\label{tab:confusion}
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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "1a336d7e-6943-4adf-b158-f10e9542d5bf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_confusion_matrix.tex",
      "content": "Table~\\ref{tab:confusion} reports the aggregated confusion matrix from 6-generator leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\\geq$ 2).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Pred gen-0} & \\textbf{Pred gen-1} & \\textbf{Pred gen-2+} \\\\\n\\midrule\n\\textbf{True gen-0} & 5{,}937 (99.4\\%) & 35 (0.6\\%) & 0 (0.0\\%) \\\\\n\\textbf{True gen-1} & 368 (6.2\\%) & 4{,}437 (75.0\\%) & 1{,}113 (18.8\\%) \\\\\n\\textbf{True gen-2+} & 464 (3.0\\%) & 3{,}646 (23.3\\%) & 11{,}529 (73.7\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\\%) is 3$\\times$ more frequent than as gen-0 (6.2\\%), indicating that gen-1 text already carries detectable recursive distortion.}\n\\label{tab:confusion}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01XkFuqSm1nuH169L4jCuLYe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "a761a878-1616-4db7-9012-11d654a7d224",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 52 · 2026-05-16T03:05:51.200Z_

<details><summary>↩ Tool result · `toolu_01XkFuqSm1nuH169L4jCuLYe`</summary>

```text
1	To verify that the depth signal resides in the features rather than the classifier,
2	we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
3	in place of XGBoost (Table~\ref{tab:alt-classifier}).
4	All other settings---the same 7 features, 3-class labels, and class-balanced downsampling---are
5	kept identical. For Logistic Regression we apply standard scaling to the features.
6	
7	\begin{table}[h]
8	\centering
9	\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1.}
10	\label{tab:alt-classifier}
11	\small
12	\begin{tabular}{lc cccccc}
13	\toprule
14	Classifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\
15	\midrule
16	XGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\
17	Random Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\
18	Logistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	
23	Both tree-based classifiers achieve LOGO F1 $\approx 0.79$,
24	and even a linear model reaches $0.725$---well above the $0.33$ chance baseline for
25	three classes.
26	The per-generator ranking is also consistent across classifiers
27	(Pythia-1B easiest, Qwen3-8B hardest),
28	confirming that discriminative power originates in the entropy and lexical features,
29	not in classifier capacity.
30	
31	\subsection*{Sampling Sensitivity Analysis}
32	\label{app:sampling-sensitivity}
33	
34	To assess robustness to decoding hyperparameters, we regenerate the full chain set under three sampling configurations and re-evaluate the 3-class LOGO pipeline (Table~\ref{tab:sampling-ablation}).
35	
36	\begin{table}[h]
37	\centering
38	\caption{Depth classification under varying sampling parameters. All other settings match the default pipeline.}
39	\label{tab:sampling-ablation}
40	\small
41	\begin{tabular}{lcc ccc}
42	\toprule
43	Config & Temp.\ & Top-$p$ & 3-class F1 & Binary F1 & $\rho$(entropy\_mean) \\
44	\midrule
45	Low        & 0.5 & 0.80 & 0.785 & 0.797 & $-0.694$ \\
46	Default    & 0.7 & 0.90 & 0.788 & 0.799 & $-0.602$ \\
47	High       & 1.0 & 0.95 & 0.726 & 0.733 & $-0.002$ \\
48	\bottomrule
49	\end{tabular}
50	\end{table}
51	
52	The depth signal is robust to moderate sampling variation: low and default configurations differ by at most 0.3\,pp in both 3-class and binary F1, and entropy--depth Spearman correlations remain strongly negative ($\rho \leq -0.60$).
53	At high temperature ($t{=}1.0$, top-$p{=}0.95$), classification degrades by approximately 6\,pp and the entropy--depth correlation collapses to near zero ($\rho = -0.002$).
54	This is consistent with the hypothesis that depth features are shaped by the sampling mechanism (\S\ref{sec:discussion}): elevated temperature injects sufficient randomness to flatten the distributional drift that accumulates across generation steps, effectively masking the depth signal.
55	The practical implication is that depth fingerprinting applies reliably under standard decoding regimes but should not be expected to generalize to high-entropy sampling settings.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "e1b77b75-07bc-45e6-af5d-ce9771b75c6b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_classifier.tex",
      "content": "To verify that the depth signal resides in the features rather than the classifier,\nwe repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest\nin place of XGBoost (Table~\\ref{tab:alt-classifier}).\nAll other settings---the same 7 features, 3-class labels, and class-balanced downsampling---are\nkept identical. For Logistic Regression we apply standard scaling to the features.\n\n\\begin{table}[h]\n\\centering\n\\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1.}\n\\label{tab:alt-classifier}\n\\small\n\\begin{tabular}{lc cccccc}\n\\toprule\nClassifier & Avg F1 & OLMo-2 & Py-1B & Py-2.8B & Qw-0.6B & Qw-1.7B & Qw-8B \\\\\n\\midrule\nXGBoost          & 0.789 & 0.764 & 0.856 & 0.804 & 0.824 & 0.806 & 0.683 \\\\\nRandom Forest    & 0.790 & 0.764 & 0.856 & 0.804 & 0.825 & 0.807 & 0.684 \\\\\nLogistic Regr.   & 0.725 & 0.719 & 0.781 & 0.740 & 0.745 & 0.743 & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth tree-based classifiers achieve LOGO F1 $\\approx 0.79$,\nand even a linear model reaches $0.725$---well above the $0.33$ chance baseline for\nthree classes.\nThe per-generator ranking is also consistent across classifiers\n(Pythia-1B easiest, Qwen3-8B hardest),\nconfirming that discriminative power originates in the entropy and lexical features,\nnot in classifier capacity.\n\n\\subsection*{Sampling Sensitivity Analysis}\n\\label{app:sampling-sensitivity}\n\nTo assess robustness to decoding hyperparameters, we regenerate the full chain set under three sampling configurations and re-evaluate the 3-class LOGO pipeline (Table~\\ref{tab:sampling-ablation}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification under varying sampling parameters. All other settings match the default pipeline.}\n\\label{tab:sampling-ablation}\n\\small\n\\begin{tabular}{lcc ccc}\n\\toprule\nConfig & Temp.\\ & Top-$p$ & 3-class F1 & Binary F1 & $\\rho$(entropy\\_mean) \\\\\n\\midrule\nLow        & 0.5 & 0.80 & 0.785 & 0.797 & $-0.694$ \\\\\nDefault    & 0.7 & 0.90 & 0.788 & 0.799 & $-0.602$ \\\\\nHigh       & 1.0 & 0.95 & 0.726 & 0.733 & $-0.002$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe depth signal is robust to moderate sampling variation: low and default configurations differ by at most 0.3\\,pp in both 3-class and binary F1, and entropy--depth Spearman correlations remain strongly negative ($\\rho \\leq -0.60$).\nAt high temperature ($t{=}1.0$, top-$p{=}0.95$), classification degrades by approximately 6\\,pp and the entropy--depth correlation collapses to near zero ($\\rho = -0.002$).\nThis is consistent with the hypothesis that depth features are shaped by the sampling mechanism (\\S\\ref{sec:discussion}): elevated temperature injects sufficient randomness to flatten the distributional drift that accumulates across generation steps, effectively masking the depth signal.\nThe practical implication is that depth fingerprinting applies reliably under standard decoding regimes but should not be expected to generalize to high-entropy sampling settings.\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01EFff1GWeiXexoCeDfH7eVH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "f7d01da2-592f-4824-a5f2-e2d434d3676e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 54 · 2026-05-16T03:05:52.146Z_

<details><summary>↩ Tool result · `toolu_01EFff1GWeiXexoCeDfH7eVH`</summary>

```text
1	To assess whether depth features are robust to post-generation human editing, we simulate two editing scenarios on the full generation chain dataset and re-evaluate the 6-generator LOGO pipeline (Table~\ref{tab:human-edit}).
2	
3	\paragraph{Random token replacement.}
4	We randomly replace 5\%, 10\%, or 20\% of tokens in each text with uniformly sampled vocabulary items, simulating unstructured human edits (typo corrections, word substitutions).
5	Classification degrades gracefully: 3-class F1 drops by 3.5\,pp at 5\% replacement and 6.0\,pp at 20\%, while binary F1 (gen-1 vs.\ gen-2+) remains nearly unchanged ($\Delta \leq 0.8$\,pp).
6	The asymmetry is expected---random edits primarily disrupt human-vs-machine separation (gen-0 classification) by injecting noise into surface features, but the depth-discriminative distributional signal between gen-1 and gen-2+ is distributed across enough tokens to survive moderate perturbation.
7	
8	\paragraph{LLM rephrase.}
9	We rephrase each text using an instruction-tuned LLM, simulating the common scenario where users lightly edit LLM-generated text with LLM assistance.
10	Three-class F1 drops modestly ($-3.4$\,pp), comparable to 5\% random replacement.
11	However, binary F1 drops substantially ($-6.3$\,pp), indicating that LLM rephrasing specifically erodes the distributional differences between generation depths---consistent with the rephraser imposing its own distributional signature that partially overwrites the depth fingerprint.
12	
13	\begin{table}[h]
14	\centering
15	\small
16	\caption{Human-edit robustness under 6-gen LOGO evaluation. Baseline uses unmodified generation chains.}
17	\label{tab:human-edit}
18	\begin{tabular}{lcccc}
19	\toprule
20	\textbf{Condition} & \textbf{3-class F1} & \textbf{Binary F1} & \textbf{$\Delta$ 3-class} & \textbf{$\Delta$ binary} \\
21	\midrule
22	Baseline          & 0.789 & 0.724 & ---       & ---       \\
23	Random 5\%        & 0.754 & 0.718 & $-3.5$\,pp & $-0.6$\,pp \\
24	Random 10\%       & 0.743 & 0.717 & $-4.6$\,pp & $-0.7$\,pp \\
25	Random 20\%       & 0.729 & 0.717 & $-6.0$\,pp & $-0.8$\,pp \\
26	LLM rephrase      & 0.755 & 0.662 & $-3.4$\,pp & $-6.3$\,pp \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	The contrasting degradation patterns reveal that random noise and LLM rephrasing attack different aspects of the depth signal.
32	Random replacement degrades surface features (TTR, hapax ratio) that drive gen-0 separation, while preserving the reference-model entropy distribution that distinguishes gen-1 from gen-2+.
33	LLM rephrasing, by contrast, reshapes the entropy distribution itself, collapsing the depth-discriminative signal while leaving gen-0 separation relatively intact (the rephrased text is still recognizably machine-generated).
34	This suggests that depth fingerprinting is more vulnerable to systematic distributional manipulation than to surface-level noise---a practical consideration for deployment in settings where LLM-assisted editing is prevalent.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "b38815c2-46d5-4e94-b2ee-4e0dc35ccd0e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/appendix_human_edit.tex",
      "content": "To assess whether depth features are robust to post-generation human editing, we simulate two editing scenarios on the full generation chain dataset and re-evaluate the 6-generator LOGO pipeline (Table~\\ref{tab:human-edit}).\n\n\\paragraph{Random token replacement.}\nWe randomly replace 5\\%, 10\\%, or 20\\% of tokens in each text with uniformly sampled vocabulary items, simulating unstructured human edits (typo corrections, word substitutions).\nClassification degrades gracefully: 3-class F1 drops by 3.5\\,pp at 5\\% replacement and 6.0\\,pp at 20\\%, while binary F1 (gen-1 vs.\\ gen-2+) remains nearly unchanged ($\\Delta \\leq 0.8$\\,pp).\nThe asymmetry is expected---random edits primarily disrupt human-vs-machine separation (gen-0 classification) by injecting noise into surface features, but the depth-discriminative distributional signal between gen-1 and gen-2+ is distributed across enough tokens to survive moderate perturbation.\n\n\\paragraph{LLM rephrase.}\nWe rephrase each text using an instruction-tuned LLM, simulating the common scenario where users lightly edit LLM-generated text with LLM assistance.\nThree-class F1 drops modestly ($-3.4$\\,pp), comparable to 5\\% random replacement.\nHowever, binary F1 drops substantially ($-6.3$\\,pp), indicating that LLM rephrasing specifically erodes the distributional differences between generation depths---consistent with the rephraser imposing its own distributional signature that partially overwrites the depth fingerprint.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Human-edit robustness under 6-gen LOGO evaluation. Baseline uses unmodified generation chains.}\n\\label{tab:human-edit}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{3-class F1} & \\textbf{Binary F1} & \\textbf{$\\Delta$ 3-class} & \\textbf{$\\Delta$ binary} \\\\\n\\midrule\nBaseline          & 0.789 & 0.724 & ---       & ---       \\\\\nRandom 5\\%        & 0.754 & 0.718 & $-3.5$\\,pp & $-0.6$\\,pp \\\\\nRandom 10\\%       & 0.743 & 0.717 & $-4.6$\\,pp & $-0.7$\\,pp \\\\\nRandom 20\\%       & 0.729 & 0.717 & $-6.0$\\,pp & $-0.8$\\,pp \\\\\nLLM rephrase      & 0.755 & 0.662 & $-3.4$\\,pp & $-6.3$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe contrasting degradation patterns reveal that random noise and LLM rephrasing attack different aspects of the depth signal.\nRandom replacement degrades surface features (TTR, hapax ratio) that drive gen-0 separation, while preserving the reference-model entropy distribution that distinguishes gen-1 from gen-2+.\nLLM rephrasing, by contrast, reshapes the entropy distribution itself, collapsing the depth-discriminative signal while leaving gen-0 separation relatively intact (the rephrased text is still recognizably machine-generated).\nThis suggests that depth fingerprinting is more vulnerable to systematic distributional manipulation than to surface-level noise---a practical consideration for deployment in settings where LLM-assisted editing is prevalent.\n",
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

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_01LvCU1y7HFpAM5evBMrAHBX`</summary>

```json
{
  "pattern": "(github\\.com|gitlab\\.com|huggingface\\.co|personal|university|institute|lab|acknowledge|thank|funding|grant|http[s]?://)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "b8c8b30f-efcf-47df-bec6-336955cd023c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 56 · 2026-05-16T03:05:53.996Z_

<details><summary>↩ Tool result · `toolu_01LvCU1y7HFpAM5evBMrAHBX`</summary>

```text
artifacts/_project/paper/related_work.tex:2:\label{sec:related}
artifacts/_project/paper/related_work.tex:5:\label{sec:related-detection}
artifacts/_project/paper/related_work.tex:12:Recent efforts extend detection to multi-class settings: \citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.
artifacts/_project/paper/related_work.tex:26:\label{sec:related-collapse}
artifacts/_project/paper/related_work.tex:40:\label{sec:related-diversity}
artifacts/_project/paper/related_work.tex:51:\label{sec:related-provenance}
artifacts/_project/paper/related_work.tex:53:Scalable data curation relies on quality signals to filter web-crawled corpora.
artifacts/_project/paper/appendix_prompt_type.tex:1:We evaluate depth fingerprinting under three prompt types using Pythia-2.8B: \emph{continuation} (``Continue the following text''), \emph{elaboration} (``Elaborate on the following text''), and \emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\times$ 5 depths.
artifacts/_project/paper/appendix_prompt_type.tex:4:5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while stationary features (entropy std, tail decay) change by less than 5\%.
artifacts/_project/paper/appendix_prompt_type.tex:7:Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
artifacts/_project/paper/appendix_qlora.tex:12:\label{tab:qlora}
artifacts/_project/paper/main.tex:36:\label{app:length}
artifacts/_project/paper/main.tex:40:\label{app:prompt-type}
artifacts/_project/paper/main.tex:44:\label{app:finer-depth}
artifacts/_project/paper/main.tex:48:\label{app:qlora}
artifacts/_project/paper/main.tex:52:\label{app:lofo}
artifacts/_project/paper/main.tex:56:\label{app:confusion}
artifacts/_project/paper/main.tex:60:\label{app:classifier}
artifacts/_project/paper/main.tex:64:\label{app:human-edit}
artifacts/_project/paper/appendix_confusion_matrix.tex:16:\label{tab:confusion}
artifacts/_project/paper/appendix_human_edit.tex:17:\label{tab:human-edit}
artifacts/_project/paper/conclusion.tex:2:\label{sec:conclusion}
artifacts/_project/paper/appendix_lofo.tex:22:\label{tab:lofo}
artifacts/_project/paper/discussion.tex:2:\label{sec:discussion}
artifacts/_project/paper/method.tex:2:\label{sec:method}
artifacts/_project/paper/method.tex:5:\label{sec:task}
artifacts/_project/paper/method.tex:14:\label{sec:generation}
artifacts/_project/paper/method.tex:29:\label{sec:features}
artifacts/_project/paper/method.tex:65:\label{sec:evaluation}
artifacts/_project/paper/limitations.tex:2:\label{sec:limitations}
artifacts/_project/paper/limitations.tex:15:We evaluate three prompt types (continuation, elaboration, rewriting; Appendix~\ref{app:prompt-type}) but all share the same Pythia-2.8B generator.
artifacts/_project/paper/limitations.tex:18:Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm that depth signal persists under generator heterogeneity (3-class F1\,=\,0.809, binary F1\,=\,0.764), though the six generators tested represent a controlled laboratory setting rather than the full diversity of web-scale contamination.
artifacts/_project/paper/table4.tex:16:\label{tab:cross-ref}
artifacts/_project/paper/_backup/table1_329527.tex:22:\label{tab:logo-results}
artifacts/_project/paper/_backup/discussion_d3a579.tex:2:\label{sec:discussion}
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:2:\label{sec:introduction}
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:14:We argue that a finer-grained characterization is needed: \emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label.
artifacts/_project/paper/_backup/main_53f11a.tex:22:We formulate \emph{ordinal generation depth estimation}---classifying text into depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label---and study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (0.6B--8B parameters).
artifacts/_project/paper/_backup/main_53f11a.tex:44:\label{app:length}
artifacts/_project/paper/_backup/table4_49aebb.tex:16:\label{tab:cross-ref}
artifacts/_project/paper/_backup/discussion_c98572.tex:2:\label{sec:discussion}
artifacts/_project/paper/_backup/limitations_69ebec.tex:2:\label{sec:limitations}
artifacts/_project/paper/_backup/limitations_69ebec.tex:9:Alternative chain types---elaboration, rewriting, summarization---may induce different drift patterns.
artifacts/_project/paper/_backup/method_e59d28.tex:2:\label{sec:method}
artifacts/_project/paper/_backup/method_e59d28.tex:5:\label{sec:task}
artifacts/_project/paper/_backup/method_e59d28.tex:12:\label{sec:chains}
artifacts/_project/paper/_backup/method_e59d28.tex:19:\label{sec:features}
artifacts/_project/paper/_backup/method_e59d28.tex:46:\label{sec:eval}
artifacts/_project/paper/_backup/table1.tex:22:\label{tab:logo-results}
artifacts/_project/paper/_backup/limitations_b3d194.tex:2:\label{sec:limitations}
artifacts/_project/paper/_backup/limitations_b3d194.tex:9:Alternative chain types---elaboration, rewriting, summarization---may induce different drift patterns and are not evaluated in this work.
artifacts/_project/paper/_backup/table2_373612.tex:16:\label{tab:feature-ablation}
artifacts/_project/paper/_backup/table2.tex:16:\label{tab:feature-ablation}
artifacts/_project/paper/_backup/table3_fc4017.tex:19:\label{tab:downstream}
artifacts/_project/paper/_backup/conclusion_b5f10d.tex:2:\label{sec:conclusion}
artifacts/_project/paper/_backup/conclusion_70534e.tex:2:\label{sec:conclusion}
artifacts/_project/paper/_backup/conclusion_70534e.tex:9:Future work should extend evaluation to frontier-scale generators (70B+), diverse prompt types (elaboration, rewriting), and multi-model generation chains that better approximate real-world contamination scenarios.
artifacts/_project/paper/_backup/table4.tex:16:\label{tab:cross-ref}
artifacts/_project/paper/_backup/table3.tex:19:\label{tab:downstream}
artifacts/_project/paper/_backup/results_b30771.tex:2:\label{sec:results}
artifacts/_project/paper/_backup/results_b30771.tex:7:\label{sec:results-classification}
artifacts/_project/paper/_backup/results_b30771.tex:48:\label{tab:logo-results}
artifacts/_project/paper/_backup/results_b30771.tex:53:\label{sec:results-differential}
artifacts/_project/paper/_backup/results_b30771.tex:87:\label{tab:ablation}
artifacts/_project/paper/_backup/results_b30771.tex:92:\label{sec:results-baselines}
artifacts/_project/paper/_backup/results_b30771.tex:111:\label{tab:baselines}
artifacts/_project/paper/_backup/results_b30771.tex:124:\label{sec:results-downstream}
artifacts/_project/paper/_backup/results_b30771.tex:144:\label{tab:downstream}
artifacts/_project/paper/_backup/method_01fe38.tex:2:\label{sec:method}
artifacts/_project/paper/_backup/method_01fe38.tex:5:\label{sec:task}
artifacts/_project/paper/_backup/method_01fe38.tex:14:\label{sec:generation}
artifacts/_project/paper/_backup/method_01fe38.tex:26:\label{sec:features}
artifacts/_project/paper/_backup/method_01fe38.tex:54:\label{sec:evaluation}
artifacts/_project/paper/appendix_classifier.tex:4:All other settings---the same 7 features, 3-class labels, and class-balanced downsampling---are
artifacts/_project/paper/appendix_classifier.tex:10:\label{tab:alt-classifier}
artifacts/_project/paper/appendix_classifier.tex:32:\label{app:sampling-sensitivity}
artifacts/_project/paper/appendix_classifier.tex:39:\label{tab:sampling-ablation}
artifacts/_project/paper/_backup/ethics_7f2659.tex:2:\label{sec:ethics}
artifacts/_project/paper/_backup/ethics_7f2659.tex:4:All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
artifacts/_project/paper/_backup/ethics_7f2659.tex:6:We acknowledge that depth estimation tools could be misused to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility aids, assistive writing).
artifacts/_project/paper/_backup/ethics_25b81b.tex:2:\label{sec:ethics}
artifacts/_project/paper/_backup/ethics_25b81b.tex:4:All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
artifacts/_project/paper/_backup/ethics_25b81b.tex:7:We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
artifacts/_project/paper/introduction.tex:2:\label{sec:introduction}
artifacts/_project/paper/introduction.tex:14:We argue that a finer-grained characterization is needed: \emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label.
artifacts/_project/paper/ethics.tex:2:\label{sec:ethics}
artifacts/_project/paper/ethics.tex:4:All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
artifacts/_project/paper/ethics.tex:7:We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
artifacts/_project/paper/appendix_finer_depth.tex:21:\label{tab:5class-logo}
artifacts/_project/paper/appendix_finer_depth.tex:35:\label{tab:5class-perclass}
artifacts/_project/paper/appendix_finer_depth.tex:51:At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), confirming that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
artifacts/_project/paper/results.tex:2:\label{sec:results}
artifacts/_project/paper/results.tex:7:\label{sec:results-classification}
artifacts/_project/paper/results.tex:56:\label{tab:logo-results}
artifacts/_project/paper/results.tex:60:To test whether the ordinal structure of the 3-class depth label provides additional discriminative power, we compare CORAL ordinal regression \cite{coral_ordinal} and Frank-Hall ordinal reduction \cite{frank_hall_ordinal} against the standard multiclass XGBoost classifier under the same LOGO protocol.
artifacts/_project/paper/results.tex:68:\label{sec:results-differential}
artifacts/_project/paper/results.tex:77:\label{fig:feature-drift}
artifacts/_project/paper/results.tex:111:\label{tab:ablation}
artifacts/_project/paper/results.tex:118:\label{sec:results-baselines}
artifacts/_project/paper/results.tex:124:\label{fig:baseline-ci}
artifacts/_project/paper/results.tex:148:\label{tab:baselines}
artifacts/_project/paper/results.tex:165:\label{sec:results-downstream}
artifacts/_project/paper/results.tex:185:\label{tab:downstream}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "6bc9fa68-8222-4ab7-ac67-ba0b23d62c81",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:2:\\label{sec:related}\nartifacts/_project/paper/related_work.tex:5:\\label{sec:related-detection}\nartifacts/_project/paper/related_work.tex:12:Recent efforts extend detection to multi-class settings: \\citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \\cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.\nartifacts/_project/paper/related_work.tex:26:\\label{sec:related-collapse}\nartifacts/_project/paper/related_work.tex:40:\\label{sec:related-diversity}\nartifacts/_project/paper/related_work.tex:51:\\label{sec:related-provenance}\nartifacts/_project/paper/related_work.tex:53:Scalable data curation relies on quality signals to filter web-crawled corpora.\nartifacts/_project/paper/appendix_prompt_type.tex:1:We evaluate depth fingerprinting under three prompt types using Pythia-2.8B: \\emph{continuation} (``Continue the following text''), \\emph{elaboration} (``Elaborate on the following text''), and \\emph{inspired rewriting} (``Write a new passage inspired by the following text''). Each uses 995 seeds $\\times$ 5 depths.\nartifacts/_project/paper/appendix_prompt_type.tex:4:5-fold CV macro-F1: continuation 0.78, rewriting 0.74, elaboration 0.73. All three prompt types exhibit the same differential depth response pattern: drifting features (hapax ratio, TTR, entropy mean) show consistent monotonic trends, while stationary features (entropy std, tail decay) change by less than 5\\%.\nartifacts/_project/paper/appendix_prompt_type.tex:7:Leave-one-prompt-type-out evaluation yields average F1\\,=\\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\\% per depth step), followed by rewriting (6.1\\%) and elaboration (1.4\\%), consistent with continuation chains applying less semantic constraint on the output.\nartifacts/_project/paper/appendix_qlora.tex:12:\\label{tab:qlora}\nartifacts/_project/paper/main.tex:36:\\label{app:length}\nartifacts/_project/paper/main.tex:40:\\label{app:prompt-type}\nartifacts/_project/paper/main.tex:44:\\label{app:finer-depth}\nartifacts/_project/paper/main.tex:48:\\label{app:qlora}\nartifacts/_project/paper/main.tex:52:\\label{app:lofo}\nartifacts/_project/paper/main.tex:56:\\label{app:confusion}\nartifacts/_project/paper/main.tex:60:\\label{app:classifier}\nartifacts/_project/paper/main.tex:64:\\label{app:human-edit}\nartifacts/_project/paper/appendix_confusion_matrix.tex:16:\\label{tab:confusion}\nartifacts/_project/paper/appendix_human_edit.tex:17:\\label{tab:human-edit}\nartifacts/_project/paper/conclusion.tex:2:\\label{sec:conclusion}\nartifacts/_project/paper/appendix_lofo.tex:22:\\label{tab:lofo}\nartifacts/_project/paper/discussion.tex:2:\\label{sec:discussion}\nartifacts/_project/paper/method.tex:2:\\label{sec:method}\nartifacts/_project/paper/method.tex:5:\\label{sec:task}\nartifacts/_project/paper/method.tex:14:\\label{sec:generation}\nartifacts/_project/paper/method.tex:29:\\label{sec:features}\nartifacts/_project/paper/method.tex:65:\\label{sec:evaluation}\nartifacts/_project/paper/limitations.tex:2:\\label{sec:limitations}\nartifacts/_project/paper/limitations.tex:15:We evaluate three prompt types (continuation, elaboration, rewriting; Appendix~\\ref{app:prompt-type}) but all share the same Pythia-2.8B generator.\nartifacts/_project/paper/limitations.tex:18:Our primary evaluation uses single-generator chains; cross-model chains (\\S\\ref{sec:results-classification}) confirm that depth signal persists under generator heterogeneity (3-class F1\\,=\\,0.809, binary F1\\,=\\,0.764), though the six generators tested represent a controlled laboratory setting rather than the full diversity of web-scale contamination.\nartifacts/_project/paper/table4.tex:16:\\label{tab:cross-ref}\nartifacts/_project/paper/_backup/table1_329527.tex:22:\\label{tab:logo-results}\nartifacts/_project/paper/_backup/discussion_d3a579.tex:2:\\label{sec:discussion}\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:2:\\label{sec:introduction}\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:14:We argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nartifacts/_project/paper/_backup/main_53f11a.tex:22:We formulate \\emph{ordinal generation depth estimation}---classifying text into depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label---and study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (0.6B--8B parameters).\nartifacts/_project/paper/_backup/main_53f11a.tex:44:\\label{app:length}\nartifacts/_project/paper/_backup/table4_49aebb.tex:16:\\label{tab:cross-ref}\nartifacts/_project/paper/_backup/discussion_c98572.tex:2:\\label{sec:discussion}\nartifacts/_project/paper/_backup/limitations_69ebec.tex:2:\\label{sec:limitations}\nartifacts/_project/paper/_backup/limitations_69ebec.tex:9:Alternative chain types---elaboration, rewriting, summarization---may induce different drift patterns.\nartifacts/_project/paper/_backup/method_e59d28.tex:2:\\label{sec:method}\nartifacts/_project/paper/_backup/method_e59d28.tex:5:\\label{sec:task}\nartifacts/_project/paper/_backup/method_e59d28.tex:12:\\label{sec:chains}\nartifacts/_project/paper/_backup/method_e59d28.tex:19:\\label{sec:features}\nartifacts/_project/paper/_backup/method_e59d28.tex:46:\\label{sec:eval}\nartifacts/_project/paper/_backup/table1.tex:22:\\label{tab:logo-results}\nartifacts/_project/paper/_backup/limitations_b3d194.tex:2:\\label{sec:limitations}\nartifacts/_project/paper/_backup/limitations_b3d194.tex:9:Alternative chain types---elaboration, rewriting, summarization---may induce different drift patterns and are not evaluated in this work.\nartifacts/_project/paper/_backup/table2_373612.tex:16:\\label{tab:feature-ablation}\nartifacts/_project/paper/_backup/table2.tex:16:\\label{tab:feature-ablation}\nartifacts/_project/paper/_backup/table3_fc4017.tex:19:\\label{tab:downstream}\nartifacts/_project/paper/_backup/conclusion_b5f10d.tex:2:\\label{sec:conclusion}\nartifacts/_project/paper/_backup/conclusion_70534e.tex:2:\\label{sec:conclusion}\nartifacts/_project/paper/_backup/conclusion_70534e.tex:9:Future work should extend evaluation to frontier-scale generators (70B+), diverse prompt types (elaboration, rewriting), and multi-model generation chains that better approximate real-world contamination scenarios.\nartifacts/_project/paper/_backup/table4.tex:16:\\label{tab:cross-ref}\nartifacts/_project/paper/_backup/table3.tex:19:\\label{tab:downstream}\nartifacts/_project/paper/_backup/results_b30771.tex:2:\\label{sec:results}\nartifacts/_project/paper/_backup/results_b30771.tex:7:\\label{sec:results-classification}\nartifacts/_project/paper/_backup/results_b30771.tex:48:\\label{tab:logo-results}\nartifacts/_project/paper/_backup/results_b30771.tex:53:\\label{sec:results-differential}\nartifacts/_project/paper/_backup/results_b30771.tex:87:\\label{tab:ablation}\nartifacts/_project/paper/_backup/results_b30771.tex:92:\\label{sec:results-baselines}\nartifacts/_project/paper/_backup/results_b30771.tex:111:\\label{tab:baselines}\nartifacts/_project/paper/_backup/results_b30771.tex:124:\\label{sec:results-downstream}\nartifacts/_project/paper/_backup/results_b30771.tex:144:\\label{tab:downstream}\nartifacts/_project/paper/_backup/method_01fe38.tex:2:\\label{sec:method}\nartifacts/_project/paper/_backup/method_01fe38.tex:5:\\label{sec:task}\nartifacts/_project/paper/_backup/method_01fe38.tex:14:\\label{sec:generation}\nartifacts/_project/paper/_backup/method_01fe38.tex:26:\\label{sec:features}\nartifacts/_project/paper/_backup/method_01fe38.tex:54:\\label{sec:evaluation}\nartifacts/_project/paper/appendix_classifier.tex:4:All other settings---the same 7 features, 3-class labels, and class-balanced downsampling---are\nartifacts/_project/paper/appendix_classifier.tex:10:\\label{tab:alt-classifier}\nartifacts/_project/paper/appendix_classifier.tex:32:\\label{app:sampling-sensitivity}\nartifacts/_project/paper/appendix_classifier.tex:39:\\label{tab:sampling-ablation}\nartifacts/_project/paper/_backup/ethics_7f2659.tex:2:\\label{sec:ethics}\nartifacts/_project/paper/_backup/ethics_7f2659.tex:4:All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.\nartifacts/_project/paper/_backup/ethics_7f2659.tex:6:We acknowledge that depth estimation tools could be misused to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility aids, assistive writing).\nartifacts/_project/paper/_backup/ethics_25b81b.tex:2:\\label{sec:ethics}\nartifacts/_project/paper/_backup/ethics_25b81b.tex:4:All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.\nartifacts/_project/paper/_backup/ethics_25b81b.tex:7:We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).\nartifacts/_project/paper/introduction.tex:2:\\label{sec:introduction}\nartifacts/_project/paper/introduction.tex:14:We argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nartifacts/_project/paper/ethics.tex:2:\\label{sec:ethics}\nartifacts/_project/paper/ethics.tex:4:All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.\nartifacts/_project/paper/ethics.tex:7:We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).\nartifacts/_project/paper/appendix_finer_depth.tex:21:\\label{tab:5class-logo}\nartifacts/_project/paper/appendix_finer_depth.tex:35:\\label{tab:5class-perclass}\nartifacts/_project/paper/appendix_finer_depth.tex:51:At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\\S\\ref{sec:results}), confirming that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.\nartifacts/_project/paper/results.tex:2:\\label{sec:results}\nartifacts/_project/paper/results.tex:7:\\label{sec:results-classification}\nartifacts/_project/paper/results.tex:56:\\label{tab:logo-results}\nartifacts/_project/paper/results.tex:60:To test whether the ordinal structure of the 3-class depth label provides additional discriminative power, we compare CORAL ordinal regression \\cite{coral_ordinal} and Frank-Hall ordinal reduction \\cite{frank_hall_ordinal} against the standard multiclass XGBoost classifier under the same LOGO protocol.\nartifacts/_project/paper/results.tex:68:\\label{sec:results-differential}\nartifacts/_project/paper/results.tex:77:\\label{fig:feature-drift}\nartifacts/_project/paper/results.tex:111:\\label{tab:ablation}\nartifacts/_project/paper/results.tex:118:\\label{sec:results-baselines}\nartifacts/_project/paper/results.tex:124:\\label{fig:baseline-ci}\nartifacts/_project/paper/results.tex:148:\\label{tab:baselines}\nartifacts/_project/paper/results.tex:165:\\label{sec:results-downstream}\nartifacts/_project/paper/results.tex:185:\\label{tab:downstream}",
    "numLines": 103
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Grep · `toolu_01T6Dd9zG9CCUpQF9cT34aE4`</summary>

```json
{
  "pattern": "\\\\cite\\{([^}]+)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "062f82e6-7002-47f4-98c9-0f99b70504c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cVdKSiadtTWeahQsdNgaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 39749,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39749
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

_source line 58 · 2026-05-16T03:05:54.832Z_

<details><summary>↩ Tool result · `toolu_01T6Dd9zG9CCUpQF9cT34aE4`</summary>

```text
artifacts/_project/paper/related_work.tex:7:Methods for distinguishing human-written from machine-generated text have evolved from statistical tests on token-level distributions \cite{gltr,grover,release_strategies} to zero-shot approaches exploiting reference-model likelihoods \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers over linguistic features \cite{feat_aug_transformer,reliable_detection,ld_score}.
artifacts/_project/paper/related_work.tex:12:Recent efforts extend detection to multi-class settings: \citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.
artifacts/_project/paper/related_work.tex:16:Our reference-model entropy features are functionally NLL-based out-of-distribution scores \cite{ood_baseline}; the contribution is not a new detection method but the task formulation (ordinal depth estimation) and the empirical finding that combining drifting and stationary features yields consistent cross-generator performance.
artifacts/_project/paper/related_work.tex:42:Declining lexical diversity in LLM-generated text is documented in both training \cite{curious_decline} and deployment \cite{writing_diversity} settings.
artifacts/_project/paper/related_work.tex:45:These features are classical stylometric measures with a long history in authorship attribution \cite{stamatatos_survey,koppel_authorship}.
artifacts/_project/paper/related_work.tex:57:An alternative approach is proactive provenance through watermarking \cite{watermark_llm,synthid_text,aaronson_watermark}, where identifiable patterns are embedded during generation.
artifacts/_project/paper/appendix_qlora.tex:1:To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
artifacts/_project/paper/discussion.tex:13:Reference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \cite{detectgpt}, GLTR \cite{gltr}, and Binoculars \cite{binoculars}.
artifacts/_project/paper/discussion.tex:15:This connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \cite{ood_baseline}.
artifacts/_project/paper/discussion.tex:29:Unlike paraphrastic chains, which converge within ${\sim}$3 steps \cite{broken_telephone}, non-paraphrastic continuation chains retain some signal at gen-4 (F1\,=\,0.423), but the gen-2/gen-3 boundary remains unresolvable with surface and entropy features alone.
artifacts/_project/paper/discussion.tex:46:The dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \cite{self_consuming_mad}.
artifacts/_project/paper/discussion.tex:49:Our results relate to, but are distinct from, model collapse \cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.
artifacts/_project/paper/method.tex:16:We construct generation chains using six generators spanning three model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, and \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}.
artifacts/_project/paper/method.tex:49:    The 90th percentile threshold follows standard practice in heavy-tail analysis \cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\,pp) across thresholds from the 85th to 95th percentile.
artifacts/_project/paper/method.tex:72:We use XGBoost \cite{xgboost} as the classifier throughout.
artifacts/_project/paper/method.tex:78:We evaluated two ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall ordinal ensemble \cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.
artifacts/_project/paper/method.tex:90:We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:7:\cite{gltr} use token rank histograms under a reference model,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:8:\cite{detectgpt} identify machine text through negative log-probability curvature,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:9:and \cite{fast_detectgpt} accelerate this via conditional probability curvature.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:10:\cite{binoculars} contrast perplexity ratios between two similar models,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:11:while \cite{dna_gpt} measure n-gram divergence after re-generation.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:13:\cite{ld_score} introduce character-distribution signatures orthogonal to perplexity,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:14:\cite{intrinsic_dimension} leverage embedding-space intrinsic dimensionality,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:15:and \cite{diveye} capture token surprisal diversity patterns.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:16:Learned approaches include generator-specific discriminators \cite{grover},
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:17:feature-augmented transformers for cross-domain transfer \cite{feat_aug_transformer},
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:18:and disentangled representations for cross-generator generalization \cite{generator_barrier}.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:19:Robustness analyses show that paraphrase attacks severely degrade detectors \cite{reliable_detection,paraphrase_evades},
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:20:though detection remains information-theoretically feasible whenever human and machine distributions are distinguishable \cite{detection_possibilities}.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:21:\cite{jawahar_survey} and \cite{release_strategies} provide broader surveys.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:25:Our reference-model entropy features are functionally NLL-based out-of-distribution scores \cite{ood_baseline}, drawing on the same signal backbone as DetectGPT and Binoculars.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:31:\cite{curse_of_recursion} prove that iterative retraining causes irreversible distribution tail loss across VAEs, GMMs, and LLMs.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:32:\cite{strong_model_collapse} show that even minimal synthetic data fractions suffice to trigger collapse,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:33:\cite{self_consuming_mad} characterize precision--diversity trade-offs in autophagous loops,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:34:and \cite{model_collapse_avoidable} demonstrate that data accumulation (rather than replacement) mitigates the effect.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:39:\cite{broken_telephone} analyze LLM paraphrasing and translation chains, showing that information distortion accumulates with depth and outputs converge toward attractor states---critically, the semantic-preservation constraint of paraphrasing bounds depth-distinguishable classes to approximately three.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:40:\cite{markovian_chains} formalize this convergence, proving that iterative rephrasing chains either collapse to small cycle sets or continue producing novel sentences depending on temperature and initialization.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:47:\cite{curious_decline} quantify lexical, syntactic, and semantic diversity loss across recursive fine-tuning iterations, finding particularly severe decline for creative tasks---the closest antecedent to our work, though they study training-loop effects rather than inference-chain drift and do not formulate depth estimation.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:48:\cite{writing_diversity} show that LLM-assisted writing reduces inter-author diversity,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:49:while \cite{mapping_llm_science} and \cite{monitoring_ai_review} estimate that 7--17\% of scientific papers and peer reviews contain substantial LLM-modified content.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:50:\cite{nucleus_sampling} characterize neural text degeneration, proposing nucleus sampling whose truncation behavior shapes the distributional properties our features capture.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:53:Our surface features (type-token ratio, hapax ratio) are essentially stylometric, drawing on a long tradition of computational stylometry \cite{stamatatos_survey,koppel_authorship}.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:54:\cite{uchendu_attribution} extend authorship attribution to neural text generator identification;
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:60:\cite{ccnet} use language model perplexity for quality filtering,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:61:\cite{dsir} apply importance resampling in n-gram feature space,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:62:and \cite{qurating} employ LLM pairwise judgments for multi-dimensional quality assessment.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:66:\cite{watermark_llm} embed statistical signals via green-list token biasing,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:67:\cite{synthid_text} deploy production-scale watermarking,
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:68:and \cite{aaronson_watermark} propose pseudorandom function-based marking.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:69:However, \cite{chainwash} demonstrate that multi-step rewriting chains reduce watermark detectability from 87.9\% to 4.86\% within five hops, motivating watermark-free approaches.
artifacts/_project/paper/_backup/related_work_2ce9dd.tex:71:Methodologically, our probability-based features also connect to membership inference \cite{min_k_percent}, which analyzes token probability distributions for training set membership rather than generation depth.
artifacts/_project/paper/_backup/discussion_d3a579.tex:12:Reference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \cite{detectgpt}, GLTR \cite{gltr}, and Binoculars \cite{binoculars}.
artifacts/_project/paper/_backup/discussion_d3a579.tex:14:This connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \cite{ood_baseline}.
artifacts/_project/paper/_backup/discussion_d3a579.tex:21:Finer-grained depth distinctions may be achievable for non-paraphrastic chains (unlike paraphrastic chains, which converge within $\sim$3 steps \cite{broken_telephone}), but the three-class scheme already captures the practically relevant boundaries.
artifacts/_project/paper/_backup/discussion_d3a579.tex:27:The dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \cite{self_consuming_mad}.
artifacts/_project/paper/_backup/discussion_d3a579.tex:30:Our results relate to, but are distinct from, model collapse \cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:5:Estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:8:Existing detectors \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:17:Concurrent work on iterative paraphrasing chains \cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:21:Our central empirical finding is \emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.
artifacts/_project/paper/_backup/discussion_c98572.tex:19:The dominant factor is data quantity, not depth composition---a result consistent with scaling-law findings that emphasize the primacy of data volume \cite{self_consuming_mad}.
artifacts/_project/paper/_backup/discussion_c98572.tex:22:Our results relate to, but are distinct from, model collapse \cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.
artifacts/_project/paper/_backup/method_e59d28.tex:9:[Omitted long matching line]
artifacts/_project/paper/_backup/method_e59d28.tex:16:[Omitted long matching line]
artifacts/_project/paper/_backup/method_e59d28.tex:32:The choice of reference model is not critical: replacing Pythia-410M with OLMo-2-1B or Qwen3-0.6B as alternative reference models yields comparable cross-generator performance (LOGO macro-F1 0.80--0.82), indicating that the features capture properties of the \emph{text} rather than artifacts of a specific reference model. This parallels findings in perplexity-based detection, where reference-model choice has limited impact \cite{detectgpt,ood_baseline}.
artifacts/_project/paper/_backup/method_e59d28.tex:37:    \item \textbf{TTR}: type-token ratio (unique tokens / total tokens), a standard lexical diversity measure \cite{curious_decline}.
artifacts/_project/paper/_backup/method_e59d28.tex:43:[Omitted long matching line]
artifacts/_project/paper/_backup/method_e59d28.tex:58:[Omitted long matching line]
artifacts/_project/paper/_backup/method_01fe38.tex:16:We construct generation chains using six generators spanning three model families: \textbf{Pythia} (2.8B, 1B) \cite{placeholder}, \textbf{OLMo} (OLMo-2-1B) \cite{placeholder}, and \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{placeholder}.
artifacts/_project/paper/_backup/method_01fe38.tex:61:We use XGBoost \cite{placeholder} as the classifier throughout.
artifacts/_project/paper/_backup/method_01fe38.tex:73:We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \cite{placeholder}, Binoculars \cite{placeholder}, and LD-Score \cite{placeholder}.
artifacts/_project/paper/introduction.tex:5:Estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.
artifacts/_project/paper/introduction.tex:8:Existing detectors \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.
artifacts/_project/paper/introduction.tex:18:Concurrent work on iterative paraphrasing chains \cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.
artifacts/_project/paper/introduction.tex:23:We characterize a \emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.
artifacts/_project/paper/results.tex:60:To test whether the ordinal structure of the 3-class depth label provides additional discriminative power, we compare CORAL ordinal regression \cite{coral_ordinal} and Frank-Hall ordinal reduction \cite{frank_hall_ordinal} against the standard multiclass XGBoost classifier under the same LOGO protocol.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "82757a76-a83e-4e6e-822a-3dba5f723957",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:7:Methods for distinguishing human-written from machine-generated text have evolved from statistical tests on token-level distributions \\cite{gltr,grover,release_strategies} to zero-shot approaches exploiting reference-model likelihoods \\cite{detectgpt,fast_detectgpt,binoculars,dna_gpt} and learned classifiers over linguistic features \\cite{feat_aug_transformer,reliable_detection,ld_score}.\nartifacts/_project/paper/related_work.tex:12:Recent efforts extend detection to multi-class settings: \\citet{beyond_binary} propose role recognition and involvement measurement to distinguish collaborative human-LLM generation scenarios, and the SemEval-2024 shared task \\cite{semeval2024_task8} evaluates multi-generator attribution across domains and languages.\nartifacts/_project/paper/related_work.tex:16:Our reference-model entropy features are functionally NLL-based out-of-distribution scores \\cite{ood_baseline}; the contribution is not a new detection method but the task formulation (ordinal depth estimation) and the empirical finding that combining drifting and stationary features yields consistent cross-generator performance.\nartifacts/_project/paper/related_work.tex:42:Declining lexical diversity in LLM-generated text is documented in both training \\cite{curious_decline} and deployment \\cite{writing_diversity} settings.\nartifacts/_project/paper/related_work.tex:45:These features are classical stylometric measures with a long history in authorship attribution \\cite{stamatatos_survey,koppel_authorship}.\nartifacts/_project/paper/related_work.tex:57:An alternative approach is proactive provenance through watermarking \\cite{watermark_llm,synthid_text,aaronson_watermark}, where identifiable patterns are embedded during generation.\nartifacts/_project/paper/appendix_qlora.tex:1:To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \\cite{qlora}.\nartifacts/_project/paper/discussion.tex:13:Reference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \\cite{detectgpt}, GLTR \\cite{gltr}, and Binoculars \\cite{binoculars}.\nartifacts/_project/paper/discussion.tex:15:This connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \\cite{ood_baseline}.\nartifacts/_project/paper/discussion.tex:29:Unlike paraphrastic chains, which converge within ${\\sim}$3 steps \\cite{broken_telephone}, non-paraphrastic continuation chains retain some signal at gen-4 (F1\\,=\\,0.423), but the gen-2/gen-3 boundary remains unresolvable with surface and entropy features alone.\nartifacts/_project/paper/discussion.tex:46:The dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \\cite{self_consuming_mad}.\nartifacts/_project/paper/discussion.tex:49:Our results relate to, but are distinct from, model collapse \\cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.\nartifacts/_project/paper/method.tex:16:We construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nartifacts/_project/paper/method.tex:49:    The 90th percentile threshold follows standard practice in heavy-tail analysis \\cite{ood_baseline}; sensitivity analysis confirms stable classification (F1 variation ${<}$0.3\\,pp) across thresholds from the 85th to 95th percentile.\nartifacts/_project/paper/method.tex:72:We use XGBoost \\cite{xgboost} as the classifier throughout.\nartifacts/_project/paper/method.tex:78:We evaluated two ordinal-specific methods (CORAL \\cite{coral_ordinal}, Frank-Hall ordinal ensemble \\cite{frank_hall_ordinal}); neither significantly outperforms multiclass XGBoost (3-class LOGO F1 0.771--0.793 vs.\\ 0.789, CIs overlapping), confirming that with only three ordinal levels, ordinal structure provides minimal additional benefit.\nartifacts/_project/paper/method.tex:90:We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:7:\\cite{gltr} use token rank histograms under a reference model,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:8:\\cite{detectgpt} identify machine text through negative log-probability curvature,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:9:and \\cite{fast_detectgpt} accelerate this via conditional probability curvature.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:10:\\cite{binoculars} contrast perplexity ratios between two similar models,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:11:while \\cite{dna_gpt} measure n-gram divergence after re-generation.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:13:\\cite{ld_score} introduce character-distribution signatures orthogonal to perplexity,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:14:\\cite{intrinsic_dimension} leverage embedding-space intrinsic dimensionality,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:15:and \\cite{diveye} capture token surprisal diversity patterns.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:16:Learned approaches include generator-specific discriminators \\cite{grover},\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:17:feature-augmented transformers for cross-domain transfer \\cite{feat_aug_transformer},\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:18:and disentangled representations for cross-generator generalization \\cite{generator_barrier}.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:19:Robustness analyses show that paraphrase attacks severely degrade detectors \\cite{reliable_detection,paraphrase_evades},\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:20:though detection remains information-theoretically feasible whenever human and machine distributions are distinguishable \\cite{detection_possibilities}.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:21:\\cite{jawahar_survey} and \\cite{release_strategies} provide broader surveys.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:25:Our reference-model entropy features are functionally NLL-based out-of-distribution scores \\cite{ood_baseline}, drawing on the same signal backbone as DetectGPT and Binoculars.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:31:\\cite{curse_of_recursion} prove that iterative retraining causes irreversible distribution tail loss across VAEs, GMMs, and LLMs.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:32:\\cite{strong_model_collapse} show that even minimal synthetic data fractions suffice to trigger collapse,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:33:\\cite{self_consuming_mad} characterize precision--diversity trade-offs in autophagous loops,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:34:and \\cite{model_collapse_avoidable} demonstrate that data accumulation (rather than replacement) mitigates the effect.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:39:\\cite{broken_telephone} analyze LLM paraphrasing and translation chains, showing that information distortion accumulates with depth and outputs converge toward attractor states---critically, the semantic-preservation constraint of paraphrasing bounds depth-distinguishable classes to approximately three.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:40:\\cite{markovian_chains} formalize this convergence, proving that iterative rephrasing chains either collapse to small cycle sets or continue producing novel sentences depending on temperature and initialization.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:47:\\cite{curious_decline} quantify lexical, syntactic, and semantic diversity loss across recursive fine-tuning iterations, finding particularly severe decline for creative tasks---the closest antecedent to our work, though they study training-loop effects rather than inference-chain drift and do not formulate depth estimation.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:48:\\cite{writing_diversity} show that LLM-assisted writing reduces inter-author diversity,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:49:while \\cite{mapping_llm_science} and \\cite{monitoring_ai_review} estimate that 7--17\\% of scientific papers and peer reviews contain substantial LLM-modified content.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:50:\\cite{nucleus_sampling} characterize neural text degeneration, proposing nucleus sampling whose truncation behavior shapes the distributional properties our features capture.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:53:Our surface features (type-token ratio, hapax ratio) are essentially stylometric, drawing on a long tradition of computational stylometry \\cite{stamatatos_survey,koppel_authorship}.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:54:\\cite{uchendu_attribution} extend authorship attribution to neural text generator identification;\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:60:\\cite{ccnet} use language model perplexity for quality filtering,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:61:\\cite{dsir} apply importance resampling in n-gram feature space,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:62:and \\cite{qurating} employ LLM pairwise judgments for multi-dimensional quality assessment.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:66:\\cite{watermark_llm} embed statistical signals via green-list token biasing,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:67:\\cite{synthid_text} deploy production-scale watermarking,\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:68:and \\cite{aaronson_watermark} propose pseudorandom function-based marking.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:69:However, \\cite{chainwash} demonstrate that multi-step rewriting chains reduce watermark detectability from 87.9\\% to 4.86\\% within five hops, motivating watermark-free approaches.\nartifacts/_project/paper/_backup/related_work_2ce9dd.tex:71:Methodologically, our probability-based features also connect to membership inference \\cite{min_k_percent}, which analyzes token probability distributions for training set membership rather than generation depth.\nartifacts/_project/paper/_backup/discussion_d3a579.tex:12:Reference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \\cite{detectgpt}, GLTR \\cite{gltr}, and Binoculars \\cite{binoculars}.\nartifacts/_project/paper/_backup/discussion_d3a579.tex:14:This connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \\cite{ood_baseline}.\nartifacts/_project/paper/_backup/discussion_d3a579.tex:21:Finer-grained depth distinctions may be achievable for non-paraphrastic chains (unlike paraphrastic chains, which converge within $\\sim$3 steps \\cite{broken_telephone}), but the three-class scheme already captures the practically relevant boundaries.\nartifacts/_project/paper/_backup/discussion_d3a579.tex:27:The dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \\cite{self_consuming_mad}.\nartifacts/_project/paper/_backup/discussion_d3a579.tex:30:Our results relate to, but are distinct from, model collapse \\cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:5:Estimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:8:Existing detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:17:Concurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:21:Our central empirical finding is \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nartifacts/_project/paper/_backup/discussion_c98572.tex:19:The dominant factor is data quantity, not depth composition---a result consistent with scaling-law findings that emphasize the primacy of data volume \\cite{self_consuming_mad}.\nartifacts/_project/paper/_backup/discussion_c98572.tex:22:Our results relate to, but are distinct from, model collapse \\cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.\nartifacts/_project/paper/_backup/method_e59d28.tex:9:[Omitted long matching line]\nartifacts/_project/paper/_backup/method_e59d28.tex:16:[Omitted long matching line]\nartifacts/_project/paper/_backup/method_e59d28.tex:32:The choice of reference model is not critical: replacing Pythia-410M with OLMo-2-1B or Qwen3-0.6B as alternative reference models yields comparable cross-generator performance (LOGO macro-F1 0.80--0.82), indicating that the features capture properties of the \\emph{text} rather than artifacts of a specific reference model. This parallels findings in perplexity-based detection, where reference-model choice has limited impact \\cite{detectgpt,ood_baseline}.\nartifacts/_project/paper/_backup/method_e59d28.tex:37:    \\item \\textbf{TTR}: type-token ratio (unique tokens / total tokens), a standard lexical diversity measure \\cite{curious_decline}.\nartifacts/_project/paper/_backup/method_e59d28.tex:43:[Omitted long matching line]\nartifacts/_project/paper/_backup/method_e59d28.tex:58:[Omitted long matching line]\nartifacts/_project/paper/_backup/method_01fe38.tex:16:We construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{placeholder}, \\textbf{OLMo} (OLMo-2-1B) \\cite{placeholder}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{placeholder}.\nartifacts/_project/paper/_backup/method_01fe38.tex:61:We use XGBoost \\cite{placeholder} as the classifier throughout.\nartifacts/_project/paper/_backup/method_01fe38.tex:73:We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{placeholder}, Binoculars \\cite{placeholder}, and LD-Score \\cite{placeholder}.\nartifacts/_project/paper/introduction.tex:5:Estimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nartifacts/_project/paper/introduction.tex:8:Existing detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nartifacts/_project/paper/introduction.tex:18:Concurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nartifacts/_project/paper/introduction.tex:23:We characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nartifacts/_project/paper/results.tex:60:To test whether the ordinal structure of the 3-class depth label provides additional discriminative power, we compare CORAL ordinal regression \\cite{coral_ordinal} and Frank-Hall ordinal reduction \\cite{frank_hall_ordinal} against the standard multiclass XGBoost classifier under the same LOGO protocol.",
    "numLines": 77
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me analyze each check item:

## 1. Anonymization Check
- Author: `\author{Anonymous}` ✅
- No GitHub URLs found in any .tex files
- No personal names, institutions, or acknowledgements found
- No URLs found that could de-anonymize
- The only URL in .bib is `https://scottaaronson.blog/?p=6823` (Aaronson watermark reference) and `https://openreview.net/forum?id=OOgsAZdFOt` (paper URL) - these are citation URLs, not deanonymizing


## 2. Page Count Check
Now I'm tallying up the line counts across the main sections to verify we're within the 8-page limit. The abstract, introduction, related work, methods, results, discussion, and conclusion sections add up to 346 lines, while the limitations and ethics sections don't count toward the page restriction.

Given that ACL format typically runs 60-70 lines per page and the results section has several tables that take up additional space, I'm estimating we're sitting right around 7-8 pages—which is tight and worth flagging.

All the required sections are in place: abstract, introduction, related work, method, results, discussion, conclusion, plus the limitations and ethics statement. Now I need to verify that all the citations in the text actually have corresponding entries in the bibliography file. Now I'm mapping out the additional detection methods and baselines, including watermarking approaches and ordinal regression techniques, while cross-referencing which papers are actually cited in the bibliography. I'm verifying that all the bibliography entries are properly cited throughout the document. Going through the list, qlora and munir_looking_glass are both accounted for, and dna_gpt and model_collapse_avoidable check out as well. The backup files with placeholder citations aren't being included in the main submission, so those won't cause issues. Now I'm looking at the appendix structure, which has eight sections.

covering everything from length confound analysis through human-edit robustness testing. The document is formatted correctly for ACL/EMNLP submission with the proper document class and bibliography setup.

Now I'm checking for potential issues in the submission package. The `acl` package should handle the bibliography style automatically, so that's fine. I need to flag that backup files in the `_backup/` directory shouldn't be included in the final submission. There's also an incomplete reference to an appendix section on sampling sensitivity analysis that needs to be verified.

Looking at the figure references, I should confirm that `fig1_differential_response.pdf` and `fig3_baseline_comparison.png` actually exist in the chart directory, since the paper references them. The conclusion's statement about releasing code and data upon publication is acceptable for an anonymous submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "ab81bd1d-4627-48b0-9786-81f0678ada6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPdcSoMaj2V1yoVfyjesWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15938,
      "cache_read_input_tokens": 51590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15938
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

_source line 60_

Let me check for figure files and verify cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "d06ad938-6856-4dd8-a6f5-50dcb3b33e13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPdcSoMaj2V1yoVfyjesWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15938,
      "cache_read_input_tokens": 51590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15938
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

_source line 61_

<details open><summary>🔧 Tool call — Glob · `toolu_01ET4qKdh1uwdHpS2fs39Dkp`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "bf6224f8-baf4-4d41-867f-25892b142053",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPdcSoMaj2V1yoVfyjesWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15938,
      "cache_read_input_tokens": 51590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15938
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

_source line 62 · 2026-05-16T03:06:46.355Z_

<details><summary>↩ Tool result · `toolu_01ET4qKdh1uwdHpS2fs39Dkp`</summary>

```text
artifacts/_project/chart/fig1_differential_response.pdf
artifacts/_project/chart/fig2_logo_performance.png
artifacts/_project/chart/fig3_baseline_comparison.png
artifacts/_project/chart/fig4_downstream_negative.pdf
artifacts/_project/chart/fig4_downstream_negative.png
artifacts/_project/chart/fig4_downstream_negative_20bbd0.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "a3be00ab-ed3e-4948-9152-3e847248fd3e",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/chart/fig1_differential_response.pdf",
      "artifacts/_project/chart/fig2_logo_performance.png",
      "artifacts/_project/chart/fig3_baseline_comparison.png",
      "artifacts/_project/chart/fig4_downstream_negative.pdf",
      "artifacts/_project/chart/fig4_downstream_negative.png",
      "artifacts/_project/chart/fig4_downstream_negative_20bbd0.pdf"
    ],
    "durationMs": 6,
    "numFiles": 6,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Grep · `toolu_01PmYVhqMS2zcQLSLFepBmf7`</summary>

```json
{
  "pattern": "\\\\includegraphics",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "08079871-7aea-4aeb-bbdd-327a13cdbe9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPdcSoMaj2V1yoVfyjesWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15938,
      "cache_read_input_tokens": 51590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15938
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

_source line 64 · 2026-05-16T03:06:47.165Z_

<details><summary>↩ Tool result · `toolu_01PmYVhqMS2zcQLSLFepBmf7`</summary>

```text
artifacts/_project/paper/results.tex:75:\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
artifacts/_project/paper/results.tex:122:\includegraphics[width=\columnwidth]{fig3_baseline_comparison.png}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "eb2d310f-ab20-43ca-8f91-0c0a2232aee5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/results.tex:75:\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\nartifacts/_project/paper/results.tex:122:\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.png}",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Grep · `toolu_013u2i3EhSUZQ98sZrq4XEDu`</summary>

```json
{
  "pattern": "\\\\ref\\{([^}]+)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "b987d166-cff7-4038-aa6d-d3c587266725",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPdcSoMaj2V1yoVfyjesWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15938,
      "cache_read_input_tokens": 51590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15938
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

_source line 66 · 2026-05-16T03:06:48.231Z_

<details><summary>↩ Tool result · `toolu_013u2i3EhSUZQ98sZrq4XEDu`</summary>

```text
artifacts/_project/paper/related_work.tex:14:Even when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently.
artifacts/_project/paper/appendix_qlora.tex:26:The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
artifacts/_project/paper/appendix_confusion_matrix.tex:1:Table~\ref{tab:confusion} reports the aggregated confusion matrix from 6-generator leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
artifacts/_project/paper/appendix_human_edit.tex:1:To assess whether depth features are robust to post-generation human editing, we simulate two editing scenarios on the full generation chain dataset and re-evaluate the 6-generator LOGO pipeline (Table~\ref{tab:human-edit}).
artifacts/_project/paper/appendix_lofo.tex:1:We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
artifacts/_project/paper/discussion.tex:5:Distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\S\ref{sec:results-differential}).
artifacts/_project/paper/discussion.tex:9:Sampling ablation supports this account: depth signal is robust to moderate sampling variation (F1 range ${\leq}0.3$\,pp for $t \in [0.5, 0.7]$) but degrades at extreme temperatures ($t = 1.0$, $-6$\,pp), consistent with shape features being determined by the sampling mechanism (Appendix~\ref{app:sampling-sensitivity}).
artifacts/_project/paper/discussion.tex:21:Whether this understanding translates to improved curation outcomes remains an open question (\S\ref{sec:results-downstream}).
artifacts/_project/paper/discussion.tex:22:Cross-model chain evaluation (\S\ref{sec:results-classification}) confirms that depth signal persists even when chains involve heterogeneous generators, supporting applicability to realistic web-contamination scenarios.
artifacts/_project/paper/discussion.tex:25:Extending to 5-class depth estimation (gen-0 through gen-4) reduces LOGO macro F1 from 0.789 to 0.501, a drop of 0.288 (Appendix~\ref{app:finer-depth}).
artifacts/_project/paper/discussion.tex:30:End-to-end fine-tuning (QLoRA on Qwen3-0.6B) raises the 3-class ceiling to F1\,=\,0.905 (+11.6\,pp over handcrafted features; Appendix~\ref{app:qlora}), confirming that raw embeddings contain exploitable depth signal beyond summary statistics.
artifacts/_project/paper/discussion.tex:40:LLM rephrasing presents a different challenge---3-class degradation is modest ($-3.4$\,pp), but binary F1 drops 6.3\,pp, indicating that systematic distributional manipulation erodes depth signal more effectively than surface noise (Appendix~\ref{app:human-edit}).
artifacts/_project/paper/discussion.tex:44:Depth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\S\ref{sec:results-downstream}).
artifacts/_project/paper/discussion.tex:70:Overall LOGO F1 varies by only 0.013 across three cross-family reference models (0.803--0.816; Table~\ref{tab:cross-ref}), and entropy drift direction is consistently negative for all three, confirming that the differential depth response is a property of recursive generation itself.
artifacts/_project/paper/discussion.tex:74:Preliminary experiments with instruction-tuned models show substantially weaker depth fingerprints: OLMo-2-1B-Instruct achieves 3-class LOGO F1\,=\,0.338 (vs.\ 0.764 for base OLMo-2-1B), and Qwen3-0.6B with chat template yields F1\,=\,0.667 (vs.\ 0.816 for the base model under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\ref{tab:logo-results}).
artifacts/_project/paper/method.tex:11:Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
artifacts/_project/paper/method.tex:22:We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
artifacts/_project/paper/method.tex:34:This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\S\ref{sec:results-differential}).
artifacts/_project/paper/method.tex:40:Although Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).
artifacts/_project/paper/method.tex:62:As shown in \S\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.
artifacts/_project/paper/method.tex:75:Baseline detectors (\S\ref{sec:results-baselines}) use the same XGBoost framework with $n\_\text{estimators}{=}100$ and $\max\_\text{depth}{=}3$ to avoid overfitting their single-feature input.
artifacts/_project/paper/method.tex:77:Alternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.
artifacts/_project/paper/method.tex:86:We report six pairwise comparisons in \S\ref{sec:results-baselines}; applying Bonferroni correction ($\alpha_{\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.
artifacts/_project/paper/method.tex:87:Feature--depth correlations (\S\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.
artifacts/_project/paper/limitations.tex:6:Preliminary instruct experiments show substantial depth-signal degradation: OLMo-2-1B-Instruct drops to 3-class LOGO F1\,=\,0.338 (vs.\ 0.764 for base OLMo-2-1B) and Qwen3-0.6B with chat template to F1\,=\,0.667 (vs.\ 0.816 base under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\ref{tab:logo-results}).
artifacts/_project/paper/limitations.tex:15:We evaluate three prompt types (continuation, elaboration, rewriting; Appendix~\ref{app:prompt-type}) but all share the same Pythia-2.8B generator.
artifacts/_project/paper/limitations.tex:18:Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm that depth signal persists under generator heterogeneity (3-class F1\,=\,0.809, binary F1\,=\,0.764), though the six generators tested represent a controlled laboratory setting rather than the full diversity of web-scale contamination.
artifacts/_project/paper/limitations.tex:19:Simulated human editing (\S\ref{sec:discussion}) suggests graceful degradation under casual editing, but the gap between simulated token replacement and real-world human post-processing remains untested.
artifacts/_project/paper/limitations.tex:21:The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\S\ref{sec:results-differential}) suggest the phenomenon is not reference-specific.
artifacts/_project/paper/limitations.tex:24:The negative downstream result (\S\ref{sec:results-downstream}) is evaluated on causal language modeling only.
artifacts/_project/paper/limitations.tex:27:Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \in [0.5, 0.7]$, F1 range ${\leq}0.3$\,pp) but substantial degradation at $t{=}1.0$ ($-6$\,pp), indicating that depth fingerprinting assumes standard decoding regimes.
artifacts/_project/paper/limitations.tex:29:We use 3-class granularity (gen-0\,/\,gen-1\,/\,gen-2+). A 5-class evaluation (Appendix~\ref{app:finer-depth}) yields LOGO F1\,$\approx$\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.
artifacts/_project/paper/appendix_length.tex:22:We subsample the dataset so that word-count distributions are equalized across depth classes, then retrain the 3-class XGBoost classifier (\S\ref{sec:results-classification}).
artifacts/_project/paper/_backup/discussion_d3a579.tex:5:Distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\S\ref{sec:results-differential}).
artifacts/_project/paper/_backup/discussion_d3a579.tex:25:Depth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\S\ref{sec:results-downstream}).
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:16:When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---confidence intervals spanning 0.41--0.82 in macro-F1 (\S\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:39:\S\ref{sec:related} surveys related work on text detection, model collapse, and data quality.
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:40:\S\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:41:\S\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.
artifacts/_project/paper/_backup/introduction_4bbcfd.tex:42:\S\ref{sec:discussion} discusses limitations and future directions.
artifacts/_project/paper/_backup/discussion_c98572.tex:5:We observe that distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\S\ref{sec:results-differential}).
artifacts/_project/paper/_backup/discussion_c98572.tex:17:The downstream experiment (\S\ref{sec:results-downstream}) demonstrates that depth-aware curation does not improve language model quality over random subsampling at equal sample count.
artifacts/_project/paper/_backup/limitations_69ebec.tex:15:The negative downstream result (\S\ref{sec:results-downstream}) is evaluated on causal language modeling only.
artifacts/_project/paper/_backup/limitations_b3d194.tex:15:The negative downstream result (\S\ref{sec:results-downstream}) is evaluated on causal language modeling only.
artifacts/_project/paper/_backup/results_b30771.tex:4:We evaluate depth fingerprinting along four axes: cross-generator classification (\S\ref{sec:results-classification}), differential depth response of individual features (\S\ref{sec:results-differential}), comparison with existing detection baselines (\S\ref{sec:results-baselines}), and downstream utility for data curation (\S\ref{sec:results-downstream}).
artifacts/_project/paper/_backup/results_b30771.tex:9:Table~\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\,/\,gen-1\,/\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.
artifacts/_project/paper/_backup/results_b30771.tex:11:The 7-feature ensemble achieves LOGO F1\,=\,0.789, significantly outperforming all single-detector baselines ($p<0.001$; \S\ref{sec:results-baselines}).
artifacts/_project/paper/_backup/results_b30771.tex:26:Length-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\Delta$\,=\,+0.041), ruling out length as a confound (Appendix~\ref{app:length}).
artifacts/_project/paper/_backup/results_b30771.tex:58:Individual-level Spearman correlations with depth confirm the split (Figure~\ref{fig:feature-drift}):
artifacts/_project/paper/_backup/results_b30771.tex:63:Table~\ref{tab:ablation} reports ablation results.
artifacts/_project/paper/_backup/results_b30771.tex:94:We repurpose four existing detection scores as ordinal depth predictors by training the same ordinal classifier on each score as a single feature, using identical LOGO evaluation (Figure~\ref{fig:baseline-ci}).
artifacts/_project/paper/_backup/results_b30771.tex:114:The ensemble outperforms all baselines in mean F1: +3.9\,pp over Avg-LogProb ($p < 0.001$, $\Delta$ CI [3.4, 4.4]), +7.7\,pp over LD-Score, +17.1\,pp over FastDetectGPT, and +21.9\,pp over Binoculars (Table~\ref{tab:baselines}).
artifacts/_project/paper/_backup/results_b30771.tex:127:We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
artifacts/_project/paper/_backup/method_01fe38.tex:11:Depths beyond 2 are merged into a single $2{+}$ class, as preliminary experiments showed diminishing discriminability at higher depths---consistent with the monotonic convergence of distributional features reported in \S\ref{sec:results}.
artifacts/_project/paper/_backup/method_01fe38.tex:51:As shown in \S\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.
artifacts/_project/paper/appendix_classifier.tex:3:in place of XGBoost (Table~\ref{tab:alt-classifier}).
artifacts/_project/paper/appendix_classifier.tex:34:To assess robustness to decoding hyperparameters, we regenerate the full chain set under three sampling configurations and re-evaluate the 3-class LOGO pipeline (Table~\ref{tab:sampling-ablation}).
artifacts/_project/paper/appendix_classifier.tex:54:This is consistent with the hypothesis that depth features are shaped by the sampling mechanism (\S\ref{sec:discussion}): elevated temperature injects sufficient randomness to flatten the distributional drift that accumulates across generation steps, effectively masking the depth signal.
artifacts/_project/paper/introduction.tex:17:When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\S\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.
artifacts/_project/paper/introduction.tex:39:\S\ref{sec:related} surveys related work on text detection, model collapse, and data quality.
artifacts/_project/paper/introduction.tex:40:\S\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.
artifacts/_project/paper/introduction.tex:41:\S\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.
artifacts/_project/paper/introduction.tex:42:\S\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.
artifacts/_project/paper/appendix_finer_depth.tex:1:We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \S\ref{sec:method}.
artifacts/_project/paper/appendix_finer_depth.tex:51:At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), confirming that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
artifacts/_project/paper/results.tex:4:We evaluate depth fingerprinting along four axes: cross-generator classification (\S\ref{sec:results-classification}), differential depth response of individual features (\S\ref{sec:results-differential}), comparison with existing detection baselines (\S\ref{sec:results-baselines}), and downstream utility for data curation (\S\ref{sec:results-downstream}).
artifacts/_project/paper/results.tex:9:Table~\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\,/\,gen-1\,/\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.
artifacts/_project/paper/results.tex:11:The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.789 (Table~\ref{tab:logo-results}). Because gen-0 seed texts are shared across generators (\S\ref{sec:generation}), the gen-0 class F1 (0.94) may be inflated; we therefore report a leak-free binary evaluation (gen-1 vs.\ gen-2+, F1\,=\,0.723) as the primary metric in \S\ref{sec:results-baselines}.
artifacts/_project/paper/results.tex:34:Length-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\Delta$\,=\,+0.041), ruling out length as a confound (Appendix~\ref{app:length}).
artifacts/_project/paper/results.tex:80:Individual-level Spearman correlations with depth confirm the split (Figure~\ref{fig:feature-drift}):
artifacts/_project/paper/results.tex:85:Table~\ref{tab:ablation} reports ablation results.
artifacts/_project/paper/results.tex:92:All three reference models achieve comparable LOGO F1: Pythia-410M\,=\,0.803, OLMo-2-1B\,=\,0.807, Qwen3-0.6B\,=\,0.816 (spread 0.013; Table~\ref{tab:cross-ref}).
artifacts/_project/paper/results.tex:93:Entropy drift direction is consistently negative across all reference models (Table~\ref{tab:cross-ref}), confirming that the differential depth response is a property of recursive generation, not of the specific reference model used.
artifacts/_project/paper/results.tex:114:Leave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\_max showing the largest marginal impact despite modest split frequency (Appendix~\ref{app:lofo}).
artifacts/_project/paper/results.tex:128:Because gen-0 seed texts are shared across generators (\S\ref{sec:generation}), 3-class LOGO evaluation creates a train--test overlap for the gen-0 class.
artifacts/_project/paper/results.tex:129:We therefore report both 3-class and binary (gen-1 vs.\ gen-2+) results; the binary metric is the primary measure of depth discrimination (Table~\ref{tab:baselines}).
artifacts/_project/paper/results.tex:147:\caption{Depth classification under unified 6-gen LOGO evaluation. \textbf{3-class}: gen-0/gen-1/gen-2+ (gen-0 samples shared across generators; see \S\ref{sec:generation}). \textbf{Binary}: gen-1 vs.\ gen-2+ only, eliminating the gen-0 train--test overlap. Per-gen std measures cross-generator consistency of the binary metric. The 7-feature ensemble is the strongest single-model method on both metrics and matches the best multi-detector ensemble on binary F1.}
artifacts/_project/paper/results.tex:168:We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "5442fa98-0f12-4eec-aa4a-06759d459375",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/related_work.tex:14:Even when detection scores correlate with generation depth, they exhibit high cross-generator variance when repurposed as ordinal predictors (binary F1 from 0.52 to 0.71 across individual baselines; Table~\\ref{tab:baselines}), because each score captures a single distributional property that generalizes inconsistently.\nartifacts/_project/paper/appendix_qlora.tex:26:The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\\,=\\,0.259), consistent with the feature-level analysis in \\S\\ref{sec:discussion}.\nartifacts/_project/paper/appendix_confusion_matrix.tex:1:Table~\\ref{tab:confusion} reports the aggregated confusion matrix from 6-generator leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\\geq$ 2).\nartifacts/_project/paper/appendix_human_edit.tex:1:To assess whether depth features are robust to post-generation human editing, we simulate two editing scenarios on the full generation chain dataset and re-evaluate the 6-generator LOGO pipeline (Table~\\ref{tab:human-edit}).\nartifacts/_project/paper/appendix_lofo.tex:1:We complement the permutation importance analysis (\\S\\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\\Delta$ is the change relative to the full 7-feature ensemble (F1\\,=\\,0.789).\nartifacts/_project/paper/discussion.tex:5:Distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\\S\\ref{sec:results-differential}).\nartifacts/_project/paper/discussion.tex:9:Sampling ablation supports this account: depth signal is robust to moderate sampling variation (F1 range ${\\leq}0.3$\\,pp for $t \\in [0.5, 0.7]$) but degrades at extreme temperatures ($t = 1.0$, $-6$\\,pp), consistent with shape features being determined by the sampling mechanism (Appendix~\\ref{app:sampling-sensitivity}).\nartifacts/_project/paper/discussion.tex:21:Whether this understanding translates to improved curation outcomes remains an open question (\\S\\ref{sec:results-downstream}).\nartifacts/_project/paper/discussion.tex:22:Cross-model chain evaluation (\\S\\ref{sec:results-classification}) confirms that depth signal persists even when chains involve heterogeneous generators, supporting applicability to realistic web-contamination scenarios.\nartifacts/_project/paper/discussion.tex:25:Extending to 5-class depth estimation (gen-0 through gen-4) reduces LOGO macro F1 from 0.789 to 0.501, a drop of 0.288 (Appendix~\\ref{app:finer-depth}).\nartifacts/_project/paper/discussion.tex:30:End-to-end fine-tuning (QLoRA on Qwen3-0.6B) raises the 3-class ceiling to F1\\,=\\,0.905 (+11.6\\,pp over handcrafted features; Appendix~\\ref{app:qlora}), confirming that raw embeddings contain exploitable depth signal beyond summary statistics.\nartifacts/_project/paper/discussion.tex:40:LLM rephrasing presents a different challenge---3-class degradation is modest ($-3.4$\\,pp), but binary F1 drops 6.3\\,pp, indicating that systematic distributional manipulation erodes depth signal more effectively than surface noise (Appendix~\\ref{app:human-edit}).\nartifacts/_project/paper/discussion.tex:44:Depth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\\S\\ref{sec:results-downstream}).\nartifacts/_project/paper/discussion.tex:70:Overall LOGO F1 varies by only 0.013 across three cross-family reference models (0.803--0.816; Table~\\ref{tab:cross-ref}), and entropy drift direction is consistently negative for all three, confirming that the differential depth response is a property of recursive generation itself.\nartifacts/_project/paper/discussion.tex:74:Preliminary experiments with instruction-tuned models show substantially weaker depth fingerprints: OLMo-2-1B-Instruct achieves 3-class LOGO F1\\,=\\,0.338 (vs.\\ 0.764 for base OLMo-2-1B), and Qwen3-0.6B with chat template yields F1\\,=\\,0.667 (vs.\\ 0.816 for the base model under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\\ref{tab:logo-results}).\nartifacts/_project/paper/method.tex:11:Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\nartifacts/_project/paper/method.tex:22:We address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nartifacts/_project/paper/method.tex:34:This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\nartifacts/_project/paper/method.tex:40:Although Pythia-410M shares the GPT-NeoX architecture with two of the six generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by only 0.013 across Pythia, OLMo, and Qwen references).\nartifacts/_project/paper/method.tex:62:As shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\nartifacts/_project/paper/method.tex:75:Baseline detectors (\\S\\ref{sec:results-baselines}) use the same XGBoost framework with $n\\_\\text{estimators}{=}100$ and $\\max\\_\\text{depth}{=}3$ to avoid overfitting their single-feature input.\nartifacts/_project/paper/method.tex:77:Alternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\nartifacts/_project/paper/method.tex:86:We report six pairwise comparisons in \\S\\ref{sec:results-baselines}; applying Bonferroni correction ($\\alpha_{\\text{adj}} = 0.05/6 = 0.0083$), all remain significant at $p < 0.001$.\nartifacts/_project/paper/method.tex:87:Feature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\nartifacts/_project/paper/limitations.tex:6:Preliminary instruct experiments show substantial depth-signal degradation: OLMo-2-1B-Instruct drops to 3-class LOGO F1\\,=\\,0.338 (vs.\\ 0.764 for base OLMo-2-1B) and Qwen3-0.6B with chat template to F1\\,=\\,0.667 (vs.\\ 0.816 base under the 7-generator LOGO split that includes the instruct variant; the base-only split yields 0.824, Table~\\ref{tab:logo-results}).\nartifacts/_project/paper/limitations.tex:15:We evaluate three prompt types (continuation, elaboration, rewriting; Appendix~\\ref{app:prompt-type}) but all share the same Pythia-2.8B generator.\nartifacts/_project/paper/limitations.tex:18:Our primary evaluation uses single-generator chains; cross-model chains (\\S\\ref{sec:results-classification}) confirm that depth signal persists under generator heterogeneity (3-class F1\\,=\\,0.809, binary F1\\,=\\,0.764), though the six generators tested represent a controlled laboratory setting rather than the full diversity of web-scale contamination.\nartifacts/_project/paper/limitations.tex:19:Simulated human editing (\\S\\ref{sec:discussion}) suggests graceful degradation under casual editing, but the gap between simulated token replacement and real-world human post-processing remains untested.\nartifacts/_project/paper/limitations.tex:21:The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\\S\\ref{sec:results-differential}) suggest the phenomenon is not reference-specific.\nartifacts/_project/paper/limitations.tex:24:The negative downstream result (\\S\\ref{sec:results-downstream}) is evaluated on causal language modeling only.\nartifacts/_project/paper/limitations.tex:27:Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \\in [0.5, 0.7]$, F1 range ${\\leq}0.3$\\,pp) but substantial degradation at $t{=}1.0$ ($-6$\\,pp), indicating that depth fingerprinting assumes standard decoding regimes.\nartifacts/_project/paper/limitations.tex:29:We use 3-class granularity (gen-0\\,/\\,gen-1\\,/\\,gen-2+). A 5-class evaluation (Appendix~\\ref{app:finer-depth}) yields LOGO F1\\,$\\approx$\\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.\nartifacts/_project/paper/appendix_length.tex:22:We subsample the dataset so that word-count distributions are equalized across depth classes, then retrain the 3-class XGBoost classifier (\\S\\ref{sec:results-classification}).\nartifacts/_project/paper/_backup/discussion_d3a579.tex:5:Distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\\S\\ref{sec:results-differential}).\nartifacts/_project/paper/_backup/discussion_d3a579.tex:25:Depth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\\S\\ref{sec:results-downstream}).\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:16:When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---confidence intervals spanning 0.41--0.82 in macro-F1 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:39:\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:40:\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:41:\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\nartifacts/_project/paper/_backup/introduction_4bbcfd.tex:42:\\S\\ref{sec:discussion} discusses limitations and future directions.\nartifacts/_project/paper/_backup/discussion_c98572.tex:5:We observe that distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\\S\\ref{sec:results-differential}).\nartifacts/_project/paper/_backup/discussion_c98572.tex:17:The downstream experiment (\\S\\ref{sec:results-downstream}) demonstrates that depth-aware curation does not improve language model quality over random subsampling at equal sample count.\nartifacts/_project/paper/_backup/limitations_69ebec.tex:15:The negative downstream result (\\S\\ref{sec:results-downstream}) is evaluated on causal language modeling only.\nartifacts/_project/paper/_backup/limitations_b3d194.tex:15:The negative downstream result (\\S\\ref{sec:results-downstream}) is evaluated on causal language modeling only.\nartifacts/_project/paper/_backup/results_b30771.tex:4:We evaluate depth fingerprinting along four axes: cross-generator classification (\\S\\ref{sec:results-classification}), differential depth response of individual features (\\S\\ref{sec:results-differential}), comparison with existing detection baselines (\\S\\ref{sec:results-baselines}), and downstream utility for data curation (\\S\\ref{sec:results-downstream}).\nartifacts/_project/paper/_backup/results_b30771.tex:9:Table~\\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.\nartifacts/_project/paper/_backup/results_b30771.tex:11:The 7-feature ensemble achieves LOGO F1\\,=\\,0.789, significantly outperforming all single-detector baselines ($p<0.001$; \\S\\ref{sec:results-baselines}).\nartifacts/_project/paper/_backup/results_b30771.tex:26:Length-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\\Delta$\\,=\\,+0.041), ruling out length as a confound (Appendix~\\ref{app:length}).\nartifacts/_project/paper/_backup/results_b30771.tex:58:Individual-level Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):\nartifacts/_project/paper/_backup/results_b30771.tex:63:Table~\\ref{tab:ablation} reports ablation results.\nartifacts/_project/paper/_backup/results_b30771.tex:94:We repurpose four existing detection scores as ordinal depth predictors by training the same ordinal classifier on each score as a single feature, using identical LOGO evaluation (Figure~\\ref{fig:baseline-ci}).\nartifacts/_project/paper/_backup/results_b30771.tex:114:The ensemble outperforms all baselines in mean F1: +3.9\\,pp over Avg-LogProb ($p < 0.001$, $\\Delta$ CI [3.4, 4.4]), +7.7\\,pp over LD-Score, +17.1\\,pp over FastDetectGPT, and +21.9\\,pp over Binoculars (Table~\\ref{tab:baselines}).\nartifacts/_project/paper/_backup/results_b30771.tex:127:We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).\nartifacts/_project/paper/_backup/method_01fe38.tex:11:Depths beyond 2 are merged into a single $2{+}$ class, as preliminary experiments showed diminishing discriminability at higher depths---consistent with the monotonic convergence of distributional features reported in \\S\\ref{sec:results}.\nartifacts/_project/paper/_backup/method_01fe38.tex:51:As shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\nartifacts/_project/paper/appendix_classifier.tex:3:in place of XGBoost (Table~\\ref{tab:alt-classifier}).\nartifacts/_project/paper/appendix_classifier.tex:34:To assess robustness to decoding hyperparameters, we regenerate the full chain set under three sampling configurations and re-evaluate the 3-class LOGO pipeline (Table~\\ref{tab:sampling-ablation}).\nartifacts/_project/paper/appendix_classifier.tex:54:This is consistent with the hypothesis that depth features are shaped by the sampling mechanism (\\S\\ref{sec:discussion}): elevated temperature injects sufficient randomness to flatten the distributional drift that accumulates across generation steps, effectively masking the depth signal.\nartifacts/_project/paper/introduction.tex:17:When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nartifacts/_project/paper/introduction.tex:39:\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\nartifacts/_project/paper/introduction.tex:40:\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\nartifacts/_project/paper/introduction.tex:41:\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\nartifacts/_project/paper/introduction.tex:42:\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\nartifacts/_project/paper/appendix_finer_depth.tex:1:We evaluate finer-grained 5-class depth classification (gen-0 through gen-4) using the same 7-feature ensemble and LOGO protocol described in \\S\\ref{sec:method}.\nartifacts/_project/paper/appendix_finer_depth.tex:51:At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\\S\\ref{sec:results}), confirming that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.\nartifacts/_project/paper/results.tex:4:We evaluate depth fingerprinting along four axes: cross-generator classification (\\S\\ref{sec:results-classification}), differential depth response of individual features (\\S\\ref{sec:results-differential}), comparison with existing detection baselines (\\S\\ref{sec:results-baselines}), and downstream utility for data curation (\\S\\ref{sec:results-downstream}).\nartifacts/_project/paper/results.tex:9:Table~\\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.\nartifacts/_project/paper/results.tex:11:The 7-feature ensemble achieves 3-class LOGO F1\\,=\\,0.789 (Table~\\ref{tab:logo-results}). Because gen-0 seed texts are shared across generators (\\S\\ref{sec:generation}), the gen-0 class F1 (0.94) may be inflated; we therefore report a leak-free binary evaluation (gen-1 vs.\\ gen-2+, F1\\,=\\,0.723) as the primary metric in \\S\\ref{sec:results-baselines}.\nartifacts/_project/paper/results.tex:34:Length-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\\Delta$\\,=\\,+0.041), ruling out length as a confound (Appendix~\\ref{app:length}).\nartifacts/_project/paper/results.tex:80:Individual-level Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):\nartifacts/_project/paper/results.tex:85:Table~\\ref{tab:ablation} reports ablation results.\nartifacts/_project/paper/results.tex:92:All three reference models achieve comparable LOGO F1: Pythia-410M\\,=\\,0.803, OLMo-2-1B\\,=\\,0.807, Qwen3-0.6B\\,=\\,0.816 (spread 0.013; Table~\\ref{tab:cross-ref}).\nartifacts/_project/paper/results.tex:93:Entropy drift direction is consistently negative across all reference models (Table~\\ref{tab:cross-ref}), confirming that the differential depth response is a property of recursive generation, not of the specific reference model used.\nartifacts/_project/paper/results.tex:114:Leave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\\_max showing the largest marginal impact despite modest split frequency (Appendix~\\ref{app:lofo}).\nartifacts/_project/paper/results.tex:128:Because gen-0 seed texts are shared across generators (\\S\\ref{sec:generation}), 3-class LOGO evaluation creates a train--test overlap for the gen-0 class.\nartifacts/_project/paper/results.tex:129:We therefore report both 3-class and binary (gen-1 vs.\\ gen-2+) results; the binary metric is the primary measure of depth discrimination (Table~\\ref{tab:baselines}).\nartifacts/_project/paper/results.tex:147:\\caption{Depth classification under unified 6-gen LOGO evaluation. \\textbf{3-class}: gen-0/gen-1/gen-2+ (gen-0 samples shared across generators; see \\S\\ref{sec:generation}). \\textbf{Binary}: gen-1 vs.\\ gen-2+ only, eliminating the gen-0 train--test overlap. Per-gen std measures cross-generator consistency of the binary metric. The 7-feature ensemble is the strongest single-model method on both metrics and matches the best multi-detector ensemble on binary F1.}\nartifacts/_project/paper/results.tex:168:We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).",
    "numLines": 78
  }
}
```

</details>

---

### Assistant

_source line 67_

<details><summary>Logged reasoning block</summary>

```text
Now I need to do a thorough cross-reference of all \cite keys used in non-backup .tex files against the .bib entries.

Let me extract all unique cite keys from the non-backup .tex files and compare against .bib entries.

From the grep results, the cited keys in non-backup files are:
- mapping_llm_science, monitoring_ai_review, fast_detectgpt, binoculars, ld_score, detectgpt
- broken_telephone, markovian_chains, ood_baseline
- gltr, grover, release_strategies, dna_gpt, feat_aug_transformer, reliable_detection


- intrinsic_dimension, diveye, generator_barrier, wu_survey_2025, jawahar_survey
- beyond_binary, semeval2024_task8, paraphrase_evades, detection_possibilities
- uchendu_attribution, munir_looking_glass
- self_consuming_mad, curse_of_recursion, model_collapse_avoidable, strong_model_collapse
- curious_decline, writing_diversity, nucleus_sampling
- stamatatos_survey, koppel_authorship
- dsir, qurating, ccnet
- watermark_llm, synthid_text, aaronson_watermark, chainw
- ash, min_k_percent
- pythia, olmo, qwen3
- xgboost, coral_ordinal, frank_hall_ordinal, qlora

All entries are accounted for in the bibliography. Now I'm cross-checking which .bib entries haven't been cited yet—looking through detectgpt, gltr, dna_gpt, binoculars, fast_detectgpt, ld_score, feat_aug_transformer, reliable_detection, grover, release_strategies, ood_baseline, and a few others to see what's missing from the document.

After going through the full list, all 50 bibliography entries are actually cited. Now I need to verify that every `\ref` target in the document has a corresponding `\label` defined—checking sections like introduction, method, task, generation, and the related work subsections.

Looking at the labels I've found, they cover all the major sections and subsections, plus tables and figures throughout the appendix. Every reference target appears to have its matching label definition, so the document is internally consistent.

Now I'm checking which figures actually exist in the chart directory and whether they're being used in the paper. Two of the figures are referenced—the differential response comparison and baseline comparison plots—but there are also a couple of unused figures sitting in the directory that aren't called out anywhere, which is fine but worth keeping in mind.

For the page count, I'm tallying up the main body sections that count toward the 8-page limit: the abstract is quite brief, the introduction runs about 43 lines, related work is around 61 lines, the method section is substantial at 96 lines, results is the longest at 197 lines with embedded tables and figures, discussion takes up 87 lines, and conclusion is just 12 lines. The limitations section and other supplementary material don't count toward that limit.

Looking at the actual ACL format constraints—single column, 11pt font—I'm realizing the page estimate is tighter than I initially thought. With roughly 504 lines of text across the main sections, plus 5 tables and 2 figures, this is probably pushing 12 pages or more, which would exceed the 8-page limit depending on how the formatting shakes out.

Let me reconsider the template structure. The `\documentclass[11pt]{article}` with the ACL review package should be handling the two-column layout automatically. In that case, each page would fit around 100-110 lines total, bringing the estimate down to roughly 7-8 pages when accounting for the tables and figures. But this really needs to be verified by actually compiling the document to see where we stand.

Now I'll move on to creating the checklist, though I should also double-check the bibliography setup with the ACL package and natbib to make sure everything's configured correctly. I'm checking the anonymization more thoroughly—no author names, affiliations, or acknowledgments are present, and the code/data release statement is appropriately vague for review. The `_backup/` directory in the paper folder is a concern though, as it could leak information or cause compilation issues if submitted, so that needs to be excluded from the final submission package.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "b72c2bb1-729b-49e6-b30a-986f3e9e717d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158x9MzPD5chtpCxBPDxqgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8569,
      "cache_read_input_tokens": 67528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8569
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

_source line 68_

Now I have all the information needed. Let me extract the citation keys systematically to verify no mismatches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "08c01dee-6127-4a43-bafb-e47005551cd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158x9MzPD5chtpCxBPDxqgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8569,
      "cache_read_input_tokens": 67528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8569
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

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_01XnhPCwSVZ63zbwT1SnNudF`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -ohP '\\\\\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract all unique citation keys from non-backup .tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "99388cff-fb9a-4fa1-b18e-f3eb6cd6420c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158x9MzPD5chtpCxBPDxqgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8569,
      "cache_read_input_tokens": 67528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8569
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

_source line 70 · 2026-05-16T03:07:38.623Z_

<details><summary>↩ Tool result · `toolu_01XnhPCwSVZ63zbwT1SnNudF`</summary>

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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "bd6cbe7f-9b1a-4509-81f2-27dd16292f6d",
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

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_013KEUXAXDQDSQEhsVCaE32e`</summary>

```json
{
  "command": "grep -ohP '@\\w+\\{(\\w+),' references.bib | grep -ohP '\\{(\\w+),' | tr -d '{,' | sort -u",
  "description": "Extract all bib entry keys from references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "21df85b2-6929-4b54-9443-dbdb1b03b369",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158x9MzPD5chtpCxBPDxqgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8569,
      "cache_read_input_tokens": 67528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8569
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

_source line 72 · 2026-05-16T03:07:40.004Z_

<details><summary>↩ Tool result · `toolu_013KEUXAXDQDSQEhsVCaE32e`</summary>

```text
aaronson_watermark
beyond_binary
binoculars
broken_telephone
ccnet
chainwash
coral_ordinal
curious_decline
curse_of_recursion
detectgpt
detection_possibilities
diveye
dna_gpt
dsir
fast_detectgpt
feat_aug_transformer
frank_hall_ordinal
generator_barrier
gltr
grover
intrinsic_dimension
jawahar_survey
koppel_authorship
ld_score
mapping_llm_science
markovian_chains
min_k_percent
model_collapse_avoidable
monitoring_ai_review
munir_looking_glass
nucleus_sampling
olmo
ood_baseline
paraphrase_evades
pythia
qlora
qurating
qwen3
release_strategies
reliable_detection
self_consuming_mad
semeval2024_task8
stamatatos_survey
strong_model_collapse
synthid_text
uchendu_attribution
watermark_llm
writing_diversity
wu_survey_2025
xgboost
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "ad9abe33-0632-4ba2-8532-46750350eab9",
  "tool_use_result": {
    "stdout": "aaronson_watermark\nbeyond_binary\nbinoculars\nbroken_telephone\nccnet\nchainwash\ncoral_ordinal\ncurious_decline\ncurse_of_recursion\ndetectgpt\ndetection_possibilities\ndiveye\ndna_gpt\ndsir\nfast_detectgpt\nfeat_aug_transformer\nfrank_hall_ordinal\ngenerator_barrier\ngltr\ngrover\nintrinsic_dimension\njawahar_survey\nkoppel_authorship\nld_score\nmapping_llm_science\nmarkovian_chains\nmin_k_percent\nmodel_collapse_avoidable\nmonitoring_ai_review\nmunir_looking_glass\nnucleus_sampling\nolmo\nood_baseline\nparaphrase_evades\npythia\nqlora\nqurating\nqwen3\nrelease_strategies\nreliable_detection\nself_consuming_mad\nsemeval2024_task8\nstamatatos_survey\nstrong_model_collapse\nsynthid_text\nuchendu_attribution\nwatermark_llm\nwriting_diversity\nwu_survey_2025\nxgboost",
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

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_01J1CHGCCZDRoEHTzAJxpoRp`</summary>

```json
{
  "command": "grep -ohP '\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract citation keys with escaped backslashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "7ebebe7b-5d59-434c-b908-6197a869f012",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JPNUymX77YazrdzWkmU8D1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2657,
      "cache_read_input_tokens": 76097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2657
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

_source line 74 · 2026-05-16T03:07:43.781Z_

<details><summary>↩ Tool result · `toolu_01J1CHGCCZDRoEHTzAJxpoRp`</summary>

```text
aaronson_watermark
beyond_binary
binoculars
broken_telephone
ccnet
chainwash
coral_ordinal
curious_decline
curse_of_recursion
detectgpt
detection_possibilities
diveye
dna_gpt
dsir
fast_detectgpt
feat_aug_transformer
frank_hall_ordinal
generator_barrier
gltr
grover
intrinsic_dimension
jawahar_survey
koppel_authorship
ld_score
mapping_llm_science
markovian_chains
min_k_percent
model_collapse_avoidable
monitoring_ai_review
munir_looking_glass
nucleus_sampling
olmo
ood_baseline
paraphrase_evades
pythia
qlora
qurating
qwen3
release_strategies
reliable_detection
self_consuming_mad
semeval2024_task8
stamatatos_survey
strong_model_collapse
synthid_text
uchendu_attribution
watermark_llm
writing_diversity
wu_survey_2025
xgboost
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "8d574451-ec7f-4366-8455-c2f1755956bd",
  "tool_use_result": {
    "stdout": "aaronson_watermark\nbeyond_binary\nbinoculars\nbroken_telephone\nccnet\nchainwash\ncoral_ordinal\ncurious_decline\ncurse_of_recursion\ndetectgpt\ndetection_possibilities\ndiveye\ndna_gpt\ndsir\nfast_detectgpt\nfeat_aug_transformer\nfrank_hall_ordinal\ngenerator_barrier\ngltr\ngrover\nintrinsic_dimension\njawahar_survey\nkoppel_authorship\nld_score\nmapping_llm_science\nmarkovian_chains\nmin_k_percent\nmodel_collapse_avoidable\nmonitoring_ai_review\nmunir_looking_glass\nnucleus_sampling\nolmo\nood_baseline\nparaphrase_evades\npythia\nqlora\nqurating\nqwen3\nrelease_strategies\nreliable_detection\nself_consuming_mad\nsemeval2024_task8\nstamatatos_survey\nstrong_model_collapse\nsynthid_text\nuchendu_attribution\nwatermark_llm\nwriting_diversity\nwu_survey_2025\nxgboost",
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

_source line 75_

<details><summary>Logged reasoning block</summary>

```text
Both lists are identical — 50 citation keys cited, 50 bib entries defined. No orphan citations, no unused bib entries. ✅

Now let me also estimate the main body line count more carefully. I need to count only the lines in sections that count toward the 8-page limit: abstract through conclusion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "2f61abf4-6673-4d13-96b3-a68e908c233b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ke769tYeVUw7XGFiaLkJUV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 78754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
      },
      "output_tokens": 8,
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

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_013zHxXxfPyyCLgCV6meCzxT`</summary>

```json
{
  "command": "for f in abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex; do echo \"$f: $(wc -l < $f) lines\"; done && echo \"---\" && for f in limitations.tex ethics.tex; do echo \"$f (not counted): $(wc -l < $f) lines\"; done && echo \"---\" && for f in appendix_*.tex table4.tex; do echo \"$f: $(wc -l < $f) lines\"; done",
  "description": "Count lines per section to estimate page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "5f571ac5-7295-4914-96fc-483a771574b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ke769tYeVUw7XGFiaLkJUV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 78754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
      },
      "output_tokens": 8,
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

_source line 77 · 2026-05-16T03:07:51.508Z_

<details><summary>↩ Tool result · `toolu_013zHxXxfPyyCLgCV6meCzxT`</summary>

```text
abstract.tex: 8 lines
introduction.tex: 42 lines
related_work.tex: 60 lines
method.tex: 95 lines
results.tex: 196 lines
discussion.tex: 86 lines
conclusion.tex: 11 lines
---
limitations.tex (not counted): 29 lines
ethics.tex (not counted): 8 lines
---
appendix_classifier.tex: 55 lines
appendix_confusion_matrix.tex: 17 lines
appendix_finer_depth.tex: 51 lines
appendix_human_edit.tex: 34 lines
appendix_length.tex: 29 lines
appendix_lofo.tex: 28 lines
appendix_prompt_type.tex: 7 lines
appendix_qlora.tex: 34 lines
table4.tex: 17 lines
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "a2e2aa13-0d60-41a0-a7d6-1e372f641aff",
  "tool_use_result": {
    "stdout": "abstract.tex: 8 lines\nintroduction.tex: 42 lines\nrelated_work.tex: 60 lines\nmethod.tex: 95 lines\nresults.tex: 196 lines\ndiscussion.tex: 86 lines\nconclusion.tex: 11 lines\n---\nlimitations.tex (not counted): 29 lines\nethics.tex (not counted): 8 lines\n---\nappendix_classifier.tex: 55 lines\nappendix_confusion_matrix.tex: 17 lines\nappendix_finer_depth.tex: 51 lines\nappendix_human_edit.tex: 34 lines\nappendix_length.tex: 29 lines\nappendix_lofo.tex: 28 lines\nappendix_prompt_type.tex: 7 lines\nappendix_qlora.tex: 34 lines\ntable4.tex: 17 lines",
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

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01B4PYyteLKabmfb3F137Gdz`</summary>

```json
{
  "command": "diff <(grep -ohP '\\\\cite[tp]?\\{[^}]+\\}' abstract.tex introduction.tex related_work.tex method.tex results.tex discussion.tex conclusion.tex limitations.tex ethics.tex appendix_*.tex table4.tex | grep -ohP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u) <(grep -ohP '@\\w+\\{(\\w+),' references.bib | grep -ohP '\\{(\\w+),' | tr -d '{,' | sort -u)",
  "description": "Diff cited keys vs bib keys to find mismatches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "1cea0bcc-b9a0-4f7f-be36-a0f40c37e7a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ke769tYeVUw7XGFiaLkJUV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 78754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
      },
      "output_tokens": 8,
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

_source line 79 · 2026-05-16T03:07:54.342Z_

<details><summary>↩ Tool result · `toolu_01B4PYyteLKabmfb3F137Gdz`</summary>

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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "afb16370-8a34-45da-8033-d195ade1d3f0",
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

_source line 80_

<details><summary>Logged reasoning block</summary>

```text
The diff output is empty, meaning all cited keys match all bib keys exactly. Perfect.

Now let me count:
Main body (counted toward 8-page limit): abstract (8) + intro (42) + related work (60) + method (95) + results (196) + discussion (86) + conclusion (11) = 498 lines

This includes 5 tables in the main body:
1. tab:logo-results (in results.tex, ~20 lines)
2. tab:cross-ref (in table4.tex, 17 lines, included via results.tex)


3. tab:ablation (in results.tex, ~15 lines)
4. tab:baselines (in results.tex, ~20 lines)
5. tab:downstream (in results.tex, ~20 lines)

And 2 figures:
1. fig:feature-drift (in results.tex)
2. fig:baseline-ci (in results.tex)

With ACL two-column format at 11pt, a typical page fits roughly 90-100 lines of formatted text. But tables and figures take extra space. With ~498 lines and 5 tables + 2 figures, I'm estimating this lands somewhere between 7-9 pages, which puts me right at the edge of the limit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "9d0f238a-2694-4ff0-b5cc-96cc2fa9dcd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vp8dCg9AATFYFkufN4T78W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 79201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
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

_source line 81_

All data collected. Citation keys match perfectly (50 cited = 50 defined). Now writing the checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "48ab1f6f-eebe-4b1a-a941-b6ae142f8eb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vp8dCg9AATFYFkufN4T78W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 79201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
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

_source line 82_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015QenzyUshHAxx9k1XtXbfR`</summary>

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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "140d49f1-1c98-496c-a392-c51d4b99a51c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vp8dCg9AATFYFkufN4T78W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 79201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 871
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

_source line 83 · 2026-05-16T03:08:02.021Z_

<details><summary>↩ Tool result · `toolu_015QenzyUshHAxx9k1XtXbfR`</summary>

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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "a9925106-d85d-42d3-b4d8-e79279a622dd",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Write · `toolu_01LTp9kBCXtjxc83PVafhjLC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md",
  "content": "# EMNLP 2026 ARR Submission Pre-flight Checklist\n\n**Paper**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains  \n**Date**: 2026-05-16  \n**Paper directory**: `artifacts/_project/paper/`\n\n---\n\n## 1. Anonymization\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 1.1 | Author field | ✅ | `\\author{Anonymous}` in `main.tex:15` |\n| 1.2 | No institutional affiliations | ✅ | None found |\n| 1.3 | No acknowledgments section | ✅ | Absent (correct for review) |\n| 1.4 | No GitHub/GitLab/personal URLs | ✅ | No repository or personal URLs in any .tex |\n| 1.5 | No funding/grant info | ✅ | None found |\n| 1.6 | Conclusion release statement | ✅ | `conclusion.tex:11` says \"will be released upon publication\" — no URL provided, safe |\n| 1.7 | PDF metadata | ⚠️ | **No compiled PDF found in paper directory. Compile and verify `pdfinfo` shows no author/creator metadata before submission.** |\n| 1.8 | `_backup/` directory | ❌ | `artifacts/_project/paper/_backup/` contains 24 old .tex files (some with `\\cite{placeholder}`). **Must exclude from submission package.** |\n\n---\n\n## 2. Page Count (8-page limit, excl. references + appendix)\n\nMain body line counts (source lines, not formatted):\n\n| Section | Lines | Tables | Figures |\n|---------|-------|--------|---------|\n| Abstract | 8 | 0 | 0 |\n| Introduction | 42 | 0 | 0 |\n| Related Work | 60 | 0 | 0 |\n| Method | 95 | 0 | 0 |\n| Results | 196 | 4 (+ table4.tex = 5) | 2 |\n| Discussion | 86 | 0 | 0 |\n| Conclusion | 11 | 0 | 0 |\n| **Total** | **498** | **5** | **2** |\n\nNot counted toward limit: Limitations (29 lines), Ethics (8 lines), References, Appendix (8 sections, 272 lines).\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 2.1 | Main body ≤ 8 pages | ⚠️ | **Estimated 7–9 pages. With 498 source lines + 5 tables + 2 figures in ACL two-column format, this is borderline. Must compile to verify.** Discussion section is substantial (86 lines, ~12 paragraphs). If over limit, Discussion is the primary candidate for trimming. |\n\n---\n\n## 3. Required Sections\n\n| # | Section | Status | Notes |\n|---|---------|--------|-------|\n| 3.1 | Abstract | ✅ | `abstract.tex`, included via `\\input` |\n| 3.2 | Introduction | ✅ | `introduction.tex`, `\\section{Introduction}` |\n| 3.3 | Related Work | ✅ | `related_work.tex`, `\\section{Related Work}` |\n| 3.4 | Method | ✅ | `method.tex`, `\\section{Method}` |\n| 3.5 | Results/Experiments | ✅ | `results.tex`, `\\section{Results}` |\n| 3.6 | Discussion | ✅ | `discussion.tex`, `\\section{Discussion}` |\n| 3.7 | Conclusion | ✅ | `conclusion.tex`, `\\section{Conclusion}` |\n| 3.8 | Limitations | ✅ | `limitations.tex`, `\\section*{Limitations}` (unnumbered, correct) |\n| 3.9 | Ethics Statement | ✅ | `ethics.tex`, `\\section*{Ethics Statement}` (unnumbered, correct) |\n\n---\n\n## 4. References\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 4.1 | .bib file exists | ✅ | `references.bib` — 50 entries |\n| 4.2 | All `\\cite{}` keys defined in .bib | ✅ | 50 unique cited keys, all present in .bib (diff is empty) |\n| 4.3 | All .bib entries cited | ✅ | 50 bib entries, all cited (no orphan entries) |\n| 4.4 | No `\\cite{placeholder}` in main files | ✅ | Only in `_backup/` (excluded from compilation) |\n| 4.5 | Bib entry completeness | ⚠️ | Some entries lack page numbers or DOIs (e.g., `stamatatos_survey`, `koppel_authorship`, `aaronson_watermark`). Acceptable for ARR but recommend filling in for camera-ready. |\n\n---\n\n## 5. Figures and Tables\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 5.1 | Figure files exist | ✅ | `fig1_differential_response.pdf` ✅, `fig3_baseline_comparison.png` ✅ (both in `../chart/`) |\n| 5.2 | `\\graphicspath` correct | ✅ | `main.tex:11`: `\\graphicspath{{../chart/}}` |\n| 5.3 | Unused figure files | ⚠️ | `fig2_logo_performance.png`, `fig4_downstream_negative.pdf/.png` exist in `chart/` but are not referenced. Clean up before submission to reduce package size. |\n| 5.4 | All `\\ref{}` targets defined | ✅ | All cross-references (sections, tables, figures, appendices) have matching `\\label{}` definitions |\n\n---\n\n## 6. Appendix / Supplementary Materials\n\n8 appendix sections in `main.tex`, ordered:\n\n| # | Appendix | Label | File |\n|---|----------|-------|------|\n| A | Length Confound Analysis | `app:length` | `appendix_length.tex` |\n| B | Prompt Type Generalization | `app:prompt-type` | `appendix_prompt_type.tex` |\n| C | Finer-Grained Depth Classification | `app:finer-depth` | `appendix_finer_depth.tex` |\n| D | End-to-End Depth Classification (QLoRA) | `app:qlora` | `appendix_qlora.tex` |\n| E | Leave-One-Feature-Out Analysis | `app:lofo` | `appendix_lofo.tex` |\n| F | Confusion Matrix | `app:confusion` | `appendix_confusion_matrix.tex` |\n| G | Classifier Sensitivity | `app:classifier` | `appendix_classifier.tex` |\n| H | Human-Edit Robustness | `app:human-edit` | `appendix_human_edit.tex` |\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 6.1 | All appendix files exist | ✅ | All 8 files present |\n| 6.2 | Sampling Sensitivity sub-section | ⚠️ | `app:sampling-sensitivity` is a `\\subsection*` inside Appendix G (`appendix_classifier.tex:32`). The label resolves to the parent section. Cross-refs from `discussion.tex:9` and `limitations.tex:27` will point to Appendix G, not the subsection header. Consider promoting to its own appendix section if precise cross-referencing is needed. |\n\n---\n\n## 7. ACL/EMNLP Format\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 7.1 | Document class | ✅ | `\\documentclass[11pt]{article}` |\n| 7.2 | ACL style package | ✅ | `\\usepackage[review]{acl}` — review mode enables anonymization + line numbers |\n| 7.3 | Bibliography style | ✅ | `\\bibliography{references}` — `acl.sty` sets `acl_natbib` style automatically |\n| 7.4 | Required packages | ✅ | `times`, `latexsym`, `graphicx`, `booktabs`, `amsmath` all loaded |\n| 7.5 | `acl.sty` in submission | ⚠️ | **Verify `acl.sty` (2023 version) is included in the submission directory or available. Not found in the paper directory — must be added.** |\n\n---\n\n## 8. Summary\n\n| Category | ✅ Pass | ❌ Fail | ⚠️ Verify |\n|----------|---------|---------|-----------|\n| Anonymization | 6 | 1 | 1 |\n| Page count | — | — | 1 |\n| Required sections | 9 | 0 | 0 |\n| References | 4 | 0 | 1 |\n| Figures/Tables | 2 | 0 | 2 |\n| Appendix | 1 | 0 | 1 |\n| Format | 4 | 0 | 1 |\n| **Total** | **26** | **1** | **6** |\n\n### Action Items (must fix)\n\n1. **❌ Remove `_backup/` directory** from submission package (`paper/_backup/` — 24 stale .tex files, some containing `\\cite{placeholder}`)\n\n### Action Items (verify before submission)\n\n1. **⚠️ Compile PDF and check page count** — estimated 7–9 pages, must be ≤ 8. If over, trim Discussion (86 lines, most expendable).\n2. **⚠️ Check PDF metadata** after compilation — ensure no author/creator info leaks via `pdfinfo`.\n3. **⚠️ Include `acl.sty`** — the ACL 2023 style file must be present in the submission directory.\n4. **⚠️ Clean up unused figures** — `fig2_logo_performance.png`, `fig4_downstream_negative.*` in `chart/`.\n5. **⚠️ `app:sampling-sensitivity` cross-ref precision** — currently a `\\subsection*` inside Appendix G; consider promoting to its own appendix.\n6. **⚠️ Fill missing bib metadata** for camera-ready (page numbers, DOIs for some entries).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "5127e0ca-feaf-4c55-87bd-387d8aba4b2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6t2ejQDkMx9CWiY4KsgzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 80072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1054
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

_source line 85 · 2026-05-16T03:08:52.073Z_

<details><summary>↩ Tool result · `toolu_01LTp9kBCXtjxc83PVafhjLC`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "f1b50ff9-c43b-4e7e-923d-c6ade3fd2c6b",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md",
    "content": "# EMNLP 2026 ARR Submission Pre-flight Checklist\n\n**Paper**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains  \n**Date**: 2026-05-16  \n**Paper directory**: `artifacts/_project/paper/`\n\n---\n\n## 1. Anonymization\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 1.1 | Author field | ✅ | `\\author{Anonymous}` in `main.tex:15` |\n| 1.2 | No institutional affiliations | ✅ | None found |\n| 1.3 | No acknowledgments section | ✅ | Absent (correct for review) |\n| 1.4 | No GitHub/GitLab/personal URLs | ✅ | No repository or personal URLs in any .tex |\n| 1.5 | No funding/grant info | ✅ | None found |\n| 1.6 | Conclusion release statement | ✅ | `conclusion.tex:11` says \"will be released upon publication\" — no URL provided, safe |\n| 1.7 | PDF metadata | ⚠️ | **No compiled PDF found in paper directory. Compile and verify `pdfinfo` shows no author/creator metadata before submission.** |\n| 1.8 | `_backup/` directory | ❌ | `artifacts/_project/paper/_backup/` contains 24 old .tex files (some with `\\cite{placeholder}`). **Must exclude from submission package.** |\n\n---\n\n## 2. Page Count (8-page limit, excl. references + appendix)\n\nMain body line counts (source lines, not formatted):\n\n| Section | Lines | Tables | Figures |\n|---------|-------|--------|---------|\n| Abstract | 8 | 0 | 0 |\n| Introduction | 42 | 0 | 0 |\n| Related Work | 60 | 0 | 0 |\n| Method | 95 | 0 | 0 |\n| Results | 196 | 4 (+ table4.tex = 5) | 2 |\n| Discussion | 86 | 0 | 0 |\n| Conclusion | 11 | 0 | 0 |\n| **Total** | **498** | **5** | **2** |\n\nNot counted toward limit: Limitations (29 lines), Ethics (8 lines), References, Appendix (8 sections, 272 lines).\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 2.1 | Main body ≤ 8 pages | ⚠️ | **Estimated 7–9 pages. With 498 source lines + 5 tables + 2 figures in ACL two-column format, this is borderline. Must compile to verify.** Discussion section is substantial (86 lines, ~12 paragraphs). If over limit, Discussion is the primary candidate for trimming. |\n\n---\n\n## 3. Required Sections\n\n| # | Section | Status | Notes |\n|---|---------|--------|-------|\n| 3.1 | Abstract | ✅ | `abstract.tex`, included via `\\input` |\n| 3.2 | Introduction | ✅ | `introduction.tex`, `\\section{Introduction}` |\n| 3.3 | Related Work | ✅ | `related_work.tex`, `\\section{Related Work}` |\n| 3.4 | Method | ✅ | `method.tex`, `\\section{Method}` |\n| 3.5 | Results/Experiments | ✅ | `results.tex`, `\\section{Results}` |\n| 3.6 | Discussion | ✅ | `discussion.tex`, `\\section{Discussion}` |\n| 3.7 | Conclusion | ✅ | `conclusion.tex`, `\\section{Conclusion}` |\n| 3.8 | Limitations | ✅ | `limitations.tex`, `\\section*{Limitations}` (unnumbered, correct) |\n| 3.9 | Ethics Statement | ✅ | `ethics.tex`, `\\section*{Ethics Statement}` (unnumbered, correct) |\n\n---\n\n## 4. References\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 4.1 | .bib file exists | ✅ | `references.bib` — 50 entries |\n| 4.2 | All `\\cite{}` keys defined in .bib | ✅ | 50 unique cited keys, all present in .bib (diff is empty) |\n| 4.3 | All .bib entries cited | ✅ | 50 bib entries, all cited (no orphan entries) |\n| 4.4 | No `\\cite{placeholder}` in main files | ✅ | Only in `_backup/` (excluded from compilation) |\n| 4.5 | Bib entry completeness | ⚠️ | Some entries lack page numbers or DOIs (e.g., `stamatatos_survey`, `koppel_authorship`, `aaronson_watermark`). Acceptable for ARR but recommend filling in for camera-ready. |\n\n---\n\n## 5. Figures and Tables\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 5.1 | Figure files exist | ✅ | `fig1_differential_response.pdf` ✅, `fig3_baseline_comparison.png` ✅ (both in `../chart/`) |\n| 5.2 | `\\graphicspath` correct | ✅ | `main.tex:11`: `\\graphicspath{{../chart/}}` |\n| 5.3 | Unused figure files | ⚠️ | `fig2_logo_performance.png`, `fig4_downstream_negative.pdf/.png` exist in `chart/` but are not referenced. Clean up before submission to reduce package size. |\n| 5.4 | All `\\ref{}` targets defined | ✅ | All cross-references (sections, tables, figures, appendices) have matching `\\label{}` definitions |\n\n---\n\n## 6. Appendix / Supplementary Materials\n\n8 appendix sections in `main.tex`, ordered:\n\n| # | Appendix | Label | File |\n|---|----------|-------|------|\n| A | Length Confound Analysis | `app:length` | `appendix_length.tex` |\n| B | Prompt Type Generalization | `app:prompt-type` | `appendix_prompt_type.tex` |\n| C | Finer-Grained Depth Classification | `app:finer-depth` | `appendix_finer_depth.tex` |\n| D | End-to-End Depth Classification (QLoRA) | `app:qlora` | `appendix_qlora.tex` |\n| E | Leave-One-Feature-Out Analysis | `app:lofo` | `appendix_lofo.tex` |\n| F | Confusion Matrix | `app:confusion` | `appendix_confusion_matrix.tex` |\n| G | Classifier Sensitivity | `app:classifier` | `appendix_classifier.tex` |\n| H | Human-Edit Robustness | `app:human-edit` | `appendix_human_edit.tex` |\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 6.1 | All appendix files exist | ✅ | All 8 files present |\n| 6.2 | Sampling Sensitivity sub-section | ⚠️ | `app:sampling-sensitivity` is a `\\subsection*` inside Appendix G (`appendix_classifier.tex:32`). The label resolves to the parent section. Cross-refs from `discussion.tex:9` and `limitations.tex:27` will point to Appendix G, not the subsection header. Consider promoting to its own appendix section if precise cross-referencing is needed. |\n\n---\n\n## 7. ACL/EMNLP Format\n\n| # | Check | Status | Notes |\n|---|-------|--------|-------|\n| 7.1 | Document class | ✅ | `\\documentclass[11pt]{article}` |\n| 7.2 | ACL style package | ✅ | `\\usepackage[review]{acl}` — review mode enables anonymization + line numbers |\n| 7.3 | Bibliography style | ✅ | `\\bibliography{references}` — `acl.sty` sets `acl_natbib` style automatically |\n| 7.4 | Required packages | ✅ | `times`, `latexsym`, `graphicx`, `booktabs`, `amsmath` all loaded |\n| 7.5 | `acl.sty` in submission | ⚠️ | **Verify `acl.sty` (2023 version) is included in the submission directory or available. Not found in the paper directory — must be added.** |\n\n---\n\n## 8. Summary\n\n| Category | ✅ Pass | ❌ Fail | ⚠️ Verify |\n|----------|---------|---------|-----------|\n| Anonymization | 6 | 1 | 1 |\n| Page count | — | — | 1 |\n| Required sections | 9 | 0 | 0 |\n| References | 4 | 0 | 1 |\n| Figures/Tables | 2 | 0 | 2 |\n| Appendix | 1 | 0 | 1 |\n| Format | 4 | 0 | 1 |\n| **Total** | **26** | **1** | **6** |\n\n### Action Items (must fix)\n\n1. **❌ Remove `_backup/` directory** from submission package (`paper/_backup/` — 24 stale .tex files, some containing `\\cite{placeholder}`)\n\n### Action Items (verify before submission)\n\n1. **⚠️ Compile PDF and check page count** — estimated 7–9 pages, must be ≤ 8. If over, trim Discussion (86 lines, most expendable).\n2. **⚠️ Check PDF metadata** after compilation — ensure no author/creator info leaks via `pdfinfo`.\n3. **⚠️ Include `acl.sty`** — the ACL 2023 style file must be present in the submission directory.\n4. **⚠️ Clean up unused figures** — `fig2_logo_performance.png`, `fig4_downstream_negative.*` in `chart/`.\n5. **⚠️ `app:sampling-sensitivity` cross-ref precision** — currently a `\\subsection*` inside Appendix G; consider promoting to its own appendix.\n6. **⚠️ Fill missing bib metadata** for camera-ready (page numbers, DOIs for some entries).\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01HJ7q1Bm3mafra5nCypd3dH`</summary>

```json
{
  "name": "EMNLP 2026 ARR Submission Checklist",
  "type": "report",
  "description": "Pre-flight checklist for EMNLP 2026 ARR submission: anonymization, page count, required sections, references, figures, appendix, and ACL format verification. 26 pass, 1 fail (backup dir), 6 need human verification.",
  "project": "gen-depth-fingerprint",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/emnlp_submission_checklist.md",
  "tags": [
    "submission",
    "emnlp2026",
    "checklist"
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
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "4e8f2015-0c22-45d9-b7b1-50a00d658739",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQM6wofNfXkUQTZJtCSv72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2869,
      "cache_read_input_tokens": 81126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2869
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

_source line 87 · 2026-05-16T03:08:57.099Z_

<details><summary>↩ Tool result · `toolu_01HJ7q1Bm3mafra5nCypd3dH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_50b473\", \"name\": \"EMNLP 2026 ARR Submission Checklist\", \"type\": \"report\", \"description\": \"Pre-flight checklist for EMNLP 2026 ARR submission: anonymization, page count, required sections, references, figures, appendix, and ACL format verification. 26 pass, 1 fail (backup dir), 6 need human verification.\", \"path\": \"projects/gen-depth-fingerprint/artifacts/_project/report/emnlp_submission_checklist.md\", \"url\": null, \"project\": \"gen-depth-fingerprint\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T03:08:56.996261+00:00\", \"tags\": [\"submission\", \"emnlp2026\", \"checklist\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "e09172de-00b3-474b-a50e-d9a555a19068",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_50b473\\\", \\\"name\\\": \\\"EMNLP 2026 ARR Submission Checklist\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Pre-flight checklist for EMNLP 2026 ARR submission: anonymization, page count, required sections, references, figures, appendix, and ACL format verification. 26 pass, 1 fail (backup dir), 6 need human verification.\\\", \\\"path\\\": \\\"projects/gen-depth-fingerprint/artifacts/_project/report/emnlp_submission_checklist.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"gen-depth-fingerprint\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T03:08:56.996261+00:00\\\", \\\"tags\\\": [\\\"submission\\\", \\\"emnlp2026\\\", \\\"checklist\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_50b473\", \"name\": \"EMNLP 2026 ARR Submission Checklist\", \"type\": \"report\", \"description\": \"Pre-flight checklist for EMNLP 2026 ARR submission: anonymization, page count, required sections, references, figures, appendix, and ACL format verification. 26 pass, 1 fail (backup dir), 6 need human verification.\", \"path\": \"projects/gen-depth-fingerprint/artifacts/_project/report/emnlp_submission_checklist.md\", \"url\": null, \"project\": \"gen-depth-fingerprint\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T03:08:56.996261+00:00\", \"tags\": [\"submission\", \"emnlp2026\", \"checklist\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 88_

Checklist 写入 `artifacts/emnlp_submission_checklist.md` 并已注册。

**结果**：26 项通过，1 项必须修复，6 项需人工确认。

**必须修复**：
- `paper/_backup/` 目录必须从提交包中删除（含 24 个过期 .tex，部分有 `\cite{placeholder}`）

**需编译验证**：
- 页数估计 7–9 页，必须编译确认 ≤ 8 页（Discussion 86 行是首选裁减对象）
- PDF metadata 无作者信息泄露
- `acl.sty` 需包含在提交目录中
- `chart/` 下有 3 个未引用图片文件可清理
- `app:sampling-sensitivity` 是 Appendix G 的 `\subsection*`，交叉引用指向父节点而非子标题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "uuid": "af45cffe-0ef8-45d9-bc1f-7107ea33e96d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMmG2BXPQDGySowL7rxC4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 601,
      "cache_read_input_tokens": 83995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 601
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

_source line 89_

Checklist 写入 `artifacts/emnlp_submission_checklist.md` 并已注册。

**结果**：26 项通过，1 项必须修复，6 项需人工确认。

**必须修复**：
- `paper/_backup/` 目录必须从提交包中删除（含 24 个过期 .tex，部分有 `\cite{placeholder}`）

**需编译验证**：
- 页数估计 7–9 页，必须编译确认 ≤ 8 页（Discussion 86 行是首选裁减对象）
- PDF metadata 无作者信息泄露
- `acl.sty` 需包含在提交目录中
- `chart/` 下有 3 个未引用图片文件可清理
- `app:sampling-sensitivity` 是 Appendix G 的 `\subsection*`，交叉引用指向父节点而非子标题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 218388,
  "duration_api_ms": 219470,
  "num_turns": 37,
  "stop_reason": "end_turn",
  "session_id": "31658f67-7d26-4c89-8d14-400871542b64",
  "total_cost_usd": 1.1660774999999999,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 86410,
    "cache_read_input_tokens": 646296,
    "output_tokens": 12054,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 86410,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 260,
        "cache_read_input_tokens": 83995,
        "cache_creation_input_tokens": 601,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 601
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1307,
      "outputTokens": 27,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001442,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 12054,
      "cacheReadInputTokens": 646296,
      "cacheCreationInputTokens": 86410,
      "webSearchRequests": 0,
      "costUSD": 1.1646355,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "54626116-be43-4165-a411-48d50df4f250"
}
```

</details>

---
