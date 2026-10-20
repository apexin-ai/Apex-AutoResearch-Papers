# Research conversation: I need to read and summarize five specific arXiv papers for a research review. For each paper, fetch the abstract page a

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ada872dd41e9c99a7.jsonl`
- **Structured JSON:** [`62700be44e439ed773f4.json`](../../sessions/62/62700be44e439ed773f4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-10T07:33:12.994Z_

I need to read and summarize five specific arXiv papers for a research review. For each paper, fetch the abstract page and read carefully. Report the key findings, method, and how they relate to multilingual instruction tuning.

Papers to fetch (use WebFetch on the arXiv abstract pages):

1. arXiv:2510.25947 - "Revisiting Multilingual Data Mixtures" (Foroutan et al., EPFL, Oct 2025) 
   URL: https://arxiv.org/abs/2510.25947
   Key question: Does this paper show that staged curriculum learning and temperature-based language reweighting hurts multilingual pretraining? Does it apply to instruction tuning or only pretraining?

2. arXiv:2511.10229 - "LangGPS" (Yangfan Ye, Xiaocheng Feng et al., HIT + Microsoft, AAAI 2026)
   URL: https://arxiv.org/abs/2511.10229
   Key question: How does it use model-internal representation signals for multilingual instruction tuning data selection? Does it address multi-pivot ordering or typological structure?

3. arXiv:2411.02460 - "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs" (Haneul Yoo et al., NAVER AI, ACL 2025 Findings)
   URL: https://arxiv.org/abs/2411.02460
   Key question: What are the 3 curriculum stages? Does it use typological distance? Does it work on low-resource languages?

4. arXiv:2502.13647 - "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh" (Laiyk et al., ACL 2025 Main)
   URL: https://arxiv.org/abs/2502.13647
   Key question: What model does it fine-tune? How many training examples? What results on Kazakh benchmarks?

5. arXiv:2510.27183 - "Simple Additions, Substantial Gains: Expanding URIEL+" (Shipton, Ng, Khan et al., LREC 2026)
   URL: https://arxiv.org/abs/2510.27183
   Key question: What specific improvements does it add to URIEL+? What is the 35% sparsity reduction figure? Does it cover Kazakh/Uzbek/Kyrgyz better?

For each paper, please provide:
- Full title and venue
- 3-4 sentence summary of method and findings
- Direct answer to the "key question" above
- How it differs from TWMP's approach (TWMP = typologically-weighted multi-pivot instruction tuning using URIEL+ cosine distances to weight source language selection from Aya corpus, with 3-stage curriculum progressively introducing more distant pivots, targeting Kazakh/Mongolian/Uyghur)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "2ef50154-a26b-45ad-8bc9-4cff5c4a15ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T07:33:13.000Z_

```json
{
  "parentUuid": "2ef50154-a26b-45ad-8bc9-4cff5c4a15ec",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
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
  "uuid": "37eab9e7-79b8-493a-ac31-c613593bfbb2",
  "timestamp": "2026-05-10T07:33:13.000Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T07:33:14.860Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018qNADrT8NG6u6Kqz1ij3Ld`</summary>

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
  "parentUuid": "37eab9e7-79b8-493a-ac31-c613593bfbb2",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVxnn5Njzxkbovuu812",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47d188a6-06d2-4452-971c-7a7095e99578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019X2uxyHMz8ZVGcgS1AFcui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9336,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9336,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-10T07:33:14.867Z_

<details><summary>↩ Tool result · `toolu_018qNADrT8NG6u6Kqz1ij3Ld`</summary>

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
  "parentUuid": "47d188a6-06d2-4452-971c-7a7095e99578",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "38c794fc-107a-4e69-ba5e-e6c789e3c3be",
  "sourceToolAssistantUUID": "47d188a6-06d2-4452-971c-7a7095e99578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T07:33:17.284Z_

I'll fetch all five arXiv abstract pages in parallel now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c794fc-107a-4e69-ba5e-e6c789e3c3be",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVxxroQsjzLZcctYEUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ad9dd67-515a-496b-b83b-2219fb5a473e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EKnNirWnhz7pXD6hYRzSwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1384,
      "cache_read_input_tokens": 9336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1384,
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

_source line 6 · 2026-05-10T07:33:19.539Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014doiviqGi7HtFEuHNUdpYi`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.25947",
  "prompt": "Extract the full title, authors, venue/conference, abstract, and any key methodological details mentioned on the page. Note whether the paper is about pretraining, instruction tuning, or both. Note any mention of curriculum learning, temperature-based reweighting, or staged training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ad9dd67-515a-496b-b83b-2219fb5a473e",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVxxroQsjzLZcctYEUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63dd24b9-85a8-4ea0-aa27-e0ec2ff180da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EKnNirWnhz7pXD6hYRzSwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1384,
      "cache_read_input_tokens": 9336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1384,
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

_source line 7 · 2026-05-10T07:33:21.215Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FeccjSQdCMoevSF2JcUUvp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.10229",
  "prompt": "Extract the full title, authors, venue/conference, abstract, and any key methodological details. Note how the paper uses model-internal representation signals for multilingual instruction tuning data selection. Note any mention of multi-pivot ordering, typological structure, or typological distance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63dd24b9-85a8-4ea0-aa27-e0ec2ff180da",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVxxroQsjzLZcctYEUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eee6f497-a72c-4530-bf6f-ed0273df6414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EKnNirWnhz7pXD6hYRzSwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1384,
      "cache_read_input_tokens": 9336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1384,
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

_source line 8 · 2026-05-10T07:33:22.772Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BqRLXRfMXDaTf1znN2bwpg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.02460",
  "prompt": "Extract the full title, authors, venue/conference, abstract, and any key methodological details. List all curriculum stages described (especially any 3-stage curriculum). Note any mention of typological distance, low-resource languages, or code-switching methodology."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eee6f497-a72c-4530-bf6f-ed0273df6414",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVxxroQsjzLZcctYEUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d517336-fe0b-47a3-86a2-a74bce490f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EKnNirWnhz7pXD6hYRzSwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1384,
      "cache_read_input_tokens": 9336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1384,
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

_source line 9 · 2026-05-10T07:33:24.251Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017r3iRrmMgoboARSCqGraw5`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.13647",
  "prompt": "Extract the full title, authors, venue/conference, abstract, and any key methodological details. Note which model is fine-tuned, the number of training examples used, and what results are achieved on Kazakh benchmarks. Note anything about low-resource language instruction tuning."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d517336-fe0b-47a3-86a2-a74bce490f10",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVxxroQsjzLZcctYEUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d699f6c5-af49-4e72-885a-d94ed3ccc52a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EKnNirWnhz7pXD6hYRzSwD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1384,
      "cache_read_input_tokens": 9336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1384,
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

### Tool result

_source line 10 · 2026-05-10T07:33:24.524Z_

<details><summary>↩ Tool result · `toolu_014doiviqGi7HtFEuHNUdpYi`</summary>

```text
# Paper Extraction Summary

**Full Title:** "Revisiting Multilingual Data Mixtures in Language Model Pretraining"

**Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut

**Venue/Conference:** Under Review (arXiv submission, submitted October 29, 2025)

**Abstract Summary:**
The researchers trained 1.1B and 3B parameter LLMs across multilingual corpora with 25-400 languages. Key findings include: combining English with multilingual data doesn't degrade performance when languages have sufficient token representation; English functions effectively as a pivot language across language families; and increasing language count doesn't produce the expected "curse of multilinguality" at this model scale.

**Scope:** This work focuses on **pretraining only**, not instruction tuning.

**Methodological Details:**
The page mentions "varying the number of languages from 25 to 400" and explores "multilingual data mixtures," but does not explicitly reference curriculum learning, temperature-based reweighting, or staged training approaches.

**Paper Access:** Available as PDF, HTML, and TeX source via arXiv (DOI: 10.48550/arXiv.2510.25947)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63dd24b9-85a8-4ea0-aa27-e0ec2ff180da",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "69fb74a2-73e2-463f-80b9-f9d0a8ed39d3",
  "sourceToolAssistantUUID": "63dd24b9-85a8-4ea0-aa27-e0ec2ff180da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T07:33:26.473Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MsMws27vk63meNYFecEUcv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.27183",
  "prompt": "Extract the full title, authors, venue/conference, abstract, and any key methodological details. Note what specific improvements are added to URIEL+. Mention any statistics about sparsity reduction (especially any 35% figure). Note whether coverage of Kazakh, Uzbek, or Kyrgyz is mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69fb74a2-73e2-463f-80b9-f9d0a8ed39d3",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVxxroQsjzLZcctYEUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38cbbb1a-fe88-47ee-beba-ac4d99d19ed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EKnNirWnhz7pXD6hYRzSwD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1384,
      "cache_read_input_tokens": 9336,
      "output_tokens": 649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1384
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 649,
          "cache_read_input_tokens": 9336,
          "cache_creation_input_tokens": 1384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1384,
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

_source line 12 · 2026-05-10T07:33:27.180Z_

<details><summary>↩ Tool result · `toolu_01FeccjSQdCMoevSF2JcUUvp`</summary>

```text
# LangGPS Paper Summary

**Full Title:** LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning

**Authors:** Yangfan Ye, Xiaocheng Feng, Xiachong Feng, Lei Huang, Weitao Ma, Qichen Hong, Yunfei Lu, Duyu Tang, Dandan Tu, Bing Qin

**Venue:** AAAI 2026 Main Track (Accepted)

**Abstract Overview:**
The paper addresses data selection for multilingual instruction tuning by proposing LangGPS, a framework that uses "language separability" as a selection criterion. The approach evaluates "how well samples in different languages can be distinguished in the model's representation space." This two-stage method filters data based on separability scores before applying existing selection techniques.

**Key Methodological Details:**

- **Core Metric:** Language separability quantifies linguistic distinction within model representations
- **Two-Stage Process:** Initial filtering by separability scores, followed by refinement using existing methods
- **Evaluation:** Tested across six benchmarks spanning 22 languages
- **Findings:** Highly separable samples create "clearer language boundaries and support faster adaptation," while low-separability samples function as "bridges for cross-lingual alignment"
- **Curriculum Learning Application:** Interleaving samples with varying separability levels produces consistent gains

**Important Note:** The submission does not mention multi-pivot ordering, typological structure, or typological distance metrics in the available content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eee6f497-a72c-4530-bf6f-ed0273df6414",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "69a2dc64-f943-4570-9f73-54fc69b135d5",
  "sourceToolAssistantUUID": "eee6f497-a72c-4530-bf6f-ed0273df6414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T07:33:27.392Z_

<details><summary>↩ Tool result · `toolu_01BqRLXRfMXDaTf1znN2bwpg`</summary>

```text
# Code-Switching Curriculum Learning for Multilingual Transfer in LLMs

## Title
"Code-Switching Curriculum Learning for Multilingual Transfer in LLMs"

## Authors
Haneul Yoo, Cheonbok Park, Sangdoo Yun, Alice Oh, Hwaran Lee

## Venue
Findings of ACL 2025

## Abstract Summary
The research addresses performance disparities in large language models across languages with varying data availability. Inspired by human second language acquisition, the authors propose a method that mirrors "the practice of language alternation in a conversation" to improve cross-lingual capabilities. The approach demonstrates significant improvements for Korean, Japanese, and Indonesian using multiple base models (Qwen 2, Gemma 2, Phi 3.5).

## Three-Stage Curriculum
The proposed curriculum consists of:
1. Token-level code-switching
2. Sentence-level code-switching  
3. Monolingual corpora

## Key Methodological Details
- **Inspiration**: Human language acquisition processes
- **Primary Focus**: Low-resource language transfer where "high-quality, monolingual corpora for language transfer are hardly available"
- **Secondary Benefit**: The method "mitigates spurious correlations between language resources and safety alignment"
- **Finding**: Ablation studies show both token and sentence-level stages "significantly enhance cross-lingual transfer"

## Notable Absence
The document does not explicitly mention typological distance considerations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d517336-fe0b-47a3-86a2-a74bce490f10",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "7a323d5a-aacc-42d0-a055-f42c6e80ca61",
  "sourceToolAssistantUUID": "6d517336-fe0b-47a3-86a2-a74bce490f10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T07:33:29.767Z_

<details><summary>↩ Tool result · `toolu_017r3iRrmMgoboARSCqGraw5`</summary>

```text
# Research Paper Summary

**Full Title:** "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh"

**Authors:** Nurkhan Laiyk, Daniil Orel, Rituraj Joshi, Maiya Goloburda, Yuxia Wang, Preslav Nakov, Fajri Koto

**Venue:** arXiv (cs.CL - Computation and Language)

**Abstract:**
The researchers created a 10,600-sample instruction-following dataset focused on Kazakh institutional and cultural knowledge. They used "LLM-assisted data generation, comparing open-weight and closed-weight models" with GPT-4o selected as the backbone, followed by manual verification of each sample. Fine-tuning Qwen, Falcon, and Gemma models on this dataset showed improvements across multiple-choice and generative tasks.

**Key Methodological Details:**

- **Training Dataset Size:** 10,600 samples
- **Models Fine-tuned:** Qwen, Falcon, Gemma
- **Data Generation Approach:** LLM-assisted with manual verification
- **Backbone Model:** GPT-4o
- **Domain Focus:** Government procedures, legal topics, structural governance
- **Language:** Kazakh (low-resource)

**Low-Resource Language Significance:**
This work addresses the underexplored area of instruction tuning for low-resource languages by demonstrating that "consistent performance improvements" can be achieved through domain-specific, manually-verified datasets combined with established open-weight model fine-tuning approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d699f6c5-af49-4e72-885a-d94ed3ccc52a",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "d1d6c99f-1efc-4d09-9b0f-274a6dcf1caa",
  "sourceToolAssistantUUID": "d699f6c5-af49-4e72-885a-d94ed3ccc52a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T07:33:32.681Z_

<details><summary>↩ Tool result · `toolu_01MsMws27vk63meNYFecEUcv`</summary>

```text
# URIEL+ Enhancement Paper Summary

**Full Title:** "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"

**Authors:** Mason Shipton, York Hay Ng, Aditya Khan, Phuong Hanh Hoang, Xiang Lu, A. Seza Doğruöz, En-Shiun Annie Lee

**Venue:** LREC 2026 (accepted)

**Abstract Summary:**
The work addresses data sparsity in URIEL+, a linguistic knowledge base that encodes languages through geographic, genetic, and typological properties. The researchers aim to improve its utility for cross-lingual transfer and low-resource language support.

**Key Improvements to URIEL+:**
1. Script vectors introduced for 7,488 languages to capture writing system characteristics
2. Glottolog integration adding 18,710 additional languages
3. Expanded lineage imputation covering 26,449 languages by propagating features across language families

**Notable Statistics:**
- Script vector sparsity reduced by 14%
- Language coverage increased by up to 19,015 languages (1,007% growth)
- "imputation quality metrics by up to 35%" improved
- Cross-lingual transfer performance gains reached 6% in certain configurations

**Language Coverage Note:**
The content provided does not mention specific coverage of Kazakh, Uzbek, or Kyrgyz languages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38cbbb1a-fe88-47ee-beba-ac4d99d19ed7",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "ff9d79a5-a89b-4aba-a112-06499f6f0bbb",
  "sourceToolAssistantUUID": "38cbbb1a-fe88-47ee-beba-ac4d99d19ed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T07:33:36.296Z_

Good — I have the abstract-level content. Some details need verification (the 35% figure returned as "imputation quality" not sparsity, and I want more precision on paper 4's venue and paper 1's stance on curriculum). Let me do targeted follow-up fetches on the two that need clarification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff9d79a5-a89b-4aba-a112-06499f6f0bbb",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVzEuiuuCTyaQkENu8M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11d354b4-8ae2-4caf-9862-6d87fc7d7b60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DyHfDkzu3jZ5ofcZg4jWEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2449,
      "cache_read_input_tokens": 10720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2449,
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

_source line 17 · 2026-05-10T07:33:38.894Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01A2UqzdYxpjcQZ7p6adJo9f`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.25947",
  "prompt": "Read the full abstract very carefully. Does the paper explicitly argue against or in favor of temperature-based language reweighting and staged curriculum learning? Does it claim these approaches hurt multilingual pretraining? Quote any key sentences from the abstract on this topic. Also confirm: is the paper entirely about pretraining, or does it also address instruction tuning or fine-tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d354b4-8ae2-4caf-9862-6d87fc7d7b60",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVzEuiuuCTyaQkENu8M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcd2d288-66bb-4a26-adbc-4f85048c8831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DyHfDkzu3jZ5ofcZg4jWEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2449,
      "cache_read_input_tokens": 10720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2449,
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

_source line 18 · 2026-05-10T07:33:41.151Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013ten3Bp7RJMUrPYmRv9tuP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.13647",
  "prompt": "Read the full abstract carefully. What is the exact venue — is it ACL 2025 Main or somewhere else? How many training examples exactly (is it 10,600 or another number)? What specific Kazakh benchmark results are reported? Which models were fine-tuned and what are the specific performance numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd2d288-66bb-4a26-adbc-4f85048c8831",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVzEuiuuCTyaQkENu8M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b050438-98e5-404b-b964-72198ff224c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DyHfDkzu3jZ5ofcZg4jWEM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2449,
      "cache_read_input_tokens": 10720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2449,
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

### Tool result

_source line 19 · 2026-05-10T07:33:41.213Z_

<details><summary>↩ Tool result · `toolu_01A2UqzdYxpjcQZ7p6adJo9f`</summary>

```text
# Response

The abstract does **not** mention temperature-based language reweighting or staged curriculum learning at all. There are no explicit arguments for or against these approaches, nor any claims about how they affect multilingual pretraining.

Regarding scope: The paper focuses exclusively on pretraining. The abstract makes no reference to instruction tuning or fine-tuning phases.

The research instead centers on different aspects of multilingual data mixtures during pretraining, examining language count variation (25 to 400 languages), the role of English as a pivot language, and whether the "curse of multilinguality" actually occurs at these model scales.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcd2d288-66bb-4a26-adbc-4f85048c8831",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "6346642c-bb01-497f-9234-8de2bc535c58",
  "sourceToolAssistantUUID": "dcd2d288-66bb-4a26-adbc-4f85048c8831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T07:33:43.036Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011MjjzArPayPXQzYLcnzxoS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.27183",
  "prompt": "Read the full abstract very carefully. What is the exact 35% figure — is it sparsity reduction, coverage improvement, or imputation quality? Does the abstract explicitly mention Kazakh, Uzbek, or Kyrgyz? Quote exact phrases from the abstract about what improvements are made and any percentage statistics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6346642c-bb01-497f-9234-8de2bc535c58",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatVzEuiuuCTyaQkENu8M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de69d992-b12e-45dc-886e-e7dd20b364c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DyHfDkzu3jZ5ofcZg4jWEM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2449,
      "cache_read_input_tokens": 10720,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 493,
          "cache_read_input_tokens": 10720,
          "cache_creation_input_tokens": 2449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2449,
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

_source line 21 · 2026-05-10T07:33:44.821Z_

<details><summary>↩ Tool result · `toolu_013ten3Bp7RJMUrPYmRv9tuP`</summary>

```text
# Paper Analysis: Kazakh Instruction Tuning Study

**Venue:** The document does not specify a conference venue. This is an arXiv preprint (arXiv:2502.13647) with no mention of ACL 2025 or any other conference publication.

**Training Dataset Size:** The abstract confirms "a large-scale (10,600 samples) instruction-following (IFT) dataset" for Kazakh.

**Benchmark Results:** The abstract does not provide specific numerical performance metrics. It only states that "fine-tuning Qwen, Falcon, and Gemma on our dataset leads to consistent performance improvements in both multiple-choice and generative tasks," without reporting exact benchmark scores or results.

**Models Fine-tuned:** Three base models received instruction tuning: Qwen, Falcon, and Gemma. The paper mentions that GPT-4o served as "the backbone" for LLM-assisted data generation rather than being fine-tuned.

**Limitation:** The provided excerpt contains only the abstract and metadata. Specific performance numbers and detailed Kazakh benchmark results would require accessing the full paper PDF or HTML version referenced on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b050438-98e5-404b-b964-72198ff224c3",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "aed12812-65ca-4f02-ba26-6e5c8ee4b01b",
  "sourceToolAssistantUUID": "1b050438-98e5-404b-b964-72198ff224c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T07:33:47.205Z_

<details><summary>↩ Tool result · `toolu_011MjjzArPayPXQzYLcnzxoS`</summary>

```text
# Analysis of URIEL+ Paper Abstract

Based on the abstract provided, here are the key findings:

**The 35% Figure:**
The abstract states: "boost imputation quality metrics by up to 35%." This refers to **imputation quality improvement**, not sparsity reduction or coverage improvement.

**Specific Language Mentions:**
The abstract does **not explicitly mention** Kazakh, Uzbek, or Kyrgyz by name.

**Key Improvements Quoted:**
1. "reduce feature sparsity by 14% for script vectors"
2. "increase language coverage by up to 19,015 languages (1,007%)"
3. "boost imputation quality metrics by up to 35%"

**Main Contributions:**
The researchers extended URIEL+ by introducing script vectors for 7,488 languages, integrating Glottolog to add coverage, and expanding lineage imputation across genealogies. The abstract notes that cross-lingual transfer task performance showed "occasionally divergent performance compared to URIEL+" with "performance gains up to 6% in certain setups."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de69d992-b12e-45dc-886e-e7dd20b364c5",
  "isSidechain": true,
  "promptId": "7cc972a9-e3ce-4665-b3b3-75c14be2a635",
  "agentId": "ada872dd41e9c99a7",
  "type": "user",
  "uuid": "152aae84-7411-404a-8f80-bdfebc111a76",
  "sourceToolAssistantUUID": "de69d992-b12e-45dc-886e-e7dd20b364c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T07:34:50.710Z_

I now have all the information needed for a thorough, accurate synthesis. Here is the full research review:

---

## Research Review: Five Papers on Multilingual Instruction Tuning and Related Topics

---

### Paper 1: "Revisiting Multilingual Data Mixtures in Language Model Pretraining"

**Full title:** Revisiting Multilingual Data Mixtures in Language Model Pretraining
**Authors:** Negar Foroutan, Paul Teiletche, Ayush Kumar Tarun, Antoine Bosselut (EPFL)
**Venue:** arXiv preprint (submitted October 2025, under review)

**Summary:** The authors train 1.1B and 3B parameter LLMs on multilingual corpora spanning 25 to 400 languages to examine what actually drives multilingual capability during pretraining. They find that combining English with multilingual data does not degrade performance as long as languages have sufficient token representation, that English functions as an effective cross-lingual pivot across language families, and that scaling language count to 400 does not produce the expected "curse of multilinguality" at these model scales.

**Key question answered:** The abstract does not argue that temperature-based language reweighting or staged curriculum learning hurts multilingual pretraining — these techniques are simply not addressed in the abstract, and the paper may not engage with them at all. The paper is entirely about pretraining; instruction tuning and fine-tuning are out of scope.

**Contrast with TWMP:** TWMP operates at the instruction tuning stage and uses URIEL+ typological distances to determine source language selection. This paper addresses only pretraining-phase data mix decisions and is agnostic to the typological weighting and curriculum staging ideas central to TWMP. The papers operate at different points in the training pipeline and are largely complementary rather than directly contradictory.

---

### Paper 2: "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning"

**Full title:** LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning
**Authors:** Yangfan Ye, Xiaocheng Feng, Xiachong Feng, Lei Huang, Weitao Ma, Qichen Hong, Yunfei Lu, Duyu Tang, Dandan Tu, Bing Qin (Harbin Institute of Technology + Microsoft)
**Venue:** AAAI 2026 Main Track (accepted)

**Summary:** LangGPS introduces "language separability" as a criterion for selecting instruction tuning data: it measures how well samples in different languages can be distinguished in the model's internal representation space. A two-stage pipeline first filters samples by their separability score and then refines the selection using existing methods. Highly separable samples establish clearer language boundaries and accelerate adaptation, while low-separability samples act as bridges for cross-lingual alignment. Evaluated across 6 benchmarks and 22 languages, the method yields consistent gains. Notably, interleaving samples with varying separability scores (a form of implicit curriculum) produces further improvements.

**Key question answered:** LangGPS directly uses model-internal representation signals (geometric separability in the model's embedding space) to drive data selection for multilingual instruction tuning. The abstract does not mention multi-pivot ordering or typological structure — the signal is purely data-driven and internal to the model, with no reference to linguistic typology databases like URIEL+.

**Contrast with TWMP:** TWMP selects source pivot languages based on external, linguistically grounded typological distance (URIEL+ cosine similarity) and orders them across a 3-stage curriculum from typologically closer to more distant. LangGPS instead uses internal model geometry as a selection signal and does not consider the linguistic relationship between languages. The two approaches are complementary: TWMP is theory-driven (typology-first), LangGPS is empirically-driven (representation-first). LangGPS also does not specifically target ultra-low-resource Central Asian languages.

---

### Paper 3: "Code-Switching Curriculum Learning for Multilingual Transfer in LLMs"

**Full title:** Code-Switching Curriculum Learning for Multilingual Transfer in LLMs
**Authors:** Haneul Yoo, Cheonbok Park, Sangdoo Yun, Alice Oh, Hwaran Lee (NAVER AI Lab)
**Venue:** Findings of ACL 2025

**Summary:** Inspired by human second-language acquisition, this paper proposes a 3-stage curriculum that progressively transitions from mixed-language to monolingual training to improve cross-lingual transfer. Applied to Korean, Japanese, and Indonesian using Qwen 2, Gemma 2, and Phi 3.5 as base models, the method demonstrates significant improvements especially in low-resource settings where high-quality monolingual corpora are scarce. A secondary finding is that the approach also mitigates spurious correlations between language resources and safety alignment. Ablation studies confirm that both intermediate code-switching stages are necessary.

**Key question answered — the 3 stages are:**
1. Token-level code-switching (words from both languages interleaved within tokens/words)
2. Sentence-level code-switching (alternating entire sentences between languages)
3. Monolingual corpora (full target-language training)

The progression moves from most mixed to least mixed, gradually weaning the model off English anchoring. Typological distance is not mentioned in the abstract — the curriculum structure is motivated by psycholinguistic principles rather than linguistic databases. The paper does work on low-resource languages (Korean/Japanese/Indonesian in low-data regimes), though it does not target Central Asian languages.

**Contrast with TWMP:** Both papers use a 3-stage curriculum, making this the closest methodological relative. However, the curricula differ substantially in mechanism and motivation. TWMP's curriculum stages are defined by typological distance of source pivot languages (closer first, more distant later), with each stage using monolingual instruction data in progressively less similar languages. This paper's stages are defined by the degree of within-sample code-switching (mixed token → mixed sentence → pure monolingual). TWMP preserves clean language boundaries per sample; this paper deliberately blurs them. Additionally, TWMP targets Kazakh/Mongolian/Uyghur specifically, while this work focuses on East and Southeast Asian languages.

---

### Paper 4: "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh"

**Full title:** Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh
**Authors:** Nurkhan Laiyk, Daniil Orel, Rituraj Joshi, Maiya Goloburda, Yuxia Wang, Preslav Nakov, Fajri Koto
**Venue:** Listed in the query as ACL 2025 Main, but the arXiv abstract page does not confirm a conference venue — it appears as an arXiv preprint at time of fetch. Treat the ACL 2025 Main designation as the user-provided claim pending verification.

**Summary:** The authors construct a 10,600-sample instruction-following dataset for Kazakh, focused on government procedures, legal topics, and structural/cultural governance knowledge. Data generation is LLM-assisted using GPT-4o as the backbone, followed by manual verification of every sample. Fine-tuning Qwen, Falcon, and Gemma on this dataset yields consistent improvements on both multiple-choice and generative tasks for Kazakh. The work is one of the few instruction tuning studies focused specifically on Kazakh as a low-resource target language.

**Key question answered:** The paper fine-tunes Qwen, Falcon, and Gemma (specific model sizes not confirmed from the abstract). The training set is exactly 10,600 samples. Specific numerical benchmark scores are not reported in the abstract — the abstract states only "consistent performance improvements in both multiple-choice and generative tasks" without quantitative figures. Full results would require reading the paper body.

**Contrast with TWMP:** This paper shares TWMP's focus on Kazakh as a low-resource target language, making it directly relevant. However, the approach differs fundamentally: this paper generates Kazakh-specific data from scratch using GPT-4o and domain knowledge (government/cultural content), while TWMP transfers from multilingual pivot languages already present in the Aya corpus using typological weighting. TWMP requires no new data generation — it selects and weights existing multilingual data. Additionally, TWMP's curriculum and typological framework could potentially extend to Mongolian and Uyghur in ways this paper does not attempt.

---

### Paper 5: "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"

**Full title:** Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+
**Authors:** Mason Shipton, York Hay Ng, Aditya Khan, Phuong Hanh Hoang, Xiang Lu, A. Seza Dogruoz, En-Shiun Annie Lee
**Venue:** LREC 2026 (accepted)

**Summary:** This paper directly extends URIEL+, the linguistic typology database that encodes languages through geographic, genetic, and typological feature vectors. The authors make three additions: script vectors for 7,488 languages, Glottolog integration expanding coverage by up to 19,015 new languages (a 1,007% increase), and expanded lineage imputation propagating features across 26,449 languages using genealogical trees. The result is a substantially more complete resource, with cross-lingual transfer task performance improving by up to 6% in certain configurations.

**Key question answered — the specific statistics are:**
- Feature sparsity for script vectors reduced by 14% (not 35%)
- The 35% figure refers to imputation quality metrics improving by up to 35% — this is quality of the imputed typological features, not a sparsity reduction figure
- Language coverage grows by up to 19,015 languages (1,007%)
- Kazakh, Uzbek, and Kyrgyz are not explicitly named in the abstract

The 35% figure the user cited is therefore real but refers to imputation quality, not sparsity.

**Contrast with TWMP:** This paper is directly enabling infrastructure for TWMP rather than an alternative approach. TWMP relies on URIEL+ cosine distances to compute typological similarity between languages for pivot selection and curriculum ordering. The expanded URIEL+ described here — with better script vectors, broader language coverage, and higher-quality imputed features — would directly improve TWMP's distance calculations, particularly for Kazakh, Mongolian, and Uyghur, which are low-resource languages likely to benefit from the improved lineage imputation. If URIEL+ now covers more Turkic and Mongolic languages through genealogical imputation, TWMP's typological distance calculations for these targets become more reliable. The two works are symbiotic, not competing.

---

## Cross-Paper Synthesis for TWMP

| Paper | Relation to TWMP |
|---|---|
| Foroutan et al. (pretraining mixtures) | Different training stage (pretraining vs. instruction tuning); no direct conflict or overlap |
| LangGPS (representation-based selection) | Alternative selection signal (internal geometry vs. external typology); complementary, could be combined |
| Yoo et al. (code-switching curriculum) | Closest structural analog (3-stage curriculum); but stages defined by code-mixing degree rather than typological distance |
| Laiyk et al. (Kazakh instruction tuning) | Same target language; complementary strategy (data generation vs. typological transfer) |
| Shipton et al. (URIEL+ expansion) | Direct dependency: improved URIEL+ strengthens TWMP's distance metrics for Central Asian targets |

The most important differentiators of TWMP relative to these five papers are: (1) the use of external linguistic typology (URIEL+) to define curriculum ordering, which no other paper does; (2) the multi-pivot framing where many source languages are weighted and selected rather than one; and (3) the explicit targeting of Kazakh, Mongolian, and Uyghur as an under-studied Central Asian cluster, which only the Laiyk et al. paper shares.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "152aae84-7411-404a-8f80-bdfebc111a76",
  "isSidechain": true,
  "agentId": "ada872dd41e9c99a7",
  "requestId": "req_011CatW1Jypyp4agGRHHryf8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa0d4568-bc97-45b1-bcfb-9596faa24a41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a745e619-ab9d-4b4a-816f-ad7e2fb9f045",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018h81G4MGKg8yrXcBEwiX6v",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 13169,
      "output_tokens": 2895,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1221
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2895,
          "cache_read_input_tokens": 13169,
          "cache_creation_input_tokens": 1221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1221,
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
