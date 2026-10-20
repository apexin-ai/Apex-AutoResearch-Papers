# Research conversation: You are searching for recent (2024-2025) academic papers on AI Text Detection methods. This is for a related work sectio

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad7ad0a40a8db59a5.jsonl`
- **Structured JSON:** [`eb34524546c1e16ee270.json`](../../sessions/eb/eb34524546c1e16ee270.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

56 recorded events

### User

_source line 1 · 2026-05-18T23:24:40.248Z_

You are searching for recent (2024-2025) academic papers on AI Text Detection methods. This is for a related work section of a paper about recursive generation depth estimation — detecting how many times text has been through LLM regeneration cycles using statistical features (perplexity percentiles, entropy, surprisal variance, etc.) with a Random Forest classifier.

Already cited papers (DO NOT include these):
- Min-K% Prob (Shi et al. 2024)
- DetectGPT (Mitchell et al. 2023)
- Binoculars (Hans et al. 2024)
- Fast-DetectGPT (Bao et al. 2024)

Please perform the following web searches and compile results:

1. Search: "AI text detection" new method 2024 2025 ACL EMNLP NeurIPS
2. Search: "machine generated text detection" 2024 2025 ICML ICLR
3. Search: "LLM watermarking" detection 2024 2025
4. Search: "AI generated text detection" survey 2024 2025

For each paper found, provide:
- Full title
- Authors (first author et al. is fine)
- Venue (ICML/NeurIPS/ICLR/ACL/EMNLP/NAACL/COLM/AAAI 2024-2025, or high-citation arXiv)
- One sentence on how it relates to recursive generation depth estimation
- Whether it should be cited: Yes/No/Maybe
- Where it should be cited in the paper
- Brief reason

Only report papers from top venues or highly-cited arXiv preprints. Aim for 3-5 papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "d964cb1d-eafc-4c4d-a6bc-f2437d86c2ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T23:24:40.250Z_

```json
{
  "parentUuid": "d964cb1d-eafc-4c4d-a6bc-f2437d86c2ab",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
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
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "454c9b95-a15e-4ba9-bbc3-fddff37a815a",
  "timestamp": "2026-05-18T23:24:40.250Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T23:24:42.391Z_



I'll perform all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "454c9b95-a15e-4ba9-bbc3-fddff37a815a",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAtzG8tDFAKC1X51fSi4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "032fcf80-3b9c-49e6-9524-2febe42cf011",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYL9EZUdZNJhyakThEi4av",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7713,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7713,
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

_source line 4 · 2026-05-18T23:24:42.950Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019TvJo6uJ2swaaxuVNpDRLm`</summary>

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
  "parentUuid": "032fcf80-3b9c-49e6-9524-2febe42cf011",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAtzG8tDFAKC1X51fSi4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "865f54f0-bd40-4173-bc1b-92175f1c83e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XYL9EZUdZNJhyakThEi4av",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7713,
      "cache_read_input_tokens": 8251,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 86,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7713,
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

_source line 5 · 2026-05-18T23:24:42.953Z_

<details><summary>↩ Tool result · `toolu_019TvJo6uJ2swaaxuVNpDRLm`</summary>

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
  "parentUuid": "865f54f0-bd40-4173-bc1b-92175f1c83e6",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "b6e5619c-8ecc-462d-bde3-abc871ab9a37",
  "sourceToolAssistantUUID": "865f54f0-bd40-4173-bc1b-92175f1c83e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T23:24:45.544Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EDvz69gxTtYhpi1dwHgUCV`</summary>

```json
{
  "query": "\"AI text detection\" new method 2024 2025 ACL EMNLP NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6e5619c-8ecc-462d-bde3-abc871ab9a37",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAtzThuJMozXPyFw8mYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e15ef0b-b46e-4b83-bc81-2adf2b9cee2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU3CrabL2fo6Pb4GW3GJ8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 7 · 2026-05-18T23:24:45.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BjLUff5vyFqSJ6e52EHzYH`</summary>

```json
{
  "query": "\"machine generated text detection\" 2024 2025 ICML ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e15ef0b-b46e-4b83-bc81-2adf2b9cee2d",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAtzThuJMozXPyFw8mYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a67ebfce-c172-4f1f-8859-09dd1f8e4964",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU3CrabL2fo6Pb4GW3GJ8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 8 · 2026-05-18T23:24:46.429Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W3PNdAt26VjabSGtNjjMFN`</summary>

```json
{
  "query": "\"LLM watermarking\" detection 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a67ebfce-c172-4f1f-8859-09dd1f8e4964",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAtzThuJMozXPyFw8mYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41dc5f41-c363-40ae-b366-e4de6fad8569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU3CrabL2fo6Pb4GW3GJ8G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 9 · 2026-05-18T23:24:46.724Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RLBMG9Y3PFKWSeY4zYCUrE`</summary>

```json
{
  "query": "\"AI generated text detection\" survey 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41dc5f41-c363-40ae-b366-e4de6fad8569",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAtzThuJMozXPyFw8mYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f16d0fbb-c072-407a-bbc1-94890490d3fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU3CrabL2fo6Pb4GW3GJ8G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15964,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 227,
          "cache_read_input_tokens": 15964,
          "cache_creation_input_tokens": 1450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1450,
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

_source line 10 · 2026-05-18T23:24:52.881Z_

<details><summary>↩ Tool result · `toolu_01EDvz69gxTtYhpi1dwHgUCV`</summary>

```text
Web search results for query: ""AI text detection" new method 2024 2025 ACL EMNLP NeurIPS"

Links: [{"title":"Efficient detection of AI-generated scientific abstracts with a lightweight transformer | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-35203-3"},{"title":"A Practical Examination of AI-Generated Text Detectors for ...","url":"https://aclanthology.org/2025.findings-naacl.271.pdf"},{"title":"Overview of the NLPCC 2025 Shared Task 1: LLM-Generated Text Detection | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3352-7_21"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/pdf/2305.15047"},{"title":"PROFILER: Black-box AI-generated Text Origin Detection ...","url":"https://aclanthology.org/2025.emnlp-main.1265.pdf"},{"title":"AI-Generated Text is Non-Stationary: Detection via Temporal Tomography","url":"https://arxiv.org/pdf/2508.01754"}]

Based on the search results, here are some recent advances in AI text detection methods from major conferences:

## Recent Methods from Major Conferences

**ACL 2024:**
MAGE: Machine-generated text detection in the wild was presented at the 62nd Annual Meeting of the Association for Computational Linguistics (ACL) in 2024.

Wang et al. presented "Stumbling blocks: stress testing the robustness of machine-generated text detectors under attacks" at ACL 2024.

**EMNLP:**
DetectLLM, which leverages log rank information for zero-shot detection of machine-generated text, was presented at EMNLP 2023.

A new paper "PROFILER: Black-box AI-generated Text Origin Detection" appears in the EMNLP 2025 proceedings.

**NeurIPS:**
Krishna et al. published work on how "Paraphrasing evades detectors of ai-generated text, but retrieval is an effective defense" in Advances in Neural Information Processing Systems (NeurIPS) 2023.

Biscope, an AI-generated text detection method that works by checking memorization of preceding tokens, was presented at NeurIPS 2024.

## Recent 2024-2025 Approaches

Recent work addresses the challenge that sophisticated modern language models enable convincing text generation with subtle modifications that introduce machine artifacts. One new detection paradigm analyzes temporal dynamics using signal processing techniques to improve detection robustness against adversarial attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e15ef0b-b46e-4b83-bc81-2adf2b9cee2d",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "8bb077a6-0a7a-48f6-9a65-897ca4044c9a",
  "sourceToolAssistantUUID": "1e15ef0b-b46e-4b83-bc81-2adf2b9cee2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T23:24:53.293Z_

<details><summary>↩ Tool result · `toolu_01BjLUff5vyFqSJ6e52EHzYH`</summary>

```text
Web search results for query: ""machine generated text detection" 2024 2025 ICML ICLR"

Links: [{"title":"Published as a conference paper at ICLR 2024 DETECTING MACHINE-GENERATED TEXTS","url":"https://openreview.net/pdf?id=3fEKavFsnv"},{"title":"Overview of the NLPCC 2025 Shared Task 1: LLM-Generated Text Detection | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3352-7_21"},{"title":"PROFILER: Black-box AI-generated Text Origin Detection ...","url":"https://aclanthology.org/2025.emnlp-main.1265.pdf"},{"title":"On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/pdf/2304.04736"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual   Machine-Generated Text Detection","url":"https://arxiv.org/pdf/2404.14183"}]

I found several relevant results on machine-generated text detection research from 2024-2025. Here's what the search revealed:

## ICLR 2024
A paper on "Detecting Machine-Generated Texts" was published at ICLR 2024, using approaches based on maximum mean discrepancy.

## ICML 2024
A paper titled "Spotting LLMs with binoculars: zero-shot detection of machine-generated text" appeared at ICML 2024 (July 21-27, Vienna). Additionally, another approach called "Fast-detectgpt: efficient zero-shot detection of machine-generated text via conditional probability curvature" was presented at ICLR 2024.

## ICML 2025
At ICML 2025, a framework called DivEye was proposed that leverages surprisal-based features to detect AI-generated text.

## Related Work from 2024
SemEval-2024 Task 8 presented a shared task on "Multidomain, Multimodel and Multilingual Machine-Generated Text Detection", which included subtasks for binary classification (human vs. machine), detecting the specific source, and identifying transition points from human to machine authorship.

There's also recent work in 2025 on detecting LLM-generated Chinese texts through the DetectRL-ZH detection dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a67ebfce-c172-4f1f-8859-09dd1f8e4964",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "8f158248-5478-4543-bf4b-073215bb490d",
  "sourceToolAssistantUUID": "a67ebfce-c172-4f1f-8859-09dd1f8e4964",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T23:24:53.844Z_

<details><summary>↩ Tool result · `toolu_01RLBMG9Y3PFKWSeY4zYCUrE`</summary>

```text
Web search results for query: ""AI generated text detection" survey 2024 2025"

Links: [{"title":"Enhancing the Robustness of AI-Generated Text Detectors: A Survey","url":"https://www.mdpi.com/2227-7390/13/13/2145"},{"title":"Towards Possibilities & Impossibilities of AI-generated Text Detection:   A Survey","url":"https://arxiv.org/pdf/2310.15264"},{"title":"A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f582daa2f2822c0aa1291fe3925f69c25280e37e"},{"title":"A Survey on AI-Generated Text Detection: Methods, Challenges, and Future Directions","url":"https://www.researchgate.net/publication/400099134_A_Survey_on_AI-Generated_Text_Detection_Methods_Challenges_and_Future_Directions"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with   Current Methods","url":"https://arxiv.org/pdf/2406.15583"},{"title":"The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161"},{"title":"On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/pdf/2304.04736"},{"title":"Are AI Detectors Good Enough? A Survey on Quality of Datasets With   Machine-Generated Texts","url":"https://arxiv.org/pdf/2410.14677"}]

Here are the key findings from recent surveys on AI-generated text detection:

## Recent Surveys (2024-2025)

A recent survey published in June 2025 provides a systematic overview of existing research on enhancing the robustness of AI-generated text detectors, with a focus on text perturbation robustness, out-of-distribution (OOD) robustness, and AI–human hybrid text (AHT) detection robustness.

AI-generated text detection (AIGTD) is the identification of text generated by an AI system, leveraging various technological approaches to automatically recognize, examine, and handle the content of the text. With the rapid advancements in generative AI technologies, such as ChatGPT and GPT-4, the ability to generate text content like humans has become increasingly powerful and accessible.

## Detection Approaches

State-of-the-art approaches to AIGT detection include watermarking, statistical and stylistic analysis, and machine learning classification. Common approaches include leveraging watermarking techniques, designing detectors based on statistical metrics, or fine-tuning classifiers on a set of training samples.

## Key Challenges

The complexity and diversity of AIGT and counter-detection methods in real-world applications present substantial challenges for AIGT detection. Additionally, state-of-art detection frameworks can be vulnerable and fragile to paraphrasing-based attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f16d0fbb-c072-407a-bbc1-94890490d3fb",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "2fc4eeee-6600-4d60-b472-ec76cf949d85",
  "sourceToolAssistantUUID": "f16d0fbb-c072-407a-bbc1-94890490d3fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T23:24:55.331Z_

<details><summary>↩ Tool result · `toolu_01W3PNdAt26VjabSGtNjjMFN`</summary>

```text
Web search results for query: ""LLM watermarking" detection 2024 2025"

Links: [{"title":"[2411.13868] Robust Detection of Watermarks for Large Language Models Under Human Edits","url":"https://arxiv.org/abs/2411.13868"},{"title":"GitHub - THU-BPM/MarkLLM: [EMNLP 2024 Demo] MarkLLM: An Open-Source Toolkit for LLM Watermarking · GitHub","url":"https://github.com/THU-BPM/MarkLLM"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0f7ee1901fef1da4dae2b88dfd43195-Paper-Conference.pdf"},{"title":"LLM Watermarking Using Mixtures and Statistical-to-Computational Gaps","url":"https://www.math.uci.edu/~rvershyn/papers/av-LLM-watermarking.pdf"},{"title":"Baselines for Identifying Watermarked Large Language Models","url":"https://arxiv.org/pdf/2305.18456"},{"title":"Can Watermarked LLMs be Identified by Users via Crafted Prompts?","url":"https://arxiv.org/pdf/2410.03168"},{"title":"Towards Better Statistical Understanding of Watermarking LLMs","url":"https://arxiv.org/pdf/2403.13027"}]

Based on the search results, here's what I found about LLM watermarking detection in 2024-2025:

## Recent Advances in Watermark Detection

Watermarking has offered an effective approach to distinguishing text generated by large language models (LLMs) from human-written text. However, researchers have identified key challenges and developed new detection methods.

### Key Challenges

The pervasive presence of human edits on LLM-generated text dilutes watermark signals, thereby significantly degrading detection performance of existing methods. Additionally, no work has considered the imperceptibility of watermarked LLMs, and LLM service providers may not disclose the existence of watermarks, as it could reduce user willingness to use the service and make it more vulnerable to attacks.

### Detection Methods

A new method called a truncated goodness-of-fit test (Tr-GoF) was introduced for detecting watermarked text under human edits. The Water-Probe algorithm has been developed for identifying watermarked LLMs by constructing two prompts with similar output distributions, then sampling repeatedly using two fixed watermark keys for each prompt, with watermark presence determined by comparing the similarity of distribution differences between the two prompts.

### Watermarking Schemes

The prominent family of Red-Green watermarks achieves detection by, at each step of generation, selecting a context-dependent pseudorandom set of logits to be boosted. Recently proposed families of Fixed-Sampling and Cache-Augmented schemes have focused on developing watermarks that aim to preserve the output distribution of the LLM.

### Toolkit Development

MarkLLM is an open-source toolkit for LLM watermarking that was presented as a demo at EMNLP 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41dc5f41-c363-40ae-b366-e4de6fad8569",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "b07568ab-7415-492c-8421-66237a0d1bce",
  "sourceToolAssistantUUID": "41dc5f41-c363-40ae-b366-e4de6fad8569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-18T23:24:58.256Z_

Let me do a few more targeted searches to get precise venue/author information for the most relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b07568ab-7415-492c-8421-66237a0d1bce",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu1NcqWYsoEm2RPy8rE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f2d3b80-bbee-41e7-ac99-e8278572d68f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8oP78gYrn636dyU9fTPug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 2404,
      "cache_read_input_tokens": 17414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2404,
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

_source line 15 · 2026-05-18T23:24:58.733Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UzQ4MtjqTSEwQntQbrtgPx`</summary>

```json
{
  "query": "Biscope NeurIPS 2024 AI text detection memorization preceding tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f2d3b80-bbee-41e7-ac99-e8278572d68f",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu1NcqWYsoEm2RPy8rE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a4092ee-714f-44ae-a160-1c83869a14ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8oP78gYrn636dyU9fTPug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 2404,
      "cache_read_input_tokens": 17414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2404,
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

_source line 16 · 2026-05-18T23:24:59.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X9LsPkr87QjuftFyPYLsGh`</summary>

```json
{
  "query": "DivEye ICML 2025 surprisal diversity AI text detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a4092ee-714f-44ae-a160-1c83869a14ee",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu1NcqWYsoEm2RPy8rE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "004c8d29-7437-4c05-b1dc-383b0490fc9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8oP78gYrn636dyU9fTPug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 2404,
      "cache_read_input_tokens": 17414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2404,
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

_source line 17 · 2026-05-18T23:25:00.143Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019KKJHzbexXEoHPs6Ur7VXo`</summary>

```json
{
  "query": "MAGE machine generated text detection wild ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "004c8d29-7437-4c05-b1dc-383b0490fc9c",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu1NcqWYsoEm2RPy8rE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db2f06b7-e901-48eb-8e39-5aedb96457e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8oP78gYrn636dyU9fTPug",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 2404,
      "cache_read_input_tokens": 17414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2404,
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

_source line 18 · 2026-05-18T23:25:00.807Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ps1uX1i8UDLCzMEaCPfjdF`</summary>

```json
{
  "query": "\"Towards Possibilities Impossibilities AI-generated Text Detection Survey\" Tang 2024 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2f06b7-e901-48eb-8e39-5aedb96457e7",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu1NcqWYsoEm2RPy8rE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c237c9f-dfa2-4702-997c-aff7f952a9e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8oP78gYrn636dyU9fTPug",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 2404,
      "cache_read_input_tokens": 17414,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 776,
          "output_tokens": 246,
          "cache_read_input_tokens": 17414,
          "cache_creation_input_tokens": 2404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2404,
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

_source line 19 · 2026-05-18T23:25:04.839Z_

<details><summary>↩ Tool result · `toolu_01UzQ4MtjqTSEwQntQbrtgPx`</summary>

```text
Web search results for query: "Biscope NeurIPS 2024 AI text detection memorization preceding tokens"

Links: [{"title":"BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/bc808cf2d2444b0abcceca366b771389-Abstract-Conference.html"},{"title":"GitHub - MarkGHX/BiScope: Official Implementation of NeurIPS 2024 paper - BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens","url":"https://github.com/MarkGHX/BiScope"},{"title":"BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens | OpenReview","url":"https://openreview.net/forum?id=Hew2JSDycr"},{"title":"NeurIPS Poster BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens","url":"https://nips.cc/virtual/2024/poster/95814"},{"title":"NeurIPS Poster BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens","url":"https://neurips.cc/virtual/2024/poster/95814"},{"title":"ai-generated-text-detection · GitHub Topics · GitHub","url":"https://github.com/topics/ai-generated-text-detection"},{"title":"BISCOPE: AI-generated Text Detection by Checking ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/bc808cf2d2444b0abcceca366b771389-Paper-Conference.pdf"},{"title":"BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BiScope:-AI-generated-Text-Detection-by-Checking-of-Guo-Cheng/97649635b7b36352df5839ba5ed87e00e2430aeb"},{"title":"BiScope: AI-generated Text Detection by Checking ...","url":"https://neurips.cc/media/neurips-2024/Slides/95814.pdf"}]

I found comprehensive information about BiScope from NeurIPS 2024. Here's what the research presents:

## BiScope: AI-generated Text Detection

BiScope addresses the pressing need to detect text generated by Large Language Models (LLMs) in order to identify and prevent misuse across various applications, including misinformation and academic dishonesty.

### Core Innovation

The key observation is that how well the current token's output logits memorizes the closely preceding input tokens provides strong evidence for AI-generated text detection. The researchers propose a novel bi-directional calculation method that measures cross-entropy losses between an output logits and the ground-truth token (forward) and between the output logits and the immediately preceding input token (backward).

### Performance Results

BiScope was evaluated on texts generated by five latest commercial LLMs across five heterogeneous datasets, including both natural language and code, demonstrating superior detection accuracy and robustness compared to six existing baseline methods, exceeding state-of-the-art non-commercial methods' detection accuracy by over 0.30 F1 score and achieving over 0.95 detection F1 score on average. It also outperforms GPTZero, a commercial tool based on a commercial LLM trained with enormous volumes of data.

The official implementation is available on GitHub at https://github.com/MarkGHX/BiScope.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a4092ee-714f-44ae-a160-1c83869a14ee",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "b1a7d3d9-8d5f-4946-9809-1dc4981c77c3",
  "sourceToolAssistantUUID": "6a4092ee-714f-44ae-a160-1c83869a14ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T23:25:05.156Z_

<details><summary>↩ Tool result · `toolu_01Ps1uX1i8UDLCzMEaCPfjdF`</summary>

```text
Web search results for query: ""Towards Possibilities Impossibilities AI-generated Text Detection Survey" Tang 2024 venue"

Links: [{"title":"[2310.15264v1] Towards Possibilities & Impossibilities of AI-generated Text Detection: A Survey","url":"https://arxiv.org/abs/2310.15264v1"},{"title":"[2310.15264] Towards Possibilities & Impossibilities of AI-generated Text Detection: A Survey","url":"https://arxiv.org/abs/2310.15264"},{"title":"Towards Possibilities & Impossibilities of AI-generated Text Detection:   A Survey","url":"https://arxiv.org/pdf/2310.15264"},{"title":"A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f582daa2f2822c0aa1291fe3925f69c25280e37e"},{"title":"Distinguishing Human From Machine: A Review of Advances and Challenges in AI-Generated Text Detection | International Journal of Interactive Multimedia and Artificial Intelligence","url":"https://revistas.unir.net/index.php/ijimai/article/view/234"},{"title":"Towards Possibilities & Impossibilities of AI-generated Text Detection: A Survey. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1ad91e400c9d3f7ec24c424913c22319c"}]

Based on the search results, I found the paper you're looking for. The survey "Towards Possibilities & Impossibilities of AI-generated Text Detection" was published in Transactions on Machine Learning Research (TMLR) in 2023.

The paper was authored by Soumya Suvra Ghosal, Souradip Chakraborty, Jonas Geiping, Furong Huang, Dinesh Manocha, and Amrit Singh Bedi.

However, I should note that the search results indicate this paper was published in 2023, not 2024 as mentioned in your query. The paper was posted to arXiv on October 23, 2023. If you were looking for a different paper by Tang from 2024, you may want to refine your search, as the results primarily show this survey by Ghosal et al. rather than one authored by Tang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c237c9f-dfa2-4702-997c-aff7f952a9e4",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "ad060f09-fc2a-4eb8-a70d-8e5eb3fa83c9",
  "sourceToolAssistantUUID": "4c237c9f-dfa2-4702-997c-aff7f952a9e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T23:25:06.785Z_

<details><summary>↩ Tool result · `toolu_019KKJHzbexXEoHPs6Ur7VXo`</summary>

```text
Web search results for query: "MAGE machine generated text detection wild ACL 2024"

Links: [{"title":"GitHub - yafuly/MAGE: Machine-generated text detection in the wild (ACL 2024) · GitHub","url":"https://github.com/yafuly/MAGE"},{"title":"MAGE: Machine-generated Text Detection in the Wild - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.3/"},{"title":"MAGE: Machine-generated Text Detection in the Wild | Qintong Li","url":"https://qtli.github.io/publication/detection/"},{"title":"MAGE/README.md at main · yafuly/MAGE","url":"https://github.com/yafuly/MAGE/blob/main/README.md"},{"title":"MAGE: Machine-generated Text Detection in the Wild - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230513242L/abstract"},{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"[2305.13242] MAGE: Machine-generated Text Detection in the Wild","url":"https://arxiv.org/abs/2305.13242"},{"title":"MAGE: Machine-generated Text Detection in the Wild","url":"https://arxiv.org/pdf/2305.13242"}]

Based on the search results, here's what I found about MAGE:

## MAGE: Machine-generated Text Detection in the Wild (ACL 2024)

MAGE is a comprehensive testbed for deepfake text detection, gathering texts from various human writings and deepfake texts generated by different LLMs.

### Key Features:

**Dataset Composition:**
The dataset includes machine-generated texts from 27 mainstream LLMs from 7 sources, such as OpenAI, LLaMA, and EleutherAI. The testbed collects human-written texts from 7 distinct writing tasks (story generation, news writing, and scientific writing) and generates corresponding machine-generated texts with 27 LLMs under 3 representative prompt types.

**Testbed Complexity:**
The dataset includes 8 systematic testbeds with increasing wildness and detection difficulty. Each testbed exhibits progressively higher levels of "wildness" in terms of distributional variance and detection complexity, starting with detecting texts generated by a white-box LLM within a specific domain, then incorporating texts from multiple LLMs across various writing tasks, with the most challenging testbed requiring detection of out-of-domain texts generated by newly developed LLMs and against paraphrasing attacks.

### Results:

The top-performing detector can identify 84.12% out-of-domain texts generated by a new LLM, indicating the feasibility for application scenarios. However, empirical results on mainstream detection methods demonstrate the difficulties associated with detecting deepfake text in a wide-ranging testbed, particularly in out-of-distribution scenarios, which aligns with the diminishing linguistic differences between the two text sources.

The paper was accepted by ACL 2024 on May 16, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db2f06b7-e901-48eb-8e39-5aedb96457e7",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "10077c83-bef0-4f81-814a-baca7199223e",
  "sourceToolAssistantUUID": "db2f06b7-e901-48eb-8e39-5aedb96457e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T23:25:07.012Z_

<details><summary>↩ Tool result · `toolu_01X9LsPkr87QjuftFyPYLsGh`</summary>

```text
Web search results for query: "DivEye ICML 2025 surprisal diversity AI text detection"

Links: [{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"DivEye","url":"https://diveye.vercel.app/"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection","url":"https://ceur-ws.org/Vol-4038/paper_282.pdf"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"}]

Based on the search results, here's what I found about DivEye and its presentation at ICML 2025:

## DivEye: AI-Generated Text Detection Framework

DivEye is a novel detection framework that leverages surprisal-based features to capture fluctuations in lexical and structural unpredictability, a signal more prominent in human-authored text.

### Key Performance Metrics

DivEye outperforms existing zero-shot detectors by up to 33.2%, matches fine-tuned baselines, and boosts existing detectors by up to 18.7% when used as an auxiliary signal.

### Core Approach

Human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, and DivEye captures this signal through a set of interpretable statistical features. Human writers naturally introduce irregularities, such as unexpected lexical choices or structural shifts, that make their text inherently more diverse.

### Presentation at ICML 2025

DivEye was presented as a poster in the Workshop: DIG-BUGS: Data in Generative Models (The Bad, the Ugly, and the Greats) on Saturday, July 19, 2025.

### Additional Features

DivEye demonstrates multilingual generalizability using both English and Chinese splits of the HC3 dataset, with consistent performance and higher F1 scores across both languages, suggesting that surprisal-based statistical features are not heavily language-specific.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "004c8d29-7437-4c05-b1dc-383b0490fc9c",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "00ed6223-0f38-4079-abef-2654fb04e0a2",
  "sourceToolAssistantUUID": "004c8d29-7437-4c05-b1dc-383b0490fc9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T23:25:09.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKZJHzjLe8ERGjeyKHkW88`</summary>

```json
{
  "query": "Kirchenbauer watermark large language models ICML 2023 2024 citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00ed6223-0f38-4079-abef-2654fb04e0a2",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu2EXhXnDEGDvKavkhf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89d43386-ffec-4432-9f44-663c00970444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqcmpdP9wArSxdUd1ktFxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1411,
      "cache_creation_input_tokens": 2859,
      "cache_read_input_tokens": 19818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2859,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 24 · 2026-05-18T23:25:10.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QxKvYWeRAcDeet2NGG1mRm`</summary>

```json
{
  "query": "Ghostbuster detecting text ghostwritten LLM Verma ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89d43386-ffec-4432-9f44-663c00970444",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu2EXhXnDEGDvKavkhf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "914b3cc0-19c1-4fa6-8eed-022f099dd3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqcmpdP9wArSxdUd1ktFxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1411,
      "cache_creation_input_tokens": 2859,
      "cache_read_input_tokens": 19818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2859,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 25 · 2026-05-18T23:25:11.713Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01348pg4oJn9N6DGXQUGpLoe`</summary>

```json
{
  "query": "\"truncated goodness-of-fit\" watermark detection human edits ICLR 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "914b3cc0-19c1-4fa6-8eed-022f099dd3d0",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu2EXhXnDEGDvKavkhf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1cdc5a8-8bd3-4dd3-bab6-cd34ba58ef4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqcmpdP9wArSxdUd1ktFxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1411,
      "cache_creation_input_tokens": 2859,
      "cache_read_input_tokens": 19818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2859,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 26 · 2026-05-18T23:25:12.147Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JTfpq7td5hYdAa5beE7V3z`</summary>

```json
{
  "query": "BiScope authors Guo NeurIPS 2024 first author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1cdc5a8-8bd3-4dd3-bab6-cd34ba58ef4c",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu2EXhXnDEGDvKavkhf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ed62205-b6b6-416e-9aaf-e82e3120873f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqcmpdP9wArSxdUd1ktFxs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1411,
      "cache_creation_input_tokens": 2859,
      "cache_read_input_tokens": 19818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2859,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 27 · 2026-05-18T23:25:16.164Z_

<details><summary>↩ Tool result · `toolu_01JTfpq7td5hYdAa5beE7V3z`</summary>

```text
Web search results for query: "BiScope authors Guo NeurIPS 2024 first author"

Links: [{"title":"BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/bc808cf2d2444b0abcceca366b771389-Abstract-Conference.html"},{"title":"GitHub - MarkGHX/BiScope: Official Implementation of NeurIPS 2024 paper - BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens","url":"https://github.com/MarkGHX/BiScope"},{"title":"NeurIPS Poster BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens","url":"https://neurips.cc/virtual/2024/poster/95814"},{"title":"Autoencoder-based phenotyping of ophthalmic images highlights genetic loci influencing retinal morphology and provides informative biomarkers","url":"https://www.medrxiv.org/content/10.1101/2023.06.15.23291410.full.pdf"},{"title":"BISCOPE: AI-generated Text Detection by Checking ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/bc808cf2d2444b0abcceca366b771389-Paper-Conference.pdf"},{"title":"Performance of a Large Language Model in BI-RADS Classification of Ultrasound Based Breast Lesions","url":"https://www.medrxiv.org/content/10.1101/2025.09.28.25336860.full.pdf"},{"title":"Distinguishing GPT-4-generated Radiology Abstracts from Original Abstracts: Performance of Blinded Human Observers and AI Content Detector","url":"https://www.medrxiv.org/content/10.1101/2023.04.28.23289283.full.pdf"}]

Based on the search results, the first author of the BiScope paper published at NeurIPS 2024 is Hanxi Guo. The full author list is: Hanxi Guo, Siyuan Cheng, Xiaolong Jin, Zhuo Zhang, Kaiyuan Zhang, Guanhong Tao, Guangyu Shen, and Xiangyu Zhang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ed62205-b6b6-416e-9aaf-e82e3120873f",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "8214c821-5442-4a41-8cd7-e80e6d529de4",
  "sourceToolAssistantUUID": "1ed62205-b6b6-416e-9aaf-e82e3120873f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T23:25:16.218Z_

<details><summary>↩ Tool result · `toolu_01BKZJHzjLe8ERGjeyKHkW88`</summary>

```text
Web search results for query: "Kirchenbauer watermark large language models ICML 2023 2024 citation"

Links: [{"title":"[2301.10226] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226"},{"title":"A Watermark for Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10522346-watermark-large-language-models"},{"title":"ICML Poster A Watermark for Large Language Models","url":"https://icml.cc/virtual/2023/poster/24544"},{"title":"[PDF] A Watermark for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Watermark-for-Large-Language-Models-Kirchenbauer-Geiping/cb5b71a622aff47014d4f28a958679629a8b6363"},{"title":"GitHub - jwkirchenbauer/lm-watermarking · GitHub","url":"https://github.com/jwkirchenbauer/lm-watermarking"},{"title":"dblp: A Watermark for Large Language Models.","url":"https://dblp.org/rec/conf/icml/KirchenbauerGWK23.html"},{"title":"A Watermark for Large Language Models","url":"https://proceedings.mlr.press/v202/kirchenbauer23a.html"},{"title":"A Watermark for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/367388838_A_Watermark_for_Large_Language_Models"},{"title":"[2306.04634] On the Reliability of Watermarks for Large Language Models","url":"https://arxiv.org/abs/2306.04634"}]

Based on the search results, here's what I found about the Kirchenbauer watermark research:

## Primary Publication

The main paper "A Watermark for Large Language Models" by John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein was published at ICML 2023, pages 17061-17084.

## Paper Details

The watermarking approach embeds signals into generated text that are invisible to humans but algorithmically detectable from a short span of tokens. The watermark can be embedded with negligible impact on text quality and works by selecting a randomized set of "green" tokens before a word is generated, then softly promoting use of green tokens during sampling.

## Citation Format

The BibTeX citation is:
@InProceedings{pmlr-v202-kirchenbauer23a, title = {A Watermark for Large Language Models}, author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom}, booktitle = {Proceedings of the 40th International Conference on Machine Learning}, pages = {17061--17084}, year = {2023}

## Follow-up Work

A follow-up paper "On the Reliability of Watermarks for Large Language Models" was accepted for publication and presented at ICLR 2024 in Vienna, Austria.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89d43386-ffec-4432-9f44-663c00970444",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "752811eb-1455-4e7c-977c-c32d47f89395",
  "sourceToolAssistantUUID": "89d43386-ffec-4432-9f44-663c00970444",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T23:25:17.132Z_

<details><summary>↩ Tool result · `toolu_01QxKvYWeRAcDeet2NGG1mRm`</summary>

```text
Web search results for query: "Ghostbuster detecting text ghostwritten LLM Verma ACL 2024"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"(PDF) Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://www.researchgate.net/publication/371009726_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"[PDF] Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ghostbuster:-Detecting-Text-Ghostwritten-by-Large-Verma-Fleisig/c4a7adcee41da8e1dfd29a0cbbf156f86940f487"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2023/11/14/ghostbuster/"},{"title":"GitHub - vivek3141/ghostbuster: Ghostbuster: Detecting Text Ghostwritten by Large Language Models (NAACL 2024) · GitHub","url":"https://github.com/vivek3141/ghostbuster"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"}]

Based on the search results, here's what I found about Ghostbuster:

Ghostbuster is a state-of-the-art system for detecting AI-generated text, introduced by Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan Klein in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024).

The method works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether documents are AI-generated.

Crucially, Ghostbuster does not require access to token probabilities from the target model, making it useful for detecting text generated by black-box models or unknown model versions.

In terms of performance, Ghostbuster achieves 99.0 F1 when evaluated across domains, which is 5.9 F1 higher than the best preexisting model, and outperforms all previous approaches in generalization across writing domains, prompting strategies, and language models.

The researchers also released three new datasets of human- and AI-generated text as detection benchmarks in the domains of student essays, creative writing, and news articles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "914b3cc0-19c1-4fa6-8eed-022f099dd3d0",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "5c5c8659-f812-4ca3-98bf-edad8fb8fe86",
  "sourceToolAssistantUUID": "914b3cc0-19c1-4fa6-8eed-022f099dd3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T23:25:19.053Z_

<details><summary>↩ Tool result · `toolu_01348pg4oJn9N6DGXQUGpLoe`</summary>

```text
Web search results for query: ""truncated goodness-of-fit" watermark detection human edits ICLR 2025 authors"

Links: [{"title":"Robust Detection of Watermarks for Large Language Models Under Human Edits","url":"https://arxiv.org/pdf/2411.13868"},{"title":"Robust detection of watermarks for large language models under human edits | Journal of the Royal Statistical Society Series B: Statistical Methodology | Oxford Academic","url":"https://academic.oup.com/jrsssb/advance-article-abstract/doi/10.1093/jrsssb/qkaf056/8261309"},{"title":"Robust Detection of Watermarks for Large Language Models Under Human Edits","url":"https://arxiv.org/html/2411.13868v3"},{"title":"Robust Detection of Watermarks for Large Language Models Under Human Edits - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241113868L/abstract"},{"title":"[2411.13868v1] Robust Detection of Watermarks for Large Language Models Under Human Edits","url":"http://arxiv.org/abs/2411.13868v1"},{"title":"[2411.13868] Robust Detection of Watermarks for Large Language Models Under Human Edits","url":"https://arxiv.org/abs/2411.13868"},{"title":"Robust Detection of Watermarks for Large Language Models ...","url":"https://www.arxiv.org/pdf/2411.13868v2"},{"title":"On the Empirical Power of Goodness-of-Fit Tests in Watermark Detection","url":"https://arxiv.org/html/2510.03944v1"},{"title":"Optimal Estimation of Watermark Proportions in Hybrid AI-Human Texts","url":"https://arxiv.org/html/2506.22343v1"},{"title":"On the Empirical Power of Goodness-of-Fit Tests in Watermark Detection","url":"https://arxiv.org/pdf/2510.03944"}]

Based on the search results, I found information about the truncated goodness-of-fit (Tr-GoF) method for watermark detection under human edits:

## Key Information

**Paper Title:** Robust Detection of Watermarks for Large Language Models Under Human Edits

**Authors:** Xiang Li, Feng Ruan, Huiyuan Wang, Qi Long, Weijie J. Su

**Method:** The paper introduces a truncated goodness-of-fit test (Tr-GoF) for detecting watermarked text under human edits by modeling human edits through mixture model detection.

**Publication Status:** The work was initially posted on arXiv on November 21, 2024, and has been published in the Journal of the Royal Statistical Society Series B: Statistical Methodology in 2025. Note that this appears to be published in a journal (JRSSSB) rather than at ICLR 2025.

**Key Results:** The Tr-GoF test achieves optimality in robust detection of the Gumbel-max watermark in a certain asymptotic regime of substantial text modifications and vanishing watermark signals.

The paper addresses the problem that human edits on LLM-generated text dilute watermark signals, significantly degrading detection performance of existing methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1cdc5a8-8bd3-4dd3-bab6-cd34ba58ef4c",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "aa2e44d4-6031-4f01-90d1-ce8f501c1fa5",
  "sourceToolAssistantUUID": "a1cdc5a8-8bd3-4dd3-bab6-cd34ba58ef4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T23:25:22.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0144howb6Nt7EtMqKcraMF9z`</summary>

```json
{
  "query": "DivEye ICML 2025 Basani Chen authors main conference or workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa2e44d4-6031-4f01-90d1-ce8f501c1fa5",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu37za9pdDrnFZWz1f6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc2e997f-9da9-4474-939b-22ff6e0fe8e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4JGWDD6nWawLRkYCgXgKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 4189,
      "cache_read_input_tokens": 22677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4189,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 32 · 2026-05-18T23:25:23.408Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CVSVfPXP227oATvEMNBaYE`</summary>

```json
{
  "query": "Ghostbuster Verma NAACL 2024 feature-based classifier perplexity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2e997f-9da9-4474-939b-22ff6e0fe8e6",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu37za9pdDrnFZWz1f6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85b60306-44e8-4c9d-bfcb-2b62acc8c1f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4JGWDD6nWawLRkYCgXgKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 4189,
      "cache_read_input_tokens": 22677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4189,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 33 · 2026-05-18T23:25:23.889Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gfozmdt2oDQairdJvKyVjQ`</summary>

```json
{
  "query": "SemEval-2024 Task 8 machine generated text detection Wang venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85b60306-44e8-4c9d-bfcb-2b62acc8c1f0",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu37za9pdDrnFZWz1f6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7351dff7-2dff-4980-b649-e43580b18117",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4JGWDD6nWawLRkYCgXgKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 4189,
      "cache_read_input_tokens": 22677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4189,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 34 · 2026-05-18T23:25:24.176Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0143WKB6VemtDYgjAjWntgQm`</summary>

```json
{
  "query": "MAGE Li ACL 2024 authors first author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7351dff7-2dff-4980-b649-e43580b18117",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu37za9pdDrnFZWz1f6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e607964a-b0e9-4c95-80ea-a4e3a58dbf3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V4JGWDD6nWawLRkYCgXgKo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 4189,
      "cache_read_input_tokens": 22677,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4189
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 625,
          "output_tokens": 227,
          "cache_read_input_tokens": 22677,
          "cache_creation_input_tokens": 4189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4189,
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

_source line 35 · 2026-05-18T23:25:26.787Z_

<details><summary>↩ Tool result · `toolu_0144howb6Nt7EtMqKcraMF9z`</summary>

```text
Web search results for query: "DivEye ICML 2025 Basani Chen authors main conference or workshop"

Links: [{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"DivEye","url":"https://diveye.vercel.app/"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection","url":"https://ceur-ws.org/Vol-4038/paper_282.pdf"}]

Based on the search results, DivEye was presented as a poster in the DIG-BUGS (Data in Generative Models - The Bad, the Ugly, and the Greats) workshop at ICML 2025, not in the main conference. The authors are Advik Basani and Pin-Yu Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc2e997f-9da9-4474-939b-22ff6e0fe8e6",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "c2ed42c3-1974-4910-89e0-2f6b7c4ac2bb",
  "sourceToolAssistantUUID": "fc2e997f-9da9-4474-939b-22ff6e0fe8e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T23:25:28.912Z_

<details><summary>↩ Tool result · `toolu_01Gfozmdt2oDQairdJvKyVjQ`</summary>

```text
Web search results for query: "SemEval-2024 Task 8 machine generated text detection Wang venue"

Links: [{"title":"SemEval-2024 Task 8","url":"https://iris.cnr.it/bitstream/20.500.14243/532501/1/2024.semeval-1.279.pdf"},{"title":"Groningen Team F at SemEval-2024 Task 8: Detecting Machine-Generated Text using Feature-Based Machine Learning Models - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.268/"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"KInIT at SemEval-2024 Task 8: Fine-tuned LLMs for Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2402.13671"},{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual   Machine-Generated Text Detection","url":"https://arxiv.org/pdf/2404.14183"}]

Based on the search results, I found information about SemEval-2024 Task 8:

SemEval-2024 Task 8 is titled "Multidomain, Multimodel and Multilingual Machine-Generated Text Detection" and was held in Mexico City, Mexico.

The task was organized by Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, and Thomas Arnold.

The task featured three subtasks: Subtask A is a binary classification task determining whether a text is written by a human or generated by a machine with two tracks (monolingual and multilingual); Subtask B is to detect the exact source of a text; and Subtask C aims to identify the changing point where authorship transitions from human to machine.

The task garnered significant interest from researchers, with 126, 59, 70, and 30 teams submitting entries for Subtask A Monolingual, Subtask A Multilingual, Subtask B, and Subtask C, respectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7351dff7-2dff-4980-b649-e43580b18117",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "5bee7002-0ccf-459b-bb20-1174a1ac9e3b",
  "sourceToolAssistantUUID": "7351dff7-2dff-4980-b649-e43580b18117",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T23:25:29.066Z_

<details><summary>↩ Tool result · `toolu_0143WKB6VemtDYgjAjWntgQm`</summary>

```text
Web search results for query: "MAGE Li ACL 2024 authors first author"

Links: [{"title":"MAGE: Machine-generated Text Detection in the Wild - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.3/"},{"title":"GitHub - yafuly/MAGE: Machine-generated text detection in the wild (ACL 2024) · GitHub","url":"https://github.com/yafuly/MAGE"},{"title":"MAGE/README.md at main · yafuly/MAGE","url":"https://github.com/yafuly/MAGE/blob/main/README.md"},{"title":"[ACL 2024] AI-generated Text Detection Research Trends - LG AI Research BLOG","url":"https://www.lgresearch.ai/blog/view?seq=482"},{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"ACL 2024: Bangkok, Thailand","url":"https://dblp.org/db/conf/acl/acl2024-1.html"},{"title":"MAGE: Machine-generated Text Detection in the Wild | Request PDF","url":"https://www.researchgate.net/publication/384198450_MAGE_Machine-generated_Text_Detection_in_the_Wild"},{"title":"[2305.13242] MAGE: Machine-generated Text Detection in the Wild","url":"https://arxiv.org/abs/2305.13242"}]

Based on the search results, here is the information about the MAGE paper at ACL 2024:

**Paper:** MAGE: Machine-generated Text Detection in the Wild

**Authors:** Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang, Longyue Wang, Linyi Yang, Shuming Shi, Yue Zhang

**First Author:** Yafu Li

**Conference:** Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2024


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e607964a-b0e9-4c95-80ea-a4e3a58dbf3b",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "192b9476-4482-4ec4-9c1d-7ee4444cd2ac",
  "sourceToolAssistantUUID": "e607964a-b0e9-4c95-80ea-a4e3a58dbf3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T23:25:30.072Z_

<details><summary>↩ Tool result · `toolu_01CVSVfPXP227oATvEMNBaYE`</summary>

```text
Web search results for query: "Ghostbuster Verma NAACL 2024 feature-based classifier perplexity"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"Not all tokens are created equal: Perplexity Attention Weighted Networks for AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S156625352500538X"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"GitHub - vivek3141/ghostbuster: Ghostbuster: Detecting Text Ghostwritten by Large Language Models (NAACL 2024) · GitHub","url":"https://github.com/vivek3141/ghostbuster"},{"title":"TECHNICAL REPORT ON THE CHECKFOR.AI AI-GENERATED TEXT CLASSIFIER Bradley Emi∗","url":"https://checkforai-public.s3.amazonaws.com/checkforai_technical_report_v1.pdf"},{"title":"M-RangeDetector: Enhancing Generalization in Machine- ...","url":"https://aclanthology.org/2025.findings-acl.469.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"}]

Based on the search results, I found information about Ghostbuster from the NAACL 2024 paper by Verma et al.:

Ghostbuster is a state-of-the-art system for detecting AI-generated text that works by passing documents through a series of weaker language models, running a structured search over possible combinations of their features, and then training a classifier on the selected features to predict whether documents are AI-generated.

Regarding the feature-based approach and perplexity: One of the baselines tested was a perplexity-only model, which resulted in a brittle and insufficiently expressive model with particularly poor performance on domain and style shifts, including worse-than-random accuracy on some out-of-domain tasks and on some non-native English speaker data.

Ghostbuster achieves 99.0 F1 when evaluated across domains, which is 5.9 F1 higher than the best preexisting model, and it also outperforms all previous approaches in generalization across writing domains (+7.5 F1), prompting strategies (+2.1 F1), and language models (+4.4 F1).

The paper demonstrates that while simple perplexity-based approaches have limitations, Ghostbuster's feature-based classifier approach using combinations of features from multiple language models provides superior detection performance and generalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85b60306-44e8-4c9d-bfcb-2b62acc8c1f0",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "2787c897-0cb3-4c23-9cf4-942d8ac13172",
  "sourceToolAssistantUUID": "85b60306-44e8-4c9d-bfcb-2b62acc8c1f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-18T23:25:32.982Z_

Now let me verify the DivEye venue more carefully -- it seems to be TMLR, not ICML main.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2787c897-0cb3-4c23-9cf4-942d8ac13172",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu3w9Ev8hWcaE5BBCEy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6cf6212-ed6f-471e-a644-771d3df2de26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FDr6R658SdFK6yw8CiCxS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1348,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 26866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2131,
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

_source line 40 · 2026-05-18T23:25:34.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015nwmh18YTAttayhSPXCGZo`</summary>

```json
{
  "query": "DivEye \"Diversity Boosts AI-Generated Text Detection\" TMLR 2026 Basani Chen venue published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6cf6212-ed6f-471e-a644-771d3df2de26",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu3w9Ev8hWcaE5BBCEy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88001684-3f67-49ca-8e60-f6b8363535a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FDr6R658SdFK6yw8CiCxS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1348,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 26866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2131,
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

_source line 41 · 2026-05-18T23:25:34.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GzX2cc31qbdafRMzksgLjX`</summary>

```json
{
  "query": "\"Detecting Machine-Generated Texts\" ICLR 2024 maximum mean discrepancy authors Liang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88001684-3f67-49ca-8e60-f6b8363535a4",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu3w9Ev8hWcaE5BBCEy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36a4105b-d568-479e-a2cf-2f1e066f2c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018FDr6R658SdFK6yw8CiCxS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1348,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 26866,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1348,
          "output_tokens": 170,
          "cache_read_input_tokens": 26866,
          "cache_creation_input_tokens": 2131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2131,
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

_source line 42 · 2026-05-18T23:25:40.469Z_

<details><summary>↩ Tool result · `toolu_015nwmh18YTAttayhSPXCGZo`</summary>

```text
Web search results for query: "DivEye "Diversity Boosts AI-Generated Text Detection" TMLR 2026 Basani Chen venue published"

Links: [{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf?id=WscAU9It1l"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"},{"title":"DIVERSITY BOOSTS AI-GENERATED TEXT DETECTION","url":"https://openreview.net/pdf?id=DNgsOhGZBI"},{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"}]

Based on the search results, here's what I found about the DivEye paper:

The paper "Diversity Boosts AI-Generated Text Detection" was authored by Advik Raj Basani and Pin-Yu Chen. 

Regarding the venue, the search results show some nuance: One version indicates it was a withdrawn submission to ICLR 2026, while another citation suggests it was accepted to a workshop called "Data in Generalist Models - The Bad, the Ugly, and the Greats" in 2025. However, I did not find confirmation of publication in TMLR 2026 specifically in these search results.

DivEye captures the signal of richer variability in lexical and structural unpredictability in human-authored text compared to LLM outputs through a set of interpretable statistical features. The method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive performance with fine-tuned baselines, is robust to paraphrasing and adversarial attacks, and generalizes well across domains and models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88001684-3f67-49ca-8e60-f6b8363535a4",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "37e3590d-06b0-44e8-9101-b0f3e9b36e1f",
  "sourceToolAssistantUUID": "88001684-3f67-49ca-8e60-f6b8363535a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T23:25:41.145Z_

<details><summary>↩ Tool result · `toolu_01GzX2cc31qbdafRMzksgLjX`</summary>

```text
Web search results for query: ""Detecting Machine-Generated Texts" ICLR 2024 maximum mean discrepancy authors Liang"

Links: [{"title":"[Quick Review] Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://liner.com/review/detecting-machinegenerated-texts-by-multipopulation-aware-optimization-for-maximum-mean"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy | OpenReview","url":"https://openreview.net/forum?id=3fEKavFsnv"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240216041Z/abstract"},{"title":"Under review as a conference paper at ICLR 2024 DETECTING MACHINE-GENERATED","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/e537e071277a2e5fefaa78f87500c7b4-Supplementary-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2024 DETECTING MACHINE-GENERATED TEXTS","url":"https://openreview.net/pdf?id=3fEKavFsnv"},{"title":"GitHub - ZSHsh98/MMD-MP: This is the source code for Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy (ICLR2024).","url":"https://github.com/ZSHsh98/MMD-MP"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization   for Maximum Mean Discrepancy","url":"https://arxiv.org/pdf/2402.16041"},{"title":"ICLR Poster Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://iclr.cc/virtual/2024/poster/19498"},{"title":"[2402.16041] Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://ar5iv.labs.arxiv.org/html/2402.16041"}]

Based on the search results, I found the paper you're looking for. Here are the key details:

## Paper Overview

The paper "Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy" was published at ICLR 2024.

## Authors

The authors are Shuhai Zhang, Yiliao Song, Jiahao Yang, Yuanqing Li, Bo Han, and Mingkui Tan.

## Main Contribution

The paper proposes a novel multi-population aware optimization method for maximum mean discrepancy (MMD-MP) to detect machine-generated texts. 

The challenge is that distinguishing machine-generated texts from human-written texts is difficult because the distributional discrepancy between them is very subtle. The paper seeks to exploit maximum mean discrepancy (MMD) to address this issue, but directly training a detector with MMD using diverse machine-generated texts incurs significantly increased variance of MMD since machine-generated texts may contain multiple text populations due to various LLMs.

The proposed MMD-MP method can avoid variance increases and thus improve the stability to measure the distributional discrepancy.

Experiments on various LLMs, such as GPT2 and ChatGPT, show superior detection performance of the proposed MMD-MP method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36a4105b-d568-479e-a2cf-2f1e066f2c75",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "292f0425-9f35-42c9-9669-379a9574af03",
  "sourceToolAssistantUUID": "36a4105b-d568-479e-a2cf-2f1e066f2c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-18T23:25:44.743Z_

Now let me verify Kirchenbauer's watermark paper venue (ICML 2023 -- too old) and check for the key ICLR 2025 watermarking paper more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "292f0425-9f35-42c9-9669-379a9574af03",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu4kWJmv5vJpBXnSxFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fb22bb1-780c-4d36-a205-0ff1b371732a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPDLZXaxhEJPMt6txMqdAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3230,
      "cache_read_input_tokens": 28997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3230,
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

_source line 45 · 2026-05-18T23:25:45.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012hDfGPtRVFVK7hUMFThuNg`</summary>

```json
{
  "query": "watermarking LLM ICLR 2025 accepted paper statistical test"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fb22bb1-780c-4d36-a205-0ff1b371732a",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu4kWJmv5vJpBXnSxFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff35981a-7080-4b3f-994d-76d642d52879",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPDLZXaxhEJPMt6txMqdAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3230,
      "cache_read_input_tokens": 28997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3230,
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

_source line 46 · 2026-05-18T23:25:46.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014ziKnN5s5VvPPNJqewXHpe`</summary>

```json
{
  "query": "\"Ghosal\" OR \"Tang\" AI generated text detection survey 2024 ACL EMNLP highly cited"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff35981a-7080-4b3f-994d-76d642d52879",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu4kWJmv5vJpBXnSxFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba6830fb-7a73-462e-b4a8-e17e45140e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPDLZXaxhEJPMt6txMqdAH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3230,
      "cache_read_input_tokens": 28997,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3230
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 28997,
          "cache_creation_input_tokens": 3230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3230,
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

_source line 47 · 2026-05-18T23:25:52.350Z_

<details><summary>↩ Tool result · `toolu_012hDfGPtRVFVK7hUMFThuNg`</summary>

```text
Web search results for query: "watermarking LLM ICLR 2025 accepted paper statistical test"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=E4LAVLXAHW"},{"title":"Published as a conference paper at ICLR 2025 CAN WATERMARKS BE USED","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8fba406323cb3930aeaccc9aa64c83a8-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.03168"},{"title":"GitHub - THU-BPM/Watermarked_LLM_Identification: Code and data for paper \"Can Watermarked LLMs be Identified by Users via Crafted Prompts?\" Accepted by ICLR 2025 (Spotlight) · GitHub","url":"https://github.com/THU-BPM/Watermarked_LLM_Identification"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0f7ee1901fef1da4dae2b88dfd43195-Paper-Conference.pdf"}]

Based on the search results, I found several ICLR 2025 accepted papers related to watermarking LLMs and statistical tests:

## Key Papers Found:

1. **Statistical Testing for Watermark Detection**: One paper introduces a statistical test for detecting watermarks from the Red-Green family, where given black-box textual access to a language model, a client can query the model and run statistical tests to rigorously test for presence of a watermark. This exploits the core property that applying the watermark introduces a context-dependent logit bias, where the model's output distribution is biased in a way that can greatly vary depending on the last few tokens generated.

2. **Watermarked LLM Identification via Crafted Prompts**: Another paper titled "Can Watermarked LLMs be Identified by Users via Crafted Prompts?" was published at ICLR 2025.

3. **Cross-Domain Watermark Detection**: A third paper's method achieves detection accuracy of over 90% in cross-domain detection on challenging model sets containing suspect LLMs with multiple settings. This method involves statistically analyzing the proportion of green list tokens in the target text using a z-test to compute z-scores or p-values.

These papers explore how watermarks on large language models can be detected through statistical testing methods in black-box settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff35981a-7080-4b3f-994d-76d642d52879",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "756a7cbf-74da-4020-ac07-c20fb995f17e",
  "sourceToolAssistantUUID": "ff35981a-7080-4b3f-994d-76d642d52879",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T23:25:55.587Z_

<details><summary>↩ Tool result · `toolu_014ziKnN5s5VvPPNJqewXHpe`</summary>

```text
Web search results for query: ""Ghosal" OR "Tang" AI generated text detection survey 2024 ACL EMNLP highly cited"

Links: [{"title":"(PDF) Detecting AI-Generated Text: Factors Influencing Detectability with Current Methods","url":"https://www.researchgate.net/publication/381666008_Detecting_AI-Generated_Text_Factors_Influencing_Detectability_with_Current_Methods"},{"title":"Distinguishing Human From Machine: A Review of Advances and Challenges in AI-Generated Text Detection | International Journal of Interactive Multimedia and Artificial Intelligence","url":"https://revistas.unir.net/index.php/ijimai/article/view/234"},{"title":"A Practical Examination of AI-Generated Text Detectors for Large Language Models","url":"https://arxiv.org/html/2412.05139v4"},{"title":"Detecting AI-Generated Text: : Factors Influencing ...","url":"https://dl.acm.org/doi/pdf/10.1613/jair.1.16665"},{"title":"[2310.15264] Towards Possibilities & Impossibilities of AI-generated Text Detection: A Survey","url":"https://arxiv.org/abs/2310.15264"},{"title":"Position: On the possibilities of AI-generated text detection","url":"https://dl.acm.org/doi/10.5555/3692070.3692305"},{"title":"The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161"},{"title":"A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f582daa2f2822c0aa1291fe3925f69c25280e37e"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"Towards Possibilities & Impossibilities of AI-generated Text Detection:   A Survey","url":"https://arxiv.org/pdf/2310.15264"}]

Based on the search results, I found information about AI-generated text detection surveys by both Ghosal and Tang:

## Ghosal et al. Survey

Ghosal et al. (2023) published "Towards possibilities & impossibilities of ai-generated text detection: A survey". This work was published in Transactions on Machine Learning Research in 2023. The survey presents an overview of both the possibilities (detection methods) and impossibilities (evasion methods) of AIGT detection.

## Tang et al. Survey

Tang et al. (2024) offer an accessible summary of major insights and challenges in the field of AIGT detection.

## Detection Categories

The detectors primarily fall into three categories: trained detectors, zero-shot detectors, and watermarking techniques.

These surveys appear to be widely cited in the field. The search results show multiple references to both the Ghosal et al. 2023 survey and Tang et al. 2024 work in recent academic publications on AI-generated text detection. However, I did not find specific information about ACL or EMNLP conference venues for these particular surveys in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba6830fb-7a73-462e-b4a8-e17e45140e54",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "586ad653-b37f-487a-9913-d7c8f28e23fc",
  "sourceToolAssistantUUID": "ba6830fb-7a73-462e-b4a8-e17e45140e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-18T23:25:58.463Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RHukq58NjNQpByGDUE6nHw`</summary>

```json
{
  "query": "Tang \"Science of Detecting LLM-Generated Text\" survey 2024 venue citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "586ad653-b37f-487a-9913-d7c8f28e23fc",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu5pGoQm2Chcpjou91A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2a4d69a-c1af-4a55-a0c7-fee38457fbca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHy19h6vJ6taSBN419MEzZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1736,
      "cache_read_input_tokens": 32227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1736,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 50 · 2026-05-18T23:25:59.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fxe3kpoWsJdAsWRrZCxrvv`</summary>

```json
{
  "query": "Kirchenbauer watermark large language models 2023 follow-up 2024 ICLR \"On the Reliability\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2a4d69a-c1af-4a55-a0c7-fee38457fbca",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu5pGoQm2Chcpjou91A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86431239-f1b3-482f-862d-52e2aa398ffe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHy19h6vJ6taSBN419MEzZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1736,
      "cache_read_input_tokens": 32227,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1736
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 32227,
          "cache_creation_input_tokens": 1736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1736,
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

_source line 51 · 2026-05-18T23:26:04.561Z_

<details><summary>↩ Tool result · `toolu_01RHukq58NjNQpByGDUE6nHw`</summary>

```text
Web search results for query: "Tang "Science of Detecting LLM-Generated Text" survey 2024 venue citations"

Links: [{"title":"The Science of Detecting LLM-Generated Texts: While many detection methods have been proposed, understanding the challenges is far more daunting. | Request PDF","url":"https://www.researchgate.net/publication/378817918_The_Science_of_Detecting_LLM-Generated_Texts_While_many_detection_methods_have_been_proposed_understanding_the_challenges_is_far_more_daunting"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future   Directions","url":"https://arxiv.org/pdf/2310.14724"},{"title":"The Science of Detecting LLM-Generated Text | Communications of the ACM","url":"https://dl.acm.org/doi/abs/10.1145/3624725"},{"title":"Distinguishing Human From Machine: A Review of Advances and Challenges in AI-Generated Text Detection | International Journal of Interactive Multimedia and Artificial Intelligence","url":"https://www.ijimai.org/index.php/ijimai/article/view/234"},{"title":"A Survey on Detection of LLMs-Generated Content","url":"https://aclanthology.org/2024.findings-emnlp.572.pdf"},{"title":"[2303.07205] The Science of Detecting LLM-Generated Texts","url":"https://arxiv.org/abs/2303.07205"},{"title":"The Science of Detecting LLM-Generated Texts","url":"https://openreview.net/pdf?id=XLuFNdEsjV2"},{"title":"(PDF) The Science of Detecting LLM-Generated Texts","url":"https://www.researchgate.net/publication/368684822_The_Science_of_Detecting_LLM-Generated_Texts"},{"title":"The Science of Detecting LLM-Generated Text – Communications of the ACM","url":"https://cacm.acm.org/research/the-science-of-detecting-llm-generated-text/"},{"title":"An overview of the LLM-generated text detection. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/An-overview-of-the-LLM-generated-text-detection_fig1_368684822"}]

Based on the search results, here's what I found about the Tang survey on detecting LLM-generated text:

## Publication Venue

The survey "The Science of Detecting LLM-Generated Text" by Tang, Chuang, and Hu was published in Communications of the ACM, Volume 67, Issue 4, Pages 50-59 on March 7, 2024.

## Citation Information

The full citation is: R. Tang, Y.-N. Chuang, X. Hu, "The science of detecting llm-generated text," Communications of the ACM, vol. 67, p. 50–59, mar 2024, doi: 10.1145/3624725.

The survey provides a precise categorization and in-depth examination of existing approaches to help the research community comprehend the strengths and limitations of each method for detecting LLM-generated text.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2a4d69a-c1af-4a55-a0c7-fee38457fbca",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "12119174-dcc6-4f1b-947c-fb3d7daacefb",
  "sourceToolAssistantUUID": "a2a4d69a-c1af-4a55-a0c7-fee38457fbca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T23:26:05.371Z_

<details><summary>↩ Tool result · `toolu_01Fxe3kpoWsJdAsWRrZCxrvv`</summary>

```text
Web search results for query: "Kirchenbauer watermark large language models 2023 follow-up 2024 ICLR "On the Reliability" authors"

Links: [{"title":"[2301.10226] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226"},{"title":"GitHub - jwkirchenbauer/lm-watermarking · GitHub","url":"https://github.com/jwkirchenbauer/lm-watermarking"},{"title":"A Watermark for Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10522346-watermark-large-language-models"},{"title":"A Watermark for Large Language Models","url":"https://proceedings.mlr.press/v202/kirchenbauer23a.html"},{"title":"[2306.04634] On the Reliability of Watermarks for Large Language Models","url":"https://arxiv.org/abs/2306.04634"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=gMLQwKDY3N"},{"title":"dblp: A Watermark for Large Language Models.","url":"https://dblp.org/rec/conf/icml/KirchenbauerGWK23.html"},{"title":"Published at ICLR 2024 Workshop on Secure and Trustworthy Large Language Models","url":"https://openreview.net/pdf?id=P2FFPRxr3Q"},{"title":"Publicly-Detectable Watermarking for Language Models","url":"https://eprint.iacr.org/2023/1661.pdf"}]

Based on the search results, I found the information you're looking for:

"On the Reliability of Watermarks for Large Language Models" is authored by John Kirchenbauer, Jonas Geiping, Yuxin Wen, Manli Shu, Khalid Saifullah, Kezhi Kong, Kasun Fernando, Aniruddha Saha, Micah Goldblum, and Tom Goldstein.

The paper was accepted for publication and was presented at ICLR 2024 in Vienna, Austria. This work documents "a deep dive into the robustness properties of more advanced watermarks" and served as a 2023-2024 follow-up to the original 2023 watermarking work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86431239-f1b3-482f-862d-52e2aa398ffe",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "5d2ff1dc-c9c3-4ace-9ac1-da63afba4ade",
  "sourceToolAssistantUUID": "86431239-f1b3-482f-862d-52e2aa398ffe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-18T23:26:11.042Z_

Now let me also check for the survey that appeared at EMNLP 2024 Findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d2ff1dc-c9c3-4ace-9ac1-da63afba4ade",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu6hr7pb7ypE6BgXCv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bb0b76d-14f7-4afa-8768-5792452198c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7E5VhbZSYxmVqpcAv99eu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 33963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1603,
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

_source line 54 · 2026-05-18T23:26:11.576Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QdpvMjdauFAd5opZq6vLoP`</summary>

```json
{
  "query": "\"A Survey on Detection of LLMs-Generated Content\" EMNLP 2024 findings authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bb0b76d-14f7-4afa-8768-5792452198c1",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu6hr7pb7ypE6BgXCv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5a411d7-9238-4ce8-bba7-af68ad7b0af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7E5VhbZSYxmVqpcAv99eu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 33963,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 33963,
          "cache_creation_input_tokens": 1603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1603,
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

_source line 55 · 2026-05-18T23:26:17.857Z_

<details><summary>↩ Tool result · `toolu_01QdpvMjdauFAd5opZq6vLoP`</summary>

```text
Web search results for query: ""A Survey on Detection of LLMs-Generated Content" EMNLP 2024 findings authors"

Links: [{"title":"A Survey on Detection of LLMs-Generated Content - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.572/"},{"title":"A Survey on Detection of LLMs-Generated Content","url":"https://arxiv.org/pdf/2310.15654"},{"title":"A Survey on Detection of LLMs-Generated Content","url":"https://aclanthology.org/2024.findings-emnlp.572.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?doi=10.18653/v1/2024.findings-emnlp.572"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future   Directions","url":"https://arxiv.org/pdf/2310.14724"},{"title":"[2310.15654] A Survey on Detection of LLMs-Generated Content","url":"https://arxiv.org/abs/2310.15654"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"[PDF] A Survey on Detection of LLMs-Generated Content | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-Detection-of-LLMs-Generated-Content-Yang-Pan/60bd26bdb23ba353e5d79f161542dd074bc8391c"}]

Based on the search results, here's the information about "A Survey on Detection of LLMs-Generated Content" published at EMNLP 2024:

## Authors

The authors are Xianjun Yang, Liangming Pan, Xuandong Zhao, Haifeng Chen, Linda Ruth Petzold, William Yang Wang, and Wei Cheng.

## Publication Details

The paper was published in the Findings of the Association for Computational Linguistics: EMNLP 2024, pages 9786–9805, Miami, Florida, USA.

## Overview and Findings

The burgeoning capabilities of advanced large language models (LLMs) such as ChatGPT have led to an increase in synthetic content generation with implications across a variety of sectors, including media, cybersecurity, public discourse, and education.

The survey aims to provide a detailed overview of existing detection strategies and benchmarks, scrutinizing their differences and identifying key challenges and prospects in the field. The authors maintain a website to consistently update the latest research as a guiding reference for researchers and practitioners.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5a411d7-9238-4ce8-bba7-af68ad7b0af0",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "ad7ad0a40a8db59a5",
  "type": "user",
  "uuid": "827eaa2e-888b-4dea-8050-6f5229e7f10f",
  "sourceToolAssistantUUID": "a5a411d7-9238-4ce8-bba7-af68ad7b0af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-18T23:26:49.223Z_

I now have enough information to compile the results. Here is the compiled list of recommended papers:

---

## Recommended Papers for Related Work

### 1. BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens

- **Authors:** Guo et al.
- **Venue:** NeurIPS 2024
- **Relation to your work:** BiScope uses a bi-directional cross-entropy measure on output logits (forward loss and backward memorization of preceding tokens) as a statistical signal for detection, which is conceptually close to your use of perplexity-based and surprisal-based statistical features for depth estimation.
- **Cite:** Yes
- **Where:** Related Work, under zero-shot / statistical detection methods
- **Reason:** It represents the latest NeurIPS-level zero-shot statistical detection method and directly shares the "token-level statistical feature" paradigm with your approach. Your work extends beyond binary detection to ordinal depth estimation, making this a natural contrast point.

### 2. MAGE: Machine-generated Text Detection in the Wild

- **Authors:** Li et al.
- **Venue:** ACL 2024
- **Relation to your work:** MAGE provides a comprehensive benchmark across 27 LLMs with increasing detection difficulty tiers, and evaluates robustness under domain shift and paraphrasing attacks. Your recursive depth estimation faces analogous generalization challenges across models and domains.
- **Cite:** Yes
- **Where:** Related Work, under benchmarks/evaluation or trained detectors
- **Reason:** As the largest-scale detection benchmark at a top venue, citing it positions your work within the broader evaluation landscape. It also demonstrates that detection difficulty increases with distributional overlap, which motivates why depth estimation (a finer-grained task) is hard.

### 3. Ghostbuster: Detecting Text Ghostwritten by Large Language Models

- **Authors:** Verma et al.
- **Venue:** NAACL 2024
- **Relation to your work:** Ghostbuster uses a structured feature search over combinations of weaker LM outputs plus a trained classifier, which is methodologically analogous to your approach of extracting statistical features (perplexity percentiles, entropy, surprisal variance) and training a Random Forest classifier.
- **Cite:** Yes
- **Where:** Related Work, under feature-based / trained detection methods
- **Reason:** The feature-engineering + classifier pipeline is the closest methodological parallel to your Random Forest approach. Ghostbuster shows that crafted statistical features can outperform end-to-end approaches, which supports the rationale of your method.

### 4. Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy (MMD-MP)

- **Authors:** Zhang et al.
- **Venue:** ICLR 2024
- **Relation to your work:** MMD-MP addresses the challenge that machine-generated texts from different LLMs form multiple sub-populations with subtle distributional discrepancies from human text. Your recursive depth estimation similarly faces a multi-population challenge where each depth level has its own distributional characteristics.
- **Cite:** Maybe
- **Where:** Related Work, under statistical detection methods
- **Reason:** The multi-population distributional analysis connects to your setting where texts at different regeneration depths form distinct but overlapping distributions. Less directly relevant than BiScope or Ghostbuster since it focuses on binary detection with a kernel-based approach rather than interpretable features.

### 5. A Survey on Detection of LLMs-Generated Content

- **Authors:** Yang et al.
- **Venue:** EMNLP 2024 Findings
- **Relation to your work:** Comprehensive survey covering watermarking, statistical, and classifier-based detection methods. Provides the taxonomic context for positioning your recursive depth estimation as a novel detection dimension beyond binary human/machine classification.
- **Cite:** Yes
- **Where:** Related Work, opening paragraph or as a general reference when introducing the AI text detection landscape
- **Reason:** A peer-reviewed survey at a top NLP venue gives readers a single entry point to the broader field. Citing it lets you keep your own Related Work section focused on the most directly relevant methods without having to individually cite every detection approach.

---

## Summary Table

| Paper | Venue | Cite? | Where |
|---|---|---|---|
| BiScope (Guo et al.) | NeurIPS 2024 | Yes | Statistical detection methods |
| MAGE (Li et al.) | ACL 2024 | Yes | Benchmarks / evaluation |
| Ghostbuster (Verma et al.) | NAACL 2024 | Yes | Feature-based trained detectors |
| MMD-MP (Zhang et al.) | ICLR 2024 | Maybe | Statistical detection methods |
| Detection Survey (Yang et al.) | EMNLP 2024 Findings | Yes | Opening of Related Work |

The three strongest recommendations are **BiScope**, **Ghostbuster**, and **Yang et al. survey**. BiScope is the closest in spirit (statistical token-level features, zero-shot), Ghostbuster is the closest in method (feature engineering + classifier), and the Yang et al. survey anchors your Related Work in the broader field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "827eaa2e-888b-4dea-8050-6f5229e7f10f",
  "isSidechain": true,
  "agentId": "ad7ad0a40a8db59a5",
  "requestId": "req_011CbAu7aab7ou1A9jEQLGLQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf7cc9d8-1954-4d14-bbbc-658ff21c197a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRjasW76MZyt1HA7CsYXbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 35566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 813,
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
