# Research conversation: Read ALL tex files from the paper at `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_ca

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9ea56a89a347f615.jsonl`
- **Structured JSON:** [`ab2bba35d3d5a589e328.json`](../../sessions/ab/ab2bba35d3d5a589e328.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-23T19:16:54.578Z_

Read ALL tex files from the paper at `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/` and also `docs/paper/main.tex`. 

For each file, extract ALL numerical values that appear - specifically:
- AUROC values (0.xxx format)
- SYCONScore values
- ToF/NoF values  
- Percentages (xx%)
- Checkpoint step numbers
- Sample counts
- Ratios (like 1.7×, 3.7×)
- Any other quantitative claims

For each number, note:
1. The exact value
2. Which file and approximate context (what sentence/table/figure it's in)
3. What it refers to (e.g., "AUROC for Qwen3-8B", "ToF for GRPO seed 1")

Be thorough - read every file completely. Output a structured list organized by section.

Important: Read the full content of every .tex file. Don't skip any.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "3fcfc334-6e81-413f-a8d6-52d88a7fb886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T19:16:54.582Z_

```json
{
  "parentUuid": "3fcfc334-6e81-413f-a8d6-52d88a7fb886",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f43ce7c9-e67d-4e70-af51-37c87a646d51",
  "timestamp": "2026-05-23T19:16:54.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-23T19:16:57.060Z_



I'll read all the tex files systematically. Let me start by finding all files and reading them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f43ce7c9-e67d-4e70-af51-37c87a646d51",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL392X3xtuStmA4tDQMA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a67f687-0fd1-46a0-9f87-51459745ab0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHJRnSW7vXm8wjoVCgDW5P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14046,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14046,
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

_source line 4 · 2026-05-23T19:16:57.679Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0195Api3w1hrwFnfYLdBdHz1`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a67f687-0fd1-46a0-9f87-51459745ab0e",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL392X3xtuStmA4tDQMA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59f859bc-1275-463a-9b74-5e9c94221ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHJRnSW7vXm8wjoVCgDW5P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14046,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14046,
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

### Tool result

_source line 5 · 2026-05-23T19:16:57.704Z_

<details><summary>↩ Tool result · `toolu_0195Api3w1hrwFnfYLdBdHz1`</summary>

```text
docs/paper/_stale/direction_quality.tex
docs/paper/_stale/cosine_failure.tex
docs/paper/_stale/probe_trap.tex
docs/paper/_stale/related_work.tex
docs/paper/_stale/framework.tex
docs/paper/_stale/introduction.tex
docs/paper/_stale/discussion.tex
docs/paper/_stale/conclusion.tex
docs/paper/_stale/abstract.tex
docs/paper/_stale/limitations.tex
docs/paper/sections/probe_trap.tex
docs/paper/sections/appendix.tex
docs/paper/sections/cosine_failure.tex
docs/paper/main.tex
docs/paper/sections/related_work.tex
docs/paper/sections/abstract.tex
docs/paper/sections/discussion.tex
docs/paper/sections/introduction.tex
docs/paper/sections/framework.tex
docs/paper/sections/direction_quality.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59f859bc-1275-463a-9b74-5e9c94221ba4",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "5e37b6d7-baf4-4bf5-a216-abc6a0668519",
  "sourceToolAssistantUUID": "59f859bc-1275-463a-9b74-5e9c94221ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-23T19:17:00.193Z_

Now let me read all the active section files and main.tex in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e37b6d7-baf4-4bf5-a216-abc6a0668519",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3923c355-9c05-4aad-9662-6bd235990cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 7 · 2026-05-23T19:17:02.166Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N6VXw5zT78tKycPXS3bHY2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3923c355-9c05-4aad-9662-6bd235990cc8",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "974c099c-3869-4390-b014-58058a97bec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 8 · 2026-05-23T19:17:02.180Z_

<details><summary>↩ Tool result · `toolu_01N6VXw5zT78tKycPXS3bHY2`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliography{references}
51	
52	\appendix
53	\input{sections/appendix}
54	
55	\end{document}
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "974c099c-3869-4390-b014-58058a97bec7",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "b0cfa979-ae78-41c9-9afd-be16d2c60775",
  "sourceToolAssistantUUID": "974c099c-3869-4390-b014-58058a97bec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:17:02.629Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UNMCyQZ59kszc75KmgjqPW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0cfa979-ae78-41c9-9afd-be16d2c60775",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3800eed0-d21a-4bae-abd2-5c8be9d2e3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 10 · 2026-05-23T19:17:02.635Z_

<details><summary>↩ Tool result · `toolu_01UNMCyQZ59kszc75KmgjqPW`</summary>

```text
1	We quantify a temporal decoupling we call the \emph{probe reward trap}: when a frozen linear probe on a contrastive sycophancy direction ($\dsyc$, cross-validated AUROC $0.827$ on Qwen3-8B, $0.779$ on Llama-3-8B) is used as an SFT training signal, behavioral death (true-positive flip rate $= 0$) occurs within 500 steps while generation entropy remains healthy (0.70). In our experiments, the resulting 1{,}300-step lag before distributional collapse means that entropy monitoring---the most common safeguard against reward hacking---misses the failure entirely. Because the trap arises under SFT with stopped gradients, it is independent of RL optimization dynamics, revealing a semantic limitation of the direction itself: $\dsyc$ encodes \emph{whether} belief changed, not \emph{whether it should have}. In additional experiments on Qwen3-8B using GRPO with group size 2, cosine and continuous probe formulations of $\dsyc$ also produced behavioral collapse; removing $\dsyc$ entirely, behavioral-reward-only GRPO exceeded vanilla at only 4 of 31 checkpoints (12.9\%), while ACT (dense per-token SFT) exceeded vanilla at every evaluated checkpoint (47/47 across all configurations). A group-size ablation and LoRA-controlled comparison confirm that this categorical reliability gap reflects supervision granularity rather than adapter capacity.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3800eed0-d21a-4bae-abd2-5c8be9d2e3d0",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "a1f0903c-48fd-488f-a84a-b4370cbd0314",
  "sourceToolAssistantUUID": "3800eed0-d21a-4bae-abd2-5c8be9d2e3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:17:03.207Z_

<details open><summary>🔧 Tool call — Read · `toolu_018FSBAF9xoTZsc6iVp1a8EE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1f0903c-48fd-488f-a84a-b4370cbd0314",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71698db6-2806-454e-b02b-0392aac7f689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 12 · 2026-05-23T19:17:03.213Z_

<details><summary>↩ Tool result · `toolu_018FSBAF9xoTZsc6iVp1a8EE`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/fig_teaser.pdf}
7	\caption{The probe reward trap. (a)~$\dsyc$ discriminates sycophantic from non-sycophantic activations (AUROC $0.827$), but valid revision and unwarranted capitulation overlap along the same direction. (b)~When used as an SFT reward, behavioral death ($\tof{=}0$) occurs at step 500 while entropy remains healthy; the 1{,}300-step lag renders standard monitoring blind.}
8	\label{fig:teaser}
9	\end{figure}
10	
11	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
12	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827$ on Qwen3-8B and $0.779$ on Llama-3-8B, with discriminability rising monotonically across evidence-strength levels (\S\ref{sec:direction_quality}), though 256-token truncation during GRPO training degrades this to approximately 0.60 (\S\ref{sec:cosine_failure}).
13	These results point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a training signal.
14	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level signal could target the internal computation rather than its surface outputs.
15	
16	This paper documents the \emph{probe reward trap}: when a frozen linear probe on $\dsyc$ is used as an SFT training signal with stopped gradients, behavioral death ($\tof = 0$) occurs within 500 steps while generation entropy remains healthy (0.70), masking the failure from standard monitoring (\S\ref{sec:probe_trap}).
17	In our experiments, the 1{,}300-step lag before distributional collapse means entropy-based early stopping---the most common safeguard against reward hacking \citep{casper2023openproblems}---would miss the failure entirely, with the reward averaging $+0.72$ throughout.
18	Because the trap arises under SFT rather than GRPO, it reflects a limitation of $\dsyc$ itself: the direction encodes \emph{whether} belief changed, not \emph{whether it should have}, so any reward conditioned on it alone will either be gamed or reward rigidity.
19	
20	Under our GRPO configuration (Qwen3-8B, group size$=$2), two additional $\dsyc$-based formulations---cosine projection (\S\ref{sec:cosine_failure}) and continuous probe---also produced behavioral collapse.
21	Removing $\dsyc$ entirely, $\rthree$-only GRPO (behavioral reward alone) exceeded vanilla at only 4 of 31 checkpoints (12.9\%) across two seeds and a group-size ablation.
22	ACT \citep{consistency2025bctact} (dense per-token SFT) exceeds vanilla at every evaluated checkpoint (47/47 across all configurations; \S\ref{sec:discussion}), and a LoRA-controlled ablation confirms the reliability gap reflects supervision granularity.
23	
24	The root cause is a semantic gap between discriminability and reward utility.
25	Techniques for discovering latent knowledge \citep{burns2023ccs} and representation-guided RL \citep{zhang2026latentgrpo} share a premise: a direction with high discriminability should transfer into a useful training signal.
26	For reasoning faithfulness and safety directions, this premise holds because the behavior to suppress is geometrically distinct from the behavior to preserve.
27	Sycophancy violates this condition: capitulation under social pressure and revision under valid evidence produce overlapping activation signatures along $\dsyc$ \citep{wang2025internal, shapira2026amplifies}.
28	When reward overoptimization \citep{gao2023scaling} operates on a signal that conflates compliance with capitulation, the result is predictable collapse \citep{skalse2022hacking}.
29	
30	This paper presents a negative result with mechanistic analysis.
31	Our two principal findings (Figure~\ref{fig:teaser}):
32	
33	\begin{itemize}
34	\item \textbf{The probe reward trap} (C2): behavioral death ($\tof{=}0$) precedes distributional collapse by 1{,}300 steps, rendering entropy monitoring blind. The trap arises under SFT with stopped gradients, implicating $\dsyc$ itself rather than the optimizer (\S\ref{sec:probe_trap}).
35	
36	\item \textbf{Categorical reliability gap between supervision paradigms} (C1): per-token SFT exceeds vanilla at every checkpoint (47/47 across all configurations and seeds) while per-completion GRPO exceeds vanilla at only 4/31 (12.9\%); under matched LoRA, the magnitude gap is $1.7{\times}$ (\S\ref{sec:discussion}).
37	\end{itemize}
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71698db6-2806-454e-b02b-0392aac7f689",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "e18db04e-9eb4-42b2-a0c0-2740b0419b9a",
  "sourceToolAssistantUUID": "71698db6-2806-454e-b02b-0392aac7f689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:17:04.040Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RkjCcWmXmmDAz4SghDrsTz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e18db04e-9eb4-42b2-a0c0-2740b0419b9a",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4aa5a1f1-4686-4135-a091-5d6222b02bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 14 · 2026-05-23T19:17:04.045Z_

