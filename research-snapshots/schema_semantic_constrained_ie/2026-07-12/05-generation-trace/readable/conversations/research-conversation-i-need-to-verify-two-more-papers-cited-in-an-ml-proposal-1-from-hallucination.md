# Research conversation: I need to verify two more papers cited in an ML proposal: 1. **"From Hallucination to Structure Snowballing: The Alignme

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a02c99b6bc249deff.jsonl`
- **Structured JSON:** [`a59092209b9b4f9f201d.json`](../../sessions/a5/a59092209b9b4f9f201d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-12T00:04:29.051Z_

I need to verify two more papers cited in an ML proposal:

1. **"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection"** — claimed arXiv Apr 2026. The proposal says it "documents cascading formatting errors under strict structural constraints in Qwen3-8B." Search for this paper on arXiv. Does it exist? Is the characterization accurate?

2. **"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs"** — claimed arXiv Mar 2026. The proposal says it demonstrates a "projection tax" from constrained decoding and achieves +24pp gains on GSM8K. Search for this paper. Does it exist? Is it accurately characterized?

3. Also search for: "CRANE constrained decoding reasoning ICML 2025 Banerjee" — the proposal claims CRANE proved that constrained decoding limits LLMs to TC⁰ complexity. Verify this.

Use WebSearch for each. Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "agentId": "a02c99b6bc249deff",
  "type": "user",
  "uuid": "69a2a88f-2607-4aba-b9c0-e5364108d1ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:04:29.054Z_

```json
{
  "parentUuid": "69a2a88f-2607-4aba-b9c0-e5364108d1ff",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
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
  "uuid": "96c8d269-3913-433d-bb92-f416c552faca",
  "timestamp": "2026-05-12T00:04:29.054Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:04:30.969Z_



I'll search for all three papers in parallel using WebSearch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96c8d269-3913-433d-bb92-f416c552faca",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhMwW8DcdkAaxd6n34e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d6a9bfa-fe96-4308-ad22-6bf698262e98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzVCw8gQhEAY2f5FdbqRjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 796,
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

_source line 4 · 2026-05-12T00:04:31.513Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CuKfjuuqmirz58Unnx5JQo`</summary>

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
  "parentUuid": "8d6a9bfa-fe96-4308-ad22-6bf698262e98",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhMwW8DcdkAaxd6n34e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c904575a-c7ec-4d1b-bae7-e40cc60c0bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzVCw8gQhEAY2f5FdbqRjc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 8223,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 796
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 90,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 796,
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

_source line 5 · 2026-05-12T00:04:31.522Z_

<details><summary>↩ Tool result · `toolu_01CuKfjuuqmirz58Unnx5JQo`</summary>

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
  "parentUuid": "c904575a-c7ec-4d1b-bae7-e40cc60c0bc4",
  "isSidechain": true,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "agentId": "a02c99b6bc249deff",
  "type": "user",
  "uuid": "9163e91d-3d3c-4a4e-b474-5412b20d2fc9",
  "sourceToolAssistantUUID": "c904575a-c7ec-4d1b-bae7-e40cc60c0bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:04:34.564Z_



Now let me search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9163e91d-3d3c-4a4e-b474-5412b20d2fc9",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhN8HWnNcanUjBAVFSv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e5ba5ef-0f2b-480a-8dac-621c8b990342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgCKbc4N3u6FwM3NUhP7xA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1407,
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

_source line 7 · 2026-05-12T00:04:35.523Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011sqpY11J4o1ao4hPvimH7w`</summary>

```json
{
  "query": "\"From Hallucination to Structure Snowballing\" \"Alignment Tax\" constrained decoding LLM reflection arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e5ba5ef-0f2b-480a-8dac-621c8b990342",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhN8HWnNcanUjBAVFSv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e471419-8308-44ef-b148-3d8278309c9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgCKbc4N3u6FwM3NUhP7xA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1407,
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

_source line 8 · 2026-05-12T00:04:36.832Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VSu1qYqQcLyoXeGRdKwkrL`</summary>

```json
{
  "query": "\"Draft-Conditioned Constrained Decoding\" structured generation LLMs arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e471419-8308-44ef-b148-3d8278309c9e",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhN8HWnNcanUjBAVFSv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c65d3c8-a93a-4685-8431-5434d2a4660b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgCKbc4N3u6FwM3NUhP7xA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1407,
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

_source line 9 · 2026-05-12T00:04:37.102Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W9CmMgyrB2mifDZBXyNjRs`</summary>

```json
{
  "query": "CRANE constrained decoding reasoning ICML 2025 Banerjee TC0 complexity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c65d3c8-a93a-4685-8431-5434d2a4660b",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhN8HWnNcanUjBAVFSv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91b8f13e-2f48-4a97-b3eb-749c6a30d144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RgCKbc4N3u6FwM3NUhP7xA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 9019,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 9019,
          "cache_creation_input_tokens": 1407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1407,
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

_source line 10 · 2026-05-12T00:04:42.774Z_

<details><summary>↩ Tool result · `toolu_011sqpY11J4o1ao4hPvimH7w`</summary>

```text
Web search results for query: ""From Hallucination to Structure Snowballing" "Alignment Tax" constrained decoding LLM reflection arXiv 2026"

Links: [{"title":"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/html/2604.06066"},{"title":"[2604.06066] From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/abs/2604.06066"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18753"},{"title":"Distortion Instead of Hallucination: The Effect of Reasoning Under Strict Constraints","url":"https://arxiv.org/html/2601.01490v1"},{"title":"From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets","url":"https://arxiv.org/html/2604.26747v1"},{"title":"Detecting and Correcting Hallucinations in LLM-Generated Code","url":"https://arxiv.org/pdf/2601.19106"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"},{"title":"LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions","url":"https://arxiv.org/html/2509.18970v1"},{"title":"LLMs Will Always Hallucinate, and We Need to Live With This","url":"https://arxiv.org/html/2409.05746v1"},{"title":"Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering | OpenReview","url":"https://openreview.net/forum?id=LBl7Hez0fF"}]

I found the paper you're looking for! Here's what I found:

## "From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection"

This study examines how intrinsic self-correction in Large Language Models frequently fails in open-ended reasoning tasks due to "hallucination snowballing," a phenomenon in which models recursively justify early errors during free-text reflection.

**Key Findings:**

The researchers investigated whether enforcing structured reflection purely through Outlines-based constrained decoding can disrupt error propagation without additional training, evaluating an 8-billion-parameter model (Qwen3-8B), and found that simply imposing structural constraints does not improve self-correction performance.

Instead, it triggers a new failure mode termed "structure snowballing," where the cognitive load required to satisfy strict formatting rules pushes the model into formatting traps.

**Main Contributions:**

The paper provides empirical evidence that intrinsic structured self-correction via constrained decoding introduces an alignment tax when deployed without external training, and defines structure snowballing as a theoretical counterpart to hallucination snowballing, revealing a new failure mode in constrained self-reasoning.

**Performance Impact:**

The application of logic-guided constrained decoding resulted in a performance penalty, with baseline accuracy dropping from 50.0% to 38.0% under constrained conditions.

The paper was published on arXiv on April 7, 2026 (arXiv:2604.06066).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e471419-8308-44ef-b148-3d8278309c9e",
  "isSidechain": true,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "agentId": "a02c99b6bc249deff",
  "type": "user",
  "uuid": "a4ce2def-ca0e-4f4e-a794-c425405db33c",
  "sourceToolAssistantUUID": "1e471419-8308-44ef-b148-3d8278309c9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T00:04:43.455Z_

<details><summary>↩ Tool result · `toolu_01VSu1qYqQcLyoXeGRdKwkrL`</summary>

```text
Web search results for query: ""Draft-Conditioned Constrained Decoding" structured generation LLMs arXiv 2026"

Links: [{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"[2604.14862] Schema Key Wording as an Instruction Channel in Structured Generation under Constrained Decoding","url":"https://arxiv.org/abs/2604.14862"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"Constrained Decoding of Diffusion LLMs with Context-Free Grammars","url":"https://arxiv.org/html/2508.10111v1"},{"title":"Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation","url":"https://arxiv.org/html/2403.06988v1"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603v1"},{"title":"Correctness-Guaranteed Code Generation via Constrained Decoding","url":"https://arxiv.org/html/2508.15866v1"},{"title":"Evaluating Structured Decoding for Text-to-Table Generation: Evidence from Three Datasets","url":"https://arxiv.org/html/2508.15910"},{"title":"Constrained Decoding of Diffusion LLMs with Context-Free Grammars | OpenReview","url":"https://openreview.net/forum?id=7Sph4KyeYO"}]

I found the paper you're looking for! Here's the information:

## Draft-Conditioned Constrained Decoding (DCCD)

Draft-Conditioned Constrained Decoding (DCCD) is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

**Problem It Addresses:**
Large language models (LLMs) are increasingly used to generate executable outputs, JSON objects, and API calls, where a single syntax error can make the output unusable. Constrained decoding enforces validity token-by-token via masking and renormalization, but it can distort generation when the model assigns low probability mass to valid continuations, pushing decoding toward locally valid yet semantically incorrect trajectories.

**Key Innovation:**
DCCD is analyzed through a KL-projection view, showing that draft conditioning increases feasible mass and reduces the cumulative "projection tax" induced by hard constraints, with an optional best-of-K draft selection.

**Paper Details:**
- **arXiv ID:** 2603.03305
- **Authors:** Avinash Reddy and 3 other authors
- **Submission Date:** February 8, 2026
- **Link:** https://arxiv.org/abs/2603.03305


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c65d3c8-a93a-4685-8431-5434d2a4660b",
  "isSidechain": true,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "agentId": "a02c99b6bc249deff",
  "type": "user",
  "uuid": "63309005-a1ef-4dd7-b60e-3cda07b991e5",
  "sourceToolAssistantUUID": "9c65d3c8-a93a-4685-8431-5434d2a4660b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:04:44.166Z_

<details><summary>↩ Tool result · `toolu_01W9CmMgyrB2mifDZBXyNjRs`</summary>

```text
Web search results for query: "CRANE constrained decoding reasoning ICML 2025 Banerjee TC0 complexity"

Links: [{"title":"ICML Poster CRANE: Reasoning with constrained LLM generation","url":"https://icml.cc/virtual/2025/poster/43624"},{"title":"CRANE: Reasoning with constrained LLM generation | OpenReview","url":"https://openreview.net/forum?id=wKs9fHYxCV"},{"title":"Improving Procedural Skill Explanations via Constrained Generation: A","url":"https://arxiv.org/pdf/2511.20942"},{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://proceedings.mlr.press/v267/banerjee25a.html"},{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"ICLR CRANE: Reasoning with constrained LLM generation","url":"https://iclr.cc/virtual/2025/36222"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"[2502.09061v2] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061v2"},{"title":"CRANE: Reasoning with constrained LLM generation | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.09061v3"}]

Based on the search results, I found comprehensive information about the CRANE paper:

## CRANE: Reasoning with Constrained LLM Generation

CRANE is a paper by Debangshu Banerjee and colleagues, published at ICML 2025 (Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:2836-2857).

### Core Problem and Solution

The paper addresses the issue that constrained LLM generation, while promising for enforcing adherence to formal grammars, has empirically been observed to diminish the reasoning capabilities of LLMs, and the authors provide a theoretical explanation for why constraining outputs to very restrictive grammars that only allow syntactically valid final answers reduces reasoning capabilities.

The key contribution is demonstrating that by augmenting the output grammar with carefully designed additional rules, it is possible to preserve the reasoning capabilities of the LLM while ensuring syntactic and semantic correctness in its outputs. The authors propose CRANE, a reasoning-augmented constrained decoding algorithm that effectively balances the correctness of constrained generation with the flexibility of unconstrained generation.

### Theoretical Insights

The paper's theoretical foundation builds on the result that a single LLM autoregressive step can be simulated by a logspace-uniform constant-depth threshold circuit (TC0), a restrictive complexity class.

### Empirical Results

Experiments on multiple open-source LLMs and benchmarks show that CRANE significantly outperforms both state-of-the-art constrained decoding strategies and standard unconstrained decoding, showing up to 10% points accuracy improvement over baselines on challenging symbolic reasoning benchmarks GSM-symbolic and FOLIO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91b8f13e-2f48-4a97-b3eb-749c6a30d144",
  "isSidechain": true,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "agentId": "a02c99b6bc249deff",
  "type": "user",
  "uuid": "7e6a6c80-aab4-4cfc-b1c4-fd596c8efe20",
  "sourceToolAssistantUUID": "91b8f13e-2f48-4a97-b3eb-749c6a30d144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T00:04:47.203Z_

Let me get more details on the DCCD paper's GSM8K results and the CRANE TC0 claim to verify the specific characterizations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e6a6c80-aab4-4cfc-b1c4-fd596c8efe20",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhP47mVdFDrpY3WzqvX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5a2a70a-35cf-4ec0-a122-267b71101550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgHF4YqV1AnTJoFnhHycFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 10426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2782,
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

_source line 14 · 2026-05-12T00:04:48.224Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018YZrYLDSbaiQeaBDhmqkQT`</summary>

```json
{
  "query": "Draft-Conditioned Constrained Decoding DCCD GSM8K \"+24\" results projection tax arXiv 2603.03305"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5a2a70a-35cf-4ec0-a122-267b71101550",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhP47mVdFDrpY3WzqvX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed88a568-635b-4cef-aaca-66e575ecfcf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgHF4YqV1AnTJoFnhHycFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 10426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2782,
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

_source line 15 · 2026-05-12T00:04:48.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HWCQEEnPTK1piV3xpZczvJ`</summary>

```json
{
  "query": "CRANE Banerjee constrained decoding \"TC0\" \"limits\" reasoning complexity class theoretical result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed88a568-635b-4cef-aaca-66e575ecfcf5",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhP47mVdFDrpY3WzqvX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0eb07e3-6b9e-4c12-b7a7-ecdca29efff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgHF4YqV1AnTJoFnhHycFu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 10426,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2782
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 10426,
          "cache_creation_input_tokens": 2782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2782,
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

_source line 16 · 2026-05-12T00:04:55.548Z_

<details><summary>↩ Tool result · `toolu_01HWCQEEnPTK1piV3xpZczvJ`</summary>

```text
Web search results for query: "CRANE Banerjee constrained decoding "TC0" "limits" reasoning complexity class theoretical result"

Links: [{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.09061v3"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v3"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://debangshu-banerjee.github.io/assets/pdf/CRANE.pdf"},{"title":"CRANE: Reasoning with constrained LLM generation | OpenReview","url":"https://openreview.net/forum?id=wKs9fHYxCV"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://par.nsf.gov/servlets/purl/10633770"},{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"[2502.09061v2] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061v2"},{"title":"[Literature Review] CRANE: Reasoning with constrained LLM generation","url":"https://www.themoonlight.io/en/review/crane-reasoning-with-constrained-llm-generation"},{"title":"Paper page - CRANE: Reasoning with constrained LLM generation","url":"https://huggingface.co/papers/2502.09061"}]

I found comprehensive information about the CRANE paper and its theoretical results. Here's what I found:

## CRANE: Reasoning with Constrained LLM Generation

The CRANE paper by Debangshu Banerjee et al. addresses how constrained LLM generation to restrictive grammars diminishes reasoning capabilities, and provides a theoretical explanation for why constraining LLM outputs to very restrictive grammars that only allow syntactically valid final answers reduces the reasoning capabilities of the model.

### Key Theoretical Result on TC0

The key theoretical insight is formalized in Proposition 3.1, which shows that LLMs under such constraints can only solve problems within the TC0 complexity class (constant-depth threshold circuits).

TC0 is a class of computational problems that can be recognized by constant-depth, polynomial-size circuits composed of threshold gates.

### The TC0 = NL Complexity Limit

Unless TC0 = NL, no LLM under constrained decoding can solve st-connectivity. There exist problems, such as st-connectivity, an LLM can solve in an unconstrained setting but cannot be solved under constrained decoding unless logspace-uniform TC0 = NL.

### The Solution: CRANE Algorithm

By augmenting the output grammar with carefully designed additional rules, it is always possible to preserve the reasoning capabilities of the LLM while ensuring syntactic and semantic correctness in its outputs. CRANE effectively alternates between unconstrained generation for reasoning and constrained generation for producing structurally correct outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0eb07e3-6b9e-4c12-b7a7-ecdca29efff5",
  "isSidechain": true,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "agentId": "a02c99b6bc249deff",
  "type": "user",
  "uuid": "e365a5a7-ab92-4ff8-afd1-64beb7dbe0de",
  "sourceToolAssistantUUID": "a0eb07e3-6b9e-4c12-b7a7-ecdca29efff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T00:04:55.963Z_

<details><summary>↩ Tool result · `toolu_018YZrYLDSbaiQeaBDhmqkQT`</summary>

```text
Web search results for query: "Draft-Conditioned Constrained Decoding DCCD GSM8K "+24" results projection tax arXiv 2603.03305"

Links: [{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"When Correct Isn’t Usable: Improving Structured Output Reliability in Small Language Models","url":"https://arxiv.org/html/2605.02363v1"},{"title":"Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference","url":"https://arxiv.org/html/2604.13634v1"},{"title":"Speculative Decoding with CTC-based Draft Model for LLM Inference Acceleration","url":"https://arxiv.org/html/2412.00061v1"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251v2"},{"title":"[2405.00218] Constrained Decoding for Secure Code Generation","url":"https://arxiv.org/abs/2405.00218"},{"title":"PARALLEL SPECULATIVE DECODING WITH ADAPTIVE ...","url":"https://openreview.net/notes/edits/attachment?id=GQowRuHgNL&name=pdf"}]

I found the arXiv paper you were searching for. Here are the key details about **Draft-Conditioned Constrained Decoding (DCCD)**:

## Overview

DCCD is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

## Key Results

The "+24" percentage points improvement you mentioned relates to this: DCCD improves strict structured accuracy by up to +24 percentage points over standard constrained decoding (e.g., 15.2% to 39.0% on GSM8K with a 1B model)

## Projection Tax Analysis

Regarding the "projection tax" mentioned in your query, DCCD is analyzed through a KL-projection view, showing that draft conditioning increases feasible mass and reduces the cumulative "projection tax" induced by hard constraints, with an optional best-of-K draft selection.

## Performance Improvements

Larger models (Qwen2.5 14B, Llama 3.1 8B, Qwen2.5 7B) demonstrate strong baseline performance with DCCD, approaching or exceeding 90% on GSM8K. Additionally, DCCD enables smaller, cheaper model pairs to match or exceed much larger constrained baselines, demonstrating that separating reasoning from formatting yields substantial gains in parameter efficiency.

The paper was published in February 2026 and the arXiv ID is 2603.03305.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed88a568-635b-4cef-aaca-66e575ecfcf5",
  "isSidechain": true,
  "promptId": "e334abec-b44e-456e-860d-77851683c630",
  "agentId": "a02c99b6bc249deff",
  "type": "user",
  "uuid": "fdc15bc1-b05e-44ba-84dd-084596a5bb81",
  "sourceToolAssistantUUID": "ed88a568-635b-4cef-aaca-66e575ecfcf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-12T00:05:24.433Z_

Here are my findings for all three papers:

---

## Paper 1: "From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection"

**Exists?** Yes. It is on arXiv as [2604.06066](https://arxiv.org/abs/2604.06066), published April 7, 2026.

**Characterization accuracy:** The proposal's claim that it "documents cascading formatting errors under strict structural constraints in Qwen3-8B" is **accurate**. The paper evaluates Qwen3-8B (an 8-billion-parameter model) and finds that imposing structured reflection via Outlines-based constrained decoding triggers a failure mode they call "structure snowballing" -- where the cognitive load of satisfying strict formatting rules pushes the model into formatting traps. Baseline accuracy dropped from 50.0% to 38.0% under constrained conditions, demonstrating a clear "alignment tax."

---

## Paper 2: "Draft-Conditioned Constrained Decoding for Structured Generation in LLMs"

**Exists?** Yes. It is on arXiv as [2603.03305](https://arxiv.org/abs/2603.03305), submitted February 8, 2026 (published in March 2026 on arXiv, consistent with the "Mar 2026" claim).

**Characterization accuracy:** The proposal's claims are **accurate but require slight nuance**:

- **"Projection tax"**: Correct. The paper analyzes constrained decoding through a KL-projection view and explicitly uses the term "projection tax" to describe the cumulative distortion induced by hard constraints.
- **"+24pp gains on GSM8K"**: Correct. DCCD improves strict structured accuracy by up to +24 percentage points over standard constrained decoding on GSM8K (e.g., 15.2% to 39.0% with a 1B model). However, it is worth noting this is the gain for a very small 1B model. Larger models (7B--14B) already have strong baselines and the absolute gains are smaller (though DCCD still helps). The proposal should ideally mention the model size when citing this number, as "+24pp" without context could be misleading about the general magnitude of improvement.

---

## Paper 3: CRANE (Banerjee et al., ICML 2025)

**Exists?** Yes. Published as [CRANE: Reasoning with constrained LLM generation](https://proceedings.mlr.press/v267/banerjee25a.html) at ICML 2025 (PMLR 267:2836-2857). Also on arXiv as [2502.09061](https://arxiv.org/abs/2502.09061).

**Characterization accuracy:** The proposal's claim that "CRANE proved that constrained decoding limits LLMs to TC^0 complexity" is **substantively correct but slightly overstated**. What the paper actually shows (Proposition 3.1) is:

- A single LLM autoregressive step can be simulated by a logspace-uniform constant-depth threshold circuit (TC^0).
- Therefore, LLMs under restrictive constrained decoding (grammars that only allow syntactically valid final answers with no room for intermediate reasoning tokens) can only solve problems within TC^0.
- Unless TC^0 = NL, such constrained LLMs cannot solve problems like st-connectivity that unconstrained LLMs can handle.

The nuance is that this limitation applies specifically to constrained decoding with **restrictive grammars that forbid intermediate reasoning steps**. CRANE's own solution demonstrates that augmenting the grammar to allow reasoning tokens removes this limitation. So the claim "constrained decoding limits LLMs to TC^0" is correct only for the restrictive case -- CRANE itself shows the limitation is avoidable by designing better grammars.

---

## Summary

| Paper | Exists? | Characterization |
|-------|---------|-----------------|
| Structure Snowballing (Apr 2026) | Yes | Accurate |
| DCCD (Mar 2026) | Yes | Accurate, but +24pp figure is specific to a 1B model |
| CRANE (ICML 2025) | Yes | Substantively correct, but the TC^0 limit applies only to restrictive grammars, not all constrained decoding |

Sources:
- [From Hallucination to Structure Snowballing (arXiv)](https://arxiv.org/abs/2604.06066)
- [From Hallucination to Structure Snowballing (HTML)](https://arxiv.org/html/2604.06066)
- [Draft-Conditioned Constrained Decoding (arXiv)](https://arxiv.org/abs/2603.03305)
- [Draft-Conditioned Constrained Decoding (PDF)](https://arxiv.org/pdf/2603.03305)
- [CRANE: Reasoning with constrained LLM generation (ICML proceedings)](https://proceedings.mlr.press/v267/banerjee25a.html)
- [CRANE (arXiv)](https://arxiv.org/abs/2502.09061)
- [CRANE (OpenReview)](https://openreview.net/forum?id=wKs9fHYxCV)
- [CRANE (ICML poster)](https://icml.cc/virtual/2025/poster/43624)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc15bc1-b05e-44ba-84dd-084596a5bb81",
  "isSidechain": true,
  "agentId": "a02c99b6bc249deff",
  "requestId": "req_011CawhPvZdSYPoMVPg13dDT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb18b06f-a721-4e75-a652-2e5cf6d09cf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "39816bd0-bf80-4353-985c-a102c062aef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014h4mRNSuCN63m62tHsCkuZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 862,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 13208,
      "output_tokens": 1307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 862,
          "output_tokens": 1307,
          "cache_read_input_tokens": 13208,
          "cache_creation_input_tokens": 1039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1039,
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
