# Research conversation: I need to verify one specific claim in a research paper for adversarial review. The paper argues that Agentless degrades

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae669b1bb81e25cce.jsonl`
- **Structured JSON:** [`0a8da17b6333ba3ab31b.json`](../../sessions/0a/0a8da17b6333ba3ab31b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

60 recorded events

### User

_source line 1 · 2026-05-10T08:24:13.364Z_

I need to verify one specific claim in a research paper for adversarial review. The paper argues that Agentless degrades from ~50.8% on SWE-bench Verified to ~13.33% on SWE-bench-Live Lite primarily due to "embedding distribution shift" - specifically that the OpenAI text-embedding-3-small model used by Agentless hasn't indexed post-2024 repository structures.

Please search for:
1. "site:arxiv.org SWE-bench-Live 2505.23419" - fetch or search for the actual paper to see if it discusses WHY Agentless degrades so dramatically (4x) from Verified to Live - is it attributed to distribution shift, harder problems, or something else?
2. "Agentless SWE-bench degradation distribution shift embedding" - any papers analyzing why Agentless performs worse on harder/newer benchmarks?
3. "OpenAI text-embedding-3-small out of distribution code retrieval" - any papers documenting this specific embedding model's OOD degradation on code retrieval?
4. Also search: "SWE-bench Verified vs Live difficulty" - any analysis of whether the 4x gap is about problem difficulty vs embedding quality?

I want to know: is the "embedding distribution shift" explanation for the Verified→Live degradation empirically supported, or is it a hypothesis the paper needs to validate?

Use WebSearch and WebFetch to read relevant sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "3f283359-72c1-4c58-b7d4-5eeeb5c85759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T08:24:14.475Z_

I'll help you verify this claim about Agentless's performance degradation. Let me search for the relevant papers and analyses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f283359-72c1-4c58-b7d4-5eeeb5c85759",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZrP8pPa899NSDsKYK5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "324654be-246b-4a42-9fc8-1c323f30425c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0146ZZ8BN5xTt8cLxbs1i9D9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 760,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T08:24:14.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013qNpwZSyKz7T9DbwSo3v4X`</summary>

```json
{
  "query": "site:arxiv.org 2505.23419 SWE-bench-Live Agentless"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "324654be-246b-4a42-9fc8-1c323f30425c",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZrP8pPa899NSDsKYK5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f06a0e79-7ba7-4826-964a-e1929f8da15e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0146ZZ8BN5xTt8cLxbs1i9D9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 760,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T08:24:14.927Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014yqMnxv7D8dJXmf4V3YXAL`</summary>

```json
{
  "query": "Agentless SWE-bench degradation distribution shift embedding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f06a0e79-7ba7-4826-964a-e1929f8da15e",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZrP8pPa899NSDsKYK5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c157bdd-6ee4-453a-8ca9-afb2d55d8a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0146ZZ8BN5xTt8cLxbs1i9D9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 760,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T08:24:15.071Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01538J3vTYktbhEPtCpJgTbm`</summary>

```json
{
  "query": "OpenAI text-embedding-3-small out of distribution code retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c157bdd-6ee4-453a-8ca9-afb2d55d8a92",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZrP8pPa899NSDsKYK5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa2fcb55-a491-4b66-9082-f98598318ec6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0146ZZ8BN5xTt8cLxbs1i9D9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 13791,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 760
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 247,
          "cache_read_input_tokens": 13791,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 760,
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

_source line 6 · 2026-05-10T08:24:15.080Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PBUFCUG4DDTc9pDjRTGaf5`</summary>

```json
{
  "query": "SWE-bench Verified vs Live difficulty comparison analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa2fcb55-a491-4b66-9082-f98598318ec6",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZrP8pPa899NSDsKYK5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5122dfac-1577-4d30-aa30-9f8269f98912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0146ZZ8BN5xTt8cLxbs1i9D9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 13791,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 760
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 247,
          "cache_read_input_tokens": 13791,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 760,
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

_source line 7 · 2026-05-10T08:24:20.250Z_

<details><summary>↩ Tool result · `toolu_01538J3vTYktbhEPtCpJgTbm`</summary>

```text
Web search results for query: "OpenAI text-embedding-3-small out of distribution code retrieval"

Links: [{"title":"text-embedding-3-small Model | OpenAI API","url":"https://developers.openai.com/api/docs/models/text-embedding-3-small"},{"title":"New embedding models and API updates | OpenAI","url":"https://openai.com/index/new-embedding-models-and-api-updates/"},{"title":"Vector embeddings | OpenAI API","url":"https://developers.openai.com/api/docs/guides/embeddings"},{"title":"The guide to text-embedding-3-small | OpenAI","url":"https://zilliz.com/ai-models/text-embedding-3-small"},{"title":"Exploring Text-Embedding-3-Large: A Comprehensive Guide to the new OpenAI Embeddings | DataCamp","url":"https://www.datacamp.com/tutorial/exploring-text-embedding-3-large-new-openai-embeddings"},{"title":"text-embedding-3-large Model | OpenAI API","url":"https://platform.openai.com/docs/models/text-embedding-3-large"},{"title":"OpenAI's Text Embeddings v3 | Pinecone","url":"https://www.pinecone.io/learn/openai-embeddings-v3/"},{"title":"Analyzing Performance Gains in OpenAI's Text-Embedding-3-Small","url":"https://www.pingcap.com/article/analyzing-performance-gains-in-openais-text-embedding-3-small/"},{"title":"Introducing text and code embeddings | OpenAI","url":"https://openai.com/index/introducing-text-and-code-embeddings/"},{"title":"Embeddings FAQ | OpenAI Help Center","url":"https://help.openai.com/en/articles/6824809-embeddings-faq"}]

Based on the search results, I can provide you with information about OpenAI's `text-embedding-3-small` model and its capabilities for code retrieval:

## Overview of text-embedding-3-small

text-embedding-3-small is OpenAI's improved, more performant version of the ada embedding model. It creates embeddings with 1536 dimensions.

## Performance and Use Cases

The text-embedding-3-small is optimized for latency and storage. Compared to other text embedding models like text-embedding-ada-002 and text-embedding-3-large, text-embedding-3-small is the most cost-effective model with improved accuracy and efficiency, and is great for general-purpose vector search applications.

## Code Retrieval Capabilities

The search results indicate that embeddings can be used for code retrieval tasks. Code search models provide code and text embeddings for code search tasks, where the task is to find the relevant code block for a natural language query.

However, the search results don't contain specific information about the out-of-distribution code retrieval performance of `text-embedding-3-small`. For detailed benchmarking data on out-of-distribution code retrieval specifically, you may want to consult OpenAI's technical documentation or research papers that benchmark this model's performance on such specialized tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa2fcb55-a491-4b66-9082-f98598318ec6",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "30c96987-9f99-4ee0-94b0-c4b9c8323c6d",
  "sourceToolAssistantUUID": "aa2fcb55-a491-4b66-9082-f98598318ec6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T08:24:21.736Z_

<details><summary>↩ Tool result · `toolu_013qNpwZSyKz7T9DbwSo3v4X`</summary>

```text
Web search results for query: "site:arxiv.org 2505.23419 SWE-bench-Live Agentless"

Links: [{"title":"[2505.23419] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419"},{"title":"arXiv:2505.23419v2 [cs.SE] 1 Jun 2025 SWE-bench Goes Live! Linghao Zhang","url":"https://arxiv.org/pdf/2505.23419"},{"title":"arXiv:2505.23419v1 [cs.SE] 29 May 2025 SWE-bench Goes Live! Linghao Zhang1∗","url":"https://arxiv.org/pdf/2505.23419v1"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419"},{"title":"LIVE-SWE-AGENT: Can Software Engineering Agents Self-Evolve on the Fly?","url":"https://arxiv.org/pdf/2511.13646"},{"title":"[2505.23419v1] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419v1"},{"title":"Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents","url":"https://arxiv.org/html/2509.23045v2"},{"title":"Paper page - SWE-bench Goes Live!","url":"https://huggingface.co/papers/2505.23419"},{"title":"[2505.23419v2] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419v2"},{"title":"SWE-bench Goes Live! | Request PDF","url":"https://www.researchgate.net/publication/392204506_SWE-bench_Goes_Live"}]

I found the paper! Here's information about arxiv paper 2505.23419 related to SWE-bench-Live and Agentless:

## SWE-bench Goes Live!

The paper presents SWE-bench-Live, a live-updatable benchmark with an initial release consisting of 1,319 tasks derived from real GitHub issues created since 2024, spanning 93 repositories.

### About the Benchmark

SWE-bench-Live facilitates rigorous, contamination-resistant evaluation of LLMs and agents in dynamic, real-world software development settings. While SWE-bench and its variants have become standard in this domain, they suffer from key limitations: they have not been updated since their initial releases, cover a narrow set of repositories, and depend heavily on manual effort for instance construction and environment setup.

### Agentless Evaluation

For Agentless, the paper largely follows the original pipeline, which consists of two main stages: issue localization and patch generation. However, they omit the reranking stage based on regression testing, as supporting this step on SWE-bench-Live would require substantial infrastructure adaptation. Consequently, both the localization and repair stages in their Agentless evaluation produce a single sample without reranking.

### Key Finding

The same agent-LLM pair consistently performs worse on SWE-bench-Live than on SWE-bench, suggesting that existing models may be overfitting to static benchmarks like SWE-bench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f06a0e79-7ba7-4826-964a-e1929f8da15e",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "b6070413-4a2b-46c4-b93c-e6b56b0680a5",
  "sourceToolAssistantUUID": "f06a0e79-7ba7-4826-964a-e1929f8da15e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T08:24:22.380Z_

<details><summary>↩ Tool result · `toolu_014yqMnxv7D8dJXmf4V3YXAL`</summary>

```text
Web search results for query: "Agentless SWE-bench degradation distribution shift embedding"

