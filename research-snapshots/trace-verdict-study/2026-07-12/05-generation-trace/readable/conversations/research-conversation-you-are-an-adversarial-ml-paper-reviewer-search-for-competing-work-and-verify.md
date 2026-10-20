# Research conversation: You are an adversarial ML paper reviewer. Search for competing work and verify claims for an idea called "Cultural-Layer

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab12362edb9b13554.jsonl`
- **Structured JSON:** [`005db04a31eacccdc7b4.json`](../../sessions/00/005db04a31eacccdc7b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-10T08:08:37.575Z_

You are an adversarial ML paper reviewer. Search for competing work and verify claims for an idea called "Cultural-Layer-Selective LoRA (CLS-LoRA)" for EMNLP 2026.

The paper's core claim: Cross-lingual instruction fine-tuning erases culturally-grounded language-specific knowledge. CLS-LoRA proposes empirical per-layer probing to identify which layers implement "cultural routing" vs "factual transfer", then freezes cultural-knowledge layers during LoRA fine-tuning to prevent erasure.

Key papers the idea references:
- arXiv:2510.26024 (Han, Agrawal & Briakou) - "Rethinking Cross-lingual Alignment" / Surgical Steering
- arXiv:2504.10191 - "Localized Cultural Knowledge is Conserved and Controllable in LLMs"
- arXiv:2510.08284 (Yamamoto et al., ICLR 2026) - Neuron-level analysis of cultural understanding
- arXiv:2602.22475 (CultureManager, Zhang et al., Feb 2026)
- arXiv:2509.11414 (LayRA) - layer-selective LoRA for continual multilingual language addition
- MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762)

Please search for:
1. Whether arXiv:2602.22475 ("Mind the Gap in Cultural Alignment") actually exists and what it proposes - search "CultureManager cultural alignment LoRA arxiv 2602.22475"
2. Any recent (2025-2026) papers on "cultural preservation fine-tuning multilingual" or "cultural erasure LLM training" that might compete
3. Search for papers on "layer freezing cultural knowledge LLM" to find direct competitors
4. Search for "selective LoRA cultural preservation multilingual" on arxiv
5. Search for "cross-lingual fine-tuning cultural knowledge preservation 2025 2026"

For each search, report: what you found, the paper title, venue/arxiv ID if available, and whether it threatens the novelty of CLS-LoRA.

Be thorough — use WebSearch with multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "a7267043-254f-43e7-8149-8503452646f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T08:08:38.742Z_

I'll conduct a thorough adversarial review by searching for competing work and verifying the claims about CLS-LoRA. Let me start with systematic searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7267043-254f-43e7-8149-8503452646f7",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYfQF8LEGbav22z7eTu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c22a7eb-e2c2-4c7b-b7e9-230bddec8a94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ND8BixoikP1BQ8q8EPB554",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 970,
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

_source line 3 · 2026-05-10T08:08:38.966Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHhfRP8yfDx3tyK17NWngT`</summary>

```json
{
  "query": "arXiv 2602.22475 CultureManager cultural alignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c22a7eb-e2c2-4c7b-b7e9-230bddec8a94",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYfQF8LEGbav22z7eTu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3211085f-3875-4bae-9c99-08f6aa2b19b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ND8BixoikP1BQ8q8EPB554",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 970,
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

_source line 4 · 2026-05-10T08:08:39.184Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NGapNnT4PwpUYko2kSDcR8`</summary>

```json
{
  "query": "cultural preservation fine-tuning multilingual LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3211085f-3875-4bae-9c99-08f6aa2b19b2",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYfQF8LEGbav22z7eTu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "636180fa-29c1-4613-9d24-71268d6dd366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ND8BixoikP1BQ8q8EPB554",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 970,
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

_source line 5 · 2026-05-10T08:08:39.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013pMzzXgCjjHhKEZNpK8DkQ`</summary>

```json
{
  "query": "cultural erasure cross-lingual instruction fine-tuning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "636180fa-29c1-4613-9d24-71268d6dd366",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYfQF8LEGbav22z7eTu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cdd11d0f-e9c0-4103-a93b-8a33c02764ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ND8BixoikP1BQ8q8EPB554",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 970,
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

_source line 6 · 2026-05-10T08:08:40.451Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014pDLUHV1LvKPTHtPBoiNTJ`</summary>

```json
{
  "query": "layer freezing cultural knowledge LLM preservation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdd11d0f-e9c0-4103-a93b-8a33c02764ba",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYfQF8LEGbav22z7eTu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e754042-3e97-4e28-9222-802c284051bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ND8BixoikP1BQ8q8EPB554",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 16155,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 970
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 970,
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

_source line 7 · 2026-05-10T08:08:40.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VMndKuZ1aybSqni16MiHhQ`</summary>

```json
{
  "query": "selective LoRA cultural preservation multilingual 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e754042-3e97-4e28-9222-802c284051bf",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYfQF8LEGbav22z7eTu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "360a2854-1fce-41d8-b1d0-826c63fde29f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ND8BixoikP1BQ8q8EPB554",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 16155,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 970
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 970,
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

_source line 8 · 2026-05-10T08:08:45.697Z_

<details><summary>↩ Tool result · `toolu_01LHhfRP8yfDx3tyK17NWngT`</summary>

```text
Web search results for query: "arXiv 2602.22475 CultureManager cultural alignment"

Links: [{"title":"Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models","url":"https://arxiv.org/html/2602.22475"},{"title":"[2602.22475] Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models","url":"https://arxiv.org/abs/2602.22475"},{"title":"Mind the Gap in Cultural Alignment: Task-Aware ...","url":"https://arxiv.org/pdf/2602.22475"},{"title":"A resource-efficient framework for cultural alignment in large language models (LLMs): The Chinese context - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S3050741326000029"},{"title":"[2504.08863] An Evaluation of Cultural Value Alignment in LLM","url":"https://arxiv.org/abs/2504.08863"},{"title":"Investigating Cultural Alignment of Large Language Models","url":"https://arxiv.org/html/2402.13231v1"},{"title":"[PDF] Investigating Cultural Alignment of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Investigating-Cultural-Alignment-of-Large-Language-AlKhamissi-ElNokrashy/b1890367317f0657c08ed96be4c474035b34b485"},{"title":"[2602.01161] Beyond Training for Cultural Awareness: The Role of Dataset Linguistic Structure in Large Language Models","url":"https://arxiv.org/abs/2602.01161"},{"title":"[2602.00046] Extending Beacon to Hindi: Cultural Adaptation Drives Cross-Lingual Sycophancy","url":"https://arxiv.org/abs/2602.00046"},{"title":"[2602.04729] \"Be My Cheese?\": Cultural Nuance Benchmarking for Machine Translation in Multilingual LLMs","url":"https://arxiv.org/abs/2602.04729"}]

Based on the search results, here's information about the arXiv paper 2602.22475:

## Overview

CultureManager is a novel pipeline for task-specific cultural alignment that synthesizes task-aware cultural data in line with target task formats, grounded in culturally relevant web search results.

## Problem Statement

Existing cultural alignment approaches fail to align LLMs' broad cultural values with the specific goals of downstream tasks and suffer from cross-culture interference.

## How CultureManager Works

The system has three main components:

1. **Data Synthesis**: An LLM-based query generator produces task-aware search queries, a web search agent retrieves culture-specific materials, and a data generator converts the retrieved content into labeled training samples in the target task format.

2. **Culture-Specific Training**: For each culture, CultureManager fine-tunes a lightweight LoRA adapter while keeping the base LLM frozen.

3. **Culture Management**: During inference, a culture router selects the appropriate adapter based on the input cultural context to produce culturally aligned outputs.

## Key Results

Experiments across ten national cultures and culture-sensitive tasks show consistent improvements over prompt-based and fine-tuning baselines, demonstrating the necessity of task adaptation and modular culture management for effective cultural alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3211085f-3875-4bae-9c99-08f6aa2b19b2",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "deabf53c-2f20-4d29-a6d7-06faf5616e9f",
  "sourceToolAssistantUUID": "3211085f-3875-4bae-9c99-08f6aa2b19b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T08:08:46.683Z_

<details><summary>↩ Tool result · `toolu_013pMzzXgCjjHhKEZNpK8DkQ`</summary>

