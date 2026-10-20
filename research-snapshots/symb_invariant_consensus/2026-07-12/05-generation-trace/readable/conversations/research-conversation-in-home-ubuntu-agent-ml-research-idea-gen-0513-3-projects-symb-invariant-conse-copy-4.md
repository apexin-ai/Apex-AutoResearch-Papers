# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/, find any .tex files tha

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a262722788ce57da0.jsonl`
- **Structured JSON:** [`df37ed9d0672a7d086b6.json`](../../sessions/df/df37ed9d0672a7d086b6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-23T01:05:20.996Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/, find any .tex files that define notation related to SCB, BR (bias ratio), SICA, SC, traces, constraints, majority voting. Show relevant snippets with file paths. Also check if there's a main paper .tex file anywhere in the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "649ba351-76d2-421f-9c3b-bac88eec4cde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T01:05:22.405Z_

I'll search for .tex files in the artifacts directory and explore the project structure to find relevant notation definitions and the main paper file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "649ba351-76d2-421f-9c3b-bac88eec4cde",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuDPbGP2vn5oDmwooA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "29a98f8b-a712-4e44-8e30-cec982de48b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NjruH7JaPMTRfVHqCsBvJS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17841,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17841,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T01:05:22.643Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014hHJkgWrksxgmqR2oj1FVe`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29a98f8b-a712-4e44-8e30-cec982de48b0",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuDPbGP2vn5oDmwooA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "66183443-fb28-4995-b0e5-68d3fe60f205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NjruH7JaPMTRfVHqCsBvJS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17841,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17841,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T01:05:22.674Z_

<details><summary>↩ Tool result · `toolu_014hHJkgWrksxgmqR2oj1FVe`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/median/paper.tex
artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
artifacts/dream_reports/dream_20260517T165032/best/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260517T165032/median/paper.tex
artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments_9ea847.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work_b9688e.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/abstract.tex
artifacts/dream_reports/dream_20260519T034058/best/paper.tex
artifacts/dream_reports/dream_20260519T034058/median/paper.tex
artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
artifacts/_project/paper/sub_population_appendix_draft.tex
artifacts/sub_population_appendix_draft.tex
artifacts/table1_bh_draft.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66183443-fb28-4995-b0e5-68d3fe60f205",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "27175ace-2060-46e2-a169-b4bf9d4ec23f",
  "sourceToolAssistantUUID": "66183443-fb28-4995-b0e5-68d3fe60f205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T01:05:22.838Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SNkfdb8uXzREmZmgR1CEwo`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27175ace-2060-46e2-a169-b4bf9d4ec23f",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuDPbGP2vn5oDmwooA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "82aa2c13-35bb-4447-83d5-65e305569333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NjruH7JaPMTRfVHqCsBvJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17841,
      "cache_read_input_tokens": 0,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17841,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T01:05:22.859Z_

<details><summary>↩ Tool result · `toolu_01SNkfdb8uXzREmZmgR1CEwo`</summary>

```text
artifacts/dream_reports/dream_20260516T051642/best/paper.tex
artifacts/dream_reports/dream_20260516T051642/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/best/paper.tex
artifacts/dream_reports/dream_20260516T054054/median/paper.tex
artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
artifacts/dream_reports/dream_20260516T124139/best/paper.tex
artifacts/dream_reports/dream_20260516T124139/median/paper.tex
artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
artifacts/dream_reports/dream_20260516T155754/best/paper.tex
artifacts/dream_reports/dream_20260516T155754/median/paper.tex
artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
artifacts/dream_reports/dream_20260517T144412/best/paper.tex
artifacts/dream_reports/dream_20260517T144412/median/paper.tex
artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
artifacts/dream_reports/dream_20260517T165032/best/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260517T165032/median/paper.tex
artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments_9ea847.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work_b9688e.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/abstract.tex
artifacts/dream_reports/dream_20260519T034058/best/paper.tex
artifacts/dream_reports/dream_20260519T034058/median/paper.tex
artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
artifacts/_project/paper/sub_population_appendix_draft.tex
artifacts/sub_population_appendix_draft.tex
artifacts/table1_bh_draft.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/limitations_content.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
docs/paper/conclusion.tex
docs/paper/related_work.tex
docs/paper/analysis.tex
docs/paper/diagnosis.tex
docs/paper/appendix.tex
docs/paper/solutions.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82aa2c13-35bb-4447-83d5-65e305569333",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "38090d52-2239-4354-bbcc-0a543623077a",
  "sourceToolAssistantUUID": "82aa2c13-35bb-4447-83d5-65e305569333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-23T01:05:24.641Z_

Good! I found multiple .tex files. Let me search for the notation definitions related to SCB, BR, SICA, SC, traces, constraints, and majority voting across these files. I'll start with the main paper structure and then search for specific notation definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38090d52-2239-4354-bbcc-0a543623077a",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuMPZ1XwZtkmnPSye8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "14f44287-78f2-4d74-a110-b0c217fa390a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017yXna7StDZsii49j2nrkZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2290,
      "cache_read_input_tokens": 17841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2290,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T01:05:25.558Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FXiSCtPC1W2fAkrthr2JNF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f44287-78f2-4d74-a110-b0c217fa390a",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuMPZ1XwZtkmnPSye8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8d9b7c84-0362-44dc-b28e-68adc855cf2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017yXna7StDZsii49j2nrkZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2290,
      "cache_read_input_tokens": 17841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2290,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T01:05:25.588Z_

<details><summary>↩ Tool result · `toolu_01FXiSCtPC1W2fAkrthr2JNF`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{tcolorbox}
14	\tcbuselibrary{skins}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Why Self-Extracted Constraints\\Fail to Improve LLM Logical Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{2pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
55	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\vspace{-1mm}
75	\section*{Limitations}
76	\input{limitations_content}
77	
78	\bibliography{references}
79	
80	\appendix
81	\input{appendix}
82	
83	\end{document}
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d9b7c84-0362-44dc-b28e-68adc855cf2a",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "2b66bf39-f64e-4873-bcba-8c43f3596e22",
  "sourceToolAssistantUUID": "8d9b7c84-0362-44dc-b28e-68adc855cf2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T01:05:26.145Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Rx7oLV9YRu49aEcB3uKpqM`</summary>