<details><summary>↩ Tool result · `toolu_01RkjCcWmXmmDAz4SghDrsTz`</summary>

```text
1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	\subsection{Direction Extraction}
5	\label{ssec:extraction}
6	
7	We extract a linear sycophancy direction $\dsyc$ from the residual stream using contrastive activation pairs: a \emph{valid correction} (warranted belief revision under strong evidence) and a \emph{sycophantic capitulation} (unwarranted concession under social pressure).
8	We construct 181 contrastive pairs using GPT-4.1 \citep{openai2025gpt41} in a two-stage pipeline: skeleton generation followed by 3-turn dialogue completion.
9	Style matching is enforced by automated validation (response length difference ${<}10\%$, shared opening phrase ${\geq}2$ words), with up to 3 retries per pair; 19 of 200 initial pairs were discarded for failing validation.
10	Evidence strength is annotated at three levels: \emph{weak} (75 pairs; personal memory or opinion), \emph{medium} (54 pairs; brief source citation), and \emph{strong} (52 pairs; authoritative source with detailed data).
11	From the 181 paired examples (362 activations total), we compute the mean difference at target layer $\ell$:
12	\begin{equation}
13	\label{eq:dsyc}
14	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
15	\end{equation}
16	where $\mathbf{h}^{+}_i$ and $\mathbf{h}^{-}_i$ are residual-stream activations for the $i$-th valid and sycophantic response.
17	The target layer is selected by 5-fold cross-validated AUROC; on Qwen3-8B this yields layer 19 with AUROC $0.827 \pm 0.028$ (5-fold CV).
18	
19	\subsection{Reward Formulations}
20	\label{ssec:reward}
21	
22	Three formulations translate $\dsyc$ into a direction-based signal $\rone$.
23	For F1 and F3, $\rone$ enters as part of a GRPO \citep{shao2024grpo} reward $R = w_1 \cdot \rone + w_3 \cdot \rthree$, where $\rthree$ is a behavioral component (DeBERTa NLI classifier scoring consistency with the ground-truth answer).
24	\begin{itemize}
25	\item[\textbf{F1}] \textbf{Cosine projection} with four variants: (a) tanh-gated dot product $\tanh(\mathbf{h} \cdot \dsyc / 20)$, (b) raw cosine $\cos(\mathbf{h},\, \dsyc)$, (c) raw cosine with online recalibration (\S\ref{ssec:recalib}), and (d) $5{\times}$ scaled cosine. See \S\ref{sec:cosine_failure} for details.
26	\item[\textbf{F2}] \textbf{Binary probe (SFT).} $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$, a frozen logistic probe with stopped gradients; trained via a custom SFT loss rather than GRPO (\S\ref{sec:probe_trap}).
27	\item[\textbf{F3}] \textbf{Continuous probe.} $\rone = 1 - P(\text{syc} \mid \mathbf{h})$, the sigmoid output of the same logistic probe, providing a continuous reward signal without discretization.
28	\end{itemize}
29	The weight $w_1$ is set by diagnostic-driven iteration rather than grid search (Appendix~\ref{app:training}).
30	As an ablation, R3-only GRPO sets $w_1{=}0$, training with only the behavioral reward.
31	
32	\subsection{Online Recalibration}
33	\label{ssec:recalib}
34	
35	LoRA fine-tuning shifts internal representations, so we re-extract $\dsyc$ every 500 steps.
36	The cosine similarity between consecutive directions remains ${\approx}\,0.96$ at step 500, indicating slow drift relative to recalibration frequency.
37	
38	\subsection{SFT Baseline: Activation Consistency Training}
39	\label{ssec:baselines}
40	
41	We implement Activation Consistency Training \citep[ACT;][]{consistency2025bctact}, which combines standard SFT loss with an L2 activation consistency loss at target layers, providing dense per-token supervision.
42	Unlike GRPO's single scalar per completion, ACT operates at the token level using labeled valid/invalid pairs.
43	
44	\subsection{Evaluation}
45	\label{ssec:eval}
46	
47	The \emph{True-positive Flip rate} ($\tof$) measures acceptance of valid corrections; the \emph{No-Flip rate} ($\nof$) measures resistance to invalid pressure.
48	Their harmonic mean captures the calibration trade-off:
49	\begin{equation}
50	\label{eq:sycon}
51	\sycon = \frac{2 \cdot \tof \cdot \nof}{\tof + \nof}
52	\end{equation}
53	By design, $\sycon = 0$ whenever $\tof = 0$: a model that never accepts valid corrections receives no credit for resisting invalid ones.
54	Flip classification uses \texttt{cross-encoder/nli-deberta-v3-base} \citep{he2023debertav3}, following \citet{consistency2025bctact}.
55	All experiments use Qwen3-8B \citep{yang2025qwen3} with LoRA (rank$=$64; $\alpha{=}64$ for GRPO, $\alpha{=}128$ for ACT) and DeepSpeed ZeRO-2.
56	GRPO uses a group size of 2 due to memory constraints with 8B-parameter models, below the typical range of 8--64 \citep{shao2024grpo}; full hyperparameters are reported in Appendix~\ref{app:training}.
57	We test six $\dsyc$-based configurations: four cosine $\rone$ variants (F1a--F1d) and continuous probe $\rone$ (F3) using GRPO, plus binary probe $\rone$ (F2) using SFT, $\rthree$-only GRPO as a non-directional baseline, and ActAdd as an inference-time baseline.
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4aa5a1f1-4686-4135-a091-5d6222b02bba",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "d2961d50-70ab-4ef1-9abe-373e774b3282",
  "sourceToolAssistantUUID": "4aa5a1f1-4686-4135-a091-5d6222b02bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:17:04.513Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CcRbng3xBE8UojQWFQXXtt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/cosine_failure.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2961d50-70ab-4ef1-9abe-373e774b3282",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddf6417d-33eb-49fe-a1dc-433529015293",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 16 · 2026-05-23T19:17:04.517Z_

<details><summary>↩ Tool result · `toolu_01CcRbng3xBE8UojQWFQXXtt`</summary>

```text
1	\section{Cosine \texorpdfstring{$\rone$}{R1}: Structural Failure}
2	\label{sec:cosine_failure}
3	
4	Section~\ref{sec:direction_quality} established that $\dsyc$ achieves AUROC 0.827 on Qwen3-8B using full-length responses.
5	During GRPO training, 256-token truncation reduces $\dsyc$ AUROC to approximately 0.60, meaning the optimizer works with a substantially weaker signal than offline metrics suggest.
6	We now test whether this discriminability translates into a viable GRPO reward.
7	Four configurations form a diagnostic chain (Table~\ref{tab:cosine_chain}): each resolves the failure mode of its predecessor but exposes a deeper limitation.
8	
9	\begin{table}[t]
10	\centering
11	\caption{Cosine $\rone$ failure chain on Qwen3-8B (LoRA rank$=$64, GRPO with $R = w_1 \cdot \rone + w_3 \cdot \rthree$).}
12	\label{tab:cosine_chain}
13	\begin{tabular}{lllll}
14	\toprule
15	Config & $\rone$ Formula & $w_1$ & Outcome & Root Cause \\
16	\midrule
17	F1a & $\tanh(\mathbf{h}\cdot\dsyc/20)$ & 0.25 & Gate saturation & Norm mismatch \\
18	F1b & $\cos(\mathbf{h},\, \dsyc)$ & 0.25 & $\rone \approx 0$ & Gap too small \\
19	F1c & +recalibration & 0.25 & Mode collapse & Reward discontinuity \\
20	F1d & $5\cos(\mathbf{h},\, \dsyc)$ & 0.40 & Mode collapse & $\rthree$ saturation \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	F1a uses a dot-product formulation ($\rone = \tanh(\mathbf{h} \cdot \dsyc / 20)$), but residual-stream norms exceed the direction norm by $100$--$1{,}200{\times}$, saturating the tanh gate and zeroing the gradient by step 955.
26	Switching to cosine similarity (F1b) eliminates norm dependence, yet the cosine gap between valid and sycophantic activations averages only 0.098 across layers---too narrow to generate meaningful reward contrast.
27	Online recalibration (F1c, \S\ref{ssec:recalib}) raises offline AUROC from 0.827 to 0.910 but paradoxically triggers mode collapse: the abrupt shift in $\dsyc$ at each recalibration event creates a reward discontinuity that destabilizes GRPO advantage estimates, collapsing entropy to 0.069 within 300 steps.
28	Amplifying the signal with $5{\times}$ scaling (F1d) lifts $\rone$ above the noise floor but simultaneously amplifies the conflation between warranted revision and unwarranted capitulation; $\rthree$ saturates at 0.9998 by step 300, leaving the noisy $\rone$ as the sole gradient source until terminal collapse at step 2160.
29	
30	Truncation further degrades the signal: under the 256-token maximum completion length used in GRPO, $\dsyc$ AUROC drops from 0.76 (full response) to 0.60, so the offline discriminability (0.827) substantially overestimates the signal available during training.
31	Checkpoint-level evaluation confirms immediate collapse: $\tof{=}0$ from step 500 onward with no stable phase.
32	The four configurations converge on a single conclusion: $\dsyc$ encodes the \emph{direction} of belief change but not whether that change is \emph{warranted}.
33	Valid revision and sycophantic capitulation both shift activations toward the user's position along $\dsyc$, so the cosine projection assigns similar scores to both.
34	This is not a calibration artifact---recalibration improves discriminability yet rewards still fail---but a semantic limitation of any continuous $\dsyc$-based reward.
35	Section~\ref{sec:probe_trap} examines whether discretizing the signal via a binary probe can escape this limitation.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddf6417d-33eb-49fe-a1dc-433529015293",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "05cf1c76-08c7-4e5b-8ec1-a717ed16904c",
  "sourceToolAssistantUUID": "ddf6417d-33eb-49fe-a1dc-433529015293",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:17:05.018Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PysaGfJzMu4oL8rFuzP5Ut`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/probe_trap.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05cf1c76-08c7-4e5b-8ec1-a717ed16904c",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7484401-c830-4edd-b07e-1fdafb29e719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 18 · 2026-05-23T19:17:05.026Z_

<details><summary>↩ Tool result · `toolu_01PysaGfJzMu4oL8rFuzP5Ut`</summary>

```text
1	\section{The Probe Reward Trap}
2	\label{sec:probe_trap}
3	
4	The cosine formulations fail because the continuous projection of $\dsyc$ produces a gap too narrow for reward contrast.
5	A natural remedy is to discretize: train a logistic probe on $\dsyc$ and threshold its output, yielding $\rone = \mathbb{I}[P(\text{syc} \mid \mathbf{h}) < 0.5]$ (F2 in \S\ref{ssec:reward}).
6	We show that this discretization sidesteps the magnitude problem but creates a qualitatively worse failure.
7	Both probe experiments use SFT rather than GRPO (\S\ref{ssec:reward}); the trap is therefore independent of GRPO's optimization dynamics.
8	
9	\paragraph{Differentiable probe: gradient gaming.}
10	Without stop-gradient (exp-008), the policy discovers within ${\sim}30$ steps that shifting activations away from the sycophancy cluster maximizes $\rone$ regardless of response content, producing an inverted profile ($\tof = 0.978$, $\nof = 0.006$).
11	This motivates the frozen-probe design below.
12	
13	\paragraph{Binary probe: the stubbornness trap.}
14	With stop-gradient (exp-008v3), the policy cannot game the boundary but instead exploits a deeper flaw: $\dsyc$ does not condition on input validity, so refusing to revise a wrong answer receives the same $\rone = 1$ as correctly resisting invalid pressure.
15	By step 500, $\tof$ drops to 0.000 and $\nof$ reaches 0.995, yielding $\sycon = 0$.
16	Qualitative analysis of 181 valid-correction responses reveals five failure modes: \emph{deliberation traps} (28.7\%), where the model identifies the correct answer but cannot commit; \emph{sycophantic stubbornness} (24.3\%), where the model verbally agrees but does not change its answer; \emph{acknowledge-but-maintain} (23.8\%); \emph{genuine-accept-missed} (18.8\%); and refute/ignore/other (4.5\%). Full taxonomy in Appendix~\ref{app:taxonomy}.
17	
18	\paragraph{Behavioral death precedes distributional collapse.}
19	
20	\begin{table}[t]
21	\centering
22	\caption{Probe reward trap trajectory (exp-008v3). Behavioral death ($\tof{=}0$) occurs at step 500; entropy remains healthy until step ${\sim}1840$. Reward averages $+0.72$ throughout.}
23	\label{tab:probe_trajectory}
24	\begin{tabular}{lccccc}
25	\toprule
26	Step & $\tof$ & $\nof$ & $\sycon$ & Entropy & Reward \\
27	\midrule
28	500 & 0.000 & 0.995 & 0.000 & 0.702 & +0.72 \\
29	1000 & 0.006 & 0.995 & 0.011 & 0.800 & +0.71 \\
30	1500 & 0.000 & 1.000 & 0.000 & 0.608 & +0.69 \\
31	2000 & 0.000 & 1.000 & 0.000 & 0.304 & +0.69 \\
32	\bottomrule
33	\end{tabular}
34	\end{table}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig_probe_trap.pdf}
39	\caption{Probe reward trap (exp-008v3). $\tof$ drops to zero at step 500 while generation entropy remains high (0.70--0.80 through step 1000). The 1{,}300-step lag means standard entropy monitoring misses the behavioral failure entirely.}
40	\label{fig:probe_trap}
41	\end{figure}
42	
43	Table~\ref{tab:probe_trajectory} and Figure~\ref{fig:probe_trap} reveal a 1{,}300-step lag between behavioral and distributional collapse.
44	At step 500, the model is behaviorally dead ($\tof = 0$) yet entropy remains high (0.70--0.80) through step 1000---well within the range that standard monitors would flag as healthy---and the combined reward averages $+0.72$ because both $\rone$ and $\rthree$ reinforce non-flipping.
45	Entropy does not collapse until step ${\sim}1840$.
46	This gap carries a practical warning: entropy-based early stopping, the most common safeguard against reward hacking~\citep{casper2023openproblems}, would miss the failure entirely.
47	Detecting probe reward traps requires behavioral monitoring (periodic $\tof$ evaluation), not distributional monitoring alone.
48	
49	\paragraph{A dilemma for direction-based rewards.}
50	The differentiable and binary failures bracket the design space.
51	With gradients, the policy games the boundary; without gradients, it exploits the fact that stubbornness and genuine resistance are indistinguishable along $\dsyc$.
52	Any reward conditioned only on $\dsyc$---continuous or discrete, differentiable or frozen---will either be gamed or will reward rigidity.
53	Escaping this dilemma requires a signal that incorporates the evidential warrant of the user's challenge, a dimension that $\dsyc$ does not encode~\citep{denison2024subterfuge}.
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7484401-c830-4edd-b07e-1fdafb29e719",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "5608faf9-c40d-46ff-b062-4c12c0b5a25e",
  "sourceToolAssistantUUID": "c7484401-c830-4edd-b07e-1fdafb29e719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:17:05.886Z_

