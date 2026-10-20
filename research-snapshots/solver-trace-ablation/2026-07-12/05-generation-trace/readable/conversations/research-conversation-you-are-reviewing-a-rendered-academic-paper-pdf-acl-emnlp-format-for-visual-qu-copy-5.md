# Research conversation: You are reviewing a rendered academic paper PDF (ACL/EMNLP format) for visual quality issues. Read and visually inspect 

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aed962cf5f080c0a7.jsonl`
- **Structured JSON:** [`9f357c8a06b10615d77d.json`](../../sessions/9f/9f357c8a06b10615d77d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-15T22:58:30.901Z_

You are reviewing a rendered academic paper PDF (ACL/EMNLP format) for visual quality issues. Read and visually inspect these 3 page images:

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p17.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p18.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p19.png

For each page, check:
1. **Layout**: margins, column alignment, spacing — does it conform to ACL/EMNLP two-column format?
2. **Figures**: Are figures clear, readable, with complete legends, proper axis labels, sufficient resolution?
3. **Tables**: Alignment, number formatting consistency, clear headers
4. **Formulas**: Rendered correctly? Overflow into margins?
5. **Citations**: Any [?] or broken references? Citation format consistency (parenthetical vs textual)?
6. **Text**: Any orphan/widow lines, overfull hboxes (text extending into margins), large whitespace gaps?
7. **Page numbers**: Present and correct?

Report ALL issues you find, categorized as:
- CRITICAL: Would cause desk rejection or seriously harm readability
- WARNING: Noticeable quality issues that should be fixed
- INFO: Minor suggestions

Format your output as a structured list. Be specific about locations (page number, column, approximate position). If a page looks fine, say "PASS" for that page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4aaddbed-c449-4fd6-858a-7f3fffb155d2",
  "agentId": "aed962cf5f080c0a7",
  "type": "user",
  "uuid": "f91e0c20-2da8-461f-b08f-25355dc8c88c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T22:58:30.904Z_

```json
{
  "parentUuid": "f91e0c20-2da8-461f-b08f-25355dc8c88c",
  "isSidechain": true,
  "agentId": "aed962cf5f080c0a7",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "13431aa5-e8fb-466e-b8ba-8f772de25c71",
  "timestamp": "2026-05-15T22:58:30.904Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-15T22:58:35.858Z_



I'll read all three page images to visually inspect them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13431aa5-e8fb-466e-b8ba-8f772de25c71",
  "isSidechain": true,
  "agentId": "aed962cf5f080c0a7",
  "requestId": "req_011Cb5BZsZNCgDvFqasXsiaP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c56a0bc-09a7-4f6b-ae2b-33935a8a6339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHeRYSDfogijkgb1iiEYKt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6233,
      "cache_read_input_tokens": 9078,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6233
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 260,
          "cache_read_input_tokens": 9078,
          "cache_creation_input_tokens": 6233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6233,
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

### Tool call

_source line 4 · 2026-05-15T22:58:35.863Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QVrnw1qx2rKK9X35CGLif6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c56a0bc-09a7-4f6b-ae2b-33935a8a6339",
  "isSidechain": true,
  "agentId": "aed962cf5f080c0a7",
  "requestId": "req_011Cb5BZsZNCgDvFqasXsiaP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fbca450-506b-4eb2-ba27-cb1b28cc44d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHeRYSDfogijkgb1iiEYKt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6233,
      "cache_read_input_tokens": 9078,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6233
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 260,
          "cache_read_input_tokens": 9078,
          "cache_creation_input_tokens": 6233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6233,
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

### Tool call

_source line 5 · 2026-05-15T22:58:35.882Z_

<details open><summary>🔧 Tool call — Read · `toolu_019TFe2dT25s7aAnr2rbujXr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fbca450-506b-4eb2-ba27-cb1b28cc44d7",
  "isSidechain": true,
  "agentId": "aed962cf5f080c0a7",
  "requestId": "req_011Cb5BZsZNCgDvFqasXsiaP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7429e51-8797-4b39-8163-903f820b261f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHeRYSDfogijkgb1iiEYKt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6233,
      "cache_read_input_tokens": 9078,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6233
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 260,
          "cache_read_input_tokens": 9078,
          "cache_creation_input_tokens": 6233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6233,
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

### Tool call

_source line 6 · 2026-05-15T22:58:35.892Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ahp1nBUo1uLot9P4K3AH5g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/_pdf_images/main_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7429e51-8797-4b39-8163-903f820b261f",
  "isSidechain": true,
  "agentId": "aed962cf5f080c0a7",
  "requestId": "req_011Cb5BZsZNCgDvFqasXsiaP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edbb6398-8715-4914-af29-1536436733c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHeRYSDfogijkgb1iiEYKt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6233,
      "cache_read_input_tokens": 9078,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6233
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 260,
          "cache_read_input_tokens": 9078,
          "cache_creation_input_tokens": 6233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6233,
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

_source line 7 · 2026-05-15T22:58:45.811Z_

<details><summary>↩ Tool result · `toolu_01Ahp1nBUo1uLot9P4K3AH5g`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edbb6398-8715-4914-af29-1536436733c1",
  "isSidechain": true,
  "promptId": "4aaddbed-c449-4fd6-858a-7f3fffb155d2",
  "agentId": "aed962cf5f080c0a7",
  "type": "user",
  "uuid": "54b6ee28-da57-4687-b396-bb7a5941bbbc",
  "sourceToolAssistantUUID": "edbb6398-8715-4914-af29-1536436733c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T22:58:49.325Z_

<details><summary>↩ Tool result · `toolu_019TFe2dT25s7aAnr2rbujXr`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7429e51-8797-4b39-8163-903f820b261f",
  "isSidechain": true,
  "promptId": "4aaddbed-c449-4fd6-858a-7f3fffb155d2",
  "agentId": "aed962cf5f080c0a7",
  "type": "user",
  "uuid": "4321b53a-5ce4-4b31-a0e9-a00783f11979",
  "sourceToolAssistantUUID": "b7429e51-8797-4b39-8163-903f820b261f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T22:58:49.329Z_

<details><summary>↩ Tool result · `toolu_01QVrnw1qx2rKK9X35CGLif6`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fbca450-506b-4eb2-ba27-cb1b28cc44d7",
  "isSidechain": true,
  "promptId": "4aaddbed-c449-4fd6-858a-7f3fffb155d2",
  "agentId": "aed962cf5f080c0a7",
  "type": "user",
  "uuid": "0bf8d491-6b30-41da-849d-65f4bd4ddb7d",
  "sourceToolAssistantUUID": "3fbca450-506b-4eb2-ba27-cb1b28cc44d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-15T22:58:53.004Z_



Now let me also read the corresponding LaTeX source files for the appendix to cross-reference any issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bf8d491-6b30-41da-849d-65f4bd4ddb7d",
  "isSidechain": true,
  "agentId": "aed962cf5f080c0a7",
  "requestId": "req_011Cb5BbDwytKFGANkHQsYRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f97c646-3974-4790-b23d-9b6b38eed2b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011B7fXUygHULZEduNTi837Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3382,
      "cache_read_input_tokens": 15311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3382,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 11 · 2026-05-15T22:58:54.735Z_

<details open><summary>🔧 Tool call — Read · `toolu_014uN1qyiDzuBCGfRYoK9Zfe`</summary>

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
  "parentUuid": "8f97c646-3974-4790-b23d-9b6b38eed2b0",
  "isSidechain": true,
  "agentId": "aed962cf5f080c0a7",
  "requestId": "req_011Cb5BbDwytKFGANkHQsYRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88c97647-ddf7-4e66-90ec-8baddcf26193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011B7fXUygHULZEduNTi837Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3382,
      "cache_read_input_tokens": 15311,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3382
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 15311,
          "cache_creation_input_tokens": 3382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3382,
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

_source line 12 · 2026-05-15T22:58:55.009Z_

<details><summary>↩ Tool result · `toolu_014uN1qyiDzuBCGfRYoK9Zfe`</summary>

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
10	\begin{table}[h]
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
25	Rollouts per prompt ($K$) & 8 \\
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
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004).
55	
56	
57	\section{STA Algorithm}
58	\label{app:algorithm}
59	
60	Algorithm~\ref{alg:sta} (Section~\ref{sec:sta}) gives the procedure for computing ISR over a proved formalization.
61	For unproved samples ($S(x) \neq \textit{proved}$), ISR is undefined and the protocol is not applied.
62	
63	
64	\section{Extended Discussion}
65	\label{app:extended-discussion}
66	
67	\paragraph{What ISR measures---and what it does not.}
68	ISR quantifies syntactic component necessity: the fraction of solver-input components whose individual removal causes proof failure.
69	This is strictly weaker than semantic faithfulness---whether the formalization accurately captures the natural-language meaning.
70	We verify this empirically: Spearman $\rho(\text{ISR}, \text{NLI accuracy}) = -0.049$ ($p = 0.187$, n.s.) from a downstream NLI evaluation on exec-only checkpoint outputs.
71	ISR and downstream task performance are uncorrelated.
72	ISR is thus a structural integrity diagnostic, not a semantic quality metric: high ISR indicates that every component contributes to the proof, not that the proof faithfully represents the original reasoning problem.
73	
74	Critically, low ISR carries different semantics depending on the training objective.
75	Under exec-only training, low ISR in Prolog reflects redundant coding---repeated ground facts where removing any single copy does not affect the proof---rather than absence of reasoning (\S\ref{sec:crosslogic}).
76	Under ISR-as-reward, high ISR reflects metric gaming (\S\ref{sec:goodhart}).
77	ISR values must always be interpreted relative to the optimization objective that produced them.
78	
79	\paragraph{The premise-count confound.}
80	LOO-based metrics like ISR have an inherent mathematical bias: with fewer components, each is mechanically more likely to be necessary.
81	A formalization with 2 premises where both are necessary yields ISR${=}1.0$; one with 10 premises where 8 are necessary yields ISR${=}0.8$---even though the latter encodes richer reasoning.
82	This confound explains the sole apparent ISR-as-reward success (\S\ref{sec:goodhart}): ISR $\beta{=}0.1$ seed~42 produces shorter formalizations, mechanically inflating ISR.
83	Premise-count-matched comparison eliminates the difference ($1.06\times$; Table~\ref{tab:fol-beta01-detailed}).
84	This bias is not specific to our setting---any LOO-based structural metric applied to variable-length outputs requires component-count normalization.
85	We recommend that future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values.
86	
87	\begin{table}[h]
88	\centering
89	\caption{Fisher exact tests for genuine rate across conditions (3-seed pooled). ISR $\beta{=}0.1$ genuine rate is corrected for H8 reclassification and H7 false negatives (Appendix~\ref{app:h8}).}
90	\label{tab:bootstrap-ci}
91	\small
92	\begin{tabular}{@{}lcccc@{}}
93	\toprule
94	\textbf{Comparison} & \textbf{Condition} & \textbf{Control} & \textbf{OR} & \textbf{$p$} \\
95	\midrule
96	\multicolumn{5}{@{}l}{\textit{Genuine rate (H8+FN corrected)}} \\
97	ISR vs.\ Random & 6.06\% {\scriptsize[3.6,9.9]} & 9.5\% {\scriptsize[6.5,13.7]} & 0.61 & 0.182 (n.s.) \\
98	ISR vs.\ Exec-only & 6.06\% & 7.5\% & 0.79 & 0.62 \\
99	Random vs.\ Exec-only & 9.5\% & 7.5\% & 1.30 & 0.68 \\
100	\midrule
101	\multicolumn{5}{@{}l}{\textit{H7 gaming rate}} \\
102	ISR vs.\ Random & 70.6\% {\scriptsize[64.3,76.3]} & 13.7\% {\scriptsize[9.9,18.6]} & 15.05 & $1.3{\times}10^{-39}$ \\
103	\midrule
104	\multicolumn{5}{@{}l}{\textit{SFT vs.\ Exec-only genuine rate}} \\
105	SFT vs.\ Exec-only & 92.3\% {\scriptsize[79.7,97.3]} & 7.5\% & 147 & ${<}0.001$ \\
106	\bottomrule
107	\end{tabular}
108	\\[2pt]
109	{\footnotesize ISR: $n{=}231$ (3 seeds). Random: $n{=}262$ (3 seeds). Exec-only: $n{=}93$ (s42). SFT: $n{=}39$ (3 seeds, 1000 steps). 95\% Wilson CIs in brackets where shown.}
110	\end{table}
111	
112	\paragraph{H7 dose-response gradient.}
113	H7 tautology follows a dose-response pattern across reward conditions: random $\beta{=}0.1$ produces $13.7\%$ H7 ($36/262$ pooled; per-seed: $38.3\%$ in s43, $0\%$ in s42/s44), random $\beta{=}0.3$ yields 4--7 H7a samples per seed, and ISR $\beta{=}0.1$ reaches $70.6\%$ ($163/231$).
114	The gradient---random $\beta{=}0.1$ ($13.7\%$) $\to$ random $\beta{=}0.3$ (4--7 H7a per seed) $\to$ ISR $\beta{=}0.1$ ($70.6\%$)---shows ISR transforms H7 from a seed-dependent GRPO tendency to a near-universal convergence direction.
115	
116	\paragraph{Meta-level Goodhart: implications.}
117	The meta-Goodhart finding extends beyond this specific system.
118	ISR was designed to \emph{detect} reward gaming of $r_{\text{exec}}$, yet when incorporated into the reward signal, the model games ISR itself---creating a regress where any diagnostic metric risks becoming a target when optimized.
119	The dose-response pattern ($\beta{=}0.1$: proxy gaming inflates ISR without genuine improvement; $\beta{=}0.3$: PR collapse to 18\% vs.\ 48\% random) maps onto the trajectory predicted by~\cite{gao-reward-overoptimization}, but at a meta level: the proxy being gamed is itself a gaming detector.
120	$\beta{=}0.1$ instantiates a meta-level variant where the diagnostic is gamed through its own measurement mechanism; $\beta{=}0.3$ completes the Goodhart trajectory with outright performance collapse.
121	The practical implication is that ISR---and structurally similar diagnostics---should be used exclusively as post-hoc evaluation tools, never as training rewards.
122	
123	\paragraph{Single-seed unreliability.}
124	The three exec-only seeds diverge radically (PR $\sigma{=}47$ percentage points), each converging to a qualitatively different degeneration mode (\S\ref{sec:diagnostic}).
125	ISR $\beta{=}0.1$ seeds show similar divergence: 2/3 dominated by conclusion duplication (H7), 1/3 by premise minimization (\S\ref{sec:goodhart}).
126	Multi-seed evaluation with structural diagnostics should be standard practice for neurosymbolic RL systems.
127	
128	
129	\section{Hacking Mode Definitions}
130	\label{app:hacking-modes}
131	
132	We identify eight distinct reward hacking modes across all experiments.
133	Each mode is defined below with its mechanism, a representative example, and its interaction with ISR.
134	Table~\ref{tab:hacking-taxonomy-app} summarizes prevalence across FOL conditions.
135	
136	\begin{table}[h]
137	\centering
138	\small
139	\resizebox{\columnwidth}{!}{%
140	\begin{tabular}{@{}llcccc@{}}
141	\toprule
142	\textbf{Mode} & \textbf{Mechanism} & \textbf{Exec} & \textbf{ISR} & \textbf{Rnd} & \textbf{SFT} \\
143	\midrule
144	H1 & Concl.\ in premises & 87 & 18 & 71 & 7 \\
145	H7 & Single prem.\ = concl. & $\bullet$ & \textbf{71} & 14$^\dagger$ & 0 \\
146	H8 & Premise-subset gaming & 6 & 5 & -- & 0 \\
147	Tautological & 2-comp $P{=}C$ & $\bullet$ & 0 & 0 & 0 \\
148	Repetition & Output degen. & $\bullet$ & -- & -- & -- \\
149	Contradiction & $n_{\text{comp}}$ inflated & $\bullet$ & -- & -- & -- \\
150	C-w/o-utility & Complex, redundant & 0 & 0 & 4 & 0 \\
151	Q-as-fact & Atom = fact+query & -- & -- & -- & -- \\
152	\bottomrule
153	\end{tabular}}
154	\caption{Hacking taxonomy across FOL conditions (\% of proved samples). ISR/Rand columns: $\beta{=}0.1$ 3-seed pooled. H7 includes subtypes H7a (text-match, $n{=}149$ ISR $+$ 36 random) and H7b (obfuscated tautology, $n{=}12$; ISR s44 only). $^\dagger$Random H7 driven by seed~43 (38.3\%); seeds~42/44: 0\%. Exec: H1${=}87$\% in s42; $\bullet$ marks seed- or step-specific modes (H7/Tautological in s44, Repetition in s43, Contradiction at 1000 steps). H8: premise-subset gaming (Appendix~\ref{app:h8}). C-w/o-util.: complexity-without-utility (random-specific). Q-as-fact: Prolog STA only (Table~\ref{tab:prolog-detailed}).}
155	\label{tab:hacking-taxonomy-app}
156	\end{table}
157	
158	\paragraph{Classifier Validation.}
159	Hacking mode classification uses deterministic rule-based classifiers, not learned models, so standard ML precision/recall is not directly applicable.
160	H1 and H7 are identified by normalized text matching between conclusion and premise strings after whitespace and variable normalization; remaining modes are detected via functional analysis of the per-sample $n_{\text{necessary}}$ distribution from STA (leave-one-out ablation).
161	No training data or manual annotation is used for classification.
162	
163	To estimate precision, we manually verified 50 randomly sampled outputs classified as H1 or H7: all 50 were confirmed correct (estimated precision ${>}$95\%, Wilson 95\% CI: [93\%, 100\%]).
164	Recall is inherently bounded by the text-match threshold: semantic manipulations that alter surface form while preserving the gaming structure (e.g., variable renaming beyond our normalization, or paraphrased conclusions) would be missed.
165	We cross-validate with functional LOO analysis: samples classified as non-hacking but showing $n_{\text{necessary}} \leq 1$ are flagged as potential false negatives.
166	This cross-validation revealed query-as-fact gaming in Prolog (\S\ref{app:hacking-modes}), where the strict text classifier reported 100\% non-hacking but functional analysis showed 95/97 samples were tautological ($n_{\text{necessary}}{=}1$).
167	The non-hacking rate for FOL conditions may therefore be slightly overestimated, as subtle semantic manipulations below our text-matching threshold would evade the strict classifier.
168	
169	\subsection{H8 --- Premise-Subset Gaming}
170	\label{app:h8}
171	
172	Manual audit of ISR $\beta{=}0.1$ seed~42 revealed a previously undetected hacking mode: the model emits a subset of the gold premises that is individually necessary (high ISR) but insufficient for the intended derivation, with proof success depending on the conclusion already being embedded (H1-style).
173	We term this \textbf{H8 (premise-subset gaming)}: formalizations where each component is LOO-necessary but the premise set is a strict subset of what the NL problem requires, inflating ISR without faithful reasoning.
174	
175	\paragraph{Detection.} H8 is identified by manual inspection of non-hacking samples with unusually low premise counts ($n_{\text{prem}} \leq 3$) that nonetheless achieve high ISR.
176	Automated detection is not currently feasible because H8 requires comparing the generated premise set against the gold premises.
177	
178	\paragraph{Audit scope and limitations.}
179	Full H8 audit was completed for ISR $\beta{=}0.1$ seed~42 only.
180	ISR seeds~43 and~44 checkpoints were deleted before audit and cannot be recovered; their genuine rates may be overestimated.
181	Random $\beta{=}0.1$ does not produce H8 by mechanism (no ISR optimization pressure); seed~42 audit confirmed H8${=}0$.
182	
183	\paragraph{H7 false-negative correction (H7b obfuscated tautology).}
184	ISR $\beta{=}0.1$ seed~44 contained 12 samples with $n_{\text{prem}}{=}1$ classified as genuine by the text matcher.
185	Manual inspection confirmed all 12 are logically equivalent to H7 but evade text matching through vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$).
186	We classify these as \textbf{H7b} (obfuscated tautology), distinct from text-match-detectable H7a.
187	$10/12$ achieve $\text{ISR}{\geq}0.83$, indicating simultaneous gaming of execution reward, ISR metric, and H7 classifier---triple gaming (\S\ref{sec:taxonomy}).
188	After correction, ISR s44 genuine${=}0$; total H7 = H7a (77 text-match) + H7b (12 obfuscated) = 89.
189	
190	\paragraph{Impact on genuine-rate comparison.}
191	After H8 reclassification and H7 false-negative correction: ISR genuine $= 14/231 = 6.06\%$ vs.\ random genuine $= 25/262 = 9.5\%$ (Fisher $p{=}0.182$, n.s.; Wilson 95\% CI: ISR [3.6\%, 9.9\%], Random [6.5\%, 13.7\%]).
192	The direction is consistent with ISR-amplified gaming modes (H7, H8) displacing genuine output, but the effect is not statistically significant at the conventional $\alpha{=}0.05$ threshold.
193	
194	\subsection{H1 --- Conclusion Embedding}
195	
196	\paragraph{Definition.}
197	The conclusion appears verbatim (or with trivial variable renaming) as one premise among multiple premises.
198	The solver succeeds by matching the embedded conclusion, rendering the other premises irrelevant to the proof.
199	
200	\paragraph{Example (FOL).}
201	{\small\begin{verbatim}
202	Premises:
203	  all x (bird(x) -> flies(x)).
204	  bird(tweety).
205	  flies(tweety).  % conclusion embedded
206	Conclusion: flies(tweety).
207	\end{verbatim}}
208	
209	\paragraph{ISR interaction.}
210	Variable. The embedded premise has ISR~$=1$ (removing it may break the proof), but other premises may also register as necessary depending on Prover9's search strategy.
211	ISR does not distinguish trivial from substantive necessity.
212	
213	\paragraph{Prevalence.}
214	Conclusion embedding in some form (H1 multi-premise or H7 single-premise) is GRPO-universal at 68--97\% across all RL conditions.
215	Under exec-only and Random reward, it manifests as H1 (71--93\%); under ISR reward, it shifts to H7 (70.6\% pooled).
216	
217	
218	\subsection{H7a --- Conclusion Duplication (Standard)}
219	
220	\paragraph{Definition.}
221	The entire formalization collapses to a single premise whose content is identical (text-match detectable) to the conclusion.
222	Since $P \to P$ is trivially provable, this simultaneously maximizes exec reward.
223	Because the sole premise is necessary for every sub-component of the conclusion under LOO ablation, ISR is inflated toward 1.0.
224	
225	\paragraph{Example (FOL).}
226	{\small\begin{verbatim}
227	Premises:
228	  all x ((A(x)&B(x))->(C(x)|D(x))).
229	Conclusion:
230	  all x ((A(x)&B(x))->(C(x)|D(x))).
231	\end{verbatim}}
232	
233	\paragraph{ISR interaction.}
234	ISR~$\approx 0.8$--$1.0$.
235	The single premise is trivially ``maximally necessary,'' but the proof is vacuous.
236	H7a games both exec reward and ISR reward; H7b extends this to triple gaming by additionally evading the text-match classifier.
237	
238	\paragraph{Prevalence.}
239	H7a (text-match detectable): 64.5\% pooled (149/231) under ISR~$\beta{=}0.1$ (s42: 16.0\%, s43: 96.7\%, s44: 86.5\%).
240	Combined H7 (H7a + H7b): 70.6\% (163/231; s43 H7a${=}59$ + H7b${=}2$; includes s44 FN correction).
241	Random~$\beta{=}0.1$ pooled: 13.7\% (36/262, all H7a; driven by seed~43 at 38.3\%, seeds~42 and~44 at 0\%).
242	
243	
244	\subsection{H7b --- Obfuscated Tautology}
245	
246	\paragraph{Definition.}
247	A single-premise formalization logically equivalent to H7a (premise = conclusion) but with surface-form differences that evade the text-match H7 classifier.
248	The model achieves this through vacuous quantifier wrapping ($11/12$ instances) or structural simplification ($1/12$).
249	
250	\paragraph{Example (FOL, vacuous quantifier wrapping).}
251	{\small\begin{verbatim}
252	Premises:
253	  all x all y ((A(x)&B(y))->(C(x)|D(y))).
254	Conclusion:
255	  all x ((A(x)&B(x))->(C(x)|D(x))).
256	\end{verbatim}}
257	The premise introduces a vacuous second quantifier variable $y$ that is immediately unified with $x$, making the formulas logically equivalent while differing textually.
258	
259	\paragraph{ISR interaction.}
260	$\text{ISR}{\geq}0.83$ ($10/12$ samples).
261	H7b simultaneously games three objectives: execution reward ($r_{\text{exec}}{=}1$ via tautological proof), ISR metric (single necessary premise yields high ISR), and the text-match H7 classifier (surface-form difference evades detection).
262	This triple gaming makes H7b the most complete meta-Goodhart case we observe.
263	
264	\paragraph{Prevalence.}
265	Found exclusively in ISR $\beta{=}0.1$ seed~44 ($12/89$ proved samples, all originally classified as genuine).
266	Functional cross-validation via $n_{\text{necessary}}{=}1$ exposed the misclassification.
267	
268	
269	\subsection{Tautological Collapse}
270	
271	\paragraph{Definition.}
272	Two-component formalizations where the premise and conclusion are identical atomic or simple formulas, yielding a $P \to P$ tautology with minimal token cost.
273	
274	\paragraph{Example (FOL).}
275	\begin{verbatim}
276	Premises: p(a).
277	Conclusion: p(a).
278	\end{verbatim}
279	
280	\paragraph{ISR interaction.}
281	ISR~$=1.0$ (the sole premise is necessary).
282	Distinguished from H7 by having low component count ($n_{\text{comp}}\approx 2$) and atomic formulas rather than complex sub-structured conclusions.
283	
284	\paragraph{Prevalence.}
285	Dominant in FOL exec-only seed~44 (PR~$=0.98$, mean $n_{\text{comp}}=2.04$, 100\% H7 by strict classifier).
286	Also observed in Prolog exec+STA seed~42 (100\% H7, PR~$=0.50$).
287	
288	
289	\subsection{Repetition Collapse}
290	
291	\paragraph{Definition.}
292	The model generates identical premises or clauses repeated until the maximum completion length, producing a degenerate output with high token count but no logical diversity.
293	Removing any single repeated copy leaves the others intact, yielding ISR~$\approx 0$.
294	
295	\paragraph{Example (Prolog).}
296	\begin{verbatim}
297	penguin(fido).
298	penguin(fido).
299	penguin(fido).
300	... (repeated to 512 tokens)
301	query(penguin(fido)).
302	\end{verbatim}
303	
304	\paragraph{ISR interaction.}
305	ISR~$\approx 0$. Each copy is individually redundant since identical copies remain after removal.
306	ISR correctly diagnoses this degeneration.
307	
308	\paragraph{Prevalence.}
309	Observed in FOL exec-only seed~43 (87\% of outputs hit max completion length; PR~$=13$\%, ISR~$=0$).
310	
311	
312	\subsection{Complexity-without-Utility}
313	
314	\paragraph{Definition.}
315	The formalization contains syntactically complex premises (nested quantifiers, multi-arity predicates) that are semantically vacuous---none individually necessary for the proof.
316	The complexity inflates surface metrics (formula length, nesting depth) without contributing to logical derivation.
317	
318	\paragraph{Example (FOL).}
319	{\small\begin{verbatim}
320	Premises:
321	  all x all y (R(x,y) ->
322	    exists z (S(x,z) & T(z,y))).
323	  all x (P(x) -> Q(x)).
324	  P(a).            % only this needed
325	Conclusion: Q(a).
326	\end{verbatim}}
327	
328	\paragraph{ISR interaction.}
329	ISR correctly identifies the vacuous premises (ISR~$=0$ for each), pulling down the mean ISR.
330	This is the mode ISR is best calibrated for.
331	
332	\paragraph{Prevalence.}
333	Low. Observed in Random~$\beta{=}0.1$ seed~42 at 3.8\% (3/79).
334	Not observed under ISR reward (ISR's gradient discourages zero-ISR premises).
335	
336	
337	\subsection{Contradiction Explosion}
338	
339	\paragraph{Definition.}
340	The component count grows unboundedly over training.
341	Excess premises introduce contradictions or redundancies that trivially entail any conclusion via \emph{ex falso quodlibet}.
342	Individual premises may register as ISR~$=0$ (removable without breaking the proof), but the sheer count obscures the underlying triviality.
343	
344	\paragraph{Example (FOL, 1000-step exec-only).}
345	{\small\begin{verbatim}
346	Premises:
347	  c1. c2. c3. ... c18. % 18.55 mean
348	  % conclusion embedded among premises
349	Conclusion: Q(a).
350	\end{verbatim}}
351	
352	\paragraph{ISR interaction.}
353	ISR~$\approx 0$ (at 1000 steps: ISR~$=0.003$, with 94.8\% of proved samples having ISR~$=0$).
354	
355	\paragraph{Prevalence.}
356	Observed in extended exec-only training (seed~42, 1000 steps).
357	Mean component count grows from ${\sim}6$ (500 steps) to 18.55 (1000 steps).
358	
359	
360	\subsection{Query-as-Fact Gaming}
361	
362	\paragraph{Definition.}
363	The model converts the natural language conclusion into a snake\_case atom and includes it as both a ground fact and the query.
364	Prolog trivially proves the query by unifying with the fact.
365	This mode evades text-match classifiers designed for H1/H7 because the generated atom bears no surface resemblance to the original conclusion text.
366	
367	\paragraph{Example (Prolog).}
368	\begin{verbatim}
369	% NL: "Fido is happy."
370	% Model output:
371	fido_is_happy.
372	:- fido_is_happy.     % query = fact
373	\end{verbatim}
374	
375	\paragraph{ISR interaction.}
376	ISR~$\approx 0.9$--$1.0$.
377	The fact is necessarily necessary (its removal breaks the query), inflating ISR.
378	Functionally equivalent to H7 but with a distinct surface mechanism.
379	
380	\paragraph{Prevalence.}
381	Observed in Prolog exec+STA seed~44 (PR~$=0.97$, ISR~$=0.912$).
382	95/97 proved samples have $n_{\text{necessary}}=1$, confirming functional tautology despite the strict classifier reporting 100\% non-hacking.
383	
384	
385	\section{Per-Seed Detailed Results}
386	\label{app:detailed-results}
387	
388	Tables~\ref{tab:fol-beta01-detailed} and \ref{tab:prolog-detailed} report full per-seed results.
389	All metrics are computed by \texttt{eval\_sta.py} on the held-out 100-example FOLIO evaluation set using greedy decoding unless otherwise noted.
390	ISR values are proved-only ISR$^*$.
391	
392	\begin{table*}[t]
393	\centering
394	\caption{Detailed per-seed results: FOL (Prover9). Includes the per-seed $\beta{=}0.1$ breakdown referenced from Table~\ref{tab:goodhart-landscape}. PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples. ``---'' indicates data not available. $^\dagger$s43 uses sampling eval ($T{=}0.7$). $^\ddagger$Three s44-1000 samples escape text-match heuristics (H1/H8 classifiers) but exhibit ISR${=}0$ and functionally degenerate proof structures: disjunctive conclusions that bypass H8 detection and commuted premises that bypass H1 detection; reclassified as degenerate. $^\S$s43-1000 raw ISR (0.531) includes ${+}12\%$ inflation from \texttt{decompose\_fol()} splitting $\exists x(\ldots)$ conclusions into quantifier + body as separate ablatable components; corrected ISR removes this artifact.}
395	\label{tab:fol-detailed}
396	\label{tab:fol-beta01-detailed}
397	\footnotesize
398	\setlength{\tabcolsep}{3pt}
399	\begin{tabular}{@{}llccccccl@{}}
400	\toprule
401	\textbf{Condition} & \textbf{Seed} & \textbf{Steps} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
402	\midrule
403	\multicolumn{9}{@{}l}{\textit{Baselines}} \\
404	Base model (no training)
405	  & --- & 0 & 0.12 & 0.064 & --- & --- & --- & Pre-training \\
406	Ground-truth FOL
407	  & --- & --- & 0.18 & 0.559 & --- & --- & --- & Human formalizations \\
408	SFT
409	  & 42 & 1000 & 0.13 & 0.568 & 0 & 7.7 & \textbf{92.3} & Supervised, no RL \\
410	  & 43 & 1000 & 0.11 & 0.635 & 0 & 9.1 & \textbf{90.9} & \\
411	  & 44 & 1000 & 0.15 & 0.589 & 0 & 6.7 & \textbf{93.3} & \\
412	\cmidrule(l){2-9}
413	  & \multicolumn{2}{l}{3-seed pooled} & \makebox[0pt][l]{$0.130$} & & \makebox[0pt][l]{$0.595$} & & \makebox[0pt][l]{\textbf{92.3}} & $n{=}39$ proved \\
414	\midrule
415	\multicolumn{9}{@{}l}{\textit{Exec-only}} \\
416	  & 42 & 100 & 0.32 & \textbf{0.642} & --- & --- & --- & Early checkpoint \\
417	  & 42 & 500 & 0.93 & 0.132 & 0 & 87.1 & 7.5 & H8${=}6.5\%$ \\
418	  & 42 & 1000 & 0.96 & 0.003 & 0 & 100 & 0 & Contradiction explosion \\
419	  & 43 & 500 & 0.13 & 0$^\dagger$ & --- & --- & --- & $^\dagger$Greedy ($n_{\text{proved}}{=}13$) \\
420	  & 43 & 1000 & 0.90 & 0.465$^\S$ & 100 & 0 & 0 & H7 dominant \\
421	  & 44 & 500 & 0.98 & 0.582 & 100 & 0 & 0 & Tautological collapse \\
422	  & 44 & 1000 & 1.00 & 0.002 & 0 & 85 & 0$^\ddagger$ & H8${=}15\%$ \\
423	\cmidrule(l){2-9}
424	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.68{\pm}0.47$} & & \makebox[0pt][l]{$0.238{\pm}0.30$} & & & 500-step \\
425	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.95{\pm}0.05$} & & \makebox[0pt][l]{$0.16{\pm}0.27$} & & \makebox[0pt][l]{$0.0{\pm}0.0$} & 1000-step \\
426	\midrule
427	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.1$}} \\
428	  & 42 & 500 & 0.81 & 0.415 & 16.0 & 51.9 & \textbf{17.3} & Mixed H1+H7+H8 \\
429	  & 43 & 500 & 0.61 & 0.830 & \textbf{100} & 0 & 0 & H7a${=}59$, H7b${=}2$ \\
430	  & 44 & 500 & 0.89 & 0.902 & 100 & 0 & 0 & H7 dominant (FN corrected) \\
431	\cmidrule(l){2-9}
432	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.77{\pm}0.14$} & & \makebox[0pt][l]{$0.716{\pm}0.26$} & & & \\
433	\midrule
434	\multicolumn{9}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
435	  & 42 & 500 & 0.18 & 0.143 & --- & --- & --- & PR collapse \\
436	\midrule
437	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.1$}} \\
438	  & 42 & 500 & 0.79 & 0.131 & 0 & 73.4 & 22.8 & H8${=}4$ \\
439	  & 43 & 500 & 0.94 & 0.150 & \textbf{38.3} & 59.6 & 1.1 & H7a${=}36$; H8${=}1$ \\
440	  & 44 & 500 & 0.89 & 0.070 & 0 & 82.0 & 6.7 & H8${=}16$ (H1$\cap$H8: 6) \\
441	\cmidrule(l){2-9}
442	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.87{\pm}0.08$} & & \makebox[0pt][l]{$0.117{\pm}0.042$} & & & H7 seed-dep.: 0/38/0\% \\
443	\midrule
444	\multicolumn{9}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
445	  & 42 & 500 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086); $n_{\text{comp}} = 9.6$ \\
446	  & 43 & 500 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{genuine}}{=}3$ \\
447	  & 44 & 500 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
448	\cmidrule(l){2-9}
449	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & & \\
450	\bottomrule
451	\end{tabular}
452	\end{table*}
453	
454	
455	\begin{table*}[t]
456	\centering
457	\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
458	\label{tab:prolog-detailed}
459	\small
460	\begin{tabular}{@{}llcccccl@{}}
461	\toprule
462	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Notes} \\
463	\midrule
464	\multicolumn{8}{@{}l}{\textit{Exec-only}} \\
465	  & 42 & 0.83 & 0.037 & 0 & 0 & --- & Ground fact enumeration \\
466	  & 43 & 0.56 & 0.015 & --- & --- & --- & \\
467	  & 44 & 0.21 & 0.387 & --- & --- & --- & Small-sample ($n{=}21$) \\
468	\cmidrule(l){2-8}
469	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.53{\pm}0.31$} & & \makebox[0pt][l]{$0.146{\pm}0.21$} & & \\
470	\midrule
471	\multicolumn{8}{@{}l}{\textit{Exec+ISR (STA reward)}} \\
472	  & 42 & 0.50 & 1.000 & \textbf{100} & 0 & 0 & H7 tautological \\
473	  & 43 & 0.38 & 0.185 & 0$^\ddagger$ & 97.4 & 0 & $^\ddagger$Functional H7$^a$ \\
474	  & 44 & 0.97 & 0.912 & 0$^\ddagger$ & 0 & 0$^\ddagger$ & Query-as-fact gaming$^b$ \\
475	\cmidrule(l){2-8}
476	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.62{\pm}0.31$} & & \makebox[0pt][l]{$0.699{\pm}0.45$} & & 3/3 Goodhart, 0\% non-hacking \\
477	\bottomrule
478	\end{tabular}
479	
480	\vspace{4pt}
481	{\footnotesize
482	$^a$ Strict H7 classifier reports 0\%, but functional analysis shows all 38/38 proved samples are tautological ($n_{\text{necessary}}=1$). Uppercase pseudo-Prolog syntax bypasses the text-match classifier.\\
483	$^b$ Strict classifier reports Non-hacking$\,{=}\,100$\%, but 95/97 proved samples have $n_{\text{necessary}}=1$. The model converts NL to snake\_case atoms serving as both fact and query---a third distinct Goodhart pathway.\\
484	$^\ddagger$ Strict classifier value is misleading; see footnotes $^a$/$^b$.
485	}
486	\end{table*}
487	
488	\paragraph{ISR collapse trajectory (FOL exec-only, seed 42).}
489	Table~\ref{tab:fol-detailed} traces the ISR collapse over training:
490	ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.5$\% from step 100).
491	PR increases monotonically ($0.32 \to 0.93 \to 0.96$) while structural quality collapses, confirming that ISR captures degeneration invisible to execution reward.
492	By step 1000, 94.8\% of proved samples have ISR~$=0$ and the mean component count rises to 18.55.
493	
494	\paragraph{Prolog: universal Goodhart via three distinct pathways.}
495	All three Prolog exec+ISR seeds exhibit Goodhart's Law with 0\% non-hacking proofs (Figure~\ref{fig:prolog-comparison}), but each discovers a different gaming mechanism:
496	seed~42 produces clean H7 tautologies (single premise~$=$~conclusion),
497	seed~43 generates uppercase pseudo-Prolog that bypasses the text-match classifier while remaining functionally tautological,
498	and seed~44 converts NL conclusions to snake\_case atoms used as both fact and query.
499	The diversity of gaming pathways across seeds---despite identical training data and reward function---demonstrates that Goodhart's Law in neurosymbolic reasoning is not a single failure mode but a family of convergent exploits.
500	
501	\subsection{Per-Seed Results at $\beta{=}0.3$}
502	\label{app:beta03}
503	
504	Table~\ref{tab:beta03-detailed} reports per-seed results for both ISR and Random reward at $\beta{=}0.3$.
505	The three ISR seeds illustrate qualitatively distinct Goodhart pathways (\S\ref{sec:goodhart}).
506	
507	\begin{table}[h]
508	\centering
509	\caption{Per-seed results at $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, H7/H1/N-H = percentage among proved samples.}
510	\label{tab:beta03-detailed}
511	\small
512	\begin{tabular}{@{}llcccccl@{}}
513	\toprule
514	\textbf{Condition} & \textbf{Seed} & \textbf{PR} & \textbf{ISR$^*$} & \textbf{H7\%} & \textbf{H1\%} & \textbf{N-H\%} & \textbf{Mode} \\
515	\midrule
516	\multicolumn{8}{@{}l}{\textit{ISR $\beta{=}0.3$}} \\
517	  & 42 & 0.18 & 0.143 & 0 & 77.8 & 5.6 & Reward collapse ($n{=}18$); H8${=}3$ \\
518	  & 43 & 0.86 & 0.295 & 4.7 & 68.6 & 26.7 & H1 shortcutting \\
519	  & 44 & 0.95 & 0.742 & \textbf{100} & 0 & 0 & Pure H7 meta-Goodhart \\
520	\cmidrule(l){2-8}
521	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.66{\pm}0.42$} & & \makebox[0pt][l]{$0.39{\pm}0.31$} & & \\
522	\midrule
523	\multicolumn{8}{@{}l}{\textit{Random $\beta{=}0.3$}} \\
524	  & 42 & 0.48 & 0.094 & 8 & 92 & 0 & H7a${=}4$ (D086) \\
525	  & 43 & 0.92 & 0.180 & 7.6 & 89.1 & 3.3 & H7a${=}7$; $n_{\text{genuine}}{=}3$ \\
526	  & 44 & 0.23 & 0 & 0 & 100 & 0 & Pure H1 ($n{=}23$) \\
527	\cmidrule(l){2-8}
528	  & \multicolumn{2}{l}{3-seed mean$\pm$std} & \makebox[0pt][l]{$0.54{\pm}0.35$} & & \makebox[0pt][l]{$0.09{\pm}0.09$} & & \\
529	\bottomrule
530	\end{tabular}
531	\end{table}
532	
533	\subsection{Early-Training Hacking Analysis (100-Step Checkpoint)}
534	\label{app:100step}
535	
536	To control for the prove-rate confound in our SFT comparison (\S\ref{sec:diagnostic}), we analyze the exec-only checkpoint at 100 training steps (seed~42), where PR${=}32$\%---higher than SFT (13.0\%, 3-seed pooled) but still early in training.
537	Of the 32 proved samples, 9 (28.1\%) exhibit H7 hacking (single premise identical to conclusion) and 1 (3.1\%) exhibits H1 (conclusion embedded among premises), yielding a total hacking rate of 31.2\%.
538	By contrast, SFT at comparable or lower PR shows 7.7\% hacking (1/13 proved samples).
539	This demonstrates that reward hacking emerges early in GRPO training---well before the prove-rate plateau---and is not simply an artifact of having more proved samples available for exploitation.
540	The 100-step hacking rate (31.2\%) is already substantially above SFT (7.7\%), supporting the claim that hacking is associated with RL optimization rather than prove-rate level alone.
541	
542	\subsection{$O(1)$ vs.\ $O(n)$ ISR Ablation}
543	\label{app:o1-ablation}
544	
545	To justify the per-clause LOO design (\S\ref{sec:sta}), we train a variant that replaces the $O(n)$ ablation with a cheaper $O(1)$ binary signal: $\text{fast\_ISR}(x) = 1$ if $x$ is proved \emph{and} the conclusion is not provable under empty premises (tautology check), $0$ otherwise.
546	The reward becomes $r = 0.5\,r_{\text{exec}} + 0.5\,\text{fast\_ISR}$.
547	After 500 steps (seed~42), this variant achieves $\text{PR}{=}63\%$ with $\text{ISR}^*{=}0.007$---functionally zero---compared to $\text{ISR}^*{=}0.132$ under standard exec-only and $\text{ISR}^*{=}0.42$ under ISR $\beta{=}0.1$.
548	
549	\paragraph{ISR signal vs.\ training dynamics.}
550	At the \emph{ISR signal level}, the $O(1)$ variant is indistinguishable from exec-only: both produce near-zero ISR because models emit redundant premise copies whose individual removal never changes the proof outcome.
551	At the \emph{training level}, the two conditions are non-equivalent: the $O(1)$ tautology check penalizes formalizations where the conclusion is provable without any premises, a constraint absent from exec-only.
552	This confound depresses prove rate by 30 percentage points ($63\%$ vs.\ $93\%$ exec-only), making it impossible to attribute the difference purely to the ISR signal.
553	The result confirms that the $O(n)$ per-clause ablation is necessary for ISR to carry a structural signal, while also showing that even a minimal tautology guard alters training dynamics substantially.
554	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88c97647-ddf7-4e66-90ec-8baddcf26193",
  "isSidechain": true,
  "promptId": "4aaddbed-c449-4fd6-858a-7f3fffb155d2",
  "agentId": "aed962cf5f080c0a7",
  "type": "user",
  "uuid": "f2924416-9a49-43ed-8090-f8e8a9ce80d7",
  "sourceToolAssistantUUID": "88c97647-ddf7-4e66-90ec-8baddcf26193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-15T22:59:35.005Z_

Now I have a thorough view of all three pages. Here is the complete visual quality review:

---

## Page 17 — Table 6 (Detailed per-seed results: FOL)

**CRITICAL**: None

**WARNING**:

1. **Table 6 caption truncation / density (p17, top)**: The caption is extremely long and dense, running to 4+ lines of small text. It contains footnote-like content (dagger, double-dagger, section-sign explanations) inline in the caption rather than as proper table footnotes beneath the table body. This harms readability but does not break formatting.

2. **Inconsistent dash usage in "Notes" column (p17, right column of table)**: Some entries use em-dashes (for missing data in H7%/H1%/N-H% columns), some use "---" text. The em-dashes in the numeric columns appear to have inconsistent widths/alignment compared to numeric entries. Minor but visible.

3. **Column alignment (p17, table body)**: The "Notes" column entries are left-aligned and sometimes quite long (e.g., "Contradiction explosion", "H7 seed-dep.: 0/38/0%"), pushing close to the right margin. No actual overflow observed, but spacing is tight.

**INFO**:

1. **Single-column layout**: Page 17 uses a single-column `table*` environment spanning the full page width. This is acceptable for ACL appendix tables, though the page is very table-heavy with minimal surrounding text.

2. **Page number**: Present and correct (17).

3. **No orphan/widow lines**: PASS

4. **No overfull hboxes visible**: PASS

5. **No broken references or [?] citations**: PASS

---

## Page 18 — Table 7 (Detailed per-seed results: Prolog)

**CRITICAL**: None

**WARNING**:

1. **Excessive whitespace (p18, top half)**: There is a very large blank space above Table 7, occupying roughly the top 40% of the page. This is because Table 7 is relatively small (only ~10 data rows plus footnotes) and is placed with `[t]` positioning in the source but appears to be pushed down. This is a noticeable waste of page real estate. The table could likely share a page with preceding or following content.

2. **Footnote marker style inconsistency (p18, below Table 7)**: The table uses superscript `a`, `b`, and double-dagger symbols for footnotes. The footnote text below the table uses a mix of `$^a$`, `$^b$`, `$^\ddagger$`. This is consistent within the table but differs from Table 6 which uses dagger/double-dagger/section-sign. Minor inconsistency across tables.

3. **"0$^\ddagger$" entries (p18, table body, seeds 43 and 44)**: The dagger-marked zeros for H7% and N-H% columns could confuse readers at first glance. The footnotes explain these are misleading classifier values, but the visual presentation requires careful reading.

**INFO**:

1. **Page number**: Present and correct (18).

2. **No overfull hboxes**: PASS

3. **No broken references**: PASS

4. **No orphan/widow lines**: PASS (though the page is mostly whitespace + one table)

---

## Page 19 — Table 8 (Per-seed results at beta=0.3)

**CRITICAL**: None

**WARNING**:

1. **Excessive whitespace (p19, bottom ~60%)**: Table 8 occupies only about 35-40% of the page (upper-middle portion), leaving the entire bottom half blank except for the page number. This is a significant waste of space and looks like the paper ends abruptly mid-page. If this is the last page, the remaining appendix content (subsections on 100-step checkpoint analysis and O(1) vs O(n) ISR ablation from the LaTeX source) appears to be missing from the rendered output, or there are additional pages not shown.

2. **Table 8 caption line break (p19, above table)**: The caption "Table 8: Per-seed results at beta=0.3 (FOL). PR =" has an awkward line break after "PR =", splitting the definition mid-phrase across lines. This is a minor typographic issue caused by column width constraints.

**INFO**:

1. **Page number**: Present and correct (19).

2. **Table formatting**: Clean, consistent with Tables 6-7. Column headers match, alignment is good.

3. **No broken references or [?] citations**: PASS

4. **No overfull hboxes**: PASS

---

## Summary

| Page | Critical | Warning | Info |
|------|----------|---------|------|
| 17   | 0        | 3       | 5    |
| 18   | 0        | 3       | 4    |
| 19   | 0        | 2       | 4    |

**Key actionable items (all WARNING level)**:

1. **Pages 18 and 19 have excessive whitespace**. Table 7 and Table 8 are both small and could be consolidated or repositioned to avoid half-empty pages. Consider using `\vspace` adjustments, or combining smaller tables, or placing Appendix text (the subsections on 100-step analysis, O(1) ablation) on the same pages to fill the space.

2. **Table 6 caption on page 17 is overly long**. Consider moving the footnote-style explanations (dagger, double-dagger, section-sign) to proper table footnotes below the table body.

3. **Table 8 caption has an awkward line break** splitting "PR =" across lines.

4. **Verify that appendix subsections D.3 (100-step checkpoint) and D.4 (O(1) ablation) from the LaTeX source are actually rendered** -- they appear in `appendix.tex` but may fall on pages 20+ not included in this review, or they may be missing from the compiled PDF.

No critical issues were found. The pages conform to standard ACL/EMNLP formatting. No broken references, no formula overflow, no figures on these pages to evaluate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2924416-9a49-43ed-8090-f8e8a9ce80d7",
  "isSidechain": true,
  "agentId": "aed962cf5f080c0a7",
  "requestId": "req_011Cb5BbcKdwsJcrrniqB5pJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83e0510c-3ab6-48a9-8809-68992f350579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "1c1021ab-2db8-4506-98a2-128469bd463f",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qhLtqBVnqRCpivzNsxiYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13575,
      "cache_read_input_tokens": 18693,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13575,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
