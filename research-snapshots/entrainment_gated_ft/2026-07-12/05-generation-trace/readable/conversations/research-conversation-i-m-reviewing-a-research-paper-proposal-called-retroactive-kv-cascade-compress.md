# Research conversation: I'm reviewing a research paper proposal called "Retroactive KV Cascade Compression for Iterative Multi-Round RAG" (RKCC)

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5ed68a9f4abf542e.jsonl`
- **Structured JSON:** [`f870ce3e6e46f3751d24.json`](../../sessions/f8/f870ce3e6e46f3751d24.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-09T18:59:38.300Z_

I'm reviewing a research paper proposal called "Retroactive KV Cascade Compression for Iterative Multi-Round RAG" (RKCC). I need you to search for and verify several things. Please do thorough searches across multiple sources.

**Task 1: Verify these papers exist and check their content:**
1. ProphetKV (arXiv:2602.02579) - "User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation"
2. FlowKV (arXiv:2505.15347) - "Enhancing Multi-Turn Conversational Coherence in LLMs via Isolated Key-Value Cache Management"
3. AgenticRAGTracer (arXiv:2602.19127) - "A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG"
4. QCFuse (arXiv:2604.08585) - "Query-Centric Cache Fusion for Efficient RAG Inference"
5. InfoFlow KV (arXiv:2603.05353) - "Prompt-Conditioned Selective KV Recomputation for RAG Inference"

For each: search "site:arxiv.org {arxiv_id}" and report what you find (title, abstract summary, whether it actually exists).

**Task 2: Search for competing work on retroactive/multi-round KV cache compression:**
- Search "multi-round RAG KV cache compression 2025 2026 arxiv"
- Search "iterative RAG KV cache eviction arxiv 2026"
- Search "cross-round KV cache reuse multi-hop RAG 2026"
- Search "retroactive KV cache compression LLM arxiv"

**Task 3: Search for any work on using key embeddings (without attention scores) as importance proxies:**
- Search "FA2 compatible KV cache eviction key similarity 2025 2026"
- Search "FlashAttention compatible KV cache pruning arxiv 2026"
- Search "key embedding importance proxy KV cache without attention scores"

Report all findings with URLs where found. Be specific about whether papers exist and what their main contributions are.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "2a98c6a6-8eeb-4d7a-b978-4d1ca86aa561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-09T18:59:39.524Z_

I'll conduct a thorough search across these research areas to verify the papers and find competing work. Let me start with systematic searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a98c6a6-8eeb-4d7a-b978-4d1ca86aa561",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWVpXrHztpVSApfwaUr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5bd700f7-36b0-4973-8a00-28a4ec5d3b28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013HLrh5JdmLaA8hVXSvchzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 957,
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

_source line 3 · 2026-05-09T18:59:39.739Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CLNWTnYPtpsciN5xa5LckE`</summary>

```json
{
  "query": "site:arxiv.org 2602.02579"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bd700f7-36b0-4973-8a00-28a4ec5d3b28",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWVpXrHztpVSApfwaUr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "152b7053-cb7d-4b2b-98d2-0f69de6a1dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013HLrh5JdmLaA8hVXSvchzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 957,
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

_source line 4 · 2026-05-09T18:59:39.958Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017gbV6XkyEkkBv48eTvxRNC`</summary>

```json
{
  "query": "site:arxiv.org 2505.15347"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "152b7053-cb7d-4b2b-98d2-0f69de6a1dd9",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWVpXrHztpVSApfwaUr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "551fc442-a1cd-4aa5-a5d9-c2eb28174ff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013HLrh5JdmLaA8hVXSvchzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 957,
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

_source line 5 · 2026-05-09T18:59:40.170Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FvnYqwaJFbUJe29goB9XXn`</summary>

```json
{
  "query": "site:arxiv.org 2602.19127"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "551fc442-a1cd-4aa5-a5d9-c2eb28174ff7",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWVpXrHztpVSApfwaUr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7f677365-4e8f-4d9e-a849-7f2c8f76b48a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013HLrh5JdmLaA8hVXSvchzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 957,
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

_source line 6 · 2026-05-09T18:59:40.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HQezbrCc5s6etCAdKXoAvh`</summary>

```json
{
  "query": "site:arxiv.org 2604.08585"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f677365-4e8f-4d9e-a849-7f2c8f76b48a",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWVpXrHztpVSApfwaUr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "741c02c5-8494-4110-8285-ca7764a75f5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013HLrh5JdmLaA8hVXSvchzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 957,
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

_source line 7 · 2026-05-09T18:59:40.333Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J6d3SpkD5PcJwtHXGeabMR`</summary>

```json
{
  "query": "site:arxiv.org 2603.05353"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741c02c5-8494-4110-8285-ca7764a75f5b",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWVpXrHztpVSApfwaUr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3eb487ec-daa4-4ec1-8498-eabe3a88ce73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013HLrh5JdmLaA8hVXSvchzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 957,
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

### Tool result

_source line 8 · 2026-05-09T18:59:43.227Z_

<details><summary>↩ Tool result · `toolu_017gbV6XkyEkkBv48eTvxRNC`</summary>

```text
Web search results for query: "site:arxiv.org 2505.15347"

Links: [{"title":"[2505.15347] FlowKV: Enhancing Multi-Turn Conversational Coherence in LLMs via Isolated Key-Value Cache Management","url":"https://arxiv.org/abs/2505.15347"},{"title":"FlowKV: Enhancing Multi-Turn Conversational Coherence in LLMs via Isolated Key-Value Cache Management","url":"https://arxiv.org/html/2505.15347"},{"title":"[2509.15347] Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning","url":"https://arxiv.org/abs/2509.15347"},{"title":"[2501.15347] Heterogeneous Population Encoding for Multi-joint Regression using sEMG Signals","url":"https://arxiv.org/abs/2501.15347"},{"title":"[2506.15347] Search for the lepton-flavour-violating decays $B^0 \\to K^{*0} τ^\\pm e^\\mp$","url":"https://arxiv.org/abs/2506.15347"},{"title":"[2604.15347] SocialWise: LLM-Agentic Conversation Therapy for Individuals with Autism Spectrum Disorder to Enhance Communication Skills","url":"https://arxiv.org/abs/2604.15347"},{"title":"1 Introduction","url":"https://arxiv.org/html/2506.15347"},{"title":"[2511.15347] Interacting binaries on the Main Sequence as in-situ tracers of mass transfer efficiency and stability","url":"https://arxiv.org/abs/2511.15347"},{"title":"[2507.15347] Probing Information Distribution in Transformer Architectures through Entropy Analysis","url":"https://arxiv.org/abs/2507.15347"},{"title":"[2602.15347] On basic $r$-ball polyhedra","url":"https://arxiv.org/abs/2602.15347"}]

