# Research conversation: Search the web for "METABENCH Kipnis ICLR 2025 huggingface dataset" and "kipnis/metabench" to find the HuggingFace datas

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad745cc9da8a2f9b6.jsonl`
- **Structured JSON:** [`fb82a97da5944080b578.json`](../../sessions/fb/fb82a97da5944080b578.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-21T10:01:17.352Z_

Search the web for "METABENCH Kipnis ICLR 2025 huggingface dataset" and "kipnis/metabench" to find the HuggingFace dataset or GitHub repository for METABENCH. I need to know:
1. The exact HuggingFace dataset ID (e.g., kipnis/metabench)
2. What benchmarks are included
3. The data format (columns, structure)
4. How to load it with the `datasets` library

Also search for the METABENCH paper to confirm which benchmarks are included. Try WebSearch and WebFetch to get this information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "5b419fc2-e104-4ccf-bed5-008ca7a425ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T10:01:17.356Z_

```json
{
  "parentUuid": "5b419fc2-e104-4ccf-bed5-008ca7a425ee",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "cad84709-0d8b-49b1-b585-f1a6fde1f38d",
  "timestamp": "2026-05-21T10:01:17.356Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T10:01:20.106Z_



I'll search for the METABENCH dataset information using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cad84709-0d8b-49b1-b585-f1a6fde1f38d",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFX9mQESWAwnGhgXt65K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b3de8d4-a88c-4bcb-8d10-617f75012259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLEmSjszYrsZ9sGQWPtxGG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15205,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15205,
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

_source line 4 · 2026-05-21T10:01:20.918Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Q5tHN3paH1mdZEdJYrTqaX`</summary>

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
  "parentUuid": "7b3de8d4-a88c-4bcb-8d10-617f75012259",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFX9mQESWAwnGhgXt65K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "807b0082-4cd7-4580-9ba9-e0bf2c7e422c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLEmSjszYrsZ9sGQWPtxGG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15205,
      "cache_read_input_tokens": 0,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15205
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15205,
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

_source line 5 · 2026-05-21T10:01:20.925Z_

<details><summary>↩ Tool result · `toolu_01Q5tHN3paH1mdZEdJYrTqaX`</summary>

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
  "parentUuid": "807b0082-4cd7-4580-9ba9-e0bf2c7e422c",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "dc0ac3cb-6c83-4054-82b8-f4607f730cb4",
  "sourceToolAssistantUUID": "807b0082-4cd7-4580-9ba9-e0bf2c7e422c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T10:01:23.695Z_



Now let me search for METABENCH information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc0ac3cb-6c83-4054-82b8-f4607f730cb4",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXA2ybzFoqdVR1Xd3Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2beaeadb-c65a-47e6-806a-503fbf2a1cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4xTTFEEnu9MZHEKFuRmfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1954,
      "cache_read_input_tokens": 15205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1954,
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

_source line 7 · 2026-05-21T10:01:24.193Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019MmnAgsyhRNAJmG9R36Xqy`</summary>

```json
{
  "query": "METABENCH Kipnis ICLR 2025 huggingface dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2beaeadb-c65a-47e6-806a-503fbf2a1cb2",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXA2ybzFoqdVR1Xd3Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dac7cffc-db2e-4885-bd70-447d1195547f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4xTTFEEnu9MZHEKFuRmfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1954,
      "cache_read_input_tokens": 15205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1954,
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

_source line 8 · 2026-05-21T10:01:24.710Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WbnHEfC68HjirhgEZoQXFE`</summary>

```json
{
  "query": "kipnis/metabench huggingface datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dac7cffc-db2e-4885-bd70-447d1195547f",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXA2ybzFoqdVR1Xd3Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5be2cb1-3efa-4bb5-b8f2-b09d985516e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4xTTFEEnu9MZHEKFuRmfW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1954,
      "cache_read_input_tokens": 15205,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1954,
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

_source line 9 · 2026-05-21T10:01:25.168Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E9xMHacxVoNgKrdogvsytp`</summary>

```json
{
  "query": "METABENCH paper benchmarks LLM evaluation redundancy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5be2cb1-3efa-4bb5-b8f2-b09d985516e2",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXA2ybzFoqdVR1Xd3Wo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2956942-87c8-4151-ad5b-1262264746d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4xTTFEEnu9MZHEKFuRmfW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1954,
      "cache_read_input_tokens": 15205,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1954
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 176,
          "cache_read_input_tokens": 15205,
          "cache_creation_input_tokens": 1954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1954,
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

_source line 10 · 2026-05-21T10:01:33.943Z_

<details><summary>↩ Tool result · `toolu_01WbnHEfC68HjirhgEZoQXFE`</summary>

```text
Web search results for query: "kipnis/metabench huggingface datasets"

Links: [{"title":"Paper page - metabench -- A Sparse Benchmark to Measure General Ability in Large Language Models","url":"https://huggingface.co/papers/2407.12844"},{"title":"GitHub - adkipnis/metabench: A principled reduction of six benchmarks from the Open LLM Leaderboard to a single sparse benchmark. · GitHub","url":"https://github.com/adkipnis/metabench"},{"title":"HCAI/metabench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HCAI/metabench"},{"title":"metabench A Sparse Benchmark to Measure General Ability in Large Language Models","url":"https://arxiv.org/html/2407.12844v1"},{"title":"metabench A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://arxiv.org/html/2407.12844v2"},{"title":"Datasets – Hugging Face","url":"https://huggingface.co/datasets"},{"title":"METABENCH A SPARSE BENCHMARK OF REASONING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf"},{"title":"[2407.12844] metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://arxiv.org/abs/2407.12844"},{"title":"HCAI/metabench · Discussions","url":"https://huggingface.co/datasets/HCAI/metabench/discussions"},{"title":"GitHub - huggingface/datasets: 🤗 The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools","url":"https://github.com/huggingface/datasets"}]

## Summary of Search Results

I found information about the kipnis/metabench Hugging Face dataset. Here are the key findings:

### About Metabench

Metabench is a sparse benchmark derived from six large language model benchmarks, capturing the essential abilities with high accuracy and efficiency. It was created using data from more than 5000 LLMs to identify the most informative items from six benchmarks: ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande (with 28,632 items in total).

### Key Features

The sparse benchmark has less than 3% of the original size of all six benchmarks combined. The estimators can be used to reconstruct each original individual benchmark score with, on average, 1.5% root mean square error (RMSE), reconstruct the original total score with 0.8% RMSE, and have a single underlying common factor whose Spearman correlation with the total score is r = 0.93.

### Access and Availability

The benchmark is available on www.huggingface.co/datasets/HCAI/metabench. The benchmark is hosted as a dataset on HuggingFace and is integrated in EleutherAI's lm-evaluation-harness, a unified framework for evaluating language models on a range of tasks.

### Source Code

All reported analyses and results are available on https://github.com/adkipnis/metabench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5be2cb1-3efa-4bb5-b8f2-b09d985516e2",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "acb5ad14-d8cf-4de3-a641-18401af3f358",
  "sourceToolAssistantUUID": "b5be2cb1-3efa-4bb5-b8f2-b09d985516e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T10:01:37.923Z_

<details><summary>↩ Tool result · `toolu_019MmnAgsyhRNAJmG9R36Xqy`</summary>

```text
Web search results for query: "METABENCH Kipnis ICLR 2025 huggingface dataset"

Links: [{"title":"Published as a conference paper at ICLR 2025 ME TABENCH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf"},{"title":"metabench A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://arxiv.org/html/2407.12844v2"},{"title":"GitHub - adkipnis/metabench: A principled reduction of six benchmarks from the Open LLM Leaderboard to a single sparse benchmark. · GitHub","url":"https://github.com/adkipnis/metabench"},{"title":"GitHub - MMKE-Bench-ICLR/MMKE-Bench: 【ICLR 2025 🔥】MMKE-Bench, a challenging benchmark for evaluating diverse semantic editing in real-world scenarios.","url":"https://github.com/MMKE-Bench-ICLR/MMKE-Bench"},{"title":"cuijiaxing/ICLR_2025_Accepted_Papers · Datasets at Hugging Face","url":"https://huggingface.co/datasets/cuijiaxing/ICLR_2025_Accepted_Papers/viewer/default/train?p=2"},{"title":"metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/4ebc26584810a189ef1e4f173aba4319-Abstract-Conference.html"},{"title":"griffin/iclr2025_data_scores · Datasets at Hugging Face","url":"https://huggingface.co/datasets/griffin/iclr2025_data_scores"},{"title":"HCAI/metabench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HCAI/metabench/viewer"},{"title":"[2407.12844] metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://arxiv.org/abs/2407.12844"},{"title":"Navigating Dataset Documentations in AI: A Large-Scale Analysis of   Dataset Cards on Hugging Face","url":"https://arxiv.org/pdf/2401.13822"}]

Based on the search results, I found information about METABENCH, which is an ICLR 2025 paper by Kipnis and colleagues:

## Overview

METABENCH distills six benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande) to less than 3% of their original size. The research identifies that there exists a small set of common underlying abilities that these benchmarks measure, and items tap into redundant information.

## Key Results

After distilling all six benchmarks to a total of 858 items, the latent abilities estimated by the reduced set can reconstruct each normalized benchmark score with an average of 1.24% root mean squared error (RMSE) on the test split.

## Dataset Access

The benchmark is available at www.huggingface.co/datasets/HCAI/metabench, and analyses and results can be viewed on www.github.com/adkipnis/metabench. Additionally, the benchmark is integrated in EleutherAI's lm-evaluation-harness.

The paper was published at ICLR 2025 and authored by Alex Kipnis and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dac7cffc-db2e-4885-bd70-447d1195547f",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "c3341b1d-0ac3-4bbd-845e-9059ff156d44",
  "sourceToolAssistantUUID": "dac7cffc-db2e-4885-bd70-447d1195547f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T10:01:38.105Z_

<details><summary>↩ Tool result · `toolu_01E9xMHacxVoNgKrdogvsytp`</summary>

```text
Web search results for query: "METABENCH paper benchmarks LLM evaluation redundancy"

Links: [{"title":"[Literature Review] metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://www.themoonlight.io/en/review/metabench-a-sparse-benchmark-of-reasoning-and-knowledge-in-large-language-models"},{"title":"metabench A Sparse Benchmark of Reasoning and Knowledge in Large Language Models","url":"https://arxiv.org/html/2407.12844v2"},{"title":"metabench A Sparse Benchmark to Measure General Ability in Large Language Models","url":"https://arxiv.org/html/2407.12844v1"},{"title":"Redundancy Principles for MLLMs Benchmarks | Request PDF","url":"https://www.researchgate.net/publication/394298581_Redundancy_Principles_for_MLLMs_Benchmarks"},{"title":"Rethinking LLM Evaluation: Can We Evaluate LLMs with 200× Less Data?","url":"https://arxiv.org/html/2510.10457v1"},{"title":"Preprint. Under review. RETHINKING LLM EVALUATION: CAN WE EVALUATE","url":"https://arxiv.org/pdf/2510.10457"},{"title":"MetaBench: A Multi-task Benchmark for Assessing LLMs in Metabolomics","url":"https://arxiv.org/pdf/2510.14944"}]

Based on the search results, here's what I found about the METABENCH paper on benchmarks and LLM evaluation redundancy:

## Overview

The paper titled "Sparse Benchmark of Reasoning and Knowledge in Large Language Models" introduces metabench, a new, compact benchmark derived from a comprehensive analysis of six existing benchmarks: ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande.

## Purpose and Motivation

The primary aim of this work is to highlight the redundancy in existing benchmarks and to distill a more efficient evaluation tool that retains essential information regarding LLMs' reasoning and knowledge capabilities. These benchmarks often measure overlapping skills, leading to redundancy and inefficiency.

## Methodology

The authors gathered item-wise accuracy data from over 5000 LLMs using responses submitted to the Open LLM Leaderboard, yielding 6875 unique models and over 152 million responses. The metabench framework leverages psychometric techniques to estimate the latent abilities captured by these benchmarks.

## Key Results

The use of latent abilities enables accurate reconstruction of individual and total benchmark scores, as well as the original ranking: metabench retains the evaluative power of the original, larger benchmarks while reducing redundancy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2956942-87c8-4151-ad5b-1262264746d4",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "1a0b725c-eec0-4e62-8fc5-9c884fa9fa9a",
  "sourceToolAssistantUUID": "d2956942-87c8-4151-ad5b-1262264746d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T10:01:42.098Z_

Good, I found the key information. The dataset is at `HCAI/metabench`. Let me now fetch the HuggingFace dataset page and the GitHub repo for detailed structure information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a0b725c-eec0-4e62-8fc5-9c884fa9fa9a",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXBJ8hj9WiHikUB9Sgq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cf3bf34-bc06-4e8f-955d-39c56f09b8f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XewGPXMZiiMJWAQaZGDp6C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 17159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2698,
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

_source line 14 · 2026-05-21T10:01:44.556Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014zKj184apSGGCE4zcjPtA4`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HCAI/metabench",
  "prompt": "Extract all information about this dataset: 1) The exact dataset ID, 2) All available subsets/configs, 3) Column names and data types, 4) How to load it with the datasets library (any code examples), 5) Which benchmarks are included, 6) Number of rows/items, 7) Any metadata about the dataset format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf3bf34-bc06-4e8f-955d-39c56f09b8f7",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXBJ8hj9WiHikUB9Sgq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "096d8734-d2c1-4c8b-a4bd-b1b762c3ab77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XewGPXMZiiMJWAQaZGDp6C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 17159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2698,
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

_source line 15 · 2026-05-21T10:01:46.082Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VyWWNEUYcbVUG89zAfkDrE`</summary>

```json
{
  "url": "https://github.com/adkipnis/metabench",
  "prompt": "Extract: 1) What benchmarks are included in metabench, 2) How is the data structured, 3) How to load the dataset, 4) Any code examples for using the dataset, 5) The item selection methodology, 6) Total number of items in the sparse benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "096d8734-d2c1-4c8b-a4bd-b1b762c3ab77",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXBJ8hj9WiHikUB9Sgq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6499568-3cdd-408c-bdb5-21663e28fc88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XewGPXMZiiMJWAQaZGDp6C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2698,
      "cache_read_input_tokens": 17159,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2698
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 17159,
          "cache_creation_input_tokens": 2698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2698,
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

_source line 16 · 2026-05-21T10:01:52.116Z_

<details><summary>↩ Tool result · `toolu_01VyWWNEUYcbVUG89zAfkDrE`</summary>

```text
# Metabench Dataset Overview

## 1) Included Benchmarks
The sparse benchmark consolidates six benchmarks from the Open LLM Leaderboard: "ARC, GSM8K, HellaSwag, MMLU, TruthfulQA and WinoGrande."

## 2) Data Structure
The repository contains item-wise accuracies collected from over 5,000 LLMs across these six benchmarks. Data is organized in folders for analysis, scraping scripts, and evaluation results.

## 3) Loading the Dataset
Complete datasets are available on Zenodo. Users should "download and extract `data.tar.gz` to `data` inside your `.../metabench/` directory" to reproduce results.

## 4) Code Examples
To test an LLM using metabench:
- Step 1: Evaluate using lm-evaluation-harness with the `metabench{version}{permute}` task specification
- Step 2: Reconstruct full scores by running `Rscript reconstruct.R {model_id} {ver} {per}`

## 5) Item Selection Methodology
The project employs item response theory (IRT) analysis. The process involves removing low-variance items, cross-validated subsampling to 350 items per benchmark, fitting IRT models, and selecting the most informative items based on item parameters.

## 6) Total Items in Sparse Benchmark
The repository reduces the original benchmark "to less than 3% of its original size" but doesn't explicitly state the final item count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6499568-3cdd-408c-bdb5-21663e28fc88",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "ef253afe-66fa-48d0-b104-6d636f7d09c9",
  "sourceToolAssistantUUID": "b6499568-3cdd-408c-bdb5-21663e28fc88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T10:01:52.240Z_

<details><summary>↩ Tool result · `toolu_014zKj184apSGGCE4zcjPtA4`</summary>

````text
# MetaBench Dataset Information

## 1. Dataset ID
**HCAI/metabench**

## 2. Available Subsets
- ARC (245 rows)
- GSM8K (486 rows)
- HellaSwag (151 rows)
- MMLU (198 rows)
- TruthfulQA (290 rows)
- Winogrande (239 rows)

## 3. Splits
- **primary** (145 rows)
- **secondary** (100 rows)

## 4. Column Names and Data Types

**Core columns:**
- `id` (string, 8-22 characters)
- `question` (string, 28-501 characters)
- `choices` (dict)
- `answerKey` (string, 6 values)
- `metabench_idx` (int64, 7-1.17k)
- `alltwentyfiveshot_longprompt` (string, 3.42k-5.98k characters)

**Few-shot columns** (repeated for shots 1-20+):
- `arc_idx_shot_X` (int64)
- `arc_question_shot_X` (string)
- `arc_choices_shot_X` (dict)
- `arc_answerKey_shot_X` (string)

## 5. Loading with Datasets Library

```python
from datasets import load_dataset

# Load entire dataset
dataset = load_dataset("HCAI/metabench")

# Load specific subset
dataset = load_dataset("HCAI/metabench", "ARC")

# Load specific split
dataset = load_dataset("HCAI/metabench", "ARC", split="primary")
```

## 6. Benchmarks Included
- **ARC** (AI2 Reasoning Challenge)
- **GSM8K** (Grade School Math)
- **HellaSwag**
- **MMLU** (Massive Multitask Language Understanding)
- **TruthfulQA**
- **Winogrande**

## 7. Total Rows/Items
**Total: 1,209 rows** (across all subsets)

## 8. Dataset Metadata

| Property | Value |
|----------|-------|
| **Format** | Parquet |
| **Modalities** | Tabular, Text |
| **Size Category** | 1K - 10K rows |
| **Libraries** | Datasets, pandas, Croissant |
| **ArXiv** | 2407.12844 |
| **Organization** | Helmholtz Institute for Human-Centered AI |
| **Status** | Auto-converted to Parquet |
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "096d8734-d2c1-4c8b-a4bd-b1b762c3ab77",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "6e700079-adf2-43ca-8b1f-147846fb2a5b",
  "sourceToolAssistantUUID": "096d8734-d2c1-4c8b-a4bd-b1b762c3ab77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T10:01:55.280Z_

Now let me get more detail on the data format by checking the dataset viewer for one specific subset.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e700079-adf2-43ca-8b1f-147846fb2a5b",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXCLVcPvNogxkLfbWoL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e1cc987-7801-47c4-b8a8-987875898b97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwiXutnikZPJZGafULHEp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 387,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 19857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1020,
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

_source line 19 · 2026-05-21T10:01:56.752Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XH8Eu1te9ZuZhWjGw93Paa`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HCAI/metabench/viewer/ARC/primary",
  "prompt": "Extract the exact column names, data types, and show sample data rows. What are all the columns? What does the data look like?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e1cc987-7801-47c4-b8a8-987875898b97",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXCLVcPvNogxkLfbWoL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec069dd9-ab16-429b-ae52-36f91920601e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwiXutnikZPJZGafULHEp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 387,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 19857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1020,
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

_source line 20 · 2026-05-21T10:01:57.261Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M3BDKUrMiMhR7RayNJmVtL`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HCAI/metabench/viewer/GSM8K/primary",
  "prompt": "Extract the exact column names and data types for the GSM8K subset. What columns exist? Show sample values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec069dd9-ab16-429b-ae52-36f91920601e",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXCLVcPvNogxkLfbWoL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0835c551-c414-4160-ab49-509e73699b2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BuwiXutnikZPJZGafULHEp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 387,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 19857,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 387,
          "output_tokens": 245,
          "cache_read_input_tokens": 19857,
          "cache_creation_input_tokens": 1020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1020,
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

_source line 21 · 2026-05-21T10:02:02.045Z_

<details><summary>↩ Tool result · `toolu_01XH8Eu1te9ZuZhWjGw93Paa`</summary>

````text
I appreciate your request, but I need to let you know that the web page content you've provided appears to be truncated or incomplete. The actual dataset information (column names, data types, and sample rows) isn't visible in what was shared.

To help you extract the exact column names, data types, and sample data from the HCAI/metabench dataset on Hugging Face, I would need:

1. **The full page content** showing the dataset preview/table
2. **Or direct access** to the dataset documentation

## What you can do:

**Visit the dataset directly:**
```
https://huggingface.co/datasets/HCAI/metabench
```

**Load the dataset programmatically:**
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("HCAI/metabench")

# Inspect structure
print(dataset)
print(dataset['train'].column_names)
print(dataset['train'][0])  # Sample row
```

**Get detailed info:**
```python
# See data types and features
print(dataset['train'].features)

# View multiple rows
for i, row in enumerate(dataset['train'].take(3)):
    print(f"Row {i}: {row}")
```

Could you please share the complete web page content or let me know which specific split/configuration of the metabench dataset you're interested in? That way I can provide accurate column names and data type information.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec069dd9-ab16-429b-ae52-36f91920601e",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "a600e638-dff2-4dde-a7d7-30f6c042d7bb",
  "sourceToolAssistantUUID": "ec069dd9-ab16-429b-ae52-36f91920601e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T10:02:04.453Z_

<details><summary>↩ Tool result · `toolu_01M3BDKUrMiMhR7RayNJmVtL`</summary>

````text
# GSM8K Subset Columns and Data Types

Based on the web page content, here are the columns for the **GSM8K subset** (486 rows):

## Column Names and Data Types

| Column Name | Data Type | Description |
|---|---|---|
| `question` | `stringlengths 87..713` | The math problem question |
| `answer` | `stringlengths 61..932` | The solution with step-by-step working |
| `metabench_idx` | `int64` | Index identifier (range: 3-1.32k) |
| `allfiveshot_longprompt` | `stringlengths 1.91k..4.81k` | Five-shot prompt variant |
| `gsm8k_idx_shot_1` through `gsm8k_idx_shot_5` | `int64` | Index references for 5 example shots |
| `gsm8k_prompt_shot_1` through `gsm8k_prompt_shot_5` | `stringlengths` | The actual prompt text for each of 5 shots |
| `gsm8k_answer_shot_1` through `gsm8k_answer_shot_5` | `stringlengths` | The answer for each of 5 shots |

## Sample Values

**Question:**
```
"A factory uses robots to manufacture batteries. For each battery that is made, 
it takes a robot 6 minutes to gather the materials for the battery and 9 minutes 
to create the battery. If the factory has 10 robots working on batteries at the 
same time, how many batteries can the robots manufacture in 5 hours?"
```

**Answer:**
```
"For each battery that a robot makes, it takes 9 + 6 = <<9+6=15>>15 minutes 
to create the battery. In 60 minutes, one robot can make 60 / 15 = <<60/15=4>>4 
batteries per hour. If the factory uses 10 robots at the same time, then they can 
produce 10 * 4 = <<10*4=40>>40 batteries per hour..."
```

The dataset includes **5-shot learning examples** for each primary question, making it useful for few-shot prompting evaluation.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0835c551-c414-4160-ab49-509e73699b2c",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "174fb06c-e117-4fff-b9ff-54d901783ca5",
  "sourceToolAssistantUUID": "0835c551-c414-4160-ab49-509e73699b2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T10:02:08.450Z_

Let me also fetch the MMLU subset structure to see how it differs, and check the arxiv paper for the complete benchmark list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "174fb06c-e117-4fff-b9ff-54d901783ca5",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXDEiNoDN1iY8J7wkZJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b9d62bd-b39c-4932-b818-b3388711e552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013B19grgG8aP1VsCXFAxRy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 20877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1670,
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

_source line 24 · 2026-05-21T10:02:10.418Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UEyBZnDxh5spgiv73EXUkU`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HCAI/metabench/viewer/MMLU/primary",
  "prompt": "Extract all column names, data types, and sample values for MMLU subset. What is the exact structure?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b9d62bd-b39c-4932-b818-b3388711e552",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXDEiNoDN1iY8J7wkZJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8d99cde-6a14-486e-bf5f-62f9f293f2b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013B19grgG8aP1VsCXFAxRy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 20877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1670,
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

_source line 25 · 2026-05-21T10:02:12.009Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015YPoiJRMc4SxAqKWzsjGDo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.12844",
  "prompt": "Extract: 1) The complete list of benchmarks included in metabench, 2) The number of items selected from each benchmark, 3) The total number of items in the sparse benchmark, 4) The IRT methodology used, 5) Primary and secondary item splits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d99cde-6a14-486e-bf5f-62f9f293f2b5",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXDEiNoDN1iY8J7wkZJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b05b29a-0a5d-4563-83b3-6f343d06531f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013B19grgG8aP1VsCXFAxRy7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1670,
      "cache_read_input_tokens": 20877,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1670
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 20877,
          "cache_creation_input_tokens": 1670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1670,
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

_source line 26 · 2026-05-21T10:02:15.963Z_

<details><summary>↩ Tool result · `toolu_01UEyBZnDxh5spgiv73EXUkU`</summary>

````text
I appreciate your request, but I need to let you know that **the web page content provided appears to be truncated or incomplete**. The actual dataset details for the MMLU subset are not visible in the excerpt you've shared.

To get the exact structure of the MMLU subset from the HCAI/metabench dataset, I recommend:

## Direct Approaches:

1. **Visit the Hugging Face page directly:**
   ```
   https://huggingface.co/datasets/HCAI/metabench
   ```

2. **Use the Hugging Face `datasets` library:**
   ```python
   from datasets import load_dataset
   
   # Load the MMLU subset
   dataset = load_dataset("HCAI/metabench", "mmlu")
   
   # Inspect structure
   print(dataset.column_names)
   print(dataset.features)
   print(dataset[0])  # Sample entry
   ```

3. **Check the dataset card** on Hugging Face, which typically includes:
   - Column names and descriptions
   - Data types (string, int, etc.)
   - Sample rows
   - Full dataset statistics

## What you'll likely find:
MMLU datasets typically include columns like:
- `question` (string)
- `choices` (list of strings)
- `answer` (string/int)
- `subject` (string)

**Could you either:**
- Share the complete web page content, or
- Let me know what specific information about MMLU you need?
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8d99cde-6a14-486e-bf5f-62f9f293f2b5",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "69020ba2-7431-4d01-9431-2866da896169",
  "sourceToolAssistantUUID": "e8d99cde-6a14-486e-bf5f-62f9f293f2b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T10:02:16.385Z_

<details><summary>↩ Tool result · `toolu_015YPoiJRMc4SxAqKWzsjGDo`</summary>

```text
# Metabench Benchmark Analysis

Based on the provided content, here's what can be extracted:

## 1) Complete List of Benchmarks
The sparse benchmark includes six benchmarks: "ARC, GSM8K, HellaSwag, MMLU, TruthfulQA and WinoGrande"

## 2) Number of Items Per Benchmark
The document does not specify how many items were selected from each individual benchmark.

## 3) Total Items in Sparse Benchmark
The original combined benchmarks contained "d = 28,632 items in total." The resulting metabench represents "less than 3% of the original size," indicating the sparse benchmark contains fewer than approximately 859 items.

## 4) IRT Methodology
The abstract does not mention Item Response Theory (IRT) or any specific statistical methodology used for item selection. The document only indicates that researchers "identify the most informative items" from existing benchmarks.

## 5) Primary and Secondary Item Splits
The provided content contains no information about primary and secondary item splits or data division strategies.

**Note:** The excerpt shown appears to be the abstract and metadata page only. More detailed methodological information would likely be found in the full paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b05b29a-0a5d-4563-83b3-6f343d06531f",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "de52c943-50ca-4522-a70e-70db081e14f8",
  "sourceToolAssistantUUID": "1b05b29a-0a5d-4563-83b3-6f343d06531f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T10:02:18.761Z_

Let me get the full paper details and the HuggingFace API for exact structure information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de52c943-50ca-4522-a70e-70db081e14f8",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXE7mwNVNMhwQSe79RS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87b405d6-5a86-4992-90c2-9a69ab5c58b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015E1JFM8KMjpCY36a1dDuBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 22547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 961,
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

_source line 29 · 2026-05-21T10:02:20.225Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018YFvDm31Xiur9TdY9X2bBr`</summary>

```json
{
  "url": "https://huggingface.co/api/datasets/HCAI/metabench",
  "prompt": "Extract all configuration names (subsets), their splits, number of rows, column names, and features/schema for each config."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87b405d6-5a86-4992-90c2-9a69ab5c58b6",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXE7mwNVNMhwQSe79RS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8772c2a-61ba-47f9-bb9c-11ef013fe49b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015E1JFM8KMjpCY36a1dDuBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 22547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 961,
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

_source line 30 · 2026-05-21T10:02:22.552Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PRnw7dkYMNqyizYgSNe9W7`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.12844v2",
  "prompt": "Extract: 1) The exact number of items selected from each of the six benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande), 2) Total number of items in the sparse benchmark, 3) How primary vs secondary items are defined, 4) The IRT model used (e.g., 2PL, 3PL), 5) The factor analysis method, 6) How score reconstruction works"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8772c2a-61ba-47f9-bb9c-11ef013fe49b",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXE7mwNVNMhwQSe79RS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac4a071f-7555-43f0-909f-94ac6d2fc976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015E1JFM8KMjpCY36a1dDuBb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 22547,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 961
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 315,
          "cache_read_input_tokens": 22547,
          "cache_creation_input_tokens": 961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 961,
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

_source line 31 · 2026-05-21T10:02:24.229Z_

<details><summary>↩ Tool result · `toolu_018YFvDm31Xiur9TdY9X2bBr`</summary>

````text
# Metabench Dataset Configuration Analysis

Based on the provided metadata, here's what I can extract:

## Configuration Names & Splits

The dataset has **6 configurations** with **2 splits each** (primary and secondary):

| Config | Primary File | Secondary File |
|--------|--------------|-----------------|
| ARC | arc.parquet | arc-secondary.parquet |
| GSM8K | gsm8k.parquet | gsm8k-secondary.parquet |
| HellaSwag | hellaswag.parquet | hellaswag-secondary.parquet |
| MMLU | mmlu.parquet | mmlu-secondary.parquet |
| TruthfulQA | truthfulqa.parquet | truthfulqa-secondary.parquet |
| Winogrande | winogrande.parquet | winogrande-secondary.parquet |

## Available Information

✅ **Configuration names**: All 6 are listed above
✅ **Splits**: Primary and secondary for each
✅ **Total test items**: 858 (combined metabench set)

## Not Available in Metadata

❌ **Row counts per split**: Not specified in the JSON metadata
❌ **Column names**: Not provided in the metadata
❌ **Schema/Features**: Not defined in the metadata

## To Get Full Schema Details

You would need to:

```python
from datasets import load_dataset

# Load a specific configuration
ds = load_dataset("HCAI/metabench", name="ARC")
print(ds.schema)  # View full schema
print(ds["primary"].info)  # View split info
```

The metadata page at https://huggingface.co/datasets/HCAI/metabench should contain complete schema documentation.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8772c2a-61ba-47f9-bb9c-11ef013fe49b",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "c4eb34fd-cc68-4c3a-838a-eb442034c101",
  "sourceToolAssistantUUID": "e8772c2a-61ba-47f9-bb9c-11ef013fe49b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T10:02:30.116Z_

<details><summary>↩ Tool result · `toolu_01PRnw7dkYMNqyizYgSNe9W7`</summary>

```text
# Metabench: Sparse Benchmark Composition and Methods

## Items Selected Per Benchmark

The researchers selected the following number of items from each benchmark:
- **ARC**: 145 items
- **GSM8K**: 237 items
- **HellaSwag**: 93 items
- **MMLU**: 96 items
- **TruthfulQA**: 154 items
- **WinoGrande**: 133 items

## Total Benchmark Size

The combined sparse benchmark contains **858 items**, representing "less than 3% of the original size of all six benchmarks combined" (approximately 28,632 original items).

## Primary vs. Secondary Items

The paper does not explicitly define "primary" versus "secondary" items. Instead, it uses an **information filtering approach** where items are selected based on Fisher information functions that quantify "how informative an item is about a test taker's ability."

## IRT Models Used

The researchers employed three IRT models and selected the best performer per benchmark:
- "2PL model, a 3PL model with an additional lower asymptote parameter, a 4PL model with an additional upper asymptote parameter"

Most benchmarks used the 3PL model, with ARC and GSM8K using 4PL and 2PL respectively.

## Factor Analysis Method

The authors applied factor analysis to latent abilities using "the psych package" and found "a single factor is sufficient to capture 79.3% of the total variability across latent abilities."

## Score Reconstruction Process

Reconstruction involves three steps: (1) IRT models estimate latent abilities from sparse benchmark responses; (2) Generalized Additive Models (GAMs) predict original scores using these latent abilities plus sparse subtest scores; (3) The joint model leverages information across all six benchmarks simultaneously, achieving "1.24% root mean squared error" for individual benchmarks and "0.58%" for the grand average score.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac4a071f-7555-43f0-909f-94ac6d2fc976",
  "isSidechain": true,
  "promptId": "5fd83662-3773-4ed3-b143-950c2bc1cad2",
  "agentId": "ad745cc9da8a2f9b6",
  "type": "user",
  "uuid": "91e6bce6-a60e-4b2e-b94b-376f84431094",
  "sourceToolAssistantUUID": "ac4a071f-7555-43f0-909f-94ac6d2fc976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T10:02:57.729Z_

Now I have comprehensive information. Here is the complete summary:

---

## METABENCH Dataset

### 1. HuggingFace Dataset ID

**`HCAI/metabench`**

(Not `kipnis/metabench` -- it is under the Helmholtz Center for Human-Centered AI organization.)

### 2. Benchmarks Included

Six benchmarks from the Open LLM Leaderboard, with the following number of items selected for the sparse benchmark:

| Benchmark | Items Selected (primary) | Original Size | IRT Model Used |
|-----------|------------------------|---------------|----------------|
| ARC | 145 | ~7,787 | 4PL |
| GSM8K | 237 | ~8,792 | 2PL |
| HellaSwag | 93 | ~10,042 | 3PL |
| MMLU | 96 | ~14,042 | 3PL |
| TruthfulQA | 154 | ~817 | 3PL |
| WinoGrande | 133 | ~1,267 | 3PL |
| **Total** | **858** | **~28,632** | |

858 items total = less than 3% of the originals.

### 3. Data Format

**6 configs** (one per benchmark), each with **2 splits**: `primary` and `secondary`.

Row counts per config (primary + secondary combined):
- ARC: 245 rows
- GSM8K: 486 rows
- HellaSwag: 151 rows
- MMLU: 198 rows
- TruthfulQA: 290 rows
- Winogrande: 239 rows

**Column structure varies by benchmark but follows a pattern:**

For **ARC** (multiple-choice):
- `id` (string) -- item identifier
- `question` (string) -- the question text
- `choices` (dict) -- answer choices
- `answerKey` (string) -- correct answer key
- `metabench_idx` (int64) -- index in the original benchmark
- `alltwentyfiveshot_longprompt` (string) -- 25-shot prompt
- `arc_idx_shot_X`, `arc_question_shot_X`, `arc_choices_shot_X`, `arc_answerKey_shot_X` -- few-shot example columns (X = 1..25)

For **GSM8K** (math/free-form):
- `question` (string) -- math problem
- `answer` (string) -- step-by-step solution
- `metabench_idx` (int64) -- index in original benchmark
- `allfiveshot_longprompt` (string) -- 5-shot prompt
- `gsm8k_idx_shot_X`, `gsm8k_prompt_shot_X`, `gsm8k_answer_shot_X` -- few-shot columns (X = 1..5)

Format is **Parquet**, with modalities listed as tabular + text.

### 4. How to Load

```python
from datasets import load_dataset

# Load all splits of a specific benchmark
ds = load_dataset("HCAI/metabench", "ARC")
# ds["primary"] -- 145 items (the core sparse benchmark)
# ds["secondary"] -- 100 items (backup/secondary items)

# Load just the primary split
arc_primary = load_dataset("HCAI/metabench", "ARC", split="primary")

# Load all benchmarks
for bench in ["ARC", "GSM8K", "HellaSwag", "MMLU", "TruthfulQA", "Winogrande"]:
    ds = load_dataset("HCAI/metabench", bench, split="primary")
    print(f"{bench}: {len(ds)} items, columns: {ds.column_names}")
```

The benchmark is also integrated into **EleutherAI's lm-evaluation-harness** as a task.

### Key Methodology Notes

- Uses Item Response Theory (IRT) with 2PL/3PL/4PL models to identify the most informative items
- A single latent factor captures 79.3% of variability across all six benchmark abilities
- Score reconstruction uses IRT ability estimates + Generalized Additive Models (GAMs)
- Reconstructs individual benchmark scores with ~1.24% RMSE and grand average with ~0.58% RMSE
- Paper: arXiv 2407.12844, published at ICLR 2025
- GitHub: `adkipnis/metabench`

Sources:
- [HCAI/metabench on HuggingFace](https://huggingface.co/datasets/HCAI/metabench)
- [GitHub: adkipnis/metabench](https://github.com/adkipnis/metabench)
- [arXiv: 2407.12844](https://arxiv.org/abs/2407.12844)
- [ICLR 2025 paper PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- [Full HTML paper (v2)](https://arxiv.org/html/2407.12844v2)
- [HuggingFace paper page](https://huggingface.co/papers/2407.12844)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91e6bce6-a60e-4b2e-b94b-376f84431094",
  "isSidechain": true,
  "agentId": "ad745cc9da8a2f9b6",
  "requestId": "req_011CbFXF9RgkKw46zUhUSqgg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7816e843-7e03-4ff1-8591-eaea9f2258f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "a9db0c01-5081-4ae7-ab4d-0c75df0b7a32",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RamSkaWpG58HCUZRzJKemu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1241,
      "cache_read_input_tokens": 23508,
      "output_tokens": 1337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1241
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1337,
          "cache_read_input_tokens": 23508,
          "cache_creation_input_tokens": 1241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1241,
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
