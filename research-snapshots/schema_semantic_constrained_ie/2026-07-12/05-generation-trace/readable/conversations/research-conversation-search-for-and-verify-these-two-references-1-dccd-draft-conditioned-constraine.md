# Research conversation: Search for and verify these two references: 1. "DCCD: Draft-Conditioned Constrained Decoding for Structured Generation i

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a56c3008d2193228f.jsonl`
- **Structured JSON:** [`e0f0fe8b43fb353dd610.json`](../../sessions/e0/e0f0fe8b43fb353dd610.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-10T18:49:56.386Z_

Search for and verify these two references:

1. "DCCD: Draft-Conditioned Constrained Decoding for Structured Generation in LLMs" (arXiv 2603.03305, February 2026). The claim is it achieves +24 pp over standard constrained decoding on GSM8K with small models, is training-free, and works by generating an unconstrained draft first, then generating constrained output conditioned on the draft.

2. "XGrammar-2" — claimed to be the default constrained decoding backend in vLLM/SGLang/TensorRT-LLM since ~early 2026, guaranteeing 100% structural validity with minimal overhead.

3. Also search for "When Correct Isn't Usable" (arXiv 2605.02363, May 2026) which claims constrained decoding causes 3.6-8.2x latency overhead while degrading task accuracy.

Use WebSearch and if needed WebFetch. Report whether each exists and whether the cited claims are accurate. Under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a56c3008d2193228f",
  "type": "user",
  "uuid": "84cb3ed0-d9ac-4f96-a179-4d995e1ceb98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:49:56.390Z_

```json
{
  "parentUuid": "84cb3ed0-d9ac-4f96-a179-4d995e1ceb98",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "89618df8-7774-4da4-ba29-491bb3ceef01",
  "timestamp": "2026-05-10T18:49:56.390Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:50:00.463Z_



I'll search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89618df8-7774-4da4-ba29-491bb3ceef01",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPZqedTx3jvemDXC7xV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbf66765-0db0-4007-a7af-ede931cc1437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQvuEfgSPckchWjETLg5Cp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 769,
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

_source line 4 · 2026-05-10T18:50:00.890Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T9XDj7LgjNFcRN4i7qfAEw`</summary>

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
  "parentUuid": "dbf66765-0db0-4007-a7af-ede931cc1437",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPZqedTx3jvemDXC7xV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a06af1dd-a818-46c2-ba9d-7b16d9c606e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQvuEfgSPckchWjETLg5Cp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 769,
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

### Tool result

_source line 5 · 2026-05-10T18:50:00.893Z_

<details><summary>↩ Tool result · `toolu_01T9XDj7LgjNFcRN4i7qfAEw`</summary>

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
  "parentUuid": "a06af1dd-a818-46c2-ba9d-7b16d9c606e3",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a56c3008d2193228f",
  "type": "user",
  "uuid": "c8debd96-a9c4-4d7b-91e6-e4048029df43",
  "sourceToolAssistantUUID": "a06af1dd-a818-46c2-ba9d-7b16d9c606e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:50:05.906Z_



Now let me search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8debd96-a9c4-4d7b-91e6-e4048029df43",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPaBR1iqzT5782xFRVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf957423-1ef1-42dd-a208-aeb7b7122c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9jm8JjuaxAUMZeQdrBPdM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
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

_source line 7 · 2026-05-10T18:50:06.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q6ABjJ1jRrv73SM3JPnoaf`</summary>

```json
{
  "query": "arXiv 2603.03305 DCCD Draft-Conditioned Constrained Decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf957423-1ef1-42dd-a208-aeb7b7122c01",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPaBR1iqzT5782xFRVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c0a089e-1a25-4014-a4ec-3a71831f2205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9jm8JjuaxAUMZeQdrBPdM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
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

_source line 8 · 2026-05-10T18:50:07.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013uw5c9wqN1s7pqfxmfCwKW`</summary>

```json
{
  "query": "XGrammar-2 constrained decoding vLLM SGLang TensorRT-LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c0a089e-1a25-4014-a4ec-3a71831f2205",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPaBR1iqzT5782xFRVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1422c417-94b8-429c-9417-b2acb008dd49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9jm8JjuaxAUMZeQdrBPdM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1900,
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

_source line 9 · 2026-05-10T18:50:08.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UaKs8qQmrQgKcWqiRC6Sz2`</summary>

```json
{
  "query": "arXiv 2605.02363 \"When Correct Isn't Usable\" constrained decoding latency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1422c417-94b8-429c-9417-b2acb008dd49",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPaBR1iqzT5782xFRVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4152a55-d1d1-4969-905e-9a31e901ff2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9jm8JjuaxAUMZeQdrBPdM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 8073,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 211,
          "cache_read_input_tokens": 8073,
          "cache_creation_input_tokens": 1900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1900,
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

_source line 10 · 2026-05-10T18:50:12.062Z_

<details><summary>↩ Tool result · `toolu_01UaKs8qQmrQgKcWqiRC6Sz2`</summary>

```text
Web search results for query: "arXiv 2605.02363 "When Correct Isn't Usable" constrained decoding latency"

Links: [{"title":"[2605.02363] When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models","url":"https://arxiv.org/abs/2605.02363"},{"title":"[2605.02363v1] When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models","url":"https://arxiv.org/abs/2605.02363v1"}]

Based on the search results, I found the arXiv paper 2605.02363 titled "When Correct Isn't Usable: Improving Structured Output Reliability in Small Language Models."

Here are the key findings related to your query:

The paper studies the structured-output reliability gap in deployed language models using two mathematical benchmarks (GSM8K and MATH) where outputs must be in JSON format with required fields.

Regarding constrained decoding and latency, constrained decoding enforces syntactic validity but incurs 3.6x-8.2x latency overhead and in several settings degrades task performance substantially.

The paper also evaluates different prompting strategies, finding that naive prompting achieves up to 85% task accuracy on GSM8K but 0% output accuracy across all models and datasets, while reference prompting yields 0% output accuracy for two of four models tested.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4152a55-d1d1-4969-905e-9a31e901ff2d",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a56c3008d2193228f",
  "type": "user",
  "uuid": "ce87cece-ed94-45d5-925d-0a639248dc6c",
  "sourceToolAssistantUUID": "d4152a55-d1d1-4969-905e-9a31e901ff2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T18:50:15.089Z_

<details><summary>↩ Tool result · `toolu_01Q6ABjJ1jRrv73SM3JPnoaf`</summary>

```text
Web search results for query: "arXiv 2603.03305 DCCD Draft-Conditioned Constrained Decoding"

Links: [{"title":"[2603.03305] Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/abs/2603.03305"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"},{"title":"Constrained Decoding with Speculative Lookaheads","url":"https://arxiv.org/html/2412.10418v1"},{"title":"[2603.05210] Balancing Coverage and Draft Latency in Vocabulary Trimming for Faster Speculative Decoding","url":"https://arxiv.org/abs/2603.05210"},{"title":"Constrained Decoding of Diffusion LLMs with Context-Free Grammars","url":"https://arxiv.org/html/2508.10111v1"},{"title":"Speculative Speculative Decoding Tanishq Kumar1,* Tri Dao2,3 Avner May3","url":"https://arxiv.org/pdf/2603.03251"},{"title":"Speculative Speculative Decoding","url":"https://arxiv.org/html/2603.03251"},{"title":"Constrained Discrete Diffusion","url":"https://arxiv.org/html/2503.09790v2"},{"title":"Correctness-Guaranteed Code Generation via Constrained Decoding","url":"https://arxiv.org/html/2508.15866v1"}]

I found the paper you were looking for! Here's what I found about arXiv 2603.03305:

## Draft-Conditioned Constrained Decoding (DCCD)

DCCD is a simple two-step, training-free inference procedure that decouples semantic planning from structural enforcement: an unconstrained draft is generated first, and constrained decoding is then applied, conditioned on this draft, to guarantee validity.

### The Problem It Addresses

Large language models (LLMs) are increasingly used to generate executable outputs, JSON objects, and API calls, where a single syntax error can make the output unusable. Constrained decoding enforces validity token-by-token via masking and renormalization, but it can distort generation when the model assigns low probability mass to valid continuations, pushing decoding toward locally valid yet semantically incorrect trajectories.

### How It Works

In Step 1, a model generates an unconstrained draft that captures the semantic plan or intermediate reasoning. In Step 2, we generate the final structured output using constrained decoding conditioned on the draft. Conditioning shifts probability mass toward schema-consistent continuations, so the subsequent constraint enforcement step is substantially less distortive.

### Results

DCCD improves strict structured accuracy by up to +24 percentage points over standard constrained decoding (e.g., 15.2% to 39.0% on GSM8K with a 1B model), and enables smaller model pairs to match or exceed much larger constrained baselines, yielding substantial gains in parameter efficiency.

The paper was submitted on February 8, 2026, and was authored by Avinash Reddy, Thayne T. Walker, James S. Ide, and Amrit Singh Bedi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c0a089e-1a25-4014-a4ec-3a71831f2205",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a56c3008d2193228f",
  "type": "user",
  "uuid": "36c33764-962d-4b52-8dbe-0455545f7716",
  "sourceToolAssistantUUID": "5c0a089e-1a25-4014-a4ec-3a71831f2205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:50:15.815Z_

<details><summary>↩ Tool result · `toolu_013uw5c9wqN1s7pqfxmfCwKW`</summary>

```text
Web search results for query: "XGrammar-2 constrained decoding vLLM SGLang TensorRT-LLM 2026"

Links: [{"title":"MLC | XGrammar-2: Fast and Customizable Structured Generation for Tool Calling and Agents","url":"https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"vLLM vs TensorRT-LLM vs SGLang: H100 Benchmarks (2026) | Spheron Blog","url":"https://www.spheron.network/blog/vllm-vs-tensorrt-llm-vs-sglang-benchmarks/"},{"title":"xgrammar · PyPI","url":"https://pypi.org/project/xgrammar/"},{"title":"Best LLM Inference Engines in 2026: vLLM, TensorRT-LLM, TGI, and SGLang Compared | Yotta Labs","url":"https://www.yottalabs.ai/post/best-llm-inference-engines-in-2026-vllm-tensorrt-llm-tgi-and-sglang-compared"},{"title":"vLLM vs SGLang: LLM Inference Server Comparison 2026","url":"https://techsy.io/en/blog/vllm-vs-sglang"},{"title":"vLLM vs Ollama vs SGLang vs TensorRT-LLM Serving 2026 Search","url":"https://theaiengineer.substack.com/p/vllm-vs-ollama-vs-sglang-vs-tensorrt"},{"title":"A Comprehensive Comparison of LLM Inference Engines: vLLM, TGI, TensorRT-LLM, SGLang, llama.cpp, and Ollama | Enterprise Unified LLM API Gateway (One Key for All Models) | n1n.ai","url":"https://explore.n1n.ai/blog/llm-inference-engine-comparison-vllm-tgi-tensorrt-sglang-2026-03-13"},{"title":"Structured Outputs | sihyeong/Awesome-LLM-Inference-Engine | DeepWiki","url":"https://deepwiki.com/sihyeong/Awesome-LLM-Inference-Engine/4.7-structured-outputs"},{"title":"Guided Decoding Performance on vLLM and SGLang - The official SqueezeBits Tech blog","url":"https://blog.squeezebits.com/guided-decoding-performance-vllm-sglang"}]

Based on the search results, here's what I found about XGrammar-2, constrained decoding, and its integration with vLLM, SGLang, and TensorRT-LLM:

## XGrammar-2 Release

XGrammar-2 has been released in May 2026. XGrammar-2 is a release that brings a series of new abstractions and optimizations designed to provide comprehensive support for agent applications.

## Integration with Serving Engines

XGrammar-2 has been integrated into mainstream LLM serving engines, including SGLang, vLLM, TensorRT-LLM, and MLC-LLM, enabling these engines to support strict mode tool calling for popular models such as DeepSeek V4 and Qwen 3.6.

## Key Features and Optimizations

XGrammar-2 introduces Structural Tag, a composable JSON protocol that uniformly expresses OpenAI harmony format, tool calling, reasoning channels, and any custom output structure. Multiple efficiency optimizations, such as cross-grammar caching, repetition-state compression, and batching and speculative decoding support, ensure fast processing and minimal overhead even for huge structures.

## Performance Improvements

XGrammar-2 achieves up to an 80× compilation speedup over XGrammar. In a single-batch setting with warm-up and comparable output lengths, the Structural Tag adds minimal latency overhead, and XGrammar-2 improves both schema reliability and tool-calling accuracy while keeping overhead minimal.

## Adoption

XGrammar-2 has been adopted by leading frontier AI labs and leading AI companies in their products.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1422c417-94b8-429c-9417-b2acb008dd49",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a56c3008d2193228f",
  "type": "user",
  "uuid": "5c6e3bf5-5f56-4847-869d-f38f56e3ec07",
  "sourceToolAssistantUUID": "1422c417-94b8-429c-9417-b2acb008dd49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T18:50:18.223Z_

Let me fetch the abstract of the third paper to verify the specific claims more precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c6e3bf5-5f56-4847-869d-f38f56e3ec07",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPbGjXb4PNN6Yp582Mv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98359a14-784b-4f2d-8a4a-9f5379904c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MArATfQduyV6pwjANtWJGM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 394,
      "cache_creation_input_tokens": 2212,
      "cache_read_input_tokens": 9973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2212,
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

_source line 14 · 2026-05-10T18:50:19.821Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nq6tMKSxw81dYdx4LDyhRS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.02363",
  "prompt": "Extract the full abstract and key claims about constrained decoding latency overhead and task accuracy degradation. Does it say 3.6-8.2x latency overhead? Does it say constrained decoding degrades task accuracy?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98359a14-784b-4f2d-8a4a-9f5379904c37",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPbGjXb4PNN6Yp582Mv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f7806f0-aa79-4dce-af02-9bf63604e07e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MArATfQduyV6pwjANtWJGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 394,
      "cache_creation_input_tokens": 2212,
      "cache_read_input_tokens": 9973,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2212
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 394,
          "output_tokens": 149,
          "cache_read_input_tokens": 9973,
          "cache_creation_input_tokens": 2212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2212,
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

_source line 15 · 2026-05-10T18:50:26.590Z_

<details><summary>↩ Tool result · `toolu_01Nq6tMKSxw81dYdx4LDyhRS`</summary>

```text
# Abstract and Key Claims Analysis

## Full Abstract

"Deployed language models must produce outputs that are both correct and format-compliant. We study this structured-output reliability gap using two mathematical benchmarks -- GSM8K and MATH -- as a controlled testbed: ground truth is unambiguous and the output contract is strict (JSON with required fields). We evaluate three 7-9B models under five prompting strategies and report output accuracy -- the joint event of mathematical correctness and valid JSON structure -- as the primary metric. A systematic format failure emerges: NAIVE prompting (no system prompt) achieves up to 85% task accuracy on GSM8K but 0% output accuracy across all models and datasets. REFERENCE prompting (a minimal hand-written JSON format prompt) fares little better, yielding 0% output accuracy for two of four models tested. Constrained decoding enforces syntactic validity but incurs 3.6x-8.2x latency overhead and in several settings degrades task performance substantially. To overcome this limitation, we developed AloLab, an iterative system-prompt optimizer (meta-agent: Claude Sonnet 4.5) requiring only black-box API access to the target model; it reaches 84-87% output accuracy on GSM8K and 34-40% on MATH across five independent runs per model, with 29/30 paired McNemar comparisons against the best static prompt significant at p < 0.05, at near-NAIVE inference latency and without model fine-tuning."

## Key Claims Verified

**Latency Overhead:** Yes, the paper explicitly states: "incurs 3.6x-8.2x latency overhead"

**Task Accuracy Degradation:** Yes, confirmed: "degrades task performance substantially"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f7806f0-aa79-4dce-af02-9bf63604e07e",
  "isSidechain": true,
  "promptId": "8ecf08e1-2116-4f25-b8d6-7ecf13c4de4d",
  "agentId": "a56c3008d2193228f",
  "type": "user",
  "uuid": "7ab6e45c-595d-48a7-92e2-df36ba00ad9d",
  "sourceToolAssistantUUID": "6f7806f0-aa79-4dce-af02-9bf63604e07e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T18:50:40.794Z_

Here are the verification results for all three references:

---

**1. DCCD (arXiv 2603.03305) -- VERIFIED.** The paper exists, dated February 2026. All claims are accurate: it is training-free, works by generating an unconstrained draft first then applying constrained decoding conditioned on that draft, and reports +24 pp improvement over standard constrained decoding on GSM8K (specifically 15.2% to 39.0% with a 1B model).

**2. XGrammar-2 -- PARTIALLY VERIFIED.** XGrammar-2 is real and was announced May 4, 2026. It is integrated into vLLM, SGLang, TensorRT-LLM, and MLC-LLM. However, the claim that it has been the "default backend since early 2026" is inaccurate -- it was only released in May 2026. The original XGrammar (v1) was the widely adopted backend earlier. The claims about 100% structural validity with minimal overhead are broadly consistent with its design goals (it enforces grammar-based constraints and reports minimal latency overhead), but the "since early 2026" timeline is wrong.

**3. "When Correct Isn't Usable" (arXiv 2605.02363) -- VERIFIED.** The paper exists, published May 2026. The 3.6-8.2x latency overhead claim is stated verbatim in the abstract. The claim that constrained decoding degrades task accuracy is also confirmed ("degrades task performance substantially"). Note: the paper studies small models (7-9B parameters) specifically, so the findings are scoped to that regime.

Sources:
- [DCCD - arXiv 2603.03305](https://arxiv.org/abs/2603.03305)
- [XGrammar-2 Blog Post](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)
- [XGrammar GitHub](https://github.com/mlc-ai/xgrammar)
- [When Correct Isn't Usable - arXiv 2605.02363](https://arxiv.org/abs/2605.02363)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab6e45c-595d-48a7-92e2-df36ba00ad9d",
  "isSidechain": true,
  "agentId": "a56c3008d2193228f",
  "requestId": "req_011CauPc4iVcZkWpwoKdMFn3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7eee9f2-30bd-475e-9488-0743b0d3993c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8c1da5e2-119a-4877-9dbb-b7ef21ad637a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjWdGsY7XAv6pkvuWDwRZt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 12185,
      "output_tokens": 534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 534,
          "cache_read_input_tokens": 12185,
          "cache_creation_input_tokens": 950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 950,
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