```text
Web search results for query: "cultural erasure cross-lingual instruction fine-tuning LLM"

Links: [{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF","url":"https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/abs/2510.26024"},{"title":"Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/pdf/2510.26024"},{"title":"AdaMCoT: Rethinking Cross-Lingual Factual Reasoning through Adaptive Multilingual Chain-of-Thought","url":"https://arxiv.org/html/2501.16154v3"},{"title":"CultureLLM: Incorporating Cultural Differences into Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/397200926_CultureLLM_Incorporating_Cultural_Differences_into_Large_Language_Models"},{"title":"CultureLLM: Incorporating Cultural Differences into Large Language Models","url":"https://arxiv.org/pdf/2402.10946"},{"title":"[Literature Review] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://www.themoonlight.io/en/review/rethinking-cross-lingual-alignment-balancing-transfer-and-cultural-erasure-in-multilingual-llms"},{"title":"M-DaQ: Retrieving Samples with Multilingual Diversity and Quality for Instruction Fine-Tuning Datasets","url":"https://arxiv.org/html/2509.15549"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"}]

Based on the search results, I found substantial research on the intersection of cultural erasure, cross-lingual instruction fine-tuning, and Large Language Models. Here's what the literature reveals:

## Key Research Findings

Cross-lingual alignment (CLA) aims to align multilingual representations, enabling Large Language Models (LLMs) to seamlessly transfer knowledge across languages. However, this pursuit of representational convergence can inadvertently cause "cultural erasure," the functional loss of providing culturally-situated responses that should diverge based on the query language.

### The Core Trade-off

Researchers have introduced a holistic evaluation framework called the "transfer-localization plane," which quantifies both desirable knowledge transfer and undesirable cultural erasure. Studies using this framework found that recent CLA approaches consistently improve factual transfer at the direct cost of cultural localization across all six languages studied.

### Two Types of Knowledge

The research distinguishes between: Universal knowledge (language-invariant where responses should be consistent across languages) and culturally-adaptive knowledge (where universal concepts are instantiated differently through local norms, cultural contexts, or regulations).

### Solutions and Approaches

Research reveals that while cross-lingual transfer is better realized within a model's middle layers, cultural localization is predominantly encoded in the deeper layers. Additionally, M-DaQ, a diversity-driven sample retrieval method, effectively mitigates multilingual challenges arising from data skewness in multilingual instruction fine-tuning data and the underrepresentation of low-resource culturally specific values.

The research suggests that balancing cultural specificity with cross-lingual knowledge transfer requires explicit consideration during both instruction fine-tuning and inference time interventions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdd11d0f-e9c0-4103-a93b-8a33c02764ba",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "0f9f34f3-99b7-446a-930f-ae8c366896f9",
  "sourceToolAssistantUUID": "cdd11d0f-e9c0-4103-a93b-8a33c02764ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T08:08:47.046Z_

<details><summary>↩ Tool result · `toolu_014pDLUHV1LvKPTHtPBoiNTJ`</summary>

```text
Web search results for query: "layer freezing cultural knowledge LLM preservation"

Links: [{"title":"[2504.10191] Localized Cultural Knowledge is Conserved and Controllable in Large Language Models","url":"https://arxiv.org/abs/2504.10191"},{"title":"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=sK06hYt75z"},{"title":"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models","url":"https://arxiv.org/html/2504.10191v1"},{"title":"A resource-efficient framework for cultural alignment in large language models (LLMs): The Chinese context - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S3050741326000029"},{"title":"Epistemoverse: Toward an AI-Driven Knowledge Metaverse for Intellectual Heritage Preservation","url":"https://arxiv.org/html/2512.12201"},{"title":"Generative AI and Large Language Models in Language Preservation: Opportunities and Challenges","url":"https://arxiv.org/html/2501.11496v1"},{"title":"When AI Writes, Whose Voice Remains? Quantifying Cultural Marker Erasure Across World English Varieties in Large Language Models","url":"https://arxiv.org/html/2602.22145"},{"title":"Null-Space–Constrained Contrastive Visual Forgetting for MLLM Unlearning","url":"https://arxiv.org/html/2605.05909v1"},{"title":"UNLEARN Efficient Removal of Knowledge in Large Language Models","url":"https://arxiv.org/html/2408.04140v1"},{"title":"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/390773600_Localized_Cultural_Knowledge_is_Conserved_and_Controllable_in_Large_Language_Models"}]

Based on the search results, I found several relevant studies on cultural knowledge preservation in LLMs:

## Key Research Findings

### Localized Cultural Knowledge in LLMs

LLMs often default to English-centric responses even when generating in other languages, but local cultural information persists within the models and can be readily activated for cultural customization.

Researchers identified an explicit cultural customization vector, conserved across all non-English languages, which enables LLMs to be steered from the synthetic English cultural world-model toward each non-English cultural world.

### Layer-Freezing Approach for Cultural Preservation

A resource-efficient approach uses layer freezing: LoRA fine-tuning updates only the adapter layer parameters while keeping the original LLM layers frozen. This method achieves significant improvements without the need to retrain the entire model, thus minimizing computational costs.

### Mechanistic Interpretability Methods

Using mechanistic interpretability tools, researchers explored where cultural localization happens within LLMs and proposed a method using activation patching analysis and linear steering vectors on relevant layers that allow culturally localizing model responses without explicit prompting.

### Language Preservation with AI

Generative AI and large-scale language models have emerged as powerful tools in the world of language preservation, especially for near-native languages, with new opportunities emerging to mitigate the dramatic decline of languages around the world.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e754042-3e97-4e28-9222-802c284051bf",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "be1bd6ef-267b-4ea3-aafe-955f98606ae7",
  "sourceToolAssistantUUID": "3e754042-3e97-4e28-9222-802c284051bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T08:08:47.539Z_

<details><summary>↩ Tool result · `toolu_01NGapNnT4PwpUYko2kSDcR8`</summary>

```text
Web search results for query: "cultural preservation fine-tuning multilingual LLM 2025 2026"

Links: [{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Opportunities and Challenges of Large Language Models for","url":"https://arxiv.org/pdf/2412.04497"},{"title":"BRIDGING THE GAPS IN MULTILINGUAL REASONING","url":"https://openreview.net/pdf?id=Q5mkmW0cUD"},{"title":"Fluent but Foreign: Even Regional LLMs Lack Cultural Alignment","url":"https://arxiv.org/html/2505.21548"},{"title":"ACL 2025: 5 Trends Shaping the Future of LLMs | Appen","url":"https://www.appen.com/blog/acl-2025"},{"title":"CultureLLM: Incorporating Cultural Differences into Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf"},{"title":"GitHub - tjunlp-lab/Awesome-Multilingual-LLMs-Papers: Awesome-Multilingual-LLMs-Papers · GitHub","url":"https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"Identity-Aware Large Language Models require Cultural Reasoning","url":"https://arxiv.org/html/2510.18510v1"},{"title":"A survey of multilingual large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666389924002903"}]

I've found comprehensive research on cultural preservation through fine-tuning of multilingual LLMs in 2025-2026. Here are the key findings:

## Recent Research and Trends

LLMs hold vast potential to preserve and comprehend the extensive cultural and intellectual treasures embedded in low-resource languages. Fine-tuning on small, domain-specific datasets helps capture regional and dialectal nuances.

## Notable Projects and Approaches

Several recent initiatives focus on cultural alignment:

- Nanda is promoted as a multilingual model aiming to "usher in a culturally-aware AI era" for Hindi users, while Jais is framed as an LLM built to preserve Arabic culture.

- Instruction-tuning datasets such as Bactrian, Aya, Multilingual Alpaca, and SphinX have improved performance across high- and low-resource languages by emphasizing diversity and cultural specificity.

## Current Challenges

However, there are significant gaps in current approaches:

- Current evaluations remain narrowly focused on multilingual fluency, overlooking the deeper question of alignment with local cultural values, beliefs, and practices. In high-stakes domains, cultural misalignment risks eroding trust and undermining the communities these models aim to serve.

- Without explicit tuning, models largely mirror the norms dominant in their training data and struggle to accurately reflect the moral or social norms of less-represented cultures. Models often default to majority cultural priors unless representations of norms and trade-offs are made explicit.

## Emerging Solutions

Cultural evaluation is positioned as a first-class requirement alongside multilingual benchmarks, with calls for native, community-authored corpora and diverse evaluations to build truly sovereign LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "636180fa-29c1-4613-9d24-71268d6dd366",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "db2ae753-19cc-43e0-ba63-0f72fd642981",
  "sourceToolAssistantUUID": "636180fa-29c1-4613-9d24-71268d6dd366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T08:08:48.389Z_

<details><summary>↩ Tool result · `toolu_01VMndKuZ1aybSqni16MiHhQ`</summary>

```text
Web search results for query: "selective LoRA cultural preservation multilingual 2025"