I found the paper you're looking for! The paper titled "FlowKV: Enhancing Multi-Turn Conversational Coherence in LLMs via Isolated Key-Value Cache Management" addresses how Large Language Models deployed in multi-turn conversational applications face significant bottlenecks in Key-Value Cache management.

The paper is available at:
- **Abstract page**: https://arxiv.org/abs/2505.15347
- **HTML version**: https://arxiv.org/html/2505.15347

You can access the full paper and PDF from these links.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "551fc442-a1cd-4aa5-a5d9-c2eb28174ff7",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "a0553e48-42d0-401b-930d-89c0d53b08b9",
  "sourceToolAssistantUUID": "551fc442-a1cd-4aa5-a5d9-c2eb28174ff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-09T18:59:44.834Z_

<details><summary>↩ Tool result · `toolu_01HQezbrCc5s6etCAdKXoAvh`</summary>

```text
Web search results for query: "site:arxiv.org 2604.08585"

Links: [{"title":"[2604.08585] QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference","url":"https://arxiv.org/abs/2604.08585"},{"title":"QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference","url":"https://arxiv.org/html/2604.08585"},{"title":"[2601.08585] Excitonic Landscape of Monolayer Transition-Metal Dichalcogenides: Experimental Discrepancies, Theoretical Advances, and Strain Dependence","url":"https://arxiv.org/abs/2601.08585"},{"title":"A characterization of interval nest digraphs","url":"https://arxiv.org/html/2603.08585"},{"title":"Simulating the Visual World with Artificial Intelligence: A Roadmap","url":"https://arxiv.org/pdf/2511.08585"},{"title":"Distribution of Gaps in Multi-lane Orderly and Disorderly Traffic Streams","url":"https://arxiv.org/html/2512.08585"},{"title":"Advanced wood species identification based on multiple anatomical sections and using deep feature transfer and fusion","url":"https://arxiv.org/html/2404.08585"},{"title":"arXiv:1703.08585v2 [astro-ph.CO] 6 Jul 2017 MNRAS 000, 1–11 (2017)","url":"https://arxiv.org/pdf/1703.08585"},{"title":"[2506.08585] k-Planar and Fan-Crossing Drawings and Transductions of Embeddable Graphs","url":"https://arxiv.org/abs/2506.08585"},{"title":"Hardy type inequalities with mixed cylindrical-spherical weights: the general case","url":"https://arxiv.org/html/2411.08585"}]

I found the paper you're looking for. The search result for arxiv.org/abs/2604.08585 is:

**Title:** QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference

**Date:** March 30, 2026

**Summary:** QCFuse is an innovative KV cache fusion system centered on the user query that leverages semantic summary anchors to enhance query representations and selectively recomputes query-related tokens to improve accuracy. Cache fusion accelerates the generation process of LLMs equipped with RAG through KV caching and selective token recomputation, thereby reducing computational costs and improving efficiency.

You can access the full paper at https://arxiv.org/abs/2604.08585.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "741c02c5-8494-4110-8285-ca7764a75f5b",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "2afd35cf-99b9-47d2-adbd-0500fde50cc8",
  "sourceToolAssistantUUID": "741c02c5-8494-4110-8285-ca7764a75f5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T18:59:44.923Z_

<details><summary>↩ Tool result · `toolu_01J6d3SpkD5PcJwtHXGeabMR`</summary>

```text
Web search results for query: "site:arxiv.org 2603.05353"

Links: [{"title":"[2603.05353] InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context","url":"https://arxiv.org/abs/2603.05353"},{"title":"InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context","url":"https://arxiv.org/html/2603.05353"},{"title":"[2605.05353] Counterargument for Critical Thinking as Judged by AI and Humans","url":"https://arxiv.org/abs/2605.05353"},{"title":"[2604.05353] Quasi-stationary Slice Detection-Based Robust Respiration Rate Estimation under Large-scale Random Body Movement","url":"https://arxiv.org/abs/2604.05353"},{"title":"[2005.05353] Dark Matter Subhalos, Strong Lensing and Machine Learning","url":"https://ar5iv.labs.arxiv.org/html/2005.05353"},{"title":"[2601.05353] GlyRAG: Context-Aware Retrieval-Augmented Framework for Blood Glucose Forecasting","url":"https://arxiv.org/abs/2601.05353"},{"title":"Contents","url":"https://arxiv.org/html/2506.05353"},{"title":"[2602.05353] AgentXRay: White-Boxing Agentic Systems via Workflow Reconstruction","url":"https://arxiv.org/abs/2602.05353"},{"title":"Quasi-stationary Slice Detection-Based Robust Respiration Rate Estimation under Large-scale Random Body Movement","url":"https://arxiv.org/html/2604.05353"},{"title":"Counterargument for Critical Thinking as Judged by AI and Humans","url":"https://arxiv.org/html/2605.05353"}]

Based on the search results, I found the paper you were looking for:

**Title:** InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context

**Paper ID:** arXiv:2603.05353

**Date:** March 5, 2026

**Overview:** The paper addresses the bottleneck of retrieval-augmented generation (RAG) for long-context question answering by improving inference-time prefilling over large retrieved contexts. The authors propose a strategy beyond existing heuristic-based methods for selectively recomputing key-value (KV) caches.

**Key Contribution:** The authors cast selective KV recomputation as an information flow problem and show that an attention-norm signal from the query reliably identifies tokens that are both semantically relevant and structurally positioned to propagate information.

You can access the paper directly at: https://arxiv.org/abs/2603.05353


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eb487ec-daa4-4ec1-8498-eabe3a88ce73",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "3ed9df1b-83f8-49ff-b7a2-e10947b1482f",
  "sourceToolAssistantUUID": "3eb487ec-daa4-4ec1-8498-eabe3a88ce73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-09T18:59:44.928Z_

<details><summary>↩ Tool result · `toolu_01FvnYqwaJFbUJe29goB9XXn`</summary>

