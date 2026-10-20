# Research conversation: Search for recent papers (2025-2026) that might compete with or overlap with a proposal to do per-instance routing of re

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9ae3a878aa277851.jsonl`
- **Structured JSON:** [`314aa1e25dd3c38252ae.json`](../../sessions/31/314aa1e25dd3c38252ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-12T00:19:38.340Z_

Search for recent papers (2025-2026) that might compete with or overlap with a proposal to do per-instance routing of retrieval configuration (granularity + context budget) for code repair. Use WebSearch with these queries:

1. "METIS RAG configuration adaptation per query 2025"
2. "BEST-Route LLM routing sampling ICML 2025"
3. "LTRR learning to rank retrievers SIGIR 2025"
4. "RouteLLM preference data routing ICLR 2025"
5. "adaptive context selection software engineering agents 2026"
6. "SWE-bench retrieval optimization 2026"

Report any papers found with titles, venues, and relevance to per-instance retrieval configuration routing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "a9ae3a878aa277851",
  "type": "user",
  "uuid": "6983e221-87fe-4328-9420-7f7cecb5a69f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-12T00:19:40.173Z_

I'll search for papers on per-instance routing and retrieval configuration that might compete with your proposal. Let me run these queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6983e221-87fe-4328-9420-7f7cecb5a69f",
  "isSidechain": true,
  "agentId": "a9ae3a878aa277851",
  "requestId": "req_011CawiWy8UP2XNanrAQRGnB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "34c7d819-8ea4-4c4c-8778-6ac13d2c5cf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EyebsfMSQZ1FSZiCG7FnzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 600,
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

_source line 3 · 2026-05-12T00:19:40.554Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FubyxSugMLd4zLs9bv2yqK`</summary>

```json
{
  "query": "METIS RAG configuration adaptation per query 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c7d819-8ea4-4c4c-8778-6ac13d2c5cf5",
  "isSidechain": true,
  "agentId": "a9ae3a878aa277851",
  "requestId": "req_011CawiWy8UP2XNanrAQRGnB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15e90354-0695-4c3a-822c-b367de3ae28d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EyebsfMSQZ1FSZiCG7FnzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 600,
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

_source line 4 · 2026-05-12T00:19:40.943Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EkUTN2PD4UgrgR2j9Pofbx`</summary>

```json
{
  "query": "BEST-Route LLM routing sampling ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15e90354-0695-4c3a-822c-b367de3ae28d",
  "isSidechain": true,
  "agentId": "a9ae3a878aa277851",
  "requestId": "req_011CawiWy8UP2XNanrAQRGnB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "667e6564-4aa5-43b1-b4e2-4d198edc417e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EyebsfMSQZ1FSZiCG7FnzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 600,
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

_source line 5 · 2026-05-12T00:19:41.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TzHXc6KCUvVhJX69QNffuv`</summary>

```json
{
  "query": "LTRR learning to rank retrievers SIGIR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "667e6564-4aa5-43b1-b4e2-4d198edc417e",
  "isSidechain": true,
  "agentId": "a9ae3a878aa277851",
  "requestId": "req_011CawiWy8UP2XNanrAQRGnB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e4e9b4ba-f0f4-4b02-ade6-ab84dbc81e70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EyebsfMSQZ1FSZiCG7FnzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 600,
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

_source line 6 · 2026-05-12T00:19:41.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CHA2Z1MsXZeC3yA4eSMgtH`</summary>

```json
{
  "query": "RouteLLM preference data routing ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4e9b4ba-f0f4-4b02-ade6-ab84dbc81e70",
  "isSidechain": true,
  "agentId": "a9ae3a878aa277851",
  "requestId": "req_011CawiWy8UP2XNanrAQRGnB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c8f6ba76-50e1-4356-bfdb-c88a2237d56c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EyebsfMSQZ1FSZiCG7FnzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 600,
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

_source line 7 · 2026-05-12T00:19:41.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019XzqnMbZFaTtwJPDuN1SPg`</summary>

```json
{
  "query": "adaptive context selection software engineering agents 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8f6ba76-50e1-4356-bfdb-c88a2237d56c",
  "isSidechain": true,
  "agentId": "a9ae3a878aa277851",
  "requestId": "req_011CawiWy8UP2XNanrAQRGnB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2925b82b-cda6-4550-b7c0-e0be1b31194f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EyebsfMSQZ1FSZiCG7FnzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 600,
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

_source line 8 · 2026-05-12T00:19:41.285Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014jQQFSvLLSdCrAQm5tFBKF`</summary>