```json
{
  "pattern": "SCB|bias ratio|SICA|SC|traces|constraints|majority voting|notation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b66bf39-f64e-4873-bcba-8c43f3596e22",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuMPZ1XwZtkmnPSye8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2a71f492-20d8-40f8-8ba9-df12c426e626",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017yXna7StDZsii49j2nrkZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2290,
      "cache_read_input_tokens": 17841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2290,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T01:05:26.160Z_

<details><summary>↩ Tool result · `toolu_01Rx7oLV9YRu49aEcB3uKpqM`</summary>

```text
artifacts/_project/paper/related_work.tex:5:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:8:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:11:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:14:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:17:[Omitted long matching line]
artifacts/_project/paper/related_work.tex:20:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:7:We evaluate SICA against Self-Consistency (SC) across five instruction-tuned models and four reasoning benchmarks.
artifacts/_project/paper/experiments.tex:11:\paragraph{Datasets.} FOLIO~\cite{han2022folio} provides formal logic problems with gold first-order logic (FOL) annotations ($n=204$), which enable the oracle control experiment (\S\ref{sec:oracle}). ProofWriter~\cite{tafjord2021proofwriter} tests multi-step deductive reasoning ($n=600$). StrategyQA~\cite{geva2021strategyqa} evaluates commonsense reasoning ($n=200$ for LLaMA-3.1-8B; $n=60$ for other models). ARC-Challenge~\cite{clark2018arc} covers science questions ($n=60$).
artifacts/_project/paper/experiments.tex:13:\paragraph{Parameters.} Unless otherwise noted, we sample $K=12$ reasoning traces per question at temperature $T=0.7$. Z3~\cite{demoura2008z3} solves each MAX-SAT instance with a 10-second timeout. Temperature ablation experiments vary $T \in \{0.3, 0.5, 0.7, 1.0\}$.
artifacts/_project/paper/experiments.tex:15:\paragraph{Metrics.} We report accuracy (\%), the multi-candidate rate $C_0$ (\S\ref{sec:c0}), and the accuracy gap $\Delta = \text{SICA} - \text{SC}$ in percentage points (pp). Statistical significance is assessed with the McNemar test for paired binary outcomes at $\alpha = 0.05$. For adequately powered conditions ($n \geq 200$), we also compute 95\% bootstrap confidence intervals with 1{,}000 resamples.
artifacts/_project/paper/experiments.tex:18:\subsection{Main Results: SICA Provides No Significant Gain}
artifacts/_project/paper/experiments.tex:21:Does symbolic constraint aggregation improve answer accuracy over majority voting? Table~\ref{tab:main_results} reports results across all model-domain conditions. The answer is no.
artifacts/_project/paper/experiments.tex:26:\caption{Accuracy of Self-Consistency (SC) and SICA across models and domains. $\Delta$ denotes the SICA$-$SC gap in percentage points, computed from unrounded values. No condition reaches statistical significance ($\alpha = 0.05$). $\dagger$: $n=60$, insufficient power for confirmatory conclusions.}
artifacts/_project/paper/experiments.tex:30:Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & McNemar $p$ \\
artifacts/_project/paper/experiments.tex:44:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:48:Across eight conditions, five models, and more than 1,300 evaluation instances, SICA does not improve upon majority voting. The next three subsections investigate why.
artifacts/_project/paper/experiments.tex:54:Is the null result caused by a flawed aggregation mechanism, or by low-quality extracted constraints? To separate these explanations, we construct an oracle variant of SICA that replaces self-extracted FOL constraints with gold FOL annotations from the FOLIO dataset ($n = 204$). The oracle uses Z3 to evaluate ground-truth formulas against each candidate answer; all other pipeline components remain identical.
artifacts/_project/paper/experiments.tex:56:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:62:Why does SICA fail to improve over SC? We examine three diagnostic dimensions: the multi-candidate rate $C_0$, constraint extraction quality, and the effect of sampling temperature on answer diversity.
artifacts/_project/paper/experiments.tex:64:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:69:\caption{Capability trap diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable FOL constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\Delta$: SICA$-$SC gap (pp), repeated from Table~\ref{tab:main_results} for reference. $\dagger$: $n=60$. $^*$Combined rate from a single run covering both FOLIO and ProofWriter.}
artifacts/_project/paper/experiments.tex:87:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:89:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:94:\caption{Per-problem scatter of vote entropy (x-axis) versus constraint exclusion rate (y-axis) for Qwen2.5-14B on FOLIO. Problems with high vote entropy (ambiguous majority vote) do not benefit from constraint filtering; the constraints fail to resolve disagreement among traces.}
artifacts/_project/paper/experiments.tex:101:\caption{Multi-candidate rate $C_0$ (x-axis) versus SICA$-$SC accuracy gap (y-axis) across all model-domain conditions. Each point represents one condition from Table~\ref{tab:main_results}. The gap remains centered around zero regardless of $C_0$: answer diversity alone does not enable constraint-based improvement.}
artifacts/_project/paper/experiments.tex:105:The diagnostic picture is consistent across all three dimensions: SICA fails not because of insufficient diversity or mechanical extraction errors, but because the extracted constraints carry no discriminative signal beyond the votes they were derived from.
artifacts/_project/paper/experiments.tex:111:The diagnostics above suggest that self-extracted constraints are semantically coupled to their source answers and therefore non-discriminative. If so, the MAX-SAT formulation should produce the same predictions as simpler baselines that ignore constraint satisfiability. We test this prediction with three ablation variants on Qwen2.5-14B across combined FOLIO and ProofWriter data ($n = 804$):
artifacts/_project/paper/experiments.tex:114:\item \textbf{SICA (MAX-SAT):} The full pipeline as described in \S\ref{sec:method}.
artifacts/_project/paper/experiments.tex:115:\item \textbf{Count-only:} Select the answer supported by the most constraints, ignoring satisfiability.
artifacts/_project/paper/experiments.tex:122:\caption{Constraint ablation (Qwen2.5-14B, $n = 804$, FOLIO + ProofWriter). SC serves as the majority-vote baseline. Agreement indicates the number of predictions identical to SC out of 804. All constraint-based variants produce nearly identical outputs.}
artifacts/_project/paper/experiments.tex:126:Aggregation & Acc.\ (\%) & Agreement w/ SC \\
artifacts/_project/paper/experiments.tex:128:SC (majority vote) & 76.24 & --- \\
artifacts/_project/paper/experiments.tex:129:SICA (MAX-SAT) & 76.49 & 802\,/\,804 \\
artifacts/_project/paper/experiments.tex:136:[Omitted long matching line]
artifacts/_project/paper/experiments.tex:138:This ablation directly supports the capability trap thesis. Symbolic verification \emph{can} improve answer selection, as the oracle control demonstrates with $+8.82$~pp over SC. But the improvement requires constraints that encode independent problem structure. Self-extracted constraints instead encode the reasoning steps that produced each candidate answer, and so they are redundant with the votes they accompany.
artifacts/_project/paper/experiments_9ea847.tex:7:We evaluate SICA against Self-Consistency (SC) across five instruction-tuned models and four reasoning benchmarks.
artifacts/_project/paper/experiments_9ea847.tex:11:\paragraph{Datasets.} FOLIO~\cite{han2022folio} provides formal logic problems with gold first-order logic (FOL) annotations ($n=204$), which enable the oracle control experiment (\S\ref{sec:oracle}). ProofWriter~\cite{tafjord2021proofwriter} tests multi-step deductive reasoning ($n=600$). StrategyQA~\cite{geva2021strategyqa} evaluates commonsense reasoning ($n=200$ for LLaMA-3.1-8B; $n=60$ for other models). ARC-Challenge~\cite{clark2018arc} covers science questions ($n=60$).
artifacts/_project/paper/experiments_9ea847.tex:13:\paragraph{Parameters.} Unless otherwise noted, we sample $K=12$ reasoning traces per question at temperature $T=0.7$. Z3~\cite{demoura2008z3} solves each MAX-SAT instance with a 10-second timeout. Temperature ablation experiments vary $T \in \{0.3, 0.5, 0.7, 1.0\}$.
artifacts/_project/paper/experiments_9ea847.tex:15:\paragraph{Metrics.} We report accuracy (\%), the multi-candidate rate $C_0$ (\S\ref{sec:c0}), and the accuracy gap $\Delta = \text{SICA} - \text{SC}$ in percentage points (pp). Statistical significance is assessed with the McNemar test for paired binary outcomes at $\alpha = 0.05$. For adequately powered conditions ($n \geq 200$), we also compute 95\% bootstrap confidence intervals with 1{,}000 resamples.
artifacts/_project/paper/experiments_9ea847.tex:18:\subsection{Main Results: SICA Provides No Significant Gain}
artifacts/_project/paper/experiments_9ea847.tex:21:Does symbolic constraint aggregation improve answer accuracy over majority voting? Table~\ref{tab:main_results} reports results across all model-domain conditions. The answer is no.
artifacts/_project/paper/experiments_9ea847.tex:26:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:30:Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p^a$ \\
artifacts/_project/paper/experiments_9ea847.tex:49:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:51:The five smaller conditions ($n \leq 60$, marked $\dagger$) are consistent with this null pattern. Qwen2.5-14B on StrategyQA shows $\Delta = +3.33$~pp ($p = 0.50$, exact binomial on 2 discordant pairs). DeepSeek-R1-7B on FOLIO+ProofWriter shows $\Delta = -3.33$~pp ($p = 0.480$). QwQ-32B on AIME produces identical outputs ($\Delta = 0$) with effective $C_0 = 2.6\%$, confirming that reasoning-specialized models leave no room for SICA to operate.
artifacts/_project/paper/experiments_9ea847.tex:53:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:59:Is the null result caused by a flawed aggregation mechanism, or by low-quality extracted constraints? To separate these explanations, we construct an oracle variant of SICA that replaces self-extracted FOL constraints with gold FOL annotations from the FOLIO dataset ($n = 204$). The oracle uses Z3 to evaluate ground-truth formulas against each candidate answer; all other pipeline components remain identical.
artifacts/_project/paper/experiments_9ea847.tex:61:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:67:Why does SICA fail to improve over SC? We examine three diagnostic dimensions: the multi-candidate rate $C_0$, constraint extraction quality, and the effect of sampling temperature on answer diversity.
artifacts/_project/paper/experiments_9ea847.tex:69:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:74:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:94:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:96:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:101:\caption{Per-problem scatter of vote entropy (x-axis) versus constraint exclusion rate (y-axis) for Qwen2.5-14B on FOLIO and ProofWriter ($n=307$ multi-candidate problems). Problems with high vote entropy (ambiguous majority vote) do not benefit from constraint filtering; the constraints fail to resolve disagreement among traces.}
artifacts/_project/paper/experiments_9ea847.tex:108:\caption{Multi-candidate rate $C_0$ (x-axis) versus SICA$-$SC accuracy gap (y-axis) across all model-domain conditions. Each point represents one condition from Table~\ref{tab:main_results}. The gap remains centered around zero regardless of $C_0$: answer diversity alone does not enable constraint-based improvement.}
artifacts/_project/paper/experiments_9ea847.tex:112:The diagnostic picture is consistent across all three dimensions: SICA fails not because of insufficient diversity or mechanical extraction errors, but because the extracted constraints carry no discriminative signal beyond the votes they were derived from.
artifacts/_project/paper/experiments_9ea847.tex:118:The diagnostics above suggest that self-extracted constraints are semantically coupled to their source answers and therefore non-discriminative. If so, the MAX-SAT formulation should produce the same predictions as simpler baselines that ignore constraint satisfiability. We test this prediction with three ablation variants on Qwen2.5-14B across combined FOLIO and ProofWriter data ($n = 804$):
artifacts/_project/paper/experiments_9ea847.tex:121:\item \textbf{SICA (MAX-SAT):} The full pipeline as described in \S\ref{sec:method}.
artifacts/_project/paper/experiments_9ea847.tex:122:\item \textbf{Count-only:} Select the answer supported by the most constraints, ignoring satisfiability.
artifacts/_project/paper/experiments_9ea847.tex:129:\caption{Constraint ablation (Qwen2.5-14B, $n = 804$, FOLIO + ProofWriter). SC serves as the majority-vote baseline. Agreement columns report the number of identical predictions out of 804 against SC and against the count-only baseline.}
artifacts/_project/paper/experiments_9ea847.tex:133:Aggregation & Acc.\ (\%) & w/ SC & w/ Count-only \\
artifacts/_project/paper/experiments_9ea847.tex:135:SC (majority vote) & 76.24 & --- & 774\,/\,804 \\
artifacts/_project/paper/experiments_9ea847.tex:136:SICA (MAX-SAT) & 76.49 & 773\,/\,804 & 803\,/\,804 \\
artifacts/_project/paper/experiments_9ea847.tex:143:[Omitted long matching line]
artifacts/_project/paper/experiments_9ea847.tex:145:This ablation directly supports the capability trap thesis. Symbolic verification \emph{can} improve answer selection, as the oracle control demonstrates with $+8.82$~pp over SC. But the improvement requires constraints that encode independent problem structure. Self-extracted constraints instead encode the reasoning steps that produced each candidate answer, and so they are redundant with the votes they accompany.
artifacts/_project/paper/conclusion.tex:4:[Omitted long matching line]
artifacts/_project/paper/conclusion.tex:6:An oracle control experiment isolates constraint quality as the sole bottleneck. Replacing self-extracted constraints with gold FOL annotations yields $+8.82$ percentage points over majority voting ($p < 0.001$), while all other pipeline components remain fixed. The aggregation mechanism is sound; the problem lies entirely in same-model self-extraction. This result quantifies an $8.82$-point gap that remains recoverable through higher-quality constraint sources.
artifacts/_project/paper/conclusion.tex:8:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:4:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:6:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:8:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:10:[Omitted long matching line]
artifacts/_project/paper/sub_population_appendix_draft.tex:1:% Sub-population Analysis: SICA vs SC (Mistral-7B)
artifacts/_project/paper/sub_population_appendix_draft.tex:13:\caption{SICA vs.\ SC accuracy by gold-label type (Mistral-7B). $\Delta$\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}
artifacts/_project/paper/sub_population_appendix_draft.tex:17:\textbf{Dataset} & \textbf{Label} & $n$ & \textbf{SC} & \textbf{SICA} & $\Delta$\,pp & $p$ \\
artifacts/_project/paper/sub_population_appendix_draft.tex:40:\caption{SICA vs.\ SC accuracy by extracted constraint count tertile (Mistral-7B). Constraint counts are unique deduplicated constraints per problem.}
artifacts/_project/paper/sub_population_appendix_draft.tex:44:\textbf{Dataset} & \textbf{Tertile} & $n$ & $\bar{c}$ & \textbf{SC} & \textbf{SICA} & $\Delta$\,pp & $p$ \\
artifacts/_project/paper/sub_population_appendix_draft.tex:59:On FOLIO-204, SICA consistently improves over SC across all three answer types, with the largest gain on \textsc{True} labels ($+$6.9\,pp) where constraint-weighted consensus helps recover correct answers from minority traces.
artifacts/_project/paper/sub_population_appendix_draft.tex:61:On ProofWriter-600, SICA shows a small uniform degradation across all subgroups; this is consistent with the overall negative transfer reported in the main results, and the constraint-count analysis shows the degradation attenuates in the high-constraint tertile ($\Delta{=}{-}0.5$\,pp, $p{=}1.0$), suggesting that when more constraints are available the symbolic aggregation at least does not hurt.
artifacts/_project/paper/abstract.tex:2:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:4:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:6:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:8:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:10:[Omitted long matching line]
artifacts/_project/paper/introduction.tex:14:    \item \textbf{Systematic negative result.} We report the first controlled evaluation of same-model constraint self-extraction across five models, four domains, and more than 1,300 instances. No condition produces a statistically significant improvement over majority voting (\S\ref{sec:main-results}).
artifacts/_project/paper/introduction.tex:15:    \item \textbf{Causal isolation via oracle control.} By replacing only the constraint source while holding all pipeline components fixed, we establish that the MAX-SAT aggregation mechanism is sound and that the bottleneck lies entirely in extraction quality. Gold FOL constraints yield $+8.82$\,pp over SC, a recoverable gap of practical significance (\S\ref{sec:oracle}).
artifacts/_project/paper/introduction.tex:16:    \item \textbf{The $C_0$ diagnostic.} We introduce the multi-candidate rate $C_0$, a zero-cost metric computable before constraint extraction, as a necessary-condition screening criterion. When $C_0 < 5\%$, constraint-based methods degenerate to majority voting by construction (\S\ref{sec:c0}).
artifacts/_project/paper/introduction.tex:17:    \item \textbf{Constraint ablation.} We show that MAX-SAT, count-only, and random-weight aggregation produce nearly identical predictions, self-extracted constraints carry no discriminative signal beyond vote counts (\S\ref{sec:ablation}).
artifacts/_project/paper/related_work_b9688e.tex:5:[Omitted long matching line]
artifacts/_project/paper/related_work_b9688e.tex:8:[Omitted long matching line]
artifacts/_project/paper/related_work_b9688e.tex:11:[Omitted long matching line]
artifacts/_project/paper/related_work_b9688e.tex:14:[Omitted long matching line]
artifacts/_project/paper/related_work_b9688e.tex:17:[Omitted long matching line]
artifacts/_project/paper/related_work_b9688e.tex:20:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a71f492-20d8-40f8-8ba9-df12c426e626",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "61311eae-66d9-46e7-9976-8badeb549198",
  "sourceToolAssistantUUID": "2a71f492-20d8-40f8-8ba9-df12c426e626",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T01:05:26.538Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011xaFd8LzqeayLX18HUdVNb`</summary>

```json
{
  "pattern": "SCB|bias ratio|SICA|SC|traces|constraints|majority voting|notation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61311eae-66d9-46e7-9976-8badeb549198",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuMPZ1XwZtkmnPSye8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "948fd316-cfc0-4b80-ae3d-fa9ee59fd236",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017yXna7StDZsii49j2nrkZo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2290,
      "cache_read_input_tokens": 17841,
      "output_tokens": 426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2290
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 426,
          "cache_read_input_tokens": 17841,
          "cache_creation_input_tokens": 2290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2290,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T01:05:26.578Z_

<details><summary>↩ Tool result · `toolu_011xaFd8LzqeayLX18HUdVNb`</summary>

```text
&lt;persisted-output>
Output too large (41.7KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/5f08a0b3-198f-4f40-8b69-e8e76d016497/tool-results/toolu_011xaFd8LzqeayLX18HUdVNb.txt

Preview (first 2KB):
docs/paper/analysis.tex:9:[Omitted long matching line]
docs/paper/analysis.tex:15:[Omitted long matching line]
docs/paper/analysis.tex:17:[Omitted long matching line]
docs/paper/analysis.tex:23:[Omitted long matching line]
docs/paper/analysis.tex:27:Model & Ext. & SC (\%) & $n_\text{err}$ & BR & $\Delta$ (pp) \\
docs/paper/analysis.tex:43:\looseness=-1 Two controls rule out answer leakage. BR is uniform across early, mid, and late reasoning steps (Fisher $p = 0.71$); high-consensus errors amplify to $\text{BR} = 18.8\times$ versus $2.7\times$ for low-consensus ($p < 0.001$). Removing the answer sentence from traces before extraction yields no BR decrease (Wilcoxon $p \geq 0.12$) despite significant accuracy loss (McNemar $p < 0.013$). SCB reflects a distributional prior embedded throughout reasoning, not answer contamination.
docs/paper/analysis.tex:48:[Omitted long matching line]
docs/paper/analysis.tex:51:CCR analysis confirms the same pattern: cross-architecture NLI yields $\text{CCR} > 0$ while same-model SICA yields $\text{CCR} < 0$, with CCR correlating with combo gain ($\rho = 0.84$, $p = 0.014$; Appendix~\ref{app:cil}).
docs/paper/analysis.tex:58:[Omitted long matching line]
docs/paper/analysis.tex:63:\caption{Twenty-three of 27 training-free strategies across four categories (four additional strategies tested but omitted for clarity). All produce neutral-to-negative $\Delta$ vs.\ SC. Grey band: $\pm 1$\,pp noise zone.}
docs/paper/analysis.tex:68:\looseness=-1 Decision boundaries ($C_0 < 5\%$, $K_\text{eff} \leq 1.3$, SC $< 40\%$) were derived from Mistral-7B and Qwen2.5-14B conditions. We evaluate prospectively on held-out LLaMA-3.1-8B, a different model family not used in boundary derivation: on FOLIO (SC $= 66.18\%$, $C_0 = 61.8\%$, $K_\text{eff} = 2.17$), the framework predicts Type~A confirmation bias ($\Delta \leq 0$); the observed $\Delta = -4.41$\,pp confirms the prediction.
docs/paper/analysis.tex:71:[Omitted long matching line]
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "948fd316-cfc0-4b80-ae3d-fa9ee59fd236",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "2b66527a-54e5-4f8e-8368-c91ad7cf9b75",
  "sourceToolAssistantUUID": "948fd316-cfc0-4b80-ae3d-fa9ee59fd236",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-23T01:05:27.780Z_

Let me read the detailed files from the docs/paper directory to find the specific notation definitions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b66527a-54e5-4f8e-8368-c91ad7cf9b75",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbudDokWMMiSaZBmfsL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e6133bfb-2bba-4a6c-bcad-258a453cb0a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QSkYpTMbuNzhTLHA3ypvD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7501,
      "cache_read_input_tokens": 20131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7501,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T01:05:28.391Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RJboXprXzrHZBbPH7zMvRP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6133bfb-2bba-4a6c-bcad-258a453cb0a9",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbudDokWMMiSaZBmfsL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0c2580d1-13d3-46c4-b8ac-bff801a2a3ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QSkYpTMbuNzhTLHA3ypvD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7501,
      "cache_read_input_tokens": 20131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7501,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T01:05:28.437Z_

<details><summary>↩ Tool result · `toolu_01RJboXprXzrHZBbPH7zMvRP`</summary>

```text
1	\section{Background \& Setup}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees majority convergence under independent voters \citep{austensmith1996}, but LLM traces violate this independence. Following \citet{ladha1992correlated} and \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa].
11	\end{equation} In our experiments (\S\ref{sec:effective-k}), $\kappa = 0.21$--$0.82$ yields $K_{\text{eff}} \approx 1.2$--$3.6$ for $K{=}12$, serving as an ordinal diagnostic of vote diversity rather than a literal effective sample size. This independence limitation motivates our investigation.
12	
13	\subsection{SICA Pipeline}
14	\label{sec:pipeline}
15	
16	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
17	
18	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
19	
20	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
21	
22	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
23	\begin{equation}
24	\label{eq:maxsat}
25	\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
26	\end{equation}
27	Z3 \citep{demoura2008z3} solves this with a 10-second timeout. Answer assertion constraints ($\texttt{answer\_a} == \texttt{True}$, weight 1) ensure every candidate receives a nonzero base score, making SICA a strict generalization of SC.
28	
29	\paragraph{Scoring.} Let $\mathcal{C}^{\setminus} = \mathcal{C} \setminus \mathcal{C}^*$. Each candidate $a$ is scored by:
30	\begin{equation}
31	\label{eq:score}
32	\text{score}(a) = \sum_{c \in \mathcal{C}^*} w_c \cdot \sigma(c, a) - \alpha \sum_{c \in \mathcal{C}^{\setminus}} w_c \cdot \sigma(c, a),
33	\end{equation}
34	where $\sigma(c, a) = 1$ if $c$ was extracted from any trace producing answer $a$, and $\alpha = 0.5$. The selected answer is $a^* = \arg\max_{a} \text{score}(a)$.
35	
36	\paragraph{Degeneration condition.} If self-extracted constraints are coupled to their source answer, MAX-SAT retains nearly all ($|\mathcal{C}^{\setminus}| \approx 0$), and scoring degenerates to:
37	\begin{equation}
38	\label{eq:degenerate}
39	\text{score}(a) \approx \sum_{\substack{c \in \mathcal{C}^* \\ \text{source}(c) \to a}} w_c,
40	\end{equation}
41	equivalent to majority voting. We show in \S\ref{sec:confirmation-bias} that this degeneration occurs in practice.
42	
43	\paragraph{The $C_0$ diagnostic.} The multi-candidate rate $C_0 = |\{q : |\mathcal{A}(q)| > 1\}| / |\mathcal{Q}|$ is a zero-cost diagnostic: $C_0 < 5\%$ means SICA reduces to SC. $\alpha = 0.5$ is not critical (${\pm}0.49$\,pp across $\alpha \in [0, 1]$).
44	
45	\subsection{The Symbolic Mirage Hypothesis}
46	\label{sec:mirage}
47	
48	We hypothesize that self-extracted symbolic structures are not independent verification signals but projections of the generating model's distributional biases. This \textbf{Symbolic Mirage} is specific to self-extracted constraints; symbolic methods employing independently sourced constraints remain effective (Appendix~\ref{app:oracle}). Unlike general self-correction failure \citep{huang2024selfcorrect}, the symbolic mirage is specific to formal verification: the solver is provably sound, yet its outputs are informationally equivalent to majority voting because self-extracted inputs carry the model's distributional prior. We quantify mirage intensity via the \emph{Bias Ratio}:
49	\begin{equation}
50	\label{eq:mirage}
51	\text{BR}(M,T) = \frac{P(c \text{ supports } a_M \mid a_M \neq a^*)}{P(c \text{ supports } a^* \mid a_M \neq a^*)},
52	\end{equation}
53	where $c$ is a self-extracted constraint, $a_M$ the model's answer, and $a^*$ the ground truth. $\text{BR} > 1$ indicates constraints project model bias rather than provide independent verification. The mirage degrades aggregation through two channels: correlated constraints compress $K_{\text{eff}} < 2$ (\emph{direct}; Eq.~\ref{eq:effk}), and answer-coupled constraints collapse MAX-SAT to vote counting (\emph{indirect}; Eq.~\ref{eq:degenerate}). If traces are unfaithful \citep{turpin2024language}, the mirage is inherent to extraction. Two observations motivate the hypothesis: (O1)~BR $> 1.0$ across all tested self-extraction conditions (\S\ref{sec:confirmation-bias}); (O2)~no training-free remediation reduces BR below $1.0$ (\S\ref{sec:remediation})---both initially observed on Mistral-7B and subsequently confirmed across nine models. These lead to a testable prediction: (P1)~structurally independent verification should break SCB (\S\ref{sec:cross-arch}).
54	
55	\begin{tcolorbox}[enhanced, colback=gray!5, colframe=gray!50, boxrule=0.3pt, left=3pt, right=3pt, top=1pt, bottom=1pt, before skip=4pt, after skip=4pt]
56	\textbf{Empirical Finding 1} (Self-Extraction Ceiling).\label{prop:ceiling}
57	For generator $M$ with $\text{BR}(M) > 1$ and oracle improvement $\Delta_\text{oracle}$, self-extracted constraints improve SC by at most $\Delta_\text{max}^\text{self}$, empirically bounded by $\Delta_\text{oracle} / \text{BR}(M)$.
58	\end{tcolorbox}
59	
60	\begin{tcolorbox}[enhanced, colback=gray!5, colframe=gray!50, boxrule=0.3pt, left=3pt, right=3pt, top=1pt, bottom=1pt, before skip=4pt, after skip=4pt]
61	\textbf{Empirical Finding 2} (Capability Gap Condition).\label{cor:capability_gap}
62	Let $G$ be a generator with SC accuracy $\text{SC}_G$ and let $V$ be an external verifier with standalone accuracy $V_\text{acc}$ and inter-system correlation $\rho_{GV} < \rho_{GG}$. Combo gain $\Delta_\text{combo} - \Delta_\text{SC}$ decreases monotonically with $\text{SC}_G$, with significant gains observed up to $\text{SC}_G \approx 70\%$.
63	\end{tcolorbox}
64	
65	\textit{Empirical support.} From Finding~1, adding $V$ with $\rho_{GV} < \rho_{GG}$ increases $K_\text{eff}^\text{combo}$. Empirically, combo gain decreases monotonically with $\text{SC}_G$ ($\rho = 1.0$, $p = 0.003$, $n{=}6$; \S\ref{sec:cross-arch}), with significant improvements even when $\text{SC}_G > V_\text{acc}$.
66	
67	We also define a Conditional Correction Ratio (CCR, Appendix~\ref{app:cil}) that summarizes these diagnostics.
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c2580d1-13d3-46c4-b8ac-bff801a2a3ea",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "dac58cf9-1134-43e3-8105-bf99392ae074",
  "sourceToolAssistantUUID": "0c2580d1-13d3-46c4-b8ac-bff801a2a3ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T01:05:28.466Z_

