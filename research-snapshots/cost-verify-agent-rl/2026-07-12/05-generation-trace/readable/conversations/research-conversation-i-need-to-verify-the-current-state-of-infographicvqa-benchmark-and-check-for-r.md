# Research conversation: I need to verify the current state of InfographicVQA benchmark and check for recent competing work in document layout mu

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6875d57d542245b6.jsonl`
- **Structured JSON:** [`4ba68e759f5a7077d3b6.json`](../../sessions/4b/4ba68e759f5a7077d3b6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-10T09:18:26.418Z_

I need to verify the current state of InfographicVQA benchmark and check for recent competing work in document layout multi-hop reasoning. Please search for:

1. Current InfographicVQA SOTA — is Qwen2.5-VL-72B still at 87.3% ANLS, or has this been surpassed in early 2026? Is any model above 90%?

2. Any papers from late 2025 or 2026 that propose typed graph traversal or explicit chain-of-thought over document layout regions (Table, Figure, Caption, TextBlock nodes with typed edges). This would be competitive work to "LHEC" approach.

3. Any papers proposing explicit verbalized traversal traces for document reasoning that might have scooped the approach.

Please search using WebSearch with queries like:
- "InfographicVQA leaderboard SOTA 2025 2026"
- "document layout graph traversal VQA 2025 2026"
- "typed spatial graph document reasoning chain-of-thought 2026"
- "multi-hop document layout reasoning VLM 2025 2026"

Report: current InfographicVQA SOTA, any new work that competes with typed document graph traversal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "89a0440b-3165-44df-9f81-f5019844d1d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T09:18:27.514Z_

I'll search for the current state of InfographicVQA SOTA and competing work on document layout reasoning. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89a0440b-3165-44df-9f81-f5019844d1d6",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzBH8BsWedT2ctRieR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e1d2a50a-7b41-419d-b1b5-f2cc853b4449",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KMK57sDbuNvXhns49XQJce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 716,
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

_source line 3 · 2026-05-10T09:18:27.747Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JLymCB6PmDNRwP7Vh9Rswm`</summary>

```json
{
  "query": "InfographicVQA leaderboard SOTA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1d2a50a-7b41-419d-b1b5-f2cc853b4449",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzBH8BsWedT2ctRieR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2c5f58ec-2c5c-4a0f-8abe-1b5d7c46774c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KMK57sDbuNvXhns49XQJce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 716,
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

_source line 4 · 2026-05-10T09:18:27.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CSFEACu5DgsEk6p6YAafpo`</summary>

```json
{
  "query": "document layout graph traversal VQA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c5f58ec-2c5c-4a0f-8abe-1b5d7c46774c",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzBH8BsWedT2ctRieR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7792278e-f070-4115-8b8e-9b85532caff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KMK57sDbuNvXhns49XQJce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 716,
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

_source line 5 · 2026-05-10T09:18:27.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FKq9TR8A7yFERVt8Fu6mZQ`</summary>

```json
{
  "query": "typed spatial graph document reasoning chain-of-thought 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7792278e-f070-4115-8b8e-9b85532caff9",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzBH8BsWedT2ctRieR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "83bb7e07-c329-4469-a0fe-263531974da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KMK57sDbuNvXhns49XQJce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 716,
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

_source line 6 · 2026-05-10T09:18:28.066Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H6ZrkbeWPewTceQCByDbf7`</summary>

```json
{
  "query": "multi-hop document layout reasoning VLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83bb7e07-c329-4469-a0fe-263531974da9",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzBH8BsWedT2ctRieR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e41ca4b-9c45-437a-bbc8-d7d5217e70b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KMK57sDbuNvXhns49XQJce",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 16155,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 716
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 247,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 716,
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

_source line 7 · 2026-05-10T09:18:31.897Z_

<details><summary>↩ Tool result · `toolu_01JLymCB6PmDNRwP7Vh9Rswm`</summary>

```text
Web search results for query: "InfographicVQA leaderboard SOTA 2025 2026"

Links: [{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"DocVQA","url":"https://www.docvqa.org/"},{"title":"Speech AI Leaderboard 2026: Best STT, ASR and TTS Models | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/speech"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"AI Trends (May 2026) — AI Trend Analysis, LLM Statistics & Industry Insights","url":"https://llm-stats.com/ai-trends"},{"title":"SOTA AI Models: Benchmarks, Metrics & Deployment Guide","url":"https://huggingface.co/blog/daya-shankar/sota-ai-models"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"How To Evaluate State‑Of‑The‑Art LLM Models: A Complete Guide | Deepchecks","url":"https://www.deepchecks.com/evaluate-state-of-the-art-llm-models/"},{"title":"[2104.12756] InfographicVQA","url":"https://arxiv.org/abs/2104.12756"}]

Based on the search results, I found information about InfographicVQA. InfographicVQA is a dataset that comprises a diverse collection of infographics along with natural language questions and answers annotations. The collected questions require methods to jointly reason over the document layout, textual content, graphical elements, and data visualizations.

The original research paper indicates that the dataset, code and leaderboard will be made available at http://docvqa.org. I found a reference that InfographicVQA arXiv preprint was available in April 2021 and 2021 Edition of the DocVQA challenge leaderboards are public.

However, the search results do not contain specific current SOTA (State-of-the-Art) leaderboard information for InfographicVQA from 2025-2026. To access the most up-to-date leaderboard results, you would need to visit the official DocVQA website at http://docvqa.org where the leaderboards are hosted.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c5f58ec-2c5c-4a0f-8abe-1b5d7c46774c",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "5e40afbc-6b61-4027-9d75-886478d5478c",
  "sourceToolAssistantUUID": "2c5f58ec-2c5c-4a0f-8abe-1b5d7c46774c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T09:18:33.818Z_

<details><summary>↩ Tool result · `toolu_01FKq9TR8A7yFERVt8Fu6mZQ`</summary>