```json
{
  "query": "SWE-bench retrieval optimization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2925b82b-cda6-4550-b7c0-e0be1b31194f",
  "isSidechain": true,
  "agentId": "a9ae3a878aa277851",
  "requestId": "req_011CawiWy8UP2XNanrAQRGnB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8cef1f5e-4b94-4e66-8077-7ad5bfa19217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EyebsfMSQZ1FSZiCG7FnzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 600,
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

_source line 9 · 2026-05-12T00:19:46.447Z_

<details><summary>↩ Tool result · `toolu_01CHA2Z1MsXZeC3yA4eSMgtH`</summary>

```text
Web search results for query: "RouteLLM preference data routing ICLR 2025"

Links: [{"title":"ICLR Poster RouteLLM: Learning to Route LLMs from Preference Data","url":"https://iclr.cc/virtual/2025/poster/30737"},{"title":"RouteLLM: Learning to Route LLMs from Preference Data | OpenReview","url":"https://openreview.net/forum?id=8sSqNntaMr"},{"title":"RouteLLM: Learning to Route LLMs from Preference Data","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html"},{"title":"[2406.18665] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/pdf/2406.18665"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data | Weaviate","url":"https://weaviate.io/papers/routellm"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=rEqETC88RY"},{"title":"RouteLLM: Learning to Route LLMs from Preference Data | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/8sSqNntaMr@OpenReview"},{"title":"dblp: RouteLLM: Learning to Route LLMs from Preference Data.","url":"https://dblp.org/rec/conf/iclr/OngAWC0GKS25.html"}]

Based on the search results, here's what I found about RouteLLM at ICLR 2025:

## RouteLLM: Learning to Route LLMs from Preference Data

RouteLLM introduces a training framework for learning efficient router models that dynamically select between a stronger and weaker LLM during inference. The framework leverages human preference data and employs data augmentation techniques to enhance performance.

### Key Results

Evaluations on public benchmarks show that the approach can reduce costs by over 2 times without sacrificing response quality. The routers exhibit strong generalization capabilities, maintaining performance even when routing between LLMs not included in training.

### Authors

The paper is authored by Isaac Ong, Amjad Almahairi, Vincent Wu, Wei-Lin Chiang, Tianhao Wu, Joseph E. Gonzalez, M. Waleed Kadous, and Ion Stoica, and was published at ICLR 2025.

The paper was presented as a poster at ICLR 2025 and addresses the fundamental trade-off between model performance and computational cost in deploying large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8f6ba76-50e1-4356-bfdb-c88a2237d56c",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "a9ae3a878aa277851",
  "type": "user",
  "uuid": "4babf5dd-b7ce-49e1-8a4c-f6cc8a125b98",
  "sourceToolAssistantUUID": "c8f6ba76-50e1-4356-bfdb-c88a2237d56c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T00:19:47.603Z_

<details><summary>↩ Tool result · `toolu_01FubyxSugMLd4zLs9bv2yqK`</summary>

```text
Web search results for query: "METIS RAG configuration adaptation per query 2025"

Links: [{"title":"METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation","url":"https://arxiv.org/pdf/2412.10543"},{"title":"[2412.10543] METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation","url":"https://arxiv.org/abs/2412.10543"},{"title":"[2412.10543v3] METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation","url":"https://arxiv.org/abs/2412.10543v3"},{"title":"METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/metis-fast-quality-aware-rag-systems-with-configuration-adaptation/"},{"title":"METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation (TR) - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/metis-fast-quality-aware-rag-systems-with-configuration-adaptation-tr/"},{"title":"METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation | Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles","url":"https://dl.acm.org/doi/10.1145/3731569.3764855"},{"title":"dblp: METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation.","url":"https://dblp.org/rec/conf/sosp/Ray0GDFANJ25.html"},{"title":"METIS: Quality-Aware RAG with Configuration Adaptation and Scheduling - YouTube","url":"https://www.youtube.com/watch?v=Ta-wOU3YJB8"},{"title":"METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation | Request PDF","url":"https://www.researchgate.net/publication/396443172_METIS_Fast_Quality-Aware_RAG_Systems_with_Configuration_Adaptation"},{"title":"Towards Automatically Optimizing Retrieval Augmented AI Systems Melissa Z. Pan1","url":"https://openreview.net/pdf/cf38ba6dea6e8b7c2cb7d989235789c656c500f7.pdf"}]

Based on the search results, here's what I found about METIS RAG configuration adaptation per query:

## Overview

METIS is the first RAG system that jointly schedules queries and adapts the key RAG configurations of each query, such as the number of retrieved text chunks and synthesis methods, in order to balance quality optimization and response delay reduction.

## Key Approach

METIS reduces RAG response delays by jointly deciding the per-query configuration and query scheduling based on available resources. The system uses query profiling to understand the characteristics of each query and adapt configurations accordingly.

Query profiles can effectively filter out undesirable RAG configurations. For example, for a query that involves at least three separate pieces of information, the estimated profile would suggest that the number of chunks (one of the configuration knobs) should be at least three.

## Performance Results

Compared with state-of-the-art RAG optimization schemes, METIS reduces the generation latency by 1.64-2.54× without sacrificing generation quality.

## Publication

The paper was published at SOSP 2025 (ACM SIGOPS 31st Symposium on Operating Systems Principles) in October 2025 by Siddhant Ray and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15e90354-0695-4c3a-822c-b367de3ae28d",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "a9ae3a878aa277851",
  "type": "user",
  "uuid": "9f80f05f-b45e-4c77-a197-abeed814ea18",
  "sourceToolAssistantUUID": "15e90354-0695-4c3a-822c-b367de3ae28d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T00:19:48.006Z_

<details><summary>↩ Tool result · `toolu_014jQQFSvLLSdCrAQm5tFBKF`</summary>

```text
Web search results for query: "SWE-bench retrieval optimization 2026"

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Lite","url":"https://www.swebench.com/lite.html"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"SWE-bench February 2026 leaderboard update","url":"https://simonwillison.net/2026/Feb/19/swe-bench/"},{"title":"SWE-Bench 2026: Claude Opus 4.7 Wins 87.6% vs GPT-5.3 85.0% - TokenMix Blog","url":"https://tokenmix.ai/blog/swe-bench-2026-claude-opus-4-7-wins"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 Leaderboard","url":"https://www.morphllm.com/swe-benchmark"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"}]

Based on the search results, here's what I found about SWE-bench retrieval optimization in 2026:

## Current State of SWE-bench Benchmarking

SWE-bench Verified was updated as of April 30, 2026, with models being tested on solving production software engineering tasks.

## Key Findings on Retrieval and Scaffolding Optimization

One of the most significant discoveries about SWE-bench in 2026 relates to retrieval optimization. Opus 4.5 scores 45.9% on SEAL but 50.2-55.4% with custom scaffolding, a 4-10 point lift from better context retrieval alone.

Opus 4.5 scores 45.9% on SEAL but 50.2-55.4% with custom scaffolding, a 4-10 point lift from better context retrieval alone. More specifically, when Opus 4.5 jumps from 45.9% (SEAL) to 51.8% (Auggie), that 5.9-point lift comes entirely from better context retrieval and agent design.

## Production Implications

For teams building coding agents, investing in scaffolding (how you retrieve context, manage the context window, and orchestrate tool calls) yields higher returns than switching to a marginally better base model.

The research suggests that WarpGrep v2 has been added as a search subagent to existing coding agents as one approach to improving retrieval optimization in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cef1f5e-4b94-4e66-8077-7ad5bfa19217",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "a9ae3a878aa277851",
  "type": "user",
  "uuid": "84b5dbc6-1d98-4d33-af3e-26072169b278",
  "sourceToolAssistantUUID": "8cef1f5e-4b94-4e66-8077-7ad5bfa19217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:19:49.625Z_

<details><summary>↩ Tool result · `toolu_01EkUTN2PD4UgrgR2j9Pofbx`</summary>

```text
Web search results for query: "BEST-Route LLM routing sampling ICML 2025"

Links: [{"title":"GitHub - microsoft/best-route-llm: Efficient LLM query routing via multi-sampling. BEST-Route selects both model and number of responses based on query difficulty, cutting costs by up to 60% with <1% performance drop. From the paper:https://arxiv.org/abs/2506.22716 · GitHub","url":"https://github.com/microsoft/best-route-llm"},{"title":"ICML Poster BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute","url":"https://icml.cc/virtual/2025/poster/43788"},{"title":"BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute | OpenReview","url":"https://openreview.net/forum?id=tFBIbCVXkG"},{"title":"best-route-llm/README.md at main · microsoft/best-route-llm","url":"https://github.com/microsoft/best-route-llm/blob/main/README.md"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf"},{"title":"[2506.22716] BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute","url":"https://arxiv.org/abs/2506.22716"},{"title":"RouteLLM: Learning to Route LLMs from Preference Data | OpenReview","url":"https://openreview.net/forum?id=8sSqNntaMr"},{"title":"BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute","url":"https://arxiv.org/html/2506.22716v1"},{"title":"Cost-Aware Contrastive Routing for LLMs Reza Shirkavand","url":"https://openreview.net/pdf?id=4Qe2Hga43N"},{"title":"LLM routing. Compound AI systems combine multiple… | by Jaideep Ray | Better ML | Medium","url":"https://medium.com/better-ml/llm-routing-63e4de34e307"}]

Based on the search results, here's information about BEST-Route and its ICML 2025 publication:

## Overview

BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute (ICML 2025) is a novel routing framework for Large Language Models that focuses on optimizing the cost-quality tradeoff.

## Core Approach

BEST-Route chooses a model and the number of responses to sample from it based on query difficulty and the quality thresholds. The key innovation addresses a limitation in prior routing methods: Prior query routing approaches generate only one response from the selected model and a single response from a small (inexpensive) model was often not good enough to beat a response from a large (expensive) model, however it is well known that for small models, generating multiple responses and selecting the best can enhance quality while remaining cheaper than a single large-model response.

## Key Features

Unlike prior work with static sampling policies, the router adaptively determines the number of samples (and hence the compute allocation) needed for a small model to match the quality of the reference large model at the lowest cost.

## Performance Results

BEST-Route selects both model and number of responses based on query difficulty, cutting costs by up to 60% with <1% performance drop.

## Code and Resources

The implementation is available on GitHub at microsoft/best-route-llm, and the full paper can be accessed on arXiv (2506.22716) and at the ICML 2025 conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "667e6564-4aa5-43b1-b4e2-4d198edc417e",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "a9ae3a878aa277851",
  "type": "user",
  "uuid": "1892ee3b-2997-4da6-8dc8-42da4dcce888",
  "sourceToolAssistantUUID": "667e6564-4aa5-43b1-b4e2-4d198edc417e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:19:49.869Z_

<details><summary>↩ Tool result · `toolu_01TzHXc6KCUvVhJX69QNffuv`</summary>

```text
Web search results for query: "LTRR learning to rank retrievers SIGIR 2025"

Links: [{"title":"GitHub - kimdanny/Starlight-LiveRAG: SIGIR 2025 LiveRAG Spotlight; LTRR: Learning To Rank Retrievers for LLMs","url":"https://github.com/kimdanny/Starlight-LiveRAG"},{"title":"LTRR: Learning To Rank Retrievers for LLMs","url":"https://arxiv.org/html/2506.13743v1"},{"title":"[2506.13743] LTRR: Learning To Rank Retrievers for LLMs","url":"https://arxiv.org/abs/2506.13743"},{"title":"LTRR: Learning To Rank Retrievers for LLMs - Fernando Diaz","url":"https://841.io/doc/ltrr.pdf"},{"title":"[Literature Review] LTRR: Learning To Rank Retrievers for LLMs","url":"https://www.themoonlight.io/en/review/ltrr-learning-to-rank-retrievers-for-llms"},{"title":"Leveraging LLMs for Unsupervised Dense Retriever Ranking | Request PDF","url":"https://www.researchgate.net/publication/382190252_Leveraging_LLMs_for_Unsupervised_Dense_Retriever_Ranking"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=learning-to-rank"},{"title":"GitHub - RUC-NLPIR/GenIR-Survey: [TOIS 2025] This is the official repository for the generative information retrieval survey. · GitHub","url":"https://github.com/RUC-NLPIR/GenIR-Survey"},{"title":"GitHub - ii-research/RAG_Overview: TBA · GitHub","url":"https://github.com/ii-research/RAG_Overview"},{"title":"Learning to Rank with Variable Result Presentation Lengths | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730020"}]

Based on the search results, here's what I found about LTRR (Learning to Rank Retrievers) and SIGIR 2025:

## LTRR: Learning To Rank Retrievers for LLMs

LTRR is a framework that learns to rank retrievers by their expected utility gain to downstream LLM performance, framing routing as a learning-to-rank (LTR) problem.

### Key Research Findings

The research shows that routing-based RAG systems can outperform the best single-retriever-based systems. Performance gains are especially pronounced in models trained with the Answer Correctness (AC) metric and with pairwise learning approaches, especially with XGBoost. Additionally, improvements in generalization to out-of-distribution queries were observed.

### SIGIR 2025 Presentation

The research was presented at the SIGIR 2025 LiveRAG Workshop, where it was selected for a spotlight talk. The team Starlight submitted a RAG system equipped with a pairwise XGBoost-based router to the SIGIR 2025 LiveRAG challenge, achieving a Correctness score of 0.818 and a Faithfulness score of 0.433.

### Paper Details

The research paper is titled "LTRR: Learning To Rank Retrievers for LLMs" by To Eun Kim and Fernando Diaz, and was released on arXiv with identifier 2506.13743. The submitted system demonstrated the practical viability of the approach, achieving competitive performance in both answer correctness and faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4e9b4ba-f0f4-4b02-ade6-ab84dbc81e70",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "a9ae3a878aa277851",
  "type": "user",
  "uuid": "9aa5e0f8-7dc8-445a-8265-2994eddf0940",
  "sourceToolAssistantUUID": "e4e9b4ba-f0f4-4b02-ade6-ab84dbc81e70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:19:52.484Z_

<details><summary>↩ Tool result · `toolu_019XzqnMbZFaTtwJPDuN1SPg`</summary>

```text
Web search results for query: "adaptive context selection software engineering agents 2026"

Links: [{"title":"Context Engineering for Personalization - State Management with Long-Term Memory Notes","url":"https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization"},{"title":"Context Engineering: A Complete Guide & Why It Is Important in 2026","url":"https://codeconductor.ai/blog/context-engineering"},{"title":"AI Agent Engineering in 2026: Architectures, Patterns, and Real-World Systems","url":"https://blog.whoisjsonapi.com/ai-agent-engineering-in-2026-architectures-patterns-and-real-world-systems/"},{"title":"2026 Agentic Coding Trends Report How coding agents are reshaping","url":"https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf"},{"title":"Context Engineering in 2025: The Complete Guide to AI Agent Optimization","url":"https://mem0.ai/blog/context-engineering-ai-agents-guide"},{"title":"An architecture for engineering AI context | InfoWorld","url":"https://www.infoworld.com/article/4139523/an-architecture-for-engineering-ai-context.html"},{"title":"Context Engineering for Coding Agents","url":"https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html"},{"title":"Efficient On-Device Agents via Adaptive Context Management | OpenReview","url":"https://openreview.net/forum?id=TPXVdBjrvU"},{"title":"On a Sandy Beach: Context Engineering for Coding Agents - Fausto's Amsterdam workshop","url":"https://www.blog.ajabbi.com/2026/05/context-engineering-for-coding-agents.html"},{"title":"Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned","url":"https://arxiv.org/html/2603.05344v1"}]

I've completed the web search for "adaptive context selection software engineering agents 2026". Here are the key findings:

## Adaptive Context Selection in Software Engineering Agents (2026)

**Core Concept:**
The Adaptive Context Engine provides the attention and selection layer that determines which parts of memory, along with current data and code, should be surfaced for any given interaction so the AI can act accurately without being overwhelmed.

**Key Mechanisms:**

1. **Context Selection Techniques:**
   Secondary agents operate as context selectors, analyzing the task at hand and determining which files, functions, or documents require full expansion and which can remain summarized or abstracted.

2. **Advanced Memory Architecture:**
   Centrally-Operated Recursively-Expanded Memory (CORE-Memory) addresses the challenge of working with large codebases by creating associative trees of information and automatically analyzes functions, files, and documentation to create hierarchical tags and associations.

3. **Dynamic Optimization:**
   The Adaptive Context Engine is dynamic and self-optimizing, learning from usage patterns, outcomes, and feedback to improve its context selection over time rather than relying on predefined rules.

**Coding Agent Applications:**
The number of options to configure and enrich a coding agent's context has exploded over the past few months, with Claude Code leading the charge in innovations, as powerful context engineering is becoming a huge part of the developer experience.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2925b82b-cda6-4550-b7c0-e0be1b31194f",
  "isSidechain": true,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "agentId": "a9ae3a878aa277851",
  "type": "user",
  "uuid": "75bb367a-83fa-43cd-a6fd-832e0359b091",
  "sourceToolAssistantUUID": "2925b82b-cda6-4550-b7c0-e0be1b31194f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T00:20:03.847Z_

## Summary of Competitive Papers Found (2025-2026)

I found several highly relevant papers that directly compete with or closely overlap your proposal on per-instance routing of retrieval configuration:

### Direct Competitors:

1. **METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation** (SOSP 2025)
   - **Venue:** ACM SIGOPS 31st Symposium on Operating Systems Principles
   - **Relevance:** Direct overlap. METIS jointly schedules queries and adapts RAG configurations per-query, including number of retrieved chunks and synthesis methods. Uses query profiling to determine optimal configurations on a per-query basis. Reports 1.64-2.54× latency reduction without quality loss.
   - **Key Distinction:** Focuses on latency/resource optimization through joint scheduling; your proposal likely emphasizes code repair effectiveness.

2. **LTRR: Learning To Rank Retrievers for LLMs** (SIGIR 2025)
   - **Venue:** SIGIR 2025 LiveRAG Workshop (Spotlight)
   - **Relevance:** Highly relevant. Frames retriever selection as a learning-to-rank problem, with per-query routing decisions based on expected utility to downstream LLM performance. Uses pairwise learning approaches.
   - **Key Distinction:** Focuses on ranking multiple retrievers; your proposal appears to focus on granularity and context budget knobs.

3. **RouteLLM: Learning to Route LLMs from Preference Data** (ICLR 2025)
   - **Venue:** International Conference on Learning Representations (ICLR)
   - **Relevance:** Related but different scope. Routes between stronger/weaker LLMs based on query difficulty using preference data. Achieves 2× cost reduction without quality loss.
   - **Key Distinction:** Routes between models rather than retrieval configurations, though the adaptive per-instance routing framework is similar.

4. **BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute** (ICLR 2025)
   - **Venue:** International Conference on Learning Representations (ICLR) / ICML 2025
   - **Relevance:** Related methodology. Adaptively determines compute allocation (number of samples) per query based on difficulty. Cuts costs up to 60% with <1% performance drop.
   - **Key Distinction:** Routes number of samples to generate rather than retrieval parameters, but uses similar per-instance adaptive allocation.

### Secondary/Related:

5. **Adaptive Context Selection for Software Engineering Agents** (2026)
   - **Findings:** Context engineering for coding agents involves adaptive context selection mechanisms, with research showing that better context retrieval and scaffolding yields 4-10 point improvements in SWE-bench scores.
   - **Relevance:** Tangential. Addresses context management in coding agents but at a higher level than specific retrieval configuration routing.

6. **SWE-bench Retrieval Optimization Trends** (2026)
   - **Finding:** Notable result that custom scaffolding and context retrieval can lift SWE-bench scores by 4-10 points, suggesting high impact of retrieval optimization for code repair tasks.
   - **Relevance:** Demonstrates the problem domain but doesn't propose specific per-instance routing methods.

### Key Competitive Insight:

METIS appears to be the most direct competitor—it's already published at a top-tier venue (SOSP 2025) and tackles per-instance configuration adaptation in RAG systems. However, METIS focuses on general RAG quality/latency tradeoffs and resource scheduling, whereas your proposal appears more specialized to code repair tasks with specific focus on granularity and context budget routing.

Sources:
- [METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation](https://arxiv.org/abs/2412.10543)
- [LTRR: Learning To Rank Retrievers for LLMs](https://arxiv.org/abs/2506.13743)
- [RouteLLM: Learning to Route LLMs from Preference Data](https://arxiv.org/abs/2406.18665)
- [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://arxiv.org/abs/2506.22716)
- [Anthropic 2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75bb367a-83fa-43cd-a6fd-832e0359b091",
  "isSidechain": true,
  "agentId": "a9ae3a878aa277851",
  "requestId": "req_011CawiY1baW8jn1DdjsEhoT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f762237b-1855-45b0-8e15-d7bde159e410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JYvPLKWbiSbtZre7V3wXMa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 5640,
      "cache_read_input_tokens": 16753,
      "output_tokens": 1067,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 845,
          "output_tokens": 1067,
          "cache_read_input_tokens": 16753,
          "cache_creation_input_tokens": 5640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5640,
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