<details open><summary>🔧 Tool call — Read · `toolu_01La4j9EKZds1NoN5Y2bXtwg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dac58cf9-1134-43e3-8105-bf99392ae074",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbudDokWMMiSaZBmfsL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cda158f2-ddb8-4c70-a870-20d604b969bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QSkYpTMbuNzhTLHA3ypvD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7501,
      "cache_read_input_tokens": 20131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7501,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T01:05:28.480Z_

<details><summary>↩ Tool result · `toolu_01La4j9EKZds1NoN5Y2bXtwg`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\looseness=-1 We test the three predictions of the symbolic mirage hypothesis (\S\ref{sec:mirage}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	\looseness=-1 Table~\ref{tab:independence} (Appendix) reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$ as an ordinal diagnostic: higher $K_{\text{eff}}$ indicates greater vote diversity, though it should not be interpreted as a literal effective sample size (\S\ref{sec:condorcet}). Across four Mistral-7B seeds, $\kappa \in [0.41, 0.51]$ yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp, indicating seed-level constraint quality matters beyond independence. Positive $\Delta$ requires both sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ degrades). All four model families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}).
10	
11	
12	\subsection{Symbolic Confirmation Bias}
13	\label{sec:confirmation-bias}
14	
15	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. A shuffle control reveals this bias is \emph{structural}: randomizing constraint--answer associations while preserving per-trace counts yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($p > 0.7$), indicating that BR reflects the trace-count distribution rather than extraction-specific error. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems on Mistral-7B FOLIO (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting. This vacuity is $\alpha$-insensitive: agreement $\geq$99\% across $\alpha \in \{0.1, \ldots, 0.9\}$ for both high- and moderate-BR conditions (Table~\ref{tab:alpha-ablation}).
16	
17	\looseness=-1 This pattern generalizes: $4.97\times$ (Mistral), $3.85\times$ (Qwen-14B), $2.88\times$ (LLaMA), all $> 1.0$ with 95\% bootstrap CIs (Table~\ref{tab:cross-model-bias}). Cross-model extraction confirms SCB universality across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{tab:frontier-scb}). BR $> 1$ further holds across all eight cells of a $2{\times}2$ generator${\times}$extractor matrix on FOLIO and ProofWriter (range $1.94$--$2.70$; Appendix~\ref{app:2x2}). Constraints use trace-specific variables (56.4\% zero cross-answer overlap), collapsing aggregation to majority voting.
18	
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3pt}
23	\caption{Symbolic confirmation bias across nine models on FOLIO ($n = 204$). BR: mean per-problem bias ratio. $n_\text{err}$: number of incorrect instances on which BR is computed. $\Delta$: SICA $-$ SC (pp). Ext.: $^a$self-extraction; $^b$cross-model (Mistral-7B extracts FOL from target traces). $^*$Interim ($n = 95/204$). All models exhibit $\text{BR} > 1$; BR estimates for high-accuracy models ($n_\text{err} < 40$) have wider confidence intervals; Gemini ($n_\text{err} \approx 12$) should be interpreted with particular caution. Process-level similarity ($\kappa_{\text{proc}}$) ranges from $0.25$ (R1-Distill) to $0.79$ (gpt-4o/4.1/Gemini); see Table~\ref{tab:cross-model-process}.}
24	\label{tab:frontier-scb}
25	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llrrrrl@{}}
26	\toprule
27	Model & Ext. & SC (\%) & $n_\text{err}$ & BR & $\Delta$ (pp) \\
28	\midrule
29	Mistral-7B & $^a$ & 55.88 & 90 & 4.97 & 0.00 \\
30	LLaMA-8B & $^a$ & \textrm{---} & \textrm{---} & 2.88 & \textrm{---} \\
31	Qwen-14B & $^a$ & 75.98 & 49 & 3.85 & $-$0.49 \\
32	\addlinespace
33	R1-Distill-8B & $^b$ & 74.51 & 52 & 2.92 & $+$2.45 \\
34	gpt-4o & $^a$ & 73.91 & 53 & 2.94 & $-$1.80 \\
35	gpt-4.1 & $^b$ & 82.84 & 35 & 2.70 & $-$1.47 \\
36	gpt-5.5 & $^b$ & 84.31 & 32 & 3.48 & $+$0.49 \\
37	o3 & $^b$ & 82.65 & 35 & 1.66 & 0.00 \\
38	Gemini-2.5-Pro$^*$ & $^b$ & 87.37 & 12 & 2.79 & $-$1.10 \\
39	\bottomrule
40	\end{tabular}}
41	\end{table}
42	
43	\looseness=-1 Two controls rule out answer leakage. BR is uniform across early, mid, and late reasoning steps (Fisher $p = 0.71$); high-consensus errors amplify to $\text{BR} = 18.8\times$ versus $2.7\times$ for low-consensus ($p < 0.001$). Removing the answer sentence from traces before extraction yields no BR decrease (Wilcoxon $p \geq 0.12$) despite significant accuracy loss (McNemar $p < 0.013$). SCB reflects a distributional prior embedded throughout reasoning, not answer contamination.
44	
45	\subsection{Process-Level Independence}
46	\label{sec:process-kappa}
47	
48	\looseness=-1 We quantify reasoning-process overlap via ProcessSim, the mean pairwise cosine similarity of TF-IDF trace vectors (Eq.~\ref{eq:process-sim}, Appendix~\ref{app:process-gradient}). ProcessSim captures lexical overlap; deeper structure measures may reveal additional patterns, so we treat it as supporting rather than primary evidence. On Mistral-7B FOLIO, mean ProcessSim $= 0.69$, far exceeding answer-level $\kappa = 0.46$: traces share reasoning processes even when answers diverge. The gap generalizes across four families (Table~\ref{tab:cross-model-process}), from $0.31$ (LLaMA) to $0.02$ (Qwen-14B). Under cross-model extraction, SICA gain decreases monotonically with ProcessSim ($\rho = -1.0$, $p = 0.008$; Table~\ref{tab:process-gradient}), modulated by self-bias severity.
49	
50	
51	CCR analysis confirms the same pattern: cross-architecture NLI yields $\text{CCR} > 0$ while same-model SICA yields $\text{CCR} < 0$, with CCR correlating with combo gain ($\rho = 0.84$, $p = 0.014$; Appendix~\ref{app:cil}).
52	
53	\subsection{Remediation Analysis}
54	\label{sec:diagnostics}
55	\label{sec:remediation}
56	\label{sec:interventions}
57	
58	\looseness=-1 All 27 training-free remediation strategies spanning four categories produce neutral-to-negative results (Figure~\ref{fig:interventions-summary}; Appendices~\ref{app:extraction}--\ref{app:entropy}). Four representative failure modes illuminate the independence-accuracy trade-off. \emph{Debate} ($\kappa = 0.15$, $\Delta = -18.6$\,pp) successfully breaks trace correlation but collapses accuracy---same-model diversity and quality are at odds. \emph{Cross-model extraction} (using a different LLM as extractor) decreases $\kappa$ slightly but $\Delta \approx 0$, because same-family models share systematic biases (Appendix Table~\ref{tab:kappa_generalization}). \emph{Contrastive prompting} produces imbalanced output (94 pro vs.\ 65 con constraints), indicating confirmation bias transfers to constraint generation. The \emph{oracle ceiling} ($+29.90$\,pp with gold constraints) proves the mechanism is sound; self-extraction captures only ${\sim}$12\%, localizing the bottleneck to extraction quality. All non-debate strategies cluster at $\kappa \approx 0.40$--$0.47$, a same-model ceiling across three families. No individual strategy achieves significance after correction (Appendix~\ref{app:intervention-individual}).
59	
60	\begin{figure}[t]
61	\centering
62	\includegraphics[width=\columnwidth]{figures/fig2_interventions_compact.pdf}
63	\caption{Twenty-three of 27 training-free strategies across four categories (four additional strategies tested but omitted for clarity). All produce neutral-to-negative $\Delta$ vs.\ SC. Grey band: $\pm 1$\,pp noise zone.}
64	\label{fig:interventions-summary}
65	\end{figure}
66	
67	\paragraph{Prospective held-out validation.}
68	\looseness=-1 Decision boundaries ($C_0 < 5\%$, $K_\text{eff} \leq 1.3$, SC $< 40\%$) were derived from Mistral-7B and Qwen2.5-14B conditions. We evaluate prospectively on held-out LLaMA-3.1-8B, a different model family not used in boundary derivation: on FOLIO (SC $= 66.18\%$, $C_0 = 61.8\%$, $K_\text{eff} = 2.17$), the framework predicts Type~A confirmation bias ($\Delta \leq 0$); the observed $\Delta = -4.41$\,pp confirms the prediction.
69	
70	\paragraph{Symbolic Mirage Hypothesis: verification.}
71	\looseness=-1 The observations and prediction of \S\ref{sec:mirage} are confirmed. Observations O1--O2, initially discovered on Mistral-7B, generalize: BR $> 1$ across three self-extraction models, six cross-model pairs, and all eight cells of a $2{\times}2$ generator${\times}$extractor matrix (\S\ref{sec:confirmation-bias}); 27 training-free strategies fail to reduce BR below 1.0 (\S\ref{sec:remediation}). Prediction P1 is validated: cross-architecture NLI escapes the mirage for generators up to SC $\approx 70\%$ (\S\ref{sec:cross-arch}).
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cda158f2-ddb8-4c70-a870-20d604b969bb",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "becdea9d-3a35-4201-bdf1-c19e8155c897",
  "sourceToolAssistantUUID": "cda158f2-ddb8-4c70-a870-20d604b969bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T01:05:28.618Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ESZHPNymAceXeUzysVm8Hz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "becdea9d-3a35-4201-bdf1-c19e8155c897",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbudDokWMMiSaZBmfsL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "046378a4-07b5-4153-80e7-ca6677bbd22e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QSkYpTMbuNzhTLHA3ypvD7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7501,
      "cache_read_input_tokens": 20131,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7501
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 254,
          "cache_read_input_tokens": 20131,
          "cache_creation_input_tokens": 7501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7501,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T01:05:28.950Z_

<details><summary>↩ Tool result · reported error · `toolu_01ESZHPNymAceXeUzysVm8Hz`</summary>

```text
File content (30865 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "046378a4-07b5-4153-80e7-ca6677bbd22e",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "bf8ac896-5ad6-4927-9010-e580f38fecea",
  "toolUseResult": "Error: File content (30865 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "046378a4-07b5-4153-80e7-ca6677bbd22e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-23T01:05:39.259Z_

Let me search more specifically for notation definitions and read the appendix in chunks:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf8ac896-5ad6-4927-9010-e580f38fecea",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuoPVYDmLQfL3QwLie",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd7379e9-7152-4820-86b7-5c0c8f9165ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QaNfuWBTnLBFAUpuV8574N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6324,
      "cache_read_input_tokens": 27632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6324,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T01:05:43.797Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ht6uaH1FPJ8sRaRt61Vj6a`</summary>

```json
{
  "pattern": "\\\\(SCB|BR|SICA|C_0|K_\\\\\\\\text\\{eff\\}|\\\\\\\\sigma|\\\\\\\\mathcal\\{C\\})",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd7379e9-7152-4820-86b7-5c0c8f9165ca",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuoPVYDmLQfL3QwLie",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bbfe4eaa-749e-44e3-a7e6-d4ab168447b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QaNfuWBTnLBFAUpuV8574N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6324,
      "cache_read_input_tokens": 27632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6324,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T01:05:43.829Z_

<details><summary>↩ Tool result · `toolu_01Ht6uaH1FPJ8sRaRt61Vj6a`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbfe4eaa-749e-44e3-a7e6-d4ab168447b1",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "f13b8d7d-0b31-4ef8-9cc9-5433de38a689",
  "sourceToolAssistantUUID": "bbfe4eaa-749e-44e3-a7e6-d4ab168447b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T01:05:43.952Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TLN8bG2PmVmfu1BBihhhde`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f13b8d7d-0b31-4ef8-9cc9-5433de38a689",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbuoPVYDmLQfL3QwLie",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "61eeb985-8474-4db7-9b8a-ea2ae0f4a83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QaNfuWBTnLBFAUpuV8574N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6324,
      "cache_read_input_tokens": 27632,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6324
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 303,
          "cache_read_input_tokens": 27632,
          "cache_creation_input_tokens": 6324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6324,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T01:05:43.959Z_

<details><summary>↩ Tool result · `toolu_01TLN8bG2PmVmfu1BBihhhde`</summary>

```text
1	\section{Regime Scatter Plot}
2	\label{app:regime-scatter}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{f2_regime_scatter}
7	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--60\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.112$).}
8	\label{fig:regime-scatter}
9	\end{figure}
10	
11	\section{Prompt Templates}
12	\label{app:prompts}
13	
14	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
15	
16	\paragraph{System Prompt.}
17	
18	\begin{lstlisting}
19	You are a constraint extraction tool. Output ONLY
20	valid JSON. Do NOT solve problems, reason about
21	correctness, or think step-by-step. Extract
22	constraints from the given trace exactly as stated.
23	\end{lstlisting}
24	
25	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
26	
27	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
28	
29	\begin{lstlisting}
30	Extract mathematical constraints from this reasoning
31	trace as a JSON object.
32	
33	Rules:
34	- type: "equation", "inequality", or "predicate"
35	- expression: human-readable, e.g. "x + y == 14"
36	- z3_formula: a single comparison expression in
37	  Python Z3 syntax
38	- source_step: step number where the constraint
39	  appears
40	- Use variable names from the trace
41	
42	z3_formula MUST follow these rules:
43	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
44	  /, **, %
45	- Use individual named variables: a1, a2, a3...
46	  NOT arrays a[1] or sets A
47	- Expand all sums explicitly:
48	  "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
49	- NO Python builtins: sum(), len(), max(), min(),
50	  list(), set(), range(), int()
51	- Each z3_formula must be exactly ONE comparison
52	  (==, !=, <, >, <=, >=)
53	- For multiple values, write separate constraints
54	  for each
55	
56	Output ONLY the JSON below, nothing else:
57	{"constraints": [{"type": "equation",
58	  "expression": "x + y == 14",
59	  "z3_formula": "x + y == 14",
60	  "source_step": 1}],
61	 "answer": "final_answer",
62	 "variables": ["x", "y"]}
63	
64	Trace:
65	{trace}
66	\end{lstlisting}
67	
68	\paragraph{Logical Constraint Extraction (LOGIC\_EXTRACTION\_PROMPT).}
69	
70	Used for ProofWriter and FOLIO datasets.
71	
72	\begin{lstlisting}
73	IMPORTANT: You are an EXTRACTION tool, NOT a problem
74	solver.
75	- Do NOT re-solve or re-reason about the problem.
76	- Do NOT verify whether the trace's reasoning is
77	  correct.
78	- ONLY extract the logical constraints that are
79	  explicitly stated or used in the trace below.
80	- Output ONLY the JSON object, nothing else.
81	
82	Extract logical constraints from this reasoning trace
83	about a logic problem.
84	
85	The problem has facts (base assertions), rules
86	(grounded implications), and derived conclusions.
87	Convert each into a Z3 boolean formula.
88	
89	Variable naming:
90	- Unary property: property_entity
91	  (e.g., kind_anne, red_charlie, round_fiona)
92	- Binary relation: relation_subject_object
93	  (e.g., eats_bear_squirrel, likes_lion_cat)
94	- Use lowercase with underscores only
95	
96	Constraint types:
97	- "fact": a given assertion,
98	  e.g., kind_anne == True
99	- "rule": a grounded implication over specific
100	  entities, e.g., Implies(kind_anne, nice_anne)
101	- "derived": an inferred conclusion from facts +
102	  rules, e.g., nice_anne == True
103	
104	Z3 operators:
105	- Implies(a, b) for if-then rules
106	- And(a, b, ...) for conjunctive conditions
107	- Or(a, b, ...) for disjunctive conditions
108	- Not(a) for negation
109	- == True / == False for boolean assertions
110	
111	Output ONLY the JSON below, nothing else:
112	{"constraints": [{"type": "fact",
113	  "expression": "kind(anne)",
114	  "z3_formula": "kind_anne == True",
115	  "source_step": 1}],
116	 "answer": "True or False or Unknown",
117	 "variables": ["kind_anne"]}
118	
119	Trace:
120	{trace}
121	\end{lstlisting}
122	
123	\paragraph{Output Schema.}
124	
125	Both prompts produce a JSON object with the following structure:
126	
127	\begin{lstlisting}
128	{
129	  "constraints": [
130	    {
131	      "type": "&lt;equation|inequality|predicate>
132	               or &lt;fact|rule|derived>",
133	      "expression": "&lt;human-readable description>",
134	      "z3_formula": "&lt;Z3-compatible expression>",
135	      "source_step": &lt;integer>
136	    }
137	  ],
138	  "answer": "&lt;final answer string>",
139	  "variables": ["&lt;var1>", "&lt;var2>", "..."]
140	}
141	\end{lstlisting}
142	
143	The pipeline additionally injects an \texttt{answer\_assertion} constraint per trace (not produced by the LLM):
144	
145	\begin{lstlisting}
146	{"type": "answer_assertion",
147	 "expression": "answer is &lt;ans>",
148	 "z3_formula": "__sica_answer_&lt;ans> == True",
149	 "source_step": -1}
150	\end{lstlisting}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61eeb985-8474-4db7-9b8a-ea2ae0f4a83b",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "288961c8-37f3-400d-8971-e0cd2c9ecb3c",
  "sourceToolAssistantUUID": "61eeb985-8474-4db7-9b8a-ea2ae0f4a83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-23T01:05:45.257Z_

Good! Now let me search for additional notation definitions and check the introduction file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "288961c8-37f3-400d-8971-e0cd2c9ecb3c",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbvv7ad7hHwJZJABA4y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "67a6bcdb-417e-4ade-880f-ad86e969f78f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TeCjzhTzHzQkBG9S1yVRXN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2233,
      "cache_read_input_tokens": 33956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2233,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T01:05:46.106Z_

<details open><summary>🔧 Tool call — Read · `toolu_015Ca5o7wTvFiJmX3UVeUM8P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67a6bcdb-417e-4ade-880f-ad86e969f78f",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbvv7ad7hHwJZJABA4y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f8c0fa5e-b9df-4fc3-b09a-a0d8256cc63d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TeCjzhTzHzQkBG9S1yVRXN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2233,
      "cache_read_input_tokens": 33956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2233,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T01:05:46.111Z_

<details><summary>↩ Tool result · `toolu_015Ca5o7wTvFiJmX3UVeUM8P`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\text{eff}}$ as an ordinal diagnostic of vote diversity ($K_{\text{eff}} \approx 1.2$--$3.6$ for nominal $K = 12$; \S\ref{sec:condorcet}).
17	Chain-of-thought cosine similarity ($0.69$) far exceeds answer-level $\kappa$ ($0.46$), revealing that traces share reasoning processes even when they diverge on final answers (\S\ref{sec:process-kappa}).
18	When the same model extracts logical constraints from these correlated traces, the constraints exhibit \emph{symbolic confirmation bias} (SCB): on problems where the model errs, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratios $1.66$--$4.97\times$ across nine models), and 94\% of errors overlap with SC (\S\ref{sec:confirmation-bias}).
19	A shuffle control shows this bias is structural: it reflects the trace-count distribution rather than extraction-specific error.
20	Self-extraction cannot supply the independent signal that CJT requires.
21	
22	We study this through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}).
23	Across six open-source models (7B--32B), three domains (FOLIO \citep{han2022folio}, ProofWriter \citep{tafjord2021proofwriter}, LogiQA \citep{liu2020logiqa}), and over 3,000 condition-evaluations with four-seed replication, twenty-seven training-free remediation strategies spanning fifteen families all produce neutral or negative results (Table~\ref{tab:main_results}).
24	Prior work shows LLMs struggle with natural-language self-correction \citep{huang2024selfcorrect} and that LLM-generated logical formulas can be unreliable \citep{stechly2025selfverification}. Our formal channel is provably sound---the failure is precisely localizable to the extraction step. The assumption that formalizing reasoning provides \emph{independent} verification evidence fails not because Z3 is unreliable (99\% of constraints are syntactically valid), but because extraction inherits the model's biases: MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems, rendering the formal layer vacuous.
25	
26	Oracle controls confirm the mechanism is sound ($+29.90$\,pp Mistral-7B, $+13.73$\,pp Qwen-14B on FOLIO, $p < 0.001$; Appendix~\ref{app:oracle}), yet self-extraction captures only ${\sim}$12\% of this ceiling.
27	The central finding is a persistent independence-accuracy trade-off \citep{krogh1994neural}: Debate reduces $\kappa$ to 0.15 but collapses accuracy ($-18.6$\,pp); other methods cluster at $\kappa \approx 0.40$--$0.47$, a same-model ceiling across three families (\S\ref{sec:remediation}).
28	A cross-architecture proof-of-concept escapes the bottleneck: zero-shot DeBERTa NLI yields $+6.67$\,pp on Mistral-7B ProofWriter ($p < 0.001$) but no significant gain for stronger generators; domain-adapted NLI amplifies gains to $+$12--26\,pp ($p < 0.0001$), extending to generators with SC up to 72\% (\S\ref{sec:cross-arch}).
29	
30	Our contributions are:
31	\begin{enumerate}[nosep,leftmargin=*]
32	\item \textbf{Quantifying symbolic confirmation bias in formal self-verification.} While the general difficulty of LLM self-correction is known \citep{huang2024selfcorrect}, we provide the first quantitative characterization of symbolic confirmation bias in formal self-verification, demonstrating that provably sound verification machinery becomes informationally vacuous under self-extraction: 83.3\% of self-extracted constraints support the wrong answer (BR $1.66$--$4.97\times$ across nine models), yet 99\% pass Z3 validation. A shuffle control and MAX-SAT ablation show this bias is structural---the formal layer adds no information beyond majority voting. Twenty-seven training-free strategies fail to break it; cross-model extraction confirms universality across nine models from 7B to frontier (\S\ref{sec:confirmation-bias}).
33	
34	\item \textbf{General diagnostic framework for trace-aggregation methods.} Three diagnostics ($K_\text{eff}$, BR, $C_0$) correctly predict success or failure across all 60 tested conditions spanning self-extraction, training-free remediation, cross-architecture verification, and oracle controls. Decision boundaries---$C_0 < 5\%$ (degenerate), $K_\text{eff} \leq 1.3$ (diversity-limited), $\text{BR} > 2\times$ (bias-dominated), $\kappa_\text{same} \geq 0.40$ (same-model ceiling)---provide zero-cost prediction of symbolic aggregation viability. The framework extends to any method extracting structured representations from LLM traces (\S\ref{sec:remediation}, \S\ref{sec:cross-arch}).
35	
36	\item \textbf{Process-level independence analysis.} CoT cosine similarity ($0.69$--$0.79$) exceeds answer-level $\kappa$ ($0.45$--$0.74$) across four models from three families; under cross-model extraction on frontier models, SICA gain decreases monotonically with process similarity ($\rho = -1.0$, $p = 0.008$; \S\ref{sec:process-kappa}).
37	\end{enumerate}
38	
39	\begin{figure}[t]
40	\centering
41	\small
42	\resizebox{\columnwidth}{!}{\begin{tikzpicture}[
43	    node distance=0.3cm and 0.1cm,
44	    box/.style={draw, rounded corners=2pt, minimum height=0.55cm,
45	                text width=1.2cm, align=center, font=\scriptsize},
46	    arr/.style={-{Stealth[length=4pt]}, thick},
47	    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},
48	    lbl/.style={font=\scriptsize, text=gray!70!black},
49	    ibottle/.style={draw=red!70!black, densely dashed, rounded corners=3pt,
50	                    inner sep=3pt},
51	]
52	\node[box] (q) {Question $q$};
53	\node[box, right=of q] (sample) {Sample $K$\\traces};
54	\node[box, right=of sample] (extract) {Extract logical\\constraints};
55	\node[box, right=of extract] (dedup) {Dedup.\ +\\weight};
56	\node[box, right=of dedup] (maxsat) {MAX-SAT\\(Z3)};
57	
58	\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};
59	\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\vote};
60	
61	\draw[arr] (q) -- (sample);
62	\draw[arr] (sample) -- (extract);
63	\draw[arr] (extract) -- (dedup);
64	\draw[arr] (dedup) -- (maxsat);
65	\draw[arr] (maxsat) -- (ans);
66	\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);
67	
68	\node[lbl, above=0.01cm of maxsat] {SICA};
69	
70	\node[ibottle, fit=(sample)(extract), label={[font=\scriptsize\itshape, text=red!70!black]above:Independence Bottleneck}] {};
71	
72	\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};
73	\end{tikzpicture}}
74	\caption{The SICA pipeline. SC selects the majority answer from $K$ traces. SICA extracts logical constraints, deduplicates, and solves MAX-SAT via Z3. Red dashed box: the independence bottleneck. Dashed arrow: oracle variant with gold FOL.}
75	\label{fig:pipeline}
76	\end{figure}
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8c0fa5e-b9df-4fc3-b09a-a0d8256cc63d",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "b5534bf1-ece4-4e74-a2f8-6c4e9c1b6dc6",
  "sourceToolAssistantUUID": "f8c0fa5e-b9df-4fc3-b09a-a0d8256cc63d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T01:05:46.550Z_

