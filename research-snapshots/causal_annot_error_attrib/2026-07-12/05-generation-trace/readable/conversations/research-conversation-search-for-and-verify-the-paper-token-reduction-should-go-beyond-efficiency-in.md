# Research conversation: Search for and verify the paper "Token Reduction Should Go Beyond Efficiency in Generative Models — From Vision, Languag

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ae99e5842e9853108.jsonl`
- **Structured JSON:** [`9c1c03261a381ac3f73e.json`](../../sessions/9c/9c1c03261a381ac3f73e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-14T06:18:30.544Z_

Search for and verify the paper "Token Reduction Should Go Beyond Efficiency in Generative Models — From Vision, Language to Multimodality" (arXiv 2505.18227). Verify:
1. Does this paper exist?
2. Is it a position/survey paper?
3. What does it argue about token reduction beyond efficiency?
4. Does it propose any concrete methods, or is it purely a position paper?
5. Does it mention VLAs or robotics?

Also search for the counter-evidence papers:
- arXiv 2601.21531: About adversarial robustness of large VLMs under visual token compression
- arXiv 2601.12042: "Less Is More — Until It Breaks" about security pitfalls of vision token compression

Verify these exist and what they actually conclude about token compression hurting robustness.

Use WebSearch and WebFetch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "995fbfe0-1dc0-43ad-a3a1-daabcbe21f0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T06:18:30.564Z_

```json
{
  "parentUuid": "995fbfe0-1dc0-43ad-a3a1-daabcbe21f0e",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
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
  "uuid": "2fdd6c07-f09d-434e-bc6c-02838121e9fc",
  "timestamp": "2026-05-14T06:18:30.564Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T06:18:33.096Z_



I'll search for all three papers systematically. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fdd6c07-f09d-434e-bc6c-02838121e9fc",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yW2oDcxaq3gSUq63Kg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "683d15c1-9d65-4ffb-8880-fc2ce6b937b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwMZbpd4SqAtohRQxA4CVK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 754,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-14T06:18:33.184Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EqMHoVtwcn6h1Bt7XF8X76`</summary>

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
  "parentUuid": "683d15c1-9d65-4ffb-8880-fc2ce6b937b8",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yW2oDcxaq3gSUq63Kg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "762f7f15-5aea-469d-b2e5-beb009623729",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwMZbpd4SqAtohRQxA4CVK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 754,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-14T06:18:33.187Z_

<details><summary>↩ Tool result · `toolu_01EqMHoVtwcn6h1Bt7XF8X76`</summary>

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
  "parentUuid": "762f7f15-5aea-469d-b2e5-beb009623729",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "d4daa4e9-5215-475b-af76-c28fdabe5cf9",
  "sourceToolAssistantUUID": "762f7f15-5aea-469d-b2e5-beb009623729",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T06:18:35.563Z_



Now let me search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4daa4e9-5215-475b-af76-c28fdabe5cf9",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yWEGHTdPUNFAtbBVMf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19a44d2e-321c-4242-acff-376b8ad9e0dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011To9N7in25KX4odTzR9QU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 7 · 2026-05-14T06:18:36.043Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VrDK5WvHNpxi4eUmygSebB`</summary>

```json
{
  "query": "arXiv 2505.18227 \"Token Reduction Should Go Beyond Efficiency in Generative Models\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a44d2e-321c-4242-acff-376b8ad9e0dc",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yWEGHTdPUNFAtbBVMf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "816745c1-3f2b-4538-94d6-dba503dd3ce8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011To9N7in25KX4odTzR9QU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 8 · 2026-05-14T06:18:36.515Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C9SodbaxbCRzGxTEJ2tgxJ`</summary>

```json
{
  "query": "arXiv 2601.21531 adversarial robustness large VLMs visual token compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "816745c1-3f2b-4538-94d6-dba503dd3ce8",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yWEGHTdPUNFAtbBVMf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b08b3f4d-4c48-4926-b036-b609b075796a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011To9N7in25KX4odTzR9QU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 9 · 2026-05-14T06:18:36.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017vnY3H6Yu52xGegk3uvSaS`</summary>

```json
{
  "query": "arXiv 2601.12042 \"Less Is More Until It Breaks\" security pitfalls vision token compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b08b3f4d-4c48-4926-b036-b609b075796a",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yWEGHTdPUNFAtbBVMf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19090d98-fb9f-4f36-9140-6079cda2b69d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011To9N7in25KX4odTzR9QU8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 8977,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 8977,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 10 · 2026-05-14T06:18:42.750Z_

<details><summary>↩ Tool result · `toolu_01VrDK5WvHNpxi4eUmygSebB`</summary>

```text
Web search results for query: "arXiv 2505.18227 "Token Reduction Should Go Beyond Efficiency in Generative Models""

Links: [{"title":"[2505.18227] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://arxiv.org/abs/2505.18227"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v1"},{"title":"Token Reduction Should Go Beyond Efficiency in ...","url":"https://arxiv.org/pdf/2505.18227"},{"title":"[2505.18227v2] Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://arxiv.org/abs/2505.18227v2"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250518227K/abstract"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.18227v2"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"(PDF) Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://www.researchgate.net/publication/392104162_Token_Reduction_Should_Go_Beyond_Efficiency_in_Generative_Models_--_From_Vision_Language_to_Multimodality"},{"title":"Token Reduction","url":"https://www.aussieai.com/research/token-reduction"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality","url":"https://www.catalyzex.com/paper/token-reduction-should-go-beyond-efficiency"}]

I found the paper arXiv 2505.18227. Here's a summary of what the search revealed:

## Paper Overview

The paper is titled "Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality" and was submitted on May 23, 2025, with the latest version (v3) revised on January 12, 2026. The authors include Zhenglun Kong and 9 other co-authors.

## Main Argument

The paper argues that token reduction should transcend its traditional efficiency-oriented role in the era of large generative models, and positions it as a fundamental principle in generative modeling, critically influencing both model architecture and broader applications.

## Key Contributions

Across vision, language, and multimodal systems, the paper contends that token reduction can: (i) facilitate deeper multimodal integration and alignment, (ii) mitigate "overthinking" and hallucinations, (iii) maintain coherence over long inputs, and (iv) enhance training stability.

## Background

Token reduction has primarily been used as an efficiency strategy due to the quadratic computational complexity of transformer self-attention mechanisms, helping to balance computational costs, memory usage, and inference latency.

The paper also maintains a GitHub repository called "Awesome-Collection-Token-Reduction" that collects various token reduction techniques for machine learning and AI applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "816745c1-3f2b-4538-94d6-dba503dd3ce8",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "5f17fe97-e165-4729-a581-60fd51edb594",
  "sourceToolAssistantUUID": "816745c1-3f2b-4538-94d6-dba503dd3ce8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T06:18:44.445Z_

<details><summary>↩ Tool result · `toolu_017vnY3H6Yu52xGegk3uvSaS`</summary>

```text
Web search results for query: "arXiv 2601.12042 "Less Is More Until It Breaks" security pitfalls vision token compression"

Links: [{"title":"Less Is More — Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models","url":"https://arxiv.org/html/2601.12042"},{"title":"[2601.12042] Less Is More -- Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models","url":"https://arxiv.org/abs/2601.12042"},{"title":"(PDF) Less Is More -- Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models","url":"https://www.researchgate.net/publication/399931955_Less_Is_More_--_Until_It_Breaks_Security_Pitfalls_of_Vision_Token_Compression_in_Large_Vision-Language_Models"},{"title":"[2601.20742] Compression Tells Intelligence: Visual Coding, Visual Token Technology, and the Unification","url":"https://arxiv.org/abs/2601.20742"},{"title":"Vision-centric Token Compression in Large Language Model","url":"https://arxiv.org/html/2502.00791v2"},{"title":"[2601.22674] VisionTrim: Unified Vision Token Compression for Training-Free MLLM Acceleration","url":"https://arxiv.org/abs/2601.22674"},{"title":"[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/abs/2601.21531"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v3"},{"title":"Vision Token Reduction via Attention-Driven Self-Compression for Efficient Multimodal Large Language Models","url":"https://arxiv.org/html/2602.12618v1"},{"title":"Towards Lossless Ultimate Vision Token Compression for VLMs","url":"https://arxiv.org/html/2512.09010"}]

I found the paper arXiv 2601.12042. Here's what the research reveals:

**Paper Summary:**

The paper is titled "Less Is More -- Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models" by Xiaomei Zhang and colleagues, and was submitted on January 17, 2026.

**Main Findings:**

The research reveals that visual token compression substantially degrades the robustness of LVLMs: models that are robust under uncompressed inference become highly vulnerable once compression is enabled. 

These vulnerabilities are state-specific; failure modes emerge only in the compressed setting and completely disappear when compression is disabled, making them particularly hidden and difficult to diagnose.

**Context:**

Visual token compression is widely adopted to improve the inference efficiency of Large Vision-Language Models (LVLMs), enabling their deployment in latency-sensitive and resource-constrained scenarios. However, existing work has mainly focused on efficiency and performance, while the security implications of visual token compression remain largely unexplored.

The paper highlights a critical security trade-off: while compression improves efficiency, it introduces hidden vulnerabilities that don't exist in uncompressed models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19090d98-fb9f-4f36-9140-6079cda2b69d",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "a019a046-abcc-47f8-83f4-5ea5ca56c2a0",
  "sourceToolAssistantUUID": "19090d98-fb9f-4f36-9140-6079cda2b69d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T06:18:46.637Z_

<details><summary>↩ Tool result · `toolu_01C9SodbaxbCRzGxTEJ2tgxJ`</summary>

```text
Web search results for query: "arXiv 2601.21531 adversarial robustness large VLMs visual token compression"

Links: [{"title":"[2601.21531] On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/abs/2601.21531"},{"title":"On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression","url":"https://arxiv.org/html/2601.21531"},{"title":"Less Is More — Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models","url":"https://arxiv.org/html/2601.12042"},{"title":"Dynamic Token Reweighting for Robust Vision-Language Models","url":"https://arxiv.org/html/2505.17132"},{"title":"Proxy Robustness in Vision Language Models is Effortlessly Transferable","url":"https://arxiv.org/html/2601.12865"},{"title":"Towards Adversarially Robust Vision-Language Models: Insights from Design Choices and Prompt Formatting Techniques","url":"https://arxiv.org/html/2407.11121v1"},{"title":"VEAttack: Downstream-agnostic Vision Encoder Attack against Large Vision Language Models","url":"https://arxiv.org/html/2505.17440"},{"title":"On Evaluating Adversarial Robustness of Large Vision-Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/a97b58c4f7551053b0512f92244b0810-Paper-Conference.pdf"},{"title":"[2305.16934] On Evaluating Adversarial Robustness of Large Vision-Language Models","url":"https://arxiv.org/abs/2305.16934"},{"title":"Towards Lossless Ultimate Vision Token Compression for VLMs","url":"https://arxiv.org/html/2512.09010"}]

Based on the search results, I found the paper you're looking for. Here's the information about arXiv 2601.21531:

## Paper Overview

Visual token compression is widely used to accelerate large vision-language models (LVLMs) by pruning or merging visual tokens, yet its adversarial robustness remains unexplored.

## Main Findings

Existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck.

## Proposed Solution

To address this gap, the researchers propose the Compression-AliGnEd attack (CAGE), which aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget.

CAGE combines (i) expected feature disruption, which concentrates distortion on tokens likely to survive across plausible budgets, and (ii) rank distortion alignment, which actively aligns token distortions with rank scores to promote the retention of highly distorted evidence.

## Key Results

Across diverse representative plug-and-play compression mechanisms and datasets, the results show that CAGE consistently achieves lower robust accuracy than the baseline. This work highlights that robustness assessments ignoring compression can be overly optimistic, calling for compression-aware security evaluation and defenses for efficient LVLMs.

The paper was published on January 29, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b08b3f4d-4c48-4926-b036-b609b075796a",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "41ed270b-c432-4089-a559-3d7dbc06304d",
  "sourceToolAssistantUUID": "b08b3f4d-4c48-4926-b036-b609b075796a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T06:18:49.670Z_

Good, all three papers exist. Now let me fetch the actual pages for more detailed information on each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41ed270b-c432-4089-a559-3d7dbc06304d",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yXDbPJqWEmjdG6uQYo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f44a2504-977f-4fa9-959b-9908497910a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2MjNdgmrRnVnorCYi13Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 10886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2003,
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

_source line 14 · 2026-05-14T06:18:52.506Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019HG9MpoxqALZqMXsp4nHFs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.18227v2",
  "prompt": "Extract the full abstract. Is this a position paper or survey paper? Does it propose concrete new methods or is it purely a position/survey paper? Does it mention VLAs (vision-language-action models) or robotics anywhere? List the authors and their affiliations. What are the main sections/arguments of the paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f44a2504-977f-4fa9-959b-9908497910a6",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yXDbPJqWEmjdG6uQYo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4c35e81-703d-4323-b587-57275ce7a455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2MjNdgmrRnVnorCYi13Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 10886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2003,
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

_source line 15 · 2026-05-14T06:18:53.972Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BuTjvWkUzXpjxJALDrPq2a`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.21531",
  "prompt": "Extract the full abstract. What are the main conclusions? Does token compression hurt or help adversarial robustness? What is CAGE? What are the key experimental results? List the authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4c35e81-703d-4323-b587-57275ce7a455",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yXDbPJqWEmjdG6uQYo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aabc7107-34ad-4060-951f-568af0d48b3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2MjNdgmrRnVnorCYi13Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 10886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2003,
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

_source line 16 · 2026-05-14T06:18:54.938Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WPYc5JR5vCukNSPf8bsjJU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.12042",
  "prompt": "Extract the full abstract. What are the main conclusions about security pitfalls of vision token compression? Does compression hurt robustness? What specific vulnerabilities does it introduce? List the authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aabc7107-34ad-4060-951f-568af0d48b3a",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yXDbPJqWEmjdG6uQYo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12b2b5ce-d815-46f8-ba59-e8eaddb3a862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2MjNdgmrRnVnorCYi13Ce",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 10886,
      "output_tokens": 381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2003
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 851,
          "output_tokens": 381,
          "cache_read_input_tokens": 10886,
          "cache_creation_input_tokens": 2003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2003,
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

_source line 17 · 2026-05-14T06:18:59.582Z_

<details><summary>↩ Tool result · `toolu_019HG9MpoxqALZqMXsp4nHFs`</summary>

```text
# Paper Analysis: Token Reduction in Generative Models

## Full Abstract
"In Transformer architectures, tokens are formed by segmenting inputs into fixed-length chunks. Each token is then mapped to an embedding, enabling parallel attention computations while preserving the input's essential information. Due to the quadratic computational complexity of transformer self-attention mechanisms, token reduction has primarily been used as an efficiency strategy. This is especially true in single vision and language domains, where it helps balance computational costs, memory usage, and inference latency. Despite these advances, this paper argues that token reduction should transcend its traditional efficiency-oriented role in the era of large generative models. Instead, we position it as a fundamental principle in generative modeling, critically influencing both model architecture and broader applications. Specifically, we contend that across vision, language, and multimodal systems, token reduction can: (i) facilitate deeper multimodal integration and alignment, (ii) mitigate "overthinking" and hallucinations, (iii) maintain coherence over long inputs, and (iv) enhance training stability, etc."

## Paper Classification
**Position/Survey Paper** — This work primarily advocates reconceptualizing token reduction beyond efficiency and outlines future research directions, rather than proposing concrete novel methods.

## VLAs and Robotics
No mention of vision-language-action models or robotics applications appears in the provided content.

## Authors and Affiliations
The webpage lists 10 authors (Zhenglun Kong, Yize Li, Fanhu Zeng, Lei Xin, Shvat Messica, Xue Lin, Pu Zhao, Manolis Kellis, Hao Tang, Marinka Zitnik) but does **not provide explicit affiliation information** in this excerpt.

## Main Arguments
The paper reframes token reduction as:
- Facilitating multimodal integration
- Reducing model hallucinations
- Improving long-context coherence
- Enhancing training stability
- Informing new architectures and learning strategies
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4c35e81-703d-4323-b587-57275ce7a455",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "ef9530b6-2eed-458e-9bf0-eac4775b8eef",
  "sourceToolAssistantUUID": "b4c35e81-703d-4323-b587-57275ce7a455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T06:18:59.981Z_

<details><summary>↩ Tool result · `toolu_01WPYc5JR5vCukNSPf8bsjJU`</summary>

```text
# Vision Token Compression Security Analysis

## Full Abstract

"Visual token compression is widely adopted to improve the inference efficiency of Large Vision-Language Models (LVLMs), enabling their deployment in latency-sensitive and resource-constrained scenarios. However, existing work has mainly focused on efficiency and performance, while the security implications of visual token compression remain largely unexplored. In this work, we first reveal that visual token compression substantially degrades the robustness of LVLMs: models that are robust under uncompressed inference become highly vulnerable once compression is enabled. These vulnerabilities are state-specific; failure modes emerge only in the compressed setting and completely disappear when compression is disabled, making them particularly hidden and difficult to diagnose. By analyzing the key stages of the compression process, we identify instability in token importance ranking as the primary cause of this robustness degradation. Small and imperceptible perturbations can significantly alter token rankings, leading the compression mechanism to mistakenly discard task-critical information and ultimately causing model failure."

## Main Conclusions

**Does compression hurt robustness?** Yes, substantially. The research demonstrates that previously robust models become "highly vulnerable once compression is enabled," revealing a previously overlooked efficiency-security trade-off.

**Specific vulnerabilities introduced:**
- State-specific failure modes appearing exclusively in compressed settings
- Instability in token importance ranking mechanisms
- Susceptibility to small perturbations that alter token selection
- Unintended discard of task-critical visual information

## Authors

1. Xiaomei Zhang
2. Zhaoxi Zhang
3. Leo Yu Zhang
4. Yanjun Zhang
5. Guanhong Tao
6. Shirui Pan
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12b2b5ce-d815-46f8-ba59-e8eaddb3a862",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "68e27e28-4264-40c1-97af-cfc619b68328",
  "sourceToolAssistantUUID": "12b2b5ce-d815-46f8-ba59-e8eaddb3a862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T06:19:02.544Z_

<details><summary>↩ Tool result · `toolu_01BuTjvWkUzXpjxJALDrPq2a`</summary>

```text
# Paper Summary: Adversarial Robustness of LVLMs under Visual Token Compression

## Full Abstract
"Visual token compression is widely used to accelerate large vision-language models (LVLMs) by pruning or merging visual tokens, yet its adversarial robustness remains unexplored. We show that existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck. To address this gap, we propose the Compression-AliGnEd attack (CAGE), which aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget. CAGE combines (i) expected feature disruption, which concentrates distortion on tokens likely to survive across plausible budgets, and (ii) rank distortion alignment, which actively aligns token distortions with rank scores to promote the retention of highly distorted evidence. Across diverse representative plug-and-play compression mechanisms and datasets, our results show that CAGE consistently achieves lower robust accuracy than the baseline. This work highlights that robustness assessments ignoring compression can be overly optimistic, calling for compression-aware security evaluation and defenses for efficient LVLMs."

## Main Conclusions
Token compression **hurts adversarial robustness**. Standard attacks overestimate how robust compressed models actually are due to a mismatch between optimization and inference phases.

## What is CAGE?
CAGE (Compression-AliGnEd attack) is a novel attack method designed to evaluate robustness by aligning adversarial perturbation optimization with the actual token-compression process used during inference.

## Key Experimental Results
CAGE consistently achieves lower robust accuracy compared to baseline attacks across multiple compression mechanisms and datasets, demonstrating that compression-naive robustness evaluations are "overly optimistic."

## Authors
Xinwei Zhang, Hangcheng Liu, Li Bai, Hao Wang, Qingqing Ye, Tianwei Zhang, Haibo Hu
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aabc7107-34ad-4060-951f-568af0d48b3a",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "288110cd-13b4-4459-9425-954ff9b638cb",
  "sourceToolAssistantUUID": "aabc7107-34ad-4060-951f-568af0d48b3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-14T06:19:05.837Z_

Now let me get more detail on the first paper -- specifically whether it mentions robotics/VLAs and whether it proposes concrete methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "288110cd-13b4-4459-9425-954ff9b638cb",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yYPYwoeUAo7jAkfmFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51da0b85-1338-4879-a376-4108f2a5213a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkC9WiCvjz2m29w5cHBZTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 403,
      "cache_creation_input_tokens": 2323,
      "cache_read_input_tokens": 12889,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2323,
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

_source line 21 · 2026-05-14T06:19:08.232Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016sWtwrd5UMYpfj5g8HQ84y`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.18227v1",
  "prompt": "Does this paper mention VLAs (vision-language-action models), robotics, or embodied AI anywhere? Does it propose any concrete new methods or algorithms, or is it purely a position/survey paper that reviews existing work and argues for a new perspective? Look for any section that introduces a novel technique, architecture, or algorithm. Also look for the paper's table of contents or section headings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51da0b85-1338-4879-a376-4108f2a5213a",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yYPYwoeUAo7jAkfmFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8be3aa88-be32-4bf1-9326-0640df0571b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkC9WiCvjz2m29w5cHBZTo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 403,
      "cache_creation_input_tokens": 2323,
      "cache_read_input_tokens": 12889,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2323
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 403,
          "output_tokens": 196,
          "cache_read_input_tokens": 12889,
          "cache_creation_input_tokens": 2323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2323,
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

_source line 22 · 2026-05-14T06:19:12.797Z_

<details><summary>↩ Tool result · `toolu_016sWtwrd5UMYpfj5g8HQ84y`</summary>

```text
# Analysis of the Paper

## VLAs, Robotics, and Embodied AI

The paper makes **minimal mention** of robotics or embodied AI. There is only one brief reference in Section 5.5 (Dense Prediction Tasks for Vision):

> "robotic control [wang2024sparse](https://arxiv.org/html/2505.18227v1#bib.bib92) would demand rotation angle according to the grid map"

This mentions robotic applications requiring dense predictions but doesn't discuss vision-language-action models or embodied AI specifically.

## Novel Methods vs. Position Paper

This is **primarily a position and survey paper**—not a methodological contribution. Evidence:

- The paper explicitly identifies itself as a "position paper" in the abstract
- No new algorithms, architectures, or techniques are proposed
- Section headings focus on "Challenges and Positions" and "Future Directions" rather than novel method contributions
- The paper reviews existing token reduction work across domains and argues for reconceptualizing token reduction beyond efficiency
- Section 5 outlines promising future research directions but doesn't implement them

The paper's core argument is that token reduction should transcend efficiency optimization to address broader challenges in generative modeling—a conceptual reframing rather than a methodological advance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be3aa88-be32-4bf1-9326-0640df0571b2",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae99e5842e9853108",
  "type": "user",
  "uuid": "4f46db57-0681-44b1-9037-0fb2e1af2fc4",
  "sourceToolAssistantUUID": "8be3aa88-be32-4bf1-9326-0640df0571b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T06:19:36.532Z_

Now I have comprehensive information on all three papers. Here is my complete verification report:

---

## Paper 1: arXiv 2505.18227 -- "Token Reduction Should Go Beyond Efficiency in Generative Models -- From Vision, Language to Multimodality"

**Does it exist?** Yes, confirmed. Available at [arxiv.org/abs/2505.18227](https://arxiv.org/abs/2505.18227). Authors: Zhenglun Kong, Yize Li, Fanhu Zeng, Lei Xin, Shvat Messica, Xue Lin, Pu Zhao, Manolis Kellis, Hao Tang, Marinka Zitnik. Originally submitted May 23, 2025, with a v2 revision.

**Is it a position/survey paper?** Yes. It explicitly identifies itself as a position paper. It reviews existing token reduction work across vision, language, and multimodal systems and argues for a conceptual reframing. It does not propose any novel algorithms, architectures, or methods.

**What does it argue about token reduction beyond efficiency?** The paper contends that token reduction should transcend its traditional role as a pure efficiency strategy and instead be seen as a "fundamental principle in generative modeling." Specifically, it argues token reduction can: (i) facilitate deeper multimodal integration and alignment, (ii) mitigate "overthinking" and hallucinations, (iii) maintain coherence over long inputs, and (iv) enhance training stability.

**Does it propose concrete methods?** No. It is purely a position/survey paper. Section 5 outlines future research directions but does not implement any of them.

**Does it mention VLAs or robotics?** Only minimally. There is one brief reference in Section 5.5 (Dense Prediction Tasks for Vision) mentioning "robotic control" in the context of dense predictions. It does not discuss vision-language-action (VLA) models or embodied AI in any substantive way.

---

## Paper 2: arXiv 2601.21531 -- "On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression"

**Does it exist?** Yes, confirmed. Available at [arxiv.org/abs/2601.21531](https://arxiv.org/abs/2601.21531). Authors: Xinwei Zhang, Hangcheng Liu, Li Bai, Hao Wang, Qingqing Ye, Tianwei Zhang, Haibo Hu. Published January 29, 2026.

**What does it conclude about token compression and robustness?** The paper shows that existing encoder-based adversarial attacks **substantially overestimate** the robustness of compressed LVLMs. The root cause is an "optimization-inference mismatch": adversarial perturbations are optimized on the full-token representation, but inference runs through a token-compression bottleneck. When attacks are properly aligned with compression (via their proposed CAGE method), compressed models show **lower robust accuracy** than previously believed. The core conclusion is that robustness assessments ignoring compression are "overly optimistic," and compression-aware security evaluation is needed.

**Key nuance:** This paper does NOT simply say "compression makes models less robust." Rather, it says that standard robustness evaluations of compressed models are misleadingly optimistic because the attacks aren't properly accounting for the compression bottleneck. When you use compression-aware attacks (CAGE), the models are revealed to be less robust than thought.

---

## Paper 3: arXiv 2601.12042 -- "Less Is More -- Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models"

**Does it exist?** Yes, confirmed. Available at [arxiv.org/abs/2601.12042](https://arxiv.org/abs/2601.12042). Authors: Xiaomei Zhang, Zhaoxi Zhang, Leo Yu Zhang, Yanjun Zhang, Guanhong Tao, Shirui Pan. Submitted January 17, 2026.

**What does it conclude?** This paper is more direct in its finding: visual token compression **substantially degrades** the robustness of LVLMs. Models that are robust under uncompressed inference become "highly vulnerable" once compression is enabled. The key findings:

- Vulnerabilities are **state-specific**: failure modes emerge only in the compressed setting and completely disappear when compression is disabled, making them hidden and hard to diagnose.
- The root cause is **instability in token importance ranking**: small, imperceptible perturbations can significantly alter which tokens get ranked as important, causing the compression mechanism to mistakenly discard task-critical information.
- This reveals a previously overlooked **efficiency-security trade-off** in visual token compression.

---

## Summary of the Three Papers Together

All three papers are real and verified. The position paper (2505.18227) argues optimistically that token reduction has benefits beyond efficiency. The two January 2026 papers (2601.21531 and 2601.12042) serve as counter-evidence, both demonstrating that token compression introduces serious security/robustness vulnerabilities in VLMs -- though from slightly different angles. Paper 2601.21531 focuses on showing that standard robustness evaluations are misleadingly optimistic for compressed models, while 2601.12042 more directly shows that compression itself degrades robustness through token ranking instability.

Sources:
- [arXiv 2505.18227 - Token Reduction Should Go Beyond Efficiency](https://arxiv.org/abs/2505.18227)
- [arXiv 2505.18227v2](https://arxiv.org/abs/2505.18227v2)
- [arXiv 2505.18227 HTML](https://arxiv.org/html/2505.18227v1)
- [arXiv 2601.21531 - Adversarial Robustness under Visual Token Compression](https://arxiv.org/abs/2601.21531)
- [arXiv 2601.12042 - Less Is More Until It Breaks](https://arxiv.org/abs/2601.12042)
- [Awesome-Collection-Token-Reduction GitHub](https://github.com/ZLKong/Awesome-Collection-Token-Reduction)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f46db57-0681-44b1-9037-0fb2e1af2fc4",
  "isSidechain": true,
  "agentId": "ae99e5842e9853108",
  "requestId": "req_011Cb1yZ9PBcqCW78R4nJvza",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1785e41f-b29f-4d8e-b645-3459dbb75c52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YhwLNFsUi34g1SxjyFzc7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 15212,
      "output_tokens": 1479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 894
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1479,
          "cache_read_input_tokens": 15212,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 894,
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
