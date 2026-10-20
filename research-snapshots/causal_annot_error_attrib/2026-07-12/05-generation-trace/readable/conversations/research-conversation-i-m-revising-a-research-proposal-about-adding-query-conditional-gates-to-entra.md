# Research conversation: I'm revising a research proposal about adding query-conditional gates to "entrainment heads" in LLMs. A reviewer pointed

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-acb12f7251d68b949.jsonl`
- **Structured JSON:** [`0655b240aeb8342e3961.json`](../../sessions/06/0655b240aeb8342e3961.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-17T08:46:56.430Z_

I'm revising a research proposal about adding query-conditional gates to "entrainment heads" in LLMs. A reviewer pointed out that the ACL 2025 paper "Llama See, Llama Do" shows entrainment heads are NOT the ICL circuit — static ablation only causes 0.2-3% ICL degradation.

I need to understand exactly what the entrainment paper says about:
1. What happens when entrainment heads are statically ablated — what capabilities ARE lost?
2. The relationship (or lack thereof) between entrainment heads and ICL
3. Any tasks or capabilities where disabling entrainment heads DOES cause significant degradation beyond ICL
4. Whether the paper discusses any downsides of static ablation on relevant-context utilization (e.g., RAG scenarios, long-context QA)

Search for and read the actual paper. The GitHub repo is at github.com/frankniujc/entrainment. The paper title is "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs".

Report your findings in detail, with specific numbers and quotes where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "4298a63b-c3af-4a3a-ba93-a5717186e311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T08:46:56.437Z_

```json
{
  "parentUuid": "4298a63b-c3af-4a3a-ba93-a5717186e311",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
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
  "uuid": "d1ef0bbc-c25a-4ce8-9b06-8a2a58bda1f7",
  "timestamp": "2026-05-17T08:46:56.437Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T08:46:58.558Z_



I'll search for and read the paper to answer your questions. Let me start by fetching the paper from the GitHub repository and any available online sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1ef0bbc-c25a-4ce8-9b06-8a2a58bda1f7",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rFGcDXxLLqeVWM552A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8afd4a06-e108-4853-994f-424e2ca7f47c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Z86c7Yvv2yHRKAHYzRzQg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 820,
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

_source line 4 · 2026-05-17T08:46:58.981Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TC37sqXgnwGLKy6xu2iy1o`</summary>

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
  "parentUuid": "8afd4a06-e108-4853-994f-424e2ca7f47c",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rFGcDXxLLqeVWM552A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fd1bef0-a0bc-42bb-abab-5abd53ae5a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Z86c7Yvv2yHRKAHYzRzQg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 8223,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 820
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 820,
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

_source line 5 · 2026-05-17T08:46:58.985Z_

<details><summary>↩ Tool result · `toolu_01TC37sqXgnwGLKy6xu2iy1o`</summary>

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
  "parentUuid": "1fd1bef0-a0bc-42bb-abab-5abd53ae5a92",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "26ebd6c9-adf3-451d-aa9d-b94ce569711a",
  "sourceToolAssistantUUID": "1fd1bef0-a0bc-42bb-abab-5abd53ae5a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-17T08:47:01.509Z_



Let me fetch the paper from the GitHub repository and also try to find the actual paper PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26ebd6c9-adf3-451d-aa9d-b94ce569711a",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rFUY4jZtSqmSd3jNVc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db08b2c4-98cf-4ea8-8cfb-026757f6d158",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Le5PcRoUWaLn28snSsPUdt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 7 · 2026-05-17T08:47:04.295Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014upqoKWCB28WNtrLhhkBgv`</summary>

```json
{
  "url": "https://github.com/frankniujc/entrainment",
  "prompt": "Extract all information about the paper: title, authors, abstract, link to the paper PDF or arxiv. Also extract any README content that describes the paper's findings, especially about ablation experiments, ICL, and entrainment heads."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db08b2c4-98cf-4ea8-8cfb-026757f6d158",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rFUY4jZtSqmSd3jNVc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47d0233a-843b-493c-9a8f-4ab8f47a59de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Le5PcRoUWaLn28snSsPUdt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 8 · 2026-05-17T08:47:05.770Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C9TtcLc2nReF8BM4vwy79F`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.06537",
  "prompt": "Extract the full abstract and all details about this paper about entrainment heads in LLMs. Look for the paper \"Llama See, Llama Do\" about contextual entrainment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d0233a-843b-493c-9a8f-4ab8f47a59de",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rFUY4jZtSqmSd3jNVc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1077dc9b-ebac-4407-8d57-bed100a7b737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Le5PcRoUWaLn28snSsPUdt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9043,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1418
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 9043,
          "cache_creation_input_tokens": 1418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1418,
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

_source line 9 · 2026-05-17T08:47:08.509Z_

<details><summary>↩ Tool result · `toolu_01C9TtcLc2nReF8BM4vwy79F`</summary>

```text
I cannot find the paper you're looking for in the provided content. The webpage shows details for **"ProFashion: Prototype-guided Fashion Video Generation with Multiple Reference Images"** (arXiv:2505.06537), which focuses on fashion video generation using diffusion models and multiple reference images.

This is not the same as "Llama See, Llama Do" or any paper about entrainment heads in large language models. The document you've shared contains information about a computer vision paper in the cs.CV category, not an LLM research paper.

To find the paper about contextual entrainment in LLMs, you would need to provide the correct arXiv page or search for it separately.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1077dc9b-ebac-4407-8d57-bed100a7b737",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "35905eaa-e7e0-4493-b1ed-3210bd4a48ec",
  "sourceToolAssistantUUID": "1077dc9b-ebac-4407-8d57-bed100a7b737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T08:47:10.274Z_

<details><summary>↩ Tool result · `toolu_014upqoKWCB28WNtrLhhkBgv`</summary>

```text
# Paper Information

**Title:** "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs"

**Authors:** Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, and Amir H. Abdi

**Paper Link:** https://arxiv.org/abs/2505.09338 (also published at ACL 2025: https://aclanthology.org/2025.acl-long.791/)

## Abstract

The researchers identify a phenomenon called "contextual entrainment" where language models assign disproportionately high probabilities to tokens that previously appeared in context, regardless of relevance. The abstract states: "LMs assign significantly higher logits (or probabilities) to any tokens that have previously appeared in the context prompt, even for random tokens."

## Key Findings

**Mechanistic Discovery:** The paper demonstrates this entrainment operates mechanistically, independent of semantic relevance. However, semantic factors modulate its strength—counterfactual prompts trigger greater entrainment than factual ones.

**Entrainment Heads:** Using differentiable masking techniques, researchers identified specific attention heads responsible for this phenomenon. When these heads are deactivated, "the effect of contextual entrainment is significantly attenuated," causing models to ignore distracting context.

## Repository Contents

The GitHub repository includes:
- `entrainment.ipynb`: Comprehensive notebook documenting all paper findings
- `head_search.py`: Script implementing the entrainment head discovery methodology
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47d0233a-843b-493c-9a8f-4ab8f47a59de",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "39defb1f-0d75-4648-be02-a4fcba950a43",
  "sourceToolAssistantUUID": "47d0233a-843b-493c-9a8f-4ab8f47a59de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-17T08:47:12.760Z_

Good, I found the correct arxiv ID. Let me now fetch the actual paper content and the notebook that contains all findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39defb1f-0d75-4648-be02-a4fcba950a43",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rGHjhzhQoMK86SkViZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33307cfe-b021-45f1-9069-61936a6de393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KszHJERGBDBjossybU25B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 187,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 10461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 659,
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

_source line 12 · 2026-05-17T08:47:14.370Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016LsTFnMRhDhaiQA5NULQr6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.09338",
  "prompt": "Extract the FULL abstract and all available details about this paper. Include authors, title, abstract text, and any other metadata available on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33307cfe-b021-45f1-9069-61936a6de393",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rGHjhzhQoMK86SkViZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0db92943-fc57-45cf-b10a-3d59f6ddff55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KszHJERGBDBjossybU25B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 187,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 10461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 659,
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

_source line 13 · 2026-05-17T08:47:17.919Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012DUdfLfUy4DZKZL2mLzJKS`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338",
  "prompt": "Extract the ENTIRE paper content. I need ALL sections including: introduction, methodology, results, ablation experiments, discussion, and conclusion. Pay special attention to: 1) What happens when entrainment heads are statically ablated - what capabilities ARE lost? 2) The relationship between entrainment heads and ICL (in-context learning) 3) Any tasks where disabling entrainment heads causes significant degradation 4) Any discussion of static ablation effects on relevant-context utilization (RAG, long-context QA). Include ALL specific numbers, percentages, and experimental results mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0db92943-fc57-45cf-b10a-3d59f6ddff55",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rGHjhzhQoMK86SkViZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f8ae46a-6920-4847-b48d-e08b3809d599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KszHJERGBDBjossybU25B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 187,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 10461,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 659
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 187,
          "output_tokens": 330,
          "cache_read_input_tokens": 10461,
          "cache_creation_input_tokens": 659,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 659,
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

_source line 14 · 2026-05-17T08:47:19.258Z_

<details><summary>↩ Tool result · `toolu_016LsTFnMRhDhaiQA5NULQr6`</summary>

```text
# Paper Details

**Title:** "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs"

**Authors:** Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi

**arXiv ID:** 2505.09338

**Submission Date:** May 14, 2025 (v1); Revised June 27, 2025 (v2)

**Field:** Computer Science > Computation and Language (cs.CL)

**Venue:** ACL 2025

**DOI:** https://doi.org/10.48550/arXiv.2505.09338

## Abstract Summary

The researchers identify a phenomenon called "contextual entrainment," where language models assign disproportionately high probabilities to tokens appearing in the input context, "regardless of semantic relevance." This occurs mechanistically across various model types and prompting conditions.

Key findings include:

- Semantic factors modulate the effect, with counterfactual prompts showing stronger entrainment than factual ones
- The team discovered circuits of attention heads ("entrainment heads") responsible for this behavior using differentiable masking techniques
- Disabling these heads significantly reduces the distraction effect, allowing models to generate outputs closer to scenarios without distracting context

**License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0db92943-fc57-45cf-b10a-3d59f6ddff55",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "d53253a9-1dce-4591-bcc3-7322221d1496",
  "sourceToolAssistantUUID": "0db92943-fc57-45cf-b10a-3d59f6ddff55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T08:47:30.253Z_

<details><summary>↩ Tool result · `toolu_012DUdfLfUy4DZKZL2mLzJKS`</summary>

```text
# Summary: Contextual Entrainment and Entrainment Heads in LLMs

## Core Phenomenon

The paper identifies **contextual entrainment**: LMs assign significantly higher logits/probabilities to tokens appearing in context prompts, regardless of relevance. As the authors colorfully phrase it, "if a token appears in the context prompt, even a random one, the model assigns it a higher probability."

## Key Findings

**Finding 1**: Distracting tokens receive consistent logit boosts (10-100x probability increases) across all context types—related, irrelevant, and random—across multiple models (Llama-3.1-8B, Llama-2-7b/13b, GPT-2 XL). All differences show p<0.0001.

**Finding 2**: Correct-answer tokens show mixed effects. Related context helps (logit increase), while irrelevant/random contexts slightly decrease correct-token logits—except for instruction-tuned models.

**Finding 3**: Counterfactual contexts (false statements) produce stronger distraction than factual ones, indicating semantic modulation of a mechanistic phenomenon.

## Entrainment Heads Discovery & Ablation Effects

Using differentiable masking, researchers identified 3-11% of attention heads (30-110 heads per relation in Llama-3.1-8B's 1,024 total) as entrainment heads.

### Static Ablation Results

When entrainment heads are "turned off" (output set to zero):

- **Contextual entrainment severely attenuates**: For country-capital queries, distracting token ranks dropped from 37.5 to 1,707 (with context vs. without). Logit gaps between correct and distracting tokens increased from 7.69 to 13.20 across all test samples.

- **ICL capabilities largely preserved**: 
  - Arithmetic: 100% accuracy maintained
  - Spelling correction (1-5 shot): 0.2-3% performance decrease
  - Translation (1-5 shot): 0.2-2.4% decrease
  - Factual recall on other relations: minimal degradation across 15 LRE relations

- **Other LM capabilities minimally affected**: General capabilities show negligible loss per Appendix H.

### Critical Limitation: Relevant Context Handling

The paper acknowledges that "distracting context can be beneficial when relevant." However, the ablation results don't explicitly quantify performance loss on tasks requiring helpful context utilization. Table 4 shows factual recall on *other* relations without context—not performance on tasks where context contains the actual answer needed.

## Task-Specificity vs. Model-Specificity

Entrainment heads are **relation-specific, not model-specific**. Different relations activate different head sets (30 for country-language vs. 110 for product-by-company), with only partial functional overlap across relations.

## Mechanism vs. Statistics

The authors argue contextual entrainment is fundamentally mechanistic (occurring even with random tokens) yet modulated by semantics (stronger for counterfactual info). This challenges strict dichotomies between mechanistic and statistical LM interpretations.

## Practical Implications

The ability to suppress distraction by disabling ~3-11% of heads while maintaining ICL performance suggests potential for internal model-level mitigation strategies, contrasting with existing RAG approaches that modify retrieval or prompts externally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f8ae46a-6920-4847-b48d-e08b3809d599",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "8a3e3c06-6e81-4b43-9041-4fcfd9135acf",
  "sourceToolAssistantUUID": "0f8ae46a-6920-4847-b48d-e08b3809d599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-17T08:47:35.052Z_

Good, I'm getting substantial findings. Let me now fetch more specific sections of the paper, particularly the ablation tables and any discussion about RAG/long-context scenarios, and also look at the ACL anthology version and the notebook.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a3e3c06-6e81-4b43-9041-4fcfd9135acf",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rHmAzK5z1NoQZMmANr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54f28285-7e24-4619-8cca-8c158f1519d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ey54nnJGmYRaZDbCTHYJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1699,
      "cache_read_input_tokens": 11120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1699,
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

_source line 17 · 2026-05-17T08:47:44.445Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014p3FXo1rj51KxbRDmFrR1d`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338",
  "prompt": "I need VERY SPECIFIC details from the following sections. Extract exact numbers, table data, and quotes:\n\n1. Section about ICL ablation (Table showing arithmetic, spelling, translation results with exact numbers for each n-shot setting)\n2. Table 4 or any table showing factual recall on other relations after ablation\n3. Appendix H or any appendix discussing general LM capabilities after ablation\n4. Any discussion of RAG, retrieval-augmented generation, long-context QA, or relevant context utilization after ablation\n5. Any discussion of LIMITATIONS of static ablation or \"downsides\" of turning off entrainment heads\n6. The exact definition of \"static ablation\" vs \"dynamic ablation\" if discussed\n7. Any mention of what capabilities ARE significantly degraded by ablation (not just ICL)\n8. Section 5 or Discussion or Conclusion - extract fully\n\nFocus on extracting EXACT numbers and direct quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54f28285-7e24-4619-8cca-8c158f1519d9",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rHmAzK5z1NoQZMmANr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfca752a-a7c1-472d-bcc4-1aefd2ef06f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ey54nnJGmYRaZDbCTHYJh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1699,
      "cache_read_input_tokens": 11120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1699,
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

_source line 18 · 2026-05-17T08:47:44.584Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017MwfMPCy5DmyKeN39d6ujZ`</summary>

```json
{
  "url": "https://aclanthology.org/2025.acl-long.791/",
  "prompt": "Extract any available information about the paper, including links to the PDF, supplementary materials, and any details about the paper content, especially ablation experiments and their effects on ICL and other capabilities."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfca752a-a7c1-472d-bcc4-1aefd2ef06f4",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rHmAzK5z1NoQZMmANr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2b7c319-f5e0-4cba-92f0-d6a55a730c18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ey54nnJGmYRaZDbCTHYJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1699,
      "cache_read_input_tokens": 11120,
      "output_tokens": 452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1699
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 452,
          "cache_read_input_tokens": 11120,
          "cache_creation_input_tokens": 1699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1699,
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

_source line 19 · 2026-05-17T08:47:49.197Z_

<details><summary>↩ Tool result · `toolu_017MwfMPCy5DmyKeN39d6ujZ`</summary>

```text
# Paper Information: "Llama See, Llama Do"

## Basic Details
- **Title:** Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs
- **Authors:** Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, Amir H. Abdi
- **Venue:** ACL 2025 (63rd Annual Meeting)
- **Award:** Outstanding Paper
- **Pages:** 16218–16239

## Links
- **PDF:** https://aclanthology.org/2025.acl-long.791.pdf
- **Full Page:** https://aclanthology.org/2025.acl-long.791/
- **DOI:** 10.18653/v1/2025.acl-long.791

## Key Research Contributions
The paper investigates "contextual entrainment," where language models assign elevated logits to tokens appearing in the input context, regardless of relevance. The authors identify specific "entrainment heads"—attention circuit components responsible for this phenomenon—using a differentiable masking approach. Disabling these heads significantly reduces the entrainment effect.

## Main Finding
The research demonstrates that "LMs assign significantly higher logits (or probabilities) to any tokens that have previously appeared in the context prompt, even for random tokens," indicating this is a mechanistic rather than purely semantic phenomenon.

**Note:** No supplementary materials or specific ablation study details are provided on this ACL Anthology entry page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2b7c319-f5e0-4cba-92f0-d6a55a730c18",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "376faad9-70bb-4801-ba9b-057b77466ee9",
  "sourceToolAssistantUUID": "a2b7c319-f5e0-4cba-92f0-d6a55a730c18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T08:47:50.549Z_

<details><summary>↩ Tool result · `toolu_014p3FXo1rj51KxbRDmFrR1d`</summary>

```text
# Key Findings: Entrainment Head Ablation Effects

## ICL Task Performance (Table 4)

After removing entrainment heads for country–capital city relation:

**Arithmetic:**
- 0-shot: 100.0% → 100.0% (no change)

**Spelling Correction:**
- 1-shot: 73.6% → 72.0% (strict), 78.6% → 76.8% (credulous)
- 2-shot: 94.6% → 91.6% (strict), 97.0% → 94.8% (credulous)
- 5-shot: 99.0% → 98.4% (strict), 100.0% → 100.0% (credulous)

**Translation:**
- 1-shot: 74.4% → 73.0% (strict), 78.4% → 76.8% (credulous)
- 2-shot: 94.0% → 93.0% (strict), 97.0% → 96.2% (credulous)
- 5-shot: 98.6% → 97.2% (strict), 99.6% → 99.4% (credulous)

## Factual Recall (Table 4)

Performance on 15 LRE relations showed minimal degradation. Example: country capital city maintained 100.0% strict accuracy both before and after ablation.

## Capabilities Impact Statement

"Removing the entrainment heads has only a negligible to small effect on other LM capabilities" with drops of "0.2∼3%" across ICL tasks.

## Limitations Acknowledged

The authors note: "we did not propose an application to mitigate the distraction problem" and acknowledge experiments used only LRE dataset, not standard RAG benchmarks, requesting validation on larger models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfca752a-a7c1-472d-bcc4-1aefd2ef06f4",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "13429509-55e8-4c3c-bf5a-5f33c9fb902f",
  "sourceToolAssistantUUID": "dfca752a-a7c1-472d-bcc4-1aefd2ef06f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-17T08:47:55.758Z_

Let me now fetch the full paper PDF and the notebook for more details, especially about Appendix H and the discussion of relevant context effects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13429509-55e8-4c3c-bf5a-5f33c9fb902f",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rKFvtyaFmokWxD7NkJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fcdb5d4-913f-4c5d-a54e-f852beefef37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqxuQhVuM3pch95EXFxxQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 397,
      "cache_creation_input_tokens": 1021,
      "cache_read_input_tokens": 12819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1021,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 22 · 2026-05-17T08:48:02.774Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ADYa6AeH5vVxrWbM6MW1DZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338",
  "prompt": "Extract the COMPLETE content from these specific sections:\n\n1. ANY section discussing \"relevant context\" or \"beneficial context\" or cases where entrainment is actually helpful - exact quotes needed\n2. Appendix H - what general LM capabilities were tested? What benchmarks? What were the exact results?\n3. The LIMITATIONS section - extract every sentence\n4. Any discussion comparing static ablation vs. dynamic/conditional ablation\n5. Any mention of \"query-conditional\" or \"gating\" or \"selective\" approaches\n6. Section on \"distraction vs. beneficial context\" - does the paper acknowledge that ablating entrainment heads could hurt performance when context IS relevant?\n7. Any discussion about what the entrainment mechanism is GOOD for (i.e., its normal function beyond just \"distraction\")\n8. The conclusion section - extract fully\n9. Any mention of RAG, retrieval, augmented generation, grounded generation, or knowledge-grounded tasks\n\nPlease be exhaustive and include direct quotes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fcdb5d4-913f-4c5d-a54e-f852beefef37",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rKFvtyaFmokWxD7NkJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "691b7fb7-27ae-416f-9b17-b68e802b1af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqxuQhVuM3pch95EXFxxQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 397,
      "cache_creation_input_tokens": 1021,
      "cache_read_input_tokens": 12819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1021,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 23 · 2026-05-17T08:48:05.247Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JbgucnQW5bQCp11UCEta42`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/frankniujc/entrainment/main/entrainment.ipynb",
  "prompt": "Extract ALL text content, markdown cells, and comments from this Jupyter notebook. Focus on any discussion of: 1) ablation experiments and their effects, 2) ICL performance after ablation, 3) relevant context scenarios, 4) any benchmarks beyond LRE, 5) limitations of the approach. Include all markdown commentary and analysis text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "691b7fb7-27ae-416f-9b17-b68e802b1af0",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rKFvtyaFmokWxD7NkJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dee586ac-d7fa-4a5d-967d-c3853c3c26fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqxuQhVuM3pch95EXFxxQK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 397,
      "cache_creation_input_tokens": 1021,
      "cache_read_input_tokens": 12819,
      "output_tokens": 482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1021
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 397,
          "output_tokens": 482,
          "cache_read_input_tokens": 12819,
          "cache_creation_input_tokens": 1021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1021,
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

_source line 24 · 2026-05-17T08:48:11.247Z_

<details><summary>↩ Tool result · `toolu_01JbgucnQW5bQCp11UCEta42`</summary>

```text
# Analysis of Notebook Content

Based on the provided Jupyter notebook excerpt, here's what I can extract:

## Key Content Areas

**Markdown Discussion:**
The notebook demonstrates how language models can be distracted by contextual information. The explanation states: "LLMs can be distracted by various types of context" with specific observations that:
- Models generate correct responses without context
- Related topics cause incorrect responses
- Different formats and paraphrasing maintain distraction effects
- Single tokens alone can trigger model distraction

**Experimental Setup:**
The code shows a `plot_top_k_probs` function that compares model predictions across four conditions:
- (a) No context baseline
- (b) Related topic context (Iraq example)
- (c) Rephrased context variants
- (d) Minimal token-based context (Asia)

**Dataset Reference:**
The notebook references the LRE (Long-Range Entailment) dataset through the import statement: `from head_search.data.lre_dataset import LREDataset`

## Missing Information

The provided excerpt does not contain:
- Ablation experiment details or results
- Quantitative ICL performance metrics post-ablation
- Benchmark comparisons beyond contextual entrainment
- Documented limitations of the approach
- Analysis of why entrainment occurs mechanistically

The notebook appears incomplete in this excerpt, cutting off during visualization code without showing analysis sections that would discuss ablations or performance metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dee586ac-d7fa-4a5d-967d-c3853c3c26fb",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "72f0b4d2-f4ea-4ea3-a6e1-d4b5a012552e",
  "sourceToolAssistantUUID": "dee586ac-d7fa-4a5d-967d-c3853c3c26fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T08:48:16.402Z_

<details><summary>↩ Tool result · `toolu_01ADYa6AeH5vVxrWbM6MW1DZ`</summary>

```text
# Extraction Summary

## 1. Beneficial/Relevant Context (Finding 2)

**Finding 2 exact quote:**
> "Distracting" context prompts can be beneficial when relevant."

**Discussion quote:**
> "Although distracting context may not contain the exact correct answer, the implicit hints it provides can be beneficial, increasing the likelihood that the model generates the correct response."

**Example:** The paper demonstrates this with "In Argentina, people speak the language of" where "In Russia, the primary language is Russian" helps steer toward Spanish rather than love/football.

---

## 2. Appendix H - General Capabilities Testing

**Not explicitly titled "Appendix H" in visible content.** The relevant section states:

> "Removing the entrainment heads has only a negligible to small effect on the LM's performance across other relations, with no obvious differences."

**Benchmarks tested (Table 4):**
- 15 LRE relations (factual recall)
- Arithmetic (0-shot): 100% → 100%
- Spelling correction (1-5 shot): 73.6%–99.0% → 72.0%–98.4%
- Translation (1-5 shot): 74.4%–98.6% → 73.0%–97.2%

No standardized benchmark suites mentioned.

---

## 3. Limitations Section (Complete)

> "We did not conduct our experiments using larger LMs such as Llama-3.1-70B and Llama-3.1-405B due to resource limitations... we observed no differences in findings between larger and smaller models... we conducted experiments using only the LRE dataset... We did not use standard RAG datasets... our experiment with random token inputs provides strong evidence... we do not propose an application to mitigate the distraction problem."

---

## 4. Static vs. Dynamic Ablation

**Not discussed.** The paper uses only static ablation (setting entrainment head outputs to zero uniformly).

---

## 5. Query-Conditional/Gating/Selective Approaches

**Not mentioned.** No discussion of conditional or selective activation mechanisms.

---

## 6. Trade-off: When Ablation Hurts Performance

The paper **acknowledges this implicitly** but does not deeply explore it:

> "our findings suggest there could be a way to mitigate distraction by directly modifying or monitoring the internal mechanisms of LMs when performing RAG."

**However,** Table 4 shows performance actually *improves* on some relations after ablation, suggesting the authors found minimal harm. The paper does not explicitly model scenarios where context IS relevant.

---

## 7. Normal Function of Entrainment Mechanism

The paper frames entrainment heads as corresponding *solely* to distraction:

> "this circuit of entrainment heads collectively corresponds to contextual entrainment rather than other capabilities... is not strongly related to how LMs process and utilise contextual information or perform ICL more broadly."

**No discussion of what entrainment is "good for" beyond acknowledging Finding 2 on beneficial context.

---

## 8. Conclusion Section (Complete)

> "Llama see, llama do. We observe and confirm a novel phenomenon, which we term contextual entrainment... an effect that is analogous to but distinct from previously identified phenomena... However, we also discover that contextual entrainment is influenced by semantic factors... This finding highlights the potential threat of dis- and misinformation... Our identification of the entrainment heads suggests that interpretability techniques could provide crucial insights for real-world applications."

---

## 9. RAG/Retrieval/Grounded Generation Mentions

**RAG mentioned 4 times:**
- "distraction has been recognised as one of the most challenging and widespread issues for RAG"
- "RAG is most relevant to the problem of distraction"
- "our findings suggest there could be a way to mitigate distraction by directly modifying or monitoring the internal mechanisms of LMs when performing RAG"

**No empirical RAG experiments conducted.** Discussion remains theoretical.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "691b7fb7-27ae-416f-9b17-b68e802b1af0",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "f566066d-0477-4e4f-a465-919d3be6a1f0",
  "sourceToolAssistantUUID": "691b7fb7-27ae-416f-9b17-b68e802b1af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-17T08:48:19.249Z_

Let me get more details from the paper, particularly about the key claim regarding ICL independence and the specific experimental evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f566066d-0477-4e4f-a465-919d3be6a1f0",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rMASJY9x2rb5epucyM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6804d120-821d-43a7-9227-172a444aa2b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJahUeTkqEGcagsSbZMpWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 355,
      "cache_creation_input_tokens": 1846,
      "cache_read_input_tokens": 13840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1846,
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

_source line 27 · 2026-05-17T08:48:27.737Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FAhPT32AYcb35B3FNZHM2c`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338",
  "prompt": "I need the EXACT content from these specific parts of the paper:\n\n1. The section that argues entrainment heads are NOT the ICL circuit. Extract the exact paragraph(s) and any supporting evidence. What is their argument? What experiment proves this?\n\n2. Table 3 - what does it show? Extract all data.\n\n3. Table 4 - extract ALL rows and columns with exact numbers. This is the key ablation table.\n\n4. Table 5 or any table showing overlap between entrainment heads and other known head types (induction heads, previous token heads, etc.)\n\n5. The section on \"head overlap\" or comparison with known attention head types.\n\n6. Any figure captions or descriptions related to ablation results.\n\n7. The exact quote where they say ablation causes \"0.2-3%\" degradation or similar.\n\n8. Any discussion of the entrainment heads' role in COPYING from context (which would be relevant for RAG/grounded generation).\n\n9. Section 4 (results/analysis) - extract key paragraphs about what ablation does and doesn't affect.\n\nPlease extract verbatim quotes wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6804d120-821d-43a7-9227-172a444aa2b5",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rMASJY9x2rb5epucyM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbf3e71f-658a-4348-9701-3605c352376e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJahUeTkqEGcagsSbZMpWG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 355,
      "cache_creation_input_tokens": 1846,
      "cache_read_input_tokens": 13840,
      "output_tokens": 361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1846
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 355,
          "output_tokens": 361,
          "cache_read_input_tokens": 13840,
          "cache_creation_input_tokens": 1846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1846,
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

_source line 28 · 2026-05-17T08:48:39.589Z_

<details><summary>↩ Tool result · `toolu_01FAhPT32AYcb35B3FNZHM2c`</summary>

```text
# Key Findings on Entrainment Heads vs. ICL and Ablation Effects

## 1. Entrainment Heads Are NOT the ICL Circuit

The paper argues entrainment heads are **task-specific, not model-specific**, distinguishing them from general ICL mechanisms:

> "entrainment heads are task-specific (or relation-specific), rather than model-specific"

They provide supporting evidence:

> "our method has identified different and different amount of entrainment heads for each LRE relation"

This directly contradicts a model-specific ICL circuit. Their reasoning: if entrainment heads were the core ICL mechanism, the same heads should activate across all tasks.

---

## 2. Table 3 Data (Entrainment Head Identification Across Relations)

| Relation | # Heads (Density) | Logit Gap Before → After |
|----------|------------------|-------------------------|
| company hq | 90 (8.8%) | 3.94 → 14.68 |
| country capital city | 36 (3.5%) | 7.69 → 13.20 |
| country currency | 42 (4.1%) | 4.73 → 11.67 |
| country language | 30 (2.9%) | 6.20 → 8.95 |
| country largest city | 33 (3.2%) | 8.68 → 13.35 |
| food from country | 38 (3.7%) | 3.98 → 9.95 |
| fruit inside color | 56 (5.5%) | 0.97 → 11.16 |
| fruit outside color | 80 (7.8%) | 2.14 → 13.82 |
| landmark in country | 59 (5.8%) | 3.93 → 9.68 |
| landmark on continent | 52 (5.1%) | 2.51 → 9.14 |
| product by company | 110 (10.7%) | 3.62 → 16.47 |
| star constellation name | 72 (7.0%) | 1.07 → 8.87 |
| task done by tool | 66 (6.4%) | 4.70 → 12.31 |
| task person type | 41 (4.0%) | 6.51 → 12.47 |
| work location | 68 (6.6%) | 3.17 → 12.68 |

---

## 3. Table 4 (Ablation Effects on Other Capabilities)

Selected critical rows:

| Task | Strict Acc (Original → Ablated) | Credulous Acc (Original → Ablated) |
|------|--------------------------------|--------------------------------|
| arithmetic 0-shot | 100.0% → 100.0% | 100.0% → 100.0% |
| spelling correction 1-shot | 73.6% → 72.0% | 78.6% → 76.8% |
| spelling correction 2-shot | 94.6% → 91.6% | 97.0% → 94.8% |
| spelling correction 5-shot | 99.0% → 98.4% | 100.0% → 100.0% |
| translation 1-shot | 74.4% → 73.0% | 78.4% → 76.8% |
| translation 2-shot | 94.0% → 93.0% | 97.0% → 96.2% |
| translation 5-shot | 98.6% → 97.2% | 99.6% → 99.4% |

---

## 4. Head Overlap / Comparison with Known Types

The paper **does not compare entrainment heads directly with induction heads or other established head types**. Appendix F mentions "Functional Overlap of Entrainment Heads" but this examines overlap *between different relations*, not with prior literature on head typologies.

---

## 5. Exact Ablation Performance Statement

> "the model exhibits only a small performance decrease (0.2∼3%) and continues demonstrate strong ICL capabilities"

This quote caps degradation at 3%, consistent with Table 4 data.

---

## 6. Role in Copying/Context Replication

The paper **explicitly distinguishes entrainment from copying**:

> "contextual entrainment does not require the reappearance of a prefix...unlike sequence copying, which depends on first encountering a pattern"

They conclude entrainment is a **mechanistic but weaker phenomenon** than literal copying—relevant for understanding RAG distraction but not grounded generation per se.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbf3e71f-658a-4348-9701-3605c352376e",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "5ad38e42-6085-4c42-8704-876d28709527",
  "sourceToolAssistantUUID": "fbf3e71f-658a-4348-9701-3605c352376e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T08:48:53.002Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SQQuZxYDdjRs9MLeLxJVhm`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338",
  "prompt": "Extract the following SPECIFIC content:\n\n1. Appendix F on \"Functional Overlap of Entrainment Heads\" - extract the full content including any overlap percentages between relations\n\n2. Any discussion of what happens to FACTUAL RECALL on the SAME relation after ablation (not other relations). Does the model still answer factual questions correctly about country-capital when entrainment heads for country-capital are ablated? This is crucial - does ablating entrainment heads hurt the model's ability to use RELEVANT context?\n\n3. The experimental setup for ablation - how exactly are heads ablated? Is it zeroing out, mean ablation, or something else?\n\n4. Any discussion of \"copy\" heads, \"induction\" heads, or \"previous token\" heads in the paper\n\n5. Finding 4 and Finding 5 - extract completely with exact quotes\n\n6. Any discussion about whether entrainment heads play a DUAL role - both causing distraction AND enabling relevant context utilization\n\n7. The \"Related Work\" section - any comparison to prior work on attention head ablation in ICL\n\nExtract exact quotes and numbers wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ad38e42-6085-4c42-8704-876d28709527",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rNse58tWqjJ2PJhs68",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e40bfa3-8c8f-46d0-9504-4aafe1ab74d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uq2aLttCocHCijLyLENAaK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1858,
      "cache_read_input_tokens": 15686,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 15686,
          "cache_creation_input_tokens": 1858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1858,
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

_source line 30 · 2026-05-17T08:49:03.193Z_

<details><summary>↩ Tool result · `toolu_01SQQuZxYDdjRs9MLeLxJVhm`</summary>

```text
# Extraction from "Llama See, Llama Do" Paper

## 1. Appendix F: Functional Overlap of Entrainment Heads

The paper references Appendix F but **does not include its content** in the provided document. The table of contents mentions it exists, but the actual text is cut off before that section.

## 2. Factual Recall on Same Relation After Ablation

**Critical Finding**: The paper does NOT test whether ablating entrainment heads hurts performance on the SAME relation with relevant context.

Table 4 shows ablated models tested on OTHER relations without distracting context. The paper states: "Removing these heads has a negligible effect on the LM's performance across other relations."

However, **no experiment directly tests**: Does removing country-capital entrainment heads harm performance when answering country-capital questions WITH relevant factual context provided?

## 3. Experimental Setup for Ablation

Ablation uses **zeroing out**: "When 'turning these entrainment heads off,' i.e., setting their output to zero" and "set their outputs to zero."

The method introduces differentiable masks where heads' contributions to the residual stream become zero.

## 4. Discussion of Copy/Induction/Previous Token Heads

The paper **distinguishes from induction heads**: "contextual entrainment does not require the reappearance of a prefix as a trigger, unlike sequence copying."

No specific mention of "copy heads" or "previous token heads" terminology.

## 5. Finding 4 and Finding 5

**Only three numbered findings exist** in the paper:
- Finding 1: Contextual entrainment phenomenon
- Finding 2: Distracting context can be beneficial when relevant
- Finding 3: Counterfactual prompts cause stronger distraction

No Finding 4 or Finding 5 appear in the document.

## 6. Dual Role Discussion

**Not explored**. The paper does not investigate whether entrainment heads simultaneously cause distraction AND enable relevant context use. This represents a significant gap.

## 7. Related Work on Attention Head Ablation in ICL

The related work section mentions Jin et al. (2024) identified "memory heads" and "context heads" but notes their method "is limited to investigating each attention head in isolation and do not consider the interaction between attention heads."

No other ablation studies on ICL heads are discussed in detail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e40bfa3-8c8f-46d0-9504-4aafe1ab74d4",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "e71b9086-3348-4136-b118-0309d9747f7e",
  "sourceToolAssistantUUID": "0e40bfa3-8c8f-46d0-9504-4aafe1ab74d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T08:49:13.975Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019RmFKRYyvBeesecDZQwA1m`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338",
  "prompt": "Find and extract these SPECIFIC parts:\n\n1. Section 3.2 or wherever they describe the differentiable masking method - how do they find entrainment heads? What is the optimization objective?\n\n2. The paragraph that discusses \"context heads\" (Jin et al. 2024) and how entrainment heads relate to them\n\n3. Any paragraph discussing whether entrainment heads overlap with \"context heads\" or \"memory heads\" from prior work\n\n4. The section header structure of the paper - list ALL section and subsection titles\n\n5. Any mention of \"relevant retrieval\", \"golden context\", \"correct context\", or scenarios where the context contains the RIGHT answer\n\n6. The paragraph starting with or containing \"this circuit of entrainment heads collectively corresponds to\" - extract the FULL paragraph\n\n7. Any text in appendices about general capability benchmarks (MMLU, HellaSwag, ARC, etc.) after ablation\n\n8. Any discussion about the FUNCTION of entrainment in normal model operation - WHY do these heads exist? What evolutionary/training pressure created them?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e71b9086-3348-4136-b118-0309d9747f7e",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rQcgTmypuaJ52LggS6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c35f699d-d41c-4800-ad3b-d7f946a2c95e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2fneNjnJLvi8EZX5QcWAk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 17544,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 891
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 17544,
          "cache_creation_input_tokens": 891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 891,
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

_source line 32 · 2026-05-17T08:49:27.296Z_

<details><summary>↩ Tool result · `toolu_019RmFKRYyvBeesecDZQwA1m`</summary>

```text
# Analysis of "Llama See, Llama Do" Paper

## 1. Differentiable Masking Method (Section 4.1)

The authors identify entrainment heads using differentiable masking with binary masks m_j for each attention head. They convert sampled variables from a Gumbel-sigmoid distribution using straight-through estimators, making masks differentiable. The optimization objective combines two components:

- **Logits Delta**: Maximize the difference between correct token logits and distracting token logits
- **Sparsity Loss**: Minimize the number of heads selected (weighted by λ=1.0)

The loss function: "ℒ = ℓ(correct) - ℓ(distracting) + λ · (1/|H|) Σ σ(l_i)"

## 2. Context Heads Discussion (Section 4)

The paper acknowledges Jin et al. (2024) identified "memory heads" and "context heads" related to knowledge conflicts. However, the authors note critical differences:

- Their setting doesn't present direct conflicts (counterfactual context about unrelated entities)
- They focus on entrainment phenomenon specifically, not conflict resolution
- Their approach examines head interactions via circuits, not isolated heads

"Jin et al. (2024) found that attention heads play a key role in utilizing contextual information" but their method examined "each attention head in isolation" without considering interactions.

## 3. Overlap with Prior Work

The paper explicitly states entrainment heads "are task-specific (or relation-specific), not model-specific," which directly contradicts Jin et al.'s classification of heads as discrete functional roles. The authors argue "this assumption cannot account for our results."

No comprehensive functional overlap analysis is provided in the main text, though Appendix F exists for this.

## 4. Section Headers Structure

**Main sections:**
- 1. Introduction (+ Contributions)
- 2. Related Work (Distraction; Mechanistic Interpretability & Induction Heads)
- 3. Context Entrainment (3.1 Experimental Setup; 3.2 Experiment Results; 3.3 Counterfactual Experiment Results)
- 4. Entrainment Heads (4.1 Entrainment Heads Discovery; 4.2 Experiment Results & Analysis)
- 5. Conclusion

**Appendices:** A-H covering datasets, supplementary results, background, and ICL tasks

## 5. Relevant/Correct Context Scenarios

The paper explicitly discusses beneficial distracting context in **Finding 2**:

"While distracting context may not contain the exact correct answer, implicit hints it provides can be beneficial, increasing the likelihood that the model generates the correct response."

Example: Ambiguous questions where related context helps clarify intent (e.g., "In Argentina, people speak the language of" benefits from context about language use in other countries).

## 6. Full Paragraph on Circuit Correspondence

"This finding supports our hypothesis that this 'circuit' of entrainment heads collectively corresponds to contextual entrainment rather than other capabilities and phenomena, such as factual recall, and is not strongly related to how LMs process and utilise contextual information or perform ICL more broadly."

(From end of Section 4.2)

## 7. General Capability Benchmarks

The paper does NOT report MMLU, HellaSwag, or ARC results. Instead, Appendix H tests "general capabilities" using other LRE relations and three ICL tasks (arithmetic, spelling correction, translation). Removing entrainment heads shows only 0.2-3% performance decrease on these tasks.

## 8. Function and Origin of Entrainment Heads

The paper provides **no explicit discussion** of why entrainment heads exist or what evolutionary/training pressure created them. They identify the phenomenon mechanistically but remain agnostic about causation. The authors note contextual entrainment occurs "independently of the relevance or semantic relation," suggesting it may be an incidental byproduct rather than an intentional feature. The discussion acknowledges an ongoing debate about whether context utilization "arises from mere memorisation...or from the implementation of an algorithm," suggesting entrainment might be compositional rather than deliberate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c35f699d-d41c-4800-ad3b-d7f946a2c95e",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "5f6a6989-8fb0-4ccd-af65-11cbb42d8d41",
  "sourceToolAssistantUUID": "c35f699d-d41c-4800-ad3b-d7f946a2c95e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-17T08:49:30.563Z_

Now I have comprehensive information. Let me also check for the appendix content on functional overlap.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f6a6989-8fb0-4ccd-af65-11cbb42d8d41",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rSPcTDCfKizB7cWzRU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1bd2a7e-a807-4fca-b245-0adb228a35df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tf6cT1EfXXDVa7n5KnRm7P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 18435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1302,
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

_source line 34 · 2026-05-17T08:49:34.762Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FQwQUiDYiDfAxcSyhCG8ex`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.09338",
  "prompt": "Focus specifically on Appendix F, G, and H content. These appendices should appear near the end of the paper. Extract:\n\n1. Appendix F \"Functional Overlap of Entrainment Heads\" - any tables showing overlap percentages between head sets for different relations\n2. Appendix G - whatever it contains\n3. Appendix H - the ICL evaluation details, including exact experimental setup and all results\n\nAlso extract: any figure showing the Jaccard similarity or overlap between entrainment head sets across relations.\n\nAlso look for: any discussion of \"copy suppression\" heads or anti-entrainment mechanisms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1bd2a7e-a807-4fca-b245-0adb228a35df",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rSPcTDCfKizB7cWzRU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b41828c-b5b5-4f37-b851-5fd14cf5d639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tf6cT1EfXXDVa7n5KnRm7P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 18435,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 239,
          "cache_read_input_tokens": 18435,
          "cache_creation_input_tokens": 1302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1302,
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

_source line 35 · 2026-05-17T08:49:39.984Z_

<details><summary>↩ Tool result · `toolu_01FQwQUiDYiDfAxcSyhCG8ex`</summary>

```text
# Analysis of Appendices F, G, and H

## Appendix F: Functional Overlap of Entrainment Heads

The document mentions this appendix exists but does not provide the detailed content in the extracted text. The paper states: "We do observe some level of overlap in the function of entrainment heads across different relations (Appendix F)," indicating that entrainment heads show task-specific rather than model-specific properties, with some functional similarities between different relation types.

No specific overlap percentages, Jaccard similarity figures, or detailed overlap tables are visible in the provided content.

## Appendix G: ICL Tasks

This appendix covers three in-context learning task categories:

1. **Arithmetic** - 0-shot evaluation
2. **Spelling Correction** - 1-shot, 2-shot, and 5-shot variants
3. **Translation** - 1-shot, 2-shot, and 5-shot variants

Results appear in Table 4, showing minimal performance degradation (0.2-3%) after removing entrainment heads, demonstrating that disabling these heads preserves ICL capabilities.

## Appendix H: General Capabilities After Head Removal

This appendix evaluates broader model performance when entrainment heads are disabled. The key finding: "Removing the entrainment heads also have a small effect on the LMs' general capabilities" across factual recall and various tasks.

## Notable Absence

The document contains **no discussion of "copy suppression" heads or anti-entrainment mechanisms**. The focus remains on identifying and disabling entrainment heads that facilitate contextual entrainment, rather than exploring competing mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b41828c-b5b5-4f37-b851-5fd14cf5d639",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "acb12f7251d68b949",
  "type": "user",
  "uuid": "beb4dae8-b8ed-4ef3-8634-81a951b14f6f",
  "sourceToolAssistantUUID": "6b41828c-b5b5-4f37-b851-5fd14cf5d639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-17T08:50:37.240Z_

I now have a thorough understanding of the paper. Here is my detailed report.

---

## Detailed Findings from "Llama See, Llama Do" (Niu et al., ACL 2025)

**Paper:** "Llama See, Llama Do: A Mechanistic Perspective on Contextual Entrainment and Distraction in LLMs" by Jingcheng Niu, Xingdi Yuan, Tong Wang, Hamidreza Saghir, and Amir H. Abdi. Published at ACL 2025 (Outstanding Paper award). arXiv: 2505.09338.

---

### 1. What happens when entrainment heads are statically ablated -- what capabilities ARE lost?

**Short answer: Almost nothing measurable is lost.** The paper ablates entrainment heads by zeroing out their output contributions to the residual stream. The results show:

**ICL tasks (Table 4, ablating country-capital entrainment heads):**
- Arithmetic (0-shot): 100.0% --> 100.0% (no change)
- Spelling correction (1-shot): 73.6% --> 72.0% strict / 78.6% --> 76.8% credulous
- Spelling correction (2-shot): 94.6% --> 91.6% strict / 97.0% --> 94.8% credulous
- Spelling correction (5-shot): 99.0% --> 98.4% strict / 100.0% --> 100.0% credulous
- Translation (1-shot): 74.4% --> 73.0% strict / 78.4% --> 76.8% credulous
- Translation (2-shot): 94.0% --> 93.0% strict / 97.0% --> 96.2% credulous
- Translation (5-shot): 98.6% --> 97.2% strict / 99.6% --> 99.4% credulous

**Factual recall:** Performance on 15 LRE relations (tested on *other* relations, not the one whose heads were ablated) showed "negligible" degradation. Country-capital-city itself maintained 100.0% strict accuracy.

**What IS affected:** The entrainment effect itself is dramatically reduced. For country-capital queries, distracting token ranks dropped from 37.5 to 1,707 (i.e., the model stopped being distracted). The logit gap between correct and distracting tokens increased from 7.69 to 13.20.

The paper's exact claim: *"the model exhibits only a small performance decrease (0.2~3%) and continues [to] demonstrate strong ICL capabilities."*

---

### 2. The relationship (or lack thereof) between entrainment heads and ICL

The paper makes a strong claim that entrainment heads are **not** the ICL circuit. The key evidence and arguments:

**a) Task-specificity, not model-specificity:** Different relations activate different numbers and sets of entrainment heads. For example, country-language uses only 30 heads (2.9% of 1,024 total in Llama-3.1-8B), while product-by-company uses 110 heads (10.7%). The paper states: *"entrainment heads are task-specific (or relation-specific), rather than model-specific."* If these were the general ICL circuit, the same heads should activate across tasks.

**b) Minimal ICL degradation upon ablation:** The 0.2-3% drops across spelling correction and translation tasks (see numbers above) are presented as evidence that ICL operates through different mechanisms.

**c) The key concluding quote:** *"This finding supports our hypothesis that this 'circuit' of entrainment heads collectively corresponds to contextual entrainment rather than other capabilities and phenomena, such as factual recall, and is not strongly related to how LMs process and utilise contextual information or perform ICL more broadly."*

**d) Distinction from induction heads:** The paper distinguishes entrainment from copying/induction: *"contextual entrainment does not require the reappearance of a prefix as a trigger, unlike sequence copying, which depends on first encountering a pattern."*

**Important nuance:** The paper does NOT compare entrainment heads to "context heads" or "memory heads" (from Jin et al. 2024) by checking functional overlap. They merely note that Jin et al.'s method *"is limited to investigating each attention head in isolation and do not consider the interaction between attention heads."*

---

### 3. Tasks or capabilities where disabling entrainment heads DOES cause significant degradation

**The honest answer: the paper does not find any.** The tested capabilities (arithmetic, spelling correction, translation, factual recall across 15 relations) all show negligible degradation. The paper does NOT test:

- Standard NLP benchmarks (MMLU, HellaSwag, ARC, etc.)
- Generative tasks (summarization, open-ended QA)
- Tasks requiring faithfully reproducing context content
- Any task with more than 5-shot ICL

The Limitations section explicitly acknowledges: *"we conducted experiments using only the LRE dataset"* and *"We did not use standard RAG datasets."*

---

### 4. Whether the paper discusses downsides of static ablation on relevant-context utilization (RAG, long-context QA)

**This is a critical gap in the paper.** Here is what the paper says and does NOT say:

**What it acknowledges (Finding 2):** *"'Distracting' context prompts can be beneficial when relevant."* The paper gives examples where related (but not directly answering) context helps the model. For instance, context about Russian language helps steer "In Argentina, people speak the language of..." toward "Spanish" rather than "love" or "football." The full quote: *"Although distracting context may not contain the exact correct answer, the implicit hints it provides can be beneficial, increasing the likelihood that the model generates the correct response."*

**What it does NOT test:** The paper never evaluates what happens when you ablate entrainment heads and then provide **relevant, correct context** (the exact scenario in RAG or long-context QA). All ablation experiments test either (a) scenarios with distracting/irrelevant context, or (b) no-context factual recall. The crucial experiment -- "does ablating country-capital entrainment heads hurt performance when the context actually contains the correct capital?" -- is simply absent.

**RAG discussion is purely theoretical.** The paper mentions RAG four times but only in framing/motivation, never in experiments:
- *"distraction has been recognised as one of the most challenging and widespread issues for RAG"*
- *"our findings suggest there could be a way to mitigate distraction by directly modifying or monitoring the internal mechanisms of LMs when performing RAG"*

**Static vs. dynamic ablation:** The paper does NOT discuss dynamic or query-conditional ablation at all. It only uses static ablation (uniform zeroing). There is no mention of "gating," "query-conditional," or "selective" approaches.

**Explicit limitations from the paper:**
- *"We did not conduct our experiments using larger LMs such as Llama-3.1-70B and Llama-3.1-405B due to resource limitations"*
- *"we conducted experiments using only the LRE dataset"*
- *"We did not use standard RAG datasets"*
- *"we do not propose an application to mitigate the distraction problem"*

---

### Key Implications for Your Research Proposal

The reviewer's point about the 0.2-3% ICL degradation is accurate -- the paper does show that. However, there are several important caveats you can leverage:

1. **The paper never tests relevant-context scenarios after ablation.** This is the biggest gap. Entrainment heads boost probabilities for ALL tokens seen in context. In RAG/grounded generation, you WANT the model to boost tokens from the retrieved context. Static ablation might throw the baby out with the bathwater. The paper explicitly acknowledges this risk in Finding 2 but never measures it.

2. **The paper only tests narrow factual recall (LRE) and simple ICL tasks.** No standard benchmarks, no generative tasks, no knowledge-intensive QA.

3. **The paper does not discuss or test query-conditional/dynamic ablation.** Your proposed query-conditional gates would directly address the paper's own acknowledged limitation: entrainment is harmful for irrelevant context but beneficial for relevant context.

4. **Entrainment heads are relation-specific (30-110 heads per relation).** This means a static "ablate all entrainment heads" approach would need to identify and ablate different head sets for different query types, further motivating a learned gating mechanism.

5. **The paper's own framing supports your direction.** Their conclusion states: *"Our identification of the entrainment heads suggests that interpretability techniques could provide crucial insights for real-world applications."* Query-conditional gates are exactly such an application.

The paper is at `https://arxiv.org/abs/2505.09338` and the code repository at `https://github.com/frankniujc/entrainment`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beb4dae8-b8ed-4ef3-8634-81a951b14f6f",
  "isSidechain": true,
  "agentId": "acb12f7251d68b949",
  "requestId": "req_011Cb7rTKpHAXvLKrecXSyf5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dc94cbf-399e-4c90-b2c6-cf9df633794c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjR6yhThY47Gb19dB4aosv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 19737,
      "output_tokens": 2157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2157,
          "cache_read_input_tokens": 19737,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 622,
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
