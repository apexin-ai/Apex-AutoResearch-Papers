# Research conversation: I need to find and read the paper "Agentic Rubrics as Contextual Verifiers for SWE Agents" (arXiv:2601.04171, Jan 2026, 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6efbd8b1b32207f4.jsonl`
- **Structured JSON:** [`d7ef992ff948c03b41e1.json`](../../sessions/d7/d7ef992ff948c03b41e1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-10T19:12:14.896Z_

I need to find and read the paper "Agentic Rubrics as Contextual Verifiers for SWE Agents" (arXiv:2601.04171, Jan 2026, Scale AI). 

Please:
1. Use WebSearch to find this paper
2. Use WebFetch to read the abstract and key method sections
3. Report: what exactly does it do? How does it differ from process-level reasoning evaluation? What are its key results (the reviewer mentions 54.2% on SWE-bench Verified with Qwen3-Coder-30B)? How should it be differentiated from a diagnostic reasoning PRM?

Be thorough - I need enough detail to write a proper citation and differentiation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "a6efbd8b1b32207f4",
  "type": "user",
  "uuid": "03da1872-6282-4ad9-9a1d-5c2499afb852",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:12:14.899Z_

```json
{
  "parentUuid": "03da1872-6282-4ad9-9a1d-5c2499afb852",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "001180e5-7282-4925-bbd3-1854aa2f10be",
  "timestamp": "2026-05-10T19:12:14.899Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:12:17.111Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then search for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "001180e5-7282-4925-bbd3-1854aa2f10be",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRGWK3VmWvGQWGF6buM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e98b043-c510-4548-ab4c-d5e685ee0c7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrtGL5hnZca3gkWdou3kYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 712,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:12:17.282Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Q5F4TJoXspRnRyqammEdYm`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e98b043-c510-4548-ab4c-d5e685ee0c7f",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRGWK3VmWvGQWGF6buM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e1e65d5-e1d2-4033-8a8a-b3670d3ae214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrtGL5hnZca3gkWdou3kYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 8223,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 712
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 712,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-10T19:12:17.286Z_

<details><summary>↩ Tool result · `toolu_01Q5F4TJoXspRnRyqammEdYm`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "1e1e65d5-e1d2-4033-8a8a-b3670d3ae214",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "a6efbd8b1b32207f4",
  "type": "user",
  "uuid": "9d81f81b-ac19-49b4-ade4-c6e722e03f9e",
  "sourceToolAssistantUUID": "1e1e65d5-e1d2-4033-8a8a-b3670d3ae214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:12:20.159Z_



Now let me search for the paper and fetch it from arXiv.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d81f81b-ac19-49b4-ade4-c6e722e03f9e",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRGgkr2yFsgY8HF59do",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54e874ce-8c41-4e0b-97a6-73bc3e54910c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJ1BCgd33YBb8sTBZdzjUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T19:12:21.582Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LnvB7Dy5FKdX3jNGMssU3H`</summary>

```json
{
  "query": "Agentic Rubrics Contextual Verifiers SWE Agents arXiv 2601.04171 Scale AI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54e874ce-8c41-4e0b-97a6-73bc3e54910c",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRGgkr2yFsgY8HF59do",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a97856e-046b-482e-a6a3-e2987688477e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJ1BCgd33YBb8sTBZdzjUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1911,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T19:12:22.455Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D6ZxoKAU47djUmZG6yLex7`</summary>

```json
{
  "query": "\"Agentic Rubrics as Contextual Verifiers\" SWE-bench Verified Qwen3-Coder"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a97856e-046b-482e-a6a3-e2987688477e",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRGgkr2yFsgY8HF59do",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14f5baef-4045-464f-9fe7-e47d68fdfb4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJ1BCgd33YBb8sTBZdzjUe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1911,
      "cache_read_input_tokens": 8935,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1911
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 8935,
          "cache_creation_input_tokens": 1911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1911,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T19:12:29.706Z_

<details><summary>↩ Tool result · `toolu_01LnvB7Dy5FKdX3jNGMssU3H`</summary>

```text
Web search results for query: "Agentic Rubrics Contextual Verifiers SWE Agents arXiv 2601.04171 Scale AI 2026"

Links: [{"title":"[2601.04171] Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://arxiv.org/abs/2601.04171"},{"title":"Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://arxiv.org/pdf/2601.04171"},{"title":"Paper page - Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://huggingface.co/papers/2601.04171"},{"title":"(PDF) Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://www.researchgate.net/publication/399559433_Agentic_Rubrics_as_Contextual_Verifiers_for_SWE_Agents"},{"title":"Agentic Rubrics as Contextual Verifiers for SWE Agents | OpenReview","url":"https://openreview.net/forum?id=edYwO6bEJD"},{"title":"[Quick Review] Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://liner.com/review/agentic-rubrics-as-contextual-verifiers-for-swe-agents"},{"title":"Agentic Rubrics as Contextual Verifiers for SWE Agents - AI for Dummies - Understand the Latest AI Papers in Simple Terms","url":"https://ai-search.io/papers/agentic-rubrics-as-contextual-verifiers-for-swe-agents"},{"title":"Agentic Rubrics as Contextual Verifiers for SWE Agents - YouTube","url":"https://www.youtube.com/watch?v=ryURmuAI1I0"},{"title":"[Literature Review] Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://www.themoonlight.io/en/review/agentic-rubrics-as-contextual-verifiers-for-swe-agents"},{"title":"A Survey on Agent-as-a-Judge","url":"https://arxiv.org/html/2601.05111"}]

I found the paper you're looking for! Here are the key details:

## Agentic Rubrics as Contextual Verifiers for SWE Agents (arXiv 2601.04171)

The paper was submitted on January 7, 2026 by authors Mohit Raghavendra, Anisha Gunjal, Bing Liu, and Yunzhong He.

### Overview
Verification is critical for improving agents as it provides reward signals for Reinforcement Learning and enables inference-time gains through Test-Time Scaling (TTS). However, verification in software engineering agent settings often relies on code execution, which is difficult to scale due to environment setup overhead.

### The Approach
The paper explores Agentic Rubrics, where an expert agent interacts with the repository to create a context-grounded rubric checklist, and candidate patches are then scored against it without requiring test execution.

### Results
On SWE-Bench Verified under parallel TTS evaluation, Agentic Rubrics achieved a score of 54.2% on Qwen3-Coder-30B-A3B and 40.6% on Qwen3-32B, with at least a +3.5 percentage-point gain over the strongest baseline in their comparison set.

The paper shows that rubric scores are consistent with ground-truth tests while also flagging issues that tests do not capture, with agentic context gathering being essential for producing codebase-specific, unambiguous criteria. Together, these results suggest that Agentic Rubrics provide an efficient, scalable, and granular verification signal for SWE agents.

You can access the full paper on arXiv at https://arxiv.org/abs/2601.04171


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a97856e-046b-482e-a6a3-e2987688477e",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "a6efbd8b1b32207f4",
  "type": "user",
  "uuid": "17617b1f-729f-48cb-ad63-1ba743d412e7",
  "sourceToolAssistantUUID": "0a97856e-046b-482e-a6a3-e2987688477e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:12:30.139Z_

<details><summary>↩ Tool result · `toolu_01D6ZxoKAU47djUmZG6yLex7`</summary>

```text
Web search results for query: ""Agentic Rubrics as Contextual Verifiers" SWE-bench Verified Qwen3-Coder"

Links: [{"title":"Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://arxiv.org/html/2601.04171v1"},{"title":"[2601.04171] Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://arxiv.org/abs/2601.04171"},{"title":"Paper page - Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://huggingface.co/papers/2601.04171"},{"title":"Agentic Rubrics as Contextual Verifiers for SWE Agents | OpenReview","url":"https://openreview.net/forum?id=edYwO6bEJD"},{"title":"[Quick Review] Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://liner.com/review/agentic-rubrics-as-contextual-verifiers-for-swe-agents"},{"title":"[Literature Review] Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://www.themoonlight.io/en/review/agentic-rubrics-as-contextual-verifiers-for-swe-agents"},{"title":"Agentic Rubrics as Contextual Verifiers for SWE Agents - AI for Dummies - Understand the Latest AI Papers in Simple Terms","url":"https://ai-search.io/papers/agentic-rubrics-as-contextual-verifiers-for-swe-agents"},{"title":"Qwen3-Coder-Next: Pushing Small Hybrid Models","url":"https://qwen.ai/blog?id=qwen3-coder-next"},{"title":"(PDF) Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://www.researchgate.net/publication/399559433_Agentic_Rubrics_as_Contextual_Verifiers_for_SWE_Agents"},{"title":"Agentic Rubrics as Contextual Verifiers for SWE Agents","url":"https://static.scale.com/uploads/654197dc94d34f66c0f5184e/Scale-Agentic-Rubrics.pdf"}]

Based on the search results, here's what I found about "Agentic Rubrics as Contextual Verifiers" and its performance on SWE-bench with Qwen3-Coder:

## Overview

Agentic Rubrics is a method where an expert agent interacts with the repository to create a context-grounded rubric checklist, and candidate patches are then scored against it without requiring test execution.

## Key Performance Results

On SWE-Bench Verified under parallel TTS evaluation, Agentic Rubrics achieve a score of 54.2% on Qwen3-Coder-30B-A3B and 40.6% on Qwen3-32B, with at least a +3.5 percentage-point gain over the strongest baseline.

## Why It's Effective

Agentic rubrics use targeted tool calls (search and file inspection) to ground criteria in concrete repository entities (files, classes, methods), making items more specific and consistently gradable; non-agentic rubrics are often high-level, which increases ambiguity and can lead to false positives.

## Context Importance

Using Sonnet-4.5 for rubric generation without repository access reduces Best@16 by 4.0 points on Qwen3-32B rollouts and 1.4 points on Qwen3-Coder-30B-A3B rollouts, showing that agentic context gathering improves both rubric quality and downstream selection.

The paper was published on arXiv in January 2026 (arXiv:2601.04171).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14f5baef-4045-464f-9fe7-e47d68fdfb4e",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "a6efbd8b1b32207f4",
  "type": "user",
  "uuid": "ef9fcf15-54cb-47b6-88d8-eba33935ebf9",
  "sourceToolAssistantUUID": "14f5baef-4045-464f-9fe7-e47d68fdfb4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T19:12:33.510Z_

Good, I have initial context. Now let me fetch the full paper content from the arXiv HTML version for detailed method description, and also fetch the abstract page and the Scale AI PDF for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef9fcf15-54cb-47b6-88d8-eba33935ebf9",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRHdXQrfd5LukSWdXjP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09103eae-e400-4dc8-b7d6-a10bb5ef7876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbQ5G2YFBCmUzyhy1oRT82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 10846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2237,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T19:12:35.412Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VuG9pFAbYwX1iXoaGFYtTk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.04171",
  "prompt": "Extract the complete abstract, the full list of authors and their affiliations, and the submission date. Also extract any summary of the method, results, and key contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09103eae-e400-4dc8-b7d6-a10bb5ef7876",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRHdXQrfd5LukSWdXjP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9b3fc53-5797-423f-bc2c-c7abc6024aa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbQ5G2YFBCmUzyhy1oRT82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 10846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2237,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T19:12:40.579Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019W38CSWKus9kSXDhgBotvm`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.04171v1",
  "prompt": "Extract the full detailed content of the paper. I need:\n1. The complete abstract\n2. The full Introduction section\n3. The complete Method/Approach section - how exactly do Agentic Rubrics work? What is the rubric generation process? What is the scoring process? What tools does the expert agent use?\n4. The Experiments section - what baselines are compared? What are the exact numerical results? What is the evaluation setup (how many candidates, which models)?\n5. The Related Work section - how do the authors position this relative to process reward models (PRMs), outcome reward models (ORMs), and other verification approaches?\n6. The Ablation studies - what happens without agentic context? What is the effect of rubric quality?\n7. The Conclusion and limitations\nBe as thorough as possible - extract all key details, numbers, and methodological specifics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9b3fc53-5797-423f-bc2c-c7abc6024aa9",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRHdXQrfd5LukSWdXjP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3452e3ba-cb59-461e-81cd-d2e5b4647686",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbQ5G2YFBCmUzyhy1oRT82",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2237,
      "cache_read_input_tokens": 10846,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 419,
          "cache_read_input_tokens": 10846,
          "cache_creation_input_tokens": 2237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2237,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:12:41.077Z_

<details><summary>↩ Tool result · `toolu_01VuG9pFAbYwX1iXoaGFYtTk`</summary>

```text
# Paper Summary: Agentic Rubrics as Contextual Verifiers for SWE Agents

**Submission Date:** January 7, 2026

**Authors:** Mohit Raghavendra, Anisha Gunjal, Bing Liu, Yunzhong He
*(Affiliations not provided in the document)*

## Abstract
The paper addresses verification challenges in software engineering agents by proposing "Agentic Rubrics." Rather than relying on code execution for verification, an expert agent examines the repository to generate context-specific evaluation criteria. Candidate patches are then assessed against this rubric without requiring test execution. The approach achieved 54.2% on Qwen3-Coder-30B-A3B and 40.6% on Qwen3-32B benchmarks, with performance gains exceeding 3.5 percentage points compared to baseline methods.

## Key Contributions

**Method:** An agent generates "a context-grounded rubric checklist" by interacting with the codebase, enabling efficient verification without environmental setup overhead.

**Results:** The approach demonstrates consistency with ground-truth tests while identifying issues that traditional testing misses.

**Significance:** The authors contend that rubrics offer "an efficient, scalable, and granular verification signal" for agent-based software engineering tasks, particularly valuable for scaling reinforcement learning and test-time inference optimization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9b3fc53-5797-423f-bc2c-c7abc6024aa9",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "a6efbd8b1b32207f4",
  "type": "user",
  "uuid": "78aaf20b-d230-458c-ab58-1be918c930ad",
  "sourceToolAssistantUUID": "b9b3fc53-5797-423f-bc2c-c7abc6024aa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T19:13:17.814Z_

<details><summary>↩ Tool result · `toolu_019W38CSWKus9kSXDhgBotvm`</summary>

```text
# Comprehensive Summary: Agentic Rubrics as Contextual Verifiers for SWE Agents

## 1. Abstract

The paper introduces Agentic Rubrics, an execution-free verification approach for software engineering agents. An expert agent explores the codebase to generate "context-grounded rubric checklists" that candidate patches are then scored against without requiring test execution. On SWE-Bench Verified with parallel test-time scaling, the method achieves 54.2% on Qwen3-Coder-30B and 40.6% on Qwen3-32B, demonstrating "+3.5 to +4.6 percentage-point gains" over strongest baselines. The authors demonstrate rubric scores align with ground-truth tests while also surfacing issues tests don't capture.

## 2. Introduction

**Core Problem**: Verification is critical for SWE agents but faces a fundamental tradeoff. Execution-based verification (running tests) is environment-aware but expensive due to sandbox overhead and may yield brittle signals. Execution-free methods (classifiers, similarity metrics) are operationally lightweight but less reliable and prone to "shallow cues rather than functional correctness."

**Key Insight**: The paper invokes "Verifier's Law," which links AI system training efficiency to verification reliability. For SWE agents, strong verification serves dual purposes: providing supervision for reinforcement learning and enabling test-time scaling through best-of-K selection.

**Proposed Solution**: Rather than writing rubrics from problem statements alone (often under-specified), the authors make rubric generation "agentic"—an expert agent actively explores the repository using tools to ground criteria in "relevant code paths, interfaces, and project conventions," yielding more specific and consistently gradable items.

## 3. Method/Approach: How Agentic Rubrics Work

### 3.1 Rubric Generation Process

The rubric-generation agent is built on the SWE-Agent scaffold, modified with a custom system prompt instructing it to explore the repository and produce a `rubrics.yaml` file.

**Repository Interaction Tools Available**:
- File search and inspection
- Shell command execution  
- Code browsing within the sandboxed environment

**Rubric Structure**: Each rubric consists of 15-26 total items organized along four axes with natural-language criteria and importance weights (1=nice-to-have, 2=important, 3=must-have):

1. **File Change** (4–8 items): "edits are minimal, local, and sufficient"
2. **Spec Alignment** (3–6): "patch satisfies requirements in issue description"
3. **Integrity** (3–6): "no-cheating constraints (e.g., no test weakening, broad refactors)"
4. **Runtime** (3–6): "intended runtime behavior without execution-time issues"

The agent explores the codebase, identifies relevant code entities, and writes specific, repository-grounded criteria. If YAML parsing fails, the generation attempt is considered invalid.

### 3.2 Rubric Grading/Scoring Process

Given a candidate patch, an LLM judge assigns each rubric item a binary score (0 or 1). Scores are aggregated with importance weights:

**S = Σ(w_i × s_i) / Σ(w_i)**

This yields a normalized verifier score S ∈ [0,1] used for reranking candidates.

**Judge Model**: The paper uses GPT-5 (low reasoning) as the judge, though ablations show judge capability has modest effect (52.6% to 55.0% performance range).

## 4. Experiments: Setup and Results

### 4.1 Evaluation Protocol

**Benchmark**: SWE-Bench Verified (500 problems)
**Candidate Generation**: K=16 independent rollouts per problem using the SWE-Agent scaffold
**Generator Models Tested**:
- Qwen3-32B (Instruct, max 30 turns, temperature 1.0)
- Qwen3-Coder-30B-A3B (max 50 turns, temperature 1.0)

**Success Criterion**: Problem resolved if candidate passes both Fail-To-Pass and Pass-To-Pass ground-truth tests

**Metrics**: Best@K resolution percentage (selecting highest-scoring patch across K candidates)

### 4.2 Baseline Comparisons

**Non-Agentic Verifiers** (no artifact generation):
- Self-Consistency: "select patch with highest average similarity to remaining K-1 candidates"
- Patch Classifier: LLM predicts correctness, outputs continuous [0,1] score

**Agentic Verifiers** (artifact-based):
- Agentic Tests: Agent generates problem-specific test suite; candidates scored by execution
- Agentic Patch Similarity: Agent generates proxy reference patch; candidates reranked by LLM-judged similarity
- Agentic Rubrics (this work)

**Artifact Generation**: All agentic methods use Claude Sonnet-4.5 as expert agent (30-turn budget); verification scoring uses GPT-5 (low reasoning)

### 4.3 Numerical Results

| Model | Method | Best@16 |
|-------|--------|---------|
| Qwen3-32B | Random | 22.6% |
| Qwen3-32B | Self-Consistency | 33.2% |
| Qwen3-32B | Patch Classifier | 37.1% |
| Qwen3-32B | Agentic Patch Similarity | 35.0% |
| Qwen3-32B | Agentic Rubrics | **40.6%** |
| Qwen3-Coder | Patch Classifier | 50.2% |
| Qwen3-Coder | Agentic Patch Similarity | 49.6% |
| Qwen3-Coder | Agentic Rubrics | **54.2%** |
| Reference | Oracle Pass@16 | 51.4% / 65.6% |

**Key Finding**: Rubric-based verifier maintains performance advantage across scaling curves (K < 16).

### 4.4 Score Quality Analysis

**Rubric-GT Test Alignment**: Figure 3 shows rubric scores for ground-truth passing patches concentrate near 0.85–1.0, while failing patches scatter 0.4–0.5 range, with "ROC-AUC of 0.886 and PR-AUC of 0.722" indicating strong separation and high precision bias.

**Ground-Truth Patch Scoring**: Human-written reference patches receive mean rubric scores >0.8 from frontier models (Sonnet-4.5: 0.8233, Opus-4.5: 0.8658), demonstrating broad compatibility.

## 5. Ablation Studies

### 5.1 Rubric-Agent Model Capability

Best@16 performance by rubric-generator model on Qwen-Coder-30B rollouts:
- Frontier models (Sonnet-4.5, Opus-4.5, Gemini-3-Pro): ~54%
- Open-weight (Qwen3-Coder-30B): ~45%
- Non-coding (Qwen3-32B): ~43%

**Finding**: "More capable models generate substantially more rubrics per instance" (Sonnet-4.5 averages >20 rubrics; others ~10), enabling finer-grained differentiation.

### 5.2 Training Open-Weight Rubric Agents

Fine-tuning Qwen3-32B as agentic rubric generator (2,000 trajectories from Sonnet-4.5, 2 epochs, AdamW, batch 32, 4×8xH100 GPUs) substantially outperforms fine-tuning same model as patch classifier on same data, suggesting "ability to produce structured rubrics is trainable" and a stronger objective than binary classification.

### 5.3 Impact of Repository Grounding

Comparing agentic vs. non-agentic rubrics (same model, no codebase access):

Non-agentic rubrics: "often high-level (e.g., 'touches the right code path'), increasing ambiguity"

Agentic rubrics: Use "targeted tool calls to ground criteria in concrete repository entities"

**Performance Impact**: Removing repository interaction reduces Best@16 by "-4.0 points on Qwen3-32B, -1.4 points on Qwen3-Coder," demonstrating "agentic context gathering improves both rubric quality and downstream selection."

### 5.4 Judge Model Sensitivity

GPT-5 judge capability effects on Sonnet-4.5 rubrics:
- GPT-5-mini: 52.6%
- GPT-5 Low Reasoning: 54.2%
- GPT-5 Medium: 54.3%
- GPT-5 High: 55.0%

**Finding**: Judge capability has "small but non-trivial effect"; atomic rubric design enables scoring with lower reasoning effort.

## 6. Utility Analysis

### 6.1 When Rubrics and Tests Agree

In cases where rubric (score ≥0.7) and ground-truth tests both accept/reject patches:
- **78% high-utility**: Judgments based on core semantics, API/compatibility, structure/scope, edge coverage
- **22% low-utility**: Low-signal, over-specified, or test-mismatched rubrics

### 6.2 When Rubrics Reject GT-Passing Patches

For cases where tests pass but rubric score <0.7:
- **54% high-utility**: "Often flagging missed root causes or missing edge-case coverage"
- **46% low-utility**: Over-specification, redundancy, rule mismatches

**Interpretation**: Rubrics surface concerns beyond test coverage—e.g., incomplete fixes or undercovered edge cases.

## 7. Related Work

The paper positions itself within two research areas:

**Coding Agents and Test-Time Scaling**: Acknowledges SWE environments (SWE-Bench, R2E-Gym) and agentic scaffolds (SWE-Agent, Agentless, OpenHands). Prior TTS work uses verifiers like patch classifiers and test-generation agents.

**Rubrics as Verifiers**: Notes rubrics are increasingly used for LLM evaluation and as reward signals in reinforcement learning, but claims this is "first work" demonstrating "context-aware rubrics as effective verifiers for SWE tasks" with "scalable test-time verification."

**Implicit Comparison**: The approach differs from process reward models (PRMs) by generating interpretable criteria rather than learned scalar rewards, and from outcome reward models (ORMs) by operating without test execution.

## 8. Limitations and Future Work

**Key Limitations Acknowledged**:

1. **Post-training Integration**: Studied only in parallel TTS setting; integration as RLVR-style reward signals requires addressing "reward hacking, non-stationarity, and credit assignment."

2. **Rubric Quality Variance**: While utility analysis shows "most judgments are high-utility," a subset exhibits "low-utility modes (over-specification, redundancy, rubric–test mismatches)."

3. **Practical Deployment**: Suggests human-in-the-loop refinement—"lightweight review/editing, rubric-template reuse, and targeted prompts"—as next steps for "preserving auditability."

## 9. Cost Analysis

From Appendix A.3 (average per-instance cost for Best@16):
- Agentic Tests: $0.515 ($0.499 artifact + $0.016 grading)
- Agentic Patch Similarity: $0.736 ($0.640 + $0.096)
- Agentic Rubrics: $0.293 ($0.245 + $0.048)

Rubrics achieve "higher performance at 40% lower cost" than alternatives.

## 10. Key Takeaways

- Execution-free rubric-based verification outperforms classifiers and heuristic baselines in test-time scaling
- Repository-grounded rubric generation is essential; non-agentic rubrics lose 1.4–4.0 points
- Rubric scores correlate strongly with ground-truth tests (PR-AUC 0.722) while surfacing additional failure modes
- Rubric generation capability is distillable into smaller open-weight models via fine-tuning
- Cost-effective compared to test execution and patch similarity approaches
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3452e3ba-cb59-461e-81cd-d2e5b4647686",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "a6efbd8b1b32207f4",
  "type": "user",
  "uuid": "11324fa3-9159-4c5e-9a66-65895698d88d",
  "sourceToolAssistantUUID": "3452e3ba-cb59-461e-81cd-d2e5b4647686",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T19:13:23.750Z_

Excellent -- I now have very thorough coverage. Let me also fetch one more detail about how the authors explicitly differentiate from PRMs and ORMs, since that's a key part of your question.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11324fa3-9159-4c5e-9a66-65895698d88d",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRM9N7QGd3s4PN1taUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3067bd64-1631-439a-80ef-9ef41bd1678a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o5irduRpd9Yc8gBGyFV5S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 13083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T19:13:28.956Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Bop3bXD9QUGNMzmW55R2Xx`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.04171v1",
  "prompt": "Focus specifically on these aspects:\n1. How do the authors discuss process reward models (PRMs) vs outcome reward models (ORMs)? Do they explicitly compare to or differentiate from PRMs?\n2. What exactly is the 'Verifier's Law' they invoke?\n3. What is the exact scoring formula and how is it different from a learned reward signal?\n4. Do they mention diagnostic reasoning, chain-of-thought verification, or step-by-step reasoning evaluation at all?\n5. What is the exact structure of the rubrics.yaml output? Can you give an example of a rubric item?\n6. How do they define 'agentic' in their context - what specific actions does the rubric-generating agent take?\n7. Do they compare to any process-based or step-level reward approaches in related work?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3067bd64-1631-439a-80ef-9ef41bd1678a",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRM9N7QGd3s4PN1taUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c8c8d78-d796-4cbb-91ea-14d2b2a6446c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o5irduRpd9Yc8gBGyFV5S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 13083,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3793
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 13083,
          "cache_creation_input_tokens": 3793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3793,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T19:13:42.376Z_

<details><summary>↩ Tool result · `toolu_01Bop3bXD9QUGNMzmW55R2Xx`</summary>

```text
# Analysis of Agentic Rubrics Paper

## 1. Process vs Outcome Reward Models

The paper does **not explicitly compare to Process Reward Models (PRMs)**. Instead, it focuses on execution-free verification through rubric-based scoring. The authors position their work within "rubric-based verification" literature but don't directly engage with PRM methodology. They mention that "Verification is critical for improving agents: it provides the reward signal for Reinforcement Learning" but treat rubrics as an alternative verification paradigm rather than comparing mechanistic approaches to process-level reasoning.

## 2. Verifier's Law

The authors invoke "Verifier's Law" citing Jason Wei (2025), describing it as: **"the ease of training AI systems on a task to the efficiency and reliability of verifying candidate solutions"**. This is presented as motivation for why verification matters, but the paper doesn't elaborate on its specific formal definition.

## 3. Scoring Formula

The rubric scoring is fundamentally different from learned reward models:

**Formula**: `S = (Σ w_i × s_i) / (Σ w_i)`

Where:
- `s_i ∈ {0,1}` is a **binary judgment** per criterion
- `w_i ∈ {1,2,3}` represents importance weights (nice-to-have/important/must-have)
- Result: `S ∈ [0,1]` as final verifier score

This is **not learned**—it's a fixed aggregation function applied to explicit, interpretable criteria rather than learned feature representations.

## 4. Diagnostic Reasoning / Chain-of-Thought

The paper does **not mention process reward models, step-by-step reasoning evaluation, or chain-of-thought verification** in their methodology. Their verification is patch-level and criterion-level but not step-trajectory-aware. However, they do note that "rubrics provide interpretable natural-language feedback" and can surface diagnostic concerns like "unnecessary edits or missing edge-case handling."

## 5. Rubrics.yaml Structure

The paper specifies four rubric axes with item counts:

- **File Change** (4-8 items): "edits are minimal, local, and sufficient for the fix"
- **Spec Alignment** (3-6): "the patch satisfies the requirements in the issue description"
- **Integrity** (3-6): "no-cheating and hygiene constraints (e.g., no test weakening...)"
- **Runtime** (3-6): "the changes imply the intended runtime behavior"

Each item is a tuple `(t_i, w_i)` where `t_i` is a "short natural-language criterion" and `w_i` is the weight. Example from Appendix A.9 shows criteria like: **"Modifies the AnchoredLocatorBase.__call__ method in...without modifying unrelated methods"** (highly specific, repository-grounded).

## 6. Definition of "Agentic"

"Agentic" in this context means the rubric-generation agent **actively explores the repository using tools**. Specifically: **"an expert agent interacts with the repository to create a context-grounded rubric"**. Actions include:
- File inspection and code navigation
- Shell command execution
- Tracing call sites
- Inspecting surrounding code and contracts
- Reasoning about edge cases

The contrast is "non-agentic rubrics" generated from problem statements alone without repository interaction, which are "often high-level" and "increase ambiguity."

## 7. Process-Based or Step-Level Reward Comparisons

The related work section acknowledges rubrics have been used as "reward signal to train LLMs during RL" but the paper **does not compare to process-level or step-by-step reasoning approaches**. Baselines include "Agentic Tests" and "Agentic Patch Similarity" but not intermediate reasoning verification methods.

---

**Key Distinction**: This work emphasizes **interpretability and repository grounding** over learned intermediate representations, making it orthogonal to process-reward-model research focused on reasoning trajectory verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c8c8d78-d796-4cbb-91ea-14d2b2a6446c",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "a6efbd8b1b32207f4",
  "type": "user",
  "uuid": "55b5cf66-98de-490c-b6d8-18ca4e8df109",
  "sourceToolAssistantUUID": "3c8c8d78-d796-4cbb-91ea-14d2b2a6446c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T19:14:38.397Z_

I now have comprehensive detail. Here is a thorough report.

---

## "Agentic Rubrics as Contextual Verifiers for SWE Agents" -- Detailed Report

**Citation**: Mohit Raghavendra, Anisha Gunjal, Bing Liu, Yunzhong He. "Agentic Rubrics as Contextual Verifiers for SWE Agents." arXiv:2601.04171, January 7, 2026. (Scale AI)

---

### What It Does

The paper introduces **Agentic Rubrics**, an execution-free verification method for software engineering (SWE) agents. The core idea is:

1. **Rubric Generation (Agentic)**: An expert agent (built on the SWE-Agent scaffold, using Claude Sonnet-4.5 with a 30-turn budget) actively explores the target repository -- inspecting files, tracing call sites, running shell commands -- and produces a structured `rubrics.yaml` file containing 15-26 natural-language criteria organized along four axes:
   - **File Change** (4-8 items): edits are minimal, local, and sufficient
   - **Spec Alignment** (3-6 items): patch satisfies the issue requirements
   - **Integrity** (3-6 items): no-cheating constraints (no test weakening, no broad refactors)
   - **Runtime** (3-6 items): intended runtime behavior without execution-time issues

   Each item is a tuple `(t_i, w_i)` where `t_i` is a short natural-language criterion grounded in concrete repository entities (files, classes, methods), and `w_i` is an importance weight in {1=nice-to-have, 2=important, 3=must-have}.

2. **Rubric Scoring**: Given a candidate patch, an LLM judge (GPT-5 low reasoning in the main experiments) assigns each rubric item a binary score `s_i in {0, 1}`. Final score: **S = sum(w_i * s_i) / sum(w_i)**, yielding S in [0,1]. The highest-scoring candidate among K=16 rollouts is selected (Best@K).

The critical word is "agentic" -- the rubric-generating agent does not merely read the issue description; it actively explores the codebase to ground criteria in specific code paths, interfaces, and project conventions. Example criterion: *"Modifies the AnchoredLocatorBase.__call__ method in [specific file path] without modifying unrelated methods."*

---

### Key Results

On **SWE-Bench Verified** (500 problems) with **parallel test-time scaling (Best@16)**:

| Generator Model | Method | Best@16 |
|---|---|---|
| Qwen3-32B | Random baseline | 22.6% |
| Qwen3-32B | Self-Consistency | 33.2% |
| Qwen3-32B | Patch Classifier | 37.1% |
| Qwen3-32B | Agentic Patch Similarity | 35.0% |
| Qwen3-32B | **Agentic Rubrics** | **40.6%** (+3.5pp over strongest baseline) |
| Qwen3-Coder-30B-A3B | Patch Classifier | 50.2% |
| Qwen3-Coder-30B-A3B | Agentic Patch Similarity | 49.6% |
| Qwen3-Coder-30B-A3B | **Agentic Rubrics** | **54.2%** (+4.0pp over strongest baseline) |

Additional quantitative findings:
- **Score quality**: ROC-AUC of 0.886 and PR-AUC of 0.722 for rubric scores vs. ground-truth test outcomes
- **Cost**: $0.293 per instance average (vs. $0.515 for Agentic Tests, $0.736 for Agentic Patch Similarity) -- 40% cheaper than alternatives while outperforming them
- **Ablation -- removing repository grounding**: Best@16 drops by -4.0pp on Qwen3-32B and -1.4pp on Qwen3-Coder when the rubric agent has no codebase access
- **Judge sensitivity**: Modest effect (52.6% with GPT-5-mini to 55.0% with GPT-5 high reasoning), because atomic rubric design keeps each judgment simple
- **Distillability**: Fine-tuning Qwen3-32B on 2,000 Sonnet-4.5 rubric trajectories substantially outperforms fine-tuning the same model as a patch classifier on the same data

---

### How It Differs from Process-Level Reasoning Evaluation (PRMs)

This is the key differentiation you need. The paper does **not** explicitly discuss or compare to Process Reward Models (PRMs). But the methodological differences are fundamental:

1. **What is evaluated**: A PRM evaluates intermediate reasoning steps in a solution trajectory (e.g., each step in a chain-of-thought). Agentic Rubrics evaluate the **final output artifact (the patch)** against externally generated criteria. They are outcome-level verifiers, not process-level verifiers. They never inspect the agent's reasoning trace or intermediate actions.

2. **How the signal is produced**: A PRM uses a **learned reward function** -- a neural network trained to assign scalar scores to intermediate steps. Agentic Rubrics use a **handcrafted aggregation function** (`S = sum(w_i * s_i) / sum(w_i)`) over **explicit natural-language criteria** judged by an LLM. There is no learned embedding or reward head.

3. **Source of verification knowledge**: A PRM's verification knowledge is implicit in its learned weights, derived from training data of correct vs. incorrect reasoning steps. Agentic Rubrics' verification knowledge is **explicitly extracted from the repository** by an agent at inference time -- it is contextual, instance-specific, and interpretable.

4. **Granularity type**: PRMs provide step-level granularity along the temporal axis of reasoning. Agentic Rubrics provide criterion-level granularity along the semantic axis of correctness (file changes, spec alignment, integrity, runtime). These are orthogonal decompositions.

5. **Interpretability**: Each rubric item is a readable natural-language statement that can be audited, edited, or overridden by a human. PRM scores are opaque scalars.

6. **Generalization mechanism**: PRMs generalize through learned features. Agentic Rubrics generalize through the rubric-generating agent's ability to explore new codebases and produce fresh criteria -- the rubric is regenerated for each problem instance.

---

### How It Should Be Differentiated from a Diagnostic Reasoning PRM

If you are comparing Agentic Rubrics against a "diagnostic reasoning PRM" (a process reward model that evaluates the quality of diagnostic/reasoning steps), the distinctions are:

- **Agentic Rubrics are not a reward model at all.** They are a structured evaluation protocol -- a checklist generated by an agent and scored by an LLM judge. There is no model training involved in the verification itself (though the rubric-generating agent can be fine-tuned).

- **Agentic Rubrics do not examine the agent's process.** They evaluate only the patch (the outcome). A diagnostic reasoning PRM would evaluate whether the agent's intermediate reasoning steps (e.g., "I hypothesize the bug is in function X because...") are sound.

- **Agentic Rubrics are codebase-contextual, not task-generic.** The criteria are dynamically generated per repository per issue. A PRM is trained once and applied across problems.

- **Agentic Rubrics operate at the semantic/functional level** ("Does the patch modify the right method? Does it handle edge case X?"), whereas a diagnostic reasoning PRM operates at the **epistemic/inferential level** ("Is this reasoning step logically valid? Does this hypothesis follow from the evidence?").

- **The paper's authors position rubrics as complementary to tests**, not as trajectory evaluators. They show rubrics can flag issues that tests miss (54% of rubric-rejected but test-passing patches were flagged for legitimate concerns like missed root causes or uncovered edge cases). This is an outcome-quality signal, not a reasoning-quality signal.

In summary: Agentic Rubrics are an **interpretable, instance-specific, execution-free outcome verifier** that uses repository-grounded checklists. They are neither process-level nor learned. They occupy a different point in the verification design space from PRMs entirely -- they verify "what was produced" rather than "how it was reasoned about."

---

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2601.04171)
- [arXiv full HTML paper](https://arxiv.org/html/2601.04171v1)
- [Hugging Face paper page](https://huggingface.co/papers/2601.04171)
- [Scale AI PDF](https://static.scale.com/uploads/654197dc94d34f66c0f5184e/Scale-Agentic-Rubrics.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55b5cf66-98de-490c-b6d8-18ca4e8df109",
  "isSidechain": true,
  "agentId": "a6efbd8b1b32207f4",
  "requestId": "req_011CauRNxP7Xz17AB9NcTfWy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb9c07b4-55a3-44df-8c4d-3e13e289f9a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KqrkzP5HmyyU1KqS8MPRL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 16876,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1382,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---
