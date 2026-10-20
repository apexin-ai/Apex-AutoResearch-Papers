# Research conversation: Research AlignScore - a factual consistency / text quality evaluation tool. I need to know: 1. What is AlignScore? (pape

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aac018ec7c892f4f1.jsonl`
- **Structured JSON:** [`9d6138830b7efc8aa1f3.json`](../../sessions/9d/9d6138830b7efc8aa1f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-25T06:31:41.151Z_

Research AlignScore - a factual consistency / text quality evaluation tool. I need to know:

1. What is AlignScore? (paper, purpose, what it measures)
2. GitHub repo and installation
3. What models does it need? GPU requirements?
4. How to use it programmatically - API / function calls
5. Is it suitable for measuring general text quality (not just factual consistency)?
6. Any alternatives that measure text quality/naturalness that could be used as independent quality indicators

Search the web for "AlignScore" paper, GitHub repo, and usage examples. Also search for "text quality metrics" that could serve as correlation targets for a contamination detection study.

Report concisely - I need enough detail to write an experiment plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "2df219f8-8950-4c72-9ae0-8ca36020627d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T06:31:41.154Z_

```json
{
  "parentUuid": "2df219f8-8950-4c72-9ae0-8ca36020627d",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "51a4ed6c-4b58-4044-9fc0-2151d7e3bf19",
  "timestamp": "2026-05-25T06:31:41.154Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-25T06:31:43.278Z_



I'll research AlignScore and text quality metrics. Let me search for the relevant information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51a4ed6c-4b58-4044-9fc0-2151d7e3bf19",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpQP7iEHXERzhtyJNta",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfd662bf-daca-42cd-9b41-b94fb0493b9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lt98M7CNEXqnJo6zMvnrnG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15072,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15072,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 4 · 2026-05-25T06:31:43.737Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014c6EDtUiAJNxZ4RBnb33xn`</summary>

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
  "parentUuid": "dfd662bf-daca-42cd-9b41-b94fb0493b9f",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpQP7iEHXERzhtyJNta",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "753171db-9673-4bc2-9107-091ccac47be2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lt98M7CNEXqnJo6zMvnrnG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15072,
      "cache_read_input_tokens": 0,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15072
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15072,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15072,
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

_source line 5 · 2026-05-25T06:31:43.745Z_

<details><summary>↩ Tool result · `toolu_014c6EDtUiAJNxZ4RBnb33xn`</summary>

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
  "parentUuid": "753171db-9673-4bc2-9107-091ccac47be2",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "8bbfbd51-7c4b-4c27-91aa-e615fc7fc21a",
  "sourceToolAssistantUUID": "753171db-9673-4bc2-9107-091ccac47be2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-25T06:31:45.965Z_



Let me search for AlignScore and related text quality metrics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bbfbd51-7c4b-4c27-91aa-e615fc7fc21a",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpQaQcSaq27UjPaJGDr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b9e975c-d66f-415a-ad6e-1c27e176c46d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqoxjrVXChsZRtoVxNPzAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 15072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 7 · 2026-05-25T06:31:46.394Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S126BToXagVbHsmJv7Lbgg`</summary>

```json
{
  "query": "AlignScore factual consistency evaluation paper GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b9e975c-d66f-415a-ad6e-1c27e176c46d",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpQaQcSaq27UjPaJGDr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "384dc6c5-1c3a-4538-a9db-c11f5ca16b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqoxjrVXChsZRtoVxNPzAJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 15072,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1460
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 15072,
          "cache_creation_input_tokens": 1460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1460,
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

_source line 8 · 2026-05-25T06:31:53.325Z_

<details><summary>↩ Tool result · `toolu_01S126BToXagVbHsmJv7Lbgg`</summary>

```text
Web search results for query: "AlignScore factual consistency evaluation paper GitHub"

Links: [{"title":"AlignScore: Unified Factual Consistency Metric","url":"https://www.emergentmind.com/papers/2305.16739"},{"title":"AlignScore: Evaluating Factual Consistency with A Unified Alignment Function - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.634/"},{"title":"AlignScore: Evaluating Factual Consistency with a Unified Alignment   Function","url":"https://arxiv.org/pdf/2305.16739"},{"title":"GitHub - yuh-zha/AlignScore: ACL2023 - AlignScore, a metric for factual consistency evaluation. · GitHub","url":"https://github.com/yuh-zha/AlignScore"},{"title":"Less is More for Improving Automatic Evaluation of Factual Consistency","url":"https://arxiv.org/pdf/2404.06579"},{"title":"factual-consistency · GitHub Topics · GitHub","url":"https://github.com/topics/factual-consistency"}]

Here are the search results for AlignScore factual consistency evaluation paper:

## Overview

AlignScore is a holistic metric that applies to a variety of factual inconsistency scenarios and is based on a general function of information alignment between two arbitrary text pieces. The paper was published in 2023 by Yuheng Zha, Yichi Yang, Ruichen Li, and Zhiting Hu in the Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL).

## Key Features

AlignScore is trained on 4.7M training examples from 7 well-established tasks (NLI, QA, paraphrase, and others). AlignScore achieves substantial improvement over a wide range of previous metrics and its 355M parameters match or even outperform metrics based on ChatGPT and GPT-4 that are orders of magnitude larger.

## GitHub Repository

The GitHub repository contains the implementation of AlignScore, a metric for automatic factual consistency evaluation of text pairs. You can find the official repository at: **https://github.com/yuh-zha/AlignScore**

## Additional Resources

