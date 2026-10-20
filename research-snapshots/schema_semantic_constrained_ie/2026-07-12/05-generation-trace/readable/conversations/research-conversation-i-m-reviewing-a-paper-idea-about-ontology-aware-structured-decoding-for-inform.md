# Research conversation: I'm reviewing a paper idea about "ontology-aware structured decoding for information extraction using hybrid grammar-cal

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 1
- **Tool calls:** 31
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aace49c5e381cb38b.jsonl`
- **Structured JSON:** [`6214c9e9145c06de2c7c.json`](../../sessions/62/6214c9e9145c06de2c7c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

71 recorded events

### User

_source line 1 · 2026-05-11T23:09:49.327Z_

I'm reviewing a paper idea about "ontology-aware structured decoding for information extraction using hybrid grammar-callback constraints." I need to find competing/concurrent work that the authors may have missed. Search for the following using WebSearch and WebFetch:

1. Search "constrained decoding information extraction 2025 2026" - any recent work combining constrained decoding with IE?
2. Search "schema-guided information extraction LLM 2026" - schema-driven IE approaches
3. Search "vLLM LogitsProcessor custom constraints" - has anyone built custom logit processors for semantic constraints in vLLM?
4. Search "ontology-constrained generation knowledge extraction 2025 2026"
5. Search "structured output information extraction joint entity relation 2026"
6. Search "site:arxiv.org grammar constrained decoding NER relation extraction 2025 2026"
7. Search "ACE05 joint extraction LLM state of the art 2025 2026" - what's the current SOTA on ACE05 joint IE?

For each search, report the most relevant papers found with titles, venues, dates, and brief descriptions. I especially need to know if anyone has already done hybrid grammar+callback constrained decoding for IE specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "c1cdc52f-298d-48ee-9b79-2b851be4575c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:09:49.330Z_

```json
{
  "parentUuid": "c1cdc52f-298d-48ee-9b79-2b851be4575c",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
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
  "uuid": "6c5d23ad-3c5f-4e12-b712-93c98fc7fe4b",
  "timestamp": "2026-05-11T23:09:49.330Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:09:53.908Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then execute all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c5d23ad-3c5f-4e12-b712-93c98fc7fe4b",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCBJ6cViDcU4UbnvkY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b128eb11-e93a-44db-ad77-ca92db87ebd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qvfx5zAdwpZHindVdbRAGo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 836,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:09:54.231Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CG2gkZFTprCuDoZ6vR6aLd`</summary>

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
  "parentUuid": "b128eb11-e93a-44db-ad77-ca92db87ebd5",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCBJ6cViDcU4UbnvkY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbd0b58f-4f2a-4a5b-8287-a373b9130912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qvfx5zAdwpZHindVdbRAGo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 8223,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 836,
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

_source line 5 · 2026-05-11T23:09:54.235Z_

<details><summary>↩ Tool result · `toolu_01CG2gkZFTprCuDoZ6vR6aLd`</summary>

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
  "parentUuid": "cbd0b58f-4f2a-4a5b-8287-a373b9130912",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "8b9d71ba-f61f-4717-8007-32b893453bcf",
  "sourceToolAssistantUUID": "cbd0b58f-4f2a-4a5b-8287-a373b9130912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:09:56.591Z_



Now let me run all seven searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9d71ba-f61f-4717-8007-32b893453bcf",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCYWoA9RLvQsspmDer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cdf52ca-c830-4206-86cc-06fb195c5889",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5xtFxndNty1xAcziVkoBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 7 · 2026-05-11T23:09:57.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017XEUnhhrsoDmeWVihL5CrF`</summary>

```json
{
  "query": "constrained decoding information extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cdf52ca-c830-4206-86cc-06fb195c5889",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCYWoA9RLvQsspmDer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1efd75f1-b987-4210-b401-9e04921c68b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5xtFxndNty1xAcziVkoBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-11T23:09:58.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Re2R9u2SUSswco7b4Ggbqk`</summary>

```json
{
  "query": "schema-guided information extraction LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1efd75f1-b987-4210-b401-9e04921c68b3",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCYWoA9RLvQsspmDer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98eac5a2-6bd0-45b8-8e29-4c584d8f977a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5xtFxndNty1xAcziVkoBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 9 · 2026-05-11T23:09:58.549Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UFFjwSz5boeARYbSwYHzgh`</summary>

```json
{
  "query": "vLLM LogitsProcessor custom constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98eac5a2-6bd0-45b8-8e29-4c584d8f977a",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCYWoA9RLvQsspmDer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e91ef62-56f1-41a2-a177-a66f7223eef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5xtFxndNty1xAcziVkoBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-11T23:09:59.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018VNKZy2ZQqCmsBxrfkqE3j`</summary>

```json
{
  "query": "ontology-constrained generation knowledge extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e91ef62-56f1-41a2-a177-a66f7223eef1",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCYWoA9RLvQsspmDer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ccc55b33-cba7-4bc8-86cb-572704fefaf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5xtFxndNty1xAcziVkoBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 11 · 2026-05-11T23:09:59.963Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ANk5715g5gjuBRwhDVXnRh`</summary>

```json
{
  "query": "structured output information extraction joint entity relation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccc55b33-cba7-4bc8-86cb-572704fefaf6",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCYWoA9RLvQsspmDer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80be8920-a77c-4b48-99e7-d5fac474afbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5xtFxndNty1xAcziVkoBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 12 · 2026-05-11T23:10:01.006Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FWiMqZVYyJdnRsz7rYBaTm`</summary>

```json
{
  "query": "site:arxiv.org grammar constrained decoding NER relation extraction 2025 2026",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80be8920-a77c-4b48-99e7-d5fac474afbc",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCYWoA9RLvQsspmDer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2caf133-68cf-45f4-ad16-284d37e7b23f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5xtFxndNty1xAcziVkoBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 13 · 2026-05-11T23:10:01.658Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014jepr4ojvpz7U1Roa8FwAC`</summary>

```json
{
  "query": "ACE05 joint extraction LLM state of the art 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2caf133-68cf-45f4-ad16-284d37e7b23f",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdCYWoA9RLvQsspmDer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d83d471-19de-4313-b9d2-a7eaca706a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5xtFxndNty1xAcziVkoBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9059,
      "output_tokens": 387,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 387,
          "cache_read_input_tokens": 9059,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 14 · 2026-05-11T23:10:06.261Z_

<details><summary>↩ Tool result · `toolu_017XEUnhhrsoDmeWVihL5CrF`</summary>

```text
Web search results for query: "constrained decoding information extraction 2025 2026"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"Constrained Decoding of Diffusion LLMs with Context-Free Grammars | OpenReview","url":"https://openreview.net/forum?id=7Sph4KyeYO"},{"title":"A Guide to Structured Generation Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Lazy-k Decoding: Constrained Decoding for Information Extraction | OpenReview","url":"https://openreview.net/forum?id=ayoGdkXi4V&noteId=IZ0HOrxSqs"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Lazy-k Decoding: Constrained Decoding for Information Extraction - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.416/"}]

Here are the search results for "constrained decoding information extraction 2025 2026":

## Overview

Constrained decoding is a technique that manipulates a generative model's token generation process to constrain its next-token predictions to only tokens that do not violate the required output structure.

## Recent Research and Applications (2024-2026)

### Grammar-Constrained Decoding for Clinical Information Extraction
In structured information extraction, there are typically semantic and syntactic constraints on the output, and constrained decoding approaches allow specifying constraints in form of context-free grammars. Research demonstrated positive impact of grammar-constrained decoding, with an increase in F1 score of 0.351-0.425 (absolute scores 0.413-0.47) on type 2 diabetes and glaucoma datasets.

### Advanced Techniques for Diffusion LLMs (2026)
Recent work on constrained decoding for diffusion LLMs demonstrates near-perfect syntactic correctness while consistently preserving or improving functional correctness on applications such as C++ code infilling and structured data extraction in JSON.

### Performance Improvements
In information extraction, unconstrained decoding F1 often trails the constrained variant by 5–13 absolute points. Constrained decoding achieves total elimination of syntax errors on benchmarks, eliminating name, arity, type, and structure errors compared to fine-tuning or prompt-only methods.

### Recent Publications
Recent papers from 2025-2026 include "Thinking Before Constraining: A Unified Decoding Framework for Large Language Models" (2026-01), "Grammar-Constrained Decoding Makes Large Language Models Better Logical Parsers" (2025-07), and "Earley-Driven Dynamic Pruning for Efficient Structured Decoding" (2025-06).

## Production Implementation
XGrammar is the default structured generation backend for vLLM, SGLang, and TensorRT-LLM as of March 2026, achieving under 40 microseconds per token with near-zero overhead in JSON generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1efd75f1-b987-4210-b401-9e04921c68b3",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "ef8c0ccd-5a5f-4489-88b6-33e73228b3cf",
  "sourceToolAssistantUUID": "1efd75f1-b987-4210-b401-9e04921c68b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T23:10:06.652Z_

<details><summary>↩ Tool result · `toolu_01Re2R9u2SUSswco7b4Ggbqk`</summary>

```text
Web search results for query: "schema-guided information extraction LLM 2026"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"LLMs for Structured Data Extraction from PDFs in 2026","url":"https://unstract.com/blog/comparing-approaches-for-using-llms-for-structured-data-extraction-from-pdfs/"},{"title":"[2604.06571v1] LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources","url":"https://arxiv.org/abs/2604.06571v1"},{"title":"LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources","url":"https://arxiv.org/html/2604.06571v1"},{"title":"[2604.06571] LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources","url":"https://arxiv.org/abs/2604.06571"},{"title":"Exploring LLMs for Scientific Information Extraction using the SciEx Framework","url":"https://arxiv.org/pdf/2512.10004"},{"title":"(PDF) LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources","url":"https://www.researchgate.net/publication/403641712_LLM-based_Schema-Guided_Extraction_and_Validation_of_Missing-Person_Intelligence_from_Heterogeneous_Data_Sources"},{"title":"Structured data extraction from unstructured content using LLM schemas","url":"https://simonwillison.net/2025/Feb/28/llm-schemas/"},{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"}]

Here are the search results for "schema-guided information extraction LLM 2026":

## Recent Research and Developments

Recent 2026 research demonstrates active innovation in schema-guided information extraction with LLMs:

**PARSE Framework**: PARSE (Parameter Automated Refinement and Schema Extraction) is a novel system with two synergistic components: ARCHITECT, which autonomously optimizes JSON schemas for LLM consumption while maintaining backward compatibility, and SCOPE, which implements reflection-based extraction with combined static and LLM-based guardrails. The framework achieves up to 64.7% improvement in extraction accuracy on SWDE with combined framework improvements reaching 10% across models.

**Guardian Parser Pack**: On a manually aligned subset of 75 cases, the LLM-assisted pathway achieved substantially higher extraction quality than the deterministic comparator (F1 = 0.8664 vs. 0.2578), while across 517 parsed records per pathway it also improved aggregate key-field completeness (96.97% vs. 93.23%). The system uses a dual-path extractor with shared deterministic validation: rule-based parsing provides reproducibility and speed for known layouts, while LLM assistance improves extraction quality and completeness for narrative-heavy or irregular documents.

**SciEx Framework**: Retrieved evidence is passed to an LLM which performs schema-guided extraction to produce structured records or tuples that conform to the schema, with schema-constrained decoding ensuring that each extracted field adheres to the expected format and type.

## Key Approaches

Many of the leading LLM providers now bake schema-guided extraction in as a feature, with OpenAI, Anthropic, Gemini and Mistral all offering variants of "structured output" through their APIs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98eac5a2-6bd0-45b8-8e29-4c584d8f977a",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "69b6df7e-9b6e-417a-8cf9-ce9cb8070dc7",
  "sourceToolAssistantUUID": "98eac5a2-6bd0-45b8-8e29-4c584d8f977a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T23:10:07.417Z_

<details><summary>↩ Tool result · `toolu_01UFFjwSz5boeARYbSwYHzgh`</summary>

```text
Web search results for query: "vLLM LogitsProcessor custom constraints"

Links: [{"title":"Custom Logits Processors - vLLM","url":"https://docs.vllm.ai/en/stable/features/custom_logitsprocs/"},{"title":"Logits Processors - vLLM","url":"https://docs.vllm.ai/en/latest/design/logits_processors/"},{"title":"logits_processor - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/"},{"title":"vllm/examples/features/logits_processor at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/tree/main/examples/features/logits_processor"},{"title":"How to use logits_processors · Issue #1728 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/1728"},{"title":"vllm/vllm/model_executor/layers/logits_processor.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/logits_processor.py"},{"title":"Custom Guided Decoding Backend (Experimental) — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/1.7.0/custom-decoding-backend.html"},{"title":"Custom Guided Decoding Backends with NVIDIA NIM for LLMs — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/latest/custom-decoding-backend.html"},{"title":"[Usage]: Logits processor with v1 · Issue #21672 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/21672"},{"title":"vLLM V1 User Guide — vLLM","url":"https://docs.vllm.ai/en/v0.8.1/getting_started/v1_user_guide.html"}]

Based on the search results, here's comprehensive information about vLLM LogitsProcessor custom constraints:

## Overview

Logits processors allow you to modify the model's output distribution before sampling, enabling controlled generation behaviors like token masking, constrained decoding, and custom sampling strategies.

## Implementation Requirements

Custom logits processors must subclass vllm.v1.sample.logits_processor.LogitsProcessor and define (at minimum) the following methods: validate_params(cls, sampling_params: SamplingParams): Raise ValueError if SamplingParams has invalid arguments (especially custom arguments) used by logits processor.

The essential methods to implement are:

1. **__init__**: Requires vllm_config: VllmConfig, device: torch.device, and is_pin_memory: bool parameters.

2. **apply()**: Consume a (num_requests) x (vocab_size) logits tensor and apply logits processor transformation at batch granularity.

3. **update_state()**: Called when there are new output tokens, prior to each forward pass. batch_update is non-None iff there have been changes to the batch makeup.

## Batch vs. Request-Level Processing

vLLM processes logits at the batch level for efficiency. If you have a per-request processor, you need to wrap it using the patterns shown in custom_req.py and custom_req_init.py.

## Passing Custom Parameters

Use SamplingParams.extra_args to pass custom keyword arguments to your logits processor on a per-request basis (e.g., target_token).

## Examples

Example code is available demonstrating how to use custom logits processors with vLLM's offline inference API, showing controlled generation behaviors like token masking, constrained decoding, and custom sampling strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e91ef62-56f1-41a2-a177-a66f7223eef1",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "b44b70f9-8eca-41da-933b-3e6f632a04ed",
  "sourceToolAssistantUUID": "8e91ef62-56f1-41a2-a177-a66f7223eef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T23:10:07.638Z_

<details><summary>↩ Tool result · `toolu_018VNKZy2ZQqCmsBxrfkqE3j`</summary>

```text
Web search results for query: "ontology-constrained generation knowledge extraction 2025 2026"

Links: [{"title":"Scientific knowledge graph and ontology generation using open large language models - Digital Discovery (RSC Publishing) DOI:10.1039/D5DD00275C","url":"https://pubs.rsc.org/en/content/articlehtml/2026/dd/d5dd00275c"},{"title":"Axiom Generation for Automated Ontology Construction from Texts Through Schema Mapping","url":"https://www.mdpi.com/2504-4990/8/2/29"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"[2509.04696] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/abs/2509.04696"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/html/2510.20345v1"},{"title":"Ontology Learning and Knowledge Graph Construction: A Comparison of Approaches and Their Impact on RAG Performance","url":"https://arxiv.org/html/2511.05991v1"},{"title":"(PDF) ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://www.researchgate.net/publication/395338944_ODKE_Ontology-Guided_Open-Domain_Knowledge_Extraction_with_LLMs"},{"title":"OntoKG: Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing","url":"https://arxiv.org/html/2604.02618v1"},{"title":"Beyond Context Graphs: How Ontology, Semantics, and Knowledge Graphs Define Context","url":"https://yearofthegraph.xyz/newsletter/2026/03/beyond-context-graphs-how-ontology-semantics-and-knowledge-graphs-define-context-the-year-of-the-graph-newsletter-vol-30-spring-2026/"}]

Based on the search results, here are the key findings on ontology-constrained generation and knowledge extraction for 2025-2026:

## Recent Developments in Ontology-Constrained Knowledge Extraction

**Production Systems and Deployment:**

ODKE+ has been deployed in production knowledge graph infrastructure since May 2025, processing an average of 150-250K new facts per day in streaming mode with end-to-end latency under 2 hours. The system dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints, processing over 9 million Wikipedia pages and ingesting 19 million high-confidence facts with 98.8% precision.

**Automated Ontology Generation:**

Knowledge graphs are increasingly recognized for their potential to enhance the factuality and reasoning capabilities of Large Language Models. Ontology learning from unstructured text has become a critical task, though the generation of formal Description Logic axioms required for constructing logically consistent and computationally tractable ontologies remains largely underexplored.

**Integration with RAG Systems:**

Ontology-guided Knowledge Graphs that included chunk information achieved 90% accuracy in retrieval tasks, showing that retrieval over an ontology-constrained KG can match state-of-the-art frameworks when text segments are integrated directly into the graph structure.

**LLM-Driven Ontology Modeling:**

LLMs serve as advanced co-modelers that assist human experts in translating natural language specifications into formal ontologies, prioritizing conceptual abstraction and structured semantic representation to ensure knowledge extraction adheres to well-defined logical constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccc55b33-cba7-4bc8-86cb-572704fefaf6",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "5e75c7bd-7ee1-4477-a9c4-c43a956ab3ad",
  "sourceToolAssistantUUID": "ccc55b33-cba7-4bc8-86cb-572704fefaf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T23:10:08.042Z_

<details><summary>↩ Tool result · `toolu_01ANk5715g5gjuBRwhDVXnRh`</summary>

```text
Web search results for query: "structured output information extraction joint entity relation 2026"

Links: [{"title":"Structured information extraction from scientific text with large language models","url":"https://ideas.repec.org/a/nat/natcom/v15y2024i1d10.1038_s41467-024-45563-x.html"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"A relation semantics-guided top-down approach for joint entity and relation extraction in complex scenarios - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095070512600376X"},{"title":"Joint entity and relation extraction with table filling based on graph convolutional Networks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095741742402997X"},{"title":"Joint Entity and Relation Extraction Network with Enhanced Explicit and Implicit Semantic Information","url":"https://www.mdpi.com/2076-3417/12/12/6231"},{"title":"Construction and Application of Text Entity Relation Joint Extraction Model Based on Multi-Head Attention Neural Network - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9155959/"},{"title":"RSTGP: A Relation-Aware and Span-Graph-Enhanced Method for Joint Entity and Relation Extraction from Medical Texts","url":"https://www.mdpi.com/2076-3417/16/9/4102"},{"title":"Joint extraction model of entity relations based on decomposition strategy | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-51559-w"},{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"},{"title":"Research on joint model relation extraction method based on entity mapping - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10889875/"}]

Based on the search results, here's what I found about structured output information extraction for joint entity and relation extraction in 2026:

## Recent Developments

Large language models like GPT-3 and Llama-2 can be fine-tuned to extract useful records of complex scientific knowledge through joint named entity recognition and relation extraction.

Records can be extracted from single sentences or entire paragraphs, with output returned as simple English sentences or more structured formats such as JSON objects.

## Current Research Focus (2026)

Recent research in 2026 is addressing several key challenges:

Many existing models experience performance degradation when processing sentences containing multiple entities and intricate relationships, particularly when handling overlapping triples, as one or more entities frequently participate simultaneously in multiple relational facts.

Medical texts are characterized by dense terminology, syntactically complex expressions, and frequent overlapping triplets, and table-filling methods like GPLinker remain limited in modeling cross-relation interactions and capturing latent structural dependencies among candidate spans.

## New Approaches

A recent unified joint extraction framework called RSTGP integrates three key mechanisms: a relation-aware scoring strategy, a span-level graph enhancement mechanism, and a type-constrained calibration mechanism.

Joint entity and relation extraction is a fundamental task in information extraction for identifying structured knowledge triples from unstructured text.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80be8920-a77c-4b48-99e7-d5fac474afbc",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "beb75da8-4abb-4ce6-8759-eb44b947c333",
  "sourceToolAssistantUUID": "80be8920-a77c-4b48-99e7-d5fac474afbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T23:10:08.526Z_

<details><summary>↩ Tool result · `toolu_01FWiMqZVYyJdnRsz7rYBaTm`</summary>

```text
Web search results for query: "site:arxiv.org grammar constrained decoding NER relation extraction 2025 2026"

Links: [{"title":"[2305.13971] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/abs/2305.13971"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/html/2305.13971v6"},{"title":"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/html/2404.12493"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Flexible Grammar-Based Constrained Decoding for Language Models","url":"https://arxiv.org/pdf/2305.13971v2"},{"title":"[2502.05111] Flexible and Efficient Grammar-Constrained Decoding","url":"https://arxiv.org/abs/2502.05111"},{"title":"Flexible and Efficient Grammar-Constrained Decoding","url":"https://arxiv.org/pdf/2502.05111"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/html/2408.02361"}]

Based on the search results, here are the relevant papers from arXiv on grammar-constrained decoding for NER and relation extraction published in 2025-2026:

## Recent Papers (2025-2026)

1. **"Grammar-Aligned Decoding"** (2405.21047, updated December 2025)
   - Proposes grammar-constrained decoding (GCD) where LLM output must follow a given grammar, introducing adaptive sampling with approximate expected futures (ASAp) as a decoding algorithm
   - Evaluation on code generation and structured NLP tasks shows ASAp produces outputs with higher likelihood than existing GCD techniques while enforcing grammatical constraints

2. **"Flexible and Efficient Grammar-Constrained Decoding"** (2502.05111, updated July 2025)
   - Grammar-constrained decoding can guarantee that LLM outputs match specified rules by masking out tokens that will provably lead to outputs not belonging to a specified context-free grammar

3. **"CRANE: Reasoning with constrained LLM generation"** (2502.09061, published May 2025)
   - Proposes a reasoning-augmented constrained decoding algorithm that balances the correctness of constrained generation with the flexibility of unconstrained generation

## Related Earlier Work

Additionally, there are foundational papers on this topic:
- Formal grammars can describe output spaces for structured NLP tasks, with input-dependent grammars allowing grammar to depend on input and enable generation of different output structures for different inputs
- EnriCo model integrates span-level and relation-level attention mechanisms with constraint-based decoding for joint entity and relation extraction


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2caf133-68cf-45f4-ad16-284d37e7b23f",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "96a8d121-3590-4c35-96e0-565f5ded618f",
  "sourceToolAssistantUUID": "e2caf133-68cf-45f4-ad16-284d37e7b23f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T23:10:08.611Z_

<details><summary>↩ Tool result · `toolu_014jepr4ojvpz7U1Roa8FwAC`</summary>

```text
Web search results for query: "ACE05 joint extraction LLM state of the art 2025 2026"

Links: [{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction","url":"https://arxiv.org/html/2401.01326v1"},{"title":"Joint entity and relation extraction based on a hybrid neural network - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231217301613"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Extracting Entities and Relations with Joint Minimum Risk Training - ACL Anthology","url":"https://aclanthology.org/D18-1249/"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"AI Model Release Timeline 2025–2026 — Every LLM Launch Tracked | AI Flash Report","url":"https://aiflashreport.com/model-releases.html"}]

Based on the search results, here's what I found about ACE05 joint extraction with LLMs and the current state of the art:

## Recent Developments (2025-2026)

A novel LLM augmented joint learning framework named Reamend was proposed for entity-relation extraction, with experimental results on benchmark datasets demonstrating superior performance compared to state-of-the-art baseline methods. The framework leverages LLMs to simultaneously recognize potential entities and corresponding relations from text, with entity-relation amendment introduced to eliminate redundant triplets.

## Key Findings on Relation Extraction

Recent survey research (published in 2024-2025) analyzing 137 papers from ACL conferences shows that BERT-based methods dominate in achieving state-of-the-art results for relation extraction, while emerging Large Language Models like T5 show promising capabilities especially in few-shot relation extraction scenarios where they excel in identifying previously unseen relations.

For ACE05 specifically, the UNIRE model based on BERT-base-uncased, ALBERT, and SciBERT achieves state-of-the-art performance on the ACE04 and ACE05 datasets.

## Current LLM Capabilities

Transformer-based LLMs have emerged as state-of-the-art technologies capable of understanding and extracting structured information from unstructured documents with high accuracy. However, existing large language models face challenges in extracting all potential triplets without specialized adjustments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d83d471-19de-4313-b9d2-a7eaca706a52",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "026a4214-c6ef-4973-a69e-b50a331e8ac4",
  "sourceToolAssistantUUID": "7d83d471-19de-4313-b9d2-a7eaca706a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-11T23:10:11.245Z_

Let me now fetch some of the most relevant papers to get more detail on the closest competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "026a4214-c6ef-4973-a69e-b50a331e8ac4",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdDbjYm9X9x3jdbBRrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d96e42c-9ccc-43a0-8707-d7cc61947e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BVMkE9g3HDDBbFhomFZYz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7205,
      "cache_read_input_tokens": 10972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7205,
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

_source line 22 · 2026-05-11T23:10:13.909Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ni7T3cHtWk3zmweuZMNkmY`</summary>

```json
{
  "url": "https://openreview.net/forum?id=ayoGdkXi4V",
  "prompt": "Extract the full paper title, authors, venue, date, and a summary of the approach. Is this about constrained decoding specifically for information extraction? What constraints do they use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d96e42c-9ccc-43a0-8707-d7cc61947e1f",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdDbjYm9X9x3jdbBRrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "717d1d3d-fc10-486e-8a01-07eb3dff74cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BVMkE9g3HDDBbFhomFZYz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7205,
      "cache_read_input_tokens": 10972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7205,
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

_source line 23 · 2026-05-11T23:10:15.074Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y4dgLj55E7fE3J3Hta9Gxh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2305.13971",
  "prompt": "Extract the full paper title, authors, date, and summary. Does this paper apply grammar-constrained decoding to NER or relation extraction? What tasks does it cover? What grammars are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "717d1d3d-fc10-486e-8a01-07eb3dff74cf",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdDbjYm9X9x3jdbBRrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "627af823-fc5f-4f3a-aac7-8241163bf064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BVMkE9g3HDDBbFhomFZYz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7205,
      "cache_read_input_tokens": 10972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7205,
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

_source line 24 · 2026-05-11T23:10:16.948Z_

<details><summary>↩ Tool result · `toolu_01Ni7T3cHtWk3zmweuZMNkmY`</summary>

```text
# Paper Summary

**Title:** "Lazy-k Decoding: Constrained Decoding for Information Extraction"

**Authors:** Arthur Hemmer, Mickael Coustaty, Nicola Bartolo, Jerome Brachat, Jean-marc Ogier

**Venue:** EMNLP 2023 Conference

**Publication Date:** October 7, 2023

## Approach Overview

Yes, this work specifically addresses constrained decoding for information extraction through token classification. The researchers present a method that "combine[s] the models with constrained decoding approaches" to perform structured prediction while satisfying constraint requirements.

## Key Innovation

The team proposes a novel decoding algorithm called Lazy-k that enables flexible trade-offs between computational efficiency and accuracy. This approach "search[es] for constraint-satisfying label-assignments while maximizing the total probability," improving upon probabilistic models—particularly smaller variants.

## Constraint Details

While the abstract doesn't explicitly detail the specific constraint types, the work evaluates multiple existing constrained decoding approaches alongside their novel method. The implementation is available at their GitHub repository for practical application in token classification tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "717d1d3d-fc10-486e-8a01-07eb3dff74cf",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "44849176-7918-4931-a682-60e417b277a6",
  "sourceToolAssistantUUID": "717d1d3d-fc10-486e-8a01-07eb3dff74cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-11T23:10:17.077Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015jYAchNqEcUkgZK3BgXops`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.04696",
  "prompt": "Extract the full paper title, authors, date, and summary. How does ODKE+ use ontology constraints during generation? Does it use constrained decoding or just prompting? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44849176-7918-4931-a682-60e417b277a6",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdDbjYm9X9x3jdbBRrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca33e2b9-b5b7-4de5-87b6-c8ff704ad959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BVMkE9g3HDDBbFhomFZYz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7205,
      "cache_read_input_tokens": 10972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7205,
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

_source line 26 · 2026-05-11T23:10:18.874Z_

<details><summary>↩ Tool result · `toolu_01Y4dgLj55E7fE3J3Hta9Gxh`</summary>

```text
# Paper Summary

**Title:** "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning"

**Authors:** Saibo Geng, Martin Josifoski, Maxime Peyrard, Robert West

**Date:** Submitted May 23, 2023; last revised January 18, 2024

**Summary:** The paper proposes using formal grammars to constrain language model outputs for structured tasks without requiring finetuning. It introduces input-dependent grammars that adapt based on input data.

## Task Coverage

The work applies grammar-constrained decoding to three tasks:
1. Information extraction
2. Entity disambiguation
3. Constituency parsing

**NER and Relation Extraction:** The abstract does not explicitly mention named entity recognition or relation extraction as tested tasks. However, information extraction can encompass these domains.

## Grammars Used

The page does not provide specific details about which formal grammar types (e.g., context-free grammars, regular expressions) were employed. The abstract emphasizes that "formal grammars can describe the output space" for various structured tasks but does not enumerate particular grammar specifications or formalisms used in the implementation.

Code and data are available at the referenced GitHub repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "627af823-fc5f-4f3a-aac7-8241163bf064",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "d9f891e9-8df3-4591-bf95-61351622f7c7",
  "sourceToolAssistantUUID": "627af823-fc5f-4f3a-aac7-8241163bf064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-11T23:10:18.962Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014LKphiPeHQB49sLyhQNtFt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.09061",
  "prompt": "Extract the full paper title, authors, date, and summary. What is CRANE's approach to constrained reasoning? Does it combine grammar constraints with semantic callbacks or dynamic constraints? What tasks is it evaluated on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9f891e9-8df3-4591-bf95-61351622f7c7",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdDbjYm9X9x3jdbBRrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0107d93f-7eb2-4f2e-b6b1-b856f0a702a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BVMkE9g3HDDBbFhomFZYz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7205,
      "cache_read_input_tokens": 10972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7205,
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

_source line 28 · 2026-05-11T23:10:20.360Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RbQ1ife3XKUwAKCcTPSL9h`</summary>

```json
{
  "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/",
  "prompt": "Extract the full paper title, authors, venue, date, and summary. How does this paper use grammar-constrained decoding for information extraction? What grammar formalism is used? Does it use callbacks or semantic constraints beyond syntax?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0107d93f-7eb2-4f2e-b6b1-b856f0a702a3",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdDbjYm9X9x3jdbBRrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e6c2813-3141-42bf-9b9d-9e6673406f43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BVMkE9g3HDDBbFhomFZYz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7205,
      "cache_read_input_tokens": 10972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7205,
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

_source line 29 · 2026-05-11T23:10:21.790Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014AE1xXXtWLyNtaNkioqTaQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.05111",
  "prompt": "Extract the full paper title, authors, date, and summary. What does 'flexible' mean here - does it support callbacks, semantic constraints, or hybrid grammar approaches? What tasks is it evaluated on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e6c2813-3141-42bf-9b9d-9e6673406f43",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdDbjYm9X9x3jdbBRrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10aa9679-88ab-4351-8049-c7cae46dfcd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BVMkE9g3HDDBbFhomFZYz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7205,
      "cache_read_input_tokens": 10972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7205,
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

_source line 30 · 2026-05-11T23:10:22.601Z_

<details><summary>↩ Tool result · `toolu_015jYAchNqEcUkgZK3BgXops`</summary>

```text
# ODKE+: Research Paper Summary

**Full Title:** ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs

**Authors:** Samira Khorshidi, Azadeh Nikfarjam, Suprita Shankar, Yisi Sang, Yash Govind, Hyun Jang, Ali Kasgari, Alexis McClimans, Mohamed Soliman, Vishnu Konda, Ahmed Fakhry, Xiaoguang Qi

**Submission Date:** September 4, 2025

## Ontology Integration Approach

The paper indicates ODKE+ uses **ontology-guided prompting** rather than constrained decoding. The system "dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints." This suggests the approach incorporates schema information into LLM prompts to guide generation toward type-consistent outputs.

## Key Results

- **Scale:** Processed over 9 million Wikipedia pages and ingested 19 million high-confidence facts
- **Precision:** Achieved 98.8% precision in extracted facts
- **Coverage:** Up to 48% overlap with third-party knowledge graphs
- **Efficiency:** Reduced update lag by 50 days on average compared to traditional methods
- **Scope:** Handles 195 different predicates across diverse entity types

The system combines pattern-based rules with LLM-based extraction, verification through a secondary LLM grounder, and fact ranking/normalization for production-grade knowledge ingestion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca33e2b9-b5b7-4de5-87b6-c8ff704ad959",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "b916279c-61d3-42f2-9126-3c5395bc6e9d",
  "sourceToolAssistantUUID": "ca33e2b9-b5b7-4de5-87b6-c8ff704ad959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-11T23:10:23.217Z_

<details><summary>↩ Tool result · `toolu_014LKphiPeHQB49sLyhQNtFt`</summary>

```text
# CRANE: Reasoning with Constrained LLM Generation

**Full Title:** "CRANE: Reasoning with constrained LLM generation"

**Authors:** Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, Gagandeep Singh

**Date:** Submitted February 13, 2025; last revised September 5, 2025 (accepted at ICML 2025)

## Summary

The paper addresses a fundamental challenge: strict grammar constraints on LLM outputs often reduce reasoning capabilities. CRANE tackles this tension through a novel approach.

## CRANE's Approach

Rather than applying only restrictive grammar rules, CRANE "augment[s] the output grammar with carefully designed additional rules" to preserve both reasoning flexibility and correctness. The method employs "a reasoning-augmented constrained decoding algorithm" that balances these competing demands without relying on separate semantic callbacks or dynamic constraint mechanisms—instead, the expanded grammar itself enables reasoning while maintaining syntactic and semantic validity.

## Evaluation Tasks

CRANE is tested on:
- Code generation
- Symbolic math reasoning
- GSM-symbolic benchmark
- FOLIO benchmark

Results show "up to 10% points accuracy improvement over baselines" on challenging symbolic reasoning tasks compared to both constrained and unconstrained baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0107d93f-7eb2-4f2e-b6b1-b856f0a702a3",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "ef07d4d7-c244-475b-9829-96a05c240c48",
  "sourceToolAssistantUUID": "0107d93f-7eb2-4f2e-b6b1-b856f0a702a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-11T23:10:23.298Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PEtN7QPrBnKfw8tXe5RJgD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2408.02361",
  "prompt": "Extract the full paper title, authors, date, venue, and summary. This is about dialogue ontology relation extraction via constrained chain-of-thought decoding. How does it constrain the output? Does it use grammar constraints or ontology constraints?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef07d4d7-c244-475b-9829-96a05c240c48",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdDbjYm9X9x3jdbBRrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a537ca60-2f57-4211-b0dd-711f85f398e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BVMkE9g3HDDBbFhomFZYz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7205,
      "cache_read_input_tokens": 10972,
      "output_tokens": 818,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7205
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 818,
          "cache_read_input_tokens": 10972,
          "cache_creation_input_tokens": 7205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7205,
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

_source line 33 · 2026-05-11T23:10:25.893Z_

<details><summary>↩ Tool result · `toolu_014AE1xXXtWLyNtaNkioqTaQ`</summary>

```text
# Paper Summary

**Title:** Flexible and Efficient Grammar-Constrained Decoding

**Authors:** Kanghee Park, Timothy Zhou, Loris D'Antoni

**Date:** Submitted February 7, 2025; revised July 15, 2025

**Summary:**
This research addresses grammar-constrained decoding (GCD) for large language models. The authors present an algorithm that enables LLMs to generate structured outputs conforming to context-free grammars (CFGs). Their key contribution is a "17.71x faster offline preprocessing than existing approaches" while maintaining competitive online efficiency.

## On "Flexible"

The page content provided does not explicitly detail what "flexible" encompasses. The abstract focuses on computational efficiency improvements rather than specifying whether the approach supports callbacks, semantic constraints, or hybrid grammar approaches.

## Evaluation Details

The available content does not describe specific tasks or benchmarks used for evaluation. The emphasis throughout is on preprocessing speed and mask computation efficiency as the primary performance metrics, but actual application domains or test cases are not mentioned in this excerpt.

To learn what flexibility features and evaluation tasks are included, the full PDF would need to be consulted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10aa9679-88ab-4351-8049-c7cae46dfcd8",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "9accb909-f039-4707-aefb-2880e38e2c17",
  "sourceToolAssistantUUID": "10aa9679-88ab-4351-8049-c7cae46dfcd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-11T23:10:26.017Z_

<details><summary>↩ Tool result · `toolu_01RbQ1ife3XKUwAKCcTPSL9h`</summary>

```text
# Paper Analysis

## Bibliographic Information

**Title:** "Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts"

**Authors:** David M Schmidt, Philipp Cimiano

**Venue:** Frontiers in Artificial Intelligence

**Date:** January 7, 2025 (Published); December 12, 2024 (Accepted)

**DOI:** 10.3389/frai.2024.1406857

## Grammar-Constrained Decoding Application

The paper employs grammar-constrained decoding (GCD) to ensure output validity in structured information extraction from clinical trial abstracts. The approach masks the vocabulary at each decoding step based on tokens valid according to a context-free grammar, guaranteeing syntactically correct outputs.

## Grammar Formalism

The research uses **context-free grammars (CFGs)** implemented via the **Lark parsing toolkit** in LALR parsing mode. The grammar defines the linearized structure of the C-TrO ontology, with special tokens for slot and template boundaries like `[start:slotName]` and `[end:slotName]`.

## Constraint Scope

The constraints are **purely syntactic**, not semantic. The grammar enforces:
- Valid token sequences following production rules
- Proper nesting of templates and slots
- Correct boundary tag matching

The paper explicitly states the approach uses the "domain-specific grammar to ensure that output structures follow the requirements" but focuses on structural validity rather than semantic constraints. No callbacks or semantic validation mechanisms beyond grammar rule enforcement are described.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e6c2813-3141-42bf-9b9d-9e6673406f43",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "0509db25-d99f-4185-86c0-c589042d0499",
  "sourceToolAssistantUUID": "2e6c2813-3141-42bf-9b9d-9e6673406f43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-11T23:10:27.887Z_

<details><summary>↩ Tool result · `toolu_01PEtN7QPrBnKfw8tXe5RJgD`</summary>

```text
# Dialogue Ontology Relation Extraction Paper Summary

**Title:** Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding

**Authors:** Renato Vukovic, David Arps, Carel van Niekerk, Benjamin Matthias Ruppik, Hsien-Chin Lin, Michael Heck, Milica Gašić

**Date:** Submitted August 5, 2024; revised March 7, 2025

**Venue:** SIGDIAL 2024

## Summary

This research addresses automated dialogue ontology construction, specifically focusing on relation extraction. The authors adapt Chain-of-Thought decoding—a technique originally designed for reasoning tasks—to improve generalization in relation extraction through a transfer learning approach.

## Constraint Mechanism

The paper employs **ontology constraints** rather than grammar constraints. According to the abstract: "By constraining the decoding to ontology terms and relations, we aim to decrease the risk of hallucination."

The constrained approach operates by generating multiple decoding branches and selecting relations based on confidence thresholds, while limiting outputs to predefined ontology vocabulary and valid relation types. This design reduces spurious outputs from the language model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a537ca60-2f57-4211-b0dd-711f85f398e5",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "c71e89b1-737a-48c1-bf0c-585f5f3bfa2b",
  "sourceToolAssistantUUID": "a537ca60-2f57-4211-b0dd-711f85f398e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-11T23:10:31.174Z_

Let me now search for a few more specific areas to be thorough -- particularly hybrid/callback approaches and recent ACE05 numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c71e89b1-737a-48c1-bf0c-585f5f3bfa2b",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdF2A1d85HRViXVYKMm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3975ecc3-20a5-4957-8874-553d240e4c1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYJS1NpM7hp3SzuNVstWvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3082,
      "cache_read_input_tokens": 18177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3082,
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

_source line 37 · 2026-05-11T23:10:32.260Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xinf6dJ1Y7WzNJB6UpXFsn`</summary>

```json
{
  "query": "\"semantic constraints\" \"logits processor\" constrained decoding callback 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3975ecc3-20a5-4957-8874-553d240e4c1b",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdF2A1d85HRViXVYKMm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8400e4a-d624-4ffe-be53-adc66a1e37fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYJS1NpM7hp3SzuNVstWvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3082,
      "cache_read_input_tokens": 18177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3082,
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

_source line 38 · 2026-05-11T23:10:33.348Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015fXqJ3qRXv4CaqUZcrz8Fi`</summary>

```json
{
  "query": "arxiv \"structured decoding\" \"information extraction\" ontology grammar hybrid 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8400e4a-d624-4ffe-be53-adc66a1e37fd",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdF2A1d85HRViXVYKMm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0855b34-5f9d-4adf-83a6-da087377f5aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYJS1NpM7hp3SzuNVstWvM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3082,
      "cache_read_input_tokens": 18177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3082,
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

_source line 39 · 2026-05-11T23:10:33.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015oSuf1GdYZFkkQWmn9kyrN`</summary>

```json
{
  "query": "ACE05 joint entity relation event extraction SOTA results 2025 leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0855b34-5f9d-4adf-83a6-da087377f5aa",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdF2A1d85HRViXVYKMm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b641e1c-b34c-4931-beca-73b4d24ea139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYJS1NpM7hp3SzuNVstWvM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3082,
      "cache_read_input_tokens": 18177,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3082
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 18177,
          "cache_creation_input_tokens": 3082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3082,
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

_source line 40 · 2026-05-11T23:10:40.462Z_

<details><summary>↩ Tool result · `toolu_015oSuf1GdYZFkkQWmn9kyrN`</summary>

```text
Web search results for query: "ACE05 joint entity relation event extraction SOTA results 2025 leaderboard"

Links: [{"title":"[1905.05529] Entity-Relation Extraction as Multi-Turn Question Answering","url":"https://arxiv.org/abs/1905.05529"},{"title":"ACE 2005 Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-ace-2005"},{"title":"Position-aware Joint Entity and Relation Extraction with Attention Mechanism","url":"https://www.ijcai.org/proceedings/2022/0624.pdf"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"GitHub - michaelmoju/ace05_ERE: Entity/Relation/Event extraction on ACE 2005 corpus","url":"https://github.com/michaelmoju/ace05_ERE"},{"title":"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction","url":"https://arxiv.org/html/2401.01326v1"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"JSEEGraph: Joint Structured Event Extraction as Graph Parsing","url":"https://arxiv.org/pdf/2306.14633"},{"title":"[PDF] The ACE 2005 ( ACE 05 ) Evaluation Plan Evaluation of the Detection and Recognition of ACE Entities , Values , Temporal Expressions , Relations , and Events 1 | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-ACE-2005-(-ACE-05-)-Evaluation-Plan-Evaluation-Ntroduction/3a9b136ca1ab91592df36f148ef16095f74d009e"}]

Based on my search results, I found relevant information about ACE05 joint entity, relation, and event extraction, though specific 2025 leaderboard results are limited in the search results.

## Key SOTA Results for ACE05:

The multi-turn question answering paradigm for entity-relation extraction achieved state-of-the-art results on ACE05 with a score of 60.2 (from 2019 research).

A position-aware joint entity and relation extraction method outperformed previous state-of-the-art with an absolute F1 improvement of +4.7% on ACE05 for relation extraction (from 2022).

The UNIRE model, based on BERT-base-uncased, ALBERT, and SciBERT, achieves state-of-the-art performance on the ACE05 dataset.

## Event Extraction on ACE05:

For event extraction specifically, recent SOTA approaches achieved 63.9 on argument role classification, and all state-of-the-art approaches for event extraction utilize a pre-trained language model (PLM).

The search results show that ACE05 is a key dataset for event extraction evaluation across sentence, document, and cross-document scopes.

However, the search results don't contain a comprehensive 2025 leaderboard with all current SOTA results. For the most up-to-date leaderboard, you may want to check Papers with Code's ACE05 benchmarks directly, which typically maintains current SOTA rankings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b641e1c-b34c-4931-beca-73b4d24ea139",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "5bc0047b-e4ea-4b64-b7b3-57fac286b73b",
  "sourceToolAssistantUUID": "4b641e1c-b34c-4931-beca-73b4d24ea139",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-11T23:10:40.672Z_

<details><summary>↩ Tool result · `toolu_01Xinf6dJ1Y7WzNJB6UpXFsn`</summary>

```text
Web search results for query: ""semantic constraints" "logits processor" constrained decoding callback 2025 2026"

Links: [{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Controlling your LLM: Deep dive into Constrained Generation | by Andrew Docherty | Medium","url":"https://medium.com/@docherty/controlling-your-llm-deep-dive-into-constrained-generation-1e561c736a20"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603v1"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"Constrained Decoding with Triton Inference Server — NVIDIA Triton Inference Server","url":"https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Feature_Guide/Constrained_Decoding/README.html"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a2d537e69a6c6638a3630eef835f07de-Paper-Conference.pdf"}]

Based on the search results, here's what I found about semantic constraints, logits processors, and constrained decoding in 2025-2026:

## Core Mechanism

Constrained decoding inserts a logit processor between the model's output and the sampling step. The fundamental technique of constrained generation boils down to "masking", or reducing the logits of, unwanted tokens.

## Semantic Constraints Integration

Grammar-guided generation has been extended to incorporate task-specific semantic constraints. For constrained decoding applications, syntactic constraints via context-free grammar are enforced alongside semantic constraints ensuring that generated expressions contain only valid problem-defined variables.

## Recent Advances (2025-2026)

XGrammar is the default structured generation backend for vLLM, SGLang, and TensorRT-LLM as of March 2026, achieving under 40 microseconds per token with near-zero overhead in JSON generation. llguidance from Microsoft uses a Rust-based Earley parser at ~50 microseconds per token, and OpenAI publicly credited llguidance for foundational work underpinning their Structured Outputs in May 2025.

## Advanced Techniques

Recent implementations include dynamic tree-of-parsers frameworks providing per-step context-sensitive regular expressions that strictly enforce semantic and runtime correctness for domain-specific scripting languages. Additionally, IterGen (ICLR 2025) introduces forward/backward generation tied to grammar symbols, with KV-cache reuse making "undo and redo" efficient.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8400e4a-d624-4ffe-be53-adc66a1e37fd",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "e37c1c33-89c8-4db0-81d7-035be8041b72",
  "sourceToolAssistantUUID": "f8400e4a-d624-4ffe-be53-adc66a1e37fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-11T23:10:42.253Z_

<details><summary>↩ Tool result · `toolu_015fXqJ3qRXv4CaqUZcrz8Fi`</summary>

```text
Web search results for query: "arxiv "structured decoding" "information extraction" ontology grammar hybrid 2025"

Links: [{"title":"arXiv:2506.00664v1 [cs.AI] 31 May 2025 1","url":"https://arxiv.org/pdf/2506.00664"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"[2506.00664] OntoRAG: Enhancing Question-Answering through Automated Ontology Derivation from Unstructured Knowledge Bases","url":"https://arxiv.org/abs/2506.00664"},{"title":"OntoRAG: Enhancing Question-Answering through Automated Ontology Derivation from Unstructured Knowledge Bases","url":"https://arxiv.org/html/2506.00664v1"},{"title":"Evo-DKD: Dual-Knowledge Decoding for Autonomous Ontology","url":"https://arxiv.org/pdf/2507.21438"},{"title":"[2509.04696] ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/abs/2509.04696"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"Ontology Guided Information Extraction from Unstructured ...","url":"https://arxiv.org/pdf/1302.1335"}]

I found several relevant papers combining structured decoding, information extraction, ontology, and grammar approaches from 2025 and recent years:

## Key Papers Found:

### 1. **Grammar-constrained decoding for structured information extraction** (2025)
This work experimentally investigates the influence of grammar-constrained decoding and pointer generators on the performance of a domain-specific information extraction system, considering fine-tuned encoder-decoder models like Longformer and Flan-T5. The task involves inducing structured representations from abstracts describing clinical trials, relying on the C-TrO ontology.

### 2. **OntoRAG: Automated Ontology Derivation** (May 2025)
OntoRAG is an automated pipeline designed to derive ontologies from unstructured knowledge bases, integrating advanced techniques including web scraping, PDF parsing, hybrid chunking, information extraction, knowledge graph construction, and ontology creation. By leveraging LLMs and graph-based methods, OntoRAG enhances global sensemaking capabilities, outperforming conventional RAG and GraphRAG approaches.

### 3. **ODKE+: Ontology-Guided Open-Domain Knowledge Extraction** (September 2025)
ODKE+ combines modular components into a scalable pipeline with hybrid Knowledge Extractors that apply both pattern-based rules and ontology-guided prompting for large language models. It dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints, enabling scalable, type-consistent fact extraction across 195 predicates.

### 4. **Evo-DKD: Dual-Knowledge Decoding for Autonomous Ontology** (2025)
This approach uses a Structured Decoder that proposes ontology edits and an Unstructured Decoder that generates textual explanations, with an Attention-Based Gating module dynamically integrating the decoder outputs.

These papers directly address the intersection of structured decoding, grammar constraints, ontology guidance, and information extraction that your query targets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0855b34-5f9d-4adf-83a6-da087377f5aa",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "4af8cb5a-1c55-42e4-9b1f-58bd8c376aed",
  "sourceToolAssistantUUID": "d0855b34-5f9d-4adf-83a6-da087377f5aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-11T23:10:45.930Z_

Let me get a few more details -- the Papers with Code leaderboard for ACE05, the "Scientific Knowledge-driven Decoding Constraints" paper, and the SLOT paper which looked relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4af8cb5a-1c55-42e4-9b1f-58bd8c376aed",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdG5afmeAvGKhQLNWND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ce0d9cf-140b-4ce1-b5c1-4515f6256d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXn3xCGRnGS1fRwHFLPTfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 2370,
      "cache_read_input_tokens": 21259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2370,
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

_source line 44 · 2026-05-11T23:10:48.501Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015af1QhMJ3hY4FhcGYUQSs9`</summary>

```json
{
  "url": "https://paperswithcode.com/sota/relation-extraction-on-ace-2005",
  "prompt": "List the top 5 models on the ACE 2005 relation extraction leaderboard with their scores, paper titles, and dates. What is the current state of the art?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ce0d9cf-140b-4ce1-b5c1-4515f6256d98",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdG5afmeAvGKhQLNWND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4daf2672-4cd8-4b39-9d78-8123fa165cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXn3xCGRnGS1fRwHFLPTfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 2370,
      "cache_read_input_tokens": 21259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2370,
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

_source line 45 · 2026-05-11T23:10:48.734Z_

<details><summary>↩ Tool result · `toolu_015af1QhMJ3hY4FhcGYUQSs9`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://paperswithcode.com/sota/relation-extraction-on-ace-2005
Redirect URL: https://huggingface.co/papers/trending
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://huggingface.co/papers/trending"
- prompt: "List the top 5 models on the ACE 2005 relation extraction leaderboard with their scores, paper titles, and dates. What is the current state of the art?"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4daf2672-4cd8-4b39-9d78-8123fa165cfe",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "e984d0d6-3894-491d-8bbd-0a62198fcc90",
  "sourceToolAssistantUUID": "4daf2672-4cd8-4b39-9d78-8123fa165cfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-11T23:10:49.856Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TBYT1ikPCR4bMpo3dAHP17`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06603",
  "prompt": "Extract the full paper title, authors, date, and summary. How does this paper use scientific knowledge-driven decoding constraints? Does it combine grammar constraints with semantic/domain knowledge callbacks? What tasks is it evaluated on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e984d0d6-3894-491d-8bbd-0a62198fcc90",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdG5afmeAvGKhQLNWND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27ebb32e-8744-40f1-b64b-72331cddc208",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXn3xCGRnGS1fRwHFLPTfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 2370,
      "cache_read_input_tokens": 21259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2370,
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

_source line 47 · 2026-05-11T23:10:51.168Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AobKKpmB9cUpqXQprw2wr4`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-industry.32.pdf",
  "prompt": "Extract the full paper title, authors, venue, date, and summary. What is SLOT? Does it use structured decoding with constraints for information extraction? How does it structure LLM outputs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27ebb32e-8744-40f1-b64b-72331cddc208",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdG5afmeAvGKhQLNWND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03f1b980-b451-421f-8841-0597f5b734da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXn3xCGRnGS1fRwHFLPTfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 2370,
      "cache_read_input_tokens": 21259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2370,
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

_source line 48 · 2026-05-11T23:10:52.539Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AC1GUKqhZdbvxSVJp5bxzt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.08623",
  "prompt": "Extract the full paper title, authors, date, and summary. What is PARSE? How does it optimize schemas for LLM extraction? Does it use constrained decoding?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03f1b980-b451-421f-8841-0597f5b734da",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdG5afmeAvGKhQLNWND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a6cc816-c3e3-4001-9eb0-a15182ac2ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXn3xCGRnGS1fRwHFLPTfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 2370,
      "cache_read_input_tokens": 21259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2370,
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

_source line 49 · 2026-05-11T23:10:53.369Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BcYFwq9CopM7BFYZKLAYrC`</summary>

```json
{
  "query": "XGrammar semantic callback constrained decoding beyond grammar 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a6cc816-c3e3-4001-9eb0-a15182ac2ae5",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdG5afmeAvGKhQLNWND",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d3b0fe4-b526-47c7-8d2c-b7eaa1db3f3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXn3xCGRnGS1fRwHFLPTfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 954,
      "cache_creation_input_tokens": 2370,
      "cache_read_input_tokens": 21259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2370,
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

_source line 50 · 2026-05-11T23:10:54.239Z_

<details><summary>↩ Tool result · `toolu_01TBYT1ikPCR4bMpo3dAHP17`</summary>

```text
# Paper Summary

**Title:** "Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs"

**Authors:** Maotian Ma, Zheni Zeng, Zhenghao Liu, Yukun Yan

**Date:** Submitted April 8, 2026

**Summary:**
The paper addresses hallucination problems in large language models by proposing SciDC, a generation method that applies "subject-specific knowledge with strong constraints." Rather than relying solely on training or prompting, the approach leverages scientific theories and domain rules.

**Technical Approach:**
The method converts flexible domain knowledge into "multi-layered, standardized rules" using strong LLMs, then applies these constraints during generation. This framework systematically restricts model outputs to align with scientific principles.

**Evaluation Tasks:**
The paper demonstrates effectiveness across three scientific domains:
- Industrial formulation design
- Clinical tumor diagnosis
- Retrosynthesis planning

Results show approximately 12% average accuracy improvement over unconstrained generation.

**Note on Constraint Types:**
While the abstract emphasizes domain-specific rule constraints, the content provided doesn't explicitly detail whether grammar constraints are separately combined with semantic callbacks, though the "multi-layered" constraint description suggests a comprehensive approach integrating multiple constraint types.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27ebb32e-8744-40f1-b64b-72331cddc208",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "0f4ed835-d827-4040-a8e9-4eaa59b1b6b2",
  "sourceToolAssistantUUID": "27ebb32e-8744-40f1-b64b-72331cddc208",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-11T23:10:56.729Z_

<details><summary>↩ Tool result · `toolu_01AobKKpmB9cUpqXQprw2wr4`</summary>

```text
I apologize, but the content you've provided appears to be a PDF file encoded in binary format that hasn't been properly converted to readable text. The output shows raw PDF stream data with compression artifacts, making it impossible to extract the paper title, authors, venue, date, or meaningful content.

To help you effectively, I would need:

1. **Plain text or properly decoded PDF content** - The current format is unreadable
2. **A direct link to the paper** - If available through arXiv, ACL, or similar repositories
3. **The paper's abstract and introduction** - In readable format

Once you provide the content in a readable format, I'll be happy to:
- Extract the full citation information (title, authors, venue, date)
- Explain what SLOT is based on the paper's description
- Detail whether it uses structured decoding with constraints
- Describe how it structures LLM outputs

Could you resubmit the paper content in a readable text format?

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-1/projects/-/861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2/tool-results/webfetch-1778541052801-1rjxqm.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03f1b980-b451-421f-8841-0597f5b734da",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "40ffd2bc-7098-4326-8d13-564474f55a7b",
  "sourceToolAssistantUUID": "03f1b980-b451-421f-8841-0597f5b734da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-11T23:10:58.415Z_

<details><summary>↩ Tool result · `toolu_01AC1GUKqhZdbvxSVJp5bxzt`</summary>

```text
# PARSE: LLM-Driven Schema Optimization

**Full Title:** "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction"

**Authors:** Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla

**Date:** Submitted October 8, 2025

**Venue:** EMNLP 2025 Industry Track

## What is PARSE?

PARSE is a system designed to improve how LLMs extract structured information from text. Rather than treating JSON schemas as fixed templates, the approach recognizes them as "a form of natural language understanding contract" that models can both interpret and improve. The framework consists of two main components:

- **ARCHITECT:** Autonomously refines JSON schemas for LLM consumption while maintaining backward compatibility
- **SCOPE:** Implements extraction with reflection and combined guardrails (static and LLM-based)

## Schema Optimization Approach

Instead of relying solely on constraint decoding or reinforcement learning for syntactic validity, PARSE addresses the root cause: ambiguous or incomplete schema specifications. ARCHITECT actively optimizes schemas themselves, supported by RELAY, an integrated code generation system that ensures compatibility.

## Constrained Decoding

The paper notes that recent approaches "apply large language models directly to extraction tasks using existing JSON schemas, often with constraint decoding" but positions PARSE as fundamentally different—it optimizes the schemas themselves rather than just enforcing validity through decoding constraints.

**Results:** Up to 64.7% accuracy improvement on SWDE dataset with 92% error reduction on first retry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a6cc816-c3e3-4001-9eb0-a15182ac2ae5",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "735e2c91-895c-4528-9d04-bad053d71938",
  "sourceToolAssistantUUID": "6a6cc816-c3e3-4001-9eb0-a15182ac2ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-11T23:11:02.009Z_

<details><summary>↩ Tool result · `toolu_01BcYFwq9CopM7BFYZKLAYrC`</summary>

```text
Web search results for query: "XGrammar semantic callback constrained decoding beyond grammar 2025 2026"

Links: [{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Catalyst: XGrammar","url":"https://catalyst.cs.cmu.edu/projects/xgrammar.html"},{"title":"MLC | XGrammar-2: Fast and Customizable Structured Generation for Tool Calling and Agents","url":"https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation"},{"title":"Structured Decoding in vLLM: a gentle introduction | vLLM Blog","url":"https://blog.vllm.ai/2025/01/14/struct-decode-intro.html"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"}]

Based on the search results, here's what I found about XGrammar and semantic callbacks in constrained decoding:

## XGrammar Overview

XGrammar is an open-source library for efficient, flexible, and portable structured generation that leverages constrained decoding to ensure 100% structural correctness of the output.

## Core Technology

XGrammar accelerates context-free grammar execution by dividing the vocabulary into context-independent tokens that can be prechecked and context-dependent tokens that need to be interpreted during runtime. A significant portion (usually more than 99%) of the tokens in the mask can be precomputed in advance.

## Performance and Adoption

XGrammar is the default structured generation backend for vLLM, SGLang, and TensorRT-LLM as of March 2026, achieving under 40 microseconds per token with near-zero overhead in JSON generation. Engines like XGrammar and DOMINO achieve near-zero overhead.

## Beyond Grammar: Semantic Considerations

While the search results don't specifically discuss "semantic callbacks," they do address going beyond pure grammar constraints. Constrained decoding often reduces semantic correctness on reasoning-intensive tasks because constrained decoding alters the model's distribution at every token by masking invalid tokens and renormalizing the remaining probability.

XGrammar is best used to enforce format constraints, not to change the semantics of an LLM's response, helping downstream programs avoid fatal failures from malformed outputs while keeping the impact on the model's accuracy minimal.

## Recent Developments (2025-2026)

XGrammar-2 is a major upgrade purpose-built for agent applications that lets you easily express complex structures for agents, delivers high performance even for very large grammars, offers native cross-platform APIs, and remains fully backward compatible.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d3b0fe4-b526-47c7-8d2c-b7eaa1db3f3b",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "dc58ac88-36eb-400d-bf06-f457e16fd85d",
  "sourceToolAssistantUUID": "1d3b0fe4-b526-47c7-8d2c-b7eaa1db3f3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-11T23:11:04.634Z_

Let me get a couple more highly relevant items -- XGrammar-2 and the Draft-Conditioned paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc58ac88-36eb-400d-bf06-f457e16fd85d",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdHY59KpDZicwJakju9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "011fefa9-7ce8-44f1-98ab-9e18af166409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zy1aLnMKHQim8FAEDNR3y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3742,
      "cache_read_input_tokens": 23629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3742,
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

_source line 55 · 2026-05-11T23:11:06.607Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011cV8e8ZH2RGTCC6SYSg4th`</summary>

```json
{
  "url": "https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation",
  "prompt": "What is XGrammar-2? Does it support semantic callbacks, custom constraint functions beyond grammar, or hybrid grammar+callback decoding? What new features does it add over XGrammar-1?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "011fefa9-7ce8-44f1-98ab-9e18af166409",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdHY59KpDZicwJakju9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75e3cb2a-9e79-4d93-9f57-ab8ccc0cc617",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zy1aLnMKHQim8FAEDNR3y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3742,
      "cache_read_input_tokens": 23629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3742,
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

_source line 56 · 2026-05-11T23:11:08.024Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AQypC1yMb4HV7AUhbMQV3e`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.03305",
  "prompt": "Extract the full paper title, authors, date, and summary. What is draft-conditioned constrained decoding? Does it combine grammar constraints with other types of constraints?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75e3cb2a-9e79-4d93-9f57-ab8ccc0cc617",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdHY59KpDZicwJakju9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "817f63c8-7a3a-4aa0-aad0-ab5cf32a1e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zy1aLnMKHQim8FAEDNR3y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3742,
      "cache_read_input_tokens": 23629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3742,
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

_source line 57 · 2026-05-11T23:11:08.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SyMGMmM3Vhi3G8RVScza1n`</summary>

```json
{
  "query": "\"guided generation\" \"information extraction\" \"entity\" \"relation\" LLM structured output NER 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "817f63c8-7a3a-4aa0-aad0-ab5cf32a1e41",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdHY59KpDZicwJakju9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24d5d3af-1c06-42bb-90e8-7ce52898cde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zy1aLnMKHQim8FAEDNR3y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3742,
      "cache_read_input_tokens": 23629,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3742
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 23629,
          "cache_creation_input_tokens": 3742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3742,
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

_source line 58 · 2026-05-11T23:11:11.070Z_

<details><summary>↩ Tool result · `toolu_011cV8e8ZH2RGTCC6SYSg4th`</summary>

```text
# XGrammar-2 Overview

**What is XGrammar-2?**

XGrammar-2 is "a major upgrade purpose-built for agent applications" that uses constrained decoding to guarantee structural correctness in LLM outputs. It ensures that language models produce outputs conforming to specified formats—from JSON schemas to complex multi-part structures.

**Regarding Semantic Callbacks and Custom Constraints:**

The documentation does not mention semantic callbacks, custom constraint functions beyond grammar, or hybrid grammar+callback approaches. XGrammar-2 appears focused exclusively on grammar-based constrained decoding without callback mechanisms.

**Key New Features Over XGrammar-1:**

1. **Structural Tag**: A composable JSON-based DSL for expressing diverse agent output structures, including OpenAI Harmony format, tool calling protocols, and custom formats

2. **Performance Optimizations**:
   - Cross-grammar caching (up to 50% structure reuse)
   - Repetition state compression (100x speedup for complex schemas)
   - Batching and speculative decoding support with CPU-GPU parallelization

3. **Broader Deployment**: Multi-platform APIs (Python, C++, Rust, JS) supporting PyTorch, JAX, MLX, and multiple operating systems

4. **Accuracy Gains**: Up to 80x compilation speedup and near-zero overhead in serving scenarios while maintaining 100% schema accuracy
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75e3cb2a-9e79-4d93-9f57-ab8ccc0cc617",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "78699167-a630-45ac-9393-8a6ef7f0c98d",
  "sourceToolAssistantUUID": "75e3cb2a-9e79-4d93-9f57-ab8ccc0cc617",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-11T23:11:12.117Z_

<details><summary>↩ Tool result · `toolu_01AQypC1yMb4HV7AUhbMQV3e`</summary>

```text
# Paper Summary

**Title:** Draft-Conditioned Constrained Decoding for Structured Generation in LLMs

**Authors:** Avinash Reddy, Thayne T. Walker, James S. Ide, Amrit Singh Bedi

**Date:** Submitted February 8, 2026

**What is DCCD?**

Draft-Conditioned Constrained Decoding is described as "a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement." The approach first generates an unconstrained draft, then applies constrained decoding conditioned on that draft to ensure validity.

**Constraint Types:**

The paper does not explicitly detail whether DCCD combines grammar constraints with other constraint types. It mentions the method addresses situations where "a single syntax error can make the output unusable" in contexts like executable outputs, JSON objects, and API calls. The focus appears to be on improving structured generation broadly rather than distinguishing between specific constraint categories.

The key innovation is that draft conditioning reduces what the authors call the "projection tax" imposed by hard constraints, enabling smaller models to achieve performance comparable to much larger constrained baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "817f63c8-7a3a-4aa0-aad0-ab5cf32a1e41",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "acd7a17c-ff32-4ec5-b4c9-ef2659574599",
  "sourceToolAssistantUUID": "817f63c8-7a3a-4aa0-aad0-ab5cf32a1e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-11T23:11:16.764Z_

<details><summary>↩ Tool result · `toolu_01SyMGMmM3Vhi3G8RVScza1n`</summary>

```text
Web search results for query: ""guided generation" "information extraction" "entity" "relation" LLM structured output NER 2025 2026 arxiv"

Links: [{"title":"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction","url":"https://arxiv.org/html/2402.13364v1"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/html/2508.10036v1"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v1"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Analysing Lightweight Large Language Models for Biomedical Named Entity Recognition on Diverse Ouput Formats","url":"https://arxiv.org/html/2604.25920"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"arXiv:2504.14633v1 [cs.CL] 20 Apr 2025","url":"https://arxiv.org/pdf/2504.14633"}]

Here are the search results for your query about guided generation, information extraction, entities, relations, and LLMs for structured output and NER from recent papers (2025-2026) on arxiv and related sources:

## Key Findings:

**Recent Work on Guided Generation for Structured IE:**

Recent methods reframe IE as a language modeling problem, where a carefully crafted prompt guides an LLM to generate structured outputs for tasks like named entity recognition (NER), relation extraction (RE), and event extraction (EE).

**Two-Stage Pipeline Approaches:**

An efficient method called G&O enhances structured text generation capabilities by breaking generation into a two-step pipeline: initially, LLMs generate answers in natural language as intermediate responses, then are asked to organize the output into the desired structure, effectively separating the generation of content from the structuring process.

**Recent 2025-2026 Papers:**

A recent paper titled "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion" (August 2025) discusses prompting-guided structured outputs for NER, RE, and EE tasks.

LLM-based structured extraction has transformed information extraction from discriminative to generative approaches that produce structured outputs directly from unstructured text.

**Constrained Generation Strategies:**

Constrained decoding strategies have been used to ensure structured outputs, including grammar-constrained decoding with input-dependent grammars, and text-to-graph frameworks generating linearized graphs for joint entity and relation extraction.

These recent papers demonstrate active research in using LLMs with guided generation techniques for reliable, schema-compliant structured information extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24d5d3af-1c06-42bb-90e8-7ce52898cde3",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "05c56db9-6cf2-4466-9ba4-e91cced8cf59",
  "sourceToolAssistantUUID": "24d5d3af-1c06-42bb-90e8-7ce52898cde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-11T23:11:21.017Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Eg91xbkZ3Dxpb1pkactaQJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.13364",
  "prompt": "Extract the full paper title, authors, date, venue, and summary. Does this paper use constrained decoding or guided generation for NER/RE? What approach does it take to improve structured LLM output for information extraction?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05c56db9-6cf2-4466-9ba4-e91cced8cf59",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdJdBkQm5yT64LShgwF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4090a249-b570-4d51-80ac-ad75c10711d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DokG7dzJMi7D3CQpKCWVG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 27371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-11T23:11:22.430Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015wTFAVt8yktVnZcZe1F6dG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2401.01326",
  "prompt": "Extract the full paper title, authors, date, venue, and summary. Does this paper use constrained decoding for joint entity and relation extraction? Is it an autoregressive text-to-graph approach? What datasets is it evaluated on (including ACE05)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4090a249-b570-4d51-80ac-ad75c10711d7",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdJdBkQm5yT64LShgwF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b47dc4a8-63e2-47ca-8c59-af099c0e10d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DokG7dzJMi7D3CQpKCWVG3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 27371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-11T23:11:23.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U4vzZdq3QgroAYPFXtgq1C`</summary>

```json
{
  "query": "llguidance Microsoft \"constrained decoding\" callback semantic constraints beyond CFG 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b47dc4a8-63e2-47ca-8c59-af099c0e10d9",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdJdBkQm5yT64LShgwF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f24c470b-aec9-4b53-9289-9d7b0a72540c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DokG7dzJMi7D3CQpKCWVG3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 27371,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 27371,
          "cache_creation_input_tokens": 2004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2004,
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

_source line 64 · 2026-05-11T23:11:26.378Z_

<details><summary>↩ Tool result · `toolu_01Eg91xbkZ3Dxpb1pkactaQJ`</summary>

```text
# Paper Summary

**Full Title:** A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction

**Authors:** Yinghao Li, Rampi Ramprasad, Chao Zhang

**Date:** Submitted February 20, 2024

**Venue:** arXiv (cs.CL - Computation and Language)

## Approach to Structured Output

This paper does **not** use constrained decoding or guided generation. Instead, it introduces **G&O**, a two-stage prompting method that:

1. **Generation Phase:** LLMs first produce answers in natural language as intermediate responses
2. **Organization Phase:** LLMs then restructure this output into the desired format using the intermediate text as context

As the abstract states, this technique "breaks the generation into a two-step pipeline" and "effectively separates the generation of content from the structuring process, reducing the pressure of completing two orthogonal tasks simultaneously."

## Key Innovation

Rather than forcing the model to simultaneously generate content while maintaining structure, G&O decouples these tasks. The authors tested this on zero-shot named entity recognition and relation extraction tasks, demonstrating significant performance improvements. Notably, this simple prompting technique can be combined with other strategies like self-consistency for enhanced results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4090a249-b570-4d51-80ac-ad75c10711d7",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "f6e72284-da50-4e61-8e8b-7758f626dae4",
  "sourceToolAssistantUUID": "4090a249-b570-4d51-80ac-ad75c10711d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-11T23:11:26.893Z_

<details><summary>↩ Tool result · `toolu_015wTFAVt8yktVnZcZe1F6dG`</summary>

```text
# Paper Information

**Title:** "An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction"

**Authors:** Urchade Zaratiana, Nadi Tomeh, Pierre Holat, Thierry Charnois

**Date:** Submitted January 2, 2024; revised January 15, 2024

**Venue:** AAAI 2024

## Summary

The paper proposes a novel approach to extracting entities and relations simultaneously by treating the task as conditional sequence generation. Rather than generating tokens sequentially left-to-right, the method operates on text spans. It uses "a transformer encoder-decoder architecture with pointing mechanism on a dynamic vocabulary of spans and relation types."

## Key Questions Answered

**Constrained Decoding for Joint Extraction?**
The abstract does not explicitly mention constrained decoding. However, it describes using a "pointing mechanism on a dynamic vocabulary," which represents a form of controlled output generation.

**Autoregressive Text-to-Graph Approach?**
Yes. The title and abstract confirm this is an autoregressive approach that "generates a linearized graph where nodes represent text spans and edges represent relation triplets."

**Datasets Evaluated**
The abstract states "Evaluation on benchmark datasets validates the effectiveness of our approach," but the specific datasets evaluated—including whether ACE05 was used—are not detailed in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b47dc4a8-63e2-47ca-8c59-af099c0e10d9",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "24a9396b-126b-4574-9274-566351a15e99",
  "sourceToolAssistantUUID": "b47dc4a8-63e2-47ca-8c59-af099c0e10d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-11T23:11:30.900Z_

<details><summary>↩ Tool result · `toolu_01U4vzZdq3QgroAYPFXtgq1C`</summary>

```text
Web search results for query: "llguidance Microsoft "constrained decoding" callback semantic constraints beyond CFG 2025"

Links: [{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub","url":"https://github.com/guidance-ai/llguidance"},{"title":"GitHub - guidance-ai/guidance: A guidance language for controlling large language models. · GitHub","url":"https://github.com/guidance-ai/guidance"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"A Guide to Structured Generation Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"GitHub - microsoft/aici: AICI: Prompts as (Wasm) Programs","url":"https://github.com/microsoft/aici"},{"title":"Constrained decoding integration by ajindal1 · Pull Request #1381 · microsoft/onnxruntime-genai","url":"https://github.com/microsoft/onnxruntime-genai/pull/1381"}]

Based on the search results, here's what I found about llguidance, Microsoft, constrained decoding, and semantic constraints:

## llguidance Overview

llguidance is a library that implements constrained decoding for Large Language Models, enforcing arbitrary context-free grammar on LLM output at approximately 50 microseconds per token with negligible startup costs.

## Constrained Decoding: Syntax vs. Semantics

The search results highlight an important distinction regarding constraints beyond CFG:

Semantic constraints like "output must be factually accurate" or "response must be polite" cannot be enforced through token masking, but hybrid approaches combine hard syntactic constraints with soft semantic guidance through prompting or reward models.

## Callback-Based and Monitor-Guided Approaches

The broader ecosystem has evolved to include semantic constraint approaches beyond pure CFG grammars:

Monitor-Guided Decoding runs monitors during decoding to reject semantically invalid states, using static analysis to ensure generated code type-checks. Additionally, Synchromesh enforces syntax, typing, and scope simultaneously, reducing SQL and DSL errors.

## Microsoft Integration

The LLGuidance library is an actively maintained evolution of Microsoft's AICI (Artificial Intelligence Controller Interface), which lets you build Controllers that constrain and direct LLM output, with Controllers being flexible programs capable of implementing constrained decoding, dynamic editing of prompts and generated text, and coordinating execution across multiple generations.

As of May 2025, constrained decoding was integrated into ONNX Runtime using the LLGuidance library.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f24c470b-aec9-4b53-9289-9d7b0a72540c",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "4f8d708e-16d2-467c-b6b2-b66acbad094a",
  "sourceToolAssistantUUID": "f24c470b-aec9-4b53-9289-9d7b0a72540c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-11T23:11:35.141Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xe71kRsKkck35GyxZ9vU6t`</summary>

```json
{
  "url": "https://github.com/microsoft/aici",
  "prompt": "What is AICI? Does it support callback-based or programmatic constraints beyond grammar? Can you write custom constraint logic (like semantic validation callbacks) that runs during decoding? What language are controllers written in?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f8d708e-16d2-467c-b6b2-b66acbad094a",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdKfa9UPLkTUa1qrfHt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e6e2dce-6bff-49ab-9066-0492dec69dd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVQV1yv4NmvkfBfQSvbwo3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 29375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1934,
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

_source line 68 · 2026-05-11T23:11:38.982Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WxfyD7AtGVUrHojvqHuWWL`</summary>

```json
{
  "query": "Synchromesh \"monitor guided decoding\" semantic type constraint decoding information extraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e6e2dce-6bff-49ab-9066-0492dec69dd8",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdKfa9UPLkTUa1qrfHt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd0a348b-39b5-4fba-a010-adc02cd1ce2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVQV1yv4NmvkfBfQSvbwo3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1934,
      "cache_read_input_tokens": 29375,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1934
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 29375,
          "cache_creation_input_tokens": 1934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1934,
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

_source line 69 · 2026-05-11T23:11:42.041Z_

<details><summary>↩ Tool result · `toolu_01Xe71kRsKkck35GyxZ9vU6t`</summary>

```text
# AICI Overview

## What is AICI?

AICI (Artificial Intelligence Controller Interface) is a system for building Controllers that "constrain and direct output of a Large Language Model (LLM) in real time." It abstracts away implementation details of LLM inference engines, allowing flexible control strategies during token-by-token generation.

## Constraint Types Supported

AICI supports multiple constraint mechanisms:

**Grammar-based constraints:** Regular expressions and Yacc/LR1 grammars are explicitly mentioned with performance benchmarks (0.3ms for regex, 2.0ms for C grammar parsing).

**Beyond grammar:** The system enables "programmatic or query-based decoding" and "custom logic during the token-by-token decoding." Controllers can implement "interaction with the LLM inference engine before, during, and after every generated token" and "constraining decoding to a set of tokens."

**Custom constraint logic:** Yes. The framework allows developers to implement semantic validation or custom callbacks. PyCtrl and JsCtrl interpreters "allow to glue these constraints together" with custom application logic, and the system supports "fast-forwarding several tokens at a time" and "forking generation into multiple branches" with "communication between forks via shared variables."

## Controller Languages

Controllers can be written in "any language that can compile to Wasm (Rust, C, C++, ...), or be interpreted inside Wasm (Python, JavaScript, ...)." The repository specifically provides PyCtrl (Python) and JsCtrl (JavaScript) implementations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e6e2dce-6bff-49ab-9066-0492dec69dd8",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "0c72b075-954d-49f8-9586-18119761ea19",
  "sourceToolAssistantUUID": "4e6e2dce-6bff-49ab-9066-0492dec69dd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-11T23:11:45.180Z_

<details><summary>↩ Tool result · `toolu_01WxfyD7AtGVUrHojvqHuWWL`</summary>

```text
Web search results for query: "Synchromesh "monitor guided decoding" semantic type constraint decoding information extraction 2024 2025"

Links: [{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"SYNCHROMESH: RELIABLE CODE GENERATION FROM PRE-TRAINED LANGUAGE MODELS","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2022/01/csd_arxiv.pdf"},{"title":"GitHub - kanishkg/synchromesh: Get language models to generate responses in a specific format reliably. Open source implementation of Synchromesh: Reliable code generation from pre-trained language models.","url":"https://github.com/kanishkg/synchromesh"},{"title":"Synchromesh: Reliable Code Generation from Pre-trained Language Models | OpenReview","url":"https://openreview.net/forum?id=KmtVD97J43e"},{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"RELIABLE CODE GENERATION FROM PRE-TRAINED ...","url":"https://www.vuminhle.com/pdf/iclr22.pdf"},{"title":"Towards neuro-symbolic constrained decoding for reliable","url":"https://dl.gi.de/server/api/core/bitstreams/706c975e-f0f4-4bfc-b735-00facba90d61/content"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Synchromesh: Reliable code generation from pre-trained language models · Machine Learning for Big Code and Naturalness","url":"https://ml4code.github.io/publications/poesia2022synchromesh/"},{"title":"Synchromesh: Reliable code generation from pre-trained language models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/synchromesh-reliable-code-generation-from-pre-trained-language-models/"}]

I found relevant results about Synchromesh and related constrained decoding techniques. Here's what the search reveals:

## Synchromesh Overview

Synchromesh is a framework for substantially improving the reliability of pre-trained models for code generation. It samples programs using Constrained Semantic Decoding (CSD): a general framework for constraining the output to a set of valid programs in the target language.

## Constrained Semantic Decoding (CSD)

CSD is a novel method for enforcing rich syntactic and semantic constraints during code generation on top of a frozen language model, with language-specific constraints ranging from syntax validity to scoping and type-checking. CSD leverages constraints on partial outputs to sample complete correct programs, and needs neither re-training nor fine-tuning of the language model.

## Related Techniques (2023-2025)

The search results also identify other relevant constrained decoding approaches:

- Monitor-Guided Decoding (NeurIPS 2023) uses static analysis to ensure generated code type-checks.
- IterGen (ICLR 2025) introduces forward/backward generation tied to grammar symbols, with KV-cache reuse making "undo and redo" efficient.
- DOMINO (ICML 2024) enforces regex/grammar constraints aligned to BPE subwords and achieves zero or even negative overhead compared to unconstrained decoding.

These techniques collectively represent the state-of-the-art in semantic type constraint decoding for structured generation and information extraction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd0a348b-39b5-4fba-a010-adc02cd1ce2e",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "aace49c5e381cb38b",
  "type": "user",
  "uuid": "a838c7c1-500e-471f-8511-7e0d97a7499c",
  "sourceToolAssistantUUID": "fd0a348b-39b5-4fba-a010-adc02cd1ce2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-11T23:13:21.713Z_

Now I have a comprehensive picture. Here is the full report.

---

## Competing/Concurrent Work Report: Ontology-Aware Structured Decoding for IE with Hybrid Grammar-Callback Constraints

### Executive Summary

**No paper was found that implements the exact combination of hybrid grammar + callback constrained decoding specifically for information extraction.** This is the core novelty gap. However, the individual components (grammar-constrained decoding for IE, ontology-guided extraction, semantic constraint callbacks during decoding, joint entity-relation extraction with LLMs) each have active concurrent work that the authors must cite and differentiate from. Below are the findings organized by search topic.

---

### 1. Constrained Decoding for Information Extraction

**Closest competitor -- must cite:**

- **"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts"** -- Schmidt & Cimiano, *Frontiers in AI*, January 2025. Uses CFG-based constrained decoding (Lark parser, LALR mode) for extracting structured representations conforming to the C-TrO clinical trial ontology. Key difference from the paper under review: constraints are **purely syntactic** (grammar-only), with no semantic callbacks. Reports F1 improvement of 0.35--0.43 absolute over unconstrained decoding. [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/)

- **"Lazy-k Decoding: Constrained Decoding for Information Extraction"** -- Hemmer et al., *EMNLP 2023*. Proposes a constrained decoding algorithm for token-classification-based IE that searches for constraint-satisfying label assignments while maximizing total probability. Focused on token classification rather than generative extraction. [Link](https://aclanthology.org/2023.emnlp-main.416/)

- **"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning"** -- Geng et al., 2023 (revised Jan 2024). Introduces input-dependent grammars for constrained decoding on IE, entity disambiguation, and constituency parsing. Foundational work but does not incorporate semantic/ontology callbacks. [Link](https://arxiv.org/abs/2305.13971)

---

### 2. Schema-Guided Information Extraction

- **"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction"** -- Shrimal et al., *EMNLP 2025 Industry Track*. Two components: ARCHITECT (autonomously optimizes JSON schemas) and SCOPE (reflection-based extraction with static + LLM-based guardrails). Explicitly positions itself as an alternative to constrained decoding -- it optimizes schemas rather than enforcing output structure at decode time. Up to 64.7% accuracy improvement on SWDE. [Link](https://arxiv.org/abs/2510.08623)

- **"LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence"** -- April 2026. Uses schema-guided prompting for extraction from heterogeneous data sources with validation. Not constrained decoding. [Link](https://arxiv.org/abs/2604.06571)

- **"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction" (G&O)** -- Li et al., Feb 2024. Two-stage approach: generate in natural language, then organize into structured format. No constrained decoding. Tested on zero-shot NER and RE. [Link](https://arxiv.org/abs/2402.13364)

---

### 3. Custom Logit Processors and Semantic Constraints in vLLM

- **vLLM now natively supports custom LogitsProcessors** (as of the V1 engine). Custom processors subclass `vllm.v1.sample.logits_processor.LogitsProcessor` and implement `apply()` (batch-level logit transformation) and `update_state()` (per-token state updates). Per-request parameters can be passed via `SamplingParams.extra_args`. This is the infrastructure the paper under review would presumably build on. [Link](https://docs.vllm.ai/en/stable/features/custom_logitsprocs/)

- **XGrammar** is now the default structured generation backend for vLLM, SGLang, and TensorRT-LLM (as of March 2026). Achieves < 40 microseconds per token. Purely grammar-based -- **no semantic callback support**. [Link](https://arxiv.org/abs/2411.15100)

- **XGrammar-2** (announced May 4, 2026) adds a composable JSON-based DSL ("Structural Tag"), cross-grammar caching, and multi-platform APIs. Still **no semantic callbacks** -- focused entirely on grammar-level constraints. [Link](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)

- **Microsoft AICI (Artificial Intelligence Controller Interface)** -- the most relevant infrastructure competitor. Allows building Wasm-based "Controllers" that run custom programmatic logic during decoding, supporting grammar constraints (regex, Yacc/LR1) **plus arbitrary custom callback logic** (Python, JavaScript, Rust, C/C++ compiled to Wasm). Supports forking, communication between forks, fast-forwarding. This is architecturally the closest to "hybrid grammar+callback" but is a general framework, **not applied to IE specifically**. [Link](https://github.com/microsoft/aici)

- **Microsoft llguidance** -- Rust-based Earley parser at ~50 microseconds/token. Evolved from AICI. Credited by OpenAI for underpinning their Structured Outputs feature. Focused on grammar enforcement, not semantic callbacks. [Link](https://github.com/guidance-ai/llguidance)

---

### 4. Ontology-Constrained Generation for Knowledge Extraction

- **"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs"** -- Khorshidi et al., September 2025. Dynamically generates ontology snippets tailored to each entity type to guide extraction via prompting (not constrained decoding). Deployed at scale: 9M Wikipedia pages, 19M facts, 98.8% precision. Uses a hybrid of pattern-based rules + LLM-based extraction + LLM grounder for verification. [Link](https://arxiv.org/abs/2509.04696)

- **"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding"** -- Vukovic et al., *SIGDIAL 2024* (revised March 2025). Constrains decoding output to ontology terms and relations to reduce hallucination. Uses ontology-vocabulary constraints (not CFG), with multiple branch generation and confidence-based selection. [Link](https://arxiv.org/abs/2408.02361)

- **"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs" (SciDC)** -- Ma et al., April 2026. Converts domain knowledge into multi-layered standardized rules and applies them as constraints during generation. Evaluated on industrial formulation design, clinical tumor diagnosis, and retrosynthesis. ~12% average accuracy improvement. Closest to "semantic callback" spirit but in scientific domains, not IE/NER/RE. [Link](https://arxiv.org/abs/2604.06603)

- **"OntoKG: Ontology-Oriented Knowledge Graph Construction with Intrinsic-Relational Routing"** -- 2026. KG construction with ontology alignment but via architecture design, not constrained decoding. [Link](https://arxiv.org/abs/2604.02618)

---

### 5. Structured Output for Joint Entity-Relation Extraction

- **"An Autoregressive Text-to-Graph Framework for Joint Entity and Relation Extraction"** -- Zaratiana et al., *AAAI 2024*. Generates linearized graphs autoregressively using a pointing mechanism on a dynamic span vocabulary. Not grammar-constrained but structurally constrained via the pointer mechanism. [Link](https://arxiv.org/abs/2401.01326)

- **"A relation semantics-guided top-down approach for joint entity and relation extraction in complex scenarios"** -- 2026 (ScienceDirect). Addresses overlapping triples with relation-guided decomposition. [Link](https://www.sciencedirect.com/science/article/abs/pii/S095070512600376X)

- **"RSTGP"** -- 2026. Integrates relation-aware scoring, span-level graph enhancement, and type-constrained calibration for joint extraction from medical texts. [Link](https://www.mdpi.com/2076-3417/16/9/4102)

- **"Reamend" (LLM augmented joint learning framework)** -- 2025. Uses LLMs with entity-relation amendment to eliminate redundant triplets. Claims SOTA on benchmark datasets. [Link](https://www.sciencedirect.com/science/article/abs/pii/S1568494625314073)

---

### 6. Grammar-Constrained Decoding + NER/RE on arXiv

- **"CRANE: Reasoning with constrained LLM generation"** -- Banerjee et al., *ICML 2025*. Augments output grammars with additional rules to preserve reasoning capability during constrained decoding. Up to 10% accuracy improvement on symbolic reasoning. Evaluated on code generation and math, **not IE**. No semantic callbacks -- reasoning is embedded in the grammar itself. [Link](https://arxiv.org/abs/2502.09061)

- **"Grammar-Aligned Decoding"** -- 2024 (updated Dec 2025). Proposes ASAp algorithm for grammar-constrained decoding that produces higher-likelihood outputs. Evaluated on code generation and structured NLP. [Link](https://arxiv.org/abs/2405.21047)

- **"Flexible and Efficient Grammar-Constrained Decoding"** -- Park et al., Feb 2025 (revised July 2025). 17.7x faster offline preprocessing for CFG mask computation. Infrastructure-level contribution, not IE-specific. [Link](https://arxiv.org/abs/2502.05111)

- **"Draft-Conditioned Constrained Decoding" (DCCD)** -- Reddy et al., Feb 2026. Two-step approach: generate unconstrained draft, then apply constrained decoding conditioned on the draft. Reduces the "projection tax" of hard constraints. General-purpose, not IE-specific. [Link](https://arxiv.org/abs/2603.03305)

- **"Constrained Decoding of Diffusion LLMs with Context-Free Grammars"** -- 2026 (OpenReview). Extends constrained decoding to diffusion-based LLMs. Near-perfect syntactic correctness on structured data extraction in JSON. [Link](https://openreview.net/forum?id=7Sph4KyeYO)

- **Synchromesh / Constrained Semantic Decoding (CSD)** -- Poesia et al., *ICLR 2022*. Enforces syntax, typing, and scope constraints simultaneously during code generation. The "semantic" constraint aspect (type-checking, scoping) is architecturally similar to callbacks. Applied to code, **not IE**. [Link](https://www.microsoft.com/en-us/research/publication/synchromesh-reliable-code-generation-from-pre-trained-language-models/)

---

### 7. ACE05 Joint IE -- Current SOTA

The ACE05 leaderboard (Papers with Code) was not directly accessible, but from the search results:

- **UNIRE** (BERT-based unified representation) remains a strong baseline on ACE05 for joint entity and relation extraction.
- **Reamend** (2025) claims SOTA on joint entity-relation extraction benchmarks using LLM-augmented learning.
- For **event extraction** on ACE05, recent SOTA approaches achieve ~63.9 F1 on argument role classification, all using PLM backbones.
- No paper was found claiming SOTA on ACE05 using constrained decoding approaches specifically.

---

### Key Takeaway for the Authors

The **specific combination** of (1) grammar-based structural constraints + (2) runtime semantic callbacks (e.g., ontology validation, type checking, entity co-reference consistency) applied to (3) information extraction tasks (NER, RE, joint extraction) appears to be **novel and unclaimed**. The closest existing work falls into two camps:

- **Grammar-constrained decoding applied to IE** (Schmidt & Cimiano 2025; Geng et al. 2023) -- these use only syntactic/structural constraints, no semantic callbacks.
- **Hybrid syntax+semantic constrained decoding** (Synchromesh, AICI, SciDC) -- these support callback-style semantic constraints but are applied to code generation or scientific domains, **not IE**.

The authors should cite Schmidt & Cimiano (2025), ODKE+ (2025), CRANE (ICML 2025), SciDC (2026), DCCD (2026), Microsoft AICI, XGrammar/XGrammar-2, and Synchromesh as the most relevant concurrent/competing work, while clearly articulating that none combines grammar+callback constraints for IE specifically.

Sources:
- [Grammar-constrained decoding for clinical trial IE (Schmidt & Cimiano 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/)
- [Lazy-k Decoding (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.416/)
- [Grammar-Constrained Decoding for Structured NLP Tasks (Geng et al.)](https://arxiv.org/abs/2305.13971)
- [PARSE: Schema Optimization (EMNLP 2025 Industry)](https://arxiv.org/abs/2510.08623)
- [LLM-based Schema-Guided Extraction (2026)](https://arxiv.org/abs/2604.06571)
- [G&O: Two-stage Structured Output for IE](https://arxiv.org/abs/2402.13364)
- [vLLM Custom LogitsProcessors](https://docs.vllm.ai/en/stable/features/custom_logitsprocs/)
- [XGrammar](https://arxiv.org/abs/2411.15100)
- [XGrammar-2 announcement](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)
- [Microsoft AICI](https://github.com/microsoft/aici)
- [llguidance](https://github.com/guidance-ai/llguidance)
- [ODKE+ (2025)](https://arxiv.org/abs/2509.04696)
- [Dialogue Ontology RE via Constrained CoT (SIGDIAL 2024)](https://arxiv.org/abs/2408.02361)
- [SciDC: Scientific Knowledge-driven Decoding Constraints (2026)](https://arxiv.org/abs/2604.06603)
- [Text-to-Graph Joint Extraction (AAAI 2024)](https://arxiv.org/abs/2401.01326)
- [CRANE (ICML 2025)](https://arxiv.org/abs/2502.09061)
- [Grammar-Aligned Decoding](https://arxiv.org/abs/2405.21047)
- [Flexible and Efficient GCD](https://arxiv.org/abs/2502.05111)
- [Draft-Conditioned Constrained Decoding (2026)](https://arxiv.org/abs/2603.03305)
- [Constrained Decoding for Diffusion LLMs (2026)](https://openreview.net/forum?id=7Sph4KyeYO)
- [Synchromesh (ICLR 2022)](https://www.microsoft.com/en-us/research/publication/synchromesh-reliable-code-generation-from-pre-trained-language-models/)
- [ACE 2005 Leaderboard](https://paperswithcode.com/sota/relation-extraction-on-ace-2005)
- [Awesome LLM Constrained Decoding list](https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding)
- [Reamend: LLM augmented joint learning](https://www.sciencedirect.com/science/article/abs/pii/S1568494625314073)
- [RSTGP: Joint extraction from medical texts (2026)](https://www.mdpi.com/2076-3417/16/9/4102)
- [LLMs for Generative IE: A Survey](https://link.springer.com/article/10.1007/s11704-024-40555-y)
- [OntoKG (2026)](https://arxiv.org/abs/2604.02618)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a838c7c1-500e-471f-8511-7e0d97a7499c",
  "isSidechain": true,
  "agentId": "aace49c5e381cb38b",
  "requestId": "req_011CawdLjJfEVoSEufPRUdZg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a5ca143-f99a-45ea-b99b-120e7f2041e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWsBypc18eiXVgvdikZCF6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 31309,
      "output_tokens": 4203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1645
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4203,
          "cache_read_input_tokens": 31309,
          "cache_creation_input_tokens": 1645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1645,
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
