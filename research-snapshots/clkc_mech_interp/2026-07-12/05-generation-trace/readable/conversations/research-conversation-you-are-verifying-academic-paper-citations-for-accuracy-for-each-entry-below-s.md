# Research conversation: You are verifying academic paper citations for accuracy. For each entry below, search the web (use WebSearch) to verify:

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a75fdddb311138678.jsonl`
- **Structured JSON:** [`7a21b98612fd79047f82.json`](../../sessions/7a/7a21b98612fd79047f82.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

55 recorded events

### User

_source line 1 · 2026-05-26T11:07:53.530Z_

You are verifying academic paper citations for accuracy. For each entry below, search the web (use WebSearch) to verify: (1) paper exists, (2) authors are correct, (3) year is correct, (4) title is correct, (5) venue is correct. Search for "paper title + first author last name" or the arXiv ID if given.

Report findings in this format for each entry:
```
KEY: [status OK/WARNING/ERROR]
- Real: [true/false]
- Authors: [correct/error description]
- Year: [correct/error description]  
- Title: [correct/error description]
- Venue: [correct/error description]
```

Here are the entries to verify:

1. `feng2026finegrained` — Feng, Zihao and Li, Tian and Zhu, Zhengyu and Zhou, Hao and Qian, Junliang and Zhang, Lin and Mao, Kede. "Fine-Grained Activation Steering: Steering Less, Achieving More". ICLR 2026. arXiv:2602.04428

2. `xing2024evaluating` — Xing, Xiaoling and He, Zhenhui and Xu, Huiyun and Wang, Xin and Wang, Rui and Hong, Yu. "Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models". arXiv:2407.01358, year 2024.

3. `sundar2025steering` — Sundar, Anirudh and Williamson, Sinead and Metcalf, Katherine and Theobald, Barry-John and Zhao, Skyler and Jurafsky, Dan. "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models". ACL 2025. arXiv:2502.15639

4. `ifergan2024beneath` — Ifergan, Matan and Choshen, Leshem and Aharoni, Roee and Szpektor, Idan and Abend, Omri. "Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs". Findings NAACL 2025. Year listed as 2024. arXiv:2408.10646

5. `marks2024geometry` — Marks, Samuel and Tegmark, Max. "The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets". ICLR 2024 (listed as 2024 but booktitle says "13th ICLR"). arXiv:2310.06824

6. `li2025taming` — Li, Gaotang and Chen, Yufei and Tong, Hanghang. "Taming Knowledge Conflicts in Language Models". ICML 2025. arXiv:2503.10996

7. `pham2026where` — Pham, Minh Vu and Borkakoty, Hrishav and Hou, Yufang. "Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models". arXiv:2601.09445, year 2026.

8. `wang2025lost` — Wang, Mingyang and Adel, Heike and Lange, Lukas and Strötgen, Jannik and Schütze, Hinrich. "Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models". ACL 2025. arXiv:2504.04264

Search for each one individually. Be thorough — check arXiv pages and any official venue pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "bfce0f56-21c5-4820-9f64-a7175e17edb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-26T11:07:53.556Z_

```json
{
  "parentUuid": "bfce0f56-21c5-4820-9f64-a7175e17edb9",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
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
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b8ffd1af-525d-4194-8307-297af444f400",
  "timestamp": "2026-05-26T11:07:53.556Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-26T11:07:56.357Z_



I'll search for each paper individually using WebSearch. Let me start by loading the tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8ffd1af-525d-4194-8307-297af444f400",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5GvWNZD3USUxM3riJ5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29ef216a-39df-4f8d-8be0-04f4aeab142d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vjyjnZGWPc6gq4TMaNq2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7459,
      "cache_read_input_tokens": 8247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7459,
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

_source line 4 · 2026-05-26T11:07:56.539Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Pn8nKMvb9AZRYaM54DbcMj`</summary>

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
  "parentUuid": "29ef216a-39df-4f8d-8be0-04f4aeab142d",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5GvWNZD3USUxM3riJ5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "523221db-0e8a-4a7b-a8eb-4363c59bcb10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vjyjnZGWPc6gq4TMaNq2u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7459,
      "cache_read_input_tokens": 8247,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 8247,
          "cache_creation_input_tokens": 7459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7459,
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

_source line 5 · 2026-05-26T11:07:56.546Z_

<details><summary>↩ Tool result · `toolu_01Pn8nKMvb9AZRYaM54DbcMj`</summary>

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
  "parentUuid": "523221db-0e8a-4a7b-a8eb-4363c59bcb10",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "16150dd9-a2d5-42a4-bfec-62c562626d5b",
  "sourceToolAssistantUUID": "523221db-0e8a-4a7b-a8eb-4363c59bcb10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-26T11:07:59.592Z_



Now let me search for all 8 papers. I'll batch them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16150dd9-a2d5-42a4-bfec-62c562626d5b",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5H9PXBfGY3bgzkqWXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c52bd625-3a5f-4380-822e-8bb1ee7dd335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zkwZzt7J2WCcLaBz5r5ku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 15706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 7 · 2026-05-26T11:08:00.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ki94fsovBzWUjYUQ2Ypai7`</summary>

```json
{
  "query": "arXiv 2602.04428 \"Fine-Grained Activation Steering\" Feng"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c52bd625-3a5f-4380-822e-8bb1ee7dd335",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5H9PXBfGY3bgzkqWXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50913b3c-b399-487d-8c39-20fa2346eb29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zkwZzt7J2WCcLaBz5r5ku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 15706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 8 · 2026-05-26T11:08:00.552Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JkXFbGFzULSsjJSVeUnskV`</summary>

```json
{
  "query": "arXiv 2407.01358 \"Evaluating Knowledge-based Cross-lingual Inconsistency\" Xing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50913b3c-b399-487d-8c39-20fa2346eb29",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5H9PXBfGY3bgzkqWXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7c80ae0-4acf-4b5c-b458-51002f21b49a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zkwZzt7J2WCcLaBz5r5ku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 15706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
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

_source line 9 · 2026-05-26T11:08:01.123Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EjfVxdqE9bCFRxcM5G72tg`</summary>

```json
{
  "query": "arXiv 2502.15639 \"Steering into New Embedding Spaces\" Sundar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7c80ae0-4acf-4b5c-b458-51002f21b49a",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5H9PXBfGY3bgzkqWXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b4ab671-3a22-4bb3-8e46-b8b92df53585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zkwZzt7J2WCcLaBz5r5ku",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 15706,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 15706,
          "cache_creation_input_tokens": 1461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1461,
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

### Tool call

_source line 10 · 2026-05-26T11:08:01.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Xv1n8tSVYozxeD8CwtCq9`</summary>

```json
{
  "query": "arXiv 2408.10646 \"Beneath the Surface of Consistency\" Ifergan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b4ab671-3a22-4bb3-8e46-b8b92df53585",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5H9PXBfGY3bgzkqWXW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8626bf20-d084-4603-a92f-62db18ae9b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014zkwZzt7J2WCcLaBz5r5ku",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 15706,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 15706,
          "cache_creation_input_tokens": 1461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1461,
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

_source line 11 · 2026-05-26T11:08:09.307Z_

<details><summary>↩ Tool result · `toolu_01EjfVxdqE9bCFRxcM5G72tg`</summary>

```text
Web search results for query: "arXiv 2502.15639 "Steering into New Embedding Spaces" Sundar"

Links: [{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/html/2502.15639v1"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment","url":"https://arxiv.org/pdf/2502.15639"},{"title":"[Literature Review] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://www.themoonlight.io/en/review/steering-into-new-embedding-spaces-analyzing-cross-lingual-alignment-induced-by-model-interventions-in-multilingual-language-models"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://www.researchgate.net/publication/389274280_Steering_into_New_Embedding_Spaces_Analyzing_Cross-Lingual_Alignment_Induced_by_Model_Interventions_in_Multilingual_Language_Models"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - Paper Detail","url":"https://deeplearn.org/arxiv/621970/steering-into-new-embedding-spaces:-analyzing-cross-lingual-alignment-induced-by-model-interventions-in-multilingual-language-models"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - haebom","url":"https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=4w67rj24qd1v4m5yq8ep"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.118/"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/steering-into-new-embedding-spaces-analyzing-cross"}]

I found the paper you're looking for! Here's what I found:

arXiv paper 2502.15639 is titled "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models" by Anirudh Sundar and 5 other authors.

**Key Details:**

The paper addresses aligned representations across languages in multilingual large language models (mLLMs), which is desirable for improving cross-lingual task performance, though typically alignment requires computationally expensive fine-tuning and sizable language data that may not be available.

**Main Contribution:**

The authors propose model interventions—a data-efficient alternative to fine-tuning that manipulates model activations to steer generation into the desired direction—and analyze the effect of a popular intervention called "finding experts" on cross-lingual representation alignment in mLLMs.

**Results:**

The research shows that modifying the mLLM's activations changes its embedding space such that cross-lingual alignment is enhanced, with these changes translating into improved downstream performance on retrieval tasks with up to 2x improvement.

The paper was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics in Vienna, Austria.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b4ab671-3a22-4bb3-8e46-b8b92df53585",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "efd9671a-0c64-4084-8611-b6ab3876b314",
  "sourceToolAssistantUUID": "0b4ab671-3a22-4bb3-8e46-b8b92df53585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T11:08:09.494Z_

<details><summary>↩ Tool result · `toolu_01JkXFbGFzULSsjJSVeUnskV`</summary>

```text
Web search results for query: "arXiv 2407.01358 "Evaluating Knowledge-based Cross-lingual Inconsistency" Xing"

Links: [{"title":"[2407.01358] Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/abs/2407.01358"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2407.01358v1"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/evaluating-knowledge-based-cross-lingual-inconsistency-large"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://www.researchgate.net/publication/381882496_Evaluating_Knowledge-based_Cross-lingual_Inconsistency_in_Large_Language_Models"},{"title":"dblp: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2407-01358.html"},{"title":"Understanding Cross-Lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2505.13141v1"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/html/2504.04264v1"},{"title":"[2309.08952] Cross-Lingual Knowledge Editing in Large Language Models","url":"https://arxiv.org/abs/2309.08952"}]

Based on the search results, I found the paper you're looking for:

**Title:** Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models

**Paper ID:** arXiv:2407.01358

**Authors:** Xiaolin Xing, Zhiwei He, Haoyu Xu, Xing Wang, Rui Wang, Yu Hong

**Submission Date:** July 1, 2024

**Overview:** The paper investigates the cross-lingual inconsistencies observed in Large Language Models (LLMs), such as ChatGPT, Llama, and Baichuan, which have shown exceptional performance in various Natural Language Processing (NLP) tasks. Despite their successes, these models often exhibit significant inconsistencies when processing the same concepts across different languages.

**Methodology:** The study proposes an innovative evaluation method for Cross-lingual Semantic Consistency (xSC) using the LaBSE model, and introduces metrics for Cross-lingual Accuracy Consistency (xAC) and Cross-lingual Timeliness Consistency (xTC) to comprehensively assess the models' performance regarding semantic, accuracy, and timeliness inconsistencies.

The full paper is available on arXiv at https://arxiv.org/abs/2407.01358.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7c80ae0-4acf-4b5c-b458-51002f21b49a",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "3bed565d-1b00-42eb-b74a-cfaf2019c4c9",
  "sourceToolAssistantUUID": "d7c80ae0-4acf-4b5c-b458-51002f21b49a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T11:08:09.662Z_

<details><summary>↩ Tool result · `toolu_01Ki94fsovBzWUjYUQ2Ypai7`</summary>

```text
Web search results for query: "arXiv 2602.04428 "Fine-Grained Activation Steering" Feng"

Links: [{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/html/2602.04428"},{"title":"FINE-GRAINED ACTIVATION STEERING","url":"https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More | OpenReview","url":"https://openreview.net/forum?id=guSVafqhrB"},{"title":"Steering to Say No: Configurable Refusal via Activation Steering in Vision Language Models","url":"https://arxiv.org/html/2602.07013v1"},{"title":"Activation Steering with a Feedback Controller","url":"https://arxiv.org/pdf/2510.04309"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169v1"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv:2602.04428)

**Key Authors:** Zijian Feng and colleagues from Nanyang Technological University, Singapore

**Main Contributions:**

The paper addresses activation steering as a cost-effective approach for modifying large language model behaviors, but reveals that existing block-level intervention methods steer bundled activations of attention heads, feedforward networks, or residual streams.

The authors show that block-level activations are heterogeneous, mixing beneficial, irrelevant, and harmful features, so they decompose block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation.

Methodologically, they propose AUSteer, a framework that localizes discriminative AUs with activation momenta for steering and ensures adaptivity across diverse inputs and AUs.

The paper evaluates AUSteer on multiple LLMs across diverse tasks including commonsense reasoning, mathematical problem solving, and open-ended generation, showing that with less intrusive intervention, AUSteer significantly outperforms other state-of-the-art activation steering methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50913b3c-b399-487d-8c39-20fa2346eb29",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "05fa7410-8381-4dfd-8214-b19b746082b7",
  "sourceToolAssistantUUID": "50913b3c-b399-487d-8c39-20fa2346eb29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T11:08:10.287Z_

<details><summary>↩ Tool result · `toolu_012Xv1n8tSVYozxeD8CwtCq9`</summary>

```text
Web search results for query: "arXiv 2408.10646 "Beneath the Surface of Consistency" Ifergan"

Links: [{"title":"[2408.10646] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646"},{"title":"[2408.10646v1] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646v1"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/html/2408.10646.pdf"},{"title":"[PDF] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beneath-the-Surface-of-Consistency:-Exploring-in-Ifergan-Choshen/54a2e0dad730c1a955c66f3568a3fa0dca400225"},{"title":"(PDF) Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://www.researchgate.net/publication/383266358_Beneath_the_Surface_of_Consistency_Exploring_Cross-lingual_Knowledge_Representation_Sharing_in_LLMs"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge","url":"https://arxiv.org/pdf/2408.10646"},{"title":"Computation and Language Aug 2024","url":"https://arxiv.org/list/cs.CL/2024-08?skip=540&show=2000"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs - Paper Detail","url":"https://deeplearn.org/arxiv/519856/beneath-the-surface-of-consistency:-exploring-cross-lingual-knowledge-representation-sharing-in-llms"}]

I found the paper! Here's what I can tell you about arXiv 2408.10646:

**Title:** "Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs"

**Authors:** Maxim Ifergan, Leshem Choshen, Roee Aharoni, Idan Szpektor, and Omri Abend from the Hebrew University of Jerusalem and Google Research

**Submitted:** August 20, 2024

**Key Research Question:** Language models are inconsistent in their ability to answer the same factual question across languages, raising questions about how LLMs represent a given fact across languages.

**Main Findings:**
- High consistency does not necessarily imply shared representation, particularly for languages with different scripts
- Script similarity is a dominant factor in representation sharing

**Methodology:** The researchers propose editing factual knowledge in one language and examining the effects on other languages, employing three knowledge editing techniques: ROME and MEMIT locate-and-edit methods, and a finetuning-based method. They compiled CLIKE, a multilingual "fill-in-the-blank" factual knowledge probing dataset with 35k samples across 13 languages with 7 scripts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8626bf20-d084-4603-a92f-62db18ae9b01",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "6b119c52-1ef6-4a60-8056-7c7b9f504fad",
  "sourceToolAssistantUUID": "8626bf20-d084-4603-a92f-62db18ae9b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T11:08:13.525Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WhVbQZZcYE43JFF5sUQGpf`</summary>

```json
{
  "query": "arXiv 2310.06824 \"The Geometry of Truth\" Marks Tegmark ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b119c52-1ef6-4a60-8056-7c7b9f504fad",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5J9v3jDvWLeg9iXjnj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "280f71b8-00b8-4b9c-95fd-82e93c56edc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsH9wRFZrF4sVuge4uRADm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 17167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3604,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 16 · 2026-05-26T11:08:14.618Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Byt7vpvq9dJUXBEiu6SgMg`</summary>

```json
{
  "query": "arXiv 2503.10996 \"Taming Knowledge Conflicts in Language Models\" Li Gaotang ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "280f71b8-00b8-4b9c-95fd-82e93c56edc8",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5J9v3jDvWLeg9iXjnj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89d5b784-a80d-4da4-bfad-c71b1b33fb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsH9wRFZrF4sVuge4uRADm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 17167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3604,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 17 · 2026-05-26T11:08:15.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bvt7s3FSLD22QWEYaQZfcF`</summary>

```json
{
  "query": "arXiv 2601.09445 \"Where Knowledge Collides\" Pham mechanistic knowledge conflict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89d5b784-a80d-4da4-bfad-c71b1b33fb4d",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5J9v3jDvWLeg9iXjnj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0db1b793-a11f-407a-a6a1-2112f29d1595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsH9wRFZrF4sVuge4uRADm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 17167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3604,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 18 · 2026-05-26T11:08:15.904Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AmsYNXU89Vyp14ayc3qqiR`</summary>

```json
{
  "query": "arXiv 2504.04264 \"Lost in Multilinguality\" Wang Mingyang cross-lingual factual inconsistency ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0db1b793-a11f-407a-a6a1-2112f29d1595",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5J9v3jDvWLeg9iXjnj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02e47b1e-e043-418d-93d9-1b3da0f9f43a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsH9wRFZrF4sVuge4uRADm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3604,
      "cache_read_input_tokens": 17167,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3604
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 17167,
          "cache_creation_input_tokens": 3604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3604,
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

_source line 19 · 2026-05-26T11:08:22.219Z_

<details><summary>↩ Tool result · `toolu_01WhVbQZZcYE43JFF5sUQGpf`</summary>

```text
Web search results for query: "arXiv 2310.06824 "The Geometry of Truth" Marks Tegmark ICLR 2024"

Links: [{"title":"[2310.06824] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://arxiv.org/abs/2310.06824"},{"title":"[2310.06824v3] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://arxiv.org/abs/2310.06824v3"},{"title":"[2310.06824] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://ar5iv.labs.arxiv.org/html/2310.06824"},{"title":"arXiv:2310.06824v2 [cs.AI] 8 Dec 2023","url":"https://arxiv.org/pdf/2310.06824"},{"title":"Paper page - The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://huggingface.co/papers/2310.06824"},{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://arxiv.org/html/2310.06824v2/"},{"title":"[PDF] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Geometry-of-Truth:-Emergent-Linear-Structure-in-Marks-Tegmark/d59523889679aee15992c4bf6e52b134186d07d3"},{"title":"Probing the Geometry of Truth: Consistency and Generalization of Truth Directions in LLMs Across Logical Transformations and Question Answering Tasks","url":"https://arxiv.org/html/2506.00823v1"}]

Based on the search results, here's what I found about this paper:

## Overview

The paper "The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets" was authored by Samuel Marks and Max Tegmark.

## Publication Details

The paper was published as a conference paper at COLM 2024 (note: the search results indicate publication at COLM 2024, not ICLR 2024 as mentioned in your query). The paper was initially submitted on October 10, 2023, with the final version (v3) revised on August 19, 2024.

## Main Contribution

The work uses high-quality datasets of simple true/false statements to study the structure of LLM representations of truth, drawing on three lines of evidence: visualizations of LLM true/false statement representations which reveal clear linear structure, transfer experiments in which probes trained on one dataset generalize to different datasets, and causal evidence obtained by surgically intervening in a LLM's forward pass, causing it to treat false statements as true and vice versa.

The research provides evidence that large language models develop linear representations of truthfulness that are generalizable and causally implicated in their outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "280f71b8-00b8-4b9c-95fd-82e93c56edc8",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "dc0d3378-08c8-4696-88f3-834910430a99",
  "sourceToolAssistantUUID": "280f71b8-00b8-4b9c-95fd-82e93c56edc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T11:08:23.304Z_

<details><summary>↩ Tool result · `toolu_01Byt7vpvq9dJUXBEiu6SgMg`</summary>

```text
Web search results for query: "arXiv 2503.10996 "Taming Knowledge Conflicts in Language Models" Li Gaotang ICML 2025"

Links: [{"title":"[2503.10996] Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/abs/2503.10996"},{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2503.10996"},{"title":"[Literature Review] Taming Knowledge Conflicts in Language Models","url":"https://www.themoonlight.io/en/review/taming-knowledge-conflicts-in-language-models"},{"title":"Task Matters: Knowledge Requirements Shape LLM Responses to Context–Memory Conflict","url":"https://arxiv.org/html/2506.06485v3"},{"title":"LLM Microscope: What Model Internals Reveal About Answer Correctness and Context Utilization","url":"https://arxiv.org/html/2510.04013v1"},{"title":"Computation and Language Mar 2025","url":"https://arxiv.org/list/cs.CL/2025-03?skip=700&show=2000"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=2800&show=250"},{"title":"LLMs Struggle to Perform Counterfactual Reasoning with Parametric Knowledge","url":"https://arxiv.org/html/2506.15732v1"},{"title":"ICML Poster Taming Knowledge Conflicts in Language Models","url":"https://icml.cc/virtual/2025/poster/46677"}]

I found the paper! Here are the key details:

**Paper Information:**
- The paper "Taming Knowledge Conflicts in Language Models" by Gaotang Li, Yuzhong Chen, and Hanghang Tong is accepted as a Spotlight presentation at ICML 2025

**Main Contribution:**
Language Models often encounter knowledge conflicts when parametric memory contradicts contextual knowledge. The study uncovers a critical phenomenon called the superposition of contextual information and parametric memory, where highly influential attention heads simultaneously contribute to both memory and context.

**Proposed Method:**
The authors propose Just Run Twice (JuICE), a test-time attention intervention method that steers LMs toward either parametric belief, and JuICE identifies a set of reliable attention heads and leverages a dual-run approach to mitigate the superposition effects.

**Experimental Results:**
Extensive experiments across 11 datasets and 6 model architectures demonstrate that JuICE sets the new state-of-the-art performance and robust generalization, achieving significant and consistent improvement across different domains under various conflict types.

You can access the paper directly at: https://arxiv.org/abs/2503.10996


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89d5b784-a80d-4da4-bfad-c71b1b33fb4d",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "b3c4f6dd-be43-457d-8143-56bd8d1d3319",
  "sourceToolAssistantUUID": "89d5b784-a80d-4da4-bfad-c71b1b33fb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T11:08:23.880Z_

<details><summary>↩ Tool result · `toolu_01AmsYNXU89Vyp14ayc3qqiR`</summary>

```text
Web search results for query: "arXiv 2504.04264 "Lost in Multilinguality" Wang Mingyang cross-lingual factual inconsistency ACL 2025"

Links: [{"title":"[2504.04264] Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/abs/2504.04264"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/html/2504.04264v1"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models | Request PDF","url":"https://www.researchgate.net/publication/390569381_Lost_in_Multilinguality_Dissecting_Cross-lingual_Factual_Inconsistency_in_Transformer_Language_Models"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.253/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Lost+in+Multilinguality:+Dissecting+Cross-lingual+Factual+Inconsistency+in+Transformer+Language+Models."},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models | alphaXiv","url":"https://www.alphaxiv.org/ja/overview/2504.04264v1"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual ...","url":"https://aclanthology.org/2025.acl-long.253.pdf"},{"title":"Mingyang Wang's Post","url":"https://www.linkedin.com/posts/mingyang-wang-873a7a221_thrilled-to-share-that-our-paper-lost-activity-7331251327236255745-JrTB"}]

I found the paper you're looking for! Here's what I found:

## "Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models"

**Paper Details:**
- Authors: Mingyang Wang, Heike Adel, Lukas Lange, Yihong Liu, Ercong Nie, Jannik Strötgen, and Hinrich Schuetze. Published in 2025 in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5075–5094, Vienna, Austria.
- arXiv identifier: 2504.04264
- Posted to arXiv on April 5, 2025

**Summary:**
The paper addresses the challenge that multilingual language models store factual knowledge across languages but often struggle to provide consistent responses to semantically equivalent prompts in different languages. 

**Key Findings:**
- The work uses mechanistic interpretability methods to investigate cross-lingual inconsistencies in MLMs and finds that MLMs encode knowledge in a language-independent concept space through most layers, and only transition to language-specific spaces in the final layers.
- Failures during the language transition often result in incorrect predictions in the target language, even when the answers are correct in other languages.
- To address this issue, the authors propose a linear shortcut method that bypasses computations in the final layers, enhancing both prediction accuracy and cross-lingual consistency.

The paper is available on [arXiv](https://arxiv.org/abs/2504.04264) and the [ACL Anthology](https://aclanthology.org/2025.acl-long.253/).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02e47b1e-e043-418d-93d9-1b3da0f9f43a",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "8b1407d2-2146-4dba-96ff-4343626e2f98",
  "sourceToolAssistantUUID": "02e47b1e-e043-418d-93d9-1b3da0f9f43a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T11:08:26.983Z_

<details><summary>↩ Tool result · `toolu_01Bvt7s3FSLD22QWEYaQZfcF`</summary>

```text
Web search results for query: "arXiv 2601.09445 "Where Knowledge Collides" Pham mechanistic knowledge conflict"

Links: [{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/html/2601.09445"},{"title":"[2601.09445] Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/abs/2601.09445"},{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory","url":"https://arxiv.org/pdf/2601.09445"},{"title":"Cutting Off the Head Ends the Conflict: A Mechanism for Interpreting and   Mitigating Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2402.18154"},{"title":"Diagnosing Knowledge Conflict in Multimodal Long-Chain Reasoning","url":"https://arxiv.org/pdf/2602.14518"},{"title":"CC-VQA: Conflict- and Correlation-Aware Method for Mitigating Knowledge Conflict in Knowledge-Based Visual Question Answering","url":"https://arxiv.org/pdf/2602.23952"}]

Based on the search results, I found the paper you're looking for:

"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models" by Minh Vu Pham, Hsuvas Borkakoty, and Yufang Hou.

**Key aspects of the paper:**

The paper addresses intra-memory knowledge conflict in language models, which arises when inconsistent information about the same event is encoded within the model's parametric knowledge.

While prior work focused on resolving conflicts between a model's internal knowledge and external resources through fine-tuning or knowledge editing, this work designs a framework based on mechanistic interpretability methods to identify where and how conflicting knowledge from pre-training data is encoded within language models.

The researchers constructed a curated dataset called SynWikiBio, consisting of Wikipedia-style biographies for synthetic entities that deliberately contain conflicting knowledge (e.g., a person's graduating university).

The findings demonstrate that specific internal components of a language model are responsible for encoding conflicting knowledge from pre-training, and show how mechanistic interpretability methods can be leveraged to causally intervene in and control conflicting knowledge at inference.

The paper (arXiv:2601.09445) was submitted on January 14, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0db1b793-a11f-407a-a6a1-2112f29d1595",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "0181be40-03f4-4ff0-af88-5cfc43e6300e",
  "sourceToolAssistantUUID": "0db1b793-a11f-407a-a6a1-2112f29d1595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-26T11:08:30.424Z_

Now let me get more details on a few entries where I need to verify specific author names or venue information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0181be40-03f4-4ff0-af88-5cfc43e6300e",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5KPG1KQtx6jLJRKy5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "221973ac-aacb-4bd3-8ca2-bf19ec584cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yqD8Ceh7quJ8tVhMPPone",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 965,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 20771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2476,
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

_source line 24 · 2026-05-26T11:08:31.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QDm5b1N4rDScmQFvjjN3gz`</summary>

```json
{
  "query": "arxiv 2602.04428 authors Zihao Feng OR Zijian Feng fine-grained activation steering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221973ac-aacb-4bd3-8ca2-bf19ec584cb1",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5KPG1KQtx6jLJRKy5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81061567-c1ef-47d1-ad0d-db00ca6ef630",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yqD8Ceh7quJ8tVhMPPone",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 965,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 20771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2476,
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

_source line 25 · 2026-05-26T11:08:32.327Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012p5bqkfUtiz3mhpPKyzvuc`</summary>

```json
{
  "query": "arxiv 2407.01358 authors Xiaoling Xing OR Xiaolin Xing cross-lingual inconsistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81061567-c1ef-47d1-ad0d-db00ca6ef630",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5KPG1KQtx6jLJRKy5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8c32e20-7442-4005-a941-8c062bd51df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yqD8Ceh7quJ8tVhMPPone",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 965,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 20771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2476,
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

_source line 26 · 2026-05-26T11:08:33.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01StboeTZdqrNPiBSJQUGvTi`</summary>

```json
{
  "query": "\"The Geometry of Truth\" Marks Tegmark COLM 2024 venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8c32e20-7442-4005-a941-8c062bd51df6",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5KPG1KQtx6jLJRKy5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec3bd5ef-3997-479b-99fa-55ac2eef4baa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yqD8Ceh7quJ8tVhMPPone",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 965,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 20771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2476,
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

_source line 27 · 2026-05-26T11:08:34.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018uzaszu3Vq5cd2QeS7Ek8r`</summary>

```json
{
  "query": "arxiv 2408.10646 Ifergan \"Matan\" OR \"Maxim\" \"Beneath the Surface\" NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec3bd5ef-3997-479b-99fa-55ac2eef4baa",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5KPG1KQtx6jLJRKy5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d1c7589-806d-4677-a8e1-3d05607005a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014yqD8Ceh7quJ8tVhMPPone",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 965,
      "cache_creation_input_tokens": 2476,
      "cache_read_input_tokens": 20771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2476,
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

_source line 28 · 2026-05-26T11:08:41.423Z_

<details><summary>↩ Tool result · `toolu_01StboeTZdqrNPiBSJQUGvTi`</summary>

```text
Web search results for query: ""The Geometry of Truth" Marks Tegmark COLM 2024 venue conference"

Links: [{"title":"The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | OpenReview","url":"https://openreview.net/forum?id=aajyHYjjsk"},{"title":"COLM.2024 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/COLM.2024"},{"title":"Published as a conference paper at COLM 2024","url":"https://openreview.net/attachment?id=aajyHYjjsk&name=pdf"},{"title":"[2310.06824] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://arxiv.org/abs/2310.06824"},{"title":"DetectingAlignmentFakingLLMwithSAEprobes.md · GitHub","url":"https://gist.github.com/bigsnarfdude/1bf43279ea0741b2facfabfb00962899"},{"title":"Probing the Geometry of Truth: Consistency and ...","url":"https://aclanthology.org/2025.findings-acl.38.pdf"},{"title":"The Geometry of Truth: Emergent Linear Structure in Large ...","url":"https://www.deepdyve.com/lp/arxiv-cornell-university/the-geometry-of-truth-emergent-linear-structure-in-large-language-pxqZ4eKRWA"},{"title":"[2310.06824v3] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets","url":"https://arxiv.org/abs/2310.06824v3"},{"title":"[PDF] The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Geometry-of-Truth:-Emergent-Linear-Structure-in-Marks-Tegmark/d59523889679aee15992c4bf6e52b134186d07d3"}]

Based on the search results, I found information about "The Geometry of Truth" by Marks and Tegmark at COLM 2024. However, the search results do not specify the venue/location where the COLM 2024 conference took place. Here's what I found:

"The Geometry of Truth: Emergent Linear Structure in LLM Representations of True/False Datasets" was published as a conference paper at COLM 2024, authored by Samuel Marks from Northeastern University and Max Tegmark from MIT.

The paper investigates LLM representations of true/false factual statements. The research includes visualizations of LLM representations revealing clear linear structure, transfer experiments where probes trained on one dataset generalize to different datasets, and causal evidence obtained by surgically intervening in an LLM's forward pass.

Unfortunately, the search results don't include the specific conference venue (location/city) for COLM 2024. If you need that information, I can search for it specifically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec3bd5ef-3997-479b-99fa-55ac2eef4baa",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "63990542-d503-4d77-a7a2-6a2a880229c8",
  "sourceToolAssistantUUID": "ec3bd5ef-3997-479b-99fa-55ac2eef4baa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T11:08:41.758Z_

<details><summary>↩ Tool result · `toolu_012p5bqkfUtiz3mhpPKyzvuc`</summary>

```text
Web search results for query: "arxiv 2407.01358 authors Xiaoling Xing OR Xiaolin Xing cross-lingual inconsistency"

Links: [{"title":"[2407.01358] Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/abs/2407.01358"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2407.01358v1"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://www.researchgate.net/publication/381882496_Evaluating_Knowledge-based_Cross-lingual_Inconsistency_in_Large_Language_Models"},{"title":"dblp: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2407-01358.html"},{"title":"Understanding Cross-Lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2505.13141v1"},{"title":"Understanding Cross-Lingual Inconsistency in Large Language Models - Paper Detail","url":"https://deeplearn.org/arxiv/606317/understanding-cross-lingual-inconsistency-in-large-language-models"},{"title":"[2504.04264] Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/abs/2504.04264"},{"title":"[2605.12515] Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation","url":"https://arxiv.org/abs/2605.12515"},{"title":"Understanding Cross-Lingual Inconsistency in Large ...","url":"https://arxiv.org/pdf/2505.13141"}]

I found the paper! Here are the details about arxiv 2407.01358:

**Title:** Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models

**Authors:** Xiaolin Xing, Zhiwei He, Haoyu Xu, Xing Wang, Rui Wang, Yu Hong

**Submission Date:** July 1, 2024

**Summary:** This paper investigates the cross-lingual inconsistencies observed in Large Language Models (LLMs), such as ChatGPT, Llama, and Baichuan. Despite their successes, these models often exhibit significant inconsistencies when processing the same concepts across different languages.

**Key Focus:** The study focuses on three primary questions: the existence of cross-lingual inconsistencies in LLMs, the specific aspects in which these inconsistencies manifest, and the correlation between cross-lingual consistency and multilingual capabilities of LLMs. The paper proposes an innovative evaluation method for Cross-lingual Semantic Consistency (xSC) using the LaBSE model, and introduces metrics for Cross-lingual Accuracy Consistency (xAC) and Cross-lingual Timeliness Consistency (xTC).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8c32e20-7442-4005-a941-8c062bd51df6",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "a5e8e824-a10c-4351-96d1-5a08d11920f0",
  "sourceToolAssistantUUID": "a8c32e20-7442-4005-a941-8c062bd51df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T11:08:41.861Z_

<details><summary>↩ Tool result · `toolu_01QDm5b1N4rDScmQFvjjN3gz`</summary>

```text
Web search results for query: "arxiv 2602.04428 authors Zihao Feng OR Zijian Feng fine-grained activation steering"

Links: [{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/html/2602.04428"},{"title":"Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:","url":"https://openreview.net/pdf?id=guSVafqhrB"},{"title":"FINE-GRAINED ACTIVATION STEERING","url":"https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"},{"title":"Activation Steering with a Feedback Controller","url":"https://arxiv.org/pdf/2510.04309"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=550&show=2000"},{"title":"STEERING LANGUAGE MODELS WITH ACTIVATION EN","url":"https://openreview.net/notes/edits/attachment?id=91L4QwqDov&name=pdf"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=1500&show=2000"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2510.25117"},{"title":"Steer2Edit: From Activation Steering to Component-Level Editing","url":"https://arxiv.org/pdf/2602.09870"}]

I found the paper! Here's the information about arxiv 2602.04428:

**Paper Title:** Fine-Grained Activation Steering: Steering Less, Achieving More

**Lead Author:** Zijian Feng

**Authors:** Zijian Feng, Tianjiao Li, Zixiao Zhu, Hanzhang Zhou, Junlang Qian, Li Zhang, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, and Kezhi Mao

**Key Contributions:**

The paper reveals that block-level activations are inherently heterogeneous, entangling beneficial, irrelevant, and harmful features. They decompose block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation.

The authors propose AUSteer, a method that operates at the AU level. AUSteer identifies discriminative AUs globally by computing activation momenta on contrastive samples, then assigns adaptive steering strengths tailored to diverse inputs and selected AU activations.

The paper demonstrates that AUSteer consistently surpasses advanced baselines while steering considerably fewer activations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81061567-c1ef-47d1-ad0d-db00ca6ef630",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "f37a37b7-0ae0-4182-97cd-961e0b9de96b",
  "sourceToolAssistantUUID": "81061567-c1ef-47d1-ad0d-db00ca6ef630",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T11:08:43.369Z_

<details><summary>↩ Tool result · `toolu_018uzaszu3Vq5cd2QeS7Ek8r`</summary>

```text
Web search results for query: "arxiv 2408.10646 Ifergan "Matan" OR "Maxim" "Beneath the Surface" NAACL 2025"

Links: [{"title":"[2408.10646] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646"},{"title":"[2408.10646v1] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646v1"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/html/2408.10646.pdf"},{"title":"(PDF) Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://www.researchgate.net/publication/383266358_Beneath_the_Surface_of_Consistency_Exploring_Cross-lingual_Knowledge_Representation_Sharing_in_LLMs"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge","url":"https://arxiv.org/pdf/2408.10646"},{"title":"InferES : A Natural Language Inference Corpus for Spanish Featuring   Negation-Based Contrastive and Adversarial Examples","url":"https://arxiv.org/pdf/2210.03068"},{"title":"FaBERT: Pre-training BERT on Persian Blogs","url":"https://arxiv.org/pdf/2402.06617"},{"title":"Entailed Between the Lines: Incorporating Implication into NLI","url":"https://arxiv.org/pdf/2501.07719"},{"title":"Right for the Wrong Reasons: Diagnosing Syntactic Heuristics in Natural   Language Inference","url":"https://arxiv.org/pdf/1902.01007"}]

I found the paper! Here's what I found based on your search:

The paper "Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs" is authored by Maxim Ifergan and 4 other authors. The full author list includes Maxim Ifergan, Leshem Choshen, Roee Aharoni, Idan Szpektor, and Omri Abend, affiliated with The Hebrew University of Jerusalem and Google Research.

The paper explores how language models are inconsistent in their ability to answer the same factual question across languages, even though the veracity of a factoid is largely independent of the language it is written in. The researchers explore multilingual factual knowledge through the model's ability to answer queries consistently across languages and to store answers in a shared representation, proposing a methodology to measure the extent of representation sharing across languages by repurposing knowledge editing methods.

Key findings reveal that high consistency does not necessarily imply shared representation, particularly for languages with different scripts, and script similarity is a dominant factor in representation sharing.

The paper was published on arXiv on August 20, 2024 (arXiv:2408.10646).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d1c7589-806d-4677-a8e1-3d05607005a0",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "bccb9aec-7437-4934-9489-e091d0fe9a05",
  "sourceToolAssistantUUID": "0d1c7589-806d-4677-a8e1-3d05607005a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-26T11:08:45.779Z_

Let me get a few more details to verify specific author names and venue information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bccb9aec-7437-4934-9489-e091d0fe9a05",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5LbWjPmqa3fwBMEaa6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89f2f0b4-e3ea-4a9a-980d-e05936960515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiXDhrU4BSHGAYt4hoycPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4478,
      "cache_read_input_tokens": 23247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4478,
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

_source line 33 · 2026-05-26T11:08:46.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NQWP9dC7kXvDXWZc6NqyXE`</summary>

```json
{
  "query": "site:arxiv.org/abs/2602.04428 fine-grained activation steering authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89f2f0b4-e3ea-4a9a-980d-e05936960515",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5LbWjPmqa3fwBMEaa6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b21bee8-6a65-427d-a8d9-c10534114548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiXDhrU4BSHGAYt4hoycPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4478,
      "cache_read_input_tokens": 23247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4478,
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

_source line 34 · 2026-05-26T11:08:47.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DxRLVk2Tr5dvEMFdFNagcZ`</summary>

```json
{
  "query": "site:arxiv.org/abs/2407.01358 authors Xiaolin Xing Zhenhui He Huiyun Xu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b21bee8-6a65-427d-a8d9-c10534114548",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5LbWjPmqa3fwBMEaa6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f671a490-bfb7-4445-b912-bab7f0961752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiXDhrU4BSHGAYt4hoycPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4478,
      "cache_read_input_tokens": 23247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4478,
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

_source line 35 · 2026-05-26T11:08:47.913Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FfUcFDNAgz4pFJWRiv1BQo`</summary>

```json
{
  "query": "\"Beneath the Surface of Consistency\" Ifergan NAACL 2025 Findings accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f671a490-bfb7-4445-b912-bab7f0961752",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5LbWjPmqa3fwBMEaa6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "870ff685-6ac0-4f7e-b7b4-24449249288c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiXDhrU4BSHGAYt4hoycPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4478,
      "cache_read_input_tokens": 23247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4478,
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

_source line 36 · 2026-05-26T11:08:49.490Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014YSun4ngm86852moy8aKYH`</summary>

```json
{
  "query": "arxiv 2601.09445 Pham Borkakoty Hou \"Where Knowledge Collides\" authors Hrishav OR Hsuvas"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "870ff685-6ac0-4f7e-b7b4-24449249288c",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5LbWjPmqa3fwBMEaa6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4672a4d0-beaf-4eda-aa5e-e3268aaec5b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiXDhrU4BSHGAYt4hoycPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4478,
      "cache_read_input_tokens": 23247,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4478
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 23247,
          "cache_creation_input_tokens": 4478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4478,
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

_source line 37 · 2026-05-26T11:08:53.629Z_

<details><summary>↩ Tool result · `toolu_01NQWP9dC7kXvDXWZc6NqyXE`</summary>

```text
Web search results for query: "site:arxiv.org/abs/2602.04428 fine-grained activation steering authors"

Links: [{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"Weight Updates as Activation Shifts: A Principled Framework for Steering","url":"https://arxiv.org/pdf/2603.00425"},{"title":"Interpretable Steering of Large Language Models with Feature Guided   Activation Additions","url":"https://arxiv.org/pdf/2501.09929"},{"title":"Fusion Steering: Prompt-Specific Activation Control","url":"https://arxiv.org/pdf/2505.22572"},{"title":"SteerVLM: Robust Model Control through Lightweight Activation Steering for Vision Language Models","url":"https://arxiv.org/pdf/2510.26769"},{"title":"Activation Steering with a Feedback Controller","url":"https://arxiv.org/pdf/2510.04309"}]

Based on the search results, I found the paper on arXiv. The authors of "Fine-Grained Activation Steering: Steering Less, Achieving More" are Zijian Feng, Tianjiao Li, Zixiao Zhu, Hanzhang Zhou, Junlang Qian, Li Zhang, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, and Kezhi Mao.

The paper is from the School of Electrical and Electronic Engineering at Nanyang Technological University, Singapore, and the Home Team Science and Technology Agency (HTX), Singapore.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b21bee8-6a65-427d-a8d9-c10534114548",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "c41176eb-d206-4512-a87d-5e36785ce2d4",
  "sourceToolAssistantUUID": "2b21bee8-6a65-427d-a8d9-c10534114548",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T11:08:54.871Z_

<details><summary>↩ Tool result · `toolu_01DxRLVk2Tr5dvEMFdFNagcZ`</summary>

```text
Web search results for query: "site:arxiv.org/abs/2407.01358 authors Xiaolin Xing Zhenhui He Huiyun Xu"

Links: [{"title":"[2407.01358] Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/abs/2407.01358"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=200&show=2000"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=500&show=1000"},{"title":"Computer Science Jul 2024","url":"https://www.arxiv.org/list/cs/2024-07?skip=1900&show=2000"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/pastweek?skip=156&show=1000"},{"title":"Computer Vision and Pattern Recognition Mar 2025","url":"https://arxiv.org/list/cs.CV/2025-03?skip=1200&show=2000"},{"title":"Computer Vision and Pattern Recognition Apr 2025","url":"https://www.arxiv.org/list/cs.CV/2025-04?skip=1200&show=1000"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=225&show=2000"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=300&show=2000"},{"title":"Artificial Intelligence - cs.AI","url":"https://www.arxiv.org/list/cs.AI/recent?skip=159&show=500"}]

Based on the search results, I found the paper you were looking for:

The paper is titled "Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models" and is authored by Xiaolin Xing and 5 other authors.

The paper investigates cross-lingual inconsistencies observed in Large Language Models such as ChatGPT, Llama, and Baichuan, which have shown exceptional performance in various Natural Language Processing tasks but often exhibit significant inconsistencies when processing the same concepts across different languages.

The study proposes an innovative evaluation method for Cross-lingual Semantic Consistency using the LaBSE model, and introduces metrics for Cross-lingual Accuracy Consistency and Cross-lingual Timeliness Consistency to comprehensively assess the models' performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f671a490-bfb7-4445-b912-bab7f0961752",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "3bdebc70-ebfc-472e-93dd-639435c44ac2",
  "sourceToolAssistantUUID": "f671a490-bfb7-4445-b912-bab7f0961752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T11:08:56.715Z_

<details><summary>↩ Tool result · `toolu_01FfUcFDNAgz4pFJWRiv1BQo`</summary>

```text
Web search results for query: ""Beneath the Surface of Consistency" Ifergan NAACL 2025 Findings accepted"

Links: [{"title":"[PDF] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beneath-the-Surface-of-Consistency:-Exploring-in-Ifergan-Choshen/54a2e0dad730c1a955c66f3568a3fa0dca400225"},{"title":"[2408.10646] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646"},{"title":"[2408.10646v1] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646v1"},{"title":"(PDF) Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://www.researchgate.net/publication/383266358_Beneath_the_Surface_of_Consistency_Exploring_Cross-lingual_Knowledge_Representation_Sharing_in_LLMs"},{"title":"Consistency in Language Models: Current Landscape, Challenges, and Future Directions","url":"https://arxiv.org/pdf/2505.00268"}]

Based on the search results, I found information about the paper "Beneath the Surface of Consistency" by Ifergan and colleagues. However, the results show this paper was posted to arXiv in August 2024, not specifically indicating it as an accepted NAACL 2025 Findings paper.

The paper examines LLMs with various multilingual configurations using a new multilingual dataset and reveals that high consistency does not necessarily imply shared representation, particularly for languages with different scripts, and finds that script similarity is a dominant factor in representation sharing.

The work explores multilingual factual knowledge through two aspects: the model's ability to answer a query consistently across languages, and the ability to "store" answers in a shared representation for several languages, proposing a methodology to measure the extent of representation sharing across languages by repurposing knowledge editing methods.

The paper has authors Maxim Ifergan, Leshem Choshen, Roee Aharoni, Idan Szpektor, and Omri Abend. However, the search results do not explicitly confirm its acceptance to NAACL 2025 Findings. If you need specific confirmation about the NAACL 2025 acceptance status, you may want to check the official NAACL conference website or proceedings directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "870ff685-6ac0-4f7e-b7b4-24449249288c",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "60b103ba-6710-4927-b1fc-503f10a64be6",
  "sourceToolAssistantUUID": "870ff685-6ac0-4f7e-b7b4-24449249288c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T11:08:58.048Z_

<details><summary>↩ Tool result · `toolu_014YSun4ngm86852moy8aKYH`</summary>

```text
Web search results for query: "arxiv 2601.09445 Pham Borkakoty Hou "Where Knowledge Collides" authors Hrishav OR Hsuvas"

Links: [{"title":"[2601.09445] Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/abs/2601.09445"},{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/html/2601.09445"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=1191&show=1000"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"Mathematical Physics","url":"https://arxiv.org/list/math-ph/recent?skip=32&show=250"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1399&show=2000"},{"title":"Computer Science Sep 2022","url":"https://arxiv.org/list/cs/2022-09?skip=1695&show=2000"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=4400&show=2000"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=1400&show=1000"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"}]

I found the paper you were searching for! Here are the details:

**Title:** "Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models"

**Authors:** Minh Vu Pham, Hsuvas Borkakoty, Yufang Hou

**arXiv ID:** 2601.09445

**Submission Date:** January 14, 2026

**Affiliation:** All authors are from IT:U Austria, with Yufang Hou also affiliated with IBM Research

**Overview:** The paper addresses intra-memory knowledge conflict in language models, where inconsistent information about the same event is encoded within the model's parametric knowledge. The authors design a framework based on mechanistic interpretability methods to identify where and how conflicting knowledge from pre-training data is encoded within language models.

The paper can be accessed at https://arxiv.org/abs/2601.09445


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4672a4d0-beaf-4eda-aa5e-e3268aaec5b5",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "e23ff0ec-3af3-4417-ae73-1f6dac14aaa0",
  "sourceToolAssistantUUID": "4672a4d0-beaf-4eda-aa5e-e3268aaec5b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T11:09:02.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SE8ss5rErawZSHxNyoJgw8`</summary>

```json
{
  "query": "\"Beneath the Surface of Consistency\" Ifergan aclanthology.org NAACL Findings 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e23ff0ec-3af3-4417-ae73-1f6dac14aaa0",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5Mg6apnCHsrvYUtFXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "812d8deb-8a44-46ba-98d5-bb8e3fda365a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXSt5FfzhA9s4d6nGgngmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2847,
      "cache_read_input_tokens": 27725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2847,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 42 · 2026-05-26T11:09:04.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SYB1w9QHXaFjXhJ1dFaCMT`</summary>

```json
{
  "query": "arxiv 2504.04264 \"Lost in Multilinguality\" Wang authors Yihong Liu Ercong Nie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "812d8deb-8a44-46ba-98d5-bb8e3fda365a",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5Mg6apnCHsrvYUtFXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9666028-4ea2-4d42-99ad-16b92cfda298",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXSt5FfzhA9s4d6nGgngmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2847,
      "cache_read_input_tokens": 27725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2847,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 43 · 2026-05-26T11:09:05.588Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WFykEmTdnpU9CG7BmJpK6c`</summary>

```json
{
  "query": "ICML 2025 \"Taming Knowledge Conflicts\" Li Chen Tong authors Yuzhong Chen Gaotang Li"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9666028-4ea2-4d42-99ad-16b92cfda298",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5Mg6apnCHsrvYUtFXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81045a7f-b009-4a4a-aad4-cd0307d7f351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXSt5FfzhA9s4d6nGgngmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2847,
      "cache_read_input_tokens": 27725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2847,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 44 · 2026-05-26T11:09:06.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0187ex8YijqhxbxCjDEVb5r4`</summary>

```json
{
  "query": "openreview.net \"Fine-Grained Activation Steering\" ICLR 2026 Feng authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81045a7f-b009-4a4a-aad4-cd0307d7f351",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5Mg6apnCHsrvYUtFXA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "451f525e-097a-4d15-b321-c44fbc243756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXSt5FfzhA9s4d6nGgngmu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2847,
      "cache_read_input_tokens": 27725,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 27725,
          "cache_creation_input_tokens": 2847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2847,
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

_source line 45 · 2026-05-26T11:09:12.643Z_

<details><summary>↩ Tool result · `toolu_01SE8ss5rErawZSHxNyoJgw8`</summary>

```text
Web search results for query: ""Beneath the Surface of Consistency" Ifergan aclanthology.org NAACL Findings 2025"

Links: [{"title":"[2408.10646v1] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646v1"},{"title":"[2408.10646] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646"},{"title":"[PDF] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beneath-the-Surface-of-Consistency:-Exploring-in-Ifergan-Choshen/54a2e0dad730c1a955c66f3568a3fa0dca400225"},{"title":"(PDF) Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://www.researchgate.net/publication/383266358_Beneath_the_Surface_of_Consistency_Exploring_Cross-lingual_Knowledge_Representation_Sharing_in_LLMs"},{"title":"Consistency in Language Models: Current Landscape, Challenges, and Future Directions","url":"https://arxiv.org/pdf/2505.00268"}]

Based on the search results, I found the paper "Beneath the Surface of Consistency" by Ifergan and colleagues. Here's what I found:

"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs" is authored by Maxim Ifergan and 4 other authors. 

The paper explores multilingual factual knowledge in language models. While the veracity of a factoid is largely independent of the language it is written in, language models are inconsistent in their ability to answer the same factual question across languages.

The research explores two aspects: the model's ability to answer a query consistently across languages, and the ability to store answers in a shared representation for several languages, proposing a methodology to measure the extent of representation sharing across languages by repurposing knowledge editing methods.

Key findings include: High consistency does not necessarily imply shared representation, particularly for languages with different scripts, and script similarity is a dominant factor in representation sharing.

The paper appears on arXiv (2408.10646) dated August 20, 2024. However, I did not locate it specifically on the aclanthology.org NAACL Findings 2025 venue you mentioned in your query. The search results primarily show the arXiv version and other academic databases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "812d8deb-8a44-46ba-98d5-bb8e3fda365a",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "eec79e7c-e368-463a-9c1e-9741d3970ef8",
  "sourceToolAssistantUUID": "812d8deb-8a44-46ba-98d5-bb8e3fda365a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T11:09:12.856Z_

<details><summary>↩ Tool result · `toolu_01SYB1w9QHXaFjXhJ1dFaCMT`</summary>

```text
Web search results for query: "arxiv 2504.04264 "Lost in Multilinguality" Wang authors Yihong Liu Ercong Nie"

Links: [{"title":"[2504.04264] Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/abs/2504.04264"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models","url":"https://arxiv.org/html/2504.04264v1"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models | Request PDF","url":"https://www.researchgate.net/publication/390569381_Lost_in_Multilinguality_Dissecting_Cross-lingual_Factual_Inconsistency_in_Transformer_Language_Models"},{"title":"Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.253/"},{"title":"GitHub - cisnlp/multilingual-fact-tracing: Tracing Multilingual Factual Knowledge Acquisition in Pretraining","url":"https://github.com/cisnlp/multilingual-fact-tracing"},{"title":"dblp: Mingyang Wang 0003","url":"https://dblp.org/pid/137/6768-3.html"},{"title":"Tracing Multilingual Factual Knowledge Acquisition in Pretraining - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.113/"}]

I found the paper you're looking for. Here's the information about arxiv 2504.04264:

**Title:** Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models

**Authors:** Mingyang Wang, Heike Adel, Lukas Lange, Yihong Liu, Ercong Nie, Jannik Strötgen, Hinrich Schütze

**Main Research Focus:** The paper investigates multilingual language models (MLMs) that often struggle to provide consistent responses to semantically equivalent prompts in different languages. While previous studies point out this cross-lingual inconsistency issue, the underlying causes remain unexplored. The work uses mechanistic interpretability methods to investigate cross-lingual inconsistencies in MLMs.

**Key Findings:** MLMs encode knowledge in a language-independent concept space through most layers, and only transition to language-specific spaces in the final layers. Failures during the language transition often result in incorrect predictions in the target language, even when the answers are correct in other languages.

**Proposed Solution:** The authors propose a linear shortcut method that bypasses computations in the final layers, enhancing both prediction accuracy and cross-lingual consistency.

The paper was published at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9666028-4ea2-4d42-99ad-16b92cfda298",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "7d58d43e-858c-444d-b7f8-44d52659ace3",
  "sourceToolAssistantUUID": "b9666028-4ea2-4d42-99ad-16b92cfda298",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T11:09:14.734Z_

<details><summary>↩ Tool result · `toolu_01WFykEmTdnpU9CG7BmJpK6c`</summary>

```text
Web search results for query: "ICML 2025 "Taming Knowledge Conflicts" Li Chen Tong authors Yuzhong Chen Gaotang Li"

Links: [{"title":"GitHub - GaotangLi/JUICE: [ICML'25 Spotlight] Taming Knowledge Conflict in Language Models","url":"https://github.com/GaotangLi/JUICE"},{"title":"Gaotang Li","url":"https://gaotangli.github.io/"},{"title":"ICML Poster Taming Knowledge Conflicts in Language Models","url":"https://icml.cc/virtual/2025/poster/46677"},{"title":"dblp: Gaotang Li","url":"https://dblp.org/pid/348/5271.html"},{"title":"[2503.10996] Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/abs/2503.10996"},{"title":"42nd ICML 2025: Vancouver, BC, Canada","url":"https://dblp.org/db/conf/icml/icml2025.html"},{"title":"ICML 2025 Program Committee - Meta Reviewer","url":"https://icml.cc/Conferences/2025/ProgramCommittee"},{"title":"Zhuosheng Zhang, Shanghai Jiao Tong University - BCMI Lab","url":"https://bcmi.sjtu.edu.cn/home/zhangzs/"},{"title":"ICML 2025 Orals","url":"https://icml.cc/virtual/2025/events/oral"}]

I found the paper you're looking for! Here are the search results for the ICML 2025 paper:

**Paper Details:**

The paper is titled "Taming Knowledge Conflicts in Language Models" by authors Gaotang Li, Yuzhong Chen, and Hanghang Tong, published at the Forty-second International Conference on Machine Learning (ICML) in 2025.

**Key Contribution:**

The paper addresses knowledge conflicts in Language Models when parametric memory contradicts contextual knowledge. The authors discover a phenomenon called the superposition of contextual information and parametric memory, where highly influential attention heads simultaneously contribute to both memory and context. They propose Just Run Twice (JuICE), a test-time attention intervention method that steers LMs toward either parametric beliefs or contextual knowledge without requiring fine-tuning.

**Results:**

Extensive experiments across 11 datasets and 6 model architectures demonstrate that JuICE achieves significant and consistent improvement across different domains under various conflict types.

**Resources:**

The code is available at https://github.com/GaotangLi/JUICE, and the paper has been published as an ICML 2025 spotlight paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81045a7f-b009-4a4a-aad4-cd0307d7f351",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "f5f2cc9b-4726-4425-b1fe-598bb3b39551",
  "sourceToolAssistantUUID": "81045a7f-b009-4a4a-aad4-cd0307d7f351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T11:09:18.548Z_

<details><summary>↩ Tool result · `toolu_0187ex8YijqhxbxCjDEVb5r4`</summary>

```text
Web search results for query: "openreview.net "Fine-Grained Activation Steering" ICLR 2026 Feng authors list"

Links: [{"title":"Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:","url":"https://openreview.net/pdf?id=guSVafqhrB"},{"title":"FINE-GRAINED ACTIVATION STEERING","url":"https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"},{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"Fusion Steering: Prompt-Specific Activation Control","url":"https://arxiv.org/pdf/2505.22572"}]

Based on the search results, I found the paper "Fine-Grained Activation Steering" published at ICLR 2026. The authors are: Zijian Feng, Tianjiao Li, Zixiao Zhu, Hanzhang Zhou, Junlang Qian, Li Zhang, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, and Kezhi Mao.

The authors are affiliated with the School of Electrical and Electronic Engineering at Nanyang Technological University, Singapore, and the Home Team Science and Technology Agency (HTX) in Singapore.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "451f525e-097a-4d15-b321-c44fbc243756",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "d10b0bde-e38a-4f00-aaea-5dba61a65e0a",
  "sourceToolAssistantUUID": "451f525e-097a-4d15-b321-c44fbc243756",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T11:09:21.387Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RJyCQNutvnhsgC5vZkD3WV`</summary>

```json
{
  "query": "Ifergan \"Beneath the Surface of Consistency\" Findings NAACL 2025 aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d10b0bde-e38a-4f00-aaea-5dba61a65e0a",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5PBjpcA7fstSkphwb3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ff8207a-164a-4923-9dac-a8b55acdd043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ngQ2a9E51CCoAWR64yhA8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 30572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 50 · 2026-05-26T11:09:21.967Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V2rJXqpoernJ4gKekuiTNd`</summary>

```json
{
  "query": "ACL 2025 \"Steering into New Embedding Spaces\" Sundar Williamson authors list aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ff8207a-164a-4923-9dac-a8b55acdd043",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5PBjpcA7fstSkphwb3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92329297-0ae1-4884-8150-da128298cdb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ngQ2a9E51CCoAWR64yhA8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 30572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2923,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 51 · 2026-05-26T11:09:27.775Z_

<details><summary>↩ Tool result · `toolu_01V2rJXqpoernJ4gKekuiTNd`</summary>

```text
Web search results for query: "ACL 2025 "Steering into New Embedding Spaces" Sundar Williamson authors list aclanthology"

Links: [{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.118/"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/new-embedding-spaces"},{"title":"[2502.15639] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/abs/2502.15639"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://www.researchgate.net/publication/389274280_Steering_into_New_Embedding_Spaces_Analyzing_Cross-Lingual_Alignment_Induced_by_Model_Interventions_in_Multilingual_Language_Models"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/steering-into-new-embedding-spaces-analyzing-cross"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - haebom","url":"https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=4w67rj24qd1v4m5yq8ep"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment","url":"https://arxiv.org/pdf/2502.15639"},{"title":"[Literature Review] Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://www.themoonlight.io/en/review/steering-into-new-embedding-spaces-analyzing-cross-lingual-alignment-induced-by-model-interventions-in-multilingual-language-models"},{"title":"Computation and Language Feb 2025","url":"https://arxiv.org/list/cs.CL/2025-02?skip=1325&show=2000"}]

Based on the search results, here is the authors list for the ACL 2025 paper "Steering into New Embedding Spaces":

The authors are Anirudh Sundar, Sinead Williamson, Katherine Metcalf, Barry-John Theobald, Skyler Seto, and Masha Fedzechkina.

The paper appears on the ACL Anthology at: https://aclanthology.org/2025.acl-long.118/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92329297-0ae1-4884-8150-da128298cdb3",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "ff30f447-4f11-43bf-b1d1-a43cdc1ae89f",
  "sourceToolAssistantUUID": "92329297-0ae1-4884-8150-da128298cdb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T11:09:29.499Z_

<details><summary>↩ Tool result · `toolu_01RJyCQNutvnhsgC5vZkD3WV`</summary>

```text
Web search results for query: "Ifergan "Beneath the Surface of Consistency" Findings NAACL 2025 aclanthology"

Links: [{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.475/"},{"title":"Findings of the Association for Computational Linguistics:","url":"https://aclanthology.org/2025.findings-naacl.475.pdf"},{"title":"[PDF] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beneath-the-Surface-of-Consistency:-Exploring-in-Ifergan-Choshen/54a2e0dad730c1a955c66f3568a3fa0dca400225"},{"title":"[2408.10646] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646"},{"title":"[2408.10646v1] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646v1"},{"title":"Computation and Language Aug 2024","url":"https://arxiv.org/list/cs.CL/2024-08?skip=540&show=2000"},{"title":"(PDF) Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://www.researchgate.net/publication/383266358_Beneath_the_Surface_of_Consistency_Exploring_Cross-lingual_Knowledge_Representation_Sharing_in_LLMs"}]

I found the paper! Here are the key details:

**Publication Information:**
The paper "Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs" was published in Findings of the Association for Computational Linguistics: NAACL 2025 (pages 4630–4644, Albuquerque, New Mexico).

**Authors:**
The paper is authored by Maxim Ifergan, Leshem Choshen, Roee Aharoni, Idan Szpektor, and Omri Abend.

**Main Research Question:**
While language models are inconsistent in their ability to answer the same factual question across languages, the researchers explore multilingual factual knowledge through two aspects: the model's ability to answer a query consistently across languages, and the ability to "store" answers in a shared representation for several languages.

**Key Findings:**
The work reveals that high consistency does not necessarily imply shared representation, particularly for languages with different scripts, and finds that script similarity is a dominant factor in representation sharing.

The paper is available on the ACL Anthology at: https://aclanthology.org/2025.findings-naacl.475/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ff8207a-164a-4923-9dac-a8b55acdd043",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "f9d0239b-b6a8-49d7-853c-bfb644c3b713",
  "sourceToolAssistantUUID": "9ff8207a-164a-4923-9dac-a8b55acdd043",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T11:09:33.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E8SGw4GHy7bpVyrMJK69p9`</summary>

```json
{
  "query": "aclanthology.org 2025.acl-long.118 \"Steering into New Embedding Spaces\" authors Skyler Seto OR Skyler Zhao Dan Jurafsky"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9d0239b-b6a8-49d7-853c-bfb644c3b713",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5Pzfr4nm6Pr92FDPCJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b337e4e-f176-461d-90c5-46ba1c13f1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WePNRN2MprPgj7DnzStdQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 857,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 33495,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 857,
          "output_tokens": 96,
          "cache_read_input_tokens": 33495,
          "cache_creation_input_tokens": 932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 932,
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

_source line 54 · 2026-05-26T11:09:41.463Z_

<details><summary>↩ Tool result · `toolu_01E8SGw4GHy7bpVyrMJK69p9`</summary>

```text
Web search results for query: "aclanthology.org 2025.acl-long.118 "Steering into New Embedding Spaces" authors Skyler Seto OR Skyler Zhao Dan Jurafsky"

Links: [{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.118/"},{"title":"Skyler Seto - ACL Anthology","url":"https://aclanthology.org/people/skyler-seto/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Aclanthology","url":"https://aclanthology.org/2025.acl-long.118.pdf"},{"title":"Dan Jurafsky - ACL Anthology","url":"https://aclanthology.org/people/dan-jurafsky/"},{"title":"Computation and Language Feb 2025","url":"https://arxiv.org/list/cs.CL/2025-02?skip=1325&show=2000"},{"title":"ACL 2025 The 63rd Annual Meeting of the Association for ...","url":"https://aclanthology.org/2025.acl-long.0.pdf"},{"title":"Two Decades of the ACL Anthology: Development, Impact, and Open Challenges","url":"https://people.cs.georgetown.edu/nschneid/p/aclanth.pdf"}]

I found the paper! The paper "Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models" is authored by Anirudh Sundar, Sinead Williamson, Katherine Metcalf, Barry-John Theobald, Skyler Seto, and Masha Fedzechkina. 

Note: Dan Jurafsky is not listed as an author of this paper. The paper is published at ACL 2025 (2025.acl-long.118) and shows changes to the embedding space translate into improved downstream performance on retrieval tasks, with up to 2x improvements in top-1 accuracy on cross-lingual retrieval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b337e4e-f176-461d-90c5-46ba1c13f1e8",
  "isSidechain": true,
  "promptId": "ebfa9b36-8eff-4926-aab9-19af1a4ed40f",
  "agentId": "a75fdddb311138678",
  "type": "user",
  "uuid": "f73af016-c382-4da5-b58e-159cd5cc6059",
  "sourceToolAssistantUUID": "1b337e4e-f176-461d-90c5-46ba1c13f1e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-26T11:10:11.865Z_

Now I have all the information needed. Here is the full verification report:

---

**1. `feng2026finegrained`** — Fine-Grained Activation Steering: Steering Less, Achieving More

```
KEY: feng2026finegrained [WARNING — multiple author errors]
- Real: true
- Authors: ERROR — The real authors are Zijian Feng (not "Zihao"), Tianjiao Li (not "Tian"), Zixiao Zhu (not "Zhengyu"), Hanzhang Zhou (not "Hao"), Junlang Qian (not "Junliang"), Li Zhang (not "Lin"), plus Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, and Kezhi Mao (not "Kede"). The bib entry has only 7 authors; the real paper has 10. Nearly every name is wrong or mangled.
- Year: correct (2026, arXiv Feb 2026, published ICLR 2026)
- Title: correct
- Venue: correct (ICLR 2026, confirmed on OpenReview)
```

**2. `xing2024evaluating`** — Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models

```
KEY: xing2024evaluating [WARNING — author name errors]
- Real: true
- Authors: ERROR — The real first author is Xiaolin Xing (not "Xiaoling"). The second author is Zhiwei He (not "Zhenhui"). The third author is Haoyu Xu (not "Huiyun"). Wang Xin should be Xing Wang (order of given/family may differ by convention, but the bib lists "Xin Wang" — the real name on arXiv is "Xing Wang"). Rui Wang and Yu Hong are correct.
- Year: correct (2024)
- Title: correct
- Venue: correct (arXiv preprint, no formal venue claimed)
```

**3. `sundar2025steering`** — Steering into New Embedding Spaces

```
KEY: sundar2025steering [WARNING — author list errors]
- Real: true
- Authors: ERROR — The real authors are Anirudh Sundar, Sinead Williamson, Katherine Metcalf, Barry-John Theobald, Skyler Seto (not "Skyler Zhao"), and Masha Fedzechkina. Dan Jurafsky is NOT an author of this paper; the bib entry lists him but should list Masha Fedzechkina instead. "Skyler Zhao" should be "Skyler Seto".
- Year: correct (2025)
- Title: correct
- Venue: correct (ACL 2025, confirmed on ACL Anthology 2025.acl-long.118)
```

**4. `ifergan2024beneath`** — Beneath the Surface of Consistency

```
KEY: ifergan2024beneath [WARNING — author first name error]
- Real: true
- Authors: ERROR — The first author is Maxim Ifergan (not "Matan Ifergan"). Leshem Choshen, Roee Aharoni, Idan Szpektor, and Omri Abend are correct.
- Year: correct (arXiv 2024, published 2025 at venue)
- Title: correct
- Venue: correct (Findings of NAACL 2025, confirmed on ACL Anthology 2025.findings-naacl.475)
```

**5. `marks2024geometry`** — The Geometry of Truth

```
KEY: marks2024geometry [ERROR — wrong venue]
- Real: true
- Authors: correct (Samuel Marks and Max Tegmark)
- Year: correct (2024 for the publication year)
- Title: correct
- Venue: ERROR — The paper was published at COLM 2024 (Conference on Language Modeling), NOT ICLR 2024. The bib entry says "13th ICLR" but COLM 2024 is the correct venue (confirmed on OpenReview). ICLR 2024 is the 12th edition, not the 13th — this is doubly wrong.
```

**6. `li2025taming`** — Taming Knowledge Conflicts in Language Models

```
KEY: li2025taming [WARNING — incomplete author list]
- Real: true
- Authors: ERROR — The real authors are Gaotang Li, Yuzhong Chen, and Hanghang Tong. The bib entry lists only "Li, Gaotang and Chen, Yufei and Tong, Hanghang" — the second author's name is Yuzhong Chen, not "Yufei Chen".
- Year: correct (2025)
- Title: correct
- Venue: correct (ICML 2025 Spotlight, confirmed on icml.cc)
```

**7. `pham2026where`** — Where Knowledge Collides

```
KEY: pham2026where [WARNING — author name error]
- Real: true
- Authors: ERROR — The second author is Hsuvas Borkakoty (not "Hrishav Borkakoty"). Minh Vu Pham and Yufang Hou are correct.
- Year: correct (2026, submitted January 2026)
- Title: correct
- Venue: correct (arXiv preprint, no formal venue claimed)
```

**8. `wang2025lost`** — Lost in Multilinguality

```
KEY: wang2025lost [WARNING — incomplete author list]
- Real: true
- Authors: ERROR — The bib entry lists 5 authors (Mingyang Wang, Heike Adel, Lukas Lange, Jannik Strötgen, Hinrich Schütze), but the real paper has 7 authors: Mingyang Wang, Heike Adel, Lukas Lange, Yihong Liu, Ercong Nie, Jannik Strötgen, and Hinrich Schütze. Two authors (Yihong Liu and Ercong Nie) are missing from the bib entry.
- Year: correct (2025)
- Title: correct
- Venue: correct (ACL 2025, confirmed on ACL Anthology 2025.acl-long.253)
```

---

**Summary**: All 8 papers are real. None are fabricated. However, **every single entry has at least one error**, mostly in author names. The most critical error is entry 5 (`marks2024geometry`), which lists the wrong venue entirely (ICLR 2024 instead of COLM 2024). Entry 1 (`feng2026finegrained`) has the most pervasive errors, with nearly every author name wrong and 3 authors missing. Entry 3 (`sundar2025steering`) fabricates Dan Jurafsky as a co-author.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f73af016-c382-4da5-b58e-159cd5cc6059",
  "isSidechain": true,
  "agentId": "a75fdddb311138678",
  "requestId": "req_011CbR5QskeSbzcWfZgwrMi9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29061142-3b2e-4fb6-b48c-eae519a4b670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "a99e8d52-116b-43ec-91a4-7d4113465b75",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDufERqS3RBJv9vi7QEM9w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1547,
      "cache_read_input_tokens": 34427,
      "output_tokens": 1681,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1547
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1681,
          "cache_read_input_tokens": 34427,
          "cache_creation_input_tokens": 1547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1547,
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
