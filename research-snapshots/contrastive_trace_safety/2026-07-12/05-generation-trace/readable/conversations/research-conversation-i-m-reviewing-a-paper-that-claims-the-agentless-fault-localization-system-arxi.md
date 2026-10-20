# Research conversation: I'm reviewing a paper that claims the Agentless fault localization system (arXiv 2407.01489) uses ONLY (a) LLM prompting

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae04fa138714712c8.jsonl`
- **Structured JSON:** [`e4609ccee0d3f82a5705.json`](../../sessions/e4/e4609ccee0d3f82a5705.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-10T08:07:36.718Z_

I'm reviewing a paper that claims the Agentless fault localization system (arXiv 2407.01489) uses ONLY (a) LLM prompting over repo folder tree and (b) embedding-based cosine similarity retrieval (OpenAI text-embedding-3-small via LlamaIndex). The paper claims BM25 appears ONLY in the "agentless RAG baseline" comparison, not the main pipeline.

Please:
1. Fetch https://arxiv.org/abs/2407.01489 to find the abstract and methodology description
2. Try to fetch https://arxiv.org/html/2407.01489 to read the actual paper text about their fault localization approach
3. Search "Agentless demystifying LLM software engineering fault localization BM25 embedding" 
4. Search "SWE-bench-Live Agentless baseline results 2026 arxiv 2505.23419"
5. Fetch https://arxiv.org/abs/2505.23419 to check if Table 3 actually reports Agentless at 11.67%/12.00%/13.33% on SWE-bench-Live Lite

Report exactly what the Agentless paper says about its retrieval/localization approach - specifically whether BM25 is part of the main pipeline or just a baseline comparison. Also report what SWE-bench-Live says about Agentless performance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1b96785b-8c6c-4d64-b557-4da570f44533",
  "agentId": "ae04fa138714712c8",
  "type": "user",
  "uuid": "0301025b-f9ab-49b5-bf95-a5f524acb178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T08:07:37.829Z_

I'll help you verify these claims about the Agentless fault localization system. Let me search for and fetch these papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0301025b-f9ab-49b5-bf95-a5f524acb178",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYav28gdymaJSHqanqw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ff1026a-b602-4b9b-880d-c854f6aa44ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H6vMNx6Q7FtDLqcf7bSd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 757,
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

_source line 3 · 2026-05-10T08:07:38.371Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LP9dCSBCcDqEKBbjKxPsxo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.01489",
  "prompt": "What is the abstract and what does it say about the fault localization methodology? What retrieval methods are mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ff1026a-b602-4b9b-880d-c854f6aa44ba",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYav28gdymaJSHqanqw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "66719671-4f58-45e8-a5df-7166c800dbfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H6vMNx6Q7FtDLqcf7bSd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 757,
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

_source line 4 · 2026-05-10T08:07:38.893Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JJDs5PohR1PrmAWeQKKti3`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.01489",
  "prompt": "Describe the fault localization approach. What retrieval methods are used? Is BM25 part of the main pipeline or only in baselines?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66719671-4f58-45e8-a5df-7166c800dbfc",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYav28gdymaJSHqanqw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92e8dd59-8f54-4370-bb50-83755419b42c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H6vMNx6Q7FtDLqcf7bSd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 757,
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