- **ArXiv Paper**: https://arxiv.org/pdf/2305.16739
- **ACL Anthology**: https://aclanthology.org/2023.acl-long.634/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "384dc6c5-1c3a-4538-a9db-c11f5ca16b84",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "0324a5d5-3013-4906-8eb6-7795d8d15b66",
  "sourceToolAssistantUUID": "384dc6c5-1c3a-4538-a9db-c11f5ca16b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T06:31:55.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HpiC2TqUbWsbjk3DSgxvVY`</summary>

```json
{
  "query": "AlignScore GitHub yuh-zha installation usage API python"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0324a5d5-3013-4906-8eb6-7795d8d15b66",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpRH9KBCYnEArqs3X4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f11e8637-174d-465c-93a0-0592729d8c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ToKLPFHPSM5bKj6YsEmXS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 16532,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 16532,
          "cache_creation_input_tokens": 689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 689,
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

_source line 10 · 2026-05-25T06:32:03.035Z_

<details><summary>↩ Tool result · `toolu_01HpiC2TqUbWsbjk3DSgxvVY`</summary>

```text
Web search results for query: "AlignScore GitHub yuh-zha installation usage API python"

Links: [{"title":"AlignScore/generate_training_data.py at main · yuh-zha/AlignScore","url":"https://github.com/yuh-zha/AlignScore/blob/main/generate_training_data.py"},{"title":"yuh-zha - Overview","url":"https://github.com/yuh-zha"},{"title":"GitHub - yuh-zha/AlignScore: ACL2023 - AlignScore, a metric for factual consistency evaluation. · GitHub","url":"https://github.com/yuh-zha/AlignScore"},{"title":"AlignScore/pyproject.toml at main · yuh-zha/AlignScore","url":"https://github.com/yuh-zha/AlignScore/blob/main/pyproject.toml"},{"title":"NeMo-Guardrails/nemoguardrails/library/factchecking/align_score/Dockerfile at develop · NVIDIA/NeMo-Guardrails","url":"https://github.com/NVIDIA/NeMo-Guardrails/blob/develop/nemoguardrails/library/factchecking/align_score/Dockerfile"},{"title":"yzha/AlignScore · Hugging Face","url":"https://huggingface.co/yzha/AlignScore"},{"title":"Actions · yuh-zha/AlignScore","url":"https://github.com/yuh-zha/AlignScore/actions"},{"title":"AlignScore/benchmark.py at main · yuh-zha/AlignScore","url":"https://github.com/yuh-zha/AlignScore/blob/main/benchmark.py"},{"title":"Releases · yuh-zha/AlignScore","url":"https://github.com/yuh-zha/AlignScore/releases"},{"title":"GitHub - yuh-zha/Align: Align, a general text alignment function","url":"https://github.com/yuh-zha/Align"}]

Based on the search results, here's information about AlignScore from the yuh-zha GitHub repository:

## Overview

AlignScore is a metric for automatic factual consistency evaluation of text pairs introduced in the ACL 2023 paper by Yuheng Zha, Yichi Yang, Ruichen Li and Zhiting Hu.

## Installation

The package is available as version 0.1.3 with support for Python >= 3.8. After installing alignscore, you should use `python -m spacy download en_core_web_sm` to install the required spaCy model for sentenization.

## Dependencies

Key dependencies include spacy (>=3.4.0,<4), nltk (>=3.7,<4), torch (>=1.12.1,<2), transformers (>=4.20.1,<5), and other packages like tqdm, jsonlines, numpy, datasets, scikit-learn, pytorch_lightning, scipy, and tensorboard.

## Python API Usage

To use the score method, you import AlignScore and create a scorer instance with parameters like model ('roberta-base'), batch_size (e.g., 32), device (e.g., 'cuda:0'), checkpoint path, and evaluation_mode. Evaluation modes include 'nli_sp', 'nli', 'bin_sp', and 'bin', where 'sp' indicates if the chunk-sentence splitting method is used. Two checkpoint versions are available: AlignScore-base and AlignScore-large.

## How It Works

The metric uses a unified information alignment function trained on 4.7 million examples from 7 tasks, and employs chunk-sentence splitting to compute alignment scores between chunks and sentences, averaging them for a factual consistency score.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f11e8637-174d-465c-93a0-0592729d8c58",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "2bb3952c-0183-4852-9e45-c66173ad0561",
  "sourceToolAssistantUUID": "f11e8637-174d-465c-93a0-0592729d8c58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T06:32:06.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CWs6QqMSKWvX4MSbRGtA6e`</summary>

```json
{
  "query": "AlignScore model checkpoints GPU requirements memory RoBERTa base large"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bb3952c-0183-4852-9e45-c66173ad0561",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpRzhtBdXkTxvSUV6bp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddd925bb-6188-431a-8f95-ae90266af51e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNFJ71Sb9ocr3SETkhTZdb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 17221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 12 · 2026-05-25T06:32:11.968Z_

<details><summary>↩ Tool result · `toolu_01CWs6QqMSKWvX4MSbRGtA6e`</summary>

```text
Web search results for query: "AlignScore model checkpoints GPU requirements memory RoBERTa base large"

Links: [{"title":"DOC: Add more specific GPU examples to System Requirements in README.md · Issue #395 · google-deepmind/gemma","url":"https://github.com/google-deepmind/gemma/issues/395"},{"title":"AlignScore Deployment — NVIDIA NeMo Guardrails Library Developer Guide","url":"https://docs.nvidia.com/nemo/guardrails/latest/user-guides/advanced/align-score-deployment.html"},{"title":"How checkpointing impacts AI infrastructure storage requirements and cluster size","url":"https://www.cudocompute.com/blog/storage-requirements-for-ai-clusters"},{"title":"Loading big models into memory · Hugging Face","url":"https://huggingface.co/docs/accelerate/en/concept_guides/big_model_inference"},{"title":"Guide to GPU Requirements for Running AI Models","url":"https://www.bacloud.com/en/blog/163/guide-to-gpu-requirements-for-running-ai-models.html"},{"title":"GPU Memory Requirement Prediction for Deep Learning Task Based on Bidirectional Gated Recurrent Unit Optimization Transformer","url":"https://arxiv.org/pdf/2510.20985"},{"title":"The Complete Guide to GPU Requirements for LLM Fine-Tuning | Runpod Blog","url":"https://www.runpod.io/blog/llm-fine-tuning-gpu-guide"}]

