# Research conversation: I need you to do two things: 1. Verify these papers exist with correct titles and venues using WebSearch: - "GoLLIE arXi

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7c580bbb8a65e0c4.jsonl`
- **Structured JSON:** [`8ce0ee4546a96fe09e83.json`](../../sessions/8c/8ce0ee4546a96fe09e83.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-10T06:56:35.835Z_

I need you to do two things:

1. Verify these papers exist with correct titles and venues using WebSearch:
   - "GoLLIE arXiv 2310.03668 2023" - search to confirm title and authors
   - "PARSE arXiv 2510.08623 2025" - search to confirm title and authors
   - "GuideX ACL Findings 2025" - search to confirm title and venue
   - "KnowCoder information extraction" - search to confirm paper and venue
   - Also search for any other key papers on: schema-guided IE, zero-shot NER, test-time adaptation LLM

2. Find NLP/ML conference submission deadlines after 2026-05-10. Search for:
   - "EMNLP 2026 submission deadline"
   - "COLING 2026 submission deadline"
   - "ACL 2027 submission deadline"
   - "NeurIPS 2026 submission deadline"
   - "ICLR 2027 submission deadline"
   - "NAACL 2026 submission deadline"
   - "EACL 2026 submission deadline"

Report exact paper titles, venues, and exact deadline dates for conferences. Today is 2026-05-10.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "059b4d71-1442-49db-8255-7249005b8ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T06:56:35.837Z_

```json
{
  "parentUuid": "059b4d71-1442-49db-8255-7249005b8ec1",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
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
  "uuid": "06678364-0766-44ab-9939-bc371d3c661e",
  "timestamp": "2026-05-10T06:56:35.837Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T06:56:37.785Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EfJECctoE7kFC6vBB4gUQm`</summary>

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
  "parentUuid": "06678364-0766-44ab-9939-bc371d3c661e",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAq7D46pH1sEk11KNj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "417544b1-338c-4a56-b8e0-c00c6f1ff58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WujeGbS7mYXyhqRM7cfVyF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 8088,
      "output_tokens": 76,
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
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8088,
          "cache_creation_input_tokens": 846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 846,
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

_source line 4 · 2026-05-10T06:56:37.793Z_

<details><summary>↩ Tool result · `toolu_01EfJECctoE7kFC6vBB4gUQm`</summary>

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
  "parentUuid": "417544b1-338c-4a56-b8e0-c00c6f1ff58e",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "304834b5-90af-4e89-b131-7296b75b09b5",
  "sourceToolAssistantUUID": "417544b1-338c-4a56-b8e0-c00c6f1ff58e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T06:56:40.271Z_

I'll run all the searches in parallel to save time.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "304834b5-90af-4e89-b131-7296b75b09b5",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAyisceg3hJhMHZapU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b344d585-ac09-4972-8503-9e93e7074d4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WFMbeTyfriunBiir74XC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 6 · 2026-05-10T06:56:41.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FVU8sWuJee7H5639AivpQz`</summary>

```json
{
  "query": "GoLLIE arXiv 2310.03668 2023 title authors information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b344d585-ac09-4972-8503-9e93e7074d4f",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAyisceg3hJhMHZapU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "991f8ff1-8c07-41be-9d28-22dae2d095ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WFMbeTyfriunBiir74XC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 7 · 2026-05-10T06:56:41.489Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y1J54DxiuNWXcV218Q3AXh`</summary>

```json
{
  "query": "PARSE arXiv 2510.08623 2025 title authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "991f8ff1-8c07-41be-9d28-22dae2d095ab",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAyisceg3hJhMHZapU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b43b258-448f-4e5a-b986-4f8b2ab5d5a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WFMbeTyfriunBiir74XC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 8 · 2026-05-10T06:56:42.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLRZyG7KduWGDd7TWVHVRa`</summary>

```json
{
  "query": "GuideX ACL Findings 2025 information extraction schema-guided"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b43b258-448f-4e5a-b986-4f8b2ab5d5a2",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAyisceg3hJhMHZapU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0a76458-a3dc-4a76-89ff-90be15792455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WFMbeTyfriunBiir74XC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 9 · 2026-05-10T06:56:43.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MnsEytT1tiNvDKXeUbnHcT`</summary>

```json
{
  "query": "KnowCoder information extraction paper venue 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0a76458-a3dc-4a76-89ff-90be15792455",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAyisceg3hJhMHZapU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8db0fb65-dc86-448d-ab24-9c68e3aded3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WFMbeTyfriunBiir74XC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 10 · 2026-05-10T06:56:43.533Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CHwpVi3fFVwUA5bMJdz8PJ`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8db0fb65-dc86-448d-ab24-9c68e3aded3f",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAyisceg3hJhMHZapU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b517b72d-be86-472d-9aaf-01aa2247743f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WFMbeTyfriunBiir74XC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 11 · 2026-05-10T06:56:43.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETmdsvhrAymLsQ9FmQYWos`</summary>

```json
{
  "query": "COLING 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b517b72d-be86-472d-9aaf-01aa2247743f",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAyisceg3hJhMHZapU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17ec30de-736f-4f5b-9a31-16631474839a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WFMbeTyfriunBiir74XC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
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

_source line 12 · 2026-05-10T06:56:44.184Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Er9QXin1RaSyf83xhHKby6`</summary>

```json
{
  "query": "ACL 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17ec30de-736f-4f5b-9a31-16631474839a",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTAyisceg3hJhMHZapU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88998817-351e-4db6-8085-68de3bfa5fa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019WFMbeTyfriunBiir74XC1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8934,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 8934,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 13 · 2026-05-10T06:56:46.115Z_

<details><summary>↩ Tool result · `toolu_01Y1J54DxiuNWXcV218Q3AXh`</summary>

```text
Web search results for query: "PARSE arXiv 2510.08623 2025 title authors"

Links: [{"title":"[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/abs/2510.08623"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623"},{"title":"Enterprise-Grade Security for the Model Context Protocol ( ...","url":"https://arxiv.org/pdf/2504.08623"},{"title":"Machine Learning","url":"https://web3.arxiv.org/list/cs.LG/recent?skip=175&show=100"},{"title":"[2401.08623] Wake-Sleep Consolidated Learning","url":"https://arxiv.org/abs/2401.08623"},{"title":"Uni-Parser Technical Report","url":"https://arxiv.org/html/2512.15098"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=36000&show=50"},{"title":"Computer Science Oct 2025","url":"https://arxiv.org/list/cs/2025-10?skip=3400&show=100"},{"title":"Document Parsing Unveiled: Techniques, Challenges, and Prospects for Structured Information Extraction","url":"https://arxiv.org/html/2410.21169v2"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://arxiv.org/list/cs.CV/2025?skip=21500&show=500"}]

Based on the search results, here is the information for arXiv paper 2510.08623:

**Title:** PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction

**Authors:** Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla

**Submission Date:** Submitted on 8 Oct 2025

**Conference:** EMNLP 2025 Industry Track

The paper presents PARSE, a system that addresses the challenge of structured information extraction by automatically optimizing JSON schemas for better LLM comprehension and extraction reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b43b258-448f-4e5a-b986-4f8b2ab5d5a2",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "3ec73c77-c4a7-4990-b52e-31a4cc03c991",
  "sourceToolAssistantUUID": "7b43b258-448f-4e5a-b986-4f8b2ab5d5a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T06:56:46.286Z_

<details><summary>↩ Tool result · `toolu_01FVU8sWuJee7H5639AivpQz`</summary>

```text
Web search results for query: "GoLLIE arXiv 2310.03668 2023 title authors information extraction"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668"},{"title":"dblp: GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction.","url":"https://dblp.org/rec/journals/corr/abs-2310-03668.html"},{"title":"HiTZ/GoLLIE-13B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-13B"},{"title":"HiTZ/GoLLIE-7B · Hugging Face","url":"https://huggingface.co/HiTZ/GoLLIE-7B"},{"title":"Large Language Models Meet NLP: A Survey","url":"https://arxiv.org/html/2405.12819v1"},{"title":"A Survey on Open Information Extraction from Rule-based Model to Large Language Model","url":"https://arxiv.org/html/2208.08690v7"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v1"},{"title":"gollie : annotation guidelines improve zero-shot ...","url":"https://arxiv.org/pdf/2310.03668"},{"title":"Paper page - GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://huggingface.co/papers/2310.03668"}]

Based on the search results, here's the information about GoLLIE (arXiv 2310.03668):

## Title
GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction

## Authors
Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, and Eneko Agirre

## Overview
GoLLIE (Guideline-following Large Language Model for IE) is a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.

## Key Details
While Large Language Models combined with instruction tuning have made significant progress when generalizing to unseen tasks, they have been less successful in Information Extraction (IE), lagging behind task-specific models. IE tasks are typically characterized by complex annotation guidelines that describe the task and give examples to humans. Previous attempts to leverage such information have failed, even with the largest models, as they are not able to follow the guidelines out of the box.

Comprehensive evaluation empirically demonstrates that GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction. The ablation study shows that detailed guidelines are key for good results.

## Publication
The paper was submitted on October 5, 2023, with the latest revision (v5) on March 6, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "991f8ff1-8c07-41be-9d28-22dae2d095ab",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "32718db1-1868-424e-8416-2a085ea41a07",
  "sourceToolAssistantUUID": "991f8ff1-8c07-41be-9d28-22dae2d095ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T06:56:47.670Z_

<details><summary>↩ Tool result · `toolu_01ETmdsvhrAymLsQ9FmQYWos`</summary>

```text
Web search results for query: "COLING 2026 submission deadline call for papers"

Links: [{"title":"COLING: International Conference on Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=533"},{"title":"Call for Main Conference Papers - COLING 2025","url":"https://coling2025.org/calls/main_conference_papers/"},{"title":"COLING 2026 - International Conference on Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/coling"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Computer Science conferences timeline","url":"https://lucjaulmes.github.io/cfp-timeline/"},{"title":"CoNLL 2026: 3rd and Final Call for Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/BDW4FPXENUKPTACOYMT5PXZSDZHJ5LB4/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AbjadNLP 2026 – The 2nd Workshop on NLP for Languages Using Arabic Script","url":"https://wp.lancs.ac.uk/abjad/"},{"title":"COLM 2026: Key Dates","url":"https://colmweb.org/dates.html"},{"title":"COLING 2025 : [CFP] International Conference on Computational Linguistics - Last Call for Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/K2WGRQA22TI434YZHIM7QO5MXOC7RUAP/"}]

Based on the search results, I found information about COLING 2025, but the search did not return specific details about COLING 2026's submission deadline and call for papers. The search results show:

- COLING 2025 will take place in Abu Dhabi, UAE, January 19-24 2025
- COLING 2025 invites the submission of long and short papers featuring substantial, original, and unpublished research in all aspects of Computational Linguistics

However, the search results don't contain specific submission deadlines or call for papers details for COLING 2026. One result mentioned COLING 2026 would be held in Abu Dhabi, but detailed information about the submission deadline and official call for papers wasn't available in these search results.

For the most up-to-date COLING 2026 call for papers and submission deadlines, I'd recommend checking the official COLING website directly or checking conference deadline tracking sites like WikiCFP as they may have posted this information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17ec30de-736f-4f5b-9a31-16631474839a",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "346edd77-5bb7-48a4-9ec0-af49490ec15d",
  "sourceToolAssistantUUID": "17ec30de-736f-4f5b-9a31-16631474839a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T06:56:49.536Z_

<details><summary>↩ Tool result · `toolu_01Er9QXin1RaSyf83xhHKby6`</summary>

```text
Web search results for query: "ACL 2027 submission deadline call for papers"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"CALL FOR BIDS TO HOST EACL 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-bids-host-eacl-2027"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=37"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=acl26"},{"title":"Information for Submitters - ACL Anthology","url":"https://aclanthology.org/info/contrib/"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_country&sort=desc"}]

Based on the search results, here's what I found regarding ACL 2027:

ACL 2027 is scheduled for July 2027 at a location to be announced (TBA), with dates predicted based on historical patterns. However, the specific submission deadline has not yet been officially announced, though submissions are expected to be done through ARR (ACL Rolling Review).

For reference, all ACL submissions are made through the ACL Rolling Review (ARR) system, which has rolling submission deadlines every two months rather than a single conference deadline.

Since ACL 2027 is still over a year away, the official call for papers and submission deadlines have not yet been released. You may want to check the official ACL website (aclweb.org) or the ACL Rolling Review website (aclrollingreview.org) periodically for the official announcement when it becomes available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88998817-351e-4db6-8085-68de3bfa5fa2",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "0e915c63-add4-4050-941a-9ec08e6cc4ac",
  "sourceToolAssistantUUID": "88998817-351e-4db6-8085-68de3bfa5fa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T06:56:50.234Z_

<details><summary>↩ Tool result · `toolu_01GLRZyG7KduWGDd7TWVHVRa`</summary>

```text
Web search results for query: "GuideX ACL Findings 2025 information extraction schema-guided"

Links: [{"title":"GUIDEX – ACL Findings 2025","url":"https://neilus03.github.io/guidex.com/"},{"title":"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1245/"},{"title":"GUIDEX: Guided Synthetic Data Generation for Zero-Shot ...","url":"https://aclanthology.org/2025.findings-acl.1245.pdf"},{"title":"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction","url":"https://arxiv.org/html/2506.00649"},{"title":"[2506.00649] GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction","url":"https://arxiv.org/abs/2506.00649"},{"title":"GitHub - Neilus03/GUIDEX: GUIDEX official repo","url":"https://github.com/Neilus03/GUIDEX"},{"title":"Taxonomy-Driven Knowledge Graph Construction for ...","url":"https://aclanthology.org/2025.findings-acl.223.pdf"},{"title":"Information Extraction from Visually Rich Documents using ...","url":"https://aclanthology.org/2025.acl-long.844.pdf"},{"title":"Adaptive Schema-aware Event Extraction with Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.419.pdf"},{"title":"Instruction-Tuning LLMs for Event Extraction with ...","url":"https://aclanthology.org/2025.findings-acl.677.pdf"}]

Based on the search results, here's what I found about GuideX from ACL Findings 2025:

## Overview

GuideX is a novel method that automatically defines domain-specific schemas, infers guidelines, and generates synthetically labeled instances, allowing for better out-of-domain generalization.

## Key Problem

Information Extraction (IE) systems are traditionally domain-specific, requiring costly adaptation that involves expert schema design, data annotation, and model training. While Large Language Models have shown promise in zero-shot IE, performance degrades significantly in unseen domains where label definitions differ.

## Technical Approach

GuideX is a fully-automatic pipeline that transforms raw documents into executable (guidelines + annotations) pairs, where a single LLaMA-3.1 70B Instruct model is queried four times in succession, each prompt feeding directly into the next stage.

The pipeline involves:
- Document Summarisation, where the model receives the entire article and is constrained to emit only atomic facts: key actors, dates, figures and claims
- Structured Representation, where bullets are re-encoded into a minimal JSON sketch whose keys are coarse, on-the-fly entity/slot names
- A filter that keeps only schema-consistent, executable pairs and reduces noise before training

## Results

Fine-tuning Llama 3.1 with GuideX sets a new state-of-the-art across seven zero-shot Named Entity Recognition benchmarks, with models trained with GuideX gaining up to 7 F1 points over previous methods without human labeled data, and nearly 2 F1 points higher when combined with it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0a76458-a3dc-4a76-89ff-90be15792455",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "e39b82c7-22af-4d59-bd38-2925560353c2",
  "sourceToolAssistantUUID": "f0a76458-a3dc-4a76-89ff-90be15792455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T06:56:50.846Z_

<details><summary>↩ Tool result · `toolu_01CHwpVi3fFVwUA5bMJdz8PJ`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Here are the key details for the EMNLP 2026 call for papers:

## Submission Deadline
The EMNLP 2026 paper submission deadline is May 25, 2026 at 23:59:59 (UTC-12).

## Conference Details
The conference will be held in Budapest, Hungary, October 24-29, 2026.

## Paper Types Welcome
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Timeline
Key dates include reviewer registration deadline for all authors on May 27, 2026, author response and discussion from July 7-13, 2026, and meta review release on July 30, 2026.

## Special Note on ARR Submissions
Since the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.

For more detailed information, the official EMNLP 2026 call for papers is at https://2026.emnlp.org/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b517b72d-be86-472d-9aaf-01aa2247743f",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "81da7ed5-76af-4dc8-bf98-eff785a548be",
  "sourceToolAssistantUUID": "b517b72d-be86-472d-9aaf-01aa2247743f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T06:56:51.503Z_

<details><summary>↩ Tool result · `toolu_01MnsEytT1tiNvDKXeUbnHcT`</summary>

```text
Web search results for query: "KnowCoder information extraction paper venue 2024"

Links: [{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.475/"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for ...","url":"https://aclanthology.org/2024.acl-long.475.pdf"},{"title":"GitHub - ICT-GoKnow/KnowCoder: Official Repo of paper \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\". In the paper, we propose KnowCoder, the most powerful large language model so far for universal information extraction.","url":"https://github.com/ICT-GoKnow/KnowCoder"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/384207388_KnowCoder_Coding_Structured_Knowledge_into_LLMs_for_Universal_Information_Extraction"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - Zixuan Li","url":"https://lee-zix.github.io/publications/2024-08-16-ACL/"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"ICT-GoKnow · GitHub","url":"https://github.com/ICT-GoKnow"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2b5538e89bfb4cac76acafc1f9f2c9f64/dblp"},{"title":"KnowCoder: Coding structured knowledge into LLMs for universal information extraction - Wikidata","url":"https://www.wikidata.org/wiki/Q131458130"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"}]

Based on the search results, here's the information about the KnowCoder paper:

The KnowCoder paper was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL) in 2024. More specifically, the paper was presented in August 2024 in Bangkok, Thailand.

The full title is "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction", authored by Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, and Xueqi Cheng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8db0fb65-dc86-448d-ab24-9c68e3aded3f",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "56b674fb-cf27-44f3-a6e9-2192531078f6",
  "sourceToolAssistantUUID": "8db0fb65-dc86-448d-ab24-9c68e3aded3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T06:56:53.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKRxCJQCtSYUUmXpYASKGa`</summary>

```json
{
  "query": "NeurIPS 2026 submission deadline abstract deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56b674fb-cf27-44f3-a6e9-2192531078f6",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTByrLcDfGgyhueYz3Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1b27a19-a48d-42b8-a206-f6151f8d54fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UuNojsiQcGRvk624MxKrEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 10326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3484,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T06:56:53.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K4sTeDodo5dziBm4e5gyaV`</summary>

```json
{
  "query": "ICLR 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1b27a19-a48d-42b8-a206-f6151f8d54fb",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTByrLcDfGgyhueYz3Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3264f154-b22e-438d-8e34-1bd46f7a1714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UuNojsiQcGRvk624MxKrEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 10326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3484,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T06:56:54.336Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GiQEj2XKnii4KGrsozyTyJ`</summary>

```json
{
  "query": "NAACL 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3264f154-b22e-438d-8e34-1bd46f7a1714",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTByrLcDfGgyhueYz3Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9179b9af-235f-4e21-975e-bfbf787c6fc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UuNojsiQcGRvk624MxKrEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 10326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3484,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T06:56:54.715Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LRDQsbMpJDRoj1yYtPNPNu`</summary>

```json
{
  "query": "EACL 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9179b9af-235f-4e21-975e-bfbf787c6fc5",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTByrLcDfGgyhueYz3Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce852e58-0862-42ae-a0db-bc6ab7b28728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UuNojsiQcGRvk624MxKrEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 10326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3484,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T06:56:55.533Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G6SckFDBfrnxNjwAc5TvUH`</summary>

```json
{
  "query": "schema-guided information extraction zero-shot NER 2024 2025 key papers LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce852e58-0862-42ae-a0db-bc6ab7b28728",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTByrLcDfGgyhueYz3Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b0c7543-d623-40f0-a593-ae44d36a023a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UuNojsiQcGRvk624MxKrEH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 10326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3484,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T06:56:55.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SnSyMtHpfUpr4vDk2nRNeH`</summary>

```json
{
  "query": "test-time adaptation LLM NER named entity recognition 2024 2025 key papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b0c7543-d623-40f0-a593-ae44d36a023a",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTByrLcDfGgyhueYz3Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e38752b-c538-4279-a865-0a849e90d4d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UuNojsiQcGRvk624MxKrEH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 10326,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3484
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2487,
          "output_tokens": 315,
          "cache_read_input_tokens": 10326,
          "cache_creation_input_tokens": 3484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3484,
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

_source line 26 · 2026-05-10T06:56:56.765Z_

<details><summary>↩ Tool result · `toolu_01BKRxCJQCtSYUUmXpYASKGa`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline abstract deadline"

Links: [{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"2026 Conference","url":"https://neurips.cc/Conferences/2026"},{"title":"NeurIPS Newsletter – April 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 Call for Position Papers","url":"https://neurips.cc/Conferences/2026/CallForPositionPapers"},{"title":"NeurIPS Conference on X: \"The NeurIPS 2026 submission site opening has been moved to April 15th. Note that all tracks (Main Submission, Evaluations &amp; Datasets, and Position Papers) share the same dates. The final submission deadlines remain unchanged: • Paper Abstracts: May 4th (AOE) • Full Papers:\" / X","url":"https://x.com/NeurIPSConf/status/2041303457554940336"}]

Based on the search results, here are the NeurIPS 2026 submission deadlines:

**Abstract Submission Deadline:** May 4, 2026 (AOE)

**Full Paper Submission Deadline:** May 6, 2026 AOE

These deadlines apply to all tracks including the Main Track, Evaluations & Datasets Track, and Position Papers Track. Submissions opened on April 15, 2026, and all authors must have an OpenReview profile when submitting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1b27a19-a48d-42b8-a206-f6151f8d54fb",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "741b6f9e-2077-4105-9345-f74e157f514e",
  "sourceToolAssistantUUID": "c1b27a19-a48d-42b8-a206-f6151f8d54fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T06:56:59.062Z_

<details><summary>↩ Tool result · `toolu_01K4sTeDodo5dziBm4e5gyaV`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline call for papers"

Links: [{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"}]

Based on the search results, I found information about ICLR conferences, but the official ICLR website has not yet published a dedicated call for papers for ICLR 2027. The most recent information available is for ICLR 2026, which has already passed its submission deadline.

From the search results, I can see that the International Conference on Learning Representations (ICLR) is the premier gathering of professionals dedicated to the advancement of the branch of artificial intelligence called representation learning, but generally referred to as deep learning, and it is a machine learning conference typically held in late April or early May each year.

For ICLR 2027 specific information, I recommend:
1. Visiting the official ICLR website at **iclr.cc** to check for announcements about ICLR 2027
2. Checking the OpenReview platform at **openreview.net** for submission details once the call for papers is released
3. Signing up for ICLR mailing lists or following their social media for announcements about the 2027 submission deadline

The conference typically announces the call for papers and submission deadlines several months in advance, so check back on the official website for the most current information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3264f154-b22e-438d-8e34-1bd46f7a1714",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "5eab0779-caa9-450c-88c3-a2dbccb0ead1",
  "sourceToolAssistantUUID": "3264f154-b22e-438d-8e34-1bd46f7a1714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T06:57:00.149Z_

<details><summary>↩ Tool result · `toolu_01GiQEj2XKnii4KGrsozyTyJ`</summary>

```text
Web search results for query: "NAACL 2026 submission deadline call for papers"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_country&sort=desc"},{"title":"NAACL 2026 - Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/naacl"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"Links - Human Language Intelligence Lab","url":"https://hli.skku.edu/links"}]

Based on the search results, here's what I found about NAACL 2026 and paper submissions:

Starting from 2024, all main *ACL conferences use ARR (ACL Rolling Review) exclusively, including NAACL 2025 and ACL 2026. This means NAACL 2026 will likely also use the ACL Rolling Review system for submissions.

However, the search results don't contain specific information about a dedicated NAACL 2026 conference call for papers. The results show that the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) will be held in San Diego, California, United States from July 2–7, 2026, and NAACL 2026 will be held in Albuquerque, USA, but detailed submission deadlines and call for papers information for NAACL 2026 specifically are not yet available in the search results.

For the most current and detailed information about NAACL 2026 submission deadlines and calls for papers, I recommend checking the official NAACL website or the ACL Rolling Review platform directly, as the specific call for papers details may not yet be publicly posted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9179b9af-235f-4e21-975e-bfbf787c6fc5",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "74789f6b-557d-4f3d-bac7-7214b5d384bd",
  "sourceToolAssistantUUID": "9179b9af-235f-4e21-975e-bfbf787c6fc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T06:57:00.315Z_

<details><summary>↩ Tool result · `toolu_01LRDQsbMpJDRoj1yYtPNPNu`</summary>

```text
Web search results for query: "EACL 2026 submission deadline call for papers"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for System Demonstrations -","url":"https://2026.eacl.org/calls/demos/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Industry Track — Call for Papers -","url":"https://2026.eacl.org/calls/industry/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL 2026 – CL deadlines for Qualifying Papers | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/15"},{"title":"LINGUIST List 36.2630 Confs: Joint Call for Tutorial Proposals: EACL/ACL 2026 (Online)","url":"https://linguistlist.org/issues/36/2630/"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"},{"title":"EACL 2026 - Industry Track — Call for Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/G4RZABE62LMTDPQFMDJ63VDWP4RXTEGB/"}]

Based on the search results, here's information about the EACL 2026 submission deadline and call for papers:

## Main Conference Call for Papers

The ARR submission deadline is October 6, 2025 and the EACL commitment deadline is December 14, 2025. EACL 2026 will be held in Rabat, Morocco, from March 24–29, 2026.

The "paper submission deadline" is the latest date that new papers can be submitted to ARR and be reviewed in time to be considered by EACL 2026. Paper submission and commitment will be handled via the ACL Rolling Review (ARR) system.

## Paper Requirements

Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices. At least one author of each accepted paper must register for EACL 2026 by the early registration deadline.

## Additional Tracks

Other submission deadlines include:
- System Demonstrations: Paper submission deadline is Monday, December 1, 2025, with notification of acceptance on Tuesday, February 10, 2026
- Industry Track: Paper submission deadline is November 17, 2025, with notification of acceptance on January 5, 2026

For more details, you can visit the official EACL 2026 website at https://2026.eacl.org/calls/papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce852e58-0862-42ae-a0db-bc6ab7b28728",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "cd10931d-0b23-419e-92b5-070f30b41164",
  "sourceToolAssistantUUID": "ce852e58-0862-42ae-a0db-bc6ab7b28728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T06:57:04.902Z_

<details><summary>↩ Tool result · `toolu_01G6SckFDBfrnxNjwAc5TvUH`</summary>

```text
Web search results for query: "schema-guided information extraction zero-shot NER 2024 2025 key papers LLM"

Links: [{"title":"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction","url":"https://arxiv.org/html/2506.00649"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Few-Shot Relation Extraction via Two-Stage Knowledge- ...","url":"https://www.ijcai.org/proceedings/2025/0897.pdf"},{"title":"A Zero-Shot Framework for Low-Resource Relation Extraction via Distant Supervision and Large Language Models","url":"https://www.mdpi.com/2079-9292/14/3/593"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"Evaluating LLM-Based Resume Information Extraction: A Comparative","url":"https://www.scitepress.org/Papers/2025/138379/138379.pdf"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"LlmRe: A zero-shot entity relation extraction method based on the large language model | Proceedings of the 2023 7th International Conference on Electronic Information Technology and Computer Engineering","url":"https://dl.acm.org/doi/abs/10.1145/3650400.3650478"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"}]

Based on the search results, here are the key findings on schema-guided information extraction, zero-shot NER, and related LLM papers from 2024-2025:

## Recent Key Papers and Approaches

### Schema-Guided Synthetic Data Generation
GuideX addresses the challenge by automating the generation of domain-specific schemas, guidelines, and annotated data to bridge the seen-unseen domain divide for zero-shot NER. Synthetic data generation has proven particularly valuable in the era of LLMs.

### Zero-Shot Information Extraction with LLMs
Zero-shot prompting relies solely on task instructions, while few-shot prompting provides in-context exemplars to enhance performance. Large language models have profoundly reshaped information extraction, with methods reframing IE as a language modeling problem where carefully crafted prompts guide LLMs to generate structured outputs for tasks like named entity recognition.

### Notable 2024-2025 Research
Recent papers include:
- UniversalNER (ICLR 2024), which involves targeted distillation from large language models for open named entity recognition
- Knowcoder (2024), coding structured knowledge into LLMs for universal information extraction
- RUIE (2025), a retrieval-based unified information extraction framework using large language models

### Schema-Constrained Synthetic Data
Recent work designs prompts that inform the LLM about essential components of extraction samples, and the LLM is guided to generate additional pseudo samples based on this structure.

### Performance Considerations
The performance of prompt-based IE methods is highly sensitive to prompt design, especially the selection of in-context examples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b0c7543-d623-40f0-a593-ae44d36a023a",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "67bf55f4-2866-48c2-920c-fa34dcce4618",
  "sourceToolAssistantUUID": "0b0c7543-d623-40f0-a593-ae44d36a023a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T06:57:08.413Z_

<details><summary>↩ Tool result · `toolu_01SnSyMtHpfUpr4vDk2nRNeH`</summary>

```text
Web search results for query: "test-time adaptation LLM NER named entity recognition 2024 2025 key papers"

Links: [{"title":"Development of a Language Model for Named-Entity-Recognition in Aerospace Requirements | Journal of Aerospace Information Systems","url":"https://arc.aiaa.org/doi/10.2514/1.I011251"},{"title":"Advancing clinical information extraction with LLM-Augmenter | Truveta","url":"https://www.truveta.com/blog/research/advancing-clinical-information-extraction-with-llm-augmenter/"},{"title":"GPT-NER: Named Entity Recognition via Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.239/"},{"title":"Rapid Adaptation of Chemical Named Entity Recognition Using Few-Shot Learning and LLM Distillation - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40310732/"},{"title":"A novel large-language-model-driven framework for named entity recognition - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457324004138"},{"title":"llmNER: (Zero|Few)-Shot Named Entity Recognition, Exploiting the Power of Large Language Models","url":"https://arxiv.org/html/2406.04528v1"},{"title":"Comparative analysis of generative LLMs for labeling entities in clinical notes - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11804004/"},{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"},{"title":"GitHub - Dereck0602/Awesome_Test_Time_LLMs","url":"https://github.com/Dereck0602/Awesome_Test_Time_LLMs"},{"title":"Evaluating the Performance of Large Language Models for Named Entity Recognition in Ophthalmology Clinical Free-Text Notes - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12099357/"}]

Based on the search results, here are key papers and research on test-time adaptation for LLMs in Named Entity Recognition from 2024-2025:

## Key Papers Found

### 1. **GPT-NER: Named Entity Recognition via Large Language Models (2025)**
This NAACL 2025 paper proposes GPT-NER to address the gap between sequence labeling tasks and text generation models, using a self-verification strategy where LLMs verify extracted entities. It achieves comparable performance to fully supervised baselines on five NER datasets. Notably, GPT-NER shows greater ability in low-resource and few-shot setups when training data is extremely scarce, significantly outperforming supervised models.

### 2. **Rapid Adaptation of Chemical Named Entity Recognition Using Few-Shot Learning and LLM Distillation (2025)**
This work demonstrates how LLM-annotated data can train models for rapid NER adaptation by distilling large language model knowledge into lightweight models suitable for efficient use.

### 3. **A Novel Large-Language-Model-Driven Framework for NER (2024)**
This framework, called LLMCC, integrates in-context learning with methods like SemnRank and InforLaw-thought prompting to guide LLMs in processing text for NER tasks.

### 4. **LinkNER (2024)**
LinkNER integrates smaller fine-tuned NER models with LLMs through an uncertainty-based linking strategy using a Recognition-Detection-Classification (RDC) approach.

### 5. **llmNER: Zero/Few-Shot Named Entity Recognition (2024)**
This Python library implements zero-shot and few-shot NER with LLMs, featuring multiple prompting methods, answer parsers, flexible prompt templating, and prompt engineering capabilities.

### 6. **Comparative Analysis of Generative LLMs for Clinical NER (2025)**
Research shows that instruction fine-tuned models outperform chat fine-tuned and base models in entity recognition, and models perform better when simple output structures are requested.

These papers highlight recent advances in adapting LLMs for NER through prompting strategies, few-shot learning, knowledge distillation, and hybrid approaches combining fine-tuned models with LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e38752b-c538-4279-a865-0a849e90d4d8",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "4e397e81-a4a5-4f47-afb1-0c1686ae6a4d",
  "sourceToolAssistantUUID": "0e38752b-c538-4279-a865-0a849e90d4d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T06:57:11.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BQvg8YNu4H5Mtry9eXkwpL`</summary>

```json
{
  "query": "NAACL 2026 ARR deadline dates Albuquerque"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e397e81-a4a5-4f47-afb1-0c1686ae6a4d",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTDEE4kWU6ApYxyAjhs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9226927-3d8d-44bd-ae2b-a89f07bd0317",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012t4ajtPpE7qJZBJqSJrh9e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7855,
      "cache_read_input_tokens": 13810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7855,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T06:57:11.936Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LqUMqHBosdcphQnWb1anz9`</summary>

```json
{
  "query": "COLING 2026 call for papers dates location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9226927-3d8d-44bd-ae2b-a89f07bd0317",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTDEE4kWU6ApYxyAjhs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e6910cd-927a-4fce-ab7b-96afffdcf3d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012t4ajtPpE7qJZBJqSJrh9e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7855,
      "cache_read_input_tokens": 13810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7855,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T06:57:12.280Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016PUCn6zyZ9gJT3ist4EyXJ`</summary>

```json
{
  "query": "GoLLIE ICLR 2024 published venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e6910cd-927a-4fce-ab7b-96afffdcf3d6",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTDEE4kWU6ApYxyAjhs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7440bc63-5e35-425a-ac05-7ef98e54088e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012t4ajtPpE7qJZBJqSJrh9e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7855,
      "cache_read_input_tokens": 13810,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7855
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 13810,
          "cache_creation_input_tokens": 7855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7855,
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

_source line 35 · 2026-05-10T06:57:15.525Z_

<details><summary>↩ Tool result · `toolu_01LqUMqHBosdcphQnWb1anz9`</summary>

```text
Web search results for query: "COLING 2026 call for papers dates location"

Links: [{"title":"COLING: International Conference on Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=533"},{"title":"CoNLL 2026: 3rd and Final Call for Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/BDW4FPXENUKPTACOYMT5PXZSDZHJ5LB4/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"CoNLL 2026 | CoNLL","url":"https://conll.org/"},{"title":"Call for Main Conference Papers - COLING 2025","url":"https://coling2025.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Language Resources and Evaluation Conference - LREC 2026","url":"https://lrec2026.info/"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"}]

Based on the search results, I found information about COLING 2025, but I did not find specific details about COLING 2026 call for papers, dates, or location. 

The search results show:

- COLING 2025 will take place in Abu Dhabi, UAE, January 19-24 2025

However, I did not locate information about a COLING 2026 call for papers, submission deadlines, or confirmed conference location and dates in the search results. The results primarily contain information about other 2026 conferences like EACL 2026, EMNLP 2026, and CoNLL 2026, but not COLING 2026 specifically.

If you're looking for COLING 2026 information, I'd recommend checking the official COLING website directly or waiting for an official announcement from the conference organizers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e6910cd-927a-4fce-ab7b-96afffdcf3d6",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "690b2bda-1737-4332-95f9-0cff2b9c66e6",
  "sourceToolAssistantUUID": "8e6910cd-927a-4fce-ab7b-96afffdcf3d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T06:57:15.813Z_

<details><summary>↩ Tool result · `toolu_016PUCn6zyZ9gJT3ist4EyXJ`</summary>

```text
Web search results for query: "GoLLIE ICLR 2024 published venue conference"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"2024 Conference","url":"https://iclr.cc/Conferences/2024"},{"title":"2023 Conference","url":"https://iclr.cc/Conferences/2023"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"ICLR 2024 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2024%2FConference"},{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"2024 Dates and Deadlines","url":"https://iclr.cc/Conferences/2024/Dates"},{"title":"Paper Digest: ICLR 2024 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2024/05/iclr-2024-highlights/"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"}]

Based on the search results, here's the information about GoLLIE and ICLR 2024:

GoLLIE was published as a conference paper at ICLR 2024. The full title is "GoLLIE: Annotation Guidelines Improve Zero-Shot Information-Extraction" by authors Oscar Sainz and Iker García-Ferrero from the HiTZ Basque Center for Language Technology.

GoLLIE (Guideline-following Large Language Model for IE) is a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.

The ICLR 2024 annual conference was held in Vienna, Austria from May 7-11, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7440bc63-5e35-425a-ac05-7ef98e54088e",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "e98a5a98-4d61-4134-90ff-3ef44d95d310",
  "sourceToolAssistantUUID": "7440bc63-5e35-425a-ac05-7ef98e54088e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T06:57:16.961Z_

<details><summary>↩ Tool result · `toolu_01BQvg8YNu4H5Mtry9eXkwpL`</summary>

```text
Web search results for query: "NAACL 2026 ARR deadline dates Albuquerque"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"NAACL 2026 - Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/naacl"},{"title":"2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics - NAACL-HLT 2025","url":"https://2025.naacl.org/"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"NAACL HLT 2025 (@naaclmeeting) / ...","url":"https://twitter.com/naaclmeeting"},{"title":"NAACL HLT 2027 (@naaclmeeting) / Posts / X","url":"https://x.com/naaclmeeting?lang=en"}]

Based on the search results, I found information about NAACL conferences, though the results contain some important clarifications:

NAACL 2026 will be held in Albuquerque, USA. However, the search results indicate that NAACL 2025 is using ARR exclusively, and there's a note that NAACL 2025 is scheduled for April 30 - May 4, 2025 in Albuquerque, New Mexico.

Unfortunately, the search results do not contain specific ARR submission deadline dates for NAACL 2026. The ARR website information in the results indicates that the new 10-week cycle schedule will be in action starting in May 2025, but the exact ARR deadline dates for papers being submitted for NAACL 2026 are not provided in these results.

To find the specific ARR deadline dates for NAACL 2026, I'd recommend checking:
- The official NAACL 2026 website
- The ACL Rolling Review website (aclrollingreview.org) for the complete cycle schedule


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9226927-3d8d-44bd-ae2b-a89f07bd0317",
  "isSidechain": true,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "agentId": "a7c580bbb8a65e0c4",
  "type": "user",
  "uuid": "8694029d-a118-4e25-a67c-fee7f3c71d3b",
  "sourceToolAssistantUUID": "e9226927-3d8d-44bd-ae2b-a89f07bd0317",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-10T06:57:52.297Z_

Here is the full verified report.

---

## Part 1: Paper Verification

### 1. GoLLIE — arXiv:2310.03668
- **Exact Title:** "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction"
- **Authors:** Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre (HiTZ Basque Center for Language Technology)
- **Venue:** Published as a conference paper at **ICLR 2024** (Vienna, Austria, May 7-11, 2024)
- **arXiv submitted:** October 5, 2023; last revised March 6, 2024 (v5)
- **Status:** CONFIRMED. The arXiv ID, title, and venue are all correct.

---

### 2. PARSE — arXiv:2510.08623
- **Exact Title:** "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction"
- **Authors:** Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla
- **Venue:** **EMNLP 2025 Industry Track**
- **arXiv submitted:** October 8, 2025
- **Status:** CONFIRMED. The arXiv ID and title are verified.

---

### 3. GuideX — ACL Findings 2025
- **Exact Title:** "GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction"
- **Venue:** **Findings of ACL 2025** (ACL Anthology: 2025.findings-acl.1245)
- **Status:** CONFIRMED. The title and venue are correct. The paper also has a companion arXiv preprint at arXiv:2506.00649. Fine-tunes Llama 3.1 and sets state-of-the-art across 7 zero-shot NER benchmarks.

---

### 4. KnowCoder — Information Extraction
- **Exact Title:** "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction"
- **Authors:** Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
- **Venue:** **ACL 2024** (Proceedings of the 62nd Annual Meeting of the ACL, Bangkok, Thailand, August 2024) — Long paper track
- **ACL Anthology:** 2024.acl-long.475
- **Status:** CONFIRMED.

---

### Additional Key Papers Found

**Schema-Guided IE / Zero-Shot NER:**
- **GPT-NER: Named Entity Recognition via Large Language Models** — NAACL 2025 Findings (2025.findings-naacl.239). Proposes self-verification for LLM-based NER; strong in few-shot/low-resource settings.
- **UniversalNER** — ICLR 2024. Targeted distillation from large LLMs for open named entity recognition.
- **llmNER** (arXiv:2406.04528, 2024) — Zero/few-shot NER exploiting LLMs with multiple prompting strategies.

**Test-Time Adaptation for LLMs:**
- No single landmark "test-time adaptation for IE/NER" paper dominates the 2024-2025 literature. The closest trend is **inference-time prompting and self-verification** (e.g., GPT-NER's self-verification, GuideX's pipeline-driven schema inference). The GitHub repo [Awesome_Test_Time_LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) aggregates this line of work but no single definitive venue paper emerged from the search.

---

## Part 2: Conference Submission Deadlines (after 2026-05-10)

| Conference | Key Deadline | Notes |
|---|---|---|
| **EMNLP 2026** | ARR Submission: **May 25, 2026** | Budapest, Hungary, Oct 24-29, 2026. Authors must select EMNLP vs. AACL at submission time (binding). |
| **NeurIPS 2026** | Abstract: **May 4, 2026** (PAST); Full paper: **May 6, 2026** (PAST) | Both deadlines are before today (May 10, 2026) — already closed. |
| **EACL 2026** | ARR submission: **Oct 6, 2025** (PAST); Commitment: **Dec 14, 2025** (PAST) | Rabat, Morocco, March 24-29, 2026. Conference already occurred. |
| **COLING 2026** | No official CFP or dates found yet | COLING runs on a biennial schedule; no 2026 edition has been announced. |
| **NAACL 2026** | No official CFP published yet | Albuquerque, USA. Will use ARR; specific cycle deadlines not yet announced. |
| **ACL 2027** | Not yet announced | Will use ARR rolling system; no CFP released. |
| **ICLR 2027** | Not yet announced | No CFP released; typically announced ~Sep-Oct of prior year. |

### Summary of upcoming actionable deadlines (after today, 2026-05-10):
- **EMNLP 2026**: ARR submission deadline **May 25, 2026** — this is the only confirmed upcoming deadline you can still hit.
- All other searched conferences either have deadlines already passed or have not yet published their 2026/2027 CFPs.

---

Sources:
- [GoLLIE arXiv:2310.03668](https://arxiv.org/abs/2310.03668)
- [GoLLIE at ICLR 2024 (OpenReview)](https://openreview.net/forum?id=Y3wpuxd7u9)
- [PARSE arXiv:2510.08623](https://arxiv.org/abs/2510.08623)
- [GUIDEX — ACL Anthology 2025.findings-acl.1245](https://aclanthology.org/2025.findings-acl.1245/)
- [GuideX arXiv:2506.00649](https://arxiv.org/abs/2506.00649)
- [KnowCoder — ACL Anthology 2024.acl-long.475](https://aclanthology.org/2024.acl-long.475/)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)
- [EACL 2026 Call for Main Conference Papers](https://2026.eacl.org/calls/papers/)
- [ACL Rolling Review Dates and Venues](http://aclrollingreview.org/dates)
- [GPT-NER at NAACL 2025 Findings](https://aclanthology.org/2025.findings-naacl.239/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8694029d-a118-4e25-a67c-fee7f3c71d3b",
  "isSidechain": true,
  "agentId": "a7c580bbb8a65e0c4",
  "requestId": "req_011CatTDrmzo1gTEgLGKocfu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7758eec1-3452-4d05-996e-c7e0f4b88139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0124RrXUUJstCAJDioFXLeAj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1386,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 21665,
      "output_tokens": 1879,
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
          "input_tokens": 1386,
          "output_tokens": 1879,
          "cache_read_input_tokens": 21665,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 894,
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
