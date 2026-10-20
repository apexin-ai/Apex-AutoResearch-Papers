# Research conversation: Search for recent papers (2025-2026) that discuss composing or stacking multiple LLM inference efficiency methods togeth

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a42cf1d58efb497c0.jsonl`
- **Structured JSON:** [`c967105c05c0f0c53901.json`](../../sessions/c9/c967105c05c0f0c53901.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-10T19:30:30.850Z_

Search for recent papers (2025-2026) that discuss composing or stacking multiple LLM inference efficiency methods together. I'm looking for:
1. Papers that combine MLP sparsity with KV cache compression as separate modules
2. Papers that discuss "orthogonality" or "composability" of different efficiency axes
3. Any work showing that activation sparsity gains are independent of and additive with KV compression gains

Use WebSearch with queries like:
- "composable LLM inference efficiency methods 2025 2026"
- "MLP sparsity orthogonal KV cache compression"
- "stacking activation sparsity KV eviction LLM"

Report what you find in under 300 words, focusing on whether there's precedent for claiming different efficiency axes are composable/orthogonal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d34ede03-7cfc-42f7-87a4-326aeae7f146",
  "agentId": "a42cf1d58efb497c0",
  "type": "user",
  "uuid": "ec8512a2-540c-405b-9410-f309eeee2c0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:30:30.852Z_

```json
{
  "parentUuid": "ec8512a2-540c-405b-9410-f309eeee2c0d",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
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
  "uuid": "4c2bd3bf-3abd-40ca-ace8-c53cbaf84faf",
  "timestamp": "2026-05-10T19:30:30.852Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T19:30:33.700Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Y9YNjKVGLmkKNpQ1RRkYtA`</summary>

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
  "parentUuid": "4c2bd3bf-3abd-40ca-ace8-c53cbaf84faf",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
  "requestId": "req_011CauSfJ28TstFTMfLFoBy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abb7f1e8-d46e-4e43-b7b7-76e836a5439f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyS635dVGn9fTSmhkQHzCw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 734
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 734,
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

_source line 4 · 2026-05-10T19:30:33.704Z_

<details><summary>↩ Tool result · `toolu_01Y9YNjKVGLmkKNpQ1RRkYtA`</summary>

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
  "parentUuid": "abb7f1e8-d46e-4e43-b7b7-76e836a5439f",
  "isSidechain": true,
  "promptId": "d34ede03-7cfc-42f7-87a4-326aeae7f146",
  "agentId": "a42cf1d58efb497c0",
  "type": "user",
  "uuid": "e7f13a49-e0a1-40a5-9185-bc56a928bd36",
  "sourceToolAssistantUUID": "abb7f1e8-d46e-4e43-b7b7-76e836a5439f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:30:37.652Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gaf5jwny6VZUCfVYpCCRW6`</summary>

```json
{
  "query": "composable LLM inference efficiency methods 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f13a49-e0a1-40a5-9185-bc56a928bd36",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
  "requestId": "req_011CauSfWXTDgLHhg6CB64Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f101521-fc26-470d-9d07-68db2a1291d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uf5GsKysRDs1eBdQbinDfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:30:38.053Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NF9wpoht7SY6qPG7u6bFhk`</summary>

```json
{
  "query": "MLP sparsity orthogonal KV cache compression LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f101521-fc26-470d-9d07-68db2a1291d3",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
  "requestId": "req_011CauSfWXTDgLHhg6CB64Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40b306df-1889-44b2-ab1e-7a4b32482490",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uf5GsKysRDs1eBdQbinDfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8957,
      "output_tokens": 163,
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
          "output_tokens": 163,
          "cache_read_input_tokens": 8957,
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

_source line 7 · 2026-05-10T19:30:38.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016gTEL6diN9rg31KaKZ9f38`</summary>

```json
{
  "query": "stacking activation sparsity KV eviction LLM inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40b306df-1889-44b2-ab1e-7a4b32482490",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
  "requestId": "req_011CauSfWXTDgLHhg6CB64Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d41d5c7c-ada3-4e39-8660-d633f1682fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uf5GsKysRDs1eBdQbinDfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 8957,
      "output_tokens": 163,
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
          "output_tokens": 163,
          "cache_read_input_tokens": 8957,
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

_source line 8 · 2026-05-10T19:30:45.149Z_

<details><summary>↩ Tool result · `toolu_01NF9wpoht7SY6qPG7u6bFhk`</summary>

```text
Web search results for query: "MLP sparsity orthogonal KV cache compression LLM"

Links: [{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/html/2505.22913v2"},{"title":"GitHub - vllm-project/llm-compressor: Transformers-compatible library for applying various compression algorithms to LLMs for optimized deployment with vLLM · GitHub","url":"https://github.com/vllm-project/llm-compressor"},{"title":"SparKV: Overhead-Aware KV Cache Loading for Efficient On-Device LLM Inference","url":"https://arxiv.org/html/2604.21231"},{"title":"LoRC: Low-Rank Compression for LLMs KV Cache with a Progressive Compression Strategy","url":"https://arxiv.org/html/2410.03111v1"},{"title":"VL-Cache: Sparsity and Modality-Aware KV Cache Compression for Vision-Language Model Inference Acceleration","url":"https://arxiv.org/html/2410.23317v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"KVComp: A High-Performance, LLM-Aware, Lossy Compression Framework for KV Cache","url":"https://arxiv.org/html/2509.00579"},{"title":"Awesome-Efficient-LLM/kv_cache_compression.md at main · horseee/Awesome-Efficient-LLM","url":"https://github.com/horseee/Awesome-Efficient-LLM/blob/main/kv_cache_compression.md"}]

Based on the search results, here's what I found about MLP sparsity, orthogonal KV cache compression, and LLM inference:

## Key Findings

**Orthogonal Compression Approaches:**

Methods like SparK are orthogonal to existing compression techniques, meaning they can be integrated on top of quantization or token-eviction methods to achieve even further memory savings.

**KV Cache Compression Techniques:**

Several recent methods focus on different compression strategies:

1. **Unstructured Sparsity**: Unstructured sparsity can ensure that compressed KV cache perform with minimal model accuracy degradation while being pruned to a higher sparsity. Per-token magnitude pruning is capable of preserving model accuracy even at 70% sparsity.

2. **Low-Rank Compression**: Low-rank compression targets the hidden dimension of KV tensors through low-rank projection of key and value weight matrices, using group-head low-rank decomposition that balances accuracy and reconstruction overhead.

3. **Orthogonal Integration**: Low-rank methods are orthogonal to both quantization and token eviction and can be stacked with either for compounded compression.

**MLP-Related Observations:**

Similar effects to KV cache compression have been documented in the context of improving reasoning by applying low-rank decomposition on the MLP layers.

The search results reveal an active research area with multiple complementary compression techniques that can be combined to achieve significant memory savings in LLM inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40b306df-1889-44b2-ab1e-7a4b32482490",
  "isSidechain": true,
  "promptId": "d34ede03-7cfc-42f7-87a4-326aeae7f146",
  "agentId": "a42cf1d58efb497c0",
  "type": "user",
  "uuid": "de30a780-c930-4e0d-815d-134b17ada5ea",
  "sourceToolAssistantUUID": "40b306df-1889-44b2-ab1e-7a4b32482490",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T19:30:45.958Z_

<details><summary>↩ Tool result · `toolu_016gTEL6diN9rg31KaKZ9f38`</summary>

```text
Web search results for query: "stacking activation sparsity KV eviction LLM inference"

Links: [{"title":"Mastering LLM Techniques: Inference Optimization | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/"},{"title":"HillInfer: Efficient Long-Context LLM Inference on the Edge with Hierarchical KV Eviction using SmartSSD","url":"https://arxiv.org/html/2602.18750"},{"title":"MadaKV: Adaptive Modality-Perception KV Cache Eviction ...","url":"https://aclanthology.org/2025.acl-long.652.pdf"},{"title":"KV Admission: Learning What to Write for Efficient Long-Context Inference","url":"https://arxiv.org/html/2512.17452"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/html/2508.15212"},{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...","url":"https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Learning What to Write: Write-Gated KV for Efficient Long-Context Inference","url":"https://arxiv.org/pdf/2512.17452"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/html/2505.22913v2"}]

Based on the search results, here's what I found about the topics you queried:

## Key Findings on Activation Sparsity, KV Eviction, and LLM Inference

**Attention Sparsity in LLMs:**
In long-context scenarios, LLM attention mechanisms exhibit extreme sparsity, with typically less than 20% of historical tokens significantly influencing the final output. Attention scores are not uniformly distributed; they exhibit pronounced sparsity where a small subset of tokens attracts the majority of attention.

**KV Cache Eviction Approaches:**
Modern inference engines employ dynamic KV cache eviction workflow, where during each step of autoregressive decoding, the system computes an importance score for all historical tokens based on the current query, and selectively retains only the highly-scoring top-α percent KV data in the active GPU cache, while evicting, offloading, or dropping the less critical ones into host memory or disk.

**KV Cache Management Framework:**
An ideal efficient inference system can employ Admission to filter the input stream, Selection to focus the attention computation, and Eviction to prune obsolete history from the admitted set, with combining Admission with Selection enabling the system to push the Pareto frontier of efficiency further than either method could achieve in isolation.

**Combination Strategies:**
Combination methods integrate multiple optimization strategies to achieve greater efficiency in KV cache management than any single technique alone, often combining eviction, compression, and hybrid memory solutions to balance memory savings, computational cost, and accuracy, with some methods applying token selection algorithms alongside quantization to reduce cache size.

**Unstructured Sparsity Benefits:**
Unstructured sparsity offers superior sparsity ratios over structured sparsity while preserving accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d41d5c7c-ada3-4e39-8660-d633f1682fa0",
  "isSidechain": true,
  "promptId": "d34ede03-7cfc-42f7-87a4-326aeae7f146",
  "agentId": "a42cf1d58efb497c0",
  "type": "user",
  "uuid": "670da748-2ddd-4db1-8b5d-194828b1a5e3",
  "sourceToolAssistantUUID": "d41d5c7c-ada3-4e39-8660-d633f1682fa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:30:46.879Z_

<details><summary>↩ Tool result · `toolu_01Gaf5jwny6VZUCfVYpCCRW6`</summary>

```text
Web search results for query: "composable LLM inference efficiency methods 2025 2026"

Links: [{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"Experts are all you need: A Composable Framework for Large Language Model Inference","url":"https://arxiv.org/html/2511.22955"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"llm-d: Intelligent Inference at Scale — Beyond What More GPUs Can Deliver | by Yakov Beder | Apr, 2026 | Medium","url":"https://medium.com/@yakovbeder/llm-d-the-inference-scheduler-that-fixes-what-more-gpus-cant-03644ac55504"},{"title":"Towards Efficient LLM Inference via Collective and Adaptive Speculative Decoding | Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis","url":"https://dl.acm.org/doi/10.1145/3712285.3759834"},{"title":"Ultimate Guide - The Best LLMs Optimized for Inference Speed in 2026","url":"https://www.siliconflow.com/articles/en/best-llms-optimized-for-inference-speed"},{"title":"Best LLM Inference Engines in 2026: vLLM, TensorRT-LLM, TGI, and SGLang Compared | Yotta Labs","url":"https://www.yottalabs.ai/post/best-llm-inference-engines-in-2026-vllm-tensorrt-llm-tgi-and-sglang-compared"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"LARGE LANGUAGE MODEL INFERENCE ACCELERATION:","url":"https://dai.sjtu.edu.cn/my_file/pdf/a43c4dc7-6132-49cb-b737-311eefde646f.pdf"},{"title":"Ultimate Guide - The Fastest Small LLMs for Inference in 2026","url":"https://www.siliconflow.com/articles/en/fastest-small-LLMs-for-inference"}]

I've found comprehensive information on composable LLM inference efficiency methods in 2025-2026. Here are the key findings:

## Composable Inference Frameworks

Comp-LLM is a composable LLM inference framework that enables cross-expert collaboration via an explicit sub-query dependency graph and improves question-answering and reasoning capabilities while reducing memory footprint through sub-query generation and cross-expert collaboration. The framework consists of three key components – a Sub-query Generator, a Query Executor and a Response Aggregator.

## Composable Inference Scheduling Approaches

A composable system enables you to start with simple prefix-aware routing and progressively layer on P/D disaggregation, tiered KV caching, expert parallelism, and SLO-aware autoscaling as your workload demands. Intelligent inference scheduling includes prefix cache-aware routing across vLLM replicas.

## Key Efficiency Methods

Several complementary techniques are emerging:

1. **Speculative Decoding**: Smurfs is an LLM inference system designed to accelerate LLM inference through collective and adaptive speculative decoding, adopting a majority-voted mechanism that harnesses multiple SSMs to collaboratively predict LLM outputs in multi-task scenarios.

2. **Model Architectures**: Cheaper, efficient hybrid architectures are becoming a bigger priority in leading labs (Qwen3-Next, Kimi Linear, Nemotron 3).

3. **Inference-Time Scaling**: There will be more focus on inference-time scaling in 2026, which means spending more time and money after training when letting the LLM generate the answer.

4. **Hardware-Optimized Kernels**: Comprehensive analytical models estimate LLM inference performance with composable and reusable high-level synthesis (HLS) kernels.

These composable methods allow teams to progressively optimize their LLM inference pipelines based on specific workload demands.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f101521-fc26-470d-9d07-68db2a1291d3",
  "isSidechain": true,
  "promptId": "d34ede03-7cfc-42f7-87a4-326aeae7f146",
  "agentId": "a42cf1d58efb497c0",
  "type": "user",
  "uuid": "2ffc80f6-70ba-4af6-ac9d-5e74baee8935",
  "sourceToolAssistantUUID": "4f101521-fc26-470d-9d07-68db2a1291d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T19:30:50.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UoFHuNidCXup6hAu87spv2`</summary>

```json
{
  "query": "\"activation sparsity\" \"KV cache\" independent orthogonal composable inference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ffc80f6-70ba-4af6-ac9d-5e74baee8935",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
  "requestId": "req_011CauSgUXRmbDJcJxo8cRJk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25669726-368e-4758-939c-e13659953577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVew9zR66LB1u3ZuCSJyo6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2020,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 10349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1268,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T19:30:50.841Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NUizPqJpt3Kxe5Nxz5cZWL`</summary>

```json
{
  "query": "MUSTAFAR SparK unstructured sparsity KV cache orthogonal complementary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25669726-368e-4758-939c-e13659953577",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
  "requestId": "req_011CauSgUXRmbDJcJxo8cRJk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2beae8ea-4197-43db-bad1-bad1b7d887c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AVew9zR66LB1u3ZuCSJyo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2020,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 10349,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1268
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2020,
          "output_tokens": 127,
          "cache_read_input_tokens": 10349,
          "cache_creation_input_tokens": 1268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1268,
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

_source line 13 · 2026-05-10T19:30:56.700Z_

<details><summary>↩ Tool result · `toolu_01UoFHuNidCXup6hAu87spv2`</summary>

```text
Web search results for query: ""activation sparsity" "KV cache" independent orthogonal composable inference 2025"

Links: [{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys","url":"https://arxiv.org/html/2603.14224"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"[2602.08329] Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference","url":"https://arxiv.org/abs/2602.08329"},{"title":"LMCACHE: AN EFFICIENT KV CACHE LAYER FOR ENTERPRISE-SCALE LLM INFERENCE","url":"https://lmcache.ai/tech_report.pdf"},{"title":"Awesome-LLM-Compression/README.md at main · HuangOwen/Awesome-LLM-Compression","url":"https://github.com/HuangOwen/Awesome-LLM-Compression/blob/main/README.md"},{"title":"MiniKV: Pushing the Limits of 2-Bit KV Cache via ...","url":"https://aclanthology.org/2025.findings-acl.952.pdf"},{"title":"PALU: KV-CACHE COMPRESSION WITH LOW-RANK ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7da6e0e00702c60607a6ae05c802ef85-Paper-Conference.pdf"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf?id=C69741fMFX"}]

Based on the search results, I found several recent 2025 research papers that address topics related to KV cache optimization, sparsity, and inference efficiency. Here are the key findings:

## Key Research Areas

**KV Cache Compression with Orthogonal Methods:**
TurboQuant achieves near-optimal distortion rates by compressing each key or value vector independently through random orthogonal rotation that isotropizes the vector, which relates to your interest in orthogonal transformations.

**Activation Sparsity:**
Training-free activation sparsity in large language models is being researched (Liu et al., 2025), addressing efficient inference without requiring model retraining.

**Composable and Independent Inference Methods:**
Several quantization methods are orthogonal to KV cache compression approaches like Expected Attention, making it possible to integrate them. Additionally, research proposes unified optimization paradigms that integrate compression and sparsity in mutually compatible ways using single compact formats that support top-k selection directly in the compressed domain.

**Sparsity-Based Approaches:**
Multiple orthogonal pre-hoc selectors are being instantiated along different dimensions for KV cache selection, enabling complementary sparsity strategies.

These papers demonstrate active research in 2025 on making KV cache compression techniques more orthogonal and composable, which aligns with efficient inference systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25669726-368e-4758-939c-e13659953577",
  "isSidechain": true,
  "promptId": "d34ede03-7cfc-42f7-87a4-326aeae7f146",
  "agentId": "a42cf1d58efb497c0",
  "type": "user",
  "uuid": "5491eee4-93db-4a0a-809e-4f1f0bbf42b7",
  "sourceToolAssistantUUID": "25669726-368e-4758-939c-e13659953577",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:30:57.746Z_

<details><summary>↩ Tool result · `toolu_01NUizPqJpt3Kxe5Nxz5cZWL`</summary>

```text
Web search results for query: "MUSTAFAR SparK unstructured sparsity KV cache orthogonal complementary"

Links: [{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/html/2505.22913v2"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/html/2508.15212"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf?id=C69741fMFX"},{"title":"[2508.15212] SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning","url":"https://arxiv.org/abs/2508.15212"},{"title":"[2505.22913] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/abs/2505.22913"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=C69741fMFX"},{"title":"Paper page - Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://huggingface.co/papers/2505.22913"},{"title":"GitHub - dhjoo98/mustafar: codebase for MUSTAFAR:Promoting Unstructured Sparsity for KV Pruning in LLM Inference","url":"https://github.com/dhjoo98/mustafar"},{"title":"NeurIPS Poster MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119320"}]

Based on the search results, here's what I found about MUSTAFAR, SparK, unstructured sparsity, KV cache, and their orthogonal/complementary properties:

## MUSTAFAR

MUSTAFAR promotes unstructured sparsity for KV cache, finding that removing constraints on the sparsity pattern allows compressed KV cache to perform with minimal model accuracy degradation while being pruned to higher sparsity. The method uses per-token magnitude-based pruning as highly effective for both Key and Value caches under unstructured sparsity, surpassing prior structured pruning schemes. Their custom attention kernel coupled with a bitmap-based format delivers substantial compression of KV cache up to 45% of dense inference, enabling longer context lengths and throughput increases of up to 2.23x compared to dense inference.

## SparK

SparK is a training-free plug-and-play method that applies unstructured sparsity by pruning KV at the channel level, while dynamically restoring the pruned entries during attention score computation. SparK reduces KV cache storage by over 30% compared to eviction-based methods while preserving or improving model accuracy, and maintains performance with less than 5% degradation even with an aggressive 80% pruning ratio.

## Orthogonal and Complementary Properties

Both methods are designed to be orthogonal and complementary to existing KV compression techniques. MUSTAFAR's per-token magnitude-based pruning demonstrates strong compatibility with orthogonal compression techniques. SparK's approach is orthogonal to existing KV compression and quantization techniques, making it compatible for integration with them to achieve further acceleration. SparK can be integrated on top of quantization or token-eviction methods to achieve even further memory savings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2beae8ea-4197-43db-bad1-bad1b7d887c3",
  "isSidechain": true,
  "promptId": "d34ede03-7cfc-42f7-87a4-326aeae7f146",
  "agentId": "a42cf1d58efb497c0",
  "type": "user",
  "uuid": "9dc14133-5557-4175-bf47-f46a078ff91b",
  "sourceToolAssistantUUID": "2beae8ea-4197-43db-bad1-bad1b7d887c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T19:31:01.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PeaDUWrNNXrxrzKtgsJ6rq`</summary>

```json
{
  "query": "\"MLP sparsity\" \"attention sparsity\" combined additive speedup LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dc14133-5557-4175-bf47-f46a078ff91b",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
  "requestId": "req_011CauShGyvmRbtoVEuKx84K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3f0fefc-cde7-4e22-92d0-ebc8d58e318c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mFGtzQf6gkNahRvyFcEAv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 11617,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4089
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 11617,
          "cache_creation_input_tokens": 4089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4089,
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

_source line 16 · 2026-05-10T19:31:09.335Z_

<details><summary>↩ Tool result · `toolu_01PeaDUWrNNXrxrzKtgsJ6rq`</summary>

```text
Web search results for query: ""MLP sparsity" "attention sparsity" combined additive speedup LLM 2025 2026"

Links: [{"title":"Track: Session 7: Quantization and Sparsity","url":"https://mlsys.org/virtual/2025/session/3153"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"},{"title":"Accelerating LLM Inference Using Sparsity Kira Selby, Varun Khare NimbleEdge","url":"https://www.nimbleedge.com/sparsity-white-paper.pdf"},{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"LLaMA-MoE v2: Exploring Sparsity of LLaMA from Perspective of Mixture-of-Experts with Post-Training","url":"https://arxiv.org/html/2411.15708"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=lqHv6dxBkj"},{"title":"SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs | OpenReview","url":"https://openreview.net/forum?id=HmwneoGoy9"},{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"MoA: Mixture of Sparse Attention for Automatic Large Language Model Compression | OpenReview","url":"https://openreview.net/forum?id=konDsSUSqg"}]

I found several relevant research papers and resources about combined MLP and attention sparsity approaches for LLMs in 2025-2026. Here are the key findings:

## Combined Sparsity Approaches

Polar Sparsity demonstrates that as batch size and sequence length grow, the importance of sparsity transitions from MLP layers to Attention layers, where head-level sparsity remains stable. By developing sparsity-aware GPU kernels for both MLP and Attention layers, it achieves consistent speedups across models and batch sizes with minimal accuracy impact, delivering up to 2.2× end-to-end speedups in large-scale settings.

## Multiplicative Speedups

LServe demonstrates the compatibility of static and dynamic sparsity in long-context LLM attention, enabling multiplicative speedups by combining these optimizations.

## Complementary Nature of Techniques

These techniques address distinct bottlenecks and are often complementary, enabling combined use for greater gains. Additionally, activation sparsity is complementary to other methods like model compression and efficient sampling and can be combined with these techniques to enhance inference speed.

## MLP Sparsity Challenges in Modern Models

A key challenge noted in recent work is that activation sparsity in older LLMs was largely made possible by high natural sparsity in ReLU-based MLP blocks, but newer architectures typically use non-ReLU-based MLPs (e.g., SwiGLU), making these methods difficult to use in practice.

The research suggests that combining MLP and attention sparsity offers multiplicative rather than purely additive speedups when properly coordinated, though the specific magnitude of combined benefits depends on implementation details and hardware considerations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3f0fefc-cde7-4e22-92d0-ebc8d58e318c",
  "isSidechain": true,
  "promptId": "d34ede03-7cfc-42f7-87a4-326aeae7f146",
  "agentId": "a42cf1d58efb497c0",
  "type": "user",
  "uuid": "8000116a-9768-442a-9acb-a52aacaa2398",
  "sourceToolAssistantUUID": "d3f0fefc-cde7-4e22-92d0-ebc8d58e318c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T19:31:28.146Z_

Here is my summary of the findings:

---

**Summary of Research on Composability of LLM Inference Efficiency Methods (2025-2026)**

There is meaningful precedent for claiming that different efficiency axes are composable/orthogonal, though I did not find a single paper that cleanly isolates "MLP activation sparsity + KV cache compression" as two independent modules and proves strict additivity. Here is what exists:

**Explicit orthogonality claims (KV cache domain):** SparK (arXiv 2508.15212) and MUSTAFAR (arXiv 2505.22913, NeurIPS 2025) both explicitly state their unstructured KV-cache sparsity methods are "orthogonal to existing compression techniques" such as quantization and token eviction, and can be stacked for compounded savings. SparK reports composing channel pruning on top of quantization/eviction for additive memory reduction.

**Combined MLP + Attention sparsity:** Polar Sparsity (arXiv 2505.14884) develops sparsity-aware GPU kernels for both MLP and Attention layers jointly, showing up to 2.2x end-to-end speedup. It demonstrates that the two sources of sparsity target different bottlenecks (MLP dominates at small batch, attention at large batch), supporting the view they are complementary axes.

**Composable framework-level work:** The "Experts Are All You Need" framework (arXiv 2511.22955) and systems like LMCache treat efficiency methods as composable modules (prefix caching, KV compression, disaggregation) that can be layered progressively.

**Gap:** No paper I found explicitly measures activation-sparsity speedup independently, KV-compression speedup independently, and then their product/sum when composed -- the clean "orthogonality proof" you are looking for. The closest is Polar Sparsity's demonstration that MLP and attention sparsity address distinct bottlenecks and compose for multiplicative gains.

Sources:
- [SparK (arXiv 2508.15212)](https://arxiv.org/abs/2508.15212)
- [MUSTAFAR (arXiv 2505.22913)](https://arxiv.org/abs/2505.22913)
- [Polar Sparsity (arXiv 2505.14884)](https://arxiv.org/pdf/2505.14884)
- [Experts Are All You Need (arXiv 2511.22955)](https://arxiv.org/html/2511.22955)
- [SparK - AMD ROCm Blog](https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html)
- [Top 10 KV Cache Compression Techniques - MarkTechPost](https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/)
- [Training-Free Activation Sparsity (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8000116a-9768-442a-9acb-a52aacaa2398",
  "isSidechain": true,
  "agentId": "a42cf1d58efb497c0",
  "requestId": "req_011CauSi8ZgxDLEEQ65U6RVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23641bfe-ead9-4ae6-9362-ff4215172db6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d38e82e7-0ffb-4fef-8704-b3642f0be851",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sitHUNPYGRo4f9shJcqax",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1010,
      "cache_read_input_tokens": 15706,
      "output_tokens": 798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1010
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 798,
          "cache_read_input_tokens": 15706,
          "cache_creation_input_tokens": 1010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1010,
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
