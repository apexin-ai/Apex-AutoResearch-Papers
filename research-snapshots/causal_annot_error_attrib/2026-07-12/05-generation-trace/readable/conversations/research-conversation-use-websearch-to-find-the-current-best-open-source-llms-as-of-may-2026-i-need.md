# Research conversation: Use WebSearch to find the current best open-source LLMs as of May 2026. I need this for a research project on activation

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3443a00d7c4e919d.jsonl`
- **Structured JSON:** [`612c42d228bffc83d495.json`](../../sessions/61/612c42d228bffc83d495.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-16T05:56:55.269Z_

Use WebSearch to find the current best open-source LLMs as of May 2026. I need this for a research project on activation steering / mechanistic interpretability, so I need models where:
- Weights are openly available
- Architecture allows layer-by-layer hidden state extraction (TransformerLens compatible or similar)
- Models in the 7B-70B parameter range are most relevant

Search for:
1. "best open source LLM 2026" 
2. "top open source language model May 2026"
3. "SOTA open source LLM leaderboard 2026"
4. "TransformerLens compatible models 2026" or "mechanistic interpretability models 2026"
5. Check if LLaMA 4 or any successor is out, or if there are newer model families (Mistral, Qwen, etc.)

Report the top current open-source models with their sizes, release dates, and whether they'd be suitable for mechanistic interpretability / activation steering research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "b2b111fc-e52c-477d-807d-48a745b84753",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T05:56:55.273Z_

```json
{
  "parentUuid": "b2b111fc-e52c-477d-807d-48a745b84753",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
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
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "df964cce-fcf7-4c97-aa07-8ce28d97ac5b",
  "timestamp": "2026-05-16T05:56:55.273Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T05:56:57.580Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NL4jNV5e7eJUdH2yHbJkoi`</summary>

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
  "parentUuid": "df964cce-fcf7-4c97-aa07-8ce28d97ac5b",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jUP8fVS7ZPQHahuZfn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0924970f-8ccf-4495-bda3-9a67bdf9d67d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RK4tUrhR59TeX9aASs3M6a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 779
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 779,
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

_source line 4 · 2026-05-16T05:56:57.582Z_

<details><summary>↩ Tool result · `toolu_01NL4jNV5e7eJUdH2yHbJkoi`</summary>

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
  "parentUuid": "0924970f-8ccf-4495-bda3-9a67bdf9d67d",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "e833f06b-0042-404d-8d3a-13e6c6827335",
  "sourceToolAssistantUUID": "0924970f-8ccf-4495-bda3-9a67bdf9d67d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T05:57:00.552Z_

Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e833f06b-0042-404d-8d3a-13e6c6827335",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jUZFNb3d2Jw62BSeT5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "593c7af2-6c0e-4b82-be0b-fca5167d2bf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTxLAni3HAUeMrDuCD9iCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9002,
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

_source line 6 · 2026-05-16T05:57:00.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EHTLXJSebV7AzXEicxdsj8`</summary>

```json
{
  "query": "best open source LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "593c7af2-6c0e-4b82-be0b-fca5167d2bf5",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jUZFNb3d2Jw62BSeT5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cea8a4e-5810-4e72-a0b2-9ba82c7904a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTxLAni3HAUeMrDuCD9iCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9002,
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

_source line 7 · 2026-05-16T05:57:01.031Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01My1KXH2KSoRBQFmeQv27dZ`</summary>

```json
{
  "query": "top open source language model May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cea8a4e-5810-4e72-a0b2-9ba82c7904a6",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jUZFNb3d2Jw62BSeT5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b3ce6a8-e083-43bb-acb9-9af1aba95e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTxLAni3HAUeMrDuCD9iCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9002,
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

_source line 8 · 2026-05-16T05:57:01.561Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011CqgGXoedRjhkrPs91Bi61`</summary>

```json
{
  "query": "SOTA open source LLM leaderboard 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b3ce6a8-e083-43bb-acb9-9af1aba95e81",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jUZFNb3d2Jw62BSeT5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "912f2d5c-1827-4424-957c-028c249f7681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTxLAni3HAUeMrDuCD9iCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9002,
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

_source line 9 · 2026-05-16T05:57:02.086Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AoHYN4DDJh1Ja2tugu9jhX`</summary>

```json
{
  "query": "TransformerLens compatible models 2026 mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "912f2d5c-1827-4424-957c-028c249f7681",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jUZFNb3d2Jw62BSeT5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c85f573-3502-4c84-a2de-106fb699f29b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTxLAni3HAUeMrDuCD9iCq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9002,
      "output_tokens": 257,
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
          "output_tokens": 257,
          "cache_read_input_tokens": 9002,
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

### Tool call

_source line 10 · 2026-05-16T05:57:02.090Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RMXhho2eaBAxE7fKyXQudR`</summary>

```json
{
  "query": "LLaMA 4 release open weights 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c85f573-3502-4c84-a2de-106fb699f29b",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jUZFNb3d2Jw62BSeT5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b76f465-22c8-4c20-adb4-2ade2e1b000d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTxLAni3HAUeMrDuCD9iCq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9002,
      "output_tokens": 257,
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
          "output_tokens": 257,
          "cache_read_input_tokens": 9002,
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

_source line 11 · 2026-05-16T05:57:08.731Z_

<details><summary>↩ Tool result · `toolu_01RMXhho2eaBAxE7fKyXQudR`</summary>

```text
Web search results for query: "LLaMA 4 release open weights 2026"

Links: [{"title":"Llama (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Llama_(language_model)"},{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Llama 4 Open-Weights Multimodal AI for Builders 2026","url":"https://www.buildmvpfast.com/blog/llama-4-open-weights-multimodal-ai-builders-2026"},{"title":"Best Llama Models in 2026 — Meta's Open-Source AI Dominance | Remote OpenClaw","url":"https://www.remoteopenclaw.com/blog/best-llama-models-2026"},{"title":"Industry Leading, Open-Source AI | Llama","url":"https://www.llama.com/"},{"title":"Meta AI All Models Available: Llama‑4, Llama‑3, and Deployment Options","url":"https://www.datastudios.org/post/meta-ai-all-models-available-llama-4-llama-3-and-deployment-options"},{"title":"Llama 4 Review: Meta Open Weights MoE — 7.5/10 | ThePlanetTools.ai","url":"https://theplanettools.ai/tools/llama-4"},{"title":"Meta’s Llama 4 is Here: A Giant Leap in AI, Open-Weight Power, and Multimodal Brilliance | by Sai Krishna Reddy Mudhiganti | Medium","url":"https://medium.com/@saimudhiganti/metas-llama-4-is-here-a-giant-leap-in-ai-open-weight-power-and-multimodal-brilliance-ac6301cbc469"},{"title":"Llama 4: Did Meta just push the panic button?","url":"https://www.interconnects.ai/p/llama-4"},{"title":"Meta Llama: The Open-Weight AI Reaching 3.27B Users","url":"https://techjacksolutions.com/ai-tools/meta-llama/what-is-meta-llama/"}]

Based on the search results, here's what I found about LLaMA 4 release with open weights in 2026:

## LLaMA 4 Release Overview

The latest version is Llama 4, released in April 2025. Llama 4 Scout and Llama 4 Maverick are the first open-weight natively multimodal models with unprecedented context length support and the first built using a mixture-of-experts (MoE) architecture.

## Current Status as of 2026

As of April 2026, Llama 4 remains Meta's current generation. Llama 4 is Meta's open-weight multimodal large language model family released April 5, 2025. The models are available for free download on Hugging Face under the Llama 4 Community License.

## Major Models Available

- **Llama 4 Scout**: 17 billion active parameters, 16 experts, and 109 billion total parameters that delivers state-of-the-art performance for its class. Llama 4 Scout dramatically increases the supported context length from 128K in Llama 3 to an industry leading 10 million tokens.

- **Llama 4 Maverick**: A multimodal mixture-of-experts model with 288B active parameters, 16 experts, and nearly two trillion total parameters.

- **Llama 4 Behemoth**: Llama 4 Behemoth, Meta's largest model, was still in training at last public update and has not been released as of April 2026.

## Transition Away from Llama

Notably, in April 2026, Meta Superintelligence Labs released Muse Spark as a replacement for Llama.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b76f465-22c8-4c20-adb4-2ade2e1b000d",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "5e27ee9d-2735-4aa0-82eb-14b8af7504be",
  "sourceToolAssistantUUID": "0b76f465-22c8-4c20-adb4-2ade2e1b000d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T05:57:08.954Z_

<details><summary>↩ Tool result · `toolu_011CqgGXoedRjhkrPs91Bi61`</summary>

```text
Web search results for query: "SOTA open source LLM leaderboard 2026"

Links: [{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2025–2026: Llama, Mistral, DeepSeek, Qwen | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm/open-models"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Open Source LLM Leaderboard 2026: Rankings, Benchmarks & the Best Models Right Now &#045; VERTU® Official Site","url":"https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"}]

Based on the web search results, here's what I found about SOTA open source LLM leaderboards in 2026:

## Key Leaderboard Resources

The Vellum Open Source LLM Leaderboard displays the latest public benchmark performance for open-weight and open-source models released after April 2024, with data from model providers and independent evaluations by Vellum or the open-source community.

CodeSOTA tracks benchmark comparisons across open-weight models including DeepSeek-R1, Llama 3, Qwen 2.5, Mistral, and Gemma 3, updated as of April 2026.

## Top Performing Open-Source Models

S-tier models like GLM-4.7, Kimi K2.5, and MiniMax M2.5 are matching or exceeding proprietary model performance on specific benchmarks.

Specific standouts include:

- **GLM-4.7**: Has an HumanEval score of 94.2 and scores 95.7 on AIME 2025, 85.7 on GPQA Diamond, and 84.9 on LiveCodeBench.

- **Kimi K2.5**: Has a HumanEval score of 99.0, leads in MMLU (92.0), IFEval (94.0), MATH-500 (98.0), and GPQA Diamond (87.6).

- **DeepSeek-R1**: A 671B MoE reasoning leader trained with reinforcement learning, matching or exceeding GPT-4o on math and coding benchmarks.

## Benchmarks Tracked

The Hugging Face Open LLM Leaderboard lets you explore open-source model performance on tests such as IFEval, BBH, MATH, GPQA, MUSR, and MMLU-PRO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "912f2d5c-1827-4424-957c-028c249f7681",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "7bf76e23-88d4-4424-98f1-878096107ec4",
  "sourceToolAssistantUUID": "912f2d5c-1827-4424-957c-028c249f7681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T05:57:09.256Z_

<details><summary>↩ Tool result · `toolu_01EHTLXJSebV7AzXEicxdsj8`</summary>

```text
Web search results for query: "best open source LLM 2026"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"11 Top Open-Source LLMs for 2026 and Their Uses | DataCamp","url":"https://www.datacamp.com/blog/top-open-source-llms"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Open Source LLM Platforms in 2026: Ollama, OpenRouter, Groq, NVIDIA NIM — Which One Should You Use? | by Developer Awam | CodeX | May, 2026 | Medium","url":"https://medium.com/codex/open-source-llm-platforms-in-2026-ollama-openrouter-groq-nvidia-nim-which-one-should-you-use-2f11c7ba60bc"}]

Based on the search results, here are the best open-source LLMs in 2026:

## Top Overall Models

GLM 5.1 is a 744B-parameter MoE model with 40B active parameters and a 200K token context, positioned as a flagship release for coding, reasoning, and agentic workflows — currently the leading open-weights model on Artificial Analysis's Intelligence Index.

Kimi K2.6 Thinking currently leads open-source models on both Coding (78.57) and Agentic Coding (58.33), with GLM 5.1 and DeepSeek V4 Pro close behind on agentic work.

DeepSeek-V4 is designed for long-context reasoning, coding, and agentic workflows, with two large MoE models: DeepSeek-V4-Pro (1.6T total, 49B active) is the flagship model for maximum reasoning, coding, and agentic performance, and DeepSeek-V4-Flash (284B total, 13B active) is a more cost-efficient option.

## Best for General Use

For most users, Qwen3 is the best overall local LLM family because it balances quality, model sizes, multilingual support, tooling, and Apache 2.0 licensing.

## Best for Resource-Constrained Environments

Phi-4-mini is the most accessible local LLM of 2026, and you should start there if your hardware is limited.

## Best for Coding

Devstral is built specifically for agentic software engineering: exploring codebases, editing multiple files, fixing real bugs, working with tools — the kind of tasks where you want the model to actually understand your repo, not just autocomplete one line.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cea8a4e-5810-4e72-a0b2-9ba82c7904a6",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "312bbb6d-086e-4efd-8b42-50983d1990cd",
  "sourceToolAssistantUUID": "6cea8a4e-5810-4e72-a0b2-9ba82c7904a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T05:57:09.761Z_

<details><summary>↩ Tool result · `toolu_01AoHYN4DDJh1Ja2tugu9jhX`</summary>

```text
Web search results for query: "TransformerLens compatible models 2026 mechanistic interpretability"

Links: [{"title":"GitHub - TransformerLensOrg/TransformerLens: A library for mechanistic interpretability of GPT-style language models · GitHub","url":"https://github.com/TransformerLensOrg/TransformerLens"},{"title":"TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/"},{"title":"nnterp: A Standardized Interface for Mechanistic Interpretability of Transformers | OpenReview","url":"https://openreview.net/forum?id=ACic3VDIHp"},{"title":"transformer-lens · PyPI","url":"https://pypi.org/project/transformer-lens/1.3.0/"},{"title":"Releases · TransformerLensOrg/TransformerLens","url":"https://github.com/neelnanda-io/TransformerLens/releases"},{"title":"Transformer Lens Main Demo Notebook - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/demos/Main_Demo.html"},{"title":"TransformerLens/README.md at 9321ca07753f816eaa210a5c7a2cf094c47421fb · TransformerLensOrg/TransformerLens","url":"https://github.com/TransformerLensOrg/TransformerLens/blob/9321ca07753f816eaa210a5c7a2cf094c47421fb/README.md"},{"title":"TransformerLens/README.md at main · TransformerLensOrg/TransformerLens","url":"https://github.com/TransformerLensOrg/TransformerLens/blob/main/README.md"},{"title":"Transformer Lens (Grade A) - Claude Skill","url":"https://www.skillsdirectory.com/skills/zechenzhangagi-transformer-lens"},{"title":"Interpreto: An Explainability Library for Transformers","url":"https://arxiv.org/html/2512.09730"}]

Based on the search results, here's what I found about TransformerLens compatible models and mechanistic interpretability in 2026:

## TransformerLens Overview

TransformerLens is the de facto standard library for mechanistic interpretability research on GPT-style language models, created by Neel Nanda and maintained by Bryce Meyer, providing clean interfaces to inspect and manipulate model internals via HookPoints on every activation.

## Model Support

TransformerLens recently migrated to a new TransformerBridge system that increased model support from ~200 models to ~9,000 models. More specifically, TransformerLens lets you load in 50+ different open source language models. Recent additions include Gemma 3, MedGemma, and Qwen3-0.6B-Base.

## Mechanistic Interpretability Purpose

The goal of mechanistic interpretability is to take a trained model and reverse engineer the algorithms the model learned during training from its weights. You can cache any internal activation in the model, and add in functions to edit, remove or replace these activations as the model runs.

## Alternative Tools

Beyond TransformerLens, the mechanistic interpretability landscape has evolved. nnterp enables researchers to write intervention code once and deploy it across 50+ model variants spanning 16 architecture families. Other tools for activation access and intervention include NNsight, Neuronpedia, and NNterp.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c85f573-3502-4c84-a2de-106fb699f29b",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "979c293f-c3fe-450b-948d-b80fd8164db3",
  "sourceToolAssistantUUID": "1c85f573-3502-4c84-a2de-106fb699f29b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T05:57:14.046Z_

<details><summary>↩ Tool result · `toolu_01My1KXH2KSoRBQFmeQv27dZ`</summary>

```text
Web search results for query: "top open source language model May 2026"

Links: [{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Open-Source LLMs in 2026: Best AI Models | Medium","url":"https://medium.com/@servifyspheresolutions/the-free-models-running-the-world-af6a3d2e8758"},{"title":"Best Open Source LLM Leaderboard 2026","url":"https://onyx.app/open-llm-leaderboard"},{"title":"The Best Open-Source Small Language Models (SLMs) in 2026","url":"https://www.bentoml.com/blog/the-best-open-source-small-language-models"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"11 Top Open-Source LLMs for 2026 and Their Uses | DataCamp","url":"https://www.datacamp.com/blog/top-open-source-llms"},{"title":"10 Best Open Source LLMs to Evaluate in 2026","url":"https://kanerika.com/blogs/open-source-llms-models/"},{"title":"The Best Open Source LLMs and Their Uses in 2026 | igmGuru","url":"https://www.igmguru.com/blog/top-open-source-llms"}]

Based on the search results for the top open source language models in May 2026, here's what's leading the landscape:

## Top Open Source LLMs as of May 2026

**Overall Leaders:**

Kimi K2.6 Thinking is the strongest open-source entry across both key coding metrics, with 78.57 Coding Avg and 58.33 Agentic Coding Avg as of May 12, 2026.

GLM 5.1 is a 744B-parameter MoE (40B active) with a 200K token context, positioned as a flagship release for coding, reasoning, and agentic workflows — currently the leading open-weights model on Artificial Analysis's Intelligence Index.

**Other Top Performers:**

- Qwen 3.5 was released in February 2026 with a 397B MoE model, featuring unified vision-language capabilities and support for 201 languages, and is one of the top-ranked open-weight models across multiple benchmarks.

- DeepSeek-V4 was released on April 24, 2026, with variants including V4-Pro (1.6T total / 49B active) and V4-Flash (284B total / 13B active), both with 1M context and MIT licensing, scoring 69.99 on Coding Avg and 56.67 on Agentic Coding Avg on the May 12, 2026 LiveBench snapshot.

By May 2026, developers worldwide can download frontier-grade models, run them on their own hardware, and deploy them without paying per token.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b3ce6a8-e083-43bb-acb9-9af1aba95e81",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "269de79e-5a92-4b1b-a6c4-dd929bfd0242",
  "sourceToolAssistantUUID": "0b3ce6a8-e083-43bb-acb9-9af1aba95e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-16T05:57:19.761Z_

Now let me search for more specific information about the smaller model variants and their compatibility with interpretability tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "269de79e-5a92-4b1b-a6c4-dd929bfd0242",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jVmgWf3aa299gbnnuK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6f92179-91f9-463c-b119-d5ab30249597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9snb61dThtVGFhSh3WfgG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2961,
      "cache_creation_input_tokens": 2198,
      "cache_read_input_tokens": 10394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2198,
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

_source line 17 · 2026-05-16T05:57:19.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013GcJy95YpbdsVehbyAouF6`</summary>

```json
{
  "query": "Qwen3 model sizes 7B 14B 32B open weights 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6f92179-91f9-463c-b119-d5ab30249597",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jVmgWf3aa299gbnnuK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "241e4b66-6cfa-4cb6-9b5c-4c8e6e03feb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9snb61dThtVGFhSh3WfgG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2961,
      "cache_creation_input_tokens": 2198,
      "cache_read_input_tokens": 10394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2198,
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

_source line 18 · 2026-05-16T05:57:20.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mewwt6MqtJqdj9Wj5PRyE1`</summary>

```json
{
  "query": "Mistral 2026 open source model release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "241e4b66-6cfa-4cb6-9b5c-4c8e6e03feb4",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jVmgWf3aa299gbnnuK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df787ece-a8da-4e29-b97f-eeb608b46cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9snb61dThtVGFhSh3WfgG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2961,
      "cache_creation_input_tokens": 2198,
      "cache_read_input_tokens": 10394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2198,
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

_source line 19 · 2026-05-16T05:57:20.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011mSeVZ6EjhLGXK5XAfHn89`</summary>

```json
{
  "query": "TransformerLens supported models list Llama Qwen Gemma 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df787ece-a8da-4e29-b97f-eeb608b46cb0",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jVmgWf3aa299gbnnuK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b7e3dbd-a50d-4d00-ae85-0ce9775e74db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9snb61dThtVGFhSh3WfgG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2961,
      "cache_creation_input_tokens": 2198,
      "cache_read_input_tokens": 10394,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2198
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2961,
          "output_tokens": 196,
          "cache_read_input_tokens": 10394,
          "cache_creation_input_tokens": 2198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2198,
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

_source line 20 · 2026-05-16T05:57:25.153Z_

<details><summary>↩ Tool result · `toolu_013GcJy95YpbdsVehbyAouF6`</summary>

```text
Web search results for query: "Qwen3 model sizes 7B 14B 32B open weights 2026"

Links: [{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"},{"title":"Qwen API and Models | OpenRouter","url":"https://openrouter.ai/qwen"},{"title":"Qwen - Wikipedia","url":"https://en.wikipedia.org/wiki/Qwen"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Model Catalog - LM Studio","url":"https://lmstudio.ai/models"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen 3: The new open standard - by Nathan Lambert","url":"https://www.interconnects.ai/p/qwen-3-the-new-open-standard"},{"title":"Qwen Models Guide: 600M to 1 Trillion Parameters","url":"https://www.digitalapplied.com/blog/qwen-models-complete-guide"},{"title":"qwen3","url":"https://ollama.com/library/qwen3"},{"title":"What Is Qwen 3.5? Alibaba's Open-Weight Model That Runs on Your Phone | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-qwen-3-5-alibaba-open-weight-model"}]

Based on the search results, here's what I found about Qwen3 model sizes with open weights in 2026:

## Qwen3 Dense Models

Qwen3 includes 6 dense models with 32B, 14B, 8B, 4B, 1.7B, and 0.6B parameters — all models with the Apache 2.0 License. 

Specifically for the sizes you mentioned:
- Qwen3-14B is a dense 14.8B parameter causal language model from the Qwen3 series
- Qwen3-32B is a dense 32.8B parameter causal language model from the Qwen3 series

## Qwen3 MoE Models

Qwen3 open-weights two MoE models: Qwen3-235B-A22B, a large model with 235 billion total parameters and 22 billion activated parameters, and Qwen3-30B-A3B, a smaller MoE model with 30 billion total parameters and 3 billion activated parameters.

## License

All these models are distributed with the Apache 2.0 License, making them freely available for open-source use and modification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "241e4b66-6cfa-4cb6-9b5c-4c8e6e03feb4",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "763f725d-5eac-4b29-ac52-2dc21b651555",
  "sourceToolAssistantUUID": "241e4b66-6cfa-4cb6-9b5c-4c8e6e03feb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T05:57:25.619Z_

<details><summary>↩ Tool result · `toolu_011mSeVZ6EjhLGXK5XAfHn89`</summary>

```text
Web search results for query: "TransformerLens supported models list Llama Qwen Gemma 2025 2026"

Links: [{"title":"Model Properties Table - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html"},{"title":"Supported Models - vLLM","url":"https://docs.vllm.ai/en/latest/models/supported_models/"},{"title":"Model Catalog - LM Studio","url":"https://lmstudio.ai/models"},{"title":"Supported Models — vLLM","url":"https://docs.vllm.ai/en/v0.6.2/models/supported_models.html"},{"title":"library","url":"https://ollama.com/library"},{"title":"transformer_lens.loading_from_pretrained - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.loading_from_pretrained.html"},{"title":"New Ollama Models May 2026: Latest Releases & Updates","url":"https://www.promptquorum.com/local-llms/top-open-source-models-ollama"},{"title":"transformer_lens.HookedTransformerConfig - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.HookedTransformerConfig.html"},{"title":"Release v4.40.0: Llama 3, Idefics 2, Recurrent Gemma, Jamba, DBRX, OLMo, Qwen2MoE, Grounding Dino · huggingface/transformers","url":"https://github.com/huggingface/transformers/releases/tag/v4.40.0"},{"title":"GitHub - intel/ipex-llm: Accelerate local LLM inference and finetuning (LLaMA, Mistral, ChatGLM, Qwen, DeepSeek, Mixtral, Gemma, Phi, MiniCPM, Qwen-VL, MiniCPM-V, etc.) on Intel XPU (e.g., local PC with iGPU and NPU, discrete GPU such as Arc, Flex and Max); seamlessly integrate with llama.cpp, Ollama, HuggingFace, LangChain, LlamaIndex, vLLM, DeepSpeed, Axolotl, etc. · GitHub","url":"https://github.com/intel/ipex-llm"}]

Based on the search results, here's information about TransformerLens supported models:

## TransformerLens Supported Models

TransformerLens supports a range of models including various Qwen versions (Qwen2.5-72B, Qwen2.5-72B-Instruct, QwQ-32B-Preview, Qwen3-0.6B through Qwen3-14B) and Google Gemma models (gemma-2b, gemma-7b, gemma-2-2b through gemma-2-27b, and instruction-tuned variants).

The library has an extensive list of official supported models available in their documentation. The supported models include GPT-2 variants, OPT models, GPT-NeoX, EleutherAI Pythia models, and various other architectures.

For Llama models, TransformerLens includes support for certain Llama models not hosted on HuggingFace (llama-7b-hf, llama-13b-hf, llama-30b-hf, llama-65b-hf).

To view the complete and most up-to-date list of supported models, you can check the official TransformerLens documentation at their model properties table on their website, which provides an interactive table with all available models and their properties. The supported models list appears to be regularly updated, particularly for newer model families as they become available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b7e3dbd-a50d-4d00-ae85-0ce9775e74db",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "f0acaeb3-a013-4384-9bd1-32363adac738",
  "sourceToolAssistantUUID": "3b7e3dbd-a50d-4d00-ae85-0ce9775e74db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T05:57:29.115Z_

<details><summary>↩ Tool result · `toolu_01Mewwt6MqtJqdj9Wj5PRyE1`</summary>

```text
Web search results for query: "Mistral 2026 open source model release"

Links: [{"title":"Mistral releases a new open source model for speech generation | TechCrunch","url":"https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation/"},{"title":"Mistral 3 AI Explained - Open-Source Models Guide 2026 — Shawn Kanungo","url":"https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026"},{"title":"Mistral AI Drops New Open-Source Model. The Internet Is Not Impressed, Except for One Thing - Decrypt","url":"https://decrypt.co/366275/mistral-ai-open-source-model-agents-internet-not-impressed"},{"title":"Mistral AI Models 2026: Small 4, Large 3, Voxtral TTS, Forge — Complete Guide | Serenities AI","url":"https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide"},{"title":"Mistral AI Releases New Open Source Models 2026 |","url":"https://multi-ai.ai/en/blog/mistral-ai-releases-new-open-source-models-for-en"},{"title":"Mistral AI Latest Models 2026: The Powerful Breakthroughs (and Hidden Limitations)","url":"https://aizolo.com/blog/mistral-ai-latest-models-2026/"},{"title":"Mistral AI Models 2026: A Powerful Complete Guide for Builders (With Some Limitations)","url":"https://aizolo.com/blog/mistral-ai-models-2026/"},{"title":"Mistral launches open-source speech AI model: Why it matters","url":"https://yourstory.com/ai-story/mistral-open-source-speech-ai-model"},{"title":"Mistral AI Drops New Open-Source Model. The Internet Is Not Impressed, Except for One Thing","url":"https://tech.yahoo.com/ai/articles/mistral-ai-drops-open-source-213103938.html"},{"title":"OpenAI, Mistral AI release new hardware-efficient language models - SiliconANGLE","url":"https://siliconangle.com/2026/03/17/openai-mistral-ai-release-new-hardware-efficient-language-models/"}]

Based on the search results, here's a comprehensive overview of Mistral's open-source model releases in 2026:

## Major 2026 Releases

Mistral 3 AI is a family of 10 artificial intelligence models that launched in December 2025, with continued momentum into 2026. Mistral 3 brings vision capabilities to every model, doubles the context window, adds reasoning modes, supports 40+ languages natively, and offers models small enough to run on your phone.

### Flagship Models

Released December 2, 2025 but still the flagship in 2026, Mistral Large 3 is the largest open-weight MoE model from a major lab. Mistral Large 3 is the largest open-weight Mixture-of-Experts model from a major lab, trained with 41 billion active parameters and 675 billion total parameters, released under the Apache 2.0 license.

In March 2026, they launched Mistral Small 4. Mistral Small 4 is a single model that combines four capabilities that previously required separate models: instruction following, deep reasoning, image understanding, and coding.

### Specialized Models

French AI company Mistral released a new open source text-to-speech model on Thursday that can be used by voice AI assistants or in enterprise use cases like customer support.

Released March 16, 2026, Leanstral is the first open-source AI agent designed specifically for Lean 4 formal proof engineering.

Announced March 17, 2026 at NVIDIA GTC, Forge is Mistral's enterprise play — a platform that lets companies build frontier-grade AI models trained on their own proprietary data.

### Later 2026 Releases

Mistral AI dropped Mistral Medium 3.5 on April 29. The Paris-based lab announced a dense 128-billion-parameter model, a set of agentic features—and walked straight into a wall of online "meh" reactions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df787ece-a8da-4e29-b97f-eeb608b46cb0",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "27b30781-a83c-4abd-95df-127dc5487b71",
  "sourceToolAssistantUUID": "df787ece-a8da-4e29-b97f-eeb608b46cb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T05:57:33.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015MnEr38UmWQ2AoAnUeD3Wv`</summary>

```json
{
  "query": "NNsight mechanistic interpretability Llama 3 Qwen activation steering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27b30781-a83c-4abd-95df-127dc5487b71",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jWsp8wYEe8gpTJvzhc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8edd68cf-d0fa-46cb-9970-172b08de5d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFWQo9LdkzzLxG1k42Lfze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5028,
      "cache_read_input_tokens": 12592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5028,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 24 · 2026-05-16T05:57:33.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015XZW3kWDoWvxhSajom4jjz`</summary>

```json
{
  "query": "Gemma 3 model sizes open weights interpretability research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8edd68cf-d0fa-46cb-9970-172b08de5d2a",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jWsp8wYEe8gpTJvzhc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51eb91de-7c65-42b4-941d-383c7e01760f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFWQo9LdkzzLxG1k42Lfze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1018,
      "cache_creation_input_tokens": 5028,
      "cache_read_input_tokens": 12592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5028,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 25 · 2026-05-16T05:57:40.560Z_

<details><summary>↩ Tool result · `toolu_015XZW3kWDoWvxhSajom4jjz`</summary>

```text
Web search results for query: "Gemma 3 model sizes open weights interpretability research"

Links: [{"title":"Gemma Scope 2: Helping the AI Safety Community Deepen Understanding of Complex Language Model Behavior — Google DeepMind","url":"https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/"},{"title":"Gemma: Open Models Based on Gemini Research and Technology","url":"https://arxiv.org/html/2403.08295v4"},{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"Google Releases Gemma 3 Vision-Language Models with Open Weights","url":"https://www.deeplearning.ai/the-batch/google-releases-gemma-3-vision-language-models-with-open-weights/"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Gemma 3: What You Need To Know - Gradient Flow","url":"https://gradientflow.com/gemma-3-what-you-need-to-know/"},{"title":"Introducing Gemma 3: The Developer Guide - Google Developers Blog","url":"https://developers.googleblog.com/en/introducing-gemma3/"},{"title":"Gemma: Google introduces new state-of-the-art open models","url":"https://blog.google/technology/developers/gemma-open-models/"},{"title":"Gemma 3, OLMo 2 32B, and the growing potential of open-source AI","url":"https://www.interconnects.ai/p/gemma-3-olmo-2-32b-and-the-growing"},{"title":"google/gemma-3-270m · Hugging Face","url":"https://huggingface.co/google/gemma-3-270m"}]

Based on the search results, here's what I found about Gemma 3 model sizes, open weights, and interpretability research:

## Model Sizes

Gemma 3 is a multimodal addition to the Gemma family of lightweight open models, ranging in scale from 1 to 27 billion parameters. More specifically, it comes in four sizes: 1 billion, 4 billion, 12 billion, and 27 billion parameters with base (pre-trained) and instruction-tuned versions.

## Open Weights

Gemma 3's model weights are openly released, allowing developers to download, deploy, and fine-tune the models on their own infrastructure. Weights are free to download from Hugging Face and Kaggle under a license that allows noncommercial and commercial uses with some restrictions.

## Interpretability Research

Google released Gemma Scope 2: a comprehensive, open suite of interpretability tools for all Gemma 3 model sizes, from 270M to 27B parameters. This is the largest ever open-source release of interpretability tools by an AI lab to date.

By combining sparse autoencoders (SAEs) and transcoders, it allows researchers to look inside models, see what they're thinking about, and how these thoughts are formed and connect to the model's behavior. This enables the richer study of jailbreaks or other AI behaviors relevant to safety, like discrepancies between a model's communicated reasoning and its internal state.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51eb91de-7c65-42b4-941d-383c7e01760f",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "50c4b37b-7e0f-4d5b-a398-ac81ed915f44",
  "sourceToolAssistantUUID": "51eb91de-7c65-42b4-941d-383c7e01760f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T05:57:41.932Z_

<details><summary>↩ Tool result · `toolu_015MnEr38UmWQ2AoAnUeD3Wv`</summary>

```text
Web search results for query: "NNsight mechanistic interpretability Llama 3 Qwen activation steering 2026"

Links: [{"title":"nnsight and nnterp | Learn Mechanistic Interpretability","url":"https://learnmechinterp.com/topics/nnsight-and-nnterp/"},{"title":"A Standardized Interface for Mechanistic Interpretability of ...","url":"https://openreview.net/pdf?id=ACic3VDIHp"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907"},{"title":"Steering Awareness: Models Can Be Trained to Detect Activation Steering","url":"https://arxiv.org/html/2511.21399v2"},{"title":"National Deep Inference Fabric · GitHub","url":"https://github.com/ndif-team"},{"title":"Introspection or confusion?","url":"https://www.lesswrong.com/posts/kfgmHvxcTbav9gnxe/introspection-or-confusion"},{"title":"Bridging Mechanistic Interpretability and Prompt Engineering with Gradient Ascent for Interpretable Persona Control","url":"https://arxiv.org/html/2601.02896v2"},{"title":"This startup’s new mechanistic interpretability tool lets you debug LLMs | MIT Technology Review","url":"https://www.technologyreview.com/2026/04/30/1136721/this-startups-new-mechanistic-interpretability-tool-lets-you-debug-llms/"},{"title":"Qwen-Scope: Open-Source Sparse AutoEncoders for LLM Interpretability and Steering • Dev|Journal","url":"https://earezki.com/ai-news/2026-05-01-qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"}]

Based on the search results, here's what I found about NNsight, mechanistic interpretability, and activation steering related to Llama 3 and Qwen models in 2026:

## NNsight and Mechanistic Interpretability Tools

NNsight is a tool for flexible model inspection and intervention that works directly with HuggingFace models. NNsight generalized the approach to work with any PyTorch model and introduced remote execution for large-scale experiments.

When a new Llama or Qwen variant drops, there is an unavoidable lag before MI researchers can study it with traditional tools. However, nnterp supports over 50 model variants across 16+ architecture families, including GPT-2, GPT-J, Llama (all versions), Mistral, Mixtral (mixture-of-experts), Gemma 2 and 3, Qwen 2 and 3, Phi-3, and more.

## Activation Steering Research in 2026

Recent research has advanced activation steering methods significantly. Prompt Steering Replacement (PSR) models estimate token-specific steering coefficients from the activations themselves and are trained to imitate prompt-based interventions.

Interestingly, detection rates vary substantially across architectures (95% for Qwen 32B vs. 43% for Llama 8B), suggesting that different model families have different susceptibilities to steering interventions.

## Related Tools and Applications

A unified interface for mechanistic interpretability of transformers built on NNsight provides standardized naming conventions across all transformer architectures with built-in interventions like logit lens, patchscope, and activation steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8edd68cf-d0fa-46cb-9970-172b08de5d2a",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "c23241fc-fbe6-4ece-a4c6-9a0f5cf341a3",
  "sourceToolAssistantUUID": "8edd68cf-d0fa-46cb-9970-172b08de5d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T05:57:44.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MsJKWrG8rpWjtvaJhuxDaG`</summary>

```json
{
  "query": "Qwen-Scope sparse autoencoders SAE interpretability steering May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c23241fc-fbe6-4ece-a4c6-9a0f5cf341a3",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jXpZxFbJrApjyzhUUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa9f27ab-b9f2-423f-a09d-eff9f119b6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qtwwFBoM4WTnTFS9KsF1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2113,
      "cache_read_input_tokens": 17620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2113,
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

### Tool call

_source line 28 · 2026-05-16T05:57:45.048Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014YSQp4SNvR37gjY957yyjv`</summary>

```json
{
  "query": "DeepSeek V4 model architecture open weights sizes dense 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa9f27ab-b9f2-423f-a09d-eff9f119b6cc",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jXpZxFbJrApjyzhUUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adb0786a-d0aa-4f70-8955-d3f0daa60173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qtwwFBoM4WTnTFS9KsF1B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 887,
      "cache_creation_input_tokens": 2113,
      "cache_read_input_tokens": 17620,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 887,
          "output_tokens": 121,
          "cache_read_input_tokens": 17620,
          "cache_creation_input_tokens": 2113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2113,
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

_source line 29 · 2026-05-16T05:57:52.718Z_

<details><summary>↩ Tool result · `toolu_01MsJKWrG8rpWjtvaJhuxDaG`</summary>

```text
Web search results for query: "Qwen-Scope sparse autoencoders SAE interpretability steering May 2026"

Links: [{"title":"Qwen AI Releases Qwen-Scope: An Open-Source Sparse AutoEncoders (SAE) Suite That Turns LLM Internal Features into Practical Development Tools - MarkTechPost","url":"https://www.marktechpost.com/2026/05/01/qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"},{"title":"Qwen-Scope: Open-Source Sparse AutoEncoders for LLM Interpretability and Steering • Dev|Journal","url":"https://earezki.com/ai-news/2026-05-01-qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/"},{"title":"Surgical Model Tuning with SAEs: Enhancing Interpretability in Qwen-Scope · Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/05/surgical-model-tuning-saes-qwen-scope-interpretability/"},{"title":"[2605.11887] Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models","url":"https://arxiv.org/abs/2605.11887"},{"title":"Qwen Releases Qwen-Scope Sparse Autoencoder Suite for Qwen Models","url":"https://www.therift.ai/news-feed/qwen-releases-qwen-scope-sparse-autoencoder-suite-for-qwen-models"},{"title":"Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models","url":"https://arxiv.org/html/2605.11887"},{"title":"Aihola","url":"https://aihola.com/article/alibaba-qwen-scope-release"},{"title":"Pairwise matrices for sparse autoencoders: single-feature inspection mislabels causal axes","url":"https://arxiv.org/html/2605.03160v1"},{"title":"Qwen/SAE-Res-Qwen3-30B-A3B-Base-W128K-L0_100 · Hugging Face","url":"https://huggingface.co/Qwen/SAE-Res-Qwen3-30B-A3B-Base-W128K-L0_100"},{"title":"Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models - programming.dev","url":"https://programming.dev/post/49644849"}]

Here's what I found about Qwen-Scope sparse autoencoders for SAE interpretability and steering:

## Overview

Qwen Team released Qwen-Scope, an open-source suite of sparse autoencoders (SAEs) trained on the Qwen3 and Qwen3.5 model families. The release comprises 14 groups of SAE weights across 7 model variants — five dense models (Qwen3-1.7B, Qwen3-8B, Qwen3.5-2B, Qwen3.5-9B, and Qwen3.5-27B) and two mixture-of-experts (MoE) models (Qwen3-30B-A3B and Qwen3.5-35B-A3B).

## How SAEs Work

A sparse autoencoder serves as a translation layer between raw neural network activations and human-understandable concepts. When an LLM processes text, it produces high-dimensional hidden states that are difficult to interpret directly. An SAE learns to decompose these activations into a large dictionary of sparse latent features, where each input activates only a small subset of features.

## Steering Applications

The most immediate application is steering — influencing model output without modifying any model weights. The idea rests on a well-supported hypothesis: high-level behaviors are encoded as directions in the model's internal representation space. By adding or subtracting a feature direction from the residual stream at inference time using the formula h' ← h + αd, where h is the hidden state, d is the SAE feature direction, and α controls strength, engineers can push the model toward or away from specific behaviors.

## Practical Use Cases

The research demonstrates multiple applications: SAE feature steering addresses endless repetition by synthetically generating one repetition-biased rollout per training group, which is then incorporated as a rare negative sample in the DAPO RL pipeline. Additionally, suppressing a specific Chinese language feature stopped the model from randomly mixing languages during an English prompt, and a classical literary style transfer can be triggered by turning on the right feature direction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa9f27ab-b9f2-423f-a09d-eff9f119b6cc",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "a5929f96-bc7c-43c2-bd80-668b0cf8a289",
  "sourceToolAssistantUUID": "aa9f27ab-b9f2-423f-a09d-eff9f119b6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T05:57:58.441Z_

<details><summary>↩ Tool result · `toolu_014YSQp4SNvR37gjY957yyjv`</summary>

```text
Web search results for query: "DeepSeek V4 model architecture open weights sizes dense 2026"

Links: [{"title":"DeepSeek is back among the leading open weights models with V4 Pro and V4 Flash","url":"https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash"},{"title":"DeepSeek V4 Ships 1M Context, Open-Weights","url":"https://winbuzzer.com/2026/04/27/deepseek-v4-open-weights-launch-xcxwbn/"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"DeepSeek V4's 1-Trillion Parameter Architecture Targets | Introl Blog","url":"https://introl.com/blog/deepseek-v4-trillion-parameter-coding-model-february-2026"},{"title":"DeepSeek V4: Features, Benchmarks & API Pricing (2026)","url":"https://codersera.com/blog/deepseek-v4-release-date-features-benchmarks/"},{"title":"What Is DeepSeek V4? Open-Weight AI at Frontier-Level Performance | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-deepseek-v4"},{"title":"DeepSeek V4: Features, Benchmarks, and Comparisons | DataCamp","url":"https://www.datacamp.com/blog/deepseek-v4"},{"title":"DeepSeek V4 Launch: 4 Specs That Make It the Most Disruptive Open-Weight Model of 2026 | MindStudio","url":"https://www.mindstudio.ai/blog/deepseek-v4-launch-specs-open-weight-2026"},{"title":"DeepSeek V4: The Open-Source Model Closing the Gap on Frontier AI | MindStudio","url":"https://www.mindstudio.ai/blog/deepseek-v4-open-source-frontier-model"},{"title":"DeepSeek V4: The Open-Source Model That Rivals Closed Frontier Models | MindStudio","url":"https://www.mindstudio.ai/blog/deepseek-v4-open-source-frontier-model-review"}]

Based on the search results, here's a comprehensive overview of DeepSeek V4's model architecture, open-weight availability, and sizes:

## Model Variants and Sizes

DeepSeek V4 introduces a new architecture with V4 Pro at 1.6T total / 49B active parameters and V4 Flash at 284B total / 13B active parameters, and is DeepSeek's first two-tier lineup, with Pro positioned for maximum capability and Flash for faster, lower-cost inference.

## Architecture Overview

V4 is the first new architecture from DeepSeek since V3. DeepSeek-V4 series include two strong Mixture-of-Experts (MoE) language models with several key architectural innovations:

**Hybrid Attention Design:** It stacks Compressed Sparse Attention, DeepSeek Sparse Attention, and Heavily Compressed Attention. According to DeepSeek, the design targets a 73% cut in per-token inference FLOPs and a 90% reduction in KV cache memory burden versus V3.2.

**Additional Components:** The models incorporate a hybrid attention mechanism combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) to dramatically improve long-context efficiency, and incorporate Manifold-Constrained Hyper-Connections (mHC) to strengthen conventional residual connections.

## Open-Weights Release

DeepSeek shipped V4-Pro and V4-Flash preview models on April 24, 2026 under an MIT license. Both ship a 1-million-token context window with up to 384,000 tokens of output, under MIT-licensed open weights hosted on Hugging Face.

## Context Window and Efficiency

In the 1M-token context setting, DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adb0786a-d0aa-4f70-8955-d3f0daa60173",
  "isSidechain": true,
  "promptId": "bbb82476-e0c9-47df-83bc-6b4c571f84cb",
  "agentId": "a3443a00d7c4e919d",
  "type": "user",
  "uuid": "6cb11ab0-40a8-4e39-9dce-7fb6d1d39463",
  "sourceToolAssistantUUID": "adb0786a-d0aa-4f70-8955-d3f0daa60173",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-16T05:58:52.226Z_

Here is a comprehensive report on the current best open-source LLMs as of May 2026, focused on suitability for mechanistic interpretability and activation steering research.

---

## Top Open-Source LLMs (May 2026) for Mechanistic Interpretability Research

### Tier 1: Best Suited for Interpretability/Activation Steering (7B-70B range)

#### 1. Qwen3 Family (Alibaba) -- Released April-May 2025, Qwen3.5 in Feb 2026
- **Sizes:** Dense: 0.6B, 1.7B, 4B, 8B, 14B, 32B; MoE: 30B-A3B, 235B-A22B
- **License:** Apache 2.0
- **Interpretability support:** EXCELLENT. Qwen-Scope (released May 1, 2026) provides a full open-source SAE suite trained on Qwen3 and Qwen3.5 models (14 groups of SAE weights across 7 model variants). Directly supports activation steering via feature directions in the residual stream. TransformerLens supports Qwen3-0.6B through Qwen3-14B. NNsight/nnterp supports all Qwen 2 and 3 variants.
- **Best picks for your research:** Qwen3-8B, Qwen3-14B, Qwen3-32B (dense models, ideal for layer-by-layer extraction)

#### 2. Gemma 3 Family (Google) -- Released March 2025
- **Sizes:** 1B, 4B, 12B, 27B (also a 270M variant)
- **License:** Gemma license (commercial + non-commercial with some restrictions)
- **Interpretability support:** EXCELLENT. Google released Gemma Scope 2 -- the largest ever open-source release of interpretability tools by an AI lab, covering all Gemma 3 sizes from 270M to 27B. Includes both SAEs and transcoders. TransformerLens explicitly supports Gemma 2 and 3 models (gemma-2-2b through gemma-2-27b, plus Gemma 3). NNsight/nnterp also supports all Gemma variants.
- **Best picks for your research:** Gemma 3 12B, Gemma 3 27B

#### 3. Llama 4 Scout (Meta) -- Released April 2025
- **Sizes:** 109B total / 17B active (MoE, 16 experts); Maverick: ~2T total / 288B active
- **License:** Llama 4 Community License
- **Interpretability support:** GOOD. TransformerLens supports Llama architectures (originally Llama 1/2/3, with ongoing expansion). NNsight/nnterp supports all Llama versions. However, the MoE architecture adds complexity for layer-by-layer analysis compared to dense models. Note: Meta released "Muse Spark" in April 2026 as a successor line.
- **Best picks for your research:** Llama 4 Scout (17B active params) or older Llama 3.1 8B/70B (dense, well-supported)

---

### Tier 2: Strong Models, Good but Less Direct Interpretability Tool Support

#### 4. Mistral Models -- Various 2025-2026 releases
- **Key models in range:** Mistral Small 4 (March 2026), Mistral Large 3 (675B total / 41B active MoE, Apache 2.0), Mistral Medium 3.5 (128B dense, April 2026)
- **License:** Apache 2.0 for many models
- **Interpretability support:** MODERATE. NNsight/nnterp supports Mistral and Mixtral architectures. TransformerLens has some Mistral support. No official SAE suite released by Mistral.
- **Best picks for your research:** Devstral (for code-focused steering research), Mistral Small 4

#### 5. DeepSeek-R1 and DeepSeek-V4 -- R1: Jan 2025; V4: April 2026
- **Sizes:** R1: 671B MoE; V4-Pro: 1.6T/49B active; V4-Flash: 284B/13B active
- **License:** MIT
- **Interpretability support:** MODERATE. Novel hybrid attention architecture (CSA + HCA) in V4 may require custom hooks. NNsight should work since it supports any PyTorch model. However, the MoE + novel attention design makes clean layer-by-layer analysis more complex. No official SAE suite.
- **Note:** DeepSeek-R1 distilled versions (1.5B, 7B, 8B, 14B, 32B, 70B) based on Qwen2.5 and Llama architectures are much more interpretability-friendly.
- **Best picks for your research:** DeepSeek-R1 distilled variants (7B, 14B, 32B -- these use standard Qwen/Llama architectures)

---

### Tier 3: Frontier-Class but Less Suitable for Interpretability at Scale

#### 6. GLM 5.1 (Zhipu AI) -- 2026
- **Size:** 744B total / 40B active (MoE)
- Currently the leading open-weights model on Artificial Analysis Intelligence Index, but no known interpretability tool suite.

#### 7. Kimi K2.6 Thinking (Moonshot AI) -- May 2026
- Leads open-source coding benchmarks but limited interpretability tooling.

---

### Interpretability Tools Landscape (May 2026)

| Tool | Models Supported | Key Feature |
|------|-----------------|-------------|
| **TransformerLens** | ~9,000 models via TransformerBridge (GPT-2, Llama, Qwen3, Gemma 3, Mistral, etc.) | HookPoints on every activation; gold standard for mech interp |
| **NNsight** | Any PyTorch model (HuggingFace native) | Remote execution for large models; flexible interventions |
| **nnterp** | 50+ variants across 16 architecture families | Standardized interface; write once, deploy across architectures |
| **Gemma Scope 2** | All Gemma 3 sizes (270M-27B) | Pre-trained SAEs + transcoders from Google |
| **Qwen-Scope** | Qwen3 + Qwen3.5 (7 model variants) | Pre-trained SAEs; direct steering applications demonstrated |

---

### Recommendations for Your Research

**For activation steering specifically:**
1. **Qwen3-8B or Qwen3-14B** -- Best choice. Apache 2.0, dense architecture, Qwen-Scope provides pre-trained SAEs with demonstrated steering applications (language switching, style transfer, repetition suppression). TransformerLens compatible.

2. **Gemma 3 12B or 27B** -- Excellent second choice. Gemma Scope 2 provides the most comprehensive interpretability toolkit from any lab. TransformerLens compatible.

3. **Qwen3-32B** -- If you need a larger model. Note that activation steering detection rates vary by architecture (95% for Qwen 32B vs 43% for Llama 8B in recent research), which is itself an interesting research finding.

4. **DeepSeek-R1 distilled 14B/32B** -- Good for studying reasoning-focused steering, uses standard Qwen2.5 architecture so all tools work.

5. **Llama 3.1 70B** -- If you need the largest dense model with mature tool support. Still widely used in the interpretability community despite being older.

---

Sources:
- [The Best Open-Source LLMs in 2026 (BentoML)](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)
- [Best Open Source LLM Leaderboard 2026 (Onyx)](https://onyx.app/open-llm-leaderboard)
- [Open Source LLM Leaderboard 2026 (Vellum)](https://www.vellum.ai/open-llm-leaderboard)
- [LLM Benchmark Leaderboard 2026 (CodeSOTA)](https://www.codesota.com/llm)
- [TransformerLens GitHub](https://github.com/TransformerLensOrg/TransformerLens)
- [TransformerLens Model Properties Table](https://transformerlensorg.github.io/TransformerLens/generated/model_properties_table.html)
- [nnterp: A Standardized Interface for Mechanistic Interpretability (OpenReview)](https://openreview.net/forum?id=ACic3VDIHp)
- [Qwen-Scope: Open-Source SAE Suite (MarkTechPost)](https://www.marktechpost.com/2026/05/01/qwen-ai-releases-qwen-scope-an-open-source-sparse-autoencoders-sae-suite-that-turns-llm-internal-features-into-practical-development-tools/)
- [Qwen-Scope Paper (arXiv)](https://arxiv.org/abs/2605.11887)
- [Gemma Scope 2 (Google DeepMind)](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/)
- [Qwen3 GitHub](https://github.com/QwenLM/qwen3)
- [Llama 4 Announcement (Meta)](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [DeepSeek V4 Open Weights Launch](https://winbuzzer.com/2026/04/27/deepseek-v4-open-weights-launch-xcxwbn/)
- [Mistral AI Models 2026 Guide](https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide)
- [NNsight and nnterp - Learn Mechanistic Interpretability](https://learnmechinterp.com/topics/nnsight-and-nnterp/)
- [Steer Like the LLM: Activation Steering (arXiv, May 2026)](https://arxiv.org/html/2605.03907)
- [Steering Awareness: Models Trained to Detect Activation Steering](https://arxiv.org/html/2511.21399v2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cb11ab0-40a8-4e39-9dce-7fb6d1d39463",
  "isSidechain": true,
  "agentId": "a3443a00d7c4e919d",
  "requestId": "req_011Cb5jZ3FieEvbz45ejdLXo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf20bed3-e78d-4694-a245-54562a9b531d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e9ad89c8-7d70-432b-bf1f-58e2870fd5c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHF6RDNw1BvvqSzs7UqWBA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3333,
      "cache_read_input_tokens": 19733,
      "output_tokens": 2670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2670,
          "cache_read_input_tokens": 19733,
          "cache_creation_input_tokens": 3333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3333,
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
