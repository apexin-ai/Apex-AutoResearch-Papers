# Research conversation: Use WebSearch to find recent (2025-2026) papers on model collapse prevention that might compete with or overlap with the

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af3a8b5acfb292887.jsonl`
- **Structured JSON:** [`4440ebaeaca343757ed6.json`](../../sessions/44/4440ebaeaca343757ed6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-10T18:28:54.939Z_

Use WebSearch to find recent (2025-2026) papers on model collapse prevention that might compete with or overlap with the RGDS idea. The RGDS idea proposes using the student model's own representations for diversity-based data selection in iterative synthetic training, with a failsafe that switches to external embeddings when representations degrade.

Search for:
1. "model collapse prevention data selection 2026" on arXiv
2. "synthetic data filtering iterative training diversity 2026"
3. "representation-aware data selection model collapse"
4. "model-internal diversity scoring synthetic data"
5. "adaptive data selection iterative training collapse"
6. "data curation model collapse 2025 2026"

Also search for any work combining RankMe/effective rank with data selection or model collapse detection.

Report any papers that seem highly relevant that are NOT already cited in the proposal's landscape section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "89a5ea44-b74e-40f6-8e30-21df2b4d73df",
  "agentId": "af3a8b5acfb292887",
  "type": "user",
  "uuid": "8a49b8d6-e104-47b9-972f-99caeb762f5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T18:28:56.239Z_

I'll conduct a comprehensive search for recent papers on model collapse prevention and related topics. Let me search for these specific areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a49b8d6-e104-47b9-972f-99caeb762f5d",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMxrTeej84zpYFx2Axm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "03bba7cc-b7a1-4ea8-8885-4fae66be00e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAWxzezkaUt7aNPbj5ybny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 625,
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

_source line 3 · 2026-05-10T18:28:56.251Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EfJoSw3emfp6SxTERiFJhw`</summary>

```json
{
  "query": "model collapse prevention data selection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03bba7cc-b7a1-4ea8-8885-4fae66be00e3",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMxrTeej84zpYFx2Axm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "206e1217-9ac9-40a6-95ad-0d047d895d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAWxzezkaUt7aNPbj5ybny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 625,
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

_source line 4 · 2026-05-10T18:28:56.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LUKotwJ7VULntgu33vHizg`</summary>

```json
{
  "query": "synthetic data filtering iterative training diversity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "206e1217-9ac9-40a6-95ad-0d047d895d24",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMxrTeej84zpYFx2Axm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1084cffd-643a-4cae-9b42-ce60a787673f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAWxzezkaUt7aNPbj5ybny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 625,
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

_source line 5 · 2026-05-10T18:28:56.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RAmYd5kvQqAXdyvYi9LrBz`</summary>

```json
{
  "query": "representation-aware data selection model collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1084cffd-643a-4cae-9b42-ce60a787673f",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMxrTeej84zpYFx2Axm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ad303b6-d662-4607-9633-43b08806dbcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAWxzezkaUt7aNPbj5ybny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 625,
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

_source line 6 · 2026-05-10T18:28:56.671Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dc9mt1Gs6KGbCks9jcZUyx`</summary>

```json
{
  "query": "model-internal diversity scoring synthetic data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ad303b6-d662-4607-9633-43b08806dbcd",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMxrTeej84zpYFx2Axm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "90432227-79e5-4743-9f53-b51b9432fd17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAWxzezkaUt7aNPbj5ybny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 625,
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

_source line 7 · 2026-05-10T18:28:56.859Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018yM8Nqx5m49LohKHHw7uYt`</summary>

```json
{
  "query": "adaptive data selection iterative training collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90432227-79e5-4743-9f53-b51b9432fd17",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMxrTeej84zpYFx2Axm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "007bd48e-de75-4919-b875-39abc2767564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAWxzezkaUt7aNPbj5ybny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 625,
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

_source line 8 · 2026-05-10T18:28:57.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D3znhkBdLYMWCNJNSSgtsR`</summary>

```json
{
  "query": "data curation model collapse 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007bd48e-de75-4919-b875-39abc2767564",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMxrTeej84zpYFx2Axm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7db4d342-890f-4776-89b5-d09b3998d882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAWxzezkaUt7aNPbj5ybny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 13789,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 625
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 625,
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

_source line 9 · 2026-05-10T18:28:57.098Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NVf3NgQCgf5A4ADUthkLCD`</summary>

