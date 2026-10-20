# Research conversation: You are helping me review an ML paper idea. I need you to search for and verify several key papers and claims. Use WebSe

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-afae822db8c4cc166.jsonl`
- **Structured JSON:** [`3a91af22e7793a8b7258.json`](../../sessions/3a/3a91af22e7793a8b7258.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-16T10:00:07.702Z_

You are helping me review an ML paper idea. I need you to search for and verify several key papers and claims. Use WebSearch and WebFetch as needed.

1. Search for "EPGS gradient sensitivity stubborn hallucinations ICML 2026" and "arxiv 2605.00939" - verify this paper exists, its venue, and whether it actually demonstrates that CHOKE/stubborn hallucinations reside in "sharp output minima" detectable via gradient magnitude after embedding perturbation.

2. Search for "SHINE perturbation hallucination detection KL divergence arxiv 2411.09689" - verify this paper exists and what exactly it does. Does it perturb at INPUT layer only, or also intermediate layers? Does it measure output KL divergence?

3. Search for "Shaking to Reveal SSP perturbation hallucination detection Luo 2025 arxiv 2506.02696" - verify this paper exists and what it does. Does it perturb at intermediate layers? Does it require training? Does it measure representation cosine shift vs output logit KL?

4. Search for "HACK hallucination certainty knowledge axes Uehara arxiv 2510.24222" - verify this paper exists and its claims about Certainty Misalignment prevalence (9-43%).

5. Search for "Aletheia cognitive conviction reasoning models arxiv 2601.01532" - verify this paper exists.

For each paper, report: does it exist? What venue? What does it actually do? Any discrepancies with the claims made above?

Use WebFetch to read the actual arxiv abstracts where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "82d58b7b-1159-4cef-827b-ce43fef8e864",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T10:00:07.705Z_

```json
{
  "parentUuid": "82d58b7b-1159-4cef-827b-ce43fef8e864",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
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
  "uuid": "b71d7f46-e731-4788-b75e-86993a427e21",
  "timestamp": "2026-05-16T10:00:07.705Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T10:00:10.476Z_



I'll systematically search for and verify each paper. Let me start by loading the WebSearch and WebFetch tools, then search for all papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b71d7f46-e731-4788-b75e-86993a427e21",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb64244BxSnpjJkWWePjn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57c62e29-1800-41e6-b870-122a2c04823c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4FoTnwpNRf3ytF4mwFoZ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9148,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9148,
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

_source line 4 · 2026-05-16T10:00:10.646Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0185mmKYXy4gqYKQcfxhzh69`</summary>

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
  "parentUuid": "57c62e29-1800-41e6-b870-122a2c04823c",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb64244BxSnpjJkWWePjn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2e9c470-e09d-403e-a653-19ea85803c15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4FoTnwpNRf3ytF4mwFoZ7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9148,
      "cache_read_input_tokens": 0,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9148
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9148,
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

_source line 5 · 2026-05-16T10:00:10.650Z_

<details><summary>↩ Tool result · `toolu_0185mmKYXy4gqYKQcfxhzh69`</summary>

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
  "parentUuid": "f2e9c470-e09d-403e-a653-19ea85803c15",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "e3154a09-7793-428d-aff3-4b77a8394093",
  "sourceToolAssistantUUID": "f2e9c470-e09d-403e-a653-19ea85803c15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T10:00:13.894Z_



Now let me search for all five papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3154a09-7793-428d-aff3-4b77a8394093",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb642H7FqvEcXjScEN6t4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07e16188-f5a5-4d46-83f4-92b05a456e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDcsbfdu85M3Axhv5hf5tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 7 · 2026-05-16T10:00:14.883Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K2ak5CGgFwtLbPu4jM2DCh`</summary>

```json
{
  "query": "EPGS gradient sensitivity stubborn hallucinations ICML 2026 arxiv 2605.00939"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07e16188-f5a5-4d46-83f4-92b05a456e18",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb642H7FqvEcXjScEN6t4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "403d9bef-9874-4461-b5d3-61d6baafc223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDcsbfdu85M3Axhv5hf5tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 8 · 2026-05-16T10:00:15.902Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012297gTtBa5JDqHhNfgd7xJ`</summary>

```json
{
  "query": "SHINE perturbation hallucination detection KL divergence arxiv 2411.09689"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403d9bef-9874-4461-b5d3-61d6baafc223",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb642H7FqvEcXjScEN6t4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e271874c-9b32-4a40-a4b3-e091e31a1fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDcsbfdu85M3Axhv5hf5tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 9 · 2026-05-16T10:00:17.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018oozp79t57gNDQwu8oGuc6`</summary>

```json
{
  "query": "Shaking to Reveal SSP perturbation hallucination detection Luo 2025 arxiv 2506.02696"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e271874c-9b32-4a40-a4b3-e091e31a1fbb",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb642H7FqvEcXjScEN6t4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6be006d0-b81a-4cd3-90ab-abb8da25be28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDcsbfdu85M3Axhv5hf5tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 10 · 2026-05-16T10:00:17.906Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WeQA82yTYLSuRaB5n7bSma`</summary>

```json
{
  "query": "HACK hallucination certainty knowledge axes Uehara arxiv 2510.24222"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6be006d0-b81a-4cd3-90ab-abb8da25be28",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb642H7FqvEcXjScEN6t4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b12b71e-f6d9-4ada-8d15-b1f57599532b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDcsbfdu85M3Axhv5hf5tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 11 · 2026-05-16T10:00:18.879Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019L9g1PKRJD6EY7CeyEGC4z`</summary>

```json
{
  "query": "Aletheia cognitive conviction reasoning models arxiv 2601.01532"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b12b71e-f6d9-4ada-8d15-b1f57599532b",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb642H7FqvEcXjScEN6t4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d3af406-0445-4c29-b989-9f9e91dad86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDcsbfdu85M3Axhv5hf5tb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9148,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1923
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 9148,
          "cache_creation_input_tokens": 1923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1923,
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

_source line 12 · 2026-05-16T10:00:19.842Z_

<details><summary>↩ Tool result · `toolu_01K2ak5CGgFwtLbPu4jM2DCh`</summary>

```text
Web search results for query: "EPGS gradient sensitivity stubborn hallucinations ICML 2026 arxiv 2605.00939"

Links: [{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"Why DDIM Hallucinates More than DDPM: A Theoretical Analysis of Reverse Dynamics","url":"https://arxiv.org/html/2605.06831"},{"title":"[2605.01428] Hallucinations Undermine Trust; Metacognition is a Way Forward","url":"https://arxiv.org/abs/2605.01428"},{"title":"Hallucination Detection and Mitigation in Large Language Models","url":"https://arxiv.org/html/2601.09929v1"},{"title":"[2601.20279] Hallucination Begins Where Saliency Drops","url":"https://arxiv.org/abs/2601.20279"},{"title":"Sensitivity Analysis in the Face of Rare Events","url":"https://arxiv.org/html/2605.09148"},{"title":"Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization","url":"https://arxiv.org/html/2605.04700"},{"title":"GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers","url":"https://gptzero.me/news/neurips/"},{"title":"Last Update: September 29, 2025 Are Hallucinations Bad Estimations? Hude Liu∗1","url":"https://arxiv.org/pdf/2509.21473"}]

I found the paper you're looking for! Here's what the search results show:

The paper proposes Embedding-Perturbed Gradient Sensitivity (EPGS), a method for detecting hallucinations in large language models. The hypothesis is that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization.

EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude, which acts as an efficient proxy for the Hessian spectrum, differentiating stable knowledge from unstable memorization. The experiments show that EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.

The paper, titled "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity," is available on arXiv (2605.00939) and is associated with ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "403d9bef-9874-4461-b5d3-61d6baafc223",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "4c488538-a48a-4ac0-b64f-0c658c9d60d7",
  "sourceToolAssistantUUID": "403d9bef-9874-4461-b5d3-61d6baafc223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T10:00:22.354Z_

<details><summary>↩ Tool result · `toolu_012297gTtBa5JDqHhNfgd7xJ`</summary>

```text
Web search results for query: "SHINE perturbation hallucination detection KL divergence arxiv 2411.09689"

Links: [{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/html/2411.09689"},{"title":"[2411.09689] Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge","url":"https://arxiv.org/abs/2411.09689"},{"title":"Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge — Seongmin Lee","url":"https://seongmin.xyz/papers/llm-hallucination-probing"},{"title":"Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/html/2407.05474v1"},{"title":"LLM Hallucination Reasoning with Zero-shot Knowledge Test","url":"https://arxiv.org/html/2411.09689v1"},{"title":"Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs","url":"https://arxiv.org/html/2505.16894v1"},{"title":"Diverging Towards Hallucination: Detection of Failures in Vision-Language Models via Multi-token Aggregation","url":"https://arxiv.org/html/2505.11741v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"Hallucination Detection in LLMs with Topological Divergence on ...","url":"https://www.semanticscholar.org/paper/1ec4be9cd511fc87e66e15233c16fa177c10aa86"},{"title":"VL-Uncertainty: Detecting Hallucination in Large Vision-Language Model via Uncertainty Estimation","url":"https://arxiv.org/html/2411.11919v2"}]

Based on the search results, I found detailed information about the paper arxiv 2411.09689:

## SHINE: Hallucination Detection via Perturbation-Driven Approach

SHINE is a novel hallucination probing method that uses the discovery that perturbing key entities in prompts affects LLM's generation of different types of text differently, and does not require external knowledge, supervised training, or LLM fine-tuning.

### Core Concept

SHINE classifies LLM-generated text into three categories: aligned, misaligned, and fabricated. Low Entity Perturbation Impact measured by KL divergence strongly indicates fabricated text, as its tokens are weakly tied to key entities. In contrast, a rise in generation probability after perturbation signals misalignment.

### Methodology

SHINE is a hallucination probing method that leverages Entity Perturbation Impact to distinguish between aligned, misaligned, and fabricated text. The method uses two main steps: a Model Knowledge Test (which identifies whether the LLM has sufficient knowledge to generate a faithful response by perturbing entities in the prompt and evaluating the impact, where fabricated text is differentiated at this stage) and an Alignment Test.

### Performance

SHINE achieves state-of-the-art performance in hallucination detection, outperforming seven competing methods across four datasets and four LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e271874c-9b32-4a40-a4b3-e091e31a1fbb",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "11ecba14-4c9b-4d20-8fde-c07dbf0762ab",
  "sourceToolAssistantUUID": "e271874c-9b32-4a40-a4b3-e091e31a1fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T10:00:24.290Z_

<details><summary>↩ Tool result · `toolu_018oozp79t57gNDQwu8oGuc6`</summary>

```text
Web search results for query: "Shaking to Reveal SSP perturbation hallucination detection Luo 2025 arxiv 2506.02696"

Links: [{"title":"[2506.02696] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696"},{"title":"arXiv:2506.02696v1 [cs.AI] 3 Jun 2025","url":"https://arxiv.org/pdf/2506.02696"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/html/2506.02696v1"},{"title":"[2506.02696v1] Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://arxiv.org/abs/2506.02696v1"},{"title":"Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations","url":"https://www.researchgate.net/publication/392371301_Shaking_to_Reveal_Perturbation-Based_Detection_of_LLM_Hallucinations"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://www.alphaxiv.org/overview/2506.02696v1"},{"title":"Perturbation-Based Detection of LLM Hallucinations","url":"https://seongheon-96.github.io/assets/pdf/shaking.pdf"},{"title":"Awesome-LM-SSP/collection/paper/safety/hallucination.md at main · CryptoAILab/Awesome-LM-SSP","url":"https://github.com/CryptoAILab/Awesome-LM-SSP/blob/main/collection/paper/safety/hallucination.md"},{"title":"[2407.05474] Enhancing Hallucination Detection through Perturbation-Based Synthetic Data Generation in System Responses","url":"https://arxiv.org/abs/2407.05474"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v1"}]

I found the paper! Here's what I found about it:

**Title:** "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations"

**Authors and Affiliation:** The paper is by Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, and Ling Chen from the Australian Artificial Intelligence Institute at the University of Technology Sydney and the Department of Computer Sciences at the University of Wisconsin-Madison.

**Key Contribution:** The paper proposes Sample-Specific Prompting (SSP), a new framework that improves self-assessment by analyzing perturbation sensitivity at intermediate representations.

**Core Idea:** SSP dynamically generates noise prompts for each input and employs a lightweight encoder to amplify the changes in representations caused by the perturbation. A contrastive distance metric is then used to quantify these differences and separate truthful from hallucinated responses.

**Motivation:** The standard self-assessment strategy assumes that the model's output distribution closely reflects the true data distribution, which may not always hold in practice. As bias accumulates through the model's layers, the final output can diverge from the underlying reasoning process, making output-level confidence an unreliable signal for hallucination detection.

**Results:** Extensive experiments demonstrate that SSP significantly outperforms prior methods across a range of hallucination detection benchmarks.

The paper was submitted to arXiv on June 3, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6be006d0-b81a-4cd3-90ab-abb8da25be28",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "7e873820-0cc6-46cc-b6c8-dbc77c14afa4",
  "sourceToolAssistantUUID": "6be006d0-b81a-4cd3-90ab-abb8da25be28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T10:00:24.538Z_

<details><summary>↩ Tool result · `toolu_01WeQA82yTYLSuRaB5n7bSma`</summary>

```text
Web search results for query: "HACK hallucination certainty knowledge axes Uehara arxiv 2510.24222"

Links: [{"title":"HACK: Hallucinations Along Certainty and Knowledge Axes","url":"https://arxiv.org/html/2510.24222"},{"title":"[2510.24222] HACK: Hallucinations Along Certainty and Knowledge Axes","url":"https://arxiv.org/abs/2510.24222"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/html/2502.12964v2"},{"title":"Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs","url":"https://arxiv.org/html/2502.12964v1"},{"title":"Multi-Modal Fact-Verification Framework for Reducing Hallucinations in Large Language Models","url":"https://arxiv.org/html/2510.22751"},{"title":"HALP: Detecting Hallucinations in Vision-Language Models without Generating a Single Token","url":"https://arxiv.org/html/2603.05465v1"},{"title":"Sequence-Level Certainty Reduces Hallucination In Knowledge-Grounded Dialogue Generation","url":"https://arxiv.org/html/2310.18794v3"},{"title":"Uncertainty Quantification for Hallucination Detection in ...","url":"https://arxiv.org/pdf/2510.12040"},{"title":"Hallucination Detection via Internal States and Structured Reasoning Consistency in Large Language Models","url":"https://arxiv.org/html/2510.11529"},{"title":"[2604.05719v1] Hackers or Hallucinators? A Comprehensive Analysis of LLM-Based Automated Penetration Testing","url":"https://arxiv.org/abs/2604.05719v1"}]

I found the paper! HACK proposes a framework for categorizing hallucinations along two axes: knowledge and certainty.

The paper is by Adi Simhi and 9 other authors. Key aspects of the framework include:

1. **Knowledge Axis**: The framework distinguishes between hallucinations caused by a lack of knowledge and those occurring despite the model having the knowledge of the correct response. Steering mitigation is applied to validate this axis by manipulating model activations.

2. **Certainty Axis**: The paper identifies a particularly concerning subset of hallucinations where models hallucinate with certainty despite having the correct knowledge internally. The authors introduce a new evaluation metric to measure the effectiveness of mitigation methods on this subset, revealing that while some methods perform well on average, they fail disproportionately on these critical cases.

The paper addresses an important limitation in hallucination research: existing research usually categorizes hallucinations by their external properties rather than by the LLMs' underlying internal properties, which overlooks that hallucinations may require tailored mitigation strategies based on their underlying mechanism.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b12b71e-f6d9-4ada-8d15-b1f57599532b",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "8035906a-d4c3-4e3d-8c39-e9f9ae9f6f67",
  "sourceToolAssistantUUID": "2b12b71e-f6d9-4ada-8d15-b1f57599532b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T10:00:26.620Z_

<details><summary>↩ Tool result · `toolu_019L9g1PKRJD6EY7CeyEGC4z`</summary>

```text
Web search results for query: "Aletheia cognitive conviction reasoning models arxiv 2601.01532"

Links: [{"title":"[2601.01532] Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix","url":"https://arxiv.org/abs/2601.01532"},{"title":"Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix","url":"https://arxiv.org/html/2601.01532"},{"title":"Aletheia: Quantifying Cognitive Conviction in Reasoning ...","url":"https://www.arxiv.org/pdf/2601.01532"},{"title":"Aletheia: Quantifying Cognitive Conviction in Reasoning ...","url":"https://web3.arxiv.org/pdf/2601.01532"},{"title":"(PDF) Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix","url":"https://www.researchgate.net/publication/399477532_Aletheia_Quantifying_Cognitive_Conviction_in_Reasoning_Models_via_Regularized_Inverse_Confusion_Matrix"},{"title":"Project Aletheia: Verifier-Guided Distillation of Backtracking for Small Language Models","url":"https://arxiv.org/html/2601.14290v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=842&show=2000"},{"title":"Aletheia: What Makes RLVR For Code Verifiers Tick?","url":"https://arxiv.org/html/2601.12186"},{"title":"[2601.14290] Project Aletheia: Verifier-Guided Distillation of Backtracking for Small Language Models","url":"https://arxiv.org/abs/2601.14290"},{"title":"Towards Autonomous Mathematics Research","url":"https://arxiv.org/html/2602.10177v1"}]

Based on the search results, here's what I found about the paper with arxiv ID 2601.01532:

## Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix

Project Aletheia is a cognitive physics framework that employs Tikhonov Regularization to invert the judge's confusion matrix.

**Core Problem and Motivation:**
Current evaluation paradigms face an epistemological crisis, where static benchmarks measure knowledge breadth but fail to quantify the depth of belief. The framework quantifies "Cognitive Conviction" in System 2 reasoning models.

**Methodology:**
To validate this methodology without relying on opaque private data, a Synthetic Proxy Protocol is implemented. The framework reformulates the evaluation of large language models not as a linguistic task but as a signal recovery problem within a noisy quantum channel, where the model's true conviction is a latent state vector, the user's prompt is a perturbation field, and the judge's evaluation is a measurement operator subject to systematic readout error.

**Key Findings:**
Preliminary pilot study on 2025 baselines (e.g., DeepSeek-R1, OpenAI o1) suggests that while reasoning models act as a "cognitive buffer," they may exhibit "Defensive OverThinking" under adversarial pressure. The framework introduces the Aligned Conviction Score (S_aligned) to verify that conviction does not compromise safety.

The paper was submitted to arXiv on January 4, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d3af406-0445-4c29-b989-9f9e91dad86e",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "c61bed74-f962-45f8-a1c5-cf5d8910726d",
  "sourceToolAssistantUUID": "3d3af406-0445-4c29-b989-9f9e91dad86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T10:00:30.456Z_

Good, all five papers appear to exist on arXiv. Now let me fetch the actual abstracts and details from each paper to verify the specific claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c61bed74-f962-45f8-a1c5-cf5d8910726d",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb643TLh6fsqyRtMUXu45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d04453fe-5c4a-4292-be95-02c1952c1d7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NikRTUAnLGex8ByXuqC9o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4530,
      "cache_read_input_tokens": 11071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4530,
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

_source line 18 · 2026-05-16T10:00:32.928Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JycSuYxNfii6w6qNvVpLGS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.00939",
  "prompt": "Extract the full title, authors, abstract, venue/submission info, and any mention of: EPGS, CHOKE, stubborn hallucinations, sharp output minima, gradient magnitude, embedding perturbation, flat minima. Report all details precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d04453fe-5c4a-4292-be95-02c1952c1d7b",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb643TLh6fsqyRtMUXu45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8684982-b247-4d46-9e95-a88253ee2c46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NikRTUAnLGex8ByXuqC9o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4530,
      "cache_read_input_tokens": 11071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4530,
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

_source line 19 · 2026-05-16T10:00:34.729Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PYVcAbUZfn2VSiibq6g8WN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.09689",
  "prompt": "Extract the full title, authors, abstract, and any mention of: SHINE, perturbation layers (input layer vs intermediate layers), KL divergence, output distribution. Report whether perturbation happens at input layer only or also at intermediate layers. Report all details precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8684982-b247-4d46-9e95-a88253ee2c46",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb643TLh6fsqyRtMUXu45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1f87917-e20e-4c15-ab2b-c482786a052a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NikRTUAnLGex8ByXuqC9o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4530,
      "cache_read_input_tokens": 11071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4530,
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

_source line 20 · 2026-05-16T10:00:36.660Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Qt8m9gruCk56DkWNYkntCd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.02696",
  "prompt": "Extract the full title, authors, abstract, and any mention of: SSP, perturbation at intermediate layers vs input layers, training requirements (does it require training a component?), cosine shift in representations, output logit KL divergence. Report all details precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1f87917-e20e-4c15-ab2b-c482786a052a",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb643TLh6fsqyRtMUXu45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cefaa18f-f487-4833-a943-a439bb3f837a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NikRTUAnLGex8ByXuqC9o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4530,
      "cache_read_input_tokens": 11071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4530,
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

_source line 21 · 2026-05-16T10:00:38.920Z_

<details><summary>↩ Tool result · `toolu_01JycSuYxNfii6w6qNvVpLGS`</summary>

```text
# Paper Summary

**Full Title:** "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity"

**Authors:** Yee Zhing Liew, Andrew Huey Ping Tan, Anwar P.P. Abdul Majeed

**Venue:** Accepted to ICML 2026 (camera-ready version)

**Submission Info:** arXiv:2605.00939 [cs.LG]; submitted May 1, 2026 (v1), revised May 12, 2026 (v2)

---

## Abstract Summary

The paper addresses "Stubborn Hallucinations"—instances where large language models confidently produce factual errors. The authors propose **Embedding-Perturbed Gradient Sensitivity (EPGS)** as their detection mechanism.

**Key concept:** They hypothesize that "robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization." 

**Method:** EPGS works by perturbing input embeddings with Gaussian noise and measuring resulting gradient magnitude spikes, functioning as "an efficient proxy for the Hessian spectrum."

**Results:** EPGS reportedly "outperforms entropy-based and representation-based baselines" for detecting high-confidence factual errors.

---

## Key Terms Identified

✓ **EPGS** (Embedding-Perturbed Gradient Sensitivity) - primary method  
✓ **Stubborn hallucinations** - confidence errors in LLMs  
✓ **Sharp minima** - where memorization occurs  
✓ **Flat minima** - where robust facts reside  
✓ **Gradient magnitude** - measurement for detecting sharpness  
✓ **Embedding perturbation** - Gaussian noise application  

*Note: "CHOKE" is not mentioned in the provided content.*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8684982-b247-4d46-9e95-a88253ee2c46",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "8034c432-7d0a-4379-87d3-472f523d3a11",
  "sourceToolAssistantUUID": "b8684982-b247-4d46-9e95-a88253ee2c46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T10:00:38.971Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016vqhJruymvMnJBM2sytQPV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.24222",
  "prompt": "Extract the full title, authors, abstract, and any mention of: Certainty Misalignment prevalence percentages (9-43% or any other numbers), knowledge axis, certainty axis, Uehara as author. Report all details precisely including author names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8034c432-7d0a-4379-87d3-472f523d3a11",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb643TLh6fsqyRtMUXu45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c0bb61c-7877-4e6f-8497-1d7f92847676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NikRTUAnLGex8ByXuqC9o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4530,
      "cache_read_input_tokens": 11071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4530,
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

_source line 23 · 2026-05-16T10:00:39.246Z_

<details><summary>↩ Tool result · `toolu_01PYVcAbUZfn2VSiibq6g8WN`</summary>

```text
# Paper Summary

**Full Title:** "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge"

**Authors:** Seongmin Lee, Hsiang Hsu, Chun-Fu Chen, Duen Horng Chau

**Abstract:**
The work addresses LLM hallucination detection by introducing "hallucination probing," which categorizes generated text into three types: aligned, misaligned, and fabricated. The authors discovered that "perturbing key entities in prompts affects LLM's generation of these three types" differently. They propose SHINE, a method requiring no external knowledge, supervised training, or fine-tuning.

---

## Key Findings from Content

**SHINE Method:** Mentioned as the proposed approach that achieves state-of-the-art performance across four datasets and four LLMs.

**Perturbation Location:** The webpage content does not specify whether perturbations occur at the input layer only or also at intermediate layers. This technical detail is not included in the abstract or available metadata.

**KL Divergence & Output Distribution:** These terms are not mentioned in the provided webpage content.

---

**Note:** The full paper details regarding perturbation layers, KL divergence, and output distribution specifics would require accessing the complete PDF or HTML version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1f87917-e20e-4c15-ab2b-c482786a052a",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "41ba9231-7d20-408d-9c07-2f77110c200a",
  "sourceToolAssistantUUID": "d1f87917-e20e-4c15-ab2b-c482786a052a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T10:00:39.462Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011WX2JVjWUS9YTCBLPKqzKc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.01532",
  "prompt": "Extract the full title, authors, abstract, venue/submission info, and key claims. Report all details precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41ba9231-7d20-408d-9c07-2f77110c200a",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb643TLh6fsqyRtMUXu45",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ff3a841-1a7b-45fe-864d-35bcc2693dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NikRTUAnLGex8ByXuqC9o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4530,
      "cache_read_input_tokens": 11071,
      "output_tokens": 619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4530
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 619,
          "cache_read_input_tokens": 11071,
          "cache_creation_input_tokens": 4530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4530,
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

_source line 25 · 2026-05-16T10:00:41.626Z_

<details><summary>↩ Tool result · `toolu_01Qt8m9gruCk56DkWNYkntCd`</summary>

```text
# Paper Summary: Hallucination Detection in LLMs

**Full Title:** "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations"

**Authors:** Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, Ling Chen

## Abstract Summary
The research addresses hallucination detection by proposing that output-level confidence is unreliable because "bias accumulates through the model's layers, the final output can diverge from the underlying reasoning process." The solution analyzes intermediate representations instead.

## Key Findings from Content:

**Sample-Specific Prompting (SSP):** The framework is explicitly mentioned as the proposed method that "dynamically generates noise prompts for each input and employs a lightweight encoder."

**Perturbation Strategy:** SSP operates on intermediate representations rather than input layers, since these representations are described as "being less influenced by model bias."

**Training Requirements:** The method includes "a lightweight encoder to amplify the changes in representations caused by the perturbation," indicating a trainable component is employed.

**Distance Metric:** The approach uses "a contrastive distance metric" to quantify representation differences.

**Notable Omissions:** The provided content does not mention cosine shift in representations or output logit KL divergence calculations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cefaa18f-f487-4833-a943-a439bb3f837a",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "3cc4bc6c-c0b7-4295-9248-7917be9ace1a",
  "sourceToolAssistantUUID": "cefaa18f-f487-4833-a943-a439bb3f837a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T10:00:44.054Z_

<details><summary>↩ Tool result · `toolu_016vqhJruymvMnJBM2sytQPV`</summary>

```text
# Paper Details Extraction

**Full Title:**
HACK: Hallucinations Along Certainty and Knowledge Axes

**Authors:**
Adi Simhi, Jonathan Herzig, Itay Itzhak, Dana Arad, Zorik Gekhman, Roi Reichart, Fazl Barez, Gabriel Stanovsky, Idan Szpektor, Yonatan Belinkov

**Abstract Summary:**
The paper proposes a framework categorizing LLM hallucinations using two dimensions. Along the knowledge axis, researchers distinguish between hallucinations from lacking knowledge versus those occurring despite possessing correct information internally. The certainty axis identifies cases where models "hallucinate with certainty despite having the correct knowledge internally." The work validates approaches through steering mitigation and introduces metrics to evaluate mitigation effectiveness on critical hallucination subsets.

**Key Findings:**

- **Knowledge Axis:** Two hallucination types based on whether parametric knowledge exists
- **Certainty Axis:** Focus on problematic cases combining high confidence with incorrect outputs
- **Certainty Misalignment Percentages:** No specific prevalence percentages (9-43% or otherwise) mentioned in this content
- **Uehara as Author:** Not listed among the ten authors

**Note:** The document does not contain the prevalence statistics or author you inquired about.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c0bb61c-7877-4e6f-8497-1d7f92847676",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "06c552e7-85a9-4fd4-86bb-299b1a125e0b",
  "sourceToolAssistantUUID": "9c0bb61c-7877-4e6f-8497-1d7f92847676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T10:00:44.195Z_

<details><summary>↩ Tool result · `toolu_011WX2JVjWUS9YTCBLPKqzKc`</summary>

```text
# Paper Summary: Aletheia

**Full Title:**
"Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix"

**Author:**
Fanzhe Fu

**Submission Info:**
- arXiv identifier: 2601.01532
- Submitted: January 4, 2026
- Classification: Computer Science > Artificial Intelligence
- Length: 6 pages, 2 figures

**Abstract Summary:**
The paper addresses evaluation limitations in advanced AI systems by proposing a framework to measure "cognitive conviction" in reasoning models. It employs Tikhonov regularization to invert confusion matrices and introduces a "Synthetic Proxy Protocol" for validation. The research examines 2025 models including DeepSeek-R1 and OpenAI o1, suggesting these systems may exhibit "Defensive OverThinking" when facing adversarial challenges. The authors also propose an "Aligned Conviction Score" to ensure confidence doesn't compromise safety considerations.

**Key Claims:**
- Current benchmarks measure breadth but fail to capture "depth of belief"
- Reasoning models function as a "cognitive buffer" in the evaluation process
- Advanced systems may demonstrate problematic reasoning patterns under pressure
- A new metric can validate that model conviction remains aligned with safety principles
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ff3a841-1a7b-45fe-864d-35bcc2693dab",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "d9297da6-d1f1-4057-88a2-2549a40ab279",
  "sourceToolAssistantUUID": "5ff3a841-1a7b-45fe-864d-35bcc2693dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-16T10:00:47.403Z_

Now let me get more details on a few papers where claims need further verification. Let me fetch the full HTML versions for SHINE and HACK to check the specific claims about perturbation layers, KL divergence, and prevalence percentages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9297da6-d1f1-4057-88a2-2549a40ab279",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb644k43kCSfccWZgSnZV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb12c03b-cb16-42a3-a77e-c2fdf9dcfb39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZzmaUdcPNvHxdpW8ECP7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 15601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 29 · 2026-05-16T10:00:50.414Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SSdYxyomCSmnuogb8aoTXc`</summary>

```json
{
  "url": "https://arxiv.org/html/2411.09689",
  "prompt": "Look for details about: 1) Where does SHINE apply perturbation - at the INPUT layer (prompt/embedding level) or at intermediate/hidden layers? 2) Does it use KL divergence as a metric? 3) What exactly is the Entity Perturbation Impact and how is it computed? Report the specific methodology details precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb12c03b-cb16-42a3-a77e-c2fdf9dcfb39",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb644k43kCSfccWZgSnZV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c91f500-5730-4898-bcc6-17cdc0fc8b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZzmaUdcPNvHxdpW8ECP7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 15601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 30 · 2026-05-16T10:00:52.702Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011cSCzW8dEemrjXeH4gvkfD`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.24222",
  "prompt": "Search for specific prevalence percentages for \"Certainty Misalignment\" - any mention of 9%, 43%, or a range like 9-43%. Also look for the author name \"Uehara\" anywhere. Report exact percentages found for any hallucination category prevalence."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c91f500-5730-4898-bcc6-17cdc0fc8b93",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb644k43kCSfccWZgSnZV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceac33df-751a-41d6-a845-d7979d92fe96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZzmaUdcPNvHxdpW8ECP7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 15601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2496,
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

_source line 31 · 2026-05-16T10:00:55.151Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UL3pogaKZUQ2uigVhTXfFw`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.02696v1",
  "prompt": "Look for details about: 1) Does SSP perturb at intermediate layers specifically? 2) Does the lightweight encoder require training/learning? 3) Does it use cosine similarity/cosine shift to measure representation changes, or KL divergence on output logits, or a contrastive distance metric? 4) What exactly is the distance metric used? Report all methodology details precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceac33df-751a-41d6-a845-d7979d92fe96",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb644k43kCSfccWZgSnZV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25557a3f-ca34-40ea-bfe2-126b15d50304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZzmaUdcPNvHxdpW8ECP7R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2496,
      "cache_read_input_tokens": 15601,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 15601,
          "cache_creation_input_tokens": 2496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2496,
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

_source line 32 · 2026-05-16T10:00:56.388Z_

<details><summary>↩ Tool result · `toolu_01SSdYxyomCSmnuogb8aoTXc`</summary>

```text
# SHINE: Perturbation Details and Methodology

## 1. Where Perturbation is Applied

SHINE applies perturbation **at the embedding layer (input level)**, not at intermediate or hidden layers. Specifically, the method:

- Identifies key entities in prompts
- Adds Gaussian noise directly to token embeddings: *"add Gaussian noise ϵ∼𝒩(0,(3𝝈₀)²)∈ℝᴷˣᵈ to all occurrences of S"*
- Uses modified embeddings as input to the LLM forward pass

## 2. KL Divergence as Metric

Yes, KL divergence is central to the approach. The method measures differences between original and perturbed probability distributions:

*"Kullback-Leibler (KL) divergence between 𝐏ᵢ and 𝐏̂ᵢ...to capture global effects across"* the vocabulary.

## 3. Entity Perturbation Impact Computation

The Entity Perturbation Impact consists of two metrics:

**KL Divergence Component:**
- Measures distance between original probability distribution 𝐏ᵢ and perturbed distribution 𝐏̂ᵢ at each token position
- Indicates strength of association between generated tokens and the perturbed entity's knowledge

**ΔPᵢ Component:**
- Change in generation probability: ΔPᵢ = 𝐏̂ᵢ(tᵢ) - 𝐏ᵢ(tᵢ)
- Captures how perturbation affects specific generated tokens
- Positive values suggest misalignment; negative/near-zero suggests alignment or fabrication

The method repeats perturbations 10 times with different random seeds to mitigate noise effects, then aggregates results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c91f500-5730-4898-bcc6-17cdc0fc8b93",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "d5fcbe40-5a27-47c5-a0bc-7513f93dc37d",
  "sourceToolAssistantUUID": "9c91f500-5730-4898-bcc6-17cdc0fc8b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T10:00:57.247Z_

<details><summary>↩ Tool result · `toolu_011cSCzW8dEemrjXeH4gvkfD`</summary>

```text
# Search Results for Certainty Misalignment Prevalence

## Key Findings

The document explicitly states that Certainty Misalignment (CM) hallucinations occur at the following rates:

**"A non-negligible amount of hallucinations (9%–43%) occur with high certainty"** across different models, certainty methods, and datasets tested.

More specifically, Table 6 indicates CM prevalence ranges from approximately 9% to 43% depending on:
- The certainty measurement method used (probability, probability difference, or semantic entropy)
- The model evaluated (Llama, Mistral, Gemma, and their instruction-tuned variants)
- The dataset (TriviaQA or Natural Questions)

## Author Search Result

**No author named "Uehara" appears anywhere in the provided document.**

The paper's authors are: Adi Simhi, Jonathan Herzig, Itay Itzhak, Dana Arad, Zorik Gekhman, Roi Reichart, Fazl Barez, Gabriel Stanovsky, Idan Szpektor, and Yonatan Belinkov.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceac33df-751a-41d6-a845-d7979d92fe96",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "da86c0e8-7034-4a90-9ef4-10411d28d0a5",
  "sourceToolAssistantUUID": "ceac33df-751a-41d6-a845-d7979d92fe96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T10:01:00.978Z_

<details><summary>↩ Tool result · `toolu_01UL3pogaKZUQ2uigVhTXfFw`</summary>

```text
# SSP Methodology Details: Perturbation and Distance Metrics

## 1. Intermediate Layer Perturbation

Yes, SSP explicitly targets intermediate layers. The framework extracts representations from intermediate layers rather than relying solely on output logits. As stated: "intermediate representations, being less influenced by model bias, offer a more faithful view of the model's latent reasoning process."

## 2. Lightweight Encoder Training

The encoder requires training. The paper implements "a shared and learnable encoder module fϕ(⋅)" with trainable parameters ϕ. This encoder is optimized during a 40-epoch training process using SGD with a learning rate of 0.01, alongside the prompt generator parameters.

## 3. Distance Metric: Cosine Similarity

SSP uses **cosine-based discrepancy**, not KL divergence on logits or contrastive distance in the traditional sense. The discrepancy function is defined as:

**Disc(z, z̃) = 1 − cos(z, z̃) = 1 − (z·z̃)/(|z||z̃|)**

## 4. Precise Methodology

The method measures representation shifts via:
- Original representation: z = fϕ(Eθ(x=True|Q,A,T))
- Perturbed representation: z̃ = fϕ(Eθ(x=True|Q,A,N,T))
- Discrepancy quantifies magnitude of change using cosine dissimilarity

The paper explicitly notes: "cosine-based metrics are robust to variations in feature magnitudes across different layers," and ablation studies confirm cosine similarity "consistently provides better separability between truthful and hallucinated responses."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25557a3f-ca34-40ea-bfe2-126b15d50304",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "33a97cce-6cc9-49eb-b313-585491c0aab2",
  "sourceToolAssistantUUID": "25557a3f-ca34-40ea-bfe2-126b15d50304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-16T10:01:04.550Z_

Now I have comprehensive information on all five papers. Let me also verify the EPGS paper's mention (or non-mention) of "CHOKE" since that's a specific claim to check.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33a97cce-6cc9-49eb-b313-585491c0aab2",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb645yn5Hm6gZk6Cq3Xrp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c8b68e8-73a4-4717-9b49-95aa573a1105",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNnoWKbwrofA1QycQZhGBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 18097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1685,
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

_source line 36 · 2026-05-16T10:01:07.442Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SXyZvpfXxaj6SWwuggKUfg`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00939",
  "prompt": "Search the full text for any mention of \"CHOKE\" or \"Confident Hallucinations with Overridden Knowledge Encoding\" or any similar acronym. Also confirm whether the paper says hallucinations reside in \"sharp output minima\" specifically - does it say \"output minima\" or just \"sharp minima\"? Report the exact phrasing used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c8b68e8-73a4-4717-9b49-95aa573a1105",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb645yn5Hm6gZk6Cq3Xrp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6927da29-dceb-4609-bf0c-b085c53d001e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNnoWKbwrofA1QycQZhGBa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 18097,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 18097,
          "cache_creation_input_tokens": 1685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1685,
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

_source line 37 · 2026-05-16T10:01:08.185Z_

<details><summary>↩ Tool result · `toolu_01SXyZvpfXxaj6SWwuggKUfg`</summary>

```text
API Error: 400 {"type":"error","error":{"type":"invalid_request_error","message":"The request body is not valid JSON: no low surrogate in string: line 1 column 102415 (char 102414)"},"request_id":"req_011Cb646VGc5DnAxaw9PVmTs"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6927da29-dceb-4609-bf0c-b085c53d001e",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "a1a5c46d-f1ad-4a79-ad6e-3ad13c88c173",
  "sourceToolAssistantUUID": "6927da29-dceb-4609-bf0c-b085c53d001e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T10:01:10.331Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018JQYXfMymDtVgm4jn33jFb`</summary>

```json
{
  "query": "arxiv 2605.00939 \"CHOKE\" \"sharp output minima\" EPGS full text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1a5c46d-f1ad-4a79-ad6e-3ad13c88c173",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb646WdU4JU8YU6aKakTG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c035f52-8bc4-4dca-a39f-d1b0148f0d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U75VgMF8rnpBznhtjC7r3Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 296,
      "cache_read_input_tokens": 19782,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 296
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 19782,
          "cache_creation_input_tokens": 296,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 296,
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

_source line 39 · 2026-05-16T10:01:20.251Z_

<details><summary>↩ Tool result · `toolu_018JQYXfMymDtVgm4jn33jFb`</summary>

```text
Web search results for query: "arxiv 2605.00939 "CHOKE" "sharp output minima" EPGS full text"

Links: [{"title":"[2605.00939] From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/abs/2605.00939"},{"title":"From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity","url":"https://arxiv.org/html/2605.00939"},{"title":"How to Escape Sharp Minima with Random Perturbations","url":"https://arxiv.org/pdf/2305.15659"},{"title":"Sharp Minima Can Generalize For Deep Nets","url":"https://arxiv.org/pdf/1703.04933"},{"title":"[1805.07898] SmoothOut: Smoothing Out Sharp Minima to Improve Generalization in Deep Learning","url":"https://arxiv.org/abs/1805.07898"},{"title":"Sharp feature-learning transitions and Bayes-optimal neural scaling laws in extensive-width networks","url":"https://arxiv.org/html/2605.10395"},{"title":"Sharp minima can generalize for deep nets","url":"https://scispace.com/papers/sharp-minima-can-generalize-for-deep-nets-1nsmqbh47m"},{"title":"[2605.11806] Adaptive Kernel Ridge Regression with Linear Structure: Sharp Oracle Inequalities and Minimax Optimality","url":"https://arxiv.org/abs/2605.11806"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=200&show=2000"},{"title":"Rethinking the Rank Threshold for LoRA Fine-Tuning","url":"https://arxiv.org/html/2605.03724v1"}]

I found the arXiv paper arxiv 2605.00939. Here's what the search results show:

The paper is titled "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity", submitted by Yee Zhing Liew and co-authors on May 1, 2026.

The paper introduces Embedding-Perturbed Gradient Sensitivity (EPGS), which addresses a key problem in LLMs. The authors hypothesize that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization.

EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude, which acts as an efficient proxy for the Hessian spectrum, differentiating stable knowledge from unstable memorization. The experiments show that EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.

Note: I didn't find the acronym "CHOKE" in the search results. The paper focuses on EPGS as the main method for detecting what the authors call "Stubborn Hallucinations" - high-confidence errors in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c035f52-8bc4-4dca-a39f-d1b0148f0d09",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "eb865fbc-2bdd-4dd1-87b7-ab825faf2848",
  "sourceToolAssistantUUID": "2c035f52-8bc4-4dca-a39f-d1b0148f0d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T10:01:22.564Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014uP2Pf5pPL1bT3f1psk1X6`</summary>

```json
{
  "query": "\"CHOKE\" \"stubborn hallucinations\" LLM hallucination detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb865fbc-2bdd-4dd1-87b7-ab825faf2848",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb647QD37ykVoLLXapDDb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8732e54f-b720-4c2e-a166-8d6db8969678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1gzQsYkSKqCDUWquAmHxK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 20078,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 859
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 20078,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 859,
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

_source line 41 · 2026-05-16T10:01:32.514Z_

<details><summary>↩ Tool result · `toolu_014uP2Pf5pPL1bT3f1psk1X6`</summary>

```text
Web search results for query: ""CHOKE" "stubborn hallucinations" LLM hallucination detection"

Links: [{"title":"Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs","url":"https://arxiv.org/html/2502.12964v1"},{"title":"Detecting hallucinations in large language models using semantic entropy | Nature","url":"https://www.nature.com/articles/s41586-024-07421-0"},{"title":"Must-Attend AI LLM Hallucination Detection And Mitigation | Deepchecks","url":"https://deepchecks.com/llm-hallucination-detection-and-mitigation-best-techniques/"},{"title":"Detecting hallucinations with LLM-as-a-judge: Prompt engineering and beyond | Datadog","url":"https://www.datadoghq.com/blog/ai/llm-hallucination-detection/"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"How to Measure and Prevent LLM Hallucinations | Promptfoo","url":"https://www.promptfoo.dev/docs/guides/prevent-llm-hallucinations/"},{"title":"5 Practical Techniques to Detect and Mitigate LLM Hallucinations Beyond Prompt Engineering - MachineLearningMastery.com","url":"https://machinelearningmastery.com/5-practical-techniques-to-detect-and-mitigate-llm-hallucinations-beyond-prompt-engineering/"},{"title":"Detect hallucinations in your RAG LLM applications with Datadog LLM Observability | Datadog","url":"https://www.datadoghq.com/blog/llm-observability-hallucination-detection/"},{"title":"LLM-Check: Investigating Detection of Hallucinations in Large Language Models","url":"https://openreview.net/pdf?id=LYx4w3CAgy"},{"title":"LLM Hallucinations: Detect and Quantify before you apply RAG | Google Cloud - Community","url":"https://medium.com/google-cloud/hallucination-detection-measurement-932e23b1873b"}]

Based on the search results, I can provide you with information about CHOKE and LLM hallucination detection:

## CHOKE: High-Certainty Hallucinations

CHOKE refers to high-certainty hallucinations, which are hallucinations that existing mitigation methods based on uncertainty fail to address. This is a recently identified phenomenon that challenges conventional understanding of how hallucinations work.

### Key Characteristics

Models may produce factually incorrect responses while maintaining a high degree of certainty, even when they possess the capability to provide the correct answer. Certain hallucinations are systematic rather than random noise, showing consistent reproduction of the same hallucinations across different settings.

### Problem with Traditional Detection Methods

Prior research has associated hallucinations with model uncertainty, leveraging uncertainty estimation metrics such as semantic entropy, sampling, and probability for hallucination detection and mitigation. However, models can hallucinate with high certainty even when they have the correct knowledge, making these uncertainty-based approaches insufficient.

### Implications

This presents a significant challenge for the deployment of LLMs in high-stakes domains, such as healthcare, legal applications, and scientific research, where erroneous outputs can have severe consequences.

### Research Findings

High-certainty hallucinations are consistent across models and datasets, distinctive enough to be singled out, and challenge existing mitigation methods. This research reveals that the common assumption linking hallucinations primarily to low model certainty is incomplete, necessitating new approaches to detect and mitigate these stubborn hallucinations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8732e54f-b720-4c2e-a166-8d6db8969678",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "d3e6b524-c91a-4a66-908a-7c52c14aa385",
  "sourceToolAssistantUUID": "8732e54f-b720-4c2e-a166-8d6db8969678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T10:01:36.020Z_

The term "CHOKE" does not appear to be a term used in the EPGS paper itself. Let me do one final check to see if "CHOKE" is a defined term from another paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3e6b524-c91a-4a66-908a-7c52c14aa385",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb648JdTLKxr1GkYdXDmD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c87a28ba-9f22-444f-958e-3ddc5528f496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gfpxt1tFkf8B4xKW6DtJnC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 20937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1034,
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

_source line 43 · 2026-05-16T10:01:36.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H9HZ1tMS8AwCQUeXFdu8di`</summary>

```json
{
  "query": "CHOKE acronym \"Confident Hallucinations\" OR \"Confidently Hallucinated\" LLM paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c87a28ba-9f22-444f-958e-3ddc5528f496",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb648JdTLKxr1GkYdXDmD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4ba35b9-7901-424e-be5b-a110b1611748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gfpxt1tFkf8B4xKW6DtJnC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 20937,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 20937,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1034,
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

_source line 44 · 2026-05-16T10:01:46.805Z_

<details><summary>↩ Tool result · `toolu_01H9HZ1tMS8AwCQUeXFdu8di`</summary>

```text
Web search results for query: "CHOKE acronym "Confident Hallucinations" OR "Confidently Hallucinated" LLM paper"

Links: [{"title":"Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs","url":"https://arxiv.org/html/2502.12964v1"},{"title":"LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://aclanthology.org/2025.findings-emnlp.792.pdf"},{"title":"[2502.12964] Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/abs/2502.12964"},{"title":"Trust Me, I’m Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer","url":"https://arxiv.org/html/2502.12964v2"},{"title":"Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250212964S/abstract"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"How to gauge LLM confidence and estimate hallucination ...","url":"https://www.linkedin.com/posts/garyang_paper-preprint-activity-7369981191980163072-nrer"},{"title":"Why language models hallucinate | OpenAI","url":"https://openai.com/index/why-language-models-hallucinate/"},{"title":"LLM Hallucinations: Mitigating AI Errors | Appen","url":"https://www.appen.com/blog/ai-hallucinations"}]

Based on the search results, I found the paper you're looking for:

The acronym CHOKE stands for "Certain Hallucinations Overriding Known Evidence", not "Confident Hallucinations" or "Confidently Hallucinated."

The paper is titled "Trust Me, I'm Wrong: LLMs Hallucinate with Certainty Despite Knowing the Answer" by Adi Simhi and 4 other authors. 

The work defines and investigates a distinct type of hallucination where a model can consistently answer a question correctly, but a seemingly trivial perturbation causes it to produce a hallucinated response with high certainty. CHOKE examples occur in 16–43% of hallucinations outputs across models and certainty methods.

The paper is available on arXiv (version 2 dated August 25, 2025) and was also published in the EMNLP 2025 Findings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4ba35b9-7901-424e-be5b-a110b1611748",
  "isSidechain": true,
  "promptId": "333a6cea-3b4c-46b8-9da2-3e1c981b5261",
  "agentId": "afae822db8c4cc166",
  "type": "user",
  "uuid": "61ad194f-5f68-4ed0-85f6-edd4a7fcae4b",
  "sourceToolAssistantUUID": "b4ba35b9-7901-424e-be5b-a110b1611748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-16T10:02:39.506Z_

Now I have comprehensive information on all papers. Here is my full report.

---

## Paper Verification Report

### 1. EPGS -- arxiv 2605.00939

**Does it exist?** Yes.

**Title:** "From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity"

**Authors:** Yee Zhing Liew, Andrew Huey Ping Tan, Anwar P.P. Abdul Majeed

**Venue:** Accepted to ICML 2026 (camera-ready). Submitted May 1, 2026.

**What it does:** Proposes Embedding-Perturbed Gradient Sensitivity (EPGS). Perturbs input embeddings with Gaussian noise and measures the resulting spike in gradient magnitude, as a proxy for the Hessian spectrum. The hypothesis is that robust facts reside in flat minima while stubborn hallucinations sit in sharp minima (brittle memorization).

**Discrepancies with your claims:**
- The claim about "CHOKE/stubborn hallucinations" is **partially misleading**. The EPGS paper uses the term "Stubborn Hallucinations" but does NOT appear to use the acronym "CHOKE." CHOKE ("Certain Hallucinations Overriding Known Evidence") is a term from a *different* paper -- "Trust Me, I'm Wrong" (Simhi et al., EMNLP 2025 Findings, arxiv 2502.12964). Conflating these two concepts is inaccurate unless the EPGS paper explicitly cites and builds on CHOKE, which is not evident from the abstract/metadata.
- The phrase "sharp output minima" -- the paper says "sharp minima," not specifically "sharp *output* minima." The word "output" may be an embellishment.
- The core claims (sharp minima, gradient magnitude after embedding perturbation) are otherwise accurate.

---

### 2. SHINE -- arxiv 2411.09689

**Does it exist?** Yes.

**Title:** "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge"

**Authors:** Seongmin Lee, Hsiang Hsu, Chun-Fu Chen, Duen Horng Chau

**Venue:** arXiv preprint (November 2024). No specific conference venue confirmed from the abstract page.

**What it does:** SHINE categorizes generated text into aligned, misaligned, and fabricated. It perturbs key entities in prompts by adding Gaussian noise to token embeddings and measures Entity Perturbation Impact via KL divergence between original and perturbed output distributions, plus change in generation probability.

**Discrepancies with your claims:**
- "Perturbs at INPUT layer only, or also intermediate layers?" -- **INPUT layer only.** SHINE adds noise to token embeddings (the embedding layer), NOT to intermediate layers. This is confirmed by the full paper text.
- "Does it measure output KL divergence?" -- **Yes.** KL divergence between original and perturbed output probability distributions is a core metric, alongside delta-P (change in generation probability). This claim is accurate.

---

### 3. SSP / "Shaking to Reveal" -- arxiv 2506.02696

**Does it exist?** Yes.

**Title:** "Shaking to Reveal: Perturbation-Based Detection of LLM Hallucinations"

**Authors:** Jinyuan Luo, Zhen Fang, Yixuan Li, Seongheon Park, Ling Chen

**Venue:** arXiv preprint (June 3, 2025). No confirmed conference venue from abstract page.

**What it does:** Proposes Sample-Specific Prompting (SSP). It dynamically generates noise prompts per input, extracts intermediate-layer representations, passes them through a lightweight learned encoder, and measures cosine-based discrepancy (1 - cosine similarity) between original and perturbed representations.

**Discrepancies with your claims:**
- "Does it perturb at intermediate layers?" -- **Yes**, confirmed. SSP explicitly targets intermediate representations rather than output logits.
- "Does it require training?" -- **Yes.** It uses a learnable encoder (fPhi) trained with SGD for 40 epochs, plus trainable prompt generator parameters. It is NOT training-free.
- "Does it measure representation cosine shift vs output logit KL?" -- It measures **cosine-based discrepancy on representations** (1 - cos(z, z_tilde)), NOT output logit KL divergence. The claim about "output logit KL" would be incorrect if attributed to this paper. The cosine shift part is accurate.

---

### 4. HACK -- arxiv 2510.24222

**Does it exist?** Yes.

**Title:** "HACK: Hallucinations Along Certainty and Knowledge Axes"

**Authors:** Adi Simhi, Jonathan Herzig, Itay Itzhak, Dana Arad, Zorik Gekhman, Roi Reichart, Fazl Barez, Gabriel Stanovsky, Idan Szpektor, Yonatan Belinkov

**Venue:** arXiv preprint (October 2025). No confirmed conference venue.

**What it does:** Proposes a two-axis framework for categorizing hallucinations: (1) Knowledge axis (does the model have the knowledge or not?), (2) Certainty axis (is the model certain or uncertain?). Identifies "Certainty Misalignment" as a critical failure mode. Uses steering-based mitigation to validate the knowledge axis.

**Discrepancies with your claims:**
- "Certainty Misalignment prevalence 9-43%" -- **Confirmed.** The paper explicitly states that 9%-43% of hallucinations occur with high certainty, varying by model, certainty method, and dataset.
- "Uehara" as author -- **INCORRECT.** There is no author named "Uehara" on this paper. The lead author is Adi Simhi. None of the 10 authors is named Uehara. This is a factual error in the claim.

---

### 5. Aletheia -- arxiv 2601.01532

**Does it exist?** Yes.

**Title:** "Aletheia: Quantifying Cognitive Conviction in Reasoning Models via Regularized Inverse Confusion Matrix"

**Author:** Fanzhe Fu (single author)

**Venue:** arXiv preprint (January 4, 2026). No confirmed conference venue. 6 pages, 2 figures.

**What it does:** Proposes a "cognitive physics" framework that uses Tikhonov regularization to invert a judge's confusion matrix, framing LLM evaluation as a signal recovery problem. Introduces a "Synthetic Proxy Protocol" and an "Aligned Conviction Score." Tests on DeepSeek-R1 and OpenAI o1.

**Discrepancies with your claims:**
- The paper does exist and the title/topic match. However, this is a very short paper (6 pages) by a single author with somewhat unconventional framing (describing LLM evaluation as a "quantum channel" analogy). No discrepancies with the basic existence claim, but anyone citing this should be aware of its scope and unconventional methodology.

---

## Summary of Discrepancies Found

| Claim | Verdict |
|-------|---------|
| EPGS paper exists at ICML 2026 | **Correct** |
| EPGS paper demonstrates CHOKE hallucinations in sharp minima | **Partially wrong** -- "CHOKE" is from a different paper (Simhi et al., EMNLP 2025), not the EPGS paper |
| "Sharp output minima" phrasing | **Minor inaccuracy** -- paper says "sharp minima," not "sharp output minima" |
| SHINE perturbs at input layer only | **Correct** -- input embeddings only, not intermediate layers |
| SHINE measures output KL divergence | **Correct** |
| SSP perturbs at intermediate layers | **Correct** |
| SSP requires training | **Correct** -- learnable encoder trained for 40 epochs |
| SSP uses cosine shift | **Correct** -- cosine-based discrepancy |
| SSP uses output logit KL | **Incorrect if claimed** -- it uses cosine distance on representations, not KL on logits |
| HACK Certainty Misalignment 9-43% | **Correct** |
| HACK authored by Uehara | **Incorrect** -- lead author is Adi Simhi; no Uehara among 10 authors |
| Aletheia paper exists | **Correct** |

Sources:
- [EPGS - arxiv 2605.00939](https://arxiv.org/abs/2605.00939)
- [SHINE - arxiv 2411.09689](https://arxiv.org/abs/2411.09689)
- [SSP "Shaking to Reveal" - arxiv 2506.02696](https://arxiv.org/abs/2506.02696)
- [HACK - arxiv 2510.24222](https://arxiv.org/abs/2510.24222)
- [Aletheia - arxiv 2601.01532](https://arxiv.org/abs/2601.01532)
- [CHOKE / "Trust Me, I'm Wrong" - arxiv 2502.12964](https://arxiv.org/abs/2502.12964)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61ad194f-5f68-4ed0-85f6-edd4a7fcae4b",
  "isSidechain": true,
  "agentId": "afae822db8c4cc166",
  "requestId": "req_011Cb649MoyLtjkoSr2JvDgg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a78fc3a8-660d-4513-89b7-61a13bb3ea5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "500d2520-b9cc-4a42-8fc8-528df874b676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXHA7PQZr45XeNhAg8gVQj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 21971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1018,
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
