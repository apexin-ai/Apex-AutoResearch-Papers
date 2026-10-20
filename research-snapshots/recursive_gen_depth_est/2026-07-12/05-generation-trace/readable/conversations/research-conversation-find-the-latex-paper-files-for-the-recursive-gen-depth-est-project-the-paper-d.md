# Research conversation: Find the LaTeX paper files for the recursive_gen_depth_est project. The paper directory should be at /home/ubuntu/.agent

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0070ff34e51f9c82.jsonl`
- **Structured JSON:** [`b0820913666d86e61aca.json`](../../sessions/b0/b0820913666d86e61aca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-22T04:54:15.597Z_

Find the LaTeX paper files for the recursive_gen_depth_est project. The paper directory should be at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper/ or docs/paper/. I need to find:
1. The main .tex file
2. Any appendix files
3. The section structure (especially section 4.2 about feature importance)
4. The .bib file

Search in these paths:
- /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper/
- /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/

Report the file paths and the structure of the appendix sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "fdf68910-80ad-4278-abcf-ac65628b78d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T04:54:17.981Z_

I'll search for the LaTeX paper files in both specified directories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdf68910-80ad-4278-abcf-ac65628b78d3",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1YjeiSTCUHKmSHdqmY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "34c9a8fd-b70e-4eb5-93e3-197ee485e382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HQD6gh5xZthDwYx1CLef4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33436,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33436,
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

_source line 3 · 2026-05-22T04:54:18.266Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CYpXxY9uMYyJ4GADz2dHES`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c9a8fd-b70e-4eb5-93e3-197ee485e382",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1YjeiSTCUHKmSHdqmY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e468051d-86be-440d-abbe-549eb11ac87a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HQD6gh5xZthDwYx1CLef4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33436,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33436,
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

_source line 4 · 2026-05-22T04:54:18.291Z_

<details><summary>↩ Tool result · `toolu_01CYpXxY9uMYyJ4GADz2dHES`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e468051d-86be-440d-abbe-549eb11ac87a",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "a7c2af93-c37b-481b-ad00-d17060bc2793",
  "sourceToolAssistantUUID": "e468051d-86be-440d-abbe-549eb11ac87a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T04:54:18.440Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013qwbSsLYFhvTKdEc4hJ8oq`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7c2af93-c37b-481b-ad00-d17060bc2793",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1YjeiSTCUHKmSHdqmY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e380e5e1-54f9-4a73-8688-d416e1a77224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HQD6gh5xZthDwYx1CLef4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33436,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33436,
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

_source line 6 · 2026-05-22T04:54:18.457Z_

<details><summary>↩ Tool result · `toolu_013qwbSsLYFhvTKdEc4hJ8oq`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e380e5e1-54f9-4a73-8688-d416e1a77224",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "02118ff1-f0f3-42be-83ac-6a73292fb9b2",
  "sourceToolAssistantUUID": "e380e5e1-54f9-4a73-8688-d416e1a77224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T04:54:18.650Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013e9EdqRqnki3iboLnd8Xyb`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02118ff1-f0f3-42be-83ac-6a73292fb9b2",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1YjeiSTCUHKmSHdqmY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9f939e43-1036-4096-a816-37a7896c70ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HQD6gh5xZthDwYx1CLef4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33436,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33436,
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

_source line 8 · 2026-05-22T04:54:18.660Z_

<details><summary>↩ Tool result · `toolu_013e9EdqRqnki3iboLnd8Xyb`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f939e43-1036-4096-a816-37a7896c70ea",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "cf22b589-877d-45c1-acda-5209c0298b68",
  "sourceToolAssistantUUID": "9f939e43-1036-4096-a816-37a7896c70ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T04:54:18.778Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Mi2RavWfPVSFhebVB72EoM`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf22b589-877d-45c1-acda-5209c0298b68",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1YjeiSTCUHKmSHdqmY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d8a4453-777b-43f0-bac7-fb30016f13e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HQD6gh5xZthDwYx1CLef4L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33436,
      "cache_read_input_tokens": 0,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33436
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33436,
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

_source line 10 · 2026-05-22T04:54:18.787Z_

<details><summary>↩ Tool result · `toolu_01Mi2RavWfPVSFhebVB72EoM`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d8a4453-777b-43f0-bac7-fb30016f13e6",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "b7516951-92e9-4af3-9dad-0923df0bb6a5",
  "sourceToolAssistantUUID": "0d8a4453-777b-43f0-bac7-fb30016f13e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-22T04:54:20.634Z_

Good! I found the paper files in the docs/paper directory. Now let me read the main.tex file to understand the structure and then check the appendix file for section details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7516951-92e9-4af3-9dad-0923df0bb6a5",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1YyKExqwQFidfiG1GS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e100b30f-a3b5-4c65-b07e-9f48532486e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WepiJpMyfMGVzzrEEmB5Sh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 33436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1761,
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

_source line 12 · 2026-05-22T04:54:21.098Z_

<details open><summary>🔧 Tool call — Read · `toolu_013tg5BFyqMUeGYCw25m1Way`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e100b30f-a3b5-4c65-b07e-9f48532486e1",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1YyKExqwQFidfiG1GS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ae106b6-0843-429f-93b9-4857299334a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WepiJpMyfMGVzzrEEmB5Sh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 33436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1761,
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

_source line 13 · 2026-05-22T04:54:21.114Z_

<details><summary>↩ Tool result · `toolu_013tg5BFyqMUeGYCw25m1Way`</summary>

