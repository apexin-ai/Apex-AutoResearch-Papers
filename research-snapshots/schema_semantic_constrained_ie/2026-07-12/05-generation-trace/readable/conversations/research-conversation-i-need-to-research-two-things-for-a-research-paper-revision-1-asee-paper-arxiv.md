# Research conversation: I need to research two things for a research paper revision: 1. **ASEE paper** (arXiv:2505.08690, "Adaptive Schema-aware

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a18db8a46d5575d85.jsonl`
- **Structured JSON:** [`19c1ba869c12c741ab5e.json`](../../sessions/19/19c1ba869c12c741ab5e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-10T10:03:45.558Z_

I need to research two things for a research paper revision:

1. **ASEE paper** (arXiv:2505.08690, "Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation", EMNLP Findings 2025): I need to confirm whether it evaluates on the MD-SEE benchmark (consolidating 12 datasets including RAMS and WikiEvents) but does NOT report separate F1 scores under the LtGaE three-way cross-dataset protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki). Please fetch the abstract and methods/results section from arXiv.

2. **Recent EAE work**: Search for any papers from late 2025 to May 2026 on:
   - Grammar-constrained generation for event argument extraction training data
   - XGrammar used for IE training data generation
   - Zero-shot event argument extraction with structured generation constraints

Please use WebSearch and WebFetch to find this information. Return: (a) what ASEE benchmarks are reported, (b) any new competitor papers we might have missed.

Search queries to try:
- "grammar constrained generation event argument extraction training data 2025 2026"
- "XGrammar information extraction training data"
- "zero-shot event argument extraction structured generation 2026"
- arXiv 2505.08690 abstract

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "421bc23e-de96-4edb-b208-d07ec37149eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T10:03:46.866Z_

I'll help you research these two topics. Let me start by fetching the ASEE paper from arXiv and then search for recent work on grammar-constrained generation for event argument extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "421bc23e-de96-4edb-b208-d07ec37149eb",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathSd8TCk2cY93PQ9ZCK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "17b46844-7791-4edd-8204-e507d4c3e83f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJz5QqkgHcdAsYiKBzaJaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16901,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16901,
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

_source line 3 · 2026-05-10T10:03:47.719Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D27jY4wNT2zqmvqtchaT6h`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.08690",
  "prompt": "Extract the abstract and methods/results sections. Specifically note: (1) what benchmarks are evaluated, (2) whether MD-SEE benchmark is mentioned, (3) whether separate F1 scores are reported under LtGaE three-way cross-dataset protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17b46844-7791-4edd-8204-e507d4c3e83f",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathSd8TCk2cY93PQ9ZCK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a3e7e17a-be25-40fd-9ed6-0d98eadcf257",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJz5QqkgHcdAsYiKBzaJaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16901,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16901,
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

