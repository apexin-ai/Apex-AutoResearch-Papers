# Research conversation: Search for and read TWO papers: 1. "DCCD: Draft-Conditioned Constrained Decoding for Structured Generation in LLMs" (arx

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a40203604e8271a8a.jsonl`
- **Structured JSON:** [`bd73f3b75dbbcc47fc0d.json`](../../sessions/bd/bd73f3b75dbbcc47fc0d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-10T18:38:54.909Z_

Search for and read TWO papers:

1. "DCCD: Draft-Conditioned Constrained Decoding for Structured Generation in LLMs" (arxiv 2603.03305, February 2026)
   - How does it decouple semantic planning from structural enforcement?
   - What is the +24 pp improvement over standard constrained decoding?
   - Is it training-free?
   - What benchmarks?

2. "The Format Tax" (arxiv 2604.03616, April 2026)
   - What is the key finding about prompt-level vs decoder-level format constraint degradation?
   - What evidence do they provide?
   - How does this relate to reducing per-step schema complexity?

Use WebSearch then WebFetch for each. Try:
- "DCCD draft-conditioned constrained decoding 2603.03305"
- "arxiv 2603.03305"
- "Format Tax structured generation 2604.03616"  
- "arxiv 2604.03616"

Report findings in detail for both papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "55281636-7dd6-4cc1-b2a9-646c9ee827dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:38:54.931Z_

```json
{
  "parentUuid": "55281636-7dd6-4cc1-b2a9-646c9ee827dd",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
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
  "uuid": "b81bb0cf-fabc-49dc-b5f6-2a628ac2380a",
  "timestamp": "2026-05-10T18:38:54.931Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:38:57.323Z_



I'll start by loading the WebSearch and WebFetch tools, then search for both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b81bb0cf-fabc-49dc-b5f6-2a628ac2380a",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNj5o4WMicc3MoEoiix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f72632ee-b320-4ea2-9a85-508b5e6d7760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CriwvQousP1QuhxPkHmKNR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 802,
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

_source line 4 · 2026-05-10T18:38:57.554Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WRXsgohLyxeHEPwKHHtKui`</summary>

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
  "parentUuid": "f72632ee-b320-4ea2-9a85-508b5e6d7760",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNj5o4WMicc3MoEoiix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a318c7a5-f6d8-4b74-a7b4-03484c5a624c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CriwvQousP1QuhxPkHmKNR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 8223,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 802
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 802,
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

_source line 5 · 2026-05-10T18:38:57.558Z_

<details><summary>↩ Tool result · `toolu_01WRXsgohLyxeHEPwKHHtKui`</summary>

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
  "parentUuid": "a318c7a5-f6d8-4b74-a7b4-03484c5a624c",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "704668cb-373a-43b5-9049-289fed6ec3e1",
  "sourceToolAssistantUUID": "a318c7a5-f6d8-4b74-a7b4-03484c5a624c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:39:00.598Z_



Now let me search for both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "704668cb-373a-43b5-9049-289fed6ec3e1",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNjH5iL5zpHsTj3aqVF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb71afc8-f7f7-43ec-b8b6-4f47d0b1f2db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Hu1SRJM4Ya2Vo73fTRye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-10T18:39:01.567Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLytidg2uDf6TFuFfQwC8M`</summary>

```json
{
  "query": "DCCD draft-conditioned constrained decoding 2603.03305"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb71afc8-f7f7-43ec-b8b6-4f47d0b1f2db",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNjH5iL5zpHsTj3aqVF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad1717b5-b34b-4cfd-9f15-db404071504c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Hu1SRJM4Ya2Vo73fTRye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-10T18:39:02.029Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011uFxzbFtsksJMmgUxLSRU4`</summary>

```json
{
  "query": "arxiv 2603.03305"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad1717b5-b34b-4cfd-9f15-db404071504c",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNjH5iL5zpHsTj3aqVF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bbf803f-f27f-4188-9407-1b0fc78cfbae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Hu1SRJM4Ya2Vo73fTRye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 9 · 2026-05-10T18:39:02.503Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UX6VNi5Xa4F3CEH2w4Tn4u`</summary>

```json
{
  "query": "Format Tax structured generation 2604.03616"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bbf803f-f27f-4188-9407-1b0fc78cfbae",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNjH5iL5zpHsTj3aqVF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d83a29b6-f3f0-4314-a221-c1378c3c554f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Hu1SRJM4Ya2Vo73fTRye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-10T18:39:02.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BofPkxDuJWqEQBxxfLJwKq`</summary>

```json
{
  "query": "arxiv 2604.03616"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d83a29b6-f3f0-4314-a221-c1378c3c554f",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNjH5iL5zpHsTj3aqVF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99669f0d-8fe3-42f1-bd64-f19693577153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2Hu1SRJM4Ya2Vo73fTRye",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

### Tool result

_source line 11 · 2026-05-10T18:39:07.324Z_

<details><summary>↩ Tool result · `toolu_01BofPkxDuJWqEQBxxfLJwKq`</summary>

```text
Web search results for query: "arxiv 2604.03616"

Links: [{"title":"[2604.03616] The Format Tax","url":"https://arxiv.org/abs/2604.03616"},{"title":"The Format Tax","url":"https://arxiv.org/html/2604.03616"},{"title":"The Format Tax | Trending arXiv papers – Ribbit Ribbit","url":"https://ribbitribbit.co/paper/arxiv.2604.03616-The-Format-Tax"},{"title":"[2603.03616] LeafInst - Unified Instance Segmentation Network for Fine-Grained Forestry Leaf Phenotype Analysis: A New UAV based Benchmark","url":"https://arxiv.org/abs/2603.03616"},{"title":"LeafInst - Unified Instance Segmentation Network for Fine-Grained Forestry Leaf Phenotype Analysis: A New UAV based Benchmark","url":"https://arxiv.org/html/2603.03616"},{"title":"[2110.03616] Cyclotomic expansions for the colored HOMFLY-PT invariants of double twist knots","url":"https://arxiv.org/abs/2110.03616"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2405.03616"},{"title":"[2511.03616] Going Beyond Expert Performance via Deep Implicit Imitation Reinforcement Learning","url":"https://arxiv.org/abs/2511.03616"},{"title":"Astronomy & Astrophysics manuscript no. main c⃝ESO 2020 April 9, 2020","url":"https://arxiv.org/pdf/2004.03616"},{"title":"Noncooperative Equilibrium Selection via a Trading-based Auction","url":"https://arxiv.org/html/2502.03616"}]

Based on the search results, arxiv paper 2604.03616 is titled "The Format Tax" by Ivan Yee Lee, Loris D'Antoni, and Taylor Berg-Kirkpatrick from UC San Diego.

The paper finds that structured output requirements like JSON, XML, LaTeX, and Markdown substantially degrade reasoning and writing performance across open-weight models, with format-requesting instructions alone causing most of the accuracy loss before any decoder constraint is applied. 

The authors propose decoupling reasoning from formatting—whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation—as a way to substantially recover lost accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99669f0d-8fe3-42f1-bd64-f19693577153",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "218a4710-78f0-4d98-acfc-e0b60c56e952",
  "sourceToolAssistantUUID": "99669f0d-8fe3-42f1-bd64-f19693577153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:39:07.735Z_

<details><summary>↩ Tool result · `toolu_011uFxzbFtsksJMmgUxLSRU4`</summary>

```text
Web search results for query: "arxiv 2603.03305"

Links: [{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"ARTIFICIAL INTELLIGENCE IN THE AUTONOMOUS NAVIGATION","url":"https://arxiv.org/pdf/2405.03305"},{"title":"my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily","url":"https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"},{"title":"[2504.03305] Unexpected clustering pattern in dwarf galaxies challenges formation models","url":"https://arxiv.org/abs/2504.03305"},{"title":"Computer Vision and Pattern Recognition","url":"https://arxiv.org/list/cs.CV/pastweek?skip=7&show=1000"},{"title":"arXiv:2209.03305v2 [hep-ph] 26 Feb 2024 UV/IR Mixing, Causal Diamonds and","url":"https://arxiv.org/pdf/2209.03305"},{"title":"[2603.07233] Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation","url":"https://arxiv.org/abs/2603.07233"},{"title":"Top arXiv papers","url":"https://scirate.com/?amp=&amp=&amp=&amp=&amp=&date=2017-03-21&date=2026-03-31&page=14&page=22&page=40&page=6&range=1&range=1"}]

Based on the search results, arxiv paper **2603.03305** is titled ""Draft-Conditioned Constrained Decoding for Structured Generation in LLMs," addressing how large language models are increasingly used to generate executable outputs, JSON objects, and API calls, where a single syntax error can make the output unusable.

The paper proposes Draft-Conditioned Constrained Decoding (DCCD), a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

The authors analyze DCCD through a KL-projection view, showing that draft conditioning increases feasible mass and reduces the cumulative "projection tax" induced by hard constraints, with an optional best-of-K draft selection.

The paper was submitted on February 8, 2026, and was authored by Avinash Reddy, Thayne T. Walker, James S. Ide, and Amrit Singh Bedi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bbf803f-f27f-4188-9407-1b0fc78cfbae",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "68576ed1-17c0-4aed-9678-df02c1df143a",
  "sourceToolAssistantUUID": "7bbf803f-f27f-4188-9407-1b0fc78cfbae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:39:09.718Z_

<details><summary>↩ Tool result · `toolu_01XLytidg2uDf6TFuFfQwC8M`</summary>

```text
Web search results for query: "DCCD draft-conditioned constrained decoding 2603.03305"

Links: [{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251"},{"title":"Part 6: Implementing Constrained Decoding | by Albersj | Medium","url":"https://medium.com/@albersj66/part-6-implementing-constrained-decoding-for-phi-3-vision-2c72a1be6a17"},{"title":"fairseq/examples/constrained_decoding/README.md at main · facebookresearch/fairseq","url":"https://github.com/facebookresearch/fairseq/blob/main/examples/constrained_decoding/README.md"},{"title":"Attention Meets Reachability: Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding","url":"https://arxiv.org/html/2603.05540"},{"title":"[2603.05210] Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding","url":"https://arxiv.org/abs/2603.05210"}]

Based on the search results, here's information about the paper DCCD (Draft-Conditioned Constrained Decoding) with arXiv identifier 2603.03305:

## Overview

Draft-Conditioned Constrained Decoding (DCCD) is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

## The Problem DCCD Addresses

Large language models are increasingly used to generate executable outputs, JSON objects, and API calls, where a single syntax error can make the output unusable. Constrained decoding enforces validity token-by-token via masking and renormalization, but it can distort generation when the model assigns low probability mass to valid continuations, pushing decoding toward locally valid yet semantically incorrect trajectories.

## How DCCD Works

In Step 1, a model generates an unconstrained draft that captures the semantic plan or intermediate reasoning. In Step 2, the final structured output is generated using constrained decoding conditioned on the draft. Conditioning shifts probability mass toward schema-consistent continuations, so the subsequent constraint enforcement step is substantially less distortive.

## Key Results

Across structured reasoning benchmarks, DCCD improves strict structured accuracy by up to +24 percentage points over standard constrained decoding (e.g., 15.2% to 39.0% on GSM8K with a 1B model), and enables smaller model pairs to match or exceed much larger constrained baselines, yielding substantial gains in parameter efficiency.

The paper was submitted on February 8, 2026, with authors Avinash Reddy, Thayne T. Walker, James S. Ide, and Amrit Singh Bedi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad1717b5-b34b-4cfd-9f15-db404071504c",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "35cbef06-b996-4d53-b2ab-c43a2c52653d",
  "sourceToolAssistantUUID": "ad1717b5-b34b-4cfd-9f15-db404071504c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:39:10.337Z_

<details><summary>↩ Tool result · `toolu_01UX6VNi5Xa4F3CEH2w4Tn4u`</summary>

```text
Web search results for query: "Format Tax structured generation 2604.03616"

Links: [{"title":"[2604.03616] The Format Tax","url":"https://arxiv.org/abs/2604.03616"},{"title":"The Format Tax","url":"https://arxiv.org/html/2604.03616"},{"title":"[2604.03616v1] The Format Tax","url":"https://arxiv.org/abs/2604.03616v1"},{"title":"The Format Tax | Trending arXiv papers – Ribbit Ribbit","url":"https://ribbitribbit.co/paper/arxiv.2604.03616-The-Format-Tax"},{"title":"TaxPraBen: A Scalable Benchmark for Structured Evaluation of LLMs in Chinese Real-World Tax Practice","url":"https://arxiv.org/html/2604.08948"},{"title":"Client Tax Organizer Form - Blank Fillable Template | Fill Out, Print & Download PDF | pdfFiller","url":"https://tax-organizer-template.pdffiller.com/"},{"title":"Tax Data Exchange","url":"https://taxdataexchange.org/"},{"title":"Tax Model Data at the NBER | NBER","url":"https://www.nber.org/research/data/tax-model-data-nber"},{"title":"Tax Leaders Inc Tax Client Information - Fill Online, Printable, Fillable, Blank - pdfFiller","url":"https://tax-client-information-sheet-template.pdffiller.com/"},{"title":"[2604.08948] TaxPraBen: A Scalable Benchmark for Structured Evaluation of LLMs in Chinese Real-World Tax Practice","url":"https://arxiv.org/abs/2604.08948"}]

Based on the search results, I found the paper you're looking for:

## "The Format Tax" (arXiv:2604.03616)

The paper addresses how asking a large language model to respond in JSON should be a formatting choice, not a capability tax.

### Key Findings:

The research shows that structured output requirements -- JSON, XML, LaTeX, Markdown -- substantially degrade reasoning and writing performance across open-weight models.

The dominant cost enters at the prompt: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied.

### Proposed Solution:

The diagnosis points to a simple principle: decouple reasoning from formatting, whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation. Across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing, decoupling recovers most lost accuracy.

### Important Note on Recent Models:

Most recent closed-weight models show little to no format tax, suggesting the problem is not inherent to structured generation but a gap that current open-weight models have yet to close.

The paper was submitted on April 4, 2026, by Ivan Yee Lee, Loris D'Antoni, and Taylor Berg-Kirkpatrick from UC San Diego.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d83a29b6-f3f0-4314-a221-c1378c3c554f",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "c5416ca7-8e15-40ff-b8f5-d0bb9655ad96",
  "sourceToolAssistantUUID": "d83a29b6-f3f0-4314-a221-c1378c3c554f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T18:39:13.583Z_

Good, I found both papers. Now let me fetch the full details from the arxiv abstract/HTML pages for both papers to get deeper information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5416ca7-8e15-40ff-b8f5-d0bb9655ad96",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNkDVwfqEX4XJ5VXc8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b18b33a6-7e69-4516-8476-20e2c73a3395",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtazyDfuuZrMADPaSHyJXC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 648,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2706,
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

_source line 16 · 2026-05-10T18:39:16.448Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WnHintxGVQFLWb5knCgQYK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.03305",
  "prompt": "Extract all details about this paper: full title, authors, abstract, methodology (how it decouples semantic planning from structural enforcement), the +24pp improvement details, whether it is training-free, what benchmarks are used, KL-projection analysis, best-of-K draft selection, and any other key results or contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b18b33a6-7e69-4516-8476-20e2c73a3395",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNkDVwfqEX4XJ5VXc8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "657bc73d-a000-4a1f-a08c-bbe3c9f30c4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtazyDfuuZrMADPaSHyJXC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 648,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2706,
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

_source line 17 · 2026-05-10T18:39:18.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UA1ekiUi1gd4Ecp4qAdtNH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03616",
  "prompt": "Extract all details about this paper: full title, authors, abstract, key finding about prompt-level vs decoder-level format constraint degradation, what evidence they provide (benchmarks, models tested, formats tested), how this relates to reducing per-step schema complexity, the decoupling approach, and any other key results or contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "657bc73d-a000-4a1f-a08c-bbe3c9f30c4c",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNkDVwfqEX4XJ5VXc8f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "566a5b53-b572-4129-849b-74de6abc5d19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtazyDfuuZrMADPaSHyJXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 648,
      "cache_creation_input_tokens": 2706,
      "cache_read_input_tokens": 10937,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2706
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 648,
          "output_tokens": 313,
          "cache_read_input_tokens": 10937,
          "cache_creation_input_tokens": 2706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2706,
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

_source line 18 · 2026-05-10T18:39:23.175Z_

<details><summary>↩ Tool result · `toolu_01WnHintxGVQFLWb5knCgQYK`</summary>

```text
# Draft-Conditioned Constrained Decoding: Paper Summary

**Full Title:** Draft-Conditioned Constrained Decoding for Structured Generation in LLMs

**Authors:** Avinash Reddy, Thayne T. Walker, James S. Ide, Amrit Singh Bedi

**Submission Date:** February 8, 2026 (arXiv:2603.03305)

## Core Methodology

The paper addresses a critical problem in LLM output generation: constrained decoding can distort semantic quality by enforcing validity token-by-token through masking. DCCD decouples these concerns into two phases:

1. **Unconstrained draft generation** produces semantic planning without structural constraints
2. **Conditioned constrained decoding** applies validity enforcement using the draft as context

This approach avoids pushing the model toward "locally valid yet semantically incorrect trajectories."

## Key Performance Results

The research demonstrates substantial improvements, with the most dramatic result being a "+24 percentage points" gain on GSM8K using a 1B model (increasing from 15.2% to 39.0% on structured accuracy metrics). Additionally, smaller model pairs can now match or exceed much larger constrained baselines, indicating significant parameter efficiency gains.

## Technical Analysis

The authors employ a **KL-projection framework** showing that draft conditioning increases feasible probability mass and reduces cumulative "projection tax" from hard constraints. An optional **best-of-K draft selection** mechanism further refines results.

## Benchmarks & Training Requirements

- Evaluated across structured reasoning benchmarks
- **Training-free inference procedure** requiring no model fine-tuning
- GSM8K benchmark specifically mentioned with 1B model testing

## Additional Contributions

The methodology enables smaller models to achieve performance parity with substantially larger constrained baselines, demonstrating practical efficiency improvements for deployment scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "657bc73d-a000-4a1f-a08c-bbe3c9f30c4c",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "098fe2a1-ac05-482b-b39e-6f4e66b3ce99",
  "sourceToolAssistantUUID": "657bc73d-a000-4a1f-a08c-bbe3c9f30c4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T18:39:23.262Z_

<details><summary>↩ Tool result · `toolu_01UA1ekiUi1gd4Ecp4qAdtNH`</summary>

```text
# The Format Tax - Paper Summary

**Full Title:** The Format Tax

**Authors:** Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick

**Core Finding on Degradation:**
The research identifies that format-requesting instructions themselves cause most accuracy loss before any decoder constraints are applied. The authors note that "sampling bias accounts for only a fraction of the degradation" and that "the dominant cost enters at the prompt."

**Evidence Provided:**
- Six open-weight models tested
- Four API models tested
- Four formats evaluated (JSON, XML, LaTeX, Markdown)
- Tasks spanning math, science, logic, and writing domains

**Key Diagnosis:**
The authors propose decoupling reasoning from formatting as the solution. This involves either generating freeform text first then reformatting afterward, or enabling extended thinking within single generation passes.

**Recovery Results:**
The decoupling approach "substantially recovers lost accuracy" across tested models and formats. Notably, recent closed-weight models exhibit minimal to no format tax, suggesting this represents a gap in current open-weight model capabilities rather than an inherent limitation.

**Availability:**
Code is provided at the project's GitHub repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "566a5b53-b572-4129-849b-74de6abc5d19",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "34a574d2-eb7e-4e02-a901-6608adc489a7",
  "sourceToolAssistantUUID": "566a5b53-b572-4129-849b-74de6abc5d19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T18:39:27.453Z_

Now let me fetch the full HTML versions of both papers to get more granular details about benchmarks, experimental results, and the specific mechanisms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34a574d2-eb7e-4e02-a901-6608adc489a7",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNmAmm1A8hAYCHATnZ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05ee5f2b-cdc5-437f-9173-a5b322b5fda7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFQjLrvviuK8DTaHvWbpRk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1807,
      "cache_read_input_tokens": 13643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1807,
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

_source line 21 · 2026-05-10T18:39:30.532Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016UMyubdFWVfE4oCsJfe3nR`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.03305",
  "prompt": "Extract detailed information about: (1) The full list of benchmarks used beyond GSM8K, (2) The exact experimental setup - what models were used, what sizes, (3) The KL-projection analysis details - how does draft conditioning increase feasible mass and reduce projection tax, (4) How best-of-K draft selection works, (5) Any tables showing main results across benchmarks, (6) How the two-step procedure works in detail - does the draft go into the prompt for step 2? (7) Any comparisons to other methods like chain-of-thought or other structured generation approaches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05ee5f2b-cdc5-437f-9173-a5b322b5fda7",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNmAmm1A8hAYCHATnZ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "338ca4ef-8a41-42ee-9c0a-e1912a2cb90f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFQjLrvviuK8DTaHvWbpRk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1807,
      "cache_read_input_tokens": 13643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1807,
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

_source line 22 · 2026-05-10T18:39:33.918Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018s8WWCSDXYzZofusazEX8o`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03616",
  "prompt": "Extract detailed information about: (1) The exact experimental evidence for prompt-level vs decoder-level degradation - what are the numbers? (2) How much accuracy is lost from prompt-level instructions vs decoder-level constraints? (3) What specific benchmarks and tasks were used? (4) How does this relate to reducing per-step schema complexity? (5) The decoupling approach details - generate-then-reformat vs extended thinking, (6) Quantitative results showing how much accuracy is recovered, (7) Which closed-weight models show no format tax? (8) Any discussion of why prompt-level instructions cause more degradation than decoder constraints."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "338ca4ef-8a41-42ee-9c0a-e1912a2cb90f",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNmAmm1A8hAYCHATnZ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f1f18ce-4bc9-4603-bb37-b9d003ae06bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFQjLrvviuK8DTaHvWbpRk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1807,
      "cache_read_input_tokens": 13643,
      "output_tokens": 447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1807
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 447,
          "cache_read_input_tokens": 13643,
          "cache_creation_input_tokens": 1807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1807,
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

_source line 23 · 2026-05-10T18:39:45.646Z_

<details><summary>↩ Tool result · `toolu_016UMyubdFWVfE4oCsJfe3nR`</summary>

```text
# Draft-Conditioned Constrained Decoding: Detailed Analysis

## (1) Full List of Benchmarks

Beyond GSM8K, the paper evaluates on:
- **MATH500**: A 500-problem subset covering algebra, geometry, and number theory
- **GSM-Symbolic**: A symbolic variant of GSM8K testing genuine mathematical reasoning
- **FOLIO**: First-order logic reasoning dataset requiring formal logical proofs verified by Prover9

## (2) Experimental Setup and Models

Models tested range from 1B to 14B parameters:
- Llama 3.2 1B
- Qwen 2.5 1.5B
- Qwen 2.5 3B
- Qwen 2.5 7B
- Llama 3.1 8B
- Qwen 2.5 14B

"Instruction-tuned models ranging from 1B to 14B parameters" were evaluated across all benchmarks with different constraint types (JSON schemas, expression grammars, FOL grammars).

## (3) KL-Projection Analysis Details

The paper frames constrained decoding as "repeated reverse-KL projections onto a prefix-valid set." The projection tax is quantified as:

**KL(ρq(·|x)∥ρθ(·|x))=𝔼z~ρq [∑ᵗ log(1/α(hₜ))]**

Where α(hₜ) = "feasible mass"—the probability the model assigns to valid tokens. When α(hₜ) is low, the per-step distortion log(1/α) becomes large.

Draft conditioning increases feasible mass because: "If we append auxiliary text d to the context, the model induces a different next-token distribution πθ(a|hₜ,d), changing feasible mass to α(hₜ;d)."

When the draft contains semantic content aligned with formatting requirements, "the forced prefix becomes in-distribution under the conditioned model, so the answer-slot distribution is better preserved."

## (4) Best-of-K Draft Selection

Algorithm 1 generates K unconstrained drafts in parallel. Selection uses "cumulative log feasible mass incurred during constrained decoding, which directly reflects the amount of constraint-induced distortion."

The algorithm scores each candidate as: **S(k) ← S(k) + log(α̃ₜ(k))** across all decoding steps, selecting "k* ∈ argmaxₖ S(k)."

When K=1, the method reduces to simple two-step inference.

## (5) Main Results Table

| Dataset | Model | CD | DCCD | Improvement |
|---------|-------|-----|------|------------|
| GSM8K | 1B | 15.24% | 39.04% | +23.8pp |
| GSM8K | 1.5B | 49.36% | 73.92% | +24.6pp |
| GSM8K | 14B | 86.43% | 95.15% | +8.7pp |
| MATH500 | 1B | 6.00% | 19.80% | +13.8pp |
| FOLIO | 7B | 19.70% | 31.53% | +11.8pp |

Gains are "particularly large for smaller models" where constraint distortion is strongest.

## (6) Two-Step Procedure Details

**Step 1**: "Sample a draft y∼pₐᵣₐfₜ(·|x)" without structural constraints.

**Step 2**: "Generate final structured output z₁:ₜ using constrained decoding conditioned on (x,y)." The draft becomes part of the context h̃ₜ ≜ (x,y,z<t), passed directly into the model alongside the input prompt.

Hard constraints "still apply to the final output prefix hₜ=(x,z<t)." The valid-next-token set remains A(hₜ), ensuring exact validity guarantees.

## (7) Comparisons to Other Methods

The paper compares against:
- **Constrained Prompting (CP)**: System prompts specifying format
- **Constrained Few-Shot (CF)**: Few-shot examples with format specifications
- **Constrained Decoding (CD)**: XGrammar token-level masking (state-of-the-art baseline)

No comparison to chain-of-thought methods is provided. The paper notes that interleaved reasoning approaches like CRANE "reduce to standard constrained decoding when structure is required from the first token."

DCCD shows consistent improvements, with parameter-efficient two-model compositions outperforming single larger models—a 7B+1.5B composition achieves better "accuracy per billion" than single 14B constrained models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "338ca4ef-8a41-42ee-9c0a-e1912a2cb90f",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "d061c4b1-3512-448e-b2c8-4f88f3026a3e",
  "sourceToolAssistantUUID": "338ca4ef-8a41-42ee-9c0a-e1912a2cb90f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T18:39:53.223Z_

<details><summary>↩ Tool result · `toolu_018s8WWCSDXYzZofusazEX8o`</summary>

```text
# The Format Tax: Experimental Evidence & Analysis

## (1) Prompt-Level vs Decoder-Level Degradation: Exact Numbers

The research isolates these sources by comparing GET· (format-requesting prompt, no constraints) against GETC (same prompt plus grammar-constrained decoding).

**Key finding:** "Of 39 cells with any statistically significant effect, 36 (92%) are already present under the format-requesting prompt alone and only 15 (38%) involve GCD."

**Quantitative breakdown:**
- Average GET· degradation: −3.9 percentage points
- Average GCD-only additional loss: −1.6 percentage points

The data reveals decoder constraints contribute minimally beyond what the prompt already causes.

## (2) Accuracy Loss: Prompt vs Decoder Attribution

Across open-weight models on reasoning benchmarks:

- **Prompt-level cost dominates**: The format-requesting instructions alone account for most accuracy reduction before any decoder constraint applies
- **Decoder impact**: Grammar-constrained decoding adds only marginal additional degradation
- **Per-question flip rates**: "25.9% with GCD and 24.1% without," indicating the prompt drives the effect

Format validity improves dramatically (55.7% → 92.2% with GCD) while accuracy remains unchanged, demonstrating "models that produce valid structured output lose just as much accuracy as those that fail to comply."

## (3) Specific Benchmarks & Tasks

Four distinct evaluation domains:

- **MATH-500**: 500 competition math problems with open-ended answers requiring multi-step symbolic reasoning
- **GPQA-Diamond**: 198 graduate-level science questions (physics, chemistry, biology) in 4-choice format
- **ZebraLogic**: 500 constraint satisfaction puzzles requiring systematic deduction
- **WritingBench**: 500 open-ended writing tasks judged by LLM on prose quality

Four output formats tested: JSON Schema, XML, Markdown, LaTeX

Ten models: six open-weight (qwen3-32b/8b, olmo3.1-32b/3-7b, smollm3-3b, nemotron3-nano) and four API models

## (4) Schema Complexity & Per-Step Constraints

The paper doesn't directly address schema complexity reduction as a mitigation. Instead, it focuses on temporal decoupling—separating reasoning from formatting rather than simplifying the constraints themselves. The U-shaped relationship between token compression/expansion and answer flips suggests the issue stems from how format requirements redirect reasoning, not the structural complexity of the output schema.

## (5) Decoupling Approach Details

Two primary strategies:

**2-Turn generation:**
- Turn 1: Generate freeform answer with no format mention (··T· prompt)
- Turn 2: Reformat output into target structure (GET· or GETC)
- Cost: Two inference calls, approximately doubled token consumption

**Extended thinking:**
- Model generates hidden reasoning trace before visible output
- Format-requesting prompt remains present
- Thinking creates "temporally separate reasoning phase before the model commits to the requested structure"

## (6) Accuracy Recovery: Quantitative Results

**2-Turn effectiveness:**
- Significantly improves 42 of 72 model-task-format comparisons (p<0.05)
- Average recovery: +6.8 percentage points
- Worsens only 2 comparisons (3% worsening rate)
- Strongest on MATH-500: 19 of 24 improved

**Extended thinking effectiveness:**
- Significantly improves 43 of 72 comparisons (+9.2 pp average)
- Higher risk: 11 comparisons (15%) worsen
- Concentrates on MATH-500: 22 of 24 improved, 0 worsened
- Mixed results on ZebraLogic; fails to help writing tasks

**Example recovery (Table 5):**
- qwen3-32b MATH: −7 pp degradation → +2 pp improvement with 2-Turn
- olmo3-7b MATH: −7 pp degradation → +1 pp improvement with 2-Turn

## (7) Closed-Weight Models Showing No Format Tax

Three recent closed-weight models demonstrate near-zero or positive deltas:

- **claude-haiku-4.5**: +1.2 pp average (no GCD), +1.6 pp with GCD
- **grok-4.1-fast**: +2.5 pp average (no GCD), +4.3 pp with GCD
- **gpt-5.4-nano**: +2.5 pp average (no GCD), with GCD exceptions noted

By contrast, gpt-5-nano (older API model) still suffers: −5.2 pp without GCD, −8.0 pp with GCD.

The paper notes: "Newer closed-weight models show near-zero degradation, suggesting that the tax is not inherent to structured generation."

## (8) Why Prompt-Level Instructions Cause More Degradation

The analysis identifies two mechanisms:

**Token compression effect:** "71% of structured outputs are shorter than their freeform counterparts (median Δ = −162 tokens)." Answer flip rates follow a U-shaped curve, highest at strongest compression/expansion extremes, suggesting "format constraints compress or redirect visible reasoning, causing answer flips."

**Reasoning redirection:** Format requests force models to produce reasoning and valid structure simultaneously. This competing demand—satisfying both the task logic and structural constraints within a single output—degrades reasoning quality. Separating these concerns (via 2-Turn) or deferring structure generation (via thinking) substantially recovers performance.

The decoder constraint merely "reinforces a constraint the model is already attempting to satisfy," making decoder-level fixes inherently limited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f1f18ce-4bc9-4603-bb37-b9d003ae06bb",
  "isSidechain": true,
  "promptId": "b6157cca-d149-4412-94bd-1f2959b7ac1c",
  "agentId": "a40203604e8271a8a",
  "type": "user",
  "uuid": "b11d6d09-92dc-4d38-b863-106eb91cf490",
  "sourceToolAssistantUUID": "0f1f18ce-4bc9-4603-bb37-b9d003ae06bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T18:40:51.277Z_

Excellent. I now have comprehensive details on both papers. Here is the full report.

---

## Paper 1: "Draft-Conditioned Constrained Decoding for Structured Generation in LLMs" (arXiv:2603.03305, February 2026)

**Authors:** Avinash Reddy, Thayne T. Walker, James S. Ide, Amrit Singh Bedi

### How DCCD Decouples Semantic Planning from Structural Enforcement

DCCD is a two-step inference procedure:

- **Step 1 (Semantic Planning):** The model generates an unconstrained draft `y ~ p_draft(.|x)` with no structural constraints. This draft captures the full semantic reasoning/plan without being distorted by token-level masking.
- **Step 2 (Structural Enforcement):** Constrained decoding generates the final structured output `z`, but now conditioned on the context `(x, y)` -- i.e., the draft is prepended as part of the prompt context. Hard constraints (grammar masks via XGrammar) still enforce exact validity on the output tokens, but because the model has already "seen" the semantic plan in the draft, its next-token distribution assigns much higher probability to valid continuations. This means the constraint masking/renormalization is far less distortive.

The key theoretical insight is framed via **KL-projection**: standard constrained decoding performs repeated reverse-KL projections onto the set of valid next tokens. Each projection incurs a "projection tax" of `log(1/alpha(h_t))` where `alpha` is the "feasible mass" -- the probability the unconstrained model assigns to valid tokens at step t. When feasible mass is low (the model doesn't naturally want to produce valid tokens), distortion is severe. Draft conditioning increases feasible mass because the draft shifts the model's distribution toward schema-consistent continuations, making the forced prefix "in-distribution" under the conditioned model.

### The +24 pp Improvement

The headline number comes from GSM8K with small models:

| Dataset | Model | Standard CD | DCCD | Improvement |
|---------|-------|------------|------|-------------|
| GSM8K | Llama 3.2 1B | 15.24% | 39.04% | +23.8 pp |
| GSM8K | Qwen 2.5 1.5B | 49.36% | 73.92% | +24.6 pp |
| GSM8K | Qwen 2.5 14B | 86.43% | 95.15% | +8.7 pp |
| MATH500 | 1B | 6.00% | 19.80% | +13.8 pp |
| FOLIO | 7B | 19.70% | 31.53% | +11.8 pp |

Gains are largest for smaller models where constraint distortion is most severe. A 7B+1.5B two-model composition can outperform a single 14B constrained model in "accuracy per billion parameters."

### Training-Free?

**Yes, entirely training-free.** It is a pure inference-time procedure. No fine-tuning, no additional training data, no learned components. Any instruction-tuned model can be used out-of-the-box.

### Benchmarks

Four benchmarks spanning different constraint types:
- **GSM8K** -- grade-school math with JSON schema constraints
- **MATH500** -- 500 competition math problems (algebra, geometry, number theory) with expression grammars
- **GSM-Symbolic** -- symbolic variant of GSM8K testing genuine mathematical reasoning
- **FOLIO** -- first-order logic reasoning requiring formal proofs verified by Prover9, with FOL grammars

Models tested: Llama 3.2 1B, Qwen 2.5 1.5B/3B/7B/14B, Llama 3.1 8B.

**Optional enhancement -- Best-of-K draft selection:** Generate K drafts in parallel, score each by cumulative log feasible mass during constrained decoding (measuring how much distortion each draft would incur), and select the draft with the highest score. When K=1, it reduces to simple two-step inference.

---

## Paper 2: "The Format Tax" (arXiv:2604.03616, April 2026)

**Authors:** Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick (UC San Diego)

### Key Finding: Prompt-Level vs. Decoder-Level Degradation

The central finding is that **the prompt-level instruction to produce structured output causes the vast majority of accuracy loss, not the decoder-level grammar constraints.** The paper isolates these effects by comparing:
- `GET.` = format-requesting prompt, no decoder constraints
- `GETC` = format-requesting prompt + grammar-constrained decoding (GCD)

**The numbers are striking:** Of 39 experimental cells showing statistically significant degradation, **36 (92%) are already present from the prompt instruction alone**, and only 15 (38%) involve GCD. Quantitatively:
- Average prompt-level degradation: **-3.9 percentage points**
- Average additional decoder-level (GCD) loss: **-1.6 percentage points**

Per-question flip rates tell the same story: 24.1% of answers flip without GCD vs 25.9% with GCD -- nearly identical. Meanwhile, format validity improves dramatically (55.7% to 92.2% with GCD), confirming that decoder constraints do their job structurally but don't meaningfully add to reasoning degradation.

### Evidence Provided

The evidence is extensive:
- **10 models:** 6 open-weight (Qwen3-32b/8b, OLMo3.1-32b/3-7b, SmolLM3-3b, Nemotron3-nano) + 4 API models
- **4 formats:** JSON Schema, XML, Markdown, LaTeX
- **4 task domains:** MATH-500 (competition math), GPQA-Diamond (graduate-level science), ZebraLogic (constraint satisfaction), WritingBench (open-ended writing)
- Statistical significance testing with per-question analysis

**Why does the prompt cause more damage than the decoder?** Two mechanisms identified:
1. **Token compression:** 71% of structured outputs are shorter than freeform counterparts (median delta = -162 tokens). Answer flip rates follow a U-shaped curve peaking at extreme compression/expansion, suggesting format constraints compress or redirect visible reasoning.
2. **Reasoning redirection:** Format-requesting prompts force models to satisfy both task logic and structural constraints simultaneously in a single output pass, degrading reasoning quality.

### Mitigation: Decoupling Reasoning from Formatting

Two strategies that substantially recover accuracy:

1. **2-Turn generation:** Turn 1 generates freeform reasoning with no format mention; Turn 2 reformats into the target structure. Results: significantly improves 42/72 comparisons (+6.8 pp average), worsens only 2 (3% worsening rate).

2. **Extended thinking:** The model generates a hidden reasoning trace before committing to visible structured output. Results: significantly improves 43/72 comparisons (+9.2 pp average), but higher risk with 11 comparisons (15%) worsening.

### Closed-Weight Models Show No Tax

Critically, recent closed-weight models exhibit near-zero or even *positive* format effects:
- claude-haiku-4.5: +1.2 pp average
- grok-4.1-fast: +2.5 pp average
- gpt-5.4-nano: +2.5 pp average

This suggests the format tax is **not inherent** to structured generation but reflects a gap that current open-weight models haven't yet closed (likely through training-time mitigation).

### Relationship to Per-Step Schema Complexity

The paper does not directly advocate reducing per-step schema complexity. Instead, its diagnosis points to **temporal decoupling** as the fix: separate the reasoning phase from the formatting phase in time, rather than simplifying the constraints themselves. The evidence shows the problem isn't the structural complexity of the output schema but the cognitive burden of satisfying task reasoning and format compliance simultaneously. This aligns with DCCD's approach -- both papers converge on the insight that generating content first and applying structure second is superior to doing both at once.

---

## How the Two Papers Connect

Both papers arrive at the same fundamental insight from different angles:
- **DCCD** shows that constrained decoding distorts semantics and fixes it by generating an unconstrained draft first, then applying structure.
- **The Format Tax** shows that even *prompting* for structure (before any decoder constraint) degrades reasoning, and fixes it by temporal decoupling (2-turn or extended thinking).

Together, they paint a clear picture: the act of simultaneously reasoning and producing structured output is the core problem, whether the structure is enforced by decoder masks or merely requested in the prompt. The solution in both cases is to let the model reason freely first, then handle formatting as a separate concern.

Sources:
- [DCCD: Draft-Conditioned Constrained Decoding (arXiv:2603.03305)](https://arxiv.org/abs/2603.03305)
- [DCCD Full HTML](https://arxiv.org/html/2603.03305)
- [The Format Tax (arXiv:2604.03616)](https://arxiv.org/abs/2604.03616)
- [The Format Tax Full HTML](https://arxiv.org/html/2604.03616)
- [The Format Tax on Ribbit Ribbit](https://ribbitribbit.co/paper/arxiv.2604.03616-The-Format-Tax)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b11d6d09-92dc-4d38-b863-106eb91cf490",
  "isSidechain": true,
  "agentId": "a40203604e8271a8a",
  "requestId": "req_011CauNoPMc8jMUYApGcAuk6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47e11cb6-2a90-48ee-8209-95dd9a214113",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e5cf350-1f40-4669-8ead-ff2293714b4b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P6JPXfsb64EAGzFYu66Amo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 15450,
      "output_tokens": 2314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3012
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2314,
          "cache_read_input_tokens": 15450,
          "cache_creation_input_tokens": 3012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3012,
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
