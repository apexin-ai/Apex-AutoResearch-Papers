# Research conversation: You are searching for recent (2024-2025) academic papers on Ordinal Classification / Ordinal Regression in NLP or deep l

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2a86d0fd624e91a0.jsonl`
- **Structured JSON:** [`600bf26a6bba9e685d68.json`](../../sessions/60/600bf26a6bba9e685d68.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-18T23:24:50.852Z_

You are searching for recent (2024-2025) academic papers on Ordinal Classification / Ordinal Regression in NLP or deep learning. This is for a related work section of a paper that uses ordinal classification to estimate "recursive generation depth" — classifying text into ordered depth classes d0, d1, d2, d3 based on how many times it has been through LLM regeneration cycles. The paper uses a Random Forest with 19 statistical features and also explores CORAL-style ordinal loss.

Please perform the following web searches and compile results:

1. Search: "ordinal classification" NLP 2024 2025 ACL EMNLP
2. Search: "ordinal regression" deep learning text 2024 2025
3. Search: "CORAL" ordinal loss deep learning 2024
4. Search: "ordered classification" natural language processing 2024

For each paper found, provide:
- Full title
- Authors (first author et al. is fine)
- Venue (ICML/NeurIPS/ICLR/ACL/EMNLP/NAACL/COLM/AAAI 2024-2025, or high-citation arXiv)
- One sentence on how it relates to ordinal depth classification
- Whether it should be cited: Yes/No/Maybe
- Where it should be cited in the paper
- Brief reason

Only report papers from top venues or highly-cited arXiv preprints. If this area has very few NLP-specific papers, also include relevant ML methodology papers on ordinal classification that could justify the ordinal approach used in the paper. Aim for 2-4 papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "045c789d-2ed7-484e-8dfd-e53c8e9db367",
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

_source line 2 · 2026-05-18T23:24:50.854Z_

```json
{
  "parentUuid": "045c789d-2ed7-484e-8dfd-e53c8e9db367",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
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
  "uuid": "13cc3e6a-706c-424b-9d6a-17a2c0e452be",
  "timestamp": "2026-05-18T23:24:50.854Z",
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

_source line 3 · 2026-05-18T23:24:53.044Z_



I'll perform all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13cc3e6a-706c-424b-9d6a-17a2c0e452be",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu13RBg2Z6vDS33iwoE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "889c5c1e-afa0-4c38-98d3-3a2dbf394b18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnryAVwUs2J19sMzB6h3w2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7688,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7688,
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

_source line 4 · 2026-05-18T23:24:53.671Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RFy95d87yX2R4cLQMzhHiB`</summary>

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
  "parentUuid": "889c5c1e-afa0-4c38-98d3-3a2dbf394b18",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu13RBg2Z6vDS33iwoE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f524161-f6cd-4256-9147-8446f4e08cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnryAVwUs2J19sMzB6h3w2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7688,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7688,
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

### Tool result

_source line 5 · 2026-05-18T23:24:53.676Z_

<details><summary>↩ Tool result · `toolu_01RFy95d87yX2R4cLQMzhHiB`</summary>

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
  "parentUuid": "0f524161-f6cd-4256-9147-8446f4e08cfe",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "cb5ed98b-dd26-4184-9920-6dd9eeace304",
  "sourceToolAssistantUUID": "0f524161-f6cd-4256-9147-8446f4e08cfe",
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

_source line 6 · 2026-05-18T23:24:56.008Z_



Running all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb5ed98b-dd26-4184-9920-6dd9eeace304",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu1FrYXgQgqWadWr8dM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54696b4a-8e24-47d9-b889-f798363c7e45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Thv27kjBrfwzyHmiNNZLVY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
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

_source line 7 · 2026-05-18T23:24:56.295Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NgTbz3bW3EwD4HBTmsu77x`</summary>

```json
{
  "query": "\"ordinal classification\" NLP 2024 2025 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54696b4a-8e24-47d9-b889-f798363c7e45",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu1FrYXgQgqWadWr8dM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a54ec4b-0680-4bb7-942c-b0a582fee513",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Thv27kjBrfwzyHmiNNZLVY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15939,
      "output_tokens": 81,
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
          "output_tokens": 81,
          "cache_read_input_tokens": 15939,
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

_source line 8 · 2026-05-18T23:25:00.838Z_

<details><summary>↩ Tool result · `toolu_01NgTbz3bW3EwD4HBTmsu77x`</summary>

```text
Web search results for query: ""ordinal classification" NLP 2024 2025 ACL EMNLP"

Links: [{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2024/"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-tutorials.pdf"},{"title":"King's College London NLP","url":"https://kclnlp.github.io/publications.html"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Joint Call for Tutorial Proposals - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/tutorials/"}]

The search results provide general information about EMNLP 2024 and 2025 conferences and ACL 2025, but they don't contain specific information about "ordinal classification" research papers or work presented at these venues. The results show conference overviews, tutorials, and some example papers, but nothing specifically focused on ordinal classification in NLP.

To get more relevant results, would you like me to search with a different query, such as:
- "ordinal regression NLP" to find papers on related topics
- Specific venues or authors you're interested in
- A narrower timeframe or specific keywords


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a54ec4b-0680-4bb7-942c-b0a582fee513",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "fbf3498a-ee2d-4c3f-a2a4-cc743f201d8c",
  "sourceToolAssistantUUID": "5a54ec4b-0680-4bb7-942c-b0a582fee513",
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

_source line 9 · 2026-05-18T23:25:03.485Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VQkKLRyiP58DcX6Sfe3mop`</summary>

```json
{
  "query": "\"ordinal regression\" deep learning text classification 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbf3498a-ee2d-4c3f-a2a4-cc743f201d8c",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu1n7DCc2F55paF96ax",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eff82317-2952-48aa-a30e-031693b5356b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vfqUH7DAmAw87vWiyp1c6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 548,
      "cache_read_input_tokens": 17389,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 17389,
          "cache_creation_input_tokens": 548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 548,
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

_source line 10 · 2026-05-18T23:25:10.711Z_

<details><summary>↩ Tool result · `toolu_01VQkKLRyiP58DcX6Sfe3mop`</summary>

```text
Web search results for query: ""ordinal regression" deep learning text classification 2024 2025"

Links: [{"title":"ordinal-classification · GitHub Topics · GitHub","url":"https://github.com/topics/ordinal-classification"},{"title":"Deep and interpretable regression models for ordinal outcomes - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S003132032100443X"},{"title":"dlordinal: a Python package for deep ordinal classification","url":"https://arxiv.org/html/2407.17163v2"},{"title":"A Deep Learning Ordinal Classifier","url":"https://thesai.org/Downloads/Volume16No3/Paper_30-A_Deep_Learning_Ordinal_Classifier.pdf"},{"title":"dlordinal: A Python package for deep ordinal classification - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231224020769"},{"title":"Continuously Generalized Ordinal Regression for Linear and Deep Models","url":"https://arxiv.org/pdf/2202.07005"},{"title":"Deep and interpretable regression models for ordinal outcomes","url":"https://arxiv.org/pdf/2010.08376"}]

I've found several relevant results for ordinal regression in deep learning. Here's what the search reveals:

## Key Findings:

**Recent Developments (2024-2025):**

dlordinal is a new Python library that unifies many recent deep ordinal classification methodologies, published in March 2025. The library includes ordinal dropout methodologies, output layers, soft labeling, losses and wrappers for deep learning.

While considerable research has been done on ordinal classification of tabular data, very little has concentrated on deep learning for ordinal classification of tabular data.

**Methodological Advances:**

Ordinal regression is a classification task where classes have an order and prediction error increases the further the predicted class is from the true class. Recent methods like continuously generalized ordinal logistic significantly outperform standard ordinal logistic models and extend to deep learning with competitive performance across various datasets.

Ordinal neural network transformation models (ONTRAMs) unite deep learning with classical ordinal regression approaches by decomposing the transformation function into terms for different data types using jointly trained neural networks.

**Text Classification Applications:**

While the search results primarily focus on image and tabular data applications, there is documented work on NLP, natural language processing, and text classification using ordinal classification methods with PyTorch from COLING 2022.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eff82317-2952-48aa-a30e-031693b5356b",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "dfa77d5a-96a5-43a5-8a18-b97dbad04968",
  "sourceToolAssistantUUID": "eff82317-2952-48aa-a30e-031693b5356b",
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

_source line 11 · 2026-05-18T23:25:13.865Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0175k7P9GMkxjLX2ANMC7c9y`</summary>

```json
{
  "query": "CORAL ordinal loss neural network 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfa77d5a-96a5-43a5-8a18-b97dbad04968",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu2WMTLrZzWC47aRSn8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84e85ad5-1e6b-4f48-ac22-6e78a963d88d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQsZJoZHiqi4skECbgSpBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 17937,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 17937,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 694,
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

_source line 12 · 2026-05-18T23:25:22.373Z_

<details><summary>↩ Tool result · `toolu_0175k7P9GMkxjLX2ANMC7c9y`</summary>

```text
Web search results for query: "CORAL ordinal loss neural network 2024 2025 paper"

Links: [{"title":"Ordinal Regression Research Based on Dual Loss Function—An Example on Lumbar Vertebra Classification in CT Images - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12691345/"},{"title":"Rank consistent ordinal regression for neural networks with application to age estimation | Pattern Recognition Letters","url":"https://dl.acm.org/doi/10.1016/j.patrec.2020.11.008"},{"title":"GitHub - Raschka-research-group/coral-cnn: Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation · GitHub","url":"https://github.com/Raschka-research-group/coral-cnn"},{"title":"GitHub - Raschka-research-group/coral-pytorch: CORAL and CORN implementations for ordinal regression with deep neural networks. · GitHub","url":"https://github.com/Raschka-research-group/coral-pytorch"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211108851S/abstract"},{"title":"coral-ordinal · PyPI","url":"https://pypi.org/project/coral-ordinal/"},{"title":"CORAL CNN model for image data (MNIST dataset) - coral_pytorch","url":"https://raschka-research-group.github.io/coral-pytorch/tutorials/pure_pytorch/CORAL_mnist/"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal ...","url":"https://arxiv.org/pdf/2111.08851"}]

Based on the search results, here's what I found about CORAL ordinal loss for neural networks:

## Overview

CORAL (COnsistent RAnk Logits) is a framework with strong theoretical guarantees for rank-monotonicity and consistent confidence scores. CORAL is a method for ordinal regression with deep neural networks that addresses the rank inconsistency issue of other ordinal regression frameworks.

## How CORAL Works

Cao et al. proposed the CORAL framework, which aims to avoid increasing the complexity of training by applying weight sharing in the penultimate layer of the neural network. The CORAL method only requires replacing the last (output) layer, which is typically a fully-connected layer, by the CORAL layer.

## Original Paper and Development

The original CORAL paper titled "Rank consistent ordinal regression for neural networks with application to age estimation" was published in Pattern Recognition Letters, volume 140, pages 325-331, in 2020 by Wenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.

## Recent Applications (2024-2025)

The search results show recent applications of CORAL:

- A 2025 study proposed and evaluated a dual loss framework—Ordinal Residual Dual Loss—for lumbar vertebra classification on CT images using ordinal regression principles related to CORAL.

- In 2024, researchers developed CORAL-CVDs, a Consistent Ordinal Regression Model for Cardiovascular Diseases Grading.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84e85ad5-1e6b-4f48-ac22-6e78a963d88d",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "7ce32ce7-0ce0-402a-80c8-dc718ccfe5a6",
  "sourceToolAssistantUUID": "84e85ad5-1e6b-4f48-ac22-6e78a963d88d",
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

_source line 13 · 2026-05-18T23:25:24.868Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MaHemhMyaiQFvBE6txMi1H`</summary>

```json
{
  "query": "\"ordered classification\" \"natural language processing\" 2024 ordinal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ce32ce7-0ce0-402a-80c8-dc718ccfe5a6",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu3NKHbpyBAt6Ahf4sR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bed041b0-4e72-4263-a61c-60c5c44f15cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWaJGdPC4W1NfE7JqExYjP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 18631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 861,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 14 · 2026-05-18T23:25:32.732Z_

<details><summary>↩ Tool result · `toolu_01MaHemhMyaiQFvBE6txMi1H`</summary>

```text
Web search results for query: ""ordered classification" "natural language processing" 2024 ordinal"

Links: [{"title":"Exploring Ordinal Classification for Spoken Language Assessment | Request PDF","url":"https://www.researchgate.net/publication/395789601_Exploring_Ordinal_Classification_for_Spoken_Language_Assessment"},{"title":"ordinal-classification · GitHub Topics · GitHub","url":"https://github.com/topics/ordinal-classification"},{"title":"A Survey on Ordinal Regression: Applications, Advances, and Prospects","url":"https://arxiv.org/html/2503.00952v1"},{"title":"Ordinal Classification with Distance Regularization for Robust Brain Age Prediction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11008505/"},{"title":"XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification","url":"https://www.researchgate.net/publication/402594018_XL-DURel_Finetuning_Sentence_Transformers_for_Ordinal_Word-in-Context_Classification"},{"title":"Active learning for ordinal classification based on expected cost minimization | Scientific Reports","url":"https://www.nature.com/articles/s41598-022-26844-1"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of   Explicit and Implicit Techniques","url":"https://arxiv.org/pdf/2405.11775"},{"title":"Classification of Ordinal Data","url":"https://arxiv.org/pdf/cs/0605123"},{"title":"Ordinality in Discrete-level Question Difficulty Estimation: Introducing Balanced DRPS and OrderedLogitNN","url":"https://arxiv.org/pdf/2507.00736"}]

Based on the web search results, here's what I found about ordered classification in natural language processing from 2024:

## Overview

Ordinal regression, also known as ordinal classification, aims to solve classification problems in which categories are not independent but instead follow a natural order. Ordinal classification is a key task in natural language processing with many applications that require ordering or ranking in the output such as Sentiment Analysis, Rating Prediction, and Age Group Classification.

## Key Distinctions

Unlike normal classification, ordinal regression takes into account the natural ordering of categories in the response variable, which allows for more nuanced and accurate modeling when the order of categories carries meaningful information, as well as training a universal model to learn ordered information from different ordinal regression tasks jointly.

## 2024 Research Developments

Many real-world prediction problems have ordinal response variables, and conventional classification losses such as multi-category cross-entropy ignore this ordering information. Ordinal regression methods for deep neural networks address this.

Recent 2024 work includes the use of neural models for classifying English written exams into CEFR competence levels. Additionally, with the advent of Pretrained Language Models, it became possible to tackle ordinality through the implicit semantics of the labels as well, with comprehensive theoretical and empirical examination of both explicit and implicit approaches.

The field continues to explore specialized loss functions and neural architectures designed specifically to preserve and exploit the ordinal nature of classification tasks in NLP applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bed041b0-4e72-4263-a61c-60c5c44f15cf",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "d062663e-14e6-45cd-8ba4-65488384efef",
  "sourceToolAssistantUUID": "bed041b0-4e72-4263-a61c-60c5c44f15cf",
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

_source line 15 · 2026-05-18T23:25:35.356Z_

Good, I found several promising leads. Let me do targeted follow-up searches for the most relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d062663e-14e6-45cd-8ba4-65488384efef",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu48VcVwyZhZQYjupqp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e80d819-f9f8-416d-871e-1a6e00200c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjCJ9HZKkQoexiKrzFKchb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 19492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 857,
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

_source line 16 · 2026-05-18T23:25:35.815Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FFrCbWXoFAwXcT7no3kUC4`</summary>

```json
{
  "query": "arxiv \"Exploring Ordinality in Text Classification\" 2024 explicit implicit techniques"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e80d819-f9f8-416d-871e-1a6e00200c66",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu48VcVwyZhZQYjupqp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b7cc658-4ecc-4c8d-8a33-a10aa87891d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjCJ9HZKkQoexiKrzFKchb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 19492,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 857
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 19492,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 857,
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

_source line 17 · 2026-05-18T23:25:45.909Z_

<details><summary>↩ Tool result · `toolu_01FFrCbWXoFAwXcT7no3kUC4`</summary>

```text
Web search results for query: "arxiv "Exploring Ordinality in Text Classification" 2024 explicit implicit techniques"

Links: [{"title":"[2405.11775] Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques","url":"https://arxiv.org/abs/2405.11775"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.320/"},{"title":"Computation and Language May 2024","url":"https://arxiv.org/list/cs.CL/2024-05?skip=600&show=100"},{"title":"Generative or Discriminative? Revisiting Text Classification in the Era of Transformers","url":"https://arxiv.org/html/2506.12181v1"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques","url":"https://arxiv.org/html/2405.11775v1"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of   Explicit and Implicit Techniques","url":"https://arxiv.org/pdf/2405.11775"}]

I found the paper you were searching for! Here are the results:

## Paper Found

The paper "Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques" was submitted on May 20, 2024, and addresses Ordinal Classification (OC) challenges in Natural Language Processing with applications in sentiment analysis, rating prediction, and more.

## Key Approaches

The paper examines two main approaches to ordinal classification:

1. **Explicit Techniques**: Previous approaches to tackle OC have primarily focused on modifying existing or creating novel loss functions that explicitly account for the ordinal nature of labels.

2. **Implicit Techniques**: With the advent of Pretrained Language Models (PLMs), it became possible to tackle ordinality through the implicit semantics of the labels as well.

## Paper Details

The paper is authored by Siva Rajesh Kasa, Aniket Goel, Karan Gupta, Sumegh Roychowdhury, Pattisapu Priyatam, Anish Bhanushali, and Prasanna Srinivasa Murthy, and it appears in the Findings of the Association for Computational Linguistics: ACL 2024 in Bangkok, Thailand.

The paper is available on arXiv at: https://arxiv.org/abs/2405.11775


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b7cc658-4ecc-4c8d-8a33-a10aa87891d5",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "cc3a051c-52a1-483e-9676-875e6e312088",
  "sourceToolAssistantUUID": "4b7cc658-4ecc-4c8d-8a33-a10aa87891d5",
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

_source line 18 · 2026-05-18T23:25:48.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ma43B3dMLib14jMxi6qiqE`</summary>

```json
{
  "query": "arxiv \"A Survey on Ordinal Regression\" 2025 applications advances prospects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc3a051c-52a1-483e-9676-875e6e312088",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu56sQr28JLVAADosC4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13bcfb89-45fd-459c-bfa7-515fdb76a131",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZnaMLb5vokYqiddSm3aVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 20349,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 20349,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 741,
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

_source line 19 · 2026-05-18T23:26:08.615Z_

<details><summary>↩ Tool result · `toolu_01Ma43B3dMLib14jMxi6qiqE`</summary>

```text
Web search results for query: "arxiv "A Survey on Ordinal Regression" 2025 applications advances prospects"

Links: [{"title":"[2503.00952] A Survey on Ordinal Regression: Applications, Advances and Prospects","url":"https://arxiv.org/abs/2503.00952"},{"title":"A Survey on Ordinal Regression: Applications, Advances, and Prospects","url":"https://arxiv.org/html/2503.00952v1"},{"title":"[Literature Review] A Survey on Ordinal Regression: Applications, Advances and Prospects","url":"https://www.themoonlight.io/en/review/a-survey-on-ordinal-regression-applications-advances-and-prospects"},{"title":"A Survey on Ordinal Regression: Applications, Advances and Prospects | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/survey-ordinal-regression-applications-advances-prospects"},{"title":"A Survey on Ordinal Regression: Applications, Advances ...","url":"https://www.connectedpapers.com/main/d732caeb0be5dc1b699482dd1549e95b20aef585/A-Survey-on-Ordinal-Regression:-Applications,-Advances-and-Prospects/graph"}]

I found the survey paper you were looking for! Here are the key findings:

## Overview

The survey presents a comprehensive examination of advances and applications of ordinal regression, introducing a systematic taxonomy that classifies techniques and applications into three categories: Continuous Space Discretization, Distribution Ordering Learning, and Ambiguous Instance.

## Applications

Ordinal regression is crucial for applications in various areas like facial age estimation, image aesthetics assessment, and even cancer staging, due to its capability to utilize ordered information effectively.

## Key Advances

The three well-defined categories of approaches are Continuous Space Discretization (which focuses on transforming ordinal regression into a deep classification task via continuous space discretization), and Distribution Ordering Learning, which addresses the main specificity of ordinal regression that differs from simple classification tasks: Labels are in order.

## Benefits and Prospects

Ordinal regression enhances model interpretation by considering category order, aiding the understanding of data trends and causal relationships. Despite significant recent progress, challenges remain, and further investigation of ordinal regression techniques and applications is essential to guide future research.

The paper was submitted to arXiv on March 2, 2025, and provides a comprehensive guide to current methodologies and future research directions in this field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13bcfb89-45fd-459c-bfa7-515fdb76a131",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "4a99cd8a-1a00-4a0f-80ac-592856ee6c98",
  "sourceToolAssistantUUID": "13bcfb89-45fd-459c-bfa7-515fdb76a131",
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

_source line 20 · 2026-05-18T23:26:11.293Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XXDbxnE8Egxododjjvcg2t`</summary>

```json
{
  "query": "\"XL-DURel\" ordinal classification sentence transformers word-in-context 2024 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a99cd8a-1a00-4a0f-80ac-592856ee6c98",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu6mvh5mw2iWrUdWcBf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5960dcc-45e3-4857-8f63-4453873f00cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6Bhbgkg6CQJDXgJ1KYrSK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 21090,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 21090,
          "cache_creation_input_tokens": 788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 788,
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

_source line 21 · 2026-05-18T23:26:16.797Z_

<details><summary>↩ Tool result · `toolu_01XXDbxnE8Egxododjjvcg2t`</summary>

```text
Web search results for query: ""XL-DURel" ordinal classification sentence transformers word-in-context 2024 venue"

Links: [{"title":"(PDF) XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification","url":"https://www.researchgate.net/publication/393889711_XL-DURel_Finetuning_Sentence_Transformers_for_Ordinal_Word-in-Context_Classification"},{"title":"[2507.14578] XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification","url":"https://arxiv.org/abs/2507.14578"},{"title":"XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification","url":"https://arxiv.org/html/2507.14578v1"},{"title":"[PDF] XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XL-DURel:-Finetuning-Sentence-Transformers-for-Yadav-Schlechtweg/ce0e48f26e3860f9e3b7489114d10198b96c3817"},{"title":"XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification - ACL Anthology","url":"https://aclanthology.org/2025.findings-ijcnlp.19/"},{"title":"XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification","url":"https://www.researchgate.net/publication/402594018_XL-DURel_Finetuning_Sentence_Transformers_for_Ordinal_Word-in-Context_Classification"},{"title":"XL-DURel: Finetuning Sentence Transformers for Ordinal ...","url":"https://arxiv.org/pdf/2507.14578"},{"title":"XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/xl-durel-finetuning-sentence-transformers-ordinal-word"},{"title":"Paper page - XL-DURel: Finetuning Sentence Transformers for Ordinal Word-in-Context Classification","url":"https://huggingface.co/papers/2507.14578"}]

Based on the search results, I found detailed information about XL-DURel:

## Overview

XL-DURel is a finetuned, multilingual Sentence Transformer model optimized for ordinal Word-in-Context classification. The model tests several loss functions for regression and ranking tasks, managing to outperform previous models on ordinal and binary data with a ranking objective based on angular distance in complex space.

## Key Findings

Binary WiC can be treated as a special case of ordinal WiC and optimizing models for the general ordinal task improves performance on the more specific binary task, paving the way for a unified treatment of WiC modeling across different task formulations.

## Publication Venue

The paper was published in the Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics in December 2025 in Mumbai, India.

The paper was authored by Sachin Yadav and Dominik Schlechtweg, with the research appearing on arXiv (arxiv:2507.14578) and accepted to the Findings of IJCNLP 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5960dcc-45e3-4857-8f63-4453873f00cf",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "4fe32e90-fb65-4b0a-9920-192e6ba43f93",
  "sourceToolAssistantUUID": "c5960dcc-45e3-4857-8f63-4453873f00cf",
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

_source line 22 · 2026-05-18T23:26:19.539Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rqn1edDkjkCHHf8o6HWvmi`</summary>

```json
{
  "query": "dlordinal Python package deep ordinal classification 2024 Neurocomputing authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fe32e90-fb65-4b0a-9920-192e6ba43f93",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu7Nu8PvnXurjFqVbFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d71b015-c9b5-4f04-986d-56bbe62c02ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CV1wH76deUszA9VPctyEao",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 21878,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 21878,
          "cache_creation_input_tokens": 1030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1030,
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

_source line 23 · 2026-05-18T23:26:25.371Z_

<details><summary>↩ Tool result · `toolu_01Rqn1edDkjkCHHf8o6HWvmi`</summary>

```text
Web search results for query: "dlordinal Python package deep ordinal classification 2024 Neurocomputing authors"

Links: [{"title":"Dlordinal: A Python package for deep ordinal classification - R Discovery","url":"https://discovery.researcher.life/article/dlordinal-a-python-package-for-deep-ordinal-classification/fb1afa0c65e43e059375ecf6ee2f8bcf"},{"title":"dlordinal: a Python package for deep ordinal classification | Víctor Manuel Vargas","url":"https://vmvargasyun.com/publications/journal/4"},{"title":"Publication - dlordinal: A Python package for deep ordinal classification","url":"https://www.uco.es/grupos/ayrna/index.php/en/publications-en/articles?view=publication&task=show&id=963"},{"title":"(PDF) dlordinal: a Python package for deep ordinal classification","url":"https://www.researchgate.net/publication/382527005_dlordinal_a_Python_package_for_deep_ordinal_classification"},{"title":"dlordinal: a Python package for deep ordinal classification","url":"https://arxiv.org/html/2407.17163v2"},{"title":"dlordinal: a Python package for deep ordinal classification | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/dlordinal-python-package-deep-ordinal-classification"},{"title":"dlordinal: : A Python package for deep ordinal classification: Neurocomputing: Vol 622, No C","url":"https://dl.acm.org/doi/10.1016/j.neucom.2024.129305"},{"title":"[2407.17163] dlordinal: a Python package for deep ordinal classification","url":"https://arxiv.org/abs/2407.17163"}]

Based on the web search results, here's what I found about the dlordinal Python package:

dlordinal is a new Python library that unifies many recent deep ordinal classification methodologies available in the literature. 

**Publication Details:**
The paper was published in Neurocomputing, Vol. 622, pp. 1-19, 2025 with DOI 10.1016/j.neucom.2024.129305.

**Authors:**
The authors are Francisco Bérchez-Moreno, Rafael Ayllón-Gavilán, Víctor Manuel Vargas, David Guijo-Rubio, César Hervás-Martínez, Juan Carlos Fernández, and Pedro Antonio Gutiérrez.

**Package Features:**
The package includes ordinal classification methodologies for deep learning with ordinal dropout methodologies, output layers, soft labelling, losses and wrappers. Additionally, performance metrics to assess novel proposals in ordinal classification depend on the distance between target and predicted classes in the ordinal scale, and suitable ordinal evaluation metrics are included.

**Availability:**
dlordinal is distributed under the BSD-3-Clause license and is available at https://github.com/ayrna/dlordinal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d71b015-c9b5-4f04-986d-56bbe62c02ae",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "cb8ac56d-36ac-442a-bf97-225f6a015cd8",
  "sourceToolAssistantUUID": "9d71b015-c9b5-4f04-986d-56bbe62c02ae",
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

_source line 24 · 2026-05-18T23:26:28.398Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013X1DGT4j5PxF9LDqoaDdHK`</summary>

```json
{
  "query": "ordinal classification sentiment analysis rating prediction EMNLP NAACL ACL 2024 2025 loss function"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb8ac56d-36ac-442a-bf97-225f6a015cd8",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu81aFsGbNWtLnn7cEo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9aaad5c0-4e26-41be-a8ab-a251b3dee284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014WaK3JWLZsCeMbvVuGrd3e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 22908,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 22908,
          "cache_creation_input_tokens": 835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 835,
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

_source line 25 · 2026-05-18T23:26:35.425Z_

<details><summary>↩ Tool result · `toolu_013X1DGT4j5PxF9LDqoaDdHK`</summary>

```text
Web search results for query: "ordinal classification sentiment analysis rating prediction EMNLP NAACL ACL 2024 2025 loss function"

Links: [{"title":"A New Approach To Text Rating Classification Using Sentiment Analysis","url":"https://arxiv.org/pdf/2103.12368"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of   Explicit and Implicit Techniques","url":"https://arxiv.org/pdf/2405.11775"},{"title":"Sentiment Analysis in the Era of Large Language Models","url":"https://aclanthology.org/2024.findings-naacl.246.pdf"},{"title":"GitHub - Zhihong-Zhu/MIR-Survey: [EMNLP 2025] A Survey on Multi-modal Intent Recognition: Recent Advances and New Frontiers · GitHub","url":"https://github.com/Zhihong-Zhu/MIR-Survey"},{"title":"An Effectiveness Metric for Ordinal Classification: Formal Properties   and Experimental Results","url":"https://arxiv.org/pdf/2006.01245"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"}]

Based on the search results, here's what I found about ordinal classification, sentiment analysis, and rating prediction in recent NLP research:

## Key Findings

Ordinal Classification (OC) is a widely encountered challenge in Natural Language Processing (NLP), with applications in various domains such as sentiment analysis, rating prediction, and more.

### Approaches to Ordinal Classification

Previous approaches to tackle OC have primarily focused on modifying existing or creating novel loss functions that explicitly account for the ordinal nature of labels. However, with the advent of Pretrained Language Models (PLMs), it became possible to tackle ordinality through the implicit semantics of the labels as well.

A recent paper titled "Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques" (source 2) provides a comprehensive examination of both explicit loss function approaches and implicit approaches using PLMs for ordinal classification tasks.

### Sentiment Analysis Context

In Ordinal Classification (OC) tasks, items have to be assigned to classes that have a relative ordering, such as *positive*, *neutral*, *negative* in sentiment analysis.

The search results include a NAACL 2024 paper on sentiment analysis in the era of large language models, and references to relevant work at ACL, NAACL, and EMNLP conferences, though the most directly relevant recent work on ordinal classification and loss functions appears to be on arxiv rather than in the main conference proceedings listed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aaad5c0-4e26-41be-a8ab-a251b3dee284",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "b8536d96-b190-4294-9456-00719046cc3e",
  "sourceToolAssistantUUID": "9aaad5c0-4e26-41be-a8ab-a251b3dee284",
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

_source line 26 · 2026-05-18T23:26:38.574Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KSc2CM3SPvxrdcUiKjWy52`</summary>

```json
{
  "query": "CORN conditional ordinal regression neural network Raschka 2022 CORAL extensions 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8536d96-b190-4294-9456-00719046cc3e",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu8kbsc3bUJCfpRb473",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f381289e-2477-4396-b3b8-670901bcbcaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XhnxmhE16Nc8oRcgDSs8G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 23743,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 792
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 23743,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 792,
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

_source line 27 · 2026-05-18T23:26:43.911Z_

<details><summary>↩ Tool result · `toolu_01KSc2CM3SPvxrdcUiKjWy52`</summary>

```text
Web search results for query: "CORN conditional ordinal regression neural network Raschka 2022 CORAL extensions 2024"

Links: [{"title":"Deep Neural Networks for Rank-Consistent Ordinal ...","url":"https://arxiv.org/pdf/2111.08851"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities","url":"https://arxiv.org/html/2111.08851v5"},{"title":"[2111.08851] Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities","url":"https://arxiv.org/abs/2111.08851"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities | Pattern Analysis & Applications","url":"https://dl.acm.org/doi/abs/10.1007/s10044-023-01181-9"},{"title":"CORN convolutional neural net for image data (MNIST dataset) - coral_pytorch","url":"https://raschka-research-group.github.io/coral-pytorch/tutorials/pytorch_lightning/ordinal-corn_mnist/"},{"title":"GitHub - Raschka-research-group/corn-ordinal-neuralnet: Code and experiments for \"Deep Neural Networks for Rank Consistent Ordinal Regression based on Conditional Probabilities\"","url":"https://github.com/Raschka-research-group/corn-ordinal-neuralnet"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities","url":"https://www.researchgate.net/publication/371915425_Deep_neural_networks_for_rank-consistent_ordinal_regression_based_on_conditional_probabilities"},{"title":"GitHub - Raschka-research-group/coral-pytorch: CORAL and CORN implementations for ordinal regression with deep neural networks. · GitHub","url":"https://github.com/Raschka-research-group/coral-pytorch"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities | Pattern Analysis and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10044-023-01181-9"}]

Based on the search results, I found comprehensive information about CORN and its relationship to CORAL:

## CORN (Conditional Ordinal Regression for Neural Networks)

CORN is a method for ordinal regression with deep neural networks, which addresses the rank inconsistency issue of other ordinal regression frameworks. The method was developed by Xintong Shi, Wenzhi Cao, and Sebastian Raschka (2021) and titled "Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities."

## Key Technical Approach

CORN achieves rank consistency by a novel training scheme that uses conditional training sets to obtain the unconditional rank probabilities through applying the chain rule for conditional probability distributions.

## Advantages Over CORAL

CORAL is limited by a weight-sharing constraint in a neural network's fully connected output layer, which may restrict the expressiveness and capacity of a network trained using CORAL. In contrast, the absence of the weight-sharing restriction in CORN improves the performance substantially compared to the CORAL reference approach.

## Flexibility

CORN is not tied to any specific architecture and can be utilized with any deep neural network classifier to train it for ordinal regression tasks.

The search results contain the original 2021 paper but don't show specific 2024 extensions mentioned in your query. The most recent reference in the results is from 2023 when the paper was published in Pattern Analysis & Applications journal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f381289e-2477-4396-b3b8-670901bcbcaa",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "8f5d9fb7-27d4-4920-acbb-dc9f51a65d46",
  "sourceToolAssistantUUID": "f381289e-2477-4396-b3b8-670901bcbcaa",
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

_source line 28 · 2026-05-18T23:26:46.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LQJdsJwDyo3ZL6HhkEtCPK`</summary>

```json
{
  "query": "\"ordinal classification\" \"machine-generated text\" detection OR \"AI-generated\" 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f5d9fb7-27d4-4920-acbb-dc9f51a65d46",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAu9NqxJbiMabhAwrTRi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2be71222-fd8c-403b-bff7-ea833fa4bb3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zPNSRcE6MroBbmTMRWxQQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 952,
      "cache_read_input_tokens": 24535,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 952
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 24535,
          "cache_creation_input_tokens": 952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 952,
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

_source line 29 · 2026-05-18T23:26:54.464Z_

<details><summary>↩ Tool result · `toolu_01LQJdsJwDyo3ZL6HhkEtCPK`</summary>

```text
Web search results for query: ""ordinal classification" "machine-generated text" detection OR "AI-generated" 2024 2025"

Links: [{"title":"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification","url":"https://arxiv.org/html/2505.11550v1"},{"title":"A Comprehensive Dataset for Human vs. AI Generated Text Detection","url":"https://arxiv.org/html/2510.22874v1"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Benchmarking AI Text Detection: Assessing Detectors ...","url":"https://aclanthology.org/2025.genaidetect-1.4.pdf"},{"title":"Mast Kalandar at SemEval-2024 Task 8: On the Trail of Textual Origins:   RoBERTa-BiLSTM Approach to Detect AI-Generated Text","url":"https://arxiv.org/pdf/2407.02978"},{"title":"mdok of KInIT: Robustly Fine-tuned LLM for Binary and Multiclass AI-Generated Text Detection","url":"https://arxiv.org/pdf/2506.01702"},{"title":"Frontiers | Investigating generative AI models and detection techniques: impacts of tokenization and dataset size on identification of AI-generated text","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1469197/full"},{"title":"Detecting AI-Generated Text: : Factors Influencing ...","url":"https://dl.acm.org/doi/pdf/10.1613/jair.1.16665"}]

I've found several relevant research results on AI-generated text detection from 2024-2025. Here's what the search revealed:

## Recent Research on AI-Generated Text Detection

A 2025 survey in Computational Linguistics discusses LLM-generated text detection methods and future directions. The research covers both detection approaches and challenges in this rapidly evolving field.

### Detection Methods and Approaches

Detection methods can be categorized as statistical and training-based approaches, with statistical/zero-shot detection methods identifying AI-generated text without task-specific training. Attributes such as perplexity and semantic features are found to be effective for distinguishing between human-written and machine-generated texts.

### Multiclass Classification Tasks

SemEval 2024 introduced a task focused on Multigenerator, Multidomain, and Multilingual Black-Box Machine-Generated Text Detection. Recent systems have shown remarkable performance in both binary detection and multiclass classification of various cases of human-AI collaboration.

### Current Challenges

As LLM-generated outputs grow more sophisticated and human-like, detecting them has become an increasingly difficult challenge. Additional challenges exist in applying trained detectors to out-of-distribution data that are significantly different from training data.

The search results show active research in 2024-2025 focused on developing more robust detection systems across multiple languages, domains, and text types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2be71222-fd8c-403b-bff7-ea833fa4bb3b",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "e994cf77-9be8-48ab-aa7e-606ead213914",
  "sourceToolAssistantUUID": "2be71222-fd8c-403b-bff7-ea833fa4bb3b",
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

_source line 30 · 2026-05-18T23:26:57.239Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mc1GQRMmtNcEd1mvAvBaf8`</summary>

```json
{
  "query": "ordinal regression random forest feature-based text classification 2024 statistical features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e994cf77-9be8-48ab-aa7e-606ead213914",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuA9vrNHa2bv1XNuCtC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da0503cf-5823-4ccb-807a-fe730d7eae6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBP8NLGjqRPmkFDtoQTsre",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 25487,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 835
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 25487,
          "cache_creation_input_tokens": 835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 835,
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

_source line 31 · 2026-05-18T23:27:04.393Z_

<details><summary>↩ Tool result · `toolu_01Mc1GQRMmtNcEd1mvAvBaf8`</summary>

```text
Web search results for query: "ordinal regression random forest feature-based text classification 2024 statistical features"

Links: [{"title":"MOX-Report No. 41/2024 Ordinal Mixed-Effects Random Forest","url":"https://www.mate.polimi.it/biblioteca/add/qmox/41-2024.pdf"},{"title":"A novel improved random forest for text classification using feature ranking and optimal number of trees - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1319157822000969"},{"title":"Random forest for ordinal responses: Prediction and variable selection | Request PDF","url":"https://www.researchgate.net/publication/284013341_Random_forest_for_ordinal_responses_Prediction_and_variable_selection"},{"title":"Random forest for ordinal responses: Prediction and variable selection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0167947315002601"},{"title":"Ordinal Forests | Journal of Classification | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00357-018-9302-x"},{"title":"Random forest for ordinal responses: Prediction and variable selection","url":"https://ideas.repec.org/a/eee/csdana/v96y2016icp57-73.html"}]

I found several relevant research results for your search query. Here's what the search returned:

**Recent 2024 Work:**
The search found a 2024 MOX-Report on Ordinal Mixed-Effects Random Forest that extends regression trees to account for clustered and longitudinal data, suited for handling hierarchical data structures.

**Text Classification with Random Forest:**
A study presents an improved random forest for text classification (IRFTC) that incorporates bootstrapping and random subspace methods simultaneously, removes unimportant features, and monitors classification performance. Results indicate IRFTC outperforms traditional RF and other machine learning models such as logistic regression, support vector machine, Naive Bayes, and decision trees.

**Ordinal Regression with Random Forest:**
Machine learning methods such as random forest are increasingly employed for ordinal prediction, where traditionally parametric statistical models like the proportional odds model were used. Since RF does not inherently account for ordinality, a promising approach involves assigning optimized numeric scores to the ordinal response categories and using regression RF.

Ordinal forests allow prediction using both low-dimensional and high-dimensional covariate data and can be used to rank covariates with respect to their importance for prediction.

The search results show active research in combining ordinal regression methods with random forest approaches for various applications, including text classification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da0503cf-5823-4ccb-807a-fe730d7eae6a",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "5a30331e-3708-4c54-b204-88a81b60ff37",
  "sourceToolAssistantUUID": "da0503cf-5823-4ccb-807a-fe730d7eae6a",
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

_source line 32 · 2026-05-18T23:27:07.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SZQZNFyA6BY2n88bUTG4eR`</summary>

```json
{
  "query": "\"Exploring Ordinality in Text Classification\" Kasa ACL 2024 Findings details results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a30331e-3708-4c54-b204-88a81b60ff37",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuAtQEYHW1tQNyU8sNt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7905ab7a-864d-4255-bdde-bcf93654d861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8GtGkwArsMCe1yySiiiTV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 26322,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 732
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26322,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 732,
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

_source line 33 · 2026-05-18T23:27:14.275Z_

<details><summary>↩ Tool result · `toolu_01SZQZNFyA6BY2n88bUTG4eR`</summary>

```text
Web search results for query: ""Exploring Ordinality in Text Classification" Kasa ACL 2024 Findings details results"

Links: [{"title":"Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.320/"},{"title":"Generative or Discriminative? Revisiting Text Classification in the Era of Transformers","url":"https://arxiv.org/html/2506.12181v1"},{"title":"Accepted Findings Papers - ACL 2024","url":"https://2024.aclweb.org/program/finding_papers/"},{"title":"Computation and Language May 2024","url":"https://arxiv.org/list/cs.CL/2024-05?skip=600&show=100"},{"title":"ACL 2024 - Amazon Science","url":"https://www.amazon.science/conferences-and-events/acl-2024"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques | OpenReview","url":"https://openreview.net/forum?id=XUqyfa8X14"},{"title":"[2405.11775] Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques","url":"https://arxiv.org/abs/2405.11775"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques","url":"https://arxiv.org/html/2405.11775v1"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of   Explicit and Implicit Techniques","url":"https://arxiv.org/pdf/2405.11775"}]

Based on the search results, here are the details about "Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques" by Kasa et al., published in ACL 2024 Findings:

## Publication Details

The paper is titled "Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques" and was published in Findings of the Association for Computational Linguistics: ACL 2024, pages 5390–5404, Bangkok, Thailand.

**Authors:** Siva Rajesh Kasa, Aniket Goel, Karan Gupta, Sumegh Roychowdhury, Pattisapu Priyatam, Anish Bhanushali, and Prasanna Srinivasa Murthy.

## Research Overview

Ordinal Classification (OC) is a widely encountered challenge in Natural Language Processing (NLP), with applications in various domains such as sentiment analysis, rating prediction, and more.

## Key Contributions

The paper conducts a comprehensive analysis of several explicit loss-based approaches for Ordinal Classification (OC), examining them through the lens of useful theoretical properties, such as proper scoring rule, convexity, unimodality and ordinality.

The empirical findings demonstrate that previously proposed techniques for solving OC excel primarily in ordinal metrics while compromising performance on nominal metrics. This analysis led to proposing a hybrid loss function that achieves a better balance between nominal and ordinal metrics compared to the performance of its individual components.

The paper also studies two general PLM based methodologies (encoder & decoder-based) that implicitly factor in ordinality. These approaches signify a paradigm shift from traditional methods, opening up new avenues in ordinal classification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7905ab7a-864d-4255-bdde-bcf93654d861",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "12760d4f-9dff-4535-bce0-e3582154654a",
  "sourceToolAssistantUUID": "7905ab7a-864d-4255-bdde-bcf93654d861",
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

_source line 34 · 2026-05-18T23:27:16.738Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NKSUSxbMmzVEmwDyoWpsAA`</summary>

```json
{
  "query": "\"ordinal regression\" OR \"ordinal classification\" NeurIPS ICML ICLR 2024 2025 deep learning method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12760d4f-9dff-4535-bce0-e3582154654a",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuBcfDaLo8XYnR2s7y6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "225a111b-bf67-4cf8-85ac-ceda5b11c895",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BFs1XF4aEPbgfC4MTDfBE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 27054,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 27054,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 936,
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

_source line 35 · 2026-05-18T23:27:23.899Z_

<details><summary>↩ Tool result · `toolu_01NKSUSxbMmzVEmwDyoWpsAA`</summary>

```text
Web search results for query: ""ordinal regression" OR "ordinal classification" NeurIPS ICML ICLR 2024 2025 deep learning method"

Links: [{"title":"Ordinal Regression as Structured Classification","url":"https://arxiv.org/pdf/1905.13658"},{"title":"THOR: Threshold-Based Ranking Loss for Ordinal Regression","url":"https://arxiv.org/pdf/2205.04864"},{"title":"Multivariate decoding of brain images using ordinal regression","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4068378/"},{"title":"Continuously Generalized Ordinal Regression for Linear and Deep Models","url":"https://arxiv.org/pdf/2202.07005"},{"title":"Continuously generalized ordinal regression","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11727037"},{"title":"A Survey on Ordinal Regression: Applications, Advances, and Prospects","url":"https://arxiv.org/html/2503.00952v1"},{"title":"Meta Ordinal Regression Forest for Medical Image Classification with   Ordinal Labels","url":"https://arxiv.org/pdf/2203.07725"}]

I found several relevant research papers and resources on ordinal regression and ordinal classification methods. Here's what the search revealed:

## Key Findings

**Recent Survey (2025):** Ordinal regression refers to classifying object instances into ordinal categories and is crucial for applications like facial age estimation, image aesthetics assessment, and cancer staging. Unlike normal classification, ordinal regression takes into account the natural ordering of categories in the response variable.

**Deep Learning Methods:** The search revealed several deep learning approaches:

1. A continuously generalized ordinal regression approach that proposes a regularization method interpolating between different extremes of model flexibility

2. THOR (Threshold-Based Ranking Loss for Ordinal Regression), which achieves strong MAE results compared to state-of-the-art ordinal regression algorithms using deep learning

3. Methods like neural-stick breaking (NSB), unimodal approaches, and soft ordinal label (SORD) that improve ordinal regression performance through rectified label space or CNN output probability calculations

4. DAR, which integrates autoregressive models with ordinal regression for local depth distribution modeling

**Problem Motivation:** The relative ordering of labels is not captured by loss functions used for multiclass classification, such as cross entropy, which assumes independence between class labels.

The search results primarily returned papers from arxiv and other venues, though I didn't find papers explicitly presenting at NeurIPS, ICML, or ICLR 2024-2025 in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "225a111b-bf67-4cf8-85ac-ceda5b11c895",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "071422f1-cdfd-488e-b83f-ecdd6cc873a0",
  "sourceToolAssistantUUID": "225a111b-bf67-4cf8-85ac-ceda5b11c895",
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

_source line 36 · 2026-05-18T23:27:26.800Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AG9D1oxr5tAmFiaud4Gfjd`</summary>

```json
{
  "query": "\"Exploring Ordinal Classification for Spoken Language Assessment\" 2024 2025 venue authors CEFR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "071422f1-cdfd-488e-b83f-ecdd6cc873a0",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuCKqDNaJskayJM6r9E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8b8d38d-490e-4200-aef0-6ba3382cc027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFPmMNjzZGiuHaKaBE4EYA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 27990,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 754
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 27990,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 754,
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

_source line 37 · 2026-05-18T23:27:33.903Z_

<details><summary>↩ Tool result · `toolu_01AG9D1oxr5tAmFiaud4Gfjd`</summary>

```text
Web search results for query: ""Exploring Ordinal Classification for Spoken Language Assessment" 2024 2025 venue authors CEFR"

Links: [{"title":"Exploring Ordinal Classification for Spoken Language Assessment | Request PDF","url":"https://www.researchgate.net/publication/395789601_Exploring_Ordinal_Classification_for_Spoken_Language_Assessment"},{"title":"HiPPO: Exploring A Novel Hierarchical Pronunciation Assessment Approach for Spoken Languages","url":"https://arxiv.org/pdf/2512.04964"},{"title":"Comparison of End-to-end Speech Assessment Models for the NOCASA 2025 Challenge","url":"https://arxiv.org/pdf/2509.03256"},{"title":"The NTNU System at the S&I Challenge 2025 SLA Open Track","url":"https://arxiv.org/pdf/2506.05121"},{"title":"Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning","url":"https://arxiv.org/pdf/2509.16025"},{"title":"Assessment of L2 Oral Proficiency using Speech Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/392132802_Assessment_of_L2_Oral_Proficiency_using_Speech_Large_Language_Models"},{"title":"Speak & Improve Corpus 2025: an L2 English Speech Corpus for Language Assessment and Feedback","url":"https://arxiv.org/html/2412.11986v2"}]

Based on the search results, I found information about research related to ordinal classification for spoken language assessment. Here's what I found:

## Paper Information

The research proposes a rank-consistent ordinal regression framework (CORN) that achieves rank consistency through a novel training scheme for spoken language assessment.

## Related Work

The search results also reveal several related papers from 2024-2025:

1. **Speak & Improve Challenge 2025**: The Speak & Improve Challenge 2025 provides a benchmark for spoken language assessment systems under constraints of limited data and computational resources.

2. **Corpus Details**: The Speak & Improve Corpus 2025 features CEFR levels from A2 to B2, which relates to the CEFR assessment framework you asked about.

3. **Related Methodologies**: Recent work uses weighted ordinal cross-entropy loss tailored for optimizing metrics such as unweighted average recall and mean absolute error in speech assessment tasks.

The primary ResearchGate entry indicates this is an active area of research in 2024-2025, though the search results don't provide complete details about all the authors and venue information. For more specific details about the exact venue and complete author list, you may want to visit the ResearchGate page directly or check the corresponding arXiv submission.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8b8d38d-490e-4200-aef0-6ba3382cc027",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "f74ce931-45b9-49b2-ae5b-02870c0a0a56",
  "sourceToolAssistantUUID": "e8b8d38d-490e-4200-aef0-6ba3382cc027",
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

_source line 38 · 2026-05-18T23:27:36.458Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CgWxntLGQyoUwgP188vy8Y`</summary>

```json
{
  "query": "survey ordinal regression 2025 arxiv Zhu taxonomy deep learning comprehensive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f74ce931-45b9-49b2-ae5b-02870c0a0a56",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuD4ZjFo68LBcUiQLKk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df10fc86-cbe8-4dba-99fe-96c7120eccf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpfrMDtZnCqaZBWUHX3xaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 28744,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 28744,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 771,
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

_source line 39 · 2026-05-18T23:27:42.898Z_

<details><summary>↩ Tool result · `toolu_01CgWxntLGQyoUwgP188vy8Y`</summary>

```text
Web search results for query: "survey ordinal regression 2025 arxiv Zhu taxonomy deep learning comprehensive"

Links: [{"title":"[2503.00952] A Survey on Ordinal Regression: Applications, Advances and Prospects","url":"https://arxiv.org/abs/2503.00952"},{"title":"A Survey on Ordinal Regression: Applications, Advances and Prospects | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/survey-ordinal-regression-applications-advances-prospects"},{"title":"A Survey on Ordinal Regression: Applications, Advances, and Prospects","url":"https://arxiv.org/html/2503.00952v1"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities | Pattern Analysis & Applications","url":"https://dl.acm.org/doi/abs/10.1007/s10044-023-01181-9"},{"title":"1 Tackling Ordinal Regression Problem for Heterogeneous Data: Sparse and Deep","url":"https://arxiv.org/pdf/1907.12508"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities","url":"https://arxiv.org/html/2111.08851v5"},{"title":"Deep and interpretable regression models for ordinal outcomes","url":"https://arxiv.org/pdf/2010.08376"},{"title":"Continuously Generalized Ordinal Regression for Linear and Deep Models","url":"https://arxiv.org/pdf/2202.07005"},{"title":"Deep Ordinal Regression using Optimal Transport Loss and Unimodal Output   Probabilities","url":"https://arxiv.org/pdf/2011.07607"}]

I found the paper you're looking for! This is a comprehensive examination of advances and applications of ordinal regression published on arXiv in March 2025.

**Key Details:**

- **Title:** A Survey on Ordinal Regression: Applications, Advances and Prospects
- **arXiv ID:** 2503.00952
- **Publication Date:** March 2, 2025

**Survey Structure:**

The survey introduces a systematic taxonomy that classifies techniques and applications into three well-defined categories: Continuous Space Discretization, Distribution Ordering Learning, and Ambiguous Instance Delving.

**Applications:**

Ordinal regression is crucial for applications in various areas like facial age estimation, image aesthetics assessment, and even cancer staging, due to its capability to utilize ordered information effectively.

**Key Benefits:**

It also enhances model interpretation by considering category order, aiding the understanding of data trends and causal relationships.

The survey appears to be a comprehensive resource on the state-of-the-art in ordinal regression, particularly focusing on deep learning approaches and their applications across diverse domains. You can access the full paper directly at https://arxiv.org/abs/2503.00952.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df10fc86-cbe8-4dba-99fe-96c7120eccf3",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "117b9a46-beed-420d-839c-716bedb33ca6",
  "sourceToolAssistantUUID": "df10fc86-cbe8-4dba-99fe-96c7120eccf3",
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

_source line 40 · 2026-05-18T23:27:45.556Z_

Now let me get the authors list for the survey paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "117b9a46-beed-420d-839c-716bedb33ca6",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuDj3VsVb6NhiTwiV76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43fec95c-b736-4c35-b5a9-d8bd54c8e5a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WTiJdFfdVDCmGWpBKJZL1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 29515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 889,
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

_source line 41 · 2026-05-18T23:27:45.937Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013yCeL1Z2vnJTdy2MNmtJ9o`</summary>

```json
{
  "query": "arxiv 2503.00952 \"A Survey on Ordinal Regression\" authors list first author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43fec95c-b736-4c35-b5a9-d8bd54c8e5a1",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuDj3VsVb6NhiTwiV76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58f05934-608d-43c5-9f19-0e7902331d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WTiJdFfdVDCmGWpBKJZL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 29515,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 889
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 29515,
          "cache_creation_input_tokens": 889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 889,
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

_source line 42 · 2026-05-18T23:27:50.834Z_

<details><summary>↩ Tool result · `toolu_013yCeL1Z2vnJTdy2MNmtJ9o`</summary>

```text
Web search results for query: "arxiv 2503.00952 "A Survey on Ordinal Regression" authors list first author"

Links: [{"title":"[2503.00952] A Survey on Ordinal Regression: Applications, Advances and Prospects","url":"https://arxiv.org/abs/2503.00952"},{"title":"A Survey on Ordinal Regression: Applications, Advances, and Prospects","url":"https://arxiv.org/html/2503.00952"},{"title":"A Survey on Ordinal Regression: Applications, Advances and Prospects | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/survey-ordinal-regression-applications-advances-prospects"},{"title":"Applying survey weights to ordinal regression models for improved inference in outcome-dependent samples with ordinal outcomes","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11577697/"},{"title":"A Brief Introduction on Latent Variable Based Ordinal Regression Models With an Application to Survey Data","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11588990/"},{"title":"[2309.16373] Regularization and Model Selection for Ordinal-on-Ordinal Regression with Applications to Food Products' Testing and Survey Data","url":"https://arxiv.org/abs/2309.16373"}]

Based on the search results, the first author of the paper "A Survey on Ordinal Regression: Applications, Advances and Prospects" (arxiv 2503.00952) is Jinhong Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58f05934-608d-43c5-9f19-0e7902331d75",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "bc0d6d14-bb34-4457-948e-0f5492eaa61d",
  "sourceToolAssistantUUID": "58f05934-608d-43c5-9f19-0e7902331d75",
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

_source line 43 · 2026-05-18T23:27:53.443Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UVbp9ZBuPirSW7vBDKQzrb`</summary>

```json
{
  "query": "THOR threshold ranking loss ordinal regression NeurIPS 2024 2025 venue citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc0d6d14-bb34-4457-948e-0f5492eaa61d",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuEK5soYhvuz3WyjDEi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cf6e655-cc52-4a39-9069-6cb2f56c7372",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RfxTEcahceWYBQq6eLyjfH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 30404,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 30404,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 506,
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

_source line 44 · 2026-05-18T23:27:59.363Z_

<details><summary>↩ Tool result · `toolu_01UVbp9ZBuPirSW7vBDKQzrb`</summary>

```text
Web search results for query: "THOR threshold ranking loss ordinal regression NeurIPS 2024 2025 venue citation"

Links: [{"title":"THOR: Threshold-Based Ranking Loss for Ordinal Regression","url":"https://arxiv.org/pdf/2205.04864"},{"title":"THOR: Threshold-Based Ranking Loss for Ordinal Regression | Request PDF","url":"https://www.researchgate.net/publication/360512681_THOR_Threshold-Based_Ranking_Loss_for_Ordinal_Regression"},{"title":"[2205.04864] THOR: Threshold-Based Ranking Loss for Ordinal Regression","url":"https://arxiv.org/abs/2205.04864"},{"title":"[2405.13288] Remarks on Loss Function of Threshold Method for Ordinal Regression Problem","url":"https://arxiv.org/abs/2405.13288"},{"title":"Remarks on Loss Function of Threshold Method for Ordinal Regression   Problem","url":"https://arxiv.org/pdf/2405.13288"},{"title":"Parallel Algorithm for Optimal Threshold Labeling of Ordinal Regression   Methods","url":"https://arxiv.org/pdf/2405.12756"}]

Based on the search results, I found information about the THOR paper. THOR: Threshold-Based Ranking Loss for Ordinal Regression was authored by Tzeviya Sylvia Fuchs and Joseph Keshet from Bar-Ilan University in Israel.

However, the search results indicate that the paper was posted to arXiv on May 10, 2022 (arxiv ID 2205.04864), which predates both NeurIPS 2024 and 2025. The search results do not show that this paper was published at NeurIPS in 2024 or 2025.

The paper presents a novel threshold-based pairwise loss function that aims at minimizing regression error and the Mean Absolute Error (MAE) measure. The results appear to reference the arXiv preprint rather than a conference venue publication in the 2024-2025 timeframe.

If you're looking for information about whether this paper was accepted to NeurIPS 2024 or 2025, or if there's a different venue publication, please let me know and I can search for more specific information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cf6e655-cc52-4a39-9069-6cb2f56c7372",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "c00c13ac-f5cc-4170-9460-22aaae2ff6b5",
  "sourceToolAssistantUUID": "0cf6e655-cc52-4a39-9069-6cb2f56c7372",
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

_source line 45 · 2026-05-18T23:28:02.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FtQbVf6K1Mo7LL8cvy9hc7`</summary>

```json
{
  "query": "\"Ordinal Mixed-Effects Random Forest\" 2024 Politecnico Milano ordinal response prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c00c13ac-f5cc-4170-9460-22aaae2ff6b5",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuEwRAUN3FJWp7nXedB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4a7b49a-7003-4bad-8f7d-d2ba7e832e84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuZQwokyKnr3wuYSVsvhZB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 655,
      "cache_read_input_tokens": 30910,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 30910,
          "cache_creation_input_tokens": 655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 655,
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

_source line 46 · 2026-05-18T23:28:09.395Z_

<details><summary>↩ Tool result · `toolu_01FtQbVf6K1Mo7LL8cvy9hc7`</summary>

```text
Web search results for query: ""Ordinal Mixed-Effects Random Forest" 2024 Politecnico Milano ordinal response prediction"

Links: [{"title":"MOX-Report No. 41/2024 Ordinal Mixed-Effects Random Forest","url":"https://www.mate.polimi.it/biblioteca/add/qmox/41-2024.pdf"},{"title":"Ordinal Mixed-Effects Random Forest","url":"https://arxiv.org/html/2406.03130v1"},{"title":"New MOX Report on “Ordinal Mixed-Effects Random Forest”","url":"https://mox.polimi.it/new-mox-report-on-ordinal-mixed-effects-random-forest/"},{"title":"[2406.03130] Ordinal Mixed-Effects Random Forest","url":"https://arxiv.org/abs/2406.03130"},{"title":"A review on longitudinal data analysis with random forest - PMC","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10025446/"},{"title":"Ordinal Mixed-Effects Random Forest","url":"https://arxiv.org/pdf/2406.03130"},{"title":"Random forest for ordinal responses: Prediction and variable selection | Request PDF","url":"https://www.researchgate.net/publication/284013341_Random_forest_for_ordinal_responses_Prediction_and_variable_selection"},{"title":"Full article: Mixed-Effects Frequency-Adjusted Borders Ordinal Forest: A Tree Ensemble Method for Ordinal Prediction with Hierarchical Data","url":"https://www.tandfonline.com/doi/full/10.1080/00273171.2025.2547416"},{"title":"Mixed-Effects Frequency-Adjusted Borders Ordinal Forest: A Tree Ensemble Method for Ordinal Prediction with Hierarchical Data","url":"https://ideas.repec.org/p/osf/osfxxx/ny6we.html"}]

I found relevant information about the Ordinal Mixed-Effects Random Forest research from Politecnico Milano. Here are the search results:

## Overview

Ordinal Mixed-Effect Random Forest (OMERF) is an innovative statistical method that extends the use of random forest to the analysis of hierarchical data and ordinal responses.

## Key Features

The model preserves the flexibility and ability of modeling complex patterns of both categorical and continuous variables, typical of tree-based ensemble methods, and, at the same time, takes into account the structure of hierarchical data, modeling the dependence structure induced by the grouping and allowing statistical inference at all data levels.

## Research and Validation

A simulation study is conducted to validate the performance of the proposed method and to compare it to the one of other state-of-the art models. The application of OMERF is exemplified in a case study focusing on predicting students performances using data from the Programme for International Student Assessment (PISA) 2022.

## Authors and Publication

The research was conducted by researchers at MOX Laboratory and the Department of Mathematics at Politecnico di Milano, including Giulia Bergonzoli, Lidia Rossi, and Chiara Masci. The work appears to have been published as a MOX Report in 2024 and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4a7b49a-7003-4bad-8f7d-d2ba7e832e84",
  "isSidechain": true,
  "promptId": "749484f7-8ce0-4a66-9d3b-8d5c11c25a59",
  "agentId": "a2a86d0fd624e91a0",
  "type": "user",
  "uuid": "38986efa-a4ed-4960-8134-f4aa45265a5b",
  "sourceToolAssistantUUID": "a4a7b49a-7003-4bad-8f7d-d2ba7e832e84",
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

_source line 47 · 2026-05-18T23:28:48.010Z_

Based on all my searches, here is the compiled report.

---

## Ordinal Classification / Ordinal Regression Papers (2024-2025)

The search reveals that ordinal classification in NLP is a relatively niche topic. Most ordinal regression research targets computer vision (age estimation, medical imaging). I found one directly relevant top-venue NLP paper, one comprehensive survey, and the foundational CORAL/CORN works that remain the primary references. Below are the recommended papers.

---

### Paper 1 (Strongly Recommend)

**Title:** Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques

**Authors:** Siva Rajesh Kasa, Aniket Goel, Karan Gupta, Sumegh Roychowdhury, Pattisapu Priyatam, Anish Bhanushali, Prasanna Srinivasa Murthy

**Venue:** Findings of ACL 2024 (pp. 5390-5404, Bangkok)

**URL:** https://aclanthology.org/2024.findings-acl.320/

**Relevance:** This is the most directly relevant paper. It systematically compares explicit ordinal loss functions (including CORAL-style approaches) and implicit PLM-based methods for ordinal text classification. The paper examines theoretical properties (proper scoring rule, convexity, unimodality, ordinality) and proposes a hybrid loss balancing nominal and ordinal metrics. This directly relates to the paper's use of ordinal loss for depth classification.

**Cite:** Yes

**Where:** Related Work (ordinal classification subsection) and possibly Method section when justifying the CORAL-style loss choice.

**Reason:** Only top-venue NLP paper from 2024-2025 that systematically studies ordinal loss functions for text classification. Directly validates the design space your paper operates in.

---

### Paper 2 (Recommend)

**Title:** A Survey on Ordinal Regression: Applications, Advances and Prospects

**Authors:** Jinhong Wang et al.

**Venue:** arXiv 2503.00952 (March 2025, comprehensive survey)

**URL:** https://arxiv.org/abs/2503.00952

**Relevance:** A 2025 survey that provides a systematic taxonomy of ordinal regression techniques across three categories: Continuous Space Discretization, Distribution Ordering Learning, and Ambiguous Instance Delving. Covers deep learning methods including CORAL, CORN, soft labeling, and unimodal approaches. Good for positioning the ordinal classification methodology choice.

**Cite:** Maybe (useful but arXiv-only survey, not peer-reviewed)

**Where:** Related Work, as a general reference for ordinal regression methodology.

**Reason:** Provides a comprehensive taxonomy that helps readers unfamiliar with ordinal regression understand the landscape. Cite only if you need a general reference for the ordinal regression field; skip if space is tight.

---

### Paper 3 (Foundational, should already be cited)

**Title:** Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation (CORAL)

**Authors:** Wenzhi Cao, Vahid Mirjalili, Sebastian Raschka

**Venue:** Pattern Recognition Letters, 140:325-331, 2020

**URL:** https://dl.acm.org/doi/10.1016/j.patrec.2020.11.008

**Relevance:** The original CORAL paper. Since your paper explicitly uses CORAL-style ordinal loss, this is a mandatory citation. CORAL uses weight sharing in the penultimate layer and binary decomposition of ordinal labels to guarantee rank-consistent predictions.

**Cite:** Yes (mandatory if using CORAL loss)

**Where:** Method section where CORAL loss is introduced.

**Reason:** Primary methodological reference for the ordinal loss function used in the paper.

---

### Paper 4 (Foundational, recommend)

**Title:** Deep Neural Networks for Rank-Consistent Ordinal Regression Based on Conditional Probabilities (CORN)

**Authors:** Xintong Shi, Wenzhi Cao, Sebastian Raschka

**Venue:** Pattern Analysis and Applications, 2023 (arXiv: 2111.08851)

**URL:** https://arxiv.org/abs/2111.08851

**Relevance:** CORN extends CORAL by removing the weight-sharing constraint, using conditional probabilities and the chain rule to achieve rank consistency with improved expressiveness. If your paper discusses alternatives to CORAL or ablates different ordinal loss variants, CORN is the natural comparison point.

**Cite:** Maybe

**Where:** Method section or Related Work, as an alternative to CORAL.

**Reason:** Cite if you discuss why CORAL was chosen over alternatives, or if you want to show awareness of the full CORAL/CORN family.

---

### Paper 5 (Recommend as tooling reference)

**Title:** dlordinal: A Python Package for Deep Ordinal Classification

**Authors:** Francisco Berchez-Moreno, Rafael Ayllon-Gavilan, Victor Manuel Vargas, David Guijo-Rubio, Cesar Hervas-Martinez, Juan Carlos Fernandez, Pedro Antonio Gutierrez

**Venue:** Neurocomputing, Vol. 622, 2025

**URL:** https://arxiv.org/abs/2407.17163

**Relevance:** A 2024-2025 software paper that unifies deep ordinal classification methods (ordinal dropout, output layers, soft labeling, CORAL/CORN losses). Demonstrates that ordinal classification for deep learning is an active research area with growing infrastructure.

**Cite:** No (tooling paper, not methodologically necessary unless you used the library)

**Where:** N/A

**Reason:** Only cite if you used the library or need to argue that ordinal deep learning is an active area.

---

### Summary of Recommendations

| Priority | Paper | Venue | Cite? |
|----------|-------|-------|-------|
| 1 | Kasa et al., "Exploring Ordinality in Text Classification" | Findings of ACL 2024 | **Yes** |
| 2 | Cao et al., CORAL | Pattern Recognition Letters 2020 | **Yes** (mandatory) |
| 3 | Wang et al., Ordinal Regression Survey | arXiv 2025 | Maybe |
| 4 | Shi et al., CORN | Pattern Analysis & Applications 2023 | Maybe |
| 5 | Berchez-Moreno et al., dlordinal | Neurocomputing 2025 | No |

**Key observation:** Ordinal classification in NLP at top venues is sparse. Kasa et al. (ACL 2024 Findings) is the only recent top-venue NLP paper directly studying ordinal losses for text. This is actually advantageous for positioning: it means your application of ordinal classification to recursive generation depth estimation is novel and under-explored in NLP, which strengthens the contribution claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38986efa-a4ed-4960-8134-f4aa45265a5b",
  "isSidechain": true,
  "agentId": "a2a86d0fd624e91a0",
  "requestId": "req_011CbAuFgK6oHk9NnxNAdtVp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dfab569-f39b-42b8-ac7c-5b673da40f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "7a0bb754-3fd0-4566-85e1-413b9070cbe1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArMASWLEvoE9kV7KcxpS7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 31565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 870,
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