```text
Web search results for query: "typed spatial graph document reasoning chain-of-thought 2026"

Links: [{"title":"[2404.07103] Graph Chain-of-Thought: Augmenting Large Language Models by Reasoning on Graphs","url":"https://arxiv.org/abs/2404.07103"},{"title":"GitHub - yaotingwangofficial/Awesome-MCoT: Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey · GitHub","url":"https://github.com/yaotingwangofficial/Awesome-MCoT"},{"title":"Graph Chain-of-Thought: Augmenting Large Language Models by Reasoning on Graphs - Penn State","url":"https://pure.psu.edu/en/publications/graph-chain-of-thought-augmenting-large-language-models-by-reason/"},{"title":"GitHub - PeterGriffinJin/Graph-CoT: Graph Chain-of-Thought: Augmenting Large Language Models by Reasoning on Graphs (ACL 2024) · GitHub","url":"https://github.com/PeterGriffinJin/Graph-CoT"},{"title":"Graph Chain-of-Thought: Augmenting Large Language Models by Reasoning on Graphs - Illinois Experts","url":"https://experts.illinois.edu/en/publications/graph-chain-of-thought-augmenting-large-language-models-by-reason/"},{"title":"Preprint. SCENECOT: ELICITING GROUNDED CHAIN-OF-THOUGHT REASONING IN 3D SCENES","url":"https://www.arxiv.org/pdf/2510.16714"},{"title":"[2510.09312] Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/abs/2510.09312"},{"title":"Chain-of-Symbol Prompting For Spatial Reasoning in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Hvq9RtSoHG"},{"title":"1 Demystifying Chains, Trees, and Graphs of Thoughts","url":"https://htor.inf.ethz.ch/publications/img/besta-topologies.pdf"},{"title":"Graph chain-of-thought: Augmenting large language models by reasoning on graphs - Amazon Science","url":"https://www.amazon.science/publications/graph-chain-of-thought-augmenting-large-language-models-by-reasoning-on-graphs"}]

I found relevant research related to your search query. Here's what the search results reveal:

## Key Research Findings

The search results primarily feature Graph Chain-of-Thought (Graph-CoT), a framework that augments LLMs with graphs by encouraging LLMs to reason on the graph iteratively. This work was published in 2024 at ACL (Association for Computational Linguistics).

### Graph Chain-of-Thought Framework

Each Graph-CoT iteration consists of three sub-steps: LLM reasoning, LLM-graph interaction, and graph execution. The research addresses a specific problem: Large language models (LLMs), while exhibiting exceptional performance, suffer from hallucinations, especially on knowledge-intensive tasks.

### Supporting Research Infrastructure

To facilitate this research, researchers manually constructed a Graph Reasoning Benchmark dataset called GRBench, containing 1,740 questions that can be answered with the knowledge from 10 domain graphs.

## Related Work

The search also revealed other recent approaches to spatial and document reasoning:
- Chain-of-Symbol Prompting investigates LLM performance on complex spatial planning and understanding tasks that require understanding a virtual spatial environment simulated via natural language
- Research on verifying chain-of-thought reasoning using computational graphs

The 2026 date in your query may relate to recent 2026 publications on these topics, though most of the foundational work appears to be from 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83bb7e07-c329-4469-a0fe-263531974da9",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "de82de7a-07ea-413e-9a8c-4597ef4e3a0f",
  "sourceToolAssistantUUID": "83bb7e07-c329-4469-a0fe-263531974da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T09:18:35.206Z_

<details><summary>↩ Tool result · `toolu_01H6ZrkbeWPewTceQCByDbf7`</summary>

```text
Web search results for query: "multi-hop document layout reasoning VLM 2025 2026"

