# Research conversation: I need to understand how XGrammar-2's API works for composability with custom LogitsProcessors in vLLM V1. Specifically:

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad5d0810279003740.jsonl`
- **Structured JSON:** [`365e6da06582ba8d234a.json`](../../sessions/36/365e6da06582ba8d234a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-12T00:51:59.530Z_

I need to understand how XGrammar-2's API works for composability with custom LogitsProcessors in vLLM V1. Specifically:

1. Search for "XGrammar-2" API documentation, GitHub repo, and the arXiv paper (arXiv Jan 2026, Li et al.). Look for:
   - How does XGrammar-2 expose its compiled grammar mask? Is there a mask_callback, get_mask, or similar API?
   - Can external code call XGrammar-2 to get the grammar-valid token mask for a given state, then intersect it with additional masks?
   - What is the TagDispatch mechanism?
   - What is the per-token speedup claimed (6-10×)?

2. Search for how vLLM V1 integrates grammar-constrained decoding:
   - Does vLLM V1 use XGrammar-2 or Outlines internally?
   - How does the LogitsProcessor API work in vLLM V1? Can multiple LogitsProcessors be composed?
   - Can a custom LogitsProcessor access the grammar engine's state?

3. Search for any papers or implementations that compose grammar constraints with additional semantic constraints in vLLM or similar serving frameworks.

Report detailed findings about the technical integration path.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "8dce0ca0-d21b-4dda-aa77-56ab6ddf57fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:51:59.537Z_

```json
{
  "parentUuid": "8dce0ca0-d21b-4dda-aa77-56ab6ddf57fc",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
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
  "uuid": "91aca18b-d90e-4bfc-b1a1-a725ac64dfdf",
  "timestamp": "2026-05-12T00:51:59.537Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:52:02.092Z_



I'll research XGrammar-2, vLLM V1's grammar integration, and composability of LogitsProcessors. Let me search across multiple sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91aca18b-d90e-4bfc-b1a1-a725ac64dfdf",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawkz4Z95ripdTYxb7Qe4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4184f15-13e8-414f-918a-360a2632889b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaV7ZRtbrhaYAZKTWu13jv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 829,
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

_source line 4 · 2026-05-12T00:52:02.684Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01M2nrnJTzD9RSU5BR8NBXSz`</summary>

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
  "parentUuid": "e4184f15-13e8-414f-918a-360a2632889b",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawkz4Z95ripdTYxb7Qe4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19056991-4312-4a6b-a0ae-1bc5ba17fef4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaV7ZRtbrhaYAZKTWu13jv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 7304,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 117,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 829,
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

_source line 5 · 2026-05-12T00:52:02.687Z_

<details><summary>↩ Tool result · `toolu_01M2nrnJTzD9RSU5BR8NBXSz`</summary>

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
  "parentUuid": "19056991-4312-4a6b-a0ae-1bc5ba17fef4",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "030fc60c-e361-48f7-897e-af6b69028c1e",
  "sourceToolAssistantUUID": "19056991-4312-4a6b-a0ae-1bc5ba17fef4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:52:06.185Z_



Let me search broadly across multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "030fc60c-e361-48f7-897e-af6b69028c1e",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011CawkzJzJLv8wBMyziBPZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dda3019-98e6-48dc-ba6a-2a2847d1b9a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016n9q49NS54xzeo3PLxZhwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1926,
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

_source line 7 · 2026-05-12T00:52:07.111Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013A65nu9cbUoFPmrHAmULjA`</summary>

```json
{
  "query": "XGrammar-2 API documentation grammar mask composability 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dda3019-98e6-48dc-ba6a-2a2847d1b9a9",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011CawkzJzJLv8wBMyziBPZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37b83cbe-e909-430f-aab8-f4c81d6c3d51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016n9q49NS54xzeo3PLxZhwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1926,
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

_source line 8 · 2026-05-12T00:52:08.225Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DGBc5CdgDu6BTrEBdoyxkT`</summary>

```json
{
  "query": "XGrammar-2 arXiv paper Li et al January 2026 TagDispatch"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37b83cbe-e909-430f-aab8-f4c81d6c3d51",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011CawkzJzJLv8wBMyziBPZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcad358d-a021-44ac-abec-1d14829cea1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016n9q49NS54xzeo3PLxZhwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1926,
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

_source line 9 · 2026-05-12T00:52:09.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F3V5NJrxpvNpMTEFjAKHSd`</summary>

```json
{
  "query": "vLLM V1 LogitsProcessor API grammar constrained decoding XGrammar 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcad358d-a021-44ac-abec-1d14829cea1c",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011CawkzJzJLv8wBMyziBPZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8ae60df-09fb-494f-9ca8-45751dadd566",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016n9q49NS54xzeo3PLxZhwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1926,
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

_source line 10 · 2026-05-12T00:52:09.103Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2mUSyyWeuZX8aSko4pXcQ`</summary>

```json
{
  "query": "XGrammar-2 GitHub repository mlc-ai"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8ae60df-09fb-494f-9ca8-45751dadd566",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011CawkzJzJLv8wBMyziBPZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22086bf3-339e-4cd3-9da1-533598551886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016n9q49NS54xzeo3PLxZhwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1926,
      "cache_read_input_tokens": 8133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1926,
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

_source line 11 · 2026-05-12T00:52:15.138Z_

<details><summary>↩ Tool result · `toolu_01DGBc5CdgDu6BTrEBdoyxkT`</summary>

```text
Web search results for query: "XGrammar-2 arXiv paper Li et al January 2026 TagDispatch"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2601.04426v1"},{"title":"[2601.04426] XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/abs/2601.04426"},{"title":"XGRAMMAR 2: DYNAMIC AND EFFICIENT STRUCTURED GENERATION ENGINE FOR AGENTIC LLMS","url":"https://www.arxiv.org/pdf/2601.04426"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.04426"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"Catalyst: XGrammar","url":"https://catalyst.cs.cmu.edu/projects/xgrammar.html"}]

I found the arXiv paper you're looking for. Here's the information about it:

**XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs**

XGrammar-2 is a structured generation engine for dynamic agentic workloads. The paper was submitted by Linzhang Li on January 7, 2026.

**Key Features:**

The paper introduces several innovations:

1. **TagDispatch**: XGrammar-2 introduces TagDispatch for dynamic structural dispatching and Cross-Grammar Cache for substructure-level cache reuse across grammars. TagDispatch is an EBNF-compatible grammar intrinsic for describing tag-triggered switching between free-form text and structured sub-grammars.

2. **Additional Optimizations**: It further improves efficiency with an Earley-based adaptive token mask cache, just-in-time compilation, and repetition state compression.

**Performance:**

XGrammar-2 achieves over 6x faster compilation than prior structured generation engines, and incurs near-zero end-to-end overhead in modern LLM serving systems.

The paper can be accessed at arXiv:2601.04426.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcad358d-a021-44ac-abec-1d14829cea1c",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "890129b7-d7ee-478b-b7e0-6d2be7c66be2",
  "sourceToolAssistantUUID": "dcad358d-a021-44ac-abec-1d14829cea1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:52:15.877Z_

<details><summary>↩ Tool result · `toolu_013A65nu9cbUoFPmrHAmULjA`</summary>

```text
Web search results for query: "XGrammar-2 API documentation grammar mask composability 2026"

Links: [{"title":"XGrammar Python API — XGrammar 0.1.30 documentation","url":"https://xgrammar.mlc.ai/docs/api/python/index.html"},{"title":"Workflow of XGrammar — XGrammar 0.1.31 documentation","url":"https://xgrammar.mlc.ai/docs/tutorials/workflow_of_xgrammar.html"},{"title":"MLC | XGrammar-2: Fast and Customizable Structured Generation for Tool Calling and Agents","url":"https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation"},{"title":"xgr.GrammarMatcher — XGrammar 0.1.27 documentation","url":"https://xgrammar.mlc.ai/docs/api/python/grammar_matcher.html"},{"title":"Advanced Topics of the Structural Tag — XGrammar 0.1.27 documentation","url":"https://xgrammar.mlc.ai/docs/tutorials/advanced_structural_tag.html"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"xgrammar.testing — XGrammar 0.1.20 documentation","url":"https://xgrammar.mlc.ai/docs/_modules/xgrammar/testing.html"},{"title":"xgr.Grammar — XGrammar 0.1.20 documentation","url":"https://xgrammar.mlc.ai/docs/api/python/grammar.html"},{"title":"Catalyst: XGrammar","url":"https://catalyst.cs.cmu.edu/projects/xgrammar.html"},{"title":"XGrammar 2: High-Performance Grammar Systems","url":"https://www.emergentmind.com/topics/xgrammar-2"}]

Based on my search results, I found substantial information about XGrammar-2 API documentation regarding grammar mask composability. Here are the key findings:

## XGrammar-2 Key Features

XGrammar-2 is a major upgrade of XGrammar built for agent applications. It introduces Structural Tag, a composable JSON protocol that uniformly expresses OpenAI harmony format, tool calling, reasoning channels, and any custom output structure, exposed directly through serving engines' API.

## Grammar Mask and Composability

Different grammar structures and different parts of the same grammar often share many common sub-structures. For example, different JSON schemas all share the same string field described by {"type": "string"}. These repeated structures can be fully reused during preprocessing. XGrammar-2 implements an automaton-based hierarchical hashing algorithm that automatically finds shared parts within and across grammars, maximizing reuse of grammar preprocessing.

## Mask Optimization Techniques

Mask computation for CFGs is expensive, but sub-grammars (e.g., "string", "number", common object patterns) are ubiquitous across many schemas. XGrammar 2 minimizes redundant computation by hashing minimized FSM representations of grammar fragments, thereby recognizing and reusing structurally identical subgraphs.

Multiple efficiency optimizations, such as cross-grammar caching, repetition-state compression, and batching and speculative decoding support, ensure fast processing and minimal overhead even for huge structures.

## Performance

XGrammar-2 delivers up to 80x efficiency gain compared to XGrammar, and achieves near-zero overhead in LLM serving scenarios.

The documentation emphasizes that XGrammar-2's mask composability features enable efficient reuse of grammar preprocessing across different structures, which is particularly valuable for complex agent applications with multiple tools and nested structures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37b83cbe-e909-430f-aab8-f4c81d6c3d51",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "f4efbe99-76be-4d49-86f6-f17b9990cc2f",
  "sourceToolAssistantUUID": "37b83cbe-e909-430f-aab8-f4c81d6c3d51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:52:16.545Z_

<details><summary>↩ Tool result · `toolu_01R2mUSyyWeuZX8aSko4pXcQ`</summary>

```text
Web search results for query: "XGrammar-2 GitHub repository mlc-ai"

Links: [{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"xgrammar/README.md at main · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/blob/main/README.md"},{"title":"Releases · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/releases"},{"title":"mlc-ai · GitHub","url":"https://github.com/mlc-ai"},{"title":"XGrammar | Home","url":"https://xgrammar.mlc.ai/"},{"title":"xgrammar/pyproject.toml at main · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/blob/main/pyproject.toml"},{"title":"MLC | XGrammar-2: Fast and Customizable Structured Generation for Tool Calling and Agents","url":"https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation"},{"title":"xgrammar.so file missing : crashes vLLM server · Issue #292 · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/issues/292"},{"title":"Release v0.1.32 · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/releases/tag/v0.1.32"},{"title":"[Bug] The xgrammar does not handle kimi-k2 tokenizer correctly with 'Ġ' replacement and causing the tool call parsing failure in sglang · Issue #483 · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/issues/483"}]

Based on the search results, here's what I found about XGrammar-2 in the mlc-ai GitHub repository:

## Overview

XGrammar-2 was released in May 2026, and it is a major upgrade of XGrammar built for agent applications.

## Key Features

XGrammar-2 introduces Structural Tag, a composable JSON protocol that uniformly expresses OpenAI harmony format, tool calling, reasoning channels, and any custom output structure, exposed directly through serving engines' API.

XGrammar-2 leverages TVM-FFI, an open ABI and FFI library for ML systems, to provide unified support across these platforms and expose a consistent cross-language interface.

## Integration & Adoption

XGrammar-2 has been integrated into mainstream LLM serving engines, including SGLang, vLLM, TensorRT-LLM, and MLC-LLM.

## Repository

The main XGrammar repository is located at **https://github.com/mlc-ai/xgrammar**, where XGrammar is an open-source library for efficient, flexible, and portable structured generation that leverages constrained decoding to ensure 100% structural correctness of the output.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22086bf3-339e-4cd3-9da1-533598551886",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "5cac839c-05e0-443b-b983-c5ad68ee2cd2",
  "sourceToolAssistantUUID": "22086bf3-339e-4cd3-9da1-533598551886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:52:18.055Z_

<details><summary>↩ Tool result · `toolu_01F3V5NJrxpvNpMTEFjAKHSd`</summary>

```text
Web search results for query: "vLLM V1 LogitsProcessor API grammar constrained decoding XGrammar 2026"

Links: [{"title":"Structured Decoding in vLLM: A Gentle Introduction","url":"https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction"},{"title":"Guided Decoding | vllm-project/vllm | DeepWiki","url":"https://deepwiki.com/vllm-project/vllm/6.1-guided-decoding"},{"title":"vllm.model_executor.guided_decoding.xgrammar_decoding - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/model_executor/guided_decoding/xgrammar_decoding.html"},{"title":"Structured Decoding in vLLM: a gentle introduction | vLLM Blog","url":"https://vllm.ai/blog/struct-decode-intro"},{"title":"Structured Decoding in vLLM: a gentle introduction | vLLM Blog","url":"https://blog.vllm.ai/2025/01/14/struct-decode-intro.html"},{"title":"Guided Decoding Performance on vLLM and SGLang - The official SqueezeBits Tech blog","url":"https://blog.squeezebits.com/guided-decoding-performance-vllm-sglang"},{"title":"[WIP] Xgrammar init in engine by mgoin · Pull Request #10835 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/10835"},{"title":"Custom Guided Decoding Backends with NVIDIA NIM for LLMs — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/latest/custom-decoding-backend.html"},{"title":"vLLM V1 User Guide — vLLM","url":"https://docs.vllm.ai/en/v0.8.1/getting_started/v1_user_guide.html"},{"title":"Structured Outputs — vLLM","url":"https://docs.vllm.ai/en/v0.8.2/features/structured_outputs.html"}]

Based on the search results, here's what I found about vLLM V1, LogitsProcessor API, grammar constrained decoding, and XGrammar:

## vLLM V1 and XGrammar Integration

The upcoming vLLM v1 release focuses on enhanced performance and schedule-level mask broadcasting for mixed-requests batch support.

## Grammar Constrained Decoding

Guided decoding is a feature in vLLM that enables structured output generation according to specific constraints, ensuring outputs follow defined patterns such as JSON schemas, regular expressions, or formal grammars.

## XGrammar Technology

XGrammar introduces a new technique that batch constrained decoding via pushdown automaton (PDA), which can be thought of as a "collection of FSMs, and each FSM represents a context-free grammar (CFG)".

In vLLM's v0 architecture, XGrammar has been implemented as a logit processor, optimizing it with caching for tokenizer data.

## LogitsProcessor API

Guided decoding integrates with the Sampler through the LogitsProcessor chain, where the guided decoding logits processor is called during the sampling process to modify the logits before sampling the next token to ensure the sampled token conforms to specified constraints.

## V1 Support Status

V1 currently supports only the xgrammar:no_fallback mode, meaning that it will error out if the output schema is unsupported by xgrammar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8ae60df-09fb-494f-9ca8-45751dadd566",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "8173617f-3387-4560-bedf-f2e4af6a7e40",
  "sourceToolAssistantUUID": "a8ae60df-09fb-494f-9ca8-45751dadd566",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T00:52:23.969Z_

Good, I have initial results. Let me now dig deeper into the specific technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8173617f-3387-4560-bedf-f2e4af6a7e40",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm1RjdXgSVB5Y4zuVoR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f71afb27-46f9-43c3-9496-878450ac6b9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQM3J1sM7dh5DsjqGgx4kW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 824,
      "cache_creation_input_tokens": 2968,
      "cache_read_input_tokens": 10059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2968,
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

_source line 16 · 2026-05-12T00:52:29.461Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GQ31nwdZt4XiJ6CkKZKH8u`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.04426v1",
  "prompt": "Extract all details about:\n1. TagDispatch mechanism - what it is, how it works technically, EBNF syntax\n2. The mask/bitmask API - how does XGrammar-2 expose grammar-valid token masks? Is there a get_mask, fill_next_token_bitmask, or mask_callback API?\n3. Cross-Grammar Cache mechanism\n4. Per-token speedup claims (6-10x or other numbers)\n5. Any mention of composability with external constraints or custom LogitsProcessors\n6. The GrammarMatcher API\n7. JIT compilation details\n8. Earley-based adaptive token mask cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f71afb27-46f9-43c3-9496-878450ac6b9e",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm1RjdXgSVB5Y4zuVoR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4eeea253-2478-4953-b51b-9e433d55af70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQM3J1sM7dh5DsjqGgx4kW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 824,
      "cache_creation_input_tokens": 2968,
      "cache_read_input_tokens": 10059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2968,
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

_source line 17 · 2026-05-12T00:52:31.888Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q31yxCnCkNX4QXsTHo8Mev`</summary>

```json
{
  "url": "https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation",
  "prompt": "Extract all technical details about:\n1. XGrammar-2 API for getting grammar masks\n2. TagDispatch mechanism\n3. Structural Tag protocol\n4. How to compose grammar constraints with other constraints\n5. Integration with vLLM and other serving engines\n6. Performance numbers and speedups\n7. Any code examples showing mask access or composability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eeea253-2478-4953-b51b-9e433d55af70",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm1RjdXgSVB5Y4zuVoR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37415705-e050-4770-860f-2b8b8a413978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQM3J1sM7dh5DsjqGgx4kW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 824,
      "cache_creation_input_tokens": 2968,
      "cache_read_input_tokens": 10059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2968,
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

_source line 18 · 2026-05-12T00:52:37.990Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018NvXhTHWSkA4eRiXNbxgxy`</summary>

```json
{
  "url": "https://xgrammar.mlc.ai/docs/api/python/grammar_matcher.html",
  "prompt": "Extract the full GrammarMatcher API documentation, especially:\n1. fill_next_token_bitmask method - parameters, return type, how it works\n2. Any method to get the current grammar state's valid token mask\n3. accept_token method\n4. reset method\n5. Any method related to composability or external mask access\n6. The full class signature and all public methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37415705-e050-4770-860f-2b8b8a413978",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm1RjdXgSVB5Y4zuVoR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42ff3308-de7a-4244-9820-feaa214ede15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQM3J1sM7dh5DsjqGgx4kW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 824,
      "cache_creation_input_tokens": 2968,
      "cache_read_input_tokens": 10059,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2968
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 824,
          "output_tokens": 571,
          "cache_read_input_tokens": 10059,
          "cache_creation_input_tokens": 2968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2968,
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

_source line 19 · 2026-05-12T00:52:39.450Z_

<details><summary>↩ Tool result · `toolu_01Q31yxCnCkNX4QXsTHo8Mev`</summary>

```text
# XGrammar-2 Technical Details

## 1. API for Grammar Masks

XGrammar-2 provides mask generation through its core API. The system features a **BatchGrammarMatcher** for efficient batch processing and a **GrammarMatcher** for individual requests. The documentation references these as key components for accessing constrained decoding masks.

## 2. TagDispatch Mechanism

The document does not mention a "TagDispatch" mechanism. This concept is not covered in the provided content.

## 3. Structural Tag Protocol

Structural Tag is "a JSON-based DSL that provides a unified, lightweight, and extensible way to describe" diverse output formats. It comprises five composable types:

- **Sequence**: Chains multiple parts together
- **Tag**: Matches begin marker, constrained content, and end marker
- **AnyText**: Allows arbitrary text until the enclosing tag ends
- **TriggeredTags**: Enables free text until a trigger string appears, then enforces structure
- **JSONSchema**: Constrains output to a given schema with format options like `"style": "deepseek_xml"`

## 4. Composing Grammar Constraints

The system achieves composability by treating "JSON Schema, regex, literal strings, and token IDs" as "first-class atomic types" that can be "nested and combined" to describe "arbitrarily complex output structures."

## 5. Integration with vLLM and Serving Engines

XGrammar-2 is "integrated into mainstream LLM serving engines, including SGLang, vLLM, TensorRT-LLM, and MLC-LLM." Users access Structural Tag through OpenAI-compatible APIs via the `response_format` field in requests.

## 6. Performance Numbers

- **Grammar compilation**: Up to 80× speedup compared to XGrammar
- **Repetition compression**: Reduces processing from 534ms to 5.37ms (100× improvement)
- **Overhead**: "Minimal latency overhead" in single-batch settings
- **Schema accuracy**: Achieves "100% schema accuracy"

## 7. Code Examples

The document shows one API example using OpenAI-compatible client calls with `extra_body` containing a custom Structural Tag format, but no direct mask-access code examples are provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37415705-e050-4770-860f-2b8b8a413978",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "cf816eeb-c69d-4d67-b4e5-c05584c4700d",
  "sourceToolAssistantUUID": "37415705-e050-4770-860f-2b8b8a413978",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T00:52:43.864Z_

<details><summary>↩ Tool result · `toolu_01GQ31nwdZt4XiJ6CkKZKH8u`</summary>

```text
# XGrammar 2: Technical Details Extraction

## 1. TagDispatch Mechanism

**What it is:** A dynamic grammar dispatching construct that enables runtime selection between multiple grammars based on detected tags in LLM output.

**How it works:**
- Operates in two modes: "dispatching" and "dispatched"
- Uses Aho–Corasick automaton to recognize predefined tags during dispatching mode
- Upon tag match, switches to dispatched mode where corresponding grammar constrains output
- Returns to dispatching mode when dispatched grammar completes or stop string detected

**Parameters:** Accepts "a list of tag-grammar pairs" and "a list of stop strings which are the exits of the TagDispatch"

**Technical details:** The system detects patterns like Llama 3.1's `&lt;function=` prefix or OpenAI's `<|channel|>analysis` tags, routing to specific constrained grammars for parameters or structured output.

No formal EBNF syntax is provided in the document.

## 2. Mask/Bitmask API

The document does not expose specific API signatures (get_mask, fill_next_token_bitmask, etc.). References mention storing results in "adaptive token mask cache" containing three categories: accepted tokens (𝒜), rejected tokens (ℛ), and context-dependent tokens (𝒰), but concrete method signatures aren't documented.

## 3. Cross-Grammar Cache Mechanism

**Core approach:** Detects identical sub-structures across different grammars to maximize token mask cache reuse.

**Implementation:**
- Represents grammar rules as finite-state machines (FSMs)
- Uses hierarchical hash algorithm with three stages: leaf FSMs, non-cyclic references, and simple cycles
- Implements "perfect cache hit" (identical FSM + lookahead) and "partial cache hit" (identical FSM, different lookahead)
- Algorithm 1 performs BFS-based consistent state numbering for stable hashing

**Adaptation mechanism:** "stores two versions in the cross-grammar cache pool: the cache determined solely by the FSM, and the full cache determined by both the FSM and the lookahead assertion"

## 4. Per-Token Speedup Claims

- **6x overall speedup:** "achieve more than 6x speedup over the existing structured generation engines"
- **7x end-to-end:** "compared to XGrammar, XGrammar 2 has about a 7x speedup over the end-to-end latency"
- **Per-token overhead:** XGrammar 2 achieves ~10 microseconds; llguidance shows 250+ microseconds
- **Compilation time:** XGrammar 2: ~10 milliseconds vs. XGrammar's 1000+ milliseconds
- **Gap to unconstrained:** "gap between the result of XGrammar 2 and the result without constraints is no more than 6%"

## 5. Composability with External Constraints

The document does not mention LogitsProcessors, custom constraints, or external composition APIs. Integration focuses on "SGLang and vLLM" inference engines rather than third-party constraint frameworks.

## 6. GrammarMatcher API

No GrammarMatcher API is mentioned or documented in this paper.

## 7. JIT Compilation Details

**Concept:** Amortizes compilation from startup to runtime, overlapping computation with inference phases.

**Partial JIT approach:** 
- Estimates preprocessing time per state
- Precomputes K most time-consuming token masks during LLM prefilling phase
- Generates remaining masks during decoding, overlapping with token generation
- Goal: "achieve zero-overhead token mask generation"

**Result (Table 1):** Reduces preprocessing from 4960ms (baseline) to 612ms with 8.1x reduction, though runtime overhead increases to 722.47 microseconds.

## 8. Earley-Based Adaptive Token Mask Cache

**Motivation:** Avoids worst-case exponential complexity of pushdown automaton approaches.

**Complexity improvements:**
- General case: O(n³)
- Unambiguous grammars: O(n²)
- Deterministic grammars: O(n)

**Caching strategy:** "only when the Earley-parser state is scannable (can immediately accept a character without predicting other rules), we will generate a token mask cache for it"

**Advantages:** "naturally support left recursion" and exploits common rule references for efficiency gains over PDA-based approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eeea253-2478-4953-b51b-9e433d55af70",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "ef0f87b8-c020-4cad-95e4-15664e7d0599",
  "sourceToolAssistantUUID": "4eeea253-2478-4953-b51b-9e433d55af70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T00:52:45.997Z_

<details><summary>↩ Tool result · `toolu_018NvXhTHWSkA4eRiXNbxgxy`</summary>

````text
# GrammarMatcher API Documentation

## Class Signature
```python
class GrammarMatcher(compiled_grammar, *, override_stop_tokens=None, 
                     terminate_without_stop_token=False, max_rollback_tokens=-1)
```

The core class for grammar-guided generation that maintains stateful matching of LLM output against specified grammar rules.

## Primary Methods for Token Mask Access

### `fill_next_token_bitmask(bitmask, index=0, *, debug_print=False)`
**Purpose:** Generate the constraint mask for next token prediction.

**Parameters:**
- `bitmask`: Int32 array-like object (CPU-resident) containing the token mask
- `index`: Batch position to fill (default: 0)
- `debug_print`: Enable internal state logging (default: False)

**Returns:** Boolean indicating whether masking is needed (optimization flag for all-true masks)

**Key detail:** "This method does not change the matcher state" — the mask is computed without advancing the matcher's parsing state.

### `accept_token(token_id, *, debug_print=False)`
**Purpose:** Consume a token and advance internal parsing state.

**Returns:** Boolean success flag

**Rejection conditions:** Token fails grammar validation, matcher already terminated, invalid token ID, or special token detected.

## State Management

### `reset()`
Restores the matcher to initial state, clearing all token history.

### `rollback(num_tokens=1)`
Reverts the matcher by specified token count. Described as "unlimited" in the current implementation.

### `is_terminated()` / `is_completed()`
- `is_terminated()`: Checks if stop token was accepted (or grammar fully matched if `terminate_without_stop_token=True`)
- `is_completed()`: Validates grammar completion without requiring stop token acceptance

## Composability

### `fork()`
Creates an independent copy sharing the compiled grammar but with deep-copied parsing state, enabling parallel exploration of multiple token paths.

## Batch Processing

### `BatchGrammarMatcher`
Multi-threaded variant for parallel mask generation:
- `batch_fill_next_token_bitmask(matchers, bitmask, indices=None)`
- `batch_accept_token(matchers, tokens)` [static]
- `batch_rollback(matchers, num_tokens)` [static]

## Properties

- `stop_token_ids`: List of terminal token IDs
- `max_rollback_tokens`: Now deprecated (always -1/unlimited)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42ff3308-de7a-4244-9820-feaa214ede15",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "fba7de0c-3d75-4bf7-85f2-a51e90d86c35",
  "sourceToolAssistantUUID": "42ff3308-de7a-4244-9820-feaa214ede15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T00:52:49.907Z_

Excellent. Now let me get deeper details on vLLM V1's LogitsProcessor API and composability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fba7de0c-3d75-4bf7-85f2-a51e90d86c35",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm3VW9xxhx86iuDtbk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "617059c0-b5dc-4e69-a63c-9ecc725442e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178AeFZdfCEHKjpzKZ7WhKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3761,
      "cache_read_input_tokens": 13027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3761,
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

_source line 23 · 2026-05-12T00:52:54.330Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KWjiRN8o64TJJCa9gRaifq`</summary>

```json
{
  "url": "https://deepwiki.com/vllm-project/vllm/6.1-guided-decoding",
  "prompt": "Extract all details about:\n1. How guided decoding works in vLLM V1 architecture\n2. LogitsProcessor chain - how are multiple processors composed?\n3. How XGrammar is integrated as a LogitsProcessor\n4. Can a custom LogitsProcessor access the grammar engine's state or mask?\n5. The architecture of the sampler and how it calls LogitsProcessors\n6. Any mention of composing grammar constraints with custom constraints\n7. V1 vs V0 differences in guided decoding architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "617059c0-b5dc-4e69-a63c-9ecc725442e3",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm3VW9xxhx86iuDtbk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d08c01b-0633-47ba-a541-6128827824b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178AeFZdfCEHKjpzKZ7WhKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3761,
      "cache_read_input_tokens": 13027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3761,
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

_source line 24 · 2026-05-12T00:52:56.628Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vsnt3KFL89G7MZCDi7Mrxk`</summary>

```json
{
  "url": "https://docs.vllm.ai/en/v0.8.2/features/structured_outputs.html",
  "prompt": "Extract details about:\n1. Structured output backends supported (XGrammar, Outlines, etc.)\n2. How to configure the guided decoding backend\n3. Any mention of LogitsProcessor composability\n4. API for custom LogitsProcessors\n5. V1 support status for structured outputs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d08c01b-0633-47ba-a541-6128827824b7",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm3VW9xxhx86iuDtbk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff259d29-e1f1-4b43-a53d-6ad7f8a596f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178AeFZdfCEHKjpzKZ7WhKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3761,
      "cache_read_input_tokens": 13027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3761,
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

_source line 25 · 2026-05-12T00:52:56.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BA39iSXrs5EFcYSHTNLSTM`</summary>

```json
{
  "query": "vLLM V1 custom LogitsProcessor compose multiple logits processors guided decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff259d29-e1f1-4b43-a53d-6ad7f8a596f1",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm3VW9xxhx86iuDtbk8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28a2aef4-cca9-402a-a46c-416b0b71efbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178AeFZdfCEHKjpzKZ7WhKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3761,
      "cache_read_input_tokens": 13027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3761,
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

### Tool result

_source line 26 · 2026-05-12T00:52:59.444Z_

<details><summary>↩ Tool result · `toolu_01KWjiRN8o64TJJCa9gRaifq`</summary>

```text
# Guided Decoding in vLLM: Not Covered in Provided Content

Based on the webpage content provided, I cannot extract details about guided decoding, LogitsProcessor chains, XGrammar integration, or sampler architecture. 

**Why:** The page documents the **OpenAI-Compatible API Server** (section 6.1), focusing on:
- HTTP server startup and routing
- Chat completion serving
- API protocol implementations (Anthropic, Speech-to-Text)
- Error handling and middleware

The content does not address:
1. Guided decoding mechanisms
2. LogitsProcessor composition or chaining
3. XGrammar or grammar engine integration
4. Custom constraint composition
5. Sampler architecture or token generation internals
6. V1 vs V0 differences in decoding systems

**Related sections that might contain this information** (based on the table of contents):
- Section 4.4: "Sampling and Token Generation"
- Section 4.5: "Speculative Decoding"
- Section 5.3: "Transformers Modeling Backend"

To answer your questions about guided decoding architecture, you would need content from those sections or documentation specifically covering the sampling and constraint systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d08c01b-0633-47ba-a541-6128827824b7",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "c6221d78-1d60-4fc0-a3b1-003e92902ce1",
  "sourceToolAssistantUUID": "2d08c01b-0633-47ba-a541-6128827824b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T00:53:05.150Z_

<details><summary>↩ Tool result · `toolu_01BA39iSXrs5EFcYSHTNLSTM`</summary>

```text
Web search results for query: "vLLM V1 custom LogitsProcessor compose multiple logits processors guided decoding"

Links: [{"title":"Custom Logits Processors - vLLM","url":"https://docs.vllm.ai/en/stable/features/custom_logitsprocs/"},{"title":"Logits Processors - vLLM","url":"https://docs.vllm.ai/en/latest/design/logits_processors/"},{"title":"[Feature]: Upgrade as many vLLM built-in logits processors to the new logits processors programming model as possible · Issue #25957 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/25957"},{"title":"Custom Logits Processing — NVIDIA NIM for Large Language Models","url":"https://docs.nvidia.com/nim/large-language-models/latest/advanced-use-cases/custom-logits.html"},{"title":"vllm/examples/features/logits_processor at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/tree/main/examples/features/logits_processor"},{"title":"How to use logits_processors · Issue #1728 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/1728"},{"title":"[RFC]: Logits processor extensibility · Issue #17799 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/17799"},{"title":"vllm/vllm/model_executor/layers/logits_processor.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/logits_processor.py"},{"title":"logits_processor - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/index.html"},{"title":"[Usage]: Logits processor with v1 · Issue #21672 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/21672"}]

Links: [{"title":"logits_processor - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/"},{"title":"[RFC]: Improve guided decoding (logit_processor) APIs and performance. · Issue #5423 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/5423"},{"title":"Custom Logits Processors - vLLM","url":"https://docs.vllm.ai/en/latest/examples/offline_inference/logits_processor/"},{"title":"Custom Guided Decoding Backend (Experimental) — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/1.7.0/custom-decoding-backend.html"},{"title":"Logits Processors - vLLM","url":"https://docs.vllm.ai/en/latest/design/logits_processors/"},{"title":"Custom Guided Decoding Backends with NVIDIA NIM for LLMs — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/latest/custom-decoding-backend.html"},{"title":"Guided Decoding | vllm-project/vllm | DeepWiki","url":"https://deepwiki.com/vllm-project/vllm/6.1-guided-decoding"},{"title":"vllm.model_executor.guided_decoding.guidance_decoding - vLLM","url":"https://docs.vllm.ai/en/v0.9.2/api/vllm/model_executor/guided_decoding/guidance_decoding.html"},{"title":"[V1][WIP] V1 supports LogitsProcessors by afeldman-nm · Pull Request #10905 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/10905"},{"title":"vllm/vllm/model_executor/guided_decoding/outlines_logits_processors.py at 80c751e7f68ade3d4c6391a0f3fce9ce970ddad0 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/80c751e7f68ade3d4c6391a0f3fce9ce970ddad0/vllm/model_executor/guided_decoding/outlines_logits_processors.py"}]

Based on the search results, here's what I found regarding vLLM V1 custom LogitsProcessor, composing multiple logits processors, and guided decoding:

## Custom LogitsProcessor in vLLM V1

Custom logits processors must subclass vllm.v1.sample.logits_processor.LogitsProcessor and define (at minimum) the following methods: validate_params(cls, sampling_params: SamplingParams), __init__(self, vllm_config: VllmConfig, device: torch.device, is_pin_memory: bool), is_argmax_invariant(), update_state(), and apply().

Custom logits processors can be passed to the LLM via a fully qualified class name (FQCN), or can be instantiated and passed directly.

## Composing Multiple Logits Processors

The search results indicate that vLLM provides a LogitsProcessors class that encapsulates initialized logitsproc objects. Multiple logits processors can be passed as a list to the LLM constructor through the logits_processors parameter.

## Guided Decoding with LogitsProcessors

Guided decoding is a feature in vLLM that enables structured output generation according to specific constraints, ensuring outputs follow defined patterns such as JSON schemas, regular expressions, or formal grammars.

All guided decoding backends implement the LogitsProcessor interface, which modifies the logits (token scores) during generation, and guided decoding integrates with the Sampler through the LogitsProcessor chain.

Logits processors allow you to modify the model's output distribution before sampling, enabling controlled generation behaviors like token masking, constrained decoding, and custom sampling strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28a2aef4-cca9-402a-a46c-416b0b71efbf",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "cda75ad4-04df-4b5b-a377-a05655e71826",
  "sourceToolAssistantUUID": "28a2aef4-cca9-402a-a46c-416b0b71efbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T00:53:06.115Z_

<details><summary>↩ Tool result · `toolu_01Vsnt3KFL89G7MZCDi7Mrxk`</summary>

```text
# Structured Outputs in vLLM: Key Details

## 1. Supported Backends

vLLM supports three guided decoding backends for structured outputs:
- **Outlines**
- **LM-Format-Enforcer**
- **XGrammar**

The documentation states: "vLLM supports the generation of structured outputs using outlines, lm-format-enforcer, or xgrammar as backends for the guided decoding."

## 2. Configuring the Guided Decoding Backend

The `guided_decoding_backend` parameter selects which backend to use. Backend-specific options follow a colon separator format. For example: `"xgrammar:no-fallback"` prevents fallback to alternative backends on error.

In offline inference, the backend is configured via the `GuidedDecodingParams` class's `backend` parameter within `SamplingParams`.

## 3. LogitsProcessor Composability

The provided documentation does **not mention** LogitsProcessor composability or custom composition strategies.

## 4. Custom LogitsProcessor API

The document contains **no information** about APIs for creating custom LogitsProcessors.

## 5. V1 Support Status

The documentation provides **no explicit statement** regarding V1 support status for structured outputs. The examples shown use current vLLM APIs without version-specific caveats.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff259d29-e1f1-4b43-a53d-6ad7f8a596f1",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "4edac51e-2625-43bf-a6ef-006132614b27",
  "sourceToolAssistantUUID": "ff259d29-e1f1-4b43-a53d-6ad7f8a596f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-12T00:53:09.357Z_

Let me now fetch the critical vLLM V1 LogitsProcessor design docs and the RFC for composability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4edac51e-2625-43bf-a6ef-006132614b27",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm4yD4Tj1n3FCwFpJ3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56aca88c-7fb5-48b5-859e-2a28c4b05f2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qH4ZWqX5Nu9xmyuH6KuBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1647,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 16788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1071,
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

_source line 30 · 2026-05-12T00:53:13.278Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XBaRoXgBzNZ9XgsFcLc8AR`</summary>

```json
{
  "url": "https://docs.vllm.ai/en/latest/design/logits_processors/",
  "prompt": "Extract ALL technical details about:\n1. The LogitsProcessor programming model in vLLM V1\n2. Required methods: validate_params, __init__, is_argmax_invariant, update_state, apply\n3. How multiple LogitsProcessors are composed/chained\n4. How guided decoding integrates as a LogitsProcessor\n5. Can a custom LogitsProcessor see the mask from the guided decoding LogitsProcessor?\n6. The lifecycle of LogitsProcessors\n7. Any mention of composing grammar constraints with custom constraints\n8. The LogitsProcessors container class\n9. How masks are applied - is it additive, multiplicative, or bitmask intersection?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56aca88c-7fb5-48b5-859e-2a28c4b05f2f",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm4yD4Tj1n3FCwFpJ3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "664678a4-2565-4c21-8e40-56d416f99ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qH4ZWqX5Nu9xmyuH6KuBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1647,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 16788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1071,
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

_source line 31 · 2026-05-12T00:53:16.160Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TbcyAHTW4UkMSEM8oxosL2`</summary>

```json
{
  "url": "https://docs.vllm.ai/en/stable/features/custom_logitsprocs/",
  "prompt": "Extract ALL technical details about:\n1. How to create a custom LogitsProcessor in vLLM V1\n2. The class interface and required methods\n3. How custom LogitsProcessors interact with guided decoding\n4. Can you compose grammar constraints with custom constraints?\n5. Code examples showing LogitsProcessor implementation\n6. How masks from different processors are combined\n7. Any mention of accessing the grammar engine state from a custom processor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "664678a4-2565-4c21-8e40-56d416f99ad6",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm4yD4Tj1n3FCwFpJ3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0860222-f011-40b3-891b-0bbdae5327d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qH4ZWqX5Nu9xmyuH6KuBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1647,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 16788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1071,
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

_source line 32 · 2026-05-12T00:53:17.851Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SNBNaUtQuw6sHgv3HNJYqJ`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/issues/17799",
  "prompt": "Extract ALL details about:\n1. The RFC for logits processor extensibility\n2. What composability features are proposed or implemented\n3. Can custom LogitsProcessors compose with guided decoding?\n4. Any discussion about accessing grammar masks from custom processors\n5. The current limitations and proposed solutions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0860222-f011-40b3-891b-0bbdae5327d0",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm4yD4Tj1n3FCwFpJ3v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76debab7-d76d-4b4f-a49a-648ba2b8a71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qH4ZWqX5Nu9xmyuH6KuBZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1647,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 16788,
      "output_tokens": 569,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1071
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1647,
          "output_tokens": 569,
          "cache_read_input_tokens": 16788,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1071,
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

_source line 33 · 2026-05-12T00:53:23.818Z_

<details><summary>↩ Tool result · `toolu_01XBaRoXgBzNZ9XgsFcLc8AR`</summary>

```text
# LogitsProcessor Programming Model in vLLM V1

## Core Programming Model

The LogitsProcessor abstraction operates at **batch granularity**, consuming a `(num_requests) x (vocab_size)` logits tensor and applying transformations per-request while "leaving other rows unmodified."

## Required Methods

**`__init__(vllm_config, device, is_pin_memory)`**
- Initializes processor with engine configuration, hardware device, and memory pinning availability

**`apply(logits: torch.Tensor) -> torch.Tensor`**
- Transforms logits tensor, either in-place or out-of-place (in-place preferred for memory efficiency)
- Returns modified logits of same shape

**`is_argmax_invariant() -> bool`**
- Returns `True` if processor never changes the highest-logit token ID for any request
- Enables optimization: argmax-invariant processors skip execution when all requests use greedy sampling
- Evaluated once at startup; implementation may be hardcoded or programmatic

**`update_state(batch_update: BatchUpdate | None) -> None`**
- Called before each forward pass to sync processor state with persistent batch changes
- Processes updates in strict order: removes, adds, moves
- Must discard information about finished requests

**`validate_params(sampling_params: SamplingParams)`**
- Class method validating sampling parameters
- Raises `ValueError` for invalid arguments before request acceptance

## Composition and Chaining

Multiple processors are applied **sequentially in order**, with distinctions based on argmax invariance:

1. Non-argmax-invariant processors execute first
2. Sampling occurs
3. Argmax-invariant processors execute (skipped if batch uses only greedy sampling)

The document provides pseudocode showing: "for processor in (sampling_metadata.logitsprocs.non_argmax_invariant): logits = processor.apply(logits)"

## BatchUpdate Data Structure

Processors receive immutable dataclass containing:
- `batch_size`: current request count
- `removed`: indices of eliminated requests
- `added`: tuples of (index, SamplingParams, prompt_tokens_ref, output_tokens_ref)
- `moved`: tuples of (source_index, dest_index, directionality_enum)

**Critical detail:** output token ID lists are passed by reference, allowing processors to observe token generation across steps.

## Guided Decoding Integration

**Not addressed in provided document.** No technical details about guided decoding as a LogitsProcessor implementation, custom processor visibility into guidance masks, or grammar constraint composition appear in the source material.

## LogitsProcessor Lifecycle

1. Engine loads processors at startup
2. Each engine step: update_state() called to reorganize processor state matching persistent batch
3. Model inference generates logits
4. Sampler applies processors sequentially
5. Softmax applied to transformed logits

Persistent batch maintains "list of loaded logits processors" with state synchronized via `refresh_metadata()`.

## Mask Application Mechanism

**Not specified in document.** No technical details about mask combination strategies (additive, multiplicative, intersection) are provided.

## LogitsProcessors Container

Referenced as `sampling_metadata.logitsprocs` with attributes:
- `.non_argmax_invariant` (list)
- `.argmax_invariant` (list)

Container organization enables selective execution based on sampling mode.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "664678a4-2565-4c21-8e40-56d416f99ad6",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "51039532-e66f-4acf-8c06-abb23ef85b76",
  "sourceToolAssistantUUID": "664678a4-2565-4c21-8e40-56d416f99ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T00:53:23.895Z_

<details><summary>↩ Tool result · `toolu_01TbcyAHTW4UkMSEM8oxosL2`</summary>

````text
# Technical Details: Custom LogitsProcessor in vLLM V1

## 1. Creating a Custom LogitsProcessor

Custom logits processors must subclass `vllm.v1.sample.logits_processor.LogitsProcessor`. The framework operates at batch granularity, processing a `(num_requests) x (vocab_size)` logits tensor during each engine step.

## 2. Required Class Interface and Methods

**Essential methods to implement:**

- **`validate_params(cls, sampling_params: SamplingParams)`**: Validates sampling parameters, raising `ValueError` for invalid arguments before request processing.

- **`__init__(self, vllm_config: VllmConfig, device: torch.device, is_pin_memory: bool)`**: Initializes the processor with engine configuration and hardware details.

- **`apply(self, logits: torch.Tensor) -> torch.Tensor`**: "Consume a `(num_requests) x (vocab_size)` logits tensor" and return the modified version. In-place modifications are more memory-efficient.

- **`is_argmax_invariant(self) -> bool`**: Returns `True` if the processor never changes which token has the highest logit value, enabling optimization skips during greedy sampling.

- **`update_state(self, batch_update: Optional[BatchUpdate]) -> None`**: Handles persistent batch state changes including request additions, removals, and reordering. Must process operations in this order: removes, adds, then moves.

## 3. Interaction with Guided Decoding

**The document contains no information about interactions between custom LogitsProcessors and guided decoding or grammar constraints.** No such integration details are provided.

## 4. Grammar Constraint Composition

**No details are provided** regarding composing grammar constraints with custom constraints or combining multiple constraint sources.

## 5. Implementation Code Example

The documentation provides `DummyLogitsProcessor`, which masks all logits except a target token:

```python
def apply(self, logits: torch.Tensor) -> torch.Tensor:
    if not self.req_info:
        return logits
    
    cols = torch.tensor(list(self.req_info.values()), 
                       dtype=torch.long, device=logits.device)
    rows = torch.tensor(list(self.req_info.keys()), 
                       dtype=torch.long, device=logits.device)
    values_to_keep = logits[rows, cols].clone()
    
    logits[rows] = float('-inf')
    logits[rows, cols] = values_to_keep
    return logits
```

## 6. Mask Combination Across Processors

**The document provides no information about how masks or modifications from different processors are combined** when multiple custom processors are loaded simultaneously.

## 7. Accessing Grammar Engine State

**No details are provided** regarding accessing grammar engine state or the internal state of other processors from a custom LogitsProcessor implementation.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0860222-f011-40b3-891b-0bbdae5327d0",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "51b5e964-a967-44b5-8e2b-c42ea05461c5",
  "sourceToolAssistantUUID": "d0860222-f011-40b3-891b-0bbdae5327d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-12T00:53:25.403Z_

<details><summary>↩ Tool result · `toolu_01SNBNaUtQuw6sHgv3HNJYqJ`</summary>

````text
# vLLM V1 Logits Processor Extensibility RFC Analysis

## 1. RFC Overview

This RFC (#17799) proposes enabling custom logits processor support in vLLM's V1 engine. The motivation stems from user requests to extend beyond hard-coded processors like min-p sampling, with reference to external libraries such as NVIDIA's logits-processor-zoo.

## 2. Proposed Composability Features

The RFC establishes three ways to specify logits processors:

**Server mode CLI:**
```
--logits-processors '[qualname, {qualname, args, kwargs}]'
```

**Python API (LLM/AsyncLLM):**
- Logits processor subclasses directly
- Qualified name strings
- `LogitsProcessorConstructor` instances with optional positional and keyword arguments

The design allows multiple processors to coexist, passed to `InputBatch` during initialization.

## 3. Custom Processors and Guided Decoding

**The document does not address composition between custom logits processors and guided decoding mechanisms.** No discussion exists regarding how these systems might interact or coordinate.

## 4. Grammar Mask Access

**There is no mention of grammar masks or mechanisms for custom processors to access constraint information.** The RFC focuses solely on instantiation and parameter passing, not inter-processor data sharing.

## 5. Limitations and Solutions

**Current limitations:**
- V1 lacks extensible logits processor support (only hard-coded processors available)
- Third-party libraries remain incompatible with V1's programming model

**Proposed solutions:**
- "Users instantiating the engine directly in Python are responsible for security concerns"
- No whitelist pattern needed (unlike V0) since explicit CLI specification provides implicit security
- Runtime processor behavior controlled via `SamplingParams.extra_args`
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76debab7-d76d-4b4f-a49a-648ba2b8a71c",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "48b6701d-f4f5-493a-a744-01a599d3132a",
  "sourceToolAssistantUUID": "76debab7-d76d-4b4f-a49a-648ba2b8a71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-12T00:53:30.643Z_

Good. Now let me search for the specific issue about composing grammar constraints with custom constraints, and look at the XGrammar Python API for mask access.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48b6701d-f4f5-493a-a744-01a599d3132a",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm6RB3AXqw91KUQ8dq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b089a5c-1fc1-4c10-a525-e2d5f616c59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLGY43ugDy1UFQTVmEQhWQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4187,
      "cache_read_input_tokens": 17859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4187,
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

_source line 37 · 2026-05-12T00:53:32.046Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EsNMtZE67qygZcjobr7xHX`</summary>

```json
{
  "query": "compose grammar constrained decoding semantic constraints LogitsProcessor vLLM intersection mask 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b089a5c-1fc1-4c10-a525-e2d5f616c59b",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm6RB3AXqw91KUQ8dq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75d67943-58be-42ff-a9c3-bdcf7bd32c09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLGY43ugDy1UFQTVmEQhWQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4187,
      "cache_read_input_tokens": 17859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4187,
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

_source line 38 · 2026-05-12T00:53:34.802Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014k8McduPDnSUTAxLgGE7mq`</summary>

```json
{
  "url": "https://xgrammar.mlc.ai/docs/api/python/index.html",
  "prompt": "Extract the full Python API reference for XGrammar, especially:\n1. All classes and their methods\n2. GrammarMatcher and fill_next_token_bitmask\n3. CompiledGrammar\n4. GrammarCompiler\n5. Any method for getting token masks\n6. Any composability or mask intersection utilities\n7. BatchGrammarMatcher\n8. allocate_token_bitmask function"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75d67943-58be-42ff-a9c3-bdcf7bd32c09",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm6RB3AXqw91KUQ8dq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c197dc76-242f-424f-bf31-118d1fdedf07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLGY43ugDy1UFQTVmEQhWQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4187,
      "cache_read_input_tokens": 17859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4187,
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

_source line 39 · 2026-05-12T00:53:38.452Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HFpmSGHJ4vJgGWTFrDGhs8`</summary>

```json
{
  "url": "https://xgrammar.mlc.ai/docs/tutorials/workflow_of_xgrammar.html",
  "prompt": "Extract the complete workflow showing:\n1. How to compile a grammar\n2. How to create a GrammarMatcher\n3. How to call fill_next_token_bitmask to get the token mask\n4. How to apply the bitmask to logits\n5. How to accept tokens and advance state\n6. Code examples showing the full loop\n7. The apply_token_bitmask_inplace function\n8. Any mention of composing masks with external constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c197dc76-242f-424f-bf31-118d1fdedf07",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm6RB3AXqw91KUQ8dq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee1028ca-848f-4b17-8156-f2c669d3b15f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLGY43ugDy1UFQTVmEQhWQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4187,
      "cache_read_input_tokens": 17859,
      "output_tokens": 456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4187
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 456,
          "cache_read_input_tokens": 17859,
          "cache_creation_input_tokens": 4187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4187,
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

_source line 40 · 2026-05-12T00:53:39.970Z_

<details><summary>↩ Tool result · `toolu_01EsNMtZE67qygZcjobr7xHX`</summary>

```text
Web search results for query: "compose grammar constrained decoding semantic constraints LogitsProcessor vLLM intersection mask 2025 2026"

Links: [{"title":"Structured Decoding in vLLM: A Gentle Introduction","url":"https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction"},{"title":"Structured Decoding in vLLM: a gentle introduction | vLLM Blog","url":"https://blog.vllm.ai/2025/01/14/struct-decode-intro.html"},{"title":"Custom Logits Processors - vLLM","url":"https://docs.vllm.ai/en/latest/examples/offline_inference/logits_processor/"},{"title":"Guided Decoding | vllm-project/vllm | DeepWiki","url":"https://deepwiki.com/vllm-project/vllm/6.1-guided-decoding"},{"title":"Guided Decoding Performance on vLLM and SGLang - The official SqueezeBits Tech blog","url":"https://blog.squeezebits.com/guided-decoding-performance-vllm-sglang"},{"title":"Custom Guided Decoding Backend (Experimental) — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/1.7.0/custom-decoding-backend.html"},{"title":"Mastering the Logits: A Guide to Constrained Decoding in Hugging Face and vLLM | by Celal Savur | Medium","url":"https://medium.com/@c.savur/mastering-the-logits-a-guide-to-constrained-decoding-in-hugging-face-and-vllm-357a5c1b9a28"},{"title":"Custom Guided Decoding Backends with NVIDIA NIM for LLMs — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/latest/custom-decoding-backend.html"},{"title":"Guided Decoding and Structured Output | z0306c/vllm | DeepWiki","url":"https://deepwiki.com/z0306c/vllm/7.2-guided-decoding-and-structured-output"},{"title":"Structured outputs in vLLM: Guiding AI responses | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/06/03/structured-outputs-vllm-guiding-ai-responses"}]

Based on the web search results, here's what I found related to your query about grammar-constrained decoding, semantic constraints, LogitsProcessor, and vLLM:

## Overview of Constrained Decoding in vLLM

Logits processors allow you to modify the model's output distribution before sampling, enabling controlled generation behaviors like token masking, constrained decoding, and custom sampling strategies.

## Grammar Compilation and Masks

The guided decoding workflow uses a grammar created from a JSON schema to generate token masks at each step to constrain the LLM's output, restricting the model's next-token choices to only those that are grammatically valid given the context so far.

XGrammar is implemented as a logit processor in vLLM's v0 architecture, optimized with caching for tokenizer data.

## Intersection Masking Approach

Structured output constrains generation by masking invalid tokens, ensuring only tokens that comply with the defined constraints remain candidates for sampling, happening dynamically on a per-token basis.

## Recent Developments (2025-2026)

vLLM's upcoming v1 release focuses on enhanced performance and schedule-level mask broadcasting for mixed-requests batch support.

Structured output support in vLLM V1 is dramatically faster than in V0, where even a single constrained request could degrade system-wide performance, while V1 introduces minimal overhead thanks to back-end optimizations and smarter architecture.

The search results show active development in this area, with multiple approaches (XGrammar, Guidance, Outlines) implementing constrained decoding through LogitsProcessor modifications and mask-based token filtering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75d67943-58be-42ff-a9c3-bdcf7bd32c09",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "702d2a0e-2f11-4514-bdb9-733f0e01fb8b",
  "sourceToolAssistantUUID": "75d67943-58be-42ff-a9c3-bdcf7bd32c09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-12T00:53:40.765Z_

<details><summary>↩ Tool result · `toolu_014k8McduPDnSUTAxLgGE7mq`</summary>

```text
# XGrammar Python API Reference Summary

Based on the documentation index provided, here's what's available:

## Core Classes

The API includes several primary classes for grammar handling:

- **Grammar**: Base grammar definition class
- **GrammarCompiler**: Compiles grammar definitions into usable formats
- **CompiledGrammar**: Output from compilation, ready for matching operations
- **GrammarMatcher**: Performs token matching against compiled grammars
- **BatchGrammarMatcher**: Handles multiple grammar matching operations simultaneously
- **TokenizerInfo**: Manages tokenizer vocabulary and types

## Token Masking Operations

The "Bitmask Operations" section documents utilities for token constraint handling:

- `allocate_token_bitmask()`: Creates bitmask structures for token constraints
- `apply_token_bitmask_inplace()`: Applies constraints directly to existing masks
- `reset_token_bitmask()`: Clears or reinitializes token masks
- `get_bitmask_shape()`: Returns dimensions of bitmask structures
- `bitmask_dtype`: Specifies the data type for bitmask operations

## Testing & Utilities

The `xgr.testing` module provides conversion and inspection methods, including functions for schema conversion and "mask extraction from bitmask structures."

## Limitations

The provided documentation is an index page only. Specific method signatures, parameters, and detailed documentation for `fill_next_token_bitmask` or composability utilities are not included in this excerpt. You'll need to access the individual class documentation pages for complete API details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c197dc76-242f-424f-bf31-118d1fdedf07",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "6284ef5a-d07f-4e10-b396-444e97a64138",
  "sourceToolAssistantUUID": "c197dc76-242f-424f-bf31-118d1fdedf07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T00:53:43.547Z_

<details><summary>↩ Tool result · `toolu_01HFpmSGHJ4vJgGWTFrDGhs8`</summary>

````text
# XGrammar Workflow: Complete Process

## 1. Grammar Compilation

Create a `GrammarCompiler` bound to tokenizer info, then compile your grammar:

```python
grammar_compiler = xgr.GrammarCompiler(tokenizer_info)
compiled_grammar = grammar_compiler.compile_grammar(grammar)
```

The compiler performs preprocessing including "simplify the grammar and build automata" and computes "an adaptive token mask cache."

## 2. GrammarMatcher Creation

Initialize the matcher with your compiled grammar:

```python
grammar_matcher = xgr.GrammarMatcher(compiled_grammar)
```

## 3. Token Bitmask Generation

Call `fill_next_token_bitmask()` to generate valid token constraints:

```python
bitmask = xgr.allocate_token_bitmask(batch_size, tokenizer_info.vocab_size)
grammar_matcher.fill_next_token_bitmask(bitmask)
```

The bitmask is a "bool tensor with the same shape as the vocabulary size," compressed into int32 format.

## 4. Apply Bitmask to Logits

Restrict model outputs using the generated mask:

```python
xgr.apply_token_bitmask_inplace(logits, bitmask.to(logits.device))
```

This modifies logits in-place on the same device.

## 5. Token Acceptance

After sampling, advance the matcher state:

```python
grammar_matcher.accept_token(next_token_id)
```

## 6. Complete Generation Loop

```python
while not grammar_matcher.is_terminated():
    logits = model(torch.tensor([input_ids])).logits
    grammar_matcher.fill_next_token_bitmask(token_bitmask)
    xgr.apply_token_bitmask_inplace(logits[0, -1, :], token_bitmask.to(logits.device))
    prob = torch.softmax(logits[0, -1, :], dim=-1)
    next_token_id = torch.argmax(prob, dim=-1)
    grammar_matcher.accept_token(next_token_id.item())
    input_ids.append(next_token_id.item())
```

**Note:** External mask composition isn't mentioned in the provided content.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee1028ca-848f-4b17-8156-f2c669d3b15f",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "f581f5d7-6f68-44ef-b833-07488ef2feb7",
  "sourceToolAssistantUUID": "ee1028ca-848f-4b17-8156-f2c669d3b15f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-12T00:53:49.029Z_

Now let me get the final pieces: vLLM's XGrammar integration code, and any research on composing constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f581f5d7-6f68-44ef-b833-07488ef2feb7",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm7jFzmjjSwWpYFy6SS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95062956-38e8-4746-ba77-6e0a7c8290b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQUB3ujkGvVCadUmuxeTPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2590,
      "cache_read_input_tokens": 22046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2590,
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

_source line 44 · 2026-05-12T00:53:52.802Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G1JyosYhCcjXDkk3yzzgLC`</summary>

```json
{
  "url": "https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/index.html",
  "prompt": "Extract the complete API reference for vLLM V1's logits_processor module:\n1. The LogitsProcessor base class and its methods\n2. How guided decoding is implemented as a LogitsProcessor\n3. How multiple processors are chained\n4. Any mention of accessing grammar state or masks from other processors\n5. The full class hierarchy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95062956-38e8-4746-ba77-6e0a7c8290b4",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm7jFzmjjSwWpYFy6SS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6e6d75d-ae7c-459e-8011-e4e787ba467b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQUB3ujkGvVCadUmuxeTPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2590,
      "cache_read_input_tokens": 22046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2590,
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

_source line 45 · 2026-05-12T00:53:55.052Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CRA6AGXiYsZgW2KEBjhzdd`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/issues/21672",
  "prompt": "Extract all details about:\n1. What issues exist with logits processors in vLLM V1\n2. Can custom logits processors work alongside guided decoding?\n3. Any workarounds for composing grammar constraints with custom constraints\n4. The current status and any resolution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6e6d75d-ae7c-459e-8011-e4e787ba467b",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm7jFzmjjSwWpYFy6SS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc6f44ad-d641-4022-beab-ec6f2965556f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQUB3ujkGvVCadUmuxeTPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2590,
      "cache_read_input_tokens": 22046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2590,
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

_source line 46 · 2026-05-12T00:53:55.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Tm5ZgiJGG32VMFjqvmGnC`</summary>

```json
{
  "query": "composing grammar constraints semantic constraints structured generation LLM serving paper 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc6f44ad-d641-4022-beab-ec6f2965556f",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm7jFzmjjSwWpYFy6SS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63ad3c85-52f6-45e5-b1ba-0696ed1f87aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQUB3ujkGvVCadUmuxeTPe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2590,
      "cache_read_input_tokens": 22046,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2590
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 389,
          "cache_read_input_tokens": 22046,
          "cache_creation_input_tokens": 2590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2590,
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

_source line 47 · 2026-05-12T00:54:01.121Z_

<details><summary>↩ Tool result · `toolu_01CRA6AGXiYsZgW2KEBjhzdd`</summary>

```text
# vLLM V1 Logits Processor Issue Summary

## Issues with Logits Processors in vLLM V1

The primary issue is **lack of documentation**. The user states: "I can't find an example on how to use the new logits processor class for vllm v1."

The user seeks to implement custom token filtering similar to:
- Setting logits to `-np.inf` for disallowed tokens
- Restricting output to specific token IDs
- Achieving behavior comparable to Hugging Face's `prefix_allowed_tokens_fn`

## Guided Decoding Comparison

The issue mentions performance discrepancies between vLLM's guided decoding and Hugging Face Transformers' prefix filtering approach. An edit reveals: "The bad performance with vllm 0.9.2 was caused by a bug in the on board transformers version."

## Workarounds and Composition

The webpage content **does not address**:
- Whether custom processors work alongside guided decoding
- Specific workarounds for composing grammar constraints with custom constraints
- Technical integration patterns

## Current Status

**Issue Status**: Closed as not planned, marked with "stale" label (>90 days inactive)

**Resolution**: No solution provided in this thread. The user's subsequent discovery of a transformer library bug may have resolved their original problem, but implementation guidance for V1 logits processors remains undocumented in this issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc6f44ad-d641-4022-beab-ec6f2965556f",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "c50bf277-45cb-4d62-9636-ab7d9f1c29a1",
  "sourceToolAssistantUUID": "dc6f44ad-d641-4022-beab-ec6f2965556f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T00:54:03.618Z_

<details><summary>↩ Tool result · `toolu_01G1JyosYhCcjXDkk3yzzgLC`</summary>

```text
# vLLM V1 Logits Processor API Reference

## Base Class Architecture

The `LogitsProcessor` abstract base class defines the core interface with four essential abstract methods:

1. **`apply(logits: Tensor) -> Tensor`** — "Apply LogitsProcessor to batch logits tensor. The updated tensor must be returned but may be modified in-place."

2. **`is_argmax_invariant() -> bool`** — Indicates whether the processor impacts argmax computation in greedy sampling. This property may vary across instances of the same subclass.

3. **`update_state(batch_update: BatchUpdate | None) -> None`** — Called before each forward pass when output tokens are generated or batch composition changes.

4. **`validate_params(sampling_params: SamplingParams)`** — Class method for validating sampling parameters; raises ValueError for invalid configurations.

## Implementation Pattern: AdapterLogitsProcessor

The framework provides `AdapterLogitsProcessor` as a wrapper for per-request processors. Subclasses must implement:

- **`new_req_logits_processor(params: SamplingParams)`** — Returns a `RequestLogitsProcessor` instance or None if inapplicable to the request
- **`is_argmax_invariant()`** — Declares impact on greedy sampling

The adapter maintains a `req_info` dictionary mapping request indices to `partial[torch.Tensor]` objects, enabling efficient per-request processing.

## Built-in Processor: LogitBiasLogitsProcessor

This processor demonstrates practical implementation by applying token-level bias adjustments. It returns `False` for `is_argmax_invariant()` since "logit bias can rebalance token probabilities and change the outcome of argmax in greedy sampling."

## Batch State Management

The `BatchUpdateBuilder` class tracks persistent batch changes through:
- **`removed`** — Requests removed (sorted descending)
- **`added`** — New requests with output token lists
- **`moved`** — Requests repositioned within the batch

The `BatchUpdate` dataclass encapsulates these changes for processor consumption.

## Multi-Processor Chaining

The `LogitsProcessors` class (referenced in the module) encapsulates multiple initialized processors. The documentation indicates that processors are applied in sequence, though specific chaining logic isn't fully detailed in the provided excerpt.

## Guided Decoding Integration

**Not explicitly documented** in this reference excerpt. Grammar state or mask access from other processors appears to require examining the `builtin` submodule implementation directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6e6d75d-ae7c-459e-8011-e4e787ba467b",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "8d39a886-61a8-4cb9-8a47-a6e6e7e620da",
  "sourceToolAssistantUUID": "a6e6d75d-ae7c-459e-8011-e4e787ba467b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-12T00:54:05.754Z_

<details><summary>↩ Tool result · `toolu_014Tm5ZgiJGG32VMFjqvmGnC`</summary>

```text
Web search results for query: "composing grammar constraints semantic constraints structured generation LLM serving paper 2025 2026"

Links: [{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"Grammar Prompting for Domain-Specific Language ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/cd40d0d65bfebb894ccc9ea822b47fa8-Paper-Conference.pdf"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/html/2305.13971v6"},{"title":"Grammar-Constrained Natural Language Generation","url":"https://aclanthology.org/2025.findings-acl.177.pdf"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v3"}]

Based on my search results, I found several relevant papers on composing grammar constraints, semantic constraints, and structured generation for LLM serving:

## Key Papers (2024-2025)

### 1. **XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models**
XGrammar is a flexible and efficient structure generation engine for large language models that accelerates context-free grammar execution by dividing the vocabulary into context-independent tokens that can be prechecked and context-dependent tokens that need to be interpreted during runtime. The system achieves up to 100x speedup over existing solutions and can generate near-zero overhead structure generation in end-to-end LLM serving. (Published November 2024, updated May 2025)

### 2. **CRANE: Reasoning with Constrained LLM Generation**
CRANE effectively alternates between unconstrained generation for reasoning and constrained generation for producing structurally correct outputs, which can be applied to diverse open-source LLMs, various grammars, and different constrained decoding algorithms. The approach imposes grammar constraints judiciously to avoid restricting the LLM's reasoning capabilities, for example applying constrained decoding only after the reasoning process is complete. (Published February 2025)

### 3. **Grammar-Aligned Decoding**
Grammar-Constrained Decoding (GCD) techniques generate outputs that are grammatical but unlikely according to the LLM, while Grammar-Aligned Decoding (GAD) better respects the LLM while still enforcing the constraints. (NeurIPS 2024)

### 4. **Grammar Prompting for Domain-Specific Language Generation**
Grammar prompting enables LLMs to perform competitively on diverse DSL generation tasks, including semantic parsing, Overnight, GeoQuery, PDDL planning, and molecule generation (SMILES).

These papers address the challenge of composing both grammar constraints (for syntactic validity) and semantic constraints in structured generation for efficient LLM serving.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63ad3c85-52f6-45e5-b1ba-0696ed1f87aa",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "0fc4a2f5-de29-4d39-85e6-18174ad6cee5",
  "sourceToolAssistantUUID": "63ad3c85-52f6-45e5-b1ba-0696ed1f87aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-12T00:54:10.566Z_

Let me get one more critical piece -- the vLLM V1 guided decoding source code and the XGrammar-2 Structural Tag details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fc4a2f5-de29-4d39-85e6-18174ad6cee5",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm9NBY9VoVfQkNCXSpL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b0956d5-e95a-4950-b74e-8ff506ce9a71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzwNZPCvZPSfqadgANUT7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2417,
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

_source line 51 · 2026-05-12T00:54:13.454Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CSJCNzbvCorJS7Q6BaSD3z`</summary>

```json
{
  "url": "https://docs.vllm.ai/en/latest/api/vllm/model_executor/guided_decoding/xgrammar_decoding.html",
  "prompt": "Extract all details about how vLLM integrates XGrammar for guided decoding:\n1. The XGrammarLogitsProcessor class\n2. How it wraps XGrammar's GrammarMatcher\n3. How it generates and applies masks\n4. Is the mask accessible from outside?\n5. The full class interface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b0956d5-e95a-4950-b74e-8ff506ce9a71",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm9NBY9VoVfQkNCXSpL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "adb111a3-af54-43ae-ba04-0e5ea68162be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzwNZPCvZPSfqadgANUT7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2417,
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

_source line 52 · 2026-05-12T00:54:16.339Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FMLJ458rJEDiNrC1naVyYH`</summary>

```json
{
  "url": "https://xgrammar.mlc.ai/docs/tutorials/advanced_structural_tag.html",
  "prompt": "Extract all details about:\n1. Structural Tag and its JSON protocol\n2. TagDispatch - how it works with EBNF\n3. TriggeredTags vs Tag\n4. How to compose multiple grammars\n5. Code examples\n6. How this relates to mask composability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adb111a3-af54-43ae-ba04-0e5ea68162be",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm9NBY9VoVfQkNCXSpL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8589225a-d3fb-4f26-a84a-5c5e3cbb540c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzwNZPCvZPSfqadgANUT7i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 24636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2417,
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

### Tool result

_source line 53 · 2026-05-12T00:54:16.517Z_

<details><summary>↩ Tool result · reported error · `toolu_01FMLJ458rJEDiNrC1naVyYH`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8589225a-d3fb-4f26-a84a-5c5e3cbb540c",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "7c0eb3f6-9372-41ce-9a16-5e9c4098f1c5",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "8589225a-d3fb-4f26-a84a-5c5e3cbb540c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-12T00:54:16.683Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BF1sYgZdWaxDdHxwoDHe8v`</summary>

```json
{
  "query": "vLLM V1 guided decoding LogitsProcessor source code xgrammar_decoding.py GuidedDecodingLogitsProcessor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c0eb3f6-9372-41ce-9a16-5e9c4098f1c5",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011Cawm9NBY9VoVfQkNCXSpL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6efe7e11-c8d1-409b-b840-352f781474c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzwNZPCvZPSfqadgANUT7i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2417,
      "cache_read_input_tokens": 24636,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 24636,
          "cache_creation_input_tokens": 2417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2417,
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

_source line 55 · 2026-05-12T00:54:18.311Z_

<details><summary>↩ Tool result · `toolu_01CSJCNzbvCorJS7Q6BaSD3z`</summary>

```text
# XGrammar Integration in vLLM - Information Not Available

Based on the web page content provided, I cannot extract the requested details about XGrammar integration because **the page does not contain any information about XGrammar, the XGrammarLogitsProcessor class, or related guided decoding mechanisms**.

The content shows:
- Navigation structure for vLLM's API documentation
- Configuration classes (ModelConfig, CacheConfig, etc.)
- Offline inference and engine interfaces
- Multimodal support documentation
- Model development resources

**To find XGrammar integration details, you would need to:**
1. Access the actual implementation files in vLLM's source code
2. Check the "Logits Processors" design document (referenced in the navigation as `../design/logits_processors/`)
3. Review the vLLM GitHub repository directly
4. Consult the vLLM documentation pages beyond this API reference summary

The page provided is primarily a navigation index and summary rather than detailed API implementation documentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adb111a3-af54-43ae-ba04-0e5ea68162be",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "c174e5f5-d342-4a50-99bd-e7f9ce6d756d",
  "sourceToolAssistantUUID": "adb111a3-af54-43ae-ba04-0e5ea68162be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-12T00:54:27.126Z_

<details><summary>↩ Tool result · `toolu_01BF1sYgZdWaxDdHxwoDHe8v`</summary>

```text
Web search results for query: "vLLM V1 guided decoding LogitsProcessor source code xgrammar_decoding.py GuidedDecodingLogitsProcessor"

Links: [{"title":"vllm/vllm/model_executor/guided_decoding/xgrammar_decoding.py at main · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/guided_decoding/xgrammar_decoding.py"},{"title":"Guided Decoding | vllm-project/vllm | DeepWiki","url":"https://deepwiki.com/vllm-project/vllm/6.1-guided-decoding"},{"title":"Structured Decoding in vLLM: A Gentle Introduction","url":"https://www.bentoml.com/blog/structured-decoding-in-vllm-a-gentle-introduction"},{"title":"Custom Guided Decoding Backends with NVIDIA NIM for LLMs — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/latest/custom-decoding-backend.html"},{"title":"vllm.model_executor.guided_decoding.xgrammar_decoding - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/model_executor/guided_decoding/xgrammar_decoding.html"},{"title":"[RFC]: Improve guided decoding (logit_processor) APIs and performance. · Issue #5423 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/5423"},{"title":"vllm.model_executor.guided_decoding - vLLM","url":"https://docs.vllm.ai/en/latest/api/vllm/model_executor/guided_decoding/index.html"},{"title":"Custom Guided Decoding Backend (Experimental) — NVIDIA NIM for Large Language Models (LLMs)","url":"https://docs.nvidia.com/nim/large-language-models/1.7.0/custom-decoding-backend.html"},{"title":"[V1][WIP] V1 supports LogitsProcessors by afeldman-nm · Pull Request #10905 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/pull/10905"},{"title":"Custom Logits Processors - vLLM","url":"https://docs.vllm.ai/en/latest/examples/offline_inference/logits_processor/"}]

I found relevant information about vLLM V1 guided decoding and the LogitsProcessor implementation. Here's what I discovered:

## Search Results Summary

The main source file is located at `vllm/model_executor/guided_decoding/xgrammar_decoding.py`, which contains the `get_local_xgrammar_guided_decoding_logits_processor` function.

The XGrammarLogitsProcessor implements guided decoding using the xgrammar library, which compiles grammar constraints into efficient finite state machines (FSMs).

### Key Components in xgrammar_decoding.py

The file contains several important classes and methods including `__init__`, `choice_as_grammar`, `from_guided_params`, and `tokenizer_info` functions. There's also an immutable container for cached tokenizer data with an `encoded_vocab` field.

### Integration with Sampling

The guided decoding logits processor is called during the sampling process to modify the logits before sampling the next token, ensuring that the sampled token conforms to the specified constraints.

### V1 Support

Recent work has added v1 logits processor support towards enabling v1 guided decoding, with the v1 model runner passing sampling_metadata to model.compute_logits(). V1 also introduces a new logits processor interface in `vllm.v1.sample.logits_processor`.

You can access the official source code directly at the GitHub link: https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/guided_decoding/xgrammar_decoding.py


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6efe7e11-c8d1-409b-b840-352f781474c2",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "9e5c9fb2-9deb-4b79-ba73-c576065a2982",
  "sourceToolAssistantUUID": "6efe7e11-c8d1-409b-b840-352f781474c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-12T00:54:33.547Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GVnoqMoHeAQrMCHqgU8787`</summary>

```json
{
  "url": "https://github.com/vllm-project/vllm/issues/25957",
  "prompt": "Extract details about:\n1. Which built-in logits processors are being upgraded to the new V1 programming model\n2. Is guided decoding / XGrammar being upgraded to the V1 LogitsProcessor model?\n3. How does guided decoding currently work in V1 - is it a separate path or a LogitsProcessor?\n4. Any mention of composability between guided decoding and custom processors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e5c9fb2-9deb-4b79-ba73-c576065a2982",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011CawmAwY2G7Bzbf2sbwCzT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5297f2db-910e-4881-96c9-5fe9baca99fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjbrjmbeRTZGapCSAZCQq5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1784,
      "cache_read_input_tokens": 27053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1784,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-12T00:54:35.883Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PZzugnqWPSFV7x1mBKEYs6`</summary>

```json
{
  "url": "https://vllm.ai/blog/struct-decode-intro",
  "prompt": "Extract details about:\n1. How structured decoding works in vLLM V1 vs V0 architecture\n2. The mask computation and application pipeline\n3. How XGrammar is integrated\n4. Whether multiple constraint sources can be composed\n5. Performance characteristics of V1 structured decoding\n6. Any mention of composing grammar masks with custom masks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5297f2db-910e-4881-96c9-5fe9baca99fe",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011CawmAwY2G7Bzbf2sbwCzT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8be4cb75-92bc-448e-96b2-5998e4a122b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjbrjmbeRTZGapCSAZCQq5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1784,
      "cache_read_input_tokens": 27053,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 323,
          "cache_read_input_tokens": 27053,
          "cache_creation_input_tokens": 1784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1784,
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

_source line 59 · 2026-05-12T00:54:37.958Z_

<details><summary>↩ Tool result · `toolu_01GVnoqMoHeAQrMCHqgU8787`</summary>

```text
# vLLM Logits Processor V1 Migration Analysis

Based on the GitHub issue content provided:

## 1. Built-in Logits Processors Upgraded to V1 Model

Only **three** processors have been converted to the new `LogitsProcessor` subclass model:
- Min-P
- Logits bias
- Min tokens

The remaining processors remain "hard-coded into the engine core."

## 2. Guided Decoding / XGrammar Status

**No mention** of guided decoding or XGrammar appears in this issue content.

## 3. Guided Decoding V1 Implementation

The provided document contains **no information** about how guided decoding currently functions in V1 or whether it uses a separate implementation path.

## 4. Composability Between Systems

**Not addressed** in this issue. The discussion focuses on migrating hard-coded processors (allowed token IDs, bad words, repetition/frequency/presence penalties, temperature, top-K, top-P) to the new architecture once issue #25389 resolves outstanding programming model questions.

**Note:** The issue was closed as "not planned," suggesting this migration effort may have been deprioritized or superseded by other development decisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5297f2db-910e-4881-96c9-5fe9baca99fe",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "f55c8e63-b554-4abe-8148-786f5371cfe4",
  "sourceToolAssistantUUID": "5297f2db-910e-4881-96c9-5fe9baca99fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-12T00:54:43.418Z_

<details><summary>↩ Tool result · `toolu_01PZzugnqWPSFV7x1mBKEYs6`</summary>

```text
# Structured Decoding in vLLM: V0 vs V1 Architecture

## V0 Architecture (Current)

**Implementation**: XGrammar operates as a logit processor with tokenizer data caching. The system applies logit masks to constrain token selection at each decoding step.

**Mask Computation**: Masks are calculated synchronously within the sampling process, creating a critical path bottleneck where "all requests in any given batches will get blocked."

## V1 Architecture (Tentative Plans)

**Key Shift**: Moving guided decoding to the scheduler level, which would "shouldn't block other requests within the batch" and place it "outside of the critical path."

**Mask Broadcasting**: The proposal involves "bit-mask calculation in one process instead of each GPU workers" with broadcast to GPU workers, aiming to reduce redundant computation.

## XGrammar Integration Details

XGrammar uses pushdown automaton (PDA) technology, described as "a collection of FSMs, and each FSM represents a context-free grammar (CFG)," enabling multiple state transitions per step rather than single-token transitions.

**Performance**: Testing shows up to 5x improvement in time per output token under load compared to Outlines backend.

## Composition and Multiple Constraints

The document contains **no information** about composing multiple constraint sources or combining grammar masks with custom masks. The article doesn't address constraint composition mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be4cb75-92bc-448e-96b2-5998e4a122b1",
  "isSidechain": true,
  "promptId": "ed9eb134-201e-4c2d-b5f4-871595a6bb6b",
  "agentId": "ad5d0810279003740",
  "type": "user",
  "uuid": "5b5bee5d-8252-4fce-857a-b4d8eb0cb561",
  "sourceToolAssistantUUID": "8be4cb75-92bc-448e-96b2-5998e4a122b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-12T00:56:13.792Z_

Now I have comprehensive information. Let me compile the detailed findings.

---

## Detailed Findings: XGrammar-2 API, vLLM V1 Integration, and Composability

### 1. XGrammar-2 Core Architecture and API

**Paper**: [XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs (arXiv:2601.04426)](https://arxiv.org/abs/2601.04426) by Linzhang Li et al., January 2026.

**Repository**: [github.com/mlc-ai/xgrammar](https://github.com/mlc-ai/xgrammar) (latest release v0.1.32 as of May 2026).

#### How XGrammar-2 Exposes the Grammar Mask

XGrammar-2 uses the same core mask API as XGrammar v1, centered on `GrammarMatcher.fill_next_token_bitmask()`. The workflow is:

```python
import xgrammar as xgr

# 1. Compile grammar
compiler = xgr.GrammarCompiler(tokenizer_info)
compiled_grammar = compiler.compile_grammar(grammar)

# 2. Create matcher
matcher = xgr.GrammarMatcher(compiled_grammar)

# 3. Allocate bitmask (int32-packed bool tensor)
bitmask = xgr.allocate_token_bitmask(batch_size, tokenizer_info.vocab_size)

# 4. Fill the bitmask with grammar-valid tokens for current state
needs_masking = matcher.fill_next_token_bitmask(bitmask, index=0)
# Returns bool: False if all tokens are valid (optimization flag)

# 5. Apply to logits
xgr.apply_token_bitmask_inplace(logits, bitmask.to(logits.device))

# 6. After sampling, advance state
matcher.accept_token(token_id)
```

Key details about the mask API:
- **`fill_next_token_bitmask(bitmask, index=0)`** -- Fills a pre-allocated int32 bitmask tensor. Does NOT change matcher state (read-only query). The bitmask is CPU-resident.
- **`apply_token_bitmask_inplace(logits, bitmask)`** -- Sets logits to `-inf` for tokens where the bitmask is 0.
- **`allocate_token_bitmask(batch_size, vocab_size)`** -- Creates the int32 bitmask tensor.
- There is no `mask_callback` or `get_mask` returning a tensor directly. The pattern is always "allocate bitmask, fill it, apply it."

**External code CAN call XGrammar-2 to get the mask and then intersect it**: Since `fill_next_token_bitmask` writes to a user-owned tensor and does not modify matcher state, you can read the bitmask, perform bitwise AND with your own constraint mask, and then apply the combined mask to logits. This is the fundamental composability seam.

#### TagDispatch Mechanism

TagDispatch is an EBNF-compatible grammar intrinsic for dynamic structural dispatching. It works as follows:

- Operates in two modes: **dispatching** (free-form text) and **dispatched** (grammar-constrained).
- In dispatching mode, an **Aho-Corasick automaton** scans the LLM output for predefined tag strings (e.g., `&lt;function=`, `<|channel|>analysis`).
- Upon tag match, it switches to dispatched mode where the corresponding sub-grammar constrains output.
- When the dispatched grammar completes (or a stop string is detected), it returns to dispatching mode.
- Accepts a list of (tag, grammar) pairs and a list of stop strings.

This is used internally for Structural Tag -- a JSON-based DSL with five composable types: **Sequence**, **Tag**, **AnyText**, **TriggeredTags**, and **JSONSchema**. The Structural Tag protocol is how users express tool calling formats, reasoning channels, and custom output structures through the serving engine's API.

#### Performance Claims

- **6x overall speedup** over prior structured generation engines (llguidance, Outlines).
- **7x end-to-end latency improvement** over XGrammar v1.
- **80x grammar compilation speedup** over XGrammar v1 (with Cross-Grammar Cache and JIT).
- **Per-token mask overhead**: ~10 microseconds (vs. 250+ microseconds for llguidance).
- **Compilation time**: ~10 ms (vs. 1000+ ms for XGrammar v1).
- **End-to-end serving overhead**: gap to unconstrained generation is no more than 6%.

The "6-10x" range you mentioned aligns with the 6x-7x figures reported for different benchmarks. The 80x figure is for compilation, not per-token.

#### Cross-Grammar Cache

XGrammar-2 represents grammar rules as FSMs and uses a hierarchical hashing algorithm (BFS-based consistent state numbering) to detect structurally identical sub-grammars across different schemas. It stores two cache versions: one keyed by FSM alone (partial hit) and one by FSM + lookahead assertion (perfect hit). This enables massive reuse when serving many requests with different but structurally overlapping schemas.

#### Earley-Based Adaptive Token Mask Cache

XGrammar-2 replaces the PDA-based approach from v1 with an Earley parser, avoiding worst-case exponential complexity. Only "scannable" Earley states (those that can immediately accept a character) get token mask cache entries. Complexity: O(n) for deterministic grammars, O(n^2) for unambiguous, O(n^3) general case.

---

### 2. vLLM V1 Integration of Grammar-Constrained Decoding

#### Which Backend Does vLLM V1 Use?

vLLM V1 uses **XGrammar as its primary backend**. As of v0.8.x, V1 supports only `xgrammar:no_fallback` mode -- it errors out if the schema is unsupported by XGrammar (no fallback to Outlines). The V0 engine supported XGrammar, Outlines, and LM-Format-Enforcer.

#### V1 Architecture for Guided Decoding

In V0, XGrammar ran as a logit processor **synchronously in the sampling critical path**, blocking all requests in the batch. The V1 plan (partially implemented) moves guided decoding to the **scheduler level**, outside the critical path:
- Bitmask computation happens in a separate process, not per-GPU-worker.
- Masks are broadcast to GPU workers.
- This prevents constrained requests from degrading unconstrained request performance.

As of the latest code, guided decoding in V1 is **not yet fully migrated to the new `LogitsProcessor` programming model**. Only three built-in processors (min-p, logit bias, min tokens) have been converted. Guided decoding appears to remain on a separate code path.

#### vLLM V1 LogitsProcessor Programming Model

The V1 LogitsProcessor is a **batch-level abstraction** operating on `(num_requests) x (vocab_size)` tensors. Required methods:

- **`validate_params(cls, sampling_params)`** -- class method, validates params at request admission time.
- **`__init__(self, vllm_config, device, is_pin_memory)`** -- initialization with engine config.
- **`apply(self, logits: Tensor) -> Tensor`** -- the core transform. Modifies logits in-place or returns a new tensor.
- **`is_argmax_invariant(self) -> bool`** -- if True, processor is skipped when all requests use greedy sampling (optimization).
- **`update_state(self, batch_update: BatchUpdate | None)`** -- called before each forward pass to sync with persistent batch changes (removes, adds, moves). Receives output token lists **by reference**, so processors can observe generated tokens.

Execution order: non-argmax-invariant processors run first, then sampling, then argmax-invariant processors.

Custom processors are specified via fully qualified class names (FQCN) on the CLI (`--logits-processors`) or passed directly in Python.

#### Can Multiple LogitsProcessors Be Composed?

**Yes.** Multiple processors are applied **sequentially** to the logits tensor. Each processor modifies the logits and passes the result to the next. They are stored in `sampling_metadata.logitsprocs` with two lists: `.non_argmax_invariant` and `.argmax_invariant`. The composition model is **sequential application** (each processor sees the logits as modified by previous processors), not explicit mask intersection.

#### Can a Custom LogitsProcessor Access the Grammar Engine's State?

**Not through any official API.** The V1 LogitsProcessor interface provides no mechanism for one processor to access another processor's internal state. Guided decoding's mask computation is on a separate code path from the extensible LogitsProcessor chain. There is no inter-processor data sharing facility.

---

### 3. The Composability Integration Path

Given the above, here are the viable approaches for composing grammar constraints with additional semantic constraints:

#### Approach A: Direct XGrammar API (Recommended for Custom Engines)

If you control the inference loop (not using vLLM's built-in serving), you can directly compose masks:

```python
# Get grammar mask
grammar_matcher.fill_next_token_bitmask(grammar_bitmask)

# Create your semantic constraint mask (same int32-packed format)
semantic_bitmask = compute_my_semantic_constraints(state)

# Intersect via bitwise AND
combined_bitmask = grammar_bitmask & semantic_bitmask

# Apply combined mask
xgr.apply_token_bitmask_inplace(logits, combined_bitmask)
```

This is fully supported by XGrammar-2's API since `fill_next_token_bitmask` is a pure read operation on the matcher state.

#### Approach B: Custom vLLM V1 LogitsProcessor (For vLLM Serving)

Since V1 processors are applied sequentially to the same logits tensor:

1. Guided decoding (XGrammar) runs first and sets invalid tokens to `-inf`.
2. Your custom `LogitsProcessor.apply()` runs next and can set additional tokens to `-inf`.

The composition is **implicit via sequential `-inf` masking** -- if either the grammar or your semantic constraint rejects a token, it stays at `-inf`. This is effectively set intersection without explicit bitmask access.

**Limitation**: Your custom processor cannot see *which* tokens the grammar engine allowed (it only sees logits, some already at `-inf`). If your semantic constraint needs to know the grammar-valid set specifically (not just the surviving logits), you would need to reconstruct this from the logits tensor (tokens not at `-inf`).

**Current caveat**: As of vLLM V1, guided decoding may not yet be fully on the LogitsProcessor chain, so sequencing with custom processors requires verification against the specific vLLM version.

#### Approach C: Wrap XGrammar Inside a Custom LogitsProcessor

Build a single custom `LogitsProcessor` that internally manages both an XGrammar `GrammarMatcher` and your semantic constraint logic:

```python
class ComposedConstraintProcessor(LogitsProcessor):
    def apply(self, logits):
        # Get grammar mask from internal XGrammar matcher
        self.matcher.fill_next_token_bitmask(self.bitmask)
        xgr.apply_token_bitmask_inplace(logits, self.bitmask)
        
        # Apply additional semantic constraints
        for idx, req in self.req_info.items():
            semantic_mask = self.compute_semantic_mask(req)
            logits[idx][~semantic_mask] = float('-inf')
        
        return logits
    
    def update_state(self, batch_update):
        # Sync both grammar matcher state and semantic state
        ...
```

This gives full control but means bypassing vLLM's built-in guided decoding entirely.

#### Related Work: CRANE (arXiv:2502.09061)

The [CRANE paper](https://arxiv.org/pdf/2502.09061) (February 2025) addresses a related problem: it alternates between unconstrained generation (for reasoning) and constrained generation (for structured output), imposing grammar constraints only after reasoning is complete. This is a temporal composition rather than per-token mask intersection, but is relevant to the general problem of composing grammar and semantic constraints.

---

### Summary of Key Gaps

1. **No official composability API in XGrammar-2**: While `fill_next_token_bitmask` technically enables external mask intersection, there is no dedicated `compose_with()` or `intersect_mask()` method. Composition must be done manually via bitwise operations on the bitmask tensor.

2. **vLLM V1 guided decoding is not yet a standard LogitsProcessor**: It runs on a separate code path, so composing it with custom LogitsProcessors requires careful version-specific investigation. The V1 LogitsProcessor RFC ([#17799](https://github.com/vllm-project/vllm/issues/17799)) does not address guided decoding composition.

3. **No inter-processor state sharing in vLLM V1**: Processors cannot query each other's state. Sequential application on the logits tensor is the only composition mechanism.

Sources:
- [XGrammar-2 arXiv Paper (2601.04426)](https://arxiv.org/abs/2601.04426)
- [XGrammar-2 Blog Post](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)
- [XGrammar Python API - GrammarMatcher](https://xgrammar.mlc.ai/docs/api/python/grammar_matcher.html)
- [XGrammar Workflow Tutorial](https://xgrammar.mlc.ai/docs/tutorials/workflow_of_xgrammar.html)
- [XGrammar GitHub Repository](https://github.com/mlc-ai/xgrammar)
- [vLLM V1 LogitsProcessor Design Doc](https://docs.vllm.ai/en/latest/design/logits_processors/)
- [vLLM Custom LogitsProcessors](https://docs.vllm.ai/en/stable/features/custom_logitsprocs/)
- [vLLM LogitsProcessor Extensibility RFC (#17799)](https://github.com/vllm-project/vllm/issues/17799)
- [vLLM V1 LogitsProcessor API Reference](https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/index.html)
- [vLLM Structured Decoding Blog Post](https://vllm.ai/blog/struct-decode-intro)
- [vLLM Structured Outputs Docs](https://docs.vllm.ai/en/v0.8.2/features/structured_outputs.html)
- [CRANE: Reasoning with Constrained LLM Generation](https://arxiv.org/pdf/2502.09061)
- [Upgrade Built-in LogitsProcessors Issue (#25957)](https://github.com/vllm-project/vllm/issues/25957)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b5bee5d-8252-4fce-857a-b4d8eb0cb561",
  "isSidechain": true,
  "agentId": "ad5d0810279003740",
  "requestId": "req_011CawmC9FzTpfP3urDfncum",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a5fb705-b431-4ac5-9728-4f2185fdcb77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "75e0b45d-e75d-44ab-9d00-5147ced3238c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9eEgUpGvsxHXEfDCyRQVz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1081,
      "cache_read_input_tokens": 28837,
      "output_tokens": 3768,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1081
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3768,
          "cache_read_input_tokens": 28837,
          "cache_creation_input_tokens": 1081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1081,
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
