# Research conversation: I need to understand the paper "Internal Attention Divergence Signals" by van Dijk (arXiv 2605.05025, May 2026). Please:

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a525bf697c9ec78a9.jsonl`
- **Structured JSON:** [`6482c711b9bfd1d74269.json`](../../sessions/64/6482c711b9bfd1d74269.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-16T09:31:58.499Z_

I need to understand the paper "Internal Attention Divergence Signals" by van Dijk (arXiv 2605.05025, May 2026). 

Please:
1. Use WebFetch to read the paper at https://arxiv.org/abs/2605.05025
2. Search for "attention divergence hallucination detection entity" and "arXiv 2605.05025"

I need to understand:
- What is their method? How do they use KL divergence of attention heads?
- What models and benchmarks do they evaluate on?
- What results do they achieve?
- Do they propose any intervention/mitigation, or just detection?
- How does it relate to using residual stream probes for hallucination detection?

Report with specific numbers and methodological details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a525bf697c9ec78a9",
  "type": "user",
  "uuid": "bd3fd1fa-2901-4e43-bf17-8cec65731521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:31:58.503Z_

```json
{
  "parentUuid": "bd3fd1fa-2901-4e43-bf17-8cec65731521",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
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
  "uuid": "6c48aee2-2c6f-4723-b9fc-1b0958e676a7",
  "timestamp": "2026-05-16T09:31:58.503Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T09:32:01.200Z_



I'll start by fetching the paper and searching for related information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c48aee2-2c6f-4723-b9fc-1b0958e676a7",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61sY3wxNq8XgA6LpcEn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec208c91-e042-4782-9dea-a3db537d578f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnqLAqfJahcCT74BKCLDEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 729,
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

_source line 4 · 2026-05-16T09:32:01.565Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01U7n3e1xyYQWVkKNLs1Yrd8`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec208c91-e042-4782-9dea-a3db537d578f",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61sY3wxNq8XgA6LpcEn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1266d6e8-64c0-49d6-a327-ea90bdd6af0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnqLAqfJahcCT74BKCLDEP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 8223,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 729
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 729,
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

_source line 5 · 2026-05-16T09:32:01.568Z_

<details><summary>↩ Tool result · `toolu_01U7n3e1xyYQWVkKNLs1Yrd8`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "1266d6e8-64c0-49d6-a327-ea90bdd6af0d",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a525bf697c9ec78a9",
  "type": "user",
  "uuid": "7d1c9870-a7f1-40b9-bbbf-a1c76efeb8e7",
  "sourceToolAssistantUUID": "1266d6e8-64c0-49d6-a327-ea90bdd6af0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T09:32:03.932Z_



Now let me fetch the paper and run searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d1c9870-a7f1-40b9-bbbf-a1c76efeb8e7",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61smGC1dhETqetT5oTs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "128001a9-b27d-4218-85f6-cf2dab803990",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgXJ9rf39JLSmNJGY6XyLq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 7 · 2026-05-16T09:32:05.559Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WPJz1YXr2YaWsQRaLxwnXK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05025",
  "prompt": "Extract ALL details from this paper page including: full title, authors, abstract, and any content available. I need the complete abstract and any methodology details visible on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "128001a9-b27d-4218-85f6-cf2dab803990",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61smGC1dhETqetT5oTs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d91e167f-8632-402a-bc08-aaeb640d7a8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgXJ9rf39JLSmNJGY6XyLq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 8 · 2026-05-16T09:32:05.567Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012URKEUFGDdLXCNNtVZTL7o`</summary>

```json
{
  "query": "attention divergence hallucination detection entity arXiv 2605.05025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d91e167f-8632-402a-bc08-aaeb640d7a8a",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61smGC1dhETqetT5oTs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69f5ff5f-9dee-4751-b30e-5cb9d062d0b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgXJ9rf39JLSmNJGY6XyLq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1904,
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

_source line 9 · 2026-05-16T09:32:06.025Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WLrdWSSrGn4Cs3p6MsyQyp`</summary>

```json
{
  "query": "\"van Dijk\" \"Internal Attention Divergence Signals\" hallucination detection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69f5ff5f-9dee-4751-b30e-5cb9d062d0b5",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61smGC1dhETqetT5oTs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "056bbd66-be03-4c6c-9371-04a186ae463c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgXJ9rf39JLSmNJGY6XyLq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1904,
      "cache_read_input_tokens": 8952,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 238,
          "cache_read_input_tokens": 8952,
          "cache_creation_input_tokens": 1904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1904,
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

_source line 10 · 2026-05-16T09:32:10.145Z_

<details><summary>↩ Tool result · `toolu_01WPJz1YXr2YaWsQRaLxwnXK`</summary>

```text
# Paper Details: Hallucination Detection in LLMs

**Full Title:** "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals"

**Author:** Gijs van Dijk

**ArXiv ID:** 2605.05025

**Submission Date:** May 6, 2026

**Field:** Computer Science - Computation and Language (cs.CL)

**Venue:** ACL SRW 2026

## Abstract Summary

The research presents a lightweight uncertainty quantification approach that detects hallucinations without requiring repeated sampling or external models. The method leverages attention matrices to identify unreliable outputs.

**Key Methodology Elements:**
- Measures Kullback-Leibler divergence between individual attention head distributions and uniform reference distributions
- Employs logistic regression probes using these divergence features
- Demonstrates effectiveness across multiple datasets, task types, and model families

**Key Findings:**
The authors report that "attention divergence is highly predictive of answer correctness" and performs competitively with existing uncertainty methods. The signal concentrates in middle layers and focuses on factual tokens (named entities, numbers), indicating attention dynamics provides an "efficient and interpretable white-box signal of model uncertainty."

**Access:** PDF and HTML versions available; licensed under CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d91e167f-8632-402a-bc08-aaeb640d7a8a",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a525bf697c9ec78a9",
  "type": "user",
  "uuid": "7272a71d-90af-43ef-9e77-77a31ef5d716",
  "sourceToolAssistantUUID": "d91e167f-8632-402a-bc08-aaeb640d7a8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T09:32:10.996Z_

<details><summary>↩ Tool result · `toolu_012URKEUFGDdLXCNNtVZTL7o`</summary>

```text
Web search results for query: "attention divergence hallucination detection entity arXiv 2605.05025"

Links: [{"title":"[2605.05025] Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/abs/2605.05025"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"(PDF) Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://www.researchgate.net/publication/390772361_Hallucination_Detection_in_LLMs_via_Topological_Divergence_on_Attention_Graphs"},{"title":"Neural Message-Passing on Attention Graphs for Hallucination Detection","url":"https://arxiv.org/html/2509.24770v1"},{"title":"Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v3"},{"title":"Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://arxiv.org/html/2504.10063v1"},{"title":"[2504.10063] Hallucination Detection in LLMs with Topological Divergence on Attention Graphs","url":"https://arxiv.org/abs/2504.10063"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Cross-Layer Attention Probing for Fine-Grained Hallucination Detection","url":"https://arxiv.org/html/2509.09700v1/"},{"title":"[2605.07209] Hallucination Detection via Activations of Open-Weight Proxy Analyzers","url":"https://arxiv.org/abs/2605.07209"}]

I found the paper you're looking for! Here's the information about arXiv paper 2605.05025:

## Paper Summary

The paper proposes a lightweight and single-pass uncertainty quantification method for detecting hallucinations in Large Language Models. 

**Methodology:**
The method uses attention matrices to estimate uncertainty without requiring repeated sampling or external models, specifically measuring the Kullback-Leibler divergence between each attention head's distribution and a uniform reference distribution, and using these features in a logistic regression probe.

**Key Findings:**
Across multiple datasets, task types, and model families, attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods. The signal is concentrated in middle layers and on factual tokens such as named entities and numbers, suggesting that attention dynamics provides an efficient and interpretable white-box signal of model uncertainty.

The paper was authored by Gijs van Dijk from Utrecht University and was submitted on May 6, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69f5ff5f-9dee-4751-b30e-5cb9d062d0b5",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a525bf697c9ec78a9",
  "type": "user",
  "uuid": "d5c161cc-57f3-42c9-9bda-8c34eda2c540",
  "sourceToolAssistantUUID": "69f5ff5f-9dee-4751-b30e-5cb9d062d0b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:32:12.244Z_

<details><summary>↩ Tool result · `toolu_01WLrdWSSrGn4Cs3p6MsyQyp`</summary>

```text
Web search results for query: ""van Dijk" "Internal Attention Divergence Signals" hallucination detection 2026"

Links: [{"title":"[2605.05025] Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/abs/2605.05025"},{"title":"Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals","url":"https://arxiv.org/html/2605.05025"},{"title":"Diverging Towards Hallucination: Detection of Failures in Vision-Language Models via Multi-token Aggregation","url":"https://arxiv.org/html/2505.11741v1"},{"title":"MTRE: Multi-Token Reliability Estimation for Hallucination Detection in VLMs","url":"https://arxiv.org/html/2505.11741"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/56cd8de3cdfac73a341ef100cfab1170dac057eb.pdf"},{"title":"[Literature Review] Hallucination Detection in LLMs Using Spectral Features of Attention Maps","url":"https://www.themoonlight.io/en/review/hallucination-detection-in-llms-using-spectral-features-of-attention-maps"},{"title":"Hallucination Detection in LLMs with Topological Divergence on ...","url":"https://www.semanticscholar.org/paper/1ec4be9cd511fc87e66e15233c16fa177c10aa86"},{"title":"(PDF) Hallucination Detection in LLMs via Topological Divergence on Attention Graphs","url":"https://www.researchgate.net/publication/390772361_Hallucination_Detection_in_LLMs_via_Topological_Divergence_on_Attention_Graphs"},{"title":"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2604.10697"},{"title":"Self-Consistency and Probe-Based Hallucination Detection","url":"https://www.emergentmind.com/topics/self-consistency-probe-based-hallucination-detection"}]

Based on the search results, I found research on this topic. The paper "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals" is by Gijs van Dijk, and it was submitted on May 6, 2026.

The work proposes a lightweight and single-pass uncertainty quantification method for detecting hallucinations in Large Language Models that uses attention matrices to estimate uncertainty without requiring repeated sampling or external models. Specifically, the method measures the Kullback-Leibler divergence between each attention head's distribution and a uniform reference distribution, and uses these features in a logistic regression probe.

Across multiple datasets, task types, and model families, attention divergence is highly predictive of answer correctness and performs competitively with existing uncertainty estimation methods, with the signal concentrated in middle layers and on factual tokens such as named entities and numbers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "056bbd66-be03-4c6c-9371-04a186ae463c",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a525bf697c9ec78a9",
  "type": "user",
  "uuid": "4444aa43-2d8a-41cf-8792-c4f550a36111",
  "sourceToolAssistantUUID": "056bbd66-be03-4c6c-9371-04a186ae463c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-16T09:32:16.637Z_

Good, I have the abstract-level information. Now let me fetch the full HTML version of the paper for detailed methodology, results, and numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4444aa43-2d8a-41cf-8792-c4f550a36111",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61taAyH8rt359F1CYwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1363db3-da6a-4112-b04b-d3e76202a68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAdNC71N6HwaQ1exxeRuFx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 10856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2154,
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

_source line 14 · 2026-05-16T09:32:21.575Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TxUMe2STZ8sm4Zcz74VxUT`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05025",
  "prompt": "Extract ALL detailed information from this paper. I need:\n1. EXACT methodology: how KL divergence is computed from attention heads, the formula, which layers, how the logistic regression probe works, what features are used\n2. ALL models evaluated (exact model names and sizes)\n3. ALL benchmarks/datasets used\n4. ALL numerical results (AUROC, F1, accuracy numbers) in tables\n5. Any intervention or mitigation methods proposed (not just detection)\n6. Any comparison to residual stream probes or other internal representation methods\n7. Layer-wise analysis details - which layers are most informative\n8. Token-level analysis - what types of tokens show the signal\n9. Baselines compared against\n10. Any limitations discussed\nPlease be as complete and specific as possible with numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1363db3-da6a-4112-b04b-d3e76202a68a",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61taAyH8rt359F1CYwN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83933170-a59c-40e2-aba1-c0c3865469ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XAdNC71N6HwaQ1exxeRuFx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 10856,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 10856,
          "cache_creation_input_tokens": 2154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2154,
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

_source line 15 · 2026-05-16T09:32:49.343Z_

<details><summary>↩ Tool result · `toolu_01TxUMe2STZ8sm4Zcz74VxUT`</summary>

```text
# Comprehensive Analysis: Detecting Hallucinations via Attention Divergence Signals

## 1. EXACT METHODOLOGY

**KL Divergence Computation:**
The method measures Kullback-Leibler divergence between attention distributions and uniform baseline:

D_KL(P||U) = Σ_x P(x)log(P(x)/(1/T)) = log T - H(P)

Where T = context window tokens, H(P) = entropy of attention distribution.

**Feature Extraction:**
- For each generation step t, attention head (h) in layer (l): extract distribution A_t^(l,h) over t previous tokens
- Compare to uniform reference U assigning probability 1/T to each position
- Compute KL divergence at each generation step
- **Average across generated answer tokens** (single scalar per head)
- Concatenate into feature vector x ∈ ℝ^(L×H)

**Logistic Regression Probe:**
- Model: P(y_i=1|x_i) = σ(w^T x_i + b)
- Loss function: -Σ[y_i log p_i + (1-y_i)log(1-p_i)] + λ||w||_1
- L1 regularization (lasso) selects sparse subset of heads
- Hyperparameters: regularization strength C=1.0, solver=saga, max iterations=20,000

**Attention Extraction Details:**
- Greedy decoding (T=0, no sampling)
- Post-softmax self-attention matrices
- Full sequence extraction (prompt + generated tokens)
- Small epsilon value for numerical stability

## 2. MODELS EVALUATED

**Three instruction-tuned models:**
1. Llama-3.2-3B-Instruct
2. Qwen3-4B-Instruct
3. Mistral-7B-Instruct-v0.2

(Note: Qwen3-4B designation appears in paper; specific sizing=4B stated)

## 3. BENCHMARKS AND DATASETS

| Dataset | Task Type | Samples | Evaluation |
|---------|-----------|---------|-----------|
| TruthfulQA | Factual QA (multiple-choice) | 272 per seed | MC1 targets, shuffled choices, letter extraction |
| TriviaQA | Open-domain QA | 2,000 | Substring match vs. gold aliases |
| HotpotQA | Multi-hop reasoning | 2,000 | Context truncated to 2048 tokens; string match |
| GSM8K | Math word problems | 1,319 | Numeric answer extraction & comparison |

**Cross-validation:** 5-fold stratified; 3 random seeds

## 4. NUMERICAL RESULTS

**Main Performance (Table 1):**

| Dataset | Model | AUROC ±SD |
|---------|-------|-----------|
| TruthfulQA | Llama-3.2-3B | 0.906±0.024 |
| TruthfulQA | Qwen3-4B | **0.906±0.025** |
| TruthfulQA | Mistral-7B | 0.891±0.024 |
| TriviaQA | Llama-3.2-3B | 0.835±0.004 |
| TriviaQA | Qwen3-4B | **0.846±0.001** |
| TriviaQA | Mistral-7B | 0.835±0.004 |
| HotpotQA | Llama-3.2-3B | **0.8035±0.0219** |
| HotpotQA | Qwen3-4B | 0.7963±0.0217 |
| HotpotQA | Mistral-7B | 0.7782±0.0061 |
| GSM8K | Llama-3.2-3B | 0.7672±0.0305 |
| GSM8K | Qwen3-4B | **0.9450±0.0151** |
| GSM8K | Mistral-7B | 0.7889±0.0270 |

**Extended Results with ECE & Accuracy (Table 7):**
- TruthfulQA: Accuracy 0.801–0.838; ECE 0.201–0.224
- TriviaQA: Accuracy 0.770–0.791; ECE 0.059–0.064
- HotpotQA: Accuracy 0.7613–0.7957; ECE 0.0644–0.0957
- GSM8K: Accuracy 0.7301–0.9166; ECE 0.0439–0.0601

**Comparison to Prior Work (Table 2 - HotpotQA/Mistral-7B):**

| Method | Single Gen. | AUROC ±SD |
|--------|-------------|-----------|
| Ours | Y | **0.78±0.02** |
| TOHA | Y | 0.71±0.08 |
| SelfCheckGPT | N | 0.70±0.06 |
| Semantic entropy | N | 0.70±0.05 |
| EigenScore | N | 0.68±0.04 |
| Max entropy | Y | 0.62±0.04 |
| Perplexity | Y | 0.55±0.06 |

**Comparison to Hidden State Methods (Table 3 - Llama-3.2-3B):**

| Method | TriviaQA | TruthfulQA |
|--------|----------|-----------|
| Ours | 0.835 | **0.906** |
| LapEigvals | **0.836** | 0.829 |
| Hidden States (probe) | 0.850 | 0.823 |

## 5. INTERVENTION/MITIGATION METHODS

**The paper is purely detection-focused.** No mitigation methods proposed. Limitations section notes: approach cannot reduce hallucinations, only identify them. Authors suggest future work could use attention divergence as "training objective" via reinforcement learning penalizing extreme divergence at critical tokens.

## 6. COMPARISON TO ALTERNATIVE INTERNAL REPRESENTATIONS

**Hidden State Probing vs. Attention Methods:**
- Paper cites Orgad et al. (2024), Binkowski et al. (2025), Chen et al. (2024) training probes on hidden states
- States these "often struggle to generalize across tasks and datasets"
- Proposes attention-based approach instead

**No direct comparison to residual stream probes** in this paper, though mentions residual stream interactions in context of head specialization.

## 7. LAYER-WISE ANALYSIS

**Layer Distribution (Table 5 - Percentage of Selected Heads):**

| Model | Early Layers | Middle Layers | Late Layers |
|-------|-------------|---------------|------------|
| Llama-3.2-3B | 15.5% | **53.5%** | 31.0% |
| Qwen3-4B | 28.1% | 35.9% | 35.9% |
| Mistral-7B | 33.8% | **46.3%** | 20.0% |

**Key finding:** "Strongest differences concentrated in middle layers" (Figure 2 heatmap). Signal is distributed across multiple heads rather than localized.

**Ablation Results (Table 4 - TriviaQA/Llama):**
- Removing early layers: AUROC 0.849 (↓ from 0.858 baseline)
- Removing middle layers: AUROC 0.844 (↓ largest drop)
- Removing late layers: AUROC 0.862 (↑)
- Max pooling vs. mean: 0.795 (↓ significant) - indicates signal distributed across multiple spikes, not single peaks

## 8. TOKEN-LEVEL ANALYSIS

**Word-Level Divergence Distribution:**
- Named entities: **High divergence**
- Numeric tokens: **High divergence** (73% of 99th percentile tail)
- Stop words: **Low divergence**
- Punctuation: **Low divergence**, absent from extreme tail

**Extreme Tail Analysis (99th percentile):**
- 961/1445 words are named entities (66.5%)
- 435 other content words (30.1%)
- 33 stop words (2.3%)
- 5 numeric tokens (0.3%)

**Ablation by Sequence Position (TriviaQA/Llama):**
- Prompt-only tokens: AUROC 0.7674
- Answer-only tokens: AUROC **0.8707** (strongest)
- Full generation: AUROC 0.8215

This suggests partial signal exists in prompt (aleatoric uncertainty) but peaks during answer generation.

## 9. BASELINES COMPARED

**Sampling/Ensemble Methods:**
- SelfCheckGPT
- Semantic entropy
- Disagreement-based approaches

**Output-Based Probabilistic Methods:**
- Perplexity
- Maximum token probability
- Output entropy
- Log-likelihood

**Other Attention-Based:**
- TOHA (Topology-based Hallucination detector)
- Lookback Lens (contextual hallucination detection)
- UQAC (Uncertainty Quantification with Attention Chain)

**Spectral/Hidden State Methods:**
- LapEigvals
- Hidden state probes
- EigenScore

**Sanity Checks (Table 6 - TriviaQA/Llama):**
- Generation length: AUROC 0.36
- Prompt length: AUROC 0.44
- Raw output length: AUROC 0.37
- Ends with punctuation: AUROC 0.54
- Number of digits: AUROC 0.48
- (All near-chance or reverse correlations)

## 10. LIMITATIONS DISCUSSED

**Five Main Limitations Stated:**

1. **No Causality:** "Does not establish causal relationship between specific patterns and false generations." Signal distributed across multiple heads; cannot reduce to simple logical rule.

2. **Probe Interpretability:** "Remains difficult to interpret" - should not be viewed as explanation of uncertainty representation, only as extraction tool.

3. **Black-box Inaccessibility:** Requires access to internal attention weights; cannot apply to models providing only text/output probabilities.

4. **Dataset/Family Specificity:** "Combination of heads and layers selected varies across datasets and families," suggesting logistic regression probe may be overly specific.

5. **Cross-dataset Generalization:** No heads appear across all four datasets. Only ~0.5% of total heads selected. Limited overlap across model families (no single head shared across all three models).

**Additional Constraints:**
- Cannot explain how uncertainty represented internally
- Attention divergence itself informative, but probe selection varies significantly

---

**Summary:** Lightweight, single-pass method achieving competitive/superior performance (AUROC 0.78–0.91 across tasks) without sampling overhead. Signal concentrates in middle layers and factual tokens, but lacks causal interpretability and shows poor cross-dataset generalization at head level.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83933170-a59c-40e2-aba1-c0c3865469ce",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a525bf697c9ec78a9",
  "type": "user",
  "uuid": "02072819-1478-4f3a-a16d-3da876a3419f",
  "sourceToolAssistantUUID": "83933170-a59c-40e2-aba1-c0c3865469ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-16T09:32:51.393Z_

Now let me also search for how this relates to residual stream probes specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02072819-1478-4f3a-a16d-3da876a3419f",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61wHLmpn9AdfadjG2qd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1cc26b6-f9a2-4bcc-87ee-a1a9b1708ebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VhTfwEgAK4vfXgpgvRm1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3049,
      "cache_read_input_tokens": 13010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3049,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 17 · 2026-05-16T09:32:52.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014AN7SGsKP5v7ypQYuo8UJE`</summary>

```json
{
  "query": "residual stream probes hallucination detection LLM hidden states 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1cc26b6-f9a2-4bcc-87ee-a1a9b1708ebe",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61wHLmpn9AdfadjG2qd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06390e44-011c-41fc-b14b-d92fafcdf977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015VhTfwEgAK4vfXgpgvRm1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3049,
      "cache_read_input_tokens": 13010,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3049,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 18 · 2026-05-16T09:32:59.392Z_

<details><summary>↩ Tool result · `toolu_014AN7SGsKP5v7ypQYuo8UJE`</summary>

```text
Web search results for query: "residual stream probes hallucination detection LLM hidden states 2025 2026"

Links: [{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable ...","url":"https://aclanthology.org/2025.acl-long.880.pdf"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"A Single Direction of Truth: An Observer Model’s Linear Residual Probe Exposes and Steers Contextual Hallucinations","url":"https://arxiv.org/html/2507.23221v1"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/html/2507.16488"},{"title":"Published as a conference paper at ICLR 2025 REDEEP: DETECTING HALLUCINATION IN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf"},{"title":"Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments","url":"https://arxiv.org/html/2605.03971v1"},{"title":"CORVUS: Red-Teaming Hallucination Detectors via Internal Signal Camouflage in Large Language Models","url":"https://arxiv.org/html/2601.14310"},{"title":"HIVE: Hidden-Evidence Verification for Hallucination Detection in Diffusion Large Language Models","url":"https://arxiv.org/html/2604.26139"}]

I found several recent research papers on using residual stream probes for hallucination detection in LLMs. Here are the key findings:

## Recent Work on Residual Stream Probes for Hallucination Detection

Recent research probes each layer's residual stream to obtain detection scores, then aggregates these scores across all layers to capture global information as input to a probe for hallucination detection.

**ICR Probe (2025):** A novel metric called the ICR Score (Information Contribution to Residual Stream) quantifies the contribution of modules to hidden state updates and is effective in distinguishing hallucinations, with a hallucination detection method called the ICR Probe that captures cross-layer evolution of hidden states. The ICR Probe effectively detects hallucinations across multiple mainstream open-source LLMs and outperforms previous methods across multiple datasets.

**Observer Model Approach (2025):** A generator-agnostic observer model detects hallucinations via a single forward pass and a linear probe on its residual stream.

**PCNet (2026):** PCNet, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream, detects hallucinations as geometric anomalies on the factual manifold through exact Negative Log-Likelihood computation and serves as a dynamic gate distinguishing hallucinated from factual hidden states.

**Generalization Challenges:** While linear and MLP-based probes can predict hallucinations using hidden states, their ability to generalize to more complex settings, such as open-ended long-form generation, remains unproven.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06390e44-011c-41fc-b14b-d92fafcdf977",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a525bf697c9ec78a9",
  "type": "user",
  "uuid": "b90fc151-8da4-40c9-9cd4-f13de54b0274",
  "sourceToolAssistantUUID": "06390e44-011c-41fc-b14b-d92fafcdf977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T09:33:41.469Z_

I now have comprehensive information. Here is the full report.

---

## Report: "Detecting Hallucinations in Large Language Models via Internal Attention Divergence Signals" (van Dijk, arXiv 2605.05025, May 2026)

**Author:** Gijs van Dijk (Utrecht University)
**Venue:** ACL SRW 2026, submitted May 6, 2026

---

### Method: KL Divergence of Attention Heads

The core idea is a **single-pass, lightweight** hallucination detector that requires no repeated sampling and no external models. It works as follows:

1. **Attention extraction:** During greedy decoding (temperature=0), extract post-softmax self-attention matrices from every attention head across all layers, for both prompt and generated tokens.

2. **KL divergence computation:** For each generation step *t*, for each attention head *(l, h)* at layer *l*, the distribution *A_t^{(l,h)}* over previous tokens is compared against a **uniform reference** *U* assigning probability *1/T* to each of the *T* context positions. The KL divergence simplifies to:

   `D_KL(P || U) = log T - H(P)`

   where *H(P)* is the entropy of the attention distribution. High divergence means the head is concentrating attention sharply (low entropy); low divergence means it's attending broadly.

3. **Feature vector construction:** The per-step KL values are **averaged across generated answer tokens**, producing a single scalar per head. These are concatenated into a feature vector *x in R^{L x H}* (number of layers times number of heads).

4. **Logistic regression probe:** A standard logistic regression with **L1 (lasso) regularization** (C=1.0, saga solver, max 20,000 iterations) is trained on these features to predict binary correctness. L1 regularization forces sparsity, selecting only a small subset of heads (approximately 0.5% of total heads are selected).

5. **Evaluation:** 5-fold stratified cross-validation across 3 random seeds.

---

### Models Evaluated

Three instruction-tuned models of varying size and architecture:
- **Llama-3.2-3B-Instruct** (3B parameters)
- **Qwen3-4B-Instruct** (4B parameters)
- **Mistral-7B-Instruct-v0.2** (7B parameters)

---

### Benchmarks

| Dataset | Task Type | Samples | Evaluation Method |
|---------|-----------|---------|-------------------|
| TruthfulQA | Factual QA (multiple-choice) | 272 per seed | MC1 targets, shuffled choices, letter extraction |
| TriviaQA | Open-domain QA | 2,000 | Substring match vs. gold aliases |
| HotpotQA | Multi-hop reasoning | 2,000 | Context truncated to 2048 tokens; string match |
| GSM8K | Math word problems | 1,319 | Numeric answer extraction and comparison |

---

### Results

**Main AUROC scores (Table 1):**

| Dataset | Llama-3.2-3B | Qwen3-4B | Mistral-7B |
|---------|-------------|----------|------------|
| TruthfulQA | 0.906 +/- 0.024 | 0.906 +/- 0.025 | 0.891 +/- 0.024 |
| TriviaQA | 0.835 +/- 0.004 | 0.846 +/- 0.001 | 0.835 +/- 0.004 |
| HotpotQA | 0.804 +/- 0.022 | 0.796 +/- 0.022 | 0.778 +/- 0.006 |
| GSM8K | 0.767 +/- 0.031 | 0.945 +/- 0.015 | 0.789 +/- 0.027 |

**Comparison vs. prior methods on HotpotQA / Mistral-7B (Table 2):**

| Method | Single Generation? | AUROC |
|--------|--------------------|-------|
| **Attention Divergence (theirs)** | **Yes** | **0.78** |
| TOHA | Yes | 0.71 |
| SelfCheckGPT | No (multiple samples) | 0.70 |
| Semantic entropy | No (multiple samples) | 0.70 |
| EigenScore | No (multiple samples) | 0.68 |
| Max entropy | Yes | 0.62 |
| Perplexity | Yes | 0.55 |

The method beats all baselines, and critically beats all single-generation methods by a substantial margin (7+ AUROC points over TOHA). It also beats sampling-based methods that require multiple forward passes.

**Comparison vs. hidden state methods on Llama-3.2-3B (Table 3):**

| Method | TriviaQA | TruthfulQA |
|--------|----------|------------|
| Attention Divergence (theirs) | 0.835 | **0.906** |
| LapEigvals (spectral) | **0.836** | 0.829 |
| Hidden state probe | 0.850 | 0.823 |

On TruthfulQA, attention divergence substantially outperforms hidden state probes (0.906 vs. 0.823). On TriviaQA, the methods are roughly comparable, with hidden state probes slightly ahead.

---

### Layer-Wise and Token-Level Analysis

**Layer importance (percentage of selected heads by L1 regularization):**

| Model | Early Layers | Middle Layers | Late Layers |
|-------|-------------|---------------|-------------|
| Llama-3.2-3B | 15.5% | **53.5%** | 31.0% |
| Qwen3-4B | 28.1% | 35.9% | 35.9% |
| Mistral-7B | 33.8% | **46.3%** | 20.0% |

Middle layers dominate, consistent with the idea that intermediate representations are where factual knowledge is most actively processed.

**Ablation by layer group (TriviaQA / Llama):**
- Full model: 0.858
- Removing middle layers: 0.844 (largest drop)
- Removing early layers: 0.849
- Removing late layers: 0.862 (slight improvement)

**Token-level analysis (99th percentile of divergence values):**
- 66.5% are named entities
- 30.1% are other content words
- 2.3% are stop words
- 0.3% are numeric tokens

The extreme tail is overwhelmingly dominated by factual tokens (entities and numbers), with stop words and punctuation contributing negligibly.

**Answer-only vs. prompt-only tokens (TriviaQA / Llama):**
- Answer tokens only: AUROC 0.871 (strongest signal)
- Prompt tokens only: AUROC 0.767 (partial signal)
- Full sequence: AUROC 0.822

---

### Detection Only -- No Intervention/Mitigation

The paper is **purely a detection method**. It does not propose any intervention or mitigation for hallucinations. The authors explicitly note this as a limitation: the approach "cannot reduce hallucinations, only identify them." They briefly suggest that future work could use attention divergence as a training objective via reinforcement learning, penalizing extreme divergence at critical tokens, but this is speculative and not implemented.

---

### Relationship to Residual Stream Probes

The paper directly compares against hidden state probing and positions itself as a complementary alternative:

- **Hidden state probes** (e.g., Orgad et al. 2024, Binkowski et al. 2025, Chen et al. 2024) train classifiers on residual stream activations at specific layers. Van Dijk argues these "often struggle to generalize across tasks and datasets."
- **The attention divergence method** uses a different signal -- the distribution of attention weights rather than the activations themselves. It captures *how* the model routes information rather than *what* information is stored.
- On TruthfulQA, attention divergence substantially outperforms hidden state probes (0.906 vs. 0.823 AUROC). On TriviaQA, hidden state probes are slightly better (0.850 vs. 0.835).
- Both approaches share a key limitation: **poor cross-dataset generalization**. The specific heads/layers/dimensions that are selected vary across datasets and model families, with no single head appearing across all four benchmarks.

Recent related work on residual stream probes includes the **ICR Probe** (ACL 2025), which tracks cross-layer evolution of hidden states, and **PCNet** (2026), which treats hallucinations as geometric anomalies on a factual manifold in the residual stream. The van Dijk paper's attention-based approach offers a distinct and complementary signal to these residual-stream methods.

---

### Key Limitations

1. **No causal mechanism established** -- the signal is distributed across multiple heads with no simple logical rule.
2. **Probe specificity** -- the combination of selected heads varies across datasets and model families; approximately 0.5% of total heads are selected, and no head is shared across all benchmarks.
3. **Requires white-box access** to internal attention weights; cannot be applied to API-only models.
4. **Detection only**, no mitigation capability.
5. **Interpretability is limited** -- the probe should be viewed as an extraction tool, not an explanation of how uncertainty is represented.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2605.05025)
- [arXiv HTML full paper](https://arxiv.org/html/2605.05025)
- [ICR Probe (ACL 2025)](https://aclanthology.org/2025.acl-long.880.pdf)
- [Observer Model residual probe](https://arxiv.org/html/2507.23221v1)
- [PCNet: Hallucination as Anomaly](https://arxiv.org/html/2605.05953)
- [TOHA: Topological Divergence on Attention Graphs](https://arxiv.org/abs/2504.10063)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b90fc151-8da4-40c9-9cd4-f13de54b0274",
  "isSidechain": true,
  "agentId": "a525bf697c9ec78a9",
  "requestId": "req_011Cb61x2Fx2fCckY4PgpxNi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c5e8905-2716-4ada-974e-0ff7ab618b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GfCGuiVAFzsmZr9z1BBu44",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1014,
      "cache_read_input_tokens": 16059,
      "output_tokens": 2560,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2560,
          "cache_read_input_tokens": 16059,
          "cache_creation_input_tokens": 1014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1014,
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
