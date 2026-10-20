# Research conversation: Search for the current state of SGLang's hybrid model support for architectures like Gated DeltaNet (Qwen3.5/3.6 series)

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac26f3c0af4ac1047.jsonl`
- **Structured JSON:** [`2a8cae558e2f7b5fbb91.json`](../../sessions/2a/2a8cae558e2f7b5fbb91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

25 recorded events

### User

_source line 1 · 2026-05-10T20:35:31.427Z_

Search for the current state of SGLang's hybrid model support for architectures like Gated DeltaNet (Qwen3.5/3.6 series). Specifically:

1. **SGLang GitHub issue #12867** - Look for roadmap items including prefix caching adaptation, speculative decoding, and GDN kernel optimization
2. Current state of hybrid (attention + recurrent) model support in SGLang
3. vLLM's alternative hybrid model support and its limitations (issue #41560 mentioned)
4. Any other serving frameworks that support hybrid architectures

Use WebSearch with queries like:
- "SGLang hybrid model Gated DeltaNet support GitHub issue"
- "SGLang Qwen3.5 Qwen3.6 hybrid architecture support"
- "vLLM hybrid model attention recurrent support limitations"
- "SGLang dual memory pool transformer recurrent"
- "Gated DeltaNet inference serving framework support 2026"

Report back with: the current state of SGLang hybrid support, what works and what's pending, and any alternative options for serving Qwen3.6-27B.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "30a13890-72b0-485e-a0a6-beb4175d2d0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:35:31.429Z_

```json
{
  "parentUuid": "30a13890-72b0-485e-a0a6-beb4175d2d0a",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
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
  "uuid": "9897eede-62a7-493b-aaed-9c8e1804f76b",
  "timestamp": "2026-05-10T20:35:31.429Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T20:35:33.889Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bb192WqrK3zQoaPWuBDN7U`</summary>

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
  "parentUuid": "9897eede-62a7-493b-aaed-9c8e1804f76b",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXcpfrqCXXZxFvWpAM1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bc514ae-aa7e-4c4c-99b5-83470749ffdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtxqdSVokKuSqY1zRQDHSZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 814,
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

_source line 4 · 2026-05-10T20:35:33.892Z_

<details><summary>↩ Tool result · `toolu_01Bb192WqrK3zQoaPWuBDN7U`</summary>

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
  "parentUuid": "5bc514ae-aa7e-4c4c-99b5-83470749ffdf",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "cb52e455-4639-4d70-85d5-493ebbcb588e",
  "sourceToolAssistantUUID": "5bc514ae-aa7e-4c4c-99b5-83470749ffdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T20:35:36.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FH8tW3wQowWQSqMcpSab4P`</summary>

```json
{
  "query": "SGLang hybrid model Gated DeltaNet support GitHub issue 12867"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb52e455-4639-4d70-85d5-493ebbcb588e",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXd1UEnS1sj5uDrxjZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06c6422c-e1cd-4cd0-b43d-f032f310f71e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZ6FxDTMBLeCBro89dGY4S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T20:35:37.444Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TyvyJ2oEePdu5K4WfsYRxi`</summary>

```json
{
  "query": "SGLang Qwen3.5 Qwen3.6 hybrid architecture support 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06c6422c-e1cd-4cd0-b43d-f032f310f71e",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXd1UEnS1sj5uDrxjZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "267c1e57-53f3-496a-a0c0-5f172fbabbaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZ6FxDTMBLeCBro89dGY4S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9037,
      "output_tokens": 176,
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
          "output_tokens": 176,
          "cache_read_input_tokens": 9037,
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

### Tool call

_source line 7 · 2026-05-10T20:35:37.466Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015xCxo7VLaW6ipSmZGphzFT`</summary>

```json
{
  "query": "vLLM hybrid model attention recurrent support limitations issue 41560"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "267c1e57-53f3-496a-a0c0-5f172fbabbaa",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXd1UEnS1sj5uDrxjZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cd1f644-4b41-4764-81bf-831cefcf0400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZ6FxDTMBLeCBro89dGY4S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9037,
      "output_tokens": 176,
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
          "output_tokens": 176,
          "cache_read_input_tokens": 9037,
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

_source line 8 · 2026-05-10T20:35:44.121Z_

<details><summary>↩ Tool result · `toolu_01TyvyJ2oEePdu5K4WfsYRxi`</summary>

```text
Web search results for query: "SGLang Qwen3.5 Qwen3.6 hybrid architecture support 2026"

Links: [{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen 3.5 Usage — SGLang","url":"https://docs.sglang.io/basic_usage/qwen3_5.html"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen3.6 - SGLang Documentation","url":"https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.6"},{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen/Qwen3.5-9B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-9B"},{"title":"Qwen3.5 | SGLang Cookbook","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.5"},{"title":"Qwen3.6 | SGLang Cookbook","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.6"},{"title":"Day 0 Support for Qwen3.6 on AMD Instinct GPUs","url":"https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-qwen3-6-on-amd-instinct-gpus.html"},{"title":"Day 0 Support for Qwen 3.5 on AMD Instinct GPUs","url":"https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-qwen-3-5-on-amd-instinct-gpus.html"}]

Based on the search results, here's what I found about SGLang support for Qwen3.5 and Qwen3.6 with hybrid architecture in 2026:

## Qwen3.5 and Qwen3.6 Hybrid Architecture Support

Both Qwen3.5 and Qwen3.6 feature efficient hybrid architecture with Gated Delta Networks combined with sparse Mixture-of-Experts.

### SGLang Support

Qwen3.6 is supported by multiple inference frameworks, with SGLang demonstrated as a fast serving framework for large language models and vision language models. 

For **Qwen3.5**: SGLang from the main branch of the open-source repository is required for Qwen3.5, which can be installed using the command: `uv pip install 'git+https://github.com/sgl-project/sglang.git#subdirectory=python&egg=sglang[all]'`

For **Qwen3.6**: sglang>=0.5.10 is recommended for Qwen3.6

### Hybrid Architecture Details

Qwen3.5 features a Gated Delta Networks combined with sparse Mixture-of-Experts architecture (397B total parameters, 17B activated), delivering high-throughput inference with minimal latency. 

Qwen3.6 features a Gated Delta Networks combined with sparse Mixture-of-Experts architecture (35B total parameters, 3B activated).

Both models have full SGLang integration with support for reasoning parsers, tool calling, and optimization strategies for the hybrid architecture across both NVIDIA and AMD GPU platforms in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "267c1e57-53f3-496a-a0c0-5f172fbabbaa",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "1b41316b-4434-4906-a7e8-5b80d67d12d2",
  "sourceToolAssistantUUID": "267c1e57-53f3-496a-a0c0-5f172fbabbaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T20:35:44.360Z_

<details><summary>↩ Tool result · `toolu_015xCxo7VLaW6ipSmZGphzFT`</summary>

```text
Web search results for query: "vLLM hybrid model attention recurrent support limitations issue 41560"

Links: [{"title":"[Bug] turboquant_4bit_nc KV cache fails unify_kv_cache_spec_page_size assertion on hybrid Qwen3_5 (GDN + attention) architecture · Issue #41560 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/41560"},{"title":"Hybrid Models as First-Class Citizens in vLLM – PyTorch","url":"https://pytorch.org/blog/hybrid-models-as-first-class-citizens-in-vllm/"},{"title":"Releases · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/releases"},{"title":"[Bug]: KV Cache offloading fails for hybrid attention models (due to missing support for SupportsHMA) - fix available upstream · Issue #15 · 1CatAI/1Cat-vLLM","url":"https://github.com/1CatAI/1Cat-vLLM/issues/15"},{"title":"Issues · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues"},{"title":"Supported Models - vLLM","url":"https://docs.vllm.ai/en/v0.10.2/models/supported_models.html"},{"title":"[RFC]: Hybrid Memory Allocator · Issue #11382 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/11382"},{"title":"Supported Models — vLLM","url":"https://docs.vllm.ai/en/v0.8.4/models/supported_models.html"},{"title":"Troubleshooting - vLLM","url":"https://docs.vllm.ai/en/latest/usage/troubleshooting/"},{"title":"GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub","url":"https://github.com/vllm-project/vllm"}]

Based on the search results, I found information about issue #41560 related to vLLM's hybrid model support:

## Issue #41560 Summary

The `--kv-cache-dtype turboquant_4bit_nc` causes a deterministic AssertionError at engine init when used with hybrid Qwen3_5ForConditionalGeneration models (Qwen3.6 27B family).

### The Problem

On a hybrid model, the GDN/mamba layer page geometry differs from attention layer page geometry. The turboquant_4bit_nc page-size calculation does not account for the hybrid page-size variance after padding, causing the assertion to fail.

More specifically, the `unify_kv_cache_spec_page_size` function walks all layer KV specs and asserts that turboquant_4bit_nc page-size bytes are compatible with the max page-size across all specs after a 0.06% padding step.

### Workarounds

With fp8_e5m2 or auto (bfloat16) KV dtype, this assertion passes cleanly on the same model, indicating these alternative cache dtypes work without issues on hybrid architectures.

### Consistency Issue

The crash is consistent and unrecoverable — no combination of --max-model-len, --gpu-memory-utilization, or --max-num-seqs resolves it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cd1f644-4b41-4764-81bf-831cefcf0400",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "f336b4f3-5fa1-4568-b4f5-700d350ad38c",
  "sourceToolAssistantUUID": "4cd1f644-4b41-4764-81bf-831cefcf0400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:35:45.238Z_

<details><summary>↩ Tool result · `toolu_01FH8tW3wQowWQSqMcpSab4P`</summary>

```text
Web search results for query: "SGLang hybrid model Gated DeltaNet support GitHub issue 12867"

Links: [{"title":"[Feature] Hybrid Linear LLMs support · Issue #12867 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/12867"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"Releases · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/releases"},{"title":"SGLang Documentation — SGLang","url":"https://sgl-project.github.io/"},{"title":"Supported Models | SGLang","url":"https://www.sglang.io/models"},{"title":"Gated DeltaNet | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llms-from-scratch/ch04/08_deltanet/"},{"title":"Issues · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues"},{"title":"sgl-project · GitHub","url":"https://github.com/sgl-project"},{"title":"GitHub - NVlabs/GatedDeltaNet: [ICLR 2025] Official PyTorch Implementation of Gated Delta Networks: Improving Mamba2 with Delta Rule · GitHub","url":"https://github.com/NVlabs/GatedDeltaNet"},{"title":"GitHub - mattbucci/m4-sglang-inference · GitHub","url":"https://github.com/mattbucci/m4-sglang-inference"}]

Based on the search results, I found information about GitHub issue #12867 in the SGLang repository:

## SGLang GitHub Issue #12867

Issue #12867 titled "[Feature] Hybrid Linear LLMs support" was opened on November 8, 2025 and addresses Hybrid Linear LLMs support as an important part that has gained widespread adoption, with examples including Qwen3-next and Kimi Linear.

The issue outlines several features that still need to be supported, including: prefix caching adaptation, page size > 1 support, overlap schedule support, storing mamba state every k steps/branch point, adaptation for kernels like shortconv, gdn, mamba1 with intermediate state storage, speculative decoding adaptation, and general speculative decoding adaptation.

Regarding Gated DeltaNet specifically, SGLang lists support for native vision-language models combining Gated DeltaNet (linear attention) with sparse MoE, indicating that work is underway to support these hybrid linear architectures in the SGLang framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c6422c-e1cd-4cd0-b43d-f032f310f71e",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "a1574a4a-c130-48b5-916f-4b6795b1f38b",
  "sourceToolAssistantUUID": "06c6422c-e1cd-4cd0-b43d-f032f310f71e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T20:35:48.817Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Q3ZdWFeurYinopizRuz1H`</summary>

```json
{
  "query": "SGLang dual memory pool transformer recurrent hybrid linear LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1574a4a-c130-48b5-916f-4b6795b1f38b",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXdqguLKry7Lpu1tvcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f10f970f-88dc-46ba-a90e-22286472c35e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3oNZbQeQxcVij81Ahn7aL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1910,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 10429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 902,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T20:35:48.883Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Psofn37MxjHhiXw1rXYEsP`</summary>

```json
{
  "query": "Gated DeltaNet inference serving framework support 2026 alternatives"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f10f970f-88dc-46ba-a90e-22286472c35e",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXdqguLKry7Lpu1tvcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1333ca9-d33f-4e8b-9ac6-f172609a7de9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3oNZbQeQxcVij81Ahn7aL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1910,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 10429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 902,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T20:35:49.572Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BASrWFiC31D8vNJVu1cZTZ`</summary>

```json
{
  "query": "SGLang issue 12867 prefix caching speculative decoding GDN kernel roadmap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1333ca9-d33f-4e8b-9ac6-f172609a7de9",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXdqguLKry7Lpu1tvcE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a72ecd04-1ec1-4737-bbba-441e166c56f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3oNZbQeQxcVij81Ahn7aL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1910,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 10429,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 902
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1910,
          "output_tokens": 170,
          "cache_read_input_tokens": 10429,
          "cache_creation_input_tokens": 902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 902,
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

_source line 14 · 2026-05-10T20:35:55.419Z_

<details><summary>↩ Tool result · `toolu_01BASrWFiC31D8vNJVu1cZTZ`</summary>

```text
Web search results for query: "SGLang issue 12867 prefix caching speculative decoding GDN kernel roadmap"

Links: [{"title":"[Feature] Hybrid Linear LLMs support · Issue #12867 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/12867"},{"title":"SGLang Documentation — SGLang","url":"https://sgl-project.github.io/"},{"title":"Releases · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/releases"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"SGLang Learning Series — Part 2: Speculative Decoding (Draft + Verify) in Practice | by Dharamendra Kumar | Medium","url":"https://medium.com/@dharamendra1314.kumar/sglang-learning-series-part-2-speculative-decoding-draft-verify-in-practice-aef8b36141fc"},{"title":"[Bug] cached_tokens Reports 0 with MTP/Speculative Decoding, Breaking Cache Hit Rate Metrics · Issue #20451 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/20451"},{"title":"Speculative Decoding — SGLang","url":"https://docs.sglang.ai/backend/speculative_decoding.html"},{"title":"Troubleshooting and Frequently Asked Questions — SGLang","url":"https://sgl-project.github.io/references/faq.html"},{"title":"Development Roadmap (2026 Q1) · Issue #12780 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/12780"},{"title":"Attention Backend — SGLang","url":"https://docs.sglang.io/advanced_features/attention_backend.html"}]

Based on the search results, I found information about SGLang issue #12867, which is about Hybrid Linear LLMs support opened on November 8, 2025. 

The issue outlines several features that need to be supported, including prefix caching adaptation, page size support, overlap schedule support, storing mamba state, kernel adaptations like shortconv, gdn, and mamba1, and speculative decoding adaptation.

The search results show that SGLang has been actively developing features related to prefix caching and speculative decoding. SGLang's core features include RadixAttention for prefix caching and speculative decoding among other optimizations. Additionally, the latest releases include Speculative Decoding V2 by default with overlap scheduling to hide CPU overhead, and Decode Radix Cache for PD Disaggregation to enable prefix caching in disaggregated deployments.

The GDN kernel mentioned in your query appears as one of the kernel adaptation targets for the Hybrid Linear LLMs support feature in issue #12867.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a72ecd04-1ec1-4737-bbba-441e166c56f0",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "51be6f32-ca87-4adb-9d9f-50ce473c7fa4",
  "sourceToolAssistantUUID": "a72ecd04-1ec1-4737-bbba-441e166c56f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T20:35:56.125Z_

<details><summary>↩ Tool result · `toolu_014Q3ZdWFeurYinopizRuz1H`</summary>

```text
Web search results for query: "SGLang dual memory pool transformer recurrent hybrid linear LLM"

Links: [{"title":"Hybrid Model Support | SGLang's Support Scheme for Hybrid Architecture Models like Mamba-Transformer - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/hybrid-model-support-%7C-sglangs-support-scheme-for-hybrid-architecture-models-like-mamba-transformer_602857"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"},{"title":"Hybrid Models Meet SGLang: More than Full Attention – PyTorch","url":"https://pytorch.org/blog/hybrid-models-meet-sglang-more-than-full-attention/"},{"title":"[Feature] Hybrid Linear LLMs support · Issue #12867 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/12867"},{"title":"SGLang: Fast Serving Framework for Large Language and Vision-Language Models on AMD Instinct GPUs — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/sglang/README.html"},{"title":"SGLang Documentation — SGLang","url":"https://sgl-project.github.io/"},{"title":"[Feature] KTransformers Integration to Support CPU/GPU Hybrid Inference for MoE Models · Issue #11425 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/11425"},{"title":"Efficiently Programming Large Language Models using SGLang","url":"https://arxiv.org/html/2312.07104v1"},{"title":"SGLang in Production: A Developer’s Guide to Structured Generation, RadixAttention, and Multi-Step LLM Pipelines","url":"https://www.runpod.io/articles/guides/blog-sglang-production-llm-pipelines"},{"title":"Releases · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/releases"}]

Based on the search results, here's what I found about SGLang's dual memory pool approach for hybrid model inference:

## SGLang's Dual Memory Pool for Hybrid Models

SGLang provides a dual memory-pool inference framework enabling efficient hybrid Transformer-Mamba model execution by resolving conflicting caching mechanisms.

### The Challenge

There is a fundamental conflict between Transformer's token-granularity caching and Mamba's request-granularity in-place update mechanism, which causes traditional optimization techniques such as prefix caching and speculative decoding to fail.

### The Solution

In SGLang, hybrid linear models separate the memory pool into two parts: Mamba pool and KV cache pool. More specifically, Mamba models maintain two separate memory pools: a paged KV pool for full attention layers and a Mamba pool for linear layers storing conv and temporal states.

Through the combined design of "multi-pool isolation + elastic scheduling," SGLang retains the benefits of fine-grained management tailored to different memory access patterns (large contiguous blocks vs. fine-grained dynamic allocation) while also gaining adaptability to dynamic workloads.

### Hybrid Model Support

Hybrid architectures interleave Transformer full-attention layers with Mamba-style state space model layers in an attempt to strike a balance between efficiency and performance. By leveraging linear attention, the KV cache memory consumption per request is bounded to a constant, and prefill latency can scale linearly with input length. This characteristic aligns well with real-world workloads, such as those in RAG queries, agentic tools, and thinking/reasoning patterns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f10f970f-88dc-46ba-a90e-22286472c35e",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "3e570e7e-82c3-45d6-999f-b2d1271b2df5",
  "sourceToolAssistantUUID": "f10f970f-88dc-46ba-a90e-22286472c35e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T20:35:56.721Z_

<details><summary>↩ Tool result · `toolu_01Psofn37MxjHhiXw1rXYEsP`</summary>

```text
Web search results for query: "Gated DeltaNet inference serving framework support 2026 alternatives"

Links: [{"title":"GitHub - NVlabs/GatedDeltaNet: [ICLR 2025] Official PyTorch Implementation of Gated Delta Networks: Improving Mamba2 with Delta Rule · GitHub","url":"https://github.com/NVlabs/GatedDeltaNet"},{"title":"[2604.19021] FG$^2$-GDN: Enhancing Long-Context Gated Delta Networks with Doubly Fine-Grained Control","url":"https://arxiv.org/abs/2604.19021"},{"title":"Qwen/Qwen3-Next-80B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct"},{"title":"DeltaNet Explained (Part I) | Songlin Yang","url":"https://sustcsonglin.github.io/blog/2024/deltanet-1/"},{"title":"Why Did Qwen3.5 Choose Gated DeltaNet?","url":"https://laonpeople.com/en/blog/why-did-qwen3-5-choose-gated-deltanet/"},{"title":"Qwen3.5-397B: 17B Active MoE, 1M-Token Context","url":"https://kiadev.net/news/2026-02-16-qwen3-5-397b-moe-17b-1m-context"},{"title":"Aihola","url":"https://aihola.com/article/qwen-flashqla-gdn-kernels"},{"title":"FG2-GDN: Enhancing Long-Context Gated Delta Networks with Doubly Fine-Grained Control","url":"https://arxiv.org/html/2604.19021v1"},{"title":"qwen3.5-gated-deltanet-analysis · GitHub","url":"https://gist.github.com/justinchuby/0213aa253664fb72e9adb0089816de15"},{"title":"Model Wars 2026: Qwen 3.5 & Gemma 4 Reshape Local Inference &middot; Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/05/model-wars-2026-qwen-35-gemma-4-local-inference/"}]

Based on the search results, here's what I found about Gated DeltaNet inference serving framework support and alternatives in 2026:

## Framework Support for Gated DeltaNet

Dedicated inference frameworks like SGLang and vLLM are recommended for inference tasks with models using Gated DeltaNet. More specifically:

- **vLLM**: vLLM version 0.10.2 or higher is required for Gated DeltaNet models, allowing creation of API endpoints with support for up to 256K token context length.

- **SGLang**: SGLang can be used to launch a server with OpenAI-compatible API service, with version 0.5.2 or higher required for Gated DeltaNet support.

## Kernel Optimization Support

vLLM and SGLang automatically dispatch to specialized GDN kernels when serving Qwen3-Next variants. Additionally, the Flash Linear Attention project added TileLang backend support for GDN kernels in April 2026.

## Important Considerations

MoE designs with Gated DeltaNet require expert-aware inference stacks with efficient expert dispatch and optimized kernels, with engineering work expected for production inference.

## Limitations

As of February 2026, no ONNX operators exist for any non-softmax attention variant, with all existing attention operators being exclusively softmax-based, which limits portability for Gated DeltaNet models to ONNX runtime environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1333ca9-d33f-4e8b-9ac6-f172609a7de9",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "222cd33d-c46e-4ecf-914d-cd3421052c39",
  "sourceToolAssistantUUID": "f1333ca9-d33f-4e8b-9ac6-f172609a7de9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T20:36:00.192Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012BvCVxXWrhULfPc4HhyJaM`</summary>

```json
{
  "query": "SGLang Qwen3.6-27B serving performance benchmark prefix caching hybrid"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "222cd33d-c46e-4ecf-914d-cd3421052c39",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXegoPd7Gf6RrUsaosx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61edf829-1119-46e0-b07a-b657a1fb3a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoRG6ojU1irZwFrgq9utTn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 4030,
      "cache_read_input_tokens": 11331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4030,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T20:36:00.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RuKoXAaWCH82Jrx6UynxaN`</summary>

```json
{
  "query": "\"sglang\" \"hybrid\" \"prefix caching\" \"recurrent state\" checkpoint mamba GDN 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61edf829-1119-46e0-b07a-b657a1fb3a0a",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXegoPd7Gf6RrUsaosx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcf93683-1ebf-4ff6-a4b5-489a3fc96e90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoRG6ojU1irZwFrgq9utTn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 4030,
      "cache_read_input_tokens": 11331,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 796,
          "output_tokens": 131,
          "cache_read_input_tokens": 11331,
          "cache_creation_input_tokens": 4030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4030,
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

_source line 19 · 2026-05-10T20:36:07.859Z_

<details><summary>↩ Tool result · `toolu_01RuKoXAaWCH82Jrx6UynxaN`</summary>

```text
Web search results for query: ""sglang" "hybrid" "prefix caching" "recurrent state" checkpoint mamba GDN 2026"

Links: [{"title":"Hybrid Models Meet SGLang: More than Full Attention – PyTorch","url":"https://pytorch.org/blog/hybrid-models-meet-sglang-more-than-full-attention/"},{"title":"Hybrid Model Support | SGLang's Support Scheme for Hybrid Architecture Models like Mamba-Transformer - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/hybrid-model-support-%7C-sglangs-support-scheme-for-hybrid-architecture-models-like-mamba-transformer_602857"},{"title":"[Feature] Mamba Radix Cache Checkpointing Proposal · Issue #22326 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/22326"},{"title":"[Feature] Limit to one cached Mamba state per multi-turn rollout · Issue #20144 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/20144"},{"title":"Qwen3-Next Usage — SGLang","url":"https://docs.sglang.io/basic_usage/qwen3.html"},{"title":"Qwen3-Next Usage - SGLang Documentation","url":"https://docs.sglang.io/docs/basic_usage/qwen3"},{"title":"Mamba-3 and State Space Models on GPU Cloud: Deploy SSM Inference as the Transformer Alternative (2026 Guide) | Spheron Blog","url":"https://www.spheron.network/blog/mamba-3-state-space-model-gpu-cloud-deployment/"},{"title":"Releases · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/releases"},{"title":"[Feature] Hybrid Linear LLMs support · Issue #12867 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/12867"},{"title":"GitHub - sgl-project/sglang: SGLang is a high-performance serving framework for large language models and multimodal models. · GitHub","url":"https://github.com/sgl-project/sglang"}]

The search returned comprehensive information about SGLang's support for hybrid models with Mamba and prefix caching features. Here's a summary of the key findings:

## SGLang Hybrid Model Support

SGLang supports prefix cache for hybrid linear models by implementing a hybrid radix tree named MambaRadixCache.

### Recurrent State and Memory Management

State space models (SSMs) such as Mamba selectively compress tokens and context into a recurrent state that is of fixed size and is updated in place. In SGLang, hybrid linear models separate the memory pool into Mamba pool and KV cache pool, with both having fixed sizes to eliminate the risk of CUDA out-of-memory errors.

### State Snapshotting and Checkpointing

Using state snapshotting, SGLang addresses Mamba's "non-reversible" limitation, making cache reuse and speculative decoding possible. A detailed GitHub issue discusses caching the Mamba state at every prefill_cache_interval (e.g., 1024 tokens), maximizing prefix reuse across requests sharing long prompts.

### Kernel Optimization

The search results reference kernel optimization, especially prefill kernel like gdn (Gated Delta Network) and kda (Key-Delta Attention).

### Recent Updates

Benchmarks show hybrid models such as Qwen3-Next run extremely fast on SGLang. The framework continues to evolve with support for speculative decoding and various optimization strategies for hybrid architectures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcf93683-1ebf-4ff6-a4b5-489a3fc96e90",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "d1b8a140-8a0e-4b40-b2de-a09614f56389",
  "sourceToolAssistantUUID": "dcf93683-1ebf-4ff6-a4b5-489a3fc96e90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T20:36:08.078Z_

<details><summary>↩ Tool result · `toolu_012BvCVxXWrhULfPc4HhyJaM`</summary>

```text
Web search results for query: "SGLang Qwen3.6-27B serving performance benchmark prefix caching hybrid"

Links: [{"title":"Qwen3.5 & Qwen3.6 Usage Guide - vLLM Recipes","url":"https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen3.6 - SGLang Documentation","url":"https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.6"},{"title":"Qwen/Qwen3.6-27B | vLLM Recipes","url":"https://recipes.vllm.ai/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen3.6 | SGLang Cookbook","url":"https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.6"},{"title":"Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model","url":"https://qwen.ai/blog?id=qwen3.6-27b"},{"title":"Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"},{"title":"We ran Qwen3.6-27B on $800 of consumer GPUs, day one. Here's how llama.cpp and vLLM compared, and what each token actually costs. - LLMKube Blog","url":"https://llmkube.com/blog/qwen3-6-27b-bakeoff"},{"title":"Qwen/Qwen3.6-27B · Deploying with sglang, weight name not matching","url":"https://huggingface.co/Qwen/Qwen3.6-27B/discussions/5"}]

Based on the search results, I found relevant information about SGLang serving of Qwen3.6-27B with prefix caching and hybrid architecture features.

## Key Findings:

**SGLang Support for Qwen3.6-27B:**
SGLang >=0.5.10 is required for Qwen3.6.

**Model Architecture:**
Qwen3.6-27B is a dense hybrid GDN (Gated Delta Networks) with smaller weights footprint and single-GPU friendly characteristics. Qwen3.6-27B is fully dense with all 27 billion parameters active on every inference pass.

**Performance and Optimization Features:**
Qwen3.6's hybrid Gated Delta Networks architecture supports two mamba scheduling strategies via --mamba-scheduler-strategy: V1 (no_buffer) as default. V2 (extra_buffer) enables overlap scheduling and branching point caching, trading higher mamba state memory for better throughput.

**Speculative Decoding and Throughput:**
Speculative decoding (MTP) can significantly reduce latency for interactive use cases. SGLang (version 0.5.10+) and vLLM both support Qwen3.6-27B with full tool-calling and reasoning parsing, providing batched inference and much higher throughput than single-user setups.

**Deployment Example:**
SGLang can create API endpoints at http://localhost:8000/v1 using tensor parallel on 8 GPUs with maximum context length of 262,144 tokens.

The search results provide deployment guidance and architectural information but do not contain specific performance benchmark comparisons for prefix caching in hybrid mode.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61edf829-1119-46e0-b07a-b657a1fb3a0a",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "4275a801-47bc-40a0-b16a-ba5865c7bdf6",
  "sourceToolAssistantUUID": "61edf829-1119-46e0-b07a-b657a1fb3a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T20:36:11.212Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011xbLKyQcCsA6ZbT2Q1qbgE`</summary>

```json
{
  "query": "SGLang mamba radix cache checkpointing issue 22326 state snapshotting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4275a801-47bc-40a0-b16a-ba5865c7bdf6",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXfXSMZH88YNw2jkrUS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1da4700f-ad82-45dc-a7c8-a168078ef816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132hUM73wrWaoiPhSksLmDE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 958,
      "cache_creation_input_tokens": 1937,
      "cache_read_input_tokens": 15361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1937,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T20:36:11.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PHn9o52SUmt1y1qnXM3oFs`</summary>

```json
{
  "query": "vLLM Qwen3.6 hybrid model turboquant KV cache bug workaround limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1da4700f-ad82-45dc-a7c8-a168078ef816",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXfXSMZH88YNw2jkrUS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "668c01c1-1b48-44ef-9ce7-4b585b5062e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132hUM73wrWaoiPhSksLmDE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 958,
      "cache_creation_input_tokens": 1937,
      "cache_read_input_tokens": 15361,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1937
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 958,
          "output_tokens": 130,
          "cache_read_input_tokens": 15361,
          "cache_creation_input_tokens": 1937,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1937,
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

_source line 23 · 2026-05-10T20:36:18.680Z_

<details><summary>↩ Tool result · `toolu_011xbLKyQcCsA6ZbT2Q1qbgE`</summary>

```text
Web search results for query: "SGLang mamba radix cache checkpointing issue 22326 state snapshotting"

Links: [{"title":"[Feature] Mamba Radix Cache Checkpointing Proposal · Issue #22326 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/22326"},{"title":"[Bug] mamba usage 1.00 even for short context, concurrency==1 · Issue #20466 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/20466"},{"title":"[Feature] Limit to one cached Mamba state per multi-turn rollout · Issue #20144 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/20144"},{"title":"Hybrid Models Meet SGLang: More than Full Attention – PyTorch","url":"https://pytorch.org/blog/hybrid-models-meet-sglang-more-than-full-attention/"},{"title":"Troubleshooting and Frequently Asked Questions — SGLang","url":"https://sgl-project.github.io/references/faq.html"},{"title":"Hybrid Model Support | SGLang's Support Scheme for Hybrid Architecture Models like Mamba-Transformer - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/hybrid-model-support-%7C-sglangs-support-scheme-for-hybrid-architecture-models-like-mamba-transformer_602857"},{"title":"Reasoning model thinking tokens pollute radix cache with unreachable entries · Issue #22373 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/22373"},{"title":"[Bug] KV cache corruption at radix cache block boundary with `--enable-deterministic-inference` (prefix_len == block_size) · Issue #22819 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/22819"},{"title":"[Bug] [GDN] Accuracy degradation with flashinfer `gated_delta_rule_decode_pretranspose` under `no_buffer` scheduling · Issue #20791 · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/issues/20791"},{"title":"Qwen3-Next Usage — SGLang","url":"https://docs.sglang.io/basic_usage/qwen3.html"}]

Based on the web search results, I found relevant information about issue #22326 in SGLang related to Mamba Radix Cache Checkpointing.

## SGLang Issue #22326: Mamba Radix Cache Checkpointing Proposal

The proposal addresses checkpointing strategies for Mamba states in the radix cache. For chunked prefill, it suggests inserting into the radix cache only when intervals are crossed, and caching the last checkpoint that aligns with chunk-size boundaries rather than caching whenever the decode sequence crosses interval-aligned boundaries.

### Key Aspects of the Proposal:

**Prefill Interval Checkpointing:**
The proposal includes caching the Mamba state at every prefill_cache_interval (e.g., 1024 tokens), which maximizes prefix reuse across requests sharing long prompts, such as system prompts plus long context.

**Decode Side Strategy:**
For chunked prefill, the proposal suggests inserting into the radix cache only when interval boundaries are crossed, caching the last checkpoint at chunk-size-aligned boundaries instead of at mamba_track_interval boundaries, with plans to deprecate mamba_track_interval. The reasoning is that partial decode outputs are rarely reused across requests.

**State Snapshotting:**
SGLang uses state snapshotting to address Mamba's "non-reversible" limitation, making cache reuse and speculative decoding possible.

### Implementation Considerations:

The proposal also addresses memory overhead concerns, as interval checkpointing multiplies Mamba pool usage by seq_len/interval per request, and multiplies the number of nodes that may need host-to-device transfers, raising questions about transfer bandwidth impact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1da4700f-ad82-45dc-a7c8-a168078ef816",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "9802844f-1300-489b-94d0-0aea59f1920b",
  "sourceToolAssistantUUID": "1da4700f-ad82-45dc-a7c8-a168078ef816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T20:36:22.953Z_

<details><summary>↩ Tool result · `toolu_01PHn9o52SUmt1y1qnXM3oFs`</summary>

```text
Web search results for query: "vLLM Qwen3.6 hybrid model turboquant KV cache bug workaround limitations"

Links: [{"title":"[Bug/Feature] TurboQuant + Hybrid MoE (Qwen3.6-35B-A3B) broken on Ampere (SM 80-86) — 13 patches with fixes · Issue #40124 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/40124"},{"title":"[Bug] turboquant_4bit_nc KV cache fails unify_kv_cache_spec_page_size assertion on hybrid Qwen3_5 (GDN + attention) architecture · Issue #41560 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/41560"},{"title":"[Bug]: MTP × TurboQuant × CUDA graph capture produces degenerate output on Qwen3-Next hybrid (not closed by v7.13 ngram fix tree) · Issue #40880 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/40880"},{"title":"[Bug]: TurboQuant KV + spec-decode + chunked-prefill crashes CUDA graph capture at query_start_loc.tolist() in continuation-prefill path (Qwen3-Next hybrid dense) · Issue #40807 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/40807"},{"title":"[Bug]: TurboQuant KV × any speculative decoding (MTP or ngram) produces degenerate token loops — confirmed across dense and hybrid attention · Issue #40831 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/40831"},{"title":"An Overnight Stack for Qwen3.6–27B: 85 TPS, 125K Context, Vision — on One RTX 3090 | Medium","url":"https://medium.com/@fzbcwvv/an-overnight-stack-for-qwen3-6-27b-85-tps-125k-context-vision-on-one-rtx-3090-0d95c6291914"},{"title":"[Bug]:[Qwen3.5] V1 KV cache page size unification fails for Qwen3.5/Qwen3.6 hybrid GPTQ Marlin model · Issue #41153 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/41153"},{"title":"TurboQuant KV Cache Compression - vllm-metal","url":"https://docs.vllm.ai/projects/vllm-metal/en/latest/turboquant/"},{"title":"[Bug]: TurboQuant `_continuation_prefill` OOMs and kills engine at long-context prefill (~185K actual tokens) · Issue #40420 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/40420"},{"title":"GitHub - varjoranta/turboquant-vllm: TurboQuant+ KV cache compression for vLLM. 3.8x smaller KV cache, same conversation quality. Fused CUDA kernels with automatic PyTorch fallback. · GitHub","url":"https://github.com/varjoranta/turboquant-vllm"}]

Based on the search results, I can provide comprehensive information about vLLM TurboQuant KV cache bugs with Qwen3.6 hybrid models:

## Key Issues

TurboQuant KV cache (k8v4) combined with hybrid MoE models (Qwen3.6-35B-A3B-FP8) does not work on Ampere GPUs (SM 80-86). Multiple code paths assume Hopper+ (SM ≥ 89) and hybrid model geometry is not handled correctly.

## Specific Bug Categories

**1. Architecture Compatibility:** vLLM raises NotImplementedError: TurboQuant KV cache is not supported for hybrid (attention + Mamba) models, though 13 issues have been identified and fixed, packaged as a runtime monkey-patch.

**2. Page Size Unification:** --kv-cache-dtype turboquant_4bit_nc causes a deterministic AssertionError at engine init when used with hybrid Qwen3_5ForConditionalGeneration models (Qwen3.6 27B family). On a hybrid model, the GDN/mamba layer page geometry differs from attention layer page geometry. The turboquant_4bit_nc page-size calculation does not account for the hybrid page-size variance after padding, causing the assertion to fail.

**3. Speculative Decoding Issues:** The MTP draft head runs its own attention over the live KV cache. When KV entries are stored through TurboQuant, the draft-head's attention distribution collapses on rare-token / structured-token contexts.

**4. CUDA Graph Capture:** Following the model card's recommendation with --kv-cache-dtype tq-t4nc for 262K context and speculative decoding enabled hits a bug on Ampere hardware.

**5. Long Context OOM:** A single chat-completion request whose tokenized prompt exceeds ~185K tokens reliably kills the entire vLLM engine (CUDA OOM in the prefill path), well below the --max-model-len=262144 the model advertises.

## Workarounds

--compilation-config '{"cudagraph_mode":"NONE"}' disables CUDA graphs but restores correctness at ~33 TPS. Dropping TurboQuant entirely (use fp8_e5m2 KV) caps context at ~32-40K on a 24 GB card but is unaffected.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "668c01c1-1b48-44ef-9ce7-4b585b5062e9",
  "isSidechain": true,
  "promptId": "fe4e25b9-bbe1-4b7d-9964-298370c59cce",
  "agentId": "ac26f3c0af4ac1047",
  "type": "user",
  "uuid": "2e24455a-25ad-411c-9316-b67fc19e11d2",
  "sourceToolAssistantUUID": "668c01c1-1b48-44ef-9ce7-4b585b5062e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T20:37:06.966Z_

Here is a comprehensive report on the current state of SGLang's hybrid model support for Gated DeltaNet architectures (Qwen3.5/3.6 series):

---

## SGLang Hybrid Model Support: Current State

### SGLang GitHub Issue #12867 - Roadmap

Issue #12867, titled "[Feature] Hybrid Linear LLMs support," was opened on November 8, 2025. It tracks the following features that still need full support or refinement:

**Completed/Working:**
- Basic inference for hybrid linear models (Mamba + attention, GDN + attention)
- Dual memory pool architecture (Mamba pool for recurrent states + KV cache pool for attention layers)
- MambaRadixCache for prefix caching on hybrid models
- Overlap scheduling (V2 "extra_buffer" strategy)
- State snapshotting for Mamba/GDN states

**Pending/In Progress (per issue #12867):**
- Prefix caching adaptation (full interval checkpointing -- see issue #22326)
- Page size > 1 support
- Overlap schedule support (partially available via `--mamba-scheduler-strategy extra_buffer`)
- Storing mamba state every k steps / branch point
- Kernel adaptations for shortconv, GDN, mamba1 with intermediate state storage
- Speculative decoding adaptation for hybrid architectures
- General speculative decoding adaptation

### SGLang's Dual Memory Pool Architecture

SGLang resolves the fundamental conflict between Transformer token-granularity caching and Mamba/GDN request-granularity in-place updates by maintaining two separate memory pools:
- **Paged KV pool** for full attention layers (fine-grained dynamic allocation)
- **Mamba/GDN pool** for linear layers storing conv and temporal states (large contiguous blocks)

Both pools have fixed sizes to eliminate CUDA OOM risks and allow elastic scheduling.

### Prefix Caching for Hybrid Models (Issue #22326)

A detailed proposal for "Mamba Radix Cache Checkpointing" exists (issue #22326). It proposes:
- Caching the recurrent state at every `prefill_cache_interval` (e.g., 1024 tokens)
- Inserting into the radix cache only when interval boundaries are crossed during chunked prefill
- Trading off memory overhead (seq_len/interval multiplier on Mamba pool usage) for prefix reuse

### Serving Qwen3.6-27B on SGLang

- **Minimum version:** SGLang >= 0.5.10
- **Architecture:** Dense hybrid GDN (27B parameters, all active), single-GPU friendly
- **Context length:** Up to 262,144 tokens
- **Scheduler strategies:** V1 (`no_buffer`, default) or V2 (`extra_buffer` for overlap scheduling and branching point caching)
- **Speculative decoding (MTP):** Supported for latency reduction
- **Known bug:** Issue #20791 reports accuracy degradation with flashinfer `gated_delta_rule_decode_pretranspose` under `no_buffer` scheduling

### GDN Kernel Status

- Flash Linear Attention project added TileLang backend support for GDN kernels (April 2026)
- SGLang and vLLM automatically dispatch to specialized GDN kernels for Qwen3-Next variants
- Kernel optimization for GDN with intermediate state storage is still listed as pending in issue #12867

---

## vLLM Alternative: Support and Limitations

vLLM supports Qwen3.6-27B (v0.10.2+) but has significant issues with hybrid architectures:

**Critical Bugs:**
1. **Issue #41560:** `turboquant_4bit_nc` KV cache fails `unify_kv_cache_spec_page_size` assertion because GDN/mamba layer page geometry differs from attention layer geometry
2. **Issue #40124:** TurboQuant + Hybrid MoE broken on Ampere GPUs (SM 80-86) -- 13 patches needed
3. **Issue #40831:** TurboQuant KV combined with any speculative decoding (MTP or ngram) produces degenerate token loops
4. **Issue #40807:** TurboQuant + spec-decode + chunked-prefill crashes CUDA graph capture
5. **Issue #41153:** V1 KV cache page size unification fails for Qwen3.5/Qwen3.6 hybrid GPTQ Marlin models

**Workarounds:**
- Use `fp8_e5m2` or `auto` (bfloat16) KV dtype instead of TurboQuant -- these pass cleanly on hybrid architectures
- Disable CUDA graphs (`--compilation-config '{"cudagraph_mode":"NONE"}'`) for correctness at ~33 TPS
- Dropping TurboQuant caps context at ~32-40K on 24GB cards but eliminates hybrid-related bugs

---

## Other Serving Frameworks for Hybrid Architectures

1. **llama.cpp:** Supports Qwen3.6-27B for local inference (one comparison showed 85 TPS on a single RTX 3090 with vLLM vs llama.cpp bakeoff)
2. **AMD Instinct GPUs:** Day-0 support for both Qwen3.5 and Qwen3.6 on AMD Instinct via SGLang with ROCm
3. **No ONNX support:** As of 2026, no ONNX operators exist for non-softmax attention variants, limiting portability

---

## Summary for Serving Qwen3.6-27B

| Feature | SGLang (>= 0.5.10) | vLLM (>= 0.10.2) |
|---------|--------------------|--------------------|
| Basic inference | Working | Working |
| GDN kernels | Auto-dispatched | Auto-dispatched |
| Prefix caching | Partially (MambaRadixCache) | Limited |
| Speculative decoding | MTP supported | Buggy with TurboQuant |
| TurboQuant/Quantized KV | N/A | Broken on hybrid models |
| Long context (262K) | Supported | Supported (with fp8/bf16 KV) |
| Overlap scheduling | V2 extra_buffer | N/A |

**Recommendation:** SGLang >= 0.5.10 is currently the more mature option for serving Qwen3.6-27B, with its dual memory pool, MambaRadixCache, and V2 overlap scheduling providing better hybrid architecture support. Use `--mamba-scheduler-strategy extra_buffer` for higher throughput. vLLM works but requires avoiding TurboQuant KV cache compression and speculative decoding combinations.

---

Sources:
- [SGLang Issue #12867 - Hybrid Linear LLMs support](https://github.com/sgl-project/sglang/issues/12867)
- [Hybrid Models Meet SGLang: More than Full Attention (PyTorch Blog)](https://pytorch.org/blog/hybrid-models-meet-sglang-more-than-full-attention/)
- [SGLang Hybrid Model Support (Alibaba Cloud)](https://www.alibabacloud.com/blog/hybrid-model-support-%7C-sglangs-support-scheme-for-hybrid-architecture-models-like-mamba-transformer_602857)
- [SGLang Issue #22326 - Mamba Radix Cache Checkpointing Proposal](https://github.com/sgl-project/sglang/issues/22326)
- [vLLM Issue #41560 - turboquant_4bit_nc KV cache fails on hybrid Qwen3.5](https://github.com/vllm-project/vllm/issues/41560)
- [vLLM Issue #40124 - TurboQuant + Hybrid MoE broken on Ampere](https://github.com/vllm-project/vllm/issues/40124)
- [Qwen3.6-27B SGLang Cookbook](https://cookbook.sglang.io/autoregressive/Qwen/Qwen3.6)
- [SGLang Qwen3.6 Documentation](https://docs.sglang.io/cookbook/autoregressive/Qwen/Qwen3.6)
- [Qwen3.6-27B Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)
- [NVlabs/GatedDeltaNet (ICLR 2025)](https://github.com/NVlabs/GatedDeltaNet)
- [Day 0 Support for Qwen3.6 on AMD Instinct GPUs](https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-qwen3-6-on-amd-instinct-gpus.html)
- [SGLang Issue #20791 - GDN accuracy degradation bug](https://github.com/sgl-project/sglang/issues/20791)
- [Hybrid Models as First-Class Citizens in vLLM (PyTorch Blog)](https://pytorch.org/blog/hybrid-models-as-first-class-citizens-in-vllm/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e24455a-25ad-411c-9316-b67fc19e11d2",
  "isSidechain": true,
  "agentId": "ac26f3c0af4ac1047",
  "requestId": "req_011CauXgcxGTTWWU3yvYKRDi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "659f9502-ec64-49a0-9bd3-46a6858f6279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fe0fe1c3-6517-4815-b6b8-db2a2dba8e02",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jSDkPerkwMaS59GPk4mPR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3756,
      "cache_read_input_tokens": 17298,
      "output_tokens": 2279,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2279,
          "cache_read_input_tokens": 17298,
          "cache_creation_input_tokens": 3756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3756,
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