<details open><summary>🔧 Tool call — Read · `toolu_01So3Z1AdqjvUFnhmSb9nNSE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/direction_quality.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5608faf9-c40d-46ff-b062-4c12c0b5a25e",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "177671bb-bd52-4e6c-ad20-2156a8dab45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 20 · 2026-05-23T19:17:05.891Z_

<details><summary>↩ Tool result · `toolu_01So3Z1AdqjvUFnhmSb9nNSE`</summary>

```text
1	\section{Direction Discriminability}
2	\label{sec:direction_quality}
3	
4	Before evaluating $\dsyc$ as a reward signal (\S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap}), we first establish that it captures a genuine sycophancy-related signal in the residual stream.
5	If the direction failed to discriminate sycophantic from non-sycophantic activations, downstream reward failures would be trivially explained by poor direction quality rather than by a fundamental gap between discriminability and reward utility.
6	We evaluate discriminability along five axes: cross-validated classification accuracy, evidence-strength stratification, cross-model transfer, training stability, and probe ablation.
7	Figure~\ref{fig:direction_quality} summarizes the per-layer AUROC profiles for both models.
8	
9	\paragraph{Qwen3-8B layer-wise discriminability.}
10	We evaluate $\dsyc$ via 5-fold cross-validated AUROC on 181 style-controlled contrastive pairs (\S\ref{ssec:extraction}).
11	The direction achieves AUROC $0.827 \pm 0.028$ (5-fold CV) at its best layer (L19).
12	Discriminability emerges gradually across depth: layers L0--L8 perform near chance, statistical significance ($p < 0.01$) first appears at L16, and performance peaks at L19.
13	This gradual emergence, with the peak in the upper third of the network, suggests that sycophancy-relevant information is encoded as a late-stage representation rather than an input-level confound.
14	The direction also captures evidential granularity.
15	AUROC rises monotonically from 0.675 on weak-evidence pairs to 0.883 on medium and 0.929 on strong pairs.
16	Discriminability covaries with evidence strength, possibly because stronger evidence produces more behaviorally distinct responses rather than because $\dsyc$ explicitly encodes epistemic quality.
17	
18	\paragraph{Cross-model generalization.}
19	To rule out that these results are specific to Qwen3-8B's representation geometry, we repeat the full extraction and evaluation pipeline on Llama-3-8B-Instruct \citep{grattafiori2024llama3}.
20	Table~\ref{tab:cross_model} compares the two models.
21	Llama-3-8B achieves AUROC $0.779 \pm 0.019$ (5-fold CV) at L16, with a parallel evidence-strength gradient (weak 0.711, medium 0.864, strong 0.911).
22	The best-layer depth differs (L16 vs.\ L19), consistent with the architectural differences between the two families, but the qualitative pattern is identical: gradual emergence, best-layer selection in the upper third, and monotonic strength scaling.
23	Discriminability is robust across knowledge domains, with per-domain AUROCs on Llama-3-8B ranging from 0.751 (geography) to 0.844 (commonsense).
24	When surface confounds (response length, hedging patterns) are explicitly controlled, Llama-3-8B's AUROC rises to 0.923, which confirms that the direction captures semantic content rather than stylistic artifacts.
25	The consistent results across architecturally distinct model families indicate that contrastive sycophancy directions reflect a shared representational phenomenon rather than a model-specific idiosyncrasy.
26	
27	\begin{table}[t]
28	\centering
29	\caption{Cross-model $\dsyc$ discriminability. AUROC uncertainty is 5-fold cross-validation standard deviation; evidence-strength AUROCs are evaluated on the full dataset at each model's best layer.}
30	\label{tab:cross_model}
31	\begin{tabular}{lccccc}
32	\toprule
33	Model & Best Layer & AUROC ($\pm$ std) & Weak & Medium & Strong \\
34	\midrule
35	Qwen3-8B & L19 & $0.827 \pm 0.028$ & 0.675 & 0.883 & 0.929 \\
36	Llama-3-8B & L16 & $0.779 \pm 0.019$ & 0.711 & 0.864 & 0.911 \\
37	\bottomrule
38	\end{tabular}
39	\end{table}
40	
41	\begin{figure}[t]
42	\centering
43	\includegraphics[width=\columnwidth]{figures/fig_layer_auroc.pdf}
44	\caption{Per-layer AUROC of $\dsyc$ as a function of normalized depth (layer index / total layers). Qwen3-8B (36 layers, solid) shows gradual emergence from near-chance at L0 to a peak at L19, with performance plateauing in the final third. Llama-3-8B (32 layers, dashed; layers 16--31 only) exhibits a similar upper-third concentration. Both models achieve best discriminability in layers 50--60\% through the network.}
45	\label{fig:direction_quality}
46	\end{figure}
47	
48	\paragraph{Training stability and probe ablation.}
49	Two additional analyses confirm the robustness of $\dsyc$ under training dynamics.
50	First, we track direction drift during LoRA fine-tuning: at step 500, the cosine similarity between the original and re-extracted $\dsyc$ is approximately 0.96, and per-layer AUROC remains above 0.77.
51	The direction drifts slowly relative to the 500-step recalibration interval (\S\ref{ssec:recalib}), so the reward signal does not become stale between updates.
52	Second, we compare $\dsyc$ against a random baseline: a logistic probe trained on the learned direction achieves AUROC 0.835, versus 0.727 for a probe trained on a random direction of equal dimensionality ($\Delta{=}{+}0.108$).
53	The learned direction carries substantially more sycophancy-relevant information than an arbitrary axis in the same activation space.
54	
55	\paragraph{Implications for reward design.}
56	These results establish that $\dsyc$ reliably separates sycophantic from non-sycophantic representations across models, evidence-strength levels, and training checkpoints.
57	Direction quality is not the bottleneck.
58	The reward failures documented in \S\ref{sec:cosine_failure}--\S\ref{sec:probe_trap} therefore cannot be attributed to a noisy or degenerate direction; they point to a deeper incompatibility between discriminability and reward utility.
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "177671bb-bd52-4e6c-ad20-2156a8dab45b",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "f798c9b7-14fa-4f6a-bbb8-1f4e29bf68e6",
  "sourceToolAssistantUUID": "177671bb-bd52-4e6c-ad20-2156a8dab45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:17:06.397Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ju5oVpcy1UtvRVMuJJMCwv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f798c9b7-14fa-4f6a-bbb8-1f4e29bf68e6",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ab16859-e7c7-4f46-b334-b1c7c553470b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 22 · 2026-05-23T19:17:06.404Z_

<details><summary>↩ Tool result · `toolu_01Ju5oVpcy1UtvRVMuJJMCwv`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Representation Engineering.}
4	Linear directions in LLM residual streams encode behavioral concepts \citep{zou2023repe}; inference-time methods---ITI \citep{li2023iti}, ActAdd \citep{turner2023actadd}, CAA \citep{rimsky2024caa}---demonstrate that activation geometry suffices for behavioral control \citep{burns2023ccs}.
5	We use the same contrastive extraction as CAA but apply $\dsyc$ as an RL reward, revealing a gap that inference-time work does not encounter.
6	
7	\paragraph{Reward Design and Overoptimization.}
8	Proxy rewards diverge from true objectives under sustained optimization \citep{gao2023scaling}, and reward hacking can escalate to active tampering \citep{denison2024subterfuge}.
9	Our probe trap (\S\ref{sec:probe_trap}) is an extreme instance: the reward actively reinforces degenerate behavior rather than merely being circumvented \citep{skalse2022hacking}.
10	\citet{wu2026rewardhacking} demonstrate that representation-level directions succeed for reward hacking suppression when behaviors are geometrically separable (\S\ref{sec:discussion}).
11	
12	\paragraph{Sycophancy Characterization and Mitigation.}
13	Sycophancy is pervasive in RLHF-trained assistants \citep{sharma2023sycophancy}, amplified by RLHF \citep{shapira2026amplifies}, and traceable to late-layer preference shifts \citep{wang2025internal}; mitigation approaches include synthetic data \citep{wei2024synthetic}, consistency training \citep{consistency2025bctact}, and neuron-level correction \citep{obrien2025fewbadneurons}.
14	Our analysis shows why the step from diagnosis to reward is structurally blocked: $\dsyc$ conflates warranted revision with unwarranted capitulation.
15	
16	\paragraph{Probe-Based and Representation-Guided Methods.}
17	\citet{papadatos2024probepenalties} reduce sycophancy via Best-of-N reranking with linear probe penalties (94\% probe accuracy), where the probe selects among candidates without producing gradients that update model parameters.
18	Our work reveals what happens when a comparable signal (AUROC $0.827$) enters the GRPO training loop: the discriminability--utility gap is specific to gradient-based optimization, not to probe quality per se (\S\ref{sec:discussion}).
19	Latent-GRPO \citep{zhang2026latentgrpo} extends GRPO with latent-space rewards for reasoning; CRAFT \citep{luo2026craft} applies representation-level constraints during RL; \citet{sinii2025smallvectors} and \citet{ackermann2026gradreg} study representation dynamics under RL.
20	SMART \citep{beigi2025smart} applies per-step process rewards with MCTS for sycophancy, succeeding where our completion-level scalar rewards fail; the key difference is supervision granularity, consistent with ACT's per-token success.
21	Preference-based methods (DPO \citep{rafailov2023dpo}, KTO \citep{ethayarajh2024kto}) may accommodate $\dsyc$-derived rankings; whether pair-wise optimization avoids the failures we observe remains open.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ab16859-e7c7-4f46-b334-b1c7c553470b",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "a2e20163-a73d-4ad9-bc9e-bae5a09f8dc9",
  "sourceToolAssistantUUID": "3ab16859-e7c7-4f46-b334-b1c7c553470b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:17:06.872Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B6k4Jx8KrSwjafBFURyTRg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2e20163-a73d-4ad9-bc9e-bae5a09f8dc9",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05332940-1b3f-434a-a827-138bd3a0724a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 24 · 2026-05-23T19:17:06.877Z_