_source line 5 · 2026-05-10T08:07:38.899Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017BpAUpwRwdkWJGRUhFRNXB`</summary>

```json
{
  "query": "Agentless demystifying LLM software engineering fault localization BM25 embedding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92e8dd59-8f54-4370-bb50-83755419b42c",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYav28gdymaJSHqanqw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "77e111f9-acd5-4776-97a0-251dab5e9d3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H6vMNx6Q7FtDLqcf7bSd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 757,
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

_source line 6 · 2026-05-10T08:07:39.194Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JjdN42N35pE2sfweVgNBZB`</summary>

```json
{
  "query": "SWE-bench-Live Agentless baseline results 2026 arxiv 2505.23419"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77e111f9-acd5-4776-97a0-251dab5e9d3a",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYav28gdymaJSHqanqw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e18d1b7-7622-4af9-a475-d46155588e5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H6vMNx6Q7FtDLqcf7bSd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 757,
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

_source line 7 · 2026-05-10T08:07:39.445Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01St68Tenocdpiwh5cMY3ihs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.23419",
  "prompt": "What does Table 3 report about Agentless performance on SWE-bench-Live Lite? What are the specific percentages reported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e18d1b7-7622-4af9-a475-d46155588e5d",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYav28gdymaJSHqanqw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "619b7ea9-8035-49dc-bc69-0e85815b976a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H6vMNx6Q7FtDLqcf7bSd7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 13791,
      "output_tokens": 439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 439,
          "cache_read_input_tokens": 13791,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 757,
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

_source line 8 · 2026-05-10T08:07:41.591Z_

<details><summary>↩ Tool result · `toolu_01LP9dCSBCcDqEKBbjKxPsxo`</summary>

```text
# Abstract Summary

The abstract describes "Agentless," a simplified approach to automated software development that challenges the necessity of complex autonomous agents. According to the paper, it "employs a simplistic three-phase process of localization, repair, and patch validation" without requiring the LLM to make autonomous decisions or use complex tools.

## Fault Localization Methodology

The abstract does not provide specific details about the fault localization methodology beyond mentioning it as the first phase in their three-step approach.

## Retrieval Methods

The provided content does not mention any specific retrieval methods. The abstract focuses on the overall system architecture and performance benchmarks rather than detailing the retrieval techniques employed within each phase of the process.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66719671-4f58-45e8-a5df-7166c800dbfc",
  "isSidechain": true,
  "promptId": "1b96785b-8c6c-4d64-b557-4da570f44533",
  "agentId": "ae04fa138714712c8",
  "type": "user",
  "uuid": "1c8640b9-8bc8-4abc-8c41-8fa7285c79d7",
  "sourceToolAssistantUUID": "66719671-4f58-45e8-a5df-7166c800dbfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T08:07:41.763Z_

<details><summary>↩ Tool result · `toolu_01St68Tenocdpiwh5cMY3ihs`</summary>

```text
I cannot provide information about Table 3's specific data on Agentless performance metrics because the web page content provided does not include the actual table or detailed numerical results. 

The page only shows the paper's abstract, which mentions that "SWE-bench-Live facilitates rigorous, contamination-resistant evaluation of LLMs and agents" and references "a substantial performance gap compared to static benchmarks," but it does not contain the specific percentages or detailed findings from Table 3.

To access this information, you would need to view the full PDF or HTML version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "619b7ea9-8035-49dc-bc69-0e85815b976a",
  "isSidechain": true,
  "promptId": "1b96785b-8c6c-4d64-b557-4da570f44533",
  "agentId": "ae04fa138714712c8",
  "type": "user",
  "uuid": "d5717dfa-0708-4d7d-a710-800ea99240de",
  "sourceToolAssistantUUID": "619b7ea9-8035-49dc-bc69-0e85815b976a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T08:07:44.358Z_

<details><summary>↩ Tool result · `toolu_01JJDs5PohR1PrmAWeQKKti3`</summary>

```text
# Agentless Fault Localization Approach

## Hierarchical Localization Strategy

Agentless employs a three-step hierarchical process rather than direct end-to-end localization:

1. **File-level localization** - Narrows down to suspicious files
2. **Element localization** - Identifies relevant classes and functions
3. **Edit location localization** - Pinpoints specific code regions for modification

## Retrieval Methods Used

The approach combines two complementary techniques:

**Prompting-based retrieval**: The system constructs a repository structure (similar to Linux's `tree` command) and prompts the LLM to identify top N suspicious files based on filenames and directory organization.

**Embedding-based retrieval**: The system filters irrelevant folders first, chunks remaining files, computes embeddings using OpenAI's text-embedding-3-small model, and retrieves files with highest cosine similarity to the issue description.

These methods are merged by selecting "top N most common files localized by both" approaches, achieving 81.67% ground truth file containment according to ablation studies.

## BM25 Usage

BM25 appears **only in baselines**, not in Agentless's main pipeline. The paper mentions it in the context of a simple RAG baseline: "the agentless baseline uses the LLM to directly generate a patch file by providing it with the file content of the most relevant files, retrieved using BM25."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92e8dd59-8f54-4370-bb50-83755419b42c",
  "isSidechain": true,
  "promptId": "1b96785b-8c6c-4d64-b557-4da570f44533",
  "agentId": "ae04fa138714712c8",
  "type": "user",
  "uuid": "d6c8cdc3-e9f1-40f4-b53b-024766d39f0f",
  "sourceToolAssistantUUID": "92e8dd59-8f54-4370-bb50-83755419b42c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T08:07:45.296Z_

<details><summary>↩ Tool result · `toolu_01JjdN42N35pE2sfweVgNBZB`</summary>

```text
Web search results for query: "SWE-bench-Live Agentless baseline results 2026 arxiv 2505.23419"

Links: [{"title":"[2505.23419] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"arXiv:2505.23419v2 [cs.SE] 1 Jun 2025 SWE-bench Goes Live! Linghao Zhang","url":"https://arxiv.org/pdf/2505.23419"},{"title":"GitHub - microsoft/SWE-bench-Live: [NeurIPS 2025 D&B] 🚀 SWE-bench Goes Live!","url":"https://github.com/microsoft/SWE-bench-Live"},{"title":"arXiv:2505.23419v1 [cs.SE] 29 May 2025 SWE-bench Goes Live! Linghao Zhang1∗","url":"https://arxiv.org/pdf/2505.23419v1"},{"title":"[2505.23419v2] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419v2"},{"title":"Paper page - SWE-bench Goes Live!","url":"https://huggingface.co/papers/2505.23419"},{"title":"[2505.23419v1] SWE-bench Goes Live!","url":"https://arxiv.org/abs/2505.23419v1"},{"title":"Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation","url":"https://arxiv.org/html/2510.08996v4"},{"title":"SWE-Universe: Scale Real-World Verifiable Environments to Millions","url":"https://arxiv.org/html/2602.02361v1"}]

I found information about the SWE-bench-Live paper (arxiv 2505.23419). Here's what I found:

## SWE-bench-Live Overview

SWE-bench-Live is a live-updatable benchmark with an initial release including 1,319 tasks derived from real GitHub issues created since 2024, spanning 93 repositories. Each task is accompanied by a dedicated Docker image to ensure reproducible execution.

## Agentless Baseline Evaluation

For Agentless evaluation, the researchers followed the original pipeline consisting of issue localization and patch generation stages, but omitted the reranking stage based on regression testing. Both the localization and repair stages in their Agentless evaluation produce a single sample without reranking.

The agents were tested using four recent state-of-the-art LLMs: GPT-4o (gpt-4o-2024-11-20), GPT-4.1 (gpt-4.1-2025-04-14), Claude 3.7 Sonnet (claude-3-7-sonnet-20250219), and DeepSeek V3 (DeepSeek-V3-0324).

The paper was published on June 1, 2025, and represents a significant advancement in software engineering agent evaluation by using continuously updated real-world bugs rather than static datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e18d1b7-7622-4af9-a475-d46155588e5d",
  "isSidechain": true,
  "promptId": "1b96785b-8c6c-4d64-b557-4da570f44533",
  "agentId": "ae04fa138714712c8",
  "type": "user",
  "uuid": "7c9add10-4275-4dac-b9b1-f5ced138bb55",
  "sourceToolAssistantUUID": "1e18d1b7-7622-4af9-a475-d46155588e5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T08:07:47.372Z_

<details><summary>↩ Tool result · `toolu_017BpAUpwRwdkWJGRUhFRNXB`</summary>

```text
Web search results for query: "Agentless demystifying LLM software engineering fault localization BM25 embedding"

Links: [{"title":"AGENTLESS : Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/pdf/2407.01489"},{"title":"[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044"},{"title":"Demystifying LLM-Based Software Engineering Agents | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/abs/10.1145/3715754"},{"title":"Paper page - Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://huggingface.co/papers/2407.01489"},{"title":"Demystifying LLM-Based Software Engineering Agents","url":"https://www.researchgate.net/publication/392847739_Demystifying_LLM-Based_Software_Engineering_Agents"},{"title":"(PDF) Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://www.researchgate.net/publication/381911059_Agentless_Demystifying_LLM-based_Software_Engineering_Agents"},{"title":"GitHub - FudanSELab/Agent4SE-Paper-List: Repository for the paper \"Large Language Model-Based Agents for Software Engineering: A Survey\". Keep updating. · GitHub","url":"https://github.com/FudanSELab/Agent4SE-Paper-List"},{"title":"Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://www.emergentmind.com/papers/2407.01489"},{"title":"Enhancing LLM-based Fault Localization with a Functionality-Aware Retrieval-Augmented Generation Framework","url":"https://arxiv.org/html/2509.20552"}]

Based on the search results, here's what I found about your query:

## Agentless: Demystifying LLM-based Software Engineering Agents

The search results primarily return information about **Agentless**, a research paper that addresses LLM-based software engineering fault localization.

### Key Findings:

**Overview:** Agentless employs a simplistic three-phase process of localization, repair, and patch validation, without letting the LLM decide future actions or operate with complex tools.

**Fault Localization Approach:** AGENTLESS's localization process makes uses of both LLM-based localization as well classic information-retrieval-based localization idea. In the localization process, Agentless employs a hierarchical process to first localize the fault to specific files, then to relevant classes or functions, and finally to fine-grained edit locations.

**Embedding and BM25 Usage:** To complement the prompting-based localization (using file names only), AGENTLESS also uses a simple embedding-based retrieval method to identify additional suspicious files. However, instead of embedding all files in the repository, AGENTLESS first filters out irrelevant folders. After removing all files from these irrelevant folders, AGENTLESS divides each remaining file into chunks of code segments and computes the embedding for each chunk using an embedding model. AGENTLESS then embeds the original issue description (i.e., the query) and computes the cosine similarity between the resulting query embedding and each chunk embedding to retrieve a list of relevant files.

**Performance:** On the popular SWE-bench Lite benchmark, Agentless achieved both the highest performance (32.00%, 96 correct fixes) and low cost ($0.70) compared with all existing open-source software agents!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77e111f9-acd5-4776-97a0-251dab5e9d3a",
  "isSidechain": true,
  "promptId": "1b96785b-8c6c-4d64-b557-4da570f44533",
  "agentId": "ae04fa138714712c8",
  "type": "user",
  "uuid": "14f0cb5d-cc2c-4053-b6f4-f244779aba10",
  "sourceToolAssistantUUID": "77e111f9-acd5-4776-97a0-251dab5e9d3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T08:07:48.906Z_

Let me fetch the full HTML version of the SWE-bench-Live paper to get Table 3 details:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f0cb5d-cc2c-4053-b6f4-f244779aba10",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYbhd2taxosdw9CtRa8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "15b55340-f34c-4a0b-a80e-71967b0998c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kmo81sUwSor5tnXAXcLi53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 997,
      "cache_creation_input_tokens": 2758,
      "cache_read_input_tokens": 14548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2758,
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

_source line 14 · 2026-05-10T08:07:49.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BLBa2gkAwzGjJ87jzG3kyN`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.23419v2",
  "prompt": "What does Table 3 show? What are the specific performance percentages reported for Agentless on SWE-bench-Live Lite?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15b55340-f34c-4a0b-a80e-71967b0998c2",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYbhd2taxosdw9CtRa8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37d78a46-35b9-4c01-87b4-8107cf5bb1a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kmo81sUwSor5tnXAXcLi53",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 997,
      "cache_creation_input_tokens": 2758,
      "cache_read_input_tokens": 14548,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2758
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 997,
          "output_tokens": 142,
          "cache_read_input_tokens": 14548,
          "cache_creation_input_tokens": 2758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2758,
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

_source line 15 · 2026-05-10T08:07:53.170Z_

<details><summary>↩ Tool result · `toolu_01BLBa2gkAwzGjJ87jzG3kyN`</summary>

```text
# Table 3 Analysis

Table 3 presents "Performance on SWE-bench-Live (Lite subset)" and displays results across three agent frameworks paired with four different language models.

## Agentless Performance Metrics

For the Agentless agent specifically, the table reports:

- **GPT-4o**: Resolved 11.67%, Apply 91.67%, Localization Success 37.67%
- **GPT-4.1**: Resolved 12.00%, Apply 84.33%, Localization Success 39.00%
- **Claude 3.7 Sonnet**: Resolved 11.33%, Apply 68.00%, Localization Success 30.00%
- **DeepSeek V3**: Resolved 13.33%, Apply 83.33%, Localization Success 40.67%

The highest performance for Agentless came with DeepSeek V3, achieving a 13.33% resolved rate. Notably, Agentless generally showed lower resolved rates compared to the other two agent frameworks (OpenHands and SWE-Agent) across most model pairings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37d78a46-35b9-4c01-87b4-8107cf5bb1a8",
  "isSidechain": true,
  "promptId": "1b96785b-8c6c-4d64-b557-4da570f44533",
  "agentId": "ae04fa138714712c8",
  "type": "user",
  "uuid": "ee06467c-cf69-4394-924f-f89521825866",
  "sourceToolAssistantUUID": "37d78a46-35b9-4c01-87b4-8107cf5bb1a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T08:08:00.558Z_

Perfect! I now have all the information needed. Let me compile my findings:

## Summary of Findings

### Agentless Fault Localization Approach (arXiv 2407.01489)

**The paper's claim about retrieval methods is ACCURATE:**

The Agentless paper confirms that the main pipeline uses **ONLY two approaches**:

1. **LLM Prompting over repository structure**: The system constructs a repository folder tree (similar to Linux `tree` command) and prompts the LLM to identify the top N suspicious files based on filenames and directory organization.

2. **Embedding-based cosine similarity retrieval**: The system filters irrelevant folders first, chunks remaining files, computes embeddings using OpenAI's text-embedding-3-small model, and retrieves files with highest cosine similarity to the issue description.

**BM25 usage is correctly characterized**: BM25 appears **ONLY in the baseline comparisons**, not in the main Agentless pipeline. The paper explicitly states: "the agentless baseline uses the LLM to directly generate a patch file by providing it with the file content of the most relevant files, retrieved using BM25."

The Agentless approach then merges both main techniques by selecting "top N most common files localized by both approaches," achieving 81.67% ground truth file containment according to ablation studies.

### SWE-bench-Live Performance (arXiv 2505.23419)

**Table 3 reports exactly as claimed:**

The table "Performance on SWE-bench-Live (Lite subset)" reports Agentless performance:
- **GPT-4o**: 11.67% resolved
- **GPT-4.1**: 12.00% resolved  
- **Claude 3.7 Sonnet**: 11.33% resolved
- **DeepSeek V3**: 13.33% resolved

These match the claimed percentages (11.67%/12.00%/13.33%) from your review. The paper notes that Agentless showed lower resolved rates compared to the other two agent frameworks (OpenHands and SWE-Agent) across most model pairings.

---

**Sources:**
- [Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489)](https://arxiv.org/abs/2407.01489)
- [Agentless HTML Version](https://arxiv.org/html/2407.01489)
- [SWE-bench Goes Live! (arXiv 2505.23419)](https://arxiv.org/abs/2505.23419)
- [SWE-bench Goes Live! HTML Version](https://arxiv.org/html/2505.23419v2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee06467c-cf69-4394-924f-f89521825866",
  "isSidechain": true,
  "agentId": "ae04fa138714712c8",
  "requestId": "req_011CatYc9BvWyNb7V6Eqwz7t",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "90e21466-d661-4328-af18-db0dd67c4006",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73ab0c9c-85f6-4d42-ac57-ef6596febe2c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KACAWapiSyvPX3J9zZ3oNA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1403,
      "cache_read_input_tokens": 17306,
      "output_tokens": 648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1403
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 648,
          "cache_read_input_tokens": 17306,
          "cache_creation_input_tokens": 1403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1403,
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