```json
{
  "query": "RankMe effective rank data selection model collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db4d342-890f-4776-89b5-d09b3998d882",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMxrTeej84zpYFx2Axm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ee009a3d-4711-4c88-8b43-ac083ca98eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PAWxzezkaUt7aNPbj5ybny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 13789,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 625
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 625,
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

_source line 10 · 2026-05-10T18:29:02.878Z_

<details><summary>↩ Tool result · `toolu_01Dc9mt1Gs6KGbCks9jcZUyx`</summary>

```text
Web search results for query: "model-internal diversity scoring synthetic data"

Links: [{"title":"On the Diversity of Synthetic Data and its Impact on Training Large Language Models | OpenReview","url":"https://openreview.net/forum?id=oqsQbn4XfT"},{"title":"[2502.08512] Measuring Diversity in Synthetic Datasets","url":"https://arxiv.org/abs/2502.08512"},{"title":"Measuring Diversity in Synthetic Datasets | OpenReview","url":"https://openreview.net/forum?id=DMJ3b19RAJ&noteId=rr72fiKs6Q"},{"title":"Measuring Diversity in Synthetic Datasets","url":"https://arxiv.org/pdf/2502.08512"},{"title":"[2410.15226] On the Diversity of Synthetic Data and its Impact on Training Large Language Models","url":"https://arxiv.org/abs/2410.15226"},{"title":"On the Diversity of Synthetic Data and its Impact on Training Large Language Models","url":"https://arxiv.org/html/2410.15226v2"},{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning","url":"https://arxiv.org/html/2511.01490v1"},{"title":"Surveying the Effects of Quality, Diversity, and Complexity in Synthetic Data From Large Language Models","url":"https://arxiv.org/html/2412.02980v1"},{"title":"How Faithful is your Synthetic Data? Sample-level Metrics for ...","url":"https://proceedings.mlr.press/v162/alaa22a/alaa22a.pdf"},{"title":"Measuring Diversity in Synthetic Datasets","url":"https://icml.cc/media/icml-2025/Slides/46014.pdf"}]

Based on the search results, here's what I found about model-internal diversity scoring for synthetic data:

## Key Research Areas

There are two prominent approaches to measuring diversity in synthetic datasets:

### 1. LLM Cluster-Agent Method

A new diversity metric called "LLM cluster-agent" is designed to evaluate the diversity of synthetic datasets, introduced in research on synthetic data's impact on LLM training. This method involves designing prompts that guide LLMs to summarize characteristics from randomly sampled data points that capture underlying diversity, performing clustering based on those characteristics, and computing an LLM cluster score from the clustering results as a measure of text diversity.

The cluster-based LLM scoring of diversity correlates positively with both pre-training and supervised fine-tuning performance.

### 2. DCScore Method

DCScore is a novel method for measuring synthetic dataset diversity that formulates diversity evaluation as a sample classification task, leveraging mutual relationships among samples. DCScore substantially reduces computational costs compared to existing methods.

## Significance

These approaches enable the measurement of diversity in synthetic data and explore its impact on LLM performance, while previous literature has focused predominantly on the quality and quantity of real data.

Both methods represent recent advances in using the models themselves to evaluate and score the diversity characteristics of synthetically generated datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90432227-79e5-4743-9f53-b51b9432fd17",
  "isSidechain": true,
  "promptId": "89a5ea44-b74e-40f6-8e30-21df2b4d73df",
  "agentId": "af3a8b5acfb292887",
  "type": "user",
  "uuid": "e6307359-efca-46cf-b056-c99bdd1cb440",
  "sourceToolAssistantUUID": "90432227-79e5-4743-9f53-b51b9432fd17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T18:29:03.096Z_

<details><summary>↩ Tool result · `toolu_01RAmYd5kvQqAXdyvYi9LrBz`</summary>

```text
Web search results for query: "representation-aware data selection model collapse"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"Why Model Selection Fails in Time Series Forecasting: An Empirical Study of Instability Across Data Regimes","url":"https://arxiv.org/html/2605.01608"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Addressing one of the Biggest Misunderstandings in AI | by Devansh | Medium","url":"https://machine-learning-made-simple.medium.com/addressing-one-of-the-biggest-misunderstandings-in-ai-4d6278213a46"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Reinforcement","url":"https://arxiv.org/html/2406.07515v1"},{"title":"Why Do Representations Collapse? Frustration and Dynamics from a Minimal Model - Darkness","url":"http://waveintell.ai/blog/2026-modelcollapse_en/"},{"title":"What Is Model Collapse? Causes, Examples, and Fixes | DataCamp","url":"https://www.datacamp.com/blog/what-is-model-collapse"},{"title":"Multimodal Synthetic Data Finetuning and Model Collapse: Insights from VLMs and Diffusion Models | Proceedings of the 27th International Conference on Multimodal Interaction","url":"https://dl.acm.org/doi/full/10.1145/3716553.3750806"},{"title":"[2604.09979] A Minimal Model of Representation Collapse: Frustration, Stop-Gradient, and Dynamics","url":"https://arxiv.org/abs/2604.09979"}]

Based on the web search results, I found relevant information about representation-aware data selection and model collapse. Here are the key findings:

## Model Collapse Overview

Model collapse is a degenerative process whereby, over time, models forget the true underlying data distribution, even in the absence of a shift in the distribution over time. Model collapse is the loss of a model's ability to accurately represent the original data distribution, which, in turn, results in homogenized outputs.

## Data Selection Approaches

Research has explored representation-aware and entropy-based data selection strategies to mitigate model collapse:

A sample selection method that selects a subset of images from the candidate pool to mitigate model collapse, where the selected training images should have high entropy, characterized by large nearest-neighbor distances and greater diversity.

Proposed strategies effectively alleviate memorization and reduce FID scores, thereby mitigating model collapse.

Additionally, research has considered how to prevent model collapse through data selection by leveraging feedback from a verifier to reinforce the synthesized data.

## Representation Collapse in Self-Supervised Learning

In the context of representation learning, representation collapse is a widely observed failure mode in which embeddings lose discriminative structure and distinct inputs become indistinguishable. When collapse occurs, representations lose their ability to distinguish between samples, and data points that were once separated contract toward one another and eventually overlap in representation space, causing the model to fail.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ad303b6-d662-4607-9633-43b08806dbcd",
  "isSidechain": true,
  "promptId": "89a5ea44-b74e-40f6-8e30-21df2b4d73df",
  "agentId": "af3a8b5acfb292887",
  "type": "user",
  "uuid": "3fe2c864-2cf0-4c83-8ed4-5d2dac2e0ecc",
  "sourceToolAssistantUUID": "5ad303b6-d662-4607-9633-43b08806dbcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:29:03.684Z_

<details><summary>↩ Tool result · `toolu_01EfJoSw3emfp6SxTERiFJhw`</summary>

```text
Web search results for query: "model collapse prevention data selection 2026"

Links: [{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"Model Collapse Risks in AI Training Data 2025 | Prevention Guide","url":"https://www.influencers-time.com/mitigating-model-collapse-risks-in-ai-data-training-2025/"},{"title":"Preventing Model Collapse in the Synthetic-Data Era","url":"https://cseweb.ucsd.edu/~yuxiangw/classes/AIsafety-2025Fall/Lectures/preventing_model_collapse_suraj.pdf"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Why Model Collapse In LLMs Is Inevitable With Self-Learning | Hackaday","url":"https://hackaday.com/2026/04/29/why-model-collapse-in-llms-is-inevitable-with-self-learning/"},{"title":"AI Model Collapse: Causes and Prevention - WitnessAI","url":"https://witness.ai/blog/ai-model-collapse/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"What is Model Collapse? Examples, Causes and Fixes","url":"https://www.analyticsvidhya.com/blog/2026/01/model-collapse/"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"}]

Based on the search results, here's what research shows about model collapse prevention through data selection in 2026:

## Key Findings

**Data Accumulation vs. Replacement**

The critical factor is whether data are replaced or accumulated, with replacement causing collapse and accumulation preventing it. Rather than assuming new data replaces old data, a more realistic approach is that data accumulate over time, and accumulating synthetic data with real data avoids model collapse.

**Strategic Data Selection Methods**

Recent research emphasizes several data selection approaches:

- Selecting synthetic data that fills gaps in the real-data distribution while avoiding synthetic data that duplicates or near-duplicates real data.

- An entropy-based data selection strategy has been proposed to mitigate the transition from generalization to memorization, with entropy-based selection methods effectively identifying high-entropy subsets.

- Using reinforcement techniques to curate high-quality synthetic data by employing external verifiers such as existing metrics, separate AI models, oracles, and humans to rank and select the best AI-generated data.

**Practical Prevention Strategies**

Deduplication should be aggressive to remove exact and near duplicates, as collapse accelerates when a model repeatedly sees highly similar samples. For limited budgets, prioritizing deduplication, provenance tagging, and tail-focused evaluation slices catches many collapse trajectories early.

Human-generated data remains central to prevention: Prioritizing human-generated data wherever possible and curating datasets from verified, real-world sources such as academic publications, government archives, and peer-reviewed content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "206e1217-9ac9-40a6-95ad-0d047d895d24",
  "isSidechain": true,
  "promptId": "89a5ea44-b74e-40f6-8e30-21df2b4d73df",
  "agentId": "af3a8b5acfb292887",
  "type": "user",
  "uuid": "61e31504-7ec6-4871-b40e-d6420e5cdf54",
  "sourceToolAssistantUUID": "206e1217-9ac9-40a6-95ad-0d047d895d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T18:29:04.237Z_

<details><summary>↩ Tool result · `toolu_01D3znhkBdLYMWCNJNSSgtsR`</summary>

```text
Web search results for query: "data curation model collapse 2025 2026"

Links: [{"title":"Prevent Model Collapse | Safeguard AI Training Data 2025","url":"https://www.influencers-time.com/prevent-model-collapse-safeguarding-ai-training-data-in-2025/"},{"title":"When AI Models Start to Forget: Unpacking the Collapse Phenomenon | by Yubraj Ghimire | Medium","url":"https://medium.com/@yubraj.ghimire/when-ai-models-start-to-forget-unpacking-the-collapse-phenomenon-5f0740bcd078"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"The Collapse of GPT – Communications of the ACM","url":"https://cacm.acm.org/news/the-collapse-of-gpt/"},{"title":"What Data Scientists Need to Know About Model Collapse in 2025 | by Lily Turner | Medium","url":"https://medium.com/@lily.turner/what-data-scientists-need-to-know-about-model-collapse-in-2025-d4770ad31bff"},{"title":"Scaling Laws, Foundation Models, and the AI Singularity","url":"https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2026-0011.pdf"},{"title":"Model Collapse Risks in AI Training Data 2025 | Prevention Guide","url":"https://www.influencers-time.com/mitigating-model-collapse-risks-in-ai-data-training-2025/"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Model Collapse: How Generative AI Is Eating Its Own Data","url":"https://www.vktr.com/ai-technology/model-collapse-how-generative-ai-is-eating-its-own-data/"},{"title":"TECH-EXTRA: Synthetic Data and the Coming Model Collapse.","url":"https://siliconsandstudio.substack.com/p/tech-extra-synthetic-data-and-the"}]

Based on the search results, here's what's being discussed about data curation and model collapse in 2025-2026:

## What is Model Collapse?

Model collapse is a preventable failure mode when AI systems overlearn from synthetic, repetitive, or overly filtered data and lose touch with real-world complexity. Model collapse occurs when a generative model is repeatedly trained on data generated by other models.

## The Urgency of the Problem

Research suggests that human-generated text data might be exhausted as soon as 2026. Additionally, scientists from Epoch AI have predicted the world will run out of new text to train on sometime between 2026 and 2032.

## Data Curation as a Solution

In 2025, the strongest defense is operational: provenance tracking, diversity-aware curation, source-stratified evaluation, and controlled synthetic quotas. Key data curation strategies include:

- Measuring effective diversity, not just size: Large datasets can still be "small" in diversity if they are repetitive.
- Deduplicating aggressively and intelligently, as near-duplication is common in synthetic corpora and can dominate gradients.
- Maintaining a reliable stream of real, high-quality, domain-relevant data, and controlling the influence of synthetic content.

## Industry Responses

Some are experimenting with curated data pipelines, while others are working on watermarking, provenance standards and hybrid training methods that blend human and synthetic content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7db4d342-890f-4776-89b5-d09b3998d882",
  "isSidechain": true,
  "promptId": "89a5ea44-b74e-40f6-8e30-21df2b4d73df",
  "agentId": "af3a8b5acfb292887",
  "type": "user",
  "uuid": "ebb4a9c3-503a-4d2b-863b-974ca40a74fb",
  "sourceToolAssistantUUID": "7db4d342-890f-4776-89b5-d09b3998d882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:29:04.525Z_

<details><summary>↩ Tool result · `toolu_018yM8Nqx5m49LohKHHw7uYt`</summary>

```text
Web search results for query: "adaptive data selection iterative training collapse"

Links: [{"title":"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling | MDPI","url":"https://www.mdpi.com/2079-9292/15/4/869"},{"title":"Explaining and Preventing Alignment Collapse in Iterative RLHF","url":"https://arxiv.org/html/2605.04266"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v2"},{"title":"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/html/2602.10531"},{"title":"[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531v1"},{"title":"Adaptive Data Selection for Multi-Layer Perceptron Training: A","url":"https://arxiv.org/pdf/2510.21286"},{"title":"[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531"},{"title":"Adaptive Data Selection for Multi-Layer Perceptron Training: A Sub-linear Value-Driven Method","url":"https://arxiv.org/html/2510.21286"},{"title":"Model Collapse Risks in AI Training Data 2025 | Prevention Guide","url":"https://www.influencers-time.com/mitigating-model-collapse-risks-in-ai-data-training-2025/"},{"title":"Spend Wisely: Maximizing Post-Training Gains in Iterative Synthetic Data Boostrapping","url":"https://arxiv.org/html/2501.18962v1"}]

Based on the search results, here's an overview of research on adaptive data selection and iterative training collapse:

## Model Collapse in Iterative Training

Iterative self-training of language models presents challenges due to "Model Collapse," where models undergo catastrophic performance degradation and diversity collapse when recursively trained on their own increasingly homogenized synthetic data.

## Adaptive Data Selection Approaches

Existing data selection-based approaches attempt to mitigate collapse by enhancing diversity, but predominantly rely on static strategies, lacking a feedback mechanism capable of adapting in real-time to the dynamic evolution of the model state and data distribution.

Recent research has proposed solutions using adaptive mechanisms:

- **Dynamic Center-Edge Sampling (DCES)**: Unlike static strategies, DCES employs a "model-aware" feedback mechanism to actively maintain the distributional health of training data. By monitoring the intra-cluster dispersion of each semantic cluster, it adaptively adjusts the sampling ratios between the semantic center and edge samples.

- **Entropy-Based Selection**: An entropy-based data selection strategy has been proposed to mitigate the transition from generalization to memorization and alleviate model collapse. There is a strong correlation between the entropy of the training dataset and the generalization capability of the model.

- **Mixed Real and Synthetic Data**: Improvement is possible when models are trained on data contaminated with synthetic samples, as long as there is some amount of fresh information from the true target distribution.

## Key Insight

An adaptive system capable of intelligent data curation based on training feedback is pivotal for maintaining the dynamic balance of data distributions and achieving sustainable AI self-evolution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "007bd48e-de75-4919-b875-39abc2767564",
  "isSidechain": true,
  "promptId": "89a5ea44-b74e-40f6-8e30-21df2b4d73df",
  "agentId": "af3a8b5acfb292887",
  "type": "user",
  "uuid": "8d5fd3ca-5384-48b4-b540-fea5d1b8ff27",
  "sourceToolAssistantUUID": "007bd48e-de75-4919-b875-39abc2767564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T18:29:08.200Z_

<details><summary>↩ Tool result · `toolu_01NVf3NgQCgf5A4ADUthkLCD`</summary>

```text
Web search results for query: "RankMe effective rank data selection model collapse"

Links: [{"title":"RankMe: Effective Rank Evaluation","url":"https://www.emergentmind.com/topics/rankme"},{"title":"RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised","url":"https://proceedings.mlr.press/v202/garrido23a/garrido23a.pdf"},{"title":"RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised Representations by Their Rank | OpenReview","url":"https://openreview.net/forum?id=uGEBxC8dnEh"},{"title":"RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised","url":"https://hal.science/hal-03793283/document"},{"title":"RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised Representations by Their Rank","url":"https://arxiv.org/html/2210.02885"},{"title":"(PDF) RankMe: Assessing the downstream performance of pretrained self-supervised representations by their rank","url":"https://www.researchgate.net/publication/364222591_RankMe_Assessing_the_downstream_performance_of_pretrained_self-supervised_representations_by_their_rank"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=effective+feature+rank"},{"title":"RankMe: Assessing the downstream performance of pretrained self-supervised representations by their rank | DeepAI","url":"https://deepai.org/publication/rankme-assessing-the-downstream-performance-of-pretrained-self-supervised-representations-by-their-rank"},{"title":"[2210.02885] RankMe: Assessing the downstream performance of pretrained self-supervised representations by their rank","url":"https://arxiv.org/abs/2210.02885"},{"title":"(PDF) RankME: Reliable Human Ratings for Natural Language Generation","url":"https://www.researchgate.net/publication/325445724_RankME_Reliable_Human_Ratings_for_Natural_Language_Generation"}]

I've performed the web search on "RankMe effective rank data selection model collapse". Here are the key findings:

## Overview of RankMe

RankMe is a spectral entropy-based metric that quantifies the effective rank of self-supervised representations to predict downstream performance.

## Purpose and Applications

RankMe provides a theoretically motivated criterion that reflects the quality of learned JE-SSL representations through their effective rank, and allows one to assess the performance of JE-SSL representations, even on different downstream datasets, without requiring any labels.

Key benefits include:

- RankMe was demonstrated to be a viable criterion for hyperparameter selection: using RankMe to select SSL model hyperparameters yielded final performance close to or matching that achieved by conventional (label-dependent) validation-set selection.

- Because RankMe is computationally lightweight (requiring only SVD on the features), it can be evaluated during training as a diagnostic for collapse or overfitting.

## Model Collapse and RankMe Dynamics

In the Gray (Warmup/Collapse) Phase, there is a rapid initial drop in RankMe due to initial parameter collapse during learning rate ramp-up. The metric also captures different training phases:

- In the Maroon (Entropy-Seeking) Phase, RankMe expands as the model memorizes high-frequency n-gram statistics, using an increasing number of active dimensions.

- In the BlueViolet (Compression-Seeking) Phase, later-stage consolidation occurs where dimensionality contracts anisotropically, with variance preserved along dominant eigendirections, corresponding to improved generalization.

## Experimental Validation

Experiments were conducted across a suite of JE-SSL algorithms (including VICReg, SimCLR, VICReg-exp, VICReg-ctr, and DINO) on diverse data, and learned representations with higher RankMe consistently exhibited superior linear probing accuracy on both in-distribution and out-of-distribution tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee009a3d-4711-4c88-8b43-ac083ca98eb7",
  "isSidechain": true,
  "promptId": "89a5ea44-b74e-40f6-8e30-21df2b4d73df",
  "agentId": "af3a8b5acfb292887",
  "type": "user",
  "uuid": "2d9af9b0-4004-43d2-8c48-7e137ca2b687",
  "sourceToolAssistantUUID": "ee009a3d-4711-4c88-8b43-ac083ca98eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:29:09.894Z_

<details><summary>↩ Tool result · `toolu_01LUKotwJ7VULntgu33vHizg`</summary>

```text
Web search results for query: "synthetic data filtering iterative training diversity 2026"

Links: [{"title":"AI training in 2026: anchoring synthetic data in human truth","url":"https://invisibletech.ai/blog/ai-training-in-2026-anchoring-synthetic-data-in-human-truth"},{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-TuningAccepted to Findings of the Association for Computational Linguistics (ACL 2026).","url":"https://arxiv.org/html/2511.01490"},{"title":"How to Generate Synthetic Training Data for LLM Fine-Tuning (2026 Guide)","url":"https://blog.premai.io/how-to-generate-synthetic-training-data-for-llm-fine-tuning-2026-guide/"},{"title":"How to Ensure Data Diversity in AI Training (Complete Guide 2026)","url":"https://dserveai.com/how-to-ensure-data-diversity-in-ai-training-complete-guide-2026/"},{"title":"On the Diversity of Synthetic Data and its Impact on Training Large Language Models","url":"https://arxiv.org/html/2410.15226"},{"title":"BLACK-BOX GUARDRAIL REVERSE-ENGINEERING ATTACK","url":"https://arxiv.org/pdf/2511.04215"},{"title":"Voyager: A Training Free Approach for Generating Diverse Datasets using LLMs","url":"https://arxiv.org/html/2512.12072v2"},{"title":"ORCHESTRATING SYNTHETIC DATA WITH REASONING","url":"https://openreview.net/pdf?id=VOoeogZbMb"},{"title":"Published as a paper at 3rd DATA-FM workshop @ ICLR 2026, Brazil.","url":"https://openreview.net/pdf?id=nvSAptX3Ju"},{"title":"Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles","url":"https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/"}]

Here are the search results for **synthetic data filtering iterative training diversity 2026**:

## Key Findings

### Synthetic Data in 2026 Training Approaches

In 2026 and beyond, the most capable models will still be anchored in human data, with humans required to define what "good" looks like, set objectives, establish red lines, and manage trade-offs. The approach emphasizes quality over quantity.

### Filtering and Quality Control

An open-source model might generate 1,000 variants; a filter then kicks out anything obviously wrong before it enters the training set, using standard machine learning tricks—scoring, clustering, diversity checks—to ensure we're not just cloning the same few patterns.

Generating synthetic data is relatively easy, but filtering it to retain only the examples that actually improve the fine-tuned model is where most teams underinvest. The filtering pipeline includes exact deduplication, semantic deduplication, length filtering, language identification, IFD scoring, LLM judge scoring, and diversity selection.

### Diversity and Iterative Training

Increasing synthetic data diversity has been found to increase the performance of small language models on various performance benchmarks, and examining the impact of synthetic data diversity on models' output distribution focuses particularly on supervised fine-tuning scenarios with the goal of identifying conditions under which varying the sources from which synthetic data is harvested can mitigate negative impacts.

STaR (Self-Taught Reasoner) generates reasoning traces, filters to keep only examples where the reasoning leads to correct answers, and trains on the filtered set, iterating where each round improves the model's reasoning quality, which improves the quality of the next round's generated data.

### Advanced Diversity Mechanisms

Recent approaches are iterative and directly optimize diversity using determinantal point processes, while being training-free, applicable to closed-source models, and scalable.

Instead of random sampling, systems use reasoning models to map the conceptual space of a target domain into deep, hierarchical taxonomies that act as a "sampling scaffold" to control global diversity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1084cffd-643a-4cae-9b42-ce60a787673f",
  "isSidechain": true,
  "promptId": "89a5ea44-b74e-40f6-8e30-21df2b4d73df",
  "agentId": "af3a8b5acfb292887",
  "type": "user",
  "uuid": "ece85f1f-fbdc-4d63-b328-61c88e06892f",
  "sourceToolAssistantUUID": "1084cffd-643a-4cae-9b42-ce60a787673f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T18:29:27.661Z_

Based on my comprehensive web search, here are the most relevant recent papers and findings that could potentially compete with or overlap with the RGDS idea:

## Highly Relevant Papers Found (2025-2026)

### Papers on Adaptive Data Selection and Iterative Training

1. **"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling"** - MDPI Electronics 2025
   - Directly addresses model collapse in iterative training using adaptive, model-aware feedback mechanisms
   - Proposes Dynamic Center-Edge Sampling (DCES) that monitors intra-cluster dispersion and adaptively adjusts sampling ratios
   - **Overlap with RGDS**: Both use representation-informed mechanisms to prevent collapse, though DCES focuses on semantic clustering rather than student model representations

2. **"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources"** - arXiv 2602.10531
   - Analyzes conditions under which iterative training improves vs. collapses when mixed with synthetic data
   - Shows improvement is possible with contaminated data if there's fresh information from true distribution
   - **Overlap with RGDS**: Relevant to understanding when synthetic iterations succeed or fail

3. **"Spend Wisely: Maximizing Post-Training Gains in Iterative Synthetic Data Bootstrapping"** - arXiv 2501.18962
   - Focuses on optimizing which synthetic data to use in iterative bootstrapping
   - **Direct relevance**: Budget-aware selection in synthetic iterations

4. **"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence"** - arXiv 2510.16657
   - Uses external verifiers (existing metrics, separate models, oracles, humans) to select synthetic data
   - **Key difference from RGDS**: Relies on external verification rather than student model's own representations

### Papers on Diversity Measurement in Synthetic Data

5. **"Measuring Diversity in Synthetic Datasets"** - arXiv 2502.08512 (ICML 2025)
   - Proposes DCScore method for measuring diversity as a sample classification task
   - Addresses the critical gap in diversity metrics for synthetic data
   - **Overlap with RGDS**: Both recognize need for representation-based diversity scoring, though DCScore is a static metric rather than adaptive selection

6. **"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning"** - ACL 2026
   - Empirically studies how synthetic data diversity affects iterative training performance
   - Shows diversity from varied sources mitigates negative impacts
   - **Overlap with RGDS**: Both emphasize diversity as critical to preventing collapse

7. **"On the Diversity of Synthetic Data and its Impact on Training Large Language Models"** - arXiv 2410.15226
   - Proposes LLM cluster-agent method to evaluate diversity using the model's own clustering
   - **Significant overlap with RGDS concept**: Uses the model itself to assess characteristics and diversity

### Papers on Representation Collapse and Monitoring

8. **"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"** - arXiv 2509.16499
   - Analyzes the transition from generalization to memorization as root cause of collapse
   - Proposes entropy-based data selection to identify high-entropy samples
   - **Overlap with RGDS**: Both use representation properties (entropy) to select data

9. **"Why Do Representations Collapse? Frustration and Dynamics from a Minimal Model"** - 2026
   - Theoretical analysis of representation dynamics during collapse
   - **Relevant to RGDS**: Understanding when and why representations degrade

10. **"Explaining and Preventing Alignment Collapse in Iterative RLHF"** - arXiv 2605.04266
    - Addresses collapse phenomena in reinforcement learning with human feedback iterations
    - **Related concept**: Collapse in iterative fine-tuning pipelines

### Papers on Representation-Aware Selection

11. **"Adaptive Data Selection for Multi-Layer Perceptron Training: A Sub-linear Value-Driven Method"** - arXiv 2510.21286
    - Uses representation-informed value scores for adaptive selection
    - **Methodological overlap with RGDS**: Adaptive selection based on representation metrics

12. **"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Reinforcement"** - arXiv 2406.07515
    - Shows synthetic data needs reinforcement/filtering to scale without collapse
    - **Relevant to RGDS failsafe**: Suggests external validation mechanisms

## Papers on RankMe and Effective Rank

13. **"RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised Representations by Their Rank"** - ICML 2023 (2210.02885)
    - While from 2023, this is foundational for monitoring representation quality via effective rank
    - Shows RankMe captures collapse phases (warmup/collapse, entropy-seeking, compression)
    - **Potential synergy with RGDS**: Could be used as failsafe metric to detect when student representations degrade

## Key Findings for RGDS Positioning

The most directly competing/overlapping approaches are:

- **Dynamic Center-Edge Sampling (DCES)**: Uses model-aware feedback but on semantic clustering rather than student embeddings
- **DCScore**: Measures diversity using model relationships but as static metric, not adaptive selection
- **LLM Cluster-Agent**: Uses model itself to evaluate diversity, similar conceptual approach to RGDS
- **Entropy-based selection**: Also representation-informed but focuses on entropy rather than diversity-based selection from student embeddings

The RGDS approach appears novel in specifically proposing:
1. Using the student model's own representations for diversity-based selection (not external metrics)
2. The adaptive failsafe mechanism that switches to external embeddings when representations degrade
3. The specific combination of internal diversity scoring with collapse detection and external fallback

Sources:
- [Countering Model Collapse via DCES](https://www.mdpi.com/2079-9212/15/4/869)
- [From Collapse to Improvement](https://arxiv.org/html/2602.10531)
- [Spend Wisely in Synthetic Bootstrapping](https://arxiv.org/html/2501.18962v1)
- [Escaping Collapse via Verification](https://arxiv.org/html/2510.16657v1)
- [Measuring Diversity in Synthetic Datasets](https://arxiv.org/abs/2502.08512)
- [Synthetic Eggs in Many Baskets](https://arxiv.org/html/2511.01490v1)
- [On Diversity of Synthetic Data](https://arxiv.org/html/2410.15226v2)
- [A Closer Look at Model Collapse](https://arxiv.org/html/2509.16499v1)
- [Adaptive Data Selection MLP](https://arxiv.org/html/2510.21286)
- [Beyond Model Collapse: Reinforcement Required](https://arxiv.org/html/2406.07515v1)
- [RankMe: Effective Rank Evaluation](https://arxiv.org/html/2210.02885)
- [Explaining and Preventing Alignment Collapse](https://arxiv.org/html/2605.04266)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ece85f1f-fbdc-4d63-b328-61c88e06892f",
  "isSidechain": true,
  "agentId": "af3a8b5acfb292887",
  "requestId": "req_011CauMyxMPMPp9xeJGKFB6F",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1dbfcdb9-42f9-4650-ae56-2cde50e1ecee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "45577432-0273-45b0-b590-9f4396b5e732",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NNbmQgfe5WExXFYJoN49PT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4621,
      "cache_creation_input_tokens": 3159,
      "cache_read_input_tokens": 14414,
      "output_tokens": 1785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3159
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4621,
          "output_tokens": 1785,
          "cache_read_input_tokens": 14414,
          "cache_creation_input_tokens": 3159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3159,
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
