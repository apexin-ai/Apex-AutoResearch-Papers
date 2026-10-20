# Research conversation: Search the web to verify these papers exist and check their claims: 1. **BridgeRAG** - claimed to be "arXiv 2604.03384, 

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a93291f0432d9bb7c.jsonl`
- **Structured JSON:** [`bc18fffc74e2d5f4ffa2.json`](../../sessions/bc/bc18fffc74e2d5f4ffa2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-14T16:05:03.726Z_

Search the web to verify these papers exist and check their claims:

1. **BridgeRAG** - claimed to be "arXiv 2604.03384, April 2026". It supposedly uses a training-free tripartite scorer s(q,b,c) for bridge-conditioned retrieval, achieving R@5=0.99 on HotpotQA. Check:
   - Does this paper actually exist on arXiv?
   - What are its actual methods and results?

2. **CUE-R** - claimed to be "arXiv 2604.05467, April 2026". It supposedly proposes an operational evidence-role taxonomy via intervention analysis, showing non-additive evidence interactions (F1 drops of 0.493 vs. 0.205 and 0.186 for individual removals). Check:
   - Does this paper exist?
   - What are its actual findings?

3. **IndexRAG** - claimed to be "arXiv 2603.16415, March 2026". Supposedly identifies bridge entities at index time for retrieval augmentation (+4.6 F1 over Naive RAG). Check:
   - Does this paper exist?
   - What are its actual contributions?

4. **BRIEF-Pro** - claimed to be "ACL 2026 Findings, arXiv 2510.13799". Supposedly achieves 34x abstractive compression on HotpotQA with 49.0 EM / 63.1 F1 with 8B reader. Check:
   - Does this paper exist?
   - What are its actual results?

Use WebSearch and WebFetch to verify. Report exactly what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "3e51149f-c204-4e19-ab2e-3b88ed8ca6c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T16:05:03.728Z_

```json
{
  "parentUuid": "3e51149f-c204-4e19-ab2e-3b88ed8ca6c2",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
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
  "uuid": "116acacd-2dc3-4bad-ac78-f29a9866ccb6",
  "timestamp": "2026-05-14T16:05:03.728Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T16:05:06.851Z_



I'll search for each of these papers systematically. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "116acacd-2dc3-4bad-ac78-f29a9866ccb6",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kEGva4xGrUmCErYqQg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e44d7ba3-853e-4362-9300-2c1c1d4e12c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2uvkj5TdwWNHkE4U65yEX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 937,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-14T16:05:06.944Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T2qQrrPcDo7e3VjgYahNzV`</summary>

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
  "parentUuid": "e44d7ba3-853e-4362-9300-2c1c1d4e12c6",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kEGva4xGrUmCErYqQg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd136f03-a067-486c-a428-84e5f7770eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2uvkj5TdwWNHkE4U65yEX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 937,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-14T16:05:06.950Z_

<details><summary>↩ Tool result · `toolu_01T2qQrrPcDo7e3VjgYahNzV`</summary>

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
  "parentUuid": "dd136f03-a067-486c-a428-84e5f7770eb7",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "4aabda23-c72c-484e-b940-6baec7b3d1c3",
  "sourceToolAssistantUUID": "dd136f03-a067-486c-a428-84e5f7770eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T16:05:10.084Z_



Now let me search for all four papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aabda23-c72c-484e-b940-6baec7b3d1c3",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kEWkmcroN6huLZs3CL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f65109b-4046-404c-a8df-454b2e83a3b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mu4VRYXvvMdWyiVxBi1AC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 7 · 2026-05-14T16:05:10.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GZ7Y9JJ4UL8PGQfRU6JAkw`</summary>

```json
{
  "query": "arXiv 2604.03384 BridgeRAG bridge-conditioned retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f65109b-4046-404c-a8df-454b2e83a3b4",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kEWkmcroN6huLZs3CL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1515e4bb-6bd4-4ff8-b7c4-5efab5c91abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mu4VRYXvvMdWyiVxBi1AC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 8 · 2026-05-14T16:05:11.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lz3SQEa83rQssagWemQPRZ`</summary>

```json
{
  "query": "arXiv 2604.05467 CUE-R evidence-role taxonomy intervention analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1515e4bb-6bd4-4ff8-b7c4-5efab5c91abc",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kEWkmcroN6huLZs3CL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feb4dc5a-7fe6-47cc-853d-9e980f92925d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mu4VRYXvvMdWyiVxBi1AC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 9 · 2026-05-14T16:05:11.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015RtkBiNXKCZTGde2iqfKWz`</summary>

```json
{
  "query": "arXiv 2603.16415 IndexRAG bridge entities index time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feb4dc5a-7fe6-47cc-853d-9e980f92925d",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kEWkmcroN6huLZs3CL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a821ddea-537c-4067-a4f1-3cfdc2f0386d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mu4VRYXvvMdWyiVxBi1AC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 10 · 2026-05-14T16:05:11.898Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018TtuvrCWKBpe55cXyUHJ1x`</summary>

```json
{
  "query": "arXiv 2510.13799 BRIEF-Pro abstractive compression HotpotQA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a821ddea-537c-4067-a4f1-3cfdc2f0386d",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kEWkmcroN6huLZs3CL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45adf73c-fa2d-4491-9f24-96bb6348890d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Mu4VRYXvvMdWyiVxBi1AC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 9160,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 9160,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1915,
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

_source line 11 · 2026-05-14T16:05:15.763Z_

<details><summary>↩ Tool result · `toolu_01Lz3SQEa83rQssagWemQPRZ`</summary>

```text
Web search results for query: "arXiv 2604.05467 CUE-R evidence-role taxonomy intervention analysis"

Links: [{"title":"Facet-Level Tracing of Evidence Uncertainty and Hallucination in RAG","url":"https://arxiv.org/html/2604.09174v1"},{"title":"[2604.25923] Evaluation Revisited: A Taxonomy of Evaluation Concerns in Natural Language Processing","url":"https://arxiv.org/abs/2604.25923"},{"title":"[2604.08082] From Binary Groundedness to Support Relations: Towards a Reader-Centred Taxonomy for Comprehension of AI Output","url":"https://arxiv.org/abs/2604.08082"},{"title":"[2604.08016] Wiring the 'Why': A Unified Taxonomy and Survey of Abductive Reasoning in LLMs","url":"https://arxiv.org/abs/2604.08016"},{"title":"From Binary Groundedness to Support Relations: Towards a Reader-Centred Taxonomy for Comprehension of AI Output","url":"https://arxiv.org/html/2604.08082"},{"title":"Dharma, Data and Deception: An LLM-Powered Rhetorical Analysis of Cow-Urine Health Claims on YouTube","url":"https://arxiv.org/html/2604.22606"},{"title":"Evaluation Revisited: A Taxonomy of Evaluation Concerns in Natural Language Processing","url":"https://arxiv.org/html/2604.25923"},{"title":"[2604.25222] Adaptive Management of Microservices in Dynamic Computing Environments: A Taxonomy and Future Directions","url":"https://arxiv.org/abs/2604.25222"},{"title":"Spontaneous Persuasion: An Audit of Model Persuasiveness in Everyday Conversations","url":"https://arxiv.org/html/2604.22109v1"},{"title":"Wiring the ‘Why’: A Unified Taxonomy and Survey of Abductive Reasoning in LLMs","url":"https://arxiv.org/html/2604.08016v1"}]

The search results don't contain the specific arXiv paper 2604.05467 with the exact title and keywords you mentioned. The results returned papers with similar arXiv IDs from the 2604.xxxxx range and related topics about evidence, taxonomies, and intervention analysis, but not the exact paper you're looking for.

To find the specific paper you're interested in, I recommend:

1. **Directly accessing arXiv**: Visit https://arxiv.org/abs/2604.05467 to access the paper directly by its ID
2. **Searching with a different approach**: If you have the paper title or author names, I can search again with that information
3. **Checking the paper's full title**: The keywords you mentioned (CUE-R, evidence-role taxonomy, intervention analysis) suggest this may be a specific methodological or analytical framework paper

Would you like me to try searching with different keywords or information you might have about this paper?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feb4dc5a-7fe6-47cc-853d-9e980f92925d",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "179d6d4b-7a72-4cbf-88f4-0933a29f594b",
  "sourceToolAssistantUUID": "feb4dc5a-7fe6-47cc-853d-9e980f92925d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T16:05:18.215Z_

<details><summary>↩ Tool result · `toolu_01GZ7Y9JJ4UL8PGQfRU6JAkw`</summary>

```text
Web search results for query: "arXiv 2604.03384 BridgeRAG bridge-conditioned retrieval"

Links: [{"title":"BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering","url":"https://arxiv.org/html/2604.03384v1"},{"title":"Regime-Conditional Retrieval: Theory and a Transferable Router for Two-Hop QA","url":"https://arxiv.org/html/2604.09019"},{"title":"BRIDGE: Multimodal-to-Text Retrieval via Reinforcement-Learned Query Alignment","url":"https://arxiv.org/html/2604.07201"},{"title":"1 Introduction","url":"https://arxiv.org/html/2604.22757"},{"title":"[2604.07816v1] Tool Retrieval Bridge: Aligning Vague Instructions with Retriever Preferences via Bridge Model","url":"https://arxiv.org/abs/2604.07816v1"},{"title":"Tool Retrieval Bridge: Aligning Vague Instructions with Retriever Preferences via Bridge Model","url":"https://arxiv.org/html/2604.07816"},{"title":"[2604.07816] Tool Retrieval Bridge: Aligning Vague Instructions with Retriever Preferences via Bridge Model","url":"https://arxiv.org/abs/2604.07816"},{"title":"StratRAG: A Multi-Hop Retrieval Evaluation Dataset ...","url":"https://arxiv.org/html/2604.22757v1"},{"title":"Bridge-RAG: An Abstract Bridge Tree Based Retrieval Augmented Generation Algorithm With Cuckoo Filter","url":"https://arxiv.org/html/2603.26668"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=25&show=1000"}]

Based on the search results, I found the paper you were looking for:

## BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering

BridgeRAG is a training-free, graph-free retrieval method for retrieval-augmented generation (RAG) over multi-hop questions that uses a tripartite scorer over (question, bridge, candidate).

### Key Concept

The paper is based on the insight that multi-hop retrieval is not a single-step relevance problem: later-hop evidence should be ranked by its utility conditioned on retrieved bridge evidence, not by similarity to the original query alone.

### How It Works

BridgeRAG separates coverage from scoring: dual-entity ANN expansion broadens the second-hop candidate pool, while a bridge-conditioned LLM judge identifies the active reasoning chain among competing candidates without any offline graph or proposition index.

### Performance

The conditioning signal is selective: showing +2.55 percentage points on parallel-chain queries while having minimal effect on single-chain subtypes. BridgeRAG requires no training; all reasoning is performed by an off-the-shelf LLM.

The paper (arXiv:2604.03384) was published on April 3, 2026, by Andre Bacellar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1515e4bb-6bd4-4ff8-b7c4-5efab5c91abc",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "689bbaa5-e676-4d8e-9353-e502f149b2bd",
  "sourceToolAssistantUUID": "1515e4bb-6bd4-4ff8-b7c4-5efab5c91abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T16:05:18.529Z_

<details><summary>↩ Tool result · `toolu_015RtkBiNXKCZTGde2iqfKWz`</summary>

```text
Web search results for query: "arXiv 2603.16415 IndexRAG bridge entities index time"

Links: [{"title":"[2603.16415] IndexRAG: Bridging Facts for Cross-Document Reasoning at Index Time","url":"https://arxiv.org/abs/2603.16415"},{"title":"IndexRAG: Bridging Facts for Cross-Document Reasoning at Index Time","url":"https://arxiv.org/html/2603.16415"},{"title":"Paper page - IndexRAG: Bridging Facts for Cross-Document Reasoning at Index Time","url":"https://huggingface.co/papers/2603.16415"},{"title":"Implement IndexRAG: Bridging Facts for Cross-Document Reasoning at Index Time pipeline (2026) · Issue #326 · NomaDamas/AutoRAG-Research","url":"https://github.com/NomaDamas/AutoRAG-Research/issues/326"},{"title":"Bridge-RAG: An Abstract Bridge Tree Based Retrieval Augmented Generation Algorithm With Cuckoo Filter","url":"https://arxiv.org/html/2603.26668"},{"title":"Surrogate-Assisted Targeted Learning for Nested Bridge Functionals under Administrative Censoring","url":"https://arxiv.org/html/2603.10405"},{"title":"[2603.26668] Bridge-RAG: An Abstract Bridge Tree Based Retrieval Augmented Generation Algorithm With Cuckoo Filter","url":"https://arxiv.org/abs/2603.26668"},{"title":"BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence","url":"https://arxiv.org/html/2603.07931"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=25&show=1000"},{"title":"Towards Better Graph-based Cross-document Relation Extraction via Non-bridge Entity Enhancement and Prediction Debiasing","url":"https://arxiv.org/html/2406.16529"}]

Based on the search results, here's what I found about arXiv paper 2603.16415 (IndexRAG):

## Overview

IndexRAG is a novel approach that shifts cross-document reasoning from online inference to offline indexing.

## Bridge Entities and Index Time Processing

IndexRAG identifies bridge entities shared across documents and generates bridging facts as independently retrievable units, requiring no additional training or fine-tuning.

During indexing, the approach extracts atomic knowledge units (AKUs) and entities from each document, identifies entities that appear across multiple documents, and prompts an LLM to generate bridging facts that capture cross-document reasoning by linking related evidence from different sources.

## Performance Results

On three widely-used multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA, MuSiQue), IndexRAG improves F1 over Naive RAG by 4.6 points on average, while requiring only single-pass retrieval and a single LLM call at inference time.

When combined with IRCoT, IndexRAG outperforms all graph-based baselines on average, including HippoRAG and FastGraphRAG, while relying solely on flat retrieval.

The paper was submitted on March 17, 2026, by authors Zhenghua Bao and Yi Shi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a821ddea-537c-4067-a4f1-3cfdc2f0386d",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "07af5d34-0f48-467f-ae9d-46db9eb26118",
  "sourceToolAssistantUUID": "a821ddea-537c-4067-a4f1-3cfdc2f0386d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T16:05:19.902Z_

<details><summary>↩ Tool result · `toolu_018TtuvrCWKBpe55cXyUHJ1x`</summary>

```text
Web search results for query: "arXiv 2510.13799 BRIEF-Pro abstractive compression HotpotQA"

Links: [{"title":"BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning","url":"https://arxiv.org/html/2510.13799"},{"title":"[2510.13799] BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning","url":"https://arxiv.org/abs/2510.13799"},{"title":"RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation","url":"https://arxiv.org/html/2310.04408.pdf"},{"title":"AttnComp: Attention-Guided Adaptive Context Compression for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.17486"},{"title":"Characterizing Prompt Compression Methods for Long Context Inference","url":"https://arxiv.org/pdf/2407.08892"},{"title":"AdaComp: Extractive Context Compression with Adaptive Predictor for Retrieval-Augmented Large Language Models","url":"https://arxiv.org/html/2409.01579"},{"title":"Enhancing Cache-Augmented Generation (CAG) with Adaptive Contextual Compression for Scalable Knowledge Integration","url":"https://arxiv.org/html/2505.08261"},{"title":"EXIT: Context-Aware Extractive Compression for Enhancing","url":"https://arxiv.org/pdf/2412.12559"},{"title":"Style-Compress: An LLM-Based Prompt Compression Framework Considering Task-Specific Styles","url":"https://arxiv.org/html/2410.14042v1"},{"title":"Simple Context Compression: Mean-Pooling and Multi-Ratio Training","url":"https://arxiv.org/html/2510.20797v1"}]

Based on the search results, here's information about arXiv paper 2510.13799:

## BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning

The key innovation of BRIEF-Pro is its long-context synthetic data pipeline, developed from short-context seed data (fewer than 1k words), enabling abstractive compression of 10k+ word contexts across diverse scenarios.

BRIEF-Pro allows users to control compression length by designing an instruction-conditioned paradigm, specifying the desired number of sentences to balance conciseness and informativeness for specific application requirements.

### Evaluation

The paper evaluated BRIEF-Pro on four open-domain multi-hop question-answering (QA) datasets: the extended MuSiQue, HotpotQA, and 2WikiMultiHopQA from LongBench, and LongSeal, with context lengths ranging from 4.9k words and beyond.

BRIEF-Pro was initialized from Llama-3.2-3B-Instruct. The original training sets of MuSiQue, HotpotQA, and LongAlign were used as the seed data of the synthesis pipeline.

It is a universal, lightweight compressor that distills relevant evidence for a given query from retrieved documents into a concise summary for seamless integration into in-context RAG.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45adf73c-fa2d-4491-9f24-96bb6348890d",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "3cb04cc8-1f64-4d72-8741-d576e5b66d28",
  "sourceToolAssistantUUID": "45adf73c-fa2d-4491-9f24-96bb6348890d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T16:05:24.647Z_

Good, I found results for papers 1, 3, and 4. Paper 2 (CUE-R) didn't appear in the search. Let me now fetch the actual arXiv pages for more details and try the direct URL for CUE-R.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cb04cc8-1f64-4d72-8741-d576e5b66d28",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kFTsQviXxopH3PorZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d476c705-8ab9-42d8-b59e-4dea1b2a918e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSkR4EZzqo1gPwevt1rBxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 11075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
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

_source line 16 · 2026-05-14T16:05:26.487Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D3C2vtM3v9EUH1qBBq3EiY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03384",
  "prompt": "Extract the full title, authors, submission date, abstract, and any key results/metrics mentioned. Specifically look for: tripartite scorer s(q,b,c), R@5 on HotpotQA, and whether it's training-free."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d476c705-8ab9-42d8-b59e-4dea1b2a918e",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kFTsQviXxopH3PorZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33841e03-4f70-454f-a847-40295dc560c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSkR4EZzqo1gPwevt1rBxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 11075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
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

_source line 17 · 2026-05-14T16:05:28.452Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C9Ufef2jDYU7hwTkM6kGHY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.05467",
  "prompt": "Extract the full title, authors, submission date, abstract, and any key results/metrics mentioned. Specifically look for: CUE-R, evidence-role taxonomy, intervention analysis, non-additive evidence interactions, F1 drops of 0.493 vs 0.205 and 0.186."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33841e03-4f70-454f-a847-40295dc560c3",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kFTsQviXxopH3PorZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64dc5e33-db33-4c64-a5b9-feffb4a8b90c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSkR4EZzqo1gPwevt1rBxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 11075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
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

_source line 18 · 2026-05-14T16:05:29.365Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Krfy15QSnbRWEEAg8yW7YG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16415",
  "prompt": "Extract the full title, authors, submission date, abstract, and any key results/metrics mentioned. Specifically look for: bridge entities at index time, +4.6 F1 over Naive RAG, and the benchmarks used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64dc5e33-db33-4c64-a5b9-feffb4a8b90c",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kFTsQviXxopH3PorZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae009cb7-84ee-4c97-9201-580787714064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSkR4EZzqo1gPwevt1rBxo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 11075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3516,
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

_source line 19 · 2026-05-14T16:05:30.791Z_

<details><summary>↩ Tool result · `toolu_01D3C2vtM3v9EUH1qBBq3EiY`</summary>

```text
# BridgeRAG Paper Summary

**Full Title:** "BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering"

**Author:** Andre Bacellar

**Submission Date:** Submitted April 3, 2026; revised April 28, 2026 (v2)

**Training-Free Status:** Yes, explicitly described as "training-free"

**Tripartite Scorer:** The method employs "a tripartite scorer s(q,b,c) over (question, bridge, candidate)" to evaluate retrieval candidates based on their relationship to both the original question and intermediate bridge evidence.

**Key Results on HotpotQA:**
- Achieves R@5 of 0.9875
- Represents a +1.35pp improvement versus PropRAG

**Additional Performance Metrics:**
- MuSiQue: 0.8146 R@5 (+3.1pp vs. PropRAG, +6.8pp vs. HippoRAG2)
- 2WikiMultiHopQA: 0.9527 R@5 (+1.2pp vs. PropRAG)

The approach distinguishes itself by "separating coverage from scoring" and uses "bridge-conditioned LLM judge" decisions to identify reasoning chains without requiring offline graphs or training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33841e03-4f70-454f-a847-40295dc560c3",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "41fdffb2-095c-46ec-84ed-79461f2dee75",
  "sourceToolAssistantUUID": "33841e03-4f70-454f-a847-40295dc560c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T16:05:31.372Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019cAjp4ibp3YpveexyFxZyU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.13799",
  "prompt": "Extract the full title, authors, submission date, abstract, and any key results/metrics mentioned. Specifically look for: BRIEF-Pro, 34x abstractive compression, HotpotQA results of 49.0 EM / 63.1 F1, 8B reader, ACL 2026 Findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41fdffb2-095c-46ec-84ed-79461f2dee75",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kFTsQviXxopH3PorZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1baedc04-225e-4484-8423-d78ce1065d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSkR4EZzqo1gPwevt1rBxo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 11075,
      "output_tokens": 585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3516
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 585,
          "cache_read_input_tokens": 11075,
          "cache_creation_input_tokens": 3516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3516,
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

_source line 21 · 2026-05-14T16:05:33.381Z_

<details><summary>↩ Tool result · `toolu_01C9Ufef2jDYU7hwTkM6kGHY`</summary>

```text
# CUE-R: Paper Summary

**Title:** "CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation"

**Authors:** Siddharth Jain and Venkat Narayan Vedam

**Submission Date:** April 7, 2026

## Abstract Summary
The paper introduces CUE-R, a framework for evaluating how individual retrieved evidence items contribute to RAG system performance. Rather than focusing solely on final answers, it uses intervention-based analysis with REMOVE, REPLACE, and DUPLICATE operations to measure evidence utility across correctness, grounding faithfulness, and confidence metrics.

## Key Findings

The research demonstrates that:
- REMOVE and REPLACE operations substantially degrade both correctness and grounding while producing significant trace shifts
- DUPLICATE operations often prove answer-redundant but maintain behavioral similarity to original responses
- Multi-hop evidence exhibits non-additive interactions, meaning removing multiple supports causes far greater performance harm than individual removals would predict

The study tested these approaches on HotpotQA and 2WikiMultihopQA datasets using Qwen-3 8B and GPT-5.2 models.

**Evidence-Role Taxonomy:** The paper provides an "operational evidence-role taxonomy for interpreting intervention outcomes," enabling deeper analysis beyond answer-level evaluation.

The work concludes that intervention-based utility analysis meaningfully complements traditional answer-only RAG evaluation approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64dc5e33-db33-4c64-a5b9-feffb4a8b90c",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "3c6c88c6-1997-4194-91de-005abe2fc2d6",
  "sourceToolAssistantUUID": "64dc5e33-db33-4c64-a5b9-feffb4a8b90c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T16:05:33.542Z_

<details><summary>↩ Tool result · `toolu_01Krfy15QSnbRWEEAg8yW7YG`</summary>

```text
# IndexRAG Paper Summary

**Full Title:** IndexRAG: Bridging Facts for Cross-Document Reasoning at Index Time

**Authors:** Zhenghua Bao and Yi Shi

**Submission Date:** March 17, 2026

**Abstract:** The research addresses multi-hop question answering by shifting cross-document reasoning from runtime to indexing. The method identifies shared entities across documents and produces "bridging facts as independently retrievable units" without requiring additional training.

**Key Results & Metrics:**
- **F1 Improvement:** Achieved a 4.6-point F1 gain over Naive RAG on average
- **Benchmarks Tested:** HotpotQA, 2WikiMultiHopQA, and MuSiQue
- **Inference Efficiency:** Requires only single-pass retrieval and one LLM call
- **Baseline Comparisons:** When paired with IRCoT, it outperforms graph-based systems including HippoRAG and FastGraphRAG while using flat retrieval alone

**Key Innovation:** Bridge entities identified at index time enable efficient multi-document reasoning without complex online processing or iterative steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae009cb7-84ee-4c97-9201-580787714064",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "762b76e2-9afc-46b3-896e-2c2d3cda0fe8",
  "sourceToolAssistantUUID": "ae009cb7-84ee-4c97-9201-580787714064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T16:05:36.749Z_

<details><summary>↩ Tool result · `toolu_019cAjp4ibp3YpveexyFxZyU`</summary>

```text
# BRIEF-Pro Research Paper Summary

**Full Title:** "BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning"

**Authors:** Jia-Chen Gu, Junyi Zhang, Di Wu, Yuankai Li, Kai-Wei Chang, Nanyun Peng

**Submission Date:** October 15, 2025 (v1); April 27, 2026 (v2)

**Venue:** ACL 2026 Findings

## Abstract Summary

The paper presents BRIEF-Pro, a compression tool designed to tackle challenges in retrieval-augmented generation. The system "distills relevant evidence for a given query from retrieved documents into a concise summary" for integration into language models. Notably, it trains on shorter contexts (under 1,000 words) yet handles extended passages exceeding 10,000 words across diverse scenarios, with adjustable summary length control.

## Key Results

The document reports that "with the 70B reader model, 32x compression by BRIEF-Pro improves QA performance by 4.67% on average over LongLLMLingua's 9x, while requiring only 23% of its computational overhead."

**Note:** The specific metrics mentioned in your query (34x compression, HotpotQA 49.0 EM / 63.1 F1, 8B reader) do not appear in this web page excerpt.

**Code/Data:** Available at the provided GitHub repository link.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1baedc04-225e-4484-8423-d78ce1065d72",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "926ea24c-e7a7-42a4-8404-20828fdf446d",
  "sourceToolAssistantUUID": "1baedc04-225e-4484-8423-d78ce1065d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T16:05:40.749Z_

Good, I have results for all four papers. Let me now fetch the HTML versions of papers 1, 2, and 4 for more detailed metrics, since some of the specific numbers in the claims need verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "926ea24c-e7a7-42a4-8404-20828fdf446d",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kGjZkxSdADqEAF6fUq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58de7f9e-daa6-4780-a7c1-fd29627108fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWfePjstwQWNQ8nREQwCSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 14591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1938,
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

_source line 25 · 2026-05-14T16:05:43.118Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0176FL24CVTmLZgrxYVzPc7h`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03384v1",
  "prompt": "Look for the specific metric R@5=0.99 on HotpotQA. What is the actual R@5 on HotpotQA? Also look for the tripartite scorer notation s(q,b,c). Report exact numbers from tables if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58de7f9e-daa6-4780-a7c1-fd29627108fd",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kGjZkxSdADqEAF6fUq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3194824-8563-4170-9419-eabc377180b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWfePjstwQWNQ8nREQwCSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 14591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1938,
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

_source line 26 · 2026-05-14T16:05:45.032Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KuAa2yDzeWfZewnHsqFvcz`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.05467v1",
  "prompt": "Look for the specific F1 drop numbers: 0.493 vs 0.205 and 0.186 for individual removals. What are the actual numbers for non-additive evidence interactions? Look for the evidence-role taxonomy details and intervention analysis methodology. Report exact numbers from any tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3194824-8563-4170-9419-eabc377180b9",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kGjZkxSdADqEAF6fUq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "089fceff-0f2f-4a19-ad6b-f682deaa100e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWfePjstwQWNQ8nREQwCSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 14591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1938,
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

_source line 27 · 2026-05-14T16:05:46.485Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CFV6r2kCgJa18Y7ypFkDH5`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13799",
  "prompt": "Look for: (1) 34x abstractive compression ratio, (2) HotpotQA results of 49.0 EM and 63.1 F1, (3) results with an 8B reader model, (4) ACL 2026 mention. Report exact numbers from tables, especially EM and F1 on HotpotQA at different compression ratios and reader sizes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "089fceff-0f2f-4a19-ad6b-f682deaa100e",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kGjZkxSdADqEAF6fUq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "587b5f76-9ff5-4cb0-afdf-88730f40a022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWfePjstwQWNQ8nREQwCSj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 14591,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 480,
          "cache_read_input_tokens": 14591,
          "cache_creation_input_tokens": 1938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1938,
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

_source line 28 · 2026-05-14T16:05:47.907Z_

<details><summary>↩ Tool result · `toolu_0176FL24CVTmLZgrxYVzPc7h`</summary>

```text
# BridgeRAG Performance on HotpotQA

The actual R@5 on HotpotQA is **0.9875**, not 0.99. This appears in Table 2, where BridgeRAG achieves this score, representing a +1.35pp improvement over PropRAG's 0.974.

## Tripartite Scorer Notation

The method employs a bridge-conditioned scoring function denoted as **s(q,b,c)**, where:
- **q** = the original query
- **b** = the bridge passage (top-1 hop-1 retrieval)
- **c** = the candidate passage being ranked

As stated in the paper: "BridgeRAG separates coverage from scoring: dual-entity ANN expansion broadens the second-hop candidate pool, while a bridge-conditioned LLM judge identifies the active reasoning chain among competing candidates."

This tripartite formulation differs fundamentally from standard approaches using s(q,c) alone, enabling the method to disambiguate parallel reasoning chains by conditioning on what the first hop already retrieved.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3194824-8563-4170-9419-eabc377180b9",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "6e735d8d-0ee3-471e-b446-3bb74e20c5b6",
  "sourceToolAssistantUUID": "e3194824-8563-4170-9419-eabc377180b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T16:05:51.037Z_

<details><summary>↩ Tool result · `toolu_01CFV6r2kCgJa18Y7ypFkDH5`</summary>

```text
# BRIEF-Pro: Key Results Summary

## Compression Ratio
BRIEF-Pro achieves **32× compression** in auto mode (not 34×), with varying ratios across compression levels: High (68×), Medium (42×), and Low (25×).

## HotpotQA Performance (8B Reader)
Using Llama-3.1-8B-Instruct, BRIEF-Pro-Auto delivers: **49.0 EM and 63.05 F1** at 34× compression rate.

## 8B Reader Model Results
Across four datasets, BRIEF-Pro-Auto averages **38.79% EM**, compared to LongLLMLingua's 32.02% EM. The system shows consistent improvements over non-compression (32.09%) while achieving substantial compression.

## Publication Timing
The paper header indicates: "arXiv:2510.13799v2 [cs.CL] 27 Apr 2026"—suggesting future publication rather than ACL 2026 confirmation within the provided content.

## Key Advantage
BRIEF-Pro requires only "23% of LongLLMLingua's computational overhead" while delivering superior QA accuracy, highlighting efficiency gains alongside performance improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "587b5f76-9ff5-4cb0-afdf-88730f40a022",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "5845b1d6-6320-4cf3-a2b3-eb042684105c",
  "sourceToolAssistantUUID": "587b5f76-9ff5-4cb0-afdf-88730f40a022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T16:05:51.590Z_

<details><summary>↩ Tool result · `toolu_01KuAa2yDzeWfZewnHsqFvcz`</summary>

```text
# CUE-R: Evidence Interaction Effects in RAG

## Non-Additive Interaction Findings

The paper identifies striking evidence of non-additive interactions in multi-hop questions. In their two-support ablation on 51 HotpotQA examples:

- **Individual removals**: Mean F1 drops of 0.205 (support 1) and 0.186 (support 2)
- **Joint removal**: Mean F1 drop of 0.493
- **Synergy margin**: 0.046 excess degradation beyond the worse single removal
- **Complementary cases**: 13.7% of examples showed "strong complementary" patterns where neither single removal changed answers, but removing both caused failure

As the authors note, "removing both supports caused a mean F1 drop of 0.493, compared with 0.205 and 0.186 for individual removals," demonstrating that evidence items can interact non-additively.

## Evidence-Role Taxonomy

CUE-R operationalizes five roles through intervention analysis:

1. **Constructive**: Perturbation harms correctness/grounding
2. **Corrective**: Enables recovery from wrong intermediate states
3. **Redundant**: Negligible utility and trace changes
4. **Distractive**: Large trace divergence + utility harm
5. **Confidence-distorting**: Alters confidence without correctness benefit

## Key Methodology Elements

The framework applies three perturbation operators (remove, replace, duplicate) and measures changes across three utility axes: correctness, grounding faithfulness, and confidence error, plus a trace-divergence signal capturing behavioral changes independent of final answers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "089fceff-0f2f-4a19-ad6b-f682deaa100e",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "a20bc62e-8b98-4124-a1e5-b42a80a62a10",
  "sourceToolAssistantUUID": "089fceff-0f2f-4a19-ad6b-f682deaa100e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T16:05:54.652Z_

Now I have detailed data for all four papers. Let me do one more search to confirm the ACL 2026 status of BRIEF-Pro.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a20bc62e-8b98-4124-a1e5-b42a80a62a10",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kHoMjnf1p9sZwHRzUp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7af654c5-0c0f-491d-ad22-b61a7ab79141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5a73kf34gcks2NS3hrSHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 316,
      "cache_creation_input_tokens": 1166,
      "cache_read_input_tokens": 16529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1166,
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

_source line 32 · 2026-05-14T16:05:54.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KRRnVQt5CJ5f7cUHcTCfP1`</summary>

```json
{
  "query": "BRIEF-Pro \"ACL 2026\" Findings context compression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7af654c5-0c0f-491d-ad22-b61a7ab79141",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kHoMjnf1p9sZwHRzUp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f631ea19-b613-4940-a157-ebc73a223da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5a73kf34gcks2NS3hrSHk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 316,
      "cache_creation_input_tokens": 1166,
      "cache_read_input_tokens": 16529,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 316,
          "output_tokens": 99,
          "cache_read_input_tokens": 16529,
          "cache_creation_input_tokens": 1166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1166,
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

_source line 33 · 2026-05-14T16:06:00.603Z_

<details><summary>↩ Tool result · `toolu_01KRRnVQt5CJ5f7cUHcTCfP1`</summary>

```text
Web search results for query: "BRIEF-Pro "ACL 2026" Findings context compression"

Links: [{"title":"BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning","url":"http://web.cs.ucla.edu/~kwchang/bibliography/gu2026briefpro/"},{"title":"GitHub - dongwonjo/FastKV: [ACL Findings 2026] Official Implementation of \"FastKV: Decoupling of Context Reduction and KV Cache Compression for Prefill-Decoding Acceleration\" · GitHub","url":"https://github.com/dongwonjo/FastKV"},{"title":"Findings of the Association for Computational Linguistics (2026) - ACL Anthology","url":"https://aclanthology.org/events/findings-2026/"},{"title":"Findings - ACL 2026","url":"https://2026.aclweb.org/program/findings/"},{"title":"BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning","url":"https://arxiv.org/html/2510.13799"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"Extending Context Window of Large Language Models via Semantic Compression - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.306/"},{"title":"BRIEF: Bridging Retrieval and Inference for Multi-hop Reasoning via Compression - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.301/"},{"title":"ACON: Optimizing Context Compression for Long-horizon LLM Agents | OpenReview","url":"https://openreview.net/forum?id=7JbSwX6bNL"}]

Based on the search results, I found information about BRIEF-Pro and its context compression approach for ACL 2026:

BRIEF-Pro is a paper titled "Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning". The paper is authored by Gu, Jia-Chen, Zhang, Junyi, Wu, Di, Li, Yuankai, Chang, Kai-Wei, and Peng, Nanyun, and appears in ACL-Findings 2026.

BRIEF-Pro builds upon prior work: BRIEF (an earlier approach) performs query-aware multi-hop reasoning by compressing retrieved documents into highly dense textual summaries to integrate into in-context retrieval-augmented generation (RAG), using synthetic data curated by extracting atomic propositions that encapsulate distinct factoids from source documents.

The search results indicate that BRIEF-Pro extends this line of research with a focus on short-to-long synthesis for improved multi-hop reasoning, though the detailed findings specific to BRIEF-Pro's novel contributions are referenced in the ACL Anthology listing but the full paper details are not fully reproduced in these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f631ea19-b613-4940-a157-ebc73a223da9",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "a93291f0432d9bb7c",
  "type": "user",
  "uuid": "86c6df26-8cfe-4ab1-9ada-876bb448611d",
  "sourceToolAssistantUUID": "f631ea19-b613-4940-a157-ebc73a223da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-14T16:06:26.577Z_

I now have comprehensive information on all four papers. Here is my full report.

---

## Verification Report: Four Claimed Papers

### 1. BridgeRAG (arXiv 2604.03384)

**Existence: CONFIRMED.** The paper exists on arXiv at [2604.03384](https://arxiv.org/abs/2604.03384).

- **Title:** "BridgeRAG: Training-Free Bridge-Conditioned Retrieval for Multi-Hop Question Answering"
- **Author:** Andre Bacellar
- **Date:** Submitted April 3, 2026 (revised April 28, 2026, v2)

**Claim verification:**
- "Training-free tripartite scorer s(q,b,c)" -- **CONFIRMED.** The paper does use this exact notation for a bridge-conditioned scoring function over (question, bridge, candidate).
- "R@5=0.99 on HotpotQA" -- **INACCURATE.** The actual R@5 on HotpotQA is **0.9875**, not 0.99. This is close but has been rounded up. The +1.35pp improvement is over PropRAG (0.974).

---

### 2. CUE-R (arXiv 2604.05467)

**Existence: CONFIRMED.** The paper exists on arXiv at [2604.05467](https://arxiv.org/abs/2604.05467).

- **Title:** "CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation"
- **Authors:** Siddharth Jain and Venkat Narayan Vedam
- **Date:** April 7, 2026

**Claim verification:**
- "Operational evidence-role taxonomy via intervention analysis" -- **CONFIRMED.** CUE-R defines five operational roles (Constructive, Corrective, Redundant, Distractive, Confidence-distorting) using three perturbation operators (REMOVE, REPLACE, DUPLICATE).
- "Non-additive evidence interactions with F1 drops of 0.493 vs. 0.205 and 0.186" -- **CONFIRMED EXACTLY.** The paper reports on 51 HotpotQA examples: joint removal caused a mean F1 drop of 0.493, compared with 0.205 (support 1) and 0.186 (support 2) for individual removals, with a synergy margin of 0.046.

---

### 3. IndexRAG (arXiv 2603.16415)

**Existence: CONFIRMED.** The paper exists on arXiv at [2603.16415](https://arxiv.org/abs/2603.16415).

- **Title:** "IndexRAG: Bridging Facts for Cross-Document Reasoning at Index Time"
- **Authors:** Zhenghua Bao and Yi Shi
- **Date:** March 17, 2026

**Claim verification:**
- "Identifies bridge entities at index time" -- **CONFIRMED.** The method identifies shared entities across documents at index time and generates bridging facts as independently retrievable units.
- "+4.6 F1 over Naive RAG" -- **CONFIRMED.** The paper reports a 4.6-point F1 gain over Naive RAG on average across HotpotQA, 2WikiMultiHopQA, and MuSiQue.
- Additional detail: requires only single-pass retrieval and one LLM call at inference. When paired with IRCoT, outperforms graph-based baselines (HippoRAG, FastGraphRAG) using flat retrieval alone.

---

### 4. BRIEF-Pro (arXiv 2510.13799)

**Existence: CONFIRMED.** The paper exists on arXiv at [2510.13799](https://arxiv.org/abs/2510.13799).

- **Title:** "BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning"
- **Authors:** Jia-Chen Gu, Junyi Zhang, Di Wu, Yuankai Li, Kai-Wei Chang, Nanyun Peng
- **Date:** Originally submitted October 15, 2025 (v1); revised April 27, 2026 (v2)
- **Venue:** Confirmed as **ACL 2026 Findings** (listed on the [ACL 2026 Findings page](https://2026.aclweb.org/program/findings/) and the [UCLA bibliography](http://web.cs.ucla.edu/~kwchang/bibliography/gu2026briefpro/)).

**Claim verification:**
- "ACL 2026 Findings" -- **CONFIRMED.**
- "34x abstractive compression on HotpotQA with 49.0 EM / 63.1 F1 with 8B reader" -- **MOSTLY CONFIRMED with nuance.** The paper's "Auto" mode achieves approximately 32x compression on average across datasets, but the specific HotpotQA row with the 8B reader (Llama-3.1-8B-Instruct) does show **49.0 EM and 63.05 F1 at a 34x compression rate**. So the claimed numbers match the HotpotQA-specific row, though the 34x is the dataset-specific ratio rather than the overall average (which is 32x). The F1 of 63.1 is a very slight rounding of the actual 63.05.

---

## Summary

| Paper | Exists? | Claims Accurate? |
|-------|---------|-----------------|
| BridgeRAG | Yes | R@5 is 0.9875, not 0.99 (rounded up). Other claims confirmed. |
| CUE-R | Yes | All specific numbers (0.493, 0.205, 0.186) confirmed exactly. |
| IndexRAG | Yes | +4.6 F1 over Naive RAG confirmed. Bridge entities at index time confirmed. |
| BRIEF-Pro | Yes | ACL 2026 Findings confirmed. 49.0 EM / 63.05 F1 confirmed (63.1 is minor rounding). 34x is HotpotQA-specific, not the overall average. |

All four papers are real and verifiable on arXiv. The claims are substantively accurate with minor discrepancies: BridgeRAG's R@5 was rounded from 0.9875 to 0.99 (a small exaggeration), and BRIEF-Pro's F1 was rounded from 63.05 to 63.1 (trivial).

Sources:
- [BridgeRAG on arXiv](https://arxiv.org/abs/2604.03384)
- [CUE-R on arXiv](https://arxiv.org/abs/2604.05467)
- [IndexRAG on arXiv](https://arxiv.org/abs/2603.16415)
- [BRIEF-Pro on arXiv](https://arxiv.org/abs/2510.13799)
- [ACL 2026 Findings](https://2026.aclweb.org/program/findings/)
- [UCLA BRIEF-Pro bibliography](http://web.cs.ucla.edu/~kwchang/bibliography/gu2026briefpro/)
- [IndexRAG on HuggingFace Papers](https://huggingface.co/papers/2603.16415)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86c6df26-8cfe-4ab1-9ada-876bb448611d",
  "isSidechain": true,
  "agentId": "a93291f0432d9bb7c",
  "requestId": "req_011Cb2kJTtjgiHrgRT29QheG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "869db620-6789-467e-8357-cedf851784d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJyzoLncza8GV9hLFmAW27",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1211,
      "cache_read_input_tokens": 17695,
      "output_tokens": 1828,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1211
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1828,
          "cache_read_input_tokens": 17695,
          "cache_creation_input_tokens": 1211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1211,
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