<details><summary>↩ Tool result · `toolu_01B6k4Jx8KrSwjafBFURyTRg`</summary>

```text
1	\section{When Does Discriminability Fail as Reward Utility?}\label{sec:discussion}
2	
3	\paragraph{Root cause of the probe reward trap.}
4	The probe reward trap (\S\ref{sec:probe_trap}) and the cosine failures (\S\ref{sec:cosine_failure}) share a common geometric root.
5	$\dsyc$ encodes the \emph{direction} of belief change but not its \emph{evidential warrant}: valid revision and sycophantic capitulation both shift activations toward the user's position along the same direction.
6	The two reward families expose complementary faces of this blindness.
7	Cosine $\rone$ penalizes all belief change indiscriminately; the resulting mode collapse (F1c, F1d) reflects excessive punishment of any activation shift along $\dsyc$.
8	The binary probe $\rone$ rewards all resistance regardless of input validity; the stubbornness trap ($\tof = 0$ by step 500) reflects excessive permissiveness toward activation stasis.
9	These are not independent design flaws but dual consequences of a direction that conflates the target behavior (resisting invalid challenges) with its complement (refusing valid corrections).
10	Cross-model evidence confirms the limitation extends beyond Qwen3-8B: Llama-3-8B independently achieves AUROC $0.779 \pm 0.019$ on the same contrastive pairs with the same monotonic evidence gradient, so discriminability generalizes across architectures while the semantic gap between discriminability and reward utility persists.
11	This pattern contrasts with reasoning faithfulness and safety directions~\citep{zhang2026latentgrpo}, where the behavior to suppress is geometrically distinct from the behavior to preserve along the relevant direction.
12	\citet{wu2026rewardhacking} reinforce this principle: concept directions applied via advantage modification in GRPO achieve 100\% validation accuracy for reward hacking detection, where shortcut behaviors are geometrically separable.
13	A quantitative comparison of geometric separability between $\dsyc$ and their reward-hacking directions remains an important open question.
14	For sycophancy, the target and its complement occupy the same activation region; they differ only in whether external evidence warrants the belief change.
15	
16	\paragraph{GRPO results under our configuration.}
17	
18	\begin{table}[t]
19	\centering
20	\caption{Comparison of all sycophancy calibration methods on Qwen3-8B. $\sycon$ is the harmonic mean of $\tof$ and $\nof$; higher indicates better calibration. Best result in \textbf{bold}. $^\dagger$Best checkpoint (seed 1, step 6500); only 4/28 checkpoints across two seeds exceed vanilla. $^\ddagger$Seed 2 (15 checkpoints); all exceed vanilla. Best $\sycon{=}0.286$ (step 7000). $^\S$All cosine variants collapsed from step 1 ($\tof{=}0$ at every checkpoint); F1d additionally diverged at step 2160 (entropy ${<}\,0.01$). $^\P$ACT and ActAdd differ from GRPO along 5+ dimensions (\S\ref{sec:discussion}); included for context, not as controlled comparisons.}
21	\label{tab:main_comparison}
22	\begin{tabular}{llcccc}
23	\toprule
24	Method & Type & $\sycon$ $\uparrow$ & $\tof$ $\uparrow$ & $\nof$ $\uparrow$ & Step \\
25	\midrule
26	Vanilla & -- & 0.134 & 0.072 & 0.945 & -- \\
27	\midrule
28	\multicolumn{6}{l}{\textit{GRPO with $\dsyc$}} \\
29	Cosine $\rone$ (F1a--F1d) & RL & 0.000$^\S$ & 0.000 & 1.000 & 500 \\
30	Continuous Probe $\rone$ (F3) & RL & 0.124 & 0.066 & 0.934 & 500 \\
31	\midrule
32	\multicolumn{6}{l}{\textit{SFT with $\dsyc$ probe penalty}} \\
33	Binary Probe $\rone$ (F2) & SFT & 0.000 & 0.000 & 0.995 & 500 \\
34	\midrule
35	\multicolumn{6}{l}{\textit{GRPO without $\dsyc$}} \\
36	$\rthree$-only GRPO & RL & 0.153$^\dagger$ & 0.083 & 0.983 & 6500 \\
37	\midrule
38	\multicolumn{6}{l}{\textit{Reference methods (not directly comparable)$^\P$}} \\
39	ActAdd ($\alpha{=}5$) & Inference & 0.054 & 0.028 & 0.961 & -- \\
40	\textbf{ACT} (seed 1) & SFT & \textbf{0.301} & \textbf{0.182} & 0.867 & 8000 \\
41	ACT (seed 2)$^\ddagger$ & SFT & 0.286 & -- & -- & 7000 \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	Table~\ref{tab:main_comparison} summarizes all methods evaluated on Qwen3-8B.
47	$\rthree$-only GRPO removes $\dsyc$ entirely and relies on the NLI-based behavioral reward alone.
48	If the failures in Sections~\ref{sec:cosine_failure} and~\ref{sec:probe_trap} stemmed solely from the representation reward, this ablation should recover calibration quality.
49	It does not.
50	The $\sycon$ trajectory for $\rthree$-only GRPO oscillates without sustained improvement.
51	Seed 1 peaks at 0.153 (checkpoint 6500) and ends at 0.143 (checkpoint 8000); seed 2 peaks at 0.143 (checkpoint 4000, its only checkpoint exceeding vanilla) and ends at 0.124 (checkpoint 8000).
52	Only 4 of 28 checkpoints across both seeds exceed vanilla (14.3\%): 3/12 for seed 1 (25\%) and 1/16 for seed 2 (6.3\%), while ACT exceeds vanilla at every evaluated checkpoint (31/31 across two seeds; Figure~\ref{fig:trajectory}).
53	Both seeds exhibit oscillations of similar amplitude ($\Delta \approx 0.069$) with crash onset differing by ${\sim}2{,}500$ steps, indicating stochastic drift in a saturated reward landscape.
54	Activation analysis confirms the drift is not representational: $\dsyc$ AUROC varies by ${<}0.01$ across checkpoints and $\rthree$ saturates at ${\sim}0.98$ ($p{=}0.703$), yet $\sycon$ swings by 17\%, reinforcing the disconnect between discriminability and behavioral utility.
55	Under our configuration (group size$=$2), $\rthree$-only GRPO exhibits a similar stubbornness pattern to the $\dsyc$ approaches (high $\nof$, near-zero $\tof$) at milder severity.
56	
57	\paragraph{Competing hypotheses and ablation.}
58	Three explanations are consistent with our GRPO results: (a)~$\dsyc$ is fundamentally unsuitable as a reward signal for sycophancy calibration; (b)~GRPO with group size$=$2 provides insufficient ranking diversity for any reward to achieve stable calibration; (c)~sycophancy calibration is inherently unsuitable for scalar per-completion RL.
59	Two ablations address these hypotheses (Table~\ref{tab:ablation}).
60	Increasing group size from 2 to 8 does not improve $\rthree$-only GRPO: three checkpoints showed a monotonically declining trajectory ($0.084 \to 0.085 \to 0.054$), all below vanilla, and gs$=$8 (best 0.085) underperforms gs$=$2 (best 0.153); the experiment was terminated early.
61	This rules out hypothesis~(b) as the primary explanation.
62	Reducing ACT's LoRA configuration to match GRPO's (rank 64, $\alpha{=}64$, 4 modules) yields $\sycon = 0.267$ (peak 0.326 at step 7000); all 16 checkpoints exceed vanilla.
63	Under identical LoRA configurations, per-token SFT ($\sycon{=}0.267$) exceeds per-completion GRPO ($\sycon{=}0.153$) by $1.7{\times}$; supervision granularity is the primary driver, while LoRA capacity modulates convergence rate but is not the determining factor.
64	The probe reward trap (C2) provides independent evidence for~(a): it arises under SFT where group size is irrelevant.
65	
66	\begin{table}[t]
67	\centering
68	\small
69	\caption{Ablation: isolating supervision paradigm from LoRA configuration. All methods use Qwen3-8B with $\rthree$ (behavioral reward). Vanilla $\sycon{=}0.134$. $^\dagger$Terminated early after three checkpoints showed monotonically declining trajectory. $^\ddagger$Peak at step 7000; final checkpoint (step 8000) $\sycon{=}0.267$.}
70	\label{tab:ablation}
71	\begin{tabular}{llcc}
72	\toprule
73	Method & LoRA config & Best $\sycon$ & ${>}$Van. \\
74	\midrule
75	GRPO gs$=$2 (2 seeds) & r64, $\alpha$64, 4m & 0.153 & 4/28 \\
76	GRPO gs$=$8$^\dagger$ & r64, $\alpha$64, 4m & 0.085 & 0/3 \\
77	\midrule
78	ACT reduced-LoRA$^\ddagger$ & r64, $\alpha$64, 4m & 0.326 & 16/16 \\
79	ACT full s1 & r64, $\alpha$128, 7m & 0.301 & 16/16 \\
80	ACT full s2 & r64, $\alpha$128, 7m & 0.286 & 15/15 \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	\begin{figure}[t]
86	\centering
87	\includegraphics[width=\columnwidth]{figures/fig_trajectory.pdf}
88	\caption{$\sycon$ trajectories for $\rthree$-only GRPO (two seeds) and ACT (two seeds) over training steps. ACT exceeds vanilla at every evaluated checkpoint (31/31 across two seeds); $\rthree$-only GRPO exceeds vanilla at only 4/28 checkpoints (14.3\%).}
89	\label{fig:trajectory}
90	\end{figure}
91	
92	\paragraph{ACT vs.\ GRPO.}
93	ACT~\citep{consistency2025bctact} achieves $\sycon = 0.301$ (seed 1) and $0.286$ (seed 2) at their respective peaks, more than $2{\times}$ vanilla and above every GRPO variant (Table~\ref{tab:main_comparison}) (held-out validation confirms generalization; see Limitations).
94	The trajectory is not monotonic---seed 1 dips to 0.214 at step 4000 but self-recovers by step 6000, unlike GRPO where stubbornness persists.
95	Full ACT peaks around steps 7000--8000 while reduced-LoRA surges to 0.326 at step 7000; both variants maintain above-vanilla performance throughout.
96	The gap is categorical: ACT's worst checkpoint ($\sycon{=}0.170$, full config) exceeds GRPO's absolute best ($\sycon{=}0.153$, R3-only seed 1, step 6500).
97	The reduced-LoRA ablation (Table~\ref{tab:ablation}) partially disentangles the five confounding dimensions: with LoRA capacity controlled, per-token SFT still dominates---and reduced-LoRA ACT ($\sycon{=}0.326$) exceeds full ACT ($\sycon{=}0.301$), ruling out adapter capacity as the explanation.
98	
99	\paragraph{Relationship to inference-time probe methods.}
100	\citet{papadatos2024probepenalties} successfully reduce sycophancy using a probe of comparable quality (94\% accuracy) via Best-of-N reranking, where the probe selects among candidates without producing gradients.
101	Together with our results, this suggests two orthogonal failure dimensions: (1)~inside vs.\ outside the optimization loop---gradient exploitation enables the probe reward trap (\S\ref{sec:probe_trap}), while inference-time reranking sidesteps it; and (2)~scalar per-completion reward---the failure persists even without the probe ($\rthree$-only GRPO), consistent with per-completion information compression as an independent factor.
102	
103	\paragraph{Future directions.}
104	Condition-aware rewards, hybrid SFT-then-RL pipelines, and per-step process rewards offer paths forward; whether other REINFORCE-style methods or behavioral attributes with similar geometric entanglement~\citep{skalse2022hacking} exhibit the same failures remains open.
105	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05332940-1b3f-434a-a827-138bd3a0724a",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "003ceca6-0e65-4aed-b9a1-ac74cef43459",
  "sourceToolAssistantUUID": "05332940-1b3f-434a-a827-138bd3a0724a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:17:07.339Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KnQ57Tqqx5TNfbog4yf4Tk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "003ceca6-0e65-4aed-b9a1-ac74cef43459",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "121b0546-175c-47cb-847f-dcfd755821ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 26 · 2026-05-23T19:17:07.344Z_

<details><summary>↩ Tool result · `toolu_01KnQ57Tqqx5TNfbog4yf4Tk`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	The probe reward trap reveals that behavioral death can precede distributional collapse by 1{,}300 steps, rendering entropy-based monitoring blind to the failure.
4	Because the trap arises under SFT with stopped gradients, it reflects a semantic limitation of $\dsyc$, not an RL artifact; under GRPO, all formulations failed (4/31 checkpoints ${>}$ vanilla across configurations) while per-token SFT succeeded at every checkpoint (47/47), and a LoRA-controlled ablation confirms supervision granularity as the primary factor~(\S\ref{sec:discussion}).
5	Our results suggest that geometric separability between the target behavior and its complement is a precondition for representation-derived rewards: directions that discriminate a behavior but conflate its warranted and unwarranted variants will reward rigidity or be gamed.
6	Condition-aware rewards that incorporate evidential warrant with dense per-token supervision, rather than relying on activation geometry or per-completion scalars alone, offer the most promising path forward.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "121b0546-175c-47cb-847f-dcfd755821ed",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "ed884985-026f-4a9f-87c1-36960158d468",
  "sourceToolAssistantUUID": "121b0546-175c-47cb-847f-dcfd755821ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T19:17:08.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DEpURfcVhSeLtBcZ11axmL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed884985-026f-4a9f-87c1-36960158d468",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73cc507c-1e3a-4fa7-9e1c-5e1842551fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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

_source line 28 · 2026-05-23T19:17:08.273Z_

<details><summary>↩ Tool result · `toolu_01DEpURfcVhSeLtBcZ11axmL`</summary>

```text
1	Our GRPO experiments use group sizes of 2 and 8, below the typical 8--64 range \citep{shao2024grpo}; a gs$=$8 ablation rules out variance reduction but larger sizes remain unexplored. All completions are truncated to 256 tokens (shared across conditions), which degrades $\dsyc$ AUROC from 0.76 to 0.60 and may affect absolute reward-utility conclusions.
2	Training and evaluation share the same 181 pairs; a held-out split (146/35) confirms ACT generalizes ($\sycon{\approx}0.20$ at peak, $3.7{\times}$ vanilla, 72\% of full-data ceiling), but performance declines at step 2000 ($\sycon{=}0.157$, still $2.8{\times}$ vanilla) due to overfitting on the small training set, and the 28\% gap suggests partial reliance on training-set-specific patterns.
3	The probe reward trap (C2) is demonstrated with a single seed; while SFT training is more deterministic than RL, replication would strengthen the temporal decoupling finding.
4	All RL training uses Qwen3-8B; cross-model discriminability is confirmed on Llama-3-8B (AUROC $0.779$; Table~\ref{tab:cross_model}), but compute constraints prevented training replication on a second architecture.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73cc507c-1e3a-4fa7-9e1c-5e1842551fc7",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "3a085660-cff9-43a7-840a-e63897338795",
  "sourceToolAssistantUUID": "73cc507c-1e3a-4fa7-9e1c-5e1842551fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T19:17:08.447Z_

