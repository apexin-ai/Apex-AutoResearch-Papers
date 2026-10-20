# Research conversation: I'm reviewing a paper about per-head mixed-precision KV cache quantization. I need to check whether the paper is missing

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af85b6f68bc376c6d.jsonl`
- **Structured JSON:** [`b53e12843bf9200dddf9.json`](../../sessions/b5/b53e12843bf9200dddf9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-14T13:06:41.174Z_

I'm reviewing a paper about per-head mixed-precision KV cache quantization. I need to check whether the paper is missing important baselines. Search the web for:

1. "KIVI per-channel quantization KV cache" — does KIVI have a per-channel quantization strategy that could serve as a more sophisticated uniform baseline?
2. "ZipCache mixed precision KV cache" — does ZipCache do token-level mixed precision that should be compared?
3. "MiKV mixed precision KV cache 2024 2025" or "per-head KV cache quantization" — any other recent per-head allocation methods?
4. "KCVT" or "QJL" or other recent KV cache quantization methods from 2025-2026 that do per-head or mixed-precision allocation

For each, briefly note: what granularity it operates at (per-head, per-token, per-channel, per-layer), and whether it would be a fair baseline for a paper about per-head bit-width allocation on hardware-aligned bit-widths {2,4,8,16}.

Keep response under 300 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "agentId": "af85b6f68bc376c6d",
  "type": "user",
  "uuid": "265c7492-ecc0-4db3-b914-9aa558cf76fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T13:06:43.009Z_

I'll search for these recent KV cache quantization methods to assess potential missing baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "265c7492-ecc0-4db3-b914-9aa558cf76fb",
  "isSidechain": true,
  "agentId": "af85b6f68bc376c6d",
  "requestId": "req_011Cb2WdLkGbsQ6RssGHSA8y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0163c659-f410-4f04-a50e-a78a3b400e4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014gcvJHjN1aNndTRQwK4UNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15081,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15081,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 3 · 2026-05-14T13:06:43.260Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WQqHQCmf5JwA2zuMiSp2VL`</summary>

```json
{
  "query": "KIVI per-channel quantization KV cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0163c659-f410-4f04-a50e-a78a3b400e4b",
  "isSidechain": true,
  "agentId": "af85b6f68bc376c6d",
  "requestId": "req_011Cb2WdLkGbsQ6RssGHSA8y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "93eb71ba-3f45-44e7-b9b0-a00d5343afe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014gcvJHjN1aNndTRQwK4UNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15081,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15081,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 4 · 2026-05-14T13:06:43.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HFPAn6mUCLpVYukXkE3dPr`</summary>

```json
{
  "query": "ZipCache mixed precision KV cache"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93eb71ba-3f45-44e7-b9b0-a00d5343afe7",
  "isSidechain": true,
  "agentId": "af85b6f68bc376c6d",
  "requestId": "req_011Cb2WdLkGbsQ6RssGHSA8y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6dd4be9d-2b82-4437-b294-21e8a58a36c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014gcvJHjN1aNndTRQwK4UNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15081,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15081,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 5 · 2026-05-14T13:06:44.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V6QgGm8Rkh1HYYkpN5zgTU`</summary>

```json
{
  "query": "MiKV mixed precision KV cache 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dd4be9d-2b82-4437-b294-21e8a58a36c7",
  "isSidechain": true,
  "agentId": "af85b6f68bc376c6d",
  "requestId": "req_011Cb2WdLkGbsQ6RssGHSA8y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6f7f36e8-646b-449f-806c-b4853245ad34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014gcvJHjN1aNndTRQwK4UNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15081,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15081,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 6 · 2026-05-14T13:06:44.525Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VFcyr6UYmJpVTsL4j6aWKN`</summary>