I found some relevant information about AlignScore deployment. The AlignScore server loads only the base model by default, and you can configure the AlignScore model to run on CPU or on a GPU device like "cuda:0".

However, the search results don't contain specific GPU memory requirements for the AlignScore model checkpoints (base or large variants). The results do mention that you need to set the ALIGN_SCORE_PATH environment variable to point to where the checkpoints have been downloaded, but the specific memory requirements for RoBERTa base and large variants used in AlignScore aren't detailed in these results.

To get more specific information about memory requirements for different AlignScore checkpoint sizes, you may want to check the official AlignScore repository documentation or the NVIDIA NeMo Guardrails documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddd925bb-6188-431a-8f95-ae90266af51e",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "0e260238-c7c1-422a-9443-6e2e31139779",
  "sourceToolAssistantUUID": "ddd925bb-6188-431a-8f95-ae90266af51e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T06:32:15.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QvczAsTNYa4y8VTbGiqySS`</summary>

```json
{
  "query": "text quality metrics NLG evaluation naturalness fluency perplexity MAUVE BERTScore 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e260238-c7c1-422a-9443-6e2e31139779",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpSetnsYgt4TU32XgyN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46a693ce-6d6a-40ac-9f80-eb106148325f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GpHfpnveg1UnHormqGutw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 18225,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 643
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 643,
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

_source line 14 · 2026-05-25T06:32:24.815Z_

<details><summary>↩ Tool result · `toolu_01QvczAsTNYa4y8VTbGiqySS`</summary>

```text
Web search results for query: "text quality metrics NLG evaluation naturalness fluency perplexity MAUVE BERTScore 2024 2025"

Links: [{"title":"TPM Vol. 32, No. S8, 2025 Open Access ISSN: 1972-6325 https://www.tpmap.org/","url":"https://tpmap.org/submission/index.php/tpm/article/download/2693/2035/5851"},{"title":"Automated metrics for evaluating the quality of text generation | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/automated-metrics-for-evaluating-generated-text"},{"title":"Improving Evaluation Metrics for Text Summarization","url":"https://bright-journal.org/Journal/index.php/JADS/article/download/547/366"},{"title":"Evaluation Metrics: Assessing the quality of NLG outputs | Towards Data Science","url":"https://towardsdatascience.com/evaluation-metrics-assessing-the-quality-of-nlg-outputs-39749a115ff3/"},{"title":"Automating Text Naturalness Evaluation of NLG Systems","url":"https://arxiv.org/pdf/2006.13268"},{"title":"Detailed Explanation of Evaluation Metrics for Large Language Models: ROUGE, BLEU, Perplexity, MRR, and BERTScore - Oreate AI Blog","url":"https://www.oreateai.com/blog/detailed-explanation-of-evaluation-metrics-for-large-language-models-rouge-bleu-perplexity-mrr-and-bertscore/8979d5f5d913403e7060e400fa59d970"},{"title":"From Internal Representations to Text Quality: A Geometric Approach to LLM Evaluation","url":"https://arxiv.org/pdf/2509.25359"}]

I've completed the web search on text quality metrics for NLG evaluation. Here's a summary of the key findings:

## Key Metrics Found

Automated metrics include Perplexity, BLEU, ROUGE, F1-Score, and BERTScore, which are commonly used to evaluate NLG systems.

### BERTScore
BERTScore uses BERT for calculating the quality of text generated by NLG systems, capturing the semantic aspect by using contextualized embeddings generated by the BERT model. BERTScore emerges as the most robust automatic metric, as it combines the efficiency of traditional metrics with better capture of semantics.

### Perplexity
Perplexity is a core metric for assessing the predictive capability of language models; it directly reflects the model's uncertainty in predicting a given sequence of text.

### Evaluation Challenges
Human Assessment is still indispensable for assessing qualitative aspects such as coherence, fluency, and relevance. Quality aspects include readability, coherence, naturalness, fluency, adequacy or grammaticality.

### Recent Research (2025)
Text quality has been defined as text naturalness - that is, text that closely resembles human language. Recent work is exploring Intrinsic Dimensionality and Effective Rank as universal reference-free measures of text quality.

Note: The search results did not include specific information about MAUVE metric, though the other metrics mentioned in your query were covered.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46a693ce-6d6a-40ac-9f80-eb106148325f",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "558542dc-8a5e-4748-9210-77f19228a1da",
  "sourceToolAssistantUUID": "46a693ce-6d6a-40ac-9f80-eb106148325f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T06:32:29.502Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AEHqxPXrjdFGtCauEn627o`</summary>

```json
{
  "query": "MAUVE metric text generation quality evaluation pillutla 2021 usage python"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "558542dc-8a5e-4748-9210-77f19228a1da",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpTboXuvbPKGBRMyutW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d55ec55c-9e46-4972-beee-b7111e05b060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019kaKMZuYeBg57QwG4afwEz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 18868,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 18868,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 907,
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

_source line 16 · 2026-05-25T06:32:35.590Z_

<details><summary>↩ Tool result · `toolu_01AEHqxPXrjdFGtCauEn627o`</summary>

```text
Web search results for query: "MAUVE metric text generation quality evaluation pillutla 2021 usage python"