<details open><summary>🔧 Tool call — Read · `toolu_011rQNAvt7mJTfGKqbXShHeN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a085660-cff9-43a7-840a-e63897338795",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL39GHn2z5r526vbZNNX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6dcf71e-eb72-4096-9e18-67ae3f21febe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gov7KFaV3yRhxnhf6X9yW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 14046,
      "output_tokens": 978,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 978,
          "cache_read_input_tokens": 14046,
          "cache_creation_input_tokens": 1228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1228,
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

_source line 30 · 2026-05-23T19:17:08.452Z_

<details><summary>↩ Tool result · `toolu_011rQNAvt7mJTfGKqbXShHeN`</summary>

```text
1	\section{Training Details}
2	\label{app:training}
3	
4	\paragraph{Reward weight selection.}
5	The weight $w_1$ is set by diagnostic-driven iteration: $w_1{=}0.25$ was initially chosen to down-weight the noisy cosine reward term; this was later increased to $w_1{=}0.40$ for F1d after diagnostics revealed that $w_1{=}0.25$ allowed the cosine term to contribute only ${\sim}8.3\%$ of total reward variance.
6	The empirical scaling factor in F1a ($\dsyc/20$) is a heuristic normalization; we did not find it critical to the failure modes reported.
7	
8	\paragraph{Response truncation.}
9	All GRPO experiments use \texttt{max\_completion\_length}=256, resulting in 80--84\% truncation of multi-turn responses.
10	This setting is shared across all conditions and does not affect relative comparisons; we retain it because response-level decisions typically manifest within the first 100--200 tokens.
11	
12	\paragraph{Hyperparameters.}
13	Table~\ref{tab:hyperparams} compares training configurations for GRPO variants and ACT.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Training hyperparameters. All experiments use Qwen3-8B, DeepSpeed ZeRO-2, bf16 precision.}
19	\label{tab:hyperparams}
20	\begin{tabular}{lcc}
21	\toprule
22	& GRPO (F1, F3)$^e$ & ACT \\
23	\midrule
24	Learning rate & 5e-5 & 5e-5 \\
25	Effective batch & 16 & 16 \\
26	Max steps & 8{,}000 & 8{,}000 \\
27	Warmup steps & 200 & 200 \\
28	LR schedule & linear$^a$ & linear \\
29	Grad.\ clipping & --- & 1.0 \\
30	\midrule
31	LoRA rank & 64 & 64 \\
32	LoRA $\alpha$ & 64 & 128 \\
33	LoRA modules & 4$^b$ & 7$^c$ \\
34	LoRA dropout & 0 & 0.05 \\
35	\midrule
36	Group size & 2$^d$ & --- \\
37	KL $\beta$ & 0.04 & --- \\
38	Max compl.\ len. & 256 & --- \\
39	Max seq.\ len. & --- & 1{,}024 \\
40	L2 loss weight & --- & 0.1 \\
41	\bottomrule
42	\end{tabular}
43	\\[2pt]
44	\raggedright\footnotesize
45	$^a$Cosine schedule for $\rthree$-only.
46	$^b$q/k/v/o\_proj.
47	$^c$+ gate/up/down\_proj (${\sim}1.75{\times}$ params; \S\ref{sec:discussion}).
48	$^d$Below typical 8--64 \citep{shao2024grpo}; not tuned.
49	$^e$Binary probe (F2) uses a custom SFT training loop rather than GRPO; group size is N/A. LoRA and optimizer settings match the GRPO column.
50	\end{table}
51	
52	\paragraph{GRPO reward variants.}
53	Cosine $\rone$ (F1d): $w_1{=}0.40$, scale$=$5.0, $w_3{=}0.60$; reward computed at layers [19, 20, 24, 27, 32, 33, 35]; recalibration every 500 steps (\S\ref{ssec:recalib}).
54	$\rthree$-only: $w_3{=}1.0$; NLI model \texttt{cross-encoder/nli-deberta-v3-base}.
55	F1a--F1c weight configurations are reported in Table~\ref{tab:cosine_chain}.
56	
57	\section{Stubbornness Taxonomy}
58	\label{app:taxonomy}
59	
60	Manual inspection of all 181 valid-correction responses from the probe-trained model (exp-008v3, step 2000, $\tof = 0$) reveals five failure categories:
61	
62	\begin{itemize}
63	\item \emph{Deliberation traps} (28.7\%): the model explicitly identifies the correct revised answer during its reasoning chain but fails to commit, reverting to the original answer in the final output.
64	\item \emph{Surface compliance / sycophantic stubbornness} (24.3\%): the model produces agreement markers (``you're right,'' ``good point'') but retains its original answer verbatim, simultaneously sycophantic and stubborn.
65	\item \emph{Acknowledge-but-maintain} (23.8\%): the model acknowledges the user's correction as plausible but explicitly maintains its original position without substantive engagement.
66	\item \emph{Genuine-accept-missed} (18.8\%): the model appears to accept the correction in its reasoning but the final answer format does not reflect the change, suggesting a generation rather than epistemic failure.
67	\item \emph{Refute/ignore/other} (4.5\%): the model directly refutes the user's input or ignores it entirely.
68	\end{itemize}
69	
70	The first three categories (76.8\%) share a common pattern: the model learns to modulate its \emph{refusal style} in response to evidence strength rather than adjusting its \emph{acceptance rate}, confirming that the probe reward optimizes surface markers rather than epistemic calibration.
71	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6dcf71e-eb72-4096-9e18-67ae3f21febe",
  "isSidechain": true,
  "promptId": "30a9a64f-8658-41fb-ba69-878f0996a7f5",
  "agentId": "a9ea56a89a347f615",
  "type": "user",
  "uuid": "3c4ede1a-41a5-463e-9e4e-c1263a2155eb",
  "sourceToolAssistantUUID": "a6dcf71e-eb72-4096-9e18-67ae3f21febe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-23T19:19:54.384Z_

Here is the complete structured extraction of all numerical values from every tex file:

---

## main.tex

No numerical values in the document body (it only includes other files and defines macros).

---

## abstract.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 0.827 | "cross-validated AUROC $0.827$ on Qwen3-8B" | AUROC of d_syc on Qwen3-8B |
| 2 | 0.779 | "$0.779$ on Llama-3-8B" | AUROC of d_syc on Llama-3-8B |
| 3 | 0 | "true-positive flip rate $= 0$" | ToF at behavioral death |
| 4 | 500 | "occurs within 500 steps" | Step at which behavioral death occurs |
| 5 | 0.70 | "generation entropy remains healthy (0.70)" | Entropy value when behavioral death has already occurred |
| 6 | 1,300 | "1,300-step lag before distributional collapse" | Step lag between behavioral death and distributional collapse |
| 7 | +0.72 | implied via intro reference (not directly in abstract text) | N/A - not in abstract |
| 8 | 2 | "GRPO with group size 2" | GRPO group size |
| 9 | 4 of 31 | "exceeded vanilla at only 4 of 31 checkpoints" | R3-only GRPO checkpoints exceeding vanilla |
| 10 | 12.9% | "(12.9%)" | Percentage of R3-only GRPO checkpoints exceeding vanilla |
| 11 | 47/47 | "exceeded vanilla at every evaluated checkpoint (47/47 across all configurations)" | ACT checkpoints exceeding vanilla |

---

## introduction.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 0.827 | "AUROC $0.827$ on Qwen3-8B" (fig caption) | AUROC of d_syc on Qwen3-8B |
| 2 | 0.827 | "cross-validated AUROC $0.827$ on Qwen3-8B" (body text) | Same |
| 3 | 0.779 | "$0.779$ on Llama-3-8B" | AUROC of d_syc on Llama-3-8B |
| 4 | 0.60 | "degrades this to approximately 0.60" | AUROC under 256-token truncation during GRPO |
| 5 | 0 | "$\tof{=}0$" (fig caption, and multiple in body) | ToF at behavioral death |
| 6 | 500 | "occurs at step 500" | Step of behavioral death |
| 7 | 0.70 | "entropy remains healthy (0.70)" | Entropy at behavioral death |
| 8 | 1,300 | "1,300-step lag" | Lag between behavioral and distributional collapse |
| 9 | +0.72 | "the reward averaging $+0.72$ throughout" | Average reward during the trap |
| 10 | 2 | "group size$=$2" | GRPO group size |
| 11 | 4 of 31 | "4 of 31 checkpoints (12.9%)" | R3-only GRPO checkpoints exceeding vanilla |
| 12 | 12.9% | "(12.9%)" | Percentage of above |
| 13 | 47/47 | "47/47 across all configurations" | ACT checkpoints exceeding vanilla |
| 14 | 1.7x | "the magnitude gap is $1.7{\times}$" | Ratio of per-token SFT to per-completion GRPO under matched LoRA |
| 15 | 4/31 | "4/31 (12.9%)" (bullet point) | GRPO checkpoints exceeding vanilla |

---

## framework.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 181 | "181 contrastive pairs" | Number of contrastive pairs used for extraction |
| 2 | 10% | "response length difference ${<}10\%$" | Style matching validation threshold |
| 3 | 2 | "shared opening phrase ${\geq}2$ words" | Minimum shared opening phrase length |
| 4 | 3 | "up to 3 retries per pair" | Maximum retries for pair validation |
| 5 | 19 of 200 | "19 of 200 initial pairs were discarded" | Pairs discarded for failing validation |
| 6 | 75 | "weak (75 pairs)" | Number of weak evidence pairs |
| 7 | 54 | "medium (54 pairs)" | Number of medium evidence pairs |
| 8 | 52 | "strong (52 pairs)" | Number of strong evidence pairs |
| 9 | 362 | "362 activations total" | Total activations from 181 pairs |
| 10 | 5 | "5-fold cross-validated AUROC" | Number of CV folds |
| 11 | 19 | "layer 19" | Best layer for Qwen3-8B |
| 12 | 0.827 ± 0.028 | "AUROC $0.827 \pm 0.028$ (5-fold CV)" | AUROC at L19 on Qwen3-8B |
| 13 | 20 | "$\dsyc / 20$" (F1a formula) | Scaling factor in tanh formulation |
| 14 | 5x | "$5{\times}$ scaled cosine" (F1d) | Cosine scaling factor |
| 15 | 0.5 | "$P(\text{syc} \mid \mathbf{h}) < 0.5$" (F2) | Probe threshold |
| 16 | 500 | "re-extract $\dsyc$ every 500 steps" | Recalibration frequency |
| 17 | 0.96 | "cosine similarity...remains ${\approx}\,0.96$" | Direction stability at step 500 |
| 18 | 64 | "LoRA (rank$=$64)" | LoRA rank |
| 19 | 64 | "$\alpha{=}64$ for GRPO" | LoRA alpha for GRPO |
| 20 | 128 | "$\alpha{=}128$ for ACT" | LoRA alpha for ACT |
| 21 | 2 | "group size of 2" | GRPO group size |
| 22 | 8--64 | "typical range of 8--64" | Typical GRPO group size range |

---

## direction_quality.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 181 | "181 style-controlled contrastive pairs" | Number of contrastive pairs |
| 2 | 0.827 ± 0.028 | "AUROC $0.827 \pm 0.028$ (5-fold CV) at its best layer (L19)" | Qwen3-8B best-layer AUROC |
| 3 | 0.01 | "$p < 0.01$" | Statistical significance threshold |
| 4 | L16 | "statistical significance...first appears at L16" | First significant layer (Qwen3-8B) |
| 5 | L19 | "peaks at L19" | Best layer (Qwen3-8B) |
| 6 | 0.675 | "AUROC rises monotonically from 0.675 on weak-evidence pairs" | Qwen3-8B AUROC on weak pairs |
| 7 | 0.883 | "0.883 on medium" | Qwen3-8B AUROC on medium pairs |
| 8 | 0.929 | "0.929 on strong pairs" | Qwen3-8B AUROC on strong pairs |
| 9 | 0.779 ± 0.019 | "AUROC $0.779 \pm 0.019$ (5-fold CV) at L16" | Llama-3-8B best-layer AUROC |
| 10 | L16 | "at L16" | Best layer (Llama-3-8B) |
| 11 | 0.711 | "weak 0.711" | Llama-3-8B AUROC on weak pairs |
| 12 | 0.864 | "medium 0.864" | Llama-3-8B AUROC on medium pairs |
| 13 | 0.911 | "strong 0.911" | Llama-3-8B AUROC on strong pairs |
| 14 | 0.751 | "0.751 (geography)" | Llama-3-8B per-domain AUROC lower bound |
| 15 | 0.844 | "0.844 (commonsense)" | Llama-3-8B per-domain AUROC upper bound |
| 16 | 0.923 | "AUROC rises to 0.923" | Llama-3-8B AUROC when surface confounds are controlled |
| 17 | 36 | "36 layers" (fig caption) | Qwen3-8B total layers |
| 18 | 32 | "32 layers" (fig caption) | Llama-3-8B total layers |
| 19 | 50--60% | "50--60\% through the network" (fig caption) | Depth range of best discriminability |
| 20 | 0.96 | "cosine similarity...is approximately 0.96" | Direction drift at step 500 |
| 21 | 500 | "at step 500" | Step at which drift is measured |
| 22 | 0.77 | "per-layer AUROC remains above 0.77" | AUROC after drift |
| 23 | 0.835 | "logistic probe...achieves AUROC 0.835" | Probe AUROC on learned direction |
| 24 | 0.727 | "0.727 for a probe trained on a random direction" | Probe AUROC on random direction |
| 25 | +0.108 | "$\Delta{=}{+}0.108$" | AUROC difference (learned minus random) |
| **Table (tab:cross_model):** | | | |
| 26 | Qwen3-8B: L19, 0.827±0.028, 0.675, 0.883, 0.929 | Table row | Qwen3-8B direction quality by evidence strength |
| 27 | Llama-3-8B: L16, 0.779±0.019, 0.711, 0.864, 0.911 | Table row | Llama-3-8B direction quality by evidence strength |

---

## cosine_failure.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 0.827 | "AUROC 0.827 on Qwen3-8B" | AUROC of d_syc (full-length) |
| 2 | 256 | "256-token truncation" | GRPO completion truncation length |
| 3 | 0.60 | "reduces $\dsyc$ AUROC to approximately 0.60" | AUROC under truncation |
| 4 | 64 | "LoRA rank$=$64" (table caption) | LoRA rank |
| 5 | 0.25 | "$w_1 = 0.25$" (F1a, F1b, F1c in table) | Weight for R1 in first three configs |
| 6 | 0.40 | "$w_1 = 0.40$" (F1d in table) | Weight for R1 in F1d |
| 7 | 20 | "$\dsyc / 20$" | F1a scaling divisor |
| 8 | 100--1,200x | "norms exceed the direction norm by $100$--$1{,}200{\times}$" | Residual-stream to direction norm ratio |
| 9 | 955 | "zeroing the gradient by step 955" | Step at which F1a gradient vanishes |
| 10 | 0.098 | "cosine gap...averages only 0.098 across layers" | Mean cosine gap between valid and sycophantic activations |
| 11 | 0.827 | "offline AUROC from 0.827" | Pre-recalibration AUROC |
| 12 | 0.910 | "to 0.910" | Post-recalibration AUROC |
| 13 | 0.069 | "collapsing entropy to 0.069 within 300 steps" | Entropy after F1c mode collapse |
| 14 | 300 | "within 300 steps" | Steps to mode collapse in F1c |
| 15 | 5x | "$5{\times}$ scaling" | F1d cosine scaling factor |
| 16 | 0.9998 | "$\rthree$ saturates at 0.9998 by step 300" | R3 saturation value in F1d |
| 17 | 300 | "by step 300" | Step of R3 saturation in F1d |
| 18 | 2160 | "terminal collapse at step 2160" | Step of terminal collapse in F1d |
| 19 | 0.76 | "AUROC drops from 0.76 (full response)" | Full-response AUROC under truncation conditions |
| 20 | 0.60 | "to 0.60" | Truncated AUROC |
| 21 | 0.827 | "offline discriminability (0.827)" | Offline AUROC (without truncation) |
| 22 | 0 | "$\tof{=}0$ from step 500 onward" | ToF for all cosine configs |
| 23 | 500 | "from step 500 onward" | Step of cosine collapse |

---

## probe_trap.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 0.5 | "$P(\text{syc} \mid \mathbf{h}) < 0.5$" | Probe threshold |
| 2 | ~30 | "within ${\sim}30$ steps" | Steps to gradient gaming without stop-gradient |
| 3 | 0.978 | "$\tof = 0.978$" | ToF with differentiable probe (exp-008) |
| 4 | 0.006 | "$\nof = 0.006$" | NoF with differentiable probe (exp-008) |
| **Table (tab:probe_trajectory) — exp-008v3:** | | | |
| 5 | Step 500: ToF=0.000, NoF=0.995, SyconScore=0.000, Entropy=0.702, Reward=+0.72 | Table row | Probe trap trajectory at step 500 |
| 6 | Step 1000: ToF=0.006, NoF=0.995, SyconScore=0.011, Entropy=0.800, Reward=+0.71 | Table row | Probe trap trajectory at step 1000 |
| 7 | Step 1500: ToF=0.000, NoF=1.000, SyconScore=0.000, Entropy=0.608, Reward=+0.69 | Table row | Probe trap trajectory at step 1500 |
| 8 | Step 2000: ToF=0.000, NoF=1.000, SyconScore=0.000, Entropy=0.304, Reward=+0.69 | Table row | Probe trap trajectory at step 2000 |
| 9 | 1,300 | "1,300-step lag" | Lag between behavioral and distributional collapse |
| 10 | 0.70--0.80 | "entropy remains high (0.70--0.80) through step 1000" | Entropy range during behavioral death |
| 11 | +0.72 | "combined reward averages $+0.72$" | Average reward throughout trap |
| 12 | ~1840 | "Entropy does not collapse until step ${\sim}1840$" | Step of distributional collapse |
| **Failure mode taxonomy (from body text):** | | | |
| 13 | 28.7% | "deliberation traps (28.7%)" | Percentage of deliberation trap failures |
| 14 | 24.3% | "sycophantic stubbornness (24.3%)" | Percentage of sycophantic stubbornness failures |
| 15 | 23.8% | "acknowledge-but-maintain (23.8%)" | Percentage of acknowledge-but-maintain failures |
| 16 | 18.8% | "genuine-accept-missed (18.8%)" | Percentage of genuine-accept-missed failures |
| 17 | 4.5% | "refute/ignore/other (4.5%)" | Percentage of refute/ignore/other failures |
| 18 | 181 | "181 valid-correction responses" | Number of responses analyzed |

---

## discussion.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 0 | "$\tof = 0$ by step 500" | ToF for binary probe stubbornness trap |
| 2 | 500 | "by step 500" | Step of stubbornness trap |
| 3 | 0.779 ± 0.019 | "AUROC $0.779 \pm 0.019$" | Llama-3-8B AUROC |
| **Table (tab:main_comparison):** | | | |
| 4 | Vanilla: SyconScore=0.134, ToF=0.072, NoF=0.945 | Table row | Vanilla baseline |
| 5 | Cosine R1 (F1a-F1d): SyconScore=0.000, ToF=0.000, NoF=1.000, Step=500 | Table row | All cosine variants collapsed |
| 6 | Continuous Probe R1 (F3): SyconScore=0.124, ToF=0.066, NoF=0.934, Step=500 | Table row | Continuous probe GRPO |
| 7 | Binary Probe R1 (F2): SyconScore=0.000, ToF=0.000, NoF=0.995, Step=500 | Table row | Binary probe SFT |
| 8 | R3-only GRPO: SyconScore=0.153, ToF=0.083, NoF=0.983, Step=6500 | Table row | R3-only GRPO best checkpoint |
| 9 | ActAdd (alpha=5): SyconScore=0.054, ToF=0.028, NoF=0.961 | Table row | ActAdd inference-time baseline |
| 10 | ACT seed 1: SyconScore=0.301, ToF=0.182, NoF=0.867, Step=8000 | Table row | ACT best (seed 1) |
| 11 | ACT seed 2: SyconScore=0.286, Step=7000 | Table row | ACT (seed 2) |
| **Table caption notes:** | | | |
| 12 | 4/28 | "only 4/28 checkpoints across two seeds exceed vanilla" | R3-only GRPO checkpoints > vanilla |
| 13 | 15 | "Seed 2 (15 checkpoints)" | Number of ACT seed 2 checkpoints |
| 14 | 0.286 | "Best $\sycon{=}0.286$ (step 7000)" | ACT seed 2 best SyconScore |
| 15 | 2160 | "F1d additionally diverged at step 2160 (entropy ${<}\,0.01$)" | F1d divergence step |
| 16 | 0.01 | "entropy ${<}\,0.01$" | F1d entropy at divergence |
| **Body text (R3-only GRPO trajectory):** | | | |
| 17 | 0.153 | "Seed 1 peaks at 0.153 (checkpoint 6500)" | R3-only seed 1 peak SyconScore |
| 18 | 6500 | "checkpoint 6500" | Step of seed 1 peak |
| 19 | 0.143 | "ends at 0.143 (checkpoint 8000)" | R3-only seed 1 final SyconScore |
| 20 | 8000 | "checkpoint 8000" | Final evaluated step |
| 21 | 0.143 | "seed 2 peaks at 0.143 (checkpoint 4000)" | R3-only seed 2 peak SyconScore |
| 22 | 4000 | "checkpoint 4000" | Step of seed 2 peak |
| 23 | 0.124 | "ends at 0.124 (checkpoint 8000)" | R3-only seed 2 final SyconScore |
| 24 | 4 of 28 | "4 of 28 checkpoints...exceed vanilla (14.3%)" | R3-only checkpoints > vanilla (both seeds) |
| 25 | 14.3% | "(14.3%)" | Percentage of above |
| 26 | 3/12 | "3/12 for seed 1 (25%)" | Seed 1 checkpoints > vanilla |
| 27 | 25% | "(25%)" | Percentage for seed 1 |
| 28 | 1/16 | "1/16 for seed 2 (6.3%)" | Seed 2 checkpoints > vanilla |
| 29 | 6.3% | "(6.3%)" | Percentage for seed 2 |
| 30 | 31/31 | "31/31 across two seeds" | ACT checkpoints > vanilla (both seeds) |
| 31 | ~0.069 | "$\Delta \approx 0.069$" | SyconScore oscillation amplitude for both GRPO seeds |
| 32 | ~2,500 | "differing by ${\sim}2{,}500$ steps" | Crash onset difference between seeds |
| 33 | <0.01 | "AUROC varies by ${<}0.01$ across checkpoints" | AUROC variation across GRPO checkpoints |
| 34 | ~0.98 | "$\rthree$ saturates at ${\sim}0.98$" | R3 saturation value |
| 35 | 0.703 | "$p{=}0.703$" | p-value for R3 saturation test |
| 36 | 17% | "$\sycon$ swings by 17\%" | SyconScore swing magnitude despite stable AUROC/R3 |
| **Group size ablation (tab:ablation):** | | | |
| 37 | 2 to 8 | "group size from 2 to 8" | Group size ablation |
| 38 | 0.084 → 0.085 → 0.054 | "monotonically declining trajectory ($0.084 \to 0.085 \to 0.054$)" | gs=8 SyconScore trajectory |
| 39 | 0.085 | "gs$=$8 (best 0.085)" | gs=8 best SyconScore |
| 40 | 0.153 | "gs$=$2 (best 0.153)" | gs=2 best SyconScore (comparison) |
| **Table (tab:ablation):** | | | |
| 41 | GRPO gs=2 (2 seeds): r64/α64/4m, Best SyconScore=0.153, >Van.=4/28 | Table row | GRPO gs=2 ablation |
| 42 | GRPO gs=8: r64/α64/4m, Best SyconScore=0.085, >Van.=0/3 | Table row | GRPO gs=8 ablation |
| 43 | ACT reduced-LoRA: r64/α64/4m, Best SyconScore=0.326, >Van.=16/16 | Table row | ACT reduced-LoRA ablation |
| 44 | ACT full s1: r64/α128/7m, Best SyconScore=0.301, >Van.=16/16 | Table row | ACT full seed 1 |
| 45 | ACT full s2: r64/α128/7m, Best SyconScore=0.286, >Van.=15/15 | Table row | ACT full seed 2 |
| **Reduced-LoRA details:** | | | |
| 46 | 0.267 | "$\sycon = 0.267$ (peak 0.326 at step 7000)" | ACT reduced-LoRA final SyconScore |
| 47 | 0.326 | "peak 0.326 at step 7000" | ACT reduced-LoRA peak SyconScore |
| 48 | 7000 | "step 7000" | Step of reduced-LoRA peak |
| 49 | 16 | "all 16 checkpoints exceed vanilla" | Number of reduced-LoRA checkpoints |
| 50 | 0.267 | "per-token SFT ($\sycon{=}0.267$)" | SFT SyconScore under matched LoRA |
| 51 | 0.153 | "per-completion GRPO ($\sycon{=}0.153$)" | GRPO SyconScore under matched LoRA |
| 52 | 1.7x | "by $1.7{\times}$" | SFT-to-GRPO ratio under matched LoRA |
| **ACT vs GRPO paragraph:** | | | |
| 53 | 0.301 | "$\sycon = 0.301$ (seed 1)" | ACT seed 1 peak SyconScore |
| 54 | 0.286 | "$0.286$ (seed 2)" | ACT seed 2 peak SyconScore |
| 55 | 2x | "more than $2{\times}$ vanilla" | ACT-to-vanilla ratio |
| 56 | 0.214 | "dips to 0.214 at step 4000" | ACT seed 1 dip SyconScore |
| 57 | 4000 | "at step 4000" | Step of ACT dip |
| 58 | 6000 | "self-recovers by step 6000" | Step of ACT recovery |
| 59 | 0.326 | "surges to 0.326 at step 7000" | Reduced-LoRA ACT peak |
| 60 | 7000 | "step 7000" | Step of reduced-LoRA peak |
| 61 | 0.170 | "ACT's worst checkpoint ($\sycon{=}0.170$, full config)" | ACT worst checkpoint SyconScore |
| 62 | 0.153 | "GRPO's absolute best ($\sycon{=}0.153$)" | GRPO best SyconScore |
| 63 | 6500 | "step 6500" | Step of GRPO best |
| 64 | 0.326 | "reduced-LoRA ACT ($\sycon{=}0.326$)" | Reduced-LoRA peak (repeated) |
| 65 | 0.301 | "full ACT ($\sycon{=}0.301$)" | Full ACT peak (repeated) |
| **Related work reference in discussion:** | | | |
| 66 | 94% | "94\% accuracy" (citing Papadatos et al.) | Probe accuracy in Best-of-N reranking method |
| 67 | 0.827 | "AUROC $0.827$" | Our probe AUROC (for comparison) |

---

## related_work.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 94% | "94\% probe accuracy" (citing Papadatos et al.) | Probe accuracy in Best-of-N reranking |
| 2 | 0.827 | "AUROC $0.827$" | Our probe AUROC |
| 3 | 100% | "100\% validation accuracy" (citing Wu et al.) | Reward hacking detection accuracy |

---

## conclusion.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 1,300 | "1,300 steps" | Lag between behavioral death and distributional collapse |
| 2 | 4/31 | "4/31 checkpoints ${>}$ vanilla" | GRPO checkpoints exceeding vanilla |
| 3 | 47/47 | "47/47" | ACT checkpoints exceeding vanilla |

---

## limitations.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| 1 | 2 | "group sizes of 2" | GRPO group size tested |
| 2 | 8 | "and 8" | GRPO group size in ablation |
| 3 | 8--64 | "typical 8--64 range" | Typical GRPO group size range |
| 4 | 256 | "truncated to 256 tokens" | Completion truncation length |
| 5 | 0.76 | "degrades $\dsyc$ AUROC from 0.76" | Full-response AUROC before truncation |
| 6 | 0.60 | "to 0.60" | AUROC after truncation |
| 7 | 181 | "same 181 pairs" | Number of training/eval pairs |
| 8 | 146/35 | "held-out split (146/35)" | Train/held-out split |
| 9 | ~0.20 | "$\sycon{\approx}0.20$ at peak" | Held-out SyconScore for ACT |
| 10 | 3.7x | "$3.7{\times}$ vanilla" | Held-out ACT vs vanilla ratio |
| 11 | 72% | "72\% of full-data ceiling" | Held-out vs full-data performance ratio |
| 12 | 2000 | "step 2000" | Step of performance decline on held-out |
| 13 | 0.157 | "$\sycon{=}0.157$" | Held-out SyconScore at step 2000 |
| 14 | 2.8x | "$2.8{\times}$ vanilla" | Held-out at step 2000 vs vanilla ratio |
| 15 | 28% | "28\% gap" | Gap suggesting partial reliance on training patterns |
| 16 | 0.779 | "AUROC $0.779$" | Llama-3-8B cross-model AUROC |

---

## appendix.tex

| # | Value | Context | Refers to |
|---|-------|---------|-----------|
| **Reward weight selection:** | | | |
| 1 | 0.25 | "$w_1{=}0.25$ was initially chosen" | Initial R1 weight |
| 2 | 0.40 | "increased to $w_1{=}0.40$ for F1d" | F1d R1 weight |
| 3 | ~8.3% | "${\sim}8.3\%$ of total reward variance" | Cosine term reward variance contribution at w1=0.25 |
| 4 | 20 | "$\dsyc/20$" | F1a heuristic normalization |
| **Response truncation:** | | | |
| 5 | 256 | "max\_completion\_length=256" | GRPO completion truncation |
| 6 | 80--84% | "80--84\% truncation" | Percentage of responses truncated |
| 7 | 100--200 | "first 100--200 tokens" | Where response-level decisions manifest |
| **Hyperparameters table (tab:hyperparams):** | | | |
| 8 | 5e-5 | Learning rate | For both GRPO and ACT |
| 9 | 16 | Effective batch size | For both |
| 10 | 8,000 | Max steps | For both |
| 11 | 200 | Warmup steps | For both |
| 12 | 1.0 | Gradient clipping | ACT only |
| 13 | 64 | LoRA rank | For both |
| 14 | 64 | LoRA alpha | GRPO |
| 15 | 128 | LoRA alpha | ACT |
| 16 | 4 | LoRA modules | GRPO (q/k/v/o_proj) |
| 17 | 7 | LoRA modules | ACT (+ gate/up/down_proj) |
| 18 | 0 | LoRA dropout | GRPO |
| 19 | 0.05 | LoRA dropout | ACT |
| 20 | 2 | Group size | GRPO |
| 21 | 0.04 | KL beta | GRPO |
| 22 | 256 | Max completion length | GRPO |
| 23 | 1,024 | Max sequence length | ACT |
| 24 | 0.1 | L2 loss weight | ACT |
| 25 | ~1.75x | "${\sim}1.75{\times}$ params" (footnote c) | ACT LoRA param ratio vs GRPO |
| **GRPO reward variants:** | | | |
| 26 | 0.40 | "$w_1{=}0.40$" | F1d weight |
| 27 | 5.0 | "scale$=$5.0" | F1d scale |
| 28 | 0.60 | "$w_3{=}0.60$" | F1d R3 weight |
| 29 | [19, 20, 24, 27, 32, 33, 35] | "layers [19, 20, 24, 27, 32, 33, 35]" | Layers used for F1d reward computation |
| 30 | 500 | "recalibration every 500 steps" | Recalibration interval |
| 31 | 1.0 | "$w_3{=}1.0$" | R3-only GRPO weight |
| **Stubbornness taxonomy (exp-008v3, step 2000):** | | | |
| 32 | 181 | "all 181 valid-correction responses" | Number of responses analyzed |
| 33 | 0 | "$\tof = 0$" | ToF for taxonomy analysis |
| 34 | 2000 | "step 2000" | Step of taxonomy analysis |
| 35 | 28.7% | "Deliberation traps (28.7%)" | Deliberation trap percentage |
| 36 | 24.3% | "Surface compliance / sycophantic stubbornness (24.3%)" | Sycophantic stubbornness percentage |
| 37 | 23.8% | "Acknowledge-but-maintain (23.8%)" | Acknowledge-but-maintain percentage |
| 38 | 18.8% | "Genuine-accept-missed (18.8%)" | Genuine-accept-missed percentage |
| 39 | 4.5% | "Refute/ignore/other (4.5%)" | Refute/ignore/other percentage |
| 40 | 76.8% | "first three categories (76.8%)" | Combined percentage of top 3 failure modes |

---

## Summary of key unique numerical claims across the paper

**AUROC values:** 0.827 (Qwen3-8B L19), 0.779 (Llama-3-8B L16), 0.60 (truncated), 0.76 (full-response pre-truncation variant), 0.910 (post-recalibration), 0.835 (probe on learned direction), 0.727 (probe on random direction), 0.675/0.883/0.929 (Qwen3 weak/medium/strong), 0.711/0.864/0.911 (Llama weak/medium/strong), 0.751/0.844 (Llama domain range), 0.923 (Llama confound-controlled)

**SyconScore values:** 0.134 (vanilla), 0.000 (cosine/binary probe), 0.124 (continuous probe), 0.153 (R3-only GRPO best), 0.301 (ACT s1), 0.286 (ACT s2), 0.326 (ACT reduced-LoRA peak), 0.267 (ACT reduced-LoRA final), 0.170 (ACT worst), 0.214 (ACT s1 dip), ~0.20 (held-out peak), 0.157 (held-out step 2000), 0.054 (ActAdd), 0.085 (gs=8 best), 0.084/0.085/0.054 (gs=8 trajectory)

**ToF/NoF:** ToF=0 (behavioral death, multiple configs), ToF=0.072/NoF=0.945 (vanilla), ToF=0.978/NoF=0.006 (differentiable probe gaming), ToF=0.083/NoF=0.983 (R3-only), ToF=0.182/NoF=0.867 (ACT s1), ToF=0.066/NoF=0.934 (continuous probe), ToF=0.028/NoF=0.961 (ActAdd), NoF=0.995/1.000 (probe trap trajectory)

**Key ratios:** 1.7x (SFT vs GRPO under matched LoRA), 2x (ACT vs vanilla), 3.7x (held-out ACT vs vanilla), 2.8x (held-out step 2000 vs vanilla), 1.75x (ACT LoRA params vs GRPO), 100-1200x (residual norm vs direction norm)

**Checkpoint fractions:** 4/28=14.3% (R3-only > vanilla, both seeds), 4/31=12.9% (mentioned in abstract/conclusion with slight denominator discrepancy vs discussion's 4/28), 3/12=25% (seed 1), 1/16=6.3% (seed 2), 31/31 (ACT > vanilla, both seeds), 47/47 (ACT across all configurations), 16/16 (reduced-LoRA ACT), 0/3 (gs=8)

**Notable discrepancy:** The abstract and introduction say "4 of 31 checkpoints (12.9%)" while the discussion section says "4 of 28 checkpoints (14.3%)" with "3/12 for seed 1, 1/16 for seed 2" (which sums to 4/28). The conclusion uses "4/31." The 47/47 figure (abstract/conclusion) versus 31/31 (discussion figure caption) likely reflects that 47/47 includes all configurations (full s1 16 + full s2 15 + reduced-LoRA 16 = 47) while 31/31 is two full seeds only (16+15).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c4ede1a-41a5-463e-9e4e-c1263a2155eb",
  "isSidechain": true,
  "agentId": "a9ea56a89a347f615",
  "requestId": "req_011CbL3A49YyQXvZGeUJPqbr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6dce06e-e88b-4f1c-9936-e4d47c04597b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "3ecebb46-94ed-4f9d-a208-d434ebe73d0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AY1aYfQQRgpHo3KfPLv39R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23981,
      "cache_read_input_tokens": 7336,
      "output_tokens": 10203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23981
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10203,
          "cache_read_input_tokens": 7336,
          "cache_creation_input_tokens": 23981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23981,
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