Links: [{"title":"Enhancing a Massively Multilingual Model for Text ...","url":"https://arxiv.org/pdf/2510.01250"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"LoRA-Based Pattern Generation for Yi Ethnic Embroidery Heritage Preservation | Proceedings of the 2025 Conference on Creativity and Cognition","url":"https://dl.acm.org/doi/10.1145/3698061.3726964"},{"title":"Probing and Enhancing Arabic Cultural Awareness in ...","url":"https://aclanthology.org/2025.arabicnlp-sharedtasks.115.pdf"},{"title":"A Language-Agnostic Hierarchical LoRA-MoE Architecture for CTC-based Multilingual ASR","url":"https://arxiv.org/html/2601.00557v1"},{"title":"Workshop on Language Models for Low-Resource Languages (2025) - ACL Anthology","url":"https://aclanthology.org/events/loreslm-2025/"},{"title":"Notebook for the PAN Lab at CLEF 2025","url":"https://ceur-ws.org/Vol-4038/paper_288.pdf"},{"title":"Dynamic Transmission and Innovative Transformation of Cultural Heritage: Generative Artificial Intelligence Practices Based on Cultural Cognitive Models","url":"https://www.mdpi.com/2076-3417/15/23/12651"},{"title":"Infusing AI Art with Cultural Authenticity Through the Culture-Specific LoRA | Proceedings of the 33rd ACM International Conference on Multimedia","url":"https://dl.acm.org/doi/10.1145/3746027.3755670"},{"title":"Published as a conference paper at ICLR 2025 CACHED MULTI-LORA COMPOSITION","url":"https://openreview.net/pdf/1ac5b3d8adcd952539a025a43cff901be07737df.pdf"}]

I found several relevant papers and resources on this topic. Here are the key findings from the search:

## Cultural Preservation with LoRA

LoRA adaptation is being applied to cultural heritage preservation, such as adapting Stable Diffusion XL to generate Yi embroidery patterns while maintaining cultural authenticity. LoRA's lightweight fine-tuning mechanism allows AI models to adapt to niche datasets, such as Yi embroidery patterns, generating culturally resonant content without overfitting.

## Multilingual Applications

Parameter-efficient LoRA fine-tuning techniques are being applied to massive multilingual models, such as adapting a 12B-parameter Gemma-3 multilingual transformer for text detoxification tasks. A Language-agnostic Hierarchical LoRA-MoE framework has been proposed for multilingual ASR, consisting of a multilingual shared LoRA for learning language-invariant acoustic representations and language-specific LoRA experts for modeling language-dependent characteristics.

## Cultural Awareness in Multilingual Models

Research in 2025 addresses how Large Language Models have demonstrated impressive multilingual capabilities, but their reasoning often reflects English-centric perspectives, which can limit accuracy in culture-specific contexts. A culture-specific LoRA framework has been developed to enhance AI-generated art with authentic cultural representation, aiming to both preserve and promote cultural heritage.

## LoRA for Heritage Preservation

LoRA technology is being used for efficient fine-tuning in cultural heritage applications, where low-rank matrices are incorporated into pre-trained model weights to effectively reduce training parameters and computational resource consumption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "360a2854-1fce-41d8-b1d0-826c63fde29f",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "f4dd7541-7bcb-4adf-8019-be2d52a7ff05",
  "sourceToolAssistantUUID": "360a2854-1fce-41d8-b1d0-826c63fde29f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T08:08:50.915Z_

Now let me do additional targeted searches to check for more specific competing work:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4dd7541-7bcb-4adf-8019-be2d52a7ff05",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYgCSzTZGKZvdUm24xR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c705dce-5716-4b9f-8fe6-629f9d6751ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SchwA7dWr9FQNnpx1sNDxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5615,
      "cache_read_input_tokens": 17125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5615,
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