Links: [{"title":"Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents","url":"https://arxiv.org/html/2509.23045v2"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"GitHub - OpenAutoCoder/Agentless: Agentless🐱: an agentless approach to automatically solve software development problems","url":"https://github.com/OpenAutoCoder/Agentless"},{"title":"Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation","url":"https://arxiv.org/html/2510.08996v1"},{"title":"AGENTLESS : Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/pdf/2407.01489"},{"title":"[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"},{"title":"Kimi-Dev: Agentless Training as Skill Prior for SWE-agents | OpenReview","url":"https://openreview.net/forum?id=tYppHuGhxJ"},{"title":"[2509.23045] Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents","url":"https://arxiv.org/abs/2509.23045"}]

The search results cover several important topics related to your query:

## Key Findings:

**Agentless Approach & SWE-bench:**
Agentless is an agentless approach to automatically solve software development problems following a simple three phase process: localization, repair, and patch validation. It leverages LLM-empowered prompting-based and embedding-based retrieval to perform hierarchical localization.

**Performance & Distribution Shift:**
The mutation of SWE-bench Verified problems from formal GitHub issues to realistic user queries results in a substantial performance degradation across all agent-model combinations, with agents suffering a 20-40% drop in relative success rates compared to baseline.

**Embedding & Distribution Analysis:**
The embeddings corresponding to SWE-Bench C# and telemetry queries make two separate clouds with little to no overlap, but the cloud corresponding to SWE-Bench C#-Mutated has much more overlap with the telemetry query cloud than the original benchmark. OpenAI's text-embedding-3-small model is used to compute embeddings with chunk size of 512 and chunk overlap of 0.

**Degradation in Training:**
The SFT prior exhibits significant degradation with 200 SWE-Agent trajectories, potentially because the trajectories collapse onto a single data mode, leading the SFT prior to overfit through memorization.

The search results highlight how distribution shifts between benchmark formats and real-world scenarios impact model performance, with embedding-based analysis revealing distinct clusters between original and mutated benchmark instances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c157bdd-6ee4-453a-8ca9-afb2d55d8a92",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "28fea108-38a8-4b55-9e91-1c0fcd7ff216",
  "sourceToolAssistantUUID": "9c157bdd-6ee4-453a-8ca9-afb2d55d8a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T08:24:22.450Z_

<details><summary>↩ Tool result · `toolu_01PBUFCUG4DDTc9pDjRTGaf5`</summary>

```text
Web search results for query: "SWE-bench Verified vs Live difficulty comparison analysis"

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"AI Coding Benchmarks: Which Models Actually Deliver? | SpecWeave","url":"https://spec-weave.com/docs/guides/ai-coding-benchmarks/"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-Bench Live Leaderboard Q2 2026: Complete Deep Analysis","url":"https://www.digitalapplied.com/blog/swe-bench-live-leaderboard-q2-2026-analysis"}]

Based on the search results, here's an analysis of the difficulty comparison between SWE-bench Verified and Live:

## Key Differences

**SWE-bench Verified:**

SWE-bench Verified is a human-validated section of the SWE-bench dataset released by OpenAI in August 2024, with each task carefully reviewed and validated by human experts, resulting in a curated set of 500 high-quality test cases. The 'easy' subset is composed of 196 <15-minute fix tasks, while the 'hard' subset is composed of 45 >1-hour tasks.

**Difficulty Characteristics:**
SWE-bench Verified is largely a single-file benchmark, with most fixes touching one file with a few lines changed. This contributes to inflated performance numbers, as top-tier models cluster between sixty and seventy percent on Pro while clearing eighty percent on Verified.

**SWE-bench Live:**

Each month, 50 newly verified, high-quality issues are added to the dataset, while the lite and verified splits remain frozen, ensuring fair leaderboard comparisons. Live represents continuously updated, fresher problem sets compared to the static Verified benchmark.

## Performance Gap Analysis

The difference in model performance is stark. A major finding is the significant drop in performance for all models when moving from the SWE-Bench Verified benchmark to the more challenging SWE-Bench Pro. Additionally, the best model scores 46% on Pro but 81% on Verified, because Verified is contaminated.

A provider that dominates Verified may sit mid-pack on Pro, and the Live ranking shifts as new tasks enter the pool.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5122dfac-1577-4d30-aa30-9f8269f98912",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "076cf4ef-f787-402f-a629-74fc2192ef12",
  "sourceToolAssistantUUID": "5122dfac-1577-4d30-aa30-9f8269f98912",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T08:24:24.167Z_

Now let me fetch the actual paper to read the specific sections about Agentless performance degradation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "076cf4ef-f787-402f-a629-74fc2192ef12",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZs3xvmBTxakqG6v835",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aeb838bc-447e-460d-a214-47c282a28edb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sg4M5ee8kfTgHga8SSYLSR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4431,
      "cache_read_input_tokens": 14551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4431,
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

_source line 12 · 2026-05-10T08:24:25.020Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R3U8yXCUydi1jgPrN2HLUu`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.23419",
  "prompt": "What explanation does the paper give for Agentless's performance degradation from SWE-bench Verified to SWE-bench-Live? Is it attributed to embedding distribution shift, model contamination, problem difficulty, or something else?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeb838bc-447e-460d-a214-47c282a28edb",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZs3xvmBTxakqG6v835",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f6017120-78e5-47af-9eb9-7e212ae2dea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sg4M5ee8kfTgHga8SSYLSR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4431,
      "cache_read_input_tokens": 14551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4431,
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

_source line 13 · 2026-05-10T08:24:25.539Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PGTpBNbhYCFwp6PnrxGxwi`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.23419",
  "prompt": "Agentless performance degradation 50.8% to 13.33% distribution shift embedding post-2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6017120-78e5-47af-9eb9-7e212ae2dea0",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZs3xvmBTxakqG6v835",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "655caa3c-2325-46a6-8819-00af062bca61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sg4M5ee8kfTgHga8SSYLSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4431,
      "cache_read_input_tokens": 14551,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4431
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 245,
          "cache_read_input_tokens": 14551,
          "cache_creation_input_tokens": 4431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4431,
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

_source line 14 · 2026-05-10T08:24:29.252Z_

<details><summary>↩ Tool result · `toolu_01R3U8yXCUydi1jgPrN2HLUu`</summary>

```text
# Agentless Performance Degradation

The paper does not provide a specific explanation for Agentless's individual performance degradation. However, it offers a general explanation for all agents tested.

The authors attribute the overall performance drop across all agent-model combinations to **potential overfitting to SWE-bench itself**. They state: "existing agents may be overfit or implicitly optimized for the SWE-bench repositories," noting that agents performed better on instances from original SWE-bench repositories (22.96% resolved) versus newer repositories (18.89% resolved).

The paper frames this as evidence of **benchmark contamination and static dataset limitations** rather than attributing the degradation to embedding distribution shift or inherent problem difficulty. The core finding is that "existing models may be overfitting to static benchmarks like SWE-bench," which motivates the need for continuously updated benchmarks like SWE-bench-Live.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6017120-78e5-47af-9eb9-7e212ae2dea0",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "ecc4d101-d2b3-4f9f-beef-949f91ef94ab",
  "sourceToolAssistantUUID": "f6017120-78e5-47af-9eb9-7e212ae2dea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T08:24:30.431Z_

<details><summary>↩ Tool result · `toolu_01PGTpBNbhYCFwp6PnrxGxwi`</summary>

```text
# SWE-bench Goes Live! - Document Summary

The document is a research paper titled **"SWE-bench Goes Live!"** by researchers from Microsoft and other institutions. It discusses the evolution and practical deployment of SWE-bench, a benchmark for evaluating AI systems on real software engineering tasks.

## Key Points

**Performance Issues with Agentless Systems:**
The paper addresses performance degradation in agent-based approaches to software engineering tasks. It notes significant distribution shifts occurring post-2024, affecting model embedding effectiveness and real-world applicability.

**Live Benchmark Initiative:**
The authors describe launching a continuously updated version of SWE-bench that adapts to evolving codebases, addressing limitations of static benchmarks that become outdated as repositories change.

**Research Focus:**
The work emphasizes maintaining benchmark relevance through live problem instances, evaluating how AI agents handle authentic, changing software environments rather than frozen snapshots.

**Resources Provided:**
The paper references multiple implementation resources including GitHub repositories and Hugging Face datasets for reproducibility and community engagement.

The research contributes to understanding practical challenges in deploying AI for software engineering at scale, particularly regarding model generalization and performance sustainability over time.

[Binary content (application/pdf, 2.1MB) also saved to /home/ubuntu/.claude-account-3/projects/-/9441f046-d0fc-42fd-a7f5-74a8892b6232/tool-results/webfetch-1778401311553-mipblu.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "655caa3c-2325-46a6-8819-00af062bca61",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "ecaf6e9f-977e-4cee-b74e-778ae36f1b7d",
  "sourceToolAssistantUUID": "655caa3c-2325-46a6-8819-00af062bca61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T08:24:31.702Z_

Let me search for more specific information about the Agentless paper itself and any analysis of embedding degradation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecaf6e9f-977e-4cee-b74e-778ae36f1b7d",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZse4n1Mf7biMQJDLpU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fdf5acf-a515-4a2a-8529-c334d899ec2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W6PdHwcb1gxjyjo3zb9tqG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 18982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 17 · 2026-05-10T08:24:32.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013qTyP8hAuBN7W2xGwSspjs`</summary>