<details open><summary>🔧 Tool call — Read · `toolu_015PMEqe5e5TYK5i33JuZCAg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5534bf1-ece4-4e74-a2f8-6c4e9c1b6dc6",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbvv7ad7hHwJZJABA4y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "22410492-fb81-42cc-b583-66ecbbd064f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TeCjzhTzHzQkBG9S1yVRXN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2233,
      "cache_read_input_tokens": 33956,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2233,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T01:05:46.556Z_

<details><summary>↩ Tool result · `toolu_015PMEqe5e5TYK5i33JuZCAg`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models, three reasoning domains, and over 3,000 condition-evaluations (${\sim}$1,250 unique instances), with diagnostic analyses of confirmation bias and process-level independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B). We additionally evaluate SCB universality via cross-model extraction on five frontier models (gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro; Table~\ref{tab:frontier-scb}), where Mistral-7B extracts constraints from the target model's traces since closed-source APIs do not expose internals suitable for self-extraction.
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} (exploratory, $n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline, revealing three observation-driven accuracy regimes.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}16$). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,uncorrected $p < 0.05$ (BH adj.\ $p = 0.112$); $^{3s}$\,3-seed; $^{4s}$\,4-seed confirmatory (unmarked: single-seed exploratory). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME, Qwen2.5-14B GSM8K) yield $\Delta = 0$; oracle upper bounds are reported in Appendix~\ref{app:oracle}.}
25	\label{tab:main_results}
26	\begin{tabular}{@{}llrrrrl@{}}
27	\toprule
28	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
29	\midrule
30	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
31	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
32	\midrule
33	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--60\%, Mistral-7B only)}} \\
34	Mistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\
35	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
36	Mistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\
37	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
38	Mistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\
39	\midrule
40	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
41	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
42	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
43	\addlinespace
44	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
45	Qwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\mathbf{-2.50}$ & 0.011{*} \\
46	Qwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.98 & 75.49 & $-$0.49 & 1.000 \\
47	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
48	Qwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\
49	\addlinespace
50	Qwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\
51	Qwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\
52	Qwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\
53	\bottomrule
54	\end{tabular}
55	\end{table*}
56	
57	\looseness=-1 No non-degenerate condition shows a significant SICA effect after FDR control (BH, $m{=}16$). Two show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$); adjusted $p = 0.112$ for both. The intermediate-SC region (50--60\%) contains the only positive trends, none reaching $p < 0.05$. An aggregate sign test across self-extraction conditions yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). Three-seed replication on Mistral-7B confirms seed-level noise: two of three seeds produce null or negative $\Delta$ (mean $+0.16 \pm 2.70$\,pp; Table~\ref{tab:multi-seed}). Four-seed replication on Qwen2.5-14B $\times$ FOLIO confirms the single-seed pattern: $\Delta \in [0.00, -2.01]$\,pp (mean $-1.24 \pm 0.86$; Table~\ref{tab:multi-seed}). TOST equivalence tests \citep{lakens2017equivalence} with margin $\pm 2$\,pp confirm 4 equivalent, 2 genuinely different (both negative), 10 underpowered. For the 10 underpowered conditions, our tests cannot rule out effects smaller than 1.86--4.84\,pp at 80\% power; the largest study ($n{=}804$) achieves MDE $= 1.86$\,pp (Appendix~\ref{app:power}). Absence of evidence is not evidence of absence for small effects. Margin sensitivity is robust: at $\pm 1$\,pp, 0/16 equivalent; at $\pm 3$\,pp, 10/16 equivalent; no margin yields a significant positive effect (Appendix Table~\ref{tab:tost-sensitivity}). We adopt $\pm 2$\,pp based on the lower bound of SC literature gains (2--5\,pp \citep{wang2023sc}), acknowledging this choice is anchored to SC effect sizes. We trace the failure below.
58	
59	
60	\looseness=-1 Oracle controls replacing self-extracted constraints with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\,pp FOLIO, $+17.17$\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\sim}$12\% of this ceiling (Appendix~\ref{app:oracle}).
61	
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22410492-fb81-42cc-b583-66ecbbd064f4",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "34fb8464-e2a8-4365-bb22-178971e2f0f6",
  "sourceToolAssistantUUID": "22410492-fb81-42cc-b583-66ecbbd064f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T01:05:47.213Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AmxQ2RmfcMPLmsn35m3Xvd`</summary>