_source line 14 · 2026-05-10T08:08:52.515Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013P2RjeRJpMoKqRkg9C2t1t`</summary>

```json
{
  "query": "cross-lingual fine-tuning cultural knowledge 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c705dce-5716-4b9f-8fe6-629f9d6751ef",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYgCSzTZGKZvdUm24xR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae4d327a-4d2d-47c7-b746-49b395413539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SchwA7dWr9FQNnpx1sNDxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5615,
      "cache_read_input_tokens": 17125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5615,
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

_source line 15 · 2026-05-10T08:08:53.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PZ6meSCnA4tgpgBAfSi7CB`</summary>

```json
{
  "query": "LayRA layer-selective LoRA multilingual continual learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae4d327a-4d2d-47c7-b746-49b395413539",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYgCSzTZGKZvdUm24xR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b5f69b1d-77f6-4841-99eb-7dd5a65e606d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SchwA7dWr9FQNnpx1sNDxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5615,
      "cache_read_input_tokens": 17125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5615,
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

_source line 16 · 2026-05-10T08:08:53.848Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GAbAzjWcgo9opZV8jgxtH1`</summary>

```json
{
  "query": "\"MLAS-LoRA\" ACL 2025 multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f69b1d-77f6-4841-99eb-7dd5a65e606d",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYgCSzTZGKZvdUm24xR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b429dd0b-f1ff-47e4-9f13-8c8563788e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SchwA7dWr9FQNnpx1sNDxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5615,
      "cache_read_input_tokens": 17125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5615,
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

_source line 17 · 2026-05-10T08:08:54.285Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LXAeLAAViNoLuSfyesqvvX`</summary>

```json
{
  "query": "arXiv 2510.08284 Yamamoto cultural understanding neurons ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b429dd0b-f1ff-47e4-9f13-8c8563788e5f",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYgCSzTZGKZvdUm24xR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d18f020-8ebb-491d-a26b-6201aa815335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SchwA7dWr9FQNnpx1sNDxg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5615,
      "cache_read_input_tokens": 17125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5615,
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

_source line 18 · 2026-05-10T08:08:54.420Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N11WHhfszpuTRN1w7t9CcC`</summary>

```json
{
  "query": "arXiv 2509.11414 LayRA layer-selective LoRA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d18f020-8ebb-491d-a26b-6201aa815335",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYgCSzTZGKZvdUm24xR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7dd8f21c-8c60-4c59-ad2c-22fd34d19d8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SchwA7dWr9FQNnpx1sNDxg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5615,
      "cache_read_input_tokens": 17125,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 290,
          "cache_read_input_tokens": 17125,
          "cache_creation_input_tokens": 5615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5615,
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

_source line 19 · 2026-05-10T08:08:59.794Z_

<details><summary>↩ Tool result · `toolu_01N11WHhfszpuTRN1w7t9CcC`</summary>

```text
Web search results for query: "arXiv 2509.11414 LayRA layer-selective LoRA"

Links: [{"title":"[2509.11414] Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/abs/2509.11414"},{"title":"Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/pdf/2509.11414"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nZeVKeeFYf9"},{"title":"[PDF] LoRA: Low-Rank Adaptation of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LoRA:-Low-Rank-Adaptation-of-Large-Language-Models-Hu-Shen/a8ca46b171467ceb2d7652fbfb67fe701ad86092"},{"title":"MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts","url":"https://arxiv.org/html/2404.15159v3"},{"title":"Cross-LoRA: A Data-Free LoRA Transfer Framework across Heterogeneous LLMs","url":"https://arxiv.org/html/2508.05232v1"},{"title":"[2509.25214] On-the-Fly Adaptation to Quantization: Configuration-Aware LoRA for Efficient Fine-Tuning of Quantized LLMs","url":"https://www.arxiv.org/abs/2509.25214"},{"title":"Adaptive Selection of LoRA Components in Privacy-Preserving Federated Learning","url":"https://arxiv.org/html/2605.05769"},{"title":"TreeLoRA: Efficient Continual Learning via Layer-Wise LoRAs Guided by a Hierarchical Gradient-Similarity Tree","url":"https://arxiv.org/html/2506.10355v1"},{"title":"Aletheia: Gradient-Guided Layer Selection for Efficient LoRA Fine-Tuning Across Architectures","url":"https://arxiv.org/html/2604.15351"}]

Based on the search results, I found information about arXiv paper 2509.11414:

The paper is titled "Continually Adding New Languages to Multilingual Language Models". 

The work investigates the problem of continually adding new languages to a multilingual model, assuming access to pretraining data in only the target languages. The paper proposes Layer-Selective LoRA (LayRA), which adds Low-Rank Adapters (LoRA) to selected initial and final layers while keeping the rest of the model frozen.

LayRA inserts LoRA modules into selected transformer layers in a language model during training, while keeping the rest of the model frozen. The approach applies LoRA to the earliest 10 and the final 2 layers, and also finetunes the embedding layer and the LM head.

The paper addresses the challenge that naive approaches, such as continued pretraining, suffer from catastrophic forgetting; however, mitigation strategies like experience replay cannot be applied due to the lack of original pretraining data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dd8f21c-8c60-4c59-ad2c-22fd34d19d8f",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "59b1d8f6-53c5-4dbc-85ca-d7128b925cbb",
  "sourceToolAssistantUUID": "7dd8f21c-8c60-4c59-ad2c-22fd34d19d8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T08:08:59.798Z_

<details><summary>↩ Tool result · `toolu_01GAbAzjWcgo9opZV8jgxtH1`</summary>

```text
Web search results for query: ""MLAS-LoRA" ACL 2025 multilingual"

Links: [{"title":"MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.762/"},{"title":"MLAS-LoRA: Language-Aware Parameters Detection and ...","url":"https://aclanthology.org/2025.acl-long.762.pdf"},{"title":"Adaptive LoRA Merge with Parameter Pruning for Low- ...","url":"https://aclanthology.org/2025.findings-acl.990.pdf"},{"title":"Challenges in Adapting Multilingual LLMs to Low-Resource Languages using LoRA PEFT Tuning - ACL Anthology","url":"https://aclanthology.org/2025.chipsal-1.22/"},{"title":"NLP4Health: Multilingual Clinical Dialogue Summarization and QA with mT5 and LoRA - ACL Anthology","url":"https://aclanthology.org/2025.nlpai4health-main.10/"},{"title":"Progressive LoRA for Multimodal Continual Instruction ...","url":"https://aclanthology.org/2025.findings-acl.143.pdf"},{"title":"Workshop on Language Models for Low-Resource Languages (2025) - ACL Anthology","url":"https://aclanthology.org/events/loreslm-2025/"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Proceedings of Recent Advances in Natural Language Processing,pages 1137–1147","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.131.pdf"},{"title":"Language Fusion for Parameter-Efficient Cross-lingual ...","url":"https://aclanthology.org/2025.acl-long.1255.pdf"}]

Based on the search results, here's what I found about MLAS-LoRA at ACL 2025:

MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation was presented at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) by Dong et al.

**Overview:**
MLAS-LoRA efficiently adapts LLMs to machine translation (MT) by selectively transferring knowledge from a large teacher to a small student model.

**Methodology:**
The approach evaluates the awareness of neurons and extracts linguistic knowledge in the teacher model for both the general MT task and specific language pairs, then proposes a multiple language-specific LoRA architecture to inject the extracted knowledge into the student model. During fine-tuning, only the parameters of the relevant language-general and language-specific LoRA modules are updated.

**Results:**
Experimental results on diverse multilingual language pairs demonstrate that MLAS-LoRA significantly outperforms strong baselines by +1.7 BLEU on average, including standard fine-tuning and other parameter-efficient methods.

The paper appears in the ACL 2025 long papers section (pages 15645-15660, July 27 - August 1, 2025, Vienna, Austria).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b429dd0b-f1ff-47e4-9f13-8c8563788e5f",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "5691a964-4e5e-41f2-8eea-b3bd620d8dc8",
  "sourceToolAssistantUUID": "b429dd0b-f1ff-47e4-9f13-8c8563788e5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T08:09:00.078Z_

<details><summary>↩ Tool result · `toolu_01PZ6meSCnA4tgpgBAfSi7CB`</summary>

```text
Web search results for query: "LayRA layer-selective LoRA multilingual continual learning"

Links: [{"title":"Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/pdf/2509.11414"},{"title":"[Literature Review] Continually Adding New Languages to Multilingual Language Models","url":"https://www.themoonlight.io/en/review/continually-adding-new-languages-to-multilingual-language-models"},{"title":"Lamer-SSL: Layer-aware mixture of LoRA experts for continual multilingual expansion of self-supervised models without forgetting","url":"https://arxiv.org/html/2602.12746"},{"title":"[2602.12746] Lamer-SSL: Layer-aware Mixture of LoRA Experts for Continual Multilingual Expansion of Self-supervised Models without Forgetting","url":"https://arxiv.org/abs/2602.12746"},{"title":"[2509.11414] Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/abs/2509.11414"},{"title":"TreeLoRA: Efficient Continual Learning via Layer-Wise LoRAs","url":"https://www.lamda.nju.edu.cn/qianyy/paper/ICML25_TreeLoRA.pdf"},{"title":"ELO: Efficient Layer-Specific Optimization for Continual Pretraining of Multilingual LLMs","url":"https://arxiv.org/html/2601.03648"},{"title":"LoRA-Whisper: Parameter-Efficient and Extensible Multilingual ASR","url":"https://arxiv.org/html/2406.06619"},{"title":"Towards Rehearsal-Free Multilingual ASR: A LoRA-based Case Study on Whisper","url":"https://arxiv.org/html/2408.10680"},{"title":"Multi-LoRA continual learning based instruction tuning framework for universal information extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705124013844"}]

Based on the search results, here's what I found about LayRA (Layer-Selective LoRA):

## LayRA Overview

LayRA is a Layer-Selective LoRA approach that inserts LoRA modules into specific transformer layers while keeping the rest of the model frozen. It's designed to address the challenge of continually adding new languages to multilingual language models.

## Key Problem and Solution

Multilingual language models are trained on a fixed set of languages, and to support new languages, the models need to be retrained from scratch. This is an expensive endeavor and is often infeasible, as model developers tend not to release their pre-training data. Naive approaches, such as continued pretraining, suffer from catastrophic forgetting; however, mitigation strategies like experience replay cannot be applied due to the lack of original pretraining data.

## Technical Approach

LayRA builds on two insights: (1) LoRA reduces forgetting, and (2) multilingual models encode inputs in the source language in the initial layers, reason in English in intermediate layers, and translate back to the source language in final layers. LayRA strategically applies LoRA only to the earliest 10 and final 2 transformer layers, in addition to finetuning the embedding layer and the LM head.

## Performance Results

LayRA considerably outperforms LoRA in terms of forgetting while being competitive with LoRA in terms of learning across all tasks and target languages. LayRA consistently demonstrated the best trade-off between mitigating catastrophic forgetting and learning new languages across tasks and target languages, outperforming full CPT, layer-selective full CPT, and LoRA CPT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5f69b1d-77f6-4841-99eb-7dd5a65e606d",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "e1c620e7-9b28-4a5a-8367-58745204d27e",
  "sourceToolAssistantUUID": "b5f69b1d-77f6-4841-99eb-7dd5a65e606d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T08:09:00.536Z_

<details><summary>↩ Tool result · `toolu_013P2RjeRJpMoKqRkg9C2t1t`</summary>

```text
Web search results for query: "cross-lingual fine-tuning cultural knowledge 2025 2026"

Links: [{"title":"CommIT Journal 20(1), 155–167, 2026 Advancing Cross-Cultural Natural Language","url":"https://journal.binus.ac.id/index.php/commit/article/download/13912/5720"},{"title":"C3NLP @ ACL 2026","url":"https://c3nlp.github.io/"},{"title":"Cross-Lingual Knowledge Transfer","url":"https://www.emergentmind.com/topics/cross-lingual-knowledge-transfer"},{"title":"Article Not peer-reviewed version Opportunities and Challenges of Natural","url":"https://www.preprints.org/manuscript/202601.1124/v1/download"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"Cross-Lingual Transfer of Cultural Knowledge","url":"https://aclanthology.org/2025.acl-short.13.pdf"},{"title":"Proceedings of the 5th Workshop on Multilingual Representation Learning (MRL 2025) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.mrl-main/"},{"title":"One Model, Many Worlds: Cross-Lingual Fine-Tuning Can Improve","url":"https://openreview.net/attachment?id=9MDdSocwIs&name=pdf"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Culturally Aware and Adapted NLP: A Taxonomy and a Survey of the State of the Art | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00760/131587/Culturally-Aware-and-Adapted-NLP-A-Taxonomy-and-a"}]

Based on the search results, here's what I found about cross-lingual fine-tuning and cultural knowledge in 2025-2026:

## Recent Research Focus

Recent research is fine-tuning multilingual Transformer models to capture both linguistic and contextual nuances through transfer learning from high-resource languages, improving translation quality for low-resource languages.

## Cross-Cultural NLP Initiatives

The 4th Workshop on Cross-Cultural Considerations in NLP (C3NLP) is being co-located with ACL 2026 in San Diego. The research agenda focuses on: understanding how global cultures and NLP technologies intersect, detecting and mitigating cultural biases and harms in ways that reflect local cultures and values, and building more cross-culturally competent NLP systems.

## Key Challenges and Solutions

For cultural knowledge, there is a frequency-driven asymmetry: high-resource languages and English exhibit bidirectional transfer, while low-resource languages "leak" knowledge to English but not vice versa.

Selective adaptation via language adapters—trainable modules plugged into frozen multilingual backbones—enables parameter-efficient transfer, which is crucial when task-specific linguistic nuances would be blurred by direct translation.

## Cultural Awareness in Language Models

Machine translations often lack quality and cultural nuance while incurring significant costs for data curation and training. Recent work compares LLM-assisted stories prompted with cultural cues, machine translation from benchmarks, and native-written stories, finding that LLM stories match natives on cultural fidelity but lag in coherence and correctness.

Parameter-Efficient Fine-Tuning (PEFT) methods have shown success in cross-lingual transfer learning and could prove important for cultural adaptations beyond dialects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae4d327a-4d2d-47c7-b746-49b395413539",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "87f07fc1-fffa-49ef-88e2-d7f77f7fd1dc",
  "sourceToolAssistantUUID": "ae4d327a-4d2d-47c7-b746-49b395413539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T08:09:01.383Z_

<details><summary>↩ Tool result · `toolu_01LXAeLAAViNoLuSfyesqvvX`</summary>

```text
Web search results for query: "arXiv 2510.08284 Yamamoto cultural understanding neurons ICLR 2026"

Links: [{"title":"[2510.08284] Neuron-Level Analysis of Cultural Understanding in Large Language Models","url":"https://arxiv.org/abs/2510.08284"},{"title":"Neuron-Level Analysis of Cultural Understanding in Large Language Models","url":"https://arxiv.org/html/2510.08284"},{"title":"Neuron-Level Analysis of Cultural Understanding in Large ...","url":"https://arxiv.org/pdf/2510.08284"},{"title":"Finding Culture-Sensitive Neurons in Vision-Language Models","url":"https://arxiv.org/html/2510.24942v2"},{"title":"Computation and Language 2025","url":"https://www.arxiv.org/list/cs.CL/2025?skip=13725&show=2000"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"Under review as a conference paper at ICLR 2026","url":"https://www.arxiv.org/pdf/2509.21798"},{"title":"Neural cyberattacks applied to the vision under realistic visual stimuli","url":"https://arxiv.org/html/2503.08284"},{"title":"[2503.08284] Neural cyberattacks applied to the vision under realistic visual stimuli","url":"https://arxiv.org/abs/2503.08284"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/4a5f5ca770673ab914afaf68cdc1cab1e2be36ef.pdf"}]

Based on the search results, I found information about the paper arXiv 2510.08284:

**Title:** Neuron-Level Analysis of Cultural Understanding in Large Language Models

**Authors:** Taisei Yamamoto from The University of Tokyo and Riken, along with Ryoma Kumon, Danushka Bollegala, and Hitomi Yanaka

**Main Findings:**

The research identifies both culture-general neurons contributing to cultural understanding regardless of cultures, and culture-specific neurons tied to an individual culture, which account for less than 1% of all neurons and are concentrated in shallow to middle MLP layers.

**Research Approach:**

The paper conducts a neuron-level analysis to identify neurons that drive cultural behavior, introducing a gradient-based scoring method with additional filtering for precise refinement.

**Validation:**

Suppressing these neurons substantially degrades performance on cultural benchmarks (by up to 30%).

The paper was posted to arXiv on October 9, 2025, and updated on March 29, 2026. However, I didn't find specific information in the search results confirming it was accepted to or published at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d18f020-8ebb-491d-a26b-6201aa815335",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "d59572e2-5e93-40bc-9f00-5c49f550be7b",
  "sourceToolAssistantUUID": "6d18f020-8ebb-491d-a26b-6201aa815335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T08:09:02.852Z_

Let me do a few more searches to check for additional competing work:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d59572e2-5e93-40bc-9f00-5c49f550be7b",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYh9zS2uChFMpCkbdqB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9c815d9-2111-4b21-8907-6061ea028823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J5ZQooqN4e6mn9V5LRtSKQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 22740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
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

_source line 25 · 2026-05-10T08:09:03.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SartXdvN16b7dPu2owNqH7`</summary>

```json
{
  "query": "arXiv 2510.26024 Han Agrawal Briakou surgical steering cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c815d9-2111-4b21-8907-6061ea028823",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYh9zS2uChFMpCkbdqB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8a00b158-2903-43e7-9b1f-1688884abea1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J5ZQooqN4e6mn9V5LRtSKQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 22740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
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

_source line 26 · 2026-05-10T08:09:03.471Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J5En5H8JuuRo486mYUKmJF`</summary>

```json
{
  "query": "probing multilingual layers cultural knowledge LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a00b158-2903-43e7-9b1f-1688884abea1",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYh9zS2uChFMpCkbdqB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "db4fc9bf-ab21-49ca-bac4-0ae61aece0cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J5ZQooqN4e6mn9V5LRtSKQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 22740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3887,
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

_source line 27 · 2026-05-10T08:09:03.697Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4oN8vBFuh5HsD1bWXW4Lt`</summary>

```json
{
  "query": "instruction fine-tuning multilingual cultural representation erasure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4fc9bf-ab21-49ca-bac4-0ae61aece0cd",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYh9zS2uChFMpCkbdqB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d0cc30c7-0acb-496f-8f8d-5568fb3d3585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J5ZQooqN4e6mn9V5LRtSKQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 823,
      "cache_creation_input_tokens": 3887,
      "cache_read_input_tokens": 22740,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 823,
          "output_tokens": 183,
          "cache_read_input_tokens": 22740,
          "cache_creation_input_tokens": 3887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3887,
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

_source line 28 · 2026-05-10T08:09:08.645Z_

<details><summary>↩ Tool result · `toolu_01SartXdvN16b7dPu2owNqH7`</summary>

```text
Web search results for query: "arXiv 2510.26024 Han Agrawal Briakou surgical steering cross-lingual"

Links: [{"title":"[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/abs/2510.26024"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF","url":"https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"},{"title":"Cross-Lingual Activation Steering for Multilingual Language Models","url":"https://arxiv.org/html/2601.16390v1"},{"title":"Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models","url":"https://arxiv.org/html/2502.15639v1"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/pdf/2602.02326"},{"title":"Cross-Lingual Stability and Bias in Instruction-Tuned Language","url":"https://arxiv.org/pdf/2510.22823"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview","url":"https://openreview.net/forum?id=8DBHkEe0sm"},{"title":"CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark","url":"https://arxiv.org/html/2601.08331v1"},{"title":"[2510.00908] Bridging Language Gaps: Advances in Cross-Lingual Information Retrieval with Multilingual LLMs","url":"https://arxiv.org/abs/2510.00908"},{"title":"A Comparative Analysis of Sparse Autoencoder and Activation Difference in Language Model Steering","url":"https://arxiv.org/html/2510.01246v1"}]

Based on the search results, I found the paper you're looking for:

arXiv paper 2510.26024 is titled "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs" by HyoJung Han, Sweta Agrawal, and Eleftheria Briakou.

The paper examines cross-lingual alignment (CLA), which aims to align multilingual representations to enable Large Language Models to transfer knowledge across languages, but hypothesizes that this pursuit of representational convergence can inadvertently cause "cultural erasure"—the functional loss of providing culturally-situated responses that should diverge based on the query language.

The authors introduce a holistic evaluation framework called the transfer-localization plane to quantify both desirable knowledge transfer and undesirable cultural erasure, and using this framework, they re-evaluate recent CLA approaches and find that they consistently improve factual transfer at the direct cost of cultural localization across all six languages studied. Their investigation into the internal representations reveals that universal factual transfer and culturally-specific knowledge are optimally steerable at different levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a00b158-2903-43e7-9b1f-1688884abea1",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "19b423d0-e394-4031-abc9-2e5ab1a4a189",
  "sourceToolAssistantUUID": "8a00b158-2903-43e7-9b1f-1688884abea1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T08:09:09.447Z_

<details><summary>↩ Tool result · `toolu_01J5En5H8JuuRo486mYUKmJF`</summary>

```text
Web search results for query: "probing multilingual layers cultural knowledge LLM 2025"

Links: [{"title":"Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models While Enhancing Native Performance","url":"https://arxiv.org/html/2504.09753"},{"title":"Multilingual LLM Evaluation","url":"https://www.emergentmind.com/topics/multilingual-evaluation-of-large-language-models"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"INCLUDE: EVALUATING MULTILINGUAL LANGUAGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf"},{"title":"Improving Multilingual Capabilities with Cultural and Local Knowledge in Large Language Models While Enhancing Native Performance - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.189/"},{"title":"Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages","url":"https://neulab.github.io/Pangea/"},{"title":"Exploring Multilingual Probing in Large Language Models","url":"https://aclanthology.org/anthology-files/anthology-files/pdf/xllm/2025.xllm-1.7.pdf"},{"title":"Analyzing LLMs' Knowledge Boundary Cognition Across ...","url":"https://aclanthology.org/2025.acl-long.1174.pdf"},{"title":"BRIDGING THE GAPS IN MULTILINGUAL REASONING","url":"https://openreview.net/pdf?id=Q5mkmW0cUD"},{"title":"Language over Content: Tracing Cultural Understanding in Multilingual Large Language Models","url":"https://arxiv.org/html/2510.16565"}]

Based on the search results, I found several relevant 2025 research papers related to probing multilingual layers and cultural knowledge in Large Language Models:

## Key Research Findings

**Probing Multilingual Representations:**

Research has examined layer-wise probing accuracy of open-source LLMs across 16 languages, and interpretability-oriented evaluation includes probing internal model representations, neuron activation, and alignment with intended behavior across languages.

**Cultural Knowledge in Multilingual Models:**

Since LLMs acquire cultural knowledge from diverse language sources during pretraining, linguistic and cultural signals are often intertwined, and most evaluations of cultural understanding have focused only on final outputs, obscuring the factors driving differences in responses.

Internal path overlap is greater for same-language, cross-country questions than for cross-language, same-country questions, indicating that multilingual LLMs rely heavily on language-specific circuits when representing and applying cultural knowledge.

**Benchmarks and Evaluation Methods:**

Ensuring equitable language support, cultural sensitivity, safety, and robust cross-lingual reasoning in LLMs requires a multifaceted approach combining linguistic, functional, cultural, and safety-oriented evaluation methods.

Recent benchmarks specifically include questions encompassing regional and cultural knowledge of diverse languages, with examinations collected from local sources in 52 countries.

The research shows growing attention to understanding how LLMs process and represent cultural knowledge across multiple languages, particularly through interpretability analysis of internal model layers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db4fc9bf-ab21-49ca-bac4-0ae61aece0cd",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "eedf38c1-9dd4-4a71-8949-c7b7f735900e",
  "sourceToolAssistantUUID": "db4fc9bf-ab21-49ca-bac4-0ae61aece0cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T08:09:11.171Z_

<details><summary>↩ Tool result · `toolu_01V4oN8vBFuh5HsD1bWXW4Lt`</summary>

```text
Web search results for query: "instruction fine-tuning multilingual cultural representation erasure"

Links: [{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | Request PDF","url":"https://www.researchgate.net/publication/397089048_Rethinking_Cross-lingual_Alignment_Balancing_Transfer_and_Cultural_Erasure_in_Multilingual_LLMs"},{"title":"Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/pdf/2510.26024"},{"title":"[2510.26024] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://arxiv.org/abs/2510.26024"},{"title":"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs | OpenReview","url":"https://openreview.net/forum?id=8DBHkEe0sm"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/abfa92cdcf181286524673db4ccf7335b915639f.pdf"},{"title":"M-DaQ: Retrieving Samples with Multilingual Diversity and Quality for Instruction Fine-Tuning Datasets","url":"https://arxiv.org/html/2509.15549"},{"title":"Final Report - Fine Tuning Methods for Low-resource Languages","url":"https://arxiv.org/html/2510.04139v1"},{"title":"Fine-Tuning LLMs for Multilingual Domains - Ghost","url":"https://latitude-blog.ghost.io/blog/fine-tuning-llms-for-multilingual-domains/"},{"title":"[2509.15549] M-DaQ: Retrieving Samples with Multilingual Diversity and Quality for Instruction Fine-Tuning Datasets","url":"https://arxiv.org/abs/2509.15549"},{"title":"[Literature Review] Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs","url":"https://www.themoonlight.io/en/review/rethinking-cross-lingual-alignment-balancing-transfer-and-cultural-erasure-in-multilingual-llms"}]

I've found substantial research on this topic. Here's what the search results reveal:

## Key Research Findings

### Cultural Erasure in Cross-Lingual Alignment

The pursuit of representational convergence in multilingual LLMs can inadvertently cause "cultural erasure," the functional loss of providing culturally-situated responses that should diverge based on the query language.

### The Core Trade-Off

Recent cross-lingual alignment approaches consistently improve factual transfer at the direct cost of cultural localization across all six languages studied. This presents a critical tension: for a question like "What is the emergency number?" representational alignment may cause the model to default to "911" regardless of the query language.

### How This Happens

Knowledge is primarily encoded in high-resource languages like English, which dominate pre-training corpora. LLMs process multilingual inputs by mapping them to a shared, language-agnostic semantic space—one that is often heavily biased towards English—before translating them back to the target language for the final output.

### Proposed Solutions

Universal factual transfer and culturally-specific knowledge are optimally steerable at different model layers. A novel inference-time method called "Surgical Steering" uses targeted activation steering to distinct layers and achieves a better balance between the two competing dimensions.

### Data-Driven Approaches

Multilingual instruction fine-tuning empowers LLMs to generalize across diverse linguistic and cultural contexts. M-DaQ is a diversity-aware sampling framework that jointly optimizes instruction-response quality and cross-lingual semantic diversity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0cc30c7-0acb-496f-8f8d-5568fb3d3585",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "66790e2c-c795-4bf0-8ce4-04e6a9f39b4f",
  "sourceToolAssistantUUID": "d0cc30c7-0acb-496f-8f8d-5568fb3d3585",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T08:09:13.231Z_

Now let me search for one more angle - recent probing work and layer-level analysis papers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66790e2c-c795-4bf0-8ce4-04e6a9f39b4f",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYhsqcRfx1E5qz8R3BE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4aea8693-1132-4074-8e6b-f732d3a163db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JqeoJTPdvG48LvfSqAE78U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3713,
      "cache_read_input_tokens": 26627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3713,
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

_source line 32 · 2026-05-10T08:09:13.731Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KnHu7oonpxZDczzQq3zRLZ`</summary>

```json
{
  "query": "\"layer probing\" multilingual LLM cultural 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aea8693-1132-4074-8e6b-f732d3a163db",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYhsqcRfx1E5qz8R3BE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "54a3cdee-74cc-4ecf-be0b-e0be91fe9290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JqeoJTPdvG48LvfSqAE78U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3713,
      "cache_read_input_tokens": 26627,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 136,
          "cache_read_input_tokens": 26627,
          "cache_creation_input_tokens": 3713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3713,
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

_source line 33 · 2026-05-10T08:09:13.737Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EXPcH3YtxoHFcxND4o7nwF`</summary>

```json
{
  "query": "EMNLP 2026 multilingual cultural knowledge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54a3cdee-74cc-4ecf-be0b-e0be91fe9290",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYhsqcRfx1E5qz8R3BE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6931f805-3d0f-4b61-912b-c91d95cc0ea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JqeoJTPdvG48LvfSqAE78U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3713,
      "cache_read_input_tokens": 26627,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 136,
          "cache_read_input_tokens": 26627,
          "cache_creation_input_tokens": 3713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3713,
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

_source line 34 · 2026-05-10T08:09:20.652Z_

<details><summary>↩ Tool result · `toolu_01EXPcH3YtxoHFcxND4o7nwF`</summary>

```text
Web search results for query: "EMNLP 2026 multilingual cultural knowledge"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures","url":"https://arxiv.org/html/2605.02601"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026: Conference on Empirical Methods in Natural Language Processing","url":"https://www.myhuiban.com/conference/424?lang=en_us"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Empirical Methods in Natural Language Processing - Wikipedia","url":"https://en.wikipedia.org/wiki/Empirical_Methods_in_Natural_Language_Processing"},{"title":"Empirical Methods in Natural Language 2026 | WorkWander","url":"https://workwander.tech/conference/emnlp_2026.html"},{"title":"Towards Cross-Cultural Machine Translation with Retrieval ...","url":"https://aclanthology.org/2024.emnlp-main.914.pdf"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"}]

I found relevant information about EMNLP 2026 and multilingual cultural knowledge. Here are the key findings:

## EMNLP 2026 Conference Overview

EMNLP 2026 will be held in Budapest, Hungary, and the main conference is scheduled for October 22-26, 2026.

## Relevant Topics

EMNLP 2026 includes relevant topics such as Computational Social Science and Cultural Analytics, Multilingualism and Cross-Lingual NLP, which directly relate to multilingual cultural knowledge research.

## SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures

A particularly relevant initiative is the BLEND benchmark for LLMs on everyday knowledge in diverse cultures and languages. This task appears to be a major focus for exploring multilingual cultural knowledge at the conference.

Multiple teams have implemented approaches like Retrieval-Augmented Generation (RAG) architectures for cross-lingual cultural question answering, with systems that parse queries to identify target regions, question types, and semantic intent. Other approaches include multi-agent frameworks based on continent-level debate architectures that leverage culture-specific performance differences.

This indicates that EMNLP 2026 has a strong focus on handling cultural nuances and knowledge across multiple languages and regions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6931f805-3d0f-4b61-912b-c91d95cc0ea9",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "b376d4ba-be4d-46d1-8fdb-a45e3cec77cf",
  "sourceToolAssistantUUID": "6931f805-3d0f-4b61-912b-c91d95cc0ea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T08:09:22.367Z_

<details><summary>↩ Tool result · `toolu_01KnHu7oonpxZDczzQq3zRLZ`</summary>

```text
Web search results for query: ""layer probing" multilingual LLM cultural 2025 2026"

Links: [{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"MME 2026 Workshop on Multilingual and Multicultural Evaluation","url":"https://aclanthology.org/2026.mme-main.pdf"},{"title":"GitHub - tjunlp-lab/Awesome-Multilingual-LLMs-Papers: Awesome-Multilingual-LLMs-Papers · GitHub","url":"https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers"},{"title":"A survey of multilingual large language models: Patterns","url":"https://www.cell.com/patterns/fulltext/S2666-3899(24)00290-3"},{"title":"[COLING Workshop] The 2nd Workshop on Scaling Up Multilingual & Multi-Cultural Evaluation | ACL Member Portal","url":"https://www.aclweb.org/portal/content/coling-workshop-2nd-workshop-scaling-multilingual-multi-cultural-evaluation"},{"title":"BRIDGING THE GAPS IN MULTILINGUAL REASONING","url":"https://openreview.net/pdf?id=Q5mkmW0cUD"},{"title":"Multilingual LLM Evaluation","url":"https://www.emergentmind.com/topics/multilingual-evaluation-of-large-language-models"},{"title":"Whose morality do they speak? Unraveling cultural bias in multilingual language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949719125000482"},{"title":"Mind the Gap! Choice Independence in Using Multilingual LLMs for Persuasive Co-Writing Tasks in Different Languages | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3706598.3713201"},{"title":"A survey of multilingual large language models - PMC - NIH","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11783891/"}]

I've performed the web search for "layer probing" multilingual LLM cultural 2025 2026. Here's a summary of the relevant findings:

## Research on Multilingual LLM Cultural Understanding (2025-2026)

The search results reveal significant activity in evaluating and understanding multilingual LLMs across cultural contexts:

### Key Research Areas:

**Multilingual and Multicultural Evaluation:**
While large language models are reshaping language technology across language and cultural barriers, the MME workshop was established to tackle evaluation issues by creating a dedicated venue for multilingual evaluation resources and metrics, standardizing practices, and integrating cultural and social perspectives into NLP and LLM evaluation.

**Probing and Analysis of Multilingual Models:**
Topics of interest at SUMEval 2025 include probing and analysis of multilingual models across cultures and languages. Additionally, intrinsic, representation, and interpretability-oriented evaluation focuses on probing internal model representations, neuron activation, and alignment with intended behavior across languages.

**Cultural Knowledge Assessment:**
Recent work examines how multilingual LLMs handle cultural reasoning. Despite recent progress in multilingual LLMs, their ability to perform factual reasoning across cultural contexts remains largely unevaluated.

**Moral and Cultural Values:**
Research investigates whether multilingual LLMs, such as GPT-3.5-Turbo, GPT-4o-mini, Llama 3.1, and MistralNeMo, reflect culturally specific moral values or impose dominant moral norms, particularly those rooted in English.

The research landscape indicates growing emphasis on understanding how different layers and components of multilingual LLMs encode and process cultural knowledge across languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54a3cdee-74cc-4ecf-be0b-e0be91fe9290",
  "isSidechain": true,
  "promptId": "ce95bc74-2e54-4cca-835d-11219d9cc9a8",
  "agentId": "ab12362edb9b13554",
  "type": "user",
  "uuid": "19dffe90-cfb4-43ce-b25d-c0ac53c29f82",
  "sourceToolAssistantUUID": "54a3cdee-74cc-4ecf-be0b-e0be91fe9290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-10T08:09:48.400Z_

Excellent. Now I have comprehensive information. Let me compile the adversarial review findings.

---

## ADVERSARIAL REVIEW: CLS-LoRA Novelty and Competing Work

Based on systematic searches of recent literature (2025-2026), here are my findings on the landscape of competing work and threats to CLS-LoRA's novelty:

### **1. ArXiv 2602.22475 - "Mind the Gap in Cultural Alignment: Task-Aware Culture Management for Large Language Models"**

**STATUS: CONFIRMED - Direct Competitor**

The paper **does exist** and proposes a very similar solution space:
- **Approach**: Synthesizes task-aware cultural data via LLM-based generators and web search, then fine-tunes lightweight LoRA adapters per culture while keeping the base model frozen
- **Culture Management**: Uses a culture router at inference time to select appropriate adapters based on input cultural context
- **Threat Level**: **VERY HIGH** - This directly overlaps with CLS-LoRA's use of LoRA adapters for cultural preservation. The main difference is task-awareness and modular routing rather than layer-selective freezing during fine-tuning.
- **Venue/Date**: ArXiv 2602.22475 (February 2026)

Sources:
- [Mind the Gap in Cultural Alignment (ArXiv HTML)](https://arxiv.org/html/2602.22475)
- [Mind the Gap in Cultural Alignment (ArXiv PDF)](https://arxiv.org/pdf/2602.22475)

---

### **2. ArXiv 2510.26024 - "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs" (Han, Agrawal & Briakou)**

**STATUS: CONFIRMED - Strong Foundational Work**

**Core Claims Verified**:
- Confirms the exact problem statement CLS-LoRA addresses: cross-lingual alignment erases cultural knowledge
- Introduces the "transfer-localization plane" framework to quantify both knowledge transfer AND cultural erasure
- **KEY FINDING**: "Universal factual transfer and culturally-specific knowledge are optimally steerable at **different model layers**"
- Proposes "Surgical Steering" for inference-time layer-targeted activation steering

**Threat Level**: **CRITICAL** - This paper already empirically validates that cultural knowledge lives in different layers than factual knowledge. CLS-LoRA's core insight (freezing cultural-knowledge layers) is directly anticipated by this work.

**Novelty Gap**: The Han et al. work focuses on inference-time steering via activation manipulation, while CLS-LoRA proposes training-time layer freezing during LoRA fine-tuning. However, the layer-level analysis principle is established.

Sources:
- [Rethinking Cross-lingual Alignment (ArXiv)](https://arxiv.org/abs/2510.26024)
- [Rethinking Cross-lingual Alignment (PDF)](https://arxiv.org/pdf/2510.26024)

---

### **3. ArXiv 2504.10191 - "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models"**

**STATUS: CONFIRMED - Directly Relevant**

**Key Findings**:
- Identifies an "explicit cultural customization vector" conserved across non-English languages
- Uses mechanistic interpretability tools including activation patching and linear steering vectors on relevant layers
- Proposes layer-freezing LoRA fine-tuning for resource efficiency while preserving cultural knowledge

**Threat Level**: **VERY HIGH** - This paper already proposes the exact combination of: (1) identifying cultural layers, (2) layer freezing, and (3) LoRA fine-tuning for cultural preservation. CLS-LoRA appears to be reinventing this approach with the addition of per-layer probing.

Sources:
- [Localized Cultural Knowledge (ArXiv)](https://arxiv.org/abs/2504.10191)
- [Localized Cultural Knowledge (HTML)](https://arxiv.org/html/2504.10191v1)

---

### **4. ArXiv 2510.08284 - "Neuron-Level Analysis of Cultural Understanding in Large Language Models" (Yamamoto et al.)**

**STATUS: CONFIRMED - Relevant Mechanistic Analysis**

**Key Findings**:
- Identifies culture-general neurons and culture-specific neurons (< 1% of all neurons)
- Culture-specific neurons are concentrated in **shallow to middle MLP layers**
- Gradient-based scoring method for precise neuron identification
- Suppressing these neurons degrades cultural benchmark performance by up to 30%

**Threat Level**: **HIGH** - This provides neuron-level validation that cultural knowledge can be precisely localized. However, it's neuron-level, not layer-level. CLS-LoRA's per-layer probing is coarser-grained than this work.

**Note**: Listed as posted October 2025, updated March 2026. Claims of ICLR 2026 acceptance not confirmed in search results.

Sources:
- [Neuron-Level Analysis (ArXiv)](https://arxiv.org/abs/2510.08284)
- [Neuron-Level Analysis (HTML)](https://arxiv.org/html/2510.08284)

---

### **5. ArXiv 2509.11414 - "Continually Adding New Languages to Multilingual Language Models" (LayRA)**

**STATUS: CONFIRMED - Layer-Selective LoRA Precedent**

**Key Technical Approach**:
- Inserts LoRA modules into **selected early layers (first 10)** and **late layers (last 2)** while keeping middle layers frozen
- Addresses catastrophic forgetting in continual multilingual learning
- Based on insight: "Multilingual models encode inputs in source language in initial layers, reason in English in intermediate layers, translate back in final layers"

**Threat Level**: **MEDIUM-HIGH** - LayRA demonstrates that layer-selective LoRA application is effective for multilingual tasks. However, it's designed for continual language addition (preventing forgetting), not cultural preservation during instruction fine-tuning. The layer selection strategy is different (early/late vs. culture-specific middle layers).

**Potential Novelty Claim**: CLS-LoRA focuses on **identifying and freezing culture-implementing layers** during instruction fine-tuning, whereas LayRA uses layer-selective **application** for continual learning. The problem formulations differ.

Sources:
- [LayRA (ArXiv PDF)](https://arxiv.org/pdf/2509.11414)
- [LayRA (ArXiv)](https://arxiv.org/abs/2509.11414)

---

### **6. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762)**

**STATUS: CONFIRMED - Language-Aware Parameter Detection**

**Approach**:
- Evaluates neuron/parameter awareness for both general MT and language-specific tasks
- Uses multiple language-specific LoRA architecture
- Selectively transfers knowledge from teacher to student models

**Threat Level**: **MEDIUM** - MLAS-LoRA also uses language-specific LoRA components, but for multilingual machine translation knowledge distillation. It's not about preserving cultural knowledge during instruction fine-tuning. The problem formulation is different (MT efficiency vs. cultural preservation).

Sources:
- [MLAS-LoRA (ACL Anthology)](https://aclanthology.org/2025.acl-long.762/)

---

### **7. Additional Highly Relevant Papers**

**M-DaQ (ArXiv 2509.15549)** - "Retrieving Samples with Multilingual Diversity and Quality for Instruction Fine-Tuning Datasets"
- Addresses cultural erasure through **data diversity** in instruction fine-tuning
- Threat Level: **MEDIUM** - Complementary approach (data) rather than architecture (layer freezing)

**Language over Content: Tracing Cultural Understanding in Multilingual LLMs**
- Probes how multilingual LLMs process cultural knowledge across layers
- Confirms that cultural understanding relies on language-specific internal circuits
- Threat Level: **MEDIUM** - Provides empirical grounding for layer-level analysis

---

## SYNTHESIS: Critical Novelty Assessment

### **Major Threats to CLS-LoRA's Novelty**

1. **ArXiv 2504.10191** already proposes layer-freezing LoRA for cultural preservation
2. **ArXiv 2510.26024** establishes that cultural and factual knowledge live in different layers
3. **ArXiv 2602.22475** (CultureManager) demonstrates LoRA-based cultural management at scale
4. **ArXiv 2509.11414** (LayRA) proves layer-selective LoRA is effective for multilingual tasks

### **CLS-LoRA's Potential Narrow Novelty**

The main differentiation appears to be:
- **Empirical per-layer probing methodology** to identify cultural-routing vs. factual-transfer layers
- **Fine-tuning-time freezing** (not inference-time steering like Han et al.)
- **Application to instruction fine-tuning** specifically (most other work targets other tasks)

### **Recommendation for EMNLP 2026 Submission**

**CLS-LoRA faces significant novelty challenges:**
- The layer-level analysis of cultural knowledge is well-established (2510.26024, 2504.10191)
- Layer-selective LoRA application to multilingual tasks is established (2509.11414)
- LoRA-based cultural preservation is established (2602.22475)

**The paper needs to clearly articulate:**
1. **Why the probing methodology is novel** beyond existing mechanistic interpretability approaches
2. **Empirical results demonstrating superiority** over CultureManager, surgical steering, and layer-freezing baselines
3. **The specific instruction fine-tuning context** and how it differs from prior cultural preservation work

**Competitive threats ranking:**
1. **CRITICAL**: 2504.10191 (same core approach)
2. **CRITICAL**: 2602.22475 (same domain, published Feb 2026)
3. **HIGH**: 2510.26024 (foundational layer analysis)
4. **MEDIUM-HIGH**: 2509.11414 (layer-selective LoRA methodology)

---

**Sources for this review:**
- [Mind the Gap in Cultural Alignment](https://arxiv.org/abs/2602.22475)
- [Rethinking Cross-lingual Alignment](https://arxiv.org/abs/2510.26024)
- [Localized Cultural Knowledge](https://arxiv.org/abs/2504.10191)
- [Neuron-Level Analysis](https://arxiv.org/abs/2510.08284)
- [LayRA: Continually Adding Languages](https://arxiv.org/abs/2509.11414)
- [MLAS-LoRA](https://aclanthology.org/2025.acl-long.762/)
- [M-DaQ: Diversity in Instruction Fine-tuning](https://arxiv.org/abs/2509.15549)
- [Cross-Lingual Activation Steering](https://arxiv.org/html/2601.16390v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19dffe90-cfb4-43ce-b25d-c0ac53c29f82",
  "isSidechain": true,
  "agentId": "ab12362edb9b13554",
  "requestId": "req_011CatYihjB2KJ2x3goXsk31",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7333279d-7ec8-4641-ad63-034c8706a6bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ca3389b0-ef08-4d6b-8028-f3decd1eae3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NjC7dCCNAWTaq64ctNrXHa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 30340,
      "output_tokens": 2716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 845,
          "output_tokens": 2716,
          "cache_read_input_tokens": 30340,
          "cache_creation_input_tokens": 1122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1122,
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