```json
{
  "query": "\"Agentless\" \"2407.01489\" embedding text-embedding-3-small performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fdf5acf-a515-4a2a-8529-c334d899ec2d",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZse4n1Mf7biMQJDLpU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb28438c-1a2d-4812-90d5-cc2676496632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W6PdHwcb1gxjyjo3zb9tqG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 18982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 18 · 2026-05-10T08:24:32.616Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PAbKp4E5wyYStwZo7wFZY8`</summary>

```json
{
  "query": "Agentless localization patch generation embedding retrieval degradation live"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb28438c-1a2d-4812-90d5-cc2676496632",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZse4n1Mf7biMQJDLpU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18695232-1ef1-45ec-9766-1fec941e2b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W6PdHwcb1gxjyjo3zb9tqG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 18982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 847,
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

_source line 19 · 2026-05-10T08:24:32.840Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012ekpW4NEo8nKhsMyWixqzZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.01489",
  "prompt": "Does this paper discuss embedding distribution shift or performance degradation on different benchmarks? What embedding model is used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18695232-1ef1-45ec-9766-1fec941e2b6d",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZse4n1Mf7biMQJDLpU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "988e826f-5508-4d44-8e89-4943bcce5a4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W6PdHwcb1gxjyjo3zb9tqG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 18982,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 232,
          "cache_read_input_tokens": 18982,
          "cache_creation_input_tokens": 847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 847,
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

_source line 20 · 2026-05-10T08:24:35.370Z_

<details><summary>↩ Tool result · `toolu_012ekpW4NEo8nKhsMyWixqzZ`</summary>

```text
Based on the content provided, I cannot find information addressing either of your questions.

The abstract and available metadata do not discuss embedding distribution shift, performance degradation across different benchmarks, or specify which embedding model is used. The paper focuses on Agentless, described as "a simplistic three-phase process of localization, repair, and patch validation," evaluated on the SWE-bench Lite benchmark, but the excerpt shared does not contain technical details about embeddings or cross-benchmark analysis.

To answer your questions, you would need to access the full paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "988e826f-5508-4d44-8e89-4943bcce5a4b",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "aa62c369-2d3a-4dc9-82fe-db118d74d9f1",
  "sourceToolAssistantUUID": "988e826f-5508-4d44-8e89-4943bcce5a4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T08:24:36.902Z_

<details><summary>↩ Tool result · `toolu_013qTyP8hAuBN7W2xGwSspjs`</summary>

```text
Web search results for query: ""Agentless" "2407.01489" embedding text-embedding-3-small performance"

Links: [{"title":"text-embedding-3-small Model | OpenAI API","url":"https://developers.openai.com/api/docs/models/text-embedding-3-small"},{"title":"AGENTLESS : Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/pdf/2407.01489"},{"title":"[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489"},{"title":"OpenAI text-embedding-3-small | Embedding Model Details & Performance","url":"https://agentset.ai/embeddings/openai-text-embedding-3-small"},{"title":"Analyzing Performance Gains in OpenAI's Text-Embedding-3-Small","url":"https://www.pingcap.com/article/analyzing-performance-gains-in-openais-text-embedding-3-small/"},{"title":"text-embedding-3-small: High-Quality Embeddings at Scale","url":"https://blog.promptlayer.com/text-embedding-3-small-high-quality-embeddings-at-scale/"},{"title":"Paper page - Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://huggingface.co/papers/2407.01489"},{"title":"Text Embedding 3 Small - API Pricing & Providers | OpenRouter","url":"https://openrouter.ai/openai/text-embedding-3-small"},{"title":"text-embedding-3-small by OpenAI on Vercel AI Gateway, Specs, Pricing & API","url":"https://vercel.com/ai-gateway/models/text-embedding-3-small"},{"title":"The guide to text-embedding-3-small | OpenAI","url":"https://zilliz.com/ai-models/text-embedding-3-small"}]

Based on the search results, I found information about both topics:

**Agentless (2407.01489):**
Agentless is an agentless approach to automatically solve software development problems that employs a simplistic three-phase process of localization, repair, and patch validation. The research focuses on how large language models have advanced automation of software development tasks, including code synthesis, program repair, and test generation.

**text-embedding-3-small Performance:**
text-embedding-3-small is an improved, more performant version of the ada embedding model. It outperforms its predecessor by 13% while costing 5× cheaper at $0.02 per million tokens. The model delivers higher MTEB scores than ada-002 at lower cost, with a 1536-dimension default.

However, the search results don't contain specific information about how text-embedding-3-small performance is discussed or evaluated within the Agentless paper (2407.01489) itself. You may need to access the full paper directly at arxiv.org/pdf/2407.01489 to find that specific connection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb28438c-1a2d-4812-90d5-cc2676496632",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "81dba153-0b86-4810-80e5-375c922e873b",
  "sourceToolAssistantUUID": "fb28438c-1a2d-4812-90d5-cc2676496632",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T08:24:39.499Z_

<details><summary>↩ Tool result · `toolu_01PAbKp4E5wyYStwZo7wFZY8`</summary>

```text
Web search results for query: "Agentless localization patch generation embedding retrieval degradation live"

