# Research conversation: You are helping review an ML paper idea about using data-flow analysis labels to train a neural context selector for rep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6f8ff7c85e9b6801.jsonl`
- **Structured JSON:** [`e8cbb47cca3ea6d17e31.json`](../../sessions/e8/e8cbb47cca3ea6d17e31.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-10T18:05:19.135Z_

You are helping review an ML paper idea about using data-flow analysis labels to train a neural context selector for repo-level code repair (replacing LLM-generated labels used by SWE-Pruner).

Search for competing/concurrent work that the idea may have missed. Use WebSearch for each query. Focus on:

1. Search: "neural context selection code repair 2025 2026" - any recent methods for selecting relevant code context
2. Search: "data flow analysis neural network code 2026" - anyone else combining static analysis with neural models for code
3. Search: "SWE-bench context pruning compression 2026" - other approaches to context reduction for SWE-bench
4. Search: "repository level fault localization 2026" - related localization methods
5. Search: "program analysis distillation code model 2026" - distilling program analysis into neural models
6. Search: "code repair context retrieval augmented 2026" - RAG approaches for code repair
7. Search: "tree-sitter def-use analysis training data" - anyone using tree-sitter for training data generation
8. Search: "Agentless SWE-bench 2026" OR "AutoCodeRover 2026" - check current SOTA on SWE-bench Verified

For each search, report the most relevant results found. I need to know if there's work that directly competes with or undermines the novelty of this idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "7e6144de-09d0-4d22-8e42-c322a714bf7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:05:19.146Z_

```json
{
  "parentUuid": "7e6144de-09d0-4d22-8e42-c322a714bf7d",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "476974f0-78db-4497-918e-d3b5af53d753",
  "timestamp": "2026-05-10T18:05:19.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:05:21.650Z_



I'll search for competing and concurrent work across all these dimensions. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "476974f0-78db-4497-918e-d3b5af53d753",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLAVQjBSeaWUBP78LSn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b4b1e3b-1cab-427c-8161-2ac6d0a06636",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6FNkrEiHEeVaACJgP58n2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 850,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T18:05:22.074Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013w7tLn4Y3MJzkwaTPuS85r`</summary>

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
  "parentUuid": "2b4b1e3b-1cab-427c-8161-2ac6d0a06636",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLAVQjBSeaWUBP78LSn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ced30e2-263a-4f8f-b41f-88cd2e1c1cdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6FNkrEiHEeVaACJgP58n2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 7304,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 850,
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

_source line 5 · 2026-05-10T18:05:22.078Z_

<details><summary>↩ Tool result · `toolu_013w7tLn4Y3MJzkwaTPuS85r`</summary>

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
  "parentUuid": "4ced30e2-263a-4f8f-b41f-88cd2e1c1cdb",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "db92012a-4f34-4010-9c86-1358ad87bac9",
  "sourceToolAssistantUUID": "4ced30e2-263a-4f8f-b41f-88cd2e1c1cdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:05:31.622Z_



Now let me run all 8 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db92012a-4f34-4010-9c86-1358ad87bac9",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLAi3jj4Wqff5B4kgeG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba1c8f55-bba8-4deb-ab59-fa4e7b19c294",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhFoVrdFrrTCKQhHJcJCpZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T18:05:32.158Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KDFEebhXY54ievb8FPWS5u`</summary>

```json
{
  "query": "neural context selection code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba1c8f55-bba8-4deb-ab59-fa4e7b19c294",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLAi3jj4Wqff5B4kgeG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1804fc5f-4152-4dce-8064-8034ccab6747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhFoVrdFrrTCKQhHJcJCpZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T18:05:33.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cb12xDWep5SRADkcCj7sM3`</summary>

```json
{
  "query": "data flow analysis neural network code 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1804fc5f-4152-4dce-8064-8034ccab6747",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLAi3jj4Wqff5B4kgeG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54d24b4a-905b-449f-9b42-f939d5465d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhFoVrdFrrTCKQhHJcJCpZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T18:05:33.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VPFKKCZgdnEPCYJ4PRwUFp`</summary>

```json
{
  "query": "SWE-bench context pruning compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54d24b4a-905b-449f-9b42-f939d5465d85",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLAi3jj4Wqff5B4kgeG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f58fae94-20b0-4d97-951c-ec025b5ce4b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhFoVrdFrrTCKQhHJcJCpZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T18:05:34.080Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017BRRJdzcD3wH4py5fDNbZS`</summary>

```json
{
  "query": "repository level fault localization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f58fae94-20b0-4d97-951c-ec025b5ce4b6",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLAi3jj4Wqff5B4kgeG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b06f5d40-5089-419f-80f3-9b2461180a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhFoVrdFrrTCKQhHJcJCpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 8154,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 207,
          "cache_read_input_tokens": 8154,
          "cache_creation_input_tokens": 1417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1417,
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

_source line 11 · 2026-05-10T18:05:39.810Z_

<details><summary>↩ Tool result · `toolu_01KDFEebhXY54ievb8FPWS5u`</summary>

```text
Web search results for query: "neural context selection code repair 2025 2026"

Links: [{"title":"CodeTranFix: A Neural Machine Translation Approach for Context-Aware Java Program Repair with CodeBERT","url":"https://www.mdpi.com/2076-3417/15/7/3632"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"CURE: Code-Aware Neural Machine Translation for Automatic Program Repair","url":"https://www.cs.purdue.edu/homes/lintan/publications/cure-icse21.pdf"},{"title":"Neural Program Repair: Automatic Bug Detection and Patch ...","url":"https://journalcrd.org/wp-content/uploads/9-CRD2851.pdf"},{"title":"Semantic Code Repair using Neuro-Symbolic Transformation Networks | OpenReview","url":"https://openreview.net/forum?id=r1hsJCe0Z"},{"title":"RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code","url":"https://arxiv.org/html/2509.16701v1"},{"title":"Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02383-9"},{"title":"Neural Program Repair : Systems, Challenges and Solutions Wenkang Zhong","url":"https://arxiv.org/pdf/2202.10868"},{"title":"ml4se/README.md at master · saltudelft/ml4se","url":"https://github.com/saltudelft/ml4se/blob/master/README.md"},{"title":"[2312.05356] Neuron Patching: Semantic-based Neuron-level Language Model Repair for Code Generation","url":"https://arxiv.org/abs/2312.05356"}]

Based on the web search results, here are the key findings related to neural context selection and code repair in 2025-2026:

## Recent Developments in Neural Context Selection for Code Repair

### CodeTransFix (2025)
CodeTransFix is a novel approach that combines neural machine translation (NMT) methods with code-specific large language models such as CodeBERT, learning contextual embeddings of bug-related code and integrating these representations as supplementary inputs to the Transformer model for context-aware patch generation.

### Context Selection Challenges
A key question in neural program repair is how much context is enough for these systems, as too long context may lead to performance degradation by containing codes unrelated to the bug. Most studies select the nearest MethodDeclaration-type ancestor of the buggy node as the root of contextual AST, while some approaches try to make the model learn to fix bugs within a narrower context — the least common ancestor of the buggy node and the fix node.

### RelRepair (2025)
RelRepair uses a structured retrieval strategy that optimizes queries based on buggy function context, constructs customized datasets from project codebases, and selects contextually relevant functions or code snippets to improve the accuracy of patches generated by LLMs.

### Recent Research Trends
Recent research addresses "Out of Context: How important is Local Context in Neural Program Repair?" and explores approaches like ContrastRepair for enhancing conversation-based automated program repair via contrastive test case pairs.

The field continues to advance with emphasis on more intelligent context selection mechanisms and improved neural architectures for code repair in both 2025 and 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1804fc5f-4152-4dce-8064-8034ccab6747",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "80dedafc-e998-404c-a6f5-157b9555e705",
  "sourceToolAssistantUUID": "1804fc5f-4152-4dce-8064-8034ccab6747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:05:40.196Z_

<details><summary>↩ Tool result · `toolu_01Cb12xDWep5SRADkcCj7sM3`</summary>

```text
Web search results for query: "data flow analysis neural network code 2026"

Links: [{"title":"Detecting Deep Neural Network Defects with Data Flow Analysis | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/9502413/9502428/09502453.pdf"},{"title":"DFA-Net: Data Flow Analyses Neural Network Architecture","url":"https://dl.acm.org/do/10.5281/zenodo.14670956/full/"},{"title":"Detecting Deep Neural Network Defects with Data Flow Analysis | Request PDF","url":"https://www.researchgate.net/publication/353696234_Detecting_Deep_Neural_Network_Defects_with_Data_Flow_Analysis"},{"title":"A Time Flow Neural Network for Solving Time-Varying Steady-State Maximum Flow Problem | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21168-2_21"},{"title":"Data Flow and Distributed Deep Neural Network based low latency IoT-Edge computation model for big data environment - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197620301780"},{"title":"Detecting Deep Neural Network Defects with Data Flow ...","url":"https://arxiv.org/pdf/1909.02190"},{"title":"DFA-Net: A Compiler-Specific Neural Architecture for Robust Generalization in Data Flow Analyses (CC 2025 - Main Conference) - CC 2025","url":"https://conf.researchr.org/details/CC-2025/CC-2025-main-conference/9/DFA-Net-A-Compiler-Specific-Neural-Architecture-for-Robust-Generalization-in-Data-Fl"},{"title":"Neural network architecture and data flow . | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Neural-network-architecture-and-data-flow_fig1_46190489"},{"title":"[1909.02190] Detecting Deep Neural Network Defects with Data Flow Analysis","url":"https://arxiv.org/abs/1909.02190"},{"title":"Types of Neural Networks - GeeksforGeeks","url":"https://www.geeksforgeeks.org/deep-learning/types-of-neural-networks/"}]

I found several relevant results for your search query about data flow analysis neural network code in 2026. Here's what I discovered:

## Key Research Areas

**DFA-Net: Compiler-Specific Neural Architecture**
DFA-Net is a neural network architecture tailored for compilers that systematically generalizes, emulating the reasoning process of compilers to facilitate the generalization of data flow analyses from simple to complex programs. The architecture decomposes data flow analyses into specialized neural networks for initialization, transfer, and meet operations, explicitly incorporating compiler-specific knowledge into the model design. DFA-Net demonstrates superior performance over traditional GNNs in data flow analysis, achieving F1 scores of 0.761 versus 0.009 for data dependencies.

**Detecting DNN Defects**
Internal data flow footprints of a DNN model can provide insights to locate the root cause of defects effectively. This approach helps developers identify whether low precision in neural network models is due to inevitable probabilistic limitations or actual design defects.

**Distributed Deep Neural Networks**
Research is focused on the integration of data flow and distributed deep learning in the IoT-Edge environment, with a novel Data Flow and Distributed Deep Neural Network (DF-DDNN) based IoT-Edge model proposed for big data environments.

These developments show active research in applying data flow analysis techniques to neural network development, testing, and optimization in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54d24b4a-905b-449f-9b42-f939d5465d85",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "72aeeeeb-02cf-4227-9ee3-fb369c4c3160",
  "sourceToolAssistantUUID": "54d24b4a-905b-449f-9b42-f939d5465d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:05:40.382Z_

<details><summary>↩ Tool result · `toolu_01VPFKKCZgdnEPCYJ4PRwUFp`</summary>

```text
Web search results for query: "SWE-bench context pruning compression 2026"

Links: [{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746"},{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"},{"title":"(PDF) SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.researchgate.net/publication/400071923_SWE-Pruner_Self-Adaptive_Context_Pruning_for_Coding_Agents"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"}]

Based on the search results, here's what I found about SWE-bench context pruning compression in 2026:

## SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents

SWE-Pruner is a self-adaptive context pruning framework tailored for coding agents. This is a recent research paper published in early 2026.

### Key Performance Results

SWE-Pruner achieves 23-54% token reduction on agent tasks like SWE-Bench Verified and up to 14.84× compression on single-turn tasks like LongCodeQA with minimal performance impact.

### How It Works

Drawing inspiration from how human programmers "selectively skim" source code during development and debugging, SWE-Pruner performs task-aware adaptive pruning for long contexts. Given the current task, the agent formulates an explicit goal (e.g., "focus on error handling") as a hint to guide the pruning targets. A lightweight neural skimmer (0.6B parameters) is trained to dynamically select relevant lines from the surrounding context given the goal.

### Benchmarks and Evaluation

For multi-turn agent tasks, SWE-Pruner was evaluated on SWE-Bench Verified (500 real-world GitHub issues requiring patch generation) and SWE-QA, integrated into Mini SWE Agent and OpenHands with Claude Sonnet 4.5 and GLM-4.6 backbone models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f58fae94-20b0-4d97-951c-ec025b5ce4b6",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "a7550017-3970-4f47-aee5-61519e294f54",
  "sourceToolAssistantUUID": "f58fae94-20b0-4d97-951c-ec025b5ce4b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:05:42.254Z_

<details><summary>↩ Tool result · `toolu_017BRRJdzcD3wH4py5fDNbZS`</summary>

```text
Web search results for query: "repository level fault localization 2026"

Links: [{"title":"LLM4FL: Multi-Agent Repository-Level Software Fault Localization via Graph-Based Retrieval and Iterative Refinement | OpenReview","url":"https://openreview.net/forum?id=z91EvZbSI1"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167v1"},{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale","url":"https://arxiv.org/pdf/2604.00167"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044v1"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3660771"},{"title":"Reformulate, Retrieve, Localize: Agents for Repository-Level Bug Localization","url":"https://arxiv.org/html/2512.07022"},{"title":"Explainable Fault Localization for Programming ...","url":"https://arxiv.org/pdf/2509.25676"}]

I've performed the web search for "repository level fault localization 2026". Here are the key findings:

## Recent Research on Repository-Level Fault Localization (2026)

Several important papers and projects have emerged in 2026 focusing on repository-level fault localization:

### Multi-Agent and LLM-Based Approaches

LLM4FL is a multi-LLM-agent-based fault localization approach that addresses challenges with large-scale projects. The system uses graph-based retrieval to identify failure reasons and rank suspicious methods in the codebase, followed by a Reviewer Agent that re-evaluates and re-ranks buggy methods using verbal reinforcement learning and self-criticism. Evaluated on the Defects4J benchmark, LLM4FL outperforms AutoFL by 18.55% in Top-1 accuracy and surpasses supervised methods like DeepFL and Grace, all without task-specific training.

### Fault Localization Granularity Studies

Fault localization approaches vary in terms of granularity of localization, with some frameworks identifying specific methods or functions responsible for an issue, while others narrow down to specific code lines or segments of lines. A study on repository-scale code repair shows that function-level granularity yields the highest repair rate against line-level and file-level.

### Advanced Localization Methods

A novel project-level fault localization approach improves both file- and element-level localization, introducing a hierarchical reasoning module that generates structured, bug-specific explanations for candidate files and elements, and leverages these explanations in a two-stage ranking scheme.

### Robustness Evaluation

The first large-scale empirical investigation into the robustness of LLMs' fault localizability has been presented, developing an end-to-end evaluation framework that addresses limitations in current LLM evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b06f5d40-5089-419f-80f3-9b2461180a24",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "65d06b17-c1ab-4047-8e95-210737611d76",
  "sourceToolAssistantUUID": "b06f5d40-5089-419f-80f3-9b2461180a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T18:05:45.085Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017Hfwp8yfp9NayZpkVBgq2q`</summary>

```json
{
  "query": "program analysis distillation code model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65d06b17-c1ab-4047-8e95-210737611d76",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLCC3WHJ3fsUz1vhDVx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7984f137-09b7-4ef1-9338-e0c333774146",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Ge5UEXDVr2QuLoZVmUwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3950,
      "cache_read_input_tokens": 9571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3950,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-10T18:05:45.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E8Nx9vnuxr321JRkyeuCD2`</summary>

```json
{
  "query": "code repair context retrieval augmented 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7984f137-09b7-4ef1-9338-e0c333774146",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLCC3WHJ3fsUz1vhDVx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "753b5341-dd26-4afd-9e84-a6f11512dc3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Ge5UEXDVr2QuLoZVmUwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3950,
      "cache_read_input_tokens": 9571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3950,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T18:05:46.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012p64wGKN449bg7S6xhQACn`</summary>

```json
{
  "query": "tree-sitter def-use analysis training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "753b5341-dd26-4afd-9e84-a6f11512dc3b",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLCC3WHJ3fsUz1vhDVx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24f62a8c-57fd-4362-bf74-f34e15a9f969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Ge5UEXDVr2QuLoZVmUwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3950,
      "cache_read_input_tokens": 9571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3950,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T18:05:47.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012m6zQoLivXfD7rETJgZgMX`</summary>

```json
{
  "query": "Agentless SWE-bench 2026 OR AutoCodeRover 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24f62a8c-57fd-4362-bf74-f34e15a9f969",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLCC3WHJ3fsUz1vhDVx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10553696-5114-450b-8fb2-6586257adfd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129Ge5UEXDVr2QuLoZVmUwe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3950,
      "cache_read_input_tokens": 9571,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 9571,
          "cache_creation_input_tokens": 3950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3950,
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

_source line 19 · 2026-05-10T18:05:52.211Z_

<details><summary>↩ Tool result · `toolu_012p64wGKN449bg7S6xhQACn`</summary>

```text
Web search results for query: "tree-sitter def-use analysis training data"

Links: [{"title":"5 Powerful Ways to Use Tree-sitter in Your Next Project | by Istiaq Ahmed Fahad | Medium","url":"https://medium.com/@ahmedfahad04/5-powerful-ways-to-use-tree-sitter-in-your-next-project-50e17c1f7055"},{"title":"A Beginner's Guide to Tree-sitter - DEV Community","url":"https://dev.to/shreshthgoyal/understanding-code-structure-a-beginners-guide-to-tree-sitter-3bbc"},{"title":"Semantic Code Indexing with AST and Tree-sitter for AI Agents (Part — 1 of 3) | by Dineshkumar | Medium","url":"https://medium.com/@email2dineshkuppan/semantic-code-indexing-with-ast-and-tree-sitter-for-ai-agents-part-1-of-3-eb5237ba687a"},{"title":"Learn How to Navigate Code Structures and Extract Details Using Tree-sitter | by Rijul Rajesh T P | Medium","url":"https://medium.com/@rijulrajtkeey2/learn-how-to-navigate-code-structures-and-extract-details-using-tree-sitter-510d6d2801f1"},{"title":"Parse and analyze source codes with Tree-sitter - Lincs","url":"https://www.lincs.fr/events/parse-and-analyze-source-codes-with-tree-sitter/"},{"title":"A Beginner’s Guide to Tree-sitter | by Shreshth Goyal | Medium","url":"https://medium.com/@shreshthg30/a-beginners-guide-to-tree-sitter-6698f2696b48"},{"title":"Tree-sitter: Revolutionizing Parsing with an Incremental Parsing Library","url":"https://www.deusinmachina.net/p/tree-sitter-revolutionizing-parsing"},{"title":"Unraveling Tree-Sitter Queries: Your Guide to Code Analysis Magic - DEV Community","url":"https://dev.to/shrsv/unraveling-tree-sitter-queries-your-guide-to-code-analysis-magic-41il"},{"title":"Tips for using tree sitter queries - Cycode","url":"https://cycode.com/blog/tips-for-using-tree-sitter-queries/"},{"title":"Tree-sitter and its Query - MartinLwx's Blog","url":"https://martinlwx.github.io/en/tree-sitter-and-its-query/"}]

I've performed the web search for "tree-sitter def-use analysis training data." The search results contain information about Tree-sitter as a parsing tool and its capabilities, but they don't appear to contain specific information about def-use analysis training data.

The search results show that Tree-sitter is a parser generator and runtime for building fast, accurate parsers for programming languages, and it's commonly used for code analysis tasks. However, the results focus on Tree-sitter's general parsing and querying capabilities rather than def-use analysis or training data specifically.

The closest relevant information is that researchers have been experimenting with training LLM-powered agents using Tree-sitter for code understanding, as ASTs and Tree-sitter provide structure to raw code. Additionally, organizations like Bearer have built systems on top of Tree-sitter to extract relationships needed for classification algorithms and data type detection.

If you're looking for more specific information about def-use analysis training data with Tree-sitter, you may need to search for more specialized resources or academic papers on this topic, as the general web results don't contain detailed information about this specific combination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24f62a8c-57fd-4362-bf74-f34e15a9f969",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "a096a75a-b690-400b-ab2e-042a17bc9e00",
  "sourceToolAssistantUUID": "24f62a8c-57fd-4362-bf74-f34e15a9f969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T18:05:53.340Z_

<details><summary>↩ Tool result · `toolu_017Hfwp8yfp9NayZpkVBgq2q`</summary>

```text
Web search results for query: "program analysis distillation code model 2026"

Links: [{"title":"Paper page - Embarrassingly Simple Self-Distillation Improves Code Generation","url":"https://huggingface.co/papers/2604.01193"},{"title":"Program Translation via Code Distillation | OpenReview","url":"https://openreview.net/forum?id=L7YoWxQq5t"},{"title":"Embarrassingly Simple Self-Distillation Improves Code Generation","url":"https://arxiv.org/html/2604.01193v1"},{"title":"Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross–Language Code Clone Detection","url":"https://arxiv.org/html/2605.02860"},{"title":"An Empirical Study of Knowledge Distillation for Code Understanding Tasks","url":"https://arxiv.org/html/2508.15423v1"},{"title":"Model Distillation for LLMs: Cut Costs & Boost Speed in 2026","url":"https://redis.io/blog/model-distillation-llm-guide/"},{"title":"Reinforcement Learning via Self-Distillation","url":"https://arxiv.org/pdf/2601.20802"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Visual+Programmability"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Model Distillation — How It Works & Why It Matters- Openxcell","url":"https://www.openxcell.com/blog/model-distillation/"}]

Based on the search results, here's what I found about program analysis distillation and code models in 2026:

## Key Research Areas

**Self-Distillation for Code Generation:**
Simple self-distillation (SSD) improves code generation by sampling solutions from the model with certain temperature and truncation configurations, then fine-tuning on those samples with standard supervised fine-tuning. SSD improves Qwen3-30B-Instruct from 42.4% to 55.3% pass@1 on LiveCodeBench v6, with gains concentrating on harder problems, and it generalizes across Qwen and Llama models at 4B, 8B, and 30B scale.

**Code Distillation for Program Translation:**
Code Distillation (CoDist) captures the semantic and structural equivalence of code in a language agnostic intermediate representation, serving as a translation pivot for any programming language and scaling to all available source code.

**Knowledge Distillation for Code Understanding:**
Knowledge distillation demonstrates consistent effectiveness across different configurations, with distilled models maintaining comparable performance to teachers while outperforming standard fine-tuned models, and feature-based distillation methods outperform logit-based approaches across code understanding tasks.

**Cross-Language Code Clone Detection:**
A knowledge distillation framework transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for cross-language code clone detection, using cross-language code pairs derived from Project CodeNet.

These developments show that distillation techniques are central to improving code models' efficiency and performance in 2026, particularly for enabling smaller models to maintain capability while reducing computational requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7984f137-09b7-4ef1-9338-e0c333774146",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "ffd598cb-ff23-4feb-ba42-59b943745348",
  "sourceToolAssistantUUID": "7984f137-09b7-4ef1-9338-e0c333774146",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:05:53.632Z_

<details><summary>↩ Tool result · `toolu_01E8Nx9vnuxr321JRkyeuCD2`</summary>

```text
Web search results for query: "code repair context retrieval augmented 2026"

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"SCPatcher: Automated Smart Contract Code Repair via Retrieval-Augmented Generation and Knowledge Graph","url":"https://arxiv.org/html/2604.00687v1"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained","url":"https://arxiv.org/pdf/2509.02330"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"[2504.20434] ARCS: Agentic Retrieval-Augmented Code Synthesis with Iterative Refinement","url":"https://arxiv.org/abs/2504.20434"},{"title":"Retrieval-augmented code completion for local projects using large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957417425022158"},{"title":"RESCUE: Retrieval Augmented Secure Code Generation | OpenReview","url":"https://openreview.net/forum?id=gbxhesw4UH"}]

The search results reveal significant research activity in 2025-2026 on retrieval-augmented generation (RAG) for code repair and code generation. Here are the key findings:

## Overview of Retrieval-Augmented Code Repair in 2026

Retrieval-Augmented Code Generation is an emerging paradigm that enhances large language models with external software knowledge through retrieval mechanisms. Tasks such as bug localization and fixing and automatic program repair are important applications of retrieval-augmented code generation.

## Recent Approaches and Methods

Several innovative systems have emerged recently:

**ReCode (2025)**: ReCode is a retrieval-augmented generation method that integrates algorithm-aware categorization and modular modeling to enable effective code repair with a fine-grained retrieval-augmented in-context learning framework. Conventional retrieval strategies often based on holistic code-text embeddings fail to capture the structural intricacies of code, resulting in suboptimal retrieval quality.

**ARCS (2025)**: Agentic Retrieval-Augmented Code Synthesis (ARCS) is a system that improves LLM-based code generation without fine-tuning by operating through a budgeted synthesize-execute-repair loop that retrieves relevant code context before generation, proposes candidates, executes them against tests, and repairs based on execution feedback.

**SCPatcher (2026)**: Knowledge graph-based RAG leverages semantic networks of entities and relationships, and for code repair, this provides fact-checked, logically structured knowledge that reduces hallucination risks and enables more reliable vulnerability patching.

## Context Retrieval Strategies

Recent works broaden the retrieval space to include behavioral traces, vulnerability records, human feedback, and external web resources, which improves task-specific performance in code repair, security, and third-party library usage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "753b5341-dd26-4afd-9e84-a6f11512dc3b",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "e8975c5e-d130-468b-bc8e-8ecca90722f4",
  "sourceToolAssistantUUID": "753b5341-dd26-4afd-9e84-a6f11512dc3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T18:05:54.111Z_

<details><summary>↩ Tool result · `toolu_012m6zQoLivXfD7rETJgZgMX`</summary>

```text
Web search results for query: "Agentless SWE-bench 2026 OR AutoCodeRover 2026"

Links: [{"title":"SWE-Bench Coding Agent Leaderboard 2026: Claude vs GPT | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/"},{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints","url":"https://arxiv.org/html/2509.09853"},{"title":"SWE-bench Leaderboard: AI Coding Agent SOTA Results | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/browse/agentic/swe-bench"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"Unified Software Engineering Agent as AI Software Engineer Leonhard Applis∗","url":"https://abhikrc.com/pdf/ICSE26-USEagent.pdf"},{"title":"GitHub - OpenAutoCoder/Agentless: Agentless🐱: an agentless approach to automatically solve software development problems","url":"https://github.com/OpenAutoCoder/Agentless"}]

Based on the search results, here's what I found about Agentless and AutoCodeRover in the context of SWE-bench in 2026:

## Agentless in 2026

Agentless rankings on SWE-Bench Verified have been updated as of April 2026. The Agentless approach is a deliberate counter-example with no tool calls, no iterative repair, just a structured three-stage pipeline (localization, repair, validation) that makes one shot at the patch.

Recent performance data shows Agentless leads all SWE scaffolds in resolution rate (48% with Qwen3-32B), but at the cost of significant computation: it consumes an average of 83.1 API calls, 209.4 seconds of inference time, and 727.9 seconds of CPU time.

## AutoCodeRover in 2026

AutoCodeRover, a simpler SWE scaffold, consistently delivers competitive performance. With Qwen3-32B, it achieves a 38% resolution rate using only 14.7 API calls and 55.5K input tokens—far more efficient than its peers.

AutoCodeRover has been acquired by an established company, Sonar, in February 2025.

## Key Comparison

Both approaches represent different design philosophies: Agentless-1.5 achieved 50.8% and SWE-Agent achieved 66%, both developed by single academic teams, with these systems showing competitive though not top-ranking results compared to industry submissions in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10553696-5114-450b-8fb2-6586257adfd2",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "d2822f01-23cb-4fee-b012-6b345572508b",
  "sourceToolAssistantUUID": "10553696-5114-450b-8fb2-6586257adfd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T18:05:58.330Z_

Now let me do a few more targeted searches to fill in gaps, particularly around the most directly competing ideas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2822f01-23cb-4fee-b012-6b345572508b",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLD4nDxzXtLBhnkWRS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4bc02b2-8205-45d4-bf36-211cafaf1b50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZinr2sXdZvHyHgzXQcEaM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3958,
      "cache_read_input_tokens": 13521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3958,
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

_source line 24 · 2026-05-10T18:05:59.149Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GGRxUqpQGoTRBCFLh9BZ8M`</summary>

```json
{
  "query": "SWE-Pruner neural skimmer training labels static analysis replacement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4bc02b2-8205-45d4-bf36-211cafaf1b50",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLD4nDxzXtLBhnkWRS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3feb6c54-c262-40e6-b750-b235b44f154b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZinr2sXdZvHyHgzXQcEaM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3958,
      "cache_read_input_tokens": 13521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3958,
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

_source line 25 · 2026-05-10T18:06:00.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EkXm9VDiEFrjtekALJbHQT`</summary>

```json
{
  "query": "learning code context selection from program analysis labels 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3feb6c54-c262-40e6-b750-b235b44f154b",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLD4nDxzXtLBhnkWRS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e70913f3-076e-43ae-85d0-81fc9fe3f493",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZinr2sXdZvHyHgzXQcEaM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3958,
      "cache_read_input_tokens": 13521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3958,
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

_source line 26 · 2026-05-10T18:06:01.284Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LahZE6AUMjid8VBgsEnNTU`</summary>

```json
{
  "query": "DFA-Net data flow analysis neural network CC 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e70913f3-076e-43ae-85d0-81fc9fe3f493",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLD4nDxzXtLBhnkWRS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88c5c63d-976e-477c-ab7a-63834aa145c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZinr2sXdZvHyHgzXQcEaM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3958,
      "cache_read_input_tokens": 13521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3958,
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

_source line 27 · 2026-05-10T18:06:05.511Z_

<details><summary>↩ Tool result · `toolu_01GGRxUqpQGoTRBCFLh9BZ8M`</summary>

```text
Web search results for query: "SWE-Pruner neural skimmer training labels static analysis replacement"

Links: [{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/html/2601.16746v1"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"Paper page - SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://huggingface.co/papers/2601.16746"},{"title":"GitHub - Ayanami1314/swe-pruner · GitHub","url":"https://github.com/Ayanami1314/swe-pruner"},{"title":"(PDF) SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.researchgate.net/publication/400071923_SWE-Pruner_Self-Adaptive_Context_Pruning_for_Coding_Agents"},{"title":"[2601.16746] SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://arxiv.org/abs/2601.16746"},{"title":"ayanami-kitasan/code-pruner · Hugging Face","url":"https://huggingface.co/ayanami-kitasan/code-pruner"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.16746v1"},{"title":"@YerbaPage on Hugging Face: \"🔥 SWE-Pruner can save up to 40% of your Claude Code cost without sacrificing…\"","url":"https://huggingface.co/posts/YerbaPage/493697712808947"},{"title":"piwheels - swe-pruner","url":"https://www.piwheels.org/project/swe-pruner/"}]

Based on the search results, here's what I found about SWE-Pruner:

## Overview

SWE-Pruner is a framework that prunes long code contexts for agents through task-aware, adaptive filtering. Drawing inspiration from how human programmers "selectively skim" source code during development and debugging, SWE-Pruner performs task-aware adaptive pruning for long contexts.

## Neural Skimmer

A lightweight neural skimmer (0.6B parameters) is trained to dynamically select relevant lines from the surrounding context given the goal. The neural skimmer extends the Qwen3-Reranker-0.6B backbone with two specialized heads: a CRF-based pruning head for line-level filtering and a reranking head for document-level scoring.

## Training Data

Regarding training labels, training the neural skimmer requires data with line-level supervision that preserves both relevance and code structure. The paper mentions using "silver labels" for training the pruning head, though specific details about how these labels are generated (such as via static analysis or other methods) are referenced in the mathematical formulation but not detailed in the accessible excerpts.

## Performance

SWE-Pruner reduces token usage by 23–38% on SWE-Bench and 29–54% on SWE-QA, and achieves up to 14.84× compression on single-turn benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3feb6c54-c262-40e6-b750-b235b44f154b",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "800366e8-c1ca-48fb-9704-7e6e1521b70f",
  "sourceToolAssistantUUID": "3feb6c54-c262-40e6-b750-b235b44f154b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T18:06:05.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BsWHY4kPHu3dPrL4odJDMJ`</summary>

```json
{
  "query": "SWE-bench Verified leaderboard 2026 top results state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "800366e8-c1ca-48fb-9704-7e6e1521b70f",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLD4nDxzXtLBhnkWRS1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f76f982-34b3-4fa8-bbf7-57cebb4545e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZinr2sXdZvHyHgzXQcEaM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3958,
      "cache_read_input_tokens": 13521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3958,
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

_source line 29 · 2026-05-10T18:06:07.303Z_

<details><summary>↩ Tool result · `toolu_01LahZE6AUMjid8VBgsEnNTU`</summary>

```text
Web search results for query: "DFA-Net data flow analysis neural network CC 2025"

Links: [{"title":"DFA-Net: A Compiler-Specific Neural Architecture for Robust Generalization in Data Flow Analyses (CC 2025 - Main Conference) - CC 2025","url":"https://conf.researchr.org/details/CC-2025/CC-2025-main-conference/9/DFA-Net-A-Compiler-Specific-Neural-Architecture-for-Robust-Generalization-in-Data-Fl"},{"title":"DFA-Net: Data Flow Analyses Neural Network Architecture","url":"https://dl.acm.org/do/10.5281/zenodo.14670956/full/"},{"title":"DFA-Net: A Compiler-Specific Neural Architecture for Robust Generalization in Data Flow Analyses | Proceedings of the 34th ACM SIGPLAN International Conference on Compiler Construction","url":"https://dl.acm.org/doi/abs/10.1145/3708493.3712687"},{"title":"DFA-Net: Data Flow Analyses Neural Network Architecture","url":"https://zenodo.org/records/14670956"},{"title":"DFA-Net: A Compiler-Specific Neural Architecture for ...","url":"https://dl.acm.org/doi/pdf/10.1145/3708493.3712687"},{"title":"CC 2025 – Proceedings - Conference Publishing","url":"https://www.conference-publishing.com/toc/CC25/noabs"},{"title":"DFA-Net: A Compiler-Specific Neural Architecture for Robust ...","url":"https://cfaed.tu-dresden.de/files/Images/people/chair-cc/publications/2503_Brauckmann_CC.pdf"},{"title":"cfaed Publications - TU Dresden","url":"https://cfaed.tu-dresden.de/publications?pubId=3804"},{"title":"DFA-Net: A Compiler-Specific Neural Architecture for Robust Generalization in Data Flow Analyses | Request PDF","url":"https://www.researchgate.net/publication/389346513_DFA-Net_A_Compiler-Specific_Neural_Architecture_for_Robust_Generalization_in_Data_Flow_Analyses"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=DFA-Net:+A+Compiler-Specific+Neural+Architecture+for+Robust+Generalization+in+Data+Flow+Analyses."}]

Based on the search results, here's information about DFA-Net:

## Overview

DFA-Net is a neural network architecture tailored for compilers that systematically generalizes, emulating the reasoning process of compilers to facilitate the generalization of data flow analyses from simple to complex programs.

## Architecture Design

The architecture decomposes data flow analyses into specialized neural networks for initialization, transfer, and meet operations, explicitly incorporating compiler-specific knowledge into the model design.

## Motivation and Problem

Data flow analysis is fundamental to modern program optimization and verification, serving as a critical foundation for compiler transformations. As machine learning increasingly drives compiler tasks, the need for models that can implicitly understand and correctly reason about data flow properties becomes crucial for maintaining soundness. State-of-the-art machine learning methods, especially graph neural networks (GNNs), face challenges in generalizing beyond training scenarios due to their limited ability to perform large propagations.

## Performance

DFA-Net demonstrates superior performance over traditional GNNs in data flow analysis, achieving F1 scores of 0.761 versus 0.009 for data dependencies and 0.989 versus 0.196 for dominators at high complexity levels, while maintaining perfect scores for liveness and reachability analyses where GNNs struggle significantly.

## Publication

The paper was presented at the 34th ACM SIGPLAN International Conference on Compiler Construction (CC '25), March 1–2, 2025, Las Vegas, NV, USA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88c5c63d-976e-477c-ab7a-63834aa145c6",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "0abeb688-0cc8-4227-87df-384427037b75",
  "sourceToolAssistantUUID": "88c5c63d-976e-477c-ab7a-63834aa145c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T18:06:13.293Z_

<details><summary>↩ Tool result · `toolu_01BsWHY4kPHu3dPrL4odJDMJ`</summary>

```text
Web search results for query: "SWE-bench Verified leaderboard 2026 top results state of the art"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"SWE-bench Lite Leaderboard 2026 - Compare AI Model Scores","url":"https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite"}]

Based on the latest 2026 SWE-bench Verified leaderboard results, here are the top performers and state-of-the-art findings:

## Top Results (May 2026)

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Verified leaderboard with 93.9%, followed by Claude Opus 4.7 (Adaptive) (87.6%) and GPT-5.3 Codex (85%).

## Important Context on Verified Benchmark Limitations

While these scores are impressive on SWE-bench Verified, there's significant debate about the benchmark's validity as a true measure of capability. OpenAI stopped reporting Verified scores in early 2026 and now recommends SWE-bench Pro instead.

The reason is substantial: Claude Opus 4.5 scores 80.9% on SWE-bench Verified while the same model, on SWE-bench Pro, using standardised scaffolding on tasks it could not have seen during training, scores 45.9%. OpenAI's internal audit found that every major frontier model, GPT-5.2, Claude Opus 4.5, Gemini 3 Flash, could reproduce verbatim gold patches for some SWE-bench Verified tasks.

## Emerging Standard: SWE-bench Pro

The benchmark is significantly more challenging than its predecessors; top models score around 23% on the SWE-Bench Pro public set, compared to 70%+ on SWE-Bench Verified, providing a more accurate measure of an agent's true problem-solving capabilities in environments that mirror professional software development.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f76f982-34b3-4fa8-bbf7-57cebb4545e5",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "6c3b1641-cf65-4db2-a70e-a85cd5156e8e",
  "sourceToolAssistantUUID": "6f76f982-34b3-4fa8-bbf7-57cebb4545e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T18:06:17.495Z_

<details><summary>↩ Tool result · `toolu_01EkXm9VDiEFrjtekALJbHQT`</summary>

```text
Web search results for query: "learning code context selection from program analysis labels 2025 2026"

Links: [{"title":"Large Language Model-Aware In-Context Learning for Code Generation | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3715908"},{"title":"Learning Generalizable Multimodal Representations for Software Vulnerability Detection","url":"https://arxiv.org/html/2604.25711v1"},{"title":"Learning to Focus: Context Extraction for Efficient Code Vulnerability Detection with Language Models","url":"https://arxiv.org/html/2505.17460v1"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Modeling Student Learning with 3.8 Million Program Traces","url":"https://arxiv.org/html/2510.05056v2"},{"title":"GitHub - codefuse-ai/Awesome-Code-LLM: [TMLR] A curated list of language modeling researches for code (and other software engineering activities), plus related datasets. · GitHub","url":"https://github.com/codefuse-ai/awesome-code-llm"},{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding Jared Zhu","url":"https://www.arxiv.org/pdf/2602.08316"},{"title":"AwesomeLLM4SE/README.md at main · iSEngLab/AwesomeLLM4SE","url":"https://github.com/iSEngLab/AwesomeLLM4SE/blob/main/README.md"},{"title":"Think Anywhere in Code Generation","url":"https://arxiv.org/html/2603.29957v3"}]

I found several relevant research papers and resources related to your query. Here are the key findings:

## Recent Research on Code Context Selection and Learning

A recent study proposes LAIL (Large language model-Aware selection approach for In-context-Learning-based code generation), which uses LLMs themselves to select examples and trains a model-aware retriever to learn the preference of LLMs. The approach requires LLMs to label candidate examples as positive or negative, where positive examples are helpful for implementing requirements while negative examples should be ignored.

## Context Selection for Code Vulnerability Detection

Research on code vulnerability detection addresses challenges with uncertain vulnerability location, as language models operate under strict input length constraints, and truncating long functions may omit vulnerable regions or retain irrelevant code. A paper titled "Learning to Focus: Context Extraction for Efficient Code Vulnerability Detection with Language Models" (May 2025) explores context extraction techniques for this purpose.

## Program Analysis and Code Understanding

Recent work on code completion includes GraphCoder (2025), which enhances repository-level code completion via code context graph-based retrieval, and STALL+ (2024), which boosts LLM-based repository-level code completion with static analysis.

## Related Resources

A comprehensive survey titled "A Survey on Large Language Models for Software Engineering" was published in Science China Information Sciences in 2026, which covers various aspects of LLMs for code-related tasks.

These resources address the intersection of learning code context selection, program analysis, and label-based approaches for improving code generation and understanding tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e70913f3-076e-43ae-85d0-81fc9fe3f493",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "f5b06811-b734-4cb9-a190-106bb349d023",
  "sourceToolAssistantUUID": "e70913f3-076e-43ae-85d0-81fc9fe3f493",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T18:06:20.790Z_

Let me do a couple more targeted searches on the most directly relevant angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5b06811-b734-4cb9-a190-106bb349d023",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLEnpLc3LV4WmgFmL76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b72fe30-0954-4090-9742-6bd50235f942",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UvV7ws7dG83jG1Bd7RS4oV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1835,
      "cache_creation_input_tokens": 2038,
      "cache_read_input_tokens": 17479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2038,
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

_source line 33 · 2026-05-10T18:06:21.800Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GB9y9vYCZVjq5vw6DRiZdd`</summary>

```json
{
  "query": "\"Learning to Focus\" context extraction vulnerability detection code slicing 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b72fe30-0954-4090-9742-6bd50235f942",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLEnpLc3LV4WmgFmL76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a36b48e-65f1-473c-b75b-6de693aefb69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UvV7ws7dG83jG1Bd7RS4oV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1835,
      "cache_creation_input_tokens": 2038,
      "cache_read_input_tokens": 17479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2038,
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

_source line 34 · 2026-05-10T18:06:22.800Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SffPbFmwesTPVMtY4MK3TZ`</summary>

```json
{
  "query": "STALL static analysis LLM code completion repository level 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a36b48e-65f1-473c-b75b-6de693aefb69",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLEnpLc3LV4WmgFmL76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4696b17c-7884-4e8e-8785-95c6c8692313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UvV7ws7dG83jG1Bd7RS4oV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1835,
      "cache_creation_input_tokens": 2038,
      "cache_read_input_tokens": 17479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2038,
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

_source line 35 · 2026-05-10T18:06:23.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011DNZTcqHgMGiFWpGgdVAb4`</summary>

```json
{
  "query": "fault localization granularity repository scale code repair 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4696b17c-7884-4e8e-8785-95c6c8692313",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLEnpLc3LV4WmgFmL76",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fec6cc9-8d7e-46ca-bca6-8b801ed99b15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UvV7ws7dG83jG1Bd7RS4oV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1835,
      "cache_creation_input_tokens": 2038,
      "cache_read_input_tokens": 17479,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2038
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1835,
          "output_tokens": 184,
          "cache_read_input_tokens": 17479,
          "cache_creation_input_tokens": 2038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2038,
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

_source line 36 · 2026-05-10T18:06:28.871Z_

<details><summary>↩ Tool result · `toolu_01SffPbFmwesTPVMtY4MK3TZ`</summary>

```text
Web search results for query: "STALL static analysis LLM code completion repository level 2024 2025"

Links: [{"title":"STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis","url":"https://arxiv.org/html/2406.10018v1"},{"title":"[2406.10018] STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis","url":"https://arxiv.org/abs/2406.10018"},{"title":"STALL+: Boosting LLM-based Repository-level Code Completion","url":"https://mingwei-liu.github.io/assets/pdf/arxiv2024STALL.pdf"},{"title":"(PDF) STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis","url":"https://www.researchgate.net/publication/381470887_STALL_Boosting_LLM-based_Repository-level_Code_Completion_with_Static_Analysis"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Combining Large Language Models with Static Analyzers for Code Review Generation The replication package is available at https://github.com/ImenJaoua/Hybrid-Code-Review and the data is available at https://zenodo.org/records/14061110.","url":"https://arxiv.org/html/2502.06633v1"},{"title":"STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis | alphaXiv","url":"https://www.alphaxiv.org/abs/2406.10018"},{"title":"Overview of the STALL + static analysis integration framework | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Overview-of-the-STALL-static-analysis-integration-framework_fig1_381470887"},{"title":"Awesome-Repo-Level-Code-Generation/README.md at main · YerbaPage/Awesome-Repo-Level-Code-Generation","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation/blob/main/README.md"}]

Based on the search results, I found comprehensive information about STALL+:

## STALL+: Boosting LLM-based Repository-level Code Completion with Static Analysis

This work performs the first study on the static analysis integration in LLM-based repository-level code completion by investigating both the effectiveness and efficiency of static analysis integration strategies across different phases of code completion.

### Framework Overview

The STALL+ framework supports an extendable and customizable integration of multiple static analysis strategies into the complete pipeline of LLM-based repository-level code completion, and extensive experiments were performed by including different code LLMs on the latest repository-level code completion benchmark CrossCodeEval.

### Key Findings

Integrating file-level dependencies in prompting phase performs the best while the integration in post-processing phase performs the worse.

Different improvements from static analysis are observed between dynamic languages and static languages, i.e., the best combination is prompting-phase with decoding-phase integration for Java while the best combination is prompting-phase with post-processing-phase integration for Python given the limitations of statically analyzing dynamic languages.

### Publication Date

The research was published in June 2024 as an arXiv paper (arXiv:2406.10018) and has been cited in subsequent research on repository-level code completion through 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4696b17c-7884-4e8e-8785-95c6c8692313",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "dcfbd286-1a7d-4299-b5cd-9b8e7508bf46",
  "sourceToolAssistantUUID": "4696b17c-7884-4e8e-8785-95c6c8692313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T18:06:29.390Z_

<details><summary>↩ Tool result · `toolu_01GB9y9vYCZVjq5vw6DRiZdd`</summary>

```text
Web search results for query: ""Learning to Focus" context extraction vulnerability detection code slicing 2025"

Links: [{"title":"Learning to Focus: Context Extraction for Efficient Code Vulnerability Detection with Language Models","url":"https://arxiv.org/html/2505.17460v1"},{"title":"Learning to Focus: Context Extraction for Efficient Code Vulnerability","url":"https://www.arxiv.org/pdf/2505.17460v1"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through ...","url":"https://www.usenix.org/system/files/usenixsecurity25-lekssays.pdf"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through Code Property","url":"https://arxiv.org/pdf/2507.16585"},{"title":"Awesome-LLMs-for-Vulnerability-Detection/README.md at main · huhusmang/Awesome-LLMs-for-Vulnerability-Detection","url":"https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection/blob/main/README.md"},{"title":"GitHub - huhusmang/Awesome-LLMs-for-Vulnerability-Detection: Awesome Large Language Models for Vulnerability Detection · GitHub","url":"https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection"},{"title":"Context and Multi-Features-Based Vulnerability Detection: A Vulnerability Detection Frame Based on Context Slicing and Multi-Features","url":"https://www.mdpi.com/1424-8220/24/5/1351"},{"title":"Context-Enhanced Vulnerability Detection Based on Large Language Model","url":"https://arxiv.org/html/2504.16877v1"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models","url":"https://arxiv.org/html/2507.16585v1"},{"title":"On the effects of program slicing for vulnerability detection during code inspection - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11972194/"}]

Based on the search results, I found relevant information about "Learning to Focus: Context Extraction for Efficient Code Vulnerability Detection with Language Models," a 2025 research paper.

## Overview

The paper addresses vulnerability detection using language models, with recent work using execution traces to manually identify key endpoints for more execution-aware context modeling.

## Key Problem and Approach

The research addresses challenges where language models operate under strict input length constraints, and truncating long functions may omit vulnerable regions or retain irrelevant code. Prior work adopted static slicing (data/control dependencies) to extract semantically relevant regions, typically guided by syntax cues like special identifiers or pointer usage.

## Context Extraction Methods

Earlier approaches extracted code gadgets around predefined anchors such as APIs or pointer operations. Other methods rely on CWE-guided heuristics to locate vulnerability-relevant regions.

The paper appears to contribute a novel approach to learning how to focus on the most relevant code context for vulnerability detection, moving beyond handcrafted heuristics and static analysis techniques to create more efficient and generalizable vulnerability detection with language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a36b48e-65f1-473c-b75b-6de693aefb69",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "af58360f-3341-47c6-bb75-3ccac812b3b4",
  "sourceToolAssistantUUID": "6a36b48e-65f1-473c-b75b-6de693aefb69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T18:06:32.928Z_

<details><summary>↩ Tool result · `toolu_011DNZTcqHgMGiFWpGgdVAb4`</summary>

```text
Web search results for query: "fault localization granularity repository scale code repair 2026 arxiv"

Links: [{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale","url":"https://arxiv.org/pdf/2604.00167"},{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260118044S/abstract"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"[2601.18044] RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/abs/2601.18044"}]

I found several relevant papers on arXiv from 2026 related to fault localization granularity and repository-scale code repair:

## Key Papers Found:

**1. "A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks"** (arXiv:2604.00167)

This paper addresses automatic program repair at repository-level, which involves fault localization and code repair, where fault localization approaches vary in terms of granularity of localization. No repository-scale studies had previously explicitly investigated granularity under the assumption of perfect fault localization. The study found that function-level granularity yields the highest repair rate against line-level and file-level, though the ideal granularity may be task dependent.

**2. "On the Role of Fault Localization Context for LLM-Based Program Repair"** (arXiv:2604.05481)

This study found that more context does not consistently improve repair performance, with file-level localization being the dominant factor yielding a 15-17x improvement over a no-file baseline.

**3. "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"** (arXiv:2605.03117)

ARISE augments an autonomous agent with specialized tools designed to navigate large-scale repositories by representing codebases as multi-granularity program graphs.

**4. "RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models"** (arXiv:2601.18044)

This paper addresses how fault localization is critical for APR with LLM-based agents, with accurate FL being essential for effective repair in project-level scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fec6cc9-8d7e-46ca-bca6-8b801ed99b15",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "575d2686-763f-4669-9150-9ec5aa9423e1",
  "sourceToolAssistantUUID": "7fec6cc9-8d7e-46ca-bca6-8b801ed99b15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-10T18:06:35.762Z_

Let me do one final round of searches on the most threatening competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "575d2686-763f-4669-9150-9ec5aa9423e1",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLFvjNcCwHsMumGzJDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a9bd115-61fc-40bf-b728-d7d6aa274a46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJPQKbpdbWqCSe2Yqsy6H6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 19517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-10T18:06:36.311Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LrNy2m8o4NwH39C8Brhzhz`</summary>

```json
{
  "query": "ARISE repository level program graph fault localization repair May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a9bd115-61fc-40bf-b728-d7d6aa274a46",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLFvjNcCwHsMumGzJDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3494c8d7-6bf9-4be4-a8a7-e7d4f52216b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJPQKbpdbWqCSe2Yqsy6H6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 19517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-10T18:06:37.765Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G5vtzd5mAHhvGB4joKN2s5`</summary>

```json
{
  "query": "LLMxCPG code property graph context vulnerability detection 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3494c8d7-6bf9-4be4-a8a7-e7d4f52216b1",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLFvjNcCwHsMumGzJDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39014280-48b2-491f-869e-1401ef7e3988",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJPQKbpdbWqCSe2Yqsy6H6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 19517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4771,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-10T18:06:38.260Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017sSAdRP8KVCranNEeV22vo`</summary>

```json
{
  "query": "SWE-Pruner silver labels LLM distillation training data generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39014280-48b2-491f-869e-1401ef7e3988",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLFvjNcCwHsMumGzJDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd7dfa52-5ed3-4461-93ab-424561dd4692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJPQKbpdbWqCSe2Yqsy6H6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 19517,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 19517,
          "cache_creation_input_tokens": 4771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4771,
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

_source line 43 · 2026-05-10T18:06:43.617Z_

<details><summary>↩ Tool result · `toolu_01G5vtzd5mAHhvGB4joKN2s5`</summary>

```text
Web search results for query: "LLMxCPG code property graph context vulnerability detection 2025"

Links: [{"title":"[2507.16585] LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models","url":"https://arxiv.org/abs/2507.16585"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays"},{"title":"llmxcpg/README.md at main · qcri/llmxcpg","url":"https://github.com/qcri/llmxcpg/blob/main/README.md"},{"title":"Source Code for \"LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models\"","url":"https://zenodo.org/records/15614095"},{"title":"[Research] “LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models” Paper Review (EN) - hackyboiz","url":"https://hackyboiz.github.io/2025/09/22/l0ch/llmxcpg_paper_review/en/"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through ...","url":"https://www.usenix.org/system/files/usenixsecurity25-lekssays.pdf"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250716585L/abstract"},{"title":"LLMxCPG: context-aware vulnerability detection through ...","url":"https://dl.acm.org/doi/10.5555/3766078.3766104"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models","url":"https://arxiv.org/html/2507.16585v1"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models - Hamad Bin Khalifa University","url":"https://elmi.hbku.edu.qa/en/publications/llmxcpg-context-aware-vulnerability-detection-through-code-proper/"}]

Based on the search results, here's what I found about LLMxCPG:

## Overview

LLMxCPG is a novel framework integrating Code Property Graphs (CPG) with Large Language Models (LLM) for robust vulnerability detection. LLMxCPG was presented at USENIX Security 2025.

## Key Technical Features

The CPG-based slice construction technique reduces code size by 67.84 to 90.93% while preserving vulnerability-relevant context. The core methodology involves a two-phase process: Slice Construction, where an LLM generates specific queries for a Code Property Graph to extract a minimal, relevant "slice" of code that may contain a vulnerability, and Vulnerability Detection, where a second LLM analyzes the extracted code slice to classify it as either vulnerable or safe.

## Implementation

The framework uses a Query Generation Model (LLMxCPG-Q) fine-tuned from Qwen2.5-Coder-32B-Instruct, and a Detection Model (LLMxCPG-D) fine-tuned from QwQ-32B-Preview.

## Performance Results

Empirical evaluation demonstrates LLMxCPG's effectiveness across verified datasets, achieving 15-40% improvements in F1-score over state-of-the-art baselines. LLMxCPG maintains high performance across function-level and multi-function codebases while exhibiting robust detection efficacy under various syntactic code modifications.

## Motivation and Context

Over 25,000 new vulnerabilities were reported in the CVE database in 2024 alone, and while deep learning based approaches show promise for vulnerability detection, recent studies reveal critical limitations with accuracy dropping by up to 45% on rigorously verified datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39014280-48b2-491f-869e-1401ef7e3988",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "cd5d5a96-0d9b-461f-b20e-ca021fe65188",
  "sourceToolAssistantUUID": "39014280-48b2-491f-869e-1401ef7e3988",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T18:06:44.136Z_

<details><summary>↩ Tool result · `toolu_01LrNy2m8o4NwH39C8Brhzhz`</summary>

```text
Web search results for query: "ARISE repository level program graph fault localization repair May 2026"

Links: [{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048"},{"title":"Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02383-9"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"[2601.18044] RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/abs/2601.18044"},{"title":"Evaluating the usage of fault localization in automated program repair: an empirical study | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-020-9263-1"},{"title":"Alibaba LingmaAgent: Improving Automated Issue Resolution via Comprehensive Repository Exploration","url":"https://arxiv.org/html/2406.01422"}]

Based on the search results, here's what I found about ARISE:

## ARISE: Repository-level Graph Representation and Toolset

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

### Key Features

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

### Performance Improvements

Compared to the unmodified SWE-agent baseline, ARISE improves Function Recall@1 by 17.0 points and Line Recall@1 by 15.0 points, with ARISE achieving 22.0% Pass@1 (66/300), a 4.7 percentage-point improvement over SWE-agent.

### Technical Approach

Repository-level fault localization and automated program repair require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch. Existing graph-based systems provide structural representations of repositories but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.

### Design Philosophy

The graph builder and slicing API are designed as a framework-agnostic, drop-in toolset for future APR research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3494c8d7-6bf9-4be4-a8a7-e7d4f52216b1",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "b6d64b33-9f4c-4156-805a-d8397916e359",
  "sourceToolAssistantUUID": "3494c8d7-6bf9-4be4-a8a7-e7d4f52216b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T18:06:45.726Z_

<details><summary>↩ Tool result · `toolu_017sSAdRP8KVCranNEeV22vo`</summary>

```text
Web search results for query: "SWE-Pruner silver labels LLM distillation training data generation"

Links: [{"title":"LLM pruning & distillation: Minitron approach | SuperAnnotate","url":"https://www.superannotate.com/blog/llm-pruning-distillation-minitron-approach"},{"title":"LLM Distillation and Pruning: Strategies for Efficiency","url":"https://www.sapien.io/blog/llm-distillation-and-pruning"},{"title":"Knowledge Distillation in Automated Annotation: Supervised Text Classification with LLM-Generated Training Labels","url":"https://arxiv.org/html/2406.17633v1"},{"title":"Model Distillation: Teacher-Student Training Guide 2026 | Label Your Data","url":"https://labelyourdata.com/articles/machine-learning/model-distillation"},{"title":"LLM distillation demystified: a complete guide | Snorkel AI","url":"https://snorkel.ai/blog/llm-distillation-demystified-a-complete-guide/"},{"title":"Distilling a faster and smaller custom LLM using Google Gemini","url":"https://labelbox.com/guides/end-to-end-workflow-for-knowledge-distillation-with-nlp/"},{"title":"Knowledge distillation and dataset distillation of large language models: emerging trends, challenges, and future directions | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11423-3"},{"title":"LLM pruning and distillation - by valstechblog","url":"https://www.valstech.blog/p/llm-pruning-and-distillation"},{"title":"LLM Model Pruning and Knowledge Distillation with NVIDIA NeMo Framework | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/llm-model-pruning-and-knowledge-distillation-with-nvidia-nemo-framework/"},{"title":"How to Generate Synthetic Training Data for LLM Fine-Tuning (2026 Guide)","url":"https://blog.premai.io/how-to-generate-synthetic-training-data-for-llm-fine-tuning-2026-guide/"}]

Based on the search results, I found information about LLM distillation and training data generation techniques, though the results don't specifically focus on "SWE-Pruner" with silver labels. Here's what the search revealed about related concepts:

## LLM Distillation and Silver Labels

Knowledge distillation uses a large "teacher" model to create surrogate labels for fine-tuning downstream supervised classification models. This approach involves first using a generative LLM to label a subset of text samples and then fine-tuning supervised text classifiers with the LLM-generated labels.

Supervised classification models fine-tuned on LLM-generated labels perform comparably to models fine-tuned with labels from human annotators, making it a fast, efficient and cost-effective method of building supervised text classifiers.

## Training Data Generation Approaches

Synthetic training data is any data generated by a model or algorithm rather than collected from human activity. For LLM fine-tuning, this usually means instruction-response pairs: a question or task prompt, and a high-quality answer.

Data scientists can distill labels from multiple sources of signal by sending the same documents with well-engineered prompts to several publicly available LLMs. Several LLMs "voting" on the right answer typically achieve better performance than any individual model.

**Note:** The search results don't contain specific information about "SWE-Pruner" as a named research project or tool. If you're looking for more specific details about that particular project, you may want to search for it directly on academic repositories like arXiv or GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd7dfa52-5ed3-4461-93ab-424561dd4692",
  "isSidechain": true,
  "promptId": "0540f4f2-3739-42dc-a5c4-e80783313a68",
  "agentId": "a6f8ff7c85e9b6801",
  "type": "user",
  "uuid": "b49c85c9-9f56-440c-9f7c-a486c3f90cfb",
  "sourceToolAssistantUUID": "cd7dfa52-5ed3-4461-93ab-424561dd4692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-10T18:07:52.991Z_

Here is a comprehensive report of competing and concurrent work relevant to your paper idea (using data-flow analysis labels to train a neural context selector for repo-level code repair, replacing LLM-generated labels used by SWE-Pruner).

---

## 1. Neural Context Selection for Code Repair

**RelRepair (2025)** -- Uses structured retrieval to optimize queries based on buggy function context, constructing customized datasets from project codebases and selecting contextually relevant functions/snippets. This is retrieval-based, not a learned selector trained on program analysis labels, but it occupies a similar problem space.

**"Learning to Focus: Context Extraction for Efficient Code Vulnerability Detection" (May 2025, arXiv:2505.17460)** -- This is thematically close. It addresses learning which code context to extract for language models, moving beyond handcrafted heuristics and static slicing. Although it targets vulnerability detection rather than code repair, the core idea of *learning to select relevant code context* overlaps significantly with your proposal.

Sources: [RelRepair](https://arxiv.org/html/2509.16701v1), [Learning to Focus](https://arxiv.org/html/2505.17460v1)

---

## 2. Data-Flow Analysis + Neural Networks for Code

**DFA-Net (CC 2025)** -- A compiler-specific neural architecture that decomposes data-flow analyses (initialization, transfer, meet operations) into specialized neural networks. Achieves F1=0.761 vs GNN's 0.009 on data dependencies. This goes in the *opposite* direction from your idea: it learns to *perform* data-flow analysis with neural nets, whereas you propose using data-flow analysis to *train* neural nets. Not directly competing, but a reviewer might cite it as related work you should discuss.

**LLMxCPG (USENIX Security 2025)** -- Uses Code Property Graphs (which include data-flow edges) to guide an LLM in extracting minimal, vulnerability-relevant code slices, reducing code size by 67-91%. A fine-tuned LLM generates CPG queries, then a second LLM analyzes the extracted slice. This is *very relevant*: it uses program-analysis-derived graph structure to guide neural context selection, though for vulnerability detection. The difference is they use CPGs at inference time as a tool, while you propose distilling data-flow knowledge into a learned model.

Sources: [DFA-Net](https://conf.researchr.org/details/CC-2025/CC-2025-main-conference/9/DFA-Net-A-Compiler-Specific-Neural-Architecture-for-Robust-Generalization-in-Data-Fl), [LLMxCPG](https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays)

---

## 3. SWE-bench Context Pruning/Compression

**SWE-Pruner (Jan 2026, arXiv:2601.16746)** -- The direct baseline. Uses a 0.6B neural skimmer (Qwen3-Reranker-0.6B with CRF pruning head + reranking head) trained on "silver labels" to perform line-level context pruning. Achieves 23-54% token reduction. Critically, SWE-Pruner's training labels appear to be generated by LLMs (silver labels from larger models), which is exactly what your proposal aims to replace with data-flow analysis labels. Your paper would need to demonstrate clear advantages over these LLM-derived silver labels.

**SWE Context Bench (Feb 2026, arXiv:2602.08316)** -- A benchmark specifically for evaluating context learning/selection in coding tasks. You should evaluate on this.

Sources: [SWE-Pruner](https://arxiv.org/abs/2601.16746), [SWE Context Bench](https://www.arxiv.org/pdf/2602.08316)

---

## 4. Repository-Level Fault Localization

**ARISE (May 2026, arXiv:2605.03117)** -- THIS IS THE MOST DIRECTLY COMPETING WORK. ARISE builds a multi-granularity program graph extending down to statement-level nodes connected by *intra-procedural definition-use edges*, and exposes data-flow slicing as a first-class queryable agent primitive. It improves Function Recall@1 by 17 points and Line Recall@1 by 15 points over SWE-agent. ARISE uses def-use edges at inference time as a tool for agents, rather than distilling them into a neural selector, but it validates the core hypothesis that data-flow information is valuable for repo-level code repair. This is a very recent (May 2026) paper you must cite and differentiate from.

**LLM4FL** -- Multi-agent fault localization using graph-based retrieval + verbal reinforcement learning. Outperforms AutoFL by 18.55% in Top-1 accuracy.

**"A Study on the Impact of Fault Localization Granularity" (Apr 2026, arXiv:2604.00167)** -- Finds that function-level granularity yields the highest repair rate vs. line-level and file-level. This has implications for what granularity your neural selector should target.

**"On the Role of Fault Localization Context for LLM-Based Program Repair" (Apr 2026, arXiv:2604.05481)** -- Finds that more context does not consistently improve repair, with file-level localization being the dominant factor (15-17x improvement). This supports the premise that intelligent context selection matters.

Sources: [ARISE](https://arxiv.org/abs/2605.03117), [LLM4FL](https://openreview.net/forum?id=z91EvZbSI1), [Granularity Study](https://arxiv.org/abs/2604.00167), [FL Context Role](https://arxiv.org/abs/2604.05481)

---

## 5. Program Analysis Distillation into Code Models

**STALL+ (2024, arXiv:2406.10018)** -- Integrates static analysis (file-level dependencies) into LLM-based repository-level code completion. Found that integrating dependencies in the prompting phase works best. This uses static analysis at inference time rather than distilling it into model weights, but it's an important related work showing static analysis helps LLM code tasks.

**Self-Distillation for Code Generation (Apr 2026, arXiv:2604.01193)** -- Shows simple self-distillation improves code generation substantially. Not directly about program analysis distillation, but relevant methodology.

No work was found that specifically distills program analysis (e.g., data-flow labels) into a neural context selector. This appears to be a genuine novelty gap.

Sources: [STALL+](https://arxiv.org/abs/2406.10018), [Self-Distillation](https://arxiv.org/html/2604.01193v1)

---

## 6. RAG Approaches for Code Repair

**ReCode (2025, arXiv:2509.02330)** -- Fine-grained retrieval-augmented code repair with algorithm-aware categorization. Addresses the problem that holistic code-text embeddings fail to capture structural intricacies.

**ARCS (2025, arXiv:2504.20434)** -- Agentic retrieval-augmented code synthesis operating through a budgeted synthesize-execute-repair loop.

**Retrieval-Augmented Code Generation Survey (2025, arXiv:2510.04905)** -- Comprehensive survey covering RAG for repo-level code tasks. Your paper should cite this.

Sources: [ReCode](https://arxiv.org/html/2509.02330v1), [ARCS](https://arxiv.org/abs/2504.20434), [RAG Survey](https://arxiv.org/abs/2510.04905)

---

## 7. Tree-sitter for Def-Use / Training Data Generation

No academic work was found specifically using tree-sitter for def-use analysis to generate training data. Tree-sitter is widely used for AST parsing in developer tools and code indexing, but the specific application of extracting def-use chains via tree-sitter queries to create supervised training labels for a neural selector appears novel.

---

## 8. Current SWE-bench SOTA (May 2026)

- SWE-bench Verified top scores: Claude Mythos Preview (93.9%), Claude Opus 4.7 Adaptive (87.6%), GPT-5.3 Codex (85%)
- However, SWE-bench Verified is considered contaminated -- models can reproduce gold patches verbatim. SWE-bench Pro is the new standard where top models score ~23-46%.
- Agentless achieves 48-50.8% on Verified; SWE-Agent reaches 66%.
- AutoCodeRover was acquired by Sonar in Feb 2025, achieves 38% with far fewer API calls.

Sources: [SWE-bench Leaderboard](https://www.swebench.com/), [SWE-bench Pro](https://www.morphllm.com/swe-bench-pro), [Agentless](https://github.com/OpenAutoCoder/Agentless)

---

## Summary Assessment of Novelty Threats

**Highest threat:** ARISE (May 2026) directly uses def-use edges in program graphs for repo-level fault localization and repair. While it uses the analysis as an agent tool rather than distilling into a neural model, it validates the same core insight and is very recent. You must differentiate clearly.

**Significant threat:** LLMxCPG uses program-analysis-derived graphs to guide context selection via a fine-tuned neural model, albeit for vulnerability detection. The paradigm (program analysis guides neural context extraction) is very similar.

**Moderate threat:** SWE-Pruner's silver labels are your direct baseline. If their LLM-generated labels already capture data-flow-relevant patterns implicitly, the marginal gain from explicit data-flow labels may be small. You need strong empirical evidence.

**Novelty gap confirmed:** No one appears to have specifically proposed replacing LLM-generated silver labels with static-analysis-derived (data-flow) labels for training a neural context pruner. The specific combination of (1) tree-sitter-based def-use extraction, (2) using those as supervised labels, and (3) training a context selector for code repair appears novel as of May 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b49c85c9-9f56-440c-9f7c-a486c3f90cfb",
  "isSidechain": true,
  "agentId": "a6f8ff7c85e9b6801",
  "requestId": "req_011CauLGsTCpGD49R6HB483F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a1b543d-4837-4694-a73b-7d18a969358c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "917fdd66-0bc1-4154-b276-25256c4a40de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AmMURQPPEyrzrPL3yFKBx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3246,
      "cache_read_input_tokens": 24288,
      "output_tokens": 2531,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3246
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2531,
          "cache_read_input_tokens": 24288,
          "cache_creation_input_tokens": 3246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3246,
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
