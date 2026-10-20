# Research conversation: Search the web to verify these specific claims about XGrammar-2: 1. Does XGrammar-2 exist as a paper (arXiv Jan 2026, Li

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a0a3ddb929492799e.jsonl`
- **Structured JSON:** [`a0b11856e26d76028b66.json`](../../sessions/a0/a0b11856e26d76028b66.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-11T23:05:00.279Z_

Search the web to verify these specific claims about XGrammar-2:
1. Does XGrammar-2 exist as a paper (arXiv Jan 2026, Li et al.)?
2. Does it support mask_callback() or TagDispatch interfaces?
3. Is it actually the default backend for vLLM/SGLang/TensorRT-LLM?
4. Does it achieve <10ms/step overhead?

Use WebSearch to find the paper and WebFetch to read its abstract and key sections. Search for "XGrammar-2 structured generation 2026" and "site:arxiv.org XGrammar-2". Report exact findings with URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "92f8a00a-6f67-4321-858e-a595e98c405a",
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

_source line 2 · 2026-05-11T23:05:00.283Z_

```json
{
  "parentUuid": "92f8a00a-6f67-4321-858e-a595e98c405a",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
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
  "uuid": "78acfc2a-576e-4487-829e-2ac124990d43",
  "timestamp": "2026-05-11T23:05:00.283Z",
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

_source line 3 · 2026-05-11T23:05:03.699Z_



I'll search for XGrammar-2 using multiple queries in parallel. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78acfc2a-576e-4487-829e-2ac124990d43",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcpsWSF1ovTRbr3cTQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cbb720a-78f3-4174-b241-9ac22ca7258b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ko5f4tJXKhgYinhSCFdhcq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8933,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8933,
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

_source line 4 · 2026-05-11T23:05:04.226Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01C12N4RxauqtuL5csaiuQPu`</summary>

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
  "parentUuid": "5cbb720a-78f3-4174-b241-9ac22ca7258b",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcpsWSF1ovTRbr3cTQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ee27295-4e7c-4482-91da-bd10cdf4c4cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ko5f4tJXKhgYinhSCFdhcq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8933,
      "cache_read_input_tokens": 0,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8933,
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

_source line 5 · 2026-05-11T23:05:04.231Z_

<details><summary>↩ Tool result · `toolu_01C12N4RxauqtuL5csaiuQPu`</summary>

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
  "parentUuid": "2ee27295-4e7c-4482-91da-bd10cdf4c4cd",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "3a3b708e-b12c-4e25-82fd-78b17152b2f6",
  "sourceToolAssistantUUID": "2ee27295-4e7c-4482-91da-bd10cdf4c4cd",
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

_source line 6 · 2026-05-11T23:05:06.902Z_



Now let me run multiple searches in parallel to investigate XGrammar-2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a3b708e-b12c-4e25-82fd-78b17152b2f6",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcqAhJEt5QFi4sAE7EZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a495421f-faa1-4863-aadf-6c7c67a0a909",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V745Vrex5k1Rz2uP5kaQ8o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1920,
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

_source line 7 · 2026-05-11T23:05:07.439Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G8v2skduSRCqL2ywZo5HWF`</summary>

```json
{
  "query": "XGrammar-2 structured generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a495421f-faa1-4863-aadf-6c7c67a0a909",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcqAhJEt5QFi4sAE7EZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc297cba-a473-4a03-b9b1-299f009f9906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V745Vrex5k1Rz2uP5kaQ8o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1920,
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

_source line 8 · 2026-05-11T23:05:07.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ZEnn9mbYSuRvZ5KEcVdpm`</summary>

```json
{
  "query": "site:arxiv.org XGrammar-2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc297cba-a473-4a03-b9b1-299f009f9906",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcqAhJEt5QFi4sAE7EZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80d2d682-d2f8-4612-9aa6-54a7876580a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V745Vrex5k1Rz2uP5kaQ8o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1920,
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

_source line 9 · 2026-05-11T23:05:08.855Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dtdh4TcVtK943TW721ccLz`</summary>

```json
{
  "query": "XGrammar-2 Li et al arXiv 2026 mask_callback TagDispatch"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80d2d682-d2f8-4612-9aa6-54a7876580a3",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcqAhJEt5QFi4sAE7EZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e907d08c-e107-42fc-ac98-e4739d63e3fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V745Vrex5k1Rz2uP5kaQ8o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1920,
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

_source line 10 · 2026-05-11T23:05:09.502Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ATjf2xR5vwXAtSLV8myzQg`</summary>

```json
{
  "query": "XGrammar vLLM SGLang TensorRT-LLM default backend"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e907d08c-e107-42fc-ac98-e4739d63e3fe",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcqAhJEt5QFi4sAE7EZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f861e61-69e1-43ab-96a4-7647b23628de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V745Vrex5k1Rz2uP5kaQ8o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 8933,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1920
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 239,
          "cache_read_input_tokens": 8933,
          "cache_creation_input_tokens": 1920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1920,
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

_source line 11 · 2026-05-11T23:05:15.038Z_

<details><summary>↩ Tool result · `toolu_01ATjf2xR5vwXAtSLV8myzQg`</summary>

```text
Web search results for query: "XGrammar vLLM SGLang TensorRT-LLM default backend"

Links: [{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"xgrammar · PyPI","url":"https://pypi.org/project/xgrammar/"},{"title":"xgrammar/README.md at main · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/blob/main/README.md"},{"title":"vLLM vs Ollama vs SGLang vs TensorRT-LLM Serving 2026 Search","url":"https://theaiengineer.substack.com/p/vllm-vs-ollama-vs-sglang-vs-tensorrt"},{"title":"vLLM vs TensorRT-LLM vs SGLang: H100 Benchmarks (2026) | Spheron Blog","url":"https://www.spheron.network/blog/vllm-vs-tensorrt-llm-vs-sglang-benchmarks/"},{"title":"8 Best LLM Structured Output Libraries, Ranked [2026]","url":"https://techsy.io/en/blog/best-llm-structured-output-libraries"},{"title":"Benchmarking vLLM, SGLang and TensorRT for Llama 3.1 API","url":"https://cerebrium.ai/blog/benchmarking-vllm-sglang-tensorrt-for-llama-3-1-api"},{"title":"vLLM vs SGLang: LLM Inference Server Comparison 2026","url":"https://techsy.io/en/blog/vllm-vs-sglang"},{"title":"Comparing SGLANG, vLLM, and TensorRT-LLM with GPT-OSS-120B","url":"https://www.clarifai.com/blog/comparing-sglang-vllm-and-tensorrt-llm-with-gpt-oss-120b"},{"title":"Best LLM Inference Engines in 2026: vLLM, TensorRT-LLM, TGI, and SGLang Compared | Yotta Labs","url":"https://www.yottalabs.ai/post/best-llm-inference-engines-in-2026-vllm-tensorrt-llm-tgi-and-sglang-compared"}]

Based on the search results, here's what I found about XGrammar and its relationship to vLLM, SGLang, and TensorRT-LLM:

## XGrammar as Default Backend

XGrammar is the default structured generation backend for most LLM inference engines, including vLLM, SGLang, TensorRT-LLM, and MLC-LLM, as well as many other companies.

## Integration Timeline

XGrammar was officially integrated into SGLang in November 2024. XGrammar was officially integrated into vLLM in December 2024. XGrammar was officially integrated into TensorRT-LLM in January 2025.

## What is XGrammar?

XGrammar is an open-source library for efficient, flexible, and portable structured generation that leverages constrained decoding to ensure 100% structural correctness of the output and supports general context-free grammar to enable a broad range of structures, including JSON, regex, custom context-free grammar, etc.

## Practical Usage

XGrammar is built into vLLM, SGLang, or TensorRT-LLM servers as the default grammar backend if you run self-hosted LLMs on these platforms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f861e61-69e1-43ab-96a4-7647b23628de",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "b30af195-3787-42a3-817e-6a97ead0ed26",
  "sourceToolAssistantUUID": "6f861e61-69e1-43ab-96a4-7647b23628de",
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

_source line 12 · 2026-05-11T23:05:15.414Z_

<details><summary>↩ Tool result · `toolu_01G8v2skduSRCqL2ywZo5HWF`</summary>

```text
Web search results for query: "XGrammar-2 structured generation 2026"

Links: [{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"MLC | XGrammar-2: Fast and Customizable Structured Generation for Tool Calling and Agents","url":"https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation"},{"title":"[2601.04426] XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/abs/2601.04426"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426v2"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"XGRAMMAR 2: DYNAMIC AND EFFICIENT STRUCTURED GENERATION ENGINE FOR AGENTIC LLMS","url":"https://www.arxiv.org/pdf/2601.04426"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.04426"},{"title":"xgrammar · PyPI","url":"https://pypi.org/project/xgrammar/"},{"title":"XGrammar | Home","url":"https://xgrammar.mlc.ai/"}]

Here are the search results for XGrammar-2 structured generation 2026:

## Overview

XGrammar-2 was released in May 2026. XGrammar-2 is a major upgrade of XGrammar built for agent applications.

## Key Features and Innovations

XGrammar-2 introduces Structural Tag, a composable JSON protocol that uniformly expresses OpenAI harmony format, tool calling, reasoning channels, and any custom output structure, exposed directly through serving engines' API.

The design is based on two key ideas: first-class support for tag-triggered structure switching, and fine-grained reuse across requests with different output structures. XGrammar-2 introduces TagDispatch for dynamic structural dispatching and Cross-Grammar Cache for substructure-level cache reuse across grammars, and further improves efficiency with an Earley-based adaptive token mask cache, just-in-time compilation, and repetition state compression.

## Performance Improvements

XGrammar-2 introduces a series of optimizations to tackle complex structures and ensure that even very large grammars incur only minimal overhead. For complex JSON schema structures, repetition compression reduces the compression time from 534 ms to 5.37 ms, a 100x time reduction. XGrammar-2 achieves over 6× tool-calling compilation speed improvement compared to prior state-of-the-art methods, while introducing near-zero latency overhead.

## Integration and Adoption

XGrammar-2 has been incorporated into open-source serving frameworks such as SGLang and vLLM, improving output reliability in agentic tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc297cba-a473-4a03-b9b1-299f009f9906",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "3ea12845-0bff-411c-850c-9d80b21bc1cb",
  "sourceToolAssistantUUID": "fc297cba-a473-4a03-b9b1-299f009f9906",
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

_source line 13 · 2026-05-11T23:05:15.459Z_

<details><summary>↩ Tool result · `toolu_013ZEnn9mbYSuRvZ5KEcVdpm`</summary>

```text
Web search results for query: "site:arxiv.org XGrammar-2"

Links: [{"title":"[2601.04426] XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/abs/2601.04426"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"XGRAMMAR 2: DYNAMIC AND EFFICIENT STRUCTURED GENERATION ENGINE FOR AGENTIC LLMS","url":"https://www.arxiv.org/pdf/2601.04426"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.04426v1"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"[2411.15100v1] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100v1"},{"title":"Guided Decoding and Its Critical Role in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.06631v1"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/html/2505.04016v1"}]

I found research results for XGrammar-2 on arXiv. Here's a summary:

## XGrammar-2 Overview

XGrammar-2 is a structured generation engine for dynamic agentic workloads. Modern LLM agents increasingly rely on dynamic structured generation, such as tool calling and response protocols. Unlike traditional structured generation with static structures, these workloads vary both across requests and within a request, posing new challenges to existing engines.

## Key Features

The design is based on two key ideas: first-class support for tag-triggered structure switching, and fine-grained reuse across requests with different output structures. XGrammar-2 introduces TagDispatch for dynamic structural dispatching and Cross-Grammar Cache for substructure-level cache reuse across grammars.

It further improves efficiency with an Earley-based adaptive token mask cache, just-in-time compilation, and repetition state compression.

## Performance

XGrammar-2 achieves over 6x faster compilation than prior structured generation engines, and incurs near-zero end-to-end overhead in modern LLM serving systems.

## Adoption

XGrammar-2 is open-source and has been adopted in both industry systems and open-source inference engines.

The paper (arXiv 2601.04426) was initially submitted on January 7, 2026, with an updated version on March 26, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80d2d682-d2f8-4612-9aa6-54a7876580a3",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "8c89ad3e-5a6d-41b0-a781-964efcbc61c7",
  "sourceToolAssistantUUID": "80d2d682-d2f8-4612-9aa6-54a7876580a3",
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

_source line 14 · 2026-05-11T23:05:16.216Z_

<details><summary>↩ Tool result · `toolu_01Dtdh4TcVtK943TW721ccLz`</summary>

```text
Web search results for query: "XGrammar-2 Li et al arXiv 2026 mask_callback TagDispatch"

Links: [{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.04426v1"},{"title":"XGRAMMAR 2: DYNAMIC AND EFFICIENT STRUCTURED GENERATION ENGINE FOR AGENTIC LLMS","url":"https://www.arxiv.org/pdf/2601.04426"},{"title":"[2601.04426] XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/abs/2601.04426"},{"title":"XGrammar 2: High-Performance Grammar Systems","url":"https://www.emergentmind.com/topics/xgrammar-2"},{"title":"MLC | XGrammar-2: Fast and Customizable Structured Generation for Tool Calling and Agents","url":"https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation"},{"title":"Re-Mask and Redirect: Exploiting Denoising Irreversibility in Diffusion Language Models","url":"https://arxiv.org/html/2604.08557"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=202&show=2000"},{"title":"Promises and Pitfalls of Generative Masked Language Modeling: Theoretical Framework and Practical Guidelines","url":"https://arxiv.org/html/2407.21046v1"},{"title":"Query Nearby: Offset-Adjusted Mask2Former enhances small-organ segmentation","url":"https://arxiv.org/html/2506.05897v1"}]

I found the research paper you were looking for. Here are the key findings about XGrammar-2:

## Overview

XGrammar-2 is a structured generation engine for dynamic agentic workloads. The paper by Li et al. (arXiv 2026) proposes XGrammar 2, a highly optimized structured generation engine for agentic LLMs.

## Key Components

The paper introduces several important components:

1. **TagDispatch**: A new dynamic dispatching semantics, TagDispatch, is designed to efficiently support intra-request dynamism. TagDispatch partitions decoding into two modes: dispatching and dispatched. Decoding starts in the dispatching mode, where the engine accepts ordinary text while continuously matching registered tags. Once a tag is matched, the engine switches to the dispatched mode and constrains subsequent decoding with the corresponding sub-grammar. After that sub-grammar completes, decoding returns to the dispatching mode. If a stop string is matched in the dispatching mode, TagDispatch exits.

2. **Mask Callback/Token Mask Cache**: XGrammar-2 improves efficiency with an Earley-based adaptive token mask cache, just-in-time compilation, and repetition state compression.

3. **Cross-Grammar Cache**: A cross-grammar caching algorithm based on the Earley parser is designed to handle inter-request dynamism.

## Performance

Experiments show that XGrammar-2 achieves over 6 times faster compilation than prior structured generation engines, and incurs near-zero end-to-end overhead in modern LLM serving systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e907d08c-e107-42fc-ac98-e4739d63e3fe",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "03212b3d-61ef-4ea4-bbdb-a08ffe8adc20",
  "sourceToolAssistantUUID": "e907d08c-e107-42fc-ac98-e4739d63e3fe",
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

_source line 15 · 2026-05-11T23:05:20.160Z_

Good, I've confirmed the paper exists. Now let me fetch the actual arXiv abstract page and the paper's HTML to verify specific details like authors, the `mask_callback()` interface, and exact performance numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03212b3d-61ef-4ea4-bbdb-a08ffe8adc20",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011Cawcr3gPpftNc6tidWES8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "793442c1-c975-429b-b231-f11b0b2e21cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K91L9ePvWJ5WFxPsAaU3Lh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 956,
      "cache_creation_input_tokens": 2804,
      "cache_read_input_tokens": 10853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2804,
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

_source line 16 · 2026-05-11T23:05:22.654Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D5FvFiXtUxJ2DscJhtGwW7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.04426",
  "prompt": "Extract the full list of authors, the submission date, the abstract, and any mentions of mask_callback, TagDispatch, performance numbers (especially latency overhead per step), and which serving engines adopted XGrammar-2."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "793442c1-c975-429b-b231-f11b0b2e21cf",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011Cawcr3gPpftNc6tidWES8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93671596-af9d-4112-ba1d-95796d4728f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K91L9ePvWJ5WFxPsAaU3Lh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 956,
      "cache_creation_input_tokens": 2804,
      "cache_read_input_tokens": 10853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2804,
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

_source line 17 · 2026-05-11T23:05:24.784Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AFoDJX9omeGSKBvLCznF1r`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.04426v2",
  "prompt": "Search for any mention of 'mask_callback' in the text. Also find mentions of TagDispatch interface details, per-step latency overhead numbers (especially anything about <10ms/step), and which serving engines (vLLM, SGLang, TensorRT-LLM) are mentioned as having adopted XGrammar-2 as a default backend. Extract exact quotes if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93671596-af9d-4112-ba1d-95796d4728f1",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011Cawcr3gPpftNc6tidWES8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7eb3c1fa-05fb-44d5-94c2-24efd5b197fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K91L9ePvWJ5WFxPsAaU3Lh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 956,
      "cache_creation_input_tokens": 2804,
      "cache_read_input_tokens": 10853,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 956,
          "output_tokens": 329,
          "cache_read_input_tokens": 10853,
          "cache_creation_input_tokens": 2804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2804,
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

_source line 18 · 2026-05-11T23:05:27.725Z_

<details><summary>↩ Tool result · `toolu_01D5FvFiXtUxJ2DscJhtGwW7`</summary>

```text
# XGrammar-2 Paper Summary

**Authors:**
Linzhang Li, Yixin Dong, Guanjie Wang, Ziyi Xu, Alexander Jiang, Tianqi Chen

**Submission Date:**
Initially submitted January 7, 2026; revised version released March 26, 2026

**Abstract:**
"Modern LLM agents increasingly rely on dynamic structured generation, such as tool calling and response protocols" with varying structures across and within requests. The paper introduces mechanisms for dynamic structural dispatching and cross-grammar cache reuse, achieving "over 6x faster compilation than prior structured generation engines, and incurs near-zero end-to-end overhead."

**Key Technical Components Found:**
- TagDispatch for dynamic structural dispatching
- Cross-Grammar Cache for substructure-level reuse
- Earley-based adaptive token mask cache
- Just-in-time compilation and repetition state compression

**Not Found in Content:**
- No mention of `mask_callback` 
- No specific per-step latency overhead numbers
- No identification of which serving engines adopted XGrammar-2

The document provided is the arXiv abstract page rather than the full paper, limiting availability of detailed implementation specifics and empirical results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93671596-af9d-4112-ba1d-95796d4728f1",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "654ac46c-769d-4a54-96b6-83b73db9e68d",
  "sourceToolAssistantUUID": "93671596-af9d-4112-ba1d-95796d4728f1",
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

_source line 19 · 2026-05-11T23:05:30.166Z_

<details><summary>↩ Tool result · `toolu_01AFoDJX9omeGSKBvLCznF1r`</summary>

```text
# Search Results for XGrammar-2 Document

## mask_callback
No mentions of 'mask_callback' found in the provided text.

## TagDispatch Interface Details
The document describes TagDispatch as a grammar construct with these characteristics:

**Core Definition:** "TagDispatch is parameterized by (i) a list of tag–grammar pairs (ti,Gi), where emitting tag ti dispatches decoding to sub-grammar Gi, and (ii) a set of stop strings stop_strs that terminate dispatching."

**Operational Modes:** The text explains it "partitions decoding into two modes: _dispatching_ and _dispatched_. Decoding starts in the dispatching mode, where the engine accepts ordinary text while continuously matching registered tags."

**Implementation:** Uses an "Aho–Corasick automaton (AC automaton) to match multiple tags simultaneously."

## Per-Step Latency Overhead
The document does not provide specific per-step latency measurements below 10ms. Section 4.2 reports per-token overhead in microseconds (μs) rather than milliseconds, with XGrammar-2 showing advantages over competitors like llguidance (250+ μs overhead).

## Serving Engine Adoption
The text states: "We have incorporated XGrammar-2 into open-source serving frameworks such as SGLang and vLLM." TensorRT-LLM is mentioned only in acknowledgments, not as an adopter of XGrammar-2 as a default backend.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eb3c1fa-05fb-44d5-94c2-24efd5b197fd",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "5084617a-42cf-4937-bac8-94a71b33fcc4",
  "sourceToolAssistantUUID": "7eb3c1fa-05fb-44d5-94c2-24efd5b197fd",
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

_source line 20 · 2026-05-11T23:05:33.898Z_

Now let me fetch the MLC blog post and check if `mask_callback` is mentioned anywhere, and also look at the GitHub repo for API details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5084617a-42cf-4937-bac8-94a71b33fcc4",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011Cawcs5GRabHY4M9z3qVGW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08d635f5-92de-4af7-bc02-1d9143c288c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMz7VNkitELZkCzpg9xSQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 13657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 21 · 2026-05-11T23:05:35.931Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SKVgxqDEJzZoap2HSK7jgD`</summary>

```json
{
  "url": "https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation",
  "prompt": "Search for any mention of 'mask_callback' API or interface. Also look for TagDispatch API details, per-step latency numbers, and which frameworks adopted XGrammar-2 as default. Extract any code examples showing the API."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08d635f5-92de-4af7-bc02-1d9143c288c1",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011Cawcs5GRabHY4M9z3qVGW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec101586-4b73-4644-b51a-756c96a468b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMz7VNkitELZkCzpg9xSQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 13657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 22 · 2026-05-11T23:05:36.360Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KqDzK6qmYSLVfJRBUBqYQi`</summary>

```json
{
  "query": "\"XGrammar\" \"mask_callback\" API interface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec101586-4b73-4644-b51a-756c96a468b2",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011Cawcs5GRabHY4M9z3qVGW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e85d58b2-b06b-43a7-96b2-ef2eb86e9d40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMz7VNkitELZkCzpg9xSQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 13657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2074,
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

_source line 23 · 2026-05-11T23:05:36.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Z9ExTeAtHkDyMwnqt7bas`</summary>

```json
{
  "query": "XGrammar-2 \"10ms\" OR \"per-step\" OR \"per step\" overhead latency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e85d58b2-b06b-43a7-96b2-ef2eb86e9d40",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011Cawcs5GRabHY4M9z3qVGW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f0bfa90-5525-4858-8167-e925b3bde497",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMz7VNkitELZkCzpg9xSQq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2074,
      "cache_read_input_tokens": 13657,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 13657,
          "cache_creation_input_tokens": 2074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2074,
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

_source line 24 · 2026-05-11T23:05:40.001Z_

<details><summary>↩ Tool result · `toolu_01SKVgxqDEJzZoap2HSK7jgD`</summary>

```text
# Search Results for XGrammar-2 Documentation

Based on my review of the provided content, here are my findings:

## mask_callback API
No mention of a `mask_callback` API or interface appears in this document.

## TagDispatch API
No TagDispatch API details are present in the provided content.

## Per-Step Latency Numbers
The document does not include per-step latency measurements. It references "end-to-end request latency" but provides only aggregate figures: "the Structural Tag adds minimal latency overhead" without specific per-step breakdowns.

## Framework Adoption as Default
The document states that XGrammar-2 integrates with four serving engines: "SGLang, vLLM, TensorRT-LLM, and MLC-LLM integrate it for strict tool calling," but does not specify which frameworks adopted it as their default configuration.

## Code Example
One API example is provided showing OpenAI-compatible response format usage:

> "response = client.chat.completions.create(model="deepseek-ai/DeepSeek-V4", messages=[...], extra_body={"response_format": {"type": "structural_tag"..."

This demonstrates how to pass custom Structural Tag formats through serving engine APIs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec101586-4b73-4644-b51a-756c96a468b2",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "4de15122-827c-4fb4-9b94-9c7f0a8b788b",
  "sourceToolAssistantUUID": "ec101586-4b73-4644-b51a-756c96a468b2",
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

_source line 25 · 2026-05-11T23:05:41.143Z_

<details><summary>↩ Tool result · `toolu_016Z9ExTeAtHkDyMwnqt7bas`</summary>

```text
Web search results for query: "XGrammar-2 "10ms" OR "per-step" OR "per step" overhead latency"

Links: [{"title":"Guided Decoding Performance on vLLM and SGLang - The official SqueezeBits Tech blog","url":"https://blog.squeezebits.com/guided-decoding-performance-vllm-sglang"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.15100v3"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://openreview.net/pdf?id=rjQfX0YgDl"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426v2"},{"title":"XGrammar 2: High-Performance Grammar Systems","url":"https://www.emergentmind.com/topics/xgrammar-2"},{"title":"GitHub - guidance-ai/llguidance: Super-fast Structured Outputs · GitHub","url":"https://github.com/guidance-ai/llguidance"},{"title":"For reference, sound travels 0.343 meters per millisecond, so 10ms latency is th... | Hacker News","url":"https://news.ycombinator.com/item?id=19445713"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"[Literature Review] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://www.themoonlight.io/en/review/xgrammar-flexible-and-efficient-structured-generation-engine-for-large-language-models"},{"title":"XGrammar: Efficient, flexible and portable structured generation engine …","url":"https://jimmysong.io/ai/xgrammar/"}]

Based on the search results, I found relevant information about XGrammar-2 and its per-step overhead latency:

XGrammar-2 achieves less than 10 ms per mask generation step on CPU+GPU evaluation, netting less than 6% total overhead due to overlap with GPU LLM execution.

The search results also indicate that XGrammar-2 achieves over 6× tool-calling compilation speed improvement compared to prior state-of-the-art methods, while introducing near-zero latency overhead.

These metrics demonstrate that XGrammar-2 maintains very low per-step latency overhead, staying under the 10ms threshold even when accounting for mask generation during the decoding process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f0bfa90-5525-4858-8167-e925b3bde497",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "b4809017-05b8-46c6-bace-de8042e2c4c2",
  "sourceToolAssistantUUID": "8f0bfa90-5525-4858-8167-e925b3bde497",
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

_source line 26 · 2026-05-11T23:05:42.590Z_

<details><summary>↩ Tool result · `toolu_01KqDzK6qmYSLVfJRBUBqYQi`</summary>

```text
Web search results for query: ""XGrammar" "mask_callback" API interface"

Links: [{"title":"Advanced Topics of the Structural Tag — XGrammar 0.1.27 documentation","url":"https://xgrammar.mlc.ai/docs/tutorials/advanced_structural_tag.html"},{"title":"XGrammar Python API — XGrammar 0.1.30 documentation","url":"https://xgrammar.mlc.ai/docs/api/python/index.html"},{"title":"Releases · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/releases"},{"title":"Workflow of XGrammar — XGrammar 0.1.31 documentation","url":"https://xgrammar.mlc.ai/docs/tutorials/workflow_of_xgrammar.html"},{"title":"XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs","url":"https://arxiv.org/html/2601.04426v2"},{"title":"Catalyst: XGrammar","url":"https://catalyst.cs.cmu.edu/projects/xgrammar.html"},{"title":"MLC | XGrammar-2: Fast and Customizable Structured Generation for Tool Calling and Agents","url":"https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation"},{"title":"[Feature]: Allow user selection of structured output (xgrammar) backend for bitmask application · Issue #37650 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/37650"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"(PDF) XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://www.researchgate.net/publication/386093501_XGrammar_Flexible_and_Efficient_Structured_Generation_Engine_for_Large_Language_Models"}]

Based on the search results, I found relevant information about XGrammar's `mask_callback` and related API interfaces:

## XGrammar `mask_callback` API Interface

The search results don't contain specific documentation about a `mask_callback` function, but they do reveal the core mask generation API in XGrammar:

### Key Mask Generation Methods

XGrammar's `GrammarMatcher` handles the logic of matching LLM output to the structure and generating the token mask. In each step, it will accept the last token generated by the LLM with `accept_token`, and then generate the mask with `fill_next_token_bitmask`.

### Token Bitmask API

The function `xgr.apply_token_bitmask_inplace` from xgrammar supports different backends (e.g., "auto", "cpu", "cuda", "triton", "torch_compile", "torch_native").

### Bitmask Operations

XGrammar's Python API includes bitmask operations such as: `allocate_token_bitmask()`, `apply_token_bitmask_inplace()`, `reset_token_bitmask()`, and `get_bitmask_shape()`.

The search results focus on the core mask generation workflow rather than a specific `mask_callback` parameter. For more detailed documentation on the `mask_callback` specifically, you may want to check the official XGrammar documentation at xgrammar.mlc.ai or the GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e85d58b2-b06b-43a7-96b2-ef2eb86e9d40",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "680b332e-d358-449f-9958-5be30469209a",
  "sourceToolAssistantUUID": "e85d58b2-b06b-43a7-96b2-ef2eb86e9d40",
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

_source line 27 · 2026-05-11T23:05:45.850Z_

Let me fetch the XGrammar Python API docs and the paper's HTML to check for `mask_callback` specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "680b332e-d358-449f-9958-5be30469209a",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcszPGJfxbNdA3duMbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "839d1d70-a238-42c0-8a46-945bec527b8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QG9QBr6n832Rch41Lnqg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 15731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1507,
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

_source line 28 · 2026-05-11T23:05:47.265Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MQyUPRaQ52UWEGVZNqRY5Z`</summary>

```json
{
  "url": "https://xgrammar.mlc.ai/docs/api/python/index.html",
  "prompt": "Search for any function or parameter named 'mask_callback'. List all public API functions and classes, especially anything related to callbacks or mask generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "839d1d70-a238-42c0-8a46-945bec527b8c",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcszPGJfxbNdA3duMbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30bf465e-1c99-4206-a516-5106c794527b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QG9QBr6n832Rch41Lnqg2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 15731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1507,
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

_source line 29 · 2026-05-11T23:05:48.935Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0183nekxUWpSgaNzMWmb29PS`</summary>

```json
{
  "url": "https://xgrammar.mlc.ai/docs/tutorials/advanced_structural_tag.html",
  "prompt": "Search for any mention of 'mask_callback'. Also extract any API examples showing TagDispatch or structural tag usage. List all function names and class names mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30bf465e-1c99-4206-a516-5106c794527b",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcszPGJfxbNdA3duMbz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad87f6ac-eab3-4486-b02a-67c7bb5c3527",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QG9QBr6n832Rch41Lnqg2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 15731,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1507
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 701,
          "output_tokens": 250,
          "cache_read_input_tokens": 15731,
          "cache_creation_input_tokens": 1507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1507,
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

_source line 30 · 2026-05-11T23:05:49.138Z_

<details><summary>↩ Tool result · reported error · `toolu_0183nekxUWpSgaNzMWmb29PS`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad87f6ac-eab3-4486-b02a-67c7bb5c3527",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "db2cc8f8-b584-41e0-b10f-1ed107c0b47d",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "ad87f6ac-eab3-4486-b02a-67c7bb5c3527",
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

_source line 31 · 2026-05-11T23:05:50.338Z_

<details><summary>↩ Tool result · `toolu_01MQyUPRaQ52UWEGVZNqRY5Z`</summary>

```text
# Search Results for 'mask_callback'

Based on the provided documentation content, **there are no references to 'mask_callback'** in this XGrammar Python API documentation page.

## Related Public APIs for Mask Operations

The documentation does list several mask-related public functions under "Bitmask Operations":

- `allocate_token_bitmask()`
- `apply_token_bitmask_inplace()`
- `reset_token_bitmask()`
- `get_bitmask_shape()`
- `bitmask_dtype`

Additionally, testing utilities include mask-related functions like:
- `bool_mask_to_bitmask()`
- `bitmask_to_bool_mask()`
- `_get_masked_tokens_from_bitmask()`
- `_is_single_token_bitmask()`

However, none of these appear to be callback-related functions. The documentation excerpt provided does not contain callback mechanism APIs or a `mask_callback` function.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30bf465e-1c99-4206-a516-5106c794527b",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "49d747a1-03b8-4862-8c63-aefd3c17f8c9",
  "sourceToolAssistantUUID": "30bf465e-1c99-4206-a516-5106c794527b",
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

_source line 32 · 2026-05-11T23:05:53.143Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SyZF95Ak8fBR2vkSKqhQpp`</summary>

```json
{
  "query": "XGrammar-2 TensorRT-LLM default backend integration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49d747a1-03b8-4862-8c63-aefd3c17f8c9",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawctZWKi9q9UoK68MmGZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "720f0981-55bc-40aa-b734-bc0de9b9f28e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lx7izvSGbucaa8nXXQdqBS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 17238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1216,
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

_source line 33 · 2026-05-11T23:05:54.991Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WnFdbmWiM8yvzrVyxiasW8`</summary>

```json
{
  "url": "https://github.com/mlc-ai/xgrammar",
  "prompt": "Check the README for mentions of mask_callback, TagDispatch, and which serving engines (vLLM, SGLang, TensorRT-LLM) have adopted XGrammar or XGrammar-2 as their default backend. Look for any API called mask_callback."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "720f0981-55bc-40aa-b734-bc0de9b9f28e",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawctZWKi9q9UoK68MmGZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da4aa450-8fd6-47cc-894a-826b9872cd2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lx7izvSGbucaa8nXXQdqBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1216,
      "cache_read_input_tokens": 17238,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1216
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 39,
          "output_tokens": 202,
          "cache_read_input_tokens": 17238,
          "cache_creation_input_tokens": 1216,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1216,
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

_source line 34 · 2026-05-11T23:06:00.435Z_

<details><summary>↩ Tool result · `toolu_01SyZF95Ak8fBR2vkSKqhQpp`</summary>

```text
Web search results for query: "XGrammar-2 TensorRT-LLM default backend integration 2025 2026"

Links: [{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"xgrammar/README.md at main · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/blob/main/README.md"},{"title":"Release Notes — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/release-notes.html"},{"title":"xgrammar · PyPI","url":"https://pypi.org/project/xgrammar/"},{"title":"API Reference — tensorrt_llm documentation","url":"https://nvidia.github.io/TensorRT-LLM/llm-api/reference.html"},{"title":"Welcome to TensorRT LLM’s Documentation! — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/"},{"title":"API Reference — TensorRT LLM","url":"https://nvidia.github.io/TensorRT-LLM/latest/llm-api/reference.html"},{"title":"Releases · NVIDIA/TensorRT-LLM","url":"https://github.com/NVIDIA/TensorRT-LLM/releases"},{"title":"GitHub - NVIDIA/TensorRT-LLM: TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way. · GitHub","url":"https://github.com/NVIDIA/TensorRT-LLM"},{"title":"GitHub - triton-inference-server/tensorrtllm_backend: The Triton TensorRT-LLM Backend · GitHub","url":"https://github.com/triton-inference-server/tensorrtllm_backend"}]

Based on the search results, here's what I found about XGrammar-2 and TensorRT-LLM integration:

## XGrammar-2 Release and Integration

XGrammar-2 was released in May 2026, marking a significant update to the XGrammar library. XGrammar is the default structured generation backend for most LLM inference engines, including vLLM, SGLang, TensorRT-LLM, and MLC-LLM.

## TensorRT-LLM Integration Timeline

The integration of XGrammar with TensorRT-LLM occurred earlier in 2025. XGrammar was officially integrated into TensorRT-LLM in January 2025. TensorRT-LLM added guided decoding support through XGrammar integration.

## Current Integration Status

The dependent xgrammar version is updated to 0.1.21 in the latest TensorRT-LLM release. The guided decoding backend parameter in TensorRT-LLM supports both 'xgrammar' and 'llguidance' options, with llguidance supported in PyTorch backend only.

The integration enables structured generation capabilities in TensorRT-LLM, allowing users to constrain model outputs to specific formats like JSON, regex patterns, and context-free grammars.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "720f0981-55bc-40aa-b734-bc0de9b9f28e",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "753e9f5b-a059-4f2a-89db-9abd54e4937f",
  "sourceToolAssistantUUID": "720f0981-55bc-40aa-b734-bc0de9b9f28e",
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

_source line 35 · 2026-05-11T23:06:03.946Z_

<details><summary>↩ Tool result · `toolu_01WnFdbmWiM8yvzrVyxiasW8`</summary>

```text
# Analysis of XGrammar README

Based on the provided GitHub page content, I cannot find mentions of:

- **mask_callback** - This API is not referenced anywhere in the README
- **TagDispatch** - This term does not appear in the documentation excerpt

## Serving Engine Adoption

The README clearly documents which inference engines have integrated XGrammar:

**Confirmed adoptions as default backend:**
- vLLM (integrated November 2024)
- SGLang (integrated November 2024)
- TensorRT-LLM (integrated January 2025)
- MLC-LLM (integrated November 2024)

The document also mentions XGrammar-2's integration into additional platforms: OpenVINO GenAI, Modular's MAX, and Mirai.

The README states: *"It is the default structured generation backend for most LLM inference engines, including vLLM, SGLang, TensorRT-LLM, and MLC-LLM."*

The specific APIs you're searching for (mask_callback and TagDispatch) are not documented in this README section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da4aa450-8fd6-47cc-894a-826b9872cd2b",
  "isSidechain": true,
  "promptId": "235e36ff-3a2f-4ca2-8e07-313f58437f1e",
  "agentId": "a0a3ddb929492799e",
  "type": "user",
  "uuid": "e298763d-e420-4cbb-a67f-5b56c3c5b213",
  "sourceToolAssistantUUID": "da4aa450-8fd6-47cc-894a-826b9872cd2b",
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

_source line 36 · 2026-05-11T23:06:38.774Z_

Now I have comprehensive findings. Here is my report:

---

## Verification Results for XGrammar-2 Claims

### Claim 1: Does XGrammar-2 exist as a paper (arXiv Jan 2026, Li et al.)?

**VERIFIED -- TRUE.** The paper exists at [arXiv:2601.04426](https://arxiv.org/abs/2601.04426) with the title "XGrammar-2: Efficient Dynamic Structured Generation Engine for Agentic LLMs." It was submitted on **January 7, 2026**, with a revised version (v2) on March 26, 2026. The authors are **Linzhang Li, Yixin Dong, Guanjie Wang, Ziyi Xu, Alexander Jiang, and Tianqi Chen**. The claim of "Li et al." is accurate.

---

### Claim 2: Does it support mask_callback() or TagDispatch interfaces?

**PARTIALLY TRUE / PARTIALLY FALSE.**

- **TagDispatch -- VERIFIED.** TagDispatch is a real, core component of XGrammar-2. The paper defines it as: "TagDispatch is parameterized by (i) a list of tag-grammar pairs (ti, Gi), where emitting tag ti dispatches decoding to sub-grammar Gi, and (ii) a set of stop strings stop_strs that terminate dispatching." It uses an Aho-Corasick automaton for simultaneous tag matching.

- **mask_callback() -- NOT FOUND.** I searched the arXiv paper (both abstract and full HTML), the official XGrammar Python API documentation at [xgrammar.mlc.ai](https://xgrammar.mlc.ai/docs/api/python/index.html), the GitHub README, and the MLC blog post. There is **no function or interface called `mask_callback()`** anywhere in XGrammar-2's public API or paper. The actual mask-related APIs are `fill_next_token_bitmask()`, `allocate_token_bitmask()`, `apply_token_bitmask_inplace()`, etc. The claim about `mask_callback()` appears to be fabricated or confused with the actual API names.

---

### Claim 3: Is it actually the default backend for vLLM/SGLang/TensorRT-LLM?

**MOSTLY TRUE, with nuance.**

- **XGrammar (v1)** is confirmed as the default structured generation backend for vLLM, SGLang, TensorRT-LLM, and MLC-LLM. The GitHub README explicitly states this. Integration dates: SGLang (Nov 2024), vLLM (Dec 2024), TensorRT-LLM (Jan 2025).

- **XGrammar-2** specifically: The paper states it has been "incorporated into open-source serving frameworks such as **SGLang and vLLM**." The MLC blog post mentions SGLang, vLLM, TensorRT-LLM, and MLC-LLM integrate it for tool calling. However, TensorRT-LLM is only mentioned in the paper's acknowledgments, not as a confirmed adopter of XGrammar-2 specifically. TensorRT-LLM also supports `llguidance` as an alternative backend.

- So the claim is **accurate for SGLang and vLLM** (XGrammar-2 adopted), **partially accurate for TensorRT-LLM** (XGrammar v1 is integrated; XGrammar-2 adoption is mentioned in the blog but not confirmed in the paper itself).

---

### Claim 4: Does it achieve <10ms/step overhead?

**TRUE, and actually better than claimed.** The paper reports per-token overhead in **microseconds (us)**, not milliseconds. XGrammar-2's per-token mask generation overhead is on the order of ~250 us or less, which is well under 1ms, let alone 10ms. The paper describes this as "near-zero end-to-end overhead" and reports less than 6% total overhead due to overlap with GPU LLM execution. The claim of "<10ms/step" is technically correct but significantly understates the actual performance -- the real overhead is roughly **10-100x better** than the "<10ms" claim suggests.

---

## Summary

| Claim | Verdict |
|-------|---------|
| Paper exists (arXiv Jan 2026, Li et al.) | **True** -- arXiv:2601.04426, Jan 7, 2026 |
| Supports `mask_callback()` | **False** -- no such API exists; actual API uses `fill_next_token_bitmask()` |
| Supports `TagDispatch` | **True** -- core component of XGrammar-2 |
| Default backend for vLLM/SGLang/TensorRT-LLM | **Mostly true** for XGrammar v1; confirmed for SGLang/vLLM with XGrammar-2 |
| Achieves <10ms/step overhead | **True** -- actually achieves sub-millisecond (~250us) per-token overhead |

Sources:
- [XGrammar-2 arXiv Paper (2601.04426)](https://arxiv.org/abs/2601.04426)
- [XGrammar-2 Full HTML Paper](https://arxiv.org/html/2601.04426v2)
- [MLC Blog: XGrammar-2 Announcement](https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation)
- [XGrammar GitHub Repository](https://github.com/mlc-ai/xgrammar)
- [XGrammar Python API Documentation](https://xgrammar.mlc.ai/docs/api/python/index.html)
- [XGrammar PyPI Page](https://pypi.org/project/xgrammar/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e298763d-e420-4cbb-a67f-5b56c3c5b213",
  "isSidechain": true,
  "agentId": "a0a3ddb929492799e",
  "requestId": "req_011CawcuZi1Zx4fJwzisgF9x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcf32b23-5fa1-4fb4-86bf-ab2723402fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861e42fe-2d6b-4cb7-aa25-22c7b0b8bdd2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A9gaGj8hGnJr6pFg9un9z3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 18454,
      "output_tokens": 1432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1432,
          "cache_read_input_tokens": 18454,
          "cache_creation_input_tokens": 1406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1406,
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
