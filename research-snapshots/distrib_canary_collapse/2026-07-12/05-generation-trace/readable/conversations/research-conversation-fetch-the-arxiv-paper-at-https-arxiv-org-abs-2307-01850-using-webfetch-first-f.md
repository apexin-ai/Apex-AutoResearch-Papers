# Research conversation: Fetch the arXiv paper at https://arxiv.org/abs/2307.01850 using WebFetch. First fetch the HTML version at https://arxiv.

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3beaf73a9e1f198f.jsonl`
- **Structured JSON:** [`5dd057f94aa95c7f5514.json`](../../sessions/5d/5dd057f94aa95c7f5514.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-20T15:00:40.141Z_

Fetch the arXiv paper at https://arxiv.org/abs/2307.01850 using WebFetch.

First fetch the HTML version at https://arxiv.org/html/2307.01850v4 with the prompt:
"Extract the full paper content in detail. I need:
1. Complete introduction section with all paragraphs
2. The contribution statement (usually end of intro)
3. Complete experiment/results section including all tables and figures descriptions
4. Limitations and future work section
5. All figure and table captions
6. All references to figures/tables in the main text
7. Method section key details
8. Baselines, metrics, datasets used
9. Training recipe details (optimizer, lr, hardware, etc.)
Return as much detail as possible."

If the HTML version fails, try https://arxiv.org/abs/2307.01850 with the same prompt.

Then report EVERYTHING you extracted - do not summarize, give me the full extracted content. This is "Self-Consuming Generative Models Go MAD" (ICLR 2024).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "2757e685-80d8-4691-b27d-a43537c8c5da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T15:00:40.144Z_

```json
{
  "parentUuid": "2757e685-80d8-4691-b27d-a43537c8c5da",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
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
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "3ec9ea97-1aa1-4612-aaf1-3ad550e7b39d",
  "timestamp": "2026-05-20T15:00:40.144Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-20T15:00:42.790Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VW5wcetT6tD7ynGmk7UTSv`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ec9ea97-1aa1-4612-aaf1-3ad550e7b39d",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2AxyPkVyJbjvpBpTkP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "becd3d19-c145-42d9-8c46-1abbfd2ec2e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CWn3FpmpK8auJAd8zXf9mD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9037,
      "cache_read_input_tokens": 8155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9037,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 4 · 2026-05-20T15:00:42.793Z_

<details><summary>↩ Tool result · `toolu_01VW5wcetT6tD7ynGmk7UTSv`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "becd3d19-c145-42d9-8c46-1abbfd2ec2e8",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "e9034bb8-5e57-4f0b-9d2d-90201f3e4373",
  "sourceToolAssistantUUID": "becd3d19-c145-42d9-8c46-1abbfd2ec2e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T15:00:45.327Z_

I'll fetch the HTML version of the paper first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9034bb8-5e57-4f0b-9d2d-90201f3e4373",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2BB79V3BNxZqu1doZ5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2ba47a5-1170-46d8-aeb0-8a3d157c87ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WXnNx4ppncrnmBVA5S7xrH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 17192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 6 · 2026-05-20T15:00:46.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0188vddtVUqSPm36Pw2fPfYe`</summary>

```json
{
  "url": "https://arxiv.org/html/2307.01850v4",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2ba47a5-1170-46d8-aeb0-8a3d157c87ff",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2BB79V3BNxZqu1doZ5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be088f1f-ed63-47e4-b600-4d55f36191e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WXnNx4ppncrnmBVA5S7xrH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 17192,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 215,
          "cache_read_input_tokens": 17192,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
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

_source line 7 · 2026-05-20T15:00:46.800Z_

<details><summary>↩ Tool result · reported error · `toolu_0188vddtVUqSPm36Pw2fPfYe`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be088f1f-ed63-47e4-b600-4d55f36191e8",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "24695243-c328-41a2-afd5-db9e8e72541d",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "be088f1f-ed63-47e4-b600-4d55f36191e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T15:00:50.105Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AnExpoogwR1mt47LwVRvdM`</summary>

```json
{
  "url": "https://arxiv.org/html/2307.01850",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24695243-c328-41a2-afd5-db9e8e72541d",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2BTPBq4D8Pqse8gFg7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aec43cbb-5476-451b-8744-9cba4fad2781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014nVa8Fn453sdsXpNWfTmh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 244,
      "cache_read_input_tokens": 18624,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 244
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 18624,
          "cache_creation_input_tokens": 244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 244,
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

_source line 9 · 2026-05-20T15:00:50.120Z_

<details><summary>↩ Tool result · reported error · `toolu_01AnExpoogwR1mt47LwVRvdM`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aec43cbb-5476-451b-8744-9cba4fad2781",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "353a6298-e56d-4473-80a5-1e1b0a0a1416",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "aec43cbb-5476-451b-8744-9cba4fad2781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T15:00:53.354Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VuUxaDKnwztCzRan5xtcMj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2307.01850",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "353a6298-e56d-4473-80a5-1e1b0a0a1416",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2BhhQc1Wyto6D3Q6TW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd045202-a4e9-4022-8820-4f30cf04b1d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WahvtRqV8pRjLb7erHzwbC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 18868,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 18868,
          "cache_creation_input_tokens": 228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 228,
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

_source line 11 · 2026-05-20T15:00:58.026Z_

<details><summary>↩ Tool result · `toolu_01VuUxaDKnwztCzRan5xtcMj`</summary>

```text
# Summary of Available Content

I can only provide information from the **arXiv abstract page** provided. The full paper content (introduction, experiments, results, figures, tables, methods, references) is **not included** in the web page excerpt you shared.

## What's Available from the Page:

**Title:** "Self-Consuming Generative Models Go MAD"

**Authors:** Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk

**Key Finding:** The abstract indicates that "without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease."

**Paper Details:** 31 pages, 31 figures; submitted July 4, 2023

## What's Missing:

To extract the detailed sections you requested (introduction, experiments, results, tables, figures, methods, baselines, training recipes, references), you would need to access the **full PDF** via the link: `/pdf/2307.01850`

The current page is only the abstract metadata page, not the complete paper content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd045202-a4e9-4022-8820-4f30cf04b1d0",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "ba546859-deb4-4f8f-a61b-96a5759571d9",
  "sourceToolAssistantUUID": "cd045202-a4e9-4022-8820-4f30cf04b1d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T15:01:02.679Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RubqKDAs8msr55C2n2eYce`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2307.01850",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba546859-deb4-4f8f-a61b-96a5759571d9",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2CHUfMxsFxyQ9F11AS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ddbd856-b1bc-4ace-a2ab-b80d7d294820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GS7LUV2bUdwejcwoHJLKLH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 19096,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 503
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 19096,
          "cache_creation_input_tokens": 503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 503,
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

_source line 13 · 2026-05-20T15:01:02.846Z_

<details><summary>↩ Tool result · reported error · `toolu_01RubqKDAs8msr55C2n2eYce`</summary>

```text
maxContentLength size of 10485760 exceeded
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ddbd856-b1bc-4ace-a2ab-b80d7d294820",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "ddd368a4-5749-45ee-a7a4-2e7cbb956a52",
  "toolUseResult": "Error: maxContentLength size of 10485760 exceeded",
  "sourceToolAssistantUUID": "4ddbd856-b1bc-4ace-a2ab-b80d7d294820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T15:01:07.216Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LpS2uqx4RpdGKwHCx6WsrL`</summary>

```json
{
  "url": "https://ar5iv.org/html/2307.01850",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddd368a4-5749-45ee-a7a4-2e7cbb956a52",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2CeZvBkrp6eJUeazGH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84cbbf4f-f57a-4b32-a1fb-e30417d5ffdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017Nar3NGy1rrVinKjXsGVf7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 232,
      "cache_read_input_tokens": 19599,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 232
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 19599,
          "cache_creation_input_tokens": 232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 232,
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

_source line 15 · 2026-05-20T15:01:08.634Z_

<details><summary>↩ Tool result · `toolu_01LpS2uqx4RpdGKwHCx6WsrL`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://ar5iv.org/html/2307.01850
Redirect URL: https://ar5iv.labs.arxiv.org/html/2307.01850
Status: 301 Moved Permanently

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://ar5iv.labs.arxiv.org/html/2307.01850"
- prompt: "Extract the full paper content in detail. I need:
1. Complete introduction section with all paragraphs
2. The contribution statement (usually end of intro)
3. Complete experiment/results section including all tables and figures descriptions
4. Limitations and future work section
5. All figure and table captions
6. All references to figures/tables in the main text
7. Method section key details
8. Baselines, metrics, datasets used
9. Training recipe details (optimizer, lr, hardware, etc.)
Return as much detail as possible."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84cbbf4f-f57a-4b32-a1fb-e30417d5ffdc",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "299153a1-8573-422e-8cfc-5676bd636803",
  "sourceToolAssistantUUID": "84cbbf4f-f57a-4b32-a1fb-e30417d5ffdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T15:01:12.065Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0117eodiV8DqTCyNfv1enGtw`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2307.01850",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "299153a1-8573-422e-8cfc-5676bd636803",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2D4g18nADJqgcveFHJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a36293b3-0c8b-425f-a5c2-b88ea103b455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QU8tuyrDDmYxaXzDrGwFFZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 460,
      "cache_read_input_tokens": 19831,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 460
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 19831,
          "cache_creation_input_tokens": 460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 460,
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

_source line 17 · 2026-05-20T15:01:15.619Z_

<details><summary>↩ Tool result · `toolu_0117eodiV8DqTCyNfv1enGtw`</summary>

```text
# Response

I cannot extract the detailed paper content you requested because the webpage indicates a **fatal conversion error**. The page explicitly states: "Conversion to HTML had a Fatal error and exited abruptly. This document may be truncated or damaged."

The page only displays metadata and navigation elements for arxiv paper 2307.01850, with no actual paper content visible. To access the full paper details (introduction, methods, experiments, results, references, etc.), you would need to:

1. **Visit the original arXiv page** directly at https://arxiv.org/abs/2307.01850
2. **Download the PDF version** from arXiv
3. **Check the conversion report** linked on the page to diagnose the conversion failure

The current HTML version is unusable for content extraction due to the documented conversion failure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a36293b3-0c8b-425f-a5c2-b88ea103b455",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "21e66842-3479-4b4d-a762-6edc41d9ac31",
  "sourceToolAssistantUUID": "a36293b3-0c8b-425f-a5c2-b88ea103b455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T15:01:18.814Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Tfm4XTUDUkQZQKyPgiEiDd`</summary>

```json
{
  "url": "https://openreview.net/forum?id=nXne4PRMVE",
  "prompt": "Extract the full paper content. I need: introduction, contribution statement, methods, experiments, results, baselines, metrics, datasets, training details, limitations. Return as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21e66842-3479-4b4d-a762-6edc41d9ac31",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2DabaHHpHdVTcxqmEb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "556c74c7-fef7-423f-90ae-0ece8c297e95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011AuEFzsQEvuafu3qvPCKZd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 20291,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 399
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 20291,
          "cache_creation_input_tokens": 399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 399,
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

_source line 19 · 2026-05-20T15:01:21.670Z_

<details><summary>↩ Tool result · `toolu_01Tfm4XTUDUkQZQKyPgiEiDd`</summary>

```text
I cannot extract the paper content you've requested because the web page provided is an error page from OpenReview, not an actual research paper.

The page shows: "The Note nXne4PRMVE was not found" - indicating the specific paper reference doesn't exist or is inaccessible on the platform.

To obtain paper details like introduction, methods, experiments, results, datasets, and training information, you would need to:

1. Verify the correct paper ID or URL
2. Access an available paper on OpenReview.net
3. Provide the actual paper content for analysis

If you have a different paper URL or content you'd like me to analyze, please share that instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "556c74c7-fef7-423f-90ae-0ece8c297e95",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "645c76c3-6ca3-4ab4-81ff-d68dc8e7a8d3",
  "sourceToolAssistantUUID": "556c74c7-fef7-423f-90ae-0ece8c297e95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T15:01:24.807Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018NdWotdFSsEGu8rVz5puJM`</summary>

```json
{
  "url": "https://openreview.net/forum?id=ShjMHfmPs0",
  "prompt": "Extract full paper content: introduction, methods, experiments, results, baselines, metrics, datasets, training details, limitations, figure/table captions. Return everything in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "645c76c3-6ca3-4ab4-81ff-d68dc8e7a8d3",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2E2U56WcjnadzckKna",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03a71df1-89e6-4bfa-b0e3-6c108b287ae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012RsVAu4ZnDzC4em6GTf6s6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 20690,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 287
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 20690,
          "cache_creation_input_tokens": 287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 287,
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

_source line 21 · 2026-05-20T15:01:30.181Z_

<details><summary>↩ Tool result · `toolu_018NdWotdFSsEGu8rVz5puJM`</summary>

```text
# Summary of "Self-Consuming Generative Models Go MAD"

Based on the webpage content provided, here's what I can extract:

## Paper Overview
This ICLR 2024 poster paper by Alemohammad et al. investigates a critical phenomenon in generative AI: the recursive training of models on synthetic data.

## Core Contribution
The authors introduce the concept of **Model Autophagy Disorder (MAD)**, demonstrating that "generative models recursively trained on synthetic data are doomed to have their quality or diversity progressively decrease" without sufficient fresh real data at each generation.

## Research Focus
- **Primary subject**: Autophagous loops in generative models (self-consuming training cycles)
- **Models studied**: State-of-the-art generative image models
- **Key finding**: Quality (precision) or diversity (recall) degrades across generations when real training data becomes limited

## Methodology Indicators
The paper conducts both analytical and empirical analysis examining three families of autophagous loops, varying how fresh real data remains available and whether previous samples traded quality for diversity.

## Keywords
Generative Models, Synthetic Data, Sampling Bias, Diffusion Models, GANs

## Data Availability
Supplementary material is available for download. Code details are anonymized per double-blind review standards.

**Note**: The webpage excerpt does not contain the full paper sections (introduction, methods, experiments, results, tables/figures). To access complete technical details, the full PDF would be required.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03a71df1-89e6-4bfa-b0e3-6c108b287ae6",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "6a489400-d0a2-45cb-be75-fa60d567ba81",
  "sourceToolAssistantUUID": "03a71df1-89e6-4bfa-b0e3-6c108b287ae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T15:01:33.828Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VYLcV6DFKeawUurjWNi5v3`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=ShjMHfmPs0",
  "prompt": "Extract the full paper content in detail. I need:\n1. Complete introduction section with all paragraphs\n2. The contribution statement (usually end of intro)\n3. Complete experiment/results section including all tables and figures descriptions\n4. Limitations and future work section\n5. All figure and table captions\n6. All references to figures/tables in the main text\n7. Method section key details\n8. Baselines, metrics, datasets used\n9. Training recipe details (optimizer, lr, hardware, etc.)\nReturn as much detail as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a489400-d0a2-45cb-be75-fa60d567ba81",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2Eer6Ty51rnM7YJH3R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fdeed22-a9f3-45a8-baa1-9356038d6e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01635QpswaER39BDZmcsojig",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 20977,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 472
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 20977,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 472,
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

_source line 23 · 2026-05-20T15:01:35.225Z_

<details><summary>↩ Tool result · reported error · `toolu_01VYLcV6DFKeawUurjWNi5v3`</summary>

```text
maxContentLength size of 10485760 exceeded
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fdeed22-a9f3-45a8-baa1-9356038d6e19",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "e688a91c-0378-4dcd-8384-ae760b9cc824",
  "toolUseResult": "Error: maxContentLength size of 10485760 exceeded",
  "sourceToolAssistantUUID": "5fdeed22-a9f3-45a8-baa1-9356038d6e19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T15:01:38.343Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017gzJgJcJZr1JXF2rUCU7BE`</summary>

```json
{
  "url": "https://proceedings.mlr.press/v235/alemohammad24a.html",
  "prompt": "Extract the full paper content in detail: introduction, contribution statement, methods, experiments, results tables and figures, limitations, baselines, metrics, datasets, training recipe. Return maximum detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e688a91c-0378-4dcd-8384-ae760b9cc824",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2F2NeZp4WA3rKbdsUc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0f5ce89-d6a7-4be8-b585-a5a2d5aac6be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XY9sFRGLUp5m4orFkRyndW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 21449,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 238
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 21449,
          "cache_creation_input_tokens": 238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 238,
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

_source line 25 · 2026-05-20T15:01:38.786Z_

<details><summary>↩ Tool result · reported error · `toolu_017gzJgJcJZr1JXF2rUCU7BE`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0f5ce89-d6a7-4be8-b585-a5a2d5aac6be",
  "isSidechain": true,
  "promptId": "1da41794-e339-4608-bf95-c667636bcab8",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "f9d04f90-1541-4f6b-93d2-09f179466ede",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "e0f5ce89-d6a7-4be8-b585-a5a2d5aac6be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T15:01:41.869Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RvCbuN346u7y9dACWggVzK`</summary>

```json
{
  "url": "https://iclr.cc/virtual/2024/poster/17896",
  "prompt": "Extract the full paper content in detail: introduction, contribution statement, methods, experiments, results tables and figures, limitations, baselines, metrics, datasets, training recipe. Return maximum detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9d04f90-1541-4f6b-93d2-09f179466ede",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2FHcvhjGeQVyMBntYm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a30baca-d6a7-4b7c-bf58-7f0106a47f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012VZKTYgnQkWPexU5teJzZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 151,
      "cache_read_input_tokens": 21687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 151,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 27 · 2026-05-20T15:01:48.208Z_

<details><summary>↩ Tool result · `toolu_01RvCbuN346u7y9dACWggVzK`</summary>

```text
# Paper Summary: Beyond Task Performance in Large Multimodal Models

## Overview
The webpage provides limited detailed content about this ICLR 2024 poster paper. The available information includes only the abstract and basic metadata, not the full paper with sections typically needed for comprehensive extraction.

## What's Available

**Paper Title:** "Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning"

**Authors:** Mustafa Shukor, Alexandre Rame, Corentin Dancette, Matthieu Cord

**Evaluation Axes Studied:** The research examines models across five dimensions: hallucinations, abstention, compositionality, explainability, and instruction following.

**Models Evaluated:** The study analyzes "10 recent open-source LMMs from 3B up to 80B parameter scale."

## Key Findings Mentioned

The abstract highlights three main conclusions:

1. "LMMs have flaws that remain unsolved with scaling alone"
2. In-context learning shows mixed results—improving some aspects like explainability while amplifying hallucinations
3. Proposed variants including "Multitask-ICL, Chain-of-Hindsight-ICL, and Self-Correcting-ICL" show promise

## Resources Referenced
- Project page available at evalign-icl.github.io
- Code repository: https://github.com/mshukor/EvALign-ICL
- Full paper accessible via OpenReview

**Limitation:** The webpage excerpt doesn't contain detailed methodology, experimental results, tables, figures, or comprehensive discussion sections needed for complete technical analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a30baca-d6a7-4b7c-bf58-7f0106a47f1b",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "01435487-c8fb-41a5-9189-b87eeae559f2",
  "sourceToolAssistantUUID": "6a30baca-d6a7-4b7c-bf58-7f0106a47f1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T15:01:50.701Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0192JQPcDC5YLvdpSrQLwTnA`</summary>

```json
{
  "url": "https://huggingface.co/papers/2307.01850",
  "prompt": "Extract the full paper content in detail: introduction, contribution statement, methods, experiments, results tables and figures, limitations, baselines, metrics, datasets, training recipe. Return maximum detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01435487-c8fb-41a5-9189-b87eeae559f2",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2FyscQ48PjVfGyRmu3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdc048c1-6d13-4c1f-ba2f-b18d73aab761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0164Nmrjx9RT1mPfd4gjumeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 21838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 504,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 29 · 2026-05-20T15:01:51.437Z_

<details><summary>↩ Tool result · `toolu_0192JQPcDC5YLvdpSrQLwTnA`</summary>

```text
&lt;persisted-output>
Output too large (83.6KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-distiller-3275b75a/e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae/tool-results/toolu_0192JQPcDC5YLvdpSrQLwTnA.txt

Preview (first 2KB):
# Self-Consuming Generative Models Go MAD

Sina Alemohammad,&lt;sup>†\*&lt;/sup> Josue Casco-Rodriguez,&lt;sup>†\*&lt;/sup> Lorenzo Luzi,&lt;sup>†&lt;/sup> Ahmed Imtiaz Humayun,&lt;sup>†&lt;/sup>

Hossein Babaei,&lt;sup>†&lt;/sup> Daniel LeJeune,&lt;sup>‡&lt;/sup> Ali Siahkooi,&lt;sup>§&lt;/sup> Richard G. Baraniuk&lt;sup>†&lt;/sup>

&lt;sup>†&lt;/sup>Department of Electrical and Computer Engineering, Rice University

&lt;sup>‡&lt;/sup>Department of Statistics, Stanford University

&lt;sup>§&lt;/sup>Department of Computational Applied Mathematics and Operations Research, Rice University

## Abstract

Seismic advances in generative AI algorithms for imagery, text, and other data types has led to the temptation to use synthetic data to train next-generation models. Repeating this process creates an autophagous (“self-consuming”) loop whose properties are poorly understood. We conduct a thorough analytical and empirical analysis using state-of-the-art generative image models of three families of autophagous loops that differ in how fixed or fresh real training data is available through the generations of training and in whether the samples from previous-generation models have been biased to trade off data quality versus diversity. Our primary conclusion across all scenarios is that *without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease*. We term this condition Model Autophagy Disorder (MAD), making analogy to mad cow disease.

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdc048c1-6d13-4c1f-ba2f-b18d73aab761",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "ee708788-bfdb-4e00-86cf-7e2244031764",
  "sourceToolAssistantUUID": "cdc048c1-6d13-4c1f-ba2f-b18d73aab761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T15:01:54.398Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MHqiZUL6B76SwfB8j4VDsB`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-distiller-3275b75a/e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae/tool-results/toolu_0192JQPcDC5YLvdpSrQLwTnA.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee708788-bfdb-4e00-86cf-7e2244031764",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2GDgKLNyum2A6NenJe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbbfcbeb-b8c1-43e2-97d8-323f05613483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XBE4cqmL5TyhkTzpNo27k3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 22342,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 678
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 22342,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 678,
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

_source line 31 · 2026-05-20T15:01:54.676Z_

<details><summary>↩ Tool result · `toolu_01MHqiZUL6B76SwfB8j4VDsB`</summary>

```text
1	# Self-Consuming Generative Models Go MAD
2	
3	Sina Alemohammad,&lt;sup>†\*&lt;/sup> Josue Casco-Rodriguez,&lt;sup>†\*&lt;/sup> Lorenzo Luzi,&lt;sup>†&lt;/sup> Ahmed Imtiaz Humayun,&lt;sup>†&lt;/sup>
4	
5	Hossein Babaei,&lt;sup>†&lt;/sup> Daniel LeJeune,&lt;sup>‡&lt;/sup> Ali Siahkooi,&lt;sup>§&lt;/sup> Richard G. Baraniuk&lt;sup>†&lt;/sup>
6	
7	&lt;sup>†&lt;/sup>Department of Electrical and Computer Engineering, Rice University
8	
9	&lt;sup>‡&lt;/sup>Department of Statistics, Stanford University
10	
11	&lt;sup>§&lt;/sup>Department of Computational Applied Mathematics and Operations Research, Rice University
12	
13	## Abstract
14	
15	Seismic advances in generative AI algorithms for imagery, text, and other data types has led to the temptation to use synthetic data to train next-generation models. Repeating this process creates an autophagous (“self-consuming”) loop whose properties are poorly understood. We conduct a thorough analytical and empirical analysis using state-of-the-art generative image models of three families of autophagous loops that differ in how fixed or fresh real training data is available through the generations of training and in whether the samples from previous-generation models have been biased to trade off data quality versus diversity. Our primary conclusion across all scenarios is that *without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease*. We term this condition Model Autophagy Disorder (MAD), making analogy to mad cow disease.
16	
17	**Figure 1: Training generative artificial intelligence (AI) models on synthetic data progressively amplifies artifacts.** As synthetic data from generative models proliferates on the Internet and in standard training datasets, future models will likely be trained on some mixture of real and synthetic data, forming an *autophagous* (“self-consuming”) loop. Here we highlight one potential unintended consequence of autophagous training. We trained a succession of StyleGAN-2 [1] generative models such that the training data for the model at generation  $t \geq 2$  was obtained by synthesizing images from the model at generation  $t - 1$ . This particular setup corresponds to a **fully synthetic loop** in Figure 3. Note how the cross-hatched artifacts (possibly an architectural *fingerprint*) are progressively amplified in each new generation. Additional samples are provided Appendices C and D.
18	
19	&lt;sup>\*&lt;/sup>Equal contribution.# 1 Introduction
20	
21	## 1.1 Generative models are training on synthetic data from generative models
22	
23	Due to rapid advances in *generative artificial intelligence (AI)*, synthetic data of all kinds is rapidly proliferating. Publicly available generative models have not only revolutionized the image, audio, and text domains [2–9], but they are also starting to impact the creation of videos, 3D models, graphs, tables, software, and even websites [10–15]. Companies like Google, Microsoft, and Shutterstock are incorporating generative models into their consumer services, and the output from these services and popular generative models like Stable Diffusion [2] (for images) and ChatGPT [16] (for text) tend to end up on the Internet. The world is racing towards a future that is best summarized by a comment overheard at the 2022 ICLR conference: “There will soon be more synthetic data than real data on the Internet.”
24	
25	Since the training datasets for generative AI models tend to be sourced from the Internet, today’s AI models are unwittingly being trained on increasing amounts of AI-synthesized data. Indeed, Figure 2 demonstrates that the popular LAION-5B dataset [17], which is used to train state-of-the-art text-to-image models like Stable Diffusion [2], contains synthetic images sampled from several earlier generations of generative models. Formerly human sources of text are now increasingly created by generative AI models, from user reviews [18] to news websites [15], often with no indication that the text is synthesized [19]. As the use of generative models continues to grow rapidly, this situation will only accelerate.
26	
27	Moreover, throwing caution to the wind, AI-synthesized data is increasingly used by choice in a wide range of applications [9, 20–24], for a number of reasons. First, it can be much easier, faster, and cheaper to synthesize training data rather than source real-world samples, particularly for data-scarce applications. Second, in some situations synthetic data augmentation has been found empirically to boost AI system performance [25–27]. Third, synthetic data can protect privacy [27–29] in sensitive applications like medical imaging or medical record aggregation [29, 30]. Fourth, and most importantly, as deep learning models become increasingly enormous, we are simply running out of real data on which to train them [31–33]. Interestingly, not only have practitioners begun deliberately training AI systems on synthetic data, but also the human annotators who provide gold-standard annotations for supervised learning tasks are increasingly using generative models to increase their productivity and income [34].
28	
29	The witting or unwitting use of synthetic data to train generative models departs from standard AI training practice in one important respect: repeating this process for generation after generation of models forms an **autophagous (“self-consuming”) loop**. As Figure 3 details, different autophagous loop variations arise depending on how existing real and synthetic data are combined into future training sets. Additional variations arise depending on how the synthetic data is generated. For instance, practitioners or algorithms will often introduce a *sampling bias* by manually “cherry picking” synthesized data to trade off perceptual *quality* (i.e., the images/texts “look/sound good”) vs. *diversity* (i.e., many different “types” of images/texts are generated). The informal concepts of quality and diversity are closely related to the statistical metrics of *precision* and *recall*, respectively [39]. If synthetic data, biased or not, is already in our training datasets today, then autophagous loops are all but inevitable in the future.
30	
31	No matter what the training set makeup or sampling method, the potential ramifications of autophagous loops on the properties and performance of generative models is poorly understood. In one direction, repeated training with synthetic data might progressively amplify the biases and artifacts present in any generative model. We hypothesize that synthetic data contains *fingerprints* of the generator architecture (e.g., convolutional traces [40] or aliasing artifacts [41]) that may be reinforced by self-consuming generators. To illustrate this, in Figure 1 we present samples generated by StyleGAN-2 generative models after repeated training on synthetic data. Each generation results in a progressive amplification of cross-hatching artifacts, which are reminiscent of aliasing in StyleGAN-2 as suggested by [41]. In another direction, autophagous loops featuring generative models tuned to produce high quality syntheses at the expense of diversity (such as [1, 42]) might progressively dilute the diversity of the data on the Internet. The closest exploration to this potential outcome has been the issue of *diversity exposure* in recommender systems, where some studies have shown that, if a recommendation system is tuned for maximum click rate, then an echo chamber results, and users lose exposure to diverse ideas. [43–47]. Other studies have shown that, subjectFigure 2: **Today’s large-scale image training datasets contain synthetic data from generative models.** Datasets such as LAION-5B [17], which is oft-used to train text-to-image models like Stable Diffusion [2], contain synthetic images sampled from earlier generations of generative models. Pictured here are representative samples from LAION-5B that include (clockwise from upper left and highlighted in red) synthetic images from the generative models StyleGAN [1], AICAN [35], Pix2Pix [36], DALL-E [37], and BigGAN [38]. We found these images using simple queries on [haveibeentrained.com](https://haveibeentrained.com). Generative models trained on the LAION-5B dataset are thus closing an autophagous (“self-consuming”) loop (see Figure 3) that can lead to progressively amplified artifacts (recall Figure 1), lower quality (precision) and diversity (recall), and other unintended consequences.
32	
33	to the recommendation logic, the echo chamber effect might not be as pronounced [48] and could be on par with that produced by human curators [49]. Exactly how the above and other unintended consequences could emerge from autophagous loops deserves thorough consideration and study.
34	
35	For analogies and cautionary tales, one may turn to mathematics and biology. In the language of mathematics, at one extreme, an autophagous loop is a *contraction mapping* that collapses to a single, boring, point, while at the other extreme it is an unstable *positive feedback loop* that diverges into bedlam. Biology provides a particularly apt “seemed like a good idea at the time” in the practice of feeding cattle with the remains (including brains) of other cattle. The resulting autophagous loop led to *mad cow disease* [50], a fatal neurodegenerative disease that eventually spread to humans before a massive intervention brought it under control. Lest an analogous malady disrupt the AI future, and to coin a term, it seems prudent to understand what can be done to prevent generative models from developing *Model Autophagy Disorder (MAD)*.
36	
37	## 1.2 Contributions
38	
39	In this paper, we conduct a careful theoretical and empirical study of AI autophagy from the perspective of generative image models. While we focus on image data for concreteness, the concepts developed herein apply to any data type, including text and Large Language Models (LLMs). This paper is an elaboration of work initially published in [51, 52]; while it was being finalized, we became aware of contemporaneous work in [53] and [54, 55] that explores certain aspects of our more general theory. We will discuss the results of these papers in context below.
40	
41	Let us summarize the three key contributions and findings that lie at the focus of this paper:
42	
43	**Realistic models for autophagous loops.** We propose three families of increasingly complex self-consuming training loops that realistically model the way real and synthetic data are combined into autophagous training datasets for generative models (recall Figure 3):
44	
45	- • **The fully synthetic loop**, wherein the training dataset for each generation’s model consists solely of synthetic data sampled from previous generations’ models. This case arises inFigure 3: **Recursively training generative models on synthetic data sampled from other generative models results in an autophagous (“self-consuming”) loop.** In this paper, we study three variations of autophagous loops: the *fully synthetic loop*, where a generative model is trained on only synthetic samples from previous generations (complete cycles through the loop); the *synthetic augmentation loop*, where the training set also includes a fixed set of real data; and the *fresh data loop*, where the training set also includes a fresh set of real data each generation. See Section 2.2 for precise definitions. Crucially, the generative samples are potentially obtained from a biased sampling process controlled by parameter  $\lambda$  that trades off sample quality vs. diversity.
46	
47	practice, for example, when iteratively fine-tuning a generative model on its own high-quality outputs (e.g., [56]). We show below in Section 3 that in this case *either the quality (precision) or the diversity (recall) of the generative models decreases over generations.*
48	
49	- • **The synthetic augmentation loop**, wherein the training dataset for each generation’s model consists of a combination of synthetic data sampled from previous generations’ models plus a fixed set of real training data. This case arises in practice, for example, in model “self-improvement,” where a model’s training data are augmented with synthetic data from some other models (e.g., [57]). We show below in Section 4 that in this case *fixed real training data only delays the inevitable degradation of the quality or diversity of the generative models over generations.*
50	- • **The fresh data loop**, wherein the training dataset for each generation’s model consists of a combination of synthetic data sampled from previous generations’ models plus a fresh set of real training data. This case models, for example, the standard practice where training datasets are acquired by scraping the Internet, which will find both real and synthetic data (recall Figure 2). We show below in Section 5 that in this case, *with enough fresh real data, the quality and diversity of the generative models do not degrade over generations.*
51	
52	The bottom line across all three autophagous loop models is that *without enough fresh real data each generation, future generative models are doomed to go MAD.*
53	
54	**Sampling bias plays a key rôle in autophagous loops.** Users of generative models tend to manually curate (“cherry-pick”) their synthetic data, preferring high-quality samples and rejecting low-quality ones. Moreover, state-of-the-art generative models typically feature controllable parameters that can increase synthetic quality at the expense of diversity [42, 58]. We demonstrate that the sampling biases induced through such quality-diversity (precision-recall) trade-offs have a major impact on the behavior of an autophagous training loop. Specifically, we show that, without sampling bias, autophagy can lead to a rapid decline of both quality and diversity, whereas, with sampling bias, quality can be maintained but diversity degrades even more rapidly.
55	
56	**Autophagous loop behaviors hold across a variety of generative models and datasets.** In addition to our analytical and empirical studies on simple multivariate Gaussian and Gaussian mixture models, we demonstrate in the main text and Appendix that our main conclusions hold across a variety of generative models, including Denoising Diffusion Probabilistic Models (DDPM) [59], StyleGAN-2 [58], WGAN [60], and Normalizing Flows [61] trained on a number of image datasets, including MNIST [62] and FFHQ [63].This paper is organized as follows. In Section 2, we rigorously define the concept of an autophagous loop, explain our universal biased sampling parameter  $\lambda$  for generative models, and define the metrics we will use to measure the quality and diversity of a generative model. Then, in Sections 3, 4, and 5, we study the **fully synthetic loop**, **synthetic augmentation loop**, and **fresh data loop** models, respectively. We conclude with a discussion in Section 6. We report on the results of numerous additional experiments in various Appendices.
57	
58	## 2 Self-consuming generative models
59	
60	Modern generative models have advanced rapidly in their ability to synthesize realistic data (signals, images, videos, text, and beyond) given a finite collection of training samples from a reference (target) probability distribution  $\mathcal{P}_r$ . As generative models have proliferated, the datasets for training new models have unwittingly (see [17] and Figure 2) or wittingly [57, 64–67] begun to include increasing amounts of synthetic data in addition to “real world” samples from  $\mathcal{P}_r$  (recall Figure 3).&lt;sup>2&lt;/sup> In this section, we propose a hierarchy of increasingly realistic models for this *autophagy* (self-consuming) phenomenon that will enable us to draw a number of conclusions about the potential ramifications for generative modeling as synthetic training data proliferates.
61	
62	### 2.1 Autophagous processes
63	
64	Consider a sequence of generative models  $(\mathcal{G}^t)_{t \in \mathbb{N}}$ , where the goal is to train each model to approximate a reference probability distribution  $\mathcal{P}_r$ . At each *generation*  $t \in \mathbb{N}$ , the model  $\mathcal{G}^t$  is trained from scratch on the dataset  $\mathcal{D}^t = (\mathcal{D}_r^t, \mathcal{D}_s^t)$  comprised of both  $n_r^t$  *real data samples*  $\mathcal{D}_r^t$  drawn from  $\mathcal{P}_r$  and  $n_s^t$  *synthetic data samples*  $\mathcal{D}_s^t$  produced by already trained generative model(s). The first-generation model  $\mathcal{G}^1$  is trained on purely real data, i.e.,  $n_s^1 = 0$ .
65	
66	**Definition.** An *autophagous generative process* is a sequence of distributions  $(\mathcal{G}^t)_{t \in \mathbb{N}}$  where each generative model  $\mathcal{G}^t$  is trained on data that includes samples from previous models  $(\mathcal{G}^\tau)_{\tau=1}^{t-1}$ .
67	
68	In this work, we study cases where such a process deteriorates (goes “MAD”) over time. Let  $\text{dist}(\cdot, \cdot)$  denote some distance metric on distributions.
69	
70	**Definition.** A *MAD generative process* is a sequence of distributions  $(\mathcal{G}^t)_{t \in \mathbb{N}}$  that follows a random walk such that  $\mathbb{E}[\text{dist}(\mathcal{G}^t, \mathcal{P}_r)]$  increases with  $t$ .
71	
72	**Claim.** Under mild conditions, an autophagous generative process is a MAD generative process.
73	
74	By studying whether a sequence of generative models  $(\mathcal{G}^t)_{t \in \mathbb{N}}$  forms a MAD generative process, we can gain insights into the potentially detrimental effects of training generative models on synthetic data.
75	
76	Two critical aspects can drive an autophagous process MAD: The balance of real and synthetic data in the training set (Section 2.2) and the manner in which synthetic data is sampled from the generative models (Section 2.3).
77	
78	### 2.2 Variants of autophagous processes
79	
80	In this paper, we study three realistic autophagous mechanisms, each of which includes synthetic data and potentially real data in a feedback loop (recall Figure 3). We now add some additional details to the descriptions from Section 1.2:
81	
82	- • **The fully synthetic loop:** In this scenario, each model  $\mathcal{G}^t$  for  $t \geq 2$  is trained exclusively on synthetic data sampled from models  $(\mathcal{G}^\tau)_{\tau=1}^{t-1}$  from previous generations, i.e.,  $\mathcal{D}^t = \mathcal{D}_s^t$ .
83	- • **The synthetic augmentation loop:** In this scenario, each model  $\mathcal{G}^t$  for  $t \geq 2$  is trained on a dataset  $\mathcal{D}^t = (\mathcal{D}_r, \mathcal{D}_s^t)$  consisting of a fixed set of real data  $\mathcal{D}_r$  sampled from  $\mathcal{P}_r$  plus synthetic data  $\mathcal{D}_s^t$  from models from previous generations.
84	
85	&lt;sup>2&lt;/sup>While the term “real” implies non-synthetic data from the “real-world” (e.g., a photographic image of a natural scene), in general, real data is any data drawn from the reference distribution  $\mathcal{P}_r$ .- • **The fresh data loop:** In this scenario, each model  $\mathcal{G}^t$  for  $t \geq 2$  is trained on a dataset  $\mathcal{D}^t = (\mathcal{D}_r^t, \mathcal{D}_s^t)$  consisting of a fresh set of real data  $\mathcal{D}_r^t$  drawn independently from  $\mathcal{P}_r$  plus synthetic data  $\mathcal{D}_s^t$  from models from previous generations.
86	
87	### 2.3 Biased sampling in autophagous loops
88	
89	While the above three autophagous loops realistically mimic real-world generative model training scenarios that involve synthetic data, it is also critical to consider how each generation’s synthetic data is produced. In particular, not all synthetic samples from a generative model will have the same level of fidelity to the training distribution, or “quality.” Consequently, in many applications (e.g., art generation), practitioners “cherry-pick” synthetic samples based on a manual evaluation of perceived quality. It can be argued that most of the synthetic images that one can find on the Internet today are to some degree cherry-picked based on human evaluation of perceptual quality. Therefore, it is critical that this notion be included in the modeling and analysis of autophagous loops.
90	
91	In our modeling and analysis, we implement cherry-picking via the *biased sampling* methods that are commonly used in generative modeling practice, such as truncation in BigGAN and StyleGAN [38, 58], guidance in diffusion models [42], polarity sampling [68], and temperature sampling in large language models [7]. These techniques assume that the data manifold is better approximated in the higher density regions of the learned distribution. By biasing a generative model’s synthetic samples to be drawn from parts of the learned generative model distribution  $\mathcal{G}^t$  that are closer to its modes, these methods increase sample fidelity or quality by trading off the variety or diversity of the synthesized data [68].
92	
93	We employ a number of generative models in our experiments below; each has a unique controllable parameter to increase sample quality. We unify these parameters in the universal *sampling bias parameter*  $\lambda \in [0, 1]$ , where  $\lambda = 1$  corresponds to unbiased sampling and  $\lambda = 0$  corresponds to sampling from the modes of the generative distribution  $\mathcal{G}^t$  with zero variance. The exact interpretation of  $\lambda$  differs across various models, but in general synthetic sample quality will increase and diversity decrease as  $\lambda$  is decreased from 1. Below we provide specific definitions for  $\lambda$  for the various generative models we consider in this paper:
94	
95	- • **Gaussian model:** Our theoretical analysis and simplified experiments use a multivariate Gaussian toy model. To implement biased sampling at generation  $t$ , we estimate the mean  $\mu_t$  and covariance  $\Sigma_t$  of the training data and then sample from the distribution  $\mathcal{N}(\mu_t, \lambda \Sigma_t)$ . As  $\lambda$  decreases, we draw samples closer to the mean  $\mu_t$ .
96	- • **Generative adversarial network:** In our StyleGAN experiments, we use the truncation parameter to increase sampling quality. Style-based generative networks employ a secondary latent space called the style-space. When using truncation during inference, latent vectors in the style-space are linearly interpolated towards the mean of the style-space latent distribution. We denote the truncation factor by  $\lambda$ ; as  $\lambda$  is decreased from 1, samples are drawn closer to the mean of the style-space distribution.
97	- • **Denoising diffusion probabilistic model (DDPM):** For conditional diffusion models, we use classifier-free diffusion guidance [42] to bias the sampling towards higher probability regions. We use 10% conditioning dropout during training to enable classifier-free guidance. We define the bias parameter  $\lambda$  in terms of the guidance factor  $w$  from [42] as  $\lambda = \frac{1}{1+w}$ . When  $\lambda = 1$ , the network acts as a conventional conditional diffusion model with no guidance. As  $\lambda$  decreases, the diffusion model samples more closely to the modes of the unconditional distribution, producing higher-quality samples.
98	
99	### 2.4 Metrics for MADness
100	
101	Ascertaining whether an autophagous loop has gone MAD or not (recall Definition 2.1) requires that we measure how far the synthesized data distribution  $\mathcal{G}^t$  has drifted from the true data distribution  $\mathcal{P}_r$  over the generations  $t$ . We use the notion of the Wasserstein distance (WD) as implemented by the Fréchet Inception Distance (FID) for this purpose. We will also find the standard concepts of precision and recall useful for making rigorous the notions of quality and diversity, respectively.
102	
103	**Wasserstein distance (WD)**, or earth mover’s or optimal transport distance [69], measures the minimum work required to move the probability mass of one distribution to another. Computingthe Wasserstein distance between two datasets (e.g., real and synthetic images) is prohibitively expensive. As such, standard practice employs the Fréchet Inception Distance (FID) [70] as an approximation, which calculates the Wasserstein-2 distance between inception feature distributions of real and synthetic images.
104	
105	**Precision** quantifies the portion of synthesized samples that are deemed high *quality* or visually appealing. We use precision as an indicator of sample quality. We compute precision by calculating the fraction of synthetic samples that are closer to a real data example than to their  $k$ -th nearest neighbor [39]. We use  $k = 5$  in all experiments.
106	
107	**Recall** estimates the fraction of samples in a reference distribution that are inside the support of the distribution learned by a generative model. High recall scores suggest that the generative model captures a large portion of *diverse* samples from the reference distribution. We compute recall in a manner similar to precision [39]. Given a set of synthetic samples from the generative model, we calculate the fraction of real data samples that are closer to any synthetic sample than its  $k$ -th nearest neighbor.
108	
109	## 2.5 Related work
110	
111	Contemporaneous work on feedback loops in generative modeling has explored certain aspects of our more general theory that confirm our main conclusions.
112	
113	In [53], the authors show that, for the **fully synthetic loop** without sampling bias, variational autoencoders (VAE) and Gaussian mixture models result in MAD generative processes. They also investigate training loops resembling the **synthetic augmentation loop** and **fresh data loop**, again without sampling bias, on LLMs. However, they take a slightly different approach from ours by fine-tuning the generative model with synthetic data instead of training from scratch. Their studies demonstrate that both the **synthetic augmentation loop** and **fresh data loop** can result in a decline in performance in fine-tuned LLMs over generations.
114	
115	In [54], the authors focus on the **fully synthetic loop** with sampling bias by utilizing a diffusion model with guidance and report that it prevents a drop in image quality. In [55], the same authors show that a **synthetic augmentation loop** containing a Denoising diffusion implicit model (DDIM) [71] without sampling bias leads to poor performance over generations. The results in [53–55] report some certain facets of a MAD generative process that align with our analytical and experimental results.
116	
117	## 3 The fully synthetic loop: Training exclusively on synthetic data leads to MADness
118	
119	Here we thoroughly analyze the **fully synthetic loop**, wherein each model is trained using synthesized data from the previous generations. We focus on the inter-generational propagation of non-idealities resulting from estimation errors and sampling biases. Specifically, we pinpoint the primary source of these non-idealities and characterize the convergence of the loop. The simplicity of the **fully synthetic loop** means that it does not accurately reflect the reality of generative modeling practice. However, one specific example of this case is when generative models are fine-tuned on their own high-quality outputs [56]. Nevertheless, this loop is in a sense the worst case and so offers valuable insights that can be extrapolated to the more practical autophagous loops discussed in subsequent sections.
120	
121	Our analysis and experiments below support our main conclusion for the **fully synthetic loop**, which can be summarized as *either the quality (precision) or the diversity (recall) of the generative models decreases over generations*.
122	
123	### 3.1 Warm up: Gaussian data and martingales
124	
125	In this section, we focus the **fully synthetic loop** and a Gaussian reference distribution and show that its martingale nature makes it a MAD generative process.
126	
127	Consider a reference (real data) distribution  $\mathcal{P}_r = \mathcal{N}(\mu_0, \Sigma_0)$  for some  $\mu_0 \in \mathbb{R}^d$  and  $\Sigma_0 \in \mathbb{R}^{d \times d}$ , and let our generation process also be Gaussian:  $\mathcal{G}^t = \mathcal{N}(\mu_t, \Sigma_t)$ . At each time  $t \in \mathbb{N}$ , we sample  $n_s$  vectors from  $\mathcal{G}^{t-1}$  with sampling bias  $\lambda \leq 1$ ; that is, we draw  $X_t^1, \dots, X_t^{n_s} \stackrel{\text{iid}}{\sim} \mathcal{N}(\mu_{t-1}, \lambda \Sigma_{t-1})$ .We then use these vectors to construct the unbiased sample mean and covariance to fit the next model  $\mathcal{G}^t$ :
128	
129	$$\mu_t = \frac{1}{n_s} \sum_{i=1}^{n_s} X_t^i, \quad \Sigma_t = \frac{1}{n_s - 1} \sum_{i=1}^{n_s} (X_t^i - \mu_t)(X_t^i - \mu_t)^\top. \quad (1)$$
130	
131	In this case, we also know the distributions of these parameters. We have  $\mu_t \sim \mathcal{N}(\mu_{t-1}, \frac{\lambda}{n_s} \Sigma_{t-1})$  and  $\Sigma_t \sim \mathcal{W}_d(\frac{\lambda}{n_s - 1} \Sigma_{t-1}, n_s - 1)$ , with  $\mathcal{W}_d$  being the Wishart distribution. The process satisfies
132	
133	$$\mathbb{E}[\mu_t | \mu_{t-1}] = \mu_{t-1} \quad \text{and} \quad \mathbb{E}[\Sigma_t | \Sigma_{t-1}] = \lambda \Sigma_{t-1}, \quad (2)$$
134	
135	which means that  $\mu_t$  and  $\Sigma_t$  are *martingale* and *supermartingale* processes, respectively [72]. Due to the uncertainty in estimation of  $\mu_t$  due to the limited sample size,  $\mu_t$  is a Gaussian random walk that will tend to drift from  $\mu_0$  over time, randomly biasing the distribution estimate. Moreover, due to being a bounded supermartingale, the covariance  $\Sigma_t$  is guaranteed to converge to zero. The proof of the following result can be found in Appendix A.
136	
137	**Proposition.** *For the random process defined in Equation (1), for any  $\lambda \leq 1$ , we have  $\Sigma_t \xrightarrow{\text{a.s.}} 0$ .*
138	
139	That is, when fitting a distribution to data sampled from that distribution repeatedly, not only should we expect some modal drift because of the random walk in  $\mu_t$  (reduction in *quality*), but we will also inevitably experience a collapse of the variance (vanishing of *diversity*).
140	
141	The key idea to takeaway from this is that these effects—the random walk and the variance collapse—are solely due to the estimation error of fitting the model parameters using random data. Importantly, this result holds true even when there is no sampling bias (i.e.,  $\lambda = 1$ ). The magnitudes of the steps of the random walk in  $\mu_t$  are determined by two main factors: the number of samples  $n_s$  and the covariance  $\Sigma_t$ . Unsurprisingly, the larger the  $n_s$ , the smaller the steps of the random walk, since there will be less estimation error. This will also slow the convergence of  $\Sigma_t$  to 0. Meanwhile,  $\Sigma_t$  can be controlled using a sampling bias factor  $\lambda < 1$ . The smaller the choice of  $\lambda$ , the more rapidly  $\Sigma_t$  will converge to zero, stopping the random walk of  $\mu_t$  (as illustrated in 17). Thus, the sampling bias factor  $\lambda$  provides a trade-off to preserve quality at the expense of diversity.
142	
143	It was recently shown in related work [53] that the expected Wasserstein-2 metric  $\mathbb{E}[\text{dist}(\mathcal{G}^t, \mathcal{P}_r)]$ , or distributional distance, is increasing for this process. This supports our conclusion that  $\mathcal{G}^t$  is a MAD generative process.
144	
145	### 3.2 Experimental setups for the fully synthetic loop
146	
147	Here we simulate the **fully synthetic loop** using two widely used types of deep generative models. Recall that the **fully synthetic loop** first requires training an initial model  $\mathcal{G}^1$  with a fully real dataset containing  $n_r^1$  samples. In our experiments, all subsequent models  $(\mathcal{G}^t)_{t=2}^\infty$  are trained using only  $n_s^t$  synthetic samples from the immediately preceding model  $\mathcal{G}^{t-1}$ , where each synthetic sample is produced with sampling bias  $\lambda$ . Our primary experiments are organized as follows:
148	
149	- • **Denoising diffusion probabilistic model:** We use a conditional DDPM [59] with  $T = 500$  diffusion time steps and train it on the MNIST dataset. In this experiment the synthetic dataset  $\mathcal{D}_s^t$  is only sampled from the previous generation  $\mathcal{G}^{t-1}$ , with  $n_r^1 = n_s^t = 60k$  for  $t \geq 2$ .&lt;sup>3&lt;/sup>
150	- • **Generative adversarial network:** We use unconditional StyleGAN2 architecture [58] and train it on the FFHQ dataset [63]. The images have been downsized to  $128 \times 128$  to reduce the computational cost. Like the previous experimental setup, the synthetic samples are sampled from the previous generation with  $n_r^1 = n_s^t = 70k$  for  $t \geq 2$ .
151	
152	### 3.3 Without sampling bias, the quality of synthetic data decreases
153	
154	Let us first investigate the **fully synthetic loop** without any sampling bias ( $\lambda = 1$ ). In higher-dimensional multimodal settings, we use *precision* and *recall* to measure synthetic quality and
155	
156	&lt;sup>3&lt;/sup>For all MNIST DDPM experiments we use features extracted by LeNet [73] instead of the Inception network for calculating the Wasserstein distance, since numerical digits do not fall into the domain of natural images. For consistency we also use the term “FID” for the MNIST results.Figure 4: **Training generative models exclusively on synthetic data in a fully synthetic loop without sampling bias reduces both the quality and diversity of their synthetic data decreases over generations.** We plot the FID (left), quality (precision, middle), and diversity (recall, right) of synthetic FFHQ and MNIST images produced in fully synthetic loop.
157	
158	Figure 5: **Without sampling bias, synthetic data modes drift from real modes and merge.** We present t-SNE plots of the real and synthesized data for MNIST from a fully synthetic loop without sampling bias ( $\lambda = 1$ ). We can see the generated modes progressively get merged and lose separation with each other. By Generation 10, the generated samples become almost illegible. See Figure 26 in the Appendix for randomly selected synthetic images of each generation.
159	
160	diversity (as supported in Appendix B.2). Figure 4 illustrates the FID, precision, and recall for each generation of model. In the absence of sampling bias, the distribution of synthetic data undergoes a random walk deviating from the original distribution, caused by the finite sample size of any given training dataset. Consequently, as the generations progress, both the precision and recall of models decrease, while the FID metric exhibits a steady increase. Figure 13 confirms that these trends in FID, precision, and recall continue until eventually saturating.
161	
162	As the generations advance, the synthetic data distribution eventually diverges completely from the true distribution, resulting in a synthetic distribution with little resemblance to real data. This lack of realism is reflected in how the precision and recall of each model eventually drop to zero (see Figure 16 in the appendix for more MNIST DDPM generations), despite having a non-zero variance.
163	
164	Figure 5 visualizes this process using the MNIST dataset. We employ the t-distributed Stochastic Neighbor Embedding (t-SNE) [74] to reduce the dimensionality of both the real and synthetic MNIST datasets at each generation. The visualization reveals that over time, the modes of the synthetic data progressively move away from the real distribution. Despite being produced by a conditional model, these modes eventually merge together, forming a unified, larger mode of data. This gradual divergence away from the modes of real data contributes to the decrease in precision and recall, and consequently, the increase in FID, resulting in a MAD generative process.
165	
166	### 3.4 With biased sampling, quality can increase, but diversity will decrease rapidly
167	
168	In this section, we present the results obtained with sampling bias ( $\lambda < 1$ ). Figure 6 shows the FID, precision, and recall of models at each generations. We see that involvement of sampling bias resultsFully synthetic loop with sampling bias: — StyleGAN on FFHQ  $\lambda = 0.7$  - - - DDPM on MNIST  $\lambda = 0.5$
169	
170	Figure 6: **Training generative models on high-quality synthetic data always produces a loss in either synthetic quality or synthetic diversity. Boosting synthetic quality penalizes synthetic diversity.** We show the FID (left), quality (precision, middle), and diversity (recall, right) of synthetic FFHQ and MNIST images produced in a **fully synthetic loop**. Values of  $\lambda$  less than 1 indicate that, at each iteration, synthetic diversity was traded for synthetic quality. Note that opposed to the unbiased case (Figure 4), precision does not decay with each generation, whereas recall decays significantly faster.
171	
172	Figure 7: **With sampling bias, synthetic data modes drift and collapse around individual (high quality) images instead of merging.** We present t-SNE plots of the real and synthesized data for MNIST from a **fully synthetic loop** with sampling bias ( $\lambda = 0.8$ ). Note that the modes collapse onto themselves, as opposed to merging together as seen in the unbiased case (Figure 5). The generated samples also remain legible. See Figure 27 in Appendix for randomly selected synthetic images from each generation. In Appendix D we present qualitative examples for StyleGAN-2 where we can see that the cross-hatching artifacts do not appear but the distribution significantly loses diversity.
173	
174	in increase of precision in generations; however, it causes a faster drop of recall compared to the case without sampling bias, which all together results in an increase in FID, making it a MAD generative process.
175	
176	The visualization of **fully synthetic loop** with sampling bias is shown in Figure 7. In the presence of sampling bias, the movement of modes of synthetic data is confined within the support of the real data, unlike the case without sampling bias where the modes merge together. However, the variance of synthetic data rapidly decreases, resulting in very limited diversity within the synthetic data.
177	
178	We provide more experiments for the **fully synthetic loop** with Gaussian mixture models, WGAN [60], and Normalizing Flows [61] in Appendix B that all result in MAD generative processes.
179	
180	#### 4 The **synthetic augmentation loop**: Fixed real training data may delay but not prevent MADness
181	
182	Although the analysis is tractable in the **fully synthetic loop**, there is little reason to believe that the it will be representative of real practice. In training real generative models, practitioners will always prefer to use at least some real data when available. In this section, we explore the **synthetic**Figure 8: **Training generative models in a synthetic augmentation loop** with both fixed real and synthetic training data without sampling bias reduces both the quality and diversity of their synthetic data over generations, albeit more slowly than in fully synthetic loop case. We show the FID (left), quality (precision, middle), and diversity (recall, right) of synthetic FFHQ images produced in mixed-training without ( $\lambda = 1$ ) sampling bias. In Appendix F we present qualitative examples, where we can see cross-hatching artifacts, similar to Figure 1, appearing with less prevalence.
183	
184	**augmentation loop**, in which the training data consists of a fixed real dataset that is progressively augmented with synthetic data.
185	
186	We motivate the **synthetic augmentation loop** with the recent practice of using generative models for augmenting datasets in classification tasks, which has shown promising results thanks to advancements in generative models [26, 27]. However, the impact of data augmentation using generative models is still not fully understood. While increasing the volume of training data generally improves the performance of machine learning models, when synthetic samples are introduced into the dataset, there is uncertainty due to the potential deviation of synthetic data from the true distribution of data. Even a small discrepancy can impact the model’s fidelity to the real-world data distribution. As we demonstrate, the presence of the fixed real dataset is not enough to prevent this loop from producing a MAD generative process.
187	
188	Our experiments below support our main conclusion for the **synthetic augmentation loop**, which can be summarized as *fixed real training data only delays the inevitable degradation of the quality or diversity of the generative models over generations*.
189	
190	#### 4.1 Experimental setups for the synthetic augmentation loop
191	
192	Here we simulate the **synthetic augmentation loop** using the same deep generative models and experimental conditions as in Section 3.2. Recall that we first require training an initial model  $\mathcal{G}^1$  with a fully real dataset of  $n_r^1$  samples. All subsequent models  $(\mathcal{G}^t)_{t=2}^\infty$  are trained using  $n_s^t$  synthetic samples from the previous model(s) and all of the original  $n_r^1$  samples used to train  $\mathcal{G}^1$ . Note that each synthetic sample is always produced with sampling bias  $\lambda$ . Our experiments are organized as follows:
193	
194	- • **Denoising diffusion probabilistic model:** We use a conditional MNIST DDPM [59] with  $T = 500$  diffusion time steps. In this experiment the synthetic dataset  $\mathcal{D}_s^t$  is only sampled from the previous generation  $\mathcal{G}^{t-1}$  with sampling bias  $\lambda$ , and  $n_r^1 = n_s^t = 60k$  for all  $t \geq 2$ . The original real MNIST dataset is also available at every generation:  $\mathcal{D}_r^1 = \mathcal{D}_r^t$  and  $n_r^1 = n_r^t = 60k$  for all  $t$ .
195	- • **Generative adversarial network:** We use an unconditional StyleGAN2 architecture [58] trained on the FFHQ-128×128 dataset [63]. Like the StyleGAN experiment in Section 3.2, at each generation  $t \geq 2$  we sample 70k images with no sampling bias ( $\lambda = 1$ ) from the immediately preceding model  $\mathcal{G}^{t-1}$ . However, now the synthetic dataset  $\mathcal{D}_s^t$  includes *all* the previously generated samples (not just the ones from generation  $t$ ), producing a synthetic data pool of size  $n_s^t = (t - 1)70k$  that grows linearly with respect to  $t$ . The real FFHQ dataset is always present at every generation:  $\mathcal{D}_r^1 = \mathcal{D}_r^t$  and  $n_r^1 = n_r^t = 70k$  for every generation  $t$ .Figure 9: **When incorporating real data in the synthetic augmentation loop, even sampling bias cannot prevent increases in FID over generations.** We show the FID (left), quality (precision, middle), and diversity (recall, right) of synthetic MNIST images produced in a synthetic augmentation loop with different sampling biases  $\lambda$ .
196	
197	#### 4.2 A fixed real dataset only slows generative model degradation
198	
199	Here we show that keeping the original real dataset in the synthetic augmentation loop only slows the malignant effects of the fully synthetic loop instead of preventing them. Figure 8 shows how keeping the full FFHQ dataset in a StyleGAN synthetic augmentation loop still produces the same symptoms as the fully synthetic loop: the overall distance from the real dataset (FID) increases, while the quality (precision) and diversity (recall) of synthetic samples still decrease in the absence of sampling bias. In fact, in Appendix F we see the same artifacts appear as in Figure 1 and Appendix C. Unlike all our other experiments, we opt for a linearly growing pool of synthetic data in the StyleGAN synthetic augmentation loop to simulate: (a) whether access to previous generations’ synthesized samples could help future generations learn, and (b) what could happen to a domain of data (e.g., the Internet) in a fresh data loop with almost no newly sampled data points and unlimited access to previous generations’ samples.
200	
201	Additionally, Figure 9 depicts how the sampling bias  $\lambda$  affects the synthetic augmentation loop in much the same way as it did the fully synthetic loop: the overall distance from the real dataset (FID) still increases (albeit more slowly), while the synthetic quality (precision) can increase, but only at the cost of accelerated losses in synthetic diversity (recall). Naturally, some values of  $\lambda$  are better than others at mitigating losses in FID and precision (for example,  $\lambda = 0.8$  in Figure 9).
202	
203	## 5 The fresh data loop: Fresh real data can prevent MADness
204	
205	The most elaborated our autophagous loop models enable new training data to come from two sources: fresh real data from the reference distribution, and synthetic data from previously trained generative models. A clear instance of this can be observed in the LAION-5B dataset [17], which already incorporates images from generative models like Stable Diffusion [2] (recall Figure 2).
206	
207	To understand the evolution of the generative models trained in this way, in this section, we investigate the fresh data loop, which takes the synthetic augmentation loop one step further by incorporating new fresh samples of real data at each iteration. Concretely, we imagine that the real data samples constitute only a fraction  $p \in (0, 1)$  of the available data pool (e.g., a training dataset or the Internet) with the remaining fraction  $1-p$  being synthetic data from generative models. When we independently sample  $n^t$  data points from such a training data set to train a generative model in the  $t$ th generation, there will be  $n_r^t = pn^t$  data points that originate from the real distribution and  $n_s^t = (1-p)n^t$  synthetic data points.
208	
209	In this context, we observe in our experiments below that the presence of fresh data samples fortunately mitigate the development of a MAD generative process; i.e., fresh new data helps keep the generative distribution somewhat close to the reference distribution instead of undergoing a purely random walk. However, we still observe some alarming phenomena. First, we find that—regardless of the performance of early generations—the performance of later generations converges to a pointFigure 10: **In a fresh data loop, generative models converge to a state independent of the initial generative model.** We show the Wasserstein distance (WD) and Fréchet Inception Distance (FID) of two [fresh data loop](#) models: a Gaussian model with  $n_r = 100, n_s = 900$  (left) and an MNIST DDPM model with  $n_r = n_s = 2k$  (right). We simulate the former with both [unbiased](#) and [biased](#) sampling. Across all models we see that the asymptotic WD and FID is independent of initial real samples  $n_{ini}$ .
210	
211	that depends only on the amounts of real and synthetic data in the training loop. Second, we find that, while limited amounts of synthetic data can actually improve the distributional estimate in the [fresh data loop](#)—since synthetic data effectively transfers previously used real data to subsequent generations and increases the effective dataset size—too much synthetic data can still dramatically decrease the performance of the distributional estimate.
212	
213	Our analysis and experiments below support our main conclusion for the [fresh data loop](#): which can be summarized as *with enough fresh real data, the quality and diversity of the generative models do not degrade over generations*.
214	
215	### 5.1 Experimental setups for [fresh data loop](#)
216	
217	As in previous autophagous loop variants, we assume that all models are initially trained solely on real samples, with the number of real samples denoted here as  $n_r^1 = n_{ini}$ . In subsequent generations (i.e., for  $t \geq 2$ ) the generative models are trained with a fixed number of real samples, denoted as  $n_r^t = n_r$ , and a fixed number of synthetic samples, denoted by  $n_s^t = n_s$ . In the [fresh data loop](#), the dataset  $\mathcal{D}_r^t$  is independently sampled from the reference probability distribution  $\mathcal{P}_r$ , while the dataset  $\mathcal{D}_s^t$  is sampled exclusively from the previous generation  $\mathcal{G}^{t-1}$ , with a sampling bias represented as  $\lambda$ .
218	
219	Throughout the remainder of this section, we simulate the [fresh data loop](#) using different values for  $n_{ini}, n_r, n_s$ , and  $\lambda$ , considering the following models and their associated reference probabilities:
220	
221	- • **Gaussian modeling:** We consider a normal reference distribution  $\mathcal{P}_r = \mathcal{N}(\mathbf{0}_d, \mathbf{I}_d)$  with a dimension of  $d = 100$ . For modeling the Gaussian distribution, we utilize an unbiased moment estimation approach, as described in Equation (1).
222	- • **Denoising diffusion probabilistic model:** We use a conditional DDPM [59] with  $T = 500$  diffusion time steps. We consider the MNIST dataset as our reference distribution.
223	
224	The Gaussian example enables examination of the [fresh data loop](#) in greater detail, especially in the asymptotic regime. Meanwhile, our MNIST DDPM example demonstrates the impact of [fresh data loop](#) on more realistic dataset and model.
225	
226	### 5.2 Initial models will eventually be forgotten in the [fresh data loop](#)
227	
228	Here we investigate the impact of the initial model in the [fresh data loop](#). We begin by training the first generative model on  $n_{ini}$  samples, and train the remaining generative models with  $n_r + n_s$  samples, where synthetic samples are synthesized with bias  $\lambda$ . Figure 10 summarizes the results for this experiment.
229	
230	Interestingly, for both model types, we found that the Wasserstein distance/FID converged to a limiting value after a few iterations, and that this limiting value was independent of  $n_{ini}$ . In other words, for a given combination of model type and ground truth distribution  $\mathcal{P}_r$ , we observed that thefinal outcome only depends on  $(n_r, n_s, \lambda)$ , that is,
231	
232	$$\lim_{t \rightarrow \infty} \mathbb{E}[\text{dist}(\mathcal{G}^t, \mathcal{P}_r)] = \text{WD}(n_r, n_s, \lambda). \quad (3)$$
233	
234	Thus, the initial model’s influence diminished throughout the process, with only the aforementioned parameters having an impact on the final result.
235	
236	In the context of autophagy, this point brings some hope: with the incorporation of fresh new data at each generation, there is not necessarily an increase in  $\mathbb{E}[\text{dist}(\mathcal{G}^t, \mathcal{P}_r)]$  as  $t$  grows. *Thus, the fresh data loop can prevent a MAD generative process.*
237	
238	### 5.3 A phase transition in the fresh data loop
239	
240	One might suspect that a complimentary perspective to the previous observation—that fresh new data mitigates the MAD generative process—is that synthetic data hurts a [fresh data loop](#) generative process. However, the truth appears to be more nuanced. What we find instead is that when we mix synthetic data trained on previous generations and fresh new data, there is a regime where modest amounts of synthetic data actually *boost* performance, but when synthetic data exceeds some critical threshold, the models suffer.
241	
242	We make this observation precise through Gaussian simulations. Specifically, we consider the limit point of the fresh data loop from Equation (3). Using the value of this limit point, which we compute via Monte-Carlo simulation, we compare against an alternative model  $\mathcal{G}(n_e)$  trained only on a collection of real data samples of size  $n_e$ . We refer to  $n_e$  as the *effective sample size* and compute its value given  $(n_r, n_s, \lambda)$  via
243	
244	$$\text{Find } n_e \text{ s.t. } \mathbb{E}[\text{dist}(\mathcal{G}(n_e), \mathcal{P}_r)] = \text{WD}(n_r, n_s, \lambda). \quad (4)$$
245	
246	That is,  $n_e$  captures the sample efficiency of the limit point of the [fresh data loop](#). We evaluate the ratio  $n_e/n_r$  in our experiments. When  $n_e/n_r \geq 1$ , the synthetic data effectively increases the number of real samples, which we consider to be **admissible**, while for  $n_e/n_r < 1$ , synthetic data effectively reduces the number of real samples.
247	
248	We plot two perspectives of the results of this experiment in Figures 11 and 12. We discover several effects. First, we make some observations regarding sample sizes. We find that, indeed, for a given combination of  $n_r$  and  $\lambda < 1$ , there exists a phase transition in  $n_s$ , such that if  $n_s$  exceeds some admissible threshold, the effective sample size drops below the fresh data sample size. However, we do not find that the ratio of  $n_r$  to  $n_s$  is allowed to be constant; in fact, we find the opposite trend. For small values of  $n_r$ , we find that large value of  $n_s$  can be useful, but as  $n_r$  grows larger, the phase transition threshold of  $n_s$  seems to become constant.
249	
250	Second, we make some observations regarding the effect of sampling bias parameter  $\lambda$ . We find that the value of the admissible threshold for  $n_s$  depends strongly on the amount of sampling bias in the synthetic process. Perhaps surprisingly, more sampling bias (smaller  $\lambda$ ) actually reduces the number of synthetic samples that can be used without harming performance. Taking the limit as  $\lambda \rightarrow 1$  for unbiased sampling appears to ensure that the effective number of samples is always increased. Whether this limiting behavior extends to other generative models beyond the Gaussian modeling setting is unclear. As discussed in Section 2.3, it is unlikely that synthetic data is generated without sampling bias in practice, so we believe it is better to draw conclusions from the  $\lambda < 1$  case.
251	
252	More experiments for the [fresh data loop](#) can be found in Appendix G.
253	
254	## 6 Discussion
255	
256	In this paper we have sought to extrapolate what might happen in the near and distant future as generative models become ubiquitous and are used to train later generations of models in an autophagous (self-consuming) loop. Using analysis and experiments with state-of-the-art image generative models and standard image datasets, we have studied three families of autophagous loops and singled out the key rôle played by the models’ sampling bias. Some ramifications are clear: without enough fresh real data each generation, future generative models are doomed to Model Autophagy Disorder (MAD), meaning that either their quality (measured in terms of precision) or their diversity (measured in terms of recall) will progressively degrade and generative artifacts willFigure 11: **In a fresh data loop, the admissible amount of synthetic data does not increase with the amount of real data.** As the real data sample size  $n_r$  increases, the maximum number of synthetic samples  $n_s$  for which  $n_e \geq n_r$  (blue area) converges. Synthetic data is only likely to be helpful when  $n_r$  is small.
257	
258	Figure 12: **In a fresh data loop, sampling bias reduces the admissible synthetic sample size.** For increased sampling bias (smaller  $\lambda$ ), the maximum number of synthetic samples  $n_s$  for which  $n_e \geq n_r$  (blue area) decreases.
259	
260	be amplified. One doomsday scenario is that, if left uncontrolled for many generations, MAD could poison the data quality and diversity of the entire Internet. Short of this, it seems inevitable that as-to-now-unseen unintended consequences will arise from AI autophagy even in the near-term.
261	
262	Practitioners who are deliberately using synthetic data for training because it is cheap and easy can take our conclusions as a warning and consider tempering their synthetic data habits, perhaps by joining an appropriate 12-step program. Those in truly data-scarce applications can interpret our results as a guide to how much scarce real data is necessary to avoid MADness in the future. For example, future practitioners who wish to train a comprehensive medical image generator using anonymous synthetic data from multiple institutions [29, 30] should now know that very deliberate care must be taken to ensure that: (i) all anonymous synthetic images are artifact-free and diverse (see the [fully synthetic loop](#)), and (ii) (ideally new) real data is present in the training as much as possible (see the [fresh data loop](#) and the [synthetic augmentation loop](#)).
263	
264	Practitioners who have not been intending to use synthetic training but find it polluting their training data pool are harder to help. To maintain trustworthy datasets containing exclusively real data, the obvious recommendation is for the community to develop methods to identify synthetic data. These methods can then be used to filter training datasets to reject synthetic data or maintain a particular ratio of synthetic-to-real data. In this regard, there is early progress in the AI literature of new methods closely related to steganography [40] that can be employed for synthetic data identification. Since generative models do not necessarily add meta-data to generated images, another approach is to *watermark* synthetic data so that it can be identified and rejected when training. The reliability of watermarking of data generated by LLMs [75] and novel methods for watermarking LLMs [76], diffusion models [77–80], andn GANs [81] are currently active areas of research. One reservation that we have about watermarking is that it deliberately introduces hidden artifacts in the synthetic datato make it detectable. These artifacts can possibly be amplified out of control by autophagy, turning watermarking from a useful to harmful. In [fresh data loop](#) we see that a large amount of synthetic data hurts performance, while a modest amount of synthetic data actually boosts performance. Watermarking can help out in this scenario to decrease the amount of synthetic data, and ideally put the model inside the good region (e.g., the blue area in Figure 11 and Figure 12), such that the negative aspects of watermarking are avoided. This opens up interesting avenues for research on autophagy-aware watermarking.
265	
266	There are many possible extensions of the work reported here, including studying combinations of the three families of autophagous loops we have proposed. For example, one could analyze autophagous loops where the training data includes some synthetic data from previous generations' models, some fixed real data, and some fresh real data. Our analysis has focused on the distance between the synthetic and reference data manifolds. An interesting research question is how this distance will manifest itself in lowered performance on AI tasks like classification (since precision can be closely related to classifier performance, the link is waiting to be made).
267	
268	Finally, in this paper we have focused on imagery, but there is nothing about our conclusions that makes them image-specific. Generative models for any kind of data can be connected into autophagous loops and go MAD. One timely data type is the text produced by LLMs (some of which are already being trained on synthetic data from pre-existing models like ChatGPT) [57, 66, 67], where our results on precision and recall translate directly into the properties of the text produced after generations of autophagy. Similar conclusions have been reached in the experiments in the contemporaneous work of [53], but there is much work to do in this vein.
269	
270	## Acknowledgements
271	
272	Thanks to Hamid Javadi, Blake Mason, and Shashank Sonkar for sharing their insights over the course of this project. This work was supported by NSF grants CCF-1911094, IIS-1838177, and IIS-1730574; ONR grants N00014-18-12571, N00014-20-1-2534, and MURI N00014-20-1-2787; AFOSR grant FA9550-22-1-0060; DOE grant DE-SC0020345; and a Vannevar Bush Faculty Fellowship, ONR grant N00014-18-1-2047.## A Proof of synthetic Gaussian martingale variance collapse
273	
274	We now prove that for the process described in Equation (1),  $\Sigma_t \xrightarrow{\text{a.s.}} 0$ .
275	
276	*Proof.* First write  $X_t^i = \sqrt{\lambda} \Sigma_{t-1}^{1/2} Z_t^i + \mu_{t-1}$  for  $Z_t^i \sim \mathcal{N}(\mathbf{0}_d, \mathbf{I}_d)$ . Then consider the process  $\text{tr}[\Sigma_t]$ , which is a lower bounded submartingale:
277	
278	$$\text{tr}[\Sigma_t] = \lambda \text{tr} \left[ \Sigma_{t-1}^{1/2} \left( \frac{1}{N-1} \sum_{i=1}^N (Z_t^i - \mu_t^Z)(Z_t^i - \mu_t^Z)^\top \right) \Sigma_{t-1}^{1/2} \right], \quad (5)$$
279	
280	where  $\mu_t^Z = \frac{1}{N} \sum_{i=1}^N Z_t^i$ . By Doob’s martingale convergence theorem [72, Ch. 11], there exists a random variable  $W$  such that  $\text{tr}[\Sigma_t] \xrightarrow{\text{a.s.}} W$ , and we now show that we must have  $W = 0$ . Without loss of generality, we can assume that  $\Sigma_{t-1}$  is diagonal, in which case it becomes clear that  $\text{tr}[\Sigma_t]$  is a generalized  $\chi^2$  random variable, being a linear combination of  $d$  independent  $\chi^2$  random variables with  $N-1$  degrees of freedom, mixed with weights  $\lambda \text{diag}(\Sigma_{t-1})$ . Therefore, we can write  $\text{tr}[\Sigma_t] = \lambda Y_t \text{tr}[\Sigma_{t-1}]$ , where  $Y_t$  is a generalized  $\chi^2$  random variable with the same degrees of freedom but with mixing weights  $\text{diag}(\Sigma_{t-1})/\text{tr}[\Sigma_{t-1}]$ , and  $\mathbb{E}[Y_t | \Sigma_{t-1}] = 1$ . This implies that at least one mixing weight is greater than  $1/D$  for each  $t$ , which means that for any  $0 < \epsilon < 1$ , there exists  $c > 0$  such that  $\Pr(|Y_t - 1| > \epsilon) > c$ . Now consider the case  $\lambda = 1$ . Since  $|Y_t - 1| > \epsilon$  infinitely often with probability one, the only  $W$  that can satisfy  $\lim_{t \rightarrow \infty} \text{tr}[\Sigma_0] \prod_{s=1}^t Y_s = W$  is  $W = 0$ . For general  $\lambda \leq 1$ ,  $\text{tr}[\Sigma_t]$  is simply the product of the process for  $\lambda = 1$  and the sequence  $\lambda^{t-1}$ , and so the product must also converge to zero almost surely. Finally, since  $\text{tr}[\Sigma_t] \xrightarrow{\text{a.s.}} 0$ , we also must have  $\Sigma_t \xrightarrow{\text{a.s.}} 0$ , where convergence is defined with any matrix norm.  $\square$
281	
282	## B Additional experiments for the fully synthetic loop
283	
284	Here we present additional experiments for the [fully synthetic loop](#).
285	
286	### B.1 WGAN-GPs in an unbiased fully synthetic loop
287	
288	In this experiment we trained Wasserstein GANs (with gradient penalty) [60] on the MNIST dataset in a [fully synthetic loop](#) for 100 generations. As shown in Figure 13, the FID monotonically increases, while quality (precision) and diversity (recall) monotonically decrease.
289	
290	Figure 13: The FID (left), quality (precision, middle), and diversity (recall, right) of synthetic FFHQ and MNIST images produced by WGAN-GPs on MNIST.
291	
292	### B.2 GMMs in an unbiased fully synthetic loop
293	
294	We also trained 2D GMMs in an unbiased [fully synthetic loop](#) using the same 25-mode distribution as [82]. In Figure 14 we see that the [fully synthetic loop](#) gradually reduces the number of modes covered by the synthetic distribution. Various metrics could measure this loss in diversity, so in Figure 15 we explore how well each metric reflects the dynamics of the [fully synthetic loop](#), finding that recall is best-equipped to measure diversity in multimodal datasets.Figure 14: Estimated GMM [82] distributions after 1, 200, and  $2k$  iterations of a **fully synthetic loop**. Notice that the modes are lost asymptotically.
295	
296	Figure 15: For GMMs in a **fully synthetic loop** (Figure 14), there are three primary potential metrics of diversity: variance\*, average modal variance\* (the average variance of each mode), and recall [39]. We observe that the overall variance (left) does not reflect the loss of modes that we see in Figure 14 as smoothly as recall (right) and average modal variance (middle). Recall is therefore a suitable choice for measuring diversity in multimodal datasets and, unlike average modal variance, is compatible with distributions where the number of modes is not tractable (e.g., natural images). \*For multidimensional datasets, we calculate variance as the trace of covariance.
297	
298	### B.3 Additional MNIST DDPM **fully synthetic loop** results
299	
300	In Figure 6 we showcased the results of training MNIST DDPMs in a **fully synthetic loop** with various sampling bias factors  $\lambda$ . In Figure 16 we have the results (FID, precision, and recall) more generations  $t$  and different sampling biases  $\lambda$ .
301	
302	Figure 16: The FID (left), quality (precision, middle), and diversity (recall, right) of synthetic images produced by DDPMs on MNIST.
303	
304	### B.4 Normalizing flow **fully synthetic loop**
305	
306	We implemented the **fully synthetic loop** using normalizing flows [83, 84] for generative modeling of the two-dimensional Rosenbrock reference distribution [85] in order to visualize the outcomeof this particular scenario in a controlled setting. Normalizing flows are unique in that they enable exact evaluation of the likelihood of the estimated distribution due to their invertibility [83]. This leads to a relatively straightforward training procedure compared to GANs, which often require careful balancing between the generator and discriminator networks to avoid mode collapse [86]. Therefore, by using a low-dimensional reference distribution, this setup allows us to demonstrate the **fully synthetic loop** while eliminating potential training imperfections.
307	
308	According to the **fully synthetic loop** setup, we start with a training dataset of  $10^4$  samples from the 2D Rosenbrock distribution with the density function  $\mathcal{P}_r(x_1, x_2) \propto \exp\left(-\frac{1}{2}x_1^2 - (x_2 - x_1^2)^2\right)$  [85], which is plotted on the left-hand side of Figure 17. The subsequent generations of normalizing flow models are trained using synthetic data generated by the previous pre-trained normalizing flow for 16 generations, both with and without sampling bias. We employ the GLOW normalizing flow architecture [84] with eight coupling layers [84] and a hidden dimension of 64. The training is carried out for 20 epochs with a batch size of 256 for each generation, ensuring convergence as determined by monitoring the model’s likelihood over a validation set. Figure 17 summarizes the results of this **fully synthetic loop** setup. To incorporate sampling bias, we sample from  $\mathcal{N}(\mathbf{0}_d, \lambda \mathbf{I}_d)$  from the latent space of the model, where  $d = 2$ . As shown, regardless of the presence of sampling bias, the resulting distribution after 16 generations loses the tails of the reference distribution, indicating a loss of diversity. This phenomenon becomes more pronounced when sampling bias is present ( $\lambda < 1$ ).
309	
310	Figure 17: The **fully synthetic loop** implemented with a formalizing flow [83] applied to the 2D Rosenbrock distribution [85]. Sampling with or without bias still loses the tails of the distribution (i.e., diversity). Using  $\lambda < 1$  accelerates this loss of diversity.### C FFHQ fully synthetic loop images with $\lambda = 1$
311	
312	We show additional randomly chosen synthetic samples produced by the same StyleGAN FFHQ unbiased **fully synthetic loop** as in Figure 1 and Figure 4.
313	
314	Figure 18: Generation  $t = 1$  of a **fully synthetic loop** with bias  $\lambda = 1$ . i.e., synthetic samples from the first model  $\mathcal{G}^1$ .
315	
316	Figure 19: Generation  $t = 3$  of a **fully synthetic loop** with bias  $\lambda = 1$Figure 20: Generation  $t = 5$  of a fully synthetic loop with bias  $\lambda = 1$
317	
318	Figure 21: Generation  $t = 7$  of a fully synthetic loop with bias  $\lambda = 1$Figure 22: Generation  $t = 9$  of a **fully synthetic loop** with bias  $\lambda = 1$
319	
320	#### D **FFHQ fully synthetic loop images with $\lambda = 0.7$**
321	
322	As in Appendix C, here we show synthetic FFHQ images produced by a StyleGAN architecture in a **fully synthetic loop** with biased sampling ( $\lambda = 0.7$ , Figure 6) that slows the proliferation of artifacts, but at the cost of severely decreased diversity.
323	
324	Figure 23: Generation  $t = 1$  of a **fully synthetic loop** with bias  $\lambda = 0.7$Figure 24: Generation  $t = 3$  of a [fully synthetic loop](#) with bias  $\lambda = 0.7$
325	
326	Figure 25: Generation  $t = 5$  of a [fully synthetic loop](#) with bias  $\lambda = 0.7$## E MNIST fully synthetic loop images
327	
328	Here we show randomly chosen samples from each generation of an MNIST DDPM in a [fully synthetic loop](#) for different sampling biases (as discussed in Figure 4 and Figure 6).
329	
330	Figure 26: **Without sampling bias, synthetic data modes drift from real modes and merge together.** Randomly selected synthetic MNIST images of each generation without sampling bias ( $\lambda = 1$ ).
331	
332	Figure 27: **With sampling bias, synthetic data modes drift and collapse around a single (high quality) image before merging.** Randomly selected synthetic MNIST images of each generation without sampling bias ( $\lambda = 0.8$ ).## F FFHQ synthetic augmentation loop images with $\lambda = 1$
333	
334	Figure 28: Generation  $t = 3$  of a synthetic augmentation loop with bias  $\lambda = 1$ . See Figure 18 for the samples from  $t = 1$  (in any autophagous loop the first model  $\mathcal{G}^1$  always trains on purely real data, see Section 2).
335	
336	Figure 29: Generation  $t = 6$  of a synthetic augmentation loop with bias  $\lambda = 1$## G Additional results for the fresh data loop
337	
338	Here we provide three additional Gaussian experiments investigating the convergence of the [fresh data loop](#).
339	
340	**Experiment 1:** In Section 5.1 we assumed that we only sample from the previous generation  $\mathcal{G}^{t-1}$  for creating the synthetic dataset  $\mathcal{D}_s^t$ . In this experiment we sample randomly from  $K$  previous models  $(\mathcal{G}^\tau)_{\tau=t-1-K}^{t-1}$ . Here  $n_r = 10^3$ ,  $n_s = 10^4$ , and  $\lambda = 1$ . In Figure 30 we see how  $\frac{n_e}{n_r}$  varies with respect to  $K$ . Increasing the memory  $K$  in sampling from previous generations can boost performance, however the rate of improvement becomes slower as  $K$  increases.
341	
342	Figure 30: The effective sample size  $n_e$  divided by real sample size  $n_r$  for different numbers of accessed previous generations  $K$ .
343	
344	**Experiment 2:** Here we assume that we are sampling from an environment where  $p$  percent of data is real, and the rest is synthetic data from the previous generation  $\mathcal{G}^{t-1}$  with sampling bias  $\lambda$ . We change the total number of data in the dataset  $n = |\mathcal{D}^t|$ , with  $n_r = p \times n$  and  $n_s = (1 - p) \times n$ . We show the Wasserstein distance for different  $p$  and  $\lambda$  in Figure 31.
345	
346	Let us first examine the dynamics of the Gaussian [fresh data loop](#) without sampling bias ( $\lambda = 1$ ). We observe in Figure 31 (left) that the Wasserstein distance (WD) decreases with respect to dataset size  $n$ . However, the presence of synthetic data ( $p < 100\%$ ) decreases the rate at which the WD decreases, and increases the overall WD each generation in the [fresh data loop](#). *This means that with presence of synthetic data in the Internet, the progress of generative models will become slower*
347	
348	In the presence of sampling bias ( $\lambda < 1$ , Figure 31 right), we see that even for close values of  $\lambda$  to 1, the Wasserstein distance follows a sub-linear trend, meaning that eventually the rate of progress in generative models will effectively stop, no matter how much (realistically) the total dataset size is increased.
349	
350	Figure 31: The Wasserstein distance (WD) as the whole dataset size increases for different values of  $p$  (left), and sampling bias (right).## References
351	
352	- [1] Tero Karras, Samuli Laine, and Timo Aila. A style-based generator architecture for generative adversarial networks. In *CVPR*, 2019.
353	- [2] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In *CVPR*, 2022.
354	- [3] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-conditional image generation with clip latents. *arXiv preprint arXiv:2204.06125*, 2022.
355	- [4] Zalán Borsos, Raphaël Marinier, Damien Vincent, Eugene Kharitonov, Olivier Pietquin, Matt Sharifi, Olivier Teboul, David Grangier, Marco Tagliasacchi, and Neil Zeghidour. AudioLM: a language modeling approach to audio generation. *arXiv preprint arXiv:2209.03143*, 2022.
356	- [5] Andrea Agostinelli, Timo I. Denk, Zalán Borsos, Jesse Engel, Mauro Verzetti, Antoine Caillon, Qingqing Huang, Aren Jansen, Adam Roberts, Marco Tagliasacchi, Matt Sharifi, Neil Zeghidour, and Christian Frank. MusicLM: Generating music from text. *arXiv preprint arXiv:2301.11325*, 2023.
357	- [6] ElevenLabs. First long-form speech synthesis platform for publishers and creators. 2022. URL &lt;https://blog.elevenlabs.io/long-form-speech-synthesis-for-publishers-and-creators/>.
358	- [7] OpenAI. GPT-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.
359	- [8] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. LLaMA: Open and efficient foundation language models. *arXiv preprint arXiv:2302.13971*, 2023.
360	- [9] Haixing Dai, Zhengliang Liu, Wenxiong Liao, Xiaoke Huang, Yihan Cao, Zihao Wu, Lin Zhao, Shaochen Xu, Wei Liu, Ninghao Liu, Sheng Li, Dajiang Zhu, Hongmin Cai, Lichao Sun, Quanzheng Li, Dinggang Shen, Tianming Liu, and Xiang Li. AugGPT: Leveraging ChatGPT for text data augmentation. *arXiv preprint arXiv:2302.13007*, 2023.
361	- [10] Ben Poole, Ajay Jain, Jonathan T. Barron, and Ben Mildenhall. Dreamfusion: Text-to-3d using 2d diffusion. In *ICLR*, 2023.
362	- [11] Ruben Villegas, Mohammad Babaeizadeh, Pieter-Jan Kindermans, Hernan Moraldo, Han Zhang, Mohammad Taghi Saffar, Santiago Castro, Julius Kunze, and Dumitru Erhan. Phenaki: Variable length video generation from open domain textual descriptions. In *ICLR*, 2023.
363	- [12] Clement Vignac, Igor Krawczuk, Antoine Siraudin, Bohan Wang, Volkan Cevher, and Pascal Frossard. DiGress: Discrete denoising diffusion for graph generation. In *ICLR*, 2023.
364	- [13] Akim Kotelnikov, Dmitry Baranchuk, Ivan Rubachev, and Artem Babenko. TabDDPM: Modelling tabular data with diffusion models. *arXiv preprint arXiv:2209.15421*, 2022.
365	- [14] Brett A Becker, Paul Denny, James Finnie-Ansley, Andrew Luxton-Reilly, James Prather, and Eddie Antonio Santos. Programming is hard-or at least it used to be: Educational opportunities and challenges of AI code generation. In *ACM Technical Symposium on Computer Science Education V.1*, 2023.
366	- [15] Matthew Cantor. Nearly 50 news websites are ‘AI-generated’, a study says. Would I be able to tell? *The Guardian*, May 2023.
367	- [16] Roberto Gozalo-Brizuela and Eduardo C. Garrido-Merchan. ChatGPT is not all you need. a state of the art review of large generative ai models. *arXiv preprint arXiv:2301.04655*, 2023.
368	- [17] Christoph Schuhmann et al. LAION-5B: An open large-scale dataset for training next generation image-text models. In *NeurIPS Datasets and Benchmarks Track*, 2022.
369	- [18] Matthew Gault. AI spam is already flooding the internet and it has an obvious tell. *VICE*, April 2023.- [19] Jon Christian. CNET secretly used AI on articles that didn't disclose that fact, staff say. *Futurism*, January 2023.
370	- [20] Ruifei He, Shuyang Sun, Xin Yu, Chuhui Xue, Wenqing Zhang, Philip Torr, Song Bai, and Xiaojuan Qi. Is synthetic data from generative models ready for image recognition? In *ICLR*, 2023.
371	- [21] Jordan Shipard, Arnold Wiliem, Kien Nguyen Thanh, Wei Xiang, and Clinton Fookes. Diversity is definitely needed: Improving model-agnostic zero-shot classification via stable diffusion. *arXiv preprint arXiv:2302.03298*, 2023.
372	- [22] Hritik Bansal and Aditya Grover. Leaving reality to imagination: Robust classification via generated datasets. *arXiv preprint arXiv:2302.02503*, 2023.
373	- [23] Shaobo Lin, Kun Wang, Xingyu Zeng, and Rui Zhao. Explore the power of synthetic data on few-shot object detection. *arXiv preprint arXiv:2303.13221*, 2023.
374	- [24] Canwen Xu, Daya Guo, Nan Duan, and Julian McAuley. Baize: An open-source chat model with parameter-efficient tuning on self-chat data. *arXiv preprint arXiv:2304.01196*, 2023.
375	- [25] Shekoofeh Azizi, Simon Kornblith, Chitwan Saharia, Mohammad Norouzi, and David J Fleet. Synthetic data from diffusion models improves imagenet classification. *arXiv preprint arXiv:2304.08466*, 2023.
376	- [26] Max F Burg, Florian Wenzel, Dominik Zietlow, Max Horn, Osama Makansi, Francesco Locatello, and Chris Russell. A data augmentation perspective on diffusion models and retrieval. *arXiv preprint arXiv:2304.10253*, 2023.
377	- [27] Lorenzo Luzi, Ali Siahkoohi, Paul M Mayer, Josue Casco-Rodriguez, and Richard Baraniuk. Boomerang: Local sampling on image manifolds using diffusion models. *arXiv preprint arXiv:2210.12100*, 2022.
378	- [28] Marvin Klemp, Kevin Rösche, Royden Wagner, Jannik Quehl, and Martin Lauer. LDFA: Latent diffusion face anonymization for self-driving applications. *arXiv preprint arXiv:2302.08931*, 2023.
379	- [29] Kai Packhäuser, Lukas Folle, Florian Thamm, and Andreas Maier. Generation of anonymous chest radiographs using latent diffusion models for training thoracic abnormality classification systems. *arXiv preprint arXiv:2211.01323*, 2022.
380	- [30] August DuMont Schütte, Jürgen Hetzel, Sergios Gatidis, Tobias Hepp, Benedikt Dietz, Stefan Bauer, and Patrick Schwab. Overcoming barriers to data sharing with medical image generation: a comprehensive evaluation. *NPJ Digital Medicine*, 2021.
381	- [31] The bigger-is-better approach to AI is running out of road. *The Economist*, June 2023.
382	- [32] Large, creative AI models will transform lives and labour markets. *The Economist*, April 2023.
383	- [33] Pablo Villalobos, Jaime Sevilla, Lennart Heim, Tamay Besiroglu, Marius Hobbhahn, and Anson Ho. Will we run out of data? an analysis of the limits of scaling datasets in machine learning. *arXiv preprint arXiv:2211.04325*, 2022.
384	- [34] Veniamin Veselovsky, Manoel Horta Ribeiro, and Robert West. Artificial artificial artificial intelligence: Crowd workers widely use large language models for text production tasks. *arXiv preprint arXiv:2306.07899*, 2023.
385	- [35] Ahmed Elgammal, Bingchen Liu, Mohamed Elhoseiny, and Marian Mazzone. CAN: Creative adversarial networks, generating "art" by learning about styles and deviating from style norms. *arXiv preprint arXiv:1706.07068*, 2017.
386	- [36] Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, and Alexei A Efros. Image-to-image translation with conditional adversarial networks. In *CVPR*, 2017.
387	- [37] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and Ilya Sutskever. Zero-shot text-to-image generation. In *ICML*, 2021.- [38] Andrew Brock, Jeff Donahue, and Karen Simonyan. Large scale GAN training for high fidelity natural image synthesis. In *ICLR*, 2019.
388	- [39] Tuomas Kynkäänniemi, Tero Karras, Samuli Laine, Jaakko Lehtinen, and Timo Aila. Improved precision and recall metric for assessing generative models. *NeurIPS*, 2019.
389	- [40] Luca Guarnera, Oliver Giudice, and Sebastiano Battiato. Deepfake detection by analyzing convolutional traces. In *CVPR workshops*, 2020.
390	- [41] Tero Karras, Miika Aittala, Samuli Laine, Erik Härkönen, Janne Hellsten, Jaakko Lehtinen, and Timo Aila. Alias-free generative adversarial networks. In *NeurIPS*, 2021.
391	- [42] Jonathan Ho and Tim Salimans. Classifier-free diffusion guidance. In *NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications*, 2021.
392	- [43] Natalie Jomini Stroud. *Niche News: The Politics of News Choice*. Oxford University Press, 2011.
393	- [44] Ivan Dylko, Igor Dolgov, William Hoffman, Nicholas Eckhart, Maria Molina, and Omar Aaziz. The dark side of technology: An experimental investigation of the influence of customizability technology on online political selective exposure. *Computers in Human Behavior*, 2017.
394	- [45] Michael A Beam. Automating the news: How personalized news recommender system design choices impact news reception. *Communication Research*, 2014.
395	- [46] Eytan Bakshy, Solomon Messing, and Lada A Adamic. Exposure to ideologically diverse news and opinion on Facebook. *Science*, 2015.
396	- [47] Derek O’Callaghan, Derek Greene, Maura Conway, Joe Carthy, and Pádraig Cunningham. Down the (white) rabbit hole: The extreme right and online recommender systems. *Social Science Computer Review*, 2015.
397	- [48] Megan A Brown, James Bisbee, Angela Lai, Richard Bonneau, Jonathan Nagler, and Joshua A Tucker. Echo chambers, rabbit holes, and algorithmic bias: How youtube recommends content to real users. *SSRN 4114905*, 2022.
398	- [49] Judith Möller, Damian Trilling, Natali Helberger, and Bram van Es. Do not blame it on the algorithm: an empirical assessment of multiple recommender systems and their impact on content diversity. *Information, Communication & Society*, 2018.
399	- [50] Neal Nathanson, John Wilesmith, and Christian Griot. Bovine Spongiform Encephalopathy (BSE): Causes and Consequences of a Common Source Epidemic. *American Journal of Epidemiology*, 145(11):959–969, 06 1997. ISSN 0002-9262.
400	- [51] Josue Casco-Rodriguez. Toward understanding the impact of generative AI on future generative AI. Electrical & Computer Engineering Technical Report No. 2023–04–79 (ELEC599), Rice University, 9 April 2023.
401	- [52] Josue Casco-Rodriguez, Lorenzo Luzi, Sina Alemohammad, Shashank Sonkar, Ahmed Imtiaz Humayun, Ali Siahkooi, and Richard Baraniuk. Toward understanding the impact of generative AI on future generative AI. In *Interface Rice*. Rice University Neuroengineering Initiative, 18 May 2023.
402	- [53] Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson. The curse of recursion: Training on generated data makes models forget. *arXiv preprint arXiv:2305.17493*, 2023.
403	- [54] Gonzalo Martínez, Lauren Watson, Pedro Reviriego, José Alberto Hernández, Marc Juarez, and Rik Sarkar. Towards understanding the interplay of generative artificial intelligence and the Internet. *arXiv preprint arXiv:2306.06130*, 2023.
404	- [55] Gonzalo Martínez, Lauren Watson, Pedro Reviriego, José Alberto Hernández, Marc Juarez, and Rik Sarkar. Combining generative artificial intelligence (ai) and the Internet: Heading towards evolution or degradation? *arXiv preprint arXiv:2303.01255*, 2023.- [56] followfox.ai. The power of synthetic data: Infinite loop to improve fine-tuning results with stable diffusion models. February 2023. URL &lt;https://followfoxai.substack.com/p/the-power-of-synthetic-data-infinite>.
405	- [57] Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, and Jiawei Han. Large language models can self-improve. *arXiv preprint arXiv:2210.11610*, 2022.
406	- [58] Tero Karras, Samuli Laine, Miika Aittala, Janne Hellsten, Jaakko Lehtinen, and Timo Aila. Analyzing and improving the image quality of StyleGAN. In *CVPR*, 2020.
407	- [59] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. In *NeurIPS*, 2020.
408	- [60] Ishaan Gulrajani, Faruk Ahmed, Martin Arjovsky, Vincent Dumoulin, and Aaron C Courville. Improved training of Wasserstein GANs. *NeurIPS*, 2017.
409	- [61] Ivan Kobyzev, Simon JD Prince, and Marcus A Brubaker. Normalizing flows: An introduction and review of current methods. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, (11), 2020.
410	- [62] Li Deng. The MNIST database of handwritten digit images for machine learning research [best of the web]. *IEEE Signal Processing Magazine*, (6), 2012.
411	- [63] Robert E Kass and Paul W Vos. *Geometrical Foundations of Asymptotic Inference*. John Wiley & Sons, 1997.
412	- [64] Walter H. L. Pinaya, Petru-Daniel Tudosi, Jessica Dafflon, Pedro F. Da Costa, Virginia Fernandez, Parashkev Nachev, Sebastien Ourselin, and M. Jorge Cardoso. Brain imaging generation with latent diffusion models. In *Deep Generative Models*. Springer Nature, 2022.
413	- [65] Chengyuan Deng, Shihang Feng, Hanchen Wang, Xitong Zhang, Peng Jin, Yinan Feng, Qili Zeng, Yinpeng Chen, and Youzuo Lin. OpenFWI: Large-scale multi-structural benchmark datasets for full waveform inversion. In *NeurIPS*, 2022.
414	- [66] Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi. Self-instruct: Aligning language model with self generated instructions. *arXiv preprint arXiv:2212.10560*, 2022.
415	- [67] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B Hashimoto. Alpaca: A strong, replicable instruction-following model. *Stanford Center for Research on Foundation Models.*, (6), 2023.
416	- [68] Ahmed Imtiaz Humayun, Randall Balestrieri, and Richard Baraniuk. Polarity sampling: Quality and diversity control of pre-trained generative networks via singular values. In *CVPR*, 2022.
417	- [69] Leonid V Kantorovich. Mathematical Methods of Organizing and Planning Production. *Management science*, (4), 1960.
418	- [70] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. GANs trained by a two time-scale update rule converge to a local Nash equilibrium. In *NeurIPS*, 2017.
419	- [71] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. In *International Conference on Learning Representations*, 2021.
420	- [72] David Williams. *Probability With Martingales*. Cambridge University Press, 1991.
421	- [73] Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-based learning applied to document recognition. *Proceedings of the IEEE*, 1998.
422	- [74] Laurens Van der Maaten and Geoffrey Hinton. Visualizing data using t-SNE. *JMLR*, 2008.
423	- [75] John Kirchenbauer, Jonas Geiping, Yuxin Wen, Manli Shu, Khalid Saifullah, Kezhi Kong, Kasun Fernando, Aniruddha Saha, Micah Goldblum, and Tom Goldstein. On the reliability of watermarks for large language models. *arXiv preprint arXiv:2306.04634*, 2023.
424	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbbfcbeb-b8c1-43e2-97d8-323f05613483",
  "isSidechain": true,
  "promptId": "641fe7b7-cbeb-41b8-a211-9837bbca15e6",
  "agentId": "a3beaf73a9e1f198f",
  "type": "user",
  "uuid": "34604d13-c673-45ee-b997-c0f8b7865124",
  "sourceToolAssistantUUID": "bbbfcbeb-b8c1-43e2-97d8-323f05613483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T15:03:46.908Z_

Here is the full extracted content from "Self-Consuming Generative Models Go MAD" (ICLR 2024, arXiv 2307.01850):

---

## Paper: Self-Consuming Generative Models Go MAD

**Authors:** Sina Alemohammad*, Josue Casco-Rodriguez*, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk (* equal contribution)
Rice University / Stanford University

**Venue:** ICLR 2024 (Poster)

---

## Abstract

Seismic advances in generative AI algorithms for imagery, text, and other data types has led to the temptation to use synthetic data to train next-generation models. Repeating this process creates an autophagous ("self-consuming") loop whose properties are poorly understood. We conduct a thorough analytical and empirical analysis using state-of-the-art generative image models of three families of autophagous loops that differ in how fixed or fresh real training data is available through the generations of training and in whether the samples from previous-generation models have been biased to trade off data quality versus diversity. Our primary conclusion across all scenarios is that *without enough fresh real data in each generation of an autophagous loop, future generative models are doomed to have their quality (precision) or diversity (recall) progressively decrease*. We term this condition **Model Autophagy Disorder (MAD)**.

---

## Section 1: Introduction

### 1.1 Generative models are training on synthetic data from generative models

Due to rapid advances in generative artificial intelligence (AI), synthetic data of all kinds is rapidly proliferating. Publicly available generative models have revolutionized the image, audio, and text domains [2–9], and are starting to impact videos, 3D models, graphs, tables, software, and websites. Companies like Google, Microsoft, and Shutterstock are incorporating generative models into their consumer services, and the output from these services and popular generative models like Stable Diffusion (for images) and ChatGPT (for text) tend to end up on the Internet. Quote overheard at 2022 ICLR: "There will soon be more synthetic data than real data on the Internet."

Since training datasets for generative AI models tend to be sourced from the Internet, today's AI models are unwittingly being trained on increasing amounts of AI-synthesized data. **Figure 2** demonstrates that the popular LAION-5B dataset contains synthetic images from earlier generations of generative models (StyleGAN, AICAN, Pix2Pix, DALL-E, BigGAN — found via haveibeentrained.com).

AI-synthesized data is increasingly used by choice for several reasons:
1. Cheaper and easier than sourcing real-world samples
2. Synthetic data augmentation has empirically boosted AI system performance
3. Synthetic data can protect privacy (medical imaging)
4. Running out of real data to train enormous deep learning models

The witting or unwitting use of synthetic data to train generative models creates an **autophagous ("self-consuming") loop**. In mathematics: at one extreme a contraction mapping that collapses to a single point; at the other extreme an unstable positive feedback loop that diverges into bedlam. Biological analogy: feeding cattle with remains of other cattle → mad cow disease → fatal neurodegenerative disease. Coin a term: **Model Autophagy Disorder (MAD)**.

### 1.2 Contributions

Three key contributions:

**1. Realistic models for autophagous loops** — Three families:
- **Fully synthetic loop**: training dataset for each generation consists solely of synthetic data from previous generations. Shows *either quality (precision) or diversity (recall) decreases over generations*.
- **Synthetic augmentation loop**: training dataset = synthetic data + fixed set of real data. Shows *fixed real training data only delays the inevitable degradation*.
- **Fresh data loop**: training dataset = synthetic data + fresh set of real data each generation. Shows *with enough fresh real data, quality and diversity do not degrade over generations*.

**2. Sampling bias plays a key role in autophagous loops** — Without sampling bias: autophagy leads to rapid decline of both quality and diversity. With sampling bias: quality can be maintained but diversity degrades even more rapidly.

**3. Autophagous loop behaviors hold across a variety of generative models and datasets** — DDPM [59], StyleGAN-2 [58], WGAN [60], Normalizing Flows [61], trained on MNIST [62] and FFHQ [63].

---

## Section 2: Self-Consuming Generative Models (Methods)

### 2.1 Autophagous Processes

A sequence of generative models (G^t), where G^t is trained from scratch on dataset D^t = (D_r^t, D_s^t) comprising n_r^t real samples and n_s^t synthetic samples. First-generation G^1 trained on purely real data (n_s^1 = 0).

**Definition.** An *autophagous generative process* is a sequence (G^t) where each G^t is trained on data including samples from previous models.

**Definition.** A *MAD generative process* is a sequence (G^t) that follows a random walk such that E[dist(G^t, P_r)] increases with t.

**Claim.** Under mild conditions, an autophagous generative process is a MAD generative process.

### 2.2 Variants of autophagous processes (as described in contributions above)

### 2.3 Biased Sampling in Autophagous Loops

Universal **sampling bias parameter λ ∈ [0, 1]**, where λ=1 = unbiased, λ=0 = sampling from modes with zero variance. Implementations:
- **Gaussian model**: sample from N(μ_t, λΣ_t)
- **StyleGAN**: truncation parameter in style-space (λ < 1 = samples closer to mean of style-space)
- **DDPM**: classifier-free diffusion guidance [42]; λ = 1/(1+w) where w is guidance factor; 10% conditioning dropout during training

### 2.4 Metrics for MADness

- **Wasserstein distance (WD)** / Fréchet Inception Distance (FID): approximation of Wasserstein-2 distance between inception feature distributions of real and synthetic images
- **Precision**: fraction of synthetic samples closer to a real data example than their k-th nearest neighbor (k=5 in all experiments). Measures quality.
- **Recall**: fraction of real data samples inside support of learned generative distribution. Measures diversity. (k=5 in all experiments)
- **Note**: For MNIST DDPM, features extracted by LeNet instead of Inception network (digits not in domain of natural images); still called "FID" for consistency.

---

## Section 3: Fully Synthetic Loop

### 3.1 Gaussian theory (martingales)

For Gaussian reference P_r = N(μ_0, Σ_0), fitting G^t = N(μ_t, Σ_t):
- μ_t is a martingale (random walk drifting from μ_0 due to finite sample size)
- Σ_t is a supermartingale → **Proposition**: Σ_t →^{a.s.} 0 for any λ ≤ 1
- Sampling bias λ controls trade-off: smaller λ accelerates Σ_t collapse (diversity loss) but slows the μ_t random walk (quality)

### 3.2 Experimental Setups — Fully Synthetic Loop

- **DDPM**: conditional DDPM, T=500 diffusion steps, MNIST dataset, n_r^1 = n_s^t = 60k images for t≥2
- **StyleGAN2**: unconditional, FFHQ dataset **downsampled to 128×128** (to reduce computational cost), n_r^1 = n_s^t = 70k images for t≥2; synthetic samples from immediately preceding model G^{t-1}

### 3.3 Without sampling bias (λ=1): both quality and diversity decrease

**Figure 4**: FID (left), precision (middle), recall (right) for FFHQ and MNIST. Both precision and recall decrease; FID monotonically increases. Distribution undergoes random walk due to finite sample size. Modes eventually diverge completely — precision and recall eventually drop to zero.

**Figure 5**: t-SNE plots of MNIST (fully synthetic, λ=1). Modes progressively move away and merge together. By Generation 10, samples become almost illegible.

### 3.4 With sampling bias (λ<1): quality can increase, diversity decreases rapidly

- StyleGAN on FFHQ: λ=0.7; DDPM on MNIST: λ=0.5

**Figure 6**: FID, precision, recall. Precision does not decay (may even increase); recall decays significantly faster than unbiased case. FID still increases → still MAD.

**Figure 7**: t-SNE MNIST with λ=0.8. Modes collapse onto themselves (rather than merging together as in unbiased case). Generated samples remain legible. Appendix D: StyleGAN-2 cross-hatching artifacts do not appear but distribution significantly loses diversity.

Additional experiments: Gaussian mixture models, WGAN [60], Normalizing Flows [61] in Appendix B — all result in MAD processes.

---

## Section 4: Synthetic Augmentation Loop

### 4.1 Experimental Setups

- **DDPM**: conditional MNIST DDPM, T=500, D_s^t from previous generation with bias λ, n_r^1 = n_s^t = 60k; original MNIST real dataset always available at every generation: D_r^1 = D_r^t, n_r^t = 60k
- **StyleGAN2**: unconditional, FFHQ-128×128. At each generation t≥2: 70k images with λ=1 from G^{t-1}. Synthetic data pool = ALL previously generated samples → grows linearly: n_s^t = (t-1)×70k. Real FFHQ always present: n_r^t = 70k every generation.

### 4.2 Results

**Figure 8**: StyleGAN synthetic augmentation loop without sampling bias (λ=1): FID, precision, recall all degrade, but more slowly than fully synthetic loop. Cross-hatching artifacts still appear (Appendix F), similar to Figure 1, but with less prevalence.

**Figure 9**: DDPM MNIST with different λ values. FID still increases (more slowly). Sampling bias still allows precision to increase but accelerates recall loss. Some λ values better than others (λ=0.8 shown as best).

**Conclusion**: fixed real data only delays, does not prevent, MADness.

---

## Section 5: Fresh Data Loop

### 5.1 Experimental Setups

- n_r^1 = n_ini (initial real samples); subsequent generations: n_r^t = n_r real, n_s^t = n_s synthetic from G^{t-1}

Models:
- **Gaussian modeling**: P_r = N(0_d, I_d), d=100; unbiased moment estimation
- **DDPM**: conditional, T=500, MNIST

### 5.2 Initial models forgotten in fresh data loop

**Figure 10**: Wasserstein distance and FID for Gaussian (n_r=100, n_s=900) and MNIST DDPM (n_r=n_s=2k). Both with unbiased and biased sampling. Key finding: asymptotic WD/FID is **independent of n_ini** — converges to a limiting value that depends only on (n_r, n_s, λ):

lim_{t→∞} E[dist(G^t, P_r)] = WD(n_r, n_s, λ)

With fresh data, no inevitable increase in E[dist(G^t, P_r)] → fresh data loop **can prevent MAD**.

### 5.3 Phase transition in fresh data loop

**Effective sample size n_e**: find n_e such that E[dist(G(n_e), P_r)] = WD(n_r, n_s, λ). When n_e/n_r ≥ 1 → admissible (synthetic data effectively increases real samples). When n_e/n_r < 1 → synthetic data hurts.

**Figure 11**: As n_r increases, maximum admissible n_s converges (does not grow with n_r). Synthetic data helpful only when n_r is small.

**Figure 12**: More sampling bias (smaller λ) reduces admissible synthetic sample size. Limit λ→1 (unbiased) appears to always ensure effective sample size increases.

---

## Section 6: Discussion / Limitations / Future Work

- Without enough fresh real data, future generative models are doomed to MAD.
- "Doomsday scenario": if left uncontrolled for many generations, MAD could poison the quality and diversity of the entire Internet.
- **Recommendations**:
  - Practitioners using synthetic data deliberately: temper synthetic data habits
  - Data-scarce applications: our results guide how much real data is necessary
  - Medical imaging use case: ensure anonymous synthetic images are artifact-free and diverse; use new real data as much as possible
  - Practitioners with unwanted synthetic pollution: develop methods to identify and filter synthetic data
- **Watermarking** synthetic data: active research area. Reservation: watermarking deliberately introduces hidden artifacts that could be amplified by autophagy. "Autophagy-aware watermarking" opened as future research direction.
- **Extensions**:
  - Combinations of the three loop families (mixed real fixed + fresh + synthetic)
  - Link precision/diversity degradation to downstream AI task performance (e.g., classification)
  - Extension to text / LLMs (nothing image-specific about the conclusions)

---

## All Figure Captions

- **Figure 1**: Training generative AI models on synthetic data progressively amplifies artifacts. StyleGAN-2 succession, training data for generation t≥2 = synthetic images from generation t-1 (fully synthetic loop). Cross-hatched artifacts (possibly architectural fingerprint) progressively amplified.
- **Figure 2**: LAION-5B contains synthetic images from earlier generative models (StyleGAN, AICAN, Pix2Pix, DALL-E, BigGAN).
- **Figure 3**: Three autophagous loop variations: fully synthetic loop, synthetic augmentation loop, fresh data loop, with sampling bias parameter λ.
- **Figure 4**: Fully synthetic loop without sampling bias — FID, precision, recall for FFHQ and MNIST.
- **Figure 5**: t-SNE plots, MNIST, fully synthetic, λ=1. Modes progressively merge; generation 10 almost illegible.
- **Figure 6**: Fully synthetic loop with sampling bias. FID, precision, recall. Precision maintained; recall drops faster. Lines: StyleGAN FFHQ λ=0.7 (solid), DDPM MNIST λ=0.5 (dashed).
- **Figure 7**: t-SNE MNIST, fully synthetic, λ=0.8. Modes collapse onto themselves (not merging).
- **Figure 8**: Synthetic augmentation loop, FFHQ StyleGAN, λ=1. FID, precision, recall — degradation slower than fully synthetic.
- **Figure 9**: Synthetic augmentation loop DDPM MNIST with different λ values.
- **Figure 10**: Fresh data loop — WD and FID for Gaussian (n_r=100, n_s=900) and DDPM MNIST (n_r=n_s=2k). Asymptotic value independent of n_ini.
- **Figure 11**: Fresh data loop — admissible n_s does not increase with n_r (phase transition). Blue area = admissible region.
- **Figure 12**: Fresh data loop — sampling bias reduces admissible synthetic sample size.
- **Figure 13** (Appendix B.1): WGAN-GP on MNIST, fully synthetic loop, 100 generations. FID monotonically increases, precision and recall monotonically decrease.
- **Figure 14** (Appendix B.2): GMM estimated distributions after 1, 200, 2k iterations of fully synthetic loop. Modes lost asymptotically.
- **Figure 15** (Appendix B.2): Metric comparison for GMMs — overall variance vs. average modal variance vs. recall. Recall best captures diversity loss.
- **Figure 16** (Appendix B.3): DDPM MNIST fully synthetic loop, more generations and different λ values.
- **Figure 17** (Appendix B.4): Normalizing flow, 2D Rosenbrock distribution, 16 generations. Tails lost regardless of sampling bias; λ<1 accelerates loss.
- **Figures 18–22** (Appendix C): FFHQ fully synthetic loop samples, λ=1, generations t=1,3,5,7,9.
- **Figures 23–25** (Appendix D): FFHQ fully synthetic loop samples, λ=0.7, generations t=1,3,5.
- **Figures 26–27** (Appendix E): MNIST DDPM samples. Figure 26: λ=1, modes drift and merge. Figure 27: λ=0.8, modes collapse around single high-quality image.
- **Figures 28–29** (Appendix F): FFHQ synthetic augmentation loop, λ=1, generations t=3 and t=6.
- **Figure 30** (Appendix G): Effective sample size n_e/n_r for different memory K (number of previous generations sampled from).
- **Figure 31** (Appendix G): Wasserstein distance as whole dataset size increases, for different p and sampling bias λ.

Total figures in paper: **31 figures** (as stated in arXiv metadata).

---

## Baselines, Metrics, Datasets, Models

**Models used:**
- Conditional DDPM [Ho et al., NeurIPS 2020], T=500 diffusion steps
- StyleGAN2 [Karras et al., CVPR 2020], unconditional
- WGAN-GP [Gulrajani et al., NeurIPS 2017]
- Normalizing Flows (GLOW architecture [8 coupling layers, hidden dim=64])
- Multivariate Gaussian and Gaussian Mixture Models (toy/analytical)

**Datasets:**
- MNIST (60k training, 10k test handwritten digits)
- FFHQ (70k faces, downsampled to 128×128)
- 2D Rosenbrock distribution (10^4 samples, for normalizing flow)
- 25-mode 2D GMM [following setup from ref. 82]

**Metrics:**
- FID (Fréchet Inception Distance) — Wasserstein-2 approximation via Inception features; LeNet features for MNIST
- Precision (k=5 nearest neighbors)
- Recall (k=5 nearest neighbors)
- Wasserstein distance (WD) — for Gaussian theoretical analysis
- Effective sample size n_e — for fresh data loop phase transition analysis
- t-SNE visualizations

**No baselines in the traditional sense** — this is a theoretical/empirical analysis paper, not a competitive benchmark. The paper compares across: loop type (fully synthetic / augmentation / fresh), sampling bias λ values, and model architectures.

---

## Training Recipe Details

- **DDPM**: conditional, T=500 diffusion time steps; 10% conditioning dropout for classifier-free guidance experiments; no explicit optimizer/lr mentioned in main text
- **StyleGAN2**: unconditional, images downsampled to 128×128; no explicit optimizer/lr mentioned
- **Normalizing flow (GLOW)**: 8 coupling layers, hidden dim=64, trained for 20 epochs, batch size=256, convergence monitored via validation likelihood
- **Hardware**: not mentioned in the retrieved text
- **Data sizes**: DDPM MNIST n_r^1 = n_s^t = 60k; StyleGAN FFHQ n_r^1 = n_s^t = 70k

---

## Related Work / Contemporaneous Papers

- [53] Shumailov et al. "The curse of recursion: Training on generated data makes models forget." (arXiv 2305.17493) — fully synthetic loop + augmentation/fresh loop for VAEs, GMMs, LLMs; fine-tuning (not from scratch)
- [54] Martínez et al. "Towards understanding the interplay of generative AI and the Internet." (arXiv 2306.06130) — fully synthetic loop with diffusion guidance; shows guidance prevents quality drop
- [55] Martínez et al. "Combining generative AI and the Internet: heading towards evolution or degradation?" (arXiv 2303.01255) — synthetic augmentation loop with DDIM without sampling bias; poor performance over generations

---

## Key Equations

- E[μ_t | μ_{t-1}] = μ_{t-1} (martingale), E[Σ_t | Σ_{t-1}] = λΣ_{t-1} (supermartingale) — Equation (2)
- **Proposition**: Σ_t →^{a.s.} 0 for any λ ≤ 1 — Equation (1), proved in Appendix A
- lim_{t→∞} E[dist(G^t, P_r)] = WD(n_r, n_s, λ) — Equation (3)
- Effective sample size: find n_e s.t. E[dist(G(n_e), P_r)] = WD(n_r, n_s, λ) — Equation (4)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34604d13-c673-45ee-b997-c0f8b7865124",
  "isSidechain": true,
  "agentId": "a3beaf73a9e1f198f",
  "requestId": "req_011CbE2GTXm5x52g4HVDqti8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "530af2bd-a8bc-46f8-b57d-5a9bacdd16f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "e1199c41-0624-4bbe-a3c3-3e8c7b3fc1ae",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MtSHYer3dXsppCwPpYygdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24662,
      "cache_read_input_tokens": 23020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24662,
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
