# Research conversation: I need to verify the paper "Decomposing Attention To Find Context-Sensitive Neurons" by Gibson (Oct 2025, arXiv:2510.033

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-adcd30016e9e7ed6f.jsonl`
- **Structured JSON:** [`cc7006d2c4a070512d0d.json`](../../sessions/cc/cc7006d2c4a070512d0d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-10T18:23:53.357Z_

I need to verify the paper "Decomposing Attention To Find Context-Sensitive Neurons" by Gibson (Oct 2025, arXiv:2510.03315). Claims to verify:

1. Does this paper exist at arXiv:2510.03315?
2. Does it decompose attention into structural (position-dependent, content-agnostic) and content-dependent components?
3. Was it demonstrated only on GPT2-Small?
4. Is it purely an interpretability paper, or does it suggest inference applications?

Search for:
- "arXiv 2510.03315"
- "Gibson decomposing attention context-sensitive neurons 2025"
- "decomposing attention structural content-dependent components"

Use WebFetch on the arXiv page to read the abstract and understand what the paper actually proposes. Report exactly what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adcd30016e9e7ed6f",
  "type": "user",
  "uuid": "02f7751c-d538-4353-b2f0-af6a6921447b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:23:53.361Z_

```json
{
  "parentUuid": "02f7751c-d538-4353-b2f0-af6a6921447b",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
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
  "uuid": "77643d5a-7895-479b-b0d5-43f88a12f05f",
  "timestamp": "2026-05-10T18:23:53.361Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:23:56.190Z_



I'll start by loading the WebSearch and WebFetch tools, then search for this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77643d5a-7895-479b-b0d5-43f88a12f05f",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMad29m35YGMfJ4fDjM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "065d4dee-d2bf-473d-915b-4eafd86399c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8sFW7DQvC1Br4qX1edgkJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 745,
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

_source line 4 · 2026-05-10T18:23:56.352Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UzmAMkHuaiuqJhRZqchTLW`</summary>

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
  "parentUuid": "065d4dee-d2bf-473d-915b-4eafd86399c5",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMad29m35YGMfJ4fDjM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5f7fbd4-4e23-41d3-842f-f139afdbd406",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8sFW7DQvC1Br4qX1edgkJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 745
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 745,
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

_source line 5 · 2026-05-10T18:23:56.355Z_

<details><summary>↩ Tool result · `toolu_01UzmAMkHuaiuqJhRZqchTLW`</summary>

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
  "parentUuid": "d5f7fbd4-4e23-41d3-842f-f139afdbd406",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adcd30016e9e7ed6f",
  "type": "user",
  "uuid": "a393aace-a290-40ae-8534-b317a163fcf7",
  "sourceToolAssistantUUID": "d5f7fbd4-4e23-41d3-842f-f139afdbd406",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:23:59.097Z_



Now let me search for the paper and fetch the arXiv page directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a393aace-a290-40ae-8534-b317a163fcf7",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMarK7Epyfgzcc2iBVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5ab2e81-fd62-4a69-9503-97e33d0107f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKog4QZj1N2jN3tLB3YmpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-10T18:23:59.648Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014GnBAk2cJrtVREK9FyX5qw`</summary>

```json
{
  "query": "arXiv 2510.03315"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5ab2e81-fd62-4a69-9503-97e33d0107f1",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMarK7Epyfgzcc2iBVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48f3b493-433d-4ff0-8285-ac78ec8e8d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKog4QZj1N2jN3tLB3YmpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-10T18:24:00.584Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KrpXCRARFMoM7a5HYaq7QK`</summary>

```json
{
  "query": "Gibson decomposing attention context-sensitive neurons 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48f3b493-433d-4ff0-8285-ac78ec8e8d30",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMarK7Epyfgzcc2iBVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6e44aa8-a230-4f48-b9f6-00f290bde400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKog4QZj1N2jN3tLB3YmpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-10T18:24:01.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ByHyQ334MAzRHS7A9Kenpm`</summary>

```json
{
  "query": "decomposing attention structural content-dependent components interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6e44aa8-a230-4f48-b9f6-00f290bde400",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMarK7Epyfgzcc2iBVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecfcce13-3809-4f40-a0ac-375d5fa023c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKog4QZj1N2jN3tLB3YmpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 10 · 2026-05-10T18:24:03.183Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PKCdjfYaHKjPLj27fnNMy3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.03315",
  "prompt": "Extract the full title, all authors, the submission date, the complete abstract, and any information about models used, methodology (especially any decomposition of attention), and whether the paper discusses inference applications or is purely interpretability-focused."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecfcce13-3809-4f40-a0ac-375d5fa023c2",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMarK7Epyfgzcc2iBVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e47e8907-db5e-47e4-a1bc-2c7bc00b01b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKog4QZj1N2jN3tLB3YmpY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

### Tool result

_source line 11 · 2026-05-10T18:24:05.898Z_

<details><summary>↩ Tool result · `toolu_014GnBAk2cJrtVREK9FyX5qw`</summary>

```text
Web search results for query: "arXiv 2510.03315"

Links: [{"title":"[2510.03315] Decomposing Attention To Find Context-Sensitive Neurons","url":"https://arxiv.org/abs/2510.03315"},{"title":"[2511.03315] Heat Kernels and Resummations: the Spinor Case","url":"https://arxiv.org/abs/2511.03315"},{"title":"Decomposing Attention To Find Context-Sensitive Neurons","url":"https://arxiv.org/html/2510.03315"},{"title":"[2605.03315] TACO: Trajectory Aligning Cross-view Optimisation","url":"https://arxiv.org/abs/2605.03315"},{"title":"[2502.03315] HMC and gradient flow with machine-learned classically perfect fixed-point actions","url":"https://arxiv.org/abs/2502.03315"},{"title":"Decomposing Attention To Find Context-Sensitive Neurons Alex Gibson","url":"https://www.arxiv.org/pdf/2510.03315"},{"title":"Machine Learning Oct 2025","url":"https://www.arxiv.org/list/cs.LG/2025-10?skip=3175&show=500"},{"title":"Why LLMs Aren’t Scientists Yet: Lessons from Four Autonomous Research Attempts","url":"https://www.arxiv.org/pdf/2601.03315"},{"title":"[2510.03815v1] A Trustworthy Industrial Fault Diagnosis Architecture Integrating Probabilistic Models and Large Language Models","url":"https://arxiv.org/abs/2510.03815v1"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=36000&show=50"}]

Based on the search results, here's what I found about arXiv paper 2510.03315:

The paper is titled "Decomposing Attention To Find Context-Sensitive Neurons" and was authored by Alex Gibson.

**Summary:**
The paper studies transformer language models, analyzing attention heads whose attention patterns are spread out and whose attention scores depend weakly on content, arguing that the softmax denominators of these heads are stable when the underlying token distribution is fixed. By sampling softmax denominators from a "calibration text", the authors combine the outputs of multiple stable heads in the first layer of GPT2-Small, approximating their combined output by a linear summary of the surrounding text. As an application, they identify first-layer neurons whose activations depend on interpretable properties of the surrounding text.

**Details:**
- The paper is 10 pages with 7 figures and was submitted to the Mechanistic Interpretability Workshop at NeurIPS 2025
- The paper covers topics in Computation and Language (cs.CL), Artificial Intelligence (cs.AI), and Machine Learning (cs.LG)
- The paper was posted on October 1, 2025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48f3b493-433d-4ff0-8285-ac78ec8e8d30",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adcd30016e9e7ed6f",
  "type": "user",
  "uuid": "441af958-e7e2-4991-b642-2dc5b27ba9ee",
  "sourceToolAssistantUUID": "48f3b493-433d-4ff0-8285-ac78ec8e8d30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:24:07.209Z_

<details><summary>↩ Tool result · `toolu_01KrpXCRARFMoM7a5HYaq7QK`</summary>

```text
Web search results for query: "Gibson decomposing attention context-sensitive neurons 2025"

Links: [{"title":"[2510.03315] Decomposing Attention To Find Context-Sensitive Neurons","url":"https://arxiv.org/abs/2510.03315"},{"title":"Decomposing Attention To Find Context-Sensitive Neurons Alex Gibson","url":"https://www.arxiv.org/pdf/2510.03315"},{"title":"Decomposing Attention To Find Context-Sensitive Neurons","url":"https://arxiv.org/html/2510.03315v1"},{"title":"Positional kernels of attention heads","url":"https://www.lesswrong.com/posts/9paB7YhxzsrBoXN8L/positional-kernels-of-attention-heads"},{"title":"Full article: What Should A “Gibsonian Neuroscience” Look Like? Introduction to the Special Issue","url":"https://www.tandfonline.com/doi/full/10.1080/10407413.2019.1615203"},{"title":"Cognitive control articles within Nature Neuroscience","url":"https://www.nature.com/subjects/cognitive-control/neuro"},{"title":"Learning is shaped by abrupt changes in neural engagement","url":"https://pubmed.ncbi.nlm.nih.gov/33782622/"},{"title":"Frontiers | Context-sensitive computational mechanistic explanation in cognitive neuroscience","url":"https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.903960/full"},{"title":"Deciphering neuronal variability across states reveals dynamic sensory encoding - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11839951/"},{"title":"All Posters - CCN 2025 - Cognitive Computational Neuroscience","url":"https://2025.ccneuro.org/poster-sessions/?view=all"}]

Based on the search results, I found relevant information about the paper you're looking for. Here's what I found:

## "Decomposing Attention To Find Context-Sensitive Neurons"

This is a research paper by Alex Gibson from the University of Cambridge, submitted to arXiv on October 1, 2025.

### Main Contributions

The paper makes several key contributions:

1. **Attention Decomposition**: The research studies transformer language models, analyzing attention heads whose attention patterns are spread out and whose attention scores depend weakly on content, arguing that the softmax denominators of these heads are stable when the underlying token distribution is fixed.

2. **The Contextual Circuit**: By sampling softmax denominators from a "calibration text", the authors can combine together the outputs of multiple such stable heads in the first layer of GPT2-Small, approximating their combined output by a linear summary of the surrounding text.

3. **Discovery of Context-Sensitive Neurons**: This approximation enables a procedure where from the weights alone - and a single calibration text - they can uncover hundreds of first layer neurons that respond to high-level contextual properties of the surrounding text, including neurons that didn't activate on the calibration text.

### Example Finding

One discovered neuron distinguishes between Commonwealth and American English.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6e44aa8-a230-4f48-b9f6-00f290bde400",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adcd30016e9e7ed6f",
  "type": "user",
  "uuid": "4e13dc9a-cde6-43d1-a705-72959e696823",
  "sourceToolAssistantUUID": "d6e44aa8-a230-4f48-b9f6-00f290bde400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:24:07.529Z_

<details><summary>↩ Tool result · `toolu_01PKCdjfYaHKjPLj27fnNMy3`</summary>

```text
# Paper Summary

**Full Title:** "Decomposing Attention To Find Context-Sensitive Neurons"

**Author:** Alex Gibson

**Submission Date:** October 1, 2025

**Abstract:**
The research examines transformer language models with a focus on attention heads displaying dispersed attention patterns and weak content-dependent attention scores. The key insight is that "softmax denominators of these heads are stable when the underlying token distribution is fixed." By sampling softmax denominators from calibration text, the authors combine outputs from multiple stable first-layer heads in GPT2-Small. This approach approximates their combined output through linear summarization of surrounding text, enabling discovery of hundreds of first-layer neurons responsive to contextual properties—including neurons absent from the calibration text.

**Model Used:** GPT2-Small

**Methodology:** The paper employs attention decomposition by isolating softmax denominators and using calibration text sampling to approximate combined head outputs. This enables neuron-level analysis without requiring activation data.

**Focus:** Purely interpretability-focused. The work aims to uncover mechanistic understanding of how neurons respond to context, with no explicit discussion of downstream inference applications.

**Venue:** Submitted to the Mechanistic Interpretability Workshop at NeurIPS 2025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e47e8907-db5e-47e4-a1bc-2c7bc00b01b9",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adcd30016e9e7ed6f",
  "type": "user",
  "uuid": "7df432f8-0980-4a58-b6fa-05e4ccdd02bb",
  "sourceToolAssistantUUID": "e47e8907-db5e-47e4-a1bc-2c7bc00b01b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:24:08.940Z_

<details><summary>↩ Tool result · `toolu_01ByHyQ334MAzRHS7A9Kenpm`</summary>

```text
Web search results for query: "decomposing attention structural content-dependent components interpretability"

Links: [{"title":"Decomposing Attention To Find Context-Sensitive Neurons","url":"https://arxiv.org/html/2510.03315v1"},{"title":"Decomposing Attention To Find Context-Sensitive Neurons Alex Gibson","url":"https://www.arxiv.org/pdf/2510.03315"},{"title":"When Attention Collapses: Residual Evidence Modeling for Compositional Inference","url":"https://arxiv.org/html/2605.02323v1"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Towards Monosemanticity: Decomposing Language Models With Dictionary Learning","url":"https://transformer-circuits.pub/2023/monosemantic-features"},{"title":"Attention Meets Post-hoc Interpretability: A Mathematical Perspective","url":"https://arxiv.org/html/2402.03485v1"},{"title":"Sparse Attention Post-Training for Mechanistic Interpretability","url":"https://arxiv.org/html/2512.05865v1"},{"title":"Masked Attention Mechanism","url":"https://www.emergentmind.com/topics/masked-attention-mechanism"},{"title":"Interpretability in Parameter Space: Minimizing Mechanistic Description Length with Attribution-based Parameter Decomposition","url":"https://arxiv.org/html/2501.14926"},{"title":"Decomposing Predictions by Modeling Model Computation – gradient science","url":"https://gradientscience.org/modelcomponents/"}]

Based on the search results, here are the key findings on decomposing attention into structural and content-dependent components for interpretability:

## Main Research Direction

The primary approach is to decompose attention by writing the keys of a head as a sum of positional and content-dependent components. However, LayerNorm complicates such a decomposition because the normalization step mixes position and content together in a nonlinear way.

## Key Findings

A recent study decomposes attention into positional and content-dependent components, revealing how first-layer heads with broad positional kernels create stable linear summaries of the surrounding text. This enables the systematic discovery of context-sensitive neurons without a large text corpus, showing how detailed mathematical analysis can advance mechanistic interpretability.

### Methodology

The approach approximates each head by a positional kernel—its baseline positional preference if tokens were identical—together with token-dependent adjustments. By sampling softmax denominators from a representative "calibration text", researchers can combine several stable heads in GPT-2 Small and construct what is called the contextual circuit: a linear summary of the surrounding text that approximates how these heads collectively influence downstream neurons.

### Applications

As an application of this approximation, researchers identify first-layer neurons whose activations depend on interpretable properties of the surrounding text. For example, one neuron distinguishes between Commonwealth and American English.

This research demonstrates how mathematical decomposition of attention mechanisms can advance understanding of neural network interpretability and help uncover the computational structure underlying language model behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecfcce13-3809-4f40-a0ac-375d5fa023c2",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adcd30016e9e7ed6f",
  "type": "user",
  "uuid": "0518d19b-595f-4260-aff5-f4b73f4b4ae4",
  "sourceToolAssistantUUID": "ecfcce13-3809-4f40-a0ac-375d5fa023c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T18:24:12.290Z_

Now let me fetch the HTML version of the paper to get more detail on the methodology, particularly regarding the "structural vs. content-dependent" decomposition framing and any mention of inference applications.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0518d19b-595f-4260-aff5-f4b73f4b4ae4",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMbmdcCMKowig3c23ZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03121be5-4476-4871-88a6-1599f1c042e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bdwn8achHuoB2WXGSoBrKA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 309,
      "cache_creation_input_tokens": 2630,
      "cache_read_input_tokens": 10878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2630,
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

_source line 16 · 2026-05-10T18:24:16.022Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XKgpG8YjxYuaZccPERw6v4`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.03315v1",
  "prompt": "I need detailed information on the following:\n1. Does the paper explicitly decompose attention into \"structural\" (position-dependent, content-agnostic) and \"content-dependent\" components? What exact terminology does it use?\n2. Is the paper demonstrated only on GPT2-Small, or are other models mentioned?\n3. Does the paper discuss any inference-time applications (e.g., pruning, speedups, efficient inference), or is it purely an interpretability/mechanistic analysis paper?\n4. What is the \"contextual circuit\" the paper defines?\n5. What specific examples of context-sensitive neurons are found?\nPlease extract exact quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03121be5-4476-4871-88a6-1599f1c042e7",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMbmdcCMKowig3c23ZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "defab219-01e7-42ac-a4be-28e311696a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bdwn8achHuoB2WXGSoBrKA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 309,
      "cache_creation_input_tokens": 2630,
      "cache_read_input_tokens": 10878,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2630
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 309,
          "output_tokens": 269,
          "cache_read_input_tokens": 10878,
          "cache_creation_input_tokens": 2630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2630,
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

_source line 17 · 2026-05-10T18:24:23.432Z_

<details><summary>↩ Tool result · `toolu_01XKgpG8YjxYuaZccPERw6v4`</summary>

```text
# Analysis of "Decomposing Attention To Find Context-Sensitive Neurons"

## 1. Attention Decomposition Terminology

Yes, the paper explicitly decomposes attention into position and content components. The exact terminology used:

- **"positional kernel"** - defined as the baseline positional preference
- **"content-dependent"** components - token-dependent adjustments

The paper states: "We approximate each head by a positional kernel—its baseline positional preference if tokens were identical—together with token-dependent adjustments."

The formal decomposition is expressed in Equation 4: attention splits into `pos[n,i,xn] · content[n,xi,xn]` components, where the positional kernel represents intrinsic positional bias.

## 2. Model Coverage

The paper is primarily demonstrated on **GPT2-Small** in the main text. However, Appendix B mentions experiments on multiple models:

- GPT2 (primary focus)
- Pythia
- TinyStories
- DeepSeek-R1 (for classification)

The authors note: "We only thoroughly investigated the contextual circuit of GPT2-Small in the main text."

## 3. Inference-Time Applications

This is **purely an interpretability/mechanistic analysis paper**. There is no discussion of pruning, speedups, or efficient inference. The work focuses on mechanistic understanding of how models represent context.

## 4. The Contextual Circuit Definition

The "contextual circuit" is defined as a linear summary of surrounding text constructed by stable first-layer attention heads. Equation 9 formalizes it as:

"∑[i=1 to n] pos[n,i,xn] · contribution[j[n,xn,xi,[denom]]]"

This approximates how multiple stable heads collectively contribute to downstream neuron activations by combining their OV circuits weighted by positional kernels.

## 5. Context-Sensitive Neuron Examples

Key example provided:

**Neuron 704** - "Commonwealth vs American English": Activates on Commonwealth English tokens like ' colour', ' favour', ' organisation', ' programme' while suppressing American English variants like ' color', ' favor', ' organization', ' program'.

Additional discovered neurons include ones responding to astronomy, religious texts, British English, programming syntax, and biological sciences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "defab219-01e7-42ac-a4be-28e311696a4c",
  "isSidechain": true,
  "promptId": "0c45e361-50c8-48f3-8884-75ae6d3fed4e",
  "agentId": "adcd30016e9e7ed6f",
  "type": "user",
  "uuid": "796bcffe-7fdd-49af-ab4b-e6d032a018cf",
  "sourceToolAssistantUUID": "defab219-01e7-42ac-a4be-28e311696a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T18:24:40.121Z_

Here are my findings on each of the four claims:

---

**1. Does the paper exist at arXiv:2510.03315?**

Yes, confirmed. The paper "Decomposing Attention To Find Context-Sensitive Neurons" by Alex Gibson exists at arXiv:2510.03315. It was submitted on October 1, 2025, and was written for the Mechanistic Interpretability Workshop at NeurIPS 2025.

**2. Does it decompose attention into structural (position-dependent, content-agnostic) and content-dependent components?**

Partially accurate, but the terminology in the claim is slightly off. The paper does decompose attention into two components, but it uses the term **"positional kernel"** (not "structural") for the position-dependent, content-agnostic component. The decomposition splits attention into:
- A **positional kernel** -- the baseline positional preference of each head, representing what the attention pattern would look like if all tokens were identical.
- **Content-dependent** adjustments -- token-dependent modifications on top of the positional baseline.

The paper states: "We approximate each head by a positional kernel -- its baseline positional preference if tokens were identical -- together with token-dependent adjustments." The formal decomposition (Equation 4) factors attention as `pos[n,i,xn] * content[n,xi,xn]`. So the decomposition is real, but calling the positional component "structural" is an imprecise paraphrase rather than the paper's own language.

**3. Was it demonstrated only on GPT2-Small?**

The main text works exclusively on **GPT2-Small**. However, this claim is not fully accurate: Appendix B mentions experiments on additional models including Pythia, TinyStories, and DeepSeek-R1. The authors explicitly note: "We only thoroughly investigated the contextual circuit of GPT2-Small in the main text." So GPT2-Small is the primary focus, but it is not the only model touched.

**4. Is it purely an interpretability paper, or does it suggest inference applications?**

It is **purely an interpretability paper**. There is no discussion of pruning, inference speedups, efficient inference, or any other inference-time application. The paper's goal is mechanistic understanding -- specifically, constructing what it calls a "contextual circuit" (a linear summary of surrounding text from stable first-layer attention heads) and using it to discover "context-sensitive neurons" whose activations depend on interpretable high-level properties of surrounding text. The flagship example is Neuron 704, which distinguishes Commonwealth English from American English.

---

**Summary of claim accuracy:**

| Claim | Verdict |
|---|---|
| Paper exists at arXiv:2510.03315 | TRUE |
| Decomposes attention into structural + content-dependent | MOSTLY TRUE -- the decomposition exists, but the paper says "positional kernel," not "structural" |
| Demonstrated only on GPT2-Small | MOSTLY TRUE -- GPT2-Small is the primary model, but appendices touch Pythia, TinyStories, and DeepSeek-R1 |
| Purely interpretability, no inference applications | TRUE |

Sources:
- [arXiv:2510.03315 Abstract Page](https://arxiv.org/abs/2510.03315)
- [arXiv:2510.03315 HTML Full Text](https://arxiv.org/html/2510.03315v1)
- [arXiv:2510.03315 PDF](https://www.arxiv.org/pdf/2510.03315)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "796bcffe-7fdd-49af-ab4b-e6d032a018cf",
  "isSidechain": true,
  "agentId": "adcd30016e9e7ed6f",
  "requestId": "req_011CauMcqbW3QbYQcd1o6BUJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9accb574-ee74-4ea2-a8ee-878ba5edcbfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0e7cb1f-e90c-4cd8-8c5b-9e19c329880c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvF1Xn3bn43kh9r8nwkqNq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 13508,
      "output_tokens": 839,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1118
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 839,
          "cache_read_input_tokens": 13508,
          "cache_creation_input_tokens": 1118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1118,
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
