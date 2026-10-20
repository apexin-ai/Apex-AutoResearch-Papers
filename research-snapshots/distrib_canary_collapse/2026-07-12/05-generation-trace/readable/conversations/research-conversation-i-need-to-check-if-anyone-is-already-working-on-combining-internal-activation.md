# Research conversation: I need to check if anyone is already working on combining internal activation signals with external semantic trajectory 

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a997c333ffc3ee2fb.jsonl`
- **Structured JSON:** [`df438731635969c97aa3.json`](../../sessions/df/df438731635969c97aa3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-15T13:09:06.678Z_

I need to check if anyone is already working on combining internal activation signals with external semantic trajectory tracking for multi-turn jailbreak defense. This is for a research planning task.

Do these web searches and report ALL findings in detail:

1. WebSearch: "multi-turn jailbreak defense activation trajectory 2026"
2. WebSearch: "dual signal jailbreak detection latent activation semantic 2026"
3. WebSearch: "stateful defense multi-turn jailbreak arXiv 2026"
4. WebSearch: "DeepContext multi-turn jailbreak RNN"
5. WebSearch: "latent adversarial detection activation trajectory jailbreak"
6. WebSearch: "multi-turn jailbreak defense fusion internal external signals"

For each search, report:
- The exact papers/works found
- Their venues and dates
- Whether any of them combine BOTH internal model activations AND external semantic tracking for multi-turn jailbreak defense
- Any highly similar concurrent work

Be thorough — this determines whether our research idea is novel or already being done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "41a946cb-f56e-4fe2-a9c8-02bcfc0b47ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T13:09:06.681Z_

```json
{
  "parentUuid": "41a946cb-f56e-4fe2-a9c8-02bcfc0b47ca",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "77a98ae3-8655-49bc-a33b-0822c7f54931",
  "timestamp": "2026-05-15T13:09:06.681Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T13:09:09.523Z_



I'll load the WebSearch tool first, then run all six searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77a98ae3-8655-49bc-a33b-0822c7f54931",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QcyuxAMRxVQN5xFZpe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fb86e2f-5008-47eb-be60-9574f8f9883c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRYgRBfGSHzKscWkVtx42U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8066,
      "cache_read_input_tokens": 0,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8066
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8066,
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

_source line 4 · 2026-05-15T13:09:09.605Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LJfyvABp3CofCfkSq46wU7`</summary>

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
  "parentUuid": "0fb86e2f-5008-47eb-be60-9574f8f9883c",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QcyuxAMRxVQN5xFZpe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a8dfbdd-ab8d-4806-a326-25d74a9a1b8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRYgRBfGSHzKscWkVtx42U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8066,
      "cache_read_input_tokens": 0,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8066
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8066,
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

_source line 5 · 2026-05-15T13:09:09.608Z_

<details><summary>↩ Tool result · `toolu_01LJfyvABp3CofCfkSq46wU7`</summary>

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
  "parentUuid": "1a8dfbdd-ab8d-4806-a326-25d74a9a1b8b",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "d51c5cd1-a116-45f2-8d51-35ca9fff5219",
  "sourceToolAssistantUUID": "1a8dfbdd-ab8d-4806-a326-25d74a9a1b8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T13:09:11.867Z_



Now I'll run all six searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d51c5cd1-a116-45f2-8d51-35ca9fff5219",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QdCWEbS1eSxvTt31fY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdaaa87c-31b4-44cf-8239-15839e3392e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DF1Yo3v5xq8AbXrwoGeQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-15T13:09:12.356Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013LJVzcpntS9699mJ1X4ray`</summary>

```json
{
  "query": "multi-turn jailbreak defense activation trajectory 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdaaa87c-31b4-44cf-8239-15839e3392e1",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QdCWEbS1eSxvTt31fY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6168cdbf-5e03-4888-88a3-8e2f839b6fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DF1Yo3v5xq8AbXrwoGeQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-15T13:09:12.361Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011EqhcoZdRaBA872Cfu3xub`</summary>

```json
{
  "query": "dual signal jailbreak detection latent activation semantic 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6168cdbf-5e03-4888-88a3-8e2f839b6fd0",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QdCWEbS1eSxvTt31fY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa1dee37-5233-43b3-95a0-a29a15fc71f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DF1Yo3v5xq8AbXrwoGeQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 9 · 2026-05-15T13:09:12.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LBWinBdUWYwVqdM1GSUfNH`</summary>

```json
{
  "query": "stateful defense multi-turn jailbreak arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa1dee37-5233-43b3-95a0-a29a15fc71f2",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QdCWEbS1eSxvTt31fY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57da8678-adad-4780-afdc-1fea955ed376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DF1Yo3v5xq8AbXrwoGeQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 10 · 2026-05-15T13:09:13.320Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UnwEjmuknqrK1z6G1L2X4B`</summary>

```json
{
  "query": "DeepContext multi-turn jailbreak RNN"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57da8678-adad-4780-afdc-1fea955ed376",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QdCWEbS1eSxvTt31fY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f253338c-0c4f-4462-9a6c-df49c4d9f773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DF1Yo3v5xq8AbXrwoGeQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 11 · 2026-05-15T13:09:13.774Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011deTD9JoDr1rpaXrX6dk5P`</summary>

```json
{
  "query": "latent adversarial detection activation trajectory jailbreak"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f253338c-0c4f-4462-9a6c-df49c4d9f773",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QdCWEbS1eSxvTt31fY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "019394a7-8d60-408b-b736-0d0258818ca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DF1Yo3v5xq8AbXrwoGeQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 12 · 2026-05-15T13:09:13.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ti7RssCfN5EHh5kAMwnN3v`</summary>

```json
{
  "query": "multi-turn jailbreak defense fusion internal external signals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "019394a7-8d60-408b-b736-0d0258818ca4",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QdCWEbS1eSxvTt31fY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96f50ff6-f98f-4513-8fce-b9faa26e73fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DF1Yo3v5xq8AbXrwoGeQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

### Tool result

_source line 13 · 2026-05-15T13:09:18.337Z_

<details><summary>↩ Tool result · `toolu_011EqhcoZdRaBA872Cfu3xub`</summary>

```text
Web search results for query: "dual signal jailbreak detection latent activation semantic 2026"

Links: [{"title":"Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection","url":"https://arxiv.org/html/2605.02958"},{"title":"SelfGrader: Stable Jailbreak Detection for Large Language Models using Token-Level Logits","url":"https://arxiv.org/html/2604.01473v2"},{"title":"[2602.11495] Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models","url":"https://arxiv.org/abs/2602.11495"},{"title":"HiddenDetect: Detecting Jailbreak Attacks against Large Vision-Language Models via Monitoring Hidden States","url":"https://arxiv.org/html/2502.14744v1"},{"title":"Defending Large Language Models Against Jailbreak ...","url":"https://arxiv.org/pdf/2511.18933"},{"title":"Machine Learning for Detection and Analysis of Novel LLM Jailbreaks.","url":"https://arxiv.org/html/2510.01644v2"},{"title":"Awesome-LM-SSP/collection/paper/safety/jailbreak.md at main · CryptoAILab/Awesome-LM-SSP","url":"https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/safety/jailbreak.md"},{"title":"Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models","url":"https://arxiv.org/html/2602.11495"},{"title":"A Hybrid Perplexity-MAS Framework for Proactive Jailbreak Attack Detection in Large Language Models","url":"https://www.mdpi.com/2076-3417/15/24/13190"},{"title":"Defending Large Language Models Against Jailbreak Exploits with Responsible AI Considerations","url":"https://arxiv.org/html/2511.18933v1"}]

Based on the search results, I found several recent research papers from 2026 related to jailbreak detection using latent signals and semantic analysis. Here are the key findings:

## Recent Research on Jailbreak Detection (2026)

Recent work identifies that refusal signals are driven by sparse distributions of anchors in the upstream latent space, and introduces SALO, a lightweight, inference-only defense framework that effectively detects sophisticated jailbreaks like GCG and AutoDAN with minimal computational overhead.

Another study examines jailbreaking from security and interpretability perspectives by analyzing how internal representations differ between jailbreak and benign prompts through systematic layer-wise analysis across multiple open-source models including GPT-J, LLaMA, Mistral, and Mamba.

Current approaches to detecting adversarial prompts before model decoding use statistical anomalies like language model perplexity and semantic similarity measures such as cosine similarity on embedding vectors, with these complementary techniques enabling efficient flagging of suspicious inputs by identifying both token-level irregularities and semantic proximity to known jailbreak categories.

Research shows that safety behaviors are encoded as latent neural features, where specific neurons and layer activations show high similarity to vectors associated with refusal-related vocabulary, revealing internal alignment mechanisms that operate even when surface-level filters fail.

These approaches represent advances in using latent activations and semantic signals to develop more robust jailbreak detection mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa1dee37-5233-43b3-95a0-a29a15fc71f2",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "a9de0102-0a09-443a-8366-e639b739310e",
  "sourceToolAssistantUUID": "fa1dee37-5233-43b3-95a0-a29a15fc71f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:09:20.132Z_

<details><summary>↩ Tool result · `toolu_013LJVzcpntS9699mJ1X4ray`</summary>

```text
Web search results for query: "multi-turn jailbreak defense activation trajectory 2026"

Links: [{"title":"Multi-turn Jailbreak Attacks: Strategies & Defenses","url":"https://www.emergentmind.com/topics/multi-turn-jailbreak-attacks"},{"title":"Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/html/2604.28129"},{"title":"Multi-Turn Jailbreak Attacks","url":"https://www.emergentmind.com/topics/multi-turn-jailbreak-attacks-337422f8-3cf7-4b39-a07f-2a4462efe74a"},{"title":"TROJail: Trajectory-Level Optimization for Multi-Turn Large Language Model Jailbreaks with Process Rewards","url":"https://arxiv.org/html/2512.07761"},{"title":"AI Jailbreak Prompts: How They Work, Why They Work, and How to Stop Them | Repello AI","url":"https://repello.ai/blog/understanding-ai-jailbreaking-techniques-and-safeguards-against-prompt-exploits"},{"title":"Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses","url":"https://arxiv.org/html/2605.03095"},{"title":"Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models","url":"https://arxiv.org/pdf/2601.05445"},{"title":"GitHub - AIM-Intelligence/Automated-Multi-Turn-Jailbreaks · GitHub","url":"https://github.com/AIM-Intelligence/Automated-Multi-Turn-Jailbreaks"},{"title":"LLM Jailbreaks 2024–2026: Techniques, Risks & Defense Strategies","url":"https://startup-house.com/blog/llm-jailbreak-techniques"},{"title":"AI Jailbreak Techniques in 2026: Current State - 15 Research Lab | 15 Research Lab","url":"https://www.15researchlab.com/blog/ai-jailbreak-techniques-2026/"}]

Based on the search results, here's what I found about multi-turn jailbreak defense activation trajectory in 2026:

## Multi-Turn Jailbreak Attacks and Defense

Robust LLM safety alignment will require advances in pattern-aware training, self-reflexive moderation, graph-based input fusion, and automated context semantics analysis across dialogue trajectories.

### Defense Activation Mechanisms

Recent research in early 2026 has focused on detecting attack signatures during multi-turn interactions. Multi-turn attacks leave a consistent signature—adversarial restlessness—in the model's residual stream: each phase shift moves the activation, producing elevated cumulative path length. Five scalar trajectory features capturing this signal lift detection from 76.2% to 93.8% on synthetic data.

### Current Attack Landscape

ICON formalizes Intent-Context Coupling, establishing that each malicious intent category has an optimal context pattern that maximally reduces the safety filter's activation, and exploits this via intent-driven routing and hierarchical optimization.

Context-agnostic architectures like Gemini 2.5 Flash demonstrate near-immunity by stripping conversational context and evaluating the final prompt in isolation.

### Defense Strategies

Multi-layer designs combining token-level, prompt-level, and dialogue-based defenses offer the most comprehensive protection, and using separate moderation models or embedding-based classifiers enables cost-effective detection at scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6168cdbf-5e03-4888-88a3-8e2f839b6fd0",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "4e5d7317-7938-4100-9b94-f310b19cf6e0",
  "sourceToolAssistantUUID": "6168cdbf-5e03-4888-88a3-8e2f839b6fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T13:09:20.230Z_

<details><summary>↩ Tool result · `toolu_01LBWinBdUWYwVqdM1GSUfNH`</summary>

```text
Web search results for query: "stateful defense multi-turn jailbreak arXiv 2026"

Links: [{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/html/2602.16935v1"},{"title":"Multi-Turn Jailbreaks Are Simpler Than They Seem","url":"https://arxiv.org/html/2508.07646v1"},{"title":"Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models","url":"https://arxiv.org/html/2601.05445"},{"title":"Recursive Language Models for Jailbreak Detection: A Procedural Defense for Tool-Augmented Agents","url":"https://arxiv.org/html/2602.16520v1"},{"title":"Multi-turn Jailbreaking via Global Refinement and Active Fabrication [WARNING] This paper contains unsafe model responses. Reader discretion is advised.","url":"https://arxiv.org/html/2506.17881v1"},{"title":"AJAR: Adaptive Jailbreak Architecture for Red-teaming","url":"https://arxiv.org/html/2601.10971v1"},{"title":"Multi-turn Jailbreaking Attack in Multi-Modal Large Language Models.","url":"https://arxiv.org/html/2601.05339"},{"title":"LLM Jailbreaking in 2026: 97% Success Rates, Autonomous Attacks, and the Arms Race That Isn't Working | redteams.ai","url":"https://redteams.ai/blog/llm-jailbreaking-2026"},{"title":"Defending Large Language Models Against Jailbreak Exploits with Responsible AI Considerations","url":"https://arxiv.org/html/2511.18933v1"},{"title":"M2S: Multi-turn to Single-turn jailbreak in Red Teaming for LLMs","url":"https://arxiv.org/html/2503.04856v3"}]

Based on the search results, I found several highly relevant papers from 2026 on stateful defenses against multi-turn jailbreaks:

## Key Research on Stateful Defense Against Multi-Turn Jailbreaks (2026)

### DeepContext: Stateful Real-Time Detection

DeepContext achieves a 0.84 F1-score against multi-turn jailbreaks while maintaining sub-20ms latency on a T4 GPU. The paradigm has moved from single-turn, optimization-based injections to complex, stateful, and agentic strategies that exploit the model's reasoning capabilities and context window.

DeepContext utilizes an RNN architecture that ingests a sequence of task-attention weighted embeddings, formulating user intent as a state space problem to leverage RNNs to model intent trajectories and detect multi-turn jailbreaks.

### Other Notable Defense Approaches

**Recursive Language Models (RLM-JB)**: RLM-JB treats jailbreak detection as a procedure rather than a one-shot classification, with RLM-JB achieving F1 up to 98.49% in AutoDAN settings.

**Multi-modal Defenses**: FragGuard is a novel fragment-optimized and multi-LLM defense mechanism to effectively mitigate jailbreaking attacks in MLLMs.

These papers represent recent advances in moving from stateless to stateful defense mechanisms that can track adversarial intent evolution across conversation turns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57da8678-adad-4780-afdc-1fea955ed376",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "b6e1f9f0-e99a-41cf-b4a0-b5102eaed41e",
  "sourceToolAssistantUUID": "57da8678-adad-4780-afdc-1fea955ed376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:09:21.661Z_

<details><summary>↩ Tool result · `toolu_01UnwEjmuknqrK1z6G1L2X4B`</summary>

```text
Web search results for query: "DeepContext multi-turn jailbreak RNN"

Links: [{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/html/2602.16935v1"},{"title":"DeepContext: Stateful Real-Time Detection of Multi-Turn ...","url":"https://www.arxiv.org/pdf/2602.16935"},{"title":"[2602.16935] DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/abs/2602.16935"},{"title":"[2602.16935v1] DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs","url":"https://arxiv.org/abs/2602.16935v1"},{"title":"DeepContext: Defending Against Multi-Turn LLM Attacks with Context-Aware Guardrails","url":"https://highflame.com/blogs/deepcontext-defending-against-multi-turn-llm-attacks-with-context-aware-guardrails"},{"title":"Multi-Turn Context Jailbreak Attack on Large Language Models From First Principles WARNING: This paper contains context which is toxic in nature.","url":"https://arxiv.org/html/2408.04686v1"},{"title":"[2408.04686] Multi-Turn Context Jailbreak Attack on Large Language Models From First Principles","url":"https://arxiv.org/abs/2408.04686"},{"title":"[Literature Review] Multi-Turn Context Jailbreak Attack on Large Language Models From First Principles","url":"https://www.themoonlight.io/en/review/multi-turn-context-jailbreak-attack-on-large-language-models-from-first-principles"},{"title":"Crescendo","url":"https://crescendo-the-multiturn-jailbreak.github.io//"},{"title":"Multi-Turn Jailbreaks Are Simpler Than They Seem","url":"https://arxiv.org/html/2508.07646v1"}]

Based on the search results, here's what I found about DeepContext and multi-turn jailbreak detection using RNNs:

## DeepContext Overview

DeepContext is a stateful monitoring framework designed to map the temporal trajectory of user intent. DeepContext discards the isolated evaluation model in favor of a Recurrent Neural Network (RNN) architecture that ingests a sequence of fine-tuned turn-level embeddings.

## How It Works

Unlike stateless models, the RNN maintains a persistent hidden state that evolves with the conversation. This state acts as a "contextual memory," allowing the system to synthesize the relationship between previous queries and the current input. By monitoring the hidden state's transition across turns, DeepContext identifies "intent drift"; the subtle, incremental shift from legitimate inquiry to adversarial steering.

## Performance

DeepContext achieves a 0.84 F1-score against multi-turn jailbreaks while maintaining sub-20ms latency on a T4 GPU.

## Key Problem It Addresses

The evolution of adversarial attacks from single-shot jailbreaks to multi-turn agentic strategies has created a "Safety Gap" that stateless guardrails cannot close. Existing defenses, relying on massive parameter counts and static context windows, fail to capture the temporal nuances of intent grooming. Attacks such as Crescendo and ActorAttack exploit the auto-regressive nature of LLMs by distributing malicious intent across a sequence of seemingly benign queries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f253338c-0c4f-4462-9a6c-df49c4d9f773",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "dd761724-9363-4d3b-b91f-cbacdd14151d",
  "sourceToolAssistantUUID": "f253338c-0c4f-4462-9a6c-df49c4d9f773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T13:09:21.976Z_

<details><summary>↩ Tool result · `toolu_011deTD9JoDr1rpaXrX6dk5P`</summary>

```text
Web search results for query: "latent adversarial detection activation trajectory jailbreak"

Links: [{"title":"Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection","url":"https://arxiv.org/html/2605.02958"},{"title":"[2605.02958] Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection","url":"https://arxiv.org/abs/2605.02958"},{"title":"Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/html/2604.28129"},{"title":"Adversarial Jailbreak Strategies","url":"https://www.emergentmind.com/topics/adversarial-jailbreak-strategies"},{"title":"Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models","url":"https://arxiv.org/html/2602.11495"},{"title":"Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation","url":"https://arxiv.org/html/2604.07835v1"},{"title":"HiddenDetect: Detecting Jailbreak Attacks against Large Vision-Language Models via Monitoring Hidden States","url":"https://arxiv.org/html/2502.14744v1"},{"title":"N-GLARE: An Non-Generative Latent Representation-Efficient LLM Safety Evaluator","url":"https://arxiv.org/html/2511.14195v1"},{"title":"(PDF) LatentBreak: Jailbreaking Large Language Models through Latent Space Feedback","url":"https://www.researchgate.net/publication/396458061_LatentBreak_Jailbreaking_Large_Language_Models_through_Latent_Space_Feedback"},{"title":"Adversarial Jailbreak Attacks","url":"https://www.emergentmind.com/topics/adversarial-jailbreak-attacks"}]

Based on the search results, here's what I found on latent adversarial detection, activation trajectories, and jailbreaking:

## Key Findings

**Latent Adversarial Detection (LAD):**
LAD proposes probing the target LLM's internal activations to detect adversarial intent in how the model understands inputs. LAD detects activation drift in what the model understood, enabling detection of attacks where surface text appears benign but internal representations shift.

**Activation Trajectories:**
Refusal is a dynamic and sparse process rather than a localized outcome, and using Causal Tracing, researchers uncovered the Refusal Trajectory—a persistent upstream signature that remains intact even when adversarial attacks (e.g., GCG) suppress terminal signals.

**SALO Defense:**
SALO (Sparse Activation Localization Operator) is an inference-time detector designed to capture these latent patterns, effectively recovering defense capabilities against forced-decoding attacks, improving detection rates from ~0% to >90%.

**Jailbreak Mechanisms:**
Jailbreaks suppress the expression of refusal (at the tail) without eliminating the intent of refusal (in the trajectory). Latent-space attacks directly edit representations in the model's hidden state to cross safety boundaries defined in latent embedding space.

**Multi-Turn Attacks:**
Multi-turn jailbreaks use the model's own conversational capabilities to steer it toward harmful compliance, and trajectory analysis detects this steering in the model's activations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "019394a7-8d60-408b-b736-0d0258818ca4",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "4f8d86b0-aa06-4b6e-97e3-785d3e89b1d7",
  "sourceToolAssistantUUID": "019394a7-8d60-408b-b736-0d0258818ca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:09:22.419Z_

<details><summary>↩ Tool result · `toolu_01Ti7RssCfN5EHh5kAMwnN3v`</summary>

```text
Web search results for query: "multi-turn jailbreak defense fusion internal external signals"

Links: [{"title":"Proactive Defense Against LLM Jailbreak","url":"https://arxiv.org/html/2510.05052v2"},{"title":"Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction","url":"https://unit42.paloaltonetworks.com/jailbreak-llms-through-camouflage-distraction/"},{"title":"Multi-turn Jailbreak Attacks: Strategies & Defenses","url":"https://www.emergentmind.com/topics/multi-turn-jailbreak-attacks"},{"title":"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense","url":"https://arxiv.org/html/2604.07727"},{"title":"Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models","url":"https://arxiv.org/html/2602.11495v1"},{"title":"Multi-Turn Jailbreak Attacks","url":"https://www.emergentmind.com/topics/multi-turn-jailbreak-attacks-337422f8-3cf7-4b39-a07f-2a4462efe74a"},{"title":"Latent Fusion Jailbreak: Blending Harmful and Harmless Representations to Elicit Unsafe LLM Outputs","url":"https://arxiv.org/html/2508.10029v1"},{"title":"DataGen‑Judge Cascade (DJC) Multi‑Turn Indirect Jailbreak Attack | by Abiola Olaleye | Jul, 2025 | Medium","url":"https://medium.com/@abiola_/datagen-judge-cascade-djc-multi-turn-indirect-jailbreak-attack-547f501e49ca"},{"title":"M2S: Multi-turn to Single-turn jailbreak in Red Teaming for LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.805/"},{"title":"The Crescendo Multi-Turn LLM Jailbreak Attack","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-805-russinovich.pdf"}]

Based on the search results, here's what I found about multi-turn jailbreak defense with fusion of internal and external signals:

## Overview

Multi-turn jailbreak attacks are adversarial tactics designed to defeat the safety alignment of LLMs by distributing a harmful objective across multiple conversational exchanges, with the attacker incrementally establishing context, semantic drift, or misdirection to progressively steer the model toward generating policy-violating content.

## Defense Approaches Using Fused Signals

Several recent defense mechanisms combine internal and external signals:

**ProAct Framework**: ProAct is a proactive defense framework designed to disrupt and mislead iterative search jailbreak methods by intentionally misleading them into thinking the model has been jailbroken with "spurious responses," which provide false signals to the attacker's internal optimization loop. ProAct can use signals from additional defensive layers to trigger spurious response creation and is fully compatible with existing defense mechanisms.

**TrajGuard**: Hidden states in critical layers during the decoding phase carry stronger and more stable risk signals than input jailbreak prompts, with hidden representations of tokens generated during jailbreak attempts progressively approaching high-risk regions in the latent space.

**Internal Representation-Based Detection**: Existing defenses largely treat jailbreak detection as a black-box problem relying on external signals from prompts or outputs, whereas fewer works explore the internal representations of LLMs as a basis for defense, motivating approaches that leverage latent-space and layer-wise signals.

## Key Challenge

Current defenses often generalize poorly, with block rates differing substantially between single and multi-turn forms of equivalent content, while some defensive architectures exhibit 30-point increases in attack success rates when multi-turn context is exploited.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96f50ff6-f98f-4513-8fce-b9faa26e73fb",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "d1427335-6a11-40cf-b45c-322e186719fb",
  "sourceToolAssistantUUID": "96f50ff6-f98f-4513-8fce-b9faa26e73fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T13:09:25.546Z_

Let me do a few follow-up searches to get more details on the most relevant papers that surfaced, particularly LAD, TrajGuard, and the refusal trajectory paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1427335-6a11-40cf-b45c-322e186719fb",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4Qe9EKFmJTnT7NkLx2U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f3e33cf-8f18-47c6-a371-96bd6dea179d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AK3HDpBPtttmgYyyVifppp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5823,
      "cache_read_input_tokens": 9475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5823,
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

_source line 20 · 2026-05-15T13:09:26.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TdnfTXvxKpXKMWhUCNqjG3`</summary>

```json
{
  "query": "TrajGuard streaming hidden-state trajectory jailbreak defense arXiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f3e33cf-8f18-47c6-a371-96bd6dea179d",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4Qe9EKFmJTnT7NkLx2U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0c7f0bf-1fac-4098-afa8-66013861496f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AK3HDpBPtttmgYyyVifppp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5823,
      "cache_read_input_tokens": 9475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5823,
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

_source line 21 · 2026-05-15T13:09:26.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q9jU9nD9A7gFvkucT891Qj`</summary>

```json
{
  "query": "Latent Adversarial Detection adaptive probing LLM activations multi-turn arXiv 2604.28129"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c7f0bf-1fac-4098-afa8-66013861496f",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4Qe9EKFmJTnT7NkLx2U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49dec885-ab4d-43ae-8d2f-670388391ba5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AK3HDpBPtttmgYyyVifppp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5823,
      "cache_read_input_tokens": 9475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5823,
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

_source line 22 · 2026-05-15T13:09:27.495Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E4Vo4JJiWAjUVjbfG7LXFv`</summary>

```json
{
  "query": "\"Jailbreaking Leaves a Trace\" internal representations arXiv 2602.11495"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49dec885-ab4d-43ae-8d2f-670388391ba5",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4Qe9EKFmJTnT7NkLx2U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6c84068-093d-4c43-9171-a140cf5caee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AK3HDpBPtttmgYyyVifppp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5823,
      "cache_read_input_tokens": 9475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5823,
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

_source line 23 · 2026-05-15T13:09:27.931Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KFCVdsPG6Fr1aMJzuirPcn`</summary>

```json
{
  "query": "JBShield representation-level jailbreak defense arXiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6c84068-093d-4c43-9171-a140cf5caee4",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4Qe9EKFmJTnT7NkLx2U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dc91dc8-f13f-48bb-870d-af02c43b4d0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AK3HDpBPtttmgYyyVifppp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5823,
      "cache_read_input_tokens": 9475,
      "output_tokens": 279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5823
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 279,
          "cache_read_input_tokens": 9475,
          "cache_creation_input_tokens": 5823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5823,
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

_source line 24 · 2026-05-15T13:09:32.983Z_

<details><summary>↩ Tool result · `toolu_01TdnfTXvxKpXKMWhUCNqjG3`</summary>

```text
Web search results for query: "TrajGuard streaming hidden-state trajectory jailbreak defense arXiv 2604"

Links: [{"title":"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense","url":"https://arxiv.org/html/2604.07727"},{"title":"[2604.07727] TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense","url":"https://arxiv.org/abs/2604.07727"},{"title":"TrajGuard: デコード時ジェイルブレイク対策向けストリーミング隠れ状態軌跡検知 | alphaXiv","url":"https://www.alphaxiv.org/ja/overview/2604.07727v1"},{"title":"TraceGuard: Structured Multi-Dimensional Monitoring as a Collusion-Resistant Control Protocol","url":"https://arxiv.org/html/2604.03968"},{"title":"TraceGuard: Structured Multi-Dimensional Monitoring as a ...","url":"https://arxiv.org/pdf/2604.03968"},{"title":"SafeMobile: Chain-level Jailbreak Detection and Automated Evaluation for Multimodal Mobile Agents","url":"https://arxiv.org/html/2507.00841"},{"title":"HSF: Defending against Jailbreak Attacks with Hidden State Filtering","url":"https://arxiv.org/html/2409.03788"},{"title":"Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation","url":"https://arxiv.org/html/2604.07835v1"},{"title":"Rethinking Jailbreak Detection of Large Vision Language Models with Representational Contrastive Scoring","url":"https://arxiv.org/html/2512.12069v1"},{"title":"[2409.03788] HSF: Defending against Jailbreak Attacks with Hidden State Filtering","url":"https://arxiv.org/abs/2409.03788"}]

I found the paper you were looking for. Here's information about TrajGuard:

## TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense

TrajGuard is a training-free, decoding-time defense framework that addresses jailbreak attacks on large language models by monitoring internal model representations during generation.

**Key Innovation:**
Hidden states in critical layers during the decoding phase carry stronger and more stable risk signals than input jailbreak prompts. The hidden representations of tokens generated during jailbreak attempts progressively approach high-risk regions in the latent space.

**Architecture:**
TrajGuard consists of two core modules: the Streaming Geometric Surveillance (SGS) continuously monitors hidden states in critical layers to track whether the current decoding path deviates from typical benign behavior, and the Prompt–Answer Inference Referee (PAIR-Judge), which reviews decoded tokens from a semantic perspective when SGS detects an anomaly.

**Performance:**
Across 12 jailbreak attacks and various open-source LLMs, TrajGuard achieves an average defense rate of 95% with detection latency of 5.2 ms/token while maintaining a false positive rate below 1.5%.

The paper was published on arXiv as #2604.07727 on April 9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0c7f0bf-1fac-4098-afa8-66013861496f",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "2da7a59a-45c7-4306-8c9a-f242e3435e7f",
  "sourceToolAssistantUUID": "c0c7f0bf-1fac-4098-afa8-66013861496f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T13:09:35.218Z_

<details><summary>↩ Tool result · `toolu_01Q9jU9nD9A7gFvkucT891Qj`</summary>

```text
Web search results for query: "Latent Adversarial Detection adaptive probing LLM activations multi-turn arXiv 2604.28129"

Links: [{"title":"[2604.28129] Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/abs/2604.28129"},{"title":"Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/html/2604.28129"},{"title":"[2503.09066] Probing Latent Subspaces in LLM for AI Security: Identifying and Manipulating Adversarial States","url":"https://arxiv.org/abs/2503.09066"},{"title":"Probing Latent Subspaces in LLM for AI Security: Identifying and Manipulating Adversarial States","url":"https://arxiv.org/html/2503.09066v1"},{"title":"Segment-Level Coherence for Robust Harmful Intent Probing in LLMs","url":"https://arxiv.org/html/2604.14865v1"},{"title":"SALLIE: Safeguarding Against Latent Language & Image Exploits","url":"https://arxiv.org/html/2604.06247"},{"title":"Obfuscated Activations Bypass LLM Latent-Space Defenses","url":"https://arxiv.org/html/2412.09565"},{"title":"Probing the Robustness of Large Language Models Safety to Latent Perturbations","url":"https://arxiv.org/html/2506.16078v1"},{"title":"[2503.09066v1] Probing Latent Subspaces in LLM for AI Security: Identifying and Manipulating Adversarial States","url":"https://arxiv.org/abs/2503.09066v1"},{"title":"Probing Latent Subspaces of LLMs for AI Security: Identifying and Manipulating Adversarial States","url":"https://arxiv.org/html/2503.09066v2"}]

I found the paper you're looking for! Here's information about it:

**Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection**

The paper is authored by Prashant Kulkarni and was submitted on April 30, 2026.

**Overview:**
Multi-turn prompt injection attacks follow a known attack path of trust-building, pivoting, and escalation, where text-level defenses miss covert attacks where individual turns appear benign. The research shows this attack path leaves an activation-level signature in the model's residual stream, with each phase shift moving the activation and producing a total path length far exceeding benign conversations.

**Key Findings:**
- The phenomenon is called "adversarial restlessness," and five scalar trajectory features capturing this signal lift conversation-level detection from 76.2% to 93.8% on synthetic held-out data.
- The signal replicates across four model families (24B-70B), though probes are model-specific and do not transfer across architectures.
- Generalization is source-dependent: leave-one-source-out evaluation shows each of synthetic, LMSYS-Chat-1M, and SafeDialBench captures distinct attack distributions, with detection on real-world LMSYS reaching 47-71% when its distribution is represented in training.

You can access the full paper at: https://arxiv.org/abs/2604.28129


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49dec885-ab4d-43ae-8d2f-670388391ba5",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "005414a1-4eef-413e-994f-3953607f641d",
  "sourceToolAssistantUUID": "49dec885-ab4d-43ae-8d2f-670388391ba5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T13:09:35.791Z_

<details><summary>↩ Tool result · `toolu_01E4Vo4JJiWAjUVjbfG7LXFv`</summary>

```text
Web search results for query: ""Jailbreaking Leaves a Trace" internal representations arXiv 2602.11495"

Links: [{"title":"[2602.11495] Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models","url":"https://arxiv.org/abs/2602.11495"},{"title":"Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models","url":"https://arxiv.org/html/2602.11495"},{"title":"Jailbreaking Leaves a Trace: Understanding and Detecting","url":"https://arxiv.org/pdf/2602.11495"},{"title":"Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2602.11495v2"},{"title":"Jailbreaking the Non-Transferable Barrier via Test-Time Data Disguising","url":"https://arxiv.org/html/2503.17198v1"},{"title":"Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection?","url":"https://arxiv.org/html/2510.06594"},{"title":"JailbreakLens: Interpreting Jailbreak Mechanism in the Lens of","url":"https://arxiv.org/pdf/2411.11114v1"},{"title":"Understanding Jailbreak Success: A Study of Latent Space Dynamics in Large Language Models","url":"https://arxiv.org/html/2406.09289v2"},{"title":"Detecting Jailbreak Attempts in Clinical Training LLMs Through Automated Linguistic Feature Extraction","url":"https://arxiv.org/html/2602.13321v1"},{"title":"Jailbreak Transferability Emerges from Shared Representations | OpenReview","url":"https://openreview.net/forum?id=UQK3tUsouK"}]

I found the paper! Here's what the search results show about "Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of Large Language Models" (arXiv 2602.11495):

## Overview

The paper was submitted on February 12, 2026 (v1) and last revised on February 20, 2026 (v2) by Sri Durga Sai Sowmya Kadali and Evangelos E. Papalexakis.

## Research Focus

The work studies jailbreaking from both security and interpretability perspectives by analyzing how internal representations differ between jailbreak and benign prompts. The authors conduct a systematic layer-wise analysis across multiple open-source models, including GPT-J, LLaMA, Mistral, and the state-space model Mamba, and identify consistent latent-space patterns associated with harmful inputs.

## Key Contributions

The researchers extract layer-wise internal representations such as multi-head attention and layer output/hidden state representation, apply tensor decomposition techniques, and demonstrate how these latent representations can be used to identify layers particularly susceptible to adversarial manipulation and to intervene during inference.

## Results

On an abliterated LLaMA 3.1 8B model, selectively bypassing high-susceptibility layers blocks 78% of jailbreak attempts while preserving benign behavior on 94% of benign prompts, with this intervention operating entirely at inference time and introducing minimal overhead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6c84068-093d-4c43-9171-a140cf5caee4",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "c5c00caa-d0fc-4b32-95ce-c364f1285bb7",
  "sourceToolAssistantUUID": "e6c84068-093d-4c43-9171-a140cf5caee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T13:09:36.616Z_

<details><summary>↩ Tool result · `toolu_01KFCVdsPG6Fr1aMJzuirPcn`</summary>

```text
Web search results for query: "JBShield representation-level jailbreak defense arXiv 2605"

Links: [{"title":"Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses","url":"https://arxiv.org/html/2605.03095v1"},{"title":"[2605.03095v1] Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses","url":"https://arxiv.org/abs/2605.03095v1"},{"title":"GitHub - NISPLab/JBShield: Code for USENIX Security 2025 paper \"JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation\"","url":"https://github.com/NISPLab/JBShield"},{"title":"[2605.03095] Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses","url":"https://arxiv.org/abs/2605.03095"},{"title":"JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and ManipulationThis is the full version of the paper accepted by USENIX Security 2025.","url":"https://arxiv.org/html/2502.07557v1"},{"title":"[2502.07557] JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation","url":"https://arxiv.org/abs/2502.07557"},{"title":"[Literature Review] JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation","url":"https://www.themoonlight.io/en/review/jbshield-defending-large-language-models-from-jailbreak-attacks-through-activated-concept-analysis-and-manipulation"},{"title":"JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.07557/sso-callbackv1"},{"title":"[PDF] JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/JBShield:-Defending-Large-Language-Models-from-and-Zhang-Zhai/80a1960dc99a2424273cf38de57f05bf4e896e42"},{"title":"JBShield: Defending Large Language Models from Jailbreak Attacks","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-341-zhang-shenyi.pdf"}]

Based on the search results, here's information about JBShield and representation-level jailbreak defense:

## Overview of JBShield

JBShield is a recent jailbreak defense with a 0% attack success rate in some settings, which detects malicious prompts via two concept signals: a toxic concept and a jailbreak concept.

## Two Components

JBShield consists of two key components: jailbreak detection (JBShield-D) and mitigation (JBShield-M). JBShield-D identifies jailbreak prompts by determining whether the input activates both toxic and jailbreak concepts, and when a jailbreak prompt is detected, JBShield-M adjusts the hidden representations of the target LLM by enhancing the toxic concept and weakening the jailbreak concept, ensuring LLMs produce safe content.

## Performance

JBShield achieved an average detection accuracy of 0.95 and reduced the average attack success rate of various jailbreak attacks to 2% from 61% across distinct LLMs.

## Recent Research (arXiv 2605)

The arXiv paper 2605.03095 titled "Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses" represents more recent work that evaluates JBShield's robustness. This research achieved an average attack success rate (ASR) of 46.2% across five configurations on Llama-3-8B using JB-GCG attacks, and showed that the attack remains effective against JBShield-M, achieving ASR up to 30.7% across evaluated settings. The researchers introduced Representation Trajectory Verification (RTV), a new defense based on Mahalanobis outlier detection over multi-layer refusal-direction fingerprints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dc91dc8-f13f-48bb-870d-af02c43b4d0c",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "8383c71a-bc8e-4aab-be9c-03dd23089457",
  "sourceToolAssistantUUID": "9dc91dc8-f13f-48bb-870d-af02c43b4d0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T13:09:39.459Z_

Now let me get more details on SALO and the refusal trajectory paper, as well as the SelfGrader paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8383c71a-bc8e-4aab-be9c-03dd23089457",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QfBtahQv1iVan1d7b3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc199d5c-1c4a-470e-ae3c-acd46b4084f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ei8ya93Va7NAYSbX25APVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4104,
      "cache_read_input_tokens": 15298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4104,
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

_source line 29 · 2026-05-15T13:09:40.411Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LMEWgbS4PW4NSETqtprV6C`</summary>

```json
{
  "query": "SALO sparse activation localization operator jailbreak detection refusal trajectory arXiv 2605.02958"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc199d5c-1c4a-470e-ae3c-acd46b4084f9",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QfBtahQv1iVan1d7b3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ee9f02e-007e-4cab-b22a-f22ebb67dfdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ei8ya93Va7NAYSbX25APVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4104,
      "cache_read_input_tokens": 15298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4104,
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

_source line 30 · 2026-05-15T13:09:40.943Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018BLV3CyWaXab8QQf2qapTN`</summary>

```json
{
  "query": "SelfGrader token-level logits jailbreak detection arXiv 2604.01473"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ee9f02e-007e-4cab-b22a-f22ebb67dfdb",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4QfBtahQv1iVan1d7b3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b53d2018-1c30-45ca-942b-5cc166307283",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ei8ya93Va7NAYSbX25APVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4104,
      "cache_read_input_tokens": 15298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4104,
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

_source line 31 · 2026-05-15T13:09:47.156Z_

<details><summary>↩ Tool result · `toolu_01LMEWgbS4PW4NSETqtprV6C`</summary>

```text
Web search results for query: "SALO sparse activation localization operator jailbreak detection refusal trajectory arXiv 2605.02958"

Links: [{"title":"Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection","url":"https://arxiv.org/html/2605.02958"},{"title":"[2605.02958] Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection","url":"https://arxiv.org/abs/2605.02958"},{"title":"[2206.14550] SALO: An Efficient Spatial Accelerator Enabling Hybrid Sparse Attention Mechanisms for Long Sequences","url":"https://ar5iv.labs.arxiv.org/html/2206.14550"},{"title":"[2605.04700v1] Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization","url":"https://arxiv.org/abs/2605.04700v1"},{"title":"Weakly Supervised Action Localization by Sparse ...","url":"https://www.computer.org/csdl/proceedings-article/cvpr/2018/642000g752/17D45WODaoG"},{"title":"Minimal, Local, Causal Explanations for Jailbreak Success in Large Language Models","url":"https://arxiv.org/html/2605.00123"},{"title":"HiddenDetect: Detecting Jailbreak Attacks against Large Vision-Language Models via Monitoring Hidden States","url":"https://arxiv.org/html/2502.14744v1"},{"title":"Rethinking Jailbreak Detection of Large Vision Language Models with Representational Contrastive Scoring","url":"https://arxiv.org/html/2512.12069v1"},{"title":"Machine Learning Apr 2025","url":"https://arxiv.org/list/cs.LG/2025-04?skip=1525&show=2000"},{"title":"On Passive-Scoping as a method for Large Language ...","url":"https://dspace.mit.edu/bitstream/handle/1721.1/162716/hernandez-adrianoh-meng-eecs-2025-thesis.pdf?sequence=1&isAllowed=y"}]

I found the paper! Here's what I found about SALO and the research:

## Paper Details

The paper is titled "Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection" and was published on arXiv on May 2, 2026 with identifier 2605.02958.

## What is SALO?

SALO (Sparse Activation Localization Operator) is a lightweight, inference-time mechanism designed for jailbreak detection. SALO is grounded in causal tracing findings and targets the persistent upstream refusal trajectory.

## Key Research Findings

The research demonstrates that refusal is a dynamic and sparse process rather than a localized outcome, and using Causal Tracing, the authors uncovered the Refusal Trajectory—a persistent upstream signature that remains intact even when adversarial attacks (e.g., GCG) suppress terminal signals.

## Performance

SALO effectively recovers defense capabilities against forced-decoding attacks, improving detection rates from ~0% to >90% where methods relying on terminal states perform poorly. While SALO utilizes a learned detector, it is trained exclusively on standard safety alignment data without ever seeing adversarial examples, granting it zero-shot generalization capabilities to unseen attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ee9f02e-007e-4cab-b22a-f22ebb67dfdb",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "2eccac49-d7df-4848-a25b-1548b50d3153",
  "sourceToolAssistantUUID": "0ee9f02e-007e-4cab-b22a-f22ebb67dfdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T13:09:48.598Z_

<details><summary>↩ Tool result · `toolu_018BLV3CyWaXab8QQf2qapTN`</summary>

```text
Web search results for query: "SelfGrader token-level logits jailbreak detection arXiv 2604.01473"

Links: [{"title":"SelfGrader: Stable Jailbreak Detection for Large Language Models using Token-Level Logits","url":"https://arxiv.org/html/2604.01473v2"},{"title":"SelfGrader: Detecting Jailbreak Attacks on Large Language Models with Token-Level Logit Distribution | OpenReview","url":"https://openreview.net/forum?id=qRSlhvA38I"},{"title":"Lockpicking LLMs: A Logit-Based Jailbreak Using Token- ...","url":"https://arxiv.org/abs/2405.13068"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf"},{"title":"A Logit-Based Jailbreak Using Token-level Manipulation","url":"https://arxiv.org/pdf/2405.13068"},{"title":"TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense","url":"https://arxiv.org/html/2604.07727"},{"title":"Safety World Model for Proactive Early Jailbreak Detection","url":"https://arxiv.org/pdf/2604.16824"},{"title":"SoK: Evaluating Jailbreak Guardrails for Large Language Models","url":"https://arxiv.org/html/2506.10597v1"},{"title":"JailbreakBench: An Open Robustness Benchmark for ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/63092d79154adebd7305dfd498cbff70-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"LLM JAILBREAK DETECTION FOR (ALMOST) FREE!","url":"https://arxiv.org/pdf/2509.14558"}]

I found comprehensive information about the paper. Here's what the search reveals:

SelfGrader is a lightweight guardrail method that formulates jailbreak detection as a numerical grading problem using token-level logits. 

Specifically, SelfGrader evaluates the safety of a user query within a compact set of numerical tokens (NTs) (e.g., 0–9) and interprets their logit distribution as an internal safety sign. The method introduces a dual-perspective scoring rule that considers both the maliciousness and benignness of the query, yielding a stable and interpretable score that reflects harmfulness and reduces the false positive rate simultaneously.

Unlike existing guardrail methods that typically rely on internal features or textual responses to detect malicious queries (which either introduce substantial latency or suffer from the randomness in text generation), SelfGrader eliminates the need for expensive safety-classifier training or slow internal-representation inspection, making it advantageous for practical deployment and compatible with low-resource or latency-sensitive settings.

Extensive experiments across diverse jailbreak benchmarks, multiple LLMs, and state-of-the-art guardrail baselines demonstrate that SelfGrader achieves accurate and robust detection while maintaining low computational overhead and latency.

The paper is authored by Zikai Zhang, Rui Hu, Olivera Kotevska, and Jiahao Xu from the University of Nevada, Reno and Oak Ridge National Laboratory, with a recent update dated April 14, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b53d2018-1c30-45ca-942b-5cc166307283",
  "isSidechain": true,
  "promptId": "e107a35d-684d-4d83-b267-ecf24af0cd65",
  "agentId": "a997c333ffc3ee2fb",
  "type": "user",
  "uuid": "2001e7fc-3552-4fdc-a230-3ef420caa674",
  "sourceToolAssistantUUID": "b53d2018-1c30-45ca-942b-5cc166307283",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T13:10:56.563Z_

Here is the comprehensive report of all findings across the six searches.

---

## Search 1: "multi-turn jailbreak defense activation trajectory 2026"

### Papers/Works Found:

1. **Latent Adversarial Detection (LAD): Adaptive Probing of LLM Activations for Multi-Turn Attack Detection** (arXiv 2604.28129, April 30, 2026)
   - Proposes probing the target LLM's internal activations to detect adversarial intent across multi-turn conversations. Identifies "adversarial restlessness" -- each phase shift in a multi-turn attack moves the activation in the residual stream, producing elevated cumulative path length. Five scalar trajectory features lift detection from 76.2% to 93.8% on synthetic data. Probes are model-specific and do not transfer across architectures. Real-world LMSYS detection reaches 47-71%.
   - **This is the most directly relevant paper to your idea.** It uses internal activation trajectories for multi-turn detection, but it does NOT combine this with external semantic tracking.

2. **TROJail: Trajectory-Level Optimization for Multi-Turn Large Language Model Jailbreaks with Process Rewards** (arXiv 2512.07761, Dec 2025)
   - An *attack* paper, not a defense. Uses trajectory-level optimization for multi-turn jailbreaking.

3. **Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses** (arXiv 2605.03095, May 2026)
   - Attacks JBShield's representation-level defense and proposes **Representation Trajectory Verification (RTV)**, a new defense using Mahalanobis outlier detection over multi-layer refusal-direction fingerprints. Primarily single-turn focused.

4. **Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models** (arXiv 2601.05445, Jan 2026)
   - An attack paper, not defense.

---

## Search 2: "dual signal jailbreak detection latent activation semantic 2026"

### Papers/Works Found:

1. **Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection** (arXiv 2605.02958, May 2, 2026)
   - Discovers the "Refusal Trajectory" -- a persistent upstream latent signature that remains intact even when adversarial attacks suppress terminal refusal signals. Introduces **SALO (Sparse Activation Localization Operator)**, a lightweight inference-time detector that improves detection from ~0% to >90% against forced-decoding attacks. Trained only on standard safety alignment data with zero-shot generalization. **Internal activations only; no external semantic tracking.**

2. **SelfGrader: Stable Jailbreak Detection for LLMs using Token-Level Logits** (arXiv 2604.01473, April 2026)
   - Uses token-level logit distributions as an internal safety signal. Dual-perspective scoring rule. Lightweight. **Single-turn, no external semantic tracking.**

3. **Jailbreaking Leaves a Trace: Understanding and Detecting Jailbreak Attacks from Internal Representations of LLMs** (arXiv 2602.11495, Feb 2026)
   - Layer-wise analysis of internal representations across GPT-J, LLaMA, Mistral, Mamba. Tensor decomposition to identify susceptible layers. On abliterated LLaMA 3.1 8B, selectively bypassing high-susceptibility layers blocks 78% of jailbreaks while preserving 94% benign behavior. **Internal representations only; single-turn focus.**

4. **HiddenDetect: Detecting Jailbreak Attacks against Large Vision-Language Models via Monitoring Hidden States** (arXiv 2502.14744, Feb 2025)
   - Hidden state monitoring for vision-language models. **Internal only.**

5. **A Hybrid Perplexity-MAS Framework for Proactive Jailbreak Attack Detection** (Applied Sciences journal)
   - Combines perplexity (statistical anomaly) with semantic similarity measures. This is closer to "dual signal" but uses external text-level features (perplexity + embedding cosine similarity), not internal model activations. **No internal activation analysis.**

---

## Search 3: "stateful defense multi-turn jailbreak arXiv 2026"

### Papers/Works Found:

1. **DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs** (arXiv 2602.16935, Feb 2026)
   - Uses an RNN architecture that ingests task-attention weighted embeddings to model intent trajectories. Maintains a persistent hidden state as "contextual memory" to detect "intent drift" across turns. Achieves 0.84 F1-score with sub-20ms latency on T4 GPU. **This uses EXTERNAL semantic embeddings processed by an RNN -- it does NOT probe the target LLM's internal activations. It is a separate monitoring model.**

2. **Recursive Language Models for Jailbreak Detection (RLM-JB)** (arXiv 2602.16520, Feb 2026)
   - Treats jailbreak detection as a procedure rather than one-shot classification. F1 up to 98.49% on AutoDAN. **External/procedural approach.**

3. **AJAR: Adaptive Jailbreak Architecture for Red-teaming** (arXiv 2601.10971, Jan 2026)
   - Attack paper.

4. **M2S: Multi-turn to Single-turn jailbreak in Red Teaming** (arXiv 2503.04856; ACL 2025)
   - Converts multi-turn attacks to single-turn for easier defense evaluation. Attack-side work.

---

## Search 4: "DeepContext multi-turn jailbreak RNN"

### Detailed Findings on DeepContext:

- **DeepContext** (arXiv 2602.16935) uses an RNN over fine-tuned turn-level embeddings (external to the target LLM). It formulates user intent as a state-space problem. The RNN's hidden state evolves with the conversation, acting as contextual memory. It monitors transitions to detect "intent drift."
- **Critically**: DeepContext operates on embeddings of the conversational text (external semantic signal). It does NOT probe the target model's internal activations. It is purely an external trajectory tracker.

---

## Search 5: "latent adversarial detection activation trajectory jailbreak"

### Papers/Works Found:

1. **LAD (Latent Adversarial Detection)** (arXiv 2604.28129) -- already detailed above. Internal activation probing for multi-turn.

2. **Tracing the Dynamics of Refusal / SALO** (arXiv 2605.02958) -- already detailed above. Internal refusal trajectory, single-turn focus.

3. **Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation** (arXiv 2604.07835, April 2026)
   - An *attack* that dynamically ablates contextual representations at inference time. Shows vulnerability of internal defenses.

4. **N-GLARE: Non-Generative Latent Representation-Efficient LLM Safety Evaluator** (arXiv 2511.14195, Nov 2025)
   - Uses latent representations for safety evaluation. Single-turn.

---

## Search 6: "multi-turn jailbreak defense fusion internal external signals"

### Papers/Works Found:

1. **TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense** (arXiv 2604.07727, April 9, 2026)
   - **This is the closest paper to your proposed idea.** TrajGuard has TWO modules:
     - **Streaming Geometric Surveillance (SGS)**: Monitors hidden states in critical layers (INTERNAL signal) to track whether decoding deviates from benign behavior.
     - **Prompt-Answer Inference Referee (PAIR-Judge)**: Reviews decoded tokens from a SEMANTIC perspective (EXTERNAL signal) when SGS detects an anomaly.
   - Achieves 95% defense rate across 12 attacks, 5.2 ms/token latency, <1.5% false positive rate.
   - **However**: TrajGuard operates at decoding time within a single turn -- it monitors the generation process, not multi-turn conversation trajectories. The "internal + external" fusion is within a single generation, not across a multi-turn dialogue.

2. **ProAct: Proactive Defense Against LLM Jailbreak** (arXiv 2510.05052)
   - Misleads iterative jailbreak methods with spurious responses. Uses signals from defensive layers to trigger responses. Not an activation-based approach.

---

## Critical Assessment: Is Your Idea Novel?

### The specific gap your idea fills:

Your proposed approach -- combining **internal model activations** (what the model "thinks") with **external semantic trajectory tracking** (how the conversation evolves textually) for **multi-turn** jailbreak defense -- does NOT appear to exist in the current literature. Here is why:

| Paper | Internal Activations | External Semantic Tracking | Multi-Turn | Fusion of Both |
|-------|---------------------|---------------------------|------------|----------------|
| **LAD** (2604.28129) | YES (residual stream probing) | No | YES | No |
| **DeepContext** (2602.16935) | No | YES (RNN over embeddings) | YES | No |
| **TrajGuard** (2604.07727) | YES (hidden state geometry) | YES (PAIR-Judge semantic check) | No (single-turn decoding) | Partial (not multi-turn) |
| **SALO** (2605.02958) | YES (refusal trajectory) | No | No | No |
| **JBShield** (2502.07557) | YES (concept activation) | No | No | No |
| **Jailbreaking Leaves a Trace** (2602.11495) | YES (layer-wise analysis) | No | No | No |
| **SelfGrader** (2604.01473) | YES (logit distributions) | No | No | No |

### Concurrent work to watch closely:

1. **LAD (April 2026)** is the most threatening concurrent work. It does internal activation trajectory analysis for multi-turn detection. If you add an external semantic component to something LAD-like, you are building directly on top of it. You must cite and differentiate clearly.

2. **DeepContext (Feb 2026)** is the mirror image -- it does external semantic trajectory tracking for multi-turn detection via RNN. Your work would need to explain why adding internal activations improves over DeepContext's approach.

3. **TrajGuard (April 2026)** is the closest to "dual signal fusion" but is limited to single-turn decoding-time defense. Extending this paradigm to multi-turn conversations would be a natural and arguably obvious next step, so you should move quickly.

### Bottom line:

**No existing paper combines both internal activation signals AND external semantic trajectory tracking for multi-turn jailbreak defense.** The three closest works (LAD, DeepContext, TrajGuard) each cover a subset of your idea. The novelty is real but the window may be narrow -- the components exist and someone else could combine them at any time.

---

Sources:
- [LAD: Latent Adversarial Detection (arXiv 2604.28129)](https://arxiv.org/abs/2604.28129)
- [DeepContext: Stateful Real-Time Detection (arXiv 2602.16935)](https://arxiv.org/abs/2602.16935)
- [TrajGuard: Streaming Hidden-state Trajectory Detection (arXiv 2604.07727)](https://arxiv.org/abs/2604.07727)
- [Tracing the Dynamics of Refusal / SALO (arXiv 2605.02958)](https://arxiv.org/abs/2605.02958)
- [Jailbreaking Leaves a Trace (arXiv 2602.11495)](https://arxiv.org/abs/2602.11495)
- [Revisiting JBShield (arXiv 2605.03095)](https://arxiv.org/abs/2605.03095)
- [JBShield original (arXiv 2502.07557)](https://arxiv.org/abs/2502.07557)
- [SelfGrader (arXiv 2604.01473)](https://arxiv.org/abs/2604.01473)
- [TROJail (arXiv 2512.07761)](https://arxiv.org/abs/2512.07761)
- [Knowledge-Driven Multi-Turn Jailbreaking (arXiv 2601.05445)](https://arxiv.org/abs/2601.05445)
- [RLM-JB: Recursive Language Models for Jailbreak Detection (arXiv 2602.16520)](https://arxiv.org/abs/2602.16520)
- [AJAR: Adaptive Jailbreak Architecture (arXiv 2601.10971)](https://arxiv.org/abs/2601.10971)
- [M2S: Multi-turn to Single-turn (arXiv 2503.04856)](https://arxiv.org/abs/2503.04856)
- [Silencing the Guardrails (arXiv 2604.07835)](https://arxiv.org/abs/2604.07835)
- [HiddenDetect (arXiv 2502.14744)](https://arxiv.org/abs/2502.14744)
- [ProAct: Proactive Defense (arXiv 2510.05052)](https://arxiv.org/abs/2510.05052)
- [Multi-turn Jailbreak Attacks: Strategies & Defenses (EmergentMind)](https://www.emergentmind.com/topics/multi-turn-jailbreak-attacks)
- [LLM Jailbreaking in 2026 (redteams.ai)](https://redteams.ai/blog/llm-jailbreaking-2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2001e7fc-3552-4fdc-a230-3ef420caa674",
  "isSidechain": true,
  "agentId": "a997c333ffc3ee2fb",
  "requestId": "req_011Cb4Qg5AYe1PWvpm6tXbv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e42ae40-11ea-45c5-9639-69b02831e578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c0bcb86-30f4-43dd-b09b-310fbe17d7f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nSxgfB8oqsZzrrds9g4tN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 19402,
      "output_tokens": 3495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1991
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3495,
          "cache_read_input_tokens": 19402,
          "cache_creation_input_tokens": 1991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1991,
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