```json
{
  "pattern": "C_0|multi-candidate|trace|reasoning trace|constraint",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34fb8464-e2a8-4365-bb22-178971e2f0f6",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbvv7ad7hHwJZJABA4y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d12696e3-4c1d-41f2-aeca-db9db746296a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TeCjzhTzHzQkBG9S1yVRXN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2233,
      "cache_read_input_tokens": 33956,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2233
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 332,
          "cache_read_input_tokens": 33956,
          "cache_creation_input_tokens": 2233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2233,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T01:05:47.228Z_

<details><summary>↩ Tool result · `toolu_01AmxQ2RmfcMPLmsn35m3Xvd`</summary>

```text
4-\subsection{Self-Consistency and the Condorcet Independence Assumption}
5-\label{sec:condorcet}
6-
7:Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees majority convergence under independent voters \citep{austensmith1996}, but LLM traces violate this independence. Following \citet{ladha1992correlated} and \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8-\begin{equation}
9-\label{eq:effk}
10-K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa].
--
13-\subsection{SICA Pipeline}
14-\label{sec:pipeline}
15-
16:Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
17-
18:\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
19-
20:[Omitted long matching line]
21-
22:\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
23-\begin{equation}
24-\label{eq:maxsat}
25-\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
26-\end{equation}
27:Z3 \citep{demoura2008z3} solves this with a 10-second timeout. Answer assertion constraints ($\texttt{answer\_a} == \texttt{True}$, weight 1) ensure every candidate receives a nonzero base score, making SICA a strict generalization of SC.
28-
29-\paragraph{Scoring.} Let $\mathcal{C}^{\setminus} = \mathcal{C} \setminus \mathcal{C}^*$. Each candidate $a$ is scored by:
30-\begin{equation}
31-\label{eq:score}
32-\text{score}(a) = \sum_{c \in \mathcal{C}^*} w_c \cdot \sigma(c, a) - \alpha \sum_{c \in \mathcal{C}^{\setminus}} w_c \cdot \sigma(c, a),
33-\end{equation}
34:where $\sigma(c, a) = 1$ if $c$ was extracted from any trace producing answer $a$, and $\alpha = 0.5$. The selected answer is $a^* = \arg\max_{a} \text{score}(a)$.
35-
36:\paragraph{Degeneration condition.} If self-extracted constraints are coupled to their source answer, MAX-SAT retains nearly all ($|\mathcal{C}^{\setminus}| \approx 0$), and scoring degenerates to:
37-\begin{equation}
38-\label{eq:degenerate}
39-\text{score}(a) \approx \sum_{\substack{c \in \mathcal{C}^* \\ \text{source}(c) \to a}} w_c,
40-\end{equation}
41-equivalent to majority voting. We show in \S\ref{sec:confirmation-bias} that this degeneration occurs in practice.
42-
43:\paragraph{The $C_0$ diagnostic.} The multi-candidate rate $C_0 = |\{q : |\mathcal{A}(q)| > 1\}| / |\mathcal{Q}|$ is a zero-cost diagnostic: $C_0 < 5\%$ means SICA reduces to SC. $\alpha = 0.5$ is not critical (${\pm}0.49$\,pp across $\alpha \in [0, 1]$).
44-
45-\subsection{The Symbolic Mirage Hypothesis}
46-\label{sec:mirage}
47-
48:[Omitted long matching line]
49-\begin{equation}
50-\label{eq:mirage}
51-\text{BR}(M,T) = \frac{P(c \text{ supports } a_M \mid a_M \neq a^*)}{P(c \text{ supports } a^* \mid a_M \neq a^*)},
52-\end{equation}
53:[Omitted long matching line]
54-
55-\begin{tcolorbox}[enhanced, colback=gray!5, colframe=gray!50, boxrule=0.3pt, left=3pt, right=3pt, top=1pt, bottom=1pt, before skip=4pt, after skip=4pt]
56-\textbf{Empirical Finding 1} (Self-Extraction Ceiling).\label{prop:ceiling}
57:For generator $M$ with $\text{BR}(M) > 1$ and oracle improvement $\Delta_\text{oracle}$, self-extracted constraints improve SC by at most $\Delta_\text{max}^\text{self}$, empirically bounded by $\Delta_\text{oracle} / \text{BR}(M)$.
58-\end{tcolorbox}
59-
60-\begin{tcolorbox}[enhanced, colback=gray!5, colframe=gray!50, boxrule=0.3pt, left=3pt, right=3pt, top=1pt, bottom=1pt, before skip=4pt, after skip=4pt]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d12696e3-4c1d-41f2-aeca-db9db746296a",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "4f232039-4008-4489-b48a-a446562bbad4",
  "sourceToolAssistantUUID": "d12696e3-4c1d-41f2-aeca-db9db746296a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-23T01:05:48.479Z_

