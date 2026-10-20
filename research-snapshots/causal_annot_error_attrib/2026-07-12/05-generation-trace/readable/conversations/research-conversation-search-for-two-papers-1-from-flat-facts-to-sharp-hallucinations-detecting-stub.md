# Research conversation: Search for two papers: 1. "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a75f44fe748c1c1cf.jsonl`
- **Structured JSON:** [`b1b9269c8ff5dd16ea21.json`](../../sessions/b1/b1b9269c8ff5dd16ea21.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-16T10:13:25.294Z_

Search for two papers:

1. "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" (EPGS), claimed to be at ICML 2026, arxiv 2605.00939. Search for:
- "arxiv 2605.00939"
- "EPGS gradient sensitivity hallucination ICML 2026"
- "stubborn hallucinations gradient sharpness"

2. "Calibrating LLM Confidence by Probing Perturbed Representation Stability" (CCPS) by Khanmohammadi et al., claimed EMNLP 2025 main, arxiv 2505.21772. Search for:
- "arxiv 2505.21772"
- "CCPS perturbed representation stability confidence calibration"
- "Khanmohammadi confidence calibration perturbation LLM"

For each paper, verify:
- Does it exist?
- Are the venue claims correct?
- What does it actually propose?

Use WebSearch and if possible WebFetch on the arxiv URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "ff1cf7c8-e4f1-4656-b8d8-2e21a846e777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T10:13:25.296Z_

```json
{
  "parentUuid": "ff1cf7c8-e4f1-4656-b8d8-2e21a846e777",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
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
  "uuid": "a056a781-721d-4890-b1c0-5c62a3122e16",
  "timestamp": "2026-05-16T10:13:25.296Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T10:13:28.298Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0125XiU8UAryt39q1FqkadWe`</summary>

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
  "parentUuid": "a056a781-721d-4890-b1c0-5c62a3122e16",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb652r7jz7SyA4jhNjd3S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e6ed2f8-98de-4e59-927b-933d6eeaa551",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015PYVBR2jFekzxrbYFvTMVn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 807,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 4 · 2026-05-16T10:13:28.303Z_

<details><summary>↩ Tool result · `toolu_0125XiU8UAryt39q1FqkadWe`</summary>

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
  "parentUuid": "5e6ed2f8-98de-4e59-927b-933d6eeaa551",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "e9d0e868-79ba-48b5-89af-d1d86fffa6f0",
  "sourceToolAssistantUUID": "5e6ed2f8-98de-4e59-927b-933d6eeaa551",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T10:13:30.887Z_

Now let me search for both papers using multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9d0e868-79ba-48b5-89af-d1d86fffa6f0",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb6536BKwAiT1WBjqdazb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a4d3429-1740-4226-b8cc-7c21f8ae0259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HAAxAzqTtnrR7yKEST1Tk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 6 · 2026-05-16T10:13:31.361Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017E6gKefUR1niLXghxdAKEv`</summary>

```json
{
  "query": "arxiv 2605.00939"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a4d3429-1740-4226-b8cc-7c21f8ae0259",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb6536BKwAiT1WBjqdazb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9251857-1108-4e74-87b9-9c205b8ec31b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HAAxAzqTtnrR7yKEST1Tk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 7 · 2026-05-16T10:13:31.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TcWh2TWAwppZpe7Eor7ySk`</summary>

```json
{
  "query": "EPGS gradient sensitivity hallucination ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9251857-1108-4e74-87b9-9c205b8ec31b",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb6536BKwAiT1WBjqdazb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68d0d87d-dc92-48d7-b24e-75b65410fb49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HAAxAzqTtnrR7yKEST1Tk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 8 · 2026-05-16T10:13:32.371Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B9ujky3ZZ5XvVAfTxQCjLT`</summary>

```json
{
  "query": "stubborn hallucinations gradient sharpness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68d0d87d-dc92-48d7-b24e-75b65410fb49",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb6536BKwAiT1WBjqdazb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a96a267-379d-4c7b-958c-f89c5d021b02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HAAxAzqTtnrR7yKEST1Tk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 9 · 2026-05-16T10:13:32.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015stfCoMXKA7HxnW5qGpvKT`</summary>

```json
{
  "query": "arxiv 2505.21772"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a96a267-379d-4c7b-958c-f89c5d021b02",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb6536BKwAiT1WBjqdazb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34bef3d5-ff16-4f70-9d92-12507faa5f85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HAAxAzqTtnrR7yKEST1Tk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 10 · 2026-05-16T10:13:32.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017JqN9pjKEPo7DBQzkuXghL`</summary>

```json
{
  "query": "CCPS perturbed representation stability confidence calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34bef3d5-ff16-4f70-9d92-12507faa5f85",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb6536BKwAiT1WBjqdazb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b40729e-03e8-47ea-a379-c9875f776a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HAAxAzqTtnrR7yKEST1Tk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 11 · 2026-05-16T10:13:33.178Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YGkEmEhD2W8ZisTQNeip8U`</summary>

```json
{
  "query": "Khanmohammadi confidence calibration perturbation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b40729e-03e8-47ea-a379-c9875f776a24",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb6536BKwAiT1WBjqdazb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a22a8958-94cf-4cd2-b758-913da239d9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HAAxAzqTtnrR7yKEST1Tk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9030,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 299,
          "cache_read_input_tokens": 9030,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 12 · 2026-05-16T10:13:35.742Z_

<details><summary>↩ Tool result · `toolu_017E6gKefUR1niLXghxdAKEv`</summary>

```text
Web search results for query: "arxiv 2605.00939"

Links: [{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"WikiVideo: Article Generation from Multiple Videos","url":"https://arxiv.org/html/2504.00939"},{"title":"1 Abstract—Recently, the use of deflecting covering meta-domes","url":"https://arxiv.org/pdf/2202.00939"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2509.00939"},{"title":"[1701.00939] 1 Introduction","url":"https://ar5iv.labs.arxiv.org/html/1701.00939"},{"title":"ShadowGS: Shadow-Aware 3D Gaussian Splatting for Satellite Imagery","url":"https://arxiv.org/html/2601.00939"},{"title":"G3DR: Generative 3D Reconstruction in ImageNet","url":"https://arxiv.org/html/2403.00939"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1259&show=1000"},{"title":"Deep learning bulk spacetime from boundary optical conductivity","url":"https://arxiv.org/html/2401.00939"}]

The arxiv paper 2605.00939 is titled "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity".

The paper addresses how traditional hallucination detection fails on "Stubborn Hallucinations" -- errors where LLMs are confidently wrong. The authors propose a geometric solution called Embedding-Perturbed Gradient Sensitivity (EPGS).

Their hypothesis is that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization. EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. Their experiments show that EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9251857-1108-4e74-87b9-9c205b8ec31b",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "d1616fa7-036d-4d2f-a3b4-2e319af87c93",
  "sourceToolAssistantUUID": "d9251857-1108-4e74-87b9-9c205b8ec31b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T10:13:37.489Z_

<details><summary>↩ Tool result · `toolu_01TcWh2TWAwppZpe7Eor7ySk`</summary>

```text
Web search results for query: "EPGS gradient sensitivity hallucination ICML 2026"

Links: [{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"Miranda Muqing Miao","url":"https://mmiao2.github.io/"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"2026 Conference","url":"https://icml.cc/"},{"title":"SENSITIVITY-GUIDED HALLUCINATION DETECTION IN ...","url":"https://openreview.net/pdf/66488d1ef8a4e92ad8ef067d06d95fd1ba248fd9.pdf"},{"title":"GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers","url":"https://gptzero.me/news/neurips/"},{"title":"ICML Poster Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance","url":"https://icml.cc/virtual/2025/poster/43644"},{"title":"AI Hallucination Rates & Benchmarks in 2026","url":"https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/"}]

Based on the search results, I found information about EPGS and gradient sensitivity for hallucination detection:

## EPGS (Embedding-Perturbed Gradient Sensitivity)

EPGS (Embedding-Perturbed Gradient Sensitivity) is a proposed geometric solution to detect hallucinations in language models. 

The approach is based on the hypothesis that robust facts reside in flat minima while stubborn hallucinations sit in sharp minima. EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. This acts as an efficient proxy for the Hessian spectrum, differentiating stable knowledge from unstable memorization.

Traditional hallucination detection fails on "Stubborn Hallucinations"—errors where LLMs are confidently wrong. EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.

The work appears to be recent research (posted to arXiv in May 2026), though the search results don't specifically confirm whether it was accepted to ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68d0d87d-dc92-48d7-b24e-75b65410fb49",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "c4258fbd-ce45-4731-bb21-e2867458c47c",
  "sourceToolAssistantUUID": "68d0d87d-dc92-48d7-b24e-75b65410fb49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T10:13:39.011Z_

<details><summary>↩ Tool result · `toolu_01B9ujky3ZZ5XvVAfTxQCjLT`</summary>

```text
Web search results for query: "stubborn hallucinations gradient sharpness"

Links: [{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"The Geometry of Hallucination. Gradient Conflict and the Topographic… | by Micheal Bee | Feb, 2026 | Medium","url":"https://medium.com/@mbonsign/the-geometry-of-hallucination-f725f41f7050"},{"title":"[2403.01548] In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation","url":"https://arxiv.org/abs/2403.01548"},{"title":"Hallucinogen persisting perception disorder - Wikipedia","url":"https://en.wikipedia.org/wiki/Hallucinogen_persisting_perception_disorder"},{"title":"Mitigating Multimodal Hallucinations via Gradient-based Self-Reflection | OpenReview","url":"https://openreview.net/forum?id=zgXGNXkC0F"},{"title":"Visual Hallucinations: Differential Diagnosis and Treatment","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC2660156/"},{"title":"Cues to body-related distortions and hallucinations? Spontaneous sensations correlate with EEG oscillatory activity recorded at rest in the somatosensory cortices - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925492722000671"},{"title":"[2601.16527] Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs","url":"https://arxiv.org/abs/2601.16527"},{"title":"Abnormal cortical topographic patterns associated with auditory verbal hallucination in first-episode schizophrenia | Translational Psychiatry","url":"https://www.nature.com/articles/s41398-025-03748-y"}]

Based on the search results, here's what I found about stubborn hallucinations and gradient sharpness:

## Key Research Findings

Recent research has established a geometric relationship between hallucinations in AI models and the sharpness of the loss landscape:

Robust facts reside in flat minima, while stubborn hallucinations sit in sharp minima, supported by brittle memorization.

### Detection Method

A method called EPGS (Embedding-Perturbed Gradient Sensitivity) detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. Rather than computing the prohibitively expensive Hessian, this method injects Gaussian noise into the input embedding space to actively probe the stability of the optimization landscape, with input sensitivity serving as a computationally efficient proxy for the Hessian spectrum, effectively measuring the "sharpness" of the model's belief.

### Why This Matters

Even a minor perturbation in a sharp basin induces a dramatic spike in the gradient magnitude, whereas a flat basin remains stable. This distinction helps explain Stubborn Hallucinations, which sit in sharp minima, as opposed to Transient Hallucinations in unstable regions.

Recent work also explores how standard erasure achieves only superficial suppression, trapping the model in sharp minima where hallucinations catastrophically resurge after lightweight relearning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a96a267-379d-4c7b-958c-f89c5d021b02",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "322ca934-cca7-4656-bc4f-2a42adb60a03",
  "sourceToolAssistantUUID": "9a96a267-379d-4c7b-958c-f89c5d021b02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T10:13:39.527Z_

<details><summary>↩ Tool result · `toolu_015stfCoMXKA7HxnW5qGpvKT`</summary>

```text
Web search results for query: "arxiv 2505.21772"

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1625&show=250"},{"title":"Towards Safety Reasoning in LLMs: AI-agentic Deliberation for Policy-embedded CoT Data Creation","url":"https://arxiv.org/html/2505.21784v1"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=4025&show=25"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=10875&show=50"},{"title":"Physics","url":"https://arxiv.org/list/physics/recent?skip=93&show=1000"},{"title":"SGM: A Framework for Building Specification-Guided Moderation Filters","url":"https://arxiv.org/html/2505.19766v1"},{"title":"Quantum Physics May 2025","url":"https://arxiv.org/list/quant-ph/2025-05?skip=75&show=1000"},{"title":"Computer Vision and Pattern Recognition May 2025","url":"https://arxiv.org/list/cs.CV/2025-05?skip=1950&show=2000"}]

Based on the search results, here's what I found about arxiv paper 2505.21772:

**Title:** Calibrating LLM Confidence by Probing Perturbed Representation Stability

**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, Mohammad M. Ghassemi

**Overview:** The paper introduces CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability), a novel method analyzing internal representational stability in LLMs. CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness.

**Evaluation:** CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.

**Results:** CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points.

The paper can be accessed directly at: https://arxiv.org/abs/2505.21772


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34bef3d5-ff16-4f70-9d92-12507faa5f85",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "d3104862-13b9-4553-93b7-f0459053c983",
  "sourceToolAssistantUUID": "34bef3d5-ff16-4f70-9d92-12507faa5f85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T10:13:39.922Z_

<details><summary>↩ Tool result · `toolu_017JqN9pjKEPo7DBQzkuXghL`</summary>

```text
Web search results for query: "CCPS perturbed representation stability confidence calibration"

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250521772K/abstract"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | alphaXiv","url":"https://www.alphaxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"[Literature Review] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.themoonlight.io/en/review/calibrating-llm-confidence-by-probing-perturbed-representation-stability"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=LLM+distribution+confidence"}]

Based on the search results, here's what I found about CCPS:

## Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs.

## Methodology

CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness.

## Key Characteristics

CCPS operates on frozen base LLMs, applying targeted adversarial perturbations to the final hidden states that generate an answer's tokens. From the LLM's response to these perturbations, features are extracted and a lightweight classifier is trained to predict answer correctness. This model-agnostic probing offers an efficient confidence proxy without modifying the base LLM.

## Evaluation and Results

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, among other improvements.

## Publication

The work was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, in Suzhou, China.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b40729e-03e8-47ea-a379-c9875f776a24",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "7521a2bc-90a3-4962-b33b-8d28c5b553fb",
  "sourceToolAssistantUUID": "2b40729e-03e8-47ea-a379-c9875f776a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T10:13:40.951Z_

<details><summary>↩ Tool result · `toolu_01YGkEmEhD2W8ZisTQNeip8U`</summary>

```text
Web search results for query: "Khanmohammadi confidence calibration perturbation LLM"

Links: [{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/calibrating-llm-confidence-by-probing-perturbed-representation"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250521772K/abstract"},{"title":"dblp: Kundan Thind","url":"https://dblp.org/pid/359/8694.html"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Confidence-Guided Probing Methods","url":"https://www.emergentmind.com/topics/confidence-guided-probing-method"}]

Based on the search results, here's what I found about the Khanmohammadi research on confidence calibration and perturbation in LLMs:

## CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability

The research introduces CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability), a novel method analyzing internal representational stability in LLMs.

### How It Works

CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness. The core intuition is that if the model's internal workings remain stable despite these small changes, it suggests the model is truly confident in its answer.

### Evaluation Results

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats. The results were substantial: CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points.

### Key Features

This model-agnostic probing offers an efficient confidence proxy without modifying the base LLM. The paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing in Suzhou, China.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a22a8958-94cf-4cd2-b758-913da239d9c3",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "749cbe35-2ce0-4d96-ab38-3e5b57a11d91",
  "sourceToolAssistantUUID": "a22a8958-94cf-4cd2-b758-913da239d9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-16T10:13:44.462Z_

Now let me fetch the arxiv pages directly for more details on both papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "749cbe35-2ce0-4d96-ab38-3e5b57a11d91",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb653zxaPkZDdBWBDDaWm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "709cd867-0580-4e4d-a7bd-9fd3ac158a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjHgnfJxPhkz5vM4SdFvTM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5354,
      "cache_read_input_tokens": 10918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5354,
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

_source line 19 · 2026-05-16T10:13:45.886Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PeFAjfDN2682Qa7uU7C2AU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.00939",
  "prompt": "Extract all details: title, authors, abstract, submission date, and any mention of venue/conference (ICML 2026 or otherwise). Is there any indication this paper was accepted to ICML 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "709cd867-0580-4e4d-a7bd-9fd3ac158a64",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb653zxaPkZDdBWBDDaWm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60639f50-6166-4881-a436-32fe971a7c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjHgnfJxPhkz5vM4SdFvTM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5354,
      "cache_read_input_tokens": 10918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5354,
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

_source line 20 · 2026-05-16T10:13:46.889Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011F2iCcZps2FzzEAdLSULUu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.21772",
  "prompt": "Extract all details: title, authors, abstract, submission date, and any mention of venue/conference (EMNLP 2025 or otherwise). Is there any indication this paper was accepted to EMNLP 2025?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60639f50-6166-4881-a436-32fe971a7c3d",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb653zxaPkZDdBWBDDaWm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f501e26-6b9c-417c-979c-08dbb1ba18e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjHgnfJxPhkz5vM4SdFvTM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5354,
      "cache_read_input_tokens": 10918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5354,
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

_source line 21 · 2026-05-16T10:13:48.353Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016ejJqShtkxiWZBztfj3Rg7`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.530/",
  "prompt": "Extract all details about this paper: title, authors, venue, pages, publication details. Confirm this is the CCPS paper at EMNLP 2025 main conference."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f501e26-6b9c-417c-979c-08dbb1ba18e0",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb653zxaPkZDdBWBDDaWm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e14f67d9-2ae4-42c2-8922-d7a98bdaaa94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjHgnfJxPhkz5vM4SdFvTM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5354,
      "cache_read_input_tokens": 10918,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 373,
          "cache_read_input_tokens": 10918,
          "cache_creation_input_tokens": 5354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5354,
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

_source line 22 · 2026-05-16T10:13:50.147Z_

<details><summary>↩ Tool result · `toolu_01PeFAjfDN2682Qa7uU7C2AU`</summary>

```text
# Paper Details Summary

**Title:** "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity"

**Authors:** Yee Zhing Liew, Andrew Huey Ping Tan, Anwar P.P. Abdul Majeed

**Submission Date:** May 1, 2026 (v1); revised May 12, 2026 (v2)

**Abstract:** The researchers propose EPGS (Embedding-Perturbed Gradient Sensitivity) to detect confident errors in language models. Their hypothesis: "robust facts reside in flat minima, [while] stubborn hallucinations sit in sharp minima, supported by brittle memorization." The method perturbs embeddings with noise to measure gradient spikes as a proxy for detecting unstable memorization versus stable knowledge.

**Conference Status:** Yes, accepted. The submission comments explicitly state: "Accepted to ICML 2026. Camera-ready version"

This indicates peer acceptance and preparation of the final manuscript version for the International Conference on Machine Learning 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60639f50-6166-4881-a436-32fe971a7c3d",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "b59abcd7-acb4-4fba-bda9-1821d77cc0a1",
  "sourceToolAssistantUUID": "60639f50-6166-4881-a436-32fe971a7c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T10:13:51.025Z_

<details><summary>↩ Tool result · `toolu_011F2iCcZps2FzzEAdLSULUu`</summary>

```text
# Paper Details Extraction

**Title:** "Calibrating LLM Confidence by Probing Perturbed Representation Stability"

**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese H. Smiley, Kundan Thind, Mohammad M. Ghassemi

**Submission Date:** Originally submitted May 27, 2025; revised version September 18, 2025

**Abstract Summary:** The paper introduces CCPS, a method for improving confidence calibration in Large Language Models by analyzing internal representational stability through adversarial perturbations. Testing across 8B-32B parameter models showed significant improvements: "CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%" compared to prior approaches.

**Venue/Conference Indication:** No mention of EMNLP 2025 or any conference venue appears in the provided content. The paper is posted on arXiv as a preprint with no indication of conference acceptance or submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f501e26-6b9c-417c-979c-08dbb1ba18e0",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "20b70f59-1e83-4754-afd9-56d1fa79a452",
  "sourceToolAssistantUUID": "9f501e26-6b9c-417c-979c-08dbb1ba18e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T10:13:52.478Z_

<details><summary>↩ Tool result · `toolu_016ejJqShtkxiWZBztfj3Rg7`</summary>

```text
# Paper Details: CCPS at EMNLP 2025

**Title:** "Calibrating LLM Confidence by Probing Perturbed Representation Stability"

**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese Smiley, Kundan S Thind, Mohammad M. Ghassemi

**Venue:** EMNLP 2025 (Conference on Empirical Methods in Natural Language Processing)

**Conference Details:**
- Location: Suzhou, China
- Month: November 2025
- Publisher: Association for Computational Linguistics

**Publication Details:**
- Pages: 10448–10514
- Anthology ID: 2025.emnlp-main.530
- DOI: 10.18653/v1/2025.emnlp-main.530

**Confirmation:** Yes, this is confirmed as the CCPS paper at the EMNLP 2025 main conference. The abstract explicitly states: "We introduce CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability)," describing a method that "applies targeted adversarial perturbations to final hidden states" for improved confidence estimation in language models across multiple architectures and benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e14f67d9-2ae4-42c2-8922-d7a98bdaaa94",
  "isSidechain": true,
  "promptId": "30dc5195-c1de-4a4e-b57a-ede33482a077",
  "agentId": "a75f44fe748c1c1cf",
  "type": "user",
  "uuid": "99a90fdb-c7c1-445f-a78f-767d63133a27",
  "sourceToolAssistantUUID": "e14f67d9-2ae4-42c2-8922-d7a98bdaaa94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-16T10:14:11.681Z_

Here are my findings for both papers:

---

## Paper 1: "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity" (EPGS)

**Does it exist?** YES. It is available at [arxiv.org/abs/2605.00939](https://arxiv.org/abs/2605.00939).

**Are the venue claims correct?** YES. The arxiv submission comments explicitly state: "Accepted to ICML 2026. Camera-ready version." The claim of ICML 2026 acceptance is confirmed.

**Authors:** Yee Zhing Liew, Andrew Huey Ping Tan, Anwar P.P. Abdul Majeed

**Submission date:** May 1, 2026 (v1); revised May 12, 2026 (v2)

**What it proposes:** The paper introduces EPGS (Embedding-Perturbed Gradient Sensitivity), a method to detect "stubborn hallucinations" -- high-confidence factual errors in LLMs that evade traditional detection. The core hypothesis is that robust facts reside in flat minima of the loss landscape, while stubborn hallucinations sit in sharp minima supported by brittle memorization. EPGS works by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude, which serves as a computationally efficient proxy for the Hessian spectrum. This distinguishes stable knowledge (flat basins, minimal gradient change) from unstable memorization (sharp basins, dramatic gradient spikes). It outperforms entropy-based and representation-based baselines.

---

## Paper 2: "Calibrating LLM Confidence by Probing Perturbed Representation Stability" (CCPS)

**Does it exist?** YES. It is available at [arxiv.org/abs/2505.21772](https://arxiv.org/abs/2505.21772).

**Are the venue claims correct?** YES. The paper was published at EMNLP 2025 main conference, confirmed by the [ACL Anthology entry](https://aclanthology.org/2025.emnlp-main.530/) (Anthology ID: 2025.emnlp-main.530, pages 10448-10514, Suzhou, China, November 2025). The claim of "EMNLP 2025 main" is accurate.

**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese Smiley, Kundan S Thind, Mohammad M. Ghassemi

**Submission date:** May 27, 2025 (v1); revised September 18, 2025

**What it proposes:** CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a method for improving confidence calibration in LLMs by analyzing internal representational stability. It operates on frozen base LLMs by applying targeted adversarial perturbations to the final hidden states that generate an answer's tokens. From the model's response to these perturbations, features are extracted and a lightweight classifier is trained to predict answer correctness. The intuition: if internal representations remain stable despite perturbations, the model is truly confident. It is model-agnostic and does not modify the base LLM. Results on models from 8B to 32B parameters (Llama, Qwen, Mistral) using MMLU/MMLU-Pro show ~55% reduction in Expected Calibration Error and ~21% reduction in Brier score.

---

## Summary

| Claim | Verified? |
|-------|-----------|
| Paper 1 exists at arxiv 2605.00939 | YES |
| Paper 1 accepted to ICML 2026 | YES (camera-ready version) |
| Paper 2 exists at arxiv 2505.21772 | YES |
| Paper 2 at EMNLP 2025 main | YES (ACL Anthology confirms) |
| Paper 2 by Khanmohammadi et al. | YES (first author: Reza Khanmohammadi) |

Both papers are real, both venue claims are correct, and both propose what was described.

Sources:
- [arxiv 2605.00939 - From Flat Facts to Sharp Hallucinations](https://arxiv.org/abs/2605.00939)
- [arxiv 2605.00939 HTML version](https://arxiv.org/html/2605.00939)
- [arxiv 2505.21772 - Calibrating LLM Confidence by Probing Perturbed Representation Stability](https://arxiv.org/abs/2505.21772)
- [ACL Anthology - EMNLP 2025 Main](https://aclanthology.org/2025.emnlp-main.530/)
- [GitHub - CCPS](https://github.com/ledengary/CCPS)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99a90fdb-c7c1-445f-a78f-767d63133a27",
  "isSidechain": true,
  "agentId": "a75f44fe748c1c1cf",
  "requestId": "req_011Cb654rJi2xx8WxB1GaF35",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f12fab9c-d453-4b57-9ef0-434d165388c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4198163-6777-42f0-a1e4-b5ef18da8454",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wn5VTdau3PKew1CjLxyFs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1281,
      "cache_read_input_tokens": 16272,
      "output_tokens": 1214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1281
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1214,
          "cache_read_input_tokens": 16272,
          "cache_creation_input_tokens": 1281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1281,
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