Links: [{"title":"MAUVE: Measuring the Gap Between Neural Text and Human Text — MAUVE","url":"https://krishnap25.github.io/mauve/"},{"title":"MAUVE: Human-Machine Divergence Curves for Evaluating Open-Ended Text Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MAUVE:-Human-Machine-Divergence-Curves-for-Text-Pillutla-Swayamdipta/0f41926bd630bf057f9a5fba0ba550fe9a46f1f0"},{"title":"[2102.01454] MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers","url":"https://arxiv.org/abs/2102.01454"},{"title":"MAUVE: Human-Machine Divergence Curves for Evaluating Open-Ended Text Generation | Request PDF","url":"https://www.researchgate.net/publication/348980479_MAUVE_Human-Machine_Divergence_Curves_for_Evaluating_Open-Ended_Text_Generation"},{"title":"MAUVE: Measuring the Gap Between Neural Text and Human Text","url":"https://arxiv.org/pdf/2102.01454"},{"title":"MAUVE Scores for Generative Models: Theory and Practice","url":"https://www.jmlr.org/papers/volume24/23-0023/23-0023.pdf"},{"title":"On the Usefulness of Embeddings, Clusters and Strings for Text Generator   Evaluation","url":"https://arxiv.org/pdf/2205.16001"}]

Here are the search results for MAUVE metric:

## Overview

MAUVE is a metric for open-ended text generation, which directly compares the distribution of machine-generated text to that of human language. The metric was published in 2021 by Krishna Pillutla, Swabha Swayamdipta, and co-authors.

## Key Characteristics

It can quantify differences in the quality of generated text based on the size of the model, the decoding algorithm, and the length of the generated text. MAUVE was found to correlate the strongest with human evaluations over baseline metrics for open-ended text generation.

MAUVE measures the mean area under the divergence curve for the two distributions, exploring the trade-off between two types of errors: those arising from parts of the human distribution that the model distribution approximates well, and those it does not.

## Advantages

Through an extensive empirical study on three open-ended generation tasks, MAUVE identifies known properties of generated text, scales naturally with model size, and correlates with human judgments, with fewer restrictions than existing distributional evaluation metrics.

## Python Implementation