Links: [{"title":"MMhops-R1: Multimodal Multi-hop Reasoning","url":"https://arxiv.org/pdf/2512.13573"},{"title":"DocVQA - Challenge 2026","url":"https://www.docvqa.org/challenges/2026"},{"title":"Ultimate Guide - The Best Multimodal AI Models in 2026","url":"https://www.siliconflow.com/articles/en/best-multimodal-ai-models"},{"title":"[2508.15851] DocHop-QA: Towards Multi-Hop Reasoning over Multimodal Document Collections","url":"https://arxiv.org/abs/2508.15851"},{"title":"DocHop-QA: Towards Multi-Hop Reasoning over Multimodal Document Collections","url":"https://arxiv.org/html/2508.15851v1"},{"title":"Turn Complex Documents into Usable Data with VLM, NVIDIA Nemotron Parse 1.1 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/turn-complex-documents-into-usable-data-with-vlm-nvidia-nemotron-parse-1-1/"},{"title":"Multi-Modal Document Understanding with Dual-Cue Page ...","url":"https://aclanthology.org/2025.emnlp-main.1443.pdf"},{"title":"Document-Packing Strategies","url":"https://www.emergentmind.com/topics/document-packing-strategies"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents | OpenReview","url":"https://openreview.net/forum?id=xpjWEgf8zi"},{"title":"[2510.09586] Vision Language Models: A Survey of 26K Papers","url":"https://arxiv.org/abs/2510.09586"}]

Based on the web search results, here's what I found about multi-hop document layout reasoning in VLMs for 2025-2026:

## Key Developments in Multi-Hop Document Reasoning

The ICDAR2026 Competition on Multimodal Reasoning over Documents (DocVQA2026) is specifically designed to evaluate models on multimodal reasoning tasks that require reasoning across multiple sources of evidence along documents.

The competition assesses spatial understanding (tested on maps, engineering drawings, and general layout tasks), temporal understanding (tested on comic stories), and multi-hop answers that require obtaining multiple evidences throughout the document.

## Benchmark Development

DocHop-QA is a large-scale benchmark comprising 11,379 QA instances for multimodal, multi-document, multi-hop question answering, constructed from scientific documents and incorporating diverse information formats including textual passages, tables, and structural layout cues.

## VLM Advances for Document Understanding

NVIDIA's NeMo Retriever Parse is a transformer-based VLM that delivers high-precision document understanding with a unique architecture featuring a heavy vision encoder and light decoder, enabling it to deeply understand complex document layouts and semantics.

SimpleDoc is a multi-modal document understanding approach consisting of offline extraction of visual embeddings and LLM-generated summaries for document pages, followed by an online reasoning loop that performs retrieval and answer generation with a memory-guided VLM agent.

The field is actively advancing with new benchmarks, competitions, and specialized VLM architectures specifically designed to handle the complexity of multi-hop reasoning over document layouts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e41ca4b-9c45-437a-bbc8-d7d5217e70b5",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "b1844e8d-77a0-479b-beb3-04bc517c0b80",
  "sourceToolAssistantUUID": "2e41ca4b-9c45-437a-bbc8-d7d5217e70b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T09:18:35.323Z_

<details><summary>↩ Tool result · `toolu_01CSFEACu5DgsEk6p6YAafpo`</summary>

```text
Web search results for query: "document layout graph traversal VQA 2025 2026"

Links: [{"title":"Enhancing Document VQA Models via Retrieval-Augmented Generation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-09368-4_6"},{"title":"GitHub - adlnlp/pdfvqa","url":"https://github.com/adlnlp/pdfvqa"},{"title":"Document Visual Question Answering","url":"https://www.emergentmind.com/topics/document-visual-question-answering-vqa"},{"title":"GRAPH-BASED DOCUMENT STRUCTURE ANALYSIS","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cf3d7d8e79703fe947deffb587a83639-Paper-Conference.pdf"},{"title":"MGA-VQA: Secure and Interpretable Graph-Augmented Visual Question Answering with Memory-Guided Protection Against Unauthorized Knowledge Use","url":"https://arxiv.org/html/2511.17881v1"},{"title":"[2508.18984] Enhancing Document VQA Models via Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2508.18984"},{"title":"Enhancing visual question answering with common sense knowledge: a data-driven neurosymbolic graph routing approach | International Journal of Data Science and Analytics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41060-025-00827-7"},{"title":"pdfvqa/README.md at main · adlnlp/pdfvqa","url":"https://github.com/adlnlp/pdfvqa/blob/main/README.md"},{"title":"PDF-VQA: A New Dataset for Real-World VQA on PDF Documents | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-43427-3_35"},{"title":"Knowledge-Enhanced VQA Architectures","url":"https://www.emergentmind.com/topics/knowledge-enhanced-vqa-architectures"}]

Based on the search results, here's what I found regarding document layout graph traversal VQA research from 2025-2026:

## Recent Research Overview

A significant work on "Enhancing Document VQA Models via Retrieval-Augmented Generation" was published in the ICDAR 2025 Workshops. This research addresses Document Visual Question Answering (DocVQA) for multi-page documents using Retrieval-Augmented Generation (RAG), systematically evaluating retrieval variants across multiple models and benchmarks.

## Graph-Based Approaches

Recent developments focus on graph-based reasoning where documents are represented as heterogeneous graphs with nodes representing elements and edges representing spatial/hierarchical relationships, with Relational GCNs yielding improved multi-hop relational understanding. 

A recent system, MGA-VQA, employs a multi-modal pipeline with five modules: token-level visual encoding, spatial graph construction, memory-augmented question processing, question-guided compression, and multi-modal spatial fusion. The spatial graph construction uses weighted graph representations over detected text spans with edges encoding geometric and semantic relationships.

## Traversal and Reasoning

Graph routing networks (GRN) explicitly reason step by step over enriched scene graphs by computing entity score vectors and transition matrices at every step to dynamically focus on question-relevant entities and relations.

Structural reasoning in multimodal knowledge graph approaches is realized through subgraph retrieval and traversal, where retrieved knowledge graph subgraphs are expanded by l-hop neighborhood via graph traversal algorithms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7792278e-f070-4115-8b8e-9b85532caff9",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "99f287ac-5746-4a92-909d-53e5d713fbdc",
  "sourceToolAssistantUUID": "7792278e-f070-4115-8b8e-9b85532caff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T09:18:36.712Z_

Now let me search more specifically for InfographicVQA performance numbers and any papers on document layout graph approaches from 2025-2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99f287ac-5746-4a92-909d-53e5d713fbdc",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzqMbHkJgsqHdrEemG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1086e308-c5f2-4189-a4c6-28b1ae685907",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CD33BEfTCJtbHM2mGrCmQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1843,
      "cache_creation_input_tokens": 2695,
      "cache_read_input_tokens": 16871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2695,
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

_source line 12 · 2026-05-10T09:18:37.174Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VSc7yM2LgweeYDtt1BDsq1`</summary>

```json
{
  "query": "Qwen2.5-VL InfographicVQA 87.3% ANLS benchmark performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1086e308-c5f2-4189-a4c6-28b1ae685907",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzqMbHkJgsqHdrEemG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7fbab01-43aa-45f6-8dd6-e0a3a662a74e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CD33BEfTCJtbHM2mGrCmQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1843,
      "cache_creation_input_tokens": 2695,
      "cache_read_input_tokens": 16871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2695,
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

_source line 13 · 2026-05-10T09:18:37.374Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SxT11P1eyKwPjrMmCnjFfQ`</summary>

```json
{
  "query": "document layout structured reasoning typed nodes edges VQA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7fbab01-43aa-45f6-8dd6-e0a3a662a74e",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzqMbHkJgsqHdrEemG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "83baad59-69fd-4c90-a389-18603cb8fb46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CD33BEfTCJtbHM2mGrCmQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1843,
      "cache_creation_input_tokens": 2695,
      "cache_read_input_tokens": 16871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2695,
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

_source line 14 · 2026-05-10T09:18:38.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RNYtJ1ntsJLwkgtV3aQgzq`</summary>

```json
{
  "query": "verbalized traversal reasoning document elements infographic 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83baad59-69fd-4c90-a389-18603cb8fb46",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011CatdzqMbHkJgsqHdrEemG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f6a9ef33-d35c-4661-896c-771fb573d63c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CD33BEfTCJtbHM2mGrCmQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1843,
      "cache_creation_input_tokens": 2695,
      "cache_read_input_tokens": 16871,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2695
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1843,
          "output_tokens": 209,
          "cache_read_input_tokens": 16871,
          "cache_creation_input_tokens": 2695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2695,
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

_source line 15 · 2026-05-10T09:18:44.532Z_

<details><summary>↩ Tool result · `toolu_01VSc7yM2LgweeYDtt1BDsq1`</summary>

```text
Web search results for query: "Qwen2.5-VL InfographicVQA 87.3% ANLS benchmark performance"

Links: [{"title":"Qwen2.5 Speed Benchmark - Qwen - Read the Docs","url":"https://qwen.readthedocs.io/en/v2.5/benchmark/speed_benchmark.html"},{"title":"Qwen2.5-VL: Architecture, Data, Benchmarks and Inference","url":"https://debuggercafe.com/qwen2-5-vl/"},{"title":"Qwen/Qwen2.5-VL-72B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct"},{"title":"Qwen3.5: Features, Access, and Benchmarks | DataCamp","url":"https://www.datacamp.com/blog/qwen3-5"},{"title":"Qwen/Qwen2.5-VL-7B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct"},{"title":"Qwen/Qwen2.5-VL-3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct"},{"title":"qwen2.5vl","url":"https://ollama.com/library/qwen2.5vl"},{"title":"Qwen2.5 VL! Qwen2.5 VL! Qwen2.5 VL! | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-vl/"},{"title":"Qwen2.5-VL 7B","url":"https://qwen.ai/blog?id=qwen2.5-vl"},{"title":"Speed Benchmark - Qwen","url":"https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html"}]

The search results provide general information about Qwen2.5-VL but don't contain the specific benchmark result you're asking about (87.3% ANLS on InfographicVQA). Let me search more specifically for this benchmark detail.

Links: [{"title":"GitHub - QwenLM/Qwen3-VL: Qwen3-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen3-VL"},{"title":"Qwen/Qwen2.5-VL-7B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct"},{"title":"qwen2.5vl","url":"https://ollama.com/library/qwen2.5vl"},{"title":"Qwen/Qwen2.5-VL-3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct"},{"title":"Qwen/Qwen2.5-VL-72B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct"},{"title":"unsloth/Qwen2.5-VL-7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF"},{"title":"Qwen/Qwen2.5-VL-32B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct"},{"title":"Qwen2.5-VL - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen25-vl"},{"title":"Qwen2.5 VL! Qwen2.5 VL! Qwen2.5 VL! | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-vl/"},{"title":"Qwen2.5 VL 72B Instruct - API Pricing & Providers | OpenRouter","url":"https://openrouter.ai/qwen/qwen2.5-vl-72b-instruct"}]

I've completed the web search for your query about Qwen2.5-VL's 87.3% ANLS benchmark performance on InfographicVQA. While the search results provide extensive information about Qwen2.5-VL's general capabilities and architecture, the specific benchmark result you're asking about (87.3% ANLS on InfographicVQA) is not appearing in the current search results.

The results confirm that Qwen2.5-VL is evaluated on various benchmarks and achieves "significant advantages in understanding documents and diagrams," but the specific InfographicVQA ANLS score of 87.3% is not detailed in these particular sources.

To find this specific benchmark result, you may want to:
1. Check the official Qwen2.5-VL technical report (which was released in February 2025 according to the search results)
2. Visit the Qwen research papers or blog posts that may contain detailed benchmark tables
3. Look at the model's official documentation or research repositories on GitHub or ArXiv


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7fbab01-43aa-45f6-8dd6-e0a3a662a74e",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "918b3c1f-e493-4194-9de9-43b8f393f0c4",
  "sourceToolAssistantUUID": "c7fbab01-43aa-45f6-8dd6-e0a3a662a74e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T09:18:44.630Z_

<details><summary>↩ Tool result · `toolu_01SxT11P1eyKwPjrMmCnjFfQ`</summary>

```text
Web search results for query: "document layout structured reasoning typed nodes edges VQA 2025 2026"

Links: [{"title":"Document Visual Question Answering","url":"https://www.emergentmind.com/topics/document-visual-question-answering-vqa"},{"title":"Doc-𝑉^∗: Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA","url":"https://arxiv.org/html/2604.13731"},{"title":"MGA-VQA: Secure and Interpretable Graph-Augmented Visual Question Answering with Memory-Guided Protection Against Unauthorized Knowledge Use","url":"https://arxiv.org/html/2511.17881"},{"title":"MGA-VQA: Secure and Interpretable Graph-Augmented ...","url":"https://arxiv.org/pdf/2511.17881"},{"title":"PDF-VQA: A New Dataset for Real-World VQA on PDF Documents | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-43427-3_35"},{"title":"Document-AI-Recommendations/Approaches/approaches_vie.md at main · SCUT-DLVCLab/Document-AI-Recommendations","url":"https://github.com/SCUT-DLVCLab/Document-AI-Recommendations/blob/main/Approaches/approaches_vie.md"},{"title":"Hierarchical multimodal transformers for Multipage DocVQA - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320323005320"},{"title":"Revolutionizing Document Processing Through DocVQA","url":"https://www.analyticsvidhya.com/blog/2023/03/revolutionizing-document-processing-through-docvqa/"},{"title":"GitHub - adlnlp/pdfvqa","url":"https://github.com/adlnlp/pdfvqa"},{"title":"ARIAL: An Agentic Framework for Document VQA with Precise Answer Localization","url":"https://arxiv.org/html/2511.18192"}]

Based on the web search results, here's what I found regarding document layout, structured reasoning, typed nodes, edges, and VQA:

## Key Findings

**Graph-Based Reasoning in Document VQA:**

Graph-based GCNs in PDF-VQA introduce GCNs over document elements (nodes with visual+textual features, spatial/hierarchical edges) for structural and relational reasoning. Representing documents as heterogeneous graphs (nodes: elements; edges: spatial/hierarchical) and applying Relational GCNs yields improved multi-hop relational understanding and layout-sensitive predictions.

**Structured Document Representation:**

The PDF-VQA dataset annotates hierarchically logical relational graphs among document layout elements and includes bounding box coordinates, textual contents, and parent-child relationships (relational graph annotation).

**Recent Developments (2025-2026):**

MGA-VQA integrates token-level encoding, spatial graph reasoning, memory-augmented inference, and introduces interpretable graph-based decision pathways and structured memory access for enhanced reasoning transparency.

ARIAL decomposes Document VQA into structured subtasks: OCR-based text extraction, retrieval-augmented context selection, answer generation, and explicit bounding-box localization through text-to-region alignment.

**Document Understanding with Layout:**

GNN-based methods consider text segments as graph nodes and encode relations between segment coordinates for edge representations, using graph convolution operations for feature extraction.

These approaches represent the current trend toward explicit graph-based structured reasoning for document VQA, where typed nodes represent document elements and edges capture spatial and hierarchical relationships.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83baad59-69fd-4c90-a389-18603cb8fb46",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "82c16e26-7b41-42cd-8492-f785db1f5955",
  "sourceToolAssistantUUID": "83baad59-69fd-4c90-a389-18603cb8fb46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T09:18:45.453Z_

<details><summary>↩ Tool result · `toolu_01RNYtJ1ntsJLwkgtV3aQgzq`</summary>

```text
Web search results for query: "verbalized traversal reasoning document elements infographic 2025 2026"

Links: [{"title":"What is GraphRAG: Complete guide [2026]","url":"https://www.meilisearch.com/blog/graph-rag"},{"title":"A Survey on the Mechanisms of Multi-Step Reasoning in ...","url":"https://www.preprints.org/frontend/manuscript/11cab45ab0d578f7080de19423eb6ffe/download_pub"},{"title":"FiDeLiS: Faithful Reasoning in Large Language Models for ...","url":"https://aclanthology.org/2025.findings-acl.436.pdf"},{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Links for 2026-04-30 - by Alexander Kruel","url":"https://axisofordinary.substack.com/p/links-for-2026-04-30"},{"title":"Evaluating Step-by-step Reasoning Traces: A Survey","url":"https://aclanthology.org/2025.findings-emnlp.94.pdf"},{"title":"VERA: Explainable Video Anomaly Detection via Verbalized Learning of","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_VERA_Explainable_Video_Anomaly_Detection_via_Verbalized_Learning_of_Vision-Language_CVPR_2025_paper.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cf3d7d8e79703fe947deffb587a83639-Paper-Conference.pdf"},{"title":"Article Not peer-reviewed version Deep Research: A Systematic Survey","url":"https://www.preprints.org/frontend/manuscript/293d609eb9e3ff1d5e0b93522128610c/download_pub"}]

I've performed the web search for "verbalized traversal reasoning document elements infographic 2025 2026". The search results provide relevant information across several research areas:

**Key findings from the search results:**

1. **GraphRAG and Document Analysis (2025-2026)**: The process extends traditional RAG workflows with a graph layer for connected reasoning and contextual information that reflects real-world relationships. A search engine can quickly handle text or metadata retrieval before moving on to graph traversal.

2. **Verbalized Learning**: The VERA paper from CVPR 2025 discusses verbalized learning for video anomaly detection, where the framework renders frozen vision-language models to describe and reason with learnable guiding questions.

3. **Reasoning and Chain-of-Thought**: Reasoning LLMs are models tuned to excel at multi-step, logic-driven tasks and typically generate intermediate steps or thoughts in their outputs.

4. **Document Structure Analysis**: One result references graph-based document structure analysis published at ICLR 2025.

5. **Multi-Step Reasoning Mechanisms**: Research reveals that chain-of-thought reasoning is a combination of sequential step-by-step reasoning, parallel associative shortcuts, and occasional after-the-fact rationalizations.

The search results show active research in 2025-2026 on how systems traverse and reason over document elements using both verbalized and graph-based approaches, though no single comprehensive infographic was found covering all these elements together.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6a9ef33-d35c-4661-896c-771fb573d63c",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "cafc757a-3b50-4838-83bd-313eced822a9",
  "sourceToolAssistantUUID": "f6a9ef33-d35c-4661-896c-771fb573d63c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T09:18:46.873Z_

Let me search more specifically for recent InfographicVQA results and any papers proposing explicit layout graph approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cafc757a-3b50-4838-83bd-313eced822a9",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011Cate1af5fFUJweCGd7Ns9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a1ba20dd-9da1-4b54-92d4-c227a3a2b2e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TNALEtbV5NQbUxGtV4gKmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5395,
      "cache_read_input_tokens": 19566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5395,
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

_source line 19 · 2026-05-10T09:18:47.091Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D6FvgdB8dkBrPyLTNnzLh1`</summary>

```json
{
  "query": "\"InfographicVQA\" benchmark results SOTA 2025 2026 accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1ba20dd-9da1-4b54-92d4-c227a3a2b2e3",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011Cate1af5fFUJweCGd7Ns9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb628718-1c93-430d-99bd-7ad979ca06df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TNALEtbV5NQbUxGtV4gKmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5395,
      "cache_read_input_tokens": 19566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5395,
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

_source line 20 · 2026-05-10T09:18:47.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cpj1hK92RYsjgY2EfRd2rQ`</summary>

```json
{
  "query": "document structure graph layout caption figure table reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb628718-1c93-430d-99bd-7ad979ca06df",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011Cate1af5fFUJweCGd7Ns9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a9b7e25-8815-4be4-85f9-ff547145d0f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TNALEtbV5NQbUxGtV4gKmJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5395,
      "cache_read_input_tokens": 19566,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 146,
          "cache_read_input_tokens": 19566,
          "cache_creation_input_tokens": 5395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5395,
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

_source line 21 · 2026-05-10T09:18:54.025Z_

<details><summary>↩ Tool result · `toolu_01Cpj1hK92RYsjgY2EfRd2rQ`</summary>

```text
Web search results for query: "document structure graph layout caption figure table reasoning 2025 2026"

Links: [{"title":"GRAPH-BASED DOCUMENT STRUCTURE ANALYSIS","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cf3d7d8e79703fe947deffb587a83639-Paper-Conference.pdf"},{"title":"Tables and Figures | Engineering Writing Center | College of Engineering | USU","url":"https://engineering.usu.edu/students/ewc/writing-resources/tables-figures"},{"title":"3.4 Figures and Tables – Technical Writing Essentials","url":"https://pressbooks.bccampus.ca/technicalwriting/chapter/figurestables/"},{"title":"Document Layout Analysis with Graph-based Methods","url":"https://prometeia.com/en/about-us/insights/article/document-layout-analysis-with-graphbased-methods-15929781"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=Fu0aggezN9"},{"title":"DocSemi: Efficient Document Layout Analysis with Guided Queries","url":"https://openaccess.thecvf.com/content/ICCV2025W/VisionDocs/papers/Shehzadi_DocSemi_Efficient_Document_Layout_Analysis_with_Guided_Queries_ICCVW_2025_paper.pdf"},{"title":"Tables & Figures - The Graduate School - NC State University","url":"https://grad.ncsu.edu/students/etd/etd-guide/tables-figures/"},{"title":"Word for Research Writing II: Figures and Tables","url":"https://graduateschool.nd.edu/assets/283522/wfrw_ii_figures_and_tables.pdf"},{"title":"Figures, Tables and Graphs - Durham University","url":"https://www.durham.ac.uk/departments/academic/physics/labs/level-1/report-writing-guidance/figures-tables-and-graphs/"},{"title":"Images, Figures and Tables - IEEE Style - LibGuides at Chalmers University of Technology","url":"https://guides.lib.chalmers.se/ieee_style/images_figures_tables"}]

I found relevant results from your search. Here's a summary of what was discovered:

## Recent Research on Document Structure Analysis (2025-2026)

The most relevant findings relate to recent academic research on graph-based document structure analysis:

Graph-based Document Structure Analysis (gDSA) aims to extract the relational graph among layout elements within the document, with nodes corresponding to layout elements and edges representing relations between these layout elements. This approach was published as a conference paper at ICLR 2025.

Layout elements that can be analyzed include Caption, Footnote, Formula, List-item, Page-footer, Page-header, Picture, Section-header, Table, Text, and Title.

The research indicates that Graph Generation is used for various vision-language tasks, such as image captioning, visual question answering, content-based image retrieval, image generation, and referring expression comprehension.

## Standard Document Guidelines for Captions, Figures, and Tables

Beyond the research papers, the search also returned conventional guidelines for document formatting:

- Figure captions are generally placed below the figures, while table captions must be placed above the tables
- Captions should contain a number, title, and any other appropriate explanatory information, and convey information to the reader about the "story" being told with the figure or table

The recent research (2025) appears to focus on using artificial intelligence and graph-based reasoning to automatically analyze and understand the relationships between different elements in document layouts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a9b7e25-8815-4be4-85f9-ff547145d0f2",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "33719499-32e9-4b0b-9882-3246cc014506",
  "sourceToolAssistantUUID": "9a9b7e25-8815-4be4-85f9-ff547145d0f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T09:18:55.003Z_

<details><summary>↩ Tool result · `toolu_01D6FvgdB8dkBrPyLTNnzLh1`</summary>

```text
Web search results for query: ""InfographicVQA" benchmark results SOTA 2025 2026 accuracy"

Links: [{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"InfographicVQA Minesh Mathew1 Viraj Bagal2* Rub`en Tito3 Dimosthenis Karatzas3","url":"https://openaccess.thecvf.com/content/WACV2022/papers/Mathew_InfographicVQA_WACV_2022_paper.pdf"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"InfographicVQA | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9706887/"},{"title":"VBench: Comprehensive Benchmark Suite for Video Generative Models","url":"https://vchitect.github.io/VBench-project/"},{"title":"What Are the SOTA AI Models? | Machine Learning Glossary","url":"https://maddevs.io/glossary/state-of-the-art-models/"},{"title":"State-of-the-Art (SOTA) AI Models: LLMs, NLP, and Computer Vision","url":"https://automatio.ai/blog/sota-models-llm-nlp/"},{"title":"DocVQA","url":"https://www.docvqa.org/"}]

Let me search for more specific InfographicVQA benchmark results and SOTA performance metrics.

Links: [{"title":"InfographicVQA Minesh Mathew1 Viraj Bagal2* Rub`en Tito3 Dimosthenis Karatzas3","url":"https://openaccess.thecvf.com/content/WACV2022/papers/Mathew_InfographicVQA_WACV_2022_paper.pdf"},{"title":"[2104.12756] InfographicVQA - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2104.12756"},{"title":"SOTA AI Models: Benchmarks, Metrics & Deployment Guide","url":"https://huggingface.co/blog/daya-shankar/sota-ai-models"},{"title":"[2104.12756] InfographicVQA","url":"https://arxiv.org/abs/2104.12756"},{"title":"(PDF) InfographicVQA","url":"https://www.researchgate.net/publication/351105828_InfographicVQA"},{"title":"InfographicsQA Leaderboard","url":"https://llm-stats.com/benchmarks/infographicsqa"},{"title":"Exploring SOTA: A Guide to Cutting-Edge AI Models | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/exploring-sota-guide-to-cutting-edge-ai-models"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"How To Evaluate State‑Of‑The‑Art LLM Models: A Complete Guide | Deepchecks","url":"https://www.deepchecks.com/evaluate-state-of-the-art-llm-models/"},{"title":"ViInfographicVQA: A Benchmark for Single and Multi-image Visual Question Answering on Vietnamese Infographics","url":"https://arxiv.org/html/2512.12424v1"}]

Based on my web search, I found some relevant information about InfographicVQA benchmark results. Here's what I discovered:

## InfographicVQA Benchmark Overview

InfographicVQA is a dataset comprising a diverse collection of infographics with natural language questions and answers annotations, where collected questions require methods to jointly reason over the document layout, textual content, graphical elements, and data visualizations.

## Recent SOTA Results

The most recent SOTA information I found indicates:

The InfographicsQA leaderboard currently ranks AI models based on their performance on this benchmark, with Llama 3.2 90B Instruct by Meta leading with a score of 0.568.

For more detailed baseline performance, researchers evaluated strong baselines based on state-of-the-art Transformer-based, scene text VQA and document understanding models, with results showing poor performance of both approaches compared to near perfect human performance.

Additionally, recent experiments with open-source VLMs show mid-60% ANLS on Single-image questions, though this refers to a Vietnamese variant (ViInfographicVQA) published more recently.

The benchmark appears to be actively maintained at docvqa.org, and performance on InfographicVQA remains a challenging task for current vision-language models, particularly for questions requiring reasoning over layout, textual content, and numerical data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb628718-1c93-430d-99bd-7ad979ca06df",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "4b23617e-a6b3-4712-9d14-89f057969c22",
  "sourceToolAssistantUUID": "cb628718-1c93-430d-99bd-7ad979ca06df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T09:18:56.380Z_

Excellent. I found the ICLR 2025 paper on graph-based document structure analysis. Let me get one more search to check for any papers on explicit verbalized traversal or step-by-step document reasoning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b23617e-a6b3-4712-9d14-89f057969c22",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011Cate2HVjXtM4rZ82uQ77x",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d714a46-d859-472d-891e-3d9175f5c298",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UvBiv4RJcZwwtXSoDyBpd3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 916,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 24961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1650,
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

_source line 24 · 2026-05-10T09:18:56.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WnHy3UkQjw1Z2dLcEc8wSt`</summary>

```json
{
  "query": "chain-of-thought document graph step-by-step reasoning VLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d714a46-d859-472d-891e-3d9175f5c298",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011Cate2HVjXtM4rZ82uQ77x",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1329bc87-0c57-4f64-ade4-085d622b85b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UvBiv4RJcZwwtXSoDyBpd3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 916,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 24961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1650,
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

_source line 25 · 2026-05-10T09:18:56.994Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C3pwCNhGj3Jno6RPyZxrh8`</summary>

```json
{
  "query": "layout element traversal spatial relations document VQA reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1329bc87-0c57-4f64-ade4-085d622b85b6",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011Cate2HVjXtM4rZ82uQ77x",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ed9f44d-e9ef-4a01-a85c-cbe8d916a037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UvBiv4RJcZwwtXSoDyBpd3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 916,
      "cache_creation_input_tokens": 1650,
      "cache_read_input_tokens": 24961,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1650
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 916,
          "output_tokens": 171,
          "cache_read_input_tokens": 24961,
          "cache_creation_input_tokens": 1650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1650,
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

_source line 26 · 2026-05-10T09:19:03.205Z_

<details><summary>↩ Tool result · `toolu_01WnHy3UkQjw1Z2dLcEc8wSt`</summary>

```text
Web search results for query: "chain-of-thought document graph step-by-step reasoning VLM 2025 2026"

Links: [{"title":"Unveiling Chain of Step Reasoning for Vision-Language ...","url":"https://arxiv.org/pdf/2509.19003"},{"title":"Improve Vision Language Model Chain-of-thought Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.82/"},{"title":"Improve Vision Language Model Chain-of-thought ...","url":"https://aclanthology.org/2025.acl-long.82.pdf"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.pdf"},{"title":"Interleaved-Modal Chain-of-Thought - CVF Open Access","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Gao_Interleaved-Modal_Chain-of-Thought_CVPR_2025_paper.pdf"},{"title":"A Survey of Chain-of-X Paradigms for LLMs","url":"https://aclanthology.org/2025.coling-main.719.pdf"},{"title":"CoT-RAG: Integrating Chain of Thought and Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.168.pdf"},{"title":"MM-Verify: Enhancing Multimodal Reasoning with Chain-of ...","url":"https://aclanthology.org/2025.acl-long.689.pdf"},{"title":"LLaVA-CoT: Let Vision Language Models Reason Step-by-Step Guowei Xu♣*","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_LLaVA-CoT_Let_Vision_Language_Models_Reason_Step-by-Step_ICCV_2025_paper.pdf"},{"title":"Learn to Think: Bootstrapping LLM Logic Through Graph Representation Learning","url":"https://www.ijcai.org/proceedings/2025/0896.pdf"}]

Based on the search results, I found several relevant papers and research on chain-of-thought reasoning for vision language models (VLMs) in 2025-2026. Here's a summary of the key findings:

## Recent VLM Chain-of-Thought Research

### Step-by-Step Reasoning Enhancement
Recent research decomposes the entire reasoning chain into consecutive steps, with each step consisting of three components: Name, Thought, and Reflection, separated by special tags. The Name component provides a concise summary of the step, the Thought component contains detailed reasoning specific to that step, and the Reflection component establishes connections between the current reasoning step, the visual information, and previous steps.

### Training and Optimization Methods
Chain-of-thought (CoT) reasoning in vision language models (VLMs) is crucial for improving interpretability and trustworthiness. Short answers are used as correctness indicators to construct positive (correct) and negative (incorrect) pairs from model-generated reasoning chains. These pairs are then used to calibrate the model's reasoning via Direct Preference Optimization.

### Structured CoT Approaches
Systematic reasoning means the model does not generate a direct reasoning chain but instead engages in multistage reasoning. Structured refers to the model's ability to clearly identify the reasoning stage it is in and understand the primary task to be addressed at each stage.

### Graph-Based Reasoning
One novel method utilizes a graph-based framework to represent the reasoning process of LLMs and applies graph learning techniques to learn and analyze this reasoning graph, subsequently generating corresponding reasoning strategies.

These developments represent significant progress in making VLMs more interpretable and reliable through structured, step-by-step reasoning processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1329bc87-0c57-4f64-ade4-085d622b85b6",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "dfc282fb-d3d0-4b64-8c02-b1bd31f50171",
  "sourceToolAssistantUUID": "1329bc87-0c57-4f64-ade4-085d622b85b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T09:19:06.078Z_

<details><summary>↩ Tool result · `toolu_01C3pwCNhGj3Jno6RPyZxrh8`</summary>

```text
Web search results for query: "layout element traversal spatial relations document VQA reasoning 2025"

Links: [{"title":"Document Visual Question Answering","url":"https://www.emergentmind.com/topics/document-visual-question-answering-vqa"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cf3d7d8e79703fe947deffb587a83639-Paper-Conference.pdf"},{"title":"Enhancing Spatial Reasoning in Vision-Language Models ...","url":"https://aclanthology.org/2025.acl-long.387.pdf"},{"title":"GitHub - EmbodiedCity/Open3D-VQA.code: [ACM MM'25] Code for the paper \"Open3D-VQA: A Benchmark for Embodied Spatial Reasoning with Multimodal Large Language Model in Open Space\"","url":"https://github.com/EmbodiedCity/Open3D-VQA.code"},{"title":"Knowledge-Enhanced VQA Architectures","url":"https://www.emergentmind.com/topics/knowledge-enhanced-vqa-architectures"},{"title":"3D-Layout-R1: Structured Reasoning for Language-Instructed Spatial Editing","url":"https://arxiv.org/pdf/2603.22279"},{"title":"SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities","url":"https://spatial-vlm.github.io/"},{"title":"GitHub - XingruiWang/Spatial457: [CVPR'25] A vision question answering (VQA) benchmark for 6D spatial reasoning.","url":"https://github.com/XingruiWang/Spatial457"},{"title":"FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations","url":"https://arxiv.org/html/2507.07644v3"},{"title":"Embedding Spatial Relations in Visual Question Answering for Remote Sensing | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9956401/"}]

Based on the search results, here are the key findings related to layout element traversal, spatial relations, document VQA, and reasoning in 2025:

## Document VQA and Spatial Reasoning

Recent developments in document VQA focus on modeling hierarchical document structure, spatial relationships, and evidence aggregation through graph-based reasoning, where documents are represented as heterogeneous graphs with nodes representing elements and edges representing spatial/hierarchical relationships, with Relational GCNs applied for improved multi-hop relational understanding and layout-sensitive predictions.

## Graph-Based Document Structure Analysis (2025)

The GraphDoc dataset, a large-scale relation graph-based document structure analysis dataset comprising 80,000 document images and over 4 million relation annotations, includes annotations for both spatial relations (Up, Down, Left, Right) and logical relations (Parent, Child, Sequence, Reference) between document components. This rich relational information enables models to perform multiple tasks like reading order prediction, hierarchical structure analysis, and complex inter-element relationship inference.

## Document VQA Architectures

End-to-end document-aware Transformers ingest image patches/tokens, positional/layout encodings, OCR tokens, and question embeddings, with self- and cross-attention layers enabling joint reasoning over spatial, textual, and visual signals, such as LayoutLMv2, DocFormer, and M4C.

## Spatial Reasoning Advances

An automatic 3D spatial VQA data generation framework has been developed that scales up to 2 billion VQA examples on 10 million real-world images. The Spatial457 benchmark evaluates 6D spatial reasoning capabilities of large multimodal models, systematically introducing four key capabilities—multi-object understanding, 2D and 3D localization, and 3D orientation—across five difficulty levels and seven question types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ed9f44d-e9ef-4a01-a85c-cbe8d916a037",
  "isSidechain": true,
  "promptId": "058c9fca-6855-4ab1-b5b6-9847d990a79b",
  "agentId": "a6875d57d542245b6",
  "type": "user",
  "uuid": "31dba505-f605-4ae6-bf35-d76e06dbcb53",
  "sourceToolAssistantUUID": "0ed9f44d-e9ef-4a01-a85c-cbe8d916a037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T09:19:28.943Z_

Perfect. I now have comprehensive search results. Let me compile the findings for the user.

## Report: InfographicVQA SOTA and Competing Document Layout Reasoning Work

### 1. Current InfographicVQA SOTA Performance

Based on the web search results, I found limited specific confirmation of Qwen2.5-VL achieving exactly 87.3% ANLS on InfographicVQA. However, the searches revealed:

- **Current leaderboard leader**: Llama 3.2 90B Instruct by Meta is leading the InfographicsQA leaderboard with a score of 0.568 (as reported on the InfographicsQA Leaderboard).
- **Qwen2.5-VL performance**: The model is confirmed to excel at "understanding documents and diagrams" according to official documentation, but the specific 87.3% ANLS metric was not found in the search results.
- **No models above 90% found**: The search results do not indicate any models achieving above 90% ANLS on InfographicVQA as of early 2026.
- **Benchmark access**: The official leaderboard is maintained at docvqa.org, and the 2026 DocVQA Challenge (ICDAR2026) is actively evaluating models on multimodal reasoning tasks.

**Recommendation**: Check the official DocVQA leaderboard directly at https://www.docvqa.org/ for the most current SOTA numbers.

---

### 2. Competing Work on Typed Document Graph Traversal (Late 2025 – 2026)

I identified several directly competing approaches that propose explicit typed graph structures with node types and spatial/logical edges:

#### **A. Graph-Based Document Structure Analysis (ICLR 2025)**
- **Paper**: Graph-Based Document Structure Analysis (published at ICLR 2025)
- **Approach**: Extracts relational graphs among layout elements where:
  - **Nodes**: Represent layout elements (Caption, Footnote, Formula, List-item, Page-footer, Page-header, Picture, Section-header, Table, Text, Title)
  - **Edges**: Represent spatial and logical relations between elements
- **Relevance**: This is a direct competitor to LHEC's typed document graph approach with labeled element types and edge relations
- **Reference**: [Graph-Based Document Structure Analysis ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf3d7d8e79703fe947deffb587a83639-Paper-Conference.pdf)

#### **B. GraphDoc Dataset (2025)**
- **Scale**: 80,000 document images with over 4 million relation annotations
- **Node Types**: Document components (implicit typing through parent/child, sequence, reference relations)
- **Edge Types**: Both spatial relations (Up, Down, Left, Right) and logical relations (Parent, Child, Sequence, Reference)
- **Tasks**: Supports reading order prediction, hierarchical structure analysis, and inter-element relationship inference
- **Relevance**: Large-scale annotated dataset for typed graph-based document reasoning

#### **C. MGA-VQA (November 2025)**
- **Paper**: "MGA-VQA: Secure and Interpretable Graph-Augmented Visual Question Answering with Memory-Guided Protection Against Unauthorized Knowledge Use"
- **Approach**: Five-module pipeline including:
  - Spatial graph construction with weighted graph representations over detected text spans
  - Edges encoding geometric and semantic relationships
  - Memory-augmented inference with structured access pathways
- **Relevance**: Explicit graph-augmented reasoning with typed relationships for document VQA
- **Reference**: [MGA-VQA arXiv:2511.17881](https://arxiv.org/html/2511.17881v1)

#### **D. ARIAL: Agentic Framework for Document VQA (November 2025)**
- **Approach**: Decomposes Document VQA into structured subtasks:
  - OCR-based text extraction
  - Retrieval-augmented context selection
  - Answer generation
  - Explicit bounding-box localization through text-to-region alignment
- **Relevance**: Structured, multi-step reasoning with explicit layout grounding
- **Reference**: [ARIAL arXiv:2511.18192](https://arxiv.org/html/2511.18192)

---

### 3. Explicit Verbalized Traversal Traces for Document Reasoning (2025-2026)

I found extensive work on chain-of-thought reasoning for vision-language models that could compete with verbalized traversal approaches:

#### **A. Step-by-Step VLM Reasoning (ICCV 2025, ACL 2025, CVPR 2025)**
- **LLaVA-CoT** (ICCV 2025): "Let Vision Language Models Reason Step-by-Step"
  - Decomposes reasoning into consecutive steps with Name, Thought, and Reflection components
  - Each step includes detailed reasoning connected to visual information and previous steps
  
- **Improve Vision Language Model Chain-of-Thought Reasoning** (ACL 2025):
  - Uses Direct Preference Optimization to calibrate reasoning chains
  - Constructs positive (correct) and negative (incorrect) reasoning pairs
  - Trains for structured, multistage reasoning with clear stage identification

- **CoT-VLA** (CVPR 2025): "Visual Chain-of-Thought Reasoning for Vision-Language-Action Models"
  - Extends CoT reasoning to action planning with visual grounding

- **Interleaved-Modal Chain-of-Thought** (CVPR 2025):
  - Integrates multimodal chain-of-thought reasoning

#### **B. Graph-Based Reasoning Chains (2025)**
- **Learn to Think: Bootstrapping LLM Logic Through Graph Representation Learning** (IJCAI 2025):
  - Uses graph-based framework to represent and learn LLM reasoning processes
  - Applies graph learning techniques to generate reasoning strategies

#### **C. Document-Specific CoT (2025-2026)**
- **DocHop-QA**: Multi-hop reasoning benchmark with 11,379 QA instances across scientific documents
  - Evaluates reasoning over multiple pieces of evidence with spatial, temporal, and multi-hop understanding
  
- **Enhancing Spatial Reasoning in Vision-Language Models** (ACL 2025):
  - Advances spatial relationship reasoning in VLMs

---

### 4. Summary: Key Competing Approaches

| Approach | Type | Key Innovation | Status | Reference |
|----------|------|-----------------|--------|-----------|
| **Graph-Based Document Structure Analysis** | Typed Graph | Typed nodes (Caption, Figure, Table, etc.) + spatial/logical edges | ICLR 2025 | Proceeding |
| **GraphDoc** | Dataset + Graph | 4M relation annotations with spatial/logical typed edges | 2025 | Large-scale benchmark |
| **MGA-VQA** | Graph Augmentation | Spatial graphs with geometric/semantic typed relationships | Nov 2025 | arXiv |
| **ARIAL** | Structured Agentic | Multi-step decomposition with explicit bounding-box alignment | Nov 2025 | arXiv |
| **LLaVA-CoT** | Verbalized CoT | Step-by-step reasoning with Name/Thought/Reflection structure | ICCV 2025 | Conference |
| **ACL 2025 CoT** | Verbalized + Optimization | DPO-trained step-by-step reasoning chains | ACL 2025 | Conference |

---

### Conclusion

The InfographicVQA benchmark remains active with Llama 3.2 90B currently leading (0.568), but no confirmation of any model exceeding 90% ANLS yet. **Directly competing work using typed document graph traversal** has emerged at ICLR 2025 (Graph-Based Document Structure Analysis) and in industry implementations (MGA-VQA, GraphDoc). **Verbalized traversal traces** are being actively explored through multiple VLM chain-of-thought papers from ACL 2025, CVPR 2025, and ICCV 2025. The field has converged on graph-based structured reasoning and multi-step verbalization as core competitive approaches.

---

## Sources

- [InfographicVQA arXiv:2104.12756](https://arxiv.org/abs/2104.12756)
- [DocVQA Official Leaderboard](https://www.docvqa.org/)
- [Graph-Based Document Structure Analysis ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf3d7d8e79703fe947deffb587a83639-Paper-Conference.pdf)
- [MGA-VQA arXiv:2511.17881](https://arxiv.org/html/2511.17881v1)
- [ARIAL arXiv:2511.18192](https://arxiv.org/html/2511.18192)
- [DocHop-QA arXiv:2508.15851](https://arxiv.org/abs/2508.15851)
- [LLaVA-CoT ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_LLaVA-CoT_Let_Vision_Language_Models_Reason_Step-by-Step_ICCV2025_paper.pdf)
- [ACL 2025: Improve Vision Language Model Chain-of-thought Reasoning](https://aclanthology.org/2025.acl-long.82.pdf)
- [CoT-VLA CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR2025_paper.pdf)
- [Interleaved-Modal Chain-of-Thought CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Gao_Interleaved-Modal_Chain-of-Thought_CVPR2025_paper.pdf)
- [Learn to Think: Graph-Based Reasoning IJCAI 2025](https://www.ijcai.org/proceedings/2025/0896.pdf)
- [Enhancing Spatial Reasoning ACL 2025](https://aclanthology.org/2025.acl-long.387.pdf)
- [InfographicsQA Leaderboard](https://llm-stats.com/benchmarks/infographicsqa)
- [DocVQA 2026 Challenge](https://www.docvqa.org/challenges/2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31dba505-f605-4ae6-bf35-d76e06dbcb53",
  "isSidechain": true,
  "agentId": "a6875d57d542245b6",
  "requestId": "req_011Cate36s464P1zhE14UCd2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e7064193-19da-4e9e-9808-1ba95a7143bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "481dd96f-61d0-48f6-8457-9179ba144554",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R478UKWaNNF1tdySBFmaDb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3099,
      "cache_read_input_tokens": 26611,
      "output_tokens": 2633,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2633,
          "cache_read_input_tokens": 26611,
          "cache_creation_input_tokens": 3099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3099,
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