```json
{
  "query": "per-head KV cache quantization recent methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7f36e8-646b-449f-806c-b4853245ad34",
  "isSidechain": true,
  "agentId": "af85b6f68bc376c6d",
  "requestId": "req_011Cb2WdLkGbsQ6RssGHSA8y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e671645e-08ee-4095-8dd2-1bc79f2d441e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014gcvJHjN1aNndTRQwK4UNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15081,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15081,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 7 · 2026-05-14T13:06:44.809Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dcbz2JvLRZgUQVKEQRL6W6`</summary>

```json
{
  "query": "KCVT QJL KV cache quantization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e671645e-08ee-4095-8dd2-1bc79f2d441e",
  "isSidechain": true,
  "agentId": "af85b6f68bc376c6d",
  "requestId": "req_011Cb2WdLkGbsQ6RssGHSA8y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fc2ef5af-aa25-4cee-9405-c9d269338616",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014gcvJHjN1aNndTRQwK4UNd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15081,
      "cache_read_input_tokens": 0,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15081
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 270,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15081,
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

_source line 8 · 2026-05-14T13:06:49.906Z_

<details><summary>↩ Tool result · `toolu_01V6QgGm8Rkh1HYYkpN5zgTU`</summary>

```text
Web search results for query: "MiKV mixed precision KV cache 2024 2025"

