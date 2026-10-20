# Research conversation: Search the web for recent papers (2025-2026) on perturbation-based or sensitivity-based hallucination detection in LLMs,

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a472047db0d9b0bf1.jsonl`
- **Structured JSON:** [`f50cf351bf45e4429055.json`](../../sessions/f5/f50cf351bf45e4429055.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-16T09:44:35.072Z_

Search the web for recent papers (2025-2026) on perturbation-based or sensitivity-based hallucination detection in LLMs, particularly methods that measure KL divergence or logit-level sensitivity after perturbing internal representations. Search for:
1. "logit sensitivity hallucination detection 2025 2026"
2. "KL divergence perturbation hallucination LLM 2025"
3. "residual stream perturbation hallucination"
4. "sharpness hallucination detection language model"
5. "Shaking to Reveal" arxiv 2506.02696 (verify this paper exists and what it does)

Also search for "SSP hallucination detection OpenReview" and "next-token gradient sensitivity hallucination". Report all papers found with their key methods and how they relate to measuring distribution sensitivity after perturbation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "74229694-f1aa-4d5e-89fb-3a5e6edbae4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:44:35.077Z_

```json
{
  "parentUuid": "74229694-f1aa-4d5e-89fb-3a5e6edbae4c",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
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
  "uuid": "003e5b58-2a2a-474b-a59d-906247858786",
  "timestamp": "2026-05-16T09:44:35.077Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T09:44:41.708Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JLoD2Wabdehmt9DJ1tgPvN`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "003e5b58-2a2a-474b-a59d-906247858786",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qJxThwpvyPfdo7AcC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e18350ba-63a3-4140-ac02-92976eca41e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DpKPmWbFgYice3z1CRFgt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 751,
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

_source line 4 · 2026-05-16T09:44:41.715Z_

<details><summary>↩ Tool result · `toolu_01JLoD2Wabdehmt9DJ1tgPvN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e18350ba-63a3-4140-ac02-92976eca41e3",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "991258b0-cfc5-40c0-bcf4-6b314c5b2c40",
  "sourceToolAssistantUUID": "e18350ba-63a3-4140-ac02-92976eca41e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T09:44:45.390Z_

Now let me run all the web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "991258b0-cfc5-40c0-bcf4-6b314c5b2c40",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qoMWPGkoA57aKfX8t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6c181da-a35e-4dd4-b877-a6a2895dab81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Shjb8dcdc5KUXNfiZNQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-16T09:44:45.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013v4kuU4AkYDx6ZyYGLvtvG`</summary>

```json
{
  "query": "logit sensitivity hallucination detection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6c181da-a35e-4dd4-b877-a6a2895dab81",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qoMWPGkoA57aKfX8t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fa3f5e3-a6d7-4644-bf78-2cac0abdca3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Shjb8dcdc5KUXNfiZNQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-16T09:44:45.866Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PZTnLvsimA8Fxy6jxGQzaC`</summary>

```json
{
  "query": "KL divergence perturbation hallucination LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fa3f5e3-a6d7-4644-bf78-2cac0abdca3d",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qoMWPGkoA57aKfX8t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "391350a5-d55d-43bf-9a99-851bf21fe14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Shjb8dcdc5KUXNfiZNQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-16T09:44:46.337Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015MK5UuDJFQX8jYYqQfbWva`</summary>

```json
{
  "query": "residual stream perturbation hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "391350a5-d55d-43bf-9a99-851bf21fe14a",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qoMWPGkoA57aKfX8t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de2e902f-f476-41c4-bf98-49a8da60887f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Shjb8dcdc5KUXNfiZNQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 9 · 2026-05-16T09:44:46.810Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PdkYQytqr1EZpfSXHMghSZ`</summary>

```json
{
  "query": "sharpness hallucination detection language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de2e902f-f476-41c4-bf98-49a8da60887f",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qoMWPGkoA57aKfX8t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bf4aea2-051a-48be-bde5-b9961412c86d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Shjb8dcdc5KUXNfiZNQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 10 · 2026-05-16T09:44:46.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018jFtczDPg5gKYSZrLi7LKC`</summary>

```json
{
  "query": "\"Shaking to Reveal\" arxiv 2506.02696"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bf4aea2-051a-48be-bde5-b9961412c86d",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qoMWPGkoA57aKfX8t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "944ca8cf-ca01-4c7b-8532-ec56757352b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Shjb8dcdc5KUXNfiZNQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 11 · 2026-05-16T09:44:47.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01APirmjSTqPmyQv1ENL57sh`</summary>

```json
{
  "query": "SSP hallucination detection OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "944ca8cf-ca01-4c7b-8532-ec56757352b4",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qoMWPGkoA57aKfX8t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1589e5e5-9551-4a90-b963-00562c69af8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Shjb8dcdc5KUXNfiZNQX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 12 · 2026-05-16T09:44:47.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BBrxNuPe6Zx6QPjrMVHGUV`</summary>

```json
{
  "query": "next-token gradient sensitivity hallucination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1589e5e5-9551-4a90-b963-00562c69af8f",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62qoMWPGkoA57aKfX8t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dea10a4e-ef1e-4768-88a5-6652fb7788be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3Shjb8dcdc5KUXNfiZNQX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8974,
      "output_tokens": 347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 347,
          "cache_read_input_tokens": 8974,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 13 · 2026-05-16T09:44:53.052Z_

<details><summary>↩ Tool result · `toolu_01APirmjSTqPmyQv1ENL57sh`</summary>

```text
Web search results for query: "SSP hallucination detection OpenReview"

Links: [{"title":"Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs | OpenReview","url":"https://openreview.net/forum?id=aZdcNDf3pc"},{"title":"SENSITIVITY-GUIDED HALLUCINATION DETECTION IN ...","url":"https://openreview.net/pdf?id=aZdcNDf3pc"},{"title":"Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs | OpenReview","url":"https://openreview.net/forum?id=YQvvJjLWX0"},{"title":"(Im)possibility of Automated Hallucination Detection in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=e5jWdZIX0Q"},{"title":"Awesome-LM-SSP/collection/paper/safety/hallucination.md at main · CryptoAILab/Awesome-LM-SSP","url":"https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/safety/hallucination.md"},{"title":"Efficient Hallucination Detection for LLMs Using Uncertainty-Aware Attention Heads | OpenReview","url":"https://openreview.net/forum?id=FSOoR1ZFtf"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation | OpenReview","url":"https://openreview.net/forum?id=YxJEMTflww"},{"title":"Hallucination Detection in LLMs: Fast and Memory-Efficient Fine-Tuned Models | OpenReview","url":"https://openreview.net/forum?id=8T8QkDsuO9"},{"title":"Revision History for Hallucination Detection in LLMs Using...","url":"https://openreview.net/revisions?id=rFGUrBibMK"}]

Based on the web search results, I found a highly relevant paper on OpenReview about SSP and hallucination detection:

**Sample-Specific Prompting (SSP)** is a theory-informed method for hallucination detection in LLMs that adaptively selects prompts to perturb the model's internal representations, consistently outperforming existing hallucination detection methods.

The approach is based on the finding that the sensitivity of internal representations to prompt-induced perturbations provides a statistically reliable indicator for distinguishing between truthful and hallucinatory samples, with SSP dynamically generating tailored prompts for each question–answer pair to enhance the sensitivity of truthful samples to perturbations while reducing that of hallucinatory ones.

When applied to representative datasets, the probability reaches nearly 99%, suggesting that sensitivity to perturbations provides a discriminative indicator. The method has been validated across diverse datasets including CoQA, TruthfulQA, TriviaQA, and TydiQA-GP, compared with state-of-the-art approaches.

The paper is available on OpenReview at: https://openreview.net/forum?id=aZdcNDf3pc


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1589e5e5-9551-4a90-b963-00562c69af8f",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "88eb89f1-2bc0-4170-a35e-353672e7cef4",
  "sourceToolAssistantUUID": "1589e5e5-9551-4a90-b963-00562c69af8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:44:53.112Z_

<details><summary>↩ Tool result · `toolu_018jFtczDPg5gKYSZrLi7LKC`</summary>

```text
Web search results for query: ""Shaking to Reveal" arxiv 2506.02696"

Links: [{"title":"[2506.02696] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696"},{"title":"[2506.02696v1] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696"},{"title":"arXiv:2506.02696v1 [cs.AI] 3 Jun 2025","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Phase-space measurements and decoherence for angular momentum systems","url":"https://arxiv.org/html/2605.02696"},{"title":"Data-Efficient Challenges in Visual Inductive Priors: A Retrospective","url":"https://arxiv.org/html/2506.08612v1"},{"title":"The structure of tiles in ℤ_𝑝^𝑛×ℤ_𝑞 and ℤ_𝑝^𝑛×ℤ_𝑝","url":"https://arxiv.org/html/2411.02696"},{"title":"qualcomm/Yolo-v7 at main","url":"https://huggingface.co/qualcomm/Yolo-v7/tree/main"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://www.alphaxiv.org/overview/2506.02696v1"},{"title":"arXiv:2402.02696v1 [cs.LG] 5 Feb 2024","url":"https://arxiv.org/pdf/2402.02696"}]

I found the paper you're looking for! Here are the key details:

**Title:** Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations

**Authors:** Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, Ling Chen

**Submission Date:** June 3, 2025

**Summary:**

Hallucination remains a key obstacle to the reliable deployment of large language models (LLMs) in real-world question answering tasks. The paper addresses limitations of traditional self-assessment methods for hallucination detection.

The authors propose Sample-Specific Prompting (SSP), a new framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations. These representations, being less influenced by model bias, offer a more faithful view of the model's latent reasoning process.

Their key insight is that truthful and hallucinated responses exhibit distinct representational shifts under input perturbations, with factual knowledge typically encoded in well-structured internal representations that are tightly coupled with the input and exhibit greater sensitivity in intermediate layers when perturbed, while hallucinated answers remain relatively stable.

You can access the full paper at: https://arxiv.org/abs/2506.02696


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "944ca8cf-ca01-4c7b-8532-ec56757352b4",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "a171bba9-7734-4f3b-8dfa-f65988cf4658",
  "sourceToolAssistantUUID": "944ca8cf-ca01-4c7b-8532-ec56757352b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T09:44:53.167Z_

<details><summary>↩ Tool result · `toolu_01PZTnLvsimA8Fxy6jxGQzaC`</summary>

```text
Web search results for query: "KL divergence perturbation hallucination LLM 2025"

Links: [{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689v4"},{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/html/2407.05474v1"},{"title":"How to evaluate LLM hallucination rates in engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/how-to-evaluate-llm-hallucination-rates-in-engineering/"},{"title":"Mitigating Hallucination of LLMs with Shared-Private ...","url":"https://aclanthology.org/2025.emnlp-main.549.pdf"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Diverging Towards Hallucination: Detection of Failures in Vision-Language Models via Multi-token Aggregation","url":"https://arxiv.org/html/2505.11741v1"},{"title":"ConceptRM: The Quest to Mitigate Alert Fatigue through Consensus-Based Purity-Driven Data Cleaning for Reflection Modelling","url":"https://arxiv.org/html/2602.20166"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"On LLM Knowledge Distillation - A Comparison between Forward KL and Reverse KL | ICLR Blogposts 2025","url":"https://iclr-blogposts.github.io/2025/blog/llm-knowledge-distil/"},{"title":"LLM hallucination rate evaluation for engineering | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/llm-hallucination-rate-evaluation-for-engineering/"}]

Based on the search results, here's an overview of recent research on KL divergence, perturbation, and hallucination in LLMs (2025):

## Key Findings

### Entity Perturbation and Hallucination Detection

Low Entity Perturbation Impact measured by KL divergence strongly indicates fabricated text, as its tokens are weakly tied to key entities. A notable 2025 paper introduces SHINE, a method that builds on the discovery that fabricated text exhibits much lower Entity Perturbation Impact (KL divergence) than aligned or misaligned text, involving four steps: identifying entity, determining perturbation strength, perturbing entity embeddings, and measuring perturbation impact.

### KL Divergence in Knowledge Distillation

Vanilla knowledge distillation using forward KL divergence as the loss function has been shown to introduce issues such as hallucination in language models, which could arise from forward KL's inherent tendency toward mean-seeking optimization, leading to distorted or unrealistic outputs in generative tasks.

### Query Perturbation Approaches

JPMorgan Chase Bank's 2025 patent on hallucination probability prediction involves perturbing an incoming query n times into lexically divergent but semantically equivalent variations, deploying n+1 independent agents to sample outputs for each variant, applying a statistical simulation algorithm, and using the resulting empirical expected hallucination rate to train an encoder classifier that returns a probability-of-hallucination value before the LLM generates any response.

### Attention-Based KL Divergence Methods

Recent methods use a KL-divergence-based attention measure with a lightweight probe, relying on a simple, single-pass uncertainty measure based on the KL divergence between attention matrices and a uniform reference distribution representing maximum uncertainty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "391350a5-d55d-43bf-9a99-851bf21fe14a",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "f73b9cc8-9272-4aea-9a76-26270eca3b06",
  "sourceToolAssistantUUID": "391350a5-d55d-43bf-9a99-851bf21fe14a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:44:53.795Z_

<details><summary>↩ Tool result · `toolu_01BBrxNuPe6Zx6QPjrMVHGUV`</summary>

```text
Web search results for query: "next-token gradient sensitivity hallucination"

Links: [{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"[2601.20279] Hallucination Begins Where Saliency Drops","url":"https://arxiv.org/abs/2601.20279"},{"title":"The Phenomenology of Hallucinations","url":"https://arxiv.org/html/2603.13911"},{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://arxiv.org/html/2504.07863v2"},{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v2"},{"title":"Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/html/2601.09929v1"},{"title":"Hallucination Tokens in AI Models","url":"https://www.emergentmind.com/topics/hallucination-token"},{"title":"Reducing LLM Hallucinations using Epistemic Neural Networks","url":"https://arxiv.org/html/2312.15576v1"}]

Based on the search results, here's what I found about next-token gradient sensitivity and hallucination:

## Overview

Next-token Gradient Sensitivity (NGS) is a statistic that quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility.

## Hallucination Detection Application

Researchers have proposed a gradient-based paradigm for hallucination detection by probing next-token prediction sensitivity, developing NGS-based Hallucination Detection (NGS-HD), which reframes detection as a token-level distribution comparison task.

The norm of NGS bounds the prediction confidence changes under small perturbations.

## Related Work on Gradient Sensitivity

A complementary approach called Embedding-Perturbed Gradient Sensitivity (EPGS) has also been developed for detecting what researchers call "stubborn hallucinations." The hypothesis is that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima supported by brittle memorization, which EPGS detects by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude as an efficient proxy for the Hessian spectrum.

## Research Context

LLMs demonstrate remarkable text generation capabilities but often produce hallucinations—factually inaccurate or unfaithful content—which pose significant deployment risks and remain challenging to detect due to their commonly subtle and localized nature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dea10a4e-ef1e-4768-88a5-6652fb7788be",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "6bd91233-5252-40f8-86cf-28b5507253b1",
  "sourceToolAssistantUUID": "dea10a4e-ef1e-4768-88a5-6652fb7788be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T09:44:54.808Z_

<details><summary>↩ Tool result · `toolu_015MK5UuDJFQX8jYYqQfbWva`</summary>

```text
Web search results for query: "residual stream perturbation hallucination"

Links: [{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400"},{"title":"Residual Decoding: Mitigating Hallucinations in Large Vision-Language Models via History-Aware Residual Guidance","url":"https://arxiv.org/html/2602.01047v3"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"From Noise to Narrative: Tracing the Origins of Hallucinations in Transformers","url":"https://arxiv.org/html/2509.06938v1"},{"title":"CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage in Large Language Models","url":"https://arxiv.org/html/2601.14310"},{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/html/2507.23221v1"},{"title":"Hallucinations in LLMs Are Not a Bug in the Data | Towards Data Science","url":"https://towardsdatascience.com/hallucinations-in-llms-are-not-a-bug-in-the-data/"},{"title":"From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales","url":"https://arxiv.org/html/2604.08591v1"},{"title":"[2602.01047] Residual Decoding: Mitigating Hallucinations in Large Vision-Language Models via History-Aware Residual Guidance","url":"https://arxiv.org/abs/2602.01047"}]

I found several recent research papers on the topic of residual stream perturbation and hallucination. Here are the key findings:

## Main Research Themes

**Hallucination as Attractor Dynamics**: Hallucination operates as a locally stable attractor basin in the residual stream state space, characterized by easy entry and difficult escape. Activation patching reveals that injecting a hallucinated activation into a correct trajectory corrupts output in 87.5% of trials, while the reverse recovers only 33.3%, with window patching showing correction requires sustained multi-step intervention whereas corruption needs only a single perturbation.

**Linear Direction in Residual Stream**: Research has identified that a generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream, isolating a single transferable linear direction separating hallucinated from faithful text. Manipulating this direction causally steers generator hallucination rates.

**Concept Activation in Residual Streams**: Transformer model hallucination is connected to an increase in high level concepts inferred by the transformer, with certain types of inputs increasing the number of concepts imposed on the inputs by the transformer models, and hallucination rates controllable through targeted concept suppression.

**Memory Architecture Perspective**: Research examining memory systems in transformers shows that conflict is basin competition (both PM and WM pulls exist); hallucination is basin absence (the hidden state wanders outside all basins).

**Residual Decoding for Mitigation**: Residual Decoding (ResDec) is an efficient, training-free decoding strategy that uses JSD to analyze logit distributions of historical tokens and merges residual streams into decoded token logits to suppress hallucination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de2e902f-f476-41c4-bf98-49a8da60887f",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "ab7de9a4-32b8-4758-aff2-7eb330dbf7b8",
  "sourceToolAssistantUUID": "de2e902f-f476-41c4-bf98-49a8da60887f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:44:55.456Z_

<details><summary>↩ Tool result · `toolu_013v4kuU4AkYDx6ZyYGLvtvG`</summary>

```text
Web search results for query: "logit sensitivity hallucination detection 2025 2026"

Links: [{"title":"Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding in VLMs - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.488/"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"Token-Level Hallucination Detection","url":"https://www.emergentmind.com/topics/token-level-hallucination-detection"},{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v2"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"LLM Hallucination Statistics 2026: AI Gets Facts Wrong Up to 82% of the Time","url":"https://sqmagazine.co.uk/llm-hallucination-statistics/"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"}]

Based on the search results, I found several relevant papers and resources on hallucination detection methods, including logit-based approaches, from 2025-2026:

## Key Findings on Logit-Based Hallucination Detection

Logit-based methods interpret the output probability distribution as a proxy for model confidence, where lower confidence or higher entropy often correlates with hallucination. A high Shannon entropy across the vocabulary for a given token position indicates that the model is uncertain and distributing probability mass widely, which is a strong signal of potential hallucination.

## Recent Research (2025-2026)

One notable 2025 paper addresses limitations of existing logit-based approaches. Researchers assessed the limitations of the logit lens technique in handling generalized visual hallucinations and introduced ContextualLens, a refined method that leverages contextual token embeddings from middle layers of LMMs.

Another recent study from 2026 explores alternative detection mechanisms. Recent research shows that logit-based methods can be enhanced through frameworks that augment detection capabilities when applied to logits alongside other signals like hidden states and attention patterns.

## Current Challenges

However, Common logit-based methods rely on signals such as log-likelihood, perplexity, maximum token probability, or predictive entropy, assuming that low-probability generations correspond to higher uncertainty, though this assumption does not always hold.

The field is moving toward more sophisticated approaches that combine multiple internal model signals rather than relying solely on logit sensitivity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fa3f5e3-a6d7-4644-bf78-2cac0abdca3d",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "936d3c40-ed9a-48d4-a51f-93e2af7546d2",
  "sourceToolAssistantUUID": "9fa3f5e3-a6d7-4644-bf78-2cac0abdca3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T09:44:55.571Z_

<details><summary>↩ Tool result · `toolu_01PdkYQytqr1EZpfSXHMghSZ`</summary>

```text
Web search results for query: "sharpness hallucination detection language model"

Links: [{"title":"[2403.01548] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://arxiv.org/abs/2403.01548"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation | OpenReview","url":"https://openreview.net/forum?id=s3e8poX3kb"},{"title":"Mitigating Hallucinations in Large Language Models via Self-Refinement-Enhanced Knowledge Retrieval","url":"https://arxiv.org/html/2405.06545v1"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"Lookback Lens: Detecting and Mitigating Contextual Hallucinations in Large Language Models Using Only Attention Maps","url":"https://arxiv.org/html/2407.07071v2"},{"title":"[Quick Review] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://liner.com/review/incontext-sharpness-as-alerts-inner-representation-perspective-for-hallucination-mitigation"},{"title":"Detection of Hallucinations Based on the Internal States of Large Language Models | Automatic Documentation and Mathematical Linguistics | Springer Nature Link","url":"https://link.springer.com/article/10.3103/S0005105525701456"},{"title":"Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation","url":"https://arxiv.org/html/2506.17088v3"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"}]

I've found several relevant research papers and resources on sharpness-based hallucination detection in language models. Here are the key findings:

## In-Context Sharpness Method

A salient pattern has been discovered that correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to incorrect ones. An entropy-based metric has been proposed to quantify the "sharpness" among the in-context hidden states and incorporate it into the decoding process to formulate a constrained decoding approach.

Experiments on various knowledge-seeking and hallucination benchmarks demonstrate this approach's consistent effectiveness, for example, achieving up to an 8.6 point improvement on TruthfulQA.

## Broader Context of Hallucination Detection

The sharpness of context activations within intermediate layers is used to signal hallucinations. In-context Sharpness analyzes features extracted from hidden states across different layers or time steps during decoding.

The research demonstrates that the Truth*Info improvement on TruthfulQA scales with LLM size, showing 3.3 points for the 7B model, 4.8 points for the 13B model, and 8.6 points for the 70B model.

This approach represents an important advance in understanding hallucinations from an inner representation perspective, offering a practical solution for hallucination mitigation during the decoding process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bf4aea2-051a-48be-bde5-b9961412c86d",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "000e7ae3-9819-4792-a846-4df21f15629a",
  "sourceToolAssistantUUID": "0bf4aea2-051a-48be-bde5-b9961412c86d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-16T09:45:00.882Z_

Now let me search for more details on a few of the most relevant papers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "000e7ae3-9819-4792-a846-4df21f15629a",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62rpNJukL6srg7vW5Lr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8209cd9a-d8da-4180-aaec-4654898a3aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjZhLG2nfRGfLXuGLdDw3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2490,
      "cache_creation_input_tokens": 4165,
      "cache_read_input_tokens": 10366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4165,
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

_source line 21 · 2026-05-16T09:45:01.417Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013QD2e9p9BHhjzNQ4q79H3k`</summary>

```json
{
  "query": "arxiv 2506.02696 \"Shaking to Reveal\" SSP method intermediate representations perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8209cd9a-d8da-4180-aaec-4654898a3aa7",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62rpNJukL6srg7vW5Lr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "670abe4d-2bd0-4e25-8f21-9d35d8abae4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjZhLG2nfRGfLXuGLdDw3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2490,
      "cache_creation_input_tokens": 4165,
      "cache_read_input_tokens": 10366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4165,
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

_source line 22 · 2026-05-16T09:45:02.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012A3Btr4cw6yW2KtNW9Q9R8`</summary>

```json
{
  "query": "\"From Flat Facts to Sharp Hallucinations\" arxiv 2605.00939 EPGS gradient sensitivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "670abe4d-2bd0-4e25-8f21-9d35d8abae4f",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62rpNJukL6srg7vW5Lr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d270d91-8c5d-41f2-ba69-67938eb314ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjZhLG2nfRGfLXuGLdDw3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2490,
      "cache_creation_input_tokens": 4165,
      "cache_read_input_tokens": 10366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4165,
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

_source line 23 · 2026-05-16T09:45:02.833Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012pkg7Ww7CXfgSDdcL6qCf4`</summary>

```json
{
  "query": "\"Next-Token Gradient Sensitivity Probing\" NGS hallucination detection OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d270d91-8c5d-41f2-ba69-67938eb314ff",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62rpNJukL6srg7vW5Lr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24a32100-5c69-449c-8879-c4e2ce0d0ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjZhLG2nfRGfLXuGLdDw3N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2490,
      "cache_creation_input_tokens": 4165,
      "cache_read_input_tokens": 10366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4165,
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

_source line 24 · 2026-05-16T09:45:03.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0149u6LGp87tdi7yEHD43e8q`</summary>

```json
{
  "query": "\"SHINE\" entity perturbation KL divergence hallucination detection arxiv 2411.09689"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24a32100-5c69-449c-8879-c4e2ce0d0ea6",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62rpNJukL6srg7vW5Lr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46691c0e-0c6c-4ebf-812f-e7a0b8adedea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjZhLG2nfRGfLXuGLdDw3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2490,
      "cache_creation_input_tokens": 4165,
      "cache_read_input_tokens": 10366,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4165
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2490,
          "output_tokens": 267,
          "cache_read_input_tokens": 10366,
          "cache_creation_input_tokens": 4165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4165,
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

_source line 25 · 2026-05-16T09:45:06.829Z_

<details><summary>↩ Tool result · `toolu_013QD2e9p9BHhjzNQ4q79H3k`</summary>

```text
Web search results for query: "arxiv 2506.02696 "Shaking to Reveal" SSP method intermediate representations perturbation"

Links: [{"title":"[2506.02696] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696"},{"title":"[2506.02696v1] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696v1"},{"title":"arXiv:2506.02696v1 [cs.AI] 3 Jun 2025","url":"https://arxiv.org/pdf/2506.02696"}]

I found the paper! Here's what the search reveals about arxiv 2506.02696:

## "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations"

The paper proposes Sample-Specific Prompting (SSP), a new framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations.

### Key Method Details:

SSP dynamically generates noise prompts for each input and employs a lightweight encoder to amplify the changes in representations caused by the perturbation. A contrastive distance metric is then used to quantify these differences and separate truthful from hallucinated responses.

### Core Insight:

Truthful and hallucinated responses exhibit distinct representational shifts under input perturbations. Factual knowledge is typically encoded in well-structured internal representations, which are tightly coupled with the input and exhibit greater sensitivity in intermediate layers when perturbed, while hallucinated answers remain relatively stable.

### Why Intermediate Representations Matter:

These representations, being less influenced by model bias, offer a more faithful view of the model's latent reasoning process.

The paper was submitted on June 3, 2025, and the authors are from the Australian Artificial Intelligence Institute at UTS and the University of Wisconsin-Madison.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "670abe4d-2bd0-4e25-8f21-9d35d8abae4f",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "7c189dbc-54a6-4395-8d21-14d2ddf6e49c",
  "sourceToolAssistantUUID": "670abe4d-2bd0-4e25-8f21-9d35d8abae4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T09:45:08.522Z_

<details><summary>↩ Tool result · `toolu_012A3Btr4cw6yW2KtNW9Q9R8`</summary>

```text
Web search results for query: ""From Flat Facts to Sharp Hallucinations" arxiv 2605.00939 EPGS gradient sensitivity"

Links: [{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"[2605.01428] Hallucinations Undermine Trust; Metacognition is a Way Forward","url":"https://arxiv.org/abs/2605.01428"},{"title":"[2605.07723v1] LLM hallucinations in the wild: Large-scale evidence from non-existent citations","url":"https://arxiv.org/abs/2605.07723v1"},{"title":"[2605.07723] LLM hallucinations in the wild: Large-scale evidence from non-existent citations","url":"https://arxiv.org/abs/2605.07723"},{"title":"Hallucination, Monofacts, and Miscalibration: An Empirical Investigation","url":"https://arxiv.org/html/2502.08666v1"},{"title":"[2605.13146] On Hallucinations in Inverse Problems: Fundamental Limits and Provable Assessment Methods","url":"https://arxiv.org/abs/2605.13146"},{"title":"From Hallucinations to Facts: Enhancing Language Models with Curated Knowledge Graphs","url":"https://arxiv.org/html/2412.18672v1"},{"title":"Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models","url":"https://arxiv.org/html/2411.14257v1"},{"title":"Last Update: September 29, 2025 Are Hallucinations Bad Estimations? Hude Liu∗1","url":"https://arxiv.org/pdf/2509.21473"}]

Perfect! I found the paper. Here's what the search revealed:

## Paper Overview

The paper "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" (arXiv:2605.00939) addresses how traditional hallucination detection fails on "Stubborn Hallucinations"—errors where LLMs are confidently wrong.

## Core Hypothesis and EPGS Method

The authors hypothesize that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization. 

EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. This acts as an efficient proxy for the Hessian spectrum, differentiating stable knowledge from unstable memorization.

## Key Contributions

The work categorizes hallucinations based on loss landscape geometry, distinguishing between Transient Hallucinations in unstable regions and Stubborn Hallucinations in sharp minima.

## Results

The experiments show that EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d270d91-8c5d-41f2-ba69-67938eb314ff",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "a220ee5c-f541-40a2-8531-6ed48eddad82",
  "sourceToolAssistantUUID": "6d270d91-8c5d-41f2-ba69-67938eb314ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T09:45:09.526Z_

<details><summary>↩ Tool result · `toolu_0149u6LGp87tdi7yEHD43e8q`</summary>

```text
Web search results for query: ""SHINE" entity perturbation KL divergence hallucination detection arxiv 2411.09689"

Links: [{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"[2411.09689] Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/abs/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge — Seongmin Lee","url":"https://seongmin.xyz/papers/llm-hallucination-probing"},{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/html/2407.05474v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Diverging Towards Hallucination: Detection of Failures in Vision-Language Models via Multi-token Aggregation","url":"https://arxiv.org/html/2505.11741v1"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"VL-Uncertainty: Detecting Hallucination in Large Vision-Language Model via Uncertainty Estimation","url":"https://arxiv.org/html/2411.11919v1"},{"title":"(PDF) Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://www.researchgate.net/publication/390772361_Hallucination_Detection_in_LLMs_via_Topological_Divergence_on_Attention_Graphs"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

## SHINE: Hallucination Detection via Entity Perturbation

SHINE is a novel hallucination probing method that does not require external knowledge, supervised training, or LLM fine-tuning, and it's based on the discovery that perturbing key entities in prompts affects LLM's generation of three types of text differently.

**Key aspects of the paper:**

- **Task Definition**: The method classifies LLM-generated text into three categories: aligned, misaligned, and fabricated

- **Performance**: SHINE achieves state-of-the-art performance in hallucination detection, outperforming seven competing methods across four datasets and four LLMs

- **Approach**: The method works by analyzing how entity perturbations affect LLM outputs differently depending on whether the text is truthful or hallucinated, leveraging internal model knowledge rather than external resources.

The paper was authored by Seongmin Lee, Hsiang Hsu, Chun-Fu Chen, and Duen Horng Chau, and is available on arXiv as paper 2411.09689.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46691c0e-0c6c-4ebf-812f-e7a0b8adedea",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "11909a82-21a7-48b3-9075-119a1e0bdaec",
  "sourceToolAssistantUUID": "46691c0e-0c6c-4ebf-812f-e7a0b8adedea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T09:45:14.542Z_

<details><summary>↩ Tool result · `toolu_012pkg7Ww7CXfgSDdcL6qCf4`</summary>

```text
Web search results for query: ""Next-Token Gradient Sensitivity Probing" NGS hallucination detection OpenReview"

Links: [{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"NEXT-TOKEN GRADIENT SENSITIVITY PROBING FOR LLM ...","url":"https://openreview.net/pdf/2a19947788cf8ce29d6d587447ae7eb6c039d117.pdf"},{"title":"Robust and Cheap Hallucination Detection in LLMs","url":"https://openreview.net/pdf?id=Zd0XLr6JKn"},{"title":"Detection and Mitigation of Hallucination in Large ...","url":"https://openreview.net/pdf?id=PTbH6uKwhm"},{"title":"Robust Hallucination Detection in LLMs via Adaptive Token Selection","url":"https://openreview.net/pdf/6e36e6ecbe04ac41b08bdb225a947bda56a47410.pdf"},{"title":"Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/html/2509.09700v1/"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"Published as a conference paper at ICLR 2025 REDEEP: DETECTING HALLUCINATION IN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Beyond Token Probes: Hallucination Detection via Activation Tensors with ACT-ViT | OpenReview","url":"https://openreview.net/forum?id=aJ7AdfOfij"}]

I found the research paper you were searching for! Here are the key findings:

## Next-Token Gradient Sensitivity Probing (NGS) for LLM Hallucination Detection

Large language models often produce hallucinations—factually inaccurate or unfaithful content—which remain challenging to detect due to their subtle and localized nature.

### The NGS Approach

The researchers propose a gradient-based paradigm for hallucination detection by probing next-token prediction sensitivity, introducing a statistic called Next-token Gradient Sensitivity (NGS) that quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility.

The norm of NGS bounds the prediction confidence changes under small perturbations.

### NGS-Based Hallucination Detection (NGS-HD)

Building on NGS, the researchers developed NGS-based Hallucination Detection (NGS-HD), which reframes detection as a token-level distribution comparison task. To overcome computational expense, they directly probe the model's local behaviors through gradients, which offer an exact first-order measure of output sensitivity to embedding perturbations without requiring explicit perturbation samplings.

### Performance Results

On the Qwen-3-8b model, NGS-HD delivered an average of 80.30%, a 6.27% improvement over baseline TSV, with notably strong performance on TruthfulQA at 77.76% and NQ Open at 82.30%.

The paper is available on OpenReview at: https://openreview.net/forum?id=yzWGQNTbHQ


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24a32100-5c69-449c-8879-c4e2ce0d0ea6",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "d62bb627-4fda-4354-b2d2-695236f65d69",
  "sourceToolAssistantUUID": "24a32100-5c69-449c-8879-c4e2ce0d0ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T09:45:18.391Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013UZzURZtXbvcU2i4ja8txG`</summary>

```json
{
  "query": "\"Perturbations Matter Sensitivity-Guided\" hallucination detection OpenReview aZdcNDf3pc"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d62bb627-4fda-4354-b2d2-695236f65d69",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62tDQBBXpiJ89Twtqab",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81642790-d6aa-484a-b072-b6f2fa82ebd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gmhNrPM3WDJwEP9GzSxNy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 5199,
      "cache_read_input_tokens": 14531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5199,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 30 · 2026-05-16T09:45:19.418Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QjAh5xNCw1vcg8U3Hj65N4`</summary>

```json
{
  "query": "\"Hallucination Begins Where Saliency Drops\" arxiv 2601.20279"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81642790-d6aa-484a-b072-b6f2fa82ebd4",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62tDQBBXpiJ89Twtqab",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "741b8df7-319f-4f5e-a1bd-34fb315b610f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gmhNrPM3WDJwEP9GzSxNy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 5199,
      "cache_read_input_tokens": 14531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5199,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 31 · 2026-05-16T09:45:20.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DwvJFXK7ZzHS1qbjVK7MDe`</summary>

```json
{
  "query": "\"In-Context Sharpness as Alerts\" hallucination mitigation ICML 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741b8df7-319f-4f5e-a1bd-34fb315b610f",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62tDQBBXpiJ89Twtqab",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f60d0d4-4e7b-46fa-ae59-75104d1bff61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gmhNrPM3WDJwEP9GzSxNy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 5199,
      "cache_read_input_tokens": 14531,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5199
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 857,
          "output_tokens": 196,
          "cache_read_input_tokens": 14531,
          "cache_creation_input_tokens": 5199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5199,
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

_source line 32 · 2026-05-16T09:45:24.739Z_

<details><summary>↩ Tool result · `toolu_013UZzURZtXbvcU2i4ja8txG`</summary>

```text
Web search results for query: ""Perturbations Matter Sensitivity-Guided" hallucination detection OpenReview aZdcNDf3pc"

Links: [{"title":"Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs | OpenReview","url":"https://openreview.net/forum?id=aZdcNDf3pc"},{"title":"SENSITIVITY-GUIDED HALLUCINATION DETECTION IN ...","url":"https://openreview.net/pdf?id=aZdcNDf3pc"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696"},{"title":"HalluGuard: Demystifying Data-Driven and Reasoning-Driven Hallucinations in LLMs","url":"https://arxiv.org/html/2601.18753v1"},{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic","url":"https://openreview.net/pdf?id=T1kZ0tdOtZM"},{"title":"Mechanistic Detection and Mitigation of Hallucination in Large Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=XU2STJa1Fi"},{"title":"Revision History for Hallucination Detection in LLMs Using...","url":"https://openreview.net/revisions?id=rFGUrBibMK"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v1"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"}]

Based on the search results, I found the paper you're looking for on OpenReview. Here's what I found:

## "Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs"

Hallucination detection is essential for ensuring the reliability of large language models. The paper addresses a key limitation of existing approaches: Internal representation–based methods have emerged as the prevailing direction for detecting hallucinations, yet the internal representations often fail to yield clear separability between truthful and hallucinatory content.

**Core Approach:**
The paper studies the separability of the sensitivity to prompt-induced perturbations in the internal representations. A theory is established to show that, with non-negligible probability, each sample admits a prompt under which factual samples exhibit greater sensitivity to prompt-induced perturbations than hallucinatory samples. When the theory is applied to the representative datasets, the probability reaches nearly 99%, suggesting that sensitivity to perturbations provides a discriminative indicator.

**Proposed Method:**
The paper proposes a novel method Sample-Specific Prompting (SSP), which leverages the sensitivity to prompt-induced perturbations as a discriminative indicator for hallucination detection. The method is tested across diverse datasets CoQA, TruthfulQA, TriviaQA and TydiQA-GP, compared with the state-of-the-art.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81642790-d6aa-484a-b072-b6f2fa82ebd4",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "a7526b95-05c6-42b4-bda6-40826c7e1c75",
  "sourceToolAssistantUUID": "81642790-d6aa-484a-b072-b6f2fa82ebd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T09:45:27.589Z_

<details><summary>↩ Tool result · `toolu_01QjAh5xNCw1vcg8U3Hj65N4`</summary>

```text
Web search results for query: ""Hallucination Begins Where Saliency Drops" arxiv 2601.20279"

Links: [{"title":"[2601.20279] Hallucination Begins Where Saliency Drops","url":"https://arxiv.org/abs/2601.20279"},{"title":"(PDF) Hallucination Begins Where Saliency Drops","url":"https://www.researchgate.net/publication/400178035_Hallucination_Begins_Where_Saliency_Drops"},{"title":"Computer Vision and Pattern Recognition Papers on X: \"Hallucination Begins Where Saliency Drops Xiaofeng Zhang, Yuanchao Zhu, Chaochen Gu, Xiaosong Yuan, Qiyan Zhao, Jiawei Cao, Feilong Tang, Sinan Fan, Yaomin Shen, Chen Shen, Hao Tang https://t.co/jWDrwdHFMe [𝚌𝚜.𝙲𝚅] https://t.co/eVlTkUT8GA\" / X","url":"https://x.com/CSVisionPapers/status/2017001728214778308"},{"title":"幻觉始于显著性下降之处 | alphaXiv","url":"https://www.alphaxiv.org/zh/overview/2601.20279v1"},{"title":"Hallucination Begins Where Saliency Drops | OpenReview","url":"https://openreview.net/forum?id=sjnErRHXf3"},{"title":"HALLUCINATION BEGINS WHERE SALIENCY DROPS","url":"https://openreview.net/pdf/5855c7ef79b8119b12f2a8950ea13499d47669d8.pdf"},{"title":"[Literature Review] Hallucination Begins Where Saliency ...","url":"https://www.themoonlight.io/review/hallucination-begins-where-saliency-drops"},{"title":"attention-mechanisms","url":"https://www.alphaxiv.org/?custom-categories=attention-mechanisms"},{"title":"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2601.02170v1"},{"title":"Towards Understanding Text Hallucination of Diffusion Models via Local Generation Bias","url":"https://arxiv.org/html/2503.03595v1"}]

I found the paper for you. Here's information about "Hallucination Begins Where Saliency Drops" (arxiv 2601.20279):

## Overview

The paper examines attention dynamics in large vision-language models (LVLMs) to detect hallucinations. It was published as a conference paper at ICLR 2026.

## Key Contribution

The authors introduce LVLMs-Saliency, a gradient-aware diagnostic framework that quantifies the visual grounding strength of each output token by fusing attention weights with their input gradients. This addresses a limitation of previous approaches: existing approaches rely solely on forward-pass attention patterns and neglect gradient-based signals that reveal how token influence propagates through the network.

## Main Finding

The analysis uncovers a decisive pattern: hallucinations frequently arise when preceding output tokens exhibit low saliency toward the prediction of the next token, signaling a breakdown in contextual memory retention.

## Proposed Solutions

The paper proposes a dual-mechanism inference-time framework: (1) Saliency-Guided Rejection Sampling (SGRS), which dynamically filters candidate tokens during autoregressive decoding by rejecting those whose saliency falls below a context-adaptive threshold; and (2) Local Coherence Reinforcement (LocoRE), a lightweight, plug-and-play module that strengthens attention from the current token to its most recent predecessors.

## Results

Extensive experiments across multiple LVLMs demonstrate that the method significantly reduces hallucination rates while preserving fluency and task performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "741b8df7-319f-4f5e-a1bd-34fb315b610f",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "708f3c74-bd8b-4e08-b611-cb1f5c7a0040",
  "sourceToolAssistantUUID": "741b8df7-319f-4f5e-a1bd-34fb315b610f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T09:45:28.354Z_

<details><summary>↩ Tool result · `toolu_01DwvJFXK7ZzHS1qbjVK7MDe`</summary>

```text
Web search results for query: ""In-Context Sharpness as Alerts" hallucination mitigation ICML 2024 2025"

Links: [{"title":"GitHub - hkust-nlp/Activation_Decoding: In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation (ICML 2024)","url":"https://github.com/hkust-nlp/Activation_decoding"},{"title":"[Quick Review] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://liner.com/review/incontext-sharpness-as-alerts-inner-representation-perspective-for-hallucination-mitigation"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation | OpenReview","url":"https://openreview.net/forum?id=s3e8poX3kb"},{"title":"ICML Poster In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://icml.cc/virtual/2024/poster/32930"},{"title":"Activation_Decoding/transformers/tests/models/blip/test_modeling_tf_blip.py at main · hkust-nlp/Activation_Decoding","url":"https://github.com/hkust-nlp/Activation_Decoding/blob/main/transformers/tests/models/blip/test_modeling_tf_blip.py"},{"title":"[2403.01548] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://arxiv.org/abs/2403.01548"},{"title":"[PDF] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/In-Context-Sharpness-as-Alerts:-An-Inner-for-Chen-Xiong/ed8f46f493abce9498851e647d900a4628f6ff7f"},{"title":"In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://proceedings.mlr.press/v235/chen24av.html"},{"title":"Mitigating Hallucinations in Large Vision-Language Models with Internal Fact-based Contrastive Decoding","url":"https://arxiv.org/html/2502.01056v1"},{"title":"IN-CONTEXT SHARPNESS AS ALERTS: AN INNER REP","url":"https://openreview.net/pdf?id=24U6vAHnYM"}]

Based on the search results, I found comprehensive information about this paper:

## In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation

This is an ICML 2024 paper that presents a method using in-context sharpness to mitigate LLM hallucinations and improve factuality.

### Key Finding

The paper discovers a pattern associated with hallucinations: correct generations tend to have sharper context activations in the hidden states of the in-context tokens, compared to that of the incorrect generations.

### Methodology

The researchers propose an entropy-based metric to quantify the sharpness among the in-context hidden states and incorporate it into the decoding process, using the entropy value to adjust the next token prediction distribution to improve the factuality and overall quality of the generated text.

### Experimental Results

Experiments on knowledge-seeking datasets (Natural Questions, HotpotQA, TriviaQA) and hallucination benchmark (TruthfulQA) demonstrate consistent effectiveness, with improvements of up to 8.6 absolute points.

### Publication Details

The paper was published in the Proceedings of the 41st International Conference on Machine Learning (ICML), with pages 7553-7567.

The code implementation is available on GitHub at the HKUST-NLP repository, and the paper is also available on arXiv (2403.01548).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f60d0d4-4e7b-46fa-ae59-75104d1bff61",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "323f50e6-5189-460c-9163-3877f3248b70",
  "sourceToolAssistantUUID": "9f60d0d4-4e7b-46fa-ae59-75104d1bff61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T09:45:33.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016ZvgmQJmyUUXxfLiPSP63k`</summary>

```json
{
  "query": "\"Detecting Hallucinations in Large Language Models via Internal Attention Divergence\" arxiv 2605.05025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "323f50e6-5189-460c-9163-3877f3248b70",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62uETChGhoHLD73X6uY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c649bdfc-1c3e-495a-8bf5-a580d86f280d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzudNrmCe8UimkCJuVcZVz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4004,
      "cache_read_input_tokens": 19730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 36 · 2026-05-16T09:45:33.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GMcQZz5P3Lv9oA7qc1314E`</summary>

```json
{
  "query": "CORVUS red-teaming hallucination detectors internal signal camouflage 2601.14310"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c649bdfc-1c3e-495a-8bf5-a580d86f280d",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62uETChGhoHLD73X6uY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12875853-1d26-490e-9286-c15b451b88c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzudNrmCe8UimkCJuVcZVz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4004,
      "cache_read_input_tokens": 19730,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 19730,
          "cache_creation_input_tokens": 4004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4004,
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

_source line 37 · 2026-05-16T09:45:39.207Z_

<details><summary>↩ Tool result · `toolu_016ZvgmQJmyUUXxfLiPSP63k`</summary>

```text
Web search results for query: ""Detecting Hallucinations in Large Language Models via Internal Attention Divergence" arxiv 2605.05025"

Links: [{"title":"[2605.05025] Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/abs/2605.05025"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Detection of Hallucinations Based on the Internal States of Large Language Models | Automatic Documentation and Mathematical Linguistics | Springer Nature Link","url":"https://link.springer.com/article/10.3103/S0005105525701456"},{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v2"},{"title":"What are Models Thinking about? Understanding Large Language Model Hallucinations through Model Internal State Analysis","url":"https://arxiv.org/html/2502.13490v1"},{"title":"Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/html/2601.09929v1"},{"title":"1 A Survey on Hallucination in Large Language Models:","url":"https://arxiv.org/pdf/2311.05232"},{"title":"Hallucinations","url":"https://www.aussieai.com/research/hallucinations"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/html/2509.24770v1"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"}]

Based on the search results, I found the paper you're looking for. Here's information about it:

## Paper Summary

"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals" is authored by Gijs van Dijk.

### Key Contributions

The paper proposes a lightweight and single-pass uncertainty quantification method for detecting hallucinations in Large Language Models that uses attention matrices to estimate uncertainty without requiring repeated sampling or external models.

### Methodology

The method measures the Kullback-Leibler divergence between each attention head's distribution and a uniform reference distribution, and uses these features in a logistic regression probe.

### Results and Findings

Across multiple datasets, task types, and model families, attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods. 

The signal is concentrated in middle layers and on factual tokens such as named entities and numbers, suggesting that attention dynamics provides an efficient and interpretable signal of model uncertainty.

The paper was submitted on May 6, 2026, and you can access it directly at https://arxiv.org/abs/2605.05025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c649bdfc-1c3e-495a-8bf5-a580d86f280d",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "c83e9bec-a0a5-42dd-85be-7cd1f3b2eb3c",
  "sourceToolAssistantUUID": "c649bdfc-1c3e-495a-8bf5-a580d86f280d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T09:45:42.622Z_

<details><summary>↩ Tool result · `toolu_01GMcQZz5P3Lv9oA7qc1314E`</summary>

```text
Web search results for query: "CORVUS red-teaming hallucination detectors internal signal camouflage 2601.14310"

Links: [{"title":"[2601.14310] CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage in Large Language Models","url":"https://arxiv.org/abs/2601.14310"},{"title":"CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage in Large Language Models","url":"https://arxiv.org/html/2601.14310"},{"title":"CORVUS: Red-Teaming Hallucination Detectors via Internal Signal","url":"https://arxiv.org/pdf/2601.14310"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"HALT: Hallucination Assessment via Latent Testing","url":"https://arxiv.org/pdf/2601.14210"},{"title":"CORVUS: Next-Generation Electronic Warfare | L3Harris® Fast. Forward.","url":"https://www.l3harris.com/all-capabilities/corvus-next-generation-electronic-warfare"},{"title":"[2601.16766] Do LLM hallucination detectors suffer from low-resource effect?","url":"https://arxiv.org/abs/2601.16766"},{"title":"Red Teaming Language Model Detectors with Language Models | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00639/119629/Red-Teaming-Language-Model-Detectors-with-Language"},{"title":"Corvus - Insane Cyber","url":"https://insanecyber.com/corvus/"},{"title":"Corvus Signal provides continuous threat analysis, tailored alerts and always-on recommendations - Help Net Security","url":"https://www.helpnetsecurity.com/2023/05/25/corvus-signal/"}]

Based on the search results, here's what I found about CORVUS (arXiv:2601.14310):

## Overview

CORVUS is an efficient red-teaming procedure that learns to camouflage detector-visible telemetry under teacher forcing, including an embedding-space FGSM attention stress test.

## Problem Being Addressed

Single-pass hallucination detectors rely on internal telemetry (e.g., uncertainty, hidden-state geometry, and attention) of large language models, implicitly assuming hallucinations leave separable traces in these signals.

## Methodology

The approach studies a white-box, model-side adversary that fine-tunes lightweight LoRA adapters on the model while keeping the detector fixed. CORVUS is trained only on 1,000 out-of-distribution Alpaca instructions and never uses FAVA-Annotation prompts for training; the same adapters transfer to FAVA without further tuning.

## Results

On FAVA-Annotation across four open-weight LLMs (Llama-2, Vicuna, Llama-3, Qwen2.5), CORVUS degrades all existing detectors calibrated on clean telemetry, including training-free scores (LLM-Check) and trained probes (ICR-probe, SEP).

The paper was published on January 19, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12875853-1d26-490e-9286-c15b451b88c8",
  "isSidechain": true,
  "promptId": "ab5656e8-b9e4-40d4-bf76-8cf45c241dcf",
  "agentId": "a472047db0d9b0bf1",
  "type": "user",
  "uuid": "c1b18062-e3fd-4dc2-9823-37d21363975c",
  "sourceToolAssistantUUID": "12875853-1d26-490e-9286-c15b451b88c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-16T09:46:55.234Z_

Here is a comprehensive report of all papers found relating to perturbation-based and sensitivity-based hallucination detection in LLMs:

---

## Confirmed Papers on Perturbation/Sensitivity-Based Hallucination Detection

### 1. "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations" (arXiv:2506.02696)
- **Authors:** Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, Ling Chen
- **Date:** June 3, 2025
- **Venue:** arXiv (confirmed to exist)
- **Method:** Proposes **Sample-Specific Prompting (SSP)**, a framework that detects hallucinations by analyzing perturbation sensitivity at intermediate representations. SSP dynamically generates noise prompts for each input and employs a lightweight encoder to amplify changes in representations caused by perturbation. A contrastive distance metric quantifies differences between truthful and hallucinated responses.
- **Key Insight:** Factual knowledge is encoded in well-structured internal representations that are tightly coupled with the input and exhibit *greater* sensitivity in intermediate layers when perturbed. Hallucinated answers remain relatively stable under perturbation. Intermediate representations are used because they are less influenced by model bias.
- **Relation to your query:** Directly measures distribution sensitivity after perturbation of internal representations.

### 2. "Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs" (OpenReview: aZdcNDf3pc)
- **Venue:** OpenReview (appears to be the formal venue version of the SSP method)
- **Method:** This is the same SSP framework. Establishes a theory showing that with non-negligible probability (~99% on representative datasets), each sample admits a prompt under which factual samples exhibit greater sensitivity to prompt-induced perturbations than hallucinatory samples. SSP leverages sensitivity to prompt-induced perturbations as a discriminative indicator.
- **Datasets:** CoQA, TruthfulQA, TriviaQA, TydiQA-GP
- **Relation to your query:** Provides theoretical grounding for why perturbation sensitivity discriminates truthful from hallucinated content.

### 3. "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" (arXiv:2605.00939)
- **Date:** May 2025
- **Method:** Proposes **Embedding-Perturbed Gradient Sensitivity (EPGS)**. Categorizes hallucinations based on loss landscape geometry: robust facts reside in *flat* minima, while stubborn hallucinations sit in *sharp* minima supported by brittle memorization. EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude, serving as an efficient proxy for the Hessian spectrum.
- **Key Insight:** Transient hallucinations occur in unstable regions, while "stubborn hallucinations" (high-confidence errors) reside in sharp minima.
- **Results:** Significantly outperforms entropy-based and representation-based baselines.
- **Relation to your query:** Directly uses embedding perturbation and measures gradient sensitivity (related to logit-level sensitivity). The sharpness/flatness framing connects loss landscape geometry to hallucination detection.

### 4. "Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection" (OpenReview: yzWGQNTbHQ)
- **Method:** Introduces **Next-token Gradient Sensitivity (NGS)**, a statistic that quantifies the first-order gradient of the maximum log-probability of the next token with respect to the current token's layer embedding, measuring local prediction fragility. The norm of NGS bounds prediction confidence changes under small perturbations.
- **Detection framework:** **NGS-HD** reframes detection as a token-level distribution comparison task. Directly probes local behaviors through gradients, offering an exact first-order measure of output sensitivity to embedding perturbations *without* requiring explicit perturbation sampling.
- **Results:** On Qwen-3-8b, NGS-HD achieved 80.30% average (6.27% improvement over TSV baseline), with 77.76% on TruthfulQA and 82.30% on NQ Open.
- **Relation to your query:** Measures logit-level sensitivity (gradient of log-probability) with respect to embedding perturbations. The gradient norm bounds KL-divergence-like changes in prediction distribution.

### 5. "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge" / SHINE (arXiv:2411.09689)
- **Authors:** Seongmin Lee, Hsiang Hsu, Chun-Fu Chen, Duen Horng Chau
- **Date:** November 2024 (v4 updated into 2025)
- **Method:** **SHINE** (Sensitivity of Hallucination to Internal kNowledge via Entity perturbation). A four-step process: (1) identify entities in the prompt, (2) determine perturbation strength, (3) perturb entity embeddings, (4) measure **Entity Perturbation Impact via KL divergence** between original and perturbed output distributions. Low KL divergence after entity perturbation strongly indicates fabricated text, since fabricated tokens are weakly tied to key entities.
- **Classification:** Categorizes LLM text as aligned, misaligned, or fabricated.
- **Results:** State-of-the-art across four datasets and four LLMs, outperforming seven competing methods. No external knowledge, supervised training, or fine-tuning required.
- **Relation to your query:** Directly uses KL divergence to measure sensitivity after perturbation of internal representations (entity embeddings).

### 6. "In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation" (arXiv:2403.01548)
- **Venue:** ICML 2024 (Proceedings of the 41st International Conference on Machine Learning, pages 7553-7567)
- **Method:** Discovers that correct generations have *sharper* context activations in hidden states of in-context tokens compared to incorrect ones. Proposes an entropy-based metric to quantify "sharpness" among in-context hidden states and incorporates it into constrained decoding.
- **Results:** Up to 8.6 absolute point improvement on TruthfulQA. Improvement scales with model size (3.3 pts for 7B, 4.8 pts for 13B, 8.6 pts for 70B).
- **Code:** Available at github.com/hkust-nlp/Activation_Decoding
- **Relation to your query:** While not perturbation-based per se, it measures "sharpness" of internal representations as a hallucination signal -- conceptually related to how perturbation methods probe the sharpness/stability of internal states.

### 7. "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals" (arXiv:2605.05025)
- **Author:** Gijs van Dijk
- **Date:** May 6, 2026
- **Method:** Measures **KL divergence between each attention head's distribution and a uniform reference distribution**, using these features in a logistic regression probe. Single-pass, no repeated sampling or external models needed.
- **Key Finding:** Signal is concentrated in middle layers and on factual tokens (named entities, numbers). Attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods.
- **Relation to your query:** Directly uses KL divergence as a measure of internal representation behavior to detect hallucinations.

---

## Additional Related Papers

### 8. "Hallucination Begins Where Saliency Drops" (arXiv:2601.20279)
- **Venue:** ICLR 2026
- **Method:** Introduces **LVLMs-Saliency**, a gradient-aware diagnostic framework for vision-language models. Fuses attention weights with input gradients to quantify visual grounding strength. Proposes Saliency-Guided Rejection Sampling (SGRS) and Local Coherence Reinforcement (LocoRE).
- **Key finding:** Hallucinations arise when preceding output tokens exhibit low saliency toward prediction of the next token (breakdown in contextual memory).
- **Relation:** Uses gradient-based sensitivity analysis of attention as hallucination signal.

### 9. "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation" (arXiv:2604.15400)
- **Date:** April 2026
- **Method:** Uses activation patching to study residual stream dynamics. Finds hallucination operates as a locally stable attractor basin. Injecting a hallucinated activation into a correct trajectory corrupts output 87.5% of the time, while the reverse recovers only 33.3%.
- **Key insight:** Corruption needs only a single perturbation, while correction requires sustained multi-step intervention.
- **Relation:** Demonstrates asymmetric sensitivity to perturbation in the residual stream between truthful and hallucinated states.

### 10. "CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage in Large Language Models" (arXiv:2601.14310)
- **Date:** January 2026
- **Method:** Adversarial attack on perturbation/sensitivity-based detectors. Fine-tunes LoRA adapters to camouflage internal telemetry (uncertainty, hidden-state geometry, attention) while keeping detectors fixed. Includes an embedding-space FGSM attention stress test.
- **Results:** Degrades all existing detectors (LLM-Check, ICR-probe, SEP) across four LLMs on FAVA-Annotation.
- **Relation:** Important adversarial counterpoint showing that perturbation-based detection signals can potentially be camouflaged.

### 11. "A Single Direction of Truth: An Observer Model's Linear Residual Probe Exposes and Steers Contextual Hallucinations" (arXiv:2507.23221)
- **Method:** A generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream, isolating a single transferable linear direction separating hallucinated from faithful text. Manipulating this direction causally steers hallucination rates.
- **Relation:** Identifies a linear perturbation direction in the residual stream that controls hallucination.

---

## Summary of How These Methods Relate to Measuring Distribution Sensitivity After Perturbation

The papers cluster into several approaches:

1. **KL divergence after embedding perturbation** (SHINE): Perturb entity embeddings, measure KL divergence of output distributions. Low KL = fabricated content.

2. **Gradient sensitivity as perturbation proxy** (NGS-HD, EPGS): Instead of explicit perturbation, use gradients to measure how much the output distribution *would* change under small perturbations. NGS measures dlog(p)/d(embedding); EPGS adds Gaussian noise and measures gradient magnitude spikes.

3. **Prompt-induced perturbation of intermediate representations** (SSP / "Shaking to Reveal"): Perturb via dynamically generated prompts, measure representational shift at intermediate layers. Truthful content shows *greater* sensitivity (well-structured, tightly coupled to input).

4. **Attention-based KL divergence** (van Dijk 2026): Measure KL divergence of attention distributions from uniform, use as uncertainty proxy.

5. **Sharpness of internal activations** (In-Context Sharpness): Measure entropy/sharpness of hidden-state activations as proxy for confidence.

6. **Loss landscape geometry** (EPGS / "Flat Facts to Sharp Hallucinations"): Frame hallucination detection as identifying sharp vs. flat minima through perturbation.

The key unifying theme: **truthful and hallucinated outputs have fundamentally different stability properties in representation space**, and perturbation-based methods exploit this by measuring how much internal states or output distributions shift when the model's inputs or internal representations are perturbed.

---

Sources:
- [Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations](https://arxiv.org/abs/2506.02696)
- [Perturbations Matter: Sensitivity-Guided Hallucination Detection in LLMs](https://openreview.net/forum?id=aZdcNDf3pc)
- [From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity](https://arxiv.org/abs/2605.00939)
- [Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection](https://openreview.net/forum?id=yzWGQNTbHQ)
- [Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge (SHINE)](https://arxiv.org/abs/2411.09689)
- [In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation](https://arxiv.org/abs/2403.01548)
- [Detecting Hallucinations in LLMs via Internal Attention Divergence Signals](https://arxiv.org/abs/2605.05025)
- [Hallucination Begins Where Saliency Drops](https://arxiv.org/abs/2601.20279)
- [Hallucination as Trajectory Commitment](https://arxiv.org/abs/2604.15400)
- [CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage](https://arxiv.org/abs/2601.14310)
- [A Single Direction of Truth: Observer Model's Linear Residual Probe](https://arxiv.org/abs/2507.23221)
- [Attractor Geometry of Transformer Memory](https://arxiv.org/abs/2605.05686)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1b18062-e3fd-4dc2-9823-37d21363975c",
  "isSidechain": true,
  "agentId": "a472047db0d9b0bf1",
  "requestId": "req_011Cb62vHUJKGzSLeYb6ZNHM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eaace5f-5f73-4ebd-8dc2-a611ccc0c316",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1c70a808-ac42-40e9-b451-f24d9f6e7546",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017f3eCP3UpMtgxaT5GS5wQM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1757,
      "cache_read_input_tokens": 23734,
      "output_tokens": 3423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3423,
          "cache_read_input_tokens": 23734,
          "cache_creation_input_tokens": 1757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1757,
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