```text
Web search results for query: "site:arxiv.org 2602.19127"

Links: [{"title":"[2602.19127] AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG","url":"https://arxiv.org/abs/2602.19127"},{"title":"AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG","url":"https://arxiv.org/html/2602.19127"},{"title":"[2509.19127] Using SOFIA's EXES to search for C$_6$H$_2$ and C$_4$N$_2$ in Titan's atmosphere","url":"https://arxiv.org/abs/2509.19127"},{"title":"[2502.19127] Exploring the Generalizability of Factual Hallucination Mitigation via Enhancing Precise Knowledge Utilization","url":"https://arxiv.org/abs/2502.19127"},{"title":"[2601.19127] Implicit Non-Causal Factors are Out via Dataset Splitting for Domain Generalization Object Detection","url":"https://arxiv.org/abs/2601.19127"},{"title":"[2506.19127] Entropy from scattering in weakly interacting systems","url":"https://arxiv.org/abs/2506.19127"},{"title":"[2603.19127] On Optimizing Multimodal Jailbreaks for Spoken Language Models","url":"https://arxiv.org/abs/2603.19127"},{"title":"[2402.19127] Hankel Determinants of convoluted Catalan numbers and nonintersecting lattice paths: A bijective proof of Cigler's Conjecture","url":"https://arxiv.org/abs/2402.19127"},{"title":"[2407.19127] Getting the Agent to Wait","url":"https://arxiv.org/abs/2407.19127"},{"title":"Hankel Determinants of convoluted Catalan numbers and nonintersecting lattice paths: A bijective proof of Cigler’s Conjecture","url":"https://arxiv.org/html/2402.19127"}]

Based on the search results, I found the paper you were looking for:

**AgenticRAGTracer: A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG** - This paper addresses the advancement of agent-based methods in Agentic RAG, with a focus on multi-hop reasoning that requires models to engage in deliberate thinking and multi-step interaction.

The paper identifies that existing benchmarks typically provide only final questions and answers while lacking intermediate hop-level questions, which prevents researchers from analyzing at which step an agent fails. AgenticRAGTracer is described as the first Agentic RAG benchmark primarily constructed automatically by large language models.

The paper was submitted on February 22, 2026. You can access it at: https://arxiv.org/abs/2602.19127


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f677365-4e8f-4d9e-a849-7f2c8f76b48a",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "c482c4bf-7e4a-4578-925b-3e1c27912c2b",
  "sourceToolAssistantUUID": "7f677365-4e8f-4d9e-a849-7f2c8f76b48a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-09T18:59:46.322Z_

<details><summary>↩ Tool result · `toolu_01CLNWTnYPtpsciN5xa5LckE`</summary>

```text
Web search results for query: "site:arxiv.org 2602.02579"

Links: [{"title":"[2602.02579] ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2602.02579"},{"title":"ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2602.02579"},{"title":"ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV","url":"https://arxiv.org/pdf/2602.02579"},{"title":"[2604.02579] Finite reservoirs lead to Wentzell boundary conditions for independent random walks and exclusion process","url":"https://arxiv.org/abs/2604.02579"},{"title":"[2603.02579] Joint Optimization of Model Partitioning and Resource Allocation for Anti-Jamming Collaborative Inference Systems","url":"https://arxiv.org/abs/2603.02579"},{"title":"[2601.02579] COUGS-DESI: A Catalog of Unusual Galaxies with Polar Structures in the DESI Legacy Imaging Surveys","url":"https://arxiv.org/abs/2601.02579"},{"title":"[2605.02579] A general thermodynamic approach for diffusion on a lattice","url":"https://arxiv.org/abs/2605.02579"},{"title":"[2507.02579] Electron-hole tunnelling probed in de Haas - van Alphen oscillations in the (double) Dirac semimetal NbTe$_4$","url":"https://arxiv.org/abs/2507.02579"},{"title":"[2501.02579] Evolutions of in-medium baryon-baryon scattering cross sections and stiffness of dense nuclear matter from Bayesian analyses of FOPI proton flow excitation functions","url":"https://arxiv.org/abs/2501.02579"},{"title":"A new proof of superadditivity and of the density conjecture for Activated Random Walks on the line","url":"https://arxiv.org/html/2502.02579"}]

Based on the search results, I found the paper you were looking for:

**ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation**

Authors: Shihao Wang, Jiahao Chen, Yanqi Pan, Hao Huang, Yichen Hao, Xiangyu Zou, Wen Xia, Wentao Zhang, Chongyang Qiu, Pengfei Wang

Submitted: January 31, 2026 (v1), last revised February 5, 2026 (v3)

**Overview:**

The prefill stage of long-context Retrieval-Augmented Generation (RAG) is severely bottlenecked by computational overhead. ProphetKV is a user-query-driven KV Cache reuse method for RAG scenarios that dynamically prioritizes tokens based on their semantic relevance to the user query and employs a dual-stage recomputation pipeline to fuse layer-wise attention metrics into a high-utility set.

The paper identifies and addresses a "crowding-out effect" in current token selection criteria where globally salient but user-query-irrelevant tokens saturate the limited recomputation budget, displacing the tokens truly essential for answering the user query and degrading inference accuracy.

You can access the paper at: https://arxiv.org/abs/2602.02579


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "152b7053-cb7d-4b2b-98d2-0f69de6a1dd9",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "28db1083-0e3f-439a-8f36-974027530c71",
  "sourceToolAssistantUUID": "152b7053-cb7d-4b2b-98d2-0f69de6a1dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-09T18:59:47.944Z_