Excellent! Now let me check if there's a main paper file in the root or other directories:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f232039-4008-4489-b48a-a446562bbad4",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbw9aD83Lz8ebr2DpbC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85972acf-6acb-426b-8ce2-39806fd4f0aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E1JqbwCtX597TjAwmLiLaK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7533,
      "cache_read_input_tokens": 36189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7533,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-23T01:05:49.380Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T1GeHHYzEqjPijSxEjbvjD`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus -name \"main.tex\" -o -name \"paper.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85972acf-6acb-426b-8ce2-39806fd4f0aa",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbw9aD83Lz8ebr2DpbC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01789685-d1b3-4bcd-a706-13a3b85eb2e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E1JqbwCtX597TjAwmLiLaK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7533,
      "cache_read_input_tokens": 36189,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7533
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 123,
          "cache_read_input_tokens": 36189,
          "cache_creation_input_tokens": 7533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7533,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-23T01:05:49.558Z_

<details><summary>↩ Tool result · `toolu_01T1GeHHYzEqjPijSxEjbvjD`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T155754/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T054054/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T051642/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01789685-d1b3-4bcd-a706-13a3b85eb2e1",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "f32b369b-9e0a-4a67-830e-c1de5fc04c46",
  "sourceToolAssistantUUID": "01789685-d1b3-4bcd-a706-13a3b85eb2e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-23T01:05:51.130Z_

Perfect! Now let me search for more specific notation definitions in the tex files to provide a comprehensive report:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f32b369b-9e0a-4a67-830e-c1de5fc04c46",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbwKTHH2sizAiWQG3rQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2aeff138-ec3c-4061-a4a5-c43b6f435d69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RjL7QtFmFdF2ZrWSSsWqUV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 43722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T01:05:51.872Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015oXEdoQwaBwVsrtRH51X3W`</summary>

