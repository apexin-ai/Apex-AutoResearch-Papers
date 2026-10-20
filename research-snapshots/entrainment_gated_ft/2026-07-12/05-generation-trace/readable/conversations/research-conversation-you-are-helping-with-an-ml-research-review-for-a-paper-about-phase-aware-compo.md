# Research conversation: You are helping with an ML research review for a paper about "Phase-Aware Compound Sparsity" that coordinates attention 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 120
- **Recorded user turns:** 1
- **Tool calls:** 57
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af3b761bcbdccae6c.jsonl`
- **Structured JSON:** [`8582287c318c4176bde4.json`](../../sessions/85/8582287c318c4176bde4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

120 recorded events

### User

_source line 1 · 2026-05-10T19:35:35.442Z_

You are helping with an ML research review for a paper about "Phase-Aware Compound Sparsity" that coordinates attention head sparsity, KV cache compression, and MLP sparsity conditioned on reasoning phase for efficient LLM inference.

Search for concurrent/recent work (2025-2026) that the proposal may have missed. Focus on:

1. **Multi-axis / compound sparsity for LLM inference** (combining multiple compression dimensions):
   - "compound sparsity LLM inference 2026"
   - "multi-axis compression LLM 2026"  
   - "joint pruning quantization sparsity LLM inference"

2. **Phase-aware or adaptive inference methods for reasoning models**:
   - "adaptive inference reasoning LLM 2026"
   - "phase-aware reasoning model inference"
   - "dynamic sparsity reasoning models 2026"

3. **Recent KV cache compression for reasoning models** (beyond what's cited):
   - "KV cache compression reasoning models 2026"
   - "thinking trace compression LLM 2026"

4. **Compound controller / routing for inference efficiency**:
   - "learned router inference efficiency LLM 2026"
   - "mixture of experts routing inference sparsity"

5. **Check known teams working on this**: 
   - "DeepSeek inference efficiency 2026"
   - "Meta LLM inference sparsity 2026"
   - "Google sparse attention reasoning 2026"

6. **Check ICML 2026 and NeurIPS 2026 submissions**:
   - "site:openreview.net compound sparsity 2026"
   - "ICML 2026 efficient inference"

For any important work you find that is NOT in this list of already-cited papers, report the title, venue, and how it relates:
Already cited: Polar Sparsity, ThinKV, RaaS, R-KV, RLKV, FASA, AMP, Deja Vu, LazyEviction, SLiM, TriAttention, LongFlow, Phase Transitions, WiSparse, DepthKV, SpeContext, Flux Attention, KV Pareto, MiniLongBench, EvoSparse, The Sparse Frontier, Thinking Sparks, "Doing More With Less"

Report what you find - especially anything highly relevant that's missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "db0efffa-4f3b-4c53-951d-0586d20ebd67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:35:35.446Z_

```json
{
  "parentUuid": "db0efffa-4f3b-4c53-951d-0586d20ebd67",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
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
  "uuid": "64159056-8538-417c-be5d-48f53df21502",
  "timestamp": "2026-05-10T19:35:35.446Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:35:38.688Z_



I'll conduct a comprehensive search for concurrent and recent work that may be missing from the paper's citations. Let me search across multiple dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64159056-8538-417c-be5d-48f53df21502",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT3kG4gcKrbBmitjRQn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb3f8710-547c-4b4e-a7ee-5609b03f4dd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuvAweB83sFBQPWAbx4wTu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1101,
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

_source line 4 · 2026-05-10T19:35:39.207Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018Mq32TDVsdpefGrweHHyqf`</summary>

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
  "parentUuid": "eb3f8710-547c-4b4e-a7ee-5609b03f4dd8",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT3kG4gcKrbBmitjRQn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c3733f6-51d9-41cd-ae8e-4a2be6ea3495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuvAweB83sFBQPWAbx4wTu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 7304,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 1101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1101,
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

_source line 5 · 2026-05-10T19:35:39.210Z_

<details><summary>↩ Tool result · `toolu_018Mq32TDVsdpefGrweHHyqf`</summary>

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
  "parentUuid": "4c3733f6-51d9-41cd-ae8e-4a2be6ea3495",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "555efa51-19f2-4bc6-94f4-b16bf30b2dc0",
  "sourceToolAssistantUUID": "4c3733f6-51d9-41cd-ae8e-4a2be6ea3495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:35:46.198Z_



Now let me launch all the searches in parallel across the key dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "555efa51-19f2-4bc6-94f4-b16bf30b2dc0",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT43RBchRZgNDUyi3No",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12c4c1b1-7d46-466c-a6c2-0088a4d9d35d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MpRzkkEnH4MTr7okTzqy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 7 · 2026-05-10T19:35:46.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XTvCeUbxSTuYFrLHtDyb2Z`</summary>

```json
{
  "query": "compound sparsity LLM inference 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12c4c1b1-7d46-466c-a6c2-0088a4d9d35d",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT43RBchRZgNDUyi3No",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cf1e798-eb38-4c29-9821-08db5e0a5857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MpRzkkEnH4MTr7okTzqy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 8405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1423,
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

_source line 8 · 2026-05-10T19:35:55.173Z_

<details><summary>↩ Tool result · `toolu_01XTvCeUbxSTuYFrLHtDyb2Z`</summary>

```text
Web search results for query: "compound sparsity LLM inference 2026"

Links: [{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"Faster LLMs by Reshaping Sparsity | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/technology/2026/faster-llms-by-reshaping-sparsity"},{"title":"LLM Architecture 2026: Key Changes and Deployment Insights - Sesame Disk","url":"https://sesamedisk.com/llm-architecture-gallery-2026/"},{"title":"GitHub - deepseek-ai/Engram: Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models · GitHub","url":"https://github.com/deepseek-ai/Engram"},{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference | OpenReview","url":"https://openreview.net/forum?id=AqpDRGnu82"},{"title":"GitHub - SakanaAI/sparser-faster-llms: Cuda kernels for leveraging LLM sparsity to improve throughput and decrease the memory requirements during inference and training. · GitHub","url":"https://github.com/SakanaAI/sparser-faster-llms"},{"title":"[2310.17157] Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/abs/2310.17157"},{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"[2601.07372] Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models","url":"https://arxiv.org/abs/2601.07372"},{"title":"Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling | ACM Transactions on Architecture and Code Optimization","url":"https://dl.acm.org/doi/10.1145/3764589"}]

Based on the search results, here's what's happening with compound sparsity and LLM inference in 2026:

## Key Developments in 2026

**Hardware-Aware Sparsity Optimization**

Sakana AI and NVIDIA unveiled a new method that reshapes sparsity in LLMs to boost GPU efficiency, achieving over 20% speedups. The innovation introduces a new format called TwELL (Tile-wise ELLPACK), a hybrid representation that dynamically routes the 99% of sparse tokens through a fast path, using a dense backup matrix for less frequent, intensive tokens.

**Multiple Sparsity Axes**

Researchers uncovered a U-shaped scaling law that optimizes the trade-off between neural computation (MoE) and static memory (Engram). While Mixture-of-Experts scales capacity via conditional computation, the approach introduces conditional memory as a complementary sparsity axis, instantiated via Engram, a module for O(1) lookup.

**Industry Shift to Efficiency**

The biggest change since March 2026 is the shift from scale to efficiency as the primary design goal, with cost per inference, not parameter count, now determining competitive advantage.

**Research Momentum**

Sparsity-based techniques are proving critical for improving efficiency while also enhancing interpretability and modularity, with scope spanning Mixture of Experts, LLM inference and serving, network pruning, sparse training, distillation, and quantization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cf1e798-eb38-4c29-9821-08db5e0a5857",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "a4f32740-b3c8-4550-b645-cb1a0bcb9599",
  "sourceToolAssistantUUID": "2cf1e798-eb38-4c29-9821-08db5e0a5857",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T19:35:57.166Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DftobTF9tCMxXYgWhm2RLj`</summary>

```json
{
  "query": "multi-axis compression joint pruning quantization sparsity LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4f32740-b3c8-4550-b645-cb1a0bcb9599",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT5ChKTVeNZzvrBWCfJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5440b14-26d3-4c37-85a4-2e4c0149cf80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDSsnMBwrUUcR4Z8BhXfAk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 9828,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1041
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 9828,
          "cache_creation_input_tokens": 1041,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1041,
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

_source line 10 · 2026-05-10T19:36:10.908Z_

<details><summary>↩ Tool result · `toolu_01DftobTF9tCMxXYgWhm2RLj`</summary>

```text
Web search results for query: "multi-axis compression joint pruning quantization sparsity LLM 2025 2026"

Links: [{"title":"Large Language Model Compression with Global Rank and Sparsity Optimization","url":"https://arxiv.org/html/2505.03801"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.14569"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.18426"},{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"Frontiers | A survey of model compression techniques: past, present, and future","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1518965/full"},{"title":"Automatic Joint Structured Pruning and Quantization for Efficient Neural","url":"https://arxiv.org/pdf/2502.16638"},{"title":"[2502.16638] Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression","url":"https://arxiv.org/abs/2502.16638"},{"title":"Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression","url":"https://arxiv.org/html/2502.16638v1"},{"title":"Compressing large language models by joint sparsification and quantization | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692743"}]

Here are the web search results for your query on multi-axis compression, joint pruning, quantization, sparsity, and LLMs from 2025-2026:

## Key Recent Work

**Joint Compression Techniques:**

Joint Sparsification and Quantization (JSQ) is a novel compression technique explicitly tailored for LLMs that integrates sparsification and quantization cohesively, addressing the limitations of applying these methods individually.

A quantization-aware structured sparse optimizer called QASSO provides reliable joint structured pruning and mixed-precision quantization-aware training, and is the first white-box joint optimizer that explicitly controls the sparsity ratio and bit width.

**Hybrid Compression Methods:**

Hybrid methods combine sparsity with quantization or low precision: SpQR (Dettmers et al., 2024) stores a tiny FP16 outlier matrix plus 4-bit weights, achieving sub-1% perplexity loss, while CALDERA (Saha et al., 2024) represents each layer as a low-rank term plus a quantized backbone, pushing below 3 bits/parameter on models up to 70B.

**Research Challenges:**

A rigorous theoretical understanding of how hybrid compression errors interact remains limited, with recent studies beginning to formally analyze the combined effects of sparsity and quantization. Developing joint optimization strategies or analytical bounds that predict the compounded impact of multiple compression methods remains a key unresolved problem.

**Unified Evaluation Frameworks:**

UniComp is a unified evaluation framework for comparing pruning, quantization, and knowledge distillation that evaluates compressed models along three dimensions: performance, reliability, and efficiency.

The search results show significant progress in 2025-2026 toward more sophisticated joint compression approaches that balance multiple optimization axes simultaneously.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5440b14-26d3-4c37-85a4-2e4c0149cf80",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "f70f8937-ecfc-4edb-b476-d58a5ed072d6",
  "sourceToolAssistantUUID": "f5440b14-26d3-4c37-85a4-2e4c0149cf80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T19:36:12.744Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ARxvuT8wS9RpRDmWduGJoo`</summary>

```json
{
  "query": "adaptive inference reasoning LLM 2026 dynamic computation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f70f8937-ecfc-4edb-b476-d58a5ed072d6",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT6MtFC3phRrfAiRRAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71025fc0-0fd4-4c9f-a259-6eb35a2f2820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JQxcjtzy3F2LvcAomHjbJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1009,
      "cache_read_input_tokens": 10869,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1009
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 10869,
          "cache_creation_input_tokens": 1009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1009,
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

_source line 12 · 2026-05-10T19:36:20.618Z_

<details><summary>↩ Tool result · `toolu_01ARxvuT8wS9RpRDmWduGJoo`</summary>

```text
Web search results for query: "adaptive inference reasoning LLM 2026 dynamic computation"

Links: [{"title":"Adaptive Parallel Reasoning: Scaling Inference with Dynamic Control • Dev|Journal","url":"https://earezki.com/ai-news/2026-05-08-adaptive-parallel-reasoning-the-next-paradigm-in-efficient-inference-scaling/"},{"title":"From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models","url":"https://arxiv.org/html/2511.10788v2"},{"title":"Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better,","url":"https://arxiv.org/pdf/2410.02725"},{"title":"Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better, Even Mid-Generation","url":"https://arxiv.org/html/2410.02725v1"},{"title":"Adaptive-solver framework for dynamic strategy selection in large language model reasoning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457324004114"},{"title":"Dynamic Adaptive Reasoning: Optimizing LLM Inference-Time Thinking via Intent-Aware Scheduling[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202511.0291"},{"title":"Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better, Even Mid-Generation | OpenReview","url":"https://openreview.net/forum?id=7tOc6h8bea"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853"},{"title":"DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference","url":"https://arxiv.org/html/2510.19669"},{"title":"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.54/"}]

Here are the search results for "adaptive inference reasoning LLM 2026 dynamic computation":

## Key Findings

**Adaptive Parallel Reasoning**
Researchers at Berkeley AI Research have introduced Adaptive Parallel Reasoning to overcome the linear scaling limits of sequential inference. Current reasoning models can take tens of minutes or hours to solve complex tasks due to sequential token generation costs.

**Defining Adaptive Reasoning**
Recent research reframes the focus from mere efficiency to adaptivity. Adaptive reasoning in LLMs is defined as the capability to allocate reasoning effort based on input characteristics such as difficulty and uncertainty. This adaptivity can be realized through learned policies that internalize allocation strategies during training, or through dynamic control mechanisms applied at inference time.

**Dynamic Compute Allocation**
Models can dynamically allocate compute during inference based on task complexity and the model's capability, optimizing resource usage and ensuring efficiency in processing all types of prompts and tasks.

**Practical Frameworks**
The Adaptive-Solver framework is designed to dynamically adapt solving strategies for LLMs across diverse reasoning scenarios, allowing for flexible allocation of test-time computational resources through an initial evaluation module and a subsequent adaptation module.

**Recent Advances (2025-2026)**
DiffAdapt is a lightweight framework that selects inference strategies based on question difficulty, achieving comparable or improved accuracy while reducing token usage by up to 22.4%. LLMs are effective at predicting necessary formal reasoning strategies with accuracy above 90%, enabling flexible integration with formal logical solvers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71025fc0-0fd4-4c9f-a259-6eb35a2f2820",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "701ab3cc-fe9b-46d0-a54f-34d97dd53732",
  "sourceToolAssistantUUID": "71025fc0-0fd4-4c9f-a259-6eb35a2f2820",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T19:36:22.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011E5zW3tLL83TfhseT74YeL`</summary>

```json
{
  "query": "phase-aware reasoning model inference sparsity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "701ab3cc-fe9b-46d0-a54f-34d97dd53732",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT75QKxS4NeYPNbttPP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd0727a7-a82e-47ce-9fca-b202f76392c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kj7F4maHtT7JLfHAAzxVS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 960,
      "cache_read_input_tokens": 11878,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 960
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 11878,
          "cache_creation_input_tokens": 960,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 960,
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

_source line 14 · 2026-05-10T19:36:30.173Z_

<details><summary>↩ Tool result · `toolu_011E5zW3tLL83TfhseT74YeL`</summary>

```text
Web search results for query: "phase-aware reasoning model inference sparsity 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.03152"},{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.01278v1"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"A Survey of Efficient LLM Inference Serving","url":"https://aclanthology.org/2025.inlg-main.32.pdf"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=500&show=2000"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=1525&show=2000"}]

Based on the search results, I found several relevant papers and discussions about phase-aware reasoning models and inference sparsity from 2025-2026:

## Key Findings:

**FASA (Frequency-Aware Sparse Attention)** - A recent approach that focuses on training-free inference in the decoding phase, rooted in the observation that differential frequencies within RoPE (Rotary Position Embedding) induce functional sparsity among frequency chunks. The framework uncovers functional sparsity at frequency chunk level induced by RoPE, with FASA-M providing 8× compression of the KV cache and FASA-C delivering 2.6× speedups.

**SparseSpec** - A speculative decoding framework for reasoning language models that features a novel sparse attention mechanism called PillarAttn, which accurately selects critical tokens via reusing information from the verification stage. The sparsity pattern adapts continuously to the evolving context, crucial for RLM workloads where reasoning chains can shift topics and focus areas.

**Broader Context** - Efficient reasoning can dramatically lower compute cost by pruning unnecessary chain-of-thought reasoning. Additionally, Claude employs hybrid symbolic-neural reasoning strategies that dynamically adjust computational depth depending on task complexity, enabling more efficient inference pipelines and lower average computation.

These approaches represent the frontier of phase-aware and sparsity-based optimization for reasoning model inference in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd0727a7-a82e-47ce-9fca-b202f76392c6",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "d6e9637b-0d0f-4c7b-9dc7-c4396ebf14ea",
  "sourceToolAssistantUUID": "bd0727a7-a82e-47ce-9fca-b202f76392c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T19:36:31.974Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vh54Astk2vs2XoQL5RXrpd`</summary>

```json
{
  "query": "KV cache compression reasoning models thinking trace 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6e9637b-0d0f-4c7b-9dc7-c4396ebf14ea",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT7nFUqCkpFDGAqaYzg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b389c216-bc3b-4e60-8a80-8c6fedc7ea80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaDrPUy6ckuiAkcJksQcC9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 12838,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 12838,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 875,
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

_source line 16 · 2026-05-10T19:36:38.610Z_

<details><summary>↩ Tool result · `toolu_01Vh54Astk2vs2XoQL5RXrpd`</summary>

```text
Web search results for query: "KV cache compression reasoning models thinking trace 2025 2026"

Links: [{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=udgrpHqw4F"},{"title":"Utilizing KV Cache for Sampling and Reasoning","url":"https://arxiv.org/pdf/2601.20326"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"NeurIPS Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://neurips.cc/virtual/2025/loc/san-diego/126664"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution | OpenReview","url":"https://openreview.net/forum?id=k5h29Qv7GN"}]

Based on the search results, here's what I found about KV cache compression for reasoning models with thinking traces in 2025-2026:

## Key Research Areas

Short but complex prompts, such as those in benchmarks like GSM8K and MATH500, often benefit from multi-step reasoning and self-reflection, resulting in thinking sequences thousands of tokens long. This poses significant challenges for memory management.

## Major Approaches

**ThinKV**: ThinKV is a thought-adaptive KV cache compression framework based on the observation that attention sparsity reveals distinct thought types with varying importance within the chain of thought. It achieves near-lossless accuracy with less than 5% of the original KV cache, while improving performance with up to 5.8x higher inference throughput.

**R-KV**: R-KV is a redundancy-aware KV-cache compression for reasoning models that solves this by ranking tokens on-the-fly for both importance and non-redundancy, retaining only the informative, diverse ones. At 16% (Llama-8B) or 33% (Qwen-14B) cache, R-KV reaches 105% of FullKV accuracy.

## Benchmarking Results

H2O and a decoding-enabled variant of SnapKV are dominant strategies for reasoning models, indicating the utility of heavy-hitter tracking for reasoning traces.

## Related Work

ForesightKV is a training-based KV cache eviction framework that learns to predict which KV pairs to evict during long-text generations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b389c216-bc3b-4e60-8a80-8c6fedc7ea80",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "9e3351bd-dbad-43e7-9c74-c48bb4fe5762",
  "sourceToolAssistantUUID": "b389c216-bc3b-4e60-8a80-8c6fedc7ea80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T19:36:42.423Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RGkN8oy8hRu3j4C39WMR4D`</summary>

```json
{
  "query": "learned router inference efficiency LLM mixture experts routing sparsity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e3351bd-dbad-43e7-9c74-c48bb4fe5762",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT8QN8LiLfv6ZutGRi4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5822abe9-ba44-4e37-8269-c91716420817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vyW9rCpVLBPQK4dBNkjE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 13713,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 968
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 13713,
          "cache_creation_input_tokens": 968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 968,
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

_source line 18 · 2026-05-10T19:36:51.984Z_

<details><summary>↩ Tool result · `toolu_01RGkN8oy8hRu3j4C39WMR4D`</summary>

```text
Web search results for query: "learned router inference efficiency LLM mixture experts routing sparsity 2026"

Links: [{"title":"Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey","url":"https://arxiv.org/html/2603.04445"},{"title":"What Is Mixture of Experts (MoE)? How Modern LLMs Get Efficient | AI Weekly","url":"https://aiweekly.co/learning-ai/generative-ai/what-mixture-experts-moe-how-modern-llms-get-efficient"},{"title":"ExpertFlow: Efficient Mixture-of-Experts Inference via Predictive Expert Caching and Token Scheduling","url":"https://arxiv.org/html/2410.17954v2"},{"title":"Read-ME: Refactorizing LLMs as Router-Decoupled ...","url":"https://utns.cs.utexas.edu/assets/papers/neurips24-readme.pdf"},{"title":"Read-ME: Refactorizing LLMs as Router-Decoupled Mixture of Experts with System Co-Design","url":"https://arxiv.org/html/2410.19123v1"},{"title":"Refactorizing LLMs as Router-Decoupled Mixture of ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d298cf34e4539f9134db7f38b42f69fe-Paper-Conference.pdf"},{"title":"Universal Model Routing for Efficient LLM Inference","url":"https://arxiv.org/html/2502.08773v2"},{"title":"TensorOpera Router: A Multi-Model Router for Efficient LLM Inference","url":"https://arxiv.org/html/2408.12320v3"},{"title":"CMoE: Converting Mixture-of-Experts from Dense to Accelerate LLM Inference","url":"https://www.arxiv.org/pdf/2502.04416v2"},{"title":"Performance Characterization of Expert Router for Scalable LLM Inference","url":"https://arxiv.org/html/2404.15153v2"}]

I've found comprehensive research results on learned router inference efficiency, mixture of experts, routing sparsity, and LLM optimization. Here's a summary of the key findings:

## Mixture of Experts (MoE) in Modern LLMs

Mixture of Experts has become the architecture of choice for frontier language models in 2026, with nearly all frontier language models using some form of MoE architecture. By splitting computation among specialized expert networks and routing each token to only the most relevant experts, MoE breaks the link between model capacity and computational cost.

## Sparse Activation and Efficiency

A model can have 671 billion total parameters, like DeepSeek-V3, but only activate 37 billion for each token. The model stores knowledge across all 671 billion parameters but pays the compute cost of a 37 billion parameter model at inference time.

## Router Design and Inference Optimization

Several recent approaches focus on learned routers for efficiency:

- **RouteLMT**: RouteLMT (Luo et al., 2026) has proposed an in-model router that probes the small translator's prompt-token representations via lightweight LoRA adaptation, identifying the marginal gain as the optimal signal for routing decisions.

- **Read-ME**: This framework proposes decoupling the router from the MoE backbone, allowing pre-gating of all requests (token sequences) before inference and applying lookahead scheduling based on the experts to which tokens will be dispatched.

- **ExpertFlow**: ExpertFlow introduces a unified system for memory-efficient MoE inference by integrating a Routing Path Predictor, a routing-aware Token Scheduler, and a predictive Expert Cache Engine.

## Load Balancing Challenges

MoE architectures face a critical practical problem with load balancing. If the router sends most tokens to a few popular experts while others sit idle, the system loses its efficiency advantage, as popular experts become bottlenecks and computational savings from sparsity disappear.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5822abe9-ba44-4e37-8269-c91716420817",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "896817e7-c927-4808-95a2-35a9ce7764a4",
  "sourceToolAssistantUUID": "5822abe9-ba44-4e37-8269-c91716420817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T19:36:55.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SuCJcku51KiVN9cxQL2XCV`</summary>

```json
{
  "query": "DeepSeek inference efficiency sparsity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "896817e7-c927-4808-95a2-35a9ce7764a4",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauT9PYHuWZHngNEt1oWj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a5e9b31-d08b-405f-8885-0155c06203b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118oGPLWX6kmzeA3fhjVNFX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1068,
      "cache_read_input_tokens": 14681,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1068
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 14681,
          "cache_creation_input_tokens": 1068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1068,
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

_source line 20 · 2026-05-10T19:37:04.501Z_

<details><summary>↩ Tool result · `toolu_01SuCJcku51KiVN9cxQL2XCV`</summary>

```text
Web search results for query: "DeepSeek inference efficiency sparsity 2025 2026"

Links: [{"title":"DeepSeek V4 Review. DeepSeek released V4 as a public… | by Barnacle Goose | Apr, 2026 | Medium","url":"https://medium.com/@leucopsis/deepseek-v4-review-a23ce940151c"},{"title":"DeepSeek-V4: a million-token context that agents can actually use","url":"https://huggingface.co/blog/deepseekv4"},{"title":"DeepSeek: implications for data science and management in the AI era - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666764925000451"},{"title":"DeepSeek V3.2-exp: Redefining AI Inference Cost Economics in 2025 | by Luke Thomas | Medium","url":"https://medium.com/@lukeeboy/deepseek-v3-2-exp-redefining-ai-inference-cost-economics-in-2025-f89abeac833b"},{"title":"DeepSeek's Low Inference Cost Explained: MoE & Strategy | IntuitionLabs","url":"https://intuitionlabs.ai/articles/deepseek-inference-cost-explained"},{"title":"DeepSeek releases 'sparse attention' model that cuts API costs in half | TechCrunch","url":"https://techcrunch.com/2025/09/29/deepseek-releases-sparse-attention-model-that-cuts-api-costs-in-half/"},{"title":"DeepSeek-V3.2-Exp Complete Analysis: 2025 AI Model Breakthrough and In-Depth Analysis of Sparse Attention Technology - DEV Community","url":"https://dev.to/czmilo/deepseek-v32-exp-complete-analysis-2025-ai-model-breakthrough-and-in-depth-analysis-of-sparse-3gcl"},{"title":"DeepSeek Slashes AI Inference Costs 50% With Sparse ...","url":"https://www.techbuzz.ai/articles/deepseek-slashes-ai-inference-costs-50-with-sparse-attention"},{"title":"DeepSeek's new models offer big inference cost savings","url":"https://www.theregister.com/2026/04/24/deepseek_v4/"},{"title":"The DeepSeek Evolution: From Scaling Laws to Reinforced Reasoning | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/the-deepseek-evolution-from-scaling-laws-to-reinforced-reasoning-aacc20a5d467"}]

I found comprehensive information about DeepSeek's inference efficiency and sparsity innovations. Here's what the search results reveal:

## DeepSeek V4 (April 2026)

DeepSeek released V4 as a public preview on April 24, 2026, exposing two hosted variants through its API and signaling that open weights would follow shortly. V4-Pro carries 1.6 trillion total parameters with 49 billion activated per token, while V4-Flash carries 284 billion total with 13 billion active.

The efficiency improvements are substantial: The headline efficiency claim is that V4-Pro reduces single-token inference FLOPs to 27% of V3.2 and KV cache occupancy to 10% of V3.2 at the 1M-token setting.

## Sparsity Architecture

The efficiency gain comes from splitting attention into two mechanisms: Compressed Sparse Attention (CSA) compresses KV entries by 4x along the sequence dimension using softmax-gated pooling, while a lightning indexer picks the top-k compressed blocks per query, inheriting the sparse-selection idea from DeepSeek Sparse Attention in V3.2. Heavily Compressed Attention (HCA) compresses KV entries by 128x and drops the sparse selection, with every query attending densely to every compressed block since the compressed sequence is short enough that dense attention is cheap.

## Earlier Models (2025)

DeepSeek-V3.2 was released December 1, 2025, featuring 685B total parameters and introducing "Thinking in Tool-Use" — the ability to generate reasoning chains before invoking external APIs. DeepSeek released an experimental model called V3.2-exp, designed to have dramatically lower inference costs when used in long-context operations. The V3.2-exp model features breakthrough sparse attention technology that cuts inference costs by up to 50% for long-context operations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a5e9b31-d08b-405f-8885-0155c06203b9",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "23f79f90-244b-4e05-bab0-6e9eec706ef2",
  "sourceToolAssistantUUID": "8a5e9b31-d08b-405f-8885-0155c06203b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T19:37:06.761Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SeJN5CLivPD4a13iMZUCPM`</summary>

```json
{
  "query": "dynamic sparsity reasoning models chain of thought efficient 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23f79f90-244b-4e05-bab0-6e9eec706ef2",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTAK5BpAhgfWrgzYuNn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2253d066-1ded-47fc-baf3-c3d03bcecb15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEUJo2ABdGJhUnxK7ahSFi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 15749,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1308
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 15749,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1308,
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

_source line 22 · 2026-05-10T19:37:14.522Z_

<details><summary>↩ Tool result · `toolu_01SeJN5CLivPD4a13iMZUCPM`</summary>

```text
Web search results for query: "dynamic sparsity reasoning models chain of thought efficient 2025 2026"

Links: [{"title":"Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models","url":"https://arxiv.org/html/2601.18383"},{"title":"From Sparse Dependence to Sparse Attention: Unveiling How Chain-of-Thought Enhances Transformer Sample Efficiency | OpenReview","url":"https://openreview.net/forum?id=AmEgWDhmTr"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.03152"},{"title":"GitHub - fscdc/Awesome-Efficient-Reasoning-Models: [TMLR 2025] Efficient Reasoning Models: A Survey · GitHub","url":"https://github.com/fscdc/Awesome-Efficient-Reasoning-Models"},{"title":"Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks","url":"https://arxiv.org/html/2508.18672v1"},{"title":"[2507.22928] How does Chain of Thought Think? Mechanistic Interpretability of Chain-of-Thought Reasoning with Sparse Autoencoding","url":"https://arxiv.org/abs/2507.22928"},{"title":"How does Chain of Thought Think? Mechanistic ...","url":"https://arxiv.org/pdf/2507.22928"},{"title":" Abstract— In order to address the chain of thought in the","url":"https://arxiv.org/pdf/2411.09111"},{"title":"Reasoning in Large Language Models: From Chain-of-Thought to Massively Decomposed Agentic Processes[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202512.2242"},{"title":"Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models","url":"https://arxiv.org/html/2601.11340v2"}]

I've completed the web search for your query about dynamic sparsity in reasoning models with chain-of-thought and efficiency in 2025-2026. Here's a summary of the key findings:

## Recent Research on Dynamic Sparsity and Efficient Reasoning

The search revealed several important developments in this area:

**Dynamic Sparsity in Thinking Tokens:**
Recent advancements in Large Reasoning Models (LRMs) have significantly strengthened the reasoning capabilities of LLMs, with representative models such as DeepSeek-R1, Gemini-3-Pro, and ChatGPT-5.2 supporting deep thinking mode for challenging mathematics, programming, and science tasks. However, the thinking process necessitates an immense KV cache memory footprint and attention-related computational cost, posing a critical deployment challenge in resource-constrained environments.

**Dynamic Token Selection Approaches:**
Dynamic Thinking-Token Selection (DynTS) is based on the observed sparsity of thinking tokens and the Pareto Principle in Large Reasoning Models.

**Chain-of-Thought and Sparsity:**
Chain-of-thought simplifies the learning process by introducing sparse sequential dependencies among input tokens, and leads to sparse and interpretable attention, with sparsity in attention layers being a key factor of improvement induced by CoT.

**Long Context of Thought Reasoning:**
Research on FASA evaluated performance on long chain-of-thought (LongCoT) reasoning tasks and achieved performance comparable to full KV cache with reduction of less than 0.7%, while consistently surpassing baseline methods.

These developments show active research into making reasoning models more efficient through dynamic sparsity techniques in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2253d066-1ded-47fc-baf3-c3d03bcecb15",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "881fec31-927a-40f2-a1f7-c7c4c039adc7",
  "sourceToolAssistantUUID": "2253d066-1ded-47fc-baf3-c3d03bcecb15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T19:37:18.485Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PCPtqcFW9EaUpR6CSajLSb`</summary>

```json
{
  "query": "Meta LLM inference sparsity attention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "881fec31-927a-40f2-a1f7-c7c4c039adc7",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTB3qvnUrN6rpytKUDr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48953f0b-a102-453a-8d1a-c89de7cd4987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019F33SDQc4mTTwqAWNjpQgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 17057,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 982
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 17057,
          "cache_creation_input_tokens": 982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 982,
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

_source line 24 · 2026-05-10T19:37:26.528Z_

<details><summary>↩ Tool result · `toolu_01PCPtqcFW9EaUpR6CSajLSb`</summary>

```text
Web search results for query: "Meta LLM inference sparsity attention 2025 2026"

Links: [{"title":"Meta Adaptive Ranking Model: Bending the Inference Scaling Curve to Serve LLM-Scale Models for Ads - Engineering at Meta","url":"https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"GitHub - iLearn-Lab/ACL26-EvoSparse: [ACL 2026 main] Official Implementation for Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention · GitHub","url":"https://github.com/iLearn-Lab/ACL26-EvoSparse"},{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/html/2507.19595v3"},{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/html/2504.17768v2"},{"title":"Evolution of Meta’s LLaMA Models and Parameter-Efficient Fine-Tuning of Large Language Models: A Survey","url":"https://arxiv.org/html/2510.12178v1"},{"title":"Scaling LLM Inference: Innovations in Tensor Parallelism, Context Parallelism, and Expert Parallelism - Engineering at Meta","url":"https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/"},{"title":"[2507.19595] Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/abs/2507.19595"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"RetrievalAttention: Accelerating Long-Context LLM Inference via Vector Retrieval | OpenReview","url":"https://openreview.net/forum?id=qBpYqQUFPx"}]

Based on the search results, here's what I found about Meta's work on LLM inference, sparsity, and attention mechanisms in 2025-2026:

## Meta's Recent Advances

Meta's Wukong Turbo architecture utilizes sparsity-based simplification that reduces redundant components in the linear layers, addressing efficiency challenges in LLM inference. Since launching on Instagram in Q4 2025, their Adaptive Ranking Model has delivered a +3% increase in ad conversions and +5% increase in ad click through rate for targeted users.

## LLaMA 4 with Sparse MoE

In April 2025, Meta unveiled LLaMA 4 Scout and Maverick, which both have 17B active parameters organized in a sparse Mixture-of-Experts (MoE) framework, meaning they each route tokens through subsets of many "experts" sub-networks. These models support a 10-million-token context window orders of magnitude beyond prior LLMs.

## Broader Industry Trends

Sparse attention has seen widespread adoption in industry, with over 150 papers with "sparse attention" in the title submitted to arXiv between January 2025 and January 2026. Linear and sparse mechanisms are increasingly viewed as complementary rather than competitive, with linear attention serving as an effective state compressor for fast inference and KV cache reduction, while sparse attention acts as a high-fidelity module to replace full attention during decoding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48953f0b-a102-453a-8d1a-c89de7cd4987",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "eba4903f-c05c-426a-aca7-8ecae974c503",
  "sourceToolAssistantUUID": "48953f0b-a102-453a-8d1a-c89de7cd4987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T19:37:28.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MJcZczQZGuBSKvLuzrB8d7`</summary>

```json
{
  "query": "Google sparse attention reasoning inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eba4903f-c05c-426a-aca7-8ecae974c503",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTBwZBTUSZRtZFJnLUf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "711eb8d5-d04f-4406-9063-65d4580e82ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THg7yW3wMAhAfnrcDYdqe7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 18039,
      "output_tokens": 62,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 62,
          "cache_read_input_tokens": 18039,
          "cache_creation_input_tokens": 1030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1030,
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

_source line 26 · 2026-05-10T19:37:35.295Z_

<details><summary>↩ Tool result · `toolu_01MJcZczQZGuBSKvLuzrB8d7`</summary>

```text
Web search results for query: "Google sparse attention reasoning inference 2025 2026"

Links: [{"title":"Google at NeurIPS 2025","url":"https://research.google/conferences-and-events/google-at-neurips-2025/"},{"title":"Sparse Attention","url":"https://www.aussieai.com/research/sparse-attention"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Long-Context Generalization with Sparse Attention | OpenReview","url":"https://openreview.net/forum?id=PsB6Lynznk"},{"title":"Best AI Models April 2026: Ranked by Benchmarks","url":"https://www.buildfastwithai.com/blogs/best-ai-models-april-2026"},{"title":"[2506.16640] Long-Context Generalization with Sparse Attention","url":"https://arxiv.org/abs/2506.16640"},{"title":"(PDF) SSA: Sparse Sparse Attention by Aligning Full and Sparse Attention Outputs in Feature Space","url":"https://www.researchgate.net/publication/397983867_SSA_Sparse_Sparse_Attention_by_Aligning_Full_and_Sparse_Attention_Outputs_in_Feature_Space"},{"title":"SpargeAttn: Accurate Sparse Attention Accelerating Any Model Inference","url":"https://arxiv.org/html/2502.18137v1"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://aclanthology.org/2025.acl-long.1126.pdf"},{"title":"GitHub - mit-han-lab/x-attention: [ICML 2025] XAttention: Block Sparse Attention with Antidiagonal Scoring · GitHub","url":"https://github.com/mit-han-lab/x-attention"}]

Based on the search results, here's what I found about Google's work on sparse attention for reasoning inference in 2025-2026:

## Google's Sparse Attention Research

Google presented research on "Spark Transformer: Reactivating Sparsity in Transformer FFN and Attention" at NeurIPS 2025, which appears to be one of their key contributions to sparse attention mechanisms.

Additionally, Google researchers presented "SPRINT: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models" at NeurIPS 2025, demonstrating their focus on optimizing reasoning models.

## Broader Context on Sparse Attention in 2025-2026

The field has seen significant progress in sparse attention mechanisms for inference optimization. There is increased focus on inference-time scaling in 2026, with developers focusing on lowering latency and making reasoning models expand fewer reasoning tokens where unnecessary.

In practical applications, GLM-5, released in 2026, was built on Mixture of Experts with DeepSeek Sparse Attention, showing how sparse attention has become integrated into state-of-the-art models.

Recent technical advances include XAttention, a block sparse attention framework that speeds up long-context inference by up to 13.5× without sacrificing accuracy by using a lightweight metric based on antidiagonal sums to efficiently select important attention blocks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "711eb8d5-d04f-4406-9063-65d4580e82ae",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "a5641bc8-7987-4341-aedc-0e84f6f213b8",
  "sourceToolAssistantUUID": "711eb8d5-d04f-4406-9063-65d4580e82ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T19:37:37.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016KqAAxPj1q5hXQK2bxBoxS`</summary>

```json
{
  "query": "ICML 2026 efficient inference LLM sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5641bc8-7987-4341-aedc-0e84f6f213b8",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTCafrWW3wP91Pk4jeL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af83bc24-0ddd-4244-baf6-bf0d20e0a9c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018F8yxJ31gweP7aghFS7L9H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 19069,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 893
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 19069,
          "cache_creation_input_tokens": 893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 893,
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

_source line 28 · 2026-05-10T19:37:45.731Z_

<details><summary>↩ Tool result · `toolu_016KqAAxPj1q5hXQK2bxBoxS`</summary>

```text
Web search results for query: "ICML 2026 efficient inference LLM sparsity"

Links: [{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"GitHub - mit-han-lab/Quest: [ICML 2024] Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference · GitHub","url":"https://github.com/mit-han-lab/Quest"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.04477"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"ICLR 2026: 12 papers on making AI systems reliable, efficient, and secure","url":"https://lambda.ai/blog/iclr-2026-12-papers"},{"title":"Awesome-LLM-Compression/README.md at main · HuangOwen/Awesome-LLM-Compression","url":"https://github.com/HuangOwen/Awesome-LLM-Compression/blob/main/README.md"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"Downloads 2025","url":"https://icml.cc/Downloads/2025"},{"title":"GitHub - chenhongyu2048/LLM-inference-optimization-paper: Summary of some awesome work for optimizing LLM inference · GitHub","url":"https://github.com/chenhongyu2048/LLM-inference-optimization-paper"}]

Based on the search results, I found relevant information about efficient inference and sparsity techniques for LLMs, though the specific focus on ICML 2026 papers is limited. Here's what the search revealed:

## ICML 2026 and LLM Efficiency Research

Several papers related to efficient LLM inference are being presented at ICLR 2026, including work on alignment-enhanced spectral sparsity in dynamic sparse training and unified quantization approaches.

## Recent Research on Efficient Inference with Sparsity

Recent work in this area includes:

1. **Dynamic Sparse Inference**: Sparsification methods are categorized into static and dynamic sparsity approaches, with dynamic sparsity adapting sparsity patterns at runtime based on input context.

2. **Query-Aware Sparsity**: Quest is an efficient long-context LLM inference framework that leverages query-aware sparsity in KV cache to reduce memory movement during attention and boost throughput, and was presented at ICML 2024.

3. **Combined Quantization and Sparsity**: Recent observations show that LLM internal activations are often dynamically sparse, but this interacts poorly with group-wise quantization; techniques have been proposed to reconcile dynamic sparse inference under low-bit quantization.

4. **Practical Performance Gains**: Recent approaches achieve up to 1.55× faster decoding throughput while maintaining accuracy comparable to dense quantized inference.

The search results show active research in sparsity-based techniques for LLM inference, with contributions spanning prediction-based methods, hardware-aware designs, and combined quantization-sparsity approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af83bc24-0ddd-4244-baf6-bf0d20e0a9c0",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "6c3239ac-3f30-47f9-a3f7-8d9b6a22908e",
  "sourceToolAssistantUUID": "af83bc24-0ddd-4244-baf6-bf0d20e0a9c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T19:37:48.257Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HVm1J5APFaht4D8zoisLpt`</summary>

```json
{
  "query": "site:openreview.net compound sparsity LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c3239ac-3f30-47f9-a3f7-8d9b6a22908e",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTDNKUktMLnN6aKRD9n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1881fac5-2b58-4528-a029-93e5f01ec38b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hyHJVGb1tY34SzQ2XY9pU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 19962,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 968
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 19962,
          "cache_creation_input_tokens": 968,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 968,
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

_source line 30 · 2026-05-10T19:37:56.513Z_

<details><summary>↩ Tool result · `toolu_01HVm1J5APFaht4D8zoisLpt`</summary>

```text
Web search results for query: "site:openreview.net compound sparsity LLM 2026"

Links: [{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference | OpenReview","url":"https://openreview.net/forum?id=AqpDRGnu82"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | OpenReview","url":"https://openreview.net/forum?id=4UfRP8MopP&noteId=jNHGkp1IWi"},{"title":"The Unseen Frontier: Pushing the Limits of LLM Sparsity with Surrogate-Free ADMM | OpenReview","url":"https://openreview.net/forum?id=ek6dQSumYx"},{"title":"Layer-wise Sensitivity-aware Sparsity Allocation for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=erGq3kjCmy"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=9VMW4iXfKt"},{"title":"Why RL Updates Look Sparse: An Implicit Compass Drives Optimization Bias | OpenReview","url":"https://openreview.net/forum?id=Q4mF4tLGbf"},{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity | OpenReview","url":"https://openreview.net/forum?id=SBUc5wirM8"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | OpenReview","url":"https://openreview.net/forum?id=wIPIhHd00i"},{"title":"Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective | OpenReview","url":"https://openreview.net/forum?id=otNB7BzsiR"},{"title":"S$^{2}$FT: Efficient, Scalable and Generalizable LLM Fine-tuning by Structured Sparsity | OpenReview","url":"https://openreview.net/forum?id=lEUle8S4xQ"}]

I found several relevant results from OpenReview related to sparsity in Large Language Models from 2025-2026. Here are the key findings:

## Research on Compound Sparsity and LLM Compression

One notable paper presents SLiM, a "one-shot" compression method that reduces a model's size without expensive retraining by combining uniform quantization, structured sparsity (pruning), and a low-rank adapter that mathematically corrects the compound errors from the first two steps. The result is an 8× smaller model that reduces the gap between its original accuracy and the compressed model's accuracy (up to 5.66% higher over state-of-the-art) and runs up to 4.3× faster.

## Other Sparsity Research (2026)

The Elsa method achieves extreme sparsity levels of up to 90% while retaining high model fidelity.

Activation sparsity denotes the existence of substantial weakly-contributed neurons within feed-forward networks of large language models (LLMs), providing wide potential benefits such as computation acceleration.

DejaVu is a system that uses a low-cost algorithm to predict contextual sparsity on the fly given inputs to each layer, along with an asynchronous and hardware-aware implementation that speeds up LLM inference.

The search results reveal active research into various forms of sparsity in LLMs, including compound approaches that combine multiple compression techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1881fac5-2b58-4528-a029-93e5f01ec38b",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "e0bb6bbd-391d-4696-ab06-72bbb45d8792",
  "sourceToolAssistantUUID": "1881fac5-2b58-4528-a029-93e5f01ec38b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T19:38:00.213Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YCfBAk1WomhqXTi6E37G2K`</summary>

```json
{
  "query": "SpargeAttn sparse attention accelerating model inference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0bb6bbd-391d-4696-ab06-72bbb45d8792",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTE9W5WpEb35zWVR19H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19ac9369-f88c-471b-9b35-18a8b9609da6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZDaACJQgKKy9spspUjvmS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 20930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1035,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T19:38:05.557Z_

<details><summary>↩ Tool result · `toolu_01YCfBAk1WomhqXTi6E37G2K`</summary>

```text
Web search results for query: "SpargeAttn sparse attention accelerating model inference 2025"

Links: [{"title":"GitHub - thu-ml/SpargeAttn: [ICML2025] SpargeAttention: A training-free sparse attention that accelerates any model inference. · GitHub","url":"https://github.com/thu-ml/SpargeAttn"},{"title":"[2502.18137] SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference","url":"https://arxiv.org/abs/2502.18137"},{"title":"SpargeAttn: Accurate Sparse Attention Accelerating Any Model Inference","url":"https://arxiv.org/html/2502.18137v1"},{"title":"Paper page - SpargeAttn: Accurate Sparse Attention Accelerating Any Model Inference","url":"https://huggingface.co/papers/2502.18137"},{"title":"SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference | OpenReview","url":"https://openreview.net/forum?id=74c3Wwk8Tc"},{"title":"SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250218137Z/abstract"},{"title":"SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference","url":"https://arxiv.org/html/2502.18137v4"},{"title":"ICLR SpargeAttn: Training-Free Sparse Attention Accelerating Any Model Inference","url":"https://iclr.cc/virtual/2025/33519"},{"title":"ICML Poster SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference","url":"https://icml.cc/virtual/2025/poster/46341"},{"title":"SpargeAttn: Training-Free Sparse Attention Accelerating Any Model Inference | OpenReview","url":"https://openreview.net/forum?id=UZggtUfsJV"}]

Based on the search results, here's what I found about SpargeAttn:

## Overview

SpargeAttention is a training-free sparse attention that accelerates any model inference. SpargeAttn and SageAttention2 were accepted by ICML 2025.

## How It Works

SpargeAttn uses a two-stage online filter: in the first stage, it rapidly and accurately predicts the attention map, enabling the skip of some matrix multiplications in attention. In the second stage, it designs an online softmax-aware filter that incurs no extra overhead and further skips some matrix multiplications.

## Performance

SpargeAttn is 2.5x to 5x faster than existing dense and sparse attention models. Additionally, SpargeAttention is a training-free sparse attention that can accelerate any model inference, achieving a 4-7x speedup.

## Applications and Results

The method significantly accelerates diverse models, including language, image, and video generation, without sacrificing end-to-end metrics. SpargeAttn is the first sparse attention method that can actually accelerate across language, image, and video models without compromising accuracy.

The code is available on GitHub at https://github.com/thu-ml/SpargeAttn.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ac9369-f88c-471b-9b35-18a8b9609da6",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "95305948-5b82-429c-b9ea-3560cffe0030",
  "sourceToolAssistantUUID": "19ac9369-f88c-471b-9b35-18a8b9609da6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T19:38:07.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014mEYbudPBLV1JYaKJLZNjb`</summary>

```json
{
  "query": "ForesightKV KV cache eviction reasoning models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95305948-5b82-429c-b9ea-3560cffe0030",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTEp6JGwoy5SVJ1oKu8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bbbedc9-1647-465e-983c-2796d1cb89fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6SgABpqCbF3JcaYGiXDN7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 21965,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 21965,
          "cache_creation_input_tokens": 916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 916,
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

_source line 34 · 2026-05-10T19:38:14.562Z_

<details><summary>↩ Tool result · `toolu_014mEYbudPBLV1JYaKJLZNjb`</summary>

```text
Web search results for query: "ForesightKV KV cache eviction reasoning models 2026"

Links: [{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution | OpenReview","url":"https://openreview.net/forum?id=k5h29Qv7GN"},{"title":"[2602.03203] ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/abs/2602.03203"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution","url":"https://arxiv.org/html/2602.03203"},{"title":"FORESIGHTKV: OPTIMIZING KV CACHE EVICTION","url":"https://openreview.net/pdf/6957849ec917fb6c85af208e505300924f9aa93b.pdf"},{"title":"Paper page - LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://huggingface.co/papers/2603.10899"},{"title":"PaFu-KV: Past & Future-Informed Cache Policy","url":"https://www.emergentmind.com/topics/past-and-future-informed-kv-cache-policy-pafu-kv"},{"title":"Neural Garbage Collection: Efficient LM Memory Management","url":"https://www.emergentmind.com/papers/2604.18002"},{"title":"KV Cache Learning","url":"https://www.emergentmind.com/topics/kv-cache-learning"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"}]

Based on the web search results, here's what I found about ForesightKV:

## Overview

ForesightKV is a training-based KV cache eviction framework that learns to predict which KV pairs to evict during long-text generations.

## Key Problem and Motivation

Large language models have shown remarkable reasoning abilities by producing long reasoning traces, but as the sequence length grows, the key-value (KV) cache expands linearly, incurring significant memory and computation costs.

## Technical Approach

The framework uses a multi-stage approach:

1. **Golden Eviction Algorithm**: ForesightKV first designs the Golden Eviction algorithm, which identifies the optimal eviction KV pairs at each step using future attention scores. These traces and the scores at each step are then distilled via supervised training with a Pairwise Ranking Loss.

2. **Reinforcement Learning**: The framework formulates cache eviction as a Markov Decision Process and applies the GRPO algorithm to mitigate the significant language modeling loss increase on low-entropy tokens.

## Performance Results

Experiments on AIME2024 and AIME2025 benchmarks with Qwen3-1.7B and Qwen3-4B demonstrate that ForesightKV consistently outperforms prior methods under only half the cache budget, while benefiting synergistically from both supervised and reinforcement learning approaches.

The research paper was submitted in February 2026 and is under review for ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bbbedc9-1647-465e-983c-2796d1cb89fe",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "7b79e253-cdb6-4177-a5a8-267542f18b0f",
  "sourceToolAssistantUUID": "6bbbedc9-1647-465e-983c-2796d1cb89fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T19:38:23.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AjuhXYM173gRrjCFW28ipb`</summary>

```json
{
  "query": "\"Engram\" \"conditional memory\" DeepSeek sparsity axis 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b79e253-cdb6-4177-a5a8-267542f18b0f",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTFUbZuoCeDTa6dgsDE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56994a19-682d-4bd9-978e-65f737a24d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhJxUvSumJPAu8mCH1dbUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 22881,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 961
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 22881,
          "cache_creation_input_tokens": 961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 961,
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

_source line 36 · 2026-05-10T19:38:31.856Z_

<details><summary>↩ Tool result · `toolu_01AjuhXYM173gRrjCFW28ipb`</summary>

```text
Web search results for query: ""Engram" "conditional memory" DeepSeek sparsity axis 2026"

Links: [{"title":"GitHub - deepseek-ai/Engram: Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models · GitHub","url":"https://github.com/deepseek-ai/Engram"},{"title":"Conditional Memory via Scalable Lookup: A New Axis of ...","url":"https://arxiv.org/pdf/2601.07372"},{"title":"DeepSeek's Engram Separates Memory from Reasoning in LLM Architecture Breakthrough | Introl Blog","url":"https://introl.com/blog/deepseek-engram-conditional-memory-architecture-january-2026"},{"title":"DeepSeek AI Researchers Introduce Engram: A Conditional Memory Axis For Sparse LLMs - MarkTechPost","url":"https://www.marktechpost.com/2026/01/14/deepseek-ai-researchers-introduce-engram-a-conditional-memory-axis-for-sparse-llms/"},{"title":"[2601.07372] Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models","url":"https://arxiv.org/abs/2601.07372"},{"title":"DeepSeek Engram: The Missing Memory Layer for Efficient LLMs | Medium","url":"https://medium.com/@graison/engram-explained-deepseeks-conditional-memory-adds-a-second-sparsity-axis-512cdfaaf93f"},{"title":"Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models","url":"https://arxiv.org/html/2601.07372v1"},{"title":"What is DeepSeek Engram ?. Conditional Memory via Scalable Lookup… | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/what-is-deepseek-engram-d9b48f4abe37"},{"title":"Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models","url":"https://arxiviq.substack.com/p/conditional-memory-via-scalable-lookup"},{"title":"DeepSeek Engram: V4 Architecture Revealed? Solving Transformer's Fatal Memory Flaw","url":"https://deepseek.ai/blog/deepseek-engram-v4-architecture"}]

Based on the search results, here's what I found about Engram, conditional memory, DeepSeek, and sparsity axis:

## Overview

DeepSeek published research on January 12, 2026 introducing Engram, a conditional memory module that achieves constant-time knowledge retrieval by decoupling static pattern storage from dynamic reasoning.

## Core Concept

While Mixture-of-Experts (MoE) scales capacity via conditional computation, Transformers lack a native primitive for knowledge lookup, forcing them to inefficiently simulate retrieval through computation. To address this, Engram introduces conditional memory as a complementary sparsity axis, instantiated via a module that modernizes classic N-gram embedding for O(1) lookup.

## Sparsity Allocation

By formulating the Sparsity Allocation problem, the research uncovers a U-shaped scaling law that optimizes the trade-off between neural computation (MoE) and static memory (Engram). The optimum appears when around 20 to 25 percent of the sparse budget is given to Engram.

## Performance Results

Scaled to 27B parameters, Engram achieves superior performance over a strictly iso-parameter and iso-FLOPs MoE baseline, with gains including MMLU +3.4, CMMLU +4.0, BBH +5.0, ARC-Challenge +3.7, HumanEval +3.0, and MATH +2.4. The 97% Needle-in-a-Haystack accuracy versus 84.2% baseline suggests Engram particularly benefits long-context applications where current models struggle.

## Open Source

The code and paper are fully open-sourced, available at the DeepSeek GitHub repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56994a19-682d-4bd9-978e-65f737a24d84",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "f1755082-b6ea-41a8-b333-235932a6e9d2",
  "sourceToolAssistantUUID": "56994a19-682d-4bd9-978e-65f737a24d84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-10T19:38:34.906Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013GrdVeE8nSdNcwevQNa8mq`</summary>

```json
{
  "query": "SVD contextual sparsity predictor LLM inference 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1755082-b6ea-41a8-b333-235932a6e9d2",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTGkWJZj9w5y4DUuxvD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3c84338-9ac1-43e0-b4a2-a2a5e59ef673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vq2NMR6yG6qaxT7jtx4ZC9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 23842,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 23842,
          "cache_creation_input_tokens": 1128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1128,
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

_source line 38 · 2026-05-10T19:38:42.283Z_

<details><summary>↩ Tool result · `toolu_013GrdVeE8nSdNcwevQNa8mq`</summary>

```text
Web search results for query: "SVD contextual sparsity predictor LLM inference 2026"

Links: [{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/html/2506.16500"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity - Z Lab","url":"https://z-lab.ai/projects/sparselora/"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://openreview.net/pdf?id=z83rodY0Pw"},{"title":"GitHub - z-lab/sparselora: [ICML 2025] SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://github.com/z-lab/sparselora"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time | OpenReview","url":"https://openreview.net/forum?id=wIPIhHd00i"},{"title":"Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/pdf/2506.16500"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=contextual+sparsity"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"}]

Based on the search results, here's what I found about SVD contextual sparsity predictors for LLM inference in 2026:

## Key Research Paper

The most relevant recent work is "SVD Contextual Sparsity Predictors for Fast LLM Inference", which was published on March 14, 2026 on arXiv.

## Core Approach

The framework provides a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices.

More specifically, the technique leverages low-rank SVD to predict sparse patterns for ReGLU-based LLMs, employing low-rank approximations of gate projection weight matrices in each layer as lightweight predictors of the FFN block sparsity mask during generation.

## Key Advantages

Unlike existing contextual sparsity prediction methods, this approach provides theoretical guarantees regarding prediction accuracy. Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math.

## Enhancement Technique

Introducing neuron-specific thresholds – implemented as bias terms – effectively mitigates accuracy degradation, and during the offline stage, sparsity predictors are constructed using low-rank SVD approximation with calibrated per-neuron thresholds.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3c84338-9ac1-43e0-b4a2-a2a5e59ef673",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "7d58d595-82a0-41d1-a2ad-7443e0341795",
  "sourceToolAssistantUUID": "d3c84338-9ac1-43e0-b4a2-a2a5e59ef673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-10T19:38:44.661Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WFMQbWBQZtzBBJcj2STn4H`</summary>

```json
{
  "query": "DynTS \"dynamic thinking token selection\" reasoning LLM sparsity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d58d595-82a0-41d1-a2ad-7443e0341795",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTHXCPi95Z6iPSQSqJz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "912f14f8-3f2c-4d33-92cc-22a81eaf8aaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyhTWTLhcXvsMWNJbFbUAy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 24970,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 953
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 24970,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 953,
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

_source line 40 · 2026-05-10T19:38:51.860Z_

<details><summary>↩ Tool result · `toolu_01WFMQbWBQZtzBBJcj2STn4H`</summary>

```text
Web search results for query: "DynTS "dynamic thinking token selection" reasoning LLM sparsity 2026"

Links: [{"title":"Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models","url":"https://arxiv.org/html/2601.18383v1"},{"title":"[2601.18383] Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models","url":"https://arxiv.org/abs/2601.18383"},{"title":"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=E1FrjgaG1J"},{"title":"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning","url":"https://arxiv.org/html/2506.02867v2"},{"title":"GitHub - iLearn-Lab/ACL26-EvoSparse: [ACL 2026 main] Official Implementation for Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention · GitHub","url":"https://github.com/iLearn-Lab/ACL26-EvoSparse"},{"title":"Dynamic Token Budgeting","url":"https://www.emergentmind.com/topics/dynamic-token-budgeting"},{"title":"[2505.16552] Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains","url":"https://arxiv.org/abs/2505.16552"},{"title":"[2510.01123] Rethinking Thinking Tokens: LLMs as Improvement Operators","url":"https://arxiv.org/abs/2510.01123"},{"title":"Dynamic Adaptive Reasoning: Optimizing LLM Inference-Time Thinking via Intent-Aware Scheduling[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202511.0291/download/final_file"},{"title":"[2602.13517] Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://arxiv.org/abs/2602.13517"}]

I found comprehensive information about DynTS and related research on reasoning token selection and sparsity in large reasoning models. Here are the key findings:

## DynTS: Dynamic Thinking Token Selection

DynTS (Dynamic Thinking Token Selection) is an approach designed to optimize efficiency in large reasoning models (LRMs). The method identifies decision-critical tokens and retains only their associated Key-Value (KV) cache states during inference, evicting the remaining redundant entries to optimize efficiency.

### Core Mechanism

DynTS introduces an Importance Predictor that dynamically estimates the importance score of each thinking token during inference time, and designs a decoding-time KV cache Selection Strategy that retains critical thinking tokens and evicts redundant ones.

### Performance Results

The method reduces the KV cache memory footprint by up to 3.32–5.73x without compromising reasoning performance compared to the full-cache transformer baseline. DynTS consistently outperforms all other KV cache eviction baselines.

### Underlying Principle

The approach presents the observed sparsity of thinking tokens and the Pareto Principle in LRMs, serving as the basis for DynTS.

### Related Research

The research also revealed broader findings on token sparsity in reasoning: MI peaks occur quite sparsely in the reasoning processes of LRMs, accounting for no more than 5% of all reasoning steps. This sparsity finding supports the efficiency gains that DynTS achieves.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "912f14f8-3f2c-4d33-92cc-22a81eaf8aaf",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "21ebd2b8-ab37-412a-a7b7-2b6c25c58a67",
  "sourceToolAssistantUUID": "912f14f8-3f2c-4d33-92cc-22a81eaf8aaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-10T19:38:53.845Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GNkmkzoQqKHHmxmB7oiA4r`</summary>

```json
{
  "query": "R-Sparse rank-aware activation sparsity efficient LLM inference 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21ebd2b8-ab37-412a-a7b7-2b6c25c58a67",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTJE43BsCJ6WgdTGsMP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67ce8164-4538-4209-a171-e17b37e00db9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq3qE6ZTkSCNw3a7x8M96X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 25923,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1087
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 25923,
          "cache_creation_input_tokens": 1087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1087,
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

_source line 42 · 2026-05-10T19:39:05.269Z_

<details><summary>↩ Tool result · `toolu_01GNkmkzoQqKHHmxmB7oiA4r`</summary>

```text
Web search results for query: "R-Sparse rank-aware activation sparsity efficient LLM inference 2026"

Links: [{"title":"[2504.19449] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/abs/2504.19449"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/html/2504.19449v1"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=9VMW4iXfKt"},{"title":"GitHub - VITA-Group/R-Sparse: [ICLR'25] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://github.com/VITA-Group/R-Sparse"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250419449Z/abstract"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference | alphaXiv","url":"https://www.alphaxiv.org/resources/2504.19449v1"},{"title":"Masked Gated Linear Unit","url":"https://arxiv.org/html/2506.23225v1"},{"title":"[Literature Review] R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://www.themoonlight.io/en/review/r-sparse-rank-aware-activation-sparsity-for-efficient-llm-inference"},{"title":"RANK-AWARE ACTIVATION SPARSITY FOR EFFICIENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf"},{"title":"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models","url":"https://arxiv.org/html/2508.02128v1"}]

Based on the search results, here's what I found about R-Sparse:

## R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference

R-Sparse is a training-free activation sparsity approach capable of achieving high sparsity levels in advanced LLMs.

### Problem it Addresses

Large Language Models present significant challenges during inference due to their substantial model size, especially when deployed on edge devices. Activation sparsity offers a promising solution to reduce computation and memory movement, enabling more efficient inference, particularly for small-batch on-device applications. However, current approaches face limitations with non-ReLU activation functions, which are foundational to most advanced LLMs, or require heavy continual training. Additionally, the difficulty in predicting active channels and limited achievable sparsity ratios constrain the effectiveness of activation sparsity-based methods.

### Key Technical Approach

The approach involves two key observations: (i) the non-sparse components of the input function can be regarded as a few bias terms, and (ii) the full computation can be effectively approximated by an appropriate combination of input channels and weight singular values. Building on this, R-Sparse replaces the linear layers in LLMs with a rank-aware sparse inference method that leverages the sparsity of input channels and singular value components, eliminating the need for active channel prediction.

### Performance Results

The approach achieves 50% model-level sparsity while maintaining performance comparable to the full model. Additionally, by utilizing a customized kernel, it demonstrates up to 43% end-to-end improvements in generation speed. Experiments were conducted on three representative LLM families: Llama-2, Llama-3, and Mistral, across ten tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67ce8164-4538-4209-a171-e17b37e00db9",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "1bae100c-dcf7-4b51-8917-2acea40a5290",
  "sourceToolAssistantUUID": "67ce8164-4538-4209-a171-e17b37e00db9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-10T19:39:07.363Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PFJ2SFMDBN98DYkghWCo9r`</summary>

```json
{
  "query": "\"Sparsing Law\" activation sparsity LLM scaling 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bae100c-dcf7-4b51-8917-2acea40a5290",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTKDRrnF7EmEZjyoAPK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15503af5-2dcd-4e0d-a9fd-0025187bd779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E8hGcGkv1aVsExM8JwMTpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 27010,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1086
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 27010,
          "cache_creation_input_tokens": 1086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1086,
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

_source line 44 · 2026-05-10T19:39:15.251Z_

<details><summary>↩ Tool result · `toolu_01PFJ2SFMDBN98DYkghWCo9r`</summary>

```text
Web search results for query: ""Sparsing Law" activation sparsity LLM scaling 2025 2026"

Links: [{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity | OpenReview","url":"https://openreview.net/forum?id=B9XP2R9LtG"},{"title":"ICML Poster Sparsing Law: Towards Large Language Models with Greater Activation Sparsity","url":"https://icml.cc/virtual/2025/poster/45239"},{"title":"[2411.02335] Sparsing Law: Towards Large Language Models with Greater Activation Sparsity","url":"https://arxiv.org/abs/2411.02335"},{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity","url":"https://arxiv.org/html/2411.02335v2"},{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity · HF Daily Paper Reviews by AI","url":"https://deep-diver.github.io/ai-paper-reviewer/paper-reviews/2411.02335/"},{"title":"(PDF) Sparsing Law: Towards Large Language Models with Greater Activation Sparsity","url":"https://www.researchgate.net/publication/385559773_Sparsing_Law_Towards_Large_Language_Models_with_Greater_Activation_Sparsity"},{"title":"Scaling Laws for Op- timal Sparsity for Mixture-of-Experts Lan","url":"https://openreview.net/pdf?id=6OT73DA0dF"},{"title":"Training-Free Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=dGVZwyq5tV"},{"title":"GitHub - thunlp/SparsingLaw: The open-source materials for paper \"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\". · GitHub","url":"https://github.com/thunlp/SparsingLaw"}]

I've found comprehensive information about the Sparsing Law research. Here are the key findings:

## Overview

"Sparsing Law" is a comprehensive study on the quantitative scaling properties and influential factors of activation sparsity within decoder-only Transformer-based LLMs.

## What is Activation Sparsity?

Activation sparsity denotes the existence of substantial weakly-contributed elements within activation outputs that can be eliminated, benefiting many important applications concerned with large language models (LLMs), such as computation acceleration and model interpretability.

## Key Findings

The research identifies several important scaling laws:

1. **Activation Functions**: ReLU-activated LLMs demonstrate a convergent decreasing logspace power-law, becoming increasingly sparse with more training data, while SiLU-activated models show a convergent increasing power-law, indicating reduced sparsity with increased training, suggesting ReLU is more efficient at leveraging training data for improved activation sparsity.

2. **Architecture Effects**: The activation ratio linearly increases with the width-depth ratio below a certain bottleneck point, indicating the potential advantage of a deeper architecture at a fixed parameter scale.

3. **Parameter Scale Independence**: At similar width-depth ratios, activation patterns within LLMs are insensitive to the parameter scale.

4. **Practical Results**: The researchers demonstrated the reliability of their findings by training a 2.4B model with a sparsity ratio of 93.52%, showing 4.1× speedup compared with its dense version.

The research was published in 2025 and has been presented at both ICML and ICLR 2025 conferences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15503af5-2dcd-4e0d-a9fd-0025187bd779",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "1159e810-054a-460f-ba9c-6cf6c30bce67",
  "sourceToolAssistantUUID": "15503af5-2dcd-4e0d-a9fd-0025187bd779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-10T19:39:17.877Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019WXziJYUzEmBrBVe4ohWDL`</summary>

```json
{
  "query": "XAttention block sparse attention antidiagonal scoring long context inference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1159e810-054a-460f-ba9c-6cf6c30bce67",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTKx4B1G9JSCJLfeKjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9f73528-39df-4183-ad19-7e91593499f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQLqrHjSJTpU5WEnCuwyRf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1049,
      "cache_read_input_tokens": 28096,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1049
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 28096,
          "cache_creation_input_tokens": 1049,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1049,
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

_source line 46 · 2026-05-10T19:39:27.196Z_

<details><summary>↩ Tool result · `toolu_019WXziJYUzEmBrBVe4ohWDL`</summary>

```text
Web search results for query: "XAttention block sparse attention antidiagonal scoring long context inference 2025"

Links: [{"title":"GitHub - mit-han-lab/x-attention: [ICML 2025] XAttention: Block Sparse Attention with Antidiagonal Scoring · GitHub","url":"https://github.com/mit-han-lab/x-attention"},{"title":"[2503.16428] XAttention: Block Sparse Attention with Antidiagonal Scoring","url":"https://arxiv.org/abs/2503.16428"},{"title":"XAttention: Block Sparse Attention with Antidiagonal Scoring | OpenReview","url":"https://openreview.net/forum?id=KG6aBfGi6e"},{"title":"XAttention: Block Sparse Attention with Antidiagonal Scoring","url":"https://par.nsf.gov/servlets/purl/10647402"},{"title":"ICML Poster XAttention: Block Sparse Attention with Antidiagonal Scoring","url":"https://icml.cc/virtual/2025/poster/45650"},{"title":"XAttention: Block Sparse Attention with Antidiagonal Scoring","url":"https://hanlab.mit.edu/projects/xattention"},{"title":"XAttention: Block Sparse Attention with Antidiagonal Scoring","url":"https://arxiv.org/html/2503.16428v1"},{"title":"(PDF) XAttention: Block Sparse Attention with Antidiagonal Scoring","url":"https://www.researchgate.net/publication/390038208_XAttention_Block_Sparse_Attention_with_Antidiagonal_Scoring"},{"title":"XAttention: Block Sparse Attention with Antidiagonal Scoring | alphaXiv","url":"https://www.alphaxiv.org/overview/2503.16428v1"},{"title":"Paper page - XAttention: Block Sparse Attention with Antidiagonal Scoring","url":"https://huggingface.co/papers/2503.16428"}]

Based on the search results, here's what I found about XAttention:

## Overview

XAttention is a plug-and-play framework that dramatically accelerates long-context inference in Transformers models using sparse attention. The paper was published at ICML 2025.

## Key Innovation

XAttention's key innovation is the insight that the sum of antidiagonal values (from the lower-left to upper-right) in the attention matrix provides a powerful proxy for block importance. Within each block of size B, elements are selected along the antidiagonal using a stride S to predict importance of the whole block.

## How It Works

XAttention optimizes attention through a three-step process: strided antidiagonal scoring where each block is scored by summing values along its strided antidiagonals, block selection based on these evaluations, and block sparse attention computed only on the selected blocks.

## Performance Results

XAttention demonstrates up to 13.5x acceleration in attention computation. Evaluations on demanding long-context benchmarks including RULER and LongBench for language, VideoMME for video understanding, and VBench for video generation show XAttention achieves accuracy comparable to full attention while delivering substantial computational gains.

## Code Availability

Code is available at https://github.com/mit-han-lab/x-attention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9f73528-39df-4183-ad19-7e91593499f0",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "4468735c-c69c-435f-8dba-35c981efb285",
  "sourceToolAssistantUUID": "b9f73528-39df-4183-ad19-7e91593499f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-10T19:39:29.389Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G4XYgmmxzzyjo4fscZUQS7`</summary>

```json
{
  "query": "\"Adaptive Parallel Reasoning\" Berkeley inference scaling 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4468735c-c69c-435f-8dba-35c981efb285",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTLq6FGP82zEzeZ185Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "031c35df-394b-4184-9239-7235237ff58f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqVdkKoEuy3tQKE2Krzp2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 29145,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 889
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 29145,
          "cache_creation_input_tokens": 889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 889,
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

_source line 48 · 2026-05-10T19:39:37.215Z_

<details><summary>↩ Tool result · `toolu_01G4XYgmmxzzyjo4fscZUQS7`</summary>

```text
Web search results for query: ""Adaptive Parallel Reasoning" Berkeley inference scaling 2026"

Links: [{"title":"Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/"},{"title":"Adaptive Parallel Reasoning: Scaling Inference with Dynamic Control • Dev|Journal","url":"https://earezki.com/ai-news/2026-05-08-adaptive-parallel-reasoning-the-next-paradigm-in-efficient-inference-scaling/"},{"title":"Learning Adaptive Parallel Reasoning with Language Models","url":"https://arxiv.org/html/2504.15466v1"},{"title":"Adaptive Parallel Reasoning: The Next Paradigm in Efficient Inference Scaling | daily.dev","url":"https://app.daily.dev/posts/adaptive-parallel-reasoning-the-next-paradigm-in-efficient-inference-scaling-nnuukhg5z"},{"title":"LLMs Can Now Reason in Parallel: UC Berkeley and UCSF Researchers Introduce Adaptive Parallel Reasoning to Scale Inference Efficiently Without Exceeding Context Windows - MarkTechPost","url":"https://www.marktechpost.com/2025/05/02/llms-can-now-reason-in-parallel-uc-berkeley-and-ucsf-researchers-introduce-adaptive-parallel-reasoning-to-scale-inference-efficiently-without-exceeding-context-windows/"},{"title":"[2512.07843] ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models","url":"https://arxiv.org/abs/2512.07843"},{"title":"[2504.15466] Learning Adaptive Parallel Reasoning with Language Models","url":"https://arxiv.org/abs/2504.15466"},{"title":"LLM can now reason in parallel: UC Berkeley and UCSF researchers introduce an adaptive parallel reasoning to scale the inference effectively without exceeding context windows","url":"https://learnopoly.com/llm-can-now-reason-in-parallel-uc-berkeley-and-ucsf-researchers-introduce-an-adaptive-parallel-reasoning-to-scale-the-inference-effectively-without-exceeding-context-windows/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=adaptive+parallel+reasoning"},{"title":"Learning Adaptive Parallel Reasoning with Language Models | OpenReview","url":"https://openreview.net/forum?id=YgwQ7sXPXU"}]

Based on the search results, here's what I found about Adaptive Parallel Reasoning and Berkeley's inference scaling work:

## Overview

Researchers at Berkeley AI Research have introduced Adaptive Parallel Reasoning to overcome the linear scaling limits of sequential inference. Recent progress in LLM reasoning capabilities has been largely driven by inference-time scaling, in addition to data and parameter scaling.

## The Core Problem and Solution

The problem is that sequential reasoning scales linearly with the amount of exploration. Adaptive Parallel Reasoning (APR) answers this question by making parallelization part of the model's generated control flow. Formally defined, adaptivity refers to the model's ability to dynamically allocate compute between parallel and serial operations at inference time. In other words, a model with adaptive parallel reasoning (APR) capability is taught to coordinate its control flow — when to generate sequences sequentially vs. in parallel.

## Key Technical Approach

APR generalizes existing reasoning methods by enabling adaptive multi-threaded inference using spawn() and join() operations. By distributing compute across parent and parallel child threads, APR minimizes the end-to-end latency, achieves better performance within the same context limit constraint, and scales better with an increasing inference-time compute budget.

## Performance Results

Experiments on the Countdown reasoning task demonstrate significant benefits of APR: (1) higher performance within the same context window (83.4% vs. 60.0% at 4k context); (2) superior scalability with increased computation (80.1% vs. 66.6% at 20k total tokens); (3) improved accuracy at equivalent latency (75.2% vs. 57.3% at approximately 5,000ms).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "031c35df-394b-4184-9239-7235237ff58f",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "67d217c7-bfb7-4fb1-8d5e-c19bbe0012ed",
  "sourceToolAssistantUUID": "031c35df-394b-4184-9239-7235237ff58f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-10T19:39:39.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01514iEj4g3RwXZo26Prwisi`</summary>

```json
{
  "query": "\"DeepSeek Sparse Attention\" V3.2 NSA native sparse 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67d217c7-bfb7-4fb1-8d5e-c19bbe0012ed",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTMZxwFh1yzeH6a2KdM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bd09ba7-cc35-4a86-9eb2-ac1354da0e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKeCRv6juW9nsXeQKaUZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 30034,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1105
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 30034,
          "cache_creation_input_tokens": 1105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1105,
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

_source line 50 · 2026-05-10T19:39:47.366Z_

<details><summary>↩ Tool result · `toolu_01514iEj4g3RwXZo26Prwisi`</summary>

```text
Web search results for query: ""DeepSeek Sparse Attention" V3.2 NSA native sparse 2025"

Links: [{"title":"[2502.11089] Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/abs/2502.11089"},{"title":"SGLang Day 0 Support for DeepSeek-V3.2 with Sparse Attention - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2025-09-29-deepseek-V32/"},{"title":"AI on AI: Sparse Attention, from NSA to DSA – Champaign Magazine","url":"https://champaignmagazine.com/2025/09/30/ai-on-ai-sparse-attention-from-nsa-to-dsa/"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively","url":"https://arxiv.org/pdf/2502.11089"},{"title":"DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models DeepSeek-AI","url":"https://arxiv.org/pdf/2512.02556"},{"title":"[2512.02556] DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models","url":"https://arxiv.org/abs/2512.02556"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1126/"},{"title":"Sparse Attention: Smart Architecture for Efficient Processing in Language Models","url":"https://deepfa.ir/en/blog/sparse-attention-efficient-text-processing-language-models"},{"title":"GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-V3.2-Exp"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/html/2502.11089v1"}]

Based on the web search results, here's what I found about DeepSeek Sparse Attention, V3.2, and NSA (Native Sparse Attention):

## Native Sparse Attention (NSA)

In February 2025, researchers introduced Native Sparse Attention (NSA) - a trainable-from-scratch sparse attention mechanism aligned with modern hardware. NSA employs a dynamic hierarchical sparse strategy, combining coarse-grained token compression with fine-grained token selection to preserve both global context awareness and local precision.

The NSA paper won a Best Paper award at ACL 2025, and experiments show the model pretrained with NSA maintains or exceeds Full Attention models across general benchmarks, long-context tasks, and instruction-based reasoning, while achieving substantial speedups over Full Attention on 64k-length sequences across decoding, forward propagation, and backward propagation.

## DeepSeek-V3.2 and DeepSeek Sparse Attention (DSA)

In late September 2025, DeepSeek company took a major step in this field by introducing DeepSeek-V3.2-Exp and the DeepSeek Sparse Attention (DSA) mechanism. At the heart of DeepSeek-V3.2 is DeepSeek Sparse Attention (DSA), a fine-grained sparse attention mechanism that redefines long-context efficiency.

The prototype of DSA primarily consists of two components: a lightning indexer and a fine-grained token selection mechanism. This design reduces the complexity of core attention from O(L²) to O(Lk), delivering dramatic improvements in both training and inference efficiency at up to 128K context length, with negligible loss of model quality.

The NSA paper is the direct foundation for the DeepSeek Sparse Attention (DSA) in the DeepSeek-V3.2 architecture.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bd09ba7-cc35-4a86-9eb2-ac1354da0e32",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "e37efd83-189b-469a-8c49-5f9a046bcd89",
  "sourceToolAssistantUUID": "0bd09ba7-cc35-4a86-9eb2-ac1354da0e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T19:39:51.673Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013NLKw2Xramp25RfYiuzoCU`</summary>

```json
{
  "query": "QASSO joint structured pruning quantization LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e37efd83-189b-469a-8c49-5f9a046bcd89",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTNMqiDrBJMUPfFhTqX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9f45824-8619-4478-9033-6b8911319e77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPYME1qdjxF1UYPoBB2Wyr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1078,
      "cache_read_input_tokens": 31139,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1078
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 31139,
          "cache_creation_input_tokens": 1078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1078,
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

_source line 52 · 2026-05-10T19:39:57.536Z_

<details><summary>↩ Tool result · `toolu_013NLKw2Xramp25RfYiuzoCU`</summary>

```text
Web search results for query: "QASSO joint structured pruning quantization LLM 2025"

Links: [{"title":"Automatic Joint Structured Pruning and Quantization for Efficient Neural","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Qu_Automatic_Joint_Structured_Pruning_and_Quantization_for_Efficient_Neural_Network_CVPR_2025_paper.pdf"},{"title":"Automatic Joint Structured Pruning and Quantization for Efficient Neural","url":"https://arxiv.org/pdf/2502.16638"},{"title":"Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression","url":"https://arxiv.org/html/2502.16638v1"},{"title":"GETA-3DGS: Automatic Joint Structured Pruning and Quantization for 3D Gaussian Splatting","url":"https://arxiv.org/html/2605.02086"},{"title":"Qu CVPR 2025: Automatic Joint Structured Pruning & Quantization for Efficient - Studocu","url":"https://www.studocu.com/row/document/regentropfen-college-of-applied-sciences/mobile-application-development/qu-cvpr-2025-automatic-joint-structured-pruning-quantization-for-efficient/150719074"},{"title":"[Literature Review] Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression","url":"https://www.themoonlight.io/en/review/automatic-joint-structured-pruning-and-quantization-for-efficient-neural-network-training-and-compression"},{"title":"[PDF] Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Joint-Structured-Pruning-and-Quantization-Qu-Aponte/28e6e3498da7e52a0ba984c0a53c74e948678346"},{"title":"CVPR Poster Automatic Joint Structured Pruning and Quantization for Efficient Neural Network Training and Compression","url":"https://cvpr.thecvf.com/virtual/2025/poster/34889"},{"title":"The Good, the Bad, and the Ugly: Cost-Efficient LLM Inference With Quantization, Pruning, and Distillation DLIT71489 | GTC 2025 | NVIDIA On-Demand","url":"https://www.nvidia.com/en-us/on-demand/session/gtc25-dlit71489/"},{"title":"Quantization, Distillation & Pruning of LLM","url":"https://www.linkedin.com/pulse/quantization-distillation-pruning-llm-tejas-bankar-k64vf"}]

Based on the search results, here's what I found about QASSO joint structured pruning quantization for LLMs in 2025:

## Overview

QASSO is a Quantization-Aware Structured Sparse Optimizer that provides reliable joint structured pruning and mixed precision quantization-aware training. QASSO is the first white-box joint optimizer that explicitly controls the sparsity ratio and bit width.

## Framework Context

QASSO is a key component of the **GETA** framework (Automatic Joint Structured Pruning and Quantization for Efficient Neural Networks). GETA automatically and efficiently performs joint structured pruning and quantization-aware training on any deep neural network.

## Key Features

QASSO employs a partial projected stochastic gradient (PPSG) method to progressively converge towards bit width budget for training stability. Moreover, a joint learning strategy is introduced to address the conflicts between pruning and quantization for performance preservation.

## Four-Stage Optimization Process

The framework uses a sequential four-stage optimization process: warm-up stage, projection stage, joint stage, and a cool-down stage.

## Applications

GETA has been tested on a wide range of neural networks including ResNet, VGG, BERT, Phi2, and ViT, achieving competitive (often superior) performance compared to state-of-the-art joint pruning and quantization methods.

This work was presented at CVPR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9f45824-8619-4478-9033-6b8911319e77",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "f76b882d-c598-4d82-b581-5170685b06b1",
  "sourceToolAssistantUUID": "d9f45824-8619-4478-9033-6b8911319e77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-10T19:40:00.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011KnSEjiFNJEhTrrMvxyCaj`</summary>

```json
{
  "query": "\"Think Silently\" latent compression reasoning chains LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f76b882d-c598-4d82-b581-5170685b06b1",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTP4qHvaATDyrd4yXcz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76c8b069-e025-41e4-a7a7-89248e7f4595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UW7mhXbQBkcLZaphB8H4ep",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 32217,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 32217,
          "cache_creation_input_tokens": 1133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1133,
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

_source line 54 · 2026-05-10T19:40:09.042Z_

<details><summary>↩ Tool result · `toolu_011KnSEjiFNJEhTrrMvxyCaj`</summary>

```text
Web search results for query: ""Think Silently" latent compression reasoning chains LLM 2025"

Links: [{"title":"[2505.16552] Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains","url":"https://arxiv.org/abs/2505.16552"},{"title":"Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains","url":"https://arxiv.org/pdf/2505.16552"},{"title":"[2505.16552v1] Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains","url":"https://arxiv.org/abs/2505.16552v1"},{"title":"GitHub - xiaomi-research/colar: [NeurIPS 2025] Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains · GitHub","url":"https://github.com/xiaomi-research/colar"},{"title":"NeurIPS Poster Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119459"},{"title":"Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains | OpenReview","url":"https://openreview.net/forum?id=AQsko3PPUe"},{"title":"Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250516552T/abstract"},{"title":"Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/think-silently-think-fast-dynamic-latent-compression"},{"title":"Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.16552v4"},{"title":"Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains","url":"https://neurips.cc/media/neurips-2025/Slides/119459.pdf"}]

Based on the search results, here's what I found about "Think Silently, Think Fast: Dynamic Latent Compression of LLM Reasoning Chains":

## Overview

Large Language Models achieve superior performance through Chain-of-Thought reasoning, but these token-level reasoning chains are computationally expensive and inefficient. The paper introduces Compressed Latent Reasoning (CoLaR), a novel framework that dynamically compresses reasoning processes in latent space through a two-stage training approach.

## Key Technical Approach

During supervised fine-tuning, CoLaR extends beyond next-token prediction by incorporating an auxiliary next compressed embedding prediction objective. This process merges embeddings of consecutive tokens using a compression factor randomly sampled from a predefined range, and trains a specialized latent head to predict distributions of subsequent compressed embeddings. Second, it enhances CoLaR through reinforcement learning that leverages the latent head's non-deterministic nature to explore diverse reasoning paths and exploit more compact ones.

## Key Results

CoLaR achieves 14.1% higher accuracy than latent-based baseline methods at comparable compression ratios, and reduces reasoning chain length by 53.3% with only 4.8% performance degradation compared to explicit CoT method. When applied to more challenging mathematical reasoning tasks, the RL-enhanced CoLaR demonstrates performance gains of up to 5.4% while dramatically reducing latent reasoning chain length by 82.8%.

## Publication Status

The paper was accepted to NeurIPS 2025. The work was published by researchers from Xiaomi Inc., with the first version released in May 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76c8b069-e025-41e4-a7a7-89248e7f4595",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "91215c52-0e6b-4627-9d75-6943cd36191d",
  "sourceToolAssistantUUID": "76c8b069-e025-41e4-a7a7-89248e7f4595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-10T19:40:12.008Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014KEwBaQTU8QY1PVQyqww8z`</summary>

```json
{
  "query": "\"SparseSpec\" sparse speculative decoding reasoning model PillarAttn 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91215c52-0e6b-4627-9d75-6943cd36191d",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTPv2z8zXjHyso4U6we",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc33270e-94ca-4155-ab6f-095a724efb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MfWyU6vayyx3TazprPHAk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 33350,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 33350,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1037,
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

_source line 56 · 2026-05-10T19:40:21.136Z_

<details><summary>↩ Tool result · `toolu_014KEwBaQTU8QY1PVQyqww8z`</summary>

```text
Web search results for query: ""SparseSpec" sparse speculative decoding reasoning model PillarAttn 2025 2026"

Links: [{"title":"[2512.01278] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://arxiv.org/abs/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with ...","url":"https://arxiv.org/pdf/2512.01278"},{"title":"1 Introduction","url":"https://arxiv.org/html/2512.01278"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.01278v1"},{"title":"[Literature Review] Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding","url":"https://www.themoonlight.io/en/review/accelerating-large-scale-reasoning-model-inference-with-sparse-self-speculative-decoding"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding – Own Your AI","url":"https://ownyourai.com/accelerating-large-scale-reasoning-model-inference-with-sparse-self-speculative-decoding/"},{"title":"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2512.01278"},{"title":"SparseSpec: Sparse Computation Innovations","url":"https://www.emergentmind.com/topics/sparsespec"},{"title":"TokenSelect: Efficient Long-Context Inference and Length Extrapolation for LLMs via Dynamic Token-Level KV Cache Selection | Request PDF","url":"https://www.researchgate.net/publication/397420153_TokenSelect_Efficient_Long-Context_Inference_and_Length_Extrapolation_for_LLMs_via_Dynamic_Token-Level_KV_Cache_Selection"},{"title":"Accelerating Large Language Model Reasoning via Speculative Search | OpenReview","url":"https://openreview.net/forum?id=oq0t5BXilT&noteId=riuU5QCsN7"}]

Based on the search results, here's comprehensive information about SparseSpec:

## Overview

SparseSpec is a speculative decoding framework that reuses the same model as both the draft and target models (i.e., self-speculation). The framework addresses the fact that lengthy generation in reasoning models shifts the inference bottleneck from compute-bound to memory-bound, as generating each token requires full attention to all previously generated tokens and memory access to an increasingly large KV-Cache, creating substantial pressure on memory bandwidth.

## PillarAttn Mechanism

SparseSpec features a novel sparse attention mechanism, PillarAttn, as the draft model, which accurately selects critical tokens via elegantly reusing information from the verification stage. PillarAttn selectively loads and computes only the critical tokens—those with the highest attention scores during inference—thereby significantly reducing memory bandwidth.

PillarAttn cleverly reuses attention scores computed during the verification phase to identify critical tokens for subsequent draft phases, eliminating the computational overhead typically associated with dynamic sparse attention.

## Key Features

SparseSpec is a lossless and training-free acceleration framework with a novel sparse attention PillarAttn, a unified batch scheduler, delayed verification, and a dynamic KV-Cache manager. The work was prototyped and evaluated across various reasoning models, including Qwen3-1.7B/8B/14B, using NVIDIA DGX-H100 servers with various tensor parallelism configurations.

## Performance Results

SparseSpec achieves up to 2.13× throughput improvement compared to the state-of-the-art serving framework vLLM. PillarAttn achieves an average acceptance token length of 6.16 out of 8 drafted tokens, significantly higher than baselines.

The paper was published in December 2025 (arxiv 2512.01278).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc33270e-94ca-4155-ab6f-095a724efb4d",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "d458f281-d03a-4920-9e42-188e19108303",
  "sourceToolAssistantUUID": "bc33270e-94ca-4155-ab6f-095a724efb4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-10T19:40:23.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B3CTX4d23Mb9d5NM8obxR6`</summary>

```json
{
  "query": "\"Compressed Sparse Attention\" DeepSeek V4 KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d458f281-d03a-4920-9e42-188e19108303",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTQonixMX9KPe8p3BjT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a09327e7-a367-4e85-9c27-5b28dd40cb57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Dci7uxAhad96t6vFWgFeA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1102,
      "cache_read_input_tokens": 34387,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1102
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 34387,
          "cache_creation_input_tokens": 1102,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1102,
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

_source line 58 · 2026-05-10T19:40:32.068Z_

<details><summary>↩ Tool result · `toolu_01B3CTX4d23Mb9d5NM8obxR6`</summary>

```text
Web search results for query: ""Compressed Sparse Attention" DeepSeek V4 KV cache 2026"

Links: [{"title":"DeepSeek AI Releases DeepSeek-V4: Compressed Sparse Attention and Heavily Compressed Attention Enable One-Million-Token Contexts - MarkTechPost","url":"https://www.marktechpost.com/2026/04/24/deepseek-ai-releases-deepseek-v4-compressed-sparse-attention-and-heavily-compressed-attention-enable-one-million-token-contexts/"},{"title":"DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2026-04-25-deepseek-v4/"},{"title":"Deepseek V4 explained, and why it matters to your wallet | LMCache Blog","url":"https://blog.lmcache.ai/en/2026/05/04/deepseek-v4-explained-and-why-it-matters-to-your-wallet/"},{"title":"DeepSeek V4 Pro Review 2026: Beats GPT-5.5 on Coding","url":"https://codersera.com/blog/deepseek-v4-pro-review-benchmarks-pricing-2026/"},{"title":"DeepSeek-V4 Review: Why Million-Token Context Needs Efficient Attention, Not Just Larger Windows | by Andrew Lukyanenko | Apr, 2026 | Medium","url":"https://artgor.medium.com/deepseek-v4-review-why-million-token-context-needs-efficient-attention-not-just-larger-windows-6dc8e74a00b1"},{"title":"DeepSeek V4 Guide: Engram Memory, Training Data Strategy & Release Status (2026)","url":"https://kili-technology.com/blog/data-story-deepseek-v4"},{"title":"DeepSeek V4 Review. DeepSeek released V4 as a public… | by Barnacle Goose | Apr, 2026 | Medium","url":"https://medium.com/@leucopsis/deepseek-v4-review-a23ce940151c"},{"title":"Inside DeepSeek V4: Hybrid Attention for Massive Contexts · Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/04/deepseek-v4-hybrid-attention-massive-contexts/"},{"title":"DeepSeek V4 (2026): Specs, Benchmarks, API Pricing, and Architecture Guide | Morph","url":"https://www.morphllm.com/deepseek-v4"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"}]

Based on the search results, here's what I found about Compressed Sparse Attention, DeepSeek V4, and KV cache optimization:

## Overview

DeepSeek-V4 features a hybrid mechanism combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA), where CSA compresses the Key-Value (KV) cache of every m tokens into one entry using a learned token-level compressor, then applies DeepSeek Sparse Attention where each query token attends only to the top-k selected compressed KV entries.

## Key Features of CSA

Compressed Sparse Attention first compresses the KV cache along the sequence dimension, then applies DeepSeek Sparse Attention over the compressed representation. It compresses groups of tokens into fewer KV entries and then selects a limited number of compressed blocks for each query.

CSA compresses KV caches along the sequence dimension at a 4x compression rate, then applies sparse attention, with a lightning indexer selecting the top 1,024 most relevant compressed KV entries for each query.

## Efficiency Gains

The efficiency improvements are substantial. In the 1M-token context setting, DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2.

The KV caches of DeepSeek V4 is ~10x smaller than DeepSeek V3.2.

## Heavily Compressed Attention (HCA)

Heavily Compressed Attention uses a much larger compression ratio, but removes sparse selection, with the compressed sequence becoming short enough that dense attention over compressed blocks is affordable.

DeepSeek-V4 was released in April 2026 and comes in two variants: V4-Pro (1.6T parameters, 49B active) and V4-Flash (284B parameters, 13B active), both supporting 1 million token context windows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a09327e7-a367-4e85-9c27-5b28dd40cb57",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "6a8038b8-66cb-4ddf-a928-1f488c5afbaf",
  "sourceToolAssistantUUID": "a09327e7-a367-4e85-9c27-5b28dd40cb57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-10T19:40:34.114Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AZK7CDZ6t2rKovrkyhYCDY`</summary>

```json
{
  "query": "ICLR 2026 efficient reasoning models inference optimization papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a8038b8-66cb-4ddf-a928-1f488c5afbaf",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTRcU7aR3fMMYEqAWpe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f519e97a-6f33-4b7e-9712-7f82be717ae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5qVoqjyNkvdzvYxYEgEbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 35489,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1285
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 35489,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1285,
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

_source line 60 · 2026-05-10T19:40:42.076Z_

<details><summary>↩ Tool result · `toolu_01AZK7CDZ6t2rKovrkyhYCDY`</summary>

```text
Web search results for query: "ICLR 2026 efficient reasoning models inference optimization papers"

Links: [{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"ICLR Poster ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference","url":"https://iclr.cc/virtual/2026/poster/10011824"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"},{"title":"ICLR 2026: 12 papers on making AI systems reliable, efficient, and secure","url":"https://lambda.ai/blog/iclr-2026-12-papers"},{"title":"ICLR 2026 Workshops","url":"https://iclr.cc/virtual/2026/events/workshop"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/c52228bf90679932f80d6962c056c6179c54af47.pdf"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"GitHub - Optimization-AI/DRPO: ICLR 2026: Efficient Reasoning via Decoupled Reward Policy Optimization · GitHub","url":"https://github.com/Optimization-AI/DRPO"}]

Based on the search results, here are key papers from ICLR 2026 related to efficient reasoning models and inference optimization:

## Quantization and Compression

**ParoQuant: Pairwise Rotation Quantization** addresses post-training quantization of LLMs by combining hardware-efficient Givens rotations with channel-wise scaling to handle outliers in weights and activations, which is especially important for reasoning LLMs where errors accumulate across long chains of thought.

## Efficient Reasoning and Test-Time Compute

**DECS framework** tackles the "overthinking" problem in large reasoning models where they generate excessively long reasoning paths without performance benefit, using a novel decoupled token-level reward mechanism that distinguishes and penalizes redundant tokens and includes curriculum batch scheduling.

**DRPO (Decoupled Reward Policy Optimization)** is a framework that decouples the length-based learning signal of correct rollouts from incorrect ones, integrating an optimized positive data distribution that maximizes length-based rewards under KL regularization into a discriminative objective.

Key research directions include hybrid reasoning mode selection approaches that dynamically choose between detailed reasoning and concise responses, and test-time compute scaling techniques that allocate computational resources dynamically during inference to optimize accuracy-efficiency trade-offs.

## Attention and Multimodal Efficiency

**VideoNSA** introduces a learnable, hardware-aware sparse attention mechanism that combines compression, selection, and sliding window branches for video tokens, using only 3.6% of attention budget at 128K tokens while improving accuracy on long-video understanding.

## Long-Context Processing

Recent work addresses efficient handling of long documents through novel agent workflows that process text in segments with memory management strategies, and extends algorithms to directly optimize memory ability in an end-to-end fashion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f519e97a-6f33-4b7e-9712-7f82be717ae1",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "4be525e4-0409-49d7-a914-a516f08f59bc",
  "sourceToolAssistantUUID": "f519e97a-6f33-4b7e-9712-7f82be717ae1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-10T19:40:44.398Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V9nd2yo65kHogX5fW9EZ9R`</summary>

```json
{
  "query": "UniComp unified evaluation LLM compression pruning quantization distillation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4be525e4-0409-49d7-a914-a516f08f59bc",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTSMFbxmkzHosh3yDPP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "681f1aea-604d-464c-bcb0-8dfd5fd5de0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxQGkca5DaBwKBU6P8Q6xk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 36774,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 36774,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1034,
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

_source line 62 · 2026-05-10T19:40:51.501Z_

<details><summary>↩ Tool result · `toolu_01V9nd2yo65kHogX5fW9EZ9R`</summary>

```text
Web search results for query: "UniComp unified evaluation LLM compression pruning quantization distillation 2025"

Links: [{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation","url":"https://arxiv.org/html/2602.09130"},{"title":"[2602.09130v2] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130v2"},{"title":"UNICOMP: A Unified Evaluation of Large Language Model Compression","url":"https://arxiv.org/pdf/2602.09130"},{"title":"(PDF) UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://www.researchgate.net/publication/400660606_UniComp_A_Unified_Evaluation_of_Large_Language_Model_Compression_via_Pruning_Quantization_and_Distillation"},{"title":"A Systematic Study of Compression Ordering for Large Language Models","url":"https://arxiv.org/html/2511.19495"},{"title":"Frontiers | A survey of model compression techniques: past, present, and future","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1518965/full"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"The Good, the Bad, and the Ugly: Cost-Efficient LLM Inference With Quantization, Pruning, and Distillation DLIT71489 | GTC 2025 | NVIDIA On-Demand","url":"https://www.nvidia.com/en-us/on-demand/session/gtc25-dlit71489/"},{"title":"Advancing Model Refinement: Muon-Optimized Distillation and Quantization for LLM Deployment","url":"https://arxiv.org/html/2601.09865v1"}]

I found comprehensive information about UniComp. Here are the key findings:

## UniComp Overview

UniComp is a unified evaluation framework for comparing pruning, quantization, and knowledge distillation that evaluates compressed models along three dimensions: performance, reliability, and efficiency, using a diverse set of capability- and safety-oriented benchmarks together with a hardware-aware efficiency analysis.

## Key Findings

Through extensive evaluation of six compression techniques on modern LLMs across more than 40 datasets, the research found that compression exhibits a consistent knowledge bias, where knowledge-intensive tasks are relatively preserved while reasoning, multilingual, and instruction-following capabilities degrade substantially.

Additionally, quantization provides the best overall trade-off between retained performance and efficiency, whereas distillation yields strong runtime acceleration gains at high computational cost, and task-specific calibration can significantly improve the reasoning ability of pruned models by up to 50%.

## Study Details

The research makes three main contributions: (1) introducing UniComp, a unified evaluation framework for systematically comparing pruning, quantization, and knowledge distillation across performance, reliability, and efficiency dimensions; (2) conducting extensive experiments on over 40 datasets covering knowledge, reasoning, multilinguality, instruction following, and a wide range of reliability and safety benchmarks, evaluated on modern LLMs including recent chain-of-thought (CoT) and mixture-of-experts (MoE) models and (3) analyzing the role of calibration data in compression and showing that reasoning-aware calibration can result in up to 50% relative improvement of reasoning performance in pruned models.

The paper was published on arXiv in February 2026 and is authored by Jonathan von Rad and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "681f1aea-604d-464c-bcb0-8dfd5fd5de0c",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "623c96a0-b1dc-4fd9-80d0-bc82fceb5b62",
  "sourceToolAssistantUUID": "681f1aea-604d-464c-bcb0-8dfd5fd5de0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-10T19:40:53.991Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015biUvb4NYJtJWCDwU9PaPp`</summary>

```json
{
  "query": "\"Optimal Sparsity\" mixture experts reasoning tasks MoE scaling 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "623c96a0-b1dc-4fd9-80d0-bc82fceb5b62",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTT3Z1gxuJHj23KabQ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd073b26-f7ee-44d7-a835-c7bc2108293d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uffo9jECDyUSEBF5GrnSSb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 37808,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1097
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 37808,
          "cache_creation_input_tokens": 1097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1097,
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

_source line 64 · 2026-05-10T19:41:01.238Z_

<details><summary>↩ Tool result · `toolu_015biUvb4NYJtJWCDwU9PaPp`</summary>

```text
Web search results for query: ""Optimal Sparsity" mixture experts reasoning tasks MoE scaling 2025 2026"

Links: [{"title":"Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks","url":"https://arxiv.org/html/2508.18672v1"},{"title":"[2508.18672] Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks","url":"https://arxiv.org/abs/2508.18672"},{"title":"Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks | OpenReview","url":"https://openreview.net/forum?id=XFw2EPRUUR"},{"title":"Mixture of Experts in Large Language Models †: Corresponding author: Junhao Song (junhao.song23@imperial.ac.uk)","url":"https://arxiv.org/html/2507.11181v2"},{"title":"Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/parameters-flops-scaling"},{"title":"Joint MoE Scaling Laws: Mixture of Experts Can Be Memory Efficient","url":"https://arxiv.org/pdf/2502.05172"},{"title":"Towards a Comprehensive Scaling Law of Mixture-of-Experts","url":"https://arxiv.org/html/2509.23678v1"},{"title":"Sparsity and Superposition in Mixture of Experts | OpenReview","url":"https://openreview.net/forum?id=azmp7x3lZv"},{"title":"The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expert Level","url":"https://arxiv.org/html/2604.02178v1"},{"title":"Understanding Mixture of Experts (MoE) Neural Networks 9/26/2025 • 50 min read","url":"https://intuitionlabs.ai/pdfs/understanding-mixture-of-experts-moe-neural-networks.pdf"}]

Based on the search results, here's what I found about "Optimal Sparsity" in mixture-of-experts (MoE) models for reasoning tasks:

## Key Research Finding

A primary study aims to identify how the optimal sparsity of MoE changes between memorization (TriviaQA, HellaSwag) and reasoning (GSM8K, GSM-Plus) tasks.

## Main Principles Discovered

The research reveals two key principles:

1. **Active FLOPs**: Models with identical training loss but greater active compute achieve higher reasoning accuracy.

2. **Total Tokens Per Parameter (TPP)**: Memorization tasks improve with more parameters, while reasoning tasks benefit from optimal TPP, indicating that reasoning is data-hungry.

## Important Finding on Sparsity vs. Reasoning

Increasing MoE sparsity improves memorization benchmarks, but saturates for reasoning performance. This suggests that the relationship between sparsity and performance differs significantly between these two capability types.

## Scaling Law Implications

Optimal MoE sparsity must be determined jointly by active FLOPs and TPP, revising the classical picture of compute-optimal scaling. Additionally, neither reinforcement learning post-training (GRPO) nor increased test-time compute alters these trends.

## Industry Application

Modern flagship models, e.g., Gemini 2.5 Pro, DeepSeek-V3, and Qwen3 now rely on MoE as a de-facto standard for economical scaling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd073b26-f7ee-44d7-a835-c7bc2108293d",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "9a8dccbf-b1a5-46e8-8129-bb41a994bee3",
  "sourceToolAssistantUUID": "fd073b26-f7ee-44d7-a835-c7bc2108293d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-10T19:41:03.178Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmGXNDJ9gtsFfFLoRfTd6E`</summary>

```json
{
  "query": "\"Adaptive Test-Time Compute\" reasoning LLM constrained policy optimization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a8dccbf-b1a5-46e8-8129-bb41a994bee3",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTTmCXxa1JxVSgB7xzq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e7f46ed-a654-4767-935b-2ec52fe0f304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XgEm8YDVSu7KBMwq9ffgYX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 38905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 971,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-10T19:41:10.566Z_

<details><summary>↩ Tool result · `toolu_01JmGXNDJ9gtsFfFLoRfTd6E`</summary>

```text
Web search results for query: ""Adaptive Test-Time Compute" reasoning LLM constrained policy optimization 2026"

Links: [{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853"},{"title":"[2604.14853] Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/abs/2604.14853"},{"title":"Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/html/2507.02076v1"},{"title":"[Literature Review] Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://www.themoonlight.io/en/review/reasoning-on-a-budget-a-survey-of-adaptive-and-controllable-test-time-compute-in-llms"},{"title":"[2507.02076] Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/abs/2507.02076"},{"title":"Test-Time Policy Adaptation for Enhanced Multi-Turn Interactions with LLMs","url":"https://arxiv.org/html/2509.23166v2"},{"title":"A Survey of Adaptive and Controllable Test-Time Compute ...","url":"https://arxiv.org/pdf/2507.02076"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning ...","url":"https://arxiv.org/pdf/2604.14853"},{"title":"[2507.02076v1] Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/abs/2507.02076v1"},{"title":"A survey of slow thinking-based reasoning LLMs using reinforcement learning and test-time scaling law - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325003358"}]

Based on the search results, I found relevant information about your query. Here's what I found:

## "Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization"

This work addresses test-time compute scaling through inference-time computation via repeated sampling, search, or extended reasoning, and formalizes the decision of which inputs deserve more compute as a constrained optimization problem (maximize expected accuracy subject to an average compute budget).

### Key Methodology

The paper solves this problem with a two-stage Solve-then-Learn pipeline, where Lagrangian relaxation decomposes the global constraint into per-instance sub-problems, each admitting a closed-form oracle action that optimally prices accuracy against cost.

In the learn stage, a lightweight classifier is trained to predict oracle actions from cheap input features, amortizing the allocation rule for real-time deployment.

### Experimental Results

Experiments on MATH and GSM8K with three LLMs (DeepSeek-V3, GPT-4o-mini, Qwen2.5-7B) show the method consistently outperforms uniform and heuristic allocation baselines, achieving up to 12.8% relative accuracy improvement on MATH under matched budget constraints, while closely tracking the Lagrangian oracle upper bound with over 91% imitation accuracy.

The paper was submitted to arXiv on April 16, 2026, and represents a principled approach to managing the accuracy-cost tradeoff in reasoning-intensive LLM inference systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e7f46ed-a654-4767-935b-2ec52fe0f304",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "bce6e826-d994-44e4-8aa5-0975e705558a",
  "sourceToolAssistantUUID": "8e7f46ed-a654-4767-935b-2ec52fe0f304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-10T19:41:15.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0197Q4ULyn9fwJWVoK5pkM9T`</summary>

```json
{
  "query": "\"Neural Garbage Collection\" LLM memory KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bce6e826-d994-44e4-8aa5-0975e705558a",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTUT69L3itnL8ikyN7X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae734e16-af7f-4818-96c5-4dd223581d7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fe28EZhEwa63kZvCHQHekL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 39876,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 39876,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 976,
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

_source line 68 · 2026-05-10T19:41:23.959Z_

<details><summary>↩ Tool result · `toolu_0197Q4ULyn9fwJWVoK5pkM9T`</summary>

```text
Web search results for query: ""Neural Garbage Collection" LLM memory KV cache 2026"

Links: [{"title":"Neural Garbage Collection: Efficient LM Memory Management","url":"https://www.emergentmind.com/papers/2604.18002"},{"title":"[2604.18002] Neural Garbage Collection: Learning to Forget while Learning to Reason","url":"https://arxiv.org/abs/2604.18002"},{"title":"KV Cache Optimization for LLMs 2026: Engineering Guide","url":"https://www.digitalapplied.com/blog/kv-cache-optimization-techniques-2026-engineering-guide"},{"title":"[Paper Note] Neural Garbage Collection: Learning to Forget while Learning to Reason, Michael Y. Li+, arXiv'26, 2026.04 · Issue #5306 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/5306"},{"title":"KV Cache Locality: The Hidden Variable in Your LLM Serving Cost | Ranvier","url":"https://ranvier.systems/2026/04/30/kv-cache-locality-the-hidden-variable-in-your-llm-serving-cost.html"},{"title":"Neural Garbage Collection: Learning to Forget while Learning to Reason","url":"https://arxiv.org/html/2604.18002v1"},{"title":"[Literature Review] Neural Garbage Collection: Learning to Forget while Learning to Reason","url":"https://www.themoonlight.io/en/review/neural-garbage-collection-learning-to-forget-while-learning-to-reason"},{"title":"How KV Cache Works Internally: From LLMs to Distributed Systems · Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/03/kv-cache-llm-inference-distributed-storage/"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"KV Cache Optimization: Serve 10x More Users on the Same GPU (2026) | Spheron Blog","url":"https://www.spheron.network/blog/kv-cache-optimization-guide/"}]

Based on the search results, here's what I found about Neural Garbage Collection:

## Overview

Neural Garbage Collection (NGC) is a framework where a language model learns to forget while learning to reason, trained end-to-end from outcome-based task reward alone. Chain-of-thought reasoning has driven striking advances in LLM capability, yet every reasoning step grows the KV cache, creating a bottleneck to scaling this paradigm further.

## How It Works

As the model reasons, it periodically pauses, decides which KV cache entries to evict, and continues to reason conditioned on the remaining cache. By treating tokens in a chain-of-thought and cache-eviction decisions as discrete actions sampled from the language model, reinforcement learning can jointly optimize how the model reasons and how it manages its own memory.

## Key Innovation

The model learns this behavior entirely from a single learning signal - the outcome-based task reward - without supervised fine-tuning or proxy objectives. This contrasts with traditional approaches that rely on hand-designed eviction criteria.

## Performance Results

On Countdown, AMC, and AIME tasks, NGC maintains strong accuracy relative to the full-cache upper bound at 2-3x peak KV cache size compression and substantially outperforms eviction baselines. Empirical results show that Neural Garbage Collection outperforms baseline eviction methods, achieving 49.6% accuracy on arithmetic reasoning and robust performance under aggressive cache reductions.

## Practical Applications

NGC enables cost- and memory-efficient chain-of-thought serving for LLM APIs, reducing per-request VRAM and increasing throughput (2–3x peak KV reduction) for reasoning-heavy endpoints.

The research paper was submitted to arXiv in April 2026 and represents a significant advance in managing memory constraints for reasoning-heavy language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae734e16-af7f-4818-96c5-4dd223581d7a",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "f906dc9d-81b5-4471-95f3-f45449380a3e",
  "sourceToolAssistantUUID": "ae734e16-af7f-4818-96c5-4dd223581d7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-10T19:41:27.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WiNucbcaD6gEW1dDbrB1ER`</summary>

```json
{
  "query": "\"LookaheadKV\" KV cache eviction future generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f906dc9d-81b5-4471-95f3-f45449380a3e",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTVSTifpfMMVPswKN1g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f30c9272-e4ec-432e-a447-309af63482cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017hhEyzd7qevv4sqs4b9khV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 40852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1063,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-10T19:41:33.670Z_

<details><summary>↩ Tool result · `toolu_01WiNucbcaD6gEW1dDbrB1ER`</summary>

```text
Web search results for query: ""LookaheadKV" KV cache eviction future generation 2026"

Links: [{"title":"GitHub - SamsungLabs/LookaheadKV: [ICLR 2026] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation · GitHub","url":"https://github.com/SamsungLabs/LookaheadKV"},{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"},{"title":"[2603.10899v1] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899v1"},{"title":"ICLR Poster LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://iclr.cc/virtual/2026/poster/10009483"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation | OpenReview","url":"https://openreview.net/forum?id=RVLMGPXt2i"},{"title":"Paper page - LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://huggingface.co/papers/2603.10899"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899v1"},{"title":"[Blog] LookaheadKV: Fast and Accurate KV Cache Eviction ...","url":"https://research.samsung.com/blog/LookaheadKV-Fast-and-Accurate-KV-Cache-Eviction-by-Glimpsing-into-the-Future-without-Generation"},{"title":"[2505.20334] Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query","url":"https://arxiv.org/abs/2505.20334"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by ...","url":"https://arxiv.org/pdf/2603.10899"}]

Based on the web search results, here's information about LookaheadKV:

## Overview

LookaheadKV is a paper presented at ICLR 2026 titled "Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation". The method performs efficient KV cache eviction by predicting the attention pattern of the model's future response with parameter-efficient modules—lookahead tokens and lookahead LoRA.

## Problem and Solution

Transformer-based large language models rely on key-value (KV) caching to avoid redundant computation during autoregressive inference, but the cache size grows linearly with the input sequence length, quickly becoming a bottleneck for long-context tasks.

Previous work proposed to improve eviction quality by "glimpsing into the future" with draft generators producing a surrogate future response, but these approaches rely on computationally expensive draft generation, which introduces substantial prefilling overhead.

LookaheadKV augments transformer layers with parameter-efficient modules trained to predict true importance scores with high accuracy, ensuring negligible runtime overhead comparable to existing inexpensive heuristics, while achieving accuracy superior to more costly approximation methods.

## Performance

LookaheadKV reduces the eviction cost by up to 14.5x, leading to significantly faster time-to-first-token.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f30c9272-e4ec-432e-a447-309af63482cb",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "11d40b2d-613f-40d3-bf1c-96c078e4ad17",
  "sourceToolAssistantUUID": "f30c9272-e4ec-432e-a447-309af63482cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-10T19:41:35.727Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0184oRbPBz1mLgKy8fRRa8ta`</summary>

```json
{
  "query": "\"VideoNSA\" video sparse attention ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d40b2d-613f-40d3-bf1c-96c078e4ad17",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTW9qckzouVaJ8fhE4D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b549778d-3d27-491d-9e82-0330857e424d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDSLDtytYgnCjr4LXENd7r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1030,
      "cache_read_input_tokens": 41915,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 41915,
          "cache_creation_input_tokens": 1030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1030,
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

_source line 72 · 2026-05-10T19:41:45.285Z_

<details><summary>↩ Tool result · `toolu_0184oRbPBz1mLgKy8fRRa8ta`</summary>

```text
Web search results for query: ""VideoNSA" video sparse attention ICLR 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 VIDEONSA:","url":"https://openreview.net/pdf/05943dbd6b808ccbffb5488718a1c9f50bcc7069.pdf"},{"title":"VideoNSA: Native Sparse Attention Scales Video Understanding | OpenReview","url":"https://openreview.net/forum?id=zA2LbsUMDd"},{"title":"[2510.02295] VideoNSA: Native Sparse Attention Scales Video Understanding","url":"https://arxiv.org/abs/2510.02295"},{"title":"ICLR 2026: 12 papers on making AI systems reliable, efficient, and secure","url":"https://lambda.ai/blog/iclr-2026-12-papers"},{"title":"VIDEONSA: NATIVE SPARSE ATTENTION SCALES VIDEO ...","url":"https://openreview.net/pdf/fe913da7396c0934269a078bd5a85e87b4932f50.pdf"},{"title":"VideoNSA: Native Sparse Attention Scales Video Understanding","url":"https://arxiv.org/html/2510.02295v1"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=35825&show=25"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3100&show=250"},{"title":"VideoNSA: Native Sparse Attention Scales Video Understanding","url":"https://enxinsong.com/VideoNSA-web/"},{"title":"GitHub - Espere-1119-Song/VideoNSA: VideoNSA: Native Sparse Attention Scales Video Understanding","url":"https://github.com/Espere-1119-Song/VideoNSA"}]

I've found comprehensive information about VideoNSA. Here's a summary of the research:

## VideoNSA: Native Sparse Attention Scales Video Understanding

VideoNSA is a paper published at ICLR 2026 by researchers from UC San Diego, Princeton University, New York University, and Lambda Inc.

### Core Problem and Solution
Video understanding in multimodal language models remains limited by context length: models often miss key transition frames and struggle to maintain coherence across long time scales. To address this, the researchers adapted Native Sparse Attention (NSA) to video-language models, with VideoNSA adapting Qwen2.5-VL through end-to-end training on a 216K video instruction dataset.

### Technical Approach
The method employs a hardware-aware hybrid approach to attention, preserving dense attention for text, while employing NSA for video. VideoNSA utilizes three sparse attention branches: a compression branch that reduces redundancy via token averaging, a selection branch that identifies top-k important tokens, and a sliding window branch that enforces local temporal coverage, with outputs combined through dynamic gating before integration with text tokens for LLM decoding.

### Performance
Compared to token-compression and training-free sparse baselines, VideoNSA achieves improved performance on long-video understanding, temporal reasoning, and spatial benchmarks. At 128K tokens, VideoNSA uses 3.6% of the attention budget and still improves accuracy over both dense and token-compression baselines on long-video understanding, temporal reasoning, and spatial benchmarks.

### Key Findings
Further ablation analysis reveals four key findings: (1) reliable scaling to 128K tokens; (2) an optimal global–local attention allocation at a fixed budget; (3) task-dependent branch usage patterns; and (4) the learnable combined sparse attention help induce dynamic attention sinks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b549778d-3d27-491d-9e82-0330857e424d",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "4dea52de-8888-4c16-b286-0cd9f6f01514",
  "sourceToolAssistantUUID": "b549778d-3d27-491d-9e82-0330857e424d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-10T19:41:47.204Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RcTT71pFypjTAsPzWFw2ZB`</summary>

```json
{
  "query": "\"ParoQuant\" pairwise rotation quantization reasoning LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dea52de-8888-4c16-b286-0cd9f6f01514",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTX1WbCgcCftiPy1qeU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dbc8c7e-3c81-4e70-9b48-c68dddc23df7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JcuvMxkBzr9wv4LbJz5eJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 42945,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1007
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 42945,
          "cache_creation_input_tokens": 1007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1007,
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

_source line 74 · 2026-05-10T19:41:53.941Z_

<details><summary>↩ Tool result · `toolu_01RcTT71pFypjTAsPzWFw2ZB`</summary>

```text
Web search results for query: ""ParoQuant" pairwise rotation quantization reasoning LLM 2026"

Links: [{"title":"GitHub - z-lab/paroquant: [ICLR 2026] ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference · GitHub","url":"https://github.com/z-lab/paroquant"},{"title":"[2511.10645] ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference","url":"https://arxiv.org/abs/2511.10645"},{"title":"ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference","url":"https://arxiv.org/html/2511.10645v2"},{"title":"ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference | OpenReview","url":"https://openreview.net/forum?id=1USeVjsKau"},{"title":"ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference - Z Lab","url":"https://z-lab.ai/projects/paroquant/"},{"title":"[Paper Note] ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference, Yesheng Liang+, arXiv'25, 2025.11 · Issue #4728 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4728"},{"title":"paroquant: pairwise rotation quantization","url":"https://arxiv.org/pdf/2511.10645"},{"title":"ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference | alphaXiv","url":"https://www.alphaxiv.org/abs/2511.10645v1"},{"title":"ICLR Poster ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference","url":"https://iclr.cc/virtual/2026/poster/10011824"},{"title":"[Literature Review] ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference","url":"https://www.themoonlight.io/en/review/paroquant-pairwise-rotation-quantization-for-efficient-reasoning-llm-inference"}]

Here are the search results for **ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference**:

## Overview

ParoQuant is a post-training quantization (PTQ) method that combines hardware-efficient and optimizable independent Givens rotations with channel-wise scaling to even out the magnitudes across channels and narrow the dynamic range within each quantization group, effectively addressing the outlier issue.

## Key Features and Performance

ParoQuant uses learned pairwise rotations to suppress weight outliers, closing the accuracy gap with FP16 while running at near-AWQ speed. It supports NVIDIA GPUs (vLLM, Transformers) and Apple Silicon (MLX).

## Why It Matters for Reasoning LLMs

The presence of outliers in weights and activations often leads to large quantization errors and severe accuracy degradation, especially in recent reasoning LLMs where errors accumulate across long chains of thought. ParoQuant is a PTQ method that combines high accuracy with minimal computational overhead, making it well-suited to reasoning LLMs.

## Results

Under weight-only quantization, ParoQuant achieves an average 2.4% accuracy improvement over AWQ on reasoning tasks, with less than 10% overhead. ParoQuant also matches the accuracy of state-of-the-art weight-activation quantization methods.

## Publication

ParoQuant was presented at the International Conference on Learning Representations (ICLR) 2026 by authors Yesheng Liang, Haisheng Chen, Zihan Zhang, Song Han, and Zhijian Liu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dbc8c7e-3c81-4e70-9b48-c68dddc23df7",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "4ce65f5e-8a6a-4e48-bdd2-429daada5d86",
  "sourceToolAssistantUUID": "9dbc8c7e-3c81-4e70-9b48-c68dddc23df7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-10T19:41:56.432Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012AtS8Ey9cCbxpKXJkQQheC`</summary>

```json
{
  "query": "\"TwELL\" Sakana NVIDIA hybrid sparsity format LLM GPU 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ce65f5e-8a6a-4e48-bdd2-429daada5d86",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTXeZYLMi4BT1ejnS9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eab1919d-9b04-4f13-a695-0719c1650e10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sch8enC9LCSS9uydKu3M6r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 43952,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1084
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 43952,
          "cache_creation_input_tokens": 1084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1084,
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

_source line 76 · 2026-05-10T19:42:04.274Z_

<details><summary>↩ Tool result · `toolu_012AtS8Ey9cCbxpKXJkQQheC`</summary>

```text
Web search results for query: ""TwELL" Sakana NVIDIA hybrid sparsity format LLM GPU 2026"

Links: [{"title":"Faster LLMs by Reshaping Sparsity | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/technology/2026/faster-llms-by-reshaping-sparsity"},{"title":"GitHub - SakanaAI/sparser-faster-llms: Cuda kernels for leveraging LLM sparsity to improve throughput and decrease the memory requirements during inference and training. · GitHub","url":"https://github.com/SakanaAI/sparser-faster-llms"},{"title":"Sparser, Faster, Lighter Transformer Language Models","url":"https://arxiv.org/html/2603.23198"},{"title":"Sakana AI on X: \"How do we make LLMs faster and lighter? Don’t force the GPU to adapt to sparsity. Reshape the sparsity to fit the GPU! ⚡️ Excited to share our new #ICML2026 paper in collaboration with @NVIDIA: \"Sparser, Faster, Lighter Transformer Language Models\". This work introduces new https://t.co/ehByWHIh6I\" / X","url":"https://x.com/SakanaAILabs/status/2052787226136990029"},{"title":"GitHub - NVIDIA/TensorRT-LLM: TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in a performant way. · GitHub","url":"https://github.com/NVIDIA/TensorRT-LLM"},{"title":"Best NVIDIA GPUs for LLMs in 2026: Ranked by Use Case | Spheron Blog","url":"https://www.spheron.network/blog/best-nvidia-gpus-for-llms/"},{"title":"Best GPUs for AI (2026): NVIDIA RTX Turing to Blackwell Quantization Support, Budget Options Under $1000","url":"https://www.bestgpusforai.com/blog/best-gpus-for-ai"},{"title":"Best GPU for local LLM Inference and Training – 2026 [Updated] | BIZON","url":"https://bizon-tech.com/blog/best-gpu-llm-training-inference"},{"title":"Nvidia - GTC 2026 – The Inference Kingdom Expands","url":"https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands"},{"title":"GitHub - NVIDIA/Model-Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. · GitHub","url":"https://github.com/NVIDIA/Model-Optimizer"}]

Based on the search results, here's what I found about TwELL, Sakana AI, and NVIDIA's hybrid sparsity format for LLMs:

## Overview

Sakana AI and NVIDIA unveiled a new method that reshapes sparsity in LLMs to boost GPU efficiency, achieving over 20% speedups. This research was presented as a #ICML2026 paper in collaboration with NVIDIA: "Sparser, Faster, Lighter Transformer Language Models".

## TwELL Format

TwELL is a sparse packing format designed for optimized tiled matrix multiplication kernels, along with custom CUDA kernels that fuse multiple sparse operations. More specifically, TwELL (Tile-wise ELLPACK) is a new packing format for sparse data that can be naturally materialized in the epilogue of highly-optimized matrix multiplication kernels, removing a canonical bottleneck of prior packing schemes.

## Hybrid Format for Training

Starting from TwELL, inference kernels fuse multiple matrix-multiplications into a single optimized pipeline that minimizes computation, while training kernels further reduce the sparse representation to a hybrid format that trivializes storage costs of intermediate activations.

## Performance Results

Benchmarks at billion-parameter scale demonstrated over 20% speed improvements and significant reductions in peak memory and energy consumption. Custom CUDA kernels were designed for H100 GPUs for sparse models, leveraging the TwELL packing format.

The code and kernels have been released open-source on GitHub as reference code for the paper Sparser, Faster, Lighter Transformer Language Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eab1919d-9b04-4f13-a695-0719c1650e10",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "f0716531-ac42-4b23-aa13-2a16fb076b88",
  "sourceToolAssistantUUID": "eab1919d-9b04-4f13-a695-0719c1650e10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-10T19:42:07.190Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017CJYB6C2EgJteBUS5qWnAr`</summary>

```json
{
  "query": "\"Amber Pruner\" N:M activation sparsity prefill LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0716531-ac42-4b23-aa13-2a16fb076b88",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTYQgPj9XSMcDUghKng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c99cbbe0-aa34-444f-ae6b-834a294cb1ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgnFvKXibopHacrkC1nYEW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 45036,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 45036,
          "cache_creation_input_tokens": 1228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1228,
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

_source line 78 · 2026-05-10T19:42:13.192Z_

<details><summary>↩ Tool result · `toolu_017CJYB6C2EgJteBUS5qWnAr`</summary>

```text
Web search results for query: ""Amber Pruner" N:M activation sparsity prefill LLM 2025"

Links: [{"title":"Amber Pruner: Leveraging N:M Activation Sparsity for ...","url":"https://arxiv.org/pdf/2508.02128"},{"title":"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models","url":"https://arxiv.org/html/2508.02128v1"},{"title":"[2508.02128] Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models","url":"https://arxiv.org/abs/2508.02128"},{"title":"Computer Science Aug 2025","url":"https://www.arxiv.org/list/cs/2025-08?skip=1125&show=250"},{"title":"Targeted Pruning for Prefill-Decode Disaggregation","url":"https://www.emergentmind.com/topics/targeted-pruning-for-prefill-decode-disaggregation"},{"title":"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models","url":"https://powerdrill.ai/discover/summary-amber-pruner-leveraging-nm-activation-sparsity-for-cmdz0zewcfysu07nq2sr8uh7n"},{"title":"gies for post-training n:m activation sparsity in llms","url":"https://www.arxiv.org/pdf/2509.22166"},{"title":"[PDF] SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SparseGPT:-Massive-Language-Models-Can-Be-Pruned-in-Frantar-Alistarh/909ad57ce8caa6b390a65ae09db352d27d8f3996"},{"title":"Týr-the-Pruner: Unlocking Accurate 50% Structural Pruning ...","url":"https://arxiv.org/pdf/2503.09657"},{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"}]

Based on the search results, here's what I found about Amber Pruner:

## Overview

Amber Pruner is a training-free N:M activation sparsity method designed specifically for the prefill stage, targeting the acceleration of linear projection layers in LLMs.

## Key Features

The method can effectively sparsify and accelerate more than 55% of linear computations without requiring model retraining across multiple sparsity ratios (2:4, 4:8, and 8:16).

Pruning is applied to the linear projection submodules in the prefill stage, including q_proj, k_proj, v_proj, and o_proj.

## Enhanced Framework

To further enhance generality and efficiency, the authors propose Outstanding-sparse, a unified framework that integrates Amber Pruner with post-training W8A8 quantization.

## Performance and Impact

The approach preserves strong performance across a range of downstream tasks, with notable advantages in generative tasks.

## Research Context

The paper was published on arXiv in August 2025. Amber-Pruner currently is the only paper that explores post-training dynamic activation sparsity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c99cbbe0-aa34-444f-ae6b-834a294cb1ff",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "0e58b325-d55e-427e-9a3f-405f3ebd10c3",
  "sourceToolAssistantUUID": "c99cbbe0-aa34-444f-ae6b-834a294cb1ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-10T19:42:15.066Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TGRrHvfAu3TnT4aW5yCav8`</summary>

```json
{
  "query": "\"Hold Onto That Thought\" KV cache compression reasoning NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e58b325-d55e-427e-9a3f-405f3ebd10c3",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTZ4qKRXuWA9xWc3xaC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fe0f0e8-eef9-41ac-befa-dae63b04ba04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQEDyyDregLSdUhKCtBRkq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 46264,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 46264,
          "cache_creation_input_tokens": 985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 985,
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

_source line 80 · 2026-05-10T19:42:22.107Z_

<details><summary>↩ Tool result · `toolu_01TGRrHvfAu3TnT4aW5yCav8`</summary>

```text
Web search results for query: ""Hold Onto That Thought" KV cache compression reasoning NeurIPS 2025"

Links: [{"title":"NeurIPS Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://neurips.cc/virtual/2025/loc/san-diego/126664"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=OtZtLYAdQY"},{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"NeurIPS Poster R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120110"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://openreview.net/pdf?id=OtZtLYAdQY"},{"title":"NeurIPS Poster Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://neurips.cc/virtual/2025/poster/119605"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"NeurIPS Poster KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse","url":"https://neurips.cc/virtual/2025/poster/116061"},{"title":"NeurIPS Towards Dynamic KV-Cache Compression: Fine-Grained Evaluation of Key and Value Ranks in LLMs","url":"https://neurips.cc/virtual/2025/loc/san-diego/122513"}]

I found relevant results for "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning" from NeurIPS 2025. Here's what the search revealed:

## Overview

The paper investigates how various KV cache compression strategies affect the performance of reasoning models on a variety of reasoning benchmarks.

## Key Findings

The KV cache, which is used to significantly speed up attention computations, grows quadratically with context length, and a suite of compression algorithms has been introduced to alleviate cache growth by evicting unimportant tokens.

The research reveals important differences between reasoning and non-reasoning models:

- For the non-reasoning Llama-3.1-8B-Instruct, no singular strategy fits all, and performance is heavily influenced by dataset type
- However, H2O and a decoding-enabled variant of SnapKV are dominant strategies for reasoning models such as Deepseek-R1 distillations, indicating the utility of heavy-hitter tracking for reasoning traces

## Notable Tradeoff

Eviction strategies at low budgets can produce longer reasoning traces, revealing a tradeoff between cache size and inference costs.

The paper was published on October 16, 2025 as part of the NeurIPS 2025 ER Workshop, and the full preprint is available on arXiv and OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fe0f0e8-eef9-41ac-befa-dae63b04ba04",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "c0a6e0e1-f99a-4e84-86ba-994efd07a8fb",
  "sourceToolAssistantUUID": "3fe0f0e8-eef9-41ac-befa-dae63b04ba04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-10T19:42:24.189Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DZCPF3tUdKsbLVd73sCEtn`</summary>

```json
{
  "query": "\"Inference-Time Hyper-Scaling\" KV cache compression NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a6e0e1-f99a-4e84-86ba-994efd07a8fb",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTZizVkr6um2T5zpJgW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d41b3b6b-b7b6-4c76-9774-762079c47fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GH6E4qmhNgspQTrjBEQLZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 47249,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1052
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 47249,
          "cache_creation_input_tokens": 1052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1052,
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

_source line 82 · 2026-05-10T19:42:31.626Z_

<details><summary>↩ Tool result · `toolu_01DZCPF3tUdKsbLVd73sCEtn`</summary>

```text
Web search results for query: ""Inference-Time Hyper-Scaling" KV cache compression NeurIPS 2025"

Links: [{"title":"NeurIPS Poster Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://neurips.cc/virtual/2025/poster/119605"},{"title":"[2506.05345] Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/abs/2506.05345"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=8ZiElzQxf1"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression Adrian Ła´ncucki†","url":"https://openreview.net/pdf?id=8ZiElzQxf1"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"NVIDIA Researchers Introduce Dynamic Memory Sparsification (DMS) for 8× KV Cache Compression in Transformer LLMs - MarkTechPost","url":"https://www.marktechpost.com/2025/06/11/nvidia-researchers-introduce-dynamic-memory-sparsification-dms-for-8x-kv-cache-compression-in-transformer-llms/"},{"title":"NeurIPS Poster ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120181"},{"title":"KVQuant: Towards 10 Million Context Length LLM Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/028fcbcf85435d39a40c4d61b42c99a4-Paper-Conference.pdf"},{"title":"nvidia/Qwen3-8B-DMS-8x · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-8B-DMS-8x"}]

I found excellent results about "Inference-Time Hyper-Scaling with KV Cache Compression" from NeurIPS 2025. Here's what the research is about:

## Overview

Inference-time hyper-scaling uses key–value cache compression with Delayed Memory Sparsification (DMS) to boost Transformer LLM reasoning accuracy for equivalent compute or memory costs.

## The Problem and Solution

In Transformer LLMs, generation cost is bottlenecked by the size of the key-value (KV) cache, rather than the number of generated tokens. Hence, researchers explore inference-time hyper-scaling: by compressing the KV cache, they can generate more tokens within the same compute budget and further improve the accuracy of scaled inference.

## Dynamic Memory Sparsification (DMS)

DMS is a novel method for sparsifying KV caches that only requires 1K training steps to achieve 8× compression, while maintaining better accuracy than training-free sparse attention. Instead of prematurely discarding cached tokens, DMS delays token eviction, implicitly merging representations and preserving critical information.

## Results

The research demonstrates the effectiveness of inference-time hyper-scaling with DMS on multiple families of LLMs, showing that it boosts accuracy for comparable inference latency and memory load. For instance, it enhances Qwen-R1 32B by 9.1 points on AIME 24, 7.6 on GPQA, and 9.6 on LiveCodeBench on average for an equivalent number of memory reads.

The research was accepted as a NeurIPS 2025 poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d41b3b6b-b7b6-4c76-9774-762079c47fd5",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "0c3b1714-0b49-4683-8176-e3d7179e6659",
  "sourceToolAssistantUUID": "d41b3b6b-b7b6-4c76-9774-762079c47fd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-10T19:42:34.901Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H1FNEvxa9W9As4r5JeKnH6`</summary>

```json
{
  "query": "\"Dynamic Model Routing\" \"Cascading\" efficient LLM inference survey 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c3b1714-0b49-4683-8176-e3d7179e6659",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTaRdFcmS1gveqN184V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "927a79af-a73e-44d1-89b4-37627271d8af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NT65cUv7Ade51dbt3aFLS1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 48301,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1091
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 48301,
          "cache_creation_input_tokens": 1091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1091,
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

_source line 84 · 2026-05-10T19:42:42.735Z_

<details><summary>↩ Tool result · `toolu_01H1FNEvxa9W9As4r5JeKnH6`</summary>

```text
Web search results for query: ""Dynamic Model Routing" "Cascading" efficient LLM inference survey 2026"

Links: [{"title":"[2603.04445] Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey","url":"https://arxiv.org/abs/2603.04445"},{"title":"Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey","url":"https://arxiv.org/html/2603.04445v1"},{"title":"Paper page - Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey","url":"https://huggingface.co/papers/2603.04445"},{"title":"Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey [Quick Review]","url":"https://liner.com/review/dynamic-model-routing-and-cascading-for-efficient-llm-inference-survey"},{"title":"Universal Model Routing for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=ka82fvJ5f1"},{"title":"UNIVERSAL MODEL ROUTING FOR EFFICIENT LLM ...","url":"https://openreview.net/pdf?id=ka82fvJ5f1"},{"title":"Towards Efficient Multi-LLM Inference: Characterization and Analysis of LLM Routing and Hierarchical Techniques","url":"https://arxiv.org/html/2506.06579v1"},{"title":"Universal Model Routing for Efficient LLM Inference","url":"https://arxiv.org/html/2502.08773v1"},{"title":"A Unified Approach to Routing and Cascading for LLMs | OpenReview","url":"https://openreview.net/forum?id=AAl89VNNy1"},{"title":"Dynamic Mix Precision Routing for Efficient Multi-step LLM Interaction","url":"https://arxiv.org/html/2602.02711"}]

Based on the search results, I found a comprehensive survey directly matching your query. Here are the key findings:

## Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey (2026)

The rapid growth of large language models with diverse capabilities, costs, and domains has created a critical need for intelligent model selection at inference time, with dynamic routing systems that adaptively select models based on query characteristics emerging as a solution to this challenge.

### Overview and Scope

The survey maps the state of the art in multi-LLM routing and cascading across six paradigms: difficulty-aware routing, human preference alignment, clustering, reinforcement learning, uncertainty quantification, and cascading. In contrast to mixture-of-experts architectures, which route within a single model, the survey studies routing across multiple independently trained LLMs.

### Key Approaches

The survey covers several major routing and cascading techniques:

- **Clustering-based Routing**: Incoming queries are compared against cluster centroids to determine which LLM should handle the request, with a key practical advantage being the ability to add new LLMs at inference time without retraining.

- **Cascading Systems**: Cascading frameworks prioritize smaller, cost-efficient models for simpler tasks and escalate to larger models only when necessary, minimizing resource usage while maintaining output quality.

- **Unified Approaches**: Recent work derives optimal strategies for cascading and proposes cascade routing, a unified framework that integrates routing and cascading into a theoretically optimal strategy.

The paper was published on arXiv on February 23, 2026, with updates through April 21, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "927a79af-a73e-44d1-89b4-37627271d8af",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "6e0993fe-d136-4967-9407-48ca606eea13",
  "sourceToolAssistantUUID": "927a79af-a73e-44d1-89b4-37627271d8af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-10T19:42:45.698Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KscFfSoCECfV45b3SSKeSR`</summary>

```json
{
  "query": "\"Spark Transformer\" reactivating sparsity FFN attention Google NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e0993fe-d136-4967-9407-48ca606eea13",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTbF7kibY3WMjvLRJW3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44360317-b5a8-4003-b12b-83226fbd58f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6zFwHPjLHo4eaeKtkLWGN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 49392,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 49392,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 944,
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

_source line 86 · 2026-05-10T19:42:53.649Z_

<details><summary>↩ Tool result · `toolu_01KscFfSoCECfV45b3SSKeSR`</summary>

```text
Web search results for query: ""Spark Transformer" reactivating sparsity FFN attention Google NeurIPS 2025"

Links: [{"title":"[2506.06644] Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://arxiv.org/abs/2506.06644"},{"title":"Spark Transformer: Reactivating Sparsity in Transformer FFN and Attention | OpenReview","url":"https://openreview.net/forum?id=o4zN34ahEK"},{"title":"NeurIPS Poster Reactivating Sparsity in Transformer FFN and Attention","url":"https://neurips.cc/virtual/2025/poster/116081"},{"title":"NeurIPS Poster Spark Transformer: Reactivating Sparsity in Transformer FFN and Attention","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116081"},{"title":"Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://arxiv.org/html/2506.06644v2"},{"title":"Chong You' Homepage - Homepage","url":"https://chongyou.github.io/"},{"title":"Universal Properties of Activation Sparsity in Modern Large Language Models","url":"https://arxiv.org/html/2509.00454v2"},{"title":"SPARK TRANSFORMER: HOW MANY FLOPS IS A TO","url":"https://openreview.net/pdf?id=iOy2pITOoH"},{"title":"Test-Time Acceleration for LLMs via Global-Local Neural ...","url":"https://arxiv.org/pdf/2508.14302"},{"title":"(PDF) Spark Transformer: Reactivating Sparsity in FFN and Attention","url":"https://www.researchgate.net/publication/392529906_Spark_Transformer_Reactivating_Sparsity_in_FFN_and_Attention"}]

I found comprehensive information about the Spark Transformer paper. Here's what the search revealed:

## Overview

Spark Transformer was published at NeurIPS 2025 as a poster presentation. The paper was authored by researchers from Google DeepMind and other institutions.

## Key Motivation

The discovery of the lazy neuron phenomenon, where fewer than 10% of feedforward network (FFN) parameters in trained Transformers are activated per token, has spurred significant interests in activation sparsity for enhancing large model efficiency. However, modern Transformers have moved away from the ReLU activation function crucial to this phenomenon, and existing efforts on re-introducing activation sparsity often degrade model quality, increase parameter count, or complicate training.

## Main Contributions

Spark Transformer is a novel architecture that achieves high activation sparsity in both FFN and the attention mechanism while maintaining model quality, parameter count, and standard training procedures, realizing sparsity via top-k masking for explicit control over sparsity level.

The paper introduces statistical top-k, a hardware-accelerator-friendly, linear-time approximate algorithm that avoids costly sorting and mitigates significant training slowdown from standard top-k operators. Furthermore, Spark Transformer reallocates existing FFN parameters and attention key embeddings to form a low-cost predictor for identifying activated entries, which mitigates quality loss from enforced sparsity and enhances wall-time benefit.

## Performance Results

Pretrained with the Gemma-2 recipe, Spark Transformer demonstrates competitive performance on standard benchmarks while exhibiting significant sparsity: only 8% of FFN neurons are activated, and each token attends to a maximum of 256 tokens, translating to a 2.5x reduction in FLOPs and leading to decoding wall-time speedups of up to 1.79x on CPU and 1.40x on GPU.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44360317-b5a8-4003-b12b-83226fbd58f1",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "e503036d-218f-4a9b-8745-85dc8117a337",
  "sourceToolAssistantUUID": "44360317-b5a8-4003-b12b-83226fbd58f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-10T19:42:56.345Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BPi8vqfFD3SbXa1QtX3ove`</summary>

```json
{
  "query": "\"DECS\" overthinking reasoning models decoupled reward token length 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e503036d-218f-4a9b-8745-85dc8117a337",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTc3nu2vcbvwtjn8h6X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be21b795-5ed9-454f-ae2d-d7e5d6ea005a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3LW43rPQW2DmzP5paKzNo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 50336,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 50336,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1023,
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

_source line 88 · 2026-05-10T19:43:04.732Z_

<details><summary>↩ Tool result · `toolu_01BPi8vqfFD3SbXa1QtX3ove`</summary>

```text
Web search results for query: ""DECS" overthinking reasoning models decoupled reward token length 2026"

Links: [{"title":"Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling | OpenReview","url":"https://openreview.net/forum?id=kdeiRledV6"},{"title":"GitHub - pixas/DECS: Official implementation for ICLR 2026 Oral: Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling · GitHub","url":"https://github.com/pixas/DECS"},{"title":"Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling","url":"https://arxiv.org/html/2509.25827"},{"title":"[2509.25827] Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling","url":"https://arxiv.org/abs/2509.25827"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"Preprint, under review OVERTHINKING REDUCTION WITH DECOUPLED RE-","url":"https://arxiv.org/pdf/2509.25827"},{"title":"(PDF) Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling","url":"https://www.researchgate.net/publication/396048783_Overthinking_Reduction_with_Decoupled_Rewards_and_Curriculum_Data_Scheduling"},{"title":"DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization","url":"https://arxiv.org/html/2510.04474v1"},{"title":"README.md · Flexan/pixas-DECS_1.5B-GGUF at main","url":"https://huggingface.co/Flexan/pixas-DECS_1.5B-GGUF/blob/main/README.md"},{"title":"[2510.04474] DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization","url":"https://arxiv.org/abs/2510.04474"}]

Based on the search results, I found comprehensive information about DECS:

## DECS: Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling

DECS addresses the critical issue of "overthinking," where large reasoning models trained with reinforcement learning generate excessively long reasoning paths without any performance benefit.

### Key Problems Identified

Existing solutions that penalize length often fail, inducing performance degradation due to a fundamental misalignment between trajectory-level rewards and token-level optimization. DECS was built on a theoretical discovery of two previously unaddressed flaws in current length rewards: (1) the erroneous penalization of essential exploratory tokens and (2) the inadvertent rewarding of partial redundancy.

### Framework Innovations

The framework includes (i) a first-of-its-kind decoupled token-level reward mechanism that surgically distinguishes and penalizes redundant tokens, and (ii) a novel curriculum batch scheduling strategy.

Specifically, DECS finetunes a small language model to detect the necessary reasoning prefix (NRP) from other redundancy, which are separately rewarded to penalize overthinking consistently while maintaining the probability for generating necessary reasoning steps.

### Results

DECS can achieve a dramatic reduction in reasoning tokens by over 50% across seven benchmarks while simultaneously maintaining or even improving performance. DECS reduces average reasoning length by 57.17% on the 1.5B model while improving pass@1 accuracy by +2.48 points, and on the 7B model, DECS cuts thinking tokens by 49.50%, outperforming all baselines, with a +0.8 point accuracy gain.

### Academic Recognition

DECS was accepted as an ICLR 2026 Oral paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be21b795-5ed9-454f-ae2d-d7e5d6ea005a",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "b899f713-18fb-4b81-946a-0624226eabae",
  "sourceToolAssistantUUID": "be21b795-5ed9-454f-ae2d-d7e5d6ea005a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-10T19:43:06.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014fBNt5rYmjMMXyCwxfhvcF`</summary>

```json
{
  "query": "\"Rethinking KV Cache Eviction\" information theoretic 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b899f713-18fb-4b81-946a-0624226eabae",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTcsEgMTgWKa2XBUcVg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "969a5fbc-6f50-4a37-9b3a-a43c43d3cce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDcSmTiPW2YjTw1r8Kg3qc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 51359,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1024
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 51359,
          "cache_creation_input_tokens": 1024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1024,
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

_source line 90 · 2026-05-10T19:43:13.015Z_

<details><summary>↩ Tool result · `toolu_014fBNt5rYmjMMXyCwxfhvcF`</summary>

```text
Web search results for query: ""Rethinking KV Cache Eviction" information theoretic 2026"

Links: [{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/html/2604.25975"},{"title":"[Literature Review] HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing","url":"https://www.themoonlight.io/en/review/hashevict-a-pre-attention-kv-cache-eviction-strategy-using-locality-sensitive-hashing"},{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899"},{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution | OpenReview","url":"https://openreview.net/forum?id=k5h29Qv7GN"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"}]

I found the paper you're looking for! The paper titled "Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective" was published in April 2026.

Here's what the research covers:

**Main Approach:**
The work rethinks KV cache eviction through the lens of the Information Bottleneck principle, deriving a closed-form mutual information objective that characterizes the effective information capacity of a retained KV cache subset.

**Key Insight:**
The formulation reveals that a wide range of existing eviction strategies can be interpreted as different approximations of the same capacity-maximization principle.

**Proposed Method:**
The authors introduce CapKV, a capacity-aware eviction method that directly targets information preservation via a log-determinant approximation using statistical leverage scores, replacing heuristic selection with a theoretically grounded mechanism that preserves the maximum predictive signal.

**Results:**
Extensive experiments across multiple models and long-context benchmarks show that CapKV consistently outperforms prior methods, achieving a better trade-off between memory efficiency and generational fidelity.

The paper was authored by Chenwei Tang and collaborators, published on arXiv on April 28, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "969a5fbc-6f50-4a37-9b3a-a43c43d3cce0",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "07331934-a032-4518-ba1a-b743618e0b31",
  "sourceToolAssistantUUID": "969a5fbc-6f50-4a37-9b3a-a43c43d3cce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-10T19:43:14.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TC8aUkeUnwSESFWYHV1qbK`</summary>

```json
{
  "query": "\"DefensiveKV\" fragility KV cache eviction ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07331934-a032-4518-ba1a-b743618e0b31",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTdUkrTFVyF65gCZ7Tu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "441ef54b-486a-4ec1-9343-7853717f7d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wsg9rv18Eh1boatEXqFWJ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1010,
      "cache_read_input_tokens": 52383,
      "output_tokens": 72,
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
          "output_tokens": 72,
          "cache_read_input_tokens": 52383,
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

### Tool result

_source line 92 · 2026-05-10T19:43:23.278Z_

<details><summary>↩ Tool result · `toolu_01TC8aUkeUnwSESFWYHV1qbK`</summary>

```text
Web search results for query: ""DefensiveKV" fragility KV cache eviction ICLR 2026"

Links: [{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...","url":"https://openreview.net/pdf?id=nJgS06sX3O"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/abs/2510.13334"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION","url":"https://openreview.net/pdf/2d8c7805c4fcdb477dd04f7b60dd05bd9551c246.pdf"},{"title":"[PDF] Taming the Fragility of KV Cache Eviction in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Taming-the-Fragility-of-KV-Cache-Eviction-in-LLM-Feng-Guo/10b323b80b3f57a7f15d44eb5a72872a3adfbcb3"},{"title":"GitHub - SamsungLabs/LookaheadKV: [ICLR 2026] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation · GitHub","url":"https://github.com/SamsungLabs/LookaheadKV"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"ICLR LLMs Know What to Drop: Self-Attention Guided KV Cache Eviction for Efficient Long-Context Inference","url":"https://iclr.cc/virtual/2025/33493"}]

Based on the search results, here's what I found about DefensiveKV:

## Overview

DefensiveKV is an official implementation for an ICLR 2026 paper titled "Taming the Fragility of KV Cache Eviction in LLM Inference".

## Problem & Solution

The work exposes the inherent fragility of stability assumptions in KV cache eviction methods and introduces defensive aggregation to counter this issue, reducing quality loss by over 4x compared to leading methods.

Specifically, recent cache eviction methods employ a scoring-aggregation framework based on the "stability assumption"—that a fixed subset of entries remains consistently important during generation. However, this underlying assumption is inherently fragile, making mean aggregation highly vulnerable in extreme cases.

## Core Innovation

The authors propose a simple yet elegant defensive aggregation strategy: a two-step, linear-time approach that controls worst-case risk, thereby defending against extreme cases with negligible computational overhead.

## Performance Results

DefensiveKV and its extension Layer-DefensiveKV incorporate layer-wise budget allocation and reduce generation quality loss by 2.3× and 4.3× respectively versus the strongest baseline under a 20% cache size.

The implementation introduces defensive aggregation on top of the current SOTA method, (Ada-)CriticalKV, and advances from AdaKV to CriticalKV then DefensiveKV, boosting performance from 39.0 to 91.4.

The official code is available on [GitHub](https://github.com/FFY0/DefensiveKV).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "441ef54b-486a-4ec1-9343-7853717f7d20",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "217f1d47-4411-4336-b20f-970b9dd8fb2f",
  "sourceToolAssistantUUID": "441ef54b-486a-4ec1-9343-7853717f7d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-10T19:43:27.091Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B25eU9nPnsB7qcEQsFXW79`</summary>

```json
{
  "query": "attention head pruning MLP sparsity joint optimization LLM inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "217f1d47-4411-4336-b20f-970b9dd8fb2f",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTeEY7jHsCwCWfjFjCx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81b8b692-8632-4c8d-a4a1-3b8457944396",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6ipV6fRwWjuXJtWSCvhzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 53393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-10T19:43:37.316Z_

<details><summary>↩ Tool result · `toolu_01B25eU9nPnsB7qcEQsFXW79`</summary>

```text
Web search results for query: "attention head pruning MLP sparsity joint optimization LLM inference 2025 2026"

Links: [{"title":"Attention Heads and MLP Pruning - Efficient LLMs with AMP","url":"https://arxiv.org/pdf/2504.21174"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/html/2504.21174v1"},{"title":"[2504.21174] Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/abs/2504.21174"},{"title":"Efficient self-attention with smart pruning for sustainable large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92586-5"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"HAPE: Hardware-Aware LLM Pruning For Efficient On-Device Inference Optimization | ACM Transactions on Design Automation of Electronic Systems","url":"https://dl.acm.org/doi/10.1145/3744244"},{"title":"Compressing and Deploying Efficient LLMs for ...","url":"https://aclanthology.org/2025.emnlp-industry.119.pdf"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250421174G/abstract"},{"title":"Structured-Then-Unstructured Pruning for Scalable MoE ...","url":"https://aclanthology.org/2025.acl-long.671.pdf"}]

Based on the search results, here's what I found regarding attention head pruning, MLP sparsity, joint optimization, and LLM inference in 2025-2026:

## Key Recent Research

AMP (Attention Heads and MLP Pruning) is a novel structured pruning method that efficiently compresses LLMs by removing less critical structures within Multi-Head Attention (MHA) and Multilayer Perceptron (MLP). AMP uses the magnitude of activations – rather than solely the weights – to evaluate the importance of structures within each layer, ensuring uniform pruning throughout all layers.

AMP achieves mean accuracy improvements of up to 4.81 percentage points for LLaMA 7B and 9.52 pp for LLaMA-2 7B, and perplexity evaluation on WikiText2 corroborates the results by demonstrating the consistency of AMP across many compression rates. AMP achieves up to 1.25× inference speedup without requiring specialized hardware.

## Joint Optimization Approaches

Developing joint optimization strategies or analytical bounds that predict the compounded impact of multiple compression methods remains a key unresolved problem in the field. Recent work has begun addressing this gap, particularly with hardware-aware approaches that break the layer-by-layer pruning setting and fuse several layers into one pruning stage to allow cross-layer optimization.

## Combined Pruning Strategies

A two-stage approach involves removing redundant experts with expert-level structured pruning, then performing unstructured pruning inside individual experts, demonstrating how combined strategies can be effectively applied to LLMs like Mixtral.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81b8b692-8632-4c8d-a4a1-3b8457944396",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "b002fabb-6690-4c85-8a0d-1338b6384422",
  "sourceToolAssistantUUID": "81b8b692-8632-4c8d-a4a1-3b8457944396",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-10T19:43:39.520Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011nqvjtn1MrNyGu4hREcZEd`</summary>

```json
{
  "query": "\"Masked Gated Linear Unit\" MLP sparsity activation LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b002fabb-6690-4c85-8a0d-1338b6384422",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTfGUiqnFA2SMfJx34T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca388c9c-60b7-4ada-b361-bb0c179eb759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1DGsL6emNJdLcQfBsuja1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 54526,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 54526,
          "cache_creation_input_tokens": 985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 985,
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

_source line 96 · 2026-05-10T19:43:47.106Z_

<details><summary>↩ Tool result · `toolu_011nqvjtn1MrNyGu4hREcZEd`</summary>

```text
Web search results for query: ""Masked Gated Linear Unit" MLP sparsity activation LLM 2026"

Links: [{"title":"Masked Gated Linear Unit","url":"https://arxiv.org/html/2506.23225v1"},{"title":"Masked Gated Linear Unit | OpenReview","url":"https://openreview.net/forum?id=5OnejG2SQH"},{"title":"Optimizing LLM Inference: Sparse Activation, MoE, and Gated-MLP Efficiency | HackerNoon","url":"https://hackernoon.com/optimizing-llm-inference-sparse-activation-moe-and-gated-mlp-efficiency"},{"title":"[2506.23225] Masked Gated Linear Unit","url":"https://arxiv.org/abs/2506.23225"},{"title":"arXiv:2505.21364v1 [cs.LG] 27 May 2025","url":"https://arxiv.org/pdf/2505.21364"},{"title":"MLP Gate & Up Tuning: Efficient Neural Adaptation","url":"https://www.emergentmind.com/topics/mlp-gate-up-tuning"},{"title":"Masked Gated Linear Unit - ADS - Astrophysics Data System","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250623225T/abstract"},{"title":"Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2408.14690v1"},{"title":"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models | Scaling Intelligence Lab at Stanford University","url":"https://scalingintelligence.stanford.edu/blogs/cats/"},{"title":"[PDF] GLU Variants Improve Transformer | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLU-Variants-Improve-Transformer-Shazeer/bdbf780dfd6b3eb0c9e980887feae5f23af15bc4"}]

Based on the search results, here's what I found about Masked Gated Linear Units:

## Overview

Masked Gated Linear Units (MGLUs) are a novel family of GLUs with an efficient kernel implementation designed to improve upon traditional gated linear units in large language models.

## The Problem Being Addressed

Gated Linear Units (GLUs) have become essential components in the feed-forward networks of state-of-the-art Large Language Models, but they require twice as many memory reads compared to feed-forward layers without gating, due to the use of separate weight matrices for the gate and value streams.

## Key Technical Contributions

The core contributions of MGLUs include: (1) the Mixture of Element-wise Gating (MoEG) architecture that learns multiple binary masks, each determining gate or value assignments at the element level on a single shared weight matrix resulting in reduced memory transfer, and (2) FlashMGLU, a hardware-friendly kernel that yields up to a 19.7× inference-time speed-up over a naive PyTorch MGLU and is 47% more memory-efficient and 34% faster than standard GLUs despite added architectural complexity on an RTX5090 GPU.

## Performance Results

In LLM experiments, the Swish-activated variant SwiMGLU preserves its memory advantages while matching—or even surpassing—the downstream accuracy of the SwiGLU baseline.

The research was recently published, with the paper made available in June 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca388c9c-60b7-4ada-b361-bb0c179eb759",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "f0b9c637-23e0-43c1-ac61-7bbcfff9c185",
  "sourceToolAssistantUUID": "ca388c9c-60b7-4ada-b361-bb0c179eb759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-10T19:43:49.091Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FAvkKXRgY4JZmTo5V6MvYP`</summary>

```json
{
  "query": "\"reasoning-aware\" \"calibration\" pruned model compression reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b9c637-23e0-43c1-ac61-7bbcfff9c185",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTfzP8RJMT2JsseLgGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a504b5c3-6ba8-48a4-95d3-50fc8c4c05b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qQkXZDBDn1SZfiYbsXzgX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 55511,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 55511,
          "cache_creation_input_tokens": 959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 959,
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

_source line 98 · 2026-05-10T19:43:55.020Z_

<details><summary>↩ Tool result · `toolu_01FAvkKXRgY4JZmTo5V6MvYP`</summary>

```text
Web search results for query: ""reasoning-aware" "calibration" pruned model compression reasoning 2026"

Links: [{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"REASONING MODELS CAN BE ACCURATELY PRUNED","url":"https://openreview.net/pdf/fa7d9bd278a00e3b281567830445203221970fe7.pdf"}]

Based on the search results, I found relevant research on reasoning-aware calibration for model compression. Here are the key findings:

## Reasoning-Aware Compression (RAC)

Reasoning-Aware Compression (RAC) augments calibration with on-policy chain-of-thought (CoT) activations, addressing a critical challenge in compressing reasoning language models.

### The Problem

Standard pruning and quantization pipelines, which calibrate only on prompt activations, strongly degrade accuracy and runtime when compressing reasoning language models, often producing longer and less reliable reasoning traces.

### The Solution

RAC integrates seamlessly with existing pruning algorithms such as SparseGPT, requiring no retraining or distillation. RAC consistently outperforms both baseline calibration methods, particularly at higher sparsity levels where standard compression techniques cause severe performance loss.

### Performance Results

On-policy calibration generally outperforms off-policy calibration, particularly at higher sparsity levels (50% sparsity: 0.900 vs 0.876 accuracy). Additionally, across Math500, AIME, and LiveCodeBench, domain-relevant calibration consistently outperforms generic C4, but RAC provides the most robust pruned models, especially at high sparsity.

The research demonstrates that RAC can be used in conjunction with other LLM pruning algorithms, such as ALPS and WANDA, making it a versatile approach for model compression.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a504b5c3-6ba8-48a4-95d3-50fc8c4c05b0",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "88fb375b-f40e-4996-900f-ac5556c2a323",
  "sourceToolAssistantUUID": "a504b5c3-6ba8-48a4-95d3-50fc8c4c05b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-10T19:43:57.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013hPcop3g2Gf3AaTLXaQ8Md`</summary>

```json
{
  "query": "\"KV Cache Transform Coding\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88fb375b-f40e-4996-900f-ac5556c2a323",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTgaA8HfS2UBq7r17pS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81e1e86c-df53-4435-b1a2-286c22cdc447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHTVmYocTBJKbWZc2ij4qr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 548,
      "cache_read_input_tokens": 56470,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 56470,
          "cache_creation_input_tokens": 548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 548,
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

_source line 100 · 2026-05-10T19:44:02.484Z_

<details><summary>↩ Tool result · `toolu_013hPcop3g2Gf3AaTLXaQ8Md`</summary>

```text
Web search results for query: ""KV Cache Transform Coding" ICLR 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"ICLR Poster KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://iclr.cc/virtual/2026/poster/10008708"},{"title":"GitHub - OnlyTerp/kvtc: First open-source KVTC implementation (NVIDIA, ICLR 2026) -- 8-32x KV cache compression via PCA + adaptive quantization + entropy coding · GitHub","url":"https://github.com/OnlyTerp/kvtc"},{"title":"KV Cache Transform Coding for Compact Storage in LLM Inference [Quick Review]","url":"https://liner.com/review/kv-cache-transform-coding-for-compact-storage-in-llm-inference"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"[2511.01815] KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://arxiv.org/abs/2511.01815"},{"title":"TurboQuant: Redefining AI efficiency with extreme compression","url":"https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/"},{"title":"Aihola","url":"https://aihola.com/article/google-turboquant-kv-cache-compression"},{"title":"GitHub - AmesianX/TurboQuant: TurboQuant KV Cache Compression for llama.cpp — 5.2x memory reduction with near-lossless quality | Implementation of Google DeepMind's TurboQuant (ICLR 2026)","url":"https://github.com/AmesianX/TurboQuant"},{"title":"KV Cache Transform Coding for Compact Storage in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=aNVKROYpLB"}]

## Results for "KV Cache Transform Coding" ICLR 2026

I found comprehensive information about this paper. Here's what the research presents:

### Overview

KVTC (Key-Value Transform Coding) is a lightweight transform coder that compresses KV caches for compact on-GPU and off-GPU storage, developed by researchers at NVIDIA and University of Warsaw.

### Technical Approach

KVTC combines PCA-based feature decorrelation, adaptive quantization, and entropy coding, building upon the transform-coding framework used in image and video compression algorithms such as JPEG. It applies feature decorrelation by projecting onto an orthonormal basis matrix obtained via singular value decomposition (SVD) of centered calibration data (i.e., principal component analysis, PCA).

### Performance

KVTC achieves up to 20x compression while maintaining reasoning and long-context accuracy, and 40x or higher for specific use cases. The research tests KVTC with Llama 3, Mistral NeMo, and R1-Qwen 2.5 models across multiple benchmarks, and it consistently outperforms inference-time baselines such as token eviction, quantization, and SVD-based methods while achieving higher compression ratios.

### Practical Benefits

The method requires only a brief initial calibration and leaves model parameters unchanged. The paper was published at ICLR 2026 and an open-source implementation is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81e1e86c-df53-4435-b1a2-286c22cdc447",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "958ebf82-7529-4106-8a7f-4e07c2ef04ef",
  "sourceToolAssistantUUID": "81e1e86c-df53-4435-b1a2-286c22cdc447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-10T19:44:05.233Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VfuV2X6T2YFoWwKwmEHuHP`</summary>

```json
{
  "query": "\"Systematic Study\" \"Compression Ordering\" LLM quantization sparsity order 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "958ebf82-7529-4106-8a7f-4e07c2ef04ef",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTh86kKSp13XXvEP7YP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18a23db7-9364-4ad2-bcf3-ff0f6d76b9ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPyPfzLBgN5P8tnd8HEGwR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1144,
      "cache_read_input_tokens": 57018,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1144
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 57018,
          "cache_creation_input_tokens": 1144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1144,
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

_source line 102 · 2026-05-10T19:44:14.019Z_

<details><summary>↩ Tool result · `toolu_01VfuV2X6T2YFoWwKwmEHuHP`</summary>

```text
Web search results for query: ""Systematic Study" "Compression Ordering" LLM quantization sparsity order 2025"

Links: [{"title":"A Systematic Study of Compression Ordering for Large Language Models","url":"https://arxiv.org/html/2511.19495"},{"title":"SLIM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Research","url":"https://research.nvidia.com/publication/2025-06_slim-one-shot-quantization-and-sparsity-low-rank-approximation-llm-weight"},{"title":"Track: Session 3: Quantization and Sparsity","url":"https://mlsys.org/virtual/2025/session/3143"},{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2310.01382"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/html/2410.09615"},{"title":"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation","url":"https://arxiv.org/html/2602.09130"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Awesome-LLM-Compression/README.md at main · HuangOwen/Awesome-LLM-Compression","url":"https://github.com/HuangOwen/Awesome-LLM-Compression/blob/main/README.md"},{"title":"CASP: Compression of Large Multimodal Models Based on Attention Sparsity","url":"https://arxiv.org/html/2503.05936"}]

I found highly relevant results for your search query. Here are the key findings:

## Main Result: "A Systematic Study of Compression Ordering for Large Language Models"

This study presents a comprehensive analysis of how knowledge distillation, structured pruning, and quantization interact when applied sequentially to compress Qwen LLMs. The results show that while each technique individually contributes to model efficiency, their performance is heavily dependent on the ordering.

### Key Findings:

**Compression Performance:**
- Quantization consistently offered the highest compression with acceptable quality loss, whereas pruning introduced structural sparsity at the expense of increased perplexity.

**Optimal Ordering:**
- Among all evaluated sequences, P-KD-Q emerged as the most effective, achieving substantial compression while maintaining high G-Eval and clarity scores. (P-KD-Q refers to Pruning → Knowledge Distillation → Quantization)
- Sequences featuring early quantization exhibited severe degradation due to irreversible quantization noise affecting downstream training.

**Evaluation Metrics:**
Multiple compression pipelines were evaluated, including single and proposed three-technique sequences, using perplexity, G-Eval, clarity, prompt alignment, and compression ratio as metrics.

### Related Work:

The search also revealed UniComp, a UNIfied COMPression evaluation framework, which systematically compares pruning, quantization, and knowledge distillation across contemporary LLMs and benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18a23db7-9364-4ad2-bcf3-ff0f6d76b9ef",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "df984dd2-b5e0-409f-99f9-cc68796fd2ea",
  "sourceToolAssistantUUID": "18a23db7-9364-4ad2-bcf3-ff0f6d76b9ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-10T19:44:16.509Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HXLW6BAV9mhqn7ZdowqMVk`</summary>

```json
{
  "query": "\"layer-wise sensitivity\" sparsity allocation efficient LLM inference 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df984dd2-b5e0-409f-99f9-cc68796fd2ea",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauThySP17uTqMf6SLXYb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37276e8a-b61f-4ed1-8e20-0f87574cdd79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExVt6nvdqtvAfF4r9EPEwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 58162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 977,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-10T19:44:24.761Z_

<details><summary>↩ Tool result · `toolu_01HXLW6BAV9mhqn7ZdowqMVk`</summary>

```text
Web search results for query: ""layer-wise sensitivity" sparsity allocation efficient LLM inference 2026"

Links: [{"title":"Layer-wise Sensitivity-aware Sparsity Allocation for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=erGq3kjCmy"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-aware Mixed Activation Sparsity","url":"https://arxiv.org/html/2602.14452"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"Published as a conference paper at ICLR 2026 LSA: LAYER-WISE SPARSITY","url":"https://openreview.net/pdf?id=xq3lza5IjN"},{"title":"LAYER-WISE SENSITIVITY-AWARE SPARSITY ALLO","url":"https://openreview.net/pdf/33cf3ee13420561ddd777abf22f3695595290bbc.pdf"},{"title":"LSA: Layer-wise Sparsity Allocation for Large Language Model...","url":"https://openreview.net/forum?id=xq3lza5IjN"},{"title":"Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference","url":"https://arxiv.org/html/2604.07394"},{"title":"Determining Layer-wise Sparsity for Large Language Models Through a Theoretical Perspective | OpenReview","url":"https://openreview.net/forum?id=otNB7BzsiR"},{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"Layer-wise heterogeneity-guided heterogeneous pruning: An LLM compression method | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-026-00724-4"}]

I found several relevant research papers and works from 2026 on layer-wise sensitivity and sparsity allocation for efficient LLM inference. Here's a summary of the key findings:

## Key Research Works (2026)

**Adaptive Sparsity Allocation Framework (ASAF)**

ASAF is a novel approach that integrates rotation-based low-bit quantization with layer-wise adaptive sparsity allocation. The framework achieves up to 3.63× prefill acceleration and 12.63% memory reduction on NVIDIA RTX 3090 GPUs while sustaining benchmark accuracy degradation within 1%.

**Layer-wise Sparsity Allocation (LSA)**

LSA quantifies layer-wise importance by evaluating the minimal linear reconstruction error (LSE) of each transformer layer under the assumption that 50% of its least important weights are removed. At an overall sparsity ratio of 70%, LSA surpasses state-of-the-art methods across language modeling tasks and seven zero-shot tasks.

**WiSparse Method**

WiSparse leverages the joint importance of both weights and activations to guide sparsification, while assigning sparsity ratios according to sensitivity at both the block and layer levels.

**Theoretical Approach to Layer-wise Sparsity**

Researchers address the challenge of determining layer-wise sparsity rates through a theoretical perspective, identifying a critical issue of "reconstruction error explosion" in existing LLMs sparsification methods, where errors from earlier layers propagate and amplify in subsequent layers.

## Key Theme

This work advances beyond uniform compression strategies by recognizing and exploiting the distinct sensitivity characteristics of different transformer layers, establishing a new paradigm for adaptive LLM compression on commodity hardware.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37276e8a-b61f-4ed1-8e20-0f87574cdd79",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "58ba9887-ee2f-4b35-8b01-d6c55f018c51",
  "sourceToolAssistantUUID": "37276e8a-b61f-4ed1-8e20-0f87574cdd79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 105 · 2026-05-10T19:44:26.937Z_

Now let me search for a few more specific areas that could be highly relevant to the compound sparsity proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58ba9887-ee2f-4b35-8b01-d6c55f018c51",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTimRM44oYUCqvdbY4K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac4cc7fb-5c1c-44b1-b1c8-09308ea45dff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWzmdPtzSeXZSbgqMcEHaQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 59139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1040,
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

_source line 106 · 2026-05-10T19:44:27.565Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PotpYuYWRTDrtPDWeKLCF4`</summary>

```json
{
  "query": "\"Reasoning Models Can Be Accurately Pruned\" chain-of-thought reconstruction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac4cc7fb-5c1c-44b1-b1c8-09308ea45dff",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTimRM44oYUCqvdbY4K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ac390e0-5ecd-4157-8cf6-69307c6c150d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YWzmdPtzSeXZSbgqMcEHaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 59139,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1040
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 59139,
          "cache_creation_input_tokens": 1040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1040,
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

_source line 107 · 2026-05-10T19:44:35.974Z_

<details><summary>↩ Tool result · `toolu_01PotpYuYWRTDrtPDWeKLCF4`</summary>

```text
Web search results for query: ""Reasoning Models Can Be Accurately Pruned" chain-of-thought reconstruction 2025"

Links: [{"title":"[2509.12464] Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction","url":"https://arxiv.org/abs/2509.12464"},{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"NeurIPS Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://neurips.cc/virtual/2025/loc/san-diego/126571"},{"title":"Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction | OpenReview","url":"https://openreview.net/forum?id=tyGfwG6xTh"},{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://openreview.net/pdf?id=o9z7pK1C76"},{"title":"Qingquan Song's research works | Linkedin and other places","url":"https://www.researchgate.net/scientific-contributions/Qingquan-Song-2131402791"},{"title":"Rohan Paul on X: \"This paper shows how to prune reasoning LLMs while keeping accuracy high. It fixes the main reason, pruned reasoning models get slower and less accurate by aligning pruning with decoding. It plugs into existing SparseGPT-style pipelines without retraining or distillation, so it https://t.co/PHO0xN60lx\" / X","url":"https://x.com/rohanpaul_ai/status/1971170823227461772"},{"title":"Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models","url":"https://arxiv.org/html/2512.02185"},{"title":"Reasoning Models Sometimes Output Illegible Chains of Thought","url":"https://arxiv.org/html/2510.27338v1"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/html/2510.09312v1"}]

I found relevant research on this topic. Here's what the web search revealed about "Reasoning Models Can Be Accurately Pruned Via Chain-of-Thought Reconstruction":

## Overview

This is a research paper titled "Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction", published in September 2025.

## Problem Statement

The paper shows that using compression techniques such as neural network pruning produces greater performance loss than in typical language modeling tasks, and in some cases can make the model slower since they cause the model to produce more thinking tokens but with worse performance. This is partly due to the fact that standard LLM pruning methods often focus on input reconstruction, whereas reasoning is a decode-dominated task.

## Solution: Reasoning-Aware Compression (RAC)

During pruning, the researchers jointly reconstruct activations from the input and the model's on-policy chain-of-thought traces. This "Reasoning-Aware Compression" (RAC) integrates seamlessly into existing pruning workflows.

## Key Results

Under the RAC approach, reasoning LLMs can be pruned to 50% sparsity while maintaining up to 95% of the original model's accuracy on math and coding tasks. On math, a 7B model at 50% sparsity stays near 90% accuracy, while a generic C4 calibration drops to 74.4%.

The paper was presented at NeurIPS 2025 and addresses the significant challenge of compressing reasoning models like DeepSeek-R1 while preserving their reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ac390e0-5ecd-4157-8cf6-69307c6c150d",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "30131010-dc06-4444-94ea-da7bb4fe12cd",
  "sourceToolAssistantUUID": "0ac390e0-5ecd-4157-8cf6-69307c6c150d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-10T19:44:37.921Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016pdrr7hb8MESLfvnbCL1fJ`</summary>

```json
{
  "query": "\"Think Before You Prune\" self-reflective structured pruning reasoning LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30131010-dc06-4444-94ea-da7bb4fe12cd",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTjbJRE97pm9HWMo2CG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54d29f20-bcba-4dbc-a183-9875abb7fba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSLpM7RSz65JasgJVjUyKT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 60179,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 60179,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1034,
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

_source line 109 · 2026-05-10T19:44:45.833Z_

<details><summary>↩ Tool result · `toolu_016pdrr7hb8MESLfvnbCL1fJ`</summary>

```text
Web search results for query: ""Think Before You Prune" self-reflective structured pruning reasoning LLM 2025"

Links: [{"title":"[2512.02185] Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models","url":"https://arxiv.org/abs/2512.02185"},{"title":"Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models","url":"https://arxiv.org/html/2512.02185"},{"title":"Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models","url":"https://arxiv.org/html/2511.18864"},{"title":"Computation and Language Dec 2025","url":"https://arxiv.org/list/cs.CL/2025-12?skip=75&show=25"},{"title":"[2511.18864] Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models","url":"https://arxiv.org/abs/2511.18864"},{"title":"Think, Prune, Train, Improve: Scaling Reasoning Without Scaling Models","url":"https://arxiv.org/html/2504.18116"},{"title":"Can LLMs learn to reason without RL or large datasets?","url":"https://bdtechtalks.com/2025/05/05/think-prune-train/"},{"title":"ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2504.01296v1"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/html/2601.18091"},{"title":"Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning","url":"https://arxiv.org/html/2505.14582"}]

Based on the search results, I found two papers with the title "Think Before You Prune" related to pruning reasoning language models:

## "Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models"

Reasoning LLMs (RLMs) such as OpenAI o1, DeepSeek-R1, and Qwen3 deliver strong multi-step reasoning through chain-of-thought generation, but their large model sizes and lengthy decode-time outputs make them costly to deploy and unsuitable for resource-constrained settings.

Existing pruning methods severely damage RLMs, as even moderate sparsity (e.g., 20%) can collapse accuracy and completely disrupt the model's reasoning coherence. The brittleness largely stems from a mismatch between the calibration data, the pruning objective, and the model's decode-time reasoning behavior.

The most reliable calibration signal comes not from human-written labels but from the model's own self-generated reasoning traces, which more accurately reflect its inference distribution.

RESP, a self-reflective structured pruning framework aligns pruning decisions with the model's reasoning dynamics through self-generated calibration, decode-only gradient-based importance estimation, and progressive regeneration that maintains calibration fidelity as sparsity increases.

Experiments on Qwen3-8B demonstrate that RESP preserves near-dense accuracy at 20-30% sparsity. At 40% sparsity, RESP attains 81.3% accuracy on GSM8K and 59.6% on MathQA, surpassing the strongest baselines by 66.87% and 47%, respectively.

---

## "Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models"

A related paper published slightly earlier (November 24, 2025) explores using self-generated reasoning data for calibration to substantially improve pruning performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54d29f20-bcba-4dbc-a183-9875abb7fba3",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "f2e410b1-f88e-4bac-a3f6-37c721abcf0b",
  "sourceToolAssistantUUID": "54d29f20-bcba-4dbc-a183-9875abb7fba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-10T19:44:48.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011F7skXtNbGSTwJmV8MB5vb`</summary>

```json
{
  "query": "\"From LLMs to LRMs\" rethinking pruning reasoning-centric models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2e410b1-f88e-4bac-a3f6-37c721abcf0b",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTkKUC9BGmzVvQutkMw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6c32733-8b65-4f28-9f47-4d557d485682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CahbXwRqZTgoFUkayPHEZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 61213,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 61213,
          "cache_creation_input_tokens": 1034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1034,
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

_source line 111 · 2026-05-10T19:44:56.937Z_

<details><summary>↩ Tool result · `toolu_011F7skXtNbGSTwJmV8MB5vb`</summary>

```text
Web search results for query: ""From LLMs to LRMs" rethinking pruning reasoning-centric models 2026"

Links: [{"title":"[2601.18091] From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/abs/2601.18091"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/pdf/2601.18091"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models | OpenReview","url":"https://openreview.net/forum?id=eHHQEsphbN"},{"title":"FROM LLMS TO LRMS","url":"https://openreview.net/pdf?id=eHHQEsphbN"},{"title":"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Cy8Qa4gAst"},{"title":"When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models","url":"https://arxiv.org/html/2504.02010"},{"title":"DRP: Distilled Reasoning Pruning with Skill-aware Step Decomposition for Efficient Large Reasoning Models","url":"https://arxiv.org/html/2505.13975"},{"title":"Pruning the Unsurprising: Efficient LLM Reasoning via First-Token Surprisal","url":"https://arxiv.org/html/2508.05988"},{"title":"[2604.16029] Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning","url":"https://arxiv.org/abs/2604.16029"},{"title":"Efficient Compressing and Tuning Methods for Large Language Models: A Systematic Literature Review | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3728636"}]

Based on the web search results, I found the paper "From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models." Here's what the research is about:

## Overview

This work conducts the first systematic investigation of pruning across both LLM-instruct and LLM-think families. Large language models (LLMs) are increasingly costly to deploy, motivating extensive research on model pruning. However, most existing studies focus on instruction-following LLMs, leaving it unclear whether established pruning strategies transfer to reasoning-augmented models that explicitly generate long intermediate reasoning traces.

## Key Distinctions Between Model Types

The recent rise of reasoning-augmented models (LLM-think), which generate explicit chain-of-thought steps, presents an unstudied challenge for established pruning methods due to their substantially different generation patterns.

## Research Methodology

The study conducts a controlled study of pruning for both instruction-following (LLM-instruct) and reasoning-augmented (LLM-think) models. To isolate the effects of pruning, they align pruning calibration and post-pruning recovery data with each model's original training distribution, which yields more stable and reliable pruning behavior.

## Pruning Strategies Evaluated

The research evaluates static depth pruning, static width pruning, and dynamic pruning across 17 tasks spanning classification, generation, and reasoning. Static depth pruning removes entire layers, static width pruning reduces hidden dimensions (neurons or attention heads), and dynamic depth pruning adaptively skips layers, attention blocks, or MLP modules depending on the input.

The paper was submitted on January 26, 2026, making it a very recent contribution to the field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6c32733-8b65-4f28-9f47-4d557d485682",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "4b275f3b-b8c6-4cff-9132-0f55f8d0c507",
  "sourceToolAssistantUUID": "f6c32733-8b65-4f28-9f47-4d557d485682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-10T19:44:59.182Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AyWruvhr9dYAUwhYZLT9U7`</summary>

```json
{
  "query": "\"Adaptive Test-Time Compute\" KV cache DMS NVIDIA reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b275f3b-b8c6-4cff-9132-0f55f8d0c507",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTm8xTMLJcmkyEfAohf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de04a75c-022e-408a-9251-ce3ae168e4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012C931nz6haWF4pWP7Jms2H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 62247,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 62247,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1004,
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

_source line 113 · 2026-05-10T19:45:07.495Z_

<details><summary>↩ Tool result · `toolu_01AyWruvhr9dYAUwhYZLT9U7`</summary>

```text
Web search results for query: ""Adaptive Test-Time Compute" KV cache DMS NVIDIA reasoning 2025"

Links: [{"title":"Nvidia’s new technique cuts LLM reasoning costs by 8x without losing accuracy | VentureBeat","url":"https://venturebeat.com/orchestration/nvidias-new-technique-cuts-llm-reasoning-costs-by-8x-without-losing-accuracy"},{"title":"NVIDIA Dynamo, A Low-Latency Distributed Inference Framework for Scaling Reasoning AI Models | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"NVIDIA Researchers Introduce Dynamic Memory Sparsification (DMS) for 8× KV Cache Compression in Transformer LLMs - MarkTechPost","url":"https://www.marktechpost.com/2025/06/11/nvidia-researchers-introduce-dynamic-memory-sparsification-dms-for-8x-kv-cache-compression-in-transformer-llms/"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"KVzap: Fast, Adaptive, and Faithful KV Cache Pruning","url":"https://arxiv.org/html/2601.07891"},{"title":"Nvidia and its partners' KV Cache extenders","url":"https://www.blocksandfiles.com/ai-ml/2026/03/30/nvidia-and-its-partners-kv-cache-extenders/5209284"},{"title":"New memory structure helps AI models think longer and faster without using more power - The Brighter Side of News","url":"https://www.thebrighterside.news/post/new-memory-structure-helps-ai-models-think-longer-and-faster-without-using-more-power/"},{"title":"Optimizing Inference for Long Context and Large Batch Sizes with NVFP4 KV Cache | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/"},{"title":"Shrinking AI memory boosts accuracy, study finds","url":"https://techxplore.com/news/2025-12-ai-memory-boosts-accuracy.html"}]

Based on the search results, here's what I found about Adaptive Test-Time Compute, KV cache, DMS, NVIDIA reasoning in 2025:

## Dynamic Memory Sparsification (DMS)

Dynamic Memory Sparsification (DMS) compresses the key value (KV) cache, the temporary memory LLMs generate and store as they process prompts and reason through problems and documents. Nvidia's approach manages to discard much of the cache while maintaining (and in some cases improving) the model's reasoning capabilities.

### How DMS Works

DMS "retrofits" existing LLMs to intelligently manage their own memory by training the model to identify which tokens are essential for future reasoning and which are disposable. A key innovation is the "delayed eviction" mechanism: DMS mitigates this by flagging a token for eviction but keeping it accessible for a short window of time (e.g., a few hundred steps), allowing the model to "extract" any remaining necessary information from the token and merge it into the current context before the token is wiped from the KV cache.

### Performance and Benefits

Dynamic Memory Sparsification enables models to compress their memory by up to eight times while maintaining, or even improving, accuracy. Experiments show that DMS enables LLMs to "think" longer and explore more solutions without the usual penalty in speed or memory costs.

On reasoning benchmarks, on the AIME 24 math benchmark, a Qwen-R1 32B model equipped with DMS achieved a score 12.0 points higher than a standard model when constrained to the same memory bandwidth budget.

### Practical Implementation

A standard enterprise model like Qwen3-8B "can be retrofitted with DMS within hours on a single DGX H100."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de04a75c-022e-408a-9251-ce3ae168e4b3",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "85aeac12-9755-42fd-846e-ee74485acfb0",
  "sourceToolAssistantUUID": "de04a75c-022e-408a-9251-ce3ae168e4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-10T19:45:10.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTs5U4PuBf89XtY6gepgss`</summary>

```json
{
  "query": "\"TurboQuant\" Google DeepMind KV cache quantization compression 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85aeac12-9755-42fd-846e-ee74485acfb0",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTmv36yHvvVWJReP7wt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5470822e-fcd2-4a85-aeda-7d4de2ef7710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqB8PDfeGRdUQ7mhFLYeJz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 63251,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 63251,
          "cache_creation_input_tokens": 1147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1147,
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

_source line 115 · 2026-05-10T19:45:17.322Z_

<details><summary>↩ Tool result · `toolu_01KTs5U4PuBf89XtY6gepgss`</summary>

```text
Web search results for query: ""TurboQuant" Google DeepMind KV cache quantization compression 2026"

Links: [{"title":"GitHub - AmesianX/TurboQuant: TurboQuant KV Cache Compression for llama.cpp — 5.2x memory reduction with near-lossless quality | Implementation of Google DeepMind's TurboQuant (ICLR 2026)","url":"https://github.com/AmesianX/TurboQuant"},{"title":"TurboQuant: Redefining AI efficiency with extreme compression","url":"https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/"},{"title":"What Is Google TurboQuant? The KV Cache Compression That Crashed Memory Chip Stocks | MindStudio","url":"https://www.mindstudio.ai/blog/what-is-google-turboquant-kv-cache-compression"},{"title":"TurboQuant - Extreme KV Cache Quantization · ggml-org/llama.cpp · Discussion #20969","url":"https://github.com/ggml-org/llama.cpp/discussions/20969"},{"title":"TurboQuant.net - Independent TurboQuant Analysis","url":"https://turboquant.net/"},{"title":"KV Cache Is Eating Your VRAM. Here’s How Google Fixed It With TurboQuant. | Towards Data Science","url":"https://towardsdatascience.com/kv-cache-is-eating-your-vram-heres-how-google-fixed-it-with-turboquant/"},{"title":"Compress the KV Cache with TurboQuant and Haystack | Haystack","url":"https://haystack.deepset.ai/tutorials/49_turboquant_quantization_with_huggingface"},{"title":"TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate","url":"https://arxiv.org/html/2504.19874v1"},{"title":"Google’s TurboQuant Compression May Support Faster Inference, Same Accuracy on Less Capable Hardware - InfoQ","url":"https://www.infoq.com/news/2026/04/turboquant-compression-kv-cache/"},{"title":"TurboQuant: the new(?) and controversial ground breaking compression breakthrough from Google","url":"https://boringbot.substack.com/p/turboquant-the-new-and-controversial"}]

I found comprehensive information about TurboQuant. Here's what the search results reveal:

## Overview

TurboQuant is a compression algorithm presented at ICLR 2026 by Google DeepMind that optimally addresses the challenge of memory overhead in vector quantization.

## Key Capabilities

TurboQuant can quantize the key-value cache to just 3 bits without requiring training or fine-tuning and causing any compromise in model accuracy, all while achieving a faster runtime than the original LLMs (Gemma and Mistral). TurboQuant is a KV cache quantization algorithm from Google DeepMind that compresses cache storage from 16 bits to 3 bits with minimal accuracy loss.

## Performance Results

The improvements include 8x faster inference and 6x memory reduction on H100 GPUs. TurboQuant achieves perfect downstream results across all benchmarks while reducing the key value memory size by a factor of at least 6x.

## Technical Approach

TurboQuant works in two stages: PolarQuant - a random orthogonal rotation maps cache vectors to a more uniform distribution, then quantizes them in polar coordinates using Lloyd-Max optimal centroids. QJL (Quantized Johnson-Lindenstrauss) - a single extra bit per vector corrects residual errors in attention score computation, preserving accuracy at extreme compression ratios.

## Implementation Status

TurboQuant (ICLR 2026, Google DeepMind) achieves KV cache compression via Walsh-Hadamard Transform + Lloyd-Max quantization with QJL correction, with implementations available for production LLM inference engines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5470822e-fcd2-4a85-aeda-7d4de2ef7710",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "733875e4-3407-4973-b20d-7f057754c967",
  "sourceToolAssistantUUID": "5470822e-fcd2-4a85-aeda-7d4de2ef7710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-10T19:45:20.131Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X8M9HyHJEG1EfcMG55dPRy`</summary>

```json
{
  "query": "\"SPRINT\" interleaved planning parallelized execution reasoning models Google 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "733875e4-3407-4973-b20d-7f057754c967",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTneP3QDsiKHQYuq5uJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f47c8af-f30a-463b-8f9b-c576ee4f1848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014abv889dMgSatHm3MAtZPC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 64398,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1086
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 64398,
          "cache_creation_input_tokens": 1086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1086,
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

_source line 117 · 2026-05-10T19:45:27.109Z_

<details><summary>↩ Tool result · `toolu_01X8M9HyHJEG1EfcMG55dPRy`</summary>

```text
Web search results for query: ""SPRINT" interleaved planning parallelized execution reasoning models Google 2025"

Links: [{"title":"[2506.05745] SPRINT: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models","url":"https://arxiv.org/abs/2506.05745"},{"title":"SPRINT: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=h5YGwnMTke"},{"title":"NeurIPS Poster SPRINT: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models","url":"https://neurips.cc/virtual/2025/poster/116677"},{"title":"SPRINT: Enabling Interleaved Planning and Parallelized ...","url":"https://openreview.net/pdf?id=h5YGwnMTke"},{"title":"SPRINT: Enabling Interleaved Planning and Parallelized ...","url":"https://scalingintelligence.stanford.edu/pubs/sprint.pdf"},{"title":"Sprint: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models","url":"https://arxiv.org/html/2506.05745v2"},{"title":"SPRINT: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.05745v1"},{"title":"GitHub - ShayanTalaei/SPRINT","url":"https://github.com/ShayanTalaei/SPRINT"},{"title":"AI Papers on X: \"SPRINT: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models. https://t.co/3cdfaQCDu3\" / X","url":"https://x.com/SciFi/status/1932198152947335200"},{"title":"SPRINT: Enabling Interleaved Planning and Parallelized Execution in Reasoning Models | Scaling Intelligence Lab at Stanford University","url":"https://scalingintelligence.stanford.edu/pubs/sprint/"}]

I found comprehensive information about SPRINT. Here's what the research shows:

## SPRINT Overview

SPRINT is a novel post-training and inference-time framework designed to enable large reasoning models (LRMs) to dynamically identify and exploit opportunities for parallelization during their reasoning process, incorporating an innovative data curation pipeline that reorganizes natural language reasoning trajectories into structured rounds of long-horizon planning and parallel execution.

## Problem It Addresses

Large reasoning models excel at complex reasoning tasks but typically generate lengthy sequential chains-of-thought, resulting in long inference times before arriving at the final answer.

## How SPRINT Works

By fine-tuning LRMs on a small amount of such curated data, the models learn to dynamically identify independent subtasks within extended reasoning processes and effectively execute them in parallel. For inference, SPRINT introduces an orchestration of LRMs through two distinct roles: a planner and a pool of executors, where the planner generates a set of independent plans, and subsequently, multiple executors concurrently carry out these plans.

## Performance Results

Models fine-tuned with the SPRINT framework match the performance of reasoning models on complex domains such as mathematics while generating up to 39% fewer sequential tokens on problems requiring more than 8,000 output tokens. The framework achieves up to 45% and 65% reduction in average sequential tokens respectively on out-of-distribution tasks, namely GPQA and Countdown, for longer reasoning trajectories, while matching the performance of the fine-tuned reasoning model.

## Publication

The work was published as a conference paper at NeurIPS 2025, authored by Emil Biju, Shayan Talaei, Zhemin Huang, Mohammadreza Pourreza, Amin Saberi, and Azalia Mirhoseini.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f47c8af-f30a-463b-8f9b-c576ee4f1848",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "7c7f851a-5d8d-4dcd-95ab-bdca1f460f4c",
  "sourceToolAssistantUUID": "5f47c8af-f30a-463b-8f9b-c576ee4f1848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-10T19:45:29.230Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QehvpRxgk2BPiyQ9DqXP93`</summary>

```json
{
  "query": "\"ThinkPrune\" pruning long chain of thought reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c7f851a-5d8d-4dcd-95ab-bdca1f460f4c",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauToMuNk5DpJk989Z5VN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22e70fe9-7f42-42be-8eac-6692a6c37ec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155wSzJMu1491dSZM7FWpWa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 65484,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1023
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 65484,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1023,
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

_source line 119 · 2026-05-10T19:45:36.091Z_

<details><summary>↩ Tool result · `toolu_01QehvpRxgk2BPiyQ9DqXP93`</summary>

```text
Web search results for query: ""ThinkPrune" pruning long chain of thought reinforcement learning 2025"

Links: [{"title":"[2504.01296] ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2504.01296"},{"title":"ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2504.01296v1"},{"title":"GitHub - UCSB-NLP-Chang/ThinkPrune","url":"https://github.com/UCSB-NLP-Chang/ThinkPrune"},{"title":"ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=V51gPu1uQD"},{"title":"[PDF] ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ThinkPrune:-Pruning-Long-Chain-of-Thought-of-LLMs-Hou-Zhang/9b487024ccc5c575a6d72a597ad65f92cce79a04"},{"title":"ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.01296"},{"title":"Inference-Time Chain-of-Thought Pruning with Latent Informativeness Signals","url":"https://arxiv.org/pdf/2511.00699"},{"title":"ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/thinkprune-pruning-long-chain-thought-llms-via"},{"title":"ThinkPrune - a Shiyu-Lab Collection","url":"https://huggingface.co/collections/Shiyu-Lab/thinkprune-67f550c57f5baf0521403881"},{"title":"dblp: ThinkPrune: Pruning Long Chain-of-Thought of LLMs via Reinforcement Learning.","url":"https://dblp.org/rec/journals/corr/abs-2504-01296.html"}]

Based on the search results, here's what I found about ThinkPrune:

## Overview

ThinkPrune is a simple yet effective method for pruning the thinking length for long-thinking LLMs, which has been found to often produce inefficient and redundant thinking processes.

## How It Works

ThinkPrune continuously trains the long-thinking LLMs via reinforcement learning (RL) with an added token limit, beyond which any unfinished thoughts and answers will be discarded, resulting in a zero reward. To further preserve model performance, ThinkPrune introduces an iterative length pruning approach, where multiple rounds of RL are conducted, each with an increasingly more stringent token limit.

## Key Results

On the AIME24 dataset, the reasoning length of DeepSeek-R1-Distill-Qwen-1.5B can be reduced by half with only 2% drop in performance. After pruning, the LLMs can bypass unnecessary steps while keeping the core reasoning process complete.

## Background Problem

Existing preliminary explorations of reducing thinking length primarily focus on forcing the thinking process to early exit, rather than adapting the LLM to optimize and consolidate the thinking process, and therefore the length-performance tradeoff observed so far is sub-optimal.

## Authors and Availability

The paper was published on April 2, 2025, by Bairu Hou, Yang Zhang, Jiabao Ji, Yujian Liu, Kaizhi Qian, Jacob Andreas, and Shiyu Chang. Code is available at https://github.com/UCSB-NLP-Chang/ThinkPrune.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22e70fe9-7f42-42be-8eac-6692a6c37ec7",
  "isSidechain": true,
  "promptId": "e8351d93-61fd-4673-ac5e-03fe84eeabea",
  "agentId": "af3b761bcbdccae6c",
  "type": "user",
  "uuid": "f5d6bb72-c704-44cc-be4a-16bb474acc42",
  "sourceToolAssistantUUID": "22e70fe9-7f42-42be-8eac-6692a6c37ec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 120 · 2026-05-10T19:47:29.618Z_

Now I have gathered extensive information. Let me compile the findings into a comprehensive report.

---

## Concurrent/Recent Work Review: Phase-Aware Compound Sparsity

Below are the most relevant papers and systems found from 2025-2026 that appear NOT to be in the paper's already-cited list. I have organized them by relevance tier.

---

### TIER 1: HIGHLY RELEVANT -- Should almost certainly be cited

These works directly address the intersection of compound compression, phase/reasoning-aware sparsity, or joint multi-axis optimization for LLM inference.

**1. DeepSeek-V4: Compressed Sparse Attention + Heavily Compressed Attention (April 2026)**
- Venue: Industry release (DeepSeek)
- DeepSeek-V4 combines two attention mechanisms -- CSA (4x KV compression + sparse top-k selection) and HCA (128x compression with dense attention over compressed blocks) -- achieving 10% KV cache and 27% FLOPs vs. V3.2 at 1M tokens. This is a deployed compound compression system coordinating multiple compression axes (KV compression ratio, sparse selection, dense fallback) -- directly relevant as a production counterpoint to the paper's proposal.
- Source: [MarkTechPost](https://www.marktechpost.com/2026/04/24/deepseek-ai-releases-deepseek-v4-compressed-sparse-attention-and-heavily-compressed-attention-enable-one-million-token-contexts/)

**2. DeepSeek Engram: Conditional Memory as a New Sparsity Axis (January 2026)**
- Venue: arXiv (DeepSeek-AI), arxiv:2601.07372
- Introduces conditional memory (O(1) lookup) as a complementary axis to MoE's conditional computation. Discovers a U-shaped scaling law for optimal allocation between the two sparsity axes. Directly relevant as a "compound sparsity" approach with a principled allocation framework.
- Source: [arXiv](https://arxiv.org/abs/2601.07372)

**3. Dynamic Memory Sparsification (DMS) / Inference-Time Hyper-Scaling (NeurIPS 2025, NVIDIA)**
- Venue: NeurIPS 2025
- DMS trains models to learn which KV entries to evict, achieving 8x KV cache compression. The "hyper-scaling" insight is that compressing KV cache lets you generate more reasoning tokens within the same memory budget, improving accuracy. On AIME24, Qwen-R1 32B + DMS gains +9.1 points. This directly relates to the paper's thesis that adaptive KV cache compression during reasoning can improve efficiency without sacrificing quality.
- Source: [arXiv](https://arxiv.org/abs/2506.05345)

**4. ForesightKV: Learned KV Cache Eviction for Reasoning Models (February 2026)**
- Venue: Under review (submitted Feb 2026)
- Uses RL (GRPO) to learn eviction policies for reasoning models, formulating cache eviction as an MDP. Trained and evaluated on AIME2024/2025 with Qwen3. Directly relevant as a learned, phase-aware cache management approach for reasoning.
- Source: [OpenReview](https://openreview.net/forum?id=k5h29Qv7GN)

**5. Neural Garbage Collection: Learning to Forget while Learning to Reason (April 2026)**
- Venue: arXiv, arxiv:2604.18002
- Trains a model to jointly reason and decide when to evict KV cache entries, using RL with outcome-based reward. Achieves 2-3x peak KV cache compression on reasoning tasks. The model learns memory management behavior entirely from task reward -- a strong conceptual parallel to the paper's phase-aware controller.
- Source: [arXiv](https://arxiv.org/abs/2604.18002)

**6. DynTS: Dynamic Thinking-Token Selection (January 2026)**
- Venue: arXiv, arxiv:2601.18383
- Exploits observed sparsity of "thinking tokens" in reasoning models (Pareto principle). Uses an Importance Predictor to dynamically estimate thinking-token importance and evict KV cache entries for redundant tokens, achieving 3.3-5.7x KV reduction without accuracy loss. Highly relevant as a phase-aware, reasoning-specific KV compression method.
- Source: [arXiv](https://arxiv.org/abs/2601.18383)

**7. Reasoning-Aware Compression (RAC) / "Reasoning Models Can Be Accurately Pruned" (NeurIPS 2025)**
- Venue: NeurIPS 2025
- Shows that standard pruning degrades reasoning models far more than instruction models, and that calibrating on on-policy CoT traces (RAC) preserves up to 95% accuracy at 50% sparsity. Directly relevant: the paper's phase-aware approach should cite this as motivation for why reasoning-specific sparsity calibration is essential.
- Source: [arXiv](https://arxiv.org/abs/2509.12464)

**8. From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models (January 2026)**
- Venue: arXiv, arxiv:2601.18091
- First systematic study comparing pruning behavior between instruction-following LLMs and reasoning-augmented models (LLM-think). Evaluates static depth, width, and dynamic pruning across 17 tasks. Directly relevant as it establishes that pruning strategies must differ for reasoning models.
- Source: [arXiv](https://arxiv.org/abs/2601.18091)

**9. KVTC: KV Cache Transform Coding (ICLR 2026, NVIDIA)**
- Venue: ICLR 2026
- Applies image/video compression principles (PCA + adaptive quantization + entropy coding) to KV cache, achieving 20-40x compression with maintained accuracy. This is a different compression axis (transform coding) that could be composed with the paper's approach.
- Source: [arXiv](https://arxiv.org/abs/2511.01815)

**10. Spark Transformer: Reactivating Sparsity in FFN and Attention (NeurIPS 2025, Google DeepMind)**
- Venue: NeurIPS 2025
- Achieves compound sparsity across both FFN (8% activation) and attention (max 256 tokens per query) simultaneously, with 2.5x FLOP reduction and 1.4-1.8x wall-time speedups. Uses statistical top-k for hardware efficiency. Directly relevant as a multi-axis sparsity approach within a single architecture.
- Source: [arXiv](https://arxiv.org/abs/2506.06644)

---

### TIER 2: STRONGLY RELEVANT -- Should likely be cited

**11. SparseSpec: Sparse Self-Speculative Decoding with PillarAttn (December 2025)**
- Venue: arXiv, arxiv:2512.01278
- Lossless, training-free acceleration for reasoning models using sparse attention (PillarAttn) for draft generation. Achieves 2.13x throughput improvement. Relevant as an alternative approach to efficient reasoning model inference that exploits attention sparsity.
- Source: [arXiv](https://arxiv.org/abs/2512.01278)

**12. DECS: Overthinking Reduction with Decoupled Rewards (ICLR 2026 Oral)**
- Venue: ICLR 2026 (Oral)
- Reduces reasoning tokens by 50%+ via a decoupled token-level reward mechanism that distinguishes essential from redundant reasoning tokens. Uses curriculum batch scheduling. Relevant as a complementary approach to compute reduction during reasoning phases.
- Source: [arXiv](https://arxiv.org/abs/2509.25827)

**13. TurboQuant: KV Cache Quantization to 3 bits (ICLR 2026, Google DeepMind)**
- Venue: ICLR 2026
- Achieves 6x KV cache memory reduction and 8x faster inference via Walsh-Hadamard rotation + Lloyd-Max quantization at 3 bits. This quantization approach is orthogonal to (and composable with) sparsity-based methods.
- Source: [Google Research Blog](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

**14. Native Sparse Attention (NSA) (ACL 2025 Best Paper, DeepSeek)**
- Venue: ACL 2025 (Best Paper)
- Hardware-aligned trainable sparse attention with hierarchical strategy (coarse compression + fine selection + sliding window). Foundation for DeepSeek V3.2 DSA and V4 CSA. Important as the architectural basis for recent deployed sparse attention systems.
- Source: [arXiv](https://arxiv.org/abs/2502.11089)

**15. R-Sparse: Rank-Aware Activation Sparsity (ICLR 2025)**
- Venue: ICLR 2025
- Training-free method achieving 50% model-level sparsity by exploiting the rank structure of activations rather than predicting active channels. 43% end-to-end speedup. Relevant as a complementary MLP sparsity technique.
- Source: [arXiv](https://arxiv.org/abs/2504.19449)

**16. Sparsing Law (ICML 2025)**
- Venue: ICML 2025
- Identifies quantitative scaling laws for activation sparsity: ReLU models get sparser with more data while SiLU models get less sparse. Architecture depth matters. Demonstrates a 2.4B model at 93.5% sparsity with 4.1x speedup. Provides theoretical grounding for MLP sparsity levels.
- Source: [arXiv](https://arxiv.org/abs/2411.02335)

**17. ParoQuant: Pairwise Rotation Quantization for Reasoning LLMs (ICLR 2026)**
- Venue: ICLR 2026
- PTQ method specifically designed for reasoning LLMs where quantization errors accumulate over long CoT. 2.4% accuracy improvement over AWQ on reasoning tasks. Relevant as a quantization method aware of reasoning-specific challenges.
- Source: [arXiv](https://arxiv.org/abs/2511.10645)

**18. Optimal Sparsity of MoE for Reasoning Tasks (2025)**
- Venue: arXiv, arxiv:2508.18672
- Discovers that increasing MoE sparsity helps memorization but saturates for reasoning. Optimal sparsity must be determined jointly by active FLOPs and tokens-per-parameter. Relevant for understanding how sparsity allocation should differ for reasoning workloads.
- Source: [arXiv](https://arxiv.org/abs/2508.18672)

**19. XAttention: Block Sparse Attention with Antidiagonal Scoring (ICML 2025, MIT Han Lab)**
- Venue: ICML 2025
- Plug-and-play framework achieving 13.5x attention speedup via antidiagonal scoring for block importance. Relevant as a hardware-efficient sparse attention primitive that could serve as a building block.
- Source: [arXiv](https://arxiv.org/abs/2503.16428)

**20. SpargeAttention (ICML 2025, Tsinghua)**
- Venue: ICML 2025
- Training-free sparse attention with two-stage online filtering, achieving 2.5-5x speedup across language, image, and video models. Relevant as a universal sparse attention acceleration method.
- Source: [arXiv](https://arxiv.org/abs/2502.18137)

---

### TIER 3: RELEVANT CONTEXT -- Consider citing

**21. Sparser, Faster, Lighter Transformer LMs with TwELL (ICML 2026, Sakana AI + NVIDIA)**
- Venue: ICML 2026
- New sparse packing format (TwELL) enabling 20%+ speedups with custom CUDA kernels for H100. Relevant for hardware-level realization of sparsity.
- Source: [GitHub](https://github.com/SakanaAI/sparser-faster-llms)

**22. Hold Onto That Thought (NeurIPS 2025 Workshop)**
- Benchmarks KV cache compression strategies on reasoning vs. non-reasoning models. Finds H2O and SnapKV variants dominate for reasoning traces. Relevant for empirical grounding of KV compression choices.
- Source: [arXiv](https://arxiv.org/abs/2512.12008)

**23. CoLaR: Think Silently, Think Fast (NeurIPS 2025, Xiaomi)**
- Compresses reasoning chains into latent space, reducing chain length by 53-83%. Relevant as an alternative approach to reasoning efficiency via latent compression rather than token-level sparsity.
- Source: [arXiv](https://arxiv.org/abs/2505.16552)

**24. UniComp: Unified Evaluation of LLM Compression (February 2026)**
- Framework comparing pruning, quantization, and distillation across 40+ datasets. Finds compression exhibits "knowledge bias" -- reasoning degrades more than knowledge tasks. Relevant for understanding compound compression tradeoffs.
- Source: [arXiv](https://arxiv.org/abs/2602.09130)

**25. DefensiveKV (ICLR 2026)**
- Exposes fragility in KV cache eviction stability assumptions and proposes defensive aggregation, reducing quality loss by 4.3x. Relevant for robustness of KV cache management.
- Source: [arXiv](https://arxiv.org/abs/2510.13334)

**26. LookaheadKV (ICLR 2026, Samsung)**
- Predicts future attention patterns for KV eviction with parameter-efficient modules, reducing eviction cost by 14.5x. Relevant as a learned KV eviction approach.
- Source: [arXiv](https://arxiv.org/abs/2603.10899)

**27. LSA: Layer-wise Sparsity Allocation (ICLR 2026)**
- Allocates non-uniform sparsity across layers based on minimal linear reconstruction error. At 70% sparsity, surpasses SOTA. Relevant for the paper's per-layer sparsity allocation decisions.
- Source: [OpenReview](https://openreview.net/forum?id=xq3lza5IjN)

**28. GETA/QASSO: Joint Structured Pruning and Quantization (CVPR 2025)**
- First white-box joint optimizer explicitly controlling both sparsity ratio and bit width. Relevant as a principled compound compression optimizer.
- Source: [arXiv](https://arxiv.org/abs/2502.16638)

**29. SVD Contextual Sparsity Predictors (March 2026)**
- Training-free sparsity prediction using truncated SVD of gate projections, with theoretical guarantees. 1.8x speedup at 90% FFN sparsity. Relevant as an alternative MLP sparsity prediction mechanism.
- Source: [arXiv](https://arxiv.org/abs/2603.14110)

**30. Adaptive Parallel Reasoning (Berkeley, May 2026)**
- Teaches models to dynamically choose between sequential and parallel reasoning via spawn/join operations. Relevant as a complementary approach to adaptive inference compute allocation.
- Source: [BAIR Blog](https://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)

**31. SPRINT: Interleaved Planning and Parallelized Execution (NeurIPS 2025, Stanford)**
- Restructures reasoning into parallel-executable subtasks, reducing sequential tokens by 39-65%. Relevant as another approach to reducing reasoning inference cost.
- Source: [arXiv](https://arxiv.org/abs/2506.05745)

**32. ThinkPrune: Pruning Long CoT via RL (April 2025)**
- Uses RL with iterative length pruning to reduce thinking length by 50% with 2% accuracy drop. Relevant as a reasoning-token-level compression approach.
- Source: [arXiv](https://arxiv.org/abs/2504.01296)

**33. VideoNSA (ICLR 2026)**
- Adapts NSA to video-language models with dynamic gating across compression/selection/sliding-window branches, using only 3.6% attention budget at 128K tokens. Relevant as a multi-branch sparse attention system with learned gating.
- Source: [arXiv](https://arxiv.org/abs/2510.02295)

**34. Masked Gated Linear Unit / MGLU (June 2025)**
- Novel GLU variant that reduces memory transfer in FFN layers by 47% via learned binary masks. Relevant as an MLP efficiency technique.
- Source: [arXiv](https://arxiv.org/abs/2506.23225)

**35. CapKV: Information-Theoretic KV Cache Eviction (April 2026)**
- Derives KV eviction from the Information Bottleneck principle using log-determinant leverage scores. Relevant for principled cache management.
- Source: [arXiv](https://arxiv.org/abs/2604.25975)

---

### Summary of Key Gaps

The most critical missing citations fall into three categories:

1. **Deployed compound sparsity systems**: DeepSeek-V4 (CSA+HCA) and Engram represent real, deployed multi-axis compression systems that the paper should discuss as concurrent industry work.

2. **Learned/RL-based reasoning-aware cache management**: Neural Garbage Collection, ForesightKV, and DynTS all train models to manage their own KV cache during reasoning, which is conceptually very close to the paper's phase-aware controller.

3. **Reasoning-specific pruning/compression**: RAC, "From LLMs to LRMs", and DECS establish that compression strategies must be fundamentally different for reasoning models -- the core premise of the paper -- and provide important empirical baselines.

The paper should also acknowledge the broader trend: the Spark Transformer (Google), NSA/DSA (DeepSeek), and KVTC (NVIDIA) demonstrate that multi-axis sparse attention with learned gating is rapidly being adopted in production systems, which strengthens the paper's motivation but also raises the bar for novelty.

Sources:
- [DeepSeek V4 - MarkTechPost](https://www.marktechpost.com/2026/04/24/deepseek-ai-releases-deepseek-v4-compressed-sparse-attention-and-heavily-compressed-attention-enable-one-million-token-contexts/)
- [Engram - arXiv](https://arxiv.org/abs/2601.07372)
- [DMS / Hyper-Scaling - arXiv](https://arxiv.org/abs/2506.05345)
- [ForesightKV - OpenReview](https://openreview.net/forum?id=k5h29Qv7GN)
- [Neural Garbage Collection - arXiv](https://arxiv.org/abs/2604.18002)
- [DynTS - arXiv](https://arxiv.org/abs/2601.18383)
- [RAC - arXiv](https://arxiv.org/abs/2509.12464)
- [From LLMs to LRMs - arXiv](https://arxiv.org/abs/2601.18091)
- [KVTC - arXiv](https://arxiv.org/abs/2511.01815)
- [Spark Transformer - arXiv](https://arxiv.org/abs/2506.06644)
- [SparseSpec - arXiv](https://arxiv.org/abs/2512.01278)
- [DECS - arXiv](https://arxiv.org/abs/2509.25827)
- [TurboQuant - Google Research](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)
- [NSA - arXiv](https://arxiv.org/abs/2502.11089)
- [R-Sparse - arXiv](https://arxiv.org/abs/2504.19449)
- [Sparsing Law - arXiv](https://arxiv.org/abs/2411.02335)
- [ParoQuant - arXiv](https://arxiv.org/abs/2511.10645)
- [Optimal MoE Sparsity - arXiv](https://arxiv.org/abs/2508.18672)
- [XAttention - arXiv](https://arxiv.org/abs/2503.16428)
- [SpargeAttention - arXiv](https://arxiv.org/abs/2502.18137)
- [TwELL/Sparser-Faster-Lighter - GitHub](https://github.com/SakanaAI/sparser-faster-llms)
- [Hold Onto That Thought - arXiv](https://arxiv.org/abs/2512.12008)
- [CoLaR - arXiv](https://arxiv.org/abs/2505.16552)
- [UniComp - arXiv](https://arxiv.org/abs/2602.09130)
- [DefensiveKV - arXiv](https://arxiv.org/abs/2510.13334)
- [LookaheadKV - arXiv](https://arxiv.org/abs/2603.10899)
- [LSA - OpenReview](https://openreview.net/forum?id=xq3lza5IjN)
- [GETA/QASSO - arXiv](https://arxiv.org/abs/2502.16638)
- [SVD Contextual Sparsity - arXiv](https://arxiv.org/abs/2603.14110)
- [Adaptive Parallel Reasoning - BAIR](https://bair.berkeley.edu/blog/2026/05/08/adaptive-parallel-reasoning/)
- [SPRINT - arXiv](https://arxiv.org/abs/2506.05745)
- [ThinkPrune - arXiv](https://arxiv.org/abs/2504.01296)
- [VideoNSA - arXiv](https://arxiv.org/abs/2510.02295)
- [MGLU - arXiv](https://arxiv.org/abs/2506.23225)
- [CapKV - arXiv](https://arxiv.org/abs/2604.25975)
- [From LLMs to LRMs - OpenReview](https://openreview.net/forum?id=eHHQEsphbN)
- [DeepSeek V3.2 DSA - arXiv](https://arxiv.org/abs/2512.02556)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5d6bb72-c704-44cc-be4a-16bb474acc42",
  "isSidechain": true,
  "agentId": "af3b761bcbdccae6c",
  "requestId": "req_011CauTp2KgWHnR61WS3wEFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4e82d87-799c-4ae9-8179-3c9f4dd17ed0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8009ef9d-2f40-4a1d-9755-86a766eaf91b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjWwYUJmZabgPFdT31gVsm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 66507,
      "output_tokens": 5699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1205
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5699,
          "cache_read_input_tokens": 66507,
          "cache_creation_input_tokens": 1205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1205,
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