```text
1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	\usepackage{enumitem}
18	\usepackage{amsthm}
19	
20	\theoremstyle{definition}
21	\newtheorem{definition}{Definition}
22	
23	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
24	
25	\author{Anonymous}
26	
27	\setlength{\dbltextfloatsep}{4pt plus 2pt minus 2pt}
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{method}
38	
39	\input{theory}
40	
41	\input{atlas}
42	
43	\input{generalization}
44	
45	\input{discussion}
46	
47	\input{conclusion}
48	
49	\bibliography{references}
50	
51	\clearpage
52	\appendix
53	\input{section_appendix}
54	
55	\end{document}
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ae106b6-0843-429f-93b9-4857299334a7",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "fdaed21d-87be-45b4-a56f-4e6f8a1ba8ec",
  "sourceToolAssistantUUID": "1ae106b6-0843-429f-93b9-4857299334a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T04:54:21.182Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pyk9mM675QFeTwqaSqXaB8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdaed21d-87be-45b4-a56f-4e6f8a1ba8ec",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1YyKExqwQFidfiG1GS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b28165ec-384e-42c6-ba2a-f691d87ce495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WepiJpMyfMGVzzrEEmB5Sh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 33436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1761,
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

_source line 15 · 2026-05-22T04:54:21.438Z_

<details><summary>↩ Tool result · `toolu_01Pyk9mM675QFeTwqaSqXaB8`</summary>

```text
1	\section{LoRA Fine-Tuning Protocol}
2	\label{app:lora_protocol}
3	
4	Table~\ref{tab:lora_protocol} lists the full LoRA fine-tuning configuration used for recursive chain construction (\S\ref{sec:method:benchmark}).
5	At each depth $k$, a fresh LoRA adapter is initialized on the base model and trained on $\mathcal{D}_{k-1}$; adapters are not inherited across depths.
6	The HuggingFace Trainer default linear decay schedule is used with no warmup.
7	Target modules are model-specific: \texttt{query\_key\_value} (Pythia), \texttt{att\_proj} (OLMo), and \texttt{c\_attn} (GPT-2~XL).
8	Cross-scale experiments (\S\ref{sec:gen:crossscale}) use QLoRA (4-bit NF4) with $r{=}16$, $\alpha{=}32$.
9	
10	\begin{table}[h]
11	\centering
12	\small
13	\caption{LoRA fine-tuning hyperparameters for the primary 1--1.5B benchmark. Identical across all three model families and all depth levels.}
14	\label{tab:lora_protocol}
15	\begin{tabular}{@{}ll@{}}
16	\toprule
17	Parameter & Value \\
18	\midrule
19	LoRA rank $r$ & 16 \\
20	LoRA alpha $\alpha$ & 32 \\
21	LoRA dropout & 0.05 \\
22	Bias & none \\
23	Epochs per depth & 3 \\
24	Learning rate & $2 \times 10^{-4}$ \\
25	LR schedule & linear decay (no warmup) \\
26	Batch size (effective) & 16 ($8 \times 2$ grad.\ accum.) \\
27	Max sequence length & 512 tokens \\
28	Precision & bfloat16 \\
29	Adapter init & from scratch (base model) \\
30	Seed & 42 (primary), 43 (replication) \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Additional Results}
36	\label{app:additional}
37	
38	\subsection{Top-$k$ Feature Trajectories}
39	\label{app:topk_trajectories}
40	
41	Figure~\ref{fig:feature_trajectory} shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
42	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
43	Concretely, the d0$\to$d1 drop in \texttt{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
44	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
45	
46	\subsection{Permutation Importance}
47	\label{app:permutation}
48	
49	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
50	The top-2 features are stable across measures: \texttt{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \texttt{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \texttt{p75\_ppl} displaces \texttt{var\_surprisal} to rank 3).
51	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
52	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
53	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical; the top features are therefore robust to the choice of importance measure at the aggregate level, though per-cell rankings exhibit model-dependent variation.
54	
55	\subsection{Feature Trajectories}
56	\label{app:feature_trajectories}
57	
58	\begin{figure}[h]
59	\centering
60	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
61	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns: Pythia-1.4B, OLMo-1B, GPT-2~XL) and strategy (line style). Five features are shown per panel: \texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}, and TTR, normalized to depth~0. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
62	\label{fig:feature_trajectory}
63	\end{figure}
64	
65	\subsection{Per-Class Recall}
66	\label{app:per_class}
67	
68	Table~\ref{tab:per_class_recall} reports per-class recall across all 9 atlas cells (4-class in-distribution, 5-fold CV).
69	Depth~0 recall exceeds 97\% uniformly.
70	Among generated depths, d2 is the hardest class in every cell; the deficit is most pronounced under top-$k$ sampling (46--53\%), where vocabulary truncation removes the tail tokens that carry depth-discriminative signal.
71	
72	\begin{table}[h]
73	\centering
74	\small
75	\caption{Per-class recall (\%) for all 9 atlas cells. d2 is the lowest-recall class in every cell. Boldface marks the highest d2 recall.}
76	\label{tab:per_class_recall}
77	\begin{tabular}{@{}lcccc@{}}
78	\toprule
79	Cell & d0 & d1 & d2 & d3 \\
80	\midrule
81	Pythia, nuc.       & 99.3 & 81.9 & 59.2 & 74.4 \\
82	Pythia, $\tau$     & 99.2 & 79.9 & 56.0 & 72.1 \\
83	Pythia, top-$k$    & 98.7 & 71.6 & 44.2 & 60.9 \\
84	OLMo, nuc.         & 97.8 & 82.1 & 60.6 & 75.3 \\
85	OLMo, $\tau$       & 99.3 & 87.1 & 65.6 & 77.1 \\
86	OLMo, top-$k$      & 99.2 & 80.9 & 50.4 & 67.2 \\
87	GPT-2~XL, nuc.     & 98.5 & 87.4 & 72.8 & 78.5 \\
88	GPT-2~XL, $\tau$   & 99.0 & 91.1 & \textbf{73.0} & 80.5 \\
89	GPT-2~XL, top-$k$  & 98.7 & 81.3 & 54.8 & 68.4 \\
90	\bottomrule
91	\end{tabular}
92	\end{table}
93	
94	\subsection{DCOL Iteration Details}
95	\label{app:dcol_iterations}
96	
97	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
98	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
99	
100	\begin{table}[h]
101	\centering
102	\small
103	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.7\%.}
104	\label{tab:dcol_iterations}
105	\resizebox{\columnwidth}{!}{%
106	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
107	\toprule
108	Ver. & Backbone & Config & Outcome \\
109	\midrule
110	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
111	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
112	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
113	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
114	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
115	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
116	\bottomrule
117	\end{tabular}}
118	\end{table}
119	
120	\subsection{Zero-Shot LLM Prompt Template}
121	\label{app:zeroshot_prompt}
122	
123	Both DeepSeek V3.2 and Qwen2.5-7B-Instruct use identical prompting.
124	The system message defines recursive generation depth with per-depth descriptions (depth~0: human-written; depth~1--3: successive LLM generation cycles) and lists expected textual patterns at each depth (vocabulary richness, repetition, coherence).
125	The user message presents the passage (truncated to ${\approx}$384 words) and requests a JSON response containing an integer depth prediction (0--3), a confidence score, and a one-sentence reasoning.
126	No in-context examples are provided.
127	
128	\begin{quote}
129	\small
130	\textbf{System:} ``You are an expert at detecting AI-generated text and estimating its generation depth. `Recursive generation depth' refers to how many times a text has been through an LLM generation cycle: Depth~0: Original human-written text [\ldots] Depth~3: Text generated by an LLM given depth-2 text as input. Key patterns by depth: Depth~0 (human): Rich vocabulary [\ldots] Depth~3 (third-gen): Noticeable repetition, formulaic structure [\ldots]''
131	
132	\textbf{User:} ``Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3). TEXT: \{text\}. Respond with ONLY a JSON object: \{\texttt{"depth"}: $\langle$int 0--3$\rangle$, \texttt{"confidence"}: $\langle$float 0--1$\rangle$, \texttt{"reasoning"}: $\langle$str$\rangle$\}''
133	\end{quote}
134	
135	\subsection{Temperature Robustness}
136	\label{app:multi_tau}
137	
138	The cross-strategy results in \S\ref{sec:gen:crossstrategy} use a single temperature ($\tau{=}0.9$).
139	To test whether depth signal generalizes across temperatures, we repeat the classification pipeline at $\tau \in \{0.5, 0.7, 0.9, 1.1\}$ on Pythia-1.4B.
140	
141	\paragraph{Within-$\tau$ robustness.}
142	For $\tau \in [0.5, 0.9]$, d1-vs-d2 AUC exceeds 0.80 (peak 0.851 at $\tau{=}0.7$, comparable to nucleus $p{=}0.95$'s 0.861) and 4-class accuracy ranges from 75.4\% to 77.3\% (Table~\ref{tab:multi_tau_within}); the depth signal is therefore not an artifact of a single temperature.
143	The same top-5 features (\texttt{var\_surprisal}, \texttt{p90\_ppl}, \texttt{mean\_ppl}, \texttt{mean\_surprisal}, \texttt{p75\_ppl}) dominate across all $\tau$ values with only minor rank-order variation.
144	
145	\paragraph{Collapse at $\tau{=}1.1$: memorization as prerequisite.}
146	At $\tau{=}1.1$, 4-class accuracy drops to 57.2\% and d1v2 AUC falls to 0.528.
147	Training loss reveals the mechanism: at low temperature ($\tau{=}0.5$), fine-tuning loss decreases steeply across recursive depths ($2.27 \to 0.42 \to 0.16$), a sign of rapid memorization of the model's own output.
148	At $\tau{=}1.1$, loss remains nearly flat ($2.27 \to 1.91 \to 1.85$); high-entropy output resists memorization, so depth-dependent distributional shifts do not accumulate.
149	This establishes \emph{memorization as a prerequisite} for detectable depth signal: recursive depth is discriminable only when successive fine-tuning iterations progressively reshape the output distribution.
150	
151	\paragraph{Cross-$\tau$ non-transferability.}
152	Leave-one-$\tau$-out transfer yields mean accuracy of 46.7\% with mean d1v2 AUC of 0.319 (Table~\ref{tab:multi_tau_cross}), worse than cross-strategy transfer (59.1\%; \S\ref{sec:gen:crossstrategy}).
153	Holdout $\tau{=}0.5$ produces inverted d1v2 AUC (0.176); different temperatures therefore produce surprisal distributions with incompatible shapes.
154	This extends the strategy-specificity finding: even within a single decoding family, the feature space is temperature-specific; strategy-conditioned classifiers are therefore necessary.
155	
156	\paragraph{Ecological validity.}
157	On WikiText-103 (546 editorial passages), all three model-specific RF classifiers achieve $\geq$98.5\% d0 accuracy despite $+$621\% domain shift in mean perplexity, partly an easy case, as WikiText's higher perplexity places it farther from d1--d3 in feature space.
158	On noisier web-crawl data (5{,}000 C4 passages), FPR ranges from 4.7\% (OLMo) to 22.4\% (GPT-2~XL), concentrated in template/SEO content with high n-gram repetition (Table~\ref{tab:calibration}); deployment on heterogeneous web data requires model-specific calibration.
159	
160	\begin{table}[h]
161	\centering
162	\small
163	\caption{Within-$\tau$ 4-class classification (Pythia-1.4B, 5-fold CV). d$i$v$j$: pairwise AUC for depth $i$ vs.\ depth $j$.}
164	\label{tab:multi_tau_within}
165	\resizebox{\columnwidth}{!}{%
166	\begin{tabular}{@{}lcccc@{}}
167	\toprule
168	$\tau$ & 4-class acc (\%) & d1v2 AUC & d0v1 AUC & d2v3 AUC \\
169	\midrule
170	0.5 & 77.3 & 0.842 & 0.996 & 0.764 \\
171	0.7 & 75.4 & 0.851 & 0.997 & 0.720 \\
172	0.9 & 75.9 & 0.808 & 0.991 & 0.781 \\
173	1.1 & 57.2 & 0.528 & 0.988 & 0.599 \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\caption{Cross-$\tau$ leave-one-out transfer (Pythia-1.4B). Train on three temperatures, test on the held-out one.}
182	\label{tab:multi_tau_cross}
183	\begin{tabular}{@{}lcc@{}}
184	\toprule
185	Holdout & Acc (\%) & d1v2 AUC \\
186	\midrule
187	$\tau{=}0.5$ & 52.2 & 0.176 \\
188	$\tau{=}0.7$ & 41.0 & 0.299 \\
189	$\tau{=}0.9$ & 46.4 & 0.277 \\
190	$\tau{=}1.1$ & 47.1 & 0.525 \\
191	\midrule
192	Mean & 46.7 & 0.319 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	\subsection{Feature Overlap Analysis}
198	\label{app:feature_overlap}
199	
200	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features via linear probing of [CLS] representations from DeBERTa-v3-base and RoBERTa-base.
201	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics; \texttt{var\_surprisal} and \texttt{p90\_ppl} yield negative $R^2$ under linear probing; these features are not linearly accessible in the pretrained representation space.
202	This confirms that the 20pp accuracy gap between feature-based and end-to-end methods (\S\ref{app:e2e}) stems from complementary, not redundant, representations: PLMs capture lexical patterns while the targeted statistical features capture distributional tail properties that constitute the dominant depth markers.
203	
204	\subsection{End-to-End Learning}
205	\label{app:e2e}
206	
207	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
208	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode (high d0 F1, $>$0.94, but collapsed d1/d2 performance, F1 $\leq$ 0.42), while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
209	
210	\begin{table}[h]
211	\centering
212	\small
213	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
214	\label{tab:e2e_detail}
215	\resizebox{\columnwidth}{!}{%
216	\begin{tabular}{@{}lccccc@{}}
217	\toprule
218	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
219	\midrule
220	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
221	RoBERTa-base & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
222	\midrule
223	RF (19 feat.) & 78.7 & --- & --- & .596$^\dagger$ & --- \\
224	\bottomrule
225	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
226	\end{tabular}}
227	\end{table}
228	
229	\paragraph{Feature space divergence.}
230	SHAP TreeExplainer analysis confirms that perplexity and surprisal features account for 88.8\% of RF's total contribution.
231	Three independent importance measures (SHAP, Gini, and permutation) show strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; pairwise Spearman $\rho$: SHAP--Gini $0.93$, SHAP--permutation $0.84$; \S\ref{app:permutation}), with \texttt{p90\_ppl} appearing in the SHAP top-2 in 9/9 cells and \texttt{var\_surprisal} in 8/9.
232	Linear probing of PLM [CLS] representations yields negative $R^2$ for both \texttt{var\_surprisal} and \texttt{p90\_ppl} (\S\ref{app:feature_overlap}); pretrained representations lack the linear structure needed to recover perplexity tail statistics, a systematic representational gap rather than a backbone-specific artifact.
233	
234	DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods; depth estimation therefore benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
235	This comparison is bounded by backbone scale ($\leq$125M parameters); whether larger PLMs (e.g., 7B+) can close the gap via richer internal representations remains an open question.
236	
237	\subsection{Domain Bias Analysis}
238	\label{app:domain_bias}
239	
240	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
241	
242	\paragraph{Methodological note.}
243	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
244	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
245	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
246	
247	\paragraph{Sub-A: Standard CV.}
248	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level); depth signal is therefore the dominant classification factor.
249	
250	\paragraph{Sub-B: LOGO evaluation.}
251	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
252	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
253	Per-cell fold standard deviations range from 0.4pp to 1.4pp; cross-group generalization is therefore as reliable as within-group classification.
254	
255	\paragraph{Sub-C: Negative control.}
256	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
257	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%, indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
258	The depth-to-seed-group accuracy ratio is 7.1$\times$; the feature representation therefore encodes depth but not seed-article identity.
259	
260	Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
261	
262	\subsection{Wild-Data Calibration}
263	\label{app:calibration}
264	
265	Table~\ref{tab:calibration} reports d0 accuracy and false positive rate (FPR) for all three model-specific nucleus RF classifiers on two out-of-distribution human-text corpora: WikiText-103 (546 editorial passages) and C4 (5{,}000 web-crawl passages, crawled 2019--2020; pre-LLM deployment).
266	
267	\begin{table}[h]
268	\centering
269	\small
270	\caption{Wild-data d0 accuracy and FPR for nucleus RF classifiers. All passages are human-written (true d0). FPR = fraction misclassified as d1+. 95\% Wilson CIs computed for C4 ($n{=}5{,}000$).}
271	\label{tab:calibration}
272	\resizebox{\columnwidth}{!}{%
273	\begin{tabular}{@{}llrccc@{}}
274	\toprule
275	Model & Source & $n$ & d0 (\%) & FPR (\%) & 95\% Wilson CI \\
276	\midrule
277	Pythia-1.4B & WikiText & 546 & 100.0 & 0.0 & --- \\
278	 & C4 & 5{,}000 & 79.8 & 20.2 & [19.1, 21.3] \\
279	\addlinespace
280	GPT-2~XL & WikiText & 546 & 99.3 & 0.7 & --- \\
281	 & C4 & 5{,}000 & 77.6 & 22.4 & [21.3, 23.6] \\
282	\addlinespace
283	OLMo-1B & WikiText & 546 & 98.5 & 1.5 & --- \\
284	 & C4 & 5{,}000 & 95.3 & 4.7 & [4.2, 5.3] \\
285	\bottomrule
286	\end{tabular}}
287	\end{table}
288	
289	On WikiText-103, all three classifiers achieve $\geq$98.5\% d0 accuracy; editorial text is therefore reliably distinguished from recursive generations across model families.
290	On C4, FPR varies sharply: OLMo (4.7\%) vs.\ Pythia (20.2\%) and GPT-2~XL (22.4\%).
291	C4 misclassifications concentrate in template and SEO content with elevated repetition features (\texttt{rep\_3gram} $+$37\%, \texttt{rep\_4gram} $+$75\% vs.\ correctly classified d0 passages), rather than in random noise.
292	The model gap likely reflects training data composition: OLMo (trained on Dolma, which includes diverse web data) produces d0 features more tolerant of web-crawl variation, while Pythia and GPT-2~XL (trained primarily on Wikipedia/WebText) map template-heavy content into the d1+ region.
293	Among C4 false positives for GPT-2~XL, predictions distribute as d1 (9.0\%), d2 (3.7\%), d3 (9.6\%); for OLMo, d1 (2.9\%), d2 (0.5\%), d3 (1.3\%). The non-uniform depth distribution suggests the classifier maps specific repetition patterns to particular depth signatures rather than producing random misclassifications.
294	
295	\paragraph{Threshold calibration.}
296	A pooled RF classifier (trained on all three families' nucleus data) achieves ECE\,=\,0.052 on in-distribution data; Platt scaling and isotonic regression yield no improvement; probability estimates are already well calibrated.
297	The high FPR on web-crawl data is therefore a decision-threshold problem, not a probability calibration defect.
298	Applying a confidence threshold $P(\mathrm{d0}) \geq 0.15$ reduces C4 FPR from 33.4\% to 2.8\% and FineWeb FPR from 16.9\% to 0.7\%, at a cost of only $-$0.3\,pp balanced accuracy (78.0\%$\to$77.7\%).
299	The $P(\mathrm{d0})$ distribution is bimodal: 67\% of samples exceed 0.95 (high-confidence d0), while 33\% fall in the 0.15--0.30 uncertainty zone; the threshold separates these modes cleanly.
300	Wild-data FPR is thus an operational threshold choice rather than a fundamental limitation, though the optimal threshold is domain-dependent.
301	
302	\subsection{Downstream Curation PoC (Inconclusive)}
303	\label{app:curation_poc}
304	
305	To assess whether depth estimation translates to actionable data curation, we conduct a proof-of-concept downstream evaluation.
306	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) for 3 epochs on 8 data conditions derived from the Pythia nucleus depth-estimation corpus, repeating each condition over 5 random seeds.
307	Conditions vary the selection mechanism (RF-predicted depth, oracle depth, random subsampling) and stringency (strict $\approx$25\%, moderate $\approx$50\%, soft threshold).
308	Table~\ref{tab:curation_poc} reports per-condition perplexity; Table~\ref{tab:curation_comparisons} reports pairwise contrasts.
309	
310	\begin{table}[h]
311	\centering
312	\small
313	\caption{Curation PoC: per-condition perplexity (Pythia-410M LoRA, 5 seeds). $\Delta$ is signed so that positive values indicate lower (better) perplexity than unfiltered. $^*$\,: $p<0.05$ (paired $t$-test vs.\ unfiltered).}
314	\label{tab:curation_poc}
315	\resizebox{\columnwidth}{!}{%
316	\begin{tabular}{@{}lcccccc@{}}
317	\toprule
318	Condition & Mean PPL & Std & $n$ & $\Delta$ vs Unfilt. & $p$ & $d_z$ \\
319	\midrule
320	unfiltered        & 15.776 & 0.066 & 10{,}000 & ---      & ---   & ---      \\
321	rf\_soft          & 15.733 & 0.038 &  4{,}422 & +0.043   & 0.407 &  0.41    \\
322	rf\_moderate      & 15.756 & 0.056 &  4{,}940 & +0.021   & 0.492 &  0.34    \\
323	rf\_strict        & 15.810 & 0.061 &  2{,}496 & $-$0.034 & 0.607 & $-$0.25  \\
324	oracle\_moderate  & 15.809 & 0.103 &  5{,}000 & $-$0.033 & 0.485 & $-$0.34  \\
325	oracle\_strict    & 15.879 & 0.128 &  2{,}500 & $-$0.103 & 0.216 & $-$0.66  \\
326	random\_soft      & 16.062 & 0.079 &  4{,}422 & $-$0.286 & ${<}$0.001$^*$ & $-$2.77  \\
327	random\_moderate  & 15.998 & 0.090 &  4{,}940 & $-$0.222 & 0.028$^*$ & $-$1.50  \\
328	random\_strict    & 16.239 & 0.165 &  2{,}496 & $-$0.463 & 0.013$^*$ & $-$1.89  \\
329	\bottomrule
330	\end{tabular}}
331	\end{table}
332	
333	\begin{table}[h]
334	\centering
335	\small
336	\caption{Pairwise comparisons (paired $t$-test, 5 seeds). $^*$\,: $p<0.05$; $^{**}$\,: $p<0.01$.}
337	\label{tab:curation_comparisons}
338	\resizebox{\columnwidth}{!}{%
339	\begin{tabular}{@{}lccc@{}}
340	\toprule
341	Comparison & $\Delta$ PPL & $t$ & $p$ \\
342	\midrule
343	rf\_strict vs random\_strict     & 0.429 & $-$7.05 & 0.002$^{**}$ \\
344	rf\_moderate vs random\_moderate & 0.242 & $-$3.77 & 0.020$^*$    \\
345	rf\_soft vs random\_soft         & 0.328 & $-$17.98 & ${<}$0.001$^{**}$ \\
346	rf\_soft vs unfiltered           & 0.043 &    0.93 & 0.407        \\
347	\bottomrule
348	\end{tabular}}
349	\end{table}
350	
351	For the binary task of identifying low-depth passages (d0 vs.\ d1--d3, evaluated on the same Pythia nucleus corpus with 5-fold CV), RF-based depth filtering achieves F1\,=\,0.997, substantially outperforming a simple perplexity-threshold baseline (F1\,=\,0.845); the multi-feature representation provides discriminative value beyond raw perplexity.
352	However, the primary comparison (RF-filtered vs.\ unfiltered, $p > 0.4$) is non-significant; the significant RF-vs-random contrasts ($p < 0.02$) involve multiple pairwise comparisons that were not corrected for multiplicity.
353	
354	\subsection{Reference Model Ablation}
355	\label{app:ref_ablation}
356	
357	Table~\ref{tab:ref_ablation} ablates the reference model used for feature extraction on Pythia-1.4B nucleus text (d0--d3, 5-fold CV).
358	Self-reference (Pythia-1.4B) yields 78.6\%; switching to a cross-architecture reference degrades accuracy by 4--11\,pp, confirming that reference-generator alignment amplifies depth signal.
359	
360	\begin{table}[h]
361	\centering
362	\caption{Reference model ablation. Classification accuracy (5-fold CV) on Pythia-1.4B generated text (nucleus, d0--d3) using different reference models for feature extraction.}
363	\label{tab:ref_ablation}
364	\resizebox{\columnwidth}{!}{%
365	\begin{tabular}{@{}lcc@{}}
366	\toprule
367	Reference Model & Architecture & Accuracy (\%) \\
368	\midrule
369	Pythia-1.4B (self) & GPT-NeoX & 78.6 $\pm$ 0.6 \\
370	OLMo-1B (cross) & OLMo & 74.5 $\pm$ 0.7 \\
371	GPT-2~XL (cross) & GPT-2 & 67.3 $\pm$ 0.7 \\
372	\bottomrule
373	\end{tabular}}
374	\end{table}
375	
376	\subsection{Cross-Scale Full Results}
377	\label{app:cross_scale_full}
378	
379	This section provides the full cross-scale analysis summarized in \S\ref{sec:gen:crossscale}.
380	We extend the benchmark to two 7--8B models (Qwen2.5-7B-Instruct \cite{qwen2.5}, Llama-3.1-8B-Instruct \cite{llama3}) and one 14B model (Qwen2.5-14B).
381	The 7--8B models use 4-bit NF4 QLoRA fine-tuning with nucleus sampling ($p{=}0.95$, 500 samples per depth, depths $d \in \{0, 1, \ldots, 5\}$).
382	The 14B model uses clean FP16 LoRA fine-tuning across all three decoding strategies (nucleus, temperature $\tau{=}0.9$, top-$k$ $k{=}50$; 5{,}000 samples per depth, depths $d \in \{0, 1, 2, 3\}$).
383	Feature extraction for 1--8B models uses Pythia-1.4B as reference; Qwen2.5-14B is evaluated under both self-reference and cross-reference (Pythia-1.4B) to disentangle reference-model artifacts from scale effects (see paragraph~5 below).
384	
385	\paragraph{Scale comparison.}
386	Table~\ref{tab:cross_scale} contrasts the 7--14B models with the three 1--1.5B models on matched evaluation (depths 0--3).
387	The 14B model is tested across all three decoding strategies; the 7--8B models use nucleus sampling only.
388	
389	\begin{table}[h]
390	\centering
391	\small
392	\caption{Cross-scale comparison: 4-class RF accuracy (\%, depths 0--3), $\mathrm{EDD}_{0.70}$ (computed from full depth range: 0--5 for 7--8B, 0--3 for 14B), and d0-vs-d1 AUC. CI: 95\% bootstrap. Chance = 25\%. $^\dagger$Self-reference model (see text).}
393	\label{tab:cross_scale}
394	\resizebox{\columnwidth}{!}{%
395	\begin{tabular}{@{}llccc@{}}
396	\toprule
397	Model & Strategy & 4-class acc & $\mathrm{EDD}_{0.70}$ & d0v1 \\
398	\midrule
399	GPT-2~XL (1.5B) & nucleus & 84.3 & 4 & 0.999 \\
400	OLMo-1B & nucleus & 78.9 & 4 & 0.997 \\
401	Pythia-1.4B & nucleus & 78.7 & 4 & 0.998 \\
402	\midrule
403	Llama-3.1-8B & nucleus & 70.2\,[68.3, 72.4] & 4 & 0.949 \\
404	Qwen2.5-7B & nucleus & 60.1\,[58.0, 62.1] & $5$ & 0.969 \\
405	\midrule
406	Qwen2.5-14B$^\dagger$ & nucleus & 54.1\,[53.4, 54.7] & 0 & 0.643 \\
407	Qwen2.5-14B$^\dagger$ & temp09 & 50.5\,[49.8, 51.2] & 0 & 0.632 \\
408	Qwen2.5-14B$^\dagger$ & top-$k$50 & 47.9\,[47.3, 48.6] & 0 & 0.561 \\
409	\cmidrule{2-5}
410	\multicolumn{2}{@{}l}{\textit{14B mean}} & \textit{50.8} & --- & --- \\
411	\bottomrule
412	\end{tabular}}
413	\end{table}
414	
415	\paragraph{(1) Depth signal persists at 7--8B scale.}
416	Both 7--8B models substantially exceed the 25\% chance baseline: Llama-3.1-8B achieves 70.2\% (95\% CI $[68.3, 72.4]$) and Qwen2.5-7B achieves 60.1\% ($[58.0, 62.1]$); recursive depth therefore remains estimable from perplexity-based features even when the generator is 5--7$\times$ larger than the reference model.
417	Depth-0 separability is preserved in both models: d0v1 AUC is 0.949 (Llama-3.1) and 0.969 (Qwen2.5).
418	
419	\paragraph{(2) EDD at 7--8B scale.}
420	At threshold $T{=}0.70$, Qwen2.5-7B maintains all consecutive-pair AUCs above 0.70 through depth~5 (Table~\ref{tab:cross_scale_auc}), yielding $\mathrm{EDD}_{0.70} = 5$ (the maximum observable from the tested depth range), exceeding the $\mathrm{EDD}_{0.70}{=}4$ observed at 1--1.5B.
421	Llama-3.1-8B matches the smaller models at $\mathrm{EDD}_{0.70}{=}4$: its monotonic decay causes d4v5 (0.618) to drop below $T$, despite stronger signal at shallower depths.
422	Both larger generators produce weaker per-step signal than the 1--1.5B models (mean consecutive AUC: 0.786 for Llama-3.1, 0.782 for Qwen2.5, vs.\ 0.852 at 1--1.5B).
423	
424	\begin{table}[h]
425	\centering
426	\small
427	\caption{Consecutive binary AUC. Llama-3.1-8B exhibits monotonic decay; Qwen2.5-7B shows a U-shaped pattern; Qwen2.5-14B$^\dagger$ (depths 0--3 only) has all pairs below $T{=}0.70$ with strategy-specific patterns. $^\dagger$Self-reference model.}
428	\label{tab:cross_scale_auc}
429	\resizebox{\columnwidth}{!}{%
430	\begin{tabular}{@{}llccccc@{}}
431	\toprule
432	Model & Strategy & d0v1 & d1v2 & d2v3 & d3v4 & d4v5 \\
433	\midrule
434	Llama-3.1-8B & nucleus & 0.949 & 0.877 & 0.771 & 0.716 & 0.618 \\
435	Qwen2.5-7B & nucleus & 0.969 & 0.729 & 0.709 & 0.732 & 0.772 \\
436	\midrule
437	Qwen2.5-14B$^\dagger$ & nucleus & 0.643 & 0.713 & \textbf{0.728} & \multicolumn{2}{c}{--} \\
438	Qwen2.5-14B$^\dagger$ & temp09 & 0.632 & \textbf{0.726} & 0.618 & \multicolumn{2}{c}{--} \\
439	Qwen2.5-14B$^\dagger$ & top-$k$50 & 0.561 & 0.687 & 0.679 & \multicolumn{2}{c}{--} \\
440	\bottomrule
441	\end{tabular}}
442	\end{table}
443	
444	\paragraph{(3) Divergent AUC trajectories and instruction-tuning effect.}
445	Among instruction-tuned models, Llama-3.1-8B exhibits monotonic AUC decay consistent with the 1--1.5B pattern, while Qwen2.5-7B shows a U-shaped recovery beyond d2v3 (Table~\ref{tab:cross_scale_auc}).
446	A base-model control (Llama-3.1-8B without instruction tuning) clarifies the causal direction: the base model achieves 59.9\% four-class accuracy (95\% CI [57.8, 62.15], $\mathrm{EDD}_{0.70}{=}2$) with non-monotonic AUC decay (Table~\ref{tab:llama3_base_auc}), while the instruction-tuned variant reaches 70.2\% with strictly monotonic decay.
447	The base-model control experiment suggests instruction-tuning regularizes rather than confounds the depth signal.
448	
449	\begin{table}[h]
450	\centering
451	\small
452	\caption{Pairwise AUC: Llama-3.1-8B Base vs.\ Instruct.}
453	\label{tab:llama3_base_auc}
454	\begin{tabular}{lccccc}
455	\toprule
456	Variant & $d_{0\text{v}1}$ & $d_{1\text{v}2}$ & $d_{2\text{v}3}$ & $d_{3\text{v}4}$ & $d_{4\text{v}5}$ \\
457	\midrule
458	Base & 0.918 & 0.794 & 0.682 & 0.730 & 0.595 \\
459	Instruct & 0.965 & 0.874 & 0.771 & 0.716 & 0.618 \\
460	\bottomrule
461	\end{tabular}
462	\end{table}
463	
464	The base model exhibits non-monotonic decay with a U-shaped recovery at $d_{3\text{v}4}$, while the instruction-tuned variant shows strictly monotonic decay. Both variants exceed chance (AUC $> 0.5$) at all boundaries; depth signal exists regardless of instruction-tuning, though instruction-tuning strengthens and regularizes it.
465	
466	\paragraph{(4) Signal attenuation at 14B.}
467	Qwen2.5-14B (clean FP16, self-reference) is tested across all three decoding strategies (Table~\ref{tab:cross_scale}).
468	Mean four-class accuracy is 50.8\% ($2.0{\times}$ chance), with nucleus 54.1\%, temperature 50.5\%, and top-$k$ 47.9\%.
469	$\mathrm{EDD}_{0.70}{=}0$ across all three strategies because the d0/d1 boundary falls below the 0.70 AUC threshold in every case (0.56--0.64), breaking the contiguous prefix at the first boundary.
470	The d0/d1 boundary, near-perfect at 1--1.5B (AUC ${>}0.99$), attenuates to 0.56--0.64 at 14B.
471	
472	Each strategy produces a structurally distinct adjacent-pair AUC pattern (Table~\ref{tab:cross_scale_auc}):
473	nucleus is monotonically increasing (d0v1=0.643 $<$ d1v2=0.713 $<$ d2v3=0.728);
474	temperature exhibits d2v3 collapse (0.618, the weakest boundary) because temperature scaling uniformly amplifies logit differences, accelerating convergence to the attractor distribution at deeper depths;
475	top-$k$ exhibits d0v1 collapse (0.561, the weakest boundary) because vocabulary truncation constrains d0 and d1 distributions to the same top-$k$ tokens, compressing their statistical distance.
476	This three-way divergence confirms at 14B that different decoding strategies induce structurally distinct degradation trajectories (\S\ref{sec:gen:crossstrategy}).
477	
478	Feature importance shifts under top-$k$: lexical diversity metrics (TTR, hapax ratio) enter the top-5, displacing perplexity tail statistics that dominate under nucleus and temperature.
479	This result carries an important caveat: Qwen2.5-14B uses self-reference, whereas all other experiments use Pythia-1.4B.
480	Self-reference conflates the generator's distributional shift with the reference model's sensitivity; the observed attenuation may partially reflect the reference model change rather than a pure scale effect.
481	
482	\paragraph{(5) Cross-reference control at 14B.}
483	To disentangle the scale effect from the reference-model artifact, we re-extract all 19 features using Pythia-1.4B (the same reference model as the 1--1.5B benchmark) on the Qwen2.5-14B generated text.
484	Table~\ref{tab:cross_ref_14b} compares self-reference and cross-reference results per strategy.
485	
486	\begin{table}[h]
487	\centering
488	\small
489	\caption{14B cross-reference control: Pythia-1.4B reference vs.\ self-reference on Qwen2.5-14B text. $\Delta$: cross $-$ self. $\mathrm{EDD}_{0.70}$ computed from consecutive pairwise AUC.}
490	\label{tab:cross_ref_14b}
491	\resizebox{\columnwidth}{!}{%
492	\begin{tabular}{@{}lccccc@{}}
493	\toprule
494	Strategy & Self-ref (\%) & Cross-ref (\%) & $\Delta$ & $\mathrm{EDD}_{0.70}$ & d0v1 AUC \\
495	\midrule
496	nucleus & 54.1 & 45.0 & $-$9.1 & 2 & 0.702 \\
497	temp ($\tau{=}0.9$) & 50.5 & 46.3 & $-$4.2 & 2 & 0.739 \\
498	top-$k$ ($k{=}50$) & 47.9 & 40.9 & $-$7.1 & 0 & 0.699 \\
499	\cmidrule{2-6}
500	\textit{mean} & \textit{50.8} & \textit{44.1} & $-$\textit{6.8} & --- & --- \\
501	\bottomrule
502	\end{tabular}}
503	\end{table}
504	
505	Cross-reference accuracy drops by 6.8\,pp on average (range 4.2--9.1\,pp), but $\mathrm{EDD}_{0.70}$ \emph{rises} from 0 to 2 for nucleus and temperature: the consecutive d0v1 (0.70--0.74) and d1v2 (0.72--0.73) AUCs now exceed the 0.70 threshold, while d2v3 remains below (0.54--0.61).
506	Under self-reference, no pair exceeds $T{=}0.70$ because the 14B model's own perplexity features are too coarse to resolve adjacent depths; the Pythia-1.4B reference model provides sharper distributional contrast at the cost of overall accuracy.
507	The ${\sim}$7\,pp accuracy gap between self- and cross-reference is therefore a reference-model artifact, not a depth-signal artifact: depth signal persists at 14B albeit attenuated relative to 1--1.5B.
508	
509	\paragraph{Caveats.}
510	For Qwen2.5-7B, the CI lower bound (58.0\%) does not exclude sub-60\% accuracy; Llama-3.1-8B's lower bound (68.3\%) is more comfortably above chance but still below the 75--83\% range at 1--1.5B.
511	The divergent AUC trajectories across two models caution against strong generalizations from only two 7--8B data points: both the monotonic (Llama-3.1) and non-monotonic (Qwen2.5) patterns are single observations, and further architectures are needed to establish which is the dominant regime at this scale.
512	
513	\paragraph{Confounds.}
514	\label{app:cross_scale_confounds}
515	Four confounds limit the 7--8B results: (1)~4-bit NF4 QLoRA quantization (absent at 1--1.5B) may distort the perplexity distribution independently of depth; (2)~smaller sample size (500 vs.\ 5{,}000 per depth) widens confidence intervals; (3)~evaluation is limited to nucleus sampling at 7--8B (the 14B model addresses this with all three strategies); (4)~vocabulary mismatch between larger generators and the 1.4B reference model.
516	For the 14B model specifically: the cross-reference control (Table~\ref{tab:cross_ref_14b}) quantifies the reference-model artifact at ${\sim}$7\,pp, but the remaining accuracy gap (44\% vs.\ 78--85\% at 1--1.5B) still conflates scale with the other confounds listed above.
517	The base-model control partially addresses a former confound (instruction-tuning): since the base variant shows weaker signal with non-monotonic decay while the instruction-tuned variant shows stronger monotonic signal, instruction-tuning regularizes rather than confounds depth estimation.
518	The remaining confounds are not mutually independent (quantization and vocabulary mismatch both affect the perplexity distribution); it is therefore infeasible to attribute the observed accuracy gap (60--70\% vs.\ 78--85\% at 1--1.5B) to any single factor.
519	
520	\subsection{Cross-Boundary Generalization}
521	\label{app:cross_boundary}
522	
523	The preceding experiments assume a single model family generates all recursive depths.
524	In practice, recursive contamination may traverse model boundaries: text generated by model~A is used to train model~B, whose output trains model~C.
525	We probe whether the depth signal persists under two relaxations of the single-model assumption.
526	
527	\paragraph{Cross-model recursive chains.}
528	We construct a heterogeneous chain: human text (d0) $\to$ Pythia-1.4B generates d1 $\to$ OLMo-1B finetuned on Pythia-d1 generates d2 $\to$ GPT-2~XL finetuned on OLMo-d2 generates d3.
529	Each recursive step uses a \emph{different} model family, eliminating the possibility that depth signal arises from a single model's idiosyncratic behavior.
530	A 4-class Random Forest achieves 84.75\% accuracy (95\% CI $[81.0, 88.25]$), with per-depth F1 scores of 0.98 (d0), 0.88 (d1), 0.76 (d2), and 0.76 (d3).
531	Pairwise AUC remains high: d0-vs-d1 = 0.999 and d2-vs-d3 = 0.841.
532	These results suggest that distributional artifacts of recursive generation persist across model boundaries. This constitutes preliminary evidence for a process-level depth signal rather than individual generator artifacts.
533	
534	\paragraph{Confound discussion.}
535	The heterogeneous chain confounds architecture identity with depth (d1=Pythia, d2=OLMo, d3=GPT-2~XL).
536	However, if the classifier exploited architecture fingerprints rather than depth signal, near-perfect accuracy would be expected since architecture perfectly determines depth label.
537	The observed 84.75\% with monotonically decreasing per-depth F1 (d0=0.98, d1=0.88, d2=0.76, d3=0.76) is more consistent with a depth-signal interpretation, as architecture fingerprinting would not produce this graded pattern.
538	We address this confound directly with a reverse-chain control below.
539	
540	\paragraph{Reverse-chain control.}
541	To empirically test the architecture confound hypothesis, we constructed a reverse chain (GPT-2~XL $\to$ OLMo $\to$ Pythia) reversing the model-depth assignment.
542	The reverse chain achieves 85.75\% (95\% CI [82.0, 89.25]), statistically indistinguishable from the forward chain (84.75\%, [81.0, 88.25]).
543	If the classifier exploited architecture fingerprints rather than depth signal, reversing the chain should invert depth predictions; the equivalent accuracy under both orderings provides empirical evidence against the architecture confound.
544	
545	\paragraph{Cross-domain transfer.}
546	All prior experiments use WikiText-103 as the seed corpus.
547	To test domain dependence, we repeat the pipeline with arXiv abstracts as the seed text (Pythia-1.4B, nucleus $p{=}0.95$, 500 samples per depth, d0--d3).
548	Five-fold cross-validation yields 74.1\% $\pm$ 2.0\% accuracy, compared to ${\sim}$78\% on the WikiText seed.
549	Per-depth F1 shows the familiar pattern: d0 = 1.00, d1 = 0.78, d2 = 0.52, d3 = 0.66, with d2 remaining the most challenging class.
550	The 4pp accuracy gap relative to WikiText likely reflects the narrower stylistic range of scientific abstracts, which may reduce the distributional contrast between adjacent depths.
551	These results provide preliminary evidence that the perplexity-based features capture properties of the recursive generation process rather than domain-specific artifacts of the seed corpus.
552	
553	\subsection{Cross-Seed Replication}
554	\label{app:seed_replication}
555	
556	Table~\ref{tab:seed_replication} reports within-seed accuracy for all three model families (nucleus, depths 0--3) under two independent LoRA training seeds.
557	
558	\begin{table}[h]
559	\centering
560	\small
561	\caption{Cross-seed replication (nucleus $p{=}0.95$, d0--d3). seed=42 is the primary benchmark (matching Table~\ref{tab:main_matrix}); seed=43 is an independent replication.}
562	\label{tab:seed_replication}
563	\begin{tabular}{@{}llccc@{}}
564	\toprule
565	Model & Seed & Acc (\%) & 95\% CI & $\Delta$ (pp) \\
566	\midrule
567	Pythia-1.4B & 42 & 78.70 & [78.10, 79.24] & --- \\
568	Pythia-1.4B & 43 & 78.84 & [78.13, 79.52] & $+$0.14 \\
569	\midrule
570	OLMo-1B & 42 & 78.94 & [78.38, 79.48] & --- \\
571	OLMo-1B & 43 & 82.11 & [81.77, 82.54] & $+$3.17 \\
572	\midrule
573	GPT-2~XL & 42 & 84.28 & [83.78, 84.80] & --- \\
574	GPT-2~XL & 43 & 86.32 & [86.17, 86.49] & $+$2.04 \\
575	\bottomrule
576	\end{tabular}
577	\end{table}
578	
579	Seed=43 yields higher accuracy in all three models ($+$0.14 to $+$3.17\,pp, same direction).
580	For Pythia ($+$0.14\,pp), CIs overlap, consistent with noise; for OLMo ($+$3.17\,pp) and GPT-2~XL ($+$2.04\,pp), CIs do not overlap, so LoRA initialization has a non-trivial effect on absolute accuracy (${\sim}$1--3\,pp).
581	Top-3 features are identical across all seeds and models (\texttt{p90\_ppl}, \texttt{var\_surprisal}, \texttt{p75\_ppl}); depth ordering is preserved in every configuration.
582	
583	\paragraph{Outlier handling.}
584	Feature extraction occasionally produces extreme perplexity values (outlier passages); we apply per-feature clipping at $\pm 10^{10}$ before classification, affecting ${<}0.1$\% of samples.
585	The d3 perplexity distribution varies substantially across seeds: under seed=42, 0.56\% of d3 passages exceed $10^6$ in raw perplexity, while under seed=43 this fraction rises to 12.8\%.
586	Despite this variation, the classifier remains effective after clipping, confirming that the depth signal resides in the p90-and-below distributional shape rather than extreme outliers.
587	
588	\subsection{Depth-4 Extension}
589	\label{app:depth4_ext}
590	
591	We extend all three model families (GPT-2~XL, Pythia-1.4B, OLMo-1B; nucleus $p{=}0.95$) to depth~4 and train 5-class RF classifiers (d0--d4, 5{,}000 samples per depth).
592	Five-class accuracy reaches 80.5\% (OLMo), 74.0\% (GPT-2~XL), and 71.3\% (Pythia), all substantially above the 20\% chance baseline.
593	For Pythia and GPT-2~XL, d3 recall drops from ${\sim}$80\% (4-class) to ${\sim}$49\% (5-class) due to d3/d4 confusion; d4 recall is higher (Pythia 68.1\%, GPT-2~XL 63.9\%).
594	$\mathrm{EDD}_{0.70} \geq 4$ was established by dedicated binary classifiers in the atlas (\S\ref{sec:atlas:edd}; d3v4 AUC: Pythia 0.784, OLMo 0.765, GPT-2~XL 0.750); the 5-class results provide complementary evidence that depth~4 remains discriminable in the multi-class setting.
595	
596	\paragraph{Feature monotonicity at d4.}
597	For Pythia and GPT-2~XL, the dominant depth markers (\texttt{p90\_ppl}, \texttt{var\_surprisal}) maintain monotonic decrease through d4 (Pythia \texttt{p90\_ppl}: $483.7 \to 12.5$ from d0 to d4; \texttt{var\_surprisal}: $6.50 \to 1.29$), consistent with continued tail erosion (\S\ref{sec:method:theory}).
598	Mean perplexity breaks monotonicity at d4 for GPT-2~XL (d3: $1{,}076\mathrm{K}$ $\to$ d4: $928\mathrm{K}$) while tail perplexity continues to decline.
599	OLMo exhibits a \texttt{var\_surprisal} rebound at d4 ($2.49 \to 2.83$, non-monotonic), creating a feature signature absent in GPT-2~XL and Pythia.
600	The 5-class RF exploits non-adjacent depth contrasts (particularly d0-vs-d4 and d2-vs-d4) to achieve 80.5\% accuracy, the highest among all three families, while the dedicated binary d3-vs-d4 classifier (AUC 0.765) is restricted to adjacent-depth features.
601	This discrepancy illustrates that multi-class classifiers can exploit global distributional structure unavailable to pairwise comparisons.
602	The divergence between aggregate and tail statistics suggests that aggregate distributional statistics saturate at deep recursion while tail statistics continue to shift.
603	This saturation provides a physical mechanism for the EDD ceiling: once per-step feature change falls below classifier resolution, adjacent depths become indistinguishable regardless of continued distributional drift.
604	
605	\subsection{Generation Length Ablation}
606	\label{app:length_ablation}
607	
608	Table~\ref{tab:length_ablation} reports classification accuracy as a function of passage length (Pythia-1.4B nucleus, depths 0--3).
609	
610	\begin{table}[h]
611	\centering
612	\small
613	\caption{Generation length ablation (Pythia-1.4B nucleus, 5-fold CV). Accuracy increases monotonically with passage length; the 9.47\,pp spread confirms that longer passages provide stronger statistical signal.}
614	\label{tab:length_ablation}
615	\begin{tabular}{@{}lc@{}}
616	\toprule
617	Passage length (tokens) & Acc (\%) \\
618	\midrule
619	128 & 68.35 \\
620	256 & 73.80 \\
621	512 & 77.82 \\
622	\bottomrule
623	\end{tabular}
624	\end{table}
625	
626	Depth signal is detectable from 128 tokens (2.7$\times$ chance) and saturates near 500 tokens.
627	The monotonic increase reflects the statistical nature of the features: longer passages yield more stable estimates of perplexity percentiles and surprisal variance, reducing within-class overlap at adjacent depth boundaries.
628	
629	\subsection{Mixed-Depth Corpus}
630	\label{app:mixed_depth}
631	
632	Per-passage classification is largely independent of corpus composition: evaluating on a corpus containing mixed proportions of d0--d3 passages (rather than balanced classes) yields macro-recall $\Delta{=}{-}1.62$\,pp relative to the balanced benchmark (within the 2\,pp tolerance).
633	Individual class deltas range from $-$0.45\,pp to $-$2.43\,pp (d1 shows the largest shift); the RF classifier operates on per-sample features without sensitivity to the class distribution of the evaluation corpus, as Random Forest produces identical per-sample predictions regardless of batch context.
634	
635	\subsection{Learned Estimator Comparison}
636	\label{app:learned_estimator}
637	
638	Table~\ref{tab:learned_estimator} evaluates three learned classifiers (XGBoost, ordinal MLP with CORAL loss \cite{coral2020}, prototypical networks) under the same leave-one-model-out protocol as Table~\ref{tab:cross_model}.
639	The ordinal MLP follows the nested binary reduction framework \cite{mccullagh1980_ordinal,frank2001} with the loss function of \citet{rennie2005}.
640	All three methods operate on the same 19-dimensional feature vector; the comparison isolates the effect of the classification head.
641	
642	\begin{table}[h]
643	\centering
644	\small
645	\caption{Learned estimator cross-model transfer (leave-one-model-out, nucleus, 4-class). RF baseline from Table~\ref{tab:cross_model}. Chance = 25\%.}
646	\label{tab:learned_estimator}
647	\begin{tabular}{@{}lcccc@{}}
648	\toprule
649	Method & Pythia & OLMo & GPT-2 XL & Mean \\
650	\midrule
651	RF (baseline) & --- & --- & --- & 66.4 \\
652	XGBoost & 63.7 & 69.8 & 68.1 & 67.2 \\
653	Ordinal MLP & 62.5 & 69.7 & 67.9 & 66.7 \\
654	Prototypical & 61.6 & 70.0 & 68.4 & 66.6 \\
655	\bottomrule
656	\end{tabular}
657	\end{table}
658	
659	All three learned methods match the RF baseline within 0.8\,pp on average; the Pythia holdout is consistently the hardest (61.6--63.7\%), while OLMo and GPT-2~XL holdouts yield 67.9--70.0\%.
660	The narrow spread ($\leq$0.8\,pp across four methods) reinforces the conclusion that the 19-feature representation, not the classifier, determines the accuracy ceiling in the cross-model transfer setting.
661	
662	\subsection{Instruction-Tuned Model at 1.5B Scale}
663	\label{app:instruct_1p5b}
664	
665	To test whether instruction tuning eliminates depth signal at matched scale (1.5B, avoiding the quantization confound of \S\ref{sec:gen:crossscale}), we run the full recursive pipeline on Qwen2.5-1.5B-Instruct with self-reference feature extraction (i.e., the same model serves as both generator and reference).
666	
667	The RF classifier achieves 47.4\% four-class accuracy (95\% CI $[46.7, 48.1]$, $1.9\times$ chance); instruction tuning therefore reduces but does not eliminate depth signal.
668	The pairwise AUC profile differs from base models: d0v1 = 0.653, d1v2 = 0.620, d2v3 = 0.664, with a gap-dependent pattern (non-adjacent pairs yield higher AUC, e.g., d0v3 = 0.902) but no pair reaching the 0.75 threshold.
669	
670	The top-5 features shift substantially: \texttt{surp\_range}, \texttt{surp\_pos\_corr}, \texttt{prob\_std}, \texttt{surp\_half\_diff}, and \texttt{surp\_std} replace the perplexity tail statistics (\texttt{p90\_ppl}, \texttt{var\_surprisal}) that dominate in base models.
671	This feature shift suggests instruction tuning compresses the perplexity distribution (reducing tail discriminability) while preserving positional and range-based surprisal patterns.
672	
673	Two caveats apply: (1) self-reference evaluation may inflate or deflate accuracy relative to cross-reference evaluation (cf.\ \S\ref{app:ref_ablation}); (2) a single instruction-tuned model does not establish the generality of the feature shift across architectures or instruction-tuning recipes.
674	
675	\subsection{Downstream Fine-Tuning Probe (Inconclusive)}
676	\label{app:downstream}
677	
678	We fine-tune Pythia-410M with LoRA ($r{=}16$, $\alpha{=}32$) on depth-stratified subsets (500 samples each) and evaluate held-out perplexity (200 samples, 50 per depth).
679	
680	\begin{table}[h]
681	\centering
682	\small
683	\caption{Downstream fine-tuning probe: held-out perplexity by training subset (Pythia-410M LoRA, seed=42). $\Delta$: signed difference vs.\ baseline (negative = better).}
684	\label{tab:downstream}
685	\begin{tabular}{@{}lcc@{}}
686	\toprule
687	Training subset & PPL & $\Delta$ vs.\ baseline \\
688	\midrule
689	Baseline (no fine-tuning) & 5.67 & --- \\
690	d0 only & 5.65 & $-$0.02 \\
691	d1 only & 5.55 & $-$0.12 \\
692	d2 only & 5.56 & $-$0.11 \\
693	Mixed (d0--d3) & 5.55 & $-$0.12 \\
694	\bottomrule
695	\end{tabular}
696	\end{table}
697	
698	The hypothesis that d0-only data yields the lowest perplexity is not supported: d1-only and mixed subsets tie for best (PPL~5.55), both marginally below d0-only (5.65).
699	The PPL spread is small (0.12, 2.1\% relative) and the sample size (500 per condition, single seed) is insufficient for statistical significance.
700	Training loss decreases monotonically with depth (d0: 2.558, d1: 1.920, d2: 1.286), consistent with recursive generation reducing information content and making text easier to model.
701	This pilot establishes that depth-filtered data is not harmful for downstream fine-tuning; whether depth-aware curation provides a meaningful advantage requires larger-scale evaluation.
702	
703	\subsection{Feature Group Ablation}
704	\label{app:feature_ablation}
705	
706	Table~\ref{tab:feature_ablation} reports cross-model transfer accuracy (leave-one-model-out, nucleus) when restricting the classifier to subsets of the 19-feature vector, grouped by signal type.
707	
708	\begin{table}[h]
709	\centering
710	\small
711	\caption{Feature group ablation (cross-model LOO, nucleus, 4-class). Chance = 25\%.}
712	\label{tab:feature_ablation}
713	\begin{tabular}{@{}lccc@{}}
714	\toprule
715	Feature group & \#Feat. & Acc (\%) & $\Delta$ vs.\ Full \\
716	\midrule
717	Full (all 19) & 19 & 66.6 & --- \\
718	Perplexity only & 9 & 66.0 & $-$0.5 \\
719	Entropy/Surprisal only & 5 & 63.2 & $-$3.4 \\
720	Repetition/Diversity only & 5 & 53.0 & $-$13.6 \\
721	\midrule
722	\texttt{p90\_ppl} only & 1 & 58.3 & $-$8.3 \\
723	\bottomrule
724	\end{tabular}
725	\end{table}
726	
727	The 9 perplexity features nearly match the full set ($\Delta{=}{-}0.5$\,pp), while repetition/diversity features alone fall 13.6\,pp below; perplexity degradation statistics therefore carry the dominant depth signal.
728	The top-2 individual features by Gini importance are \texttt{p90\_ppl} (22.4\%) and \texttt{var\_surprisal} (18.8\%), accounting for 41\% of total importance.
729	
730	\subsection{RF Seed Robustness}
731	\label{app:rf_seed}
732	
733	Table~\ref{tab:rf_seed} reports cross-model transfer accuracy across three RF random seeds.
734	
735	\begin{table}[h]
736	\centering
737	\small
738	\caption{RF seed robustness (cross-model LOO, nucleus, 4-class).}
739	\label{tab:rf_seed}
740	\begin{tabular}{@{}lc@{}}
741	\toprule
742	Seed & Acc (\%) \\
743	\midrule
744	42 & 66.4 \\
745	123 & 66.5 \\
746	456 & 66.5 \\
747	\midrule
748	Mean $\pm$ std & 66.48 $\pm$ 0.06 \\
749	\bottomrule
750	\end{tabular}
751	\end{table}
752	
753	The 0.06\,pp standard deviation across seeds confirms that RF classification is deterministic to within rounding noise at this sample size, and reported accuracy differences across experimental conditions (e.g., feature ablation, cross-model transfer) are not attributable to classifier randomness.
754	
755	\subsection{Binary Detector Baselines for Ordinal Classification}
756	\label{app:detector_baselines}
757	
758	We evaluate whether existing binary AI-text detectors and membership inference methods, when repurposed for ordinal classification, can match our 19-feature RF pipeline.
759	
760	\paragraph{Binary detectors (Pythia nucleus).}
761	Binoculars~\cite{binoculars2024} and Fast-DetectGPT~\cite{fast_detectgpt2024} scores are computed on the Pythia-1.4B nucleus ($p{=}0.95$) subset and fed to: (a)~a log-likelihood rank classifier (Log-Rank, 64.0\%), (b)~a combined RF trained on both detector scores (Combined, 74.2\%), and (c)~the standard 19-feature RF (78.7\%).
762	The 4.5\,pp gap (74.2\% vs.\ 78.7\%) confirms that perplexity distributional features capture ordinal depth structure beyond what generic detection scores provide.
763	Note that Fast-DetectGPT exhibits numerical overflow on Pythia nucleus d1 (mean perturbation score $>$28{,}000); results for this cell should be interpreted cautiously.
764	Across all 9 atlas cells, Binoculars and Fast-DetectGPT ordinal accuracy averages ${\sim}$35\% and ${\sim}$32\%, respectively.
765	
766	\paragraph{Membership inference baselines (all 9 cells).}
767	DetectGPT~\cite{mitchell2023_detectgpt} (gpt2-large scoring model, t5-large perturbation model, 5 perturbations) achieves 30.7\% mean 4-class accuracy (d1--d3 BalAcc: 24.3\%).
768	Min-K\% Prob~\cite{shi2024_minkprob} ($K{=}20$) with CORAL ordinal calibration reaches 33.2\% (d1--d3 BalAcc: 40.4\%); the best single cell is gpt2xl\_temp09 at 50.6\%.
769	Min-K\%'s advantage over DetectGPT (+2.5\,pp) is consistent with token-level log-probabilities containing more depth-relevant information than perturbation-based curvature, but both remain within 10\,pp of chance.
770	CORAL calibration improves ordinal structure (d1--d3 BalAcc 40.4\% vs.\ 33.3\% random) without closing the gap to RF (71.6\%), confirming that the bottleneck is the input signal rather than the calibration strategy.
771	Perturbation-based and membership-inference methods (28--33\%) confirm that token-level detection scores lack ordinal depth resolution.
772	Cross-perplexity (Binoculars) is a notable exception: when evaluated across all 9 atlas cells with threshold calibration, Binoculars achieves 69.8\%; with multi-feature RF calibration (11 cross-perplexity statistics), it reaches 78.1\%, matching our 19-feature pipeline within 0.3\,pp (\S\ref{sec:gen:baselines}).
773	
774	\paragraph{Augmented feature set.}
775	To test whether detection scores carry complementary ordinal signal, we add Min-K\% probability ($K{=}20$) and DetectGPT perturbation discrepancy as additional RF features.
776	The 20-feature model (19 + Min-K\%) achieves 78.90\% mean 4-class accuracy (+0.48\,pp) and 72.20\% d1--d3 balanced accuracy (+0.60\,pp).
777	Min-K\% ranks \#3 by feature importance (0.095), behind \texttt{p90\_ppl} (0.161) and \texttt{var\_surprisal} (0.126); DetectGPT ranks \#17 (0.026).
778	The marginal improvement is consistent across 8 of 9 atlas cells, indicating that Min-K\%'s token-level log-probability signal provides weak but real complementary information to the passage-level distributional features.
779	The top-2 features (\texttt{p90\_ppl} + \texttt{var\_surprisal}) retain combined importance of 28.7\%, confirming that perplexity tail statistics remain the dominant depth markers even after augmentation.
780	
781	\subsection{Binoculars Feature Ablation and Signal Decomposition}
782	\label{app:feature_ablation_bino}
783	
784	To quantify the overlap and complementarity between our 19-feature pipeline and Binoculars' cross-perplexity features, we evaluate four feature configurations across all 9 atlas cells (Table~\ref{tab:bino_ablation}).
785	
786	\begin{table}[h]
787	\centering
788	\small
789	\caption{Feature ablation: overlap and merged configurations (9-cell mean, 5-fold CV, RF 200 trees). The 6 overlap features are the perplexity statistics shared between both pipelines (mean, variance, median, p10, p90, skewness).}
790	\label{tab:bino_ablation}
791	\begin{tabular}{@{}lccc@{}}
792	\toprule
793	Configuration & \#Feat. & Acc (\%) & $\Delta$ vs.\ 19-feat \\
794	\midrule
795	6 overlap only & 6 & 75.9 & $-$2.5 \\
796	Our 19 features & 19 & 78.4 & --- \\
797	Binoculars 11 features & 11 & 78.1 & $-$0.3 \\
798	Merged (19 + 11) & 30 & \textbf{82.6} & +4.2 \\
799	\bottomrule
800	\end{tabular}
801	\end{table}
802	
803	The 6 shared perplexity features alone achieve 75.9\% (97\% of the full pipeline's accuracy), confirming that mean-level perplexity distributional displacement is the core depth signal.
804	Our 13 additional features (kurtosis, surprisal variance, lexical/n-gram statistics) contribute +2.5\,pp of shape-level information; Binoculars' 5 unique features (observer-performer agreement score, cross-entropy statistics) contribute +4.2\,pp of cross-model divergence when merged.
805	
806	Table~\ref{tab:bino_ablation_percell} reports per-cell results for three configurations with per-cell breakdown (Bino-11 per-cell values are omitted because features were computed on the pooled 9-cell corpus).
807	
808	\begin{table}[h]
809	\centering
810	\small
811	\caption{Per-cell feature ablation (4-class accuracy \%, 5-fold CV, RF 200 trees). $\Delta$: merged minus 19-feature accuracy. Bino-11 per-cell values omitted because Binoculars features were computed on the pooled 9-cell corpus; the per-cell mean (78.1\%) is reported in Table~\ref{tab:bino_ablation}.}
812	\label{tab:bino_ablation_percell}
813	\resizebox{\columnwidth}{!}{%
814	\begin{tabular}{@{}lcccc c@{}}
815	\toprule
816	Cell & 6-overlap & 19-feat & Bino-11 & Merged & $\Delta$ \\
817	\midrule
818	Pythia nucleus & 76.7 & 78.7 & --- & 83.5 & +4.8 \\
819	Pythia temp09 & 73.9 & 76.8 & --- & 81.5 & +4.7 \\
820	Pythia top-$k$50 & 65.3 & 68.9 & --- & 71.2 & +2.3 \\
821	OLMo nucleus & 76.4 & 78.9 & --- & 84.2 & +5.3 \\
822	OLMo temp09 & 81.0 & 82.3 & --- & 88.3 & +6.0 \\
823	OLMo top-$k$50 & 72.5 & 74.4 & --- & 78.4 & +4.0 \\
824	GPT-2~XL nucleus & 81.7 & 84.3 & --- & 88.8 & +4.5 \\
825	GPT-2~XL temp09 & 84.0 & 85.9 & --- & 88.5 & +2.6 \\
826	GPT-2~XL top-$k$50 & 72.1 & 75.8 & --- & 79.1 & +3.3 \\
827	\midrule
828	\textbf{9-cell mean} & \textbf{75.9} & \textbf{78.4} & \textbf{78.1} & \textbf{82.6} & \textbf{+4.2} \\
829	\bottomrule
830	\end{tabular}}
831	\end{table}
832	
833	\paragraph{Strategy-dependent complementarity.}
834	The merged improvement varies by decoding strategy: nucleus and temperature cells gain +4.7\,pp on average, while top-k cells gain +3.2\,pp.
835	Top-k sampling truncates the token distribution to the $k$ highest-probability tokens, producing text with reduced distributional diversity; this limits the information available to cross-model divergence features, which rely on disagreement between observer and performer predictions.
836	Merged improvement also varies by generator family: OLMo cells (observer-dissimilar) gain +5.1\,pp on average, compared to +3.9\,pp for Pythia (observer-similar) and +3.5\,pp for GPT-2~XL, suggesting cross-model divergence features contribute more when observer and generator architectures differ.
837	
838	\paragraph{Cross-scale Binoculars ablation (14B).}
839	We evaluate Binoculars cross-scale on two representative strategies (temperature, top-$k$); the nucleus cell was used for the main 14B pipeline and its GPU hours were allocated to generation rather than Binoculars evaluation.
840	At 14B, when only 1--1.5B reference models are available for cross-perplexity computation (Pythia-1.4B observer analyzing Qwen2.5-14B text), Binoculars features degrade substantially (Table~\ref{tab:bino_14b_ablation}).
841	Self-reference statistical features (19-feat) outperform Binoculars (11-feat) by 8--11\,pp, reversing the near-parity observed at 1--1.5B.
842	Merging all 30 features yields a consistent +3.6--3.7\,pp gain over the self-reference baseline across both tested strategies, confirming that cross-perplexity features retain complementary signal even under the 10$\times$ scale gap, though the gain is attenuated relative to +4.2\,pp at 1--1.5B.
843	
844	\begin{table}[h]
845	\centering
846	\small
847	\caption{Feature ablation at 14B (Qwen2.5-14B, self-reference$^\dagger$). Binoculars: observer=Pythia-1.4B, performer=Pythia-410M. $\Delta$: merged minus main-pipeline stat-only accuracy (Method~A alignment). Chance = 25\%.}
848	\label{tab:bino_14b_ablation}
849	\begin{tabular}{@{}lcccc@{}}
850	\toprule
851	Strategy & Bino-11 & Stat-19$^\dagger$ & Merged-30 & $\Delta$ \\
852	\midrule
853	temp09 & 42.6 & 50.5 & 54.2 & +3.7 \\
854	top-$k$50 & 37.7 & 47.9 & 51.5 & +3.6 \\
855	\bottomrule
856	\end{tabular}
857	\end{table}
858	
859	The Binoculars degradation reflects a practical deployment constraint: the 10$\times$ scale gap between observer (1.4B) and generator (14B) causes cross-perplexity features to lose sensitivity, not a fundamental limitation of the cross-model divergence channel.
860	Self-reference features are more robust across scales because they avoid the observer--generator mismatch.
861	The accuracy difference between self-reference (50.8\%) and Binoculars stat-only (40.1\% mean) may therefore partially reflect observer capacity limitations rather than feature design differences.
862	
863	\subsection{Prompted Generation Results}
864	\label{app:prompted_gen}
865	
866	Table~\ref{tab:prompted_gen} reports depth estimation performance under topic-seeded (prompted) generation using GPT-2~XL with nucleus sampling ($p{=}0.95$, depths 0--3).
867	Generation is conditioned on Wikipedia topic prompts rather than a bare BOS token, a more ecologically valid test of depth signal persistence.
868	
869	\begin{table}[h]
870	\centering
871	\small
872	\caption{Prompted generation (GPT-2~XL, nucleus $p{=}0.95$, topic-seeded). 5-fold CV accuracy and pairwise AUC. Chance = 25\%.}
873	\label{tab:prompted_gen}
874	\begin{tabular}{@{}lc@{}}
875	\toprule
876	Metric & Value \\
877	\midrule
878	4-class accuracy (\%) & 69.52 $[68.9, 70.2]$ \\
879	BOS-seeded baseline (\%) & 83.3 \\
880	$\Delta$ (prompted $-$ BOS) & $-$13.78\,pp \\
881	\midrule
882	AUC d0v1 & 0.916 \\
883	AUC d1v2 & 0.782 \\
884	AUC d2v3 & 0.744 \\
885	\midrule
886	Top-1 feature & \texttt{p90\_ppl} \\
887	Top-2 feature & \texttt{var\_surprisal} \\
888	Top-3 feature & \texttt{p75\_ppl} \\
889	\bottomrule
890	\end{tabular}
891	\end{table}
892	
893	The 13.8\,pp drop relative to BOS-seeded generation is expected: topic prompts constrain the output distribution, reducing the variance that distinguishes depths.
894	Nevertheless, accuracy remains $2.8\times$ chance and pairwise AUC decays monotonically (0.916, 0.782, 0.744); the depth signal is therefore not an artifact of unconstrained generation.
895	Top features are identical to BOS-seeded (\texttt{p90\_ppl} first); the same perplexity tail erosion mechanism operates under prompted conditions.
896	
897	\subsection{Extended Discussion}
898	\label{app:extended_discussion}
899	
900	\paragraph{Cross-strategy conditional decomposition.}
901	The two-stage pipeline (strategy identification followed by depth classification) recovers 11.5\,pp over the na\"ive pooled classifier.
902	Under correct strategy routing, four-class accuracy reaches 72.6\% vs.\ 68.0\% under misrouting ($N{=}103{,}498$ / $76{,}502$), a gap of 4.6\,pp; d0 accuracy remains near-ceiling (${\sim}99.6$\%) regardless of routing, confirming that the d0 signal is strategy-invariant.
903	Even the worst routing yields a floor of 67.6\% ($2.7\times$ chance), and the 31.5\,pp d1--d3 gap between correct and wrong routing confirms feature-space misalignment rather than uniform noise.
904	End-to-end PLMs lag RF by ${\sim}20$\,pp, suggesting that current pretrained representations do not capture the distributional tail statistics that drive depth discrimination.
905	
906	\paragraph{Depth-graduated curation (inconclusive).}
907	Initial curation experiments remain inconclusive: RF-vs-unfiltered is not significant ($p>0.4$; Appendix~\ref{app:curation_poc}).
908	
909	\paragraph{Toward a provenance toolkit.}
910	Depth estimation complements existing provenance methods along orthogonal axes.
911	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
912	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
913	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
914	A layered provenance system combining these three signals (watermark presence, source model, and recursive generation depth) could support more nuanced data auditing than any single method.
915	
916	\subsection{Computational Resources and Reproducibility}
917	\label{app:compute}
918	
919	\paragraph{Hardware.}
920	All experiments were conducted on 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) GPUs locally and 2$\times$ NVIDIA RTX PRO 6000 (48\,GB) on cloud instances.
921	Total computation is approximately 200 GPU$\cdot$hours, covering the $3 \times 3$ generation matrix (LoRA fine-tuning + sampling at each depth), feature extraction, depth extension to d5, 7--14B QLoRA experiments, and all ablations.
922	
923	\paragraph{Software.}
924	Key library versions: PyTorch 2.10.0+cu128, Transformers 5.8.1, PEFT 0.7.1, scikit-learn 1.8.0.
925	Additional dependencies: Accelerate 1.13.0, Datasets 4.8.4, XGBoost 3.2.0, NumPy 2.2.6 (Python 3.12.3, CUDA 12.8).
926	
927	\paragraph{Hyperparameters.}
928	LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout $0.05$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs) follow \citet{hu2022lora}.
929	The Random Forest classifier uses 200 trees, Gini criterion, and no max depth, without hyperparameter search; all reported results use 5-fold stratified cross-validation.
930	
931	\paragraph{Inference cost.}
932	Feature extraction requires a single forward pass of the reference model.
933	On a single GPU this takes approximately 2 minutes for 5{,}000 passages; a CPU-only alternative requires approximately 50 minutes on server-grade hardware.
934	RF classification adds negligible overhead ($<$1\,s).
935	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b28165ec-384e-42c6-ba2a-f691d87ce495",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "27819b8e-21ba-407c-8a83-f52d437ce7f6",
  "sourceToolAssistantUUID": "b28165ec-384e-42c6-ba2a-f691d87ce495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-22T04:54:23.501Z_

Perfect! Now let me search for any mention of section 4.2 about feature importance to understand the main paper structure better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27819b8e-21ba-407c-8a83-f52d437ce7f6",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1ZAWSMBkQDwf8xBDBG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "524da5d7-32d3-44ea-939b-95770dee4af9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161R3kwQ16b5Ezj2uBENiEm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25881,
      "cache_read_input_tokens": 35197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25881,
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

_source line 17 · 2026-05-22T04:54:24.793Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01K2ewp6C3KhNyvLmsp5o7Sy`</summary>