The official MAUVE implementation is available at https://krishnap25.github.io/mauve/, which provides a Python package for using the metric in your own projects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d55ec55c-9e46-4972-beee-b7111e05b060",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "3a8431c1-19bd-46e7-aa54-ec7240c49d5e",
  "sourceToolAssistantUUID": "d55ec55c-9e46-4972-beee-b7111e05b060",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T06:32:38.071Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CkQATFwK2r1DacxXmSwzv2`</summary>

```json
{
  "query": "AlignScore python code example scorer = AlignScore evaluation_mode checkpoint usage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a8431c1-19bd-46e7-aa54-ec7240c49d5e",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpUPqj1DY6YWNCVynv6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e5812a0-20d6-4817-a1b9-e646eff14951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QMZqk3BJokgynd5xTa2o7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 19775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 808,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 18 · 2026-05-25T06:32:45.482Z_

<details><summary>↩ Tool result · `toolu_01CkQATFwK2r1DacxXmSwzv2`</summary>

````text
Web search results for query: "AlignScore python code example scorer = AlignScore evaluation_mode checkpoint usage"

Links: [{"title":"README.md · yzha/AlignScore at 8509e78d25bb914939fc585c626500c9b2944249","url":"https://huggingface.co/yzha/AlignScore/blob/8509e78d25bb914939fc585c626500c9b2944249/README.md"},{"title":"GitHub - yuh-zha/AlignScore: ACL2023 - AlignScore, a metric for factual consistency evaluation. · GitHub","url":"https://github.com/yuh-zha/AlignScore"},{"title":"yzha/AlignScore · Hugging Face","url":"https://huggingface.co/yzha/AlignScore"},{"title":"Not initialized model weights when loading checkpoint · Issue #7 · yuh-zha/AlignScore","url":"https://github.com/yuh-zha/AlignScore/issues/7"},{"title":"Huggingface","url":"https://huggingface.co/yzha/AlignScore/raw/06cd3881dd3adb495a932c316dbafd69f5561a4e/README.md"},{"title":"AlignScore/benchmark.py at main · yuh-zha/AlignScore","url":"https://github.com/yuh-zha/AlignScore/blob/main/benchmark.py"},{"title":"krotima1/AlignScoreCS · Hugging Face","url":"https://huggingface.co/krotima1/AlignScoreCS"},{"title":"NeMo-Guardrails/nemoguardrails/library/factchecking/align_score/Dockerfile at develop · NVIDIA/NeMo-Guardrails","url":"https://github.com/NVIDIA/NeMo-Guardrails/blob/develop/nemoguardrails/library/factchecking/align_score/Dockerfile"},{"title":"AlignScore Deployment — NVIDIA NeMo Guardrails Library Developer Guide","url":"https://docs.nvidia.com/nemo/guardrails/latest/user-guides/advanced/align-score-deployment.html"}]

Based on the search results, here's a comprehensive overview of AlignScore Python code examples:

## Basic Python Code Example

The basic usage is:
```python
from alignscore import AlignScore
scorer = AlignScore(model='roberta-base', batch_size=32, device='cuda:0', ckpt_path='/path/to/checkpoint', evaluation_mode='nli_sp')
score = scorer.score(contexts=['hello world.'], claims=['hello world.'])
```

## Parameter Explanation

**Key parameters:**

- **model**: the backbone model of the metric. Now, we only provide the metric trained on RoBERTa. **batch_size**: the batch size of the inference. **device**: which device to run the metric. **ckpt_path**: the path to the checkpoint.

- **evaluation_mode**: choose from 'nli_sp', 'nli', 'bin_sp', 'bin'. nli and bin refer to the 3-way and binary classification head, respectively. sp indicates if the chunk-sentence splitting method is used. nli_sp is the default setting of AlignScore

## Available Checkpoints

AlignScore-base and AlignScore-large checkpoints are available for download from Hugging Face, which can be used directly for factual consistency evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e5812a0-20d6-4817-a1b9-e646eff14951",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "8d3747d6-3a2c-4a4d-b631-76c3169d78a6",
  "sourceToolAssistantUUID": "2e5812a0-20d6-4817-a1b9-e646eff14951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T06:32:48.394Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dh3zeksSonbhSkXMvXbPFX`</summary>

```json
{
  "query": "\"text quality\" \"reference-free\" metric LLM generation evaluation GPT-score UniEval 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d3747d6-3a2c-4a4d-b631-76c3169d78a6",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpV8CQwYg7PdLRPdMbP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44ee41b6-f46d-45cf-8e99-de99493f35a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BgE1R2TPpsrokbHVRUFW8R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 942,
      "cache_read_input_tokens": 20583,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 20583,
          "cache_creation_input_tokens": 942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 942,
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

_source line 20 · 2026-05-25T06:32:56.065Z_

<details><summary>↩ Tool result · `toolu_01Dh3zeksSonbhSkXMvXbPFX`</summary>

```text
Web search results for query: ""text quality" "reference-free" metric LLM generation evaluation GPT-score UniEval 2024 2025"

Links: [{"title":"From Internal Representations to Text Quality: A Geometric Approach to LLM Evaluation","url":"https://arxiv.org/pdf/2509.25359"},{"title":"Reference-free Evaluation Metrics for Text Generation: A Survey","url":"https://arxiv.org/html/2501.12011v1"},{"title":"Check-Eval: A Checklist-based Approach for Evaluating Text Quality","url":"https://arxiv.org/pdf/2407.14467"},{"title":"[2304.00723] Exploring the Use of Large Language Models for Reference-Free Text Quality Evaluation: An Empirical Study","url":"https://arxiv.org/abs/2304.00723"},{"title":"Benchmarking LLMs' Judgments with No Gold Standard","url":"https://arxiv.org/pdf/2411.07127"},{"title":"Exploring the Use of Large Language Models for Reference-Free Text   Quality Evaluation: An Empirical Study","url":"https://arxiv.org/pdf/2304.00723"},{"title":"LLMs as Narcissistic Evaluators: When Ego Inflates Evaluation Scores","url":"https://arxiv.org/pdf/2311.09766"},{"title":"LLMs Are Not Scorers: Rethinking MT Evaluation with Generation-Based Methods","url":"https://arxiv.org/pdf/2505.16129"}]

I found comprehensive search results related to reference-free evaluation metrics for LLM-generated text. Here's what the current research shows:

## Key Reference-Free Metrics

Intrinsic Dimensionality and Effective Rank are proposed as universal reference-free measures of text quality based on fundamental geometric properties, representing a recent geometric approach to evaluation.

GPTScore is a framework that utilizes generative pre-trained transformers and other language models to evaluate NLG outputs without relying on reference texts, assessing the probability that the LLM assigns to the generated text. Check-Eval achieves higher correlations with human judgments compared to existing metrics, such as G-EVAL and GPTSCORE.

## Recent Research

With the advent of LLMs, reference-free metrics have also advanced. A comprehensive survey from January 2025 provides updates on the field, noting that slight modifications in the prompt can alter evaluations and there are biases like giving higher ratings to longer hypotheses; additionally, most LLMs used in this approach are proprietary commercial models subject to frequent updates, which poses challenges to reproducibility.

## UniEval and Limitations

While I found results about GPT-score and other metrics, the search results don't contain specific information about UniEval in 2024-2025 timeframes. The results do show that evaluation metrics can demonstrate bias toward their underlying language models in a reference-free manner, and assessments can be influenced by factors beyond inherent text quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44ee41b6-f46d-45cf-8e99-de99493f35a5",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "0ae33b7f-b1eb-4e8d-b52d-6d832cc543e7",
  "sourceToolAssistantUUID": "44ee41b6-f46d-45cf-8e99-de99493f35a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T06:32:58.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012SAbSWua9v7f1Nvg9hKZo4`</summary>

```json
{
  "query": "mauve-text pip install python usage example compute_mauve 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ae33b7f-b1eb-4e8d-b52d-6d832cc543e7",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpVuQkHhGbbEafSX7jg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c775f6d-2aa1-4809-9935-255c0957d58a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Yybmm1g22eK61AfMNLBhP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 21525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 807,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 22 · 2026-05-25T06:33:06.741Z_

<details><summary>↩ Tool result · `toolu_012SAbSWua9v7f1Nvg9hKZo4`</summary>

```text
Web search results for query: "mauve-text pip install python usage example compute_mauve 2024"

Links: [{"title":"GitHub - krishnap25/mauve: Package to compute Mauve, a similarity score between neural text and human text. Install with `pip install mauve-text`. · GitHub","url":"https://github.com/krishnap25/mauve"},{"title":"mauve-text · PyPI","url":"https://pypi.org/project/mauve-text/"},{"title":"GitHub - krishnap25/mauve-experiments","url":"https://github.com/krishnap25/mauve-experiments"},{"title":"mauve-experiments/README.md at main · krishnap25/mauve-experiments","url":"https://github.com/krishnap25/mauve-experiments/blob/main/README.md"},{"title":"MAUVE: Measuring the Gap Between Neural Text and Human Text — MAUVE","url":"https://krishnap25.github.io/mauve/"},{"title":"mauve/setup.py at main · krishnap25/mauve","url":"https://github.com/krishnap25/mauve/blob/main/setup.py"},{"title":"mauve/README.md at main · krishnap25/mauve","url":"https://github.com/krishnap25/mauve/blob/main/README.md"},{"title":"Releases · krishnap25/mauve","url":"https://github.com/krishnap25/mauve/releases"},{"title":"mauve/pyproject.toml at main · krishnap25/mauve","url":"https://github.com/krishnap25/mauve/blob/main/pyproject.toml"},{"title":"Workflow runs · krishnap25/mauve","url":"https://github.com/krishnap25/mauve/actions"}]

Based on the search results, here's information about mauve-text and how to use `compute_mauve`:

## Installation

The mauve-text library is built on PyTorch and HuggingFace Transformers to measure the gap between neural text and human text with the MAUVE measure. The latest version was released on Jul 3, 2024, and you can install it with `pip install mauve-text`.

## What is MAUVE

MAUVE is a measure of the gap between neural text and human text, computed using the Kullback–Leibler (KL) divergences between the two text distributions in a quantized embedding space of a large language model.

## Basic Usage Example

Let p_text and q_text each be a list of strings, where each string is a complete generation (including context). For best practice, MAUVE needs at least a few thousand generations each for p_text and q_text (the paper uses 5000 each), though for a demo, 100 generations each can be used for fast running time.

To call mauve.compute_mauve using tokens on GPU, you can pass p_tokens and q_tokens which are each a list of LongTensors, along with device_id and max_text_length parameters.

## Output

The output includes out.mauve_star and out.frontier_integral_star (their corresponding versions computed with Krichevsky-Trofimov smoothing), and out.divergence_curve (a numpy.ndarray of shape (m, 2) that can be plotted with matplotlib).

For more detailed usage examples and documentation, you can refer to the official GitHub repository at https://github.com/krishnap25/mauve or the documentation at https://krishnap25.github.io/mauve/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c775f6d-2aa1-4809-9935-255c0957d58a",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "5fbcbcee-fd3a-4699-9b97-8e9290995646",
  "sourceToolAssistantUUID": "6c775f6d-2aa1-4809-9935-255c0957d58a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T06:33:09.166Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E6as2G18zmjj7hmqizeTHX`</summary>

```json
{
  "query": "UniEval text quality evaluation multidimensional coherence fluency naturalness pip install"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fbcbcee-fd3a-4699-9b97-8e9290995646",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpWhQiCF197tvd4htdo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14c7299d-3844-4414-bf23-0285343e7499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTFXcpuEiht2qtPr8xpqUQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 22332,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 22332,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 944,
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

_source line 24 · 2026-05-25T06:33:20.044Z_

<details><summary>↩ Tool result · `toolu_01E6as2G18zmjj7hmqizeTHX`</summary>

```text
Web search results for query: "UniEval text quality evaluation multidimensional coherence fluency naturalness pip install"

Links: [{"title":"UniEval/README.md at main · maszhongming/UniEval","url":"https://github.com/maszhongming/UniEval/blob/main/README.md"},{"title":"GitHub - weibifan/eval_UniEval: Repository for EMNLP 2022 Paper: Towards a Unified Multi-Dimensional Evaluator for Text Generation","url":"https://github.com/weibifan/eval_UniEval"},{"title":"GitHub - maszhongming/UniEval: Repository for EMNLP 2022 Paper: Towards a Unified Multi-Dimensional Evaluator for Text Generation · GitHub","url":"https://github.com/maszhongming/unieval"},{"title":"Towards a Unified Multi-Dimensional Evaluator for Text Generation","url":"https://arxiv.org/pdf/2210.07197"},{"title":"Towards a Unified Multi-Dimensional Evaluator for Text Generation - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.131/"},{"title":"Towards a Unified Multi-Dimensional Evaluator for Text Generation | Request PDF","url":"https://www.researchgate.net/publication/372930157_Towards_a_Unified_Multi-Dimensional_Evaluator_for_Text_Generation"},{"title":"Towards a Unified Multi-Dimensional Evaluator for Text ...","url":"https://aclanthology.org/2022.emnlp-main.131.pdf"},{"title":"MingZhong/unieval-sum · Hugging Face","url":"https://huggingface.co/MingZhong/unieval-sum"},{"title":"[2210.07197] Towards a Unified Multi-Dimensional Evaluator for Text Generation","url":"https://arxiv.org/abs/2210.07197"},{"title":"Towards a Unified Multi-Dimensional Evaluator for Text Generation Ming Zhong§","url":"https://blender.cs.illinois.edu/paper/generationeval2022.pdf"}]

Based on the search results, here's what I found about UniEval:

## Overview

UniEval is a unified multi-dimensional evaluator for NLG that re-frames evaluation as a Boolean Question Answering (QA) task, allowing one evaluator to assess multiple dimensions by guiding the model with different questions.

## Evaluation Dimensions

UniEval-sum evaluates coherence, consistency, fluency and relevance for text summarization, and can also be used to evaluate naturalness and informativeness for data-to-text. UniEval-dialog evaluates naturalness, coherence, engagingness, groundedness and understandability for dialogue response generation.

## Performance

UniEval correlates substantially better with human judgments than existing metrics, achieving a 23% higher correlation on text summarization and over 43% on dialogue response generation compared to top-performing unified evaluators.

## Availability

Source code, data, and all pre-trained evaluators are available at https://github.com/maszhongming/UniEval. The GitHub repository contains the code and resources for installation and usage. For pip installation instructions, you would need to refer to the repository's README file or installation guide at that GitHub link.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14c7299d-3844-4414-bf23-0285343e7499",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "409f2677-0b4a-4d59-8ee1-87f07a60165a",
  "sourceToolAssistantUUID": "14c7299d-3844-4414-bf23-0285343e7499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T06:33:22.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MxY3icYEzaRRsKitmg799Y`</summary>

```json
{
  "query": "AlignScore beyond factual consistency general text quality evaluation limitations scope"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "409f2677-0b4a-4d59-8ee1-87f07a60165a",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpXfwBre3gKf2nV2SyT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebc8cebd-57de-42b0-9188-542d90f995bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fpJBiHUvPDn7Y6BP3Zenz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 897,
      "cache_read_input_tokens": 23276,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 897
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 23276,
          "cache_creation_input_tokens": 897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 897,
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

_source line 26 · 2026-05-25T06:33:30.085Z_

<details><summary>↩ Tool result · `toolu_01MxY3icYEzaRRsKitmg799Y`</summary>

```text
Web search results for query: "AlignScore beyond factual consistency general text quality evaluation limitations scope"

Links: [{"title":"AlignScore: Evaluating Factual Consistency with a Unified Alignment   Function","url":"https://arxiv.org/pdf/2305.16739"},{"title":"AlignScore: Unified Factual Consistency Metric","url":"https://www.emergentmind.com/papers/2305.16739"},{"title":"AlignScore: Evaluating Factual Consistency with a Unified Alignment Function | alphaXiv","url":"https://www.alphaxiv.org/overview/2305.16739"},{"title":"[2305.16739] AlignScore: Evaluating Factual Consistency with a Unified Alignment Function","url":"https://arxiv.org/abs/2305.16739"},{"title":"[2404.06579] Less is More for Improving Automatic Evaluation of Factual Consistency","url":"https://ar5iv.labs.arxiv.org/html/2404.06579v1"},{"title":"[2305.16739v1] AlignScore: Evaluating Factual Consistency with a Unified Alignment Function","url":"https://arxiv.org/abs/2305.16739v1"},{"title":"[Literature Review] Less is More for Improving Automatic Evaluation of Factual Consistency","url":"https://www.themoonlight.io/en/review/less-is-more-for-improving-automatic-evaluation-of-factual-consistency"},{"title":"Less is More for Improving Automatic Evaluation of Factual Consistency","url":"https://arxiv.org/html/2404.06579v1"},{"title":"Less is More for Improving Automatic Evaluation of Factual Consistency","url":"https://arxiv.org/pdf/2404.06579"}]

Based on the search results, here's what I found about AlignScore's scope, limitations, and relationship to general text quality evaluation:

## AlignScore's Primary Focus and Scope

AlignScore is a general factual consistency metric based on a unified text-to-text information alignment function. It was trained by reformatting and aggregating 15 datasets from 7 popular language tasks, including NLI, QA, paraphrasing, fact verification, information retrieval, semantic similarity, and summarization, resulting in 4.7M training examples.

## Limitations and Scope

While AlignScore addresses factual consistency specifically, it has notable limitations:

**Training Data Quality Issues:** The training data was derived in a heuristic manner from many existing NLP tasks and datasets, adding noise and poor quality in some samples.

**Robustness Concerns:** AlignScore displays fragility regarding robustness, as it fails to identify some clear perturbations involving entities like names, numbers, with even simple modifications producing false positives and false negatives.

**Beyond Factual Consistency:** The search results indicate that AlignScore defines alignment in a general way to enable integration of diverse training data, and is delivered as a metric focusing on factual consistency rather than broader text quality. The metric is not intended as a comprehensive general text quality evaluation tool, but rather specialized for assessing whether generated text maintains consistency with source information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebc8cebd-57de-42b0-9188-542d90f995bb",
  "isSidechain": true,
  "promptId": "1aaff919-6b1e-499f-9a2e-edbca12dff84",
  "agentId": "aac018ec7c892f4f1",
  "type": "user",
  "uuid": "d2e58c17-9c03-49ed-b94b-e62955e4c81e",
  "sourceToolAssistantUUID": "ebc8cebd-57de-42b0-9188-542d90f995bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-25T06:34:10.262Z_

Here is the consolidated research report.

---

## 1. What is AlignScore?

**Paper:** "AlignScore: Evaluating Factual Consistency with a Unified Alignment Function" (Yuheng Zha, Yichi Yang, Ruichen Li, Zhiting Hu). Published at **ACL 2023**.

**Purpose:** Measures **factual consistency** between two text pieces (e.g., a source document and a generated summary). It defines a general "information alignment" function and trains it on 4.7M examples from 7 task types (NLI, QA, paraphrase, fact verification, information retrieval, semantic similarity, summarization).

**What it measures:** Given a `context` (source) and a `claim` (generated text), it returns a score [0, 1] indicating how factually consistent the claim is with the context. It uses chunk-sentence splitting to handle long texts.

**Key result:** 355M-parameter model that matches or outperforms ChatGPT/GPT-4-based factual consistency metrics on standard benchmarks.

---

## 2. GitHub Repo and Installation

- **Repo:** [github.com/yuh-zha/AlignScore](https://github.com/yuh-zha/AlignScore)
- **HuggingFace checkpoints:** [huggingface.co/yzha/AlignScore](https://huggingface.co/yzha/AlignScore)

**Installation:**
```bash
pip install alignscore
python -m spacy download en_core_web_sm
```

**Key dependencies:** `torch>=1.12.1,<2`, `transformers>=4.20.1,<5`, `spacy>=3.4.0,<4`, `nltk`, `numpy`, `scikit-learn`. Note the strict upper bounds on torch and transformers -- this may cause dependency conflicts with modern stacks.

---

## 3. Models and GPU Requirements

Two checkpoints available on HuggingFace:
- **AlignScore-base** (RoBERTa-base backbone, ~125M params) -- lightweight, runs fine on any GPU or even CPU
- **AlignScore-large** (RoBERTa-large backbone, ~355M params) -- better performance, still small by modern standards

**GPU requirements:** Minimal. RoBERTa-large is ~1.4GB in memory. With batch_size=32, total GPU memory usage is well under 4GB. Easily runs on a single consumer GPU. CPU inference is also feasible for moderate-scale experiments.

---

## 4. Programmatic Usage

```python
from alignscore import AlignScore

scorer = AlignScore(
    model='roberta-large',        # or 'roberta-base'
    batch_size=32,
    device='cuda:0',              # or 'cpu'
    ckpt_path='/path/to/AlignScore-large.ckpt',
    evaluation_mode='nli_sp'      # options: 'nli_sp', 'nli', 'bin_sp', 'bin'
)

# contexts = source texts, claims = generated texts
scores = scorer.score(
    contexts=['The capital of France is Paris.'],
    claims=['Paris is the capital of France.']
)
# Returns list of floats in [0, 1]
```

**Evaluation modes:**
- `nli` / `bin` -- 3-way NLI head / binary classification head
- `nli_sp` / `bin_sp` -- same but with chunk-sentence splitting (recommended for longer texts)
- `nli_sp` is the default and recommended setting

---

## 5. Suitability for General Text Quality (not just factual consistency)

**Not suitable as a general text quality metric.** AlignScore is specifically designed and trained for factual consistency -- measuring whether claim information aligns with context information. It does **not** measure:
- Fluency / naturalness / grammaticality
- Coherence or discourse structure
- Stylistic quality or readability
- Overall generation quality in an open-ended sense

Additionally, it has known robustness issues (fragile to entity perturbations involving names/numbers). For a contamination detection study where you need an independent text quality signal, AlignScore alone would be insufficient.

---

## 6. Alternatives for Text Quality / Naturalness Measurement

Here are metrics more suitable as independent quality indicators for a contamination study:

### Distribution-level metrics

| Metric | What it measures | Installation | Notes |
|--------|-----------------|-------------|-------|
| **MAUVE** | Distributional gap between human and machine text | `pip install mauve-text` | Best for comparing populations of texts (needs ~5000 samples). Uses KL divergence in quantized GPT-2 embedding space. [github.com/krishnap25/mauve](https://github.com/krishnap25/mauve) |

```python
import mauve
out = mauve.compute_mauve(p_text=human_texts, q_text=machine_texts, device_id=0, max_text_length=256)
print(out.mauve)  # scalar in [0, 1], higher = more similar to human
```

### Instance-level metrics

| Metric | What it measures | Installation | Notes |
|--------|-----------------|-------------|-------|
| **Perplexity** (GPT-2 / other LM) | Text predictability / fluency | Built-in with `transformers` | Reference-free. Lower = more "natural" to the scoring model. Simple and widely used. |
| **BERTScore** | Semantic similarity to reference | `pip install bert-score` | Needs reference text. Good for measuring deviation from expected output. |
| **UniEval** | Multi-dimensional: coherence, fluency, naturalness, consistency | Clone from [github.com/maszhongming/UniEval](https://github.com/maszhongming/UniEval) | EMNLP 2022. Frames evaluation as Boolean QA. Can score individual dimensions separately. T5-based, ~770M params. |

### For a contamination detection experiment, recommended combination:

1. **Perplexity** (from an external LM like GPT-2 or Llama) -- reference-free, instance-level, measures fluency/naturalness. Easy to compute, well-understood.
2. **MAUVE** -- distribution-level, measures how machine-like vs human-like a set of generations is. Strong correlation with human judgments for open-ended generation.
3. **UniEval** -- if you want multi-dimensional scores (fluency, coherence, naturalness as separate signals). More informative than a single scalar but heavier to run.
4. **BERTScore** -- if you have reference texts to compare against.

AlignScore could still serve as one signal (factual consistency dimension) if your contamination study involves factual tasks, but it should not be the sole quality indicator.

---

Sources:
- [AlignScore paper (ACL Anthology)](https://aclanthology.org/2023.acl-long.634/)
- [AlignScore GitHub](https://github.com/yuh-zha/AlignScore)
- [AlignScore HuggingFace](https://huggingface.co/yzha/AlignScore)
- [MAUVE GitHub](https://github.com/krishnap25/mauve)
- [MAUVE paper (arXiv)](https://arxiv.org/abs/2102.01454)
- [UniEval GitHub](https://github.com/maszhongming/UniEval)
- [UniEval paper (ACL Anthology)](https://aclanthology.org/2022.emnlp-main.131/)
- [Reference-free Evaluation Metrics Survey (2025)](https://arxiv.org/html/2501.12011v1)
- [NVIDIA NeMo AlignScore Deployment](https://docs.nvidia.com/nemo/guardrails/latest/user-guides/advanced/align-score-deployment.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2e58c17-9c03-49ed-b94b-e62955e4c81e",
  "isSidechain": true,
  "agentId": "aac018ec7c892f4f1",
  "requestId": "req_011CbNpYQtqsN4g71r3yTNGL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af059f37-661a-43e5-87d9-6cd155821b99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "7a64af56-6cfa-429c-9571-3bdc9b88f0e6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUQL3SjQCcsJSoB5YNCGAz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 24173,
      "output_tokens": 1931,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 846
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1931,
          "cache_read_input_tokens": 24173,
          "cache_creation_input_tokens": 846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 846,
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