Links: [{"title":"AGENTLESS : Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/pdf/2407.01489"},{"title":"Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity - NVIDIA ADLR","url":"https://research.nvidia.com/labs/adlr/cortexa/"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044"},{"title":"NEMOTRON-CORTEXA: Enhancing LLM Agents for Software Engineering","url":"https://openreview.net/pdf?id=k6p8UKRdH7"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"Understanding Software Engineering Agents Through the ...","url":"https://arxiv.org/pdf/2506.08311"},{"title":"Enhancing LLM-based Fault Localization with a Functionality-Aware Retrieval-Augmented Generation Framework","url":"https://arxiv.org/html/2509.20552"},{"title":"LocAgent: Graph-Guided LLM Agents for Code Localization","url":"https://arxiv.org/html/2503.09089v1"},{"title":"We introduce CoRNStack, a large-scale, high-quality contrastive training dataset for code that spans multiple programming languages. We demonstrate that contrastive training of embedding models using CoRNStack leads to state-of-the-art performance across a variety of code retrieval tasks.","url":"https://gangiswag.github.io/cornstack/"}]

Based on the search results, I can provide you with information about the topics related to your query:

## Agentless: Overview

Agentless employs a three-phase workflow of hierarchical localization, patch generation, and patch validation, demonstrating that a carefully designed pipeline can match or outperform tool-driven agents at substantially lower cost.

## Localization with Embedding Retrieval

AGENTLESS uses both prompting-based and embedding-based retrieval to perform hierarchical localization, and during repair, samples multiple candidate patches in a simple diff format for efficient patch generation.

The embedding retrieval process involves: dividing each remaining file into chunks of code segments and computing the embedding for each chunk using an embedding model, then embedding the original issue description and computing the cosine similarity between the resulting query embedding and each chunk embedding to retrieve a list of relevant files.

## Patch Generation

AGENTLESS samples multiple candidate patches in a simple diff format for efficient patch generation. AGENTLESS then generates reproduction tests to verify that the issue has been resolved.

## Performance Degradation Issues

Research has identified performance degradation scenarios. Using raw inputs directly as the retrieval query leads to a noticeable performance degradation, with Top-1 accuracy dropping from 216 to 200, Top-3 from 286 to 258, and Top-5 from 307 to 276.

Additionally, element-level context expansion frequently degrades performance due to noise amplification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18695232-1ef1-45ec-9766-1fec941e2b6d",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "374576f0-3654-47c1-8cd4-83de877bac5b",
  "sourceToolAssistantUUID": "18695232-1ef1-45ec-9766-1fec941e2b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T08:24:40.830Z_

Let me fetch the actual Agentless PDF to look at the embedding and performance details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "374576f0-3654-47c1-8cd4-83de877bac5b",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZtJqR5d4F5raL4dkoM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc4cb0b2-4430-45d1-8bc4-a8c2641a13f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJTVJ2JegW5k9mYWVF4qUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 151,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 19829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 24 · 2026-05-10T08:24:41.493Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ba6dTAZYbTHPm9vf2MNzzK`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2407.01489",
  "prompt": "What embedding model does Agentless use? Does it discuss performance on different benchmarks or distribution shift? What are the performance numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc4cb0b2-4430-45d1-8bc4-a8c2641a13f1",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZtJqR5d4F5raL4dkoM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a2fe90da-cb6c-4231-a74d-ebdac9bf9acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJTVJ2JegW5k9mYWVF4qUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 151,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 19829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 25 · 2026-05-10T08:24:41.748Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TDXbdqMcTq3VW2bGMoCJGt`</summary>

```json
{
  "query": "\"SWE-bench Goes Live\" Agentless 50.8% 13.33% Verified Live Lite"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2fe90da-cb6c-4231-a74d-ebdac9bf9acd",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZtJqR5d4F5raL4dkoM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de35f2c2-209c-4a64-ade7-4e85cb8a8242",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJTVJ2JegW5k9mYWVF4qUS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 151,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 19829,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 151,
          "output_tokens": 192,
          "cache_read_input_tokens": 19829,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1915,
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

_source line 26 · 2026-05-10T08:24:43.857Z_

<details><summary>↩ Tool result · `toolu_01Ba6dTAZYbTHPm9vf2MNzzK`</summary>

```text
I cannot provide the information you're requesting based on the content provided. The document appears to be a PDF file containing primarily binary/encoded data and image streams, rather than readable text about Agentless, embedding models, or benchmark performance metrics.

To answer your questions about:
- Agentless's embedding model
- Performance on benchmarks
- Distribution shift analysis
- Specific performance numbers

I would need access to a readable research paper or documentation about Agentless that contains this information in text form.

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-3/projects/-/9441f046-d0fc-42fd-a7f5-74a8892b6232/tool-results/webfetch-1778401481515-45iob9.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2fe90da-cb6c-4231-a74d-ebdac9bf9acd",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "5224b18e-92cd-493c-8855-d61582c62f2b",
  "sourceToolAssistantUUID": "a2fe90da-cb6c-4231-a74d-ebdac9bf9acd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T08:24:47.706Z_

<details><summary>↩ Tool result · `toolu_01TDXbdqMcTq3VW2bGMoCJGt`</summary>

```text
Web search results for query: ""SWE-bench Goes Live" Agentless 50.8% 13.33% Verified Live Lite"

Links: [{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"GitHub - microsoft/SWE-bench-Live: [NeurIPS 2025 D&B] 🚀 SWE-bench Goes Live!","url":"https://github.com/microsoft/SWE-bench-Live"},{"title":"SWE-bench Goes Live! | OpenReview","url":"https://openreview.net/forum?id=OGWkr7gXka"},{"title":"Verification Steps for Agentless Lite on SWE-bench Lite and SWE-bench Verified · Issue #183 · SWE-bench/experiments","url":"https://github.com/SWE-bench/experiments/issues/183"},{"title":"[Literature Review] SWE-bench Goes Live!","url":"https://www.themoonlight.io/en/review/swe-bench-goes-live"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"}]

Based on the search results, here's what I found about "SWE-bench Goes Live" with the specific metrics you mentioned:

## Overview
The research evaluates three leading agent frameworks (OpenHands, SWE-Agent, and Agentless) in combination with four state-of-the-art LLMs (GPT-4.1, GPT-4o, Claude 3.7 Sonnet, and DeepSeek V3).

## Performance Metrics

The specific percentages you mentioned (50.8% and 13.33%) relate to Agentless results:

- Agentless-1.5 achieved 50.8% on Verified and 40.67% on Lite
- Agentless achieved 27.33% on Lite

## SWE-bench-Live Structure

A lite subset of SWE-bench-Live was constructed by sampling 50 instances per month from issues created between October 2024 and March 2025, resulting in a compact set of 300 instances.

## Key Finding

The findings suggest that existing models may be overfitting to static benchmarks like SWE-bench, underscoring the importance of developing more dynamic and diverse evaluation settings, such as those provided by SWE-bench-Live.

The research paper presents SWE-bench-Live as an automatically constructed, continuously updatable benchmark that addresses limitations of static benchmarks by using real, previously unseen GitHub issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de35f2c2-209c-4a64-ade7-4e85cb8a8242",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "67526776-e07e-478b-ba14-436e339c9b64",
  "sourceToolAssistantUUID": "de35f2c2-209c-4a64-ade7-4e85cb8a8242",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T08:24:48.848Z_

Now let me get the actual detailed numbers and analysis from the SWE-bench Goes Live paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67526776-e07e-478b-ba14-436e339c9b64",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZtuyX5nkweK6Vo8RYg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3508be8c-6fab-46d9-9259-37e544a27399",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01586KZZ2CbaJScza55jnxEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1405,
      "cache_read_input_tokens": 21744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1405,
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

_source line 29 · 2026-05-10T08:24:49.762Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Dpmu1WK24BykqqC1HEMFjV`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.23419v2",
  "prompt": "What are the exact performance numbers for Agentless on Verified, Live Lite, and other benchmarks? What explanation is given for the performance degradation? Is embedding distribution shift mentioned as a cause?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3508be8c-6fab-46d9-9259-37e544a27399",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZtuyX5nkweK6Vo8RYg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c23649c-2c50-40a5-a72f-1496fc124ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01586KZZ2CbaJScza55jnxEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1405,
      "cache_read_input_tokens": 21744,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1405
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 149,
          "cache_read_input_tokens": 21744,
          "cache_creation_input_tokens": 1405,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1405,
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

_source line 30 · 2026-05-10T08:24:54.672Z_

<details><summary>↩ Tool result · `toolu_01Dpmu1WK24BykqqC1HEMFjV`</summary>

```text
# Agentless Performance Analysis

## Performance Numbers

The document provides limited Agentless-specific data on established benchmarks. For **SWE-bench-Live Lite**, Agentless achieved:

- **GPT-4o**: 11.67% resolved rate
- **GPT-4.1**: 12.00% resolved rate
- **Claude 3.7 Sonnet**: 11.33% resolved rate
- **DeepSeek V3**: 13.33% resolved rate

The paper does not report separate Agentless results for SWE-bench Verified or other benchmarks.

## Explanation for Performance Degradation

The authors identify a significant performance gap between static and live benchmarks. They note: "the same methods achieve substantially higher scores on SWE-bench compared to their performance on SWE-bench-Live, despite both benchmarks targeting the same issue-resolving task."

The primary explanation focuses on **overfitting to static benchmarks**. The paper observes that agents perform better on repositories originally in SWE-bench (22.96% resolved) versus new repositories (18.89%), suggesting "existing agents may be overfit or implicitly optimized for the SWE-bench repositories."

## Embedding Distribution Shift

**No, embedding distribution shift is not mentioned** as a cause for the performance degradation. The document does not discuss this concept anywhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c23649c-2c50-40a5-a72f-1496fc124ec2",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "ce52a896-e4e3-48da-905e-0ab2dfc39323",
  "sourceToolAssistantUUID": "5c23649c-2c50-40a5-a72f-1496fc124ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T08:24:55.876Z_

Let me search for more analysis about why there's such a degradation and whether any papers have investigated embedding issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce52a896-e4e3-48da-905e-0ab2dfc39323",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZuRhSj37oHpNVRTg7v",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5f8b180e-3321-4361-94f7-726f24388b04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D4JtKp6j3zzhqo6b8H7KmZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 23149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 475,
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

_source line 32 · 2026-05-10T08:24:56.316Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H3dZosFcCEaAmN7C4g96EM`</summary>

```json
{
  "query": "\"SWE-bench Goes Live\" analysis why degradation Agentless embedding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f8b180e-3321-4361-94f7-726f24388b04",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZuRhSj37oHpNVRTg7v",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "77e5dc38-a255-4e41-910d-dda316566310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D4JtKp6j3zzhqo6b8H7KmZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 23149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 475,
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

_source line 33 · 2026-05-10T08:24:56.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TiHTi1oR441z3iydZRjPUX`</summary>

```json
{
  "query": "\"Saving SWE-Bench\" embedding distribution shift code retrieval benchmark mutation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77e5dc38-a255-4e41-910d-dda316566310",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZuRhSj37oHpNVRTg7v",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "81debe70-7c45-4c39-8f44-ec156c95df00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D4JtKp6j3zzhqo6b8H7KmZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 23149,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 475
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 145,
          "cache_read_input_tokens": 23149,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 475,
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

_source line 34 · 2026-05-10T08:25:03.098Z_

<details><summary>↩ Tool result · `toolu_01H3dZosFcCEaAmN7C4g96EM`</summary>

```text
Web search results for query: ""SWE-bench Goes Live" analysis why degradation Agentless embedding"

Links: [{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"arXiv:2505.23419v1 [cs.SE] 29 May 2025 SWE-bench Goes Live! Linghao Zhang1∗","url":"https://arxiv.org/pdf/2505.23419v1"},{"title":"SWE-bench Goes Live! | OpenReview","url":"https://openreview.net/forum?id=OGWkr7gXka"},{"title":"[2505.23419] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"SWE-Bench+: Enhanced Coding Benchmark for LLMs - arXiv.gg","url":"https://arxiv.gg/abs/2410.06992"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"[Literature Review] SWE-bench Goes Live!","url":"https://www.themoonlight.io/en/review/swe-bench-goes-live"}]

Based on the search results, here's an analysis of the SWE-bench Goes Live paper, including insights about the performance degradation related to Agentless and embedding approaches:

## Overview

SWE-bench Goes Live introduces a live-updatable benchmark with GitHub issues created since 2024 spanning 93 repositories, with each task accompanied by a dedicated Docker image for reproducible execution and an automated curation pipeline called REPOLAUNCH.

## Performance Degradation on Live Benchmark

A key finding is a substantial performance gap compared to static benchmarks like SWE-bench, even under controlled evaluation conditions. The best-performing combination, OpenHands with Claude 3.7 Sonnet, achieves a resolved rate of only 19.25% on SWE-bench-Live-Full, compared to 43.20% on SWE-bench Verified.

The gap is partly due to potential overfitting/optimization towards the original SWE-bench dataset, as performance is higher on instances from repositories present in SWE-bench (22.96%) than on those from new repositories (18.89%).

## Agentless and Embedding Issues

Regarding Agentless specifically, Agentless-Lite is a simplification that uses an embedding model to retrieve relevant files from the repository through RAG-based localization, querying the LLM to generate a repair based on the top 5 retrieved files. 

The analysis reveals broader difficulty patterns: current agents struggle to coordinate coherent edits across multiple files or to reason about large, intra-file changes. This suggests that RAG-based embedding approaches may have fundamental limitations in handling complex, multi-file patches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77e5dc38-a255-4e41-910d-dda316566310",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "1fffe8bc-b422-4c11-a813-093978a92d00",
  "sourceToolAssistantUUID": "77e5dc38-a255-4e41-910d-dda316566310",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T08:25:04.607Z_

<details><summary>↩ Tool result · `toolu_01TiHTi1oR441z3iydZRjPUX`</summary>

```text
Web search results for query: ""Saving SWE-Bench" embedding distribution shift code retrieval benchmark mutation"

Links: [{"title":"Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation","url":"https://arxiv.org/html/2510.08996v1"},{"title":"[2510.08996] Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation","url":"https://arxiv.org/abs/2510.08996"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"(PDF) Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation","url":"https://www.researchgate.net/publication/396456997_Saving_SWE-Bench_A_Benchmark_Mutation_Approach_for_Realistic_Agent_Evaluation"},{"title":"SWE-bench","url":"https://www.swebench.com/original.html"},{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://arxiv.org/html/2602.08316"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"SWE-Bench+: Next-Gen Code Agent Benchmarks","url":"https://www.emergentmind.com/topics/swe-bench-3b86a734-b378-4ee6-bcaf-640949ed7afb"},{"title":"Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/saving-swe-bench-a-benchmark-mutation-approach-for-realistic-agent-evaluation/"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"}]

Based on the search results, I found comprehensive information about the "Saving SWE-Bench" paper and its focus on embedding distribution shift, code retrieval, benchmark mutation, and related topics.

## Key Findings

The paper introduces a novel benchmarking framework that transforms existing formal benchmarks into realistic user queries through systematic analysis of developer interaction patterns with chat-based agents. Current benchmarks for evaluating software engineering agents, such as SWE-Bench Verified, are predominantly derived from GitHub issues and fail to accurately reflect how developers interact with chat-based coding assistants in IDEs.

### Distribution Shift Analysis

The researchers embedded queries using OpenAI's text-embedding-3-large model and applied PCA to visualize embeddings in 3D, finding that SWE-Bench C# and telemetry queries form separate clouds with little overlap, while SWE-Bench C#-Mutated shows significantly more overlap with real-world telemetry queries.

### Benchmark Mutation Approach

The mutation approach successfully transforms benchmark queries to better match the characteristics of actual developer interactions, shifting the distribution toward more realistic user queries. The framework was applied to SWE-Bench Verified, the TypeScript subset of Multi-SWE-Bench, and a private SWE-Bench C# benchmark to transform formal GitHub issue descriptions into realistic user-style queries based on telemetry analysis.

### Performance Impact

The findings reveal that existing benchmarks significantly overestimate agent capabilities by approximately 10-16% for internal benchmarks. For public benchmarks, overestimation can exceed 50% over baseline performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81debe70-7c45-4c39-8f44-ec156c95df00",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "5a0b98f6-1c66-4683-9f6b-e3fc8ec22792",
  "sourceToolAssistantUUID": "81debe70-7c45-4c39-8f44-ec156c95df00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-10T08:25:05.843Z_

Excellent! Now let me fetch the "Saving SWE-Bench" paper to see the specific embedding distribution analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a0b98f6-1c66-4683-9f6b-e3fc8ec22792",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZvADZ8yPKLv9tAq5Rf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9891aa2a-cf36-4e6a-990b-24c19a9f8395",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HZ1s8YQ9W8U4z7451fYr2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1995,
      "cache_read_input_tokens": 23624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1995,
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

_source line 37 · 2026-05-10T08:25:06.713Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015gJ2eDTYg7pYq4dGf8t5Xr`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.08996v1",
  "prompt": "What does this paper say about embedding distribution shift and text-embedding-3 models? Does it show evidence of distribution mismatch between training data and newer code? What are the specific findings about why embeddings fail on mutated/realistic benchmarks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9891aa2a-cf36-4e6a-990b-24c19a9f8395",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZvADZ8yPKLv9tAq5Rf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e3671fbf-5da2-41f5-a2a4-4a18e317a13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HZ1s8YQ9W8U4z7451fYr2C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1995,
      "cache_read_input_tokens": 23624,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1995
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 164,
          "cache_read_input_tokens": 23624,
          "cache_creation_input_tokens": 1995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1995,
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

_source line 38 · 2026-05-10T08:25:12.738Z_

<details><summary>↩ Tool result · `toolu_015gJ2eDTYg7pYq4dGf8t5Xr`</summary>

```text
# Distribution Shift and Embedding Analysis in SWE-Bench Mutation Paper

The paper demonstrates embedding distribution misalignment through a specific visualization approach. According to the authors, they "embedded using text-embedding-3-large model, followed by PCA to reduce dimensionality" for 3D plotting of original benchmarks versus mutated variants against telemetry queries.

## Key Findings on Distribution Mismatch

The paper shows empirical evidence that original SWE-Bench and telemetry queries occupy separate embedding spaces. Specifically, the researchers found that "the embeddings corresponding to SWE-Bench C# (red) and the telemetry queries (blue) make two separate clouds, with little to no overlap."

However, after mutation, the distribution shifted meaningfully: "the cloud corresponding to SWE-Bench C#-Mutated (green) has a lot more overlap with telemetry query cloud than the original benchmark."

## Why This Matters for Evaluation

Rather than claiming embeddings "fail," the paper uses embedding distributions to validate their core premise—that formal GitHub-issue-style problems differ substantially from how developers actually communicate bugs to chat agents. The visualization serves as quantitative confirmation that their mutation methodology successfully transforms benchmark problems toward realistic communication patterns.

The paper doesn't analyze why embeddings fail on mutated benchmarks, but rather uses embeddings to show that mutations successfully bridge the gap between formal and informal problem descriptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3671fbf-5da2-41f5-a2a4-4a18e317a13e",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "42d86aac-53e9-4051-bca0-b7141a4a937e",
  "sourceToolAssistantUUID": "e3671fbf-5da2-41f5-a2a4-4a18e317a13e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-10T08:25:14.206Z_

Now let me search for more specific analysis about whether the embedding models have training data cutoffs or OOD issues with post-2024 code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42d86aac-53e9-4051-bca0-b7141a4a937e",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZvkxMEPfrsBotXx9K4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "95e1f79f-182e-4641-9b13-f69b8d481737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VHpRC2KhjsCxLd72AjX3mz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 25619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 489,
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

_source line 40 · 2026-05-10T08:25:14.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WZ2SsjWri62AMWsHz7nn38`</summary>

```json
{
  "query": "OpenAI text-embedding-3-small training data cutoff date knowledge 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95e1f79f-182e-4641-9b13-f69b8d481737",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZvkxMEPfrsBotXx9K4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "503a5628-3f95-4d90-b951-bef88b3e8b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VHpRC2KhjsCxLd72AjX3mz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 25619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 489,
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

_source line 41 · 2026-05-10T08:25:14.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LGSiv3zdVyN14eGTcZjFZt`</summary>

```json
{
  "query": "\"SWE-bench Goes Live\" post-2024 repositories new issues degradation analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "503a5628-3f95-4d90-b951-bef88b3e8b89",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZvkxMEPfrsBotXx9K4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc2608fe-2d9a-4e68-b5a5-ebf41c18f55e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VHpRC2KhjsCxLd72AjX3mz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 25619,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 489
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 156,
          "cache_read_input_tokens": 25619,
          "cache_creation_input_tokens": 489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 489,
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

_source line 42 · 2026-05-10T08:25:18.554Z_

<details><summary>↩ Tool result · `toolu_01WZ2SsjWri62AMWsHz7nn38`</summary>

```text
Web search results for query: "OpenAI text-embedding-3-small training data cutoff date knowledge 2024"

Links: [{"title":"What is the training data knowledge cutoff date for text-embedding-3-large? - API - OpenAI Developer Community","url":"https://community.openai.com/t/what-is-the-training-data-knowledge-cutoff-date-for-text-embedding-3-large/1361283"},{"title":"Vector embeddings | OpenAI API","url":"https://developers.openai.com/api/docs/guides/embeddings"},{"title":"text-embedding-3-small Model | OpenAI API","url":"https://developers.openai.com/api/docs/models/text-embedding-3-small"},{"title":"New embedding models and API updates | OpenAI","url":"https://openai.com/index/new-embedding-models-and-api-updates/"},{"title":"Embeddings FAQ | OpenAI Help Center","url":"https://help.openai.com/en/articles/6824809-embeddings-faq"},{"title":"The guide to text-embedding-3-small | OpenAI","url":"https://zilliz.com/ai-models/text-embedding-3-small"},{"title":"text-embedding-3-large Model | OpenAI API","url":"https://platform.openai.com/docs/models/text-embedding-3-large"},{"title":"It looks like 'text-embedding-3' embeddings are truncated/scaled versions from higher dim version - API - OpenAI Developer Community","url":"https://community.openai.com/t/it-looks-like-text-embedding-3-embeddings-are-truncated-scaled-versions-from-higher-dim-version/602276"},{"title":"OpenAI's Text Embeddings v3 | Pinecone","url":"https://www.pinecone.io/learn/openai-embeddings-v3/"},{"title":"Text Embedding 3 Small API — One API 400+ AI Models","url":"https://aimlapi.com/models/text-embedding-3-small"}]

Based on the search results, I found information about the text-embedding-3-small model, though the specific training data cutoff date isn't explicitly stated in the search results. However, I did find an important note about the model's knowledge cutoff:

The max tokens and knowledge cutoff have not changed, which represents a minor drawback for use cases performing retrieval in domains requiring up-to-date knowledge. This indicates that the text-embedding-3-small model maintained the same knowledge cutoff as its predecessor, the text-embedding-ada-002 model, which had a September 2021 knowledge cutoff date.

The text-embedding-3-small model was released on January 25, 2024. Despite this 2024 release date, the model's training data knowledge cutoff appears to have remained at September 2021, the same as the earlier ada-002 embedding model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "503a5628-3f95-4d90-b951-bef88b3e8b89",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "d4a0a15b-e28f-4cdd-be2f-83b45d104ad8",
  "sourceToolAssistantUUID": "503a5628-3f95-4d90-b951-bef88b3e8b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T08:25:21.572Z_

<details><summary>↩ Tool result · `toolu_01LGSiv3zdVyN14eGTcZjFZt`</summary>

```text
Web search results for query: ""SWE-bench Goes Live" post-2024 repositories new issues degradation analysis"

Links: [{"title":"SWE-bench Goes Live! | OpenReview","url":"https://openreview.net/forum?id=OGWkr7gXka"},{"title":"NeurIPS Poster SWE-bench Goes Live!","url":"https://neurips.cc/virtual/2025/poster/121677"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-bench Goes Live! - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/swe-bench-goes-live/"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v1"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"[2505.23419] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419"},{"title":"[2505.23419v1] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419v1"},{"title":"SWE-bench Verified Issues Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified-issues"},{"title":"GitHub - microsoft/SWE-bench-Live: [NeurIPS 2025 D&B] 🚀 SWE-bench Goes Live!","url":"https://github.com/microsoft/SWE-bench-Live"}]

Based on the search results, here's what I found about SWE-bench Goes Live:

## Overview

SWE-bench-Live is a live-updatable benchmark designed to address limitations in the original SWE-bench. The original SWE-bench has not been updated since its release, is restricted to only 12 repositories, and relies heavily on manual effort for constructing test instances and setting up executable environments.

## Post-2024 Repositories and New Issues

SWE-bench-Live currently includes 1,890 tasks derived from real GitHub issues created since 2024, spanning 223 repositories. To ensure freshness and reduce the risk of data contamination from pretraining, the dataset is restricted to issues created between January 1, 2024, and April 20, 2025.

## Automated Pipeline and Methodology

RepoLaunch is a fully automated system that streamlines the entire process—from issue mining to environment packaging, specifically employing an agentic, end-to-end workflow to set up Docker-based environments by identifying relevant instruction files, selecting appropriate base images, installing dependencies, building the project, and validating its test suite.

## Continuous Updates

SWE-bench-Live is planned to be updated on a monthly basis to provide the community with up-to-date task instances and support rigorous and contamination-free evaluation.

The search results don't contain specific information about degradation analysis, so I cannot provide details on that aspect from these sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc2608fe-2d9a-4e68-b5a5-ebf41c18f55e",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "dcedb786-ec26-4aaf-b95a-409f54536695",
  "sourceToolAssistantUUID": "bc2608fe-2d9a-4e68-b5a5-ebf41c18f55e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-10T08:25:23.034Z_

Perfect! Now let me search for any papers that specifically discuss the relationship between embedding model knowledge cutoff and SWE-bench performance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcedb786-ec26-4aaf-b95a-409f54536695",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZwQjxGwWCxzHzbmqax",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a982c3c0-d5dc-4a54-8af7-47594f5908af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018muvn3oduaPXfwUsxy5fd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 26108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1730,
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

_source line 45 · 2026-05-10T08:25:23.531Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BTyeuc2ToDFZAHqivb9wYn`</summary>

```json
{
  "query": "Agentless \"text-embedding-3-small\" Lite SWE-bench repositories 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a982c3c0-d5dc-4a54-8af7-47594f5908af",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZwQjxGwWCxzHzbmqax",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4217cece-e178-4780-9988-6c3e6724e6a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018muvn3oduaPXfwUsxy5fd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 26108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1730,
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

_source line 46 · 2026-05-10T08:25:23.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YDxFQoK3nAKrZVRDuFTTF1`</summary>

```json
{
  "query": "code embedding model out of distribution new repositories post-training knowledge cutoff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4217cece-e178-4780-9988-6c3e6724e6a7",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZwQjxGwWCxzHzbmqax",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21fc4a2e-857b-4163-a280-bdda1066fb3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018muvn3oduaPXfwUsxy5fd9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 26108,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1730
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 152,
          "cache_read_input_tokens": 26108,
          "cache_creation_input_tokens": 1730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1730,
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

_source line 47 · 2026-05-10T08:25:30.714Z_

<details><summary>↩ Tool result · `toolu_01BTyeuc2ToDFZAHqivb9wYn`</summary>

```text
Web search results for query: "Agentless "text-embedding-3-small" Lite SWE-bench repositories 2024"

Links: [{"title":"GitHub - sorendunn/Agentless-Lite: Agentless Lite: RAG-based SWE-Bench software engineering scaffold · GitHub","url":"https://github.com/sorendunn/Agentless-Lite"},{"title":"Verification Steps for Agentless Lite on SWE-bench Lite and SWE-bench Verified · Issue #183 · SWE-bench/experiments","url":"https://github.com/SWE-bench/experiments/issues/183"},{"title":"Agentless-Lite/README.md at main · sorendunn/Agentless-Lite","url":"https://github.com/sorendunn/Agentless-Lite/blob/main/README.md"},{"title":"SWE-bench Lite","url":"https://www.swebench.com/lite.html"},{"title":"GitHub - OpenAutoCoder/Agentless: Agentless🐱: an agentless approach to automatically solve software development problems","url":"https://github.com/OpenAutoCoder/Agentless"},{"title":"Paper page - Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://huggingface.co/papers/2407.01489"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"arXiv:2505.23419v1 [cs.SE] 29 May 2025 SWE-bench Goes Live! Linghao Zhang1∗","url":"https://arxiv.org/pdf/2505.23419v1"}]

Based on the search results, I found relevant information about Agentless, text-embedding-3-small, and SWE-bench Lite:

## Key Findings

Agentless Lite is a generalized, lightweight adaptation of the Agentless framework for solving software development issues. Specifically, Agentless Lite performs the following steps: Use an embedding model to retrieve relevant files from the repository and Query the LLM to generate a repair based on the top 5 retrieved files, retrying the generation until the model outputs a valid patch.

Agentless Lite 1.0 was released on February 13th, 2025, and is the top-performing RAG-only scaffold for SWE-bench, increasing RAG performance on the lite subset from 4.33% to 32.33% and costing only $0.21 per instance ($0.12 if using the prepared retrieval contexts).

### Text-embedding-3-small Usage

The retrieval step uses the `text-embedding-3-small` model as a filter parameter in the command to process SWE-bench Lite repositories.

### Repository Information

The main repository for Agentless Lite is available at:
- **GitHub**: https://github.com/sorendunn/Agentless-Lite

The purpose of verification steps is to provide instructions on how to verify the open source status and benchmark results for Agentless Lite on the Lite and Verified benchmarks. The team ran inference with the provided retrievals twice on lite (solving 97 and 99 issues respectively and reporting the lower of the two runs) and once on verified (solving the reported 212 issues).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4217cece-e178-4780-9988-6c3e6724e6a7",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "7e5317f5-6e2f-4a9e-bd71-617059f094f1",
  "sourceToolAssistantUUID": "4217cece-e178-4780-9988-6c3e6724e6a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T08:25:31.418Z_

<details><summary>↩ Tool result · `toolu_01YDxFQoK3nAKrZVRDuFTTF1`</summary>

```text
Web search results for query: "code embedding model out of distribution new repositories post-training knowledge cutoff"

Links: [{"title":"State-of-the-Art Code Retrieval With Efficient Code Embedding Models","url":"https://www.qodo.ai/blog/qodo-embed-1-code-embedding-code-retrieval/"},{"title":"Qwen3 Embedding Series Overview","url":"https://www.emergentmind.com/topics/qwen3-embedding-series"},{"title":"Code-Embed: A Family of Open Large Language Models for Code Embedding","url":"https://arxiv.org/html/2411.12644v2"},{"title":"Train 400x faster Static Embedding Models with Sentence Transformers","url":"https://huggingface.co/blog/static-embeddings"},{"title":"Post-Training 4-bit Quantization on Embedding Tables","url":"https://guanh01.github.io/files/2019fb.pdf"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Qwen3+Embedding+series"},{"title":"Learning Code-Edit Embedding to Model Student Debugging Behavior","url":"https://arxiv.org/html/2502.19407v1"},{"title":"The Best Open-Source Embedding Models in 2026","url":"https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models"},{"title":"6 Best Code Embedding Models Compared: A Complete Guide","url":"https://modal.com/blog/6-best-code-embedding-models-compared"},{"title":"An empirical study of best practices for code pre-trained models on software engineering classification tasks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425003847"}]

Based on the search results, here are findings related to code embedding models, out-of-distribution performance, new repositories, and post-training knowledge:

## Recent Code Embedding Model Developments

CodeXEmbed is a family of large-scale code embedding models ranging from 400M to 7B parameters, with a novel training pipeline that unifies multiple programming languages and transforms various code-related tasks into a common retrieval framework.

For Qodo-Embed-1, a pipeline was built that automatically scrapes open-source code from GitHub, applies multiple filtering steps for quality, and then injects the data with synthetic function descriptions and docstrings.

## Out-of-Distribution and Generalization

Model merging using spherical linear interpolation (slerp) is a strategy shown to improve generalization and robustness, particularly when facing distributional or domain imbalances.

CodeXEmbed was evaluated on RepoEval and SWE-Bench-Lite, demonstrating that improved retrieval significantly enhances end-to-end Retrieval-Augmented Generation (RAG) performance for code tasks.

## Post-Training Enhancements

Matryoshka Representation Learning (MRL) support allows embedding dimension to be truncated post-training with little performance loss, optimizing for latency and resource use across deployment contexts.

These developments show active research into making code embedding models more robust across different code repositories and improving their ability to generalize to out-of-distribution code samples through techniques like synthetic data generation, model merging, and post-training optimization methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21fc4a2e-857b-4163-a280-bdda1066fb3f",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "78cd9409-51fd-4986-abc9-f8f1a982b08f",
  "sourceToolAssistantUUID": "21fc4a2e-857b-4163-a280-bdda1066fb3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-10T08:25:33.945Z_

Let me search more specifically for discussions about the exact performance drop cited and whether embedding cutoff is the cause.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78cd9409-51fd-4986-abc9-f8f1a982b08f",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZx9JntKBCZHic6bLFq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f595180a-2f20-41ab-8fbd-2dc4533d2b2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TwKocEGBoLYvm5U4iSV79d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 27838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1963,
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

_source line 50 · 2026-05-10T08:25:34.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZiHrLw7JNmk1xiR8359Mq`</summary>

```json
{
  "query": "\"50.8\" \"13.33\" Agentless SWE-bench degradation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f595180a-2f20-41ab-8fbd-2dc4533d2b2c",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZx9JntKBCZHic6bLFq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d79ae2e-9028-40c5-a921-f3e79bbc32eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TwKocEGBoLYvm5U4iSV79d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 27838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1963,
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

_source line 51 · 2026-05-10T08:25:34.656Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0143apb4Xkao5bMoowUpWHK2`</summary>

```json
{
  "query": "SWE-bench Live results table Agentless GPT-4o Claude performance scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d79ae2e-9028-40c5-a921-f3e79bbc32eb",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZx9JntKBCZHic6bLFq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dfaac974-9816-48d3-a73d-19666f85e368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TwKocEGBoLYvm5U4iSV79d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 27838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1963,
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

### Tool result

_source line 52 · 2026-05-10T08:25:40.357Z_

<details><summary>↩ Tool result · `toolu_01QZiHrLw7JNmk1xiR8359Mq`</summary>

```text
Web search results for query: ""50.8" "13.33" Agentless SWE-bench degradation"

Links: [{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-BENCH+: ENHANCED CODING BENCHMARK","url":"https://openreview.net/pdf?id=R40rS2afQ3"},{"title":"GitHub - OpenAutoCoder/Agentless: Agentless🐱: an agentless approach to automatically solve software development problems","url":"https://github.com/OpenAutoCoder/Agentless"},{"title":"arXiv:2509.16941v2 [cs.SE] 14 Nov 2025 SWE-Bench Pro: Can AI Agents Solve","url":"https://arxiv.org/pdf/2509.16941"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"},{"title":"AGENTLESS : Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/pdf/2407.01489"},{"title":"GitHub - zplus1/swe-bench-agentless: Agentless🐱: an agentless approach to automatically solve software development problems","url":"https://github.com/zplus1/swe-bench-agentless"},{"title":"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?","url":"https://arxiv.org/html/2509.16941v1"}]

Based on the search results, I found relevant information about these specific numbers in relation to Agentless and SWE-bench:

Agentless integrated with Claude 3.5 Sonnet achieved a 50.8% solve rate on SWE-bench verified (the 50.8% figure). The 13.33% figure appears in a different context: 13.33% of all issues in SWE-Bench Lite are identified as problematic due to weak test cases.

These metrics reflect concerns about SWE-bench quality. The 50.8% performance represents Agentless's strong results on the verified benchmark, while the 13.33% refers to the proportion of issues in the Lite version that have weak test cases that could lead to inflated performance metrics. Weak tests resulted in significant drops in resolution percentages across models, with AutoCodeRover-v2.0 experiencing a drop of 26 percentage points when weak test cases were removed, illustrating the degradation in performance when benchmarks are more rigorously evaluated.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d79ae2e-9028-40c5-a921-f3e79bbc32eb",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "32f8c0ed-c605-48e4-ae56-d451d05759d0",
  "sourceToolAssistantUUID": "2d79ae2e-9028-40c5-a921-f3e79bbc32eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T08:25:44.145Z_

<details><summary>↩ Tool result · `toolu_0143apb4Xkao5bMoowUpWHK2`</summary>

```text
Web search results for query: "SWE-bench Live results table Agentless GPT-4o Claude performance scores"

Links: [{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Live-SWE-agent Leaderboard","url":"https://live-swe-agent.github.io/"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-Bench 2026: Claude 77.2% vs GPT-5 74.9% | Full Leaderboard | Local AI Master","url":"https://localaimaster.com/models/swe-bench-explained-ai-benchmarks"},{"title":"SWE-Bench Coding Agent Leaderboard 2026: Claude vs GPT | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-Bench Leaderboard May 2026 | GPT-5.5 Leads at 88.7%","url":"https://www.marc0.dev/en/leaderboard"}]

Based on the search results, here's information about SWE-bench Live results with performance scores for various models:

## SWE-Bench Verified Results (as of May 2026)

GPT-5.5 leads at 88.7%, with Claude Opus 4.7 at 87.6% and GPT-5.3-Codex at 85.0%.

Claude Opus 4.5 scores 80.9%, Opus 4.6 scores 80.8%, and DeepSeek V4 Pro Max and Gemini 3.1 Pro both score 80.6%.

## Agentless Performance

Agentless uses a fixed three-stage pipeline (fault localization, patch generation, and patch selection) with no iterative tool calls, achieving 34.2% on Verified.

## SWE-Bench Pro Results

Claude Opus 4.7 leads on SWE-Bench Pro at 64.3%.

## Claude vs GPT-4o Specific Comparison

For GPT-4o specifically (an earlier model), the results viewer lists entries like "Agentless-1.5 + GPT 4o" and "AutoCodeRover (v20240620) + GPT 4o", though specific performance scores for GPT-4o are not detailed in the current results.

The official SWE-bench results viewer and leaderboards are available at swebench.com, which provides the most up-to-date comparative performance data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfaac974-9816-48d3-a73d-19666f85e368",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "7c366a1b-6093-4f0f-a889-199a3d31013f",
  "sourceToolAssistantUUID": "dfaac974-9816-48d3-a73d-19666f85e368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-10T08:25:45.336Z_

Let me fetch the detailed results table from the SWE-bench Goes Live paper more carefully to get the exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c366a1b-6093-4f0f-a889-199a3d31013f",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZy5Fjbthm5do36wFMg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ffcdc25b-395a-4a56-9429-bdda537821f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ebfe2vNZt22K2ywZU1o6ek",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 29801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1798,
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

_source line 55 · 2026-05-10T08:25:46.179Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QZTWLvSAmCdFgoonPzo8XG`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.23419v2",
  "prompt": "What are the exact performance numbers for Agentless on SWE-bench Verified and SWE-bench Live Lite with GPT-4o, Claude, and DeepSeek? Show all the tables with results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffcdc25b-395a-4a56-9429-bdda537821f7",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZy5Fjbthm5do36wFMg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "adbf5725-8038-4078-8e0a-17bfcbabc0c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ebfe2vNZt22K2ywZU1o6ek",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 29801,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1798
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 159,
          "cache_read_input_tokens": 29801,
          "cache_creation_input_tokens": 1798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1798,
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

_source line 56 · 2026-05-10T08:25:52.338Z_

<details><summary>↩ Tool result · `toolu_01QZTWLvSAmCdFgoonPzo8XG`</summary>

```text
I apologize, but I cannot locate the specific performance numbers you're requesting in the provided PDF content. The document appears to be "SWE-bench Goes Live!" by Zhang et al., but the extracted text is heavily compressed and contains mostly binary/encoded data rather than readable tables with performance metrics.

To provide you with the exact performance numbers for Agentless on:
- SWE-bench Verified with GPT-4o, Claude, and DeepSeek
- SWE-bench Live Lite with the same models

I would need access to a readable version of the document containing the results tables. The current extraction doesn't contain legible tabular data showing these specific benchmark results.

I recommend:
1. Accessing the PDF directly from arXiv (https://arxiv.org/abs/2505.23419v2)
2. Checking the supplementary materials or appendices
3. Visiting the official SWE-bench-Live repository for benchmark results

If you can provide the specific tables or a clearer document excerpt, I'd be happy to help extract and present the performance numbers.

[Binary content (application/pdf, 2.1MB) also saved to /home/ubuntu/.claude-account-3/projects/-/9441f046-d0fc-42fd-a7f5-74a8892b6232/tool-results/webfetch-1778401546903-bdxw9j.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adbf5725-8038-4078-8e0a-17bfcbabc0c2",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "c825cfe8-7217-4271-854e-f2403dafe0ad",
  "sourceToolAssistantUUID": "adbf5725-8038-4078-8e0a-17bfcbabc0c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-10T08:25:53.518Z_

Let me try the HTML version of the paper instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c825cfe8-7217-4271-854e-f2403dafe0ad",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZygGA8eSoLZ82qF8mJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "97d67473-c4f5-4d09-9117-fcd2ab379759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019dVYkWDFALM1ft9HAYZdjb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 31599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 492,
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

_source line 58 · 2026-05-10T08:25:53.973Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KWgbWZ5qRd7d8Hb8Ki5742`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.23419",
  "prompt": "Show me the complete results table with all performance numbers for Agentless, OpenHands, and SWE-Agent on both SWE-bench Verified and SWE-bench-Live Lite. What are the exact degradation numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97d67473-c4f5-4d09-9117-fcd2ab379759",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZygGA8eSoLZ82qF8mJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "74befcc5-9ab0-4b37-ae97-c41364426902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019dVYkWDFALM1ft9HAYZdjb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 31599,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 492
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 148,
          "cache_read_input_tokens": 31599,
          "cache_creation_input_tokens": 492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 492,
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

_source line 59 · 2026-05-10T08:25:58.977Z_

<details><summary>↩ Tool result · `toolu_01KWgbWZ5qRd7d8Hb8Ki5742`</summary>

```text
# Performance Comparison: SWE-bench Verified vs. SWE-bench-Live Lite

Based on the document, I can only provide **partial performance data**. The paper does not include a complete results table comparing all three agents across both benchmarks.

## Available Data from Document

**SWE-bench-Live Lite Results (Table 3):**
- OpenHands + Claude 3.7 Sonnet: 17.67% resolved
- SWE-Agent + Claude 3.7 Sonnet: 17.67% resolved
- Agentless + Claude 3.7 Sonnet: 11.33% resolved

**SWE-bench Verified Reference:**
The authors note: "the best-performing agent–model pair achieves a higher resolved rate of 22.96% on SWE-bench Instances" and state that "OpenHands with Claude 3.7 Sonnet...on the SWE-bench verified subset using the exact same setups...reached 43.20%."

## Performance Degradation

The document indicates substantial degradation but doesn't provide complete side-by-side comparisons. The authors observe: "the same methods achieve substantially higher scores on SWE-bench compared to their performance on SWE-bench-Live, despite both benchmarks targeting the same issue-resolving task with identical settings."

The most concrete degradation example: OpenHands + Claude achieves 43.20% on SWE-bench Verified but only 19.25% on SWE-bench-Live Full (56% relative decline).

**Note:** A comprehensive results table across all agent-model combinations on both benchmarks is not presented in this document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74befcc5-9ab0-4b37-ae97-c41364426902",
  "isSidechain": true,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "agentId": "ae669b1bb81e25cce",
  "type": "user",
  "uuid": "ef0ff0ad-06d3-469d-87bf-1cf4ae676ff4",
  "sourceToolAssistantUUID": "74befcc5-9ab0-4b37-ae97-c41364426902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-10T08:26:12.187Z_

Based on my comprehensive search, I can now provide you with findings about the claim regarding Agentless's degradation and the "embedding distribution shift" explanation.

## Verification of the Embedding Distribution Shift Claim

**The "embedding distribution shift" explanation is NOT empirically supported by the papers I reviewed.** Here are the key findings:

### What the SWE-bench Goes Live Paper Actually Says

The paper (2505.23419) does NOT attribute Agentless's degradation to embedding distribution shift or OpenAI text-embedding-3-small knowledge cutoff issues. Instead:

1. **The explanation offered is benchmark overfitting**, not embedding OOD degradation. The authors state: "existing agents may be overfit or implicitly optimized for the SWE-bench repositories."

2. **Empirical evidence of overfitting**: Agents perform better on instances from original SWE-bench repositories (22.96% resolved) versus new repositories (18.89% resolved), but the paper frames this as evidence of dataset-specific optimization, not embedding model limitations.

3. **Embedding distribution shift is not mentioned** anywhere in the paper's explanation of performance degradation.

### The Actual Performance Numbers

From the SWE-bench Goes Live paper:
- **Agentless + Claude 3.7 Sonnet on SWE-bench-Live Lite: 11.33%**
- **Agentless + DeepSeek V3 on SWE-bench-Live Lite: 13.33%** (this is the 13.33% mentioned)

However, the paper does NOT report Agentless results on SWE-bench Verified directly. The 50.8% figure you cited may come from a different source or context.

### What We Know About text-embedding-3-small

A critical finding: **text-embedding-3-small has a September 2021 knowledge cutoff**, NOT a 2024 cutoff. This is documented in OpenAI community forums. The model was released in January 2024 but maintained the same knowledge cutoff as its predecessor (text-embedding-ada-002), which is pre-2022. This could theoretically cause OOD issues with post-2024 code repositories, but:

- **No paper directly attributes Agentless degradation to this cutoff**
- The "Saving SWE-Bench" paper (2510.08996) uses text-embedding-3-**large** and finds embedding distribution shifts between formal benchmark queries and realistic user queries, but this is about query phrasing style, NOT knowledge cutoff issues

### What Actually Explains the Verified→Live Degradation

Multiple factors are documented:

1. **Problem difficulty**: SWE-bench-Live includes newer repositories and issue types not in the static Verified set
2. **Benchmark contamination**: Models trained on pre-2024 data may have seen SWE-bench Verified instances during training
3. **Repository diversity**: Original SWE-bench covers only ~12 repositories; Live has 223+ repositories with different codebases
4. **Query format differences**: The "Saving SWE-Bench" paper shows distribution shifts between formal GitHub issues and realistic developer queries

### The Bottom Line

**The "embedding distribution shift due to Sept 2021 knowledge cutoff" explanation is a hypothesis NOT validated by the papers.** The SWE-bench Goes Live paper attributes degradation to benchmark overfitting and dataset differences, not embedding model knowledge cutoffs. This claim requires explicit empirical testing (e.g., replacing text-embedding-3-small with a model having newer training data and measuring improvement) which the papers do not provide.

---

Sources:
- [SWE-bench Goes Live! (2505.23419)](https://arxiv.org/html/2505.23419)
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)
- [Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation](https://arxiv.org/html/2510.08996v1)
- [OpenAI text-embedding-3-small Model Documentation](https://developers.openai.com/api/docs/models/text-embedding-3-small)
- [What is the training data knowledge cutoff date for text-embedding-3-large? - OpenAI Developer Community](https://community.openai.com/t/what-is-the-training-data-knowledge-cutoff-date-for-text-embedding-3-large/1361283)
- [Dissecting the SWE-Bench Leaderboards](https://arxiv.org/html/2506.17208v2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef0ff0ad-06d3-469d-87bf-1cf4ae676ff4",
  "isSidechain": true,
  "agentId": "ae669b1bb81e25cce",
  "requestId": "req_011CatZzAexcKq7tWHLMfsk6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7a3c6d40-0b03-49dc-a542-8c145ac57c73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WnMGCtY77gXMBUSWAj9fcw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 32091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 544,
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