```json
{
  "pattern": "\\\\section\\{|\\\\subsection\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "524da5d7-32d3-44ea-939b-95770dee4af9",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1ZAWSMBkQDwf8xBDBG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41e80995-8517-4388-95f1-86aeed74cbd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161R3kwQ16b5Ezj2uBENiEm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25881,
      "cache_read_input_tokens": 35197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25881,
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

_source line 18 · 2026-05-22T04:54:24.811Z_

<details><summary>↩ Tool result · `toolu_01K2ewp6C3KhNyvLmsp5o7Sy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:1:\section{Related Work}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:1:\section{The Depth Degradation Atlas}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:8:\subsection{In-Distribution Performance}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:40:\subsection{Feature Consistency Across the Grid}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:88:\subsection{EDD Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:115:\subsection{Strategy-Dependent Trajectories}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/acl.sty:234:\def\section{\@startsection {section}{1}{\z@}{-2.0ex plus
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/acl.sty:236:\def\subsection{\@startsection{subsection}{2}{\z@}{-1.8ex plus
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex:1:\section{Discussion and Conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:1:\section{Method}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:4:\subsection{Problem Definition}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:15:\subsection{Multi-Generational Benchmark Construction}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:44:\subsection{Statistical Feature Design}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:78:\subsection{Effective Discriminable Depth}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/theory.tex:1:\subsection{Theoretical Motivation}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:1:\section{Generalization and Robustness}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:6:\subsection{Classifier Comparison and Surface-Text Ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:55:\subsection{Cross-Model Transfer}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:79:\subsection{Cross-Strategy Transfer}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:103:\subsection{Preliminary Cross-Scale Observations (14B)}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:1:\section{LoRA Fine-Tuning Protocol}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:35:\section{Additional Results}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:38:\subsection{Top-$k$ Feature Trajectories}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:46:\subsection{Permutation Importance}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:55:\subsection{Feature Trajectories}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:65:\subsection{Per-Class Recall}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:94:\subsection{DCOL Iteration Details}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:120:\subsection{Zero-Shot LLM Prompt Template}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:135:\subsection{Temperature Robustness}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:197:\subsection{Feature Overlap Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:204:\subsection{End-to-End Learning}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:237:\subsection{Domain Bias Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:262:\subsection{Wild-Data Calibration}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:302:\subsection{Downstream Curation PoC (Inconclusive)}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:354:\subsection{Reference Model Ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:376:\subsection{Cross-Scale Full Results}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:520:\subsection{Cross-Boundary Generalization}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:553:\subsection{Cross-Seed Replication}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:588:\subsection{Depth-4 Extension}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:605:\subsection{Generation Length Ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:629:\subsection{Mixed-Depth Corpus}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:635:\subsection{Learned Estimator Comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:662:\subsection{Instruction-Tuned Model at 1.5B Scale}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:675:\subsection{Downstream Fine-Tuning Probe (Inconclusive)}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:703:\subsection{Feature Group Ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:730:\subsection{RF Seed Robustness}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:755:\subsection{Binary Detector Baselines for Ordinal Classification}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:781:\subsection{Binoculars Feature Ablation and Signal Decomposition}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:863:\subsection{Prompted Generation Results}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:897:\subsection{Extended Discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:916:\subsection{Computational Resources and Reproducibility}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:1:\section{Introduction}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:12:\subsection{Cross-Scale Observations}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:36:\subsection{Preliminary Cross-Scale Observations}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/drafts/14b_scenarios.tex:59:\subsection{Preliminary Cross-Scale Observations}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41e80995-8517-4388-95f1-86aeed74cbd4",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "348ff89a-d796-4295-9861-5bff6764288b",
  "sourceToolAssistantUUID": "41e80995-8517-4388-95f1-86aeed74cbd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T04:54:24.927Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nzh7X1VgPjp1fiMBjAg6TR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "348ff89a-d796-4295-9861-5bff6764288b",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1ZAWSMBkQDwf8xBDBG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0f6e5e72-0152-443d-851d-978fa5417548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0161R3kwQ16b5Ezj2uBENiEm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25881,
      "cache_read_input_tokens": 35197,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25881
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 229,
          "cache_read_input_tokens": 35197,
          "cache_creation_input_tokens": 25881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25881,
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

_source line 20 · 2026-05-22T04:54:24.933Z_

<details><summary>↩ Tool result · `toolu_01Nzh7X1VgPjp1fiMBjAg6TR`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells at the 1--1.5B parameter scale, evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 68.9\% (Pythia, top-$k$) to 85.9\% (GPT-2~XL, temperature) four-class (d1--d3 balanced: 58.9--81.5\%), all exceeding the 25\%/33\% chance baselines.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (75.8--85.9\%), followed by OLMo (74.4--82.3\%) and Pythia (68.9--78.7\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 9.3~pp, comparable to the 7.2~pp mean within-strategy model gap; decoding strategy contributes at least as much as model family to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) with bootstrap 95\% CI (${\pm}$half-width; $B{=}1{,}000$). RF with 200 trees, evaluated via 5-fold stratified CV (seed=42). Parenthesized: d1--d3 balanced accuracy from the same 4-class RF (chance = 25\% / 33\%). Depth-0 recall exceeds 97\% in all cells. Within-distribution ordinal quality: mean absolute error (MAE)\,=\,0.23, QWK\,=\,0.89 (QWK$_{\text{d1--d3}}$\,=\,0.74); 98.2\% of errors fall on adjacent depths ($|\Delta| \leq 1$). $^\dagger$Self-reference scoring (Pythia-1.4B is both generator and reference model); 4--11\,pp advantage over cross-model references (Appendix~\ref{app:ref_ablation}). Cross-cell comparisons involving Pythia should be interpreted with this caveat.}
22	\label{tab:main_matrix}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
27	\midrule
28	Pythia-1.4B$^\dagger$  & 78.7{\scriptsize$\pm$0.6}\,(71.8) & 76.8{\scriptsize$\pm$0.6}\,(69.3) & 68.9{\scriptsize$\pm$0.6}\,(58.9) \\
29	OLMo-1B     & 78.9{\scriptsize$\pm$0.6}\,(72.7) & 82.3{\scriptsize$\pm$0.5}\,(76.6) & 74.4{\scriptsize$\pm$0.6}\,(66.2) \\
30	GPT-2~XL    & \textbf{84.3}{\scriptsize$\pm$0.5}\,(79.6) & \textbf{85.9}{\scriptsize$\pm$0.4}\,(81.5) & \textbf{75.8}{\scriptsize$\pm$0.6}\,(68.1) \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	
35	\paragraph{Per-class recall.}
36	Depth-0 recall exceeds 97\% in all 9 cells.
37	Among generated depths, d2 consistently yields the lowest recall (44--73\%), reflecting its position at the center of the depth gradient where features overlap with both d1 and d3, consistent with d2-vs-d3 as the EDD bottleneck (\S\ref{sec:atlas:edd}; full per-class recall in Appendix~\ref{app:per_class}).
38	
39	%% ----------------------------------------------------------------
40	\subsection{Feature Consistency Across the Grid}
41	\label{sec:atlas:features}
42	
43	Multicollinearity is substantial (VIF${>}$10 for 14--16 of 19 features); importance rankings below indicate feature \emph{family} contributions rather than individual effects; permutation importance (Appendix~\ref{app:permutation}) partially mitigates collinearity bias \cite{strobl2008_conditional,hooker2021_permutation}.
44	Despite the 17.1~pp accuracy spread across cells, the perplexity tail statistics family (\texttt{p90\_ppl}, \texttt{p75\_ppl}, \texttt{kurtosis\_ppl}) and surprisal variance (\texttt{var\_surprisal}) dominate depth discrimination in every setting.
45	Within this family, \texttt{p90\_ppl} and \texttt{var\_surprisal} are consistently prominent, though individual rankings should be interpreted cautiously given VIF${>}$10; group-level ablation (\S\ref{sec:atlas:features}, below) provides the collinearity-robust confirmation.\footnote{The group-level dominance of perplexity tail statistics is robust across importance measures (Gini, SHAP, permutation; Kendall's $W{=}0.90$, $p{<}0.005$).}
46	Table~\ref{tab:feature_importance} shows the full per-cell ranking.
47	
48	Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ ($[0.619, 0.954]$): models agree on which features carry depth information despite differing in absolute accuracy.
49	Top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$), as vocabulary truncation imposes a more uniform feature landscape at the cost of weaker signal (\S\ref{sec:atlas:strategy}).
50	
51	Feature ablation confirms this concentration: the top-5 features achieve 97.6\% of full accuracy (76.5\% vs.\ 78.4\%); group-level ablation shows perplexity features alone reach 76.6\%, surprisal 73.2\%, lexical diversity ${\leq}$47\%, and repetition ${\leq}$40\%.\footnote{Best single feature (\texttt{p90\_ppl}) achieves 58.3\%, providing a more competitive single-feature baseline than mean perplexity (25.1\%).}
52	
53	The feature hierarchy shifts with depth.
54	At shallow boundaries (d1 vs.\ d2), \texttt{var\_surprisal} dominates importance; at deeper boundaries (d3 vs.\ d4, d4 vs.\ d5), tail perplexity statistics (\texttt{p90\_ppl}, \texttt{kurtosis\_ppl}) take over.
55	This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
56	
57	\begin{table}[t]
58	\centering
59	\small
60	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 8/9 under SHAP (7/9 under Gini). Individual rankings are approximate due to multicollinearity (VIF${>}$10 for 14--16/19 features).}
61	\label{tab:feature_importance}
62	\resizebox{\columnwidth}{!}{%
63	\begin{tabular}{@{}l l@{}}
64	\toprule
65	Cell & Top-5 features (Gini importance, ranked) \\
66	\midrule
67	Pythia, nuc.       & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.15)}, m\_ppl\,(.11), var\_ppl\,(.08), p75\,(.07) \\
68	Pythia, $\tau$     & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.14)}, m\_ppl\,(.11), p75\,(.07), m\_surp\,(.07) \\
69	Pythia, top-$k$    & \textbf{var\_surp\,(.16)}, \textbf{p90\_ppl\,(.12)}, m\_ppl\,(.11), var\_ppl\,(.07), m\_surp\,(.06) \\
70	GPT-2\,XL, nuc.    & \textbf{var\_surp\,(.21)}, \textbf{p90\_ppl\,(.21)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.06) \\
71	GPT-2\,XL, $\tau$  & \textbf{p90\_ppl\,(.25)}, \textbf{p75\,(.15)}, m\_surp\,(.13), var\_surp\,(.12), p50\,(.05) \\
72	GPT-2\,XL, top-$k$ & \textbf{p90\_ppl\,(.24)}, \textbf{p75\,(.12)}, var\_surp\,(.10), m\_surp\,(.09), ttr\,(.04) \\
73	OLMo, nuc.         & \textbf{p90\_ppl\,(.18)}, \textbf{var\_surp\,(.15)}, p75\,(.11), m\_surp\,(.07), ttr\,(.06) \\
74	OLMo, $\tau$       & \textbf{p90\_ppl\,(.21)}, \textbf{var\_surp\,(.16)}, p75\,(.12), m\_surp\,(.09), ttr\,(.05) \\
75	OLMo, top-$k$      & \textbf{p90\_ppl\,(.20)}, \textbf{var\_surp\,(.17)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.05) \\
76	\bottomrule
77	\end{tabular}}
78	\end{table}
79	
80	\begin{figure}[t]
81	\centering
82	\includegraphics[width=\columnwidth]{figures/fig_atlas_heatmap.pdf}
83	\caption{Atlas feature importance heatmap for the top-7 features. Rows: features ranked by mean Gini importance; columns: 9 model--strategy cells. Stars mark the two universal top-2 features (\texttt{p90\_ppl}, \texttt{var\_surprisal}). Full 19-feature breakdown in Appendix~\ref{app:feature_ablation}.}
84	\label{fig:atlas_heatmap}
85	\end{figure}
86	
87	%% ----------------------------------------------------------------
88	\subsection{EDD Analysis}
89	\label{sec:atlas:edd}
90	\label{sec:atlas:monotonicity}
91	
92	Depth features exhibit strong monotonic trends (Spearman $\rho = -1.0$ for perplexity tail statistics; Figure~\ref{fig:feature_trajectory}); inter-depth distances are non-uniform (d0-vs-d1 AUC ${>}$0.99 in all 9 cells, d2-vs-d3: 0.69--0.89).
93	
94	We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
95	Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (Pythia-1.4B).
96	We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
97	
98	\paragraph{AUC decay and cross-model convergence.}
99	For Pythia-1.4B (nucleus), AUC decays monotonically from $0.999$ (d0v1) to $0.683$ (d4v5); AUC-excess contraction ratios (0.80 at d1v2$\to$d2v3, 0.69 at d3v4$\to$d4v5) show convergence toward indistinguishability accelerates with depth (Figure~\ref{fig:auc_decay}).
100	The d3-vs-d4 AUC clusters near $T{=}0.75$ for all three models (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$), while d4-vs-d5 converges to a narrow band ($0.681$--$0.684$, range $0.003$), suggesting an architecture-independent depth ceiling within the 1--1.5B nucleus setting.
101	Bootstrap testing ($H_0{:}\, \mathrm{AUC} \leq 0.75$; Bonferroni-corrected for 3 comparisons, $\alpha{=}0.0167$) yields $p = 0.001$ (Pythia), $0.091$ (OLMo), $0.505$ (GPT-2~XL).
102	
103	\paragraph{EDD threshold sensitivity.}
104	Across the 9-cell benchmark (depths 0--3), all cells achieve $\mathrm{EDD}{=}3$ at $T{=}0.65$; at $T{=}0.70$, 8/9 cells; at $T{=}0.75$, 7/9; at $T{=}0.80$, 5/9.
105	Top-$k$ configurations lose $\mathrm{EDD}{=}3$ first (Pythia top-$k$ at $T{=}0.70$, OLMo top-$k$ at $T{=}0.75$); d2-vs-d3 is the consistent bottleneck.
106	
107	\begin{figure}[t]
108	\centering
109	\includegraphics[width=\columnwidth]{figures/fig_auc_decay.pdf}
110	\caption{AUC decay curves for Pythia-1.4B (nucleus, depths 0--5) under three pipeline configurations: binary pairwise RF, 4-class RF, and 6-class RF. Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All curves converge below 0.70 at d4-vs-d5. Shaded bands: bootstrap 95\% CIs.}
111	\label{fig:auc_decay}
112	\end{figure}
113	
114	%% ----------------------------------------------------------------
115	\subsection{Strategy-Dependent Trajectories}
116	\label{sec:atlas:strategy}
117	
118	The three strategies induce qualitatively distinct degradation trajectories.
119	Temperature ($\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.9\%, OLMo 82.3\%) because uniform logit scaling accelerates convergence to an attractor~\cite{shumailov2024_nature}, amplifying the fingerprint but creating a boundary reversal risk under cross-strategy transfer (\S\ref{sec:generalization}).
120	Top-$k$ ($k{=}50$) produces the lowest accuracy (68.9--75.8\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens.
121	The strategy effect (9.3\,pp range) exceeds the model effect (7.2\,pp); deployment-time knowledge of the decoding strategy matters at least as much as the generator model.
122	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f6e5e72-0152-443d-851d-978fa5417548",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "c9b20742-0609-4aed-b982-41c5dab9293e",
  "sourceToolAssistantUUID": "0f6e5e72-0152-443d-851d-978fa5417548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T04:54:26.874Z_

Perfect! Now I have a complete picture. Let me verify the .bib file location and create a summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9b20742-0609-4aed-b982-41c5dab9293e",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1ZRemR5RhEisMmR7PN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01316059-2a4b-4faa-a80a-fd4c4af9fd0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TuB54dgRRFyB6W94YHZUiE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7549,
      "cache_read_input_tokens": 61078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7549,
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

_source line 22 · 2026-05-22T04:54:27.694Z_

<details open><summary>🔧 Tool call — Read · `toolu_013UeTuMJ4D6ghJRuaPBfZPN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01316059-2a4b-4faa-a80a-fd4c4af9fd0b",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1ZRemR5RhEisMmR7PN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "12741a85-3ad2-4e7c-98c6-9ef25638d7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TuB54dgRRFyB6W94YHZUiE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7549,
      "cache_read_input_tokens": 61078,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7549
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 131,
          "cache_read_input_tokens": 61078,
          "cache_creation_input_tokens": 7549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7549,
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

_source line 23 · 2026-05-22T04:54:27.715Z_

<details><summary>↩ Tool result · `toolu_013UeTuMJ4D6ghJRuaPBfZPN`</summary>

```text
1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},
46	  year      = {2024},
47	  note      = {arXiv:2307.01850},
48	  url       = {https://arxiv.org/abs/2307.01850},
49	}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12741a85-3ad2-4e7c-98c6-9ef25638d7e8",
  "isSidechain": true,
  "promptId": "b16e5ffa-4125-4979-b6b4-1ec3a848cfe3",
  "agentId": "a0070ff34e51f9c82",
  "type": "user",
  "uuid": "4087f216-45a8-4622-9057-eaaba23d4ed7",
  "sourceToolAssistantUUID": "12741a85-3ad2-4e7c-98c6-9ef25638d7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-22T04:54:40.434Z_

Perfect! I now have all the information needed. Let me compile the final report.

## Summary: LaTeX Paper Files for recursive_gen_depth_est Project

### Main Paper Files Found

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/`

#### Core Files:
1. **Main .tex file:** `main.tex` - Orchestrates the document structure with `\input{}` commands
2. **.bib file:** `references.bib` - Bibliography with model collapse papers and related work

#### Section Files (organized by `main.tex`):
1. `abstract.tex` - Abstract section
2. `introduction.tex` - Introduction section
3. `related_work.tex` - Related Work section
4. `method.tex` - Method section with subsections:
   - Problem Definition
   - Multi-Generational Benchmark Construction
   - Statistical Feature Design
   - Effective Discriminable Depth (EDD)
5. `theory.tex` - Theoretical Motivation
6. `atlas.tex` - The Depth Degradation Atlas section (contains feature importance analysis)
7. `generalization.tex` - Generalization and Robustness section with subsections:
   - Classifier Comparison and Surface-Text Ablation
   - Cross-Model Transfer
   - Cross-Strategy Transfer
   - Preliminary Cross-Scale Observations (14B)
8. `discussion.tex` - Discussion and Conclusion section
9. `conclusion.tex` - Conclusion section

#### Appendix Structure (in `section_appendix.tex`):

The appendix contains extensive supplementary material with 25+ subsections:
- Appendix A: LoRA Fine-Tuning Protocol
- Appendix B: Additional Results (19 detailed subsections including):
  - Top-k Feature Trajectories
  - **Permutation Importance** (A.2) - Feature importance robustness analysis
  - Feature Trajectories
  - Per-Class Recall
  - DCOL Iteration Details
  - Zero-Shot LLM Prompt Template
  - Temperature Robustness
  - Feature Overlap Analysis
  - End-to-End Learning
  - Domain Bias Analysis
  - Wild-Data Calibration
  - Downstream Curation PoC
  - Reference Model Ablation
  - Cross-Scale Full Results (extensive)
  - Cross-Boundary Generalization
  - Cross-Seed Replication
  - Depth-4 Extension
  - Generation Length Ablation
  - Mixed-Depth Corpus
  - Learned Estimator Comparison
  - Instruction-Tuned Model at 1.5B Scale
  - Downstream Fine-Tuning Probe
  - Feature Group Ablation
  - RF Seed Robustness
  - Binary Detector Baselines
  - Binoculars Feature Ablation and Signal Decomposition
  - Prompted Generation Results
  - Extended Discussion
  - Computational Resources and Reproducibility

### Feature Importance Analysis (Section 4.2 equivalent)

**Location:** `atlas.tex`, subsection 4.2 titled **"Feature Consistency Across the Grid"** (lines 40-86)

**Key findings on feature importance:**
- Feature importance rankings are shown in Table 3 (tab:feature_importance)
- Top-2 features are consistently:
  - **p90_ppl** (90th percentile perplexity) - appears in top-2 in all 9 cells
  - **var_surprisal** (surprisal variance) - appears in top-2 in 8/9 cells
- These features account for 41% of total importance (combined Gini: 22.4% + 18.8%)
- Feature ablation shows top-5 features achieve 97.6% of full accuracy
- Perplexity features alone reach 76.6% accuracy (vs 78.4% full)

### Additional Key Details

- **Total paper structure:** 7 main sections + appendix with supplementary material
- **Appendix depth:** Extends from depths 0-5 (main paper uses 0-3 for primary results)
- **Reference model used:** Pythia-1.4B as reference for feature extraction
- **Bibliography entries:** Contains model collapse literature and AI detection baselines

All files are in LaTeX format and organized in the single directory `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4087f216-45a8-4622-9057-eaaba23d4ed7",
  "isSidechain": true,
  "agentId": "a0070ff34e51f9c82",
  "requestId": "req_011CbH1ZdVesLiDQ49meff1M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "336fc4dd-03fb-423b-b66b-d13cd3a397c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/.claude/sessions/agent_7e0c4ba8",
  "sessionId": "c2859d15-42da-4b70-9484-b6a50be64d5d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "structured-brewing-tower",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GsWHRHnGigBv5a8tNXTiUZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 991,
      "cache_read_input_tokens": 68627,
      "output_tokens": 1083,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 991
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1083,
          "cache_read_input_tokens": 68627,
          "cache_creation_input_tokens": 991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 991,
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