_source line 4 · 2026-05-10T10:03:47.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WViu2xSiwgrP1Zy2PSqmiZ`</summary>

```json
{
  "query": "grammar constrained generation event argument extraction training data 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3e7e17a-be25-40fd-9ed6-0d98eadcf257",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathSd8TCk2cY93PQ9ZCK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0c86c07-0f7b-4d25-b2c1-6ceae1678533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJz5QqkgHcdAsYiKBzaJaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16901,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16901,
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

_source line 5 · 2026-05-10T10:03:48.069Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VrrKF8TzszsnXhG95sx3ms`</summary>

```json
{
  "query": "XGrammar information extraction training data generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0c86c07-0f7b-4d25-b2c1-6ceae1678533",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathSd8TCk2cY93PQ9ZCK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d1ae4015-f3cc-4835-a285-5f84da70c4cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJz5QqkgHcdAsYiKBzaJaW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16901,
      "cache_read_input_tokens": 0,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16901
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16901,
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

_source line 6 · 2026-05-10T10:03:48.074Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RAVfUYKSX7dJvMvn16K2ba`</summary>

```json
{
  "query": "zero-shot event argument extraction structured generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1ae4015-f3cc-4835-a285-5f84da70c4cb",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathSd8TCk2cY93PQ9ZCK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4bef87e1-fa20-42c2-b7fd-4c68154937f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GJz5QqkgHcdAsYiKBzaJaW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16901,
      "cache_read_input_tokens": 0,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16901
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 334,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16901,
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

_source line 7 · 2026-05-10T10:03:51.713Z_

<details><summary>↩ Tool result · `toolu_01D27jY4wNT2zqmvqtchaT6h`</summary>

```text
# Analysis of arXiv:2505.08690

Based on the webpage content provided, I can only access the abstract and metadata. The full methods and results sections are not displayed on this page.

## What I can confirm:

**1. Benchmarks Evaluated:**
The abstract mentions: "Extensive evaluations on MD-SEE show that our proposed ASEE demonstrates strong adaptability across various scenarios."

However, specific benchmark names and F1 scores are not detailed in the visible content.

**2. MD-SEE Benchmark:**
Yes, it is mentioned. The authors "construct the Multi-Dimensional Schema-aware Event Extraction (MD-SEE) benchmark, which systematically consolidates 12 datasets across diverse domains, complexity levels, and language settings."

**3. LtGaE Three-way Cross-Dataset Protocol:**
The specific cross-dataset protocols (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki) with separate F1 scores are **not mentioned** in the abstract or metadata visible on this page.

## Limitation:

To obtain the detailed methods section and results with specific F1 scores under the three-way protocol you're asking about, you would need to access the full PDF or HTML version of the paper using the links provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3e7e17a-be25-40fd-9ed6-0d98eadcf257",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "7420ea84-7e2b-49cc-8a55-16450e1c8be7",
  "sourceToolAssistantUUID": "a3e7e17a-be25-40fd-9ed6-0d98eadcf257",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T10:03:54.718Z_

<details><summary>↩ Tool result · `toolu_01WViu2xSiwgrP1Zy2PSqmiZ`</summary>

```text
Web search results for query: "grammar constrained generation event argument extraction training data 2025 2026"

Links: [{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"A Guide to Structured Generation Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"[2305.13971] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/abs/2305.13971"},{"title":"Event co-occurrences for prompt-based generative event argument extraction | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-82883-w"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"}]

Based on the search results, I found several relevant sources about grammar-constrained generation and event argument extraction. Here's what the recent research shows:

## Grammar-Constrained Decoding for Structured Information Extraction

In structured information extraction, there are typically semantic and syntactic constraints on the output of information extraction systems, but these constraints typically cannot be guaranteed using standard fine-tuned encoder-decoder architectures. Grammar-constrained decoding (GCD) can be used to control the generation of language models, guaranteeing that the output follows a given structure.

## Recent Applications to Event Argument Extraction

Many recent studies aim to understand events and capture their correlations by extracting event triggers and arguments using large language models. Prompt-based approaches for Event Argument Extraction transform downstream tasks into a more consistent format with the training task of pre-trained language models.

A 2024-2025 study specifically investigated the impact of grammar-constrained decoding in a fine-tuning setting on structured information extraction, focusing on low-resource settings, an area that had not been investigated before.

## Recent Activity in the Field

Multiple grammar-constrained decoding papers were published in 2025-2026, including works on grammar-constrained natural language generation, deterministic pushdown automata for faster structured generation, and syntactic control of language models.

The search results show active research in combining grammar constraints with generative models for structured extraction tasks, with particular focus on improving reliability and handling complex output structures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0c86c07-0f7b-4d25-b2c1-6ceae1678533",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "a8511b32-59c2-4593-b675-92d8ef7a7152",
  "sourceToolAssistantUUID": "a0c86c07-0f7b-4d25-b2c1-6ceae1678533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T10:03:55.172Z_

<details><summary>↩ Tool result · `toolu_01RAVfUYKSX7dJvMvn16K2ba`</summary>

```text
Web search results for query: "zero-shot event argument extraction structured generation 2026"

Links: [{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/html/2603.02909v2"},{"title":"Zero-shot event argument extraction by disentangling trigger from argument and role | International Journal of Machine Learning and Cybernetics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13042-024-02446-3"},{"title":"[2603.02909] Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/abs/2603.02909"},{"title":"[2603.02909v2] Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/abs/2603.02909v2"},{"title":"Bi-directional feature learning-based approach for zero-shot event argument extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325001402"},{"title":"Figure 1 from Code4Struct: Code Generation for Few-Shot Structured Prediction from Natural Language | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Code4Struct:-Code-Generation-for-Few-Shot-from-Wang-Li/450b8dff662a5d41388d04d994e5117020777ce5/figure/0"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for","url":"https://arxiv.org/pdf/2511.13118"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction","url":"https://arxiv.org/html/2511.13118v1"},{"title":"GitHub - ZeroNLP/Distar: Zero-shot Event Argument Extraction by Disentangling Trigger from Argument and Role","url":"https://github.com/ZeroNLP/Distar"},{"title":"Zero-Shot Cross-Lingual Event Argument Extraction with Language-Oriented","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26482/26254"}]

Based on the search results, here are the key findings on zero-shot event argument extraction with structured generation:

## Recent Research (2026)

A multi-agent collaboration framework for zero-shot document-level event argument extraction (ZS-DEAE) has been introduced, which simulates the human collaborative cognitive process of "Propose–Evaluate–Revise." The generation agent synthesizes data for unseen events by leveraging knowledge from seen events, while the evaluation agent extracts arguments from the synthetic data and assesses their semantic consistency with the context. The evaluation results are converted into reward signals, with event structure constraints incorporated into the reward design to enable iterative optimization of both agents via reinforcement learning.

## Code-Generation Approaches

Agent-Event-Coder (AEC), a novel multi-agent framework treats event extraction like software engineering: as a structured, iterative code-generation process. AEC decomposes zero-shot event extraction into specialized subtasks—retrieval, planning, coding, and verification—each handled by a dedicated LLM agent. Event schemas are represented as executable class definitions, enabling deterministic validation and precise feedback via a verification agent. This programming-inspired approach allows for systematic disambiguation and schema enforcement through iterative refinement.

## Bi-Directional Feature Learning

BiTer, a bi-directional feature learning-based approach for zero-shot event argument extraction, gains bi-directional transferable knowledge and mitigates context generation bias.

These approaches represent the latest developments in applying structured generation and multi-agent collaboration to improve zero-shot event argument extraction performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bef87e1-fa20-42c2-b7fd-4c68154937f9",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "6aaba2d3-651f-4e61-b3dc-32f421af2a69",
  "sourceToolAssistantUUID": "4bef87e1-fa20-42c2-b7fd-4c68154937f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T10:03:55.603Z_

<details><summary>↩ Tool result · `toolu_01VrrKF8TzszsnXhG95sx3ms`</summary>

```text
Web search results for query: "XGrammar information extraction training data generation"

Links: [{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"XGrammar: Efficient, flexible and portable structured generation engine …","url":"https://jimmysong.io/ai/xgrammar/"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"XGrammar | Home","url":"https://xgrammar.mlc.ai/"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/html/2505.04016v1"},{"title":"Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://arxiv.org/html/2501.10868v1"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"},{"title":"xgrammar/README.md at main · mlc-ai/xgrammar","url":"https://github.com/mlc-ai/xgrammar/blob/main/README.md"},{"title":"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models - Paper Detail","url":"https://deeplearn.org/arxiv/551290/xgrammar:-flexible-and-efficient-structured-generation-engine-for-large-language-models"}]

Based on the search results, here's what I found about XGrammar:

## Overview

XGrammar is an open-source library for efficient, flexible, and portable structured generation. XGrammar is an open-source engine for structured generation that leverages constrained decoding to guarantee syntactic correctness for outputs such as JSON, regex-constrained text, and custom CFGs.

## How It Works

XGrammar accelerates context-free grammar execution by dividing the vocabulary into context-independent tokens that can be prechecked and context-dependent tokens that need to be interpreted during runtime.

## Performance

XGrammar uses careful optimizations to achieve extremely low overhead in structured generation. It has achieved near-zero overhead in JSON generation, making it one of the fastest structured generation engines available.

## Information Extraction Applications

While the search results don't directly address "training data generation" for information extraction, there are references to XGrammar being used in information extraction contexts. XGrammar sometimes over-constrains the model's generative capabilities when the schema is highly structured, particularly affecting the nuanced language expression in fields with longer texts like descriptions. Additionally, task-specific fine-tuning has shown success in structured output generation, particularly for tasks like named-entity recognition and information extraction.

## Industry Adoption

XGrammar is the default structured generation backend for most LLM inference engines, including vLLM, SGLang, TensorRT-LLM, and MLC-LLM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1ae4015-f3cc-4835-a285-5f84da70c4cb",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "e0af45c1-170b-4de3-af37-8525f22d827b",
  "sourceToolAssistantUUID": "d1ae4015-f3cc-4835-a285-5f84da70c4cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T10:03:57.051Z_

Now let me fetch the full ASEE paper PDF to get more detailed information about the benchmarks and cross-dataset protocols:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0af45c1-170b-4de3-af37-8525f22d827b",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathTMinKY2hgYVcVQ2LX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "41ca564a-fbcf-4ceb-a3a6-be5c9a4c266a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CgtHhB3FpW3bgiRxz1Fhgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 973,
      "cache_creation_input_tokens": 3250,
      "cache_read_input_tokens": 16901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3250,
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

_source line 12 · 2026-05-10T10:03:57.960Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XxErqQpNibTYULwSZYnVfV`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.08690",
  "prompt": "Provide the detailed results section. What are all the benchmarks evaluated? Are separate F1 scores reported for the LtGaE three-way cross-dataset protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41ca564a-fbcf-4ceb-a3a6-be5c9a4c266a",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathTMinKY2hgYVcVQ2LX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b49d065-dceb-4d30-b78b-171a7e594c93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CgtHhB3FpW3bgiRxz1Fhgi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 973,
      "cache_creation_input_tokens": 3250,
      "cache_read_input_tokens": 16901,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3250
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 973,
          "output_tokens": 161,
          "cache_read_input_tokens": 16901,
          "cache_creation_input_tokens": 3250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3250,
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

_source line 13 · 2026-05-10T10:04:02.560Z_

<details><summary>↩ Tool result · `toolu_01XxErqQpNibTYULwSZYnVfV`</summary>

```text
I appreciate your request, but I'm unable to provide the detailed results section you're asking for. The document you've shared appears to be a PDF file encoded in a binary format that hasn't been properly converted to readable text.

What I can tell you is that this document is titled **"Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation"** by Sheng Liang, Hang Lv, Zhihao Wen, and others (arXiv:2505.08690). 

To obtain the specific information about:
- All benchmarks evaluated
- F1 scores for the LtGaE three-way cross-dataset protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki)

I recommend:
1. Accessing the paper directly from arXiv.org using the identifier 2505.08690
2. Navigating to the Results or Experimental Evaluation section
3. Locating the performance tables for the cross-dataset evaluation

This approach will give you the accurate, detailed results you're seeking.

[Binary content (application/pdf, 1.9MB) also saved to /home/ubuntu/.claude-account-1/projects/-/463e5fa5-38e0-4ede-baf8-cbc603cf470f/tool-results/webfetch-1778407437987-j9udi5.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b49d065-dceb-4d30-b78b-171a7e594c93",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "df24f146-66e9-4d2a-a7d5-0becd68dba6a",
  "sourceToolAssistantUUID": "0b49d065-dceb-4d30-b78b-171a7e594c93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T10:04:04.278Z_

Let me search more specifically for the ASEE paper's evaluation details and recent event extraction papers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df24f146-66e9-4d2a-a7d5-0becd68dba6a",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathTsrGKpMDKe37Mgoiy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85e04fd0-7d30-493f-a9d2-e1dc237e628f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X1Cz7rTCoq6ztVVZA5fPbd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 20151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
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

_source line 15 · 2026-05-10T10:04:04.713Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CSKQNo6fmtyGha8BnqqyrY`</summary>

```json
{
  "query": "ASEE Adaptive Schema-aware Event Extraction 2505.08690 MD-SEE cross-dataset RAMS2RAMS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85e04fd0-7d30-493f-a9d2-e1dc237e628f",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathTsrGKpMDKe37Mgoiy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "979eebe1-bd12-460b-8390-70670a4dbc74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X1Cz7rTCoq6ztVVZA5fPbd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 20151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
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

_source line 16 · 2026-05-10T10:04:04.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016HnU4TzUCwhyxhb6ekPQ75`</summary>

```json
{
  "query": "\"event argument extraction\" \"training data generation\" 2025 2026 neural"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "979eebe1-bd12-460b-8390-70670a4dbc74",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathTsrGKpMDKe37Mgoiy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d07f79b5-8599-4c30-8e81-ae4441eb2853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X1Cz7rTCoq6ztVVZA5fPbd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 20151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1456,
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

_source line 17 · 2026-05-10T10:04:05.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011QoecrsBuWEjEvEf87Fthc`</summary>

```json
{
  "query": "event extraction EMNLP 2025 findings benchmark evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d07f79b5-8599-4c30-8e81-ae4441eb2853",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathTsrGKpMDKe37Mgoiy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b1aed7eb-18a2-4db3-bd98-3ca7a20c43cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X1Cz7rTCoq6ztVVZA5fPbd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1456,
      "cache_read_input_tokens": 20151,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1456
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 202,
          "cache_read_input_tokens": 20151,
          "cache_creation_input_tokens": 1456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1456,
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

_source line 18 · 2026-05-10T10:04:10.360Z_

<details><summary>↩ Tool result · `toolu_01CSKQNo6fmtyGha8BnqqyrY`</summary>

```text
Web search results for query: "ASEE Adaptive Schema-aware Event Extraction 2505.08690 MD-SEE cross-dataset RAMS2RAMS"

Links: [{"title":"[2505.08690] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.08690"},{"title":"[2505.08690v1] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.08690v1"},{"title":"Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.08690"},{"title":"[Literature Review] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://www.themoonlight.io/en/review/adaptive-schema-aware-event-extraction-with-retrieval-augmented-generation"},{"title":"Adaptive Schema-aware Event Extraction with Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.419.pdf"},{"title":"Yaxiong Wu","url":"https://www.catalyzex.com/author/Yaxiong%20Wu"},{"title":"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/html/2505.14992v1"},{"title":"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240601045S/abstract"},{"title":"Effective and Efficient Schema-aware Information Extraction Using","url":"https://openreview.net/pdf?id=lW7nJDWWz4"},{"title":"Effective and Efficient Schema-aware Information ...","url":"https://www.arxiv.org/pdf/2505.14992"}]

Based on my search results, here's what I found about the paper you're asking about:

## ASEE - Adaptive Schema-aware Event Extraction

ASEE is a novel paradigm combining schema paraphrasing with schema retrieval-augmented generation. It addresses the need to select appropriate schemas from hundreds of candidates during extraction, as well as existing gaps including the rigid schema fixation in existing pipeline systems and the absence of benchmarks for evaluating joint schema matching and extraction.

## MD-SEE Benchmark

The Multi-Dimensional Schema-aware Event Extraction (MD-SEE) benchmark systematically consolidates 12 datasets across diverse domains, complexity levels, and language settings. Extensive evaluations on MD-SEE show that ASEE demonstrates strong adaptability across various scenarios, significantly improving the accuracy of event extraction.

## Paper Details

The paper (arxiv 2505.08690) was published on May 13, 2025, and authored by Sheng Liang and colleagues from Huawei Noah's Ark Lab and the University of Science and Technology of China.

Regarding the "RAMS2RAMS" cross-dataset evaluation you mentioned—the search results don't contain specific information about this particular cross-dataset evaluation. You may find more details in the full paper PDF on arxiv.org.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "979eebe1-bd12-460b-8390-70670a4dbc74",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "e3933562-de9b-47d5-baf5-192ff83b0cff",
  "sourceToolAssistantUUID": "979eebe1-bd12-460b-8390-70670a4dbc74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T10:04:10.924Z_

<details><summary>↩ Tool result · `toolu_011QoecrsBuWEjEvEf87Fthc`</summary>

```text
Web search results for query: "event extraction EMNLP 2025 findings benchmark evaluation"

Links: [{"title":"A Comprehensive Benchmark for Evaluating Event ...","url":"https://aclanthology.org/2025.findings-emnlp.482.pdf"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"dblp: Xinya Du","url":"https://dblp.org/pid/200/8114.html"},{"title":"EMNLP (Findings) 2024: Miami, FL, USA","url":"https://dblp.org/db/conf/emnlp/emnlp2024f.html"},{"title":"dblp: EMNLP (Findings) 2025","url":"https://dblp.org/db/conf/emnlp/emnlp2025f.html"},{"title":"dblp: EMNLP 2025 - Industry Track","url":"https://dblp.org/db/conf/emnlp/emnlp2025i.html"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"GitHub - ej0cl6/TextEE: A standardized, fair, and reproducible benchmark for evaluating event extraction approaches · GitHub","url":"https://github.com/ej0cl6/TextEE"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"}]

Based on the search results, I found relevant information about event extraction work at EMNLP 2025:

## Event Extraction Research at EMNLP 2025

The search results reveal several event extraction-related papers and benchmarks presented at EMNLP 2025:

1. **EventRelBench**: A comprehensive benchmark for evaluating event extraction, published in the Findings of EMNLP 2025.

2. **SciEvent**: A benchmark for multi-domain scientific event extraction presented at EMNLP 2025.

3. **Multimedia Event Extraction with LLM Knowledge Editing**: This work on multimedia event extraction with LLM knowledge editing was accepted as a main conference paper at EMNLP 2025.

4. **Event Detection for Real-World Applications**: An industry track paper presenting "A Reasoner for Real-World Event Detection: Scaling Reinforcement Learning via Adaptive Perplexity-Aware Sampling Strategy".

Additionally, the search results indicate that EMNLP 2025 accepted more than 2,000 papers, with numerous contributions spanning different aspects of event extraction including event relation extraction and document-level event extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1aed7eb-18a2-4db3-bd98-3ca7a20c43cc",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "db9c7a2d-93e6-4566-991b-01b0b7005145",
  "sourceToolAssistantUUID": "b1aed7eb-18a2-4db3-bd98-3ca7a20c43cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T10:04:12.898Z_

<details><summary>↩ Tool result · `toolu_016HnU4TzUCwhyxhb6ekPQ75`</summary>

```text
Web search results for query: ""event argument extraction" "training data generation" 2025 2026 neural"

Links: [{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/html/2603.02909v2"},{"title":"Event co-occurrences for prompt-based generative event argument extraction | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-82883-w"},{"title":"GitHub - ll0ruc/event-extraction-paper: Papers from top conferences and journals for event extraction in recent years · GitHub","url":"https://github.com/ll0ruc/event-extraction-paper"},{"title":"Data augmentation of event causality identification task with pre-trained language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-49244-1"},{"title":"Joint event extraction model based on dynamic attention matching and graph attention networks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-91501-2"},{"title":"Event Argument Extraction with Enriched Prompts","url":"https://arxiv.org/html/2501.06825"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"A Survey on Deep Learning Event Extraction","url":"https://arxiv.org/pdf/2107.02126"},{"title":"Frontiers | Enhancing pre-trained language model by answering natural questions for event extraction","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1520290/full"}]

Based on the search results, here are the key findings related to event argument extraction and training data generation in neural approaches from 2025-2026:

## Recent Developments in Event Argument Extraction

Event extraction research spans from 1991 through 2025, with key milestones in the Pre-PLM, PLM, and LLM eras. Event extraction aims to identify event triggers, event types, and participant roles from unstructured text, and organize them into a computable structured representation.

## Training Data Generation Approaches

Synthetic data generation has become a promising strategy for low-resource information extraction. Recent work demonstrates innovative approaches to generating training data: LLMs create seed instances for fine-tuning smaller models and expand pattern diversity with iterative feedback. Additionally, researchers introduce dual-agent frameworks to iteratively refine synthetic samples, while integrating in-context learning with direct preference optimization to increase data diversity.

## Multi-Agent and Zero-Shot Approaches

Multi-agent collaboration has recently emerged as an influential paradigm in information extraction, with cooperative multi-agent systems for zero-shot NER that separate entity recognition from type feature extraction. Document-level Event Argument Extraction aims to extract textual spans that serve as arguments for specific roles within a given event type, based on the entire input document.

## Neural Architecture Innovations

Recent deep learning progressions include Convolutional and Recurrent Neural Networks, the revolutionary impact of Transformer-based pre-trained language models, and explicit modeling of syntax with Graph Neural Networks. Joint event extraction models leverage dynamic attention matching and graph attention networks to identify event nodes and resolve the problem of ambiguous and unknown trigger word classification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d07f79b5-8599-4c30-8e81-ae4441eb2853",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "88229488-8697-4901-a215-3bdebee3d80c",
  "sourceToolAssistantUUID": "d07f79b5-8599-4c30-8e81-ae4441eb2853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T10:04:14.410Z_

Let me fetch the ASEE paper directly from ACL Anthology to get the detailed results section:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88229488-8697-4901-a215-3bdebee3d80c",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathUdeX15s7AFHr9PEhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d1bcf48-53e8-4570-b040-22d3ff084bfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DmYorquAcSZb8oAdSWejhX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 813,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 21607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2001,
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

_source line 22 · 2026-05-10T10:04:15.664Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018McX9p9i7EamB2obji2Tb6`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-emnlp.419.pdf",
  "prompt": "Extract the results section. List all benchmarks evaluated and report on cross-dataset protocol results, specifically whether RAMS2RAMS, RAMS2Wiki, Wiki2Wiki F1 scores are reported separately."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d1bcf48-53e8-4570-b040-22d3ff084bfc",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathUdeX15s7AFHr9PEhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "64ccbeb8-fdbd-41f5-977b-30475d5dffe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DmYorquAcSZb8oAdSWejhX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 813,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 21607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2001,
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

_source line 23 · 2026-05-10T10:04:15.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K7ZnvVGSR8ypqJU5bTy7s7`</summary>

```json
{
  "query": "\"Agent-Event-Coder\" OR \"AEC\" zero-shot event extraction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64ccbeb8-fdbd-41f5-977b-30475d5dffe8",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathUdeX15s7AFHr9PEhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37f03890-e14d-4fdc-a884-e4819b34dd71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DmYorquAcSZb8oAdSWejhX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 813,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 21607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2001,
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

_source line 24 · 2026-05-10T10:04:16.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XN6drFWr729SXhLuyUDUv6`</summary>

```json
{
  "query": "LLM event argument extraction generation framework 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37f03890-e14d-4fdc-a884-e4819b34dd71",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathUdeX15s7AFHr9PEhg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b87c397f-5a91-4c64-82c8-5a02f3f42f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DmYorquAcSZb8oAdSWejhX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 813,
      "cache_creation_input_tokens": 2001,
      "cache_read_input_tokens": 21607,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2001
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 813,
          "output_tokens": 258,
          "cache_read_input_tokens": 21607,
          "cache_creation_input_tokens": 2001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2001,
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

_source line 25 · 2026-05-10T10:04:21.123Z_

<details><summary>↩ Tool result · `toolu_018McX9p9i7EamB2obji2Tb6`</summary>

```text
I apologize, but the content provided appears to be a corrupted or improperly encoded PDF file. The text is largely unreadable binary data and compressed streams, making it impossible to accurately extract a results section or identify specific benchmark scores.

To properly assist you, I would need:

1. A clean, text-based version of the paper, or
2. A properly decoded PDF that renders readable content

If you have access to the original paper, please provide it in a readable format (plain text, properly extracted PDF text, or HTML). Once available, I can identify the results section and report on whether cross-dataset protocol metrics (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki F1 scores) are presented separately.

[Binary content (application/pdf, 2.3MB) also saved to /home/ubuntu/.claude-account-1/projects/-/463e5fa5-38e0-4ede-baf8-cbc603cf470f/tool-results/webfetch-1778407457717-8xsuw5.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64ccbeb8-fdbd-41f5-977b-30475d5dffe8",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "a00389fb-bde6-42ba-aed0-eab20c63ee4b",
  "sourceToolAssistantUUID": "64ccbeb8-fdbd-41f5-977b-30475d5dffe8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T10:04:23.844Z_

<details><summary>↩ Tool result · `toolu_01XN6drFWr729SXhLuyUDUv6`</summary>

```text
Web search results for query: "LLM event argument extraction generation framework 2025 2026"

Links: [{"title":"Boundary-Aware LLM Augmentation for Low-Resource Event Argument Extraction - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.230/"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/html/2603.02909"},{"title":"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1743/"},{"title":"Argument Extraction from Communication Failures via Event Focusing and","url":"https://www.sciengine.com/doi/pdfView/38A45CA1AA6D48DB936B5BD3407995ED"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40346/44307"},{"title":"Closed-Domain Event Extraction Literature Review January 2025 v1.0","url":"https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf"},{"title":"Agent-DA: Enhancing low-resource event extraction with collaborative multi-agent data augmentation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705124012590"},{"title":"Under review as a conference paper at ICLR 2026","url":"https://www.arxiv.org/pdf/2510.03595"},{"title":"[2503.02628] Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction","url":"https://arxiv.org/abs/2503.02628"}]

Based on the web search results, here's what I found about LLM event argument extraction generation frameworks in 2025-2026:

## Recent Research Frameworks

**Boundary-Aware LLM Augmentation (2026)**

Researchers have investigated four LLM-based augmentation strategies for event argument extraction: argument replacement, adjunction rewriting, their combination, and annotation generation. Studies employ GPT-4o-Mini and DeepSeek-R1-7B as data generators, showing that boundary-aware augmentation consistently leads to greater performance improvements over boundary-agnostic methods.

**Multi-Agent Collaboration Frameworks**

Multi-agent collaboration has recently emerged as an influential paradigm in information extraction, spanning cooperative, competitive, and debate-based modes. One approach shows substantial F1 improvements of 7.53, 3.86, and 6.14 across datasets, benefiting from collaborative interaction between generation and evaluation agents.

**LLM-based Partitioning Extraction (LLM-PEE)**

To alleviate excessively long prompts caused by massive event types, researchers propose an LLM-based Partitioning method that first recalls candidate event types and then splits them into multiple partitions for LLMs to extract.

**Decoupled Generation Framework (DECO-G)**

A decoupled generation framework separates output format constraints from LLM task solving to unlock the full potential of LLMs.

## Current Challenges

LLM-based pipelines face deployment gaps, including hallucinations under weak constraints, fragile temporal and causal linking over long contexts and across documents, and limited long horizon knowledge management within a bounded context window.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b87c397f-5a91-4c64-82c8-5a02f3f42f04",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "123cdb94-dd35-4ee2-8800-d72b9a244178",
  "sourceToolAssistantUUID": "b87c397f-5a91-4c64-82c8-5a02f3f42f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T10:04:26.524Z_

<details><summary>↩ Tool result · `toolu_01K7ZnvVGSR8ypqJU5bTy7s7`</summary>

```text
Web search results for query: ""Agent-Event-Coder" OR "AEC" zero-shot event extraction 2025"

Links: [{"title":"[2511.13118] Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction","url":"https://arxiv.org/abs/2511.13118"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction","url":"https://arxiv.org/html/2511.13118v1"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction | Request PDF","url":"https://www.researchgate.net/publication/397701692_Extracting_Events_Like_Code_A_Multi-Agent_Programming_Framework_for_Zero-Shot_Event_Extraction"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction","url":"https://chatpaper.com/paper/210373"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for","url":"https://arxiv.org/pdf/2511.13118"},{"title":"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2511.13118"},{"title":"GitHub - UESTC-GQJ/AEC: This is the source code of AAAI 2026 paper \"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction\". · GitHub","url":"https://github.com/UESTC-GQJ/AEC"},{"title":"Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://www.researchgate.net/publication/394270737_Instruction-Tuning_LLMs_for_Event_Extraction_with_Annotation_Guidelines"},{"title":"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/391467195_A_Cooperative_Multi-Agent_Framework_for_Zero-Shot_Named_Entity_Recognition"},{"title":"Learning to Generate and Extract: A Multi-Agent Collaboration Framework For Zero-shot Document-level Event Arguments Extraction","url":"https://arxiv.org/html/2603.02909"}]

Based on the search results, I found comprehensive information about Agent-Event-Coder (AEC) and zero-shot event extraction from 2025:

## Overview

Agent-Event-Coder (AEC) is a novel multi-agent framework that treats event extraction like software engineering: as a structured, iterative code-generation process. This is the source code of an AAAI 2026 paper titled "Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction".

## The Problem Being Addressed

Zero-shot event extraction (ZSEE) remains a significant challenge for large language models (LLMs) due to the need for complex reasoning and domain-specific understanding. Direct prompting often yields incomplete or structurally invalid outputs—such as misclassified triggers, missing arguments, and schema violations.

## How AEC Works

AEC decomposes ZSEE into specialized subtasks—retrieval, planning, coding, and verification—each handled by a dedicated LLM agent. Event schemas are represented as executable class definitions, enabling deterministic validation and precise feedback via a verification agent.

## Performance Results

Experiments across five diverse domains and six LLMs demonstrate that AEC consistently outperforms prior zero-shot baselines, showcasing the power of treating event extraction like code generation. AEC was evaluated on five widely used event extraction benchmarks covering diverse domains: FewEvent (General), ACE 2005 (News), GENIA (Biomedical), SPEED (Epidemiological), and CASIE (Cybersecurity).

## Availability

The code and data are released on https://github.com/UESTC-GQJ/Agent-Event-Coder.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37f03890-e14d-4fdc-a884-e4819b34dd71",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "be5c0125-80e5-4406-8764-7a49466bce9d",
  "sourceToolAssistantUUID": "37f03890-e14d-4fdc-a884-e4819b34dd71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T10:04:27.681Z_

Now let me search for more specific information about the ASEE benchmarks by checking the HTML version:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be5c0125-80e5-4406-8764-7a49466bce9d",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathVdtgFoHrszvhB9vND",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0e1a70af-86d7-4ff9-823a-c1fe022d496a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016MabTMJbyjB1qvKEYaWBPd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 970,
      "cache_creation_input_tokens": 2341,
      "cache_read_input_tokens": 23608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2341,
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

_source line 29 · 2026-05-10T10:04:28.802Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XtmvzLeH92cNb4AW42VLhn`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.08690",
  "prompt": "What benchmarks are evaluated in the experiments? List all datasets tested. Are cross-dataset protocol results (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki) reported with separate F1 scores?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e1a70af-86d7-4ff9-823a-c1fe022d496a",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathVdtgFoHrszvhB9vND",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "493cb387-9e62-4e5c-87a6-98ceac38a655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016MabTMJbyjB1qvKEYaWBPd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 970,
      "cache_creation_input_tokens": 2341,
      "cache_read_input_tokens": 23608,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2341
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 970,
          "output_tokens": 148,
          "cache_read_input_tokens": 23608,
          "cache_creation_input_tokens": 2341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2341,
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

_source line 30 · 2026-05-10T10:04:33.783Z_

<details><summary>↩ Tool result · `toolu_01XtmvzLeH92cNb4AW42VLhn`</summary>

```text
# Benchmarks and Datasets Evaluated

## Datasets Tested

The experiments evaluate performance across multiple datasets:

1. **Individual Datasets**: CrudeOilNews, DocEE (English and Chinese versions), GENEVA, IEPILE (English and Chinese versions), and MAVEN-Arg

2. **MD-SEE Benchmark**: A newly constructed consolidated dataset combining 12 source datasets with "300 schemas covering multiple dimensions, 12,817 training samples, 1,775 development samples, and 7,686 test samples"

## Cross-Dataset Protocol Results

**No, cross-dataset protocol results are not reported.** The paper does not mention separate F1 scores for cross-dataset protocols like RAMS→RAMS, RAMS→Wiki, or Wiki→Wiki evaluations. 

The experimental sections (5.3-5.5) focus on:
- Schema retrieval evaluation using Recall@K metrics
- Schema-aware extraction evaluation using F1 scores on individual datasets
- End-to-End (E2E) evaluation on MD-SEE and individual datasets

The evaluation methodology emphasizes "rigorous joint assessment of schema selection and extraction accuracy" but does not implement the specific zero-shot generalization protocols you referenced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "493cb387-9e62-4e5c-87a6-98ceac38a655",
  "isSidechain": true,
  "promptId": "a65aa7d5-d6bd-4dcc-b69f-c468c2ef86be",
  "agentId": "a18db8a46d5575d85",
  "type": "user",
  "uuid": "2bce74ec-2dbe-4a5e-8fb4-27c6d545d7f1",
  "sourceToolAssistantUUID": "493cb387-9e62-4e5c-87a6-98ceac38a655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T10:04:47.087Z_

Perfect! Now I have comprehensive information. Let me compile my findings:

## Summary of Findings

### 1. ASEE Paper (arXiv:2505.08690) - EMNLP Findings 2025

**Benchmarks Evaluated:**
- Individual datasets: CrudeOilNews, DocEE (English and Chinese), GENEVA, IEPILE (English and Chinese), MAVEN-Arg
- **MD-SEE Benchmark**: Newly constructed consolidation of 12 datasets with 300 schemas, 12,817 training samples, 1,775 dev samples, 7,686 test samples

**Key Finding - Cross-Dataset Protocol Results:**
**The ASEE paper does NOT report separate F1 scores under the LtGaE three-way cross-dataset protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki).** The evaluation focuses on:
- Schema retrieval evaluation (Recall@K metrics)
- Schema-aware extraction (F1 scores on individual datasets)
- End-to-End evaluation on MD-SEE and individual datasets

The paper confirms it evaluates on MD-SEE but does not implement the specific zero-shot generalization protocols you mentioned.

### 2. Recent EAE Work (Late 2025 to May 2026)

I identified several important competitor papers you may have missed:

**Grammar-Constrained and Structured Generation Approaches:**

1. **Agent-Event-Coder (AEC)** - AAAI 2026 Paper
   - Treats event extraction as code generation with multiple LLM agents
   - Represents event schemas as executable class definitions
   - Enables deterministic validation and precise feedback
   - Evaluated on 5 domains (FewEvent, ACE 2005, GENIA, SPEED, CASIE) and 6 different LLMs
   - Source: https://arxiv.org/abs/2511.13118

2. **Grammar-Constrained Decoding for Structured Information Extraction** 
   - Applies GCD in fine-tuning settings for low-resource scenarios (2024-2025)
   - Uses grammar constraints to guarantee output structure
   - Published in Frontiers AI: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full

3. **XGrammar** (November 2024 - active infrastructure)
   - Flexible structured generation engine for LLMs
   - Used as default structured generation backend in vLLM, SGLang, TensorRT-LLM, MLC-LLM
   - Particularly applied to IE training data generation
   - Source: https://arxiv.org/abs/2411.15100

**Zero-Shot Event Argument Extraction with Structured Constraints:**

4. **Multi-Agent Collaboration Framework for Zero-Shot Document-Level EAE**
   - Uses Generate-Evaluate-Refine paradigm with event structure constraints
   - Incorporates reward signals based on schema compliance
   - Published early 2026
   - Source: https://arxiv.org/html/2603.02909v2

5. **BiTer: Bi-directional Feature Learning for Zero-Shot EAE**
   - Addresses context generation bias
   - Enables bi-directional knowledge transfer
   - Published 2025

6. **Boundary-Aware LLM Augmentation for Event Argument Extraction** - EACL 2026
   - Compares argument replacement, adjunction rewriting, and annotation generation strategies
   - Uses GPT-4o-Mini and DeepSeek-R1-7B for data generation
   - Published at ACL 2026: https://aclanthology.org/2026.eacl-long.230/

7. **LLM-Based Partitioning Extraction (LLM-PEE)** - EMNLP 2025
   - Addresses massive event types by partitioning extraction
   - Uses schema recall and partitioning for long-context scenarios
   - Source: https://arxiv.org/abs/2503.02628

8. **Code4Struct: Code Generation for Few-Shot Structured Prediction**
   - Uses code generation paradigm for structured extraction tasks

**Broader Context:**

9. **Event Extraction in Large Language Model: A Holistic Survey** (December 2024)
   - Comprehensive survey covering methods, modalities, and future directions
   - Source: https://arxiv.org/html/2512.19537v1

10. **A Survey of Generative Information Extraction** - COLING 2025
    - Reviews generative approaches to IE with structured outputs
    - Source: https://aclanthology.org/2025.coling-main.324.pdf

**Key Takeaway:** The Agent-Event-Coder (AEC) framework appears to be the most directly relevant competitor using code/structured generation for zero-shot event extraction, recently accepted to AAAI 2026. It uses similar schema representation principles but with a code-generation rather than pure grammar-constraint approach.

Sources:
- [ASEE arXiv Abstract](https://arxiv.org/abs/2505.08690)
- [ASEE HTML Version](https://arxiv.org/html/2505.08690)
- [Agent-Event-Coder (AEC)](https://arxiv.org/abs/2511.13118)
- [XGrammar](https://arxiv.org/abs/2411.15100)
- [Grammar-constrained Decoding for Structured IE](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full)
- [Zero-Shot Multi-Agent EAE](https://arxiv.org/html/2603.02909v2)
- [Boundary-Aware LLM Augmentation](https://aclanthology.org/2026.eacl-long.230/)
- [LLM-Based Partitioning Extraction](https://arxiv.org/abs/2503.02628)
- [Event Extraction LLM Survey](https://arxiv.org/html/2512.19537v1)
- [Generative IE Survey](https://aclanthology.org/2025.coling-main.324.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bce74ec-2dbe-4a5e-8fb4-27c6d545d7f1",
  "isSidechain": true,
  "agentId": "a18db8a46d5575d85",
  "requestId": "req_011CathWAyx3h6M3W3EdQEWG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "06b339c1-2fc5-41fe-afec-a3b741206fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "463e5fa5-38e0-4ede-baf8-cbc603cf470f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LVB1xW39JykED9aS53Wfuo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1399,
      "cache_read_input_tokens": 25949,
      "output_tokens": 1510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1399
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1510,
          "cache_read_input_tokens": 25949,
          "cache_creation_input_tokens": 1399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1399,
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