```json
{
  "pattern": "degeneration|majority voting|answer assertion|deduplication",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2aeff138-ec3c-4061-a4a5-c43b6f435d69",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbwKTHH2sizAiWQG3rQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0b727a2-58e2-4ea3-9808-e3e30f7b6b7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RjL7QtFmFdF2ZrWSSsWqUV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 43722,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1141
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 190,
          "cache_read_input_tokens": 43722,
          "cache_creation_input_tokens": 1141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1141,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T01:05:51.885Z_

<details><summary>↩ Tool result · `toolu_015oXEdoQwaBwVsrtRH51X3W`</summary>

```text
docs/paper/analysis.tex:15:[Omitted long matching line]
docs/paper/analysis.tex:17:[Omitted long matching line]
docs/paper/method.tex:22:\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
docs/paper/method.tex:41:equivalent to majority voting. We show in \S\ref{sec:confirmation-bias} that this degeneration occurs in practice.
docs/paper/method.tex:48:[Omitted long matching line]
docs/paper/limitations_content.tex:1:[Omitted long matching line]
docs/paper/abstract.tex:1:Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
docs/paper/abstract.tex:4:[Omitted long matching line]
docs/paper/appendix.tex:162:Domain constraint variables (e.g., \texttt{x + y == 14}) and answer assertion variables (e.g., \texttt{\_\_sica\_answer\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.
docs/paper/appendix.tex:312:All three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.
docs/paper/appendix.tex:524:[Omitted long matching line]
docs/paper/appendix.tex:1190:\emph{Effective-K} ($K_\text{eff}$; Eq.~\ref{eq:effk}): compute Fleiss' $\kappa$ across $K$ traces, then $K_\text{eff} = 1 + (K-1)(1-\kappa)$. Threshold: $K_\text{eff} \leq 1.3$ never improves in our experiments---aggregation collapses to majority voting. $K_\text{eff} > 1.8$ is a necessary (not sufficient) condition for gain.
docs/paper/appendix.tex:1209:[Omitted long matching line]
docs/paper/introduction.tex:7:The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
docs/paper/introduction.tex:32:[Omitted long matching line]
docs/paper/diagnosis.tex:138:[Omitted long matching line]
docs/paper/related_work.tex:17:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0b727a2-58e2-4ea3-9808-e3e30f7b6b7f",
  "isSidechain": true,
  "promptId": "73d90633-9b3d-44bb-8d7b-f141a06d0b7a",
  "agentId": "a262722788ce57da0",
  "type": "user",
  "uuid": "471b6eb5-5732-4a1c-8bf1-938d9584607e",
  "sourceToolAssistantUUID": "a0b727a2-58e2-4ea3-9808-e3e30f7b6b7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-23T01:06:17.041Z_

Perfect! I have gathered comprehensive information. Let me compile the final report with all the relevant findings.

## Summary: Notation and Definitions in the Symb_Invariant_Consensus Project

### Main Paper File
**Primary location:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`

This is the main paper file that orchestrates the entire document structure through includes of specialized sections.

---

### Key Notation Definitions Found

#### **1. SCB (Symbolic Confirmation Bias)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex` (lines 12-18)

SCB is defined as the systematic alignment of self-extracted constraints with the model's majority answer:
- On Mistral-7B FOLIO: when SICA errs, 83.3% of constraints support the incorrect answer
- Bias ratio values across nine models: 1.66--4.97× all greater than 1.0
- SCB reflects a distributional prior embedded throughout reasoning, not answer contamination
- The bias is structural: randomizing constraint-answer associations while preserving per-trace counts yields the same BR distribution

#### **2. BR (Bias Ratio)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (lines 48-52)

Formal definition (Equation 1 - eq:mirage):
```tex
BR(M,T) = P(c supports a_M | a_M ≠ a*) / P(c supports a* | a_M ≠ a*)
```
Where:
- c = self-extracted constraint
- a_M = model's answer
- a* = ground truth answer
- BR > 1 indicates constraints project model bias rather than provide independent verification
- Empirical findings: BR > 1.0 across all tested self-extraction conditions

#### **3. SICA (Symbolic Invariant Consensus Aggregation)**
**Files:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (lines 13-42)

SICA extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset.

Key components:
- **Trace generation:** Question q generates K traces {t_1, ..., t_K} at temperature T=0.7
- **Constraint extraction:** Same LLM extracts logical constraints at T_ext=0.3
- **Extraction rate:** Fraction of traces yielding at least one parseable constraint (global average: 99.0% propositional, 1.0% with quantifiers)

#### **4. SC (Self-Consistency)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (lines 4-7)

SC samples K reasoning traces and selects the majority answer. Relies on the Condorcet Jury Theorem (CJT) for majority convergence under independent voters, but LLM traces violate this independence assumption.

#### **5. Traces (Reasoning Traces)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (line 18)

Defined as:
- K traces {t_1, ..., t_K} generated from question q at temperature T=0.7
- Each trace t_i yields answer a_i
- Traces are chain-of-thought reasoning sequences

#### **6. Constraints (Logical Constraints)**
**Files:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` and `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex` (lines 14-121)

Constraints are extracted in multiple types:
- **Mathematical:** equations, inequalities, predicates (Z3 syntax)
- **Logical:** facts, rules, derived conclusions (boolean formulas with Implies, And, Or, Not operators)
- **Answer assertions:** injected constraints of form "__sica_answer_&lt;ans> == True" (weight 1)

Deduplication ratio: Global average 46.0% by syntactic equivalence
Each unique constraint c_m receives weight w_m equal to number of source traces

#### **7. Constraints - MAX-SAT Formulation**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (lines 22-26)

Equation (eq:maxsat):
```tex
C* = arg max_{S ⊆ C} Σ_{c ∈ S} w_c  s.t.  S is satisfiable
```
Where:
- C = set of all constraints
- C* = largest-weight satisfiable subset
- w_c = weight of constraint c
- Solved by Z3 with 10-second timeout

#### **8. Degeneration Condition**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (lines 36-41)

When self-extracted constraints are coupled to their source answer, MAX-SAT retains nearly all (|C^∖| ≈ 0), and scoring degenerates to:
```tex
score(a) ≈ Σ_{c ∈ C* : source(c) → a} w_c
```
This is equivalent to majority voting, making the formal verification layer vacuous.

#### **9. C_0 (Multi-Candidate Rate)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (line 43)

Definition:
```tex
C_0 = |{q : |A(q)| > 1}| / |Q|
```
Where:
- q = questions
- A(q) = set of distinct candidate answers for question q
- Q = all questions
- Zero-cost diagnostic: C_0 < 5% means SICA reduces to SC
- Decision boundary: C_0 < 5% indicates degenerate conditions

#### **10. Scoring Function**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (lines 29-34)

Equation (eq:score):
```tex
score(a) = Σ_{c ∈ C*} w_c · σ(c,a) - α Σ_{c ∈ C^∖} w_c · σ(c,a)
```
Where:
- σ(c,a) = 1 if c was extracted from any trace producing answer a, else 0
- α = 0.5 (penalty parameter, not critical: ±0.49pp across α ∈ [0,1])
- a* = arg max_a score(a)
- C^∖ = C \ C* (unsatisfiable constraints)

#### **11. K_eff (Effective Sample Size)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex` (lines 7-11)

Equation (eq:effk):
```tex
K_eff = K / [1 + (K-1) · κ]
```
Where:
- K = number of traces
- κ = Fleiss' kappa (intraclass correlation proxy)
- Empirical range: κ = 0.21--0.82, yielding K_eff ≈ 1.2--3.6 for K=12
- Ordinal diagnostic of vote diversity (not a literal effective sample size)
- Decision boundary: K_eff ≤ 1.3 never improves in experiments

#### **12. Majority Voting**
**Files:** Multiple locations (introduction.tex, experiments.tex, method.tex)

Referenced as the baseline aggregation mechanism that SC implements. SICA degenerates to majority voting when constraints become answer-coupled. Agreement metrics show SICA produces identical outputs to majority voting on 94.4% of problems.

---

### Additional Key Findings from Papers

**Empirical Findings (method.tex, lines 55-63):**

**Empirical Finding 1 (Self-Extraction Ceiling):**
```
For generator M with BR(M) > 1 and oracle improvement Δ_oracle,
self-extracted constraints improve SC by at most Δ_max^self,
empirically bounded by Δ_oracle / BR(M).
```

**Empirical Finding 2 (Capability Gap Condition):**
```
For generator G with SC accuracy SC_G and external verifier V with
standalone accuracy V_acc and inter-system correlation ρ_GV < ρ_GG,
combo gain Δ_combo - Δ_SC decreases monotonically with SC_G.
```

---

### Paper Structure
The main paper at `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex` includes:
- `abstract.tex` - Project abstract
- `introduction.tex` - Problem motivation and contributions
- `method.tex` - **[PRIMARY NOTATION SOURCE]** Background, SICA pipeline, symbolic mirage hypothesis
- `related_work.tex` - Related work section
- `experiments.tex` - Experimental setup and main results
- `analysis.tex` - **[SECONDARY NOTATION SOURCE]** Analysis of confirmation bias, process-level independence
- `solutions.tex` - Proposed solutions and remediation strategies
- `discussion.tex` - Discussion of findings
- `limitations_content.tex` - Limitations section
- `appendix.tex` - **[COMPREHENSIVE DEFINITIONS]** Detailed prompts, notation reference (line 1190+), oracle controls, additional analyses

---

All `.tex` files with notation are in `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/` directory, with the main orchestrating file being `main.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "471b6eb5-5732-4a1c-8bf1-938d9584607e",
  "isSidechain": true,
  "agentId": "a262722788ce57da0",
  "requestId": "req_011CbJbwVhBK57Ezs4r8XKN8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ef574ebe-efba-401a-8dea-cc7cf9e2a310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "5f08a0b3-198f-4f40-8b69-e8e76d016497",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XRw9dHBrcDzcfQCct34QvH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 44863,
      "output_tokens": 2613,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2613,
          "cache_read_input_tokens": 44863,
          "cache_creation_input_tokens": 1128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1128,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