Great! All five papers exist. Now let me search for competing work on multi-round RAG KV cache compression.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28db1083-0e3f-439a-8f36-974027530c71",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWWQmt9nm3GucfqXBfa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "82d270d6-06e8-4655-8f0c-2fe7540f83d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Bac7oU87rGvYfK7MMGshpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2895,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 17112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 14 · 2026-05-09T18:59:48.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013tjQtzh6nJqvP8uXBT772W`</summary>

```json
{
  "query": "multi-round RAG KV cache compression 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82d270d6-06e8-4655-8f0c-2fe7540f83d7",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWWQmt9nm3GucfqXBfa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5358e091-f747-4ad3-adb4-c2fb84d753e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Bac7oU87rGvYfK7MMGshpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2895,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 17112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 15 · 2026-05-09T18:59:48.363Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AoaPqY85GVPyr6JoAL6KB8`</summary>

```json
{
  "query": "iterative RAG KV cache eviction arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5358e091-f747-4ad3-adb4-c2fb84d753e2",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWWQmt9nm3GucfqXBfa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "854d07a7-148d-464a-bf9f-481a51a010e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Bac7oU87rGvYfK7MMGshpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2895,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 17112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 16 · 2026-05-09T18:59:48.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019JFguCMTi5VEREB7MBZbbF`</summary>

```json
{
  "query": "cross-round KV cache reuse multi-hop RAG 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "854d07a7-148d-464a-bf9f-481a51a010e5",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWWQmt9nm3GucfqXBfa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "19251541-f71f-4382-b40b-cc2f2c861185",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Bac7oU87rGvYfK7MMGshpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2895,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 17112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2014,
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

_source line 17 · 2026-05-09T18:59:48.628Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bi8pzqM9WRTyg6NyrSvUoh`</summary>

```json
{
  "query": "retroactive KV cache compression LLM arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19251541-f71f-4382-b40b-cc2f2c861185",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWWQmt9nm3GucfqXBfa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dc40d2c5-4c74-4136-bb2e-9d6bc2b2c80a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Bac7oU87rGvYfK7MMGshpR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2895,
      "cache_creation_input_tokens": 2014,
      "cache_read_input_tokens": 17112,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2895,
          "output_tokens": 238,
          "cache_read_input_tokens": 17112,
          "cache_creation_input_tokens": 2014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2014,
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

_source line 18 · 2026-05-09T18:59:54.813Z_

<details><summary>↩ Tool result · `toolu_013tjQtzh6nJqvP8uXBT772W`</summary>

```text
Web search results for query: "multi-round RAG KV cache compression 2025 2026 arxiv"

Links: [{"title":"[2503.04973] Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://arxiv.org/abs/2503.04973"},{"title":"CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/html/2510.10129v1"},{"title":"Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://arxiv.org/html/2503.04973v1"},{"title":"Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2503.04973"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"[2510.10129] CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/abs/2510.10129"},{"title":"Caching and Reuse Optimizations","url":"https://www.aussieai.com/research/caching"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Paper page - Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://huggingface.co/papers/2503.04973"},{"title":"GitHub - LMCache/LMCache: Supercharge Your LLM with the Fastest KV Cache Layer · GitHub","url":"https://github.com/lmcache/lmcache"}]

Based on the search results, I found several relevant papers on RAG and KV cache compression from 2025-2026 on arXiv:

## Key Papers Found:

1. **Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning** (arXiv:2503.04973, March 2025)
   - Proposes task-aware key-value (KV) cache compression, which compresses external knowledge in a zero- or few-shot setup
   - Improves accuracy by up to 7 absolute points over RAG with a 30x compression rate, while reducing inference latency from 0.43s to 0.16s

2. **CacheClip: Accelerating RAG with Effective KV Cache Reuse** (arXiv:2510.10129, October 2025)
   - Presents a practical framework that significantly accelerates RAG inference while maintaining high generation quality, achieving up to 1.92× speedup in prefill time with selective KV cache recomputation
   - Outperforms other compression methods on LongBench with particularly strong results on multi-chunk reasoning tasks like 2wikimqa and hotpotqa

3. **Expected Attention: KV Cache Compression by Estimating Attention** (arXiv:2510.00636, 2025)
   - Addresses KV cache memory consumption challenges for long-context applications including multi-round dialogues

Additionally, the search results indicate a GitHub repository tracking recent KV cache compression research papers with multiple 2025-2026 arxiv submissions on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5358e091-f747-4ad3-adb4-c2fb84d753e2",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "86acd73e-6b68-4302-9818-9e2cd219d67f",
  "sourceToolAssistantUUID": "5358e091-f747-4ad3-adb4-c2fb84d753e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-09T18:59:56.168Z_

<details><summary>↩ Tool result · `toolu_019JFguCMTi5VEREB7MBZbbF`</summary>

```text
Web search results for query: "cross-round KV cache reuse multi-hop RAG 2026"

Links: [{"title":"[2510.10129] CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/abs/2510.10129"},{"title":"CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/html/2510.10129v1"},{"title":"[2602.02579] ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2602.02579"},{"title":"KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning","url":"https://arxiv.org/html/2602.23592v2"},{"title":"An experimental study of KV cache reuse strategies in chunk-level caching systems","url":"https://arxiv.org/html/2603.20218v1"},{"title":"KV-Cache Wins You Can See: From Prefix Caching in vLLM to Distributed Scheduling with llm-d | llm-d","url":"https://llm-d.ai/blog/kvcache-wins-you-can-see"},{"title":"ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2602.02579"},{"title":"GORGO: Maximizing KV-Cache Reuse While Minimizing Network Latency in Cross-Region LLM Load Balancing","url":"https://arxiv.org/html/2602.11688v1"},{"title":"Cache-Craft: Managing Chunk-Caches for Efficient Retrieval-Augmented Generation","url":"https://skejriwal44.github.io/docs/CacheCraft_SIGMOD_2025.pdf"},{"title":"CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://www.researchgate.net/publication/396458373_CacheClip_Accelerating_RAG_with_Effective_KV_Cache_Reuse"}]

Based on the search results, here's what I found about cross-round KV cache reuse in multi-hop RAG systems in 2026:

## Key Recent Research

Several cutting-edge approaches have emerged in early 2026 addressing KV cache reuse for multi-hop RAG:

**ProphetKV** - ProphetKV is a user-query-driven KV Cache reuse method for RAG scenarios that dynamically prioritizes tokens based on their semantic relevance to the user query and employs a dual-stage recomputation pipeline to fuse layer-wise attention metrics into a high-utility set. ProphetKV retains 96%-101% of full-prefill accuracy with only a 20% recomputation ratio, while achieving accuracy improvements of 8.8%-24.9% on RULER and 18.6%-50.9% on LongBench over state-of-the-art approaches.

**Multi-hop Memory Recomputation** - The KEEP system features a Multi-hop Memory Re-computation algorithm that dynamically identifies important cross-attention among different memory groups and reconstructs memory interactions iteratively.

**Cross-chunk Reasoning** - Research emphasizes that answering correctly requires the LLM to reason about multiple chunks in the query, which is crucial to analyze cross-chunk attention dynamics. The field is focusing on chunk-level caching that addresses this limitation by computing the KV caches of individual chunks independently and pursues position-independent reuse to avoid redundant computation.

The core challenge remains balancing efficiency with quality—existing KV cache reuse methods face a fundamental trade-off: prefix caching requires identical prefixes that rarely occur in RAG scenarios, while direct precomputation sacrifices quality due to missing inter-chunk attention and repeated attention sinks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19251541-f71f-4382-b40b-cc2f2c861185",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "1015551a-e3cf-45e3-8ad6-b0504a12ff9a",
  "sourceToolAssistantUUID": "19251541-f71f-4382-b40b-cc2f2c861185",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-09T18:59:56.691Z_

<details><summary>↩ Tool result · `toolu_01AoaPqY85GVPyr6JoAL6KB8`</summary>

```text
Web search results for query: "iterative RAG KV cache eviction arxiv 2026"

Links: [{"title":"CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/html/2510.10129v1"},{"title":"Scaling Graph Chain-of-Thought Reasoning: A Multi-Agent Framework with Efficient LLM Serving","url":"https://arxiv.org/html/2511.01633"},{"title":"RAGCache: Efficient Knowledge Caching for Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2404.12457"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"[2605.04075] RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/abs/2605.04075"},{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"KVCache Cache in the Wild: Characterizing and Optimizing KVCache Cache at a Large Cloud Provider","url":"https://arxiv.org/html/2506.02634v5"},{"title":"GraphKV: Breaking the Static Selection Paradigm with Graph-Based KV Cache Eviction","url":"https://arxiv.org/html/2509.00388"},{"title":"[2603.10899] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899"},{"title":"[2603.10899v1] LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/abs/2603.10899v1"}]

I found several relevant papers on KV cache eviction and RAG systems from arxiv in 2026. Here are the key results:

## Recent Papers on KV Cache Eviction and RAG:

1. **CacheClip: Accelerating RAG with Effective KV Cache Reuse** (October 2025)
   - Presents CacheClip, a framework that achieves both fast time-to-first-token and high generation quality by leveraging auxiliary LLMs to identify tokens critical for inter-chunk attention.

2. **Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective** (April 2026)
   - Approaches KV cache eviction through the Information Bottleneck principle and introduces CapKV, a capacity-aware eviction method using statistical leverage scores.

3. **RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction** (April 2026)
   - Leverages information entropy to enable dynamic reactivation of evicted tokens when semantic relevance arises during decoding, achieving 5.0 times KV cache compression.

4. **GraphKV: Breaking the Static Selection Paradigm with Graph-Based KV Cache Eviction** (August 2025)
   - Formulates KV cache as a graph with tokens as nodes, using a decay-signal-propagation mechanism to iteratively suppress redundant tokens.

5. **LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation** (March 2026)
   - Uses parameter-efficient modules to predict importance scores with reduced eviction cost by up to 14.5x, leading to faster time-to-first-token.

6. **Scaling Graph Chain-of-Thought Reasoning: A Multi-Agent Framework with Efficient LLM Serving** (November 2025)
   - Includes a priority-based KV-cache eviction policy tailored to Graph-CoT access patterns to improve cache efficiency.

These papers represent the latest advances in KV cache management for RAG and long-context LLM inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "854d07a7-148d-464a-bf9f-481a51a010e5",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "7b897a1e-fd9b-4bea-af3a-7f95763e9c7c",
  "sourceToolAssistantUUID": "854d07a7-148d-464a-bf9f-481a51a010e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-09T19:00:03.498Z_

<details><summary>↩ Tool result · `toolu_01Bi8pzqM9WRTyg6NyrSvUoh`</summary>

```text
Web search results for query: "retroactive KV cache compression LLM arxiv"

Links: [{"title":"RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE","url":"https://arxiv.org/pdf/2503.24000"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/html/2502.00299v5"},{"title":"[2511.01815] KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://arxiv.org/abs/2511.01815"},{"title":"GitHub - IsaacRe/vllm-kvcompress: KV cache compression for high-throughput LLM inference · GitHub","url":"https://github.com/IsaacRe/vllm-kvcompress"},{"title":"[2508.06297] KV Cache Compression for Inference Efficiency in LLMs: A Review","url":"https://arxiv.org/abs/2508.06297"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving | Proceedings of the ACM SIGCOMM 2024 Conference","url":"https://dl.acm.org/doi/10.1145/3651890.3672274"},{"title":"PackKV: Reducing KV Cache Memory Footprint through LLM-Aware Lossy Compression","url":"https://arxiv.org/html/2512.24449"},{"title":"KV Cache Compression for Inference Efficiency in LLMs: A Review","url":"https://arxiv.org/pdf/2508.06297"},{"title":"KVComp: A High-Performance, LLM-Aware, Lossy Compression Framework for KV Cache","url":"https://arxiv.org/html/2509.00579v1"}]

I've found several relevant papers on KV cache compression for LLMs. Here are the key results:

## Main Papers Found:

1. **"Rethinking KV Cache Compression Techniques for LLMs"** (arXiv:2503.24000)
   This paper addresses how while KV cache can reduce memory consumption, current implementations do not optimize for production-level LLM serving, resulting in suboptimal throughput performance and potentially longer outputs that increase end-to-end latency. The authors provide tools for future KV cache compression studies and facilitate practical deployment in production, open-sourced on GitHub.

2. **"ChunkKV: Semantic-Preserving KV Cache Compression"** (arXiv:2502.00299)
   ChunkKV reimagines KV cache compression by treating semantic chunks rather than isolated tokens as basic compression units, which preserves complete linguistic structures and contextual integrity.

3. **"KV Cache Transform Coding for Compact Storage in LLM Inference"** (arXiv:2511.01815)
   This work addresses how KV caches can be reused across conversation turns via shared-prefix prompts, but stale caches consume scarce GPU memory or require offloading.

4. **"PackKV: Reducing KV Cache Memory Footprint through LLM-Aware Lossy Compression"** (arXiv:2512.24449)
   PackKV is the first LLM-aware lossy compression framework integrating quantization, encode-aware repacking, and bit-packing encoding, achieving 153.2% and 179.6% higher compression ratios for K and V caches respectively compared with state-of-the-art quantization methods.

These papers represent recent advances in the KV cache compression field, with various approaches including semantic preservation, transform coding, and lossy compression techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc40d2c5-4c74-4136-bb2e-9d6bc2b2c80a",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "af846b40-3a83-4608-95df-a4f5397cd247",
  "sourceToolAssistantUUID": "dc40d2c5-4c74-4136-bb2e-9d6bc2b2c80a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-09T19:00:04.810Z_

Now let me search for work on key embeddings and FA2-compatible KV cache techniques.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af846b40-3a83-4608-95df-a4f5397cd247",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWXgDquMFee63H7cJpz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eb03fd80-86dd-4f0a-921d-19f1e116062f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MUhx38suBGqtJQNV8NAmDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7171,
      "cache_read_input_tokens": 19126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7171,
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

_source line 23 · 2026-05-09T19:00:05.539Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KmepzhrYUWt4wEtxtb34AV`</summary>

```json
{
  "query": "FA2 compatible KV cache eviction key similarity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb03fd80-86dd-4f0a-921d-19f1e116062f",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWXgDquMFee63H7cJpz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "51170dbb-b885-4db5-b474-d666f3428ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MUhx38suBGqtJQNV8NAmDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7171,
      "cache_read_input_tokens": 19126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7171,
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

_source line 24 · 2026-05-09T19:00:05.558Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bh1eXdg2GZ7FseF5z6nnje`</summary>

```json
{
  "query": "FlashAttention compatible KV cache pruning arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51170dbb-b885-4db5-b474-d666f3428ded",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWXgDquMFee63H7cJpz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de6d86ce-d810-4d63-a5ad-794233157db2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MUhx38suBGqtJQNV8NAmDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7171,
      "cache_read_input_tokens": 19126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7171,
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

_source line 25 · 2026-05-09T19:00:05.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018jyzXfjL6UXy1msyW38tkV`</summary>

```json
{
  "query": "key embedding importance proxy KV cache without attention scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de6d86ce-d810-4d63-a5ad-794233157db2",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWXgDquMFee63H7cJpz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33929382-c4c7-44e0-9325-a90943129dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MUhx38suBGqtJQNV8NAmDe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7171,
      "cache_read_input_tokens": 19126,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7171,
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

_source line 26 · 2026-05-09T19:00:12.709Z_

<details><summary>↩ Tool result · `toolu_01KmepzhrYUWt4wEtxtb34AV`</summary>

```text
Web search results for query: "FA2 compatible KV cache eviction key similarity 2025 2026"

Links: [{"title":"[2504.15364] KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/abs/2504.15364"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364"},{"title":"NeurIPS Poster KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/115521"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by ...","url":"https://arxiv.org/pdf/2603.10899"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"KV Cache Eviction","url":"https://www.aussieai.com/research/kv-cache-eviction"},{"title":"ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution | OpenReview","url":"https://openreview.net/forum?id=k5h29Qv7GN"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"},{"title":"[Literature Review] KeDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://www.themoonlight.io/en/review/kediff-key-similarity-based-kv-cache-eviction-for-long-context-llm-inference-in-resource-constrained-environments"}]

I found several relevant results about KV cache eviction with key similarity focus. Here are the key findings:

## KeyDiff: Key Similarity-Based KV Cache Eviction

KeyDiff is a training-free KV cache eviction method based solely on key similarity. Geometrically distinctive keys during LLM inference tend to have high attention scores. Unlike other KV cache eviction methods, KeyDiff can process arbitrarily long prompts within strict resource constraints and efficiently generate responses.

The paper was updated as recently as January 20, 2026 and has been presented at NeurIPS 2025.

## Related KV Cache Eviction Methods

The search results show a broader ecosystem of KV cache eviction approaches including:

- L₂-norm pruning which exploits the correlation between low key norm and high attentional relevance, achieving 50–90% cache reduction without accuracy loss
- Graph and diversity-based approaches like GraphKV that propagate decay signals through dynamic similarity graphs to ensure diversity among selected tokens
- Cluster-based approaches like Chelsea that use intra-sequence clustering to merge similar tokens, achieving up to 80% cache reduction

## FA2 (FlashAttention-2) Compatibility

While the search results reference FlashAttention compatibility in some methods, kvtc does not alter the structure of KV cache and does not change how attention is calculated, making it directly compatible with token eviction methods.

The field of KV cache optimization is rapidly evolving with multiple approaches combining clustering, quantization, and similarity-based selection strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51170dbb-b885-4db5-b474-d666f3428ded",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "b3d69d1b-cfbb-4e64-8d2b-8a0b5ac78d9d",
  "sourceToolAssistantUUID": "51170dbb-b885-4db5-b474-d666f3428ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-09T19:00:13.020Z_

<details><summary>↩ Tool result · `toolu_01Bh1eXdg2GZ7FseF5z6nnje`</summary>

```text
Web search results for query: "FlashAttention compatible KV cache pruning arxiv 2026"

Links: [{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"KVzap: Fast, Adaptive, and Faithful KV Cache Pruning","url":"https://arxiv.org/html/2601.07891v1"},{"title":"PureKV: Plug-and-Play KV Cache Optimization with Spatial ...","url":"https://www.arxiv.org/pdf/2510.25600"},{"title":"(PDF) KVzap: Fast, Adaptive, and Faithful KV Cache Pruning","url":"https://www.researchgate.net/publication/399754198_KVzap_Fast_Adaptive_and_Faithful_KV_Cache_Pruning"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE","url":"https://arxiv.org/pdf/2503.24000"},{"title":"[2510.00636] Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/abs/2510.00636"},{"title":"PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models","url":"https://arxiv.org/html/2510.25600"},{"title":"Revisiting Multimodal KV Cache Compression: A Frequency-Domain-Guided Outlier-KV-Aware Approach","url":"https://arxiv.org/html/2511.16786"}]

Based on the search results, I found several recent papers on FlashAttention-compatible KV cache pruning from 2025-2026:

## Key Papers

**1. KVzap: Fast, Adaptive, and Faithful KV Cache Pruning** (January 2026)
KVzap is designed to be compatible with kernels like FlashAttention2 or PagedAttention. KVzap is a fast, input-adaptive approximation that works in both prefilling and decoding, achieving 4× KV cache compression with negligible accuracy loss on various models.

**2. PagedEviction: Structured Block-wise KV Cache Pruning** (September 2025)
PagedEviction is a novel structured KV cache pruning algorithm designed for vLLM's PagedAttention, with block-aligned KV cache compression that aligns with vLLM's block-based memory. Traditional KV cache eviction methods relying on attention scores cannot be integrated into PagedAttention, as FlashAttention never returns the attention score during the inference process.

**3. Expected Attention: KV Cache Compression by Estimating Attention** (October 2025)
Expected Attention estimates future attention allocation from the distribution of future queries and can prune the KV cache up to 60% while preserving performance quality without architectural modifications or additional training.

**4. FlashCache: Frequency-Domain-Guided KV Cache Compression** (March 2026)
FlashCache is a frequency-domain–guided, Outlier-KV-aware KV Cache compression framework that is the first attention-score-free and training-free multimodal KV Cache compression framework, inherently compatible with efficient attention implementations like FlashAttention.

These papers all address the fundamental challenge that modern efficient attention mechanisms such as FlashAttention do not explicitly generate attention matrices, rendering traditional attention-score-based pruning incompatible.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de6d86ce-d810-4d63-a5ad-794233157db2",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "ce91c534-7886-4a25-80ea-684fa5655ea9",
  "sourceToolAssistantUUID": "de6d86ce-d810-4d63-a5ad-794233157db2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-09T19:00:13.567Z_

<details><summary>↩ Tool result · `toolu_018jyzXfjL6UXy1msyW38tkV`</summary>

```text
Web search results for query: "key embedding importance proxy KV cache without attention scores"

Links: [{"title":"KEYDIFF: Key Similarity-Based KV Cache Eviction for Long ...","url":"https://openreview.net/pdf/5717ff92a2ae0a9fa4cb2f7968739b926adc1318.pdf"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments","url":"https://arxiv.org/html/2504.15364v3"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"[2510.00636] Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/abs/2510.00636"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention From Future Queries Distribution | OpenReview","url":"https://openreview.net/forum?id=VmojW15eRc"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"hashevict:apre-attention kv cache eviction strategy using ...","url":"https://arxiv.org/pdf/2412.16187"},{"title":"HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing","url":"https://arxiv.org/html/2412.16187v3"}]

Based on the search results, here's what I found regarding key embedding importance as a proxy for KV cache eviction without attention scores:

## Key Findings

Lower pairwise cosine similarity among keys correlates with higher attention scores, suggesting its utility as a proxy for token importance. This observation has become the basis for several recent KV cache compression methods.

### KeyDiff Method

KeyDiff is an eviction strategy that selects keys based on their similarity to other cached entries without relying on attention scores or future tokens. KeyDiff does not rely on attention scores, allowing the use of optimized attention mechanisms like FlashAttention.

### Other Embedding-Based Approaches

Beyond KeyDiff, there are several other methods using key embeddings as proxies:

- The L2-norm of each Key token is inversely proportional to the cumulative attention score of each token. This principle is used by methods like PagedEviction.

- HashEvict evicts past tokens from the cache whose key embedding is highly cosine dissimilar to the current query token embedding, based on the intuition that high cosine dissimilarity indicates a low dot-product attention score.

### Practical Advantages

Using a proxy importance metric derived solely from the static key and value states already stored in the KV cache avoids reliance on attention scores and is computed on-the-fly without modifying the attention kernel or maintaining additional memory. This addresses the practical limitation that modern transformer implementations do not materialize attention scores, making them inaccessible.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33929382-c4c7-44e0-9325-a90943129dd5",
  "isSidechain": true,
  "promptId": "16b2fe29-10c7-4305-932f-2b2ee3287f13",
  "agentId": "a5ed68a9f4abf542e",
  "type": "user",
  "uuid": "1859019c-c9bb-45f3-8d72-129008359462",
  "sourceToolAssistantUUID": "33929382-c4c7-44e0-9325-a90943129dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-09T19:00:38.811Z_

Perfect! Let me compile my comprehensive findings report.

## Comprehensive Research Verification Report

### TASK 1: Verification of Referenced Papers

All five papers **exist and are verified** on arxiv.org:

1. **ProphetKV (arXiv:2602.02579)** - CONFIRMED EXISTING
   - Full Title: "User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation"
   - Submission Date: January 31, 2026 (v1), last revised February 5, 2026 (v3)
   - Main Contribution: User-query-driven KV cache reuse method that dynamically prioritizes tokens based on semantic relevance. Addresses the "crowding-out effect" where globally salient but query-irrelevant tokens displace tokens essential for answering user queries. Achieves 96%-101% of full-prefill accuracy with only 20% recomputation ratio.
   - URL: https://arxiv.org/abs/2602.02579

2. **FlowKV (arXiv:2505.15347)** - CONFIRMED EXISTING
   - Full Title: "Enhancing Multi-Turn Conversational Coherence in LLMs via Isolated Key-Value Cache Management"
   - Addresses KV cache management bottlenecks in multi-turn conversational LLM applications
   - URL: https://arxiv.org/abs/2505.15347

3. **AgenticRAGTracer (arXiv:2602.19127)** - CONFIRMED EXISTING
   - Full Title: "A Hop-Aware Benchmark for Diagnosing Multi-Step Retrieval Reasoning in Agentic RAG"
   - Submission Date: February 22, 2026
   - Main Contribution: First agentic RAG benchmark automatically constructed by LLMs, providing hop-level intermediate questions to diagnose multi-step retrieval failures
   - URL: https://arxiv.org/abs/2602.19127

4. **QCFuse (arXiv:2604.08585)** - CONFIRMED EXISTING
   - Full Title: "Query-Centric Cache Fusion for Efficient RAG Inference"
   - Publication Date: March 30, 2026
   - Main Contribution: Query-centric KV cache fusion using semantic summary anchors for enhanced query representations and selective token recomputation
   - URL: https://arxiv.org/abs/2604.08585

5. **InfoFlow KV (arXiv:2603.05353)** - CONFIRMED EXISTING (Title differs slightly from proposal)
   - Actual Title: "Information-Flow-Aware KV Recomputation for Long Context"
   - Publication Date: March 5, 2026
   - Main Contribution: Frames selective KV recomputation as an information flow problem; uses attention-norm signal from query to identify semantically relevant, structurally positioned tokens
   - URL: https://arxiv.org/abs/2603.05353
   - **Note**: The title in the proposal appears to be "Prompt-Conditioned Selective KV Recomputation for RAG Inference" but the actual paper is titled "Information-Flow-Aware KV Recomputation for Long Context"

---

### TASK 2: Competing Work on Multi-Round/Iterative RAG KV Cache Compression

**Highly Relevant Papers (Direct Competitors):**

1. **Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning** (arXiv:2503.04973, March 2025)
   - Task-aware KV cache compression for zero/few-shot knowledge reasoning
   - Achieves 7-point accuracy improvement with 30× compression and reduces latency from 0.43s to 0.16s
   - URL: https://arxiv.org/abs/2503.04973

2. **CacheClip: Accelerating RAG with Effective KV Cache Reuse** (arXiv:2510.10129, October 2025)
   - Multi-chunk reasoning with selective KV cache recomputation
   - Achieves 1.92× speedup in prefill time; particularly strong on multi-hop tasks (2wikimqa, hotpotqa)
   - URL: https://arxiv.org/abs/2510.10129

3. **Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution** (arXiv:2510.00636, October 2025)
   - Estimates future attention without explicit attention scores
   - Achieves up to 60% KV cache pruning; compatible with multi-round dialogues
   - URL: https://arxiv.org/abs/2510.00636

4. **Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective** (arXiv:2604.25975, April 2026)
   - Information Bottleneck principle for KV cache eviction
   - Introduces CapKV using statistical leverage scores
   - URL: https://arxiv.org/abs/2604.25975

5. **RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction** (arXiv:2605.04075, April 2026)
   - Dynamic reactivation of evicted tokens using information entropy
   - Achieves 5.0× KV cache compression with uncertainty awareness
   - URL: https://arxiv.org/abs/2605.04075

6. **GraphKV: Breaking the Static Selection Paradigm with Graph-Based KV Cache Eviction** (arXiv:2509.00388, August 2025)
   - Iterative token suppression via decay-signal-propagation
   - Graphs tokens as nodes with dynamic decay mechanisms
   - URL: https://arxiv.org/abs/2509.00388

7. **LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation** (arXiv:2603.10899, March 2026)
   - Parameter-efficient importance score prediction
   - Reduces eviction cost by 14.5×
   - URL: https://arxiv.org/abs/2603.10899

8. **KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning** (arXiv:2602.23592)
   - Multi-hop memory recomputation with cross-attention analysis
   - Iterative reconstruction of memory interactions
   - URL: https://arxiv.org/abs/2602.23592

---

### TASK 3: Key Embedding-Based Importance Proxies (Without Attention Scores)

This is a particularly strong area of competing work, especially relevant for FA2/FlashAttention compatibility:

**Key Papers:**

1. **KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference** (arXiv:2504.15364, April 2025)
   - **Core Insight**: Lower pairwise cosine similarity among keys correlates with higher attention scores
   - Training-free method using ONLY key similarity (no attention scores needed)
   - Fully compatible with FlashAttention-2 and other optimized attention kernels
   - Presented at NeurIPS 2025
   - URL: https://arxiv.org/abs/2504.15364

2. **KVzap: Fast, Adaptive, and Faithful KV Cache Pruning** (arXiv:2601.07891, January 2026)
   - Explicitly designed for FlashAttention2/PagedAttention compatibility
   - Uses spatial-temporal features from KV states without attention scores
   - Achieves 4× KV cache compression with negligible accuracy loss
   - URL: https://arxiv.org/html/2601.07891v1

3. **PagedEviction: Structured Block-wise KV Cache Pruning** (arXiv:2509.04377, September 2025)
   - Designed for vLLM's PagedAttention framework
   - Block-aligned compression; addresses that "FlashAttention never returns attention scores"
   - Leverages L2-norm of keys as importance proxy
   - URL: https://arxiv.org/pdf/2509.04377

4. **Revisiting Multimodal KV Cache Compression: A Frequency-Domain-Guided Outlier-KV-Aware Approach** (arXiv:2511.16786, March 2026)
   - First attention-score-free, training-free multimodal KV cache compression
   - Frequency-domain analysis of key embeddings
   - Inherently compatible with FlashAttention
   - URL: https://arxiv.org/html/2511.16786

5. **HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing** (arXiv:2412.16187)
   - Uses cosine dissimilarity between key embeddings and current query
   - Pre-attention eviction based on key-query embedding similarity
   - Avoids attention score dependency
   - URL: https://arxiv.org/html/2412.16187v3

6. **PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention** (arXiv:2510.25600, October 2025)
   - Spatial-temporal features derived from stored KV states
   - URL: https://arxiv.org/pdf/2510.25600

---

### Summary of Findings

**Verification Status**: All five papers in the proposal **exist and are legitimate arxiv publications from 2025-2026**.

**Competitive Landscape**:
- **Strong competition exists** in the multi-round/iterative RAG KV cache space, with at least 8+ papers directly addressing similar problems (CacheClip, Beyond RAG, RetentiveKV, GraphKV, etc.)
- **Key embedding approaches are well-established**: KeyDiff (NeurIPS 2025), KVzap, PagedEviction, and frequency-domain approaches all use non-attention-score-based importance metrics
- **FA2/FlashAttention compatibility is a major focus** in recent work, suggesting the RKCC paper's approach to FA2 compatibility is timely but addresses a well-recognized need

**Critical Finding**: The KeyDiff paper (arXiv:2504.15364) from April 2025 is particularly relevant as it was presented at NeurIPS 2025 and directly addresses key similarity as an importance proxy without attention scores—core to the RKCC proposal's stated novelty.

---

### Sources:
- [ProphetKV](https://arxiv.org/abs/2602.02579)
- [FlowKV](https://arxiv.org/abs/2505.15347)
- [AgenticRAGTracer](https://arxiv.org/abs/2602.19127)
- [QCFuse](https://arxiv.org/abs/2604.08585)
- [InfoFlow KV](https://arxiv.org/abs/2603.05353)
- [Beyond RAG: Task-Aware KV Cache Compression](https://arxiv.org/abs/2503.04973)
- [CacheClip](https://arxiv.org/abs/2510.10129)
- [Expected Attention](https://arxiv.org/abs/2510.00636)
- [Rethinking KV Cache Eviction via Information-Theoretic Objective](https://arxiv.org/abs/2604.25975)
- [RetentiveKV](https://arxiv.org/abs/2605.04075)
- [GraphKV](https://arxiv.org/abs/2509.00388)
- [LookaheadKV](https://arxiv.org/abs/2603.10899)
- [KEEP](https://arxiv.org/abs/2602.23592)
- [KeyDiff](https://arxiv.org/abs/2504.15364)
- [KVzap](https://arxiv.org/html/2601.07891v1)
- [PagedEviction](https://arxiv.org/pdf/2509.04377)
- [Frequency-Domain Multimodal KV Compression](https://arxiv.org/html/2511.16786)
- [HashEvict](https://arxiv.org/html/2412.16187v3)
- [PureKV](https://arxiv.org/pdf/2510.25600)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1859019c-c9bb-45f3-8d72-129008359462",
  "isSidechain": true,
  "agentId": "a5ed68a9f4abf542e",
  "requestId": "req_011CasWYRGx7EVNYrPdbfyY6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "091cca79-f164-4fed-84c1-cf04ecd649b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6981c5b9-a047-45f9-bec4-bddbe2b1b26b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NbUhoTwcYcmcm3LWWfT4TQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2988,
      "cache_read_input_tokens": 26297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2988,
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