Links: [{"title":"MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning","url":"https://arxiv.org/html/2512.19206v1"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"No Token Left Behind: Reliable KV Cache Compression via Importance-Aware Mixed Precision Quantization","url":"https://arxiv.org/html/2402.18096"},{"title":"[2402.18096] No Token Left Behind: Reliable KV Cache Compression via Importance-Aware Mixed Precision Quantization","url":"https://arxiv.org/abs/2402.18096"},{"title":"Constant-Memory KV Cache Methods","url":"https://www.emergentmind.com/topics/constant-memory-kv-cache"},{"title":"Don’t Discard, but Keep It Small: Context-Preserving KV Cache Compression with Importance-Aware Adaptive Precision | OpenReview","url":"https://openreview.net/forum?id=CRQ8JuQDEd&noteId=kmd3faszWL"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs","url":"https://arxiv.org/html/2505.18610v1"},{"title":"Published as a conference paper at COLM 2024","url":"https://arxiv.org/pdf/2407.18003"},{"title":"No Token Left Behind: Reliable KV Cache Compression via Importance-Aware Mixed Precision Quantization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240218096Y/abstract"},{"title":"[2512.19206] MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning","url":"https://arxiv.org/abs/2512.19206"}]

Based on the search results, here's what I found about MiKV mixed precision KV cache:

## MiKV (Mixed-Precision KV Cache)

MiKV is a reliable cache compression method that preserves context details by retaining evicted KV pairs in low-precision while ensuring generation quality by keeping important KV pairs in high-precision.

### Key Problem It Addresses

MiKV examines the detrimental impact of cache eviction and addresses unforeseen risks like safety breaches, hallucinations, and context loss. Rather than completely discarding unimportant KV pairs, preserving even a small amount of information in evicted KV pairs via reduced precision quantization substantially recovers degradation, while important KV pairs must be kept at higher precision to safeguard generation quality.

### Performance and Results

Experimental results across multiple benchmarks and LLM architectures demonstrate that MiKV achieves a state-of-the-art balance between compression ratio and model performance, outperforming existing baselines.

### Recent Developments (2025)

There are also related approaches building on this concept. Recent progress in reasoning-capable LLMs through long Chain-of-Thought techniques has led to substantial memory overhead from KV Cache. For instance, PM-KVQ is another progressive mixed-precision KV cache quantization method proposed for long-CoT LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f7f36e8-646b-449f-806c-b4853245ad34",
  "isSidechain": true,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "agentId": "af85b6f68bc376c6d",
  "type": "user",
  "uuid": "bab361e4-e520-4cc8-9387-75d376251b32",
  "sourceToolAssistantUUID": "6f7f36e8-646b-449f-806c-b4853245ad34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T13:06:50.046Z_

<details><summary>↩ Tool result · `toolu_01WQqHQCmf5JwA2zuMiSp2VL`</summary>

```text
Web search results for query: "KIVI per-channel quantization KV cache"

Links: [{"title":"GitHub - jy-yuan/KIVI: [ICML 2024] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache · GitHub","url":"https://github.com/jy-yuan/KIVI"},{"title":"[2402.02750] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://arxiv.org/abs/2402.02750"},{"title":"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://proceedings.mlr.press/v235/liu24bz.html"},{"title":"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://arxiv.org/html/2402.02750v2"},{"title":"[Literature Review] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://www.themoonlight.io/en/review/kivi-a-tuning-free-asymmetric-2bit-quantization-for-kv-cache"},{"title":"KITTY: ACCURATE AND EFFICIENT 2-BIT KV CACHE QUANTIZATION WITH","url":"https://www.arxiv.org/pdf/2511.18643"},{"title":"KIVI-Plug-and-play-2bit-KV-Cache-Quantization-with- ...","url":"https://www.researchgate.net/profile/Zirui-Liu-29/publication/376831635_KIVI_Plug-and-play_2bit_KV_Cache_Quantization_with_Streaming_Asymmetric_Quantization/links/658b5d282468df72d3db3280/KIVI-Plug-and-play-2bit-KV-Cache-Quantization-with-Streaming-Asymmetric-Quantization.pdf"},{"title":"Unlocking Longer Generation with Key-Value Cache Quantization","url":"https://huggingface.co/blog/kv-cache-quantization"},{"title":"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bz/liu24bz.pdf"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"}]

Based on the search results, here's what I found about KIVI per-channel quantization for KV cache:

## Overview

KIVI is a plug-and-play 2bit KV cache quantization algorithm without any fine-tuning. KIVI was accepted by ICML 2024.

## Per-Channel Quantization Strategy

The core innovation of KIVI is its asymmetric quantization approach: the key cache should be quantized per-channel, i.e., group elements along the channel dimension and quantize them together. In contrast, the value cache should be quantized per-token.

KIVI quantizes the key cache per-channel and the value cache per-token, because they showed that for LLMs keys have higher magnitudes of outliers in some channels while values don't show such a pattern.

## Performance Benefits

With hardware-friendly implementation, KIVI can enable Llama, Falcon, and Mistral models to maintain almost the same quality while using 2.6× less peak memory (including model weight). This reduction in memory usage enables up to 4× larger batch size, bringing 2.35× ~ 3.47× throughput on real LLM inference workload.

## Key Technical Insight

The per-token value cache quantization aligns well with the streaming nature of auto-regressive inference, allowing newly quantized tensors to be directly appended to the existing quantized value cache by token dimension.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93eb71ba-3f45-44e7-b9b0-a00d5343afe7",
  "isSidechain": true,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "agentId": "af85b6f68bc376c6d",
  "type": "user",
  "uuid": "a97ac357-aeec-4b7f-a59a-775c9bdef657",
  "sourceToolAssistantUUID": "93eb71ba-3f45-44e7-b9b0-a00d5343afe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T13:06:50.451Z_

<details><summary>↩ Tool result · `toolu_01HFPAn6mUCLpVYukXkE3dPr`</summary>

```text
Web search results for query: "ZipCache mixed precision KV cache"

Links: [{"title":"ZipCache: Accurate and Efficient KV Cache Quantization ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/7e57131fdeb815764434b65162c88895-Paper-Conference.pdf"},{"title":"GitHub - ThisisBillhe/ZipCache: [NeurIPS 2024] The official implementation of ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification","url":"https://github.com/ThisisBillhe/ZipCache"},{"title":"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification","url":"https://arxiv.org/html/2405.14256v1"},{"title":"KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference","url":"https://arxiv.org/html/2502.04420"},{"title":"Accurate KV Cache Quantization with Outlier Tokens Tracing","url":"https://arxiv.org/html/2505.10938v1"},{"title":"KV-Cache Quantization Techniques","url":"https://www.emergentmind.com/topics/kv-cache-quantization-4cf1d820-95b5-4aa4-a906-6619bb81d40a"},{"title":"ZipCache: accurate and efficient KV cache quantization ...","url":"https://dl.acm.org/doi/10.5555/3737916.3740097"},{"title":"RotateKV: Accurate and Robust 2-Bit KV Cache Quantization","url":"https://www.ijcai.org/proceedings/2025/0690.pdf"},{"title":"[PDF] ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ZipCache:-Accurate-and-Efficient-KV-Cache-with-He-Zhang/ca1952a54cf85f0f449cb337f70b083100069c9c"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"}]

Based on the search results, here's what I found about ZipCache mixed precision KV cache:

## Overview

ZipCache is an accurate and efficient mixed-precision quantization framework for compressing KV cache. The approach introduces an adaptive KV cache mixed-precision quantization method for LLMs.

## Key Technical Approach

ZipCache employs mixed precision quantization for KV cache where salient tokens will be quantized to 4-bit while the remaining will be quantized to 2-bit. For both subsets, it applies channelwise quantization for the key cache and channel-separable tokenwise quantization for the value cache.

## Salient Token Identification

ZipCache presents a novel metric for accurately assessing token saliency based on normalized attention scores, which enables adaptive quantization of all tokens according to their saliency, leading to improved compression ratios without sacrificing model performance.

## Performance Results

ZipCache attains a compression ratio of 4.94× without sacrificing performance when tested with the Mistral-7B model, outperforming predecessor methods. Additionally, when evaluating LLaMA3-8B model with an input length of 4096, ZipCache showcases a 37.3% reduction in prefill-phase latency, a 56.9% reduction in decoding-phase latency, and a 19.8% reduction in GPU memory usage.

## Publication

ZipCache was presented at NeurIPS 2024 and has an official implementation available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6dd4be9d-2b82-4437-b294-21e8a58a36c7",
  "isSidechain": true,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "agentId": "af85b6f68bc376c6d",
  "type": "user",
  "uuid": "c75b9f95-c8ef-48e7-8e10-98be6248054c",
  "sourceToolAssistantUUID": "6dd4be9d-2b82-4437-b294-21e8a58a36c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T13:06:51.567Z_

<details><summary>↩ Tool result · `toolu_01VFcyr6UYmJpVTsL4j6aWKN`</summary>

```text
Web search results for query: "per-head KV cache quantization recent methods"

Links: [{"title":"Quantized KV Cache - vLLM","url":"https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"Optimizing Inference for Long Context and Large Batch Sizes with NVFP4 KV Cache | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/"},{"title":"The State of FP8 KV-Cache and Attention Quantization in vLLM | vLLM Blog","url":"https://vllm-project.github.io/2026/04/22/fp8-kvcache.html"},{"title":"FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression","url":"https://arxiv.org/html/2605.11478"},{"title":"Key-Value(KV) Cache Quantization — lmdeploy 0.5.0 documentation","url":"https://lmdeploy.readthedocs.io/en/v0.5.0/quantization/kv_quant.html"},{"title":"NeurIPS Poster KV Cache is 1 Bit Per Channel: Efficient Large Language Model Inference with Coupled Quantization","url":"https://neurips.cc/virtual/2024/poster/93558"},{"title":"TurboQuant - Extreme KV Cache Quantization · ggml-org/llama.cpp · Discussion #20969","url":"https://github.com/ggml-org/llama.cpp/discussions/20969"},{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"}]

Based on the web search results, here's an overview of recent per-head KV cache quantization methods:

## Recent Methods

### RateQuant (2026)
RateQuant operates at per-head granularity with closed-form allocation and supports arbitrary base quantizers through calibration. It addresses a "distortion model mismatch" failure mode where applying one quantizer's distortion model to another inverts the allocation order. RateQuant fits a per-quantizer distortion model from a small calibration set, then solves the resulting bit-allocation problem in closed form via reverse waterfilling from rate-distortion theory. On Qwen3-8B at 2.5 average bits, calibrated RateQuant reduces KIVI's perplexity from 49.3 to 14.9 (70% reduction).

### Per-Head Support in vLLM
Per-attention-head quantization assigns each scale to an attention head: q_scale = [num_heads], k/v_scale = [num_kv_heads]. Per-attention-head quantization is currently available only with the Flash Attention backend and requires the calibration pathway provided by llm-compressor.

### Other Notable Methods
KIVI, published at ICML 2024, is a plug-and-play 2-bit KV cache quantization algorithm that requires no fine-tuning. Quantization methods (KIVI, KVQuant, TurboQuant) reduce memory without removing tokens.

### LMDeploy's Approach
Since v0.4.0, LMDeploy has supported online key-value cache quantization with int4 and int8 numerical precision, utilizing an asymmetric quantization method that is applied on a per-head, per-token basis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e671645e-08ee-4095-8dd2-1bc79f2d441e",
  "isSidechain": true,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "agentId": "af85b6f68bc376c6d",
  "type": "user",
  "uuid": "fdaa26d1-5988-4d8d-aea7-e74132a5f1ee",
  "sourceToolAssistantUUID": "e671645e-08ee-4095-8dd2-1bc79f2d441e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T13:06:54.235Z_

<details><summary>↩ Tool result · `toolu_01Dcbz2JvLRZgUQVKEQRL6W6`</summary>

```text
Web search results for query: "KCVT QJL KV cache quantization 2025 2026"

Links: [{"title":"TurboQuant - Extreme KV Cache Quantization · ggml-org/llama.cpp · Discussion #20969","url":"https://github.com/ggml-org/llama.cpp/discussions/20969"},{"title":"INT4/INT8 KV Cache — lmdeploy","url":"https://lmdeploy.readthedocs.io/en/latest/quantization/kv_quant.html"},{"title":"KV Cache Is Eating Your VRAM. Here’s How Google Fixed It With TurboQuant. | Towards Data Science","url":"https://towardsdatascience.com/kv-cache-is-eating-your-vram-heres-how-google-fixed-it-with-turboquant/"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"},{"title":"Quantized KV Cache - vLLM","url":"https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/"},{"title":"TurboQuant Explained: 3-Bit KV Cache at 6× Compression","url":"https://decodethefuture.org/en/turboquant-vector-quantization-kv-cache/"},{"title":"QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead | OpenReview","url":"https://openreview.net/forum?id=xHPVGmLXjd"},{"title":"ICLR QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead","url":"https://iclr.cc/virtual/2025/33512"},{"title":"Implementing Google’s TurboQuant: KV Cache Compression and LLM Evaluation with W&B | by Dave Davies | Online Inference | Mar, 2026 | Medium","url":"https://medium.com/online-inference/implementing-googles-turboquant-kv-cache-compression-and-llm-evaluation-with-w-b-1403d460846b"},{"title":"TurboQuant.net - Independent TurboQuant Analysis","url":"https://turboquant.net/"}]

Based on the web search results, here's what I found about KCVT, QJL, and KV cache quantization in 2025-2026:

## Overview

TurboQuant is a two-stage vector quantization algorithm from Google Research (ICLR 2026) that compresses high-dimensional vectors — particularly LLM key-value caches — to as low as 3 bits per coordinate with zero accuracy loss.

## Key Components

The TurboQuant approach combines two main techniques:

**QJL (Quantized Johnson-Lindenstrauss):** QJL uses a small, residual amount of compression power (just 1 bit) to apply the QJL algorithm to the tiny amount of error left over from the first stage. QJL is a new quantization approach that consists of a Johnson-Lindenstrauss (JL) transform followed by sign-bit quantization. In contrast to existing methods, QJL eliminates memory overheads by removing the need for storing quantization constants.

**PolarQuant (Stage 1):** The method involves randomly rotating the data vectors using orthogonal transforms like Hadamard transform, which simplifies the data's geometry, making it easy to apply a standard, high-quality quantizer to each part of the vector individually. This stage uses most of the compression power to capture the main concept and strength of the original vector.

## Performance Results

LMDeploy supports KV quantization based on Google Research's TurboQuant technology, achieving higher compression ratio with near-zero accuracy loss through K=4bit QJL4 + V=2bit MSE combination. At 3-bit quantization, TurboQuant achieves at least 6× memory reduction compared to FP16 storage. For example, the KV cache of Qwen2.5-3B at 8K tokens drops from 289 MB to approximately 58 MB.

## Recent Developments

As of March 30th 2026, WHT + QJL + MSE was confirmed as the working solution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc2ef5af-aa25-4cee-9405-c9d269338616",
  "isSidechain": true,
  "promptId": "1add3373-1a7b-44ff-97f3-44b1252a5708",
  "agentId": "af85b6f68bc376c6d",
  "type": "user",
  "uuid": "3c3c68b8-dcc5-45e1-8369-24e1f8465210",
  "sourceToolAssistantUUID": "fc2ef5af-aa25-4cee-9405-c9d269338616",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T13:07:02.228Z_

## Summary: Missing KV Cache Quantization Baselines

Your paper likely should compare against these recent per-head methods:

**KIVI (ICML 2024)** — Per-channel keys, per-token values. Uniform 2-bit only, not mixed-precision or per-head. Not a direct baseline for your per-head work, though widely cited as a strong baseline.

**ZipCache (NeurIPS 2024)** — Token-level mixed-precision (4-bit salient, 2-bit others) with channel-wise key quantization. Operates at token granularity, not per-head. Fair comparison point for mixed-precision effectiveness, but different granularity.

**RateQuant (2026, recent)** — **Per-head mixed-precision with closed-form rate-distortion allocation.** This is your most critical missing baseline. Supports arbitrary bit-widths through calibrated distortion models. On Qwen3-8B at 2.5 bits, it achieves 70% better perplexity than KIVI (14.9 vs 49.3). If your paper is about per-head allocation, RateQuant is essentially a competing solution—you must compare against it.

**QJL (ICLR 2025)** — Quantized Johnson-Lindenstrauss with 1-bit residual quantization (part of TurboQuant). Operates per-coordinate with zero overhead, but not per-head. Less directly relevant.

**PM-KVQ (2025)** — Progressive mixed-precision for long-CoT reasoning, operates at token/layer level. Not per-head.

**Critical gap:** RateQuant is the main comparable baseline you're likely missing. It directly addresses per-head mixed-precision allocation using rate-distortion theory. Depending on your paper's novelty (algorithm, hardware efficiency, empirical results), you should either compare against it or clearly distinguish your approach (e.g., different bit-width constraints, hardware targets, or optimization objectives).

Sources:
- [KIVI (ICML 2024)](https://arxiv.org/abs/2402.02750)
- [ZipCache (NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/file/7e57131fdeb815764434b65162c88895-Paper-Conference.pdf)
- [RateQuant](https://arxiv.org/html/2605.06675)
- [QJL (ICLR 2025)](https://iclr.cc/virtual/2025/33512)
- [PM-KVQ](https://arxiv.org/html/2505.18610v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c3c68b8-dcc5-45e1-8369-24e1f8465210",
  "isSidechain": true,
  "agentId": "af85b6f68bc376c6d",
  "requestId": "req_011Cb2WeJX6ocYRcxXABLvvM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff8dd438-9e10-4e1f-9867-159b3693b046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_1_36f1d6e8",
  "sessionId": "957b9df0-67d4-4b3a-8244-4b6f12b8919d",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TgcSCH8KKHoAT1ea8Yhavp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6273,
      "cache_read_input_tokens": 15081,
      "output_tokens": 635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6273
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 635,
          "cache_read_input_tokens": 15081,
          "cache_creation_input_tokens": 6273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6273,
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
