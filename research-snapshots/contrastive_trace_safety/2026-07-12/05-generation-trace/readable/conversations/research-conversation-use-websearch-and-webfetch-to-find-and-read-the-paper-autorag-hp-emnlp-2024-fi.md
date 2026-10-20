# Research conversation: Use WebSearch and WebFetch to find and read the paper "AutoRAG-HP" (EMNLP 2024 Findings, arXiv 2406.19251). I need: 1. T

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a574fd1e405cf0bb5.jsonl`
- **Structured JSON:** [`309cd8691b023a1da646.json`](../../sessions/30/309cd8691b023a1da646.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-12T00:08:07.373Z_

Use WebSearch and WebFetch to find and read the paper "AutoRAG-HP" (EMNLP 2024 Findings, arXiv 2406.19251). I need:
1. The full title and authors
2. The core method: how does it formulate RAG hyperparameter tuning as a multi-armed bandit?
3. What specific hyperparameters does it tune? (top-k, compression ratio, embedding methods, etc.)
4. Is it online or offline? Per-query or global?
5. Key results and benchmarks
6. How does it differ from routing discrete structural program abstractions (file/function/line) for code repair?

Report in under 300 words with exact details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "915c6a0b-1009-439d-bb6c-b8a27bfd43f0",
  "agentId": "a574fd1e405cf0bb5",
  "type": "user",
  "uuid": "6353d398-4589-406d-9f12-546b09cbfc1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:08:07.378Z_

```json
{
  "parentUuid": "6353d398-4589-406d-9f12-546b09cbfc1c",
  "isSidechain": true,
  "agentId": "a574fd1e405cf0bb5",
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
  "uuid": "f25d84e5-75ec-4467-9e4f-6f07a1897845",
  "timestamp": "2026-05-12T00:08:07.378Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:08:09.296Z_



Let me search for and fetch this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f25d84e5-75ec-4467-9e4f-6f07a1897845",
  "isSidechain": true,
  "agentId": "a574fd1e405cf0bb5",
  "requestId": "req_011Cawhe2xVH33aXk736gJE8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97c2b466-0061-4d82-8989-3d19a7c88a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHQbaJHYwRWmi3g66Rv2JA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7991,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7991,
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

_source line 4 · 2026-05-12T00:08:09.770Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019hRk9xzkYYg8kGuQbeZAPh`</summary>

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
  "parentUuid": "97c2b466-0061-4d82-8989-3d19a7c88a5d",
  "isSidechain": true,
  "agentId": "a574fd1e405cf0bb5",
  "requestId": "req_011Cawhe2xVH33aXk736gJE8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eee89698-23ef-408b-9a31-5fe794717c81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHQbaJHYwRWmi3g66Rv2JA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7991,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7991,
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

_source line 5 · 2026-05-12T00:08:09.774Z_

<details><summary>↩ Tool result · `toolu_019hRk9xzkYYg8kGuQbeZAPh`</summary>

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
  "parentUuid": "eee89698-23ef-408b-9a31-5fe794717c81",
  "isSidechain": true,
  "promptId": "915c6a0b-1009-439d-bb6c-b8a27bfd43f0",
  "agentId": "a574fd1e405cf0bb5",
  "type": "user",
  "uuid": "a90df5bc-b473-473f-b530-4a4f134b47ef",
  "sourceToolAssistantUUID": "eee89698-23ef-408b-9a31-5fe794717c81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-12T00:08:14.289Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XRq8sJBZ828WgeSvdahqtd`</summary>

```json
{
  "query": "AutoRAG-HP EMNLP 2024 arXiv 2406.19251 multi-armed bandit RAG hyperparameter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a90df5bc-b473-473f-b530-4a4f134b47ef",
  "isSidechain": true,
  "agentId": "a574fd1e405cf0bb5",
  "requestId": "req_011CawheDsZmnP9AJ1ZtHD5i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db44d5f7-c43a-4148-9d9d-7b3dc0987ac1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2U2Dy44sjLkk7w8sqamKw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 7991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1899,
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

_source line 7 · 2026-05-12T00:08:15.012Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0178Lu2nA28LCu8Y1QozTx5V`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.19251",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db44d5f7-c43a-4148-9d9d-7b3dc0987ac1",
  "isSidechain": true,
  "agentId": "a574fd1e405cf0bb5",
  "requestId": "req_011CawheDsZmnP9AJ1ZtHD5i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd98f82e-acc7-453c-8b53-2c3be4902a44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2U2Dy44sjLkk7w8sqamKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 7991,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1899
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 7991,
          "cache_creation_input_tokens": 1899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1899,
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

_source line 8 · 2026-05-12T00:08:20.264Z_

<details><summary>↩ Tool result · `toolu_0178Lu2nA28LCu8Y1QozTx5V`</summary>

```text
# Paper Summary

**Full Title:**
"AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation"

**Authors:**
Jia Fu, Xiaoting Qin, Fangkai Yang, Lu Wang, Jue Zhang, Qingwei Lin, Yubo Chen, Dongmei Zhang, Saravan Rajmohan, and Qi Zhang

**Complete Abstract:**
The authors propose a framework addressing optimization challenges in RAG systems. They present that "Recent advancements in Large Language Models have transformed ML/AI development, necessitating a reevaluation of AutoML principles for the Retrieval-Augmented Generation (RAG) systems." The work formulates hyperparameter tuning as an online multi-armed bandit problem and introduces a "novel two-level Hierarchical MAB (Hier-MAB) method for efficient exploration of large search spaces." Testing on ALCE-ASQA and Natural Questions datasets showed their approach achieved strong recall metrics "using only ~20% of the LLM API calls required by the Grid Search approach" when optimizing parameters like document retrieval count, prompt compression, and embedding methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd98f82e-acc7-453c-8b53-2c3be4902a44",
  "isSidechain": true,
  "promptId": "915c6a0b-1009-439d-bb6c-b8a27bfd43f0",
  "agentId": "a574fd1e405cf0bb5",
  "type": "user",
  "uuid": "893f89ec-7cfa-4a74-9b67-29d1c14a4acc",
  "sourceToolAssistantUUID": "cd98f82e-acc7-453c-8b53-2c3be4902a44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T00:08:21.164Z_

<details><summary>↩ Tool result · `toolu_01XRq8sJBZ828WgeSvdahqtd`</summary>

```text
Web search results for query: "AutoRAG-HP EMNLP 2024 arXiv 2406.19251 multi-armed bandit RAG hyperparameter"

Links: [{"title":"[2406.19251] AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2406.19251"},{"title":"[PDF] AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AutoRAG-HP:-Automatic-Online-Hyper-Parameter-Tuning-Fu-Qin/758881985475e137439da465fadf968aead68c4c"},{"title":"AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2406.19251"},{"title":"EMNLP 2024 Paraphrase Types Elicit Prompt Engineering ...","url":"https://arxiv.org/html/2406.19898v3"},{"title":"AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.223/"},{"title":"A Component-Based Survey of Interactions between Large Language Models and Multi-Armed Bandits","url":"https://arxiv.org/html/2601.12945v2"},{"title":"AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation | Request PDF","url":"https://www.researchgate.net/publication/381770940_AutoRAG-HP_Automatic_Online_Hyper-Parameter_Tuning_for_Retrieval-Augmented_Generation"},{"title":"Large Language Model-Enhanced Multi-Armed Bandits","url":"https://arxiv.org/html/2502.01118v1"},{"title":"Multi-Armed Bandits Meet Large Language Models","url":"https://arxiv.org/html/2505.13355v1"},{"title":"[1904.10040] A Survey on Practical Applications of Multi-Armed and Contextual Bandits","url":"https://arxiv.org/abs/1904.10040"}]

Based on the search results, here's the information about AutoRAG-HP:

## AutoRAG-HP Overview

AutoRAG-HP is a framework that formulates hyper-parameter tuning as an online multi-armed bandit (MAB) problem and introduces a novel two-level Hierarchical MAB (Hier-MAB) method for efficient exploration of large search spaces.

## Key Details

**Paper Information:**
- The paper was published in Findings of the Association for Computational Linguistics: EMNLP 2024
- arXiv ID: 2406.19251
- Submitted on June 27, 2024

**Authors:** Jia Fu, Xiaoting Qin, Fangkai Yang, Lu Wang, Jue Zhang, Qingwei Lin, Yubo Chen, Dongmei Zhang, Saravan Rajmohan, and Qi Zhang

## Technical Approach

The framework uses a two-level Hierarchical MAB method, wherein a high-level MAB guides the optimization of modules, while several low-level MABs search for optimal settings within each module.

## Experimental Results

The research involved tuning hyper-parameters such as top-k retrieved documents, prompt compression ratio, and embedding methods, using the ALCE-ASQA and Natural Questions datasets. Experimental evaluation showed that MAB-based online learning methods can achieve Recall@5 ≈ 0.8 for scenarios with prominent gradients in search space, using only ~20% of the LLM API calls required by the Grid Search approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db44d5f7-c43a-4148-9d9d-7b3dc0987ac1",
  "isSidechain": true,
  "promptId": "915c6a0b-1009-439d-bb6c-b8a27bfd43f0",
  "agentId": "a574fd1e405cf0bb5",
  "type": "user",
  "uuid": "6ff33248-c484-498a-bb1f-cf7ec7a1eaee",
  "sourceToolAssistantUUID": "db44d5f7-c43a-4148-9d9d-7b3dc0987ac1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-12T00:08:29.724Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013jekjNioxFuEAa7do3pwQi`</summary>

```json
{
  "url": "https://arxiv.org/html/2406.19251",
  "prompt": "Extract detailed information about: 1) How the multi-armed bandit formulation works (each arm = what? reward signal = what?). 2) The exact hyperparameters tuned (top-k values, compression ratios, embedding methods - list all specific values). 3) Is it online or offline? Per-query or global? 4) The Hier-MAB two-level structure details. 5) Key quantitative results and baselines compared. 6) Which MAB algorithms are used (UCB, Thompson Sampling, etc)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff33248-c484-498a-bb1f-cf7ec7a1eaee",
  "isSidechain": true,
  "agentId": "a574fd1e405cf0bb5",
  "requestId": "req_011Cawhf3wJN2dzi8dihaBhE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d72c9292-1825-4752-ab37-b4a459e9f089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoyV5QnGbN5uQk6DEVdy6p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 297,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 9890,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1162
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 297,
          "output_tokens": 202,
          "cache_read_input_tokens": 9890,
          "cache_creation_input_tokens": 1162,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1162,
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

_source line 11 · 2026-05-12T00:08:42.623Z_

<details><summary>↩ Tool result · `toolu_013jekjNioxFuEAa7do3pwQi`</summary>

```text
# AutoRAG-HP: Multi-Armed Bandit Hyper-Parameter Tuning

## 1) Multi-Armed Bandit Formulation

**Arms:** Each arm represents either a single hyper-parameter value (e.g., top-k=3) or a combination of hyper-parameter settings when jointly optimizing multiple parameters.

**Reward Signal:** A linear combination balancing response accuracy and token cost:
- Reward = w·accuracy − (1−w)·(tokens/max_tokens)
- The weight parameter w ∈ {0.1, 0.5, 0.9} allows tuning between cost-central, balanced, and accuracy-central optimization modes
- Inaccurate responses receive a penalty of -1

## 2) Exact Hyperparameters Tuned

The paper evaluates two optimization scenarios:

**Two-parameter optimization:**
- Top-k (𝒦): [1, 3, 5, 7, 9]
- Compression ratio (𝒞): [0.3, 0.5, 0.7, 0.9, 1]
- Embedding fixed to "mpnet"

**Three-parameter optimization:**
- Top-k and compression ratio (same values as above)
- Embedding model (ℰ): ["mpnet", "ada_002", "contriever"]

## 3) Online vs. Offline + Query Scope

**Online learning:** The framework operates in an online fashion, receiving feedback from user interactions (e.g., thumb up/down ratings) to continuously adapt hyper-parameters.

**Per-query or global:** The approach is global—it optimizes across batches of B=4 queries per trial to reduce variance, testing combinations on multiple questions from the dataset.

## 4) Hier-MAB Two-Level Structure

The hierarchical design addresses the combinatorial explosion of jointly tuning multiple parameters:

- **High-level MAB:** Selects which hyper-parameter to tune in each trial
- **Low-level MABs:** For each hyper-parameter, a separate MAB selects its specific value

Example: When tuning (top-k, compression, embedding), the system has 4 MABs total—one high-level arm selector plus three low-level arms (one per parameter). This avoids flattening the search space, which would require evaluating all possible combinations simultaneously.

After pulling arms and observing rewards, both high-level and low-level arm distributions update to reflect performance.

## 5) Key Quantitative Results

**Efficiency:** "MAB-based online learning methods can achieve Recall@5 ≈0.8 for scenarios with prominent gradients in search space, using only ∼20% of the LLM API calls required by Grid Search."

**Task complexity classification:**
- Easy scenarios: Recall@x ≈ 0.8
- Medium scenarios: Recall@x ≈ 0.5
- Hard scenarios: Recall@x ≲ 0.3

**Hier-UCB performance:** Consistently outperforms baselines (standard UCB, Thompson Sampling, Random Search) in "Medium" complexity cases with faster convergence.

**Datasets:** ALCE-ASQA and Natural Questions (350 questions each)

**Base LLMs:** GPT-3.5-Turbo and GPT-4

## 6) MAB Algorithms Used

**Primary algorithm:** Upper Confidence Bound (UCB)
- Selection formula: A_t = argmax(Q_t(a) + α√(ln(t)/N_a(t)))
- Q_t(a) = estimated arm value; N_a(t) = selection count
- Parameter α balances exploration vs. exploitation (set to 1 in main experiments)

**Secondary baseline:** Thompson Sampling
- Samples arms from posterior reward distributions

**Comparison baseline:** Random Search (uniform random arm selection)

**Hier-MAB variant:** Hier-UCB uses separate α parameters for high-level (α^h) and low-level (α^l) selections; ablation studies found α^h=1.5, α^l=0.5 optimal for some scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d72c9292-1825-4752-ab37-b4a459e9f089",
  "isSidechain": true,
  "promptId": "915c6a0b-1009-439d-bb6c-b8a27bfd43f0",
  "agentId": "a574fd1e405cf0bb5",
  "type": "user",
  "uuid": "10189c7b-1cec-4964-b075-4012856870ec",
  "sourceToolAssistantUUID": "d72c9292-1825-4752-ab37-b4a459e9f089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-12T00:09:02.438Z_

Here is the report:

---

**AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation**

**Authors:** Jia Fu, Xiaoting Qin, Fangkai Yang, Lu Wang, Jue Zhang, Qingwei Lin, Yubo Chen, Dongmei Zhang, Saravan Rajmohan, Qi Zhang. Published in Findings of EMNLP 2024.

**Core Method:** RAG hyperparameter tuning is cast as an online multi-armed bandit (MAB) problem. Each "arm" is a hyperparameter setting (e.g., top-k=5) or a combination of settings. The reward signal is a linear combination: `w * accuracy - (1-w) * (tokens/max_tokens)`, where w controls the accuracy-vs-cost tradeoff. A novel two-level Hierarchical MAB (Hier-MAB) is introduced: a high-level MAB selects *which hyperparameter* to tune on each trial, and separate low-level MABs select the *value* for that parameter. This avoids combinatorial explosion from flattening all combinations into a single arm space. The primary algorithm is UCB; Thompson Sampling and Random Search serve as baselines.

**Hyperparameters tuned:**
- Top-k retrieved documents: {1, 3, 5, 7, 9}
- Prompt compression ratio: {0.3, 0.5, 0.7, 0.9, 1.0}
- Embedding model: {mpnet, ada_002, contriever}

**Online and global:** It operates online, receiving per-query feedback (e.g., thumbs up/down). Optimization is global (not per-query), using batches of B=4 queries per trial to reduce variance.

**Key results:** On ALCE-ASQA and Natural Questions (GPT-3.5-Turbo, GPT-4), MAB methods achieve Recall@5 approximately 0.8 in easy search spaces using only ~20% of the LLM API calls required by grid search. Hier-UCB outperforms flat UCB, Thompson Sampling, and Random Search in medium-difficulty scenarios.

**Difference from code repair routing:** AutoRAG-HP tunes continuous/categorical RAG pipeline parameters (retrieval count, compression, embeddings) via bandit exploration over a shared global policy. Code repair routing over structural abstractions (file/function/line) is a discrete, per-instance decision about *what context granularity to retrieve* for a specific broken code location -- a fundamentally different problem of selecting retrieval scope per fault, not tuning shared pipeline knobs across queries.

Sources:
- [AutoRAG-HP arXiv page](https://arxiv.org/abs/2406.19251)
- [AutoRAG-HP HTML version](https://arxiv.org/html/2406.19251)
- [ACL Anthology entry](https://aclanthology.org/2024.findings-emnlp.223/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10189c7b-1cec-4964-b075-4012856870ec",
  "isSidechain": true,
  "agentId": "a574fd1e405cf0bb5",
  "requestId": "req_011CawhgdeNATDtAyWcQ6h7F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1dba4ca-fb36-4277-a8b8-1bdd61e31c56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "cb44b8e2-fc32-497e-9c1e-9775d229f955",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TURDDaBb61sSZjiUSBiKiW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 11052,
      "output_tokens": 720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1480
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 720,
          "cache_read_input_tokens": 11052,
          "cache_creation_input_tokens": 1480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1480,
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
